"""Check all triples of residues containing zero at modulus 53."""

from itertools import combinations


# Coefficients in ascending powers, omitting the leading x^10.
LEHMER = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1)
MODULUS = 53
MAX_DEGREE = 106
FIELD = 1009


def power_vectors():
    """Return the integral coefficient vectors of x^e modulo L."""
    degree = len(LEHMER)
    powers = [(1,) + (0,) * (degree - 1)]
    for _ in range(MAX_DEGREE):
        previous = powers[-1]
        shifted = (0,) + previous[:-1]
        powers.append(tuple(v - previous[-1] * c for v, c in zip(shifted, LEHMER)))
    return powers


def modular_rank(vectors):
    basis = {}
    for vector in vectors:
        row = [v % FIELD for v in vector]
        for j in range(len(row)):
            if not row[j]:
                continue
            if j not in basis:
                inv = pow(row[j], -1, FIELD)
                basis[j] = [(v * inv) % FIELD for v in row]
                break
            multiple = row[j]
            row = [(v - multiple * w) % FIELD for v, w in zip(row, basis[j])]
    return len(basis)


def gram_determinant(vectors):
    """Fraction-free elimination on the symmetric integer Gram matrix."""
    matrix = [[sum(x * y for x, y in zip(u, v)) for v in vectors] for u in vectors]
    previous = 1
    for j in range(len(vectors) - 1):
        pivot = matrix[j][j]
        if pivot == 0:
            # The leading Gram minor vanishes, so the full list is dependent.
            return 0
        for row in range(j + 1, len(vectors)):
            for col in range(j + 1, len(vectors)):
                numerator = pivot * matrix[row][col] - matrix[row][j] * matrix[j][col]
                matrix[row][col], remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("Bareiss division was not exact")
        previous = pivot
    return matrix[-1][-1]


def main():
    powers = power_vectors()
    total = 0
    smallest = None
    for a, b in combinations(range(1, MODULUS), 2):
        exponents = [e for e in range(MAX_DEGREE + 1) if e % MODULUS in (0, a, b)]
        vectors = [powers[e] for e in exponents]
        if len(vectors) != 7 or modular_rank(vectors) != 7:
            raise ArithmeticError(f"Rank 7 over F_{FIELD} failed for {(a, b)}")
        determinant = gram_determinant(vectors)
        if determinant <= 0:
            raise ArithmeticError(f"Positive Gram determinant failed for {(a, b)}")
        total += 1
        if smallest is None or determinant < smallest[0]:
            smallest = (determinant, a, b)
    if total != 1326:
        raise ArithmeticError(f"Unexpected number of residue triples: {total}")
    print(f"{total} triples: rank 7 over F_{FIELD} and positive integral Gram determinant")
    print(f"Least Gram determinant: {smallest[0]} at residues (0, {smallest[1]}, {smallest[2]})")


if __name__ == "__main__":
    main()
