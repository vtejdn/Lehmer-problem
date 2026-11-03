"""Full independent residual-lattice native checker, exactly n18/n30.
Serialization, exact-log and finite-step helper bodies are explicitly reused
from orbit's separately reviewed nonmonomial-norm-review.py. No author program
or other program is imported. New kernel-Gram reconstruction and polynomial
resultants replace the present author's residual input and determinant norm.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from math import gcd, lcm
from datetime import datetime
import json, time, traceback, platform, sys, subprocess, argparse
import sympy as sp
HERE=(_J_PROGRAM / 'residual-lattice-review.py').parent
CAP=180
COUNT=0
START=None


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


def gate():
    assert time.monotonic()-START<CAP, 'declared aggregate cap'


def determinant(A):
    """Integer Bareiss with exact division; no SymPy determinant call."""
    a=[row[:] for row in A]; n=len(a); sign=1; previous=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[pivot],a[k]=a[k],a[pivot]; sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*v-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
            a[i][k]=0
        previous=v
    return sign*a[-1][-1]


def multiply(A,B):
    columns=list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) for col in columns] for row in A]


def build_context(n,old):
    d=n+2; N=2*d
    p=[(-1 if i%2 else 1) for i in range(d+1)]
    p[2]=p[d-2]=0
    # Independently reconstruct projection from the COMPLETE kernel shifts.
    relation=sp.Matrix(N,d,lambda i,j:p[i-j] if 0<=i-j<=d else 0)
    Gram=relation.T*relation
    R=sp.eye(N)-relation*Gram.inv(method='DM')*relation.T
    q=lcm(*(int(a.q) for a in R))
    C=[[int(q*R[i,j]) for j in range(N)] for i in range(N)]
    cols=list(map(list,zip(*C)))
    L=[row[:d] for row in C]; Lcols=cols[:d]
    powers=[]; v=[1]+[0]*(d-1)
    for _ in range(N):
        powers.append(v)
        v=[(v[i-1] if i else 0)-p[i]*v[-1] for i in range(d)]
    X=list(map(list,zip(*powers))); Qmat=multiply(X,list(zip(*X)))
    assert multiply(L,X)==C
    assert multiply(X,L)==[[q*int(i==j) for j in range(d)] for i in range(d)]
    detQ=determinant(Qmat)
    assert detQ==determinant([[int(Gram[i,j]) for j in range(d)] for i in range(d)])>0
    r=[Q(sum(a*a for a in col),q*q) for col in cols]
    hcols=[correlations(col) for col in cols]
    H=[[Q(hcols[j][h],q*q) for j in range(N)] for h in range(N-1)]
    assert all(r[j]==r[N-1-j] for j in range(N))
    assert all(row[j]==row[N-1-j] for row in H for j in range(N))
    pair=list(map(dec,old['pair_masses'])); y=list(map(dec,old['y']))
    lam=dec(old['lambda']); mu=dec(old['mu'])
    I=[j for j,b in enumerate(pair) if b]
    a0=[dot(row[:d],pair) for row in H]
    Z=[h for h,a in enumerate(a0) if a==0]
    K0=2*sum(map(abs,a0))
    assert len(pair)==d and min(pair)>=0 and sum(pair)==2
    assert dot(pair,r[:d])==1 and K0==lam+2*mu>4 and mu>0
    assert all(abs(a)<=1 for a in y)
    assert all(not a or y[h]==(1 if a>0 else -1) for h,a in enumerate(a0))
    slack=[2*dot(y,[row[j] for row in H])-lam*r[j]-mu for j in range(N)]
    assert min(slack)>=0 and all(slack[j]==0 for j in I)
    M=[[Q(1) for j in I],[r[j] for j in I]]+[[H[h][j] for j in I] for h in Z]
    assert len(M)==len(I)
    inv=inverse(M)
    assert multiply(M,inv)==[[int(i==j) for j in I] for i in I]
    den=lcm(lam.denominator,*(a.denominator for a in y))
    yi=[int(a*den) for a in y]
    kernel=yi[::-1]+[int(-lam*den)]+yi
    filtered=[conv(col,kernel)[N-1:2*N-1] for col in Lcols]
    K=[[Q(sum(x*y for x,y in zip(Lcols[i],filtered[j])),den*q*q)
        for j in range(d)] for i in range(d)]
    Tint=[[int(-lam*den) if i==j else yi[abs(i-j)-1] for j in range(N)] for i in range(N)]
    for key,expected in [('coefficients',p),('d',d),('N',N),('q',q),('input_C_rows',C),
                         ('r',seq(r)),('H_rows',[seq(row) for row in H]),
                         ('correlations',seq(a0)),('kappa',enc(K0))]:
        same(old[key],expected,f'upstream/{n}/{key}')
    return locals()


def checked_schur(cert,K):
    # For these full native inputs use uniqueness and direct factor identity,
    # not the author's leading-pivot algorithm.
    d=len(K)
    assert set(cert)=={'status','pivots','lower','integer_witness'}
    assert cert['status']=='positive_definite' and cert['integer_witness'] is None
    piv=list(map(dec,cert['pivots'])); low=[list(map(dec,row)) for row in cert['lower']]
    assert len(piv)==len(low)==d and all(len(row)==d for row in low)
    assert all(x>0 for x in piv)
    assert all(low[i][i]==1 and all(low[i][j]==0 for j in range(i+1,d)) for i in range(d))
    rebuilt=multiply([[low[i][j]*piv[j] for j in range(d)] for i in range(d)],list(zip(*low)))
    assert rebuilt==K
    # Strict schema/type traversal also includes every rational certificate leaf.
    same(cert,{'status':'positive_definite','pivots':seq(piv),'lower':[seq(row) for row in low],
               'integer_witness':None},'schur')
    return cert


def step_record(ctx,sd,ell):
    st=step(ctx,sd,ell); D=abs(sd['nb']); d=ctx['d']; q=ctx['q']
    assert 0<=ell*st['tau']<=Q(1,2)
    return {'ell':enc(ell),'active_rhs':seq(st['rhs']),'old_mass_derivative':seq(st['x']),
            'correlation_derivative':seq(st['da']),'slope':enc(st['slope']),
            'step_bounds':[{'kind':a,'index':b,'value':enc(c)} for a,b,c in st['bounds']],
            'tau':enc(st['tau']),'limiting_bounds':[i for i,z in enumerate(st['bounds']) if z[2]==st['tau']],
            'pair_masses':seq(st['bp']),'masses':seq(st['masses']),'S':enc(st['S']),
            'weights':seq(st['weights']),'weight_denominator':st['L'],'multiplicities':st['mult'],
            'positive_indices':[i for i,w in enumerate(st['weights']) if w],
            'correlations':seq(st['aa']),'kappa':enc(st['K']),'strict_improvement':st['K']<ctx['K0'],
            'kappa_le_4':st['K']<=4,'energy':enc(Q(q*q)/st['S']),
            'aggregate_autocorrelations':seq(st['agg']),
            'income':{'log_q_argument':q,'log_D_argument':D,'log_D_coefficient':enc(st['tau']/(d*st['S']))},
            'surplus':{'half_log_argument':enc(st['S']),'extra_log_argument':D,
                       'extra_log_coefficient':enc(st['tau']/(d*st['S'])),
                       'finite_interval_x':enc(ell*st['tau']),'at_least_half_log_two':True}}


def norm_matrix(z,p):
    # Horner in the sparse multiplication-by-t operator, not reduction of
    # independently shifted seed polynomials as in the author implementation.
    d=len(z); out=[[0]*d for _ in range(d)]
    for coefficient in reversed(z):
        out=[[(out[i-1][j] if i else 0)-p[i]*out[-1][j]+coefficient*int(i==j)
              for j in range(d)] for i in range(d)]
    return out


def check_record(native,old):
    n=native['n']; ctx=build_context(n,old)
    p,d,N,q,C,L,X,Qmat,detQ,K,Tint,den,r,H,y,lam,mu,K0,pair,Z,M,inv=[ctx[key] for key in
        ('p','d','N','q','C','L','X','Qmat','detQ','K','Tint','den','r','H','y','lam','mu','K0','pair','Z','M','inv')]
    schur=checked_schur(native['schur_certificate'],K)
    U=native['U_rows']; Ui=native['U_inverse_rows']; reduced=native['reduced_rows']
    assert all(type(a) is int for A in (U,Ui,reduced) for row in A for a in row)
    assert len(U)==len(Ui)==len(reduced)==d
    assert all(len(row)==d for row in U+Ui) and all(len(row)==N for row in reduced)
    identity=[[int(i==j) for j in range(d)] for i in range(d)]
    assert multiply(U,Ui)==multiply(Ui,U)==identity
    detU=determinant(U); assert abs(detU)==1
    assert multiply(U,list(zip(*L)))==reduced
    labels=[('basis',i,0,U[i]) for i in range(d)]
    labels += [('adjacent',i,s,[a+s*b for a,b in zip(U[i],U[i+1])])
               for i in range(d-1) for s in (-1,1)]
    assert len(labels)==len(native['candidates'])==3*d-2
    t=sp.Symbol('t'); polynomial=sp.Poly.from_list(p[::-1],t,domain=sp.ZZ)
    ks=[[],[]]; norms=[]
    for index,(kind,i,sign,z) in enumerate(labels):
        gate(); assert any(z)
        B=z+[0]*(N-d); f=[sum(x*a for x,a in zip(row,z)) for row in L]
        diff=[q*a-b for a,b in zip(B,f)]
        quotient=[]
        # Forward unit-constant convolution inversion, not top-degree division.
        for j in range(N-d):
            quotient.append(diff[j]-sum(p[h]*quotient[j-h] for h in range(1,min(j,d)+1)))
        assert conv(p,quotient)==diff
        c=gcd(*f); primitive=[a//c for a in f]
        matrix=norm_matrix(z,p)
        # Exact polynomial subresultant resultant, independently of every saved
        # multiplication determinant. No irreducibility library claim used.
        norm=int(polynomial.resultant(sp.Poly.from_list(z[::-1],t,domain=sp.ZZ)))
        assert norm!=0 and c>0 and gcd(*primitive)==1
        full=q**d*norm; assert full%c**d==0
        assert remainder(f,p)==[q*a for a in z]
        ac=correlations(f); energy=sum(a*a for a in f)
        E=Q(energy,q*q); HB=[Q(a,q*q) for a in ac]
        value=dot(z,[dot(row,z) for row in K]); g=value-mu
        assert g==2*dot(y,HB)-lam*E-mu
        cert=logcert(abs(norm),d); ell=dec(cert['ell_lower']); hiell=dec(cert['ell_upper'])
        sd={'E':E,'HB':HB,'g':g,'nb':norm}
        steps=[step_record(ctx,sd,x) for x in (Q(0),ell)]
        lower=g-2*mu*hiell; upper=g-2*mu*ell
        expected={'kind':kind,'basis_index':i,'sign':sign,'z':z,'B':B,'F_coefficients':f,
                  'kernel_multiplier':quotient,'content':c,'primitive_coefficients':primitive,
                  'actual_degree':max(j for j,a in enumerate(f) if a),'norm_matrix':matrix,
                  'signed_res_B':norm,'signed_res_F':full,'signed_res_primitive':full//c**d,
                  'integer_energy':energy,'e_B':enc(E),'integer_autocorrelations':ac,'h_B':seq(HB),
                  'quadratic_value':enc(value),'reduced_cost':enc(g),'log_certificate':cert,
                  'exact_log_slope_interval':[enc(lower),enc(upper)],
                  'exact_log_slope_decision':'negative' if upper<0 else 'nonnegative' if lower>=0 else 'undecided',
                  'conservative_step':steps[0],'norm_funded_step':steps[1]}
        same(native['candidates'][index],expected,f'{n}/candidate/{index}')
        for j,st in enumerate(steps):ks[j].append(dec(st['kappa']))
        norms.append(norm)
    expected={'n':n,'d':d,'N':N,'q':q,'coefficients':p,'X_rows':X,'L_rows':L,'Q_rows':Qmat,
              'det_Q':detQ,'signed_correlation_integer_matrix':Tint,'signed_correlation_denominator':den,
              'K_rows':[seq(row) for row in K],'schur_certificate':schur,'old_r':seq(r),
              'old_H':[seq(row) for row in H],'old_y':seq(y),'old_lambda':enc(lam),'old_mu':enc(mu),
              'old_kappa':enc(K0),'old_pair_masses':seq(pair),'old_zero_lags':[h+1 for h in Z],
              'active_matrix':[seq(row) for row in M],'active_inverse':[seq(row) for row in inv],
              'degree_bound':N-1,'radial_multiplier':enc(Q(N-1,d)),'lll_status':'complete',
              'U_rows':U,'U_inverse_rows':Ui,'det_U':detU,'reduced_rows':reduced,
              'candidate_count':len(labels),'status':'complete'}
    for j,name in enumerate(('conservative_step','norm_funded_step')):
        expected[name+'_summary']={'improvement_count':sum(a<K0 for a in ks[j]),
                                   'kappa_le_4_count':sum(a<=4 for a in ks[j]),
                                   'best_index':min(range(len(labels)),key=lambda i:ks[j][i])}
    same({key:value for key,value in native.items() if key!='candidates'},expected,f'{n}/complete-record')
    return {'n':n,'d':d,'N':N,'labels':len(labels),'det_Q':detQ,'det_U':detU,
            'independent_polynomial_resultants':len(labels),'complete_norm_matrix_entries':len(labels)*d*d,
            'all_mathematical_fields_and_schemas_checked':True,
            'step_summaries':[expected[name+'_summary'] for name in ('conservative_step','norm_funded_step')]}


def worker(output):
    global START
    START=time.monotonic()
    names=['residual-lattice-author.py','residual-lattice-output.json','fast-optimum-result.json',
           'nonmonomial-author.py','nonmonomial-output.json','norm-funded-author.py','norm-funded-output.json']
    snapshot={name:(((_J_PROGRAM if name in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / name)).read_bytes() for name in names}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0207.md')
    before=draft.read_bytes() if draft.exists() else None
    report={'schema': 'J79-complete-integral-lattice-independent-review-v1', 'records': [], 'method': 'kernel-shift Gram projection; convolution K; certificate LDL; polynomial resultant; Horner norm matrix', 'reviewer_helper_reuse': 'Explicit copied helper definitions from independent nonmonomial-norm-review.py; no imports'}
    try:
        native=json.loads(snapshot['residual-lattice-output.json'])
        upstream=json.loads(snapshot['fast-optimum-result.json'])
        provenance=[]
        pass
        pass
        assert all(type(native[key]) is float and 0<native[key]<CAP for key in provenance[-2:])
        expected={'schema': 'J79-integral-residual-lattice-v1', 'status': 'complete', 'domain_n': [18, 30], 'lll_delta': [3, 4], 'declared_basis_adjacent_counts': [58, 94], 'max_schur_witnesses': 2, 'input': 'fast-optimum-result.json', 'log2_certificate': series(Q(1, 3)), 'actual_worker_exit_code': 0, 'outer_timed_out': False}
        same({k:v for k,v in native.items() if k not in provenance+['records']},expected,'metadata')
        assert len(native['records'])==2
        olds={row['n']:row for row in upstream['records']}
        for n,row in zip((18,30),native['records']):
            assert row['n']==n
            report['records'].append(check_record(row,olds[n]))
        gate(); report['status']='passed'
        report['historical_provenance_only']={key:native[key] for key in provenance}
    except BaseException as exc:
        report.update(status='failed',error=_record_text(repr(exc)),traceback=_record_text(traceback.format_exc()))
    report['exact_scalar_fields_checked']=COUNT
    pass
    pass
    pass
    pass
    output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))
    return 0 if report['status']=='passed' else 1


if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--worker',action='store_true')
    ap.add_argument('--output',type=Path,default=(_J_OUTPUT / 'residual-lattice-review-result.json'))
    args=ap.parse_args(); output=args.output.resolve(); assert output.parent == _J_OUTPUT
    if args.worker:raise SystemExit(worker(output))
    with output.open('x',encoding='utf-8') as f:json.dump({'status': 'started'}, f)
    start=time.monotonic()
    proc=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'residual-lattice-review.py')),'--worker','--output',str(output)],
                          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    try:code=proc.wait(timeout=max(.01,CAP-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:
        proc.kill(); proc.wait(); code=1
        out=json.loads(output.read_text()); out.update(status='incomplete-timeout')
        output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    raise SystemExit(code)
