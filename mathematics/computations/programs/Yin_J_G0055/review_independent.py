"""Independent D121/J55 reviewer certificate; no author imports.

Rebuild all roots and bases. Full 6x6 determinants admit the original pairs.
Pfaffians use the alternating-permutation definition collected into 15 terms.
For every target-Pfaffian candidate, two scalar Bareiss determinants and the
complete reciprocal endpoint identity recover the entire polynomial. Cyclic/
reversal representatives are independently formed as orbits of all720 orders.
Author files are only read and observed for within-run no-write protection.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product, combinations, permutations
from collections import Counter, defaultdict
from time import perf_counter
import json

BASE=(_J_PROGRAM / 'review_independent.py').parent
G=((2,1,1,1,1,1),(1,2,1,-1,-1,1),(1,1,2,1,-1,-1),
   (1,-1,1,2,1,-1),(1,-1,-1,1,2,1),(1,1,-1,-1,1,2))
OLD=tuple(tuple(int(i==j)-int(i==j-1) for i in range(6)) for j in range(6))
TARGETS={3:(-2,(1,-2,1,-1,1,-2,1)),1:(0,(1,0,-1,-1,-1,0,1))}

def det(rows):
    a=[list(r) for r in rows];n=len(a);sg=1;old=1
    for k in range(n-1):
        j=next((i for i in range(k,n) if a[i][k]),None)
        if j is None:return 0
        if j!=k:a[j],a[k]=a[k],a[j];sg=-sg
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=pivot*a[i][j]-a[i][k]*a[k][j]
                assert value%old==0
                a[i][j]=value//old
        for i in range(k+1,n):a[i][k]=0
        old=pivot
    return sg*a[-1][-1]

def dot(r,s):return sum(r[i]*G[i][j]*s[j] for i in range(6) for j in range(6))
def gram(cols):return [[dot(r,s) for s in cols] for r in cols]
def upper(h):return [[int(i==j)+(h[i][j] if i<j else 0) for j in range(6)] for i in range(6)]
def abs_upper(h):return [[int(i==j)+(-abs(h[i][j]) if i<j else 0) for j in range(6)] for i in range(6)]
def d_at(v,t):return det([[t*v[i][j]+v[j][i] for j in range(6)] for i in range(6)])

# All720 terms of the exterior definition; swap each pair into ascending order
# and collect. Every perfect matching has coefficient +/-48 before division.
MATCH=defaultdict(int)
for p in permutations(range(6)):
    sg=(-1)**sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))
    pairs=[]
    for i in (0,2,4):
        a,b=p[i:i+2]
        if a>b:a,b=b,a;sg=-sg
        pairs.append((a,b))
    MATCH[tuple(sorted(pairs))]+=sg
assert len(MATCH)==15 and all(abs(v)==48 for v in MATCH.values())
MATCH=tuple((v//48,p) for p,v in MATCH.items())

def pf(h):return sum(sg*h[p[0][0]][p[0][1]]*h[p[1][0]][p[1][1]]*h[p[2][0]][p[2][1]] for sg,p in MATCH)
def full_poly(v,endpoint=None):
    # det V=1, dimension6: exact reciprocity leaves three free coefficients.
    e=d_at(v,1) if endpoint is None else endpoint
    u,w=d_at(v,2),d_at(v,3)
    numerator=w-9*u-235+45*e
    assert numerator%30==0
    a=numerator//30
    numerator=u-49-8*e-18*a
    assert numerator%4==0
    b=numerator//4;c=e-2-2*a-2*b
    out=(1,a,b,c,b,a,1)
    assert sum(out)==e
    return out

def normalized(cols):
    return tuple(sorted(tuple(-v for v in c) if next(v for v in c if v)<0 else tuple(c) for c in cols))
def orbit(p):
    z=[]
    for q in (p,p[::-1]):
        for k in range(6):z.append(q[k:]+q[:k])
    return tuple(sorted(set(z)))

def main():
    start=perf_counter()
    names=['readme.md','search.py','search_result.json','orders.py','orders_result.json','smaller_control.py','smaller_result.json']
    # Additional author verification files, if present at freeze, are included
    # in no-write observation. They are not imported or executed here.
    names+=sorted(p.name for p in (*BASE.iterdir(), *_J_OUTPUT.iterdir()) if p.name not in names and p.suffix in ('.py','.json') and not p.name.startswith('review_'))
    before={name:(((_J_PROGRAM if name in ('orders.py', 'readme.md', 'review_independent.py', 'search.py', 'smaller_control.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in names}
    observed={p:p.read_bytes() for p in ((_J_ROOT / 'mathematics/drafts/Yin_D_G0121.md'),) if p.exists()}
    assert det(G)==-1 and det(list(zip(*OLD)))==1
    roots=tuple(r for r in product((-1,0,1),repeat=6) if dot(r,r)==2)
    assert len(roots)==114
    saved=json.loads(before['search_result.json'])
    assert [list(r) for r in roots]==saved['roots']
    coords={r:tuple(sum(r[k:]) for k in range(6)) for r in roots}
    all_products={(r,s):dot(r,s) for r in roots for s in roots}
    assert all(c in roots for c in OLD)
    totals=Counter();position_counts=[];hist=Counter();bases=set();initial_polys=0
    for i,j in combinations(range(6),2):
        counts=Counter()
        for r,s in product(roots,repeat=2):
            counts['pairs']+=1;cols=list(OLD);cols[i]=r;cols[j]=s
            determinant=det(list(zip(*cols)))
            c,d=coords[r],coords[s]
            assert determinant==c[i]*d[j]-c[j]*d[i]
            if abs(determinant)!=1:continue
            counts['unimodular']+=1
            assert all(dot(v,v)==2 for v in cols)
            if r in (OLD[i],tuple(-v for v in OLD[i])) or s in (OLD[j],tuple(-v for v in OLD[j])):
                counts['old_single_column_controls']+=1;continue
            counts['genuine_two_column']+=1
            key=normalized(cols);assert len(set(key))==6;bases.add(key)
            h=[[all_products[a,b] for b in cols] for a in cols]
            f=pf(h);hist[str(f)]+=1
            if abs(f)!=3:continue
            counts['target_pfaffian']+=1;v=upper(h);poly=full_poly(v,-1);initial_polys+=1
            assert sum(a*(-1)**k for k,a in enumerate(poly))==f*f
            if poly==TARGETS[3][1]:counts['target_hits']+=1
        totals.update(counts);position_counts.append({'positions':[i,j],'counts':dict(counts)})
    assert dict(totals)==saved['counts']
    assert position_counts==saved['position_counts']
    assert dict(hist)==saved['pfaffian_histogram']
    assert saved['hits']==[] and totals['target_hits']==0
    assert saved['scope']==dict(root_box=[-1,1],rank=6,position_pairs=15,ordered_root_pairs=True,pair_cap=194940)
    assert totals['pairs']==194940 and len(bases)==7446
    orders=sorted({min(orbit(p)) for p in permutations(range(6))})
    assert len(orders)==60 and all(len(orbit(p))==12 for p in orders)
    assert all(p[0]==0 and p[1]<p[-1] for p in orders)
    # Build the actual original data for both scalar targets in one complete pass.
    tally={t:Counter() for t in TARGETS};coefs={t:Counter() for t in TARGETS};actual_orders=0;fulls=0
    energies=Counter();max_height=0
    for cols in sorted(bases):
        h=[[all_products[a,b] for b in cols] for a in cols]
        energies[str(sum(h[i][j]**2 for i in range(6) for j in range(i+1,6)))]+=1
        max_height=max(max_height,max(abs(h[i][j]) for i in range(6) for j in range(i+1,6)))
        for order in orders:
            actual_orders+=1;ho=[[h[a][b] for b in order] for a in order]
            f=pf(ho);t=abs(f)
            if t not in TARGETS:continue
            tally[t]['target_pfaffian']+=1
            v=upper(ho);poly=full_poly(v,-1);fulls+=1
            assert sum(a*(-1)**k for k,a in enumerate(poly))==f*f
            coefs[t][str(poly[1])]+=1
            if poly==TARGETS[t][1]:tally[t]['target_hits']+=1
    assert actual_orders==446760
    for t,name in ((3,'orders_result.json'),(1,'smaller_result.json')):
        out=json.loads(before[name])
        current={'orders':actual_orders,**dict(tally[t])}
        assert current==out['counts']
        assert dict(coefs[t])==out['coefficient_histogram_given_target_pf']
        assert dict(energies)==out['energy_histogram'] and max_height==out['max_entry_height']==3
        assert min(map(int,energies))==17 and max(map(int,energies))==69
        assert all(int(a)%4!=(2 if t==3 else 0) for a in coefs[t])
        assert out['genuine_pairs']==totals['genuine_two_column']==61516
        assert out['distinct_unordered_signed_bases']==len(bases)
        assert out['scope']['parent_pairs']==194940
        assert out['scope']['base_cap']==15379
        assert out['scope']['orders_per_basis']==60
        assert out['scope']['order_cap']==922740
        if 'target_pfaffian_abs' in out['scope']:assert out['scope']['target_pfaffian_abs']==t
        if 'target_first_coefficient' in out['scope']:assert out['scope']['target_first_coefficient']==TARGETS[t][0]
        assert out['hits']==[] and tally[t]['target_hits']==0
    # Direct full-poly checks of cyclic AND reversal invariance for signed and
    # absolute forms on a declared deterministic sample of25 bases, all720 orders.
    sorted_bases=sorted(bases)
    indices=sorted(set(list(range(12))+list(range(len(bases)-12,len(bases)))+[len(bases)//2]))
    assert len(indices)==25
    symchecks=0
    for bi in indices:
        cols=sorted_bases[bi];h=[[all_products[a,b] for b in cols] for a in cols]
        for rep in orders:
            values=[]
            for p in orbit(rep):
                hp=[[h[a][b] for b in p] for a in p]
                v=upper(hp);vm=abs_upper(hp)
                pp=full_poly(v,-1);pm=full_poly(vm)
                for mat,poly in ((v,pp),(vm,pm)):
                    assert d_at(mat,4)==sum(a*4**k for k,a in enumerate(poly))
                values.append((pp,pm));symchecks+=1
            assert len(set(values))==1
    assert symchecks==18000
    # Cover every statement and retained sample in the additional author verifier.
    ver=json.loads(before['verification.json'])
    assert ver['passed'] and ver['sample_bases']==3 and len(ver['samples'])==3
    assert ver['full_degree6_polynomial_checks']==4320 and ver['all_orders_per_sample']==720
    assert ver['dihedral_classes_per_sample']==60 and ver['full_degree12_cover_checks']==3
    assert ver['independent_scalar_cover_values']==39 and ver['finite_residue_patterns_verified']
    author_samples=0;cover_values=0
    for sample in ver['samples']:
        cols=tuple(tuple(c) for c in zip(*sample['basis']));label=sample['label']
        assert abs(det(sample['basis']))==1
        if 'kind' in label:assert label=={'kind':'original_path'} and cols==OLD
        else:
            i,j=label['positions'];r,sr=map(tuple,label['roots']);expect=list(OLD);expect[i]=r;expect[j]=sr
            assert tuple(expect)==cols and r in roots and sr in roots
            assert r not in (OLD[i],tuple(-v for v in OLD[i])) and sr not in (OLD[j],tuple(-v for v in OLD[j]))
            assert label['minor']==det(sample['basis'])
        h=gram(cols);assert h==sample['gram'] and det(h)==-1
        assert all(h[i][i]==2 for i in range(6))
        v=upper(h);vm=abs_upper(h);pp=full_poly(v,-1);pm=full_poly(vm)
        assert list(pp)==sample['original_polynomial'] and list(pm)==sample['absolute_polynomial']
        assert sample['energy']==sum(h[i][j]**2 for i in range(6) for j in range(i+1,6))
        convolution=[sum(pp[j]*pm[k-j] for j in range(7) if 0<=k-j<7) for k in range(13)]
        assert convolution==sample['full_cover_polynomial']
        cover=[[int(i==j) for j in range(12)] for i in range(12)]
        for i in range(6):
            for j in range(i+1,6):
                value=v[i][j]
                for sheet in range(2):cover[2*i+sheet][2*j+(sheet if value<=0 else 1-sheet)]=-abs(value)
        assert sum(cover[i][j]**2 for i in range(12) for j in range(i+1,12))==2*sample['energy']
        for t0 in range(-6,7):
            scalar=det([[t0*cover[i][j]+cover[j][i] for j in range(12)] for i in range(12)])
            assert scalar==sum(c*t0**k for k,c in enumerate(convolution));cover_values+=1
        # Full degree12 equality follows from these13 distinct values and the
        # independently verified degree bound, not an imported factor routine.
        orbit_values={}
        for order in permutations(range(6)):
            ho=[[h[i][j] for j in order] for i in order]
            pol=full_poly(upper(ho),-1);polm=full_poly(abs_upper(ho))
            assert sum(a*(-1)**j for j,a in enumerate(pol))==pf(ho)**2
            key=min(orbit(order));value=(pol,polm)
            if key in orbit_values:assert orbit_values[key]==value
            else:orbit_values[key]=value
            author_samples+=2
        assert len(orbit_values)==60
    assert author_samples==4320 and cover_values==39
    assert all((((_J_PROGRAM if n in ('orders.py', 'readme.md', 'review_independent.py', 'search.py', 'smaller_control.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes()==b for n,b in before.items())
    assert all(p.read_bytes()==b for p,b in observed.items())
    result={'passed': True, 'method': 'Full basis Bareiss; alternating-permutation Pfaffian; full reciprocal polynomial from scalar determinants at2,3 and actual symmetric endpoint; no author imports', 'root_cube_vectors': 729, 'norm_two_roots': len(roots), 'full_basis_determinants': totals['pairs'], 'fixed_order_counts': dict(totals), 'fixed_order_full_polynomials': initial_polys, 'distinct_unordered_signed_bases': len(bases), 'complete_order_representatives': 60, 'complete_order_tests': actual_orders, 'two_target_full_polynomials': fulls, 'target_counts': {str(t): dict(tally[t]) for t in TARGETS}, 'complete_histograms_and_per_position_counts_matched': True, 'energy_range': [17, 69], 'maximum_entry_height': max_height, 'additional_author_sample_full_polynomials': author_samples, 'complete_cover_identities': 3, 'independent_cover_values': cover_values, 'symmetry_sample_base_indices': indices, 'symmetry_sample_orders': symchecks, 'symmetry_original_absolute_full_polynomials_checked': 2 * symchecks, 'all_symmetry_polynomials_also_checked_at4': True, 'scope': 'No all-integral nonexistence inferred from the finite root cube; symmetry is additionally proved in written review.'}
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
