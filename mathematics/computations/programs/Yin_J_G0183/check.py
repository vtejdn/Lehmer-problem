"""Verify the section census in trace coordinates and check the torsion obstruction."""

from argparse import ArgumentParser
from collections import Counter
import json
from math import gcd, lcm
from pathlib import Path

import sympy as sp
from flint import fmpq, fmpz_poly, nmod_poly


X = fmpz_poly([0, 1])
ONE = fmpz_poly([1])
A_COEFFICIENTS = (1, 7, 10, -7, 1)


def section_trace(k, ell):
    """Build the trace directly from the centered terms, including collisions."""
    weights = Counter()
    for j, coefficient in enumerate(A_COEFFICIENTS):
        weights[abs(ell + (j - 2) * k)] += coefficient
    trace = ONE + 2 * weights[0]
    previous, current = 2 * ONE, X
    for j in range(1, ell + 2 * k + 1):
        if j in weights:
            trace += weights[j] * current
        previous, current = current, X * current - previous
    return trace


def coefficients(k, ell):
    values = [0] * (2 * ell + 4 * k + 1)
    values[ell + 2 * k] = 1
    for j, value in enumerate(A_COEFFICIENTS):
        values[2 * ell + j * k] += value
        values[(4 - j) * k] += value
    return values


def modular_degrees(trace, primes):
    """Exclude rational factor degrees using subset sums of modular factor degrees."""
    cap = trace.degree() // 2
    mask = (1 << (cap + 1)) - 1
    possible = mask ^ 1
    coeff = [int(c) for c in trace.coeffs()]
    for prime in primes:
        _, parts = nmod_poly(coeff, prime).factor()
        attainable = 1
        for factor, exponent in parts:
            for _ in range(exponent):
                attainable = (attainable | (attainable << factor.degree())) & mask
        possible &= attainable
        if not possible:
            return True
    return False


def interior_sign_change(trace):
    """Find a real embedding where the quadratic lift has negative discriminant."""
    for level in range(10):
        denominator = 2 ** level
        last = trace(-2)
        for numerator in range(-2 * denominator + 1, 2 * denominator + 1):
            value = trace(fmpq(numerator, denominator))
            if value * last < 0:
                return True
            if value:
                last = value
    return False


def check_sample_signature(k, ell, trace, factor):
    """Recount the real intervals for three controls with SymPy's exact root counter."""
    if (k, ell) not in {(1, 2), (7, 19), (23, 24)}:
        return
    t = sp.Symbol("t")
    poly = sp.Poly.from_list([int(c) for c in reversed(trace.coeffs())], t)
    negative = int(poly.count_roots(-sp.oo, -2))
    middle = int(poly.count_roots(-2, 2))
    positive = int(poly.count_roots(2, sp.oo))
    exterior = trace.degree() - middle
    if (negative, 2 * middle, positive, exterior) != (
        factor["negative_real_exterior"], factor["unit_circle"],
        factor["positive_real_exterior"], factor["exterior"],
    ):
        raise ArithmeticError(f"exact root-count disagreement for {(k, ell)}")


def verify_census(rows, limit):
    primes = list(map(int, sp.primerange(2, limit + 1)))
    methods = Counter()
    expected = {(k, ell) for k in range(1, 51) for ell in range(k + 1, 151)
                if 4 * k + 2 * ell <= 300 and gcd(k, ell) == 1}
    expected.update((k, k * k + 1) for k in (13, 17, 19, 23, 29, 31))
    actual = [(r["k"], r["ell"]) for r in rows]
    if set(actual) != expected or len(actual) != len(expected):
        raise ArithmeticError("the census does not contain the stated directions exactly once")
    for row in rows:
        k, ell = row["k"], row["ell"]
        if len(row["core"]) != 1 or row["torsion"]:
            raise ArithmeticError(f"expected a single factor for {(k, ell)}")
        factor = row["core"][0]
        trace = section_trace(k, ell)
        if factor["coefficients"] != coefficients(k, ell):
            raise ArithmeticError(f"the reported factor differs from the section at {(k, ell)}")
        if factor["degree"] != 2 * trace.degree() or factor["mult"] != 1:
            raise ArithmeticError(f"wrong lift degree or multiplicity at {(k, ell)}")
        exterior = factor["exterior"]
        if (2 * exterior + factor["unit_circle"] != factor["degree"] or
                exterior != factor["negative_real_exterior"] + factor["positive_real_exterior"]
                + 2 * factor["nonreal_exterior_pairs"]):
            raise ArithmeticError(f"inconsistent signature at {(k, ell)}")
        check_sample_signature(k, ell, trace, factor)
        if not interior_sign_change(trace):
            raise ArithmeticError(f"no rational sign witness for {(k, ell)}")
        if modular_degrees(trace, primes):
            methods["modular_trace"] += 1
        else:
            content, parts = trace.factor()
            if content != 1 or parts != [(trace, 1)]:
                raise ArithmeticError(f"trace splits at {(k, ell)}")
            methods["integer_trace"] += 1
    return methods


def torsion():
    u, v = sp.symbols("u v")
    a = (u**2 - 3*u - 1) * (u**2 - 4*u - 1)
    ar = (1 - 3*u - u**2) * (1 - 4*u - u**2)
    curve = a * v**2 + u**2 * v + ar
    primes = (2, 2, 17, 2, 17, 5, 3, 2, 5, 17, 3)
    for order, prime in enumerate(primes, start=1):
        resultant = sp.Poly(sp.resultant(curve, sp.cyclotomic_poly(order, v), v), u)
        degree = resultant.degree()
        multiple = lcm(*(m for m in range(1, 2 * degree**2 + 1) if sp.totient(m) <= degree))
        reduction = nmod_poly([int(c) for c in resultant.all_coeffs()[::-1]], prime)
        x = nmod_poly([0, 1], prime)
        if not reduction or reduction.degree() < 1 or (pow(x, multiple, reduction) - 1).gcd(reduction).degree() != 0:
            raise ArithmeticError(f"torsion gcd failed at order {order}")
        print(order, degree, multiple, prime)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--torsion", action="store_true")
    parser.add_argument("--prime-limit", type=int, default=43)
    args = parser.parse_args()
    if args.torsion:
        torsion()
        return
    group = Path(__file__).resolve().parent
    output = group.parents[1] / "outputs" / group.name / "census.json"
    print(dict(verify_census(json.loads(output.read_bytes()), args.prime_limit)))


if __name__ == "__main__":
    main()
