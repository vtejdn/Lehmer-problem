"""Independent review of exactly J128's three declared CRT targets.

Reviewer-authored exponent-set arithmetic is adapted from the reviewer's J127
checker, with no contributor-code imports.  The fixed C643v2/J126 group theorem
is accepted at R987v2's exact scope; no group construction or source scan runs.
"""

import json
from pathlib import Path


ONE = frozenset({0})
ZERO = frozenset()
X = frozenset({1})
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


X8 = frozenset({8})
PHI16 = power(PHI, 16)
MODULUS = times(X8, PHI16)


def multiply(a, b):
    return rem(times(a, b), MODULUS)


def inverse(a, modulus=MODULUS):
    old_r, r, old_s, s = modulus, a, ZERO, ONE
    while r:
        q, remainder = divide(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s ^ times(q, s)
    assert old_r == ONE
    answer = rem(old_s, modulus)
    assert rem(times(a, answer), modulus) == ONE
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
    parameters = [(0, 1), (1, 0), (1, 1)]
    assert certificate['parameters'] == [list(p) for p in parameters]
    rows = certificate['results']
    assert len(rows) == 3 and [(r['u'], r['v']) for r in rows] == parameters
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

    expected = [(0x101104001, 0x34cf799601, 20, 5),
                (0x5000fc005, 1, None, 18),
                (0x15010ec015, 0xb6dbdb6d01, 36, 22)]
    chi = times(X, power(PHI, 2))
    assert chi == frozenset({1, 3, 5})
    used, results = set(), []
    for row, (u, v), (expected_target, expected_residual, expected_bit, expected_steps) in zip(rows, parameters, expected):
        hx = ONE ^ (X if u else ZERO) ^ (power(X, 2) if v else ZERO)
        hc = ONE ^ (chi if u else ZERO) ^ (power(chi, 2) if v else ZERO)
        low = rem(times(ONE ^ power(X, 4), inverse(power(hx, 2), X8)), X8)
        primary = rem(times(power(X, 14), power(inverse(hc, PHI16), 7, PHI16)), PHI16)
        target = primary ^ times(PHI16, low ^ rem(primary, X8))
        assert max(target) < 40 and rem(target, X8) == low and rem(target, PHI16) == primary
        assert encode(low) == row['low_X'] and encode(primary) == row['phi_primary']
        assert encode(target) == row['target'] == expected_target
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
        assert len(trace) == expected_steps
        assert encode(reduced) == row['residual'] == expected_residual
        assert leading(reduced) == row['first_missing_bit'] == expected_bit
        assert multiply(expression(row['expression']), reduced) == target
        assert row['member'] == (reduced == ONE)
        results.append({'u': u, 'v': v, 'target': hex(encode(target)),
                        'member': row['member'], 'residual': hex(encode(reduced)),
                        'first_missing_bit': leading(reduced), 'trace': trace,
                        'crt_and_full_96_factor_product': 'verified'})
    assert len(used) == 28
    output = {'verified': True, 'scope': 'Exactly J128 parameters (0,1), (1,0), (1,1) in X^8 phi^16',
              'results': results, 'used_pivot_expressions': sorted(used),
              'total_cancellations': sum(len(r['trace']) for r in results),
              'accepted_input': 'Unchanged C643v2/J126 complete group theorem, previously reviewed in R987v2',
              'limits': 'No fourth native target, ratio test, new group construction, source scan, enlarged modulus, or original-input witness.'}
    (outputs / home.name).mkdir(parents=True, exist_ok=True)
    (outputs / home.name / 'reviewer_verification.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
