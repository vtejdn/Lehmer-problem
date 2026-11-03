"""Independent exact review of the 12 J57 cases; no author imports.
Core Fraction and quotient-ring helpers reuse the coordinator-authored J56 reviewer."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from math import gcd, lcm
from functools import reduce
import json, time, datetime

BASE=(_J_PROGRAM / 'review_independent.py').parent
START=time.monotonic()
def trim(v):
    v=list(v)
    while len(v)>1 and not v[-1]:v.pop()
    return v
def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def scale(a,s):return trim([s*x for x in a])
def deriv(a):return [i*a[i] for i in range(1,len(a))] or [0]
def rem(a,p):
    a=trim(a);d=len(p)-1
    while len(a)>d:
        c=a[-1];shift=len(a)-1-d
        for i,x in enumerate(p):a[shift+i]-=c*x
        a=trim(a)
    return a+[0]*(d-len(a))
def solve(a,b):
    n=len(a);a=[[Q(x) for x in row]+[Q(y)] for row,y in zip(a,b)]
    for i in range(n):
        j=next(j for j in range(i,n) if a[j][i])
        a[i],a[j]=a[j],a[i]
        z=a[i][i];a[i]=[x/z for x in a[i]]
        for j in range(n):
            if j!=i:
                z=a[j][i]
                a[j]=[x-z*y for x,y in zip(a[j],a[i])]
    return [row[-1] for row in a]
def det(a):
    a=[list(row) for row in a];n=len(a);old=1;sgn=1
    if n==0:return 1
    for i in range(n-1):
        piv=next((j for j in range(i,n) if a[j][i]),None)
        if piv is None:return 0
        if piv!=i:a[i],a[piv]=a[piv],a[i];sgn=-sgn
        z=a[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                v=a[j][k]*z-a[j][i]*a[i][k]
                assert v%old==0
                a[j][k]=v//old
        for j in range(i+1,n):a[j][i]=0
        old=z
    return sgn*a[-1][-1]
def resultant(p,f):
    d=len(p)-1
    cols=[rem([0]*j+f,p) for j in range(d)]
    return det([[cols[j][i] for j in range(d)] for i in range(d)])
def content(a):return reduce(gcd,[abs(x) for x in a])
def norm2(a):return sum(x*x for x in a)
def sign(a):return (a>0)-(a<0)


def divide(a,p):
    a=trim(a);d=len(p)-1
    assert p[-1]==1
    out=[0]*max(1,len(a)-d)
    while len(a)>d:
        c=a[-1];shift=len(a)-1-d;out[shift]=c
        for i,x in enumerate(p):a[shift+i]-=c*x
        a=trim(a)
    assert a==[0]
    return trim(out)
def evaluate(p,t):
    ans=0
    for x in reversed(p):ans=ans*t+x
    return ans
def trace_interpolation(p,s):
    # Evaluate at distinct rational t+1/t, rather than triangular coefficient extraction.
    ts=list(range(2,s+3));xs=[Q(t)+Q(1,t) for t in ts]
    vals=[Q(evaluate(p,t),t**s) for t in ts]
    v=solve([[x**i for i in range(s+1)] for x in xs],vals)
    assert all(x.denominator==1 for x in v)
    v=trim([int(x) for x in v])
    # Additional points check the full Laurent identity up to its degree.
    for t in range(s+3,3*s+7):
        assert Q(evaluate(p,t),t**s)==evaluate(v,Q(t)+Q(1,t))
    return v
def center(p,j):
    d=len(p)-1;N=2*j+1
    cols=[rem([0]*n+[1],p) for n in range(N)]
    w=[[sum(v[a]*v[b] for v in cols) for b in range(d)] for a in range(d)]
    y=solve(w,cols[j])
    r=[sum(Q(x)*z for x,z in zip(col,y)) for col in cols]
    assert r[j]==sum(x*x for x in r)
    den=lcm(*(x.denominator for x in r));raw=[int(den*x) for x in r];c=content(raw)
    f=trim([x//c for x in raw]);q=Q(den,c)
    assert q.denominator==1;q=int(q)
    assert rem(add(f,scale([0]*j+[1],-q)),p)==[0]*d
    pf=mul(p,f);a=trim(pf[:d]);b=trim(list(reversed(pf[:d])))
    assert pf==add(a,[0]*N+b) and content(a)==content(b)==1
    return f,a,b,q,str(r[j])

specs=[]
for name,p in [
    ("quartic",[1,-1,-1,-1,1]),
    ("degree_six",[1,-1,0,-1,0,-1,1]),
    ("lehmer",[1,1,0,-1,-1,-1,-1,-1,0,1,1])
]:
    d=len(p)-1
    for j in (d-1,d,2*d-1):specs.append((name,p,j))
for j in (1,4):specs.append(("quadratic_a3",[1,-3,1],j))
specs.append(("radical_a4_q2",[1,0,-4,0,1],4))
retained=json.loads(((_J_OUTPUT / 'verification.json')).read_text(encoding="utf-8"))
assert len(retained["rows"])==len(specs)==12
before={p:p.read_bytes() for p in (*BASE.iterdir(), *_J_OUTPUT.iterdir()) if p.is_file() and p.name in ("readme.md","verify.py","verification.json")}
results=[]
for row,(name,p,j) in zip(retained["rows"],specs):
    assert (row["name"],row["P"],row["j"])==(name,p,j)
    d=len(p)-1
    f,a,b,q,l=center(p,j);fn,an,bn,qn,ln=center(p,j+1)
    h=add(mul(an,b),scale([0,0]+mul(a,bn),-1))
    C=divide(h,p)
    assert C==add(mul(fn,b),scale([0,0]+mul(f,bn),-1))
    expected={"name":name,"P":p,"d":d,"j":j,"N":2*j+1,
        "q":q,"q_next":qn,"centered_norm_squared":l,"next_centered_norm_squared":ln,
        "F":f,"F_next":fn,"A":a,"B":b,"A_next":an,"B_next":bn,"C_zero":C==[0]}
    if C==[0]:
        expected.update(shift_plateau=scale(fn,q)==scale([0]+f,qn),all_exact_checks_passed=True)
    else:
        assert len(C)-1<=d
        formal=C+[0]*(d+1-len(C))
        assert formal==[-x for x in formal[::-1]]
        c=content(C);c0=[x//c for x in C]
        W=add(scale(b,qn),scale([0]+bn,-q))
        assert rem(add(C,scale([0]*(j+1)+W,-1)),p)==[0]*d
        qt=trace_interpolation(p,d//2)
        v=trace_interpolation(divide(C,[-1,0,1]),d//2-1)
        assert content(v)==c
        v0=[x//c for x in v]
        rC=resultant(p,C);rC0=resultant(p,c0);rW=resultant(p,W)
        rQV=resultant(qt,v0)
        cyclic=evaluate(p,1)*evaluate(p,-1)
        assert rC==rW and rC0==cyclic*rQV**2 and rC==c**d*rC0 and rC0!=0
        from math import comb
        integ=mul([4,0,-1],mul(v,v))
        assert sum(x*comb(i,i//2) for i,x in enumerate(integ) if i%2==0)==norm2(C)
        expected.update(C=C,C_degree=len(C)-1,C_content=c,C_primitive=c0,
            C_primitive_energy=norm2(c0),Q=qt,V=v,V_primitive=v0,C_resultant=rC,
            C_primitive_resultant=rC0,trace_resultant=rQV,time_two_resultant=cyclic,
            net_margin_sign=sign(rC0**2-norm2(c0)**d),all_exact_checks_passed=True)
    assert set(expected)==set(row),(name,j,set(expected)^set(row))
    for key,value in expected.items():assert row[key]==value,(name,j,key,row[key],value)
    results.append({"name":name,"j":j,"checked_fields":len(expected),
        "zero":C==[0],"margin_sign":expected.get("net_margin_sign"),"passed":True})
assert all(p.read_bytes()==value for p,value in before.items())
out={'scope': 'Independent row-space projections, quotient-ring determinants and rational trace interpolation for all12 declared pairs', 'cases': results, 'all_passed': True, 'author_imports': False}
target=(_J_OUTPUT / 'review_result.json')
assert not target.exists(),"Preserve existing reviewer output; redirect writes for replay"
target.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({'all_passed': True, 'cases': len(results)}))
