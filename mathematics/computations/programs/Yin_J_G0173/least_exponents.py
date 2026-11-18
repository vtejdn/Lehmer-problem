"""Compute the least half-mass exponent on Mossinghoff's June 2026 Salem table."""

import csv
from collections import Counter
from io import StringIO
from math import isqrt
from pathlib import Path
from tempfile import NamedTemporaryFile


GROUP = Path(__file__).resolve().parent
SOURCE = GROUP.parents[2] / "literature" / "pdf" / "Mos26b" / "SalemList.txt"
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "least_exponents.tsv"


def source_rows():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    header = ["Rank", "d", "Salem", "number", "Coefficients"]
    first = next(i + 1 for i, line in enumerate(lines) if line.split() == header)
    rows = []
    for line in lines[first:]:
        if not line.strip():
            continue
        rank, degree, sigma, *coefficients = line.split()
        rank, degree = int(rank), int(degree)
        half = list(map(int, coefficients))
        if rank != len(rows) + 1 or degree != 2 * (len(half) - 1) or half[0] != 1:
            raise ValueError(f"Unexpected source data at rank {rank}")
        rows.append((rank, degree, sigma, half))
    if len(rows) != 72:
        raise ValueError("The June 1 table has 72 ranks")
    return rows


def trace_at_zero(half):
    """Constant and linear coefficients of the monic trace polynomial over Z."""
    center_first = half[::-1]
    constant = center_first[0]
    linear = 0
    for j, coefficient in enumerate(center_first[1:], 1):
        sign = (-1) ** (j // 2)
        if j % 2:
            linear += sign * j * coefficient
        else:
            constant += sign * 2 * coefficient
    return constant, linear


def homogeneous_value(half, numerator, denominator):
    """Return denominator**degree * P(numerator / denominator) over Z."""
    full = half + half[-2::-1]
    value = full[0]
    scale = 1
    for coefficient in full[1:]:
        scale *= denominator
        value = numerator * value + coefficient * scale
    return value


def binary_remainder(a, modulus):
    while a and a.bit_length() >= modulus.bit_length():
        a ^= modulus << (a.bit_length() - modulus.bit_length())
    return a


def binary_gcd(a, b):
    while b:
        a, b = b, binary_remainder(a, b)
    return a


def power_of_x(exponent, modulus):
    """Square-and-multiply x in F_2[x]/modulus, stored as coefficient bits."""
    result = 1
    for digit in bin(exponent)[2:]:
        squared = 0
        for j in range(result.bit_length()):
            squared |= ((result >> j) & 1) << (2 * j)
        result = binary_remainder(squared << int(digit), modulus)
    return result


def possible_orders(s):
    orders = set()
    for f in range(1, s + 1):
        for group_size in (2**f - 1, 2**f + 1):
            for divisor in range(1, isqrt(group_size) + 1):
                if group_size % divisor == 0:
                    orders.update((divisor, group_size // divisor))
    return sorted(orders)


def binary_weights(half):
    full = half + half[-2::-1]
    modulus = sum((value % 2) << i for i, value in enumerate(reversed(full)))
    degree = len(full) - 1
    multiplicity_bound = 1 << (degree - 1).bit_length()
    weights = {}
    for n in possible_orders(degree // 2):
        power = power_of_x(n * multiplicity_bound, modulus)
        common_degree = binary_gcd(modulus, power ^ 1).bit_length() - 1
        if common_degree % 2:
            raise ArithmeticError("Inverse pairs must give even total multiplicity")
        weight = common_degree // 2 - sum(w for j, w in weights.items() if n % j == 0)
        if weight < 0:
            raise ArithmeticError("Negative exact-order weight")
        if weight:
            weights[n] = weight
    if sum(weights.values()) != degree // 2:
        raise ArithmeticError("The order census has missing multiplicity")
    return weights


def least_exponent(constant, linear, weights):
    w1 = weights.get(1, 0)
    if (w1 == 0) != (constant % 2 == 1):
        raise ArithmeticError("Binary and integral constant tests disagree")
    if w1 and (w1 == 1) != (linear % 2 == 1):
        raise ArithmeticError("Binary and integral simple-root tests disagree")
    if constant % 4 == 0 or (constant % 2 == 0 and linear % 2 == 0):
        return 1
    threshold = 2 if w1 == 0 else 1
    return min(n for n, w in weights.items() if n > 1 and w >= threshold)


def main():
    data = StringIO(newline="")
    writer = csv.writer(data, delimiter="\t", lineterminator="\n")
    writer.writerow(("rank", "degree", "source_decimal", "Q(0)", "Q'(0)",
                     "exact_order:weight", "least_exponent"))
    totals = Counter()
    below = Counter()
    for rank, degree, sigma, half in source_rows():
        if homogeneous_value(half, 7, 6) >= 0 or homogeneous_value(half, 49, 37) <= 0:
            raise ArithmeticError(f"Salem root outside the source interval at rank {rank}")
        if rank in (14, 37):
            separating_value = homogeneous_value(half, 9, 7)
            if (rank == 14 and separating_value <= 0) or (rank == 37 and separating_value >= 0):
                raise ArithmeticError("The two exponent-one inputs failed separation")
        constant, linear = trace_at_zero(half)
        weights = binary_weights(half)
        exponent = least_exponent(constant, linear, weights)
        if rank == 1 and (degree, weights, exponent) != (10, {31: 5}, 31):
            raise ArithmeticError("Lehmer polynomial control failed")
        profile = ",".join(f"{n}:{w}" for n, w in weights.items())
        writer.writerow((rank, degree, sigma, constant, linear, profile, exponent))
        totals[exponent] += 1
        if homogeneous_value(half, 13, 10) > 0 and degree <= 44:
            below[exponent] += 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                            dir=OUTPUT.parent, delete=False) as result:
        result.write(data.getvalue())
    Path(result.name).replace(OUTPUT)
    print(f"All {sum(totals.values())} rows: {dict(sorted(totals.items()))}")
    print(f"Below 1.3 through degree 44 ({sum(below.values())} rows): {dict(sorted(below.items()))}")


if __name__ == "__main__":
    main()
