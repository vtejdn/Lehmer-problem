"""Independent verification of the finite-table, all-n S-part certificate.

Reuses only this reviewer's verify.py arithmetic helpers and freshly checks
all input polynomials, factors and orders.  No main.py or actual.py import.  Each listed
probe is recomputed by a companion matrix power and an integer Bareiss
determinant, independent of FLINT resultants.  Every n in the retained range
is checked directly from the local LTE table, followed by a rigorous tail.
"""
from fractions import Fraction
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import verify as v

HERE = _J_OUTPUT


def valuation(n, p):
    v.check(n != 0, 'valuation nonzero input')
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def bareiss(matrix):
    a = [row[:] for row in matrix]
    sign, previous = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            pivot_row = next((j for j in range(k+1, len(a)) if a[j][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                quotient, residual = divmod(numerator, previous)
                v.check(residual == 0, 'Bareiss exact division')
                a[i][j] = quotient
        for i in range(k+1, len(a)):
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def check_probe(coeff, probe, expected_n, expected_p):
    n, p, precision = probe['n'], probe['prime'], probe['precision']
    v.check(n == expected_n and p == expected_p and precision > 0, 'probe domain')
    modulus = p**precision
    a = v.companion_power(coeff, n, modulus)
    for i in range(len(a)):
        a[i][i] = (a[i][i]-1) % modulus
    remainder = v.clean([row[0] for row in a])
    v.check(remainder == v.clean(probe['remainder']), 'matrix-derived polynomial remainder')
    residue = bareiss(a) % modulus
    v.check(residue == probe['resultant_residue'] and residue != 0, 'independent determinant residue')
    exact = valuation(residue, p)
    v.check(exact == probe['valuation'] and exact < precision, 'exact modular valuation')
    return exact


def check_tables(coeff, prime_records, tables):
    v.check([t['prime'] for t in tables] == v.PRIMES, 'local-table prime coverage')
    total_probes = 0
    for row, table in zip(prime_records, tables):
        p = row['prime']
        v.check(row['squarefree'], 'unramified LTE domain')
        orders = sorted({f['root_order'] for f in row['factors']})
        v.check([g['order'] for g in table['groups']] == orders, 'complete order partition')
        isolated = []
        for g in table['groups']:
            o = g['order']
            weight = sum(f['degree'] for f in row['factors'] if f['root_order'] == o)
            v.check(g['weight'] == weight and o % p != 0, 'order-group degree and tame order')
            values = []
            v.check(len(g['probes']) == (2 if p == 2 else 1), 'required LTE probe count')
            for r, probe in enumerate(g['probes']):
                h = check_probe(coeff, probe, o*p**r, p)
                total_probes += 1
                b = h-sum(old['B'][r] for old in isolated if o % old['order'] == 0)
                values.append(b)
                v.check(b >= weight*(r+1), 'unramified valuation floor')
                v.check(b == weight*(r+1), 'automatic local floor is exact for these inputs')
            v.check(values == g['B'], 'divisor-poset isolated valuation')
            if p == 2:
                v.check(values[1] >= values[0]+weight, 'dyadic upper-constant domination')
            isolated.append(g)
        constant = sum(g['B'][1]-g['weight'] if p == 2 else g['B'][0] for g in isolated)
        v.check(constant == table['upper_constant'], 'local tail constant')
        v.check(sum(g['weight'] for g in isolated) == len(coeff)-1, 'complete local degree')
    return total_probes


def direct_weights(n, tables, degree):
    w = {p: 0 for p in v.PRIMES}
    w[2] = -degree
    for table in tables:
        p, q, exponent = table['prime'], n, 0
        while q % p == 0:
            q //= p
            exponent += 1
        for g in table['groups']:
            if q % g['order'] == 0:
                if p == 2 and exponent > 0:
                    amount = g['B'][1]+(exponent-1)*g['weight']
                else:
                    amount = g['B'][0]+exponent*g['weight']
                w[p] += amount
    return w


def check_optimum(inp, base):
    tables, degree, opt = inp['local_tables'], inp['degree'], inp['actual_optimum']
    logs = {p: v.log_bounds(p) for p in v.PRIMES}
    scaled_logs = {p: v.scaled(x) for p, x in logs.items()}
    best, limit = opt['representative_n'], opt['enumerated_n_max']
    wb = direct_weights(best, tables, degree)
    v.check(wb == {int(p): x for p, x in opt['numerator_log_weights'].items()}, 'actual winner weights')
    low, high = v.weighted_interval(wb, scaled_logs)
    v.check(low > 0, 'positive actual winner')
    old = base['aggregate_optimum']
    author_logs = {int(p): x for p, x in old['scaled_log_intervals'].items()}
    author_scale = 1 << opt['scale_bits']
    v.check(opt['scale_bits'] == old['scale_bits'], 'retained interval scale')
    v.check(set(author_logs) == set(v.PRIMES), 'author log prime coverage')
    for p in v.PRIMES:
        v.check(Fraction(author_logs[p][0], author_scale) <= logs[p][0] and
                logs[p][1] <= Fraction(author_logs[p][1], author_scale),
                'fresh independent author-log enclosure')
    v.check(v.weighted_interval(wb, author_logs) == (opt['numerator_lower'], opt['numerator_upper']),
            'retained actual winner interval')
    ties, strict = [], 0
    for n in range(1, limit+1):
        wn = direct_weights(n, tables, degree)
        _, upper = v.weighted_interval(wn, scaled_logs)
        if all(wn[p]*best == wb[p]*n for p in v.PRIMES):
            ties.append(n)
        else:
            v.check(upper*best < low*n, 'strict actual-score comparison at '+str(n))
            strict += 1
    v.check(ties == opt['maximizer_exponents'] and best == min(ties), 'actual optimum and all ties')
    v.check(strict == opt['strict_nonmaximizer_comparisons'], 'actual comparison count')
    constant_lower = sum(t['upper_constant']*logs[t['prime']][0] for t in tables)-degree*logs[2][1]
    constant_upper = sum(t['upper_constant']*logs[t['prime']][1] for t in tables)-degree*logs[2][0]
    v.check(constant_lower > degree, 'actual tail monotonicity on n>=1')
    tail_at = limit+1
    v.check(tail_at == opt['tail_at'], 'actual tail boundary')
    tail = (constant_upper+degree*v.log_bounds(tail_at)[1])/tail_at
    v.check(tail < Fraction(low, v.SCALE*best), 'actual infinite-tail exclusion')
    v.check(tail*tail_at <= Fraction(opt['tail_upper_numerator'], author_scale), 'retained actual tail enclosure')
    floor = Fraction(opt['certified_lower_decimal_truncated'])
    v.check(floor < Fraction(low, v.SCALE*best) < Fraction(high, v.SCALE*best) < floor+Fraction(1, 10**10),
            'actual displayed decimal lower and precision')
    v.check([r['prime'] for r in inp['winner_direct_probes']] == v.PRIMES, 'winner direct-probe coverage')
    for probe in inp['winner_direct_probes']:
        exact = check_probe(inp['coefficients'], probe, best, probe['prime'])
        v.check(exact == wb[probe['prime']]+(degree if probe['prime'] == 2 else 0), 'winner direct valuation matches LTE reconstruction')
    v.check(best == old['representative_n'] and wb == {int(p): x for p, x in old['numerator_log_weights'].items()},
            'actual S-part and first-floor winner agreement')
    tail_scaled = tail*v.SCALE
    return {'representative_n': best, 'maximizer_exponents': ties,
            'numerator_log_weights': wb, 'directly_checked_exponents': limit,
            'independent_scale_bits': v.BITS, 'winner_lower_scaled': low,
            'winner_upper_scaled': high, 'tail_at': tail_at,
            'tail_upper_scaled': -(-tail_scaled.numerator//tail_scaled.denominator),
            'certified_all_n_actual_S_part_optimum': True,
            'agrees_with_first_floor_at_winner': True,
            'certified_lower_decimal_truncated': opt['certified_lower_decimal_truncated']}


def run():
    initial_checks = v.CHECKS
    first = json.loads((HERE/'result.json').read_text(encoding='utf-8'))
    actual = json.loads((HERE/'actual-result.json').read_text(encoding='utf-8'))
    expected = v.polynomial_inputs()
    retained = json.loads((v.ROOT/'mathematics/computations/outputs/Yin_J_G0010/result.json').read_text(encoding='utf-8'))
    retained_inputs = {i['name']: i['coefficients'] for i in retained['inputs']}
    v.check(first['primes'] == v.PRIMES, 'base finite prime set')
    v.check(actual['primes'] == v.PRIMES, 'same finite prime set')
    base = {i['name']: i for i in first['inputs']}
    v.check(set(base) == set(expected) and len(first['inputs']) == len(expected), 'base input coverage')
    v.check({i['name'] for i in actual['inputs']} == set(base), 'actual input coverage')
    results = []
    for inp in actual['inputs']:
        b = base[inp['name']]
        coeff = expected[inp['name']]
        v.check(b['coefficients'] == coeff == retained_inputs[inp['name']], 'fresh exact base/J10 input')
        v.check(b['degree'] == len(coeff)-1 and coeff == coeff[::-1], 'fresh input degree and reciprocity')
        v.check([r['prime'] for r in b['prime_records']] == v.PRIMES, 'fresh factor/order prime coverage')
        for record in b['prime_records']:
            v.check_prime(coeff, record)
        v.check(inp['coefficients'] == b['coefficients'] and inp['degree'] == b['degree'], 'exact actual input')
        probes = check_tables(inp['coefficients'], b['prime_records'], inp['local_tables'])
        optimum = check_optimum(inp, b)
        results.append({'name': inp['name'], 'local_table_probes': probes,
                        'winner_direct_probes': len(inp['winner_direct_probes']),
                        'all_local_automatic_floors_exact': True,
                        'actual_S_part_equals_first_floor_for_all_n': True,
                        'actual_optimum_check': optimum})
        print(inp['name'], 'actual S-part independently passed;', probes, 'local probes', flush=True)
    output = {'status': 'passed',               'checks_passed': v.CHECKS-initial_checks,
              'arithmetic': 'pure Python integer companion powers and Bareiss determinants; direct n sums; independent rational log intervals',
              'author_main_or_actual_imported': False,
              'all_local_automatic_floors_exact': True,
              'all_n_equality_scope': 'the two retained inputs and the eleven selected primes from 2 through 31',
              'reused_scope': 'only verify.py arithmetic helpers; input polynomials, all 22 factor/order records and author log enclosures freshly verified mathematically',
              'inputs': results}
    (HERE/'actual-verification.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print('checks_passed', output['checks_passed'], flush=True)


if __name__ == '__main__':
    run()
