"""Reproduce the completed finite cyclotomic central-minus-two probe.

Exact polynomial construction and small factorization are separated from
uncertified double-precision quadrature and numerical root screens.
"""

import json
import math
from pathlib import Path
import platform

import numpy as np
import sympy as sp


def probe(n):
    z = sp.symbols("z")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(n, z), z)
    degree = cyclotomic.degree()
    coefficients = [
        int(cyclotomic.nth(k)) - (2 if k == degree // 2 else 0)
        for k in range(degree + 1)
    ]
    polynomial = sp.Poly.from_list(coefficients[::-1], z)
    jordan_2 = int(n * n * sp.prod(
        1 - sp.Rational(1, p * p) for p in sp.factorint(n)
    ))
    result = {
        "n": n,
        "degree": degree,
        "coefficients_ascending": coefficients,
        "support_count": sum(c != 0 for c in coefficients),
        "J2": jordan_2,
        "positive_real_log_upper_formula": "sqrt(24/J2)",
        "positive_real_log_upper_numeric": math.sqrt(24 / jordan_2),
        "negative_real_log_upper_formula": "sqrt(8/J2)",
        "negative_real_log_upper_numeric": math.sqrt(8 / jordan_2),
        "dyadic_total_lower_formula": "degree*log(5)/(4*n)",
        "dyadic_total_lower_numeric": degree * math.log(5) / (4 * n),
        "quadrature": [],
    }
    numeric_coefficients = np.array(coefficients, dtype=np.float64)
    for exponent in (17, 19, 21):
        size = 2 ** exponent
        padded = np.zeros(size, dtype=complex)
        padded[:degree + 1] = numeric_coefficients * np.exp(
            1j * np.pi * np.arange(degree + 1) / size
        )
        values = np.fft.ifft(padded) * size
        magnitudes = np.abs(values)
        result["quadrature"].append({
            "midpoint_count": size,
            "approximate_total_log_measure": float(np.mean(np.log(magnitudes))),
            "minimum_sampled_absolute_value": float(np.min(magnitudes)),
        })
    if degree <= 48:
        roots = np.roots(numeric_coefficients[::-1])
        outside = [root for root in roots if abs(root) > 1 + 1e-7]
        positive_real = [
            float(root.real) for root in outside
            if abs(root.imag) < 1e-7 and root.real > 1
        ]
        total = sum(math.log(abs(root)) for root in outside)
        real_part = sum(math.log(root) for root in positive_real)
        result["numerical_roots"] = {
            "exterior_modulus_threshold": 1 + 1e-7,
            "real_imaginary_tolerance": 1e-7,
            "exterior_count": len(outside),
            "positive_real_exterior_roots": positive_real,
            "approximate_total_log_measure": total,
            "positive_real_log_contribution": real_part,
            "other_exterior_log_contribution": total - real_part,
        }
        factor_content, factors = sp.factor_list(polynomial)
        assert factor_content == 1
        reconstructed = sp.Poly(1, z)
        result["exact_factors"] = []
        for factor, multiplicity in factors:
            reconstructed *= factor ** multiplicity
            result["exact_factors"].append({
                "coefficients_ascending": [int(factor.nth(k))
                                           for k in range(factor.degree() + 1)],
                "degree": factor.degree(),
                "multiplicity": multiplicity,
                "is_cyclotomic": bool(factor.is_cyclotomic),
            })
        assert reconstructed == polynomial
    return result


def main():
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name / "results.json"
    payload = {
        "arithmetic_limits": (
            "Integer coefficient construction and small factorization are exact; "
            "FFT integrals, displayed real bounds and root screens use floating "
            "point and provide no certified numerical intervals."
        ),
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "sympy": sp.__version__,
        },
        "inputs": [probe(n) for n in (15, 105, 1155)],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(output.relative_to(group.parents[3]))
    for result in payload["inputs"]:
        print(result["n"], result["degree"],
              result["quadrature"][-1]["approximate_total_log_measure"])


if __name__ == "__main__":
    main()
