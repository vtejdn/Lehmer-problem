"""S10 degree validation: D18 then D20, fixed/A, seeds 10..14, 20 x 10 s.

The existing A class is imported unchanged, with no reference training.
Worker evaluation, precision, caching, duplicates and validity use the frozen
sampler through sampling_runtime; this entry owns its independent 20-run screen.
"""

import argparse
import json
from pathlib import Path

import prior_strength_live as prior
import sampling_runtime as runtime

HERE = Path(__file__).resolve().parent
OUTPUT = prior.OUTPUT
PROTOCOL = "S10-degree-validation"
DEGREES = (18, 20)
VARIANTS = ("fixed", "A")
SEEDS = tuple(range(10, 15))
SECONDS = 10.0


def configuration(degree, variant, seed):
    widths = [2] * (degree // 4) + ([1] if (degree // 2) % 2 else [])
    return {"protocol": PROTOCOL, "degree": degree, "arm": variant, "variant": variant,
            "seed": seed, "implementation_arm": prior.base_arm(variant),
            "law_class": prior.law_class(variant).__name__,
            "law_source": "prior_strength_live.py:UnitPairPriorLaw" if variant == "A" else "sampler.py:Law",
            "adaptive_block_widths": widths if variant == "A" else [],
            "pair_prior_total": 1 if variant == "A" else None,
            "singleton_prior_total": 9 if variant == "A" and 1 in widths else None}


def run_stem(label, degree, variant, seed):
    prior.check_label(label)
    return OUTPUT / f"{label}_d{degree}_{variant}_s{seed}"


def degree_validity(record):
    validity = runtime.frozen.run_validity(record)
    validity.pop("eligible_full_pilot_run")
    config = record["configuration"]
    validity["eligible_degree_validation_run"] = bool(
        validity["valid_run"] and validity["termination_reason"] == "deadline"
        and config["protocol"] == PROTOCOL and config["degree"] in DEGREES
        and config["variant"] in VARIANTS and config["seed"] in SEEDS
        and config["seconds"] == SECONDS and config["max_proposals"] == 0
        and not config.get("controlled_failure_check", False))
    return validity


def run_once(degree, variant, seed, seconds, label, max_proposals=0, *, failure_check=False, raise_on_failure=True):
    if degree not in DEGREES or variant not in VARIANTS or seed not in SEEDS or not 0 < seconds <= SECONDS or max_proposals < 0:
        raise ValueError("degree validation requires D18/20, fixed/A, seeds 10..14 and 0<seconds<=10")
    args = argparse.Namespace(degree=degree, variant=variant, seed=seed, seconds=seconds, max_proposals=max_proposals)
    stem = run_stem(label, degree, variant, seed)
    record = runtime.supervise(__file__, stem, args, configuration(degree, variant, seed), failure_check)
    record.update(degree_validity(record))
    runtime.frozen.write_json(stem.with_suffix(".json"), record)
    print(json.dumps({"file": stem.with_suffix(".json").name, "degree": degree, "variant": variant,
                      "seed": seed, "valid_run": record["valid_run"], "termination_reason": record["termination_reason"],
                      "completed_proposals": record["counts"]["completed_proposals"],
                      "distinct_whole_values": record["distinct_whole_values"],
                      "first_target_hit_seconds": record["first_target_hit_seconds"]}), flush=True)
    if raise_on_failure and not record["valid_run"]:
        raise RuntimeError(record["supervision"]["stderr"] or record["termination_reason"])
    return record


def run_paths(label):
    return [path for degree in DEGREES for seed in SEEDS for variant in VARIANTS
            if (path := run_stem(label, degree, variant, seed).with_suffix(".json")).is_file()]


def allocation_screen(runs):
    expected = {(degree, variant, seed) for degree in DEGREES for variant in VARIANTS for seed in SEEDS}
    actual = {(row["degree"], row["arm"], row["seed"]) for row in runs}
    complete = len(runs) == 20 and actual == expected and all(row["eligible_degree_validation_run"] for row in runs)
    degree_screens = []
    for degree in DEGREES:
        matched = []
        for seed in SEEDS:
            arms = {row["arm"]: row for row in runs if row["degree"] == degree and row["seed"] == seed
                    and row["eligible_degree_validation_run"]}
            if set(arms) != set(VARIANTS):
                continue
            counts = {variant: row["distinct_whole_values"]["6/5"] for variant, row in arms.items()}
            improves = counts["A"] > counts["fixed"] or (
                counts["A"] == counts["fixed"] and counts["A"] > 0 and
                arms["A"]["first_target_hit_seconds"] < arms["fixed"]["first_target_hit_seconds"])
            matched.append({"seed": seed, "target_counts": counts,
                            "first_hit_seconds": {variant: row["first_target_hit_seconds"] for variant, row in arms.items()},
                            "A_avoids_loss_to_fixed": counts["A"] >= counts["fixed"],
                            "A_improves_on_fixed": improves})
        degree_screens.append({"degree": degree, "matched_seed_outcomes": matched,
                               "A_nonlosses_to_fixed": sum(row["A_avoids_loss_to_fixed"] for row in matched),
                               "A_improvements_on_fixed": sum(row["A_improves_on_fixed"] for row in matched)})
    nonloss = complete and all(row["A_nonlosses_to_fixed"] >= 4 for row in degree_screens)
    improvement = complete and any(row["A_improvements_on_fixed"] >= 4 for row in degree_screens)
    return {"complete_declared_degree_validation": complete, "degree_screens": degree_screens,
            "nonloss_screen_passes_at_both_degrees": nonloss,
            "improvement_screen_passes_at_one_degree": improvement,
            "allocation_screen_passes": nonloss and improvement}


def whole_value_observations(record):
    return [{"proposal": item["proposal"], "elapsed": item["elapsed"], "value_id": item["value_id"],
             **{key: item["certificate"][key] for key in ("coefficients_ascending", "core_coefficients_ascending",
                                                         "measure_interval", "measure_ball", "thresholds", "neutral")}}
            for item in record.get("whole_discoveries", [])]


def report(label):
    runs = []
    for path in run_paths(label):
        record = json.loads(path.read_text(encoding="utf-8"))
        config = record["configuration"]
        if config.get("protocol") != PROTOCOL or run_stem(label, config["degree"], config["variant"], config["seed"]) != path.with_suffix(""):
            raise ValueError(f"wrong protocol or run identity: {path.name}")
        observations = whole_value_observations(record)
        first = record["first_target_hit_seconds"]
        first_proposal = next((item["proposal"] for item in observations
                               if item["elapsed"] == first and item["thresholds"]["6/5"] == "below"), None)
        runs.append({"degree": config["degree"], "arm": config["variant"], "seed": config["seed"],
                     "configuration": config, "budget_seconds": config["seconds"], "max_proposals": config["max_proposals"],
                     **degree_validity(record), "counts": record["counts"],
                     "distinct_whole_values": record["distinct_whole_values"],
                     "raw_whole_hits": record["raw_whole_hits"], "first_target_hit_seconds": first,
                     "first_target_hit_censored_at": record["first_target_hit_censored_at"],
                     "first_target_hit_proposal": first_proposal,
                     "A_hit_in_initial_batch": first_proposal <= 256 if config["variant"] == "A" and first_proposal is not None else None,
                     "neutral_mass_completed": record["neutral_mass_completed"],
                     "whole_value_observations": observations,
                     "best_measure_ball": record["best_certified_positive"]["certificate"]["measure_ball"]
                     if record["best_certified_positive"] else None,
                     "accounted_stage_seconds": record.get("accounted_stage_seconds", {}),
                     "last_committed_elapsed": record["last_committed_elapsed"],
                     "supervision": record["supervision"]})
    groups = []
    for degree in DEGREES:
        for variant in VARIANTS:
            rows = [row for row in runs if row["degree"] == degree and row["arm"] == variant]
            eligible = [row for row in rows if row["eligible_degree_validation_run"]]
            groups.append({"degree": degree, "arm": variant, "all_seed_outcomes": rows,
                           "distinct_value_statistics": {threshold: prior.summary_statistics([row["distinct_whole_values"][threshold] for row in eligible])
                                                         for threshold in runtime.frozen.THRESHOLDS},
                           "first_hit_statistics_among_hits": prior.summary_statistics([row["first_target_hit_seconds"] for row in eligible
                                                                                         if row["first_target_hit_seconds"] is not None]),
                           "censored_no_hit_runs": sum(row["first_target_hit_seconds"] is None for row in eligible)})
    return {"protocol": PROTOCOL, "label": label, "degrees": list(DEGREES), "seeds": list(SEEDS),
            "groups": groups, **allocation_screen(runs),
            "invalid_or_ineligible_runs": [{key: row[key] for key in ("degree", "arm", "seed", "valid_run", "termination_reason", "observed_run_seconds")}
                                            for row in runs if not row["eligible_degree_validation_run"]],
            "experimental_seconds_ceiling_represented": sum(row["budget_seconds"] for row in runs),
            "interpretation": "Reused D18/20 benchmarks with new seeds. Pre-update first-hit comparisons are observations without learning attribution. No unseen-set or significance claim."}


def schedule():
    return [(degree, variant, seed) for degree_index, degree in enumerate(DEGREES)
            for seed_index, seed in enumerate(SEEDS)
            for variant in (VARIANTS if (degree_index + seed_index) % 2 == 0 else VARIANTS[::-1])]


def compare(label):
    if any(run_stem(label, degree, variant, seed).with_suffix(suffix).exists()
           for degree, variant, seed in schedule() for suffix in (".json", ".jsonl")):
        raise FileExistsError("preserve existing runs; use explicit remaining run commands")
    try:
        for degree, variant, seed in schedule():
            run_once(degree, variant, seed, SECONDS, label)
    finally:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        runtime.frozen.write_json(OUTPUT / f"{label}_degree_comparison.json", report(label))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("run", "_worker"):
        command = commands.add_parser(name)
        command.add_argument("--degree", type=int, choices=DEGREES, required=True)
        command.add_argument("--variant", choices=VARIANTS, required=True)
        command.add_argument("--seed", type=int, choices=SEEDS, required=True)
        command.add_argument("--seconds", type=float, default=SECONDS)
        command.add_argument("--max-proposals", type=int, default=0)
        if name == "run":
            command.add_argument("--label", required=True)
        else:
            command.add_argument("--started", type=float, required=True)
            command.add_argument("--events", required=True)
            command.add_argument("--fail-after-first-proposal", action="store_true")
    for name in ("compare", "report"):
        commands.add_parser(name).add_argument("--label", required=True)
    args = parser.parse_args()
    if args.command == "_worker":
        runtime.worker(args, configuration(args.degree, args.variant, args.seed),
                       prior.law_class(args.variant), prior.base_arm(args.variant))
    elif args.command == "run":
        run_once(args.degree, args.variant, args.seed, args.seconds, args.label, args.max_proposals)
    elif args.command == "compare":
        compare(args.label)
    else:
        runtime.frozen.write_json(OUTPUT / f"{args.label}_degree_comparison.json", report(args.label))


if __name__ == "__main__":
    main()
