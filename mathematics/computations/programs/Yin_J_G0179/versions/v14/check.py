"""Check the degree-72 census, degree deficits and the first remaining prime."""

from collections import Counter
from fractions import Fraction
from functools import cache
import json
from math import isqrt, prod
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from census import CUTOFF, DEGREE, DEST, VERSIONS, compile_worker, sieve


def check_bounds(data):
    assert (data["degree"], Fraction(*data["cutoff"])) == (DEGREE, CUTOFF)
    limits, rows = data["bounds"], data["source_rows"]
    assert len(limits) == len(rows) == 120
    radius = Fraction(1091, 1000)
    boxes = json.loads((sieve.OUTPUT / "v7" / "boxes.json").read_text())
    assert radius**7553 < CUTOFF**10000 <= radius**7554
    for k, (cap, (source, layer)) in enumerate(zip(limits, rows), 1):
        if source == 0:
            assert layer == 0 and cap == int(70 + CUTOFF**k + CUTOFF**-k)
        else:
            assert 0 < layer and radius**layer >= CUTOFF**k
            row = boxes[str(source)]["certificates"][layer-1]
            assert row["unit"]["k"] == 0 and row["outer"]["k"] == layer
            u, v = row["unit"]["upper"], row["outer"]["upper"]
            fraction = min(1, Fraction(7554*k, 10000*layer))
            assert cap == (36*u + fraction*max(0, v-u)) // 10**12
    assert prod((2*b+k)//k for k, b in enumerate(limits[:36], 1)) < 2**63
    return limits


def check_census():
    data = json.loads((DEST / "census.json").read_text())
    limits = check_bounds(data)
    bounds = limits[:36]
    tensor = sieve.module_at("tensor", VERSIONS / "v10" / "verify.py")
    old_fields = sieve.previous.load_driver("v10").FIELDS
    tensor.sieve = SimpleNamespace(HERE=VERSIONS / "v10", FIELDS=old_fields, T=CUTOFF)
    exact = sieve.module_at("exact", VERSIONS / "v12" / "verify.py")
    exact.CUTOFFS[DEGREE], exact.PRIME_DIVISORS[DEGREE] = CUTOFF, (2, 3)
    pairs = tensor.tensor_totals(bounds, (2, 3))
    totals, classes = Counter(), Counter()
    for pair, size in pairs.items():
        report = json.loads((DEST / f"slice_{pair[0]}_{pair[1]}.json").read_text())
        counts = report["counts"]
        assert report["prefix"] == list(pair) and set(counts) == set(sieve.FIELDS)
        assert all(type(n) is int and n >= 0 for n in counts.values())
        assert size == counts["representatives"] >= counts["first_reflected"] >= counts["nine_reflected"]
        assert counts["nine_reflected"] == sum(counts[key] for key in sieve.FIELDS[3:])
        labels = Counter(row["classification"] for row in report["rows"])
        assert not report["unresolved"]
        exact.verify_rows({"prefix": pair, "counts": {"fallback": counts["exact_division"]},
                           "fallback_rows": report["rows"], "fallback_classifications": labels,
                           "exact_witnesses": report["witnesses"], "unresolved": []}, DEGREE, bounds)
        totals.update(counts)
        classes.update(labels)
    assert dict(totals) == data["counts"] and dict(classes) == data["classifications"]
    # This subtree contains a polynomial surviving all cyclotomic divisions.
    prefix = [0,-2,0,2,0,4,7,-6,0,8,0,-4]
    direct = tensor.check_direct(DEGREE, (2,3), prefix, [0, *limits], bounds)
    reference = {key: direct[key] for key in sieve.FIELDS[:6]}
    reference["exact_division"] = direct["modular_graeffe"] + direct["fallback"]
    with TemporaryDirectory(dir=DEST) as folder:
        scratch = Path(folder)
        caps = scratch / "limits.txt"
        caps.write_text(sieve.configuration(DEGREE, limits), encoding="ascii")
        actual, _ = sieve.native_subtree(DEGREE, prefix, compile_worker(scratch), caps, scratch / "sample.txt")
    assert actual == reference and actual["exact_division"] > 0
    sieve.write_json(DEST / "summary.json", {"degree": DEGREE, "cutoff": data["cutoff"],
        "verified_pairs": len(pairs), "counts": dict(totals), "classes": dict(classes),
        "direct_prefix": prefix, "direct_counts": actual})
    print("Census:", len(pairs), dict(totals), "subtree:", actual, flush=True)


@cache
def lower(d):
    if d < 56 or d > 110 or d % 2:
        raise ValueError("Degree outside the finite cutoff table.")
    if d >= 86:
        return sieve.cutoff_for(d)
    smaller = {56: Fraction(1101,1000), 58: Fraction(2193,2000),
               68: Fraction(541,500), 70: Fraction(431,400), 72: CUTOFF}
    return smaller.get(d, Fraction(1091,1000) if d < 68 else Fraction(53,50))


def degree_deficits():
    costs = {0: Fraction(1)}
    maxima = [0]
    assert lower(110)**36 > 2
    for _ in range(8):
        updated = {}
        for deficit, cost in costs.items():
            for d in range(56, 111, 2):
                product = cost * lower(d)
                total = deficit + 112-d
                if product**4 < 2 and (total not in updated or product < updated[total]):
                    updated[total] = product
        costs = updated
        maxima.append(max(costs))
    assert maxima == [0,56,98,110,116,120,124,120,100]
    print("Maximal deficits:", maxima)


def triples(width, passes):
    accepted = []
    for i in range(86, width-123, 2):
        for j in range(68, width-i-55, 2):
            for k in range(56, width-i-j+1, 2):
                a, b, c = lower(i), lower(j), lower(k)
                if passes(a*max(a,b)*max(a,b,c)):
                    accepted.append((i,j,k))
    return accepted


def budgets():
    assert triples(226, lambda z: z**4 < 2) == [(92,74,60)]
    assert [p for p in range(492,504) if all(p % q for q in range(2,isqrt(p)+1))] == [499,503]
    remaining = [(86,74,72),(86,86,60),(88,72,72),(92,72,68)]
    for p, width, expected in ((499,230,[]), (503,232,remaining)):
        assert (width-1)**8 < p**7 < width**8 and 2*width <= p+1 and 2**8 <= p < 3**8

        @cache
        def passes(z):
            return z.numerator**(4*p)*(2*p*width+1)**4 < z.denominator**(4*p)*2**p*(p*width+1)**4

        assert triples(width, passes) == expected
        print("Prime:", p, width, expected)


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Verification requires assertions enabled.")
    check_census()
    degree_deficits()
    budgets()
