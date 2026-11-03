"""Separate reviewer certificate: dyadic intervals, trace recurrences,
exhaustive supporting hyperplanes and Lagrange coefficient bounds.

No author program is imported or rerun. Saved words/rational vertices are
witnesses only; saved floating facets and all saved conclusions are untrusted.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time

Q = 1 << 110
BASE = (_J_PROGRAM / 'review_independent.py').parent


def pt(x):
    x = F(x)*Q
    return x.numerator//x.denominator, -((-x.numerator)//x.denominator)


def add(a, b): return a[0]+b[0], a[1]+b[1]
def neg(a): return -a[1], -a[0]
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    p = [x*y for x in a for y in b]
    return min(p)//Q, -((-max(p))//Q)
def div(a, b):
    assert b[0]*b[1] > 0
    p = [F(x*Q, y) for x in a for y in b]
    lo, hi = min(p), max(p)
    return lo.numerator//lo.denominator, -((-hi.numerator)//hi.denominator)
def sq(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(x*x for x in a)
    hi = max(x*x for x in a)
    return lo//Q, -((-hi)//Q)
def rt(a):
    assert a[0] >= 0
    return isqrt(a[0]*Q), isqrt(a[1]*Q)+1
def ab(a):
    return (0 if a[0] <= 0 <= a[1] else min(abs(x) for x in a),
            max(abs(x) for x in a))
def total(xs):
    z = pt(0)
    for x in xs: z = add(z, x)
    return z
def scaled(a, n): return mul(a, pt(n))
def horner(coeff, x):
    ans = pt(0)
    for a in reversed(coeff): ans = add(mul(ans, x), pt(a))
    return ans
def cmul(a, b):
    return sub(mul(a[0], b[0]), mul(a[1], b[1])), add(mul(a[0], b[1]), mul(a[1], b[0]))
def cadd(a, b): return add(a[0], b[0]), add(a[1], b[1])
def cdiv(a, b):
    den = add(sq(b[0]), sq(b[1]))
    num = cmul(a, (b[0], neg(b[1])))
    return div(num[0], den), div(num[1], den)


def trace(x): return x*x*x-x*x-3*x+1


def root_data():
    us = []
    for lo, hi in ((F(-2), F(-1)), (F(0), F(1)), (F(2), F(9, 4))):
        assert trace(lo)*trace(hi) < 0
        while hi-lo > F(1, 1 << 122):
            mid = (lo+hi)/2
            assert trace(mid) != 0
            if trace(lo)*trace(mid) < 0: hi = mid
            else: lo = mid
        us.append((pt(lo)[0], pt(hi)[1]))
    beta = div(add(us[2], rt(sub(sq(us[2]), pt(4)))), pt(2))
    assert pt(F(3, 2))[1] < beta[0] < beta[1] < pt(F(151, 100))[0]
    zs = [(div(u, pt(2)), div(rt(sub(pt(4), sq(u))), pt(2))) for u in us[:2]]
    return us, beta, zs


def trace_tables(u, n=12):
    c, s = [pt(2), u], [pt(0), pt(1)]
    for k in range(1, n):
        c.append(sub(mul(u, c[k]), c[k-1]))
        s.append(sub(mul(u, s[k]), s[k-1]))
    return c, s


def magnitude_squared(coeff, c):
    value = pt(sum(a*a for a in coeff))
    for k in range(1, len(coeff)):
        value = add(value, scaled(c[k], sum(coeff[i]*coeff[i+k] for i in range(len(coeff)-k))))
    return value


def residue(coeff):
    # Polynomial long division in F2[t], independent of a state lookup table.
    bits = sum((a % 2) << i for i, a in enumerate(coeff))
    while bits.bit_length() > 2:
        bits ^= 0b111 << (bits.bit_length()-3)
    return bits


def word_geometry(word, tables, zs):
    assert 1 <= len(word) <= 12 and all(type(a) is int and a in (-1, 0, 1) for a in word)
    assert residue(tuple(reversed(word))) == 0
    re, im = [], []
    norms = []
    for (c, s), z in zip(tables, zs):
        re.append(div(total(scaled(c[i+1], a) for i, a in enumerate(word)), pt(2)))
        im.append(neg(mul(z[1], total(scaled(s[i+1], a) for i, a in enumerate(word)))))
        norms.append(magnitude_squared(word, c))
    norm = total(norms)
    assert norm[0] > 0
    return norm, [div(v, norm) for v in re+im]


def det3(a, b, c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def exhaustive_facets(vertices, grid):
    # Every facet of a full-dimensional 4-polytope contains four affinely
    # independent vertices. Enumerate ALL such candidate hyperplanes.
    supporting = set()
    total_candidates = 0
    independent_five = False
    for face in combinations(range(len(vertices)), 4):
        total_candidates += 1
        base = vertices[face[0]]
        rows = [[vertices[i][j]-base[j] for j in range(4)] for i in face[1:]]
        normal = [(-1)**j*det3(*[[r[k] for k in range(4) if k != j] for r in rows]) for j in range(4)]
        if not any(normal): continue
        offset = -sum(a*b for a, b in zip(normal, base))
        positive = negative = False
        for v in vertices:
            side = sum(a*b for a, b in zip(normal, v))+offset
            positive |= side > 0
            negative |= side < 0
            if positive and negative: break
        independent_five |= positive or negative
        if positive and negative: continue
        if not (positive or negative): continue
        if positive:
            normal, offset = [-a for a in normal], -offset
        divisor = 0
        for a in normal+[offset]: divisor = gcd(divisor, abs(a))
        p = tuple(a//divisor for a in normal+[offset])
        supporting.add(p)
    assert independent_five and supporting
    for p in supporting:
        assert p[-1] < 0
        assert p[-1]**2*1000**2 > 201**2*grid**2*sum(a*a for a in p[:-1])
    return total_candidates, len(supporting)


def coefficient_bounds(beta, zs, S):
    # Lagrange identity x(t)=sum_r x(r) P(t)/((t-r)P'(r)).
    # This uses synthetic division at each conjugate, not interval matrix inversion.
    roots = [(beta, pt(0)), (div(pt(1), beta), pt(0))]+zs
    all_duals = []
    p = (1, -1, 0, -1, 0, -1, 1)
    for r in roots:
        b = [None]*6
        b[5] = (pt(1), pt(0))
        for k in range(5, 0, -1): b[k-1] = cadd((pt(p[k]), pt(0)), cmul(r, b[k]))
        derivative = (pt(0), pt(0))
        for bk in reversed(b): derivative = cadd(cmul(derivative, r), bk)
        all_duals.append([cdiv(bk, derivative) for bk in b])
    upper = []
    for i in range(6):
        reals = add(ab(all_duals[0][i][0]), mul(S, ab(all_duals[1][i][0])))
        neutral_norm = rt(total(add(sq(row[i][0]), sq(row[i][1])) for row in all_duals[2:]))
        upper.append(add(reals, scaled(neutral_norm, 5))[1])  # 2R=5
    bounds = tuple(v//Q for v in upper)
    assert bounds == (2, 2, 2, 1, 1, 2)
    return bounds, [str(F(v, Q)) for v in upper]


def multiply_mod(coeff, digit):
    # Polynomial multiplication and long division by the complete P6.
    a = [digit]+list(coeff)
    p = (1, -1, 0, -1, 0, -1, 1)
    for k in range(len(a)-1, 5, -1):
        lead = a[k]
        for j in range(7): a[k-6+j] -= lead*p[j]
    assert all(v == 0 for v in a[6:])
    return tuple(a[:6])


def compact(beta, zs, tables):
    stable = div(pt(1), beta)
    S = div(beta, sub(beta, pt(1)))
    bounds, uppers = coefficient_bounds(beta, zs, S)
    counts = dict(nonzero_residue=0, real_excluded=0, stable_excluded=0, neutral_excluded=0, retained=0)
    retained = []
    for coeff in product(*(range(-b, b+1) for b in bounds)):
        if residue(coeff): counts['nonzero_residue'] += 1; continue
        xp, xm = horner(coeff, beta), horner(coeff, stable)
        rho2 = total(magnitude_squared(coeff, c) for c, _ in tables)
        if ab(xp)[0] > Q: counts['real_excluded'] += 1; continue
        if ab(xm)[0] > S[1]: counts['stable_excluded'] += 1; continue
        if rho2[0]*4 > 25*Q: counts['neutral_excluded'] += 1; continue
        assert ab(xp)[1] <= Q and ab(xm)[1] <= S[0] and rho2[1]*4 <= 25*Q
        retained.append(coeff)
        counts['retained'] += 1
    a = (-1, -1, -2, 0, 0, 1)
    assert set(retained) == {a, tuple(-v for v in a), (0,)*6}
    assert sum(counts.values()) == 5625
    x = a
    for _ in range(3): x = multiply_mod(x, 0)
    assert x == (-1, 0, 0, 1, 0, 0)
    paths = []
    for sign in (1, -1):
        x = tuple(sign*v for v in a)
        path = [x]
        for digit in (-1, 0, 0, 0, -1, 1):
            x = multiply_mod(x, sign*digit)
            path.append(x)
        assert x == (0,)*6
        paths.append(path)
    return dict(coefficient_bounds=bounds, independent_upper_enclosures=uppers,
                all_box_tuples=5625, classification=counts, retained=retained, return_paths=paths)


def main():
    started = time.monotonic()
    native_names = ('exact.py', 'verify_hulls.py', 'verify_compact.py', 'probe.py',
                    'cover12.json', 'pilot.json', 'pilot12.json', 'hull_verification.json',
                    'compact_verification.json', 'readme.md')
    before = {name: (((_J_PROGRAM if name in ('exact.py', 'probe.py', 'readme.md', 'review_independent.py', 'verify_compact.py', 'verify_hulls.py') else _J_OUTPUT) / name)).read_bytes() for name in native_names}
    words_data = json.loads(before['cover12.json'])
    vertices_data = json.loads(before['hull_verification.json'])
    assert [r['j'] for r in words_data['cells']] == list(range(50, 100))
    assert [r['j'] for r in vertices_data['cells']] == list(range(50, 100))
    grid = vertices_data['rational_grid']
    assert grid == 10**10
    _, beta, zs = root_data()
    tables = [trace_tables(scaled(z[0], 2)) for z in zs]
    cache, rows = {}, []
    min_norm = None
    min_margin = None
    for wr, vr in zip(words_data['cells'], vertices_data['cells']):
        j, words, verts = wr['j'], wr['words'], vr['rational_vertices']
        assert len(words) == len(verts)
        for word, vertex in zip(words, verts):
            key = tuple(word)
            if key not in cache: cache[key] = word_geometry(key, tables, zs)
            norm, vector = cache[key]
            min_norm = norm[0] if min_norm is None else min(min_norm, norm[0])
            assert len(vertex) == 4 and all(type(v) is int for v in vertex)
            for q, (lo, hi) in zip(vertex, vector):
                assert max(abs(F(q, grid)-F(lo, Q)), abs(F(q, grid)-F(hi, Q))) <= F(1, 100000)
            endpoints = []
            for endpoint in (F(j, 100), F(j+1, 100)):
                value = pt(endpoint)
                for digit in word: value = add(mul(beta, value), pt(digit))
                endpoints.append(value)
            margin = min(endpoints[0][0]+Q, Q-endpoints[1][1])
            assert margin > 0
            min_margin = margin if min_margin is None else min(min_margin, margin)
        tested, facets = exhaustive_facets(verts, grid)
        rows.append(dict(j=j, word_uses=len(words), all_four_subsets=tested, supporting_hyperplanes=facets))
        print(json.dumps(rows[-1]), flush=True)
    assert F(min_norm, Q) > F(61, 250)
    assert F(min_margin, Q) >= F(71, 2000000)
    assert len(cache) == 818 and sum(r['word_uses'] for r in rows) == 1379
    assert F(201, 1000)-2*F(1, 100000) > F(2009, 10000)
    assert F(61, 250)*(5*F(2009, 10000)-1) == F(549, 500000)
    compact_result = compact(beta, zs, tables)
    saved_compact = json.loads(before['compact_verification.json'])
    assert compact_result['classification'] == saved_compact['classification']
    assert [list(a) for a in compact_result['retained']] == [r['coefficients'] for r in saved_compact['retained']]
    assert [[list(a) for a in path] for path in compact_result['return_paths']] == [r['integer_path'] for r in saved_compact['exact_returns']]
    for row, saved in zip(rows, vertices_data['cells']):
        assert row['supporting_hyperplanes'] == saved['rational_facets']
    unchanged = all((((_J_PROGRAM if name in ('exact.py', 'probe.py', 'readme.md', 'review_independent.py', 'verify_compact.py', 'verify_hulls.py') else _J_OUTPUT) / name)).read_bytes() == content for name, content in before.items())
    assert unchanged
    result = dict(exact_cells=50, word_uses=sum((r['word_uses'] for r in rows)), distinct_words=len(cache), all_four_subsets=sum((r['all_four_subsets'] for r in rows)), all_supporting_hyperplanes=sum((r['supporting_hyperplanes'] for r in rows)), certified_actual_radius='2009/10000', minimum_norm_squared_lower='61/250', squared_radius_drop_lower='549/500000', independent_real_margin_lower=str(F(min_margin, Q)), compact=compact_result, cells=rows, native_files_compared=list(before))
    ((_J_OUTPUT / 'review_independent_result.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cells', 'compact')}))
    print(json.dumps(compact_result))


if __name__ == '__main__': main()
