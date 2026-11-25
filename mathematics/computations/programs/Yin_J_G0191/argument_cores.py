"""Exclude faithful class representations of argument rank at most two."""

from collections import Counter
from math import lcm
from pathlib import Path
import sys


PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0188"))
from radial_cores import signature, squarefree_pattern, table_rows, trace_from_half


ORDERS = {
    3: {1, 2, 3, 4, 6},
    4: {1, 2, 3, 4, 5, 6, 8, 10, 12},
}
PRIMES = (2, 3, 11)


def order_certificate(polynomial, rank_bound):
    for prime in PRIMES:
        try:
            degrees = squarefree_pattern(polynomial, prime)
        except ArithmeticError as error:
            if not str(error).startswith("Repeated factor in characteristic"):
                raise
            continue
        if sum(degrees) != len(polynomial) - 1:
            raise ArithmeticError("Factor degrees do not sum to the input degree.")
        if lcm(*degrees) not in ORDERS[rank_bound]:
            return prime, degrees
    return None


def main():
    signature_count = 0
    rank_counts = Counter()
    prime_counts = Counter()
    later_certificates = []
    for line, degree, _, _, polynomial in table_rows():
        if degree > 44:
            continue
        n = degree // 2
        trace = trace_from_half(polynomial[:n + 1])
        _, (_, neutral, _, _) = signature(trace)
        exterior = n - neutral
        if not 0 < neutral < n:
            raise ArithmeticError(f"Unexpected signature on line {line}.")
        if neutral > 2 * exterior:
            signature_count += 1
            continue
        rank_bound = 2 * n // neutral
        if rank_bound not in ORDERS:
            raise ArithmeticError(f"Unsupported rank bound {rank_bound} on line {line}.")
        certificate = order_certificate(polynomial, rank_bound)
        if certificate is None:
            raise ArithmeticError(f"No order certificate on line {line}.")
        prime, degrees = certificate
        rank_counts[rank_bound] += 1
        prime_counts[prime] += 1
        if prime != 2:
            later_certificates.append((line, rank_bound, prime, degrees, lcm(*degrees)))

    total = signature_count + sum(prime_counts.values())
    if (total, signature_count, dict(prime_counts)) != (944, 810, {2: 123, 3: 10, 11: 1}):
        raise ArithmeticError("The exhaustive counts differ from the recorded result.")
    print(f"Rows checked: {total}. Excluded by signature: {signature_count}.")
    print(f"Order tests by rank bound: {dict(sorted(rank_counts.items()))}")
    print(f"Order tests by first certifying prime: {dict(sorted(prime_counts.items()))}")
    print("Later certificates (line, rank bound, prime, factor degrees, order):")
    for certificate in later_certificates:
        print(certificate)


if __name__ == "__main__":
    main()
