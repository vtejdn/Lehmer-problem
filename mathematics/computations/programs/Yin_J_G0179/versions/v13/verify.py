"""Check pair counts, last divisors, exact Newton subtrees and finite prime budgets."""

import argparse
from collections import Counter
from fractions import Fraction
import json
from math import isqrt, prod
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
from types import SimpleNamespace

import sieve


def prime_triples(p, b):
    if not (b-1)**8 < p**7 < b**8:
        raise ArithmeticError("Incorrect width.")
    older = {56: Fraction(1101, 1000), 58: Fraction(2193, 2000),
             68: Fraction(541, 500), 70: Fraction(431, 400)}

    def lower(d):
        if d < 86:
            return older.get(d, Fraction(1091, 1000) if d < 68 else Fraction(53, 50))
        if d not in sieve.DEGREES:
            raise ArithmeticError("Triple exceeds the census degrees.")
        return sieve.cutoff_for(d)

    result = []
    for i in range(86, b-123, 2):
        for j in range(68, b-i-55, 2):
            for k in range(56, b-i-j+1, 2):
                a, c, e = lower(i), lower(j), lower(k)
                z = a * max(a, c) * max(a, c, e)
                if z**(4*p)*(2*p*b+1)**4 < 2**p*(p*b+1)**4:
                    result.append((i, j, k))
    return result


def verify(degree, command):
    path = sieve.OUTPUT / "v13" / f"d{degree}"
    data = json.loads((path / "census.json").read_text())
    cutoff = sieve.cutoff_for(degree)
    limits, choices = sieve.trace_bounds(degree, cutoff)
    assert data["degree"] == degree and Fraction(*data["cutoff"]) == cutoff
    assert limits == data["bounds"] and [list(r) for r in choices] == data["source_rows"]
    bounds = limits[:degree//2]
    assert prod((2*b+k)//k for k,b in enumerate(bounds,1)) < 2**64
    base = runpy.run_path(str(sieve.GROUP / "count_prefixes.py"))
    divisors = tuple(p for p, _ in base["prime_powers"](degree))
    prefix = sieve.module_at("pair_census", sieve.HERE.parent / "v10" / "verify.py")
    original_fields = sieve.previous.load_driver("v10").FIELDS
    prefix.sieve = SimpleNamespace(HERE=sieve.HERE, T=cutoff, FIELDS=original_fields)
    sums_by_pair = prefix.tensor_totals(bounds, divisors)
    independent = sieve.module_at("ramanujan", sieve.HERE.parent / "v12" / "verify.py")
    # The v12 row verifier also checks sign orientation, substitutions and
    # integer Newton membership before its independent Ramanujan calculation.
    independent.CUTOFFS[degree] = cutoff
    independent.PRIME_DIVISORS[degree] = divisors
    totals, labels = Counter(), Counter()
    sample = None
    for (x, y), expected in sums_by_pair.items():
        report = json.loads((path / f"slice_{x}_{y}.json").read_text())
        counts = report["counts"]
        assert report["prefix"] == [x,y] and set(counts) == set(sieve.FIELDS)
        assert all(type(v) is int and v >= 0 for v in counts.values())
        assert counts["representatives"] == expected >= counts["first_reflected"] >= counts["nine_reflected"]
        assert counts["nine_reflected"] == sum(counts[name] for name in sieve.FIELDS[3:])
        assert len(report["rows"]) == counts["exact_division"]
        classes = Counter(row["classification"] for row in report["rows"])
        assert not report["unresolved"] and all(key.startswith("phi_") for key in classes)
        independent.verify_rows({"prefix":[x,y], "fallback_rows":report["rows"],
            "fallback_classifications":classes, "counts":{"fallback":len(report["rows"])},
            "exact_witnesses":report["witnesses"], "unresolved":report["unresolved"]}, degree, bounds)
        totals.update(counts)
        labels.update(classes)
        if report["rows"] and sample is None:
            coeff = report["rows"][0]["half"]
            sample = []
            for k in range(1,9):
                sample.append(-k*coeff[k] - sum(coeff[i]*sample[k-i-1] for i in range(1,k)))
    assert dict(totals) == data["counts"] and dict(labels) == data["classifications"]
    if sample is None:
        sample = [1,-1,1,-1,1,-1,1,-1]
    direct = prefix.check_direct(degree, divisors, sample, [0,*limits], bounds)
    expected_counts = {k: direct[k] for k in original_fields[:6]}
    expected_counts["exact_division"] = direct["modular_graeffe"] + direct["fallback"]
    with TemporaryDirectory(dir=path) as folder:
        scratch = Path(folder)
        caps = scratch / "limits.txt"
        caps.write_text(sieve.configuration(degree, limits), encoding="ascii")
        actual, _ = sieve.native_subtree(degree, sample, command, caps, scratch / "sample.txt")
    assert expected_counts == actual and expected_counts["representatives"] > 0
    summary = {"degree": degree, "cutoff":data["cutoff"], "verified_pairs":len(sums_by_pair),
               "counts":dict(totals), "verified_divisors":dict(labels), "direct_prefix":sample,
               "direct_counts":expected_counts}
    sieve.write_json(path / "summary.json", summary)
    print(degree, len(sums_by_pair), dict(totals), flush=True)


def main():
    if not __debug__:
        raise RuntimeError("Verification requires assertions enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, nargs="+", choices=sieve.DEGREES, default=sieve.DEGREES)
    args = parser.parse_args()
    # The complete next prime interval, determined by trial division.
    primes = [n for n in range(458,500) if all(n%k for k in range(2, isqrt(n)+1))]
    widths = [215,215,217,222,225,227,230]
    assert primes == [461,463,467,479,487,491,499]
    assert [prime_triples(p,b) for p,b in zip(primes,widths)] == [[]]*6 + [[(86,72,72)]]
    p, b = 499, 230
    z = Fraction(1057,1000)*Fraction(53,50)**2
    assert z**(4*p)*(2*p*b+1)**4 > 2**p*(p*b+1)**4
    with TemporaryDirectory(dir=sieve.OUTPUT / "v13") as folder:
        compiler = sieve.previous.load_driver("v10")
        compiler.HERE = sieve.HERE
        command = compiler.compile_worker(Path(folder))
        for degree in args.degree:
            verify(degree, command)


if __name__ == "__main__":
    main()
