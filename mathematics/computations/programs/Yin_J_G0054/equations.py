"""Exact unbounded one-column equations; no search is performed here."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as s

BASE = (_J_PROGRAM / 'equations.py').parent
G0 = s.Matrix([[2,1,1,1,1,1],[1,2,1,-1,-1,1],
               [1,1,2,1,-1,-1],[1,-1,1,2,1,-1],
               [1,-1,-1,1,2,1],[1,1,-1,-1,1,2]])
Q0=s.eye(6)
for i in range(1,6):Q0[i-1,i]=-1
H=Q0.T*G0*Q0
x=s.symbols('x0:6')

def pf(A):
    if A.rows==0:return s.Integer(1)
    return s.expand(sum((-1)**(j+1)*A[0,j]*pf(A.minor_submatrix(0,j).minor_submatrix(j-1,0)) for j in range(1,A.rows)))

def equations(i):
    c=s.Matrix(x);c[i]=1
    Q=Q0.copy();Q[:,i]=Q0*c
    G=Q.T*G0*Q
    V=s.eye(6)
    for a in range(6):
        for b in range(a+1,6):V[a,b]=G[a,b]
    N=V-s.eye(6)
    Vinv=sum(((-N)**j for j in range(6)),s.zeros(6))
    assert (V*Vinv-s.eye(6)).applyfunc(s.expand)==s.zeros(6)
    norm=s.expand((c.T*H*c)[0]/2-1)
    a=s.expand(s.trace(Vinv*V.T))
    alternating=pf(V-V.T)
    assert s.total_degree(alternating)<=1
    assert s.total_degree(a)<=2
    cases=[]
    for sign in (-3,3):
        linear=s.expand(alternating-sign)
        variable=min((v for v in x if linear.coeff(v)!=0),key=lambda v:abs(linear.coeff(v)))
        replacement=s.solve(linear,variable)[0]
        ns=s.factor(norm.subs(variable,replacement))
        aa=s.factor((a+2).subs(variable,replacement))
        cases.append({'pfaffian':sign,'eliminate':str(variable),'replacement':str(replacement),
                      'norm_equation':str(ns),'coefficient_equation':str(aa),
                      'difference':str(s.factor(aa-ns))})
    return {'column':i,'norm_equation':str(norm),'first_coefficient':str(a),
            'pfaffian':str(alternating),'cases':cases}

def main():
    assert Q0.det()==1 and G0.det()==-1
    result={'passed':True,'gram_path':list(map(list,H.tolist())),
            'columns':[equations(i) for i in (2,3)]}
    result['gram_path']=[[int(v) for v in row] for row in result['gram_path']]
    ((_J_OUTPUT / 'equations.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
