"""Search height-one multiples with large integer quotient coefficients.

MILP is a discovery tool only. Every saved witness is rechecked with Python
integers; optimizer claims of optimality are not mathematical certificates.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)


def multiply(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scipy-path', type=str)
    ap.add_argument('--lengths', default='20,40,80')
    ap.add_argument('--cases', default='quartic_1722,mercat_1883,lehmer,golden_ratio')
    ap.add_argument('--seconds', type=float, default=8)
    ap.add_argument('--bound', type=int, default=50)
    ap.add_argument('--output', type=Path, default=(_J_OUTPUT / 'pilot.json'))
    args = ap.parse_args()
    if not args.output.is_absolute():
        args.output = _J_REPOSITORY / args.output
    if args.scipy_path:
        sys.path.insert(0, args.scipy_path)
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    cases = {
        'quartic_1722': [1,-1,-1,-1,1],
        'mercat_1883': [1,-2,1,-2,1],
        'lehmer': [1,1,0,-1,-1,-1,-1,-1,0,1,1],
        'golden_ratio': [-1,-1,1],
    }
    output = {'quotient_bound':args.bound, 'cases': []}
    for name,p in cases.items():
        if name not in args.cases.split(','):
            continue
        for n in map(int,args.lengths.split(',')):
            mat = np.zeros((n+len(p)-1,n))
            for j in range(n):
                mat[j:j+len(p),j] = p
            objective = np.zeros(n)
            objective[n//2] = -1
            result=milp(objective, integrality=np.ones(n),
                bounds=Bounds(-args.bound*np.ones(n),args.bound*np.ones(n)),
                constraints=LinearConstraint(mat,-np.ones(mat.shape[0]),np.ones(mat.shape[0])),
                options={'time_limit':args.seconds,'mip_rel_gap':0})
            row={'name':name,'p_ascending':p,'quotient_length':n,
                 'target_index':n//2,'optimizer_status':int(result.status),
                 'optimizer_message':result.message}
            if result.x is not None:
                q=[int(round(x)) for x in result.x]
                product=multiply(p,q)
                valid=max(map(abs,product))<=1 and max(map(abs,q))<=args.bound
                row.update(q_ascending=q,product_ascending=product,
                    exact_witness_valid=valid,quotient_height=max(map(abs,q)),
                    target_value=q[n//2])
                if not valid:
                    raise RuntimeError('MILP rounded candidate failed exact integer check')
            output['cases'].append(row)
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
            print(name,n,row.get('quotient_height'),result.status,flush=True)
    print(args.output)


if __name__ == '__main__':
    main()
