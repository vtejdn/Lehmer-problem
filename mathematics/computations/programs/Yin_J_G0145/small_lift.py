"""Lift primitive binary blocks and apply both endpoint tests to inverse pairs."""

from argparse import ArgumentParser
from collections import Counter
from itertools import combinations


def binary_remainder(value, divisor):
    degree = divisor.bit_length()
    while value.bit_length() >= degree:
        value ^= divisor << (value.bit_length() - degree)
    return value


def binary_product(a, b):
    value = 0
    while b:
        bit = b & -b
        value ^= a << (bit.bit_length() - 1)
        b ^= bit
    return value


def inverse_mod_binary(a, divisor):
    u, v = a, divisor
    s, t = 1, 0
    while u != 1:
        assert u
        shift = u.bit_length() - v.bit_length()
        if shift < 0:
            u, v, s, t = v, u, t, s
            shift = -shift
        u ^= v << shift
        s ^= t << shift
    return binary_remainder(s, divisor)


def power_of_eight(binary):
    return sum(((binary >> j) & 1) << (8 * j) for j in range(binary.bit_length()))


def binary_blocks(prime, order):
    # In the two Mersenne cases, every degree-order irreducible has order prime.
    assert prime == 2**order - 1 and order in (3, 13)
    blocks = []
    for phi in range(2**order + 1, 2**(order + 1), 2):
        if phi.bit_count() % 2 == 0:
            continue
        power = 2
        for _ in range(order):
            power = binary_remainder(binary_product(power, power), phi)
        if power == 2:  # order is prime and neither linear factor divides phi
            blocks.append(phi)
    assert len(blocks) == (prime - 1) // order
    return blocks


def field_orbit_blocks(prime, order, field_polynomial):
    """Build each irreducible factor of Phi_p from a primitive root and Frobenius."""
    def multiply(a, b):
        return binary_remainder(binary_product(a, b), field_polynomial)

    def power(value, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = multiply(result, value)
            value = multiply(value, value)
            exponent >>= 1
        return result

    # Here the degree 41 is prime, so testing x^(2^41)=x and no linear factor
    # proves irreducibility of the specified degree-41 polynomial.
    assert order == 41 and field_polynomial.bit_length() == order + 1
    assert field_polynomial & 1 and field_polynomial.bit_count() % 2 == 1
    assert power(2, 1 << order) == 2
    field_size_minus_one = (1 << order) - 1
    assert field_size_minus_one % prime == 0
    root = power(2, field_size_minus_one // prime)
    assert root != 1 and power(root, prime) == 1
    root_powers = [1]
    for _ in range(1, prime):
        root_powers.append(multiply(root_powers[-1], root))

    visited = {0}
    blocks = []
    for starting_exponent in range(1, prime):
        if starting_exponent in visited:
            continue
        exponent = starting_exponent
        coefficients = [1]
        while exponent not in visited:
            visited.add(exponent)
            constant = root_powers[exponent]
            next_coefficients = [multiply(c, constant) for c in coefficients] + [0]
            for i, coefficient in enumerate(coefficients):
                next_coefficients[i + 1] ^= coefficient
            coefficients = next_coefficients
            exponent = 2 * exponent % prime
        assert exponent == starting_exponent and len(coefficients) == order + 1
        assert all(c in (0, 1) for c in coefficients)
        blocks.append(sum(c << i for i, c in enumerate(coefficients)))
    assert len(set(blocks)) == len(blocks) == (prime - 1) // order
    return blocks


class PackedRing:
    """Polynomial residues mod a monic integer polynomial and 2^bits."""

    def __init__(self, polynomial, bits):
        self.degree = len(polynomial) - 1
        self.mask = (1 << bits) - 1
        self.width = (4 * self.degree * (1 << (2 * bits))).bit_length() + 1
        self.coefficient_mask = self.mask * self.pack([1] * self.degree)
        # One bias per slot prevents a borrow into adjacent slots during division.
        self.bias = self.pack([1] * (2 * self.degree)) << (self.width - 1)
        self.polynomial = self.pack([c & self.mask for c in polynomial])

    def pack(self, coefficients):
        return sum(c << (self.width * j) for j, c in enumerate(coefficients))

    def unpack(self, value):
        return [(value >> (self.width * j)) & self.mask for j in range(self.degree)]

    def add(self, a, b):
        return (a + b) & self.coefficient_mask

    def multiply(self, a, b):
        residue = a * b + self.bias
        for j in range(2 * self.degree - 2, self.degree - 1, -1):
            coefficient = (residue >> (self.width * j)) & self.mask
            if coefficient:
                shift = self.width * (j - self.degree)
                residue -= (coefficient * self.polynomial) << shift
        return residue & self.coefficient_mask

    def power(self, a, exponent):
        value = 1
        while exponent:
            if exponent & 1:
                value = self.multiply(value, a)
            exponent >>= 1
            if exponent:
                a = self.multiply(a, a)
        return value

    def geometric_sum(self, a, count):
        if count == 0:
            return 1, 0
        power, total = self.geometric_sum(a, count // 2)
        total = self.multiply(total, self.add(1, power))
        power = self.multiply(power, power)
        if count % 2:
            return self.multiply(power, a), self.add(total, power)
        return power, total


def twice_polynomial(ring, prime, endpoint):
    x = ring.pack([0, 1])
    plus = ring.add(x, 1)
    minus = ring.add(x, ring.mask)
    if endpoint:
        _, fourth_sum = ring.geometric_sum(ring.multiply(ring.mask, ring.power(x, 4)), prime)
        _, second_sum = ring.geometric_sum(ring.multiply(ring.mask, ring.power(x, 2)), prime)
        a = ring.multiply(minus, fourth_sum)
        b = ring.multiply(plus, ring.power(second_sum, 2))
    else:
        # Twice D^2 H from the short P5/P6 identity. D is a primitive-block unit.
        t = ring.power(x, 2 * prime)
        a = ring.multiply(minus, ring.power(ring.add(ring.power(x, 2), 1), 2))
        a = ring.multiply(a, ring.add(ring.power(t, 2), 1))
        b = ring.multiply(plus, ring.add(ring.power(x, 4), 1))
        b = ring.multiply(b, ring.power(ring.add(t, 1), 2))
    return ring.add(ring.power(a, 2), ring.power(b, 2))


def lift_block(prime, phi, bits):
    endpoint = phi == 3
    modulus = 5 if endpoint else power_of_eight(phi)
    degree = modulus.bit_length() - 1
    coefficients = [(modulus >> j) & 1 for j in range(degree + 1)]
    if endpoint:
        inverse = 1  # Phi_p^8 == 1 mod (x+1)^2
    else:
        derivative = sum(((phi >> j) & 1) << (j - 1) for j in range(1, phi.bit_length(), 2))
        # Phi_p/phi = (x(x+1) phi')^(-1) mod phi. Its eighth power is needed mod phi^8.
        inverse_quotient = binary_remainder(binary_product(6, derivative), phi)
        linear_power = binary_product(1 + (1 << 16), 5)  # (x+1)^18
        inverse = binary_product(power_of_eight(inverse_quotient), inverse_mod_binary(linear_power, modulus))
        inverse = binary_remainder(inverse, modulus)
    for k in range(1, bits):
        ring = PackedRing(coefficients, k + 2)  # one extra bit for the division by two
        remainder = ring.unpack(twice_polynomial(ring, prime, endpoint))
        assert all(c % (1 << (k + 1)) == 0 for c in remainder)
        error = sum((c >> (k + 1)) << j for j, c in enumerate(remainder))
        correction = binary_remainder(binary_product(error, inverse), modulus)
        for j in range(degree):
            coefficients[j] += ((correction >> j) & 1) << k
    ring = PackedRing(coefficients, bits + 1)
    assert twice_polynomial(ring, prime, endpoint) == 0
    return coefficients


def endpoints(coefficients, mask):
    return sum(coefficients) & mask, (sum(coefficients[::2]) - sum(coefficients[1::2])) & mask


def coefficient_product(left, right, bits):
    """Full convolution modulo 2^bits with carry-free nonnegative byte slots."""
    mask = (1 << bits) - 1
    width = (2 * bits + min(len(left), len(right)).bit_length() + 7) // 8
    def pack(values):
        return int.from_bytes(b''.join((c & mask).to_bytes(width, 'little') for c in values), 'little')
    size = len(left) + len(right) - 1
    data = (pack(left) * pack(right)).to_bytes(width * size, 'little')
    return [int.from_bytes(data[i:i + width], 'little') & mask for i in range(0, len(data), width)]


def verify_product(prime, bits, factors):
    while len(factors) > 1:
        joined = [coefficient_product(factors[j], factors[j + 1], bits) for j in range(0, len(factors) - 1, 2)]
        if len(factors) % 2:
            joined.append(factors[-1])
        factors = joined
    def quotient(stride):
        result = [0] * (stride * (prime - 1) + 1)
        result[::stride] = [(-1) ** j for j in range(prime)]
        return result
    phi = quotient(2)
    a = coefficient_product([-1, 1], quotient(4), bits + 1)
    b = coefficient_product([1, 1], coefficient_product(phi, phi, bits + 1), bits + 1)
    aa = coefficient_product(a, a, bits + 1)
    bb = coefficient_product(b, b, bits + 1)
    mask = (1 << bits) - 1
    assert len(aa) == len(bb) == len(factors[0]) == 8 * prime - 5
    assert all((x + y) % 2 == 0 and (((x + y) // 2) & mask) == z
               for x, y, z in zip(aa, bb, factors[0]))
    print(f'full product agrees with defining coefficient formula modulo {1 << bits}, degree {len(aa) - 1}')


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--prime', type=int, choices=(7, 8191, 13367), default=8191)
    parser.add_argument('--bits', type=int, default=16)
    options = parser.parse_args()
    assert options.bits >= 2
    prime, bits = options.prime, options.bits
    mask = (1 << bits) - 1
    if prime == 13367:
        blocks = field_orbit_blocks(prime, 41, (1 << 41) + (1 << 3) + 1)
        pair_counts = (1,)
    else:
        blocks = binary_blocks(prime, prime.bit_length())
        pair_counts = (1, 2)
    block_set = set(blocks)
    factors = [lift_block(prime, 3, bits)]
    end = endpoints(factors[0], mask)
    pairs = []
    for phi in blocks:
        inverse = int(f'{phi:b}'[::-1], 2)
        assert inverse in block_set and inverse != phi
        if phi >= inverse:
            continue
        left = lift_block(prime, phi, bits)
        inverse_constant = pow(left[0], -1, mask + 1)
        right = [(inverse_constant * c) & mask for c in reversed(left)]
        if prime == 7:
            assert right == lift_block(prime, inverse, bits)
        factors.extend((left, right))
        pair = tuple((a * b) & mask for a, b in zip(endpoints(left, mask), endpoints(right, mask)))
        pairs.append(pair)
    verify_product(prime, bits, factors)
    for j in range(2):
        total = end[j]
        for pair in pairs:
            total = (total * pair[j]) & mask
        assert total == 2
    counts = Counter()
    def record(pair, number):
        for k in range(2, bits + 1):
            low = (1 << k) - 1
            if all((v & low) == 1 for v in pair):
                counts[k, number, 0] += 1
            if all(((v * w) & low) == 2 for v, w in zip(pair, end)):
                counts[k, number, 2] += 1
    for pair in pairs:
        record(pair, 1)
    if 2 in pair_counts:
        for a, b in combinations(pairs, 2):
            record(tuple((u * v) & mask for u, v in zip(a, b)), 2)
    for k in range(2, bits + 1):
        print(f'p={prime} mod={1 << k} pairs={len(pairs)} candidates='
              f'{[counts[k, n, endpoint] for n in pair_counts for endpoint in (0, 2)]}')


if __name__ == '__main__':
    main()
