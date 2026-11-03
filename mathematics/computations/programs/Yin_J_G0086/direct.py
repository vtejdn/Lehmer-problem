"""Independent original Laurent convolution; imports no recurrence construction."""

from math import comb


def multiply(left, right):
    out = {}
    products = 0
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] = out.get(i + j, 0) + a * b
            products += 1
    return {i: a for i, a in out.items() if a}, products


def compute(p, depth):
    d = len(p) - 1
    h = sum(abs(a) for a in p)
    # Direct two-polynomial product, separate from trace autocorrelations/Chebyshev.
    polynomial = {i: a for i, a in enumerate(p) if a}
    reversed_laurent = {-i: a for i, a in enumerate(p) if a}
    b, input_products = multiply(polynomial, reversed_laurent)
    z = {i: -a for i, a in b.items()}
    z[0] = z.get(0, 0) + h * h
    z = {i: a for i, a in z.items() if a}
    power = {0: 1}
    h_power = 1
    states = []
    coefficient_checks = products = 0
    max_support = max_bits = 0
    for n in range(depth + 1):
        for exponent, coefficient in power.items():
            if abs(exponent) > n * d or abs(coefficient) > h_power:
                raise ArithmeticError(f"Direct Fourier/degree bound at n={n}")
            coefficient_checks += 1
            max_bits = max(max_bits, abs(coefficient).bit_length())
        max_support = max(max_support, len(power))
        row = []
        for k in range(d + 1):
            # CT[(z+z^-1)^k Z^n], using its independent explicit binomial expansion.
            value = sum(comb(k, j) * power.get(-(k - 2 * j), 0)
                        for j in range(k + 1))
            row.append(value)
        states.append(row)
        if n < depth:
            power, count = multiply(power, z)
            products += count
            h_power *= h * h
    return states, {"input_term_products": input_products,
                    "power_term_products": products,
                    "fourier_coefficient_checks": coefficient_checks,
                    "max_power_support": max_support,
                    "max_coefficient_bits": max_bits}
