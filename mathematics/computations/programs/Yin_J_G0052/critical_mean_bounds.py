"""Exact critical-time consequences of adopted C836 and C839.

Reads the existing complete 0..512 return/first-return arrays, not a graph.
The source file cap is 16 MiB and the declared prefix length stays 512.
All mathematical decisions use integers and Fraction; decimals are display only.
No author graph module is imported or executed. Completeness is the adopted
C836 input, not inferred from the consistency checks below.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sys

LAST = 512
INPUT_BYTE_CAP = 16 * 1024**2
T = F(68883, 40000)
X = F(172208381, 100000000)
DELTA = F(2894667437079809876755951, 302231454903657293676544000)
P512_NUM = 5298548391970129745344684892772394289057669827956111368871272718708030755799876567240009996275901111428878134985202079634126536883620984644784010837788567749143910392852997044503323399


def rational(q):
    return {"numerator": q.numerator, "denominator": q.denominator}


def evaluate(weights, z, moment=False):
    q, value = z / 4, F(0)
    for n in range(LAST, 0, -1):
        value = (value + (n if moment else 1) * weights[n]) * q
    return value


def main():
    sys.set_int_max_str_digits(20000)
    group = Path(__file__).resolve().parent
    repository = group.parents[3]
    outputs = repository / "mathematics" / "computations" / "outputs" / group.name
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=outputs / "return_midpoint_512.json")
    parser.add_argument("--output", type=Path, default=outputs / "critical_mean_bounds.json")
    args = parser.parse_args()
    if args.input.stat().st_size > INPUT_BYTE_CAP:
        raise ValueError("Declared 16 MiB source-input cap exceeded")
    source = json.loads(args.input.read_text(encoding="utf-8"))
    scope = source["scope"]
    assert source["status"] == "complete"
    assert scope["polynomial_coefficients_ascending"] == [1, -1, -1, -1, 1]
    assert scope["digit_integer_weights"] == {"-1": 1, "0": 2, "1": 1}
    assert scope["digit_denominator"] == 4
    assert scope["complete_return_times_including_zero"] == [0, LAST]
    W = source["complete_return_integer_weights"]
    V = source["complete_first_return_integer_weights"]
    assert len(W) == len(V) == LAST + 1
    assert W[0] == 1 and V[0] == 0 and W[1] == V[1] == 2
    assert all(type(n) is int and n >= 0 for n in W + V)
    assert W[LAST] == 32 * P512_NUM
    for n in range(1, LAST + 1):
        assert W[n] == sum(V[j] * W[n - j] for j in range(1, n + 1))
    del source

    root_value = X**4 - X**3 - X**2 - X + 1
    assert root_value > 0 and 1 < T < X < 2
    fbar, a0, epsilon0 = 1 - DELTA, 1 - X / 2, (X - T) / X
    eta_one = (DELTA - (X - T) / 2) / a0
    eta_one_floor = F(6889, 100000)
    assert eta_one > eta_one_floor > 0
    one_step_mean = T / 2 + a0 * T / (X - T) * sum(
        (eta_one_floor**j / j for j in range(1, 4)), F(0)
    )
    one_step_tail = a0 - (fbar - T / 2) / (1 - 10000 * epsilon0)
    mixed_norm = X * DELTA / (X - T)
    assert one_step_mean > 1939 and one_step_tail > F(1, 400)
    assert mixed_norm > 1872

    ft, fx, mt = evaluate(V, T), evaluate(V, X), evaluate(V, T, True)
    late_mass, late_transform = 1 - fx, fbar - ft
    assert 0 < late_transform < late_mass < 1
    eta = 1 - late_transform / late_mass
    mt_floor, mass_floor = F(2829, 500), F(45951, 1000000)
    eta_floor, transform_ceiling = F(1039, 5000), F(36403, 1000000)
    assert mt > mt_floor and late_mass > mass_floor
    assert eta > eta_floor and late_transform < transform_ceiling
    mean_floor = mt_floor + mass_floor * T / (X - T) * sum(
        (eta_floor**j / j for j in range(1, 5)), F(0)
    )
    tail_floor = mass_floor - transform_ceiling / (1 - 30000 * epsilon0)
    assert 30000 * epsilon0 < 1
    assert mean_floor > 2097 and tail_floor > F(1, 350)

    B = lambda r: (2 - r) * (4 - r) / (2 * r)
    coefficient = X**3 * (4 - X)**2 / 128
    gprime_floor = (2097 - (1 + 3 * B(T))) / coefficient
    phase_mean_floor = F(2096) / B(T) - 2
    stationary_zero_level_ceiling = (T + 8 / T - 5) / 2097
    assert gprime_floor > 10121 and phase_mean_floor > 11400
    assert stationary_zero_level_ceiling < F(1, 1500)

    payload = {
        "status": "complete",
        "scope": {
            "input": "return_midpoint_512.json",
            "prefix_times": [0, LAST], "source_input_byte_cap": INPUT_BYTE_CAP,
            "polynomial_coefficients_ascending": [1, -1, -1, -1, 1],
            "digit_integer_weights": {"-1": 1, "0": 2, "1": 1},
            "digit_denominator": 4, "new_graph_or_return_times": False,
            "arithmetic": "exact integers and rational numbers",
        },
        "constants": {"t0": rational(T), "x": rational(X), "delta0": rational(DELTA)},
        "root_upper_polynomial_value": rational(root_value),
        "input_checks": {"return_entries": len(W), "first_return_entries": len(V),
                         "all_512_renewal_equalities": True, "p512_control": True},
        "one_step": {
            "eta": rational(eta_one), "eta_floor": rational(eta_one_floor),
            "mean_floor": rational(one_step_mean), "mean_floor_exceeds_1939": True,
            "tail10000_floor": rational(one_step_tail), "tail_floor_exceeds_1_over_400": True,
            "mixed_critical_norm_floor": rational(mixed_norm),
            "mixed_norm_floor_exceeds_1872": True,
        },
        "prefix512": {
            "F_t0": rational(ft), "F_x": rational(fx), "M_t0": rational(mt),
            "late_mass_floor_exact": rational(late_mass),
            "late_transform_ceiling_exact": rational(late_transform), "eta": rational(eta),
            "coarse_bounds": {"M_t0_lower": rational(mt_floor), "late_mass_lower": rational(mass_floor),
                              "eta_lower": rational(eta_floor), "late_transform_upper": rational(transform_ceiling)},
            "mean_floor": rational(mean_floor), "mean_floor_exceeds_2097": True,
            "tail30000_floor": rational(tail_floor), "tail_floor_exceeds_1_over_350": True,
        },
        "consequences": {
            "gprime_floor": rational(gprime_floor), "gprime_floor_exceeds_10121": True,
            "positive_phase_mean_floor": rational(phase_mean_floor), "phase_mean_exceeds_11400": True,
            "finite_branch_zero_level_mass_ceiling": rational(stationary_zero_level_ceiling),
            "zero_level_ceiling_below_1_over_1500": True,
        },
        "display_only": {"prefix_F_t0": float(ft), "prefix_F_x": float(fx),
                         "prefix_M_t0": float(mt), "mean_floor": float(mean_floor),
                         "tail30000_floor": float(tail_floor)},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    try:
        temporary.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
        temporary.replace(args.output)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(json.dumps({"status": "complete", "output": str(args.output),
                      "mean_exceeds": 2097, "tail30000_exceeds": "1/350",
                      "gprime_exceeds": 10121, "phase_mean_exceeds": 11400,
                      "new_graph_or_return_times": False}))


if __name__ == "__main__":
    main()
