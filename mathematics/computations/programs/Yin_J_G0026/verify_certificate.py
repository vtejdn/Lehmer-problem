"""Recompute completeness bounds from retained integer data, without prepare.py."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from array import array
import gzip,json
import estimate as e

iv=e.iv;BASE=(_J_PROGRAM / 'verify_certificate.py').parent


def inverse_exact(M):
    n=len(M);A=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if A[i][k])
        A[k],A[pivot]=A[pivot],A[k]
        d=A[k][k];A[k]=[x/d for x in A[k]]
        for i in range(n):
            if i==k:continue
            c=A[i][k];A[i]=[x-c*y for x,y in zip(A[i],A[k])]
    return [row[n:] for row in A]


def norm_upper(v):return iv.sqrt_interval(iv.point(sum(x*x for x in v)))[1]
def absupper(a):return max(abs(a[0]),abs(a[1]))


def verify_states(raw, run, bounds):
    """Validate the complete saved enumeration without a byte-order binding."""
    assert run['completed'] and len(raw)==8*run['retained_candidates']
    states=array('Q');states.frombytes(raw)
    assert len(set(states))==len(states)
    for key in states:
        assert key<1<<40
        assert all(abs(((key>>(4*i))&15)-8)<=bounds[i] for i in range(10))
    return states


def main():
    inputs=_J_PROGRAM/'inputs'
    c=json.loads((inputs/'enumeration-certificate.json').read_text())
    beta,M=e.embeddings();S,bd=e.bounds(beta,M)
    assert bd==c['original_coefficient_bounds'] and S[1]<F(67,10)
    U=c['unimodular_U'];assert abs(e.determinant(U))==1
    inverse=inverse_exact(U)
    assert all(v.denominator==1 for row in inverse for v in row)
    bbound=[sum(bd[i]*abs(inverse[i][j]) for i in range(10)) for j in range(10)]
    assert bbound==c['reduced_coefficient_bounds']
    Q=c['B_scale'];H=c['T_scale'];B=c['integer_rounded_weighted_embedding_basis'];T=c['integer_triangular_T']
    reduced=[[sum(U[i][k]*B[k][j] for k in range(10)) for j in range(10)] for i in range(10)]
    G=[[F(sum(reduced[i][k]*reduced[j][k] for k in range(10)),Q*Q) for j in range(10)] for i in range(10)]
    # Exact Gram-Schmidt on the retained rational Gram matrix.
    mu=[[F(i==j) for j in range(10)] for i in range(10)];d=[]
    for j in range(10):
        d.append(G[j][j]-sum(mu[j][k]**2*d[k] for k in range(j)))
        assert d[j]>0
        for i in range(j+1,10):mu[i][j]=(G[i][j]-sum(mu[i][k]*mu[j][k]*d[k] for k in range(j)))/d[j]
    eps_triangle=[]
    for j in range(10):
        sq=iv.sqrt_interval(iv.point(d[j]));error=F(0)
        assert T[j][j]>0 and all(T[i][j]==0 for i in range(j))
        for i in range(j,10):
            value=iv.mul(iv.point(mu[i][j]),sq)
            error+=bbound[i]*absupper(iv.sub(value,iv.point(F(T[i][j],H))))
        eps_triangle.append(error)
    sqrt8=iv.sqrt_interval(iv.point(8))
    weights=[sqrt8,iv.div(sqrt8,iv.point(F(67,10)))]+[iv.point(1)]*8
    eps_basis=[]
    for j in range(10):
        eps_basis.append(sum(bd[i]*absupper(iv.sub(iv.mul(M[j][i],weights[j]),iv.point(F(B[i][j],Q)))) for i in range(10)))
    radius=iv.sqrt_interval(iv.point(80))[1]+norm_upper(eps_basis)+norm_upper(eps_triangle)
    assert F(c['squared_enumeration_radius'],H*H)>=radius*radius
    Escale=c['embedding_scale']
    for j in range(10):
        for i in range(10):
            assert F(c['embedding_lower'][j][i],Escale)<=M[j][i][0]
            assert F(c['embedding_upper'][j][i],Escale)>=M[j][i][1]
    assert F(c['stable_outer_bound_scaled'],Escale)>=S[1]
    # Explicit signed-64-bit safety bounds for the compiled loop's arithmetic.
    for j in range(10):
        term=sum(bbound[i]*abs(T[i][j]) for i in range(j,10))
        assert term*term<2**63-1
    assert sum((sum(bd[i]*max(abs(c['embedding_lower'][j][i]),abs(c['embedding_upper'][j][i])) for i in range(10)))**2 for j in range(2,10))<2**63-1
    run=json.loads((inputs/'enumeration.json').read_text(encoding='utf-8-sig'))
    raw=gzip.decompress((inputs/'compact-states.bin.gz').read_bytes())
    states=verify_states(raw, run, bd)
    result={'exact_containing_ellipsoid_verified':True,'unimodular_change_verified':True,
            'coefficient_and_outward_filter_bounds_verified':True,'int64_arithmetic_bounds_verified':True,
            'completed_enumeration_report':run,'unique_retained_states':len(states),
            'scope':'completeness certificate and output integrity; compiled traversal read separately; no zero paths checked'}
    ((_J_OUTPUT / 'certificate-verification.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='completed_enumeration_report'},indent=2))


if __name__=='__main__':main()
