"""Independent bounded D140 certificate: no author imports.
Declared scope: general norm, exact stationary equations/eliminant, four rational
critical boxes and the same16 actual controls. 120 seconds; no new search.
Symbolic determinants use explicit permutation expansion, full norms use
six-dimensional multiplication matrices; intervals use Fraction monomial bounds.
"""
import itertools,json,math,time
from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as S
start=time.perf_counter();CAP=120
a,u,v,w,x,t=S.symbols('a u v w x t')
def det(A):
 n=A.rows
 return S.expand(sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))*S.prod(A[i,p[i]] for i in range(n)) for p in itertools.permutations(range(n))))
M=S.Matrix([[0,0,1],[1,0,a+3],[0,1,a]]);I=S.eye(3)
N=det(u*M*M+v*M+w*I)
p=u*w*(u-v+w)
L=-u*u*v+4*u*u*w+u*v*v-3*u*v*w+2*u*w*w-v*v*w+v*w*w
R=u**3-3*u*u*v+9*u*u*w-3*u*v*w+6*u*w*w+v**3-3*v*v*w+w**3
assert S.expand(N-a*a*p-a*L-R)==0
assert sum(abs(c) for c in S.Poly(L,u,v,w).coeffs())==13
assert sum(abs(c) for c in S.Poly(R,u,v,w).coeffs())==27
pp=w*(1-v+w);K=1+v*v+(1+w)**2
f=S.cancel(-(2*pp*S.diff(pp,v)*K-3*pp*pp*S.diff(K,v))/(2*pp*w))
g=S.cancel((2*pp*S.diff(pp,w)*K-3*pp*pp*S.diff(K,w))/(2*pp))
fc=S.Poly(f,v).all_coeffs();gc=S.Poly(g,v).all_coeffs()
sy=S.zeros(5)
for i in range(3):
 for j,c in enumerate(fc):sy[i,i+j]=c
for i in range(2):
 for j,c in enumerate(gc):sy[3+i,i+j]=c
J=2*w**4-8*w*w+w+6
assert S.expand(det(sy)-9*(2*w*w+4*w+3)*J)==0
vs=-2*w**3-2*w*w+5*w+4
assert S.rem(f.subs(v,vs),J,w)==0 and S.rem(g.subs(v,vs),J,w)==0
assert S.expand(g-(v/2-w/4+S.Rational(1,4))*f-S.Rational(3,4)*((3*w*w-5)*v-w**3-w*w+4*w+2))==0
for rr in [S.Rational(sgn)*r for sgn in (-1,1) for r in (1,2,3,6,S.Rational(1,2),S.Rational(3,2))]:assert J.subs(w,rr)!=0
def add(A,B):return A[0]+B[0],A[1]+B[1]
def mul(A,B):
 cc=[q*r for q in A for r in B];return min(cc),max(cc)
def power(A,n):
 if n==0:return F(1),F(1)
 if n%2==0:
  low=F(0) if A[0]<=0<=A[1] else min(A[0]**n,A[1]**n)
  return low,max(A[0]**n,A[1]**n)
 return A[0]**n,A[1]**n
def polynomial(coefs,A):
 out=(F(0),F(0))
 for i,c in enumerate(coefs):out=add(out,mul((F(c),F(c)),power(A,i)))
 return out
def rat_eval(coefs,z):return sum(F(c)*z**i for i,c in enumerate(coefs))
boxes=[(-1840012,-1840011),(-892923,-892922),(1163265,1163266),(1569668,1569669)]
cert=[]
for i,(l,h) in enumerate(boxes):
 W=(F(l,10**6),F(h,10**6))
 assert rat_eval([6,1,-8,0,2],W[0])*rat_eval([6,1,-8,0,2],W[1])<0
 V=polynomial([4,5,-2,-2],W)
 P=mul(W,add(add((F(1),F(1)),mul((F(-1),F(-1)),V)),W))
 KK=add((F(1),F(1)),add(power(V,2),power(add((F(1),F(1)),W),2)))
 numerator=power(P,2)
 bounds=(numerator[0]/(8*KK[1]**3),numerator[1]/(8*KK[0]**3))
 assert bounds[0]>0
 if i==0:
  assert F(1016,10000)<bounds[0]<bounds[1]<F(1017,10000)
  assert 4-2*V[1]+W[0]>0 and 4+2*V[0]+W[0]>0
 else:assert bounds[1]<F(1,50)
 cert.append({'w_box':[str(z) for z in W],'independent_v_box':[str(z) for z in V],'independent_squared_capacity_box':[str(z) for z in bounds]})
 assert time.perf_counter()-start<CAP
def companion(coeff):
 n=len(coeff)-1;A=S.zeros(n)
 for i in range(n-1):A[i+1,i]=1
 for i in range(n):A[i,n-1]=-coeff[n-i]
 return A
def evalmat(coeff,A):
 B=S.zeros(A.rows);I=S.eye(A.rows)
 for c in coeff:B=B*A+c*I
 return B
controls=[]
for av in (1,2,3,6):
 Mv=M.subs(a,av);T=companion([1,-av,-av,-2*av-1,-av,-av,1])
 for name,vec in [('D',(1,1,1)),('changed_nonunit',(2,1,-4)),('identity',(0,0,1)),('trace_derivative',(3,-2*av,-av-3))]:
  uu,vv,ww=vec;cc=[uu,vv,uu+ww,0,-uu-ww,-vv,-uu]
  while cc[0]==0:cc=cc[1:]
  nn=int(det(uu*Mv*Mv+vv*Mv+ww*I));result=int(evalmat(cc,T).det(method='bareiss'))
  energy=sum(z*z for z in cc);content=math.gcd(*cc)
  assert result==-(6*av-1)*(2*av+3)*nn*nn
  controls.append({'a':av,'direction':name,'vector':list(vec),'norm':nn,'content':content,'energy':energy,'actual_degree':len(cc)-1,'resultant':result,'primitive_energy':str(F(energy,content**2)),'primitive_resultant':str(F(result,content**6))})
assert S.expand(N.subs({u:2,v:1,w:-4})-24*a*a-42*a-17)==0
assert F(51,50)**6<F(32,27)
author=json.loads((_J_OUTPUT / 'derivation.json').read_text(encoding='utf-8'))
for field,actual in [('norm',N),('norm_expanded',N),('leading_a2',p),('critical_f',f),('critical_g',g),('eliminate_v',det(sy)),('real_critical_quartic',J),('v_on_quartic',vs)]:
 assert S.expand(S.sympify(author[field])-actual)==0,field
assert controls==author['controls']
for i,ac in enumerate(author['exact_critical_certificates']):
 assert list(map(F,ac['w_box']))==list(map(F,cert[i]['w_box']))
 low,high=map(F,ac['capacity_squared_bounds'])
 if i==0:assert F(1016,10000)<low<high<F(1017,10000)
 else:assert 0<low<high<F(1,50)
for ac in author['critical_values']:
 low,high=map(F,ac['w_interval'])
 assert rat_eval([6,1,-8,0,2],low)*rat_eval([6,1,-8,0,2],high)<0 and ac['multiplicity']==1
# Author numerical displays are discovery only, not accepted numerical premises.
report={'status': 'passed', 'author_imports': False, 'general_norm_and_stationary_identities': 'passed', 'exact_critical_boxes': cert, 'actual_controls': controls, 'rational_threshold': 'passed', 'limits': 'Whole symbolic/finite accepted certificate; radical irreducibility and uniform projective proof reviewed separately in D140. Discovery decimals are not evidence.'}
assert time.perf_counter()-start<CAP
(_J_OUTPUT / 'review_result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed': True, 'controls': len(controls), 'critical_boxes': len(cert)}))

