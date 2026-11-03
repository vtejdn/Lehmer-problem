"""Declared genuine three-column short-root experiment, exact integers only."""
from itertools import product,combinations
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import Counter
import json,time

G=[[2,1,1,1,1,1],[1,2,1,-1,-1,1],[1,1,2,1,-1,-1],[1,-1,1,2,1,-1],[1,-1,-1,1,2,1],[1,1,-1,-1,1,2]]
Q0=[[int(i==j)-int(j==i+1) for j in range(6)] for i in range(6)]
OLD=list(map(list,zip(*Q0)))
def dot(x,y):return sum(x[i]*G[i][j]*y[j] for i in range(6) for j in range(6))
def canonical(x):
    sign=next(z for z in x if z)
    return tuple(x if sign>0 else [-z for z in x])
def pf(g):
    # The complete15-term expansion, with the first remaining label paired first.
    def f(ids):
        if not ids:return 1
        return sum((-1)**(k+1)*g[ids[0]][j]*f(ids[1:k]+ids[k+1:]) for k,j in enumerate(ids[1:],1))
    return f(tuple(range(6)))
def first(v):
    z=[[int(i==j) for j in range(6)] for i in range(6)]
    for i in range(5,-1,-1):
        for j in range(i+1,6):z[i][j]=-sum(v[i][k]*z[k][j] for k in range(i+1,j+1))
    return 6+sum(z[i][j]*v[i][j] for i in range(6) for j in range(i+1,6))
def run():
    start=time.perf_counter();allroots=[list(r) for r in product((-1,0,1),repeat=6) if dot(r,r)==2];assert len(allroots)==114
    roots=sorted({canonical(r) for r in allroots});assert len(roots)==57
    coords=[[sum(r[k:]) for k in range(6)] for r in roots]
    rr=[[dot(r,s) for s in roots] for r in roots];ro=[[dot(r,s) for s in OLD] for r in roots]
    base=[[dot(r,s) for s in OLD] for r in OLD];oldcanon=[canonical(x) for x in OLD]
    totals=Counter();tables=[];hits=[];escapes=[];energy=Counter();ph=Counter();cohist=Counter();cap=False
    for i,j,k in combinations(range(6),3):
        count=Counter();positions=[i,j,k];fixed=[l for l in range(6) if l not in positions]
        for ir,r in enumerate(roots):
            c=coords[ir]
            for is_,s in enumerate(roots):
                d=coords[is_]
                cof=[c[j]*d[k]-c[k]*d[j],c[k]*d[i]-c[i]*d[k],c[i]*d[j]-c[j]*d[i]]
                for it,u in enumerate(roots):
                    count['triples']+=1;f=coords[it];minor=cof[0]*f[i]+cof[1]*f[j]+cof[2]*f[k]
                    if minor==0:count['singular']+=1;continue
                    if abs(minor)!=1:count['nonunit_nonsingular']+=1;continue
                    count['unit_minor']+=1
                    if r==oldcanon[i] or s==oldcanon[j] or u==oldcanon[k]:count['old_controls']+=1;continue
                    count['genuine']+=1;h=[row[:] for row in base];inds=[ir,is_,it]
                    for a,ia in zip(positions,inds):
                        for b in fixed:h[a][b]=h[b][a]=ro[ia][b]
                    for a,b in combinations(range(3),2):h[positions[a]][positions[b]]=h[positions[b]][positions[a]]=rr[inds[a]][inds[b]]
                    p=pf(h);assert p%2;ph[str(p)]+=1
                    v=[[int(a==b)+(h[a][b] if a<b else 0) for b in range(6)] for a in range(6)]
                    a=first(v);b=(p*p-5)//4;assert (p*p-5)%4==0
                    e=sum(h[x][y]**2 for x in range(6) for y in range(x+1,6));energy[str(e)]+=1
                    cohist[f'{a%4},{b%4}']+=1
                    labels=[]
                    if a==-2 and abs(p)==3:labels.append('F')
                    if a==0 and abs(p)==1:labels.append('S6')
                    escape=a%2==0 and (a+b)%4!=1
                    if escape:count['congruence_escape']+=1
                    if labels or (escape and len(escapes)<20):
                        cols=[x[:] for x in OLD]
                        for pos,root in zip(positions,[r,s,u]):cols[pos]=list(root)
                        record=dict(positions=positions,root_indices=inds,roots=[list(r),list(s),list(u)],minor=minor,basis=list(map(list,zip(*cols))),gram=h,matrix=v,pfaffian=p,original_polynomial=[1,a,b,-3-2*a-2*b,b,a,1],energy=e,height=max(abs(h[x][y]) for x in range(6) for y in range(x+1,6)),target_labels=labels)
                        if labels:hits.append(record);count['target_hits']+=1
                        if escape and len(escapes)<20:escapes.append(record)
                if time.perf_counter()-start>120:cap=True;break
            if cap:break
        totals.update(count);tables.append(dict(positions=positions,counts=dict(count)))
        if cap:break
    complete=not cap
    if complete:assert totals['triples']==3703860
    return dict(complete=complete, scope=dict(root_box=[-1, 1], norm=2, root_sign_representatives=57, position_triples=20, ordered_roots=True, fixed_order=True, declared_triple_cap=3703860), all_roots=allroots, normalized_roots=list(map(list, roots)), counts=dict(totals), position_counts=tables, energy_histogram=dict(sorted(energy.items(), key=lambda x: int(x[0]))), pfaffian_histogram=dict(sorted(ph.items(), key=lambda x: int(x[0]))), coefficient_mod4_histogram=dict(sorted(cohist.items())), target_hits=hits, first20_congruence_escape_controls=escapes)
if __name__=='__main__':
    out=run();name='search_result.json' if out['complete'] else 'search_partial.json';(_J_OUTPUT / name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k in ['complete','scope','counts']}));print(json.dumps(dict(hits=len(out['target_hits']),escapes=len(out['first20_congruence_escape_controls']),coefficient_mod4_histogram=out['coefficient_mod4_histogram'])))
