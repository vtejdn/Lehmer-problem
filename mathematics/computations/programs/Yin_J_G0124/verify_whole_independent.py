"""Independent C641/J124 review: polynomial division and termwise intervals.

Run from the repository root with standard Python 3.
Requires the retained J118 input, J121 certificate and J124 domains output.
Imports no contributor module, and does not regenerate either source certificate.
The finite mathematical result is saved to this J group's ignored output home.
"""
from fractions import Fraction as Q
from functools import cmp_to_key
from itertools import product
from pathlib import Path
import json

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[3]
OUTPUT = ROOT / 'mathematics/computations/outputs/Yin_J_G0124'
MOD = (Q(1), Q(-1), Q(-1), Q(-1), Q(1))


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def polyadd(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def polymul(a, b):
    c = [Q(0)] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def division(a, b):
    a, b = trim(a), trim(b)
    assert b
    quotient = [Q(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        j, q = len(a) - len(b), a[-1] / b[-1]
        quotient[j] += q
        for i, v in enumerate(b):
            a[i + j] -= q * v
        a = trim(a)
    return trim(quotient), a


def ring(a):
    _, a = division(a, MOD)
    return tuple(a + [Q(0)] * (4 - len(a)))


def plus(a, b):
    return ring(polyadd(a, b))


def scale(a, x):
    return ring([v * x for v in a])


def minus(a, b):
    return plus(a, scale(b, -1))


def times(a, b):
    return ring(polymul(a, b))


def inverse(a):
    r0, r1, s0, s1 = list(MOD), trim(a), [], [Q(1)]
    while r1:
        q, r2 = division(r0, r1)
        s2 = polyadd(s0, [-x for x in polymul(q, s1)])
        r0, r1, s0, s1 = r1, r2, s1, s2
    assert len(r0) == 1
    result = ring([v / r0[0] for v in s0])
    assert times(a, result) == ONE
    return result


def power(a, n):
    if n < 0:
        return power(inverse(a), -n)
    result = ONE
    for _ in range(n):
        result = times(result, a)
    return result


ZERO, ONE, BETA = ring([]), ring([Q(1)]), ring([Q(0), Q(1)])
root = json.loads((ROOT / 'mathematics/computations/programs/Yin_J_G0118/inputs.json').read_text())
assert root['polynomial_ascending'] == list(MOD)
LOW, HIGH = Q(*root['beta_lower']), Q(*root['beta_upper'])
assert Q(17, 10) < LOW < HIGH < Q(18, 10)


def enclosure(a):
    # Independent termwise monotonic powers on the positive root bracket.
    lower = upper = Q(0)
    for j, coefficient in enumerate(a):
        p, q = coefficient * LOW ** j, coefficient * HIGH ** j
        lower += min(p, q)
        upper += max(p, q)
    return lower, upper


def evaluate(a, x):
    return sum(v * x ** i for i, v in enumerate(a))


assert evaluate(MOD, LOW) < 0 < evaluate(MOD, HIGH)
assert enclosure([Q(-1), Q(-2), Q(-3), Q(4)])[0] > 0
# Irreducible modulo 2: no linear roots and not divisible by x^2+x+1.
assert sum(MOD) % 2 and MOD[0] % 2
assert any(int(x) % 2 for x in division(MOD, [Q(1), Q(1), Q(1)])[1])


def cmp(a, b):
    d = minus(a, b)
    if d == ZERO:
        return 0
    lo, hi = enclosure(d)
    assert lo > 0 or hi < 0, ('unresolved exact comparison', d, lo, hi)
    return 1 if lo > 0 else -1


def maximum(*args):
    return max(args, key=cmp_to_key(cmp))


def minimum(*args):
    return min(args, key=cmp_to_key(cmp))


def unpack(value):
    return tuple(Q(*v) for v in value)


def endpoint_pair(record):
    return unpack(record['lower']), unpack(record['upper'])


INV = inverse(BETA)
BM = minus(BETA, ONE)
T = plus(BETA, INV)
H = inverse(times(BETA, times(BM, BM)))
DELTA = minus(BETA, INV)
I = {
    -1: (minus(BETA, H), plus(H, INV)),
    0: (scale(H, -1), H),
    1: (scale(plus(H, INV), -1), minus(H, BETA)),
}
assert minus(minus(times(T, T), T), scale(ONE, 3)) == ZERO
assert times(BM, ring([-2, -1, 0, 1])) == ONE
assert cmp(H, ring([Q(1113705, 10**6)])) > 0
assert cmp(H, ring([Q(1113707, 10**6)])) < 0
assert cmp(DELTA, ring([Q(1141391, 10**6)])) > 0
assert cmp(DELTA, ring([Q(1141393, 10**6)])) < 0
assert cmp(times(BETA, BETA), plus(BETA, ONE)) > 0
assert cmp(BETA, scale(ONE, 2)) < 0

source = json.loads((ROOT / 'mathematics/computations/outputs/Yin_J_G0121/certificate.json').read_text())
target = json.loads((OUTPUT / 'domains.json').read_text())
native_input = json.loads((HOME / 'inputs.json').read_text())
assert target['input_scope'] == native_input
assert native_input['polynomial_ascending'] == list(MOD)
assert native_input['root_input'] == 'mathematics/computations/programs/Yin_J_G0118/inputs.json'
assert native_input['pair_input'] == 'mathematics/computations/outputs/Yin_J_G0121/certificate.json'
assert native_input['source_columns'] == [-1, 0, 1]
assert native_input['expected_lambda_zero_pairs_per_order'] == 147
assert (OUTPUT / 'domains.json').stat().st_size <= native_input['output_limit_bytes'] == 2097152
patterns = list(product((-1, 0, 1), repeat=4))
assert source['pattern_words'] == [list(w) for w in patterns]
assert len(source['pairs']) == 81 ** 2
old_pairs = {(p['u_index'], p['v_index']): p for p in source['pairs']}
assert len(old_pairs) == 81 ** 2


def admissible(word):
    w = times(ring(word), BM)
    return cmp(times(w, w), scale(ONE, 4)) < 0


accepted = {'YCY': [], 'CYC': []}
counts = {'YCY': 0, 'CYC': 0, 'YCY_lambda_change': 0, 'CYC_lambda_change': 0}
for ui, u in enumerate(patterns):
    for vi, v in enumerate(patterns):
        diff = tuple(vj - uj for uj, vj in zip(u, v))
        a_diff, r_diff = admissible(diff), admissible(diff[::-1])
        verdicts = {
            'YCY': a_diff and r_diff and admissible(u[::-1]) and admissible(v[::-1]),
            'CYC': a_diff and r_diff and admissible(u) and admissible(v),
        }
        old = old_pairs[(ui, vi)]
        for order, passed in verdicts.items():
            increment = sum(diff) * (1 if order == 'YCY' else -1)
            assert old[order] == passed
            assert old[order + '_lambda_change'] == increment
            if passed:
                counts[order] += 1
                counts[order + '_lambda_change'] += bool(increment)
                if not increment:
                    accepted[order].append((ui, vi))
assert counts == source['count'] == {'YCY': 183, 'CYC': 183, 'YCY_lambda_change': 36, 'CYC_lambda_change': 36}

computed = {}
grouped = {}
nonempty = {'YCY': 0, 'CYC': 0}
for order in ('YCY', 'CYC'):
    assert len(accepted[order]) == 147
    for ui, vi in accepted[order]:
        u, v = patterns[ui], patterns[vi]
        theta = [Q(vj - uj) * (1 if order == 'YCY' else -1) for uj, vj in zip(u, v)]
        quotient, remainder = division(theta, [-1, 1])
        assert not remainder
        aa, bb, cc = (quotient + [Q(0)] * 3)[:3]
        dm, dx = aa - cc, plus(scale(ONE, bb), scale(T, cc))
        assert all(x.denominator == 1 for x in (aa, bb, cc, dm))
        for m in (-1, 0, 1):
            key = (order, ui, vi, m)
            group = (m, int(m + dm), int(bb), int(cc))
            if m + dm not in I:
                computed[key] = ('target-column-absent', group, None)
                continue
            # Derive the intermediate affine label and divide its core strip.
            g0, g1 = times(power(BETA, -4), BM), times(power(BETA, -3), BM)
            if order == 'CYC':
                constant = plus(scale(times(power(BETA, 4), g0), m), ring(u))
                slope = times(power(BETA, 4), g1)
                radius = inverse(BM)
            else:
                # Stable embedding beta -> beta^-1 of c-beta^-4 u.
                us = ZERO
                for j, digit in enumerate(u):
                    us = plus(us, scale(power(INV, j), digit))
                constant = minus(scale(times(power(INV, -4), minus(INV, ONE)), m), times(power(INV, -4), us))
                slope = times(power(INV, -3), minus(INV, ONE))
                radius = times(BETA, inverse(BM))
            first = times(minus(scale(radius, -1), constant), inverse(slope))
            second = times(minus(radius, constant), inverse(slope))
            core = (minimum(first, second), maximum(first, second))
            overlap = (maximum(I[m][0], minus(I[m + dm][0], dx)), minimum(I[m][1], minus(I[m + dm][1], dx)))
            interval = (maximum(overlap[0], core[0]), minimum(overlap[1], core[1]))
            result = 'nonempty' if cmp(*interval) < 0 else 'empty'
            computed[key] = (result, group, interval)
            if result == 'nonempty':
                nonempty[order] += 1
                grouped.setdefault(group, []).append((interval, key))

assert len(computed) == 882 and nonempty == {'YCY': 259, 'CYC': 259}
assert target['counts'] == {order: {'pairs': 147, 'attempts': 441, 'nonempty': 259} for order in accepted}
assert len(target['attempts']) == len(computed)
attempt_keys = []
for saved in target['attempts']:
    key = (saved['order'], saved['u_index'], saved['v_index'], saved['from_m'])
    attempt_keys.append(key)
    result, group, interval = computed[key]
    assert saved['result'] == result
    assert group == (saved['from_m'], saved['to_m'], saved['dx_integer'], saved['dx_t'])
    if interval:
        assert endpoint_pair(saved['intersection']) == interval
assert len(set(attempt_keys)) == 882
for m, interval in I.items():
    assert endpoint_pair(target['columns'][str(m)]) == interval

expected_shifts = {
    (-1, -1): [(-1, 0), (0, 0), (1, 0)],
    (-1, 0): [(-1, 0), (0, -1), (0, 0), (1, -1)],
    (-1, 1): [(-1, -1), (0, -1), (1, -1)],
    (0, -1): [(-1, 1), (0, 0), (0, 1), (1, 0)],
    (0, 0): [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    (0, 1): [(-1, 0), (0, -1), (0, 0), (1, -1)],
    (1, -1): [(-1, 1), (0, 1), (1, 1)],
    (1, 0): [(-1, 1), (0, 0), (0, 1), (1, 0)],
    (1, 1): [(-1, 0), (0, 0), (1, 0)],
}
assert set(grouped) == {(m, n, b, c) for (m, n), steps in expected_shifts.items() for b, c in steps}
saved_groups = {(d['from_m'], d['to_m'], d['dx_integer'], d['dx_t']): d for d in target['merged_domains']}
assert set(saved_groups) == set(grouped) and len(grouped) == 33
for group, intervals in grouped.items():
    ordered = sorted(intervals, key=cmp_to_key(lambda a, b: cmp(a[0][0], b[0][0]) or cmp(a[0][1], b[0][1])))
    lo, hi = ordered[0][0]
    for (next_lo, next_hi), _ in ordered[1:]:
        assert cmp(next_lo, hi) < 0  # Equality would leave a missing point.
        hi = maximum(hi, next_hi)
    m, n, b, c = group
    dx = plus(scale(ONE, b), scale(T, c))
    endpoint_overlap = (maximum(I[m][0], minus(I[n][0], dx)), minimum(I[m][1], minus(I[n][1], dx)))
    assert (lo, hi) == endpoint_overlap
    saved = saved_groups[group]
    assert saved['equals_full_endpoint_overlap'] is True and len(saved['domains']) == 1
    assert endpoint_pair(saved['domains'][0]) == endpoint_overlap
    saved_witnesses = [attempt_keys[j] for j in saved['domains'][0]['attempt_indices']]
    assert len(saved_witnesses) == len(intervals) and set(saved_witnesses) == {key for _, key in intervals}

chosen_pairs = [((0, 1, -1, 0), (1, -1, 0, 0)), ((1, 0, 1, -1), (1, 1, -1, 0))]
chosen_keys = [('CYC', patterns.index(u), patterns.index(v), -1) for u, v in chosen_pairs]
assert {attempt_keys[s['attempt_index']] for s in target['selected_full_outer_bridges']} == set(chosen_keys)
for saved in target['selected_full_outer_bridges']:
    key = attempt_keys[saved['attempt_index']]
    assert saved['u'] == list(patterns[key[1]]) and saved['v'] == list(patterns[key[2]])
    assert saved['covers_entire_outer_column'] is True
for key in chosen_keys:
    assert computed[key][0] == 'nonempty' and computed[key][2] == I[-1]

# Check (4)--(7) without sampling any algebraic coordinate or original word.
g0, g1 = times(power(BETA, -4), BM), times(power(BETA, -3), BM)
for idx, (u, v) in enumerate(chosen_pairs):
    dx = scale(ONE, -1) if idx == 0 else minus(ONE, T)
    displacement = plus(g0, times(dx, g1))
    assert times(power(BETA, 4), displacement) == minus(ring(u), ring(v))
    values = [times(BM, plus(times(power(BETA, 4), plus(scale(g0, -1), times(s, g1))), ring(u))) for s in I[-1]]
    prescribed = (
        [plus(scale(ONE, -1), times(times(BM, BM), minus(minus(times(BETA, BETA), BETA), ONE))), minus(ONE, times(BETA, times(BM, BM)))]
        if idx == 0 else
        [plus(scale(ONE, -1), times(BM, minus(scale(ONE, 2), BETA))), plus(ONE, times(times(BETA, BETA), minus(BETA, scale(ONE, 2))))]
    )
    assert values == prescribed
    assert cmp(values[0], scale(ONE, -1)) > 0 and cmp(values[1], ONE) < 0
    assert cmp(plus(I[-1][0], dx), I[0][0]) >= 0
    assert cmp(plus(I[-1][1], dx), I[0][1]) <= 0
J = (minus(I[-1][0], ONE), minus(I[-1][1], ONE))
R = minus(T, scale(ONE, 2))
assert plus(J[0], J[1]) == R
assert cmp(minus(J[1], J[0]), ONE) > 0
assert cmp(R, ZERO) > 0 and cmp(R, ONE) < 0
assert cmp(J[0], I[0][0]) > 0 and cmp(J[1], I[0][1]) < 0
assert cmp(scale(plus(plus(ONE, H), INV), 2), scale(ONE, 6)) < 0

result = {
    'result': 'PASS',
    'method': 'Independent polynomial long division and Euclidean inversion; termwise exact rational root intervals; direct intermediate-label strip derivation; no contributor imports.',
    'source_pair_decisions': 6561,
    'source_counts': counts,
    'column_cases': len(computed),
    'nonempty_per_order': nonempty,
    'merged_domains': len(grouped),
    'all_open_unions_equal_full_endpoint_overlap': True,
    'whole_column_bridges': 2,
    'analytic_endpoint_and_descent_scalar_identities': True,
    'limits': 'No coordinate, word-length or graph-path search; no full endpoint-count values, uniform mass, congestion or critical-mean claim. Infinite coefficient termination and common-tail realization are mathematical review obligations recorded in fixed R.',
}
encoded = json.dumps(result, indent=2) + '\n'
assert len(encoded.encode()) < 16384
pending = OUTPUT / 'whole_independent_verification.partial.json'
pending.write_text(encoded, encoding='utf-8')
pending.replace(OUTPUT / 'whole_independent_verification.json')
print(encoded)
