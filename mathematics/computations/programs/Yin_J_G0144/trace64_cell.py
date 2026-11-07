"""Exact certificate and input data for the degree-64 one-pair cell."""

import argparse
from fractions import Fraction
import json
from math import comb

from trace_control import SOURCE_HALF, ellipse


N = 32
SEPARATORS = (-2000, -1978, -1925, -1837, -1717, -1566, -1467, -1371,
              -1184, -959, -809, -685, -463, -290, -157, 67, 263, 394,
              591, 840, 1008, 1120, 1288, 1480, 1612, 1688, 1781, 1885,
              1956, 1988, 2000)
# c=(U+iV)/D, radius=R/D.
U, V, R, D = -177624, 8300, 10, 100000
RHO = Fraction(219, 200)


def chebyshev_basis():
    """Return the monomial coefficient lists of 1,C_1,...,C_N."""
    powers = [[2], [0, 1]]
    for _ in range(2, N + 1):
        poly = [0] + powers[-1]
        for j, value in enumerate(powers[-2]):
            poly[j] -= value
        powers.append(poly)
    powers[0] = [1]
    return powers


def seed_vector():
    """Free coefficients center first, followed by C_1,...,C_31; C_32 is fixed."""
    control = SOURCE_HALF + SOURCE_HALF[-2::-1]
    full = [sum(control[j] for j in range(len(control)) if 0 <= k-j < 47)
            for k in range(2*N + 1)]
    assert full == full[::-1] and max(map(abs, full)) == 3 and full[0] == 1
    return full[N:0:-1]


def signed_rows():
    """Sign-normalized integer coefficient rows, all to be strictly positive."""
    rows = []
    for index, numerator in enumerate(SEPARATORS):
        x = Fraction(numerator, 1000)
        values = [Fraction(2), x]
        for _ in range(2, N + 1):
            values.append(x * values[-1] - values[-2])
        values[0] = Fraction(1)
        scale = (-1)**index * x.denominator**N
        rows.append([int(value * scale) for value in values])
    return rows


def disk_rows():
    """Each (real,imaginary) row pair gives [s^k] D^N Q(c+rs)."""
    powers = [(1, 0)]
    for _ in range(N):
        a, b = powers[-1]
        powers.append((U*a - V*b, V*a + U*b))
    basis = chebyshev_basis()
    rows = []
    for k in range(N + 1):
        reals, imags = [], []
        for polynomial in basis:
            real = imag = 0
            for m in range(k, len(polynomial)):
                factor = polynomial[m] * comb(m, k) * R**k * D**(N-m)
                a, b = powers[m-k]
                real += factor*a
                imag += factor*b
            reals.append(real)
            imags.append(imag)
        rows.append((reals, imags))
    return rows


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def directional_model(signs, disks, direction):
    """Each row represents sum(terms[var]*var) >= rhs, with integral entries."""
    columns = [f"x{j}" for j in range(N)]
    auxiliaries = []
    rows = []

    def add_row(row, auxiliary_terms, margin):
        terms = {name: value for name, value in zip(columns, row[:-1]) if value}
        terms.update(auxiliary_terms)
        rows.append(dict(terms=terms, rhs=margin-row[-1]))

    # Strict signs are exactly at least one after integer scaling.
    for row in signs:
        add_row(row, {}, 1)
    for k, pair in enumerate(disks):
        if k == 1:
            continue
        for axis, row in zip(("r","i"), pair):
            name = f"abs_{k}{axis}"
            auxiliaries.append(name)
            add_row(row, {name: 1}, 0)
            add_row([-v for v in row], {name: 1}, 0)
    orientation = {"pos-real": (0,1), "neg-real": (0,-1),
                   "pos-imag": (1,1), "neg-imag": (1,-1)}
    axis, sign = orientation[direction]
    # With integer free variables all Taylor components are scaled integers.
    # Taking auxiliaries at their smallest allowed values makes strictness a unit.
    add_row([sign*v for v in disks[1][axis]], {a: -1 for a in auxiliaries}, 1)
    return dict(integers={x: [-3,3] for x in columns}, continuous_nonnegative=auxiliaries,
                direction=direction, rows_ge=rows)


def certificate(free, signs, disks):
    """Every returned success is a rational proof of 1<M<(219/200)^2."""
    if len(free) != N or any(type(a) is not int or abs(a) > 3 for a in free):
        return False, "coefficient box"
    full = list(free) + [1]
    if min(dot(row, full) for row in signs) <= 0:
        return False, "real brackets"
    shifted = [(dot(real, full), dot(imag, full)) for real, imag in disks]
    error = sum(abs(a) + abs(b) for k, (a, b) in enumerate(shifted) if k != 1)
    if error >= max(map(abs, shifted[1])):
        return False, "disk"
    if not (V > R and ellipse(Fraction(abs(U)+R, D), Fraction(V+R, D), RHO) < 1):
        return False, "ellipse"
    return True, "strict sign, disk and ellipse"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", choices=["pos-real","neg-real","pos-imag","neg-imag"],
                        help="Print one complete exact directional formulation as JSON.")
    args = parser.parse_args()
    signs, disks = signed_rows(), disk_rows()
    seed = seed_vector()
    assert all(dot(row, seed + [1]) > 0 for row in signs)
    assert certificate(seed, signs, disks) == (False, "disk")
    assert len(SEPARATORS) == N-1 and all(a < b for a,b in zip(SEPARATORS, SEPARATORS[1:]))
    assert ellipse(Fraction(abs(U)+R, D), Fraction(V+R, D), RHO) < Fraction(992, 1000)
    if args.model:
        print(json.dumps(directional_model(signs, disks, args.model), separators=(",",":")))
    else:
        print("All 31 seed signs verified; the seed fails the target disk.")
