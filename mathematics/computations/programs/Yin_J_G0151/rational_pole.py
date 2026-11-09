"""Exact fixed rational-pole check in the five N=7 residual branches.

Scope: five (O,V,W) triples, the two possible values h(-1)=32,2048,
and the four displayed moment/localizing matrices from sigma_0,...,sigma_5.
No LP, conductor scan, or parameter scan is performed.  The inherited
layer minima are checked at their common attaining vector, not reoptimized.
"""

from fractions import Fraction as F
from time import monotonic

from conductor19683 import DEGREES, NORM_EXPONENT, P, PARITIES, VALUATIONS


TRIPLES = ((10, 18, 27), (11, 20, 33), (11, 20, 34),
           (11, 21, 36), (11, 21, 37))
ATOM_VALUES = (32, 2048)
ATOM_FACTOR = F(183, 100 * P)
Y = F(-161, 100)
EXPECTED_PLUS_CAPS = (
    F(1890993681, 3916078),
    F(35503342470, 58516507),
    F(211554917910, 210917321),
    F(30336347205, 97326293),
    F(196053932115, 327346679),
)
# These weights/minima are inherited exact inputs from C882v3 and C882v5.
LAYER_COSTS = (
    ("linear-3", (183, 171, 109, 106, 100, 101, 101, 101, 101), 1562883),
    ("linear-9", (549, 247, 123, 110, 101, 102, 101, 101, 101), 1580979),
    ("linear-27", (1647, 355, 139, 114, 103, 102, 101, 101, 101), 1623531),
    ("cubic", (135, 15, 17, 15, 14, 14, 14, 14, 14), 219942),
    ("seventh", (6588, 355, 139, 114, 103, 102, 101, 101, 101), 1781643),
)


def determinant(matrix):
    matrix = [list(map(F, row)) for row in matrix]
    result = F(1)
    for i in range(len(matrix)):
        pivot = next((j for j in range(i, len(matrix)) if matrix[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
            result = -result
        value = matrix[i][i]
        result *= value
        for j in range(i + 1, len(matrix)):
            multiplier = matrix[j][i] / value
            for k in range(i + 1, len(matrix)):
                matrix[j][k] -= multiplier * matrix[i][k]
    return result


def leading_minors(matrix):
    return tuple(determinant([row[:size] for row in matrix[:size]])
                 for size in range(1, len(matrix) + 1))


def solve(matrix, rhs):
    n = len(matrix)
    augmented = [list(map(F, row)) + [F(value)]
                 for row, value in zip(matrix, rhs)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if augmented[j][i])
        augmented[i], augmented[pivot] = augmented[pivot], augmented[i]
        divisor = augmented[i][i]
        augmented[i] = [value / divisor for value in augmented[i]]
        for j in range(n):
            if j != i:
                multiplier = augmented[j][i]
                augmented[j] = [a - multiplier * b
                                for a, b in zip(augmented[j], augmented[i])]
    result = [row[-1] for row in augmented]
    assert all(sum(a * b for a, b in zip(row, result)) == value
               for row, value in zip(matrix, rhs))
    return result


def sigma_moments(triple):
    residue = [3, 4, 7, *triple]
    sigma = [F(261, 100)]
    for j in range(5):
        sigma.append(F(residue[j + 1]) - Y * residue[j] - 2 * sigma[-1])
    assert sigma[:3] == [F(261, 100), F(361, 100), F(622, 100)]
    return sigma


def matrices(sigma):
    return {
        "plain": [[sigma[i + j] for j in range(3)] for i in range(3)],
        "plus": [[2 * sigma[i + j] + sigma[i + j + 1]
                  for j in range(3)] for i in range(3)],
        "minus": [[2 * sigma[i + j] - sigma[i + j + 1]
                   for j in range(3)] for i in range(3)],
        "interior": [[4 * sigma[i + j] - sigma[i + j + 2]
                      for j in range(2)] for i in range(2)],
    }


def atom_cap(matrix, multiplier):
    vector = [F((-1) ** i) for i in range(len(matrix))]
    coefficients = solve(matrix, vector)
    quadratic = sum(a * b for a, b in zip(vector, coefficients))
    assert quadratic > 0
    return 1 / (ATOM_FACTOR * multiplier * quadratic), coefficients


def main():
    started = monotonic()
    assert VALUATIONS[0] == 5
    assert sum(d * t for d, t in zip(DEGREES, VALUATIONS)) == NORM_EXPONENT
    assert all(t % 2 == parity for t, parity in zip(VALUATIONS, PARITIES))
    assert NORM_EXPONENT % 3 == 2 and PARITIES[0] == 1
    # Positive sigma mass bounds h(-1) strictly; together with t1=5 mod 6
    # this leaves exactly the two values displayed, without a long prefix.
    scalar_cap = F(261, 100) / ATOM_FACTOR
    assert 2**11 < scalar_cap < 2**17
    print("norm/parity and positive-mass candidates", ATOM_VALUES)
    for row, triple in enumerate(TRIPLES):
        assert monotonic() - started < 60, "60-second finite-check limit"
        sigma = sigma_moments(triple)
        original = matrices(sigma)
        caps = {}
        for name, matrix in original.items():
            assert all(value > 0 for value in leading_minors(matrix))
            multiplier = {"plain": 1, "plus": 1, "minus": 3, "interior": 3}[name]
            caps[name], _ = atom_cap(matrix, multiplier)
        assert caps["plus"] == EXPECTED_PLUS_CAPS[row]
        assert 32 < caps["plus"] < 2048
        print("triple", triple, "strict h(-1) caps",
              {name: str(value) for name, value in caps.items()})
        outcomes = {}
        for atom in ATOM_VALUES:
            reduced = [value - ATOM_FACTOR * atom * (-1)**j
                       for j, value in enumerate(sigma)]
            minors = {name: leading_minors(matrix)
                      for name, matrix in matrices(reduced).items()}
            outcomes[atom] = {
                name: all(value > 0 for value in values)
                for name, values in minors.items()
            }
            print("  atom", atom, "leading minors",
                  {name: [str(value) for value in values]
                   for name, values in minors.items()})
        assert not outcomes[2048]["plus"]
        assert all(outcomes[32].values())
        print("  all four reduced matrices positive definite at h(-1)=32")
    for name, weights, old_minimum in LAYER_COSTS:
        value = sum(d * 2**t * weight
                    for d, t, weight in zip(DEGREES, VALUATIONS, weights))
        assert value == old_minimum
        remainder = value - 32 * weights[0]
        print("inherited minimum", name, old_minimum,
              "attained with t1=5; remaining-layer minimum", remainder)
    assert monotonic() - started < 60, "60-second finite-check limit"
    print("COMPLETE: all five branches force h(-1)=32; no branch is excluded",
          "by these reduced matrices or the inherited scalar layer minima")


if __name__ == "__main__":
    main()
