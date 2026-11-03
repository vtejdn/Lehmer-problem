"""Discover true digit blocks covering expanding intervals with neutral triangles."""
from __future__ import annotations
import argparse, cmath, itertools, json, math, sys
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)


def cross(a,b):
    return (a.conjugate()*b).imag


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-length',type=int,default=10)
    ap.add_argument('--grid',type=int,default=100)
    ap.add_argument('--scipy-path')
    args=ap.parse_args()
    if args.scipy_path: sys.path.insert(0,args.scipy_path)
    import numpy as np
    from scipy.spatial import ConvexHull
    u=(1+math.sqrt(13))/2
    beta=(u+math.sqrt(u*u-4))/2
    v=(1-math.sqrt(13))/2
    zeta=complex(v/2,math.sqrt(1-v*v/4))
    # tuple: digits, Q(beta), sum digit_i zeta^-i
    rows=[((),0.0,0j)]
    allrows=[]
    for k in range(1,args.max_length+1):
        rows=[(w+(a,),beta*x+a,c+a*zeta**(-k)) for w,x,c in rows for a in (-1,0,1)]
        power=beta**k
        allrows += [(w,x,c,power) for w,x,c in rows
                    if x+power*.5<1 and x+power*1>-1 and abs(c)>1e-10]
    cells=[]
    for j in range(args.grid//2,args.grid):
        lo=j/args.grid; hi=(j+1)/args.grid
        feasible=[row for row in allrows if row[1]+row[3]*lo >-1+1e-9
                  and row[1]+row[3]*hi<1-1e-9]
        points=np.array([[row[2].real,row[2].imag] for row in feasible])
        if len(points)<3:
            cells.append({'j':j,'failure':'fewer than three blocks'});continue
        hull=ConvexHull(points)
        vertices=[feasible[i] for i in hull.vertices]
        best=None
        for triple in itertools.combinations(vertices,3):
            c=[row[2] for row in triple]
            orient=[cross(c[i],c[(i+1)%3]) for i in range(3)]
            if min(orient)<=1e-8: continue
            radius=min(orient[i]/abs(c[(i+1)%3]-c[i]) for i in range(3))
            square=max(abs(z)**2 for z in c)
            threshold=square/(2*radius)
            if best is None or threshold<best[0]: best=(threshold,triple,radius)
        if best is None:
            cells.append({'j':j,'failure':'no strict surrounding hull triangle','feasible':len(feasible)})
        else:
            threshold,triple,radius=best
            cells.append({'j':j,'digits':[list(row[0]) for row in triple],
                'neutral_radius_float':radius,'descent_threshold_float':threshold,
                'feasible_count':len(feasible)})
    out={'beta_float':beta,'zeta_float':[zeta.real,zeta.imag],
         'grid':args.grid,'max_length':args.max_length,'strip_radius':1,
         'annulus':[.5,1],'cells':cells}
    path=(_J_OUTPUT / 'triangles.json')
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    failures=[x for x in cells if 'failure' in x]
    print('cells',len(cells),'failures',len(failures),'largest threshold',max((x.get('descent_threshold_float',0) for x in cells),default=0))
    print(failures)


if __name__=='__main__':main()
