"""Independent D141 finite review: direct ordered-column coverage, no author imports.

Declared complete domain: all norm-one ordered bases of the stated form over F2,
all 32768 upper forms for separately reproduced stage counts, all saved lift
certificates and full original/absolute/literal-cover coefficient arrays.
120 second cap; standard library only. Draft presence is optional and is never
a mathematical input. Native bytes are compared only before/after this run.
"""
from collections import Counter
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
import json

HOME = (_J_PROGRAM / 'review_independent.py').parent
NATIVE = ('readme.md', 'classify.py', 'classification.json', 'verify.py', 'verification.json')
V = [[0,-1,-2,0,-1,0],[1,0,-1,1,0,1],[2,1,0,2,1,1],
     [0,-1,-1,0,-1,0],[1,-1,-1,1,0,1],[1,-1,-1,0,-1,0]]
N = 6
UP = [(i,j) for i in range(N) for j in range(i+1,N)]
POS = [(i,j) for i in range(N) for j in range(i)]+[(i,i) for i in range(N)]

def tr(a):
    return [list(c) for c in zip(*a)]

def mul(a,b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]

def bits(a):
    return tuple(sum((x&1)<<j for j,x in enumerate(r)) for r in a)

def matrix(rows):
    return [[(r>>j)&1 for j in range(N)] for r in rows]

def column_rows(cols):
    return tuple(sum(((v>>i)&1)<<j for j,v in enumerate(cols)) for i in range(N))

def span(columns):
    """Image-space echelon basis, highest set bit; no row left-kernel reduction."""
    basis = {}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p not in basis:
                basis[p]=c
                break
            c ^= basis[p]
    return basis

def residue(value,basis):
    for p in sorted(basis,reverse=True):
        if (value>>p)&1:
            value ^= basis[p]
    return value

def act(cols,v):
    answer=0
    for j,c in enumerate(cols):
        if (v>>j)&1:
            answer ^= c
    return answer

def cyclic_columns(cols,v):
    ans=[]
    for _ in range(N):
        ans.append(v)
        v=act(cols,v)
    return ans

def annihilated(cols):
    # Evaluate I+C^2+C^3+C^4+C^6 on each standard basis vector.
    for j in range(N):
        w=1<<j
        value=0
        for k in range(7):
            if k in (0,2,3,4,6):
                value ^= w
            w=act(cols,w)
        if value:
            return False
    return True

def solve_binary(a,rhs):
    # Tiny augmented elimination, used ONLY to derive C0, not for compatibility.
    b=[[x&1 for x in r]+[(rhs[i]>>0)&1] for i,r in enumerate(a)]
    for j in range(len(a)):
        p=next(i for i in range(j,len(a)) if b[i][j])
        b[j],b[p]=b[p],b[j]
        for i in range(len(a)):
            if i!=j and b[i][j]:
                b[i]=[x^y for x,y in zip(b[i],b[j])]
    return sum(b[i][-1]<<i for i in range(len(a)))

def determinant(a):
    a=[r[:] for r in a]
    n=len(a);sign=1;previous=1
    for k in range(n-1):
        if not a[k][k]:
            p=next((i for i in range(k+1,n) if a[i][k]),None)
            if p is None:
                return 0
            a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def pencil(a):
    """Full coefficient determinant by subset/permutation DP, no interpolation."""
    n=len(a)
    dp={0:[1]}
    for row in range(n):
        nxt={}
        for mask,p in dp.items():
            for col in range(n):
                if (mask>>col)&1:
                    continue
                c0=a[col][row];c1=a[row][col]
                if c0==c1==0:
                    continue
                sign=-1 if (mask>>(col+1)).bit_count()%2 else 1
                out=nxt.setdefault(mask|(1<<col),[0]*(row+2))
                for k,coef in enumerate(p):
                    out[k]+=sign*c0*coef
                    out[k+1]+=sign*c1*coef
        dp=nxt
    return dp[(1<<n)-1]

def convolve(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return out

def run():
    started=perf_counter()
    def cap():
        assert perf_counter()-started<120, 'Declared 120-second review cap reached'
    original={name:(((_J_PROGRAM if name in ('classify.py', 'readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in NATIVE}
    data=json.loads(original['classification.json'])
    cost=json.loads(original['verification.json'])
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0141.md')
    draft_before=draft.read_bytes() if draft.exists() else None
    assert data['V0']==V and data['complete'] is True
    assert data['domain']=={'all_upper_forms':32768,'all_vector_images':64,
                           'modulus':4}

    # Complete congruence enumeration through direct ordered columns.
    # A new norm-one vector orthogonal on the left to earlier columns is
    # automatically independent: their prior upper-unitriangular Gram is invertible.
    pair=[[sum(((x>>i)&1)*V[i][j]*((y>>j)&1)
               for i in range(N) for j in range(N)) for y in range(64)] for x in range(64)]
    norm_one=[x for x in range(64) if pair[x][x]&1]
    levels=[0]*7
    independent_bases={}
    def extend(cols,candidates):
        levels[len(cols)]+=1
        if len(cols)==6:
            key=column_rows(cols)
            assert key not in independent_bases
            b=[[pair[x][y] for y in cols] for x in cols]
            u=[[z&1 for z in row] for row in b]
            mask=sum(u[i][j]<<k for k,(i,j) in enumerate(UP))
            independent_bases[key]=(mask,b)
            return
        for x in candidates:
            extend(cols+[x],[v for v in candidates if pair[v][x]%2==0])
    extend([],norm_one)
    cap()
    assert len(independent_bases)==5625
    assert len(norm_one)==28
    observed=Counter(mask for mask,b in independent_bases.values())
    assert len(observed)==375 and set(observed.values())=={15}

    # Independent complete upper-form stage counts using direct back substitution
    # and column action, rather than author's row-matrix inversion/Horner code.
    counts={'processed_upper_forms':32768,'nonsingular_symmetric_forms':0,
            'annihilator_forms':0,'cyclic_forms':0,'congruent_forms':len(observed),
            'binary_bases':len(independent_bases),'liftable_bases':0,'nonliftable_bases':5625}
    cyclic_forms={}
    for mask in range(32768):
        if mask%256==0: cap()
        u=[[int(i==j) for j in range(N)] for i in range(N)]
        for k,(i,j) in enumerate(UP):
            u[i][j]=(mask>>k)&1
        symcols=[sum((u[i][j]^u[j][i])<<i for i in range(N)) for j in range(N)]
        if len(span(symcols))!=6:
            continue
        counts['nonsingular_symmetric_forms']+=1
        c=[]
        for j in range(N):
            x=[0]*N
            for i in reversed(range(N)):
                x[i]=(u[j][i]+sum(u[i][v]*x[v] for v in range(i+1,N)))%2
            c.append(sum(z<<i for i,z in enumerate(x)))
        if not annihilated(c):
            continue
        counts['annihilator_forms']+=1
        first=next((v for v in range(64) if len(span(cyclic_columns(c,v)))==6),None)
        if first is not None:
            counts['cyclic_forms']+=1
            cyclic_forms[mask]=(u,c,first)
    assert counts==data['counts']
    assert set(cyclic_forms)==set(observed)
    c0=[solve_binary(V,[V[j][i] for i in range(N)]) for j in range(N)]
    assert column_rows(c0)==tuple(data['C0_rows'])==tuple([4,16,32,17,34,8])
    assert annihilated(c0)
    cyclic0=[v for v in range(64) if len(span(cyclic_columns(c0,v)))==6]
    assert cyclic0==data['cyclic_vectors_C0'] and len(cyclic0)==45
    k0=matrix(column_rows(cyclic_columns(c0,1)))
    assert bits(k0)==(17,16,8,50,40,36) and determinant(k0)==1

    # Image columns of derivative; decide consistency by whether error is in their span.
    saved_seen=set();ranks=Counter();nonzero_residues=Counter();all_certificates=0
    for form in data['forms']:
        mask=form['upper_mask'];u,c,first=cyclic_forms[mask]
        assert bits(u)==tuple(form['upper_rows']) and first==form['cyclic_vector']
        images=[]
        for a in range(N):
            for b in range(N):
                image=sum(((int(j==b)*u[i][a]+int(i==b)*u[a][j])%2)<<k
                          for k,(i,j) in enumerate(POS))
                images.append(image)
        image_space=span(images)
        rank=len(image_space)
        assert rank==form['linear_rank']==19
        ranks[rank]+=1
        kernel=form['left_kernel_basis']
        assert len(kernel)==2 and len(span(kernel))==2
        assert all((z&im).bit_count()%2==0 for z in kernel for im in images)
        assert len(form['bases'])==observed[mask]
        for rec in form['bases']:
            key=tuple(rec['Q_rows'])
            assert key not in saved_seen and key in independent_bases
            saved_seen.add(key)
            found_mask,gram=independent_bases[key]
            assert found_mask==mask
            q=matrix(key)
            assert determinant(q)%2==1
            assert mul(mul(tr(q),V),q)==gram
            e=0
            for k,(i,j) in enumerate(POS):
                raw=gram[i][j]-int(i==j)
                assert raw%2==0
                e|=((raw//2)%2)<<k
            assert e==rec['error_bits']
            rem=residue(e,image_space)
            assert rem!=0
            nonzero_residues[rem]+=1
            z=rec['inconsistency_witness']
            assert 0<z<1<<21
            assert all((z&im).bit_count()%2==0 for im in images)
            assert (z&e).bit_count()%2==1
            cols=[sum(q[i][j]<<i for i in range(N)) for j in range(N)]
            assert act(cols,first)==rec['image_vector']
            # Every six-column intertwining equality, including the final iterate.
            for j in range(N):
                assert act(c0,cols[j])==act(cols,c[j])
            all_certificates+=1
        cap()
    assert saved_seen==set(independent_bases) and all_certificates==5625

    # Displayed readable witness and exact integer values.
    q=matrix([13,54,53,29,42,10]);gram=mul(mul(tr(q),V),q)
    assert determinant(q)==-1 and bits(gram)==(35,18,12,8,16,32)
    assert gram[3][2]+gram[2][2]-1+gram[3][3]-1==-6
    assert [POS[i] for i in range(21) if (393248>>i)&1]==[(3,2),(2,2),(3,3)]
    assert sum((((gram[i][j]-int(i==j))//2)%2)<<k for k,(i,j) in enumerate(POS))==1135803

    # Full polynomials, including the literal rank12 coefficient determinant.
    g=[[V[i][j]+V[j][i] for j in range(6)] for i in range(6)]
    assert determinant(V)==1 and determinant(g)==-1
    assert all(g[i][i]==0 for i in range(6))
    expected_g={(0,5):1,(1,4):-1,(2,3):1}
    assert all(g[i][j]==expected_g.get((i,j),0) for i in range(6) for j in range(i+1,6))
    absolute=[[-abs(x) for x in r] for r in V]
    cover=[[0]*12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            for a in range(2):
                for b in range(2):
                    cover[2*i+a][2*j+b]=(-abs(V[i][j]) if
                        ((a==b and V[i][j]<=0) or (a!=b and V[i][j]>0)) else 0)
    polynomials=[pencil(a) for a in (V,absolute,cover)]
    assert polynomials[0]==convolve([1,-1,1],[1,-1,-1,-1,1])
    assert polynomials[1]==[-1,0,7,11,7,0,-1]
    assert polynomials[2]==convolve(polynomials[0],polynomials[1])
    for t in range(-6,7):
        value=determinant([[t*cover[i][j]+cover[j][i] for j in range(12)] for i in range(12)])
        assert value==sum(c*t**i for i,c in enumerate(polynomials[2]))
    reconstructed={'all_saved_inconsistency_certificates_checked':5625,
                   'distinct_forms':375,'linear_rank_distribution':{'19':375},
                   'no_new_basis_search':True,
                   'original_matrix':V,'symmetric_matrix':g,'absolute_matrix':absolute,
                   'literal_cover_matrix':cover,'original_polynomial':polynomials[0],
                   'absolute_polynomial':polynomials[1],'literal_cover_polynomial':polynomials[2],
                   'ranks':[6,6,12], 'degrees':[6,6,12],
                   'heights':[max(abs(v) for row in a for v in row) for a in (V,absolute,cover)],
                   'whole_squared_entry_sums':[sum(v*v for row in a for v in row) for a in (V,absolute,cover)],
                   'direct_cover_evaluations':13,'absolute_coefficient_l1':sum(abs(x) for x in polynomials[1])}
    assert all(determinant(a)!=0 for a in (V,absolute,cover))
    assert cost==reconstructed
    # Strict metadata type agreement, not just Python's bool/int or int/float equality.
    def types_equal(a,b):
        if type(a) is not type(b): return False
        if isinstance(a,dict): return a.keys()==b.keys() and all(types_equal(a[k],b[k]) for k in a)
        if isinstance(a,list): return len(a)==len(b) and all(types_equal(x,y) for x,y in zip(a,b))
        return a==b
    assert types_equal(cost,reconstructed)
    cap()
    assert all((((_J_PROGRAM if name in ('classify.py', 'readme.md', 'review_independent.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()==raw for name,raw in original.items())
    if draft_before is not None:
        assert draft.read_bytes()==draft_before
    return {'passed': True, 'review_method': 'direct norm-one ordered-column recursion; image-space compatibility; subset polynomial determinants', 'author_imports': False, 'third_party_imports': False, 'norm_one_vectors': len(norm_one), 'complete_prefix_counts': levels, 'complete_stage_counts': counts, 'independent_exact_basis_set_matches': True, 'cyclic_vectors_C0': len(cyclic0), 'linear_rank_distribution': dict(ranks), 'all_saved_witnesses_and_full_kernel_bases_checked': 5625, 'nonzero_image_quotient_residues': dict(nonzero_residues), 'full_polynomials': polynomials, 'full_cost_payload_and_types_match': True}

if __name__=='__main__':
    report=run()
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
