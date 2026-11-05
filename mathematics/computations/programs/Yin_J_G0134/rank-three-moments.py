"""Exact finite logarithm certificates for bounded rank-three relations.

Canonical relations are sorted positive primitive four-tuples with entries
at most five and no equal-sum signed partition.  Only the declared degree
J=128 is used.  All evidence arithmetic uses Python integers and Fraction.
The analytic bridge and normalization are developed in Yin_D_G0018.md.
"""

import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import sys


DEGREE = 128
BOUND = 5
INPUT_PATH = Path("mathematics/computations/programs/Yin_J_G0134/inputs/rank-three-cases.json")
CERTIFICATE_PATH = Path("mathematics/computations/programs/Yin_J_G0134/inputs/rank-three-certificate.json")
OUTPUT_PATH = Path("mathematics/computations/outputs/Yin_J_G0134/rank-three-moments.json")
PILOT = ((1, 1, 1, 2), (1, 3, 3, 3))


def canonical_cases():
    cases = []
    for relation in itertools.combinations_with_replacement(range(1, BOUND + 1), 4):
        if math.gcd(*relation) != 1:
            continue
        if any(sum(a * s for a, s in zip(relation, signs)) == 0
               for signs in itertools.product((-1, 1), repeat=4)):
            continue
        cases.append({"relation": list(relation),
                      "sigma_values": [1] if sum(relation) % 2 else [1, -1]})
    assert len(cases) == 42
    return {"coefficient_bound": BOUND, "positive_sorted_primitive_full_support": True,
            "balanced_partitions_excluded": True, "cases": cases}


def binomial_rows(nmax):
    return [[math.comb(n, k) for k in range(n + 1)] for n in range(nmax + 1)]


def walk_coefficient(n, vector, binomials):
    """Coefficient of z^vector in (sum_j(z_j+z_j^-1))^n."""
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


def orbit_representative(relation, sigma):
    signs = [1, 1, 1, 1]
    if sigma == -1:
        j = next(j for j, c in enumerate(relation) if c % 2)
        signs[j] = -1
    assert math.prod(e ** c for e, c in zip(signs, relation)) == sigma
    return signs


def moments(relation, sigma, binomials, degree=DEGREE):
    """M_k=integral (2 sum epsilon_j sin(theta_j))^(2k) on H_c."""
    coefficient_sum = sum(relation)
    result = []
    for k in range(degree + 1):
        n = 2 * k
        value = walk_coefficient(n, (0, 0, 0, 0), binomials)
        for ell in range(1, n // coefficient_sum + 1):
            phase_numerator = ell * coefficient_sum
            if phase_numerator % 2:
                continue
            phase = (-1) ** (phase_numerator // 2) * sigma ** ell
            vector = tuple(ell * c for c in relation)
            value += 2 * phase * walk_coefficient(n, vector, binomials)
        assert value >= 0
        result.append(value)
    assert result[:3] == [1, 8, 168]
    return result


def logarithm_certificate(moment_values):
    degree = len(moment_values) - 1
    powers64 = [64 ** j for j in range(degree + 1)]
    residuals = []
    total = Fraction(0)
    previous_numerator = 1
    for j in range(1, degree + 1):
        numerator = sum((-1) ** k * math.comb(j, k) * moment_values[k]
                        * powers64[j - k] for k in range(j + 1))
        assert 0 <= numerator <= powers64[j]
        assert numerator <= 64 * previous_numerator
        previous_numerator = numerator
        residuals.append(numerator)
        total += Fraction(numerator, j * powers64[j])
    margin = 5 * total.numerator - 14 * total.denominator
    return {
        "degree": degree,
        "moments": [str(value) for value in moment_values],
        "residual_numerators_denominator_64_power_j": [str(value) for value in residuals],
        "sum_numerator": str(total.numerator),
        "sum_denominator": str(total.denominator),
        "comparison_5_num_minus_14_den": str(margin),
        "passed_strict_sum_gt_14_over_5": margin > 0,
        "sum_floor_scaled_10_power_12": str(total.numerator * 10 ** 12 // total.denominator),
    }


def multiply_walk(polynomial, signs, antisymmetric):
    result = {}
    for exponent, coefficient in polynomial.items():
        for j in range(4):
            for direction in (-1, 1):
                child = list(exponent)
                child[j] += direction
                child = tuple(child)
                factor = signs[j] * (direction if antisymmetric else 1)
                result[child] = result.get(child, 0) + coefficient * factor
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def small_exact_checks(binomials):
    # A separate finite expansion, with no use of the binomial formula.
    polynomial = {(0, 0, 0, 0): 1}
    checked = 0
    for n in range(9):
        for exponent, coefficient in polynomial.items():
            assert walk_coefficient(n, exponent, binomials) == coefficient
            checked += 1
        if n < 8:
            polynomial = multiply_walk(polynomial, (1, 1, 1, 1), False)
    comparisons = []
    for relation in PILOT:
        for sigma in (1, -1):
            signs = orbit_representative(relation, sigma)
            expected = moments(relation, sigma, binomials, degree=5)
            polynomial = {(0, 0, 0, 0): 1}
            actual = []
            for n in range(11):
                if n % 2 == 0:
                    coefficient_sum = 0
                    for exponent, coefficient in polynomial.items():
                        if exponent[0] % relation[0]:
                            continue
                        ell = exponent[0] // relation[0]
                        if all(v == ell * c for v, c in zip(exponent, relation)):
                            coefficient_sum += coefficient
                    actual.append((-1) ** (n // 2) * coefficient_sum)
                if n < 10:
                    polynomial = multiply_walk(polynomial, signs, True)
            assert actual == expected
            comparisons.append({"relation": relation, "sigma": sigma,
                                "moments_through_order_5": actual})
    return {"walk_expansion_degrees": [0, 8], "coefficient_equalities": checked,
            "signed_restriction_comparisons": comparisons,
            "relationship": "Author self-check by direct integer Laurent expansion; not independent review."}


def selected_certificate(result):
    if not result["full_scope_completed"] or not result["all_completed_cases_have_a_passing_sign"]:
        raise ValueError("A selected full certificate requires all 42 cases and a passing sign in each.")
    rows = []
    for case in result["cases"]:
        witness = next(row for row in case["attempts"]
                       if row["passed_strict_sum_gt_14_over_5"])
        rows.append({"relation": list(case["relation"]), "sigma": witness["sigma"],
                     "sum_numerator": witness["sum_numerator"],
                     "sum_denominator": witness["sum_denominator"],
                     "comparison_5_num_minus_14_den": witness["comparison_5_num_minus_14_den"]})
    return {"coefficient_bound": BOUND, "degree": DEGREE, "threshold": [14, 5],
            "case_count": len(rows), "cases": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Compute the entire declared 42-case scope.")
    parser.add_argument("--prepare-input", action="store_true", help="Exclusively create the generated fixed case input.")
    certificate_action = parser.add_mutually_exclusive_group()
    certificate_action.add_argument("--write-certificate", action="store_true",
                                    help="Exclusively create the selected full exact certificate; requires --all.")
    certificate_action.add_argument("--verify-certificate", action="store_true",
                                    help="Recompute and compare all selected certificate fields; requires --all.")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    if (args.write_certificate or args.verify_certificate) and not args.all:
        parser.error("Selected-certificate operations require --all.")
    required = canonical_cases()
    if args.prepare_input:
        INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with INPUT_PATH.open("x", encoding="utf-8") as stream:
            json.dump(required, stream, indent=2)
            stream.write("\n")
    actual_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    if actual_input != required:
        raise ValueError("The retained cases do not equal the regenerated declared scope.")
    binomials = binomial_rows(2 * DEGREE)
    checks = small_exact_checks(binomials)
    selected = [case for case in required["cases"]
                if args.all or tuple(case["relation"]) in PILOT]
    rows = []
    for case in selected:
        relation = tuple(case["relation"])
        attempts = []
        for sigma in case["sigma_values"]:
            certificate = logarithm_certificate(moments(relation, sigma, binomials))
            certificate["sigma"] = sigma
            certificate["sign_representative"] = orbit_representative(relation, sigma)
            attempts.append(certificate)
            if certificate["passed_strict_sum_gt_14_over_5"]:
                break
        passed = any(row["passed_strict_sum_gt_14_over_5"] for row in attempts)
        rows.append({"relation": relation, "allowed_sigma_values": case["sigma_values"],
                     "attempts": attempts, "some_sign_passed": passed})
        print(relation, "PASS" if passed else "NOT CERTIFIED", "tried sigma",
              [row["sigma"] for row in attempts], "scaled floor sums",
              [row["sum_floor_scaled_10_power_12"] for row in attempts], flush=True)
    result = {
        "evidence": "Exact integer/Fraction finite certificate under the separately derived logarithm bridge; author checks, no independent review.",
        "python": sys.version,
        "coefficient_bound": BOUND,
        "degree": DEGREE,
        "full_declared_case_count": len(required["cases"]),
        "completed_case_count": len(rows),
        "full_scope_completed": args.all and len(rows) == 42,
        "all_completed_cases_have_a_passing_sign": all(row["some_sign_passed"] for row in rows),
        "exact_checks": checks,
        "cases": rows,
    }
    if args.write_certificate:
        with CERTIFICATE_PATH.open("x", encoding="utf-8") as stream:
            json.dump(selected_certificate(result), stream, indent=2)
            stream.write("\n")
        print("Wrote selected certificate", CERTIFICATE_PATH, flush=True)
    if args.verify_certificate:
        retained = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        if retained != selected_certificate(result):
            raise ValueError("Recomputed exact selected certificate differs from retained mathematical fields.")
        print("Verified all selected exact certificate fields", flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Wrote", args.output, flush=True)


if __name__ == "__main__":
    main()
