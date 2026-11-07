"""Whole D213 native checker: no author imports, full convolution and integer log bounds."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
import argparse,json,platform,subprocess,sys,time,traceback
HERE=(_J_PROGRAM / 'nonlinear-bound-review.py').parent
CAP=30;GRID=1<<32;ELL=1<<20;LEAVES=0
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


def enc(x):return [x.numerator,x.denominator]
def dec(x):return F(*x)
def vec(x):return [enc(v) for v in x]
def same(a,b,path=''):
    global LEAVES
    assert type(a) is type(b),(path,type(a),type(b))
    if isinstance(a,dict):
        assert set(a)==set(b),(path,set(a)^set(b))
        for k in a:same(a[k],b[k],path+'/'+k)
    elif isinstance(a,list):
        assert len(a)==len(b),(path,len(a),len(b))
        for i,(x,y) in enumerate(zip(a,b)):same(x,y,path+'/'+str(i))
    else:assert a==b,(path,a,b);LEAVES+=1
def series(x):
    assert 0<=x<=F(1,3)
    low=[];up=[]
    for j in range(32):
        num=2*GRID*pow(x.numerator,2*j+1);den=(2*j+1)*pow(x.denominator,2*j+1)
        q,r=divmod(num,den);assert q*den<=num<(q+1)*den
        low.append(q);up.append(q+int(r>0))
    return {'x':enc(x),'lower_term_numerators':low,'upper_term_numerators':up,
            'lower_numerator':sum(low),'upper_numerator':sum(up)+1,'denominator':GRID,'tail_upper_grid_units':1}
def logcert(D,d,l2):
    if D==1:return {'D':D,'d':d,'exact_zero':True,'ell_lower':[0,1],'ell_upper':[0,1],'log_lower':[0,1],'log_upper':[0,1]}
    k=D.bit_length()-1;r=F(D,1<<k);assert 1<=r<2
    sr=series((r-1)/(r+1));lo=F(k*l2['lower_numerator']+sr['lower_numerator'],GRID);hi=F(k*l2['upper_numerator']+sr['upper_numerator'],GRID)
    l=(lo/d*ELL).__floor__();u=(hi/d*ELL).__ceil__()
    return {'D':D,'d':d,'exact_zero':False,'binary_exponent':k,'range_reduced':enc(r),'series':sr,
            'log_lower':enc(lo),'log_upper':enc(hi),'ell_lower':enc(F(l,ELL)),'ell_upper':enc(F(u,ELL))}
def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def solve_fixed(rows,rhs):
    n=len(rows)
    assert n==len(rhs) and all(len(row)==n for row in rows)
    matrix=[[F(x) for x in row]+[F(b)] for row,b in zip(rows,rhs)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if matrix[i][col])
        matrix[col],matrix[pivot]=matrix[pivot],matrix[col]
        scale=matrix[col][col]
        matrix[col]=[x/scale for x in matrix[col]]
        for i in range(n):
            if i!=col:
                scale=matrix[i][col]
                matrix[i]=[x-scale*y for x,y in zip(matrix[i],matrix[col])]
    values=[row[-1] for row in matrix]
    assert all(sum(a*b for a,b in zip(row,values))==v for row,v in zip(rows,rhs))
    return values

def fixed_record():
    # This checker forms its own matrices and both reconstruction systems.
    # It imports no author program, solver or upstream generated output.
    from math import gcd
    fixed=json.loads((_J_PROGRAM/'inputs/joint-budget-n18.json').read_text())
    assert fixed['format']=='joint-budget-n18-v1'
    assert fixed['source_family']=='unit-cap-certificates.json' and fixed['source_input']=='P20'
    assert [fixed[k] for k in ('n','d','N','q')]==[18,20,40,36887312]
    source=json.loads((_J_PROGRAM/'inputs/unit-cap-certificates.json').read_text())
    selected=[r for r in source['inputs'] if r['name']=='P20'];assert len(selected)==1
    raw=selected[0];q=raw['q'];P=raw['P'];assert q==36887312 and len(P)==21
    family=[];l2=series(F(1,3))
    assert len(raw['columns'])==98
    for j,column in enumerate(raw['columns']):
        B,f,U=column['B'],column['F'],column['U']
        assert len(B)==len(f)==40 and len(U)==20
        assert [q*b-a for b,a in zip(B,f)]==conv(P,U)
        assert all(sum(f[k+i]*P[i] for i in range(21))==0 for k in range(20))
        assert gcd(*f)==column['content_F'] and type(column['norm_B']) is int and column['norm_B']!=0
        if j<40:assert B==[int(k==j) for k in range(40)] and column['norm_B']==1
        D=abs(column['norm_B']);aut=conv(f,f[::-1]);cert=None if j<40 else logcert(D,20,l2)
        meta={'kind':'monomial' if j<40 else 'frozen_residue','index':j if j<40 else j-40}
        if j>=40:
            k=j-40
            meta.update(seed_kind='basis' if k<20 else 'adjacent',basis_index=k if k<20 else (k-20)//2,
                seed_sign=0 if k<20 else (-1 if (k-20)%2==0 else 1),z=B[:20])
        ell_value=F(0) if cert is None else dec(cert['ell_lower'])
        norm=column['norm_B'];content=column['content_F'];full=q**20*norm
        assert full%content**20==0
        family.append(dict(meta,B=B,F_coefficients=f,kernel_multiplier=U,signed_res_B=norm,signed_res_F=full,
            content=content,e=enc(F(aut[39],q*q)),h=vec([F(x,q*q) for x in aut[40:]]),
            ell=enc(ell_value),D=D,log_certificate=cert,integer_energy=aut[39],integer_autocorrelations=aut[40:],
            a=enc(1+2*ell_value),primitive_coefficients=[x//content for x in f],
            signed_res_primitive=full//content**20,actual_degree=max(k for k,x in enumerate(f) if x)))
    e=[dec(c['e']) for c in family];ell=[dec(c['ell']) for c in family];aa=[1+2*x for x in ell]
    H=[[dec(c['h'][h]) for c in family] for h in range(39)]
    compressed=list(range(20))+list(range(40,98));ep=[e[j]/aa[j] for j in compressed]
    hp=[[row[j]/aa[j] for j in compressed] for row in H]
    support=fixed['compressed_support'];zero=fixed['zero_lags']
    assert support==[0,1,2,15,16,17,36,37,42,45,55,66,75]
    assert zero==[1,2,9,10,11,15,20,24,30,35,38]
    rows=[[ep[j] for j in support],[F(1)]*13]+[[hp[h-1][j] for j in support] for h in zero]
    values=solve_fixed(rows,[F(1),F(2)]+[F(0)]*11)
    uc=[F(0)]*len(compressed)
    for j,x in zip(support,values):uc[j]=x
    v=[F(0)]*98
    for j,x in zip(compressed,uc):
        if j<20:v[j]=v[39-j]=x/2
        else:v[j]=x/aa[j]
    corr=[sum(x*y for x,y in zip(row,v)) for row in H]
    assert [h+1 for h,x in enumerate(corr) if not x]==zero
    y=[dec(x) for x in fixed['y']];assert len(y)==39 and all(abs(x)<=1 for x in y)
    free=[h-1 for h in zero]
    assert all(y[h]==(1 if x>0 else -1) for h,x in enumerate(corr) if x)
    dr=[[2*hp[h][j] for h in free]+[-ep[j],F(-1)] for j in support]
    db=[-sum(2*hp[h][j]*y[h] for h in range(39) if h not in free) for j in support]
    dual=solve_fixed(dr,db);assert dual[:-2]==[y[h] for h in free]
    lam,mu=dual[-2:];assert enc(lam)==fixed['lambda_value'] and enc(mu)==fixed['mu'] and mu>0
    slacks=[2*sum(y[h]*H[h][j] for h in range(39))-lam*e[j]-mu*aa[j] for j in range(98)]
    K=2*sum(map(abs,corr))
    assert min(v)>=0 and sum(x*y for x,y in zip(e,v))==1
    assert sum(x*y for x,y in zip(aa,v))==2 and min(slacks)>=0
    assert all(x*y==0 for x,y in zip(v,slacks)) and K==lam+2*mu
    return {'n':18,'d':20,'N':40,'q':q,'coefficients':P,'status':'complete',
        'global_finite_family_optimum_certified':True,'family':family,'v':vec(v),'y':vec(y),
        'lambda_value':enc(lam),'mu':enc(mu),'dual_slacks':vec(slacks),'kappa':enc(K),'S':enc(sum(v)),
        'compressed_indices':compressed,'r_prime':vec(ep),'H_prime':[vec(row) for row in hp],
        'compressed_u':vec(uc),'correlations':vec(corr)}

def worker(output):
    start=time.perf_counter();report={'schema': 'J79-nonlinear-independent-review-v1'}
    paths=[(_J_OUTPUT / 'nonlinear-bound-output.json')]
    old={p.name:p.read_bytes() for p in paths};draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0213.md');db=draft.read_bytes() if draft.exists() else None
    try:
        observed=json.loads(old['nonlinear-bound-output.json']);r=fixed_record()
        assert r['status']=='complete' and r['global_finite_family_optimum_certified']
        family=r['family'];assert len(family)==98
        q=r['q'];q2=q*q;energies=[];columns=[];logs=[];lower=[];upper=[];l2=series(F(1,3));tail=F(9,260*3**65);assert tail<F(1,GRID)
        assert r['d']==20 and r['N']==40
        for j,c in enumerate(family):
            f=c['F_coefficients'];assert len(f)==40 and all(type(x) is int for x in f)
            aut=conv(f,list(reversed(f)));en=F(aut[39],q2);h=[F(x,q2) for x in aut[40:]]
            same(enc(en),c['e']);same(vec(h),c['h']);assert en>0
            cert=None if c['log_certificate'] is None else logcert(c['D'],20,l2)
            same(cert,c['log_certificate']);ell=F(0) if cert is None else dec(cert['ell_lower']);eu=F(0) if cert is None else dec(cert['ell_upper'])
            if cert is None:assert c['D']==1
            same(enc(ell),c['ell']);assert 0<=ell<=eu
            energies.append(en);columns.append(h);logs.append(cert);lower.append(ell);upper.append(eu)
        H=[list(row) for row in zip(*columns)];err=[b-a for a,b in zip(lower,upper)];eps=max(err)
        y=list(map(dec,r['y']));lam=dec(r['lambda_value']);mu=dec(r['mu']);assert len(y)==39 and mu>=0 and all(abs(x)<=1 for x in y)
        slack=[2*sum(a*b for a,b in zip(y,col))-lam*en-mu*(1+2*ell) for col,en,ell in zip(columns,energies,lower)]
        assert min(slack)>=0;same(vec(slack),r['dual_slacks'])
        # Verify the actual upper witness against reconstructed full coefficient correlations.
        v=list(map(dec,r['v']));assert len(v)==98 and min(v)>=0
        assert sum(a*b for a,b in zip(v,energies))==1
        S=sum(v);L=sum(a*b for a,b in zip(v,lower));assert S+2*L>=2
        corr=[sum(v[j]*H[h][j] for j in range(98)) for h in range(39)];kap=2*sum(map(abs,corr));same(enc(kap),r['kappa']);assert kap==lam+2*mu
        A=1/max(energies);B=1/min(energies);width=(B-A)/32
        expect={'schema': 'J79-full-nonlinear-cell-bound-v1', 'status': 'complete', 'input': 'inputs/joint-budget-n18.json', 'input_n': 18, 'cell_count': 32, 'log_terms': 32, 'log_grid': GRID, 'ell_grid': ELL, 'cells': [], 'd': 20, 'N': 40, 'q': q, 'coefficients': r['coefficients'], 'family_count': 98, 'family_labels': [{'kind': c['kind'], 'index': c['index'], 'D': c['D']} for c in family], 'e': vec(energies), 'ell_lower': vec(lower), 'ell_upper': vec(upper), 'ell_errors': vec(err), 'epsilon': enc(eps), 'max_error_indices': [j for j, x in enumerate(err) if x == eps], 'norm_log_certificates': logs, 'y': vec(y), 'lambda_value': enc(lam), 'mu': enc(mu), 'H_rows': [vec(row) for row in H], 'dual_slacks': vec(slack), 'A': enc(A), 'B': enc(B), 'width': enc(width), 'max_energy_indices': [j for j, x in enumerate(energies) if x == max(energies)], 'min_energy_indices': [j for j, x in enumerate(energies) if x == min(energies)], 'log2_certificate': l2, 'tail_upper': enc(tail)}
        for i in range(32):
            assert time.perf_counter()-start<CAP
            a=A+(B-A)*F(i,32);b=A+(B-A)*F(i+1,32);z=b/2
            nn=logcert(z.numerator,1,l2);dd=logcert(z.denominator,1,l2)
            bl=dec(nn['log_lower'])-dec(dd['log_upper']);bu=dec(nn['log_upper'])-dec(dd['log_lower']);t=bu+2*eps
            ends=[t*a,t*b];mx=ends[0] if t<=0 else ends[1];bc=a+max(F(0),-mx)
            expect['cells'].append({'index':i,'a':enc(a),'b':enc(b),'b_over_two':enc(z),'numerator_log_certificate':nn,'denominator_log_certificate':dd,
                'beta_lower':enc(bl),'beta_upper':enc(bu),'t':enc(t),'t_sign':(t>0)-(t<0),'t_times_a':enc(ends[0]),'t_times_b':enc(ends[1]),'endpoint_max':enc(mx),
                'max_endpoint_indices':[j for j,x in enumerate(ends) if x==mx],'mass_only_bound':enc(a),'budget_bound':enc(a-mx),'budget_mass_lower':enc(bc),'kappa_lower':enc(lam+mu*bc)})
        bounds=[dec(c['kappa_lower']) for c in expect['cells']];raw=min(bounds);clipped=max(F(0),raw);assert clipped<=kap
        expect.update(raw_lower_bound=enc(raw),full_nonlinear_lower_bound=enc(clipped),minimizing_cells=[j for j,x in enumerate(bounds) if x==raw],
            signs_count={str(s):sum(c['t_sign']==s for c in expect['cells']) for s in [-1,0,1]},positive_lower_bound=clipped>0,
            lower_ten_thousandth_bin=[int(clipped*10000),int(clipped*10000)+1],actual_feasible_upper=enc(kap),strict_interval=clipped<kap,
            input_budget_surplus_used='exact full nonlinear, threshold half log2',degree_bound=39,radial_multiplier=[39,20])
        meta=['actual_worker_exit_code', 'outer_timed_out']
        assert set(observed)==set(expect)|set(meta)
        pass
        pass
        assert type(observed['actual_worker_exit_code']) is int and observed['actual_worker_exit_code']==0
        assert observed['outer_timed_out'] is False
        for k in []:assert type(observed[k]) is float and 0<=observed[k]<=CAP
        pass
        same(expect,{k:v for k,v in observed.items() if k not in meta})
        report.update(status='passed',exact_scalar_comparisons=LEAVES,directions=98,cells=32,complete_polynomial_convolutions=98,
            full_correlations=3822,integer_log_certificates=64+sum(x is not None for x in logs),all_schemas_checked=True,
            lower_bound=enc(clipped),upper_witness=enc(kap),signs=expect['signs_count'],minimizing_cells=expect['minimizing_cells'],
            prior_norm_irreducibility_scope='L344 accepted full native review, not a new resultant or modular rerun',
            method='full integer polynomial autocorrelation and direct integer log-term inequalities; sign-separated endpoint bound; no author imports')
    except BaseException:report.update(status='failed',traceback=_record_text(traceback.format_exc()),exact_scalar_comparisons=LEAVES)
    pass
    pass
    pass;pass
    output.write_text(json.dumps(report,indent=2),encoding='utf-8')
    return 0 if report['status']=='passed' else 1
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--worker',action='store_true');ap.add_argument('--output',type=Path,default=(_J_OUTPUT / 'nonlinear-bound-review-result.json'));args=ap.parse_args();p=args.output.resolve();assert p.parent == _J_OUTPUT
    if args.worker:return worker(p)
    if p.exists():raise FileExistsError(p)
    proc=subprocess.Popen([sys.executable,__file__,'--worker','--output',str(p)],creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    try:return proc.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        proc.kill();proc.wait();p.write_text(json.dumps({'status': 'timeout-incomplete'}), encoding='utf-8');return 1
if __name__=='__main__':raise SystemExit(main())
