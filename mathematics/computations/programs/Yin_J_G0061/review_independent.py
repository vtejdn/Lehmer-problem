"""Independent complete J61 verification; no author imports or native writes.

Declared scope: the two retained starting fields, three 3-adic steps, the
single mod4 compatibility obstruction, five cost representatives, all65
literal cover evaluations; independent reverse-variable 3-adic steps too.
Cap:120 seconds. Draft presence is optional and only observed for no-write.
Polynomial determinants use subset/permutation dynamic expansion, while
point determinants use fraction-free elimination. Jacobians use symmetric
integer finite differences, not the author's infinitesimal formula.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
import ast
import json
import time

HERE = (_J_PROGRAM / 'review_independent.py').parent
V = [[0,-1,-2,0,-1,0], [1,0,-1,1,0,1], [2,1,0,2,1,1],
     [0,-1,-1,0,-1,0], [1,-1,-1,1,0,1], [1,-1,-1,0,-1,0]]
Q2 = [[0,0,0,0,1,1], [1,1,1,1,1,1], [0,1,1,1,1,1],
      [0,0,0,1,1,0], [1,1,1,0,0,0], [1,1,0,0,0,1]]
Q3 = [[1,2,0,1,2,0], [0,0,0,1,2,2], [0,1,1,0,0,0],
      [0,0,1,2,2,1], [0,2,2,1,2,1], [1,2,2,2,1,0]]
F = [1,-2,1,-1,1,-2,1]
LOWER = [(i,j) for i in range(6) for j in range(i)]
POSITIONS = LOWER + [(i,i) for i in range(5)]
NATIVE = ['readme.md', 'lift.py', 'lift_result.json', 'two_adic.py',
          'two_adic_result.json', 'costs.py', 'cost_result.json']
START = time.perf_counter()
CAP = 120

def checktime():
    assert time.perf_counter()-START < CAP, 'reviewer runtime cap reached'

def transpose(a):
    return list(map(list, zip(*a)))

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def gram(q):
    return mm(transpose(q),mm(V,q))

def modmat(a,m):
    return [[x%m for x in row] for row in a]

def eye(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def det(a):
    a=[row[:] for row in a]
    n=len(a); sign=1; last=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:
            return 0
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k]; sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=v*a[i][j]-a[i][k]*a[k][j]
                assert x%last==0
                a[i][j]=x//last
            a[i][k]=0
        last=v
    return sign*a[-1][-1]

def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def ptr(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def poly_det(a):
    """Det(t*a+a.T), expanded by chosen-column subsets, no interpolation."""
    n=len(a)
    dp={0:[1]}
    for i in range(n):
        nd={}
        for mask,coeff in dp.items():
            for j in range(n):
                if mask>>j&1: continue
                c,s=a[j][i],a[i][j]
                if not(c or s): continue
                nxt=mask|(1<<j)
                sign=-1 if (mask>>(j+1)).bit_count()%2 else 1
                arr=nd.setdefault(nxt,[0]*(i+2))
                for z,x in enumerate(coeff):
                    arr[z]+=sign*c*x
                    arr[z+1]+=sign*s*x
        dp=nd
        checktime()
    return dp.get((1<<n)-1,[0]*(n+1))

def peval(p,x):
    out=0
    for c in reversed(p):out=out*x+c
    return out

def factor_expression(s):
    """Expand the saved display factor string as a polynomial, no CAS."""
    def go(node):
        if isinstance(node,ast.Constant):
            assert type(node.value) is int
            return [node.value]
        if isinstance(node,ast.Name):
            assert node.id=='t'; return [0,1]
        if isinstance(node,ast.UnaryOp):
            p=go(node.operand)
            assert isinstance(node.op,(ast.USub,ast.UAdd))
            return [-v for v in p] if isinstance(node.op,ast.USub) else p
        assert isinstance(node,ast.BinOp)
        if isinstance(node.op,ast.Pow):
            assert isinstance(node.right,ast.Constant) and type(node.right.value) is int
            n=node.right.value; assert 0<=n<=12
            p=[1]
            for _ in range(n):p=pmul(p,go(node.left))
            return p
        p,q=go(node.left),go(node.right)
        if isinstance(node.op,ast.Mult):return pmul(p,q)
        assert isinstance(node.op,(ast.Add,ast.Sub))
        sign=1 if isinstance(node.op,ast.Add) else -1
        return [(p[i] if i<len(p) else 0)+sign*(q[i] if i<len(q) else 0)
                for i in range(max(len(p),len(q)))]
    return ptr(go(ast.parse(s,mode='eval').body))

def equations(q):
    b=gram(q)
    return [det(q)-1]+[b[i][j]-int(i==j) for i,j in POSITIONS]

def finite_difference_jacobian(q,p):
    columns=[]
    for i,j in product(range(6),repeat=2):
        qp=[row[:] for row in q]; qm=[row[:] for row in q]
        for r in range(6):
            qp[r][j]+=q[r][i]; qm[r][j]-=q[r][i]
        a,b=equations(qp),equations(qm)
        assert all((v-w)%2==0 for v,w in zip(a,b))
        columns.append([((v-w)//2)%p for v,w in zip(a,b)])
    return transpose(columns)

def eliminate(a,p,order=None,rhs=None):
    """Independent elimination, optionally using reverse variable priority."""
    n=len(a[0]); z=[[x%p for x in row] for row in a]
    if rhs is not None:
        for row,x in zip(z,rhs):row.append(x%p)
    order=list(range(n)) if order is None else order
    piv=[]; row=0
    for col in order:
        k=next((k for k in range(row,len(z)) if z[k][col]),None)
        if k is None:continue
        z[row],z[k]=z[k],z[row]
        inv=pow(z[row][col],-1,p)
        z[row]=[x*inv%p for x in z[row]]
        for k in range(len(z)):
            if k!=row and z[k][col]:
                scale=z[k][col]
                z[k]=[(x-scale*y)%p for x,y in zip(z[k],z[row])]
        piv.append(col); row+=1
        if row==len(z):break
    if rhs is None:return z,piv
    assert all(any(r[:n]) or r[-1]==0 for r in z)
    sol=[0]*n
    for r,c in enumerate(piv):sol[c]=z[r][-1]
    assert all(sum(x*y for x,y in zip(r,sol))%p==v%p for r,v in zip(a,rhs))
    return sol,piv

def verify_basis(q,m,saved=None):
    b=modmat(gram(q),m); d=det(q)
    assert d%m==1
    assert all(b[i][j]==0 for i,j in LOWER)
    assert all(b[i][i]==1 for i in range(6))
    coeff=[v%m for v in poly_det(b)]
    assert coeff==[v%m for v in F]
    result=dict(basis=q,determinant_modulus=d%m,transformed_matrix=b,
                full_original_polynomial_modulus=coeff,integer_representative_determinant=d)
    if saved is not None:
        for key,value in result.items(): assert saved[key]==value,(m,key)
    return result

def correct(q,x,m,p):
    op=[[int(i==j)+m*x[i][j] for j in range(6)] for i in range(6)]
    return modmat(mm(q,op),m*p)

def literal_lift(b):
    w=[[0]*12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            x=b[i][j]
            block=[[x,0],[0,x]] if x<=0 else [[0,-x],[-x,0]]
            for r in range(2):
                for s in range(2):w[2*i+r][2*j+s]=block[r][s]
    return w

def proper(a):
    return all(a[i][i]==1 for i in range(len(a))) and all(a[i][j]==0 for i in range(len(a)) for j in range(i))

def main():
    before={name:(((_J_PROGRAM if name in ('costs.py', 'lift.py', 'readme.md', 'review_independent.py', 'two_adic.py') else _J_OUTPUT) / name)).read_bytes() for name in NATIVE}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0137.md')
    author_before=draft.read_bytes() if draft.exists() else None
    lift=json.loads(before['lift_result.json']); two=json.loads(before['two_adic_result.json'])
    costs=json.loads(before['cost_result.json'])
    old=json.loads(((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0060/congruence_result.json')).read_bytes())
    assert lift['initial_matrix']==V and lift['full_original_polynomial']==F
    assert det(V)==1 and poly_det(V)==F
    assert pmul([1,-1,1],[1,-1,-1,-1,1])==F
    assert lift['scope']['equation_order']==['determinant']+[list(v) for v in POSITIONS]
    assert lift['scope']['variables']==36 and lift['scope']['equations']==21
    assert lift['scope']['primes']==[2,3] and lift['scope']['maximum_exponent']==4
    witnesses={r['prime']:r['basis'] for r in old['field_tests']}
    tests={r['prime']:r for r in lift['tests']}
    assert set(tests)=={2,3}
    bases=[]; jac={}; ranks={}; step_count=0
    for p,q in ((2,Q2),(3,Q3)):
        row=tests[p]; raw=witnesses[p]
        rawdet=det(raw)%p
        assert row['original_basis_determinant_modp']==rawdet
        expected=modmat([[(-x if p==3 and j==5 else x) for j,x in enumerate(r)] for r in raw],p)
        assert expected==q and row['last_column_sign_changed']==(p==3)
        verify_basis(q,p,row['initial']); bases.append((p,q))
        j=finite_difference_jacobian(q,p); jac[p]=j
        assert j==row['jacobian']
        _,piv=eliminate(j,p); ranks[p]=len(piv)
        assert row['rank']==len(piv) and row['pivot_columns']==piv
        if p==2:
            assert len(piv)==20 and row['steps']==[] and row['stop_reason']=='derivative_not_surjective'
            continue
        minor=det([[r[c] for c in piv] for r in j])
        assert len(piv)==21 and minor==16==row['maximal_minor_integer_determinant']
        assert [s['modulus'] for s in row['steps']]==[9,27,81]
        assert row['stop_reason']=='declared_p4_completed'
        m=p
        for exponent,step in enumerate(row['steps'],2):
            err=equations(q); assert all(x%m==0 for x in err)
            eq=[(x//m)%p for x in err]
            assert step['error_quotient_modp']==eq and step['exponent']==exponent
            x=step['correction_matrix']; flat=sum(x,[])
            assert all(sum(v*w for v,w in zip(r,flat))%p==(-e)%p for r,e in zip(j,eq))
            nq=correct(q,x,m,p); assert modmat(nq,m)==q
            m*=p; verify_basis(nq,m,step); q=nq
            bases.append((m,q)); step_count+=1
    assert ranks=={2:20,3:21}
    # Reconstruct a DIFFERENT coherent branch with reversed free-variable priority.
    independent=[]; q=Q3; m=3
    for _ in range(3):
        err=equations(q); assert all(x%m==0 for x in err)
        rhs=[-(x//m)%3 for x in err]
        flat,_=eliminate(jac[3],3,order=list(range(35,-1,-1)),rhs=rhs)
        x=[flat[i:i+6] for i in range(0,36,6)]
        nq=correct(q,x,m,3); assert modmat(nq,m)==q
        m*=3; state=verify_basis(nq,m); state['modulus']=m
        independent.append(state); q=nq
    # Verify every aspect of the same-class modulo4 contradiction.
    assert two['initial_basis']==Q2
    err=equations(Q2); rhs=[-(x//2)%2 for x in err]
    assert all(x%2==0 for x in err)
    assert err==two['equation_errors'] and rhs==two['right_hand_side_mod2']
    left=[0]*21
    for pos in [(4,1),(1,1),(4,4)]:left[1+POSITIONS.index(pos)]=1
    assert left==two['left_kernel_vector']
    assert all(sum(left[i]*jac[2][i][j] for i in range(21))%2==0 for j in range(36))
    assert sum(x*y for x,y in zip(left,rhs))%2==1==two['left_kernel_pairing']
    _,apiv=eliminate([r+[v] for r,v in zip(jac[2],rhs)],2)
    assert len(apiv)==21==two['augmented_rank'] and two['derivative_rank']==20 and two['compatible'] is False
    b=gram(Q2); assert det(Q2)==1
    assert b[4][1]+b[1][1]-1+b[4][4]-1==-6
    u=modmat(b,2)
    assert [(i,j) for i in range(6) for j in range(i+1,6) if u[i][j]]==[(0,3),(1,4),(2,5),(3,5)]
    # For all36 generators, the exact lower/diagonal combination stays2 mod4.
    for i,j in product(range(6),repeat=2):
        x=[[int(r==i and c==j) for c in range(6)] for r in range(6)]
        bb=gram(correct(Q2,x,2,2))
        assert (bb[4][1]+bb[1][1]-1+bb[4][4]-1)%4==2
    summaries=[]; determinant_nodes=0
    assert [m for m,q in bases]==[2,3,9,27,81]
    assert len(costs['costs'])==5 and costs['scope']['moduli']==[2,3,9,27,81]
    for (m,q),saved in zip(bases,costs['costs']):
        checktime(); d=det(q); b=gram(q); a=[[-abs(x) for x in r] for r in b]; w=literal_lift(b)
        pb,pa,pw=poly_det(b),poly_det(a),poly_det(w)
        assert pb==[d*d*x for x in F] and pw==pmul(pb,pa)
        assert ptr(factor_expression(saved['absolute_factorization']))==ptr(pa[:])
        assert det(b)!=0 and det(a)!=0 and det(w)!=0
        assert pb[-1]==det(b)==d*d and pa[-1]==det(a) and pw[-1]==det(w)
        for t in range(-6,7):
            ev=[[t*w[i][j]+w[j][i] for j in range(12)] for i in range(12)]
            assert det(ev)==peval(pw,t); determinant_nodes+=1
        en=sum(x*x for row in b for x in row); height=max(abs(x) for row in b for x in row)
        assert en==sum(x*x for row in a for x in row)
        assert 2*en==sum(x*x for row in w for x in row)
        assert height==max(abs(x) for row in a for x in row)==max(abs(x) for row in w for x in row)
        calculated=dict(modulus=m,basis_determinant=d,matrix=b,absolute_matrix=a,full_entry_lift=w,
            original_polynomial=pb,absolute_polynomial=pa,full_cover_polynomial=pw,
            absolute_zero=not any(pa),absolute_coefficient_l1=sum(map(abs,pa)),
            rank=6,absolute_rank=6,cover_rank=12,original_degree=6,absolute_degree=6,full_cover_degree=12,
            height=height,whole_squared_entry_sum=en,cover_whole_squared_entry_sum=2*en,
            proper_integer_matrix=proper(b),proper_integer_cover=proper(w),direct_cover_determinant_checks=13)
        assert set(saved)==set(calculated)|{'absolute_factorization'}
        for key,value in calculated.items():assert saved[key]==value,(m,key)
        assert not proper(b) and not proper(w) and abs(pa[-1])>=107
        summaries.append({k:v for k,v in calculated.items() if k not in ('matrix','absolute_matrix','full_entry_lift')})
    # Optional within-run no-write observation, not a historical fingerprint gate.
    assert all((((_J_PROGRAM if name in ('costs.py', 'lift.py', 'readme.md', 'review_independent.py', 'two_adic.py') else _J_OUTPUT) / name)).read_bytes()==data for name,data in before.items())
    if author_before is not None:assert draft.read_bytes()==author_before
    checktime()
    return dict(status='passed', author_program_imports=False, source_files_required_for_future_replay=NATIVE, jacobians_by_integer_symmetric_differences=2, derivative_columns_checked=72, ranks=ranks, odd_prime_saved_minor=16, retained_corrections_verified=step_count, independent_reverse_variable_lifts=independent, mod2_error_pairing=1, mod2_augmented_rank=21, mod4_generator_controls=36, cost_polynomials_by_subset_expansion=15, other_full_polynomial_checks=9, reverse_variable_lifts_differ_from_author=[x['basis'] != y['basis'] for x, y in zip(independent, tests[3]['steps'])], literal_cover_evaluations=determinant_nodes, complete_costs=summaries)

if __name__=='__main__':
    out=main()
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('complete_costs','independent_reverse_variable_lifts','source_files_required_for_future_replay')}))
