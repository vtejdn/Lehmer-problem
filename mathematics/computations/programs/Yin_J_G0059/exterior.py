"""Exact exterior-square target form and a declared bounded integer triangularization."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations,product
from collections import Counter
import json,time
import sympy as sp

def transpose(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def congruence(v,q):return mul(mul(transpose(q),v),q)
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def norm(v,x):return sum(x[i]*v[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def canonical(x):return next(a for a in x if a)>0
def run():
    start=time.perf_counter();t=sp.Symbol('t');a=sp.Matrix([[0,0,0,-1],[1,0,0,1],[0,1,0,-2],[0,0,1,2]])
    ids=list(combinations(range(4),2));g=sp.zeros(6)
    for x,y,s in [(0,5,1),(1,4,-1),(2,3,1)]:g[x,y]=g[y,x]=s
    c=sp.Matrix(6,6,lambda i,j:a.extract(ids[i],ids[j]).det())
    f=t**6-2*t**5+t**4-t**3+t**2-2*t+1
    assert a.det()==1 and c.T*g*c==g and c.charpoly(t).as_expr()==f
    v=g*(sp.eye(6)-c).inv();assert all(x.q==1 for x in v)
    assert v.det()==1 and v+v.T==g and -v.inv()*v.T==c
    assert sp.expand((t*v+v.T).det())==f
    initial=[[int(x) for x in row] for row in v.tolist()]
    counts=Counter();seen=set();dead=[];maxheight=0;stop=None
    def recurse(form,path):
        nonlocal stop,maxheight
        if counts['nodes']>=20000:stop='node_cap';return None
        if time.perf_counter()-start>120:stop='runtime_cap';return None
        counts['nodes']+=1;n=len(form);counts[f'dimension_{n}']+=1
        maxheight=max(maxheight,max(abs(x) for row in form for x in row))
        key=tuple(map(tuple,form))
        if key in seen:counts['duplicate_forms']+=1;return None
        seen.add(key)
        if n==1:
            if form==[[1]]:return eye(1),path
            counts['nonpositive_last_pivot']+=1;return None
        roots=[x for x in product((-1,0,1),repeat=n) if any(x) and canonical(x) and norm(form,x)==1]
        roots.sort(key=lambda x:(sum(abs(a) for a in x),x));counts['tested_norm_one_pivots']+=len(roots)
        if not roots:
            counts['no_small_norm_one_pivot']+=1
            if len(dead)<20:dead.append(dict(form=form,path=path))
        for x in roots:
            r=next(i for i,a in enumerate(x) if a)
            assert x[r]==1
            cols=[list(x)]+[[int(i==j) for i in range(n)] for j in range(n) if j!=r]
            q=transpose(cols);s=congruence(form,q);assert s[0][0]==1
            for j in range(1,n):
                coeff=s[j][0]
                for i in range(n):q[i][j]-=coeff*q[i][0]
            s=congruence(form,q);assert s[0][0]==1 and all(s[j][0]==0 for j in range(1,n))
            child=recurse([row[1:] for row in s[1:]],path+[list(x)])
            if child:
                z,pivots=child;block=eye(n)
                for i in range(1,n):
                    for j in range(1,n):block[i][j]=z[i-1][j-1]
                return mul(q,block),pivots
            if stop:return None
        return None
    answer=recurse(initial,[])
    out=dict(scope=dict(complete_exterior_target='Phi6 P4',pivot_box=[-1,1],sign_normalized=True,node_cap=20000,completion='unit-coordinate primitive completion; left-orthogonal column clearing'),matrix_A=a.tolist(),exterior_C=c.tolist(),pairing_G=g.tolist(),bilinear_V0=initial,initial_polynomial=[int(x) for x in sp.Poly(f,t).all_coeffs()],counts=dict(counts),max_intermediate_entry=maxheight,stop_reason=stop,finite_tree_complete=answer is None and stop is None,found=bool(answer),first20_dead_forms=dead)
    if answer:
        q,pivots=answer;s=congruence(initial,q);sq=sp.Matrix(q);sv=sp.Matrix(s)
        assert abs(sq.det())==1 and all(s[i][i]==1 for i in range(6)) and all(s[i][j]==0 for i in range(6) for j in range(i))
        assert sp.expand((t*sv+sv.T).det())==f
        out.update(basis=q,pivot_word=pivots,triangular_matrix=s,basis_determinant=int(sq.det()),energy=sum(s[i][j]**2 for i in range(6) for j in range(i+1,6)),height=max(abs(x) for row in s for x in row))
    pass
    # SymPy integer objects occur only in the explicitly displayed original matrices.
    return json.loads(json.dumps(out,default=int))
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'exterior_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k in ['found','counts','stop_reason','finite_tree_complete','energy','height','bilinear_V0','triangular_matrix','basis']}))
