"""Determine the argument-rank-three core below 1.3 through degree 44."""

from collections import Counter
from fractions import Fraction
from math import lcm
from pathlib import Path
import sys


PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0188"))
from radial_cores import signature, squarefree_pattern, table_rows, trace_from_half


ORDER_PRIMES = (2, 3, 5, 11, 13)
# The index and degree of each cyclotomic polynomial of degree at most six.
CYCLOTOMICS = ((1, 1), (2, 1), (3, 2), (4, 2), (6, 2), (5, 4),
               (8, 4), (10, 4), (12, 4), (7, 6), (9, 6), (14, 6), (18, 6))
# Source line: (prime exhibiting an (n-1)-cycle, prime exhibiting a mixed flip).
# A transitive action on a prime number of inverse pairs needs no extra prime.
EXTRA_PRIMES = {158: (None, 5), 159: (None, 5), 162: (19, 2),
                164: (3, 5), 165: (5, 7), 166: (17, 37), 193: (29, 11)}


def permitted_orders(rank):
    states = {(0, 1)}
    for index, degree in CYCLOTOMICS:
        states |= {(used + degree, lcm(order, index)) for used, order in states
                   if used + degree <= rank}
    return {order for _, order in states}


def order_prime(polynomial, orders):
    for prime in ORDER_PRIMES:
        try:
            degrees = squarefree_pattern(polynomial, prime)
        except ArithmeticError as error:
            if not str(error).startswith("Repeated factor in characteristic"):
                raise
            continue
        if sum(degrees) != len(polynomial) - 1:
            raise ArithmeticError("Incomplete factorization pattern.")
        if lcm(*degrees) not in orders:
            return prime
    return None


def verify_flip(line, polynomial, trace, shape):
    n = len(trace) - 1
    cycle_prime, flip_prime = EXTRA_PRIMES[line]
    if cycle_prime is None:
        if n != 5:
            raise ArithmeticError("Missing primitivity certificate.")
    elif squarefree_pattern(trace, cycle_prime) != (1, n - 1):
        raise ArithmeticError("Missing full cycle on the remaining labels.")

    trace_degrees = squarefree_pattern(trace, flip_prime)
    root_degrees = squarefree_pattern(polynomial, flip_prime)
    if sum(trace_degrees) != n or sum(root_degrees) != 2 * n:
        raise ArithmeticError("Incomplete joint degree patterns.")
    power = lcm(*trace_degrees)
    moved = sum(length for length in root_degrees if power % length)
    if moved % 2 or not 0 < moved < 2 * n:
        raise ArithmeticError("The resulting sign flip is constant.")
    below, _, above, nonreal_pairs = shape
    argument_rank = n - below - above - nonreal_pairs
    if argument_rank <= 3:
        raise ArithmeticError("Unexpected rank at a signed certificate.")
    print(line, n, cycle_prime, flip_prime, trace_degrees, root_degrees,
          moved // 2, argument_rank)


def verify_winner(polynomial, shape):
    if polynomial != (1, 0, 0, 1, -1, 1, 0, 0, 1) or shape != (1, 3, 0, 0):
        raise ArithmeticError("Unexpected attaining polynomial or trace signature.")
    signs = []
    for endpoint in (Fraction(12806, 10000), Fraction(12807, 10000)):
        value = 0
        for coefficient in polynomial:
            value = value * (-endpoint) + coefficient
        signs.append((value > 0) - (value < 0))
    if signs != [-1, 1]:
        raise ArithmeticError("The exterior root is not isolated in the stated interval.")


def main():
    order_sets = {r: permitted_orders(r) for r in range(1, 7)}
    counts = Counter()
    unresolved = []
    for line, degree, _, _, polynomial in table_rows():
        if degree > 44:
            continue
        n = degree // 2
        trace = trace_from_half(polynomial[:n + 1])
        _, shape = signature(trace)
        neutral = shape[1]
        if not 0 < neutral < n:
            raise ArithmeticError(f"Unexpected neutral count on line {line}.")
        if neutral > 3 * (n - neutral):
            counts["signature"] += 1
            continue
        rank_bound = 3 * n // neutral
        if rank_bound not in order_sets:
            raise ArithmeticError(f"Unsupported rank bound on line {line}.")
        prime = order_prime(polynomial, order_sets[rank_bound])
        if prime is not None:
            counts[prime] += 1
            continue
        unresolved.append(line)
        if line == 152:
            verify_winner(polynomial, shape)
        else:
            verify_flip(line, polynomial, trace, shape)

    if unresolved != sorted({152, *EXTRA_PRIMES}):
        raise ArithmeticError(f"Unexpected residual rows: {unresolved}.")
    expected = {"signature": 519, 2: 369, 3: 40, 5: 6, 11: 1, 13: 1}
    if dict(counts) != expected or sum(counts.values()) + len(unresolved) != 944:
        raise ArithmeticError(f"Unexpected exhaustive counts: {counts}.")
    print(f"First exclusions: {dict(counts)}")
    print(f"Residual lines: {unresolved}")
    print("Unique compressed row of rank at most three: 152 (rank three).")


if __name__ == "__main__":
    main()
