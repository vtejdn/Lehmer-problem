"""Exact classification of uncovered discovery targets against actual K8."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from array import array
import json
import estimate as e

iv=e.iv;BASE=(_J_PROGRAM / 'classify_uncovered.py').parent


def main():
    beta,M=e.embeddings();S=iv.div(beta,iv.sub(beta,iv.point(1)))
    raw=(_J_PROGRAM/'inputs/uncovered.bin').read_bytes();keys=array('Q');keys.frombytes(raw)
    records=[];counts={}
    for key in keys:
        a=[((key>>(5*i))&31)-16 for i in range(10)]
        values=[iv.sum_intervals(iv.mul(iv.point(v),m) for v,m in zip(a,row)) for row in M]
        norm2=iv.sum_intervals(iv.square(v) for v in values[2:])
        if values[0][0]>1 or values[0][1]<-1:reason='outside_expanding_strip'
        elif values[1][0]>S[1] or values[1][1]<-S[1]:reason='outside_contracting_strip'
        elif norm2[0]>=64:reason='outside_strict_neutral_ball'
        else:reason='not_excluded'
        counts[reason]=counts.get(reason,0)+1
        records.append({'state':a,'reason':reason,'neutral_squared_interval':[str(x) for x in norm2]})
    out={'uncovered_count':len(keys),'exact_classification_counts':counts,
         'all_uncovered_excluded_from_K8':all(r['reason']!='not_excluded' for r in records),'records':records}
    ((_J_OUTPUT / 'uncovered-classification.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))


if __name__=='__main__':main()
