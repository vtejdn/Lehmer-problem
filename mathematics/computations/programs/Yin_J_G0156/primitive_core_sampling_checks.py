"""Mechanical checks and the five explicitly bounded D56 child controls.

The subprocess mode starts exactly five runs, each at most two seconds: direct
and DP at max32 proposals, two deadlines, and one deliberate DP worker failure.
It never repeats an unsuccessful stochastic control automatically.
"""

import argparse
import copy
import io
import json
from pathlib import Path
import random
import tempfile
import time
from unittest import mock

import primitive_core_sampling as live
import primitive_core_sampling_export as export


def startup_failure_fixture(stem):
    """Exercise the real runtime's failed-start branch without starting a child."""
    args = argparse.Namespace(degree=56, variant="dp_closure", seed=104, seconds=2, max_proposals=0)
    with mock.patch.object(live.runtime.subprocess, "Popen", side_effect=OSError("mechanical startup failure")) as start:
        record = live.runtime.supervise(live.__file__, stem, args, live.configuration(56, "dp_closure", 104))
    start.assert_called_once()
    assert record["configuration_source"] == "requested; worker produced no configuration"
    assert record["supervision"]["worker_returncode"] == -1
    return live.enrich(record, [])


def factor_structure(polynomial, degree=56):
    poly = live.frozen.fmpz_poly(polynomial)
    content, factors = poly.factor()
    assert content == 1
    certificate = {"coefficients_ascending": polynomial,
                   "core_coefficients_ascending": live.frozen.normalized_core(factors),
                   "neutral": all(factor.is_cyclotomic() for factor, _ in factors),
                   "factors": [{"coefficients_ascending": list(map(int, factor)), "exponent": int(power),
                                "degree": int(factor.degree()), "cyclotomic": bool(factor.is_cyclotomic())}
                               for factor, power in factors]}
    return live.structural_diagnostics(certificate, degree)


def mechanism_checks():
    parents = live.direct_parents()
    assert len(parents) == 10
    assert all(len(parent["coefficients_ascending"]) == 57 for parent in parents)
    assert factor_structure([1, -3, 1], 2)["primary_class"]
    repeat = list(live.archive.closure.multiply([1, -3, 1], [1, -3, 1]))
    assert not factor_structure(repeat, 4)["primary_class"]
    substitute = [0] * 57
    substitute[0], substitute[28], substitute[56] = 1, -3, 1
    diagnostic = factor_structure(substitute)
    assert diagnostic["output_exponent_gcd"] == 28 and not diagnostic["primary_class"]
    q23 = [0] * 47
    q23[0], q23[23], q23[46] = 1, -3, 1
    reducible56 = list(live.archive.closure.multiply(live.SEED_CORE, q23))
    diagnostic = factor_structure(reducible56)
    assert diagnostic["normalized_whole_core_degree"] == 56 and diagnostic["noncyclotomic_product_reducible"]
    assert not diagnostic["primary_class"]
    phi87 = list(map(int, live.frozen.fmpz_poly.cyclotomic(87)))
    diagnostic = factor_structure(phi87)
    assert diagnostic["output_degree"] == 56 and diagnostic["output_irreducible"] and diagnostic["output_exponent_gcd"] == 1
    assert diagnostic["cyclotomic_degree"] == 56 and not diagnostic["primary_class"]
    factor = diagnostic["individual_irreducible_factors"][0]
    assert factor["coefficients_ascending"] == phi87 and factor["degree"] == 56
    assert not factor["noncyclotomic_normalization_applicable"]
    assert factor["compressed_sign_normalized_coefficients_ascending"] is None
    # Independent order test for a single paired move, with repeated neutral
    # multiplicities.  Phi_m divides 1+z^r iff m|2r and m does not divide r.
    factors = [(2, 2), (4, 3), (12, 2)]
    neutral = live.frozen.fmpz_poly([1])
    for order, power in factors:
        neutral *= live.frozen.fmpz_poly.cyclotomic(order)**power
    lifted = [0] * 41
    for i, value in enumerate(live.SEED_CORE):
        lifted[4 * i] = value
    parent = {"neutral_coefficients_ascending": list(map(int, neutral)),
              "coefficients_ascending": list(map(int, live.frozen.fmpz_poly(lifted) * neutral))}
    assert len(parent["coefficients_ascending"]) == 57
    for i in (1, 13, 14, 27, 28):
        delta = [0] * 57
        delta[i] = 1
        if i != 28:
            delta[56 - i] = 1
        child = [a + b for a, b in zip(parent["coefficients_ascending"], delta)]
        observed = live.parent_diagnostics({"parent": parent, "mutation": {"delta_coefficients_ascending": delta}}, child)
        expected = live.frozen.fmpz_poly([1])
        if i != 28:
            r = 56 - 2 * i
            for order, _ in factors:
                if 2 * r % order == 0 and r % order != 0:
                    expected *= live.frozen.fmpz_poly.cyclotomic(order)
        assert observed["old_neutral_gcd_coefficients_ascending"] == list(map(int, expected))
    unchanged = live.parent_diagnostics({"parent": parent, "mutation": {"delta_coefficients_ascending": [0] * 57}}, parent["coefficients_ascending"])
    assert unchanged["old_neutral_gcd_coefficients_ascending"] == list(map(int, neutral))
    assert not live.parent_diagnostics({"parent": None}, [1] + [0] * 55 + [1])["applicable"]
    return {"direct_templates": 10, "exact_structure_fixtures": "pass",
            "reducible_normalized_degree56_rejected": True, "neutral_phi87_excluded": True,
            "paired_move_order_gcd_fixtures": 5, "boundary_and_uniform_diagnostics": "pass"}


def stopping_and_replay_checks():
    stream = io.StringIO()
    writer = live.Writer(stream, time.perf_counter())
    sampler = live.LoggedParentSampler(56, writer)
    # A deterministic rejection stub checks all 4096 iterations and their cost
    # accounting without constructing or certifying any trial polynomial.
    sampler.construct = lambda k, sign, rank: {"substitution_index": k, "sign": sign,
        "neutral_ticket": rank, "observed_height": 5, "accepted": False}
    result = sampler.parent(random.Random(0), 1, None)
    assert result["status"] == "attempt_limit" and result["attempts_started"] == result["height_rejections"] == 4096
    events = [json.loads(line) for line in stream.getvalue().splitlines()]
    assert all(sum(event["kind"] == kind for event in events) == 4096
               for kind in ("raw_attempt_intent", "raw_attempt_ticket", "raw_attempt_result"))
    record = {"configuration": {**live.configuration(56, "dp_closure", 30), "seconds": 20, "max_proposals": 0},
              "counts": {"completed_proposals": 0}, "parent_attempt_limit_stop": True,
              "supervision": {"killed_at_cap": True, "worker_returncode": 0, "supervisor_elapsed_seconds": 20}}
    assert not live.validity(record)["eligible_primitive_comparison_run"]
    assert live.validity(record)["termination_reason"] == "parent_attempt_limit"
    # Actual integer tickets only, no roots: preserve an interrupted first raw
    # attempt both before and after the three selected choices are journalled.
    config = live.configuration(56, "dp_closure", 0)
    rng = random.Random(0)
    ticket = rng.randrange(10)
    assert ticket != 0
    dp = live.ParentSampler(live.SEED_CORE, 56, 4)
    k_ticket = rng.randrange(dp.weight_sum)
    k = dp.select_k(k_ticket)
    sign_ticket = rng.randrange(2)
    rank = rng.randrange(dp.weights[k - 1])
    events = [{"kind": "generation_start", "request": 1},
              {"kind": "generation_branch", "request": 1, "branch_ticket": ticket, "branch": "dp_closure"},
              {"kind": "raw_attempt_intent", "request": 1, "attempt": 1, "request_attempt": 1}]
    before = export.replay_generation(events, config)
    assert before["pending_generation"]["observed_phase"] == "raw_selection_pending"
    events.append({"kind": "raw_attempt_ticket", "request": 1, "attempt": 1, "request_attempt": 1,
                   "substitution_ticket": k_ticket, "substitution_index": k, "sign_ticket": sign_ticket,
                   "sign": (-1, 1)[sign_ticket], "neutral_ticket": rank})
    after = export.replay_generation(events, config)
    assert after["pending_generation"]["observed_phase"] == "raw_construction_pending"
    assert before["pending_generation"]["reconstructed_raw_candidate"] == after["pending_generation"]["reconstructed_raw_candidate"]
    stream = io.StringIO()
    writer = live.Writer(stream, time.perf_counter())
    generation = live.generate(random.Random(0), 1, 56, "direct", live.direct_parents(), None, writer, float("inf"))
    events = [json.loads(line) for line in stream.getvalue().splitlines()]
    pending = export.replay_generation(events, live.configuration(56, "direct", 0))
    assert pending["pending_generation"]["free_coefficients"] == generation["free_coefficients"]
    writer.emit("proposal", request=1, proposal=1, elapsed=2.000001,
                free_coefficients=generation["free_coefficients"],
                coefficients_ascending=live.frozen.reciprocal_polynomial(generation["free_coefficients"]), generation=generation)
    replay = export.replay_generation([json.loads(line) for line in stream.getvalue().splitlines()], live.configuration(56, "direct", 0))
    assert replay["journalled_whole_proposals"] == 1 and replay["pending_generation"] is None
    entries = [json.loads(line) for line in stream.getvalue().splitlines()]
    assert list(export.unpack_events(export.pack_events(entries))) == entries
    assert live.schedule()[:4] == [("direct", 30), ("dp_closure", 30), ("dp_closure", 31), ("direct", 31)]
    missing = live.OUTPUT / "control_primitive_mechanical_no_journal.json"
    assert not missing.with_suffix(".jsonl").exists()
    failed = startup_failure_fixture(missing.with_suffix(""))
    retained = export.retain_run(failed, missing, export.common.Witnesses())
    assert not retained["valid_run"] and not retained["generation_trace"]["rows"]
    assert not retained["evaluation_observations"] and retained["generation_replay"]["journalled_whole_proposals"] == 0
    return {"mock_rejections": 4096, "exhaustion_invalid_even_at_deadline": True,
            "pending_selection_and_construction_replayed": True, "pending_mutation_replayed": True,
            "after_cap_whole_proposal_replayed": True, "ten_identity_rotation": True,
            "explicit_no_configuration_startup_failure_retained": True}


def ledger_checks():
    # Only retained low-degree known-core enclosures and synthetic intervals;
    # no new root computation or asserted degree56 discovery is involved.
    catalog = live.archive.load_catalog()
    seed = {**catalog[live.SEED_CORE], "thresholds": {key: "below" for key in live.frozen.THRESHOLDS}}
    other = next({**item, "thresholds": seed["thresholds"]} for core, item in catalog.items() if core != live.SEED_CORE)
    whole, primary = live.archive.SeededLedger(seed), live.archive.SeededLedger(seed)
    assert not whole.add(seed, 1)["new_nonseed_value"] and not primary.add(seed, 1)["new_nonseed_value"]
    assert whole.add(other, 2)["new_nonseed_value"] and primary.add(other, 3)["new_nonseed_value"]
    overlap = dict(seed, core_coefficients_ascending=[1, 0, 1])
    assert not primary.add(overlap, 4)["certified_nonseed_value"]
    best = live.PrimitiveBest()
    first = {"core_coefficients_ascending": [1, 1, 1], "measure_interval": [[20, -4], [24, -4]]}
    second = {"core_coefficients_ascending": [1, 2, 1], "measure_interval": [[21, -4], [22, -4]]}
    third = {"core_coefficients_ascending": [1, 3, 1], "measure_interval": [[19, -4], [19, -4]]}
    best.add(first, 1)
    snapshot = best.add(second, 2)
    assert snapshot["contender_proposals"] == [1, 2] and snapshot["minimum_measure_enclosure"] == [[20, -4], [22, -4]]
    assert not snapshot["unique_minimizing_coefficient_core_certified"]
    snapshot = best.add(third, 3)
    assert snapshot["contender_proposals"] == [3] and snapshot["unique_minimizing_coefficient_core_certified"]
    return {"independent_seed_excluding_ledgers": True, "overlap_unresolved": True, "finite_minimum_contenders": True}


def export_controls(label, source_label):
    paths = [live.run_stem(source_label, 56, variant, seed).with_suffix(".json")
             for variant, seed in (("direct", 100), ("dp_closure", 101), ("direct", 102), ("dp_closure", 103), ("dp_closure", 104))]
    comparison, witnesses = export.write_exports(source_label, live.OUTPUT / f"{label}_native_comparison.json",
        live.OUTPUT / f"{label}_native_witnesses.json", True, paths)
    assert comparison["retained_run_count"] == 5 and not comparison["complete_declared_primitive_comparison"]
    results = []
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            replay = export.replay_generation(export.unpack_events(row["generation_trace"]), row["configuration"])
            assert replay == row["generation_replay"]
            results.append({"arm": row["arm"], "seed": row["seed"], "proposals": replay["journalled_whole_proposals"],
                            "raw_attempts": replay["raw_attempt_intents"]})
    return {"runs": results, "witnesses": len(witnesses["witnesses"]), "lossless_table_and_replay": "pass"}


def compare_retention(before_path, after_path):
    before, after = export.common.read_json(before_path), export.common.read_json(after_path)
    same = lambda left, right: json.dumps(left, sort_keys=True, separators=(",", ":")) == json.dumps(right, sort_keys=True, separators=(",", ":"))
    compared_events = removed_tickets = compared_runs = 0
    for old_group, new_group in zip(before["groups"], after["groups"]):
        assert old_group["arm"] == new_group["arm"]
        assert len(old_group["all_seed_outcomes"]) == len(new_group["all_seed_outcomes"])
        for old, new in zip(old_group["all_seed_outcomes"], new_group["all_seed_outcomes"]):
            old, new = copy.deepcopy(old), copy.deepcopy(new)
            events = old.pop("generation_events")
            table_events = list(export.unpack_events(new.pop("generation_trace")))
            assert same(events, table_events)
            old_replay, new_replay = old.pop("generation_replay"), new.pop("generation_replay")
            tickets = old_replay.pop("raw_ticket_inputs")
            observed = new_replay.pop("raw_tickets_observed")
            assert observed == sum(ticket["ticket_observed"] for ticket in tickets)
            assert same(old_replay, new_replay) and same(old, new)
            by_id = {event["attempt"]: event for event in table_events if event["kind"] == "raw_attempt_ticket"}
            results = {event["attempt"] for event in table_events if event["kind"] == "raw_attempt_result"}
            for ticket in tickets:
                assert ticket["ticket_observed"] == (ticket["attempt"] in by_id)
                assert ticket["result_observed"] == (ticket["attempt"] in results)
                if ticket["ticket_observed"]:
                    assert all(by_id[ticket["attempt"]][key] == value for key, value in ticket.items()
                               if key not in ("ticket_observed", "result_observed"))
            compared_events += len(events)
            removed_tickets += len(tickets)
            compared_runs += 1
    assert same({key: value for key, value in before.items() if key != "groups"},
                {key: value for key, value in after.items() if key != "groups"})
    return {"runs": compared_runs, "generation_events_equal": compared_events,
            "duplicate_ticket_copies_removed": removed_tickets,
            "certificates_metrics_costs_failure_inputs": "exact JSON values and scalar types preserved"}


def structure_controls(source_label, native_path):
    checked = neutral_items = native_checked = 0
    identities = (("direct", 100), ("dp_closure", 101), ("direct", 102), ("dp_closure", 103), ("dp_closure", 104))

    def check(certificate, observed):
        nonlocal checked, neutral_items
        expected = live.combine_diagnostics(live.structural_diagnostics(certificate), observed["parent_neutral"])
        adjusted = copy.deepcopy(observed)
        for item in adjusted["individual_irreducible_factors"]:
            item["noncyclotomic_normalization_applicable"] = not item["cyclotomic"]
            if item["cyclotomic"]:
                # The first controls recorded frozen.normalized_core(Phi)=[1].
                # Preserve those historical bytes; only this checked comparison
                # changes the interpretation to explicitly inapplicable.
                assert item["compressed_sign_normalized_coefficients_ascending"] in ([1], None)
                item["compressed_sign_normalized_coefficients_ascending"] = None
                neutral_items += 1
        assert adjusted == expected
        checked += 1

    for variant, seed in identities:
        path = live.run_stem(source_label, 56, variant, seed).with_suffix(".jsonl")
        for event in export.journal_events(path):
            if event["kind"] == "evaluation" and "diagnostics" in event:
                check(event["certificate"], event["diagnostics"])
    journal_checked = checked
    native = export.common.read_json(native_path)
    assert native["label"] == source_label and native["retained_run_count"] == 5
    for group in native["groups"]:
        for row in group["all_seed_outcomes"]:
            for event in row["evaluation_observations"]:
                if "diagnostics" in event:
                    check(event["certificate"], event["diagnostics"])
                    native_checked += 1
    assert native_checked == journal_checked
    return {"journal_structures": journal_checked, "native_structures": native_checked,
            "cyclotomic_items_checked_across_both": neutral_items,
            "only_difference": "explicit noncyclotomic normalization applicability and null for cyclotomic items",
            "original_factor_coefficients_degrees_and_all_classifications": "unchanged",
            "sampling_or_roots": "none"}


def evidence_controls(label, source_label):
    """Existing history plus incomplete-evidence fixtures; no children or roots."""
    identities = (("direct", 100), ("dp_closure", 101), ("direct", 102), ("dp_closure", 103), ("dp_closure", 104))
    original = {}
    for arm, seed in identities:
        path = live.run_stem(source_label, 56, arm, seed).with_suffix(".json")
        record = export.common.read_json(path)
        events = list(export.journal_events(path.with_suffix(".jsonl")))
        assert export.validate_journal_evidence(record, path.with_suffix(".jsonl"), events)
        original[seed] = (record, events)
    rejected, accepted = [], []
    # These disposable copies are confined to the output directory; verify the
    # resolved cleanup target before TemporaryDirectory can remove its tree.
    with tempfile.TemporaryDirectory(prefix=label + "_", dir=live.OUTPUT) as temporary:
        directory = Path(temporary).resolve()
        assert directory.is_relative_to(live.OUTPUT.resolve()) and directory != live.OUTPUT.resolve()

        def fixture(name, record, events=None, tail=""):
            path = directory / (name + ".json")
            copied = copy.deepcopy(record)
            if "events_file" in copied:
                copied["events_file"] = path.with_suffix(".jsonl").name
            if events is not None:
                path.with_suffix(".jsonl").write_text("".join(json.dumps(event) + "\n" for event in events) + tail, encoding="utf-8")
            return copied, path

        def reject(name, record, events=None):
            copied, path = fixture(name, record, events)
            witnesses = export.common.Witnesses()
            try:
                export.retain_run(copied, path, witnesses)
            except ValueError as error:
                assert not witnesses.by_coefficients
                rejected.append({"case": name, "reason": str(error)})
            else:
                raise AssertionError(f"insufficient evidence accepted: {name}")

        complete, complete_events = original[100]
        failed, failed_events = original[104]
        assert complete["counts"]["completed_proposals"] == 32 and complete["valid_run"]
        assert failed["counts"]["proposals"] == 1 and not failed["valid_run"]
        reject("complete32_missing", complete)
        reject("complete32_empty", complete, [])
        reject("complete32_config_only", complete, complete_events[:1])
        cutoff = next(i for i, event in enumerate(complete_events) if event["kind"] == "commit" and event["proposal"] == 31)
        reject("complete32_truncated_after_commit31", complete, complete_events[:cutoff + 1])
        reject("failed_after_proposal_missing", failed)
        reject("failed_after_proposal_empty", failed, [])

        # A real observed DP prefix, synthetically stopped before its first raw
        # ticket: zero completed/whole proposals does not erase pending inputs.
        dp_record, dp_events = original[101]
        cutoff = next(i for i, event in enumerate(dp_events) if event["kind"] == "raw_attempt_intent")
        pending_events = dp_events[:cutoff + 1]
        _, pending_path = fixture("pending_dp_present", dp_record, pending_events)
        pending = live.frozen.summarize_events(pending_path.with_suffix(".jsonl"))
        pending.update(worker_failure=True, supervision={"killed_at_cap": False, "worker_returncode": 1,
                       "supervisor_elapsed_seconds": pending_events[-1]["elapsed"], "stderr": "synthetic prefix interruption"})
        pending.update(live.validity(pending))
        pending["first_target_hit_censored_at"] = pending["observed_run_seconds"]
        live.enrich(pending, pending_events)
        assert pending["counts"]["proposals"] == pending["counts"]["completed_proposals"] == 0
        assert pending["generation_counts"]["dp_attempts_unfinished"] == 1
        retained = export.retain_run(pending, pending_path, export.common.Witnesses())
        assert retained["generation_replay"]["pending_generation"]["observed_phase"] == "raw_selection_pending"
        accepted.append("failed_pending_dp_present")
        reject("failed_pending_dp_missing", pending)
        reject("failed_pending_dp_empty", pending, [])
        reject("failed_pending_dp_config_only", pending, pending_events[:1])

        # Exercise the actual runtime's OSError startup branch under a mocked
        # Popen; a real child is neither launched nor claimed to have failed.
        startup_path = directory / "startup_missing.json"
        startup = startup_failure_fixture(startup_path.with_suffix(""))
        for name, entries, tail in (("startup_missing", None, ""), ("startup_empty", [], ""),
                                     ("startup_incomplete_first_line", [], '{"kind":')):
            copied, path = fixture(name, startup, entries, tail)
            retained = export.retain_run(copied, path, export.common.Witnesses())
            assert not retained["valid_run"] and retained["termination_reason"] == "worker_failure"
            assert not retained["generation_trace"]["rows"] and not retained["evaluation_observations"]
            assert retained["generation_replay"]["requests_started"] == 0
            accepted.append(name)
        false_startup = copy.deepcopy(startup)
        false_startup["generation_counts"]["requests_started"] = 1
        reject("startup_marker_with_known_generation", false_startup)
        reject("startup_with_generation_but_no_config", startup, pending_events[-1:])

        # A hard kill need not leave a finish event or a complete final line.
        # An extra unparsed half-line does not remove any observed summary fact.
        deadline, deadline_events = original[102]
        assert deadline["termination_reason"] == "deadline" and not any(event["kind"] == "finish" for event in deadline_events)
        copied, path = fixture("deadline_partial_tail", deadline, deadline_events, '{"kind":"evaluation",')
        retained = export.retain_run(copied, path, export.common.Witnesses())
        assert retained["valid_run"] and retained["counts"] == deadline["counts"]
        assert retained["generation_replay"]["journalled_whole_proposals"] == deadline["generation_counts"]["journalled_whole_proposals"]
        accepted.append("deadline_partial_tail_without_finish")
    return {"existing_summaries_reconstructed_exactly": len(original), "rejected_insufficient_evidence": rejected,
            "accepted_evidence_cases": accepted, "original_history": "read only",
            "subprocesses_sampling_and_root_certifications": 0}


def actual_controls(label):
    if not label.startswith("control_"):
        raise ValueError("controls need a control_ label")
    plan = [("direct", 100, 32, False), ("dp_closure", 101, 32, False),
            ("direct", 102, 0, False), ("dp_closure", 103, 0, False), ("dp_closure", 104, 0, True)]
    paths, results = [], []
    for variant, seed, limit, failure in plan:
        record = live.run_once(variant, seed, 2, label, limit, failure_check=failure, raise_on_failure=False)
        paths.append(live.run_stem(label, 56, variant, seed).with_suffix(".json"))
        results.append({"variant": variant, "seed": seed, "valid_run": record["valid_run"],
                        "termination_reason": record["termination_reason"], "completed": record["counts"]["completed_proposals"],
                        "generation_counts": record["generation_counts"], "primitive_metrics": record["primitive_metrics"]})
    # Export/portable replay only: no new proposals or root calculations.
    comparison, witnesses = export.write_exports(label, live.OUTPUT / f"{label}_native_comparison.json",
        live.OUTPUT / f"{label}_native_witnesses.json", True, paths)
    assert comparison["retained_run_count"] == 5 and not comparison["complete_declared_primitive_comparison"]
    for result, (_, _, limit, failure) in zip(results, plan):
        if failure:
            assert not result["valid_run"] and result["termination_reason"] == "worker_failure" and result["completed"] == 0
        else:
            assert result["valid_run"]
            assert result["termination_reason"] in (("deadline", "proposal_limit") if limit else ("deadline",))
            assert result["completed"] <= limit if limit else True
    return {"runs": results, "subprocess_budget_ceiling_seconds": 10,
            "retained_witnesses": len(witnesses["witnesses"]), "portable_replay": "pass"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True)
    parser.add_argument("--actual-controls", action="store_true")
    parser.add_argument("--export-controls", help="existing control label; no sampling or roots")
    parser.add_argument("--compare-retention", nargs=2, metavar=("BEFORE", "AFTER"))
    parser.add_argument("--structure-controls", nargs=2, metavar=("CONTROL_LABEL", "NATIVE_COMPARISON"),
                        help="existing controls and explicit native comparison; exact factor-data check only")
    parser.add_argument("--evidence-controls", help="existing control label; missing/truncated journal fixtures, no children or roots")
    args = parser.parse_args()
    if not args.label.startswith("control_"):
        raise ValueError("checks require a control_ label")
    if sum(bool(mode) for mode in (args.actual_controls, args.export_controls, args.compare_retention, args.structure_controls, args.evidence_controls)) > 1:
        raise ValueError("select only one control mode; no implicit combined sampling")
    destination = live.OUTPUT / f"{args.label}_checks.json"
    if destination.exists():
        raise FileExistsError("preserve previous checks")
    result = {"protocol": live.PROTOCOL, "scope": "ordinary implementation checks, not formal comparison"}
    if args.compare_retention:
        if args.actual_controls or args.export_controls:
            raise ValueError("payload comparison is a separate read-only mode")
        result["retention_payload_comparison"] = compare_retention(*args.compare_retention)
    elif args.evidence_controls:
        result["journal_evidence_regression"] = evidence_controls(args.label, args.evidence_controls)
    else:
        result.update(mechanisms=mechanism_checks(), stopping_and_replay=stopping_and_replay_checks(), ledgers=ledger_checks())
    if args.actual_controls:
        result["actual_controls"] = actual_controls(args.label)
    if args.export_controls:
        result["retention_controls"] = export_controls(args.label, args.export_controls)
    if args.structure_controls:
        if args.actual_controls:
            raise ValueError("structure regression must not launch stochastic controls")
        result["structure_interface_regression"] = structure_controls(*args.structure_controls)
    live.OUTPUT.mkdir(parents=True, exist_ok=True)
    live.frozen.write_json(destination, result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
