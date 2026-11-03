"""One declared 600-direction exact residual-bundle escape test; no optimization loop."""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json, platform, subprocess, sys, time, traceback

HERE = (_J_PROGRAM / 'nonmonomial-author.py').parent
OUTPUT = (_J_OUTPUT / 'nonmonomial-output.json')
CAP = 120

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


def rat(a):
    a = F(a)
    return [a.numerator, a.denominator]

def vec(a):
    return [rat(x) for x in a]

def readrat(a):
    return F(*a)

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def invert(a):
    n = len(a)
    b = [[F(x) for x in row]+[F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for j in range(n):
        k = next(k for k in range(j, n) if b[k][j])
        b[j], b[k] = b[k], b[j]
        z = b[j][j]
        b[j] = [x/z for x in b[j]]
        for k in range(n):
            if k != j:
                z = b[k][j]
                b[k] = [x-z*y for x, y in zip(b[k], b[j])]
    assert all(b[i][j] == (i == j) for i in range(n) for j in range(n))
    return [row[n:] for row in b]

def quotient(a, p):
    a = list(a)
    d = len(p)-1
    q = [0]*(len(a)-d)
    for i in range(len(a)-1, d-1, -1):
        q[i-d] = a[i]
        for k, c in enumerate(p):
            a[i-d+k] -= q[i-d]*c
    assert all(x == 0 for x in a)
    return q

def save(out):
    OUTPUT.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')

def worker():
    from sympy import Poly, Symbol, resultant
    start = time.monotonic()
    out = {'schema': 'J79-nonmonomial-escape-v1', 'status': 'running', 'domain': {'n': [18, 30], 'h': [1, 2, 3], 's': [-1, 1], 'j': 'every integer 0<=j<N-h', 'counts': [228, 372]}, 'input': 'fast-optimum-result.json', 'records': []}
    save(out)
    try:
        source = json.loads(((_J_OUTPUT / 'fast-optimum-result.json')).read_text(encoding='utf-8'))
        records = {r['n']: r for r in source['records']}
        t = Symbol('t')
        for n in [18, 30]:
            old = records[n]
            p, d, N, q = old['coefficients'], old['d'], old['N'], old['q']
            C = old['input_C_rows']
            r = list(map(readrat, old['r']))
            H = [list(map(readrat, row)) for row in old['H_rows']]
            pair = list(map(readrat, old['pair_masses']))
            I = [j for j, a in enumerate(pair) if a]
            a0 = list(map(readrat, old['correlations']))
            Z = [h for h, a in enumerate(a0) if not a]
            y = list(map(readrat, old['y']))
            lam, mu, K0 = map(readrat, [old['lambda'], old['mu'], old['kappa']])
            M = [[F(1) for j in I], [r[j] for j in I]]+[[H[h][j] for j in I] for h in Z]
            assert len(M) == len(I)
            inv = invert(M)
            assert dot(r[:d], pair) == 1 and sum(pair) == 2
            assert all(sum(C[i][k]*C[k][j] for k in range(N)) == q*C[i][j]
                       for i in range(N) for j in range(N))
            assert all(C[i][j] == C[j][i] for i in range(N) for j in range(N))
            assert sum(C[i][i] for i in range(N)) == q*d
            for j in I:
                assert 2*dot(y, [H[h][j] for h in range(N-1)]) == lam*r[j]+mu
            assert all(abs(a) <= 1 for a in y)
            assert all(y[h] == (1 if a0[h] > 0 else -1) for h in range(N-1) if a0[h])
            assert K0 == 2*sum(abs(a) for a in a0) == lam+2*mu
            base_poly = Poly(sum(c*t**i for i, c in enumerate(p)), t)
            bin_norm = {(h, s): int(resultant(base_poly.as_expr(), 1+s*t**h, t))
                        for h in [1, 2, 3] for s in [-1, 1]}
            norm_t = (-1)**d*p[0]
            rec = {'n': n, 'coefficients': p, 'd': d, 'N': N, 'q': q,
                   'C_rows': C, 'r': vec(r), 'H_rows': [vec(row) for row in H],
                   'old_pair_masses': vec(pair), 'old_support': I,
                   'old_zero_lags': [h+1 for h in Z], 'old_correlations': vec(a0),
                   'old_kappa': rat(K0), 'old_y': vec(y),
                   'old_lambda': rat(lam), 'old_mu': rat(mu),
                   'active_matrix': [vec(row) for row in M],
                   'active_inverse': [vec(row) for row in inv],
                   'old_contents': old['column_contents'],
                   'degree_bound': N-1, 'radial_multiplier': rat(F(N-1, d)),
                   'binomial_resultants': [{'h': h, 's': s, 'signed': bin_norm[h, s]}
                                           for h in [1, 2, 3] for s in [-1, 1]],
                   'candidates': [], 'status': 'running'}
            out['records'].append(rec)
            for h in [1, 2, 3]:
                for s in [-1, 1]:
                    for j in range(N-h):
                        assert time.monotonic()-start < CAP, 'Worker elapsed cap'
                        b = [0]*N
                        b[j], b[j+h] = 1, s
                        coeff = [row[j]+s*row[j+h] for row in C]
                        U = quotient([q*b[i]-coeff[i] for i in range(N)], p)
                        content = gcd(*coeff)
                        energy_int = sum(a*a for a in coeff)
                        E = F(energy_int, q*q)
                        autocorr_int = [sum(coeff[i]*coeff[i+l] for i in range(N-l))
                                        for l in range(1, N)]
                        HB = [F(a, q*q) for a in autocorr_int]
                        assert E == F(C[j][j]+C[j+h][j+h]+2*s*C[j][j+h], q)
                        NB = norm_t**j*bin_norm[h, s]
                        assert NB != 0 and content > 0 and E > 0
                        NF = q**d*NB
                        assert NF % content**d == 0
                        z = [F(1), E]+[HB[l] for l in Z]
                        x = [dot(row, z) for row in inv]
                        assert all(dot(row, x) == val for row, val in zip(M, z))
                        da = [HB[l]-sum(x[k]*H[l][col] for k, col in enumerate(I))
                              for l in range(N-1)]
                        assert all(da[l] == 0 for l in Z)
                        g = 2*dot(y, HB)-lam*E-mu
                        assert g == 2*dot(y, da)
                        bounds = [('unit', -1, F(1))]
                        bounds += [('mass', col, pair[col]/x[k])
                                   for k, col in enumerate(I) if x[k] > 0]
                        bounds += [('sign', l+1, abs(a0[l]/da[l]))
                                   for l in range(N-1) if a0[l]*da[l] < 0]
                        tau = min(v for _, _, v in bounds)
                        bp = pair.copy()
                        for k, col in enumerate(I):
                            bp[col] -= tau*x[k]
                        vm = [F(0)]*N
                        for col, value in enumerate(bp):
                            vm[col] = vm[N-1-col] = value/2
                        v = vm+[tau]
                        assert all(a >= 0 for a in v) and sum(v) == 2
                        assert dot(r, vm)+tau*E == 1
                        aa = [a0[l]+tau*da[l] for l in range(N-1)]
                        assert all(not a0[l] or aa[l]*a0[l] >= 0 for l in range(N-1))
                        kk = 2*sum(abs(a) for a in aa)
                        assert kk == K0+tau*g
                        w = [a/2 for a in v]
                        L = lcm(*(a.denominator for a in w))
                        mult = [int(L*a) for a in w]
                        assert sum(mult) == L
                        native = {'h': h, 's': s, 'j': j, 'B': b,
                                  'F_coefficients': coeff, 'kernel_multiplier': U,
                                  'content': content, 'primitive_coefficients': [a//content for a in coeff],
                                  'actual_degree': max(i for i, a in enumerate(coeff) if a),
                                  'signed_res_B': NB, 'signed_res_F': NF,
                                  'signed_res_primitive': NF//content**d,
                                  'integer_energy': energy_int, 'e_B': rat(E),
                                  'integer_autocorrelations': autocorr_int, 'h_B': vec(HB),
                                  'active_rhs': vec(z), 'old_mass_derivative': vec(x),
                                  'correlation_derivative': vec(da), 'reduced_cost': rat(g),
                                  'step_bounds': [{'kind': kind, 'index': idx, 'value': rat(val)}
                                                  for kind, idx, val in bounds],
                                  'tau': rat(tau),
                                  'limiting_bounds': [i for i, (_, _, val) in enumerate(bounds) if val == tau],
                                  'pair_masses_after': vec(bp), 'masses': vec(v),
                                  'weights': vec(w), 'weight_denominator': L, 'multiplicities': mult,
                                  'positive_weight_indices': [i for i, a in enumerate(w) if a],
                                  'correlations_after': vec(aa), 'kappa_after': rat(kk),
                                  'strict_improvement': kk < K0, 'kappa_le_4': kk <= 4,
                                  'energy_after': rat(F(q*q, 2)),
                                  'aggregate_autocorrelations_after': vec([F(q*q, 2)*a for a in aa]),
                                  'income': {'log_q_argument': q, 'log_abs_res_B_argument': abs(NB),
                                             'log_abs_res_B_coefficient': rat(tau/(2*d))},
                                  'surplus': {'half_log_argument': 2,
                                              'extra_log_argument': abs(NB),
                                              'extra_log_coefficient': rat(tau/(2*d))}}
                        rec['candidates'].append(native)
                    save(out)
            assert len(rec['candidates']) == 2*sum(N-h for h in [1, 2, 3])
            best = min(range(len(rec['candidates'])),
                       key=lambda i: readrat(rec['candidates'][i]['kappa_after']))
            rec['best_candidate_index'] = best
            rec['negative_reduced_cost_count'] = sum(readrat(c['reduced_cost']) < 0 for c in rec['candidates'])
            rec['strict_improvement_count'] = sum(c['strict_improvement'] for c in rec['candidates'])
            rec['kappa_le_4_count'] = sum(c['kappa_le_4'] for c in rec['candidates'])
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
    p = subprocess.Popen([sys.executable, str((_J_PROGRAM / 'nonmonomial-author.py')), '--worker'])
    timed_out = False
    try:
        code = p.wait(timeout=CAP)
    except subprocess.TimeoutExpired:
        timed_out = True
        p.kill()
        code = p.wait()
    out = json.loads(OUTPUT.read_text(encoding='utf-8')) if OUTPUT.exists() else {'records': []}
    if timed_out:
        out['status'] = 'timeout'
    pass
    out['actual_worker_exit_code'] = code
    out['outer_timed_out'] = timed_out
    save(out)
    print(json.dumps({'status': out['status'], 
                      'records': [{'n': r['n'], 'status': r['status'],
                                   'candidate_count': len(r['candidates'])} for r in out['records']]}))
    return 0 if out.get('status') == 'complete' and code == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
