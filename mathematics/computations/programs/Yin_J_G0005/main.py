"""Exact guided calculations for the coprime reciprocal length-five family.

The finite tables do not prove that no other cyclotomic order occurs; the
separate five-root vanishing-sum argument supplies that analytic reduction.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import math
import sympy as sp

t, y = sp.symbols('t y')
tables = {}
for m in (1, 2, 3, 4, 5, 6, 10, 12):
    cyclo = sp.Poly(sp.cyclotomic_poly(m, t), t)
    pairs = []
    for n in range(m):
        for a in range(m):
            if math.gcd(math.gcd(n, a), m) != 1:
                continue
            h = sp.Poly(t**n+t**((-n)%m)-t**a-t**((-a)%m)-1, t)
            if h.rem(cyclo).is_zero:
                pairs.append([n, a])
    tables[str(m)] = pairs

n, k = 21, 13
a = n-k
q = sp.Poly(t**(2*n)-t**(2*n-k)-t**n-t**k+1, t)
c = sp.Poly(sp.cyclotomic_poly(10,t)*sp.cyclotomic_poly(12,t),t)
p = q.exquo(c)
trace = sp.Poly(2*sp.chebyshevt(n,y/2)-2*sp.chebyshevt(a,y/2)-1,y)
trace_c = sp.Poly((y*y-y-1)*(y*y-3),y)
trace_p = trace.exquo(trace_c)
assert sp.expand(t**17*trace_p.as_expr().subs(y,t+1/t)) == p.as_expr()
modular_irreducibility = {}
for ell in (2,3,5,7,11,13):
    modular_irreducibility[str(ell)] = bool(sp.Poly(trace_p.as_expr(),y,modulus=ell).is_irreducible)
interval_values = {str(sp.Rational(j,8)):str(trace_p.eval(sp.Rational(j,8))) for j in range(-15,16)}
mod3 = sp.Poly(trace_p.as_expr(),y,modulus=3)
def ternary_code(poly):
    return sum((int(poly.nth(j))%3)*3**j for j in range(poly.degree()+1))
frobenius = sp.Poly(y,y,modulus=3)
frobenius_codes = []
for j in range(17):
    frobenius = (frobenius**3).rem(mod3)
    frobenius_codes.append(ternary_code(frobenius))
assert frobenius == sp.Poly(y,y,modulus=3)
assert [int(mod3.eval(j))%3 for j in range(3)] == [2,2,2]
assert trace_p.eval(sp.Rational(1,2)) < 0 < trace_p.eval(sp.Rational(5,8))

graph=sp.zeros(42)
for j in range(13): graph[j,(j+1)%13] = 1
for j in range(29): graph[13+j,13+(j+1)%29] = 1
graph[12,13] = 1
graph[13+7,0] = 1
assert graph.charpoly(t).as_expr() == q.as_expr()
assert sum(graph) == 44

root_probe=p.nroots(n=35,maxsteps=250)
probe_moduli=[sp.Abs(z).evalf(35) for z in root_probe]
probe_expanding=[value for value in probe_moduli if value>1+sp.Rational(1,10**20)]
probe_mahler=sp.prod(probe_expanding).evalf(30)
graeffe=p
graeffe_checks=[]
for iteration in range(13):
    norm_squared=sum(int(coefficient)**2 for coefficient in graeffe.all_coeffs())
    exponent=2**(iteration+1)
    passed=norm_squared*10**exponent < 13**exponent
    graeffe_checks.append({'iteration':iteration,'norm_squared':str(norm_squared),
                          'comparison_exponent':exponent,'strict_upper_13_over10':passed})
    if passed:
        break
    even=sp.Poly.from_list(list(reversed([graeffe.nth(j) for j in range(0,35,2)])),t)
    odd=sp.Poly.from_list(list(reversed([graeffe.nth(j) for j in range(1,35,2)])),t)
    graeffe=even*even-sp.Poly(t,t)*odd*odd
assert passed
out = {
    'scope':'Finite residue identities and one exact n=21,k=13 control; order completeness requires the written vanishing-sum proof',
    'cyclotomic_residue_pairs_n_a':tables,
    'control':{
        'n':n,'k':k,'a':a,
        'q_coefficients_ascending':[int(q.nth(j)) for j in range(q.degree()+1)],
        'p_coefficients_ascending':[int(p.nth(j)) for j in range(p.degree()+1)],
        'trace_p_coefficients_ascending':[int(trace_p.nth(j)) for j in range(trace_p.degree()+1)],
        'p_irreducible_over_Q':bool(p.is_irreducible),
        'trace_modular_irreducibility':modular_irreducibility,
        'trace_GF3_ternary_code':ternary_code(mod3),
        'trace_GF3_frobenius_remainders_codes':frobenius_codes,
        'trace_GF3_values_at_0_1_2':[2,2,2],
        'trace_values':interval_values,
        'trace_roots_minus2_to2':int(trace_p.count_roots(-2,2)),
        'trace_real_roots_total':int(trace_p.count_roots(-sp.oo,sp.oo)),
        'graph_vertices':42,'graph_edges':44,'graph_characteristic_polynomial_checked':True,
        'canonical_negative_indices':[1,10,12],
        'canonical_repair_degree':23,'optimal_repair_degree':8,
        'graeffe_upper_certificate':{
            'steps':graeffe_checks,
            'final_coefficients_ascending':[str(graeffe.nth(j)) for j in range(35)],
            'threshold':'13/10',
            'scope':'Exact root-squaring and Jensen-Parseval norm bound prove M(p)<13/10; no numerical root is used',
        },
        'numerical_probe_only':{
            'decimal_digits':35,'maxsteps':250,'expanding_cutoff':'1+10^(-20)',
            'root_moduli':[str(value) for value in probe_moduli],
            'expanding_roots_above_cutoff':len(probe_expanding),
            'mahler_approximation':str(probe_mahler),
            'scope':'Numerical orientation only; no enclosure, root classification or Mahler inequality is certified by this probe',
        },
    }
}
text=json.dumps(out,indent=2)
(_J_OUTPUT / 'result.json').write_text(text+'\n',encoding='utf-8')
print(text)
