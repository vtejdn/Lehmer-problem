"""Independent finite J66 certificate; no imports of author implementations.
Declared scope: three original inputs, k=1,2, all retained 16-step paths,
all saved rational isolations and full costs; 120-second reviewer cap.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from itertools import permutations
from math import gcd, factorial, comb, log
from functools import reduce
import json, time, platform

BASE=(_J_PROGRAM / 'review_independent.py').parent
START=time.perf_counter()
def gate():
    if time.perf_counter()-START>120: raise RuntimeError('independent 120-second cap reached')
def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a
def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,k): return trim([k*x for x in a])
def rem(a,b):
    a=list(map(F,a)); b=list(map(F,b))
    while len(a)>=len(b) and any(a):
        k=a[-1]/b[-1]; j=len(a)-len(b)
        for i,x in enumerate(b): a[i+j]-=k*x
        a=trim(a)
    return a
def ev(a,x):
    y=0
    for c in reversed(a): y=y*x+c
    return y
def derivative(a): return [i*a[i] for i in range(1,len(a))] or [0]
def sturm(a):
    out=[list(map(F,a)),list(map(F,derivative(a)))]
    while any(out[-1]):
        nxt=scale(rem(out[-2],out[-1]),-1)
        if not any(nxt): break
        out.append(nxt)
    return out
def variations(seq,x):
    v=[ev(a,x) for a in seq]; v=[1 if z>0 else -1 for z in v if z]
    return sum(v[i]!=v[i-1] for i in range(1,len(v)))
def root_count(a,l,u):
    assert ev(a,l) and ev(a,u)
    seq=sturm(a); return variations(seq,l)-variations(seq,u)
def check_intervals(a,intervals):
    last=None
    for bounds,m in intervals:
        lo,hi=map(F,bounds); assert m==1 and lo<=hi
        if last is not None: assert last<lo
        if lo==hi: assert ev(a,lo)==0
        else: assert root_count(a,lo,hi)==1
        last=hi
    assert len(intervals)==len(a)-1

def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def mi(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def ma(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def ms(A,c): return [[c*x for x in row] for row in A]
def companion(a):
    n=len(a)-1; assert a[-1]==1
    T=[[0]*n for _ in range(n)]
    for j in range(n-1): T[j+1][j]=1
    for i in range(n): T[i][-1]=-a[i]
    return T
def matrix_poly(a,T):
    out=[[0]*len(T) for _ in T]; I=mi(len(T))
    for c in reversed(a): out=ma(mm(out,T),ms(I,c))
    return out
def det(A):
    A=[row[:] for row in A]; n=len(A); old=1; sg=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]),None)
            if j is None:return 0
            A[k],A[j]=A[j],A[k]; sg=-sg
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=A[i][j]*pivot-A[i][k]*A[k][j]
                assert z%old==0
                A[i][j]=z//old
        for i in range(k+1,n): A[i][k]=0
        old=pivot
    return sg*A[-1][-1]

def spadd(a,b):
    out=dict(a)
    for u,v in b.items(): out[u]=out.get(u,0)+v
    return {u:v for u,v in out.items() if v}
def spprod(a,b):
    out={}
    for k,(u,c) in enumerate(a.items()):
        if k%64==0:gate()
        for v,d in b.items():
            w=tuple(x+y for x,y in zip(u,v)); out[w]=out.get(w,0)+c*d
    return {u:c for u,c in out.items() if c}
def norm_form(matrices):
    n=len(matrices); out={}; zero=(0,)*n
    for perm in permutations(range(n)):
        sg=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term={zero:sg}
        for i,j in enumerate(perm):
            linear={tuple(int(k==l) for l in range(n)):matrices[k][i][j] for k in range(n) if matrices[k][i][j]}
            term=spprod(term,linear)
        out=spadd(out,term)
    return out

def spherical_integral(poly,s):
    # Gaussian Wick moments divided by the independent radial moment.
    total=F(0)
    for powers,c in poly.items():
        if any(p&1 for p in powers):continue
        halves=[p//2 for p in powers]; h=sum(halves)
        gaussian=1
        for k in halves: gaussian*=factorial(2*k)//(2**k*factorial(k))
        radial=1
        for k in range(h):radial*=s+2*k
        total+=F(c*gaussian,radial)
    return total

def fp_rem(a,b,p):
    a=trim([x%p for x in a]);b=trim([x%p for x in b])
    while len(a)>=len(b) and any(a):
        c=a[-1]*pow(b[-1],-1,p)%p;j=len(a)-len(b)
        for i,x in enumerate(b):a[i+j]=(a[i+j]-c*x)%p
        a=trim(a)
    return a

def fp_pow(a,k,mod,p):
    out=[1]
    while k:
        if k&1:out=fp_rem(mul(out,a),mod,p)
        a=fp_rem(mul(a,a),mod,p);k//=2
    return out

def fp_gcd(a,b,p):
    while any(b):a,b=b,fp_rem(a,b,p)
    return trim(a)

def irreduc_prime(q):
    n=len(q)-1; divs=[l for l in range(2,n+1) if n%l==0 and all(l%d for d in range(2,l))]
    for p in (2,3,5,7,11,13):
        if any(fp_rem(add(fp_pow([0,1],p**n,q,p),[0,-1]),q,p)):continue
        if all(len(fp_gcd(q,add(fp_pow([0,1],p**(n//l),q,p),[0,-1]),p))==1 for l in divs):return p
    raise AssertionError('declared irreducibility primes exhausted')

def rounded_direction(g):
    high=max(map(abs,g)); assert high
    c=[]
    for x in g:
        y=F(1024*abs(x),high)+F(1,2)
        c.append((1 if x>=0 else -1)*(y.numerator//y.denominator))
    divisor=reduce(gcd,c);assert divisor
    return [x//divisor for x in c]
def fracstr(v):return f'{v.numerator}/{v.denominator}'
def polynomial_string_check(text,coeff,var):
    # The author display is checked at degree+1 exact integer points; it is
    # parsed only as polynomial syntax in the independently expected variable.
    import ast
    tree=ast.parse(text.replace('^','**'),mode='eval')
    def walk(node,x):
        if isinstance(node,ast.Expression):return walk(node.body,x)
        if isinstance(node,ast.Constant) and isinstance(node.value,int):return node.value
        if isinstance(node,ast.Name) and node.id==var:return x
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):return -walk(node.operand,x)
        if isinstance(node,ast.BinOp):
            a=walk(node.left,x);b=walk(node.right,x)
            if isinstance(node.op,ast.Add):return a+b
            if isinstance(node.op,ast.Sub):return a-b
            if isinstance(node.op,ast.Mult):return a*b
            if isinstance(node.op,ast.Pow):assert isinstance(b,int) and b>=0;return a**b
        raise AssertionError('unexpected polynomial display syntax')
    for x in range(len(coeff)+1):assert walk(tree,x)==ev(coeff,x)

INPUTS=[('quartic',[1,-1,-1,-1,1]),('sextic',[1,-1,0,-1,0,-1,1]),('Lehmer',[1,1,0,-1,-1,-1,-1,-1,0,1,1])]
native_names=['readme.md','derive.py','derivation.json','verify.py','verification.json']
native={name:(((_J_PROGRAM if name in ('derive.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / name)).read_bytes() for name in native_names if (((_J_PROGRAM if name in ('derive.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / name)).exists()}
draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0147.md')
draft_before=draft.read_bytes() if draft.exists() else None
saved=json.loads(((_J_OUTPUT / 'derivation.json')).read_text(encoding='utf-8'))
assert len(saved['rows'])==3
summary=[]
for (name,P),row in zip(INPUTS,saved['rows']):
    gate();assert row['name']==name
    s=(len(P)-1)//2; assert row['s']==s
    polynomial_string_check(row['P'],P,'t')
    # Trace polynomials are reconstructed from t^j+t^-j recurrence, not
    # the author's descending expansion/subtraction in t.
    trace=[[2],[0,1]]
    for j in range(2,s+1):trace.append(add(mul([0,1],trace[-1]),scale(trace[-2],-1)))
    Q=[P[s]]
    for j in range(1,s+1):Q=add(Q,scale(trace[j],P[s+j]))
    polynomial_string_check(row['Q'],Q,'x')
    prime=irreduc_prime(Q)
    check_intervals(Q,row['trace_root_intervals'])
    assert sum(F(b[0])>2 for b,_ in row['trace_root_intervals'])==1
    assert sum(-2<F(b[0]) and F(b[1])<2 for b,_ in row['trace_root_intervals'])==s-1
    # Q is totally real and irreducible. One internal embedding makes
    # tau^2-4 negative, so it is not a square in this totally real field;
    # t^s Q(t+t^-1) is consequently irreducible of degree 2s.
    T=companion(Q);I=mi(s);Umat=[I,T]
    for j in range(2,s):Umat.append(ma(mm(T,Umat[-1]),ms(Umat[-2],-1)))
    Umat=Umat[:s]
    nd=norm_form(Umat)
    assert nd=={tuple(x['exponent']):x['coefficient'] for x in row['norm_terms']}
    nsq=spprod(nd,nd); fourth=spprod(nsq,nsq)
    ends=ev(P,1)*ev(P,-1)
    moments=[]
    for k,poly,target in zip((1,2),(nsq,fourth),row['moments']):
        val=spherical_integral(poly,s);dimension=comb(k*s+s-1,s-1)
        assert target['k']==k and F(target['A'])==val and target['dimension']==dimension
        low=log(abs(ends))/(2*s)-log(2)/2+log(float(val))/(2*k*s)
        assert abs(target['lower_discovery']-low)<1e-12
        assert abs(target['upper_discovery']-(low+log(dimension)/(2*k*s)))<1e-12
        moments.append({'k':k,'exact_moment':fracstr(val),'dimension':dimension,'sparse_terms':len(poly)})
    starts=[[int(i==j) for i in range(s)] for j in range(s)]+[[1]*s,[1 if i%2==0 else -1 for i in range(s)]]
    assert len(row['paths'])==len(starts)
    best=None;paths_checked=0
    for start,path in zip(starts,row['paths']):
        c=start;assert len(path)==17
        for step,item in enumerate(path):
            gate();M=[[sum(c[k]*Umat[k][i][j] for k in range(s)) for j in range(s)] for i in range(s)]
            nv=det(M);energy=2*sum(x*x for x in c);ratio=F(abs(ends)*nv*nv,energy**s)
            assert item['step']==step and item['c']==c and item['norm']==nv and item['energy']==energy
            assert F(item['exp_dB'])==ratio
            assert abs(item['B_discovery']-log(float(ratio))/(2*s))<1e-12
            if best is None or ratio>best[0]:best=(ratio,c[:],nv,energy)
            if step<16:
                grad=[]
                for k in range(s):
                    value=0
                    for col in range(s):
                        replaced=[r[:] for r in M]
                        for i in range(s):replaced[i][col]=Umat[k][i][col]
                        value+=det(replaced)
                    grad.append(value)
                c=rounded_direction(grad)
            paths_checked+=1
    ratio,c,nv,energy=best;b=row['best']
    assert b['c']==c and b['norm']==nv and b['energy']==energy and F(b['exp_dB'])==ratio
    Ub=[[1],[0,1]]
    for j in range(2,s):Ub.append(add(mul([0,1],Ub[-1]),scale(Ub[-2],-1)))
    V=[0]
    for j in range(s):V=add(V,scale(Ub[j],c[j]))
    C=[0]*(2*s+1)
    for j in range(s):C[s+j+1]+=c[j];C[s-j-1]-=c[j]
    C=trim(C)
    polynomial_string_check(b['V'],V,'x');polynomial_string_check(b['C'],C,'t')
    resultant=det(matrix_poly(C,companion(P)))
    assert resultant==ends*nv*nv==b['resultant']
    content=reduce(gcd,C);leading=C[-1]
    assert content==1==b['content'] and leading==b['leading'] and len(C)-1==b['actual_degree']
    assert sum(x*x for x in C)==energy
    degree_mean=F(sum(i*x*x for i,x in enumerate(C)),energy)
    rho=F(sum(map(abs,C))**2,energy)
    assert F(b['degree_energy_mean'])==degree_mean
    assert F(b['rho_l1_over_l2_squared'])==rho
    check_intervals(V,b['trace_aux_intervals'])
    inside=root_count(V,F(-2),F(2)); assert inside==b['trace_aux_roots_inside_minus2_2']
    all_circle=inside==len(V)-1==s-1
    assert b['all_aux_roots_on_circle']==all_circle
    blo,bhi=map(F,b['beta_interval']);assert 1<blo<bhi and root_count(P,blo,bhi)==1
    assert b['certified_B_above_m']==(ratio>bhi**(2*s))
    assert abs(b['B_discovery']-log(float(ratio))/(2*s))<1e-12
    assert abs(b['m_discovery']-log(float((blo+bhi)/2)))<1e-12
    if name=='quartic':
        assert F(225,32)<blo**4 and b['certified_exp_dB_over_beta_d_exceeds'] is None
        # Global quartic norm optimization: N=c0^2+c0*c1-3*c1^2.
        # Max |N| on the unit circle equals 1+sqrt(17)/2, not this pilot.
        assert nd=={(2,0):1,(1,1):1,(0,2):-3}
        assert b['auxiliary_M_interval']==['512/1','512/1'] and all_circle
    else:
        factor=F(21,20) if name=='sextic' else F(7,5)
        assert F(b['certified_exp_dB_over_beta_d_exceeds'])==factor and ratio>factor*bhi**(2*s)
        if name=='sextic':assert all_circle and b['auxiliary_M_interval']==['512/1','512/1']
        else:
            lo,hi=map(F,b['trace_aux_intervals'][0][0]);assert F(-7,2)<lo<hi<F(-17,5)
            assert inside==3 and not all_circle
            # The exterior reciprocal auxiliary pair has modulus between3
            # and13/4 by monotonic u+1/u for u>1.
            assert 3+F(1,3)<F(17,5) and F(13,4)+F(4,13)>F(7,2)
            assert b['auxiliary_M_interval']==['1152/1','1248/1']
    summary.append({'name':name,'Q':Q,'trace_irreducibility_prime':prime,'norm_terms':len(nd),'moments':moments,'full_paths_steps':paths_checked,'best_vector':c,'full_original_resultant':resultant,'degree_energy_mean':fracstr(degree_mean),'rho_l1_over_l2_squared':fracstr(rho),'complete_root_intervals_checked':True})
for name,data in native.items():assert (((_J_PROGRAM if name in ('derive.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / name)).read_bytes()==data
if draft_before is not None: assert draft.read_bytes()==draft_before
result={'status': 'passed', 'scope': 'Same three declared inputs; complete norm forms, k=1,2, all deterministic paths, full original resultants and every saved root/cost bound. No directional or moment search expansion.', 'implementation': 'Integer companion matrices and Leibniz norm determinant; determinant column derivatives; exact Gaussian Wick/radial moments; independent rational Sturm counts and modular trace irreducibility. No author imports and no SymPy.', 'rows': summary, 'discovery_float_comparison': 'Display values only, tolerance 1e-12; all mathematical inequalities exact integers or Fraction.'}
gate()
((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
