"""Sieve reciprocal degrees using the two congruences at a rational pole."""

from argparse import ArgumentParser


def local_lift(base, degree, period, coefficients, pole_norm):
    """Return the affine lift h = offset + slope * next_coefficient (mod |base|)."""
    radix = abs(base)
    depth = len(coefficients)
    place = radix**depth
    modulus = place * radix
    unit = 1 + base
    ratio = base * pow(unit, -1, modulus) % modulus
    prefix = 0
    for coefficient in reversed(coefficients):
        prefix = (prefix * ratio + coefficient) % modulus
    unit_power = pow(unit, degree, modulus)
    value = unit_power * prefix % modulus
    offset, remainder = divmod(pole_norm - value, place)
    if remainder:
        raise ArithmeticError("Invalid prefix congruence")
    lift_unit, remainder = divmod(pow(unit, period, modulus) - 1, place)
    if remainder:
        raise ArithmeticError("Invalid period")
    inverse_step = pow(value * lift_unit, -1, radix)
    digit_step = unit_power * pow(ratio, depth, modulus) // place
    return offset * inverse_step % radix, -digit_step * inverse_step % radix


def combine(left, right, q):
    """Chinese remainder modulo q and q+1, using q = -1 mod q+1."""
    return left + q * ((left - right) % (q + 1))


def digits(prefix, perturbed):
    depth = len(prefix)
    if perturbed:
        if depth == 1:
            return range(-4, 1)
        return range(-9, 8) if depth == 2 else range(-8, 9)
    if depth == 1:
        return range(-4, 0)
    mean = -2 * prefix[1]
    shift = 1 if depth == 2 else 0
    return range(1 - mean - shift, mean - shift)


def sieve(q, minimum_n, maximum_n, depth_limit, perturbed=False):
    if q < 5 or q % 4 not in (0, 3):
        raise ValueError("Require q >= 5 and q or q+1 divisible by four")
    if not 1 <= depth_limit < minimum_n or minimum_n < 4 or maximum_n < minimum_n:
        raise ValueError("Require 1 <= depth < minimum_n <= maximum_n and minimum_n >= 4")
    if perturbed and depth_limit > 8:
        raise ValueError("Perturbed-grid digit bounds are supplied only through depth eight")
    product = q * (q + 1)
    pole_norm = (2 * q + 1)**2
    period = 1
    states = [(0, (1,))]
    for depth in range(1, depth_limit + 1):
        next_period = period * product
        next_states = []
        represented_degrees = 0
        for degree, prefix in states:
            a, b = local_lift(q, degree, period, prefix, pole_norm)
            c, d = local_lift(-q-1, degree, period, prefix, pole_norm)
            offset = combine(a, c, q)
            slope = combine(b, d, q)
            for digit in digits(prefix, perturbed):
                residue = degree + period * ((offset + slope * digit) % product)
                if residue % 2:
                    continue
                first = 2 * minimum_n + (residue - 2 * minimum_n) % next_period
                if first > 2 * maximum_n:
                    continue
                represented_degrees += 1 + (2 * maximum_n - first) // next_period
                next_states.append((residue, (*prefix, digit)))
        states, period = next_states, next_period
        print(f"depth={depth} prefixes={len(states)} degrees={represented_degrees}")
        if not states:
            break
    return states


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--q", type=int, default=40)
    parser.add_argument("--min-n", type=int, default=23)
    parser.add_argument("--max-n", type=int, default=10**12)
    parser.add_argument("--depth", type=int, default=20)
    parser.add_argument("--perturbed", action="store_true")
    args = parser.parse_args()
    sieve(args.q, args.min_n, args.max_n, args.depth, args.perturbed)
