"""Certify M(V_k) > 41/20 on the fixed range -3 <= k <= 27."""

from math import comb
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Yin_J_G0144"))
from pilot import graeffe


def fourth_power(seed):
    coefficients = [1]
    for _ in range(4):
        product = [0] * (len(coefficients) + len(seed) - 1)
        for i, a in enumerate(coefficients):
            for j, b in enumerate(seed):
                product[i + j] += a * b
        coefficients = product
    return coefficients


def shifted_difference(k, left, right):
    left_shift = 4 * max(k, 0)
    right_shift = 4 * max(-k, 0)
    result = [0] * max(left_shift + len(left), right_shift + len(right))
    for i, coefficient in enumerate(left):
        result[left_shift + i] += coefficient
    for i, coefficient in enumerate(right):
        result[right_shift + i] -= coefficient
    while result[-1] == 0:
        result.pop()
    return result


def main():
    left = fourth_power([-1, -1, 0, 1])
    right = fourth_power([1, 0, -1, -1])
    ordinary = []
    for k in range(-3, 28):
        poly = shifted_difference(k, left, right)
        degree = len(poly) - 1
        if k == 0:
            assert (degree, poly[0], poly[-1]) == (11, 0, -4)
        for _ in range(8):
            poly = graeffe(poly)
        index = 1 if k == 1 else 3
        numerator = abs(poly[index]) * 20**256
        denominator = comb(degree, index) * 41**256
        if numerator <= denominator:
            raise ArithmeticError(f"failed coefficient certificate at k={k}")
        ratio_floor = numerator // denominator
        if k == 1:
            print(f"k=1, j=1: floor {ratio_floor}")
        else:
            ordinary.append((ratio_floor, k))
    minimum, minimizer = min(ordinary)
    print(f"other {len(ordinary)} inputs, j=3: minimum floor {minimum} at k={minimizer}")


if __name__ == "__main__":
    main()
