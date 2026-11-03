"""Exact certificates for the bounded pilot's structural interpretation.

No new parameter scan or Mahler approximation. The explicit (3,2) trace
certificate is rational/modular, independently of factor_list(W).
"""

from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp

HERE = (_J_PROGRAM / 'certify_structure.py').parent
t,x,u,v = sp.symbols("t x u v")
f = u*v-u-1
h = 1-v-u*v
G = sp.expand((h*h*f.subs({u:u*u,v:v*v},simultaneous=True)
               +f*f*h.subs({u:u*u,v:v*v},simultaneous=True))/2)
expected = u**4*v**3-u**4*v**2+u**3*v**4-2*u**3*v**2+u**3*v-u**2*v**2+u*v**3-2*u*v**2+u-v**2+v
assert G==expected
assert sp.expand(G-G.subs({u:v,v:u},simultaneous=True)
                 +(u-v)*(u*v-1)*(u*u*v+u*v*v+2*u*v+u+v))==0

R = sp.Poly(x**5-5*x**3-2*x**2+6*x+3,x)
W = sp.Poly(t**10-2*t**7+t**6-t**5+t**4-2*t**3+1,t)
assert sp.expand(t**5*R.as_expr().subs(x,t+1/t)-W.as_expr())==0
assert sp.expand(G.subs({u:t**2,v:t})-t*W.as_expr())==0
q = sp.Poly(R.as_expr(),x,modulus=2)
assert q.degree()==5
assert sp.rem(sp.Poly(x**32-x,x,modulus=2),q).is_zero
assert sp.gcd(q,sp.Poly(x*x-x,x,modulus=2)).degree()==0
# Degree 5 is prime: these two Rabin conditions certify irreducibility mod 2.

chain = [sp.Poly(p,x) for p in sp.sturm(R.as_expr(),x)]
for j in range(2,len(chain)):
    assert chain[j]==-sp.rem(chain[j-2],chain[j-1])

def signs_at(value):
    if value==sp.oo:
        return [int(sp.sign(p.LC())) for p in chain]
    if value==-sp.oo:
        return [int(sp.sign(p.LC())*(-1)**p.degree()) for p in chain]
    return [int(sp.sign(p.eval(value))) for p in chain]

def changes(signs):
    nonzero = [s for s in signs if s]
    return sum(a!=b for a,b in zip(nonzero,nonzero[1:]))

variations = [changes(signs_at(z)) for z in [-sp.oo,-2,2,sp.oo]]
assert variations==[4,4,2,1]
assert R.eval(-2)==-9 and R.eval(2)==-1

phi6 = t*t-t+1
assert sp.expand(phi6*(t**3-t-1)-(t**5-t**4-1))==0
rows = json.loads(((_J_OUTPUT / 'pilot.json')).read_text(encoding="utf-8"))
assert rows["completed"] and len(rows["rows"])==45
types = {}
cyclotomic_multiplicities = {}
for row in rows["rows"]:
    a,b = row["a"],row["b"]
    seed = sp.Poly(t**a-t**b-1,t)
    has_phi6 = a%6 in [1,5] and b%6==(2*a)%6
    quotient,remainder = sp.div(seed,sp.Poly(phi6,t))
    assert remainder.is_zero==has_phi6
    facs = row["factors"]
    noncyclo = [fac for fac in facs if not fac["cyclotomic"]]
    assert len(noncyclo)==1 and noncyclo[0]["multiplicity"]==1
    kind = noncyclo[0]["type"]
    types[kind] = types.get(kind,0)+1
    rebuilt = sp.Integer(row["content"])
    for fac in facs:
        polynomial = sp.Poly.from_list(fac["coefficients_descending"],t).as_expr()
        rebuilt *= polynomial**fac["multiplicity"]
        if fac["cyclotomic"]:
            orders = [n for n in [6,12,15] if sp.expand(polynomial-sp.cyclotomic_poly(n,t))==0]
            assert len(orders)==1
            cyclotomic_multiplicities.setdefault(str(orders[0]),[]).append([a,b,fac["multiplicity"]])
    reverse = 1-t**(a-b)-t**a
    actual = sp.expand((reverse**2*seed.as_expr().subs(t,t*t)+seed.as_expr()**2*reverse.subs(t,t*t))/2)
    assert sp.expand(t**row["ell"]*rebuilt-actual)==0
assert types=={"nonmonic_one_expanding":1,"Salem":2,"multiple_expanding":42}

result = {'all_assertions_passed': True, 'sparse_formula_and_swap_identity': True, 'trace32': str(R.as_expr()), 'residual32': str(W.as_expr()), 'trace32_mod2_irreducibility': {'degree': 5, 'x32_minus_x_remainder': '0', 'gcd_x2_minus_x': '1'}, 'sturm_chain32': [str(p.as_expr()) for p in chain], 'sturm_signs32': {str(z): signs_at(z) for z in [-sp.oo, -2, 2, sp.oo]}, 'sturm_variations32': variations, 'trace32_roots': {'below_minus2': 0, 'between_minus2_and2': 2, 'above2': 1, 'nonreal': 2}, 'row_count': 45, 'residual_types': types, 'each_row_one_simple_noncyclotomic_factor': True, 'cyclotomic_factors_by_order': cyclotomic_multiplicities, 'seed54_equals_phi6_seed31': True, 'scope': 'Exact finite pilot reconstruction and explicit structural certificates; no approximate Mahler assertion, unrestricted classification, or graph-exclusion claim beyond the written block-bipartite proof.'}
((_J_OUTPUT / 'structural-certificate.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"all_assertions_passed":True,"types":types,"sturm_variations32":variations},indent=2))
