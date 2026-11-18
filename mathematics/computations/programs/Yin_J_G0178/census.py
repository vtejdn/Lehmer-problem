"""Census of reciprocal sextic units of Mahler measure at most two."""

import json
from fractions import Fraction
from itertools import product
from math import comb, gcd
from pathlib import Path


OUTPUT = Path(__file__).resolve().parents[2] / "outputs" / "Yin_J_G0178" / "results.json"


def trimmed(poly):
    for i, value in enumerate(poly):
        if value:
            return poly[i:]
    return []


def divide(poly, divisor):
    """Descending coefficients; all nonmonic divisions use rational arithmetic."""
    remainder = list(poly)
    size = len(poly) - len(divisor) + 1
    quotient = []
    for i in range(max(0, size)):
        factor = remainder[i] if divisor[0] == 1 else Fraction(remainder[i], divisor[0])
        quotient.append(factor)
        for j, value in enumerate(divisor):
            remainder[i + j] -= factor * value
    return trimmed(quotient), trimmed(remainder)


def powers(poly, count):
    degree = len(poly) - 1
    sums = [degree]
    for n in range(1, count + 1):
        lower = sum(poly[j] * sums[n-j] for j in range(1, min(n-1, degree) + 1))
        sums.append(-lower - (n * poly[n] if n <= degree else 0))
    return sums


def from_powers(sums):
    coefficients = [1]
    for n in range(1, len(sums)):
        total = -sum(sums[j] * coefficients[n-j] for j in range(1, n + 1))
        assert total % n == 0
        coefficients.append(total // n)
    return coefficients


def exterior_poly(poly, order):
    size = comb(6, order)
    s = powers(poly, order * size)
    values = [size]
    for j in range(1, size + 1):
        if order == 2:
            numerator = s[j]**2 - s[2*j]
        else:
            numerator = s[j]**3 - 3*s[j]*s[2*j] + 2*s[3*j]
        denominator = 2 if order == 2 else 6
        assert numerator % denominator == 0
        values.append(numerator // denominator)
    return from_powers(values)


def shift_test(poly, numerator, denominator=1):
    """Coefficients at both signs after scaling roots by the denominator."""
    for sign in (1, -1):
        translated = [1]
        factor = 1
        for coefficient in poly[1:]:
            factor *= denominator * sign
            translated = (
                [1] + [translated[j] + numerator * translated[j-1]
                       for j in range(1, len(translated))]
                + [numerator * translated[-1] + coefficient * factor]
            )
        if min(translated) < 0:
            return False
    return True


def small_factors():
    for degree in (1, 2, 3):
        bounds = [2 * comb(degree, i) for i in range(1, degree)]
        for inner in product(*(range(-h, h + 1) for h in bounds)):
            for last in (-1, 1):
                yield [1, *inner, last]


def cyclotomics():
    table = {}
    for n in range(1, 2 * 30**2 + 1):
        if sum(gcd(i, n) == 1 for i in range(1, n + 1)) > 30:
            continue
        poly = [1] + [0] * (n - 1) + [-1]
        for d, previous in table.items():
            if n % d == 0:
                poly, rem = divide(poly, previous)
                assert not rem
        table[n] = poly
    return table


def traces_inside(trace):
    chain = [trace, [3, 2 * trace[1], trace[2]]]
    while len(chain[-1]) > 1:
        _, rem = divide(chain[-2], chain[-1])
        assert rem
        chain.append([-value for value in rem])

    def variations(endpoint):
        signs = []
        for poly in chain:
            value = 0
            for coefficient in poly:
                value = value * endpoint + coefficient
            if value:
                signs.append(value > 0)
        return sum(a != b for a, b in zip(signs, signs[1:]))

    return variations(-2) - variations(2)


def census():
    factors = list(small_factors())
    cyclo = cyclotomics()
    results = []
    count_full = count_capped = count_irred = 0
    for a, b, c in product(range(13), range(-30, 31), range(-40, 41)):
        if a == 0 and c < 0:
            continue
        count_full += 1
        poly = [1, a, b, c, b, a, 1]
        if not shift_test(poly, 2):
            continue
        second = exterior_poly(poly, 2)
        if not shift_test(second, 2):
            continue
        third = exterior_poly(poly, 3)
        if not shift_test(third, 2):
            continue
        count_capped += 1
        if any(not divide(poly, factor)[1] for factor in factors):
            continue
        count_irred += 1
        if poly in cyclo.values():
            continue
        g = 3 - traces_inside([1, a, b - 3, c - 2*a])
        assert g in (1, 2)
        lower = (7, 5) if g == 1 else (17, 10)
        assert not all(shift_test(q, *lower) for q in (poly, second, third))
        exponent = 4 * (6-g) - (9-2)
        assert lower[0]**exponent > 64 * lower[1]**exponent

        sums = powers(poly, 30)
        ratios = from_powers([30] + [v*v - 6 for v in sums[1:]])
        orders = [n for n, phi in cyclo.items() if not divide(ratios, phi)[1]]
        assert not orders
        results.append({"a": a, "b": b, "c": c, "outside": g,
                        "strict_measure_lower": f"{lower[0]}/{lower[1]}",
                        "torsion_ratio_orders": orders})
    return {"coefficient_box": count_full, "measure_at_most_two": count_capped,
            "irreducible": count_irred, "nontorsion": len(results), "seeds": results}


if __name__ == "__main__":
    data = census()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"{data['coefficient_box']} triples, {data['measure_at_most_two']} capped, "
          f"{data['irreducible']} irreducible, {data['nontorsion']} nontorsion")
