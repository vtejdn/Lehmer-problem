"""Two declared squaring targets; arithmetic reused from fixed J126."""
import json
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

def inverse(a, modulus):
    result = power(a, 47, modulus)
    assert mul(a, result, modulus) == 1
    return result

PHI=7
M=power(PHI,16)<<8

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

def membership(value, group):
    teich = group['teichmuller']
    residue = divmod_poly(value, PHI)[1]
    r = next(i for i in range(3) if divmod_poly(power(teich, i, M), PHI)[1] == residue)
    u = mul(value, power(teich, (-r) % 3, M), M)
    trace = []
    expression = [0] * len(group['generators'])
    expression[group['b3_index']] = 16 * r
    pivots = {p['bit']: p for p in group['pivots']}
    for _ in range(38):
        bit = leading_bit(u)
        if bit is None or bit not in pivots:
            return {'target': value, 'member': bit is None,
                    'expression': expression, 'residual': u, 'first_missing_bit': bit, 'trace': trace}
        p = pivots[bit]
        trace.append(bit)
        u = mul(u, inverse(p['value'], M), M)
        expression = add_vectors(expression, p['exponents'])
    raise AssertionError('Membership bound exceeded')

def main():
    home=Path(__file__).resolve().parent
    outputs=home.parents[2]/'computations'/'outputs'
    fixed=outputs/'Yin_J_G0126'/'certificate.json'
    data=json.loads(fixed.read_text(encoding='utf-8'))
    group=data['group']
    assert data['M']==M and len(group['generators'])==96
    assert len(group['pivots'])==34 and group['order']==3*2**34
    y=0x1500150011
    assert data['targets'][0]['target']==y
    results=[]
    for exponent in (2,4):
        target=power(y,exponent,M)
        result=membership(target,group)
        result['power']=exponent
        assert len(result['trace'])<=37
        assert result['trace']==sorted(set(result['trace']))
        assert mul(product_vector(result['expression'],group['generators']),result['residual'],M)==target
        results.append(result)
    assert results[0]['target']==0x1100110001
    assert results[0]['target']&255==1
    assert divmod_poly(results[0]['target'],power(PHI,16))[1]==power(2,4)
    out=outputs/home.name
    out.mkdir(parents=True,exist_ok=True)
    payload={'fixed_input':'mathematics/computations/outputs/Yin_J_G0126/certificate.json',
             'modulus':M,'base_target':y,'tested_powers':[2,4],'results':results}
    (out/'certificate.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{'power':r['power'],'target':hex(r['target']),'member':r['member'],
                      'residual':hex(r['residual']),'first_missing_bit':r['first_missing_bit'],
                      'cancellations':len(r['trace'])} for r in results],indent=2))

if __name__=='__main__':
    main()
