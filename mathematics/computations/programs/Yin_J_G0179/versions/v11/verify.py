"""Verify thin Mahler-measure boxes by congruence counts and direct Newton sums."""

import argparse
from collections import Counter
from fractions import Fraction
import json
from math import comb, prod
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory

import sieve


CUTOFF = Fraction(53, 50)
DIVISORS = {68: (2, 17), 70: (2, 5, 7), 72: (2, 3), 74: (2, 37),
            76: (2, 19), 78: (2, 3, 13), 80: (2, 5), 82: (2, 41), 84: (2, 3, 7)}
# Away from degree 68 the witness is the product of the Phi_(2p)
# for the indicated primes, allowing a repeated factor.
PRIMES = {70: (71,), 72: (73,), 74: (5, 71), 76: (5, 73),
          78: (79,), 80: (41, 41), 82: (83,), 84: (43, 43)}


def read_slices(degree, destination, pairs):
    graeffe = runpy.run_path(str(sieve.HERE.parent / "v3" / "finish.py"))["graeffe"]
    totals, labels = Counter(), Counter()
    witnesses, unresolved = [], []
    for (first, second), expected in pairs.items():
        report = json.loads((destination / f"slice_{first}_{second}.json").read_text())
        assert report["degree"] == degree and report["cutoff"] == [53, 50]
        assert report["prefix"] == [first, second]
        counts = report["counts"]
        assert set(counts) == set(sieve.FIELDS)
        assert all(type(n) is int and n >= 0 for n in counts.values())
        assert counts["representatives"] == expected
        assert expected >= counts["first_reflected"] >= counts["nine_reflected"]
        assert counts["nine_reflected"] == sum(counts[k] for k in sieve.FIELDS[3:])
        categories = report["fallback_classifications"]
        assert counts["fallback"] == sum(categories.values())
        assert len(report["unresolved"]) == categories.get("unresolved", 0)
        exact = report["exact_witnesses"]
        assert Counter(f"exact_graeffe_{w['round']}" for w in exact) == {
            key: n for key, n in categories.items() if key.startswith("exact_graeffe_")
        }
        for witness in exact:
            half = witness["half"]
            assert len(half) == degree // 2 + 1 and half[0] == 1
            assert first == -half[1] and second == first**2 - 2 * half[2]
            full = half + half[-2::-1]
            for _ in range(witness["round"]):
                full = graeffe(full)
            i = witness["index"]
            bound = int(comb(degree, i) * CUTOFF**(2**witness["round"]))
            assert full[i] == witness["coefficient"] and witness["upper"] == bound
            assert abs(full[i]) > bound
        witnesses.extend(exact)
        unresolved.extend(report["unresolved"])
        totals.update(counts)
        labels.update(categories)
    return totals, labels, witnesses, unresolved


def direct_prefixes(degree, bounds):
    length = degree // 4
    indices = range(1, length + 1)
    if degree == 68:
        # (X^70 + X^35 + 1)/Phi_3 = Phi_15 Phi_21 Phi_105.
        # Its first 34 sums equal the negatives of the Newton sums of Phi_3.
        cyclotomic = tuple(-2 if j % 3 == 0 else 1 for j in indices)
    else:
        primes = PRIMES[degree]
        assert sum(p - 1 for p in primes) == degree
        cyclotomic = tuple((-1)**j * sum((p - 1) if j % p == 0 else -1 for p in primes)
                           for j in indices)
    short = 4 if degree <= 72 else 6
    samples = [
        ("cyclotomic", cyclotomic),
        (f"first_{short}_sums", cyclotomic[:short]),
        ("delayed_odd_sum", tuple(3 * (j % 3 == 0) + 5 * (j % 5 == 0) for j in indices)),
        ("constant_sums", (min(5, min(bounds[:length])),) * length),
    ]
    assert all(b < j for j, b in enumerate(bounds, 1) if j > length)
    for q in DIVISORS[degree]:
        multiples = [bounds[j-1] for j in indices if j % q == 0]
        first_nonzero = q if multiples and q <= min(multiples) else 0
        prefix = tuple(first_nonzero if j % q == 0 else 0 for j in indices)
        samples.append((f"substitution_{q}", prefix))
    return samples


def check_samples(degree, destination, bounds, direct):
    config = sieve.configuration(degree, bounds)
    limits = list(map(int, config.splitlines()[0].split()))
    records = []
    with TemporaryDirectory(dir=destination) as folder:
        scratch = Path(folder)
        command = sieve.compile_worker(scratch)
        caps = scratch / "caps.txt"
        caps.write_text(config, encoding="ascii")
        for label, prefix in direct_prefixes(degree, bounds):
            assert all(abs(s) <= limit for s, limit in zip(prefix, bounds))
            expected = direct(degree, DIVISORS[degree], prefix, limits, bounds)
            native = sieve.run_slice(degree, prefix, command, caps, True, scratch)
            assert expected == native["counts"]
            if label == "cyclotomic":
                order = 15 if degree == 68 else 2 * min(PRIMES[degree])
                assert native["fallback_classifications"].get(f"phi_{order}", 0) > 0
            elif label == "first_4_sums":
                assert all(expected[k] > 0 for k in sieve.FIELDS)
            elif label == "first_6_sums":
                assert expected["representatives"] > 1 and expected["fallback"] > 0
            elif label.startswith("substitution_"):
                assert expected["representatives"] == 0
            records.append({"case": label, "prefix": prefix, "counts": expected})
    return records


def verify(degree):
    if not __debug__:
        raise RuntimeError("Verification requires assertions to be enabled.")
    assert sieve.T == CUTOFF
    destination = sieve.OUTPUT / "v11" / f"d{degree}"
    source = json.loads((destination / "boxes.json").read_text())
    bounds = source["bounds"]
    assert len(bounds) == degree // 2
    # Each admissible prefix prescribes one residue class for the next sum.
    # All final counts for a slice or a restricted box fit in a uint64.
    branch_bound = prod((2 * b + k) // k for k, b in enumerate(bounds, 1))
    assert branch_bound < 2**64
    procedures = runpy.run_path(str(sieve.HERE.parent / "v10" / "verify.py"))
    pairs = procedures["tensor_totals"](bounds, DIVISORS[degree])
    totals, labels, witnesses, unresolved = read_slices(degree, destination, pairs)
    assert totals["representatives"] == source["no_power_substitution_up_to_sign"]
    checks = check_samples(degree, destination, bounds, procedures["check_direct"])
    summary = {"degree": degree, "cutoff": [53, 50], "tensor_verified_pairs": len(pairs),
               "counts": dict(totals), "fallback_classifications": dict(labels),
               "direct_prefix_checks": checks, "exact_graeffe_witnesses": witnesses,
               "unresolved": unresolved}
    with TemporaryDirectory(dir=destination) as folder:
        pending = Path(folder) / "summary.json"
        pending.write_text(json.dumps(summary, indent=2) + "\n", encoding="ascii")
        pending.replace(destination / "summary.json")
    print(degree, dict(totals), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--degree", type=int, choices=tuple(DIVISORS), required=True)
    verify(parser.parse_args().degree)
