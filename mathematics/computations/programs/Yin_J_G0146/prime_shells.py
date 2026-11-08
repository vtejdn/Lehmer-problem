"""Complete signed circular-unit boxes below the strict whole-measure threshold 6/5."""

from collections import Counter
from itertools import product
from math import comb, isqrt
from time import perf_counter
import argparse

from sympy import Poly, cyclotomic_poly
from shell import graeffe, required_signatures, signature, z
from trace_control import SOURCE_HALF


def reduce_word(word):
    """Use 1 + zeta + ... + zeta^(p-1) = 0 to remove both terms at +/-n."""
    offset = word[len(word)//2]
    return tuple(x - offset for x in word)


def multiply(left, right):
    p = len(left)
    out = [0] * p
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                out[(i+j) % p] += a*b
    return reduce_word(out)


def unit_word(p, j, exponent_sign):
    # For a modular inverse h of j, sin(jh theta)/sin(j theta) inverts u_j.
    h, w = (j, 1) if exponent_sign == 1 else (pow(j, -1, p), j)
    word = [0]*p
    for l in range(h):
        word[(w*(h-1-2*l)) % p] += 1
    return reduce_word(word)


def signed_units(p, bound):
    n = p//2
    one = (1,) + (0,)*(p-1)
    exponents = range(-bound, bound+1)
    units = {}
    for j in range(2, n+1):
        units[j, 0] = one
        for sign in (-1, 1):
            unit = unit_word(p, j, sign)
            for k in range(1, bound+1):
                units[j, sign*k] = multiply(units[j, sign*(k-1)], unit)
        assert multiply(units[j, 1], units[j, -1]) == one
    parity_choices = [tuple(e for e in exponents if e % 2 == b) for b in (0, 1)]
    cuts = required_signatures(p)
    columns = [signature(p, j) for j in range(2, n+1)]
    full = (1 << n) - 1

    def magnitudes(choices, j, word):
        if j > n:
            yield word
            return
        for e in choices[j-2]:
            yield from magnitudes(choices, j+1, multiply(word, units[j, e]) if e else word)

    for parity in product((0, 1), repeat=n-1):
        unit_mask = 0
        for bit, column in zip(parity, columns):
            if bit:
                unit_mask ^= column
        choices = [parity_choices[b] for b in parity]
        for sign, mask in [(1, unit_mask), (-1, unit_mask ^ full)]:
            if mask in cuts:
                for word in magnitudes(choices, 2, one):
                    yield cuts[mask], tuple(sign*x for x in word)


def lift(p, word, a):
    n = p//2
    values = [1, 1-a] + [2-a]*(p-2) + [1-a, 1]
    for j in range(1-n, n):
        values[n+1+j] += word[abs(j)]
    return values


def check_controls(p, bound):
    if p == 19 and bound >= 2:
        exponents = (-1, 0, 0, -1, -1, 0, -1, 2)
        cut = 5
        expected = Poly(cyclotomic_poly(20, z)*cyclotomic_poly(21, z), z)
    elif p == 29:
        exponents = (-1, -1, 0, 0, 1, 1, -1, 1, 0, 0, -1, 0, 0)
        cut = 7
        source = SOURCE_HALF + SOURCE_HALF[-2::-1]
        core = Poly.from_list([(-1)**k*v for k, v in enumerate(source)], z)
        expected = core*Poly(cyclotomic_poly(12, z)*cyclotomic_poly(20, z), z)
    else:
        return
    word = (1,) + (0,)*(p-1)
    mask = 0
    for j, exponent in enumerate(exponents, 2):
        if exponent:
            unit = unit_word(p, j, 1 if exponent > 0 else -1)
            for _ in range(abs(exponent)):
                word = multiply(word, unit)
            if exponent % 2:
                mask ^= signature(p, j)
    n = p//2
    c_left = word[0] + 2*sum((-1)**j*word[j] for j in range(1, n))
    assert required_signatures(p)[mask] == cut and (-1)**n*c_left < 4
    assert Poly.from_list(lift(p, word, 2), z) == expected


def classify(values, power_limits, norm_limits):
    # For a reciprocal polynomial with M <= R the k-th power sum has absolute
    # value <= D-2 + R^k + R^(-k). Integer parts are safe for strict exclusion.
    sums = [0]
    for k in range(1, len(power_limits)):
        sk = -k*values[k] - sum(values[j]*sums[k-j] for j in range(1, k))
        if abs(sk) > power_limits[k]:
            return "above by Newton"
        sums.append(sk)
    original = values
    for h, (coefficient_max, a_square, b_square) in enumerate(norm_limits):
        if any(abs(v) > limit for v, limit in zip(values, coefficient_max)):
            return "above by Graeffe"
        if sum(v*v for v in values)*b_square < a_square:
            poly = Poly.from_list(original, z)
            factors = poly.factor_list()[1]
            if all(factor.is_cyclotomic for factor, _ in factors):
                return "neutral"
            return "positive hit"
        if h+1 < len(norm_limits):
            values = graeffe(values)
    raise ArithmeticError(f"Unresolved strict threshold for {original}")


def census(p, bound):
    if p < 5 or any(p % j == 0 for j in range(2, isqrt(p)+1)) or bound < 1:
        raise ValueError("An odd prime >= 5 and an exponent bound >= 1 are required")
    check_controls(p, bound)
    n, degree = p//2, p+1
    power_limits = [0]
    for k in range(1, n+2):
        u, v = 6**k, 5**k
        power_limits.append(degree-2+(u*u+v*v)//(u*v))
    norm_limits = []
    binomials = [comb(degree, j) for j in range(degree+1)]
    for h in range(15):
        power = 1 << h
        u, v = 6**power, 5**power
        norm_limits.append(([b*u//v for b in binomials], u*u, v*v))
    counts = Counter()
    units_by_cut, atoms_by_cut = Counter(), Counter()
    positive_polynomials = []
    for r, word in signed_units(p, bound):
        units_by_cut[r] += 1
        c_left = word[0]+2*sum((-1)**j*word[j] for j in range(1, n))
        # Q(-2)/B(-2) < 0, with B(-2) = (-1)^n.
        first_a = max(-10, (-1)**n*c_left-1)
        for a in range(first_a, 7):
            atoms_by_cut[r] += 1
            values = lift(p, word, a)
            decision = classify(values, power_limits, norm_limits)
            counts[decision] += 1
            if decision == "positive hit":
                positive_polynomials.append((r, a, values[:n+2]))
    raw = 2 * (2*bound+1)**(n-1) * 17
    return raw, units_by_cut, atoms_by_cut, counts, positive_polynomials


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prime", type=int)
    parser.add_argument("bound", type=int)
    args = parser.parse_args()
    start = perf_counter()
    raw, signed, atoms, outcomes, hits = census(args.prime, args.bound)
    print(f"p={args.prime}, |exponent| <= {args.bound}, -10 <= a <= 6; {raw} raw atoms")
    print("Units before endpoint test:", sum(signed.values()), dict(sorted(signed.items())))
    print("Conditioned atoms:", sum(atoms.values()), dict(sorted(atoms.items())))
    print("Whole-measure classes:", dict(sorted(outcomes.items())))
    for hit in hits:
        print("Positive hit (cut, a, coefficient prefix):", hit)
    print(f"Elapsed seconds: {perf_counter()-start:.3f}")
