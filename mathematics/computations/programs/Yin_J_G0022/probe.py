"""Numerical full joint-neutral feasibility, retaining actual integer blocks."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse, sys, json, time


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--scipy-path')
    p.add_argument('--length',type=int,default=11)
    p.add_argument('--cells',default='50,75,99')
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
    assert len(zs)==4
    cells=[int(x) for x in args.cells.split(',')]
    lists={j:[] for j in cells}
    ids={j:[] for j in cells}
    q=np.zeros(1)
    c=np.zeros((1,4),dtype=complex)
    for k in range(1,args.length+1):
        q=np.repeat(q,3)*beta+np.tile([-1,0,1],len(q))
        c=np.repeat(c,3,axis=0)+np.tile(np.array([-1,0,1])[:,None]*zs[None,:]**(-k),(len(c),1))
        v=np.column_stack((c.real,c.imag))
        for j in cells:
            low=beta**k*j/args.grid+q
            high=beta**k*(j+1)/args.grid+q
            ix=np.flatnonzero((low>-1+1e-7)&(high<1-1e-7))
            lists[j].append(v[ix])
            ids[j].extend((k,int(i)) for i in ix)
    def word(k,index):
        out=[]
        for _ in range(k):out.append(index%3-1);index//=3
        return out[::-1]
    out={'beta':beta,'upper_unit_roots':[[float(z.real),float(z.imag)] for z in zs],
         'coordinate_order':'Re(z1),Re(z2),Re(z3),Re(z4),Im(z1),Im(z2),Im(z3),Im(z4)',
         'max_length':args.length,'grid':args.grid,'scope':'floating-point discovery only',
         'cells':[]}
    for j in cells:
        V=np.concatenate(lists[j])
        result=linprog(np.zeros(len(V)),A_eq=np.vstack((V.T,np.ones(len(V)))),b_eq=[0]*8+[1],
                       bounds=(0,None),method='highs')
        row={'j':j,'candidate_count':len(V),'success':bool(result.success),'message':result.message}
        if result.success:
            chosen=np.flatnonzero(result.x>1e-8)
            W=V[chosen]
            row['digits']=[word(*ids[j][i]) for i in chosen]
            row['weights']=result.x[chosen].tolist()
            row['joint_displacements']=W.tolist()
            row['support_size']=len(chosen)
            row['barycentric_residual']=float(np.linalg.norm(result.x@V))
            if len(chosen)==9:
                A=np.vstack((W.T,np.ones(9)))
                inv=np.linalg.inv(A)
                lam=inv@np.array([0]*8+[1])
                radius=float(min(lam/np.linalg.norm(inv[:,:8],axis=1)))
                m2=float(max(np.sum(W*W,axis=1)))
                row.update({'affine_condition':float(np.linalg.cond(A)),
                            'simplex_inradius':radius,'max_vertex_norm_squared':m2,
                            'sufficient_neutral_radius':m2/(2*radius) if radius>0 else None})
        out['cells'].append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ('digits','weights','joint_displacements')}),flush=True)
    (_J_OUTPUT/args.output).write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
