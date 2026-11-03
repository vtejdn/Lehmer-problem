"""Exact author certificate independent of ground_roots and resultant routines.

Full 7-by-7 permutation determinant; explicit quadratic Sylvester identity;
integer roots tested by the proved constant-term divisibility criterion.
This is an author second implementation, not an independent human/agent review.
"""
from itertools import permutations
from math import isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp

HOME=(_J_PROGRAM / 'verify.py').parent
t,h,k=sp.symbols('t h k')
vars6=sp.symbols('a b c d e f')
a,b,c,d,e,f=vars6
B=sp.Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1]])
C=sp.Matrix([[1,a,b,c],[0,1,d,e],[0,0,1,f],[0,0,0,1]])
V=sp.eye(7);V[:3,3:]=-B;V[3:,3:]=C
M=t*V+V.T
terms=[]
nonzero=0
for perm in permutations(range(7)):
    if any(M[i,perm[i]]==0 for i in range(7)): continue
    sign=(-1)**sum(perm[i]>perm[j] for i in range(7) for j in range(i+1,7))
    term=sign
    for i in range(7): term*=M[i,perm[i]]
    terms.append(term);nonzero+=1
P=sp.Poly(sp.expand(sum(terms)),t)
assert P.degree()==7 and P.all_coeffs()==P.all_coeffs()[::-1]
search=json.loads(((_J_OUTPUT / 'search_result.json')).read_text(encoding='utf-8'))
expressions=[sp.sympify(search['coefficient_equations'][name]) for name in ['t6','t5','t4']]
assert all(sp.expand(P.nth(i)-ex)==0 for i,ex in zip([6,5,4],expressions))
rev={a:f,b:e,c:c,d:d,e:b,f:a}
assert sp.expand(P.as_expr().subs(rev,simultaneous=True)-P.as_expr())==0
x=sp.symbols('x')
A,D,H=expressions
trace=x**3+(A-1)*x**2+(D-A-2)*x+H-D-A+1
assert sp.expand((t+1)*t**3*trace.subs(x,t+1/t)-P.as_expr())==0
v0=sp.Matrix([1,-1,1,-1])
z=sp.Matrix([a-b+c,b-c-d+e,c-e+f,1,-1,1,-1])
assert ((V.T-V)*z).applyfunc(sp.expand)==sp.zeros(7,1)
assert sp.expand(sp.diff(P.as_expr(),t).subs(t,-1)-(z.T*V*z)[0])==0

def integer_roots_by_divisors(expr,var):
    p=sp.Poly(expr,var)
    assert not p.is_zero
    roots=[]
    while p.degree()>0 and p.nth(0)==0:
        if 0 not in roots: roots.append(0)
        p=sp.Poly(p.as_expr()/var,var)
    constant=abs(int(p.nth(0)))
    assert constant>0
    divisors=set()
    for i in range(1,isqrt(constant)+1):
        if constant%i==0: divisors.update([i,constant//i])
    for i in sorted(divisors):
        for signed in [-i,i]:
            if p.eval(signed)==0: roots.append(signed)
    obstruction=None
    for modulus in range(2,101):
        residues=[i for i in range(modulus) if int(p.eval(i))%modulus==0]
        if not residues:
            obstruction=modulus
            break
    return sorted(roots),{'zero_removed_polynomial':str(p.as_expr()),
                        'constant_abs':constant,'positive_divisors':sorted(divisors),
                        'zero_free_modulus':obstruction}

fiber=json.loads(((_J_OUTPUT / 'fiber_result.json')).read_text(encoding='utf-8'))
rows=[]
for record in fiber['records']:
    u,v,w=record['kernel'];R=u*u+v*v+w*w+u-v+w-1
    subs={a:h-u,b:k+h,c:k,d:k+R+v,e:k+R-h,f:R-h-w}
    p=sp.Poly(sp.expand(expressions[0].subs(subs)),h)
    q=sp.Poly(sp.expand((expressions[1]+1).subs(subs)),h)
    assert p.degree()==q.degree()==2
    a2,a1,a0=p.all_coeffs();b2,b1,b0=q.all_coeffs()
    res=sp.expand((a2*b0-a0*b2)**2-(a2*b1-a1*b2)*(a1*b0-a0*b1))
    assert sp.expand(res-sp.sympify(record['resultant']))==0
    kroots,cert=integer_roots_by_divisors(res,k)
    assert kroots==record['integer_k']
    remaining=[]
    for kval in kroots:
        ph=sp.expand(p.as_expr().subs(k,kval))
        qh=sp.Poly(q.as_expr().subs(k,kval),h)
        assert ph==0 and qh.degree()==2
        A,D,H=map(int,qh.all_coeffs())
        disc=D*D-4*A*H
        assert disc in [20,53] and isqrt(disc)**2 != disc
        remaining.append({'k':kval,'quadratic':str(qh.as_expr()),'discriminant':disc})
    rows.append({'kernel':[u,v,w],'resultant':str(sp.factor(res)),
                 'integer_k':kroots,'integer_divisor_certificate':cert,
                 'remaining_quadratics':remaining})
assert not fiber['witnesses']
out={'full_symbolic_determinant_terms':nonzero,'coefficient_identity':True,
     'core_reversal_identity':True,'full_trace_cubic_identity':True,
     'primitive_kernel_identity':True,'kernel_norm_derivative_identity':True,
     'quadratic_resultant_identity':True,'fiber_count':len(rows),
     'all_27_integer_fibers_excluded':True,'records':rows,
     'scope':'Author second exact implementation, not an independent review. No ground_roots or resultant call.'}
((_J_OUTPUT / 'verification.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:val for key,val in out.items() if key!='records'},indent=2))
print('Unique reversal representatives:')
for row in rows:
    if row['kernel'][0]<=row['kernel'][2]:
        print(row['kernel'],row['integer_k'],row['integer_divisor_certificate']['zero_free_modulus'],row['resultant'])
