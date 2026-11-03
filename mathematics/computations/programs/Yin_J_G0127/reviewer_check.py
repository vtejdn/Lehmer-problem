"""Independent review of exactly J127's two fixed squaring targets.

Exponent-set arithmetic is reviewer-authored and imports no contributor code.
The unchanged full group theorem and J126 source reconstruction are accepted
at R987v2's exact scope; only the two new targets are reduced here.
"""

import json
from pathlib import Path


ONE = frozenset({0})
ZERO = frozenset()
PHI = frozenset({0, 1, 2})


def decode(n):
    assert isinstance(n, int) and n >= 0
    return frozenset(i for i in range(n.bit_length()) if (n >> i) & 1)


def encode(a):
    return sum(1 << i for i in a)


def times(a, b):
    answer = set()
    for i in a:
        for j in b:
            if i+j in answer:
                answer.remove(i+j)
            else:
                answer.add(i+j)
    return frozenset(answer)


def divide(a, b):
    assert b
    quotient, remainder = set(), set(a)
    while remainder and max(remainder) >= max(b):
        shift = max(remainder) - max(b)
        quotient.add(shift)
        remainder.symmetric_difference_update(shift+j for j in b)
    return frozenset(quotient), frozenset(remainder)


def rem(a, b):
    return divide(a, b)[1]


def power(a, n, modulus=None):
    answer = ONE
    while n:
        if n & 1:
            answer = times(answer, a)
            if modulus:
                answer = rem(answer, modulus)
        n //= 2
        a = frozenset(2*j for j in a)
        if modulus:
            a = rem(a, modulus)
    return answer


PHI16 = power(PHI, 16)
MODULUS = times(frozenset({8}), PHI16)


def multiply(a, b):
    return rem(times(a, b), MODULUS)


def inverse(a):
    old_r, r, old_s, s = MODULUS, a, ZERO, ONE
    while r:
        q, remainder = divide(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s ^ times(q, s)
    assert old_r == ONE
    answer = rem(old_s, MODULUS)
    assert multiply(a, answer) == ONE
    return answer


def leading(a):
    assert rem(a, PHI) == ONE and 0 in a
    low = frozenset(j for j in a ^ ONE if j < 8)
    if low:
        return min(low)-1
    principal, j = rem(a, PHI16) ^ ONE, 0
    while principal:
        principal, digit = divide(principal, PHI)
        if digit:
            assert j > 0
            return 7 + 2*(j-1) + min(digit)
        j += 1
    return None


def main():
    home = Path(__file__).resolve().parent
    outputs = home.parents[2] / 'computations' / 'outputs'
    fixed_path = outputs / 'Yin_J_G0126' / 'certificate.json'
    fixed = json.loads(fixed_path.read_text(encoding='utf-8'))
    certificate = json.loads((outputs / home.name / 'certificate.json').read_text(encoding='utf-8'))
    assert certificate['fixed_input'] == 'mathematics/computations/outputs/Yin_J_G0126/certificate.json'
    assert fixed['M'] == certificate['modulus'] == encode(MODULUS)
    assert certificate['tested_powers'] == [2, 4]
    rows = certificate['results']
    assert len(rows) == 2 and [r['power'] for r in rows] == [2, 4]
    base = frozenset({2}) ^ times(PHI16, frozenset({0, 2, 4}))
    assert encode(base) == certificate['base_target'] == fixed['targets'][0]['target'] == 0x1500150011
    group = fixed['group']
    gs = [decode(row['value']) for row in fixed['rows']]
    assert len(gs) == 96 and [encode(g) for g in gs] == group['generators']
    assert group['modulus'] == encode(MODULUS) and group['order'] == 3*2**34
    bits = [p['bit'] for p in group['pivots']]
    assert bits == [bit for bit in range(37) if bit not in (12, 20, 36)]
    pivots = {p['bit']: p for p in group['pivots']}
    b3 = group['b3_index']
    assert fixed['rows'][b3]['n'] == 3 and gs[b3] == frozenset({0, 1})
    t = power(gs[b3], 16, MODULUS)
    assert encode(t) == group['teichmuller'] and power(t, 3, MODULUS) == ONE
    tpowers = [power(t, j, MODULUS) for j in range(3)]
    residues = [rem(v, PHI) for v in tpowers]
    assert len(set(residues)) == 3

    def expression(exponents):
        assert len(exponents) == 96
        result = ONE
        for g, e in zip(gs, exponents):
            assert isinstance(e, int) and 0 <= e < 48
            result = multiply(result, power(g, e, MODULUS))
        return result

    used = set()
    results = []
    for row in rows:
        exponent = row['power']
        phi_target = frozenset({2*exponent})
        low_part = frozenset(j for j in phi_target if j < 8)
        crt_target = phi_target ^ times(PHI16, ONE ^ low_part)
        target = power(base, exponent, MODULUS)
        assert target == crt_target and encode(target) == row['target']
        assert frozenset(j for j in target if j < 8) == ONE
        assert rem(target, PHI16) == phi_target
        residue_power = residues.index(rem(target, PHI))
        reduced = multiply(target, tpowers[(-residue_power) % 3])
        trace = []
        while (bit := leading(reduced)) is not None and bit in pivots:
            pivot = pivots[bit]
            pivot_value = decode(pivot['value'])
            if bit not in used:
                assert expression(pivot['exponents']) == pivot_value
                assert leading(pivot_value) == bit
                used.add(bit)
            trace.append(bit)
            reduced = multiply(reduced, inverse(pivot_value))
            next_bit = leading(reduced)
            assert next_bit is None or next_bit > bit
            assert len(trace) <= 37
        assert trace == row['trace'] == sorted(set(trace))
        assert encode(reduced) == row['residual'] and leading(reduced) == row['first_missing_bit']
        assert multiply(expression(row['expression']), reduced) == target
        assert row['member'] == (reduced == ONE)
        if exponent == 2:
            assert encode(target) == 0x1100110001
            assert encode(reduced) == 0xb6dbdb6d01 and leading(reduced) == 36
            assert len(trace) == 10 and row['member'] is False
        else:
            assert encode(target) == 0x100010101 and reduced == ONE
            assert len(trace) == 4 and row['member'] is True
        results.append({'power': exponent, 'target': hex(encode(target)),
                        'member': row['member'], 'residual': hex(encode(reduced)),
                        'first_missing_bit': leading(reduced), 'trace': trace,
                        'crt_and_full_96_factor_product': 'verified'})
    assert len(used) == 12
    output = {'verified': True, 'scope': 'Exactly powers 2 and 4 of the fixed J126 base target',
              'results': results, 'used_pivot_expressions': sorted(used),
              'total_cancellations': sum(len(r['trace']) for r in results),
              'quotient_class_order': 4,
              'accepted_input': 'Unchanged C643v2/J126 complete group theorem, previously reviewed in R987v2',
              'limits': 'No new group construction, source scan, quotient, or original-input witness.'}
    (outputs / home.name / 'reviewer_verification.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
