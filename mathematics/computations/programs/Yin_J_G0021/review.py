"""Independent scaled-integer enclosure and polynomial certificate replay.

Reads author data; imports no author interval, enumeration or path helper.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from math import isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

Q = 10**25


def ceiling(a, b):
    return -((-a)//b)


class Box:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = lo, lo if hi is None else hi
        assert self.lo <= self.hi

    @staticmethod
    def exact(value):
        f = Fraction(value)
        return Box((f.numerator*Q)//f.denominator,
                   ceiling(f.numerator*Q, f.denominator))

    def __add__(self, other):
        return Box(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        corners = [a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return Box(min(corners)//Q, ceiling(max(corners),Q))

    def __truediv__(self, other):
        assert other.lo > 0 or other.hi < 0
        corners = [Fraction(a*Q,b) for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        low, high = min(corners), max(corners)
        return Box(low.numerator//low.denominator,
                   ceiling(high.numerator,high.denominator))

    def square(self):
        least = 0 if self.lo <= 0 <= self.hi else min(self.lo**2,self.hi**2)
        most = max(self.lo**2,self.hi**2)
        return Box(least//Q,ceiling(most,Q))

    def sqrt(self):
        assert self.lo >= 0
        low = isqrt(self.lo*Q)
        high = isqrt(self.hi*Q)
        high += high*high < self.hi*Q
        return Box(low,high)

    def absmax(self):
        return max(abs(self.lo),abs(self.hi))


ZERO, ONE = Box.exact(0), Box.exact(1)


def polynomial(t):
    return t**4-t**3-t**2-t+1


def roots():
    # Isolate beta directly by sign bisection, rather than importing J18.
    low, high = Fraction(17,10), Fraction(18,10)
    assert polynomial(low) < 0 < polynomial(high)
    while high-low > Fraction(1,Q):
        mid=(low+high)/2
        if polynomial(mid)<0:
            low=mid
        else:
            high=mid
    beta=Box(Box.exact(low).lo,Box.exact(high).hi)
    real=(ONE-Box.exact(13).sqrt())/Box.exact(4)
    imag=(ONE-real.square()).sqrt()
    return beta, (real,imag)


def cmul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def cplus(a,b):
    return (a[0]+b[0],a[1]+b[1])


def triangle_check(data,beta,zeta):
    assert data['grid']==100
    assert [r['j'] for r in data['cells']]==list(range(50,100))
    margin=10**100
    count=0
    maximum=0
    for row in data['cells']:
        assert len(row['digits'])==3
        vertices=[]
        for word in row['digits']:
            assert 1<=len(word)<=9
            assert all(type(d) is int and d in (-1,0,1) for d in word)
            x=Box(row['j']*Q//100,(row['j']+1)*Q//100)
            power=(ONE,ZERO)
            vertex=(ZERO,ZERO)
            for d in word:
                x=beta*x+Box.exact(d)
                power=cmul(power,(zeta[0],-zeta[1]))
                vertex=cplus(vertex,(Box.exact(d)*power[0],Box.exact(d)*power[1]))
            assert -Q<x.lo and x.hi<Q
            vertices.append(vertex)
            count+=1
            maximum=max(maximum,len(word))
        squared=max((a.square()+b.square()).hi for a,b in vertices)
        for i in range(3):
            a,b=vertices[i],vertices[(i+1)%3]
            det=a[0]*b[1]-a[1]*b[0]
            assert det.lo>0
            edge=((b[0]-a[0]).square()+(b[1]-a[1]).square()).sqrt()
            r_lower=Fraction(det.lo,edge.hi)
            m=20*r_lower-Fraction(squared,Q)
            assert m>=Fraction(557,500)
            margin=min(margin,m)
    return {'verified_cells':50,'verified_words':count,'maximum_length':maximum,
            'minimum_margin_lower_rounded_down_1e6':str(Fraction(margin.numerator*10**6//margin.denominator,10**6))}


def embedding_matrix(beta,zeta):
    bp,rp,zp=[ONE],[ONE],[(ONE,ZERO)]
    for _ in range(3):
        bp.append(bp[-1]*beta)
        rp.append(rp[-1]/beta)
        zp.append(cmul(zp[-1],zeta))
    return [bp,rp,[z[0] for z in zp],[z[1] for z in zp]]


def invert(matrix):
    # Interval Gaussian elimination gives an enclosure of the exact inverse.
    rows=[list(row)+[Box.exact(int(i==j)) for j in range(4)] for i,row in enumerate(matrix)]
    for col in range(4):
        pivot=next(i for i in range(col,4) if rows[i][col].lo>0 or rows[i][col].hi<0)
        rows[col],rows[pivot]=rows[pivot],rows[col]
        divisor=rows[col][col]
        rows[col]=[x/divisor for x in rows[col]]
        for i in range(4):
            if i==col:
                continue
            factor=rows[i][col]
            rows[i]=[a-factor*b for a,b in zip(rows[i],rows[col])]
    return [row[4:] for row in rows]


def linear(a,row):
    result=ZERO
    for coefficient,entry in zip(a,row):
        result=result+Box.exact(coefficient)*entry
    return result


def enumeration_check(author,matrix,beta):
    inverse=invert(matrix)
    stable=beta/(beta-ONE)
    limits=[]
    for row in inverse:
        neutral=(row[2].square()+row[3].square()).sqrt()
        bound=Fraction(row[0].absmax(),Q)+Fraction(stable.hi*row[1].absmax(),Q*Q)+10*Fraction(neutral.hi,Q)
        limits.append(bound.numerator//bound.denominator)
    assert limits==[5,7,7,4]
    kept=set()
    expanding=0
    total=0
    for a in product(*(range(-v,v+1) for v in limits)):
        total+=1
        xp=linear(a,matrix[0])
        if xp.lo>Q or xp.hi<-Q:
            continue
        expanding+=1
        xm=linear(a,matrix[1])
        if xm.lo>stable.hi or xm.hi<-stable.hi:
            continue
        re,im=linear(a,matrix[2]),linear(a,matrix[3])
        if (re.square()+im.square()).lo>=100*Q:
            continue
        kept.add(a)
    saved={tuple(x) for x in author['states']}
    assert len(saved)==len(author['states'])==259
    assert kept==saved
    assert author['coefficient_bounds']==limits
    return {'coefficient_bounds':limits,'full_box_tuples':total,
            'expanding_strip_tuples':expanding,'retained_candidates':len(kept),
            'matches_author_set':True},kept


def polynomial_remainder(coefficients):
    a=list(coefficients)
    # Divide by P with coefficients [1,-1,-1,-1,1].
    for k in range(len(a)-1,3,-1):
        c=a[k]
        for j,p in enumerate((1,-1,-1,-1,1)):
            a[k-4+j]-=c*p
    return tuple((a+[0]*4)[:4])


def continuation_check(data,candidates):
    covered=set()
    maximum=0
    for row in data['witnesses']:
        a=tuple(row['state'])
        w=row['digits']
        assert len(a)==4 and all(type(x) is int for x in a)
        assert a in candidates and a not in covered
        assert all(type(d) is int and d in (-1,0,1) for d in w)
        # Verify the whole polynomial identity, not the author's step recurrence.
        polynomial=list(reversed(w))+list(a)
        assert polynomial_remainder(polynomial)==(0,0,0,0)
        covered.add(a)
        maximum=max(maximum,len(w))
    assert covered==candidates
    return {'verified_paths':len(covered),'maximum_length':maximum,
            'method':'whole-word integer polynomial long division'}


def main():
    base= _J_OUTPUT
    j18=base.parent/'Yin_J_G0018'
    j19=base.parent/'Yin_J_G0019'
    beta,zeta=roots()
    out={'scale':Q,'author_code_imported':False,
         'triangles':triangle_check(json.loads((j18/'triangles.json').read_text()),beta,zeta)}
    out['enumeration'],candidates=enumeration_check(json.loads((j19/'compact.json').read_text()),embedding_matrix(beta,zeta),beta)
    out['continuations']=continuation_check(json.loads((j19/'paths.json').read_text()),candidates)
    (base/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
