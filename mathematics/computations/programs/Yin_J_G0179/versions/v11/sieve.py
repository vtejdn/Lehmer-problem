"""Enumerate small reciprocal measures using the certified v7 ellipse maxima."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
import importlib.util
import json
from math import comb
from pathlib import Path
import runpy
import subprocess
from tempfile import TemporaryDirectory
from time import monotonic


HERE = Path(__file__).resolve().parent
GROUP = HERE.parents[1]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions"
T = Fraction(53, 50)
LARGER_RADIUS = Fraction(1091, 1000)
DEGREES = tuple(range(68, 85, 2))
LOG_RATIO_UPPER = Fraction(6691, 10000)
MAX_TRACE = 120

# The v10 compiler and exact final classification accept their native source
# directory and rational cutoff through module parameters.
spec = importlib.util.spec_from_file_location("reciprocal_v10", HERE.parent / "v10" / "sieve.py")
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)
previous.HERE, previous.T = HERE, T
compile_worker, fallback, FIELDS = previous.compile_worker, previous.fallback, previous.FIELDS


def box(degree):
    source = json.loads((OUTPUT / "v7" / "boxes.json").read_text())
    scale = runpy.run_path(str(GROUP / "trace_bounds.py"))["LOG_SCALE"]
    count = runpy.run_path(str(GROUP / "count_prefixes.py"))["full_reciprocal_box"]
    h = degree // 2
    if T**LOG_RATIO_UPPER.denominator > LARGER_RADIUS**LOG_RATIO_UPPER.numerator:
        raise ArithmeticError("The rational logarithm-ratio certificate failed.")
    selections = []
    for k in range(1, h + 1):
        choices = []
        for name in ("64", "66"):
            for j, row in enumerate(source[name]["certificates"], 1):
                if row["unit"]["k"] != 0 or row["outer"]["k"] != j:
                    raise ValueError("Unexpected radius in v7 certificate")
                if LARGER_RADIUS ** j >= T ** k:
                    unit, outer = row["unit"]["upper"], row["outer"]["upper"]
                    if degree <= 72:
                        bound = (h - 1) * unit + outer
                    else:
                        fraction = min(Fraction(1), LOG_RATIO_UPPER * k / j)
                        bound = h * unit + fraction * max(0, outer - unit)
                    choices.append((bound, name, j))
        bound, name, j = min(choices)
        choice = {"k": k, "source_degree": int(name), "source_layer": j,
                  "upper_numerator": bound.numerator, "bound": bound // scale}
        if degree > 72:
            choice["upper_denominator"] = bound.denominator
        selections.append(choice)
    result = count(degree, [selection["bound"] for selection in selections])
    result["ellipse_selections"] = selections
    return result


def arithmetic(degree, bounds):
    h = degree // 2
    if len(bounds) != h:
        raise ValueError("A bound is required for every first-half trace.")
    coeff = [1]
    first = []
    for k in range(1, h + 1):
        numerator = sum(coeff[k - j] * bounds[j - 1] for j in range(1, k + 1))
        first.append(numerator)
        coeff.append(numerator // k)
    full = coeff + coeff[-2::-1]
    limits = [0, *bounds, *(int(degree - 2 + T**k + T**-k) for k in range(h + 1, MAX_TRACE + 1))]
    reflected = []
    for k in range(h + 1, MAX_TRACE + 1):
        total = k * full[k] if k <= degree else 0
        reflected.append(total + sum(full[i] * limits[k - i] for i in range(1, min(k, degree + 1))))
    if max(coeff + limits) >= 2**31 or max(max(first), max(reflected), 2 * sum(full)) >= 2**63:
        raise ArithmeticError("Native types do not cover the exact Newton bounds.")
    evidence = {"coefficient_max": max(coeff), "full_coefficient_sum": sum(full),
                "prefix_numerator_max": max(first), "reflected_numerator_max": max(reflected)}
    return limits, evidence


def configuration(degree, bounds):
    limits, _ = arithmetic(degree, bounds)
    rows = [limits]
    for g in range(1, 11):
        caps = [int(comb(degree, i) * T**(2**g)) for i in range(degree // 2 + 1)]
        rows.append([v if v < 2**63 else -1 for v in caps])
    return "\n".join(" ".join(map(str, row)) for row in rows) + "\n"


def run_slice(degree, prefix, command, config, audit, dest):
    # The direct recurrence is identical for audit prefixes and exhaustive slices.
    name = "slice_" + "_".join(map(str, prefix))
    with TemporaryDirectory(dir=dest) as folder:
        survivors = Path(folder) / "survivors.txt"
        raw = subprocess.check_output([*command, config, survivors, str(degree), *map(str, prefix)], text=True)
        numbers = list(map(int, raw.split()))
        rows = [list(map(int, line.split())) for line in survivors.read_text().splitlines()]
        if len(numbers) != len(FIELDS) or numbers[2] != sum(numbers[3:]) or len(rows) != numbers[-1]:
            raise ArithmeticError("Native counts and survivor file disagree.")
        labels, unresolved, witnesses = fallback(degree, rows) if rows else ({}, [], [])
        result = {"degree": degree, "cutoff": [T.numerator, T.denominator], "prefix": list(prefix),
                  "counts": dict(zip(FIELDS, numbers)), "fallback_classifications": labels,
                  "exact_witnesses": witnesses, "unresolved": unresolved}
        report = Path(folder) / "report.json"
        report.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
        report.replace(dest / (name + ".json"))
        return result


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--degree", type=int, choices=DEGREES, nargs="+", default=list(DEGREES))
    cli.add_argument("--workers", type=int, default=1)
    cli.add_argument("--prefix", type=int, nargs="+")
    args = cli.parse_args()
    if args.workers < 1:
        cli.error("A positive worker count is required.")
    dest = OUTPUT / "v11"
    dest.mkdir(exist_ok=True, parents=True)
    with TemporaryDirectory(dir=dest) as folder:
        scratch = Path(folder)
        command = compile_worker(scratch)
        for degree in args.degree:
            path = dest / f"d{degree}"
            path.mkdir(exist_ok=True)
            source = box(degree)
            bounds = source["bounds"]
            source["arithmetic"] = arithmetic(degree, bounds)[1]
            (path / "boxes.json").write_text(json.dumps(source, indent=2) + "\n", encoding="ascii")
            config = scratch / f"limits_{degree}.txt"
            config.write_text(configuration(degree, bounds), encoding="ascii")
            if args.prefix is not None:
                if len(args.prefix) > len(bounds) or any(abs(v) > b for v, b in zip(args.prefix, bounds)):
                    cli.error("Prefix outside the degree's Newton box.")
                prefixes = [args.prefix]
            else:
                prefixes = [(x, y) for x in range(bounds[0], -1, -1) for y in range(-bounds[1], bounds[1] + 1)
                            if (x - y) % 2 == 0]
            start = monotonic()
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                reports = list(pool.map(lambda p: run_slice(degree, p, command, config, False, path), prefixes))
            print(degree, len(reports), "slices,", sum(r["counts"]["representatives"] for r in reports),
                  "representatives,", round(monotonic() - start, 2), "seconds", flush=True)


if __name__ == "__main__":
    main()
