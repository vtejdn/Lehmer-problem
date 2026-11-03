"""Whole D150 finite certificate, independently reconstructed by root for Yin.
Declared before first execution: same full energy-eight 4x4 integer domain;
normalize only the first nonzero sign in EACH ROW, no column/forest quotient.
Check coefficients by sums of squared minors of B (not Gram principal minors).
Reconstruct complete control pencils by integer triangular inverse/Newton traces.
120-second aggregate cap; no imports of author code or third-party packages.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations,product
from collections import Counter
from time import perf_counter
import json,platform
HOME=(_J_PROGRAM / 'review_independent.py').parent
CAP=120
PAIRS=list(combinations(range(4),2))
TRIPLES=list(combinations(range(4),3))
def det3(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def determinant4(a):
 return sum((-1)**j*a[0][j]*det3([[a[r][c] for c in range(4) if c!=j] for r in range(1,4)]) for j in range(4))
def e2_of_b(a):
 total=0
 for r,s in PAIRS:
  ar,ass=a[r],a[s]
  for c,d in PAIRS:
   v=ar[c]*ass[d]-ar[d]*ass[c]
   total+=v*v
   if total>18:return total
 return total
def e3_of_b(a):
 return sum(det3([[a[r][c] for c in cs] for r in rs])**2 for rs in TRIPLES for cs in TRIPLES)
def matmul(a,b):
 cols=list(zip(*b))
 return [[sum(x*y for x,y in zip(row,col)) for col in cols] for row in a]
def gram(a):
 return matmul([list(c) for c in zip(*a)],a)
def pencil_coefficients(v):
 n=len(v)
 inv=[[int(i==j) for j in range(n)] for i in range(n)]
 for i in range(n-1,-1,-1):
  assert v[i][i]==1 and all(v[i][j]==0 for j in range(i))
  for j in range(i+1,n):inv[i][j]=-sum(v[i][k]*inv[k][j] for k in range(i+1,j+1))
 q=[[-z for z in row] for row in matmul(inv,[list(c) for c in zip(*v)])]
 power=[[int(i==j) for j in range(n)] for i in range(n)]
 trace=[0];desc=[1]
 for k in range(1,n+1):
  power=matmul(power,q);trace.append(sum(power[i][i] for i in range(n)))
  numerator=-sum(desc[j]*trace[k-j] for j in range(k))
  assert numerator%k==0
  desc.append(numerator//k)
 return list(reversed(desc))
def proper(b):
 r,g=len(b),len(b[0]);n=r+g
 v=[[int(i==j) for j in range(n)] for i in range(n)]
 for i in range(r):
  for j in range(g):v[i][r+j]=-b[i][j]
 return v
def literal_cover(v):
 n=len(v);w=[[int(i==j) for j in range(2*n)] for i in range(2*n)]
 for i in range(n):
  for j in range(i+1,n):
   z=v[i][j]
   if z:
    for eps in range(2):w[2*i+eps][2*j+(eps if z<0 else 1-eps)]=-abs(z)
 return w
def height(a):return max(abs(z) for row in a for z in row)
def energy(a):return sum(a[i][j]**2 for i in range(len(a)) for j in range(i+1,len(a)))
def mulpoly(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def main():
 start=perf_counter()
 native={n:(((_J_PROGRAM if n in ('main.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / n)).read_bytes() for n in ("readme.md","main.py","result.json")}
 author=json.loads(native["result.json"])
 assert author["status"]=="complete" and author["target_count"]==0
 stats=Counter();found=[]
 def visit(support,weights,kind):
  stats[kind+"_supports"]+=1
  rows={p//4 for p in support};cols={p%4 for p in support}
  if len(rows)<3 or len(cols)<3:
   stats[kind+"_rank_support_exclusions"]+=1
   return
  pivots={min(p for p in support if p//4==r) for r in rows}
  free=[p for p in support if p not in pivots]
  for signs in product((-1,1),repeat=len(free)):
   a=[[0]*4 for _ in range(4)]
   for p,w in zip(support,weights):a[p//4][p%4]=w
   for p,sign in zip(free,signs):a[p//4][p%4]*=sign
   stats[kind+"_row_sign_representatives"]+=1
   assert sum(z*z for row in a for z in row)==8
   if e2_of_b(a)!=18:continue
   stats[kind+"_e2_matches"]+=1
   if e3_of_b(a)!=9:continue
   stats[kind+"_e3_matches"]+=1
   if determinant4(a)!=0:continue
   found.append(a)
  if stats[kind+"_supports"]%500==0:
   assert perf_counter()-start<CAP,"declared checker cap"
 for support in combinations(range(16),8):visit(support,[1]*8,"eight_units")
 for doubled in range(16):
  others=[p for p in range(16) if p!=doubled]
  for units in combinations(others,4):
   support=sorted((doubled,)+units)
   visit(support,[2 if p==doubled else 1 for p in support],"one_double")
 assert stats["eight_units_supports"]==12870==author["stages"]["eight_units_supports"]
 assert stats["one_double_supports"]==21840==author["stages"]["one_double_supports"]
 assert len(list(combinations(range(16),2)))==120==author["two_double_supports_rejected_by_rank"]
 assert found==author["targets"]==[]
 assert author["absolute_polynomial_histogram"]==[]
 controls=[]
 for name,b in (("B5",[[1,0,1],[0,1,1],[0,-1,1],[0,0,1],[0,1,0]]),
                ("B7",[[1,0,1],[0,1,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1]])):
  v=proper(b);av=proper([[abs(z) for z in row] for row in b]);w=literal_cover(v)
  p,pa,pw=map(pencil_coefficients,(v,av,w))
  got={"B":b,"gram":gram(b),"absolute_gram":gram([[abs(z) for z in row] for row in b]),
       "V":v,"absolute_V":av,"cover":w,"original":p,"absolute":pa,"cover_polynomial":pw,
       "ranks":list(map(len,(v,av,w))),"heights":list(map(height,(v,av,w))),
       "energies":list(map(energy,(v,av,w)))}
  assert set(got)==set(author["controls"][name]),set(author["controls"][name])
  assert got==author["controls"][name],name
  assert pw==mulpoly(p,pa)
  controls.append({"name":name,"all_control_fields_equal":True,"degrees":got["ranks"],
                   "method":"complete integer triangular-inverse Newton coefficient arrays"})
 assert perf_counter()-start<CAP
 for n,b in native.items():assert (((_J_PROGRAM if n in ('main.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / n)).read_bytes()==b,n
 return {'status': 'passed', 'method': 'all energy-eight supports; only row-first-sign normalization; squared B minors; full inverse/Newton pencils', 'scope': 'entire declared 4x4 integer energy-eight class and both complete B5/B7 controls', 'stages': dict(stats), 'two_double_rank_exclusions': 120, 'targets': found, 'controls': controls, 'author_imports': False, 'third_party_imports': False}
if __name__=="__main__":
 result=main()
 ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(result,indent=2))

