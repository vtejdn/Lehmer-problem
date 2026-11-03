"""Reuse already discovered joint simplices wherever all their blocks are legal."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json


def main():
    base= _J_OUTPUT
    data=json.loads((base/'cover.json').read_text())
    beta=data['beta'];grid=data['grid']
    out={k:v for k,v in data.items() if k!='cells'}
    rows=[]
    for j in range(50,100):
        choices=[]
        for source in data['cells']:
            legal=True
            for w in source['digits']:
                lo=j/grid;hi=(j+1)/grid
                for d in w:lo=beta*lo+d;hi=beta*hi+d
                if not(-1+1e-7<lo and hi<1-1e-7):legal=False;break
            if legal:choices.append(source)
        best=min(choices,key=lambda r:r['sufficient_neutral_radius'])
        row=dict(best);row['source_cell']=best['j'];row['j']=j
        rows.append(row)
    out['cells']=rows
    out['scope']='numerical reuse of saved joint simplices; exact recheck required'
    (base/'reused-cover.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'cells':len(rows),'distinct_source_cells':len({r['source_cell'] for r in rows}),
                      'largest_sufficient_radius':max(r['sufficient_neutral_radius'] for r in rows),
                      'worst_cells':[r['j'] for r in rows if r['sufficient_neutral_radius']>1000]},indent=2))


if __name__=='__main__':main()
