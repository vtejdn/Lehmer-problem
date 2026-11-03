"""Exact coefficient bounds and discriminant; labelled numerical size estimate."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
import importlib.util,json,math

base=(_J_PROGRAM / 'estimate.py').parent
repository=next(parent for parent in base.resolve().parents if (parent/'repository/config.json').is_file())
spec=importlib.util.spec_from_file_location('j22',repository/'mathematics/computations/programs/Yin_J_G0022/verify.py')
iv=importlib.util.module_from_spec(spec);spec.loader.exec_module(iv)


def embeddings():
    beta,zs,_=iv.roots();r=iv.div(iv.point(1),beta)
    bp=[iv.point(1)];rp=[iv.point(1)];zp=[[(iv.point(1),iv.point(0))] for z in zs]
    for _ in range(9):
        bp.append(iv.mul(bp[-1],beta));rp.append(iv.mul(rp[-1],r))
        for j,z in enumerate(zs):zp[j].append(iv.cmul(zp[j][-1],z))
    M=[bp,rp]+[[v[0] for v in ps] for ps in zp]+[[v[1] for v in ps] for ps in zp]
    return beta,M


def bounds(beta,M):
    A=iv.inverse(M);S=iv.div(beta,iv.sub(beta,iv.point(1)))
    bd=[]
    for row in A:
        real=max(map(abs,row[0]))+S[1]*max(map(abs,row[1]))
        neutral=iv.sqrt_interval(iv.sum_intervals(iv.square(v) for v in row[2:]))[1]
        bd.append(iv.floor(real+8*neutral))
    return S,bd


def determinant(matrix):
    A=[r[:] for r in matrix];n=len(A);prev=1;sgn=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next(i for i in range(k+1,n) if A[i][k])
            A[k],A[p]=A[p],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=A[i][j]*pivot-A[i][k]*A[k][j]
                assert value%prev==0
                A[i][j]=value//prev
            A[i][k]=0
        prev=pivot
    return sgn*A[-1][-1]


def discriminant():
    p=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
    d=[p[i]*i for i in range(1,11)]
    syl=[]
    for shift in range(9):syl.append([0]*shift+p+[0]*(8-shift))
    for shift in range(10):syl.append([0]*shift+d+[0]*(9-shift))
    return -determinant(syl)


def main():
    iv.check_trace_identity_and_irreducibility()
    beta,M=embeddings();S,bd=bounds(beta,M)
    disc=discriminant()
    sf=float(sum(S)/2);R=8
    cov=math.sqrt(abs(disc))/16
    volume=4*sf*(math.pi**4/math.factorial(4))*R**8
    # Optimized product-containing ellipsoid: 8*x+^2+8*x-^2/S^2+rho^2<=80.
    ellipse=(math.pi**5/math.factorial(5))*80**5*sf/8
    out={'coefficient_bounds':bd,'complete_power_box_tuples':math.prod(2*b+1 for b in bd),
         'discriminant_exact':disc,'sqrt_abs_discriminant_exact':math.isqrt(abs(disc)),
         'covolume_numerical':cov,'S_numerical':sf,
         'volume_over_covolume_K8_diagnostic':volume/cov,
         'optimized_ellipsoid_volume_over_covolume_diagnostic':ellipse/cov,
         'diagnostic_warning':'volume ratios are heuristic counts, not integer enumeration bounds',
         'algorithm_candidate':'exact rational enclosure, unimodular reduced basis, certified triangular branch enumeration'}
    ((_J_OUTPUT / 'estimate.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
