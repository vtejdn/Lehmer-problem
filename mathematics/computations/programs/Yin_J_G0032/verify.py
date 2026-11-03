"""Exact finite controls for D G0033; no imported earlier research implementation."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import itertools, json, platform, time
import sympy as sp

HERE=(_J_PROGRAM / 'verify.py').parent
def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def energy(v):return sum(v[i][j]**2 for i in range(len(v)) for j in range(i+1,len(v)))
def windmill(r):
    v=ident(2*r+1)
    for j in range(r):
        a,b=2*j+1,2*j+2
        v[0][a]=v[0][b]=v[a][b]=1
    return v
def mutate(v,j):
    a,b=2*j+1,2*j+2
    q=ident(len(v)); q[a][a]=0;q[a][b]=q[b][a]=1;q[b][b]=-v[a][b]
    assert abs(bareiss(q))==1
    out=mul(transpose(q),mul(v,q))
    assert all(out[i][j]==int(i==j) for i in range(len(v)) for j in range(i+1))
    return out
def absolute(v):
    out=ident(len(v))
    for i in range(len(v)):
        for j in range(i+1,len(v)):out[i][j]=-abs(v[i][j])
    return out
def bareiss(matrix):
    a=[row[:] for row in matrix];n=len(a);prior=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((j for j in range(k+1,n) if a[j][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prior==0
                a[i][j]=num//prior
        for i in range(k+1,n):a[i][k]=0
        prior=pivot
    return sign*a[-1][-1]
def determinant_polynomial_check(v,expected):
    n=len(v)
    for t in range(n+1):
        a=[[t*v[i][j]+v[j][i] for j in range(n)] for i in range(n)]
        assert bareiss(a)==expected(t),(n,t,'Stokes determinant')
    return n+1

started=time.perf_counter();rows=[];det_values=0;commutations=0
for r in range(1,9):
    subsets={tuple(range(k)) for k in range(r+1)}
    if r<=4:
        subsets.update(tuple(j for j in range(r) if mask>>j&1) for mask in range(1<<r))
    for subset in sorted(subsets,key=lambda s:(len(s),s)):
        v=windmill(r)
        for j in subset:
            before=energy(v);v=mutate(v,j);assert energy(v)==before-1
        reverse=windmill(r)
        for j in reversed(subset):reverse=mutate(reverse,j)
        assert reverse==v;commutations+=int(len(subset)>=2)
        k=len(subset);n=len(v);vm=absolute(v)
        assert energy(v)==3*r-k
        f=lambda t:t*t+t+1
        expected=lambda t:(t+1)*f(t)**(r-1)*(t*t+(1-r)*t+1)
        expected_abs=lambda t:(t+1)*f(t)**(r-1)*(t*t+(1-3*r+2*k)*t+1)
        det_values+=determinant_polynomial_check(v,expected)
        det_values+=determinant_polynomial_check(vm,expected_abs)
        a=[[abs(v[i][j]) if i<j else abs(v[j][i]) if i>j else 0 for j in range(n)] for i in range(n)]
        for x in range(n+1):
            actual=bareiss([[x*int(i==j)-a[i][j] for j in range(n)] for i in range(n)])
            claim=(x*x-1)**(r-1)*(x**3-(1+2*r-k)*x-2*(r-k))
            assert actual==claim,(r,k,x,'adjacency polynomial')
            det_values+=1
        if k==r:
            signs=[1]+[-1]*(2*r)
            switched=[[signs[i]*v[i][j]*signs[j] for j in range(n)] for i in range(n)]
            assert switched==vm
        rows.append({'r':r,'processed':list(subset),'k':k,'energy':energy(v),'signed_quadratic_middle':1-r,'absolute_quadratic_middle':1-3*r+2*k})

gram_checks=[];x=sp.Symbol('x')
for r in range(1,9):
    v=sp.Matrix(windmill(r));g=v+v.T;c=-v.inv()*v.T
    assert c.T*g*c==g
    assert c-sp.eye(2*r+1)==-v.inv()*g
    assert g.charpoly(x).as_expr().expand()==sp.expand((x-1)**r*(x-3)**(r-1)*(x*x-5*x+6-2*r))
    ker=g.nullspace()
    assert all(c*z==z for z in ker)
    assert len(ker)==int(r==3)
    gram_checks.append({'r':r,'kernel_dimension':len(ker),'negative_eigenvalues':int(r>3),'positive_eigenvalues':2*r+1-int(r>=3)})

# Full symbolic three-by-three identities, including arbitrary integer weights.
a,b,c=sp.symbols('a b c');v=sp.Matrix([[1,a,b],[0,1,c],[0,0,1]])
g=v+v.T;cox=-v.inv()*v.T
assert all(sp.expand(z)==0 for z in cox.T*g*cox-g)
assert all(sp.expand(z)==0 for z in cox-sp.eye(3)+v.inv()*g)

result={'status': 'passed', 'family_inputs': len(rows), 'r_range': [1, 8], 'all_subsets_for_r_leq': 4, 'otherwise_prefix_subsets': True, 'exact_integer_determinant_values': det_values, 'reverse_order_controls': commutations, 'gram_controls': gram_checks, 'symbolic_general_weighted_rank_three_identities': True, 'finite_controls_not_general_proof': True, 'rows': rows}
((_J_OUTPUT / 'verification.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('rows','gram_controls')},indent=2))
