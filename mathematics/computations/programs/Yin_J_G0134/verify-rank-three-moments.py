"""Independent integer verification of the C863 v2 rank-three certificate.

No import or execution of rank-three-moments.py is used.  Endpoint walk
coefficients are computed by interleaving four one-dimensional walks,
instead of its closed two-dimensional binomial formula.  All 42 cases and
both sigma choices are evaluated through order 128.  Native mathematical
fields, rather than a saved success flag, are compared exactly.
"""

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import itertools
import json
from math import comb, gcd
from pathlib import Path
import sys


GROUP = Path(__file__).resolve().parent
ORDER = 128
BOUND = 5
DEFAULT_OUTPUT = GROUP.parent.parent / "outputs" / GROUP.name / "rank-three-verification.json"


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def enumerate_relations():
    # Deliberately use the whole Cartesian box and an ordinary sorting test.
    result = []
    for c in itertools.product(range(1, BOUND + 1), repeat=4):
        if list(c) != sorted(c) or gcd(*c) != 1:
            continue
        # A balanced sign partition is equivalent to a subset of half the sum.
        total = sum(c)
        balanced = any(2 * sum(c[j] for j in range(4) if mask & (1 << j)) == total
                       for mask in range(16))
        if not balanced:
            result.append(c)
    return result


@lru_cache(maxsize=None)
def axis_interleaving_coefficients(vector, max_degree):
    """All walk counts to this endpoint, by allocating steps to axes.

    A length t one-axis walk ending at a has comb(t,(t-a)/2) choices.
    Inserting its steps among an existing n-t-step walk costs comb(n,t).
    Iteration over four axes counts every full walk once and only once.
    """
    previous = [1] + [0] * max_degree
    minimum = 0
    for endpoint in vector:
        current = [0] * (max_degree + 1)
        one_axis = {t: comb(t, (t - endpoint) // 2)
                    for t in range(endpoint, max_degree + 1, 2)}
        for n in range(minimum + endpoint, max_degree + 1, 2):
            current[n] = sum(comb(n, t) * previous[n - t] * one_axis[t]
                             for t in range(endpoint, n - minimum + 1, 2))
        previous = current
        minimum += endpoint
    return tuple(previous)


def endpoint_coefficients(vector, max_degree):
    # Axis permutation and reversal give bijections of unsigned walks.
    return axis_interleaving_coefficients(tuple(sorted(map(abs, vector))), max_degree)


def moment_pairs(c, order):
    nmax = 2 * order
    base = endpoint_coefficients((0, 0, 0, 0), nmax)
    answer = {sigma: [base[2 * k] for k in range(order + 1)] for sigma in (1, -1)}
    total = sum(c)
    for multiple in range(1, nmax // total + 1):
        endpoint = tuple(multiple * a for a in c)
        if sum(endpoint) % 2:
            continue
        coefficients = endpoint_coefficients(endpoint, nmax)
        # For even degree, the sine phase depends on endpoint sum alone.
        phase = 1 if (sum(endpoint) // 2) % 2 == 0 else -1
        for sigma in (1, -1):
            multiplier = 2 * phase * sigma ** multiple
            for k in range((sum(endpoint) + 1) // 2, order + 1):
                answer[sigma][k] += multiplier * coefficients[2 * k]
    for sigma, moments in answer.items():
        require(moments[:3] == [1, 8, 168], f"initial moments {c}, {sigma}")
        require(all(0 <= m <= 64 ** k for k, m in enumerate(moments)),
                f"moment bounds {c}, {sigma}")
    if total % 2:
        require(answer[1] == answer[-1], f"odd-sum sign equivalence {c}")
    return answer


def logarithm_sum(moments):
    residuals = []
    result = Fraction(0)
    previous = 1
    for j in range(1, len(moments)):
        # Horner evaluation of sum_k (-1)^k binom(j,k) M_k 64^(j-k).
        numerator = 0
        for k in range(j + 1):
            numerator = 64 * numerator + (-1) ** k * comb(j, k) * moments[k]
        require(0 <= numerator <= 64 ** j, f"residual range at {j}")
        require(numerator <= 64 * previous, f"residual monotonicity at {j}")
        previous = numerator
        residuals.append(numerator)
        result += Fraction(numerator, j * 64 ** j)
    return result, residuals


def direct_expansions(cases, moment_results):
    # A separate dictionary expansion checks every supported unsigned
    # coefficient through degree 8, then signed restrictions through degree 10.
    unsigned = {(0, 0, 0, 0): 1}
    count = 0
    for degree in range(9):
        for exponent, value in unsigned.items():
            require(endpoint_coefficients(exponent, 8)[degree] == value,
                    f"direct unsigned expansion {degree}, {exponent}")
            count += 1
        following = defaultdict(int)
        for exponent, value in unsigned.items():
            for axis in range(4):
                for direction in (-1, 1):
                    next_exponent = list(exponent)
                    next_exponent[axis] += direction
                    following[tuple(next_exponent)] += value
        unsigned = dict(following)

    sign_patterns = {(1, 1, 1, 1)}
    representatives = {}
    for c in cases:
        negative = [1] * 4
        negative[next(j for j in range(4) if c[j] % 2)] = -1
        representatives[c] = {1: (1, 1, 1, 1), -1: tuple(negative)}
        sign_patterns.add(tuple(negative))
    expansions = {}
    for signs in sign_patterns:
        polynomial = {(0, 0, 0, 0): 1}
        even = []
        for degree in range(11):
            if degree % 2 == 0:
                even.append(polynomial)
            following = defaultdict(int)
            for exponent, value in polynomial.items():
                for axis in range(4):
                    for direction in (-1, 1):
                        next_exponent = list(exponent)
                        next_exponent[axis] += direction
                        following[tuple(next_exponent)] += value * signs[axis] * direction
            polynomial = {v: a for v, a in following.items() if a}
        expansions[signs] = even
    restriction_count = 0
    for c in cases:
        for sigma in (1, -1):
            signs = representatives[c][sigma]
            require(all((s in (-1, 1)) for s in signs), "sign representative")
            require((-1) ** sum(c[j] for j in range(4) if signs[j] == -1) == sigma,
                    f"sign product {c}, {sigma}")
            for k, polynomial in enumerate(expansions[signs]):
                integral = 0
                for v, value in polynomial.items():
                    if v[0] % c[0] == 0:
                        multiple = v[0] // c[0]
                        if v == tuple(multiple * a for a in c):
                            integral += value
                require((-1) ** k * integral == moment_results[c][sigma][k],
                        f"direct sine restriction {c}, {sigma}, {k}")
                restriction_count += 1
    return {"unsigned_supported_coefficient_equalities": count,
            "unsigned_degrees": [0, 8], "signed_even_moment_equalities": restriction_count,
            "signed_degrees": [0, 10], "relations": len(cases), "sigma_choices_per_relation": 2}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    cases = enumerate_relations()
    require(len(cases) == 42, "exhaustive case count")
    expected_cases = {"coefficient_bound": BOUND,
                      "positive_sorted_primitive_full_support": True,
                      "balanced_partitions_excluded": True,
                      "cases": [{"relation": list(c),
                                 "sigma_values": [1] if sum(c) % 2 else [1, -1]}
                                for c in cases]}
    actual_cases = json.loads((GROUP / "inputs/rank-three-cases.json").read_text(encoding="utf-8"))
    require(actual_cases == expected_cases, "complete case input and sign classes")
    native = json.loads((GROUP / "inputs/rank-three-certificate.json").read_text(encoding="utf-8"))
    expected_native = {"coefficient_bound": BOUND, "degree": ORDER,
                       "threshold": [14, 5], "case_count": 42, "cases": []}
    moments_by_case = {}
    rows = []
    sums = {}
    for c in cases:
        moments = moment_pairs(c, ORDER)
        moments_by_case[c] = moments
        orbit_rows = []
        for sigma in (1, -1):
            total, residuals = logarithm_sum(moments[sigma])
            margin = 5 * total.numerator - 14 * total.denominator
            orbit_rows.append({"sigma": sigma, "sum_numerator": str(total.numerator),
                               "sum_denominator": str(total.denominator),
                               "comparison_5_num_minus_14_den": str(margin),
                               "passed": margin > 0,
                               "moments": list(map(str, moments[sigma])),
                               "residual_numerators": list(map(str, residuals))})
            if sigma == 1:
                require(margin > 0, f"chosen sign comparison {c}")
                sums[c] = total
                expected_native["cases"].append({"relation": list(c), "sigma": sigma,
                                                  "sum_numerator": str(total.numerator),
                                                  "sum_denominator": str(total.denominator),
                                                  "comparison_5_num_minus_14_den": str(margin)})
        rows.append({"relation": list(c), "orbits": orbit_rows})
        print(c, "chosen sign verified; both sigma choices computed", flush=True)
    require(native == expected_native, "entire selected certificate mathematical payload")
    smallest = min(sums, key=sums.get)
    require(smallest == (1, 4, 4, 5), "minimum selected sum relation")
    require(sums[smallest].numerator * 10 ** 12 // sums[smallest].denominator == 2953181645613,
            "claimed exact rational enclosure")
    controls = direct_expansions(cases, moments_by_case)
    odd = sum(sum(c) % 2 for c in cases)
    require(odd == 32, "odd/even relation count")
    result = {"scope": "Independent integer recomputation; checker self-inspected by its implementer.",
              "python": sys.version, "order": ORDER, "coefficient_bound": BOUND,
              "case_count": len(cases), "odd_sum_cases": odd, "even_sum_cases": len(cases) - odd,
              "distinct_sign_classes": odd + 2 * (len(cases) - odd),
              "sigma_computations": 2 * len(cases), "native_fields_match": True,
              "all_selected_comparisons_positive": True,
              "minimum_selected_relation": list(smallest),
              "minimum_floor_scaled_10_power_12": 2953181645613,
              "direct_expansion_controls": controls, "cases": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PASS: 42 native rows; 52 distinct sign classes; 84 sigma computations;", controls, flush=True)
    print("Replaceable verification output:", args.output, flush=True)


if __name__ == "__main__":
    main()
