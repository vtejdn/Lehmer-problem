"""Bounded degree/seed/dispatch and screen checks; never run the 20-run schedule."""

import argparse
from collections import Counter
import copy
from fractions import Fraction as F
import json
from math import prod

import degree_validation as validation


def probabilities(law):
    return tuple(tuple(F(weight, sum(block["weights"])) for weight in block["weights"]) for block in law.blocks)


def initial_probabilities(blocks):
    return tuple(tuple(prod(F(2**(4-abs(k)), 46) for k in state) for state in block["states"]) for block in blocks)


def fraction_update(previous, blocks, elite):
    if not elite:
        return previous
    result = []
    for old, block in zip(previous, blocks):
        start, width = block["start"], block["width"]
        counts = Counter(tuple(vector[start:start+width]) for vector in elite)
        prior_per_state = F(1, 81) if width == 2 else F(1)
        prior_total = 1 if width == 2 else 9
        result.append(tuple(F(4, 5)*value + F(1, 5)*(counts[state]+prior_per_state)/(len(elite)+prior_total)
                            for state, value in zip(block["states"], old)))
    return tuple(result)


def check_block_arithmetic():
    records = []
    for degree in validation.DEGREES:
        half = degree // 2
        law = validation.prior.UnitPairPriorLaw(half, "adaptive", 10)
        widths = [block["width"] for block in law.blocks]
        assert widths == ([2, 2, 2, 2, 1] if degree == 18 else [2, 2, 2, 2, 2])
        assert [len(block["states"]) for block in law.blocks] == [9**width for width in widths]
        expected = initial_probabilities(law.blocks)
        assert probabilities(law) == expected
        synthetic = [[(i % 9)-4, (i // 9)-1] + [0]*(half-2) for i in range(26)]
        for elite in ([], [[4]*half], synthetic):
            law.apply_elites(elite)
            expected = fraction_update(expected, law.blocks, elite)
            assert probabilities(law) == expected
            assert all(sum(block) == 1 and all(value > 0 for value in block) for block in expected)
        records.append({"degree": degree, "block_widths": widths, "exact_fraction_updates": True})
    return records


def check_screen():
    """Synthetic metric cases remain in memory and are not experimental outcomes."""
    runs = [{"degree": degree, "arm": variant, "seed": seed, "eligible_degree_validation_run": True,
             "distinct_whole_values": {"6/5": 1}, "first_target_hit_seconds": 2 if variant == "A" else 3}
            for degree in validation.DEGREES for seed in validation.SEEDS for variant in validation.VARIANTS]
    assert validation.allocation_screen(runs)["allocation_screen_passes"]
    boundary = copy.deepcopy(runs)
    for row in boundary:
        if row["arm"] == "A" and (row["degree"] == 20 or row["seed"] == 14):
            row["first_target_hit_seconds"] = 3
    result = validation.allocation_screen(boundary)
    assert [row["A_improvements_on_fixed"] for row in result["degree_screens"]] == [4, 0]
    assert result["allocation_screen_passes"]
    insufficient = copy.deepcopy(boundary)
    next(row for row in insufficient if (row["degree"],row["arm"],row["seed"]) == (18,"A",13))["first_target_hit_seconds"] = 3
    assert not validation.allocation_screen(insufficient)["allocation_screen_passes"]
    losses = copy.deepcopy(runs)
    for row in losses:
        if row["degree"] == 20 and row["arm"] == "A" and row["seed"] >= 13:
            row["distinct_whole_values"]["6/5"] = 0
            row["first_target_hit_seconds"] = None
    result = validation.allocation_screen(losses)
    assert result["degree_screens"][1]["A_nonlosses_to_fixed"] == 3 and not result["allocation_screen_passes"]
    zeros = copy.deepcopy(runs)
    for row in zeros:
        row["distinct_whole_values"]["6/5"] = 0
        row["first_target_hit_seconds"] = None
    result = validation.allocation_screen(zeros)
    assert not result["allocation_screen_passes"] and all(row["A_improvements_on_fixed"] == 0 for row in result["degree_screens"])
    count_gain = copy.deepcopy(boundary)
    for row in count_gain:
        if row["degree"] == 18 and row["arm"] == "fixed":
            row["distinct_whole_values"]["6/5"] = 0
            row["first_target_hit_seconds"] = None
    assert validation.allocation_screen(count_gain)["allocation_screen_passes"]
    invalid = copy.deepcopy(runs)
    invalid[-1]["eligible_degree_validation_run"] = False
    assert not validation.allocation_screen(invalid)["allocation_screen_passes"]
    assert not validation.allocation_screen(runs[:-1])["complete_declared_degree_validation"]
    duplicate = copy.deepcopy(runs)
    duplicate[-1] = duplicate[0]
    assert not validation.allocation_screen(duplicate)["complete_declared_degree_validation"]
    foreign = copy.deepcopy(runs)
    foreign[-1]["seed"] = 9
    assert not validation.allocation_screen(foreign)["complete_declared_degree_validation"]
    schedule = validation.schedule()
    assert len(schedule) == len(set(schedule)) == 20
    assert all(degree == 18 for degree, _, _ in schedule[:10]) and all(degree == 20 for degree, _, _ in schedule[10:])
    assert schedule[:4] == [(18,"fixed",10),(18,"A",10),(18,"A",11),(18,"fixed",11)]
    assert schedule[10:14] == [(20,"A",10),(20,"fixed",10),(20,"fixed",11),(20,"A",11)]
    return True


def replay_child(path, degree, variant):
    events = validation.runtime.frozen.read_events(path)
    config = next(event for event in events if event["kind"] == "config")
    assert (config["protocol"],config["degree"],config["variant"],config["seed"]) == (validation.PROTOCOL,degree,variant,10)
    assert config["adaptive_block_widths"] == validation.configuration(degree,variant,10)["adaptive_block_widths"]
    law = validation.prior.law_class(variant)(degree//2, validation.prior.base_arm(variant), 10)
    selector = validation.prior.OriginalLaw(degree//2, "adaptive", 10)
    expected = initial_probabilities(law.blocks)
    proposal = evaluation = None
    batch, completed, certificates, updates = [], 0, 0, 0
    for event in events:
        if event["kind"] == "proposal":
            proposal = event
            assert len(event["free_coefficients"]) == degree//2
            assert law.draw() == event["free_coefficients"]
        elif event["kind"] == "evaluation":
            evaluation = event
            if "certificate" in event:
                certificate = event["certificate"]
                assert len(certificate["coefficients_ascending"]) == degree+1
                assert certificate["root_count_with_multiplicity"] == degree
                assert certificate["coefficients_ascending"] == validation.runtime.frozen.reciprocal_polynomial(proposal["free_coefficients"])
                certificates += 1
        elif event["kind"] == "commit" and event["elapsed"] <= config["seconds"]:
            assert event["proposal"] == evaluation["proposal"] == proposal["proposal"]
            completed += 1
            if not evaluation.get("unresolved_error") and evaluation["ranking_resolved"] and not evaluation["neutral"]:
                batch.append((tuple(evaluation["core_coefficients_ascending"]),evaluation["log_score"],proposal["free_coefficients"]))
            if event["proposal"] % 256 == 0:
                update = law.update(batch)
                assert update == evaluation["update"]
                if variant == "A":
                    assert selector.update(batch) == update
                    expected = fraction_update(expected, law.blocks, update["elite_free_coefficients"])
                    assert probabilities(law) == expected
                    updates += 1
                batch.clear()
    assert completed == 257 and certificates > 0
    return {"degree":degree,"variant":variant,"seed":10,"replayed_proposals":completed,
            "full_degree_certificates_checked":certificates,"exact_updates_checked":updates}


def checks(label):
    block_checks = check_block_arithmetic()
    assert check_screen()
    controls = []
    for degree in validation.DEGREES:
        for variant in validation.VARIANTS:
            record = validation.run_once(degree,variant,10,10,label+"_257",max_proposals=257)
            assert record["valid_run"] and record["termination_reason"] == "proposal_limit"
            assert not record["eligible_degree_validation_run"]
            controls.append(replay_child(validation.run_stem(label+"_257",degree,variant,10).with_suffix(".jsonl"),degree,variant))
    partial = validation.report(label+"_257")
    assert not partial["complete_declared_degree_validation"] and not partial["allocation_screen_passes"]
    assert not validation.prior.run_paths(label+"_257")
    deadline = validation.run_once(20,"A",12,0.75,label+"_deadline")
    assert deadline["valid_run"] and deadline["termination_reason"] == "deadline"
    assert deadline["last_committed_elapsed"] <= 0.75 and not deadline["eligible_degree_validation_run"]
    failure = validation.run_once(18,"fixed",11,2,label+"_failure",failure_check=True,raise_on_failure=False)
    assert not failure["valid_run"] and failure["termination_reason"] == "worker_failure"
    assert failure["counts"]["proposals"] == 1 and failure["counts"]["completed_proposals"] == 0
    assert failure["first_target_hit_censored_at"] == failure["observed_run_seconds"] < 2
    failed_report = validation.report(label+"_failure")
    assert not failed_report["allocation_screen_passes"] and len(failed_report["invalid_or_ineligible_runs"]) == 1
    result = {"passed":True,"scope":"implementation checks only; no formal twenty-run comparison",
              "block_arithmetic":block_checks,"controls_257":controls,
              "screen_boundaries_and_schedule":True,
              "deadline_control":{"degree":20,"seed":12,"cap":0.75,"last_committed_elapsed":deadline["last_committed_elapsed"],"counts":deadline["counts"]},
              "failure_control":{"degree":18,"seed":11,"reason":failure["termination_reason"],"observed_seconds":failure["observed_run_seconds"]},
              "old_D14_paths_exclude_new_runs":True}
    validation.runtime.frozen.write_json(validation.OUTPUT/f"{label}_checks.json",result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label",required=True)
    args = parser.parse_args()
    print(json.dumps(checks(args.label)))


if __name__ == "__main__":
    main()
