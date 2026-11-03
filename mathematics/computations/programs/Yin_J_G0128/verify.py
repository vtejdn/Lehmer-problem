"""Dense CRT and full product checks for exactly the three A12 targets.
This is author verification, not independent agent review.
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

PHI=[1,1,1]
M16=powmod(PHI,16)
MODULUS=[0]*8+M16

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

def main():
    home=Path(__file__).resolve().parent
    outputs=home.parents[2]/'computations'/'outputs'
    data=json.loads((outputs/'Yin_J_G0126'/'certificate.json').read_text(encoding='utf-8'))
    cert=json.loads((outputs/home.name/'certificate.json').read_text(encoding='utf-8'))
    assert cert['parameters']==[[0,1],[1,0],[1,1]] and len(cert['results'])==3
    assert cert['modulus']==data['M']==encode(MODULUS)
    group=data['group']
    gs=[decode(r['value']) for r in data['rows']]
    assert len(gs)==96 and [encode(g) for g in gs]==group['generators']
    pivots={p['bit']:p for p in group['pivots']}
    assert len(pivots)==34
    chi=multiply([0,1],powmod(PHI,2))
    x8=[0]*8+[1]
    used=set()
    summaries=[]
    for (u,v),result in zip(((0,1),(1,0),(1,1)),cert['results']):
        assert (result['u'],result['v'])==(u,v)
        hx=trim([1,u,v])
        hc=[1]
        if u: hc=add(hc,chi)
        if v: hc=add(hc,powmod(chi,2))
        low=multiply([1,0,0,0,1],inv(powmod(hx,2,x8),x8),x8)
        primary=multiply(powmod([0,1],14,M16),powmod(inv(hc,M16),7,M16),M16)
        target=decode(result['target'])
        assert divide(target,x8)[1]==low and divide(target,M16)[1]==primary
        assert result['low_X']==encode(low) and result['phi_primary']==encode(primary)
        assert len(target)<len(MODULUS)
        residual=decode(result['residual'])
        assert multiply(expression(result['expression'],gs),residual,MODULUS)==target
        bit=first_bit(residual)
        assert bit==result['first_missing_bit']
        assert result['member']==(residual==[1])
        assert bit is None or bit not in pivots
        t=decode(group['teichmuller'])
        residue=divide(target,PHI)[1]
        j=next(j for j in range(3) if divide(powmod(t,j,MODULUS),PHI)[1]==residue)
        reduced=multiply(target,powmod(t,(-j)%3,MODULUS),MODULUS)
        trace=result['trace']
        assert len(trace)<=37 and trace==sorted(set(trace))
        for expected in trace:
            assert first_bit(reduced)==expected and expected in pivots
            p=pivots[expected]
            if expected not in used:
                assert expression(p['exponents'],gs)==decode(p['value'])
                assert first_bit(decode(p['value']))==expected
                used.add(expected)
            reduced=multiply(reduced,inv(decode(p['value']),MODULUS),MODULUS)
        assert reduced==residual
        summaries.append({'u':u,'v':v,'member':result['member'],'missing_bit':bit,
                          'crt_identity':True,'target_product_identity':True})
    out={'verified':True,'exact_targets':summaries,'used_pivot_expressions':len(used),
         'unchanged_group_completeness':'adopted C643v2 and fixed J126, not reproved here'}
    (outputs/home.name/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
