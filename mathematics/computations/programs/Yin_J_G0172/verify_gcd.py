"""Check every direction by a polynomial gcd with the squarefree correction."""

from math import gcd, isqrt

from flint import nmod_poly


def residual_polynomial(p):
    z = nmod_poly([0, 1], p * p)
    zp = z**p
    g = z**3 - z - 1
    b = 1 - z**2 - z**3
    numerator = (zp**3 - zp - 1) * b**p - g**p * (1 - zp**2 - zp**3)
    coefficients = [int(value) for value in numerator]
    assert all(value % p == 0 for value in coefficients)
    h = nmod_poly([value // p for value in coefficients], p)
    assert h[1] == 1

    t = nmod_poly([0, 1], p)
    radical = nmod_poly([1], p)
    for block, _ in h.factor_squarefree()[1]:
        radical *= block
    assert radical.gcd(radical.derivative()) == 1
    assert h % radical == 0 and pow(radical, h.degree(), h) == 0

    # Construct each cyclotomic polynomial from all of its proper divisors.
    cyclotomics = {}
    orders = (1, 2, 3, 5, 8, 12, 18, 30)
    for m in range(1, max(orders) + 1):
        if any(j % m == 0 for j in orders):
            value = t**m - 1
            for d, factor in cyclotomics.items():
                if m % d == 0:
                    value = value // factor
            cyclotomics[m] = value
    g = t**3 - t - 1
    b = 1 - t**2 - t**3
    excluded = t * g * b
    for j in orders:
        excluded *= cyclotomics[j]
    return radical // radical.gcd(excluded), t, g, b


def degree_sums(p):
    modulus, t, g, b = residual_polynomial(p)
    if modulus.degree() == 0:
        return {}
    one, inverse, _ = b.xgcd(modulus)
    assert one == 1
    f = (-g * inverse) % modulus
    limit = 270 // p
    difference = 2858
    t_powers = [nmod_poly([1], p)]
    for _ in range(3 * limit + difference):
        t_powers.append(t * t_powers[-1] % modulus)
    f_power = nmod_poly([1], p)
    result = {}
    for a in range(1, max(limit, (difference + limit) // 3) + 1):
        f_power = f * f_power % modulus
        last_b = 3 * a + difference if a <= limit else limit
        for exponent in range(max(1, 3 * a - difference), last_b + 1):
            if gcd(a, exponent) == 1:
                degree = modulus.gcd(t_powers[exponent] - f_power).degree()
                if degree:
                    result[a, exponent] = degree
    return result


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Use Python without optimization to check the radical.")
    for prime in range(11, 132):
        if all(prime % d for d in range(2, isqrt(prime) + 1)):
            totals = degree_sums(prime)
            print(prime, len(totals), max(totals.values(), default=0), flush=True)
