"""Author self-check via full-Z Laurent kernels in Z[z]/Phi480.

No producer imports; only the four declared periodic restrictions are checked.
"""
from pathlib import Path
import json
import sympy as sp

x, z = sp.symbols('x z')
C = [sp.Poly(2, x, domain=sp.ZZ), sp.Poly(x, x, domain=sp.ZZ)]
for _ in range(2, 65):
    C.append(sp.Poly(x, x, domain=sp.ZZ)*C[-1]-C[-2])


def trace_factor(n):
    phi = sp.Poly(sp.cyclotomic_poly(n, z), z, domain=sp.ZZ)
    d = phi.degree()//2
    return sum((phi.nth(d+j)*C[j] for j in range(1, d+1)),
               sp.Poly(phi.nth(d), x, domain=sp.ZZ))


def coeff(poly):
    return [int(poly.nth(j)) for j in range(poly.degree()+1)] if poly else [0]


def valuation(poly):
    values = [abs(int(v)) for v in poly.all_coeffs() if v]
    return min((v & -v).bit_length()-1 for v in values) if values else 'infinity'


def main():
    here = Path(__file__).resolve().parent
    output = here.parents[3] / 'mathematics/computations/outputs' / here.name
    saved = json.loads((output/'odd_support_family.json').read_text(encoding='utf-8'))
    classes = [(6, 187), (7, 379), (8, 763), (9, 571)]
    assert saved['period'] == 960 and len(saved['cases']) == 4
    phi = sp.Poly(sp.cyclotomic_poly(480, z), z, domain=sp.ZZ)
    v = trace_factor(480)
    r0 = (sp.Poly((x-2)**2, x)*trace_factor(15)**2
          *trace_factor(3)**2*trace_factor(5)**3)
    assert coeff(v) == saved['V_coefficients']
    assert coeff(r0) == saved['R0_coefficients']
    zp = [sp.Poly(1, z, domain=sp.ZZ)]
    for _ in range(480):
        zp.append((zp[-1]*sp.Poly(z, z)).rem(phi))
    assert zp[480] == zp[0]
    trace = zp[1]+zp[479]

    def evaluate(poly, argument):
        result = sp.Poly(0, z, domain=sp.ZZ)
        for value in poly.all_coeffs():
            result = (result*argument+int(value)).rem(phi)
        return result

    def ringpower(poly, exponent):
        result = sp.Poly(1, z, domain=sp.ZZ)
        for _ in range(exponent):
            result = (result*poly).rem(phi)
        return result

    cp = {p: zp[p]+zp[(-p) % 480] for p in (2, 3, 5)}
    theta = {}
    for p in (2, 3, 5):
        numerator = evaluate(v, cp[p])
        assert all(int(a) % p == 0 for a in numerator.all_coeffs())
        theta[p] = sp.Poly.from_list([int(a)//p for a in numerator.all_coeffs()], z)
    rows = []
    for (s, n), original in zip(classes, saved['cases']):
        assert original['s_class'] == s and original['representative_n'] == n
        assert original['first_family_n'] == 3*2**s-5
        assert original['original_first_trace_degree'] == 82+(3*2**s-6)//2
        assert original['quotient_degree'] == 64
        canonical = []
        for p in (2, 3, 5):
            a = (n-1)//2
            kernel = sum((zp[(p*j) % 480] for j in range(-a, a+1)), sp.Poly(0, z))
            canonical.append((evaluate(r0, cp[p])*kernel*theta[p]).rem(phi))
        a, b, c = canonical
        f = (2*ringpower(c, 2)-3*ringpower(a, 5)).rem(phi)
        g = (ringpower(c, 3)-2*ringpower(b, 5)).rem(phi)
        base = ringpower(b, 2)-ringpower(a, 3)
        actual = dict(a=a, b=b, c=c, F=f, G=g,
                      X_plus=(base+g).rem(phi), X_minus=(base-g).rem(phi))
        exact = {}
        for name, poly in actual.items():
            trace_poly = sp.Poly.from_list(list(reversed(original['residues_mod4'][name])), x)
            assert trace_poly.degree() < 64 or trace_poly.is_zero
            difference = (evaluate(trace_poly, trace)-poly).rem(phi)
            assert all(int(a) % 4 == 0 for a in difference.all_coeffs()), (n, name)
            value = valuation(poly)
            exact[name] = value
            truncated = value if isinstance(value, int) and value < 2 else 'at_least_2'
            assert original['restriction_valuations_through_mod4'][name] == truncated
        rows.append(dict(s_class=s, representative_n=n,
                         all_seven_trace_images_match_mod4=True,
                         exact_cyclotomic_basis_restriction_valuations=exact,
                         actual_integer_cyclotomic_basis={key: coeff(value) for key, value in actual.items()}))
    result = dict(scope='four periodic restrictions, never full original remainders',
                  implementation='separate full-Z Laurent sums in Z[z]/Phi480',
                  quotient_reciprocal_degree=128, cases=rows, sympy_version=sp.__version__)
    temporary = output/'odd_support_family_verification.json.partial'
    temporary.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    temporary.replace(output/'odd_support_family_verification.json')
    print(json.dumps([{key: value for key, value in row.items()
                       if key != 'actual_integer_cyclotomic_basis'} for row in rows]))


if __name__ == '__main__':
    main()
