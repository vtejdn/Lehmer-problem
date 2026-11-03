"""One specified F9^4 B187 unit adjustment; full original degree187 T."""
from pathlib import Path
import json
from main import add, mul, rem, power, compose, chebyshev, canonical_mod4, trim
from odd_support_probe import binary_order, binary_initial_unit


def main():
    f3, f5 = [1, 1], [-1, 1, 1]
    f9 = [1, -3, 0, 1]
    f15, f30 = [1, 4, -4, -1, 1], [1, -4, -4, 1, 1]
    kernel = [1]
    for j in range(1, 94):
        kernel = add(kernel, chebyshev(j))
    r = power([-2, 1], 2)
    for factor, exponent in [(f15, 2), (f3, 2), (f5, 3), (f9, 4), (kernel, 1)]:
        r = mul(r, power(factor, exponent))
    t = mul(r, compose(f30, chebyshev(16)))
    assert len(t)-1 == 187
    a, b, c = [canonical_mod4(t, p) for p in (2, 3, 5)]
    f = rem(add([2*x for x in power(c, 2, t, 4)], power(a, 5, t, 4), -3), t, 4)
    g = rem(add(power(c, 3, t, 4), power(b, 5, t, 4), -2), t, 4)
    base = add(power(b, 2, t, 4), power(a, 3, t, 4), -1)
    xp, xm = rem(add(base, g), t, 4), rem(add(base, g, -1), t, 4)
    residues = dict(a=a, b=b, c=c, F=f, G=g, X_plus=xp, X_minus=xm)
    valuations = {key: (0 if any(v % 2 for v in poly)
                        else 1 if any(poly) else 'at_least_2')
                  for key, poly in residues.items()}
    halves = {name: [v//2 for v in poly] for name, poly in residues.items()
              if all(v % 2 == 0 for v in poly)}
    jodd = mul(f5, kernel, 2)
    dj = trim([(i*jodd[i]) % 2 for i in range(1, len(jodd))])
    diagnostics = dict(
        full_radical_degree=104, J_derivative_order_at_f3=binary_order(dj, f3),
        full_binary_orders={label: {name: binary_order(poly, factor) for name, poly in residues.items()}
                            for label, factor in [('f15', f15), ('f9', f9)]},
        half_f15_orders={name: binary_order(poly, f15) for name, poly in halves.items()},
        half_f15_initial_units={name: binary_initial_unit(poly, f15) for name, poly in halves.items()},
        first_nonzero_mod4={name: next(((i, v) for i, v in enumerate(poly) if v), None)
                            for name, poly in residues.items()},
        full_primary_binary_remainders={
            label: {name: rem(poly, modulus, 2) for name, poly in residues.items()}
            for label, modulus in [('X2', [0, 0, 1]), ('f3_squared', power(f3, 2, modulus=2)),
                ('f5_cubed', power(f5, 3, modulus=2)), ('f9_fourth', power(f9, 4, modulus=2)),
                ('f15_power18', power(f15, 18, modulus=2)), ('B187', kernel)]})
    payload = dict(candidate='(X-2)^2 F480 F15^2 F3^2 F5^3 F9^4 B187',
                   exact_single_case=True, degree=187, reciprocal_degree=374,
                   T_coefficients=t, R_coefficients=r, B187_coefficients=kernel,
                   residues_mod4=residues, coefficient_valuations_through_mod4=valuations,
                   diagnostics=diagnostics)
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    output.mkdir(parents=True, exist_ok=True)
    tmp = output/'unit_adjusted_result.json.partial'
    tmp.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'unit_adjusted_result.json')
    print(json.dumps(dict(degree=187, valuations=valuations,
                         diagnostics={k: v for k, v in diagnostics.items() if k != 'full_primary_binary_remainders'})))


if __name__ == '__main__':
    main()
