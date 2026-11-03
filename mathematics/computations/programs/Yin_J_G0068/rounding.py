"""Exactly two predeclared roundings of one retained actual Lehmer direction."""
import time,json,math
from functools import reduce
from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as S
start=time.perf_counter()
t,x=S.symbols('t x')
P=t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1
Q=x**5+x**4-5*x**3-5*x**2+4*x+3
assert S.expand(t**5*Q.subs(x,t+1/t)-P)==0
old=(196,-235,458,-1024,-384); S0=sum(c*c for c in old)
U=[S.Integer(1),x]
for i in range(2,5): U.append(S.expand(x*U[-1]-U[-2]))
def frac(q):return str(q.numerator)+'/'+str(q.denominator)
def rnd(c,H):
    a=H*abs(c); n=math.isqrt(a*a//S0)
    if 4*a*a>=S0*(2*n+1)**2:n+=1
    return n if c>=0 else -n
out=[]
for H in (45,179):
    z=[rnd(c,H) for c in old]
    if z[-1]==0:z[-1]=1 if old[-1]>=0 else -1
    g=reduce(math.gcd,z);c=[a//g for a in z]
    V=S.expand(sum(a*u for a,u in zip(c,U)))
    C=S.expand(sum(c[j]*(t**(6+j)-t**(4-j)) for j in range(5)))
    norm=int(S.resultant(Q,V,x));R=int(S.resultant(P,C,t));assert R==-norm*norm
    E=2*sum(a*a for a in c);ratio=F(abs(R),E**5)
    beta_hi=F(1434031,1219123) # retained exact L280 upper endpoint
    vint=[([str(a),str(b)],int(m)) for (a,b),m in S.Poly(V,x).intervals(eps=S.Rational(1,10**10))]
    inside=int(S.Poly(V,x).count_roots(-2,2))
    assert S.degree(C,t)==10 and S.Poly(C,t).content()==1
    assert len(vint)==4 and inside==3
    a,b=map(F,vint[0][0]);assert F(-7,2)<a<b<F(-17,5)
    lead=abs(int(S.LC(S.Poly(C,t))))
    row={'H':H,'raw_rounding':z,'gcd_removed':g,'primitive_c':c,'height':max(map(abs,c)),
      'V':str(V),'C':str(C),'trace_norm':norm,'original_resultant':R,'energy':E,
      'exp_10B':frac(ratio),'certified_B_above_m':ratio>beta_hi**10,
      'certified_exp_10B_over_beta_10_exceeds_343_over_320':ratio>F(343,320)*beta_hi**10,
      'B_discovery':math.log(ratio.numerator/ratio.denominator)/10,
      'actual_degree':10,'content':1,'leading_abs':lead,'rho':frac(F((2*sum(map(abs,c)))**2,E)),
      'trace_intervals':vint,'aux_roots_inside_trace_interval':inside,
      'complete_aux_M_strict_interval':[frac(F(3*lead)),frac(F(13*lead,4))]}
    out.append(row);print(row,flush=True)
elapsed=time.perf_counter()-start
assert elapsed<=120
(_J_OUTPUT / 'rounding.json').write_text(json.dumps({'scope': 'One exact input, two predetermined grids only', 'rows': out}, indent=2) + '\n', encoding='utf-8')
print('elapsed',elapsed)
