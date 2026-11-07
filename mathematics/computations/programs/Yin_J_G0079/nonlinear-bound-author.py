"""One no-solver32-cell exact full-surplus lower bound from frozen n18 dual."""
from fractions import Fraction as F
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util, json, platform, subprocess, sys, time, traceback
import fixed_joint_budget

HERE=(_J_PROGRAM / 'nonlinear-bound-author.py').parent
OUTPUT=(_J_OUTPUT / 'nonlinear-bound-output.json')
CAP,CELLS=30,32
spec=importlib.util.spec_from_file_location('nonlinear_log_helpers',(_J_PROGRAM / 'norm-funded-author.py'))
logs=importlib.util.module_from_spec(spec)
spec.loader.exec_module(logs)
rat,vec,rr=logs.rat,logs.vec,logs.rr

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


def save(out):
    pending=OUTPUT.with_suffix('.json.pending')
    pending.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    pending.replace(OUTPUT)

def worker():
    start=time.monotonic()
    out={'schema': 'J79-full-nonlinear-cell-bound-v1', 'status': 'running', 'input': 'inputs/joint-budget-n18.json', 'input_n': 18, 'cell_count': CELLS, 'log_terms': logs.TERMS, 'log_grid': logs.GRID, 'ell_grid': logs.ELLGRID, 'cells': []}
    save(out)
    try:
        r=fixed_joint_budget.load()
        assert r['status']=='complete' and r['global_finite_family_optimum_certified']
        family=r['family']
        assert len(family)==98 and r['N']==40 and r['d']==20
        energies=[rr(c['e']) for c in family]
        lower=[rr(c['ell']) for c in family]
        upper=[F(0) if c['log_certificate'] is None else rr(c['log_certificate']['ell_upper'])
               for c in family]
        error=[b-a for a,b in zip(lower,upper)]
        assert all(a>0 for a in energies) and all(a>=0 for a in lower) and all(a>=0 for a in error)
        epsilon=max(error)
        y=list(map(rr,r['y']))
        lam,mu=rr(r['lambda_value']),rr(r['mu'])
        assert mu>=0 and all(-1<=a<=1 for a in y)
        H=[[rr(c['h'][h]) for c in family] for h in range(39)]
        slack=[2*sum(y[h]*H[h][j] for h in range(39))-lam*energies[j]-mu*(1+2*lower[j])
               for j in range(98)]
        assert all(a>=0 for a in slack) and vec(slack)==r['dual_slacks']
        A,B=1/max(energies),1/min(energies)
        width=(B-A)/CELLS
        log2=logs.series(F(1,3))
        assert F(9,260*3**65)<F(1,logs.GRID)
        out.update(d=20,N=40,q=r['q'],coefficients=r['coefficients'],family_count=98,
            family_labels=[{'kind':c['kind'],'index':c['index'],'D':c['D']} for c in family],
            e=vec(energies),ell_lower=vec(lower),ell_upper=vec(upper),ell_errors=vec(error),
            epsilon=rat(epsilon),max_error_indices=[j for j,a in enumerate(error) if a==epsilon],
            norm_log_certificates=[c['log_certificate'] for c in family],
            y=vec(y),lambda_value=rat(lam),mu=rat(mu),H_rows=[vec(row) for row in H],
            dual_slacks=vec(slack),A=rat(A),B=rat(B),width=rat(width),
            max_energy_indices=[j for j,a in enumerate(energies) if a==max(energies)],
            min_energy_indices=[j for j,a in enumerate(energies) if a==min(energies)],
            log2_certificate=log2,tail_upper=rat(F(9,260*3**65)))
        save(out)
        for i in range(CELLS):
            assert time.monotonic()-start<CAP
            a,b=A+i*width,A+(i+1)*width
            z=b/2
            numerator=logs.logcert(z.numerator,1,log2)
            denominator=logs.logcert(z.denominator,1,log2)
            beta_lower=rr(numerator['log_lower'])-rr(denominator['log_upper'])
            beta_upper=rr(numerator['log_upper'])-rr(denominator['log_lower'])
            assert beta_lower<=beta_upper
            t=beta_upper+2*epsilon
            endpoint_max=max(t*a,t*b)
            bc=max(a,a-endpoint_max)
            bound=lam+mu*bc
            out['cells'].append({'index':i,'a':rat(a),'b':rat(b),'b_over_two':rat(z),
                'numerator_log_certificate':numerator,'denominator_log_certificate':denominator,
                'beta_lower':rat(beta_lower),'beta_upper':rat(beta_upper),
                't':rat(t),'t_sign':(t>0)-(t<0),'t_times_a':rat(t*a),'t_times_b':rat(t*b),
                'endpoint_max':rat(endpoint_max),
                'max_endpoint_indices':[j for j,x in enumerate([t*a,t*b]) if x==endpoint_max],
                'mass_only_bound':rat(a),'budget_bound':rat(a-endpoint_max),
                'budget_mass_lower':rat(bc),'kappa_lower':rat(bound)})
            save(out)
        bounds=[rr(c['kappa_lower']) for c in out['cells']]
        raw=min(bounds)
        clipped=max(F(0),raw)
        upper_witness=rr(r['kappa'])
        assert clipped<=upper_witness
        out.update(status='complete',raw_lower_bound=rat(raw),full_nonlinear_lower_bound=rat(clipped),
            minimizing_cells=[i for i,a in enumerate(bounds) if a==raw],
            signs_count={str(s):sum(c['t_sign']==s for c in out['cells']) for s in [-1,0,1]},
            positive_lower_bound=clipped>0,
            lower_ten_thousandth_bin=[clipped.numerator*10000//clipped.denominator,
                                      clipped.numerator*10000//clipped.denominator+1],
            actual_feasible_upper=rat(upper_witness),strict_interval=clipped<upper_witness,
            input_budget_surplus_used='exact full nonlinear, threshold half log2',
            degree_bound=39,radial_multiplier=[39,20])
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
    p=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'nonlinear-bound-author.py')),'--worker'],
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    timeout=False
    try:
        code=p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        timeout=True;p.kill();code=p.wait()
    out=json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {'status':'incomplete','cells':[]}
    out.update(actual_worker_exit_code=code, outer_timed_out=timeout)
    if timeout:
        out.update(status='incomplete',error_type='OuterDeadline',error='Declared aggregate30-second cap')
    save(out)
    print(json.dumps({'status':out['status'],
        'cell_count':len(out['cells']),'bin':out.get('lower_ten_thousandth_bin'),
        'error':out.get('error')}),flush=True)
    return 0 if code==0 and not timeout and out['status']=='complete' else 1

if __name__=='__main__':
    sys.exit(main())
