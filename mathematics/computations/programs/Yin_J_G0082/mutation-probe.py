"""Declared k3/4, 4000-state/+3-energy/90-second actual congruence probe."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import deque
import argparse, heapq, json, platform, subprocess, sys, time, traceback

BASE=(_J_PROGRAM / 'mutation-probe.py').parent
CAP=90
LIMIT=4000

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


def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def normalize(V):
    n=len(V);sign=[0]*n
    for root in range(n):
        if sign[root]:continue
        sign[root]=1;todo=deque([root])
        while todo:
            i=todo.popleft()
            for j in range(n):
                a=V[min(i,j)][max(i,j)] if i!=j else 0
                if a and not sign[j]:
                    sign[j]=-sign[i]*(1 if a>0 else -1);todo.append(j)
    W=[[sign[i]*sign[j]*V[i][j] for j in range(n)] for i in range(n)]
    return W,sign

def mutate(V,i,direction):
    n=len(V);j=i+1;a=V[i][j];W=[row[:] for row in V]
    for h in range(n):
        if h in (i,j):continue
        x=V[h][i] if h<i else V[i][h]
        y=V[h][j] if h<i else V[j][h]
        b,c=(y,x-a*y) if direction==1 else (y-a*x,x)
        if h<i:W[h][i],W[h][j]=b,c
        else:W[i][h],W[j][h]=b,c
    W[i][j]=-a
    return W

def energy(V):return sum(V[i][j]**2 for i in range(len(V)) for j in range(i+1,len(V)))

def binary_rank(V):
    basis={};n=len(V)
    for j in range(n):
        x=sum(((V[i][j]+V[j][i])&1)<<i for i in range(n))
        while x:
            lead=x.bit_length()-1
            if lead not in basis:basis[lead]=x;break
            x^=basis[lead]
    return len(basis)

def abs_trace(V):
    n=len(V);A=[[abs(x) for x in row] for row in V];paths=eye(n)
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):paths[i][j]=sum(A[i][h]*paths[h][j] for h in range(i+1,j+1))
    return -n+sum(A[i][j]*paths[i][j] for i in range(n) for j in range(i+1,n))

def state(V,parent,generator,signs,depth):
    n=len(V)
    return {'matrix':V,'parent':parent,'generator':generator,'normalization_signs':signs,
            'depth':depth,'energy':energy(V),'height':max(abs(x) for row in V for x in row),
            'positive_edges':sum(V[i][j]>0 for i in range(n) for j in range(i+1,n)),
            'absolute_monodromy_trace':abs_trace(V),'binary_symmetrization_rank':binary_rank(V)}

def priority(s,i):return (s['positive_edges'],s['absolute_monodromy_trace'],s['energy'],s['depth'],i)

def flatten(V):return tuple(x for row in V for x in row)

def full(V):
    import sympy as sp
    n=len(V);inv=eye(n)
    assert all(V[i][i]==1 and all(V[i][j]==0 for j in range(i)) for i in range(n))
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):inv[i][j]=-sum(V[i][h]*inv[h][j] for h in range(i+1,j+1))
    mon=[[-sum(inv[i][h]*V[j][h] for h in range(n)) for j in range(n)] for i in range(n)]
    p=sp.Matrix(mon).charpoly().as_poly()
    coeff=[int(x) for x in reversed(p.all_coeffs())]
    fac,items=sp.factor_list(p)
    assert p==sp.Poly(fac*sp.prod(f**m for f,m in items),p.gen)
    return {'matrix':V,'dimension':n,'height':max(abs(x) for row in V for x in row),
            'energy':energy(V),'full_squared_sum':n+energy(V),'coefficients':coeff,
            'factorization':{'constant':int(fac),'factors':[{'coefficients':[int(x) for x in reversed(f.all_coeffs())],
                                                         'multiplicity':int(m)} for f,m in items]},
            'monodromy_trace':sum(mon[i][i] for i in range(n))}

def cover(V):
    n=len(V);W=eye(2*n)
    for i in range(n):
        for j in range(i+1,n):
            a=V[i][j]
            for s in (0,1):W[2*i+s][2*j+(s if a<=0 else 1-s)]=-abs(a)
    return W

def endpoint(rec,idx):
    import sympy as sp
    states=rec['states'];n=len(rec['original_matrix']);path=[];at=idx
    while states[at]['parent'] is not None:path.append(at);at=states[at]['parent']
    path.reverse()
    Q=eye(n)
    for j,s in enumerate(states[0]['normalization_signs']):Q[j][j]=s
    detQ=1
    for s in states[0]['normalization_signs']:detQ*=s
    for child in path:
        s=states[child];i,direction,a=s['generator']
        old=[row[:] for row in Q]
        for h in range(n):
            x,y=old[h][i],old[h][i+1]
            Q[h][i],Q[h][i+1]=(y,x-a*y) if direction==1 else (y-a*x,x)
        detQ=-detQ
        for j,sign in enumerate(s['normalization_signs']):
            detQ*=sign
            for h in range(n):Q[h][j]*=sign
    V=states[idx]['matrix'];qs=sp.Matrix(Q)
    assert qs.T*sp.Matrix(rec['original_matrix'])*qs==sp.Matrix(V)
    assert int(qs.det())==detQ and abs(detQ)==1
    U=[[1 if i==j else -abs(V[i][j]) for j in range(n)] for i in range(n)]
    records={'original':full(V),'absolute':full(U),'cover':full(cover(V))}
    assert records['original']['coefficients']==rec['full_original_polynomial']
    a=records['original']['coefficients'];b=records['absolute']['coefficients'];c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    assert c==records['cover']['coefficients']
    return {'state_id':idx,'path_state_ids':path,'Q':Q,'det_Q':detQ,'congruence_verified':True,
            'records':records,'switchable':states[idx]['positive_edges']==0}

def save(output,out,start):
    pass
    pending=output.with_suffix('.json.pending')
    pending.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');pending.replace(output)

def worker(output,start):
    out=json.loads(output.read_text(encoding='utf-8'))
    import sympy as sp
    source=json.loads(((_J_OUTPUT / 'result.json')).read_text(encoding='utf-8'))
    def gate():
        if time.perf_counter()-start>=CAP:raise TimeoutError('Declared aggregate90second cap')
    try:
        for k in (3,4):
            gate();old=next(x for x in source['instances'] if x['k']==k)
            V=old['matrices']['V']['matrix'];W,signs=normalize(V)
            rec={'k':k,'original_matrix':V,'full_original_polynomial':old['matrices']['V']['coefficients_ascending'],
                 'energy_ceiling':5*k+5,'states':[state(W,None,None,signs,0)],'attempts':[],
                 'status':'searching','endpoints':[]}
            out['instances'].append(rec);save(output,out,start)
            states=rec['states'];seen={flatten(W):0};queue=[priority(states[0],0)];stop=False
            while queue and not stop:
                gate();sid=heapq.heappop(queue)[-1];s=states[sid]
                if not s['positive_edges']:
                    rec['status']='switchable-found';rec['switchable_state']=sid;break
                for i in range(len(V)-1):
                    for direction in (1,-1):
                        M=mutate(s['matrix'],i,direction);e=energy(M)
                        attempt={'parent':sid,'index':i,'direction':direction,'candidate_energy':e}
                        if e>rec['energy_ceiling']:
                            attempt['status']='energy-rejected';rec['attempts'].append(attempt);continue
                        M,sgn=normalize(M);key=flatten(M)
                        if key in seen:
                            attempt.update(status='duplicate',child=seen[key]);rec['attempts'].append(attempt);continue
                        if len(states)==LIMIT:
                            attempt['status']='state-cap';rec['attempts'].append(attempt)
                            rec.update(status='state-cap',partial_expansion={'state':sid,'index':i,'direction':direction})
                            stop=True;break
                        child=len(states);seen[key]=child
                        states.append(state(M,sid,[i,direction,s['matrix'][i][i+1]],sgn,s['depth']+1))
                        assert states[-1]['binary_symmetrization_rank']==3*k-k%2
                        heapq.heappush(queue,priority(states[-1],child))
                        attempt.update(status='new',child=child);rec['attempts'].append(attempt)
                    if stop:break
                if len(states)%100==0:save(output,out,start)
            if rec['status']=='searching':rec['status']='complete-energy-component'
            rec['frontier_ids']=[item[-1] for item in sorted(queue)]
            rec['state_count']=len(states);rec['attempt_count']=len(rec['attempts'])
            ids=[min(range(len(states)),key=lambda i:priority(states[i],i)),
                 min(range(len(states)),key=lambda i:(states[i]['energy'],priority(states[i],i))),
                 min(range(len(states)),key=lambda i:(states[i]['absolute_monodromy_trace'],priority(states[i],i)))]
            if 'switchable_state' in rec:ids[0]=rec['switchable_state']
            selected=list(dict.fromkeys(ids));assert len(selected)<=3
            rec['selected_ids']=selected;save(output,out,start)
            for idx in selected:
                gate();rec['endpoints'].append(endpoint(rec,idx));save(output,out,start)
            print(json.dumps({'k':k,'status':rec['status'],'states':len(states),'selected':selected,
                              'scores':[priority(states[i],i) for i in selected]}),flush=True)
        gate();out['status']='complete-declared-probe';save(output,out,start);return 0
    except Exception as error:
        out.update(status='incomplete',error_type=type(error).__name__,error=_record_text(str(error)),traceback=_record_text(traceback.format_exc()))
        save(output,out,start);return 1

def main():
    if len(sys.argv)==4 and sys.argv[1]=='--worker':return worker(Path(sys.argv[2]),float(sys.argv[3]))
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=(_J_OUTPUT / 'mutation-probe.json'))
    output=ap.parse_args().output.resolve();assert output.parent == _J_OUTPUT
    start=time.perf_counter()
    out={'status': 'started', 'state_limit_per_input': LIMIT, 'domain_k': [3, 4], 'priority': ['positive_edges', 'absolute_monodromy_trace', 'energy', 'depth', 'state_id'], 'input': 'result.json', 'instances': []}
    with output.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2)
    proc=subprocess.Popen([sys.executable,'-X','utf8',str((_J_PROGRAM / 'mutation-probe.py')),'--worker',str(output),repr(start)],
                          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    timeout=False
    try:code=proc.wait(timeout=max(.01,CAP-(time.perf_counter()-start)))
    except subprocess.TimeoutExpired:timeout=True;proc.kill();code=proc.wait()
    out=json.loads(output.read_text(encoding='utf-8'))
    out.update(worker_returncode=code, outer_deadline_triggered=timeout)
    if timeout:out.update(status='incomplete',error_type='OuterDeadline',error='Declared90second outer deadline')
    save(output,out,start)
    print(json.dumps({k:v for k,v in out.items() if k!='instances'}),flush=True)
    return 1 if timeout else code

if __name__=='__main__':raise SystemExit(main())
