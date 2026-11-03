"""Second author implementation: exact Schur determinant, fiber congruences,
nonintegral boundary control, and complete signed-cover factorization.
No numerical search or floating arithmetic is used.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import json
import sympy as sp

HOME=(_J_PROGRAM / 'verify.py').parent
t,x=sp.symbols('t x')
a,b,c,d,e,f=sp.symbols('a b c d e f')
B=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,1]])
C=sp.Matrix([[1,a,b,c],[0,1,d,e],[0,0,1,f],[0,0,0,1]])
M=(t+1)*(t*C+C.T)-t*(B.T*B)
det4=sp.Poly(M.det(method='domain-ge'),t)
p,rem=sp.div(det4,sp.Poly(t+1,t));assert rem.is_zero
saved=json.loads(((_J_OUTPUT / 'derivation.json')).read_text(encoding='utf-8'))
assert all(sp.expand(p.nth(i)-sp.sympify(saved['coefficients'][str(i)]))==0 for i in [6,5,4])
A,D,H=[p.nth(i) for i in [6,5,4]]
expected_A=3+f-a*a-b*b-c*c-d*d-e*e-f*f+a*b*d+a*c*e+b*c*f+d*e*f-a*c*d*f
assert sp.expand(A-expected_A)==0
trace=x**3+(A-1)*x*x+(D-A-2)*x+H-D-A+1
assert sp.expand((t+1)*t**3*trace.subs(x,t+1/t)-p.as_expr())==0
V=sp.eye(7);V[:3,3:]=-B;V[3:,3:]=C
z=sp.Matrix([c-b,e-d,f,0,0,1,-1])
skew=V.T-V
assert (skew*z).applyfunc(sp.expand)==sp.zeros(7,1)
assert skew[:6,:6].det()==1
norm=(c-b)**2+(e-d)**2+f*f-f+2
assert sp.expand((z.T*V*z)[0]-norm)==0
assert sp.expand(sp.diff(p.as_expr(),t).subs(t,-1)-norm)==0
solutions=[(fv,u,v) for fv,u,v in product(range(-1,3),range(-1,2),range(-1,2))
           if u*u+v*v+fv*(fv-1)==3]
assert len(solutions)==8
assert set(solutions)=={(fv,u,v) for fv in [-1,2] for u,v in [(1,0),(-1,0),(0,1),(0,-1)]}
checks=[]
residue_tests=0
for fv,u,v in solutions:
    sub={c:b+u,e:d+v,f:fv}
    A,D=[sp.expand(p.nth(i).subs(sub)) for i in [6,5]]
    q=d if u else b
    difference=sp.Poly(sp.expand(D-A-q*q),a,b,d)
    assert all(int(z)%3==0 for z in difference.coeffs())
    expected_A=(-a*(a+u*d) if u else -a*(a-v*b)) if fv==2 else (
        -a*a+a*d*(3*b+2*u)-3*b*(b+u)-3*d*d if u else
        -a*a+a*b*(3*d+v)-3*b*b-3*d*(d+v))
    expected_Diff=(q*q-3) if fv==2 else (q*q+3*(
        4*a*b*d+2*a*u*d-3*b*(b+u)-3*d*d-1 if u else
        4*a*b*d+2*a*v*b-3*b*b-3*d*(d+v)-1))
    assert sp.expand(A-expected_A)==0 and sp.expand(D-A-expected_Diff)==0
    for aa,bb,dd in product(range(3),repeat=3):
        av=int(A.subs({a:aa,b:bb,d:dd}))%3
        dv=int(D.subs({a:aa,b:bb,d:dd}))%3
        assert not(av==0 and dv==2)
        residue_tests+=1
    checks.append({'f':fv,'u':u,'v':v,'square_variable':str(q),
                   'D_minus_A_minus_square_divided_by_3':str(sp.expand(difference.as_expr()/3))})

rt=sp.sqrt(2)
sub={a:0,b:0,c:1,d:rt,e:rt,f:2}
control=V.subs(sub)
negative=sp.eye(7)
for i in range(7):
    for j in range(i+1,7):negative[i,j]=-sp.Abs(control[i,j])
P6=t**6-t**5-t**3-t+1
R6=t**6-13*t**5-32*t**4-45*t**3-32*t**2-13*t+1
qabs=x**3-13*x*x-35*x-19
assert sp.expand(t**3*qabs.subs(x,t+1/t)-R6)==0
assert sp.expand((t*control+control.T).det(method='domain-ge')-(t+1)*P6)==0
assert sp.expand((t*negative+negative.T).det(method='domain-ge')-(t+1)*R6)==0
assert sp.Poly(P6,t).is_irreducible and sp.Poly(R6,t).is_irreducible
intervals=[(-2,-1),(-1,0),(15,16)]
counts=[sp.Poly(qabs,x).count_roots(lo,hi) for lo,hi in intervals]
assert counts==[1,1,1]
assert all(qabs.subs(x,k)!=0 for k in [1,-1,19,-19])
cover=sp.eye(14);swap=sp.Matrix([[0,1],[1,0]])
for i in range(7):
    for j in range(i+1,7):
        val=control[i,j]
        block=val*sp.eye(2) if val<0 else -val*swap
        cover[2*i:2*i+2,2*j:2*j+2]=block
Q=sp.diag(*([sp.Matrix([[1,1],[1,-1]])]*7))
diagonalized=(Q.inv()*cover*Q).applyfunc(sp.simplify)
order=list(range(0,14,2))+list(range(1,14,2))
diagonalized=diagonalized.extract(order,order)
assert diagonalized==sp.diag(negative,control)
full_cover=sp.expand((t+1)**2*P6*R6)
assert sp.expand((t*cover+cover.T).det(method='domain-ge')-full_cover)==0
energy=lambda mat:sp.simplify(sum(mat[i,j]**2 for i in range(mat.rows) for j in range(i+1,mat.cols)))
assert energy(control)==13 and energy(cover)==26
assert max(abs(z) for z in control)==2 and max(abs(z) for z in cover)==2
assert rt in list(control) and -rt in list(cover)
sym=control+control.T
assert sym.det()==-2
positive5=sym[:5,:5]
leading=[positive5[:j,:j].det() for j in range(1,6)]
assert all(v>0 for v in leading)
# Five positive directions and a negative nonzero determinant in dimension7
# imply precisely one negative direction, hence inertia(6,1).
out={'full_schur_identity':True,'primitive_kernel_minor':1,
     'full_trace_cubic_identity':True,'general_first_coefficient_identity':True,
     'kernel_norm_derivative_identity':True,'all_norm_five_solutions':solutions,
     'all_eight_unbounded_fiber_identities':checks,'mod3_residue_checks':residue_tests,
     'complete_architecture_target_excluded':True,
     'general_input_obstruction':'P monic reciprocal degree6, P(-1)=5, coefficient t4 divisible by3',
     'nonintegral_control':{'rank':7,'original':str(sp.expand((t+1)*P6)),
        'absolute':str(sp.expand((t+1)*R6)),'absolute_trace':str(qabs),
        'absolute_trace_intervals':intervals,'interval_counts':list(map(int,counts)),
        'P6_irreducible':True,'R6_irreducible':True,
        'cover_rank':14,'full_cover':str(full_cover),'direct_cover_determinant':True,
        'height':2,'energy':13,'cover_energy':26,'nonintegral_entries_retained':True,
        'positive_principal_minor_chain':list(map(str,leading)),'inertia':[6,1]},
     'scope':'Author second exact implementation; all-entry architecture proof, no matrix box search, not independent review.'}
((_J_OUTPUT / 'verification.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
