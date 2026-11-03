"""Whole J83 independent review: binary autocorrelation; exact rational logs. 180 s."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import defaultdict
from math import gcd, lcm
import json, sys, time, subprocess, traceback

HOME=(_J_PROGRAM / 'review_independent.py').parent
OUT=(_J_OUTPUT / 'review_result.json')
CAP=180
S=1<<128
L=1
for q in range(1,256,2): L=lcm(L,q)
COEF=[L//(2*j+1) for j in range(128)]

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


def sign_surd(a,b):
    if not b:return (a>0)-(a<0)
    if a>=0 and b>=0:return 1
    if a<=0 and b<=0:return -1
    d=a*a-5*b*b
    return ((d>0)-(d<0))*(1 if a>0 else -1)

def logcheck(p,q,lo,hi):
    assert q<=p<=2*q and type(lo) is int and type(hi) is int
    if p==q:
        assert lo==hi==0;return
    p,q=p-q,p+q
    g=gcd(p,q);p//=g;q//=g
    p2,q2=p*p,q*q
    h=COEF[-1];qp=q2
    for c in reversed(COEF[:-1]):
        h=h*p2+c*qp;qp*=q2
    # h=sum c_j p^(2j) q^(254-2j), denominator L*q^255.
    q255=pow(q,255);den=L*q255;num=2*p*h
    assert lo*den<=num*S
    top=num*257*(q2-p2)+2*pow(p,257)*L
    bot=den*257*(q2-p2)
    assert hi*bot>=top*S and lo<=hi

def allints(x):
    if isinstance(x,list):return all(allints(t) for t in x)
    if isinstance(x,dict):return all(allints(t) for t in x.values())
    return type(x) is int

def perform(report):
    start=time.perf_counter()
    files=[(_J_PROGRAM / 'profile.py'),(_J_OUTPUT / 'result.json'),(_J_PROGRAM / 'readme.md')]
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0198.md')
    if draft.exists():files.append(draft)
    before={str(p):p.read_bytes() for p in files}
    d=json.loads(before[str((_J_OUTPUT / 'result.json'))])
    assert set(d)=={'schema', 'status', 'input', 'interval_method', 'carry_states', 'zero_index', 'carry_matrices', 'records', 'failures', 'undecided'}
    assert d['schema']=='golden-c1-v1' and d['status']=='complete'
    assert d['input'] == {'ascending_polynomial': [-1, -1, 1], 'degree': 2, 'windows': list(range(5, 19)), 'digits': [-1, 0, 1], 'numerator_weights': [1, 2, 1], 'probability_denominator': 4}
    assert d['failures']==d['undecided']==[]
    pass
    pass
    pass
    it=d['interval_method']
    assert set(it)=={'terms','scale','log2_interval','tail_numerator','tail_denominator'}
    assert it['terms']==128 and it['scale']==S and it['tail_numerator']==9 and it['tail_denominator']==1028*3**257 and 9*S<1028*3**257
    log2=it['log2_interval'];assert allints(it)
    logcheck(2,1,*log2)
    # Exhaust strict inequalities via exact signs in Q(sqrt 5), with proved |h|<4, |a|<9.
    states=[]
    for a in range(-8,9):
        for h in range(-3,4):
            if all(sign_surd(A,B)>0 for A,B in [(2-2*a-h,2-h),(2+2*a+h,2+h),(6-2*a-h,2+h),(6+2*a+h,2-h)]):states.append((a,h))
    states.sort();assert len(states)==29 and d['carry_states']==[list(x) for x in states]
    zero=states.index((0,0));assert d['zero_index']==zero
    incoming={}
    for e in [-1,0,1]:
        mat=[];inc=[[] for _ in states]
        for i,(a,h) in enumerate(states):
            row=[]
            for j,(c,k) in enumerate(states):
                # phi*(c+k phi)-(a+h phi)=(k-a,c+k-h).
                digit=e-(k-a)
                val=(2 if digit==0 else 1) if c+k-h==0 and digit in(-1,0,1) else 0
                row.append(val)
                if val:inc[j].append((i,val))
            mat.append(row)
        assert d['carry_matrices'][str(e)]==mat
        incoming[e]=inc
    assert set(d['carry_matrices'])=={'-1','0','1'} and allints(d['carry_matrices'])
    def backward(word):
        v={zero:1}
        for e in reversed(word):
            nxt={}
            for j,c in v.items():
                for i,w in incoming[e][j]:nxt[i]=nxt.get(i,0)+c*w
            v=nxt
        return v.get(zero,0)
    binary={(0,0):1};cols=[];x=(1,0);records=d['records'];assert len(records)==14
    totalrows=totalclasses=paircount=carrycalls=0
    for b in range(1,19):
        cols.append(x);bb=dict(binary)
        for (a,h),c in binary.items():
            t=(a+x[0],h+x[1]);bb[t]=bb.get(t,0)+c
        binary=bb;x=(x[1],x[0]+x[1])
        assert sum(binary.values())==2**b
        if b<5:continue
        rec=records[b-5]
        assert set(rec)=={'window', 'rank', 'nullity', 'columns', 'gram', 'determinant', 'central_count', 'probability_denominator', 'endpoint_count', 'normalization', 'class_count', 'classes', 'rows_schema', 'rows', 'equality_endpoints', 'failure_endpoints', 'undecided_endpoints', 'all_carry_counts_checked'}
        assert rec['window']==b and rec['rank']==2 and rec['nullity']==b-2
        assert rec['columns']==[list(z) for z in cols]
        # Injective flattening of all binary DIFFERENCES, followed by unordered autocorrelation.
        maxa=sum(c[0] for c in cols);stride=2*maxa+1
        items=sorted((a+stride*h,c) for (a,h),c in binary.items())
        counts={0:sum(c*c for _,c in items)}
        for i,(code,ci) in enumerate(items):
            for j in range(i):
                other,cj=items[j];dd=code-other
                counts[dd]=counts.get(dd,0)+ci*cj
            if i%256==0 and time.perf_counter()-start>CAP-2:raise TimeoutError('declared review deadline')
        paircount+=len(items)*(len(items)-1)//2
        assert counts[0]+2*sum(c for k,c in counts.items() if k)==4**b
        full={}
        for code,c in counts.items():
            a=(code+maxa)%stride-maxa;h=(code-a)//stride
            full[(a,h)]=c
            if code:full[(-a,-h)]=c
        gram=[[sum(z[i]*z[j] for z in cols) for j in range(2)] for i in range(2)]
        ga,gb,gc=gram[0][0],gram[0][1],gram[1][1];det=ga*gc-gb*gb
        assert det>0 and rec['gram']==gram and rec['determinant']==det
        central=full[(0,0)];assert rec['central_count']==central and rec['normalization']==rec['probability_denominator']==4**b
        assert rec['endpoint_count']==len(full)==len(rec['rows'])
        assert rec['rows_schema']==['a','h','count','energy_numerator','energy_denominator','word','status']
        logdata={};classmax={};rowmap={};equal=[];fail=[];undec=[]
        for cl in rec['classes']:
            assert set(cl)=={'count','energy','endpoint','word','log_ratio_data','margin_interval','status'}
            c=cl['count'];k,lo,hi=cl['log_ratio_data']
            assert type(c) is int and c>0 and type(k) is int and k>=0
            assert c*(1<<k)<=central<2*c*(1<<k)
            logcheck(central,c*(1<<k),lo,hi)
            assert c not in logdata;logdata[c]=(k,lo,hi)
        for row in rec['rows']:
            assert len(row)==7
            a,h,c,en,ed,word,status=row
            assert all(type(q) is int for q in[a,h,c,en,ed]) and all(type(q) is int and q in(-1,0,1) for q in word) and len(word)==b
            assert (a,h) not in rowmap and full[(a,h)]==c
            assert (sum(word[j]*cols[j][0] for j in range(b)),sum(word[j]*cols[j][1] for j in range(b)))==(a,h)
            assert backward(word)==c;carrycalls+=1
            raw=gc*a*a-2*gb*a*h+ga*h*h;g=gcd(raw,det)
            assert [en,ed]==[raw//g,det//g]
            k,lo,hi=logdata[c];coeff=ed*k-en
            low=ed*lo+coeff*(log2[0] if coeff>=0 else log2[1])
            high=ed*hi+coeff*(log2[1] if coeff>=0 else log2[0])
            expected='equality' if (a,h)==(0,0) else 'strict-pass' if low>0 else 'strict-failure' if high<0 else 'undecided'
            assert status==expected
            if expected=='equality':assert en==0 and c==central;equal.append([a,h])
            elif expected=='strict-failure':fail.append([a,h])
            elif expected=='undecided':undec.append([a,h])
            if c not in classmax or en*classmax[c][1]>classmax[c][0]*ed:classmax[c]=(en,ed)
            rowmap[(a,h)]=row
        assert set(rowmap)==set(full) and rec['class_count']==len(classmax)==len(logdata)==len(rec['classes'])
        for cl in rec['classes']:
            en,ed=cl['energy'];c=cl['count'];ep=tuple(cl['endpoint']);row=rowmap[ep]
            assert [en,ed]==list(classmax[c]) and cl['word']==row[5] and row[2:5]==[c,en,ed] and cl['status']==row[6]
            k,lo,hi=logdata[c];cf=ed*k-en
            margin=[ed*lo+cf*(log2[0] if cf>=0 else log2[1]),ed*hi+cf*(log2[1] if cf>=0 else log2[0]),ed*S]
            assert cl['margin_interval']==margin
            assert allints({k:cl[k] for k in['count','energy','endpoint','word','log_ratio_data','margin_interval']})
        assert equal==rec['equality_endpoints']==[[0,0]] and fail==rec['failure_endpoints']==[] and undec==rec['undecided_endpoints']==[]
        assert rec['all_carry_counts_checked'] is True
        pass;pass
        for key in['window','rank','nullity','columns','gram','determinant','central_count','probability_denominator','endpoint_count','normalization','class_count','equality_endpoints','failure_endpoints','undecided_endpoints']:assert allints(rec[key])
        totalrows+=len(full);totalclasses+=len(classmax)
        report['windows'].append({'b':b,'binary_endpoints':len(binary),'original_endpoints':len(full),'classes':len(classmax),'central_count':central,'gram_determinant':det,'all_math_fields_verified':True})
        OUT.write_text(json.dumps(report,indent=2),encoding='utf-8')
        print('checked window',b,flush=True)
    assert totalrows==114072 and totalclasses==21872 and carrycalls==totalrows
    report.update(status='complete',endpoint_count=totalrows,class_count=totalclasses,binary_unordered_pairs=paircount,backward_carry_words=carrycalls,exact_128_term_log_intervals=totalclasses+1,all_native_schema_and_math_fields_verified=True)
    pass
    pass
    pass

def worker():
    r={'reviewer': 'orbit_research', 'status': 'running', 'domain': {'windows': list(range(5, 19)), 'series_terms': 128, 'source_scale': S}, 'methods': ['binary integer autocorrelation', 'backward full labelled carry', 'homogeneous rational log polynomial with exact rational tail'], 'windows': []}
    try:perform(r)
    except BaseException as e:
        r.update(status='failed-or-incomplete',failure=_record_text(repr(e)),traceback=_record_text(traceback.format_exc()));raise
    finally:OUT.write_text(json.dumps(r,indent=2),encoding='utf-8')

if __name__=='__main__':
    if '--worker' in sys.argv:worker()
    else:
        st=time.perf_counter();p=subprocess.Popen([sys.executable,__file__,'--worker'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        timeout=False
        try:stdout,stderr=p.communicate(timeout=CAP)
        except subprocess.TimeoutExpired:timeout=True;p.kill();stdout,stderr=p.communicate()
        r=json.loads(OUT.read_text()) if OUT.exists() else {'status':'not-started'}
        if timeout:r['status']='incomplete-timeout'
        pass
        OUT.write_text(json.dumps(r,indent=2),encoding='utf-8')
        print(json.dumps({k: r.get(k) for k in ['status', 'endpoint_count', 'class_count', 'binary_unordered_pairs']}))
        print(stdout);print(stderr)
        raise SystemExit(0 if r.get('status')=='complete' and not timeout and p.returncode==0 else 1)
