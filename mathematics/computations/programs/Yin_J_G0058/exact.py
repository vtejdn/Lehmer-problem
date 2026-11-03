"""Fixed actual first root, thirty positions, unrestricted second-root polynomials."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
from collections import Counter
import json, time
import sympy as sp

H=sp.Matrix([[2,-1,0,0,0,0],[-1,2,-1,-2,0,2],[0,-1,2,1,-2,-2],[0,-2,1,2,1,-2],[0,0,-2,1,2,1],[0,2,-2,-2,1,2]])
C=sp.Matrix([-1,0,1,1,0,1])
X=sp.symbols('d0:6')
N=sp.expand((sp.Matrix(X).T*H*sp.Matrix(X))[0]/2)

def pf(g,ids=tuple(range(6))):
    if not ids:return sp.Integer(1)
    return sp.expand(sum((-1)**(k+1)*g[ids[0],j]*pf(g,ids[1:k]+ids[k+1:]) for k,j in enumerate(ids[1:],1)))

def model(i,j):
    q=sp.eye(6);q[:,i]=C;q[:,j]=sp.Matrix(X)
    g=q.T*H*q
    v=sp.eye(6)
    for k in range(6):
        for l in range(k+1,6):v[k,l]=g[k,l]
    inv=sp.eye(6)
    for k in range(5,-1,-1):
        for l in range(k+1,6):inv[k,l]=sp.expand(-sum(v[k,h]*inv[h,l] for h in range(k+1,l+1)))
    a=sp.expand(6+sum(inv[k,l]*v[k,l] for k in range(6) for l in range(k+1,6)))
    ell=sp.expand(C[i]*X[j]-C[j]*X[i]);p=pf(g)
    assert sp.Poly(a,X).total_degree()<=2
    assert sp.Poly(p,X).total_degree()<=1
    assert sp.expand(q.det()-ell)==0
    assert all(sp.expand(z)==0 for z in v*inv-sp.eye(6))
    return {'ell':ell,'pf':p,'norm_half':N,'first':a}

def terms(expr,variables=X):
    return [[int(co),list(mon)] for mon,co in sp.Poly(expr,variables).terms()]

def evaluator(expr,variables=X):
    ts=[(int(co),tuple(k for k,e in enumerate(mon) for _ in range(e))) for mon,co in sp.Poly(expr,variables).terms()]
    def ev(row):
        ans=0
        for co,indices in ts:
            z=co
            for k in indices:z*=row[k]
            ans+=z
        return ans
    return ev

def run():
    start=time.perf_counter();records=[]
    assert (C.T*H*C)[0]==2 and H.det()==-1
    residues=list(product(range(4),repeat=6))
    for i in range(6):
        for j in range(6):
            if i==j:continue
            if time.perf_counter()-start>120:raise RuntimeError('Declared 120-second cap reached; no complete output published')
            m=model(i,j);f={k:evaluator(v) for k,v in m.items()};counts=Counter();surv={'F':[],'S6':[]}
            for row in residues:
                counts['residue_vectors']+=1
                if f['ell'](row)%4 not in (1,3):continue
                counts['unit_minor']+=1
                if f['pf'](row)%4 not in (1,3):continue
                counts['odd_pfaffian']+=1
                if f['norm_half'](row)%4!=1:continue
                counts['norm_two']+=1
                a=f['first'](row)%4
                if a==2:surv['F'].append(list(row))
                if a==0:surv['S6'].append(list(row))
            records.append(dict(positions=[i,j],formulas={k:str(v) for k,v in m.items()},terms={k:terms(v) for k,v in m.items()},linear_rank=int(sp.Matrix([[sp.diff(m[k],x) for x in X] for k in ('ell','pf')]).rank()),counts=dict(counts),survivors=surv))
    return dict(scope=dict(fixed_first_root=list(map(int, C)), unchanged_columns='other four standard path-coordinate columns', order='positions 0 through 5 unchanged', ordered_positions=30, modulus=4, residue_vectors_per_position=4096), models=records, total_survivors={k: sum((len(r['survivors'][k]) for r in records)) for k in ('F', 'S6')})

if __name__=='__main__':
    result=run();(_J_OUTPUT / 'mod4_result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='models'}))
    print(json.dumps([{'positions':r['positions'],'rank':r['linear_rank'],'survivors':{k:len(v) for k,v in r['survivors'].items()}} for r in result['models']]))
