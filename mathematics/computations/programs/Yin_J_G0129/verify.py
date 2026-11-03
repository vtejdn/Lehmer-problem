"""Independent dense/Laurent author checker of the new full A12 certificate.
No generator import and no group insertion algorithm.
"""
import json
from pathlib import Path
from math import gcd,isqrt

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

def divide(a,b):
    a=trim(a)
    b=trim(b)
    assert b
    support=[i for i,v in enumerate(b) if v]
    q=[0]*max(0,len(a)-len(b)+1)
    while len(a)>=len(b):
        j=len(a)-len(b)
        q[j]=1
        for k in support: a[j+k]^=1
        a=trim(a)
    return trim(q),a

def multiply(a,b,modulus=None):
    if not a or not b: return []
    # Every integer convolution coefficient is <=min(len(a),len(b)).
    # The digit base is strictly larger, so ordinary multiplication has no inter-digit carry.
    k=(min(len(a),len(b))+1).bit_length()
    aa=sum(v<<(k*i) for i,v in enumerate(a) if v)
    bb=sum(v<<(k*i) for i,v in enumerate(b) if v)
    product=aa*bb
    c=trim([(product>>(k*i))&1 for i in range(len(a)+len(b)-1)])
    return divide(c,modulus)[1] if modulus else c


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

PHI=[1,1,1]
M48=powmod(PHI,48)
MODULUS=[0]*24+M48
PRE=[0]*24+powmod(PHI,49)


def first_bit(value):
    low = add(value[:24], [1])
    if low:
        assert not low[0]
        return next(i - 1 for i in range(1, len(low)) if low[i])
    a = add(divide(value, M48)[1], [1])
    j = 0
    while a:
        a, digit = divide(a, PHI)
        if digit:
            assert j > 0
            return 23 + 2 * (j - 1) + (0 if digit[0] else 1)
        j += 1
    return None

def matrix_product(a, b, modulus=MODULUS):
    return [[add(multiply(a[i][0], b[0][j], modulus),
                 multiply(a[i][1], b[1][j], modulus)) for j in range(2)] for i in range(2)]

def matrix_power(n, modulus=MODULUS):
    a = [[[0, 1], [1]], [[1], []]]
    c = [[[1], []], [[], [1]]]
    while n:
        if n % 2:
            c = matrix_product(c, a, modulus)
        a = matrix_product(a, a, modulus)
        n //= 2
    return c

def compose(a, b):
    c = []
    for coefficient in reversed(a):
        c = multiply(c,b)
        if coefficient:
            c = add(c,[1])
    return c

def compose_mod(a,b,modulus):
    result=[]
    for coefficient in reversed(a):
        result=multiply(result,b,modulus)
        if coefficient: result=add(result,[1])
    return result

def generator_squares(gs):
    squares=[]
    for g in gs:
        row=[g]
        for _ in range(7): row.append(multiply(row[-1],row[-1],MODULUS))
        squares.append(row)
    return squares

def expression(e,squares):
    assert len(e)==320
    result=[1]
    for exponent,row in zip(e,squares):
        assert 0<=exponent<192
        for j in range(8):
            if exponent&(1<<j): result=multiply(result,row[j],MODULUS)
    return result

def reduce_member(value,teich,pivots,pivot_inverses):
    residue=divide(value,PHI)[1]
    j=next(j for j in range(3) if divide(powmod(teich,j,MODULUS),PHI)[1]==residue)
    value=multiply(value,powmod(teich,(-j)%3,MODULUS),MODULUS)
    trace=[]
    while first_bit(value) in pivots:
        bit=first_bit(value)
        value=multiply(value,pivot_inverses[bit],MODULUS)
        trace.append(bit)
        assert first_bit(value) is None or first_bit(value)>bit
        assert len(trace)<=117
    return value,first_bit(value),trace

def exact_targets():
    x=[0,1]
    chi=multiply(x,powmod(PHI,2))
    b=multiply(powmod(x,10),add(chi,[1]))
    t12=[0]*12+[1]
    den=multiply(powmod(PHI,42,t12),[1,1],t12)
    ell=multiply([1]+[0]*7+[1],inv(den,t12),t12)
    low=powmod(ell,2)
    beta=powmod(x,64,M48)
    ix=inv(x,M48)
    ib=inv(b,M48)
    ybase=multiply(powmod(ix,12,M48),powmod(ib,7,M48),M48)
    sc=multiply(powmod(x,16,M48),multiply(powmod([1,1],32,M48),powmod(PHI,40,M48),M48),M48)
    correction=multiply(beta,multiply(powmod(ix,12,M48),powmod(ib,13,M48),M48),M48)
    return [(low,ybase),(low,add(ybase,multiply(correction,sc,M48)))]

def verify_gate(y,epsilon):
    x=[0,1]
    chi=multiply(x,powmod(PHI,2))
    psi=add(add(powmod(chi,2),chi),[1])
    b=multiply(powmod(x,10),add(chi,[1]))
    h=multiply(powmod(x,12,M48),y,M48)
    c=multiply(powmod(x,12,M48),multiply(compose_mod(y,chi,M48),powmod(psi,84,M48),M48),M48)
    v=multiply(h,b,M48)
    d=add(v,powmod(c,3,M48))
    beta=powmod(x,64,M48)
    z=multiply(powmod(beta,2,M48),inv(b,M48),M48)
    s=multiply(powmod(x,16,M48),multiply(powmod([1,1],32,M48),powmod(PHI,40,M48),M48),M48) if epsilon else []
    assert not divide(add(powmod(z,11,M48),multiply(h,powmod(c,2,M48),M48)),powmod(PHI,36))[1]
    assert powmod(h,6,M48)==powmod(c,21,M48)
    assert not add(multiply(z,d,M48),multiply(h,multiply(v,s,M48),M48))
    assert not divide(d,powmod(PHI,40))[1]
    assert not divide(d,powmod(PHI,12))[1]
    assert not divide(deriv(y),[0]*24+[1])[1]
    assert not divide(deriv(v),M48)[1]
    assert y[0]==1 and divide(y,PHI)[1]
    return {'root_precision':36,'old_and_gate_precision':48,'D_order_at_least':40,
            'canonical_phi_bracket_precision':12,'low_X_derivative_order':24,
            'V_phi_derivative_order':48,'Z':encode(z),'C':encode(c),'D':encode(d),'S':encode(s)}

def divisor_list(n):
    result=set()
    for d in range(1,isqrt(n)+1):
        if n%d==0: result.update((d,n//d))
    return sorted(d for d in result if d>1)

def verify_witness(w,target,rows,global_degrees):
    counts={}
    factors=[]
    degree=960
    for row,e,degree_row in zip(rows,target['expression'],global_degrees):
        if not e: continue
        factors.append({'kind':row['kind'],'index':row['m'],'exponent':e})
        degree+=e*degree_row
        orders=divisor_list(row['m']) if row['kind']=='B' else divisor_list(row['ell'])
        if row['kind']=='D': orders=orders+[5*d for d in orders]
        for n in orders: counts[n]=counts.get(n,0)+e
    factors.append({'kind':'B','index':1921,'exponent':1})
    for n in divisor_list(1921): counts[n]=counts.get(n,0)+1
    assert w['factors']==factors and len(factors)<=321
    assert {int(n):e for n,e in w['complete_multiplicities'].items()}==counts
    assert counts[1921]==w['order1921_multiplicity']==1
    assert all(n%3 and n%25 for n in counts)
    weighted=sum((sum(gcd(a,n)==1 for a in range(1,n))//2)*e for n,e in counts.items())
    assert weighted==degree==w['degree'] and degree<=58370560
    inequalities=[]
    for n,e in sorted(counts.items()):
        if n%5==0:
            parent=counts.get(n//5,0)
            assert e<=parent
            inequalities.append({'source_order':n,'source_multiplicity':e,
                                 'target_order':n//5,'target_multiplicity':parent})
    assert w['C5_downward_inequalities']==inequalities
    assert w['all_orders_coprime3'] and w['no_order25_source']
    assert w['normalized_U_degree']==180+degree and w['normalized_R_degree']==171+degree
    assert w['degree_gap']==9 and w['X_orders']==[12,22] and w['phi_orders']==[84,72]
    assert w['normalized_U_and_R_nonsquare']
    assert w['full_gate']==verify_gate(decode(target['target']),target['epsilon'])
    return {'epsilon':target['epsilon'],'degree':degree,'full_multiplicities':len(counts),
            'all_primary_C3_C5_scope':True,'full_gate':True,'global_nonsquare_order1921':True}

def main():
    home=Path(__file__).resolve().parent
    out=home.parents[2]/'computations'/'outputs'/home.name
    data=json.loads((out/'certificate.json').read_text(encoding='utf-8'))
    assert data['M']==encode(MODULUS) and data['predivision_M']==encode(PRE)
    assert data['exponent']==192 and data['ambient_order']==3*2**117
    identity=[[[1],[]],[[],[1]]]
    assert matrix_power(320,MODULUS)==matrix_power(320,PRE)==identity
    expected=[('B',n) for n in range(1,640,2) if n%5]+[('D',n) for n in range(5,640,10)]
    rows=data['rows']
    assert [(r['kind'],r['n']) for r in rows]==expected
    chi=multiply([0,1],powmod(PHI,2))
    gs=[]
    global_degrees=[]
    for row in rows:
        n,m=row['n'],row['m']
        original=whole_trace(n)
        lifted=whole_trace(m)
        if row['kind']=='B':
            assert m==(n if n%3 else n+640) and m<=1279 and gcd(m,15)==1
        else:
            r=n//5
            k=next(k for k in range(3) if gcd(r+128*k,15)==1)
            ell=r+128*k
            assert row['k']==k and row['ell']==ell and m==5*ell and m<=1915
            original,rem=divide(original,PHI)
            lifted,rem_lift=divide(lifted,PHI)
            assert not rem and not rem_lift
            assert lifted==compose(whole_trace(ell),chi)
        reduced=divide(original,MODULUS)[1]
        assert divide(lifted,MODULUS)[1]==reduced and encode(reduced)==row['value']
        assert reduced[0]==1 and divide(reduced,PHI)[1]
        gs.append(reduced)
        global_degrees.append(len(lifted)-1)
    invisible=whole_trace(1921)
    assert len(invisible)-1==960 and divide(invisible,MODULUS)[1]==[1]
    group=data['group']
    assert group['modulus']==data['M'] and group['generators']==[encode(g) for g in gs]
    b3=next(i for i,r in enumerate(rows) if r['kind']=='B' and r['n']==3)
    assert group['b3_index']==b3
    teich=powmod([1,1],64,MODULUS)
    assert encode(teich)==group['teichmuller'] and trim(teich[:24])==[1]
    assert powmod(teich,3,MODULUS)==[1] and teich!=[1]
    bits=[p['bit'] for p in group['pivots']]
    assert bits==sorted(set(bits)) and all(0<=b<117 for b in bits)
    assert group['order']==3*2**len(bits) and len(bits)<=117
    assert group['insertions']<=437 and group['cancellations']<=437*117
    squares=generator_squares(gs)
    pivots={p['bit']:decode(p['value']) for p in group['pivots']}
    inverses={b:inv(p,MODULUS) for b,p in pivots.items()}
    for p in group['pivots']:
        value=decode(p['value'])
        assert first_bit(value)==p['bit'] and expression(p['exponents'],squares)==value
        rem,bit,_=reduce_member(multiply(value,value,MODULUS),teich,pivots,inverses)
        assert rem==[1] and bit is None
    for g in gs:
        rem,bit,_=reduce_member(g,teich,pivots,inverses)
        assert rem==[1] and bit is None
    summaries=[]
    assert len(data['targets'])==2
    x24=[0]*24+[1]
    for epsilon,((low,primary),target) in enumerate(zip(exact_targets(),data['targets'])):
        assert target['epsilon']==epsilon
        value=decode(target['target'])
        assert len(value)<len(MODULUS)
        assert divide(value,x24)[1]==low and divide(value,M48)[1]==primary
        assert target['low_X']==encode(low) and target['phi_primary']==encode(primary)
        rem,bit,trace=reduce_member(value,teich,pivots,inverses)
        assert encode(rem)==target['residual'] and bit==target['first_missing_bit'] and trace==target['trace']
        assert target['member']==(rem==[1])
        assert multiply(expression(target['expression'],squares),rem,MODULUS)==value
        summaries.append({'epsilon':epsilon,'member':target['member'],'first_missing_bit':bit,
                          'target_product_identity':True,'full_CRT':True})
    positive=[t for t in data['targets'] if t['member']]
    assert len(data['witnesses'])==len(positive)
    witnesses=[verify_witness(w,t,rows,global_degrees) for w,t in zip(data['witnesses'],positive)]
    result={'verified':True,'reconstructed_rows':len(rows),'matrix_periods':[320,320],
            'odd_index_periods':[640,640],'pivot_expressions':len(bits),
            'group_order':group['order'],'ambient_index':data['ambient_order']//group['order'],
            'targets':summaries,'witnesses':witnesses,
            'scope':'complete new quotient and two fixed targets; no characteristic-zero realization'}
    (out/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
