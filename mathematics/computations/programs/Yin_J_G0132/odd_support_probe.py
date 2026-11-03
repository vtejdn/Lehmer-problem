"""One fixed degree127 cyclotomic candidate; full original modular remainders.

The original four cases in main.py are not run or changed here.
This producer explicitly reuses that group's standard-library arithmetic.
"""
from pathlib import Path
import json

from main import add, mul, rem, power, compose, chebyshev, canonical_mod4, trim


def divide_binary(a, b):
    a = trim([v % 2 for v in a])
    b = trim([v % 2 for v in b])
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        q[k] = 1
        for j, value in enumerate(b):
            a[k + j] ^= value
        trim(a)
    return trim(q), a


def binary_order(poly, factor):
    value = trim([v % 2 for v in poly])
    if value == [0]:
        return 'infinity'
    order = 0
    while True:
        quotient, remainder = divide_binary(value, factor)
        if remainder != [0]:
            return order
        value = quotient
        order += 1


def binary_initial_unit(poly, factor):
    value = trim([v % 2 for v in poly])
    exponent = binary_order(value, factor)
    if exponent == 'infinity':
        return [0]
    for _ in range(exponent):
        value, residue = divide_binary(value, factor)
        assert residue == [0]
    return rem(value, factor, 2)


def main():
    f3, f5 = [1, 1], [-1, 1, 1]
    f15, f30 = [1, 4, -4, -1, 1], [1, -4, -4, 1, 1]
    b91 = [1]
    for j in range(1, 46):
        b91 = add(b91, chebyshev(j))
    cofactor = power([-2, 1], 2)
    for factor, exponent in ((f15, 2), (f3, 2), (f5, 3), (b91, 1)):
        cofactor = mul(cofactor, power(factor, exponent))
    v16 = compose(f30, chebyshev(16))
    t = mul(cofactor, v16)
    assert len(t) - 1 == 127
    a, b, c = [canonical_mod4(t, p) for p in (2, 3, 5)]
    a3, a5 = power(a, 3, t, 4), power(a, 5, t, 4)
    b2, b5 = power(b, 2, t, 4), power(b, 5, t, 4)
    c2, c3 = power(c, 2, t, 4), power(c, 3, t, 4)
    f = rem(add([2 * v for v in c2], a5, -3), t, 4)
    g = rem(add(c3, b5, -2), t, 4)
    xp = rem(add(add(b2, a3, -1), g), t, 4)
    xm = rem(add(add(b2, a3, -1), g, -1), t, 4)
    residues = dict(a=a, b=b, c=c, F=f, G=g, X_plus=xp, X_minus=xm)
    valuations = {name: (0 if any(v % 2 for v in poly)
                         else 1 if any(poly) else 'at_least_2')
                  for name, poly in residues.items()}
    j_odd = mul(f5, b91, 2)
    j_derivative = trim([(i * j_odd[i]) % 2 for i in range(1, len(j_odd))])
    assert all(v % 2 == 0 for v in f)
    fhalf = [v // 2 for v in f]
    diagnostics = dict(
        B91_plus_F5_order_at_f3=binary_order(add(b91, f5), f3),
        J_derivative_order_at_f3=binary_order(j_derivative, f3),
        full_radical_degree=53,
        odd_multiplicity_factor_degree=len(j_odd)-1,
        binary_f15_orders={name: binary_order(poly, f15)
                           for name, poly in residues.items()},
        F_half_binary_f15_order=binary_order(fhalf, f15),
        f15_initial_units={name: binary_initial_unit(poly, f15)
                           for name, poly in [('F_half', fhalf), ('X_plus', xp), ('X_minus', xm)]},
        first_nonzero_mod4={name: next(((i, v) for i, v in enumerate(poly) if v), None)
                            for name, poly in residues.items()},
        full_primary_binary_remainders={
            label: {name: rem(poly, modulus, 2) for name, poly in residues.items()}
            for label, modulus in (
                ('X2', [0, 0, 1]), ('f3_squared', power(f3, 2, modulus=2)),
                ('f5_cubed', power(f5, 3, modulus=2)),
                ('f15_power18', power(f15, 18, modulus=2)), ('B91', b91))})
    payload = dict(
        candidate='(X-2)^2 F480 F15^2 F3^2 F5^3 B91',
        exact_single_case=True, degree=127, reciprocal_degree=254,
        T_coefficients=t, R_coefficients=cofactor, B91_coefficients=b91,
        J_binary_coefficients=j_odd, J_derivative_binary_coefficients=j_derivative,
        residues_mod4=residues, coefficient_valuations_through_mod4=valuations,
        diagnostics=diagnostics,
        arithmetic='monic integer remainder modulo4p, then actual division by p')
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    output.mkdir(parents=True, exist_ok=True)
    temporary = output / 'odd_support_result.json.partial'
    temporary.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    temporary.replace(output / 'odd_support_result.json')
    print(json.dumps(dict(degree=127, valuations=valuations,
                         diagnostic_orders={key: diagnostics[key] for key in (
                             'B91_plus_F5_order_at_f3', 'J_derivative_order_at_f3',
                             'binary_f15_orders', 'F_half_binary_f15_order',
                             'f15_initial_units', 'first_nonzero_mod4')})))


if __name__ == '__main__':
    main()
