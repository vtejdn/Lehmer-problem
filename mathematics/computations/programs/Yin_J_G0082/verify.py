"""Author J82: exactly k=3,4,5,6, two presentations, 24 whole pencils.

Declared aggregate wall cap 120 seconds. No search, input extension or imports
from earlier author/reviewer programs. Preserve first output, including failure.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
import sympy as sp

CAP = 120
KS = (3, 4, 5, 6)
t = sp.Symbol('t')
OUT = (_J_OUTPUT / 'result.json')
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


if OUT.exists():
    raise SystemExit('Refusing to overwrite the first result.json')
started = time.perf_counter()
report = {'status': 'running', 'domain': list(KS), 'method': 'integer triangular inverse and exact characteristic polynomial', 'instances': [], 'matrix_count': 0}


def guard():
    if time.perf_counter() - started > CAP:
        raise RuntimeError('declared aggregate wall cap exceeded')


def coeff(p):
    return [int(v) for v in reversed(sp.Poly(sp.expand(p), t).all_coeffs())]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def cover(v):
    n = len(v)
    w = eye(2*n)
    for i in range(n):
        for j in range(i+1, n):
            a = v[i][j]
            if a:
                for s in (0, 1):
                    w[2*i+s][2*j+(s if a < 0 else 1-s)] = -abs(a)
    return w


def absolute(v):
    return [[(1 if i == j else -abs(v[i][j])) for j in range(len(v))]
            for i in range(len(v))]


def full(v, expected):
    guard()
    n = len(v)
    assert all(v[i][i] == 1 for i in range(n))
    assert all(v[i][j] == 0 for i in range(n) for j in range(i))
    inv = eye(n)
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            inv[i][j] = -sum(v[i][s]*inv[s][j] for s in range(i+1, j+1))
    mon = [[-sum(inv[i][s]*v[j][s] for s in range(n))
            for j in range(n)] for i in range(n)]
    actual = [int(x) for x in reversed(sp.Matrix(mon).charpoly(t).all_coeffs())]
    assert actual == coeff(expected)
    assert actual == actual[::-1] and actual[0] == actual[-1] == 1
    factor_constant, factors = sp.factor_list(sp.Poly(expected, t))
    factored = {'constant': int(factor_constant),
                'factors': [{'coefficients_ascending': coeff(f.as_expr()),
                             'multiplicity': int(m)} for f, m in factors]}
    energy = sum(v[i][j]**2 for i in range(n) for j in range(i+1, n))
    record = {'matrix': v, 'dimension': n,
              'height': max(abs(x) for row in v for x in row),
              'strict_energy': energy, 'full_squared_sum': energy+n,
              'coefficients_ascending': actual, 'factorization': factored,
              'monodromy_trace': sum(mon[i][i] for i in range(n)),
              'support_degrees': [sum(int(v[min(i,j)][max(i,j)] != 0)
                                      for j in range(n) if j != i) for i in range(n)]}
    report['matrix_count'] += 1
    return record


def mixed(u):
    n = len(u)
    N = [[-u[i][j] if i < j else 0 for j in range(n)] for i in range(n)]
    power = [row[:] for row in N]
    values = []
    for length in range(1, n):
        values.append(sum(power[i][j]*N[i][j] for i in range(n) for j in range(n)))
        power = [[sum(power[i][s]*N[s][j] for s in range(i+1, j)) if i < j else 0
                  for j in range(n)] for i in range(n)]
    return values


try:
    q, d, e = t+1, t*t+1, (t-1)**2
    A = t**4-4*t**3-2*t*t+1
    Ast = t**4-2*t*t-4*t+1
    report['seed'] = {'A': coeff(A), 'A_reversal': coeff(Ast),
                      'A_at_4': int(A.subs(t, 4)), 'A_at_5': int(A.subs(t, 5)),
                      'A_reversal_at_5': int(Ast.subs(t, 5))}
    for k in KS:
        guard()
        C = [sp.expand(sum(t**i for i in range(j+1))) for j in range(k+1)]
        T = [sp.Integer(1), sp.expand(e)]
        for j in range(2, k):
            T.append(sp.expand(e*T[-1]-4*t*t*T[-2]))
        F = sp.expand((d*d-t*q*q)*C[k]-2*d*q*t*C[k-1]
                      +q*q*t*t*C[k-2]-q*q*(t**(k+1)+t))
        assert sp.expand((t-1)*F-t**(k+1)*A+Ast) == 0
        G = sp.expand(F*T[k-1]-8*t*t*(d*C[k]-q*t*C[k-1])*T[k-2]
                      +16*t**4*C[k]*T[k-3]
                      -2**k*q*(t**(2*k)*(C[k]+1)+t*C[k]+t**(k+1)))
        original = sp.expand(q**(k-1)*e**(k-1)*F)
        companion = sp.expand(q**(k-1)*G)
        n = 4*k+1
        v = eye(n)
        for i in range(k):
            a, b, c = 3*i, 3*i+1, 3*i+2
            nxt = 3*(i+1) if i+1 < k else 4*k
            v[a][b] = v[a][c] = v[b][nxt] = -1
            v[c][nxt] = 1
        v[0][4*k] = -1
        path = [0]+list(range(3*k, 4*k))+[4*k]
        for i,j in zip(path, path[1:]):
            v[i][j] = -1
        z = eye(n)
        endpoint = k+1
        for i in range(endpoint):
            z[i][i+1] = -1
        z[0][endpoint] = -1
        for j in (k+2, k+3): z[0][j] = -1
        for j in (k+4, k+5): z[endpoint][j] = -1
        offset = k+6
        for j in range(k-1): z[offset+2*j][offset+2*j+1] = -2
        u = absolute(v)
        zu = absolute(z)
        assert zu == z
        matrices = {'V': full(v, original), 'U': full(u, companion),
                    'WV': full(cover(v), original*companion),
                    'Z': full(z, original), 'ZU': full(zu, original),
                    'WZ': full(cover(z), original**2)}
        for name in ('V', 'U', 'Z', 'ZU'):
            assert matrices[name]['strict_energy'] == 5*k+2
            assert matrices[name]['full_squared_sum'] == 9*k+3
        for name in ('WV', 'WZ'):
            assert matrices[name]['strict_energy'] == 10*k+4
            assert matrices[name]['full_squared_sum'] == 18*k+6
        values = mixed(u)
        expect = [0]*(n-1)
        expect[0], expect[k], expect[2*k-1] = 5*k+2, 1, 2**k
        assert values == expect
        assert matrices['U']['monodromy_trace'] == k+2**k+2
        assert max(matrices['V']['support_degrees']) == 4
        report['instances'].append({'k': k, 'r': k, 'F': coeff(F), 'G': coeff(G),
                                    'C': [coeff(x) for x in C],
                                    'T': [coeff(x) for x in T],
                                    'F_at_1': int(F.subs(t, 1)),
                                    'mixed_traces': values, 'matrices': matrices,
                                    'reciprocal_trace_rhs': 2**k-3*k+5,
                                    'exponential_measure_lower': 2**k-3*k+4})
    guard()
    assert report['matrix_count'] == 24
    report['status'] = 'passed'
except Exception as exc:
    report['status'] = 'failed'
    report['failure'] = {'type': type(exc).__name__, 'message': _record_text(str(exc))}
    raise
finally:
    pass
    pass
    OUT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('status', 'matrix_count')}))
