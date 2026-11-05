"""Independent exact recomputation of the fixed order-4096 torus certificate.

This verifier does not import or execute independent-torus.py.  Split the four
coordinates into two pairs.  The constant coefficient of the 2k-th power of
the two-coordinate sum is binom(2k,k)^2, by Vandermonde.  Consequently the
four-coordinate moment is sum_k binom(2n,2k) binom(2k,k)^2
binom(2n-2k,n-k)^2.  The program evaluates that convolution using its symmetry,
then evaluates each scaled binomial transform B_j by Horner's rule.  All
arithmetic is exact; only the prescribed final dyadic floors round downward.

The small-order control counts actual lattice walks, independently of the
convolution.  The mathematical interpretation is in Yin_C_G0863_v1.md.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import comb
from pathlib import Path


ORDER = 4096
BITS = 40


def exact_divide(numerator: int, denominator: int) -> int:
    quotient, remainder = divmod(numerator, denominator)
    if remainder:
        raise ArithmeticError("nonexact combinatorial recurrence")
    return quotient


def walk_control(max_order: int = 4) -> list[int]:
    origin = (0, 0, 0, 0)
    counts = {origin: 1}
    result = [1]
    for step in range(1, 2 * max_order + 1):
        following = defaultdict(int)
        for point, count in counts.items():
            for axis in range(4):
                for direction in (-1, 1):
                    target = list(point)
                    target[axis] += direction
                    following[tuple(target)] += count
        counts = following
        if step % 2 == 0:
            result.append(counts[origin])
    return result


def pair_convolution(order: int) -> list[int]:
    pair_moments = [comb(2 * k, k) ** 2 for k in range(order + 1)]
    result = []
    for n in range(order + 1):
        choose_even = 1
        total = 0
        for k in range(n // 2 + 1):
            term = choose_even * pair_moments[k] * pair_moments[n - k]
            total += term if 2 * k == n else 2 * term
            if k < n // 2:
                choose_even = exact_divide(
                    choose_even * (2 * n - 2 * k) * (2 * n - 2 * k - 1),
                    (2 * k + 1) * (2 * k + 2),
                )
        result.append(total)
        if n and n % 256 == 0:
            print(f"pair-convolution moments complete through {n}", flush=True)
    return result


def recompute(order: int, bits: int) -> dict:
    moments = pair_convolution(order)
    controls = walk_control()
    if moments[: len(controls)] != controls:
        raise ArithmeticError("direct lattice-walk control disagrees")
    denominator = 1 << bits
    lower = 0
    checkpoints = []
    for j in range(1, order + 1):
        choose = 1
        numerator = moments[0]
        for k in range(1, j + 1):
            choose = exact_divide(choose * (j - k + 1), k)
            signed = -moments[k] if k % 2 else moments[k]
            numerator = 64 * numerator + choose * signed
        power = 1 << (6 * j)
        if not 0 <= numerator <= power:
            raise ArithmeticError(f"moment-transform range fails at {j}")
        lower += (denominator * numerator) // (j * power)
        if j in (128, 256, 512, 1024, 2048, order):
            checkpoints.append({"order": j, "scaled_lower_sum": lower})
        if j % 256 == 0:
            print(f"Horner transforms and floors complete through {j}", flush=True)
    return {
        "order": order,
        "rounding_bits": bits,
        "scaled_lower_sum": lower,
        "denominator": denominator,
        "target_numerator": 81,
        "target_denominator": 25,
        "positive_integer_margin": 25 * lower - 81 * denominator,
        "checkpoints": checkpoints,
        "small_lattice_walk_moments": controls,
        "method": "two-coordinate convolution and Horner binomial transform; exact integers",
    }


def main() -> None:
    group = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", type=Path,
        default=group / "inputs" / "independent-torus-certificate.json",
    )
    args = parser.parse_args()
    expected = json.loads(args.input.read_text(encoding="utf-8-sig"))
    fields = (
        "order", "rounding_bits", "scaled_lower_sum", "denominator",
        "target_numerator", "target_denominator", "positive_integer_margin",
    )
    if set(expected) != set(fields) or any(type(expected[f]) is not int for f in fields):
        raise ValueError("certificate must contain exactly the seven integer fields")
    if (expected["order"], expected["rounding_bits"]) != (ORDER, BITS):
        raise ValueError("this verifier checks only order 4096 and rounding bits 40")
    actual = recompute(ORDER, BITS)
    for field in fields:
        if actual[field] != expected[field]:
            raise ArithmeticError(f"certificate disagrees at {field}: computed {actual[field]}")
    if actual["positive_integer_margin"] <= 0:
        raise ArithmeticError("the required strict 81/25 lower bound does not hold")
    actual["certificate_verified"] = True
    output = group.parent.parent / "outputs" / group.name / "independent-torus-verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(actual, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(actual, indent=2))


if __name__ == "__main__":
    main()
