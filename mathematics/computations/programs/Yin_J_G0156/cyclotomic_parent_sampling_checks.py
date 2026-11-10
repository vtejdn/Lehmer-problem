"""Bounded exact-parent controls only; no mutated polynomial or Mahler search."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import random
import time

from cyclotomic_closure import LEHMER, cyclotomic_products, generate
from cyclotomic_parent_sampling import NeutralMultisets, ParentSampler

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name


class Tickets:
    def __init__(self, values):
        self.values = iter(values)
        self.calls = []

    def randrange(self, bound):
        assert type(bound) is int and bound > 0
        value = next(self.values)
        assert type(value) is int and 0 <= value < bound
        self.calls.append((bound, value))
        return value


class Clock:
    def __init__(self, values):
        self.values = iter(values)

    def __call__(self):
        return next(self.values)


def callback_isolation_control():
    sampler = ParentSampler(LEHMER, 18)
    bad_powers = [0] * len(sampler.neutral.factors)
    bad_powers[0] = 4  # (z-1)^8; the selected parent's x^2 coefficient is 20.
    good_powers = [int(f.order == 16) for f in sampler.neutral.factors]  # 1+z^8.
    bad_rank = sampler.neutral.rank(8, bad_powers)
    good_rank = sampler.neutral.rank(8, good_powers)
    bad = sampler.construct(1, -1, bad_rank)
    good = sampler.construct(1, -1, good_rank)
    assert not bad["accepted"] and good["accepted"]
    seen = []

    def mutate_copy(number, candidate, seconds):
        seen.append((number, candidate["accepted"]))
        candidate["accepted"] = not candidate["accepted"]
        candidate["coefficients_ascending"][0] = 999
        candidate["neutral_factor_powers"][0][1] = 999
        candidate["neutral_factor_powers"].append([999, 999])

    rng = Tickets([0, 0, bad_rank, 0, 0, good_rank])
    result = sampler.sample_accepted(rng, max_attempts=2,
                                    clock=Clock([0, 0, 1, 1, 3, 4]),
                                    on_attempt=mutate_copy)
    assert result["status"] == "accepted" and result["parent"] == good
    assert result["attempts_started"] == 2 and result["height_rejections"] == 1
    assert result["construction_seconds"] == 3 and result["elapsed_seconds"] == 4
    assert seen == [(1, False), (2, True)] and len(rng.calls) == 6
    return {"callback_payload_isolation": "pass", "attempts": 2, "rejections": 1,
            "nested_coefficients_and_factor_powers": "unmodified internal parent"}


def census_controls():
    rows, rejection = [], None
    for degree, expected in ((18, 174), (20, 344), (24, 1170), (30, 5532)):
        sampler = ParentSampler(LEHMER, degree)
        started = time.perf_counter()
        accepted, raw, counts = set(), set(), []
        for k, count in enumerate(sampler.weights, 1):
            remainder = degree - k * 10
            old_neutral = set(cyclotomic_products(remainder))
            assert count == len(old_neutral)
            dp_neutral = set()
            accepted_k = 0
            for ticket in range(count):
                powers = sampler.neutral.unrank(remainder, ticket)
                assert sampler.neutral.rank(remainder, powers) == ticket
                dp_neutral.add(sampler.neutral.polynomial(powers))
                for sign in (-1, 1):
                    candidate = sampler.construct(k, sign, ticket)
                    polynomial = tuple(candidate["coefficients_ascending"])
                    assert polynomial not in raw
                    raw.add(polynomial)
                    if candidate["accepted"]:
                        accepted.add(polynomial[1:degree // 2 + 1])
                        accepted_k += 1
                    elif degree == 18 and rejection is None:
                        rejection = candidate
            assert dp_neutral == old_neutral
            counts.append({"substitution_index": k, "neutral_product_count": count,
                           "constructed_count": 2 * count, "accepted_count": accepted_k})
        existing, existing_counts = generate(LEHMER, degree)
        assert accepted == set(existing) and len(accepted) == expected
        assert len(raw) == 2 * sampler.weight_sum
        assert counts == [{name: row[name] for name in counts[0]} for row in existing_counts]
        # Integer interval sizes, not a frequency estimate of the categorical law.
        k_counts = Counter(sampler.select_k(t) for t in range(sampler.weight_sum))
        assert [k_counts[k] for k in range(1, len(sampler.weights) + 1)] == list(sampler.weights)
        rows.append({"degree": degree, "build": sampler.build, "counts": counts,
                     "accepted_count": len(accepted), "all_raw_parents_distinct": True,
                     "complete_neutral_and_parent_sets_equal": True,
                     "control_seconds": time.perf_counter() - started})
    assert rejection is not None
    return rows, rejection


def mechanical_controls(rejection):
    small = ParentSampler(LEHMER, 10)
    signs = []
    for bit in (0, 1):
        rng = Tickets([0, bit, 0])
        candidate = small.draw_raw(rng)
        assert candidate["accepted"] and candidate["sign"] == (-1, 1)[bit]
        assert [bound for bound, _ in rng.calls] == [1, 2, 1]
        signs.append(candidate["sign"])
    neutral = NeutralMultisets(2)
    assert neutral.count(0) == 1 and neutral.count(2) == 5
    assert {neutral.polynomial(neutral.unrank(2, t)) for t in range(5)} == {
        (1, -2, 1), (1, 2, 1), (1, 1, 1), (1, 0, 1), (1, -1, 1)}

    sampler = ParentSampler(LEHMER, 18)
    bad = [0, int(rejection["sign"] == 1), rejection["neutral_ticket"]]
    good = next(sampler.construct(1, sign, ticket)
                for ticket in range(sampler.weights[0]) for sign in (-1, 1)
                if sampler.construct(1, sign, ticket)["accepted"])
    good_tickets = [0, int(good["sign"] == 1), good["neutral_ticket"]]
    seen = []
    rng = Tickets(bad + good_tickets)
    result = sampler.sample_accepted(rng, max_attempts=2,
                                    clock=Clock([0, 0, 1, 1, 3, 4]),
                                    on_attempt=lambda i, p, t: seen.append((i, p["accepted"], t)))
    assert result["status"] == "accepted" and result["parent"] == good
    assert result["attempts_started"] == 2 and result["height_rejections"] == 1
    assert result["construction_seconds"] == 3 and result["elapsed_seconds"] == 4
    assert seen == [(1, False, 1), (2, True, 2)] and len(rng.calls) == 6

    exhausted = sampler.sample_accepted(Tickets(bad), max_attempts=1,
                                        clock=Clock([0, 0, 1, 1]))
    assert exhausted["status"] == "attempt_limit" and exhausted["parent"] is None
    assert exhausted["attempts_started"] == exhausted["height_rejections"] == 1
    no_draw = Tickets([])
    stopped = small.sample_accepted(no_draw, max_attempts=1, deadline=1,
                                    clock=Clock([1, 1, 1]))
    assert stopped["status"] == "deadline" and stopped["attempts_started"] == 0
    assert not no_draw.calls
    between = Tickets(bad)
    stopped_after_reject = sampler.sample_accepted(between, max_attempts=2, deadline=2,
                                                   clock=Clock([0, 0, 1, 2, 2]))
    assert stopped_after_reject["status"] == "deadline" and len(between.calls) == 3
    assert stopped_after_reject["height_rejections"] == 1
    overrun = small.sample_accepted(Tickets([0, 0, 0]), max_attempts=1, deadline=1,
                                    clock=Clock([0, 0, 3, 3]))
    assert overrun["status"] == "accepted" and overrun["soft_overrun_seconds"] == 2
    # Large integer ranks remain exact; no binary64 conversion of weights.
    high = ParentSampler(LEHMER, 80)
    for k, count in enumerate(high.weights, 1):
        remainder = 80 - 10 * k
        for ticket in {0, count // 2, count - 1}:
            assert high.neutral.rank(remainder, high.neutral.unrank(remainder, ticket)) == ticket
    try:
        ParentSampler(LEHMER, 1000)
    except ValueError:
        pass
    else:
        raise AssertionError("construction budget was not enforced")
    return {"integer_signs": signs, "degree_two_products": 5,
            "reject_then_accept_and_attempt_limit": "pass",
            "pre_attempt_deadline_and_uncensored_overrun": "pass",
            "large_integer_rank_endpoints": "pass", "construction_budget": "pass"}


def higher_degree_controls():
    rows = []
    for degree, seed in ((56, 5601), (80, 8001)):
        sampler = ParentSampler(LEHMER, degree)
        remainder = degree - 10
        # x^r+1 = product_{m|2r, m not|r} Phi_m, a known neutral witness.
        powers = tuple(int(2 * remainder % f.order == 0 and remainder % f.order != 0)
                       if f.order >= 3 else 0 for f in sampler.neutral.factors)
        ticket = sampler.neutral.rank(remainder, powers)
        neutral = sampler.neutral.polynomial(powers)
        assert neutral == (1,) + (0,) * (remainder - 1) + (1,)
        witnesses = [sampler.construct(1, sign, ticket) for sign in (-1, 1)]
        assert all(p["accepted"] and p["observed_height"] == 1 for p in witnesses)
        attempts = []
        # A finite mechanical use of the rejection helper, never a Mahler search.
        result = sampler.sample_accepted(random.Random(seed), max_attempts=32,
                                          deadline=time.perf_counter() + 2,
                                          on_attempt=lambda i, p, t: attempts.append({
                                              "attempt": i, "accepted": p["accepted"],
                                              "height": p["observed_height"], "seconds": t,
                                              "substitution_index": p["substitution_index"]}))
        assert result["attempts_started"] == len(attempts) <= 32
        assert result["height_rejections"] == sum(not p["accepted"] for p in attempts)
        rows.append({"degree": degree, "seed": seed, "build": sampler.build,
                     "explicit_height_one_witnesses": witnesses,
                     "mechanical_rejection_control": result, "attempt_costs": attempts})
    return rows


def feasibility_controls():
    """Fixed raw counts, with one shared soft cap; never mutate or measure."""
    started = time.perf_counter()
    deadline = started + 20
    rows = []
    for degree, seed in ((56, 56002), (80, 80002)):
        row_started = time.perf_counter()
        attempts = accepted = 0
        unique_accepted = set()
        attempt_seconds = maximum_attempt = 0.0
        status = "raw_count_completed"
        sampler = None
        if row_started >= deadline:
            status = "shared_deadline"
        else:
            sampler = ParentSampler(LEHMER, degree)
            rng = random.Random(seed)
            for _ in range(10000):
                before = time.perf_counter()
                if before >= deadline:
                    status = "shared_deadline"
                    break
                candidate = sampler.draw_raw(rng)
                elapsed = time.perf_counter() - before
                attempts += 1
                attempt_seconds += elapsed
                maximum_attempt = max(maximum_attempt, elapsed)
                if candidate["accepted"]:
                    accepted += 1
                    unique_accepted.add(tuple(candidate["coefficients_ascending"]))
        rows.append({
            "degree": degree, "seed": seed, "requested_raw_proposals": 10000,
            "status": status, "completed_raw_proposals": attempts,
            "height_accepted": accepted, "distinct_accepted_parents": len(unique_accepted),
            "height_rejected": attempts - accepted,
            "build": sampler.build if sampler is not None else None,
            "construction_seconds": attempt_seconds, "max_attempt_seconds": maximum_attempt,
            "elapsed_seconds": time.perf_counter() - row_started,
            "accepted_coefficients_ascending": [list(p) for p in sorted(unique_accepted)],
        })
    finished = time.perf_counter()
    assert all(row["height_accepted"] + row["height_rejected"] == row["completed_raw_proposals"]
               for row in rows)
    return {
        "scope": "Parent-only finite feasibility control; no mutation or Mahler evaluation.",
        "shared_soft_limit_seconds": 20, "elapsed_seconds": finished - started,
        "soft_overrun_seconds": max(0.0, finished - deadline), "groups": rows,
        "interpretation": "Observed fixed seeded raw counts only; no general acceptance-rate or timed-uniformity claim.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=OUTPUT / "cyclotomic_parent_sampling_controls.json")
    parser.add_argument("--feasibility", action="store_true",
                        help="only the two fixed 10000-raw parent controls under one 20-second soft cap")
    parser.add_argument("--callback-control", action="store_true",
                        help="only the detached-callback two-attempt mechanical regression")
    args = parser.parse_args()
    if args.feasibility and args.callback_control:
        parser.error("choose one bounded control mode")
    if args.output.exists():
        raise FileExistsError(args.output)
    if args.callback_control:
        result = callback_isolation_control()
    elif args.feasibility:
        result = feasibility_controls()
    else:
        census, rejection = census_controls()
        result = {
            "scope": "Exact parent sampling preparation; no mutated polynomial or Mahler evaluation.",
            "complete_small_comparisons": census,
            "mechanical_controls": mechanical_controls(rejection),
            "higher_degree_controls": higher_degree_controls(),
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    if args.callback_control:
        print(json.dumps(result))
        return
    if args.feasibility:
        print(json.dumps({key: ([{k: v for k, v in row.items() if k != "accepted_coefficients_ascending"}
                                for row in value] if key == "groups" else value)
                          for key, value in result.items()}))
        return
    print(json.dumps({
        "small": [{"degree": row["degree"], "accepted": row["accepted_count"],
                   "raw": row["build"]["raw_parent_count"]} for row in census],
        "mechanical_controls": result["mechanical_controls"],
        "higher": [{"degree": row["degree"], "build": row["build"],
                    "status": row["mechanical_rejection_control"]["status"],
                    "attempts": row["mechanical_rejection_control"]["attempts_started"]}
                   for row in result["higher_degree_controls"]],
        "output": str(args.output),
    }))


if __name__ == "__main__":
    main()
