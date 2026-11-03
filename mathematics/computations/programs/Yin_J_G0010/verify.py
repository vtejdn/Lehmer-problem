"""Independent SymPy reconstruction of the two exact modular controls.

The main program uses binary polynomial arithmetic and a Sylvester rank.
This verifier uses SymPy polynomial factorization, finite-field orders,
and factors the characteristic polynomial of an independently constructed
modular companion power. No main-program functions are imported.
"""
from __future__ import annotations

import json
import os
from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

# Keep this reconstruction independent of main.py's FLINT factorization.
# SymPy 1.14's FLINT wrapper also raises an ordering TypeError on these
# factors in the installed environment; the pure-Python backend avoids it.
os.environ["SYMPY_GROUND_TYPES"] = "python"
import sympy as sp

ROOT = _J_OUTPUT
x = sp.Symbol("x")


def code(poly: sp.Poly) -> int:
    return sum((int(poly.nth(i)) % 2) << i for i in range(poly.degree() + 1)) if poly else 0


def gf_power(base: sp.Poly, exponent: int, modulus: sp.Poly) -> sp.Poly:
    result = sp.Poly(1, x, modulus=2)
    while exponent:
        if exponent & 1:
            result = (result * base).rem(modulus)
        base = (base * base).rem(modulus)
        exponent //= 2
    return result


def matrix_power(matrix: sp.Matrix, exponent: int) -> sp.Matrix:
    result = sp.eye(matrix.rows)
    base = matrix
    while exponent:
        if exponent & 1:
            result = (result * base).applyfunc(lambda value: int(value) % 2)
        base = (base * base).applyfunc(lambda value: int(value) % 2)
        exponent //= 2
    return result


def factor_payload(poly: sp.Poly) -> list[dict]:
    return sorted(
        [{"code": code(f), "degree": int(f.degree()), "multiplicity": int(e)}
         for f, e in sp.factor_list(poly)[1]],
        key=lambda item: item["code"],
    )


def reconstruct(name: str, polynomial: sp.Poly) -> dict:
    degree = int(polynomial.degree())
    coefficients = [int(polynomial.nth(i)) for i in range(degree + 1)]
    reduced = sp.Poly(polynomial.as_expr(), x, modulus=2)
    gcd = sp.gcd(reduced, reduced.diff())
    assert gcd.degree() == 0 and reduced.nth(0) == 1
    order = 1
    factors = []
    for factor, multiplicity in sp.factor_list(reduced)[1]:
        assert multiplicity == 1
        candidate = 2 ** int(factor.degree()) - 1
        for prime in sp.factorint(candidate):
            prime = int(prime)
            while candidate % prime == 0:
                trial = candidate // prime
                if code(gf_power(sp.Poly(x, x, modulus=2), trial, factor)) != 1:
                    break
                candidate = trial
        assert code(gf_power(sp.Poly(x, x, modulus=2), candidate, factor)) == 1
        order = int(sp.ilcm(order, candidate))
        factors.append({"code": code(factor), "degree": int(factor.degree()), "order": candidate})
    assert code(gf_power(sp.Poly(x, x, modulus=2), order, reduced)) == 1
    order_prime_tests = {
        str(prime): code(gf_power(sp.Poly(x, x, modulus=2), order // int(prime), reduced))
        for prime in sp.factorint(order)
    }
    assert all(value != 1 for value in order_prime_tests.values())
    companion = sp.zeros(degree)
    for column in range(degree - 1):
        companion[column + 1, column] = 1
    for row in range(degree):
        companion[row, degree - 1] = -coefficients[row] % 2
    divisor_profiles = []
    candidates = []
    for a_sym in sp.divisors(order):
        a = int(a_sym)
        powered = matrix_power(companion, a)
        characteristic = sp.Poly(powered.charpoly(x).as_expr(), x, modulus=2)
        factorization = factor_payload(characteristic)
        nu = sum(item["degree"] * item["multiplicity"] ** 2 for item in factorization)
        assert sum(item["degree"] * item["multiplicity"] for item in factorization) == degree
        ratio = Fraction(2 ** nu, (2 * degree) ** degree)
        denominator = (2 * degree - 1) * 3 * a
        divisor_profiles.append({
            "a": a,
            "nu": nu,
            "power_remainder_code": code(gf_power(sp.Poly(x, x, modulus=2), a, reduced)),
            "characteristic_code": code(characteristic),
            "factorization": factorization,
            "ratio_numerator": str(ratio.numerator),
            "ratio_denominator": str(ratio.denominator),
            "entropy_denominator": denominator,
        })
        if ratio > 1:
            candidates.append((a, ratio))
    best_a = None
    best_ratio = None
    for a, ratio in candidates:
        if best_a is None or ratio ** best_a > best_ratio ** a:
            best_a, best_ratio = a, ratio
    return {
        "name": name,
        "coefficients": coefficients,
        "degree": degree,
        "modulus_code": code(reduced),
        "squarefree_gcd_code": code(gcd),
        "factor_orders": sorted(factors, key=lambda item: item["code"]),
        "order": order,
        "order_prime_tests": order_prime_tests,
        "divisor_profiles": divisor_profiles,
        "best_a": best_a,
    }


def build() -> list[dict]:
    lehmer = sp.Poly(x**10 + x**9 - x**7 - x**6 - x**5 - x**4 - x**3 + x + 1, x)
    quotient, remainder = sp.div(
        sp.Poly(x**24 - x**17 - x**12 - x**7 + 1, x),
        sp.Poly(x**2 - x + 1, x),
    )
    assert remainder.is_zero and quotient.degree() == 22
    return [reconstruct("lehmer", lehmer), reconstruct("degree22", quotient)]


def main() -> None:
    rebuilt = build()
    original = json.loads((ROOT / "result.json").read_text(encoding="utf-8"))
    inputs = original["inputs"]
    count = 0
    for actual in rebuilt:
        expected = next(item for item in inputs if item["name"] == actual["name"])
        for key in ("coefficients", "degree", "modulus_code", "order", "order_prime_tests", "best_a"):
            assert actual[key] == expected[key], (actual["name"], key, actual[key], expected[key])
            count += 1
        assert actual["squarefree_gcd_code"] == expected["squarefree_gcd_code"] == 1
        assert [(item["code"], item["degree"]) for item in actual["factor_orders"]] == [
            (item["code"], item["degree"]) for item in expected["gf2_factorization"]
        ]
        count += 1
        expected_profiles = {item["a"]: item for item in expected["divisor_profiles"]}
        assert set(expected_profiles) == {item["a"] for item in actual["divisor_profiles"]}
        count += 2
        for profile in actual["divisor_profiles"]:
            target = expected_profiles[profile["a"]]
            assert profile["nu"] == target["nu"]
            assert actual["degree"] ** 2 - profile["nu"] == target["sylvester_rank"]
            assert profile["power_remainder_code"] == target["power_remainder_code"]
            assert profile["ratio_numerator"] == target["entropy_log_ratio"]["numerator"]
            assert profile["ratio_denominator"] == target["entropy_log_ratio"]["denominator"]
            assert profile["entropy_denominator"] == target["entropy_denominator"]
            assert (int(profile["ratio_numerator"]) > int(profile["ratio_denominator"])) == target["positive_certificate"]
            count += 7
    payload = {
        "method": "Independent GF(2) factorization, orders and modular companion characteristic polynomials",
        "compared_mathematical_fields": count,
        "inputs": rebuilt,
        "status": "passed",
    }
    (ROOT / "verification.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "compared_mathematical_fields": count,
                      "controls": [{"name": item["name"], "order": item["order"],
                                    "best_a": item["best_a"]} for item in rebuilt]}))


if __name__ == "__main__":
    main()
