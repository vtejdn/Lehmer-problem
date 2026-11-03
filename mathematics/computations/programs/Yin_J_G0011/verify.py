"""Independent exact check of the bounded multi-prime certificate.

No main import or numerical library.  Factor candidates are checked by Rabin;
full companion matrices independently check identity/projective minimality.
The score uses direct divisibility at every n, not the author's sieve.  A
different-length rational atanh expansion gives 192-bit outward log bounds.
"""
from fractions import Fraction
from math import gcd, lcm, prod
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json

HERE = _J_OUTPUT
ROOT = _J_REPOSITORY
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
BITS = 192
SCALE = 1 << BITS
CHECKS = 0


def check(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def clean(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def product(a, b, p=None):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai*bj
    return clean([v % p for v in c] if p else c)


def remainder(a, f, p):
    a = clean([v % p for v in a])
    f = clean([v % p for v in f])
    inv = pow(f[-1], -1, p)
    for k in range(len(a)-len(f), -1, -1):
        leading = a[k+len(f)-1]*inv % p
        for j in range(len(f)):
            a[k+j] = (a[k+j] - leading*f[j]) % p
    return clean(a[:len(f)-1])


def pgcd(a, b, p):
    a, b = clean(a), clean(b)
    while b:
        a, b = b, remainder(a, b, p)
    return [v*pow(a[-1], -1, p) % p for v in a]


def difference(a, b, p):
    n = max(len(a), len(b))
    return clean([((a[i] if i < len(a) else 0) -
                  (b[i] if i < len(b) else 0)) % p for i in range(n)])


def power_x(n, f, p):
    # Left-to-right binary powering differs from the author's implementation.
    acc = [1]
    for bit in bin(n)[2:]:
        acc = remainder(product(acc, acc, p), f, p)
        if bit == '1':
            acc = remainder([0] + acc, f, p)
    return acc


def prime64(n):
    # Deterministic Miller-Rabin on the stated unsigned-64-bit domain.
    check(0 < n < 2**64, 'primality domain')
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n-1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                break
        else:
            return False
    return True


def small_prime_divisors(n):
    out, q = [], 2
    while q*q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        out.append(n)
    return out


def matrix_mul(a, b, p):
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) % p for col in bt] for row in a]


def companion_power(coeff, n, p):
    d = len(coeff)-1
    a = [[0]*d for _ in range(d)]
    for j in range(d-1):
        a[j+1][j] = 1
    for i in range(d):
        a[i][-1] = -coeff[i] % p
    out = [[int(i == j) for j in range(d)] for i in range(d)]
    while n:
        if n % 2:
            out = matrix_mul(out, a, p)
        a = matrix_mul(a, a, p)
        n //= 2
    return out


def is_scalar(a):
    c = a[0][0]
    return c != 0 and all(v == (c if i == j else 0)
                          for i, row in enumerate(a) for j, v in enumerate(row))


def check_prime(coeff, record):
    p, d = record['prime'], len(coeff)-1
    f = [v % p for v in coeff]
    rebuilt, all_order_primes, root_orders = [1], set(), []
    fs = record['factors']
    for item in fs:
        g, m, e = item['coefficients'], item['multiplicity'], item['degree']
        check(len(g) == e+1 and g[-1] == 1 and g[0] != 0 and m > 0,
              'factor shape')
        x = remainder([0, 1], g, p)
        check(power_x(p**e, g, p) == x, 'Rabin Frobenius')
        rabin = {}
        for q in small_prime_divisors(e):
            z = pgcd(g, difference(power_x(p**(e//q), g, p), x, p), p)
            rabin[str(q)] = z
            check(z == [1], 'Rabin proper subfield')
        check(rabin == item['rabin_gcds'], 'retained Rabin data')
        order = item['root_order']
        fac = {int(q): exponent for q, exponent in item['order_factorization'].items()}
        check(all(prime64(q) and exponent > 0 for q, exponent in fac.items()),
              'root-order prime factors')
        check(prod(q**exponent for q, exponent in fac.items()) == order,
              'root-order factorization product')
        check((p**e-1) % order == 0 and power_x(order, g, p) == [1],
              'root-order equality')
        check(set(item['order_prime_remainders']) == {str(q) for q in fac},
              'root-order remainder keys')
        for q in fac:
            z = power_x(order//q, g, p)
            check(z != [1], 'root-order strictness')
            check(z == clean(item['order_prime_remainders'][str(q)]), 'root-order remainder')
        for _ in range(m):
            rebuilt = product(rebuilt, g, p)
        all_order_primes.update(fac)
        root_orders.append(order)
    check(rebuilt == f, 'complete reduced factorization')
    derivative = [i*f[i] % p for i in range(1, len(f))]
    good = pgcd(f, derivative, p) == [1]
    check(good == record['squarefree'], 'unramified/squarefree guard')
    nil_order = 1
    while nil_order < max(item['multiplicity'] for item in fs):
        nil_order *= p
    if nil_order > 1:
        all_order_primes.add(p)
    identity = lcm(*root_orders)*nil_order
    check(identity == record['identity_order'], 'Jordan identity formula')
    ip = companion_power(coeff, identity, p)
    check(is_scalar(ip) and ip[0][0] == 1, 'matrix identity period')
    check(set(record['identity_prime_remainders']) == {str(q) for q in all_order_primes},
          'identity minimality keys')
    for q in all_order_primes:
        mp = companion_power(coeff, identity//q, p)
        check(not (is_scalar(mp) and mp[0][0] == 1), 'matrix identity minimality')
        check(clean([row[0] for row in mp]) == clean(record['identity_prime_remainders'][str(q)]),
              'identity retained remainder')
    scalar_n = record['scalar_order']
    check(identity % scalar_n == 0 and (p-1) % (identity//scalar_n) == 0,
          'projective/identity index')
    mp = companion_power(coeff, scalar_n, p)
    check(is_scalar(mp) and mp[0][0] == record['scalar'], 'matrix scalar period')
    scalar_primes = {q for q in all_order_primes if scalar_n % q == 0}
    check(set(record['scalar_prime_remainders']) == {str(q) for q in scalar_primes},
          'scalar minimality keys')
    for q in scalar_primes:
        mp = companion_power(coeff, scalar_n//q, p)
        check(not is_scalar(mp), 'matrix scalar minimality')
        check(clean([row[0] for row in mp]) == clean(record['scalar_prime_remainders'][str(q)]),
              'scalar retained remainder')
    minus = False
    if p != 2 and identity % 2 == 0:
        mp = companion_power(coeff, identity//2, p)
        minus = is_scalar(mp) and mp[0][0] == p-1
    check(scalar_n == (identity//2 if minus else identity), 'reciprocal scalar shortcut')
    check(record['scalar']**2 % p == 1, 'inverse-pair scalar restriction')
    return {'prime': p, 'squarefree': good, 'scalar_order': scalar_n,
            'identity_order': identity, 'factor_degrees': [i['degree'] for i in fs]}


def log_bounds(n):
    # 160 rational series terms, versus author's 100 terms and 128-bit scale.
    def series(a, b):
        z = Fraction(a-b, a+b)
        check(0 <= z <= Fraction(1, 3), 'atanh range')
        zz, term, total = z*z, z, Fraction(0)
        for j in range(160):
            total += 2*term/(2*j+1)
            term *= zz
        error = 2*term/(321*(1-zz))
        return total, total+error
    k = n.bit_length()-1
    lo2, hi2 = series(2, 1)
    lor, hir = series(n, 1 << k)
    return k*lo2+lor, k*hi2+hir


def scaled(bounds):
    lo, hi = (x*SCALE for x in bounds)
    return lo.numerator//lo.denominator, -(-hi.numerator//hi.denominator)


def weighted_interval(w, intervals):
    lo = hi = 0
    for p, v in w.items():
        a, b = intervals[p]
        lo += v*(a if v >= 0 else b)
        hi += v*(b if v >= 0 else a)
    return lo, hi


def direct_weights(n, records, degree):
    w = {p: 0 for p in PRIMES}
    w[2] = -degree
    for row in records:
        if row['squarefree']:
            p, n0, v = row['prime'], n, 0
            while n0 % p == 0:
                v += 1
                n0 //= p
            w[p] += (v+1)*sum(f['degree'] for f in row['factors'] if n % f['root_order'] == 0)
    return w


def verify_optimum(item):
    data, records, degree = item['aggregate_optimum'], item['prime_records'], item['degree']
    good = [r['prime'] for r in records if r['squarefree']]
    check(good == data['good_primes'], 'good-prime list')
    radical = prod(good)
    check(radical == data['radical'], 'good-prime radical')
    rational_logs = {p: log_bounds(p) for p in PRIMES}
    intervals = {p: scaled(v) for p, v in rational_logs.items()}
    author_scale = 1 << data['scale_bits']
    author_logs = {int(p): v for p, v in data['scaled_log_intervals'].items()}
    for p in PRIMES:
        low, high = rational_logs[p]
        check(Fraction(author_logs[p][0], author_scale) <= low and
              high <= Fraction(author_logs[p][1], author_scale), 'author log enclosure')
    best, nmax = data['representative_n'], data['enumerated_n_max']
    wb = direct_weights(best, records, degree)
    check(wb == {int(p): c for p, c in data['numerator_log_weights'].items()}, 'winner weights')
    low, high = weighted_interval(wb, intervals)
    check(low > 0, 'positive winner')
    author_lo, author_hi = weighted_interval(wb, author_logs)
    check((author_lo, author_hi) == (data['numerator_lower'], data['numerator_upper']),
          'retained combined score bounds')
    ties, compared = [], 0
    runner = None
    for n in range(1, nmax+1):
        w = direct_weights(n, records, degree)
        nl, nh = weighted_interval(w, intervals)
        if all(w[p]*best == wb[p]*n for p in PRIMES):
            ties.append(n)
        else:
            check(nh*best < low*n, 'strict finite-range comparison at '+str(n))
            compared += 1
            if runner is None or nh*runner[1] > runner[0]*n:
                runner = (nh, n)
    check(ties == data['maximizer_exponents'] and best == min(ties), 'all finite exact ties')
    check(compared == data['strict_nonmaximizer_comparisons'], 'finite comparison count')
    check(runner[1] == data['runner_up_n'], 'runner-up exponent')
    # Reconstruct author's separate-term runner interval, which is wider when
    # its positive log2 contribution partly cancels the archimedean cost.
    wr = direct_weights(runner[1], records, degree)
    _, runner_upper = weighted_interval(wr, author_logs)
    positive_two = wr[2]+degree
    runner_upper += (-degree*author_logs[2][0] + positive_two*author_logs[2][1]
                     - wr[2]*(author_logs[2][1] if wr[2] >= 0 else author_logs[2][0]))
    check(runner_upper == data['runner_up_upper_numerator'], 'retained runner upper bound')
    tail_at = nmax+1
    check(tail_at == data['tail_at'], 'tail boundary')
    log_r, log_t = log_bounds(radical), log_bounds(tail_at)
    tail_low = log_r[0]+log_t[0]-rational_logs[2][1]
    tail_high = log_r[1]+log_t[1]-rational_logs[2][0]
    check(tail_low > 1, 'tail monotonicity')
    check(degree*tail_high/tail_at < Fraction(low, SCALE*best), 'strict infinite-tail exclusion')
    check(degree*tail_high <= Fraction(data['tail_upper_numerator'], author_scale),
          'author tail upper enclosure')
    lower_decimal = Fraction(data['certified_lower_decimal_truncated'])
    check(lower_decimal < Fraction(low, SCALE*best), 'displayed decimal lower bound')
    check(Fraction(high, SCALE*best) < lower_decimal+Fraction(1, 10**10),
          'displayed decimal precision')
    scaled_tail = SCALE*degree*tail_high/tail_at
    tail_ceiling = -(-scaled_tail.numerator//scaled_tail.denominator)
    return {'representative_n': best, 'maximizer_exponents': ties,
            'directly_checked_exponents': nmax, 'numerator_log_weights': wb,
            'independent_scale_bits': BITS, 'winner_lower_scaled': low,
            'winner_upper_scaled': high, 'tail_at': tail_at,
            'tail_upper_scaled': tail_ceiling,
            'certified_all_n_optimum': True,
            'certified_lower_decimal_truncated': data['certified_lower_decimal_truncated']}


def polynomial_inputs():
    p10 = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
    numerator = [0]*25
    for j, c in [(0, 1), (7, -1), (12, -1), (17, -1), (24, 1)]:
        numerator[j] = c
    divisor, q = [1, -1, 1], [0]*23
    for k in range(22, -1, -1):
        q[k] = numerator[k+2]
        for j, c in enumerate(divisor):
            numerator[k+j] -= q[k]*c
    check(not any(numerator), 'integer input division')
    return {'lehmer': p10, 'degree22': q}


def run():
    payload = json.loads((HERE/'result.json').read_text(encoding='utf-8'))
    check(payload['primes'] == PRIMES, 'prescribed finite prime set')
    expected = polynomial_inputs()
    retained = json.loads((ROOT/'mathematics/computations/outputs/Yin_J_G0010/result.json').read_text(encoding='utf-8'))
    old_inputs = {i['name']: i['coefficients'] for i in retained['inputs']}
    results = []
    check({i['name'] for i in payload['inputs']} == set(expected), 'input names')
    for item in payload['inputs']:
        coeff = expected[item['name']]
        check(item['coefficients'] == coeff == old_inputs[item['name']], 'retained exact input')
        check(item['degree'] == len(coeff)-1 and coeff == coeff[::-1], 'degree and reciprocity')
        check([r['prime'] for r in item['prime_records']] == PRIMES, 'prime-record coverage')
        records = [check_prime(coeff, r) for r in item['prime_records']]
        optimum = verify_optimum(item)
        scalar_min = min(r['scalar_order'] for r in records)
        scalar_min_primes = [r['prime'] for r in records if r['scalar_order'] == scalar_min]
        identity_best = min(records, key=lambda r: r['prime'])
        best_log = log_bounds(identity_best['prime'])
        for r in records:
            if r['prime'] != identity_best['prime']:
                other_log = log_bounds(r['prime'])
                check(identity_best['identity_order']*other_log[1] <
                      r['identity_order']*best_log[0], 'normalized identity-period minimum')
        results.append({'name': item['name'], 'prime_checks': records, 'aggregate_check': optimum,
                        'minimum_scalar_period_primes': scalar_min_primes,
                        'minimum_scalar_period_over_degree': str(Fraction(scalar_min, item['degree'])),
                        'minimum_identity_period_over_degree_log_prime': identity_best['prime']})
        print(item['name'], 'passed; winner', optimum['representative_n'], flush=True)
    out = {'checks_passed': CHECKS,
           'arithmetic': 'pure Python integers/Fraction; companion matrices; direct n divisibility; independent 192-bit log intervals',
           'main_imported': False, 'input_data': 'result.json plus retained J10 inputs',
           'inputs': results, 'status': 'passed'}
    (HERE/'verification.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print('checks_passed', CHECKS, flush=True)


if __name__ == '__main__':
    run()
