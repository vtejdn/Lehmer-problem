"""Search all trace grids by integral reciprocal power sums and the exact pole."""

from argparse import ArgumentParser
from collections import Counter
from math import comb

from lobatto_digits import combine


def residue_digit(q, degree, prefix, norm):
    """Residue of the next reciprocal coefficient mod q(q+1) at fixed degree."""
    j = len(prefix)
    residues = []
    for b in (q, -q-1):
        base = abs(b)
        place = base**j
        modulus = base * place
        x = (b * pow(1+b, -1, modulus)) % modulus
        value = 0
        for coefficient in reversed(prefix):
            value = (value*x + coefficient) % modulus
        unit = pow(1+b, degree, modulus)
        diff = (norm-unit*value) % modulus
        if diff % place:
            raise ArithmeticError("Incompatible prefix")
        slope = unit * pow(x, j, modulus) // place
        residues.append((diff // place) * pow(slope, -1, base) % base)
    return combine(*residues, q)


def trace_polynomial(reciprocal, n):
    """Recover descending trace coefficients from the low reciprocal half."""
    ordinary = []
    for j, coefficient in enumerate(reciprocal):
        previous = sum(c * (-1)**(j-i) * comb(2*(n-i), j-i)
                       for i, c in enumerate(ordinary))
        ordinary.append(coefficient - previous)
    return ordinary


def has_signature(coefficients, q):
    """Exact Sturm counts with endpoint and squarefreeness checks."""
    from sympy import Poly, Rational, Symbol
    x = Symbol("x")
    H = Poly.from_list(coefficients, gens=x)
    h = Rational(1, q*(q+1))
    return (H.eval(-4) != 0 and H.eval(0) != 0 and H.eval(h) != 0
            and H.gcd(H.diff()).degree() == 0
            and H.count_roots(-4, 0) == H.degree()-1 and H.count_roots(0, h) == 1)


def search(q, n, depth, *, norm=None):
    if q < 2 or n < 2 or depth < 1:
        raise ValueError("Require q,n>=2 and depth>=1")
    modulus = q*(q+1)
    target = 4*modulus+1 if norm is None else norm
    if target <= 0 or (target-1) % modulus:
        raise ValueError("Require a positive norm congruent to 1 mod M")
    states = [((1,), ())]
    for j in range(1, min(n, depth)+1):
        denominator = modulus**j
        center = q**(2*j) + (q+1)**(2*j)
        # The exterior pair contributes more than two at every positive pole.
        lower = 3 - 2*(n-1)
        if target < modulus**2:
            lower = max(lower, (center - (2*(n-1)+1)*denominator) // denominator + 1)
        upper = (center + 2*(n-1)*denominator - 1) // denominator
        # The nonzero integral resultants at both signs of unity bound the mean.
        # This optional test is valid for the first nonunit target (irreducible Salem lift).
        if target == 4*modulus+1:
            scale = q*denominator
            lo = q*center - ((n+2)*q+j)*denominator
            hi = q*center + ((n+1)*q+j)*denominator
            lower = max(lower, lo//scale+1)
            upper = min(upper, (hi-1)//scale)
        next_states = []
        for prefix, moments in states:
            residue = residue_digit(q, 2*n, prefix, target)
            known = -sum(c*s for c, s in zip(prefix[1:], reversed(moments)))
            first = lower + (known - j*residue - lower) % (j*modulus)
            for moment in range(first, upper+1, j*modulus):
                digit = (known-moment)//j
                next_states.append(((*prefix, digit), (*moments, moment)))
        states = next_states
        if not states:
            return j, []
    if depth < n:
        return None, states
    witnesses = []
    for prefix, _ in states:
        H = trace_polynomial(prefix, n)
        if sum(c * modulus**i for i, c in enumerate(H)) == target and has_signature(H, q):
            witnesses.append(H)
    return n+1, witnesses


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("q", type=int)
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int)
    parser.add_argument("--depth", type=int, default=12)
    parser.add_argument("--norm", type=int)
    args = parser.parse_args()
    failures = Counter()
    pending = []
    for degree in range(args.minimum, args.maximum+1):
        where, states = search(args.q, degree, args.depth, norm=args.norm)
        if where is None:
            pending.append((degree,len(states)))
        elif states:
            print(f"witnesses n={degree} H={states}")
        else:
            failures[where] += 1
    print("excluded by stage:", sorted(failures.items()))
    if pending:
        print(f"degrees still open at the requested depth: {len(pending)}; first {pending[:8]}")
