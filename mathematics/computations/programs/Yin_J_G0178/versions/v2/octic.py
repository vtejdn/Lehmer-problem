"""Exact width-eight fixed-seed census for reciprocal octics."""

import json
import runpy
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path


GROUP = Path(__file__).resolve().parents[2]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v2" / "results.json"
BASE = runpy.run_path(str(GROUP / "census.py"))
divide, powers = BASE["divide"], BASE["powers"]


def graeffe(poly):
    """Return the monic polynomial whose indexed roots are the original roots squared."""
    degree = len(poly) - 1
    return [sum((-1)**i * poly[i] * poly[2*j-i]
                for i in range(max(0, 2*j-degree), min(degree, 2*j)+1))
            for j in range(degree+1)]


def measure_test(poly, power, cap):
    """Compare M(poly)**power with cap, certified by integer Graeffe bounds."""
    degree = len(poly) - 1
    binomials = [comb(degree, i)**power for i in range(degree+1)]
    while True:
        if any(abs(c)**power > cap*b for c, b in zip(poly, binomials)):
            return False
        if sum(c*c for c in poly)**power <= cap*cap:
            return True
        poly = graeffe(poly)
        cap *= cap


def octics():
    """Generate the four leading octic coefficients using power-sum bounds."""
    partials = [([1], [8])]
    for k in range(1, 5):
        next_partials = []
        bound = 6 + 2**k
        for coeffs, sums in partials:
            prior = sum(coeffs[j]*sums[k-j] for j in range(1, k))
            for value in range((-bound-prior+k-1)//k, (bound-prior)//k+1):
                extended = coeffs + [value]
                if (k == 1 and value < 0) or (k == 3 and coeffs[1] == 0 and value < 0):
                    continue
                next_partials.append((extended, sums + [-prior-k*value]))
        partials = next_partials
    for coeffs, _ in partials:
        yield coeffs + coeffs[-2::-1]


def small_factors():
    for degree in range(1, 5):
        bounds = [2*comb(degree, j) for j in range(1, degree)]
        for inner in product(*(range(-b, b+1) for b in bounds)):
            for unit in (-1, 1):
                poly = [1, *inner, unit]
                if measure_test(poly, 1, 2):
                    yield poly


def trace_inside(octic):
    _, a, b, c, d, *_ = octic
    trace = [1, a, b-4, c-3*a, d-2*b+2]
    chain = [trace, [4, 3*a, 2*(b-4), c-3*a]]
    while len(chain[-1]) > 1:
        _, remainder = divide(chain[-2], chain[-1])
        assert remainder
        chain.append([-v for v in remainder])

    def signs(point):
        sequence = []
        for row in chain:
            value = 0
            for coefficient in row:
                value = point*value + coefficient
            if value:
                sequence.append(value > 0)
        return sum(a != b for a, b in zip(sequence, sequence[1:]))

    return signs(-2) - signs(2)


def census():
    factors = list(small_factors())
    counts = Counter()
    records = []
    for poly in octics():
        counts["first_four_power_sums"] += 1
        if any(abs(v) > 6+2**j for j, v in enumerate(powers(poly, 16)) if j >= 5):
            continue
        counts["first_sixteen_power_sums"] += 1
        if not measure_test(poly, 1, 2):
            continue
        counts["under_measure_cap"] += 1
        if any(not divide(poly, f)[1] for f in factors):
            continue
        counts["irreducible"] += 1
        outside = 4 - trace_inside(poly)
        if outside == 0:
            continue
        counts["nontorsion"] += 1
        exponent = 4*(8-outside)-6
        survives = measure_test(poly, exponent, 256)
        record = {"coefficients": poly[1:5], "outside": outside,
                  "measure_exponent": exponent, "passes_count_bound": survives}
        if survives:
            record["measure_to_45_above_65536"] = not measure_test(poly, 45, 65536)
        records.append(record)
    return {"counts": dict(counts), "seeds": records}


if __name__ == "__main__":
    data = census()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT)
    print(data["counts"])
    print([r for r in data["seeds"] if r["passes_count_bound"]])
