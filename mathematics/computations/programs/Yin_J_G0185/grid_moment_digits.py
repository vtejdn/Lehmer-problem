"""Sieve degrees using the first integer coefficients of a cosine grid."""

from argparse import ArgumentParser
from math import comb

from lobatto_digits import combine, local_lift


def moment_kernel(modulus, endpoint_power, depth):
    """Return M^j [z^j] (1-z^2) / ((1-(2+1/M)z+z^2) V)."""
    grid = [0] * (2 * endpoint_power + 1)
    for j in range(endpoint_power + 1):
        grid[2 * j] = (-1)**j * comb(endpoint_power, j)
    denominator = [0] * (len(grid) + 2)
    for j, coefficient in enumerate(grid):
        denominator[j] += coefficient * modulus**j
        denominator[j + 1] -= (2 * modulus + 1) * coefficient * modulus**j
        denominator[j + 2] += coefficient * modulus**(j + 2)
    kernel = []
    for j in range(depth + 1):
        numerator = 1 if j == 0 else -modulus**2 if j == 2 else 0
        correction = sum(denominator[i] * kernel[j-i]
                         for i in range(1, min(j+1, len(denominator))))
        kernel.append(numerator - correction)
    return kernel


def census(q, endpoint_power, minimum_n, maximum_n, depth, perturbed=False):
    if q < 2 or q % 4 not in (0, 3):
        raise ValueError("The local lift requires a multiple of four in q, q+1")
    if not 1 <= depth or minimum_n < 2*depth+2 or maximum_n < minimum_n:
        raise ValueError("Require 2*depth+2 <= minimum_n <= maximum_n")
    if perturbed and (q != 40 or depth > 10 or minimum_n < 23):
        raise ValueError("Perturbation bounds require q=40, depth<=10, n>=23")
    modulus = q * (q + 1)
    norm = (2*q + 1)**2
    powers = [modulus**i for i in range(depth+1)]
    kernel = moment_kernel(modulus, endpoint_power, depth)
    states = [(0, (1,))]
    counts = []
    for j in range(1, depth + 1):
        place = powers[j]
        period = powers[j-1]
        new_states = []
        represented = 0
        for degree, prefix in states:
            base = sum(c * powers[i] * kernel[j-i] for i, c in enumerate(prefix))
            first_digit = (-2*place - base) // place + 1
            last_digit = first_digit + 3
            if perturbed:
                first_digit = -((9*place + 4*base) // (4*place))
                last_digit = (9*place - 4*base) // (4*place)
            a, b = local_lift(q, degree, period, prefix, norm)
            c, d = local_lift(-q-1, degree, period, prefix, norm)
            offset, slope = combine(a, c, q), combine(b, d, q)
            for digit in range(first_digit, last_digit + 1):
                residue = degree + period * ((offset + slope * digit) % modulus)
                if residue % 2:
                    continue
                first = 2*minimum_n + (residue - 2*minimum_n) % place
                if first <= 2*maximum_n:
                    new_states.append((residue, (*prefix, digit)))
                    represented += 1 + (2*maximum_n-first) // place
        states = new_states
        counts.append((len(states), represented))
        if not states:
            break
    return counts


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--q", type=int, default=40)
    parser.add_argument("--endpoint-power", type=int, choices=(1, 2), required=True)
    parser.add_argument("--min-n", type=int, default=23)
    parser.add_argument("--max-n", type=int, default=10**24)
    parser.add_argument("--depth", type=int, default=10)
    parser.add_argument("--perturbed", action="store_true")
    args = parser.parse_args()
    rows = census(args.q, args.endpoint_power, args.min_n, args.max_n, args.depth,
                  args.perturbed)
    for j, (prefixes, degrees) in enumerate(rows, 1):
        print(f"depth={j} prefixes={prefixes} degrees={degrees}")
