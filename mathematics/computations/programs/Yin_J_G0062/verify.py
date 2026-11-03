"""Bounded author certificate; no imported expected-output table."""
import itertools
import json
import math
import time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as sp

started = time.monotonic()
CAP_SECONDS = 120
a, x, t = sp.symbols('a x t')
Q = x**3-a*x**2-(a+3)*x-1
H = a*a+3*a+9
D = x*x+x+1
P = sp.Poly(sp.expand(t**3*Q.subs(x,t+1/t)),t).as_expr()

def reduced(f):
    return sp.rem(sp.expand(f),Q,x)

def check_zero(f):
    assert sp.expand(f) == 0, f

def norm(f):
    return sp.factor(sp.resultant(Q,f,x))

def edge(f):
    return sp.Poly(sp.expand(t**2*(t*t-1)*f.subs(x,t+1/t)),t).as_expr()

def energy(f):
    return sum(c*c for c in sp.Poly(f,t).all_coeffs())

def coef(f,var):
    return [str(c) for c in sp.Poly(f,var).all_coeffs()]

def assert_cap():
    assert time.monotonic()-started < CAP_SECONDS, 'Declared cap exceeded'

tau_inverse = sp.invert(x,Q,x)
plus_inverse = sp.invert(x+1,Q,x)
check_zero(reduced(D**3-H*(x*(x+1))**2))
check_zero(norm(D)-H)
check_zero(reduced(D**2-x*(x+1)*sp.diff(Q,x)))
sigma_D = reduced(D.subs(x,-plus_inverse))
check_zero(reduced(sigma_D*(x+1)**2-D))
check_zero(reduced(Q.subs(x,-plus_inverse)))
check_zero(reduced(D**2)-((a*a+3*a+6)*x*x+(a*a+5*a+9)*x+a+3))
check_zero(P.subs(t,1)*P.subs(t,-1)+(6*a-1)*(2*a+3))
check_zero(energy(edge(D))-12)
check_zero(energy(edge(sp.diff(Q,x)))-(10*a*a+18))
check_zero(sp.discriminant(reduced(D**2),x)-H*(H-8))
matrix = sp.Matrix([[sp.Poly(reduced(x*x**j),x).nth(i) for j in range(3)] for i in range(3)])
assert matrix.det() == 1
assert (matrix+sp.eye(3)).det() == -1
short = []
pair_count = 0
for y in itertools.product(range(-2,3),repeat=3):
    if not (0 < sum(c*c for c in y) <= 6):
        continue
    if next(c for c in y if c) < 0:
        continue
    u,v,last = y
    w = last-u
    if math.gcd(math.gcd(abs(u),abs(v)),abs(w)) != 1:
        continue
    pair_count += 1
    V = u*x*x+v*x+w
    N = norm(V)
    all_parameters = []
    finite = set()
    for sign in (-1,1):
        difference = sp.Poly(N-sign*H,a)
        if difference.is_zero:
            all_parameters.append(sign)
        else:
            for r in sp.polys.polytools.ground_roots(difference):
                if r.is_Integer and r >= 1:
                    finite.add(int(r))
    if all_parameters or finite:
        short.append({'uvw':[u,v,w], 'energy':2*sum(c*c for c in y),
                      'norm':str(N), 'all_a_norm_signs':all_parameters,
                      'exceptional_positive_integer_a':sorted(finite)})
    assert_cap()

controls=[]
for av in (1,2,3,6):
    q=Q.subs(a,av)
    p=P.subs(a,av)
    hv=int(H.subs(a,av))
    gv=math.gcd(av,3)
    assert sp.Poly(p,t).is_irreducible
    raw=[sp.Integer(1),D,reduced(D**2).subs(a,av)]
    contents=[int(sp.Poly(v,x).content()) for v in raw]
    assert contents == [1,1,gv]
    rows=[]
    for r,Vraw in enumerate(raw):
        V=Vraw/contents[r]
        C=edge(V)
        assert sp.Poly(C,t).content()==1
        n=sp.resultant(q,V,x)
        R=sp.resultant(p,C,t)
        assert R == -(6*av-1)*(2*av+3)*n*n
        rows.append({'r':r,'trace_coefficients':coef(V,x),'content_raw':contents[r],
                     'trace_norm':int(n),'full_resultant':int(R),
                     'edge_coefficients':coef(C,t),'edge_energy':int(energy(C)),
                     'edge_factorization':str(sp.factor(C))})
    derivative=sp.diff(q,x)/gv
    derivativeC=edge(derivative)
    assert sp.resultant(q,derivative,x)==-hv*hv//(gv**3)
    # Cubic derivative norm is -discriminant; its sign is retained.
    # D^2/(tau(tau+1)) has norm -H^2, consistently.
    rows.append({'representative':'Qprime/g','trace_coefficients':coef(derivative,x),
                 'trace_norm':int(sp.resultant(q,derivative,x)),
                 'full_resultant':int(sp.resultant(p,derivativeC,t)),
                 'edge_energy':int(energy(derivativeC)),
                 'edge_coefficients':coef(derivativeC,t)})
    root_checks=[]
    for label,V,expected_exterior in [('D2/g',raw[2]/gv,0),('Qprime/g',derivative,0 if av==1 else 1)]:
        intervals=sp.polys.polytools.intervals(V,eps=sp.Rational(1,1000))
        assert sum(mult for _,mult in intervals)==2
        outside=0
        retained=[]
        for (lo,hi),mult in intervals:
            if hi < -2 or lo > 2:
                outside+=mult
                status='exterior'
            else:
                assert -2 < lo <= hi < 2
                status='interior'
            retained.append({'interval':[str(lo),str(hi)],'multiplicity':mult,'status':status})
        assert outside == expected_exterior
        root_checks.append({'trace':label,'isolating_intervals':retained,
                            'full_edge_off_circle_roots':2*outside})
    assert sp.discriminant(D,x)==-3
    controls.append({'a':av,'H':hv,'g':gv,'actual_polynomial':str(p),'rows':rows,
                     'exact_trace_root_checks':root_checks,
                     'D_edge_off_circle_roots':4})
    assert_cap()

report={'symbolic_checks': 'passed', 'tau_inverse': str(tau_inverse), 'plus_inverse': str(plus_inverse), 'multiplication_tau_matrix': [[str(v) for v in row] for row in matrix.tolist()], 'short_primitive_sign_representatives': pair_count, 'short_norm_H_hits': short, 'actual_controls': controls, 'limits': 'Author exact checks, not independent review or a numerical infinite-orbit proof.'}
out=(_J_OUTPUT / 'verification.json')
out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed': True, 'short_representatives': pair_count, 'short_hits': len(short), 'controls': len(controls)}))
