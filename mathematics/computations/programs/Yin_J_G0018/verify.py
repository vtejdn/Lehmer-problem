"""Rational interval proof of the saved neutral triangle certificate.

No floating point, optimization, or discovery helper is used.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

SCALE=10**35


def point(x):return (F(x),F(x))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    z=[x*y for x in a for y in b]
    return (min(z),max(z))
def div(a,b):
    assert b[0]>0 or b[1]<0
    return mul(a,(1/b[1],1/b[0]))
def square(a):
    return (F(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))
def sqrt_interval(a):
    assert a[0]>=0
    low=isqrt((a[0].numerator*SCALE*SCALE)//a[0].denominator)
    hi=isqrt((a[1].numerator*SCALE*SCALE)//a[1].denominator)+1
    return (F(low,SCALE),F(hi,SCALE))
def cmul(a,b):return (sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0])))
def cadd(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
def csub(a,b):return (sub(a[0],b[0]),sub(a[1],b[1]))
def cnorm2(a):return add(square(a[0]),square(a[1]))
def cross(a,b):return sub(mul(a[0],b[1]),mul(a[1],b[0]))


def root_intervals():
    r=sqrt_interval(point(13))
    u=div(add(point(1),r),point(2))
    beta=div(add(u,sqrt_interval(sub(square(u),point(4)))),point(2))
    re=div(sub(point(1),r),point(4))
    im=sqrt_interval(sub(point(1),square(re)))
    return beta,(re,im)


def evaluate_block(word,x,beta,zeta):
    assert 1<=len(word)<=10
    assert all(type(a) is int and a in (-1,0,1) for a in word)
    zinv=(zeta[0],neg(zeta[1]))
    power=(point(1),point(0))
    c=(point(0),point(0))
    for a in word:
        x=add(mul(beta,x),point(a))
        power=cmul(power,zinv)
        c=cadd(c,(mul(point(a),power[0]),mul(point(a),power[1])))
    return x,c


def main():
    base= _J_OUTPUT
    data=json.loads((_J_PROGRAM/'inputs/triangles.json').read_text())
    assert data['grid']==100
    assert [r['j'] for r in data['cells']]==list(range(50,100))
    beta,zeta=root_intervals()
    assert F(17,10)<beta[0]<beta[1]<F(18,10)
    margins=[]
    for row in data['cells']:
        assert len(row['digits'])==3
        interval=(F(row['j'],100),F(row['j']+1,100))
        c=[]
        for word in row['digits']:
            image,z=evaluate_block(word,interval,beta,zeta)
            assert -1<image[0] and image[1]<1
            c.append(z)
        m2=max(cnorm2(z)[1] for z in c)
        radii=[]
        for i in range(3):
            determinant=cross(c[i],c[(i+1)%3])
            assert determinant[0]>0
            edge2=cnorm2(csub(c[(i+1)%3],c[i]))
            edge_upper=sqrt_interval(edge2)[1]
            radius_lower=determinant[0]/edge_upper
            radii.append(radius_lower)
            # The origin is strictly inside the oriented triangle; every edge
            # is at distance > m2/20, so radius ten suffices for strict descent.
            assert 20*radius_lower>m2
        margin=20*min(radii)-m2
        margins.append(margin)
    minimum=min(margins)
    # A compact small rational lower bound, independently checked.
    uniform=F(minimum.numerator*1000//minimum.denominator,1000)
    assert uniform>0
    out={'arithmetic':'Fraction integer interval arithmetic',
         'root_scale':SCALE,'verified_cells':50,'verified_blocks':150,'max_block_length':max(len(w) for r in data['cells'] for w in r['digits']),
         'annulus':['1/2','1'],'expanding_target':['-1','1'],
         'neutral_threshold':10,'uniform_squared_norm_drop_lower':str(uniform),
         'root_definition':'beta=(u+sqrt(u^2-4))/2, u=(1+sqrt(13))/2; Re(zeta)=(1-sqrt(13))/4, Im(zeta)>0',
         'all_strict_interval_and_triangle_checks_passed':True,
         'scope':'geometric block certificate only; compact residual not asserted solved'}
    (base/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
