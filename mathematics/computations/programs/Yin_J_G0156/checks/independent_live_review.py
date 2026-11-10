"""Independent pre-run arithmetic and eligibility checks for the S10 live control.

This command starts no worker and does not run the formal 15-run schedule.
It consumes the explicitly named short-control outputs produced separately by
prior_strength_live_checks.py and checks the changed interfaces directly.
"""

import argparse
import copy
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import prior_strength_live as live


def probabilities(law):
    return [[F(weight, sum(block["weights"])) for weight in block["weights"]] for block in law.blocks]


def exact_update(blocks, old, elites, pair_prior):
    if not elites:
        return old
    result = []
    for block, distribution in zip(blocks, old):
        start, width = block["start"], block["width"]
        prior = pair_prior if width == 2 else F(1)
        denominator = len(elites) + len(block["states"]) * prior
        frequencies = [sum(tuple(row[start:start + width]) == state for row in elites)
                       for state in block["states"]]
        result.append([F(4, 5) * old_probability + F(1, 5) * (count + prior) / denominator
                       for old_probability, count in zip(distribution, frequencies)])
    return result


def arithmetic_checks():
    law = live.UnitPairPriorLaw(7, "adaptive", 5)
    expected = probabilities(law)
    weights = (1, 2, 4, 8, 16, 8, 4, 2, 1)
    for block, distribution in zip(law.blocks, expected):
        for state, probability in zip(block["states"], distribution):
            product = F(1)
            for value in state:
                product *= F(weights[value + 4], 46)
            assert probability == product
    controls = [[], [[0] * 7], [[-4, 4, -3, 3, -2, 2, 1], [4, -4, 3, -3, 2, -2, -1]],
                [list(row) for row in itertools.islice(itertools.product(range(-4, 5), repeat=7), 26)]]
    for elites in controls:
        expected = exact_update(law.blocks, expected, elites, F(1, 81))
        law.apply_elites(elites)
        assert probabilities(law) == expected
        assert all(sum(distribution) == 1 and all(value > 0 for value in distribution) for distribution in expected)
    before = probabilities(law)
    assert law.update([]) == {"eligible_proposals": 0, "unique_eligible_cores": 0,
                              "elite_count": 0, "elite_free_coefficients": []}
    assert probabilities(law) == before
    # Three eligible cores, repeated representatives and deterministic score/tuple ties.
    batch = [((1,), 2.0, [0] * 7), ((1,), 1.0, [1] * 7), ((1,), 1.0, [-1] * 7),
             ((2,), 1.0, [0] * 7), ((3,), 3.0, [2] * 7)]
    expected = exact_update(law.blocks, before, [[-1] * 7], F(1, 81))
    assert law.update(batch) == {"eligible_proposals": 5, "unique_eligible_cores": 3,
                                "elite_count": 1, "elite_free_coefficients": [[-1] * 7]}
    assert probabilities(law) == expected
    maximum = live.UnitPairPriorLaw(7, "adaptive", 9)
    batch = [((i,), float(i), [i % 9 - 4] * 7) for i in range(256)]
    result = maximum.update(batch)
    assert result["unique_eligible_cores"] == 256 and result["elite_count"] == 26
    assert result["elite_free_coefficients"] == [[i % 9 - 4] * 7 for i in range(26)]
    assert live.law_class("A") is live.UnitPairPriorLaw
    assert live.law_class("O") is live.OriginalLaw and live.law_class("fixed") is live.OriginalLaw
    return {"exact_pair_prior": "1/81 per state", "singleton_prior": "1 per state",
            "smoothing": "4/5 old + 1/5 updated empirical law", "checked_elite_sizes": [0, 1, 2, 26],
            "selector_ties_and_maximum_elite_count": True}


def validity_checks():
    base = {"configuration": {"protocol": live.PROTOCOL, "degree": 14, "variant": "A", "seed": 5,
                               "seconds": 10, "max_proposals": 0, "controlled_failure_check": False},
            "counts": {"completed_proposals": 257}, "last_committed_elapsed": 9.9,
            "supervision": {"killed_at_cap": True, "worker_returncode": 1, "supervisor_elapsed_seconds": 10.02}}
    result = live.live_validity(base)
    assert result == {"valid_run": True, "termination_reason": "deadline", "observed_run_seconds": 10,
                      "eligible_live_comparison_run": True}
    cases = []
    early = copy.deepcopy(base)
    early["supervision"] = {"killed_at_cap": False, "worker_returncode": 0, "supervisor_elapsed_seconds": 0.4}
    cases.append(("clean_early_exit", early, False, "early_exit", 0.4))
    failure = copy.deepcopy(early)
    failure["supervision"]["worker_returncode"] = 1
    cases.append(("worker_failure", failure, False, "worker_failure", 0.4))
    limited = copy.deepcopy(early)
    limited["configuration"]["max_proposals"] = 257
    cases.append(("proposal_limit", limited, True, "proposal_limit", 0.4))
    short = copy.deepcopy(base)
    short["configuration"]["seconds"] = 0.75
    short["supervision"]["supervisor_elapsed_seconds"] = 0.77
    cases.append(("short_deadline", short, True, "deadline", 0.75))
    for name, record, valid, reason, observed in cases:
        result = live.live_validity(record)
        assert result["valid_run"] == valid and result["termination_reason"] == reason
        assert result["observed_run_seconds"] == observed and not result["eligible_live_comparison_run"], name
    for key, value in (("protocol", "S10-first-experiment"), ("degree", 18), ("seed", 0),
                       ("controlled_failure_check", True)):
        record = copy.deepcopy(base)
        record["configuration"][key] = value
        assert not live.live_validity(record)["eligible_live_comparison_run"]
    runs = [{"arm": variant, "seed": seed, "eligible_live_comparison_run": True,
             "distinct_whole_values": {"6/5": 1}, "first_target_hit_seconds": 1 if variant == "A" else 2}
            for seed in range(5, 10) for variant in ("fixed", "O", "A")]
    assert live.allocation_screen(runs)["allocation_screen_passes"]
    assert not live.allocation_screen(runs[:-1])["allocation_screen_passes"]
    duplicate = copy.deepcopy(runs)
    duplicate[-1] = copy.deepcopy(duplicate[0])
    assert not live.allocation_screen(duplicate)["complete_declared_live_control"]
    for seed in (8, 9):
        next(row for row in runs if row["arm"] == "A" and row["seed"] == seed)["first_target_hit_seconds"] = 2
    result = live.allocation_screen(runs)
    assert result["complete_declared_live_control"] and result["A_improvements_on_O"] == 3
    assert not result["allocation_screen_passes"]
    return {"deadline_and_failure_cases": [name for name, *_ in cases], "ineligible_scopes_excluded": True,
            "15_identity_completeness_and_four_seed_threshold": True}


def short_control_checks(label):
    observed = []
    for variant in live.VARIANTS:
        path = live.run_stem(label + "_257", variant, 5).with_suffix(".json")
        record = json.loads(path.read_text(encoding="utf-8"))
        config = record["configuration"]
        assert (config["variant"], config["seed"], config["degree"]) == (variant, 5, 14)
        assert config["law_class"] == live.law_class(variant).__name__
        assert config["implementation_arm"] == live.base_arm(variant)
        assert config["seconds"] == 10 and config["max_proposals"] == 257
        assert record["counts"]["completed_proposals"] == 257
        assert record["valid_run"] and not record["eligible_live_comparison_run"]
        observed.append({"variant": variant, "completed": 257, "termination_reason": record["termination_reason"]})
    failed = json.loads(live.run_stem(label + "_failure", "O", 7).with_suffix(".json").read_text(encoding="utf-8"))
    assert not failed["valid_run"] and failed["termination_reason"] == "worker_failure"
    assert failed["counts"]["proposals"] == 1 and failed["counts"]["completed_proposals"] == 0
    assert failed["first_target_hit_censored_at"] == failed["observed_run_seconds"] < 2
    for suffix in ("_257", "_deadline", "_failure"):
        report = live.report(label + suffix)
        assert not report["complete_declared_live_control"] and not report["allocation_screen_passes"]
        assert all(group["distinct_value_statistics"]["6/5"] is None for group in report["groups"])
    return {"controls": observed, "actual_failure_censor": failed["observed_run_seconds"],
            "all_short_or_failed_controls_excluded_from_live_statistics": True}


def main():
    if not __debug__:
        raise RuntimeError("run without -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True)
    parser.add_argument("--output", type=Path, default=live.OUTPUT / "independent_live_preflight_review.json")
    args = parser.parse_args()
    result = {"scope": "pre-run changed-interface review; no formal live experiment",
              "arithmetic": arithmetic_checks(), "validity": validity_checks(), "short_controls": short_control_checks(args.label)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
