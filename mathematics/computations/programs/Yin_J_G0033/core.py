"""Exact quartic phase arrangement for the full two-step strip kernel."""
from fractions import Fraction as F
from functools import cmp_to_key, lru_cache
from itertools import product
from time import perf_counter

ZERO=(0,0,0,0)
ONE=(1,0,0,0)
BETA=(0,1,0,0)
INV=(1,1,1,-1)
B=(-2,-1,0,1)
S=(-1,-1,0,1)
OUT_PLUS=(-1,0,0,1)
OUT_MINUS=(-3,-2,-1,2)
BOX=tuple(product(range(-8,9),range(-7,8)))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(a,q): return tuple(q*x for x in a)
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b):
    c=[F(0)]*7
    for i in range(4):
        for j in range(4): c[i+j]+=a[i]*b[j]
    for k in range(6,3,-1):
        z=c[k]
        for i,p in enumerate((1,-1,-1,-1)): c[k-4+i]-=z*p
    return tuple(c[:4])

def polynomial(t): return t**4-t**3-t**2-t+1

def beta_interval():
    lo,hi=F(172,100),F(173,100)
    assert polynomial(lo)<0<polynomial(hi)
    # P' is positive throughout this bracket by termwise lower bounds.
    assert 4*lo**3-3*hi**2-2*hi-1>0
    for _ in range(150):
        mid=(lo+hi)/2
        if polynomial(mid)>0: hi=mid
        else: lo=mid
    return lo,hi

ROOT=beta_interval()

@lru_cache(None)
def interval(a):
    lo=hi=F(0)
    for c in reversed(a):
        z=(lo*ROOT[0],lo*ROOT[1],hi*ROOT[0],hi*ROOT[1])
        lo,hi=min(z)+c,max(z)+c
    return lo,hi

@lru_cache(None)
def sign(a):
    if a==ZERO:return 0
    lo,hi=interval(a)
    assert lo>0 or hi<0, ('insufficient exact separation',a)
    return 1 if lo>0 else -1

def compare(a,b):return sign(sub(a,b))

def constants_check():
    assert mul(B,sub(BETA,ONE))==ONE
    assert mul(BETA,INV)==ONE
    assert mul(BETA,B)==S
    assert mul(mul(BETA,BETA),B)==OUT_PLUS
    assert mul(mul(INV,INV),S)==OUT_MINUS
    # Safe coordinate enclosure, using beta in (17/10,18/10).
    gap=F(17,10)-F(10,17)
    bound_b=F(10,7); bound_s=F(17,7)
    bound_op=bound_s+F(18,10); bound_om=bound_b
    assert (bound_op+bound_om+3)/gap<8
    assert (bound_b+bound_s+3)/gap<8
    assert bound_s+2+7*F(10,17)<9
    assert 1+ROOT[1]<3 and 1+1/ROOT[0]<2

def coordinate_value(n,m,axis):
    return add(scale(ONE,n),scale(BETA if axis==0 else INV,m))

def sigma(a):
    out=ZERO;power=ONE
    for coefficient in a:
        out=add(out,scale(power,coefficient));power=mul(power,INV)
    return out

def mask_at(axis,phase):
    caps=(B,OUT_PLUS) if axis==0 else (S,OUT_MINUS)
    return tuple(frozenset(i for i,(n,m) in enumerate(BOX)
            if sign(sub(cap,add(phase,coordinate_value(n,m,axis))))>0
            and sign(add(cap,add(phase,coordinate_value(n,m,axis))))>0)
            for cap in caps)

def breakpoints(axis):
    top=scale(ONE,3 if axis==0 else 2)
    caps=(B,OUT_PLUS) if axis==0 else (S,OUT_MINUS)
    points={ZERO,top}
    for n,m in BOX:
        shift=coordinate_value(n,m,axis)
        for cap in caps:
            for s in (-1,1):
                t=sub(scale(cap,s),shift)
                if sign(t)>0 and sign(sub(t,top))<0:points.add(t)
    ordered=tuple(sorted(points,key=cmp_to_key(compare)))
    assert all(sign(sub(b,a))>0 for a,b in zip(ordered,ordered[1:]))
    return ordered

def interval_masks(axis,points):
    caps=(B,OUT_PLUS) if axis==0 else (S,OUT_MINUS)
    masks=[]
    for left,right in zip(points,points[1:]):
        mid=scale(add(left,right),F(1,2))
        kinds=[]
        for cap in caps:
            kinds.append(frozenset(i for i,(n,m) in enumerate(BOX)
                if sign(sub(cap,add(mid,coordinate_value(n,m,axis))))>0
                and sign(add(cap,add(mid,coordinate_value(n,m,axis))))>0))
        masks.append(tuple(kinds))
    return tuple(masks)

def matrix(xmask,ymask):
    columns=sorted(xmask[0]&ymask[0]);rows=sorted(xmask[1]&ymask[1])
    weights={-1:1,0:2,1:1}
    values=tuple(tuple(weights.get(BOX[c][0]-BOX[r][0],0)*
                       weights.get(BOX[c][1]-BOX[r][1],0)
                       for c in columns) for r in rows)
    # Drop zero rows and columns; this changes neither singular norm nor scope.
    values=tuple(row for row in values if any(row))
    if not values:return ()
    keep=[j for j in range(len(values[0])) if any(row[j] for row in values)]
    return tuple(tuple(row[j] for j in keep) for row in values)

def all_patterns(cap=50000,seconds=60):
    start=perf_counter()
    constants_check()
    xp,yp=breakpoints(0),breakpoints(1)
    xm,ym=interval_masks(0,xp),interval_masks(1,yp)
    assert len(xm)*len(ym)<=cap
    patterns={}
    for i,x in enumerate(xm):
        assert perf_counter()-start<seconds, 'phase construction time cap reached'
        for j,y in enumerate(ym):patterns.setdefault(matrix(x,y),(i,j))
    return xp,yp,patterns

def gram(a):
    return [[sum(x*y for x,y in zip(r,s)) for s in a] for r in a]
