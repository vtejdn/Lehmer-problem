"""Bounded native checks of the separate live control; never run its 15-run schedule."""

import argparse
import copy
from fractions import Fraction as F
import json
from pathlib import Path

import prior_strength_control as exact
import prior_strength_live as live


def probabilities(law):
    return tuple(tuple(F(weight, sum(block["weights"])) for weight in block["weights"]) for block in law.blocks)


def check_allocation_screen():
    """Synthetic in-memory metric cases, never saved as experimental runs."""
    runs = [{"arm": variant, "seed": seed, "eligible_live_comparison_run": True,
             "distinct_whole_values": {"6/5": 1}, "first_target_hit_seconds": 2 if variant == "A" else 3}
            for seed in live.SEEDS for variant in live.VARIANTS]
    result = live.allocation_screen(runs)
    assert result["complete_declared_live_control"] and result["allocation_screen_passes"]
    assert result["A_nonlosses_to_fixed"] == result["A_improvements_on_O"] == 5
    four = copy.deepcopy(runs)
    next(row for row in four if row["arm"] == "A" and row["seed"] == 9)["first_target_hit_seconds"] = 3
    assert live.allocation_screen(four)["A_improvements_on_O"] == 4
    assert live.allocation_screen(four)["allocation_screen_passes"]
    tie = copy.deepcopy(runs)
    for row in tie:
        if row["arm"] == "A" and row["seed"] >= 8:
            row["first_target_hit_seconds"] = 3
    assert live.allocation_screen(tie)["A_improvements_on_O"] == 3
    assert not live.allocation_screen(tie)["allocation_screen_passes"]
    zeros = copy.deepcopy(runs)
    for row in zeros:
        row["distinct_whole_values"]["6/5"] = 0
        row["first_target_hit_seconds"] = None
    assert live.allocation_screen(zeros)["A_improvements_on_O"] == 0
    assert not live.allocation_screen(zeros)["allocation_screen_passes"]
    count_gain = copy.deepcopy(runs)
    for row in count_gain:
        if row["arm"] == "O":
            row["distinct_whole_values"]["6/5"] = 0
            row["first_target_hit_seconds"] = None
    assert live.allocation_screen(count_gain)["A_improvements_on_O"] == 5
    losses = copy.deepcopy(runs)
    for row in losses:
        if row["arm"] == "A" and row["seed"] >= 8:
            row["distinct_whole_values"]["6/5"] = 0
            row["first_target_hit_seconds"] = None
    assert live.allocation_screen(losses)["A_nonlosses_to_fixed"] == 3
    assert not live.allocation_screen(losses)["allocation_screen_passes"]
    failed = copy.deepcopy(runs)
    failed[-1]["eligible_live_comparison_run"] = False
    assert live.allocation_screen(failed)["A_improvements_on_O"] == 4
    assert not live.allocation_screen(failed)["allocation_screen_passes"]
    assert not live.allocation_screen(runs[:-1])["complete_declared_live_control"]
    duplicate = copy.deepcopy(runs)
    duplicate[-1] = duplicate[0]
    assert not live.allocation_screen(duplicate)["complete_declared_live_control"]
    return True


def replay_dispatched_journal(path):
    """Check every actual child proposal, including proposal 257 after an update."""
    events = live.frozen.read_events(path)
    config = next(event for event in events if event["kind"] == "config")
    variant = config["variant"]
    law = live.law_class(variant)(7, live.base_arm(variant), config["seed"])
    selected_law = live.OriginalLaw(7, "adaptive", config["seed"])
    assert config["law_class"] == type(law).__name__
    assert config["implementation_arm"] == live.base_arm(variant)
    expected_probabilities = exact.initial_law()
    proposal = evaluation = None
    batch, checked, updates, proposals = [], 0, 0, []
    for event in events:
        if event["kind"] == "proposal":
            proposal = event
            drawn = law.draw()
            assert drawn == proposal["free_coefficients"]
            proposals.append(drawn)
        elif event["kind"] == "evaluation":
            evaluation = event
        elif event["kind"] == "commit" and event["elapsed"] <= config["seconds"]:
            assert proposal["proposal"] == evaluation["proposal"] == event["proposal"]
            checked += 1
            if not evaluation.get("unresolved_error") and evaluation["ranking_resolved"] and not evaluation["neutral"]:
                batch.append((tuple(evaluation["core_coefficients_ascending"]), evaluation["log_score"], proposal["free_coefficients"]))
            if event["proposal"] % 256 == 0:
                result = law.update(batch)
                assert result == evaluation["update"]
                if variant != "fixed":
                    # The selected elites must also equal the unchanged selector.
                    original_selection = selected_law.update(batch)
                    assert original_selection == result
                    expected_probabilities = exact.update_law(expected_probabilities, result["elite_free_coefficients"], variant)
                    assert probabilities(law) == expected_probabilities
                updates += variant != "fixed"
                batch.clear()
    return {"checked_proposals": checked, "checked_updates": updates,
            "last_proposal": proposals[-1], "first_256_proposals": proposals[:256]}


def checks(label):
    assert check_allocation_screen()
    data = exact.read_json(exact.DEFAULT_INPUT)
    alternative = live.UnitPairPriorLaw(7, "adaptive", 0)
    expected = exact.initial_law()
    for batch in data["batches"]:
        elite = batch["elite_free_coefficients"]
        alternative.apply_elites(elite)
        expected = exact.update_law(expected, elite, "A")
        assert probabilities(alternative) == expected
    assert live.law_class("O") is live.OriginalLaw and live.law_class("fixed") is live.OriginalLaw
    assert alternative.update([])["elite_count"] == 0 and probabilities(alternative) == expected

    controls, replays = [], {}
    for variant in live.VARIANTS:
        record = live.run_once(variant, 5, 10, label + "_257", max_proposals=257)
        assert record["valid_run"] and record["termination_reason"] == "proposal_limit"
        assert record["counts"]["completed_proposals"] == 257
        assert not record["eligible_live_comparison_run"]
        replay = replay_dispatched_journal(live.run_stem(label + "_257", variant, 5).with_suffix(".jsonl"))
        assert replay["checked_proposals"] == 257
        replays[variant] = replay
        controls.append({"variant": variant, "termination_reason": record["termination_reason"],
                         "checked_proposals": replay["checked_proposals"], "checked_updates": replay["checked_updates"]})
    assert replays["O"]["first_256_proposals"] == replays["A"]["first_256_proposals"]
    assert replays["O"]["last_proposal"] != replays["A"]["last_proposal"]
    partial = live.report(label + "_257")
    assert not partial["complete_declared_live_control"] and not partial["allocation_screen_passes"]
    assert all(group["distinct_value_statistics"]["6/5"] is None for group in partial["groups"])

    deadline = live.run_once("A", 6, 0.75, label + "_deadline")
    assert deadline["valid_run"] and deadline["termination_reason"] == "deadline"
    assert deadline["last_committed_elapsed"] <= 0.75 and not deadline["eligible_live_comparison_run"]
    failed = live.run_once("O", 7, 2, label + "_failure", failure_check=True, raise_on_failure=False)
    assert not failed["valid_run"] and failed["termination_reason"] == "worker_failure"
    assert failed["counts"]["proposals"] == 1 and failed["counts"]["completed_proposals"] == 0
    assert failed["first_target_hit_censored_at"] == failed["observed_run_seconds"] < 2
    failed_report = live.report(label + "_failure")
    assert not failed_report["complete_declared_live_control"] and not failed_report["allocation_screen_passes"]
    assert len(failed_report["invalid_or_ineligible_runs"]) == 1

    result = {"passed": True, "scope": "implementation controls only; no formal live comparison executed",
              "exact_fixed_elite_A_snapshots_checked": 13, "controls_257": controls,
              "O_and_A_first_256_identical": True, "O_and_A_proposal_257_differ": True,
              "proposal_257": {variant: replay["last_proposal"] for variant, replay in replays.items()},
              "deadline_control": {"cap": 0.75, "last_committed_elapsed": deadline["last_committed_elapsed"],
                                   "counts": deadline["counts"]},
              "failure_control": {"reason": failed["termination_reason"], "observed_seconds": failed["observed_run_seconds"],
                                  "censor_seconds": failed["first_target_hit_censored_at"]},
              "partial_and_failed_runs_cannot_pass_screen": True}
    result["allocation_screen_boundary_cases"] = True
    live.frozen.write_json(live.OUTPUT / f"{label}_checks.json", result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True)
    parser.add_argument("--screen-only", action="store_true")
    args = parser.parse_args()
    if args.screen_only:
        assert check_allocation_screen()
        partial = live.report(args.label + "_257")
        failed = live.report(args.label + "_failure")
        assert not partial["complete_declared_live_control"] and not partial["allocation_screen_passes"]
        assert not failed["complete_declared_live_control"] and not failed["allocation_screen_passes"]
        print(json.dumps({"screen_boundary_cases": "passed", "existing_partial_and_failure_reports": "excluded"}))
        return
    result = checks(args.label)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
