"""Certify the circle norm of the cyclotomic multiple in Yin_C_G0901_v16."""

from functools import cache
from itertools import zip_longest
from math import comb


def add(first, second):
    return [a + b for a, b in zip_longest(first, second, fillvalue=0)]


def multiply(first, second):
    product = [0] * (len(first) + len(second) - 1)
    for i, a in enumerate(first):
        for j, b in enumerate(second):
            product[i + j] += a * b
    return product


def divide_monic(dividend, divisor):
    remainder = dividend.copy()
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    for i in reversed(range(len(quotient))):
        coefficient = remainder[i + len(divisor) - 1]
        quotient[i] = coefficient
        for j, b in enumerate(divisor):
            remainder[i + j] -= coefficient * b
    if any(remainder):
        raise ArithmeticError("Nonzero remainder in cyclotomic factorization")
    return quotient


@cache
def cyclotomic(n):
    polynomial = [-1] + [0] * (n - 1) + [1]
    for divisor in range(1, n):
        if n % divisor == 0:
            polynomial = divide_monic(polynomial, cyclotomic(divisor))
    return polynomial


def trace_polynomial(reciprocal):
    """Return W such that R(z) = z**d W(z + 1/z) in degree 2d."""
    degree = len(reciprocal) - 1
    if degree % 2 or reciprocal != reciprocal[::-1]:
        raise ValueError("Expected a reciprocal polynomial of even degree")
    d = degree // 2
    result = [reciprocal[d]]
    previous, current = [2], [0, 1]
    for j in range(1, d + 1):
        result = add(result, [reciprocal[d + j] * c for c in current])
        previous, current = current, add([0] + current, [-c for c in previous])
    return result


def interval_minima(polynomial):
    """Return floors of local Bernstein coefficient minima on 16 intervals."""
    degree = len(polynomial) - 1
    minima = []
    for left in range(-8, 8):
        numerator = [left, left + 1]
        denominator = [4, 4]
        value = [polynomial[-1]]
        denominator_power = [1]
        for coefficient in reversed(polynomial[:-1]):
            denominator_power = multiply(denominator_power, denominator)
            value = add(multiply(value, numerator),
                        [coefficient * c for c in denominator_power])
        minima.append(min(c // (4**degree * comb(degree, i))
                          for i, c in enumerate(value)))
    return minima


def main():
    lehmer = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
    orders = (9, 9, 10, 10, 15, 21)
    factors = [lehmer] * 6 + [cyclotomic(order) for order in orders]
    product = [1]
    for factor in factors:
        product = multiply(product, factor)
    trace = trace_polynomial(product)
    if len(product) != 101 or trace[:2] != [729, 0]:
        raise ArithmeticError("Degree, value or derivative at the contact differs")
    trace_product = [1]
    for factor in factors:
        trace_product = multiply(trace_product, trace_polynomial(factor))
    if trace_product != trace:
        raise ArithmeticError("Trace factorization differs from the full product")
    for name, factor in [("L", lehmer)] + [(f"Phi_{n}", cyclotomic(n))
                                           for n in sorted(set(orders))]:
        print(f"{name} trace, ascending coefficients: {trace_polynomial(factor)}")
    tests = [("729 + W", add([729], trace)),
             ("(729 - W)/x^2", [-c for c in trace[2:]])]
    for name, polynomial in tests:
        minima = interval_minima(polynomial)
        if min(minima) <= 0:
            raise ArithmeticError(f"Positivity certificate failed for {name}")
        print(f"{name}, degree {len(polynomial) - 1}: {minima}")


if __name__ == "__main__":
    main()
