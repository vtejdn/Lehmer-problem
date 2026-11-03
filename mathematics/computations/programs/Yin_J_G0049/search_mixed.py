"""Second pre-capped test, with genuine norm-preserving two-root replacements."""
import json, math, random, time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import search as S

CONFIG=dict(S.CONFIG,seed=20261011, move_probabilities={'two_root':.6,'reflect':.3,'swap':.1})
def two_root(g,q,i,j,k,c,d):
    # Coefficient of old r_i is one: unimodularity is automatic.
    condition=c*g[i][j]+d*g[i][k]+c*c+d*d+c*d*g[j][k]
    if condition: return None
    ng=[r[:] for r in g]; nq=[r[:] for r in q]
    for l in range(S.N):
        nq[l][i]=q[l][i]+c*q[l][j]+d*q[l][k]
        if l!=i: ng[i][l]=ng[l][i]=g[i][l]+c*g[j][l]+d*g[k][l]
    ng[i][i]=2
    return ng,nq
def seed():
    g=[r[:] for r in S.GSEED]; q=[r[:] for r in S.Q0]
    g,q=two_root(g,q,0,1,3,-1,1)
    g,q=two_root(g,q,5,3,1,-1,1)
    assert S.gram(q)==g
    return g,q
def main():
    rng=random.Random(CONFIG['seed']); start=time.time()
    gseed,qseed=seed(); best=None; improvements=[]; seen=set()
    counts={k:0 for k in ['proposed','norm_rejected','gram_rejected','basis_rejected',
                          'evaluated','accepted','target_hits']}
    for restart in range(CONFIG['restarts']):
        perm=list(range(S.N)); rng.shuffle(perm)
        g=[[gseed[a][b] for b in perm] for a in perm]
        q=[[r[b] for b in perm] for r in qseed]
        poly=S.coefficients(g); score=S.quality(poly)
        for step in range(CONFIG['proposals_per_restart']):
            counts['proposed']+=1; choice=rng.random()
            i,j,k=rng.sample(range(S.N),3)
            if choice<.6:
                proposal=two_root(g,q,i,j,k,rng.choice([-1,1]),rng.choice([-1,1]))
                if proposal is None: counts['norm_rejected']+=1; continue
                ng,nq=proposal
            else: ng,nq=S.move(g,q,'reflect' if choice<.9 else 'swap',i,j)
            if max(abs(v) for r in ng for v in r)>CONFIG['gram_height_cap'] or S.energy(ng)>CONFIG['energy_cap']:
                counts['gram_rejected']+=1; continue
            if max(abs(v) for r in nq for v in r)>CONFIG['basis_coordinate_cap']:
                counts['basis_rejected']+=1; continue
            counts['evaluated']+=1; np=S.coefficients(ng); ns=S.quality(np)
            seen.add(tuple(np)); key=(ns,S.energy(ng),max(abs(v) for r in ng for v in r))
            if best is None or key<tuple(best['key']):
                best={'key':list(key),'proposal':counts['proposed'],'restart':restart,
                      'poly':np,'gram':ng,'basis':nq}
                improvements.append({k:best[k] for k in ['key','proposal','restart','poly']})
            if ns==0: counts['target_hits']+=1; break
            temperature=1+5*(1-step/CONFIG['proposals_per_restart'])
            if ns<=score or rng.random()<math.exp((score-ns)/temperature):
                g,q,poly,score=ng,nq,np,ns; counts['accepted']+=1
        if counts['target_hits']: break
    assert best is not None and S.gram(best['basis'])==best['gram']
    result={'config': CONFIG, 'counts': counts, 'different_polynomials': len(seen), 'best': best, 'improvements': improvements, 'seed_gram': gseed, 'seed_basis': qseed, 'seed_polynomial': S.coefficients(gseed)}
    (_J_OUTPUT / 'mixed_result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['counts','different_polynomials','best']},indent=2))
if __name__=='__main__': main()
