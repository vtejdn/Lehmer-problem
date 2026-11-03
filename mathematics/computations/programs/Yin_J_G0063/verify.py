"""Check every retained certificate by direct integer formulas and full costs.

This is an author self-check, not a separately organized independent review.
Completeness of the set is supplied by classify.py and the written reduction.
"""
import json
import time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as sp

N=6
V=[[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],[2,1,0,2,1,1],
   [0,-1,-1,0,-1,0],[1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]]
SELECT=[(i,j) for i in range(6) for j in range(i)]+[(i,i) for i in range(6)]

def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def transpose(a): return [list(x) for x in zip(*a)]
def decode(a): return [[(row>>j)&1 for j in range(6)] for row in a]
def coeff(p,t): return [int(x) for x in sp.Poly(p,t).all_coeffs()][::-1]
def array(a): return [[int(x) for x in row] for row in a.tolist()]

def run():
    started=time.monotonic()
    data=json.loads((_J_OUTPUT / 'classification.json').read_text(encoding='utf-8'))
    assert data['complete'] and data['counts']['processed_upper_forms']==32768
    checked=0
    seen=set()
    ranks={}
    for form in data['forms']:
        u=decode(form['upper_rows'])
        assert all(u[i][j]==int(i==j) for i,j in SELECT)
        masks=[]
        for i,j in SELECT:
            masks.append(sum((((b==i)*u[a][j]+(b==j)*u[i][a])%2)<<(6*a+b)
                             for a in range(6) for b in range(6)))
        for rec in form['bases']:
            key=tuple(rec['Q_rows'])
            assert key not in seen
            seen.add(key)
            q=decode(key)
            b=matmul(matmul(transpose(q),V),q)
            assert [[x%2 for x in row] for row in b]==u
            e=sum((((b[i][j]-int(i==j))//2)%2)<<k for k,(i,j) in enumerate(SELECT))
            assert e==rec['error_bits']
            z=rec['inconsistency_witness']
            lhs=0
            for k,mask in enumerate(masks):
                if (z>>k)&1: lhs ^= mask
            assert lhs==0 and (z&e).bit_count()%2==1
            checked+=1
        ranks[form['linear_rank']]=ranks.get(form['linear_rank'],0)+1
    assert checked==5625==data['counts']['binary_bases']==data['counts']['nonliftable_bases']
    assert len(data['forms'])==375 and data['counts']['liftable_bases']==0
    t=sp.Symbol('t');v=sp.Matrix(V);g=v+v.T
    assert v.det()==1 and g.det()==-1
    assert sp.expand((sp.Matrix(sp.symbols('x0:6')).T*v*sp.Matrix(sp.symbols('x0:6')))[0]) == \
           sp.Symbol('x0')*sp.Symbol('x5')-sp.Symbol('x1')*sp.Symbol('x4')+sp.Symbol('x2')*sp.Symbol('x3')
    original=sp.expand((t*v+v.T).det(method='domain-ge'))
    assert original==sp.expand((t*t-t+1)*(t**4-t**3-t*t-t+1))
    absolute=-v.applyfunc(abs)
    pa=sp.expand((t*absolute+absolute.T).det(method='domain-ge'))
    assert pa==-(t**6-7*t**4-11*t**3-7*t*t+1)
    w=sp.zeros(12)
    for i in range(6):
        for j in range(6):
            x=V[i][j]
            for sheet in range(2):
                w[2*i+sheet,2*j+(sheet if x<=0 else 1-sheet)]=-abs(x)
    cover=sp.expand(original*pa)
    for value in range(-6,7):
        assert (value*w+w.T).det(method='domain-ge')==cover.subs(t,value)
    report={'all_saved_inconsistency_certificates_checked': checked, 'distinct_forms': len(data['forms']), 'linear_rank_distribution': ranks, 'no_new_basis_search': True, 'original_matrix': V, 'symmetric_matrix': array(g), 'absolute_matrix': array(absolute), 'literal_cover_matrix': array(w), 'original_polynomial': coeff(original, t), 'absolute_polynomial': coeff(pa, t), 'literal_cover_polynomial': coeff(cover, t), 'ranks': [int(v.rank()), int(absolute.rank()), int(w.rank())], 'degrees': [int(sp.degree(original, t)), int(sp.degree(pa, t)), int(sp.degree(cover, t))], 'heights': [max((abs(int(x)) for x in a)) for a in [v, absolute, w]], 'whole_squared_entry_sums': [sum((int(x) ** 2 for x in a)) for a in [v, absolute, w]], 'direct_cover_evaluations': 13, 'absolute_coefficient_l1': sum((abs(x) for x in coeff(pa, t)))}
    return report

if __name__=='__main__':
    result=run()
    (_J_OUTPUT / 'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if not k.endswith('matrix')},indent=2))
