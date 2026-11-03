"""Complete independent power classification by modular binary exponentiation.

Own quotient-Gram/serialization helpers reused explicitly; no author imports.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from math import gcd
import importlib.util,json,time,traceback,sys,subprocess,platform
import sympy as sp
HERE=(_J_PROGRAM / 'power-classification-review.py').parent
OUT=(_J_OUTPUT / 'power-classification-review-result.json')
CAP=30
spec=importlib.util.spec_from_file_location('own_prior',(_J_PROGRAM / 'nonmonomial-norm-review.py'))
own=importlib.util.module_from_spec(spec);spec.loader.exec_module(own)
same,enc,conv=own.same,own.enc,own.conv

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


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def mulmod(a,b,p): return own.remainder(conv(a,b),p)

def power(base,k,p):
    v=[1]+[0]*(len(p)-2)
    while k:
        if k&1: v=mulmod(v,base,p)
        base=mulmod(base,base,p);k//=2
    return v

def quotient_from_constant(a,p):
    d=len(p)-1; size=max(1,len(a)-d); u=[]
    for i in range(size):
        value=(a[i] if i<len(a) else 0)-sum(p[j]*u[i-j] for j in range(1,min(i,d)+1))
        assert value%p[0]==0;u.append(value//p[0])
    assert trim(conv(u,p))==trim(a)
    return trim(u)

def record(r,src):
    n=r['n'];p,d,N,q,C,cols,_,_,_=own.build(n)
    assert (n,d,N) in ((18,20,40),(30,32,64)) and src['n']==n
    K=4*N;one=[1]+[0]*(d-1);t=[0,1]+[0]*(d-2)
    tinv=[-p[j+1]//p[0] for j in range(d)]
    assert mulmod(t,tinv,p)==one and all(-p[j+1]%p[0]==0 for j in range(d))
    powers={k:power(t if k>=0 else tinv,abs(k),p) for k in range(-K,K+1)}
    assert len({tuple(v) for v in powers.values()})==2*K+1
    tables=[{'k':k,'coefficients':powers[k]} for k in range(-K,K+1)]
    U=src['U_rows'];Ui=src['U_inverse_rows']
    assert sp.Matrix(U)*sp.Matrix(Ui)==sp.eye(d) and sp.Matrix(Ui)*sp.Matrix(U)==sp.eye(d)
    T=sp.Symbol('t'); P=sp.Poly.from_list(p[::-1],T,domain=sp.ZZ)
    candidates=[]
    for j in range(3*d-2):
        if j<d:kind,idx,sgn='basis',j,0
        else:kind,idx,sgn='adjacent',(j-d)//2,(-1 if (j-d)%2==0 else 1)
        z=[U[idx][a]+(sgn*U[idx+1][a] if sgn else 0) for a in range(d)]
        b=z+[0]*(N-d);f=[sum(row[a]*b[a] for a in range(N)) for row in C]
        nb=int(sp.resultant(P,sp.Poly.from_list(z[::-1],T,domain=sp.ZZ)))
        assert nb!=0
        e=Q(sum(x*x for x in f),q*q); c=gcd(*f)
        for key,value in [('kind',kind),('basis_index',idx),('sign',sgn),('z',z),('B',b),
                          ('F_coefficients',f),('signed_res_B',nb),('content',c),('e_B',enc(e))]:
            same(src['candidates'][j][key],value,f'parent/{n}/{j}/{key}')
        positive=[z==powers[k] for k in range(-K,K+1)]
        negative=[z==[-a for a in powers[k]] for k in range(-K,K+1)]
        matches=[]
        for k in range(-K,K+1):
            for sign,truth in ((1,positive[k+K]),(-1,negative[k+K])):
                if not truth:continue
                if k>=0:
                    a=[0]*max(k+1,d);a[k]=1
                    for h,x in enumerate(z):a[h]-=sign*x
                else:
                    a=[0]*(-k+d);a[0]=-sign
                    for h,x in enumerate(z):a[h-k]+=x
                a=trim(a);u=quotient_from_constant(a,p)
                matches.append({'k':k,'sign':sign,'identity_coefficients':a,'quotient_coefficients':u})
                # Matching low-window powers give the very original projected column.
                assert 0<=k<N and f==[sign*x for x in cols[k]] and abs(nb)==1
        assert len(matches)<=1
        candidates.append({'source_index':j,'kind':kind,'basis_index':idx,'sign':sgn,'z':z,'B':b,
            'F_coefficients':f,'signed_res_B':nb,'content':c,'e_B':enc(e),
            'equal_positive':positive,'equal_negative':negative,'matches':matches,'bounded_match':bool(matches)})
    matched=[c['source_index'] for c in candidates if c['matches']]
    exp={'n':n,'d':d,'N':N,'q':q,'coefficients':p,'k_min':-K,'k_max':K,'power_table':tables,
         'candidates':candidates,'candidate_count':len(candidates),'matched_indices':matched,
         'unmatched_indices':[c['source_index'] for c in candidates if not c['matches']],
         'matched_exponents':[{'index':c['source_index'],'k':c['matches'][0]['k'],'sign':c['matches'][0]['sign']} for c in candidates if c['matches']]}
    same(r,exp,f'whole/{n}')
    assert len(matched)==(11 if n==18 else 20)
    if n==18:
        z=candidates[17]['z']
        assert sum(p[j]*(-1)**j for j in range(d+1))==19
        assert sum(z[::2])==-123 and sum(z[1::2])==268
        assert sum(z[j]*(-1)**j for j in range(d))==-391
        assert (-391)%19==8 not in (1,18) and candidates[17]['signed_res_B']==1
        assert candidates[17]['matches']==[]
    return {'n':n,'powers':len(tables),'signed_comparisons':2*len(tables)*len(candidates),
            'quotients':len(matched),'matched_exponents':exp['matched_exponents'],
            'all_copied_arithmetic_fields_recomputed':True,'all_schema_fields_checked':True}

def worker(output):
    start=time.perf_counter()
    names=['power-classification-author.py','power-classification-output.json','residual-lattice-output.json','nonmonomial-norm-review.py']
    before={name:(((_J_PROGRAM if name in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / name)).read_bytes() for name in names}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0214.md'); db=draft.read_bytes() if draft.exists() else None
    report={'schema': 'J79-signed-power-independent-review-v1', 'records': []}
    try:
        a=json.loads(before['power-classification-output.json']);parent=json.loads(before['residual-lattice-output.json'])
        expectedkeys={'schema', 'status', 'input', 'domain_n', 'power_bound_multiplier', 'records', 'actual_worker_exit_code', 'outer_timed_out'}
        assert set(a)==expectedkeys and len(a['records'])==2 and parent['status']=='complete'
        provenance=[]
        same({k: v for k, v in a.items() if k not in provenance + ['records']}, {'schema': 'J79-exact-signed-power-classification-v1', 'status': 'complete', 'input': 'residual-lattice-output.json', 'domain_n': [18, 30], 'power_bound_multiplier': 4, 'actual_worker_exit_code': 0, 'outer_timed_out': False}, 'metadata')
        pass
        pass
        assert all((type(a[k]) is float and 0 < a[k] < CAP for k in ()))
        for r,p in zip(a['records'],parent['records']):
            assert time.perf_counter()-start<CAP
            report['records'].append(record(r,p))
        assert sum(r['powers'] for r in report['records'])==834
        assert sum(r['signed_comparisons'] for r in report['records'])==133680
        assert sum(r['quotients'] for r in report['records'])==31
        report.update(status='passed', exact_scalar_comparisons=own.COUNT, all_integer_exponent_mod19_written_control_checked=True, author_replayed=False)
    except BaseException as exc:
        report.update(status='failed',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass
    pass
    pass;pass
    with output.open('x',encoding='utf8') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ('records',)}))
    return 0 if report['status']=='passed' else 1

if __name__=='__main__':
    if '--output' in sys.argv:OUT=Path(sys.argv[sys.argv.index('--output')+1]).resolve()
    if '--worker' in sys.argv:sys.exit(worker(OUT))
    if OUT.exists():raise SystemExit('Preserve first independent report')
    start=time.perf_counter()
    p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'power-classification-review.py')),'--worker','--output',str(OUT)],creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    try:code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        p.kill();p.wait();code=1
        if not OUT.exists():OUT.write_text(json.dumps({'status': 'incomplete', 'error': 'outer30secondcap'}) + '\n')
    sys.exit(code)
