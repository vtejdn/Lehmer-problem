"""Exact full Fourier-envelope candidate for the four-pair rank-two bound.

The sign-averaged order-N logarithm polynomial has Fourier support 2a,
||a||_1 <= N.  Its coefficient symmetry permits canonical nonnegative
sorted tuples.  A two-coordinate injection on a rank-two relation lattice
then bounds all negative coefficients by the projected-pair envelope.
This author program is not an independent review.
"""

import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import time


GROUP = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = GROUP / "inputs" / "rank-two-fourier-envelope.json"


def prepare(degree):
    common = math.lcm(*range(1, degree + 1))
    scale = 64 ** degree
    denominator = common * scale
    weights = [sum(common // j for j in range(1, degree + 1)) * scale]
    weights.extend((-1) ** k * math.comb(degree, k) * (common // k)
                   * 64 ** (degree - k) for k in range(1, degree + 1))
    binomials = [[math.comb(n, k) for k in range(n + 1)] for n in range(2 * degree + 1)]
    kernel = [[weights[l + m] * binomials[2 * (l + m)][2 * l]
               for m in range(degree - l + 1)] for l in range(degree + 1)]
    pairs = {}
    transforms = {}
    for a in range(degree // 2 + 1):
        for b in range(a, degree - a + 1):
            start = a + b
            pair = [binomials[2 * t][t + a + b] * binomials[2 * t][t + a - b]
                    for t in range(start, degree + 1)]
            pairs[a, b] = pair
            transforms[a, b] = [sum(row[m] * pair[m - start]
                                        for m in range(start, len(row)))
                                for row in kernel[:degree - start + 1]]
    return denominator, pairs, transforms


def coefficient_numerator(vector, degree, pairs, transforms):
    a, b, c, d = vector
    first = pairs[a, b]
    second = transforms[c, d]
    start = a + b
    value = sum(first[l - start] * second[l] for l in range(start, degree - c - d + 1))
    return (-1) ** sum(vector) * value


def direct_small_check(degree, denominator, pairs, transforms):
    """Direct multiplication, with no use of the pair transform formula."""
    if degree > 5:
        raise ValueError("The direct control is restricted to degrees at most five.")
    polynomial = {(0, 0, 0, 0): 1}
    common = math.lcm(*range(1, degree + 1))
    accumulated = {(0, 0, 0, 0): sum(common // j for j in range(1, degree + 1)) * 64 ** degree}
    for n in range(1, 2 * degree + 1):
        following = {}
        for vector, value in polynomial.items():
            for i in range(4):
                for direction in (-1, 1):
                    child = list(vector)
                    child[i] += direction
                    child = tuple(child)
                    following[child] = following.get(child, 0) + direction * value
        polynomial = {v: x for v, x in following.items() if x}
        if n % 2 == 0:
            k = n // 2
            # The (-1)^k from G^(2k)=(-1)^k F^(2k) cancels P's sign.
            weight = math.comb(degree, k) * (common // k) * 64 ** (degree - k)
            for vector, value in polynomial.items():
                if any(x % 2 for x in vector):
                    continue
                half = tuple(x // 2 for x in vector)
                accumulated[half] = accumulated.get(half, 0) + weight * value
    checked = 0
    for vector in itertools.combinations_with_replacement(range(degree + 1), 4):
        if sum(vector) <= degree:
            expected = accumulated.get(vector, 0)
            actual = coefficient_numerator(vector, degree, pairs, transforms)
            assert actual == expected, (degree, vector, actual, expected, denominator)
            checked += 1
    return checked


def calculate(degree=128):
    direct_checks = 0
    for control_degree in (1, 2, 3, 4, 5):
        data = prepare(control_degree)
        direct_checks += direct_small_check(control_degree, *data)
    started = time.monotonic()
    denominator, pairs, transforms = prepare(degree)
    print(f"Prepared exact pair transforms in {time.monotonic() - started:.2f} seconds", flush=True)
    free = coefficient_numerator((0, 0, 0, 0), degree, pairs, transforms)
    envelope = {}
    class_count = 0
    negative_classes = 0
    for a in range(degree // 4 + 1):
        for b in range(a, (degree - a) // 3 + 1):
            for c in range(b, (degree - a - b) // 2 + 1):
                for d in range(c, degree - a - b - c + 1):
                    vector = (a, b, c, d)
                    # Saturation plus admissibility excludes these shapes.
                    if a == b == 0 and (c == 0 or c == d):
                        continue
                    class_count += 1
                    value = coefficient_numerator(vector, degree, pairs, transforms)
                    if value >= 0:
                        continue
                    negative_classes += 1
                    for projected in set(itertools.combinations(vector, 2)):
                        if projected == (0, 0):
                            continue
                        if projected not in envelope or -value > envelope[projected][0]:
                            envelope[projected] = (-value, vector)
        if a % 4 == 0:
            print(f"Completed first coordinate {a}; {class_count} classes", flush=True)
    total = 0
    rows = []
    for (a, b), (value, witness) in sorted(envelope.items()):
        multiplicity = (1 if a == b else 2) * (1 if a == 0 else 2) * (1 if b == 0 else 2)
        total += multiplicity * value
        rows.append({"projected_absolute_pair": [a, b], "multiplicity": multiplicity,
                     "maximum_negative_numerator": str(value), "witness": list(witness)})
    # Independent integer count after substituting successive differences:
    # (a,b,c,d)=(a,a+x,a+x+y,a+x+y+z).
    canonical_count = sum(degree - 4 * a - 3 * x - 2 * y + 1
                          for a in range(degree // 4 + 1)
                          for x in range((degree - 4 * a) // 3 + 1)
                          for y in range((degree - 4 * a - 3 * x) // 2 + 1))
    assert class_count == canonical_count - (1 + degree + degree // 2)
    comparison = 25 * (free - total) - 71 * denominator
    print(f"Envelope={float(Fraction(total, denominator)):.12f}; "
          f"free-minus-envelope={float(Fraction(free-total, denominator)):.12f}; "
          f"passed={comparison > 0}", flush=True)
    return {"degree": degree, "threshold": [71, 25],
            "common_denominator": str(denominator), "free_numerator": str(free),
            "negative_envelope_numerator": str(total),
            "comparison_25_free_minus_envelope_minus_71_den": str(comparison),
            "passed": comparison > 0, "canonical_admissible_class_count": class_count,
            "negative_class_count": negative_classes, "envelope": rows,
            "direct_control_degrees": [1, 2, 3, 4, 5],
            "direct_control_canonical_coefficients_checked": direct_checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, default=128)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write-certificate", action="store_true")
    modes.add_argument("--verify-certificate", action="store_true")
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    args = parser.parse_args()
    if not 1 <= args.degree <= 128:
        parser.error("This program has a declared scope of degrees1 through128.")
    result = calculate(args.degree)
    if args.write_certificate:
        args.certificate.parent.mkdir(parents=True, exist_ok=True)
        with args.certificate.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    else:
        with args.certificate.open(encoding="utf-8") as stream:
            assert json.load(stream) == result
    print("Exact full-scope certificate " + ("written" if args.write_certificate else "recomputed and matched"))


if __name__ == "__main__":
    main()
