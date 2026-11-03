"""Finite exact phase cover plus numerical positive-vector discovery."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from time import perf_counter
import json,platform,math
import numpy as np
import core

def main():
    start=perf_counter()
    xp,yp,patterns=core.all_patterns()
    print('phase cells',len(xp)-1,len(yp)-1,'distinct matrices',len(patterns),flush=True)
    cases=[]
    largest=-1.;worst=None
    for a,cell in patterns.items():
        assert perf_counter()-start<60, 'discovery time cap reached'
        if not a:continue
        m=core.gram(a)
        eigen=float(np.linalg.eigvalsh(np.array(m,dtype=float))[-1])
        cases.append((a,m,cell))
        if eigen>largest:largest=eigen;worst=cell
    q=math.ceil(largest)
    certificates=[]
    for a,m,cell in cases:
        assert perf_counter()-start<60, 'discovery time cap reached'
        matrix=np.array(m,dtype=float)
        v=np.linalg.solve(q*np.eye(len(m))-matrix,np.ones(len(m)))
        ints=[int(round(x*10**9)) for x in v]
        assert min(ints)>0
        assert all(sum(x*y for x,y in zip(row,ints))<=q*ints[i] for i,row in enumerate(m))
        certificates.append({'matrix':a,'positive_vector':ints,'example_cell':cell})
    # Construct one actual algebraic representative for a lower-bound block.
    def real(a):return float(sum(core.interval(a))/2)
    beta=real(core.BETA);u=core.add(core.BETA,core.INV)
    target_plus=(real(xp[worst[0]])+real(xp[worst[0]+1]))/2
    target_minus=(real(yp[worst[1]])+real(yp[worst[1]+1]))/2
    target_b=(target_plus-target_minus)/(beta-1/beta)
    target_a=target_plus-beta*target_b
    def approximate(target):
        choices=[]
        for m in range(-500,501):
            n=round(target-m*real(u))
            choices.append((abs(n+m*real(u)-target),n,m))
        _,n,m=min(choices)
        return core.add(core.scale(core.ONE,n),core.scale(u,m))
    r=core.add(approximate(target_a),core.mul(approximate(target_b),core.BETA))
    rs=core.sigma(r)
    assert core.sign(core.sub(r,xp[worst[0]]))>0
    assert core.sign(core.sub(xp[worst[0]+1],r))>0
    assert core.sign(core.sub(rs,yp[worst[1]]))>0
    assert core.sign(core.sub(yp[worst[1]+1],rs))>0
    lower_matrix=core.matrix(core.mask_at(0,r),core.mask_at(1,rs))
    lower_gram=np.array(core.gram(lower_matrix),dtype=float)
    evals,evecs=np.linalg.eigh(lower_gram)
    lower_vector=[int(round(x*10**7)) for x in evecs[:,-1]]
    numerator=sum(x*y*lower_gram[i,j] for i,x in enumerate(lower_vector)
                  for j,y in enumerate(lower_vector))
    assert numerator>96*sum(x*x for x in lower_vector)
    out={'scope': 'quartic full phase rectangle [0,3] x [0,2]', 'pattern_cap': 50000, 'coordinate_box': [-8, 8, -7, 7], 'axis_intervals': [len(xp) - 1, len(yp) - 1], 'distinct_patterns': len(patterns), 'nonempty_patterns': len(cases), 'q': q, 'certificates': certificates, 'actual_lower_witness': {'representative': [int(x) for x in r], 'matrix': lower_matrix, 'vector': lower_vector, 'gram_lower': 96}, 'discovery_only': {'max_gram_eigenvalue': largest, 'worst_cell': worst, 'operator_upper_bound': math.sqrt(q) / 16}}
    p=(_J_OUTPUT / 'certificate.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('certificates','actual_lower_witness')},indent=2),flush=True)

if __name__=='__main__':main()
