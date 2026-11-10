"""Independent check of the one fixed J153 24-cluster input at genus 72.

Run with Python 3.14 and -B from the repository root.
The actual cluster_word_control.json is a declared comparison input.
The installed python-flint dependency is at J156 outputs/packages.
No author program or J156 evaluator is imported or executed.
The trace is generated in the conjugate square-root variable using integer lists;
the complete polynomial is lifted directly through x=2-z^2-z^-2.
The original matrix is rebuilt by applying the two shears and rotation to every
basis vector, retaining the full cross term automatically.
FLINT characteristic polynomials/factorization and Arb root isolation remain
trusted backend operations, not independently verified implementations.
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
sys.path.insert(0, str(COMPUTATIONS / "outputs" / "Yin_J_G0156" / "packages"))
import flint
from flint import ctx, fmpz_mat, fmpz_poly

G = 72
RUNS = [(1, 1), (-1, 1), (1, 2), (-1, 7), (1, 5), (-1, 4), (1, 4)]


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    result = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        result[i] += value
    for i, value in enumerate(b):
        result[i] += value
    return trim(result)


def multiply(a, b):
    if not a or not b:
        return []
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return trim(result)


def divide_monic(a, b):
    assert b[-1] == 1 and len(a) >= len(b)
    remainder, quotient = list(a), [0] * (len(a) - len(b) + 1)
    while len(remainder) >= len(b):
        shift, lead = len(remainder) - len(b), remainder[-1]
        quotient[shift] = lead
        for j, value in enumerate(b):
            remainder[shift + j] -= lead * value
        remainder = trim(remainder)
    assert not remainder and multiply(quotient, b) == a
    return quotient


def matrix_product(a, b):
    return [[add(multiply(a[i][0], b[0][j]), multiply(a[i][1], b[1][j]))
             for j in range(2)] for i in range(2)]


def evaluate(a, value):
    result = 0
    for coefficient in a[::-1]:
        result = result * value + coefficient
    return result


def trace_and_polynomial(word):
    # For real -2<t<2, E_s is conjugate to [[1-u^2,s*u],[-s*u,1]],
    # where u^2=x=4-t^2; the common conjugation preserves the entire word trace.
    product = [[[1], []], [[], [1]]]
    for sign in word:
        product = matrix_product(product, [[[1, 0, -1], [0, sign]], [[0, -sign], [1]]])
    in_u = add(product[0][0], product[1][1])
    assert all(value == 0 for value in in_u[1::2])
    in_x = in_u[::2]
    assert len(in_x) == 25 and evaluate(in_x, 0) == 2 and evaluate(in_x, 1) == -2
    in_t = [0] * 49
    for degree, coefficient in enumerate(in_x):
        for j in range(degree + 1):
            in_t[2 * j] += coefficient * math.comb(degree, j) * 4 ** (degree - j) * (-1) ** j
    assert evaluate(in_t, 2) == 2
    assert sum(in_t[2 * j] * 3 ** j for j in range(25)) == -2
    # Direct Laurent substitution x=2-z^2-z^-2, independent of the t-binomial lift.
    laurent, x_power = {}, {0: 1}
    for coefficient in in_x:
        for exponent, value in x_power.items():
            laurent[exponent] = laurent.get(exponent, 0) + coefficient * value
        following = {}
        for exponent, value in x_power.items():
            for shift, scalar in ((0, 2), (2, -1), (-2, -1)):
                following[exponent + shift] = following.get(exponent + shift, 0) + scalar * value
        x_power = {exponent: value for exponent, value in following.items() if value}
    polynomial = [0] * 145
    polynomial[0] = polynomial[-1] = 1
    for exponent, value in laurent.items():
        assert 0 < G + exponent < 2 * G
        polynomial[G + exponent] -= value
    assert polynomial == polynomial[::-1]
    return in_x, in_t, polynomial


def action_matrix(physical_word):
    edges, epsilon, eta = [], [], []
    for cluster, sign in enumerate(physical_word):
        edges.extend((3 * cluster, 3 * cluster + 1))
        epsilon.extend((sign, sign))
        eta.extend((-sign, sign))
    assert len(set(edges)) == 48 and sum(epsilon) == sum(eta) == 0
    matrix = [[0] * (2 * G) for _ in range(2 * G)]
    for column in range(2 * G):
        x, y = [0] * G, [0] * G
        if column < G:
            x[column] = 1
        else:
            y[column - G] = 1
        # First L(E), then U(D), then the forward shift R.
        after_y = list(y)
        for site, sign in zip(edges, eta):
            following = (site + 1) % G
            value = sign * (x[site] + x[following])
            after_y[site] += value
            after_y[following] += value
        after_x = list(x)
        for site, sign in zip(edges, epsilon):
            following = (site + 1) % G
            value = sign * (after_y[site] - after_y[following])
            after_x[site] += value
            after_x[following] -= value
        for source in range(G):
            matrix[(source + 1) % G][column] = after_x[source]
            matrix[G + (source + 1) % G][column] = after_y[source]
    return fmpz_mat(matrix), {"sites_zero_based": edges, "epsilon": epsilon, "eta": eta}


def dyadic(pair):
    mantissa, exponent = map(int, pair)
    return Q(mantissa * 2 ** max(exponent, 0), 2 ** max(-exponent, 0))


def bounds(ball):
    return tuple(dyadic(value.man_exp()) for value in (ball.lower(), ball.upper()))


def displayed_interval(text):
    centered = re.fullmatch(r"\[\+/- ([+\-0-9.eE]+)\]", text)
    if centered:
        radius = Q(centered.group(1))
        assert radius >= 0
        return -radius, radius
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


def compact_dyadic(interval):
    scale = 2 ** 240
    lower, upper = interval[0] * scale, interval[1] * scale
    return [[lower.numerator // lower.denominator, -240],
            [-((-upper.numerator) // upper.denominator), -240]]


def verify_measure(polynomial, certificate):
    unit_factors = [([-1, 1], 2), ([1, 1], 2), ([1, 0, 0, 0, 1], 2)]
    remainder, rebuilt_units = polynomial, [1]
    for factor, exponent in unit_factors:
        for _ in range(exponent):
            remainder = divide_monic(remainder, factor)
            rebuilt_units = multiply(rebuilt_units, factor)
    assert len(remainder) == 133 and multiply(rebuilt_units, remainder) == polynomial
    content, factorization = fmpz_poly(remainder).factor()
    assert int(content) == 1 and len(factorization) == 1
    assert list(map(int, factorization[0][0])) == remainder and int(factorization[0][1]) == 1
    expected = {tuple(factor): exponent for factor, exponent in unit_factors}
    expected[tuple(remainder)] = 1
    assert len(certificate["factors"]) == 4
    assert {tuple(row["coefficients_ascending"]): row["exponent"] for row in certificate["factors"]} == expected
    nonunit = None
    for row in certificate["factors"]:
        degree = len(row["coefficients_ascending"]) - 1
        assert row["degree"] == row["root_count"] == degree
        if degree == 132:
            nonunit = row
            assert not row["cyclotomic"] and row["exponent"] == 1
        else:
            assert row["cyclotomic"] and row["roots"] == []
            assert tuple(map(dyadic, row["measure_interval"])) == (Q(1), Q(1))
            assert displayed_interval(row["measure_ball"]) == (Q(1), Q(1))
            assert all(value == "neutral" for value in row["thresholds"].values())
    assert sum(row["degree"] * row["exponent"] for row in certificate["factors"]) == 144
    fresh = fmpz_poly(remainder).complex_roots()
    assert len(fresh) == 132 and all(int(mult) == 1 for _, mult in fresh)
    assert len(nonunit["roots"]) == 132
    used, records, counts, product = set(), [], {"inside": 0, "outside": 0, "meets_one": 0}, (Q(1), Q(1))
    for stored in nonunit["roots"]:
        assert stored["multiplicity"] == 1
        old_real, old_imaginary = rectangle(stored["root_ball"])
        matches = [j for j, (root, _) in enumerate(fresh) if j not in used
                   and contained(bounds(root.real), old_real) and contained(bounds(root.imag), old_imaginary)]
        assert len(matches) == 1
        index = matches[0]
        used.add(index)
        root = fresh[index][0]
        modulus = bounds(abs(root))
        assert contained(modulus, displayed_interval(stored["modulus_ball"]))
        contribution = (max(Q(1), modulus[0]), max(Q(1), modulus[1]))
        assert contained(contribution, displayed_interval(stored["contribution_ball"]))
        region = "outside" if modulus[0] > 1 else "inside" if modulus[1] < 1 else "meets_one"
        assert stored["region"] == region
        counts[region] += 1
        product = product[0] * contribution[0], product[1] * contribution[1]
        records.append({"root_ball": str(root), "multiplicity": 1, "region": region,
                        "modulus_bounds": [[v.numerator, v.denominator] for v in modulus],
                        "contribution_bounds": [[v.numerator, v.denominator] for v in contribution]})
    assert len(used) == 132
    enclosure = compact_dyadic(product)
    rounded = tuple(map(dyadic, enclosure))
    assert contained(product, rounded)
    old = tuple(map(dyadic, certificate["measure_interval"]))
    assert old == tuple(map(dyadic, nonunit["measure_interval"]))
    assert old[0] < rounded[0] <= rounded[1] < old[1]
    assert contained(rounded, displayed_interval(certificate["measure_ball"]))
    assert contained(rounded, displayed_interval(nonunit["measure_ball"]))
    assert Q("47.97469677926936") < old[0] < old[1] < Q("47.97469677926937")
    for threshold in ("6/5", "5/4", "13/10", "7/5"):
        assert old[0] > Q(threshold)
        assert certificate["thresholds"][threshold] == nonunit["thresholds"][threshold] == "above"
    divisor = math.gcd(*(j for j, value in enumerate(remainder) if j and value))
    assert divisor == 2
    compressed = remainder[::divisor]
    degree = len(compressed) - 1
    opposite = [value * (-1) ** (degree + j) for j, value in enumerate(compressed)]
    assert certificate["core_coefficients_ascending"] == min(compressed[::-1], opposite[::-1])[::-1]
    assert not certificate["neutral"] and certificate["ranking_resolved"]
    return {"noncyclotomic_coefficients_ascending": remainder,
            "factorization": "one degree-132 irreducible factor with multiplicity one, using trusted FLINT",
            "root_count_with_multiplicity": 144, "noncyclotomic_ball_regions": counts,
            "region_limit": "meets_one is an enclosure classification, not a proof of a unit-circle root",
            "fresh_complete_dyadic_interval": enclosure, "author_complete_dyadic_interval": certificate["measure_interval"],
            "all_fresh_boxes_matched_uniquely": True, "strictly_inside_author_measure_interval": True,
            "roots": records}


def main():
    ctx.prec, ctx.threads = 256, 1
    author = json.loads((OUTPUT / "cluster_word_control.json").read_text(encoding="utf-8"))
    word = [sign for sign, count in RUNS for _ in range(count)]
    assert len(word) == 24 and sum(word) == 0
    physical = word[::-1]
    assert author["genus"] == G and author["matrix_word_runs_left_to_right"] == [list(pair) for pair in RUNS]
    assert author["physical_cluster_signs_in_cyclic_order"] == physical
    in_x, in_t, polynomial = trace_and_polynomial(word)
    matrix, original_input = action_matrix(physical)
    assert author["original_input"] == original_input
    assert author["trace_coefficients_ascending"] == in_t
    matrix_coefficients = list(map(int, matrix.charpoly()))
    assert matrix_coefficients == polynomial
    certificate = author["certificate"]
    assert certificate["coefficients_ascending"] == polynomial
    assert certificate["factorization_product_verified"] and certificate["root_count_with_multiplicity"] == 144
    assert certificate["precision_bits"] == 128
    assert author["exact_controls"] == {"trace_at_2": 2, "trace_remainder_mod_t2_minus_3": [-2],
                                         "original_matrix_charpoly_matches_trace_lift": True, "balanced_sign_vectors": True}
    measure = verify_measure(polynomial, certificate)
    result = {"scope": "One fixed 24-cluster word at genus 72; no other input or family exclusion",
              "python_version": platform.python_version(), "python_flint_version": flint.__version__,
              "precision_bits": 256, "matrix_word_runs_left_to_right": RUNS,
              "physical_cluster_signs_in_cyclic_order": physical, "original_input": original_input,
              "trace_in_x_coefficients_ascending": in_x, "trace_coefficients_ascending": in_t,
              "coefficients_ascending": polynomial, "original_action_charpoly_matches": True,
              "measure_method": "exact rational max(1,modulus) endpoint products, rounded outward to denominator 2^240 for retention",
              "trusted_backend": "FLINT characteristic polynomial/factorization and Arb root isolation/ball arithmetic",
              "measure": measure}
    destination = OUTPUT / "cluster_word_independent.json"
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    temporary.replace(destination)
    print(json.dumps({"degree": len(polynomial) - 1, "trace_degree": len(in_t) - 1,
                      "fresh_interval": measure["fresh_complete_dyadic_interval"],
                      "regions": measure["noncyclotomic_ball_regions"]}, indent=2))
    print("Both independent coefficient constructions, exact factors, all root boxes and complete measure passed.")


if __name__ == "__main__":
    main()
