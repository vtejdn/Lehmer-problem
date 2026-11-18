"""Reproduce the degree-106 Lehmer test by exact maximal minors."""

from itertools import combinations


def monomial_remainder(exponent):
    """Divide one monomial by the monic Lehmer polynomial over the integers."""
    coeffs = [0] * max(10, exponent + 1)
    coeffs[exponent] = 1
    for top in range(exponent, 9, -1):
        leading = coeffs.pop()
        offset = top - 10
        for degree in (0, 1, 9):
            coeffs[offset + degree] -= leading
        for degree in (3, 4, 5, 6, 7):
            coeffs[offset + degree] += leading
    return coeffs


def maximal_minors(columns):
    """Expand minors of the first k columns along column k."""
    previous = {(): 1}
    for k, column in enumerate(columns, start=1):
        current = {}
        for rows in combinations(range(len(column)), k):
            value = 0
            for i, row in enumerate(rows):
                smaller = rows[:i] + rows[i + 1:]
                term = column[row] * previous[smaller]
                value += term if (i + k - 1) % 2 == 0 else -term
            current[rows] = value
        previous = current
    return tuple(previous.values())


def main():
    remainders = [monomial_remainder(e) for e in range(107)]
    checked = 0
    minimum = None
    minimizers = []
    for a in range(1, 52):
        for b in range(a + 1, 53):
            support = (0, a, b, 53, 53 + a, 53 + b, 106)
            minors = maximal_minors([remainders[e] for e in support])
            if len(minors) != 120 or not any(value % 1009 for value in minors):
                raise ArithmeticError(f"Missing full-rank minor at {(a, b)}")
            gram = sum(value * value for value in minors)
            if minimum is None or gram < minimum:
                minimum = gram
                minimizers = []
            if gram == minimum:
                minimizers.append((a, b))
            checked += 1
    if checked != 1326:
        raise ArithmeticError(f"Incomplete count: {checked}")
    print(f"Pairs with a nonzero integer minor also nonzero modulo 1009: {checked}")
    print(f"Least sum of squared maximal minors: {minimum} at {minimizers}")


if __name__ == "__main__":
    main()
