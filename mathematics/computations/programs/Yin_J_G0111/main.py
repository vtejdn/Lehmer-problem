"""Exact, bounded affine residual screen; see the predeclared README."""
import argparse
import itertools
import json
from pathlib import Path
import subprocess
import sys
import time

import sympy as sp


GRID = (-2, -1, 1, 2)
X = sp.Symbol("X")


def coefficients(poly):
    return [str(value) for value in poly.all_coeffs()]


def one_case(u, v, sign):
    b = sp.Poly(u * X + v, X, domain=sp.ZZ)
    g = sp.Poly(X**3 - 2 * b.as_expr()**5, X, domain=sp.ZZ)
    q = b**2 + sign * g
    h = 27 * q**5 - sp.Poly(8 * X**6, X, domain=sp.ZZ)
    content, factors = sp.factor_list(h)
    rebuilt = sp.Poly(content, X, domain=sp.ZZ)
    rows = []
    for factor, multiplicity in factors:
        rebuilt *= factor**multiplicity
        row = {
            "factor_descending": coefficients(factor),
            "degree": factor.degree(),
            "multiplicity": multiplicity,
            "leading_coefficient": str(factor.LC()),
        }
        real_count = int(factor.count_roots(-sp.oo, sp.oo))
        row["distinct_real_roots"] = real_count
        if abs(factor.LC()) != 1:
            row["disposition"] = "nonintegral_root"
        elif real_count != factor.degree():
            row["disposition"] = "not_totally_real"
        else:
            f = factor.monic().set_domain(sp.QQ)
            b0, g0, q0 = (p.set_domain(sp.QQ).rem(f) for p in (b, g, q))
            x0 = sp.Poly(X, X, domain=sp.QQ).rem(f)
            if x0.is_zero or b0.is_zero or g0.is_zero:
                row["disposition"] = "zero_original_value"
            else:
                inverse_x2 = sp.invert(x0**2, f)
                a0 = (sp.Rational(3, 2) * q0**2 * inverse_x2).rem(f)
                checks = (
                    (a0**3 - q0).rem(f),
                    (3 * a0**5 - 2 * x0**2).rem(f),
                    (b0**2 - a0**3 + sign * g0).rem(f),
                    (g0 - x0**3 + 2 * b0**5).rem(f),
                )
                if a0.is_zero or not all(check.is_zero for check in checks):
                    raise ArithmeticError("Reconstruction failed")
                norm_g = sp.resultant(f, g0)
                if norm_g.q != 1 or norm_g == 0:
                    raise ArithmeticError("Nonzero integral norm check failed")
                row.update(
                    a_descending=coefficients(a0),
                    g_descending=coefficients(g0),
                    exact_identities=True,
                    norm_g=str(norm_g),
                    norm_square=str(norm_g**2),
                    target_square=str(2**f.degree()),
                    disposition=(
                        "admissible_violation"
                        if norm_g**2 < 2**f.degree()
                        else "admissible_floor"
                    ),
                )
        rows.append(row)
    if rebuilt != h:
        raise ArithmeticError("Complete factorization reconstruction failed")
    return {
        "u": u,
        "v": v,
        "s": sign,
        "Q_descending": coefficients(q),
        "H_descending": coefficients(h),
        "content": str(content),
        "factorization_reconstructed": True,
        "factors": rows,
    }


def publish(path, payload):
    temporary = path.with_suffix(".pending.json")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--one-case", nargs=3, type=int)
    args = parser.parse_args()
    if args.one_case is not None:
        u, v, sign = args.one_case
        if u not in GRID or v not in GRID or sign not in (-1, 1):
            raise ValueError("Outside the predeclared grid")
        print(json.dumps(one_case(u, v, sign)))
        return

    group = Path(__file__).resolve().parent
    repository = group.parents[3]
    output = repository / "mathematics" / "computations" / "outputs" / group.name
    output.mkdir(parents=True, exist_ok=True)
    result = {
        "complete": False,
        "arithmetic": "exact ZZ/QQ factorization and Sturm counts",
        "sympy_version": sp.__version__,
        "grid": {"u": list(GRID), "v": list(GRID), "s": [-1, 1]},
        "limits": {"per_case_seconds": 15, "whole_pass_seconds": 120},
        "analytic_even_even": [],
        "cases": [],
    }
    start = time.monotonic()
    try:
        for u, v, sign in itertools.product(GRID, GRID, (-1, 1)):
            if u % 2 == 0 and v % 2 == 0:
                result["analytic_even_even"].append(
                    {"u": u, "v": v, "s": sign, "bound": "abs Norm_F(g)>=2^r"}
                )
                continue
            remaining = 120 - (time.monotonic() - start)
            if remaining <= 0:
                raise TimeoutError("Whole-pass bound reached")
            child = subprocess.run(
                [sys.executable, "-B", str(Path(__file__).resolve()),
                 "--one-case", str(u), str(v), str(sign)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=min(15, remaining),
                check=True,
            )
            result["cases"].append(json.loads(child.stdout))
        if len(result["cases"]) != 24 or len(result["analytic_even_even"]) != 8:
            raise ArithmeticError("Incomplete grid")
        result["complete"] = True
        publish(output / "results.json", result)
        counts = {}
        for case in result["cases"]:
            for factor in case["factors"]:
                key = factor["disposition"]
                counts[key] = counts.get(key, 0) + 1
        print(json.dumps({"complete": True, "cases": 24,
                          "analytic_cases": 8, "factor_dispositions": counts}))
    except Exception as error:
        result["failure"] = type(error).__name__ + ": " + str(error)
        publish(output / "incomplete.json", result)
        raise


if __name__ == "__main__":
    main()
