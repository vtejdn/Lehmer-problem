"""Independent verification of the 22 fixed C887/J160 boundary inputs.

Run from the repository root with Python 3.14 and -B.
The installed python-flint 0.9.0 dependency is at J156 outputs/packages.
The actual author boundary.json is a declared comparison input.
No author program is imported or executed.
Gaussian integer coefficient convolution regenerates each complete polynomial.
Fresh 256-bit factor-root enclosures are combined by exact rational interval
products with endpoint clipping at one, retaining every multiplicity.
FLINT factorization and Arb root isolation remain trusted backend operations.
"""

from fractions import Fraction as Q
import json
import math
from pathlib import Path
import platform
import re
import sys


GROUP = Path(__file__).resolve().parent.parent
COMPUTATIONS = GROUP.parent.parent
OUTPUT = COMPUTATIONS / "outputs" / GROUP.name
PACKAGES = COMPUTATIONS / "outputs" / "Yin_J_G0156" / "packages"
sys.path.insert(0, str(PACKAGES))
import flint
from flint import ctx, fmpz_poly

THRESHOLDS = ("6/5", "5/4", "13/10", "7/5")
UNIT_FACTORS = {
    (1, 1): 2,
    (1, -1, 1): 6,
    (1, 0, 1): 4,
    (1, 0, 0, 0, 1): 8,
    (1, 0, -1, 0, 1): 12,
}


def trim(values):
    values = list(values)
    while values and values[-1] == 0:
        values.pop()
    return values


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return trim(result)


def power(a, n):
    result = [1]
    for _ in range(n):
        result = multiply(result, a)
    return result


def divides_unity(poly, order):
    remainder = [-1] + [0] * (order - 1) + [1]
    assert poly[-1] == 1
    while len(remainder) >= len(poly):
        shift, lead = len(remainder) - len(poly), remainder[-1]
        for j, coefficient in enumerate(poly):
            remainder[shift + j] -= lead * coefficient
        remainder = trim(remainder)
    assert not remainder


def gaussian_input(m, b):
    # Expanded g, with all coincident powers accumulated before multiplication.
    g = [[0, 0] for _ in range(m + 3)]
    for degree, real, imaginary in (
        (m + 2, 1, 0), (m + 1, 1, -b), (m, -1, 0),
        (2, -1, 0), (1, 1, b), (0, 1, 0),
    ):
        g[degree][0] += real
        g[degree][1] += imaginary
    norm = [[0, 0] for _ in range(2 * m + 5)]
    for i, (a, b0) in enumerate(g):
        for j, (c, d) in enumerate(g):
            norm[i + j][0] += a * c + b0 * d
            norm[i + j][1] += b0 * c - a * d
    assert all(imaginary == 0 for _, imaginary in norm)
    polynomial = [real for real, _ in norm]
    assert polynomial[0] == polynomial[-1] == 1
    assert polynomial == polynomial[::-1]
    assert g == [[a, -b0] for a, b0 in g[::-1]]
    return trim(a for a, _ in g), trim(b0 for _, b0 in g), polynomial


def dyadic(endpoint):
    mantissa, exponent = map(int, endpoint)
    return Q(mantissa * 2 ** max(exponent, 0), 2 ** max(-exponent, 0))


def bounds(ball):
    return tuple(dyadic(value.man_exp()) for value in (ball.lower(), ball.upper()))


def displayed_interval(text):
    match = re.fullmatch(r"\[([+\-0-9.eE]+) \+/- ([+\-0-9.eE]+)\]", text)
    if match:
        center, radius = map(Q, match.groups())
        assert radius >= 0
        return center - radius, center + radius
    value = Q(text)
    return value, value


def rectangle(text):
    if text.endswith("j"):
        if " + " in text:
            real, imaginary = text[:-1].split(" + ")
        else:
            real, imaginary = "0", text[:-1]
    else:
        real, imaginary = text, "0"
    return displayed_interval(real), displayed_interval(imaginary)


def contained(inner, outer):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def serialized(interval):
    return [[value.numerator, value.denominator] for value in interval]


def multiply_intervals(left, right, exponent=1):
    assert 0 < left[0] <= left[1] and 0 < right[0] <= right[1]
    return left[0] * right[0] ** exponent, left[1] * right[1] ** exponent


def classify(interval, neutral):
    if neutral:
        assert interval == (Q(1), Q(1))
        return {key: "neutral" for key in THRESHOLDS}
    result = {}
    for key in THRESHOLDS:
        threshold = Q(key)
        assert interval[0] > threshold
        result[key] = "above"
    return result


def normalized_core(factors):
    coefficients = [1]
    for poly, exponent, unit in factors:
        if not unit:
            coefficients = multiply(coefficients, power(poly, exponent))
    support = [i for i, value in enumerate(coefficients) if i and value]
    divisor = math.gcd(*support) if support else 0
    if divisor > 1:
        coefficients = coefficients[::divisor]
    degree = len(coefficients) - 1
    other = [value * (-1) ** (degree + i) for i, value in enumerate(coefficients)]
    return min(coefficients[::-1], other[::-1])[::-1]


def verify_factor(record):
    coefficients = record["coefficients_ascending"]
    degree = len(coefficients) - 1
    assert record["degree"] == record["root_count"] == degree
    unit = tuple(coefficients) in UNIT_FACTORS
    assert record["cyclotomic"] == unit
    if unit:
        divides_unity(coefficients, UNIT_FACTORS[tuple(coefficients)])
        assert record["roots"] == []
        product, roots = (Q(1), Q(1)), []
    else:
        fresh = fmpz_poly(coefficients).complex_roots()
        assert sum(int(mult) for _, mult in fresh) == degree
        assert all(int(mult) == 1 for _, mult in fresh)
        assert len(record["roots"]) == degree
        used = set()
        product, roots = (Q(1), Q(1)), []
        for stored in record["roots"]:
            assert stored["multiplicity"] == 1
            old_real, old_imaginary = rectangle(stored["root_ball"])
            matches = [index for index, (root, _) in enumerate(fresh)
                       if index not in used and contained(bounds(root.real), old_real)
                       and contained(bounds(root.imag), old_imaginary)]
            assert len(matches) == 1
            index = matches[0]
            used.add(index)
            root, multiplicity = fresh[index]
            modulus = bounds(abs(root))
            assert contained(modulus, displayed_interval(stored["modulus_ball"]))
            contribution = (max(Q(1), modulus[0]), max(Q(1), modulus[1]))
            assert contained(contribution, displayed_interval(stored["contribution_ball"]))
            region = "outside" if modulus[0] > 1 else "inside" if modulus[1] < 1 else "meets_one"
            assert stored["region"] == region
            product = multiply_intervals(product, contribution, int(multiplicity))
            roots.append({"root_ball": str(root), "multiplicity": int(multiplicity),
                          "region": region, "modulus_bounds_rational": serialized(modulus),
                          "contribution_bounds_rational": serialized(contribution)})
        assert len(used) == degree
    stored_interval = tuple(map(dyadic, record["measure_interval"]))
    assert contained(product, stored_interval)
    assert contained(product, displayed_interval(record["measure_ball"]))
    assert record["thresholds"] == classify(product, unit)
    return product, unit, {"coefficients_ascending": coefficients,
                           "exponent": record["exponent"], "unit": unit,
                           "unit_order": UNIT_FACTORS.get(tuple(coefficients)),
                           "root_count": degree, "roots": roots,
                           "measure_bounds_rational": serialized(product)}


def main():
    ctx.prec, ctx.threads = 256, 1
    author = json.loads((OUTPUT / "boundary.json").read_text(encoding="utf-8"))
    parameters = [(m, b) for m in range(1, 5) for b in range(m + 3)]
    assert author["parameters"] == [list(pair) for pair in parameters]
    assert [(row["m"], row["b"]) for row in author["records"]] == parameters
    assert len(parameters) == 22 and len(author["summary"]) == 22
    results, measures, neutrals = [], {}, []
    for row, summary, (m, b) in zip(author["records"], author["summary"], parameters):
        real, imaginary, polynomial = gaussian_input(m, b)
        assert gaussian_input(m, -b)[2] == polynomial
        certificate = row["certificate"]
        assert row["gaussian_real_coefficients_ascending"] == real
        assert row["gaussian_imaginary_coefficients_ascending"] == imaginary
        assert certificate["coefficients_ascending"] == polynomial
        assert certificate["precision_bits"] == 128
        assert certificate["factorization_product_verified"]
        assert certificate["root_count_with_multiplicity"] == 2 * m + 4
        content, fresh_factors = fmpz_poly(polynomial).factor()
        assert int(content) == 1
        expected_factors = {tuple(map(int, factor)): int(mult) for factor, mult in fresh_factors}
        assert len(expected_factors) == len(fresh_factors)
        assert expected_factors == {tuple(f["coefficients_ascending"]): f["exponent"]
                                    for f in certificate["factors"]}
        assert len(certificate["factors"]) == len(expected_factors)
        rebuilt, product, root_count, factors, core_input = [1], (Q(1), Q(1)), 0, [], []
        for factor in certificate["factors"]:
            coefficients, exponent = factor["coefficients_ascending"], factor["exponent"]
            assert type(exponent) is int and exponent > 0
            rebuilt = multiply(rebuilt, power(coefficients, exponent))
            measure, unit, report = verify_factor(factor)
            product = multiply_intervals(product, measure, exponent)
            root_count += (len(coefficients) - 1) * exponent
            factors.append(report)
            core_input.append((coefficients, exponent, unit))
        assert rebuilt == polynomial and root_count == 2 * m + 4
        neutral = all(unit for _, _, unit in core_input)
        assert certificate["neutral"] == neutral
        assert certificate["core_coefficients_ascending"] == normalized_core(core_input)
        assert certificate["thresholds"] == classify(product, neutral)
        assert certificate["ranking_resolved"]
        old_interval = tuple(map(dyadic, certificate["measure_interval"]))
        assert contained(product, old_interval)
        assert contained(product, displayed_interval(certificate["measure_ball"]))
        if neutral:
            neutrals.append([m, b])
            assert old_interval == (Q(1), Q(1))
        else:
            assert old_interval[0] < product[0] <= product[1] < old_interval[1]
            assert old_interval[0] > Q(6, 5)
        measures[(m, b)] = product
        assert summary == {"m": m, "b": b, "degree": 2 * m + 4,
                           "neutral": neutral, "whole_measure_ball": certificate["measure_ball"],
                           "target_6_5": certificate["thresholds"]["6/5"],
                           "factor_degrees": [[f["degree"], f["exponent"]]
                                              for f in certificate["factors"]]}
        results.append({"m": m, "b": b, "gaussian_real_coefficients_ascending": real,
                        "gaussian_imaginary_coefficients_ascending": imaginary,
                        "coefficients_ascending": polynomial, "neutral": neutral,
                        "root_count_with_multiplicity": root_count,
                        "factors": factors, "complete_measure_bounds_rational": serialized(product),
                        "contained_in_author_interval": True})
    assert neutrals == [[1, 0], [1, 1], [3, 0]]
    # These exact products verify all neutral identities independently of classification.
    assert gaussian_input(1, 0)[2] == multiply(power([1, 1], 2), power([1, -1, 1], 2))
    assert gaussian_input(1, 1)[2] == multiply([1, 0, 1], [1, 0, 0, 0, 1])
    assert gaussian_input(3, 0)[2] == multiply(power([1, 1], 2), power([1, 0, -1, 0, 1], 2))
    expected_minima = {1: (2, "5.10981333907131"), 2: (2, "3.26441716669129"),
                       3: (1, "3.26441716669129"), 4: (1, "2.83097660999536")}
    for m, (best_b, display) in expected_minima.items():
        best = measures[(m, best_b)]
        assert contained(best, (Q(display) - Q(1, 2 * 10 ** 14), Q(display) + Q(1, 2 * 10 ** 14)))
        for (other_m, other_b), other in measures.items():
            if other_m == m and other_b != best_b and [other_m, other_b] not in neutrals:
                assert best[1] < other[0]
    smallest = measures[(4, 1)]
    assert Q("2.83097660999535") < smallest[0] <= smallest[1] < Q("2.83097660999537")
    assert all(smallest[1] < interval[0] for pair, interval in measures.items()
               if pair != (4, 1) and list(pair) not in neutrals)
    result = {"scope": "Exactly 22 fixed C887/J160 boundary inputs; no initial twelve-input experiment",
              "python_version": platform.python_version(), "python_flint_version": flint.__version__,
              "precision_bits": 256, "method": "Gaussian integer convolution; exact factor reconstruction; all factor roots; rational endpoint clipping and products",
              "trusted_backend": "FLINT factorization and Arb all-root isolation and ball arithmetic",
              "parameters": [list(pair) for pair in parameters], "neutral_parameters": neutrals,
              "positive_inputs_strictly_above_6_5": 19, "smallest_positive_parameter": [4, 1],
              "strict_smallest_bounds": ["2.83097660999535", "2.83097660999537"],
              "records": results}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT / "boundary_independent.json"
    temporary = destination.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(destination)
    print(json.dumps({key: result[key] for key in ("neutral_parameters", "positive_inputs_strictly_above_6_5",
                                                  "smallest_positive_parameter", "strict_smallest_bounds")}, indent=2))
    print("Every exact input, factor, multiplicity, saved noncyclotomic root box and complete measure passed.")


if __name__ == "__main__":
    main()
