"""Isolated review of C638's fixed finite evidence; no author-code imports.

Run after main.py from any working directory.
Sparse exponent sets implement F_2[X]; full B_n is 1+sum C_j where
C_j(z+z^-1)=z^j+z^-j.  The checker validates supplied certificates,
not a fresh subgroup search.  Its report stays in this J's output home.
"""

import json
import math
import re
from functools import lru_cache
from pathlib import Path

ONE = frozenset({0})
X = frozenset({1})
PHI = frozenset({0, 1, 2})


def decode(n):
    return frozenset(i for i in range(n.bit_length()) if n & (1 << i))


def encode(p):
    return sum(1 << i for i in p)


def div(a, b):
    q, r = set(), set(a)
    while r and max(r) >= max(b):
        shift = max(r) - max(b)
        q.symmetric_difference_update({shift})
        r.symmetric_difference_update({i + shift for i in b})
    return frozenset(q), frozenset(r)


def mul(a, b, modulus=None):
    c = set()
    for i in a:
        c.symmetric_difference_update({i + j for j in b})
    result = frozenset(c)
    return div(result, modulus)[1] if modulus else result


def power(a, n, modulus=None):
    result = ONE
    for bit in bin(n)[2:]:
        result = mul(result, result, modulus)
        if bit == '1':
            result = mul(result, a, modulus)
    return result


def inverse(a, modulus):
    r0, r1, t0, t1 = modulus, a, frozenset(), ONE
    while r1:
        q, r = div(r0, r1)
        r0, r1, t0, t1 = r1, r, t1, t0 ^ mul(q, t1)
    assert r0 == ONE
    return div(t0, modulus)[1]


def derivative(a):
    return frozenset(i - 1 for i in a if i % 2)


@lru_cache(None)
def whole(n):
    assert n > 0 and n % 2
    prev, current, total = frozenset(), X, ONE
    for _ in range(1, (n + 1) // 2):
        total ^= current
        prev, current = current, mul(X, current) ^ prev
    return total


def first(a):
    value, level = a ^ ONE, 0
    while value:
        value, digit = div(value, PHI)
        if digit:
            assert level >= 1
            return 2 * (level - 1) + min(digit)
        level += 1
    return None


def expression(exponents, generators, modulus):
    assert len(exponents) == len(generators)
    result = ONE
    for e, g in zip(exponents, generators):
        assert isinstance(e, int) and 0 <= e < 48
        result = mul(result, power(g, e, modulus), modulus)
    return result


def reduce_member(value, group):
    modulus, t = decode(group['modulus']), decode(group['teichmuller'])
    value = div(value, modulus)[1]
    for exponent in range(3):
        if div(power(t, exponent, modulus), PHI)[1] == div(value, PHI)[1]:
            value = mul(value, inverse(power(t, exponent, modulus), modulus), modulus)
            break
    else:
        raise AssertionError('Nonunit')
    for pivot in group['pivots']:
        bit = first(value)
        if bit is None:
            break
        if bit == pivot['bit']:
            value = mul(value, inverse(decode(pivot['value']), modulus), modulus)
            assert first(value) is None or first(value) > bit
    return value == ONE, value


def rank(vectors):
    rows = [set(v) for v in vectors if v]
    result = 0
    for column in sorted(set().union(*rows)) if rows else []:
        pivot = next((i for i in range(result, len(rows)) if column in rows[i]), None)
        if pivot is None:
            continue
        rows[result], rows[pivot] = rows[pivot], rows[result]
        for i in range(len(rows)):
            if i != result and column in rows[i]:
                rows[i] ^= rows[result]
        result += 1
    return result


def matrix_mul(a, b):
    return [[mul(a[i][0], b[0][j]) ^ mul(a[i][1], b[1][j])
             for j in range(2)] for i in range(2)]


def main():
    home = Path(__file__).resolve().parent
    root = home.parents[3]
    output = home.parents[2] / 'computations' / 'outputs' / home.name
    data = json.loads((output / 'certificate.json').read_text(encoding='utf-8'))
    assert data['phi'] == 7
    moduli = {n: power(PHI, n) for n in (8, 16, 17, 32)}
    matrix = [[X, ONE], [ONE, frozenset()]]
    identity = [[ONE, frozenset()], [frozenset(), ONE]]
    a5 = identity
    for _ in range(5):
        a5 = matrix_mul(a5, matrix)
    for i in range(2):
        for j in range(2):
            expected = mul(PHI, mul(PHI, matrix[i][j]) ^ (X ^ ONE if i == j else frozenset()))
            assert a5[i][j] ^ identity[i][j] == expected
            assert not div(power(expected, 16), moduli[16])[1]
            assert not div(power(expected, 32), moduli[32])[1]
    a_power = a5
    for step in range(1, 6):
        a_power = matrix_mul(a_power, a_power)
        if step in (4, 5):
            modulus = moduli[16 if step == 4 else 17]
            assert [[div(a_power[i][j], modulus)[1] for j in range(2)] for i in range(2)] == identity
    rows = data['source_rows']
    labels = [('B', n) for n in range(1, 160, 2) if n % 5] + [('D', n) for n in range(5, 320, 10)]
    assert len(rows) == 96 and [(r['kind'], r['n']) for r in rows] == labels
    for row in rows:
        b = whole(row['n'])
        assert 0 in b and max(b) == (row['n'] - 1) // 2
        if row['kind'] == 'D':
            b, remainder = div(b, PHI)
            assert not remainder
        assert div(b, PHI)[1]
        assert div(b, moduli[16])[1] == decode(row['value'])
        dlog = mul(derivative(b), inverse(div(b, moduli[8])[1], moduli[8]), moduli[8])
        assert (13 in dlog) == (15 in dlog)
    assert set(data['groups']) == {'G8', 'G16', 'E8', 'E16'}
    expected = {'G8': (13, 24576), 'G16': (29, 1610612736), 'E8': (14, 49152), 'E16': (30, 3221225472)}
    for name, group in data['groups'].items():
        n = int(name[1:])
        assert group['N'] == n and group['endpoint'] == (name[0] == 'E')
        modulus = moduli[n]
        assert group['modulus'] == encode(modulus)
        gs = [div(decode(r['value']), modulus)[1] for r in rows] + ([X] if name[0] == 'E' else [])
        assert group['generators'] == [encode(g) for g in gs]
        assert [(v['kind'], v['n']) for v in group['generator_labels']] == labels + ([('X', 1)] if name[0] == 'E' else [])
        assert group['b3_index'] == labels.index(('B', 3)) and group['teichmuller_exponent'] == n
        t = power(X ^ ONE, n, modulus)
        assert encode(t) == group['teichmuller'] and t != ONE and power(t, 3, modulus) == ONE
        bits = [p['bit'] for p in group['pivots']]
        assert bits == sorted(set(bits)) and len(bits) == expected[name][0]
        assert group['order'] == expected[name][1] == 3 * 2 ** len(bits)
        for p in group['pivots']:
            value = decode(p['value'])
            assert first(value) == p['bit'] and expression(p['exponents'], gs, modulus) == value
            square = mul(value, value, modulus)
            assert first(square) is None or first(square) > p['bit']
            assert reduce_member(square, group)[0]
        assert all(reduce_member(g, group)[0] for g in gs)
        assert group['insertions'] == len(gs) + len(bits)
        assert group['cancellations'] <= group['insertions'] * 2 * (n - 1)
    assert set(data['tests']) == {'G', 'E'}
    for prefix, test in data['tests'].items():
        small, large = data['groups'][prefix + '8'], data['groups'][prefix + '16']
        vectors = [mul(derivative(decode(p['value'])), inverse(decode(p['value']), moduli[16]), moduli[16]) for p in large['pivots']]
        r = rank(vectors)
        assert r == test['dlog_rank'] == (15 if prefix == 'G' else 16)
        kernel = test['kernel_basis']
        assert len(kernel) == len(vectors) - r == rank([decode(k['word']) for k in kernel])
        for k in kernel:
            word = decode(k['word'])
            assert not word or max(word) < len(vectors)
            v, logarithm = ONE, frozenset()
            for i in word:
                v = mul(v, decode(large['pivots'][i]['value']), moduli[16])
                logarithm ^= vectors[i]
            assert not logarithm and not derivative(v) and encode(v) == k['value']
            assert expression(k['exponents'], [decode(g) for g in large['generators']], moduli[16]) == v
            root_v = frozenset(j // 2 for j in v)
            assert encode(root_v) == k['root'] and mul(root_v, root_v) == v
            flag, residual = reduce_member(root_v, small)
            assert flag == k['root_member'] and encode(residual) == k['root_residual']
            removed = expression(k['root_expression'], [decode(g) for g in small['generators']], moduli[8])
            assert mul(removed, residual, moduli[8]) == root_v
        assert test['square_intersection_order'] == 3 * 2 ** (len(vectors) - r) == 49152
        assert test['square_prior_order'] == small['order']
        assert test['quotient_order'] == 49152 // small['order']
        assert test['saturation'] == (prefix == 'E') == all(k['root_member'] for k in kernel)
        assert test['X_squared_member'] and test['X_squared_residual'] == 1
        assert expression(test['X_squared_expression'], [decode(g) for g in large['generators']], moduli[16]) == frozenset({2})
    witness = data['witness']
    mults, total, degree = {}, ONE, 0
    for row in witness['rows']:
        assert row['exponent'] > 0
        b = whole(row['n'])
        if row['kind'] == 'D':
            b, rem = div(b, PHI)
            assert not rem
        factor, e = div(b, moduli[16])[1], row['exponent']
        powered = power(factor, e, moduli[16])
        total = mul(total, powered, moduli[16])
        assert (encode(factor), encode(powered), encode(total)) == (row['factor_residue'], row['powered_residue'], row['partial_product'])
        degree += e * max(b)
        for d in range(3, row['n'] + 1, 2):
            if row['n'] % d == 0 and d != 5:
                mults[str(d)] = mults.get(str(d), 0) + e
    assert total == frozenset({2}) and degree == witness['degree'] == 2813
    assert mults == witness['complete_group_multiplicities']
    assert sum(e * sum(math.gcd(k, int(n)) == 1 for k in range(1, int(n))) // 2 for n, e in mults.items()) == degree
    assert witness['odd_complete_orders'] == sorted(int(n) for n, e in mults.items() if e % 2)
    assert witness['odd_complete_orders'] and witness['endpoint_exponent'] == 0
    assert witness['phi16_residue'] == 4 and witness['unique_phi8_root'] == 2
    assert inverse(X, moduli[8]) == frozenset({7, 15})
    assert not reduce_member(X, data['groups']['G8'])[0]
    # Read the fixed C629 table directly, without trusting its generator.
    c629 = (root / 'mathematics/claims/Yin_C_G0608_v1.md').read_text(encoding='utf-8')
    table = re.findall(r'^\| (\d+) \| (0x[0-9a-f]+) \| (0x[0-9a-f]+) \|$', c629, re.M)
    assert len(table) == 32
    old_modulus = mul(frozenset({4}), moduli[8])
    for n, b, d in table:
        bp, dp = decode(int(b, 16)), decode(int(d, 16))
        assert div(whole(int(n)), old_modulus)[1] == bp
        assert mul(bp, dp, old_modulus) == derivative(bp)
        assert (13 in dp) == (15 in dp)
    # Compare every displayed C638 pivot, product row and multiplicity.
    claim = (root / 'mathematics/claims/Yin_C_G0617_v1.md').read_text(encoding='utf-8')
    pivots = re.findall(r'^\| (\d+) \| ([0-9a-f]+|not in this precision) \| ([0-9a-f]+) \|$', claim, re.M)
    assert len(pivots) == 29
    for bit, g8, g16 in pivots:
        assert next(p['value'] for p in data['groups']['G16']['pivots'] if p['bit'] == int(bit)) == int(g16, 16)
        if g8 != 'not in this precision':
            assert next(p['value'] for p in data['groups']['G8']['pivots'] if p['bit'] == int(bit)) == int(g8, 16)
    products = re.findall(r'^\| ([BD])_(\d+) \| (\d+) \| ([0-9a-f]+) \| ([0-9a-f]+) \| ([0-9a-f]+) \|$', claim, re.M)
    assert len(products) == len(witness['rows']) == 15
    for values, row in zip(products, witness['rows']):
        kind, n, e, f, p, cumulative = values
        assert (kind, int(n), int(e), int(f, 16), int(p, 16), int(cumulative, 16)) == (row['kind'], row['n'], row['exponent'], row['factor_residue'], row['powered_residue'], row['partial_product'])
    mult_table = dict(re.findall(r'^\| (\d+) \| (\d+) \|$', claim, re.M))
    assert {n: int(e) for n, e in mult_table.items()} == mults
    result = {'result': 'verified', 'arithmetic': 'reviewer sparse exponent sets',
              'source_rows': 96, 'group_orders': {n: g['order'] for n, g in data['groups'].items()},
              'dlog_ranks': {p: t['dlog_rank'] for p, t in data['tests'].items()},
              'character_rows': 96, 'C629_rows': 32, 'witness_degree': degree,
              'witness_residue': encode(total), 'displayed_C638_tables': 'all checked',
              'scope': 'fixed C638 phi^8 and phi^16 certificate; no all-depth or original-gate claim'}
    (output / 'reviewer-verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
