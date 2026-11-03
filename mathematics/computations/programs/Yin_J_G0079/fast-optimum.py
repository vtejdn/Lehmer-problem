"""Fixed two-input floating discovery and one complete rational reconstruction each."""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json, platform, subprocess, sys, time, traceback

HERE = (_J_PROGRAM / 'fast-optimum.py').parent
CAP, PIVOT_CAP = 120, 10000
EPS, ACTIVE = 1e-9, 1e-7

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

def vec(xs):
    return [rat(x) for x in xs]

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))

def solve_exact(rows, rhs, approx):
    n = len(approx)
    M = [[F(x) for x in row]+[F(b)] for row, b in zip(rows, rhs)]
    pivots = []
    for j in range(n):
        at = len(pivots)
        pos = next((i for i in range(at, len(M)) if M[i][j]), None)
        if pos is None:
            continue
        M[at], M[pos] = M[pos], M[at]
        v = M[at][j]
        M[at] = [x/v for x in M[at]]
        for i in range(len(M)):
            if i != at and M[i][j]:
                a = M[i][j]
                M[i] = [x-a*y for x, y in zip(M[i], M[at])]
        pivots.append(j)
    assert all(any(row[:n]) or row[n] == 0 for row in M), 'Inconsistent active system'
    free = [j for j in range(n) if j not in pivots]
    x = [F(float(v)).limit_denominator(10**6) for v in approx]
    for i, j in enumerate(pivots):
        x[j] = M[i][n]-sum(M[i][k]*x[k] for k in free)
    assert all(dot(row, x) == b for row, b in zip(rows, rhs))
    return x, {'rank': len(pivots), 'unknown_count': n, 'free_indices': free,
               'equation_count': len(rows)}

def tableau(hp, rp, cap):
    import numpy as np
    d, L = len(rp), len(hp)
    orig, m = d+L, 2*L+2
    surplus = orig+2*L
    art = [surplus+1, surplus+2]
    width = art[-1]+1
    A = np.zeros((m, width), dtype=np.float64)
    rhs = np.zeros(m, dtype=np.float64)
    basis = []
    for h, row in enumerate(hp):
        A[2*h, :d] = row
        A[2*h+1, :d] = -np.array(row)
        A[2*h:2*h+2, d+h] = -1
        for i in (2*h, 2*h+1):
            A[i, orig+i] = 1
            basis.append(orig+i)
    A[-2, :d], A[-2, surplus], A[-2, art[0]], rhs[-2] = 1, -1, 1, 2
    A[-1, :d], A[-1, art[1]], rhs[-1] = rp, 1, 1
    basis += art
    T = np.column_stack((A, rhs))
    total, phase_counts = 0, []
    def pivot(i, j):
        nonlocal total
        cap()
        assert total < PIVOT_CAP, 'Per-input floating pivot cap'
        T[i] /= T[i, j]
        column = T[:, j].copy()
        column[i] = 0
        T[:] -= column[:, None]*T[i]
        basis[i] = j
        total += 1
    def optimize(c, allowed):
        before = total
        while True:
            cap()
            rc = c-c[basis] @ T[:, :-1]
            enter = next((j for j in allowed if j not in basis and rc[j] < -EPS), None)
            if enter is None:
                phase_counts.append(total-before)
                return rc
            eligible = [i for i in range(m) if T[i, enter] > EPS]
            assert eligible, 'Floating candidate unbounded direction'
            ratios = [(T[i, -1]/T[i, enter], basis[i], i) for i in eligible]
            lowest = min(t[0] for t in ratios)
            leave = min((b, i) for r, b, i in ratios if r <= lowest+1e-10)[1]
            pivot(leave, enter)
    c1 = np.zeros(width)
    c1[art] = 1
    optimize(c1, range(width))
    phase1 = float(c1[basis] @ T[:, -1])
    assert abs(phase1) < ACTIVE, 'Phase one not zero'
    for i in range(m):
        if basis[i] in art:
            assert abs(T[i, -1]) < ACTIVE
            j = next((j for j in range(art[0]) if j not in basis and abs(T[i, j]) > EPS), None)
            assert j is not None, 'Redundant artificial row needs unapproved repair'
            pivot(i, j)
    c2 = np.zeros(width)
    c2[d:orig] = 2
    rc = optimize(c2, range(art[0]))
    x = np.zeros(width)
    x[basis] = T[:, -1]
    pi = np.zeros(m)
    pi[:2*L] = -rc[orig:orig+2*L]
    pi[-2], pi[-1] = rc[surplus], -rc[art[1]]
    y = [(pi[2*h+1]-pi[2*h])/2 for h in range(L)]
    return {'status': 'candidate-returned', 'pivot_count': total,
            'phase_pivot_counts': phase_counts, 'phase1_objective': phase1,
            'basis': basis, 'standard_variables': x.tolist(), 'tableau_rows': T.tolist(),
            'reduced_costs': rc.tolist(), 'standard_dual': pi.tolist(),
            'pair_masses': x[:d].tolist(), 'candidate_correlations': (np.array(hp) @ x[:d]).tolist(),
            'objective': float(c2 @ x), 'y': list(map(float, y)),
            'lambda': float(pi[-1]), 'mu': float(pi[-2]),
            'reduced_cost_tolerance': EPS, 'active_selection_tolerance': ACTIVE,
            'ratio_tie_tolerance': 1e-10}

def save(output, report, start):
    pass
    pending = output.with_suffix(output.suffix+'.pending')
    pending.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    pending.replace(output)

def worker(output, start):
    report = json.loads(output.read_text(encoding='utf-8'))
    source = json.loads(((_J_OUTPUT / 'family-output.json')).read_text(encoding='utf-8'))
    def cap():
        if time.perf_counter()-start >= CAP:
            raise TimeoutError('Aggregate120-second cap')
    try:
        for n in (18, 30):
            cap()
            parent = next(x for x in source['records'] if x['n'] == n)
            selected = [x for x in parent['factors'] if x['selected']]
            assert len(selected) == 1 and selected[0]['status'] == 'actual-certified'
            f = selected[0]
            p = f['projection']
            C, q, d, N = p['C_rows'], p['q'], p['d'], p['N']
            assert N == 2*d
            r = [F(C[j][j], q) for j in range(N)]
            H = [[F(sum(C[i][j]*C[i+h][j] for i in range(N-h)), q*q)
                  for j in range(N)] for h in range(1, N)]
            assert all(r[j] == r[N-1-j] for j in range(N))
            assert all(row[j] == row[N-1-j] for row in H for j in range(N))
            uniform = F(2, d)*sum(abs(sum(row)) for row in H)
            assert rat(uniform) == p['kappa']
            contents = [gcd(*(C[i][j] for i in range(N))) for j in range(N)]
            rec = {'n': n, 'coefficients': f['coefficients'], 'd': d, 'N': N, 'q': q,
                   'input_C_rows': C, 'r': vec(r), 'H_rows': [vec(row) for row in H],
                   'column_contents': contents, 'uniform_kappa': rat(uniform), 'S0': 2,
                   'status': 'matrices-ready'}
            report['records'].append(rec)
            save(output, report, start)
            hp, rp = [row[:d] for row in H], r[:d]
            candidate = tableau([[float(x) for x in row] for row in hp], list(map(float, rp)), cap)
            rec['floating_candidate'], rec['status'] = candidate, 'candidate-returned'
            save(output, report, start)
            support = [j for j, x in enumerate(candidate['pair_masses']) if x > ACTIVE]
            zeros = [h for h, x in enumerate(candidate['candidate_correlations']) if abs(x) < ACTIVE]
            tightS = abs(sum(candidate['pair_masses'])-2) < ACTIVE
            rows, rhs = [[rp[j] for j in support]], [F(1)]
            if tightS:
                rows.append([F(1)]*len(support)); rhs.append(F(2))
            for h in zeros:
                rows.append([hp[h][j] for j in support]); rhs.append(F(0))
            bsub, info = solve_exact(rows, rhs, [candidate['pair_masses'][j] for j in support])
            b = [F(0)]*d
            for j, val in zip(support, bsub):
                b[j] = val
            v = [b[min(j, N-1-j)]/2 for j in range(N)]
            S = sum(v)
            correlations = [dot(row, v) for row in H]
            assert all(x >= 0 for x in v) and dot(r, v) == 1 and S >= 2
            kappa = 2*sum(abs(x) for x in correlations)
            rec.update({'status': 'primal-certified', 'primal_reconstruction': info,
                        'selected_support': support, 'selected_zero_lags': [h+1 for h in zeros],
                        'selected_S_tight': tightS, 'pair_masses': vec(b), 'v': vec(v),
                        'S': rat(S), 'correlations': vec(correlations), 'kappa': rat(kappa)})
            save(output, report, start)
            free_y, y = [], [None]*len(H)
            for h, a in enumerate(correlations):
                if a:
                    y[h] = F(1 if a > 0 else -1)
                elif abs(abs(candidate['y'][h])-1) < ACTIVE:
                    y[h] = F(1 if candidate['y'][h] > 0 else -1)
                else:
                    free_y.append(h)
            unknown = len(free_y)+2
            rows, rhs = [], []
            for j, val in enumerate(b):
                if val:
                    rows.append([2*hp[h][j] for h in free_y]+[-rp[j], F(-1)])
                    rhs.append(-sum(2*hp[h][j]*y[h] for h in range(len(H)) if y[h] is not None))
            if S > 2 or abs(candidate['mu']) < ACTIVE:
                rows.append([F(0)]*(unknown-1)+[F(1)]); rhs.append(F(0))
            approx = [candidate['y'][h] for h in free_y]+[candidate['lambda'], candidate['mu']]
            solution, dinfo = solve_exact(rows, rhs, approx)
            for h, val in zip(free_y, solution):
                y[h] = val
            lam, mu = solution[-2:]
            slacks = [2*sum(H[h][j]*y[h] for h in range(len(H)))-lam*r[j]-mu for j in range(N)]
            lower = lam+2*mu
            rec.update({'dual_reconstruction': dinfo, 'dual_free_y_lags': [h+1 for h in free_y],
                        'y': vec(y), 'lambda': rat(lam), 'mu': rat(mu),
                        'dual_slacks': vec(slacks), 'lower_bound': rat(lower), 'gap': rat(kappa-lower)})
            save(output, report, start)
            assert all(-1 <= x <= 1 for x in y) and mu >= 0 and all(x >= 0 for x in slacks)
            assert kappa == lower, 'Exact primal/dual objective mismatch'
            w = [x/S for x in v]
            denom = lcm(*(x.denominator for x in w))
            multiplicities = [int(x*denom) for x in w]
            energy, aggregate = F(q*q)/S, [F(q*q)*x/S for x in correlations]
            Q = [0]*(2*N-1)
            for j, copies in enumerate(multiplicities):
                for a in range(N):
                    for c in range(N):
                        Q[a+N-1-c] += copies*C[a][j]*C[c][j]
            assert F(Q[N-1], denom) == energy
            assert all(F(Q[N-1+h], denom) == aggregate[h-1] for h in range(1, N))
            assert sum(multiplicities) == denom
            rec.update({'status': 'complete', 'global_optimum_certified': True,
                        'weights': vec(w), 'weight_denominator': denom, 'multiplicities': multiplicities,
                        'positive_columns': [j for j, x in enumerate(w) if x],
                        'zero_correlation_lags': [h+1 for h, x in enumerate(correlations) if not x],
                        'strict_dual_slack_columns': [j for j, x in enumerate(slacks) if x > 0],
                        'energy': rat(energy), 'aggregate_autocorrelations': vec(aggregate),
                        'aggregate_polynomial': Q, 'each_full_resultant_abs': q**d,
                        'income_log_argument': q, 'surplus_half_log_argument': rat(S),
                        'degree_bound': N-1, 'radial_multiplier': rat(F(N-1, d)),
                        'kappa_le_4': kappa <= 4, 'improves_uniform': kappa < uniform,
                        'kappa_thousandth_bin': [kappa.numerator*1000//kappa.denominator,
                                                   kappa.numerator*1000//kappa.denominator+1]})
            cap()
            save(output, report, start)
            print(json.dumps({'n': n, 'kappa': rat(kappa), 'S': rat(S),
                              'support': rec['positive_columns'], 'pivots': candidate['pivot_count']}), flush=True)
        report['status'], report['all_global_optima_certified'] = 'complete', True
        save(output, report, start)
        return 0
    except Exception as error:
        report.update({'status': 'incomplete', 'error_type': type(error).__name__, 'error': _record_text(str(error)),
                       'traceback': _record_text(traceback.format_exc())})
        save(output, report, start)
        return 1

def main():
    if len(sys.argv) == 4 and sys.argv[1] == '--worker':
        return worker(Path(sys.argv[2]), float(sys.argv[3]))
    if len(sys.argv) not in (1, 3) or (len(sys.argv) == 3 and sys.argv[1] != '--output'):
        raise SystemExit('Usage: fast-optimum.py [--output path-in-J79]')
    output = Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else (_J_OUTPUT / 'fast-optimum-result.json')
    assert output.parent == _J_OUTPUT
    start = time.perf_counter()
    report = {'schema': 'J79-fast-exact-optimum-v1', 'status': 'started', 'domain_n': [18, 30], 'S0': 2, 'pivot_cap_per_input': PIVOT_CAP, 'input': 'family-output.json', 'records': []}
    with output.open('x', encoding='utf-8') as handle:
        json.dump(report, handle, indent=2)
    proc = subprocess.Popen([sys.executable, '-X', 'utf8', str((_J_PROGRAM / 'fast-optimum.py')),
                             '--worker', str(output), repr(start)],
                            creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    timeout = False
    try:
        code = proc.wait(timeout=max(0.01, CAP-(time.perf_counter()-start)))
    except subprocess.TimeoutExpired:
        timeout = True
        proc.kill()
        code = proc.wait()
    result = json.loads(output.read_text(encoding='utf-8'))
    result.update({'worker_returncode': code, 'outer_deadline_triggered': timeout})
    if timeout:
        result.update({'status': 'incomplete', 'error_type': 'OuterDeadline',
                       'error': 'Worker terminated at declared aggregate120-second cap'})
    save(output, result, start)
    print(json.dumps({k: result[k] for k in ['status', 'worker_returncode', 'outer_deadline_triggered']}), flush=True)
    return 1 if timeout else code

if __name__ == '__main__':
    raise SystemExit(main())
