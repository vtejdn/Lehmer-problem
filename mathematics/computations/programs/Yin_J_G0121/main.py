"""One exact 81^2 pair screen and one fixed seven-update original-word chain."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OUT = REPO/'mathematics'/'computations'/'outputs'/HERE.name
ZERO = (0,0,0,0)


def beta(a):
    return (-a[3],a[0]+a[3],a[1]+a[3],a[2]+a[3])


def inverse(a):
    return (a[0]+a[1],a[0]+a[2],a[0]+a[3],-a[0])


def power(a,n):
    for _ in range(abs(n)):
        a=(beta if n>=0 else inverse)(a)
    return a


def word_value(digits):
    a=ZERO
    for d in reversed(digits):
        a=beta(a)
        a=(a[0]+d,*a[1:])
    return a


def mul(a,b):
    values=[x*y for x in a for y in b]
    return min(values),max(values)


def ev(a,x):
    r=(F(0),F(0))
    for d in reversed(a):
        r=mul(r,x)
        r=(r[0]+d,r[1]+d)
    return r


def abs_i(a):
    lo=F(0) if a[0]<=0<=a[1] else min(abs(a[0]),abs(a[1]))
    return lo,max(abs(a[0]),abs(a[1]))


def sign_test(interval):
    assert interval[1]<2 or interval[0]>2, interval
    return interval[1]<2


def lam(c):
    return sum(a*b for a,b in zip((2,3,5,9),c))


def rational_json(v):
    if isinstance(v,F):
        return [v.numerator,v.denominator]
    if isinstance(v,(tuple,list)):
        return [rational_json(x) for x in v]
    if isinstance(v,dict):
        return {k:rational_json(x) for k,x in v.items()}
    return v


def main():
    inp=json.loads((HERE/'inputs.json').read_text(encoding='utf-8'))
    assert inp['starting_word_input']=='mathematics/computations/programs/Yin_J_G0118/inputs.json'
    old=json.loads((REPO/inp['starting_word_input']).read_text(encoding='utf-8'))
    assert old['polynomial_ascending']==[1,-1,-1,-1,1]
    x=(F(*old['beta_lower']),F(*old['beta_upper']))
    assert ev(old['polynomial_ascending'],(x[0],x[0]))[0]<0
    assert ev(old['polynomial_ascending'],(x[1],x[1]))[0]>0
    assert F(17,10)<x[0]<x[1]<F(18,10)
    xm1=(x[0]-1,x[1]-1)
    xi=(1/x[1],1/x[0])
    words=list(product((-1,0,1),repeat=4))
    records={}
    def measures(theta):
        if theta not in records:
            a=mul(abs_i(ev(theta,x)),xm1)
            r=mul(abs_i(ev(tuple(reversed(theta)),x)),xm1)
            records[theta]={'theta':theta,'A':a,'R':r,'A_pass':sign_test(a),'R_pass':sign_test(r)}
        return records[theta]
    pairs=[]
    count={'YCY':0,'CYC':0,'YCY_lambda_change':0,'CYC_lambda_change':0}
    for i,u in enumerate(words):
        mu=measures(u)
        for j,v in enumerate(words):
            mv=measures(v)
            difference=tuple(v[q]-u[q] for q in range(4))
            md=measures(difference)
            ycy=md['A_pass'] and mu['R_pass'] and mv['R_pass'] and md['R_pass']
            cyc=mu['A_pass'] and mv['A_pass'] and md['A_pass'] and md['R_pass']
            change=sum(difference)
            pairs.append({'u_index':i,'v_index':j,'YCY':ycy,'CYC':cyc,'YCY_lambda_change':change,'CYC_lambda_change':-change})
            count['YCY']+=int(ycy)
            count['CYC']+=int(cyc)
            count['YCY_lambda_change']+=int(ycy and change!=0)
            count['CYC_lambda_change']+=int(cyc and change!=0)
    assert len(pairs)==81**2
    u=tuple(inp['u']);v=tuple(inp['v'])
    chosen=pairs[words.index(u)*81+words.index(v)]
    assert chosen['YCY'] and chosen['YCY_lambda_change']==1
    h_patterns=((-1,1,0,0),(0,-1,1,0),(0,0,-1,1))
    for theta in h_patterns:
        assert pairs[words.index(ZERO)*81+words.index(theta)]['YCY']
    c0=tuple(old['c']);ca=(-3,2,0,0);cp=(0,3,0,-1);cm=(-2,0,-1,1)
    assert tuple(cp[i]-c0[i] for i in range(4))==power(tuple(v[i]-u[i] for i in range(4)),-4)
    assert (lam(c0),lam(cp),lam(cm))==(-1,0,0)
    core_records=[]
    for c in (c0,ca,cp,cm,ZERO,power(c0,4),power(cp,4),power(cm,4)):
        plus=mul(abs_i(ev(c,x)),xm1)
        minus=mul(abs_i(ev(c,xi)),xm1)
        assert plus[1]<1 and minus[1]<x[0]
        core_records.append({'state':c,'expanding_scaled':plus,'stable_scaled':minus})
    k=inp['tail_length'];assert k==24 and old['tail_length']==k
    a0=old['left'];r0=old['right'];ap=inp['left_cp'];am=inp['left_cm']
    ra=inp['right_a'];rp=inp['right_cp'];rm=inp['right_cm'];zero=[0]*k
    for tail in (a0,r0,ap,am,ra,rp,rm):
        assert len(tail)==k and set(tail)<={-1,0,1}
    assert word_value(ra)==ca and word_value(rp)==cp and word_value(rm)==cm
    assert word_value(ap)==tuple(-a for a in power(cp,k+4))
    assert word_value(am)==tuple(-a for a in power(cm,k+4))
    zero_mid=[0]*4
    chain=[a0+zero_mid+r0,a0+list(u)+ra,ap+list(v)+ra,
           ap+zero_mid+rp,ap+inp['short_middle_one']+rm,
           am+zero_mid+rm,am+inp['short_middle_two']+zero,[0]*(2*k+4)]
    assert len(chain)==8
    for w in chain:
        assert len(w)==52 and set(w)<={-1,0,1} and word_value(w)==ZERO
    transitions=[]
    for j,(before,after) in enumerate(zip(chain,chain[1:])):
        fixes_y=before[:k]==after[:k]
        fixes_c=before[k+4:]==after[k+4:]
        assert fixes_y != fixes_c
        varied=after[k:] if fixes_y else after[:k+4]
        endpoint=word_value(varied)
        transitions.append({'from':j,'to':j+1,'type':'Y' if fixes_y else 'C',
                            'conditional_length':k+4,'conditional_endpoint':endpoint,
                            'target_variable_zero_count':varied.count(0),
                            'K_numerator_power_two':varied.count(0)-1,
                            'K_denominator':'c_28(conditional_endpoint)',
                            'Q_numerator_power_two':before.count(0)+varied.count(0)-1,
                            'Q_denominator':'c_52(0) c_28(conditional_endpoint)'})
    payload={'pair_count':len(pairs),'count':count,'pattern_words':words,
             'interval_records':[records[key] for key in sorted(records)],'pairs':pairs,
             'chosen_pair':chosen,'core_state_intervals':core_records,'n':26,
             'chain':chain,'word_zero_counts':[w.count(0) for w in chain],
             'transitions':transitions,
             'selected_seven_update_lower_bound_exponent':sum(t['target_variable_zero_count'] for t in transitions)-7*57}
    output=json.dumps(rational_json(payload),indent=2)+'\n'
    assert len(output.encode('utf-8'))<4*1024*1024
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'certificate.json').write_text(output,encoding='utf-8')
    print(json.dumps({'count':count,'n':26,'states':8,'transitions':transitions,
                      'word_zero_counts':payload['word_zero_counts'],
                      'lower_bound_exponent':payload['selected_seven_update_lower_bound_exponent']}))


if __name__=='__main__':
    main()
