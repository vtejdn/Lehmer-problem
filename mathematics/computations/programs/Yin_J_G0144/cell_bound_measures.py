"""Classify the full Mahler measures of all short mutations passing the real signs."""

from collections import Counter
from math import comb

from cell_bound_short import main as enumerate_mutations
from pilot import graeffe, monic_quotient
from trace64_cell import N, RHO


DEGREE = 2*N
TARGET = RHO**2
MAX_SQUARINGS = 14
LEHMER = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1)


def cyclotomics():
    # phi(m)^2 >= m/2. Divisors e|m of eligible orders also have phi(e)<=DEGREE.
    limit = 2*DEGREE**2
    totient = list(range(limit+1))
    for prime in range(2, limit+1):
        if totient[prime] == prime:
            for multiple in range(prime, limit+1, prime):
                totient[multiple] -= totient[multiple]//prime
    polys = {}
    for m in range(1, limit+1):
        if totient[m] > DEGREE:
            continue
        poly = [-1] + [0]*(m-1) + [1]
        for e, phi in polys.items():
            if m%e == 0:
                poly = monic_quotient(poly, phi)
                assert poly is not None
        assert len(poly) == totient[m]+1
        polys[m] = poly
    return polys


def strip_cyclotomics(poly, polys):
    rest = list(poly)
    removed = []
    for order, phi in polys.items():
        while len(rest) >= len(phi):
            quotient = monic_quotient(rest, phi)
            if quotient is None:
                break
            rest = quotient
            removed.append(order)
    return rest, removed


def compare_threshold(poly):
    # Operate on the entire degree-64 polynomial, including neutral factors.
    num, den = TARGET.numerator, TARGET.denominator
    for step in range(MAX_SQUARINGS+1):
        if den**2 * sum(a*a for a in poly) < num**2:
            return "positive_hit", step
        if any(den*abs(a) > num*comb(DEGREE,k) for k,a in enumerate(poly)):
            return "above", step
        if step < MAX_SQUARINGS:
            poly = graeffe(poly)
            num *= num
            den *= den
    return "undecided", MAX_SQUARINGS


def lehmer_divisors(core):
    divisors = []
    for k in range(1, (len(core)-1)//10+1):
        for sign in (-1, 1):
            lift = [0]*(10*k+1)
            for j, a in enumerate(LEHMER):
                lift[k*j] = a*sign**j
            if monic_quotient(core, lift) is not None:
                divisors.append((sign, k))
    return divisors


def main():
    polys = cyclotomics()
    census = Counter()
    deepest = 0
    def inspect(mutation, free):
        nonlocal deepest
        half = free + [1]
        poly = half[:0:-1] + half
        assert len(poly) == DEGREE+1 and poly == poly[::-1] and poly[0] == 1
        core, removed = strip_cyclotomics(poly, polys)
        if core == [1]:
            outcome = "cyclotomic"
        else:
            # By Kronecker a nonconstant remainder has positive logarithmic measure.
            outcome, step = compare_threshold(poly)
            deepest = max(deepest, step)
            if outcome == "positive_hit":
                print("positive_hit", mutation, "full polynomial (ascending)", poly,
                      "cyclotomic orders", removed, "core (ascending)", core,
                      "L(sign*x^k) divisors (sign,k)", lehmer_divisors(core))
            elif outcome == "undecided":
                print("undecided", mutation, "full polynomial (ascending)", poly)
        census[len(mutation), outcome] += 1
    enumerate_mutations(on_sign_survivor=inspect)
    keys = ("cyclotomic", "positive_hit", "above", "undecided")
    print("Categories:", *keys)
    for weight in range(6):
        print("support", weight, *(census[weight,k] for k in keys))
    print("total", *(sum(census[w,k] for w in range(6)) for k in keys))
    print("maximum Graeffe steps used", deepest)


if __name__ == "__main__":
    main()
