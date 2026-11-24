"""Certify the catalogue cut, the three Salem signatures and the five higher degrees."""

from collections import Counter
from math import comb
from pathlib import Path
import sys


PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0144"))
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0185"))
from pilot import graeffe
from pole_catalogue import table_rows
from trace_control import SOURCE_HALF


def compare_measure(coefficients):
    degree = len(coefficients) - 1
    row = list(coefficients)
    numerator, denominator = 601, 500
    binomials = [comb(degree, k) for k in range(degree + 1)]
    for step in range(17):
        if sum(abs(value) for value in row) * denominator < numerator:
            return "below", step
        if any(abs(value) * denominator > numerator * bound
               for value, bound in zip(row, binomials)):
            return "above", step
        if step < 16:
            row = graeffe(row)
            numerator *= numerator
            denominator *= denominator
    raise ArithmeticError("The exact Graeffe comparisons did not decide a row.")


def trace_from_half(half):
    # Ascending coefficients for z^k+z^-k as a polynomial in u=z+z^-1.
    order = len(half) - 1
    trace = [half[-1]] + [0] * order
    previous, current = [2], [0, 1]
    for k in range(1, order + 1):
        for j, value in enumerate(current):
            trace[j] += half[order - k] * value
        following = [0] + current
        for j, value in enumerate(previous):
            following[j] -= value
        previous, current = current, following
    return trace


def grid_sign(poly, index, scale):
    # Homogeneous Horner evaluation at index/scale with a positive denominator.
    value = poly[-1]
    denominator = 1
    for coefficient in reversed(poly[:-1]):
        denominator *= scale
        value = value * index + coefficient * denominator
    if value == 0:
        raise ArithmeticError("A rational grid point is a trace root.")
    return 1 if value > 0 else -1


def count_real_traces(poly):
    scale = 1000
    interior = exterior = 0
    previous = grid_sign(poly, -3 * scale, scale)
    for j in range(-3 * scale + 1, 3 * scale + 1):
        current = grid_sign(poly, j, scale)
        if previous != current:
            if -2 * scale < j <= 2 * scale:
                interior += 1
            else:
                exterior += 1
        previous = current
    if interior + exterior != len(poly) - 1:
        raise ArithmeticError("Sign changes do not exhaust the trace degree.")
    return interior, exterior


def main():
    counts = Counter()
    higher = Counter()
    survivors = []
    maximum_step = 0
    for _, degree, _, _, coefficients in table_rows():
        if degree > 54:
            continue
        result, step = compare_measure(coefficients)
        maximum_step = max(step, maximum_step)
        if degree > 44:
            if result != "above":
                raise ArithmeticError(f"Unexpected small row of primitive degree {degree}.")
            higher[degree] += 1
            continue
        counts[result] += 1
        if result == "below":
            survivors.append(tuple(coefficients[:degree // 2 + 1]))
    if counts != {"below": 4, "above": 940} or len(set(survivors)) != 4:
        raise ArithmeticError("Unexpected strict-cut counts.")
    if tuple(SOURCE_HALF) not in survivors:
        raise ArithmeticError("The degree-18 nonreal-trace witness is absent.")
    if set(higher) != {46, 48, 50, 52, 54}:
        raise ArithmeticError("Missing higher-degree rows.")
    print(f"Strictly below 601/500: {counts['below']}; strictly above: {counts['above']}.")
    print(f"All higher rows strictly above, by degree: {dict(sorted(higher.items()))}.")
    print(f"Maximum number of Graeffe squarings: {maximum_step}.")
    for half in survivors:
        if half == tuple(SOURCE_HALF):
            print(f"{half}: J144 nonreal-trace input")
        else:
            interior, exterior = count_real_traces(trace_from_half(half))
            if exterior != 1:
                raise ArithmeticError("A remaining input is not a signed Salem minimum.")
            print(f"{half}: {interior} interior trace roots, {exterior} exterior")


if __name__ == "__main__":
    main()
