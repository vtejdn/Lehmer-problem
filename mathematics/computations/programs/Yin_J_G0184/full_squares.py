"""Verify complete trace discriminant factorizations and their square divisors."""
from functools import cache
from math import gcd, isqrt, prod

from sympy import factorint

from trace_survey import exceptional, linear_contact, section

# Factors occur with multiplicity. Their order plays no part in verification.
FACTORS = {
    (2, 5): (67, 44987, 1612683784637),
    (2, 7): (383, 672097, 942825352167033847),
    (2, 9): (5, 5, 2610063395871287, 253445847762423683),
    (2, 11): (17, 523, 433524514050214439, 469959986258643269737),
    (2, 13): (157, 4441, 18701237, 4290420640152874429, 5171168798337212921),
    (2, 15): (443, 6531737400233, 21856422199006988043916204419737958097578599),
    (2, 17): (11, 131, 313, 91681619, 438157056168423839780689371722510730926598576217918939),
    (2, 19): (5, 5, 25169, 10464068335170973725498904365313239376016183764179786397509834856200733),
    (2, 21): (19, 19, 47, 47, 4378631, 45626261, 37518343, 127409362494149,
              3885053731405546846906573823891172135278009),
    (3, 7): (3, 3, 17179638680986458549885332737),
    (3, 10): (5, 580848722154281719, 45846024861468220512023),
    (3, 13): (19, 1511, 48259, 6344761, 27081604978898828065204553218629832331),
    (3, 16): (5, 5, 449, 782072148511963380763, 91280512040131155286530541449224008032631),
    (3, 19): (11, 11, 13, 13, 3697, 38110117, 1813912426364101136965073996018122598974619246823332041175094961),
    (4, 9): (23, 29, 41, 424421974303326345168755360968154411),
    (4, 13): (5, 5, 17, 17, 976794340980400429, 57094563204776067960621036174623393),
    (5, 11): (13, 31, 22630627, 563680733006849157983508806748884284751641),
}


@cache
def certify_prime(n):
    if n < 1_000_000:
        assert n >= 2 and all(n % j for j in range(2, isqrt(n) + 1)), n
        return
    # Only factors used in a Pocklington certificate have to be resolved.
    power_product = 1
    for q, e in sorted(factorint(n - 1).items()):
        q, e = int(q), int(e)
        assert q > 1 and e >= 1 and (n - 1) % q**e == 0
        certify_prime(q)
        for witness in range(2, 64):
            if (pow(witness, n - 1, n) == 1
                    and gcd(pow(witness, (n - 1)//q, n) - 1, n) == 1):
                break
        else:
            raise ValueError(f'missing witness for {q} in {n}-1')
        power_product *= q**e
        if power_product*power_product > n:
            assert (n - 1) % power_product == 0
            return
    raise ValueError(f'insufficient certified factors of {n}-1')


def main():
    for (k, l), factors in FACTORS.items():
        Q = section(k, l)
        delta = abs(int(Q.discriminant()))
        assert delta == prod(factors)
        B = exceptional(k, l)
        assert B
        square = coarse = refined = 1
        for p in sorted(set(factors)):
            certify_prime(p)
            e = 2*(factors.count(p)//2)
            if not e:
                continue
            square *= p**e
            if B % p == 0:
                coarse *= p**e
                refined *= p**e
                continue
            poly = Q.set_modulus(p)
            repeated = poly.gcd(poly.diff()).factor_list()[1]
            accounted = 0
            for factor, multiplicity in repeated:
                assert multiplicity == 1 and factor.degree() == 1
                z = -int(factor.TC()) % p
                b, _, split = linear_contact(Q, p, z, factors.count(p))
                accounted += b
                if b % 2 == 0:
                    coarse *= p**b
                    if split:
                        refined *= p**b
            assert accounted == factors.count(p)
        print(k, l, square, coarse, refined, max(factors).bit_length(), flush=True)


if __name__ == '__main__':
    main()
