"""Exact finite superset of D13's compact quartic residual.

This uses the reviewed J18 rational root intervals, then outward rounds every
embedding power to a fixed integer scale for fast, still exact, enumeration.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product, permutations
from fractions import Fraction as F
import importlib.util, json

base= _J_OUTPUT
spec=importlib.util.spec_from_file_location('j18_intervals',_J_PROGRAM.parent/'Yin_J_G0018'/'verify.py')
iv=importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
Q=10**25


def floor(x): return x.numerator//x.denominator
def ceil(x): return -floor(-x)
def absupper(a): return max(abs(a[0]),abs(a[1]))
def determinant(a):
    n=len(a)
    total=iv.point(0)
    for p in permutations(range(n)):
        parity=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=iv.point((-1)**parity)
        for i in range(n): term=iv.mul(term,a[i][p[i]])
        total=iv.add(total,term)
    return total


def embeddings():
    b,z=iv.root_intervals()
    r=iv.div(iv.point(1),b)
    bp=[iv.point(1)];rp=[iv.point(1)];zp=[(iv.point(1),iv.point(0))]
    for j in range(3):
        bp.append(iv.mul(bp[-1],b));rp.append(iv.mul(rp[-1],r))
        zp.append(iv.cmul(zp[-1],z))
    return b,[bp,rp,[v[0] for v in zp],[v[1] for v in zp]]


def bounds(matrix,S):
    det=determinant(matrix)
    assert det[0]>0 or det[1]<0
    inverse=[]
    for i in range(4):
        row=[]
        for j in range(4):
            minor=[[matrix[k][l] for l in range(4) if l!=i] for k in range(4) if k!=j]
            adj=iv.mul(iv.point((-1)**(i+j)),determinant(minor))
            row.append(iv.div(adj,det))
        inverse.append(row)
    bd=[]
    for row in inverse:
        neutral=iv.sqrt_interval(iv.add(iv.square(row[2]),iv.square(row[3])))[1]
        bd.append(floor(absupper(row[0])+S[1]*absupper(row[1])+10*neutral))
    return bd


def integer_rows(matrix):
    return [[(floor(a[0]*Q),ceil(a[1]*Q)) for a in row] for row in matrix]


def evaluate(a,row):
    lo=hi=0
    for x,(l,h) in zip(a,row):
        lo+=x*(l if x>=0 else h)
        hi+=x*(h if x>=0 else l)
    return lo,hi


def min_square(interval):
    l,h=interval
    return 0 if l<=0<=h else min(l*l,h*h)


def main():
    beta,matrix=embeddings()
    S=iv.div(beta,iv.sub(beta,iv.point(1)))
    bd=bounds(matrix,S)
    rows=integer_rows(matrix)
    stable=ceil(S[1]*Q)
    candidates=[]
    examined=0
    for tail in product(*(range(-v,v+1) for v in bd[1:])):
        tail_interval=evaluate((0,)+tail,rows[0])
        a0lo=max(-bd[0],ceil(F(-Q-tail_interval[1],Q)))
        a0hi=min(bd[0],floor(F(Q-tail_interval[0],Q)))
        for a0 in range(a0lo,a0hi+1):
            a=(a0,)+tail
            examined+=1
            sm=evaluate(a,rows[1])
            if sm[0]>stable or sm[1]<-stable:continue
            zr=evaluate(a,rows[2]);zi=evaluate(a,rows[3])
            if min_square(zr)+min_square(zi)>=100*Q*Q:continue
            candidates.append(a)
    out={'method':'outward rational inverse-embedding coefficient bounds and exhaustive integer slicing',
         'scale':Q,'coefficient_bounds':bd,'stable_outer_bound':str(F(stable,Q)),
         'sliced_integer_tuples_examined':examined,'candidate_count':len(candidates),
         'scope':'certified finite superset of K; ambiguous boundary points retained',
         'states':candidates}
    (base/'compact.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='states'},indent=2))


if __name__=='__main__':main()
