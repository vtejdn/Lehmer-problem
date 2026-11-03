"""Declared bounded symbolic nonunit-capacity discovery; native output is beside this file."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
import sympy as S

START = time.perf_counter()
a,u,v,w,x = S.symbols('a u v w x')
Q = x**3-a*x**2-(a+3)*x-1
V = u*x**2+v*x+w
cols = [S.Poly(S.rem(V*x**k,Q,x),x) for k in range(3)]
matrix = S.Matrix([[c.nth(i) for c in cols] for i in range(3)])
norm = S.factor(matrix.det())
assert S.expand(norm-S.resultant(Q,V,x)) == 0
K = 1+v*v+(1+w)**2
p = w*(1-v+w)
f = S.expand(K+3*v*(1-v+w))
g = S.expand((1-v+2*w)*K-3*p*(1+w))
elim = S.factor(S.resultant(f,g,v))
quotient,remainder=S.div(g,f,v)
gb = S.groebner([f,g],v,w)
quartic = 2*w**4-8*w*w+w+6
vstar = S.rem(-gb.polys[0].as_expr().subs(v,0)/121,quartic,w)
critical_values = []
def add(A,B): return (A[0]+B[0],A[1]+B[1])
def mul(A,B):
    values=[p*q for p in A for q in B]
    return (min(values),max(values))
def scale(c,A): return mul((c,c),A)
def square(A):
    return (0 if A[0]<=0<=A[1] else min(A[0]**2,A[1]**2), max(A[0]**2,A[1]**2))
def horner(coeffs,A):
    value=(S.Integer(0),S.Integer(0))
    for c in coeffs: value=add(mul(value,A),(c,c))
    return value
certified=[]
for interval,multiplicity in S.Poly(quartic,w).intervals(eps=S.Rational(1,10**15)):
    lo,hi=interval
    ww=(lo+hi)/2
    vv=vstar.subs(w,ww)
    val=S.N((p*p/(8*K**3)).subs({w:ww,v:vv}),18)
    critical_values.append({'w_interval':[str(lo),str(hi)],'multiplicity':multiplicity,
                            'v_discovery':str(S.N(vv,18)),'squared_capacity_discovery':str(val)})
    left=S.floor(lo*10**6)/S.Integer(10**6)
    right=left+S.Rational(1,10**6)
    assert left<lo<=hi<right
    assert quartic.subs(w,left)*quartic.subs(w,right)<0
    W=(left,right)
    VV=horner([-2,-2,5,4],W)
    PP=mul(W,add(add((1,1),scale(-1,VV)),W))
    KK=add((1,1),add(square(VV),square(add((1,1),W))))
    NUM=square(PP)
    BOUNDS=(NUM[0]/(8*KK[1]**3),NUM[1]/(8*KK[0]**3))
    certified.append({'w_box':[str(z) for z in W],'v_box':[str(z) for z in VV],
                      'capacity_squared_bounds':[str(z) for z in BOUNDS]})
assert S.Rational(certified[0]['capacity_squared_bounds'][0])>S.Rational(1016,10000)
assert S.Rational(certified[0]['capacity_squared_bounds'][1])<S.Rational(1017,10000)
for row in certified[1:]:
    assert S.Rational(row['capacity_squared_bounds'][1])<S.Rational(1,50)
assert S.rem(f.subs(v,vstar),quartic,w)==0
assert S.rem(g.subs(v,vstar),quartic,w)==0
t=S.symbols('t')
controls=[]
for aa in [1,2,3,6]:
    qa=Q.subs({a:aa,x:t})
    pa=S.Poly(S.expand(t**3*Q.subs({a:aa,x:t+1/t})),t)
    for name,vec in [('D',(1,1,1)),('changed_nonunit',(2,1,-4)),
                     ('identity',(0,0,1)),('trace_derivative',(3,-2*aa,-aa-3))]:
        uu,vv,ww=vec
        cc=S.Poly(S.expand(t**2*(t*t-1)*(uu*(t+1/t)**2+vv*(t+1/t)+ww)),t)
        energy=sum(c*c for c in cc.all_coeffs())
        nn=norm.subs({a:aa,u:uu,v:vv,w:ww})
        result=S.resultant(pa.as_expr(),cc.as_expr(),t)
        assert result==-(6*aa-1)*(2*aa+3)*nn**2
        assert energy==2*(uu*uu+vv*vv+(uu+ww)**2)
        content=S.gcd_list(cc.all_coeffs())
        assert content==S.gcd_list(vec)
        controls.append({'a':aa,'direction':name,'vector':list(vec),'norm':int(nn),
                         'content':int(content),'energy':int(energy),
                         'actual_degree':cc.degree(),'resultant':int(result),
                         'primitive_energy':str(energy/content**2),
                         'primitive_resultant':str(result/content**6)})
assert S.expand(norm.subs({u:2,v:1,w:-4})-(24*a*a+42*a+17))==0
assert S.Rational(51,50)**6<S.Rational(32,27)
out = {'scope': 'one symbolic family and one critical system; no parameter search', 'norm': str(norm), 'norm_expanded': str(S.expand(norm)), 'leading_a2': str(S.expand(norm).coeff(a, 2)), 'critical_f': str(f), 'critical_g': str(g), 'eliminate_v': str(elim), 'groebner': [str(z) for z in gb.polys], 'division_g_by_f': [str(quotient), str(S.factor(remainder))], 'real_critical_quartic': str(quartic), 'v_on_quartic': str(vstar), 'critical_values': critical_values, 'exact_critical_certificates': certified, 'controls': controls}
(_J_OUTPUT / 'derivation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
