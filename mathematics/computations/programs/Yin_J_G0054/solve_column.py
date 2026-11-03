"""Declared137842 triples; the eliminated x0 has no imposed size bound."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
from math import isqrt
import json
import sympy as s
from equations import equations, x, G0, Q0

BASE=(_J_PROGRAM / 'solve_column.py').parent
BOUND=20

def main():
    witnesses=[];checked=0;singular=0;integral=0
    x0,x1,_,_,v,w=x
    for case in equations(2)['cases']:
        N=s.sympify(case['norm_equation']);A=s.sympify(case['coefficient_equation'])
        R=s.Poly(s.expand(A+3*N),x0)
        assert R.degree()==1
        den=s.lambdify((x1,v,w),R.coeff_monomial(x0),'math')
        const=s.lambdify((x1,v,w),R.coeff_monomial(1),'math')
        nf=s.lambdify((x0,x1,v,w),N,'math')
        af=s.lambdify((x0,x1,v,w),A,'math')
        linear=s.lambdify((x1,v,w),s.expand(N).coeff(x0),'math')
        normconst=s.lambdify((x1,v,w),s.expand(N).subs(x0,0),'math')
        for b,c,d in product(range(-BOUND,BOUND+1),repeat=3):
            checked+=1
            D=den(b,c,d);C=const(b,c,d)
            roots=[]
            if D:
                if (-C)%D==0:roots=[(-C)//D];integral+=1
            else:
                singular+=1
                if C==0:
                    L=linear(b,c,d);T=normconst(b,c,d);disc=L*L-4*T
                    if disc>=0:
                        j=isqrt(disc)
                        if j*j==disc:
                            roots=sorted({(-L+sgn*j)//2 for sgn in (-1,1) if (-L+sgn*j)%2==0})
            for a in roots:
                if nf(a,b,c,d) or af(a,b,c,d):continue
                k=(5-case['pfaffian'])//2
                coeff=[a,b,1,k-3*c-d,c,d]
                Q=Q0.copy();Q[:,2]=Q0*s.Matrix(coeff)
                assert Q.det()==1
                G=Q.T*G0*Q
                assert list(G.diagonal())==[2]*6
                E=sum(int(G[i,j])**2 for i in range(6) for j in range(i+1,6))
                witnesses.append({'pfaffian':case['pfaffian'],'path_coefficients':coeff,
                                  'energy':E,'basis':[[int(v) for v in row] for row in Q.tolist()]})
    assert checked==137842
    witnesses.sort(key=lambda r:(r['energy'],r['path_coefficients']))
    result={'passed':True,'declared_bound':BOUND,'declared_triple_cap':137842,
            'triples_tested':checked,'singular_linear_cases':singular,
            'nonsingular_integral_x0_cases':integral,'target_count':len(witnesses),
            'all_targets':witnesses}
    ((_J_OUTPUT / 'solve_column.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='all_targets'}))
    print(json.dumps(witnesses[:3]))
if __name__=='__main__':main()
