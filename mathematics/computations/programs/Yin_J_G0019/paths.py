"""Discover exact backward paths inside a numerically selected finite region.

Floating embedding bounds only guide discovery. Saved paths are integer objects;
their validity and coverage of compact.json are checked separately.
"""
import argparse, json, math, cmath
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import deque

base= _J_OUTPUT


def predecessor(a,d):
    b=a[0]-d
    return (b+a[1],b+a[2],b+a[3],-b)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--radius',type=float,default=12)
    parser.add_argument('--cap',type=int,default=1000000)
    args=parser.parse_args()
    data=json.loads((_J_PROGRAM/'inputs/compact.json').read_text())
    targets={tuple(a) for a in data['states']}
    u=(1+math.sqrt(13))/2
    beta=(u+math.sqrt(u*u-4))/2
    z=cmath.rect(1,math.acos((1-math.sqrt(13))/4))
    bp=[beta**i for i in range(4)]
    rp=[beta**(-i) for i in range(4)]
    zp=[z**i for i in range(4)]
    S=beta/(beta-1);B=1/(beta-1)
    def retain(a):
        return (abs(sum(x*y for x,y in zip(a,bp)))<=B+1e-9 and
                abs(sum(x*y for x,y in zip(a,rp)))<=S+1e-9 and
                abs(sum(x*y for x,y in zip(a,zp)))<=args.radius+1e-9)
    zero=(0,0,0,0)
    parent={zero:None}
    todo=deque([zero])
    remaining=targets-{zero}
    capped=False
    while todo and remaining:
        a=todo.popleft()
        for d in (-1,0,1):
            p=predecessor(a,d)
            if p in parent or not retain(p):continue
            parent[p]=(a,d)
            todo.append(p)
            remaining.discard(p)
            if len(parent)>=args.cap:
                capped=True
                break
        if capped:break
    witnesses=[]
    for state in sorted(targets-remaining):
        a=state;digits=[]
        while a!=zero:
            a,d=parent[a]
            digits.append(d)
        witnesses.append({'state':state,'digits':digits})
    out={'discovery_radius':args.radius,'discovery_node_cap':args.cap,
         'visited':len(parent),'capped':capped,'covered':len(witnesses),
         'uncovered':sorted(remaining),'max_length':max(len(r['digits']) for r in witnesses),
         'scope':'finite integer witnesses only; numerical search boundaries are not proof premises',
         'witnesses':witnesses}
    (base/'paths.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))


if __name__=='__main__':main()
