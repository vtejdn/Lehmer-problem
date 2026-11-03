"""Exact rational checks for two analytic lower-integral certificates.

No numerical integration, no polynomial-parameter sweep, and no assertion
of an effective Lawton convergence rate is made.
"""
from fractions import Fraction as Q
from math import prod
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parents[1]
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name / "limit"
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

# Radical bounds used by the four-interval proof.
assert Q(11,5)**2 < 5
assert Q(17,10)**2 < 3
assert Q(141,100)**2 < 2 < Q(71,50)**2
assert Q(19,25)**2 < 2-Q(71,50)
assert Q(46,25)**2 < 2+Q(141,100)
assert Q(707,500)**2 < 2
assert Q(61,25)**2 < 6
assert Q(173,100)**2 < 3
radical_lower = [Q(13,5), Q(37,10), Q(501,100), Q(6071,1000)]
root_lower = [Q(21,10), Q(17,5), Q(24,5), Q(59,10)]
radical_margins = [a-r-1/r for a,r in zip(radical_lower,root_lower)]
assert all(v>0 for v in radical_margins)
lhs = 3**129 * 7**4 * 17**5 * 59**10
rhs = 2**239 * 5**24
assert lhs > rhs
assert prod(r**w for r,w in zip(root_lower,[4,5,5,10])) > Q(4,3)**120

# Independently derived five-interval Taylor proof, using pi<22/7.
def cosine_lower(x): return 1-x*x/2+x**4/24-x**6/720
taylor_roots = [Q(33,5),Q(29,5),Q(24,5),Q(17,5),Q(17,10)]
taylor_bounds = [1+2*sum(cosine_lower(Q(11*j*k,84)) for k in (1,2,3))
                 for j in range(1,6)]
taylor_margins = [a-r-1/r for a,r in zip(taylor_bounds,taylor_roots)]
assert all(v>0 for v in taylor_margins)
assert prod(taylor_roots) == Q(3318876,3125)
assert prod(taylor_roots)-Q(4,3)**24 == Q(57739308097115356,882592301503125)

result = {
    'status':'passed',
    'scope':'Exact auxiliary arithmetic for two direct analytic certificates M(F)>4/3; not numerical quadrature, not a finite-g cutoff',
    'four_interval':{'beta_lower_bounds':list(map(str,root_lower)),
                     'radical_comparison_margins':list(map(str,radical_margins)),
                     'integer_comparison_difference':str(lhs-rhs)},
    'five_interval_independent_check':{'beta_lower_bounds':list(map(str,taylor_roots)),
                     'taylor_comparison_margins':list(map(str,taylor_margins)),
                     'product':'3318876/3125',
                     'product_comparison_difference':'57739308097115356/882592301503125'},
}
(_J_OUTPUT / 'result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
