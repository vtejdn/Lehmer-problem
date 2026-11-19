"""Test reflected Newton sums on affine families of independently varying suffixes."""

import json
from fractions import Fraction
from itertools import product
from pathlib import Path


def coefficients(sums):
    coeff = [1]
    for k in range(1, len(sums) + 1):
        numerator = sum(coeff[k - j] * sums[j - 1] for j in range(1, k + 1))
        if numerator % k:
            raise ArithmeticError("Nonintegral Newton coefficient")
        coeff.append(-numerator // k)
    return coeff


def reflected_sums(half_coefficients, through):
    c = half_coefficients + half_coefficients[-2::-1]
    sums = [0]
    for k in range(1, through + 1):
        value = k * c[k] if k < len(c) else 0
        value += sum(c[i] * sums[k - i] for i in range(1, min(len(c), k)))
        sums.append(-value)
    return sums


def example(degree, bounds):
    half, m = degree // 2, 20
    horizon = 2 * m + 1
    primes = (5, 7, 11, 17, 23)
    # This legal base vector comes from a product of cyclotomic polynomials.
    original = [sum(q - 1 if k % q == 0 else -1 for q in primes)
                for k in range(1, half + 1)]
    prefix = original[:m]
    assert all(abs(s) <= b for s, b in zip(prefix, bounds))
    choices, base_sums = [], list(prefix)
    for j in range(m + 1, half + 1):
        lo, hi = -bounds[j - 1], bounds[j - 1]
        first = lo + (original[j - 1] - lo) % j
        choices.append(range((hi - first) // j + 1))
        base_sums.append(first)
    base = coefficients(base_sums)
    base_high = reflected_sums(base, horizon)
    inverse = [1]
    for k in range(1, m + 1):
        inverse.append(-sum(base[i] * inverse[k - i] for i in range(1, k + 1)))
    shifts = []
    for j in range(m + 1, half + 1):
        terms = [0] * (2 * half + 1)
        for i in range(j, half + 1):
            terms[i] = terms[2 * half - i] = base[i - j]
        shifts.append([k * sum(terms[i] * inverse[k - i] for i in range(j, k + 1))
                       for k in range(half + 1, horizon + 1)])
    target = Fraction(1091, 1000)
    caps = [int(degree - 2 + target**k + target**-k) for k in range(half + 1, horizon + 1)]
    entering = first_pass = through = 0
    for digits in product(*choices):
        high = [base_high[k] + sum(b * row[i] for b, row in zip(digits, shifts))
                for i, k in enumerate(range(half + 1, horizon + 1))]
        s = list(base_sums)
        for k, b in enumerate(digits, m + 1):
            s[k - 1] += k * b
        assert high == reflected_sums(coefficients(s), horizon)[half + 1:]
        entering += 1
        first_pass += abs(high[0]) <= caps[0]
        through += all(abs(a) <= cap for a, cap in zip(high, caps))
    assert prefix[0] == -5
    return {"prefix": prefix, "total": entering, "first_reflection": first_pass,
            "through_41": through}


if __name__ == "__main__":
    group = Path(__file__).resolve().parents[2]
    out = group.parents[1] / "outputs" / group.name / "versions" / "v7"
    boxes = json.loads((out / "boxes.json").read_text(encoding="utf-8"))
    report = {int(d): example(int(d), data["certified_all_available"]["bounds"])
              for d, data in boxes.items()}
    (out / "affine.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(report)
