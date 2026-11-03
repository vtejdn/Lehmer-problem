"""Declared complete two-column short-root test, exact arithmetic only."""
from itertools import product, combinations
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import Counter
import json, time
G=[[2,1,1,1,1,1],[1,2,1,-1,-1,1],[1,1,2,1,-1,-1],[1,-1,1,2,1,-1],[1,-1,-1,1,2,1],[1,1,-1,-1,1,2]]
Q0=[[int(i==j)-int(j==i+1) for j in range(6)] for i in range(6)]
TARGET=[1,-2,1,-1,1,-2,1]
def dot(r,s): return sum(r[i]*G[i][j]*s[j] for i in range(6) for j in range(6))
def gram(cols): return [[dot(r,s) for s in cols] for r in cols]
def upper(h): return [[int(i==j)+(h[i][j] if i<j else 0) for j in range(6)] for i in range(6)]
def pf(h, ids=tuple(range(6))):
    if not ids: return 1
    i=ids[0]
    return sum((-1)**(k+1)*h[i][j]*pf(h,ids[1:k]+ids[k+1:]) for k,j in enumerate(ids[1:],1))
def first(v):
    z=[[int(i==j) for j in range(6)] for i in range(6)]
    for i in range(5,-1,-1):
        for j in range(i+1,6): z[i][j]=-sum(v[i][k]*z[k][j] for k in range(i+1,j+1))
    return 6+sum(z[i][j]*v[i][j] for i in range(6) for j in range(i+1,6))
def run():
    start=time.perf_counter()
    roots=[list(r) for r in product((-1,0,1),repeat=6) if dot(r,r)==2]
    assert len(roots)==114
    coords=[[sum(r[k:]) for k in range(6)] for r in roots]
    old=[list(v) for v in zip(*Q0)]
    # Precompute all root products and products against unchanged columns.
    rr=[[dot(r,s) for s in roots] for r in roots]
    ro=[[dot(r,s) for s in old] for r in roots]
    base=gram(old); totals=Counter(); table=[]; hits=[]; pf_hist=Counter()
    for i,j in combinations(range(6),2):
        count=Counter()
        for ir,r in enumerate(roots):
            c=coords[ir]
            for is_,s in enumerate(roots):
                d=coords[is_]; count['pairs']+=1
                minor=c[i]*d[j]-c[j]*d[i]
                if abs(minor)!=1: continue
                count['unimodular']+=1
                if r==old[i] or r==[-x for x in old[i]] or s==old[j] or s==[-x for x in old[j]]:
                    count['old_single_column_controls']+=1; continue
                count['genuine_two_column']+=1
                h=[row[:] for row in base]
                for k in range(6):
                    if k not in (i,j):
                        h[i][k]=h[k][i]=ro[ir][k]; h[j][k]=h[k][j]=ro[is_][k]
                h[i][j]=h[j][i]=rr[ir][is_]
                f=pf(h); pf_hist[str(f)]+=1
                if abs(f)!=3: continue
                count['target_pfaffian']+=1
                v=upper(h); a=first(v)
                if a!=-2: continue
                count['target_hits']+=1
                cols=[q[:] for q in old]; cols[i]=r; cols[j]=s
                hits.append(dict(positions=[i,j],root_indices=[ir,is_],roots=[r,s],coordinates=[c,d],minor=minor,basis=[list(row) for row in zip(*cols)],gram=h,matrix=v,first_coefficient=a,pfaffian=f,energy=sum(v[k][l]**2 for k in range(6) for l in range(k+1,6))))
        totals.update(count); table.append(dict(positions=[i,j],counts=dict(count)))
    assert totals['pairs']==194940
    return dict(scope=dict(root_box=[-1, 1], rank=6, position_pairs=15, ordered_root_pairs=True, pair_cap=194940), roots=roots, counts=dict(totals), position_counts=table, pfaffian_histogram=dict(sorted(pf_hist.items(), key=lambda z: int(z[0]))), hits=hits)
if __name__=='__main__':
    out=run(); (_J_OUTPUT / 'search_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(dict(counts=out['counts'], hits=len(out['hits']))))
