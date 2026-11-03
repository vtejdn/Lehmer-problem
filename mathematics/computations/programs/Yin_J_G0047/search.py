"""Exact bounded D85 search; no floating arithmetic or expanded search window."""
from itertools import permutations, product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp

HOME = (_J_PROGRAM / 'search.py').parent
t = sp.symbols('t')
vars6 = sp.symbols('a b c d e f')
a,b,c,d,e,f = vars6
B = sp.Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1]])
C = sp.Matrix([[1,a,b,c],[0,1,d,e],[0,0,1,f],[0,0,0,1]])
M = (t+1)*(t*C+C.T)-t*(B.T*B)
det4 = 0
for perm in permutations(range(4)):
    sign = (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    term = sign
    for i in range(4):
        term *= M[i,perm[i]]
    det4 += term
det4 = sp.Poly(sp.expand(det4), t)
p,rem = sp.div(det4,sp.Poly(t+1,t))
assert rem.is_zero
coeffs = p.all_coeffs()
assert coeffs == coeffs[::-1] and coeffs[0]==1
exprs = [sp.expand(p.nth(k)) for k in (6,5,4)]
functions = [sp.lambdify(vars6,z,modules='math') for z in exprs]
restricted = sp.expand(p.as_expr().subs({b:0,c:0,e:0}))
out = {'parameter_order':list(map(str,vars6)), 'range':[-3,3],
       'declared_tuples':7**6, 'B':B.tolist(),
       'coefficient_equations':dict(zip(['t6','t5','t4'],map(str,exprs))),
       'restricted_path_t6':str(sp.expand(restricted).coeff(t,6)),
       'visited':0, 'energy_filtered':0, 'tested':0,
       'first_coefficient_matches':0,'second_coefficient_matches':0,
       'witness':None}
for values in product(range(-3,4),repeat=6):
    out['visited'] += 1
    energy = 6+sum(z*z for z in values)
    if energy<13:
        out['energy_filtered'] += 1
        continue
    out['tested'] += 1
    first = functions[0](*values)
    assert type(first) is int
    if first != 0:
        continue
    out['first_coefficient_matches'] += 1
    second = functions[1](*values)
    assert type(second) is int
    if second != -1:
        continue
    out['second_coefficient_matches'] += 1
    third = functions[2](*values)
    assert type(third) is int
    if third != -1:
        continue
    Cv = C.subs(dict(zip(vars6,values)))
    V = sp.eye(7)
    V[:3,3:] = -B
    V[3:,3:] = Cv
    direct = sp.Poly((t*V+V.T).det(method='domain-ge'),t)
    target = sp.Poly((t+1)*(t**6-t**5-t**3-t+1),t)
    assert direct==target
    out['witness'] = {'parameters':list(values),'V':V.tolist(),
                      'energy':energy,'full_polynomial':str(direct.as_expr())}
    break
out['box_complete'] = out['visited']==out['declared_tuples']
out['scope'] = 'Complete declared box only if box_complete; otherwise first exact witness and visited prefix.'
def integer_default(x):
    if isinstance(x,sp.Integer): return int(x)
    raise TypeError(type(x))
text = json.dumps(out,indent=2,default=integer_default)+'\n'
((_J_OUTPUT / 'search_result.json')).write_text(text,encoding='utf-8')
print(text)
