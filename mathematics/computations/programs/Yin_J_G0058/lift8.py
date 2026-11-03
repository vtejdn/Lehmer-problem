"""Declared complete mod8 lifting of every retained mod4 class."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import product
from collections import Counter
import json,time
from exact import model,evaluator

def run():
    start=time.perf_counter();source=json.loads((_J_OUTPUT / 'mod4_result.json').read_text(encoding='utf-8'));rows=[]
    for r in source['models']:
        i,j=r['positions'];m=model(i,j);f={k:evaluator(v) for k,v in m.items()};targets={}
        for target,pf,a in [('F',3,-2),('S6',1,0)]:
            count=Counter();surv=[]
            for base in r['survivors'][target]:
                for bits in product(range(2),repeat=6):
                    x=tuple(base[k]+4*bits[k] for k in range(6));count['lift_tests']+=1
                    if f['ell'](x)%8 not in (1,7):continue
                    count['unit_minor']+=1
                    if f['pf'](x)%8 not in (pf%8,(-pf)%8):continue
                    count['target_pfaffian']+=1
                    if f['norm_half'](x)%8!=1:continue
                    count['norm_two']+=1
                    if f['first'](x)%8!=a%8:continue
                    surv.append(list(x))
            targets[target]=dict(counts=dict(count),survivors=surv)
            if time.perf_counter()-start>120:raise RuntimeError('Declared 120-second cap reached; no complete output published')
        rows.append(dict(positions=[i,j],targets=targets))
    return dict(scope=dict(modulus=8, source_modulus=4, complete_binary_lifts_per_class=64, declared_test_cap=229376), positions=rows, total_lift_tests=sum((r['targets'][t]['counts'].get('lift_tests', 0) for r in rows for t in ['F', 'S6'])), total_survivors={t: sum((len(r['targets'][t]['survivors']) for r in rows)) for t in ['F', 'S6']})
if __name__=='__main__':
    result=run();(_J_OUTPUT / 'mod8_result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='positions'}));print(json.dumps([dict(positions=r['positions'],survivors={t:len(z['survivors']) for t,z in r['targets'].items()}) for r in result['positions']]))
