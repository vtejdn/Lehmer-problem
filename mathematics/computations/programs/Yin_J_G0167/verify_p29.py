"""Test three residue classes modulo 29 for multiples of degree at most 32."""

from collections import Counter
from itertools import combinations

from checks.maximal_minors import maximal_minors, monomial_remainder


def main():
    powers = [monomial_remainder(e) for e in range(33)]
    counts = Counter()
    deficient = []
    for a, b in combinations(range(1, 29), 2):
        residues = {0, a, b}
        columns = [power for e, power in enumerate(powers) if e % 29 in residues]
        if not any(maximal_minors(columns)):
            deficient.append((a, b))
        counts[len(columns)] += 1
    if counts != {4: 300, 5: 75, 6: 3}:
        raise ArithmeticError(f"Incomplete support enumeration: {counts}")
    print(f"Triples by number of columns: {dict(sorted(counts.items()))}")
    print(f"Rank-deficient triples: {deficient}")
    if deficient:
        raise ArithmeticError("At least one tested support admits a nonzero multiple")


if __name__ == "__main__":
    main()
