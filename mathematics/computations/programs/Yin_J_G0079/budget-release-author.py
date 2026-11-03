"""One exact n18 active-budget release; no optimization or new directions."""
from fractions import Fraction as F
from math import lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util,json,platform,subprocess,sys,time,traceback

HERE=(_J_PROGRAM / 'budget-release-author.py').parent
OUTPUT=(_J_OUTPUT / 'budget-release-output.json')
CAP=30
spec=importlib.util.spec_from_file_location('release_exact_helpers',(_J_PROGRAM / 'fast-optimum.py'))
lp=importlib.util.module_from_spec(spec);spec.loader.exec_module(lp)
rat,vec,dot=lp.rat,lp.vec,lp.dot

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


def rr(a):return F(*a)
def save(out):
    pending=OUTPUT.with_suffix('.json.pending')
    pending.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');pending.replace(OUTPUT)

def worker():
    start=time.monotonic()
    out={'schema': 'J79-exact-nonlinear-budget-release-v1', 'status': 'running', 'input': 'joint-budget-output.json', 'input_n': 18}
    save(out)
    try:
        src=json.loads(((_J_OUTPUT / 'joint-budget-output.json')).read_text())
        candidates=[r for r in src['records'] if r['n']==18];assert len(candidates)==1
        old=candidates[0];assert old['status']=='complete' and old['global_finite_family_optimum_certified']
        d,N,q=old['d'],old['N'],old['q'];assert (d,N)==(20,40)
        family=old['family'];assert len(family)==98
        e=[rr(c['e']) for c in family];ell=[rr(c['ell']) for c in family]
        aa=[1+2*a for a in ell]
        H=[[rr(c['h'][h]) for c in family] for h in range(N-1)]
        comp=old['compressed_indices']
        ep=[e[j]/aa[j] for j in comp]
        hp=[[row[j]/aa[j] for j in comp] for row in H]
        assert vec(ep)==old['r_prime'] and [vec(row) for row in hp]==old['H_prime']
        uc=list(map(rr,old['compressed_u']))
        I=[j for j,a in enumerate(uc) if a>0]
        corr=[dot(row,uc) for row in hp]
        Z=[h for h,a in enumerate(corr) if not a]
        assert vec(corr)==old['correlations'] and sum(uc)==2 and dot(ep,uc)==1
        rows=[[ep[j] for j in I],[F(1)]*len(I)]+[[hp[h][j] for j in I] for h in Z]
        rhs=[F(0),F(-1)]+[F(0)]*len(Z)
        assert len(rows)==len(I)
        out.update(status='system-ready',d=d,N=N,q=q,coefficients=old['coefficients'],
            family=family,compressed_indices=comp,r_prime=vec(ep),H_prime=[vec(row) for row in hp],
            old_compressed_u=vec(uc),support=I,zero_lags=[h+1 for h in Z],
            solve_matrix=[vec(row) for row in rows],solve_rhs=vec(rhs))
        save(out)
        sub,info=lp.solve_exact(rows,rhs,[0]*len(I))
        assert info['rank']==info['unknown_count']==len(I) and not info['free_indices']
        delta=[F(0)]*len(comp)
        for j,a in zip(I,sub):delta[j]=a
        dc=[dot(row,delta) for row in hp]
        assert sum(delta)==-1 and dot(ep,delta)==0 and all(dc[h]==0 for h in Z)
        y=list(map(rr,old['y']));lam,mu=rr(old['lambda_value']),rr(old['mu'])
        assert mu>0 and all(-1<=a<=1 for a in y)
        slacks=[2*sum(y[h]*hp[h][j] for h in range(N-1))-lam*ep[j]-mu for j in range(len(comp))]
        assert all(a>=0 for a in slacks) and all(slacks[j]==0 for j in I)
        assert all(not a or y[h]==(1 if a>0 else -1) for h,a in enumerate(corr))
        assert 2*dot(y,dc)==-mu
        S0=sum(uc[k]/aa[j] for k,j in enumerate(comp));assert S0==rr(old['S']) and 0<S0<2
        sigma=sum(delta[k]/aa[j] for k,j in enumerate(comp))
        M=(2-S0)**2/4;D=1+abs(sigma)*(2/S0-1)
        bounds=[{'kind':'unit','index':-1,'value':rat(F(1))},
                {'kind':'surplus','index':-1,'value':rat(M/(2*D))}]
        bounds += [{'kind':'mass','index':j,'value':rat(uc[j]/(-a))}
                   for j,a in enumerate(delta) if a<0]
        bounds += [{'kind':'sign','index':h+1,'value':rat(abs(corr[h]/dc[h]))}
                   for h in range(N-1) if corr[h]*dc[h]<0]
        assert all(rr(b['value'])>0 for b in bounds)
        tau=min(rr(b['value']) for b in bounds)
        unew=[a+tau*b for a,b in zip(uc,delta)]
        v=[F(0)]*98;dv=[F(0)]*98
        for k,j in enumerate(comp):
            if j<d:
                v[j]=v[N-1-j]=unew[k]/2
                dv[j]=dv[N-1-j]=delta[k]/2
            else:
                v[j]=unew[k]/aa[j];dv[j]=delta[k]/aa[j]
        S,LL=sum(v),dot(ell,v)
        cn=[dot(row,v) for row in H]
        K=2*sum(abs(a) for a in cn);K0=rr(old['kappa'])
        assert all(a>=0 for a in v) and dot(e,v)==1 and S>0
        assert S==S0+tau*sigma and S+2*LL==2-tau
        assert sum(dv)==sigma and all(dot(row,dv)==a for row,a in zip(H,dc))
        assert all(a==b+tau*c for a,b,c in zip(cn,corr,dc))
        assert all(not b or a*b>=0 for a,b in zip(cn,corr)) and all(cn[h]==0 for h in Z)
        assert K==K0-mu*tau<K0
        tangent_lower=M-tau*D;assert tangent_lower>=M/2>0
        margin=tangent_lower/(2*S)
        w=[a/S for a in v];den=lcm(*(a.denominator for a in w));mult=[int(a*den) for a in w]
        aggregate=[0]*(2*N-1)
        for copies,c in zip(mult,family):
            if copies:
                for i,a in enumerate(c['F_coefficients']):
                    for j,b in enumerate(c['F_coefficients']):aggregate[i+N-1-j]+=copies*a*b
        energy=F(q*q)/S;auto=[F(q*q)*a/S for a in cn]
        assert sum(mult)==den and aggregate==aggregate[::-1] and F(aggregate[N-1],den)==energy
        assert all(F(aggregate[N-1+h],den)==auto[h-1] for h in range(1,N))
        out.update(status='complete',solve_info=info,delta_compressed_u=vec(delta),
            delta_original_v=vec(dv),delta_correlations=vec(dc),old_correlations=vec(corr),
            y=vec(y),lambda_value=rat(lam),mu=rat(mu),compressed_dual_slacks=vec(slacks),
            old_S=rat(S0),sigma=rat(sigma),M=rat(M),D=rat(D),bounds=bounds,tau=rat(tau),
            limiting_bound_indices=[i for i,b in enumerate(bounds) if rr(b['value'])==tau],
            new_compressed_u=vec(unew),v=vec(v),S=rat(S),L=rat(LL),budget=rat(S+2*LL),
            correlations=vec(cn),old_kappa=rat(K0),kappa=rat(K),strict_gap=rat(mu*tau),
            tangent_lower=rat(tangent_lower),actual_surplus_margin_lower=rat(margin),
            weights=vec(w),weight_denominator=den,multiplicities=mult,
            positive_indices=[j for j,a in enumerate(w) if a],
            energy=rat(energy),aggregate_autocorrelations=vec(auto),aggregate_polynomial=aggregate,
            income={'log_q_argument':q,'norm_terms':[{'D':c['D'],'coefficient':rat(w[j]/d)} for j,c in enumerate(family)]},
            exact_arithmetic_product={'q_base':q,'q_exponent':d*den,
                'norm_factors':[{'D':c['D'],'exponent':mult[j]} for j,c in enumerate(family)]},
            degree_bound=N-1,radial_multiplier=rat(F(N-1,d)),
            strict_actual_surplus=True,strictly_below_old=True,kappa_le_4=K<=4,
            kappa_ten_thousandth_bin=[K.numerator*10000//K.denominator,K.numerator*10000//K.denominator+1])
        assert time.monotonic()-start<CAP
    except BaseException as exc:
        out.update(status='incomplete',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass;pass
    save(out);return 0 if out['status']=='complete' else 1

def main():
    if '--worker' in sys.argv:return worker()
    if OUTPUT.exists():raise SystemExit('Refusing to overwrite first native output')
    start=time.monotonic()
    p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'budget-release-author.py')),'--worker'],
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0));timeout=False
    try:code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:timeout=True;p.kill();code=p.wait()
    out=json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {'status':'incomplete'}
    out.update(actual_worker_exit_code=code, outer_timed_out=timeout)
    if timeout:out.update(status='incomplete',error_type='OuterDeadline',error='Declared aggregate30-second cap')
    save(out)
    print(json.dumps({'status':out['status'],
        'bin':out.get('kappa_ten_thousandth_bin'),'error':out.get('error')}),flush=True)
    return 0 if code==0 and not timeout and out['status']=='complete' else 1

if __name__=='__main__':sys.exit(main())
