"""Independent complete integer check of the C863 v4 Fourier envelope.

Polynomial weights are accumulated from the original residual powers.
Two-axis walk counts are obtained by interleaving one-axis walks, without
the author's product of two binomial coefficients.  Four-axis coefficients
use the crossing pairing (a,c)|(b,d).  Enumeration uses successive gaps.
The native certificate is read only after all coefficients and maxima have
been computed.  No author program is imported or executed.
"""

from collections import defaultdict
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import platform


GROUP = Path(__file__).resolve().parent
INPUT = GROUP / "inputs" / "rank-two-fourier-envelope.json"
OUTPUT = GROUP.parent.parent / "outputs" / GROUP.name / "rank-two-fourier-envelope-verification.json"


def prepare(order):
    common = 1
    for j in range(1, order + 1):
        common = common * j // math.gcd(common, j)
    denominator = common * 64 ** order
    # coefficient lists for (64-X)^j, followed by multiplication by
    # common/j * 64^(order-j), directly implementing the defining sum.
    residual = [1]
    weights = [0] * (order + 1)
    for j in range(1, order + 1):
        following = [0] * (j + 1)
        for k, value in enumerate(residual):
            following[k] += 64 * value
            following[k + 1] -= value
        residual = following
        scale = (common // j) * 64 ** (order - j)
        for k, value in enumerate(residual):
            weights[k] += scale * value
    choose = [[math.comb(n, k) for k in range(n + 1)] for n in range(2 * order + 1)]
    pairs = {}
    for weight in range(order + 1):
        for a in range(weight // 2 + 1):
            b = weight - a
            values = []
            for length in range(weight, order + 1):
                # Of 2*length steps, 2*t lie in the first axis.  The positive
                # step counts on the two axes are t+a and length-t+b.
                values.append(sum(choose[2 * length][2 * t]
                                  * choose[2 * t][t + a]
                                  * choose[2 * (length - t)][length - t + b]
                                  for t in range(a, length - b + 1)))
            pairs[a, b] = values
    transformed = {}
    for (a, b), values in pairs.items():
        minimum = a + b
        transformed[a, b] = [sum(weights[left + right]
                                     * choose[2 * (left + right)][2 * right]
                                     * values[right - minimum]
                                     for right in range(minimum, order - left + 1))
                              for left in range(order - minimum + 1)]
    return denominator, pairs, transformed


def numerator(vector, order, pairs, transformed):
    a, b, c, d = vector
    # Deliberately split into coordinates 1,3 and 2,4 rather than 1,2 and 3,4.
    first = pairs[a, c]
    second = transformed[b, d]
    value = sum(first[length - a - c] * second[length]
                for length in range(a + c, order - b - d + 1))
    return -value if sum(vector) % 2 else value


def gap_vectors(order):
    """Sorted nonnegative vectors from their unique successive gaps."""
    for first in range(order // 4 + 1):
        for gap1 in range((order - 4 * first) // 3 + 1):
            for gap2 in range((order - 4 * first - 3 * gap1) // 2 + 1):
                for gap3 in range(order - 4 * first - 3 * gap1 - 2 * gap2 + 1):
                    yield (first, first + gap1, first + gap1 + gap2,
                           first + gap1 + gap2 + gap3)


def direct_controls():
    """Compare complete signed Fourier polynomials at orders 1 through 5.

    The reference directly multiplies the antisymmetric polynomial and
    builds each (64+F^2)^j/j.  This does not use the collapsed PT1 weights.
    """
    checked = 0
    full_signed_checks = 0
    for order in range(1, 6):
        denominator, pairs, transformed = prepare(order)
        common = denominator // 64 ** order
        antisymmetric = {}
        for axis in range(4):
            for direction in (-1, 1):
                vector = [0] * 4
                vector[axis] = direction
                antisymmetric[tuple(vector)] = direction

        def multiply(first, second):
            result = defaultdict(int)
            for u, a in first.items():
                for v, b in second.items():
                    result[tuple(x + y for x, y in zip(u, v))] += a * b
            return {v: a for v, a in result.items() if a}

        residual_base = multiply(antisymmetric, antisymmetric)
        residual_base[(0, 0, 0, 0)] += 64
        residual = {(0, 0, 0, 0): 1}
        accumulated = defaultdict(int)
        for j in range(1, order + 1):
            residual = multiply(residual, residual_base)
            scale = (common // j) * 64 ** (order - j)
            for vector, value in residual.items():
                if all(x % 2 == 0 for x in vector):
                    accumulated[tuple(x // 2 for x in vector)] += value * scale
        for vector in gap_vectors(order):
            if numerator(vector, order, pairs, transformed) != accumulated.get(vector, 0):
                raise AssertionError(("Canonical direct control", order, vector))
            checked += 1
        for vector, value in accumulated.items():
            canonical = tuple(sorted(map(abs, vector)))
            if numerator(canonical, order, pairs, transformed) != value:
                raise AssertionError(("Signed direct control", order, vector))
            full_signed_checks += 1
    return checked, full_signed_checks


def signed_pair_orbit(a, b):
    return {(s * x, t * y) for x, y in ((a, b), (b, a))
            for s in (-1, 1) for t in (-1, 1)}


def count_sorted_by_partitions(order):
    # Sorted four-tuples of sum n correspond to partitions with at most
    # four parts, equivalently parts of size at most four.
    counts = [1] + [0] * order
    for part in range(1, 5):
        for total in range(part, order + 1):
            counts[total] += counts[total - part]
    return sum(counts)


def main():
    direct, full_signed = direct_controls()
    if direct != 43:
        raise AssertionError(("Small canonical coverage", direct))
    order = 128
    denominator, pairs, transformed = prepare(order)
    print("Prepared independent residual weights and axis-interleaved pair counts", flush=True)
    free = numerator((0, 0, 0, 0), order, pairs, transformed)
    envelope = {}
    total_count = 0
    excluded = 0
    admissible_count = 0
    negative_count = 0
    for vector in gap_vectors(order):
        total_count += 1
        nonzero = [a for a in vector if a]
        if not nonzero or len(nonzero) == 1 or (len(nonzero) == 2 and nonzero[0] == nonzero[1]):
            excluded += 1
            continue
        value = numerator(vector, order, pairs, transformed)
        admissible_count += 1
        if value < 0:
            negative_count += 1
            projected_pairs = {(vector[i], vector[j]) for i in range(4) for j in range(i + 1, 4)}
            for projected in projected_pairs - {(0, 0)}:
                previous = envelope.get(projected)
                candidate = (-value, vector)
                if previous is None or candidate[0] > previous[0] or (candidate[0] == previous[0] and vector < previous[1]):
                    envelope[projected] = candidate
        if admissible_count % 100000 == 0:
            print(f"Independently computed {admissible_count} admissible Fourier classes", flush=True)
    if total_count != count_sorted_by_partitions(order) or total_count != 550968:
        raise AssertionError(("Full support count", total_count))
    if excluded != 193 or admissible_count != 550775 or negative_count != 232646:
        raise AssertionError(("Class coverage", excluded, admissible_count, negative_count))
    rows = []
    total = 0
    for (a, b), (value, witness) in sorted(envelope.items()):
        multiplicity = len(signed_pair_orbit(a, b))
        if multiplicity != (4 if a == 0 or a == b else 8):
            raise AssertionError(("Multiplicity", a, b, multiplicity))
        total += multiplicity * value
        rows.append({"projected_absolute_pair": [a, b], "multiplicity": multiplicity,
                     "maximum_negative_numerator": str(value), "witness": list(witness)})
    if len(rows) != 4158:
        raise AssertionError(("Envelope coverage", len(rows)))
    comparison = 25 * (free - total) - 71 * denominator
    if comparison <= 0:
        raise AssertionError("Threshold did not pass")
    expected = {"degree": order, "threshold": [71, 25],
                "common_denominator": str(denominator), "free_numerator": str(free),
                "negative_envelope_numerator": str(total),
                "comparison_25_free_minus_envelope_minus_71_den": str(comparison),
                "passed": True, "canonical_admissible_class_count": admissible_count,
                "negative_class_count": negative_count, "envelope": rows,
                "direct_control_degrees": [1, 2, 3, 4, 5],
                "direct_control_canonical_coefficients_checked": direct}
    native = json.loads(INPUT.read_text(encoding="utf-8"))
    if native != expected:
        raise AssertionError("Full native envelope certificate mismatch")
    envelope_floor = total * 10 ** 12 // denominator
    bound_floor = (free - total) * 10 ** 12 // denominator
    if envelope_floor != 114488225296 or bound_floor != 2842086038655:
        raise AssertionError(("Decimal rational enclosures", envelope_floor, bound_floor))
    old = json.loads((GROUP / "inputs" / "rank-two-moment-certificate.json").read_text(encoding="utf-8"))
    old_free = old["free_torus"]
    if Fraction(free, denominator) != Fraction(int(old_free["sum_numerator"]), int(old_free["sum_denominator"])):
        raise AssertionError("Previously independently recomputed free fraction mismatch")
    report = {"result": "PASS", "python": platform.python_version(),
              "all_native_fields_matched": True,
              "full_canonical_support_count": total_count,
              "excluded_shapes_count": excluded,
              "direct_canonical_coefficients": direct,
              "direct_signed_coefficients": full_signed,
              "envelope_floor_times_10_to_12": envelope_floor,
              "free_minus_envelope_floor_times_10_to_12": bound_floor,
              "old_free_fraction_matched": True,
              "native_payload": expected}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: all {admissible_count} Fourier classes and {len(rows)} maxima independently recomputed; every native field matched.")
    print(f"Direct controls: {direct} canonical and {full_signed} signed coefficients.")
    print(f"Exact enclosure floors: envelope {envelope_floor}; free-minus-envelope {bound_floor}.")
    print(OUTPUT)


if __name__ == "__main__":
    main()
