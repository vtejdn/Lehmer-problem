"""Independent D133/J60 mathematical-payload verification; no author imports.

The draft is not a runtime input. Native bytes are observed within this run only;
no historical digest or revision gate is used. The complete declared prefix graph
is rebuilt breadth first by a rank-one formula, and terminal impossibility is
certified independently by complete residue sets. Field traversal counts use the
declared ordering but that same separately derived rank-one formula. All full
polynomials use integer Bareiss evaluations and rational forward interpolation.
Declared review caps: 20,000 prefix edges, 200,000 calls per field, 120 seconds.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
from collections import Counter, deque
from fractions import Fraction
from math import isqrt, gcd, factorial
import json
import time
import sympy as sp

HOME = (_J_PROGRAM / 'review_independent.py').parent
NATIVE = ['readme.md', 'terminal.py', 'terminal_result.json',
          'congruence.py', 'congruence_result.json', 'control.py',
          'control_result.json', 'historical_control.py',
          'historical_control_result.json']
V = ((0,-1,-2,0,-1,0), (1,0,-1,1,0,1), (2,1,0,2,1,1),
     (0,-1,-1,0,-1,0), (1,-1,-1,1,0,1), (1,-1,-1,0,-1,0))
TARGET = [1,-2,1,-1,1,-2,1]

def matrix(a):
    return tuple(tuple(int(x) for x in row) for row in a)

def determinant(a):
    a = [list(row) for row in a]
    n = len(a)
    if not n: return 1
    sign, prev = 1, 1
    for k in range(n-1):
        if not a[k][k]:
            r = next((r for r in range(k+1,n) if a[r][k]), None)
            if r is None: return 0
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val = pivot*a[i][j]-a[i][k]*a[k][j]
                assert val % prev == 0
                a[i][j] = val//prev
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]

def polynomial(a):
    n = len(a)
    diffs = [determinant([[t*a[i][j]+a[j][i] for j in range(n)]
                          for i in range(n)]) for t in range(n+1)]
    out = [Fraction(0)]*(n+1)
    falling = [Fraction(1)]
    for k in range(n+1):
        for i,v in enumerate(falling): out[i] += diffs[0]*v/factorial(k)
        diffs = [diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
        nxt = [Fraction(0)]*(len(falling)+1)
        for i,v in enumerate(falling):
            nxt[i] -= k*v
            nxt[i+1] += v
        falling = nxt
    assert all(v.denominator == 1 for v in out)
    return [int(v) for v in out]

def multiply_poly(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return c

def quadratic(a,x):
    n = len(a)
    return sum(a[i][j]*x[i]*x[j] for i in range(n) for j in range(n))

def congruence(a,q):
    n = len(a)
    return tuple(tuple(sum(q[r][i]*a[r][s]*q[s][j]
                           for r in range(n) for s in range(n))
                       for j in range(n)) for i in range(n))

def child(a,x,mod=None):
    n = len(a)
    assert quadratic(a,x) == 1 if mod is None else quadratic(a,x)%mod == 1
    omit = next(i for i,v in enumerate(x) if v)
    assert x[omit] == 1
    keep = [i for i in range(n) if i != omit]
    right = [sum(a[i][j]*x[j] for j in range(n)) for i in range(n)]
    left = [sum(x[i]*a[i][j] for i in range(n)) for j in range(n)]
    b = tuple(tuple(a[i][j]-right[i]*left[j] for j in keep) for i in keep)
    if mod is not None: b = tuple(tuple(v%mod for v in row) for row in b)
    return b

def cube_pivots(a):
    n = len(a)
    return [x for x in product((-1,0,1),repeat=n)
            if any(x) and next(v for v in x if v)==1 and quadratic(a,x)==1]

def prefix_graph(deadline):
    queue = deque([V]); seen = {V}; terminals = set()
    counts = Counter(calls=1,dimension_6=1)
    unique = Counter({6:1})
    while queue:
        assert time.perf_counter()<deadline
        a=queue.popleft(); n=len(a)
        assert determinant(a)==1
        if n==2:
            terminals.add(a)
            if a[0][0]==a[1][1]==0: kind='zero_quadratic'
            else:
                k=a[0][1]-a[1][0]
                kind='semidefinite' if k*k==4 else 'indefinite' if k*k>4 else 'definite'
            counts['binary_'+kind]+=1
            continue
        roots=cube_pivots(a)
        counts['permitted_prefix_pivots']+=len(roots)
        if not roots: counts['no_small_prefix_pivot']+=1
        for x in roots:
            b=child(a,x); counts['calls']+=1; counts[f'dimension_{n-1}']+=1
            assert counts['calls']<=20000
            if b in seen: counts['duplicate_forms']+=1
            else:
                seen.add(b); unique[n-1]+=1; queue.append(b)
    return counts,unique,terminals

def check_binary_row(row,solution_required=False):
    form=matrix(row['form']); a,b=form[0]; c,d=form[1]
    assert a*d-b*c==1
    if a==d==0:
        assert row=={'kind':'zero_quadratic','solution':None,'form':[list(x) for x in form]}
        return
    swapped=a==0
    if swapped: a,b,c,d=d,c,b,a
    delta=(b-c)**2-4
    assert row['swapped']==swapped and row['discriminant']==delta
    if delta==0:
        assert row['kind']=='semidefinite' and row['bound'] is None
        assert row['y_values_tested']==0
    elif delta>0:
        bound=isqrt(4*abs(a))+1
        assert row['kind']=='indefinite' and row['bound']==bound
        # Check the exact declared first-hit count as a historical implementation
        # field, independent of the residue proof of every negative conclusion.
        count=0; first=None
        for y in range(-bound,bound+1):
            count+=1; z=delta*y*y+4*a
            if z<0: continue
            rt=isqrt(z)
            if rt*rt!=z: continue
            for u in sorted({rt,-rt}):
                if (u-(b+c)*y)%(2*a)==0:
                    first=[(u-(b+c)*y)//(2*a),y]; break
            if first is not None: break
        if first is not None and swapped: first.reverse()
        assert row['y_values_tested']==count and row['solution']==first
    else:
        raise AssertionError('unexpected saved definite form')
    if solution_required:
        assert row['solution'] is not None
        assert quadratic(form,row['solution'])==1 and gcd(*row['solution'])==1
    else:
        assert row['solution'] is None

def field_counts(p,deadline):
    counts=Counter(); seen=set()
    def visit(a):
        assert time.perf_counter()<deadline
        counts['calls']+=1; n=len(a); counts[f'dimension_{n}']+=1
        assert counts['calls']<=200000
        if a in seen: counts['duplicates']+=1; return False
        seen.add(a)
        if n==1: return a==((1,),)
        roots=[x for x in product(range(p),repeat=n)
               if any(x) and next(v for v in x if v)==1 and quadratic(a,x)%p==1]
        roots.sort(key=lambda x:(sum(v!=0 for v in x),x))
        counts['permitted_roots']+=len(roots)
        for x in roots:
            if visit(child(a,x,p)): return True
        return False
    assert visit(tuple(tuple(v%p for v in row) for row in V))
    return counts

def sheet_lift(a,proper=False):
    n=len(a); w=[[0]*(2*n) for _ in range(2*n)]
    if proper:
        for i in range(2*n):w[i][i]=1
    for i in range(n):
        for j in range(n):
            if proper and i>=j:continue
            v=a[i][j]
            if v<=0:
                w[2*i][2*j]=w[2*i+1][2*j+1]=v
            else:
                w[2*i][2*j+1]=w[2*i+1][2*j]=-v
    return matrix(w)

def run():
    before={n:(((_J_PROGRAM if n in ('congruence.py', 'control.py', 'historical_control.py', 'readme.md', 'review_independent.py', 'terminal.py') else _J_OUTPUT) / n)).read_bytes() for n in NATIVE}
    start=time.perf_counter(); deadline=start+120
    data={n:json.loads(before[n]) for n in NATIVE if n.endswith('.json')}
    term=data['terminal_result.json']; cong=data['congruence_result.json']
    now=data['control_result.json']; old=data['historical_control_result.json']
    assert matrix(term['initial_matrix'])==V and determinant(V)==1
    assert polynomial(V)==TARGET
    neg=matrix([[-abs(v) for v in row] for row in V]); lifted=sheet_lift(V)
    absolute=[-1,0,7,11,7,0,-1]
    assert polynomial(neg)==absolute
    assert polynomial(lifted)==multiply_poly(TARGET,absolute)
    assert max(abs(x) for row in V for x in row)==2
    assert sum(x*x for row in V for x in row)==33
    assert sum(x*x for row in lifted for x in row)==66
    counts,unique,ends=prefix_graph(deadline)
    assert dict(counts)==term['counts']
    assert term['stop_reason'] is None and term['found'] is False and term['tree_complete'] is True
    assert term['scope']==dict(prefix_dimensions=[6,5,4,3],prefix_cube=[-1,1],terminal_dimension=2,
        terminal_domain='all integer vectors; exact arithmetic criterion',node_cap=20000)
    saved={matrix(r['form']):r for r in term['terminals']}
    assert len(saved)==len(term['terminals'])==89 and set(saved)==ends
    for form,row in saved.items():
        a=V
        for x in row['prefix']:
            assert tuple(x) in cube_pivots(a)
            a=child(a,x)
        assert a==form and len(row['prefix'])==4
        check_binary_row({k:v for k,v in row.items() if k!='prefix'})
    obstructions=Counter(); certificates={matrix(r['form']):r['certificate'] for r in cong['binary_obstructions']}
    assert set(certificates)==ends and len(cong['binary_obstructions'])==89
    residue_pair_count=0
    for a in sorted(ends):
        hit=None
        for mod in range(2,25):
            vals=sorted({quadratic(a,(x,y))%mod for x in range(mod) for y in range(mod)})
            residue_pair_count+=mod*mod
            if 1 not in vals:
                hit={'modulus':mod,'represented_residues':vals}; break
        assert hit==certificates[a] and hit is not None
        obstructions[str(hit['modulus'])]+=1
    assert dict(obstructions)==cong['binary_obstruction_counts']
    assert cong['binary_scope']==dict(forms=89,moduli=list(range(2,25)))
    fields=[]
    for row in cong['field_tests']:
        p=row['prime']; assert p in(2,3)
        assert row['node_cap']==200000
        assert row['found'] is True and row['stop_reason'] is None and row['complete_failure'] is False
        result=field_counts(p,deadline); assert dict(result)==row['counts']
        q=matrix(row['basis']); det=determinant(q)%p
        assert det==row['basis_determinant_modp'] and det!=0
        v=tuple(tuple(x%p for x in rr) for rr in congruence(V,q))
        assert v==matrix(row['upper_matrix'])
        assert all(v[i][i]==1 for i in range(6)) and all(v[i][j]==0 for i in range(6) for j in range(i))
        pol=[v%p for v in polynomial(v)]
        assert pol==row['full_polynomial_modp']==[v%p for v in TARGET]
        fields.append({'prime':p,'counts':dict(result),'witness_verified':True,'full_polynomial':pol})
    assert {r['prime'] for r in fields}=={2,3}
    # Symbolic binary identities are separate rational-polynomial calculations.
    a,b,c=sp.symbols('a b c',nonzero=True); d=(1+b*c)/a
    bmat=sp.Matrix([[a,b],[c,d]]); hmat=sp.Matrix([[-c,-d],[a,b]])
    assert (hmat.T*bmat*hmat-bmat).applyfunc(sp.simplify)==sp.zeros(2)
    x,y=sp.symbols('x y'); h=b+c; k=b-c; disc=k*k-4
    u=2*a*x+h*y; xp=-c*x-d*y; yp=a*x+b*y
    assert sp.simplify(2*a*xp+h*yp-(k*u+disc*y)/2)==0
    assert sp.simplify(yp-(u+k*y)/2)==0
    n=sp.symbols('n',integer=True); smat=sp.Matrix([[n,n+1],[n-1,n]])
    amat=sp.Matrix([[1,3],[0,1]]); expected=sp.Matrix([[5*n*n-5*n+1,5*n*n],[5*n*n-3,5*n*n+5*n+1]])
    assert (smat.T*amat*smat-expected).applyfunc(sp.expand)==sp.zeros(2)
    assert sp.expand(sum(v*v for v in expected))==100*n**4+40*n*n+11
    assert [[str(sp.expand(v)) for v in row] for row in expected.tolist()]==now['all_parameter_matrix_formula']
    assert sp.expand(sp.sympify(now['all_parameter_squared_entry_sum'],locals={'n':n})-(100*n**4+40*n*n+11))==0
    # Remove only the documented historical matrix field; every other field must
    # equal the current output, while the old matrix is independently checked.
    old_compare=json.loads(json.dumps(old)); new_compare=json.loads(json.dumps(now))
    changed=[]; A=((1,3),(0,1)); Q=[1,-7,1]; Q2=multiply_poly(Q,Q)
    assert now['scope']==[2,3,17,101] and now['original_polynomial']==Q and now['passed'] is True
    for row,orow in zip(now['rows'],old['rows']):
        nn=row['n']; v=matrix([[5*nn*nn-5*nn+1,5*nn*nn],[5*nn*nn-3,5*nn*nn+5*nn+1]])
        assert v==matrix(row['matrix']) and determinant(v)==1
        qb=matrix(row['solver_basis']); eb=matrix(row['explicit_basis'])
        assert eb==((nn,-nn-1),(1-nn,nn))
        assert determinant(qb)==determinant(eb)==1
        assert congruence(v,qb)==congruence(v,eb)==matrix(row['positive_matrix'])==A
        assert list(qb[i][0] for i in range(2))==row['solver']['solution']
        check_binary_row(row['solver'],True)
        vals=sorted({quadratic(v,p) for p in product((-1,0,1),repeat=2) if any(p)})
        assert vals==row['cube_nonzero_values']==sorted({5*nn*nn-5*nn+1,5*nn*nn+5*nn+1,20*nn*nn-1,5})
        assert row['initial_height']==5*nn*nn+5*nn+1
        assert row['initial_squared_entry_sum']==100*nn**4+40*nn*nn+11
        assert row['relaxed_cover_squared_entry_sum']==2*row['initial_squared_entry_sum']
        assert row['proper_height']==3 and row['proper_energy']==9 and row['proper_cover_energy']==18
        assert polynomial(v)==polynomial([[-abs(x) for x in rr] for rr in v])==row['full_absolute_polynomial']==Q
        assert polynomial(sheet_lift(v))==row['full_cover_polynomial']==Q2
        proper=sheet_lift(A,True); historical=sheet_lift(A)
        assert matrix(row['proper_cover_matrix'])==proper
        assert matrix(orow['proper_cover_matrix'])==historical
        assert polynomial(proper)==polynomial(historical)==Q2
        assert all(proper[i][i]==1 for i in range(4))
        assert all(proper[i][j]==0 for i in range(4) for j in range(i))
        assert any(historical[i][j]!=0 for i in range(4) for j in range(i))
        assert sum(proper[i][j]**2 for i in range(4) for j in range(i+1,4))==18
        assert sum(historical[i][j]**2 for i in range(4) for j in range(i+1,4))==20
        changed.append({'n':nn,'current_proper_energy':18,'historical_mislabeled_matrix_upper_energy':20,
                        'both_full_polynomials':Q2,'matrices_differ':proper!=historical})
    for out in (old_compare,new_compare):
        for row in out['rows']:row.pop('proper_cover_matrix')
    assert old_compare==new_compare
    after={name:(((_J_PROGRAM if name in ('congruence.py', 'control.py', 'historical_control.py', 'readme.md', 'review_independent.py', 'terminal.py') else _J_OUTPUT) / name)).read_bytes() for name in NATIVE}
    assert before==after, 'reviewer must not modify author inputs during this execution'
    return dict(passed=True, method='breadth-first exact rank-one graph; complete residues; independent field graph; Bareiss interpolation', caps=dict(prefix_calls=20000, field_calls=200000), prefix_counts=dict(counts), unique_by_dimension=dict(unique), terminal_forms=89, modular_obstructions=dict(obstructions), residue_pairs_checked=residue_pair_count, field_results=fields, binary_symbolic_isometry_and_controls=True, original_target_and_full_absolute_cover=True, all_four_integer_controls=True, historical_correction=changed, draft_required=False)

if __name__=='__main__':
    output=run()
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output))
