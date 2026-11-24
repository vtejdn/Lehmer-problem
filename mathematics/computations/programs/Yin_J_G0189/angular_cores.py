"""Count the unit-circle inverse pairs in the complete degree-44 catalogue."""

from collections import Counter
from pathlib import Path
import sys


PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0188"))
from radial_cores import signature, table_rows, trace_from_half


def main():
    counts = Counter()
    minimum_rows = []
    minimum = None
    for line, degree, _, _, polynomial in table_rows():
        if degree > 44:
            continue
        trace = trace_from_half(polynomial[:degree // 2 + 1])
        _, (_, inside, _, _) = signature(trace)
        counts[inside] += 1
        if minimum is None or inside < minimum:
            minimum = inside
            minimum_rows = []
        if inside == minimum:
            minimum_rows.append((line, degree))

    if sum(counts.values()) != 944 or minimum != 3:
        raise ArithmeticError(f"Unexpected catalogue result: {counts}")
    print(f"Rows checked: {sum(counts.values())}")
    print(f"Minimum circle inverse pairs: {minimum}")
    print(f"Minimizing (source line, degree): {minimum_rows}")
    print(f"Counts by circle inverse pairs: {dict(sorted(counts.items()))}")


if __name__ == "__main__":
    main()
