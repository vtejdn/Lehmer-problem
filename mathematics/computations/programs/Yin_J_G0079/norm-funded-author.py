"""Same 600 frozen directions, one norm-funded exact step, certified rational logs."""
from fractions import Fraction as F
from math import lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json, platform, subprocess, sys, time, traceback

HERE = (_J_PROGRAM / 'norm-funded-author.py').parent
OUTPUT = (_J_OUTPUT / 'norm-funded-output.json')
CAP, GRID, ELLGRID, TERMS = 120, 2**32, 2**20, 32

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


def rat(x):
    x = F(x)
    return [x.numerator, x.denominator]

def vec(x):
    return [rat(a) for a in x]

def rr(x):
    return F(*x)

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def ceil(x):
    return -((-x.numerator)//x.denominator)

def series(x):
    terms = [2*x**(2*j+1)/F(2*j+1) for j in range(TERMS)]
    lo = [(GRID*a).numerator//(GRID*a).denominator for a in terms]
    hi = [ceil(GRID*a) for a in terms]
    return {'x': rat(x), 'lower_term_numerators': lo, 'upper_term_numerators': hi,
            'lower_numerator': sum(lo), 'upper_numerator': sum(hi)+1,
            'denominator': GRID, 'tail_upper_grid_units': 1}

def logcert(D, d, log2):
    assert isinstance(D, int) and D >= 1
    if D == 1:
        return {'D': 1, 'd': d, 'exact_zero': True, 'ell_lower': [0, 1],
                'ell_upper': [0, 1], 'log_lower': [0, 1], 'log_upper': [0, 1]}
    k = D.bit_length()-1
    t = F(D, 2**k)
    x = (t-1)/(t+1)
    c = series(x)
    lower = F(k*log2['lower_numerator']+c['lower_numerator'], GRID)
    upper = F(k*log2['upper_numerator']+c['upper_numerator'], GRID)
    a = lower*ELLGRID/d
    b = upper*ELLGRID/d
    return {'D': D, 'd': d, 'exact_zero': False, 'binary_exponent': k,
            'range_reduced': rat(t), 'series': c,
            'log_lower': rat(lower), 'log_upper': rat(upper),
            'ell_lower': rat(F(a.numerator//a.denominator, ELLGRID)),
            'ell_upper': rat(F(ceil(b), ELLGRID))}

def save(out):
    OUTPUT.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')

def worker():
    start = time.monotonic()
    out = {'schema': 'J79-norm-funded-residue-v1', 'status': 'running', 'input': 'nonmonomial-output.json', 'domain_n': [18, 30], 'counts': [228, 372], 'series_terms': TERMS, 'log_grid_denominator': GRID, 'ell_grid_denominator': ELLGRID, 'log2_certificate': series(F(1, 3)), 'tail_bound': {'numerator': 9, 'denominator': 260 * 3 ** 65}, 'records': []}
    assert F(9, 260*3**65) < F(1, GRID)
    save(out)
    try:
        src = json.loads(((_J_OUTPUT / 'nonmonomial-output.json')).read_text(encoding='utf-8'))
        assert src['status'] == 'complete' and len(src['records']) == 2
        for old in src['records']:
            n, d, N, q = old['n'], old['d'], old['N'], old['q']
            H = [list(map(rr, row)) for row in old['H_rows']]
            r = list(map(rr, old['r']))
            pair = list(map(rr, old['old_pair_masses']))
            I = old['old_support']
            Z = [h-1 for h in old['old_zero_lags']]
            a0 = list(map(rr, old['old_correlations']))
            inv = [list(map(rr, row)) for row in old['active_inverse']]
            M = [list(map(rr, row)) for row in old['active_matrix']]
            y = list(map(rr, old['old_y']))
            lam, mu, K0 = map(rr, [old['old_lambda'], old['old_mu'], old['old_kappa']])
            assert mu > 0
            Ds = sorted({abs(c['signed_res_B']) for c in old['candidates']})
            certs = [logcert(D, d, out['log2_certificate']) for D in Ds]
            lookup = {c['D']: c for c in certs}
            rec = {'n': n, 'd': d, 'N': N, 'q': q, 'coefficients': old['coefficients'],
                   'first_stage_record_n': n, 'original_kappa': rat(K0),
                   'original_support': I, 'original_zero_lags': old['old_zero_lags'],
                   'original_lambda': rat(lam), 'original_mu': rat(mu),
                   'log_certificates': certs, 'degree_bound': N-1,
                   'radial_multiplier': rat(F(N-1, d)), 'candidates': [], 'status': 'running'}
            out['records'].append(rec)
            for index, seed in enumerate(old['candidates']):
                assert time.monotonic()-start < CAP, 'Worker elapsed cap'
                D = abs(seed['signed_res_B'])
                cert = lookup[D]
                ell, upper = rr(cert['ell_lower']), rr(cert['ell_upper'])
                assert 0 <= ell <= upper
                E, HB, g = rr(seed['e_B']), list(map(rr, seed['h_B'])), rr(seed['reduced_cost'])
                z = [1+2*ell, E]+[HB[h] for h in Z]
                x = [dot(row, z) for row in inv]
                assert all(dot(row, x) == v for row, v in zip(M, z))
                da = [HB[h]-sum(x[k]*H[h][j] for k, j in enumerate(I)) for h in range(N-1)]
                assert all(da[h] == 0 for h in Z)
                lower_slope, upper_slope = g-2*mu*upper, g-2*mu*ell
                assert upper_slope == 2*dot(y, da)
                bounds = [('unit', -1, F(1))]
                if ell:
                    bounds.append(('mass_total', -1, 1/(2*ell)))
                bounds += [('mass', j, pair[j]/x[k]) for k, j in enumerate(I) if x[k] > 0]
                bounds += [('sign', h+1, abs(a0[h]/da[h]))
                           for h in range(N-1) if a0[h]*da[h] < 0]
                tau = min(b for _, _, b in bounds)
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
                assert K == K0+tau*upper_slope
                w = [a/S for a in v]
                L = lcm(*(a.denominator for a in w))
                mult = [int(a*L) for a in w]
                assert sum(mult) == L and all(a >= 0 for a in mult)
                decision = ('negative' if upper_slope < 0 else 'nonnegative' if lower_slope >= 0
                            else 'undecided')
                native = {'first_stage_candidate_index': index,
                          'h': seed['h'], 's': seed['s'], 'j': seed['j'],
                          'B': seed['B'], 'F_coefficients': seed['F_coefficients'],
                          'content': seed['content'], 'signed_res_B': seed['signed_res_B'],
                          'signed_res_F': seed['signed_res_F'],
                          'signed_res_primitive': seed['signed_res_primitive'],
                          'e_B': seed['e_B'], 'h_B': seed['h_B'],
                          'ell_lower': rat(ell), 'ell_upper': rat(upper),
                          'active_rhs': vec(z), 'old_mass_derivative': vec(x),
                          'correlation_derivative': vec(da), 'old_reduced_cost': rat(g),
                          'chosen_slope': rat(upper_slope),
                          'exact_log_slope_interval': [rat(lower_slope), rat(upper_slope)],
                          'exact_log_slope_decision': decision,
                          'step_bounds': [{'kind': kind, 'index': idx, 'value': rat(val)}
                                          for kind, idx, val in bounds],
                          'tau': rat(tau), 'limiting_bounds': [i for i, (_, _, b) in enumerate(bounds) if b == tau],
                          'pair_masses_after': vec(bp), 'masses': vec(v), 'S': rat(S),
                          'weights': vec(w), 'weight_denominator': L, 'multiplicities': mult,
                          'positive_weight_indices': [i for i, a in enumerate(w) if a],
                          'correlations_after': vec(aa), 'kappa_after': rat(K),
                          'strict_improvement': K < K0, 'kappa_le_4': K <= 4,
                          'energy_after': rat(F(q*q)/S),
                          'aggregate_autocorrelations_after': vec([F(q*q)*a/S for a in aa]),
                          'income': {'log_q_argument': q, 'log_abs_res_B_argument': D,
                                     'log_abs_res_B_coefficient': rat(tau/(d*S))},
                          'surplus': {'half_log_argument': rat(S), 'extra_log_argument': D,
                                      'extra_log_coefficient': rat(tau/(d*S)),
                                      'x_in_finite_interval_proof': rat(ell*tau),
                                      'at_least_half_log_two': True}}
                rec['candidates'].append(native)
                if (index+1) % 64 == 0:
                    save(out)
            assert len(rec['candidates']) == (228 if n == 18 else 372)
            rec['best_candidate_index'] = min(range(len(rec['candidates'])),
                                              key=lambda i: rr(rec['candidates'][i]['kappa_after']))
            rec['strict_improvement_count'] = sum(c['strict_improvement'] for c in rec['candidates'])
            rec['kappa_le_4_count'] = sum(c['kappa_le_4'] for c in rec['candidates'])
            rec['exact_log_slope_counts'] = {s: sum(c['exact_log_slope_decision'] == s for c in rec['candidates'])
                                             for s in ['negative', 'nonnegative', 'undecided']}
            rec['status'] = 'complete'
            save(out)
        out['status'] = 'complete'
    except BaseException as e:
        out['status'] = 'failed'
        out['error'] = _record_text(repr(e))
        out['traceback'] = _record_text(traceback.format_exc())
    pass
    pass
    save(out)
    return 0 if out['status'] == 'complete' else 1

def main():
    if '--worker' in sys.argv:
        return worker()
    if OUTPUT.exists():
        raise SystemExit('Refusing to overwrite first native output')
    start = time.monotonic()
    p = subprocess.Popen([sys.executable, str((_J_PROGRAM / 'norm-funded-author.py')), '--worker'])
    timeout = False
    try:
        code = p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        timeout = True
        p.kill()
        code = p.wait()
    out = json.loads(OUTPUT.read_text(encoding='utf-8')) if OUTPUT.exists() else {'records': []}
    if timeout:
        out['status'] = 'timeout'
    pass
    out['actual_worker_exit_code'] = code
    out['outer_timed_out'] = timeout
    save(out)
    print(json.dumps({'status': out['status'], 
                      'records': [{'n': r['n'], 'status': r['status'],
                                   'candidates': len(r['candidates']),
                                   'improvements': r.get('strict_improvement_count'),
                                   'exact_log_decisions': r.get('exact_log_slope_counts')}
                                  for r in out['records']]}))
    return 0 if out.get('status') == 'complete' and code == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
