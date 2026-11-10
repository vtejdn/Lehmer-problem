"""Independent bounded review of the fixed cyclotomic parent sampler.

Exact arithmetic only: independent totients, prefix counting, recursive small
multisets, FLINT products, stopping controls, and replay of the already specified
seeded controls. No Mahler roots, mutation research, or new sampling experiment.
The two original author output files are explicit verification inputs.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import reduce
import json
from math import gcd
from pathlib import Path
import random
import sys
import time

from flint import fmpz_poly

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
sys.path.insert(0, str(HERE))
from cyclotomic_closure import LEHMER, generate
from cyclotomic_parent_sampling import ParentSampler
from cyclotomic_parent_sampling_checks import callback_isolation_control


def phi(n):
    value, left, prime = n, n, 2
    while prime * prime <= left:
        if left % prime == 0:
            value -= value // prime
            while left % prime == 0:
                left //= prime
        prime += 1
    if left > 1:
        value -= value // left
    return value


def factor_types(limit):
    if not limit:
        return []
    return [(1, 2), (2, 2)] + [(m, phi(m)) for m in range(3, 2 * limit**2 + 1)
                              if phi(m) <= limit]


def factor_poly(order):
    if order == 1:
        return fmpz_poly([-1, 1]) ** 2
    if order == 2:
        return fmpz_poly([1, 1]) ** 2
    return fmpz_poly.cyclotomic(order)


def prefix_counts(specs, limit):
    counts = [1] + [0] * limit
    for _, width in specs:
        for degree in range(width, limit + 1):
            counts[degree] += counts[degree - width]
    return counts


def independent_multisets(specs, degree):
    polynomials = [factor_poly(order) for order, _ in specs]
    powers = [0] * len(specs)

    def visit(remaining, first, polynomial):
        if remaining == 0:
            yield tuple(powers), polynomial
            return
        for j in range(first, len(specs)):
            width = specs[j][1]
            if width <= remaining:
                powers[j] += 1
                yield from visit(remaining - width, j, polynomial * polynomials[j])
                powers[j] -= 1

    yield from visit(degree, 0, fmpz_poly([1]))


def lifted_core(k, sign):
    result = [0] * (10 * k + 1)
    for i, coefficient in enumerate(LEHMER):
        result[k * i] = coefficient * sign**i
    return fmpz_poly(result)


def checked_sampler(degree, saved_build=None):
    sampler = ParentSampler(LEHMER, degree)
    specs = factor_types(degree - 10)
    assert specs == [(f.order, f.degree) for f in sampler.neutral.factors]
    counts = prefix_counts(specs, degree - 10)
    assert counts == [sampler.neutral.count(r) for r in range(degree - 9)]
    weights = [counts[degree - 10 * k] for k in range(1, degree // 10 + 1)]
    assert weights == list(sampler.weights)
    if saved_build is not None:
        for key, value in sampler.build.items():
            if key != "build_seconds":
                assert saved_build[key] == value, (degree, key)
    return sampler, specs


def small_complete_checks(saved):
    result, rejection, acceptance = [], None, None
    for row in saved["complete_small_comparisons"]:
        degree = row["degree"]
        sampler, specs = checked_sampler(degree, row["build"])
        raw, accepted, per_index = set(), set(), []
        for k, count in enumerate(sampler.weights, 1):
            remainder = degree - 10 * k
            ranks, neutrals, accepted_k = set(), set(), 0
            for powers, neutral in independent_multisets(specs, remainder):
                ticket = sampler.neutral.rank(remainder, powers)
                assert ticket not in ranks
                ranks.add(ticket)
                assert sampler.neutral.unrank(remainder, ticket) == powers
                neutral_coefficients = tuple(map(int, neutral))
                assert sampler.neutral.polynomial(powers) == neutral_coefficients
                assert neutral_coefficients not in neutrals
                neutrals.add(neutral_coefficients)
                for sign in (-1, 1):
                    expected = tuple(map(int, lifted_core(k, sign) * neutral))
                    candidate = sampler.construct(k, sign, ticket)
                    assert tuple(candidate["coefficients_ascending"]) == expected
                    assert candidate["observed_height"] == max(map(abs, expected))
                    assert candidate["accepted"] == (max(map(abs, expected)) <= 4)
                    assert expected not in raw
                    raw.add(expected)
                    if candidate["accepted"]:
                        accepted.add(expected)
                        accepted_k += 1
                        if degree == 18 and acceptance is None:
                            acceptance = candidate
                    elif degree == 18 and rejection is None:
                        rejection = candidate
            assert ranks == set(range(count)) and len(neutrals) == count
            per_index.append({"substitution_index": k, "neutral_product_count": count,
                              "constructed_count": 2 * count, "accepted_count": accepted_k})
        assert per_index == row["counts"]
        assert len(raw) == row["build"]["raw_parent_count"]
        assert len(accepted) == row["accepted_count"]
        legacy, _ = generate(LEHMER, degree)
        assert set(legacy) == {p[1:degree // 2 + 1] for p in accepted}
        interval_counts = Counter(sampler.select_k(t) for t in range(sampler.weight_sum))
        assert [interval_counts[k] for k in range(1, len(sampler.weights) + 1)] == list(sampler.weights)
        result.append({"degree": degree, "raw_parents": len(raw),
                       "accepted_parents": len(accepted), "counts": per_index,
                       "all_multisets_ranks_products_and_closure_sets_equal": True})
    assert rejection is not None and acceptance is not None
    return result, rejection, acceptance


class Tickets:
    def __init__(self, values):
        self.values = iter(values)
        self.bounds = []

    def randrange(self, bound):
        self.bounds.append(bound)
        assert type(bound) is int and bound > 0
        value = next(self.values)
        assert 0 <= value < bound
        return value


class Clock:
    def __init__(self, values):
        self.values = iter(values)

    def __call__(self):
        return next(self.values)


def stopping_checks(bad, good):
    sampler = ParentSampler(LEHMER, 18)
    bad_tickets = [0, int(bad["sign"] == 1), bad["neutral_ticket"]]
    good_tickets = [0, int(good["sign"] == 1), good["neutral_ticket"]]
    seen = []

    def mutating_observer(number, candidate, seconds):
        seen.append((number, candidate["accepted"], seconds))
        candidate["accepted"] = not candidate["accepted"]
        candidate["coefficients_ascending"][:] = [999]
        candidate["neutral_factor_powers"][0][:] = [999, 999]

    rng = Tickets(bad_tickets + good_tickets)
    outcome = sampler.sample_accepted(rng, max_attempts=2, deadline=13,
                                     clock=Clock([10, 10, 11, 12, 14, 18]),
                                     on_attempt=mutating_observer)
    assert outcome["parent"] == good and outcome["status"] == "accepted"
    assert outcome["attempts_started"] == 2 and outcome["height_rejections"] == 1
    assert outcome["construction_seconds"] == 3 and outcome["elapsed_seconds"] == 8
    assert outcome["last_attempt_seconds"] == outcome["max_attempt_seconds"] == 2
    assert outcome["soft_overrun_seconds"] == 5
    assert seen == [(1, False, 1), (2, True, 2)] and len(rng.bounds) == 6
    exhausted = sampler.sample_accepted(Tickets(bad_tickets), max_attempts=1,
                                        clock=Clock([0, 0, 1, 1]))
    assert exhausted["status"] == "attempt_limit" and exhausted["parent"] is None
    assert exhausted["height_rejections"] == exhausted["attempts_started"] == 1
    rng = Tickets([])
    stopped = sampler.sample_accepted(rng, max_attempts=1, deadline=2,
                                     clock=Clock([2, 2, 2]))
    assert stopped["status"] == "deadline" and stopped["attempts_started"] == 0 and not rng.bounds
    rng = Tickets(bad_tickets)
    stopped = sampler.sample_accepted(rng, max_attempts=2, deadline=2,
                                     clock=Clock([0, 0, 1, 2, 2]))
    assert stopped["status"] == "deadline" and stopped["height_rejections"] == 1
    assert len(rng.bounds) == 3

    def failure(*args):
        raise RuntimeError("reviewer callback failure")

    try:
        sampler.sample_accepted(Tickets(good_tickets), max_attempts=1,
                                clock=Clock([0, 0, 1]), on_attempt=failure)
    except RuntimeError as exc:
        assert str(exc) == "reviewer callback failure"
    else:
        raise AssertionError("callback failure was swallowed")
    small = ParentSampler(LEHMER, 10)
    for sign_bit in (0, 1):
        rng = Tickets([0, sign_bit, 0])
        candidate = small.draw_raw(rng)
        assert rng.bounds == [1, 2, 1] and candidate["sign"] == (-1, 1)[sign_bit]
    for kwargs in ({"max_attempts": 0}, {"max_attempts": True},
                   {"max_attempts": 1, "deadline": float("nan")}):
        try:
            small.sample_accepted(Tickets([]), **kwargs)
        except ValueError:
            pass
        else:
            raise AssertionError(("invalid limit accepted", kwargs))
    try:
        ParentSampler(LEHMER, 1000)
    except ValueError:
        pass
    else:
        raise AssertionError("order construction guard failed")
    assert callback_isolation_control()["callback_payload_isolation"] == "pass"
    return {"independent_callback_copy_and_soft_overrun": "pass",
            "rejection_caps_deadlines_integer_draws_and_failures": "pass",
            "author_two_attempt_callback_regression": "pass"}


def normalize_exact(coefficients):
    content, factors = fmpz_poly(coefficients).factor()
    assert content == 1
    reconstructed, remaining = fmpz_poly([1]), fmpz_poly([1])
    for factor, exponent in factors:
        reconstructed *= factor**exponent
        if not factor.is_cyclotomic():
            remaining *= factor**exponent
    assert tuple(map(int, reconstructed)) == tuple(coefficients)
    values = tuple(map(int, remaining))
    divisor = reduce(gcd, (i for i, value in enumerate(values) if i and value), 0)
    assert divisor > 0
    values = values[::divisor]
    opposite = tuple(value * (-1)**i for i, value in enumerate(values))
    return min(values[::-1], opposite[::-1])[::-1]


def high_degree_checks(controls, feasibility):
    rows = []
    for saved in controls["higher_degree_controls"]:
        degree = saved["degree"]
        sampler, _ = checked_sampler(degree, saved["build"])
        for k, count in enumerate(sampler.weights, 1):
            for ticket in {0, count // 2, count - 1}:
                assert sampler.neutral.rank(degree - 10 * k,
                    sampler.neutral.unrank(degree - 10 * k, ticket)) == ticket
        for witness in saved["explicit_height_one_witnesses"]:
            neutral = fmpz_poly([1])
            for order, exponent in witness["neutral_factor_powers"]:
                neutral *= factor_poly(order)**exponent
            assert tuple(map(int, neutral)) == (1,) + (0,) * (degree - 11) + (1,)
            expected = tuple(map(int, lifted_core(witness["substitution_index"], witness["sign"]) * neutral))
            assert expected == tuple(witness["coefficients_ascending"])
            assert max(map(abs, expected)) == 1 and witness["accepted"]
            assert sampler.construct(1, witness["sign"], witness["neutral_ticket"]) == witness
        rng = random.Random(saved["seed"])
        for record in saved["attempt_costs"]:
            candidate = sampler.draw_raw(rng)
            assert candidate["accepted"] == record["accepted"]
            assert candidate["observed_height"] == record["height"]
            assert candidate["substitution_index"] == record["substitution_index"]
        attempt_records = saved["attempt_costs"]
        summary = saved["mechanical_rejection_control"]
        assert summary["status"] == "attempt_limit" and summary["parent"] is None
        assert summary["attempts_started"] == len(attempt_records) == 32
        assert summary["height_rejections"] == sum(not r["accepted"] for r in attempt_records) == 32
        assert summary["construction_seconds"] == sum(r["seconds"] for r in attempt_records)
        assert summary["max_attempt_seconds"] == max(r["seconds"] for r in attempt_records)
        assert summary["last_attempt_seconds"] == attempt_records[-1]["seconds"]
        rows.append({"degree": degree, "raw_parent_count": sampler.build["raw_parent_count"],
                     "substitution_weights": list(sampler.weights),
                     "explicit_witnesses": 2, "original_short_draws_replayed": 32})

    replay = []
    for saved in feasibility["groups"]:
        assert saved["status"] == "raw_count_completed"
        assert saved["requested_raw_proposals"] == saved["completed_raw_proposals"] == 10000
        sampler, _ = checked_sampler(saved["degree"], saved["build"])
        started = time.perf_counter()
        rng, accepted, coefficients = random.Random(saved["seed"]), 0, set()
        for _ in range(saved["completed_raw_proposals"]):
            candidate = sampler.draw_raw(rng)
            if candidate["accepted"]:
                accepted += 1
                coefficients.add(tuple(candidate["coefficients_ascending"]))
        assert accepted == saved["height_accepted"]
        assert 10000 - accepted == saved["height_rejected"]
        assert len(coefficients) == saved["distinct_accepted_parents"]
        assert sorted(coefficients) == list(map(tuple, saved["accepted_coefficients_ascending"]))
        for polynomial in coefficients:
            assert len(polynomial) == saved["degree"] + 1 and polynomial == polynomial[::-1]
            assert polynomial[0] == polynomial[-1] == 1 and max(map(abs, polynomial)) <= 4
            assert normalize_exact(list(polynomial)) == LEHMER
        replay.append({"degree": saved["degree"], "seed": saved["seed"], "raw_count": 10000,
                       "accepted": accepted, "rejected": 10000 - accepted,
                       "distinct_witnesses_exactly_normalized": len(coefficients),
                       "replay_and_witness_check_seconds": time.perf_counter() - started})
    return {"high_degree_counts_and_short_controls": rows, "fixed_seed_feasibility_replay": replay}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT / "independent_parent_sampling_review.json")
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    controls = json.loads((OUTPUT / "cyclotomic_parent_sampling_controls.json").read_text(encoding="utf-8"))
    feasibility = json.loads((OUTPUT / "cyclotomic_parent_sampling_feasibility.json").read_text(encoding="utf-8"))
    assert [r["degree"] for r in controls["complete_small_comparisons"]] == [18, 20, 24, 30]
    assert [(r["degree"], r["seed"]) for r in controls["higher_degree_controls"]] == [(56, 5601), (80, 8001)]
    assert [(r["degree"], r["seed"]) for r in feasibility["groups"]] == [(56, 56002), (80, 80002)]
    small, bad, good = small_complete_checks(controls)
    result = {"scope": "Independent bounded parent-sampler review; no Mahler roots or new sampling research.",
              "small_complete_checks": small, "stopping_and_callback": stopping_checks(bad, good),
              "high_degree_checks": high_degree_checks(controls, feasibility)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
