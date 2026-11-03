"""Only n18/n30 and one predeclared exact rational descent step per input."""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'direct-author.py').parent
OUTPUT = (_J_OUTPUT / 'direct-output.json')
PENDING = _J_OUTPUT / 'direct-output.json.pending'
CAP = 30


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


def pair(x):
    x = F(x)
    return [x.numerator, x.denominator]


def vector(xs):
    return [pair(x) for x in xs]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def bin1000(x):
    lo = (1000 * x.numerator) // x.denominator
    assert F(lo, 1000) <= x < F(lo + 1, 1000)
    return [lo, lo + 1]


def save(report, start):
    pass
    PENDING.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    PENDING.replace(OUTPUT)


def worker(start):
    report = json.loads(OUTPUT.read_text(encoding='utf-8'))
    source = json.loads(((_J_OUTPUT / 'family-output.json')).read_text(encoding='utf-8'))

    def cap():
        if time.perf_counter() - start >= CAP:
            raise TimeoutError('Declared aggregate 30-second direct-step cap')

    try:
        for n in (18, 30):
            cap()
            parent = next(r for r in source['records'] if r['n'] == n)
            choices = [x for x in parent['factors'] if x['selected']]
            assert len(choices) == 1 and choices[0]['status'] == 'actual-certified'
            selected = choices[0]
            old = selected['projection']
            C, q, d, N = old['C_rows'], old['q'], old['d'], old['N']
            assert N == 2 * d and len(C) == N and all(len(row) == N for row in C)
            assert all(C[i][j] == C[j][i] for i in range(N) for j in range(N))
            assert sum(C[i][i] for i in range(N)) == q * d
            assert all(sum(C[i][h] * C[h][j] for h in range(N)) == q * C[i][j]
                       for i in range(N) for j in range(N))
            r = [F(C[j][j], q) for j in range(N)]
            assert all(x > 0 for x in r)
            Hnum = [[sum(C[i][j] * C[i + h][j] for i in range(N - h)) for j in range(N)]
                    for h in range(1, N)]
            H = [[F(x, q * q) for x in row] for row in Hnum]
            assert all(r[j] == r[N - 1 - j] for j in range(N))
            assert all(row[j] == row[N - 1 - j] for row in Hnum for j in range(N))
            v0 = [F(1, d)] * N
            a = [dot(row, v0) for row in H]
            k0 = 2 * sum(abs(x) for x in a)
            assert pair(k0) == old['kappa']
            contents = [gcd(*(C[i][j] for i in range(N))) for j in range(N)]
            assert all(content > 0 and q % content == 0 for content in contents)
            rec = {'n': n, 'coefficients': selected['coefficients'], 'd': d, 'N': N, 'q': q,
                   'C_rows': C, 'column_contents': contents, 'r': vector(r),
                   'H_rows': [vector(row) for row in H], 'v0': vector(v0),
                   'uniform_correlations': vector(a), 'uniform_kappa': pair(k0),
                   'uniform_kappa_thousandth_bin': bin1000(k0),
                   'zero_uniform_correlations': [i + 1 for i, x in enumerate(a) if x == 0],
                   'status': 'matrices-ready'}
            report['records'].append(rec)
            save(report, start)
            if any(x == 0 for x in a):
                rec['status'] = 'nonzero-correlation-premise-fails'
                save(report, start)
                continue
            signs = [1 if x > 0 else -1 for x in a]
            g = [2 * sum(signs[h] * H[h][j] for h in range(N - 1)) for j in range(N)]
            r2, g1, gr = dot(r, r), sum(g), dot(g, r)
            determinant = N * r2 - d * d
            if determinant == 0:
                assert len(set(r)) == 1
                c1, cr = g1 / N, F(0)
                span_rank = 1
            else:
                assert determinant > 0
                c1, cr = (r2 * g1 - d * gr) / determinant, (N * gr - d * g1) / determinant
                span_rank = 2
            z = [g[j] - c1 - cr * r[j] for j in range(N)]
            delta = [-x for x in z]
            norm2 = dot(z, z)
            assert sum(delta) == 0 and dot(r, delta) == 0 and dot(g, delta) == -norm2
            rec.update({'gradient': vector(g), 'normalization_span_rank': span_rank,
                        'span_coefficients_one_r': vector([c1, cr]), 'span_gram_determinant': pair(determinant),
                        'z': vector(z), 'delta': vector(delta), 'gradient_projection_squared_norm': pair(norm2)})
            if norm2 == 0:
                rec['status'] = 'equal-weights-fixed-surplus-optimal'
                save(report, start)
                continue
            Hd = [dot(row, delta) for row in H]
            positivity = [{'column': j, 'ratio': pair(v0[j] / (2 * abs(delta[j])))}
                          for j in range(N) if delta[j] < 0]
            sign_limits = [{'lag': h + 1, 'ratio': pair(abs(a[h]) / (2 * abs(Hd[h])))}
                           for h in range(N - 1) if Hd[h]]
            assert positivity and sign_limits
            candidates = [F(1)] + [F(*item['ratio']) for item in positivity + sign_limits]
            tau = min(candidates)
            assert tau > 0
            v1 = [v0[j] + tau * delta[j] for j in range(N)]
            assert all(x > 0 for x in v1) and sum(v1) == 2 and dot(r, v1) == 1
            a1 = [dot(row, v1) for row in H]
            assert all(a1[h] == a[h] + tau * Hd[h] and a1[h] * a[h] > 0 for h in range(N - 1))
            k1 = 2 * sum(abs(x) for x in a1)
            decrement = tau * norm2
            assert decrement > 0 and k1 == k0 - decrement
            weights = [x / 2 for x in v1]
            denominator = lcm(*(x.denominator for x in weights))
            multiplicities = [int(x * denominator) for x in weights]
            assert all(x > 0 for x in multiplicities) and sum(multiplicities) == denominator
            energy = F(q * q, 2)
            aggregate = [q * q * x / 2 for x in a1]
            assert 2 * sum(abs(x) for x in aggregate) / energy == k1
            rec.update({'status': 'strict-improvement-certified', 'H_delta': vector(Hd), 'positivity_half_breakpoints': positivity, 'sign_half_breakpoints': sign_limits, 'tau': pair(tau), 'v1': vector(v1), 'new_correlations': vector(a1), 'new_kappa': pair(k1), 'decrement': pair(decrement), 'new_kappa_thousandth_bin': bin1000(k1), 'decrement_thousandth_bin': bin1000(decrement), 'weights': vector(weights), 'weight_denominator': denominator, 'multiplicities': multiplicities, 'positive_weight_count': len(weights), 'energy': pair(energy), 'aggregate_autocorrelations': vector(aggregate), 'each_full_resultant_abs': q ** d, 'income_log_argument': q, 'surplus_half_log_argument': [2, 1], 'degree_bound': N - 1, 'radial_multiplier': pair(F(N - 1, d)), 'new_kappa_le_4': k1 <= 4})
            cap()
            save(report, start)
            print(json.dumps({'n': n, 'status': rec['status'], 'old_bin': bin1000(k0), 'new_bin': bin1000(k1), 'new_kappa_le_4': k1 <= 4}), flush=True)
        report['status'] = 'complete'
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
    report = {'schema': 'J79-direct-weights-v1', 'domain_n': [18, 30], 'input': 'family-output.json', 'status': 'started', 'records': []}
    assert not PENDING.exists(), 'An earlier incomplete checkpoint must be preserved'
    with OUTPUT.open('x', encoding='utf-8') as handle:
        json.dump(report, handle, indent=2)
    process = subprocess.Popen([sys.executable, '-X', 'utf8', str((_J_PROGRAM / 'direct-author.py')), '--worker', repr(start)],
                               creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    timed_out = False
    try:
        process.wait(timeout=max(0.01, CAP - (time.perf_counter() - start)))
    except subprocess.TimeoutExpired:
        timed_out = True
        process.kill()
        process.wait()
    result = json.loads(OUTPUT.read_text(encoding='utf-8'))
    result['worker_exit_code'] = process.returncode
    result['supervisor_exit_code'] = 124 if timed_out else process.returncode
    result['outer_deadline_triggered'] = timed_out
    pass
    if timed_out:
        result.update({'status': 'incomplete', 'error_type': 'OuterDeadline',
                       'error': 'Worker killed at the declared aggregate 30-second deadline'})
    elif process.returncode and result['status'] != 'incomplete':
        result.update({'status': 'incomplete', 'error_type': 'WorkerExit', 'error': _record_text(str(process.returncode))})
    if PENDING.exists():
        result['interrupted_checkpoint_retained'] = PENDING.name
        OUTPUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    else:
        save(result, start)
    print(json.dumps({'status': result['status'], 'outer_deadline_triggered': timed_out}), flush=True)
    return result['supervisor_exit_code']


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--worker':
        raise SystemExit(worker(float(sys.argv[2])))
    if len(sys.argv) != 1:
        raise SystemExit('Only the declared default command is supported')
    raise SystemExit(supervise())
