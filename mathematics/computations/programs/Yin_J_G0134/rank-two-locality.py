"""Exact order-128 sign-averaged certificates for finite relation locality.

Only Python integer and Fraction arithmetic enters the certificate.
The full scope is the free torus and admissible primitive rank-three
relations with sorted nonnegative coordinates at most seven.
The separate Fourier estimate handles every larger rank-three relation.
No exceptional rank-two lattice enumeration is performed.
"""

import argparse
from fractions import Fraction
import json
import math
import itertools
from pathlib import Path


GROUP = Path(__file__).resolve().parent
CERTIFICATE = GROUP / "inputs" / "rank-two-moment-certificate.json"
DEGREE = 128
BOUND = 7


def free_even_moment(k):
    n = 2 * k
    return sum(math.comb(n, t) * math.comb(t, t // 2) ** 2
               * math.comb(n - t, (n - t) // 2) ** 2
               for t in range(0, n + 1, 2))


def walk_coefficient(n, vector, binomials):
    u, v, w, x = map(abs, vector)
    if u + v + w + x > n or (n - u - v - w - x) % 2:
        return 0
    total = 0
    for t in range(u + v, n - w - x + 1, 2):
        rest = n - t
        total += (binomials[n][t]
                  * binomials[t][(t + u + v) // 2]
                  * binomials[t][(t + u - v) // 2]
                  * binomials[rest][(rest + w + x) // 2]
                  * binomials[rest][(rest + w - x) // 2])
    return total


def canonical_cases():
    return [c for c in itertools.combinations_with_replacement(range(BOUND + 1), 4)
            if math.gcd(*c) == 1 and c not in ((0, 0, 0, 1), (0, 0, 1, 1))]


def averaged_moments(relation, free_moments, binomials):
    weight = sum(relation)
    result = []
    for k in range(DEGREE + 1):
        value = free_moments[k]
        for r in range(1, k // weight + 1):
            value += (2 * (-1) ** (r * weight)
                      * walk_coefficient(2 * k, tuple(2 * r * c for c in relation), binomials))
        assert value >= 0
        result.append(value)
    return result


def logarithm_sum(moments):
    assert moments[:3] == [1, 8, 168]
    total = Fraction(0)
    previous = 1
    for j in range(1, DEGREE + 1):
        residual = sum((-1) ** k * math.comb(j, k) * moments[k]
                       * 64 ** (j - k) for k in range(j + 1))
        assert 0 <= residual <= 64 ** j
        assert residual <= 64 * previous
        previous = residual
        total += Fraction(residual, j * 64 ** j)
    return total


def exact_row(value, threshold):
    comparison = threshold.denominator * value.numerator - threshold.numerator * value.denominator
    assert comparison > 0
    return {"sum_numerator": str(value.numerator),
            "sum_denominator": str(value.denominator),
            "positive_comparison_integer": str(comparison)}


def small_direct_checks(binomials):
    polynomial = {(0, 0, 0, 0): 1}
    antisymmetric = {(0, 0, 0, 0): 1}
    checked = 0
    controls = ((0, 0, 1, 2), (0, 0, 1, 3), (0, 1, 1, 1), (1, 1, 1, 1))
    for n in range(9):
        for vector, coefficient in polynomial.items():
            assert coefficient == walk_coefficient(n, vector, binomials)
            checked += 1
        if n % 2 == 0:
            k = n // 2
            for relation in controls:
                pivot = next(i for i, value in enumerate(relation) if value)
                actual = 0
                for vector, coefficient in antisymmetric.items():
                    if any(x % 2 for x in vector) or vector[pivot] % relation[pivot]:
                        continue
                    multiple = vector[pivot] // relation[pivot]
                    if all(x == multiple * c for x, c in zip(vector, relation)):
                        actual += (-1) ** k * coefficient
                weight = sum(relation)
                expected = free_even_moment(k)
                for r in range(1, k // weight + 1):
                    expected += (2 * (-1) ** (r * weight)
                                 * walk_coefficient(n, tuple(2 * r * c for c in relation), binomials))
                assert actual == expected
        if n < 8:
            following = {}
            for vector, coefficient in polynomial.items():
                for i in range(4):
                    for direction in (-1, 1):
                        child = list(vector)
                        child[i] += direction
                        child = tuple(child)
                        following[child] = following.get(child, 0) + coefficient
            polynomial = following
            following_antisymmetric = {}
            for vector, coefficient in antisymmetric.items():
                for i in range(4):
                    for direction in (-1, 1):
                        child = list(vector)
                        child[i] += direction
                        child = tuple(child)
                        following_antisymmetric[child] = (following_antisymmetric.get(child, 0)
                                                         + direction * coefficient)
            antisymmetric = {vector: coefficient for vector, coefficient
                             in following_antisymmetric.items() if coefficient}
    return checked


def calculate():
    binomials = [[math.comb(n, k) for k in range(n + 1)] for n in range(2 * DEGREE + 1)]
    checks = small_direct_checks(binomials)
    free_moments = [free_even_moment(k) for k in range(DEGREE + 1)]
    free_sum = logarithm_sum(free_moments)
    free_row = exact_row(free_sum, Fraction(59, 20))
    cases = canonical_cases()
    rows = []
    for index, relation in enumerate(cases):
        value = logarithm_sum(averaged_moments(relation, free_moments, binomials))
        rows.append({"relation": list(relation), **exact_row(value, Fraction(14, 5))})
        if (index + 1) % 50 == 0:
            print(f"Certified {index + 1}/{len(cases)} canonical relations", flush=True)
    return {"degree": DEGREE, "coefficient_bound": BOUND,
            "free_threshold": [59, 20], "free_torus": free_row,
            "rank_three_sign_average_threshold": [14, 5],
            "case_count": len(cases), "cases": rows,
            "small_direct_walk_coefficient_checks": checks,
            "small_signed_controls": [[0, 0, 1, 2], [0, 0, 1, 3], [0, 1, 1, 1], [1, 1, 1, 1]]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write-certificate", action="store_true")
    mode.add_argument("--verify-certificate", action="store_true")
    args = parser.parse_args()
    result = calculate()
    if args.write_certificate:
        CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
        with CERTIFICATE.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    else:
        with CERTIFICATE.open(encoding="utf-8") as stream:
            assert json.load(stream) == result
    print(f"PASS: exact order-{DEGREE} free and {result['case_count']} sign-averaged certificates "
          + ("created" if args.write_certificate else "recomputed and matched"))


if __name__ == "__main__":
    main()
