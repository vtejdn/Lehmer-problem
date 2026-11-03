"""Separate complete verification of the two declared J68 controls only."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from functools import reduce
from itertools import product
import json,math,time,sys
HERE=(_J_PROGRAM / 'review_independent.py').parent
CAP=120
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return trim(c)
def det(a):
    a=[r[:] for r in a];n=len(a);sign=1;old=1
    if not n:return 1
    for k in range(n-1):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:return 0
        if p!=k:a[p],a[k]=a[k],a[p];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%old==0
                a[i][j]=z//old
            a[i][k]=0
        old=pivot
    return sign*a[-1][-1]
def resultant(a,b):
    m,n=len(a)-1,len(b)-1
    aa=list(reversed(a));bb=list(reversed(b))
    rows=[]
    for i in range(n):rows.append([0]*i+aa+[0]*(n-i-1))
    for i in range(m):rows.append([0]*i+bb+[0]*(m-i-1))
    return det(rows)
def value(a,x):
    r=F(0)
    for c in reversed(a):r=r*x+c
    return r
def fmt(a,var):
    out=[]
    for i in range(len(a)-1,-1,-1):
        c=a[i]
        if not c:continue
        mon='' if i==0 else var if i==1 else var+'**'+str(i)
        term=str(abs(c)) if not mon else ('' if abs(c)==1 else str(abs(c))+'*')+mon
        if not out:out.append(('-' if c<0 else '')+term)
        else:out.append((' - ' if c<0 else ' + ')+term)
    return ''.join(out) or '0'
def round_one(v,H,S):
    # Locate the exact nearest-integer interval by squared half-integer thresholds.
    a=abs(v)*H
    lo,hi=0,H+1
    while lo+1<hi:
        k=(lo+hi)//2
        if 4*a*a>=S*(2*k-1)**2:lo=k
        else:hi=k
    k=lo
    assert k==0 or S*(2*k-1)**2<=4*a*a
    assert 4*a*a<S*(2*k+1)**2
    return k if v>=0 else -k
def run():
    start=time.perf_counter()
    native=[(_J_PROGRAM / 'readme.md'),(_J_PROGRAM / 'rounding.py'),(_J_OUTPUT / 'rounding.json')]
    snapshots={p:p.read_bytes() for p in native}
    a=json.loads(snapshots[(_J_OUTPUT / 'rounding.json')])
    assert [r['H'] for r in a['rows']]==[45,179]
    old=[196,-235,458,-1024,-384];S=sum(c*c for c in old)
    P=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
    Q=[3,4,-5,-5,1,1]
    # Direct Laurent expansion verifies the full retained trace conversion.
    power={0:1};la={}
    for q in Q:
        for e,c in power.items():la[e+5]=la.get(e+5,0)+q*c
        new={}
        for e,c in power.items():
            for f in [-1,1]:new[e+f]=new.get(e+f,0)+c
        power=new
    assert all(la.get(i,0)==c for i,c in enumerate(P))
    assert all(v==0 for i,v in la.items() if i<0 or i>10)
    assert value(P,F(1))*value(P,F(-1))==-1
    U=[[1],[0,1]]
    for j in range(2,5):U.append(add([0]+U[-1],[-x for x in U[-2]]))
    records=[]
    for row in a['rows']:
        H=row['H']
        raw=[round_one(v,H,S) for v in old]
        if not raw[-1]:raw[-1]=1 if old[-1]>=0 else -1
        g=reduce(math.gcd,raw);c=[v//g for v in raw]
        assert raw==row['raw_rounding'] and g==row['gcd_removed'] and c==row['primitive_c']
        assert reduce(math.gcd,c)==1 and max(map(abs,c))==row['height']
        V=[0]
        for b,u in zip(c,U):V=add(V,[b*v for v in u])
        C=[0]*11
        for j,b in enumerate(c):C[6+j]+=b;C[4-j]-=b
        assert fmt(V,'x')==row['V'] and fmt(C,'t')==row['C']
        assert len(trim(C[:]))-1==row['actual_degree']==10
        assert reduce(math.gcd,C)==row['content']==1
        assert abs(C[-1])==row['leading_abs'] and C[0]==-C[-1]
        norm=resultant(Q,V);res=resultant(P,C)
        assert norm==row['trace_norm'] and res==row['original_resultant']==-norm*norm
        E=sum(v*v for v in C);assert E==row['energy']==2*sum(v*v for v in c)
        ratio=F(abs(res),E**5);assert ratio==F(row['exp_10B'])
        beta_hi=F(1434031,1219123)
        assert ratio>F(343,320)*beta_hi**10>beta_hi**10
        assert row['certified_B_above_m'] is True
        assert row['certified_exp_10B_over_beta_10_exceeds_343_over_320'] is True
        rho=F(sum(map(abs,C))**2,E)
        assert rho==F(row['rho'])<=10
        assert F(sum(i*v*v for i,v in enumerate(C)),E)==5
        assert abs(math.log(float(ratio))/10-row['B_discovery'])<1e-14
        intervals=[]
        for endpoints,multiplicity in row['trace_intervals']:
            l,r=map(F,endpoints)
            assert l<r and r-l<=F(1,10**10) and multiplicity==1
            vl,vr=value(V,l),value(V,r)
            assert vl*vr<0
            intervals.append((l,r))
        assert len(intervals)==4
        assert all(intervals[i][1]<intervals[i+1][0] for i in range(3))
        assert F(-7,2)<intervals[0][0]<intervals[0][1]<F(-17,5)
        assert all(-2<l<r<2 for l,r in intervals[1:])
        assert row['aux_roots_inside_trace_interval']==3
        # Four disjoint sign-changing intervals exhaust degree four with simple roots.
        lead=abs(C[-1])
        cost=[F(3*lead),F(13*lead,4)]
        assert cost==list(map(F,row['complete_aux_M_strict_interval']))
        assert F(3)+F(1,3)<F(17,5) and F(13,4)+F(4,13)>F(7,2)
        records.append(dict(H=H,primitive_c=c,V_coefficients=V,C_coefficients=C,
            trace_norm=norm,full_original_resultant=res,energy=E,
            exact_margin_passed=True,all_four_intervals_sign_certified=True,
            complete_M_strict_interval=list(map(str,cost)),
            all_native_mathematical_fields_checked=True))
    for p,data in snapshots.items():assert p.read_bytes()==data
    elapsed=time.perf_counter()-start;assert elapsed<CAP
    return dict(status='passed', scope='Exactly both declared grids of the one retained actual Lehmer input', method='standard-library squared-threshold rounding; Sylvester/Bareiss full resultants; four exact sign-changing root intervals', author_imports=False, third_party_imports=False, rows=records)
if __name__=='__main__':
    result=run()
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

