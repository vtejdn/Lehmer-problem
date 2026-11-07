"""Test individual self-reciprocal binary blocks in the even-order case."""

from argparse import ArgumentParser

from degree_screen import is_prime, order_of_two
from small_lift import binary_remainder, endpoints, lift_block, verify_product


def primitive_blocks(prime, order):
    # The order is even, hence inversion belongs to the doubling orbit.
    # A monic reciprocal polynomial of degree 2h and constant one has h free bits.
    half_degree = order // 2
    cyclotomic = (1 << prime) - 1
    for middle in range(1 << half_degree):
        candidate = (1 << order) | 1
        for j in range(1, half_degree + 1):
            if middle & (1 << (j - 1)):
                candidate |= (1 << j) | (1 << (order - j))
        # Every irreducible factor of Phi_p has degree exactly order.
        if binary_remainder(cyclotomic, candidate) == 0:
            yield candidate


def test(prime, bits):
    if not is_prime(prime) or prime < 3 or bits < 2:
        raise ValueError("expected an odd prime and at least two bits")
    order = order_of_two(prime)
    if order % 2:
        raise ValueError("expected an even multiplicative order of two")
    blocks = list(primitive_blocks(prime, order))
    assert len(blocks) * order == prime - 1
    mask = (1 << bits) - 1
    endpoint = lift_block(prime, 3, bits)
    end = endpoints(endpoint, mask)
    factors = [lift_block(prime, block, bits) for block in blocks]
    values = [endpoints(factor, mask) for factor in factors]
    verify_product(prime, bits, [endpoint] + factors)
    print(f"p={prime}, residue degree {order}, reciprocal choices {len(values)}")
    for k in range(2, bits + 1):
        modulus = 1 << k
        plain = sum(a % modulus == b % modulus == 1 for a, b in values)
        extra = sum(a * end[0] % modulus == b * end[1] % modulus == 2 for a, b in values)
        print(f"modulus {modulus}: {plain} without endpoint, {extra} with endpoint")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--bits", type=int, required=True)
    options = parser.parse_args()
    test(options.prime, options.bits)
