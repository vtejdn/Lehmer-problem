"""One fixed test of genuine terminal root-to-pole intervals.

Only (O,V,W)=(10,18,27), s=-15/16 is used. The seven coarse parameters,
eta=2^-20, at most eight Newton steps, 128-bit ball arithmetic, and radius
2^-16 are fixed. No parameter or precision expansion is performed.
"""

import argparse
from fractions import Fraction as F
import json
from time import perf_counter

from negative_one_higher import chebyshev_polynomial, trace_differences
from negative_one_seven import relaxation_system


P = 19683
N = 9841
CUT_CELL = 1991
S = F(-15, 16)
ETA = F(1, 2**20)
FREE = (0, 65, 110, 112, 159, 221, 253)
FULL = ((66, 109), (160, 220), (254, 255))
TRIPLE = (10, 18, 27)
RADIUS = F(1, 2**16)
# Fixed dyadic proposal retained from the bounded three-step Newton run.
CENTER_NUMERATORS = (349236363733, 787334542439, 560980995009, 641270727983, 260181169280, 989387092080, 829862555069)
PRECONDITIONER_NUMERATORS = (
    (2512633332006, -2103145062129, 1600416396782, -1099452619399, 581198466793, -274197025007, 97051828926),
    (33305393017723, -23770375713416, 11048026309928, -719107375333, -2108499462226, 2989295473938, -1822165733995),
    (-392236937956884, 423515665805192, -275278659286077, 67033926548984, -44582045153412, -73640360190490, 89796656184153),
    (400210452566522, -422981498154578, 267830013456676, -62281509684909, 48894322323659, 71249606278320, -90918696063722),
    (12271978823711, 17202136589635, -11051036555018, -4157746558528, -2486474951891, 252520931179, 3442724667874),
    (13738049522320, 6594656008681, 4900412092121, 3859932193, -1121805985143, -1004646796301, -835000712114),
    (567309090249, 1542560526614, 950827585589, 1220029756992, 823304762221, 427781328361, 239429828878),
)


def cheb_values(value):
    previous, current = 2, value
    values = [current]
    for _ in range(2, 8):
        previous, current = current, value * current - previous
        values.append(current)
    return values


def cheb_derivatives(value):
    previous, current = 2, value
    dprevious, dcurrent = 0, 1
    values = [dcurrent]
    for _ in range(2, 8):
        previous, current, dprevious, dcurrent = current, value * current - previous, dcurrent, current + value * dcurrent - dprevious
        values.append(dcurrent)
    return values


def traces():
    differences = trace_differences([3, 4, 7, *TRIPLE])
    return [sum(coefficient * differences[j] for j, coefficient in enumerate(chebyshev_polynomial([F(0)] * (degree - 1) + [F(1)]))) for degree in range(1, 8)]


def overlap(left, right, a, b, zero):
    if right <= a or b <= left:
        return zero
    if left >= a:
        lower = left
    else:
        assert left < a
        lower = a
    if right <= b:
        upper = right
    else:
        assert right > b
        upper = b
    result = upper - lower
    assert result > 0
    return result


def numeric_proposal():
    import numpy as np
    start = perf_counter()
    poles = np.r_[-2., 2 * np.cos(2 * np.pi * np.arange(N, 0, -1) / P)]
    poles[N + 1 - P // 3] = -1.
    cut = poles[CUT_CELL]
    keep = np.arange(1, N + 1) != CUT_CELL
    left, right = poles[:-1][keep], poles[1:][keep]
    gaps = right - left
    full = sum(np.maximum(0, np.minimum(right, -2 + (b + 1) / 64) - np.maximum(left, -2 + a / 64)) for a, b in FULL)
    weights = np.array([np.maximum(0, np.minimum(right, -2 + (index + 1) / 64) - np.maximum(left, -2 + index / 64)) for index in FREE]).T
    eta = float(ETA)
    jacobian_weights = (1 - 2 * eta) * weights
    right_values = np.array(cheb_values(right))
    target = 2 * np.array(cheb_values(float(S))) - np.array(cheb_values(cut)) - np.array(traces(), dtype=float)
    old, _ = relaxation_system(TRIPLE, 256)
    old = np.array(old[1:], dtype=float)[:, 257:]
    full_indices = [index for a, b in FULL for index in range(a, b + 1)]
    theta = np.linalg.solve(old[:, FREE], -target - old[:, full_indices].sum(axis=1))

    def evaluate(parameters):
        roots = right - eta * gaps - (1 - 2 * eta) * (full + weights @ parameters)
        residual = (right_values - np.array(cheb_values(roots))).sum(axis=1) - target
        derivatives = cheb_derivatives(roots)
        derivatives[0] = np.ones_like(roots)
        jacobian = np.array(derivatives) @ jacobian_weights
        return residual, jacobian

    for iteration in range(8):
        assert perf_counter() - start < 60, "Fixed Newton time bound reached"
        residual, jacobian = evaluate(theta)
        correction = np.linalg.solve(jacobian, residual)
        print(json.dumps({"iteration": iteration, "residual_inf": float(np.max(np.abs(residual))), "correction_inf": float(np.max(np.abs(correction)))}), flush=True)
        theta -= correction
        assert np.all(theta > 0) and np.all(theta < 1), "Fixed seven-parameter domain left"
        if np.max(np.abs(correction)) < 1e-10:
            break
    residual, jacobian = evaluate(theta)
    center = [round(float(value) * 2**40) for value in theta]
    inverse = [[round(float(value) * 2**40) for value in row] for row in np.linalg.inv(jacobian)]
    print(json.dumps({"center_numerators": center, "preconditioner_numerators": inverse, "denominator": 2**40, "residual_inf": float(np.max(np.abs(residual))), "seconds": perf_counter() - start}), flush=True)


def verify():
    from flint import arb, ctx
    start = perf_counter()
    ctx.prec = 128
    assert len(CENTER_NUMERATORS) == len(PRECONDITIONER_NUMERATORS) == 7
    assert all(len(row) == 7 for row in PRECONDITIONER_NUMERATORS)
    center = [arb((value, -40)) for value in CENTER_NUMERATORS]
    box = [arb((value, -40), (1, -16)) for value in CENTER_NUMERATORS]
    preconditioner = [[arb((value, -40)) for value in row] for row in PRECONDITIONER_NUMERATORS]
    assert all(value > 0 and value < 1 for value in box)
    eta, factor = arb((1, -20)), 1 - 2 * arb((1, -20))
    angle = 2 * arb.pi() / P
    poles = [arb(-2)] + [arb(-1) if index == P // 3 else 2 * (angle * index).cos() for index in range(N, 0, -1)]
    assert len(poles) == N + 1 and all(left < right for left, right in zip(poles, poles[1:]))
    cut = poles[CUT_CELL]
    cut_bounds = (arb(-1609663) / 1000000, arb(-804831) / 500000)
    assert cut > cut_bounds[0] and cut < cut_bounds[1]
    coarse_free = [(arb(-2) + arb(index) / 64, arb(-2) + arb(index + 1) / 64) for index in FREE]
    coarse_full = [(arb(-2) + arb(a) / 64, arb(-2) + arb(b + 1) / 64) for a, b in FULL]
    full_indices = {index for a, b in FULL for index in range(a, b + 1)}
    assert full_indices.isdisjoint(FREE) and len(FREE) == len(set(FREE)) == 7
    residual = [arb(0) for _ in range(7)]
    jacobian = [[arb(0) for _ in range(7)] for _ in range(7)]
    count = 0
    for index in range(1, N + 1):
        if index == CUT_CELL:
            continue
        if index % 128 == 0:
            assert perf_counter() - start < 60, "Fixed interval verification time bound reached"
        left, right = poles[index - 1], poles[index]
        gap = right - left
        baseline = sum((overlap(left, right, a, b, arb(0)) for a, b in coarse_full), arb(0))
        weights = [overlap(left, right, a, b, arb(0)) for a, b in coarse_free]
        root_center = right - eta * gap - factor * (baseline + sum((weight * value for weight, value in zip(weights, center)), arb(0)))
        for j, (right_value, root_value) in enumerate(zip(cheb_values(right), cheb_values(root_center))):
            residual[j] += right_value - root_value
        active = [column for column, weight in enumerate(weights) if weight != 0]
        if active:
            root_box = right - eta * gap - factor * (baseline + sum((weight * value for weight, value in zip(weights, box)), arb(0)))
            derivative = cheb_derivatives(root_box)
            for j in range(7):
                for column in active:
                    jacobian[j][column] += derivative[j] * factor * weights[column]
        count += 1
    assert count == N - 1 == 9840
    target = [2 * a - b - arb(value.numerator) / value.denominator for a, b, value in zip(cheb_values(arb(-15) / 16), cheb_values(cut), traces())]
    residual = [value - rhs for value, rhs in zip(residual, target)]
    error = [sum((a * b for a, b in zip(row, residual)), arb(0)) for row in preconditioner]
    defect = [[arb(int(i == j)) - sum((preconditioner[i][k] * jacobian[k][j] for k in range(7)), arb(0)) for j in range(7)] for i in range(7)]
    displacement = max(value.abs_upper() for value in error)
    contraction = max(sum((value.abs_upper() for value in row), arb(0)).upper() for row in defect)
    radius = arb((1, -16))
    assert contraction < 1 and displacement + radius * contraction < radius
    assert perf_counter() - start < 60, "Fixed interval verification time bound reached"
    print("Verified 9840 genuine terminal intervals, the forbidden cut cell omitted, and all seven exact trace equations by contraction.")
    print("128-bit ball bounds: displacement", displacement, "Jacobian defect", contraction, "radius", radius)
    print("All seven coarse parameters remain strictly between 0 and 1; eta=2^-20 forces every selected root strictly inside its own actual pole cell.")
    print("Only (10,18,27), s=-15/16. No integer coefficients or resultant constraint is certified. Seconds", perf_counter() - start)


def endpoint_diagnostic():
    """Enclose the endpoint value on the same fixed box; add no equation."""
    from flint import arb, ctx
    start = perf_counter()
    ctx.prec = 128
    box = [arb((value, -40), (1, -16)) for value in CENTER_NUMERATORS]
    assert all(value > 0 and value < 1 for value in box)
    eta, factor = arb((1, -20)), 1 - 2 * arb((1, -20))
    angle = 2 * arb.pi() / P
    poles = [arb(-2)] + [arb(-1) if index == P // 3 else 2 * (angle * index).cos() for index in range(N, 0, -1)]
    cut = poles[CUT_CELL]
    coarse_free = [(arb(-2) + arb(index) / 64, arb(-2) + arb(index + 1) / 64) for index in FREE]
    coarse_full = [(arb(-2) + arb(a) / 64, arb(-2) + arb(b + 1) / 64) for a, b in FULL]
    logarithm = 2 * (2 + arb(-15) / 16).log() - (2 + cut).log()
    for index in range(1, N + 1):
        if index == CUT_CELL:
            continue
        if index % 128 == 0:
            assert perf_counter() - start < 60, "Fixed endpoint diagnostic time bound reached"
        left, right = poles[index - 1], poles[index]
        baseline = sum((overlap(left, right, a, b, arb(0)) for a, b in coarse_full), arb(0))
        weights = [overlap(left, right, a, b, arb(0)) for a, b in coarse_free]
        root_box = right - eta * (right - left) - factor * (baseline + sum((weight * value for weight, value in zip(weights, box)), arb(0)))
        assert root_box + 2 > 0 and right + 2 > 0
        logarithm += (2 + root_box).log() - (2 + right).log()
    value = logarithm.exp()
    assert value > arb(22) / 1000 and value < arb(23) / 1000
    assert perf_counter() - start < 60
    print("Endpoint diagnostic on the same entire 128-bit parameter box: log U =", logarithm)
    print("U =", value, "; U=1 is not imposed by the seven polynomial moments. Seconds", perf_counter() - start)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--propose", action="store_true")
    parser.add_argument("--endpoint", action="store_true")
    args = parser.parse_args()
    if args.propose:
        numeric_proposal()
    elif args.endpoint:
        endpoint_diagnostic()
    else:
        verify()
        endpoint_diagnostic()


if __name__ == "__main__":
    main()
