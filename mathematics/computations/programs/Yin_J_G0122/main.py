"""Exact finite margins and extraction from the accepted complete pair table."""
from fractions import Fraction as F
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[3]
OUT=REPO/'mathematics'/'computations'/'outputs'/HERE.name


def beta(a):
    return (-a[3],a[0]+a[3],a[1]+a[3],a[2]+a[3])


def inverse(a):
    return (a[0]+a[1],a[0]+a[2],a[0]+a[3],-a[0])


def power(a,n):
    for _ in range(abs(n)):
        a=(beta if n>=0 else inverse)(a)
    return a


def mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def ev(a,x):
    q=(F(0),F(0))
    for d in reversed(a):
        q=add(mul(q,x),(F(d),F(d)))
    return q


def abs_i(q):
    return (F(0) if q[0]<=0<=q[1] else min(abs(q[0]),abs(q[1])),max(abs(q[0]),abs(q[1])))


def serial(q):
    if isinstance(q,F):return [q.numerator,q.denominator]
    if isinstance(q,(tuple,list)):return [serial(x) for x in q]
    if isinstance(q,dict):return {k:serial(v) for k,v in q.items()}
    return q


def main():
    inp=json.loads((HERE/'inputs.json').read_text(encoding='utf-8'))
    assert inp['root_input']=='mathematics/computations/programs/Yin_J_G0118/inputs.json'
    assert inp['pair_input']=='mathematics/computations/outputs/Yin_J_G0121/certificate.json'
    old=json.loads((REPO/inp['root_input']).read_text(encoding='utf-8'))
    pairs=json.loads((REPO/inp['pair_input']).read_text(encoding='utf-8'))
    x=(F(*old['beta_lower']),F(*old['beta_upper']))
    assert old['polynomial_ascending']==[1,-1,-1,-1,1]
    assert ev(old['polynomial_ascending'],(x[0],x[0]))[0]<0<ev(old['polynomial_ascending'],(x[1],x[1]))[0]
    xm1=(x[0]-1,x[1]-1);xi=(1/x[1],1/x[0])
    bp4=ev((0,0,0,0,1),x);bm4=ev((0,0,0,0,1),xi)
    ep=F(*inp['epsilon_plus']);em=F(*inp['epsilon_minus'])
    assert (ep,em)==(F(1,100),F(1,5))
    margins=[]
    for q in inp['right_labels']:
        plus=mul(add(abs_i(ev(q,x)),(ep,ep)),xm1)
        minus=mul(add(abs_i(ev(q,xi)),(em,em)),xm1)
        assert plus[1]<1 and minus[1]<x[0]
        margins.append({'side':'right','label':q,'expanding_scaled':plus,'stable_scaled':minus})
    for q in inp['left_base_labels']:
        y=power(tuple(q),4)
        plus=mul(add(abs_i(ev(y,x)),mul(bp4,(ep,ep))),xm1)
        minus=mul(add(abs_i(ev(y,xi)),mul(bm4,(em,em))),xm1)
        assert plus[1]<1 and minus[1]<x[0]
        margins.append({'side':'left','label':y,'expanding_scaled':plus,'stable_scaled':minus})
    assert len(margins)==9
    words=pairs['pattern_words']
    assert len(words)==81 and len({tuple(w) for w in words})==81
    assert all(len(w)==4 and set(w)<={-1,0,1} for w in words)
    assert pairs['pair_count']==6561 and len(pairs['pairs'])==6561
    assert {(r['u_index'],r['v_index']) for r in pairs['pairs']}=={(i,j) for i in range(81) for j in range(81)}
    positive=set();coverage=[];actual_counts={'YCY':0,'CYC':0}
    for r in pairs['pairs']:
        u=words[r['u_index']];v=words[r['v_index']]
        for kind in ('YCY','CYC'):
            if not r[kind]:continue
            actual_counts[kind]+=1
            w=tuple((v[i]-u[i])*(1 if kind=='YCY' else -1) for i in range(4))
            inc=sum(w)
            assert inc==r[kind+'_lambda_change'] and inc in (-1,0,1)
            if inc>0:
                positive.add(w)
                coverage.append({'u_index':r['u_index'],'v_index':r['v_index'],'kind':kind,'w':w})
    assert actual_counts=={'YCY':183,'CYC':183}
    expected={(-2,2,2,-1),(-1,1,2,-1),(-1,2,0,0),(-1,2,1,-1),(-1,2,2,-2),(0,0,2,-1)}
    assert positive==expected and len(coverage)==36
    cb=tuple(inp['blocked_label']);assert cb==(-3,9,1,-3)
    assert sum(a*b for a,b in zip((2,3,5,9),cb))==-1
    cbp=mul(abs_i(ev(power(cb,4),x)),xm1)
    cbm=mul(abs_i(ev(cb,xi)),xm1)
    assert cbp[1]<1 and cbm[1]<x[0]
    failures=[]
    for w in sorted(positive):
        delta=power(w,-4)
        target=tuple(cb[i]+delta[i] for i in range(4))
        plus=mul(abs_i(ev(power(target,4),x)),xm1)
        minus=mul(abs_i(ev(target,xi)),xm1)
        bad_plus=plus[0]>1;bad_minus=minus[0]>x[1]
        assert bad_plus or bad_minus
        failures.append({'w':w,'delta':delta,'target':target,'expanding_scaled':plus,'stable_scaled':minus,
                         'fails_expanding':bad_plus,'fails_stable':bad_minus})
    result={'root_bracket':x,'margin_records':margins,'strict_margin_count':18,
            'reused_pair_coverage':actual_counts,'positive_pair_occurrences':coverage,
            'positive_translations':sorted(positive),'blocked_label':cb,
            'blocked_expanding_scaled':cbp,'blocked_stable_scaled':cbm,'endpoint_failures':failures}
    text=json.dumps(serial(result),indent=2)+'\n'
    assert len(text.encode('utf-8'))<262144
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'certificate.json').write_text(text,encoding='utf-8')
    print(json.dumps({'strict_margins':18,'positive_occurrences':len(coverage),'positive_translations':len(positive),
                      'blocked_label_lambda':-1,'endpoint_failures':len(failures)}))


if __name__=='__main__':main()
