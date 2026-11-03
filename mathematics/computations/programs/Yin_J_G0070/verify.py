"""Predeclared eight-input exact capacity controls; no directional search."""
import json, math, time
from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as S

START = time.perf_counter()
def gate():
    if time.perf_counter() - START > 120:
        raise RuntimeError('aggregate author 120-second cap exceeded')
def fs(a):
    return f'{a.numerator}/{a.denominator}'
def oddfact(k):
    return math.prod(range(1, 2*k, 2))
def moment(poly, s):
    total = Fraction(0)
    for u, a in poly.terms():
        if any(v % 2 for v in u):
            continue
        total += Fraction(int(a) * math.prod(oddfact(v//2) for v in u),
                          math.prod(s+2*j for j in range(sum(u)//2)))
    return total

t, x = S.symbols('t x')
moments = []
for p in (3, 5, 7):
    gate()
    P = S.cyclotomic_poly(p, t)
    s = (p-1)//2
    rem, Q = S.expand(P), S.Integer(0)
    for j in range(s, -1, -1):
        a = rem.coeff(t, s+j)
        Q += a*x**j
        rem = S.expand(rem-a*S.expand(t**s*(t+1/t)**j))
    assert rem == 0
    c = S.symbols('c0:'+str(s))
    U = [S.Integer(1), x]
    for j in range(2, s):
        U.append(S.expand(x*U[-1]-U[-2]))
    V = sum(c[j]*U[j] for j in range(s))
    N = S.resultant(Q, V, x)
    assert S.Poly(P,t).is_irreducible and S.Poly(Q,x).is_irreducible
    rows = []
    for k in (1, 2):
        gate()
        computed = moment(S.Poly(S.expand(N**(2*k)), *c), s)
        formula = Fraction(p**(k*(s-1))*oddfact(k)**s,
                           math.prod(s+2*j for j in range(k*s)))
        assert computed == formula
        rows.append({'k':k,'computed_moment':fs(computed),
                     'formula_moment':fs(formula),'equal':True})
    moments.append({'p':p,'P':str(P),'degree':2*s,'Q':str(Q),
                    'trace_norm_form':str(S.expand(N)),
                    'P_endpoint_product':int(P.subs(t,1)*P.subs(t,-1)),
                    'moments':rows})

controls = []
inputs = [('dyadic-4', t**2+1), ('dyadic-8', t**4+1)]
inputs += [(f'nontorsion-q{q}',t**(2*q)-3*t**q+1) for q in (3,5,7)]
for name, P in inputs:
    gate()
    d = int(S.degree(P,t)); C = t**d-1
    coeffs = [int(a) for a in S.Poly(C,t).all_coeffs()]
    R = int(S.resultant(P,C,t))
    expected = 2**d if name.startswith('dyadic') else (-5)**(d//2)
    assert R == expected and S.Poly(P,t).is_irreducible
    assert S.expand(t**d*C.subs(t,1/t)+C) == 0
    E = sum(a*a for a in coeffs)
    controls.append({'name':name,'P':str(P),'actual_original_degree':d,
                     'C':str(C),'actual_auxiliary_degree':int(S.degree(C,t)),
                     'content':int(S.Poly(C,t).content()),'leading_abs':abs(coeffs[0]),
                     'energy':E,'full_signed_resultant':R,'predicted_signed_resultant':expected,
                     'rho':fs(Fraction(sum(map(abs,coeffs))**2,E)),
                     'auxiliary_M':1,
                     'M_reason':'C=t^d-1 is monic and all its d roots lie on the unit circle',
                     'exp_dB':fs(Fraction(abs(R),E**(d//2)))})
gate()
out={'scope': 'Eight declared inputs only; three norm forms, six exact moments, five fixed auxiliary controls', 'moments': moments, 'controls': controls}
(_J_OUTPUT / 'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
