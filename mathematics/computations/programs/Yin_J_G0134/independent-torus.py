"""Exact truncated-log upper bound for four independent sine characters.

Uses integer arithmetic only.  CT(F**(2*k)), F=sum(x_i+x_i**-1),
is binom(2*k,k)*sum_j binom(k,j)^2*binom(2*j,j)*binom(2*k-2*j,k-j).
For X=F**2/64, sum_{j=1}^J E[(1-X)**j]/j gives a lower bound
on log(64)-2*m(F).  Every term is rounded downward on a dyadic grid.
This program establishes only the displayed finite rational inequality;
the analytic interpretation is a separate mathematical argument.
"""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path


def moment(k: int, central: list[int]) -> int:
    choose = 1
    total = 0
    for j in range(k + 1):
        total += choose * choose * central[j] * central[k - j]
        if j < k:
            choose = choose * (k - j) // (j + 1)
    return central[k] * total


def certificate(order: int, bits: int) -> dict:
    central = [comb(2 * k, k) for k in range(order + 1)]
    moments = [moment(k, central) for k in range(order + 1)]
    assert moments[:4] == [1, 8, 168, 5120]
    scale = 1 << bits
    lower = 0
    checkpoints = []
    for j in range(1, order + 1):
        choose = 1
        numerator = 0
        for k in range(j + 1):
            term = (choose * moments[k]) << (6 * (j - k))
            numerator += -term if k % 2 else term
            if k < j:
                choose = choose * (j - k) // (k + 1)
        assert 0 <= numerator <= 1 << (6 * j)
        lower += (numerator << bits) // (j << (6 * j))
        if j in (128, 256, 512, 1024, 2048, order):
            checkpoints.append({"order": j, "scaled_lower_sum": lower})
    return {
        "order": order,
        "rounding_bits": bits,
        "scaled_lower_sum": lower,
        "denominator": scale,
        "target_numerator": 81,
        "target_denominator": 25,
        "strict_target_passed": 25 * lower > 81 * scale,
        "positive_integer_margin": 25 * lower - 81 * scale,
        "checkpoints": checkpoints,
        "arithmetic": "exact integers, downward dyadic rounding",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=4096)
    parser.add_argument("--bits", type=int, default=40)
    args = parser.parse_args()
    if args.order < 3 or args.bits < 1:
        parser.error("order >= 3 and bits >= 1 are required")
    result = certificate(args.order, args.bits)
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name / "independent-torus.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
