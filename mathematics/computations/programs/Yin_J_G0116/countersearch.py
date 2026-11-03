from pathlib import Path
from fractions import Fraction
from time import monotonic
from datetime import datetime, timezone
from math import isqrt
import itertools, json, sys

started=monotonic()
started_utc=datetime.now(timezone.utc).isoformat()
CAP=180.0
ledger=Path('mathematics/ledger/Yin_L_G0004_v1.md')
blocks=ledger.read_text(encoding='utf-8').split(chr(96)*3+'python\n')
first=blocks[1].split('\n'+chr(96)*3,1)[0]
second=blocks[2].split('\n'+chr(96)*3,1)[0]
third=blocks[3].split('\n'+chr(96)*3,1)[0]
exec(first.split('\ninputs=',1)[0],globals())
exec(second[second.index('def trim('):second.index('\ncyclo={}')],globals())
exec(third[third.index('def trace_polynomial('):third.index('\nout=')],globals())
primes=[2,3,5,7,11,13,17,19,23,29,31]

def divides(f,g):
    r=f[:]
    while len(r)>=len(g) and r!=[0]:
        c=r[-1]
        shift=len(r)-len(g)
        for j,a in enumerate(g): r[shift+j]-=c*a
        trim(r)
    return r==[0]

cyclo={}
for n in range(1,513):
    f=[-1]+[0]*(n-1)+[1]
    for j in range(1,n):
        if n%j==0: f=divexact(f,cyclo[j])
    cyclo[n]=f
cyclo_small=sorted([(n,f) for n,f in cyclo.items() if len(f)<=17],
                   key=lambda pair:(len(pair[1]),pair[0]))

def toeplitz_gram(p):
    d=len(p)-1
    autoc=[sum(p[j]*p[j+r] for j in range(d+1-r)) for r in range(d)]
    return det([[autoc[abs(i-j)] for j in range(d)] for i in range(d)])

controls=[[1,-3,1],[1,1,1],[1,1,0,-1,-1,-1,-1,-1,0,1,1]]
for p in controls:
    assert toeplitz_gram(p)==gram(p,2*(len(p)-1))

def certify(p):
    if monotonic()-started>=CAP: return {'status':'time_cap_before_certificate'}
    for q in primes:
        if irreducible_mod(p,q):
            return {'status':'irreducible','direct_prime':q}
    Q=trace_polynomial(p)
    qprime=(2 if len(Q)==2 else next((q for q in primes if irreducible_mod(Q,q)),None))
    bracket=real_bracket(Q) if qprime is not None else None
    if qprime is not None and bracket is not None:
        return {'status':'irreducible','trace':Q,'trace_prime':qprime,'bracket':bracket}
    return {'status':'unclassified','trace':Q,'trace_prime':qprime,'bracket':bracket}

out={'python':sys.version.split()[0],'started_utc':started_utc,
     'cap_seconds':CAP,'maximum_patterns':12653,'cyclotomic_order_bound':512,
     'prime_certificate_list':primes,'control_gram_equalities':len(controls),
     'windows':[],'certified_core_counterexamples':[]}
windows=[(d,2) for d in [2,4,6,8,10]]+[(14,1),(16,1)]
stop=False
for d,H in windows:
    counts={'degree':d,'height_bound':H,'expected_patterns':(2*H+1)**(d//2),
            'enumerated':0,'cyclotomic_divisor_removed':0,'not_squarefree':0,
            'squarefree_survivors':0,'positivity_failures':0,'complete':False}
    best=[]; failures=[]
    for coeff in itertools.product(range(-H,H+1),repeat=d//2):
        if monotonic()-started>=CAP:
            stop=True;break
        p=[0]*(d+1);p[0]=p[-1]=1
        for i,a in enumerate(coeff,1):p[i]=p[d-i]=a
        counts['enumerated']+=1
        counts['last_independent_coefficients']=list(coeff)
        if any(divides(p,f) for _,f in cyclo_small if len(f)<=len(p)):
            counts['cyclotomic_divisor_removed']+=1;continue
        delta=disc(p)
        if delta==0:
            counts['not_squarefree']+=1;continue
        counts['squarefree_survivors']+=1
        G=toeplitz_gram(p);boundary=(2*d)**d;X=delta*G
        assert G>0
        ratio=Fraction(X,boundary)
        record={'coefficients_ascending':p,'discriminant_abs':delta,'gram_2d':G,
                'boundary':boundary,'ratio_numerator':ratio.numerator,
                'ratio_denominator':ratio.denominator,'positivity':X>boundary}
        best.append((ratio,record));best.sort(key=lambda v:(v[0],v[1]['coefficients_ascending']))
        best=best[:8]
        if X<=boundary:
            counts['positivity_failures']+=1
            cert=certify(p);record['certificate']=cert;failures.append(record)
            if cert['status']=='irreducible':
                out['certified_core_counterexamples'].append({'degree':d,**record})
                stop=True;break
    counts['complete']=counts['enumerated']==counts['expected_patterns']
    for _,record in best:
        if 'certificate' not in record:
            record['certificate']=certify(record['coefficients_ascending'])
    counts['smallest_surplus_candidates']=[r for _,r in best]
    counts['failures']=failures
    out['windows'].append(counts)
    if stop:break
out['elapsed_seconds']=round(monotonic()-started,6)
out['stop_reason']=('certified_core_counterexample' if out['certified_core_counterexamples']
                    else 'time_cap' if stop else 'finite_scope_complete')
out['enumerated_total']=sum(w['enumerated'] for w in out['windows'])
print(json.dumps(out,indent=2))
