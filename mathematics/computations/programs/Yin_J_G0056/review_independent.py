"""Independent exact review of the 18 J56 cases; no author imports."""
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

specs=[]
for a in (3,4,5):
    for j in (1,2,4):specs.append((f"quadratic_a{a}",[1,-a,1],j))
for name,p in [
    ("quartic",[1,-1,-1,-1,1]),
    ("degree_six",[1,-1,0,-1,0,-1,1]),
    ("lehmer",[1,1,0,-1,-1,-1,-1,-1,0,1,1])
]:
    d=len(p)-1
    for j in (d-1,d,2*d-1):specs.append((name,p,j))
retained=json.loads(((_J_OUTPUT / 'verification.json')).read_text(encoding="utf-8"))
assert len(retained["rows"])==len(specs)==18
results=[]
for row,(name,p,j) in zip(retained["rows"],specs):
    assert (row["name"],row["P"],row["j"])==(name,p,j)
    d=len(p)-1;D=d-1;N=2*j+1
    cols=[rem([0]*n+[1],p) for n in range(N)]
    w=[[sum(v[a]*v[b] for v in cols) for b in range(d)] for a in range(d)]
    y=solve(w,cols[j])
    r=[sum(Q(x)*z for x,z in zip(col,y)) for col in cols]
    assert r[j]==sum(x*x for x in r)
    den=lcm(*(x.denominator for x in r))
    raw=[int(den*x) for x in r];c=content(raw)
    f=trim([x//c for x in raw]);q=Q(den,c)
    assert q.denominator==1;q=int(q)
    assert rem(add(f,scale([0]*j+[1],-q)),p)==[0]*d
    pf=mul(p,f);a=pf[:d];b=trim(list(reversed(a)));a=trim(a)
    assert pf==add(a,[0]*N+b)
    z=add([0]+add(mul(deriv(a),b),scale(mul(a,deriv(b)),-1)),scale(mul(a,b),-N))
    cz=content(z);z0=[x//cz for x in z]
    low=next(i for i,x in enumerate(a) if x);high=len(a)-1
    middle=-sum((N+D-2*i)*x*x for i,x in enumerate(a))
    extreme=-(N+D-high-low)*a[high]*a[low]
    assert z[D]==middle and z[-1]==extreme
    assert len(z)-1==D+high-low
    assert next(i for i,x in enumerate(z) if x)==D+low-high
    rz=resultant(p,z);rz0=resultant(p,z0)
    disc=(-1)**(d*(d-1)//2)*resultant(p,deriv(p))
    ra=resultant(p,a);rb=resultant(p,b)
    assert abs(rz)==q**d*abs(disc*rb)
    assert rz==cz**d*rz0 and ra==rb and content(a)==1
    expected={
        "d":d,"N":N,"q":q,"centered_norm_squared":str(r[j]),
        "F":f,"F_degree":len(f)-1,"F_energy":norm2(f),"F_resultant":resultant(p,f),
        "A":a,"B":b,"A_energy":norm2(a),"A_resultant":ra,"B_resultant":rb,
        "discriminant":disc,"Z":z,"Z_content":cz,"Z_primitive":z0,
        "Z_degree":len(z)-1,"Z_primitive_energy":norm2(z0),"Z_resultant":rz,
        "Z_primitive_resultant":rz0,"Z_middle":middle,"Z_leading":extreme,
        "net_margin_sign":sign(rz0**2-norm2(z0)**d),"all_exact_checks_passed":True
    }
    for key,value in expected.items():assert row[key]==value,(name,j,key,row[key],value)
    assert expected["net_margin_sign"]==-1
    results.append({"name":name,"j":j,"checked_fields":len(expected),"passed":True})
out={'scope': 'Independent row-space projection and quotient-ring determinant check of exactly18 declared cases', 'cases': results, 'all_passed': True, 'author_imports': False}
target=(_J_OUTPUT / 'review_result.json')
assert not target.exists(),"Preserve existing reviewer output; redirect writes for replay"
target.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({'all_passed': True, 'cases': len(results)}))

