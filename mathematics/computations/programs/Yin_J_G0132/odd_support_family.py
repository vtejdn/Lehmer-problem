"""Exactly four periodic degree64 restrictions; never expanded full T_s."""
from pathlib import Path
import json
from main import add, mul, rem, power, compose, chebyshev, canonical_mod4
from odd_support_probe import binary_order, binary_initial_unit

CLASSES = [(6, 187), (7, 379), (8, 763), (9, 571)]


def kernel_at(n, argument, divisor, modulus):
    assert n > 0 and n % 2 == 1
    left, right = [2], rem(argument, divisor, modulus)
    total = [1]
    for _ in range(1, (n-1)//2+1):
        total = add(total, right, modulus=modulus)
        left, right = right, rem(add(mul(argument, right, modulus), left, -1,
                                     modulus=modulus), divisor, modulus)
    return rem(total, divisor, modulus)


def main():
    f3, f5 = [1, 1], [-1, 1, 1]
    f15, f30 = [1, 4, -4, -1, 1], [1, -4, -4, 1, 1]
    v = compose(f30, chebyshev(16))
    r0 = power([-2, 1], 2)
    for factor, exponent in [(f15, 2), (f3, 2), (f5, 3)]:
        r0 = mul(r0, power(factor, exponent))
    theta = {p: canonical_mod4(v, p) for p in (2, 3, 5)}
    rows = []
    for s, n in CLASSES:
        assert (3*2**s-5) % 960 == n
        canonical = []
        for p in (2, 3, 5):
            cp = chebyshev(p)
            weight = rem(mul(compose(r0, cp, v, 4), kernel_at(n, cp, v, 4), 4), v, 4)
            canonical.append(rem(mul(weight, theta[p], 4), v, 4))
        a, b, c = canonical
        f = rem(add([2*x for x in power(c, 2, v, 4)], power(a, 5, v, 4), -3), v, 4)
        g = rem(add(power(c, 3, v, 4), power(b, 5, v, 4), -2), v, 4)
        base = add(power(b, 2, v, 4), power(a, 3, v, 4), -1)
        xp, xm = rem(add(base, g), v, 4), rem(add(base, g, -1), v, 4)
        residues = dict(a=a, b=b, c=c, F=f, G=g, X_plus=xp, X_minus=xm)
        valuations = {key: (0 if any(x % 2 for x in poly)
                            else 1 if any(poly) else 'at_least_2')
                      for key, poly in residues.items()}
        assert all(x % 2 == 0 for x in f)
        fh = [x//2 for x in f]
        rows.append(dict(s_class=s, representative_n=n, first_family_n=3*2**s-5,
                         original_first_trace_degree=82+(3*2**s-6)//2,
                         quotient_degree=64, residues_mod4=residues,
                         restriction_valuations_through_mod4=valuations,
                         F_half_f15_order=binary_order(fh, f15),
                         F_half_initial_unit=binary_initial_unit(fh, f15),
                         binary_f15_orders={key: binary_order(poly, f15)
                                            for key, poly in residues.items()}))
    payload = dict(scope='four periodic factor restrictions only; not full T remainders',
                   family='n_s=3*2^s-5, s>=6', period=960,
                   V_coefficients=v, R0_coefficients=r0, cases=rows)
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    output.mkdir(parents=True, exist_ok=True)
    temporary = output/'odd_support_family.json.partial'
    temporary.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    temporary.replace(output/'odd_support_family.json')
    print(json.dumps([{key: value for key, value in row.items() if key != 'residues_mod4'} for row in rows]))


if __name__ == '__main__':
    main()
