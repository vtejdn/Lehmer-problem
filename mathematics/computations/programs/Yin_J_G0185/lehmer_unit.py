"""Test the degree-ten Lehmer unit in every consecutive-coefficient section."""

from fractions import Fraction
from math import comb


# Coefficients in order of increasing exponent.
LEHMER = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1)
LOWER = Fraction(117628, 100000)
UPPER = Fraction(117629, 100000)


def value(point):
    acc = 0
    for coefficient in reversed(LEHMER):
        acc = acc * point + coefficient
    return acc


def check_real_root():
    shifted = [
        sum(LEHMER[i] * comb(i, j) for i in range(j, len(LEHMER)))
        for j in range(len(LEHMER))
    ]
    assert shifted[:2] == [-1, -5] and all(c > 0 for c in shifted[2:])
    assert 1 < LOWER < UPPER and value(LOWER) < 0 < value(UPPER)


def enumerate_exponents():
    candidates = []
    short = 1
    while True:
        lower_power = LOWER**short
        upper_power = UPPER**short
        bound = 2 * lower_power / (lower_power - 1) ** 2
        max_q = bound.numerator // bound.denominator
        if max_q == 0:
            break
        row = []
        for q in range(1, max_q + 1):
            low_difference = q * lower_power - (q + 1)
            high_difference = q * upper_power - (q + 1)
            assert low_difference * high_difference > 0
            sign = 1 if low_difference > 0 else -1
            denominator = min(abs(low_difference), abs(high_difference))
            upper_ratio = ((q + 1) * upper_power - q) / denominator
            long = short + 1
            while LOWER**long <= upper_ratio:
                row.append((q, short, long, sign))
                long += 1
        print(short, max_q, len(row), max((v for _, _, v, _ in row), default="-"))
        candidates.extend(row)
        short += 1
    return candidates


def power_remainders(max_exponent):
    degree = len(LEHMER) - 1
    powers = [(1,) + (0,) * (degree - 1)]
    for _ in range(max_exponent):
        old = powers[-1]
        shifted = (0,) + old[:-1]
        powers.append(tuple(shifted[i] - old[-1] * LEHMER[i] for i in range(degree)))
    return powers


def main():
    check_real_root()
    print("U  maximum q  candidates  maximum V")
    candidates = enumerate_exponents()
    powers = power_remainders(max(31, max(u + v for _, u, v, _ in candidates)))
    assert all((a - b) % 2 == 0 for a, b in zip(powers[31], powers[0]))
    assert value(1) % 2
    for q, u, v, sign in candidates:
        remainder = [
            q * (a + sign * d) - (q + 1) * (b + sign * c)
            for a, b, c, d in zip(powers[0], powers[u], powers[v], powers[u + v])
        ]
        assert any(remainder), (q, u, v, sign)
        index = v - u if q % 2 == 0 else v + u
        assert 0 < index < 31, (q, u, v, index)
    print(f"{len(candidates)} nonzero integer remainders; every binary index is below 31.")


if __name__ == "__main__":
    main()
