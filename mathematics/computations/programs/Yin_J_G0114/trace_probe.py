from pathlib import Path
from fractions import Fraction
import itertools,json,sys
draft=Path('mathematics/ledger/Yin_L_G0004_v1.md')
blocks=draft.read_text(encoding='utf-8').split('```python\n')
second=blocks[2].split('\n```',1)[0]
exec(second.split('\nprimes=',1)[0],globals())
primes=[2,3,5,7,11,13,17,19,23,29,31]

def trace_polynomial(p):
    m=(len(p)-1)//2
    S=[[2],[0,1]]
    for j in range(2,m+1):
        v=[0]+S[-1]
        for i,a in enumerate(S[-2]): v[i]-=a
        S.append(trim(v))
    Q=[p[m]]+[0]*m
    for j in range(1,m+1):
        for i,a in enumerate(S[j]): Q[i]+=p[m+j]*a
    return trim(Q)

def evaluate(f,x):
    y=Fraction(0)
    for a in f[::-1]: y=y*x+a
    return y

def real_bracket(Q):
    values=[evaluate(Q,Fraction(a,4)) for a in range(-8,9)]
    for j in range(1,16):
        if values[j]==0: return [str(Fraction(j-8,4))]*2
    for j in range(16):
        if values[j]*values[j+1]<0:
            return [str(Fraction(j-8,4)),str(Fraction(j-7,4))]
    return None

out={'python':sys.version.split()[0],'grid':'a/4, -8<=a<=8',
     'prime_certificate_list':primes,'degrees':{},'positivity_failures':[],
     'trace_added_threshold_failures':[],'lehmer_certificate':None}
for d in [2,4,6,8,10,12]:
    counts={'enumerated':0,'direct_noncyclotomic':0,'trace_added_noncyclotomic':0,
            'cyclotomic_certified':0,'unresolved':0,'positivity_failures':0,
            'fixed_threshold_failures':0}
    for coeff in itertools.product([-1,0,1],repeat=d//2):
        p=[0]*(d+1);p[0]=p[-1]=1
        for i,a in enumerate(coeff,1): p[i]=p[d-i]=a
        counts['enumerated']+=1
        direct=next((q for q in primes if irreducible_mod(p,q)),None)
        Q=trace_polynomial(p)
        qprime=(2 if len(Q)==2 else next((q for q in primes if irreducible_mod(Q,q)),None))
        bracket=real_bracket(Q) if qprime is not None else None
        if direct is None and bracket is None:
            counts['unresolved']+=1;continue
        if tuple(p) in cyclo_polys:
            counts['cyclotomic_certified']+=1;continue
        key='direct_noncyclotomic' if direct is not None else 'trace_added_noncyclotomic'
        counts[key]+=1
        delta=disc(p);N=2*d;G=gram(p,N);X=delta*G
        record={'degree':d,'coefficients_ascending':p,'direct_prime':direct,
                'trace_coefficients':Q,'trace_prime':qprime,'real_bracket':bracket,
                'N':N,'discriminant_abs':delta,'gram':G,'boundary':N**d}
        if p==[1,1,0,-1,-1,-1,-1,-1,0,1,1]: out['lehmer_certificate']=record
        if X<=N**d:
            counts['positivity_failures']+=1
            out['positivity_failures'].append(record)
        if X**4<N**(4*d)*2**(N-1):
            counts['fixed_threshold_failures']+=1
            if direct is None: out['trace_added_threshold_failures'].append(record)
    out['degrees'][str(d)]=counts
print(json.dumps(out,indent=2))
