"""Parametric exterior-square identities and full relaxed absolute/cover costs."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations
import json
import sympy as sp

def data(a,k):
    A=sp.Matrix([[0,0,0,-1],[1,0,0,k],[0,1,0,a],[0,0,1,k+1]])
    ids=list(combinations(range(4),2));G=sp.zeros(6)
    for i,j,s in [(0,5,1),(1,4,-1),(2,3,1)]:G[i,j]=G[j,i]=s
    C=sp.Matrix(6,6,lambda i,j:A.extract(ids[i],ids[j]).det());V=G*(sp.eye(6)-C).inv()
    V=V.applyfunc(sp.cancel)
    return A,G,C,V
def coeff(expr,t):return [int(x) for x in sp.Poly(expr,t).all_coeffs()][::-1]
def control(a,k,label):
    t=sp.Symbol('t');A,G,C,V=data(a,k);n=6
    assert all(x.q==1 for x in V) and V.det()==1 and V+V.T==G
    B=V.applyfunc(lambda x:-abs(x));W=sp.zeros(12)
    for i in range(n):
        for j in range(n):
            x=int(V[i,j])
            for s in range(2):W[2*i+s,2*j+(s if x<=0 else 1-s)]=-abs(x)
    p=sp.expand((t*V+V.T).det());pb=sp.expand((t*B+B.T).det());whole=sp.expand(p*pb)
    assert p==C.charpoly(t).as_expr()
    for t0 in range(-6,7):assert (t0*W+W.T).det(method='domain-ge')==whole.subs(t,t0)
    S=sp.zeros(12)
    for i in range(6):S[2*i,i]=S[2*i+1,i]=1;S[2*i,6+i]=1;S[2*i+1,6+i]=-1
    assert S.T*S==2*sp.eye(12)
    assert (S.T*W*S)/2==sp.diag(B,V)
    return dict(label=label,a=a,k=k,A=A.tolist(),G=G.tolist(),C=C.tolist(),V=V.tolist(),full_absolute_B=B.tolist(),cover_W=W.tolist(),original_polynomial=coeff(p,t),absolute_polynomial=coeff(pb,t),absolute_factorization=str(sp.factor(pb)),full_cover_polynomial=coeff(whole,t),V_determinant=int(V.det()),absolute_determinant=int(B.det()),cover_determinant=int(W.det()),original_degree=int(sp.degree(p,t)),absolute_degree=int(sp.degree(pb,t)),cover_degree=int(sp.degree(whole,t)),height=max(abs(int(x)) for x in V),squared_entry_sum=sum(int(x)**2 for x in V),cover_height=max(abs(int(x)) for x in W),cover_squared_entry_sum=sum(int(x)**2 for x in W))
def run():
    a,k,t=sp.symbols('a k t');A,G,C,V=data(a,k)
    expected=t**6+a*t**5+(k*(k+1)-1)*t**4-(2*a+2*k*(k+1)+1)*t**3+(k*(k+1)-1)*t**2+a*t+1
    assert sp.expand(C.charpoly(t).as_expr()-expected)==0
    assert sp.expand((sp.eye(6)-C).det())==-1 and G.det()==-1
    assert all(sp.expand(x)==0 for x in C.T*G*C-G)
    assert all(sp.expand(x)==0 for x in V+V.T-G)
    assert all(sp.expand(x)==0 for x in V*(sp.eye(6)-C)-G)
    assert all(sp.Poly(x,a,k).domain==sp.ZZ for x in V if x!=0)
    u=sp.Symbol('u')
    B=sp.Matrix([[0,-1,-k-1,0,-1,0],[-1,0,-u,-1,0,-1],[-k-1,-u,0,-k-1,-u,-k],[0,-1,-k,0,-1,0],[-1,-1,-u,-1,0,-1],[-1,-1,-k,0,-1,0]])
    pb=sp.expand((t*B+B.T).det(method='domain-ge'));assert sp.expand(B.det())==-1
    controls=[control(-2,1,'F=Phi6 P4'),control(0,0,'S6')]
    for control_ in controls:
        got=coeff(pb.subs({k:control_['k'],u:abs(control_['a']+1)}),t)
        assert got==control_['absolute_polynomial']
    out=dict(passed=True,parameter_scope='a any integer, k any nonnegative integer',matrix_V_formula=[[str(x) for x in row] for row in V.tolist()],full_characteristic_formula=str(expected),full_absolute_formula=str(pb),absolute_parameter='u=abs(a+1), k>=0',absolute_determinant=-1,full_cover_scalar_determinant_checks=26,controls=controls)
    return json.loads(json.dumps(out,default=int))
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'costs_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='controls'}));print(json.dumps([{k:c[k] for k in ['label','original_polynomial','absolute_polynomial','absolute_factorization','absolute_determinant','cover_determinant','height','squared_entry_sum','cover_squared_entry_sum']} for c in out['controls']]))
