"""Exact illustrative two-linear elimination; no integer search enlargement."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import json
import sympy as sp
from exact import X,model,terms

def run():
    m=model(0,2);y=sp.symbols('x y z w');x,v,z,w=y;rows=[]
    for name,target,pf in [('F',-2,3),('S6',0,1)]:
        for eps,delta in product((1,-1),(pf,-pf)):
            k=(delta+eps)//2
            sub={X[0]:-x-eps,X[1]:2*x-2*z-2*w-k,X[2]:x,X[3]:v,X[4]:z,X[5]:w}
            assert sp.expand(m['ell'].subs(sub)-eps)==0 and sp.expand(m['pf'].subs(sub)-delta)==0
            ns=sp.expand(m['norm_half'].subs(sub)-1);aa=sp.expand(m['first'].subs(sub)-target)
            def reduce(p):return str(sp.Poly(p,y).trunc(4).as_expr())
            rows.append(dict(target=name,epsilon=eps,delta=delta,k=k,norm_residual=str(ns),coefficient_residual=str(aa),norm_mod4=reduce(ns),coefficient_mod4=reduce(aa),difference_mod4=reduce(aa-ns)))
    return dict(positions=[0,2],parameters=['x','y','z','w'],substitution=['-x-epsilon','2*x-2*z-2*w-k','x','y','z','w'],cases=rows)
if __name__=='__main__':
    result=run();(_J_OUTPUT / 'elimination.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
