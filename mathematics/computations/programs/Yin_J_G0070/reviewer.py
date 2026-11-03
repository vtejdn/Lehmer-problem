"""Independent complete eight-input verification; no author imports or resultants."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
from fractions import Fraction as F
from math import prod, factorial, gcd
import json
import sympy as S
HERE=(_J_PROGRAM / 'reviewer.py').parent
START=perf_counter()
def gate():
    if perf_counter()-START>120:raise TimeoutError('review120secondcap')
def comp(poly,var):
    p=S.Poly(poly,var);d=p.degree();coef=list(reversed(p.all_coeffs()))
    A=S.zeros(d)
    for j in range(d-1):A[j+1,j]=1
    for j in range(d):A[j,d-1]=-coef[j]
    return A
def fs(v):return str(v.numerator)+'/'+str(v.denominator)
def norm(P,C,t):
    A=comp(P,t);n=A.rows
    B=S.zeros(n)
    for (j,),v in S.Poly(C,t).terms():B+=v*A**j
    return S.expand(B.det(method='bareiss'))
def sphere(poly,vars):
    ans=F(0);s=len(vars)
    for powers,a in S.Poly(poly,*vars).terms():
        if any(v%2 for v in powers):continue
        halves=[v//2 for v in powers];L=sum(halves)
        # Gaussian moments via factorial quotients, independently of author's odd-factor loop.
        num=prod(factorial(2*v)//(2**v*factorial(v)) for v in halves)
        ans+=F(int(a)*num,prod(s+2*j for j in range(L)))
    return ans
native=json.loads(((_J_OUTPUT / 'verification.json')).read_text())
t,x=S.symbols('t x');rows=[]
for p in [3,5,7]:
    gate();s=(p-1)//2;P=sum(t**j for j in range(p))
    # P/t^s is 1+sum(t^j+t^-j), using a separate Chebyshev first-kind recurrence.
    v=[S.Integer(2),x]
    for j in range(2,s+1):v.append(S.expand(x*v[-1]-v[-2]))
    Q=S.expand(1+sum(v[1:s+1]))
    assert S.expand(t**s*Q.subs(x,t+1/t)-P)==0
    c=S.symbols('c0:'+str(s));basis=[]
    for j in range(s):
        basis.append(sum((-1)**k*S.binomial(j-k,k)*x**(j-2*k) for k in range(j//2+1)))
    N=norm(Q,sum(c[j]*basis[j] for j in range(s)),x)
    moments=[]
    for k in [1,2]:
        z=sphere(S.expand(N**(2*k)),c)
        expected=F(p**(k*(s-1))*(factorial(2*k)//(2**k*factorial(k)))**s,prod(s+2*j for j in range(k*s)))
        assert z==expected
        moments.append(dict(k=k,computed_moment=fs(z),formula_moment=fs(expected),equal=True))
    rows.append(dict(p=p,P=str(S.expand(P)),degree=2*s,Q=str(Q),trace_norm_form=str(N),P_endpoint_product=int(P.subs(t,1)*P.subs(t,-1)),moments=moments))
assert rows==native['moments']
controls=[]
for name,P in [('dyadic-4',t*t+1),('dyadic-8',t**4+1)]+[(f'nontorsion-q{q}',t**(2*q)-3*t**q+1) for q in [3,5,7]]:
    gate();d=S.degree(P,t);d=int(d);C=t**d-1;a=[int(v) for v in S.Poly(C,t).all_coeffs()]
    R=int(norm(P,C,t));pred=2**d if name.startswith('dyadic') else (-5)**(d//2)
    assert R==pred
    E=sum(v*v for v in a)
    controls.append(dict(name=name,P=str(P),actual_original_degree=d,C=str(C),actual_auxiliary_degree=d,content=gcd(*a),leading_abs=abs(a[0]),energy=E,full_signed_resultant=R,predicted_signed_resultant=pred,rho=fs(F(sum(map(abs,a))**2,E)),auxiliary_M=1,M_reason='C=t^d-1 is monic and all its d roots lie on the unit circle',exp_dB=fs(F(abs(R),E**(d//2)))))
assert controls==native['controls']
assert native['scope']=='Eight declared inputs only; three norm forms, six exact moments, five fixed auxiliary controls'
assert set(native)=={'scope', 'moments', 'controls'}
pass
gate()
out=dict(passed=True, all_mathematical_native_fields_equal=True, inputs=8, norm_forms=3, moments=6, full_resultants=5, method='Independent companion multiplication determinants and factorial Gaussian moment contraction; no author program import, polynomial resultant or native output rewrite.')
if __name__=='__main__':
    ((_J_OUTPUT / 'reviewer.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
