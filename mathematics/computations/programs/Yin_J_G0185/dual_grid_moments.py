"""Exact residue and Hankel tests for an integral trace grid polynomial (low coefficients first)."""

from fractions import Fraction

from trace_grid import next_chebyshev


def scaled_pole(polynomial, modulus):
    """Return M^degree Q(1/M) using Horner evaluation of the reversed coefficients."""
    value = 0
    for coefficient in polynomial:
        value = modulus * value + coefficient
    return value


def centered(residue, modulus):
    residue %= modulus
    return residue - modulus if 2 * residue > modulus else residue


def scaled_monomial_moments(grid, chebyshev_moments):
    degree = len(grid) - 1
    moments = [chebyshev_moments[0]]
    previous, current = [2], [2, 1]
    for j in range(1, degree):
        moments.append(chebyshev_moments[j] - sum(a*b for a, b in zip(current, moments)))
        previous, current = current, next_chebyshev(previous, current)
    for j in range(degree, 2*degree-1):
        moments.append(-sum(grid[i] * moments[j-degree+i] for i in range(degree)))
    return moments


def positive_leading_minors(moments, degree):
    """Fraction-free symmetric elimination, stopping at the first nonpositive minor."""
    matrix = [[moments[i+j] for j in range(degree)] for i in range(degree)]
    previous = 1
    minors = []
    for i in range(degree):
        pivot = matrix[i][i]
        minors.append(pivot)
        if pivot <= 0:
            break
        for a in range(i+1, degree):
            for b in range(a, degree):
                numerator = pivot*matrix[a][b] - matrix[a][i]*matrix[i][b]
                entry, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("Non-exact fraction-free division")
                matrix[a][b] = matrix[b][a] = entry
        previous = pivot
    return minors


def test_grid(q, grid, target):
    """Input Q must be monic with distinct real roots in [-4,0], including both endpoints."""
    degree = len(grid) - 1
    modulus = q*(q+1)
    if q < 2 or degree < 2 or grid[-1] != 1 or target <= 0:
        raise ValueError("Require q>=2, positive target and monic Q of degree>=2")
    if target % modulus != 1:
        return {"feasible": False, "failure": "pole congruence"}
    pole = scaled_pole(grid, modulus)
    if pole <= target:
        return {"feasible": False, "failure": "total mass"}
    mass = pole - target
    factor = mass // modulus
    ratio = (q+1)*pow(q, -1, pole) % pole
    inverse = pow(ratio, -1, pole)
    forward = backward = 1
    moments = [mass]
    for j in range(1, degree):
        forward = forward*ratio % pole
        backward = backward*inverse % pole
        value = modulus * centered(factor*(forward+backward), pole)
        if abs(value) > 2*mass:
            return {"feasible": False, "failure": "moment interval", "index": j}
        moments.append(value)
    monomial = scaled_monomial_moments(grid, moments)
    minors = positive_leading_minors(monomial, degree)
    return {"feasible": minors[-1] > 0,
            "moments": [Fraction(value, pole) for value in moments],
            "minors": [Fraction(value, pole**j) for j, value in enumerate(minors, 1)]}


if __name__ == "__main__":
    grid = [0, 12, 7, 1]  # x(x+3)(x+4)
    for target in (25, 109):
        data = test_grid(2, grid, target)
        print(f"K={target} feasible={data['feasible']}")
        print("moments", *(str(value) for value in data['moments']))
        print("leading minors", *(str(value) for value in data['minors']))
    assert not test_grid(2, grid, 25)["feasible"]
    assert test_grid(2, grid, 109)["feasible"]
