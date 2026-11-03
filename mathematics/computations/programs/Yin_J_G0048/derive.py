"""Full exact localized-kernel determinant and all eight necessary fibers."""
from itertools import permutations
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp

HOME=(_J_PROGRAM / 'derive.py').parent
t=sp.symbols('t')
a,b,c,d,e,f=sp.symbols('a b c d e f')
B=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,1]])
C=sp.Matrix([[1,a,b,c],[0,1,d,e],[0,0,1,f],[0,0,0,1]])
V=sp.eye(7);V[:3,3:]=-B;V[3:,3:]=C
M=t*V+V.T
terms=[]
for perm in permutations(range(7)):
    if any(M[i,perm[i]]==0 for i in range(7)):continue
    s=(-1)**sum(perm[i]>perm[j] for i in range(7) for j in range(i+1,7))
    term=s
    for i in range(7):term*=M[i,perm[i]]
    terms.append(term)
p=sp.Poly(sp.expand(sum(terms)),t)
assert p.all_coeffs()==p.all_coeffs()[::-1]
z=sp.Matrix([c-b,e-d,f,0,0,1,-1])
assert ((V.T-V)*z).applyfunc(sp.expand)==sp.zeros(7,1)
norm=sp.expand((z.T*V*z)[0])
assert norm==sp.expand((c-b)**2+(e-d)**2+f*f+2-f)
assert sp.expand(sp.diff(p.as_expr(),t).subs(t,-1)-norm)==0
records=[]
for fval in [-1,2]:
    for u,v in [(1,0),(-1,0),(0,1),(0,-1)]:
        sub={c:b+u,e:d+v,f:fval}
        A,D,H=[sp.factor(p.nth(i).subs(sub)) for i in [6,5,4]]
        assert sp.expand(7-5*A+3*D-H)==5
        row={'f':fval,'u':u,'v':v,'A':str(A),'D_plus_one':str(sp.factor(D+1))}
        if fval==2:
            branches=[]
            for aval in [0,b*v-u*d]:
                assert sp.expand(A.subs(a,aval))==0
                branches.append({'a':str(aval),'D_plus_one':str(sp.factor((D+1).subs(a,aval)))})
            row['branches']=branches
        records.append(row)
out={'B':B.tolist(),'nonzero_determinant_terms':len(terms),
     'coefficients':{str(i):str(p.nth(i)) for i in [6,5,4]},
     'kernel':list(map(str,z)),'norm':str(norm),'records':records}
control={a:0,b:0,c:1,d:sp.sqrt(2),e:sp.sqrt(2),f:2}
negative={a:0,b:0,c:-1,d:-sp.sqrt(2),e:-sp.sqrt(2),f:-2}
P6=t**6-t**5-t**3-t+1
original=sp.Poly(sp.expand(p.as_expr().subs(control)),t)
absolute=sp.Poly(sp.expand(p.as_expr().subs(negative)),t)
assert original.as_expr()==sp.expand((t+1)*P6)
x=sp.symbols('x')
A,D,H=[absolute.nth(i) for i in [6,5,4]]
trace=x**3+(A-1)*x**2+(D-A-2)*x+H-D-A+1
assert sp.expand((t+1)*t**3*trace.subs(x,t+1/t)-absolute.as_expr())==0
out['nonintegral_control']={'entries':{str(var):str(value) for var,value in control.items()},
 'full_original':str(original.as_expr()),'full_absolute':str(absolute.as_expr()),
 'absolute_trace':str(trace),'absolute_trace_factorization':str(sp.factor(trace)),
 'full_cover':str(sp.expand(original.as_expr()*absolute.as_expr())),
 'height':2,'energy':13,'cover_energy':26,'integral':False}
((_J_OUTPUT / 'derivation.json')).write_text(json.dumps(out,indent=2,default=int)+'\n',encoding='utf-8')
print(json.dumps({'records':records,'nonintegral_control':out['nonintegral_control']},indent=2))
