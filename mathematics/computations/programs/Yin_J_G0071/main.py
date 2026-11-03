"""Complete predetermined scalar finite-map test of the ln(2) relative profile."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations_with_replacement
from collections import Counter
import json,time,sys
CAP=60
def run():
    start=time.perf_counter();records=[];failures=[];checks=0
    for n in range(1,9):
        for cols in combinations_with_replacement(range(1,5),n):
            mu={0:1}
            for a in cols:
                nxt=Counter()
                for z,w in mu.items():
                    for digit,weight in [(-1,1),(0,2),(1,1)]:nxt[z+a*digit]+=w*weight
                mu=dict(nxt)
            assert sum(mu.values())==4**n
            assert all(mu[z]==mu[-z] for z in mu)
            Q=sum(a*a for a in cols);zero=mu[0];bad=[]
            for z in sorted(mu):
                if not z:continue
                checks+=1
                if pow(mu[z],Q)*(1<<(z*z))>pow(zero,Q):
                    bad.append(z);failures.append(dict(columns=list(cols),Q=Q,z=z,count=mu[z],zero=zero))
            records.append(dict(columns=list(cols),Q=Q,denominator=4**n,
                counts=[[z,mu[z]] for z in sorted(mu)],failed_endpoints=bad))
            if time.perf_counter()-start>CAP:raise TimeoutError('Declared cap exceeded; incomplete result not published')
    return dict(status='complete', scope=dict(lengths=[1, 8], positive_column_values=[1, 2, 3, 4], normalization='sorted multisets', all_nonzero_endpoints=True), pattern_count=len(records), endpoint_test_count=checks, failure_count=len(failures), failures=failures, records=records)
if __name__=='__main__':
    r=run()
    (_J_OUTPUT / 'result.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k: r[k] for k in ['status', 'pattern_count', 'endpoint_test_count', 'failure_count', 'failures']}, indent=2))

