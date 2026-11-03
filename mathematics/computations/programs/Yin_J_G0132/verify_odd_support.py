"""Separate full-Z SymPy reconstruction of the one degree127 candidate.

Imports neither producer nor its arithmetic helper; requires saved producer data.
"""
from pathlib import Path
import json
import sympy as sp

x, z = sp.symbols('x z')
C = [sp.Poly(2, x, domain=sp.ZZ), sp.Poly(x, x, domain=sp.ZZ)]
for j in range(2, 65):
    C.append(sp.Poly(x, x, domain=sp.ZZ) * C[-1] - C[-2])


def trace_factor(n):
    phi = sp.Poly(sp.cyclotomic_poly(n, z), z, domain=sp.ZZ)
    d = phi.degree() // 2
    result = sp.Poly(phi.nth(d), x, domain=sp.ZZ)
    for j in range(1, d + 1):
        result += phi.nth(d + j) * C[j]
    return result


def coefficients(poly, modulus=None):
    values = [int(poly.nth(j)) for j in range(poly.degree() + 1)] if poly else [0]
    if modulus:
        values = [value % modulus for value in values]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def valuation(poly):
    values = [abs(int(v)) for v in poly.all_coeffs() if v]
    return min((v & -v).bit_length() - 1 for v in values) if values else 'infinity'


def order(poly, factor):
    p = sp.Poly(poly, x, modulus=2)
    f = sp.Poly(factor, x, modulus=2)
    if p.is_zero:
        return 'infinity'
    result = 0
    while p.rem(f).is_zero:
        p = p.exquo(f)
        result += 1
    return result


def initial_unit(poly, factor):
    binary = sp.Poly(poly, x, modulus=2)
    modulus = sp.Poly(factor, x, modulus=2)
    exponent = order(binary, modulus)
    if exponent == 'infinity':
        return [0]
    leading = binary.exquo(modulus**exponent).rem(modulus)
    assert leading.gcd(modulus).degree() == 0
    return coefficients(leading, 2)


def main():
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    saved = json.loads((output / 'odd_support_result.json').read_text(encoding='utf-8'))
    assert saved['candidate'] == '(X-2)^2 F480 F15^2 F3^2 F5^3 B91'
    assert saved['exact_single_case'] is True
    factors = {n: trace_factor(n) for n in (3, 5, 7, 13, 15, 30, 91, 480)}
    b91 = factors[7] * factors[13] * factors[91]
    assert b91 == sp.Poly(1, x) + sum(C[1:46], sp.Poly(0, x))
    assert factors[480] == factors[30].compose(C[16])
    cofactor = (sp.Poly((x-2)**2, x) * factors[15]**2 * factors[3]**2
                * factors[5]**3 * b91)
    t = cofactor * factors[480]
    assert saved['degree'] == t.degree() == 127
    assert saved['reciprocal_degree'] == 2*t.degree() == 254
    for key, poly in [('T_coefficients', t), ('R_coefficients', cofactor),
                      ('B91_coefficients', b91)]:
        assert saved[key] == coefficients(poly), key
    canonical = []
    for p in (2, 3, 5):
        remainder = t.compose(C[p]).rem(t)
        assert all(int(v) % p == 0 for v in remainder.all_coeffs())
        canonical.append(sp.Poly.from_list([int(v)//p for v in remainder.all_coeffs()], x))
    a, b, c = canonical
    f = (2*c**2 - 3*a**5).rem(t)
    g = (c**3 - 2*b**5).rem(t)
    xp = (b**2 - a**3 + g).rem(t)
    xm = (b**2 - a**3 - g).rem(t)
    actual = dict(a=a, b=b, c=c, F=f, G=g, X_plus=xp, X_minus=xm)
    exact = {}
    for name, poly in actual.items():
        assert saved['residues_mod4'][name] == coefficients(poly, 4), name
        value = valuation(poly)
        exact[name] = value
        truncated = value if isinstance(value, int) and value < 2 else 'at_least_2'
        assert saved['coefficient_valuations_through_mod4'][name] == truncated
        assert saved['diagnostics']['binary_f15_orders'][name] == order(poly, factors[15])
    jodd = sp.Poly(factors[5]*b91, x, modulus=2)
    assert saved['J_binary_coefficients'] == coefficients(jodd, 2)
    assert saved['J_derivative_binary_coefficients'] == coefficients(jodd.diff(), 2)
    derivative_order = order(jodd.diff(), factors[3])
    jet_order = order(b91+factors[5], factors[3])
    assert all(int(v) % 2 == 0 for v in f.all_coeffs())
    fhalf = sp.Poly.from_list([int(v)//2 for v in f.all_coeffs()], x)
    fhalf_order = order(fhalf, factors[15])
    units = {name: initial_unit(poly, factors[15])
             for name, poly in [('F_half', fhalf), ('X_plus', xp), ('X_minus', xm)]}
    assert saved['diagnostics']['F_half_binary_f15_order'] == fhalf_order
    assert saved['diagnostics']['f15_initial_units'] == units
    assert saved['diagnostics']['J_derivative_order_at_f3'] == derivative_order
    assert saved['diagnostics']['B91_plus_F5_order_at_f3'] == jet_order
    radical = sp.Poly(x*factors[3]*factors[5]*factors[15]*b91, x, modulus=2)
    assert radical.gcd(radical.diff()).degree() == 0
    assert radical.degree() == saved['diagnostics']['full_radical_degree'] == 53
    assert jodd.degree() == saved['diagnostics']['odd_multiplicity_factor_degree'] == 47
    primary = [('X2', sp.Poly(x**2, x)), ('f3_squared', factors[3]**2),
               ('f5_cubed', factors[5]**3), ('f15_power18', factors[15]**18), ('B91', b91)]
    for label, modulus in primary:
        binary_modulus = sp.Poly(modulus, x, modulus=2)
        for name, poly in actual.items():
            binary_remainder = sp.Poly(poly, x, modulus=2).rem(binary_modulus)
            assert saved['diagnostics']['full_primary_binary_remainders'][label][name] == coefficients(binary_remainder, 2)
    cofactor_divisibility = {name: poly.rem(cofactor).is_zero for name, poly in actual.items()}
    assert all(cofactor_divisibility.values())
    result = dict(
        candidate=saved['candidate'], degree=127, reciprocal_degree=254,
        exact_coefficient_valuations=exact,
        all_T_R_B91_coefficients_and_seven_residue_arrays_match=True,
        all_complete_binary_primary_remainders_match=True,
        J_derivative_order_at_f3=derivative_order, B91_plus_F5_order_at_f3=jet_order,
        F_half_binary_f15_order=fhalf_order, f15_initial_units=units,
        full_radical_degree=53, R_divides_actual_canonical_and_residuals=cofactor_divisibility,
        actual_integer_polynomials={name: coefficients(poly) for name, poly in actual.items()},
        implementation='separate SymPy full-Z cyclotomic reconstruction and exact monic remainders',
        sympy_version=sp.__version__)
    temporary = output / 'odd_support_verification.json.partial'
    temporary.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    temporary.replace(output / 'odd_support_verification.json')
    print(json.dumps({key: value for key, value in result.items() if key != 'actual_integer_polynomials'}))


if __name__ == '__main__':
    main()
