"""Exact rational rotation and trace-root control for the same k=3 input."""

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
    z, x = sp.symbols("z x")
    k = K_INPUT
    assert k == 3, "Only the previously fixed k=3 input is selected."
    n = 2**k
    r = n // 2 + 1
    b_expr, b_rem = sp.div(z**n - 1, z**2 - 1, z)
    c_expr, c_rem = sp.div(z**n - 1, z**2 + 1, z)
    assert b_rem == c_rem == 0
    q = sp.Poly(z**(2*n) + 1 - z**r*b_expr, z, domain=sp.ZZ)
    f = sp.Poly(z**(2*r)*c_expr**2 + (z**(2*n)+1)**2,
                z, domain=sp.ZZ)
    q_negative = sp.Poly(q.as_expr().subs(z, -z), z, domain=sp.ZZ)
    f_rotated = sp.Poly(sp.expand(f.as_expr().subs(z, sp.I*z)),
                        z, domain=sp.ZZ)
    sparse = sp.Poly(z**(2*n+2)-z**(2*n)-z**(3*n//2+1)
                     +z**(n//2+1)+z**2-1, z, domain=sp.ZZ)
    checks = {
        "rotation_product": f_rotated == q*q_negative,
        "six_term_completion": sp.Poly(z**2-1, z)*q == sparse,
        "six_terms": len(sparse.terms()) == 6,
        "monic_unit_reciprocal": q.LC() == q.TC() == 1
            and q.all_coeffs() == list(reversed(q.all_coeffs())),
        "degree_halved": 2*q.degree() == f.degree(),
    }

    content, factors = sp.factor_list(q)
    reconstructed = sp.Poly(content, z, domain=sp.ZZ)
    factor_records = []
    positive = []
    for factor, multiplicity in factors:
        reconstructed *= factor**multiplicity
        cyclotomic = bool(factor.is_cyclotomic)
        factor_records.append(dict(polynomial_data(factor),
                                   multiplicity=int(multiplicity),
                                   is_cyclotomic=cyclotomic))
        if not cyclotomic:
            positive.append((factor, multiplicity))
    checks["complete_factor_product"] = reconstructed == q
    checks["one_degree14_positive_factor"] = (
        len(positive) == 1 and positive[0][0].degree() == 14
        and positive[0][1] == 1
    )
    assert checks["one_degree14_positive_factor"]
    core = positive[0][0]
    phi6 = sp.Poly(z**2-z+1, z, domain=sp.ZZ)
    checks["phi6_core_product"] = phi6*core == q

    half_degree = core.degree() // 2
    s_previous, s_current = sp.Integer(2), x
    trace = core.nth(half_degree)
    for j in range(1, half_degree+1):
        if j > 1:
            s_previous, s_current = s_current, sp.expand(x*s_current-s_previous)
        trace += core.nth(half_degree+j)*s_current
    trace = sp.Poly(trace, x, domain=sp.ZZ)
    trace_return = sp.Poly(sp.expand(z**half_degree
        *trace.as_expr().subs(x, z+1/z)), z, domain=sp.ZZ)
    checks["exact_trace_return"] = trace_return == core
    checks["trace_endpoints_nonzero"] = trace.eval(-2) != 0 and trace.eval(2) != 0
    checks["trace_squarefree"] = sp.gcd(trace, trace.diff()).degree() == 0
    assert checks["trace_endpoints_nonzero"]
    counts = {
        "real_below_minus2": int(trace.count_roots(-sp.oo, -2)),
        "real_between_minus2_and2": int(trace.count_roots(-2, 2)),
        "real_above2": int(trace.count_roots(2, sp.oo)),
        "real_total": int(trace.count_roots(-sp.oo, sp.oo)),
    }
    counts["nonreal"] = int(trace.degree())-counts["real_total"]
    checks["trace_counts_partition"] = sum(counts[key] for key in (
        "real_below_minus2", "real_between_minus2_and2", "real_above2"
    )) == counts["real_total"]
    h = sp.Poly(z**28+z**26-z**22-z**20+z**18+2*z**14
                +z**10-z**8-z**6+z**2+1, z, domain=sp.ZZ)
    core_negative = sp.Poly(core.as_expr().subs(z, -z), z, domain=sp.ZZ)
    h_rotated = sp.Poly(sp.expand(h.as_expr().subs(z, sp.I*z)),
                        z, domain=sp.ZZ)
    checks["previous_positive_core_rotation"] = h_rotated == core*core_negative
    assert all(checks.values()), checks

    result = {
        "scope": "k=3 only; exact rational rotation and real trace-root counts",
        "parameters": {"k": k, "n": n, "r": r},
        "software": {"python": platform.python_version(), "sympy": sp.__version__},
        "Q": polynomial_data(q),
        "sparse_completion": polynomial_data(sparse),
        "factorization": factor_records,
        "positive_core": polynomial_data(core),
        "trace_polynomial": polynomial_data(trace),
        "trace_root_counts": counts,
        "checks": checks,
        "limits": "Symbolic-library factorization and exact real-root counts; no numerical Mahler value and no larger k."
    }
    group = Path(__file__).resolve().parent
    destination = group.parent.parent / "outputs" / group.name / "rotation.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), "checks": checks,
                      "positive_core": str(core.as_expr()),
                      "trace": str(trace.as_expr()), "trace_counts": counts}, indent=2))


if __name__ == "__main__":
    main()
