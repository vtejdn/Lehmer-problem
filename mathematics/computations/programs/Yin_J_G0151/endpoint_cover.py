"""One fixed box-cover check for the first N=7 triple's nonreal pair.

The four fixed rational dual polynomials are tested on 4096 equal s cells
covering [-6/5,-1/3], the full d interval [-1/10100,0], and the full
retained cut interval. A returned unresolved cell is not an exclusion.
"""

from fractions import Fraction as F
import argparse
import json
from math import comb
from pathlib import Path

from flint import arb,ctx
from endpoint_dual import ball,evaluate,positive_penalty,differences,CUT_LEFT,CUT_RIGHT

CELLS=4096
S_LEFT,S_RIGHT=F(-6,5),F(-1,3)
D_LEFT,D_RIGHT=F(-1,10100),F(0)


def shifted(coefficients,center):
    point=ball(center)
    return [evaluate([ball(v*comb(j,k)) for j,v in enumerate(coefficients) if j>=k],point)
            for k in range(len(coefficients))]


def prepare(native,actual_cut=False):
    q=list(map(F,native['q']))
    kernel=1 if native['kind']=='endpoint' else 0
    penalty,roots,primitive=positive_penalty(q,kernel)
    original=[sum(primitive[j]*F(comb(j,k))*2**(j-k)/4**j
                  for j in range(k,8)) for k in range(8)]
    D_F=sum(a*b for a,b in zip(original,differences()))
    cut=2*(2*arb.pi()*7851/19683).cos() if actual_cut else ball(CUT_LEFT).union(ball(CUT_RIGHT))
    if actual_cut:
        assert cut>ball(CUT_LEFT) and cut<ball(CUT_RIGHT)
    cut_center=(CUT_LEFT+CUT_RIGHT+4)/8
    cut_offset=(cut+2)/4-ball(cut_center)
    cut_term=evaluate(shifted(primitive,cut_center),cut_offset)
    return {'kernel':kernel,'primitive':primitive,'constant':cut_term+ball(D_F)+penalty,
            'penalty':str(penalty),'root_boxes':[[str(a),str(b)] for a,b in roots],
            'cut':cut}


def bound(data,left,right,d_left=D_LEFT):
    center=(left+right+4)/8
    offset=ball((left-right)/8).union(ball((right-left)/8))
    d=ball(d_left).union(ball(D_RIGHT))
    coefficients=shifted(data['primitive'],center)
    trace=[arb(2),2*offset]
    for k in range(2,8):
        trace.append(2*offset*trace[-1]-(offset*offset-d/16)*trace[-2])
    value=sum((a*b for a,b in zip(coefficients,trace)),arb(0))-data['constant']
    if data['kernel']:
        s=ball(left).union(ball(right))
        cut=data['cut']
        argument=((s+2)**2-d)/(cut+2)
        assert argument>0
        value-=argument.log()
    assert value.is_finite()
    return value


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--small-shell',action='store_true',
                        help='One fixed R=1001/1000 check with the actual cut and 16384 cells.')
    args=parser.parse_args()
    ctx.prec=256
    cells=16384 if args.small_shell else CELLS
    d_left=F(-1,1001000) if args.small_shell else D_LEFT
    path=Path(__file__).resolve().parent/'inputs/endpoint_first_duals.json'
    native=json.loads(path.read_text())
    assert native['triple']==[10,18,27]
    prepared=[prepare(item,actual_cut=args.small_shell) for item in native['certificates']]
    counts=[0]*len(prepared)
    unresolved=[]
    for i in range(cells):
        left=S_LEFT+(S_RIGHT-S_LEFT)*F(i,cells)
        right=S_LEFT+(S_RIGHT-S_LEFT)*F(i+1,cells)
        values=[]
        for j,data in enumerate(prepared):
            value=bound(data,left,right,d_left)
            values.append(str(value))
            if value>0:
                counts[j]+=1
                break
        else:
            unresolved.append({'left':str(left),'right':str(right),'bounds':values})
    result={'cells':cells,'s':[str(S_LEFT),str(S_RIGHT)],'d':[str(d_left),str(D_RIGHT)],
            'actual_cut':args.small_shell,
            'certified_counts':counts,'unresolved_count':len(unresolved),
            'complete':not unresolved,'unresolved':unresolved,
            'certificates':[{k:v for k,v in row.items() if k in ('kernel','penalty','root_boxes')}
                            for row in prepared]}
    source=Path(__file__).resolve()
    output=source.parents[2]/'outputs'/source.parent.name
    output.mkdir(parents=True,exist_ok=True)
    name='endpoint_cover_small.json' if args.small_shell else 'endpoint_cover.json'
    (output/name).write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items() if k not in ('unresolved','certificates')},flush=True)
    print('first unresolved',unresolved[:5],flush=True)


if __name__=='__main__':
    main()
