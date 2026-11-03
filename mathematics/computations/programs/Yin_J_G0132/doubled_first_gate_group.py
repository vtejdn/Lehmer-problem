"""Complete64-class subgroup and one doubled target in F2[X]/f15^14.

Carries are actual ring multiplications; every principal pivot square is closed.
No actual cofactor candidates or second-residual solutions are enumerated.
"""
from pathlib import Path
from collections import deque
from math import gcd
import json
from first_gate_character import F, rawmul, remainder, multiply, power, inverse, evaluate

EXPONENT = 240


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
    value, layer = unit ^ 1, 0
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


def main():
    mod7, modulus = 1, 1
    for _ in range(7):
        mod7 = rawmul(mod7, F)
    modulus = rawmul(mod7, mod7)
    assert modulus.bit_length()-1 == 56
    cheb = [0, 2]
    for _ in range(2, 16):
        cheb.append(rawmul(2, cheb[-1]) ^ cheb[-2])
    kernels = {}
    for q in (1, 3, 5, 15):
        arg = remainder(cheb[q], modulus)
        previous, current, values = 0, arg, [1]
        for _ in range(1, 121):
            values.append(values[-1] ^ current)
            previous, current = current, multiply(arg, current, modulus) ^ previous
        kernels[q] = values
    residues = [r for r in range(1, 240) if gcd(r, 240) == 1]
    ns = [241 if r == 1 else r for r in residues]
    assert len(ns) == 64
    images = []
    for n in ns:
        a = (n-1)//2
        b1, b3, b5, b15 = [kernels[q][a] for q in (1, 3, 5, 15)]
        pi1 = multiply(power(b3, 2, modulus), inverse(b1, modulus), modulus)
        pi5 = multiply(power(b15, 2, modulus), inverse(b5, modulus), modulus)
        h = multiply(pi5, inverse(power(pi1, 5, modulus), modulus), modulus)
        assert power(h, EXPONENT, modulus) == 1
        images.append(dict(n=n, h=h, Pi_at_X=pi1, Pi_at_C5=pi5))
    hs = [row['h'] for row in images]

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
    field_log = {power(2, j, F): j for j in range(15)}
    assert len(field_log) == 15
    tau = power(2, 16, modulus)
    logs = [field_log[remainder(h, F)] for h in hs]
    target_log = field_log[remainder(target, F)]
    for h, j in zip(hs, logs):
        assert power(h, 16, modulus) == power(tau, j, modulus)
    assert power(target, 16, modulus) == power(tau, target_log, modulus)
    divisor, multiple15, bezout = 15, 1, [0]*64
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
            value = multiply(value, power(h, exponent, modulus), modulus)
        return value

    pivots = {}
    queue = deque()
    for i, h in enumerate(hs):
        word = [0]*64
        word[i] = 225
        queue.append((power(h, 225, modulus), word))
    while queue:
        element, word = queue.popleft()
        while element != 1:
            position = leading_coordinate(element)
            if position not in pivots:
                assert remainder(element, F) == 1
                assert word_product(word) == element
                pivot = dict(position=position, element=element, word=word,
                             inverse=inverse(element, modulus))
                pivots[position] = pivot
                queue.append((multiply(element, element, modulus), [(2*v) % EXPONENT for v in word]))
                break
            pivot = pivots[position]
            element = multiply(element, pivot['inverse'], modulus)
            word = [(a-b) % EXPONENT for a, b in zip(word, pivot['word'])]
            assert element == 1 or leading_coordinate(element) > position
    assert len(pivots) <= 52

    def reduce_principal(element):
        used = []
        while element != 1:
            position = leading_coordinate(element)
            if position not in pivots:
                break
            element = multiply(element, pivots[position]['inverse'], modulus)
            used.append(position)
            assert element == 1 or leading_coordinate(element) > position
        return dict(remainder=element, used_positions=used,
                    first_missing_position=leading_coordinate(element))

    generator_reductions = []
    for h in hs:
        result = reduce_principal(power(h, 225, modulus))
        assert result['remainder'] == 1
        generator_reductions.append(result)
    basis = []
    for position in sorted(pivots):
        pivot = pivots[position]
        closure = reduce_principal(multiply(pivot['element'], pivot['element'], modulus))
        assert closure['remainder'] == 1
        assert all(j > position for j in closure['used_positions'])
        basis.append({key: pivot[key] for key in ('position', 'element', 'word')} | {'square_reduction': closure})
    target_principal = power(target, 225, modulus)
    target_reduction = reduce_principal(target_principal)
    normalization_word = [0]*64
    for position in target_reduction['used_positions']:
        normalization_word = [(a+b) % EXPONENT for a, b in zip(normalization_word, pivots[position]['word'])]
    assert multiply(word_product(normalization_word), target_reduction['remainder'], modulus) == target_principal
    member = odd_member and target_reduction['remainder'] == 1
    witness = None
    if member:
        witness_word = [(a+b) % EXPONENT for a, b in zip(odd_word, normalization_word)]
        assert word_product(witness_word) == target
        cost = sum(e*5*(n-1)//2 for e, n in zip(witness_word, ns))
        witness = dict(exponents=witness_word, cofactor_degree=cost,
                       original_trace_degree=374+cost, original_reciprocal_degree=2*(374+cost),
                       first_gate_only=True, second_gate_not_tested=True)
    payload = dict(scope='all64 n classes modulo240, representative1 replaced by241; doubled F4 target only',
                   coefficient_encoding='bit i is coefficient of X^i over F2',
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
    tmp = output/'doubled_first_gate_group.json.partial'
    tmp.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    tmp.replace(output/'doubled_first_gate_group.json')
    print(json.dumps({key: payload[key] for key in ('old_target', 'target', 'principal_rank',
                     'odd_subgroup_order', 'subgroup_order', 'target_member',
                     'target_principal_reduction', 'witness')}))


if __name__ == '__main__':
    main()
