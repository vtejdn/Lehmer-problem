"""Screen odd-prime parameters using the degree and height bounds for H_p."""

from argparse import ArgumentParser
from math import isqrt


def multiply(left, right):
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] += a * b
    return product


def remainder(dividend, monic_divisor):
    coefficients = dividend.copy()
    while len(coefficients) >= len(monic_divisor):
        shift = len(coefficients) - len(monic_divisor)
        leading = coefficients[-1]
        for j, value in enumerate(monic_divisor):
            coefficients[shift + j] -= leading * value
        coefficients.pop()
    return coefficients


def square_layer(prime):
    def cyclotomic_quotient(stride):
        coefficients = [0] * (stride * (prime - 1) + 1)
        for j in range(prime):
            coefficients[stride * j] = (-1) ** j
        return coefficients

    phi_4p = cyclotomic_quotient(2)
    a = multiply([-1, 1], cyclotomic_quotient(4))
    b = multiply([1, 1], multiply(phi_4p, phi_4p))
    twice_h = [x + y for x, y in zip(multiply(a, a), multiply(b, b), strict=True)]
    assert all(c % 2 == 0 for c in twice_h)
    return [c // 2 for c in twice_h]


def check_small_blocks():
    assert remainder(square_layer(3), [1, 1, 1]) == [2, 0]
    # In ascending coefficient order, these lift the two irreducible cubics of Phi_7.
    lifts = ([3, 2, 3, 1], [3, 1, 2, 1])
    assert [c % 4 for c in multiply(*lifts)] == [1] * 7
    h7 = square_layer(7)
    for lifted in lifts:
        assert [c % 4 for c in remainder(h7, lifted)] == [2, 2, 0]
    print("calibration: H_3 mod Phi_3 = 2; H_7 mod (4, each lifted cubic) = 2+2x")


def is_prime(number):
    return number >= 2 and all(number % d for d in range(2, isqrt(number) + 1))


def order_of_two(prime):
    residue = 2
    order = 1
    while residue != 1:
        residue = 2 * residue % prime
        order += 1
    return order


def candidate_degrees(prime, block_size):
    # The sufficient height target is M(f) < 2^(7/30).
    # P16 gives M(f) <= 2^(9e/(2p-10)).
    maximum_degree = (7 * (2 * prime - 10) - 1) // 270
    return [
        degree
        for base in range(block_size, maximum_degree + 1, block_size)
        for degree in (base, base + 2)
        if degree <= maximum_degree
    ]


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--max-prime", type=int, default=8191)
    options = parser.parse_args()
    check_small_blocks()
    for prime in range(7, options.max_prime + 1, 2):
        if not is_prime(prime):
            continue
        order = order_of_two(prime)
        # Degree bounds before the mod-4 argument, including the square mod 2.
        before = candidate_degrees(prime, 2 * order)
        # All eight copies of each mod-2 primitive block belong together.
        # Reciprocity pairs distinct inverse orbits if the order is odd.
        block_size = (16 if order % 2 else 8) * order
        after = candidate_degrees(prime, block_size)
        if prime == 2113 or after:
            print(f"p={prime}, ord={order}, earlier={before}, screened={after}")


if __name__ == "__main__":
    main()
