"""Exact construction and full factorization of the single dyadic defect k=3."""

import json
from pathlib import Path
import platform

import sympy as sp


K_INPUT = 3


def polynomial_data(poly):
    return {
        "degree": int(poly.degree()),
        "coefficients_descending": [int(value) for value in poly.all_coeffs()],
        "expression": str(poly.as_expr()),
    }


def main():
    z, w = sp.symbols("z w")
    k = K_INPUT
    assert k == 3, "This retained finite computation has only the input k=3."
    n = 2 ** (k + 1)
    shift = 2 ** (k - 1) + 1
    quotient, remainder = sp.div(z ** (2**k) - 1, z**2 + 1, z)
    assert remainder == 0
    c = sp.Poly(quotient, z, domain=sp.ZZ)
    d = sp.Poly(z**n + 1, z, domain=sp.ZZ)
    a = sp.Poly(z**shift * c.as_expr(), z, domain=sp.ZZ)
    f = a * a + d * d

    checks = {
        "exact_c_quotient": remainder == 0,
        "input_coprime": sp.gcd(a, d).degree() == 0,
        "balanced_degrees": d.degree() == c.degree() + 2 * shift,
        "opposite_constant_signs": c.TC() == -1 and d.TC() == 1,
        "monic_output": f.LC() == 1,
        "unit_output": f.TC() == 1,
        "output_degree": f.degree() == 2 * n,
        "reciprocal_output": f.all_coeffs() == list(reversed(f.all_coeffs())),
    }

    input_factors = {}
    for name, poly in (("C", c), ("D", d)):
        content, factorization = sp.factor_list(poly)
        assert content == 1
        parts = []
        for factor, multiplicity in factorization:
            cyclotomic = bool(factor.is_cyclotomic)
            assert cyclotomic
            parts.append(
                dict(polynomial_data(factor), multiplicity=int(multiplicity),
                     is_cyclotomic=cyclotomic)
            )
        input_factors[name] = parts
    checks["cyclotomic_inputs"] = True
    checks["displayed_pure_dyadic_inputs"] = (
        c.as_expr() == sp.expand((z - 1) * (z + 1) * (z**4 + 1))
        and d.as_expr() == z**16 + 1
    )

    content, factorization = sp.factor_list(f)
    reconstructed = sp.Poly(content, z, domain=sp.ZZ)
    factor_records = []
    positive_count = 0
    cyclotomic_degree = 0
    for factor, multiplicity in factorization:
        assert factor.LC() == 1 and abs(factor.TC()) == 1
        cyclotomic = bool(factor.is_cyclotomic)
        reconstructed *= factor**multiplicity
        if cyclotomic:
            cyclotomic_degree += factor.degree() * multiplicity
        else:
            positive_count += multiplicity
        factor_records.append(
            dict(polynomial_data(factor), multiplicity=int(multiplicity),
                 is_cyclotomic=cyclotomic,
                 classification=("cyclotomic" if cyclotomic else
                                 "positive irreducible monic unit factor"))
        )
    checks["content_one"] = content == 1
    checks["complete_factor_product"] = reconstructed == f
    checks["complete_factor_degree"] = sum(
        factor.degree() * multiplicity for factor, multiplicity in factorization
    ) == f.degree()

    h = sp.Poly(
        z**28 + z**26 - z**22 - z**20 + z**18 + 2*z**14
        + z**10 - z**8 - z**6 + z**2 + 1,
        z, domain=sp.ZZ,
    )
    phi12 = sp.Poly(sp.cyclotomic_poly(12, z), z, domain=sp.ZZ)
    checks["explicit_phi12_h_product"] = phi12 * h == f
    checks["returned_exact_two_factors"] = {
        (tuple(factor.all_coeffs()), multiplicity)
        for factor, multiplicity in factorization
    } == {(tuple(phi12.all_coeffs()), 1), (tuple(h.all_coeffs()), 1)}

    g_expression = sp.expand(
        z**2 * w * (w - 1)**2 + (z**2 + 1)**2 * (w**2 + 1)**2
    )
    g = sp.Poly(g_expression, z, w, domain=sp.ZZ)
    specialization = sp.Poly(g_expression.subs(w, z ** (2**k)), z, domain=sp.ZZ)
    checks["complete_cost_identity"] = (
        sp.Poly((z**2 + 1)**2, z, domain=sp.ZZ) * f == specialization
    )
    g_length = sum(abs(int(value)) for value in g.coeffs())
    checks["g_support_and_length"] = len(g.terms()) == 11 and g_length == 16
    assert all(checks.values()), checks

    result = {
        "scope": "Single exact input k=3; no numerical roots or additional k.",
        "environment": {"python": platform.python_version(), "sympy": sp.__version__},
        "parameters": {"k": k, "N": n, "r": shift},
        "inputs": {"C": polynomial_data(c), "D": polynomial_data(d),
                   "A": polynomial_data(a)},
        "input_factors": input_factors,
        "output": polynomial_data(f),
        "content": int(content),
        "factors": factor_records,
        "positive_irreducible_factor_count_with_multiplicity": int(positive_count),
        "cyclotomic_degree_with_multiplicity": int(cyclotomic_degree),
        "exact_values": {"F(1)": str(f.eval(1)), "F(-1)": str(f.eval(-1)),
                         "F(i)": str(sp.expand(f.as_expr().subs(z, sp.I)))},
        "bivariate_cost_polynomial": {
            "expression": str(g_expression),
            "terms": [{"exponents_z_w": list(powers), "coefficient": int(value)}
                      for powers, value in g.terms()],
            "coefficient_absolute_sum": g_length,
        },
        "checks": {name: bool(value) for name, value in checks.items()},
        "limits": [
            "Irreducibility and cyclotomic classification use exact SymPy algorithms.",
            "Product reconstruction independently checks the full coefficient identity.",
            "No hand irreducibility certificate, all-k conclusion, Mahler approximation, "
            "or formal independent review is supplied.",
        ],
    }
    group = Path(__file__).resolve().parent
    output_dir = group.parent.parent / "outputs" / group.name
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "results.json"
    temporary = output_dir / "results.pending.json"
    temporary.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    temporary.replace(destination)
    print(json.dumps({
        "scope": {"k": k, "degree": int(f.degree())},
        "factor_degrees_and_multiplicities": [
            [int(factor.degree()), int(multiplicity)]
            for factor, multiplicity in factorization
        ],
        "positive_factor_count": int(positive_count),
        "cyclotomic_degree": int(cyclotomic_degree),
        "all_exact_checks": True,
        "output": str(destination),
    }, indent=2))


if __name__ == "__main__":
    main()
