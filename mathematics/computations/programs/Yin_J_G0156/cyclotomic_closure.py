"""Generate every bounded-height representation of one certified reciprocal core.

For a monic even reciprocal, cyclotomic-free core F with exponent gcd one,
normalization can be reversed exactly as F(+/-z**k) times a monic reciprocal
cyclotomic product. Generation uses F, the output degree and the height only.
The finite comparison loads the known target partitions AFTER generation.
No proposals, Mahler roots, new certificates or performance experiment occur.
"""

from __future__ import annotations

import argparse
from functools import lru_cache, reduce
import json
from math import gcd
from pathlib import Path
import time

from flint import fmpz_poly

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
LEHMER = (1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1)
SECOND = (1, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 1)


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return tuple(result)


@lru_cache(None)
def cyclotomic_products(degree):
    """All monic reciprocal cyclotomic products at one even degree.

    Reuses J147's neutral enumeration: +/-1 have even multiplicities;
    every remaining order m obeys phi(m)**2 >= m/2. No intermediate
    height pruning is allowed because subsequent factors can cancel.
    """
    if type(degree) is not int or degree < 0 or degree % 2:
        raise ValueError("a nonnegative even cyclotomic degree is required")
    if degree == 0:
        return ((1,),)
    factors = [(1, -2, 1), (1, 2, 1)]
    for order in range(3, 2*degree**2+1):
        phi = tuple(map(int, fmpz_poly.cyclotomic(order)))
        if len(phi)-1 <= degree:
            assert phi == phi[::-1] and phi[0] == phi[-1] == 1
            factors.append(phi)
    layers = [set() for _ in range(degree+1)]
    layers[0].add((1,))
    for factor in factors:
        width = len(factor)-1
        for size in range(width, degree+1):
            layers[size].update(multiply(poly, factor) for poly in layers[size-width])
    return tuple(sorted(layers[degree]))


def generate(core, degree, height=4):
    """The caller supplies a certified cyclotomic-free normalized core."""
    core = tuple(core)
    core_degree = len(core)-1
    if (core_degree < 2 or core_degree % 2 or core != core[::-1]
            or core[0] != 1 or core[-1] != 1
            or any(type(a) is not int for a in core)
            or reduce(gcd, (i for i, a in enumerate(core) if i and a), 0) != 1):
        raise ValueError("an even monic reciprocal integer core with exponent gcd one is required")
    if type(degree) is not int or degree < core_degree or degree % 2:
        raise ValueError("an even output degree at least the core degree is required")
    if type(height) is not int or height < 1:
        raise ValueError("positive integer height required")
    prefixes, counts = set(), []
    for k in range(1, degree//core_degree+1):
        remainder = degree-k*core_degree
        cyclotomics = cyclotomic_products(remainder)
        accepted = 0
        for sign in (-1, 1):
            lifted = [0] * (k*core_degree+1)
            for i, a in enumerate(core):
                lifted[k*i] = a*sign**i
            for neutral in cyclotomics:
                polynomial = multiply(lifted, neutral)
                assert len(polynomial) == degree+1 and polynomial == polynomial[::-1]
                assert polynomial[0] == polynomial[-1] == 1
                if max(map(abs, polynomial)) <= height:
                    prefixes.add(polynomial[1:degree//2+1])
                    accepted += 1
        counts.append({"substitution_index": k, "cyclotomic_degree": remainder,
                       "neutral_product_count": len(cyclotomics),
                       "constructed_count": 2*len(cyclotomics), "accepted_count": accepted})
    return sorted(prefixes), counts


def self_test():
    assert cyclotomic_products(0) == ((1,),)
    assert set(cyclotomic_products(2)) == {
        (1,-2,1), (1,2,1), (1,1,1), (1,0,1), (1,-1,1)}
    prefixes, counts = generate(LEHMER, 10)
    assert len(prefixes) == 2 and counts[0]["neutral_product_count"] == 1
    for degree in (2,4,6,8,10):
        products = cyclotomic_products(degree)
        for product in products:
            content, factors = fmpz_poly(list(product)).factor()
            assert content == 1 and all(factor.is_cyclotomic() for factor, _ in factors)
            assert product == product[::-1] and len(product) == degree+1
    # A separate exact factorization checks reverse normalization, including k=2.
    import sampler
    checked = 0
    for core, degrees in ((LEHMER,(14,18,20)), (SECOND,(18,20))):
        for degree in degrees:
            prefixes, _ = generate(core, degree)
            for prefix in prefixes:
                polynomial = sampler.reciprocal_polynomial(list(prefix))
                _, factors = fmpz_poly(polynomial).factor()
                assert tuple(sampler.normalized_core(factors)) == core
                checked += 1
    return {"small_products_and_factorizations": "pass", "normalized_representations_checked": checked}


def compare():
    generated = []
    started = time.perf_counter()
    # Neither target prefixes nor census counts are consulted during generation.
    for degree in (18,20):
        for core in (LEHMER, SECOND):
            prefixes, counts = generate(core, degree)
            generated.append({"degree": degree, "core_coefficients_ascending": list(core),
                              "prefixes": [list(p) for p in prefixes], "construction_counts": counts})
    generation_seconds = time.perf_counter()-started
    reference_path = HERE / "inputs" / "degree_core_mass_states.json"
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    for row in generated:
        part = next(p for p in reference["target_partitions"] if p["degree"] == row["degree"])
        group = next(g for g in part["core_groups"] if g["core_coefficients_ascending"] == row["core_coefficients_ascending"])
        assert set(map(tuple,row["prefixes"])) == set(map(tuple,group["target_prefixes"]))
        row["count"] = len(row["prefixes"])
        row["exact_census_set_match"] = True
    return {"scope": "Complete representations from each supplied core; no discovery or timed search.",
            "height": 4, "generation_seconds": generation_seconds, "groups": generated}


def prepare():
    groups = []
    for degree in (24,30):
        started = time.perf_counter()
        prefixes, counts = generate(LEHMER, degree)
        groups.append({"degree": degree, "core_coefficients_ascending": list(LEHMER),
                       "count": len(prefixes), "construction_counts": counts,
                       "generation_seconds": time.perf_counter()-started,
                       "prefixes": [list(p) for p in prefixes]})
    return {"scope": "Deterministic template construction only; no stochastic or measure evaluation.",
            "height": 4, "groups": groups}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("self-test", "compare", "prepare"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "self-test":
        print(json.dumps(self_test()))
        return
    result = compare() if args.command == "compare" else prepare()
    destination = args.output or OUTPUT / ("cyclotomic_closure.json" if args.command == "compare" else "cyclotomic_closure_preparation.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({k: ([{name:value for name,value in row.items() if name != "prefixes"} for row in value]
                         if k == "groups" else value) for k,value in result.items()}))


if __name__ == "__main__":
    main()
