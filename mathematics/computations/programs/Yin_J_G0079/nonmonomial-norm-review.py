"""Complete independent reconstruction of both declared 600-direction passes.

No author imports. Quotient row Gram, integer norm matrices, convolution and
independent aggregate coefficient sums are the mathematical inputs.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from math import gcd, lcm
from datetime import datetime
import json, time, traceback, platform, sys, subprocess
import sympy as sp

HERE = (_J_PROGRAM / 'nonmonomial-norm-review.py').parent
OUT = (_J_OUTPUT / 'nonmonomial-norm-review-result.json')
CAP = 180
COUNT = 0
START = None

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


def same(a, b, path):
    global COUNT
    if isinstance(b, dict):
        assert type(a) is dict and set(a) == set(b), (path, set(a), set(b))
        for k in b: same(a[k], b[k], path+'/'+k)
    elif isinstance(b, list):
        assert type(a) is list and len(a) == len(b), (path, len(a), len(b))
        for j, (x, y) in enumerate(zip(a,b)): same(x,y,path+'/'+str(j))
    else:
        assert type(a) is type(b) and a == b, (path,a,b)
        COUNT += 1

def enc(x):
    x=Q(x)
    return [x.numerator,x.denominator]
def seq(v): return [enc(x) for x in v]
def dec(x):
    assert type(x) is list and len(x)==2 and all(type(y) is int for y in x)
    assert x[1]>0 and gcd(*x)==1
    return Q(*x)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def correlations(a): return conv(a,a[::-1])[len(a):]
def remainder(a,p):
    a=list(a)+[0]*max(0,len(p)-1-len(a))
    for i in range(len(a)-1,len(p)-2,-1):
        x=a[i]
        for j,y in enumerate(p): a[i-len(p)+1+j]-=x*y
    return a[:len(p)-1]
def inverse(rows):
    # Fraction-free DomainMatrix inversion, rather than author's row Gauss--Jordan.
    m=sp.Matrix(rows).inv(method='DM')
    return [[Q(m[i,j]) for j in range(m.cols)] for i in range(m.rows)]

def build(n):
    d=n+2; N=2*d
    parent=[0]*(n+4)
    for j,x in [(0,1),(2,-1),(3,-1),(n,-1),(n+1,-1),(n+3,1)]: parent[j]+=x
    p=[parent[0]]
    for j in range(1,d+1): p.append(parent[j]-p[-1])
    assert conv(p,[1,1])==parent and p==p[::-1]
    powers=[]
    v=[1]+[0]*(d-1)
    for j in range(N):
        powers.append(v)
        v=remainder([0]+v,p)
    W=sp.Matrix(d,N,lambda i,j:powers[j][i])
    R=W.T*(W*W.T).inv(method='DM')*W
    q=lcm(*(int(x.q) for x in R))
    C=[[int(q*R[i,j]) for j in range(N)] for i in range(N)]
    r=[Q(R[i,i]) for i in range(N)]
    cols=list(map(list,zip(*C)))
    ac=[correlations(c) for c in cols]
    H=[[Q(ac[j][h],q*q) for j in range(N)] for h in range(N-1)]
    assert all(dot(cols[i],cols[j])==q*C[i][j] for i in range(N) for j in range(N))
    assert all(remainder(cols[j],p)==[q*x for x in powers[j]] for j in range(N))
    assert all(r[j]==r[N-1-j] for j in range(N))
    assert all(row[j]==row[N-1-j] for row in H for j in range(N))
    # Multiplication matrices on Q[t]/P; their integer determinants are signed norms.
    norms={}
    for h in (1,2,3):
        shifts=[remainder([0]*h+[0]*j+[1],p) for j in range(d)]
        for s in (-1,1):
            M=sp.Matrix(d,d,lambda i,j:int(i==j)+s*shifts[j][i])
            norms[h,s]=int(M.det(method='domain-ge'))
            assert norms[h,s]!=0
    return p,d,N,q,C,cols,r,H,norms

def series(x):
    # Integer powers/division, with an independently bounded geometric integral tail.
    a,b=x.numerator,x.denominator
    low=[]; high=[]; grid=1<<32
    for j in range(32):
        top=2*grid*a**(2*j+1); bot=(2*j+1)*b**(2*j+1)
        lo,rem=divmod(top,bot)
        low.append(lo); high.append(lo+int(rem!=0))
    assert 0<=x<=Q(1,3)
    tail=2*x**65/(65*(1-x*x))
    assert tail<=Q(9,260*3**65)<Q(1,grid)
    return {'x':enc(x),'lower_term_numerators':low,'upper_term_numerators':high,
            'lower_numerator':sum(low),'upper_numerator':sum(high)+1,
            'denominator':grid,'tail_upper_grid_units':1}

def logcert(D,d):
    if D==1:
        return {'D':1,'d':d,'exact_zero':True,'ell_lower':[0,1],'ell_upper':[0,1],
                'log_lower':[0,1],'log_upper':[0,1]}
    k=0
    while 2**(k+1)<=D: k+=1
    t=Q(D,2**k); cc=series((t-1)/(t+1)); c2=series(Q(1,3))
    lo=Q(k*c2['lower_numerator']+cc['lower_numerator'],1<<32)
    hi=Q(k*c2['upper_numerator']+cc['upper_numerator'],1<<32)
    u=lo*(1<<20)/d; v=hi*(1<<20)/d
    el=Q(u.numerator//u.denominator,1<<20)
    eu=Q(-((-v.numerator)//v.denominator),1<<20)
    return {'D':D,'d':d,'exact_zero':False,'binary_exponent':k,'range_reduced':enc(t),
            'series':cc,'log_lower':enc(lo),'log_upper':enc(hi),'ell_lower':enc(el),'ell_upper':enc(eu)}

def context(n, old):
    p,d,N,q,C,cols,r,H,norms=build(n)
    # The old exact witness is a parameter, checked against ALL reconstructed columns.
    pair=list(map(dec,old['pair_masses'])); y=list(map(dec,old['y']))
    lam=dec(old['lambda']); mu=dec(old['mu'])
    assert len(pair)==d and all(x>=0 for x in pair) and sum(pair)==2
    I=[j for j,x in enumerate(pair) if x]
    a0=[dot(row[:d],pair) for row in H]
    Z=[j for j,x in enumerate(a0) if x==0]
    K0=2*sum(map(abs,a0))
    assert dot(pair,r[:d])==1 and mu>0 and K0==lam+2*mu>4
    assert all(abs(x)<=1 for x in y)
    assert all(not a or y[j]==(1 if a>0 else -1) for j,a in enumerate(a0))
    slacks=[2*dot(y,[row[j] for row in H])-lam*r[j]-mu for j in range(N)]
    assert all(x>=0 for x in slacks) and all(slacks[j]==0 for j in I)
    M=[[Q(1) for j in I],[r[j] for j in I]]+[[H[h][j] for j in I] for h in Z]
    assert len(M)==len(I)
    inv=inverse(M)
    assert all(dot(row,[inv[k][j] for k in range(len(I))])==int(i==j)
               for i,row in enumerate(M) for j in range(len(I)))
    for key,expected in [('coefficients',p),('d',d),('N',N),('q',q),('input_C_rows',C),
                         ('r',seq(r)),('H_rows',[seq(row) for row in H]),
                         ('correlations',seq(a0)),('kappa',enc(K0))]:
        same(old[key],expected,'upstream/'+str(n)+'/'+key)
    return locals()

def seed_data(ctx,h,s,j):
    p,d,N,q,C,cols= [ctx[k] for k in ('p','d','N','q','C','cols')]
    b=[0]*N; b[j]=1; b[j+h]=s
    f=[sum(C[i][k]*b[k] for k in range(N)) for i in range(N)]
    # Quotient coefficients recovered forward using the unit constant coefficient.
    diff=[q*x-y for x,y in zip(b,f)]
    U=[]
    for k in range(N-d): U.append((diff[k]-sum(p[l]*U[k-l] for l in range(1,min(k,d)+1)))//p[0])
    assert conv(p,U)==diff
    c=gcd(*f); primitive=[x//c for x in f]
    ac=correlations(f); E=Q(sum(x*x for x in f),q*q); HB=[Q(x,q*q) for x in ac]
    nb=((-1)**d*p[0])**j*ctx['norms'][h,s]
    nf=q**d*nb
    assert nf%c**d==0 and gcd(*primitive)==1 and E>0
    # Every root-evaluation identity is independently checked in the quotient order.
    assert remainder(f,p)==[q*x for x in remainder(b,p)]
    assert [c*x for x in remainder(primitive,p)]==remainder(f,p)
    g=2*dot(ctx['y'],HB)-ctx['lam']*E-ctx['mu']
    return dict(h=h,s=s,j=j,b=b,f=f,U=U,c=c,primitive=primitive,ac=ac,E=E,HB=HB,nb=nb,nf=nf,g=g)

def step(ctx, sd, ell):
    I,M,inv,H,pair,a0,Z = [ctx[k] for k in ('I','M','inv','H','pair','a0','Z')]
    N,d,q=ctx['N'],ctx['d'],ctx['q']
    rhs=[1+2*ell,sd['E']]+[sd['HB'][h] for h in Z]
    x=[dot(row,rhs) for row in inv]
    assert [dot(row,x) for row in M]==rhs
    da=[sd['HB'][h]-dot(x,[H[h][j] for j in I]) for h in range(N-1)]
    bounds=[('unit',-1,Q(1))]
    if ell: bounds.append(('mass_total',-1,1/(2*ell)))
    bounds += [('mass',j,pair[j]/x[k]) for k,j in enumerate(I) if x[k]>0]
    bounds += [('sign',h+1,-a0[h]/da[h]) for h in range(N-1) if a0[h]*da[h]<0]
    tau=min(row[2] for row in bounds)
    bp=pair.copy()
    for k,j in enumerate(I): bp[j]-=tau*x[k]
    masses=[Q(0)]*N+[tau]
    for j in range(d): masses[j]=masses[N-1-j]=bp[j]/2
    S=sum(masses); weights=[v/S for v in masses]
    L=lcm(*(w.denominator for w in weights)); mult=[int(w*L) for w in weights]
    # Reconstruct final correlation and energy from ALL actual full polynomials.
    aa=[sum(masses[j]*H[h][j] for j in range(N))+tau*sd['HB'][h] for h in range(N-1)]
    en=dot(masses[:-1],[Q(sum(a*a for a in col),q*q) for col in ctx['cols']])+tau*sd['E']
    assert en==1 and S==2-2*ell*tau and S>=1
    assert all(v>=0 for v in masses) and tau>0 and sum(mult)==L
    assert all(aa[h]==a0[h]+tau*da[h] for h in range(N-1))
    assert all(aa[h]==0 for h in Z)
    assert all(not a0[h] or aa[h]*a0[h]>=0 for h in range(N-1))
    K=2*sum(map(abs,aa)); slope=sd['g']-2*ctx['mu']*ell
    assert K==ctx['K0']+tau*slope and slope==2*dot(ctx['y'],da)
    agg=[Q(q*q)*a/S for a in aa]
    return dict(rhs=rhs,x=x,da=da,bounds=bounds,tau=tau,bp=bp,masses=masses,S=S,weights=weights,
                L=L,mult=mult,aa=aa,K=K,slope=slope,agg=agg)

def common(sd,st,ctx):
    return {'h':sd['h'],'s':sd['s'],'j':sd['j'],'B':sd['b'],'F_coefficients':sd['f'],
            'content':sd['c'],'signed_res_B':sd['nb'],'signed_res_F':sd['nf'],
            'signed_res_primitive':sd['nf']//sd['c']**ctx['d'],'e_B':enc(sd['E']),'h_B':seq(sd['HB']),
            'active_rhs':seq(st['rhs']),'old_mass_derivative':seq(st['x']),
            'correlation_derivative':seq(st['da']),
            'step_bounds':[{'kind':a,'index':b,'value':enc(c)} for a,b,c in st['bounds']],
            'tau':enc(st['tau']),'limiting_bounds':[i for i,x in enumerate(st['bounds']) if x[2]==st['tau']],
            'pair_masses_after':seq(st['bp']),'masses':seq(st['masses']),'weights':seq(st['weights']),
            'weight_denominator':st['L'],'multiplicities':st['mult'],
            'positive_weight_indices':[i for i,w in enumerate(st['weights']) if w],
            'correlations_after':seq(st['aa']),'kappa_after':enc(st['K']),
            'strict_improvement':st['K']<ctx['K0'],'kappa_le_4':st['K']<=4,
            'energy_after':enc(Q(ctx['q']**2)/st['S']),
            'aggregate_autocorrelations_after':seq(st['agg']),
            'income':{'log_q_argument':ctx['q'],'log_abs_res_B_argument':abs(sd['nb']),
                      'log_abs_res_B_coefficient':enc(st['tau']/(ctx['d']*st['S']))}}

def review_record(n,old,first,second):
    ctx=context(n,old)
    p,d,N,q,C,r,H,pair,I,Z,a0,K0,y,lam,mu,M,inv=[ctx[k] for k in
        ('p','d','N','q','C','r','H','pair','I','Z','a0','K0','y','lam','mu','M','inv')]
    e1={'n':n,'coefficients':p,'d':d,'N':N,'q':q,'C_rows':C,'r':seq(r),'H_rows':[seq(x) for x in H],
        'old_pair_masses':seq(pair),'old_support':I,'old_zero_lags':[h+1 for h in Z],
        'old_correlations':seq(a0),'old_kappa':enc(K0),'old_y':seq(y),'old_lambda':enc(lam),'old_mu':enc(mu),
        'active_matrix':[seq(x) for x in M],'active_inverse':[seq(x) for x in inv],
        'old_contents':[gcd(*col) for col in ctx['cols']],
        'degree_bound':N-1,'radial_multiplier':enc(Q(N-1,d)),
        'binomial_resultants':[{'h':h,'s':s,'signed':ctx['norms'][h,s]} for h in (1,2,3) for s in (-1,1)],
        'status':'complete'}
    Ds=sorted({abs(x) for x in ctx['norms'].values()})
    logs={D:logcert(D,d) for D in Ds}
    e2={'n':n,'d':d,'N':N,'q':q,'coefficients':p,'first_stage_record_n':n,'original_kappa':enc(K0),
        'original_support':I,'original_zero_lags':[h+1 for h in Z],'original_lambda':enc(lam),'original_mu':enc(mu),
        'log_certificates':[logs[D] for D in Ds],'degree_bound':N-1,'radial_multiplier':enc(Q(N-1,d)),'status':'complete'}
    ks=[[],[]]; gs=[]; decisions=[]; count=0
    for h in (1,2,3):
        for s in (-1,1):
            for j in range(N-h):
                assert time.monotonic()-START<CAP,'aggregate cap reached'
                sd=seed_data(ctx,h,s,j); st=step(ctx,sd,Q(0))
                expect=common(sd,st,ctx)
                expect.update(kernel_multiplier=sd['U'],primitive_coefficients=sd['primitive'],
                              actual_degree=max(i for i,a in enumerate(sd['f']) if a),
                              integer_energy=sum(x*x for x in sd['f']),integer_autocorrelations=sd['ac'],
                              reduced_cost=enc(sd['g']),surplus={'half_log_argument':2,'extra_log_argument':abs(sd['nb']),
                                                               'extra_log_coefficient':enc(st['tau']/(2*d))})
                same(first['candidates'][count],expect,f'first/{n}/{count}')
                ks[0].append(st['K']); gs.append(sd['g'])
                cert=logs[abs(sd['nb'])]; ell=dec(cert['ell_lower']); upper=dec(cert['ell_upper'])
                st=step(ctx,sd,ell); lo=sd['g']-2*mu*upper; hi=st['slope']
                decision='negative' if hi<0 else 'nonnegative' if lo>=0 else 'undecided'
                expect=common(sd,st,ctx)
                expect.update(first_stage_candidate_index=count,ell_lower=enc(ell),ell_upper=enc(upper),
                              old_reduced_cost=enc(sd['g']),chosen_slope=enc(hi),
                              exact_log_slope_interval=[enc(lo),enc(hi)],exact_log_slope_decision=decision,S=enc(st['S']),
                              surplus={'half_log_argument':enc(st['S']),'extra_log_argument':abs(sd['nb']),
                                       'extra_log_coefficient':enc(st['tau']/(d*st['S'])),
                                       'x_in_finite_interval_proof':enc(ell*st['tau']),'at_least_half_log_two':True})
                assert 0<=ell*st['tau']<=Q(1,2)
                same(second['candidates'][count],expect,f'second/{n}/{count}')
                ks[1].append(st['K']); decisions.append(decision); count+=1
    assert count==2*sum(N-h for h in (1,2,3))
    assert len(first['candidates'])==len(second['candidates'])==count
    for idx,e in enumerate((e1,e2)):
        e.update(best_candidate_index=min(range(count),key=lambda i:ks[idx][i]),
                 strict_improvement_count=sum(k<K0 for k in ks[idx]),kappa_le_4_count=sum(k<=4 for k in ks[idx]))
    e1['negative_reduced_cost_count']=sum(g<0 for g in gs)
    e2['exact_log_slope_counts']={s:decisions.count(s) for s in ('negative','nonnegative','undecided')}
    same({k:v for k,v in first.items() if k!='candidates'},e1,f'first/{n}/record')
    same({k:v for k,v in second.items() if k!='candidates'},e2,f'second/{n}/record')
    assert all(g>=0 for g in gs) and all(s=='nonnegative' for s in decisions)
    return {'n':n,'d':d,'N':N,'q':q,'candidates_each_pass':count,'signed_norms':sorted(set(ctx['norms'].values())),
            'first_negative_reduced_costs':sum(g<0 for g in gs),'second_exact_log_decisions':e2['exact_log_slope_counts'],
            'strict_improvements':[sum(k<K0 for k in kk) for kk in ks],'all_complete_fields_checked':True}

def worker():
    global START
    START=time.monotonic()
    names=['nonmonomial-author.py','nonmonomial-output.json','norm-funded-author.py','norm-funded-output.json']
    snapshot={n:(((_J_PROGRAM if n in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / n)).read_bytes() for n in names}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0203.md')
    before=draft.read_bytes() if draft.exists() else None
    out={'schema': 'J79-full-two-pass-independent-review-v1', 'domain': 'Both complete original 600-seed semantic passes; no domain expansion', 'records': []}
    try:
        a=json.loads(snapshot[names[1]]); b=json.loads(snapshot[names[3]])
        provenance=[]
        for native in (a,b):
            pass
            pass
            assert all(type(native[k]) is float and 0<native[k]<120 for k in provenance[-2:])
        e1={'schema': 'J79-nonmonomial-escape-v1', 'status': 'complete', 'domain': {'n': [18, 30], 'h': [1, 2, 3], 's': [-1, 1], 'j': 'every integer 0<=j<N-h', 'counts': [228, 372]}, 'input': 'fast-optimum-result.json', 'actual_worker_exit_code': 0, 'outer_timed_out': False}
        e2={'schema': 'J79-norm-funded-residue-v1', 'status': 'complete', 'input': 'nonmonomial-output.json', 'domain_n': [18, 30], 'counts': [228, 372], 'series_terms': 32, 'log_grid_denominator': 1 << 32, 'ell_grid_denominator': 1 << 20, 'log2_certificate': series(Q(1, 3)), 'tail_bound': {'numerator': 9, 'denominator': 260 * 3 ** 65}, 'actual_worker_exit_code': 0, 'outer_timed_out': False}
        for native,expected,label in ((a,e1,'first'),(b,e2,'second')):
            same({k:v for k,v in native.items() if k not in provenance+['records']},expected,label+'/metadata')
            assert len(native['records'])==2
        upstream=json.loads(((_J_OUTPUT / 'fast-optimum-result.json')).read_text(encoding='utf-8'))
        old={r['n']:r for r in upstream['records']}
        for idx,n in enumerate((18,30)):
            out['records'].append(review_record(n,old[n],a['records'][idx],b['records'][idx]))
        out['status']='passed'
        out['provenance_only_fields']={label:{k:native[k] for k in provenance} for label,native in [('first',a),('second',b)]}
    except BaseException as exc:
        out['status']='failed'; out['error']=_record_text(repr(exc)); out['traceback']=_record_text(traceback.format_exc())
    out['exact_scalar_fields_checked']=COUNT
    pass
    pass
    pass
    pass
    OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
    return 0 if out['status']=='passed' else 1

if __name__=='__main__':
    if '--worker' in sys.argv: raise SystemExit(worker())
    if OUT.exists(): raise SystemExit('Refusing to overwrite first review report')
    p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'nonmonomial-norm-review.py')),'--worker'])
    try: raise SystemExit(p.wait(timeout=CAP))
    except subprocess.TimeoutExpired:
        p.kill(); p.wait()
        if not OUT.exists(): OUT.write_text(json.dumps({'status': 'incomplete-timeout'}) + '\n', encoding='utf-8')
        raise SystemExit(1)
