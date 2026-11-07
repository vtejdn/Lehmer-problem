"""Independent whole-node polynomial identities and exact 70-point exclusions."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from array import array
from math import isqrt
import json, struct, platform, gzip

BASE=(_J_PROGRAM / 'verify.py').parent
SOURCE=(_J_ROOT / 'mathematics/computations/programs/Yin_J_G0026/inputs')
P=(1,1,0,-1,-1,-1,-1,-1,0,1,1)
PRECISION=10**50


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def const(x):return (F(x),F(x))
def mul(a,b):
    corners=[x*y for x in a for y in b]
    return min(corners),max(corners)
def divide(a,b):
    assert b[0]>0 or b[1]<0
    return mul(a,(1/b[1],1/b[0]))
def square(a):
    return (F(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))
def sqrt(a):
    assert a[0]>=0
    return F(isqrt(a[0].numerator*PRECISION**2//a[0].denominator),PRECISION),F(isqrt(a[1].numerator*PRECISION**2//a[1].denominator)+1,PRECISION)


def trace(x):
    y=0
    for c in (1,1,-5,-5,4,3):y=y*x+c
    return y


def embeddings():
    intervals=[]
    for a,b in [(-19,-18),(-15,-14),(-6,-5),(9,10),(20,21)]:
        lo,hi=F(a,10),F(b,10)
        assert trace(lo)*trace(hi)<0
        while hi-lo>F(1,PRECISION):
            mid=(lo+hi)/2
            if trace(lo)*trace(mid)<0:hi=mid
            else:lo=mid
        intervals.append((lo,hi))
    u=intervals[-1]
    beta=divide(add(u,sqrt(sub(square(u),const(4)))),const(2))
    stable=divide(beta,sub(beta,const(1)))
    rows=[]
    for root in (beta,divide(const(1),beta)):
        powers=[const(1)]
        for _ in range(9):powers.append(mul(powers[-1],root))
        rows.append(powers)
    reals=[];imags=[]
    for u in intervals[:-1]:
        re=divide(u,const(2));im=sqrt(sub(const(1),square(re)))
        powers=[(const(1),const(0))]
        for _ in range(9):
            a,b=powers[-1]
            powers.append((sub(mul(a,re),mul(b,im)),add(mul(a,im),mul(b,re))))
        reals.append([v[0] for v in powers]);imags.append([v[1] for v in powers])
    return rows+reals+imags,stable


def decode(key,bits,offset):
    return [(key>>(bits*i)&((1<<bits)-1))-offset for i in range(10)]


def repack(a):
    assert all(-16<=x<=15 for x in a)
    return sum((x+16)<<(5*i) for i,x in enumerate(a))


def main():
    # Explicit little-endian reads; no native-endian array interpretation.
    raw=gzip.decompress((SOURCE/'compact-states.bin.gz').read_bytes())
    assert len(raw)%8==0
    targets=set()
    for (key,) in struct.iter_unpack('<Q',raw):
        assert key<1<<40
        value=repack(decode(key,4,8))
        assert value not in targets
        targets.add(value)
    assert len(targets)==797507
    keys=array('Q');depths=array('I');seen=set()
    max_depth=0
    for data in [gzip.decompress((SOURCE/'path-nodes.bin.gz').read_bytes())]:
        assert len(data)%13==0
        for key,parent,code in struct.iter_unpack('<QIB',data):
            index=len(keys)
            assert key<1<<50 and key not in seen and code in (0,1,2)
            a=decode(key,5,16)
            if index==0:
                assert a==[0]*10 and parent==0 and code==1
                depth=0
            else:
                assert parent<index
                # The degree-ten polynomial t*a(t)+digit-parent(t) must be
                # exactly a_9*P(t); compare all eleven coefficients.
                parent_coefficients=decode(keys[parent],5,16)
                difference=[code-1]+a
                for i,v in enumerate(parent_coefficients):difference[i]-=v
                assert tuple(difference)==tuple(a[-1]*v for v in P)
                depth=depths[parent]+1
            keys.append(key);depths.append(depth);seen.add(key)
            max_depth=max(max_depth,depth)
    assert len(keys)==1044588 and max_depth==25
    uncovered=targets-seen
    assert len(uncovered)==70
    saved={key for (key,) in struct.iter_unpack('<Q',(SOURCE/'uncovered.bin').read_bytes())}
    assert uncovered==saved
    rows,stable=embeddings()
    records=[];counts={}
    for key in sorted(uncovered):
        a=decode(key,5,16)
        values=[]
        for row in rows:
            value=const(0)
            for c,v in zip(a,row):value=add(value,mul(const(c),v))
            values.append(value)
        neutral=const(0)
        for v in values[2:]:neutral=add(neutral,square(v))
        if values[0][0]>1 or values[0][1]<-1:reason='expanding'
        elif values[1][0]>stable[1] or values[1][1]<-stable[1]:reason='contracting'
        elif neutral[0]>=64:reason='neutral_at_least_64'
        else:raise AssertionError(('not excluded',a,neutral))
        counts[reason]=counts.get(reason,0)+1
        records.append({'state':a,'reason':reason,
                        'neutral_squared_lower_floor_1e12':str(F(neutral[0].numerator*10**12//neutral[0].denominator,10**12))})
    assert counts=={'neutral_at_least_64':68,'contracting':2}
    result={'author_helpers_imported': False, 'path_nodes': len(keys), 'original_complete_superset_count': len(targets), 'covered_candidates': len(targets & seen), 'excluded_candidates': len(uncovered), 'maximum_path_length': max_depth, 'exclusion_counts': counts, 'edge_method': 'all eleven coefficients of t*a+digit-parent equal a9*P', 'exclusion_method': 'new rational root bisection and exact Fraction interval embeddings', 'scope': 'path correctness and coverage/exclusions; enumeration completeness reviewed separately', 'exclusions': records}
    ((_J_OUTPUT / 'verification.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='exclusions'},indent=2))


if __name__=='__main__':main()
