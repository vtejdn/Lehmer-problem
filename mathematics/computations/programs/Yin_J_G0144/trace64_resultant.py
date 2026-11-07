"""Bound the integer resultant with the degree-nine control on two degree-64 cells."""

from fractions import Fraction
from math import comb, prod

from trace_control import TRACE


# Each entry is the left endpoint numerator of a sign-changing interval.
MILLION = 10**6
SEED_LEFT = (
    -1995534, -1959924, -1889339, -1785038, -1648884, -1483305,
    -1451338, -1291256, -1076165, -841870, -776741, -592552,
    -332659, -248046, -66830, 200191, 324974, 463640, 718815,
    961163, 1054226, 1186359, 1390384, 1569598, 1655361,
    1720803, 1841299, 1928938, 1982154, 1994041,
)
JET = tuple(tuple(TRACE[j] * comb(j, k) for j in range(k, len(TRACE)))
            for k in range(len(TRACE)))


def evaluate(polynomial, x):
    value = 0
    for coefficient in reversed(polynomial):
        value = x * value + coefficient
    return value


def psi47(x):
    previous, current = 2, x
    total = 1
    for _ in range(23):
        total += current
        previous, current = current, x * current - previous
    return total


def seed_brackets():
    bounds = [(Fraction(a, MILLION), Fraction(a + 1, MILLION)) for a in SEED_LEFT]
    assert all(upper < lower for (_, upper), (lower, _) in zip(bounds, bounds[1:]))
    assert -2 < bounds[0][0] and bounds[-1][1] < 2
    original = []
    for lower, upper in bounds:
        original.append(evaluate(TRACE, lower) * evaluate(TRACE, upper) < 0)
        cyclotomic = psi47(lower) * psi47(upper) < 0
        assert original[-1] != cyclotomic
    assert len(bounds) == 30 and sum(original) == 7
    return bounds, original


def binary_irreducibility():
    modulus = sum((coefficient % 2) << j for j, coefficient in enumerate(TRACE))
    assert modulus.bit_length() == 10
    for divisor in range(2, 32):  # Every monic polynomial of degree one through four.
        remainder = modulus
        while remainder.bit_length() >= divisor.bit_length():
            remainder ^= divisor << (remainder.bit_length() - divisor.bit_length())
        assert remainder != 0


def evaluate_gaussian(polynomial, center):
    a, b = center
    real, imag = 0, 0
    for coefficient in reversed(polynomial):
        real, imag = real * a - imag * b + coefficient, real * b + imag * a
    return real, imag


def disk_bound():
    center = (Fraction(-177624, 100000), Fraction(8300, 100000))
    radius = Fraction(1, 10000)
    real, imag = evaluate_gaussian(TRACE, center)
    assert real**2 + imag**2 < Fraction(19, 1000)**2
    tail = 0
    for k, polynomial in enumerate(JET[1:], 1):
        real, imag = evaluate_gaussian(polynomial, center)
        tail += (abs(real) + abs(imag)) * radius**k
    assert tail < Fraction(1, 1000)


def max_on_interval(left, right):
    pieces = 16
    half = (right - left) / (2 * pieces)
    assert half > 0
    bounds = []
    for index in range(pieces):
        center = left + (2 * index + 1) * half
        bounds.append(sum(abs(evaluate(p, center)) * half**k for k, p in enumerate(JET)))
    return max(bounds)


def main():
    binary_irreducibility()
    disk_bound()
    bounds, original = seed_brackets()
    lower = [Fraction(-2)] + [a for a, _ in bounds] + [Fraction(2)]
    upper = [Fraction(-2)] + [b for _, b in bounds] + [Fraction(2)]
    quarters = []
    midpoints = []
    possible_moves = []
    tolerance = Fraction(1, 1000)
    displacement = Fraction(1, 50)
    for i in range(1, len(bounds) + 1):
        quarters.append(max_on_interval((3 * lower[i] + lower[i - 1]) / 4,
                                        (3 * upper[i] + upper[i + 1]) / 4))
        left = (lower[i - 1] + lower[i]) / 2 - tolerance if i > 1 else Fraction(-2)
        right = (upper[i] + upper[i + 1]) / 2 + tolerance if i < len(bounds) else Fraction(2)
        if original[i - 1]:
            latest_left = (upper[i - 1] + upper[i]) / 2 + tolerance if i > 1 else Fraction(-2)
            earliest_right = (lower[i] + lower[i + 1]) / 2 - tolerance if i < len(bounds) else Fraction(2)
            if left < upper[i] - displacement:
                possible_moves.append((i, "left"))
                test_point = upper[i] - displacement
                assert latest_left < test_point < earliest_right and test_point.denominator > 1
            if right > lower[i] + displacement:
                possible_moves.append((i, "right"))
                test_point = lower[i] + displacement
                assert latest_left < test_point < earliest_right and test_point.denominator > 1
            left = max(left, lower[i] - displacement)
            right = min(right, upper[i] + displacement)
        midpoints.append(max_on_interval(left, right))
    assert prod(quarters) < 1000
    assert prod(midpoints) < 2400
    assert possible_moves == [(7, "right")] + [
        (i, side) for i in (11, 14, 17, 21, 25) for side in ("left", "right")
    ]
    print("Verified both bounds for the product of 30 real evaluations: <1000 and <2400.")
    print("The two disk evaluations contribute <1/2500. Both resultants must vanish.")
    print("The necessary displacement has eleven possible directions and indices.")


if __name__ == "__main__":
    main()
