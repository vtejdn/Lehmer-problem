"""Exact necessary moment filters for the logarithmic cut at 3**9.

Only integer and rational arithmetic supplies certificates.
The tables are necessary conditions, without a realization assertion.
"""

from fractions import Fraction


P = 19683
NODES = (P - 1) // 2
CUT = 1990
SEPARATOR = Fraction(-161, 100)
DEGREES = [3**index for index in range(9)]
PARITIES = [1, 0, 1, 0, 0, 0, 0, 1, 0]
VALUATIONS = [5, 4, 3, 2, 2, 2, 2, 1, 0]
NORM_EXPONENT = 4391


def ceiling_root(value, degree):
    lower, upper = 0, 1
    while upper**degree < value:
        upper *= 2
    while upper - lower > 1:
        middle = (lower + upper) // 2
        if middle**degree >= value:
            upper = middle
        else:
            lower = middle
    return upper


def minimum_weighted_sum(weights):
    """Optimize all valuation vectors, with an exact incumbent cutoff."""
    incumbent = sum(
        degree * 2**valuation * weight
        for degree, valuation, weight in zip(DEGREES, VALUATIONS, weights)
    )
    states = {0: (0, [])}
    for degree, parity, weight in zip(DEGREES, PARITIES, weights):
        following = {}
        for exponent, (cost, vector) in states.items():
            valuation = parity
            while exponent + degree * valuation <= NORM_EXPONENT:
                next_cost = cost + degree * 2**valuation * weight
                if next_cost > incumbent:
                    break
                next_exponent = exponent + degree * valuation
                if next_exponent not in following or next_cost < following[next_exponent][0]:
                    following[next_exponent] = (next_cost, vector + [valuation])
                valuation += 2
        states = following
    return states[NORM_EXPONENT]


def separator_certificate(value=SEPARATOR):
    u, v = value.numerator, value.denominator
    previous, current = 1, u + v
    last_sign = 1
    variations = 0
    for index in range(1, NODES + 1):
        if index > 1:
            previous, current = current, u * current - v * v * previous
        if current:
            sign = 1 if current > 0 else -1
            variations += sign != last_sign
            last_sign = sign
    assert variations == NODES - CUT
    assert P * abs(current) > 2 * v**NODES
    return variations


def linear_layer_weights():
    numerator, denominator = SEPARATOR.numerator, SEPARATOR.denominator
    weights = {3: [], 9: [], 27: []}
    for degree in DEGREES:
        resultant = abs(numerator + denominator)
        for factor, bounds in weights.items():
            bounds.append(ceiling_root(factor * resultant, degree))
        numerator, denominator = (
            numerator**3 - 3 * numerator * denominator**2,
            denominator**3,
        )
    return weights


def multiply_mod(left, right, monic):
    product = [0] * 5
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            product[i + j] += first * second
    for index in (4, 3):
        coefficient = product[index]
        for offset in range(3):
            product[index - 3 + offset] -= coefficient * monic[offset]
    return product[:3]


def determinant3(rows):
    a, b, c = rows[0]
    d, e, f = rows[1]
    g, h, i = rows[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def cubic_layer_weights(coefficients):
    """Norm of (2-b)H(b), for H=A*t**3+a*t**2+b*t+c."""
    leading, quadratic, linear, constant = coefficients
    monic = [leading**2 * constant, leading * linear, quadratic]
    remainder = [0, 1, 0]
    denominator = leading
    bounds, resultant_bits = [], []
    for degree in DEGREES:
        evaluation = remainder[:]
        evaluation[0] += denominator
        columns = [multiply_mod(evaluation, basis, monic) for basis in ([1, 0, 0], [0, 1, 0], [0, 0, 1])]
        determinant = determinant3(list(map(list, zip(*columns))))
        resultant, residual = divmod(abs(determinant), denominator**2)
        assert residual == 0
        bounds.append(ceiling_root(3 * resultant, degree))
        resultant_bits.append(resultant.bit_length())
        cube = multiply_mod(multiply_mod(remainder, remainder, monic), remainder, monic)
        remainder = [value - 3 * denominator**2 * old for value, old in zip(cube, remainder)]
        denominator **= 3
    return bounds, resultant_bits


def moment_table(bounds, cubic_bound):
    y = SEPARATOR
    tables = []
    for profile in range(-2, 3):
        first, second = profile**2 + 2, -4 * profile
        total = second - y * first
        endpoint_ceiling = ((4 + y) * first - second - bounds[9]) / (4 * (2 + y))
        endpoint_maximum = endpoint_ceiling.numerator // endpoint_ceiling.denominator
        for endpoint in range(-1 - 2 * profile, endpoint_maximum + 1):
            s0 = first - (2 + y) * endpoint
            endpoint_sum = (4 + y) * first - second - 4 * (2 + y) * endpoint
            if min(total, s0) < bounds[3] or endpoint_sum < bounds[9]:
                continue
            s1 = second - (2 + y) * first + 2 * (2 + y) * endpoint
            survivors = []
            third_floor = bounds[27] + y * second + 6 * total - 16 * s0
            third_ceiling = (2 + y) * second - 2 * y * first - bounds[9]
            third_minimum = -((-third_floor.numerator) // third_floor.denominator)
            third_maximum = third_ceiling.numerator // third_ceiling.denominator
            for third in range(third_minimum, third_maximum + 1):
                upper_sum = (2 + y) * second - 2 * y * first - third
                lower_sum = third - y * second - 6 * total + 16 * s0
                s2 = third - (2 + y) * second + 2 * (2 + y) * first - 4 * (2 + y) * endpoint
                cubic_sum = 13 * third - 41 * second + 49 * first - 58 * endpoint
                if upper_sum >= bounds[9] and lower_sum >= bounds[27] and s0 * s2 > s1**2 and cubic_sum >= cubic_bound:
                    survivors.append(third)
            if survivors:
                tables.append((profile, first, second, endpoint, survivors))
    return tables


def main():
    partial_log = 2 * sum((Fraction(1, 2) ** (2 * j + 1) / (2 * j + 1) for j in range(40)), Fraction())
    log_error = 2 * Fraction(1, 2) ** 81 / 81 / Fraction(3, 4)
    assert P / Fraction(CUT + 1) < 9 * partial_log
    assert 9 * (partial_log + log_error) < P / Fraction(CUT)
    print("cut", CUT, "poles_above_separator", separator_certificate())
    rounded_counts = [(2 * CUT + 3**i) // (2 * 3**i) for i in range(10)]
    signs = [(rounded_counts[9 - layer] - rounded_counts[10 - layer]) % 2 for layer in range(1, 10)]
    flips = [(signs[index] - (signs[index - 1] if index else 0)) % 2 for index in range(9)]
    exponent = sum(bit * (3**index - 1) // 2 for index, bit in enumerate(flips))
    assert exponent == NORM_EXPONENT
    assert PARITIES == [1 - bit for bit in signs]
    assert VALUATIONS == [sum(flips[layer:]) for layer in range(1, 10)]
    assert sum(d * t for d, t in zip(DEGREES, VALUATIONS)) == exponent
    print("layer_signs", signs, "norm_exponent", exponent)
    print("minimum_layer_mass", minimum_weighted_sum([1] * 9))
    bounds = {}
    for factor, weights in linear_layer_weights().items():
        minimum, vector = minimum_weighted_sum(weights)
        bounds[factor] = Fraction(minimum, P * SEPARATOR.denominator)
        print("linear_layer", factor, weights, "minimum", minimum, "at", vector)
    cubic = (13, -15, -33, 40)
    cubic_value = lambda value: 13 * value**3 - 15 * value**2 - 33 * value + 40
    other_endpoint = Fraction(-16099, 10000)
    assert cubic_value(SEPARATOR) < 0 < cubic_value(other_endpoint)
    assert separator_certificate(other_endpoint) == NODES - CUT
    leading, quadratic, linear, constant = cubic
    discriminant = quadratic**2 * linear**2 - 4 * leading * linear**3 - 4 * quadratic**3 * constant - 27 * leading**2 * constant**2 + 18 * leading * quadratic * linear * constant
    assert discriminant == -13851
    weights, bits = cubic_layer_weights(cubic)
    print("cubic", cubic, "layer_bounds", weights, "resultant_bits", bits)
    cubic_minimum, cubic_vector = minimum_weighted_sum(weights)
    print("cubic_minimum", cubic_minimum, "at", cubic_vector)
    table = moment_table(bounds, Fraction(cubic_minimum, P))
    print("moment_table", table)
    matching = [(x, first, second, endpoint, 6 + 2 * x**2) for x, first, second, endpoint, thirds in table if 6 + 2 * x**2 in thirds]
    print("matching_third_moment", matching)


if __name__ == "__main__":
    main()
