"""Choose leading trace coefficients and recover an exact grid from a sine deformation."""

from fractions import Fraction
from math import cos, fsum, pi, sin

from trace_grid import candidate_on_grid, next_chebyshev, value_at


def choose_prefix(q, degree, depth):
    """Round each shifted Chebyshev trace to the integer pole-congruence lattice."""
    modulus = q * (q + 1)
    h = Fraction(1, modulus)
    residual = 4
    previous, current = [2], [2, 1]
    coefficients = [1]
    powers = [degree]
    targets, references = [], []
    for j in range(1, depth + 1):
        # Constant part of the j-th Newton sum before choosing c_j.
        constant = -sum(coefficients[i] * powers[j-i] for i in range(1, j))
        trace = constant + sum(b * p for b, p in zip(current[:-1], powers))
        reference = value_at(reversed(current), h)
        residue = residual % modulus
        offset = round((trace - j*residue - reference) / (j*modulus))
        coefficient = residue + modulus*offset
        moment = trace - j*coefficient
        assert 2*abs(moment - reference) <= j*modulus
        targets.append(moment)
        references.append(float(reference))
        coefficients.append(coefficient)
        powers.append(constant - j*coefficient)
        residual = (residual - coefficient) // modulus
        previous, current = current, next_chebyshev(previous, current)
    return coefficients, targets, references


def propose(q, degree, depth, denominator):
    """Use a numerical sine deformation to propose rational trace nodes."""
    count = degree - 1
    _, targets, references = choose_prefix(q, degree, depth)
    frequencies = range(1, depth + 1)
    midpoints = [pi * (i + 0.5)/count for i in range(count)]
    modes = [[sin(j*x) for j in frequencies] for x in midpoints]
    amplitudes = [0.0] * depth
    for _ in range(120):
        angles = [x + fsum(a*b for a, b in zip(amplitudes, row))/count
                  for x, row in zip(midpoints, modes)]
        updates = [(2*fsum(cos(j*x) for x in angles)+reference-target)/j
                   for j, reference, target in zip(frequencies, references, targets)]
        if max(map(abs, updates)) < 1e-8:
            break
        if max(map(abs, updates)) > degree:
            raise ValueError("Deformation failed to converge")
        amplitudes = [a+u for a, u in zip(amplitudes, updates)]
    else:
        raise ValueError("Deformation failed to converge")
    numerators = []
    for i in range(count+1):
        x = pi*i/count
        angle = x+fsum(a*sin(j*x) for j, a in zip(frequencies, amplitudes))/count
        numerators.append(round(denominator * (2*cos(angle)-2)))
    nodes = [Fraction(a, denominator) for a in reversed(numerators)]
    if any(left >= right for left, right in zip(nodes, nodes[1:])):
        raise ValueError("Proposed grid is not strictly increasing")
    return nodes


if __name__ == "__main__":
    trials = ((5, 121, 4, 5), (5, 481, 8, 10), (5, 981, 16, 17),
              (6, 643, 12, 14), (40, 1643, 4, 5))
    for q, degree, depth, expected_failure in trials:
        grid = propose(q, degree, depth, 2**40)
        poly, failure = candidate_on_grid(grid, q*(q+1), (2*q+1)**2, pole_weights=True)
        assert poly is None and failure == expected_failure
        print(f"q={q} degree={degree} fitted={depth} first_failure={failure}")
