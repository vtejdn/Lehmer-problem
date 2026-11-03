"""Exact complete five-descending support test; standalone arithmetic copied from J125."""

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
    premodulus = power(PHI, 17) << 8
    previous, current = 1, 3
    values = {1: previous, 3: current}
    for n in range(5, 964, 2):
        previous, current = current, mul(2, current, premodulus) ^ previous
        values[n] = current
    rows = []
    for n in range(1, 160, 2):
        if n % 5:
            m = n if n % 3 else n + 160
            value = divmod_poly(values[n], M)[1]
            assert divmod_poly(values[m], M)[1] == value
            rows.append({'kind': 'B', 'n': n, 'm': m, 'value': value})
    for n in range(5, 320, 10):
        r = n // 5
        k = next(k for k in range(3) if (r + 64*k) % 3 and (r + 64*k) % 5)
        ell = r + 64*k
        m = 5*ell
        value, remainder = divmod_poly(values[n], PHI)
        lifted, lifted_remainder = divmod_poly(values[m], PHI)
        assert remainder == lifted_remainder == 0 and value == lifted
        assert value.bit_length() <= 40
        rows.append({'kind': 'D', 'n': n, 'm': m, 'ell': ell, 'k': k, 'value': value})
    assert len(rows) == 96 and divmod_poly(values[961], M)[1] == 1
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
    assert events <= 133
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


def compose(a, b, modulus):
    value = 0
    for j in range(a.bit_length()-1, -1, -1):
        value = mul(value, b, modulus) ^ ((a >> j) & 1)
    return value


def euler(n):
    result, p = n, 2
    while p*p <= n:
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result -= result // n
    return result


def gate_certificate(y, epsilon):
    f16, f12, f28 = power(PHI,16), power(PHI,12), power(PHI,28)
    chi = mul(2, power(PHI,2))
    psi = mul(chi,chi) ^ chi ^ 1
    h = mul(power(2,4),y,f16)
    v = mul(power(2,10),y,f16)
    c = mul(mul(power(2,4), compose(y,chi,f16),f16), power(psi,28,f16),f16)
    d = v ^ power(c,3,f16)
    z = power(mul(h,power(c,2,f12),f12),35,f12)
    correction = mul(mul(power(2,8),power(3,16),f16),power(PHI,8),f16) if epsilon else 0
    root_error = power(z,11,f12) ^ mul(h,power(c,2,f12),f12)
    old_error = power(h,6,f16) ^ power(c,21,f16)
    gate_error = mul(z,d,f16) ^ mul(mul(h,v,f16),correction,f16)
    canonical_phi = mul(power(PHI,24),
        mul(mul(power(2,12),power(psi,84,f28),f28),power(compose(y,chi,f28),3,f28),f28)
        ^ mul(power(2,10),y,f28),f28)
    assert root_error == old_error == gate_error == canonical_phi == 0
    assert c == 16 and divmod_poly(d,power(PHI,4))[1] == 0
    assert derivative(y) & 255 == 0
    assert divmod_poly(derivative(v),f16)[1] == 0
    return {'H_phi16':h, 'V_phi16':v, 'C_phi16':c, 'D_phi16':d,
            'Z_phi12':z, 'S_phi16':correction,
            'root_error':root_error, 'old_support_error':old_error,
            'full_gate_error':gate_error, 'canonical_phi28_error':canonical_phi,
            'low_X_derivative_zero':True, 'V_phi16_derivative_zero':True,
            'canonical_X4_zero':True}


def main():
    rows = source_rows()
    group = subgroup(rows)
    targets = []
    for epsilon in (0,1):
        y = 4 ^ mul(power(PHI,16),21)
        if epsilon:
            y ^= power(PHI,8) << 14
        row = membership(y,group)
        row['epsilon'] = epsilon
        targets.append(row)
    witness = None
    for target in targets:
        if target['member']:
            assert product_vector(target['expression'],group['generators']) == target['target']
            factors = [{'kind':r['kind'],'m':r['m'],'exponent':e}
                       for r,e in zip(rows,target['expression']) if e]
            factors.append({'kind':'B','m':961,'exponent':1})
            multiplicities = {}
            degree = 0
            for f in factors:
                degree += f['exponent']*((f['m']-1)//2 - (2 if f['kind']=='D' else 0))
                for d in range(3,f['m']+1,2):
                    if f['m'] % d == 0 and d != 5:
                        multiplicities[d] = multiplicities.get(d,0)+f['exponent']
            assert multiplicities[961] == 1
            inequalities = []
            for n,b in sorted(multiplicities.items()):
                assert n % 3 and n % 25
                if n % 5 == 0:
                    parent = multiplicities[n//5]
                    assert b <= parent
                    inequalities.append({'source_order':n,'source_multiplicity':b,
                                         'target_order':n//5,'target_multiplicity':parent})
            assert degree == sum(euler(n)//2*b for n,b in multiplicities.items())
            odd_degree = sum(euler(n)//2 for n,b in multiplicities.items() if b % 2)
            assert odd_degree >= 33
            witness = {'epsilon':target['epsilon'],'factors':factors,
                       'complete_multiplicities':multiplicities,'degree':degree,
                       'odd_part_degree':odd_degree,'target':target['target'],
                       'C5_downward_inequalities':inequalities,
                       'no_order25_source':True,'all_orders_coprime3':True,
                       'order961_multiplicity':1,
                       'normalized_U_degree':60+degree,'normalized_R_degree':58+degree,
                       'gate':gate_certificate(target['target'],target['epsilon'])}
            break
    data = {'phi':PHI,'M':M,'predivision_M':power(PHI,17)<<8,
            'ambient_order':3*2**37,'rows':rows,'group':group,'targets':targets,'witness':witness}
    home = Path(__file__).resolve().parent
    out = home.parents[2]/'computations'/'outputs'/home.name/'certificate.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(out),'pivots':len(group['pivots']),
                      'order':group['order'],'index':data['ambient_order']//group['order'],
                      'targets':[{k:r[k] for k in ('epsilon','member','residual','first_missing_bit')} for r in targets],
                      'witness_degree':witness['degree'] if witness else None,
                      'complete_orders':len(witness['complete_multiplicities']) if witness else None},indent=2))


if __name__ == '__main__':
    main()
