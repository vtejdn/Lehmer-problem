"""Enumerate three reciprocal Newton boxes for the strict budget at prime 503."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from pathlib import Path
import sys
from tempfile import TemporaryDirectory

VERSIONS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VERSIONS / "v14"))
from census import compile_worker, sieve

CUTOFFS = {86: Fraction(104902, 100000), 88: Fraction(104116, 100000),
           92: Fraction(102769, 100000)}
OUTPUT = sieve.OUTPUT / "v15"


def enumerate_degree(degree, command, scratch, workers):
    cutoff = CUTOFFS[degree]
    limits, choices = sieve.trace_bounds(degree, cutoff)
    caps = scratch / f"limits{degree}.txt"
    caps.write_text(sieve.configuration(degree, limits), encoding="ascii")
    sieve.previous.CUTOFFS[degree] = cutoff
    classify = sieve.previous.Census(degree).classify
    sieve.previous.division_tables(degree)
    dest = OUTPUT / f"d{degree}"
    dest.mkdir(exist_ok=True)
    pairs = [(x, y) for x in range(limits[0]+1) for y in range(-limits[1], limits[1]+1)
             if (x-y) % 2 == 0]

    def run_pair(pair):
        report = sieve.run_slice(degree, pair, command, caps, dest, classify)
        return report["counts"], Counter(row["classification"] for row in report["rows"])

    totals, labels = Counter(), Counter()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for counts, classes in pool.map(run_pair, pairs):
            totals.update(counts)
            labels.update(classes)
    sieve.write_json(dest / "census.json", {
        "degree": degree, "cutoff": [cutoff.numerator, cutoff.denominator],
        "bounds": limits, "source_rows": choices, "counts": dict(totals),
        "classifications": dict(labels)})
    print(degree, dict(totals), dict(labels), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--degree", type=int, nargs="+", choices=CUTOFFS, default=list(CUTOFFS))
    args = parser.parse_args()
    if args.workers <= 0:
        parser.error("A positive worker count is required.")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=OUTPUT) as folder:
        scratch = Path(folder)
        command = compile_worker(scratch)
        for d in args.degree:
            enumerate_degree(d, command, scratch, args.workers)
