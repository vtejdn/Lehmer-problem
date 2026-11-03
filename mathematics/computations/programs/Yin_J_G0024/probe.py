"""Discover normalized joint displacement bodies, retaining integer words."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse,sys,json,time


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--scipy-path')
    p.add_argument('--length',type=int,default=11)
    p.add_argument('--cells',default='50:75,75:100')
    p.add_argument('--grid',type=int,default=100)
    p.add_argument('--output',default='pilot.json')
    args=p.parse_args()
    if args.scipy_path:
        sys.path.insert(0,args.scipy_path)
    import numpy as np
    from scipy.optimize import linprog
    start=time.monotonic()
    roots=np.roots([1,1,0,-1,-1,-1,-1,-1,0,1,1])
    beta=max(r.real for r in roots if abs(r.imag)<1e-8)
    zs=np.array(sorted([r for r in roots if r.imag>1e-8],key=lambda r:r.real))
    cells=[tuple(map(int,s.split(':'))) for s in args.cells.split(',')]
    candidates={c:[] for c in cells};identities={c:[] for c in cells}
    q=np.zeros(1);c=np.zeros((1,4),dtype=complex)
    for k in range(1,args.length+1):
        q=np.repeat(q,3)*beta+np.tile([-1,0,1],len(q))
        c=np.repeat(c,3,axis=0)+np.tile(np.array([-1,0,1])[:,None]*zs[None,:]**(-k),(len(c),1))
        v=np.column_stack((c.real,c.imag));norm2=np.sum(v*v,axis=1)
        for cell in cells:
            lo=beta**k*cell[0]/args.grid+q
            hi=beta**k*cell[1]/args.grid+q
            ix=np.flatnonzero((lo>-1+1e-7)&(hi<1-1e-7)&(norm2>1e-7))
            candidates[cell].append(v[ix]/norm2[ix,None])
            identities[cell].extend((k,int(i)) for i in ix)
    def word(k,index):
        out=[]
        for _ in range(k):out.append(index%3-1);index//=3
        return out[::-1]
    out={'grid':args.grid,'max_length':args.length,'normalization':'joint c / ||c||^2',
         'scope':'numerical discovery only','cells':[]}
    for cell in cells:
        V=np.concatenate(candidates[cell]);n=len(V)
        axes=[];success=True
        A=np.vstack((V.T,np.ones(n)))
        for coordinate in range(8):
            for sign in (-1,1):
                direction=np.zeros(9);direction[coordinate]=sign
                result=linprog(np.r_[np.zeros(n),-1.],A_eq=np.column_stack((A,-direction)),
                               b_eq=[0]*8+[1],bounds=(0,None),method='highs')
                if not result.success:success=False;break
                axes.append((coordinate,sign,float(result.x[-1])))
            if not success:break
        row={'cell':cell,'candidate_count':n,'all_radial_lps_feasible':success,'radial_optima':axes}
        if success:
            target=int(min(v[2] for v in axes)*900)/1000
            row['target_numerator']=round(target*1000);row['target_denominator']=1000
            row['crosspolytope_sufficient_radius']=8**.5/(2*target) if target>0 else None
            certificates=[]
            for coordinate,sign,_ in axes:
                rhs=np.zeros(9);rhs[coordinate]=sign*target;rhs[-1]=1
                result=linprog(np.zeros(n),A_eq=A,b_eq=rhs,bounds=(0,None),method='highs')
                assert result.success
                selected=np.flatnonzero(result.x>1e-8)
                certificates.append({'coordinate':coordinate,'sign':sign,
                                     'digits':[word(*identities[cell][i]) for i in selected],
                                     'weights':result.x[selected].tolist(),
                                     'support_size':len(selected)})
            row['certificates']=certificates
        out['cells'].append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ('radial_optima','certificates')}),flush=True)
    pass
    (_J_OUTPUT/args.output).write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
