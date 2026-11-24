"""Verify a cyclotomic multiple of L^160 with coefficient one-norm below 2^160."""

from lehmer_phi4 import cyclotomic, multiply


LEHMER = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
MULTIPLICITIES = [
    (2, 64), (3, 15), (4, 40), (5, 12), (6, 54),
    (10, 60), (12, 12), (14, 43), (15, 45), (21, 6),
    (22, 17), (26, 9), (33, 14), (35, 14), (48, 9),
    (54, 17), (55, 7), (76, 6), (77, 10), (80, 5),
]
EXPECTED_NORM = 1021447200076579342416613392732943233813204502112


def main():
    cofactor = [1]
    for order, count in MULTIPLICITIES:
        factor = cyclotomic(order)
        for _ in range(count):
            cofactor = multiply(factor, cofactor)
    value_at_one = sum(cofactor)
    if value_at_one != 2**104 * 3**15 * 5**12:
        raise ArithmeticError("Unexpected cofactor value at one")
    result = cofactor
    multiplicity = 160
    for _ in range(multiplicity):
        result = multiply(LEHMER, result)
    degree = len(result) - 1
    norm = sum(abs(coefficient) for coefficient in result)
    if degree != 5508 or norm != EXPECTED_NORM or 10 * norm >= 7 * 2**multiplicity:
        raise ArithmeticError("Degree, coefficient norm or strict bound differs")
    print(f"deg(C) = {len(cofactor) - 1}")
    print(f"C(1) = {value_at_one}")
    print(f"deg(L^160 C) = {degree}")
    print(f"||L^160 C||_1 = {norm}")
    print(f"2^160 = {2**multiplicity}")


if __name__ == "__main__":
    main()
