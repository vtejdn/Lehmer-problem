"""Regression for a saved failed/early run being pooled as a complete pilot."""

from copy import deepcopy
import itertools
import json
from unittest.mock import patch

import sampler


class SavedRun:
    def __init__(self, record):
        self.record = record

    def read_text(self, encoding=None):
        return json.dumps(self.record)


def records():
    return [{
        "configuration": {"degree": degree, "arm": arm, "seed": seed,
                          "seconds": 60, "max_proposals": 0},
        "supervision": {"killed_at_cap": True, "worker_returncode": 0,
                        "supervisor_elapsed_seconds": 60.01, "stderr": ""},
        "counts": {"completed_proposals": 100}, "last_committed_elapsed": 59.99,
        "distinct_whole_values": {key: 1 for key in sampler.THRESHOLDS},
        "raw_whole_hits": {key: 1 for key in sampler.THRESHOLDS},
        "first_target_hit_seconds": None, "first_target_hit_censored_at": 60,
        "neutral_mass_completed": 0, "best_certified_positive": None,
    } for degree, arm, seed in itertools.product(sampler.DEGREES, sampler.ARMS, range(5))]


def report(rows):
    with patch.object(sampler, "run_paths", return_value=[SavedRun(row) for row in rows]):
        return sampler.comparison_report("failure-regression")


def main():
    baseline = records()
    assert report(baseline)["complete_declared_pilot"]
    rows = deepcopy(baseline)
    target = next(row for row in rows if (row["configuration"]["degree"], row["configuration"]["arm"],
                                        row["configuration"]["seed"]) == (18, "adaptive", 2))
    target["worker_failure"] = True
    target["supervision"].update(killed_at_cap=False, worker_returncode=1, supervisor_elapsed_seconds=1.25)
    target["distinct_whole_values"] = {key: 99 for key in sampler.THRESHOLDS}
    actual = report(rows)
    assert not actual["complete_declared_pilot"] and len(actual["invalid_runs"]) == 1
    group = next(group for group in actual["groups"] if (group["degree"], group["arm"]) == (18, "adaptive"))
    failed = next(run for run in group["seed_outcomes"] if run["seed"] == 2)
    assert failed["worker_failure"] and not failed["valid_run"]
    assert failed["first_target_hit_censored_at"] == 1.25
    assert group["distinct_value_statistics"]["6/5"] == {"median": 1, "range": [1, 1], "valid_runs": 4}
    matched = next(row for row in actual["held_out_matched_comparisons"] if row["degree"] == 18)
    assert {item["seed"] for item in matched["matched_seeds"]} == {0, 1, 3, 4}
    for row in rows:
        row["worker_failure"] = True
        row["supervision"].update(killed_at_cap=False, worker_returncode=1, supervisor_elapsed_seconds=1.25)
    actual = report(rows)
    assert not actual["complete_declared_pilot"] and len(actual["invalid_runs"]) == 45
    assert all(not row["matched_seeds"] for row in actual["held_out_matched_comparisons"])
    assert all(group["distinct_value_statistics"]["6/5"]["median"] is None for group in actual["groups"])
    early = deepcopy(baseline[0])
    early["supervision"].update(killed_at_cap=False, supervisor_elapsed_seconds=0.5)
    assert sampler.run_validity(early)["termination_reason"] == "early_exit"
    assert not sampler.run_validity(early)["valid_run"]
    early["configuration"]["max_proposals"] = 100
    assert sampler.run_validity(early)["valid_run"]
    assert not sampler.run_validity(early)["eligible_full_pilot_run"]
    print(json.dumps({"failure_boundary_regression_passed": True,
                      "cases": ["valid pilot", "one failed run", "45 failed runs", "early successful exit", "proposal-limited control"]}))


if __name__ == "__main__":
    main()
