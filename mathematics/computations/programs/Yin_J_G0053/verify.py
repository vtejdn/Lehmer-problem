"""Exact mathematical certificate checks, not another heuristic target scan."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import json
import sympy as sp

BASE=(_J_PROGRAM / 'verify.py').parent
data=json.loads(((_J_OUTPUT / 'search_result.json')).read_text(encoding='utf-8'))
N=6
G0=sp.Matrix(data['seed_gram'])
C=G0-2*sp.eye(N)
assert C*C==5*sp.eye(N) and sp.trace(C)==0 and G0.det()==-1
Q=sp.eye(N)
G=G0
for kind,i,j in data['selected_steps']:
    R=sp.eye(N)
    if kind=='swap':
        R.col_swap(i,j)
    else:
        R[j,i]=-G[i,j]
    assert R.det() in (-1,1)
    Q=Q*R; G=R.T*G*R
    assert list(G.diagonal())==[2]*N
assert Q==sp.Matrix(data['integral_basis']) and G==sp.Matrix(data['gram'])
V=sp.eye(N)
Vm=sp.eye(N)
W=sp.eye(2*N)
for i in range(N):
    for j in range(i+1,N):
        a=int(G[i,j]); V[i,j]=a; Vm[i,j]=-abs(a)
        if a<=0:
            W[2*i,2*j]=W[2*i+1,2*j+1]=a
        else:
            W[2*i,2*j+1]=W[2*i+1,2*j]=-a
t,u=sp.symbols('t u')
p=sp.Poly((t*V+V.T).det(),t)
pm=sp.Poly((t*Vm+Vm.T).det(),t)
assert [int(v) for v in p.all_coeffs()]==data['polynomial_descending']
assert [int(v) for v in pm.all_coeffs()]==data['absolute_polynomial_descending']
# Independent full 12-degree determinant via exact integer interpolation.
for k in range(13):
    assert (k*W+W.T).det()==p.eval(k)*pm.eval(k)
assert [int(v) for v in (p*pm).all_coeffs()]==data['cover_polynomial_descending']
q=sp.Poly(u**3-3*u**2-2*u+7,u)
qm=sp.Poly(u**3-37*u**2-54*u+23,u)
assert sp.expand(t**3*q.as_expr().subs(u,t+1/t))==p.as_expr()
assert sp.expand(t**3*qm.as_expr().subs(u,t+1/t))==pm.as_expr()
# Complete real-root isolation; intervals identify every quadratic factor's cost.
q_intervals=q.intervals(eps=sp.Rational(1,100000))
qm_intervals=qm.intervals(eps=sp.Rational(1,100000))
assert len(q_intervals)==len(qm_intervals)==3
assert all(mult==1 for _,mult in q_intervals+qm_intervals)
def interval_record(rows):
    return [[[str(a),str(b)],mult] for (a,b),mult in rows]
# All 64 binary vectors are checked against the explicit even-weight model.
for x in product((0,1),repeat=6):
    col=sp.Matrix(x)
    image=(sum(x)%2,)+x
    assert sum(image)%2==0
    assert int((col.T*G0*col)[0]//2)%2==(sum(image)//2)%2
# An independently enumerated short-root diagnostic, no target basis search.
short_roots=[]
for x in product((-1,0,1),repeat=6):
    col=sp.Matrix(x)
    if (col.T*G0*col)[0]==2:
        binary=tuple(v%2 for v in x)
        image=(sum(binary)%2,)+binary
        short_roots.append({'coordinates':list(x),'mod2_weight':sum(image)})
outside=[row for row in short_roots if row['mod2_weight']==6]
out={'passed':True,'seed_square_identity':True,
     'replayed_basis_steps':len(data['selected_steps']),'basis_determinant':int(Q.det()),
     'gram_determinant':int(G.det()),'full_cover_determinant_points':13,
     'trace_polynomial':str(q.as_expr()),'absolute_trace_polynomial':str(qm.as_expr()),
     'trace_root_intervals':interval_record(q_intervals),
     'absolute_trace_root_intervals':interval_record(qm_intervals),
     'binary_quadratic_model_vectors':64,'short_root_cube_size':729,
     'short_root_count':len(short_roots),'exceptional_weight_six_short_roots':outside,
     'all_short_roots':short_roots}
((_J_OUTPUT / 'verification.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('passed','replayed_basis_steps','basis_determinant','trace_root_intervals','absolute_trace_root_intervals','short_root_count','exceptional_weight_six_short_roots')}))
