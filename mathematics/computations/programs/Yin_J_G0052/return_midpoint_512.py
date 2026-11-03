"""Complete original quartic returns through 512 and true midpoint M_256.

Declared before execution: actual P=t^4-t^3-t^2-t+1; iid weights (1,2,1)/4;
all times 0..512, only midpoint 256; H=95 because 1426/15<96; at most
500000 reached states.  No change to experiment.CAP=100000 or old results.
The graph below copies the bounded original graph logic with this explicit
local cap; original.allowed/successors/constants and the C819 coordinate and
neutral-mark helpers are reused.  C573 supplies complete-return height and
real-strip validity; C423/C819 supplies the full original reversal bijection.
Real strips use outward 10^6 coefficient enclosures from beta in
(861/500,1723/1000).  Pressure tests refine that bracket by 40 exact bisections.
Stop incomplete at the state cap, process working set >=4 GiB, available
physical memory <1 GiB, unavailable memory monitoring, or any failed check.
Memory is checked every 4096 graph states and 16 DP steps (not a hard allocator
limit); there is no artificial elapsed-time limit.  Progress goes to stdout.
The complete JSON is published atomically only after all required checks.
An incomplete run publishes only a separate .incomplete.json with its scope,
stage, failure and useful return prefix.  It never replaces complete output.
No profile, larger graph, extrapolation, radius or critical-mean theorem runs.
"""
from __future__ import annotations

import argparse
from collections import deque
import ctypes
from fractions import Fraction as F
import json
import os
from pathlib import Path
import sys

import experiment as original
from midpoint_continuation import original_coordinates, quadratic_coefficients


LAST_TIME = 512
MIDPOINT_TIME = 256
HEIGHT = 95
STATE_CAP = 500000
WORKING_SET_LIMIT = 4 * 1024**3
AVAILABLE_MEMORY_FLOOR = 1024**3
SQRT_LO = F(3605551275463989, 10**15)
SQRT_HI = F(3605551275463990, 10**15)
SCOPE = {
    "polynomial_coefficients_ascending": [1, -1, -1, -1, 1],
    "digit_integer_weights": {"-1": 1, "0": 2, "1": 1},
    "digit_denominator": 4, "complete_return_times_including_zero": [0, LAST_TIME],
    "midpoint_times": [MIDPOINT_TIME], "deterministic_complete_height": HEIGHT,
    "state_cap": STATE_CAP, "old_helper_cap_unchanged": 100000,
    "working_set_stop_bytes": WORKING_SET_LIMIT,
    "available_physical_memory_stop_below_bytes": AVAILABLE_MEMORY_FLOOR,
    "memory_checks_graph_states": 4096, "memory_checks_dp_steps": 16,
    "real_strip_coefficient_scale": 10**6, "pressure_root_bisections": 40,
    "source_helpers": ["experiment.py:allowed/successors/constants",
                       "midpoint_continuation.py:original_coordinates/quadratic_coefficients"],
    "old_prefix_required_input": "midpoint_continuation.json",
    "output_vector_order": "quotient_states; same index for forward256 and backward256",
}


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def atomic_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(payload, stream, separators=(",", ":"))
        stream.write("\n")
    temporary.replace(path)


def memory_guard():
    """Live standard-library Windows monitor; unsupported systems stop honestly."""
    if os.name != "nt":
        raise RuntimeError("This declared native run requires Windows memory monitoring")
    class MemoryStatus(ctypes.Structure):
        _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong)] + [
            (name, ctypes.c_ulonglong) for name in
            ("total_physical", "available_physical", "total_pagefile",
             "available_pagefile", "total_virtual", "available_virtual", "extended_virtual")]
    class ProcessMemory(ctypes.Structure):
        _fields_ = [("size", ctypes.c_ulong), ("page_faults", ctypes.c_ulong)] + [
            (name, ctypes.c_size_t) for name in
            ("peak_working_set", "working_set", "peak_paged_pool", "paged_pool",
             "peak_nonpaged_pool", "nonpaged_pool", "pagefile", "peak_pagefile")]
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    kernel.GlobalMemoryStatusEx.argtypes = [ctypes.POINTER(MemoryStatus)]
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    psapi.GetProcessMemoryInfo.argtypes = [ctypes.c_void_p, ctypes.POINTER(ProcessMemory), ctypes.c_ulong]
    global_status = MemoryStatus()
    global_status.length = ctypes.sizeof(global_status)
    process_status = ProcessMemory()
    process_status.size = ctypes.sizeof(process_status)
    if not kernel.GlobalMemoryStatusEx(ctypes.byref(global_status)):
        raise OSError(ctypes.get_last_error(), "GlobalMemoryStatusEx failed")
    if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(process_status), process_status.size):
        raise OSError(ctypes.get_last_error(), "GetProcessMemoryInfo failed")
    if process_status.working_set >= WORKING_SET_LIMIT:
        raise RuntimeError("Declared 4-GiB process working-set stop reached")
    if global_status.available_physical < AVAILABLE_MEMORY_FLOOR:
        raise RuntimeError("Declared 1-GiB available-physical-memory floor reached")
    return {"working_set_bytes": process_status.working_set,
            "available_physical_bytes": global_status.available_physical}


def progress(stage, **fields):
    print(json.dumps({"stage": stage, **fields, **memory_guard()}), flush=True)


def bounded_graph(strips):
    """Original graph construction with a declared local cap, never monkey-patched."""
    states, indices, edges = [original.ZERO], {original.ZERO: 0}, []
    for i, q in enumerate(states):
        if i % 4096 == 0:
            memory_guard()
        if i % 65536 == 0:
            progress("graph_forward", processed=i, reached=len(states), cap=STATE_CAP)
        row = []
        for digit, target in original.successors(q):
            if not original.allowed(target, HEIGHT, strips):
                continue
            if target not in indices:
                if len(states) >= STATE_CAP:
                    raise RuntimeError(f"Reached-state cap {STATE_CAP} hit at H={HEIGHT}; incomplete")
                indices[target] = len(states)
                states.append(target)
            row.append((indices[target], digit))
        edges.append(row)
    del indices
    reverse = [[] for _ in states]
    for i, row in enumerate(edges):
        if i % 4096 == 0:
            memory_guard()
        for j, _ in row:
            reverse[j].append(i)
    can_return, queue = {0}, deque([0])
    processed = 0
    while queue:
        if processed % 4096 == 0:
            memory_guard()
        processed += 1
        for predecessor in reverse[queue.popleft()]:
            if predecessor not in can_return:
                can_return.add(predecessor)
                queue.append(predecessor)
    kept = sorted(can_return)
    remap = {j: i for i, j in enumerate(kept)}
    assert kept[0] == 0
    kept_states = [states[i] for i in kept]
    kept_edges = []
    for counter, i in enumerate(kept):
        if counter % 4096 == 0:
            memory_guard()
        kept_edges.append([(remap[j], digit) for j, digit in edges[i] if j in remap])
    statistics = {"height": HEIGHT, "full_box_states": (2 * HEIGHT + 1)**4,
                  "forward_reached_states": len(states), "returning_graph_states": len(kept),
                  "retained_edges": sum(map(len, kept_edges)), "cap": STATE_CAP}
    progress("graph_complete", **statistics)
    return kept_states, kept_edges, statistics


def main():
    # Exact refined-root endpoint fractions can exceed Python's decimal guard.
    # Only locally generated/declared integer evidence is serialized here.
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=original._J_OUTPUT / "return_midpoint_512.json")
    parser.add_argument("--prefix-input", type=Path, default=original._J_OUTPUT / "midpoint_continuation.json")
    args = parser.parse_args()
    status = {"status": "incomplete", "scope": SCOPE, "last_completed_stage": "not_started"}
    returns = []
    try:
        progress("scope_declared", **SCOPE)
        assert original.CAP == 100000
        assert F(6, 5) + F(11, 30) * MIDPOINT_TIME == F(1426, 15) < 96
        assert original.floor(F(1426, 15)) == HEIGHT
        assert SQRT_LO**2 < 13 < SQRT_HI**2
        old = json.loads(args.prefix_input.read_text(encoding="utf-8"))
        assert old["scope"]["complete_return_times"] == [1, 256]
        assert old["scope"]["polynomial_coefficients_ascending"] == SCOPE["polynomial_coefficients_ascending"]
        assert old["scope"]["digit_integer_weights"] == SCOPE["digit_integer_weights"]
        assert old["scope"]["digit_denominator"] == 4
        assert len(old["complete_return_integer_weights"]) == 257
        assert len(old["complete_first_return_integer_weights"]) == 257
        for q in [original.ZERO] + [tuple(int(i == j) for i in range(4)) for j in range(4)]:
            for digit, target in original.successors(q):
                a, b, c, d = original_coordinates(target)
                assert (-d - digit, a + d, b + d, c + d) == original_coordinates(q)
        strips, constants = original.constants()
        states, edges, graph_stats = bounded_graph(strips)
        status.update(last_completed_stage="graph", graph=graph_stats)
        count = len(states)
        forward = [0] * count
        forward[0] = 1
        returns = [1]
        forward256 = None
        for time in range(1, LAST_TIME + 1):
            nxt = [0] * count
            for i, value in enumerate(forward):
                if value:
                    for j, digit in edges[i]:
                        nxt[j] += value * (2 if digit == 0 else 1)
            forward = nxt
            returns.append(forward[0])
            if time <= 256:
                assert returns[time] == old["complete_return_integer_weights"][time]
            if time == MIDPOINT_TIME:
                forward256 = forward.copy()
            if time % 16 == 0:
                progress("forward", time=time, complete_through=time)
        del forward, nxt
        status["last_completed_stage"] = "forward512"
        backward = [0] * count
        backward[0] = 1
        for time in range(1, MIDPOINT_TIME + 1):
            backward = [sum((2 if digit == 0 else 1) * backward[j] for j, digit in row) for row in edges]
            assert backward[0] == returns[time]
            if time % 16 == 0:
                progress("backward", time=time)
        status["last_completed_stage"] = "backward256"
        total = anum = bnum = positive = 0
        means = [0, 0, 0, 0]
        for i, (q, left, right) in enumerate(zip(states, forward256, backward)):
            if i % 4096 == 0:
                memory_guard()
            weight = left * right
            if not weight:
                continue
            positive += 1
            total += weight
            aa, bb = quadratic_coefficients(q)
            anum += weight * aa
            bnum += weight * bb
            for j in range(4):
                means[j] += weight * q[j]
        assert total == returns[512] and means == [0, 0, 0, 0]
        aa, bb = F(anum, 2 * total), F(bnum, 2 * total)
        mlo = aa + bb * (SQRT_LO if bb >= 0 else SQRT_HI)
        mhi = aa + bb * (SQRT_HI if bb >= 0 else SQRT_LO)
        assert 0 < mlo < mhi
        overlap = F(total, returns[256]**2)
        overlap_display = [F(original.floor(overlap * 10**6), 10**6),
                           F(original.floor(overlap * 10**6) + 1, 10**6)]
        moment_display = [F(original.floor(mlo * 10**6 / 256), 10**6),
                          F(original.ceil(mhi * 10**6 / 256), 10**6)]
        assert overlap_display[0] < overlap < overlap_display[1]
        assert moment_display[0] < mlo / 256 < mhi / 256 < moment_display[1]
        midpoint = {"midpoint_time": 256, "total_time": 512,
            "complete_bridge_integer_weight": total, "positive_midpoint_states": positive,
            "moment_integer_A_sum": anum, "moment_integer_B_sum": bnum,
            "moment_rational_part": rational(aa), "moment_sqrt13_part": rational(bb),
            "moment_lower": rational(mlo), "moment_upper": rational(mhi),
            "scaled_moment_lower": rational(mlo / 256), "scaled_moment_upper": rational(mhi / 256),
            "scaled_moment_rational_enclosure": [rational(x) for x in moment_display],
            "overlap_D_n": rational(overlap),
            "overlap_rational_enclosure": [rational(x) for x in overlap_display],
            "zero_midpoint_probability": rational(F(forward256[0] * backward[0], total)),
            "weighted_quotient_coordinate_means": means}
        first_returns = [0]
        for time in range(1, LAST_TIME + 1):
            value = returns[time] - sum(first_returns[j] * returns[time - j] for j in range(1, time))
            assert value >= 0
            first_returns.append(value)
        assert returns[:257] == old["complete_return_integer_weights"]
        assert first_returns[:257] == old["complete_first_return_integer_weights"]
        beta_lo, beta_hi = F(861, 500), F(1723, 1000)
        for _ in range(40):
            middle = (beta_lo + beta_hi) / 2
            value = original.poly(middle)
            assert value != 0
            if value < 0:
                beta_lo = middle
            else:
                beta_hi = middle
        assert original.poly(beta_lo) < 0 < original.poly(beta_hi)
        no_crossing = all(F(returns[n], 4**n) * beta_hi**n < 1 for n in range(1, 513))
        first_lo = sum(F(first_returns[n], 4**n) * beta_lo**n for n in range(1, 513))
        first_hi = sum(F(first_returns[n], 4**n) * beta_hi**n for n in range(1, 513))
        assert first_lo < first_hi
        first_display = [F(original.floor(first_lo * 10**6), 10**6),
                         F(original.ceil(first_hi * 10**6), 10**6)]
        payload = {"status": "complete", "scope": SCOPE, "constants": constants,
            "graph": graph_stats, "sqrt13_interval": [rational(SQRT_LO), rational(SQRT_HI)],
            "complete_return_integer_weights": returns,
            "complete_first_return_integer_weights": first_returns,
            "old_prefix_comparison": {"times_including_zero": [0, 256],
                "all_return_weights_equal": True, "all_first_return_weights_equal": True},
            "selected_complete_returns": {str(n): rational(F(returns[n], 4**n)) for n in (128, 256, 512)},
            "midpoint": midpoint, "quotient_states": states,
            "forward256": forward256, "backward256": backward,
            "pressure_beta_interval": [rational(beta_lo), rational(beta_hi)],
            "all_times_fail_strict_pressure_crossing": no_crossing,
            "partial_first_return_at_beta_lower_bracket": rational(first_lo),
            "partial_first_return_at_beta_upper_bracket": rational(first_hi),
            "partial_first_return_beta_interval_display": [rational(x) for x in first_display],
            "partial_first_return_upper_is_below_one": first_hi < 1}
        progress("all_checks_complete", graph=graph_stats, positive_midpoint_states=positive,
                 moment_over_n_interval=payload["midpoint"]["scaled_moment_rational_enclosure"],
                 overlap_interval=payload["midpoint"]["overlap_rational_enclosure"])
        atomic_json(args.output, payload)
        print(json.dumps({"status": "complete", "output": str(args.output), "graph": graph_stats,
              "p512": payload["selected_complete_returns"]["512"],
              "first_return_interval": payload["partial_first_return_beta_interval_display"],
              "all_times_fail_strict_pressure_crossing": no_crossing,
              "partial_first_return_upper_is_below_one": first_hi < 1}), flush=True)
    except BaseException as error:
        status.update(failure_type=type(error).__name__, failure=str(error),
                      completed_return_integer_weights=returns)
        incomplete = args.output.with_suffix(".incomplete.json")
        atomic_json(incomplete, status)
        raise


if __name__ == "__main__":
    main()
