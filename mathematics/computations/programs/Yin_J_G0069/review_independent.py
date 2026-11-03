"""Complete noncontributor J69 check: standard library, integer pencils/interpolation."""
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
    return {'rank':len(V),'height':max(map(abs,entries),default=0),'energy':sum(a*a for a in entries)}
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
def complete(V,row):
    assert row['matrix']==V
    A,W=absolute(V),cover(V)
    assert row['absolute_matrix']==A and row['proper_cover_matrix']==W
    op,ov=coefficients(V);ap,av=coefficients(A);wp,wv=coefficients(W)
    assert row['original_polynomial']==op and row['absolute_polynomial']==ap and row['cover_polynomial']==wp
    assert wp==[int(v) for v in pmul(op,ap)]
    for key,M in [('original',V),('absolute',A),('cover',W)]:assert row[key+'_cost']==cost(M)
    assert row['pencil_values']=={'original':ov,'absolute':av,'cover':wv}
    return sum(map(len,(ov,av,wv)))

def main():
    saved={name:(((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in ('verify.py','result.json','readme.md')}
    data=json.loads(saved['result.json']);U=eye(6)
    B=[[1,1],[0,1],[0,1],[0,1]]
    for i in range(4):
        for j in range(2):U[i][j+4]=-B[i][j]
    up,_=coefficients(U)
    assert up==[1,1,-2,-4,-2,1,1]
    pairs=[(i,i) for i in range(6)]+[(i,j) for i in range(6) for j in range(i+1,6)]
    qp={}
    diagonal={}
    for i,j in pairs:
        c=[0]*6;c[i]=1
        if j!=i:c[j]=1
        vals=[]
        for t in range(1,7):
            n=(t+1)*det(pencil(U,t))-det(pencil(append(U,c),t))
            assert n%t==0;vals.append(n//t)
        co=interp(vals,1)
        if i==j:diagonal[i]=co
        else:co=[z-a-b for z,a,b in zip(co,diagonal[i],diagonal[j])]
        qp[i,j]=co
    # The iteration above requires all diagonals before off-diagonal polarization.
    for k,text in enumerate(data['symbolic']['adjugate_coefficients_in_t']):
        expected={}
        for (i,j),co in qp.items():
            u=[0]*6;u[i]+=1;u[j]+=1
            if co[k]:expected[tuple(u)]=co[k]
        assert parse(text,['x0','x1','x2','x3','y0','y1'])==expected
    assert len(data['symbolic']['adjugate_coefficients_in_t'])==6
    a,b,t=(variable(i,3) for i in range(3))
    xs=[{},a,b,scale(plus(a,b),-1),{},{}]
    adj={}
    for (i,j),co in qp.items():
        for k,z in enumerate(co):adj=plus(adj,scale(times(times(xs[i],xs[j]),power(t,k,3)),z))
    core={}
    for k,z in enumerate(up):core=plus(core,scale(power(t,k,3),z))
    family=plus(times(plus(t,const(1,3)),core),scale(times(t,adj),-1))
    assert family==parse(data['symbolic']['full_family_original'],['a','b','t'])
    norm={}
    for v in xs:norm=plus(norm,times(v,v))
    assert norm==parse(data['symbolic']['kernel_norm'],['a','b','t'])
    a,b,L,z=(variable(i,4) for i in range(4));one=const(1,4)
    N=plus(plus(times(a,a),times(b,b)),times(plus(a,b),plus(a,b)))
    G=[[plus(z,scale(one,-1)),scale(one,-1),{}],
       [scale(one,-1),plus(z,scale(one,-4)),scale(L,-1)],
       [{},scale(L,-1),plus(z,scale(N,-1))]]
    assert poly_det(G,4)==parse(data['symbolic']['absolute_gram_characteristic'],['a','b','L','z'])
    assert data['symbolic']['all_symbolic_equalities'] is True
    declared=[(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(0,0)]
    assert len(data['controls'])==8 and len(data['cyclic_controls'])==36
    pencil_count=0;ci=0;rotations=0;energy_counts={};companions={}
    for idx,(a,b) in enumerate(declared):
        c=[0,a,b,-a-b,0,0];V=append(U,c);row=data['controls'][idx]
        assert row['label']==f'kernel_{a}_{b}'
        assert row['parameters']=={'a':a,'b':b,'N':sum(v*v for v in c),'L':sum(map(abs,c))}
        pencil_count+=complete(V,row)
        if a==b==0:continue
        core=[r[:] for r in U];coupling=c[:]
        for phase in range(6):
            row=data['cyclic_controls'][ci];ci+=1
            assert (row['a'],row['b'],row['core_phase'])==(a,b,phase)
            W=append(core,coupling);op,_=coefficients(W);ap,_=coefficients(absolute(W));cp,_=coefficients(cover(W))
            assert row['original_polynomial']==op and row['absolute_polynomial']==ap and row['proper_cover_polynomial']==cp
            assert cp==[int(v) for v in pmul(op,ap)] and row['cost']==cost(W)
            e=cost(W)['energy'];energy_counts[e]=energy_counts.get(e,0)+1
            companions.setdefault(tuple(ap),0);companions[tuple(ap)]+=1
            positions=[]
            for rotation in range(7):
                assert coefficients(W)[0]==op and coefficients(absolute(W))[0]==ap
                assert coefficients(cover(W))[0]==cp and cost(W)==row['cost']
                positions.append(6-rotation);W,Q=rotate(W);rotations+=1
            assert row['insertion_positions']==positions and sorted(positions)==list(range(7))
            core,Q=rotate(core);coupling=[v[0] for v in mm(tr(Q),[[v] for v in coupling])]
    boundary=[[1,0,-2,-1],[0,1,0,0],[0,0,1,1],[0,0,0,1]]
    assert data['controls'][-1]['label']=='closed_endpoint_lambda4'
    pencil_count+=complete(boundary,data['controls'][-1])
    assert data['cyclic_cases']==rotations==252 and data['pencil_evaluations']==pencil_count==236
    assert energy_counts=={7:28,8:8} and len(companions)==2
    assert data['cubic_endpoint_values']==[x**3-x*x-7*x-4 for x in (-2,-1,0,3,4)]==[-2,1,-4,-7,16]
    extra=[x**3-5*x*x-15*x-8 for x in (-2,-1,0,7,8)]
    assert extra==[-6,1,-8,-15,64]
    assert data['scope']=={'discovery_search': False, 'finite_controls': 8, 'core_phases': 6, 'insertion_positions': 7, 'norm2_pairs': 6}
    assert data['passed'] is True
    for name,old in saved.items():assert (((_J_PROGRAM if name in ('readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()==old
    return {'passed': True, 'method': 'integer Bareiss pencils plus full Newton interpolation and quadratic polarization; no author imports or SymPy', 'symbolic_quadratic_monomials': 21, 'symbolic_t_coefficients': 6, 'full_main_matrix_controls': 8, 'native_pencil_values': pencil_count, 'cyclic_groups': ci, 'insertion_cases': rotations, 'energy_group_counts': energy_counts, 'complete_companion_groups': [{'polynomial': list(k), 'count': v} for k, v in companions.items()], 'extra_cubic_endpoint_values': extra, 'unique_literal_matrices_interpolated': len(CACHE), 'literal_matrix_pencil_evaluations': PENCIL_CALLS, 'symbolic_basis_pair_evaluations': 126}

if __name__=='__main__':
    try:
        result=main();gate()
        ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
        print(json.dumps(result,indent=2))
    except Exception as exc:
        (_J_OUTPUT / 'review_failure.json').write_text(json.dumps({'error': _record_text(repr(exc))}, indent=2) + '\n', encoding='utf-8')
        raise
