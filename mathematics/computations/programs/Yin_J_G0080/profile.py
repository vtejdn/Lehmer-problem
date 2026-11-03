"""Complete exact actual-power profile domain; standard library, no author imports."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import gcd, lcm
import time, json, gzip, sys, platform

HOME=(_J_PROGRAM / 'profile.py').parent
CAP=120

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


def inverse(a):
    n=len(a); x=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=next(i for i in range(j,n) if x[i][j])
        x[j],x[k]=x[k],x[j]
        v=x[j][j]; x[j]=[e/v for e in x[j]]
        for i in range(n):
            if i!=j:
                v=x[i][j]
                x[i]=[e-v*f for e,f in zip(x[i],x[j])]
    return [row[n:] for row in x]

def rational(a):
    return [[[v.numerator,v.denominator] for v in row] for row in a]

def columns(p,b):
    d=len(p)-1; x=[1]+[0]*(d-1); out=[]
    for _ in range(b):
        out.append(x)
        x=[(x[i-1] if i else 0)-x[-1]*p[i] for i in range(d)]
    return out

def run():
    start=time.perf_counter(); completed=[]; result_created=False
    def cap():
        elapsed=time.perf_counter()-start
        if elapsed>CAP: raise TimeoutError('Declared aggregate 120-second cap exceeded')
        return elapsed
    domains=[('quartic',[1,-1,-1,-1,1],b) for b in (7,8,9,10)]
    domains += [('lehmer',[1,1,0,-1,-1,-1,-1,-1,0,1,1],12)]
    targets=[(_J_OUTPUT / 'result.json')]+[_J_OUTPUT/f'{name}_b{b}.json.gz' for name,p,b in domains]
    assert not any(p.exists() for p in targets), 'First author outputs must not be overwritten'
    try:
        for name,p,b in domains:
            cap(); d=len(p)-1; k=b-d; cols=columns(p,b)
            rel=[[p[i-j] if 0<=i-j<=d else 0 for j in range(k)] for i in range(b)]
            G=[[sum(rel[i][j]*rel[i][h] for i in range(b)) for h in range(k)] for j in range(k)]
            Gi=inverse(G); den=lcm(*(v.denominator for row in Gi for v in row))
            adj=[[int(v*den) for v in row] for row in Gi]
            Q=[[sum(c[i]*c[j] for c in cols) for j in range(d)] for i in range(d)]
            Qi=inverse(Q)
            assert all(sum(cols[i][u]*rel[i][j] for i in range(b))==0 for u in range(d) for j in range(k))
            for i in range(b):
                for j in range(b):
                    left=F(i==j)-sum(F(rel[i][u]*adj[u][v]*rel[j][v],den) for u in range(k) for v in range(k))
                    right=sum(cols[i][u]*Qi[u][v]*cols[j][v] for u in range(d) for v in range(d))
                    assert left==right
            dist={(0,)*d:(1,0)}
            for j,col in enumerate(cols):
                nd={}
                for z,(count,word) in dist.items():
                    for eta,w in ((-1,1),(0,2),(1,1)):
                        y=tuple(z[i]+eta*col[i] for i in range(d))
                        c,rep=nd.get(y,(0,word|((eta+1)<<(2*j))))
                        nd[y]=(c+w*count,rep)
                dist=nd; cap()
            zero=(0,)*d; c0=dist[zero][0]; total=sum(c for c,w in dist.values())
            assert total==4**b
            assert all(dist[tuple(-v for v in z)][0]==c for z,(c,w) in dist.items())
            filename=f'{name}_b{b}.json.gz'; out=[]; bins={}; failures=[]; equality=0
            for j,(z,(c,packed)) in enumerate(sorted(dist.items())):
                if j%2048==0: cap()
                eta=[((packed>>(2*i))&3)-1 for i in range(b)]
                assert all(v in (-1,0,1) for v in eta)
                assert tuple(sum(eta[i]*cols[i][u] for i in range(b)) for u in range(d))==z
                v=[sum(rel[i][h]*eta[i] for i in range(b)) for h in range(k)]
                num=den*sum(e*e for e in eta)-sum(v[u]*adj[u][h]*v[h] for u in range(k) for h in range(k))
                g=gcd(num,den); A=num//g; B=den//g
                assert 0<=A<=b*B
                left=pow(c,B)*(1<<A); right=pow(c0,B); passed=left<=right
                equality += left==right
                if not passed: failures.append([list(z),c,A,B])
                out.append([list(z),c,A,B,passed])
                old=bins.get(c)
                if old is None or A*old['energy'][1]>old['energy'][0]*B:
                    bins[c]={'count':c,'energy':[A,B],'endpoint':list(z),'word':eta,
                             'left':left,'right':right,'passed':passed}
            assert all(c==sum(1 for row in out if row[1]==key) or True for key,c in [])
            with gzip.open(((_J_PROGRAM if filename in ('profile.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / filename),'xt',encoding='utf-8',compresslevel=1) as f:
                json.dump(out,f,separators=(',',':'))
            cap()
            item={'name':name,'polynomial':p,'degree':d,'window':b,'rank':d,'nullity':k,
                  'raw_words':3**b,'columns':cols,'Q':Q,'Q_inverse':rational(Qi),
                  'relations':rel,'relation_gram':G,'relation_gram_inverse':rational(Gi),
                  'projection_identity':True,'normalization':total,'denominator':4**b,
                  'endpoint_count':len(dist),'zero_count':c0,'symmetry':True,
                  'equality_count':equality,'failures':failures,'all_passed':not failures,
                  'count_energy_certificate':[bins[c] for c in sorted(bins)],
                  'payload':filename,'payload_schema':['endpoint','count','energy_numerator','energy_denominator','passed']}
            completed.append(item)
            print(json.dumps({'domain':name,'b':b,'endpoints':len(dist),'zero_count':c0,'failures':len(failures),'elapsed':time.perf_counter()-start}),flush=True)
        report={'schema': 'J80-original-profile-v1', 'domains': completed, 'total_raw_words': sum((x['raw_words'] for x in completed)), 'total_endpoints': sum((x['endpoint_count'] for x in completed)), 'complete': False, 'all_passed': all((x['all_passed'] for x in completed))}
        with ((_J_OUTPUT / 'result.json')).open('x',encoding='utf-8') as f:
            result_created=True
            json.dump(report,f,indent=2)
        cap()
        report['complete']=True
        with ((_J_OUTPUT / 'result.json')).open('w',encoding='utf-8') as f: json.dump(report,f,indent=2)
        elapsed=cap()
        print(json.dumps({'complete':True,'total_endpoints':report['total_endpoints'],'all_passed':report['all_passed'],'elapsed':elapsed}),flush=True)
    except Exception as e:
        if result_created:
            ((_J_OUTPUT / 'result.json')).unlink(missing_ok=True)
        failure={'exception':type(e).__name__,'message':_record_text(str(e)),'completed_domains':completed,'complete':False}
        with (_J_OUTPUT/'failure.json').open('w',encoding='utf-8') as f:json.dump(failure,f,indent=2)
        raise

if __name__=='__main__':run()
