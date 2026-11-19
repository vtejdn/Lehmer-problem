"""Enumerate small reciprocal measures by congruences and reflected trace bounds."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from functools import cache
import importlib.util
import json
from math import prod
from pathlib import Path
import runpy
import subprocess
from tempfile import TemporaryDirectory


HERE = Path(__file__).resolve().parent
GROUP = HERE.parents[1]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions"
R = Fraction(1091, 1000)
LAST = 120
DEGREES = tuple(range(86, 111, 2))
CUTOFFS = {86: Fraction(521, 500), 88: Fraction(26, 25), 90: Fraction(259, 250),
           **{d: Fraction(1027, 1000) for d in range(92, 100, 2)}, 100: Fraction(511, 500)}
FIELDS = ("representatives", "first_reflected", "nine_reflected", "endpoint_zero",
          "later_trace_exclusion", "quadratic_cyclotomic", "exact_division")


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


previous = module_at("asymmetric_census", HERE.parent / "v12" / "sieve.py")


@cache
def chord_rows():
    boxes = json.loads((OUTPUT / "v7" / "boxes.json").read_text())
    scale = runpy.run_path(str(GROUP / "trace_bounds.py"))["LOG_SCALE"]
    rows = []
    for name, data in boxes.items():
        for j, row in enumerate(data["certificates"], 1):
            if row["unit"]["k"] != 0 or row["outer"]["k"] != j:
                raise ArithmeticError("The v7 radii are inconsistent.")
            rows.append((int(name), j, row["unit"]["upper"], row["outer"]["upper"]))
    return rows, scale


@cache
def log_ratio(cutoff):
    target = cutoff**10000
    lo, hi = 0, 10000
    if R**hi < target:
        raise ValueError("Cutoff outside the chord bracket.")
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if R**mid >= target:
            hi = mid
        else:
            lo = mid
    return Fraction(hi, 10000)


def trace_bounds(degree, cutoff):
    rows, scale = chord_rows()
    ratio = log_ratio(cutoff)
    bounds, choices = [], []
    for k in range(1, LAST + 1):
        # The unweighted reciprocal bound covers radii beyond the v7 grid.
        candidates = [((degree-2 + cutoff**k + cutoff**-k)*scale, 0, 0)]
        for name, j, u, v in rows:
            if R**j >= cutoff**k:
                position = min(1, ratio*k/j)
                candidates.append((degree//2 * u + position*max(0, v-u), name, j))
        cap, name, j = min(candidates)
        bounds.append(int(cap // scale))
        choices.append((name, j))
    return bounds, choices


def configuration(degree, limits):
    coefficients = [1]
    for k in range(1, degree//2+1):
        coefficients.append(sum(coefficients[k-j]*limits[j-1] for j in range(1, k+1))//k)
    norm = 2*sum(coefficients)
    if norm*(degree+max(limits)) >= 2**63 or max(limits)*degree**2 >= 2**31:
        raise ArithmeticError("The uniform numerator or congruence bound exceeds its type.")
    bound = prod((2*b+k)//k for k, b in enumerate(limits[:degree//2], 1))
    if bound >= 2**63:
        raise ArithmeticError("Native counters might overflow.")
    return " ".join(map(str, [0, *limits]))


def cutoff_for(degree):
    return CUTOFFS.get(degree, Fraction(51, 50))


def write_json(path, data):
    with TemporaryDirectory(dir=path.parent) as folder:
        pending = Path(folder) / "result.json"
        pending.write_text(json.dumps(data, indent=2) + "\n", encoding="ascii")
        pending.replace(path)


def native_subtree(degree, prefix, command, caps, path):
    raw = subprocess.check_output([*command, caps, path, str(degree), *map(str, prefix)], text=True)
    counts = list(map(int, raw.split()))
    halves = [list(map(int, row.split())) for row in path.read_text().splitlines()]
    if len(counts) != len(FIELDS) or counts[2] != sum(counts[3:]) or counts[-1] != len(halves):
        raise ArithmeticError("Native counts and survivor file disagree.")
    return dict(zip(FIELDS, counts)), halves


def run_slice(degree, prefix, command, caps, dest, classify):
    with TemporaryDirectory(dir=dest) as folder:
        counts, halves = native_subtree(degree, prefix, command, caps, Path(folder) / "survivors.txt")
        rows, witnesses, unresolved = classify(halves)
        result = {"prefix": prefix, "counts": counts,
                  "rows": rows, "witnesses": witnesses, "unresolved": unresolved}
        pending = Path(folder) / "report.json"
        pending.write_text(json.dumps(result, separators=(",", ":"))+"\n", encoding="ascii")
        pending.replace(dest / ("slice_" + "_".join(map(str, prefix)) + ".json"))
        return result


def enumerate_degree(degree, workers, command):
    cutoff = cutoff_for(degree)
    previous.CUTOFFS[degree] = cutoff
    classify = previous.Census(degree).classify
    dest = OUTPUT / "v13" / f"d{degree}"
    dest.mkdir(exist_ok=True, parents=True)
    limits, choices = trace_bounds(degree, cutoff)
    bounds = limits[:degree//2]
    pairs = [(x, y) for x in range(bounds[0]+1) for y in range(-bounds[1], bounds[1]+1)
             if (x-y) % 2 == 0]
    previous.division_tables(degree)
    with TemporaryDirectory(dir=dest) as folder:
        caps = Path(folder) / "limits.txt"
        caps.write_text(configuration(degree, limits), encoding="ascii")
        with ThreadPoolExecutor(max_workers=workers) as pool:
            reports = pool.map(lambda pair: run_slice(degree, pair, command, caps, dest, classify), pairs)
            totals, labels = Counter(), Counter()
            for report in reports:
                totals.update(report["counts"])
                labels.update(row["classification"] for row in report["rows"])
    write_json(dest / "census.json", {"degree": degree, "cutoff": [cutoff.numerator, cutoff.denominator], "bounds": limits,
               "source_rows": choices, "counts": dict(totals), "classifications": dict(labels)})
    print(degree, dict(totals), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, nargs="+", choices=DEGREES, default=DEGREES)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("A positive number of workers is required.")
    dest = OUTPUT / "v13"
    dest.mkdir(exist_ok=True, parents=True)
    with TemporaryDirectory(dir=dest) as folder:
        compiler = previous.load_driver("v10")
        compiler.HERE = HERE
        command = compiler.compile_worker(Path(folder))
        for degree in args.degree:
            enumerate_degree(degree, args.workers, command)


if __name__ == "__main__":
    main()
