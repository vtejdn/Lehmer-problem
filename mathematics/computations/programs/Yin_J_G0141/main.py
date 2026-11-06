"""Exact n=1,2 cubic all-pass pullbacks with uncertified full-root diagnostics."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import platform

import mpmath as mp
import numpy as np
import sympy as sp


Z = sp.Symbol("z")
GROUP = Path(__file__).resolve().parent
OUTPUT = GROUP.parent.parent / "outputs" / GROUP.name
SEED = sp.Poly(Z**10 + Z**9 - Z**7 - Z**6 - Z**5 - Z**4 - Z**3 + Z + 1, Z, domain=sp.ZZ)
G = sp.Poly(Z**3 - Z - 1, Z, domain=sp.ZZ)
G_STAR = sp.Poly(1 - Z**2 - Z**3, Z, domain=sp.ZZ)


def coefficient_list(poly: sp.Poly) -> list[int]:
    """Descending coefficients, including all zero coefficients."""
    return [int(c) for c in poly.all_coeffs()]


def pullback(poly: sp.Poly) -> sp.Poly:
    """Homogeneous Horner evaluation of g^D P(g*/g) over ZZ."""
    coefficients = poly.all_coeffs()
    result = sp.Poly(coefficients[0], Z, domain=sp.ZZ)
    g_power = sp.Poly(1, Z, domain=sp.ZZ)
    for coefficient in coefficients[1:]:
        g_power *= G
        result = result * G_STAR + coefficient * g_power
    return result


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def full_root_diagnostics(poly: sp.Poly, digits: int) -> dict:
    """All roots contribute log(max(1,abs(root))); no exterior tolerance is used."""
    coefficients = coefficient_list(poly)
    answer = {"certified": False, "degree": poly.degree()}
    numpy_measure = None
    try:
        roots = np.roots(np.asarray(coefficients, dtype=np.float64))
        if len(roots) != poly.degree() or not np.all(np.isfinite(roots)):
            raise ArithmeticError("NumPy did not return the required finite root list")
        moduli = np.abs(roots)
        numpy_measure = math.fsum(math.log(max(1.0, float(value))) for value in moduli)
        residuals = []
        for root in roots:
            value = complex(coefficients[0])
            scale = float(abs(coefficients[0]))
            for coefficient in coefficients[1:]:
                value = value * root + coefficient
                scale = scale * abs(root) + abs(coefficient)
            residuals.append(float(abs(value) / scale))
        answer["numpy_float64"] = {
            "status": "completed",
            "log_measure": numpy_measure,
            "roots": [[float(root.real), float(root.imag)] for root in roots],
            "max_scaled_polynomial_residual": max(residuals, default=0.0),
            "log_product_moduli": math.fsum(math.log(float(value)) for value in moduli),
        }
    except Exception as error:
        answer["numpy_float64"] = {"status": "failed", "error": f"{type(error).__name__}: {error}"}

    try:
        roots = poly.nroots(n=digits, maxsteps=200)
        if len(roots) != poly.degree():
            raise ArithmeticError("SymPy nroots did not return the required root count")
        with mp.workdps(digits):
            converted = []
            for root in roots:
                real, imag = root.as_real_imag()
                converted.append(mp.mpc(str(real), str(imag)))
            if not all(mp.isfinite(root.real) and mp.isfinite(root.imag) for root in converted):
                raise ArithmeticError("Nonfinite high-precision root")
            contributions = [max(mp.mpf(0), mp.log(abs(root))) for root in converted]
            measure = mp.fsum(contributions)
            residuals = []
            for root in converted:
                value = mp.mpc(coefficients[0])
                scale = mp.mpf(abs(coefficients[0]))
                for coefficient in coefficients[1:]:
                    value = value * root + coefficient
                    scale = scale * abs(root) + abs(coefficient)
                residuals.append(abs(value) / scale)
            answer["sympy_nroots"] = {
                "status": "completed",
                "digits": digits,
                "maxsteps": 200,
                "log_measure": mp.nstr(measure, digits),
                "roots": [[mp.nstr(root.real, digits), mp.nstr(root.imag, digits)] for root in converted],
                "individual_log_plus_contributions": [mp.nstr(value, digits) for value in contributions],
                "max_scaled_polynomial_residual": mp.nstr(max(residuals, default=mp.mpf(0)), digits),
                "log_product_moduli": mp.nstr(mp.fsum(mp.log(abs(root)) for root in converted), digits),
            }
            if numpy_measure is not None:
                answer["absolute_measure_difference_between_methods"] = mp.nstr(abs(measure - mp.mpf(numpy_measure)), digits)
    except Exception as error:
        answer["sympy_nroots"] = {
            "status": "failed",
            "digits": digits,
            "maxsteps": 200,
            "error": f"{type(error).__name__}: {error}",
        }
    return answer


def analyze(poly: sp.Poly, iteration: int, digits: int) -> dict:
    expected_degree = 10 * 3**iteration
    coefficients = coefficient_list(poly)
    assert poly.degree() == expected_degree
    assert poly.LC() == 1 and poly.TC() == 1
    assert coefficients == coefficients[::-1]
    assert poly.eval(1) == -1 and poly.eval(-1) == 1
    print(f"n={iteration}: factoring degree {poly.degree()} over ZZ", flush=True)
    content, factors = sp.factor_list(poly)
    assert content == 1
    reconstructed = sp.Poly(content, Z, domain=sp.ZZ)
    factor_records = []
    positive_count = 0
    cyclotomic_degree = 0
    positive_degree = 0
    for index, (factor, multiplicity) in enumerate(factors, start=1):
        assert factor.LC() == 1 and abs(factor.TC()) == 1
        reconstructed *= factor**multiplicity
        cyclotomic = bool(factor.is_cyclotomic)
        if cyclotomic:
            cyclotomic_degree += multiplicity * factor.degree()
        else:
            positive_count += multiplicity
            positive_degree += multiplicity * factor.degree()
        print(f"n={iteration}: factor {index}/{len(factors)}, degree {factor.degree()}, multiplicity {multiplicity}, cyclotomic={cyclotomic}; computing all roots", flush=True)
        factor_records.append({
            "degree": factor.degree(),
            "multiplicity": int(multiplicity),
            "coefficients_descending": coefficient_list(factor),
            "cyclotomic": cyclotomic,
            "positive_measure_by_kronecker": not cyclotomic,
            "numerics": full_root_diagnostics(factor, digits),
        })
    assert reconstructed == poly
    assert cyclotomic_degree + positive_degree == poly.degree()

    totals = {}
    for method in ("numpy_float64", "sympy_nroots"):
        with mp.workdps(digits):
            if all(factor["numerics"][method]["status"] == "completed" for factor in factor_records):
                raw = mp.fsum(factor["multiplicity"] * mp.mpf(factor["numerics"][method]["log_measure"]) for factor in factor_records)
                positive_values = [mp.mpf(factor["numerics"][method]["log_measure"]) for factor in factor_records if not factor["cyclotomic"]]
                total = mp.fsum(factor["multiplicity"] * mp.mpf(factor["numerics"][method]["log_measure"]) for factor in factor_records if not factor["cyclotomic"])
                totals[method] = {
                    "status": "completed",
                    "raw_all_factor_root_sum": mp.nstr(raw, digits),
                    "total_with_exact_zero_cyclotomic_cost": mp.nstr(total, digits),
                    "minimum_positive_factor_measure": mp.nstr(min(positive_values), digits) if positive_values else None,
                }
            else:
                totals[method] = {"status": "incomplete", "reason": "At least one factor root calculation failed"}

    record = {
        "iteration": iteration,
        "degree": poly.degree(),
        "coefficients_descending": coefficients,
        "coefficient_max_absolute_value": max(abs(c) for c in coefficients),
        "content": int(content),
        "exact_checks": {
            "monic": True,
            "constant_one": True,
            "reciprocal": True,
            "value_at_one": -1,
            "value_at_minus_one": 1,
            "complete_factor_product_reconstructs_input": True,
            "factor_degree_sum_equals_actual_degree": True,
        },
        "positive_factor_count_with_multiplicity": positive_count,
        "cyclotomic_degree_with_multiplicity": cyclotomic_degree,
        "positive_degree_with_multiplicity": positive_degree,
        "factors": factor_records,
        "uncertified_numerical_totals": totals,
    }
    print(f"n={iteration}: exact positive count={positive_count}; numerical totals={json.dumps(totals)}", flush=True)
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, choices=(1, 2), help="Analyze only this assigned iteration; construct all required predecessors exactly")
    parser.add_argument("--digits", type=int, default=50, help="Uncertified SymPy nroots decimal working precision")
    args = parser.parse_args()
    if args.digits < 20:
        parser.error("--digits must be at least 20")
    requested = [args.n] if args.n is not None else [1, 2]
    assert sp.gcd(G, G_STAR).degree() == 0
    assert coefficient_list(G_STAR) == coefficient_list(G)[::-1]
    assert sp.Poly(G.as_expr() - G_STAR.as_expr(), Z, modulus=2).as_expr() != 0
    assert G.eval(1) == -1 and G.eval(-1) == -1
    assert G_STAR.eval(1) == -1 and G_STAR.eval(-1) == 1
    metadata = {
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "numpy": np.__version__,
        "mpmath": mp.__version__,
        "assigned_iterations": [1, 2],
        "requested_iterations": requested,
        "nroots_digits": args.digits,
        "nroots_maxsteps": 200,
        "seed_coefficients_descending": coefficient_list(SEED),
        "g_coefficients_descending": coefficient_list(G),
        "g_star_coefficients_descending": coefficient_list(G_STAR),
        "g_and_g_star_coprime": True,
        "g_and_g_star_congruent_modulo_two": False,
        "numeric_measure_certified": False,
    }
    polynomial = SEED
    records = []
    for iteration in range(1, max(requested) + 1):
        polynomial = pullback(polynomial)
        if iteration in requested:
            record = analyze(polynomial, iteration, args.digits)
            records.append(record)
            atomic_json(OUTPUT / f"n{iteration}_results.json", {"metadata": metadata, "result": record})
    if requested == [1, 2]:
        atomic_json(OUTPUT / "results.json", {"metadata": metadata, "results": records})
    print(f"Completed assigned iterations {requested}; output directory {OUTPUT}", flush=True)


if __name__ == "__main__":
    main()
