"""Certified Newton sum bounds from logarithms of eleven integral polynomials."""

import json
from fractions import Fraction as F
from functools import lru_cache
from math import comb, log, sqrt
from pathlib import Path


POLYNOMIALS = (
    (1, 0), (1, 1), (1, 2), (1, 0, -2), (1, 1, -1), (1, 0, -3),
    (1, 1, -2, -1), (1, 0, -3, 1), (1, 1, -4, -4, 1),
    (1, 1, -4, -3, 3, 1), (1, 1, -5, -5, 4, 3),
)
WEIGHTS = (14768307, 49117397, 56247516, 3015563, 22586214, 5159352,
           15415127, 2119227, 5373559, 4126272, 4828564)
HALF_WEIGHT_DEN = 2 * 10**8
T = F(1089, 1000)
DEGREE = 10
COEFF_SCALE = 10**32
LOG_SCALE = 10**12
# Rational test points only.  Every proposed upper bound is proved separately.
WITNESSES = (F(-151265, 200000), F(-73260, 100000), F(-77560, 100000),
             F(-85013, 100000), F(-88573, 100000), F(-92220, 100000),
             F(-96553, 100000))


def ceildiv(num, den):
    return -((-num) // den)


SERIES_SCALE = 10**24


def core_log(num, den):
    """Integer bounds in units of 10^-24 for log(num/den), 1 <= num/den <= 2."""
    scale = SERIES_SCALE
    v_lo = (num-den)*scale // (num+den)
    v_hi = ceildiv((num-den)*scale, num+den)
    square_lo, square_hi = v_lo*v_lo // scale, ceildiv(v_hi*v_hi, scale)
    power_lo, power_hi = v_lo, v_hi
    lo = hi = 0
    for odd in range(1, 50, 2):
        lo += 2 * power_lo // odd
        hi += ceildiv(2 * power_hi, odd)
        power_lo = power_lo*square_lo // scale
        power_hi = ceildiv(power_hi*square_hi, scale)
    # The geometric bound on the unused odd powers starts at order 51.
    hi += ceildiv(9*scale, 4*51*3**51)
    return lo, hi


LOG_TWO = core_log(2, 1)


def log_bound(value, upper):
    """One end of 10^12 log(value), using integer range reduction and series."""
    num, den = value.numerator, value.denominator
    k = num.bit_length() - den.bit_length()
    if k >= 0:
        den <<= k
    else:
        num <<= -k
    if num < den:
        k -= 1
        num *= 2
    lo, hi = core_log(num, den)
    lb, ub = LOG_TWO if k >= 0 else LOG_TWO[::-1]
    lo += k*lb
    hi += k*ub
    if upper:
        return ceildiv(hi*LOG_SCALE, SERIES_SCALE)
    return lo*LOG_SCALE // SERIES_SCALE


def chebyshev():
    polys = [[1], [0, 1]]
    while len(polys) <= DEGREE:
        result = [0] + [2 * v for v in polys[-1]]
        for i, coeff in enumerate(polys[-2]):
            result[i] -= coeff
        polys.append(result)
    return polys


@lru_cache(maxsize=None)
def squared_moduli(radius):
    """Power coefficients in x=cos(theta), via symmetric Laurent expansions."""
    cosines = chebyshev()
    result = []
    for poly in POLYNOMIALS:
        m = len(poly) - 1
        laurent = [0] * (2 * m + 1)
        for degree, coeff in enumerate(reversed(poly)):
            for j in range(degree + 1):
                laurent[m + degree - 2 * j] += coeff * comb(degree, j)
        amplitudes = [c * radius**(i - m) for i, c in enumerate(laurent)]
        power = [F(0)] * (2 * m + 1)
        for k, basis in enumerate(cosines[:2 * m + 1]):
            correlation = sum(amplitudes[i] * amplitudes[i + k]
                              for i in range(len(amplitudes) - k))
            if k:
                correlation *= 2
            for j, coeff in enumerate(basis):
                power[j] += correlation * coeff
        result.append(power)
    return result


def upper_bernstein(power):
    # Substitute x=2u-1, then elevate the power polynomial to degree ten.
    shifted = [sum(power[i] * comb(i, j) * (-1)**(i-j)
                   for i in range(j, len(power))) * 2**j for j in range(len(power))]
    coeffs = []
    for k in range(DEGREE + 1):
        value = sum((shifted[j] * F(comb(k, j), comb(DEGREE, j))
                     for j in range(min(k+1, len(shifted)))), F(0))
        coeffs.append(ceildiv(value.numerator * COEFF_SCALE, value.denominator))
    return coeffs


def split(coeffs):
    left, right = [], []
    while len(coeffs) > 1:
        left.append(coeffs[0])
        right.append(coeffs[-1])
        coeffs = [ceildiv(a + b, 2) for a, b in zip(coeffs, coeffs[1:])]
    left.append(coeffs[0])
    right.append(coeffs[0])
    return left, right[::-1]


def cell_upper(net, weights, radius_sum, idx, depth):
    # log S <= log y + S/y - 1.  The resulting single polynomial retains
    # cancellation between slopes from different logarithms on this cell.
    denom = DEGREE * 2**depth
    total = []
    for i in range(DEGREE+1):
        xnum = -denom + 2 * (DEGREE * idx + i)
        total.append(HALF_WEIGHT_DEN * ceildiv(-radius_sum.numerator * xnum * LOG_SCALE,
                                                radius_sum.denominator * denom))
    for coeffs, weight in zip(net, weights):
        y = max(coeffs)
        if y <= 0:
            raise ArithmeticError("nonzero squared modulus has no positive majorant")
        offset = weight * log_bound(F(y, COEFF_SCALE), True)
        for i, value in enumerate(coeffs):
            total[i] += offset + ceildiv(weight * (value - y) * LOG_SCALE, y)
    return ceildiv(max(total), HALF_WEIGHT_DEN)


def witness_interval(polys, weights, radius_sum, x):
    initial = -radius_sum * x * LOG_SCALE
    lower = HALF_WEIGHT_DEN * (initial.numerator // initial.denominator)
    upper = HALF_WEIGHT_DEN * ceildiv(initial.numerator, initial.denominator)
    for poly, weight in zip(polys, weights):
        value = F(0)
        for coeff in reversed(poly):
            value = value * x + coeff
        if value <= 0:
            raise ValueError("a witness must avoid the logarithmic singularities")
        lower += weight * log_bound(value, False)
        upper += weight * log_bound(value, True)
    return lower // HALF_WEIGHT_DEN, ceildiv(upper, HALF_WEIGHT_DEN)


def guide(k, weights):
    """Floating point selects a rational witness.  It supplies no proof bound."""
    r = float(T**k)
    active = [(poly, w / 10**8) for poly, w in zip(POLYNOMIALS, weights) if w]

    def value(x):
        z = complex((r + 1/r)*x, (r - 1/r)*sqrt(max(0, 1-x*x)))
        total = -z.real
        for poly, weight in active:
            q = 0
            for c in poly:
                q = q*z+c
            if q == 0:
                return float("-inf")
            total += weight * log(abs(q))
        return total

    n = 1024
    points = [-1+2*i/n for i in range(n+1)]
    values = [value(x) for x in points]
    peaks = [(values[0], points[0]), (values[-1], points[-1])]
    for i in range(1, n):
        if values[i] < values[i-1] or values[i] < values[i+1]:
            continue
        left, right = points[i-1], points[i+1]
        for _ in range(34):
            x, y = (2*left+right)/3, (left+2*right)/3
            if value(x) > value(y):
                right = y
            else:
                left = x
        mid = (left+right)/2
        peaks.append((value(mid), mid))
    return F(round(max(peaks)[1] * 10**9), 10**9)


def certify(k, weights, x, margin):
    radius = T**k
    radius_sum = radius + 1 / radius
    active = [(p, w) for p, w in zip(squared_moduli(radius), weights) if w]
    polys = [p for p, _ in active]
    weights = [w for _, w in active]
    lower, witness_upper = witness_interval(polys, weights, radius_sum, x)
    cap = (lower // margin + 3) * margin
    pending = [([upper_bernstein(poly) for poly in polys], 0, 0)]
    leaves = max_depth = 0
    while pending:
        net, idx, depth = pending.pop()
        if cell_upper(net, weights, radius_sum, idx, depth) <= cap:
            leaves += 1
            max_depth = max(max_depth, depth)
            continue
        if depth >= 48:
            raise ArithmeticError(f"failed to certify proposed cap at k={k}, cell={idx}")
        halves = [split(coeffs) for coeffs in net]
        for side in (0, 1):
            pending.append(([pair[side] for pair in halves], 2 * idx + side, depth + 1))
    return {"k": k, "x": str(x), "lower": lower, "witness_upper": witness_upper,
            "upper": cap, "leaves": leaves, "depth": max_depth}


def main():
    group = Path(__file__).resolve().parent
    rows = [certify(k, WEIGHTS, WITNESSES[k] if k < len(WITNESSES) else F(-1), 10**6)
            for k in range(30)]
    fixed_degrees = {}
    for degree in (56, 58):
        half = degree // 2
        bounds = []
        for row in rows[1:half+1]:
            cap = (half - 1) * rows[0]["upper"] + row["upper"]
            bounds.append(cap // LOG_SCALE)
        fixed_degrees[str(degree)] = bounds
    weights_by_degree = json.loads((group / "refined_weights.json").read_text(encoding="utf-8"))
    degrees, refined = {}, {}
    for degree in (56, 58):
        name = str(degree)
        half = degree // 2
        weights_by_k = weights_by_degree[name]
        if len(weights_by_k) != half:
            raise ValueError(f"expected {half} weight vectors")
        refined[name], degrees[name] = [], []
        for k, weights in enumerate(weights_by_k, 1):
            if len(weights) != len(WEIGHTS) or any(type(w) is not int or w < 0 for w in weights):
                raise ValueError(f"invalid weights at degree {degree}, index {k}")
            unit, outer = [certify(j, weights, guide(j, weights), 10**7) for j in (0, k)]
            cap = ((half-1)*unit["upper"]+outer["upper"]) // LOG_SCALE
            degrees[name].append(min(fixed_degrees[name][k-1], cap))
            refined[name].append({"k": k, "unit": unit, "outer": outer})
    report = {"radius_limit": str(T), "log_scale": LOG_SCALE,
              "degrees": degrees, "fixed_degrees": fixed_degrees, "ellipse_maxima": rows,
              "refined_maxima": refined}
    target = group.parents[1] / "outputs" / group.name / "results.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"degrees": degrees, "leaves": sum(row["leaves"] for row in rows)}))


if __name__ == "__main__":
    main()
