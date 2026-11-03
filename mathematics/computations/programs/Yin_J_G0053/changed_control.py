"""Exact certificate of a selected changed-partition, unpadded Salem control."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp

BASE=(_J_PROGRAM / 'changed_control.py').parent
seed=json.loads(((_J_OUTPUT / 'search_result.json')).read_text(encoding='utf-8'))['seed_gram']
G0=sp.Matrix(seed);Q=sp.eye(6)
for i in range(1,6):Q[i-1,i]=-1
Q[:,2]=sp.Matrix([-1,-1,0,1,-1,1])
assert Q.det()==1
G=Q.T*G0*Q
assert list(G.diagonal())==[2]*6 and G.det()==-1
V=sp.eye(6);Vm=sp.eye(6);W=sp.eye(12)
for i in range(6):
 for j in range(i+1,6):
  a=int(G[i,j]);V[i,j]=a;Vm[i,j]=-abs(a)
  if a<=0: W[2*i,2*j]=W[2*i+1,2*j+1]=a
  else: W[2*i,2*j+1]=W[2*i+1,2*j]=-a
t,u=sp.symbols('t u')
p=sp.Poly((t*V+V.T).det(),t);pm=sp.Poly((t*Vm+Vm.T).det(),t)
assert p==sp.Poly(t**6-2*t**5-t**4+3*t**3-t**2-2*t+1,t)
coxeter=-V.inv()*V.T
traces=[int(sp.trace(coxeter**j)) for j in (1,2,3)]
assert traces==[2,6,5]
q=sp.Poly(u**3-2*u*u-4*u+7,u)
a,b,c=pm.all_coeffs()[1:4]
qm=sp.Poly(u**3+a*u*u+(b-3)*u+c-2*a,u)
assert sp.expand(t**3*qm.as_expr().subs(u,t+1/t))==pm.as_expr()
assert q.is_irreducible and p.is_irreducible
for k in range(13):assert (k*W+W.T).det()==p.eval(k)*pm.eval(k)
intervals=q.intervals(eps=sp.Rational(1,100000))
absolute_intervals=qm.intervals(eps=sp.Rational(1,100000))
def rows(M):return [[int(x) for x in row] for row in M.tolist()]
def enc_intervals(v):return [[[str(a),str(b)],int(mult)] for (a,b),mult in v]
result={'passed':True,'basis':rows(Q),'basis_determinant':1,'gram':rows(G),
        'matrix':rows(V),'absolute_matrix':rows(Vm),'cover_matrix':rows(W),
        'rank':6,'height':max(abs(int(x)) for x in V),
        'energy':sum(int(V[i,j])**2 for i in range(6) for j in range(i+1,6)),
        'polynomial':list(map(int,p.all_coeffs())),
        'absolute_polynomial':list(map(int,pm.all_coeffs())),
        'cover_polynomial':list(map(int,(p*pm).all_coeffs())),
        'trace_polynomial':str(q.as_expr()),'absolute_trace_polynomial':str(qm.as_expr()),
        'trace_intervals':enc_intervals(intervals),
        'absolute_trace_intervals':enc_intervals(absolute_intervals),
        'irreducible_original':True,'full_cover_det_integer_points':13}
result['original_first_three_power_traces']=traces
((_J_OUTPUT / 'changed_control.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('passed','basis','matrix','energy','polynomial','absolute_polynomial','trace_intervals','absolute_trace_intervals')}))
