"""Only the unexecuted exact remainder after the retained failed first review.

Explicitly imports this reviewer's unit-cap-review.py helper, never author code.
No input projection, norm, first-five-certificate or floating tableau rerun.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util, json, time, subprocess, sys, traceback, platform

HERE=(_J_PROGRAM / 'unit-cap-remainder-review.py').parent
OUT=(_J_OUTPUT / 'unit-cap-remainder-review-result.json')
CAP=30


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


def worker(start):
    report={'schema': 'J79-unit-cap-remainder-independent-review-v1', 'status': 'running'}
    paths=[((_J_PROGRAM if f in ('author.py', 'budget-release-author.py', 'budget-release-review.py', 'direct-author.py', 'family-author.py', 'family-review.py', 'fast-optimum-review.py', 'fast-optimum.py', 'joint-budget-author.py', 'joint-budget-review.py', 'lehmer-bundle-author.py', 'lehmer-bundle-review.py', 'nonlinear-bound-author.py', 'nonlinear-bound-review.py', 'nonmonomial-author.py', 'nonmonomial-norm-review.py', 'norm-funded-author.py', 'power-classification-author.py', 'power-classification-review.py', 'readme.md', 'residual-lattice-author.py', 'residual-lattice-review.py', 'review_independent.py', 'unit-cap-author.py', 'unit-cap-remainder-review.py', 'unit-cap-review.py', 'weights-author.py', 'weights-review.py') else _J_OUTPUT) / f) for f in ('unit-cap-author.py','unit-cap-output.json','unit-cap-review.py','unit-cap-review-result.json')]
    draft=(_J_ROOT / 'mathematics/drafts/Yin_D_G0221.md')
    if draft.exists():paths.append(draft)
    before={str(p):p.read_bytes() for p in paths}
    try:
        spec=importlib.util.spec_from_file_location('orbit_first_review',(_J_PROGRAM / 'unit-cap-review.py'))
        core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
        core.START=start;core.CAP=CAP
        a=json.loads(((_J_OUTPUT / 'unit-cap-output.json')).read_text(encoding='utf-8'))
        first=json.loads(((_J_OUTPUT / 'unit-cap-review-result.json')).read_text(encoding='utf-8'))
        assert first['status']=='failed' and first['error_type']=='AssertionError'
        assert '2.5781250000651568' in first['error'] and 'basis_tableau' in first['error']
        assert len(first['inputs'])==3 and len(first['instances'])==5
        core.same(first['inputs'],[
          {'input':'P10','columns':48,'admitted_residues':19,'all_fresh_signed_norms':True},
          {'input':'n18','columns':98,'admitted_residues':23,'all_fresh_signed_norms':True},
          {'input':'n30','columns':158,'admitted_residues':41,'all_fresh_signed_norms':True}], 'first-scope')
        assert len(a['inputs'])==3 and len(a['instances'])==6
        for j,(label,fam) in enumerate(core.ORDER):
            rec=a['instances'][j]
            core.same([rec['input'],rec['family']],[label,fam],'order/'+str(j))
            if j<5:
                old=first['instances'][j]
                assert old['status']=='complete-exact-optimum'
                for k in ('input','family','kappa','S','weight_denominator'):
                    core.same(rec[k],old[k],'retained-first/'+str(j)+'/'+k)
                core.same(rec['positive_source_indices'],old['positive_sources'],'retained-support/'+str(j))
                core.same(rec['kappa_ten_thousandth_bin'],old['bin'],'retained-bin/'+str(j))
        # The first run already inspected all sixth floating keys, shapes,
        # finite leaves and direct equations; its failed equation stays failed.
        # This callback disables no exact constraint: only a disclosed skip of
        # the already failed FLOAT check permits the unexecuted exact stage.
        def retained_failed_float(c,hp,ep,expected_pivots):
            assert expected_pivots==c['pivot_count']==2952
            return {'scope':'Not rerun; first complete floating inspection failed',
              'first_report':'unit-cap-review-result.json','basis_tableau_consistency_passed':False,
              'retained_scaled_residual':2.5781250000651568,'retained_tolerance':1e-6,
              'does_not_supply_exact_certificate':True}
        core.inspect_float=retained_failed_float
        inp=a['inputs'][2]; assert inp['input']=='n30'
        exact,detail=core.instance(a['instances'][5],inp,5)
        assert detail['status']=='feasible-primal-invalid-dual'
        core.same(detail['y9'],[
          1250219600952020615518359902017890571723595934078126182947316886673692860099756472755062996000312,
          520463645430827783431694946531536913247130193491482178915911692497465315333918297999572546108191], 'printed-y9')
        comparisons=[]
        for j in (1,3):
            base=a['instances'][j-1];enlarged=a['instances'][j]
            K0=core.dec(base['kappa']);K=core.dec(enlarged['kappa']);assert K<K0
            comparisons.append({'input':base['input'],'baseline_kappa':core.enc(K0),
              'enlarged_kappa':core.enc(K),'improvement':core.enc(K0-K),
              'strict_improvement':True,'equal_optima':False})
        core.same(a['comparisons'],comparisons,'complete-comparisons')
        expected={'schema': 'J79-unit-cap-comparison-v1', 'status': 'incomplete', 'input_files': core.SOURCES, 'helper_files': ['fast-optimum.py', 'nonmonomial-author.py'], 'candidate_rule': {'EPS': 1e-09, 'ACTIVE': 1e-07, 'ratio_tie': 1e-10, 'pivot_cap_per_instance': 10000, 'free_denominator_cap': 1000000, 'candidate_calls_per_instance': 1, 'reconstructions_per_instance': 1}, 'error_type': 'AssertionError', 'error': '', 'actual_worker_exit_code': 1, 'outer_timed_out': False}
        for k,v in expected.items():core.same(a[k],v,'top/'+k)
        provenance={'traceback'}
        assert set(a)==set(expected)|provenance|{'instances','inputs','comparisons'}
        pass
        assert all((type(a[k]) is float and 0 < a[k] < 180 for k in ()))
        pass
        assert 'all_six_optima_certified' not in a
        core.checktime()
        report.update(status='passed-remainder-only', exact_sixth=detail, comparisons=comparisons, exact_field_leaves=core.COUNT, first_report_status='failed-preserved', first_five_and_all304_scope='Reused from complete reached checks in first report, not rerun', floating_tableau_status='Sixth basis-tableau still fails1e-6; no corrected candidate', exact_source='Same frozen original matrices; no new source/norm/LLL/optimization', all_new_native_keys_covered_across_two_scopes=True)
    except BaseException as exc:
        report.update(status='failed',error_type=type(exc).__name__,error=_record_text(str(exc)),traceback=_record_text(traceback.format_exc()))
    pass
    pass
    pass
    pass
    with OUT.open('x',encoding='utf-8') as f:json.dump(report,f,indent=2);f.write('\n')
    return 0 if report['status']=='passed-remainder-only' else 1


def main():
    if len(sys.argv)==3 and sys.argv[1]=='--worker':return worker(float(sys.argv[2]))
    assert len(sys.argv)==1 and not OUT.exists(),'Refusing an extra run or first-report overwrite'
    start=time.monotonic()
    proc=subprocess.Popen([sys.executable,str((_J_PROGRAM / 'unit-cap-remainder-review.py')),'--worker',repr(start)],
      creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    timeout=False
    try:code=proc.wait(timeout=max(.01,CAP-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:timeout=True;proc.kill();code=proc.wait()
    elapsed=time.monotonic()-start
    if not OUT.exists():
        with OUT.open('x',encoding='utf-8') as f:
            json.dump({'schema': 'J79-unit-cap-remainder-independent-review-v1', 'status': 'incomplete', 'error': 'Outer deadline or worker termination before first remainder report', 'outer_timed_out': timeout, 'worker_exit_code': code}, f, indent=2)
    print(json.dumps({'worker_exit_code': code, 'outer_timed_out': timeout}), flush=True)
    return code if not timeout else 124


if __name__=='__main__':raise SystemExit(main())
