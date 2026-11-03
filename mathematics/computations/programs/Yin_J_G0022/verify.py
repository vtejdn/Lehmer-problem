"""Exact interval check of all eight joint neutral coordinates.

All operations are Fraction/integer arithmetic, rounded outward to a fixed
rational grid. Numerical roots, weights and radii in the discovery file are
ignored. The trace quintic is isolated by five disjoint sign-changing brackets.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

SCALE=10**40


def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def point(x):return F(x),F(x)
def outward(a):return F(floor(a[0]*SCALE),SCALE),F(ceil(a[1]*SCALE),SCALE)
def add(a,b):return outward((a[0]+b[0],a[1]+b[1]))
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b]
    return outward((min(v),max(v)))
def div(a,b):
    assert b[0]>0 or b[1]<0
    return mul(a,(1/b[1],1/b[0]))
def square(a):
    return outward((0 if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2)))
def sqrt_interval(a):
    assert a[0]>=0
    lo=isqrt(floor(a[0]*SCALE*SCALE))
    hi=isqrt(floor(a[1]*SCALE*SCALE))+1
    return F(lo,SCALE),F(hi,SCALE)
def sum_intervals(a):
    total=point(0)
    for v in a:total=add(total,v)
    return total
def cmul(a,b):return sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0]))


def trace(x):
    result=F(0)
    for a in (1,1,-5,-5,4,3):result=result*x+a
    return result


def check_trace_identity_and_irreducibility():
    # Exact Laurent expansion t^5 Q(t+t^-1).
    result={}
    power={0:1}
    for coefficient in (3,4,-5,-5,1,1):
        for exponent,value in power.items():
            result[exponent+5]=result.get(exponent+5,0)+coefficient*value
        nxt={}
        for exponent,value in power.items():
            for shift in (-1,1):nxt[exponent+shift]=nxt.get(exponent+shift,0)+value
        power=nxt
    assert [result.get(i,0) for i in range(11)]==[1,1,0,-1,-1,-1,-1,-1,0,1,1]
    assert all(value==0 for exponent,value in result.items() if exponent<0 or exponent>10)
    # Q mod 2 is encoded by bits 0,2,3,4,5. Since degree 5 is prime,
    # Q | (u^32-u) and no roots 0,1 prove irreducibility over F_2.
    modulus=61
    def remainder(value):
        while value.bit_length()>=modulus.bit_length():
            value^=modulus<<(value.bit_length()-modulus.bit_length())
        return value
    value=2
    for _ in range(5):
        squared=0
        for i in range(value.bit_length()):
            if value&(1<<i):squared^=1<<(2*i)
        value=remainder(squared)
    assert value==2 and (modulus&1)==1 and modulus.bit_count()%2==1


def roots():
    brackets=[(F(-19,10),F(-18,10)),(F(-15,10),F(-14,10)),
              (F(-6,10),F(-5,10)),(F(9,10),F(1)),(F(2),F(21,10))]
    # Degree five plus five disjoint sign changes proves exactly one root in
    # each bracket and accounts for all roots, without numerical root input.
    assert all(brackets[i][1]<brackets[i+1][0] for i in range(4))
    isolated=[]
    for low,high in brackets:
        fl=trace(low);fh=trace(high)
        assert fl*fh<0
        while high-low>F(1,SCALE*100):
            mid=(low+high)/2;fm=trace(mid)
            assert fm!=0
            if fl*fm<0:high=mid;fh=fm
            else:low=mid;fl=fm
        isolated.append(outward((low,high)))
    u=isolated[-1]
    beta=div(add(u,sqrt_interval(sub(square(u),point(4)))),point(2))
    assert F(117,100)<beta[0]<beta[1]<F(118,100)
    zs=[]
    for t in isolated[:-1]:
        re=div(t,point(2));im=sqrt_interval(sub(point(1),square(re)))
        zs.append((re,im))
    return beta,zs,isolated


def block(word,cell,beta,zs):
    assert 1<=len(word)<=11 and all(type(d) is int and d in (-1,0,1) for d in word)
    x=cell
    powers=[(point(1),point(0)) for _ in zs]
    displacements=[(point(0),point(0)) for _ in zs]
    for d in word:
        x=add(mul(beta,x),point(d))
        for j,z in enumerate(zs):
            powers[j]=cmul(powers[j],(z[0],neg(z[1])))
            displacements[j]=(add(displacements[j][0],mul(point(d),powers[j][0])),
                              add(displacements[j][1],mul(point(d),powers[j][1])))
    return x,[c[0] for c in displacements]+[c[1] for c in displacements]


def inverse(matrix):
    n=len(matrix)
    A=[[v for v in row]+[point(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for k in range(n):
        # Exact midpoint comparison selects a pivot; it is no approximation.
        pivot=max(range(k,n),key=lambda i:abs(A[i][k][0]+A[i][k][1]))
        A[k],A[pivot]=A[pivot],A[k]
        denominator=A[k][k]
        assert denominator[0]>0 or denominator[1]<0
        for j in range(k+1,2*n):A[k][j]=div(A[k][j],denominator)
        A[k][k]=point(1)
        for i in range(n):
            if i==k:continue
            factor=A[i][k]
            for j in range(k+1,2*n):A[i][j]=sub(A[i][j],mul(factor,A[k][j]))
            A[i][k]=point(0)
    return [row[n:] for row in A]


def main(output_path=None):
    base= _J_OUTPUT
    data=json.loads((base/'reused-cover.json').read_text())
    assert data['grid']==100 and [r['j'] for r in data['cells']]==list(range(50,100))
    check_trace_identity_and_irreducibility()
    beta,zs,trace_roots=roots()
    R=1500
    margins=[];radii=[];squared_sizes=[];cached={}
    for row in data['cells']:
        assert len(row['digits'])==9
        cell=(F(row['j'],100),F(row['j']+1,100))
        vertices=[]
        for word in row['digits']:
            x,c=block(word,cell,beta,zs)
            assert -1<x[0] and x[1]<1
            vertices.append(c)
        key=tuple(tuple(w) for w in row['digits'])
        if key not in cached:
            A=[[vertices[j][i] for j in range(9)] for i in range(8)]+[[point(1)]*9]
            inv=inverse(A)
            face_distances=[]
            for bary in inv:
                assert bary[-1][0]>0
                gradient=sqrt_interval(sum_intervals(square(v) for v in bary[:8]))
                assert gradient[0]>0
                face_distances.append(bary[-1][0]/gradient[1])
            radius=min(face_distances)
            m2=max(sum_intervals(square(v) for v in c)[1] for c in vertices)
            assert 2*R*radius-m2>0
            cached[key]=(radius,m2)
        r,m2=cached[key]
        radii.append(r);squared_sizes.append(m2);margins.append(2*R*r-m2)
    delta=F(floor(min(margins)*1000),1000)
    assert delta>0
    out={'arithmetic':'Fraction with outward rounding after every operation',
         'scale':SCALE,'trace_polynomial_descending':[1,1,-5,-5,4,3],
         'trace_identity_and_mod2_irreducibility_checked':True,
         'trace_root_isolation':'five disjoint rational sign-changing brackets; all degree-five roots accounted for',
         'verified_cells':50,'verified_blocks':450,'distinct_joint_simplices':len(cached),
         'joint_real_dimension':8,'max_block_length':max(len(w) for r in data['cells'] for w in r['digits']),
         'neutral_euclidean_threshold':R,'uniform_squared_norm_drop_lower':str(delta),
         'simplex_ball_radius_lower':str(F(floor(min(radii)*10**6),10**6)),
         'largest_vertex_norm_squared_upper':str(F(ceil(max(squared_sizes)*1000),1000)),
         'all_closed_cell_images_and_joint_simplex_checks_passed':True,
         'scope':'full joint neutral descent certificate; compact termination and actual Lehmer return-core infinity not asserted'}
    destination = base/'verification.json' if output_path is None else Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
