"""Check the combined coprime-fifteen certificate with dense/Laurent arithmetic.

This is a second implementation by the same author, not independent agent review.
It does not import main.py or reproduce its subgroup-insertion algorithm.
"""

import json
from pathlib import Path


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def decode(a):
    return [(a >> i) & 1 for i in range(a.bit_length())]


def encode(a):
    return sum(v << i for i, v in enumerate(a))


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] ^= v
    for i, v in enumerate(b):
        c[i] ^= v
    return trim(c)


def divide(a, b):
    a = trim(a)
    q = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        j = len(a) - len(b)
        q[j] = 1
        for k, v in enumerate(b):
            a[j + k] ^= v
        a = trim(a)
    return trim(q), a


def multiply(a, b, modulus=None):
    c = [0] * max(0, len(a) + len(b) - 1)
    for i, v in enumerate(a):
        if v:
            for j, w in enumerate(b):
                c[i + j] ^= w
    c = trim(c)
    return divide(c, modulus)[1] if modulus else c


def powmod(a, n, modulus=None):
    c = [1]
    while n:
        if n % 2:
            c = multiply(c, a, modulus)
        n //= 2
        a = multiply(a, a, modulus)
    return c


def inv(a, modulus):
    # Extended Euclid, separate from main.py's finite exponent inverse.
    old_r, r, old_s, s = modulus, a, [], [1]
    while r:
        q, new_r = divide(old_r, r)
        old_r, r = r, new_r
        old_s, s = s, add(old_s, multiply(q, s))
    assert old_r == [1]
    result = divide(old_s, modulus)[1]
    assert multiply(a, result, modulus) == [1]
    return result


def deriv(a):
    return trim([a[j + 1] if j % 2 == 0 else 0 for j in range(max(0, len(a) - 1))])


def whole_trace(n):
    # Invert the symmetric Laurent expression sum(z^j,-d<=j<=d).
    d = (n - 1) // 2
    remainder = [1] * (d + 1)
    result = [0] * (d + 1)
    for k in range(d, -1, -1):
        if remainder[k]:
            result[k] = 1
            for j in range(k // 2 + 1):
                if j & k == j:
                    remainder[k - 2 * j] ^= 1
    assert not any(remainder)
    return trim(result)



PHI = [1, 1, 1]
M16 = powmod(PHI, 16)
MODULUS = [0] * 8 + M16


def first_bit(value):
    low = add(value[:8], [1])
    if low:
        assert not low[0]
        return next(i - 1 for i in range(1, len(low)) if low[i])
    a = add(divide(value, M16)[1], [1])
    j = 0
    while a:
        a, digit = divide(a, PHI)
        if digit:
            assert j > 0
            return 7 + 2 * (j - 1) + (0 if digit[0] else 1)
        j += 1
    return None


def expression(e, gs):
    result = [1]
    for exponent, g in zip(e, gs):
        assert 0 <= exponent < 48
        result = multiply(result, powmod(g, exponent, MODULUS), MODULUS)
    return result


def member(value, group):
    t = decode(group['teichmuller'])
    residue = divide(value, PHI)[1]
    j = next(j for j in range(3) if divide(powmod(t, j, MODULUS), PHI)[1] == residue)
    value = multiply(value, powmod(t, (-j) % 3, MODULUS), MODULUS)
    pivots = {p['bit']: decode(p['value']) for p in group['pivots']}
    steps = 0
    while first_bit(value) in pivots:
        bit = first_bit(value)
        value = multiply(value, inv(pivots[bit], MODULUS), MODULUS)
        assert first_bit(value) is None or first_bit(value) > bit
        steps += 1
        assert steps <= 37
    return first_bit(value) is None, value, first_bit(value)


def matrix_product(a, b):
    return [[add(multiply(a[i][0], b[0][j], MODULUS),
                 multiply(a[i][1], b[1][j], MODULUS)) for j in range(2)] for i in range(2)]


def matrix_power(n):
    a = [[[0, 1], [1]], [[1], []]]
    c = [[[1], []], [[], [1]]]
    while n:
        if n % 2:
            c = matrix_product(c, a)
        a = matrix_product(a, a)
        n //= 2
    return c


def main():
    home = Path(__file__).resolve().parent
    out = home.parents[2] / 'computations' / 'outputs' / home.name
    data = json.loads((out / 'certificate.json').read_text(encoding='utf-8'))
    assert encode(MODULUS) == data['M']
    assert matrix_power(80) == [[[1], []], [[], [1]]]
    assert divide(whole_trace(161), MODULUS)[1] == [1]
    rows = data['rows']
    assert [r['n'] for r in rows] == [n for n in range(1, 160, 2) if n % 5]
    gs = []
    for r in rows:
        assert r['m'] == (r['n'] if r['n'] % 3 else r['n'] + 160)
        assert r['m'] % 3 and r['m'] % 5
        a = divide(whole_trace(r['n']), MODULUS)[1]
        b = divide(whole_trace(r['m']), MODULUS)[1]
        assert a == b and encode(a) == r['value']
        assert a[0] == 1 and divide(a, PHI)[1]
        gs.append(a)
    group = data['group']
    assert [encode(g) for g in gs] == group['generators']
    teich = powmod([1, 1], 16, MODULUS)
    assert encode(teich) == group['teichmuller']
    assert trim(teich[:8]) == [1] and powmod(teich, 3, MODULUS) == [1] and teich != [1]
    assert rows[group['b3_index']]['n'] == 3
    bits = []
    for p in group['pivots']:
        value = decode(p['value'])
        assert first_bit(value) == p['bit']
        bits.append(p['bit'])
        assert expression(p['exponents'], gs) == value
        square = multiply(value, value, MODULUS)
        assert first_bit(square) is None or first_bit(square) > p['bit']
        assert member(square, group)[0]
    assert bits == sorted(set(bits)) and len(bits) <= 37
    for g in gs:
        assert member(g, group)[0]
    assert group['order'] == 3 * 2 ** len(bits)
    assert group['insertions'] <= 101
    for row in data['targets']:
        eps = row['epsilon']
        y = add([0, 0, 1], multiply(M16, [1, 0, 1, 0, 1]))
        if eps:
            y = add(y, [0] * 14 + powmod(PHI, 8))
        assert encode(y) == row['target']
        assert trim(y[:8]) == [1, 0, 0, 0, 1]
        phi_target = [0, 0, 1]
        if eps:
            phi_target = add(phi_target, [0] * 14 + powmod(PHI, 8))
        assert divide(y, M16)[1] == phi_target
        flag, residual, bit = member(y, group)
        assert flag == row['member'] and encode(residual) == row['residual']
        assert bit == row['first_missing_bit']
        reconstructed = multiply(expression(row['expression'], gs), residual, MODULUS)
        assert reconstructed == y
    assert not any(r['member'] for r in data['targets']) and data['witness'] is None
    result = {'result': 'verified', 'source_rows': len(rows),
              'matrix_period': 80, 'odd_index_period': 160, 'pivots': len(bits),
              'group_order': group['order'], 'ambient_index': data['ambient_order'] // group['order'],
              'target_membership': [r['member'] for r in data['targets']],
              'first_missing_bits': [r['first_missing_bit'] for r in data['targets']],
              'scope': 'all complete coprime-fifteen groups at the two fixed CRT targets'}
    (out / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
