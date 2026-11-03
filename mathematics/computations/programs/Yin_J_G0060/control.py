"""Exact declared n=2,3,17,101 checks of the all-n larger-pivot control."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import json
import sympy as sp
from terminal import binary,binary_basis,norm

def coeff(expr,t):return [int(x) for x in sp.Poly(expr,t).all_coeffs()][::-1]
def lift(V):
    n=V.rows;W=sp.zeros(2*n)
    for i in range(n):
        for j in range(n):
            x=int(V[i,j])
            for r in range(2):W[2*i+r,2*j+(r if x<=0 else 1-r)]=-abs(x)
    return W
def proper_lift(V):
    n=V.rows;W=sp.eye(2*n)
    for i in range(n):
        for j in range(i+1,n):
            x=int(V[i,j])
            for r in range(2):W[2*i+r,2*j+(r if x<=0 else 1-r)]=-abs(x)
    assert all(W[i,i]==1 for i in range(2*n))
    assert all(W[i,j]==0 for i in range(2*n) for j in range(i))
    return W
def run():
    n,t=sp.symbols('n t');A=sp.Matrix([[1,3],[0,1]]);S=sp.Matrix([[n,n+1],[n-1,n]])
    B=sp.expand(S.T*A*S);expected=sp.Matrix([[5*n*n-5*n+1,5*n*n],[5*n*n-3,5*n*n+5*n+1]])
    assert B==expected and sp.expand(S.det())==1 and sp.expand(B.det())==1
    assert sp.expand((t*B+B.T).det())==t*t-7*t+1
    energy=sp.expand(sum(x*x for x in B));rows=[]
    for nn in [2,3,17,101]:
        b=B.subs(n,nn);s=S.subs(n,nn);values=sorted({norm(b.tolist(),x) for x in product((-1,0,1),repeat=2) if any(x)})
        assert 1 not in values
        sol=binary(b.tolist());assert sol['solution'] is not None
        q=sp.Matrix(binary_basis(b.tolist(),sol['solution']));out=q.T*b*q
        assert q.det()==1 and out==A and s.inv().T*b*s.inv()==A
        bb=-b.applyfunc(abs);w=lift(b);wa=proper_lift(A);pa=t*t-7*t+1
        assert sp.expand((t*bb+bb.T).det())==pa
        assert sp.expand((t*w+w.T).det())==sp.expand(pa*pa)
        assert sp.expand((t*wa+wa.T).det())==sp.expand(pa*pa)
        assert sum(int(wa[i,j])**2 for i in range(4) for j in range(i+1,4))==18
        rows.append(dict(n=nn,matrix=b.tolist(),explicit_basis=s.inv().tolist(),solver=sol,solver_basis=q.tolist(),positive_matrix=out.tolist(),cube_nonzero_values=values,initial_height=max(abs(int(x)) for x in b),initial_squared_entry_sum=sum(int(x)**2 for x in b),full_absolute_polynomial=coeff((t*bb+bb.T).det(),t),full_cover_polynomial=coeff((t*w+w.T).det(),t),proper_height=3,proper_energy=9,proper_cover_energy=18,relaxed_cover_squared_entry_sum=sum(int(x)**2 for x in w),proper_cover_matrix=wa.tolist()))
    return json.loads(json.dumps(dict(passed=True,scope=[2,3,17,101],all_parameter_matrix_formula=[[str(x) for x in row] for row in B.tolist()],all_parameter_squared_entry_sum=str(energy),original_polynomial=[1,-7,1],rows=rows),default=int))
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'control_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
