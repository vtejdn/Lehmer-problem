"""Finite central-minus-one probe, with exhaustive exact cyclotomic removal.

Only n = 35, 105, 1155 are tested.  For a monic integer polynomial of degree D,
every cyclotomic divisor Phi_k has phi(k) <= D.  Multiplicativity gives
phi(k)^2/k = product_{p^a || k} p^(a-2)*(p-1)^2.  Every odd-prime factor is
at least one; for p = 2 only a = 1 gives 1/2, and a >= 2 gives at least one.
The empty product for k = 1 is one.  Hence k <= 2*D^2 exhausts the possibilities.

The modulo-two test rejects only impossible divisors: integer divisibility
would survive reduction, and a monic cyclotomic polynomial keeps its degree
and remains nonzero modulo two.  Passing this filter is never accepted as
integer divisibility; repeated exact division supplies the actual factors.
Floating-point quadrature and root counts have no certified error intervals.
"""

import json
import math
from pathlib import Path
import platform

import numpy as np
import sympy as sp


def possible_orders(degree):
    bound = 2 * degree * degree
    totients = list(range(bound + 1))
    for prime in range(2, bound + 1):
        if totients[prime] == prime:
            for multiple in range(prime, bound + 1, prime):
                totients[multiple] -= totients[multiple] // prime
    return bound, [k for k in range(1, bound + 1) if totients[k] <= degree]


def bits_mod_two(polynomial):
    return sum((int(polynomial.nth(k)) & 1) << k
               for k in range(polynomial.degree() + 1))


def remainder_mod_two(dividend, divisor):
    divisor_length = divisor.bit_length()
    assert divisor_length
    while dividend and dividend.bit_length() >= divisor_length:
        dividend ^= divisor << (dividend.bit_length() - divisor_length)
    return dividend


def coefficients_ascending(polynomial):
    return [int(polynomial.nth(k)) for k in range(polynomial.degree() + 1)]


def remove_all_cyclotomic(polynomial):
    z = polynomial.gens[0]
    bound, orders = possible_orders(polynomial.degree())
    original_bits = bits_mod_two(polynomial)
    residual = polynomial
    cyclotomic_product = sp.Poly(1, z, domain=sp.ZZ)
    factors = []
    modular_passes = []
    for order in orders:
        factor = sp.Poly(sp.cyclotomic_poly(order, z), z, domain=sp.ZZ)
        if remainder_mod_two(original_bits, bits_mod_two(factor)):
            continue
        modular_passes.append(order)
        multiplicity = 0
        while residual.degree() >= factor.degree():
            quotient, remainder = residual.div(factor, auto=False)
            if not remainder.is_zero:
                break
            residual = quotient
            multiplicity += 1
        if multiplicity:
            factors.append({
                "order": order,
                "multiplicity": multiplicity,
                "degree": factor.degree(),
            })
            cyclotomic_product *= factor ** multiplicity
    assert cyclotomic_product * residual == polynomial
    assert residual.LC() == 1 and abs(int(residual.TC())) == 1
    return residual, {
        "necessary_order_upper_bound": bound,
        "necessary_order_count": len(orders),
        "maximum_necessary_order": max(orders),
        "orders_passing_mod_two_filter": modular_passes,
        "exact_cyclotomic_factors": factors,
        "exact_cyclotomic_degree": cyclotomic_product.degree(),
        "residual_has_no_cyclotomic_factor": True,
    }


def quadrature(polynomial):
    coefficients = np.array(coefficients_ascending(polynomial), dtype=np.float64)
    results = []
    for exponent in (17, 19, 21):
        size = 2 ** exponent
        padded = np.zeros(size, dtype=complex)
        padded[:len(coefficients)] = coefficients * np.exp(
            1j * np.pi * np.arange(len(coefficients)) / size
        )
        magnitudes = np.abs(np.fft.ifft(padded) * size)
        results.append({
            "midpoint_count": size,
            "approximate_total_log_measure": float(np.mean(np.log(magnitudes))),
            "minimum_sampled_absolute_value": float(np.min(magnitudes)),
        })
    return results


def probe(n):
    z = sp.symbols("z")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(n, z), z, domain=sp.ZZ)
    degree = cyclotomic.degree()
    polynomial = cyclotomic - sp.Poly(z ** (degree // 2), z, domain=sp.ZZ)
    residual, extraction = remove_all_cyclotomic(polynomial)
    result = {
        "n": n,
        "degree": degree,
        "coefficients_ascending": coefficients_ascending(polynomial),
        **extraction,
        "residual_degree": residual.degree(),
        "residual_coefficients_ascending": coefficients_ascending(residual),
        "residual_support_count": sum(c != 0 for c in residual.all_coeffs()),
        "residual_coefficient_height": max(abs(int(c)) for c in residual.all_coeffs()),
        "positive_irreducible_factor_count_with_multiplicity": None,
        "positive_irreducible_factor_count_lower_bound": 1,
        "residual_quadrature": quadrature(residual),
    }
    assert residual.degree() > 0
    if residual.degree() <= 48:
        content, factors = sp.factor_list(residual)
        assert content == 1
        reconstructed = sp.Poly(1, z, domain=sp.ZZ)
        exact_factors = []
        for factor, multiplicity in factors:
            reconstructed *= factor ** multiplicity
            assert not factor.is_cyclotomic
            exact_factors.append({
                "coefficients_ascending": coefficients_ascending(factor),
                "degree": factor.degree(),
                "multiplicity": multiplicity,
                "is_cyclotomic": False,
            })
        assert reconstructed == residual
        result["exact_residual_irreducible_factors"] = exact_factors
        result["positive_irreducible_factor_count_with_multiplicity"] = sum(
            multiplicity for _, multiplicity in factors
        )
        roots = np.roots([float(c) for c in residual.all_coeffs()])
        outside = [root for root in roots if abs(root) > 1 + 1e-7]
        result["numerical_residual_roots"] = {
            "exterior_modulus_threshold": 1 + 1e-7,
            "exterior_count": len(outside),
            "approximate_total_log_measure": sum(math.log(abs(root)) for root in outside),
        }
    return result


def main():
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name / "center_one_results.json"
    payload = {
        "arithmetic_limits": (
            "Cyclotomic generation, exhaustive necessary orders, modulo-two "
            "rejection and integer division are exact. Residual factorization "
            "is completed only for n=35,105. FFT integrals and numerical roots "
            "use double precision without certified intervals or root counts."
        ),
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "sympy": sp.__version__,
        },
        "inputs": [probe(n) for n in (35, 105, 1155)],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(output.relative_to(group.parents[3]))
    for result in payload["inputs"]:
        print(result["n"], result["exact_cyclotomic_degree"],
              result["residual_degree"],
              result["residual_quadrature"][-1]["approximate_total_log_measure"])


if __name__ == "__main__":
    main()
