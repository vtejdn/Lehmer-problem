"""Whole joint-budget review; no author imports and no optimization rerun.

Explicit reuse: orbit's own nonmonomial-norm-review.py exact helpers.
The saved floating basis is only checked for consistency, not made proof.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from math import gcd, lcm, isfinite
import importlib.util, json, time, traceback, subprocess, sys, platform
import sympy as sp
import numpy as np

HERE=(_J_PROGRAM / 'joint-budget-review.py').parent
CAP=180
TOL=1e-6
OUT=(_J_OUTPUT / 'joint-budget-review-result.json')
spec=importlib.util.spec_from_file_location('own_prior_review',(_J_PROGRAM / 'nonmonomial-norm-review.py'))
own=importlib.util.module_from_spec(spec); spec.loader.exec_module(own)
same,enc,seq,dec,dot,conv=own.same,own.enc,own.seq,own.dec,own.dot,own.conv

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


def inspect_float(c,hp,ep):
    keys={'status','pivot_count','phase_pivot_counts','phase1_objective','basis',
          'standard_variables','tableau_rows','reduced_costs','standard_dual','pair_masses',
          'candidate_correlations','objective','y','lambda','mu','reduced_cost_tolerance',
          'active_selection_tolerance','ratio_tie_tolerance'}
    assert set(c)==keys and c['status']=='candidate-returned'
    assert c['pivot_count']==sum(c['phase_pivot_counts'])==1929
    assert c['phase_pivot_counts']==[1707,222]
    for k,v in [('reduced_cost_tolerance',1e-9),('active_selection_tolerance',1e-7),('ratio_tie_tolerance',1e-10)]:
        assert type(c[k]) is float and c[k]==v
    m,L=len(ep),len(hp); rows=2*L+2; orig=m+L; surplus=m+3*L; width=surplus+3
    A=np.zeros((rows,width)); b=np.zeros(rows)
    for h in range(L):
        A[2*h,:m]=list(map(float,hp[h])); A[2*h+1,:m]=-A[2*h,:m]
        A[2*h:2*h+2,m+h]=-1
        A[2*h,orig+2*h]=1; A[2*h+1,orig+2*h+1]=1
    A[-2,:m]=1; A[-2,surplus]=-1; A[-2,surplus+1]=1; b[-2]=2
    A[-1,:m]=list(map(float,ep)); A[-1,surplus+2]=1; b[-1]=1
    basis=c['basis']; assert len(basis)==rows and len(set(basis))==rows
    assert all(type(x) is int and 0<=x<surplus+1 for x in basis)
    floats=0
    def array(key,shape):
        nonlocal floats
        def visit(x):
            nonlocal floats
            if type(x) is list:
                for y in x: visit(y)
            else:
                assert type(x) is float and isfinite(x),(key,x)
                floats+=1
        visit(c[key]); v=np.array(c[key]); assert v.shape==shape
        return v
    T=array('tableau_rows',(rows,width+1)); x=array('standard_variables',(width,))
    rc=array('reduced_costs',(width,)); pi=array('standard_dual',(rows,))
    pair=array('pair_masses',(m,)); corr=array('candidate_correlations',(L,)); y=array('y',(L,))
    for k in ('phase1_objective','objective','lambda','mu'): array(k,())
    costs=np.zeros(width);costs[m:orig]=2
    checks={
      'basis_tableau':np.max(np.abs(A[:,basis]@T-np.column_stack((A,b)))),
      'basis_identity':np.max(np.abs(T[:,basis]-np.eye(rows))),
      'standard_primal':np.max(np.abs(A@x-b)),
      'reduced_cost':np.max(np.abs(rc-(costs-costs[basis]@T[:,:-1]))),
      'basis_values':np.max(np.abs(x[basis]-T[:,-1])),
      'nonbasis_zero':max(abs(x[j]) for j in range(width) if j not in basis),
      'pair_values':np.max(np.abs(pair-x[:m])),
      'correlation_values':np.max(np.abs(np.array(hp,dtype=float)@pair-corr)),
      'objective':abs(c['objective']-costs@x),
      'dual_slack_part':np.max(np.abs(pi[:2*L]+rc[orig:orig+2*L])),
      'dual_budget':abs(pi[-2]-rc[surplus]),'dual_energy':abs(pi[-1]+rc[surplus+2]),
      'dual_y':np.max(np.abs(y-(pi[1:2*L:2]-pi[:2*L:2])/2)),
      'lambda':abs(c['lambda']-pi[-1]),'mu':abs(c['mu']-pi[-2]),
      'phase1_reported_zero':abs(c['phase1_objective'])}
    assert all(v<TOL for v in checks.values()),checks
    assert min(x)>=-TOL and min(rc[:surplus+1])>=-TOL
    return {'all_float_fields_inspected':floats,'equation_tolerance':TOL,
            'maximum_residuals':{k:float(v) for k,v in checks.items()},
            'not_an_exact_certificate_or_pivot_history_replay':True}

def solve(rows,rhs):
    M=sp.Matrix(rows); assert M.rows==M.cols and M.det(method='domain-ge')!=0
    values=M.inv(method='DM')*sp.Matrix(rhs)
    ans=[Q(x) for x in values]
    assert all(dot(row,ans)==b for row,b in zip(rows,rhs))
    return ans,{'rank':len(ans),'unknown_count':len(ans),'free_indices':[],'equation_count':len(rows)}

def review_record(rec,old,parent):
    n=rec['n']; ctx=own.context(n,old)
    p,d,N,q,C=[ctx[k] for k in ('p','d','N','q','C')]
    assert parent['n']==n and len(parent['candidates'])==3*d-2
    U=sp.Matrix(parent['U_rows']); Ui=sp.Matrix(parent['U_inverse_rows'])
    assert U*Ui==Ui*U==sp.eye(d) and int(U.det(method='domain-ge'))==parent['det_U']==-1
    family=[]; comparison={k:[] for k in ('conservative_step','norm_funded_step')}
    t=sp.Symbol('t'); P=sp.Poly.from_list(p[::-1],t,domain=sp.ZZ)
    for index in range(N+3*d-2):
        if index<N:
            b=[int(j==index) for j in range(N)]; nb=((-1)**d*p[0])**index
            cert=None; ell=Q(0); meta={'kind':'monomial','index':index}
        else:
            j=index-N; c=parent['candidates'][j]
            if j<d: kind,k,sgn='basis',j,0
            else: kind,k,sgn='adjacent',(j-d)//2,(-1 if (j-d)%2==0 else 1)
            z=[int(U[k,a]+(sgn*U[k+1,a] if sgn else 0)) for a in range(d)]
            for key,value in [('kind',kind),('basis_index',k),('sign',sgn),('z',z)]: same(c[key],value,f'seed/{n}/{j}/{key}')
            b=z+[0]*(N-d)
            nb=int(sp.resultant(P,sp.Poly.from_list(z[::-1],t,domain=sp.ZZ)))
            assert nb!=0
            cert=own.logcert(abs(nb),d); ell=dec(cert['ell_lower'])
            meta={'kind':'frozen_residue','index':j,'seed_kind':kind,'basis_index':k,'seed_sign':sgn,'z':z}
        f=[sum(row[j]*b[j] for j in range(N)) for row in C]
        diff=[q*b[j]-f[j] for j in range(N)]; up=[]
        for j in range(N-d):
            top=diff[j]-sum(p[k]*up[j-k] for k in range(1,min(j,d)+1))
            assert top%p[0]==0; up.append(top//p[0])
        assert conv(p,up)==diff
        content=gcd(*f); nf=q**d*nb
        assert content>0 and nf%content**d==0
        E=sum(x*x for x in f); ac=own.correlations(f); e=Q(E,q*q); h=[Q(x,q*q) for x in ac]
        assert e>0
        row=dict(meta,B=b,F_coefficients=f,kernel_multiplier=up,signed_res_B=nb,signed_res_F=nf,
                 content=content,ell=enc(ell),log_certificate=cert,D=abs(nb),integer_energy=E,
                 integer_autocorrelations=ac,e=enc(e),h=seq(h),a=enc(1+2*ell),
                 primitive_coefficients=[x//content for x in f],signed_res_primitive=nf//content**d,
                 actual_degree=max(j for j,x in enumerate(f) if x))
        family.append(row)
        same(rec['family'][index],row,f'{n}/family/{index}')
        if index>=N and n==18:
            sd={'E':e,'HB':h,'g':2*dot(ctx['y'],h)-ctx['lam']*e-ctx['mu']}
            for name,el in [('conservative_step',Q(0)),('norm_funded_step',ell)]:
                st=own.step(ctx,sd,el);same(c[name]['kappa'],enc(st['K']),f'previous/{j}/{name}')
                comparison[name].append(st['K'])
    e=[dec(x['e']) for x in family]; ell=[dec(x['ell']) for x in family]; aa=[1+2*x for x in ell]
    H=[[dec(x['h'][h]) for x in family] for h in range(N-1)]
    assert all(e[j]==e[N-1-j] and aa[j]==aa[N-1-j]==1 and all(row[j]==row[N-1-j] for row in H) for j in range(d))
    compressed=list(range(d))+list(range(N,len(family)))
    ep=[e[j]/aa[j] for j in compressed]; hp=[[row[j]/aa[j] for j in compressed] for row in H]
    expected={'n':n,'d':d,'N':N,'q':q,'coefficients':p,'status':'matrices-ready',
              'family':family,'family_count':len(family),'compressed_indices':compressed,
              'compressed_count':len(compressed),'r_prime':seq(ep),'H_prime':[seq(row) for row in hp],
              'degree_bound':N-1,'radial_multiplier':enc(Q(N-1,d))}
    if n==30:
        same(rec,expected,'n30/whole-matrices-ready-record')
        return {'n':n,'complete_directions':len(family),'compressed':len(compressed),'norms':3*d-2,
                'status':'all-retained-matrices-checked-no-optimizer-present'}
    fc=rec['floating_candidate']; float_report=inspect_float(fc,hp,ep)
    support=[j for j,x in enumerate(fc['pair_masses']) if x>1e-7]
    zeros=[h for h,x in enumerate(fc['candidate_correlations']) if abs(x)<1e-7]
    tight=abs(sum(fc['pair_masses'])-2)<1e-7; assert tight
    rows=[[ep[j] for j in support],[Q(1)]*len(support)]+[[hp[h][j] for j in support] for h in zeros]
    rhs=[Q(1),Q(2)]+[Q(0)]*len(zeros)
    primal_input={'support':support,'zero_lags':[h+1 for h in zeros],'budget_tight':True,
                  'rows':[seq(row) for row in rows],'rhs':seq(rhs),'approx':[fc['pair_masses'][j] for j in support]}
    sub,pinfo=solve(rows,rhs); uc=[Q(0)]*len(compressed)
    for j,x in zip(support,sub): uc[j]=x
    v=[Q(0)]*len(family)
    for k,j in enumerate(compressed):
        if j<d: v[j]=v[N-1-j]=uc[k]/2
        else: v[j]=uc[k]/aa[j]
    u=[a*b for a,b in zip(aa,v)]; S=sum(v); L=dot(ell,v); A=dot(aa,v)
    corr=[dot(row,v) for row in H]; K=2*sum(map(abs,corr))
    assert all(x>=0 for x in v) and dot(e,v)==1 and S>0 and A==S+2*L==sum(uc)==2
    y=[None]*(N-1); free=[]
    for h,a in enumerate(corr):
        if a: y[h]=Q(1 if a>0 else -1)
        elif abs(abs(fc['y'][h])-1)<1e-7: y[h]=Q(1 if fc['y'][h]>0 else -1)
        else: free.append(h)
    rows=[];rhs=[]
    for j,a in enumerate(uc):
        if a:
            rows.append([2*hp[h][j] for h in free]+[-ep[j],Q(-1)])
            rhs.append(-sum(2*hp[h][j]*y[h] for h in range(N-1) if y[h] is not None))
    assert A==2 and abs(fc['mu'])>=1e-7
    dual_input={'free_y_lags':[h+1 for h in free],'fixed_y':[None if x is None else enc(x) for x in y],
                'rows':[seq(row) for row in rows],'rhs':seq(rhs),
                'approx':[fc['y'][h] for h in free]+[fc['lambda'],fc['mu']]}
    sol,dinfo=solve(rows,rhs)
    for h,a in zip(free,sol): y[h]=a
    lam,mu=sol[-2:]; slacks=[2*dot(y,[row[j] for row in H])-lam*e[j]-mu*aa[j] for j in range(len(v))]
    assert all(abs(x)<=1 for x in y) and mu>0 and min(slacks)>=0
    assert all(v[j]*slacks[j]==0 for j in range(len(v))) and K==lam+2*mu
    w=[x/S for x in v]; M=lcm(*(x.denominator for x in w)); mult=[int(M*x) for x in w]
    aggregate=[0]*(2*N-1)
    for copies,c in zip(mult,family):
        for j,x in enumerate(conv(c['F_coefficients'],c['F_coefficients'][::-1])): aggregate[j]+=copies*x
    energy=Q(q*q)/S; autocorr=[q*q*x/S for x in corr]
    assert sum(mult)==M and aggregate==aggregate[::-1] and Q(aggregate[N-1],M)==energy
    assert [Q(aggregate[N-1+h],M) for h in range(1,N)]==autocorr
    comparisons={name:{'all_previous_kappa':seq(vals),'minimum':enc(min(vals)),
                        'strictly_below_all':K<min(vals),'at_most_all':K<=min(vals)} for name,vals in comparison.items()}
    assert all(x['strictly_below_all'] for x in comparisons.values()) and 0<S<2
    expected.update(status='complete',floating_candidate=fc,primal_reconstruction_input=primal_input,
       primal_reconstruction=pinfo,compressed_u=seq(uc),u=seq(u),v=seq(v),S=enc(S),L=enc(L),budget=enc(A),
       correlations=seq(corr),kappa=enc(K),dual_reconstruction_input=dual_input,dual_reconstruction=dinfo,
       y=seq(y),lambda_value=enc(lam),mu=enc(mu),dual_slacks=seq(slacks),
       transformed_slacks=seq([x/a for x,a in zip(slacks,aa)]),lower_bound=enc(lam+2*mu),gap=enc(K-lam-2*mu),
       global_finite_family_optimum_certified=True,weights=seq(w),weight_denominator=M,multiplicities=mult,
       positive_indices=[j for j,x in enumerate(w) if x],zero_lags=[h+1 for h,x in enumerate(corr) if not x],
       energy=enc(energy),aggregate_autocorrelations=seq(autocorr),aggregate_polynomial=aggregate,
       income={'log_q_argument':q,'norm_terms':[{'D':c['D'],'coefficient':enc(w[j]/d)} for j,c in enumerate(family)]},
       exact_arithmetic_product={'q_base':q,'q_exponent':d*M,'norm_factors':[{'D':c['D'],'exponent':mult[j]} for j,c in enumerate(family)]},
       certified_surplus={'half_log_argument':enc(S),'additional_lower':enc(L/S),'x':enc(S/2),'budget':enc(A),'at_least_half_log_two':True},
       old_kappa=enc(ctx['K0']),strictly_below_old=K<ctx['K0'],comparisons=comparisons,kappa_le_4=K<=4,
       kappa_ten_thousandth_bin=[K.numerator*10000//K.denominator,K.numerator*10000//K.denominator+1])
    # Floating payload already inspected separately; it is not an exact numerical equality test.
    same({k:x for k,x in rec.items() if k!='floating_candidate'},
         {k:x for k,x in expected.items() if k!='floating_candidate'},'n18/whole-exact-record')
    assert enc(K)==[1714168546953605078758047203716801788773584362557009514078913891651411860149161,
                    462591029463190283103106576950550691944921758466862571505279774057966813526445]
    assert expected['kappa_ten_thousandth_bin']==[37055,37056]
    return {'n':n,'complete_directions':len(family),'compressed':len(compressed),'norms':3*d-2,
            'status':'complete-exact-global-certificate','kappa':enc(K),'positive_support':expected['positive_indices'],
            'all_schema_exact_fields_checked':True,'floating_provenance_consistency':float_report}

def worker(output):
    start=time.monotonic(); own.START=start
    names=['joint-budget-author.py','joint-budget-output.json','fast-optimum.py','nonmonomial-author.py',
           'fast-optimum-result.json','residual-lattice-output.json','nonmonomial-norm-review.py']
    snapshot={n:(((_J_PROGRAM if n in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / n)).read_bytes() for n in names}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0211.md'); before=draft.read_bytes() if draft.exists() else None
    out={'schema': 'J79-joint-budget-independent-review-v1', 'records': []}
    try:
        a=json.loads(snapshot['joint-budget-output.json']); old=json.loads(snapshot['fast-optimum-result.json'])['records']
        parent=json.loads(snapshot['residual-lattice-output.json'])['records']
        keys={'schema', 'status', 'domain_n', 'new_residue_counts', 'input_files', 'helper_files', 'candidate_rule', 'records', 'error_type', 'error', 'traceback', 'actual_worker_exit_code', 'outer_timed_out'}
        assert set(a)==keys and len(a['records'])==2
        same({k: a[k] for k in ['schema', 'status', 'domain_n', 'new_residue_counts', 'input_files', 'helper_files', 'candidate_rule', 'error_type', 'error', 'actual_worker_exit_code', 'outer_timed_out']}, {'schema': 'J79-joint-norm-budget-v1', 'status': 'incomplete', 'domain_n': [18, 30], 'new_residue_counts': [58, 94], 'input_files': ['fast-optimum-result.json', 'residual-lattice-output.json'], 'helper_files': ['fast-optimum.py', 'nonmonomial-author.py'], 'candidate_rule': {'EPS': 1e-09, 'ACTIVE': 1e-07, 'ratio_tie': 1e-10, 'pivot_cap': 10000, 'free_denominator_cap': 10 ** 6, 'candidate_calls_per_input': 1, 'reconstructions_per_input': 1}, 'error_type': 'AssertionError', 'error': 'Per-input floating pivot cap', 'actual_worker_exit_code': 1, 'outer_timed_out': False}, 'metadata')
        pass
        for r,o,p in zip(a['records'],old,parent):
            assert time.monotonic()-start<CAP
            out['records'].append(review_record(r,o,p))
        out.update(status='passed', exact_scalar_field_comparisons=own.COUNT, historical_execution_fields={k: a[k] for k in ('actual_worker_exit_code', 'outer_timed_out', 'error')}, solver_replayed=False, failed_n30_not_retried=True)
    except BaseException as exc:
        out.update(status='failed',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass
    pass
    pass;pass
    with output.open('x',encoding='utf-8') as f: json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('records',)}))
    return 0 if out['status']=='passed' else 1

if __name__=='__main__':
    if '--output' in sys.argv: OUT=Path(sys.argv[sys.argv.index('--output')+1]).resolve()
    if '--worker' in sys.argv: sys.exit(worker(OUT))
    if OUT.exists(): raise SystemExit('Refusing to overwrite first independent report')
    start=time.monotonic();p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'joint-budget-review.py')),'--worker','--output',str(OUT)],creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    try: code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        p.kill();p.wait();OUT.write_text(json.dumps({'status': 'incomplete', 'error': 'outer180secondcap'}) + '\n');code=1
    sys.exit(code)
