"""Check the fixed degree-18 positive control using integer and rational arithmetic."""

from fractions import Fraction
from math import comb


# Q is given in ascending powers. Mossinghoff's half starts at the leading term.
TRACE = (1, 2, -13, -16, 19, 20, -8, -8, 1, 1)
SOURCE_HALF = (1, 1, 1, 0, 0, -1, 0, -1, 0, -1)
BRACKETS = (-146, -78, -25, 32, 105, 165, 199)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def evaluate(x):
    value = 0
    for coefficient in reversed(TRACE):
        value = value * x + coefficient
    return value


def ellipse(x, y, rho):
    return (x / (rho + 1 / rho)) ** 2 + (y / (rho - 1 / rho)) ** 2


def main():
    degree = len(TRACE) - 1
    lift = [0] * (2 * degree + 1)
    for j, coefficient in enumerate(TRACE):
        for k in range(j + 1):
            lift[degree + 2 * k - j] += coefficient * comb(j, k)
    require(tuple(reversed(lift)) == SOURCE_HALF + SOURCE_HALF[-2::-1],
            "The reciprocal lift differs from the source coefficient list.")

    require(len(BRACKETS) == degree - 2 and
            all(a + 1 <= b for a, b in zip(BRACKETS, BRACKETS[1:])),
            "The real brackets must have disjoint interiors and use n-2 roots.")
    for k in BRACKETS:
        left, right = Fraction(k, 100), Fraction(k + 1, 100)
        require(-2 <= left < right <= 2 and evaluate(left) * evaluate(right) < 0,
                f"Invalid sign bracket with left endpoint {left}.")

    # The disk has center (u+iv)/D and radius 1/D.
    u, v, denominator = -177624, 8576, 100000
    require(v > 1, "The disk must lie strictly above the real axis.")
    powers = [(1, 0)]
    for _ in range(degree):
        x, y = powers[-1]
        powers.append((u*x - v*y, v*x + u*y))

    # Compute coefficients of D^n Q((u+iv+s)/D) as Gaussian integers.
    shifted = []
    for k in range(degree + 1):
        real = imag = 0
        for j in range(k, degree + 1):
            weight = TRACE[j] * comb(j, k) * denominator ** (degree - j)
            x, y = powers[j - k]
            real += weight * x
            imag += weight * y
        shifted.append((real, imag))
    error = sum(abs(x) + abs(y) for k, (x, y) in enumerate(shifted) if k != 1)
    require(8 * error < -shifted[1][1],
            "The linear term lacks the specified strict Rouche margin on |s|=1.")

    lower = Fraction(109606, 100000)
    upper = Fraction(10961, 10000)
    min_x, min_y = Fraction(abs(u) - 1, denominator), Fraction(v - 1, denominator)
    max_x, max_y = Fraction(abs(u) + 1, denominator), Fraction(v + 1, denominator)
    require(ellipse(min_x, min_y, lower) > 1 and ellipse(max_x, max_y, upper) < 1,
            "The disk does not lie strictly between the two specified ellipses.")
    print("Verified degree-18 lift, seven real trace roots and one nonreal trace pair.")
    print(f"Mahler measure: {lower**2} < M < {upper**2}")


if __name__ == "__main__":
    main()
