"""Distinct full-Z verification of only the paired degree72 restriction.

Reconstructs Pi11/Pi59 via actual cyclotomic factor products, not producer division.
No full degree357 T is expanded; imports no producer arithmetic.
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
    saved = json.loads((output/'paired_move72_result.json').read_text(encoding='utf-8'))
    assert saved['selected_moves'] == [11, 59]
    f = {n: trace_factor(n) for n in (3, 5, 9, 11, 15, 17, 33, 59, 177, 187, 480)}
    divisor = f[15]**2*f[480]
    assert divisor.degree() == saved['quotient_degree'] == 72
    assert saved['J_coefficients'] == coefficients(divisor)
    kernel187 = f[11]*f[17]*f[187]
    pi11, pi59 = f[11]*f[33]**2, f[59]*f[177]**2
    for n in (11, 59):
        bn, dn = f[n], f[3*n]
        assert bn.compose(C[3]) == bn*dn
        row = saved['moves'][str(n)]
        assert row['B_coefficients'] == coefficients(bn)
        assert row['D_coefficients'] == coefficients(dn)
        assert row['Pi_coefficients'] == coefficients(bn*dn**2)
    factors = [('endpoint', sp.Poly(x-2, x), 2), ('F3', f[3], 2), ('F5', f[5], 3),
               ('F9', f[9], 4), ('B187', kernel187, 1), ('Pi11', pi11, 1), ('Pi59', pi59, 1)]
    assert len(saved['cofactor_factor_list']) == len(factors)
    for (name, factor, exponent), row in zip(factors, saved['cofactor_factor_list']):
        assert row == dict(name=name, coefficients=coefficients(factor), exponent=exponent)
    full_degree = divisor.degree()+sum(poly.degree()*e for _, poly, e in factors)
    assert full_degree == saved['full_trace_degree'] == 357
    assert 2*full_degree == saved['full_reciprocal_degree'] == 714
    radical_factors = [sp.Poly(x, x, modulus=2)]+[sp.Poly(f[n], x, modulus=2)
                       for n in (3, 5, 9, 15, 11, 17, 187, 33, 59, 177)]
    for i, poly in enumerate(radical_factors):
        assert poly.gcd(poly.diff()).degree() == 0
        for previous in radical_factors[:i]:
            assert poly.gcd(previous).degree() == 0
    assert sum(poly.degree() for poly in radical_factors) == saved['full_radical_degree'] == 201
    canonical = []
    for p in (2, 3, 5):
        numerator = divisor.compose(C[p]).rem(divisor)
        assert all(int(v) % p == 0 for v in numerator.all_coeffs())
        theta = sp.Poly.from_list([int(v)//p for v in numerator.all_coeffs()], x)
        assert saved['canonical_J_mod4'][str(p)] == coefficients(theta, 4)
        weight = sp.Poly(1, x)
        for _, factor, exponent in factors:
            weight = (weight*factor.compose(C[p]).rem(divisor)**exponent).rem(divisor)
        assert saved['cofactor_weights_mod4'][str(p)] == coefficients(weight, 4)
        canonical.append((weight*theta).rem(divisor))
    a, b, c = canonical
    ff = (2*c**2-3*a**5).rem(divisor)
    gg = (c**3-2*b**5).rem(divisor)
    actual = dict(a=a, b=b, c=c, F=ff, G=gg,
                  X_plus=(b**2-a**3+gg).rem(divisor), X_minus=(b**2-a**3-gg).rem(divisor))
    exact = {}
    for name, poly in actual.items():
        assert saved['original_restrictions_mod4'][name] == coefficients(poly, 4), name
        value = valuation(poly)
        exact[name] = value
        truncated = value if isinstance(value, int) and value < 2 else 'at_least_2'
        assert saved['restriction_valuations_through_mod4'][name] == truncated
        assert saved['binary_f15_orders'][name] == order(poly, f[15])
        if all(int(v) % 2 == 0 for v in poly.all_coeffs()):
            half = sp.Poly.from_list([int(v)//2 for v in poly.all_coeffs()], x)
            assert saved['half_f15_orders'][name] == order(half, f[15])
            assert saved['half_f15_initial_units'][name] == initial_unit(half, f[15])
    gates = dict(F_mod4=all(int(v) % 4 == 0 for v in actual['F'].all_coeffs()),
                 X_plus_mod2=all(int(v) % 2 == 0 for v in actual['X_plus'].all_coeffs()),
                 X_minus_mod2=all(int(v) % 2 == 0 for v in actual['X_minus'].all_coeffs()),
                 G_nonzero_mod2=any(int(v) % 2 for v in actual['G'].all_coeffs()))
    assert gates == saved['global_gates_via_GR6']
    result = dict(selected_moves=[11, 59], quotient_degree=72, full_trace_degree=357,
                  full_reciprocal_degree=714, full_radical_degree=201,
                  all_factor_canonical_weight_and_seven_restriction_arrays_match=True,
                  global_gates_via_GR6=gates, exact_local_integer_valuations=exact,
                  actual_integer_restrictions={name: coefficients(poly) for name, poly in actual.items()},
                  implementation='separate full-Z SymPy primitive-trace products and weighted monic remainders',
                  sympy_version=sp.__version__)
    tmp = output/'paired_move72_verification.json.partial'
    tmp.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'paired_move72_verification.json')
    print(json.dumps({key: value for key, value in result.items() if key != 'actual_integer_restrictions'}))


if __name__ == '__main__':
    main()
