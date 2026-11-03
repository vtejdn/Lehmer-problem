"""Independent exact certificate for D136; no author program imports.
Declared before execution: <=120s; all symbolic identities, complete energy<=12
sign classes, and exactly a=1,2,3,6 controls. Matrix norms replace resultants;
quadratic discriminants replace ground_roots. No parameter/exponent search.
"""
import itertools,json,math,time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sympy as s
started=time.monotonic();CAP=120
a,x,t=s.symbols('a x t'); H=a*a+3*a+9
M=s.Matrix([[0,0,1],[1,0,a+3],[0,1,a]])
I=s.eye(3);D=M*M+M+I
def clean(A): return A.applyfunc(s.expand)
def zero(A): assert clean(A)==s.zeros(*A.shape)
def det3(A):
 return s.expand(sum((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))*s.prod(A[i,p[i]] for i in range(3)) for p in itertools.permutations(range(3))))
assert det3(M)==1 and det3(M+I)==-1
zero(M**3-a*M**2-(a+3)*M-I)
zero(M*(M*M-a*M-(a+3)*I)-I)
plus_inv=-M*M+(a+1)*M+2*I;zero((M+I)*plus_inv-I)
S=-plus_inv;zero(S**3-a*S*S-(a+3)*S-I)
zero((S*S+S+I)*(M+I)**2-D)
assert det3(D)==H
zero(D**3-H*(M*(M+I))**2)
zero(D**2-M*(M+I)*(3*M*M-2*a*M-(a+3)*I))
zero(D**2-((a*a+3*a+6)*M*M+(a*a+5*a+9)*M+(a+3)*I))
def integer_roots(poly):
 c=s.Poly(poly,a)
 if c.is_zero:return None
 co=[int(v) for v in c.all_coeffs()]
 if len(co)==1:return []
 if len(co)==2:
  b,c=co
  return [-c//b] if (-c)%b==0 and -c//b>=1 else []
 A,B,C=co;disc=B*B-4*A*C
 if disc<0:return []
 q=math.isqrt(disc)
 if q*q!=disc:return []
 return sorted({n//(2*A) for n in (-B+q,-B-q) if n%(2*A)==0 and n//(2*A)>=1})
hits=[];count=0
for yy in itertools.product(range(-2,3),repeat=3):
 if not 0<sum(v*v for v in yy)<=6:continue
 if next(v for v in yy if v)<0:continue
 u,v,z=yy;w=z-u
 if math.gcd(u,math.gcd(v,w))!=1:continue
 count+=1;N=det3(u*M*M+v*M+w*I);all_sign=[];finite=set()
 for sign in (-1,1):
  rr=integer_roots(s.expand(N-sign*H))
  if rr is None:all_sign.append(sign)
  else:finite.update(rr)
 if all_sign or finite:hits.append({'uvw':[u,v,w],'energy':2*sum(vv*vv for vv in yy),'norm':str(N),'all_a_norm_signs':all_sign,'exceptional_positive_integer_a':sorted(finite)})
 assert time.monotonic()-started<CAP
assert count==37
def companion(coeff):
 n=len(coeff)-1; A=s.zeros(n)
 for i in range(n-1):A[i+1,i]=1
 for i in range(n):A[i,n-1]=-coeff[n-i]
 return A
def eval_matrix(coeff,A):
 B=s.zeros(A.rows); Id=s.eye(A.rows)
 for c in coeff:B=B*A+c*Id
 return B
def full_coeff(u,v,w):
 return [u,v,u+w,0,-u-w,-v,-u]
controls=[]
author=json.loads((_J_OUTPUT / 'verification.json').read_text(encoding='utf-8'))
assert count==author['short_primitive_sign_representatives']
assert len(hits)==len(author['short_norm_H_hits'])==9
for h,orig in zip(hits,author['short_norm_H_hits']):
 assert h['uvw']==orig['uvw'] and h['energy']==orig['energy']
 assert s.expand(s.sympify(h['norm'])-s.sympify(orig['norm']))==0
 for k in ('all_a_norm_signs','exceptional_positive_integer_a'):assert h[k]==orig[k]
for av,ac in zip((1,2,3,6),author['actual_controls']):
 assert av==ac['a'];gv=math.gcd(av,3);hv=av*av+3*av+9
 coeff=[1,-av,-av,-2*av-1,-av,-av,1];T=companion(coeff);Mv=M.subs(a,av)
 assert list(s.Poly(s.sympify(ac['actual_polynomial']),t).all_coeffs())==coeff
 reps=[(0,0,1),(1,1,1),((av*av+3*av+6)//gv,(av*av+5*av+9)//gv,(av+3)//gv),(3//gv,-2*av//gv,-(av+3)//gv)]
 out=[]
 for (u,v,w),row in zip(reps,ac['rows']):
  ec=full_coeff(u,v,w)
  while ec[0]==0:ec=ec[1:]
  assert ec==list(map(int,row['edge_coefficients']))
  N=int(det3(u*Mv*Mv+v*Mv+w*I))
  # Whole original norm independently uses its 6x6 multiplication operator.
  R=int(eval_matrix(ec,T).det(method='bareiss'))
  E=sum(c*c for c in ec)
  assert (N,R,E)==(row['trace_norm'],row['full_resultant'],row['edge_energy'])
  assert R==-(6*av-1)*(2*av+3)*N*N
  assert math.gcd(*ec)==1
  out.append({'uvw':[u,v,w],'norm':N,'full_resultant':R,'energy':E})
 for tr,rep in zip(ac['exact_trace_root_checks'],reps[2:]):
  u,v,w=rep
  prior=None
  for item in tr['isolating_intervals']:
   lo,hi=map(s.Rational,item['interval']);assert lo<hi
   assert (u*lo*lo+v*lo+w)*(u*hi*hi+v*hi+w)<0
   assert prior is None or prior<lo
   prior=hi
   assert item['multiplicity']==1
   if item['status']=='interior':assert -2<lo<hi<2
   else:assert hi<-2 or lo>2
 controls.append({'a':av,'controls':out,'root_interval_sign_checks':'passed'})
 assert time.monotonic()-started<CAP
report={'symbolic_matrix_identities': 'passed', 'short_primitive_sign_representatives': count, 'short_norm_H_hits': hits, 'actual_controls': controls, 'author_native_comparison': 'passed', 'limits': 'Independent exact finite certificate; whole all-exponent and Mahler arguments reviewed in D136. No complete unit group or near-one claim.'}
(_J_OUTPUT / 'review_result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed': True, 'short_representatives': count, 'hits': len(hits), 'controls': len(controls)}))

