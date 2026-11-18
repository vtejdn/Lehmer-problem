"""Exact width-five exclusions and minimal-width controls for the two quartic seeds."""

import json
from fractions import Fraction
from math import gcd, isqrt, lcm
from pathlib import Path


SEEDS = {"A": (1, -1, -1, -1, 1), "B": (1, -2, 1, -2, 1)}
PRIME_LIMIT = 1009
OUTPUT = Path(__file__).resolve().parents[2] / "outputs" / "Yin_J_G0177" / "results.json"


def rational_kernel(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    pivots = []
    width = len(rows[0])
    for column in range(width):
        i = len(pivots)
        pivot = next((k for k in range(i, len(rows)) if rows[k][column]), None)
        if pivot is None:
            continue
        rows[i], rows[pivot] = rows[pivot], rows[i]
        factor = rows[i][column]
        rows[i] = [x / factor for x in rows[i]]
        for k in range(len(rows)):
            if k != i and rows[k][column]:
                factor = rows[k][column]
                rows[k] = [x - factor*y for x, y in zip(rows[k], rows[i])]
        pivots.append(column)
    basis = []
    for column in range(width):
        if column not in pivots:
            vector = [Fraction(j == column) for j in range(width)]
            for i, pivot in enumerate(pivots):
                vector[pivot] = -rows[i][column]
            basis.append(vector)
    return basis


def combine(u, a, v, b):
    return [a*x + b*y for x, y in zip(u, v)]


def bezout(a, b):
    r, s, t = a, 1, 0
    q, u, v = b, 0, 1
    while q:
        step = r // q
        r, s, t, q, u, v = q, u, v, r-step*q, s-step*u, t-step*v
    return (r, s, t) if r >= 0 else (-r, -s, -t)


def integral_kernel(matrix):
    basis = rational_kernel(matrix)
    if len(basis) == 1:
        u = basis[0]
        denominator = lcm(*(x.denominator for x in u))
        return [[int(denominator*x) for x in u]]
    if len(basis) != 2:
        raise ValueError("Expected a one- or two-dimensional eigenspace")
    u, v = basis
    # Free coordinates in the RREF basis must be integers.
    # Impose the remaining coordinate congruences one at a time.
    for j in range(len(u)):
        denominator = lcm(u[j].denominator, v[j].denominator)
        if denominator > 1:
            a, b = int(denominator*u[j]), int(denominator*v[j])
            g, s, t = bezout(a, b)
            index = denominator // gcd(g, denominator)
            u, v = combine(u, index*s, v, index*t), combine(u, b//g, v, -a//g)
    assert all(x.denominator == 1 for x in u + v)
    return [list(map(int, u)), list(map(int, v))]


def dot(u, v):
    return sum(x*y for x, y in zip(u, v))


def norm_one(u):
    return sum(map(abs, u))


def reduce_plane(u, v):
    while True:
        a, c = dot(u, u), dot(v, v)
        if c < a:
            u, v = v, u
            a = c
        b = dot(u, v)
        if 2*abs(b) <= a:
            return u, v
        multiple = (2*b + a) // (2*a)
        v = combine(v, 1, u, -multiple)


def short_vectors(plane, limit):
    """One sign per nonzero integral vector of one-norm at most limit."""
    u, v = plane
    a, b, c = dot(u, u), dot(u, v), dot(v, v)
    determinant = a*c - b*b
    for j in range(isqrt(limit*limit*a // determinant) + 1):
        radius = isqrt(a*limit*limit - determinant*j*j)
        left = -((b*j + radius) // a)
        right = (-b*j + radius) // a
        for i in range(left, right + 1):
            if j or i > 0:
                vector = combine(u, i, v, j)
                if norm_one(vector) <= limit:
                    yield vector


def row_system(seed, p, width):
    degree = len(seed)-1
    square = [sum(seed[j]*seed[i-j] for j in range(degree+1) if 0 <= i-j <= degree)
              for i in range(2*degree+1)]
    columns = {}
    wanted = {p*i + j for i in range(width+1) for j in (0, 1)}
    vector = [1] + [0]*(2*degree-1)
    for exponent in range(p*width+2):
        if exponent in wanted:
            columns[exponent] = vector
        vector = [x - vector[-1]*c for x, c in zip([0]+vector[:-1], square)]
    systems = []
    for sign in (1, -1):
        matrix = [[columns[p*i][j] + sign*columns[p*(width-i)+1][j]
                   for i in range(width+1)] for j in range(2*degree)]
        systems.append(integral_kernel(matrix))
    return columns, systems


def trimmed(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def coprime(u, v):
    a, b = trimmed(list(map(Fraction, u))), trimmed(list(map(Fraction, v)))
    while b:
        while len(a) >= len(b):
            factor, offset = a[-1]/b[-1], len(a)-len(b)
            for i, x in enumerate(b):
                a[offset+i] -= factor*x
            trimmed(a)
        a, b = b, a
    return len(a) == 1


def unequal_moduli(u, v):
    return any(dot(u[:len(u)-k], u[k:]) != dot(v[:len(v)-k], v[k:])
               for k in range(len(u)))


def certify_graph(columns, p, u, v):
    assert all(sum(columns[p*i][j]*u[i] + columns[p*i+1][j]*v[i]
                   for i in range(len(u))) == 0 for j in range(len(columns[0])))
    assert unequal_moduli(u, v) and coprime(u, v)


def mixed_rows(plus, minus):
    u = [(a+b)//2 for a, b in zip(plus, minus)]
    v = [(a-b)//2 for a, b in zip(plus, minus)][::-1]
    return u, v


def minimum_at_four(seed, p):
    columns, ((a,), (b,)) = row_system(seed, p, 4)
    if not a[0]*b[-1] + a[-1]*b[0]:
        return {"cost": None, "primitive_lines": [a, b]}
    scale = 1 if all((x-y) % 2 == 0 for x, y in zip(a, b)) else 2
    u, v = mixed_rows([scale*x for x in a], [scale*y for y in b])
    certify_graph(columns, p, u, v)
    return {"cost": max(norm_one(u), norm_one(v)), "rows": [u, v]}


def search(planes, columns, p, height):
    if max(dot(u, u) for u, _ in planes) > (2*height)**2:
        return None, None
    positive, negative = [list(short_vectors(plane, 2*height)) for plane in planes]
    best = None
    for a in positive:
        for b in negative:
            if any((x-y) % 2 for x, y in zip(a, b)):
                continue
            u, v = mixed_rows(a, b)
            if not any(u) or not any(v):
                continue
            while u[0] == v[0] == 0:
                u, v = u[1:] + [0], v[1:] + [0]
            cost = max(norm_one(u), norm_one(v))
            if cost <= height and (best is None or cost < best["cost"]):
                if unequal_moduli(u, v) and coprime(u, v):
                    certify_graph(columns, p, u, v)
                    best = {"cost": cost, "rows": [u, v]}
    return best, [len(positive), len(negative)]


def main():
    records = []
    for p in range(3, PRIME_LIMIT+1, 2):
        if any(p % factor == 0 for factor in range(3, isqrt(p)+1, 2)):
            continue
        for name, seed in SEEDS.items():
            columns, kernels = row_system(seed, p, 5)
            planes = [reduce_plane(*kernel) for kernel in kernels]
            result, counts = search(planes, columns, p, 2**p)
            record = {"prime": p, "seed": name, "cutoff_witness": result,
                      "shortest_squared": [dot(u, u) for u, _ in planes],
                      "enumerated_counts": counts}
            if p in (3, 5, 7):
                record["width_four"] = minimum_at_four(seed, p)
                height = 2**p
                while result is None:
                    height *= 2
                    result, _ = search(planes, columns, p, height)
                record["width_five_uncapped"] = result
            records.append(record)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    print(f"{len(records)} seed/prime cases; "
          f"{sum(r['cutoff_witness'] is not None for r in records)} pass the cutoff.")
    print(f"{sum(r['enumerated_counts'] is None for r in records)} excluded by squared lengths.")


if __name__ == "__main__":
    main()
