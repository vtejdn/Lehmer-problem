"""Complete noncontributor J72 check; own J69 primitives reused: standard library, integer pencils/interpolation."""
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

def rational_parse(text,names):
    dim=len(names);one=const(1,dim)
    def visit(n):
        if isinstance(n,ast.Constant) and type(n.value)==int:return const(n.value,dim),one
        if isinstance(n,ast.Name) and n.id in names:return variable(names.index(n.id),dim),one
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):
            a,b=visit(n.operand);return scale(a,-1),b
        if isinstance(n,ast.BinOp):
            a,b=visit(n.left)
            if isinstance(n.op,ast.Pow):
                assert isinstance(n.right,ast.Constant) and type(n.right.value)==int and 0<=n.right.value<=20
                return power(a,n.right.value,dim),power(b,n.right.value,dim)
            c,d=visit(n.right)
            if isinstance(n.op,ast.Add):return plus(times(a,d),times(b,c)),times(b,d)
            if isinstance(n.op,ast.Sub):return plus(times(a,d),scale(times(b,c),-1)),times(b,d)
            if isinstance(n.op,ast.Mult):return times(a,c),times(b,d)
            if isinstance(n.op,ast.Div):
                assert c;return times(a,d),times(b,c)
        raise ValueError('outside rational polynomial AST')
    return visit(ast.parse(text,mode='eval').body)

def aspoly(cs):return {(i,):c for i,c in enumerate(cs) if c}
def ev(cs,x):return sum(c*x**i for i,c in enumerate(cs))
def paired(U,C):
    n=len(U);k=len(C[0]);V=eye(n+2*k)
    for i in range(n):V[i][:n]=U[i][:];V[i][n:n+k]=C[i][:];V[i][n+k:]=C[i][:]
    for j in range(k):V[n+j][n+k+j]=2
    return V
def laurent_trace(poly,degree):
    # Expand t^degree*q(t+t^-1) directly, without the author's Chebyshev recurrence.
    out={}
    for (j,),a in poly.items():
        for k in range(j+1):
            e=degree+j-2*k;out[e]=out.get(e,0)+a*math.comb(j,k)
    out={e:a for e,a in out.items() if a};assert min(out)>=0
    return [out.get(i,0) for i in range(max(out)+1)]
def rem3(a,b):
    a=[x%3 for x in a];b=[x%3 for x in b]
    while a and not a[-1]:a.pop()
    while len(a)>=len(b):
        q=a[-1]*pow(b[-1],-1,3)%3;shift=len(a)-len(b)
        for j,x in enumerate(b):a[j+shift]=(a[j+shift]-q*x)%3
        while a and not a[-1]:a.pop()
    return a+[0]*(len(b)-1-len(a))

def main():
    native={n:(((_J_PROGRAM if n in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes() for n in ('verify.py','result.json','readme.md')}
    # Optional operational observation only; fixed retention may retire this draft.
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0158.md')
    draft_before=draft.read_bytes() if draft.exists() else None
    data=json.loads(native['result.json']);z=data['symbolic']
    assert data['scope']=='D158 exact five controls; no discovery search'
    assert data['all_exact_checks_passed'] is True
    assert set(z)=={'rank_one_identity','contractions','full_H_L_coefficients','trace_endpoint_values','mod3_values','phi6_trace_values','independent_trace_coefficients','independent_trace_endpoints','independent_trace_values','independent_mod3_linear_values','independent_mod3_quadratic_remainders'}
    # Full formal rank-one identity, not a numerical sample.
    names=['t','a','b','k','R'];dim=5
    M=[[parse('(t+1)-t*R*a*a',names),parse('t*k-t*R*a*b',names)],
       [parse('k-t*R*a*b',names),parse('(t+1)-t*R*b*b',names)]]
    assert poly_det(M,dim)==parse('(t+1)**2-t*k*k-t*R*(t+1)*(a*a+b*b-k*a*b)',names)
    assert z['rank_one_identity'] is True
    # Explicit numerator inverse and its polynomial product, in either orientation.
    t=variable(0,1);one=const(1,1);s=plus(t,one);q=parse('(t-1)**2',['t'])
    ci=0
    for k in (1,2):
        for sign in (1,-1):
            T=[[{} for _ in range(2*k)] for _ in range(2*k)]
            N=[[{} for _ in range(2*k)] for _ in range(2*k)]
            for i in range(k):
                T[i][i]=T[k+i][k+i]=N[i][i]=N[k+i][k+i]=s
                T[i][k+i]=scale(t,2*sign);T[k+i][i]=scale(one,2*sign)
                N[i][k+i]=scale(t,-2*sign);N[k+i][i]=scale(one,-2*sign)
            assert poly_det(T,1)==power(q,k,1)
            for i in range(2*k):
                for j in range(2*k):
                    val={}
                    for h in range(2*k):val=plus(val,times(T[i][h],N[h][j]))
                    assert val==(q if i==j else {})
            row=z['contractions'][ci];ci+=1;assert row['k']==k and row['sign']==sign
            assert len(row['contraction'])==k and all(len(r)==k for r in row['contraction'])
            for i in range(k):
                for j in range(k):
                    val=plus(plus(N[i][j],N[i][k+j]),plus(N[k+i][j],N[k+i][k+j]))
                    assert val==(scale(s,4) if i==j and sign==-1 else {})
                    a,b=rational_parse(row['contraction'][i][j],['t'])
                    assert times(a,q)==times(val,b)
    assert ci==len(z['contractions'])==4
    U=eye(6);B=[[1,1],[0,1],[0,1],[0,1]]
    for i in range(4):
        for j in range(2):U[i][4+j]=-B[i][j]
    pu,_=coefficients(U);P=[1,-1,-1,-1,1]
    assert pu==[int(x) for x in pmul([1,2,1],P)]
    # Border determinants reconstruct each actual cofactor polynomial independently.
    cofactors=[]
    for c,rhs in [([0,1,0,0,0,0],'(t+1)**2*(t**4+1)'),
                  ([0,1,1,0,0,0],'2*(t+1)**2*((t+1)**4-3*t*(t+1)**2+t*t)')]:
        vals=[]
        for h in range(6):
            A=pencil(U,h);border=[row+[c[i]] for i,row in enumerate(A)]+[c+[0]]
            vals.append(-det(border))
        cf=interp(vals);assert aspoly(pmul(cf,[1,1]))==parse(rhs,['t']);cofactors.append(cf)
    # All-L polynomial, exact endpoint expressions, and fourth/fifth trace data.
    assert len(z['full_H_L_coefficients'])==7
    f=parse('v**3-(4*L+3)*v*v-v+8*L+6',['v','L'])
    def substitute_v(expr):
        out={};L=variable(0,1)
        for (i,j),a in f.items():out=plus(out,scale(times(power(expr,i,1),power(L,j,1)),a))
        return out
    actual_h={}
    for (i,j),a in f.items():
        for k in range(i+1):
            e=3+i-2*k;actual_h[(e,j)]=actual_h.get((e,j),0)+a*math.comb(i,k)
    for i,txt in enumerate(z['full_H_L_coefficients']):
        assert parse(txt,['L'])=={(j,):a for (e,j),a in actual_h.items() if e==i and a}
    hpoly={e:a for e,a in actual_h.items() if a}
    assert hpoly==parse('(1-t-t*t-t**3+t**4)*(t-1)**2-4*t*L*(t**4+1)',['t','L'])
    ends=['-2','-1','1','2','4*L+2','4*L+3'];assert len(z['trace_endpoint_values'])==6
    for ep,out in zip(ends,z['trace_endpoint_values']):assert substitute_v(parse(ep,['L']))==parse(out,['L'])
    assert z['mod3_values']==[ev([2,-1,-1,1],i)%3 for i in range(3)]==[2,1,1]
    fj=[3,-10,-6,1];J=laurent_trace(aspoly(fj),3)
    assert z['phi6_trace_values']==[ev(fj,i) for i in [-2,-1,0,1,7,8]]==[-9,6,3,-12,-18,51]
    assert aspoly(J)==parse('(1-t-t*t-t**3+t**4)*(t*t+t+1)-6*t*((t+1)**4-3*t*(t+1)**2+t*t)',['t'])
    g=[-44,64,33,-13,1];H8=laurent_trace(aspoly(g),4)
    assert z['independent_trace_coefficients']==g
    pts=[-2,-1,0,1,6,7,8];assert z['independent_trace_endpoints']==pts
    assert z['independent_trace_values']==[ev(g,i) for i in pts]==[80,-61,-44,41,16,-37,20]
    assert z['independent_mod3_linear_values']==[ev(g,i)%3 for i in range(3)]==[1,2,2]
    quadratics=[list(b)+[1] for b in itertools.product(range(3),repeat=2) if all(ev(list(b)+[1],x)%3 for x in range(3))]
    # Above tuples are converted explicitly; ordering is deterministic below.
    quadratics=sorted(quadratics);assert quadratics==[[1,0,1],[2,1,1],[2,2,1]]
    assert z['independent_mod3_quadratic_remainders']==[rem3(g,q) for q in quadratics]==[[2,2],[1,2],[2,2]]
    e1=[1,0,0,0,0,0];e2=[0,1,0,0,0,0]
    fixed=[('pair_m1',[[x] for x in e2],1),('pair_m2',[[2*x] for x in e2],4),
           ('two_repeated',[[x,x] for x in e2],2),('two_independent',[[x,y] for x,y in zip(e1,e2)],None)]
    controls=[(label,paired(U,C),C,L) for label,C,L in fixed]
    V=eye(8);c=[0,1,-1,0,0,0]
    for i in range(6):V[i][:6]=U[i][:];V[i][6]=V[i][7]=c[i]
    V[6][7]=1;controls.append(('nonbipartite_phi6',V,None,None))
    assert len(data['controls'])==5
    pencil_count=schur_count=0;checked=[]
    for (label,V,C,L),row in zip(controls,data['controls']):
        assert set(row)=={'label','C','original_matrix','absolute_matrix','proper_cover_matrix','original_polynomial','absolute_polynomial','cover_polynomial','original_cost','absolute_cost','cover_cost','absolute_trace_polynomial','absolute_factorization','pencil_values','schur_values'}
        assert row['label']==label and row['C']==C and row['original_matrix']==V
        A,W=absolute(V),cover(V);assert row['absolute_matrix']==A and row['proper_cover_matrix']==W
        op,ov=coefficients(V);ap,av=coefficients(A);wp,wv=coefficients(W)
        assert row['original_polynomial']==op and row['absolute_polynomial']==ap and row['cover_polynomial']==wp
        assert wp==pmul(op,ap)
        for key,mat in [('original',V),('absolute',A),('cover',W)]:assert row[key+'_cost']==cost(mat)
        assert row['pencil_values']=={'original':ov,'absolute':av,'proper_cover':wv}
        pencil_count+=len(ov)+len(av)+len(wv)
        assert parse(row['absolute_factorization'],['t'])==aspoly(ap)
        assert laurent_trace(parse(row['absolute_trace_polynomial'],['v']),len(V)//2)==ap
        sv=[]
        if C is not None:
            k=len(C[0]);D=[[abs(x) for x in r] for r in C];DD=mm(D,tr(D))
            assert aspoly(op)==times(aspoly(pu),parse('(t-1)**'+str(2*k),['t']))
            for h in range(2,len(V)+3):
                M=pencil(U,h)
                X=[[(h-1)**2*M[i][j]-4*h*(h+1)*DD[i][j] for j in range(6)] for i in range(6)]
                num=det(X);den=(h-1)**(12-2*k);assert num%den==0
                val=num//den;assert val==ev(ap,h);sv.append(val)
            if L is None:assert ap==pmul([1,2,1],H8)
            else:
                HL=laurent_trace(aspoly([8*L+6,-1,-4*L-3,1]),3)
                expect=times(times(parse('(t+1)**2',['t']),parse('(t-1)**'+str(2*k-2),['t'])),aspoly(HL))
                assert aspoly(ap)==expect
            assert cost(V)['energy']==5+2*sum(x*x for r in C for x in r)+4*k
        else:
            assert op==pmul(pu,[1,-1,1]) and ap==pmul([1,2,1],J)
            assert cost(V)=={'rank':8,'height':1,'energy':10}
        assert row['schur_values']==sv;schur_count+=len(sv)
        checked.append({'label':label,'costs':{key:cost(mat) for key,mat in [('original',V),('absolute',A),('cover',W)]},'all_payload_fields_matched':True})
    assert pencil_count==191 and schur_count==40
    gate();assert all((((_J_PROGRAM if n in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes()==b for n,b in native.items())
    if draft_before is not None:assert draft.read_bytes()==draft_before
    return {'scope': 'entire final J72 symbolic and five-control mathematical payload', 'method': 'standard-library Bareiss/Newton; sparse formal polynomials; bordered cofactors; integer-cleared Schur; Laurent and F3 division', 'author_imports': False, 'sympy_used': False, 'controls': checked, 'saved_full_pencil_values_checked': pencil_count, 'schur_values_checked': schur_count, 'actual_pencil_determinants': PENCIL_CALLS, 'cofactor_border_determinants': 12, 'full_polynomials_checked': 15, 'formal_rank_one_identity': True, 'paired_inverse_cases': 4, 'all_symbolic_fields_checked': True, 'all_exact_checks_passed': True}

if __name__=='__main__':
    try:
        result=main();((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result))
    except Exception:
        import traceback
        failure={'traceback': _record_text(traceback.format_exc())}
        p=(_J_OUTPUT / 'review_failure.json');i=1
        p.write_text(json.dumps(failure,indent=2)+'\n',encoding='utf-8');raise
