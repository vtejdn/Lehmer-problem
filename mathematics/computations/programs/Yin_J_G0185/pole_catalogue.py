"""Test whether a listed short coordinate can have an integral graph partner."""

from collections import Counter
from math import comb, isqrt
from pathlib import Path
import re


TABLE = (Path(__file__).resolve().parents[3] / "literature" / "pdf" / "Mos26"
         / "AllSmallMeasures_200.txt")


def table_rows():
    started = False
    for line_number, line in enumerate(TABLE.read_text(encoding="utf-8").splitlines(), 1):
        if not started and not re.match(r"^\s*\d+\s+1\.\d+\s+\d+\s", line):
            continue
        if not line.strip():
            continue
        started = True
        degree, measure, exterior, *words = line.split()
        half = tuple(map(int, words))
        if half[0] != 1 or int(degree) != 2*(len(half)-1):
            raise ValueError(f"Invalid reciprocal row on source line {line_number}")
        yield line_number, int(degree), measure, int(exterior), half + half[-2::-1]


def pole_coefficient(coefficients):
    # First nonzero coefficient of Q^D S(1+1/Q) - 1.
    degree = len(coefficients) - 1
    linear = degree + coefficients[1]
    if linear:
        return linear
    for k in range(2, degree + 1):
        value = sum(coefficients[j]*comb(degree-j, k-j) for j in range(k+1))
        if value:
            return value
    raise ValueError("Identically one would require S(X) = (X-1)^D")


def pole_value(coefficients, q):
    result = 1
    q_power = 1
    for c in coefficients[1:]:
        q_power *= q
        result = (q+1)*result + c*q_power
    return result


def main():
    counts = Counter()
    min_linear = None
    max_height = 0
    for line, degree, measure, exterior, original in table_rows():
        counts["rows"] += 1
        if degree <= 44:
            counts["complete-range rows"] += 1
        for sign in (1, -1):
            coefficients = tuple(c * sign**j for j, c in enumerate(original))
            linear = degree + coefficients[1]
            min_linear = linear if min_linear is None else min(min_linear, linear)
            counts["zero linear coefficients"] += int(linear == 0)
            at_minus_one = abs(sum(c * (-1)**j for j, c in enumerate(coefficients)))
            if at_minus_one == 0:
                raise ValueError(f"Cyclotomic linear divisor on source line {line}")
            counts["max endpoint norm"] = max(counts["max endpoint norm"], at_minus_one)
            # A pole norm other than one must divide S(-1) and equal one modulo q(q+1).
            end = (isqrt(1 + 4*(at_minus_one + 1)) - 1)//2
            for q in range(2, end + 1):
                counts["divisor evaluations"] += 1
                value = pole_value(coefficients, q)
                if value == 0:
                    raise ValueError(f"Rational nonunit root on source line {line}")
                if value != 1 and at_minus_one % value == 0:
                    counts["other signed divisors"] += 1
                    print(f"DIVISOR {line=} {degree=} {sign=} {q=} {value=} {at_minus_one=}")
            bound = abs(pole_coefficient(coefficients))
            # Reciprocity makes the same divisibility hold for q and -q-1.
            for q in range(2, (isqrt(1+4*bound)-1)//2 + 1):
                if bound % (q*(q+1)):
                    continue
                counts["evaluations"] += 1
                max_height = max(max_height, q)
                if pole_value(coefficients, q) == 1:
                    counts["hits"] += 1
                    print(f"HIT {line=} {degree=} {measure=} {exterior=} {sign=} {q=}")
    if not counts["rows"]:
        raise ValueError("No source rows")
    print(f"rows={counts['rows']} complete-range rows={counts['complete-range rows']} "
          f"signs={2*counts['rows']} zero linear coefficients={counts['zero linear coefficients']} "
          f"min linear={min_linear} evaluations={counts['evaluations']} "
          f"max q evaluated={max_height} hits={counts['hits']}")
    print(f"max endpoint norm={counts['max endpoint norm']} "
          f"additional divisor evaluations={counts['divisor evaluations']} "
          f"other signed divisors={counts['other signed divisors']}")


if __name__ == "__main__":
    main()
