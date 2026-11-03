from fractions import Fraction as F
from math import isqrt
from itertools import product
from pathlib import Path
import argparse, json, subprocess, sys, time

parser=argparse.ArgumentParser(description='Independent exact reconstruction of the original J116 finite scope.')
j_dir=Path(__file__).resolve().parents[1]
root=j_dir.parents[3]
parser.add_argument('--output',type=Path,default=root/'mathematics/computations/outputs'/j_dir.name/'reviewer_exact/result.json')
args=parser.parse_args()
start=time.monotonic(); CAP=180
old=json.loads((j_dir/'original-output.json').read_text(encoding='utf-8'))
assert [(w['degree'],w['height_bound']) for w in old['windows']]==[(2,2),(4,2),(6,2),(8,2),(10,2),(14,1),(16,1)]
assert old['maximum_patterns']==12653 and old['cyclotomic_order_bound']==512 and old['cap_seconds']==180
def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p
def remainder(a,b,q=None):
    a=list(a)
    if q is None: a=list(map(F,a)); b=list(map(F,b))
    else: a=[v%q for v in a]; b=trim([v%q for v in b])
    trim(a)
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b)
        c=a[-1]/b[-1] if q is None else a[-1]*pow(b[-1],-1,q)%q
        for k in range(len(b)): a[k+j]-=c*b[k]
        if q is not None: a=[v%q for v in a]
        trim(a)
    return a
def resultant(a,b):
    a=list(map(F,a)); b=trim(list(map(F,b))); val=F(1)
    while len(b)>1:
        m,n=len(a)-1,len(b)-1
        r=remainder(a,b)
        if r==[0]: return 0
        k=len(r)-1
        val*=(-1)**(m*n)*b[-1]**(m-k)
        a,b=b,r
    val*=b[0]**(len(a)-1)
    assert val.denominator==1
    return val.numerator
def discriminant(p): return abs(resultant(p,[j*p[j] for j in range(1,len(p))]))
def determinant_rational(a):
    a=[list(map(F,row)) for row in a]; ans=F(1)
    for i in range(len(a)):
        row=next((j for j in range(i,len(a)) if a[j][i]),None)
        if row is None:return 0
        if row!=i:a[i],a[row]=a[row],a[i];ans=-ans
        pivot=a[i][i]; ans*=pivot
        for j in range(i+1,len(a)):
            mul=a[j][i]/pivot
            for k in range(i+1,len(a)):a[j][k]-=mul*a[i][k]
    assert ans.denominator==1
    return ans.numerator
def orbit_gram(p):
    d=len(p)-1; cols=[]
    for j in range(2*d):
        cols.append([int(x) for x in remainder([0]*j+[1],p)]+[0]*d)
        cols[-1]=cols[-1][:d]
    return determinant_rational([[sum(c[i]*c[j] for c in cols) for j in range(d)] for i in range(d)])
def phi(n):return sum(__import__('math').gcd(j,n)==1 for j in range(1,n+1))
def mobius(n):
    s=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;s=-s
            if n%p==0:return 0
        while n%p==0:n//=p
        p+=1
    return -s if n>1 else s
def cyclotomic(n):
    if n==1:return [-1,1]
    e=phi(n);v=[1]+[0]*e
    for d in range(1,n+1):
        if n%d:continue
        m=mobius(n//d)
        if m==1:
            for j in range(e,d-1,-1):v[j]-=v[j-d]
        elif m==-1:
            for j in range(d,e+1):v[j]+=v[j-d]
    assert v[-1]==1
    return v
cyclos=[cyclotomic(n) for n in range(1,513) if phi(n)<=16]
def mod_mul(a,b,p,q):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]=(v[i+j]+x*y)%q
    return remainder(v,p,q)
def mod_pow(a,n,p,q):
    v=[1]
    while n:
        if n&1:v=mod_mul(v,a,p,q)
        a=mod_mul(a,a,p,q);n//=2
    return v
def poly_gcd(a,b,q):
    while b!=[0]:a,b=b,remainder(a,b,q)
    return a
def matrix_rank(a,q):
    a=[[x%q for x in row] for row in a];r=0
    for col in range(len(a[0])):
        j=next((i for i in range(r,len(a)) if a[i][col]),None)
        if j is None:continue
        a[r],a[j]=a[j],a[r]; inv=pow(a[r][col],-1,q)
        a[r]=[x*inv%q for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                m=a[i][col];a[i]=[(x-m*y)%q for x,y in zip(a[i],a[r])]
        r+=1
    return r
def berlekamp_irreducible(p,q):
    n=len(p)-1
    if len(poly_gcd(p,trim([j*p[j]%q for j in range(1,len(p))] or [0]),q))!=1:return False
    cols=[]
    for j in range(n):cols.append(mod_pow([0,1],q*j,p,q)+[0]*n)
    mat=[[(cols[j][i]-(i==j))%q for j in range(n)]for i in range(n)]
    return matrix_rank(mat,q)==n-1
# Known tiny values catch sign/reduction conventions without using producer helpers.
assert discriminant([1,-3,1])==5
assert orbit_gram([1,-3,1])==85
assert berlekamp_irreducible([1,1,1],2)
assert not berlekamp_irreducible([1,0,1],2)
summary=[];total=0
for w in old['windows']:
    d,H=w['degree'],w['height_bound']; counts=dict(degree=d,enumerated=0,cyclotomic_divisor_removed=0,not_squarefree=0,squarefree_survivors=0,positivity_failures=0);best=[]
    for co in product(range(-H,H+1),repeat=d//2):
        if time.monotonic()-start>=CAP:raise TimeoutError('Independent reconstruction incomplete at its 180-second cap; no complete result published.')
        p=[0]*(d+1);p[0]=p[-1]=1
        for j,v in enumerate(co,1):p[j]=p[d-j]=v
        counts['enumerated']+=1;total+=1
        if any(len(c)<=len(p) and remainder(p,c)==[0] for c in cyclos):counts['cyclotomic_divisor_removed']+=1;continue
        delta=discriminant(p)
        if delta==0:counts['not_squarefree']+=1;continue
        counts['squarefree_survivors']+=1
        g=orbit_gram(p);assert g>0; boundary=(2*d)**d;ratio=F(delta*g,boundary)
        if delta*g<=boundary:counts['positivity_failures']+=1
        best.append((ratio,p,delta,g));best.sort();best=best[:8]
    for k,v in counts.items():assert v==w[k],(d,k,v,w[k])
    assert len(best)==len(w['smallest_surplus_candidates'])
    for computed,r in zip(best,w['smallest_surplus_candidates']):
        rat,p,delta,g=computed
        assert (p,delta,g,rat.numerator,rat.denominator)==(r['coefficients_ascending'],r['discriminant_abs'],r['gram_2d'],r['ratio_numerator'],r['ratio_denominator'])
        c=r['certificate'];assert c['status']=='irreducible'
        if 'direct_prime'in c:assert berlekamp_irreducible(p,c['direct_prime'])
        else:
            Q=c['trace']; assert berlekamp_irreducible(Q,c['trace_prime'])
            # Independently reconstruct t^m Q(t+t^-1) as a Laurent convolution.
            m=d//2;seq={0:1};acc={}
            for a in Q:
                for exp,v in seq.items():acc[exp+m]=acc.get(exp+m,0)+a*v
                new={}
                for exp,v in seq.items():
                    new[exp-1]=new.get(exp-1,0)+v;new[exp+1]=new.get(exp+1,0)+v
                seq=new
            assert [acc.get(j,0) for j in range(d+1)]==p
            l,rgt=map(F,c['bracket'])
            def ev(x):return sum(F(a)*x**j for j,a in enumerate(Q))
            assert -2<l==rgt<2 and ev(l)==0 or -2<=l<rgt<=2 and ev(l)*ev(rgt)<0
    counts['candidate_certificates_checked']=len(best)
    counts['minimum_ratio']=([best[0][0].numerator,best[0][0].denominator] if best else None)
    counts['minimizer_ascending']=(best[0][1] if best else None)
    summary.append(counts)
    print(json.dumps(dict(progress_degree=d,elapsed=time.monotonic()-start)),flush=True)
remaining=CAP-(time.monotonic()-start)
if remaining<=0:raise TimeoutError('Native replay not reached within the reviewer cap; no complete result published.')
native=subprocess.run([sys.executable,str(j_dir/'countersearch.py')],cwd=root,text=True,encoding='utf-8',capture_output=True,check=True,timeout=remaining)
replayed=json.loads(native.stdout)
volatile={'python','started_utc','elapsed_seconds'}
assert {k:v for k,v in old.items() if k not in volatile}=={k:v for k,v in replayed.items() if k not in volatile}
assert replayed['stop_reason']=='finite_scope_complete' and replayed['enumerated_total']==12653
report=dict(cap_seconds=CAP,complete=True,enumerated_total=total,python=sys.version.split()[0],elapsed_seconds=time.monotonic()-start,windows=summary,native_nonvolatile_fields_match=True,native_elapsed_seconds=replayed['elapsed_seconds'],candidate_certificates_checked=sum(w['candidate_certificates_checked'] for w in summary),algorithm='independent Mobius cyclotomics; rational Euclidean resultants; orbit remainder Gram with rational Gaussian determinant; Berlekamp certificate verification')
args.output.parent.mkdir(parents=True,exist_ok=True)
temporary=args.output.with_suffix(args.output.suffix+'.new')
temporary.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
temporary.replace(args.output)
print(json.dumps(report),flush=True)


