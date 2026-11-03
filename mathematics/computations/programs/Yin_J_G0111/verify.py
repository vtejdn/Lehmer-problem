"""Independent verification of J111's fixed 24 computed and 8 analytic cases.

No author helper is imported.
Integer-list convolution constructs the equations, and Fraction Euclidean
remainders produce the complete Sturm chains.
Only irreducibility is rechecked using the author's same SymPy engine.
The reconstruction numerators are checked even for rejected factors; this
does not exercise the absent admissible-field resultant/norm branch.
"""

import argparse
from fractions import Fraction
from functools import reduce
import itertools
import json
from math import comb, gcd, lcm
from pathlib import Path
import subprocess
import sys
import time

import sympy as sp


GRID = (-2, -1, 1, 2)
GROUP = Path(__file__).resolve().parent
OUTPUT = GROUP.parents[3] / "mathematics" / "computations" / "outputs" / GROUP.name
SOURCE = OUTPUT / "results.json"


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left, right):
    result = [0] * max(len(left), len(right))
    for j, value in enumerate(left):
        result[j] += value
    for j, value in enumerate(right):
        result[j] += value
    return trim(result)


def scale(poly, value):
    return trim([value * coefficient for coefficient in poly])


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def power(poly, exponent):
    result = [1]
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def monomial(degree, coefficient):
    return [0] * degree + [coefficient]


def rational_remainder(left, right):
    remainder = [Fraction(value) for value in left]
    divisor = [Fraction(value) for value in right]
    require(divisor != [0], "Division by zero polynomial")
    while remainder != [0] and len(remainder) >= len(divisor):
        offset = len(remainder) - len(divisor)
        ratio = remainder[-1] / divisor[-1]
        for j, coefficient in enumerate(divisor):
            remainder[offset + j] -= ratio * coefficient
        remainder = trim(remainder)
    return remainder


def positive_primitive_scale(poly):
    """Multiply by a strictly positive rational, never flip a Sturm sign."""
    denominator = lcm(*(value.denominator for value in poly))
    integers = [int(value * denominator) for value in poly]
    divisor = reduce(gcd, (abs(value) for value in integers))
    require(divisor > 0, "Zero Sturm polynomial")
    return [value // divisor for value in integers]


def variations(signs):
    return sum(left != right for left, right in zip(signs, signs[1:]))


def full_sturm(poly):
    derivative = [j * poly[j] for j in range(1, len(poly))]
    chain = [poly, positive_primitive_scale(list(map(Fraction, derivative)))]
    while True:
        remainder = rational_remainder(chain[-2], chain[-1])
        if remainder == [0]:
            break
        chain.append(positive_primitive_scale(scale(remainder, -1)))
    require(len(chain[-1]) == 1, "Factor is not squarefree")
    plus = [1 if item[-1] > 0 else -1 for item in chain]
    minus = [
        sign * (-1 if (len(item) - 1) % 2 else 1)
        for sign, item in zip(plus, chain)
    ]
    vminus, vplus = variations(minus), variations(plus)
    return {
        "degrees": [len(item) - 1 for item in chain],
        "signs_minus_infinity": minus,
        "signs_plus_infinity": plus,
        "variations_minus_infinity": vminus,
        "variations_plus_infinity": vplus,
        "distinct_real_roots": vminus - vplus,
        "terminal_constant": str(chain[-1][0]),
        "complete_chain_to_constant": True,
    }


def read_data():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    require(data["complete"] is True, "Author output is incomplete")
    require(data["grid"] == {"u": list(GRID), "v": list(GRID), "s": [-1, 1]},
            "Wrong declared parameter grid")
    require(data["limits"] == {"per_case_seconds": 15, "whole_pass_seconds": 120},
            "Author resource scope changed")
    expected = set(itertools.product(GRID, GRID, (-1, 1)))
    even = {case for case in expected if case[0] % 2 == case[1] % 2 == 0}
    cases = {(row["u"], row["v"], row["s"]): row for row in data["cases"]}
    analytic = {(row["u"], row["v"], row["s"]): row
                for row in data["analytic_even_even"]}
    require(len(cases) == len(data["cases"]) == 24, "Duplicate or missing cases")
    require(len(analytic) == len(data["analytic_even_even"]) == 8,
            "Duplicate or missing analytic cases")
    require(set(cases) == expected - even and set(analytic) == even,
            "The exact 32-case partition is not preserved")
    require(all(row["bound"] == "abs Norm_F(g)>=2^r" for row in analytic.values()),
            "Analytic bound differs from the declared C178 consequence")
    return data, cases


def verify_case(case):
    u, v, sign = case["u"], case["v"], case["s"]
    # Direct binomial coefficients, rather than the author's Poly composition.
    b2 = [comb(2, j) * u**j * v**(2 - j) for j in range(3)]
    b5 = [comb(5, j) * u**j * v**(5 - j) for j in range(6)]
    g = add(monomial(3, 1), scale(b5, -2))
    q = add(b2, scale(g, sign))
    q5 = power(q, 5)
    h = add(scale(q5, 27), monomial(6, -8))
    require(list(reversed(q)) == list(map(int, case["Q_descending"])),
            "Q coefficients disagree")
    require(list(reversed(h)) == list(map(int, case["H_descending"])),
            "H coefficients disagree")
    require(len(h) - 1 == 25, "Unexpected elimination degree")
    integer_content = reduce(gcd, (abs(value) for value in h))
    signed_content = integer_content * (1 if h[-1] > 0 else -1)
    require(signed_content == int(case["content"]), "Content or sign disagrees")
    require(case["factorization_reconstructed"] is True, "Author product check absent")

    # a = numerator / denominator. Check both exact cleared identities.
    numerator = scale(power(q, 2), 3)
    denominator = monomial(2, 2)
    cube_left = add(power(numerator, 3), scale(multiply(q, power(denominator, 3)), -1))
    fifth_left = add(scale(power(numerator, 5), 3),
                     scale(multiply(monomial(2, 2), power(denominator, 5)), -1))
    require(cube_left == multiply(q, h), "Cleared a^3 identity failed")
    require(fifth_left == multiply(h, add(scale(q5, 27), monomial(6, 8))),
            "Cleared a^5 identity failed")

    product = [signed_content]
    verified_factors = []
    require(len(case["factors"]) == 1, "Reported one-factor result changed")
    for row in case["factors"]:
        factor = list(reversed(list(map(int, row["factor_descending"]))))
        require(factor == trim(factor), "Noncanonical factor coefficients")
        degree, multiplicity = len(factor) - 1, row["multiplicity"]
        require(degree == row["degree"] == 25 and multiplicity == 1,
                "Factor degree or multiplicity disagrees")
        require(reduce(gcd, (abs(value) for value in factor)) == 1,
                "Factor is not primitive")
        expected_lc = 864 if abs(u) == 1 else 28991029248
        require(factor[-1] == int(row["leading_coefficient"]) == expected_lc,
                "Factor leading coefficient or sign disagrees")
        require(factor[-1] > 1 and row["disposition"] == "nonintegral_root",
                "Expected nonmonic exclusion changed")
        polynomial = sp.Poly.from_list(list(reversed(factor)), sp.Symbol("Y"),
                                       domain=sp.QQ)
        require(polynomial.is_irreducible is True,
                "Same-engine irreducibility recheck failed")
        sturm = full_sturm(factor)
        require(sturm["distinct_real_roots"] == row["distinct_real_roots"],
                "Independent full Sturm count disagrees")
        require(sturm["distinct_real_roots"] in (1, 3), "Unexpected real-root count")
        require(not any(key in row for key in
                        ("norm_g", "norm_square", "target_square", "a_descending")),
                "A purported unexercised admissible branch has output")
        product = multiply(product, power(factor, multiplicity))
        verified_factors.append({
            "degree": degree,
            "multiplicity": multiplicity,
            "leading_coefficient": str(factor[-1]),
            "primitive_positive_leading": True,
            "irreducible_over_Q_same_sympy_engine": True,
            "sturm": sturm,
            "disposition": "nonintegral_root",
        })
    require(product == h, "Complete factor product does not reconstruct H")
    return {
        "u": u, "v": v, "s": sign,
        "all_coefficients_content_and_product_match": True,
        "cleared_reconstruction_identities": True,
        "factors": verified_factors,
    }


def publish(path, payload):
    intermediate = path.with_suffix(".pending.json")
    intermediate.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    intermediate.replace(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--one-case", nargs=3, type=int)
    args = parser.parse_args()
    data, cases = read_data()
    if args.one_case is not None:
        selected = tuple(args.one_case)
        require(selected in cases, "Outside the declared 24 computed cases")
        print(json.dumps(verify_case(cases[selected])))
        return

    result = {
        "complete": False,
        "author_input": "results.json",
        "sympy_version": sp.__version__,
        "coefficient_and_sturm_arithmetic": "Python integers and Fraction",
        "irreducibility_limitation": "Same SymPy engine as main.py",
        "grid": data["grid"],
        "limits": {"per_case_seconds": 15, "whole_pass_seconds": 120},
        "computed_case_count": 24,
        "analytic_even_even_case_count": 8,
        "analytic_even_even_bound": "C178 consequence reviewed in the accompanying R",
        "admissible_norm_branch_exercised": False,
        "cases": [],
    }
    start = time.monotonic()
    try:
        for selected in sorted(cases):
            remaining = 120 - (time.monotonic() - start)
            require(remaining > 0, "Verification whole-pass limit reached")
            process = subprocess.run(
                [sys.executable, "-B", str(Path(__file__).resolve()), "--one-case",
                 *map(str, selected)],
                capture_output=True, text=True, encoding="utf-8",
                timeout=min(15, remaining), check=True,
            )
            result["cases"].append(json.loads(process.stdout))
        require(json.loads(SOURCE.read_text(encoding="utf-8")) == data,
                "Author mathematical input changed during verification")
        require(len(result["cases"]) == 24, "Incomplete verification")
        result["complete"] = True
        publish(OUTPUT / "verification.json", result)
        print(json.dumps({
            "complete": True, "verified_computed_cases": 24,
            "checked_analytic_case_labels": 8, "nonintegral_factors": 24,
            "admissible_norm_branch_exercised": False,
        }))
    except Exception as error:
        result["failure"] = type(error).__name__ + ": " + str(error)
        publish(OUTPUT / "verification-incomplete.json", result)
        raise


if __name__ == "__main__":
    main()
