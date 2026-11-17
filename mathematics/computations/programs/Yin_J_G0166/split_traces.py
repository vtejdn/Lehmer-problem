"""Exact rational irreducibility certificates for ten prime-block inputs."""

from collections import Counter
from fractions import Fraction
from itertools import pairwise
import json
from math import comb, isqrt
from pathlib import Path


CASES = [(3, 307), (4, 577), (5, 431), (8, 601), (10, 431)]
PRIMES = (2, 3, 7, 11, 13, 17)


def quotient_at_root(coefficients, root):
    """Divide an ascending coefficient list exactly by X-root."""
    quotient = [0] * (len(coefficients) - 1)
    carry = coefficients[-1]
    for j in reversed(range(len(quotient))):
        quotient[j] = carry
        carry = coefficients[j] + root * carry
    assert carry == 0
    return quotient


def trace_polynomial(g, q, sign):
    parent = [0] * (q + g + 1)
    for degree, coefficient in [(q + g, 1), (q, -5), (q - g, 6),
                                (2 * g, 6 * sign), (g, -5 * sign), (0, sign)]:
        parent[degree] += coefficient
    core = parent
    for root in (1, -1):
        if sum(value * root**i for i, value in enumerate(core)) == 0:
            core = quotient_at_root(core, root)
    m = (len(core) - 1) // 2
    assert len(core) == 2 * m + 1 and core == core[::-1]
    trace = [core[m]] + [0] * m
    previous, current = [2], [0, 1]
    for j in range(1, m + 1):
        for i, value in enumerate(current):
            trace[i] += core[m + j] * value
        following = [0] + current
        for i, value in enumerate(previous):
            following[i] -= value
        previous, current = current, following
    rebuilt = [0] * len(core)
    for j, value in enumerate(trace):
        for k in range(j + 1):
            rebuilt[m - j + 2 * k] += value * comb(j, k)
    assert rebuilt == core and trace[-1] == 1
    return trace


def interior_interval(trace):
    def sign_at(point):
        value = 0
        for coefficient in reversed(trace):
            value = value * point + coefficient
        return (value > 0) - (value < 0)

    for left, right in pairwise(Fraction(j, 8) for j in range(-15, 16)):
        if sign_at(left) * sign_at(right) < 0:
            return [str(left), str(right)]
    raise ValueError("The selected rational grid has no strict sign change.")


def trim(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def divrem(a, b, p):
    """Polynomial division over F_p, with [] representing zero."""
    remainder = a.copy()
    quotient = [0] * max(0, len(a) - len(b) + 1)
    inverse = pow(b[-1], -1, p)
    for j in reversed(range(len(quotient))):
        value = remainder[len(b) - 1 + j] % p * inverse % p
        quotient[j] = value
        if value:
            for i, coefficient in enumerate(b):
                remainder[i + j] -= value * coefficient
    low = [value % p for value in remainder[:len(b) - 1]]
    return trim(quotient), trim(low)


def gcd_poly(a, b, p):
    while b:
        a, b = b, divrem(a, b, p)[1]
    inverse = pow(a[-1], -1, p)
    return [value * inverse % p for value in a]


def degree_pattern(trace, p):
    """Remove every degree j factor, including multiplicities, before j+1."""
    remaining = [value % p for value in trace]
    frobenius = [0, 1]
    degree = 1
    pattern = Counter()
    while 2 * degree <= len(remaining) - 1:
        raised = [0] * (p * (len(frobenius) - 1) + 1) if frobenius else []
        raised[::p] = frobenius
        frobenius = divrem(raised, remaining, p)[1]
        difference = frobenius + [0] * max(0, 2 - len(frobenius))
        difference[1] = (difference[1] - 1) % p
        layer = gcd_poly(remaining, trim(difference), p)
        while len(layer) > 1:
            assert (len(layer) - 1) % degree == 0
            pattern[degree] += (len(layer) - 1) // degree
            remaining, remainder = divrem(remaining, layer, p)
            assert not remainder
            layer = gcd_poly(remaining, layer, p)
        if len(remaining) > 1:
            frobenius = divrem(frobenius, remaining, p)[1]
        degree += 1
    if len(remaining) > 1:
        pattern[len(remaining) - 1] += 1
    assert sum(d * count for d, count in pattern.items()) == len(trace) - 1
    return pattern


def order(base, q):
    power = base % q
    for i in range(1, q):
        if power == 1:
            return i
        power = power * base % q
    raise ValueError("Base has no multiplicative order.")


def certificate(g, q, sign):
    assert q > 3 and all(q % j for j in range(2, isqrt(q) + 1))
    assert q > 7 * g and (q - 1) % g == 0
    orders = [order(base, q) for base in (2, 3)]
    assert all((q - 1) % (g * f) == 0 for f in orders)
    trace = trace_polynomial(g, q, sign)
    m = len(trace) - 1
    candidates = set(range(1, m // 2 + 1))
    steps = []
    for p in PRIMES:
        pattern = degree_pattern(trace, p)
        subset = 1
        for degree, count in pattern.items():
            for _ in range(count):
                subset |= subset << degree
        candidates = {d for d in candidates if (subset >> d) & 1}
        steps.append({"prime": p, "degree_counts": dict(sorted(pattern.items())),
                      "remaining_degrees": sorted(candidates)})
        if not candidates:
            break
    if candidates:
        raise ValueError(f"Insufficient modular degree data at {(g, q, sign)}")
    return {"g": g, "q": q, "sign": sign, "orders_2_3": orders, "trace_degree": m,
            "core_degree": 2 * m, "interior_sign_change": interior_interval(trace),
            "reductions": steps}


def main():
    results = [certificate(g, q, sign) for g, q in CASES for sign in (-1, 1)]
    folder = Path(__file__).resolve().parents[2] / "outputs" / "Yin_J_G0166"
    folder.mkdir(parents=True, exist_ok=True)
    output = folder / "certificates.json"
    temporary = output.with_suffix(".tmp")
    temporary.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output)
    for row in results:
        print(row["g"], row["q"], row["sign"], row["core_degree"],
              row["interior_sign_change"], [s["prime"] for s in row["reductions"]])


if __name__ == "__main__":
    main()
