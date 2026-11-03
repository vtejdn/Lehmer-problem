"""Compress the already checked residue classes into a reusable coefficient law."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import Counter
import json
from exact import model,evaluator,terms

def run():
    src=json.loads((_J_OUTPUT / 'mod4_result.json').read_text(encoding='utf-8'));rows=[];total=0
    for r in src['models']:
        i,j=r['positions'];m=model(i,j);f={k:evaluator(v) for k,v in m.items()}
        # This makes the parity of D=(Pf^2-ell^2)/8 unchanged by d -> d+4z.
        assert all(co%2==0 for co,mon in terms(m['pf']-m['ell']))
        hist=Counter()
        for target in ('F','S6'):
            for d in r['survivors'][target]:
                e,p,a=f['ell'](d),f['pf'](d),f['first'](d)
                assert e%2 and p%2 and f['norm_half'](d)%4==1 and a%2==0
                assert (p*p-e*e)%8==0
                b=(p*p-e*e)//8
                assert (a+2*b)%4==2
                hist[f'{a%4},{b%2}']+=1;total+=1
        rows.append(dict(positions=[i,j],even_trace_classes=sum(hist.values()),trace_residue_D_parity_histogram=dict(sorted(hist.items()))))
    assert total==3584
    return dict(passed=True,scope='All already enumerated mod4 classes with odd ell, N=1 mod4 and even A; P=ell mod2 holds identically',invariant='A+2*((Pf^2-ell^2)/8) = 2 mod4',actual_polynomial_consequence='If a is even, a+b=1 mod4',checked_classes=total,positions=rows)
if __name__=='__main__':
    out=run();(_J_OUTPUT / 'congruence_result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
