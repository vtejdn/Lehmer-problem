"""Find the least good prime excluding short odd degrees in each J176 trace."""

from math import isqrt

from flint import nmod_poly

from diagnostic import EXPONENTS, attainable_degrees, offsets, trace_core


LIMIT = 199


def least_witness(a, c, primes):
    b = 6*a + c*c
    _, trace, _ = trace_core(a, b)
    coeffs = [int(value) for value in trace.coeffs()]
    if trace.degree() % 2 != 1:
        raise ArithmeticError("The sample requires an odd total trace degree")
    bad = []
    failed = []
    for p in primes:
        reduction = nmod_poly(coeffs, p)
        if reduction.gcd(reduction.derivative()).degree() > 0:
            bad.append(p)
            continue
        possible, signature = attainable_degrees(coeffs, p)
        smallest = min(deg for deg, exponent in signature if deg % 2)
        odd_divisor_degree = next(j for j in range(1, trace.degree()+1, 2)
                                  if (possible >> j) & 1)
        if smallest != odd_divisor_degree:
            raise ArithmeticError("Odd irreducible and subset minima disagree")
        if a*smallest >= b:
            return p, smallest, bad, failed
        failed.append((p, smallest))
    return None, None, bad, failed


def main():
    primes = [p for p in range(2, LIMIT+1)
              if all(p % j for j in range(2, isqrt(p)+1))]
    print("a c b least_prime least_odd_degree bad_primes earlier_good_primes_and_minima")
    for a in EXPONENTS:
        for c in offsets(a):
            p, smallest, bad, failed = least_witness(a, c, primes)
            print(a, c, 6*a+c*c, p, smallest, bad, failed, flush=True)


if __name__ == "__main__":
    main()
