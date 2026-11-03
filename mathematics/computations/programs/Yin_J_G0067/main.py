"""Complete declared energy-eight 4x4 Gram test; author implementation.

All mathematical operations use Python integers. Outputs are native J67 files.
The deterministic forest sign reduction is proved in D150 Section3.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
from itertools import combinations, product
from collections import Counter
import json
import time

HERE = (_J_PROGRAM / 'main.py').parent
CAP = 120


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def ppow(a, n):
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def det(a):
    a = [row[:] for row in a]
    n, sign, old = len(a), 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            row = next((i for i in range(k + 1, n) if a[i][k]), None)
            if row is None:
                return 0
            a[k], a[row] = a[row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = pivot * a[i][j] - a[i][k] * a[k][j]
                assert value % old == 0
                a[i][j] = value // old
            a[i][k] = 0
        old = pivot
    return sign * a[-1][-1]


def gram(b):
    g = len(b[0])
    return [[sum(row[i] * row[j] for row in b) for j in range(g)] for i in range(g)]


def char(a):
    """Characteristic polynomial by sums of principal minors, ascending."""
    n = len(a)
    out = [0] * (n + 1)
    out[n] = 1
    for k in range(1, n + 1):
        out[n - k] = (-1) ** k * sum(
            det([[a[i][j] for j in ix] for i in ix])
            for ix in combinations(range(n), k)
        )
    return out


def block_poly(b):
    r, g = len(b), len(b[0])
    assert r >= g
    out = [0] * (2 * g + 1)
    for k, v in enumerate(char(gram(b))):
        for j, x in enumerate(ppow([1, 2, 1], k)):
            out[g - k + j] += v * x
    return mul(out, ppow([1, 1], r - g))


def proper(b):
    r, g = len(b), len(b[0])
    n = r + g
    v = [[int(i == j) for j in range(n)] for i in range(n)]
    for i in range(r):
        for j in range(g):
            v[i][r + j] = -b[i][j]
    return v


def cover(v):
    n = len(v)
    w = [[int(i == j) for j in range(2 * n)] for i in range(2 * n)]
    for i in range(n):
        for j in range(i + 1, n):
            z = v[i][j]
            for sheet in range(2):
                w[2 * i + sheet][2 * j + (sheet if z <= 0 else 1 - sheet)] = -abs(z)
    return w


def peval(p, x):
    z = 0
    for a in reversed(p):
        z = z * x + a
    return z


def pencil(a, x):
    return det([[x * a[i][j] + a[j][i] for j in range(len(a))] for i in range(len(a))])


def control(b):
    v = proper(b)
    ab = [[abs(z) for z in row] for row in b]
    av = proper(ab)
    w = cover(v)
    p, pa = block_poly(b), block_poly(ab)
    pw = mul(p, pa)
    # Each degree-n equality is verified at n+1 distinct integer nodes.
    for a, poly in [(v, p), (av, pa), (w, pw)]:
        for x in range(-len(a) // 2, len(a) // 2 + 1):
            assert pencil(a, x) == peval(poly, x)
    return dict(B=b, gram=gram(b), absolute_gram=gram(ab), V=v, absolute_V=av,
                cover=w, original=p, absolute=pa, cover_polynomial=pw,
                ranks=[len(v), len(av), len(w)],
                heights=[max(abs(z) for row in a for z in row) for a in [v, av, w]],
                energies=[sum(a[i][j] ** 2 for i in range(len(a)) for j in range(i + 1, len(a))) for a in [v, av, w]])


def signed_forms(positions, weights):
    parent = list(range(8))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    chords = []
    for k, z in enumerate(positions):
        i, j = z // 4, 4 + z % 4
        a, b = find(i), find(j)
        if a == b:
            chords.append(k)
        else:
            parent[a] = b
    for signs in product([1, -1], repeat=len(chords)):
        vals = list(weights)
        for k, sign in zip(chords, signs):
            vals[k] *= sign
        b = [[0] * 4 for _ in range(4)]
        for z, value in zip(positions, vals):
            b[z // 4][z % 4] = value
        yield b, len(chords)


def run():
    start = time.monotonic()
    stages = Counter()
    cycles = Counter()
    accepted = []
    abs_hist = Counter()
    def inspect(pos, weights, typ):
        stages[typ + '_supports'] += 1
        if stages[typ + '_supports'] % 128 == 0 and time.monotonic() - start > CAP:
            raise TimeoutError('Declared aggregate120-second cap reached; no complete result')
        for b, c in signed_forms(pos, weights):
            stages[typ + '_sign_representatives'] += 1
            cycles[str(c)] += 1
            a = gram(b)
            e2 = sum(a[i][i] * a[j][j] - a[i][j] ** 2 for i in range(4) for j in range(i + 1, 4))
            if e2 != 18:
                continue
            stages[typ + '_e2'] += 1
            cp = char(a)
            if cp != [0, -9, 18, -8, 1]:
                continue
            stages[typ + '_targets'] += 1
            ap = block_poly([[abs(z) for z in row] for row in b])
            abs_hist[tuple(ap)] += 1
            accepted.append(dict(type=typ, B=b, gram=a, gram_characteristic=cp,
                                 original=block_poly(b), absolute=ap,
                                 cover_polynomial=mul(block_poly(b), ap)))
    for pos in combinations(range(16), 8):
        inspect(pos, [1] * 8, 'eight_units')
    for double in range(16):
        for unit in combinations([i for i in range(16) if i != double], 4):
            pos = sorted((double,) + unit)
            inspect(pos, [2 if i == double else 1 for i in pos], 'one_double')
    # Complete third square partition; every matrix has at most two nonzeros.
    two_double = sum(1 for _ in combinations(range(16), 2))
    assert two_double == 120
    b5 = [[1,0,1],[0,1,1],[0,-1,1],[0,0,1],[0,1,0]]
    b7 = [[1,0,1],[0,1,0],[0,1,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1]]
    controls = dict(B5=control(b5), B7=control(b7))
    if accepted:
        controls['first_square_target'] = control(accepted[0]['B'])
    elapsed = time.monotonic() - start
    assert elapsed <= CAP
    return dict(status='complete', target_gram_characteristic=[0, -9, 18, -8, 1], stages=dict(sorted(stages.items())), cycle_sign_histogram=dict(sorted(cycles.items())), two_double_supports_rejected_by_rank=two_double, target_count=len(accepted), targets=accepted, absolute_polynomial_histogram=[dict(polynomial=list(p), count=n) for p, n in sorted(abs_hist.items())], controls=controls)


if __name__ == '__main__':
    result = run()
    ((_J_OUTPUT / 'result.json')).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ['status','stages','target_count','absolute_polynomial_histogram']}, indent=2))
