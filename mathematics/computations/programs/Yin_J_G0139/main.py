"""Bounded author diagnostics; floating measures are not certified bounds."""

from pathlib import Path
import json
import os

import numpy as np
import sympy as sp


def construct(r):
    assert 2 <= r <= 7
    k = 1 << r
    eps = [(-1) ** j.bit_count() for j in range(k)]
    eps[k // 2] += 2
    eps[k // 2 + 1] -= 2
    assert all(e in (-1, 1) for e in eps)
    p = [0] * (4 * k + 1)
    p[0] = p[-1] = 1
    for j, e in enumerate(eps):
        for exponent in range(1 + 2 * j, 4 * k - 2 * j, 2):
            p[exponent] -= e

    b = [1]
    for i in range(1, r):
        shift = 1 << (i + 1)
        product = b + [0] * shift
        for j, coefficient in enumerate(b):
            product[j + shift] -= coefficient
        b = product
    closed = [0] * len(p)
    closed[0] = closed[-1] = 1
    for j, coefficient in enumerate(b):
        closed[j + 1] -= coefficient
        closed[j + 2 * k + 3] += (-1) ** r * coefficient
    closed[3 * k - 1] -= 2
    closed[k + 1] -= 2
    assert p == closed
    assert p == p[::-1] and sum(p) == -2
    return k, p


def order_at_one_mod_two(coefficients):
    polynomial = sum((coefficient & 1) << j
                     for j, coefficient in enumerate(coefficients))
    order = 0
    while polynomial.bit_count() % 2 == 0:
        remainder = polynomial
        quotient = 0
        for j in range(polynomial.bit_length() - 2, -1, -1):
            if (remainder >> (j + 1)) & 1:
                quotient ^= 1 << j
                remainder ^= 3 << j
        assert remainder == 0 and quotient != 0
        polynomial = quotient
        order += 1
    return order, polynomial.bit_length() - 1


def direct_integrals(p):
    result = []
    for samples in (16384, 65536):
        points = np.exp(2j * np.pi * (np.arange(samples) + 0.371) / samples)
        values = np.polynomial.polynomial.polyval(points, np.asarray(p, dtype=float))
        result.append({
            "samples": samples,
            "log_integral_approx": float(np.log(np.abs(values)).mean()),
            "min_abs": float(np.abs(values).min()),
        })
    return result


def fft_integrals(p):
    result = []
    for samples in (262144, 1048576):
        values = np.zeros(samples, dtype=complex)
        indices = np.arange(len(p))
        values[:len(p)] = np.asarray(p) * np.exp(2j * np.pi * 0.371 * indices / samples)
        values = np.fft.ifft(values) * samples
        result.append({
            "samples": samples,
            "log_integral_approx": float(np.log(np.abs(values)).mean()),
            "min_abs": float(np.abs(values).min()),
        })
    return result


def run():
    z = sp.symbols("z")
    rows = []
    for r in range(2, 8):
        k, p = construct(r)
        degree = len(p) - 1
        auxiliary = [0] * (degree + 5)
        for j, coefficient in enumerate(p):
            auxiliary[j] ^= coefficient & 1
            auxiliary[j + 4] ^= coefficient & 1
        support = [j for j, coefficient in enumerate(auxiliary) if coefficient]
        expected = [0, 1, 4, 2 * k + 1, 2 * k + 3, 4 * k, 4 * k + 3, 4 * k + 4]
        assert support == expected
        order, residual_degree = order_at_one_mod_two(p)
        assert order == 2 * k - 2 and residual_degree == 2 * k + 2
        row = {
            "r": r, "k": k, "degree": degree,
            "coefficients_ascending": p,
            "support": sum(c != 0 for c in p),
            "coefficient_l1": sum(abs(c) for c in p),
            "value_at_one": sum(p),
            "mod2_aux_support": support,
            "mod2_order_at_one": order,
            "mod2_residual_degree": residual_degree,
        }
        if r <= 6:
            polynomial = sp.Poly.from_list(p[::-1], z, domain=sp.ZZ)
            content, factors = sp.factor_list(polynomial)
            reconstructed = sp.Poly(content, z, domain=sp.ZZ)
            factor_rows = []
            total = 0.0
            for factor, multiplicity in factors:
                reconstructed *= factor ** multiplicity
                cyclotomic = bool(factor.is_cyclotomic)
                if cyclotomic:
                    measure = 0.0
                else:
                    roots = np.roots(np.asarray(factor.all_coeffs(), dtype=float))
                    measure = float(np.maximum(np.log(np.abs(roots)), 0.0).sum())
                total += int(multiplicity) * measure
                factor_rows.append({
                    "degree": factor.degree(),
                    "multiplicity": int(multiplicity),
                    "cyclotomic": cyclotomic,
                    "coefficients_descending": [int(c) for c in factor.all_coeffs()],
                    "measure_approx": measure,
                    "auxiliary_span_to_factor_degree": (degree + 4) / factor.degree(),
                })
            assert reconstructed == polynomial
            row.update({
                "factorization_status": "completed_exact_sympy_factor_list",
                "factors": factor_rows,
                "whole_measure_root_approx": total,
                "whole_measure_integral_diagnostics": direct_integrals(p),
            })
        else:
            row.update({
                "factorization_status": "not_run_by_this_program; earlier_attempt_interrupted_without_result",
                "whole_measure_integral_diagnostics": fft_integrals(p),
            })
        rows.append(row)
        print(json.dumps({
            "r": r, "degree": degree,
            "factorization_status": row["factorization_status"],
            "root_measure_approx": row.get("whole_measure_root_approx"),
            "integral_approximations": [v["log_integral_approx"] for v in row["whole_measure_integral_diagnostics"]],
        }), flush=True)
    group = Path(__file__).resolve().parent
    output_dir = group.parent.parent / "outputs" / group.name
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "results.json"
    temporary = output_dir / "results.json.tmp"
    payload = {
        "scope": "r=2..7; exact factors and floating roots only r<=6; r=7 FFT only",
        "precision_limit": "all floating measures are double-precision diagnostics without certified errors",
        "versions": {"sympy": sp.__version__, "numpy": np.__version__},
        "rows": rows,
    }
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, target)
    print(str(target), flush=True)


if __name__ == "__main__":
    run()
