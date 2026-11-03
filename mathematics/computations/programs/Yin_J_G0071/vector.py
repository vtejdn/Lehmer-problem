"""Second explicitly declared joint-covariance domain; no scalar-stage expansion."""
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
    start=time.perf_counter();records=[];fails=[];checks=0
    alphabet=[(1,0),(0,1),(1,1),(1,-1),(2,1),(1,2)]
    for k in range(5):
        for indices in combinations_with_replacement(range(6),k):
            cols=[(1,0),(0,1)]+[alphabet[j] for j in indices]
            mu={(0,0):1}
            for a,b in cols:
                nxt=Counter()
                for (x,y),w in mu.items():
                    for t,v in [(-1,1),(0,2),(1,1)]:nxt[x+t*a,y+t*b]+=w*v
                mu=dict(nxt)
            n=len(cols);assert sum(mu.values())==4**n
            aa=sum(x*x for x,y in cols);bb=sum(x*y for x,y in cols);cc=sum(y*y for x,y in cols)
            D=aa*cc-bb*bb;assert D>0
            zero=mu[0,0];rhs=pow(zero,D);bad=[]
            for x,y in sorted(mu):
                assert mu[x,y]==mu[-x,-y]
                if not(x or y):continue
                checks+=1;v=cc*x*x-2*bb*x*y+aa*y*y
                if pow(mu[x,y],D)*(1<<v)>rhs:
                    bad.append([x,y]);fails.append(dict(columns=cols,Q=[[aa,bb],[bb,cc]],D=D,z=[x,y],v=v,count=mu[x,y],zero=zero))
            records.append(dict(columns=cols,Q=[[aa,bb],[bb,cc]],D=D,denominator=4**n,
                counts=[[x,y,mu[x,y]] for x,y in sorted(mu)],failed_endpoints=bad))
            if time.perf_counter()-start>CAP:raise TimeoutError('Declared cap reached; no complete output')
    return dict(status='complete', scope=dict(fixed_columns=[[1, 0], [0, 1]], alphabet=alphabet, extra_column_counts=[0, 4], all_nonzero_endpoints=True), pattern_count=len(records), endpoint_test_count=checks, failure_count=len(fails), failures=fails, records=records)
if __name__=='__main__':
    r=run();(_J_OUTPUT / 'result-vector.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k: r[k] for k in ['status', 'pattern_count', 'endpoint_test_count', 'failure_count', 'failures']}, indent=2))

