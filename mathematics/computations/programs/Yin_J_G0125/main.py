"""Exact combined-ring coprime-fifteen support test; kernels copied from J123."""

import json
from collections import deque
from pathlib import Path


def divmod_poly(a, b):
    q = 0
    while a.bit_length() >= b.bit_length():
        j = a.bit_length() - b.bit_length()
        q ^= 1 << j
        a ^= b << j
    return q, a


def mul(a, b, modulus=0):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return divmod_poly(c, modulus)[1] if modulus else c


def power(a, n, modulus=0):
    c = 1
    while n:
        if n & 1:
            c = mul(c, a, modulus)
        a = mul(a, a, modulus)
        n >>= 1
    return c


def derivative(a):
    return sum(((a >> j) & 1) << (j - 1) for j in range(1, a.bit_length(), 2))


def inverse(a, modulus):
    result = power(a, 47, modulus)
    assert mul(a, result, modulus) == 1
    return result



PHI = 7
M = power(PHI, 16) << 8


def leading_bit(a):
    low = (a ^ 1) & 255
    if low:
        assert not low & 1
        return (low & -low).bit_length() - 2
    value = divmod_poly(a, power(PHI, 16))[1] ^ 1
    j = 0
    while value:
        value, r = divmod_poly(value, PHI)
        if r:
            assert j > 0
            return 7 + 2 * (j - 1) + (0 if r & 1 else 1)
        j += 1
    return None


def product_vector(e, gs):
    value = 1
    for exponent, g in zip(e, gs):
        value = mul(value, power(g, exponent, M), M)
    return value


def add_vectors(a, b, sign=1):
    return [(x + sign * y) % 48 for x, y in zip(a, b)]


def source_rows():
    previous, current = 1, 3
    values = {1: previous, 3: current}
    for n in range(5, 322, 2):
        previous, current = current, mul(2, current, M) ^ previous
        values[n] = current
    rows = []
    for n in range(1, 160, 2):
        if n % 5:
            m = n if n % 3 else n + 160
            assert values[m] == values[n]
            rows.append({'n': n, 'm': m, 'value': values[n]})
    assert len(rows) == 64 and values[161] == 1
    return rows


def subgroup(rows):
    gs = [r['value'] for r in rows]
    b3 = next(i for i, r in enumerate(rows) if r['n'] == 3)
    teich = power(3, 16, M)
    assert teich & 255 == 1 and power(teich, 3, M) == 1
    residues = {divmod_poly(power(teich, j, M), PHI)[1]: j for j in range(3)}
    queue = deque()
    for i, g in enumerate(gs):
        r = residues[divmod_poly(g, PHI)[1]]
        e = [0] * len(gs)
        e[i] = 1
        e[b3] = (e[b3] - 16 * r) % 48
        queue.append((mul(g, power(teich, (-r) % 3, M), M), e))
    pivots = {}
    events = cancellations = 0
    while queue:
        u, e = queue.popleft()
        events += 1
        for _ in range(38):
            bit = leading_bit(u)
            if bit is None:
                break
            if bit not in pivots:
                pivots[bit] = {'bit': bit, 'value': u, 'exponents': e}
                queue.append((mul(u, u, M), [(2 * v) % 48 for v in e]))
                break
            p = pivots[bit]
            u = mul(u, inverse(p['value'], M), M)
            e = add_vectors(e, p['exponents'], -1)
            cancellations += 1
        else:
            raise AssertionError('Filtration bound exceeded')
    assert events <= 101
    group = {'modulus': M, 'generators': gs, 'teichmuller': teich, 'b3_index': b3,
             'pivots': [pivots[b] for b in sorted(pivots)],
             'insertions': events, 'cancellations': cancellations,
             'order': 3 * 2 ** len(pivots)}
    for p in group['pivots']:
        assert product_vector(p['exponents'], gs) == p['value']
        assert membership(mul(p['value'], p['value'], M), group)['member']
    for g in gs:
        assert membership(g, group)['member']
    return group


def membership(value, group):
    teich = group['teichmuller']
    residue = divmod_poly(value, PHI)[1]
    r = next(i for i in range(3) if divmod_poly(power(teich, i, M), PHI)[1] == residue)
    u = mul(value, power(teich, (-r) % 3, M), M)
    expression = [0] * len(group['generators'])
    expression[group['b3_index']] = 16 * r
    pivots = {p['bit']: p for p in group['pivots']}
    for _ in range(38):
        bit = leading_bit(u)
        if bit is None or bit not in pivots:
            return {'target': value, 'member': bit is None,
                    'expression': expression, 'residual': u, 'first_missing_bit': bit}
        p = pivots[bit]
        u = mul(u, inverse(p['value'], M), M)
        expression = add_vectors(expression, p['exponents'])
    raise AssertionError('Membership bound exceeded')


def main():
    rows = source_rows()
    group = subgroup(rows)
    targets = []
    for epsilon in (0, 1):
        y = 4 ^ mul(power(PHI, 16), 21)
        if epsilon:
            y ^= power(PHI, 8) << 14
        row = membership(y, group)
        row['epsilon'] = epsilon
        assert y & 255 == 17
        assert divmod_poly(y, power(PHI, 16))[1] == (4 ^ ((power(PHI, 8) << 14) if epsilon else 0))
        targets.append(row)
    witness = None
    for target in targets:
        if target['member']:
            assert product_vector(target['expression'], group['generators']) == target['target']
            factors = [{'m': r['m'], 'exponent': e} for r, e in zip(rows, target['expression']) if e]
            factors.append({'m': 161, 'exponent': 1})
            multiplicities = {}
            degree = 0
            for f in factors:
                degree += f['exponent'] * ((f['m'] - 1) // 2)
                for d in range(3, f['m'] + 1, 2):
                    if f['m'] % d == 0:
                        multiplicities[d] = multiplicities.get(d, 0) + f['exponent']
            assert multiplicities[161] == 1
            witness = {'epsilon': target['epsilon'], 'factors': factors,
                       'complete_multiplicities': multiplicities, 'degree': degree,
                       'target': target['target']}
            break
    data = {'phi': PHI, 'M': M, 'ambient_order': 3 * 2 ** 37,
            'rows': rows, 'group': group, 'targets': targets, 'witness': witness}
    home = Path(__file__).resolve().parent
    out = home.parents[2] / 'computations' / 'outputs' / home.name / 'certificate.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(out), 'pivots': len(group['pivots']),
                      'order': group['order'], 'index': data['ambient_order'] // group['order'],
                      'targets': [{k: r[k] for k in ('epsilon','member','residual','first_missing_bit')} for r in targets],
                      'witness_degree': witness['degree'] if witness else None}, indent=2))


if __name__ == '__main__':
    main()
