"""Exact dyadic lifting for the primitive cubic directions in L462v172."""

from math import comb, gcd


def binary_remainder(value, modulus):
    while value.bit_length() >= modulus.bit_length():
        value ^= modulus << (value.bit_length() - modulus.bit_length())
    return value


def binary_gcd(left, right):
    while right:
        left, right = right, binary_remainder(left, right)
    return left


def binary_product(left, right, modulus):
    value = 0
    while right:
        if right & 1:
            value ^= left
        left <<= 1
        right >>= 1
    return binary_remainder(value, modulus)


def binary_power(base, exponent, modulus):
    value = 1
    while exponent:
        if exponent & 1:
            value = binary_product(value, base, modulus)
        base = binary_product(base, base, modulus)
        exponent >>= 1
    return value


def signed_terms(a, b):
    return ((3*a, 1), (a, -1), (0, -1), (b, 1), (b+2*a, -1), (b+3*a, -1))


def binary_derivative(terms, modulus):
    value = 0
    for exponent, coefficient in terms:
        if exponent % 2 and coefficient % 2:
            value ^= binary_power(2, exponent-1, modulus)
    return value


def universal_orbit():
    # The two irreducible reciprocal factors of the Lehmer polynomial modulo 2.
    quintic = 0b101111
    powers = [binary_power(2, n, quintic) for n in range(31)]
    assert len(set(powers)) == 31
    g = powers[3] ^ powers[1] ^ 1
    reverse_g = 1 ^ powers[2] ^ powers[3]
    exponent = (powers.index(g) - powers.index(reverse_g)) % 31
    lehmer = sum(1 << j for j in (0, 1, 3, 4, 5, 6, 7, 9, 10))
    reciprocal = int(f"{quintic:b}"[::-1], 2)
    assert binary_product(quintic, reciprocal, 1 << 11) == lehmer
    return lehmer, exponent


def orbit_at_x(a, lehmer):
    # The powers of x are reduced using x^31 = 1 before taking the gcd.
    substituted = 0
    for j in range(11):
        if (lehmer >> j) & 1:
            substituted ^= 1 << ((j*a) % 31)
    orbit = binary_gcd(substituted, (1 << 31) | 1)
    assert orbit.bit_length() == 11
    return orbit


def correction_multiplier(orbit, terms):
    degree = orbit.bit_length() - 1
    derivative = binary_derivative(terms, orbit)
    assert binary_gcd(derivative, orbit) == 1
    inverse = binary_power(derivative, 30, orbit)
    assert binary_product(inverse, derivative, orbit) == 1
    orbit_terms = [(j, (orbit >> j) & 1) for j in range(degree+1)]
    return binary_product(binary_derivative(orbit_terms, orbit), inverse, orbit)


def multiply_mod(left, right, divisor, mask):
    degree = len(divisor)
    product = [0] * (2*degree-1)
    for i, coefficient in enumerate(left):
        if coefficient:
            for j, other in enumerate(right):
                product[i+j] += coefficient * other
    for j in range(len(product)-1, degree-1, -1):
        leading = product[j] & mask
        if leading:
            for index, coefficient in enumerate(divisor):
                product[j-degree+index] -= leading * coefficient
    return [coefficient & mask for coefficient in product[:degree]]


def sparse_remainder(terms, divisor, mask):
    degree = len(divisor)
    one = [1] + [0] * (degree-1)
    powers = [[0, 1] + [0] * (degree-2)]
    for _ in range(1, max(j for j, _ in terms).bit_length()):
        powers.append(multiply_mod(powers[-1], powers[-1], divisor, mask))
    total = [0] * degree
    for exponent, coefficient in terms:
        value = one
        for index in range(exponent.bit_length()):
            if (exponent >> index) & 1:
                value = multiply_mod(value, powers[index], divisor, mask)
        for index, element in enumerate(value):
            total[index] += coefficient * element
    return [element & mask for element in total]


def lift_candidate(orbit, terms, counts):
    correction = correction_multiplier(orbit, terms)
    degree = orbit.bit_length() - 1
    divisor = [(orbit >> j) & 1 for j in range(degree)]
    modulus = 2
    for stage in range(len(counts)):
        next_modulus = 2*modulus
        residual = sparse_remainder(terms, divisor, next_modulus-1)
        assert all(value in (0, modulus) for value in residual)
        bits = sum((value // modulus) << j for j, value in enumerate(residual))
        update = binary_product(bits, correction, orbit)
        divisor = [value + modulus*((update >> j) & 1) for j, value in enumerate(divisor)]
        modulus = next_modulus
        if (1 + sum(divisor)) % modulus not in (1, modulus-1):
            return None
        counts[stage] += 1
    coefficients = [value if 2*value < modulus else value-modulus for value in divisor] + [1]
    return coefficients


def divides_over_integers(terms, divisor):
    degree = len(divisor)-1
    dividend = [0] * (max(j for j, _ in terms)+1)
    for j, coefficient in terms:
        dividend[j] += coefficient
    for j in range(len(dividend)-1, degree-1, -1):
        leading = dividend[j]
        if leading:
            for index, coefficient in enumerate(divisor[:-1]):
                dividend[j-degree+index] -= leading * coefficient
    return not any(dividend[:degree])


def check_known_factor(lehmer):
    divisor = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
    terms = [(j+shift, coefficient) for j, coefficient in enumerate(divisor)
             for shift in (0, 1)]
    assert lift_candidate(lehmer, terms, [0]*10) == divisor
    assert divides_over_integers(terms, divisor)
    assert not divides_over_integers(terms + [(0, 2048)], divisor)


def main():
    lehmer, exponent = universal_orbit()
    check_known_factor(lehmer)
    print("Exponent of f(t) on the order-31 orbits:", exponent)
    orbits = {a: orbit_at_x(a, lehmer) for a in range(1, 31)}
    counts = [0] * 10
    pairs = 0
    survivors = []
    for a in range(1, 438):
        for difference in range(-218, 219):
            b = 3*a + difference
            if b <= 0 or gcd(a, b) != 1 or (b-exponent*a) % 31:
                continue
            pairs += 1
            terms = signed_terms(a, b)
            candidate = lift_candidate(orbits[a % 31], terms, counts)
            if candidate and divides_over_integers(terms, candidate):
                assert candidate == candidate[::-1]
                assert all(value**2 <= 8*comb(10, j)**2 for j, value in enumerate(candidate))
                survivors.append((a, b, candidate))
    print("Primitive pairs satisfying the congruence:", pairs)
    print("Endpoint survivors at moduli 4 through 2048:", counts)
    print("Exact reciprocal divisors (coefficients in ascending order):")
    for result in survivors:
        print(result)
    print("Total:", len(survivors))


if __name__ == "__main__":
    main()
