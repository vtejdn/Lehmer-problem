"""Additional exact author certificate; not a noncontributor review."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import permutations, combinations
import json
from search import G,Q0,gram,upper,first,pf

def poly(v):
    n=len(v);dp={0:[1]}
    for mask in range(1<<n):
        if mask not in dp:continue
        i=mask.bit_count()
        if i==n:continue
        a=dp[mask]
        for j in range(n):
            if mask>>j&1:continue
            lo,hi=v[j][i],v[i][j]
            if not lo and not hi:continue
            s=-1 if (mask>>(j+1)).bit_count()%2 else 1
            nm=mask|1<<j;b=dp.setdefault(nm,[0]*(i+2))
            for k,x in enumerate(a):b[k]+=s*x*lo;b[k+1]+=s*x*hi
    return dp[(1<<n)-1]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def bareiss(a):
    a=[r[:] for r in a];n=len(a);prev=1;sgn=1
    for k in range(n-1):
        if a[k][k]==0:
            q=next((q for q in range(k+1,n) if a[q][k]),None)
            if q is None:return 0
            a[k],a[q]=a[q],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j];assert z%prev==0;a[i][j]=z//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]
def cover(v):
    w=[[int(i==j) for j in range(12)] for i in range(12)]
    for i in range(6):
        for j in range(i+1,6):
            a=v[i][j]
            for k in range(2):w[2*i+k][2*j+(k if a<=0 else 1-k)]=-abs(a)
    return w
def run():
    d=(_J_PROGRAM / 'verify.py').parent
    initial=json.loads(((_J_OUTPUT / 'search_result.json')).read_text());ordered=json.loads(((_J_OUTPUT / 'orders_result.json')).read_text());small=json.loads(((_J_OUTPUT / 'smaller_result.json')).read_text())
    assert all(not z['hits'] for z in [initial,ordered,small])
    assert sum(ordered['energy_histogram'].values())==7446
    assert ordered['energy_histogram']==small['energy_histogram']
    assert all(int(a)%4!=2 for a in ordered['coefficient_histogram_given_target_pf'])
    assert all(int(a)%4!=0 for a in small['coefficient_histogram_given_target_pf'])
    roots=initial['roots'];old=[list(c) for c in zip(*Q0)]; samples=[old]; labels=[dict(kind='original_path')]
    for i,j in combinations(range(6),2):
        if len(samples)==3:break
        for r in roots:
            if len(samples)==3:break
            c=[sum(r[k:]) for k in range(6)]
            for s in roots:
                z=[sum(s[k:]) for k in range(6)]
                if abs(c[i]*z[j]-c[j]*z[i])!=1:continue
                if r in [old[i],[-x for x in old[i]]] or s in [old[j],[-x for x in old[j]]]:continue
                cols=[x[:] for x in old];cols[i]=r;cols[j]=s;h=gram(cols)
                if abs(pf(h))!=3:continue
                samples.append(cols);labels.append(dict(positions=[i,j],roots=[r,s],minor=c[i]*z[j]-c[j]*z[i]));break
    assert len(samples)==3
    checks=0;payload=[]
    for cols,label in zip(samples,labels):
        h=gram(cols);q=[list(r) for r in zip(*cols)];assert abs(bareiss(q))==1;assert bareiss(h)==-1
        polys={}
        for order in permutations(range(6)):
            ho=[[h[i][j] for j in order] for i in order];v=upper(ho)
            vm=[[int(i==j)-abs(v[i][j]) if i<j else int(i==j) for j in range(6)] for i in range(6)]
            p,pm=poly(v),poly(vm);assert p==p[::-1] and pm==pm[::-1]
            assert sum(p)==-1 and p[-2]==first(v)
            assert sum(a*(-1)**i for i,a in enumerate(p))==pf(ho)**2
            assert pm[-2]==first(vm)
            k=order.index(0);cyc=order[k:]+order[:k];rev=(0,)+cyc[:0:-1];key=min(cyc,rev)
            pair=(p,pm)
            if key in polys:assert pair==polys[key]
            else:polys[key]=pair
            checks+=2
        assert len(polys)==60
        v=upper(h);vm=[[int(i==j)-abs(v[i][j]) if i<j else int(i==j) for j in range(6)] for i in range(6)]
        w=cover(v);whole=poly(w);assert whole==mul(poly(v),poly(vm))
        for t in range(-6,7):assert bareiss([[t*w[i][j]+w[j][i] for j in range(12)] for i in range(12)])==sum(a*t**i for i,a in enumerate(whole))
        payload.append(dict(label=label,basis=q,gram=h,original_polynomial=poly(v),absolute_polynomial=poly(vm),full_cover_polynomial=whole,energy=sum(v[i][j]**2 for i in range(6) for j in range(i+1,6))))
    return dict(passed=True,full_degree6_polynomial_checks=checks,sample_bases=3,all_orders_per_sample=720,dihedral_classes_per_sample=60,full_degree12_cover_checks=3,independent_scalar_cover_values=39,finite_residue_patterns_verified=True,samples=payload)
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='samples'}))
