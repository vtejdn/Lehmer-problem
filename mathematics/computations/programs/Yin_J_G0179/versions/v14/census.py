"""Enumerate the degree-72 reciprocal box at measure 267/250."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction
from pathlib import Path
import sys
from tempfile import TemporaryDirectory


VERSIONS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VERSIONS / "v13"))
import sieve


DEGREE = 72
CUTOFF = Fraction(267, 250)
DEST = sieve.OUTPUT / "v14" / "d72"


def compile_worker(scratch):
    compiler = sieve.previous.load_driver("v10")
    compiler.HERE = VERSIONS / "v13"
    return compiler.compile_worker(scratch)


def enumerate_box(workers):
    limits, choices = sieve.trace_bounds(DEGREE, CUTOFF)
    configuration = sieve.configuration(DEGREE, limits)
    # The v12 classifier takes its Graeffe threshold from this degree table.
    sieve.previous.CUTOFFS[DEGREE] = CUTOFF
    classify = sieve.previous.Census(DEGREE).classify
    sieve.previous.division_tables(DEGREE)
    pairs = [(x, y) for x in range(limits[0]+1) for y in range(-limits[1], limits[1]+1)
             if (x-y) % 2 == 0]
    DEST.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=DEST) as folder:
        scratch = Path(folder)
        command = compile_worker(scratch)
        caps = scratch / "limits.txt"
        caps.write_text(configuration, encoding="ascii")

        def run(pair):
            report = sieve.run_slice(DEGREE, pair, command, caps, DEST, classify)
            return report["counts"], Counter(row["classification"] for row in report["rows"])

        totals, labels = Counter(), Counter()
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for counts, classes in pool.map(run, pairs):
                totals.update(counts)
                labels.update(classes)
    sieve.write_json(DEST / "census.json", {
        "degree": DEGREE, "cutoff": [CUTOFF.numerator, CUTOFF.denominator],
        "bounds": limits, "source_rows": choices, "counts": dict(totals),
        "classifications": dict(labels)})
    print(dict(totals), dict(labels))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("A positive worker count is required.")
    enumerate_box(args.workers)
