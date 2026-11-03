"""Author exact interval utilities, adapted from the inspected J22 pattern.

All arithmetic is rational and rounded outward to a fixed decimal grid.
"""
from fractions import Fraction as F
from math import isqrt

SCALE = 10**35


def floor(x): return x.numerator // x.denominator
def point(x): return F(x), F(x)
def outward(a): return F(floor(a[0]*SCALE), SCALE), F(-floor(-a[1]*SCALE), SCALE)
def add(a, b): return outward((a[0]+b[0], a[1]+b[1]))
def neg(a): return -a[1], -a[0]
def sub(a, b): return add(a, neg(b))


def mul(a, b):
    v = [x*y for x in a for y in b]
    return outward((min(v), max(v)))


def div(a, b):
    assert b[0] > 0 or b[1] < 0
    return mul(a, (1/b[1], 1/b[0]))


def square(a):
    return outward((0 if a[0] <= 0 <= a[1] else min(x*x for x in a), max(x*x for x in a)))


def sqrt_interval(a):
    assert a[0] >= 0
    return F(isqrt(floor(a[0]*SCALE*SCALE)), SCALE), F(isqrt(floor(a[1]*SCALE*SCALE))+1, SCALE)


def absolute(a):
    return (0 if a[0] <= 0 <= a[1] else min(abs(x) for x in a), max(abs(x) for x in a))


def total(values):
    value = point(0)
    for v in values: value = add(value, v)
    return value


def cmul(a, b):
    return sub(mul(a[0], b[0]), mul(a[1], b[1])), add(mul(a[0], b[1]), mul(a[1], b[0]))


def trace(x): return x**3-x**2-3*x+1


def roots():
    # Three disjoint sign-changing intervals exhaust the cubic degree.
    brackets = [(F(-2), F(-1)), (F(0), F(1)), (F(2), F(9, 4))]
    result = []
    for lo, hi in brackets:
        fl, fh = trace(lo), trace(hi)
        assert fl*fh < 0
        while hi-lo > F(1, SCALE*100):
            mid = (lo+hi)/2
            fm = trace(mid)
            assert fm != 0
            if fl*fm < 0: hi, fh = mid, fm
            else: lo, fl = mid, fm
        result.append(outward((lo, hi)))
    outer = result[-1]
    beta = div(add(outer, sqrt_interval(sub(square(outer), point(4)))), point(2))
    assert F(3, 2) < beta[0] < beta[1] < F(151, 100)
    zs = []
    for value in result[:-1]:
        re = div(value, point(2))
        zs.append((re, sqrt_interval(sub(point(1), square(re)))))
    return beta, zs


def word_geometry(word, beta, zs):
    powers = [(point(1), point(0)) for z in zs]
    c = [(point(0), point(0)) for z in zs]
    residue = 0
    for digit in word:
        assert type(digit) is int and digit in (-1, 0, 1)
        residue = (0, 2, 3, 1)[residue] ^ (digit % 2)
        for j, z in enumerate(zs):
            powers[j] = cmul(powers[j], (z[0], neg(z[1])))
            c[j] = (add(c[j][0], mul(point(digit), powers[j][0])),
                    add(c[j][1], mul(point(digit), powers[j][1])))
    vector = [c[0][0], c[1][0], c[0][1], c[1][1]]
    norm2 = total(square(x) for x in vector)
    assert residue == 0 and norm2[0] > 0
    return vector, norm2, [div(x, norm2) for x in vector]


def image(word, cell, beta):
    x = cell
    for digit in word: x = add(mul(beta, x), point(digit))
    return x


def inverse(matrix):
    n = len(matrix)
    A = [[v for v in row]+[point(int(i == j)) for j in range(n)] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(A[i][k][0]+A[i][k][1]))
        A[k], A[pivot] = A[pivot], A[k]
        denominator = A[k][k]
        assert denominator[0] > 0 or denominator[1] < 0
        for j in range(k+1, 2*n): A[k][j] = div(A[k][j], denominator)
        A[k][k] = point(1)
        for i in range(n):
            if i == k: continue
            factor = A[i][k]
            for j in range(k+1, 2*n): A[i][j] = sub(A[i][j], mul(factor, A[k][j]))
            A[i][k] = point(0)
    return [row[n:] for row in A]


def embeddings(beta, zs):
    stable = div(point(1), beta)
    rows = []
    for root in (beta, stable):
        row = [point(1)]
        for _ in range(5): row.append(mul(row[-1], root))
        rows.append(row)
    cp = []
    for z in zs:
        row = [(point(1), point(0))]
        for _ in range(5): row.append(cmul(row[-1], z))
        cp.append(row)
    rows.extend([[v[0] for v in row] for row in cp])
    rows.extend([[v[1] for v in row] for row in cp])
    return rows
