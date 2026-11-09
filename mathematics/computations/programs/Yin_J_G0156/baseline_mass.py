"""Exact target probabilities for the two fixed S10 sampling laws.

This verification calculation never supplies examples or scores to a learner.
The complete Newton cover and its proof are retained in Yin_J_G0147.
Only the box [-4,4]^(D/2) is counted here; all-height counts are not box counts.
"""

import argparse
from collections import Counter
from fractions import Fraction
import json
from math import comb, prod
from pathlib import Path
import subprocess
import sys
from time import perf_counter

from flint import fmpz_poly
from sampler import certify_polynomial, reciprocal_polynomial

HERE = Path(__file__).resolve().parent
PROGRAMS = HERE.parent
DEFAULT_OUTPUT = HERE.parent.parent / "outputs" / HERE.name / "baseline_mass.json"
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0144"))
from pilot import graeffe


def strict_threshold(coefficients):
    """The exact whole-measure 6/5 test from J147, without its SymPy imports."""
    degree = len(coefficients) - 1
    binomials = [comb(degree, j) for j in range(degree + 1)]
    for numerator in (6, -6):
        value = denominator = 1
        for coefficient in coefficients[1:]:
            denominator *= 5
            value = numerator * value + denominator * coefficient
        if value < 0:
            return "above"
    squared = list(coefficients)
    for step in range(19):
        num, den = 6 ** (1 << step), 5 ** (1 << step)
        if any(den * abs(a) > num * b for a, b in zip(squared, binomials)):
            return "above"
        if den * den * sum(a * a for a in squared) < num * num:
            return "below"
        if step < 18:
            squared = graeffe(squared)
    raise ArithmeticError(("unresolved strict 6/5 threshold", coefficients))


def neutral(coefficients):
    polynomial = fmpz_poly(list(coefficients))
    content, factors = polynomial.factor()
    assert content == 1
    reconstructed = fmpz_poly([1])
    for factor, multiplicity in factors:
        reconstructed *= factor ** multiplicity
    assert reconstructed == polynomial
    return all(factor.is_cyclotomic() for factor, _ in factors)


def as_json(value):
    return {"numerator": value.numerator, "denominator": value.denominator,
            "decimal": float(value)}


def census(degree):
    start = perf_counter()
    result = json.loads(subprocess.run(
        ["node", str(PROGRAMS / "Yin_J_G0147" / "newton.cjs"), str(degree)],
        capture_output=True, text=True, check=True, timeout=180).stdout)
    assert result["degree"] == degree
    half = degree // 2
    prefixes = [tuple(a) for a in result["survivors"] if max(map(abs, a)) <= 4]
    assert len(prefixes) == len(set(prefixes))
    counts = Counter()
    targets = []
    for prefix in prefixes:
        coefficients = (1, *prefix, *reversed(prefix[:-1]), 1)
        if neutral(coefficients):
            counts["neutral"] += 1
            continue
        label = strict_threshold(coefficients)
        counts[label] += 1
        if label == "below":
            targets.append(list(prefix))
    assert sum(counts.values()) == len(prefixes)
    count = len(targets)
    # Separate complete-value certification cross-checks every strict target.
    # Cores organize this verification output; no reference reaches the learner.
    cores = {}
    for prefix in targets:
        certificate = certify_polynomial(reciprocal_polynomial(prefix))
        assert not certificate["neutral"] and certificate["thresholds"]["6/5"] == "below"
        core = tuple(certificate["core_coefficients_ascending"])
        entry = cores.setdefault(core, {
            "core_coefficients_ascending": list(core), "count": 0,
            "product_weight": 0, "measure_interval": certificate["measure_interval"],
            "measure_ball": certificate["measure_ball"],
        })
        entry["count"] += 1
        entry["product_weight"] += prod(2 ** (4 - abs(k)) for k in prefix)
    for entry in cores.values():
        uniform_core = Fraction(entry["count"], 9 ** half)
        product_core = Fraction(entry.pop("product_weight"), 46 ** half)
        entry["uniform_probability"] = as_json(uniform_core)
        entry["static_mixture_probability"] = as_json(uniform_core / 10 + 9 * product_core / 10)
    # p(k)=2^(4-|k|)/46, so the product probability is an exact rational.
    product_numerator = sum(prod(2 ** (4 - abs(k)) for k in a) for a in targets)
    uniform = Fraction(count, 9 ** half)
    product_mass = Fraction(product_numerator, 46 ** half)
    static_mass = uniform / 10 + 9 * product_mass / 10
    return {
        "degree": degree, "height": 4,
        "newton_survivors_all_heights": len(result["survivors"]),
        "newton_survivors_in_box": len(prefixes),
        "box_survivor_classification": dict(counts),
        "strict_target_count": count,
        "uniform_target_probability": as_json(uniform),
        "product_target_probability": as_json(product_mass),
        "static_mixture_target_probability": as_json(static_mass),
        "static_to_uniform_ratio": as_json(static_mass / uniform) if uniform else None,
        "certified_core_groups": list(cores.values()),
        "target_prefixes": targets,
        "elapsed_seconds": perf_counter() - start,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("degrees", nargs="*", type=int, choices=(14, 18, 20),
                        default=[14, 18, 20])
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    rows = []
    for degree in args.degrees:
        row = census(degree)
        rows.append(row)
        print(json.dumps({k: v for k, v in row.items() if k != "target_prefixes"}), flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({
        "purpose": "offline verification only; not proposal generation or adaptation",
        "target": "1 < whole polynomial Mahler measure < 6/5",
        "results": rows,
    }, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
