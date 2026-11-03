"""Independent complete rational witness reconstruction, not an LP rerun."""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as F
from math import gcd, lcm, isfinite
import json, sys, time, platform, subprocess, traceback
import sympy as sp

BASE=(_J_PROGRAM / 'fast-optimum-review.py').parent
CAP=180
CHECKS=0

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


def equal(actual,expected,path):
    global CHECKS
    if isinstance(expected,list):
        assert type(actual) is list and len(actual)==len(expected),path
        for i,(a,b) in enumerate(zip(actual,expected)): equal(a,b,f'{path}/{i}')
    elif isinstance(expected,dict):
        assert type(actual) is dict and set(actual)==set(expected),path
        for k,v in expected.items(): equal(actual[k],v,f'{path}/{k}')
    else:
        assert type(actual) is type(expected) and actual==expected,(path,actual,expected)
        CHECKS+=1

def rat(x):
    x=F(x)
    return [x.numerator,x.denominator]

def number(x):
    assert type(x) is list and len(x)==2 and all(type(y) is int for y in x)
    assert x[1]>0 and gcd(*x)==1
    return F(*x)

def vec(v): return [rat(x) for x in v]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def matrix_rat(m): return [[rat(m[i,j]) for j in range(m.cols)] for i in range(m.rows)]

def rem(coeff,p):
    v=list(coeff)
    d=len(p)-1
    for k in range(len(v)-1,d-1,-1):
        lead=v[k]
        for j in range(d+1): v[k-d+j]-=lead*p[j]
    return (v+[0]*d)[:d]

def reconstruct(n):
    pn=[0]*(n+4)
    for j,c in [(0,1),(2,-1),(3,-1),(n,-1),(n+1,-1),(n+3,1)]: pn[j]+=c
    d=n+2
    p=[0]*(d+1)
    p[0]=pn[0]
    for j in range(1,d+1): p[j]=pn[j]-p[j-1]
    assert p[-1]==pn[-1]==1
    N=2*d
    columns=[rem([0]*j+[1],p) for j in range(N)]
    X=sp.Matrix(d,N,lambda i,j:columns[j][i])
    gram=X*X.T
    # DomainMatrix fraction-free inverse on the QUOTIENT row Gram, not author kernel elimination.
    R=X.T*gram.inv(method='DM')*X
    q=lcm(*(int(x.q) for x in R))
    C=[[int(q*R[i,j]) for j in range(N)] for i in range(N)]
    assert R*R==R and R.T==R and sp.trace(R)==d
    for j in range(N):
        assert rem([C[i][j] for i in range(N)],p)==[q*x for x in columns[j]]
    r=[F(R[j,j]) for j in range(N)]
    convs=[]
    for j in range(N):
        a=[C[i][j] for i in range(N)]
        rev=a[::-1]
        conv=[0]*(2*N-1)
        for i,x in enumerate(a):
            for k,y in enumerate(rev): conv[i+k]+=x*y
        convs.append(conv)
    H=[[F(convs[j][N-1+h],q*q) for j in range(N)] for h in range(1,N)]
    assert all(r[j]==r[N-1-j] for j in range(N))
    assert all(row[j]==row[N-1-j] for row in H for j in range(N))
    return p,d,N,q,C,r,H,convs

def rankinfo(rows,n):
    mat=sp.Matrix(rows)
    pivots=mat.rref()[1]
    return {'rank':len(pivots),'unknown_count':n,
            'free_indices':[j for j in range(n) if j not in pivots], 'equation_count':len(rows)}

def float_provenance(c,H,r,d):
    global CHECKS
    L=len(H); orig=d+L; m=2*L+2; surplus=orig+2*L; art=[surplus+1,surplus+2]; width=art[-1]+1
    expected_keys={'status','pivot_count','phase_pivot_counts','phase1_objective','basis',
                   'standard_variables','tableau_rows','reduced_costs','standard_dual','pair_masses',
                   'candidate_correlations','objective','y','lambda','mu','reduced_cost_tolerance',
                   'active_selection_tolerance','ratio_tie_tolerance'}
    assert set(c)==expected_keys
    equal(c['status'],'candidate-returned','float/status')
    equal(c['reduced_cost_tolerance'],1e-9,'float/tolerance')
    equal(c['active_selection_tolerance'],1e-7,'float/active')
    equal(c['ratio_tie_tolerance'],1e-10,'float/tie')
    basis=c['basis']; assert len(basis)==m and len(set(basis))==m
    assert all(type(j) is int and 0<=j<art[0] for j in basis)
    assert type(c['pivot_count']) is int and 0<c['pivot_count']<=10000
    assert len(c['phase_pivot_counts'])==2 and all(type(x) is int and x>=0 for x in c['phase_pivot_counts'])
    assert 0<=c['pivot_count']-sum(c['phase_pivot_counts'])<=m
    dims={'standard_variables':width,'reduced_costs':width,'standard_dual':m,
          'pair_masses':d,'candidate_correlations':L,'y':L}
    for k,length in dims.items():
        assert type(c[k]) is list and len(c[k])==length
        assert all(type(x) is float and isfinite(x) for x in c[k])
    T=c['tableau_rows'];assert len(T)==m and all(len(row)==width+1 for row in T)
    assert all(type(x) is float and isfinite(x) for row in T for x in row)
    for k in ['phase1_objective','objective','lambda','mu']:
        assert type(c[k]) is float and isfinite(c[k])
    A=[[0.0]*width for _ in range(m)]; rhs=[0.0]*m
    for h in range(L):
        for j in range(d): A[2*h][j]=float(H[h][j]);A[2*h+1][j]=-float(H[h][j])
        A[2*h][d+h]=A[2*h+1][d+h]=-1.0
        A[2*h][orig+2*h]=A[2*h+1][orig+2*h+1]=1.0
    for j in range(d): A[-2][j]=1.0;A[-1][j]=float(r[j])
    A[-2][surplus]=-1.0;A[-2][art[0]]=1.0;rhs[-2]=2.0
    A[-1][art[1]]=1.0;rhs[-1]=1.0
    errors={}
    def near(x,y,label):
        global CHECKS
        err=abs(x-y)/(1+abs(y))
        errors[label]=max(errors.get(label,0),err)
        assert err<2e-6,(label,x,y,err)
        CHECKS+=1
    # Check every tableau cell against B*T=A with original basis B, no inverse or pivots rerun.
    for i in range(m):
        nz=[(k,A[i][basis[k]]) for k in range(m) if A[i][basis[k]]]
        for j in range(width+1):
            got=sum(value*T[k][j] for k,value in nz)
            near(got,rhs[i] if j==width else A[i][j],'basis_tableau_relation')
    for i in range(m):
        for k,j in enumerate(basis): near(T[i][j],float(i==k),'basic_identity')
    vars_expected=[0.0]*width
    for i,j in enumerate(basis): vars_expected[j]=T[i][-1]
    objective=[2.0 if d<=j<orig else 0.0 for j in range(width)]
    for j in range(width):
        near(c['standard_variables'][j],vars_expected[j],'variable_extract')
        near(c['reduced_costs'][j],objective[j]-sum(objective[basis[i]]*T[i][j] for i in range(m)),'reduced_costs')
        assert c['standard_variables'][j]>=-2e-6
        if j<art[0]: assert c['reduced_costs'][j]>=-2e-6
    pi=c['standard_dual'];rc=c['reduced_costs']
    for i in range(2*L):near(pi[i],-rc[orig+i],'dual_extract')
    near(pi[-2],rc[surplus],'dual_extract');near(pi[-1],-rc[art[1]],'dual_extract')
    for j in range(width):near(sum(pi[i]*A[i][j] for i in range(m)),objective[j]-rc[j],'dual_original_relation')
    for j in range(d): near(c['pair_masses'][j],c['standard_variables'][j],'pairs')
    for h in range(L):
        near(c['candidate_correlations'][h],sum(float(H[h][j])*c['pair_masses'][j] for j in range(d)),'float_correlations')
        near(c['y'][h],(pi[2*h+1]-pi[2*h])/2,'float_y')
    near(c['lambda'],pi[-1],'float_lambda');near(c['mu'],pi[-2],'float_mu')
    near(c['objective'],sum(objective[j]*c['standard_variables'][j] for j in range(width)),'float_objective')
    near(c['phase1_objective'],0.0,'phase1_zero')
    return {'maximum_relative_residuals':errors,'comparison_tolerance':2e-6,
            'basis_rows':m,'tableau_columns_with_rhs':width+1,'reran_float_solver':False}

def check_record(rec):
    n=rec['n'];assert n in (18,30)
    p,d,N,q,C,r,H,convs=reconstruct(n)
    expected={'n':n,'coefficients':p,'d':d,'N':N,'q':q,'input_C_rows':C,
              'r':vec(r),'H_rows':[vec(row) for row in H],
              'column_contents':[gcd(*(C[i][j] for i in range(N))) for j in range(N)],
              'uniform_kappa':rat(F(2,d)*sum(abs(sum(row)) for row in H)), 'S0':2}
    c=rec['floating_candidate']
    provenance=float_provenance(c,H,r,d)
    support=[j for j,x in enumerate(c['pair_masses']) if x>1e-7]
    zeros=[h for h,x in enumerate(c['candidate_correlations']) if abs(x)<1e-7]
    tight=abs(sum(c['pair_masses'])-2)<1e-7
    rows=[[r[j] for j in support]]
    rhs=[F(1)]
    if tight:rows.append([F(1)]*len(support));rhs.append(F(2))
    for h in zeros:rows.append([H[h][j] for j in support]);rhs.append(F(0))
    info=rankinfo(rows,len(support));assert not info['free_indices']
    # A different exact method: determinant/adjugate solve of square active matrices.
    mtx=sp.Matrix(rows);assert mtx.rows==mtx.cols
    det=mtx.det(method='bareiss');assert det
    sol=mtx.adjugate(method='bareiss')*sp.Matrix(rhs)/det
    b=[F(0)]*d
    for j,x in zip(support,sol):b[j]=F(x)
    v=[b[min(j,N-1-j)]/2 for j in range(N)]
    S=sum(v); correlations=[dot(row,v) for row in H];kappa=2*sum(abs(x) for x in correlations)
    assert dot(r,v)==1 and all(x>=0 for x in v) and S>=2
    expected.update({'selected_support':support,'selected_zero_lags':[h+1 for h in zeros],
                     'selected_S_tight':tight,'primal_reconstruction':info,
                     'pair_masses':vec(b),'v':vec(v),'S':rat(S),'correlations':vec(correlations),'kappa':rat(kappa)})
    y=[None]*(N-1);free=[]
    for h,x in enumerate(correlations):
        if x:y[h]=F(1 if x>0 else -1)
        elif abs(abs(c['y'][h])-1)<1e-7:y[h]=F(1 if c['y'][h]>0 else -1)
        else:free.append(h)
    dr=[];db=[]
    for j,x in enumerate(b):
        if x:
            dr.append([2*H[h][j] for h in free]+[-r[j],F(-1)])
            db.append(-sum(2*H[h][j]*y[h] for h in range(N-1) if y[h] is not None))
    if S>2 or abs(c['mu'])<1e-7:dr.append([F(0)]*(len(free)+1)+[F(1)]);db.append(F(0))
    dinfo=rankinfo(dr,len(free)+2);assert not dinfo['free_indices']
    dm=sp.Matrix(dr);ddet=dm.det(method='bareiss');assert ddet
    ds=dm.adjugate(method='bareiss')*sp.Matrix(db)/ddet
    for h,x in zip(free,ds):y[h]=F(x)
    lam,mu=map(F,ds[-2:])
    slacks=[2*sum(H[h][j]*y[h] for h in range(N-1))-lam*r[j]-mu for j in range(N)]
    assert mu>0 and all(abs(x)<=1 for x in y) and all(x>=0 for x in slacks)
    assert kappa==lam+2*mu
    expected.update({'dual_reconstruction':dinfo,'dual_free_y_lags':[h+1 for h in free],
                     'y':vec(y),'lambda':rat(lam),'mu':rat(mu),'dual_slacks':vec(slacks),
                     'lower_bound':rat(lam+2*mu),'gap':rat(kappa-lam-2*mu)})
    w=[x/S for x in v];den=lcm(*(x.denominator for x in w));multip=[int(x*den) for x in w]
    energy=F(q*q,S);ag=[F(q*q)*x/S for x in correlations]
    poly=[sum(multip[j]*convs[j][k] for j in range(N)) for k in range(2*N-1)]
    assert F(poly[N-1],den)==energy and sum(multip)==den
    assert all(F(poly[N-1+h],den)==ag[h-1] for h in range(1,N))
    expected.update({'status':'complete','global_optimum_certified':True,'weights':vec(w),
                     'weight_denominator':den,'multiplicities':multip,
                     'positive_columns':[j for j,x in enumerate(w) if x],
                     'zero_correlation_lags':[h+1 for h,x in enumerate(correlations) if not x],
                     'strict_dual_slack_columns':[j for j,x in enumerate(slacks) if x>0],
                     'energy':rat(energy),'aggregate_autocorrelations':vec(ag),
                     'aggregate_polynomial':poly,'each_full_resultant_abs':q**d,
                     'income_log_argument':q,'surplus_half_log_argument':rat(S),
                     'degree_bound':N-1,'radial_multiplier':rat(F(N-1,d)),
                     'kappa_le_4':kappa<=4,'improves_uniform':kappa<number(expected['uniform_kappa']),
                     'kappa_thousandth_bin':[kappa.numerator*1000//kappa.denominator,
                                             kappa.numerator*1000//kappa.denominator+1]})
    assert set(rec)==set(expected)|{'floating_candidate'}
    for k,value in expected.items():equal(rec[k],value,f'n{n}/{k}')
    # Full uniqueness face and stability constants claimed in D200, derived from saved native witnesses.
    I=[j for j in range(d) if not slacks[j]]
    Z=[h for h in range(N-1) if abs(y[h])<1]
    assert I==support and Z==zeros
    assert all(b[j]>0 for j in I) and all(not b[j] for j in range(d) if j not in I)
    BI=sp.Matrix([[F(1)]*len(I),[r[j] for j in I]]+[[H[h][j] for j in I] for h in Z])
    BI_det=BI.det(method='bareiss');assert BI_det
    assert BI*sp.Matrix([b[j] for j in I])==sp.Matrix([2,1]+[0]*len(Z))
    inverse=BI.adjugate(method='bareiss')/BI_det
    O=[j for j in range(d) if j not in I]
    BO=sp.Matrix([[F(1)]*len(O),[r[j] for j in O]]+[[H[h][j] for j in O] for h in Z])
    delta=min(slacks[j] for j in O);eta=min(1-abs(y[h]) for h in Z)
    norm=lambda mat:max(sum(abs(F(mat[i,j])) for i in range(mat.rows)) for j in range(mat.cols))
    M=norm(inverse);BO_norm=norm(BO)
    stability=1/delta+M*(1/mu+1/(2*eta)+BO_norm/delta)
    return {'n':n,'full_native_fields_checked':sorted(expected), 'floating_provenance':provenance,
            'pair_support':I,'interior_lags':[h+1 for h in Z], 'B_I':matrix_rat(BI),
            'B_I_determinant':rat(BI_det),'B_I_inverse':matrix_rat(inverse),
            'outside_pairs':O,'B_O':matrix_rat(BO),'delta':rat(delta),'eta':rat(eta),
            'inverse_one_norm':rat(M),'outside_one_norm':rat(BO_norm),'stability_constant':rat(stability),
            'necessary_S_for_K_le_4':rat(2-(kappa-4)/mu),'kappa':rat(kappa),'S':rat(S),
            'primal_active_determinant':rat(det),'dual_active_determinant':rat(ddet),
            'minimum_pair_support':len(I),'optimal_face_dimension':len(I),'status':'pass'}

def worker(out):
    started=time.perf_counter()
    paths=[(_J_PROGRAM / 'fast-optimum.py'),(_J_OUTPUT / 'fast-optimum-result.json'),(_J_OUTPUT / 'family-output.json')]
    observed=[p.read_bytes() for p in paths]
    native=json.loads(observed[1]);report={'status': 'running', 'records': []}
    def save():
        pass;report['strict_comparisons']=CHECKS
        out.write_text(json.dumps(report,indent=2),encoding='utf-8')
    try:
        expected_top={'schema', 'status', 'domain_n', 'S0', 'pivot_cap_per_input', 'input', 'records', 'worker_returncode', 'outer_deadline_triggered', 'all_global_optima_certified'}
        assert set(native)==expected_top
        for k,v in {'schema': 'J79-fast-exact-optimum-v1', 'status': 'complete', 'domain_n': [18, 30], 'S0': 2, 'pivot_cap_per_input': 10000, 'input': 'family-output.json', 'worker_returncode': 0, 'outer_deadline_triggered': False, 'all_global_optima_certified': True}.items():equal(native[k],v,'top/'+k)
        assert len(native['records'])==2 and [r['n'] for r in native['records']]==[18,30]
        pass
        for k in []:assert type(native[k]) is float and 0<native[k]<121
        source=json.loads(observed[2])
        for rec in native['records']:
            f=next(r for r in source['records'] if r['n']==rec['n'])
            chosen=[x for x in f['factors'] if x['selected']]
            assert len(chosen)==1 and chosen[0]['status']=='actual-certified'
            equal(rec['coefficients'],chosen[0]['coefficients'],'certified-source-coefficients')
            report['records'].append(check_record(rec));save()
        report['status']='pass'
    except Exception as error:
        report.update({'status':'failed','error':_record_text(str(error)),'traceback':_record_text(traceback.format_exc())})
    pass
    save()
    return 0 if report['status']=='pass' else 1

def main():
    if len(sys.argv)==3 and sys.argv[1]=='--worker':return worker(Path(sys.argv[2]))
    out=(_J_OUTPUT / 'fast-optimum-review-result.json')
    if len(sys.argv)==3 and sys.argv[1]=='--output':out=Path(sys.argv[2]).resolve()
    assert out.parent == _J_OUTPUT and not out.exists()
    started=time.perf_counter()
    proc=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'fast-optimum-review.py')),'--worker',str(out)])
    timeout=False
    try:code=proc.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        timeout=True;proc.kill();code=proc.wait()
    data=json.loads(out.read_text(encoding='utf-8')) if out.exists() else {'records':[]}
    pass
    if timeout:data['status']='incomplete-timeout'
    out.write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(json.dumps({'status': data.get('status'), 'records': len(data['records']), 'strict_comparisons': data.get('strict_comparisons')}))
    return 0 if data.get('status')=='pass' else 1

if __name__=='__main__':raise SystemExit(main())
