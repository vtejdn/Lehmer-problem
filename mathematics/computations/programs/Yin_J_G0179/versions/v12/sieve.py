"""Classify four Newton boxes at the cutoffs for the two-value test at 251."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import runpy
import subprocess
from tempfile import TemporaryDirectory
from time import monotonic


HERE = Path(__file__).resolve().parent
GROUP = HERE.parents[1]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions"
CUTOFFS = {56: Fraction(2202, 2000), 58: Fraction(2193, 2000),
           68: Fraction(2164, 2000), 70: Fraction(2155, 2000)}
R = Fraction(1091, 1000)


def load_driver(version):
    spec = importlib.util.spec_from_file_location(
        "census_" + version, HERE.parent / version / "sieve.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def box(degree, t):
    source = json.loads((OUTPUT / "v7" / "boxes.json").read_text())
    scale = runpy.run_path(str(GROUP / "trace_bounds.py"))["LOG_SCALE"]
    count = runpy.run_path(str(GROUP / "count_prefixes.py"))["full_reciprocal_box"]
    # Find the least grid majorant of log(t)/log(R) by exact integer powers.
    target = t**10000
    lo, hi = 0, 20000
    if R**hi < target:
        raise ArithmeticError("The logarithm ratio is outside the bracket.")
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if R**mid >= target:
            hi = mid
        else:
            lo = mid
    h = degree // 2
    selections = []
    for k in range(1, h + 1):
        candidates = []
        for name in ("64", "66"):
            for j, row in enumerate(source[name]["certificates"], 1):
                if row["unit"]["k"] != 0 or row["outer"]["k"] != j:
                    raise ValueError("Unexpected v7 certificate radius.")
                if R**j < t**k:
                    continue
                u, v = row["unit"]["upper"], row["outer"]["upper"]
                position = min(1, Fraction(hi * k, 10000 * j))
                candidates.append((h * u + position * max(0, v - u), int(name), j))
        cap, source_degree, layer = min(candidates)
        selections.append({"k": k, "source_degree": source_degree, "source_layer": layer,
                           "cap_numerator": cap.numerator, "cap_denominator": cap.denominator,
                           "bound": cap // scale})
    result = count(degree, [row["bound"] for row in selections])
    result.update(log_ratio_upper=[hi, 10000], ellipse_selections=selections)
    return result


@lru_cache(maxsize=None)
def division_tables(degree):
    finish = runpy.run_path(str(HERE.parent / "v3" / "finish.py"))
    verify = runpy.run_path(str(HERE.parent / "v6" / "verify_totals.py"))
    polynomials = {n: phi for n, phi, _ in finish["cyclotomics"](degree)}
    polynomials.update(verify["remaining_cyclotomics"](degree, finish["divide"]))
    tables = [(n, phi, finish["bit_polynomial"](phi)) for n, phi in polynomials.items()]
    return tables, finish


class Census:
    def __init__(self, degree):
        self.degree = degree
        self.T = CUTOFFS[degree]
        self.HERE, self.OUTPUT = HERE, OUTPUT
        self.fast = degree <= 58
        self.native = load_driver("v10" if self.fast else "v11")
        self.native.T = self.T
        self.FIELDS = self.native.FIELDS
        self.compile_worker = self.native.compile_worker
        self.configuration = self.native.configuration
        self.final = load_driver("v10")
        self.final.T = self.T

    def classify(self, rows):
        classifications, exact, unresolved = [], [], []
        tables, finish = division_tables(self.degree)
        for half in rows:
            full = half + half[-2::-1]
            bits = finish["bit_polynomial"](full)
            for order, phi, bits_phi in tables:
                if finish["bit_remainder"](bits, bits_phi) == 0 and not any(finish["divide"](full, phi)[1]):
                    category = f"phi_{order}"
                    break
            else:
                labels, residual, witnesses = self.final.fallback(self.degree, [half])
                if sum(labels.values()) != 1:
                    raise ArithmeticError("Missing final classification.")
                category = next(iter(labels))
                exact.extend(witnesses)
                unresolved.extend(residual)
            classifications.append({"half": half, "classification": category})
        return classifications, exact, unresolved

    def run_slice(self, degree, prefix, command, config, audit, dest):
        if degree != self.degree:
            raise ValueError("Wrong cutoff for the requested degree.")
        name = "slice_" + "_".join(map(str, prefix))
        with TemporaryDirectory(dir=dest) as folder:
            survivors = Path(folder) / "survivors.txt"
            mode = ["audit" if audit else "search"] if self.fast else []
            args = [*command, config, survivors, *mode, str(degree), *map(str, prefix)]
            raw = list(map(int, subprocess.check_output(args, text=True).split()))
            rows = [list(map(int, line.split())) for line in survivors.read_text().splitlines()]
            if len(raw) != len(self.FIELDS) or raw[2] != sum(raw[3:]) or len(rows) != raw[-1]:
                raise ArithmeticError("Native counts and final rows disagree.")
            classifications, witnesses, unresolved = self.classify(rows)
            labels = Counter(row["classification"] for row in classifications)
            report = {"degree": degree, "cutoff": [self.T.numerator, self.T.denominator],
                      "prefix": list(prefix), "counts": dict(zip(self.FIELDS, raw)),
                      "fallback_classifications": dict(labels), "fallback_rows": classifications,
                      "exact_witnesses": witnesses, "unresolved": unresolved}
            pending = Path(folder) / "report.json"
            pending.write_text(json.dumps(report, separators=(",", ":")) + "\n", encoding="ascii")
            pending.replace(dest / (name + ".json"))
            return report


def configure(degree):
    return Census(degree)


def check_products():
    p, b = 251, 126
    if not (b - 1)**8 < p**7 < b**8:
        raise ArithmeticError("The width does not match the prime.")
    for left, right in [(56, 68), (56, 70), (58, 68)]:
        product = CUTOFFS[left] * CUTOFFS[right]
        if product**(4*p) * (2*p*b + 1)**4 <= 2**p * (p*b + 1)**4:
            raise ArithmeticError("Cutoff product does not cover the prime-251 budget.")


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--degree", nargs="+", type=int, choices=CUTOFFS, default=list(CUTOFFS))
    cli.add_argument("--workers", type=int, default=1)
    args = cli.parse_args()
    if args.workers < 1:
        cli.error("A positive worker count is required.")
    check_products()
    for degree in args.degree:
        run = configure(degree)
        dest = OUTPUT / "v12" / f"d{degree}"
        dest.mkdir(exist_ok=True, parents=True)
        source = box(degree, run.T)
        bounds = source["bounds"]
        (dest / "boxes.json").write_text(json.dumps(source, indent=2) + "\n", encoding="ascii")
        with TemporaryDirectory(dir=dest) as folder:
            scratch = Path(folder)
            caps = scratch / "caps.txt"
            caps.write_text(run.configuration(degree, bounds), encoding="ascii")
            command = run.compile_worker(scratch)
            pairs = [(x, y) for x in range(bounds[0], -1, -1) for y in range(-bounds[1], bounds[1] + 1)
                     if (x - y) % 2 == 0]
            start = monotonic()
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                reports = pool.map(lambda p: run.run_slice(degree, p, command, caps, False, dest), pairs)
                total = sum(r["counts"]["representatives"] for r in reports)
            if total != source["no_power_substitution_up_to_sign"]:
                raise ArithmeticError("Native and tensor box counts disagree.")
            print(degree, total, "representatives,", round(monotonic() - start, 2), "seconds", flush=True)


if __name__ == "__main__":
    main()
