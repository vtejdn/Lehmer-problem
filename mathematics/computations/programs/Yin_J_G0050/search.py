"""Predeclared bounded determinant-preserving cost discovery, floats only rank proposals."""
import json, math, random, time
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import numpy as np

HERE=(_J_PROGRAM / 'search.py').parent
N=7
CONFIG={'seed':20261012,'blocks':30,'proposals_per_block':2000,'total_proposal_cap':60000,
        'height_cap':6,'energy_cap':160,'basis_coordinate_cap':1000000,
        'temperature_start':0.8,'temperature_end':0.015,
        'objective':'complete absolute-companion logarithmic Mahler measure'}
V0=[[1,1,-4,1,1,2,1],[0,1,-1,2,2,2,-1],[0,0,1,-1,-1,-4,-2],
    [0,0,0,1,3,3,-2],[0,0,0,0,1,2,-1],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1]]
Q0=[[1,1,-2,1,1,1,0],[-1,0,3,0,1,1,-2],[0,0,0,1,0,0,0],
    [0,-1,0,0,-1,0,1],[1,0,-2,0,0,0,1],[0,1,-3,0,1,0,0],[0,0,1,0,0,0,0]]

def energy(v):return sum(v[i][j]**2 for i in range(N) for j in range(i+1,N))
def height(v):return max(abs(v[i][j]) for i in range(N) for j in range(i+1,N))
def absolute(v):return [[1 if i==j else -abs(v[i][j]) if i<j else 0 for j in range(N)] for i in range(N)]
def poly(v):
    c=[[0]*N for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(N):c[i][j]=-v[j][i]-sum(v[i][k]*c[k][j] for k in range(i+1,N))
    tr=sum(c[i][i] for i in range(N))
    tr2=sum(c[i][j]*c[j][i] for i in range(N) for j in range(N))
    tr3=sum(c[i][j]*c[j][k]*c[k][i] for i in range(N) for j in range(N) for k in range(N))
    assert (tr*tr-tr2)%2==0 and (tr**3-3*tr*tr2+2*tr3)%6==0
    a=-tr;d=(tr*tr-tr2)//2;h=-(tr**3-3*tr*tr2+2*tr3)//6
    return [1,a,d,h,h,d,a,1]
def numerical_measure(p):
    a,d,h=p[1:4]
    roots=np.roots([1,a-1,d-a-2,h-d-a+1])
    answer=0.
    for x in roots:
        z=(complex(x)+np.sqrt(complex(x*x-4)))/2
        # Product of the lifted pair is exactly one; numeric selection only.
        answer+=max(0.,math.log(abs(z)), -math.log(abs(z)))
    return answer
def mutate(v,q,i,forward):
    a=v[i][i+1];w=[r[:] for r in v];b=[r[:] for r in q]
    for j in range(i):
        x,y=v[j][i],v[j][i+1]
        w[j][i],w[j][i+1]=(y,x-a*y) if forward else (y-a*x,x)
    for j in range(i+2,N):
        x,y=v[i][j],v[i+1][j]
        w[i][j],w[i+1][j]=(y,x-a*y) if forward else (y-a*x,x)
    w[i][i+1]=-a
    for j in range(N):
        x,y=q[j][i],q[j][i+1]
        b[j][i],b[j][i+1]=(y,x-a*y) if forward else (y-a*x,x)
    return w,b
def main():
    start=time.time();rng=random.Random(CONFIG['seed'])
    p0=poly(absolute(V0));m0=numerical_measure(p0)
    best={'measure_approx':m0,'energy':energy(V0),'height':height(V0),'matrix':V0,'basis':Q0,
          'absolute_polynomial':p0,'path':[],'proposal':0}
    improvements=[];counts={k:0 for k in ['proposed','matrix_rejected','basis_rejected','evaluated','accepted']}
    seen=set();cache={tuple(p0):m0}
    for block in range(CONFIG['blocks']):
        v=[r[:] for r in best['matrix']];q=[r[:] for r in best['basis']]
        path=best['path'][:];current=best['measure_approx']
        for step in range(CONFIG['proposals_per_block']):
            counts['proposed']+=1;i=rng.randrange(N-1);forward=bool(rng.randrange(2))
            w,b=mutate(v,q,i,forward);e=energy(w);h=height(w)
            if h>CONFIG['height_cap'] or e>CONFIG['energy_cap']:
                counts['matrix_rejected']+=1;continue
            if max(abs(x) for row in b for x in row)>CONFIG['basis_coordinate_cap']:
                counts['basis_rejected']+=1;continue
            counts['evaluated']+=1;p=poly(absolute(w));key=tuple(p);seen.add(key)
            if key not in cache:cache[key]=numerical_measure(p)
            m=cache[key]
            if (m,e,h)<(best['measure_approx'],best['energy'],best['height']):
                best={'measure_approx':m,'energy':e,'height':h,'matrix':w,'basis':b,
                      'absolute_polynomial':p,'path':path+[[i,forward]],'proposal':counts['proposed']}
                improvements.append({k:best[k] for k in ['measure_approx','energy','height','absolute_polynomial','proposal']})
            temp=CONFIG['temperature_end']+(CONFIG['temperature_start']-CONFIG['temperature_end'])*(1-step/CONFIG['proposals_per_block'])
            if m<=current or rng.random()<math.exp((current-m)/temp):
                v,q,current=w,b,m;path.append([i,forward]);counts['accepted']+=1
    assert counts['proposed']==CONFIG['total_proposal_cap']
    assert poly(best['matrix'])==[1,0,-1,-1,-1,-1,0,1]
    out={'config': CONFIG, 'counts': counts, 'different_absolute_polynomials': len(seen), 'start_absolute_polynomial': p0, 'start_measure_approx': m0, 'best': best, 'improvements': improvements}
    ((_J_OUTPUT / 'search_result.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['best','improvements']},indent=2))
    print(json.dumps({k:v for k,v in best.items() if k!='path'},indent=2))
if __name__=='__main__':main()
