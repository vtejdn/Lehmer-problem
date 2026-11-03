"""Declared binary obstruction and complete finite-field positive-basis tests."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
from collections import Counter
import time,json
import sympy as sp
from terminal import V0,cg,mul,tr,eye,norm

def field_run(p):
    start=time.perf_counter();counts=Counter();seen=set();stop=None
    def recurse(v):
        nonlocal stop
        if counts['calls']>=200000:stop='node_cap';return None
        if time.perf_counter()-start>120:stop='runtime_cap';return None
        counts['calls']+=1;n=len(v);counts[f'dimension_{n}']+=1
        key=tuple(map(tuple,v))
        if key in seen:counts['duplicates']+=1;return None
        seen.add(key)
        if n==1:return [[1]] if v==[[1]] else None
        roots=[x for x in product(range(p),repeat=n) if any(x) and next(a for a in x if a)==1 and norm(v,x)%p==1]
        roots.sort(key=lambda x:(sum(a!=0 for a in x),x))
        counts['permitted_roots']+=len(roots)
        for x in roots:
            r=next(i for i,a in enumerate(x) if a);q=tr([list(x)]+[[int(i==j) for i in range(n)] for j in range(n) if j!=r]);s=cg(v,q)
            assert s[0][0]%p==1
            for j in range(1,n):
                z=s[j][0]%p
                for i in range(n):q[i][j]=(q[i][j]-z*q[i][0])%p
            s=[[a%p for a in row] for row in cg(v,q)]
            assert s[0][0]==1 and all(s[i][0]==0 for i in range(1,n))
            child=recurse([row[1:] for row in s[1:]])
            if child is not None:
                block=eye(n)
                for i in range(1,n):
                    for j in range(1,n):block[i][j]=child[i-1][j-1]
                return [[a%p for a in row] for row in mul(q,block)]
            if stop:return None
        return None
    q=recurse([[x%p for x in row] for row in V0])
    out=dict(prime=p, node_cap=200000, counts=dict(counts), stop_reason=stop, found=q is not None, complete_failure=q is None and stop is None)
    if q is not None:
        det=int(sp.Matrix(q).det())%p;assert det!=0
        v=[[a%p for a in row] for row in cg(V0,q)]
        assert all(v[i][i]==1 for i in range(6)) and all(v[i][j]==0 for i in range(6) for j in range(i))
        t=sp.Symbol('t');V=sp.Matrix(v);poly=sp.Poly((t*V+V.T).det(method='domain-ge'),t)
        coeff=[int(a)%p for a in poly.all_coeffs()][::-1];assert coeff==[a%p for a in [1,-2,1,-1,1,-2,1]]
        out.update(basis=q,basis_determinant_modp=det,upper_matrix=v,full_polynomial_modp=coeff)
    return out
def run():
    data=json.loads((_J_OUTPUT / 'terminal_result.json').read_text());rows=[];counts=Counter()
    for row in data['terminals']:
        v=row['form'];found=None
        for mod in range(2,25):
            values=sorted({norm(v,x)%mod for x in product(range(mod),repeat=2)})
            if 1 not in values:found=dict(modulus=mod,represented_residues=values);counts[str(mod)]+=1;break
        rows.append(dict(form=v,certificate=found))
    return dict(binary_scope=dict(forms=89,moduli=list(range(2,25))),binary_obstruction_counts=dict(counts),binary_obstructions=rows,field_tests=[field_run(2),field_run(3)])
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'congruence_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='binary_obstructions'}))
