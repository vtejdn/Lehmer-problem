"""Exact four-case denominator-three screen; no numerical arithmetic."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

import sympy as sp

HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[3]
OUTPUT = REPOSITORY / "mathematics" / "computations" / "outputs" / HERE.name
X = sp.Symbol("X")


def coefficients(poly):
    return [str(value) for value in poly.all_coeffs()]


def load_inputs():
    data = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    expected = [[1, 2, -1], [-1, 2, -1], [2, 1, 1], [-2, 1, 1]]
    if data["representatives"] != expected:
        raise ValueError("The declared four-case domain changed")
    if (
        data["original_u"] != [-2, -1, 1, 2]
        or data["original_v"] != [-2, -1, 1, 2]
        or data["original_s"] != [-1, 1]
    ):
        raise ValueError("The declared original family changed")
    if data["denominator"] != 3 or data["remaining_degree"] != 5:
        raise ValueError("The declared arithmetic domain changed")
    if data["limits"] != {
        "per_case_seconds": 15,
        "whole_pass_seconds": 60,
        "output_bytes": 64 * 1024 * 1024,
    }:
        raise ValueError("The declared resource limits changed")
    return data


def one_case(u, v, sign):
    b = sp.Poly(sp.Rational(u, 3) * X + v, X, domain=sp.QQ)
    g = sp.Poly(X**3, X, domain=sp.QQ) - 2 * b**5
    q = b**2 + sign * g
    h = 27 * q**5 - sp.Poly(8 * X**6, X, domain=sp.QQ)
    denominator, cleared = h.clear_denoms(convert=True)
    if cleared.set_domain(sp.QQ) != denominator * h:
        raise ArithmeticError("Denominator clearing failed")
    content, factors = sp.factor_list(cleared)
    rebuilt = sp.Poly(content, X, domain=sp.ZZ)
    rows = []
    for factor, multiplicity in factors:
        rebuilt *= factor**multiplicity
        row = {
            "factor_descending": coefficients(factor),
            "degree": int(factor.degree()),
            "multiplicity": int(multiplicity),
            "leading_coefficient": str(factor.LC()),
        }
        if abs(factor.LC()) != 1:
            row["disposition"] = "nonintegral_c"
        elif factor.degree() != 5:
            row["disposition"] = "outside_remaining_low_norm_degree"
        else:
            f = factor.monic().set_domain(sp.QQ)
            real_count = int(f.count_roots(-sp.oo, sp.oo))
            row["distinct_real_roots"] = real_count
            if real_count != 5:
                row["disposition"] = "not_totally_real"
            else:
                # Invert the affine change c=3(b-v)/u.  This is the
                # exact monic minimal polynomial, not just an annihilator.
                b_minpoly = sp.Poly(
                    sp.Rational(u, 3)**5
                    * f.as_expr().subs(X, sp.Rational(3, u) * (X - v)),
                    X,
                    domain=sp.QQ,
                )
                if b_minpoly.degree() != 5 or b_minpoly.LC() != 1:
                    raise ArithmeticError("Affine minimal polynomial failed")
                row["b_minpoly_descending"] = coefficients(b_minpoly)
                b_integral = all(value.q == 1 for value in b_minpoly.all_coeffs())
                row["b_integral"] = b_integral
                if not b_integral:
                    row["disposition"] = "nonintegral_b"
                else:
                    b0, g0, q0 = (poly.rem(f) for poly in (b, g, q))
                    c0 = sp.Poly(X, X, domain=sp.QQ).rem(f)
                    if c0.is_zero or b0.is_zero or g0.is_zero:
                        row["disposition"] = "zero_original_value"
                    else:
                        a0 = (
                            sp.Rational(3, 2) * q0**2 * sp.invert(c0**2, f)
                        ).rem(f)
                        checks = [
                            (a0**3 - q0).rem(f),
                            (2 * c0**2 - 3 * a0**5).rem(f),
                            (b0**2 - a0**3 + sign * g0).rem(f),
                            (g0 - c0**3 + 2 * b0**5).rem(f),
                        ]
                        if a0.is_zero or not all(poly.is_zero for poly in checks):
                            raise ArithmeticError("Original equations failed")
                        # Integrality of a follows from a^3=q0 and the
                        # independently checked integral b,c.
                        norm_g = sp.resultant(f, g0)
                        if norm_g.q != 1 or norm_g == 0:
                            raise ArithmeticError("Full integral norm failed")
                        row.update(
                            a_descending=coefficients(a0),
                            b_descending=coefficients(b0),
                            g_descending=coefficients(g0),
                            exact_original_identities=True,
                            a_integral_via_cube=True,
                            norm_g=str(norm_g),
                            norm_square=str(norm_g**2),
                            target_square="32",
                            disposition=(
                                "admissible_violation"
                                if norm_g**2 < 32
                                else "admissible_floor"
                            ),
                        )
        rows.append(row)
    if rebuilt != cleared:
        raise ArithmeticError("Full factor product failed")
    return {
        "u": u,
        "v": v,
        "s": sign,
        "b_descending": coefficients(b),
        "Q_descending": coefficients(q),
        "H_rational_descending": coefficients(h),
        "clearing_denominator": str(denominator),
        "H_integer_descending": coefficients(cleared),
        "factor_content": str(content),
        "factorization_reconstructed": True,
        "factors": rows,
    }


def publish(name, payload, cap):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    target = OUTPUT / name
    temporary = OUTPUT / (name + ".pending")
    raw = (json.dumps(payload, indent=2) + "\n").encode("utf-8")
    existing = sum(
        path.stat().st_size
        for path in OUTPUT.iterdir()
        if path.is_file() and path not in (target, temporary)
    )
    if existing + len(raw) > cap:
        raise RuntimeError("Native output budget exceeded")
    temporary.write_bytes(raw)
    temporary.replace(target)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--one-case", nargs=3, type=int)
    arguments = parser.parse_args()
    inputs = load_inputs()
    if arguments.one_case is not None:
        if arguments.one_case not in inputs["representatives"]:
            raise ValueError("Outside the declared representatives")
        print(json.dumps(one_case(*arguments.one_case)))
        return
    result = {
        "complete": False,
        "inputs": inputs,
        "arithmetic": "exact QQ construction, ZZ factorization, conditional Sturm and norms",
        "sympy_version": sp.__version__,
        "cases": [],
    }
    limits = inputs["limits"]
    start = time.monotonic()
    try:
        for case in inputs["representatives"]:
            remaining = limits["whole_pass_seconds"] - (time.monotonic() - start)
            if remaining <= 0:
                raise TimeoutError("Whole-pass limit reached")
            child = subprocess.run(
                [sys.executable, "-B", str(Path(__file__).resolve()), "--one-case"]
                + [str(value) for value in case],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=min(limits["per_case_seconds"], remaining),
                check=True,
            )
            if len(child.stdout.encode("utf-8")) > limits["output_bytes"]:
                raise RuntimeError("Worker output budget exceeded")
            result["cases"].append(json.loads(child.stdout))
        elapsed = time.monotonic() - start
        if elapsed > limits["whole_pass_seconds"]:
            raise TimeoutError("Whole-pass limit reached after final case")
        if len(result["cases"]) != 4:
            raise ArithmeticError("Incomplete representative domain")
        result["complete"] = True
        result["elapsed_seconds"] = elapsed
        publish("results.json", result, limits["output_bytes"])
        dispositions = {}
        for case in result["cases"]:
            for row in case["factors"]:
                key = row["disposition"]
                dispositions[key] = dispositions.get(key, 0) + 1
        print(json.dumps({
            "complete": True,
            "computed_representatives": 4,
            "dispositions": dispositions,
        }))
    except Exception as error:
        result["failure"] = type(error).__name__ + ": " + str(error)
        result["elapsed_seconds"] = time.monotonic() - start
        publish("incomplete.json", result, limits["output_bytes"])
        raise


if __name__ == "__main__":
    main()
