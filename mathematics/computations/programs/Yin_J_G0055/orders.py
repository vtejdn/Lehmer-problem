"""Predeclared changed-order extension, at most922740 exact tests."""
from itertools import combinations, permutations
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import Counter
import json, time
from search import Q0, gram, upper, first, pf

def normalize(r):
    return tuple(r) if next(x for x in r if x)!=-1 else tuple(-x for x in r)
def run(target_pf=3,target_a=-2):
    start=time.perf_counter(); initial=json.loads((_J_OUTPUT / 'search_result.json').read_text(encoding='utf-8'))
    roots=initial['roots']; coords=[[sum(r[k:]) for k in range(6)] for r in roots]
    old=[list(v) for v in zip(*Q0)]; bases=set(); genuine=0
    for i,j in combinations(range(6),2):
        for ir,r in enumerate(roots):
            c=coords[ir]
            for iz,z in enumerate(roots):
                d=coords[iz]
                if abs(c[i]*d[j]-c[j]*d[i])!=1: continue
                if r==old[i] or r==[-x for x in old[i]] or z==old[j] or z==[-x for x in old[j]]:continue
                genuine+=1;cols=[q[:] for q in old];cols[i]=r;cols[j]=z
                key=tuple(sorted(normalize(q) for q in cols));assert len(set(key))==6;bases.add(key)
    assert genuine==initial['counts']['genuine_two_column']==61516
    assert len(bases)<=15379
    orders=[(0,)+p for p in permutations(range(1,6)) if p[0]<p[-1]]; assert len(orders)==60
    counts=Counter(); hits=[]; spectra=Counter(); energies=Counter(); max_height=0
    for bi,cols in enumerate(sorted(bases)):
        h=gram(cols)
        energy=sum(h[i][j]**2 for i in range(6) for j in range(i+1,6)); energies[str(energy)]+=1
        max_height=max(max_height,max(abs(h[i][j]) for i in range(6) for j in range(i+1,6)))
        for order in orders:
            counts['orders']+=1
            ho=[[h[i][j] for j in order] for i in order]
            f=pf(ho)
            if abs(f)!=target_pf:continue
            counts['target_pfaffian']+=1
            v=upper(ho);a=first(v);spectra[str(a)]+=1
            if a!=target_a:continue
            counts['target_hits']+=1
            vo=upper([[ho[i][j] if i==j else -abs(ho[i][j]) for j in range(6)] for i in range(6)])
            ordered=[cols[i] for i in order]
            hits.append(dict(basis_index=bi,order=list(order),basis=[list(row) for row in zip(*ordered)],gram=ho,matrix=v,absolute_matrix=vo,pfaffian=f,first_coefficient=a,companion_first_coefficient=first(vo),energy=sum(v[i][j]**2 for i in range(6) for j in range(i+1,6))))
    assert counts['orders']==len(bases)*60<=922740
    return dict(scope=dict(parent_pairs=194940, base_cap=15379, orders_per_basis=60, order_cap=922740, target_pfaffian_abs=target_pf, target_first_coefficient=target_a), genuine_pairs=genuine, distinct_unordered_signed_bases=len(bases), counts=dict(counts), energy_histogram=dict(sorted(energies.items(), key=lambda z: int(z[0]))), max_entry_height=max_height, coefficient_histogram_given_target_pf=dict(sorted(spectra.items(), key=lambda z: int(z[0]))), hits=hits)
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'orders_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ('hits','coefficient_histogram_given_target_pf')}))
