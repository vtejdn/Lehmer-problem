"""Exact integer arcsine-state recurrence proved in D25; no floating arithmetic."""

from math import comb


def trace_polynomial(p):
    if len(p) < 2 or not p[0] or not p[-1]:
        raise ValueError("The declared recurrence needs nonmonomial actual span >= 1")
    if any(type(a) is not int for a in p):
        raise TypeError("Integer coefficients required")
    d = len(p) - 1
    h = sum(abs(a) for a in p)
    correlations = [sum(p[i] * p[i + lag] for i in range(d + 1 - lag))
                    for lag in range(d + 1)]
    r = [h * h - correlations[0]] + [0] * d
    previous, current = [2], [0, 1]
    for lag in range(1, d + 1):
        for j, coefficient in enumerate(current):
            r[j] -= correlations[lag] * coefficient
        if lag < d:
            following = [0] + current
            for j, coefficient in enumerate(previous):
                following[j] -= coefficient
            previous, current = current, following
    if r[-1] != -p[0] * p[-1] or not r[-1]:
        raise ArithmeticError("Actual degree/leading coefficient mismatch")
    return h, r


def initial_state(d):
    return [comb(k, k // 2) if k % 2 == 0 else 0 for k in range(d + 1)]


def step(state, r, n, h_power):
    d = len(r) - 1
    if len(state) != d + 1 or d < 1 or n < 0:
        raise ValueError("Invalid declared state")
    extended = list(state)
    divisions = terms = 0
    numerator_bits = divisor_bits = 0
    extended_bits = max(abs(v).bit_length() for v in extended)
    for k in range(d + 1, 2 * d + 1):
        j = k - d - 1
        numerator = 0
        for lag, coefficient in enumerate(r):
            weight = 4 * (j + (n + 1) * lag) * coefficient
            if weight:
                index = j + lag - 1
                if not 0 <= index < len(extended):
                    raise ArithmeticError("Negative or unavailable moment index")
                numerator += weight * extended[index]
                terms += 1
        for lag in range(d):
            weight = (j + 1 + (n + 1) * lag) * r[lag]
            if weight:
                numerator -= weight * extended[j + lag + 1]
                terms += 1
        divisor = (j + 1 + (n + 1) * d) * r[d]
        if not divisor:
            raise ArithmeticError("Zero triangular coefficient")
        quotient, remainder = divmod(numerator, divisor)
        if remainder:
            raise ArithmeticError(f"Nonexact signed division at n={n}, k={k}")
        if abs(quotient) > (1 << k) * h_power:
            raise ArithmeticError(f"Extended-state size bound failed at n={n}, k={k}")
        divisions += 1
        numerator_bits = max(numerator_bits, abs(numerator).bit_length())
        divisor_bits = max(divisor_bits, abs(divisor).bit_length())
        extended_bits = max(extended_bits, abs(quotient).bit_length())
        extended.append(quotient)
    following = []
    for j in range(d + 1):
        value = 0
        for lag, coefficient in enumerate(r):
            if coefficient:
                value += coefficient * extended[j + lag]
                terms += 1
        following.append(value)
    return following, {
        "exact_divisions": divisions,
        "extended_size_checks": divisions,
        "term_accumulations": terms,
        "max_numerator_bits": numerator_bits,
        "max_divisor_bits": divisor_bits,
        "max_extended_state_bits": extended_bits,
    }


def compute(p, depth, retain_states=False, checkpoints=()):
    h, r = trace_polynomial(p)
    d = len(p) - 1
    state = initial_state(d)
    h_squared, h_power = h * h, 1
    history = [list(state)] if retain_states else None
    points = {}
    totals = {"exact_divisions": 0, "extended_size_checks": 0,
              "term_accumulations": 0, "state_size_checks": 0,
              "scalar_range_checks": 0, "scalar_monotonicity_checks": 0,
              "max_numerator_bits": 0, "max_divisor_bits": 0,
              "max_extended_state_bits": 0}
    for n in range(depth + 1):
        for k, value in enumerate(state):
            if abs(value) > (1 << k) * h_power:
                raise ArithmeticError(f"Stored-state size bound at n={n}, k={k}")
            totals["state_size_checks"] += 1
        if not 0 <= state[0] <= h_power:
            raise ArithmeticError(f"Scalar range bound at n={n}")
        totals["scalar_range_checks"] += 1
        if n in checkpoints:
            points[str(n)] = str(state[0])
        if n == depth:
            break
        next_state, information = step(state, r, n, h_power)
        if next_state[0] > h_squared * state[0]:
            raise ArithmeticError(f"Normalized scalar monotonicity at n={n}")
        totals["scalar_monotonicity_checks"] += 1
        for key, value in information.items():
            if key.startswith("max_"):
                totals[key] = max(totals[key], value)
            else:
                totals[key] += value
        state = next_state
        h_power *= h_squared
        if retain_states:
            history.append(list(state))
    return {"degree": d, "H": h, "R_ascending": r,
            "states": history, "checkpoints": points,
            "final_state": state, "checks": totals}
