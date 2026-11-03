"""Complete D204 native review: literal congruences, witness search replay, full pencils."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse,heapq,json,math,platform,time,traceback
import review_independent as base
BASE=(_J_PROGRAM / 'mutation-review.py').parent
START=time.perf_counter();CAP=180;LEAVES=0
COUNTS={'states':0,'attempts':0,'congruences':0,'binary_ranks':0,'linear_solve_traces':0,'full_matrices':0,'pencil_evaluations':0,'factor_products':0}
# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def gate():
    if time.perf_counter()-START>=CAP:raise TimeoutError('Declared180second complete review cap')
def cmp(x,y,p=''):
    global LEAVES
    assert type(x) is type(y),(p,type(x),type(y))
    if isinstance(x,dict):
        assert set(x)==set(y),(p,set(x)^set(y))
        for k in x:cmp(x[k],y[k],p+'/'+str(k))
    elif isinstance(x,list):
        assert len(x)==len(y),(p,len(x),len(y))
        for i,(a,b) in enumerate(zip(x,y)):cmp(a,b,p+'/'+str(i))
    else:assert x==y,(p,x,y);LEAVES+=1
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):
    out=[[0]*len(B[0]) for _ in A]
    for i,row in enumerate(A):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(B[k]):
                    if y:out[i][j]+=x*y
    return out
def transpose(A):return [list(r) for r in zip(*A)]
def congr(V,T):
    COUNTS['congruences']+=1
    return mm(transpose(T),mm(V,T))
def transform(n,i,direction,a):
    T=eye(n)
    if direction==1:T[i][i],T[i][i+1],T[i+1][i],T[i+1][i+1]=0,1,1,-a
    else:T[i][i],T[i][i+1],T[i+1][i],T[i+1][i+1]=-a,1,1,0
    return T
def normalize(V):
    n=len(V);signs=[0]*n;serial=0
    for root in range(n):
        if signs[root]:continue
        signs[root]=1;frontier=[(0,serial,root)];serial+=1
        while frontier:
            level,order,u=heapq.heappop(frontier)
            for v in range(n):
                a=V[u][v]+V[v][u] if u!=v else 0
                if a and not signs[v]:
                    signs[v]=-signs[u]*(1 if a>0 else -1)
                    heapq.heappush(frontier,(level+1,serial,v));serial+=1
    return [[signs[i]*signs[j]*V[i][j] for j in range(n)] for i in range(n)],signs
def energy(V):return sum(x*x for i,row in enumerate(V) for x in row[i+1:])
def binary_rank(V):
    n=len(V);rows=[sum(((V[i][j]+V[j][i])%2)<<j for j in range(n)) for i in range(n)]
    at=0
    for col in range(n):
        pivot=next((i for i in range(at,n) if (rows[i]>>col)&1),None)
        if pivot is None:continue
        rows[at],rows[pivot]=rows[pivot],rows[at]
        for i in range(at+1,n):
            if (rows[i]>>col)&1:rows[i]^=rows[at]
        at+=1
    COUNTS['binary_ranks']+=1
    return at
def trace_by_solves(V):
    n=len(V);trace=0
    # Solve V x = column_j(V^T), retaining the diagonal x_j of V^-1 V^T.
    for j in range(n):
        x=[0]*n
        for i in range(n-1,-1,-1):
            x[i]=V[j][i]-sum(V[i][h]*x[h] for h in range(i+1,n))
        trace-=x[j]
    COUNTS['linear_solve_traces']+=1
    return trace
def state(V,parent,generator,signs,depth):
    n=len(V)
    assert all(len(row)==n and all(type(x) is int for x in row) for row in V)
    assert all(V[i][i]==1 and all(V[i][j]==0 for j in range(i)) for i in range(n))
    return {'matrix':V,'parent':parent,'generator':generator,'normalization_signs':signs,'depth':depth,
            'energy':energy(V),'height':max(abs(x) for row in V for x in row),
            'positive_edges':sum(x>0 for i,row in enumerate(V) for x in row[i+1:]),
            'absolute_monodromy_trace':trace_by_solves(base.absolute(V)),
            'binary_symmetrization_rank':binary_rank(V)}
def key(V):return tuple(tuple(row) for row in V)
def priority(s,i):return s['positive_edges'],s['absolute_monodromy_trace'],s['energy'],s['depth'],i
def determinant(V):
    base.START=START;base.CAP=CAP
    return base.determinant(V)
def full(rec,V,label):
    n=len(V);p=rec['coefficients']
    assert len(p)==n+1 and all(type(x) is int for x in p) and p[0]==p[-1]==1 and p==p[::-1]
    for t in range(n+1):
        assert determinant([[t*V[i][j]+V[j][i] for j in range(n)] for i in range(n)])==base.ev(p,t),(label,t)
        COUNTS['pencil_evaluations']+=1
    f=rec['factorization'];assert set(f)=={'constant','factors'} and type(f['constant']) is int
    product=[f['constant']]
    for r in f['factors']:
        assert set(r)=={'coefficients','multiplicity'}
        a=r['coefficients'];m=r['multiplicity']
        assert all(type(x) is int for x in a) and len(a)>=2 and a[-1]==1 and type(m) is int and m>=1
        product=base.mul(product,base.powp(a,m))
    assert product==p,(label,'factor product')
    expected={'matrix':V,'dimension':n,'height':max(abs(x) for row in V for x in row),
              'energy':energy(V),'full_squared_sum':n+energy(V),'coefficients':p,'factorization':f,
              'monodromy_trace':trace_by_solves(V)}
    cmp(rec,expected,label);assert expected['monodromy_trace']==-p[-2]
    COUNTS['full_matrices']+=1;COUNTS['factor_products']+=1
    return p
def verify(d):
    cmp(set(),set()) if False else None
    schema={'status', 'state_limit_per_input', 'domain_k', 'priority', 'input', 'instances', 'worker_returncode', 'outer_deadline_triggered'}
    assert set(d)==schema
    for k,v in {'status': 'complete-declared-probe', 'state_limit_per_input': 4000, 'domain_k': [3, 4], 'priority': ['positive_edges', 'absolute_monodromy_trace', 'energy', 'depth', 'state_id'], 'input': 'result.json', 'worker_returncode': 0, 'outer_deadline_triggered': False}.items():cmp(d[k],v,k)
    for k in ():
        assert type(d[k]) is float and math.isfinite(d[k]) and 0<d[k]<90
    assert len(d['instances'])==2
    reports=[]
    for k,r in zip((3,4),d['instances']):
        gate();V,_=base.graph(k);n=len(V);cmp(r['original_matrix'],V,str(k)+'/input')
        cmp(r['k'],k);cmp(r['energy_ceiling'],5*k+5)
        assert set(r)=={'k','original_matrix','full_original_polynomial','energy_ceiling','states','attempts','status','endpoints',
                       'partial_expansion','frontier_ids','state_count','attempt_count','selected_ids'}
        saved=r['states'];assert len(saved)==4000
        W,sign=normalize(V);expected=[state(W,None,None,sign,0)];cmp(saved[0],expected[0])
        seen={key(W):0};queue=[priority(expected[0],0)];ap=0;stop=False
        while queue and not stop:
            gate();sid=heapq.heappop(queue)[-1];s=expected[sid]
            assert s['positive_edges']>0,'Native cap must not skip a switchable stop'
            for i in range(n-1):
                for direction in (1,-1):
                    T=transform(n,i,direction,s['matrix'][i][i+1]);raw=congr(s['matrix'],T);en=energy(raw)
                    attempt={'parent':sid,'index':i,'direction':direction,'candidate_energy':en}
                    if en>5*k+5:attempt['status']='energy-rejected'
                    else:
                        new,signs=normalize(raw);ky=key(new)
                        if ky in seen:attempt.update(status='duplicate',child=seen[ky])
                        elif len(expected)==4000:
                            attempt['status']='state-cap';stop=True
                            cmp(r['partial_expansion'],{'state':sid,'index':i,'direction':direction})
                        else:
                            child=len(expected);seen[ky]=child
                            candidate=state(new,sid,[i,direction,s['matrix'][i][i+1]],signs,s['depth']+1)
                            assert candidate['binary_symmetrization_rank']==3*k-k%2
                            expected.append(candidate);cmp(saved[child],candidate,str(k)+'/state/'+str(child))
                            heapq.heappush(queue,priority(candidate,child));attempt.update(status='new',child=child)
                    assert ap<len(r['attempts']);cmp(r['attempts'][ap],attempt,str(k)+'/attempt/'+str(ap));ap+=1
                    if stop:break
                if stop:break
        assert stop and ap==len(r['attempts'])
        cmp(r['status'],'state-cap');cmp(r['state_count'],len(expected));cmp(r['attempt_count'],ap)
        cmp(r['frontier_ids'],[x[-1] for x in sorted(queue)])
        ids=[min(range(len(expected)),key=lambda i:priority(expected[i],i)),
             min(range(len(expected)),key=lambda i:(expected[i]['energy'],priority(expected[i],i))),
             min(range(len(expected)),key=lambda i:(expected[i]['absolute_monodromy_trace'],priority(expected[i],i)))]
        ids=list(dict.fromkeys(ids));cmp(r['selected_ids'],ids);assert len(r['endpoints'])==len(ids)
        for chosen,ep in zip(ids,r['endpoints']):
            gate();path=[];at=chosen
            while expected[at]['parent'] is not None:path.append(at);at=expected[at]['parent']
            path.reverse();Q=eye(n)
            for j,sg in enumerate(expected[0]['normalization_signs']):Q[j][j]=sg
            for child in path:
                s=expected[child];i,direction,aa=s['generator'];T=transform(n,i,direction,aa)
                Q=mm(Q,T)
                Q=[[x*s['normalization_signs'][j] for j,x in enumerate(row)] for row in Q]
            end=expected[chosen]['matrix'];cmp(congr(V,Q),end)
            detq=determinant(Q);assert abs(detq)==1
            assert set(ep['records'])=={'original','absolute','cover'}
            po=full(ep['records']['original'],end,str(k)+'/original')
            pu=full(ep['records']['absolute'],base.absolute(end),str(k)+'/absolute')
            pc=full(ep['records']['cover'],base.lift(end),str(k)+'/cover')
            cmp(po,r['full_original_polynomial']);assert base.mul(po,pu)==pc
            exp={'state_id':chosen,'path_state_ids':path,'Q':Q,'det_Q':detq,'congruence_verified':True,
                 'records':ep['records'],'switchable':expected[chosen]['positive_edges']==0}
            cmp(ep,exp,str(k)+'/endpoint')
        COUNTS['states']+=len(expected);COUNTS['attempts']+=ap
        reports.append({'k':k,'states':len(expected),'attempts':ap,'frontier':len(queue),'selected':ids,
                        'complete_native_verified':True,'search_closed':False})
    return reports
def main():
    global START
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=(_J_OUTPUT / 'mutation-review-result.json'))
    out=ap.parse_args().output.resolve();assert out.parent == _J_OUTPUT and not out.exists()
    START=time.perf_counter()
    names=['mutation-probe.py','mutation-probe.json','verify.py','result.json','review_independent.py','review_result.json',
           'binary-invariants.py','binary-invariants.json','binary-review.py','binary-review-result.json']
    before={n:(((_J_PROGRAM if n in ('binary-invariants.py', 'binary-review.py', 'mutation-probe.py', 'mutation-review.py', 'readme.md', 'repeated-cell-author.py', 'repeated-cell-review.py', 'review_independent.py', 'verify.py') else _J_OUTPUT) / n)).read_bytes() for n in names}
    report={'status': 'started', 'domain': [3, 4], 'method': 'generic sparse bilinear congruences, complete retained frontier replay, low-bit row rank, linear-system traces, Bareiss pencils'}
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    try:
        report['instances']=verify(json.loads(before['mutation-probe.json']))
        gate();report['status']='passed';code=0
    except Exception as exc:
        report.update(status='failed',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()));code=1
    report.update(counters=COUNTS, strict_scalar_comparisons=LEAVES, factor_scope='complete exact product decompositions; no library irreducibility assumption')
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    print(json.dumps(report,indent=2));return code
if __name__=='__main__':raise SystemExit(main())
