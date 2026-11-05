"""Independent integer recomputation of the C863 v3 order-128 certificate.

The walk implementation interleaves one axis at a time, without importing
the author program or its two-coordinate closed formula.  The bounded scope
is generated from the full Cartesian box before the native certificate is
read.  Only the final complete result is written to the ignored output home.
"""

from collections import defaultdict
from functools import cache
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import platform


GROUP = Path(__file__).resolve().parent
INPUT = GROUP / "inputs" / "rank-two-moment-certificate.json"
OUTPUT = GROUP.parent.parent / "outputs" / GROUP.name / "rank-two-locality-verification.json"
ORDER = 128
MAX_DEGREE = 2 * ORDER
BINOM = [[math.comb(n, j) for j in range(n + 1)] for n in range(MAX_DEGREE + 1)]


@cache
def axis_interleaving(endpoint):
    """Return all n-step counts in len(endpoint) axes, 0 <= n <= 256.

    Choosing t of n positions for the last axis, its + and - counts are
    (t+a)/2 and (t-a)/2.  The other positions form the previous-axis walk.
    Thus every full walk is counted exactly once, using integer arithmetic.
    """
    if not endpoint:
        return (1,) + (0,) * MAX_DEGREE
    endpoint = tuple(abs(a) for a in endpoint)
    a = endpoint[-1]
    earlier = endpoint[:-1]
    previous = axis_interleaving(earlier)
    lower = sum(earlier)
    result = [0] * (MAX_DEGREE + 1)
    for n in range(lower + a, MAX_DEGREE + 1, 2):
        result[n] = sum(BINOM[n][t] * BINOM[t][(t - a) // 2] * previous[n - t]
                        for t in range(a, n - lower + 1, 2))
    return tuple(result)


def cases_from_box():
    """All canonical primitive vectors, excluding exactly forbidden lattices."""
    result = []
    for c in itertools.product(range(8), repeat=4):
        if tuple(sorted(c)) != c or math.gcd(*c) != 1:
            continue
        # In this primitive canonical scope these are exactly the coordinate
        # and two-coordinate collision relations, respectively.
        if c == (0, 0, 0, 1) or c == (0, 0, 1, 1):
            continue
        result.append(c)
    if len(result) != 275:
        raise AssertionError("Unexpected complete canonical count")
    return result


def averaged_moments(relation):
    result = list(axis_interleaving((0, 0, 0, 0))[::2])
    weight = sum(relation)
    for r in range(1, ORDER // weight + 1):
        endpoint = tuple(2 * r * a for a in relation)
        coefficients = axis_interleaving(endpoint)
        multiplier = -2 if r * weight % 2 else 2
        for k in range(r * weight, ORDER + 1):
            result[k] += multiplier * coefficients[2 * k]
    return result


def finite_logarithm(moments):
    """Use exact Horner evaluation of every residual numerator."""
    if moments[:3] != [1, 8, 168]:
        raise AssertionError("Moment normalization mismatch")
    for k, moment in enumerate(moments):
        if not 0 <= moment <= 64 ** k:
            raise AssertionError(("Moment bound", k, moment))
    previous = 1
    total = Fraction(0)
    for j in range(1, ORDER + 1):
        residual = 0
        for k in range(j + 1):
            signed = BINOM[j][k] * moments[k]
            residual = 64 * residual + (-signed if k % 2 else signed)
        if not (0 <= residual <= 64 ** j and residual <= 64 * previous):
            raise AssertionError(("Residual bound", j, residual))
        previous = residual
        total += Fraction(residual, j * 64 ** j)
    return total


def exact_fields(value, numerator, denominator):
    comparison = denominator * value.numerator - numerator * value.denominator
    if comparison <= 0:
        raise AssertionError(("Threshold failure", numerator, denominator))
    return {"sum_numerator": str(value.numerator),
            "sum_denominator": str(value.denominator),
            "positive_comparison_integer": str(comparison)}


def belongs_to_line(vector, relation):
    """Cross-products and divisibility avoid a leading-nonzero assumption."""
    pivot = next(i for i, a in enumerate(relation) if a)
    return (vector[pivot] % relation[pivot] == 0
            and all(vector[i] * relation[pivot] == vector[pivot] * relation[i]
                    for i in range(4)))


def direct_controls(cases, moments):
    """Expand unsigned and antisymmetric Laurent powers without walk formulae."""
    positive = {(0, 0, 0, 0): 1}
    signed = positive.copy()
    coefficient_checks = 0
    moment_checks = 0
    for n in range(9):
        for endpoint, coefficient in positive.items():
            if axis_interleaving(tuple(sorted(map(abs, endpoint))))[n] != coefficient:
                raise AssertionError(("Direct walk mismatch", n, endpoint))
            coefficient_checks += 1
        if n % 2 == 0:
            even_terms = [(v, a) for v, a in signed.items() if all(x % 2 == 0 for x in v)]
            for relation in cases:
                actual = sum(a for v, a in even_terms if belongs_to_line(v, relation))
                actual *= (-1) ** (n // 2)
                if actual != moments[relation][n // 2]:
                    raise AssertionError(("Direct averaged moment mismatch", n, relation))
                moment_checks += 1
        if n == 8:
            break
        next_positive = defaultdict(int)
        next_signed = defaultdict(int)
        for coordinate in range(4):
            for direction in (-1, 1):
                for vector, value in positive.items():
                    child = list(vector)
                    child[coordinate] += direction
                    next_positive[tuple(child)] += value
                for vector, value in signed.items():
                    child = list(vector)
                    child[coordinate] += direction
                    next_signed[tuple(child)] += direction * value
        positive = dict(next_positive)
        signed = {v: a for v, a in next_signed.items() if a}
    return coefficient_checks, moment_checks


def main():
    cases = cases_from_box()
    free = finite_logarithm(list(axis_interleaving((0, 0, 0, 0))[::2]))
    free_fields = exact_fields(free, 59, 20)
    rows = []
    moments = {}
    values = []
    for index, relation in enumerate(cases, 1):
        moments[relation] = averaged_moments(relation)
        value = finite_logarithm(moments[relation])
        rows.append({"relation": list(relation), **exact_fields(value, 14, 5)})
        values.append(value)
        if index % 25 == 0 or index == len(cases):
            print(f"Independently computed {index}/{len(cases)} relations", flush=True)
    coefficient_checks, moment_checks = direct_controls(cases, moments)
    if coefficient_checks != 5301 or moment_checks != 1375:
        raise AssertionError("Direct-control coverage mismatch")
    expected = {"degree": ORDER, "coefficient_bound": 7,
                "free_threshold": [59, 20], "free_torus": free_fields,
                "rank_three_sign_average_threshold": [14, 5],
                "case_count": len(cases), "cases": rows,
                "small_direct_walk_coefficient_checks": coefficient_checks,
                "small_signed_controls": [[0, 0, 1, 2], [0, 0, 1, 3], [0, 1, 1, 1], [1, 1, 1, 1]]}
    # The certificate is an object to compare, never an input to the arithmetic.
    native = json.loads(INPUT.read_text(encoding="utf-8"))
    if native != expected:
        raise AssertionError("Full native certificate mismatch")
    minimum = min(values)
    minimizers = [list(c) for c, value in zip(cases, values) if value == minimum]
    floor = minimum.numerator * 10 ** 12 // minimum.denominator
    if minimizers != [[0, 1, 1, 1]] or floor != 2944235671458:
        raise AssertionError("Claimed minimum/enclosure mismatch")
    report = {"result": "PASS", "python": platform.python_version(),
              "order": ORDER, "complete_canonical_cases": len(cases),
              "matched_all_native_fields": True,
              "free_threshold": [59, 20], "rank_three_threshold": [14, 5],
              "direct_walk_coefficients": coefficient_checks,
              "direct_sign_averaged_moments": moment_checks,
              "minimum_relations": minimizers, "minimum_floor_times_10_to_12": floor,
              "native_payload": expected}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: free and {len(cases)} exact order-{ORDER} certificates matched every field; "
          f"{coefficient_checks} direct coefficients and {moment_checks} averaged moments checked.")
    print(f"Minimum relation {minimizers[0]} has floor(10^12 S)={floor}.")
    print(OUTPUT)


if __name__ == "__main__":
    main()
