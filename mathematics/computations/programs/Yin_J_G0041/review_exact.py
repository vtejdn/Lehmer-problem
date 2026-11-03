"""Independent finite check of D68, without importing/rerunning its author code.

Field elements are columns acted on by an integer companion matrix; determinants
are the 720-term permutation formula and coordinates use Cramer's rule. This is
deliberately distinct from author convolution reduction, Bareiss, and elimination.
The all-h, module, and metric claims require the separate written proof review.
"""
from fractions import Fraction as Q
from itertools import permutations
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

ROOT = (_J_ROOT / 'mathematics')
HERE = (_J_PROGRAM / 'review_exact.py').parent
AUTHOR = [((_J_PROGRAM if n in ('readme.md', 'review_exact.py', 'verify.py') else _J_OUTPUT) / n) for n in ('readme.md', 'verify.py', 'verification.json')]
AUTHOR.append((_J_ROOT / 'mathematics/ledger/Yin_L_G0204_v1.md'))


def ident():
    return [[int(i == j) for j in range(6)] for i in range(6)]


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(6))
             for j in range(6)] for i in range(6)]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def mp(a, n):
    out = ident()
    for _ in range(n):
        out = mm(out, a)
    return out


def vs(a, b):
    return [x-y for x, y in zip(a, b)]


def ms(a, b):
    return [vs(x, y) for x, y in zip(a, b)]


def det(a):
    out = 0
    for perm in permutations(range(6)):
        term = (-1)**sum(perm[i] > perm[j] for i in range(6) for j in range(i+1, 6))
        for i, j in enumerate(perm):
            term *= a[i][j]
        out += term
    return out


def coordinates(a, b):
    denominator = det(a)
    answer = []
    for j in range(6):
        replaced = [row[:] for row in a]
        for i in range(6):
            replaced[i][j] = b[i]
        answer.append(Q(det(replaced), denominator))
    assert mv(a, answer) == b
    return list(map(str, answer))


def columns(vectors):
    return list(map(list, zip(*vectors)))


def main():
    before = {p: p.read_bytes() for p in AUTHOR}
    saved = json.loads(((_J_OUTPUT / 'verification.json')).read_text())
    one = [1, 0, 0, 0, 0, 0]
    zero = [0]*6
    companion = [[0]*6 for _ in range(6)]
    for i in range(5):
        companion[i+1][i] = 1
    for i, coefficient in enumerate([-1, 1, 0, 1, 0, 1]):
        companion[i][5] = coefficient
    identity = ident()
    cp = [mp(companion, k) for k in range(8)]
    inverse = [[identity[i][j]+cp[2][i][j]+cp[4][i][j]-cp[5][i][j]
                for j in range(6)] for i in range(6)]
    assert mm(companion, inverse) == identity
    theta = cp[6]
    beta = mv(companion, one)
    c = columns([mv(mp(theta, k), one) for k in range(6)])
    assert c == saved['power_coordinate_matrix']
    assert det(c) == saved['determinant'] == 1024
    assert coordinates(c, beta) == saved['beta_in_theta_basis']
    am = ms(identity, mp(inverse, 3))
    gm = mm(theta, am)
    a, g = mv(am, one), mv(gm, one)
    assert a == saved['a'] and g == saved['g']

    def word(state, digits):
        path = [state[:]]
        for digit in digits:
            assert digit in (-1, 0, 1)
            state = mv(companion, state)
            state[0] += digit
            path.append(state)
        return path

    w = [-1, 0, 0, 0, -1, 1]
    assert w == saved['generator_return']
    assert word(a, w)[-1] == zero
    assert word(zero, w)[-1] == [-x for x in g]
    bm1 = ms(companion, identity)
    x1 = mv(bm1, a)
    y1 = mv(mm(mp(inverse, 6), bm1), one)
    x2 = mv(mm(ms(cp[3], identity), mp(bm1, 2)), one)
    y2 = mv(mm(mp(inverse, 3), mp(bm1, 2)), one)
    assert mv(gm, y1) == x1 and mv(gm, y2) == x2
    witnesses = [(saved['first_witness'], x1, y1),
                 (saved['inner_strip_witness'], x2, y2)]
    for record, x, y in witnesses:
        assert record['x'] == x and record['scaled_y'] == y
        cc = coordinates(c, y)
        assert cc == record['scaled_y_theta_coordinates']
        assert any(Q(t).denominator > 1 for t in cc)
    path = word(x1, [0, 0, -1, -1, 1, 0])
    assert path == saved['first_witness']['integer_path']
    assert path[4] != zero and path[5] == path[6] == zero
    assert mv(theta, x1) == [0, -1, 1, 1, 0, 0]
    assert y2 == [1, -1, 1, -2, 1, 0]

    lo, hi = Q(3, 2), Q(151, 100)
    assert hi-1 == Q(saved['first_witness_real_bounds'][0]) < 1
    assert (hi**3-1)*(1-1/hi) == Q(saved['first_witness_real_bounds'][1]) < 1
    assert (hi-1)**2/lo**3 == Q(289, 3750) < 1/(hi**6-1)
    assert (hi-1)**2/lo**3 == Q(saved['inner_strip_witness']['plus_upper_bound'])
    assert 1/(hi**6-1) == Q(saved['inner_strip_witness']['macro_plus_radius_lower_bound'])
    assert hi*(hi-1)**2 == Q(saved['inner_strip_witness']['minus_upper_bound']) < 1
    v = [-1, 0, -1, 0, -1, 1]
    prefixes = word(one, v)
    assert prefixes == saved['return_of_one']['prefixes']
    assert prefixes[-1] == zero
    assert prefixes[5] == [-x for x in mv(inverse, one)]
    assert det(columns(prefixes[:6])) == 1
    # Exact endpoint evaluation, justified by increasing derivatives for s1..s4.
    assert 3*lo**2-2*hi > 0
    assert 4*lo**3-3*hi**2-1 > 0
    bounds = [(Q(1), Q(1))]
    for state in prefixes[1:5]:
        bounds.append(tuple(sum(Q(a)*b**j for j, a in enumerate(state)) for b in (lo, hi)))
    bounds.extend([(-1/lo, -1/hi), (Q(0), Q(0))])
    printed = [('1','1'), ('1/2','51/100'), ('3/4','7701/10000'),
               ('1/8','162851/1000000'), ('3/16','24590501/100000000'),
               ('-2/3','-100/151'), ('0','0')]
    assert bounds == [tuple(map(Q, pair)) for pair in printed]
    assert all(-1 <= left <= right <= 1 for left, right in bounds)

    record = saved['cyclic_rotation_illustration']
    assert record['h'] == 7
    cyclic = v+[1]
    g7m = ms(cp[7], identity)
    assert record['word'] == cyclic and record['generator'] == mv(g7m, one)
    assert word(one, cyclic)[-1] == one
    assert word(vs(one, mv(mp(inverse, 7), one)), cyclic)[-1] == zero
    assert len(record['rotations']) == 7
    for j in range(7):
        rotated = cyclic[j:]+cyclic[:j]
        translation = word(zero, rotated)[-1]
        digit = [-x for x in prefixes[j]]
        assert translation == mv(g7m, digit)
        assert record['rotations'][j] == {'rotation': j, 'word': rotated,
                                         'translation': translation, 'divided_digit': digit}
    assert all(p.read_bytes() == data for p, data in before.items())
    result = {'status': 'passed', 'method': 'integer companion matrices; permutation determinants; Cramer coordinates', 'power_order_index': det(c), 'actual_witnesses': 2, 'original_return_first_zero_step': 5, 'prefix_Z_basis_determinant': 1, 'printed_prefix_bounds': printed, 'cyclic_rotations_checked': 7, 'finite_scope': 'h=7 only; all-h, module, and joint metric claims checked in written review', 'author_code_imported_or_executed': False}
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
