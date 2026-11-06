"""Only n=5,7,9,13: exact moving-map factors, then 50-digit full-root diagnostics."""

from __future__ import annotations

import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as sp


Z = sp.Symbol("z")
INPUTS = (5, 7, 9, 13)
DIGITS = 50
MAXSTEPS = 200
GROUP = Path(__file__).resolve().parent
OUTPUT = GROUP.parent.parent / "outputs" / GROUP.name
SEED = sp.Poly(Z**10 + Z**9 - Z**7 - Z**6 - Z**5 - Z**4 - Z**3 + Z + 1, Z, domain=sp.ZZ)


def coefficients(poly: sp.Poly) -> list[int]:
    return [int(c) for c in poly.all_coeffs()]


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def construct(n: int) -> tuple[sp.Poly, sp.Poly, sp.Poly]:
    assert n in INPUTS
    g = sp.Poly(Z**n - Z - 1, Z, domain=sp.ZZ)
    star = sp.Poly(1 - Z**(n - 1) - Z**n, Z, domain=sp.ZZ)
    assert coefficients(star) == coefficients(g)[::-1]
    assert sp.gcd(g, star).degree() == 0
    assert g.eval(1) == -1 and g.eval(-1) == -1
    assert star.eval(1) == -1 and star.eval(-1) == 1
    assert sp.Poly(g.as_expr() - star.as_expr(), Z, modulus=2).as_expr() != 0
    result = sp.Poly(SEED.LC(), Z, domain=sp.ZZ)
    power = sp.Poly(1, Z, domain=sp.ZZ)
    for coefficient in SEED.all_coeffs()[1:]:
        power *= g
        result = result * star + coefficient * power
    return result, g, star


def exact_analysis(n: int) -> dict:
    polynomial, g, star = construct(n)
    coeffs = coefficients(polynomial)
    assert polynomial.degree() == 10 * n
    assert polynomial.LC() == 1 and polynomial.TC() == 1
    assert coeffs == coeffs[::-1]
    assert polynomial.eval(1) == -1 and polynomial.eval(-1) == 1
    print(f"n={n}: exact factorization over ZZ, degree {polynomial.degree()}", flush=True)
    content, factors = sp.factor_list(polynomial)
    assert content == 1
    reconstruction = sp.Poly(content, Z, domain=sp.ZZ)
    rows = []
    for factor, multiplicity in factors:
        assert factor.LC() == 1 and abs(factor.TC()) == 1
        reconstruction *= factor**multiplicity
        rows.append({
            "degree": factor.degree(),
            "multiplicity": int(multiplicity),
            "coefficients_descending": coefficients(factor),
            "cyclotomic": bool(factor.is_cyclotomic),
        })
    assert reconstruction == polynomial
    degree_sum = sum(row["degree"] * row["multiplicity"] for row in rows)
    assert degree_sum == polynomial.degree()
    positive_count = sum(row["multiplicity"] for row in rows if not row["cyclotomic"])
    cyclotomic_degree = sum(row["degree"] * row["multiplicity"] for row in rows if row["cyclotomic"])
    positive_degree = degree_sum - cyclotomic_degree
    result = {
        "n": n,
        "degree": polynomial.degree(),
        "g_coefficients_descending": coefficients(g),
        "g_star_coefficients_descending": coefficients(star),
        "coefficients_descending": coeffs,
        "maximum_absolute_coefficient": max(abs(c) for c in coeffs),
        "content": int(content),
        "exact_checks": {
            "g_and_g_star_coprime": True,
            "g_and_g_star_congruent_modulo_two": False,
            "monic": True,
            "constant_one": True,
            "reciprocal": True,
            "value_at_one": -1,
            "value_at_minus_one": 1,
            "factor_product_reconstructs_complete_input": True,
            "factor_degree_sum_equals_actual_degree": True,
        },
        "factors": rows,
        "positive_factor_count_with_multiplicity": positive_count,
        "cyclotomic_degree_with_multiplicity": cyclotomic_degree,
        "positive_degree_with_multiplicity": positive_degree,
    }
    print(f"EXACT n={n}: positive_count={positive_count}, cyclotomic_degree={cyclotomic_degree}, factors={[(r['degree'], r['multiplicity'], r['cyclotomic']) for r in rows]}", flush=True)
    return result


def root_diagnostics(factor: dict) -> dict:
    poly = sp.Poly.from_list(factor["coefficients_descending"], Z, domain=sp.ZZ)
    answer = {
        "degree": factor["degree"],
        "multiplicity": factor["multiplicity"],
        "cyclotomic": factor["cyclotomic"],
        "digits": DIGITS,
        "maxsteps": MAXSTEPS,
        "certified": False,
    }
    try:
        approximate_roots = poly.nroots(n=DIGITS, maxsteps=MAXSTEPS)
        assert len(approximate_roots) == poly.degree()
        with mp.workdps(DIGITS):
            roots = []
            for root in approximate_roots:
                real, imag = root.as_real_imag()
                roots.append(mp.mpc(str(real), str(imag)))
            if not all(mp.isfinite(root.real) and mp.isfinite(root.imag) for root in roots):
                raise ArithmeticError("A root has a nonfinite component")
            contributions = [max(mp.mpf(0), mp.log(abs(root))) for root in roots]
            coeffs = factor["coefficients_descending"]
            residuals = []
            for root in roots:
                value = mp.mpc(coeffs[0])
                scale = mp.mpf(abs(coeffs[0]))
                for coefficient in coeffs[1:]:
                    value = value * root + coefficient
                    scale = scale * abs(root) + abs(coefficient)
                residuals.append(abs(value) / scale)
            answer.update({
                "status": "completed",
                "root_count": len(roots),
                "raw_all_root_log_measure": mp.nstr(mp.fsum(contributions), DIGITS),
                "roots": [[mp.nstr(root.real, DIGITS), mp.nstr(root.imag, DIGITS)] for root in roots],
                "individual_log_plus_contributions": [mp.nstr(value, DIGITS) for value in contributions],
                "max_scaled_polynomial_residual": mp.nstr(max(residuals, default=mp.mpf(0)), DIGITS),
                "log_product_moduli": mp.nstr(mp.fsum(mp.log(abs(root)) for root in roots), DIGITS),
            })
    except Exception as error:
        answer.update({"status": "failed", "error": f"{type(error).__name__}: {error}"})
    return answer


def numerical_analysis(record: dict) -> dict:
    n = record["n"]
    rows = []
    for index, factor in enumerate(record["factors"], start=1):
        print(f"n={n}: 50-digit roots for factor {index}/{len(record['factors'])}, degree {factor['degree']}", flush=True)
        rows.append(root_diagnostics(factor))
    result = {"n": n, "degree": record["degree"], "certified": False, "factors": rows}
    if all(row["status"] == "completed" for row in rows):
        with mp.workdps(DIGITS):
            raw = mp.fsum(row["multiplicity"] * mp.mpf(row["raw_all_root_log_measure"]) for row in rows)
            positive = [mp.mpf(row["raw_all_root_log_measure"]) for row in rows if not row["cyclotomic"]]
            total = mp.fsum(row["multiplicity"] * mp.mpf(row["raw_all_root_log_measure"]) for row in rows if not row["cyclotomic"])
            result.update({
                "status": "completed",
                "raw_all_factor_root_sum": mp.nstr(raw, DIGITS),
                "total_with_exact_zero_cyclotomic_cost": mp.nstr(total, DIGITS),
                "minimum_positive_factor_measure": mp.nstr(min(positive), DIGITS) if positive else None,
            })
    else:
        result.update({"status": "incomplete", "reason": "At least one numerical root calculation failed"})
    print(f"NUMERIC n={n}: status={result['status']}, total={result.get('total_with_exact_zero_cyclotomic_cost')}", flush=True)
    return result


def main() -> None:
    metadata = {
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "mpmath": mp.__version__,
        "assigned_n": list(INPUTS),
        "nroots_digits": DIGITS,
        "nroots_maxsteps": MAXSTEPS,
        "numeric_measures_certified": False,
        "seed_coefficients_descending": coefficients(SEED),
        "n3_recomputed": False,
    }
    exact = [exact_analysis(n) for n in INPUTS]
    atomic_json(OUTPUT / "exact_results.json", {"metadata": metadata, "status": "completed", "results": exact})
    print("All four exact factorizations completed; beginning numerical diagnostics in the same process", flush=True)
    summaries = []
    for record in exact:
        numeric = numerical_analysis(record)
        filename = f"roots_n{record['n']}.json"
        atomic_json(OUTPUT / filename, {"metadata": metadata, "result": numeric})
        summaries.append({
            "n": record["n"],
            "degree": record["degree"],
            "positive_factor_count_with_multiplicity": record["positive_factor_count_with_multiplicity"],
            "cyclotomic_degree_with_multiplicity": record["cyclotomic_degree_with_multiplicity"],
            "numerical_status": numeric["status"],
            "uncertified_total_measure": numeric.get("total_with_exact_zero_cyclotomic_cost"),
            "uncertified_minimum_positive_factor_measure": numeric.get("minimum_positive_factor_measure"),
            "root_data_file": filename,
        })
    atomic_json(OUTPUT / "results.json", {"metadata": metadata, "results": summaries})
    print("Finished only the four assigned inputs", flush=True)


if __name__ == "__main__":
    main()
