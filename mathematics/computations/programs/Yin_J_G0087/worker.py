"""Exact critical-level geometry plus the reused L379/J86 integer recurrence.

All mathematical comparisons use integers/Fraction; floats occur only in clocks.
Every constant and moment enclosure is rounded outward to denominator 2**160.
"""

from fractions import Fraction as F
import importlib.util
import json
from math import comb, isqrt
import os
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import sys
from time import perf_counter

GROUP = (_J_PROGRAM / 'worker.py').parent
UPSTREAM = (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0086')
P = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
Q = [3, 4, -5, -5, 1, 1]
EXPECTED_R = [72, -24, 14, 70, 9, -64, -23, 20, 9, -2, -1]
H, D, N, PRECISION = 9, 10, 4096, 160
SCALE, LEVEL = 1 << PRECISION, F(1, 4)
POINTS = (0, 8, 64, 128, 256, 512, 1024, 2048, 4096)
START = float(sys.argv[1])
sys.set_int_max_str_digits(0)
PAYLOAD = {'complete': False, 'arithmetic': 'exact integers and rational intervals; outward 2^-160 grid', 'parameters': {'P_ascending': P, 'Q_ascending': Q, 'H': H, 'degree': D, 'N': N, 'precision_bits': PRECISION, 'b': ['1', '4'], 'root_grid': ['-2', '9/4', '1/64'], 'root_width': '1/1099511627776', 'max_bisections': 60, 'cover_cells_each': 128, 'arctan_terms': 64, 'atanh_terms': 128}, 'stage': 'input-gate'}


# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def clock_check():
    if perf_counter() - START >= 180:
        raise TimeoutError("The declared aggregate 180-second cap was reached")


def rat(value):
    value = F(value)
    return [str(value.numerator), str(value.denominator)]


def interval(value):
    return [rat(value[0]), rat(value[1])]


def down(value):
    value = F(value) * SCALE
    return value.numerator // value.denominator


def up(value):
    value = F(value) * SCALE
    return -((-value.numerator) // value.denominator)


def grid_interval(value):
    return [str(down(value[0])), str(up(value[1]))]


def publish(name):
    pass
    target = ((_J_PROGRAM if name in ('main.py', 'readme.md', 'worker.py') else _J_OUTPUT) / name)
    pending = target.with_suffix(target.suffix + ".pending")
    pending.write_text(json.dumps(PAYLOAD, indent=2) + "\n", encoding="utf-8")
    os.replace(pending, target)


def mul(left, right):
    products = [a * b for a in left for b in right]
    return min(products), max(products)


def square(value):
    a, b = value
    return (F(0) if a <= 0 <= b else min(a * a, b * b), max(a * a, b * b))


def evaluate(poly, x):
    answer = F(0)
    for coefficient in reversed(poly):
        answer = answer * x + coefficient
    return answer


def horner(poly, x):
    answer = (F(0), F(0))
    for coefficient in reversed(poly):
        answer = mul(answer, x)
        answer = answer[0] + coefficient, answer[1] + coefficient
    return answer


def isolate(name, poly):
    # Every exact grid root is added once. Sign-changing intervals exclude such
    # endpoints; degree exhaustion then proves all roots are simple and real.
    grid = [F(k, 64) for k in range(-128, 145)]
    values = [evaluate(poly, x) for x in grid]
    found = [(x, x) for x, value in zip(grid, values) if value == 0]
    found += [(grid[i], grid[i + 1]) for i in range(len(grid) - 1)
              if values[i] * values[i + 1] < 0]
    found.sort()
    need(len(found) == len(poly) - 1, name + ": degree-exhausting root count failed")
    need(all(found[i][1] < found[i + 1][0] for i in range(len(found) - 1)),
         name + ": distinct disjoint brackets failed")
    refined, data = [], []
    for left, right in found:
        initial = (left, right)
        initial_values = (evaluate(poly, left), evaluate(poly, right))
        count = 0
        while right - left > F(1, 1 << 40):
            clock_check()
            need(count < 60, name + ": bisection cap reached")
            middle = (left + right) / 2
            fl, fm = evaluate(poly, left), evaluate(poly, middle)
            if fm == 0:
                left = right = middle
            elif fl * fm < 0:
                right = middle
            else:
                left = middle
            count += 1
        fl, fr = evaluate(poly, left), evaluate(poly, right)
        need((left == right and fl == 0) or fl * fr < 0,
             name + ": final root sign check failed")
        refined.append((left, right))
        data.append({"initial": interval(initial), "initial_values": interval(initial_values),
                     "bracket": interval((left, right)), "endpoint_values": interval((fl, fr)),
                     "bisections": count})
    return refined, {"polynomial_ascending": poly, "degree": len(poly) - 1,
                     "root_count": len(refined), "roots": data}


def geometry():
    derivative = [i * Q[i] for i in range(1, len(Q))]
    polys = {"Q": Q, "Qprime": derivative,
             "4Qplus1": [4 * Q[0] + 1] + [4 * a for a in Q[1:]],
             "4Qminus1": [4 * Q[0] - 1] + [4 * a for a in Q[1:]]}
    roots, root_data = {}, {}
    PAYLOAD["geometry"] = {"root_isolation": root_data}
    for name, poly in polys.items():
        roots[name], root_data[name] = isolate(name, poly)
    critical = []
    for x in (-2, 2):
        value = evaluate(Q, F(x))
        need(abs(value) > LEVEL, "Endpoint level gate failed")
        critical.append({"point": str(x), "Q_value": rat(value)})
    for bracket in roots["Qprime"]:
        if bracket[1] < -2 or bracket[0] > 2:
            continue
        need(bracket[0] >= -2 and bracket[1] <= 2,
             "A critical bracket straddles a circle endpoint")
        value = horner(Q, bracket)
        need(value[0] > LEVEL or value[1] < -LEVEL,
             "Critical value interval does not certify b < b_star")
        critical.append({"bracket": interval(bracket), "Q_interval": interval(value)})
    PAYLOAD["geometry"]["critical_and_endpoint_gates"] = critical
    original_inside = [r for r in roots["Q"] if -2 < r[0] and r[1] < 2]
    exterior = [r for r in roots["Q"] if r[0] > 2]
    need(len(original_inside) == 4 and len(exterior) == 1,
         "Original trace-root location gate failed")
    level_inside = sorted((r, name) for name in ("4Qplus1", "4Qminus1")
                          for r in roots[name] if -2 < r[0] and r[1] < 2)
    need(len(level_inside) == 8, "Exactly eight interior level roots are required")
    covers, bounds = [], []
    PAYLOAD["geometry"]["covers"] = covers
    for i in range(4):
        (leftroot, lname), (rightroot, rname) = level_inside[2 * i:2 * i + 2]
        left, right = leftroot[0], rightroot[1]
        need(lname != rname and -2 < left < right < 2,
             "Cover endpoint levels or interior gate failed")
        need(leftroot[1] < original_inside[i][0] <= original_inside[i][1] < rightroot[0],
             "Cover does not enclose exactly its original trace root")
        if covers:
            need(F(*map(int, covers[-1]["cover"][1])) < left, "Covers are not disjoint")
        cells, signs, minima = [], [], []
        for j in range(128):
            clock_check()
            cell = (left + (right - left) * F(j, 128),
                    left + (right - left) * F(j + 1, 128))
            qprime = horner(derivative, cell)
            need(qprime[0] > 0 or qprime[1] < 0, "Derivative sign cell gate failed")
            signs.append(1 if qprime[0] > 0 else -1)
            xsquared = square(cell)
            weight = (4 - xsquared[1], 4 - xsquared[0])
            weighted = mul(weight, square(qprime))
            need(weighted[0] > 0, "Weighted derivative lower bound failed")
            minima.append(weighted[0])
            cells.append({"cell": interval(cell), "Qprime": interval(qprime),
                          "weighted_derivative_squared": interval(weighted)})
        need(len(set(signs)) == 1, "Derivative sign changes between cover cells")
        bound = min(minima)
        bounds.append(bound)
        covers.append({"cover": interval((left, right)), "left_level_polynomial": lname,
                       "right_level_polynomial": rname, "derivative_sign": signs[0],
                       "D_lower": rat(bound), "D_lower_grid": str(down(bound)), "cells": cells})
    return bounds


def atan_bounds(q):
    total = sum((F((-1) ** k, (2 * k + 1) * q ** (2 * k + 1)) for k in range(64)), F(0))
    remainder = F(1, 129 * q ** 129)
    return total, total + remainder  # 64 terms end with a negative term.


def sqrt_bounds(value):
    need(value >= 0, "Square root input is negative")
    value = F(value)
    scaled_numerator = value.numerator * SCALE * SCALE
    lower = isqrt(scaled_numerator // value.denominator)
    need(lower * lower * value.denominator <= scaled_numerator <
         (lower + 1) * (lower + 1) * value.denominator,
         "Neighboring integer-square check failed")
    upper = lower if lower * lower * value.denominator == scaled_numerator else lower + 1
    return lower, upper


def constants(bounds):
    a, c = atan_bounds(5), atan_bounds(239)
    pi_exact = (16 * a[0] - 4 * c[1], 16 * a[1] - 4 * c[0])
    pi_grid = down(pi_exact[0]), up(pi_exact[1])
    need(3 * SCALE < pi_grid[0] <= pi_grid[1] < 4 * SCALE, "Pi enclosure failed")
    log_partial = 4 * sum((F(1, (2 * k + 1) * 2 ** (2 * k + 1)) for k in range(128)), F(0))
    log_remainder = F(4, 257 * 2 ** 257) / F(3, 4)
    logarithm = down(log_partial), up(log_partial + log_remainder)
    pi_sqrt = sqrt_bounds(F(pi_grid[0], SCALE))[0]
    di_sqrts = [sqrt_bounds(value) for value in bounds]
    need(pi_sqrt > 0 and all(pair[0] > 0 for pair in di_sqrts), "Positive inverse-root gate failed")
    c_rational_upper = F(H * SCALE, pi_sqrt) * sum((F(SCALE, pair[0]) for pair in di_sqrts), F(0))
    c_upper = up(c_rational_upper)
    rho = 1 - LEVEL * LEVEL / (H * H)
    need(0 <= rho < 1, "Complement rho gate failed")
    geometric = rho ** (N + 1) / (2 * (N + 1) * (1 - rho))
    geometric_upper = up(geometric)
    need(isqrt(N) ** 2 == N, "Declared square cutoff changed")
    local_upper = up(F(c_upper, SCALE * isqrt(N)))
    tail_upper = local_upper + geometric_upper
    PAYLOAD["constants"] = {
        "scale": str(SCALE), "encoding": "grid integers divided by scale; rationals [num,den]",
        "atan_1_over_5_rational": interval(a), "atan_1_over_239_rational": interval(c),
        "pi_grid": list(map(str, pi_grid)), "sqrt_pi_lower_grid": str(pi_sqrt),
        "log9_partial_rational": rat(log_partial), "log9_remainder_upper": rat(log_remainder),
        "log9_grid": list(map(str, logarithm)),
        "sqrt_D_grid": [list(map(str, pair)) for pair in di_sqrts],
        "C_upper_grid": str(c_upper), "rho": rat(rho),
        "geometric_tail_upper_grid": str(geometric_upper),
        "local_tail_upper_grid": str(local_upper), "tail_upper_grid": str(tail_upper)}
    return logarithm, tail_upper


def direct_ct():
    # Independent original Laurent multiplication; no trace or recurrence call.
    symbol = {0: H * H}
    for i, a in enumerate(P):
        for j, b in enumerate(P):
            symbol[i - j] = symbol.get(i - j, 0) - a * b
    symbol = {k: value for k, value in symbol.items() if value}
    power, values = {0: 1}, []
    for n in range(1, 9):
        clock_check()
        following = {}
        for i, a in power.items():
            for j, b in symbol.items():
                following[i + j] = following.get(i + j, 0) + a * b
        power = {k: value for k, value in following.items() if value}
        need(all(abs(k) <= n * D and abs(v) <= H ** (2 * n) for k, v in power.items()),
             "Direct original Laurent Fourier bound failed")
        values.append(power.get(0, 0))
    PAYLOAD["direct_CT_control"] = {"range": [1, 8], "original_symbol": {str(k): v for k, v in sorted(symbol.items())},
                                    "numerators": list(map(str, values)), "equalities_checked": 0}
    return values


def upstream_gate():
    spec = importlib.util.spec_from_file_location("j86_fast_reused", (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0086/fast.py'))
    fast = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fast)
    reconstructed = [0] * 11
    for k, coefficient in enumerate(Q):
        for j in range(k + 1):
            reconstructed[5 + k - 2 * j] += coefficient * comb(k, j)
    need(reconstructed == P, "Original P = z^5 Q(z+z^-1) input mismatch")
    h, r = fast.trace_polynomial(P)
    need(h == H and r == EXPECTED_R, "Upstream recurrence trace normalization mismatch")
    squared = [0] * 11
    for i, a in enumerate(Q):
        for j, b in enumerate(Q):
            squared[i + j] += a * b
    need([H * H - squared[0]] + [-v for v in squared[1:]] == r, "R = H^2-Q^2 gate failed")
    comparison = json.loads(((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0086/comparison.json')).read_text(encoding="utf-8"))
    larger = json.loads(((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0086/lehmer1024.json')).read_text(encoding="utf-8"))
    need(comparison.get("complete") is True and comparison.get("mode") == "compare"
         and comparison.get("depth") == 64 and comparison.get("independent_state_equalities") == 1235,
         "Upstream n64 completed scope mismatch")
    need(larger.get("complete") is True and larger.get("mode") == "lehmer1024" and larger.get("depth") == 1024,
         "Upstream n1024 completed scope mismatch")
    small, big = comparison["cases"]["lehmer_degree_ten"], larger["cases"]["lehmer_degree_ten"]
    for data in (small, big):
        need(data["coefficients_ascending"] == P and data["H"] == H and data["degree"] == D
             and data["R_ascending"] == EXPECTED_R, "Upstream exact input scope mismatch")
    need(len(small["state_vectors"]) == 65 and all(len(row) == 11 for row in small["state_vectors"]),
         "Upstream n64 state shape mismatch")
    need(len(big["final_state"]) == 11 and big["n64_overlap_matched"] is True,
         "Upstream n1024 state shape/overlap mismatch")
    PAYLOAD["upstream"] = {"program": "../Yin_J_G0086/fast.py", "fixed_proof": "Yin_L_G0379_v1",
                           "independent_review": "Yin_R_G0205_v1", "R_ascending": r,
                           "overlaps": {"64": False, "1024": False}}
    return fast, r, {64: int(small["state_vectors"][64][0]),
                      1024: int(big["scalar_numerator_checkpoints"]["1024"])}


def moments(fast, r, control, overlaps):
    state, h_power = fast.initial_state(D), 1
    sums = [0, 0]
    terms, checkpoints = [], {}
    counts = {"exact_divisions": 0, "extended_size_checks": 0, "term_accumulations": 0,
              "state_size_checks": 0, "scalar_range_checks": 0, "scalar_monotonicity_checks": 0,
              "max_numerator_bits": 0, "max_divisor_bits": 0, "max_extended_state_bits": 0}
    PAYLOAD["moments"] = {"rounded_term_pairs_grid": terms, "scalar_numerator_checkpoints": checkpoints,
                          "checks": counts, "denominator_convention": "nu_n = I[n,0]/9^(2n); term = nu_n/n"}
    for n in range(N + 1):
        clock_check()
        for k, value in enumerate(state):
            need(abs(value) <= (1 << k) * h_power, f"Stored-state bound failed at n{n}, k{k}")
            counts["state_size_checks"] += 1
        need(0 <= state[0] <= h_power, f"Scalar range failed at n{n}")
        counts["scalar_range_checks"] += 1
        if n in POINTS:
            checkpoints[str(n)] = str(state[0])
        if n in overlaps:
            need(state[0] == overlaps[n], f"Upstream exact n{n} overlap failed")
            PAYLOAD["upstream"]["overlaps"][str(n)] = True
        if 1 <= n <= 8:
            need(state[0] == control[n - 1], f"Independent CT control failed at n{n}")
            PAYLOAD["direct_CT_control"]["equalities_checked"] += 1
        if n:
            numerator, denominator = state[0] * SCALE, n * h_power
            lower, remainder = divmod(numerator, denominator)
            upper = lower + (1 if remainder else 0)
            need(lower * denominator <= numerator <= upper * denominator and 0 <= upper - lower <= 1,
                 f"Outward summand inequality failed at n{n}")
            terms.append([str(lower), str(upper)])
            sums[0] += lower
            sums[1] += upper
        PAYLOAD["moments"]["last_checked_n"] = n
        PAYLOAD["moments"]["sum_grid"] = list(map(str, sums))
        if n % 512 == 0:
            publish("progress.json")
        if n == N:
            break
        following, info = fast.step(state, r, n, h_power)
        need(following[0] <= H * H * state[0], f"Normalized monotonicity failed at n{n}")
        counts["scalar_monotonicity_checks"] += 1
        for key, value in info.items():
            counts[key] = max(counts[key], value) if key.startswith("max_") else counts[key] + value
        state, h_power = following, h_power * H * H
    need(len(terms) == N and sums[1] - sums[0] <= N, "Full term retention/rounding width failed")
    PAYLOAD["moments"]["final_state"] = list(map(str, state))
    PAYLOAD["moments"]["total_rounding_width_grid"] = str(sums[1] - sums[0])
    return sums


def main():
    clock_check()
    fast, r, overlaps = upstream_gate()
    PAYLOAD["stage"] = "rational-geometry"
    bounds = geometry()
    publish("progress.json")
    PAYLOAD["stage"] = "constants-and-direct-control"
    logarithm, tail = constants(bounds)
    control = direct_ct()
    publish("progress.json")
    PAYLOAD["stage"] = "exact-moments"
    sums = moments(fast, r, control, overlaps)
    lower = F(logarithm[0], SCALE) - F(sums[1], 2 * SCALE) - F(tail, SCALE)
    t_bounds = (F(logarithm[0], SCALE) - F(sums[1], 2 * SCALE),
                F(logarithm[1], SCALE) - F(sums[0], 2 * SCALE))
    PAYLOAD["result"] = {"T4096_rational_interval": interval(t_bounds),
                         "mahler_lower_rational": rat(lower), "mahler_lower_grid": str(down(lower)),
                         "strictly_positive": lower > 0,
                         "scope": "one original Lehmer polynomial; no unrestricted gap conclusion",
                         "independent_whole_review": "pending"}
    clock_check()
    PAYLOAD["complete"] = True
    PAYLOAD["stage"] = "complete"
    pass
    publish("certificate.json")
    ((_J_OUTPUT / 'progress.json')).unlink(missing_ok=True)
    print(json.dumps({'complete': True, 'strictly_positive': lower > 0, 'mahler_lower_rational': rat(lower)}), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        PAYLOAD["complete"] = False
        PAYLOAD["failure"] = {'type': type(error).__name__, 'message': _record_text(str(error))}
        publish("failure.json")
        print(json.dumps({"complete": False, "failure": PAYLOAD["failure"],
                          "stage": PAYLOAD["stage"]}), flush=True)
        raise SystemExit(1)
