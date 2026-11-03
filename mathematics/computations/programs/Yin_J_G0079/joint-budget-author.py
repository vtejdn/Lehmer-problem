"""One declared joint-budget LP candidate/reconstruction for each frozen input."""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util, json, platform, subprocess, sys, time, traceback

HERE = (_J_PROGRAM / 'joint-budget-author.py').parent
OUTPUT = (_J_OUTPUT / 'joint-budget-output.json')
CAP = 180

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


def helper(name, filename):
    spec = importlib.util.spec_from_file_location(name, ((_J_PROGRAM if filename in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# Guarded imports reuse candidate/reconstruction and scalar arithmetic only.
# No upstream worker or main runs, and upstream outputs are read-only.
lp = helper('joint_existing_candidate', 'fast-optimum.py')
poly = helper('joint_existing_polynomial', 'nonmonomial-author.py')
rat, vec, dot = lp.rat, lp.vec, lp.dot

def rr(x):
    return F(*x)

def save(data):
    pending = OUTPUT.with_suffix('.json.pending')
    pending.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    pending.replace(OUTPUT)

def worker():
    start = time.monotonic()
    out = {'schema': 'J79-joint-norm-budget-v1', 'status': 'running', 'domain_n': [18, 30], 'new_residue_counts': [58, 94], 'input_files': ['fast-optimum-result.json', 'residual-lattice-output.json'], 'helper_files': ['fast-optimum.py', 'nonmonomial-author.py'], 'candidate_rule': {'EPS': lp.EPS, 'ACTIVE': lp.ACTIVE, 'ratio_tie': 1e-10, 'pivot_cap': lp.PIVOT_CAP, 'free_denominator_cap': 10 ** 6, 'candidate_calls_per_input': 1, 'reconstructions_per_input': 1}, 'records': []}
    save(out)
    def cap():
        if time.monotonic()-start >= CAP:
            raise TimeoutError('Declared aggregate180-second cap')
    try:
        olddata=json.loads(((_J_OUTPUT / 'fast-optimum-result.json')).read_text())['records']
        lattice=json.loads(((_J_OUTPUT / 'residual-lattice-output.json')).read_text())
        assert lattice['status']=='complete'
        for old, parent in zip(olddata,lattice['records']):
            cap()
            n,d,N,q=(old[k] for k in ['n','d','N','q'])
            assert n==parent['n'] and n in (18,30) and N==2*d
            p,C=old['coefficients'],old['input_C_rows']
            assert p==parent['coefficients'] and len(parent['candidates'])==3*d-2
            family=[]
            for j in range(N):
                b=[int(i==j) for i in range(N)]
                f=[C[i][j] for i in range(N)]
                up=poly.quotient([q*b[k]-f[k] for k in range(N)],p)
                norm=((-1)**d*p[0])**j
                family.append({'kind':'monomial','index':j,'B':b,'F_coefficients':f,
                    'kernel_multiplier':up,'signed_res_B':norm,'signed_res_F':q**d*norm,
                    'content':gcd(*f),'ell':[0,1],'log_certificate':None})
            for j,c in enumerate(parent['candidates']):
                family.append({'kind':'frozen_residue','index':j,
                    'seed_kind':c['kind'],'basis_index':c['basis_index'],'seed_sign':c['sign'],
                    'z':c['z'],'B':c['B'],'F_coefficients':c['F_coefficients'],
                    'kernel_multiplier':c['kernel_multiplier'],'signed_res_B':c['signed_res_B'],
                    'signed_res_F':c['signed_res_F'],'content':c['content'],
                    'ell':c['log_certificate']['ell_lower'],'log_certificate':c['log_certificate']})
            for rec in family:
                f,b,up=rec['F_coefficients'],rec['B'],rec['kernel_multiplier']
                assert len(f)==N and len(b)==N and rec['content']==gcd(*f)>0
                conv=[0]*N
                for i,a in enumerate(up):
                    for j,c in enumerate(p):
                        conv[i+j]+=a*c
                assert all(f[k]+conv[k]==q*b[k] for k in range(N))
                assert rec['signed_res_F']==q**d*rec['signed_res_B']!=0
                norm=abs(rec['signed_res_B'])
                ell=rr(rec['ell'])
                assert ell>=0
                E=sum(a*a for a in f)
                H=[sum(f[k]*f[k+h] for k in range(N-h)) for h in range(1,N)]
                content=rec['content']
                assert rec['signed_res_F']%content**d==0
                rec.update(D=norm,integer_energy=E,integer_autocorrelations=H,
                    e=rat(F(E,q*q)),h=vec([F(a,q*q) for a in H]),a=rat(1+2*ell),
                    primitive_coefficients=[a//content for a in f],
                    signed_res_primitive=rec['signed_res_F']//content**d,
                    actual_degree=max(i for i,a in enumerate(f) if a))
            e=[rr(c['e']) for c in family]
            ell=[rr(c['ell']) for c in family]
            aa=[rr(c['a']) for c in family]
            H=[[rr(c['h'][h]) for c in family] for h in range(N-1)]
            assert all(e[j]==e[N-1-j] and aa[j]==aa[N-1-j]==1
                       and all(row[j]==row[N-1-j] for row in H) for j in range(d))
            compressed=list(range(d))+list(range(N,len(family)))
            ep=[e[j]/aa[j] for j in compressed]
            hp=[[row[j]/aa[j] for j in compressed] for row in H]
            rec={'n':n,'d':d,'N':N,'q':q,'coefficients':p,'status':'matrices-ready',
                 'family':family,'family_count':len(family),'compressed_indices':compressed,
                 'compressed_count':len(compressed),'r_prime':vec(ep),
                 'H_prime':[vec(row) for row in hp],
                 'degree_bound':N-1,'radial_multiplier':rat(F(N-1,d))}
            out['records'].append(rec)
            save(out)
            candidate=lp.tableau([[float(a) for a in row] for row in hp],list(map(float,ep)),cap)
            rec.update(status='candidate-returned',floating_candidate=candidate)
            save(out)
            support=[j for j,a in enumerate(candidate['pair_masses']) if a>lp.ACTIVE]
            zeros=[h for h,a in enumerate(candidate['candidate_correlations']) if abs(a)<lp.ACTIVE]
            tight=abs(sum(candidate['pair_masses'])-2)<lp.ACTIVE
            rows,rhs=[[ep[j] for j in support]],[F(1)]
            if tight:
                rows.append([F(1)]*len(support)); rhs.append(F(2))
            rows += [[hp[h][j] for j in support] for h in zeros]
            rhs += [F(0)]*len(zeros)
            approx=[candidate['pair_masses'][j] for j in support]
            rec['primal_reconstruction_input']={'support':support,'zero_lags':[h+1 for h in zeros],
                'budget_tight':tight,'rows':[vec(row) for row in rows],'rhs':vec(rhs),'approx':approx}
            save(out)
            sub,info=lp.solve_exact(rows,rhs,approx)
            uc=[F(0)]*len(compressed)
            for j,a in zip(support,sub):
                uc[j]=a
            v=[F(0)]*len(family)
            for k,j in enumerate(compressed):
                if j<d:
                    v[j]=v[N-1-j]=uc[k]/2
                else:
                    v[j]=uc[k]/aa[j]
            u=[aa[j]*v[j] for j in range(len(v))]
            S,L,A=sum(v),dot(ell,v),dot(aa,v)
            corr=[dot(row,v) for row in H]
            kappa=2*sum(abs(a) for a in corr)
            rec.update(status='primal-reconstructed',primal_reconstruction=info,
                compressed_u=vec(uc),u=vec(u),v=vec(v),S=rat(S),L=rat(L),budget=rat(A),
                correlations=vec(corr),kappa=rat(kappa))
            save(out)
            assert all(a>=0 for a in v) and S>0 and dot(e,v)==1 and A>=2
            assert S+2*L==A==sum(uc) and all(dot(row,uc)==a for row,a in zip(hp,corr))
            y,free=[None]*(N-1),[]
            for h,a in enumerate(corr):
                if a:
                    y[h]=F(1 if a>0 else -1)
                elif abs(abs(candidate['y'][h])-1)<lp.ACTIVE:
                    y[h]=F(1 if candidate['y'][h]>0 else -1)
                else:
                    free.append(h)
            rows,rhs=[],[]
            for j,a in enumerate(uc):
                if a:
                    rows.append([2*hp[h][j] for h in free]+[-ep[j],F(-1)])
                    rhs.append(-sum(2*hp[h][j]*y[h] for h in range(N-1) if y[h] is not None))
            if A>2 or abs(candidate['mu'])<lp.ACTIVE:
                rows.append([F(0)]*(len(free)+1)+[F(1)]);rhs.append(F(0))
            approx=[candidate['y'][h] for h in free]+[candidate['lambda'],candidate['mu']]
            rec['dual_reconstruction_input']={'free_y_lags':[h+1 for h in free],
                'fixed_y':[None if a is None else rat(a) for a in y],
                'rows':[vec(row) for row in rows],'rhs':vec(rhs),'approx':approx}
            save(out)
            sol,dinfo=lp.solve_exact(rows,rhs,approx)
            for h,a in zip(free,sol):
                y[h]=a
            lam,mu=sol[-2:]
            slacks=[2*sum(y[h]*H[h][j] for h in range(N-1))-lam*e[j]-mu*aa[j]
                    for j in range(len(family))]
            lower=lam+2*mu
            rec.update(status='dual-reconstructed',dual_reconstruction=dinfo,y=vec(y),
                lambda_value=rat(lam),mu=rat(mu),dual_slacks=vec(slacks),
                transformed_slacks=vec([a/b for a,b in zip(slacks,aa)]),
                lower_bound=rat(lower),gap=rat(kappa-lower))
            save(out)
            assert all(-1<=a<=1 for a in y) and mu>=0 and all(a>=0 for a in slacks)
            assert kappa==lower and all(v[j]*slacks[j]==0 for j in range(len(v)))
            assert mu*(A-2)==0
            w=[a/S for a in v]
            denominator=lcm(*(a.denominator for a in w))
            mult=[int(a*denominator) for a in w]
            aggregate=[0]*(2*N-1)
            for copies,c in zip(mult,family):
                if copies:
                    for i,a in enumerate(c['F_coefficients']):
                        for j,b in enumerate(c['F_coefficients']):
                            aggregate[i+N-1-j]+=copies*a*b
            energy=F(q*q)/S
            autocorr=[F(q*q)*a/S for a in corr]
            assert sum(mult)==denominator and F(aggregate[N-1],denominator)==energy
            assert all(F(aggregate[N-1+h],denominator)==autocorr[h-1] for h in range(1,N))
            assert aggregate==aggregate[::-1]
            oldK=rr(old['kappa'])
            previous={name:[rr(c[name]['kappa']) for c in parent['candidates']]
                      for name in ['conservative_step','norm_funded_step']}
            comparisons={name:{'all_previous_kappa':vec(vals),'minimum':rat(min(vals)),
                'strictly_below_all':kappa<min(vals),'at_most_all':kappa<=min(vals)}
                for name,vals in previous.items()}
            assert all(x['at_most_all'] for x in comparisons.values())
            rec.update(status='complete',global_finite_family_optimum_certified=True,
                weights=vec(w),weight_denominator=denominator,multiplicities=mult,
                positive_indices=[j for j,a in enumerate(w) if a],
                zero_lags=[h+1 for h,a in enumerate(corr) if not a],
                energy=rat(energy),aggregate_autocorrelations=vec(autocorr),
                aggregate_polynomial=aggregate,
                income={'log_q_argument':q,'norm_terms':[{'D':c['D'],
                    'coefficient':rat(w[j]/d)} for j,c in enumerate(family)]},
                exact_arithmetic_product={'q_base':q,'q_exponent':d*denominator,
                    'norm_factors':[{'D':c['D'],'exponent':mult[j]} for j,c in enumerate(family)]},
                certified_surplus={'half_log_argument':rat(S),'additional_lower':rat(L/S),
                    'x':rat(S/2),'budget':rat(A),'at_least_half_log_two':True},
                old_kappa=rat(oldK),strictly_below_old=kappa<oldK,
                comparisons= comparisons,kappa_le_4=kappa<=4,
                kappa_ten_thousandth_bin=[kappa.numerator*10000//kappa.denominator,
                                          kappa.numerator*10000//kappa.denominator+1])
            cap();save(out)
            print(json.dumps({'n':n,'status':rec['status'],'bin':rec['kappa_ten_thousandth_bin'],
                'support':rec['positive_indices'],'pivots':candidate['pivot_count']}),flush=True)
        out['status']='complete'
    except BaseException as exc:
        out.update(status='incomplete',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass
    pass
    save(out)
    return 0 if out['status']=='complete' else 1

def main():
    if '--worker' in sys.argv:
        return worker()
    if OUTPUT.exists():
        raise SystemExit('Refusing to overwrite first native output')
    start=time.monotonic()
    proc=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'joint-budget-author.py')),'--worker'],
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    timeout=False
    try:
        code=proc.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        timeout=True;proc.kill();code=proc.wait()
    out=json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {'records':[],'status':'incomplete'}
    out.update(actual_worker_exit_code=code, outer_timed_out=timeout)
    if timeout:
        out.update(status='incomplete',error_type='OuterDeadline',error='Declared aggregate180-second cap')
    save(out)
    print(json.dumps({'status':out['status'],
        'error':out.get('error'),'records':[{'n':r['n'],'status':r['status'],
        'bin':r.get('kappa_ten_thousandth_bin')} for r in out['records']]}),flush=True)
    return 0 if code==0 and not timeout and out['status']=='complete' else 1

if __name__=='__main__':
    sys.exit(main())
