"""Prepare an exact, bounded integer triangular ellipsoid enumeration certificate."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
import json
import estimate as e

iv=e.iv
BASE=(_J_PROGRAM / 'prepare.py').parent
B_SCALE=10**8
T_SCALE=10**5
E_SCALE=10**6


def absupper(a):return max(abs(a[0]),abs(a[1]))


def main():
    from sympy import Matrix
    beta,M=e.embeddings();S,bd=e.bounds(beta,M)
    assert S[1]<F(67,10)
    sqrt8=iv.sqrt_interval(iv.point(8))
    weights=[sqrt8,iv.div(sqrt8,iv.point(F(67,10)))]+[iv.point(1)]*8
    weighted=[[iv.mul(M[j][i],weights[j]) for j in range(10)] for i in range(10)]
    B=[[iv.floor((v[0]+v[1])*B_SCALE/2) for v in row] for row in weighted]
    Bmat=Matrix(B)
    reduced,U=Bmat.lll_transform()
    assert U*Bmat==reduced and abs(int(U.det()))==1
    Ui=U.inv()
    assert all(v.q==1 for v in Ui)
    b_bounds=[sum(bd[i]*abs(int(Ui[i,j])) for i in range(10)) for j in range(10)]
    G=reduced*reduced.T
    L=[[F(int(i==j)) for j in range(10)] for i in range(10)]
    D=[]
    for j in range(10):
        d=F(int(G[j,j]))-sum(L[j][k]**2*D[k] for k in range(j))
        assert d>0
        D.append(d)
        for i in range(j+1,10):
            L[i][j]=(F(int(G[i,j]))-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/d
    Ttrue=[[iv.point(0) for _ in range(10)] for _ in range(10)]
    T=[[0]*10 for _ in range(10)]
    for j in range(10):
        diagonal=iv.sqrt_interval(iv.point(D[j]))
        for i in range(j,10):
            v=iv.div(iv.mul(iv.point(L[i][j]),diagonal),iv.point(B_SCALE))
            Ttrue[i][j]=v
            T[i][j]=iv.floor((v[0]+v[1])*T_SCALE/2)
        assert T[j][j]>0
    errors_B=[];errors_T=[]
    for j in range(10):
        errors_B.append(sum(bd[i]*absupper(iv.sub(weighted[i][j],iv.point(F(B[i][j],B_SCALE)))) for i in range(10)))
        errors_T.append(sum(b_bounds[i]*absupper(iv.sub(Ttrue[i][j],iv.point(F(T[i][j],T_SCALE)))) for i in range(10)))
    eps_B=iv.sqrt_interval(iv.point(sum(v*v for v in errors_B)))[1]
    eps_T=iv.sqrt_interval(iv.point(sum(v*v for v in errors_T)))[1]
    bound=iv.sqrt_interval(iv.point(80))[1]+eps_B+eps_T
    radius_squared=iv.ceil(bound**2*T_SCALE**2)
    assert radius_squared<2**53
    embedding_lo=[[iv.floor(v[0]*E_SCALE) for v in row] for row in M]
    embedding_hi=[[iv.ceil(v[1]*E_SCALE) for v in row] for row in M]
    out={'B_scale':B_SCALE,'T_scale':T_SCALE,'embedding_scale':E_SCALE,
         'original_coefficient_bounds':bd,'reduced_coefficient_bounds':b_bounds,
         'integer_rounded_weighted_embedding_basis':B,
         'unimodular_U':[[int(v) for v in row] for row in U.tolist()],
         'integer_triangular_T':T,'squared_enumeration_radius':radius_squared,
         'embedding_lower':embedding_lo,'embedding_upper':embedding_hi,
         'stable_outer_bound_scaled':iv.ceil(S[1]*E_SCALE),
         'error_B_bound':str(eps_B),'error_T_bound':str(eps_T),
         'node_cap':50000000,'candidate_cap':2000000,
         'scope':'exact containing ellipsoid and conservative coordinate filters; volume estimate is not a completeness premise'}
    ((_J_OUTPUT / 'enumeration-certificate.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'original_bounds':bd,'reduced_bounds':b_bounds,'squared_enumeration_radius':radius_squared,
                      'triangle_scale':T_SCALE,'weighted_error_bound':float(eps_B),
                      'triangle_error_bound':float(eps_T),'node_cap':out['node_cap'],'candidate_cap':out['candidate_cap']},indent=2))


if __name__=='__main__':main()
