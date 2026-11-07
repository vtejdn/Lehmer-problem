"""Exact finite calibration for degree ten reciprocal integer polynomials."""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import comb


DEGREE = 10
HALF = DEGREE // 2
RADIUS = Fraction(6, 5)
MAX_SQUARINGS = 12


def autocorrelation_cuts(depth, errors):
    """Certificates with entries in {-1,0,1}, up to shift and overall sign."""
    cuts = set()
    for middle in product((-1, 0, 1), repeat=depth - 1):
        for last in (-1, 1):
            vector = (1, *middle, last)
            corr = tuple(
                sum(vector[i] * vector[i + lag] for i in range(len(vector) - lag))
                for lag in range(depth + 1)
            )
            slack = 2 * sum(abs(corr[k]) * errors[k] for k in range(1, depth + 1))
            # The other terms are integers, so flooring the allowance is exact.
            allowance = DEGREE * corr[0] + int(slack)
            cuts.add((corr[1:], allowance))
    return sorted(cuts)


def surviving_prefixes(height, use_toeplitz):
    errors = [RADIUS**k + RADIUS**(-k) - 2 for k in range(HALF + 1)]
    cuts = {k: autocorrelation_cuts(k, errors) for k in range(1, HALF + 1)}
    frontier = [((), ())]
    counts = []
    for k in range(1, HALF + 1):
        next_frontier = []
        for prefix, sums in frontier:
            offset = -sum(a * s for a, s in zip(prefix, reversed(sums)))
            for a_k in range(-height, height + 1):
                s_k = offset - k * a_k
                if abs(s_k) > DEGREE + errors[k]:
                    continue
                extended_sums = (*sums, s_k)
                if use_toeplitz and any(
                    allowance + 2 * sum(c * s for c, s in zip(coeffs, extended_sums)) < 0
                    for coeffs, allowance in cuts[k]
                ):
                    continue
                next_frontier.append(((*prefix, a_k), extended_sums))
        frontier = next_frontier
        counts.append(len(frontier))
    return {prefix for prefix, _ in frontier}, counts


def monic_quotient(poly, divisor):
    """Return an exact quotient or None. Coefficients are in ascending order."""
    if len(poly) < len(divisor):
        return None
    rest = list(poly)
    quotient = [0] * (len(poly) - len(divisor) + 1)
    for shift in reversed(range(len(quotient))):
        coefficient = rest[shift + len(divisor) - 1]
        quotient[shift] = coefficient
        for i, a in enumerate(divisor):
            rest[shift + i] -= coefficient * a
    return quotient if not any(rest) else None


def cyclotomic_factors():
    # phi(m)^2 / m is a product of p^(e-2)(p-1)^2 >= 1 except for 2^1.
    # Thus a cyclotomic factor of degree <= DEGREE has order <= 2*DEGREE^2.
    factors = {}
    for order in range(1, 2 * DEGREE**2 + 1):
        poly = [-1] + [0] * (order - 1) + [1]
        for divisor, phi in factors.items():
            if order % divisor == 0:
                poly = monic_quotient(poly, phi)
                if poly is None:
                    raise ArithmeticError(f"failed cyclotomic construction at {order}")
        factors[order] = poly
    return [phi for phi in factors.values() if len(phi) <= DEGREE + 1]


def is_cyclotomic_product(poly, factors):
    rest = poly
    for phi in factors:
        while len(rest) >= len(phi):
            quotient = monic_quotient(rest, phi)
            if quotient is None:
                break
            rest = quotient
    return rest == [1]


def graeffe(poly):
    """E(x)^2 - x O(x)^2 for the monic even-degree input E(x^2)+x O(x^2)."""
    result = [0] * len(poly)
    for offset, sign in ((0, 1), (1, -1)):
        part = poly[offset::2]
        for i, a in enumerate(part):
            for j, b in enumerate(part):
                result[offset + i + j] += sign * a * b
    return result


def classify(prefix, factors):
    # The palindromic vector reads the same in either coefficient order.
    poly = [1, *prefix, *reversed(prefix[:-1]), 1]
    if is_cyclotomic_product(poly, factors):
        return "cyclotomic"
    # Kronecker now gives M>1. Bound the full product after each root squaring.
    for iteration in range(MAX_SQUARINGS + 1):
        exponent = 2**iteration
        num = RADIUS.numerator**exponent
        den = RADIUS.denominator**exponent
        if den**2 * sum(a * a for a in poly) < num**2:
            return "positive_hit"
        if any(den * abs(a) > num * comb(DEGREE, k) for k, a in enumerate(poly)):
            return "above_threshold"
        if iteration < MAX_SQUARINGS:
            poly = graeffe(poly)
    return "undecided"


def run(height):
    single, single_counts = surviving_prefixes(height, False)
    combined, combined_counts = surviving_prefixes(height, True)
    if not combined <= single:
        raise ArithmeticError("combined leaves must also pass the single-moment tests")
    factors = cyclotomic_factors()
    census = Counter()
    hits = []
    for prefix in product(range(-height, height + 1), repeat=HALF):
        outcome = classify(prefix, factors)
        census[outcome] += 1
        if outcome in ("cyclotomic", "positive_hit") and prefix not in combined:
            raise ArithmeticError(f"false negative for {prefix} ({outcome})")
        if outcome == "positive_hit":
            hits.append(prefix)
    return {
        "degree": DEGREE,
        "height": height,
        "threshold": str(RADIUS),
        "single_moment_surviving_prefixes_by_depth": single_counts,
        "combined_surviving_prefixes_by_depth": combined_counts,
        "full_box": sum(census.values()),
        "independent_census": {
            key: census[key]
            for key in ("cyclotomic", "positive_hit", "above_threshold", "undecided")
        },
        "positive_prefixes_from_high_degree": hits,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--height", type=int, choices=(1, 2), default=1)
    args = parser.parse_args()
    print(json.dumps(run(args.height), indent=2))
