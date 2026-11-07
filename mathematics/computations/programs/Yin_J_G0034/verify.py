"""Independent exact event-sweep checker for the quartic two-step certificate.

Imports no author module.  Root enclosures use the explicit nested radical;
phase membership is reconstructed by ordered event ranks, not midpoint tests.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
import json,platform,time

HERE=(_J_PROGRAM / 'verify.py').parent
SOURCE=(_J_ROOT / 'mathematics/computations/programs/Yin_J_G0033/inputs/certificate.json')
ZERO=(F(0),)*4; ONE=(F(1),F(0),F(0),F(0)); X=(F(0),F(1),F(0),F(0))
P=(1,-1,-1,-1,1)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def times(a,c):return tuple(c*x for x in a)
def minus(a,b):return plus(a,times(b,-1))
def product(a,b):
    q=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):q[i+j]+=x*y
    while len(q)>4:
        z=q[-1];k=len(q)-5
        for j,p in enumerate(P):q[k+j]-=z*p
        assert q[-1]==0;q.pop()
    return tuple(q+[F(0)]*(4-len(q)))
def imul(a,b):
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def iadd(a,b):return a[0]+b[0],a[1]+b[1]
def isqrt_interval(a):
    assert a[0]>=0;scale=10**60
    lo=isqrt((a[0]*scale*scale).numerator//(a[0]*scale*scale).denominator)
    hi=isqrt((a[1]*scale*scale).numerator//(a[1]*scale*scale).denominator)+1
    return F(lo,scale),F(hi,scale)
sqrt13=isqrt_interval((F(13),F(13)))
u=tuple((1+x)/2 for x in sqrt13)
disc=iadd(imul(u,u),(F(-4),F(-4)))
root=tuple(x/2 for x in iadd(u,isqrt_interval(disc)))
assert F(172,100)<root[0]<root[1]<F(173,100)
@lru_cache(None)
def enclosure(a):
    v=(F(0),F(0))
    for x in reversed(a):v=iadd(imul(v,root),(x,x))
    return v
@lru_cache(None)
def sgn(a):
    if a==ZERO:return 0
    lo,hi=enclosure(a)
    assert lo>0 or hi<0,('unseparated algebraic value',a)
    return 1 if lo>0 else -1

# Inverse of beta comes from -[P(X)-1]/X.  Inverse of beta-1
# is the quotient [P(X)+1]/(X-1), computed by polynomial division.
inv=tuple(F(-P[j+1]) for j in range(4))
q=[F(p) for p in P];q[0]+=1;quot=[F(0)]*4
for k in range(4,0,-1):
    z=q[k];quot[k-1]=z;q[k]-=z;q[k-1]+=z
assert all(z==0 for z in q)
b=tuple(quot);s=product(X,b)
op=product(product(X,X),b);om=product(product(inv,inv),s)
assert product(X,inv)==ONE and product(minus(X,ONE),b)==ONE
assert product(X,b)==s
gap=root[0]-enclosure(inv)[1]
mbounds=[(enclosure(b)[1]+enclosure(s)[1]+3)/gap,
         (enclosure(op)[1]+enclosure(om)[1]+3)/gap]
mmax=max(v.numerator//v.denominator for v in mbounds)
n_bound=max(enclosure(s)[1],enclosure(om)[1])+2+mmax*enclosure(inv)[1]
nmax=n_bound.numerator//n_bound.denominator
assert nmax<=8 and mmax<=7
assert root[1]+1<3 and enclosure(inv)[1]+1<2
# The independently derived enclosure can be tighter.  Enlarge it to the
# declared certificate box to compare every saved phase subdivision exactly.
box=tuple((n,m) for n in range(-8,9) for m in range(-7,8))

def axis_events(axis):
    top=times(ONE,3 if axis==0 else 2)
    caps=(b,op) if axis==0 else (s,om)
    direction=X if axis==0 else inv
    events={ZERO,top};ranges=[]
    for cap in caps:
        entries=[]
        for n,m in box:
            shift=plus(times(ONE,n),times(direction,m))
            lo=minus(times(cap,-1),shift);hi=minus(cap,shift)
            assert sgn(minus(hi,lo))>0
            entries.append((lo,hi))
            for point in (lo,hi):
                if sgn(point)>0 and sgn(minus(point,top))<0:events.add(point)
        ranges.append(entries)
    # Interval midvalues only propose an ordering; every adjacent gap is then
    # proved strictly positive with fresh exact rational enclosures.
    ordered=tuple(sorted(events,key=lambda a:sum(enclosure(a))/2))
    assert ordered[0]==ZERO and ordered[-1]==top
    assert all(sgn(minus(y,x))>0 for x,y in zip(ordered,ordered[1:]))
    ranks={p:i for i,p in enumerate(ordered)};last=len(ordered)-1
    def rank(p):
        if sgn(p)<0:return -1
        if sgn(minus(p,top))>0:return last+1
        return ranks[p]
    ranks_by_kind=[[(rank(lo),rank(hi)) for lo,hi in entries] for entries in ranges]
    interiors=[];vertices=[]
    for i in range(last):
        interiors.append(tuple(frozenset(j for j,(lo,hi) in enumerate(entries) if lo<=i<hi) for entries in ranks_by_kind))
    for i in range(last+1):
        vertices.append(tuple(frozenset(j for j,(lo,hi) in enumerate(entries) if lo<i<hi) for entries in ranks_by_kind))
    # Both adjacent interior masks are now available, including right neighbors.
    checks=0
    for i,vertex in enumerate(vertices):
        for neighbor in (i-1,i):
            if 0<=neighbor<last:
                for kind in (0,1):assert vertex[kind]<=interiors[neighbor][kind];checks+=1
    faces=[]
    for i in range(last):faces.extend(((vertices[i],i,'vertex'),(interiors[i],i,'interval')))
    faces.append((vertices[-1],last-1,'vertex'))
    return ordered,interiors,vertices,faces,checks

def sets(x,y):return sorted(x[1]&y[1]),sorted(x[0]&y[0])
def matrix(x,y):
    rows,cols=sets(x,y)
    vals=[]
    for ri in rows:
        row=[]
        for ci in cols:
            dn=box[ci][0]-box[ri][0];dm=box[ci][1]-box[ri][1]
            row.append((2-abs(dn))*(2-abs(dm)) if abs(dn)<=1 and abs(dm)<=1 else 0)
        if any(row):vals.append(row)
    if not vals:return ()
    keep=[j for j in range(len(cols)) if any(row[j] for row in vals)]
    return tuple(tuple(row[j] for j in keep) for row in vals)

started=time.perf_counter()
xe,xi,xv,xf,xc=axis_events(0);ye,yi,yv,yf,yc=axis_events(1)
patterns={matrix(x,y) for x in xi for y in yi}
faces=0;lower_faces=0
for x,ix,xtype in xf:
    for y,iy,ytype in yf:
        rows,cols=sets(x,y);bigrows,bigcols=sets(xi[ix],yi[iy])
        assert set(rows)<=set(bigrows) and set(cols)<=set(bigcols)
        faces+=1;lower_faces+=int(xtype=='vertex' or ytype=='vertex')

saved=json.loads(SOURCE.read_text(encoding='utf-8'))
assert saved['q']==97
pass
assert saved['coordinate_box']==[-8,8,-7,7]
assert saved['axis_intervals']==[len(xi),len(yi)]
assert saved['distinct_patterns']==len(patterns)
assert len(xi)*len(yi)<=saved['pattern_cap']==50000
seen=set();vector_checks=0;max_rows=max_cols=0;min_slack=None
for case in saved['certificates']:
    a=tuple(tuple(row) for row in case['matrix'])
    assert a and a not in seen and a in patterns
    assert all(len(row)==len(a[0]) for row in a)
    assert all(type(z) is int and z in (0,1,2,4) for row in a for z in row)
    seen.add(a);v=case['positive_vector']
    assert len(v)==len(a) and all(type(z) is int and z>0 for z in v)
    # A(A^T v) avoids the author's explicitly formed row Gram matrix.
    atv=[sum(a[i][j]*v[i] for i in range(len(a))) for j in range(len(a[0]))]
    aatv=[sum(a[i][j]*atv[j] for j in range(len(atv))) for i in range(len(a))]
    assert all(lhs<=97*rhs for lhs,rhs in zip(aatv,v))
    slack=min(97*rhs-lhs for lhs,rhs in zip(aatv,v))
    min_slack=slack if min_slack is None else min(slack,min_slack)
    vector_checks+=len(v);max_rows=max(max_rows,len(a));max_cols=max(max_cols,len(a[0]))
assert seen==patterns-{()}
assert saved['nonempty_patterns']==len(seen)==len(saved['certificates'])
assert min_slack==999999951

# Check the new actual algebraic lower witness, including the full block and
# both exact Rayleigh integers, without constructing the author's Gram matrix.
lower=saved['actual_lower_witness']
r=tuple(F(z) for z in lower['representative'])
assert r==tuple(map(F,(-413,774,0,-180)))
rs=ZERO
for z in reversed(r):rs=plus(product(rs,inv),times(ONE,z))
assert sgn(r)>=0 and sgn(minus(times(ONE,3),r))>=0
assert sgn(rs)>=0 and sgn(minus(times(ONE,2),rs))>=0
def phase_mask(phase,events,interior,vertex):
    for i,event in enumerate(events):
        if phase==event:return vertex[i],('vertex',i)
    for i,(left,right) in enumerate(zip(events,events[1:])):
        if sgn(minus(phase,left))>0 and sgn(minus(right,phase))>0:
            return interior[i],('interval',i)
    raise AssertionError('actual phase is not covered')
rx,rloc=phase_mask(r,xe,xi,xv);ry,sloc=phase_mask(rs,ye,yi,yv)
actual=matrix(rx,ry)
assert actual==tuple(tuple(row) for row in lower['matrix'])
h=lower['vector']
assert len(h)==len(actual) and all(type(z) is int for z in h)
mth=[sum(actual[i][j]*h[i] for i in range(len(actual))) for j in range(len(actual[0]))]
numerator=sum(z*z for z in mth);denominator=sum(z*z for z in h)
assert numerator==9633565984214612 and denominator==100000003825002
assert lower['gram_lower']==96 and denominator>0 and numerator>96*denominator
# sqrt(97)/16 < lambda_3^2 is equivalent to 29<48sqrt(2).
assert 29**2<48**2*2
out={'status': 'passed', 'root_method': 'nested radical with rational sqrt enclosures at10^60', 'root_interval': [str(z) for z in root], 'coordinate_m_bounds': [str(z) for z in mbounds], 'coordinate_n_bound': str(n_bound), 'independently_derived_box': [-nmax, nmax, -mmax, mmax], 'checked_certificate_box': [-8, 8, -7, 7], 'axis_intervals': [len(xi), len(yi)], 'interior_phase_cells': len(xi) * len(yi), 'all_phase_faces_including_boundaries': faces, 'lower_dimensional_faces': lower_faces, 'axis_boundary_subset_checks': xc + yc, 'exact_distinct_matrices': len(patterns), 'certificate_set_equal': True, 'positive_integer_vectors': len(seen), 'positive_vector_coordinate_checks': vector_checks, 'minimum_integer_slack': min_slack, 'maximum_matrix_shape': [max_rows, max_cols], 'q': 97, 'actual_lower_representative': [int(z) for z in r], 'actual_lower_phase_cells': [rloc, sloc], 'lower_rayleigh_numerator': numerator, 'lower_rayleigh_denominator': denominator, 'strict_two_step_improvement_verified': True, 'imports_author_code': False, 'scope': 'all phase enclosure and every retained rational matrix certificate; source proof review separate'}
((_J_OUTPUT / 'verification.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('root_interval','coordinate_m_bounds','coordinate_n_bound')},indent=2))
