"""Bounded review of the new degree-validation interfaces; no worker is started.

The actual four 257-proposal child controls are produced separately by
degree_validation_checks.py under the explicitly selected label.
The mocked startup failure below checks the new runtime failure branch without
creating a synthetic experimental journal or running the 20-run schedule.
"""

import argparse
import copy
import itertools
import json
from pathlib import Path
import sys
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import degree_validation as validation


def check_interfaces(label):
    schedule = validation.schedule()
    expected = set(itertools.product((18, 20), ("fixed", "A"), range(10, 15)))
    assert len(schedule) == 20 and set(schedule) == expected
    for degree_index, degree in enumerate((18, 20)):
        for seed_index, seed in enumerate(range(10, 15)):
            offset = 10 * degree_index + 2 * seed_index
            order = ("fixed", "A") if (degree_index + seed_index) % 2 == 0 else ("A", "fixed")
            assert schedule[offset:offset + 2] == [(degree, arm, seed) for arm in order]
    for degree in (18, 20):
        config = validation.configuration(degree, "A", 14)
        assert config["adaptive_block_widths"] == ([2, 2, 2, 2, 1] if degree == 18 else [2, 2, 2, 2, 2])
        assert config["law_class"] == "UnitPairPriorLaw" and config["implementation_arm"] == "adaptive"
        assert config["pair_prior_total"] == 1
        assert config["singleton_prior_total"] == (9 if degree == 18 else None)
    base = {"configuration": {**validation.configuration(18, "A", 10), "seconds": 10,
                              "max_proposals": 0, "controlled_failure_check": False},
            "counts": {"completed_proposals": 257}, "last_committed_elapsed": 9.9,
            "supervision": {"killed_at_cap": True, "worker_returncode": 1, "supervisor_elapsed_seconds": 10.01}}
    assert validation.degree_validity(base) == {"valid_run": True, "termination_reason": "deadline",
                                               "observed_run_seconds": 10, "eligible_degree_validation_run": True}
    for key, value in (("protocol", "S10-prior-strength-follow-up"), ("degree", 14), ("seed", 9),
                       ("variant", "O"), ("seconds", 0.75), ("max_proposals", 257), ("controlled_failure_check", True)):
        record = copy.deepcopy(base)
        record["configuration"][key] = value
        assert not validation.degree_validity(record)["eligible_degree_validation_run"]
    for returncode, reason in ((0, "early_exit"), (1, "worker_failure")):
        record = copy.deepcopy(base)
        record["supervision"] = {"killed_at_cap": False, "worker_returncode": returncode, "supervisor_elapsed_seconds": 0.3}
        result = validation.degree_validity(record)
        assert not result["valid_run"] and not result["eligible_degree_validation_run"]
        assert result["termination_reason"] == reason and result["observed_run_seconds"] == 0.3

    arguments = argparse.Namespace(degree=20, variant="A", seed=14, seconds=2, max_proposals=0)
    configuration = validation.configuration(20, "A", 14)
    stem = validation.run_stem(label + "_mock_startup", 20, "A", 14)
    with patch.object(validation.runtime.subprocess, "Popen", side_effect=OSError("review-only simulated startup failure")) as launch:
        failed = validation.runtime.supervise(HERE / "degree_validation.py", stem, arguments, configuration)
    command = launch.call_args.args[0]
    assert Path(command[2]).resolve() == (HERE / "degree_validation.py").resolve()
    assert command[3] == "_worker"
    for flag, expected_value in (("--degree", "20"), ("--variant", "A"), ("--seed", "14"),
                                 ("--seconds", "2"), ("--max-proposals", "0")):
        assert command[command.index(flag) + 1] == expected_value
    assert not failed["valid_run"] and failed["worker_failure"] and failed["termination_reason"] == "worker_failure"
    assert failed["counts"]["completed_proposals"] == 0 and failed["configuration"]["degree"] == 20
    assert failed["first_target_hit_censored_at"] == failed["observed_run_seconds"] < 2
    assert not validation.degree_validity(failed)["eligible_degree_validation_run"]
    assert not stem.with_suffix(".jsonl").exists()

    controls = []
    for degree, variant in itertools.product((18, 20), ("fixed", "A")):
        path = validation.run_stem(label + "_257", degree, variant, 10).with_suffix(".json")
        record = json.loads(path.read_text(encoding="utf-8"))
        config = record["configuration"]
        assert (config["degree"], config["variant"], config["seed"]) == (degree, variant, 10)
        assert record["counts"]["completed_proposals"] == 257
        assert record["valid_run"] and record["termination_reason"] == "proposal_limit"
        assert not record["eligible_degree_validation_run"]
        controls.append({"degree": degree, "variant": variant, "completed": 257})
    for suffix in ("_257", "_deadline", "_failure"):
        report = validation.report(label + suffix)
        assert not report["complete_declared_degree_validation"] and not report["allocation_screen_passes"]
        assert not report["nonloss_screen_passes_at_both_degrees"]
        assert not report["improvement_screen_passes_at_one_degree"]
        assert all(group["distinct_value_statistics"]["6/5"] is None for group in report["groups"])
    return {"scope": "new degree/runtime/identity interfaces only; no formal comparison",
            "schedule_identities": len(schedule), "rotation_checked": True,
            "actual_short_controls": controls, "foreign_and_early_runs_ineligible": True,
            "startup_failure": {"simulated": True, "degree": 20, "variant": "A", "seed": 14,
                                "valid_run": failed["valid_run"], "observed_censor": failed["observed_run_seconds"]},
            "short_and_failed_reports_cannot_pass_either_screen": True}


def main():
    if not __debug__:
        raise RuntimeError("run without -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True)
    parser.add_argument("--output", type=Path, default=validation.OUTPUT / "independent_degree_preflight_review.json")
    args = parser.parse_args()
    result = check_interfaces(args.label)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
