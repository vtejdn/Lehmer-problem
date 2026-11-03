"""Different exact author calculation: scalar determinants and coefficient interpolation."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations,permutations
import json

H=[[2,-1,0,0,0,0],[-1,2,-1,-2,0,2],[0,-1,2,1,-2,-2],[0,-2,1,2,1,-2],[0,0,-2,1,2,1],[0,2,-2,-2,1,2]]
C=[-1,0,1,1,0,1]
E=[[int(i==j) for i in range(6)] for j in range(6)]
def dot(x,y):return sum(x[i]*H[i][j]*y[j] for i in range(6) for j in range(6))
def bareiss(a):
    a=[r[:] for r in a];sgn=1;prev=1;n=len(a)
    for k in range(n-1):
        if not a[k][k]:
            q=next((j for j in range(k+1,n) if a[j][k]),None)
            if q is None:return 0
            a[k],a[q]=a[q],a[k];sgn=-sgn
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*p-a[i][k]*a[k][j];assert z%prev==0;a[i][j]=z//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sgn*a[-1][-1]
def basis(i,j,d):
    cols=[e[:] for e in E];cols[i]=C[:];cols[j]=list(d)
    g=[[dot(x,y) for y in cols] for x in cols]
    v=[[int(k==l)+(g[k][l] if k<l else 0) for l in range(6)] for k in range(6)]
    return cols,g,v
def value(v,t):return bareiss([[t*v[i][j]+v[j][i] for j in range(len(v))] for i in range(len(v))])
def poly(v):
    e,u,w=value(v,1),value(v,2),value(v,3)
    z=w-9*u-235+45*e;assert z%30==0;a=z//30
    z=u-49-8*e-18*a;assert z%4==0;b=z//4
    p=[1,a,b,e-2-2*a-2*b,b,a,1]
    for t in (-2,0,4):assert value(v,t)==sum(q*t**k for k,q in enumerate(p))
    return p

MATCH={}
for p in permutations(range(6)):
    sign=(-1)**sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))
    pairs=[]
    for k in (0,2,4):
        a,b=p[k:k+2]
        if a>b:a,b=b,a;sign=-sign
        pairs.append((a,b))
    key=tuple(sorted(pairs));MATCH[key]=MATCH.get(key,0)+sign
assert len(MATCH)==15 and all(abs(z)==48 for z in MATCH.values())
def pf(v):return sum((sign//48)*v[a][b]*v[c][d]*v[e][f] for ((a,b),(c,d),(e,f)),sign in MATCH.items())
def values(i,j,d):
    cols,g,v=basis(i,j,d)
    return dict(ell=bareiss(list(map(list,zip(*cols)))),pf=pf(v),norm_half=dot(d,d)//2,first=poly(v)[1])
def fit(samples):
    z=(0,)*6;f0=samples[z];out={z:f0};diag={}
    for k in range(6):
        e=tuple(E[k]);tw=tuple(2*x for x in e);q=samples[tw]-2*samples[e]+f0;assert q%2==0;diag[k]=q//2
        out[e]=samples[e]-f0-diag[k];out[tw]=diag[k]
    for i,j in combinations(range(6),2):
        u=tuple(E[i][k]+E[j][k] for k in range(6));out[u]=samples[u]-samples[tuple(E[i])]-samples[tuple(E[j])]+f0
    return {k:v for k,v in out.items() if v}
def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def control(i,j,d):
    cols,g,v=basis(i,j,d);q=list(map(list,zip(*cols)))
    assert abs(bareiss(q))==1 and all(g[k][k]==2 for k in range(6)) and bareiss(g)==-1
    vm=[[int(k==l)-(abs(v[k][l]) if k<l else 0) for l in range(6)] for k in range(6)]
    p,pm=poly(v),poly(vm);w=[[int(k==l) for l in range(12)] for k in range(12)]
    for k in range(6):
        for l in range(k+1,6):
            for h in range(2):w[2*k+h][2*l+(h if v[k][l]<=0 else 1-h)]=-abs(v[k][l])
    total=conv(p,pm)
    for t in range(-6,7):assert value(w,t)==sum(a*t**k for k,a in enumerate(total))
    assert (p[1]+p[2])%4==1 if p[1]%2==0 else True
    return dict(positions=[i,j],second_root=d,basis_path_coordinates=q,gram=g,matrix=v,original_polynomial=p,absolute_polynomial=pm,full_cover_polynomial=total,height=max(abs(x) for row in v for x in row),energy=sum(v[k][l]**2 for k in range(6) for l in range(k+1,6)),cover_height=max(abs(x) for row in w for x in row),cover_energy=sum(w[k][l]**2 for k in range(12) for l in range(k+1,12)))
def run():
    src=json.loads((_J_OUTPUT / 'mod4_result.json').read_text(encoding='utf-8'));nodes=[(0,)*6]+[tuple(e) for e in E]+[tuple(2*x for x in e) for e in E]+[tuple(E[i][k]+E[j][k] for k in range(6)) for i,j in combinations(range(6),2)]
    assert len(nodes)==28;count=0
    for row in src['models']:
        i,j=row['positions'];samples={x:values(i,j,x) for x in nodes}
        for key,terms in row['terms'].items():
            actual=fit({x:z[key] for x,z in samples.items()});wanted={tuple(mon):co for co,mon in terms if co};assert actual==wanted;(count:=count+1)
    controls=[control(2,0,[1,0,0,0,0,0]),control(0,1,[0,1,2,1,0,1])]
    return dict(passed=True,exact_polynomial_models_compared=count,full_determinant_interpolation_nodes=30*28,scalar_degree6_determinant_checks=30*28*6,signed_pfaffian_method='15 terms collected independently from all720 alternating permutations',complete_cover_polynomials=2,scalar_cover_evaluations=26,controls=controls)
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='controls'}))
