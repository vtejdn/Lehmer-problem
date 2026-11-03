"""Exact auxiliary arithmetic for S4 and the three-variable kernel limit.

No polynomial/root sweep and no effective Lawton convergence rate.
The numerical integral diagnostics are retained separately and are not premises.
"""
from fractions import Fraction as Q
from math import prod
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

# S4: standard-angle endpoint bounds, all established by positive squares.
assert Q(173,100)**2 < 3
assert Q(193,100)**2 < 2+Q(173,100)
assert Q(17,10)**2 < 3
assert Q(11,5)**2 < 5
assert Q(141,100)**2 < 2
cs=[Q(233,50),Q(37,10),Q(16,5),Q(241,100)]
bs=[Q(22,5),Q(17,5),Q(14,5),Q(15,8)]
margins=[c-b-1/b for c,b in zip(cs,bs)]
assert all(v>0 for v in margins)
weights=[5,5,2,3]
product=prod(b**w for b,w in zip(bs,weights))
target=Q(4,3)**60
assert product>target

# Limiting three-variable P: seven width-pi/24 lower rectangles.
def C(x): return 1-x*x/2+x**4/24-x**6/720
rs=[Q(99,50),Q(193,100),Q(46,25),Q(173,100),Q(79,50),Q(141,100),Q(121,100)]
assert Q(11*7,84)<1
pmargins=[2*C(Q(11*j,84))-v for j,v in enumerate(rs,1)]
assert all(v>0 for v in pmargins)
pprod=prod(rs)
assert pprod>Q(4,3)**12

result={
 'status':'passed',
 'scope':'Exact arithmetic only for direct S4 and three-variable-limit integral bounds M>4/3',
 's4':{'beta_lower_bounds':list(map(str,bs)), 'weights':weights,
       'comparison_margins':list(map(str,margins)),
       'product':str(product),'product_minus_target':str(product-target)},
 'three_variable_limit':{'cosine_lower_bounds':list(map(str,rs)),
       'comparison_margins':list(map(str,pmargins)),
       'product':str(pprod),'product_minus_target':str(pprod-Q(4,3)**12)},
}
(_J_OUTPUT / 'result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
