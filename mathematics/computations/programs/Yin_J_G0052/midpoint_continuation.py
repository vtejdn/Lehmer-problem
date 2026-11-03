"""Exact original quartic bridges through length 256, with true midpoint marks.

The full deterministic quotient-height proof is C573; the reversed original
state map is C423.  D37 retains the new finite interpretation and limitations.
This author calculation is not an independent implementation of experiment.py.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path

import experiment as original


MIDPOINT_TIMES = (16, 32, 64, 128)
LAST_TIME = 2 * max(MIDPOINT_TIMES)


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def original_coordinates(q):
    q0, q1, q2, q3 = q
    return (-q0 + q1 + q2 + q3, -q1 + q2 + q3, -q2 + q3, -q3)


def quadratic_coefficients(q):
    """Return integers A,B with |Psi(q)(zeta)|^2=(A+B*sqrt(13))/2."""
    a = original_coordinates(q)
    s = [sum(a[j] * a[j + ell] for j in range(4 - ell)) for ell in range(4)]
    cross = s[1] + s[2] + s[3]
    return 2 * (s[0] + s[2] + 3 * s[3]) + cross, -cross


def decimal_enclosure(value, scale=10**6):
    lower = F(original.floor(value * scale), scale)
    return [rational(lower), rational(lower + F(1, scale))]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=original._J_OUTPUT / "midpoint_continuation.json")
    args = parser.parse_args()
    height = original.floor(F(6, 5) + F(11, 30) * (LAST_TIME // 2))
    assert height == 48
    # Verify the reversed original edge map on the zero state and basis.
    for q in [(0, 0, 0, 0)] + [tuple(int(i == j) for i in range(4)) for j in range(4)]:
        for digit, target in original.successors(q):
            a, b, c, d = original_coordinates(target)
            assert (-d - digit, a + d, b + d, c + d) == original_coordinates(q)
    strips, constants = original.constants()
    states, edges, graph_stats = original.graph(height, strips)
    count = len(states)

    # Forward complete original integer weights; no renormalization at a wall.
    forward = [0] * count
    forward[0] = 1
    returns = [1]
    forward_marks = {}
    for time in range(1, LAST_TIME + 1):
        nxt = [0] * count
        for i, value in enumerate(forward):
            if value:
                for j, digit in edges[i]:
                    nxt[j] += value * (2 if digit == 0 else 1)
        forward = nxt
        returns.append(forward[0])
        if time in MIDPOINT_TIMES:
            forward_marks[time] = forward.copy()

    # Backward terminal weights are computed separately in original time.
    backward = [0] * count
    backward[0] = 1
    backward_marks = {}
    for time in range(1, max(MIDPOINT_TIMES) + 1):
        backward = [sum((2 if digit == 0 else 1) * backward[j]
                        for j, digit in row) for row in edges]
        assert backward[0] == returns[time]
        if time in MIDPOINT_TIMES:
            backward_marks[time] = backward.copy()

    sqrt_lo = F(3605551275463989, 10**15)
    sqrt_hi = F(3605551275463990, 10**15)
    assert sqrt_lo**2 < 13 < sqrt_hi**2
    quadratics = [quadratic_coefficients(q) for q in states]
    midpoint_rows = []
    for n in MIDPOINT_TIMES:
        weights = [a * b for a, b in zip(forward_marks[n], backward_marks[n])]
        total = sum(weights)
        assert total == returns[2 * n]
        anum = sum(weight * quad[0] for weight, quad in zip(weights, quadratics))
        bnum = sum(weight * quad[1] for weight, quad in zip(weights, quadratics))
        aa, bb = F(anum, 2 * total), F(bnum, 2 * total)
        mlo = aa + bb * (sqrt_lo if bb >= 0 else sqrt_hi)
        mhi = aa + bb * (sqrt_hi if bb >= 0 else sqrt_lo)
        assert 0 < mlo < mhi
        scaled_enclosure = [F(original.floor(mlo * 10**6 / n), 10**6),
                            F(original.ceil(mhi * 10**6 / n), 10**6)]
        assert scaled_enclosure[0] < mlo / n < mhi / n < scaled_enclosure[1]
        # Sign-reversed states and every complete bridge carry equal weights.
        weighted_coordinates = [sum(w * q[j] for w, q in zip(weights, states)) for j in range(4)]
        assert weighted_coordinates == [0, 0, 0, 0]
        overlap = F(total, returns[n] ** 2)
        midpoint_rows.append({
            "midpoint_time": n, "total_time": 2 * n,
            "complete_bridge_weight": total,
            "positive_midpoint_states": sum(w > 0 for w in weights),
            "overlap_D_n": rational(overlap),
            "overlap_rational_enclosure": decimal_enclosure(overlap),
            "moment_rational_part": rational(aa),
            "moment_sqrt13_part": rational(bb),
            "moment_integer_A_sum": anum,
            "moment_integer_B_sum": bnum,
            "moment_lower": rational(mlo), "moment_upper": rational(mhi),
            "scaled_moment_lower": rational(mlo / n),
            "scaled_moment_upper": rational(mhi / n),
            "scaled_moment_rational_enclosure": [rational(v) for v in scaled_enclosure],
            "zero_midpoint_probability": rational(F(weights[0], total)),
            "weighted_quotient_coordinate_means": weighted_coordinates,
        })

    # Renewal inversion retains all earlier zero visits in the return counts.
    first_returns = [0]
    for time in range(1, LAST_TIME + 1):
        value = returns[time] - sum(first_returns[j] * returns[time - j] for j in range(1, time))
        assert value >= 0
        first_returns.append(value)

    controls = {16: F(5339, 134217728), 32: F(504250923, 144115188075855872),
                64: F(121338835637214357477, 2658455991569831745807614120560689152)}
    for time, expected in controls.items():
        assert F(returns[time], 4**time) == expected
    selected_returns = {str(n): rational(F(returns[n], 4**n)) for n in (16, 32, 64, 128, 256)}
    # A negative finite test: if p_n < (upper beta)^(-n), then p_n < beta^(-n).
    beta_upper = F(1723, 1000)
    no_pressure_crossing = all(F(returns[n], 4**n) * beta_upper**n < 1 for n in range(1, LAST_TIME + 1))
    first_return_upper = sum(F(first_returns[n], 4**n) * beta_upper**n
                             for n in range(1, LAST_TIME + 1))
    first_return_lower = sum(F(first_returns[n], 4**n) * F(861, 500)**n
                             for n in range(1, LAST_TIME + 1))
    assert first_return_lower < first_return_upper < 1
    # C673's explicit G_m is <(55/2)m for every m>=256:
    # gamma^2<53, kappa<2/3, pi<4; the two decreasing ratios are checked at256.
    beta_lower = F(861, 500)
    assert 16 * beta_lower / (beta_lower - 1)**2 < 53
    assert F(7, 2)**2 < 13
    assert 53 * 4 * (F(256, 2) + F(2, 3)) < F(9, 16) * 256**2
    assert (1 + F(106, 3)) / 256 < F(1, 4)
    # The full dyadic identity then gives R^256*p256>=1/(55*256).
    radius_lower = F(1687, 1000)
    radius_certificate = 55 * 256 * F(returns[256], 4**256) * radius_lower**256
    assert radius_certificate < 1
    assert all(F(**row["scaled_moment_lower"]) > F(1, 5)
               for row in midpoint_rows if row["midpoint_time"] in (64, 128))
    payload = {
        "scope": {"polynomial_coefficients_ascending": [1, -1, -1, -1, 1],
                  "digit_integer_weights": {"-1": 1, "0": 2, "1": 1},
                  "digit_denominator": 4, "complete_return_times": [1, LAST_TIME],
                  "midpoint_times": MIDPOINT_TIMES, "deterministic_complete_height": height,
                  "state_cap": original.CAP},
        "constants": constants, "graph": graph_stats,
        "sqrt13_interval": [rational(sqrt_lo), rational(sqrt_hi)],
        "selected_complete_returns": selected_returns,
        "complete_return_integer_weights": returns,
        "complete_first_return_integer_weights": first_returns,
        "midpoints": midpoint_rows,
        "all_times_fail_strict_pressure_crossing": no_pressure_crossing,
        "pressure_test_beta_upper": rational(beta_upper),
        "partial_first_return_at_beta_lower_bracket": rational(first_return_lower),
        "partial_first_return_at_beta_upper_bracket": rational(first_return_upper),
        "partial_first_return_beta_interval_display": [
            rational(F(original.floor(first_return_lower * 10**6), 10**6)),
            rational(F(original.ceil(first_return_upper * 10**6), 10**6))],
        "strict_radius_lower": rational(radius_lower),
        "radius_certificate_product": rational(radius_certificate),
        "dyadic_G_coefficient_for_m_at_least_256": rational(F(55, 2)),
        "old_complete_controls_matched": sorted(controls),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(args.output)
    print(json.dumps({"graph": graph_stats, "complete_through": LAST_TIME,
                      "all_times_fail_strict_pressure_crossing": no_pressure_crossing,
                      "display_only": [{"n": row["midpoint_time"],
                          "D_n": float(F(**row["overlap_D_n"])),
                          "m_n_over_n": float(F(**row["scaled_moment_lower"]))}
                          for row in midpoint_rows]}, indent=2))


if __name__ == "__main__":
    main()
