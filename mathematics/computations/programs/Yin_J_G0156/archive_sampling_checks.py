"""Bounded implementation controls, excluded from the formal archive comparison.

No result here is a new-value or live-performance claim.  Synthetic ledger and
screen fixtures test decisions; subprocess controls use seeds >= 100, <= 2 s.
"""

import argparse
import copy
import io
import json
from pathlib import Path
import time

import archive_sampling as live


def exact_mechanism_checks():
    checked = {}
    for degree in live.DEGREES:
        sparse = live.sparse_completions(live.SEED_CORE, degree)
        # Independent polynomial ring construction of the sparse formula.
        expected = set()
        for k in range(1, degree // 10 + 1):
            for sign in (-1, 1):
                lifted = [0] * (10 * k + 1)
                for i, coefficient in enumerate(live.SEED_CORE):
                    lifted[k * i] = coefficient * sign**i
                remainder = degree - 10 * k
                neutral = [1] if not remainder else [1] + [0] * (remainder - 1) + [1]
                polynomial = live.frozen.fmpz_poly(lifted) * live.frozen.fmpz_poly(neutral)
                coefficients = list(map(int, polynomial))
                if max(map(abs, coefficients)) <= 4:
                    expected.add(tuple(coefficients[1:degree // 2 + 1]))
        assert set(sparse) == expected
        full, _ = live.closure.generate(live.SEED_CORE, degree)
        assert len(full) == {24: 1170, 30: 5532}[degree]
        assert set(sparse) <= set(full)
        fixed = live.ArchiveLaw(degree, "fixed", 100)
        original = live.OriginalLaw(degree // 2, "fixed", 100)
        assert fixed.initialize() is None and fixed.cores == {}
        for _ in range(257):
            assert fixed.draw() == original.draw()
        direct = live.ArchiveLaw(degree, "direct", 100)
        direct.initialize()
        prefix = sparse[0]
        first = direct.observe_target(live.SEED_CORE, prefix)
        second = direct.observe_target(live.SEED_CORE, prefix)
        assert first["new_observed_template"] and not first["added_template"]
        assert not second["new_observed_template"] and len(direct.cores) == 1
        nongenerated = next(prefix for prefix in full if prefix not in expected)
        added = direct.observe_target(live.SEED_CORE, nongenerated)
        assert added["added_template"] and added["observed_nongenerated_template_count"] == 1
        # A separate endpoint check reconstructs each returned mutation.
        branches, boundary = set(), 0
        for _ in range(1000):
            sample = direct.draw()
            metadata = direct.last_draw
            branches.add(metadata["branch"])
            assert len(sample) == degree // 2 and all(-4 <= a <= 4 for a in sample)
            if metadata["branch"] == "archive_mutation":
                endpoint = list(metadata["parent_free_coefficients"])
                assert len(set(metadata["coordinates"])) == metadata["k"]
                for index, sign in zip(metadata["coordinates"], metadata["signs"]):
                    endpoint[index] += sign
                exited = any(abs(a) > 4 for a in endpoint)
                assert metadata["boundary_return"] == exited
                assert sample == (metadata["parent_free_coefficients"] if exited else endpoint)
                boundary += exited
        assert branches == {"uniform_box", "archive_mutation"}
        # Force a legal edge template to exercise the no-resampling branch.
        edge = tuple([4] * (degree // 2))
        direct.cores[live.SEED_CORE]["templates"] = [edge]
        for _ in range(100):
            sample = direct.draw()
            if direct.last_draw["branch"] == "archive_mutation" and direct.last_draw["boundary_return"]:
                assert sample == list(edge)
                boundary += 1
        assert boundary > 0
        checked[str(degree)] = {"sparse_templates": len(sparse), "closure_templates": len(full),
                                "fixed_exact_draws": 257, "endpoint_checks": 1000, "boundary_returns_checked": boundary}
    return checked


def ledger_and_new_core_checks():
    seed = live.frozen.certify_polynomial(list(live.SEED_CORE))
    ledger = live.SeededLedger(seed)
    recovered = ledger.add(seed, 1)
    assert recovered["seed_recovery"] and not recovered["new_nonseed_value"]
    # Synthetic interval-only control: a different core may overlap the seed.
    overlap = copy.deepcopy(seed)
    overlap["core_coefficients_ascending"] = [1, 0, 1]
    ambiguous = ledger.add(overlap, 2)
    assert ambiguous["seed_relation"] == "unresolved_overlap_with_seed"
    assert ambiguous["identity"]["status"] == "unresolved_equality" and not ambiguous["certified_nonseed_value"]
    assert not ledger.add(overlap, 3)["certified_nonseed_value"]
    below = copy.deepcopy(seed)
    below["core_coefficients_ascending"] = [1, 1, 1]
    below["measure_interval"] = [[9, -3], [9, -3]]  # Synthetic exact 9/8 enclosure.
    result = ledger.add(below, 4)
    assert result["new_nonseed_value"] and result["seed_relation"] == "strictly_below_seed_enclosure"
    # The actual second known core is used ONLY in this labelled mechanism test.
    second = next(core for core in live.load_catalog() if core != live.SEED_CORE)
    certificate = live.frozen.certify_polynomial(list(second))
    discovered = ledger.add(certificate, 5)
    assert discovered["new_nonseed_value"] and discovered["seed_relation"] == "strictly_above_seed_enclosure"
    for variant in ("direct", "closure"):
        law = live.ArchiveLaw(24, variant, 101)
        law.initialize()
        prefix = live.sparse_completions(second, 24)[0]
        update = law.observe_target(second, prefix)
        assert update["new_core"]["core_coefficients_ascending"] == list(second)
        assert list(law.cores) == [live.SEED_CORE, second]
        assert prefix in law.cores[second]["templates"]
        assert not law.observe_target(second, prefix)["new_observed_template"]
    # New successful observed template survives even an empty sparse completion.
    original = live.sparse_completions
    try:
        law = live.ArchiveLaw(24, "direct", 102)
        law.initialize()
        live.sparse_completions = lambda core, degree: []
        update = law.observe_target(second, prefix)
        assert update["generated_template_count"] == 0 and update["distinct_template_count"] == 1
        assert law.cores[second]["templates"] == [prefix]
    finally:
        live.sparse_completions = original
    return {"seed_excluded": True, "overlap_unresolved": True, "strict_below_seed_fixture": True,
            "new_core_and_empty_sparse_controls": True}


def screen_checks():
    rows = [{"degree": degree, "arm": variant, "seed": seed, "eligible_archive_comparison_run": True,
             "archive_metrics": {"distinct_nonseed_target_values": 0}, "first_nonseed_hit_seconds": None}
            for degree, variant, seed in live.schedule()]
    screen = live.allocation_screen(rows)
    assert screen["complete_declared_archive_comparison"] and screen["nonloss_screen_passes_at_both_degrees"]
    assert not screen["allocation_screen_passes"]
    assert not live.allocation_screen(rows[:-1])["complete_declared_archive_comparison"]
    assert not live.allocation_screen(rows[:-1] + [rows[0]])["complete_declared_archive_comparison"]
    for row in rows:
        row["archive_metrics"]["distinct_nonseed_target_values"] = 1
        row["first_nonseed_hit_seconds"] = 5.0 if row["arm"] != "closure" else 4.0
    assert live.allocation_screen(rows)["allocation_screen_passes"]
    # Separate groups of three wins are insufficient: only one joint seed wins.
    for row in rows:
        if row["arm"] == "fixed":
            row["first_nonseed_hit_seconds"] = 5.0 if row["seed"] <= 22 else 3.0
        if row["arm"] == "direct":
            row["first_nonseed_hit_seconds"] = 5.0 if row["seed"] >= 22 else 3.0
    assert all(group["closure_joint_improvements"] == 1 for group in live.allocation_screen(rows)["degree_screens"])
    assert not live.allocation_screen(rows)["allocation_screen_passes"]
    rows[0]["eligible_archive_comparison_run"] = False
    assert not live.allocation_screen(rows)["complete_declared_archive_comparison"]
    expected_first = [(24, "fixed", 20), (24, "direct", 20), (24, "closure", 20),
                      (24, "direct", 21), (24, "closure", 21), (24, "fixed", 21)]
    assert live.schedule()[:6] == expected_first
    assert live.schedule()[15:18] == [(30, "direct", 20), (30, "closure", 20), (30, "fixed", 20)]
    return {"zero_zero_never_improves": True, "joint_same_seed_rule": True,
            "missing_duplicate_failure_identities": True, "rotated_30_run_schedule": True}


def hook_atomicity_check():
    """Scripted callback control, not an RNG experiment or performance result."""
    original_worker = live.frozen.worker
    stream = io.StringIO()
    seed_prefix = live.sparse_completions(live.SEED_CORE, 24)[0]
    seed_certificate = live.frozen.certify_polynomial(live.frozen.reciprocal_polynomial(list(seed_prefix)))
    second = next(core for core in live.load_catalog() if core != live.SEED_CORE)
    second_prefix = live.sparse_completions(second, 24)[0]
    second_certificate = live.frozen.certify_polynomial(live.frozen.reciprocal_polynomial(list(second_prefix)))
    args = argparse.Namespace(degree=24, variant="direct", seed=103, seconds=2,
                              started=time.perf_counter(), max_proposals=0, events="unused", fail_after_first_proposal=False)

    def scripted_worker(unused):
        live.frozen.write_event(stream, {"kind": "config", "seconds": 2, "max_proposals": 0})
        # Factor-only target cannot invoke the archive or primary target ledger.
        live.frozen.write_event(stream, {"kind": "evaluation", "proposal": 1,
                                        "thresholds": {"6/5": "above"}, "factor_discoveries": [{"test_fixture": True}]})
        live.frozen.write_event(stream, {"kind": "commit", "proposal": 1, "elapsed": 0.1})
        for proposal, certificate in ((2, seed_certificate), (3, second_certificate)):
            live.frozen.write_event(stream, {"kind": "evaluation", "proposal": proposal,
                                            "thresholds": certificate["thresholds"], "certificate": certificate,
                                            "cost_seconds": {}})
            if proposal == 2:
                live.frozen.write_event(stream, {"kind": "commit", "proposal": 2, "elapsed": 0.2})

    try:
        live.frozen.worker = scripted_worker
        live.worker(args)
    finally:
        live.frozen.worker = original_worker
    events = [json.loads(line) for line in stream.getvalue().splitlines()]
    evaluations = [event for event in events if event["kind"] == "evaluation"]
    assert "archive_update" not in evaluations[0] and "seeded_target" not in evaluations[0]
    assert evaluations[2]["archive_update"]["new_core"] is not None  # Computed, but not committed.
    record = {"configuration": {"seconds": 2}, "observed_run_seconds": 2}
    live.enrich_record(record, events)
    assert record["archive_metrics"]["distinct_nonseed_target_values"] == 0
    assert len(record["final_archive"]) == 1 and record["final_archive"][0]["observed_template_count"] == 1
    assert len(record["committed_archive_changes"]) == 1
    assert not record["nonseed_discoveries"] and record["first_nonseed_hit_censored_at"] == 2
    uncommitted = [event for event in events if event["kind"] not in ("commit", "archive_initialization_commit")]
    live.enrich_record(record, uncommitted)
    assert not record["archive_initialization_committed"] and record["final_archive"] == []
    return {"factor_only_does_not_train": True, "uncommitted_core_excluded": True,
            "uncommitted_initialization_excluded": True}


def subprocess_checks(label):
    if not label.startswith("control_"):
        raise ValueError("checks require a control_ label")
    results = []
    for degree in live.DEGREES:
        for index, variant in enumerate(live.VARIANTS):
            seed = 100 + index
            record = live.run_once(degree, variant, seed, 2, label, 257)
            config = record["configuration"]
            assert (config["degree"], config["variant"], config["seed"]) == (degree, variant, seed)
            assert config["precision_bits"] == 128 and config["cache_size"] == 4096
            assert record["counts"]["completed_proposals"] == 257
            assert record["termination_reason"] == "proposal_limit" and not record["eligible_archive_comparison_run"]
            assert record["archive_initialization_committed"]
            if variant == "closure":
                assert record["final_archive"][0]["generated_template_count"] == {24: 1170, 30: 5532}[degree]
            assert record["counts"].get("adaptive_updates", 0) == 0
            replay = live.replay_journal(live.run_stem(label, degree, variant, seed).with_suffix(".jsonl"))
            assert replay["checked_proposals"] == 257
            results.append({"degree": degree, "variant": variant, "seed": seed,
                            "completed": 257, "initialization_elapsed": record["archive_initialization_elapsed"], **replay})
    deadline_label = label + "_deadline"
    record = live.run_once(30, "closure", 103, 2, deadline_label)
    assert record["valid_run"] and record["termination_reason"] == "deadline"
    assert not record["eligible_archive_comparison_run"]
    assert record["last_committed_elapsed"] <= 2
    replay = live.replay_journal(live.run_stem(deadline_label, 30, "closure", 103).with_suffix(".jsonl"))
    failure_label = label + "_failure"
    failure = live.run_once(24, "direct", 104, 2, failure_label, failure_check=True, raise_on_failure=False)
    assert not failure["valid_run"] and failure["termination_reason"] == "worker_failure"
    assert failure["counts"]["proposals"] == 1 and failure["counts"]["completed_proposals"] == 0
    assert failure["archive_metrics"]["distinct_nonseed_target_values"] == 0
    assert failure["first_nonseed_hit_censored_at"] < 2
    return {"proposal_controls": results, "deadline_completed": record["counts"]["completed_proposals"],
            "deadline_replay": replay, "deadline_label": deadline_label, "failure_label": failure_label,
            "failure_preserved": True, "subprocess_budget_ceiling_seconds": 16}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True)
    parser.add_argument("--mechanism-only", action="store_true")
    args = parser.parse_args()
    result = {"protocol": live.PROTOCOL, "scope": "ordinary author implementation checks; not formal sampling data",
              "mechanisms": exact_mechanism_checks(), "ledger": ledger_and_new_core_checks(),
              "screen": screen_checks(), "atomicity": hook_atomicity_check()}
    if not args.mechanism_only:
        result["subprocess"] = subprocess_checks(args.label)
    live.OUTPUT.mkdir(parents=True, exist_ok=True)
    path = live.OUTPUT / f"{args.label}_checks.json"
    if path.exists():
        raise FileExistsError("choose a fresh checks label")
    live.frozen.write_json(path, result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
