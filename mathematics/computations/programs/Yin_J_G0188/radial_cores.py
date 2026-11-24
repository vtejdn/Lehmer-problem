"""Certify the minimum with conjugate radial rank at least two through degree 55."""

from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path
import sys


PROGRAMS = Path(__file__).resolve().parents[1]
for directory in ("Yin_J_G0187", "Yin_J_G0166", "Yin_J_G0144/checks"):
    sys.path.insert(0, str(PROGRAMS / directory))
from small_cores import graeffe, table_rows, trace_from_half
from split_traces import degree_pattern, gcd_poly, trim
from independent_trace56_review import evaluate, sturm, variations


LOWER = Fraction(12193, 10000)
UPPER = Fraction(3049, 2500)
WITNESS = (1, 1, 1, 0, -1, -1, -1, 0, 0, 1)
HIGHER_COUNTS = {46: 107, 48: 80, 50: 76, 52: 66, 54: 66}


def compare_measure(coefficients, cutoff):
    """Compare coefficient bounds for successive root squarings with cutoff."""
    degree = len(coefficients) - 1
    binomials = [comb(degree, j) for j in range(degree + 1)]
    numerator, denominator = cutoff.as_integer_ratio()
    row = list(coefficients)
    for step in range(19):
        if sum(map(abs, row)) * denominator < numerator:
            return -1, step
        if any(abs(value) * denominator > bound * numerator
               for value, bound in zip(row, binomials)):
            return 1, step
        if step < 18:
            row = graeffe(row)
            numerator *= numerator
            denominator *= denominator
    raise ArithmeticError(f"Unresolved comparison at {cutoff} for {coefficients}")


def signature(trace):
    """Return Sturm variations and the exterior-place counts in the reciprocal lift."""
    if not evaluate(trace, -2) or not evaluate(trace, 2):
        raise ArithmeticError("An endpoint is a trace root.")
    chain = sturm(trace)
    if len(chain[-1]) != 1:
        raise ArithmeticError("The trace polynomial has a repeated root.")
    bound = 2 + max(map(abs, trace[:-1]))
    counts = tuple(variations(chain, point) for point in (-bound, -2, 2, bound))
    below, inside, above = (a - b for a, b in zip(counts, counts[1:]))
    nonreal = len(trace) - 1 - below - inside - above
    if min(below, inside, above, nonreal) < 0 or nonreal % 2:
        raise ArithmeticError("Inconsistent Sturm signature.")
    return counts, (below, inside, above, nonreal // 2)


def squarefree_pattern(coefficients, prime):
    polynomial = [value % prime for value in coefficients]
    derivative = trim([i * polynomial[i] % prime for i in range(1, len(polynomial))])
    if gcd_poly(polynomial, derivative, prime) != [1]:
        raise ArithmeticError(f"Repeated factor in characteristic {prime}")
    return tuple(sorted(degree_pattern(polynomial, prime).elements()))


def main():
    counts = Counter()
    higher = Counter()
    signatures = Counter()
    maximum_step = 0
    for line, degree, _, _, polynomial in table_rows():
        if degree > 54:
            continue
        comparison, step = compare_measure(polynomial, UPPER)
        maximum_step = max(maximum_step, step)
        if degree > 44:
            if comparison < 0:
                raise ArithmeticError(f"Unexpected small higher-degree row {line}")
            higher[degree] += 1
            continue
        counts[comparison] += 1
        if comparison > 0:
            continue
        half = polynomial[:degree // 2 + 1]
        lower_comparison, step = compare_measure(polynomial, LOWER)
        maximum_step = max(maximum_step, step)
        trace = trace_from_half(half)
        changes, shape = signature(trace)
        print(f"line {line}, degree {degree}: variations {changes}, signature {shape}")
        below, _, above, pairs = shape
        if half == WITNESS:
            if shape != (1, 6, 0, 1) or lower_comparison != 1:
                raise ArithmeticError("The degree-18 witness failed its signature or interval.")
            signatures["witness"] += 1
        else:
            if below + above + pairs != 1 or lower_comparison != -1:
                raise ArithmeticError(f"Row {line} failed the one-place or measurement test.")
            signatures["one real" if pairs == 0 else "one complex pair"] += 1
    if (counts != {-1: 14, 1: 930} or higher != HIGHER_COUNTS or
            signatures != {"witness": 1, "one real": 5, "one complex pair": 8}):
        raise ArithmeticError(f"Unexpected source counts: {counts}, {higher}, {signatures}")
    print(f"Through degree 44: {counts[-1]} below the upper cutoff and {counts[1]} above.")
    print(f"All checked higher rows above: {dict(sorted(higher.items()))}.")
    print(f"Below the upper cutoff: {dict(signatures)}. Maximum Graeffe step: {maximum_step}.")
    trace = trace_from_half(WITNESS)
    lift = WITNESS + WITNESS[-2::-1]
    tests = (("trace", trace, 2, (9,)), ("trace", trace, 13, (2, 7)),
             ("lift", lift, 13, (4, 14)))
    for name, coefficients, prime, expected in tests:
        pattern = squarefree_pattern(coefficients, prime)
        if pattern != expected:
            raise ArithmeticError(f"Unexpected modular degrees: {name}, {prime}, {pattern}")
        print(f"{name} modulo {prime}: squarefree factor degrees {pattern}")


if __name__ == "__main__":
    main()
