"""Declared two-input exact lattice/Schur/LLL-candidate test, no enumeration claim."""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util, json, platform, subprocess, sys, time, traceback

HERE = (_J_PROGRAM / 'residual-lattice-author.py').parent
OUTPUT = (_J_OUTPUT / 'residual-lattice-output.json')
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


def helper(name, file):
    spec = importlib.util.spec_from_file_location(name, ((_J_PROGRAM if file in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / file))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# Reuse the frozen SAME-AUTHOR exact scalar/step/log helpers, not their workers.
oldhelp = helper('residual_integer_helpers', 'nonmonomial-author.py')
logs = helper('residual_log_helpers', 'norm-funded-author.py')
rat, vec, dot, invert, quotient = oldhelp.rat, oldhelp.vec, oldhelp.dot, oldhelp.invert, oldhelp.quotient

def rr(x):
    return F(*x)

def save(out):
    OUTPUT.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')

def schur(K):
    d = len(K)
    low = [[F(i == j) for j in range(d)] for i in range(d)]
    pivots = []
    for j in range(d):
        pivot = K[j][j]-sum(low[j][k]**2*pivots[k] for k in range(j))
        pivots.append(pivot)
        if pivot <= 0:
            rhs = [K[k][j] for k in range(j)]
            fwd = []
            for i in range(j):
                fwd.append(rhs[i]-sum(low[i][k]*fwd[k] for k in range(i)))
            mid = [fwd[i]/pivots[i] for i in range(j)]
            sol = [F(0)]*j
            for i in range(j-1, -1, -1):
                sol[i] = mid[i]-sum(low[k][i]*sol[k] for k in range(i+1, j))
            v = [-x for x in sol]+[F(1)]+[F(0)]*(d-j-1)
            denominator = lcm(*(a.denominator for a in v))
            raw = [int(a*denominator) for a in v]
            content = gcd(*raw)
            z = [a//content for a in raw]
            value = dot(z, [dot(row, z) for row in K])
            assert dot(v, [dot(row, v) for row in K]) == pivot
            assert value == pivot*F(denominator, content)**2 <= 0
            later = [K[j][i]-sum(low[j][k]*low[i][k]*pivots[k] for k in range(j))
                     for i in range(j+1,d)]
            return {'status': 'nonpositive_pivot', 'pivot_index': j,
                    'pivots': vec(pivots), 'partial_lower': [vec(row) for row in low],
                    'preceding_rhs': vec(rhs), 'preceding_solution': vec(sol),
                    'rational_witness': vec(v), 'clearing_denominator': denominator,
                    'cleared_content': content, 'integer_witness': z,
                    'quadratic_value': rat(value),
                    'zero_pivot': pivot == 0,
                    'later_schur_couplings': vec(later),
                    'later_offdiagonal_nonzero': any(later)}
        for i in range(j+1, d):
            low[i][j] = (K[i][j]-sum(low[i][k]*low[j][k]*pivots[k] for k in range(j)))/pivot
    assert all(K[i][j] == sum(low[i][k]*pivots[k]*low[j][k] for k in range(d))
               for i in range(d) for j in range(d))
    return {'status': 'positive_definite', 'pivots': vec(pivots),
            'lower': [vec(row) for row in low], 'integer_witness': None}

def quotient_remainder(a, p):
    a = list(a)
    d = len(p)-1
    for i in range(len(a)-1, d-1, -1):
        c = a[i]
        for j in range(d+1):
            a[i-d+j] -= c*p[j]
    return a[:d]

def step(data, E, HB, g, ell, D):
    pair, I, Z, H, r, inv = (data[k] for k in ['pair','I','Z','H','r','inv'])
    a0, K0, mu, d, N, q = (data[k] for k in ['a0','K0','mu','d','N','q'])
    z = [1+2*ell, E]+[HB[h] for h in Z]
    x = [dot(row, z) for row in inv]
    assert all(dot(row, x) == v for row, v in zip(data['M'], z))
    da = [HB[h]-sum(x[k]*H[h][j] for k, j in enumerate(I)) for h in range(N-1)]
    assert all(da[h] == 0 for h in Z)
    slope = g-2*mu*ell
    assert slope == 2*dot(data['y'], da)
    bounds = [('unit', -1, F(1))]
    if ell:
        bounds.append(('mass_total', -1, 1/(2*ell)))
    bounds += [('mass', j, pair[j]/x[k]) for k, j in enumerate(I) if x[k] > 0]
    bounds += [('sign', h+1, abs(a0[h]/da[h])) for h in range(N-1) if a0[h]*da[h] < 0]
    tau = min(a for _, _, a in bounds)
    bp = pair.copy()
    for k, j in enumerate(I):
        bp[j] -= tau*x[k]
    v = [F(0)]*N
    for j, b in enumerate(bp):
        v[j] = v[N-1-j] = b/2
    v.append(tau)
    S = 2-2*ell*tau
    assert all(a >= 0 for a in v) and sum(v) == S and S >= 1
    assert dot(v[:-1], r)+tau*E == 1
    aa = [a0[h]+tau*da[h] for h in range(N-1)]
    assert all(not a0[h] or a0[h]*aa[h] >= 0 for h in range(N-1))
    K = 2*sum(abs(a) for a in aa)
    assert K == K0+tau*slope
    w = [a/S for a in v]
    denom = lcm(*(a.denominator for a in w))
    mult = [int(denom*a) for a in w]
    assert sum(mult) == denom
    return {'ell': rat(ell), 'active_rhs': vec(z), 'old_mass_derivative': vec(x),
            'correlation_derivative': vec(da), 'slope': rat(slope),
            'step_bounds': [{'kind': a, 'index': b, 'value': rat(c)} for a,b,c in bounds],
            'tau': rat(tau), 'limiting_bounds': [i for i, (_,_,a) in enumerate(bounds) if a == tau],
            'pair_masses': vec(bp), 'masses': vec(v), 'S': rat(S), 'weights': vec(w),
            'weight_denominator': denom, 'multiplicities': mult,
            'positive_indices': [i for i,a in enumerate(w) if a],
            'correlations': vec(aa), 'kappa': rat(K), 'strict_improvement': K < K0,
            'kappa_le_4': K <= 4, 'energy': rat(F(q*q)/S),
            'aggregate_autocorrelations': vec([F(q*q)*a/S for a in aa]),
            'income': {'log_q_argument': q, 'log_D_argument': D,
                       'log_D_coefficient': rat(tau/(d*S))},
            'surplus': {'half_log_argument': rat(S), 'extra_log_argument': D,
                        'extra_log_coefficient': rat(tau/(d*S)),
                        'finite_interval_x': rat(ell*tau), 'at_least_half_log_two': True}}

def worker():
    from sympy import Matrix, Rational
    start = time.monotonic()
    out = {'schema': 'J79-integral-residual-lattice-v1', 'status': 'running', 'domain_n': [18, 30], 'lll_delta': [3, 4], 'declared_basis_adjacent_counts': [58, 94], 'max_schur_witnesses': 2, 'input': 'fast-optimum-result.json', 'log2_certificate': logs.series(F(1, 3)), 'records': []}
    save(out)
    try:
        originals = json.loads(((_J_OUTPUT / 'fast-optimum-result.json')).read_text())['records']
        for old in originals:
            n,d,N,q = (old[k] for k in ['n','d','N','q'])
            assert n in [18,30] and N == 2*d
            p,C = old['coefficients'],old['input_C_rows']
            L = [row[:d] for row in C]
            Xcols = [quotient_remainder([0]*j+[1]+[0]*max(0,d-j-1), p) for j in range(N)]
            X = [[Xcols[j][i] for j in range(N)] for i in range(d)]
            assert all(sum(L[i][k]*X[k][j] for k in range(d)) == C[i][j]
                       for i in range(N) for j in range(N))
            assert all(sum(X[i][k]*L[k][j] for k in range(N)) == q*(i==j)
                       for i in range(d) for j in range(d))
            Q = Matrix(X)*Matrix(X).T
            r,H = list(map(rr,old['r'])),[list(map(rr,row)) for row in old['H_rows']]
            y = list(map(rr,old['y']))
            lam,mu,K0 = map(rr,[old['lambda'],old['mu'],old['kappa']])
            den = lcm(lam.denominator,*(a.denominator for a in y))
            Tint = [[int(-lam*den) if i==j else int(y[abs(i-j)-1]*den) for j in range(N)]
                    for i in range(N)]
            Ki = Matrix(L).T*Matrix(Tint)*Matrix(L)
            Kden = den*q*q
            K = [[F(int(Ki[i,j]),Kden) for j in range(d)] for i in range(d)]
            cert = schur(K)
            pair = list(map(rr,old['pair_masses']))
            I = [j for j,a in enumerate(pair) if a]
            a0 = list(map(rr,old['correlations']))
            Z = [h for h,a in enumerate(a0) if not a]
            M = [[F(1) for j in I],[r[j] for j in I]]+[[H[h][j] for j in I] for h in Z]
            inv = invert(M)
            data = dict(pair=pair,I=I,Z=Z,H=H,r=r,inv=inv,M=M,a0=a0,K0=K0,mu=mu,d=d,N=N,q=q,y=y)
            rec = {'n':n,'d':d,'N':N,'q':q,'coefficients':p,'X_rows':X,'L_rows':L,
                   'Q_rows':[[int(Q[i,j]) for j in range(d)] for i in range(d)],
                   'det_Q':int(Q.det(method='domain-ge')),'signed_correlation_integer_matrix':Tint,
                   'signed_correlation_denominator':den,'K_rows':[vec(row) for row in K],
                   'schur_certificate':cert,'old_r':vec(r),'old_H':[vec(row) for row in H],
                   'old_y':vec(y),'old_lambda':rat(lam),'old_mu':rat(mu),'old_kappa':rat(K0),
                   'old_pair_masses':vec(pair),'old_zero_lags':[h+1 for h in Z],
                   'active_matrix':[vec(row) for row in M],'active_inverse':[vec(row) for row in inv],
                   'degree_bound':N-1,'radial_multiplier':rat(F(N-1,d)),
                   'lll_status':'not_started','candidates':[],'status':'running'}
            out['records'].append(rec)
            save(out)
            # Blocking library call is covered by the outer aggregate deadline.
            reduced,U = Matrix(L).T.lll_transform(delta=Rational(3,4))
            Ui = U.inv()
            detU = int(U.det(method='domain-ge'))
            assert abs(detU)==1 and U*Matrix(L).T==reduced
            assert all(a.q==1 for a in Ui)
            assert U*Ui==Matrix.eye(d) and Ui*U==Matrix.eye(d)
            rows = [[int(U[i,j]) for j in range(d)] for i in range(d)]
            rec.update(lll_status='complete',U_rows=rows,U_inverse_rows=[[int(Ui[i,j]) for j in range(d)] for i in range(d)],
                       det_U=detU,reduced_rows=[[int(reduced[i,j]) for j in range(N)] for i in range(d)])
            seeds = [('basis',i,0,rows[i]) for i in range(d)]
            seeds += [('adjacent',i,s,[rows[i][j]+s*rows[i+1][j] for j in range(d)])
                      for i in range(d-1) for s in [-1,1]]
            if cert['integer_witness'] is not None:
                seeds.append(('schur',cert['pivot_index'],0,cert['integer_witness']))
            assert len(seeds)==3*d-2+(cert['integer_witness'] is not None)
            for index,(kind,i,s,z) in enumerate(seeds):
                assert time.monotonic()-start<CAP,'Worker elapsed cap'
                assert any(z)
                b=z+[0]*(N-d)
                f=[sum(L[k][j]*z[j] for j in range(d)) for k in range(N)]
                up=quotient([q*b[k]-f[k] for k in range(N)],p)
                content=gcd(*f)
                normcols=[quotient_remainder([0]*j+z,p) for j in range(d)]
                normmatrix=[[normcols[j][k] for j in range(d)] for k in range(d)]
                signed_norm=int(Matrix(normmatrix).det(method='domain-ge'))
                assert signed_norm != 0 and content>0
                D=abs(signed_norm)
                full=q**d*signed_norm
                assert full%content**d==0
                energy=sum(a*a for a in f)
                autocorr=[sum(f[k]*f[k+h] for k in range(N-h)) for h in range(1,N)]
                E,HB=F(energy,q*q),[F(a,q*q) for a in autocorr]
                value=dot(z,[dot(row,z) for row in K])
                g=value-mu
                assert g==2*dot(y,HB)-lam*E-mu
                if kind=='schur':
                    assert value<=0 and g<0
                log=logs.logcert(D,d,out['log2_certificate'])
                ell,ellU=rr(log['ell_lower']),rr(log['ell_upper'])
                conservative=step(data,E,HB,g,F(0),D)
                funded=step(data,E,HB,g,ell,D)
                low,high=g-2*mu*ellU,g-2*mu*ell
                slope_status='negative' if high<0 else 'nonnegative' if low>=0 else 'undecided'
                rec['candidates'].append({'kind':kind,'basis_index':i,'sign':s,'z':z,'B':b,
                    'F_coefficients':f,'kernel_multiplier':up,'content':content,
                    'primitive_coefficients':[a//content for a in f],
                    'actual_degree':max(k for k,a in enumerate(f) if a),
                    'norm_matrix':normmatrix,'signed_res_B':signed_norm,'signed_res_F':full,
                    'signed_res_primitive':full//content**d,'integer_energy':energy,'e_B':rat(E),
                    'integer_autocorrelations':autocorr,'h_B':vec(HB),'quadratic_value':rat(value),
                    'reduced_cost':rat(g),'log_certificate':log,
                    'exact_log_slope_interval':[rat(low),rat(high)],'exact_log_slope_decision':slope_status,
                    'conservative_step':conservative,'norm_funded_step':funded})
                if (index+1)%16==0:
                    save(out)
            rec['candidate_count']=len(rec['candidates'])
            for name in ['conservative_step','norm_funded_step']:
                rec[name+'_summary']={'improvement_count':sum(c[name]['strict_improvement'] for c in rec['candidates']),
                    'kappa_le_4_count':sum(c[name]['kappa_le_4'] for c in rec['candidates']),
                    'best_index':min(range(len(rec['candidates'])),key=lambda i:rr(rec['candidates'][i][name]['kappa']))}
            rec['status']='complete'
            save(out)
        out['status']='complete'
    except BaseException as e:
        out['status']='failed'
        out['error']=_record_text(repr(e))
        out['traceback']=_record_text(traceback.format_exc())
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
    p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'residual-lattice-author.py')),'--worker'])
    timeout=False
    try:
        code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        timeout=True
        p.kill()
        code=p.wait()
    out=json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {'records':[]}
    if timeout:
        out['status']='timeout'
    pass
    out['actual_worker_exit_code']=code
    out['outer_timed_out']=timeout
    save(out)
    print(json.dumps({'status':out['status'],
          'records':[{'n':r['n'],'schur':r['schur_certificate']['status'],'lll':r['lll_status'],
                      'count':len(r['candidates']),'conservative':r.get('conservative_step_summary'),
                      'funded':r.get('norm_funded_step_summary')} for r in out['records']]}))
    return 0 if out.get('status')=='complete' and code==0 else 1

if __name__=='__main__':
    sys.exit(main())
