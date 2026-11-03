"""Whole independent Lehmer bundle check; no author imports/LLL/optimizer.

Own preceding exact/log helper and active-system solver explicitly reused.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from fractions import Fraction as Q
from datetime import datetime
from math import gcd,lcm
import importlib.util,json,sys,time,traceback,subprocess,platform
import sympy as sp
HERE=(_J_PROGRAM / 'lehmer-bundle-review.py').parent
OUT=(_J_OUTPUT / 'lehmer-bundle-review-result.json')
CAP=180

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


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,((_J_PROGRAM if file in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / file))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
own=load('own_exact','nonmonomial-norm-review.py')
prior=load('own_joint','joint-budget-review.py')
same,enc,seq,dec,dot,conv=own.same,own.enc,own.seq,own.dec,own.dot,own.conv

def inverse(A):
    n=len(A); B=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if B[i][j]);B[j],B[k]=B[k],B[j]
        z=B[j][j];B[j]=[x/z for x in B[j]]
        for i in range(n):
            if i!=j:
                z=B[i][j];B[i]=[x-z*y for x,y in zip(B[i],B[j])]
    assert [row[:n] for row in B]==[[int(i==j) for j in range(n)] for i in range(n)]
    return sp.Matrix([row[n:] for row in B])

def integers(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]
def rationals(M):return [seq([Q(x) for x in row]) for row in M.tolist()]

def float_check(c,hp,ep):
    # Reuse the reviewer's own complete direct-equation checker, with ONLY its
    # two historical pivot-count literals specialized to this declared run.
    # The copied callable's algorithm is not author simplex code.
    import inspect
    source=inspect.getsource(prior.inspect_float)
    source=source.replace('==1929','==283').replace('[1707,222]','[257,26]')
    space=dict(prior.__dict__);exec(compile(source,str((_J_PROGRAM / 'lehmer-bundle-review.py')),'exec'),space)
    return space['inspect_float'](c,hp,ep)

def review(a):
    p=[1,1,0,-1,-1,-1,-1,-1,0,1,1];d,N=10,20
    # Integral companion matrix, evaluated by matrix powers, reconstructs X
    # and every multiplication matrix; no saved quotient table is an input.
    T=sp.zeros(d)
    for j in range(d-1):T[j+1,j]=1
    for j in range(d):T[j,d-1]=-p[j]
    unit=sp.eye(d)[:,0]
    X=sp.Matrix.hstack(*[(T**j)*unit for j in range(N)])
    A=sp.zeros(N,d)
    for j in range(d):
        for k,x in enumerate(p):A[j+k,j]=x
    Qm=X*X.T;G=A.T*A;Qi=inverse(integers(Qm));Gi=inverse(integers(G))
    assert Qm*Qi==Qi*Qm==G*Gi==Gi*G==sp.eye(d)
    R=X.T*Qi*X;assert R==sp.eye(N)-A*Gi*A.T and X*A==sp.zeros(d)
    assert R*R==R and R.T==R and R.trace()==d
    q=lcm(*(int(x.q) for x in R));C=q*R;W=q*Gi*A.T;Lmat=C[:,:d]
    assert C+A*W==q*sp.eye(N) and X*C==q*X and C==Lmat*X and X*Lmat==q*sp.eye(d)
    exp={'schema': 'J79-actual-lehmer-joint-bundle-v1', 'status': 'complete', 'coefficients': p, 'd': d, 'N': N, 'input_scope': 'L170 original degree10 irreducible unit; L323/J80 actual coefficients', 'helper_files': ['fast-optimum.py', 'nonmonomial-author.py', 'norm-funded-author.py'], 'lll_delta': [3, 4], 'declared_residue_count': 28, 'declared_family_count': 48, 'candidate_rule': {'EPS': 1e-09, 'ACTIVE': 1e-07, 'ratio_tie': 1e-10, 'pivot_cap': 10000, 'free_denominator_cap': 10 ** 6}, 'q': q, 'X_rows': integers(X), 'A_rows': integers(A), 'Q_rows': integers(Qm), 'G_rows': integers(G), 'Q_inverse': rationals(Qi), 'G_inverse': rationals(Gi), 'R_rows': rationals(R), 'C_rows': integers(C), 'kernel_multiplier_rows': integers(W), 'L_rows': integers(Lmat), 'det_Q': int(Qm.det(method='domain-ge')), 'det_G': int(G.det(method='domain-ge')), 'actual_worker_exit_code': 0, 'outer_timed_out': False}
    assert q==26487 and exp['det_Q']==exp['det_G']==79461
    U=sp.Matrix(a['U_rows']);Ui=inverse(a['U_rows'])
    assert U*Ui==Ui*U==sp.eye(d) and all(x.q==1 for x in Ui)
    detU=int(U.det(method='domain-ge'));assert detU==-1
    exp.update(U_rows=integers(U),U_inverse_rows=integers(Ui),det_U=detU,reduced_rows=integers(U*Lmat.T),
               log2_certificate=own.series(Q(1,3)))
    family=[];t=sp.Symbol('t');P=sp.Poly.from_list(p[::-1],t,domain=sp.ZZ)
    for idx in range(48):
        if idx<N:kind,j,s='monomial',idx,0;b=[int(k==j) for k in range(N)]
        else:
            r=idx-N
            if r<d:kind,j,s='basis',r,0
            else:kind,j,s='adjacent',(r-d)//2,(-1 if (r-d)%2==0 else 1)
            b=[int(U[j,k]+(s*U[j+1,k] if s else 0)) for k in range(d)]+[0]*d
        assert any(b)
        f=[int(x) for x in C*sp.Matrix(b)];up=[int(x) for x in W*sp.Matrix(b)]
        assert all(x.q==1 for x in W*sp.Matrix(b)) and conv(p,up)==[q*x-y for x,y in zip(b,f)]
        Bmatrix=sp.zeros(d)
        for coeff in b[::-1]:Bmatrix=Bmatrix*T+coeff*sp.eye(d)
        nb=int(sp.resultant(P,sp.Poly.from_list(b[::-1],t,domain=sp.ZZ)))
        assert nb!=0 and int(Bmatrix.det(method='domain-ge'))==nb
        content=gcd(*f);nf=q**d*nb;assert nf%content**d==0
        ac=own.correlations(f);energy=sum(x*x for x in f);cert=own.logcert(abs(nb),d);ell=dec(cert['ell_lower'])
        family.append({'index':idx,'kind':kind,'basis_or_monomial_index':j,'sign':s,'B':b,
          'F_coefficients':f,'kernel_multiplier':up,'norm_matrix':integers(Bmatrix),
          'signed_res_B':nb,'D':abs(nb),'signed_res_F':nf,'content':content,
          'primitive_coefficients':[x//content for x in f],'signed_res_primitive':nf//content**d,
          'actual_degree':max(k for k,x in enumerate(f) if x),'integer_energy':energy,'integer_autocorrelations':ac,
          'e':enc(Q(energy,q*q)),'h':seq([Q(x,q*q) for x in ac]),'log_certificate':cert,'ell':enc(ell),'a':enc(1+2*ell)})
    e=[dec(c['e']) for c in family];ell=[dec(c['ell']) for c in family];aa=[1+2*x for x in ell]
    H=[[dec(c['h'][h]) for c in family] for h in range(N-1)]
    assert sum(e[:N])==d and all(e[j]==e[N-1-j] and aa[j]==aa[N-1-j]==1 and all(row[j]==row[N-1-j] for row in H) for j in range(d))
    bv=[Q(1,d)]*N+[Q(0)]*28;bcorr=[dot(row,bv) for row in H];base=2*sum(map(abs,bcorr))
    assert dot(e,bv)==1 and sum(bv)==2 and base==Q(443186,132435)
    baseline={'v':seq(bv),'weights':seq([Q(1,N)]*N+[Q(0)]*28),'correlations':seq(bcorr),'kappa':enc(base),
              'S':[2,1],'energy':enc(Q(q*q,2)),'income_log_q':q,'surplus_half_log_argument':2,'optimized_monomial_claim':False}
    comp=list(range(d))+list(range(N,48));ep=[e[j]/aa[j] for j in comp];hp=[[row[j]/aa[j] for j in comp] for row in H]
    exp.update(family=family,family_count=48,compressed_indices=comp,compressed_count=38,r_prime=seq(ep),H_prime=[seq(row) for row in hp],
               uniform_monomial_baseline=baseline,degree_bound=19,radial_multiplier=[19,10])
    fc=a['floating_candidate']; freport=float_check(fc,hp,ep)
    support=[j for j,x in enumerate(fc['pair_masses']) if x>1e-7]
    zeros=[h for h,x in enumerate(fc['candidate_correlations']) if abs(x)<1e-7]
    assert abs(sum(fc['pair_masses'])-2)<1e-7
    rows=[[ep[j] for j in support],[Q(1)]*len(support)]+[[hp[h][j] for j in support] for h in zeros]
    rhs=[Q(1),Q(2)]+[Q(0)]*len(zeros)
    pin={'support':support,'zero_lags':[h+1 for h in zeros],'budget_tight':True,'rows':[seq(row) for row in rows],
         'rhs':seq(rhs),'approx':[fc['pair_masses'][j] for j in support]}
    sub,pinfo=prior.solve(rows,rhs);uc=[Q(0)]*38
    for j,x in zip(support,sub):uc[j]=x
    v=[Q(0)]*48
    for k,j in enumerate(comp):
        if j<d:v[j]=v[N-1-j]=uc[k]/2
        else:v[j]=uc[k]/aa[j]
    u=[x*y for x,y in zip(aa,v)];S=sum(v);LL=dot(ell,v);budget=dot(aa,v);corr=[dot(row,v) for row in H];K=2*sum(map(abs,corr))
    assert min(v)>=0 and dot(e,v)==1 and 0<S<2 and S+2*LL==budget==sum(uc)==2
    y=[None]*(N-1);free=[]
    for h,x in enumerate(corr):
        if x:y[h]=Q(1 if x>0 else -1)
        elif abs(abs(fc['y'][h])-1)<1e-7:y[h]=Q(1 if fc['y'][h]>0 else -1)
        else:free.append(h)
    rows=[];rhs=[]
    for j,x in enumerate(uc):
        if x:
            rows.append([2*hp[h][j] for h in free]+[-ep[j],Q(-1)])
            rhs.append(-sum(2*hp[h][j]*y[h] for h in range(N-1) if y[h] is not None))
    assert budget==2 and abs(fc['mu'])>=1e-7
    din={'free_y_lags':[h+1 for h in free],'fixed_y':[None if x is None else enc(x) for x in y],
         'rows':[seq(row) for row in rows],'rhs':seq(rhs),'approx':[fc['y'][h] for h in free]+[fc['lambda'],fc['mu']]}
    sol,dinfo=prior.solve(rows,rhs)
    for h,x in zip(free,sol):y[h]=x
    lam,mu=sol[-2:];slacks=[2*dot(y,[row[j] for row in H])-lam*e[j]-mu*aa[j] for j in range(48)]
    assert max(map(abs,y))<=1 and lam<0 and mu>0 and min(slacks)>=0 and K==lam+2*mu
    assert all(x*z==0 for x,z in zip(v,slacks))
    w=[x/S for x in v];M=lcm(*(x.denominator for x in w));mult=[int(M*x) for x in w]
    aggregate=[0]*39
    for count,c in zip(mult,family):
        for j,x in enumerate(conv(c['F_coefficients'],c['F_coefficients'][::-1])):aggregate[j]+=count*x
    energy=Q(q*q)/S;ac=[q*q*x/S for x in corr]
    assert sum(mult)==M and aggregate==aggregate[::-1] and Q(aggregate[19],M)==energy
    assert [Q(aggregate[19+h],M) for h in range(1,N)]==ac
    exp.update(primal_reconstruction_input=pin,primal_reconstruction=pinfo,compressed_u=seq(uc),u=seq(u),v=seq(v),
       S=enc(S),L=enc(LL),budget=enc(budget),correlations=seq(corr),kappa=enc(K),
       dual_reconstruction_input=din,dual_reconstruction=dinfo,y=seq(y),lambda_value=enc(lam),mu=enc(mu),
       dual_slacks=seq(slacks),transformed_slacks=seq([x/z for x,z in zip(slacks,aa)]),lower_bound=enc(lam+2*mu),gap=[0,1],
       global_finite_family_optimum_certified=True,weights=seq(w),weight_denominator=M,multiplicities=mult,
       positive_indices=[j for j,x in enumerate(w) if x],zero_lags=[h+1 for h,x in enumerate(corr) if not x],
       energy=enc(energy),aggregate_autocorrelations=seq(ac),aggregate_polynomial=aggregate,
       income={'log_q_argument':q,'norm_terms':[{'D':c['D'],'coefficient':enc(w[j]/d)} for j,c in enumerate(family)]},
       exact_arithmetic_product={'q_base':q,'q_exponent':d*M,'norm_factors':[{'D':c['D'],'exponent':mult[j]} for j,c in enumerate(family)]},
       certified_surplus={'half_log_argument':enc(S),'additional_lower':enc(LL/S),'x':enc(S/2),'budget':enc(budget),'at_least_half_log_two':True},
       strictly_below_uniform=K<base,kappa_le_4=K<=4,kappa_ten_thousandth_bin=[K.numerator*10000//K.denominator,K.numerator*10000//K.denominator+1])
    assert set(a)==set(exp)|{'floating_candidate'}
    same({k:v for k,v in a.items() if k != 'floating_candidate'},exp,'whole-native')
    pass
    assert family[7]['content']==family[12]['content']==3 and family[47]['content']==1
    assert family[47]['B']==[int(j in (2,4)) for j in range(20)] and family[47]['D']==9
    assert K==Q(16019300828244880114628,5290823672429397181749)
    assert M==84149520269621413984 and exp['positive_indices']==[4,5,6,7,12,13,14,15,47]
    return {'all_directions': 48, 'full_norm_matrix_entries': 4800, 'signed_norms': 48, 'primal_rank': pinfo['rank'], 'dual_rank': dinfo['rank'], 'kappa': enc(K), 'uniform_baseline': enc(base), 'content_control': {'C7': 3, 'C12': 3, 'selected_binomial_F': 1}, 'all_native_exact_fields_checked': True, 'floating_provenance_consistency': freport}

def worker(output):
    start=time.perf_counter()
    names=['lehmer-bundle-author.py','lehmer-bundle-output.json','nonmonomial-norm-review.py','joint-budget-review.py']
    before={n:(((_J_PROGRAM if n in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / n)).read_bytes() for n in names}
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0215.md');db=draft.read_bytes() if draft.exists() else None
    out={'schema': 'J79-actual-lehmer-independent-review-v1'}
    try:
        out['complete_result']=review(json.loads(before['lehmer-bundle-output.json']))
        out.update(status='passed',exact_scalar_comparisons=own.COUNT,author_replayed=False,lll_replayed=False,optimizer_replayed=False)
    except BaseException as exc:out.update(status='failed',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass
    pass
    pass;pass
    with output.open('x',encoding='utf8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='complete_result'}));return 0 if out['status']=='passed' else 1

if __name__=='__main__':
    if '--output' in sys.argv:OUT=Path(sys.argv[sys.argv.index('--output')+1]).resolve()
    if '--worker' in sys.argv:sys.exit(worker(OUT))
    if OUT.exists():raise SystemExit('Preserve first review report')
    start=time.perf_counter();p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'lehmer-bundle-review.py')),'--worker','--output',str(OUT)],creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    try:code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        p.kill();p.wait();code=1
        if not OUT.exists():OUT.write_text(json.dumps({'status': 'incomplete', 'error': 'outer180secondcap'}) + '\n')
    sys.exit(code)
