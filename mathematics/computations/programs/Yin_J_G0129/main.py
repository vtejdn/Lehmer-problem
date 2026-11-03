"""Exact two-target full A12 image; new 320-row certificate at X24 phi48."""
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

PHI=7
P48=power(PHI,48)
M=P48<<24
PRE=power(PHI,49)<<24
EXP=192
LOW=(1<<24)-1

def inverse(a,modulus):
    result=power(a,EXP-1,modulus)
    assert mul(a,result,modulus)==1
    return result


def leading_bit(a):
    low = (a ^ 1) & LOW
    if low:
        assert not low & 1
        return (low & -low).bit_length() - 2
    value = divmod_poly(a, power(PHI, 48))[1] ^ 1
    j = 0
    while value:
        value, r = divmod_poly(value, PHI)
        if r:
            assert j > 0
            return 23 + 2 * (j - 1) + (0 if r & 1 else 1)
        j += 1
    return None

def product_vector(e, gs):
    value = 1
    for exponent, g in zip(e, gs):
        value = mul(value, power(g, exponent, M), M)
    return value

def add_vectors(a, b, sign=1):
    return [(x + sign * y) % EXP for x, y in zip(a, b)]

def subgroup(rows):
    gs = [r['value'] for r in rows]
    b3 = next(i for i, r in enumerate(rows) if r['n'] == 3)
    teich = power(3, 64, M)
    assert teich & LOW == 1 and power(teich, 3, M) == 1
    residues = {divmod_poly(power(teich, j, M), PHI)[1]: j for j in range(3)}
    queue = deque()
    for i, g in enumerate(gs):
        r = residues[divmod_poly(g, PHI)[1]]
        e = [0] * len(gs)
        e[i] = 1
        e[b3] = (e[b3] - 64 * r) % EXP
        queue.append((mul(g, power(teich, (-r) % 3, M), M), e))
    pivots = {}
    events = cancellations = 0
    while queue:
        u, e = queue.popleft()
        events += 1
        for _ in range(118):
            bit = leading_bit(u)
            if bit is None:
                break
            if bit not in pivots:
                pivots[bit] = {'bit': bit, 'value': u, 'exponents': e}
                queue.append((mul(u, u, M), [(2 * v) % EXP for v in e]))
                break
            p = pivots[bit]
            u = mul(u, inverse(p['value'], M), M)
            e = add_vectors(e, p['exponents'], -1)
            cancellations += 1
        else:
            raise AssertionError('Filtration bound exceeded')
    assert events <= 437
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
    trace = []
    expression = [0] * len(group['generators'])
    expression[group['b3_index']] = 64 * r
    pivots = {p['bit']: p for p in group['pivots']}
    for _ in range(118):
        bit = leading_bit(u)
        if bit is None or bit not in pivots:
            return {'target': value, 'member': bit is None,
                    'expression': expression, 'residual': u, 'first_missing_bit': bit, 'trace': trace}
        p = pivots[bit]
        trace.append(bit)
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

def matrix_product(a,b,modulus):
    return [[mul(a[i][0],b[0][j],modulus)^mul(a[i][1],b[1][j],modulus)
             for j in range(2)] for i in range(2)]

def matrix_power(n,modulus):
    a=[[2,1],[1,0]]
    result=[[1,0],[0,1]]
    while n:
        if n&1: result=matrix_product(result,a,modulus)
        a=matrix_product(a,a,modulus)
        n>>=1
    return result

def source_rows():
    previous,current=1,3
    values={1:previous,3:current}
    for n in range(5,1924,2):
        previous,current=current,mul(2,current,PRE)^previous
        values[n]=current
    rows=[]
    for n in range(1,640,2):
        if n%5:
            m=n if n%3 else n+640
            value=divmod_poly(values[n],M)[1]
            assert divmod_poly(values[m],M)[1]==value
            rows.append({'kind':'B','n':n,'m':m,'value':value})
    for n in range(5,640,10):
        r=n//5
        k=next(k for k in range(3) if (r+128*k)%3 and (r+128*k)%5)
        ell=r+128*k
        m=5*ell
        value,rem=divmod_poly(values[n],PHI)
        lifted,rem_lift=divmod_poly(values[m],PHI)
        assert rem==rem_lift==0 and value==lifted
        assert value.bit_length()<=120
        rows.append({'kind':'D','n':n,'m':m,'ell':ell,'k':k,'value':value})
    assert len(rows)==320 and divmod_poly(values[1921],M)[1]==1
    assert matrix_power(320,M)==matrix_power(320,PRE)==[[1,0],[0,1]]
    return rows

def full_targets():
    chi=mul(2,power(PHI,2))
    psi=power(chi,2)^chi^1
    b=mul(1<<10,chi^1)
    den=mul(power(7,42,1<<12),3,1<<12)
    ell=mul(1^(1<<8),inverse(den,1<<12),1<<12)
    low=power(ell,2)
    assert low.bit_length()<=24
    beta=power(2,64,P48)
    ix=inverse(2,P48)
    ib=inverse(b,P48)
    base=mul(power(ix,12,P48),power(ib,7,P48),P48)
    correction=mul(beta,mul(power(ix,12,P48),power(ib,13,P48),P48),P48)
    s=mul(power(2,16,P48),mul(power(3,32,P48),power(PHI,40,P48),P48),P48)
    targets=[]
    for epsilon in (0,1):
        primary=base ^ (mul(correction,s,P48) if epsilon else 0)
        adjustment=mul(inverse(P48,1<<24),low^(primary&LOW),1<<24)
        target=primary^mul(P48,adjustment)
        assert target&LOW==low and divmod_poly(target,P48)[1]==primary
        targets.append({'epsilon':epsilon,'target':target,'low_X':low,'phi_primary':primary})
    return targets

def gate_certificate(y,epsilon):
    chi=mul(2,power(PHI,2))
    psi=power(chi,2)^chi^1
    b=mul(1<<10,chi^1)
    beta=power(2,64,P48)
    h=mul(power(2,12,P48),y,P48)
    c=mul(power(2,12,P48),mul(compose(y,chi,P48),power(psi,84,P48),P48),P48)
    v=mul(h,b,P48)
    d=v^power(c,3,P48)
    s=mul(power(2,16,P48),mul(power(3,32,P48),power(PHI,40,P48),P48),P48) if epsilon else 0
    z=mul(power(beta,2,P48),inverse(b,P48),P48)
    assert divmod_poly(power(z,11,P48)^mul(h,power(c,2,P48),P48),power(PHI,36))[1]==0
    assert power(h,6,P48)==power(c,21,P48)
    assert mul(z,d,P48)^mul(h,mul(v,s,P48),P48)==0
    assert divmod_poly(d,power(PHI,40))[1]==0
    assert divmod_poly(d,power(PHI,12))[1]==0
    assert derivative(y)&LOW==0
    assert divmod_poly(derivative(v),P48)[1]==0
    return {'root_precision':36,'old_and_gate_precision':48,'D_order_at_least':40,
            'canonical_phi_bracket_precision':12,'low_X_derivative_order':24,
            'V_phi_derivative_order':48,'Z':z,'C':c,'D':d,'S':s}

def divisors(n):
    return [d for d in range(2,n+1) if n%d==0]

def witness(result,rows):
    factors=[]
    counts={}
    degree=0
    for row,e in zip(rows,result['expression']):
        if not e: continue
        assert 0<=e<EXP
        factors.append({'kind':row['kind'],'index':row['m'],'exponent':e})
        degree+=e*((row['m']-1)//2-(2 if row['kind']=='D' else 0))
        if row['kind']=='B':
            orders=divisors(row['m'])
        else:
            ds=divisors(row['ell'])
            orders=ds+[5*d for d in ds]
        for n in orders: counts[n]=counts.get(n,0)+e
    factors.append({'kind':'B','index':1921,'exponent':1})
    degree+=960
    for n in divisors(1921): counts[n]=counts.get(n,0)+1
    assert counts[1921]==1
    assert all(n%3 and n%25 for n in counts)
    inequalities=[]
    for n,e in sorted(counts.items()):
        if n%5==0:
            parent=counts.get(n//5,0)
            assert e<=parent
            inequalities.append({'source_order':n,'source_multiplicity':e,
                                 'target_order':n//5,'target_multiplicity':parent})
    assert degree==sum(euler(n)//2*e for n,e in counts.items())
    assert degree<=58370560 and len(factors)<=321
    return {'epsilon':result['epsilon'],'factors':factors,
            'complete_multiplicities':counts,'degree':degree,
            'order1921_multiplicity':1,'all_orders_coprime3':True,'no_order25_source':True,
            'C5_downward_inequalities':inequalities,'normalized_U_degree':180+degree,
            'normalized_R_degree':171+degree,'degree_gap':9,'X_orders':[12,22],
            'phi_orders':[84,72],'normalized_U_and_R_nonsquare':True,
            'full_gate':gate_certificate(result['target'],result['epsilon'])}

def main():
    rows=source_rows()
    group=subgroup(rows)
    targets=[]
    for item in full_targets():
        result=membership(item['target'],group)
        result.update(item)
        assert len(result['trace'])<=117
        assert mul(product_vector(result['expression'],group['generators']),result['residual'],M)==result['target']
        targets.append(result)
    witnesses=[witness(t,rows) for t in targets if t['member']]
    home=Path(__file__).resolve().parent
    out=home.parents[2]/'computations'/'outputs'/home.name
    out.mkdir(parents=True,exist_ok=True)
    data={'phi':PHI,'M':M,'predivision_M':PRE,'ambient_order':3*2**117,
          'exponent':192,'rows':rows,'group':group,'targets':targets,'witnesses':witnesses}
    (out/'certificate.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'pivots':len(group['pivots']),'order':group['order'],
                     'index':data['ambient_order']//group['order'],
                     'insertions':group['insertions'],'cancellations':group['cancellations'],
                     'targets':[{k:t[k] for k in ('epsilon','member','first_missing_bit','residual')} for t in targets],
                     'witness_degrees':[w['degree'] for w in witnesses]},indent=2))

if __name__=='__main__':
    main()
