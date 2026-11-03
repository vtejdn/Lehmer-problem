"""Complete declared energy-eight 5x4 Gram test; author implementation.

All mathematical operations use Python integers. Outputs are native J104 files; J67 algorithms are adapted with explicit new dimensions.
The deterministic forest sign reduction is proved in record.md before execution.
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
CAP = 300


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
    parent = list(range(9))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    chords = []
    for k, z in enumerate(positions):
        i, j = z // 4, 5 + z % 4
        a, b = find(i), find(j)
        if a == b:
            chords.append(k)
        else:
            parent[a] = b
    for signs in product([1, -1], repeat=len(chords)):
        vals = list(weights)
        for k, sign in zip(chords, signs):
            vals[k] *= sign
        b = [[0] * 4 for _ in range(5)]
        for z, value in zip(positions, vals):
            b[z // 4][z % 4] = value
        yield b, len(chords)


def save(result, check_time=None):
    target = _J_OUTPUT / "result.json"
    pending = target.with_suffix(".json.writing")
    encoded = json.dumps(result, indent=2) + "\n"
    if check_time:
        check_time()
    pending.write_text(encoded, encoding="utf-8")
    if check_time:
        check_time()
    pending.replace(target)


def run():
    from math import comb
    start = time.monotonic()
    target = [0, -9, 18, -8, 1]
    expected_original = mul(ppow([1, 1], 3), [1, -2, 1, -1, 1, -2, 1])
    stages, cycles, hist = Counter(), Counter(), Counter()
    accepted, representatives = [], {}
    result = dict(status="incomplete", rows=5, columns=4, energy=8,
                  target_gram_characteristic=target, target_original=expected_original,
                  cap_seconds=CAP, stages={}, targets=[])
    save(result)

    def check_time():
        if time.monotonic()-start > CAP:
            raise TimeoutError("Declared aggregate300-second cap reached")

    def inspect(pos, weights, kind):
        stages[kind+"_supports"] += 1
        if stages[kind+"_supports"] % 128 == 0:
            check_time()
        for b, count in signed_forms(pos, weights):
            stages[kind+"_sign_representatives"] += 1
            cycles[str(count)] += 1
            g = gram(b)
            assert sum(g[i][i] for i in range(4)) == 8
            e2 = sum(g[i][i]*g[k][k]-g[i][k]**2 for i in range(4) for k in range(i+1,4))
            if e2 != 18:
                continue
            stages[kind+"_e2"] += 1
            cp = char(g)
            if cp != target:
                continue
            stages[kind+"_targets"] += 1
            ab = [[abs(v) for v in row] for row in b]
            ag = gram(ab)
            acp = char(ag)
            original, absolute = block_poly(b), block_poly(ab)
            assert original == expected_original
            equality = acp == target
            row = dict(type=kind, B=b, gram=g, gram_characteristic=cp,
                       absolute_gram=ag, absolute_gram_characteristic=acp,
                       original=original, absolute=absolute,
                       cover_polynomial=mul(original, absolute), equality=equality)
            accepted.append(row)
            key=tuple(acp)
            hist[key] += 1
            representatives.setdefault(key,b)

    try:
        for pos in combinations(range(20),8):
            inspect(pos,[1]*8,"eight_units")
        print("eight-unit domain complete",dict(stages),flush=True)
        for double in range(20):
            for unit in combinations([i for i in range(20) if i!=double],4):
                pos=sorted((double,)+unit)
                inspect(pos,[2 if p==double else 1 for p in pos],"one_double")
        two_double=comb(20,2)
        assert stages["eight_units_supports"] == comb(20,8)
        assert stages["one_double_supports"] == 20*comb(19,4)
        assert two_double == 190
        assert accepted, "The known three-column target with a zero fourth column belongs to this domain"
        controls={}
        for number,(key,b) in enumerate(sorted(representatives.items())):
            check_time()
            controls[str(number)] = control(b)
            assert char(controls[str(number)]["absolute_gram"]) == list(key)
        check_time()
        result.update(status="complete",stages=dict(sorted(stages.items())),
                      cycle_sign_histogram=dict(sorted(cycles.items())),
                      two_double_supports_rejected_by_rank=two_double,
                      target_count=len(accepted), equality_count=sum(v["equality"] for v in accepted),
                      targets=accepted,
                      absolute_gram_histogram=[dict(characteristic=list(key),count=value)
                                              for key,value in sorted(hist.items())],
                      representative_controls=controls)
        save(result, check_time)
        print(json.dumps({k:result[k] for k in ("status","stages","target_count","equality_count","absolute_gram_histogram")},indent=2),flush=True)
        return
    except Exception as error:
        result.update(status="incomplete", error=type(error).__name__+": "+str(error),stages=dict(stages),
                      cycle_sign_histogram=dict(cycles),targets=accepted,
                      target_count=len(accepted))
        save(result)
        raise


if __name__ == "__main__":
    run()
