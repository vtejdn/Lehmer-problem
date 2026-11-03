"""Complete noncontributor J75 check; own J69/J72/J74 primitives reused: standard library, integer pencils/interpolation."""
import ast, itertools, json, math, sys, time
from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

HERE=(_J_PROGRAM / 'review_independent.py').parent
START=time.perf_counter(); CAP=120
# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def gate():
    if time.perf_counter()-START>CAP: raise TimeoutError('review aggregate120-second cap')
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def tr(A): return [list(r) for r in zip(*A)]
def mm(A,B): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def det(A):
    gate(); A=[row[:] for row in A]; n=len(A); old=1; sign=1
    if not n:return 1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:A[k],A[pivot]=A[pivot],A[k];sign=-sign
        z=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=z*A[i][j]-A[i][k]*A[k][j]
                assert v%old==0
                A[i][j]=v//old
            A[i][k]=0
        old=z
    return sign*A[-1][-1]
def pencil(V,x): return [[x*V[i][j]+V[j][i] for j in range(len(V))] for i in range(len(V))]
def padd(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):out[i]+=v
    for i,v in enumerate(b):out[i]+=v
    return out
def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return out
def interp(values,start=0):
    # Newton forward basis: delta^j f(start) * product(t-start-h)/j!.
    dif=[F(v) for v in values]; basis=[F(1)]; out=[F(0)]
    for j in range(len(values)):
        out=padd(out,[dif[0]*v for v in basis])
        dif=[dif[i+1]-dif[i] for i in range(len(dif)-1)]
        basis=[v/F(j+1) for v in pmul(basis,[-start-j,1])]
    out+= [F(0)]*(len(values)-len(out))
    assert all(v.denominator==1 for v in out)
    return [int(v) for v in out]
CACHE={}; PENCIL_CALLS=0
def coefficients(V):
    global PENCIL_CALLS
    key=tuple(map(tuple,V))
    if key not in CACHE:
        n=len(V); vals=[det(pencil(V,x)) for x in range(n+1)]
        PENCIL_CALLS+=n+1
        out=interp(vals); assert out[0]==out[-1]==1
        CACHE[key]=(out,vals)
    return CACHE[key]
def absolute(V):
    out=eye(len(V))
    for i,row in enumerate(V):
        for j in range(i+1,len(V)):out[i][j]=-abs(row[j])
    return out
def cover(V):
    out=eye(2*len(V))
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            a=V[i][j]
            for sheet in (0,1):
                dest=sheet if a<=0 else 1-sheet
                out[2*i+sheet][2*j+dest]=-abs(a)
    return out
def cost(V):
    entries=[V[i][j] for i in range(len(V)) for j in range(i+1,len(V))]
    return {'rank':len(V),'height':max([1]+list(map(abs,entries))),'energy':sum(a*a for a in entries)}
def append(U,c):
    n=len(U);out=eye(n+1)
    for i in range(n):out[i][:n]=U[i][:];out[i][n]=c[i]
    return out
def rotate(V):
    n=len(V); order=list(range(1,n))+[0]; W=eye(n)
    for i in range(n):
        for j in range(i+1,n):
            a,b=order[i],order[j];W[i][j]=V[a][b]+V[b][a]
    Q=[[0]*n for _ in range(n)]
    for j in range(1,n):Q[j][j-1]=1;Q[0][j-1]=-V[0][j]
    Q[0][-1]=-1
    assert abs(det(Q))==1 and mm(mm(tr(Q),V),Q)==W
    return W,Q

# Exact sparse multivariate polynomials. Only a restricted AST is accepted from native strings.
def plus(a,b):
    out=dict(a)
    for u,v in b.items():out[u]=out.get(u,0)+v
    return {u:v for u,v in out.items() if v}
def scale(a,c):return {u:v*c for u,v in a.items() if v*c}
def times(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            w=tuple(x+y for x,y in zip(u,v));out[w]=out.get(w,0)+c*d
    return {u:v for u,v in out.items() if v}
def const(c,n):return {(0,)*n:c} if c else {}
def variable(i,n):return {tuple(int(j==i) for j in range(n)):1}
def power(a,n,dim):
    out=const(1,dim)
    for _ in range(n):out=times(out,a)
    return out
def parse(text,names):
    dim=len(names)
    def visit(node):
        if isinstance(node,ast.Constant) and type(node.value)==int:return const(node.value,dim)
        if isinstance(node,ast.Name) and node.id in names:return variable(names.index(node.id),dim)
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,ast.USub):return scale(visit(node.operand),-1)
        if isinstance(node,ast.BinOp):
            a=visit(node.left)
            if isinstance(node.op,ast.Pow):
                assert isinstance(node.right,ast.Constant) and type(node.right.value)==int and 0<=node.right.value<=20
                return power(a,node.right.value,dim)
            b=visit(node.right)
            if isinstance(node.op,ast.Add):return plus(a,b)
            if isinstance(node.op,ast.Sub):return plus(a,scale(b,-1))
            if isinstance(node.op,ast.Mult):return times(a,b)
        raise ValueError('outside polynomial AST')
    return visit(ast.parse(text,mode='eval').body)
def poly_det(M,dim):
    n=len(M);out={}
    for perm in itertools.permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=const(sign,dim)
        for i,j in enumerate(perm):term=times(term,M[i][j])
        out=plus(out,term)
    return out

def aspoly(cs):return {(i,):c for i,c in enumerate(cs) if c}
def ev(cs,x):return sum(c*x**i for i,c in enumerate(cs))
def fraction_det(M):
    # Separate exact rational elimination for the two small weighted cyclic blocks.
    A=[[F(x) for x in row] for row in M];out=F(1);n=len(A)
    for k in range(n):
        i=next((i for i in range(k,n) if A[i][k]),None)
        if i is None:return 0
        if i!=k:A[i],A[k]=A[k],A[i];out=-out
        z=A[k][k];out*=z
        for i in range(k+1,n):
            q=A[i][k]/z
            for j in range(k+1,n):A[i][j]-=q*A[k][j]
            A[i][k]=0
    assert out.denominator==1;return int(out)
def trace_expand(cs):
    r=len(cs)-1;out={}
    for j,c in enumerate(cs):
        for k in range(j+1):
            e=r+j-2*k;out[e]=out.get(e,0)+c*math.comb(j,k)
    out={e:c for e,c in out.items() if c};assert min(out)>=0
    return [out.get(i,0) for i in range(max(out)+1)]
def one_complete(V,row):
    assert set(row)=={'matrix','coefficients_ascending','pencil_times','pencil_values','rank','height','energy'}
    assert row['matrix']==V
    cs,values=coefficients(V)
    assert row['coefficients_ascending']==cs and cs==cs[::-1]
    assert row['pencil_times']==list(range(len(V)+1)) and row['pencil_values']==values
    assert {key:row[key] for key in ('rank','height','energy')}==cost(V)
    return cs,len(values)

def trim(cs):
    cs=list(cs)
    while len(cs)>1 and cs[-1]==0:cs.pop()
    return cs

def divide(a,b):
    a=[F(x) for x in trim(a)];b=[F(x) for x in trim(b)]
    assert b[-1]
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b);z=a[-1]/b[-1];q[k]+=z
        for j,x in enumerate(b):a[k+j]-=z*x
        a=trim(a)
    assert not any(a)
    assert all(x.denominator==1 for x in q)
    return trim([int(x) for x in q])

CYCLO={}
def cyclotomic(n):
    if n not in CYCLO:
        p=[-1]+[0]*(n-1)+[1]
        for j in range(1,n):
            if n%j==0:p=divide(p,cyclotomic(j))
        CYCLO[n]=p
    return CYCLO[n]

def product(polys):
    out=[1]
    for p in polys:out=pmul(out,p)
    return [int(x) for x in out]

def specialization(f,a):
    out=[0]*(max(i+a*j for i,j in f)+1)
    for (i,j),c in f.items():out[i+a*j]+=c
    return trim(out)

def main():
    native={n:(((_J_PROGRAM if n in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes() for n in ('verify.py','result.json','readme.md')}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0166.md')
    db=draft.read_bytes() if draft.exists() else None
    data=json.loads(native['result.json'])
    assert set(data)=={'scope', 'coefficient_order', 'formal', 'controls', 'paid_target', 'full_polynomial_count', 'full_integer_pencil_count'}
    assert data['scope']=='Exactly a=3,4,5,6,7,8; no search;120s aggregate cap'
    assert data['coefficient_order']=='ascending'
    pass
    pass
    assert set(data['formal'])=={'H','Hstar','numerator_plus','numerator_minus','factored_plus','factored_minus'}
    names=['t','y'];t,y=(variable(i,2) for i in range(2));one=const(1,2)
    H=plus(times(t,t),scale(plus(t,one),-1))
    Hstar=plus(one,scale(plus(t,times(t,t)),-1))
    assert parse(data['formal']['H'],names)==H and parse(data['formal']['Hstar'],names)==Hstar
    cross=scale(times(plus(times(t,t),scale(one,-1)),y),2)
    common=plus(times(H,times(y,y)),scale(Hstar,-1))
    formal={}
    for sign,label in [(1,'plus'),(-1,'minus')]:
        f=plus(common,scale(cross,sign))
        fact=times(plus(y,scale(one,sign)),plus(times(y,H),scale(Hstar,-sign)))
        assert f==fact==parse(data['formal']['numerator_'+label],names)==parse(data['formal']['factored_'+label],names)
        formal[label]=f
    S6=[1,0,-1,-1,-1,0,1];P4=[1,-1,-1,-1,1]
    assert len(data['controls'])==6;count=0;checked=[]
    basekeys={'a','B0','B','D','minor_rows','full_rank_minor_B','full_rank_minor_D','det_Gram_B','det_Gram_D','original','absolute','cover','endpoints','original_quotient_trace_ascending','absolute_quotient_trace_ascending'}
    for a,row in zip(range(3,9),data['controls']):
        gate();keys=basekeys.copy()
        if a in (3,4):keys.add('original_boundary_factorization')
        if a==5:keys.add('paid_target_factorization')
        assert set(row)==keys and row['a']==a
        B0=[[int(j==i)+int(j==i+1) for j in range(a)] for i in range(a)]
        B0[-1][0]=-1;B=B0+[[1]+[0]*(a-1)]
        D=[[abs(x) for x in r] for r in B]
        assert row['B0']==B0 and row['B']==B and row['D']==D
        indices=list(range(a-1))+[a]
        assert row['minor_rows']==indices
        bm=fraction_det([B[i] for i in indices]);dm=fraction_det([D[i] for i in indices])
        assert bm==dm==(-1)**(a-1)
        assert row['full_rank_minor_B']==bm and row['full_rank_minor_D']==dm
        gb=fraction_det(mm(tr(B),B));gd=fraction_det(mm(tr(D),D))
        assert row['det_Gram_B']==gb>0 and row['det_Gram_D']==gd>0
        V=eye(2*a+1)
        for i in range(a+1):
            for j in range(a):V[i][a+1+j]=-B[i][j]
        A=absolute(V);W=cover(V)
        for i in range(a+1):assert A[i][a+1:]==[-x for x in D[i]]
        p,n0=one_complete(V,row['original']);pa,n1=one_complete(A,row['absolute']);pc,n2=one_complete(W,row['cover']);count+=n0+n1+n2
        assert p==divide(specialization(formal['plus'],a),[-1,1])
        assert pa==divide(specialization(formal['minus'],a),[-1,1])
        assert pc==pmul(p,pa)
        assert cost(V)==cost(A)=={'rank':2*a+1,'height':1,'energy':2*a+1}
        assert cost(W)=={'rank':4*a+2,'height':1,'energy':4*a+2}
        # A separate expansion of the complete cycle-plus-leaf formula.
        base=[1]+[0]*(a-1)+[1];base_abs=[-1]+[0]*(a-1)+[1]
        leaf=[0]+[-1]*(2*a)
        assert trim(padd(pmul([1,1],pmul(base,base)),leaf))==p
        assert trim(padd(pmul([1,1],pmul(base_abs,base_abs)),leaf))==pa
        pq=divide(p,[1,1]);aq=divide(pa,[1,1])
        assert ev(pq,-1)==gb and ev(aq,-1)==gd
        for key,cs in [('original_quotient_trace_ascending',pq),('absolute_quotient_trace_ascending',aq)]:
            trace=row[key];assert len(trace)==a+1 and trace[-1]==1
            assert trace_expand(trace)==cs
        eps={'P1':ev(p,1),'A1':ev(pa,1),'absolute_Qplus2':2**a*ev([-1,-1,1],2)+ev([1,-1,-1],2)}
        assert row['endpoints']==eps
        assert eps=={'P1':8-2*a,'A1':-2*a,'absolute_Qplus2':2**a-5}
        if a==3:
            assert row['original_boundary_factorization']=='Phi2 Phi6 Phi12; zero measure'
            assert p==product([cyclotomic(j) for j in (2,6,12)])
        if a==4:
            assert row['original_boundary_factorization']=='Phi1^2 Phi2 Phi3 Phi8; zero measure'
            assert p==product([cyclotomic(j) for j in (1,1,2,3,8)])
        if a==5:
            assert p==product([cyclotomic(2),cyclotomic(10),S6])
            assert pa==product([cyclotomic(2),cyclotomic(5),cyclotomic(6),P4])
            assert pc==product([cyclotomic(2),cyclotomic(2),cyclotomic(5),cyclotomic(6),cyclotomic(10),S6,P4])
            neutral=[len(p)-len(S6),len(pa)-len(P4),(len(pc)-1)-(len(S6)-1)-(len(P4)-1)]
            assert row['paid_target_factorization']=={'original':'Phi2 Phi10 S6','absolute':'Phi2 Phi5 Phi6 P4','cover':'Phi2^2 Phi5 Phi6 Phi10 S6 P4','neutral_degrees':neutral}
            assert neutral==[5,7,12]
        checked.append({'a':a,'full_polynomials':3,'integer_pencils':n0+n1+n2,'full_rank_minor_B':bm,'full_rank_minor_D':dm,'Gram_B':gb,'Gram_D':gd,'original_cost':cost(V),'absolute_cost':cost(A),'cover_cost':cost(W),'all_mathematical_fields_match':True})
    paid=data['paid_target']
    assert set(paid)=={'S6_coefficients','P4_coefficients','S6_trace','P4_trace','S6_endpoints','S6_values','P4_endpoints','P4_values','S6_trace_points','S6_trace_values','rational_candidates','rational_values'}
    assert paid['S6_coefficients']==S6 and paid['P4_coefficients']==P4
    assert trace_expand(paid['S6_trace'])==S6 and trace_expand(paid['P4_trace'])==P4
    assert paid['S6_trace']==[-1,-4,0,1] and paid['P4_trace']==[-3,-1,1]
    for name,cs,points in [('S6',S6,[F(7,5),F(3,2)]),('P4',P4,[F(5,3),F(7,4)])]:
        vals=[ev(cs,x) for x in points]
        assert paid[name+'_endpoints']==[str(x) for x in points]
        assert paid[name+'_values']==[str(x) for x in vals]
        assert vals[0]<0<vals[1]
    points=[-2,-1,0,2,3];assert paid['S6_trace_points']==points
    assert paid['S6_trace_values']==[ev(paid['S6_trace'],x) for x in points]==[-1,2,-1,-1,14]
    assert paid['rational_candidates']==[1,-1]
    assert paid['rational_values']==[ev(paid['S6_trace'],x) for x in [1,-1]]==[-4,2]
    assert count==306==data['full_integer_pencil_count']
    assert data['full_polynomial_count']==18 and PENCIL_CALLS==306
    gate();assert all((((_J_PROGRAM if n in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes()==b for n,b in native.items())
    if db is not None:assert draft.read_bytes()==db
    return {'scope': 'entire final J75 symbolic and six-control native mathematical payload', 'method': 'standard-library integer Bareiss pencils/Newton full-polynomial interpolation; Fraction minors/Gram determinants; sparse bivariate identities, cyclotomic exact division and binomial Laurent trace expansion', 'reuse': 'reviewer own J69/J72/J74 primitives; no author import or generated-result premise', 'author_imports': False, 'sympy_used': False, 'controls': checked, 'full_polynomials_checked': 18, 'all_saved_integer_pencils_checked': count, 'independent_minor_Gram_determinants': 24, 'all_formal_fields_checked': True, 'all_trace_endpoint_factorization_neutral_degree_cost_fields_checked': True, 'all_exact_checks_passed': True}

if __name__=='__main__':
    try:
        result=main();((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result))
    except BaseException:
        import traceback
        failure={'traceback': _record_text(traceback.format_exc())}
        p=(_J_OUTPUT / 'review_failure.json');i=1
        p.write_text(json.dumps(failure,indent=2)+'\n',encoding='utf-8');raise
