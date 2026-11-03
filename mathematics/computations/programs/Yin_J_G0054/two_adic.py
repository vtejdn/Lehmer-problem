"""Declared8736 mod2/mod4/mod8 checks; verify all printed general formulas."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import json
import sympy as s
from equations import equations
BASE=(_J_PROGRAM / 'two_adic.py').parent

def main():
    x,b,v,w,k=s.symbols('x b v w k')
    N=x*x-x*b+b*b+6*b*v+4*b*w-(2*k+1)*b+7*v*v+12*v*w-(5*k+5)*v+4*w*w-(4*k+3)*w+k*k+k
    R=(4*b+4*v+8*w-2*k-4)*x-4*b*b-8*b*v-16*b*w+(4*k+6)*b-11*v*v-28*v*w+(9*k+5)*v-20*w*w+(12*k+11)*w-2*k*k-2*k-3
    records=[];total=0
    for case in equations(2)['cases']:
        kv=(5-case['pfaffian'])//2
        sub={s.Symbol('x0'):x,s.Symbol('x1'):b,s.Symbol('x4'):v,s.Symbol('x5'):w}
        sourceN=s.sympify(case['norm_equation']).subs(sub)
        sourceA=s.sympify(case['coefficient_equation']).subs(sub)
        assert s.expand(N.subs(k,kv)-sourceN)==0
        assert s.expand(R.subs(k,kv)-sourceA-3*sourceN)==0
        f=s.lambdify((x,b,v,w),(sourceN,sourceA),'math')
        for m in (2,4,8):
            survivors=[]
            for point in product(range(m),repeat=4):
                total+=1;n,a=f(*point)
                if n%m==0 and a%m==0:survivors.append(list(point))
            records.append({'column':2,'pfaffian':case['pfaffian'],'modulus':m,
                            'tuples':m**4,'survivor_count':len(survivors),'survivors':survivors})
    assert total==8736
    y,z=s.symbols('y z')
    N3=21*x*x+4*x*y-10*x*v+10*x*z-(9*k+10)*x+y*y-(k+1)*y+v*v+(2*k+3)*v-3*v*z+z*z-(2*k+2)*z+k*k+2*k
    D3=x*x+4*x*y+y*y-k*x-(k+1)*y+k-3
    for case in equations(3)['cases']:
        kv=(5-case['pfaffian'])//2
        sub={s.Symbol('x0'):x,s.Symbol('x2'):y+2*v,s.Symbol('x4'):v,s.Symbol('x5'):z}
        sourceN=s.sympify(case['norm_equation']).subs(sub)
        sourceA=s.sympify(case['coefficient_equation']).subs(sub)
        assert s.expand(N3.subs(k,kv)-sourceN)==0
        assert s.expand(D3.subs(k,kv)-sourceA+sourceN)==0
    result={'passed':True,'declared_residue_cap':8736,'total_tuples':total,
            'printed_equations_symbolically_checked':True,'systems':records}
    ((_J_OUTPUT / 'two_adic.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for r in records:print({k:v for k,v in r.items() if k!='survivors'})
if __name__=='__main__':main()
