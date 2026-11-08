"""Classify the full reciprocal shell and test the sign transition on its prime grid."""

from collections import Counter
from functools import lru_cache
import json
from math import comb
from pathlib import Path
import subprocess
import sys

from sympy import Poly, Rational, cyclotomic_poly, oo, symbols, totient

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "Yin_J_G0144"))
from pilot import graeffe

t, z = symbols("t z")
# Counts in order: Newton survivors, neutral, strict, strict in the chamber.
EXPECTED = {14: (2955, 2257, 38, 0), 18: (21726, 10133, 332, 0),
            20: (64799, 20399, 850, 1)}
DEGREE_20_INPUT = (1, -3, 4, -4, 3, -1, -1, 3, -4, 4, -4)


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return tuple(result)


def neutral_inputs(degree):
    factors = [(1, -2, 1), (1, 2, 1)]
    for order in range(3, 2 * degree**2 + 1):
        if totient(order) <= degree:
            factors.append(tuple(map(int, Poly(cyclotomic_poly(order, z), z).all_coeffs())))
    by_degree = [set() for _ in range(degree + 1)]
    by_degree[0].add((1,))
    for factor in factors:
        width = len(factor) - 1
        for k in range(width, degree + 1):
            by_degree[k].update(multiply(p, factor) for p in by_degree[k - width])
    return by_degree[degree]


@lru_cache(None)
def threshold(step):
    return 6**(1 << step), 5**(1 << step)


def classify(polynomial, binomials):
    for numerator in (6, -6):
        # A negative sign before the monic even polynomial reaches infinity
        # certifies a real root of modulus greater than 6/5.
        value = denominator = 1
        for coefficient in polynomial[1:]:
            denominator *= 5
            value = numerator * value + denominator * coefficient
        if value < 0:
            return "above"
    squared = polynomial
    for step in range(19):
        num, den = threshold(step)
        if any(den * abs(x) > num * b for x, b in zip(squared, binomials)):
            return "above"
        if den**2 * sum(x*x for x in squared) < num**2:
            return "inside"
        if step < 18:
            squared = graeffe(squared)
    raise ArithmeticError(("unresolved 6/5 comparison", polynomial))


def trace_basis(half):
    terms = [Poly(2, t), Poly(t, t)]
    while len(terms) <= half:
        terms.append(Poly(t, t) * terms[-1] - terms[-2])
    return terms


def to_trace(polynomial, basis):
    half = len(polynomial) // 2
    return Poly(polynomial[half], t) + sum(
        (polynomial[half - k] * basis[k] for k in range(1, half + 1)), Poly(0, t)
    )


def sign_on_interval(polynomial, interval):
    lo, hi = interval
    lower = upper = 0
    for coefficient in polynomial.all_coeffs():
        endpoints = (lower * lo, lower * hi, upper * lo, upper * hi)
        lower, upper = min(endpoints) + coefficient, max(endpoints) + coefficient
    if lower > 0:
        return 1
    if upper < 0:
        return -1
    raise ArithmeticError(("isolating interval did not certify sign", polynomial, interval))


def check_unique_input(polynomial, basis):
    poly = Poly.from_list(polynomial, z)
    core = poly.exquo(Poly((z - 1)**2, z))
    assert core.is_irreducible
    trace = to_trace(core.all_coeffs(), basis)
    assert trace.count_roots(-2, 2) == 8 and trace.count_roots(2, oo) == 1
    assert trace.eval(-2) == trace.eval(2) == -1
    assert core.eval(Rational(118836814, 10**8)) < 0 < core.eval(Rational(118836815, 10**8))


def census(degree):
    run = subprocess.run(["node", str(HERE / "newton.cjs"), str(degree)],
                         capture_output=True, text=True, check=True)
    result = json.loads(run.stdout)
    half = degree // 2
    basis = trace_basis(half)
    poles = Poly(1, t) + sum(basis[1:half], Poly(0, t))
    assert poles.degree() == half - 1
    intervals = [pair for pair, multiplicity in poles.intervals(eps=Rational(1, 10**14))]
    assert len(intervals) == half - 1
    neutral = neutral_inputs(degree)
    binomials = [comb(degree, j) for j in range(degree + 1)]
    labels = Counter()
    chamber = []
    for prefix in result["survivors"]:
        polynomial = (1, *prefix, *reversed(prefix[:-1]), 1)
        if polynomial in neutral:
            labels["one"] += 1
            continue
        label = classify(polynomial, binomials)
        labels[label] += 1
        if label != "inside":
            continue
        trace = to_trace(polynomial, basis)
        norm = abs(int(poles.resultant(trace)))
        if norm == 0 or poles.eval(-2) * trace.eval(-2) >= 0:
            continue
        signs = [sign_on_interval(trace, pair) * (-1)**(len(intervals) - 1 - i)
                 for i, pair in enumerate(intervals)]
        negatives = signs.count(-1)
        if 0 < negatives < len(signs) and signs == sorted(signs):
            chamber.append((polynomial[:half + 1], norm, negatives))
    assert labels["one"] == len(neutral)
    sizes = len(result["survivors"]), len(neutral), labels["inside"], len(chamber)
    assert sizes == EXPECTED[degree], sizes
    if degree == 20:
        assert chamber == [(DEGREE_20_INPUT, 4313, 1)]
        check_unique_input((*DEGREE_20_INPUT, *DEGREE_20_INPUT[-2::-1]), basis)
    print(f"Degree {degree}, prefixes by length: {result['counts'][1:]}")
    print(f"After 32 Newton sums: {sizes[0]}; M=1: {sizes[1]}; above: {labels['above']}; strict: {sizes[2]}")
    print(f"Strict chamber: {sizes[3]}; unit-resultant strict chamber: {sum(row[1] == 1 for row in chamber)}")
    for prefix, norm, negatives in chamber:
        print(f"  {prefix}, |Res|={norm}, negative poles={negatives}")


if __name__ == "__main__":
    for size in map(int, sys.argv[1:] or sorted(EXPECTED)):
        census(size)
