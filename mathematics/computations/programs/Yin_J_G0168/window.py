"""Compute the powered-order index and exponent throughout Lehmer's prime window."""

import csv
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb, gcd, isqrt, lcm
from pathlib import Path
from tempfile import TemporaryDirectory


GROUP = Path(__file__).resolve().parent
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "window.csv"
sys.path.insert(0, str(GROUP.parent / "Yin_J_G0167" / "checks"))
from maximal_minors import maximal_minors, monomial_remainder


# Coefficients from the constant through degree nine of the monic input.
LEHMER = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1)


def prime_window():
    """Certify the ceiling with outward bounds and enumerate by trial division."""
    log_value = Decimal(3 * len(LEHMER)).ln()
    lower = Fraction(log_value.next_minus()) ** 4
    upper = Fraction(log_value.next_plus()) ** 4
    start = -(-lower.numerator // lower.denominator)
    if upper > start:
        raise ArithmeticError("The window ceiling is undecided")
    return [p for p in range(start + 1, 2 * start + 1)
            if all(p % i for i in range(2, isqrt(p) + 1))]


def powers_through(last):
    """Multiply each remainder by x and reduce its leading term."""
    previous = (1,) + (0,) * (len(LEHMER) - 1)
    powers = [previous]
    for _ in range(last):
        shifted = (0,) + previous[:-1]
        previous = tuple(x - previous[-1] * c for x, c in zip(shifted, LEHMER))
        powers.append(previous)
    return powers


def lattice_invariants(columns, next_power):
    """Reduce [M | 1 | beta^d] to recover the inverse and the power relation."""
    degree = len(columns)
    matrix = [[Fraction(c[i]) for c in columns]
              + [Fraction(i == j) for j in range(degree)]
              + [Fraction(next_power[i])] for i in range(degree)]
    determinant = Fraction(1)
    for j in range(degree):
        pivot_row = next((i for i in range(j, degree) if matrix[i][j]), None)
        if pivot_row is None:
            raise ArithmeticError("Powering loses degree")
        if pivot_row != j:
            matrix[j], matrix[pivot_row] = matrix[pivot_row], matrix[j]
            determinant = -determinant
        pivot = matrix[j][j]
        determinant *= pivot
        matrix[j] = [value / pivot for value in matrix[j]]
        for i, row in enumerate(matrix):
            if i != j and row[j]:
                multiple = row[j]
                matrix[i] = [x - multiple * y for x, y in zip(row, matrix[j])]
    if determinant.denominator != 1:
        raise ArithmeticError("Nonintegral determinant")
    exponent = lcm(*(x.denominator for row in matrix for x in row[degree:-1]))
    if any(row[-1].denominator != 1 for row in matrix):
        raise ArithmeticError("Nonintegral powered minimal polynomial")
    polynomial = [-row[-1].numerator for row in matrix] + [1]
    return abs(determinant.numerator), exponent, polynomial


def check_minors(p, index, exponent):
    """Rebuild all columns by long division and expand the minors over Z."""
    columns = [monomial_remainder(j * p) for j in range(len(LEHMER))]
    determinant, = maximal_minors(columns)
    divisor = 0
    for j in range(len(columns)):
        minors = maximal_minors(columns[:j] + columns[j + 1:])
        divisor = gcd(divisor, *minors)
    if abs(determinant) != index or divisor * exponent != index:
        raise ArithmeticError(f"Determinantal divisors disagree at {p}")


def norm_in_order(polynomial, element):
    """Compute the norm of an element of Z[X]/(monic polynomial)."""
    degree = len(polynomial) - 1
    column = list(element) + [0] * (degree - len(element))
    columns = [column]
    for _ in range(1, degree):
        lead = column[-1]
        column = [x - lead * c for x, c in zip([0] + column[:-1], polynomial)]
        columns.append(column)
    determinant, = maximal_minors(columns)
    return abs(determinant)


def clean_index(p, index, polynomial, discriminant):
    """Remove full prime powers at bad reduction and possible triple roots."""
    first = [j * a for j, a in enumerate(polynomial) if j >= 1]
    second = [comb(j, 2) * a for j, a in enumerate(polynomial) if j >= 2]
    obstruction = gcd(index, norm_in_order(polynomial, second))
    if obstruction > 1:
        mixed = first.copy()
        for j, a in enumerate(second):
            mixed[j] += a
        obstruction = gcd(obstruction, norm_in_order(polynomial, mixed))
    bad = p * discriminant * obstruction
    clean = index
    while (overlap := gcd(clean, bad)) > 1:
        clean //= overlap
    return clean, obstruction


def log_bounds(value):
    """Rational bounds using neighbors of the correctly rounded decimal log."""
    estimate = Decimal(value).ln()
    return Fraction(estimate.next_minus()), Fraction(estimate.next_plus())


def certified_extrema(intervals):
    """Identify the uniquely least and greatest entries by disjoint intervals."""
    lowest = min(intervals, key=lambda p: intervals[p][0])
    highest = max(intervals, key=lambda p: intervals[p][1])
    if any(intervals[lowest][1] >= limits[0] for p, limits in intervals.items() if p != lowest):
        raise ArithmeticError("Minimum not separated")
    if any(intervals[highest][0] <= limits[1] for p, limits in intervals.items() if p != highest):
        raise ArithmeticError("Maximum not separated")
    return lowest, highest


def main():
    with localcontext() as context:
        context.prec = 50
        primes = prime_window()
        powers = powers_through(len(LEHMER) * max(primes))
        input_polynomial = [*LEHMER, 1]
        derivative = [j * a for j, a in enumerate(input_polynomial) if j >= 1]
        discriminant = norm_in_order(input_polynomial, derivative)
        rows = []
        rates = {}
        concentrations = {}
        cofactor_bounds = {}
        for p in primes:
            columns = [powers[j * p] for j in range(len(LEHMER))]
            index, exponent, polynomial = lattice_invariants(columns, powers[len(LEHMER) * p])
            check_minors(p, index, exponent)
            clean, obstruction = clean_index(p, index, polynomial, discriminant)
            if clean != index or gcd(discriminant, p) != 1:
                raise ArithmeticError(f"Isolated-pair and support-prime bounds fail at {p}")
            log_index, log_exponent = Decimal(index).ln(), Decimal(exponent).ln()
            rate = log_exponent / p
            baseline = 2 * log_index / (len(LEHMER) * p)
            index_lo, index_hi = log_bounds(index)
            exp_lo, exp_hi = log_bounds(exponent)
            rates[p] = (exp_lo / p, exp_hi / p)
            concentrations[p] = (5 * exp_lo / index_hi, 5 * exp_hi / index_lo)
            pair_and_support = 4 * index_lo + 10 * log_bounds(p)[0]
            cofactor_bounds[p] = (Fraction(p - 4, 321 * p) * pair_and_support
                                  - 2 * log_bounds("1.2")[1]
                                  - Fraction(2, p) * log_bounds(322 * p)[1])
            rows.append((p, exponent, index, rate, baseline, rate / baseline, clean, obstruction))
        low_rate, high_rate = certified_extrema(rates)
        low_conc, high_conc = certified_extrema(concentrations)
        if min(cofactor_bounds.values()) <= Fraction(187, 100) or cofactor_bounds[263] <= Fraction(437, 100):
            raise ArithmeticError("Cofactor floor not attained")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    scratch_root = GROUP.parents[3] / ".tmp"
    scratch_root.mkdir(exist_ok=True)
    with TemporaryDirectory(dir=scratch_root, prefix="j168-window-") as directory:
        pending = Path(directory) / OUTPUT.name
        with pending.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(("p", "exponent", "index", "log_exponent_per_p",
                             "twice_log_index_per_dp", "concentration", "clean_index",
                             "possible_triple_divisor"))
            writer.writerows(rows)
        pending.replace(OUTPUT)
    print(f"{len(rows)} primes, with indices and exponents checked by minors.")
    print(f"Results: {OUTPUT}")
    print(f"Absolute discriminant {discriminant}. Full cleaned indices: "
          f"{sum(row[2] == row[6] for row in rows)}/{len(rows)}")
    for index, label, lowest, highest in [(3, "log(s)/p", low_rate, high_rate),
                                         (5, "concentration", low_conc, high_conc)]:
        for end, prime in [("min", lowest), ("max", highest)]:
            row = next(row for row in rows if row[0] == prime)
            print(f"{end} {label}: p={prime}, {row[index]:.15f}")
    print("Cofactor measure exceeds 1.87 throughout and 4.37 at p=263.")


if __name__ == "__main__":
    main()
