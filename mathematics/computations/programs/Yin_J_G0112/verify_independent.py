"""Independent same-scope verification of the retained J112 four-case payload.

Declared before this verifier's first execution, 2026-10-20:
only the original 32 parameter labels and their four retained representatives
are permitted.  The original mathematical program is neither imported nor run.
Python integers, binomial coefficients, Fraction, and independent polynomial
arrays reconstruct every coefficient, denominator and factor product.
The separate factor irreducibility check uses SymPy Poly.is_irreducible:
this is an explicitly SHARED symbolic engine, not an independent backend.
Limits: 15 seconds per irreducibility worker, 60 seconds for this verification
pass, 64 MiB total native output.  No retry, larger grid or extra prime search.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, gcd
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[3]
OUTPUT = REPOSITORY / "mathematics" / "computations" / "outputs" / HERE.name
EXPECTED = [[1, 2, -1], [-1, 2, -1], [2, 1, 1], [-2, 1, 1]]
LIMITS = {
    "per_case_seconds": 15,
    "whole_pass_seconds": 60,
    "output_bytes": 64 * 1024 * 1024,
}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trim(values):
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def add(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def scale(values, scalar):
    return trim([scalar * item for item in values])


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def power(values, exponent):
    result = [1]
    for _ in range(exponent):
        result = multiply(result, values)
    return result


def linear_power(u, v, exponent):
    # Direct binomial construction of (u X + 3 v)^exponent.
    return [
        comb(exponent, k) * u**k * (3 * v)**(exponent - k)
        for k in range(exponent + 1)
    ]


def parse_integer_descending(values):
    require(isinstance(values, list) and 1 <= len(values) <= 26,
            "Polynomial outside the declared degree-25 window")
    result = []
    for value in reversed(values):
        item = Fraction(value)
        require(item.denominator == 1, "Noninteger claimed ZZ coefficient")
        result.append(item.numerator)
    require(len(trim(result.copy())) == len(result),
            "Uncollected leading zero coefficient")
    return result


def compare_rational_descending(values, numerator, denominator, label):
    actual = [Fraction(value) for value in values]
    expected = [Fraction(value, denominator) for value in reversed(numerator)]
    require(actual == expected, label + " coefficient mismatch")


def load_payload():
    inputs = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    require(inputs == {
        "original_u": [-2, -1, 1, 2],
        "original_v": [-2, -1, 1, 2],
        "original_s": [-1, 1],
        "denominator": 3,
        "representatives": EXPECTED,
        "remaining_degree": 5,
        "limits": LIMITS,
    }, "Declared domain or limits changed")
    payload = json.loads((OUTPUT / "results.json").read_text(encoding="utf-8"))
    require(payload["complete"] is True, "Author pass is not complete")
    require(payload["inputs"] == inputs, "Output scope differs from input")
    require(len(payload["cases"]) == 4, "Missing or extra representative")
    require([[case["u"], case["v"], case["s"]]
             for case in payload["cases"]] == EXPECTED,
            "Representative labels or order differ")
    return inputs, payload


def verify_labels(inputs):
    family = [
        (u, v, sign)
        for u in inputs["original_u"]
        for v in inputs["original_v"]
        for sign in inputs["original_s"]
    ]
    survivors = [
        case for case in family
        if case[0] % 2 != case[1] % 2
        and case[1] % 3 == case[2] % 3
    ]
    representatives = {
        (u, v, sign) if v > 0 else (u, -v, -sign)
        for u, v, sign in survivors
    }
    require(len(family) == 32 and len(survivors) == 8,
            "Finite analytic-filter label count differs")
    require(representatives == {tuple(row) for row in EXPECTED},
            "Sign symmetry does not give the declared representatives")
    return {
        "original_labels": 32,
        "surviving_labels": [list(row) for row in survivors],
        "representatives": EXPECTED,
        "boundary": "Enumeration checks the declared necessary filters only; "
                    "their original-domain proof is checked separately in R.",
    }


def verify_coefficients(case):
    u, v, sign = case["u"], case["v"], case["s"]
    # 3^5 Q = 27 (uX+3v)^2 + 243 s X^3 - 2s (uX+3v)^5.
    q_numerator = add(
        add(scale(linear_power(u, v, 2), 27),
            [0, 0, 0, 243 * sign]),
        scale(linear_power(u, v, 5), -2 * sign),
    )
    denominator = 3**22
    # 27 Q^5 - 8 X^6 = (q_numerator^5 - 8*3^22 X^6)/3^22.
    integer_polynomial = add(
        power(q_numerator, 5),
        [0] * 6 + [-8 * denominator],
    )
    require(len(integer_polynomial) == 26, "Wrong independent degree")
    require(gcd(integer_polynomial[-1], 3) == 1,
            "Claimed denominator minimality not supplied")
    require(int(case["clearing_denominator"]) == denominator,
            "Clearing denominator differs")
    compare_rational_descending(case["b_descending"], [3 * v, u], 3, "b")
    compare_rational_descending(case["Q_descending"], q_numerator, 243, "Q")
    compare_rational_descending(case["H_rational_descending"],
                               integer_polynomial, denominator, "Rational H")
    require(parse_integer_descending(case["H_integer_descending"])
            == integer_polynomial, "Cleared H coefficient mismatch")
    content = int(case["factor_content"])
    coefficient_gcd = 0
    for value in integer_polynomial:
        coefficient_gcd = gcd(coefficient_gcd, abs(value))
    require(abs(content) == coefficient_gcd, "Incorrect polynomial content")
    rebuilt = [content]
    require(len(case["factors"]) == 1,
            "Actual retained factor branch changed; review required")
    factors = []
    for row in case["factors"]:
        factor = parse_integer_descending(row["factor_descending"])
        multiplicity = row["multiplicity"]
        require(multiplicity == 1, "Unexpected retained multiplicity")
        require(row["degree"] == len(factor) - 1 == 25,
                "Incorrect factor degree")
        require(int(row["leading_coefficient"]) == factor[-1],
                "Incorrect factor leading coefficient")
        primitive_gcd = 0
        for value in factor:
            primitive_gcd = gcd(primitive_gcd, abs(value))
        require(primitive_gcd == 1, "Factor not primitive")
        require(abs(factor[-1]) > 1, "Nonmonic disposition not applicable")
        require(row["disposition"] == "nonintegral_c",
                "Wrong actual factor disposition")
        require("distinct_real_roots" not in row and "b_integral" not in row
                and "norm_g" not in row,
                "Conditional branch was reported as executed")
        rebuilt = multiply(rebuilt, factor)
        factors.append({
            "degree": 25,
            "multiplicity": multiplicity,
            "leading_coefficient": factor[-1],
            "primitive": True,
            "disposition": row["disposition"],
        })
    require(rebuilt == integer_polynomial, "Independent full product failed")
    require(case["factorization_reconstructed"] is True,
            "Author product status is not successful")
    return {
        "parameters": [u, v, sign],
        "all_b_Q_H_coefficients_match": True,
        "minimal_clearing_denominator": denominator,
        "signed_content": content,
        "complete_factor_product_matches": True,
        "factors": factors,
    }


def shared_irreducibility_worker(case_index, payload):
    import sympy as sp
    x = sp.Symbol("X")
    rows = payload["cases"][case_index]["factors"]
    checks = []
    for row in rows:
        coefficients = [int(value) for value in row["factor_descending"]]
        factor = sp.Poly.from_list(coefficients, x, domain=sp.ZZ)
        checks.append(bool(factor.is_irreducible))
    require(all(checks), "Shared-engine irreducibility recheck failed")
    return {
        "sympy_version": sp.__version__,
        "method": "Poly.is_irreducible on each retained primitive factor",
        "shared_engine_with_author": True,
        "independent_symbolic_backend": False,
        "irreducible": checks,
    }


def publish(payload):
    target = OUTPUT / "verification.json"
    temporary = OUTPUT / "verification.json.pending"
    raw = (json.dumps(payload, indent=2) + "\n").encode("utf-8")
    existing = sum(
        path.stat().st_size for path in OUTPUT.iterdir()
        if path.is_file() and path not in (target, temporary)
    )
    require(existing + len(raw) <= LIMITS["output_bytes"],
            "Native output cap exceeded")
    temporary.write_bytes(raw)
    temporary.replace(target)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--irreducibility-case", type=int, choices=range(4))
    arguments = parser.parse_args()
    inputs, payload = load_payload()
    if arguments.irreducibility_case is not None:
        print(json.dumps(shared_irreducibility_worker(
            arguments.irreducibility_case, payload)))
        return
    start = time.monotonic()
    result = {
        "complete": False,
        "scope": "Exactly J112's four retained representatives",
        "construction_method": "Independent Python integer arrays, binomial "
                               "coefficients and Fraction comparisons",
        "main_program_imported_or_rerun": False,
        "cases": [],
    }
    try:
        result["label_check"] = verify_labels(inputs)
        for index, case in enumerate(payload["cases"]):
            row = verify_coefficients(case)
            remaining = LIMITS["whole_pass_seconds"] - (time.monotonic() - start)
            require(remaining > 0, "Whole verification limit reached")
            child = subprocess.run(
                [sys.executable, "-B", str(Path(__file__).resolve()),
                 "--irreducibility-case", str(index)],
                capture_output=True, text=True, encoding="utf-8",
                timeout=min(LIMITS["per_case_seconds"], remaining), check=True,
            )
            require(len(child.stdout.encode("utf-8")) <= LIMITS["output_bytes"],
                    "Worker output cap exceeded")
            row["shared_engine_irreducibility"] = json.loads(child.stdout)
            result["cases"].append(row)
        require(time.monotonic() - start <= LIMITS["whole_pass_seconds"],
                "Whole verification limit reached after final case")
        result["complete"] = True
        result["unexecuted_conditional_branches"] = [
            "Sturm real-root count", "rational-affine b integrality",
            "a reconstruction", "full original norm comparison",
        ]
        result["elapsed_seconds"] = time.monotonic() - start
        publish(result)
        print(json.dumps({
            "complete": True,
            "independent_coefficient_and_product_cases": 4,
            "shared_engine_irreducibility_checks": 4,
            "main_program_rerun": False,
        }))
    except Exception as error:
        result["failure"] = type(error).__name__ + ": " + str(error)
        result["elapsed_seconds"] = time.monotonic() - start
        publish(result)
        raise


if __name__ == "__main__":
    main()
