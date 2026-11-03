"""Bounded integer root-basis search; float annealing chooses proposals only."""
import json, math, random, time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

N=7
CONFIG={'seed':20261010,'restarts':100,'proposals_per_restart':2000,
        'total_proposal_cap':200000,'gram_height_cap':6,'energy_cap':180,
        'basis_coordinate_cap':10000}
G0=[[0]*N for _ in range(N)]; G0[0][0]=2
for a,b in [(1,2),(3,4),(5,6)]: G0[a][b]=G0[b][a]=1
Q0=[[int(i==j or i==0) for j in range(N)] for i in range(N)]
def gram(q):
    return [[sum(q[k][i]*G0[k][l]*q[l][j] for k in range(N) for l in range(N))
             for j in range(N)] for i in range(N)]
GSEED=gram(Q0)
def coefficients(g):
    # C=-V^{-1}V^T by unitriangular back substitution, all integer.
    c=[[0]*N for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(N):
            rhs=-(1 if i==j else g[i][j] if i>j else 0)
            c[i][j]=rhs-sum(g[i][k]*c[k][j] for k in range(i+1,N))
    tr=sum(c[i][i] for i in range(N))
    tr2=sum(c[i][j]*c[j][i] for i in range(N) for j in range(N))
    assert (tr*tr-tr2)%2==0
    a=-tr; d=(tr*tr-tr2)//2; h=-2-a-d
    return [1,a,d,h,h,d,a,1]
def energy(g): return sum(g[i][j]**2 for i in range(N) for j in range(i+1,N))
def quality(poly): return abs(poly[1])+abs(poly[2]+1)+abs(poly[3]+1)
def move(g,q,kind,i,j):
    ng=[r[:] for r in g]; nq=[r[:] for r in q]
    if kind=='reflect':
        k=g[i][j]
        for l in range(N):
            nq[l][i]=q[l][i]-k*q[l][j]
            if l!=i: ng[i][l]=ng[l][i]=g[i][l]-k*g[j][l]
        ng[i][i]=2
    else:
        perm=list(range(N)); perm[i],perm[j]=perm[j],perm[i]
        ng=[[g[a][b] for b in perm] for a in perm]
        nq=[[row[b] for b in perm] for row in q]
    return ng,nq
def main():
    rng=random.Random(CONFIG['seed']); counters={k:0 for k in
        ['proposed','gram_rejected','basis_rejected','evaluated','accepted','target_hits']}
    best=None; improvements=[]; seen=set(); start=time.time()
    for restart in range(CONFIG['restarts']):
        g=[r[:] for r in GSEED]; q=[r[:] for r in Q0]
        perm=list(range(N)); rng.shuffle(perm)
        g=[[g[a][b] for b in perm] for a in perm]
        q=[[r[b] for b in perm] for r in q]
        poly=coefficients(g); score=quality(poly)
        for step in range(CONFIG['proposals_per_restart']):
            counters['proposed']+=1
            i,j=rng.sample(range(N),2)
            kind='reflect' if rng.random()<.8 else 'swap'
            ng,nq=move(g,q,kind,i,j)
            if max(abs(v) for r in ng for v in r)>CONFIG['gram_height_cap'] or energy(ng)>CONFIG['energy_cap']:
                counters['gram_rejected']+=1; continue
            if max(abs(v) for r in nq for v in r)>CONFIG['basis_coordinate_cap']:
                counters['basis_rejected']+=1; continue
            counters['evaluated']+=1
            np=coefficients(ng); ns=quality(np)
            seen.add(tuple(np))
            key=(ns,energy(ng),max(abs(v) for r in ng for v in r))
            if best is None or key<tuple(best['key']):
                best={'key':list(key),'proposal':counters['proposed'],'restart':restart,
                      'poly':np,'gram':ng,'basis':nq}
                improvements.append({k:best[k] for k in ['key','proposal','restart','poly']})
            if ns==0:
                counters['target_hits']+=1
                break
            temperature=1+5*(1-step/CONFIG['proposals_per_restart'])
            if ns<=score or rng.random()<math.exp((score-ns)/temperature):
                g,q,poly,score=ng,nq,np,ns; counters['accepted']+=1
        if counters['target_hits']: break
    assert best is not None and gram(best['basis'])==best['gram']
    result={'config': CONFIG, 'counts': counters, 'different_polynomials': len(seen), 'best': best, 'improvements': improvements, 'seed_gram': GSEED, 'seed_basis': Q0, 'seed_polynomial': coefficients(GSEED)}
    (_J_OUTPUT / 'search_result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['counts','different_polynomials','best']},indent=2))
if __name__=='__main__': main()
