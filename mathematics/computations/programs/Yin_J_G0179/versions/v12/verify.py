"""Verify the four asymmetric censuses and every recorded final exclusion."""

import argparse
from collections import Counter
from fractions import Fraction
from functools import cache
import importlib.util
import json
from math import comb, prod
from pathlib import Path
from tempfile import TemporaryDirectory

import sieve


CUTOFFS = {56: Fraction(2202, 2000), 58: Fraction(2193, 2000),
           68: Fraction(2164, 2000), 70: Fraction(2155, 2000)}
PRIME_DIVISORS = {56: (2, 7), 58: (2, 29), 68: (2, 17), 70: (2, 5, 7)}


@cache
def mobius(n):
    if n == 1:
        return 1
    return -sum(mobius(d) for d in range(1, n) if n % d == 0)


@cache
def ramanujan_weights(n):
    if n < 1:
        raise ValueError("A cyclotomic order must be positive.")
    return [(d, d * mobius(n // d)) for d in range(1, n+1)
            if n % d == 0 and mobius(n // d)]


def primitive_root_energy(coeff, n):
    """Sum |P(z)|² over primitive n-th roots, by the Ramanujan sum formula.

    In the expansion in coefficient pairs (i,j), a divisor d of n
    contributes d*mu(n/d) exactly when i and j agree modulo d.
    """
    energy = 0
    for d, weight in ramanujan_weights(n):
        folded = [0] * min(d, len(coeff))
        for i, a in enumerate(coeff):
            folded[i % d] += a
        energy += weight * sum(x*x for x in folded)
    return energy


def graeffe_by_convolution(coeff):
    """Keep the even coefficients of P(X)P(-X) in ascending order."""
    return [sum((-1 if j % 2 else 1) * coeff[j] * coeff[2*k-j]
                for j in range(max(0, 2*k-len(coeff)+1), min(len(coeff), 2*k+1)))
            for k in range(len(coeff))]


def verify_witness(full, degree, cutoff, witness, label):
    rounds = witness["round"]
    assert 0 <= rounds <= 12 and label == f"exact_graeffe_{rounds}"
    for _ in range(rounds):
        full = graeffe_by_convolution(full)
    i = witness["index"]
    assert 0 <= i <= degree
    upper = int(comb(degree, i) * cutoff**(2**rounds))
    assert full[i] == witness["coefficient"] and witness["upper"] == upper
    assert abs(full[i]) > upper


def verify_rows(report, degree, bounds):
    cutoff = CUTOFFS[degree]
    first, second = report["prefix"]
    rows = report["fallback_rows"]
    assert len(rows) == report["counts"]["fallback"]
    assert Counter(r["classification"] for r in rows) == report["fallback_classifications"]
    witnesses = {tuple(w["half"]): w for w in report["exact_witnesses"]}
    assert len(witnesses) == len(report["exact_witnesses"])
    unresolved = set(map(tuple, report["unresolved"]))
    assert len(unresolved) == len(report["unresolved"])
    seen = set()
    for row in rows:
        half = tuple(row["half"])
        assert len(half) == degree//2+1 and half[0] == 1
        assert all(type(a) is int for a in half) and half not in seen
        seen.add(half)
        sums = [0]
        for k in range(1, len(half)):
            value = -k*half[k] - sum(half[i]*sums[k-i] for i in range(1, k))
            assert abs(value) <= bounds[k-1]
            sums.append(value)
        assert sums[1:3] == [first, second]
        assert next(s for s in sums[1::2] if s) > 0
        for prime in PRIME_DIVISORS[degree]:
            assert any(half[j] for j in range(1, len(half)) if j % prime)
        full = half + half[-2::-1]
        label = row["classification"]
        if label.startswith("phi_"):
            order = int(label.removeprefix("phi_"))
            assert primitive_root_energy(full, order) == 0
        elif label.startswith("exact_graeffe_"):
            verify_witness(full, degree, cutoff, witnesses.pop(half), label)
        else:
            assert label == "unresolved"
            unresolved.remove(half)
    assert not witnesses and not unresolved


def direct_samples(degree, bounds):
    length = 16 if degree <= 58 else 17
    if degree == 68:
        # (X^70+X^35+1)/Phi_3 = Phi_15 Phi_21 Phi_105.
        known_order = 15
        reference = tuple(-2 if j % 3 == 0 else 1 for j in range(1, length+1))
    else:
        # The other reference polynomials are Phi_58^2, Phi_118 and Phi_142.
        known_order = {56: 58, 58: 118, 70: 142}[degree]
        copies = 2 if degree == 56 else 1
        reference = tuple(copies * (-1)**(j+1) for j in range(1, length+1))
    short_length = 10 if degree == 56 else 6
    samples = [("cyclotomic", reference), ("branching", reference[:short_length])]
    assert all(b < j for j, b in enumerate(bounds, 1) if j > length)
    for p in PRIME_DIVISORS[degree]:
        multiples = [bounds[j-1] for j in range(p, length+1, p)]
        value = p if multiples and p <= min(multiples) else 0
        samples.append((f"substitution_{p}", tuple(value if j % p == 0 else 0
                                                  for j in range(1, length+1))))
    return known_order, samples


def check_direct(degree, bounds, destination, context, procedures):
    text = context.configuration(degree, bounds)
    limits = list(map(int, text.splitlines()[0].split()))
    order, samples = direct_samples(degree, bounds)
    checks = []
    with TemporaryDirectory(dir=destination) as folder:
        scratch = Path(folder)
        cmd = context.compile_worker(scratch)
        config = scratch / "caps.txt"
        config.write_text(text, encoding="ascii")
        for label, prefix in samples:
            assert all(abs(s) <= b for s, b in zip(prefix, bounds))
            direct = procedures.check_direct(degree, PRIME_DIVISORS[degree], prefix, limits, bounds)
            native = context.run_slice(degree, prefix, cmd, config, True, scratch)
            assert direct == native["counts"]
            if label == "cyclotomic":
                assert native["fallback_classifications"].get(f"phi_{order}", 0) > 0
            elif label == "branching":
                assert all(direct[k] > 0 for k in context.FIELDS)
            else:
                assert direct["representatives"] == 0
            checks.append({"case": label, "prefix": prefix, "counts": direct})
    return checks


def verify(degree):
    if not __debug__:
        raise RuntimeError("Verification requires assertions to be enabled.")
    context = sieve.configure(degree)
    cutoff = CUTOFFS[degree]
    assert context.T == cutoff
    destination = context.OUTPUT / "v12" / f"d{degree}"
    source = json.loads((destination / "boxes.json").read_text())
    bounds = source["bounds"]
    assert len(bounds) == degree//2
    assert prod((2*b+k)//k for k, b in enumerate(bounds, 1)) < 2**64
    path = context.HERE.parent / "v10" / "verify.py"
    spec = importlib.util.spec_from_file_location("pair_and_newton_checks", path)
    procedures = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(procedures)
    procedures.sieve = context
    pairs = procedures.tensor_totals(bounds, PRIME_DIVISORS[degree])
    totals, labels = Counter(), Counter()
    witnesses, unresolved = [], []
    for (x, y), expected in pairs.items():
        report = json.loads((destination / f"slice_{x}_{y}.json").read_text())
        assert report["degree"] == degree and Fraction(*report["cutoff"]) == cutoff
        assert report["prefix"] == [x, y]
        counts = report["counts"]
        assert set(counts) == set(context.FIELDS)
        assert all(type(n) is int and n >= 0 for n in counts.values())
        assert counts["representatives"] == expected
        assert expected >= counts["first_reflected"] >= counts["nine_reflected"]
        assert counts["nine_reflected"] == sum(counts[k] for k in context.FIELDS[3:])
        verify_rows(report, degree, bounds)
        totals.update(counts)
        labels.update(report["fallback_classifications"])
        witnesses.extend(report["exact_witnesses"])
        unresolved.extend(report["unresolved"])
    assert totals["representatives"] == source["no_power_substitution_up_to_sign"]
    checks = check_direct(degree, bounds, destination, context, procedures)
    summary = {"degree": degree, "cutoff": [cutoff.numerator, cutoff.denominator],
               "tensor_verified_pairs": len(pairs), "counts": dict(totals),
               "fallback_classifications": dict(labels), "direct_prefix_checks": checks,
               "exact_graeffe_witnesses": witnesses, "unresolved": unresolved,
               "verified_cyclotomic_rows": sum(n for k, n in labels.items() if k.startswith("phi_"))}
    with TemporaryDirectory(dir=destination) as folder:
        pending = Path(folder) / "summary.json"
        pending.write_text(json.dumps(summary, indent=2) + "\n", encoding="ascii")
        pending.replace(destination / "summary.json")
    print(degree, dict(totals), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", choices=tuple(CUTOFFS), type=int, required=True)
    verify(parser.parse_args().degree)
