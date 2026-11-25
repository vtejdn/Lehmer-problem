"""Exact obstructions to alternating signs on two rational trace grids."""

from collections import Counter
from fractions import Fraction
from math import prod


def uniform_endpoint_bound(n, modulus):
    """Upper bound for |H(-2)| on the equally spaced grid with n nodes."""
    nodes = [Fraction(4 * i, n - 1) - 4 for i in range(n)]
    farthest = [max(abs(left + 2), abs(right + 2))
                for left, right in zip(nodes, nodes[1:])]
    return (2 + Fraction(1, modulus)) * prod(farthest)


def circular_grid(n):
    """Generate a rational grid with the first two Lobatto node moments."""
    groups, remainder = divmod(n - 3, 4)
    if remainder or not groups:
        raise ValueError("Expected n = 4k + 3 with k positive")
    centered = [Fraction(-2), Fraction(0), Fraction(2)]
    for j in range(1, groups + 1):
        parameter = Fraction(j, 3 * groups + 1)
        square = parameter * parameter
        a = 2 * (1 - square) / (1 + square)
        b = 4 * parameter / (1 + square)
        assert a*a + b*b == 4
        centered.extend((-a, -b, b, a))
    nodes = sorted(t - 2 for t in centered)
    assert len(nodes) == len(set(nodes)) == n
    assert nodes[0] == -4 and nodes[-1] == 0
    assert sum(nodes) == -2 * n
    assert sum(t*t for t in nodes) == 6 * n + 2
    return nodes


def admissible_moment_pairs(q, n):
    """Possible residue moments after the Cauchy and pole-coefficient tests."""
    modulus = q * (q + 1)
    pairs = []
    for s in (2, 4):
        leading, rem = divmod(2*n - s - 4, modulus)
        if rem or leading <= 0:
            continue
        second_q = 2*n*n - 3*n - 1
        upper = Fraction(s, modulus) - s*s
        for moment in range(-4*s + 1, 0):
            if moment < upper and (moment - second_q + 2*n*s - leading) % modulus == 0:
                pairs.append((s, moment))
    return pairs


def next_chebyshev(previous, current):
    """Ascending coefficients of (x+2)current - previous."""
    result = [0] * (len(current) + 1)
    for j, coefficient in enumerate(current):
        result[j] += 2 * coefficient
        result[j+1] += coefficient
    for j, coefficient in enumerate(previous):
        result[j] -= coefficient
    return result


def value_at(coefficients, x):
    value = 0
    for coefficient in coefficients:
        value = x * value + coefficient
    return value


def candidate_on_grid(nodes, modulus, target, upper_root=None, *, pole_weights=False):
    """Return (H or None, failed index, with zero denoting infeasible pole data)."""
    n = len(nodes)
    assert n >= 2 and nodes[0] == -4 and nodes[-1] == 0
    assert all(left < right for left, right in zip(nodes, nodes[1:]))
    h = Fraction(1, modulus)
    if (target-1) % modulus:
        return None, 0
    if upper_root is None:
        assert target > 0
        upper_root = h
    assert upper_root > 0
    residue = (target-1) // modulus
    node_poly = [1]
    polynomial = [1]
    node_powers = [Fraction(1)] * n
    power_sums = [n]
    moments = []
    previous, current = [2], [2, 1]
    if pole_weights:
        mass = 1 - Fraction(target, prod(1-modulus*t for t in nodes))
        if mass <= 0:
            return None, 0
        weighted_moments = [mass]
    for j in range(1, n+1):
        node_powers = [power * t for power, t in zip(node_powers, nodes)]
        power_sums.append(sum(node_powers))
        node_poly.append(-sum(node_poly[j-k] * power_sums[k] for k in range(1, j+1)) / j)
        base = node_poly[j] - sum(node_poly[k] * moments[j-1-k] for k in range(1, j))
        if j == 1:
            lower, upper = base - (4+upper_root), base
        else:
            center = base + sum(c * moment for c, moment in zip(previous[:-1], moments))
            lower, upper = center - 2*moments[0], center + 2*moments[0]
        smallest = lower // 1 + 1
        largest = -((-upper) // 1) - 1
        if pole_weights:
            offset = h * weighted_moments[-1] - base
            offset += sum(c*m for c, m in zip(current[:-1], weighted_moments))
            smallest = max(smallest, -((2*mass + offset) // 1))
            largest = min(largest, (2*mass - offset) // 1)
        if j == n:
            coefficient = residue
        else:
            coefficient = smallest + (residue - smallest) % modulus
            if coefficient + modulus <= largest:
                raise ValueError("Grid step admits multiple integers of the required residue")
        if not smallest <= coefficient <= largest:
            return None, j
        polynomial.append(coefficient)
        residue = (residue - coefficient) // modulus
        moments.append(base - coefficient)
        if pole_weights:
            weighted_moments.append(h * weighted_moments[-1] - moments[-1])
        previous, current = current, next_chebyshev(previous, current)
    if value_at(polynomial, upper_root) <= 0 or any(
        (-1)**(n-i) * value_at(polynomial, t) <= 0 for i, t in enumerate(nodes)
    ):
        return None, "signs"
    assert modulus**n * value_at(polynomial, h) == target
    return polynomial, None


def distorted_grid(nodes, parameter):
    assert -1 <= parameter <= 1
    return [t + parameter*t*(t+4)/16 for t in nodes]


def sweep_deformations(q, degrees, *, pole_weights=False):
    modulus = q * (q + 1)
    results = Counter()
    for n in degrees:
        nodes = circular_grid(n)
        for leading in range(1, 10):
            for twice_mass in range(1, 8):
                mass = Fraction(twice_mass, 2)
                parameter = 8 * (4 + modulus*leading + mass - 2*n) / (n-1)
                if abs(parameter) > 1:
                    continue
                candidate, failure = candidate_on_grid(
                    distorted_grid(nodes, parameter), modulus, (2*q+1)**2, pole_weights=pole_weights
                )
                if candidate is not None:
                    print(f"candidate q={q} n={n} parameter={parameter} H={candidate}")
                results[failure] += 1
    return results


def main():
    for n in (16, 17):
        bound = uniform_endpoint_bound(n, 30)
        assert bound < 1
        print(f"uniform n={n} bound={bound}")
    for q, n in ((5, 63), (6, 87), (40, 1643), (5, 423)):
        nodes = circular_grid(n)
        modulus = q*(q+1)
        assert (2*n-6) % modulus == 0
        pairs = admissible_moment_pairs(q, n)
        candidate, failure = candidate_on_grid(nodes, modulus, (2*q+1)**2)
        assert candidate is None
        print(f"circular q={q} n={n} A={(2*n-6)//modulus} pairs={pairs} first failure={failure}")
        if (q, n) == (5, 423):
            assert pairs == [(2, -6)]
        else:
            assert not pairs
    nodes = [Fraction(-4), Fraction(-15, 4), Fraction(-3), Fraction(-2), Fraction(0)]
    recovered, _ = candidate_on_grid(nodes, 30, 6762031)
    assert recovered == [1, 11, 43, 69, 36, -1]
    assert candidate_on_grid(nodes, 30, 6762031, pole_weights=True)[0] == recovered
    print("positive control:", recovered)
    witness, _ = candidate_on_grid([Fraction(-4), Fraction(-2), Fraction(0)], 6, -5, Fraction(1))
    assert witness == [1, 5, 5, -1]
    witness_grid = [Fraction(-4), Fraction(-2), Fraction(0)]
    assert candidate_on_grid(witness_grid, 6, -5, Fraction(1), pole_weights=True)[0] == witness
    assert candidate_on_grid(witness_grid, 6, -4, Fraction(1)) == (None, 0)
    print("q=2 section witness:", witness)
    for q, degrees in ((5, range(23, 124, 4)), (6, range(23, 124, 4)),
                       (40, (1643,))):
        for reweight in (False, True):
            results = sweep_deformations(q, degrees, pole_weights=reweight)
            print(f"deformed q={q} reweighted={reweight} grids={results.total()} "
                  f"first failures={dict(results)}")


if __name__ == "__main__":
    main()
