"""Complete256 B/Gamma NECESSARY joint-filter subgroup, not the cubic gate.

Carries are actual ring multiplications; every principal pivot square is closed.
No actual cofactor candidates or second-residual solutions are enumerated.
"""
from pathlib import Path
from collections import deque
from math import gcd
import json
from first_gate_character import F, rawmul, remainder, multiply, power, inverse, evaluate, derivative

EXPONENT = 240
UNIT_BITS = 56
UNIT_MASK = (1 << UNIT_BITS)-1


def gmultiply(a, b, modulus):
    unit = multiply(a & UNIT_MASK, b & UNIT_MASK, modulus)
    return unit | (((a >> UNIT_BITS) ^ (b >> UNIT_BITS)) << UNIT_BITS)


def gpower(a, exponent, modulus):
    unit = power(a & UNIT_MASK, exponent, modulus)
    return unit | ((a >> UNIT_BITS) << UNIT_BITS if exponent % 2 else 0)


def ginverse(a, modulus):
    return inverse(a & UNIT_MASK, modulus) | ((a >> UNIT_BITS) << UNIT_BITS)



def divide(a, b):
    quotient = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length()-b.bit_length()
        quotient ^= 1 << shift
        a ^= b << shift
    return quotient, a


def leading_coordinate(unit):
    if unit == 1:
        return None
    if (unit & UNIT_MASK) == 1:
        additive = unit >> UNIT_BITS
        return 52+(additive & -additive).bit_length()-1
    value, layer = (unit & UNIT_MASK) ^ 1, 0
    while True:
        quotient, coefficient = divide(value, F)
        if coefficient:
            break
        value, layer = quotient, layer+1
    assert 1 <= layer <= 13
    bit = (coefficient & -coefficient).bit_length()-1
    return 4*(layer-1)+bit


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x-(a//b)*y


def totient(n):
    value, remaining, divisor = n, n, 2
    while divisor*divisor <= remaining:
        if remaining % divisor == 0:
            value -= value//divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        value -= value//remaining
    return value


def main():
    mod7, modulus = 1, 1
    for _ in range(7):
        mod7 = rawmul(mod7, F)
    modulus = rawmul(mod7, mod7)
    assert modulus.bit_length()-1 == 56
    mod24 = 1
    for _ in range(24):
        mod24 = rawmul(mod24, F)
    assert mod24.bit_length()-1 == 96
    cheb = [0, 2]
    for _ in range(2, 16):
        cheb.append(rawmul(2, cheb[-1]) ^ cheb[-2])
    kernels = {}
    for q in (1, 3, 5, 15):
        arg = remainder(cheb[q], modulus)
        previous, current, values = 0, arg, [1]
        for _ in range(1, 241):
            values.append(values[-1] ^ current)
            previous, current = current, multiply(arg, current, modulus) ^ previous
        kernels[q] = values
    kernel24 = {}
    for q in (5, 15):
        argument = remainder(cheb[q], mod24)
        previous, current, values = 0, argument, [1]
        for _ in range(1, 241):
            values.append(values[-1] ^ current)
            previous, current = current, multiply(argument, current, mod24) ^ previous
        kernel24[q] = values
    residues = [r for r in range(1, 480) if gcd(r, 480) == 1]
    ns = [481 if r == 1 else r for r in residues]
    assert len(ns) == 128
    images = []
    for n in ns:
        a = (n-1)//2
        b1, b3, b5, b15 = [kernels[q][a] for q in (1, 3, 5, 15)]
        hb = multiply(b5, inverse(power(b1, 5, modulus), modulus), modulus)
        hg = multiply(b15, inverse(power(b3, 5, modulus), modulus), modulus)
        for family, at_x, at_c5, image, weight in (
                ('B', b1, b5, hb, 1), ('Gamma', b3, b15, hg, 3)):
            q5 = kernel24[5 if family == 'B' else 15][a]
            dlog = multiply(derivative(q5), inverse(q5, mod24), mod24)
            pair = image | (dlog << UNIT_BITS)
            assert gpower(pair, EXPONENT, modulus) == 1
            images.append(dict(family=family, n=n, h=pair, L=image, Dlog_Q5=dlog,
                               at_X=at_x, at_C5=at_c5, at_C5_R24=q5,
                               trace_degree=weight*(n-1)//2))
    hs = [row['h'] for row in images]
    word_length = len(hs)
    assert word_length == 256

    # Recompute the actual old target formula at its exact R7 precision.
    x, phi, f9, chi = 2, 7, 11, cheb[5]
    delta = remainder((1 << 56) ^ (1 << 24), mod7)
    d = remainder((1 << 12) ^ (1 << 28), mod7)
    h0 = power(x, 2, mod7)
    for factor, exponent in [(x ^ 1, 2), (phi, 3), (f9, 4), (remainder(kernels[1][93], mod7), 1)]:
        h0 = multiply(h0, power(factor, exponent, mod7), mod7)
    gamma = power(x ^ 1, 2, mod7)
    for factor, exponent in [(chi, 2), (evaluate(F, chi, mod7), 18),
                             (evaluate(phi, chi, mod7), 3), (evaluate(f9, chi, mod7), 4),
                             (remainder(kernels[5][93], mod7), 1)]:
        gamma = multiply(gamma, power(factor, exponent, mod7), mod7)
    t = multiply(h0, delta, mod7)
    old_target = multiply(multiply(d, power(t, 5, mod7), mod7), inverse(gamma, mod7), mod7)
    target = power(old_target, 2, modulus)
    assert power(target, EXPONENT, modulus) == 1

    # Odd projection, in the cyclic order15 residue field, with a Bezout word.
    field_log = {gpower(2, j, F): j for j in range(15)}
    assert len(field_log) == 15
    tau = gpower(2, 16, modulus)
    logs = [field_log[remainder(h & UNIT_MASK, F)] for h in hs]
    target_log = field_log[remainder(target, F)]
    for h, j in zip(hs, logs):
        assert gpower(h, 16, modulus) == gpower(tau, j, modulus)
    assert gpower(target, 16, modulus) == gpower(tau, target_log, modulus)
    divisor, multiple15, bezout = 15, 1, [0]*word_length
    for i, value in enumerate(logs):
        g, a, b = egcd(divisor, value)
        multiple15 *= a
        bezout = [a*v for v in bezout]
        bezout[i] += b
        divisor = g
    assert 15*multiple15+sum(a*b for a, b in zip(logs, bezout)) == divisor
    odd_member = target_log % divisor == 0
    odd_word = [16*(target_log//divisor)*v % EXPONENT for v in bezout] if odd_member else None

    def word_product(word):
        value = 1
        for h, exponent in zip(hs, word):
            value = gmultiply(value, gpower(h, exponent, modulus), modulus)
        return value

    pivots = {}
    queue = deque()
    for i, h in enumerate(hs):
        word = [0]*word_length
        word[i] = 225
        queue.append((gpower(h, 225, modulus), word))
    while queue:
        element, word = queue.popleft()
        while element != 1:
            position = leading_coordinate(element)
            if position not in pivots:
                assert remainder(element & UNIT_MASK, F) == 1
                assert word_product(word) == element
                pivot = dict(position=position, element=element, word=word,
                             inverse=ginverse(element, modulus))
                pivots[position] = pivot
                queue.append((gmultiply(element, element, modulus), [(2*v) % EXPONENT for v in word]))
                break
            pivot = pivots[position]
            element = gmultiply(element, pivot['inverse'], modulus)
            word = [(a-b) % EXPONENT for a, b in zip(word, pivot['word'])]
            assert element == 1 or leading_coordinate(element) > position
    assert len(pivots) <= 100

    def reduce_principal(element):
        used = []
        while element != 1:
            position = leading_coordinate(element)
            if position not in pivots:
                break
            element = gmultiply(element, pivots[position]['inverse'], modulus)
            used.append(position)
            assert element == 1 or leading_coordinate(element) > position
        return dict(remainder=element, used_positions=used,
                    first_missing_position=leading_coordinate(element))

    generator_reductions = []
    for h in hs:
        result = reduce_principal(gpower(h, 225, modulus))
        assert result['remainder'] == 1
        generator_reductions.append(result)
    basis = []
    for position in sorted(pivots):
        pivot = pivots[position]
        closure = reduce_principal(gmultiply(pivot['element'], pivot['element'], modulus))
        assert closure['remainder'] == 1
        assert all(j > position for j in closure['used_positions'])
        basis.append({key: pivot[key] for key in ('position', 'element', 'word')} | {'square_reduction': closure})
    target_principal = gpower(target, 225, modulus)
    target_reduction = reduce_principal(target_principal)
    normalization_word = [0]*word_length
    for position in target_reduction['used_positions']:
        normalization_word = [(a+b) % EXPONENT for a, b in zip(normalization_word, pivots[position]['word'])]
    assert gmultiply(word_product(normalization_word), target_reduction['remainder'], modulus) == target_principal
    member = odd_member and target_reduction['remainder'] == 1
    witness = None
    if member:
        witness_word = [(a+b) % EXPONENT for a, b in zip(odd_word, normalization_word)]
        assert word_product(witness_word) == target
        cost = sum(e*row['trace_degree'] for e, row in zip(witness_word, images))
        terms = [dict(family=row['family'], n=row['n'], exponent=e,
                      degree_contribution=e*row['trace_degree'])
                 for e, row in zip(witness_word, images) if e]
        counts = {}
        for row in terms:
            for r in range(2, row['n']+1):
                if row['n'] % r == 0:
                    counts[r] = counts.get(r, 0)+row['exponent']
                    if row['family'] == 'Gamma':
                        counts[3*r] = counts.get(3*r, 0)+row['exponent']
        assert cost == sum(e*totient(r)//2 for r, e in counts.items())
        full_counts = {3:4, 5:6, 9:8, 15:4, 960:1, 11:2, 17:2, 187:2}
        for r, e in counts.items():
            full_counts[r] = full_counts.get(r, 0)+e
        assert 374+cost == 4+sum(e*totient(r)//2 for r, e in full_counts.items())
        reciprocal_counts = {1:8, **full_counts}
        assert 2*(374+cost) == sum(e*totient(r) for r, e in reciprocal_counts.items())
        binary_exponents = {}
        endpoint_exponent = reciprocal_counts[1]//2
        for order, multiplicity in full_counts.items():
            odd_order, dyadic = order, 0
            while odd_order % 2 == 0:
                odd_order //= 2
                dyadic += 1
            assert odd_order > 1
            weight = 1 if dyadic == 0 else 2**(dyadic-1)
            binary_exponents[odd_order] = binary_exponents.get(odd_order, 0)+weight*multiplicity
        q_binary = 1
        values = [endpoint_exponent]+list(binary_exponents.values())
        while all(value % (2*q_binary) == 0 for value in values):
            q_binary *= 2
        radical_degree = 1+sum(totient(r)//2 for r in binary_exponents)
        assert binary_exponents[15] == 36 and binary_exponents[3] == 4 and binary_exponents[5] == 6
        witness = dict(exponents=witness_word, terms=terms, cofactor_degree=cost,
                       cofactor_trace_factor_multiplicities=[dict(order=r, multiplicity=e) for r,e in sorted(counts.items())],
                       complete_reciprocal_cyclotomic_multiplicities=[dict(order=r, multiplicity=e) for r,e in sorted(reciprocal_counts.items())],
                       binary_endpoint_exponent=endpoint_exponent,
                       complete_binary_odd_order_exponents=[dict(odd_order=r, exponent=e) for r,e in sorted(binary_exponents.items())],
                       maximal_binary_Frobenius_exponent=q_binary, full_binary_radical_degree=radical_degree,
                       original_trace_degree=374+cost, original_reciprocal_degree=2*(374+cost),
                       first_gate_and_necessary_square_filter_only=True,
                       full_second_gate_not_tested=True)
    payload = dict(scope='all256 B/Gamma necessary-filter images at128 n classes modulo480, representative1 replaced by481; NO cubic equation or second-residual test',
                   generator_count=256, n_class_count=128,
                   coefficient_encoding='unit bits0..55; additive Dlog bits56..151, each polynomial little-endian over F2',
                   unit_bits=56, additive_modulus=mod24, additive_degree=96,
                   principal_coordinate_order='52 f-adic unit coordinates then96 raw additive coefficient bits',
                   f=F, modulus=modulus, quotient_degree=56, group_exponent=240,
                   generators=images, old_target=old_target, target=target,
                   odd_part=dict(logs=logs, target_log=target_log, gcd_with15=divisor,
                                 bezout_multiple15=multiple15, bezout_coefficients=bezout,
                                 target_member=odd_member, target_word=odd_word),
                   principal_basis=basis, generator_principal_reductions=generator_reductions,
                   target_principal=target_principal, target_principal_reduction=target_reduction,
                   target_normalization_word=normalization_word,
                   principal_rank=len(basis), odd_subgroup_order=15//divisor,
                   subgroup_order=(15//divisor)*(1 << len(basis)),
                   target_member=member, witness=witness,
                   no_actual_candidate_or_second_gate_enumeration=True)
    here = Path(__file__).resolve().parent
    output = here.parents[3]/'mathematics/computations/outputs'/here.name
    output.mkdir(parents=True, exist_ok=True)
    tmp = output/'joint_necessary_filter_group.json.partial'
    tmp.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'joint_necessary_filter_group.json')
    summary = {key: payload[key] for key in ('old_target', 'target', 'principal_rank',
                     'odd_subgroup_order', 'subgroup_order', 'target_member',
                     'target_principal_reduction')}
    summary['witness_degree_summary'] = ({key: witness[key] for key in
        ('cofactor_degree', 'original_trace_degree', 'original_reciprocal_degree')} if witness else None)
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
