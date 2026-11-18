"""Test the first four admissible square offsets in each of four quartic families."""

from math import gcd, isqrt

from flint import fmpz_poly, nmod_poly


X = fmpz_poly([0, 1])
EXPONENTS = (5, 7, 9, 11)
PRIMES = (3, 2, 5, 7, 11, 13, 17, 19, 23, 29, 31)


def offsets(a):
    c = isqrt(a**3)
    selected = []
    while len(selected) < 4:
        if c % 2 and c*c >= a**3 and gcd(a, c) == 1:
            selected.append(c)
        c += 1
    return selected


def trace_core(a, b):
    parent = 1 + X**a - X**(4*a) + X**b * (X**(4*a) + X**(3*a) - 1)
    core = parent
    orders = []
    for order in (2, 4, 6, 10, 14, 18, 24):
        cyclotomic = fmpz_poly.cyclotomic(order)
        quotient, remainder = divmod(core, cyclotomic)
        if not remainder:
            orders.append(order)
            core = quotient
            if not core % cyclotomic:
                raise ArithmeticError("Repeated cyclotomic factor")
    n = core.degree() // 2
    if core.degree() != 2*n or core.coeffs() != core.coeffs()[::-1]:
        raise ArithmeticError("Invalid reciprocal core")
    trace = fmpz_poly([core[n]])
    old, current = fmpz_poly([2]), X
    for j in range(1, n+1):
        trace += core[n+j] * current
        old, current = current, X*current-old
    if trace(2) != 1 or trace(-2) != (b-6*a)//(5 if 10 in orders else 1):
        raise ArithmeticError("Unexpected trace endpoints")
    if b+2*a <= parent.degree()-core.degree():
        raise ArithmeticError("No circle root has been certified in the core")
    return core, trace, orders


def attainable_degrees(coefficients, p):
    polynomial = nmod_poly(coefficients, p)
    leading, factors = polynomial.factor()
    reconstruction = nmod_poly([int(leading)], p)
    bits = 1
    signature = []
    for factor, exponent in factors:
        reconstruction *= factor**exponent
        signature.append((factor.degree(), exponent))
        for _ in range(exponent):
            bits |= bits << factor.degree()
    if reconstruction != polynomial:
        raise ArithmeticError("Incomplete modular factorization")
    return bits, signature


def count_odd_divisors(signature, cutoff):
    """Count monic divisor polynomials, respecting repeated modular factors."""
    counts = [1] + [0]*cutoff
    for deg, exponent in signature:
        previous = counts.copy()
        for e in range(1, min(exponent, cutoff//deg)+1):
            offset = e*deg
            for j in range(offset, cutoff+1):
                counts[j] += previous[j-offset]
    return sum(counts[1::2])


def test_direction(a, c):
    b = 6*a + c*c
    core, trace, orders = trace_core(a, b)
    n = trace.degree()
    coefficients = [int(t) for t in trace.coeffs()]
    proper = (1 << n)-2  # All degrees from 1 to n-1.
    odd_small = sum(1 << j for j in range(1, n, 2) if a*j < b)
    odd_eliminator = None
    for index, p in enumerate(PRIMES):
        possible, signature = attainable_degrees(coefficients, p)
        proper &= possible
        if index == 0:
            small = (odd_small & possible).bit_count()
            divisors = count_odd_divisors(signature, min(n-1, (b-1)//a))
        if odd_eliminator is None and not (proper & odd_small):
            odd_eliminator = p
        if not proper:
            if (a, c) == (5, 13):
                leading, factors = core.factor()
                if leading != 1 or factors != [(core, 1)]:
                    raise ArithmeticError("The independent integer factorization disagrees")
            return b, n, orders, small, divisors, odd_eliminator, p, [core.degree()]
    _, factors = core.factor()
    reconstruction = fmpz_poly([1])
    degrees = []
    for f, e in factors:
        reconstruction *= f**e
        degrees.extend([f.degree()]*e)
    if reconstruction != core:
        raise ArithmeticError("Incomplete rational factorization")
    if len(degrees) > 1:
        print("RATIONAL SPLIT", a, c, b, degrees, flush=True)
    return b, n, orders, small, divisors, odd_eliminator, 0, sorted(degrees)


def main():
    print("a c b n cyclotomic_orders mod3_degrees mod3_divisors odd_last full_last core_degrees")
    for a in EXPONENTS:
        for c in offsets(a):
            b, n, orders, small, divisors, odd_last, p, degrees = test_direction(a, c)
            print(a, c, b, n, orders, small, divisors, odd_last or "-", p or "Q", degrees,
                  flush=True)


if __name__ == "__main__":
    main()
