"""Independent Fraction/Sylvester/Horner certificate, no author code imported."""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
import traceback

HERE = (_J_PROGRAM / 'verify.py').parent
OLD = _J_ROOT / 'mathematics/computations/outputs/Yin_J_G0089'
START = time.monotonic()
P = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
D = 10
REPORT = {'status': 'started', 'method': 'Independent exact Fraction elimination, companion Horner norms and Sylvester resultants', 'limits': 'Selected primal certificate only; no solver, full atom enumeration, lattice-whole proof or exact optimum.'}

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


def gate():
    assert time.monotonic() - START < 58, 'Review worker 58-second guard'

def read(name):
    path = OLD / name
    assert path.stat().st_size < 2_000_000, 'Input-size bound'
    return json.loads(path.read_text(encoding='utf8'))

def pair(x):
    x = F(x)
    return [x.numerator, x.denominator]

def frac(x):
    assert len(x) == 2
    return F(x[0], x[1])

def det(rows):
    n = len(rows)
    assert 1 <= n <= 20 and all(len(row) == n for row in rows)
    a = [[F(x) for x in row] for row in rows]
    value = F(1)
    for k in range(n):
        gate()
        at = next((i for i in range(k, n) if a[i][k]), None)
        if at is None:
            return F(0)
        if at != k:
            a[k], a[at] = a[at], a[k]
            value = -value
        pivot = a[k][k]
        value *= pivot
        for i in range(k + 1, n):
            ratio = a[i][k] / pivot
            for j in range(k + 1, n):
                a[i][j] -= ratio * a[k][j]
            a[i][k] = F(0)
    return value

def solve(rows, rhs):
    n = len(rows)
    assert n == 11 and all(len(row) == n for row in rows) and len(rhs) == n
    a = [[F(x) for x in row] + [F(b)] for row, b in zip(rows, rhs)]
    for k in range(n):
        at = next(i for i in range(k, n) if a[i][k])
        a[k], a[at] = a[at], a[k]
        pivot = a[k][k]
        a[k] = [x / pivot for x in a[k]]
        for i in range(n):
            if i != k:
                ratio = a[i][k]
                a[i] = [x - ratio * y for x, y in zip(a[i], a[k])]
    solution = [row[-1] for row in a]
    assert all(sum(F(v) * x for v, x in zip(row, solution)) == b for row, b in zip(rows, rhs))
    return solution

def auto(v, h):
    return sum(v[i] * v[i + h] for i in range(len(v) - h))

def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(D)) for j in range(D)] for i in range(D)]

def norm(residue):
    companion = [[0] * D for _ in range(D)]
    for j in range(D - 1):
        companion[j + 1][j] = 1
    for i in range(D):
        companion[i][-1] = -P[i]
    value = [[0] * D for _ in range(D)]
    for coefficient in reversed(residue):
        value = mm(value, companion)
        for i in range(D):
            value[i][i] += coefficient
    dn = det(value)
    assert dn.denominator == 1 and dn != 0
    return int(dn), value

def resultant(numerator):
    b = list(numerator)
    while b and b[-1] == 0:
        b.pop()
    assert b
    m, n = D, len(b) - 1
    if n == 0:
        return b[0] ** D, []
    size = m + n
    rows = []
    for shift in range(n):
        rows.append([0] * shift + list(reversed(P)) + [0] * (n - 1 - shift))
    for shift in range(m):
        rows.append([0] * shift + list(reversed(b)) + [0] * (m - 1 - shift))
    assert len(rows) == size and all(len(row) == size for row in rows)
    answer = det(rows)
    assert answer.denominator == 1
    return int(answer), rows

def canonical(v):
    v = list(v)
    assert any(v)
    return v if next(x for x in v if x) > 0 else [-x for x in v]

def primitive(v):
    g = gcd(*v)
    assert g > 0
    return canonical([x // g for x in v])

def shift(v):
    return [-v[-1] * P[0]] + [v[i - 1] - v[-1] * P[i] for i in range(1, D)]

def main():
    saved, lead = read('highs_result.json'), read('highs_lead.json')
    old, fail = read('progress.json'), read('failure.json')
    matrix = read('matrix.json')
    assert saved['coefficients'] == lead['coefficients'] == matrix['coefficients'] == P
    assert saved['d'] == saved['allowed_T'] == D and saved['N'] == 11
    assert saved['status'] == 'complete' and saved['outcome'] == 'exact-first-window-packet-below-one'
    assert len(saved['packet']) == 10
    indices = lead['basis']['basic_original_columns']
    nums36 = lead['basic_column_numerators']
    assert len(indices) == len(nums36) == 11 and len(set(indices)) == 11
    assert all(len(v) == 11 and all(isinstance(x, int) and abs(x) <= 10**6 for x in v) for v in nums36)
    assert all(0 <= j < 762150 for j in indices)
    a = [[int(i == j) for j in range(D)] + [-P[i]] for i in range(D)]
    assert matrix['A_rows'] == a
    beta = [1, 0, 1, 0, 0, 0, -1, -1, 1, 1, -1]
    h0 = [[2 if i == j else -beta[abs(i-j)] for j in range(11)] for i in range(11)]
    h = [row[:D] for row in h0[:D]]
    assert matrix['beta'] == beta and matrix['H0_rows'] == h0 and matrix['H_rows'] == h
    assert [sum(row[j]*P[j] for j in range(11)) for row in h0] == [0]*11
    assert all(sum(a[k][i]*h[k][l]*a[l][j] for k in range(D) for l in range(D)) == h0[i][j]
               for i in range(11) for j in range(11))
    congruence = matrix['congruence_certificate']
    s = [[frac(x) for x in row] for row in congruence['basis_rows']]
    block = [[frac(x) for x in row] for row in congruence['block_rows']]
    assert len(s) == len(block) == 10 and all(len(row) == 10 for row in s+block)
    assert det(s) == -1 and pair(det(s)) == congruence['basis_determinant']
    assert all(sum(s[k][i]*h[k][l]*s[l][j] for k in range(D) for l in range(D)) == block[i][j]
               for i in range(D) for j in range(D))
    assert all(block[i][j] == 0 for i in range(D) for j in range(D) if i != j)
    assert sum(block[i][i] > 0 for i in range(D)) == 9 and sum(block[i][i] < 0 for i in range(D)) == 1
    assert congruence['inertia'] == {'positive':9, 'negative':1, 'zero':0}
    negative = congruence['negative_integer_witness']
    ternary = matrix['ternary_scan']['first_minimum_vector']
    assert negative == [2,4,3,2,0,0,-3,-2,-4,0]
    assert sum(negative[i]*h[i][j]*negative[j] for i in range(D) for j in range(D)) == -4 == congruence['negative_H_value']
    assert ternary == [0,1,1,1,0,0,-1,-1,-1,-1] and all(x in (-1,0,1) for x in ternary)
    assert sum(ternary[i]*h[i][j]*ternary[j] for i in range(D) for j in range(D)) == 0
    REPORT['phase_A_small_payload_certificate'] = {'kernel_descent_verified': True,
          'rational_congruence_verified': True, 'basis_determinant':[-1,1],
          'diagonal_entries':[pair(block[i][i]) for i in range(D)],
          'negative_witness_H_value':-4, 'displayed_ternary_witness_H_value':0,
          'full_ternary_minimum_rerun':False, 'integral_lattice_equivalence_claim':False}
    rows = [[1296] * 11] + [[auto(v, h) for v in nums36] for h in range(1, 11)]
    rhs = [1296] + [0] * 10
    assert rows == saved['exact_original_system'] and rhs == saved['exact_system_rhs']
    weights = solve(rows, rhs)
    assert weights == [frac(x) for x in saved['exact_basis_weights']]
    assert all(x >= 0 for x in weights) and sum(weights) == 1
    support = [(j, [F(x, 36) for x in v], w) for j, v, w in zip(indices, nums36, weights) if w]
    assert len(support) == 10
    assert [j for j, f, w in support] == [r['atom_index'] for r in saved['packet']]
    q = lcm(*(x.denominator for j, f, w in support for x in f))
    mw = lcm(*(w.denominator for j, f, w in support))
    assert q == saved['actual_q'] == 9 and mw == saved['actual_M'] == 2043
    assert [int(w * mw) for j, f, w in support] == [155, 172, 533, 612, 334, 3, 3, 3, 227, 1]
    records = []
    for (index, f, w), declared in zip(support, saved['packet']):
        gate()
        assert [pair(x) for x in f] == declared['coefficients'] and pair(w) == declared['weight']
        numerator = [int(q * x) for x in f]
        assert all(F(x, q) == y for x, y in zip(numerator, f))
        assert numerator == declared['numerator_coefficients']
        residue = [sum(F(a[i][j]) * f[j] for j in range(11)) for i in range(D)]
        assert any(residue) and all(x.denominator == 1 for x in residue)
        residue = [int(x) for x in residue]
        assert residue == declared['integer_residue']
        dn, norm_matrix = norm(residue)
        res, sylvester = resultant(numerator)
        assert dn == declared['signed_residue_norm']
        assert res == q**D * dn == declared['signed_numerator_resultant']
        content = gcd(*numerator)
        assert content == declared['content'] and res % content**D == 0
        energy = sum(x * x for x in f)
        lags = [auto(f, h) for h in range(1, 11)]
        assert pair(energy) == declared['energy'] and [pair(x) for x in lags] == declared['autocorrelations']
        generator = declared['generator']
        seed = generator['seed']
        assert len(seed) == 10 and primitive(seed) == seed
        origin = generator['seed_provenance']
        if origin['kind'] == 'ternary':
            assert all(x in (-1, 0, 1) for x in seed)
        else:
            assert origin == {'kind': 'adjacent-orbit', 'anchor': 1, 'power': 1, 'sign': 1}
            base = old['actual_anchors'][1]
            assert base == [2, 4, 3, 2, 0, 0, -3, -2, -4, 0]
            first = shift(base)
            assert seed == primitive([x + y for x, y in zip(first, shift(first))])
        ell = generator['scalar_l']
        assert isinstance(ell, int) and -12 <= ell <= 12
        multiplier = ell - 4 * sum(seed[i] * P[i] for i in range(D))
        generated = canonical([36 * seed[i] + multiplier * P[i] for i in range(D)] + [multiplier])
        assert generated == [int(36 * x) for x in f]
        old_member = False
        for sign in (-1, 1):
            r = [sign * x for x in residue]
            if all(x in (-1, 0, 1) for x in r) and next(x for x in r if x) == 1:
                k = 9 * sign * f[-1] + sum(r[i] * P[i] for i in range(D))
                if k.denominator == 1 and -2 <= k <= 2 and energy <= 4:
                    old_member = True
        initial = any(f == [F(int(i == 0 or (h and i == h))) for i in range(11)] for h in range(11))
        old_member = old_member or initial
        functional = energy - lags[1] + lags[5] + lags[6] - lags[7] - lags[8] + lags[9]
        records.append({'atom_index': index, 'weight': pair(w), 'multiplicity': int(w * mw),
                        'numerator_coefficients': numerator, 'integer_residue': residue,
                        'content': content, 'actual_individual_denominator': lcm(*(x.denominator for x in f)),
                        'energy': pair(energy), 'autocorrelations': [pair(x) for x in lags],
                        'signed_norm': dn, 'norm_multiplication_matrix': norm_matrix,
                        'signed_resultant': res, 'sylvester_matrix': sylvester,
                        'selected_generator_verified': True, 'old_C24_family_member': old_member,
                        'old_finite_functional_value': pair(functional)})
        REPORT['verified_prefix'] = records
    assert [r['signed_norm'] for r in records] == [1] * 9 + [-269]
    energy = sum(w * sum(x * x for x in f) for j, f, w in support)
    lags = [sum(w * auto(f, h) for j, f, w in support) for h in range(1, 11)]
    assert energy == F(680, 681) and pair(energy) == saved['energy']
    assert lags == [0] * 10 and [pair(x) for x in lags] == saved['all_lags']
    positions = [i for j, f, w in support for i, x in enumerate(f) if x]
    width = max(positions) - min(positions)
    assert width == saved['actual_union_width'] == 10
    assert pair(q * q * energy) == saved['integer_numerator_energy_S']
    assert mw * energy == 2040 and pair(mw * energy) == saved['ME']
    assert energy >= F(451609, 508032) and q >= 5 and 1 <= mw * energy < mw
    sign = (-1) ** sum(r['multiplicity'] for r in records if r['signed_norm'] < 0)
    expected_product = {'sign': sign, 'scalar_factor': [q, D * mw],
                        'absolute_residue_factors': [[abs(r['signed_norm']), r['multiplicity']] for r in records]}
    assert expected_product == saved['copied_full_signed_product'] and sign == -1
    assert any(not r['old_C24_family_member'] for r in records)
    assert any(frac(r['old_finite_functional_value']) < 1 for r in records)
    assert sum(frac(r['weight']) * frac(r['old_finite_functional_value']) for r in records) == energy
    for key in ('seed_count', 'generated_labels', 'distinct_atoms', 'actual_anchors', 'true_initial_basis', 'true_initial_numerators'):
        assert saved[key] == old[key] == fail[key]
    assert [old[k] for k in ('seed_count', 'generated_labels', 'distinct_atoms')] == [30486, 762161, 762150]
    assert old['status'] == 'atoms-ready' and fail['status'] == 'failed'
    assert fail['error'] == 'Declared3000-pivot cap' and fail['parameters']['pivot_cap'] == 3000
    assert not any(k in fail for k in ('floating_lead', 'returned_basis_numerators', 'exact_basis_weights', 'packet'))
    assert not ((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0089/result.json')).exists()
    assert lead['primal_column_count'] == lead['basis']['column_count'] == 762150
    assert len(lead['basis']['row_status']) == 11 and lead['basis']['valid']
    assert lead['status'] == 'returned-uncertified-lead'
    REPORT.pop('verified_prefix', None)
    REPORT.update(status='complete', original_coefficients=P, original_A_rows=a,
                  exact_original_rows=rows, exact_rhs=rhs, basic_original_indices=indices,
                  exact_basic_weights=[pair(x) for x in weights], packet=records,
                  energy=pair(energy), actual_q=q, actual_M=mw, ME=int(mw * energy),
                  all_lags=[pair(x) for x in lags], actual_union_width=width,
                  integer_energy=pair(q*q*energy), copied_product=expected_product,
                  simplified_copied_product={'sign': -1, 'positive_factors': [[269, 1], [9, 20430]]},
                  norm_income='log(9)+log(269)/20430',
                  normalized_surplus='log(269)/20430+(1/2)*log(681/680)',
                  actual_expense='(10/10)*m(original P)',
                  declaration_scopes_agree=True, selected_family_membership_verified=True,
                  full_atom_enumeration_rerun=False, solver_rerun=False,
                  phase_A_terminal_scope='Declared pivot-cap failure, no saved final solver state, no infeasibility conclusion',
                  phase_B_terminal_scope='Completed exact primal; numerical Optimal is not exact optimality')
    pass
    ((_J_OUTPUT / 'certificate.json')).write_text(json.dumps(REPORT, indent=2) + '\n', encoding='utf8')
    print(json.dumps({'status': 'complete', 'energy': pair(energy), 'q': q, 'M': mw, 'norms': [r['signed_norm'] for r in records], 'width': width, 'old_family_members': [r['old_C24_family_member'] for r in records]}))

if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        REPORT.update(status='failed', error_type=type(error).__name__, error=_record_text(str(error)), traceback=_record_text(traceback.format_exc()))
        ((_J_OUTPUT / 'failure.json')).write_text(json.dumps(REPORT, indent=2) + '\n', encoding='utf8')
        raise
