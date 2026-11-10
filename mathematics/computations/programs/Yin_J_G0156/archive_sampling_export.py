"""Retain archive comparison observations and exact verification witnesses.

This uses the new 30 identities exclusively.  Deterministic generated template
arrays are represented by their exact core/degree/height recipe and counts;
observed template order, all committed archive changes, times, metrics, seed,
whole and separate factor witnesses remain native.  No sampling or roots run.
"""

import argparse
import copy
import json
from pathlib import Path

import archive_sampling as live
import prior_strength_live_export as common

EXTRA_COLLECTIONS = ("nonseed_discoveries", "unresolved_nonseed_equalities",
                     "strictly_below_seed_values", "whole_target_core_observations")


def compact_generated(item, degree, variant):
    result = copy.deepcopy(item)
    generated = result.pop("generated_templates", None)
    if generated is not None:
        result["generated_template_count"] = len(generated)
        result["generated_template_reproduction"] = {
            "source": "cyclotomic_closure.py:generate" if variant == "closure" else "archive_sampling.py:sparse_completions",
            "degree": degree, "height": 4,
            "input": "core_coefficients_ascending in this object",
            "order": "lexicographically sorted distinct free prefixes"}
    return result


def add_parent_costs(row, path):
    wanted = {item["proposal"] for item in row["factor_parent_outputs"]}
    if not wanted:
        return
    parents = {item["proposal"]: item for item in row["factor_parent_outputs"]}
    found = set()
    with path.with_suffix(".jsonl").open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                break
            if event["kind"] == "evaluation" and event["proposal"] in wanted:
                parents[event["proposal"]].update({
                    "cost_seconds": event["cost_seconds"], "cached": event["cached"],
                    "repeated_proposal": event["repeated_proposal"],
                    "all_parent_factor_associations": event["factor_discoveries"]})
                found.add(event["proposal"])
    assert found == wanted


def journal_events(path):
    with Path(path).open(encoding="utf-8") as stream:
        for line in stream:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                break


def retain_failure_inputs(events, budget):
    """Keep exact retry inputs without inventing certificates or yield credit."""
    unresolved, incomplete = [], []
    proposal = evaluation = None

    def retain(committed, elapsed=None):
        if proposal is None:
            return
        reasons = []
        if evaluation:
            if "unresolved_error" in evaluation:
                reasons.append("unresolved_error")
            if evaluation.get("ranking_resolved") is False:
                reasons.append("unresolved_ranking")
            reasons.extend("unresolved_threshold_" + key for key, value in evaluation.get("thresholds", {}).items()
                           if value == "unresolved")
        if not committed:
            reasons.append("no_predeadline_commit")
        if not reasons:
            return
        prefix = proposal["free_coefficients"]
        item = {"proposal": proposal["proposal"], "proposal_elapsed": proposal["elapsed"],
                "free_coefficients": prefix, "coefficients_ascending": live.frozen.reciprocal_polynomial(prefix),
                "committed": committed, "commit_elapsed": elapsed, "evaluation_present": evaluation is not None,
                "reasons": reasons,
                "yield_scope": "retry input only; no additional discovery credit; uncommitted work is excluded, committed threshold statuses retain their original scope"}
        if evaluation:
            fields = ("unresolved_error", "ranking_resolved", "thresholds", "neutral", "core_coefficients_ascending",
                      "cached", "repeated_proposal", "cost_seconds")
            item["evaluation_observations"] = {key: copy.deepcopy(evaluation[key]) for key in fields if key in evaluation}
            item["uncommitted_archive_update_present"] = not committed and evaluation.get("archive_update") is not None
            if "certificate" in evaluation:
                item["certificate"] = common.compact_whole(evaluation["certificate"])
                assert item["certificate"]["coefficients_ascending"] == item["coefficients_ascending"]
            else:
                item["certificate_scope"] = "no full certificate retained by the frozen worker for this event"
        (unresolved if committed else incomplete).append(item)

    for event in events:
        kind = event["kind"]
        if kind == "proposal":
            if proposal is not None:
                retain(False)
            proposal, evaluation = event, None
        elif kind == "evaluation":
            assert proposal is not None and event["proposal"] == proposal["proposal"]
            evaluation = event
        elif kind == "commit":
            assert proposal is not None and evaluation is not None and event["proposal"] == proposal["proposal"]
            retain(event["elapsed"] <= budget, event["elapsed"])
            proposal = evaluation = None
    if proposal is not None:
        retain(False)
    return {"committed_unresolved_inputs": unresolved, "incomplete_proposal_inputs": incomplete}


def build_exports(label, allow_partial=False, paths=None):
    # Explicit paths are for labelled implementation controls only; formal
    # exports always enumerate archive_sampling.run_paths, never old pilot paths.
    if paths is not None and not label.startswith("control_"):
        raise ValueError("explicit control paths require a control_ label")
    paths = live.run_paths(label) if paths is None else list(map(Path, paths))
    if not paths:
        raise ValueError("no archive comparison summaries found")
    if len(paths) != 30 and not allow_partial:
        raise ValueError("all 30 identities required unless --allow-partial is explicit")
    comparison = live.report(label, paths)
    indexed = {}
    for path in paths:
        record = common.read_json(path)
        config = record["configuration"]
        key = (config["degree"], config["variant"], config["seed"])
        assert config["protocol"] == live.PROTOCOL and key not in indexed
        indexed[key] = (record, path)
    witnesses = common.Witnesses()
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            record, path = indexed[(row["degree"], row["arm"], row["seed"])]
            common.retain_run(row, record, path, witnesses)
            add_parent_costs(row, path)
            row.update(retain_failure_inputs(journal_events(path.with_suffix(".jsonl")), row["configuration"]["seconds"]))
    # Check the established whole/factor export contract before adding extra
    # archive-specific witness roles that its frozen validator does not know.
    document = {"protocol": live.PROTOCOL, "source_label": label,
                "purpose": "exact certificate replay; supplied seed is not a discovery",
                "witnesses": list(witnesses.by_coefficients.values())}
    common.validate_references(comparison, document)
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            _, path = indexed[(row["degree"], row["arm"], row["seed"])]
            run = path.stem
            initial = row["archive_initialization"]
            if initial:
                cert = initial["seed_certificate"]
                initial["seed_certificate"] = common.compact_whole(cert)
                initial["seed_witness_id"] = witnesses.add(cert["coefficients_ascending"], "supplied_seed_not_discovery", run)
                if initial["initial_archive"]:
                    initial["initial_archive"] = compact_generated(initial["initial_archive"], row["degree"], row["arm"])
            row["final_archive"] = [compact_generated(item, row["degree"], row["arm"]) for item in row["final_archive"]]
            for state in row["final_archive"]:
                state["observed_template_witness_ids"] = [
                    witnesses.add(live.frozen.reciprocal_polynomial(prefix), "observed_archive_whole_target", run)
                    for prefix in state["observed_templates"]]
            for change in row["committed_archive_changes"]:
                if change["new_core"]:
                    change["new_core"] = compact_generated(change["new_core"], row["degree"], row["arm"])
            for field in EXTRA_COLLECTIONS:
                for item in row[field]:
                    certificate = item["certificate"]
                    item["certificate"] = common.compact_whole(certificate)
                    item["witness_id"] = witnesses.add(certificate["coefficients_ascending"], field, run)
    document["witnesses"] = list(witnesses.by_coefficients.values())
    comparison["retained_run_count"] = len(paths)
    comparison["retention_role"] = (
        "Observed 30-identity protocol, raw count/time/config/supervision, whole/best/unresolved and nonseed outcomes, "
        "all committed archive changes and observed templates, separate factors with complete parent associations "
        "and charged stage costs. Exact unresolved and uncommitted retry inputs stay outside the certified witness list. "
        "Generated templates are reproducible exact recipes, not stored prior training. "
        "Incomplete or failed controls stay incomplete or failed. No literature-new claim.")
    validate_references(comparison, document)
    return comparison, document


def validate_references(comparison, document):
    entries = document["witnesses"]
    by_id = {item["witness_id"]: item["coefficients_ascending"] for item in entries}
    assert len(by_id) == len(entries) == len({tuple(item["coefficients_ascending"]) for item in entries})
    used = set()
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            whole = row["whole_discoveries"] + row["unresolved_value_equalities"] + row["factor_parent_outputs"]
            for field in EXTRA_COLLECTIONS:
                whole += row[field]
            if row["best_certified_positive"]:
                whole.append(row["best_certified_positive"])
            for item in whole:
                assert by_id[item["witness_id"]] == item["certificate"]["coefficients_ascending"]
                used.add(item["witness_id"])
            initial = row["archive_initialization"]
            if initial:
                assert by_id[initial["seed_witness_id"]] == list(live.SEED_CORE)
                assert initial["seed_certificate"]["coefficients_ascending"] == list(live.SEED_CORE)
                used.add(initial["seed_witness_id"])
            for state in row["final_archive"]:
                assert len(state["observed_templates"]) == len(state["observed_template_witness_ids"])
                for prefix, witness_id in zip(state["observed_templates"], state["observed_template_witness_ids"]):
                    assert by_id[witness_id] == live.frozen.reciprocal_polynomial(prefix)
                    used.add(witness_id)
            parents = {item["proposal"]: item for item in row["factor_parent_outputs"]}
            for field, _ in common.FACTOR_COLLECTIONS:
                for item in row[field]:
                    assert by_id[item["factor_witness_id"]] == item["coefficients_ascending"]
                    parent = parents[item["proposal"]]
                    assert item["parent_witness_id"] == parent["witness_id"] and "cost_seconds" in parent
                    used.add(item["factor_witness_id"])
    assert used == set(by_id)


def replay_retained_run(row):
    """Portable RNG/archive reconstruction from compact native inputs only.

    This reconstructs every journalled proposal and the committed archive, but
    does not redo timing, root certificates or outcomes for other proposals.
    """
    config = row["configuration"]
    law = live.ArchiveLaw(config["degree"], config["variant"], config["seed"])
    # The frozen count includes only proposals whose journalled elapsed time
    # is <= budget.  A final draw can start before the cap but finish journalling
    # after it; its exact input is still retained and must also be replayed.
    retry_inputs = {}
    for field in ("committed_unresolved_inputs", "incomplete_proposal_inputs"):
        for item in row[field]:
            proposal = item["proposal"]
            assert type(proposal) is int and proposal > 0 and proposal not in retry_inputs
            assert item["coefficients_ascending"] == live.frozen.reciprocal_polynomial(item["free_coefficients"])
            retry_inputs[proposal] = item
    within_budget_proposals = row["counts"]["proposals"]
    last_proposal = max([within_budget_proposals, *retry_inputs])
    if not row["archive_initialization_committed"]:
        assert last_proposal == 0 and row["counts"]["completed_proposals"] == 0 and not row["final_archive"]
        return {"initialized": False, "proposals": 0, "within_budget_proposals": 0,
                "checked_retry_inputs": 0, "changes": 0}
    initialized = law.initialize()
    if initialized:
        retained = row["archive_initialization"]["initial_archive"]
        assert compact_generated(initialized, config["degree"], config["variant"]) == retained
    changes = {change["proposal"]: change for change in row["committed_archive_changes"]}
    assert len(changes) == len(row["committed_archive_changes"])
    for proposal in range(1, last_proposal + 1):
        prefix = law.draw()
        if proposal in retry_inputs:
            assert prefix == retry_inputs[proposal]["free_coefficients"], "retained retry prefix differs from RNG replay"
        if proposal in changes:
            change = changes[proposal]
            assert prefix == change["observed_free_coefficients"]
            update = law.observe_target(change["core_coefficients_ascending"], prefix)
            if update["new_core"]:
                update["new_core"] = compact_generated(update["new_core"], config["degree"], config["variant"])
            assert update == {key: value for key, value in change.items() if key not in ("proposal", "elapsed", "cost_seconds")}
    for state, (core, reconstructed) in zip(row["final_archive"], law.cores.items()):
        assert state["core_coefficients_ascending"] == list(core)
        assert set(map(tuple, state["observed_templates"])) == reconstructed["observed"]
        assert all(state[key] == value for key, value in law.counts(core).items())
    assert len(row["final_archive"]) == len(law.cores)
    return {"initialized": True, "proposals": last_proposal, "within_budget_proposals": within_budget_proposals,
            "checked_retry_inputs": len(retry_inputs), "changes": len(changes)}


def after_cap_proposal_check(row):
    """Move only a retained final proposal timestamp past cap, as a fixture."""
    fixture = copy.deepcopy(row)
    unfinished = fixture["incomplete_proposal_inputs"]
    assert len(unfinished) == 1
    final = unfinished[0]
    assert not final["committed"] and final["proposal"] == fixture["counts"]["proposals"]
    assert final["proposal"] == fixture["counts"]["completed_proposals"] + 1
    final["proposal_elapsed"] = fixture["configuration"]["seconds"] + 0.000001
    # Exactly the frozen summarizer's boundary: omit this proposal from its
    # elapsed<=budget count, while preserving its already journalled input.
    fixture["counts"]["proposals"] -= 1
    fixture["counts"]["incomplete_proposals"] -= 1
    replay = replay_retained_run(fixture)
    assert replay["proposals"] == final["proposal"]
    assert replay["within_budget_proposals"] == final["proposal"] - 1
    assert replay["checked_retry_inputs"] >= 1
    assert fixture["archive_metrics"] == row["archive_metrics"]
    assert fixture["final_archive"] == row["final_archive"]
    # Merely increasing the loop bound is insufficient: the retained endpoint
    # must be checked against the generated draw, including the after-cap item.
    altered = copy.deepcopy(fixture)
    target = altered["incomplete_proposal_inputs"][0]
    target["free_coefficients"][0] += -1 if target["free_coefficients"][0] == 4 else 1
    target["coefficients_ascending"] = live.frozen.reciprocal_polynomial(target["free_coefficients"])
    try:
        replay_retained_run(altered)
    except AssertionError as error:
        assert str(error) == "retained retry prefix differs from RNG replay"
    else:
        raise AssertionError("after-cap retained prefix was not checked")
    return {"fixture_scope": "synthetic timestamp/count boundary; no new sampling or yield",
            **replay, "after_cap_proposal": final["proposal"],
            "after_cap_elapsed": final["proposal_elapsed"], "altered_prefix_rejected": True}


def write_exports(label, comparison_path, witnesses_path, allow_partial=False, paths=None):
    comparison_path, witnesses_path = Path(comparison_path), Path(witnesses_path)
    if comparison_path.resolve() == witnesses_path.resolve():
        raise ValueError("destinations must differ")
    if comparison_path.exists() or witnesses_path.exists():
        raise FileExistsError("preserve existing native input; choose fresh destinations")
    comparison, witnesses = build_exports(label, allow_partial, paths)
    payloads = [(comparison_path, json.dumps(comparison, indent=2) + "\n"),
                (witnesses_path, json.dumps(witnesses, indent=2) + "\n")]
    for path, payload in payloads:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload, encoding="utf-8")
    return comparison, witnesses


def self_test(label, control_label):
    if not label.startswith("control_") or not control_label.startswith("control_"):
        raise ValueError("self-test labels must start control_")
    failure_fixture = failure_input_check()
    results, after_cap_fixture = [], None
    collections = [
        ("proposals", control_label, [live.run_stem(control_label, degree, variant, 100 + index).with_suffix(".json")
                                     for degree in live.DEGREES for index, variant in enumerate(live.VARIANTS)]),
        ("deadline", control_label + "_deadline", [live.run_stem(control_label + "_deadline", 30, "closure", 103).with_suffix(".json")]),
        ("failure", control_label + "_failure", [live.run_stem(control_label + "_failure", 24, "direct", 104).with_suffix(".json")])]
    for role, source_label, paths in collections:
        destination = live.OUTPUT / f"{label}_{role}"
        try:
            build_exports(source_label, paths=paths)
            raise AssertionError("partial export unexpectedly accepted")
        except ValueError as error:
            assert "30 identities" in str(error)
        comparison, witnesses = write_exports(source_label, destination.with_suffix(".json"),
                                               destination.with_name(destination.name + "_witnesses").with_suffix(".json"),
                                               True, paths)
        assert comparison["retained_run_count"] == len(paths) and not comparison["allocation_screen_passes"]
        for group in comparison["groups"]:
            for row in group["all_seed_outcomes"]:
                assert not row["eligible_archive_comparison_run"]
                assert row["archive_metrics"]["distinct_nonseed_target_values"] == 0
                if role == "failure":
                    assert not row["valid_run"] and row["termination_reason"] == "worker_failure"
                    assert len(row["incomplete_proposal_inputs"]) == 1
                    assert not row["incomplete_proposal_inputs"][0]["evaluation_present"]
                if role == "deadline":
                    assert len(row["incomplete_proposal_inputs"]) == row["counts"]["incomplete_proposals"]
                    after_cap_fixture = after_cap_proposal_check(row)
                for state in row["final_archive"]:
                    assert "generated_templates" not in state and "generated_template_reproduction" in state
                replay_retained_run(row)
        results.append({"role": role, "retained_runs": len(paths), "witnesses": len(witnesses["witnesses"]),
                        "factor_parents": sum(len(row["factor_parent_outputs"]) for group in comparison["groups"] for row in group["all_seed_outcomes"])})
        try:
            write_exports(source_label, destination.with_suffix(".json"), destination.with_suffix(".unused"), True, paths)
            raise AssertionError("overwrite unexpectedly accepted")
        except FileExistsError:
            pass
    return {"protocol": live.PROTOCOL, "controls": results, "no_roots_or_sampling": True,
            "partial_and_overwrite_guards": "pass", "synthetic_failure_input_checks": failure_fixture,
            "after_cap_proposal_replay": after_cap_fixture}


def failure_input_check():
    """Mechanical stream fixtures only: no evaluation or invented discovery."""
    prefix = [0] * 12
    certificate = {"coefficients_ascending": live.frozen.reciprocal_polynomial(prefix),
                   "core_coefficients_ascending": [1], "measure_interval": [[1, 0], [1, 0]],
                   "measure_ball": "1", "thresholds": {"6/5": "unresolved"}, "neutral": False}
    proposals = [{"kind": "proposal", "proposal": i, "free_coefficients": prefix, "elapsed": i / 10}
                 for i in range(1, 5)]
    events = [proposals[0], {"kind": "evaluation", "proposal": 1, "unresolved_error": "synthetic arithmetic failure"},
              {"kind": "commit", "proposal": 1, "elapsed": 0.11},
              proposals[1], {"kind": "evaluation", "proposal": 2, "ranking_resolved": False,
                             "thresholds": {"6/5": "unresolved"}, "certificate": certificate},
              {"kind": "commit", "proposal": 2, "elapsed": 0.21},
              proposals[2], {"kind": "evaluation", "proposal": 3, "certificate": certificate,
                             "archive_update": {"synthetic_uncommitted": True}}]
    retained = retain_failure_inputs(events, 2)
    assert len(retained["committed_unresolved_inputs"]) == 2 and len(retained["incomplete_proposal_inputs"]) == 1
    error, ranking = retained["committed_unresolved_inputs"]
    assert error["evaluation_observations"]["unresolved_error"] == "synthetic arithmetic failure"
    assert error["coefficients_ascending"] == certificate["coefficients_ascending"] and "certificate" not in error
    assert ranking["reasons"] == ["unresolved_ranking", "unresolved_threshold_6/5"]
    assert ranking["certificate"]["measure_interval"] == certificate["measure_interval"]
    unfinished = retained["incomplete_proposal_inputs"][0]
    assert unfinished["evaluation_present"] and unfinished["uncommitted_archive_update_present"]
    assert not unfinished["committed"] and unfinished["certificate"] == certificate
    no_evaluation = retain_failure_inputs([proposals[3]], 2)["incomplete_proposal_inputs"][0]
    assert not no_evaluation["evaluation_present"] and not no_evaluation["committed"]
    late = retain_failure_inputs(events + [{"kind": "commit", "proposal": 3, "elapsed": 2.01}], 2)
    assert len(late["committed_unresolved_inputs"]) == 2 and not late["incomplete_proposal_inputs"][0]["committed"]
    return {"error_exact_input": True, "ranking_and_threshold_with_interval": True,
            "uncommitted_with_and_without_evaluation": True, "postdeadline_commit_excluded": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export")
    export.add_argument("--label", required=True)
    export.add_argument("--allow-partial", action="store_true")
    export.add_argument("--comparison", type=Path, default=live.HERE / "inputs" / "archive_comparison.json")
    export.add_argument("--witnesses", type=Path, default=live.HERE / "inputs" / "archive_witnesses.json")
    check = commands.add_parser("self-test")
    check.add_argument("--label", required=True)
    check.add_argument("--control-label", required=True)
    commands.add_parser("replay-retained").add_argument("comparison", type=Path)
    args = parser.parse_args()
    if args.command == "self-test":
        print(json.dumps(self_test(args.label, args.control_label), indent=2))
    elif args.command == "replay-retained":
        comparison = common.read_json(args.comparison)
        assert comparison["protocol"] == live.PROTOCOL
        print(json.dumps([replay_retained_run(row) for group in comparison["groups"] for row in group["all_seed_outcomes"]], indent=2))
    else:
        comparison, witnesses = write_exports(args.label, args.comparison, args.witnesses, args.allow_partial)
        print(json.dumps({"retained_runs": comparison["retained_run_count"], "witnesses": len(witnesses["witnesses"])}))


if __name__ == "__main__":
    main()
