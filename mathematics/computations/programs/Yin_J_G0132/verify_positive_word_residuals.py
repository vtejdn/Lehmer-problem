"""Different AUTHOR verification of only the retained31-term word.

No producer arithmetic is imported.  The ring is the degree288 Laurent
quotient by Phi15^4*Phi960, with exact packed integer convolution and
complete primitive-factor weights reconstructed from the original word.
"""
from pathlib import Path
from collections import Counter
from math import gcd
import json
import sympy as sp

x, z = sp.symbols('x z')
C = [sp.Poly(2, x, domain=sp.ZZ), sp.Poly(x, x, domain=sp.ZZ)]
for _ in range(2, 145):
    C.append(sp.Poly(x, x, domain=sp.ZZ)*C[-1]-C[-2])


def coefficients(poly):
    return [int(poly.nth(i)) for i in range(poly.degree()+1)] if not poly.is_zero else [0]


def trace_factor(n):
    phi = sp.Poly(sp.cyclotomic_poly(n, z), z, domain=sp.ZZ)
    d = phi.degree()//2
    return sum((phi.nth(d+j)*C[j] for j in range(1, d+1)),
               sp.Poly(phi.nth(d), x, domain=sp.ZZ))


class LaurentRing:
    def __init__(self, polynomial, modulus):
        self.d = polynomial.degree()
        self.modulus = modulus
        self.p = [int(polynomial.nth(i)) % modulus for i in range(self.d+1)]
        assert self.p[0] == self.p[-1] == 1
        self.lower = [(i, v) for i, v in enumerate(self.p[:-1]) if v]
        self.one = [1]+[0]*(self.d-1)
        self.z = [0, 1]+[0]*(self.d-2)
        self.zi = [(-self.p[i+1]) % modulus for i in range(self.d)]
        assert self.multiply(self.z, self.zi) == self.one
        self.powers = {0: self.one, 1: self.z, -1: self.zi}

    def add(self, a, b, scale=1):
        return [(u+scale*v) % self.modulus for u, v in zip(a, b)]

    def multiply(self, a, b):
        # Base2^32 exceeds every convolution coefficient: d<=288, M<=20.
        assert self.d*(self.modulus-1)**2 < 2**32
        aa = int.from_bytes(b''.join(v.to_bytes(4, 'little') for v in a), 'little')
        bb = int.from_bytes(b''.join(v.to_bytes(4, 'little') for v in b), 'little')
        raw = (aa*bb).to_bytes(4*(2*self.d-1), 'little')
        values = [int.from_bytes(raw[4*i:4*i+4], 'little') % self.modulus
                  for i in range(2*self.d-1)]
        for i in range(len(values)-1, self.d-1, -1):
            lead = values[i]
            if lead:
                for j, value in self.lower:
                    values[i-self.d+j] = (values[i-self.d+j]-lead*value) % self.modulus
        return values[:self.d]

    def power(self, a, exponent):
        result = self.one
        while exponent:
            if exponent & 1:
                result = self.multiply(result, a)
            exponent //= 2
            if exponent:
                a = self.multiply(a, a)
        return result

    def z_power(self, exponent):
        if exponent not in self.powers:
            direction = 1 if exponent > 0 else -1
            start = max(self.powers) if direction == 1 else min(self.powers)
            for i in range(start+direction, exponent+direction, direction):
                previous = self.powers[i-direction]
                if direction == 1:
                    lead = previous[-1]
                    value = [0]+previous[:-1]
                    for j, v in self.lower:
                        value[j] = (value[j]-lead*v) % self.modulus
                else:
                    low = previous[0]
                    value = previous[1:]+[0]
                    value = [(v-low*self.p[j+1]) % self.modulus for j, v in enumerate(value)]
                self.powers[i] = value
        return self.powers[exponent]

    def argument(self, p):
        return self.add(self.z_power(p), self.z_power(-p))

    def evaluate(self, polynomial, argument):
        result = [0]*self.d
        for v in polynomial.all_coeffs():
            result = self.multiply(result, argument)
            result[0] = (result[0]+int(v)) % self.modulus
        return result

    def kernel(self, n, q):
        result = [0]*self.d
        for j in range(-(n-1)//2, (n-1)//2+1):
            result = self.add(result, self.z_power(q*j))
        return result


def trace_poly(values):
    return sp.Poly.from_list(list(reversed(values)), x, domain=sp.ZZ)


def binary_diagnostic(values, factor):
    polynomial = sp.Poly(trace_poly(values), x, modulus=2)
    if polynomial.is_zero:
        return 'infinity', [0]
    exponent = 0
    while polynomial.rem(factor).is_zero:
        polynomial = polynomial.exquo(factor)
        exponent += 1
    leading = polynomial.rem(factor)
    return exponent, [int(v) % 2 for v in coefficients(leading)]


def main():
    here = Path(__file__).resolve().parent
    output = here.parents[3]/'mathematics/computations/outputs'/here.name
    word = json.loads((here/'inputs/enlarged_doubled_positive_word.json').read_text(encoding='utf-8'))
    saved = json.loads((output/'positive_word_residuals.json').read_text(encoding='utf-8'))
    assert saved['terms'] == word['terms'] and len(word['terms']) == 31
    counts, cost = Counter(), 0
    for row in word['terms']:
        n, exponent = row['n'], row['exponent']
        assert n > 1 and gcd(n, 30) == 1 and 0 < exponent < 240
        for r in sp.divisors(n):
            if r > 1:
                counts[int(r)] += exponent
                if row['family'] == 'Gamma':
                    counts[3*int(r)] += exponent
        degree = (n-1)//2*(3 if row['family'] == 'Gamma' else 1)
        assert row['degree_contribution'] == degree*exponent
        cost += degree*exponent
    assert dict(counts) == {r['order']: r['multiplicity'] for r in word['cofactor_trace_factor_multiplicities']}
    assert cost == 112665 and cost+374 == saved['full_trace_degree'] == 113039
    full = counts+Counter({3: 4, 5: 6, 9: 8, 11: 2, 15: 4, 17: 2, 187: 2, 960: 1})
    expected_reciprocal = dict(full)
    expected_reciprocal[1] = 8
    assert expected_reciprocal == {r['order']: r['multiplicity'] for r in word['complete_reciprocal_cyclotomic_multiplicities']}
    binary = counts+Counter({3: 4, 5: 6, 9: 8, 11: 2, 15: 36, 17: 2, 187: 2})
    assert dict(binary) == {r['odd_order']: r['exponent'] for r in word['complete_binary_odd_order_exponents']}
    q = 4
    for value in binary.values():
        q = gcd(q, value & -value)
    radical = 1+sum(int(sp.totient(n))//2 for n in binary)
    assert q == 1 == saved['maximal_binary_Frobenius_exponent']
    assert radical == 801 == saved['full_binary_radical_degree']

    factors = {n: trace_factor(n) for n in set(full)|{480}}
    j2 = factors[15]**4*factors[960]
    assert j2.degree() == 144 and coefficients(j2) == saved['J_coefficients']
    assert factors[960] == factors[480].compose(C[2]) and factors[960] != factors[480]**2
    reciprocal = sp.Poly(sp.cyclotomic_poly(15, z)**4*sp.cyclotomic_poly(960, z), z, domain=sp.ZZ)
    assert reciprocal.degree() == 288
    # Check the exact integral trace/reciprocal identity by binomial expansion.
    expansion = sp.Poly(0, z, domain=sp.ZZ)
    for i in range(145):
        for k in range(i+1):
            expansion += sp.Poly(int(j2.nth(i))*int(sp.binomial(i, k))*z**(144+i-2*k), z)
    assert expansion == reciprocal
    ring = LaurentRing(reciprocal, 4)
    trace = ring.argument(1)

    def image(values):
        assert len(values) <= 144
        return ring.evaluate(trace_poly(values), trace)

    actual, theta_records, weight_records = {}, {}, {}
    for p, name in ((2, 'a'), (3, 'b'), (5, 'c')):
        exact_ring = LaurentRing(reciprocal, 4*p)
        numerator = exact_ring.evaluate(j2, exact_ring.argument(p))
        assert all(value % p == 0 for value in numerator)
        theta = [value//p for value in numerator]
        assert theta == image(saved['canonical_J_mod4'][str(p)])
        # Build Q's weight from ALL complete primitive factor counts, not B recurrences.
        q_weight = ring.one
        for n, exponent in sorted(counts.items()):
            contribution = ring.evaluate(factors[n], ring.argument(p))
            q_weight = ring.multiply(q_weight, ring.power(contribution, exponent))
        assert q_weight == image(saved['Q_evaluations_mod4'][str(p)])
        full_h = counts+Counter({3: 4, 5: 6, 9: 8, 11: 2, 17: 2, 187: 2})
        weight = ring.power(ring.evaluate(sp.Poly(x-2, x), ring.argument(p)), 4)
        for n, exponent in sorted(full_h.items()):
            contribution = ring.evaluate(factors[n], ring.argument(p))
            weight = ring.multiply(weight, ring.power(contribution, exponent))
        assert weight == image(saved['full_H_evaluations_mod4'][str(p)])
        # Also compare every selected term through the direct centered Laurent sum.
        records = saved['each_term_evaluation_mod4'][str(p)]
        assert len(records) == 31
        for row, record in zip(word['terms'], records):
            assert all(record[key] == value for key, value in row.items())
            value = ring.kernel(row['n'], p*(3 if row['family'] == 'Gamma' else 1))
            assert value == image(record['evaluated_factor'])
            assert ring.power(value, row['exponent']) == image(record['evaluated_power'])
        actual[name] = ring.multiply(weight, theta)
        theta_records[p], weight_records[p] = theta, weight

    a, b, c = [actual[key] for key in ('a', 'b', 'c')]
    c2, c3 = ring.power(c, 2), ring.power(c, 3)
    a3, a5, b2, b5 = ring.power(a, 3), ring.power(a, 5), ring.power(b, 2), ring.power(b, 5)
    actual['F'] = ring.add([2*v % 4 for v in c2], a5, -3)
    actual['G'] = ring.add(c3, b5, -2)
    base = ring.add(b2, a3, -1)
    actual['X_plus'], actual['X_minus'] = ring.add(base, actual['G']), ring.add(base, actual['G'], -1)
    f = sp.Poly(x**4+x**3+1, x, modulus=2)
    valuation, orders, units = {}, {}, {}
    for name, value in actual.items():
        assert value == image(saved['original_restrictions_mod4'][name]), name
        valuation[name] = 0 if any(v % 2 for v in value) else 1 if any(value) else 'at_least_2'
        assert valuation[name] == saved['restriction_valuations_through_mod4'][name]
        order, unit = binary_diagnostic(saved['original_restrictions_mod4'][name], f)
        orders[name], units[name] = order, unit
        assert order == saved['binary_f15_orders'][name] and unit == saved['binary_f15_initial_units'][name]
    gates = dict(F_mod4=not any(actual['F']),
                 X_plus_mod2=not any(v % 2 for v in actual['X_plus']),
                 X_minus_mod2=not any(v % 2 for v in actual['X_minus']),
                 X_plus_mod4=not any(actual['X_plus']), X_minus_mod4=not any(actual['X_minus']),
                 G_nonzero_mod2=any(v % 2 for v in actual['G']))
    assert gates == saved['global_gates_via_EG2']
    result = dict(scope='same ONE retained31-term word; all seven original restrictions',
                  implementation='different Laurent quotient, complete primitive-factor products and packed integer convolution',
                  reciprocal_quotient_degree=288, trace_quotient_degree=144,
                  exact_integer_trace_reciprocal_identity=True,
                  all93_term_values_and_powers_match=True,
                  all_three_canonical_divisions_and_full_weights_match=True,
                  all_seven_original_residues_match=True,
                  global_gates_via_EG2=gates, restriction_valuations_through_mod4=valuation,
                  binary_f15_orders=orders, binary_f15_initial_units=units,
                  full_trace_degree=113039, full_reciprocal_degree=226078,
                  cofactor_degree=cost, maximal_binary_Frobenius_exponent=q, full_binary_radical_degree=radical,
                  original_laurent_restrictions_mod4=actual,
                  canonical_laurent_J_mod4=theta_records, full_H_laurent_evaluations_mod4=weight_records,
                  author_self_check=True, independent_review=False, no_full_Q_or_T_expansion=True,
                  sympy_version=sp.__version__)
    temporary = output/'positive_word_residuals_verification.json.partial'
    temporary.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    temporary.replace(output/'positive_word_residuals_verification.json')
    print(json.dumps({key: result[key] for key in ('all93_term_values_and_powers_match',
                     'all_three_canonical_divisions_and_full_weights_match',
                     'all_seven_original_residues_match', 'global_gates_via_EG2',
                     'binary_f15_orders', 'binary_f15_initial_units')}))


if __name__ == '__main__':
    main()
