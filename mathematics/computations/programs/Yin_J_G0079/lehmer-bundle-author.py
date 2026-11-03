"""Sole original-Lehmer N20 integral-bundle candidate and exact certificate."""
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util,json,platform,subprocess,sys,time,traceback

HERE=(_J_PROGRAM / 'lehmer-bundle-author.py').parent
OUTPUT=(_J_OUTPUT / 'lehmer-bundle-output.json')
CAP=180
P=[1,1,0,-1,-1,-1,-1,-1,0,1,1]

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


def helper(name,filename):
    spec=importlib.util.spec_from_file_location(name,((_J_PROGRAM if filename in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / filename))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

lp=helper('lehmer_existing_candidate','fast-optimum.py')
poly=helper('lehmer_existing_division','nonmonomial-author.py')
logs=helper('lehmer_existing_logs','norm-funded-author.py')
rat,vec,dot,rr=lp.rat,lp.vec,lp.dot,logs.rr

def fr(a):
    return F(int(a.p),int(a.q))

def ints(m):
    assert all(a.q==1 for a in m)
    return [[int(a) for a in row] for row in m.tolist()]

def rats(m):
    return [vec([fr(a) for a in row]) for row in m.tolist()]

def remainder(a):
    a=list(a)+[0]*max(0,10-len(a))
    for k in range(len(a)-1,9,-1):
        c=a[k]
        for j,p in enumerate(P):
            a[k-10+j]-=c*p
    return a[:10]

def save(out):
    pending=OUTPUT.with_suffix('.json.pending')
    pending.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    pending.replace(OUTPUT)

def worker():
    from sympy import Matrix,Rational,eye
    import sympy
    start=time.monotonic()
    out={'schema': 'J79-actual-lehmer-joint-bundle-v1', 'status': 'running', 'coefficients': P, 'd': 10, 'N': 20, 'input_scope': 'L170 original degree10 irreducible unit; L323/J80 actual coefficients', 'helper_files': ['fast-optimum.py', 'nonmonomial-author.py', 'norm-funded-author.py'], 'lll_delta': [3, 4], 'declared_residue_count': 28, 'declared_family_count': 48, 'candidate_rule': {'EPS': lp.EPS, 'ACTIVE': lp.ACTIVE, 'ratio_tie': 1e-10, 'pivot_cap': lp.PIVOT_CAP, 'free_denominator_cap': 10 ** 6}, 'family': []}
    save(out)
    def cap():
        if time.monotonic()-start>=CAP:
            raise TimeoutError('Declared aggregate180-second cap')
    try:
        d,N=10,20
        X=Matrix.hstack(*[Matrix(remainder([0]*j+[1])) for j in range(N)])
        A=Matrix(N,N-d,lambda i,j:P[i-j] if 0<=i-j<=d else 0)
        Q,G=X*X.T,A.T*A
        Qi,Gi=Q.inv(),G.inv()
        R=X.T*Qi*X
        assert R==eye(N)-A*Gi*A.T and X*A==Matrix.zeros(d,N-d)
        assert R*R==R and R.T==R and R.trace()==d
        q=lcm(*(int(a.q) for a in R))
        C=q*R;W=q*Gi*A.T;L=C[:,:d]
        assert X*C==q*X and C+A*W==q*eye(N) and X*L==q*eye(d)
        assert C==L*X
        out.update(status='projection-complete',q=q,X_rows=ints(X),A_rows=ints(A),
            Q_rows=ints(Q),G_rows=ints(G),Q_inverse=rats(Qi),G_inverse=rats(Gi),
            R_rows=rats(R),C_rows=ints(C),kernel_multiplier_rows=ints(W),L_rows=ints(L),
            det_Q=int(Q.det(method='domain-ge')),det_G=int(G.det(method='domain-ge')))
        save(out);cap()
        reduced,U=L.T.lll_transform(delta=Rational(3,4))
        Ui=U.inv();detU=int(U.det(method='domain-ge'))
        assert abs(detU)==1 and U*Ui==eye(d) and Ui*U==eye(d) and U*L.T==reduced
        ur=ints(U)
        out.update(status='basis-complete',U_rows=ur,U_inverse_rows=ints(Ui),det_U=detU,
            reduced_rows=ints(reduced))
        save(out)
        seeds=[('basis',i,0,ur[i]) for i in range(d)]
        seeds += [('adjacent',i,s,[ur[i][j]+s*ur[i+1][j] for j in range(d)])
                  for i in range(d-1) for s in [-1,1]]
        log2=logs.series(F(1,3))
        assert F(9,260*3**65)<F(1,logs.GRID)
        out['log2_certificate']=log2
        Crows=ints(C)
        labels=[('monomial',j,0,[int(k==j) for k in range(N)]) for j in range(N)]
        labels += [(kind,i,s,z+[0]*d) for kind,i,s,z in seeds]
        assert len(labels)==48
        for index,(kind,i,s,b) in enumerate(labels):
            cap();assert any(b)
            f=[sum(Crows[k][j]*b[j] for j in range(N)) for k in range(N)]
            up=poly.quotient([q*b[k]-f[k] for k in range(N)],P)
            assert Matrix(f)+A*Matrix(up)==q*Matrix(b)
            nm=Matrix.hstack(*[Matrix(remainder([0]*j+b)) for j in range(d)])
            norm=int(nm.det(method='domain-ge'));assert norm!=0
            if kind=='monomial':
                assert norm==1
            content=gcd(*f);full=q**d*norm
            assert content>0 and full%content**d==0
            E=sum(a*a for a in f)
            H=[sum(f[k]*f[k+h] for k in range(N-h)) for h in range(1,N)]
            cert=logs.logcert(abs(norm),d,log2)
            ell=rr(cert['ell_lower']);assert ell>=0
            out['family'].append({'index':index,'kind':kind,'basis_or_monomial_index':i,'sign':s,
                'B':b,'F_coefficients':f,'kernel_multiplier':up,'norm_matrix':ints(nm),
                'signed_res_B':norm,'D':abs(norm),'signed_res_F':full,'content':content,
                'primitive_coefficients':[a//content for a in f],
                'signed_res_primitive':full//content**d,
                'actual_degree':max(j for j,a in enumerate(f) if a),
                'integer_energy':E,'integer_autocorrelations':H,'e':rat(F(E,q*q)),
                'h':vec([F(a,q*q) for a in H]),'log_certificate':cert,
                'ell':rat(ell),'a':rat(1+2*ell)})
        family=out['family']
        e=[rr(c['e']) for c in family];ell=[rr(c['ell']) for c in family]
        aa=[rr(c['a']) for c in family]
        H=[[rr(c['h'][h]) for c in family] for h in range(N-1)]
        assert sum(e[:N])==d
        assert all(e[j]==e[N-1-j] and aa[j]==aa[N-1-j]==1
                   and all(row[j]==row[N-1-j] for row in H) for j in range(d))
        bv=[F(1,d)]*N+[F(0)]*28
        bcorr=[dot(row,bv) for row in H]
        base=2*sum(abs(a) for a in bcorr)
        assert dot(e,bv)==1 and sum(bv)==2
        baseline={'v':vec(bv),'weights':vec([F(1,N)]*N+[F(0)]*28),
            'correlations':vec(bcorr),'kappa':rat(base),'S':[2,1],
            'energy':rat(F(q*q,2)),'income_log_q':q,'surplus_half_log_argument':2,
            'optimized_monomial_claim':False}
        comp=list(range(d))+list(range(N,48))
        ep=[e[j]/aa[j] for j in comp]
        hp=[[row[j]/aa[j] for j in comp] for row in H]
        out.update(status='matrices-ready',family_count=48,compressed_indices=comp,
            compressed_count=len(comp),r_prime=vec(ep),H_prime=[vec(row) for row in hp],
            uniform_monomial_baseline=baseline,degree_bound=19,radial_multiplier=[19,10])
        save(out)
        cand=lp.tableau([[float(a) for a in row] for row in hp],list(map(float,ep)),cap)
        out.update(status='candidate-returned',floating_candidate=cand);save(out)
        support=[j for j,a in enumerate(cand['pair_masses']) if a>lp.ACTIVE]
        zeros=[h for h,a in enumerate(cand['candidate_correlations']) if abs(a)<lp.ACTIVE]
        tight=abs(sum(cand['pair_masses'])-2)<lp.ACTIVE
        rows,rhs=[[ep[j] for j in support]],[F(1)]
        if tight:
            rows.append([F(1)]*len(support));rhs.append(F(2))
        rows += [[hp[h][j] for j in support] for h in zeros];rhs += [F(0)]*len(zeros)
        approx=[cand['pair_masses'][j] for j in support]
        out['primal_reconstruction_input']={'support':support,'zero_lags':[h+1 for h in zeros],
            'budget_tight':tight,'rows':[vec(row) for row in rows],'rhs':vec(rhs),'approx':approx}
        save(out)
        sub,info=lp.solve_exact(rows,rhs,approx)
        uc=[F(0)]*len(comp)
        for j,a in zip(support,sub):uc[j]=a
        v=[F(0)]*48
        for k,j in enumerate(comp):
            if j<d:v[j]=v[N-1-j]=uc[k]/2
            else:v[j]=uc[k]/aa[j]
        u=[aa[j]*v[j] for j in range(48)]
        S,LL,budget=sum(v),dot(ell,v),dot(aa,v)
        corr=[dot(row,v) for row in H];kappa=2*sum(abs(a) for a in corr)
        out.update(status='primal-reconstructed',primal_reconstruction=info,
            compressed_u=vec(uc),u=vec(u),v=vec(v),S=rat(S),L=rat(LL),budget=rat(budget),
            correlations=vec(corr),kappa=rat(kappa));save(out)
        assert all(a>=0 for a in v) and S>0 and dot(e,v)==1 and budget>=2
        assert S+2*LL==budget==sum(uc) and all(dot(row,uc)==a for row,a in zip(hp,corr))
        y,free=[None]*(N-1),[]
        for h,a in enumerate(corr):
            if a:y[h]=F(1 if a>0 else -1)
            elif abs(abs(cand['y'][h])-1)<lp.ACTIVE:y[h]=F(1 if cand['y'][h]>0 else -1)
            else:free.append(h)
        rows,rhs=[],[]
        for j,a in enumerate(uc):
            if a:
                rows.append([2*hp[h][j] for h in free]+[-ep[j],F(-1)])
                rhs.append(-sum(2*hp[h][j]*y[h] for h in range(N-1) if y[h] is not None))
        if budget>2 or abs(cand['mu'])<lp.ACTIVE:
            rows.append([F(0)]*(len(free)+1)+[F(1)]);rhs.append(F(0))
        approx=[cand['y'][h] for h in free]+[cand['lambda'],cand['mu']]
        out['dual_reconstruction_input']={'free_y_lags':[h+1 for h in free],
            'fixed_y':[None if a is None else rat(a) for a in y],
            'rows':[vec(row) for row in rows],'rhs':vec(rhs),'approx':approx};save(out)
        sol,dinfo=lp.solve_exact(rows,rhs,approx)
        for h,a in zip(free,sol):y[h]=a
        lam,mu=sol[-2:]
        slacks=[2*sum(y[h]*H[h][j] for h in range(N-1))-lam*e[j]-mu*aa[j] for j in range(48)]
        bound=lam+2*mu
        out.update(status='dual-reconstructed',dual_reconstruction=dinfo,y=vec(y),lambda_value=rat(lam),
            mu=rat(mu),dual_slacks=vec(slacks),transformed_slacks=vec([a/b for a,b in zip(slacks,aa)]),
            lower_bound=rat(bound),gap=rat(kappa-bound));save(out)
        assert all(-1<=a<=1 for a in y) and mu>=0 and all(a>=0 for a in slacks)
        assert kappa==bound and mu*(budget-2)==0 and all(v[j]*slacks[j]==0 for j in range(48))
        w=[a/S for a in v];den=lcm(*(a.denominator for a in w));mult=[int(a*den) for a in w]
        aggregate=[0]*(2*N-1)
        for copies,c in zip(mult,family):
            if copies:
                for i,a in enumerate(c['F_coefficients']):
                    for j,b in enumerate(c['F_coefficients']):aggregate[i+N-1-j]+=copies*a*b
        energy=F(q*q)/S;auto=[F(q*q)*a/S for a in corr]
        assert sum(mult)==den and F(aggregate[N-1],den)==energy and aggregate==aggregate[::-1]
        assert all(F(aggregate[N-1+h],den)==auto[h-1] for h in range(1,N))
        assert kappa<=base
        out.update(status='complete',global_finite_family_optimum_certified=True,
            weights=vec(w),weight_denominator=den,multiplicities=mult,
            positive_indices=[j for j,a in enumerate(w) if a],zero_lags=[h+1 for h,a in enumerate(corr) if not a],
            energy=rat(energy),aggregate_autocorrelations=vec(auto),aggregate_polynomial=aggregate,
            income={'log_q_argument':q,'norm_terms':[{'D':c['D'],'coefficient':rat(w[j]/d)} for j,c in enumerate(family)]},
            exact_arithmetic_product={'q_base':q,'q_exponent':d*den,
                'norm_factors':[{'D':c['D'],'exponent':mult[j]} for j,c in enumerate(family)]},
            certified_surplus={'half_log_argument':rat(S),'additional_lower':rat(LL/S),
                'x':rat(S/2),'budget':rat(budget),'at_least_half_log_two':True},
            strictly_below_uniform=kappa<base,kappa_le_4=kappa<=4,
            kappa_ten_thousandth_bin=[kappa.numerator*10000//kappa.denominator,kappa.numerator*10000//kappa.denominator+1])
        cap()
    except BaseException as exc:
        out.update(status='incomplete',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass;pass
    save(out)
    return 0 if out['status']=='complete' else 1

def main():
    if '--worker' in sys.argv:return worker()
    if OUTPUT.exists():raise SystemExit('Refusing to overwrite first native output')
    start=time.monotonic()
    p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'lehmer-bundle-author.py')),'--worker'],
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    timeout=False
    try:code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:timeout=True;p.kill();code=p.wait()
    out=json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {'status':'incomplete','family':[]}
    out.update(actual_worker_exit_code=code, outer_timed_out=timeout)
    if timeout:out.update(status='incomplete',error_type='OuterDeadline',error='Declared aggregate180-second cap')
    save(out)
    print(json.dumps({'status':out['status'],
        'family_count':len(out['family']),'bin':out.get('kappa_ten_thousandth_bin'),
        'error':out.get('error')}),flush=True)
    return 0 if code==0 and not timeout and out['status']=='complete' else 1

if __name__=='__main__':sys.exit(main())
