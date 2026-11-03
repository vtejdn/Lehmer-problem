"""Predeclared 29 reciprocal inputs; exact actual-domain certificates and H4.

Old J79 pilot files are not inputs and are never changed. See readme.md.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from math import lcm
import json
import time
import traceback
import sympy as sp

HERE = (_J_PROGRAM / 'family-author.py').parent
CAP = 180
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
t, u = sp.symbols('t u')


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


def clean(a, p):
    a = [int(x) % p for x in a]
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a or [0]


def add(a, b, p, sign=1):
    return clean([(a[i] if i < len(a) else 0) + sign * (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))], p)


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return clean(out, p)


def divrem(a, b, p):
    a, b = clean(a, p), clean(b, p)
    assert b != [0]
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        c = a[-1] * inv % p
        q[shift] = c
        for j, v in enumerate(b):
            a[shift + j] = (a[shift + j] - c * v) % p
        a = clean(a, p)
    return clean(q, p), a


def powmod(a, exponent, modulus, p):
    out = [1]
    a = divrem(a, modulus, p)[1]
    while exponent:
        if exponent & 1:
            out = divrem(mul(out, a, p), modulus, p)[1]
        exponent >>= 1
        if exponent:
            a = divrem(mul(a, a, p), modulus, p)[1]
    return out


def bezout(a, b, p):
    r0, r1 = clean(a, p), clean(b, p)
    s0, s1, v0, v1 = [1], [0], [0], [1]
    while r1 != [0]:
        q, r = divrem(r0, r1, p)
        r0, r1 = r1, r
        s0, s1 = s1, add(s0, mul(q, s1, p), p, -1)
        v0, v1 = v1, add(v0, mul(q, v1, p), p, -1)
    scale = pow(r0[-1], -1, p)
    gcd = clean([scale * x for x in r0], p)
    s, v = clean([scale * x for x in s0], p), clean([scale * x for x in v0], p)
    assert add(mul(s, a, p), mul(v, b, p), p) == gcd
    return gcd, s, v


def coefficients(poly):
    return [int(poly.nth(i)) for i in range(poly.degree() + 1)]


def modular_attempts(c, cap):
    degree = len(c) - 1
    divisors = list(map(int, sp.factorint(degree)))
    attempts = []
    for prime in PRIMES:
        cap()
        f = clean(c, prime)
        x = divrem([0, 1], f, prime)[1]
        residues = {0: x}
        for j in range(1, degree + 1):
            residues[j] = powmod(residues[j - 1], prime, f, prime)
        tests = []
        for ell in divisors:
            step = degree // ell
            difference = add(residues[step], x, prime, -1)
            gcd, s, v = bezout(f, difference, prime)
            tests.append({'degree_prime_divisor': ell, 'step': step,
                          'frobenius_residue': residues[step], 'difference': difference,
                          'gcd': gcd, 'bezout_f': s, 'bezout_difference': v})
        passed = residues[degree] == x and all(test['gcd'] == [1] for test in tests)
        attempts.append({'prime': prime, 'reduced_polynomial': f, 'degree': degree,
                         'residue_at_degree': residues[degree], 'x_remainder': x,
                         'proper_degree_tests': tests, 'passed': passed})
        if passed:
            return attempts, prime
    return attempts, None


def trace_poly(f):
    d = f.degree()
    assert d % 2 == 0
    r = d // 2
    s = [sp.Integer(2), u]
    for j in range(2, r + 1):
        s.append(sp.expand(u * s[-1] - s[-2]))
    q = sp.Poly(f.nth(r) + sum(f.nth(r + j) * s[j] for j in range(1, r + 1)), u, domain=sp.ZZ)
    assert sp.expand(t ** r * q.as_expr().subs(u, t + 1 / t) - f.as_expr()) == 0
    return q


def rat(x):
    return [int(x.p), int(x.q)]


def integer_rows(matrix):
    return [[int(v) for v in row] for row in matrix.tolist()]


def projection(c, cap):
    d = len(c) - 1
    N = 2 * d
    A = sp.zeros(N, d)
    for j in range(d):
        for i, value in enumerate(c):
            A[i + j, j] = value
    G = A.T * A
    cap()
    Y = G.inv(method='DM') * A.T
    R = sp.eye(N) - A * Y
    q = lcm(*(int(v.q) for v in R), *(int(v.q) for v in Y))
    C, U = (q * R).applyfunc(int), (q * Y).applyfunc(int)
    assert C + A * U == q * sp.eye(N)
    assert C.T == C and C * C == q * C and sp.trace(C) == q * d
    diagonal_sums = [sum(R[j, j + h] for j in range(N - h)) for h in range(1, N)]
    kappa = 2 * sum(abs(v) for v in diagonal_sums) / d
    autocorrelation = [sum(c[i] * c[i + h] for i in range(d + 1 - h)) for h in range(d + 1)]
    B = autocorrelation[0]
    theta = sp.Rational(max(sum(abs(G[i, j]) for i in range(d) if i != j) for j in range(d)), B)
    gamma = sp.Rational(2 * sum(abs(v) for v in autocorrelation[1:]), B)
    cap()
    return {'d': d, 'N': N, 'G_rows': integer_rows(G), 'q': q,
            'C_rows': integer_rows(C), 'U_rows': integer_rows(U),
            'signed_diagonal_sums': [rat(v) for v in diagonal_sums],
            'endpoint_diagonals': [rat(R[0, 0]), rat(R[N - 1, N - 1])],
            'kappa': rat(kappa), 'autocorrelations': autocorrelation, 'B': B,
            'theta': rat(theta), 'gamma': rat(gamma), 'H4_passed': bool(kappa <= 4),
            'identity_checks': ['C+A*U=qI', 'C.T=C', 'C*C=qC', 'trace(C)=qd']}


def main():
    start = time.perf_counter()
    output = (_J_OUTPUT / 'family-output.json')
    report = {'schema': 'J79-reciprocal-family-v1', 'n_domain': list(range(4, 33)), 'prime_domain': PRIMES, 'trace_quarter_grid': list(range(-8, 9)), 'status': 'started', 'records': []}
    with output.open('x', encoding='utf-8') as handle:
        json.dump(report, handle, indent=2)

    def cap():
        if time.perf_counter() - start > CAP:
            raise TimeoutError('Declared aggregate 180-second author cap exceeded')

    def save():
        pass
        output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')

    try:
        for n in range(4, 33):
            cap()
            p = sp.Poly(t ** n * (t ** 3 - t - 1) + 1 - t ** 2 - t ** 3, t, domain=sp.ZZ)
            factor_unit, factors = sp.factor_list(p)
            factors.sort(key=lambda fm: (fm[0].degree(), coefficients(fm[0])))
            assert factor_unit == 1
            assert sp.prod(f.as_expr() ** multiplicity for f, multiplicity in factors).expand() == p.as_expr()
            record = {'n': n, 'polynomial': coefficients(p), 'degree': p.degree(),
                      'values_at_1_2': [int(p.eval(1)), int(p.eval(2))],
                      'coefficient_square_sum': sum(v * v for v in coefficients(p)),
                      'factor_unit': int(factor_unit), 'factor_product_verified': True, 'factors': []}
            report['records'].append(record)
            for f, multiplicity in factors:
                cap()
                c = coefficients(f)
                reciprocal = c == list(reversed(c))
                endpoints = [int(f.eval(1)), int(f.eval(2))]
                selected = reciprocal and endpoints[0] * endpoints[1] < 0
                factor_record = {'coefficients': c, 'multiplicity': int(multiplicity),
                                 'reciprocal': reciprocal, 'values_at_1_2': endpoints,
                                 'selected': selected, 'status': 'not-selected'}
                record['factors'].append(factor_record)
                if not selected:
                    continue
                attempts, prime = modular_attempts(c, cap)
                certificate = {'direct_attempts': attempts, 'method': 'uncertified'}
                factor_record['irreducibility'] = certificate
                if prime is not None:
                    certificate.update({'method': 'direct-modular', 'prime': prime})
                else:
                    assert f.degree() % 2 == 0
                    qpoly = trace_poly(f)
                    qcoeff = coefficients(qpoly)
                    trace_attempts, qprime = modular_attempts(qcoeff, cap)
                    grid = [qpoly.eval(sp.Rational(a, 4)) for a in range(-8, 9)]
                    bracket = next(([-8 + j, -7 + j] for j in range(16) if grid[j] * grid[j + 1] < 0), None)
                    certificate.update({'trace_polynomial': qcoeff, 'trace_identity_verified': True,
                                        'trace_attempts': trace_attempts, 'quarter_grid_values': [rat(v) for v in grid],
                                        'quarter_grid_bracket_numerators': bracket})
                    if qprime is not None and bracket is not None:
                        certificate.update({'method': 'trace-modular-and-interior-sign', 'prime': qprime})
                actual = certificate['method'] != 'uncertified'
                factor_record['status'] = 'actual-certified' if actual else 'conditional-uncertified'
                factor_record['projection'] = projection(c, cap)
                factor_record['actual_H4_counterexample'] = actual and not factor_record['projection']['H4_passed']
            record['complete'] = True
            pass
            save()
            print(json.dumps({'n': n, 'selected': [{'degree': len(f['coefficients']) - 1, 'status': f['status'], 'kappa': f['projection']['kappa'], 'theta': f['projection']['theta'], 'H4_passed': f['projection']['H4_passed']} for f in record['factors'] if f['selected']]}), flush=True)
        report['status'] = 'complete'
        report['selected_factor_count'] = sum(f['selected'] for r in report['records'] for f in r['factors'])
        report['certified_actual_count'] = sum(f['status'] == 'actual-certified' for r in report['records'] for f in r['factors'])
        report['actual_counterexamples'] = [{'n': r['n'], 'factor_index': j} for r in report['records']
                                           for j, f in enumerate(r['factors']) if f.get('actual_H4_counterexample', False)]
        cap()
        save()
        cap()
    except Exception as error:
        report.update({'status': 'incomplete', 'error_type': type(error).__name__, 'error': _record_text(str(error)),
                       'traceback': _record_text(traceback.format_exc())})
        save()
        raise
    print(json.dumps({'status': report['status'], 'actual_counterexamples': report['actual_counterexamples']}), flush=True)


if __name__ == '__main__':
    main()
