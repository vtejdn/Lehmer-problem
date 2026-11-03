"""Exact fourth moments and radial profiles for the fixed complete C819 bridges.

Same H=48, full time<=256, cap=100000 and midpoint times16,32,64,128.
No mutation of the prior program, output, graph law or state cap is performed.
D37 #complete-original-midpoint-profile-256 owns the new author argument.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import cmp_to_key
import json
from pathlib import Path

import experiment as original
from midpoint_continuation import original_coordinates, quadratic_coefficients


MIDPOINT_TIMES = (16, 32, 64, 128)
THRESHOLDS = (F(1, 20), F(1, 10), F(1, 5), F(1, 2), F(1), F(2))
SQRT_LO = F(3605551275463989, 10**15)
SQRT_HI = F(3605551275463990, 10**15)


def rational(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def sign_integer(x):
    return (x > 0) - (x < 0)


def sign_quadratic(x, y):
    """Exact sign of x+y*sqrt(13) for rational x,y; no floating comparison."""
    sx, sy = sign_integer(x), sign_integer(y)
    if not sy:
        return sx
    if not sx or sx == sy:
        return sy
    norm_sign = sign_integer(x * x - 13 * y * y)
    assert norm_sign != 0  # 13 is nonsquare and neither x nor y is zero.
    return sx * norm_sign


def enclose(a, b):
    lo = a + b * (SQRT_LO if b >= 0 else SQRT_HI)
    hi = a + b * (SQRT_HI if b >= 0 else SQRT_LO)
    assert lo <= hi
    scale = 10**6
    return {
        "rational_part": rational(a), "sqrt13_part": rational(b),
        "lower": rational(lo), "upper": rational(hi),
        "decimal_rational_enclosure": [rational(F(original.floor(lo * scale), scale)),
                                        rational(F(original.ceil(hi * scale), scale))],
    }


def quantile(mark_weights, probability, n, total):
    ordered = sorted(mark_weights, key=cmp_to_key(
        lambda x, y: sign_quadratic(x[0] - y[0], x[1] - y[1])))
    cumulative = 0
    for a, b in ordered:
        before = cumulative
        cumulative += mark_weights[a, b]
        if cumulative * probability.denominator >= total * probability.numerator:
            assert before * probability.denominator < total * probability.numerator
            return {"probability": rational(probability),
                    "scaled_squared_radius": enclose(F(a, 2 * n), F(b, 2 * n)),
                    "mass_strictly_below": rational(F(before, total)),
                    "mass_at_or_below": rational(F(cumulative, total))}
    raise AssertionError("Quantile was not reached")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=original._J_OUTPUT / "midpoint_profile.json")
    args = parser.parse_args()
    assert SQRT_LO**2 < 13 < SQRT_HI**2
    assert original.CAP == 100000
    strips, constants = original.constants()
    states, edges, graph_stats = original.graph(48, strips)
    assert graph_stats["forward_reached_states"] == 68211
    assert len(states) == 65893 and sum(map(len, edges)) == 114445
    count = len(states)
    forward = [0] * count
    forward[0] = 1
    returns, forward_marks = [1], {}
    for time in range(1, 257):
        nxt = [0] * count
        for i, value in enumerate(forward):
            if value:
                for j, digit in edges[i]:
                    nxt[j] += value * (2 if digit == 0 else 1)
        forward = nxt
        returns.append(forward[0])
        if time in MIDPOINT_TIMES:
            forward_marks[time] = forward.copy()
    backward = [0] * count
    backward[0] = 1
    backward_marks = {}
    for time in range(1, 129):
        backward = [sum((2 if digit == 0 else 1) * backward[j]
                        for j, digit in row) for row in edges]
        assert backward[0] == returns[time]
        if time in MIDPOINT_TIMES:
            backward_marks[time] = backward.copy()
    assert F(returns[64], 4**64) == F(121338835637214357477, 2**121)
    assert F(returns[128], 4**128) == F(241348810511898190541699791270635467354265589, 2**253)
    assert F(returns[256], 4**256) == F(264543412341747108848944040326875358997077741567393090275411759418849446982212078897310231, 2**504)
    marks = [quadratic_coefficients(q) for q in states]
    rows = []
    for n in MIDPOINT_TIMES:
        weights = [a * b for a, b in zip(forward_marks[n], backward_marks[n])]
        total = sum(weights)
        assert total == returns[2 * n]
        first_a = first_b = fourth_a = fourth_b = 0
        tail_weights = [0] * len(THRESHOLDS)
        tail_states = [0] * len(THRESHOLDS)
        tail_moment_a = [0] * len(THRESHOLDS)
        tail_moment_b = [0] * len(THRESHOLDS)
        distribution = defaultdict(int)
        positive_states = 0
        for weight, (a, b) in zip(weights, marks):
            if not weight:
                continue
            positive_states += 1
            assert sign_quadratic(a, b) >= 0
            first_a += weight * a
            first_b += weight * b
            fourth_a += weight * (a * a + 13 * b * b)
            fourth_b += weight * (2 * a * b)
            distribution[a, b] += weight
            for i, threshold in enumerate(THRESHOLDS):
                x = threshold.denominator * a - 2 * n * threshold.numerator
                y = threshold.denominator * b
                if sign_quadratic(x, y) >= 0:
                    tail_weights[i] += weight
                    tail_states[i] += 1
                    tail_moment_a[i] += weight * a
                    tail_moment_b[i] += weight * b
        assert sum(distribution.values()) == total
        assert all(tail_weights[i] >= tail_weights[i + 1] for i in range(len(THRESHOLDS) - 1))
        aa, bb = F(first_a, 2 * total), F(first_b, 2 * total)
        # The measured moment is not carried by only the far radial tails.
        assert sign_quadratic(first_a - 10 * tail_moment_a[4],
                              first_b - 10 * tail_moment_b[4]) > 0
        assert sign_quadratic(3 * first_a - 1000 * tail_moment_a[5],
                              3 * first_b - 1000 * tail_moment_b[5]) > 0
        if n in (64, 128):
            assert 2 * tail_weights[1] > total
        fourth = enclose(F(fourth_a, 4 * total * n * n), F(fourth_b, 4 * total * n * n))
        moment = enclose(aa / n, bb / n)
        assert sign_quadratic(F(fourth_a, 4 * total) - aa * aa - 13 * bb * bb,
                              F(fourth_b, 4 * total) - 2 * aa * bb) >= 0
        # C301's B_n coefficient is minus the present sqrt13 integer numerator.
        signed_ratio = -F(first_b, n * total)
        real_product = enclose(aa, -bb)
        assert F(**real_product["lower"]) > -F(430500, 130321)
        assert F(**real_product["upper"]) < F(430500, 130321)
        rows.append({
            "midpoint_time": n, "total_time": 2 * n,
            "complete_bridge_integer_weight": total,
            "positive_midpoint_states": positive_states,
            "distinct_radial_marks": len(distribution),
            "scaled_second_moment": moment,
            "scaled_fourth_moment": fourth,
            "fourth_integer_A_sum": fourth_a,
            "fourth_integer_B_sum": fourth_b,
            "C301_signed_ratio_B_over_nC": rational(signed_ratio),
            "C301_real_product_mean": real_product,
            "tail_at_1_contributes_less_than_one_tenth_of_second_moment": True,
            "tail_at_2_contributes_less_than_three_thousandths_of_second_moment": True,
            "tails": [{"threshold": rational(t), "comparison": ">=",
                       "integer_weight": tail_weights[i], "positive_states": tail_states[i],
                       "probability": rational(F(tail_weights[i], total)),
                       "probability_enclosure": enclose(F(tail_weights[i], total), F(0)),
                       "scaled_second_moment_on_tail": enclose(
                           F(tail_moment_a[i], 2 * total * n),
                           F(tail_moment_b[i], 2 * total * n))}
                      for i, t in enumerate(THRESHOLDS)],
            "quantiles": [quantile(distribution, p, n, total) for p in (F(1, 2), F(9, 10))],
        })
    payload = {"scope": {"polynomial_coefficients_ascending": [1, -1, -1, -1, 1],
                          "original_digit_weights": [1, 2, 1], "digit_denominator": 4,
                          "midpoint_times": MIDPOINT_TIMES, "max_total_time": 256,
                          "complete_height": 48, "state_cap": 100000,
                          "tail_thresholds": [rational(t) for t in THRESHOLDS]},
               "graph": graph_stats, "constants": constants,
               "sqrt13_interval": [rational(SQRT_LO), rational(SQRT_HI)], "midpoints": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(args.output)
    print(json.dumps({"display_only": [{"n": row["midpoint_time"],
        "fourth_over_n_squared": float(F(**row["scaled_fourth_moment"]["lower"])),
        "tail_probabilities": [float(F(**t["probability"])) for t in row["tails"]],
        "median_scaled_radius_squared": float(F(**row["quantiles"][0]["scaled_squared_radius"]["lower"])),
        "q90_scaled_radius_squared": float(F(**row["quantiles"][1]["scaled_squared_radius"]["lower"])),
        "C301_signed_ratio": float(F(**row["C301_signed_ratio_B_over_nC"]))} for row in rows]}, indent=2))


if __name__ == "__main__":
    main()
