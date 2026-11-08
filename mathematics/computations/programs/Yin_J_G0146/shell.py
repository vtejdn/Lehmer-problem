"""Exact circular-unit construction, conditional census, and whole-measure checks."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import sys

from sympy import Poly, Rational, symbols, oo

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Yin_J_G0144"))
from pilot import graeffe

t, z = symbols("t z")

# (lower, upper) in thousandths, indexed by the exponents and integer a.
HIT_WINDOWS = {
    ((-1, 0, -1, 1, 0), 1): (1250, 1260),
    ((0, 1, 0, -1, 0), 1): (1260, 1266),
    ((1, 0, 0, 0, -1), 0): (1266, 1275),
    ((-1, 0, 0, 0, 1), 2): (1275, 1290),
}


def signature(p, j):
    """Bit k-1 is one for a negative j-th unit at b_k (b_1 is largest)."""
    return sum(((2*j*k // p) % 2) << (k-1) for k in range(1, p//2 + 1))


def required_signatures(p):
    """Include the derivative sign to turn a residue cut into a numerator signature."""
    n = p//2
    derivative = sum((k % 2) << k for k in range(n))
    return {derivative ^ ((1 << n) - (1 << r)): r for r in range(1, n)}


def signature_image(p):
    basis = {}

    def reduce_mask(mask):
        while mask and mask.bit_length() in basis:
            mask ^= basis[mask.bit_length()]
        return mask

    n = p//2
    for row in [(1 << n) - 1, *(signature(p, j) for j in range(2, n + 1))]:
        reduced = reduce_mask(row)
        if reduced:
            basis[reduced.bit_length()] = reduced
    cuts = sorted(r for mask, r in required_signatures(p).items() if reduce_mask(mask) == 0)
    return len(basis), cuts


def trace_ring(p):
    """Construct B, the circular units, their integral inverses and their signs."""
    n = p//2
    one = Poly(1, t)
    variable = Poly(t, t)
    previous, current = 2*one, variable
    poles = one
    for _ in range(n):
        poles += current
        previous, current = current, variable*current - previous
    intervals = list(reversed(poles.intervals(eps=Rational(1, 10000))))
    assert len(intervals) == n
    units = {}
    previous, current = one, variable
    for j in range(2, n + 1):
        inverse = current.invert(poles).set_domain("ZZ")
        assert (inverse*current).rem(poles) == one
        negative = 0
        for k, ((lo, hi), multiplicity) in enumerate(intervals):
            assert multiplicity == 1 and current.count_roots(lo, hi) == 0
            if current.eval(lo) < 0:
                negative |= 1 << k
        assert negative == signature(p, j)
        units[j] = {-1: inverse, 0: one, 1: current}
        previous, current = current, variable*current - previous
    return poles, units


def reciprocal_lift(trace):
    """Return integer coefficients in ascending order via z^d (z + z^-1)^k."""
    d = trace.degree()
    coefficients = [0] * (2*d + 1)
    for (k,), value in trace.terms():
        for j in range(k + 1):
            coefficients[d-k+2*j] += int(value)*comb(k, j)
    assert coefficients[0] == coefficients[-1] == 1
    assert coefficients == coefficients[::-1]
    return tuple(coefficients)


def certify_window(coefficients, lower, upper, max_depth):
    """Give a strict whole-measure decision or report insufficient resolution."""
    values = coefficients
    binomials = [comb(len(values) - 1, j) for j in range(len(values))]
    for depth in range(max_depth + 1):
        power = 1 << depth
        def above(bound):
            numerator = bound.numerator**power
            denominator = bound.denominator**power
            return any(abs(value)*denominator > b*numerator for value, b in zip(values, binomials))

        if above(upper):
            return "above", depth
        square_norm = sum(value*value for value in values)
        if square_norm * upper.denominator**(2*power) < upper.numerator**(2*power) and above(lower):
            return "inside", depth
        if depth < max_depth:
            values = graeffe(values)
    raise ArithmeticError(f"Undecided window ({lower}, {upper}) for {coefficients}")


def check_hit(trace, coefficients, exponents, a):
    low, high = HIT_WINDOWS[exponents, a]
    decision, depth = certify_window(coefficients, Fraction(low, 1000), Fraction(high, 1000), 13)
    assert decision == "inside"
    assert trace.gcd(trace.diff()).degree() == 0
    assert trace.eval(-2) and trace.eval(2)
    inside = trace.count_roots(-2, 2)
    left = trace.count_roots(-oo, -2)
    right = trace.count_roots(2, oo)
    polynomial = Poly.from_list(coefficients, z)
    if low == 1250:
        assert (left, inside, right) == (0, 6, 1)
        assert trace.set_modulus(2).is_irreducible
    else:
        assert (left, inside, right) == (0, 5, 0)
        if low == 1266:
            cofactor = Poly(1 + z + z**2 + z**3 + z**4, z)
            core = Poly(1 + z**2 + z**3 + z**5 + z**7 + z**8 + z**10, z)
            assert polynomial == cofactor*core and core.set_modulus(3).is_irreducible
        else:
            assert polynomial.set_modulus(2).is_irreducible
    return low, high, depth


def run():
    p, n = 13, 6
    poles, units = trace_ring(p)
    targets = required_signatures(p)
    full = (1 << n) - 1
    cut_units, cut_atoms, depths = Counter(), Counter(), Counter()
    inputs, hits = set(), []
    for exponents in product((-1, 0, 1), repeat=n-1):
        unsigned = Poly(1, t)
        mask = 0
        for j, exponent in enumerate(exponents, 2):
            unsigned = (unsigned*units[j][exponent]).rem(poles)
            if exponent:
                mask ^= signature(p, j)
        for sign in (-1, 1):
            signed_mask = mask ^ (full if sign == -1 else 0)
            if signed_mask not in targets:
                continue
            cut = targets[signed_mask]
            cut_units[cut] += 1
            numerator = sign*unsigned
            assert abs(poles.resultant(numerator)) == 1
            for a in range(-3, 4):
                trace = Poly(t-a, t)*poles + numerator
                if trace.eval(-2)*poles.eval(-2) >= 0:
                    continue
                coefficients = reciprocal_lift(trace)
                assert coefficients not in inputs
                inputs.add(coefficients)
                cut_atoms[cut] += 1
                decision, depth = certify_window(coefficients, Fraction(6, 5), Fraction(13, 10), 9)
                depths[decision, depth] += 1
                if decision == "inside":
                    assert sign == 1
                    low, high, narrow_depth = check_hit(trace, coefficients, exponents, a)
                    hits.append((low, high, cut, a, exponents, coefficients[:n+2], narrow_depth))
    assert tuple(cut_units[r] for r in range(1, n)) == (8, 4, 4, 2, 16)
    assert tuple(cut_atoms[r] for r in range(1, n)) == (13, 9, 11, 5, 64)
    assert set((row[4], row[3]) for row in hits) == set(HIT_WINDOWS)
    assert sum(depths.values()) == len(inputs) == 102 and len(hits) == 4
    print(f"Original atoms: {2 * 3**(n-1) * 7}; conditioned: {len(inputs)}; hits: {len(hits)}")
    print("Signed units by cut:", dict(sorted(cut_units.items())))
    print("Endpoint survivors by cut:", dict(sorted(cut_atoms.items())))
    print("Whole-measure decisions by depth:", dict(sorted(depths.items())))
    for result in sorted(hits):
        print("Hit (lower, upper, cut, a, exponents, prefix, depth):", result)
    assert signature_image(13) == (6, [1, 2, 3, 4, 5])
    assert signature_image(29) == (11, [4, 7, 9])
    print("Conductor 29 signature rank and attainable cuts:", signature_image(29))


if __name__ == "__main__":
    run()
