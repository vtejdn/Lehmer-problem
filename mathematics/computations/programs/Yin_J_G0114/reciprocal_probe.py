from pathlib import Path
import itertools, json, sys
from math import isqrt
draft=Path('mathematics/ledger/Yin_L_G0004_v1.md')
first=draft.read_text(encoding='utf-8').split('```python\n',1)[1].split('\n```',1)[0]
exec(first.split('\ninputs=',1)[0],globals())

def trim(f):
    while len(f)>1 and f[-1]==0: f.pop()
    return f

def remmod(f,g,q):
    f=trim([a%q for a in f]); g=trim([a%q for a in g])
    inv=pow(g[-1],-1,q)
    while len(f)>=len(g) and f!=[0]:
        c=f[-1]*inv%q; shift=len(f)-len(g)
        for j,a in enumerate(g): f[shift+j]=(f[shift+j]-c*a)%q
        trim(f)
    return f

def mulmod(f,g,p,q):
    h=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g): h[i+j]=(h[i+j]+a*b)%q
    return remmod(h,p,q)

def powmod(f,n,p,q):
    z=[1]
    while n:
        if n&1: z=mulmod(z,f,p,q)
        f=mulmod(f,f,p,q); n//=2
    return z

def gcdmod(f,g,q):
    while g!=[0]: f,g=g,remmod(f,g,q)
    return trim(f)

def irreducible_mod(p,q):
    d=len(p)-1; x=[0,1]; u=x
    divisors=[ell for ell in range(2,d+1)
              if d%ell==0 and all(ell%j for j in range(2,isqrt(ell)+1))]
    checks={d//ell for ell in divisors}
    for j in range(1,d+1):
        u=powmod(u,q,p,q)
        if j in checks:
            diff=u+[0]*max(0,2-len(u)); diff[1]=(diff[1]-1)%q
            if len(gcdmod(p,trim(diff),q))!=1: return False
    return trim(u)==x

def divexact(f,g):
    f=f[:]; out=[0]*(len(f)-len(g)+1)
    while len(f)>=len(g) and f!=[0]:
        assert f[-1]%g[-1]==0
        c=f[-1]//g[-1]; shift=len(f)-len(g); out[shift]=c
        for j,a in enumerate(g): f[shift+j]-=c*a
        trim(f)
    assert f==[0]
    return trim(out)

cyclo={}
for n in range(1,289):
    f=[-1]+[0]*(n-1)+[1]
    for j in range(1,n):
        if n%j==0: f=divexact(f,cyclo[j])
    cyclo[n]=f
cyclo_polys={tuple(f):n for n,f in cyclo.items()}
primes=[2,3,5,7,11,13,17,19,23,29,31]
out={'python':sys.version.split()[0],'prime_certificate_list':primes,
     'independent_coefficients':[-1,0,1],'degrees':{},'positivity_failures':[],
     'fixed_threshold_failure_examples':[]}
for d in [2,4,6,8,10,12]:
    counts={'enumerated':0,'modularly_certified':0,'cyclotomic_certified':0,
            'no_modular_certificate':0,'noncyclotomic_certified':0,
            'positivity_failures':0,'fixed_threshold_failures':0}
    for coeff in itertools.product([-1,0,1],repeat=d//2):
        p=[0]*(d+1);p[0]=p[-1]=1
        for i,a in enumerate(coeff,1): p[i]=p[d-i]=a
        counts['enumerated']+=1
        witness=next((q for q in primes if irreducible_mod(p,q)),None)
        if witness is None:
            counts['no_modular_certificate']+=1;continue
        counts['modularly_certified']+=1
        if tuple(p) in cyclo_polys:
            counts['cyclotomic_certified']+=1;continue
        counts['noncyclotomic_certified']+=1
        delta=disc(p);N=2*d;G=gram(p,N);X=delta*G
        assert delta>0 and G>0
        record={'degree':d,'coefficients_ascending':p,'irreducible_mod_prime':witness,
                'N':N,'discriminant_abs':delta,'gram':G,'boundary':N**d}
        if X<=N**d:
            counts['positivity_failures']+=1
            out['positivity_failures'].append(record)
        if X**4<N**(4*d)*2**(N-1):
            counts['fixed_threshold_failures']+=1
            if len(out['fixed_threshold_failure_examples'])<8:
                out['fixed_threshold_failure_examples'].append(record)
    out['degrees'][str(d)]=counts
print(json.dumps(out,indent=2))
