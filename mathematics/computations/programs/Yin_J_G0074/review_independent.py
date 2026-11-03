"""Complete noncontributor J74 check; own J69/J72 primitives reused: standard library, integer pencils/interpolation."""
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

def main():
    native={n:(((_J_PROGRAM if n in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes() for n in ('verify.py','result.json','readme.md')}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0162.md')
    db=draft.read_bytes() if draft.exists() else None
    data=json.loads(native['result.json'])
    assert set(data)=={'scope', 'coefficient_order', 'formal', 'first_index', 'controls', 'full_polynomial_count', 'full_integer_pencil_count'}
    assert data['scope']=='Exactly a=3,4,5,6,7,8; no search;120s aggregate cap'
    assert data['coefficient_order']=='ascending'
    pass
    assert set(data['formal'])=={'numerator_plus','numerator_minus','next_difference_plus','next_difference_minus'}
    names=['t','y'];t,y=(variable(i,2) for i in range(2))
    one=const(1,2);common=plus(times(plus(t,scale(one,-4)),times(y,y)),plus(scale(t,4),scale(one,-1)))
    cross=scale(times(plus(t,scale(one,-1)),y),4)
    for sign,label in [(1,'plus'),(-1,'minus')]:
        f=plus(common,scale(cross,sign))
        assert parse(data['formal']['numerator_'+label],names)==f
        substituted={(i+j,j):c for (i,j),c in f.items()}
        diff=plus(substituted,scale(times(times(t,t),f),-1))
        expected=parse(('-' if sign==1 else '')+'4*t*(t-1)**2*y-(4*t-1)*(t*t-1)',names)
        assert diff==expected==parse(data['formal']['next_difference_'+label],names)
    assert len(data['controls'])==6;count=0;checked=[]
    for a,row in zip(range(3,9),data['controls']):
        assert set(row)=={'a','B','D','det_B','det_D','original','absolute','cover','endpoints','original_trace_ascending','absolute_trace_ascending'}
        assert row['a']==a
        B=eye(a)
        for i in range(a-1):B[i][i+1]=1
        B[-1][0]=-2;D=[[abs(x) for x in r] for r in B]
        assert row['B']==B and row['D']==D
        assert fraction_det(B)==row['det_B']==1+2*(-1)**a
        assert fraction_det(D)==row['det_D']==1-2*(-1)**a
        V=eye(2*a)
        for i in range(a):
            for j in range(a):V[i][a+j]=-B[i][j]
        A,W=absolute(V),cover(V)
        for i in range(a):assert A[i][a:]==[-x for x in D[i]]
        p,n0=one_complete(V,row['original']);pa,n1=one_complete(A,row['absolute']);pc,n2=one_complete(W,row['cover']);count+=n0+n1+n2
        expected=[1]+[-3]*(2*a-1)+[1];expected[a]+=4
        expected_abs=expected[:];expected_abs[a]-=8
        assert p==expected and pa==expected_abs and pc==pmul(p,pa)
        assert cost(V)==cost(A)=={'rank':2*a,'height':2,'energy':2*a+3}
        assert cost(W)=={'rank':4*a,'height':2,'energy':4*a+6}
        for label,cs in [('plus',p),('minus',pa)]:
            # Specialize the independently reconstructed formal numerator y=t^a.
            f=parse(data['formal']['numerator_'+label],names);sub={}
            for (i,j),c in f.items():sub[(i+a*j,)]=sub.get((i+a*j,),0)+c
            sub={e:c for e,c in sub.items() if c}
            assert sub==aspoly(pmul([-1,1],cs))
        eps={'P1':ev(p,1),'A1':ev(pa,1),'twice_P3':2*ev(p,3),'triple_P4':3*ev(p,4),'triple_A4':3*ev(pa,4),'quadruple_A5':4*ev(pa,5)}
        assert row['endpoints']==eps
        assert eps['P1']==9-6*a and eps['A1']==1-6*a
        assert eps['twice_P3']==-3**(2*a)+8*3**a+11<0
        assert eps['triple_P4']==12*4**a+15>0
        assert eps['triple_A4']==-12*4**a+15<0
        assert eps['quadruple_A5']==5**(2*a)-16*5**a+19>0
        for key,cs in [('original_trace_ascending',p),('absolute_trace_ascending',pa)]:
            trace=row[key];assert len(trace)==a+1 and trace[-1]==1
            assert trace_expand(trace)==cs
        if a==3:
            assert row['original_trace_ascending']==[7,-6,-3,1]
            assert row['absolute_trace_ascending']==[-1,-6,-3,1]
        checked.append({'a':a,'full_polynomials':3,'integer_pencils':n0+n1+n2,'original_cost':cost(V),'absolute_cost':cost(A),'cover_cost':cost(W),'all_mathematical_fields_match':True})
    first=data['first_index'];assert set(first)=={'f_rational_candidates','f_values','g_rational_candidates','g_values'}
    for prefix,cs in [('f',[7,-6,-3,1]),('g',[-1,-6,-3,1])]:
        candidates=[e for i in range(1,abs(cs[0])+1) if cs[0]%i==0 for e in (i,-i)]
        assert first[prefix+'_rational_candidates']==candidates
        vals=[ev(cs,x) for x in candidates]
        assert first[prefix+'_values']==vals and all(vals)
    assert count==282==data['full_integer_pencil_count']
    assert data['full_polynomial_count']==18 and PENCIL_CALLS==282
    gate();assert all((((_J_PROGRAM if n in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes()==b for n,b in native.items())
    if db is not None:assert draft.read_bytes()==db
    return {'scope': 'entire final J74 symbolic and six-control native mathematical payload', 'method': 'standard-library Bareiss pencils and Newton full-polynomial interpolation; Fraction block determinants; sparse bivariate identities and direct Laurent traces', 'reuse': 'reviewer own J69/J72 primitives; no author import or generated-result premise', 'author_imports': False, 'sympy_used': False, 'controls': checked, 'full_polynomials_checked': 18, 'all_saved_integer_pencils_checked': count, 'independent_B_D_determinants': 12, 'all_formal_fields_checked': True, 'all_trace_endpoint_first_index_cost_fields_checked': True, 'all_exact_checks_passed': True}

if __name__=='__main__':
    try:
        result=main();((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result))
    except BaseException:
        import traceback
        failure={'traceback': _record_text(traceback.format_exc())}
        p=(_J_OUTPUT / 'review_failure.json');i=1
        p.write_text(json.dumps(failure,indent=2)+'\n',encoding='utf-8');raise

