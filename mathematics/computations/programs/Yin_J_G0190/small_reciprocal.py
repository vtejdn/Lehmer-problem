"""Enumerate small-degree reciprocal minima using exact Newton sums and trace signatures."""

from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import sys


PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0188"))
from radial_cores import compare_measure, signature, trace_from_half


CUTOFF = Fraction(53, 40)
LAST_POWER = 32
EXPECTED_COUNTS = {
    2: (5, 5, 0, 0),
    4: (41, 19, 0, 0),
    6: (373, 59, 0, 0),
    8: (3931, 185, 20, 2),
    10: (44485, 621, 102, 16),
    12: (530345, 2383, 450, 22),
}


def monic_quotient(polynomial, divisor):
    """Return the quotient in ascending order if a monic polynomial divides."""
    row = list(polynomial)
    degree = len(divisor) - 1
    if len(row) <= degree:
        return None
    quotient = [0] * (len(row) - degree)
    for shift in reversed(range(len(quotient))):
        coefficient = row[shift + degree]
        quotient[shift] = coefficient
        if coefficient:
            for i, value in enumerate(divisor):
                row[shift + i] -= coefficient * value
    return tuple(quotient) if not any(row) else None


def small_cyclotomics(degree):
    # phi(q) >= sqrt(q/2): at each odd prime factor phi(p^e)^2 >= p^e,
    # and the only local factor below one in phi(q)^2/q is 1/2 at 2^1.
    by_order = {}
    for q in range(1, 2 * degree**2 + 1):
        phi = sum(gcd(j, q) == 1 for j in range(1, q + 1))
        if phi > degree:
            continue
        row = (-1,) + (0,) * (q - 1) + (1,)
        for divisor, factor in by_order.items():
            if q % divisor == 0:
                row = monic_quotient(row, factor)
                if row is None:
                    raise ArithmeticError("Cyclotomic recurrence failed.")
        if len(row) != 1 + phi:
            raise ArithmeticError("Unexpected cyclotomic degree.")
        by_order[q] = row
    return tuple(by_order.values())


def power_limits(degree):
    result = [0]
    for j in range(1, LAST_POWER + 1):
        bound = degree - 2 + CUTOFF**j + (1 / CUTOFF)**j
        result.append(bound.numerator // bound.denominator)
    return result


def reciprocal_candidates(degree, limits):
    """Construct the leading half by Newton's triangular identities."""
    half_degree = degree // 2

    def extend(coefficients, sums):
        j = len(coefficients)
        if j > half_degree:
            yield tuple(coefficients + coefficients[-2::-1]), sums
            return
        known = sum(coefficients[i] * sums[j - i] for i in range(1, j))
        lo = -((known + limits[j]) // j)
        hi = (limits[j] - known) // j
        for coefficient in range(lo, hi + 1):
            value = -j * coefficient - known
            yield from extend(coefficients + [coefficient], sums + [value])

    yield from extend([1], [degree])


def passes_remaining_powers(polynomial, first, limits):
    d = len(polynomial) - 1
    sums = first.copy()
    for j in range(len(sums), len(limits)):
        value = -sum(polynomial[i] * sums[j - i] for i in range(1, min(j - 1, d) + 1))
        if j <= d:
            value -= j * polynomial[j]
        if abs(value) > limits[j]:
            return False
        sums.append(value)
    return True


def main():
    for d in range(2, 13, 2):
        limits = power_limits(d)
        cyclotomics = small_cyclotomics(d)
        counts = Counter()
        survivors = []
        for polynomial, sums in reciprocal_candidates(d, limits):
            counts["generated"] += 1
            if not passes_remaining_powers(polynomial, sums, limits):
                continue
            counts["power"] += 1
            if any(monic_quotient(polynomial, factor) is not None for factor in cyclotomics):
                continue
            counts["no cyclotomic"] += 1
            measure_side, _ = compare_measure(polynomial, CUTOFF)
            if measure_side > 0:
                continue
            counts["below"] += 1
            trace = trace_from_half(polynomial[:d // 2 + 1])
            _, (_, inside, _, _) = signature(trace)
            counts[("neutral", inside)] += 1
            if inside <= 1:
                survivors.append(polynomial)
        print(d, dict(counts), "at most one neutral pair:", survivors)
        observed = tuple(counts[key] for key in ("generated", "power", "no cyclotomic", "below"))
        if observed != EXPECTED_COUNTS[d]:
            raise ArithmeticError(f"Unexpected counts in degree {d}: {observed}")
        if survivors:
            raise ArithmeticError("A small candidate with at most one neutral pair remains.")


if __name__ == "__main__":
    main()
