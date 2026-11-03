"""Exact symbolic coupling identities and independent finite controls."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations, permutations, product
import json
import sympy as sp


def move(v,i,inverse=False):
    q=sp.eye(v.rows)
    a=v[i,i+1]
    q[i,i],q[i+1,i+1]=(-a,0) if inverse else (0,-a)
    q[i,i+1]=q[i+1,i]=1
    w=q.T*v*q
    assert w.is_upper and all(w[j,j]==1 for j in range(w.rows))
    return w,q


def energy(v):
    return sum(v[i,j]**2 for i in range(v.rows) for j in range(i+1,v.rows))


def dot(a,b):
    return (a.T*b)[0]


def symbolic(m):
    left,right=2,3
    n=left+m+right
    v=sp.eye(n)
    for i in range(m-1):v[left+i,left+i+1]=1 if i==m-2 else -1
    # Fully variable earlier and later couplings; do not silently omit either.
    c=sp.Matrix(left,m,lambda i,j:sp.Symbol(f'c{i}_{j}',integer=True))
    r=sp.Matrix(m,right,lambda i,j:sp.Symbol(f'r{i}_{j}',integer=True))
    v[:left,left:left+m]=c
    v[left:left+m,left+m:]=r
    v[0,1]=sp.Symbol('ell',integer=True)
    for i in range(right):
        for j in range(i+1,right):v[left+m+i,left+m+j]=sp.Symbol(f'b{i}_{j}',integer=True)
    v[:left,left+m:]=sp.Matrix(left,right,lambda i,j:sp.Symbol(f'd{i}_{j}',integer=True))
    initial=v.copy()
    e=energy(v)
    u=[c[:,i].col_join(r[i,:].T) for i in range(m)]
    p=sp.eye(n)
    for j in range(m-2):
        v,q=move(v,left+j)
        p=p*q
        s=sum(u[:j+2],sp.zeros(left+right,1))
        expected=1+dot(s,s)-dot(u[0],u[0])
        assert sp.expand(energy(v)-e-expected)==0
    v,q=move(v,left+m-2,True)
    p=p*q
    s=sum(u[:-1],sp.zeros(left+right,1))
    expected=2*dot(s,s)-2*dot(u[-1],s)-dot(u[0],u[0])
    assert sp.expand(energy(v)-e-expected)==0
    core=sp.zeros(m)
    for i in range(m-2):core[i+1,i]=1
    for i in range(m-1):core[i,m-2],core[i,m-1]=-1,1
    core[m-1,m-2]=1
    assert p[left:left+m,left:left+m]==core
    assert abs(core.det())==1
    assert v==p.T*initial*p
    return {'path_block_size':m,'left_dimension':left,'right_dimension':right,
            'variable_couplings':m*(left+right),'all_prefix_and_final_identities':True}


def polynomial_control():
    t=sp.Symbol('t')
    count=0
    for n in range(3,7):
        # Fix first vertex to zero and identify the two cycle directions.
        for tail in permutations(range(1,n)):
            order=(0,)+tail
            if order[1]>order[-1]:continue
            v=sp.eye(n)
            k=0
            for i in range(n):
                a,b=order[i],order[(i+1)%n]
                k+=a<b
                v[min(a,b),max(a,b)]=1 if i==0 else -1
            # Direct determinant evaluations suffice because degree is <=n.
            for x in range(n+1):
                assert (x*v+v.T).det()==(x**k+1)*(x**(n-k)+1)
                absolute=sp.eye(n)-(v-sp.eye(n)).applyfunc(abs)
                assert (x*absolute+absolute.T).det()==(x**k-1)*(x**(n-k)-1)
            count+=1
    return count


def counterexample_control():
    count=0
    gram_survivors=0
    locations=list(combinations(range(4),2))
    for size in range(4):
        for support in combinations(locations,size):
            for signs in product((-1,1),repeat=size):
                v=sp.eye(4)
                for (i,j),sign in zip(support,signs):v[i,j]=sign
                count+=1
                if (v+v.T).det()!=4:continue
                gram_survivors+=1
                assert (v.T-v).det()!=4
    assert count==233 and gram_survivors==32
    return {'all_matrices':count,'surviving_t1_test':gram_survivors,
            'surviving_t_minus1_test':0,'method':'direct determinants at 1 and -1'}


def lattice_controls():
    for n in range(4,13):
        basis=sp.zeros(n)
        for i in range(n-1):basis[i,i]=1;basis[i+1,i]=-1
        basis[n-1,n-1]=basis[0,n-1]=1
        gram=basis.T*basis
        desired=2*sp.eye(n)
        for i in range(n-1):desired[i,i+1]=desired[i+1,i]=-1
        desired[0,n-1]=desired[n-1,0]=1
        assert gram==desired and abs(basis.det())==2
    return {'dimensions_checked':list(range(4,13)),'gram_identity_and_index_two':True}


def degree_controls():
    out=[]
    for n in range(4,7):
        for leaves in range(4):
            size=n*(leaves+1)
            v=sp.eye(size)
            for i in range(n-1):v[i,i+1]=-1
            v[0,n-1]=1
            for i in range(n):
                for j in range(leaves):v[i,n+i*leaves+j]=-1
            initial=energy(v)
            changes=set()
            for i in range(size-1):
                for inv in (False,True):
                    w,_=move(v,i,inv)
                    changes.add(int(energy(w)-initial))
            assert changes <= {0,leaves+1} and leaves+1 in changes
            out.append({'cycle':n,'leaves_per_cycle_vertex':leaves,
                        'energy':int(initial),'one_step_changes':sorted(changes)})
    return out


def main(output_path=None):
    report={'symbolic_arbitrary_couplings':[symbolic(m) for m in range(3,8)],
            'all_ordered_cycle_controls_n3_to_n6':polynomial_control(),
            'rank_four_exclusion':counterexample_control(),
            'lattice_controls':lattice_controls(),
            'degree_controls':degree_controls(),
            'relationship':'Separate checking program by the same authoring agent; not independent review.'}
    (Path(output_path) if output_path is not None else _J_OUTPUT / 'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
