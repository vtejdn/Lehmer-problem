"""Declared golden-unit domain only. Exact arithmetic; supervised 120 s cap."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from collections import defaultdict
from fractions import Fraction
from math import gcd
import sys, json, time, subprocess, platform

HOME = (_J_PROGRAM / 'profile.py').parent
OUT = (_J_OUTPUT / 'result.json')
PART = (_J_OUTPUT / 'partial.json')
CAP = 120
SCALE = 1 << 128
TERMS = 128

def ceildiv(a, b):
    return -(-a // b)

def log_unit_interval(p, q):
    """log(p/q), 1<=p/q<=2; endpoints are integer multiples of 2^-128."""
    assert q <= p <= 2*q
    if p == q:
        return (0, 0)
    num, den = p-q, p+q
    lo, hi = SCALE*num//den, ceildiv(SCALE*num, den)
    xxlo, xxhi = lo*lo//SCALE, ceildiv(hi*hi, SCALE)
    hlow = SCALE//255
    hhigh = ceildiv(SCALE, 255)
    for j in range(126, -1, -1):
        hlow = SCALE//(2*j+1) + xxlo*hlow//SCALE
        hhigh = ceildiv(SCALE, 2*j+1) + ceildiv(xxhi*hhigh, SCALE)
    outlo = 2*lo*hlow//SCALE
    outhi = ceildiv(2*hi*hhigh, SCALE) + 1
    assert 9*SCALE < 1028*3**257  # complete omitted series tail < one unit
    return outlo, outhi

LOG2 = log_unit_interval(2, 1)

def log_ratio_interval(p, q):
    assert p >= q > 0
    k = 0
    while p >= 2*q:
        q *= 2
        k += 1
    lo, hi = log_unit_interval(p, q)
    return k, lo, hi

def margin_interval(logdata, A, B):
    k, lo, hi = logdata
    kdiff = B*k-A
    low = B*lo + kdiff*(LOG2[0] if kdiff >= 0 else LOG2[1])
    high = B*hi + kdiff*(LOG2[1] if kdiff >= 0 else LOG2[0])
    return low, high, B*SCALE

def write(obj, path=PART):
    path.write_text(json.dumps(obj, separators=(',', ':')), encoding='utf-8')

def worker():
    started = time.perf_counter()
    states = [(a, 0) for a in range(-3, 4)]
    for h, aa in [(1, range(-4, 2)), (2, range(-3, 0)), (3, range(-3, -1))]:
        for a in aa:
            states.extend([(a, h), (-a, -h)])
    states = sorted(states)
    assert len(states) == len(set(states)) == 29
    idx = {s:i for i,s in enumerate(states)}
    zero = idx[(0,0)]
    matrices, edges = {}, {}
    for e in [-1,0,1]:
        mat = [[0]*29 for _ in states]
        edge = [[] for _ in states]
        for i,(a,h) in enumerate(states):
            for eta,w in [(-1,1),(0,2),(1,1)]:
                delta=e-eta
                target=(h-a-delta,a+delta)
                if target in idx:
                    j=idx[target]
                    mat[i][j] += w
                    edge[i].append((j,w))
        matrices[str(e)] = mat
        edges[e] = edge
    def transfer(word):
        v={zero:1}
        for e in word:
            nxt=defaultdict(int)
            for i,value in v.items():
                for j,w in edges[e][i]:
                    nxt[j] += value*w
            v=nxt
        return v.get(zero,0)
    data={'schema': 'golden-c1-v1', 'status': 'running', 'input': {'ascending_polynomial': [-1, -1, 1], 'degree': 2, 'windows': list(range(5, 19)), 'digits': [-1, 0, 1], 'numerator_weights': [1, 2, 1], 'probability_denominator': 4}, 'interval_method': {'terms': TERMS, 'scale': SCALE, 'log2_interval': list(LOG2), 'tail_numerator': 9, 'tail_denominator': 1028 * 3 ** 257}, 'carry_states': [list(s) for s in states], 'zero_index': zero, 'carry_matrices': matrices, 'records': [], 'failures': [], 'undecided': []}
    write(data)
    # Forward exact convolution retains a representative, never substitutes it for count.
    dist={(0,0):(1,())}
    cols=[]
    col=(1,0)
    QA=QB=QC=0
    F=[0,1]
    for j in range(2,20): F.append(F[-1]+F[-2])
    for b in range(1,19):
        cols.append(col)
        QA += col[0]**2; QB += col[0]*col[1]; QC += col[1]**2
        nxt={}
        for (a,h),(count,word) in dist.items():
            for digit,w in [(-1,1),(0,2),(1,1)]:
                key=(a+digit*col[0],h+digit*col[1])
                if key in nxt:
                    old,oldword=nxt[key]
                    nxt[key]=(old+count*w,oldword)
                else:
                    nxt[key]=(count*w,word+(digit,))
        dist=nxt
        col=(col[1],col[0]+col[1])
        if b<5: continue  # internal construction only; old scopes not recertified
        assert sum(v[0] for v in dist.values())==4**b
        Aform=1+F[b-2]*F[b-1]
        Bform=F[b-1]**2+((-1)**(b-1)-1)//2
        Cform=F[b-1]*F[b]
        assert (QA,QB,QC)==(Aform,Bform,Cform)
        determinant=QA*QC-QB*QB
        central=dist[(0,0)][0]
        assert transfer((0,)*b)==central
        logcache={c:log_ratio_interval(central,c) for c in {v[0] for v in dist.values()}}
        rows=[]; classes={}; equalities=[]; failures=[]; undecided=[]
        for (a,h),(count,word) in sorted(dist.items()):
            assert dist[(-a,-h)][0]==count
            assert transfer(word)==count
            assert sum(word[j]*cols[j][0] for j in range(b))==a
            assert sum(word[j]*cols[j][1] for j in range(b))==h
            numerator=QC*a*a-2*QB*a*h+QA*h*h
            common=gcd(numerator,determinant)
            en,ed=numerator//common,determinant//common
            low,high,den=margin_interval(logcache[count],en,ed)
            if (a,h)==(0,0):
                status='equality'; equalities.append([a,h])
                assert en==0 and count==central
            elif low>0: status='strict-pass'
            elif high<0:
                status='strict-failure';failures.append([a,h])
            else:
                status='undecided';undecided.append([a,h])
            rows.append([a,h,count,en,ed,list(word),status])
            old=classes.get(count)
            if old is None or en*old['energy'][1]>old['energy'][0]*ed:
                classes[count]={'count':count,'energy':[en,ed],'endpoint':[a,h],
                                'word':list(word),'log_ratio_data':list(logcache[count]),
                                'margin_interval':[low,high,den], 'status':status}
        record={'window': b, 'rank': 2, 'nullity': b - 2, 'columns': [list(x) for x in cols], 'gram': [[QA, QB], [QB, QC]], 'determinant': determinant, 'central_count': central, 'probability_denominator': 4 ** b, 'endpoint_count': len(rows), 'normalization': sum((v[0] for v in dist.values())), 'class_count': len(classes), 'classes': [classes[c] for c in sorted(classes)], 'rows_schema': ['a', 'h', 'count', 'energy_numerator', 'energy_denominator', 'word', 'status'], 'rows': rows, 'equality_endpoints': equalities, 'failure_endpoints': failures, 'undecided_endpoints': undecided, 'all_carry_counts_checked': True}
        data['records'].append(record)
        data['failures'].extend([[b,*x] for x in failures])
        data['undecided'].extend([[b,*x] for x in undecided])
        pass
        write(data)
    data['status']='complete'
    pass
    write(data)

def main():
    if '--worker' in sys.argv:
        worker(); return
    start=time.perf_counter()
    process=subprocess.Popen([sys.executable, str((_J_PROGRAM / 'profile.py')), '--worker'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    timed_out=False
    try:
        stdout,stderr=process.communicate(timeout=CAP)
    except subprocess.TimeoutExpired:
        timed_out=True;process.kill();stdout,stderr=process.communicate()
    elapsed=time.perf_counter()-start
    data=json.loads(PART.read_text(encoding='utf-8')) if PART.exists() else {'records':[]}
    pass
    if timed_out: data['status']='incomplete-timeout'
    elif process.returncode: data['status']='failed-worker'
    if data["status"] == "complete":
        write(data)
        PART.replace(OUT)
    else:
        write(data)
    print(json.dumps({'status':data['status'],'completed_windows':len(data['records']),
                      'endpoint_count':sum(r['endpoint_count'] for r in data['records']),
                      'failures':len(data.get('failures',[])),
                      'undecided':len(data.get('undecided',[])), 'wall_seconds':elapsed}))
    return 0 if data['status']=='complete' else 1

if __name__=='__main__':
    raise SystemExit(main())
