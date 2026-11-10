"""Review the actual twenty degree-validation histories and retained witnesses.

This performs no sampling run.
It reuses the reviewer's committed-event reconstruction with explicit degree,
protocol, seed, variant and validity parameters, leaving the D14 defaults intact.
"""

import argparse
import itertools
from pathlib import Path
import statistics
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import degree_validation as validation
from independent_live_results import read, write, reconstruct, verify_witnesses, verify_native

THRESHOLDS = ("6/5", "5/4", "13/10", "7/5")


def check_retained_description(native):
    """Reproduce the final descriptive counts from already checked native records."""
    rows = [row for group in native["groups"] for row in group["all_seed_outcomes"]]
    assert len(rows) == 20
    expected = set(itertools.product((18, 20), ("fixed", "A"), range(10, 15)))
    assert {(row["degree"], row["arm"], row["seed"]) for row in rows} == expected
    assert all(row["valid_run"] and row["eligible_degree_validation_run"] for row in rows)
    fields = ("whole_discoveries", "factor_discoveries_separate", "unresolved_factor_equalities_separate",
              "unresolved_value_equalities", "factor_parent_outputs")
    totals = {name: sum(len(row[name]) for row in rows) for name in fields}
    assert totals == {"whole_discoveries": 1691, "factor_discoveries_separate": 1849,
                      "unresolved_factor_equalities_separate": 66, "unresolved_value_equalities": 0,
                      "factor_parent_outputs": 1844}
    unresolved = [item for row in rows for item in row["unresolved_factor_equalities_separate"]]
    assert all(item["thresholds"]["13/10"] == "above" for item in unresolved)
    targets = [item for row in rows for item in row["factor_discoveries_separate"]
               if item["thresholds"]["6/5"] == "below" and not item["certificate"]["neutral"]]
    lehmer = (1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1)
    reflected = tuple(value * (-1)**index for index, value in enumerate(lehmer))
    assert len(targets) == 17
    assert {tuple(item["coefficients_ascending"]) for item in targets} == {lehmer, reflected}
    outside = sum(not item["whole_output_below_6_5"] for item in targets)
    assert outside == 5
    whole_targets = [item for row in rows for item in row["whole_discoveries"]
                     if item["certificate"]["thresholds"]["6/5"] == "below"
                     and not item["certificate"]["neutral"]]
    assert {tuple(item["certificate"]["core_coefficients_ascending"]) for item in whole_targets} == {lehmer}
    best_balls = {row["best_certified_positive"]["certificate"]["measure_ball"] for row in rows
                  if row["distinct_whole_values"]["6/5"]}
    assert best_balls == {"[1.176280818259917506544070338474035051 +/- 5.05e-37]"}
    wider = [{"degree": group["degree"], "arm": group["arm"],
              "counts_by_seed": {threshold: [row["distinct_whole_values"][threshold]
                                             for row in sorted(group["all_seed_outcomes"], key=lambda item: item["seed"])]
                                 for threshold in THRESHOLDS[1:]}}
             for group in native["groups"]]
    return {"scope": "fixed retained descriptive fields only; no journal or certificate replay in this mode",
            **totals, "separate_target_factor_records": len(targets),
            "target_factor_records_in_whole_outputs_outside_target": outside,
            "all_unresolved_factor_equalities_above_13_10": True,
            "all_retained_target_cores_are_Lehmer": True, "best_measure_ball": next(iter(best_balls)),
            "wider_counts_by_seed": wider}


def check_report(comparison, originals, replays):
    rows = [row for group in comparison["groups"] for row in group["all_seed_outcomes"]]
    expected = set(itertools.product((18, 20), ("fixed", "A"), range(10, 15)))
    assert len(rows) == 20 and {(row["degree"], row["arm"], row["seed"]) for row in rows} == expected
    assert comparison["protocol"] == validation.PROTOCOL
    assert comparison["degrees"] == [18, 20] and comparison["seeds"] == list(range(10, 15))
    replay_by_id = {(row["degree"], row["variant"], row["seed"]): row for row in replays}
    for row in rows:
        key = row["degree"], row["arm"], row["seed"]
        original, replay = originals[key], replay_by_id[key]
        for name in ("configuration", "valid_run", "termination_reason", "observed_run_seconds", "eligible_degree_validation_run",
                     "counts", "distinct_whole_values", "raw_whole_hits", "first_target_hit_seconds", "first_target_hit_censored_at",
                     "neutral_mass_completed", "accounted_stage_seconds", "last_committed_elapsed", "supervision"):
            assert row[name] == original[name]
        assert row["budget_seconds"] == 10 and row["max_proposals"] == 0
        assert row["best_measure_ball"] == original["best_certified_positive"]["certificate"]["measure_ball"]
        observations = [{"proposal": item["proposal"], "elapsed": item["elapsed"], "value_id": item["value_id"],
                         **{name: item["certificate"][name] for name in ("coefficients_ascending", "core_coefficients_ascending",
                                                                        "measure_interval", "measure_ball", "thresholds", "neutral")}}
                        for item in original["whole_discoveries"]]
        assert row["whole_value_observations"] == observations
        first_proposal = replay["first_target_hit"]["proposal"] if replay["first_target_hit"] else None
        assert row["first_target_hit_proposal"] == first_proposal
        assert row["A_hit_in_initial_batch"] == (first_proposal <= 256 if row["arm"] == "A" and first_proposal is not None else None)
    assert len(comparison["groups"]) == 4
    assert {(group["degree"], group["arm"]) for group in comparison["groups"]} == set(itertools.product((18, 20), ("fixed", "A")))
    for group in comparison["groups"]:
        group_rows = group["all_seed_outcomes"]
        assert len(group_rows) == 5 and all((row["degree"], row["arm"]) == (group["degree"], group["arm"]) for row in group_rows)
        for threshold in THRESHOLDS:
            values = [row["distinct_whole_values"][threshold] for row in group_rows]
            assert group["distinct_value_statistics"][threshold] == {"median": statistics.median(values), "range": [min(values), max(values)]}
        times = [row["first_target_hit_seconds"] for row in group_rows if row["first_target_hit_seconds"] is not None]
        assert group["first_hit_statistics_among_hits"] == ({"median": statistics.median(times), "range": [min(times), max(times)]} if times else None)
        assert group["censored_no_hit_runs"] == 5 - len(times)
    screens = []
    for degree in (18, 20):
        matched = []
        for seed in range(10, 15):
            counts = {arm: originals[degree, arm, seed]["distinct_whole_values"]["6/5"] for arm in ("fixed", "A")}
            times = {arm: originals[degree, arm, seed]["first_target_hit_seconds"] for arm in ("fixed", "A")}
            improvement = counts["A"] > counts["fixed"] or (counts["A"] == counts["fixed"] > 0 and times["A"] < times["fixed"])
            matched.append({"seed": seed, "target_counts": counts, "first_hit_seconds": times,
                            "A_avoids_loss_to_fixed": counts["A"] >= counts["fixed"], "A_improves_on_fixed": improvement})
        screens.append({"degree": degree, "matched_seed_outcomes": matched,
                        "A_nonlosses_to_fixed": sum(row["A_avoids_loss_to_fixed"] for row in matched),
                        "A_improvements_on_fixed": sum(row["A_improves_on_fixed"] for row in matched)})
    nonloss = all(row["A_nonlosses_to_fixed"] >= 4 for row in screens)
    improvement = any(row["A_improvements_on_fixed"] >= 4 for row in screens)
    assert comparison["complete_declared_degree_validation"] and not comparison["invalid_or_ineligible_runs"]
    assert comparison["degree_screens"] == screens
    assert comparison["nonloss_screen_passes_at_both_degrees"] == nonloss
    assert comparison["improvement_screen_passes_at_one_degree"] == improvement
    assert comparison["allocation_screen_passes"] == (nonloss and improvement)
    assert comparison["experimental_seconds_ceiling_represented"] == 200
    return screens


def main():
    if not __debug__:
        raise RuntimeError("run without -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", default="s10_degree_validation")
    parser.add_argument("--originals", type=Path, default=validation.OUTPUT)
    parser.add_argument("--native-comparison", type=Path, default=HERE / "inputs" / "degree_comparison.json")
    parser.add_argument("--native-witnesses", type=Path, default=HERE / "inputs" / "degree_witnesses.json")
    parser.add_argument("--reuse-verification", type=Path, nargs="*", default=[])
    parser.add_argument("--retained-description-only", action="store_true")
    parser.add_argument("--output", type=Path, default=validation.OUTPUT / "independent_degree_results_review.json")
    args = parser.parse_args()
    if args.retained_description_only:
        print(check_retained_description(read(args.native_comparison)))
        return
    originals, replays = {}, []
    for degree, variant, seed in itertools.product((18, 20), ("fixed", "A"), range(10, 15)):
        base = args.originals / f"{args.label}_d{degree}_{variant}_s{seed}"
        summary = read(base.with_suffix(".json"))
        originals[degree, variant, seed] = summary
        config = summary["configuration"]
        assert config["adaptive_block_widths"] == (([2, 2, 2, 2, 1] if degree == 18 else [2, 2, 2, 2, 2]) if variant == "A" else [])
        replay = reconstruct(base.with_suffix(".jsonl"), summary, protocol=validation.PROTOCOL, degree=degree,
                             seeds=range(10, 15), variants=("fixed", "A"), validity_function=validation.degree_validity,
                             eligibility_field="eligible_degree_validation_run")
        replay["degree"] = degree
        replays.append(replay)
        print({"checked": base.name, "completed": replay["completed_proposals"], "updates": replay["exact_updates_checked"]}, flush=True)
    comparison = read(args.originals / f"{args.label}_degree_comparison.json")
    screens = check_report(comparison, originals, replays)
    native, witnesses = read(args.native_comparison), read(args.native_witnesses)
    assert native["expected_run_count"] == 20 and not native["missing_run_identities"]
    check_retained_description(native)
    previous = {tuple(cert["coefficients_ascending"]): cert for path in args.reuse_verification for cert in read(path)["certificates"]}
    certificates, computed = verify_witnesses(originals, replays, witnesses, previous)
    native_result = verify_native(comparison, native, witnesses, originals, args.originals, args.label, certificates,
                                  protocol=validation.PROTOCOL, expected_runs=20)
    write(validation.OUTPUT / "independent_degree_witness_verification.json", {"kind": "separate_reference_replay", "certificates": list(certificates.values())})
    result = {"scope": "Actual D18/20 fixed/A control: committed proposals, exact laws, complete-measure witnesses and native associations",
              "runs_checked": 20, "completed_proposals": sum(row["completed_proposals"] for row in replays),
              "incomplete_proposals": sum(row["incomplete_proposals"] for row in replays),
              "exact_updates_checked": sum(row["exact_updates_checked"] for row in replays),
              "polynomial_certificates_checked": len(certificates), "certificates_computed_this_call": computed,
              "certificates_reused_from_selected_prior_checks": len(certificates) - computed,
              "native_retention": native_result, "degree_screens": screens, "runs": replays}
    write(args.output, result)
    print({key: value for key, value in result.items() if key not in ("runs", "degree_screens")})


if __name__ == "__main__":
    main()
