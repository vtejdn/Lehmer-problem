"""Different AUTHOR verification of the complete full-eighth kernel certificate.

The producer is not imported.  All actual joint generator images are rebuilt
in faithful Laurent rings.  Mixed arithmetic uses ordinary modulo-four
coefficient convolution and monic division, followed by the exact B quotient.
This program checks the one retained target, never a new residual probe.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
from math import comb, gcd
from array import array
import json
import sys
import sympy as sp

from verify_augmented_endpoint_kernel_image import Ring as BinaryRing, bits


X, Z = sp.symbols('X Z')


def binary_remainder(value, modulus):
    while value.bit_length() >= modulus.bit_length():
        value ^= modulus << (value.bit_length() - modulus.bit_length())
    return value


def binary_inverse(value, modulus):
    u, v, a, b = binary_remainder(value, modulus), modulus, 1, 0
    while u != 1:
        if not u:
            raise ValueError('nonunit at the stated binary modulus')
        shift = u.bit_length() - v.bit_length()
        if shift < 0:
            u, v, a, b = v, u, b, a
            shift = -shift
        u ^= v << shift
        a ^= b << shift
    return binary_remainder(a, modulus)


@lru_cache(maxsize=8192)
def packed_coefficients(values):
    """Base65536 packing: all coefficients are ordinary integers0..3."""
    raw = array('H', values)
    if sys.byteorder != 'little':
        raw.byteswap()
    return int.from_bytes(raw.tobytes(), 'little')


class ModFourRing:
    """Exact (Z/4)[variable]/monic polynomial, not a graded-ring model."""
    def __init__(self, polynomial):
        self.degree = polynomial.degree()
        self.polynomial = tuple(int(polynomial.nth(i)) % 4
                                for i in range(self.degree + 1))
        assert self.polynomial[-1] == 1
        assert self.degree * 9 < 65536
        self.lower = tuple((i, c) for i, c in enumerate(self.polynomial[:-1]) if c)
        self.binary_modulus = sum((c & 1) << i for i, c in enumerate(self.polynomial))
        self.one = (1,) + (0,) * (self.degree - 1)
        self.zero = (0,) * self.degree

    def reduce(self, values):
        work = [int(v) % 4 for v in values]
        if len(work) < self.degree:
            work.extend([0] * (self.degree - len(work)))
        for top in range(len(work) - 1, self.degree - 1, -1):
            lead = work[top]
            if lead:
                for index, coefficient in self.lower:
                    k = top - self.degree + index
                    work[k] = (work[k] - lead * coefficient) % 4
        return tuple(work[:self.degree])

    def add(self, first, second, scale=1):
        return tuple((a + scale*b) % 4 for a, b in zip(first, second))

    def multiply(self, first, second):
        if first == self.one:
            return second
        if second == self.one:
            return first
        if first == self.zero or second == self.zero:
            return self.zero
        raw = (packed_coefficients(first) * packed_coefficients(second)).to_bytes(
            2 * (2 * self.degree - 1), 'little')
        values = array('H')
        values.frombytes(raw)
        if sys.byteorder != 'little':
            values.byteswap()
        return self.reduce(values)

    def power(self, value, exponent):
        answer = self.one
        while exponent:
            if exponent & 1:
                answer = self.multiply(answer, value)
            exponent //= 2
            if exponent:
                value = self.multiply(value, value)
        return answer

    @lru_cache(maxsize=8192)
    def inverse(self, value):
        residue = sum((c & 1) << i for i, c in enumerate(value))
        inverse = binary_inverse(residue, self.binary_modulus)
        lift = tuple((inverse >> i) & 1 for i in range(self.degree))
        error = self.multiply(value, lift)
        assert all((v & 1) == (i == 0) for i, v in enumerate(error))
        two_minus_error = tuple(((2 if i == 0 else 0) - v) % 4
                                for i, v in enumerate(error))
        answer = self.multiply(lift, two_minus_error)
        assert self.multiply(value, answer) == self.one
        return answer


class CharacterRing:
    """B=(Z/4)[X]/(V,2P^28), with coefficient-list arithmetic."""
    def __init__(self, V):
        self.ring = ModFourRing(V)
        assert self.ring.degree == 128
        self.high_modulus = bits(sp.Poly((X**4+X**3+1)**28, X, modulus=2))
        self.one = self.ring.one

    def normal(self, value):
        low = [v & 1 for v in value]
        high = sum(((v >> 1) & 1) << i for i, v in enumerate(value))
        high = binary_remainder(high, self.high_modulus)
        return tuple(low[i] + 2*((high >> i) & 1) for i in range(128))

    def decode(self, planes):
        assert len(planes) == 2
        low, high = planes
        assert isinstance(low, int) and 0 <= low < 1 << 128
        assert isinstance(high, int) and 0 <= high < 1 << 112
        return tuple(((low >> i) & 1) + 2*((high >> i) & 1) for i in range(128))

    def encode(self, value):
        assert self.normal(value) == value
        return [sum((v & 1) << i for i, v in enumerate(value)),
                sum(((v >> 1) & 1) << i for i, v in enumerate(value))]

    def multiply(self, first, second):
        return self.normal(self.ring.multiply(first, second))

    def power(self, value, exponent):
        answer = self.one
        while exponent:
            if exponent & 1:
                answer = self.multiply(answer, value)
            exponent //= 2
            if exponent:
                value = self.multiply(value, value)
        return answer

    @lru_cache(maxsize=8192)
    def inverse(self, value):
        result = self.normal(self.ring.inverse(value))
        assert self.multiply(value, result) == self.one
        return result

    def half(self, value):
        assert all((v & 1) == (i == 0) for i, v in enumerate(value))
        # Subtract1 as an integer coefficient representative before /2.
        even = tuple((v - (i == 0)) % 4 for i, v in enumerate(value))
        assert all(v % 2 == 0 for v in even)
        return binary_remainder(sum((v//2) << i for i, v in enumerate(even)),
                                self.high_modulus)


def full_trace_factor(n):
    cyclotomic = sp.Poly(sp.cyclotomic_poly(n, Z), Z, domain=sp.ZZ)
    degree = cyclotomic.degree() // 2
    cheb = [sp.Poly(2, X), sp.Poly(X, X)]
    for _ in range(2, degree + 1):
        cheb.append(sp.Poly(X, X)*cheb[-1] - cheb[-2])
    result = sp.Poly(int(cyclotomic.nth(degree)), X)
    for j in range(1, degree + 1):
        result += int(cyclotomic.nth(degree+j))*cheb[j]
    return result


class FaithfulCharacterImages:
    """Generate Omega from complete centered Laurent kernels moduloPhi960."""
    def __init__(self, character_ring):
        self.B = character_ring
        self.ring = ModFourRing(sp.Poly(sp.cyclotomic_poly(960, Z), Z, domain=sp.ZZ))
        assert self.ring.degree == 256
        self.z = self.ring.reduce([0, 1])
        self.shift = self.ring.power(self.z, 127)
        assert self.ring.power(self.z, 960) == self.ring.one
        assert self.ring.power(self.z, 480) == self.ring.add(self.ring.zero, self.ring.one, -1)
        self.shifted = []
        for j in range(128):
            self.shifted.append(tuple((127+j-2*k, comb(j, k) % 4)
                                      for k in range(j+1) if comb(j, k) % 4))

    def recover_trace(self, value):
        work = list(self.ring.multiply(self.shift, value))
        assert work[255] == 0
        result = [0] * 128
        for j in range(127, -1, -1):
            coefficient = work[127+j]
            result[j] = coefficient
            if coefficient:
                for i, v in self.shifted[j]:
                    work[i] = (work[i] - coefficient*v) % 4
        assert not any(work)
        return tuple(result)

    @lru_cache(maxsize=8192)
    def kernel(self, n, index):
        values = [0] * 960
        for j in range(-(n-1)//2, (n-1)//2+1):
            k = (index*j) % 960
            values[k] = (values[k]+1) % 4
        return self.ring.reduce(values)

    def endpoint(self, index):
        values = [0] * 960
        values[index % 960] += 1
        values[-index % 960] += 1
        values[0] -= 2
        return self.ring.reduce(values)

    def image(self, label):
        if label['kind'] == 'endpoint':
            weight2, weight5 = self.endpoint(2), self.endpoint(5)
        else:
            weight2 = self.kernel(label['n'], 2*label['q'])
            weight5 = self.kernel(label['n'], 5*label['q'])
        inverse2 = self.ring.inverse(weight2)
        omega = self.ring.multiply(self.ring.power(weight5, 2),
                                   self.ring.power(inverse2, 5))
        return (self.B.normal(self.recover_trace(omega)),
                self.B.normal(self.recover_trace(weight2)),
                self.B.normal(self.recover_trace(weight5)))


def xi_pack(values):
    a, b, c = values
    assert 0 <= a < 1 << 64 and 0 <= b < 1 << 24 and 0 <= c < 1 << 24
    return a | (b << 64) | (c << 88)


def xi_unpack(value):
    return value & ((1 << 64)-1), (value >> 64) & ((1 << 24)-1), value >> 88


class XiImages:
    def __init__(self):
        polynomials = [sp.Poly((Z**4+Z**3+1)**16, Z, modulus=2),
                       sp.Poly((Z+1)**24, Z, modulus=2),
                       sp.Poly((Z**2+Z+1)**12, Z, modulus=2)]
        self.rings = [BinaryRing(bits(p)) for p in polynomials]
        self.one = (1, 1, 1)
        self.recoverers = []
        for order, multiplicity, period, target in zip((15, 3, 5), (16, 24, 12),
                                                        (240, 96, 80), self.rings):
            lr = BinaryRing(bits(sp.Poly(sp.cyclotomic_poly(order, Z), Z, modulus=2)**multiplicity))
            d = target.degree
            assert lr.degree == 2*d
            powers = [1]
            for _ in range(period):
                powers.append(lr.multiply(powers[-1], 2))
            assert powers[period] == 1
            trace = powers[1] ^ powers[-2]
            trace_powers = [1]
            for _ in range(d-1):
                trace_powers.append(lr.multiply(trace_powers[-1], trace))
            shifted = [lr.multiply(powers[d-1], v) for v in trace_powers]

            def recover(value, lr=lr, d=d, powers=powers, shifted=shifted):
                work = lr.multiply(powers[d-1], value)
                assert work.bit_length() <= 2*d-1
                result = 0
                for j in range(d-1, -1, -1):
                    if (work >> (d-1+j)) & 1:
                        result |= 1 << j
                        work ^= shifted[j]
                assert work == 0
                return result

            assert recover(trace) == 2

            def kernel(n, q, period=period, lr=lr, recover=recover):
                value = 0
                for j in range(-(n-1)//2, (n-1)//2+1):
                    value ^= 1 << ((q*j) % period)
                return recover(lr.reduce(value))
            self.recoverers.append(lru_cache(maxsize=8192)(kernel))

    def image(self, label):
        if label['kind'] == 'endpoint':
            return (2, 2, 2)
        return tuple(fn(label['n'], label['q']) for fn in self.recoverers)

    def multiply(self, first, second):
        return tuple(r.multiply(a, b) for r, a, b in zip(self.rings, first, second))

    def power(self, value, exponent):
        return tuple(r.power(a, exponent) for r, a in zip(self.rings, value))


def actual_target(output):
    arrays = json.loads((output/'endpoint_kernel_product_mod8_verification.json').read_text(encoding='utf-8'))
    original = json.loads((output/'endpoint_kernel_product_mod8.json').read_text(encoding='utf-8'))
    values = arrays['original_restrictions_mod8']
    assert values == original['original_restrictions_mod8']
    assert arrays['all7_full_mod8_trace_arrays_recovered_and_matched']
    assert all(c % 4 == 0 for c in values['F'])
    f = sp.Poly(X**4+X**3+1, X, modulus=2)

    def binary_poly(coefficients):
        return sp.Poly.from_list(list(reversed(coefficients)), X, modulus=2)

    c = binary_poly(values['c'])
    gamma = c.exquo(f**4).rem(f**28)
    quarter = binary_poly([v//4 for v in values['F']])
    numerator = quarter.exquo(f**8).rem(f**28)
    denominator = (gamma**2).rem(f**28)
    target = (numerator*sp.invert(denominator, f**28)).rem(f**28)
    return dict(source_result='endpoint_kernel_product_mod8.json',
                source_verification='endpoint_kernel_product_mod8_verification.json',
                c_binary=bits(c), quarter_binary=bits(quarter),
                gamma_mod_f28=bits(gamma), quarter_div_f8=bits(numerator),
                gamma_squared_mod_f28=bits(denominator), target=bits(target))


def decode_word(word, count=4193):
    assert isinstance(word, list) and word == sorted(word)
    assert len({i for i, e in word}) == len(word)
    assert all(isinstance(i, int) and 0 <= i < count and isinstance(e, int)
               and 0 < e < 960 for i, e in word)
    return dict(word)


def add_word(first, second, scale=1):
    answer = dict(first)
    for index, exponent in second.items():
        value = (answer.get(index, 0) + scale*exponent) % 960
        if value:
            answer[index] = value
        else:
            answer.pop(index, None)
    return answer


def encode_word(word):
    return [[i, e] for i, e in sorted(word.items())]


@lru_cache(maxsize=None)
def phi(n):
    return int(sp.totient(n))


def actual_costs(word, labels):
    counts = Counter()
    endpoint = 0
    terms = []
    for index, exponent in sorted(word.items()):
        assert 0 < exponent < 960
        label = labels[index]
        terms.append({key: label[key] for key in ('kind', 'n', 'q', 'a', 'b', 'trace_degree') if key in label}
                     | dict(index=index, exponent=exponent,
                            degree_contribution=exponent*label['trace_degree']))
        if label['kind'] == 'endpoint':
            endpoint += exponent
        else:
            for divisor in sp.divisors(label['n'])[1:]:
                for a in range(label['a']+1):
                    for b in range(label['b']+1):
                        counts[int(divisor)*3**a*5**b] += exponent
    degree = sum(row['degree_contribution'] for row in terms)
    assert degree == endpoint + sum(e*phi(n)//2 for n, e in counts.items())
    reciprocal = dict(counts)
    if endpoint:
        reciprocal[1] = 2*endpoint
    assert 2*degree == sum(e*phi(n) for n, e in reciprocal.items())
    return dict(terms=terms, endpoint_exponent=endpoint, nonzero_terms=len(word),
                kernel_trace_degree=degree, kernel_reciprocal_degree=2*degree,
                resulting_T_trace_degree_not_tested=6520358+degree,
                resulting_T_reciprocal_degree_not_tested=2*(6520358+degree),
                complete_trace_factors=[dict(order=n, multiplicity=e) for n, e in sorted(counts.items())],
                complete_reciprocal_factors=[dict(order=n, multiplicity=e) for n, e in sorted(reciprocal.items())])


def binary_division(value, divisor):
    quotient = 0
    while value and value.bit_length() >= divisor.bit_length():
        shift = value.bit_length() - divisor.bit_length()
        quotient ^= 1 << shift
        value ^= divisor << shift
    return quotient, value


def xi_leading(value):
    if value == (1, 1, 1):
        return None
    for unit, prime, degree, length, offset in zip(value, (25, 3, 7), (4, 1, 2),
                                                    (16, 24, 12), (0, 60, 83)):
        if unit == 1:
            continue
        work, layer = unit ^ 1, 0
        while True:
            quotient, coefficient = binary_division(work, prime)
            if coefficient:
                break
            work, layer = quotient, layer+1
        assert 1 <= layer < length
        bit = next(i for i in range(degree) if (coefficient >> i) & 1)
        return offset + degree*(layer-1) + bit
    raise AssertionError('a nonidentity principal class has a leading position')


def main():
    here = Path(__file__).resolve().parent
    output = here.parents[3]/'mathematics/computations/outputs'/here.name
    saved = json.loads((output/'full_eighth_kernel_image.json').read_text(encoding='utf-8'))
    quotient = json.loads((output/'augmented_endpoint_kernel_image.json').read_text(encoding='utf-8'))
    original = json.loads((output/'endpoint_kernel_product_mod8.json').read_text(encoding='utf-8'))
    tracked = json.loads((here/'inputs/endpoint_kernel_product_word.json').read_text(encoding='utf-8'))
    assert original['terms'] == tracked['terms'] and len(tracked['terms']) == 138
    assert tracked['costs']['original_trace_degree'] == 6520358
    assert quotient['principal_rank'] == 92 and quotient['odd_subgroup_order'] == 45
    assert quotient['subgroup_order'] == 45*(1 << 92)
    assert saved['joint_exponent'] == 960
    target_data = actual_target(output)
    assert target_data == saved['target_data']

    # Full integer primitive trace and monic cancellation, before reduction.
    V = full_trace_factor(960)
    P = full_trace_factor(15)
    J = sp.Poly.from_list(list(reversed(original['J_coefficients'])), X, domain=sp.ZZ)
    assert J.exquo(P**4) == V and V.degree() == 128
    exact_v = [int(V.nth(i)) for i in range(129)]
    assert exact_v == saved['actual_V_coefficients']
    assert [v % 4 for v in exact_v] == saved['V_coefficients_mod4']
    B = CharacterRing(V)
    assert saved['high_modulus'] == B.high_modulus
    assert saved['binary_V_modulus'] == B.ring.binary_modulus
    laurent = FaithfulCharacterImages(B)
    xi = XiImages()

    # Complete actual parameter list, independently reconstructed.
    mixed_minima = {}
    for a in range(1, 9):
        for b in range(1, 9):
            q = 3**a*5**b
            mixed_minima[q % 480] = min(q, mixed_minima.get(q % 480, q))
    qs = sorted({1, *[3**a for a in range(1, 9)], *[5**b for b in range(1, 9)],
                 *mixed_minima.values()})
    ns = [n for n in range(2, 480) if gcd(n, 480) == 1]
    assert qs == quotient['q_representatives'] and ns == quotient['n_representatives']
    assert len(qs) == 33 and len(ns) == 127
    labels = [dict(kind='endpoint', integer_factor='X-2', trace_degree=1)]
    for n in ns:
        for q in qs:
            factorization = sp.factorint(q)
            a, b = int(factorization.get(3, 0)), int(factorization.get(5, 0))
            assert q == 3**a*5**b
            labels.append(dict(kind='rectangle', n=n, q=q, q_residue=q % 480,
                               a=a, b=b, trace_degree=q*(n-1)//2))
    labels.append(dict(kind='rectangle', n=481, q=1, q_residue=1,
                       a=0, b=0, trace_degree=240))
    assert len(labels) == saved['generator_count'] == 4193
    assert len(saved['generators']) == 4193
    xis, omegas, verified_images = [], [], []
    for index, (label, row) in enumerate(zip(labels, saved['generators'])):
        projected = xi.image(label)
        omega, weight2, weight5 = laurent.image(label)
        expected = label | dict(xi_image=xi_pack(projected), xi_components=list(projected),
                                weight_C2=B.encode(weight2), weight_C5=B.encode(weight5),
                                omega=B.encode(omega))
        assert row == expected
        if index < 4192:
            old = quotient['generators'][index]
            assert {k: v for k, v in old.items() if k not in ('image', 'components')} == label
            assert old['image'] == xi_pack(projected) and old['components'] == list(projected)
        assert B.power(omega, 960) == B.one
        assert xi.power(projected, 480) == xi.one
        xis.append(projected)
        omegas.append(omega)
        verified_images.append(dict(index=index, xi_image=xi_pack(projected), omega=B.encode(omega)))
        if (index+1) % 1024 == 0:
            print(f'faithful joint images checked: {index+1}/4193', flush=True)
    assert omegas[-1] == B.one
    assert xis[-1] == xi.power(xis[0], 240)
    print('all4193 faithful joint images and old projections checked', flush=True)

    # Cache powers of genuine label images; every word uses exponents<960.
    word_powers = {}

    def word_image(word):
        mx, bx = xi.one, B.one
        for index, exponent in sorted(word.items()):
            assert 0 <= index < 4193 and 0 < exponent < 960
            if index not in word_powers:
                xv, bv = [xis[index]], [omegas[index]]
                for _ in range(9):
                    xv.append(xi.multiply(xv[-1], xv[-1]))
                    bv.append(B.multiply(bv[-1], bv[-1]))
                word_powers[index] = xv, bv
            xv, bv = word_powers[index]
            for j in range(10):
                if (exponent >> j) & 1:
                    mx = xi.multiply(mx, xv[j])
                    bx = B.multiply(bx, bv[j])
        return mx, bx

    odd = {}
    assert len(saved['odd_lifts']) == len(quotient['odd_subgroup']) == 45
    for row, old in zip(saved['odd_lifts'], quotient['odd_subgroup']):
        pair = tuple(row['pair'])
        assert pair == tuple(old['pair']) and pair not in odd
        assert row['word'] == old['word'] and row['xi_image'] == old['image']
        word = decode_word(row['word'])
        projected, omega = word_image(word)
        assert xi_pack(projected) == row['xi_image']
        assert B.encode(omega) == row['omega']
        odd[pair] = dict(word=word, xi=projected, omega=omega)
    assert sorted(odd) == [(a, b) for a in range(15) for b in range(3)]
    assert odd[(0, 0)]['word'] == {} and odd[(0, 0)]['omega'] == B.one
    # NO assumption that the Omega component of a chosen odd lift has odd order.
    pivots = {}
    assert len(saved['principal_lifts']) == len(quotient['principal_basis']) == 92
    for row, old in zip(saved['principal_lifts'], quotient['principal_basis']):
        pos = row['position']
        assert pos == old['position'] and pos not in pivots
        assert row['word'] == old['word'] and row['xi_image'] == old['element']
        assert row['later_square_positions'] == old['square_reduction']['used_positions']
        word = decode_word(row['word'])
        projected, omega = word_image(word)
        assert xi_pack(projected) == row['xi_image'] and xi_leading(projected) == pos
        assert B.encode(omega) == row['omega']
        pivots[pos] = dict(word=word, xi=projected, omega=omega,
                           later=row['later_square_positions'], inverse=xi.power(projected, 479))
    assert list(pivots) == sorted(pivots)
    print('all45 odd and92 principal literal lifts checked', flush=True)

    field15, field3 = BinaryRing(25), BinaryRing(7)
    log15 = {field15.power(2, i): i for i in range(15)}
    log3 = {field3.power(2, i): i for i in range(3)}

    def section(value):
        assert binary_remainder(value[1], 3) == 1
        pair = (log15[field15.reduce(value[0])], log3[field3.reduce(value[2])])
        work = xi.power(value, 225)
        used = []
        while work != xi.one:
            pos = xi_leading(work)
            assert pos in pivots
            work = xi.multiply(work, pivots[pos]['inverse'])
            used.append(pos)
            assert work == xi.one or xi_leading(work) > pos
        word = dict(odd[pair]['word'])
        omega = odd[pair]['omega']
        projected = odd[pair]['xi']
        for pos in used:
            word = add_word(word, pivots[pos]['word'])
            omega = B.multiply(omega, pivots[pos]['omega'])
            projected = xi.multiply(projected, pivots[pos]['xi'])
        assert projected == value
        return pair, used, word, omega

    assert saved['relation_counts'] == dict(generator=4193, square=92, odd=2025)
    assert len(saved['relations']) == 6310
    relation_words, vectors, checked_relations = [], [], []

    def check_relation(recipe, word, projected, omega):
        index = len(vectors)
        row = saved['relations'][index]
        assert row['index'] == index and row['recipe'] == recipe
        assert projected == xi.one
        vector = B.half(omega)
        assert B.encode(omega) == row['omega'] and vector == row['vector']
        assert vector.bit_length() <= 112
        relation_words.append(word)
        vectors.append(vector)
        checked_relations.append(dict(index=index, recipe=recipe, vector=vector,
                                      omega=B.encode(omega)))

    for index, value in enumerate(xis):
        pair, positions, word, omega = section(value)
        relation_word = add_word({index: 1}, word, -1)
        result = B.multiply(omegas[index], B.inverse(omega))
        projected = xi.multiply(value, xi.power(odd[pair]['xi'], 479))
        for pos in positions:
            projected = xi.multiply(projected, pivots[pos]['inverse'])
        check_relation(dict(kind='generator', generator=index, odd_pair=list(pair),
                            positions=positions), relation_word, projected, result)
    for pos, pivot in sorted(pivots.items()):
        word = add_word({}, pivot['word'], 2)
        projected = xi.power(pivot['xi'], 2)
        omega = B.power(pivot['omega'], 2)
        for later in pivot['later']:
            assert later > pos
            word = add_word(word, pivots[later]['word'], -1)
            projected = xi.multiply(projected, pivots[later]['inverse'])
            omega = B.multiply(omega, B.inverse(pivots[later]['omega']))
        check_relation(dict(kind='square', position=pos, later_positions=pivot['later']),
                       word, projected, omega)
    for a, oa in sorted(odd.items()):
        for b, ob in sorted(odd.items()):
            c = ((a[0]+b[0]) % 15, (a[1]+b[1]) % 3)
            oc = odd[c]
            word = add_word(oa['word'], ob['word'])
            word = add_word(word, oc['word'], -1)
            projected = xi.multiply(xi.multiply(oa['xi'], ob['xi']), xi.power(oc['xi'], 479))
            omega = B.multiply(B.multiply(oa['omega'], ob['omega']), B.inverse(oc['omega']))
            check_relation(dict(kind='odd', a=list(a), b=list(b), c=list(c)), word, projected, omega)
    assert len(vectors) == 6310
    print('all6310 mixed-characteristic relation identities checked', flush=True)

    basis = {}
    positions = [row['position'] for row in saved['additive_basis']]
    assert positions == sorted(set(positions)) and len(positions) <= 112
    for row in saved['additive_basis']:
        pos, vector = row['position'], row['vector']
        assert vector and (vector & -vector).bit_length()-1 == pos
        seed = row['seed_relation']
        assert 0 <= seed < 6310
        rebuilt = vectors[seed]
        word = dict(relation_words[seed])
        used = row['construction_positions']
        assert used == sorted(set(used))
        for oldpos in used:
            assert oldpos < pos and oldpos in basis
            assert basis[oldpos]['seed'] < seed
            rebuilt ^= basis[oldpos]['vector']
            word = add_word(word, basis[oldpos]['word'])
        assert rebuilt == vector and encode_word(word) == row['word']
        decode_word(row['word'])
        projected, omega = word_image(word)
        assert projected == xi.one and B.encode(omega) == [1, vector]
        costs = actual_costs(word, labels)
        assert costs == row['costs']
        basis[pos] = dict(vector=vector, word=word, seed=seed, costs=costs)
    assert saved['additive_rank'] == len(basis)

    def reduce_vector(value):
        used = []
        while value:
            pos = (value & -value).bit_length()-1
            if pos not in basis:
                break
            value ^= basis[pos]['vector']
            used.append(pos)
            assert not value or (value & -value).bit_length()-1 > pos
        return dict(remainder=value, used_positions=used,
                    first_missing_position=((value & -value).bit_length()-1 if value else None))

    for index, vector in enumerate(vectors):
        reduced = reduce_vector(vector)
        assert reduced == saved['relations'][index]['linear_reduction']
        assert reduced['remainder'] == 0
        checked_relations[index]['linear_reduction'] = reduced
    # Both inclusions: every basis vector is a relation combination above;
    # every one of ALL6310 relation vectors reduces into this independent basis.
    assert saved['quotient_image_order'] == quotient['subgroup_order']
    assert saved['joint_image_order'] == quotient['subgroup_order']*(1 << len(basis))
    print('complete relation span and every positive basis word/cost checked', flush=True)

    decision = saved['target_decision']
    target = target_data['target']
    assert target == decision['target'] and target.bit_length() <= 112
    reduced = reduce_vector(target)
    assert reduced == decision['reduction']
    word = {}
    for pos in reduced['used_positions']:
        word = add_word(word, basis[pos]['word'])
    assert encode_word(word) == decision['normalization_word']
    normalized = target ^ reduced['remainder']
    assert normalized == decision['normalization_vector']
    projected, omega = word_image(word)
    assert projected == xi.one and B.encode(omega) == [1, normalized]
    member = reduced['remainder'] == 0
    assert decision['target_member'] == member
    if member:
        assert decision['word'] == encode_word(word)
        assert decision['costs'] == actual_costs(word, labels)
    else:
        assert decision['word'] is None and decision['costs'] is None
    assert saved['all6310_relations_complete_before_target']
    assert saved['all_relation_reductions_zero']
    assert saved['all_basis_positive_words_and_costs_checked']
    result = dict(scope='ALL4193 actual joint labels, ALL6310 relations, ONE exact full112-bit target',
        faithful_mixed_Laurent_modulus='Phi960 over Z/4', mixed_Laurent_degree=256,
        faithful_Xi_Laurent_moduli=['Phi15^16', 'Phi3^24', 'Phi5^12'],
        faithful_Xi_Laurent_degrees=[128, 48, 48],
        verified_generator_count=4193, verified_images=verified_images,
        verified_old_Xi_projections=4192, verified_added_B481_joint_image=True,
        verified_literal_odd_lifts=45, verified_literal_principal_lifts=92,
        relation_counts=dict(generator=4193, square=92, odd=2025),
        verified_relations=checked_relations, verified_all_relation_count=6310,
        additive_rank=len(basis), verified_basis_positive_words=len(basis),
        verified_basis_complete_factor_costs=True,
        both_relation_span_inclusions_checked=True,
        quotient_image_order=quotient['subgroup_order'],
        joint_image_order=saved['joint_image_order'],
        independently_recomputed_target_data=target_data,
        target_decision=dict(target=target, target_member=member, reduction=reduced,
                             normalization_word=encode_word(word),
                             positive_word_checked=member,
                             positive_word_costs=(decision['costs'] if member else None)),
        arithmetic='faithful modulo-four Laurent reconstruction; ordinary coefficient-list convolution/monic division; independent SymPy target divisions',
        sympy_version=sp.__version__, author_self_check=True, independent_review=False,
        no_new_original_residual_probe=True, no_other_target_or_profile=True,
        no_word_optimization=True, no_full_large_polynomial_expansion=True)
    temporary = output/'full_eighth_kernel_image_verification.json.partial'
    temporary.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    temporary.replace(output/'full_eighth_kernel_image_verification.json')
    print(json.dumps(dict(verified_generator_count=4193, verified_relation_count=6310,
        additive_rank=len(basis), target=target, target_member=member,
        target_remainder=reduced['remainder'], joint_image_order=saved['joint_image_order'],
        positive_word_costs=(None if not member else {k: v for k, v in decision['costs'].items()
            if k not in ('terms', 'complete_trace_factors', 'complete_reciprocal_factors')}))), flush=True)


if __name__ == '__main__':
    main()
