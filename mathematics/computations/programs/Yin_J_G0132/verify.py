"""Independent full-integer SymPy reconstruction; imports no producer code."""
from pathlib import Path
import json
import sympy as sp

CASES = [(2, 2, 3, 2, 16, 0), (2, 8, 12, 4, 16, 1),
         (4, 8, 12, 4, 16, 1), (2, 4, 6, 2, 8, 1)]
x, z = sp.symbols('x z')
C = [sp.Poly(2, x), sp.Poly(x, x)]
for j in range(2, 17):
    C.append(sp.Poly(x, x) * C[-1] - C[-2])


def trace_factor(n):
    phi = sp.Poly(sp.cyclotomic_poly(n, z), z)
    d = phi.degree() // 2
    result = sp.Poly(phi.nth(d), x)
    for j in range(1, d + 1):
        result += phi.nth(d + j) * C[j]
    return result


def coefficients(poly, modulus=None):
    values = [int(poly.nth(j)) for j in range(max(0, poly.degree()) + 1)] if poly else [0]
    if modulus:
        values = [v % modulus for v in values]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def valuation(poly):
    values = [abs(int(v)) for v in poly.all_coeffs() if v]
    return min((v & -v).bit_length() - 1 for v in values) if values else 'infinity'


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    output = root / 'mathematics' / 'computations' / 'outputs' / here.name
    original = json.loads((output / 'result.json').read_text(encoding='utf-8'))
    assert original['parameter_order'] == ['A', 'B', 'D', 'K', 'w', 'e']
    assert len(original['cases']) == len(CASES)
    f3, f5, f15, f30 = [trace_factor(n) for n in (3, 5, 15, 30)]
    verified = []
    for params, saved in zip(CASES, original['cases']):
        aa, bb, dd, kk, w, e = params
        t = (sp.Poly(x ** aa, x) * f3 ** bb * f5 ** dd * f15 ** kk
             * f30.compose(C[w]) * f30.compose(C[w // 2]) ** e)
        assert saved['parameters'] == list(params)
        assert saved['degree'] == t.degree()
        assert saved['T_coefficients'] == coefficients(t)
        canonical = []
        for p in (2, 3, 5):
            r = t.compose(C[p]).rem(t)
            assert all(int(v) % p == 0 for v in r.all_coeffs())
            canonical.append(sp.Poly.from_list([int(v) // p for v in r.all_coeffs()], x))
        a, b, c = canonical
        f = (2 * c ** 2 - 3 * a ** 5).rem(t)
        g = (c ** 3 - 2 * b ** 5).rem(t)
        xp = (b ** 2 - a ** 3 + g).rem(t)
        xm = (b ** 2 - a ** 3 - g).rem(t)
        actual = dict(a=a, b=b, c=c, F=f, G=g, X_plus=xp, X_minus=xm)
        exact = {}
        for name, poly in actual.items():
            assert saved['residues_mod4'][name] == coefficients(poly, 4), name
            v = valuation(poly)
            truncated = v if isinstance(v, int) and v < 2 else 'at_least_2'
            assert saved['coefficient_valuations_through_mod4'][name] == truncated
            exact[name] = v
        verified.append(dict(parameters=list(params), degree=t.degree(),
                             exact_coefficient_valuations=exact,
                             all_T_coefficients_and_seven_residue_arrays_match=True))
    result = dict(implementation='separate full-integer SymPy cyclotomic trace reconstruction',
                  cases=verified, finite_cases=4, residue_arrays_compared=28)
    temporary = output / 'verification.json.partial'
    temporary.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    temporary.replace(output / 'verification.json')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
