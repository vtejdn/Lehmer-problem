"""Exact endpoint and quartic certificates for the p=19683, x=-1 chamber.

Run with Python 3.11 or later. All certificate arithmetic uses integers and
fractions. The script proves the stated polynomial inequalities, conditional
on the residue hypotheses and root pairing explained in the mathematical text.
It does not construct an integral two-moment hit or settle N=7 and N=8.
"""

from fractions import Fraction


def trim(polynomial):
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def add(left, right):
    length = max(len(left), len(right))
    result = [Fraction(0) for _ in range(length)]
    for index, coefficient in enumerate(left):
        result[index] += coefficient
    for index, coefficient in enumerate(right):
        result[index] += coefficient
    return trim(result)


def scale(polynomial, scalar):
    return trim([coefficient * scalar for coefficient in polynomial])


def remainder(dividend, divisor):
    result = list(dividend)
    while len(result) >= len(divisor) and any(result):
        coefficient = result[-1] / divisor[-1]
        offset = len(result) - len(divisor)
        for index, value in enumerate(divisor):
            result[offset + index] -= coefficient * value
        trim(result)
    return result


def evaluate(polynomial, argument):
    value = Fraction(0)
    for coefficient in reversed(polynomial):
        value = value * argument + coefficient
    return value


def sturm_sequence(polynomial):
    derivative = [index * polynomial[index] for index in range(1, len(polynomial))]
    sequence = [polynomial, derivative]
    while len(sequence[-1]) > 1:
        next_polynomial = scale(remainder(sequence[-2], sequence[-1]), -1)
        assert any(next_polynomial), "A squarefree quartic is required here."
        sequence.append(next_polynomial)
    return sequence


def signs_at(sequence, argument):
    values = [evaluate(polynomial, argument) for polynomial in sequence]
    assert all(values), "This certificate has no zero endpoint entries."
    return tuple(1 if value > 0 else -1 for value in values)


def variations(signs):
    return sum(left != right for left, right in zip(signs, signs[1:]))


def separator_certificate(conductor, negative_count, separator):
    numerator, denominator = separator.as_integer_ratio()
    degree = (conductor - 1) // 2
    previous = 1
    current = numerator + denominator
    previous_sign = 1
    changes = 0
    for index in range(1, degree + 1):
        if index > 1:
            previous, current = current, numerator * current - denominator**2 * previous
        if current:
            sign = 1 if current > 0 else -1
            changes += sign != previous_sign
            previous_sign = sign
    assert current and changes == degree - negative_count
    assert conductor * abs(current) > 2 * denominator**degree
    return changes


def main():
    p, k = 19683, 1990
    y = Fraction(-161, 100)
    assert separator_certificate(p, k, y) == 7851

    # E>1/2 and W>1/2 together imply the integral endpoint U=1.
    # Their sum is 32+12y-16(2+y)U, which is <=1/5 at U>=2.
    assert 32 + 12 * y - 32 * (2 + y) == Fraction(1, 5)
    assert 8 - 2 * y - Fraction(1, 2) == Fraction(268, 25)

    # N=6 makes the sqrt(2) test A=261/25-(361/50)sqrt(2)<1/2.
    # Here |B(sqrt(2))|=1+sqrt(2), because p is 3 modulo 16.
    assert p % 16 == 3
    assert Fraction(497, 50)**2 < 2 * Fraction(361, 50)**2

    f = [Fraction(0), Fraction(-9, 4), Fraction(3, 2), Fraction(5, 3), Fraction(-1)]
    critical_points = [Fraction(-2), Fraction(-3, 4), Fraction(1, 2), Fraction(3, 2), Fraction(2)]
    values = [evaluate(f, point) for point in critical_points]
    negative_variation = sum(max(Fraction(0), left - right) for left, right in zip(values, values[1:]))
    maximum = max(values)
    assert negative_variation == Fraction(2953, 768)
    assert maximum == Fraction(387, 256)

    traces = [[2], [0, 1], [-2, 0, 1], [0, -3, 0, 1], [2, 0, -4, 0, 1]]
    coefficients = [0, Fraction(11, 4), Fraction(-5, 2), Fraction(5, 3), -1]
    base = Fraction(73, 6) - negative_variation + evaluate(f, y)
    assert base == Fraction(26972673, 12500000)
    assert base - 2 * maximum == Fraction(-43281183, 50000000)
    print("The inherited N=8 real-line separation fails:", base - 2 * maximum)

    old_radius = Fraction(47, 40)
    old_ellipse = [Fraction(-3)]
    for index in range(1, 5):
        multiplier = coefficients[index] * (old_radius**index + old_radius**-index) / 2
        old_ellipse = add(old_ellipse, scale(traces[index], multiplier))
    old_certificate = add([base], scale(old_ellipse, -2))
    failed_value = evaluate(old_certificate, Fraction(-3, 4))
    assert failed_value == Fraction(-3772705508166056991, 1998717337600000000)
    print("The old R=47/40 ellipse certificate is negative at -3/4:", failed_value)
    print("These failures leave the N=8 Mahler lower-bound assertion undecided.")

    for moment, radius in [(9, Fraction(5, 4)), (10, Fraction(7, 5))]:
        bound = base + 4 * (moment - 8)
        assert bound > 2 * maximum
        ellipse_value = [Fraction(-3)]
        for index in range(1, 5):
            multiplier = coefficients[index] * (radius**index + radius**-index) / 2
            ellipse_value = add(ellipse_value, scale(traces[index], multiplier))
        certificate = add([bound], scale(ellipse_value, -2))
        sequence = sturm_sequence(certificate)
        left_signs = signs_at(sequence, -2)
        right_signs = signs_at(sequence, 2)
        assert variations(left_signs) == variations(right_signs)
        assert evaluate(certificate, 0) > 0
        print(f"N={moment}, R={radius}, M>{radius**2}")
        print("Sturm endpoint signs:", left_signs, right_signs)
        print("Certificate at zero:", evaluate(certificate, 0))


if __name__ == "__main__":
    main()
