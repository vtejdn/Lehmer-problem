"""Two predeclared exact adaptive-weight problems with an outer 180s cap.

The old family payload is read-only input. A sole worker is killed at the
aggregate deadline, including during simplex. The first report is preserved.
"""
from math import lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import os
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'weights-author.py').parent
OUTPUT = (_J_OUTPUT / 'weights-output.json')
CHECKPOINT = _J_OUTPUT / 'weights-output.json.pending'
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


def save(report, start):
    pass
    CHECKPOINT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    CHECKPOINT.replace(OUTPUT)


def worker(start):
    import sympy as sp
    from sympy.solvers.simplex import linprog

    def rat(x):
        x = sp.Rational(x)
        return [int(x.p), int(x.q)]

    def rows(matrix):
        return [[rat(x) for x in row] for row in matrix.tolist()]

    def cap():
        if time.perf_counter() - start >= CAP:
            raise TimeoutError('Aggregate 180-second adaptive author cap')

    report = json.loads(OUTPUT.read_text(encoding='utf-8'))
    original = json.loads(((_J_OUTPUT / 'family-output.json')).read_text(encoding='utf-8'))
    try:
        for n in (18, 30):
            cap()
            source = next(r for r in original['records'] if r['n'] == n)
            selected = [f for f in source['factors'] if f['selected']]
            assert len(selected) == 1
            source_factor = selected[0]
            assert source_factor['status'] == 'actual-certified'
            base = source_factor['projection']
            d, N, q = base['d'], base['N'], base['q']
            assert N == 2 * d
            C = sp.Matrix(base['C_rows'])
            assert C.shape == (N, N) and C.T == C and C * C == q * C
            assert sp.trace(C) == q * d
            r = sp.Matrix([sp.Rational(C[j, j], q) for j in range(N)])
            assert all(x > 0 for x in r)
            H = sp.Matrix(N - 1, N, lambda h, j:
                          sp.Rational(sum(C[i, j] * C[i + h + 1, j] for i in range(N - h - 1)), q * q))
            assert all(r[j] == r[N - 1 - j] for j in range(d))
            assert all(H[h, j] == H[h, N - 1 - j] for h in range(N - 1) for j in range(d))
            uniform_v = sp.ones(N, 1) / d
            uniform_kappa = 2 * sum(abs(x) for x in H * uniform_v)
            assert rat(uniform_kappa) == base['kappa']
            rec = {'n': n, 'coefficients': source_factor['coefficients'], 'd': d, 'N': N, 'q': q,
                   'input_C_rows': base['C_rows'], 'r': [rat(x) for x in r], 'H_rows': rows(H),
                   'mirror_pairs': [[j, N - 1 - j] for j in range(d)],
                   'uniform_kappa': rat(uniform_kappa), 'surplus_mass_threshold': 2,
                   'stage': 'matrices-ready'}
            report['records'].append(rec)
            save(report, start)
            hp = H[:, :d]
            rp = r[:d, :]
            lag_count = N - 1
            primal_A = []
            primal_b = []
            for h in range(lag_count):
                slack = [sp.Integer(-int(i == h)) for i in range(lag_count)]
                primal_A.append([hp[h, j] for j in range(d)] + slack)
                primal_A.append([-hp[h, j] for j in range(d)] + slack)
                primal_b += [0, 0]
            primal_A.append([-1] * d + [0] * lag_count)
            primal_b.append(-2)
            cost = [0] * d + [2] * lag_count
            equality = [[rp[j] for j in range(d)] + [0] * lag_count]
            cap()
            primal_value, primal_variables = linprog(cost, primal_A, primal_b, equality, [1])
            cap()
            primal_value = sp.Rational(primal_value)
            primal_variables = list(map(sp.Rational, primal_variables))
            rec.update({'stage': 'primal-candidate-returned', 'raw_primal_objective': rat(primal_value),
                        'raw_primal_variables': [rat(x) for x in primal_variables]})
            save(report, start)
            masses = primal_variables[:d]
            epigraph = primal_variables[d:]
            assert all(x >= 0 for x in primal_variables)
            v = sp.zeros(N, 1)
            for j, mass in enumerate(masses):
                v[j] = v[N - 1 - j] = mass / 2
            S = sum(v)
            correlation = H * v
            assert (r.T * v)[0] == 1 and S >= 2
            assert all(epigraph[h] >= abs(correlation[h]) for h in range(lag_count))
            kappa = 2 * sum(abs(x) for x in correlation)
            assert primal_value == kappa == 2 * sum(epigraph)
            rec.update({'stage': 'primal-certified', 'pair_masses': [rat(x) for x in masses],
                        'primal_epigraph': [rat(x) for x in epigraph],
                        'v': [rat(x) for x in v], 'S': rat(S),
                        'correlations_Hv': [rat(x) for x in correlation],
                        'primal_objective': rat(primal_value), 'kappa': rat(kappa)})
            save(report, start)
            # Only paired duplicate constraints are removed; full slacks checked below.
            dual_A = [[-2 * hp[h, j] for h in range(lag_count)] + [rp[j], 1] for j in range(d)]
            dual_cost = [0] * lag_count + [-1, -2]
            bounds = [(-1, 1)] * lag_count + [(None, None), (0, None)]
            dual_minimum, dual_variables = linprog(dual_cost, dual_A, [0] * d, bounds=bounds)
            cap()
            dual_minimum = sp.Rational(dual_minimum)
            dual_variables = list(map(sp.Rational, dual_variables))
            rec.update({'stage': 'dual-candidate-returned', 'raw_dual_minimum': rat(dual_minimum),
                        'raw_dual_variables': [rat(x) for x in dual_variables]})
            save(report, start)
            y = sp.Matrix(dual_variables[:lag_count])
            lam, mu = dual_variables[-2:]
            slacks = 2 * H.T * y - lam * r - mu * sp.ones(N, 1)
            assert all(-1 <= x <= 1 for x in y) and mu >= 0 and all(x >= 0 for x in slacks)
            lower = lam + 2 * mu
            assert dual_minimum == -lower
            gap = kappa - lower
            assert gap >= 0
            weights = v / S
            weight_denominator = lcm(*(int(x.q) for x in weights))
            multiplicities = [int(x * weight_denominator) for x in weights]
            assert sum(multiplicities) == weight_denominator and all(x >= 0 for x in multiplicities)
            energy = sp.Rational(q * q, 1) / S
            aggregate_A = q * q * correlation / S
            rec.update({'stage': 'complete', 'y': [rat(x) for x in y], 'lambda': rat(lam), 'mu': rat(mu), 'dual_full_slacks': [rat(x) for x in slacks], 'dual_lower_bound': rat(lower), 'primal_dual_gap': rat(gap), 'global_optimum_certified': bool(gap == 0), 'weights': [rat(x) for x in weights], 'weight_denominator': weight_denominator, 'multiplicities': multiplicities, 'positive_weight_count': sum((x > 0 for x in multiplicities)), 'energy': rat(energy), 'aggregate_autocorrelations': [rat(x) for x in aggregate_A], 'each_full_resultant_abs': q ** d, 'income_log_argument': q, 'surplus_half_log_argument': rat(S), 'degree_bound': N - 1, 'radial_multiplier': rat(sp.Rational(N - 1, d)), 'kappa_le_4': bool(kappa <= 4), 'improves_uniform': bool(kappa < uniform_kappa)})
            save(report, start)
            print(json.dumps({'n': n, 'kappa': rat(kappa), 'lower': rat(lower), 'S': rat(S), 'optimal': gap == 0, 'positive_weights': rec['positive_weight_count']}), flush=True)
        report['status'] = 'complete'
        report['all_global_optima_certified'] = all(r['global_optimum_certified'] for r in report['records'])
        save(report, start)
        cap()
        return 0
    except Exception as error:
        report.update({'status': 'incomplete', 'error_type': type(error).__name__, 'error': _record_text(str(error)),
                       'traceback': _record_text(traceback.format_exc())})
        save(report, start)
        raise


def supervise():
    start = time.perf_counter()
    report = {'schema': 'J79-adaptive-weights-v1', 'domain_n': [18, 30], 'input': 'family-output.json', 'status': 'started', 'records': []}
    assert not CHECKPOINT.exists(), 'Preserve an old incomplete checkpoint for inspection'
    with OUTPUT.open('x', encoding='utf-8') as handle:
        json.dump(report, handle, indent=2)
    process = subprocess.Popen([sys.executable, '-X', 'utf8', str((_J_PROGRAM / 'weights-author.py')), '--worker', repr(start)],
                               creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    timed_out = False
    try:
        code = process.wait(timeout=max(0.01, CAP - (time.perf_counter() - start)))
    except subprocess.TimeoutExpired:
        timed_out = True
        process.kill()
        process.wait()
        code = 124
    result = json.loads(OUTPUT.read_text(encoding='utf-8'))
    pass
    result['worker_returncode'] = code
    result['outer_deadline_triggered'] = timed_out
    if timed_out:
        result.update({'status': 'incomplete', 'error_type': 'OuterDeadline',
                       'error': 'Worker killed at the declared aggregate 180-second deadline'})
    elif code and result['status'] != 'incomplete':
        result.update({'status': 'incomplete', 'error_type': 'WorkerExit', 'error': _record_text(str(code))})
    if CHECKPOINT.exists():
        result['interrupted_checkpoint_retained'] = CHECKPOINT.name
        OUTPUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    else:
        save(result, start)
    print(json.dumps({'status': result['status'], 'outer_deadline_triggered': timed_out}), flush=True)
    return code


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--worker':
        raise SystemExit(worker(float(sys.argv[2])))
    if len(sys.argv) != 1:
        raise SystemExit('Only the declared default command is supported')
    raise SystemExit(supervise())
