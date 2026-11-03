"""Complete binary terminal solve after declared bounded positive-pivot prefixes."""
from itertools import product
from math import isqrt,gcd
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import Counter
import json,time
import sympy as sp

V0=[[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],[2,1,0,2,1,1],
    [0,-1,-1,0,-1,0],[1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]]
# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def tr(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def cg(a,q):return mul(mul(tr(q),a),q)
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def norm(a,x):return sum(x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def egcd(a,b):
    if not b:return abs(a),1 if a>=0 else -1,0
    g,x,y=egcd(b,a%b);return g,y,x-(a//b)*y
def binary(form):
    a,b=form[0];c,d=form[1];assert a*d-b*c==1
    swap=False
    if a==0:
        if d==0:return dict(kind='zero_quadratic',solution=None,form=form)
        a,b,c,d=d,c,b,a;swap=True
    h=b+c;k=b-c;delta=k*k-4
    ans=None;tested=0;bound=None
    if delta<0:
        kind='positive_definite' if a>0 else 'negative_definite'
        ys=range(-isqrt((4*a)//(-delta)),isqrt((4*a)//(-delta))+1) if a>0 else []
    elif delta==0:
        kind='semidefinite';ys=[]
        if a>0:
            rt=isqrt(4*a)
            if rt*rt==4*a:
                g,s,_=egcd(h,2*a)
                for u in sorted({rt,-rt}):
                    if u%g==0:
                        y=s*(u//g);ans=[(u-h*y)//(2*a),y];break
    else:
        kind='indefinite';bound=isqrt(4*abs(a))+1;ys=range(-bound,bound+1)
    for y in ys:
        tested+=1;rad=delta*y*y+4*a
        if rad<0:continue
        rt=isqrt(rad)
        if rt*rt!=rad:continue
        for u in sorted({rt,-rt}):
            if (u-h*y)%(2*a)==0:
                ans=[(u-h*y)//(2*a),y];break
        if ans is not None:break
    if ans is not None:
        if swap:ans=ans[::-1]
        assert norm(form,ans)==1 and gcd(*ans)==1
    return dict(form=form,kind=kind,swapped=swap,discriminant=delta,bound=bound,y_values_tested=tested,solution=ans)
def binary_basis(form,v):
    g,s,t=egcd(*v);assert g==1
    q=[[v[0],-t],[v[1],s]];a=cg(form,q);coeff=a[1][0]
    for i in range(2):q[i][1]-=coeff*q[i][0]
    out=cg(form,q);assert out[0][0]==out[1][1]==1 and out[1][0]==0
    assert q[0][0]*q[1][1]-q[0][1]*q[1][0]==1
    return q
def costs(q):
    t=sp.Symbol('t');Q=sp.Matrix(q);v=Q.T*sp.Matrix(V0)*Q;n=6
    assert abs(Q.det())==1 and all(v[i,i]==1 for i in range(n))
    assert all(v[i,j]==0 for i in range(n) for j in range(i))
    f=t**6-2*t**5+t**4-t**3+t**2-2*t+1
    p=sp.expand((t*v+v.T).det(method='domain-ge'));assert p==f
    bm=sp.eye(6)
    for i in range(n):
        for j in range(i+1,n):bm[i,j]=-abs(v[i,j])
    pb=sp.expand((t*bm+bm.T).det(method='domain-ge'));w=sp.eye(12)
    for i in range(n):
        for j in range(i+1,n):
            x=int(v[i,j])
            for s in range(2):w[2*i+s,2*j+(s if x<=0 else 1-s)]=-abs(x)
    pw=sp.expand(p*pb)
    for t0 in range(-6,7):assert (t0*w+w.T).det(method='domain-ge')==pw.subs(t,t0)
    co=lambda z:[int(a) for a in sp.Poly(z,t).all_coeffs()][::-1]
    return dict(basis=q,basis_determinant=int(Q.det()),matrix=v.tolist(),absolute=bm.tolist(),cover=w.tolist(),original_polynomial=co(p),absolute_polynomial=co(pb),full_cover_polynomial=co(pw),absolute_factorization=str(sp.factor(pb)),height=max(abs(int(x)) for x in v),energy=sum(int(v[i,j])**2 for i in range(6) for j in range(i+1,6)),cover_energy=sum(int(w[i,j])**2 for i in range(12) for j in range(i+1,12)),rank=6,cover_rank=12,cover_scalar_checks=13)
def run():
    start=time.perf_counter();counts=Counter();seen=set();terminals=[];stop=None
    t=sp.Symbol('t');s=sp.Matrix(V0)
    assert s.det()==1 and sp.expand((t*s+s.T).det())==t**6-2*t**5+t**4-t**3+t**2-2*t+1
    def recurse(form,path):
        nonlocal stop
        if counts['calls']>=20000:stop='node_cap';return None
        if time.perf_counter()-start>120:stop='runtime_cap';return None
        counts['calls']+=1;n=len(form);counts[f'dimension_{n}']+=1
        key=tuple(map(tuple,form))
        if key in seen:counts['duplicate_forms']+=1;return None
        seen.add(key)
        if n==2:
            ans=binary(form);ans['prefix']=path;terminals.append(ans);counts['binary_'+ans['kind']]+=1
            if ans['solution'] is not None:return binary_basis(form,ans['solution']),path+[ans['solution']]
            return None
        roots=[x for x in product((-1,0,1),repeat=n) if any(x) and next(a for a in x if a)>0 and norm(form,x)==1]
        roots.sort(key=lambda x:(sum(abs(a) for a in x),x));counts['permitted_prefix_pivots']+=len(roots)
        if not roots:counts['no_small_prefix_pivot']+=1
        for x in roots:
            r=next(i for i,a in enumerate(x) if a);assert x[r]==1
            q=tr([list(x)]+[[int(i==j) for i in range(n)] for j in range(n) if j!=r]);s=cg(form,q)
            assert s[0][0]==1
            for j in range(1,n):
                z=s[j][0]
                for i in range(n):q[i][j]-=z*q[i][0]
            s=cg(form,q);assert s[0][0]==1 and all(s[j][0]==0 for j in range(1,n))
            answer=recurse([row[1:] for row in s[1:]],path+[list(x)])
            if answer:
                z,pivots=answer;embed=eye(n)
                for i in range(1,n):
                    for j in range(1,n):embed[i][j]=z[i-1][j-1]
                return mul(q,embed),pivots
            if stop:return None
        return None
    answer=recurse(V0,[])
    out=dict(scope=dict(prefix_dimensions=[6,5,4,3],prefix_cube=[-1,1],terminal_dimension=2,terminal_domain='all integer vectors; exact arithmetic criterion',node_cap=20000),initial_matrix=V0,counts=dict(counts),terminals=terminals,stop_reason=stop,found=bool(answer),tree_complete=answer is None and stop is None,elapsed_search_seconds=time.perf_counter()-start)
    if answer:out.update(pivot_word=answer[1],actual_realization=costs(answer[0]))
    return json.loads(json.dumps(out,default=int))
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'terminal_result.json').write_text(_record_text(json.dumps(out,indent=2)+'\n'),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['terminals','actual_realization']}))
    if out['found']:print(json.dumps(out['actual_realization']))
