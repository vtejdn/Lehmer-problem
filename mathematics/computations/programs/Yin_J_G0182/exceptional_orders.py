"""Exclude exceptional second-prime orders in the p=59 Salem seed slice."""

from collections import Counter
from functools import cache
from math import gcd, isqrt


FIRST_PRIME = 59
LAST_SECOND_PRIME = 410


def is_prime(value):
    return value >= 2 and all(value % t for t in range(2, isqrt(value) + 1))


@cache
def frobenius_orbit(characteristic, order, reciprocal):
    """Orbit size on one primitive root under Frobenius, optionally with inversion."""
    if gcd(characteristic, order) != 1:
        raise ValueError("Root order must be coprime to the characteristic.")
    orbit = set()
    residue = 1 % order
    while residue not in orbit:
        orbit.add(residue)
        residue = residue * characteristic % order
    if reciprocal:
        orbit |= {(-a) % order for a in orbit}
    return len(orbit)


def sparse_traces(seed, delay, sign, limit, modulus):
    """Newton sums of X^(n+1)-aX^n+sign*(aX-1), including the degree at zero."""
    degree = delay + 1
    coefficients = ((1, -seed), (delay, sign * seed), (degree, -sign))
    traces = [degree]
    for index in range(1, limit + 1):
        total = 0
        for offset, coefficient in coefficients:
            if offset == index:
                total += index * coefficient
            elif offset < index:
                total += coefficient * traces[index - offset]
        traces.append(-total % modulus)
    return traces


@cache
def admissible_seeds(characteristic, delay, sign):
    """All lifts mod h^2 surviving s_(hj)=s_j for j from one through four."""
    modulus = characteristic**2
    surviving = []
    for residue in range(characteristic):
        first = sparse_traces(residue, delay, sign, characteristic, modulus)
        lifted = first[characteristic]
        if lifted % characteristic != residue:
            raise ArithmeticError("Frobenius trace congruence failed.")
        traces = sparse_traces(lifted, delay, sign, 4 * characteristic, modulus)
        if all(traces[characteristic * j] == traces[j] for j in range(1, 5)):
            surviving.append(lifted)
    return tuple(surviving)


@cache
def cyclotomic_orders(delay, sign, seed):
    """Primitive root orders and their common multiplicities in G_seed/U."""
    if seed == 0:
        exponent, scalar = delay + 1, sign
    elif abs(seed) == 1:
        exponent, scalar = delay, -sign * seed
    else:
        raise ValueError("Cyclotomic seed required.")
    orders = Counter()
    period = exponent if scalar == 1 else 2 * exponent
    for order in range(1, period + 1):
        if period % order == 0 and (scalar == 1 or exponent % order != 0):
            orders[order] = 1
    if seed:
        orders[1 if seed == 1 else 2] += 1
    for root in (-1, 1):
        if root ** (delay - 1) == sign:
            orders[1 if root == 1 else 2] -= 1
    if min(orders.values()) < 0:
        raise ArithmeticError("The indicated linear cofactor must divide the seed.")
    return tuple((order, mult) for order, mult in sorted(orders.items()) if mult)


def forces_cyclotomic_inverse(characteristic, exponent, delay, sign, lifted):
    residue = lifted % characteristic
    if residue == characteristic - 1:
        residue = -1
    if residue not in (-1, 0, 1):
        return False
    for order, multiplicity in cyclotomic_orders(delay, sign, residue):
        if gcd(order, characteristic * exponent) != 1:
            return False
        target = frobenius_orbit(characteristic, order, reciprocal=True)
        source = frobenius_orbit(characteristic, order * exponent, reciprocal=True)
        cost, remainder = divmod(source, target)
        if remainder:
            raise ArithmeticError("The orbit map must have constant fiber size.")
        if cost <= multiplicity:
            return False
    return True


def direction(characteristic, exponent, delay, sign):
    lifts = admissible_seeds(characteristic, delay, sign)
    return tuple(lift for lift in lifts if not forces_cyclotomic_inverse(
        characteristic, exponent, delay, sign, lift
    ))


def centered(residues, modulus):
    return tuple(sorted((v + modulus // 2) % modulus - modulus // 2 for v in residues))


def main():
    for delay in range(55, 59):
        for sign in (-1, 1):
            lifts = centered(admissible_seeds(FIRST_PRIME, delay, sign), FIRST_PRIME**2)
            print("first-prime trace lifts", delay, sign, lifts)
    print("q ord_q(59) forward_rows reverse_rows reverse_lifts unresolved_rows")
    second_primes = [
        q for q in range(FIRST_PRIME + 1, LAST_SECOND_PRIME + 1)
        if is_prime(q) and frobenius_orbit(FIRST_PRIME, q, reciprocal=False) <= 58
    ]
    unresolved = []
    reverse_details = []
    for prime in second_primes:
        forward = reverse = reverse_lifts = 0
        for delay in range(55, 59):
            for sign in (-1, 1):
                remaining = direction(FIRST_PRIME, prime, delay, sign)
                if not remaining:
                    forward += 1
                    continue
                reverse_remaining = direction(prime, FIRST_PRIME, delay, sign)
                reverse_lifts += len(admissible_seeds(prime, delay, sign))
                if reverse_remaining:
                    unresolved.append((prime, delay, sign, remaining, reverse_remaining))
                else:
                    reverse += 1
                    lifts = admissible_seeds(prime, delay, sign)
                    reverse_details.append((prime, delay, sign, centered(lifts, prime**2)))
        print(prime, frobenius_orbit(FIRST_PRIME, prime, reciprocal=False),
              forward, reverse, reverse_lifts, 8 - forward - reverse)
    if unresolved:
        raise ArithmeticError(f"Unresolved pairs of seed residues: {unresolved}")
    for row in reverse_details:
        print("reverse trace lifts", *row)
    print("excluded primes", len(second_primes), "excluded delay/sign rows", 8 * len(second_primes))


if __name__ == "__main__":
    main()
