"""Independent exact review: permutation polynomials and mod-eight Taylor lifts.
No author program imports. Native author files are read and compared within-run;
D125 is optional so this remains runnable after promotion. No historical gate.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product, permutations
from collections import Counter
from math import comb
import json, time

HERE=(_J_PROGRAM / 'review_independent.py').parent
H=((2,-1,0,0,0,0),(-1,2,-1,-2,0,2),(0,-1,2,1,-2,-2),
   (0,-2,1,2,1,-2),(0,0,-2,1,2,1),(0,2,-2,-2,1,2))
C=(-1,0,1,1,0,1)
Z=(0,)*6
ONE={Z:1}
PERMS=[(p,(-1)**sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))) for p in permutations(range(6))]
MATCH=[(p,s) for p,s in PERMS if all(p[i]<p[i+1] for i in (0,2,4)) and p[0]<p[2]<p[4]]
assert len(MATCH)==15

def add(a,b,scale=1):
    ans=dict(a)
    for m,v in b.items():
        ans[m]=ans.get(m,0)+scale*v
        if not ans[m]:del ans[m]
    return ans

def mul(a,b):
    ans={}
    for m,v in a.items():
        for n,w in b.items():
            k=tuple(x+y for x,y in zip(m,n))
            ans[k]=ans.get(k,0)+v*w
    return {m:v for m,v in ans.items() if v}

def const(v):return {Z:v} if v else {}
def variable(i):return {tuple(int(j==i) for j in range(6)):1}
def ev(a,x):
    ans=0
    for m,v in a.items():
        t=v
        for j,e in enumerate(m):
            if e:t*=x[j]**e
        ans+=t
    return ans

def gradient(a,x):
    out=[]
    for i in range(6):
        val=0
        for m,v in a.items():
            if m[i]:
                t=v*m[i]
                for j,e in enumerate(m):
                    power=e-int(i==j)
                    if power:t*=x[j]**power
                val+=t
        out.append(val)
    return out

def bareiss(a):
    a=[list(r) for r in a];n=len(a);den=1;sgn=1
    for k in range(n-1):
        row=next((i for i in range(k,n) if a[i][k]),None)
        if row is None:return 0
        if row!=k:a[k],a[row]=a[row],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*pivot-a[i][k]*a[k][j]
                assert v%den==0
                a[i][j]=v//den
        for i in range(k+1,n):a[i][k]=0
        den=pivot
    return sgn*a[-1][-1]

def own_model(i,j):
    cols=[[const(int(a==b)) for a in range(6)] for b in range(6)]
    cols[i]=[const(v) for v in C];cols[j]=[variable(a) for a in range(6)]
    gram=[[{} for _ in range(6)] for _ in range(6)]
    for a in range(6):
        for b in range(a+1,6):
            v={}
            for u in range(6):
                for w in range(6):
                    if H[u][w]:v=add(v,mul(cols[a][u],cols[b][w]),H[u][w])
            gram[a][b]=gram[b][a]=v
    coeff=[{} for _ in range(7)]
    # Each Leibniz term is t^asc*(t+1)^fixed times its offdiagonal product.
    for perm,sign in PERMS:
        term=ONE;asc=0;fixed=0
        for a,b in enumerate(perm):
            if a==b:fixed+=1
            else:
                term=mul(term,gram[a][b]);asc+=int(a<b)
        for z in range(fixed+1):coeff[asc+z]=add(coeff[asc+z],term,sign*comb(fixed,z))
    pf={}
    for perm,sign in MATCH:
        term=ONE
        for a in (0,2,4):term=mul(term,gram[perm[a]][perm[a+1]])
        pf=add(pf,term,sign)
    ell=add(variable(j),{},0)
    ell=add(const(0),variable(j),C[i]);ell=add(ell,variable(i),-C[j])
    norm={}
    for a in range(6):
        norm=add(norm,mul(variable(a),variable(a)))
        for b in range(a+1,6):norm=add(norm,mul(variable(a),variable(b)),H[a][b])
    assert all(sum(m)<=2 for a in coeff for m in a)
    assert all(sum(m)<=1 for m in pf)
    return {'ell':ell,'pf':pf,'norm_half':norm,'first':coeff[5]},coeff

def from_terms(ts):return {tuple(m):int(v) for v,m in ts if v}
def rank_two(a,b):
    x=[ev(a,tuple(int(z==j) for z in range(6))) for j in range(6)]
    y=[ev(b,tuple(int(z==j) for z in range(6))) for j in range(6)]
    return 2 if any(x[i]*y[j]!=x[j]*y[i] for i in range(6) for j in range(i+1,6)) else int(any(x) or any(y))


def parse_poly(expr):
    import ast
    def go(node):
        if isinstance(node,ast.Constant) and type(node.value) is int:return const(node.value)
        if isinstance(node,ast.Name) and node.id in ('x','y','z','w'):return variable(('x','y','z','w').index(node.id))
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):return add({},go(node.operand),-1)
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.UAdd):return go(node.operand)
        if isinstance(node,ast.BinOp):
            if isinstance(node.op,ast.Add):return add(go(node.left),go(node.right))
            if isinstance(node.op,ast.Sub):return add(go(node.left),go(node.right),-1)
            if isinstance(node.op,ast.Mult):return mul(go(node.left),go(node.right))
            if isinstance(node.op,ast.Pow) and isinstance(node.right,ast.Constant) and type(node.right.value) is int and node.right.value in (0,1,2):
                out=ONE
                for _ in range(node.right.value):out=mul(out,go(node.left))
                return out
        raise AssertionError(('unexpected polynomial syntax',expr))
    out=go(ast.parse(expr,mode='eval').body)
    assert all(sum(m)<=2 for m in out)
    return out

def compose(poly,sub):
    out={}
    for mon,co in poly.items():
        term=const(co)
        for i,e in enumerate(mon):
            for _ in range(e):term=mul(term,sub[i])
        out=add(out,term)
    return out

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def characteristic_from_unitriangular(v):
    # Complete characteristic polynomial of -V^-1 V^T by finite nilpotent inverse
    # and Newton trace identities, not determinant interpolation.
    n=len(v);eye=[[int(i==j) for j in range(n)] for i in range(n)]
    negu=[[int(i==j)-v[i][j] for j in range(n)] for i in range(n)]
    inv=[r[:] for r in eye];power=[r[:] for r in eye]
    for _ in range(1,n):
        power=mm(power,negu)
        inv=[[x+y for x,y in zip(a,b)] for a,b in zip(inv,power)]
    assert mm(inv,v)==eye and not any(x for row in mm(power,negu) for x in row)
    c=[[-x for x in row] for row in mm(inv,list(map(list,zip(*v))))]
    power=[r[:] for r in eye];traces=[];coeff=[1]
    for j in range(1,n+1):
        power=mm(power,c);traces.append(sum(power[i][i] for i in range(n)))
        numerator=-sum(coeff[j-z]*traces[z-1] for z in range(1,j+1))
        assert numerator%j==0
        coeff.append(numerator//j)
    return list(reversed(coeff))

def verify_controls(data):
    returned=[]
    for rec in data['controls']:
        i,j=rec['positions'];d=rec['second_root']
        cols=[[int(z==a) for z in range(6)] for a in range(6)];cols[i]=list(C);cols[j]=d
        q=list(map(list,zip(*cols)))
        g=mm(list(map(list,zip(*q))),mm([list(r) for r in H],q))
        v=[[int(a==b)+(g[a][b] if a<b else 0) for b in range(6)] for a in range(6)]
        vm=[[int(a==b)-(abs(v[a][b]) if a<b else 0) for b in range(6)] for a in range(6)]
        assert abs(bareiss(q))==1 and bareiss(g)==-1 and all(g[a][a]==2 for a in range(6))
        assert q==rec['basis_path_coordinates'] and g==rec['gram'] and v==rec['matrix']
        pp=characteristic_from_unitriangular(v);pm=characteristic_from_unitriangular(vm)
        assert pp==rec['original_polynomial'] and pm==rec['absolute_polynomial']
        w=[[int(a==b) for b in range(12)] for a in range(12)]
        for a in range(6):
            for b in range(a+1,6):
                for z in range(2):w[2*a+z][2*b+(z if v[a][b]<=0 else 1-z)]=-abs(v[a][b])
        cover=characteristic_from_unitriangular(w)
        convolution=[0]*13
        for a,x in enumerate(pp):
            for b,y in enumerate(pm):convolution[a+b]+=x*y
        assert cover==convolution==rec['full_cover_polynomial']
        for name,mat in [('height',v),('cover_height',w)]:assert max(abs(x) for row in mat for x in row)==rec[name]
        for name,mat in [('energy',v),('cover_energy',w)]:assert sum(mat[a][b]**2 for a in range(len(mat)) for b in range(a+1,len(mat)))==rec[name]
        returned.append({'positions':[i,j],'original_polynomial':pp,'absolute_polynomial':pm,'full_cover_polynomial':cover,'height':rec['height'],'energy':rec['energy']})
    return returned

def run():
    start=time.perf_counter()
    author={p.name:p.read_bytes() for p in (*HERE.iterdir(), *_J_OUTPUT.iterdir()) if p.is_file() and not p.name.startswith('review_')}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0125.md')
    draft_before=draft.read_bytes() if draft.exists() else None
    src=json.loads(author['mod4_result.json']);lift_src=json.loads(author['mod8_result.json'])
    con=json.loads(author['congruence_result.json']);elim=json.loads(author['elimination.json'])
    assert bareiss(H)==-1
    assert sum(C[i]*H[i][j]*C[j] for i in range(6) for j in range(6))==2
    std=(C[0]-C[1],C[1]-C[2],C[2]-C[3],C[3]-C[4],C[4]-C[5],C[5])
    assert std==(-1,-1,0,1,-1,1)
    hc=tuple(sum(H[i][j]*C[j] for j in range(6)) for i in range(6))
    assert hc==(-2,0,1,1,0,-2)
    null=tuple(C[i]+int(i==0) for i in range(6))
    assert null==(0,0,1,1,0,1)
    assert sum(null[i]*H[i][j]*null[j] for i in range(6) for j in range(6))==0
    assert sum(C[i]*H[i][j]*null[j] for i in range(6) for j in range(6))==0
    assert C[0]==-1 and null[0]==0 and C[1]==null[1]==0
    assert max(sum(abs(x) for x in row) for row in H)==9 and sum(abs(x) for x in hc)==6
    records=[];residue_total=0;lift_total=0;class_total=0;formula_fields=0
    models={}
    for rec in src['models']:
        i,j=rec['positions'];m,cp=own_model(i,j);models[i,j]=m
        for name in m:
            assert m[name]==from_terms(rec['terms'][name]),(i,j,name)
            formula_fields+=1
        assert rank_two(m['ell'],m['pf'])==rec['linear_rank']
        assert all(v%2==0 for v in add(m['pf'],m['ell'],-1).values())
        counts=Counter();surv={'F':[],'S6':[]};hist=Counter()
        for x in product(range(4),repeat=6):
            counts['residue_vectors']+=1;residue_total+=1
            e=ev(m['ell'],x)
            if e%4 not in (1,3):continue
            counts['unit_minor']+=1
            p=ev(m['pf'],x)
            if p%4 not in (1,3):continue
            counts['odd_pfaffian']+=1
            if ev(m['norm_half'],x)%4!=1:continue
            counts['norm_two']+=1
            a=ev(m['first'],x)%4
            if a==2:surv['F'].append(list(x))
            if a==0:surv['S6'].append(list(x))
            if a%2==0:
                assert (p*p-e*e)%8==0
                b=(p*p-e*e)//8
                assert (a+2*b)%4==2
                hist[f'{a},{b%2}']+=1;class_total+=1
        assert dict(counts)==rec['counts'],(i,j,'counts')
        assert surv==rec['survivors'],(i,j,'full residue sets')
        cr=next(x for x in con['positions'] if x['positions']==[i,j])
        assert dict(sorted(hist.items()))==cr['trace_residue_D_parity_histogram']
        assert sum(hist.values())==cr['even_trace_classes']
        lr=next(x for x in lift_src['positions'] if x['positions']==[i,j])
        actual={}
        for target,pf_target,a_target in [('F',3,-2),('S6',1,0)]:
            ct=Counter();out=[]
            for base in surv[target]:
                vals={key:ev(poly,base) for key,poly in m.items()}
                grad={key:gradient(poly,base) for key,poly in m.items()}
                for bits in product(range(2),repeat=6):
                    # Exact degree-two Taylor modulo8; quadratic increments are multiples of16.
                    v={key:(vals[key]+4*sum(u*b for u,b in zip(grad[key],bits)))%8 for key in m}
                    ct['lift_tests']+=1;lift_total+=1
                    if v['ell'] not in (1,7):continue
                    ct['unit_minor']+=1
                    if v['pf'] not in (pf_target%8,(-pf_target)%8):continue
                    ct['target_pfaffian']+=1
                    if v['norm_half']!=1:continue
                    ct['norm_two']+=1
                    if v['first']!=a_target%8:continue
                    out.append([base[z]+4*bits[z] for z in range(6)])
            assert dict(ct)==lr['targets'][target]['counts'],(i,j,target,'lift counts')
            assert out==lr['targets'][target]['survivors']==[]
            actual[target]=dict(counts=dict(ct),survivors=0)
        records.append(dict(positions=[i,j],mod4_survivors={key:len(v) for key,v in surv.items()},mod8=actual))
    assert len(records)==30 and residue_total==122880 and lift_total==229376 and class_total==3584
    # Every illustrative eliminated polynomial is independently substituted as a polynomial.
    m=models[0,2];substitution_checks=0
    for rec in elim['cases']:
        eps,delta,kk=rec['epsilon'],rec['delta'],rec['k']
        assert 2*kk==eps+delta
        x,y,z,w=[variable(a) for a in range(4)]
        sub=[add(add({},x,-1),const(-eps)),add(add(add({},x,2),z,-2),add(add({},w,-2),const(-kk))),x,y,z,w]
        assert compose(m['ell'],sub)==const(eps) and compose(m['pf'],sub)==const(delta)
        n=add(compose(m['norm_half'],sub),const(-1))
        a=add(compose(m['first'],sub),const(2 if rec['target']=='F' else 0))
        assert n==parse_poly(rec['norm_residual']) and a==parse_poly(rec['coefficient_residual'])
        for name,expected in [('norm_mod4',n),('coefficient_mod4',a),('difference_mod4',add(a,n,-1))]:
            got=parse_poly(rec[name])
            assert all(v%4==0 for v in add(expected,got,-1).values())
        substitution_checks+=7
    controls=verify_controls(json.loads(author['verification.json']))
    unchanged=all((((_J_PROGRAM if name in ('congruence.py', 'eliminate.py', 'exact.py', 'lift8.py', 'readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()==raw for name,raw in author.items())
    assert unchanged
    draft_unchanged=draft_before is None or draft.read_bytes()==draft_before
    assert draft_unchanged
    return dict(passed=True, method='independent sparse Leibniz coefficient polynomials; canonical matching Pfaffian; exact mod-eight Taylor lifts', source_imports=False, unbounded_first_root_family_exact_coefficients=True, full_cost_row_bounds_verified=True, formula_fields_checked=formula_fields, all_mod4_vectors=residue_total, complete_mod4_survivors={'F': sum((r['mod4_survivors']['F'] for r in records)), 'S6': sum((r['mod4_survivors']['S6'] for r in records))}, exact_mod8_binary_lifts=lift_total, all_mod8_survivors={'F': 0, 'S6': 0}, compressed_invariant_classes=class_total, elimination_exact_polynomial_checks=substitution_checks, complete_control_polynomials=controls, positions=records)

if __name__=='__main__':
    out=run();((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='positions'},indent=2))
