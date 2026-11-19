"""Verify the three degree censuses, deficit maxima and ordered prime triples."""

from collections import Counter
from fractions import Fraction
from functools import cache
import json
from math import isqrt, prod
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from run import CUTOFFS, OUTPUT, VERSIONS, compile_worker, sieve
from check import lower as previous_lower


def verify(degree, command, scratch):
    cutoff = CUTOFFS[degree]
    path = OUTPUT / f"d{degree}"
    data = json.loads((path / "census.json").read_text())
    assert data["degree"] == degree and Fraction(*data["cutoff"]) == cutoff
    limits = data["bounds"]
    assert len(limits) == len(data["source_rows"]) == 120
    boxes = json.loads((sieve.OUTPUT / "v7" / "boxes.json").read_text())
    radius = Fraction(1091, 1000)
    a = int(10000*sieve.log_ratio(cutoff))
    assert radius**(a-1) < cutoff**10000 <= radius**a
    for k, (cap, (source, j)) in enumerate(zip(limits, data["source_rows"]), 1):
        if source:
            assert 0 < j <= len(boxes[str(source)]["certificates"]) and cutoff**k <= radius**j
            row = boxes[str(source)]["certificates"][j-1]
            assert row["unit"]["k"] == 0 and row["outer"]["k"] == j
            u, v = row["unit"]["upper"], row["outer"]["upper"]
            position = min(1, Fraction(a*k, 10000*j))
            assert cap == (degree//2*u + position*max(0,v-u)) // 10**12
        else:
            assert j == 0 and cap == int(degree-2 + cutoff**k + cutoff**-k)
    bounds = limits[:degree//2]
    assert prod((2*b+k)//k for k,b in enumerate(bounds,1)) < 2**63
    factors = runpy.run_path(str(sieve.GROUP / "count_prefixes.py"))["prime_powers"]
    divisors = tuple(p for p, _ in factors(degree))
    tensor = sieve.module_at("pair_counts", VERSIONS / "v10" / "verify.py")
    tensor.sieve = SimpleNamespace(HERE=VERSIONS / "v10", T=cutoff, FIELDS=sieve.previous.load_driver("v10").FIELDS)
    pairs = tensor.tensor_totals(bounds, divisors)
    exact = sieve.module_at("integer_witnesses", VERSIONS / "v12" / "verify.py")
    exact.CUTOFFS[degree], exact.PRIME_DIVISORS[degree] = cutoff, divisors
    totals, classes = Counter(), Counter()
    sample = None
    for (x,y), size in pairs.items():
        report = json.loads((path / f"slice_{x}_{y}.json").read_text())
        counts, rows = report["counts"], report["rows"]
        assert report["prefix"] == [x,y] and set(counts) == set(sieve.FIELDS)
        assert all(type(n) is int and n >= 0 for n in counts.values())
        assert size == counts["representatives"] >= counts["first_reflected"] >= counts["nine_reflected"]
        assert counts["nine_reflected"] == sum(counts[k] for k in sieve.FIELDS[3:])
        labels = Counter(row["classification"] for row in rows)
        assert all(key.startswith("phi_") for key in labels) and not report["unresolved"] and not report["witnesses"]
        exact.verify_rows({"prefix":[x,y], "counts":{"fallback":counts["exact_division"]},
                           "fallback_rows":rows, "fallback_classifications":labels,
                           "exact_witnesses":[], "unresolved":[]}, degree, bounds)
        totals.update(counts)
        classes.update(labels)
        if rows and sample is None:
            half = rows[0]["half"]
            sample = []
            for k in range(1,9):
                sample.append(-k*half[k] - sum(half[i]*sample[k-i-1] for i in range(1,k)))
    assert dict(totals) == data["counts"] and dict(classes) == data["classifications"]
    if sample is None:
        sample = [1,-1,1,-1,1,-1,1,-1]
    direct = tensor.check_direct(degree, divisors, sample, [0,*limits], bounds)
    reference = {key: direct[key] for key in sieve.FIELDS[:6]}
    reference["exact_division"] = direct["modular_graeffe"] + direct["fallback"]
    caps = scratch / "limits.txt"
    caps.write_text(sieve.configuration(degree, limits), encoding="ascii")
    actual, _ = sieve.native_subtree(degree, sample, command, caps, scratch / "sample.txt")
    assert reference == actual and actual["representatives"] > 0
    sieve.write_json(path / "summary.json", {"degree":degree, "cutoff":data["cutoff"],
        "verified_pairs":len(pairs), "counts":dict(totals), "classes":dict(classes),
        "direct_prefix":sample, "direct_counts":actual})
    print(degree, len(pairs), dict(totals), "checked subtree", actual, flush=True)


@cache
def lower(d):
    return CUTOFFS[d] if d in CUTOFFS else previous_lower(d)


def budgets():
    assert [p for p in range(500,510) if all(p % k for k in range(2,isqrt(p)+1))] == [503,509]
    for p,b in ((503,232),(509,234)):
        assert (b-1)**8 < p**7 < b**8 and 2*b <= p+1 and 2**8 <= p < 3**8

        @cache
        def allowed(z):
            return z.numerator**(4*p)*(2*p*b+1)**4 < z.denominator**(4*p)*2**p*(p*b+1)**4

        rows = []
        for i in range(86,b-123,2):
            for j in range(68,b-i-55,2):
                for k in range(56,b-i-j+1,2):
                    u, v, w = lower(i), lower(j), lower(k)
                    if allowed(u*max(u,v)*max(u,v,w)):
                        rows.append([i,j,k])
        print(p, b, rows)
        assert len(rows) == (0 if p==503 else 16)
        sieve.write_json(OUTPUT / f"prime{p}.json", {"prime":p, "width":b, "triples":rows})

    best = [0]*9

    def visit(count, start, cost, deficit):
        best[count] = max(best[count], deficit)
        for d in range(start,111,2):
            new = cost*lower(d)
            if new.numerator**4 < 2*new.denominator**4:
                visit(count+1, d, new, deficit+112-d)

    assert lower(110)**36 > 2
    visit(0, 56, Fraction(1), 0)
    assert best == [0,56,98,110,116,118,122,114,98]
    print("Largest deficits:", best)


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Verification requires assertions enabled.")
    with TemporaryDirectory(dir=OUTPUT) as folder:
        scratch = Path(folder)
        command = compile_worker(scratch)
        for d in CUTOFFS:
            verify(d, command, scratch)
    budgets()
