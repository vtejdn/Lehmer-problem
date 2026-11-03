"""Distinct full-Z verification of the one unit-adjusted degree187 input.

Reuses only the prior independent SymPy-side helpers, never producer code.
"""
from pathlib import Path
import json
import sympy as sp
from verify_odd_support import C, x, trace_factor, coefficients, valuation, order, initial_unit


def main():
    while len(C) <= 93:
        C.append(sp.Poly(x, x, domain=sp.ZZ)*C[-1]-C[-2])
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    saved = json.loads((output/'unit_adjusted_result.json').read_text(encoding='utf-8'))
    assert saved['candidate'] == '(X-2)^2 F480 F15^2 F3^2 F5^3 F9^4 B187'
    factors = {n: trace_factor(n) for n in (3, 5, 9, 11, 15, 17, 30, 187, 480)}
    kernel = factors[11]*factors[17]*factors[187]
    assert kernel == sum(C[1:94], sp.Poly(1, x))
    assert factors[480] == factors[30].compose(C[16])
    r = (sp.Poly((x-2)**2, x)*factors[15]**2*factors[3]**2
         *factors[5]**3*factors[9]**4*kernel)
    t = r*factors[480]
    assert t.degree() == saved['degree'] == 187
    assert saved['reciprocal_degree'] == 374
    for key, poly in [('T_coefficients', t), ('R_coefficients', r), ('B187_coefficients', kernel)]:
        assert saved[key] == coefficients(poly), key
    canonical = []
    for p in (2, 3, 5):
        remainder = t.compose(C[p]).rem(t)
        assert all(int(v) % p == 0 for v in remainder.all_coeffs())
        canonical.append(sp.Poly.from_list([int(v)//p for v in remainder.all_coeffs()], x))
    a, b, c = canonical
    f = (2*c**2-3*a**5).rem(t)
    g = (c**3-2*b**5).rem(t)
    actual = dict(a=a, b=b, c=c, F=f, G=g,
                  X_plus=(b**2-a**3+g).rem(t), X_minus=(b**2-a**3-g).rem(t))
    exact = {}
    for name, poly in actual.items():
        assert saved['residues_mod4'][name] == coefficients(poly, 4), name
        value = valuation(poly)
        exact[name] = value
        truncated = value if isinstance(value, int) and value < 2 else 'at_least_2'
        assert saved['coefficient_valuations_through_mod4'][name] == truncated
        for label, factor in [('f15', factors[15]), ('f9', factors[9])]:
            assert saved['diagnostics']['full_binary_orders'][label][name] == order(poly, factor)
        if all(int(v) % 2 == 0 for v in poly.all_coeffs()):
            half = sp.Poly.from_list([int(v)//2 for v in poly.all_coeffs()], x)
            assert saved['diagnostics']['half_f15_orders'][name] == order(half, factors[15])
            assert saved['diagnostics']['half_f15_initial_units'][name] == initial_unit(half, factors[15])
    primary = [('X2', sp.Poly(x**2, x)), ('f3_squared', factors[3]**2),
               ('f5_cubed', factors[5]**3), ('f9_fourth', factors[9]**4),
               ('f15_power18', factors[15]**18), ('B187', kernel)]
    for label, modulus in primary:
        binary_modulus = sp.Poly(modulus, x, modulus=2)
        for name, poly in actual.items():
            assert saved['diagnostics']['full_primary_binary_remainders'][label][name] == coefficients(sp.Poly(poly, x, modulus=2).rem(binary_modulus), 2)
    radical = sp.Poly(x*factors[3]*factors[5]*factors[9]*factors[15]*kernel, x, modulus=2)
    assert radical.gcd(radical.diff()).degree() == 0
    assert radical.degree() == saved['diagnostics']['full_radical_degree'] == 104
    jodd = sp.Poly(factors[5]*kernel, x, modulus=2)
    assert saved['diagnostics']['J_derivative_order_at_f3'] == order(jodd.diff(), factors[3])
    result = dict(candidate=saved['candidate'], degree=187, reciprocal_degree=374,
                  all_full_T_R_kernel_and_seven_residue_arrays_match=True,
                  all_complete_binary_primary_arrays_match=True,
                  exact_coefficient_valuations=exact,
                  actual_integer_polynomials={name: coefficients(poly) for name, poly in actual.items()},
                  full_radical_degree=104, J_derivative_order_at_f3=order(jodd.diff(), factors[3]),
                  implementation='separate full-Z SymPy cyclotomic reconstruction', sympy_version=sp.__version__)
    tmp = output/'unit_adjusted_verification.json.partial'
    tmp.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'unit_adjusted_verification.json')
    print(json.dumps({key: value for key, value in result.items() if key != 'actual_integer_polynomials'}))


if __name__ == '__main__':
    main()
