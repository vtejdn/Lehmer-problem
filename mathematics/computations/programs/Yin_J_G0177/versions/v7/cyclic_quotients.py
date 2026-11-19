"""The two cyclic quotient orders and their shortest modular approximations."""

import json
import runpy
from itertools import combinations
from math import gcd, isqrt, lcm
from pathlib import Path


GROUP = Path(__file__).resolve().parents[2]
QUARTIC = runpy.run_path(str(GROUP / "versions" / "v5" / "quartic_circuits.py"))
BASE = QUARTIC["BASE"]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v7" / "results.json"


def floor_sum(count, modulus, slope, offset):
    """Sum floor((slope*i + offset)/modulus) for 0 <= i < count."""
    total = 0
    while True:
        slope_quotient, slope = divmod(slope, modulus)
        offset_quotient, offset = divmod(offset, modulus)
        total += slope_quotient * count * (count - 1) // 2 + offset_quotient * count
        height = slope * count + offset
        if height < modulus:
            return total
        count, offset = divmod(height, modulus)
        modulus, slope = slope, modulus


def points_in_square(radius, modulus, residue):
    """Count one representative with positive second coordinate for a small square."""
    assert 0 <= 2 * radius < modulus
    count = 0
    for slope in (residue, -residue):
        count += (floor_sum(radius, modulus, slope, slope + radius)
                  - floor_sum(radius, modulus, slope, slope))
    return count


def cyclic_data(first, second):
    """Recover the proportionality residue from a Bezout identity for the first column."""
    order = gcd(*(first[i] * second[j] - first[j] * second[i]
                  for i, j in combinations(range(len(first)), 2)))
    assert order > 0
    content = residue = 0
    for a, b in zip(first, second):
        content, u, v = BASE["bezout"](content, a)
        residue = (u * residue + v * b) % order
    assert content == 1 and gcd(residue, order) == 1
    assert all((b - residue * a) % order == 0 for a, b in zip(first, second))

    # Every point in the candidate square has one-norm at most twice its radius.
    short, other = BASE["reduce_plane"]([order, 0], [-residue, 1])
    assert abs(short[0] * other[1] - short[1] * other[0]) == order
    ceiling = max(map(abs, short))
    candidates = BASE["short_vectors"]((short, other), 2 * ceiling)
    witness = min(candidates, key=lambda v: max(map(abs, v)))
    mu = max(map(abs, witness))
    assert mu <= ceiling and (witness[0] + residue * witness[1]) % order == 0
    assert mu <= isqrt(order)
    assert points_in_square(mu - 1, order, residue) == 0
    assert points_in_square(mu, order, residue) > 0
    return {"order": order, "residue": residue, "minimum": mu, "witness": witness}


def record(n):
    plus, minus = (line["coefficients"] for line in QUARTIC["records"](n, 8))
    edge = abs(plus[0] * minus[-1] + plus[-1] * minus[0])
    assert edge
    results = []
    for sign in (1, -1):
        first = QUARTIC["multiply"](plus, (1, sign))
        second = QUARTIC["multiply"](minus, (1, -sign))
        results.append(cyclic_data(first, second))
    plus_order, minus_order = (x["order"] for x in results)
    common = gcd(plus_order, minus_order)
    joint = lcm(plus_order, minus_order)
    assert 4 % common == 0 and edge % joint == 0
    return {"n": n, "edge": edge, "plus": results[0], "minus": results[1],
            "common": common, "residual_factor": edge // joint}


if __name__ == "__main__":
    primes = [n for n in range(13, 258) if all(n % d for d in range(2, isqrt(n) + 1))]
    exponents = sorted(set(primes).union((16, 32, 64, 128, 256)))
    rows = [record(n) for n in exponents]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(f"Computed the two quotient orders and exact congruence minima at {len(rows)} exponents.")
