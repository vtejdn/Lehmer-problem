"""Exact structural diagnostics for the fixed B constructor; not a larger box."""
from itertools import product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp

HOME=(_J_PROGRAM / 'structure.py').parent
saved=json.loads(((_J_OUTPUT / 'search_result.json')).read_text(encoding='utf-8'))
v6=sp.symbols('a b c d e f')
a,b,c,d,e,f=v6
eq=[sp.sympify(saved['coefficient_equations'][k]) for k in ['t6','t5','t4']]
fn=[sp.lambdify(v6,z,modules='math') for z in eq]
B=sp.Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1]])
C=sp.Matrix([[1,a,b,c],[0,1,d,e],[0,0,1,f],[0,0,0,1]])
v=sp.Matrix([1,-1,1,-1])
x=(B.T).gauss_jordan_solve((C.T-C)*v)[0]
assert (-B.T*x+(C.T-C)*v).applyfunc(sp.expand)==sp.zeros(4,1)
norm=sp.expand((x.T*x+v.T*C*v)[0])
assert sp.expand(7-5*eq[0]+3*eq[1]-eq[2]-norm)==0
mod_results={}
for modulus in [2,3,4,5]:
    residues=[]
    for vals in product(range(modulus),repeat=6):
        if all((g(*vals)-target)%modulus==0 for g,target in zip(fn,[0,-1,-1])):
            residues.append(vals)
    mod_results[str(modulus)]={'tuple_count':modulus**6,'target_residue_count':len(residues),'first':residues[:4]}
out={'kernel_core':list(v),'kernel_auxiliary':list(map(str,x)),
     'primitive_kernel_norm':str(norm),'norm_equals_derivative':True,
     'modular_target_tests':mod_results}
u,vv,w,h,k=sp.symbols('u v w h k')
R=u*u+vv*vv+w*w+u-vv+w-1
subs={a:h-u,b:k+h,c:k,d:k+R+vv,e:k+R-h,f:R-h-w}
out['norm_five_parameterization']={str(z):str(value) for z,value in subs.items()}
out['norm_five_t6']=str(sp.factor(eq[0].subs(subs)))
out['norm_five_det_plus_one']=str(sp.factor(2*(1+eq[0]+eq[1]+eq[2]).subs(subs)))
((_J_OUTPUT / 'structure_result.json')).write_text(json.dumps(out,indent=2,default=int)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,default=int))
