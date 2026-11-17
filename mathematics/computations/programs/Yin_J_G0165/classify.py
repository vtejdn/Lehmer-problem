"""Exhaust the two reduced quadratic sources using exact standard-library arithmetic."""

import json
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
from itertools import groupby
from math import comb, gcd
from pathlib import Path
from tempfile import NamedTemporaryFile

J_DIR = Path(__file__).resolve().parent
OUTPUT = J_DIR.parents[1] / "outputs" / J_DIR.name / "classifications.json"
ONE = (1,)


def trim(poly):
    data = list(poly)
    while len(data) > 1 and data[-1] == 0:
        data.pop()
    return tuple(data)


def combine(a, b, multiplier=1):
    terms = list(a) + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        terms[i] += multiplier*x
    return trim(terms)


def multiply(a, b):
    result = [0] * (len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            result[i+j] += v*w
    return trim(result)


def divide_monic(poly, divisor):
    rem = list(poly)
    quotient = [0] * max(1, len(poly)-len(divisor)+1)
    for i in range(len(poly)-len(divisor), -1, -1):
        lead = rem[i+len(divisor)-1]
        quotient[i] = lead
        for j, value in enumerate(divisor):
            rem[i+j] -= lead*value
    return trim(quotient), trim(rem)


@cache
def cyclotomic(n):
    poly = (-1,) + (0,) * (n-1) + (1,)
    for div in range(1, n):
        if n % div == 0:
            poly, remainder = divide_monic(poly, cyclotomic(div))
            assert remainder == (0,)
    return poly


@cache
def trace_block(n):
    phi = cyclotomic(n)
    half = (len(phi)-1)//2
    assert n > 2 and phi == phi[::-1] and len(phi) == 2*half+1
    poly = (phi[half],)
    previous, current = (2,), (0, 1)
    for j in range(1, half+1):
        poly = combine(poly, current, phi[half+j])
        previous, current = current, combine((0,) + current, previous, -1)
    return poly


def evaluate(poly, x):
    result = 0
    for a in reversed(poly):
        result = x*result + a
    return result


def totients(limit):
    values = list(range(limit+1))
    for p in range(2, limit+1):
        if values[p] == p:
            for n in range(p, limit+1, p):
                values[n] -= values[n]//p
    return values


@dataclass(frozen=True)
class Product:
    orders: tuple
    angles: tuple
    coefficients: tuple


def all_products(orders, max_degree):
    by_degree = [[] for _ in range(max_degree+1)]
    by_degree[0].append(Product((), (), ONE))
    for n in orders:
        nodes = tuple(Fraction(a, n) for a in range(1, (n+1)//2) if gcd(a, n) == 1)
        block = trace_block(n)
        degree = len(nodes)
        assert degree == len(block)-1 and block[-1] == 1
        for target in range(max_degree, degree-1, -1):
            for old in by_degree[target-degree]:
                by_degree[target].append(Product(
                    old.orders + (n,), tuple(sorted(old.angles + nodes)),
                    multiply(old.coefficients, block)))
    return by_degree


def strict_interlacing(den, rem):
    return all(den[i] < angle < den[i+1] for i, angle in enumerate(rem))


def endpoints(den, rem, c):
    return tuple(x+c-Fraction(evaluate(rem, x), evaluate(den, x)) for x in (-2, 2))


def covers_quadratic(left, right, t, u):
    discriminant = t*t - 4*u
    low, high = 2*left+t, 2*right+t
    return low <= 0 and low*low >= discriminant and high >= 0 and high*high >= discriminant


def inverse_lift(den, rem, c, t, u):
    num = combine(multiply((c, 1), den), rem, -1)
    trace = combine(combine(multiply(num, num), multiply(num, den), t), multiply(den, den), u)
    deg = len(trace)-1
    lift = [0]*(2*deg+1)
    for j, value in enumerate(trace):
        for l in range(j+1):
            lift[deg-j+2*l] += value*comb(j, l)
    return tuple(lift)


def cyclotomic_factors(lift, possible_orders):
    residue = lift
    factors = []
    for n in possible_orders:
        phi = cyclotomic(n)
        while len(phi) <= len(residue):
            quo, rem = divide_monic(residue, phi)
            if rem != (0,):
                break
            factors.append(n)
            residue = quo
    assert residue == ONE, (lift, residue)
    return factors


def enumerate_maps():
    phi = totients(2*32**2)
    pole_orders = [n for n in range(3, 2*14**2+1) if phi[n] <= 14]
    output_orders = [n for n in range(1, len(phi)) if phi[n] <= 32]
    products = all_products(pole_orders, 7)
    hits, counts = [], {}
    sources = [("Y^2-Y-1", -1, -1, 7, (0, 1)), ("Y^2-2", 0, -2, 1, (0,))]
    for name, t, u, p_max, constants in sources:
        by_degree = []
        for p in range(1, p_max+1):
            pairs = 0
            raw_count = len(products[p])*len(products[p-1])
            before = len(hits)
            for den in products[p]:
                for rem in products[p-1]:
                    if not strict_interlacing(den.angles, rem.angles):
                        continue
                    pairs += 1
                    for c in constants:
                        left, right = endpoints(den.coefficients, rem.coefficients, c)
                        if not covers_quadratic(left, right, t, u):
                            continue
                        lift = inverse_lift(den.coefficients, rem.coefficients, c, t, u)
                        assert len(lift) == 4*(p+1)+1
                        hits.append({
                            "source": name, "B_orders": den.orders, "R_orders": rem.orders,
                            "c": c, "endpoint_values": [str(left), str(right)],
                            "full_degree": len(lift)-1,
                            "output_cyclotomic_orders": cyclotomic_factors(lift, output_orders),
                        })
            by_degree.append({
                "p": p, "products_B": len(products[p]), "products_R": len(products[p-1]),
                "candidate_pairs": raw_count, "interlacing_pairs": pairs,
                "endpoint_tests": pairs*len(constants), "presentations": len(hits)-before,
            })
        counts[name] = by_degree
    return {"allowed_pole_orders": pole_orders, "counts": counts, "presentations": hits}


def main():
    result = enumerate_maps()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=OUTPUT.parent, delete=False) as out:
        out.write(json.dumps(result, indent=2) + "\n")
        temp_path = Path(out.name)
    temp_path.replace(OUTPUT)
    for source, hits in groupby(result["presentations"], key=lambda rec: rec["source"]):
        hits = list(hits)
        print(source, len(hits), "presentations;", dict(sorted(Counter(r["full_degree"] for r in hits).items())))
        for row in hits:
            print(row["B_orders"], row["R_orders"], row["c"], row["output_cyclotomic_orders"])


if __name__ == "__main__":
    main()
