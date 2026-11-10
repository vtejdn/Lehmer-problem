"""Separate S10 live control: D14, seeds 5..9, fixed/O/A, 10 seconds each.

The frozen sampler supplies the worker, complete evaluator, cache, duplicate
handling, journal summary and failure/censoring rules without source edits.
Only A's pair pseudocount arithmetic is replaced in the worker process itself.
This program owns its seeds, subprocess dispatch and 15-run report; it never
calls the frozen pilot's run/compare/run_paths or its 45-run completeness test.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import reduce
import json
import math
from pathlib import Path
import statistics
import subprocess
import sys
import time

import sampler as frozen

HERE = Path(__file__).resolve().parent
OUTPUT = frozen.OUTPUT
PROTOCOL = "S10-prior-strength-follow-up"
VARIANTS = ("fixed", "O", "A")
SEEDS = tuple(range(5, 10))
SECONDS = 10.0
OriginalLaw = frozen.Law


class UnitPairPriorLaw(OriginalLaw):
    """Same initialization/draw law; pair total prior 1 and singleton total 9."""

    def apply_elites(self, selected):
        if not selected:
            return
        for block in self.blocks:
            start, width = block["start"], block["width"]
            observations = Counter(tuple(free[start:start + width]) for free in selected)
            # Pair (c + 1/81)/(m + 1) = (81*c + 1)/(81*m + 81).
            scale = 81 if width == 2 else 1
            counts = [scale * observations[state] + 1 for state in block["states"]]
            denominator, total = sum(counts), sum(block["weights"])
            weights = [4 * old * denominator + count * total
                       for old, count in zip(block["weights"], counts)]
            divisor = reduce(math.gcd, weights)
            block["weights"] = [value // divisor for value in weights]
            block["cumulative"] = frozen.cumulative(block["weights"])

    def update(self, batch):
        if self.arm != "adaptive":
            return None
        # This is the frozen selector, unchanged; it is checked against Law.
        representatives = {}
        for core, score, free in batch:
            item = (score, tuple(free))
            if core not in representatives or item < representatives[core]:
                representatives[core] = item
        selected = sorted(representatives.values())[:math.ceil(len(representatives) / 10)]
        self.apply_elites([free for _, free in selected])
        return {"eligible_proposals": len(batch), "unique_eligible_cores": len(representatives),
                "elite_count": len(selected), "elite_free_coefficients": [list(free) for _, free in selected]}


def base_arm(variant):
    return "fixed" if variant == "fixed" else "adaptive"


def law_class(variant):
    return UnitPairPriorLaw if variant == "A" else OriginalLaw


def tag_configuration(event, variant, failure_check=False):
    return {**event, "protocol": PROTOCOL, "arm": variant, "variant": variant,
            "implementation_arm": base_arm(variant), "law_class": law_class(variant).__name__,
            "pair_prior_total": 1 if variant == "A" else 81 if variant == "O" else None,
            "singleton_prior_total": 9 if variant != "fixed" else None,
            "controlled_failure_check": failure_check}


def worker(args):
    """Select the actual variant inside this new subprocess, before construction."""
    original_write = frozen.write_event

    def write_event(stream, event):
        if event["kind"] == "config":
            event = tag_configuration(event, args.variant, args.fail_after_first_proposal)
        original_write(stream, event)
        if args.fail_after_first_proposal and event["kind"] == "proposal":
            raise RuntimeError("deliberate live-control failure after first proposal")

    frozen.Law = law_class(args.variant)
    frozen.write_event = write_event
    try:
        frozen.worker(argparse.Namespace(degree=14, arm=base_arm(args.variant), seed=args.seed,
                                         seconds=args.seconds, started=args.started,
                                         events=args.events, max_proposals=args.max_proposals))
    finally:
        frozen.Law = OriginalLaw
        frozen.write_event = original_write


def check_label(label):
    if not label or any(ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for ch in label):
        raise ValueError("label must contain only letters, numbers, '-' and '_'")


def run_stem(label, variant, seed):
    check_label(label)
    return OUTPUT / f"{label}_d14_{variant}_s{seed}"


def live_validity(record):
    validity = frozen.run_validity(record)
    validity.pop("eligible_full_pilot_run")
    config = record["configuration"]
    validity["eligible_live_comparison_run"] = bool(
        validity["valid_run"] and validity["termination_reason"] == "deadline"
        and config["protocol"] == PROTOCOL and config["degree"] == 14
        and config["variant"] in VARIANTS and config["seed"] in SEEDS
        and config["seconds"] == SECONDS and config["max_proposals"] == 0
        and not config.get("controlled_failure_check", False))
    return validity


def run_once(variant, seed, seconds, label, max_proposals=0, *, failure_check=False, raise_on_failure=True):
    if variant not in VARIANTS or seed not in SEEDS or not 0 < seconds <= SECONDS or max_proposals < 0:
        raise ValueError("live control requires fixed/O/A, seeds 5..9, and 0<seconds<=10")
    stem = run_stem(label, variant, seed)
    events = stem.with_suffix(".jsonl")
    if events.exists() or stem.with_suffix(".json").exists():
        raise FileExistsError(f"preserve existing output; choose another label: {stem.name}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    command = [sys.executable, "-B", str(Path(__file__).resolve()), "_worker", "--variant", variant,
               "--seed", str(seed), "--seconds", str(seconds), "--started", str(started),
               "--events", str(events), "--max-proposals", str(max_proposals)]
    if failure_check:
        command.append("--fail-after-first-proposal")
    process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    killed = False
    try:
        _, stderr = process.communicate(timeout=max(0, seconds - (time.perf_counter() - started)))
    except subprocess.TimeoutExpired:
        killed = True
        process.kill()
        _, stderr = process.communicate()
    elapsed = time.perf_counter() - started
    journal = frozen.read_events(events) if events.exists() else []
    has_config = any(event["kind"] == "config" for event in journal)
    if has_config:
        record = frozen.summarize_events(events)
        config = record["configuration"]
        if (config["protocol"], config["variant"], config["seed"]) != (PROTOCOL, variant, seed):
            raise RuntimeError("worker dispatch/configuration mismatch")
    else:
        # Persist a startup failure rather than silently losing a requested run.
        config = tag_configuration({"degree": 14, "seed": seed, "seconds": seconds,
                                    "max_proposals": max_proposals}, variant, failure_check)
        record = {"configuration": config, "counts": {"proposals": 0, "completed_proposals": 0},
                  "configuration_source": "requested; worker produced no configuration",
                  "last_committed_elapsed": 0, "first_target_hit_seconds": None,
                  "first_target_hit_censored_at": None, "worker_failure": True,
                  "distinct_whole_values": {key: 0 for key in frozen.THRESHOLDS},
                  "raw_whole_hits": {key: 0 for key in frozen.THRESHOLDS},
                  "best_certified_positive": None, "neutral_mass_completed": None}
    record["supervision"] = {"killed_at_cap": killed, "worker_returncode": process.returncode,
                              "supervisor_elapsed_seconds": elapsed, "stderr": stderr.decode(errors="replace"),
                              "summary_computed_after_cap": "bookkeeping only; no polynomial evaluation or certification",
                              "shared_dependency_import_seconds": frozen.DEPENDENCY_IMPORT_SECONDS}
    if not killed and process.returncode != 0:
        record["worker_failure"] = True
    record.update(live_validity(record))
    if record["first_target_hit_seconds"] is None:
        record["first_target_hit_censored_at"] = record["observed_run_seconds"]
    frozen.write_json(stem.with_suffix(".json"), record)
    print(json.dumps({"file": stem.with_suffix(".json").name, "variant": variant, "seed": seed,
                      "valid_run": record["valid_run"], "termination_reason": record["termination_reason"],
                      "completed_proposals": record["counts"]["completed_proposals"],
                      "distinct_whole_values": record["distinct_whole_values"],
                      "first_target_hit_seconds": record["first_target_hit_seconds"]}), flush=True)
    if raise_on_failure and not record["valid_run"]:
        raise RuntimeError(record["supervision"]["stderr"] or record["termination_reason"])
    return record


def run_paths(label):
    return [path for seed in SEEDS for variant in VARIANTS
            if (path := run_stem(label, variant, seed).with_suffix(".json")).is_file()]


def summary_statistics(values):
    return {"median": statistics.median(values), "range": [min(values), max(values)]} if values else None


def report(label):
    runs = []
    for path in run_paths(label):
        record = json.loads(path.read_text(encoding="utf-8"))
        config = record["configuration"]
        if config.get("protocol") != PROTOCOL:
            raise ValueError(f"foreign experiment in {path.name}")
        if run_stem(label, config["variant"], config["seed"]) != path.with_suffix(""):
            raise ValueError(f"run identity does not match filename: {path.name}")
        runs.append({"arm": config["variant"], "seed": config["seed"],
                     "budget_seconds": config["seconds"], "max_proposals": config["max_proposals"],
                     **live_validity(record), "counts": record["counts"],
                     "distinct_whole_values": record["distinct_whole_values"],
                     "raw_whole_hits": record["raw_whole_hits"],
                     "first_target_hit_seconds": record["first_target_hit_seconds"],
                     "first_target_hit_censored_at": record["first_target_hit_censored_at"],
                     "neutral_mass_completed": record["neutral_mass_completed"],
                     "best_measure_ball": record["best_certified_positive"]["certificate"]["measure_ball"]
                     if record["best_certified_positive"] else None,
                     "supervision": record["supervision"]})
    groups = []
    for variant in VARIANTS:
        all_rows = [run for run in runs if run["arm"] == variant]
        eligible = [run for run in all_rows if run["eligible_live_comparison_run"]]
        groups.append({"arm": variant, "all_seed_outcomes": all_rows,
                       "distinct_value_statistics": {threshold: summary_statistics([run["distinct_whole_values"][threshold] for run in eligible])
                                                     for threshold in frozen.THRESHOLDS},
                       "first_hit_statistics_among_hits": summary_statistics([run["first_target_hit_seconds"] for run in eligible
                                                                               if run["first_target_hit_seconds"] is not None]),
                       "censored_no_hit_runs": sum(run["first_target_hit_seconds"] is None for run in eligible)})
    return {"protocol": PROTOCOL, "label": label, "degree": 14, "seeds": list(SEEDS),
            "groups": groups, **allocation_screen(runs),
            "invalid_or_ineligible_runs": [{key: run[key] for key in ("arm", "seed", "valid_run", "termination_reason", "observed_run_seconds")}
                                            for run in runs if not run["eligible_live_comparison_run"]],
            "experimental_seconds_ceiling_represented": sum(run["budget_seconds"] for run in runs),
            "interpretation": "Separate reused D14 benchmark with new seeds; incomplete controls cannot pass and no significance or unseen-degree claim is made."}


def allocation_screen(runs):
    """The separately specified 15-run screen, with explicit completeness gating."""
    matched = []
    for seed in SEEDS:
        arms = {run["arm"]: run for run in runs if run["seed"] == seed and run["eligible_live_comparison_run"]}
        if set(arms) != set(VARIANTS):
            continue
        target = {arm: run["distinct_whole_values"]["6/5"] for arm, run in arms.items()}
        improves_o = target["A"] > target["O"] or (
            target["A"] == target["O"] and target["A"] > 0 and
            arms["A"]["first_target_hit_seconds"] < arms["O"]["first_target_hit_seconds"])
        matched.append({"seed": seed, "target_counts": target,
                        "first_hit_seconds": {arm: run["first_target_hit_seconds"] for arm, run in arms.items()},
                        "A_avoids_loss_to_fixed": target["A"] >= target["fixed"],
                        "A_improves_on_O": improves_o})
    expected_keys = {(variant, seed) for variant in VARIANTS for seed in SEEDS}
    actual_keys = {(run["arm"], run["seed"]) for run in runs}
    complete = len(runs) == 15 and actual_keys == expected_keys and all(run["eligible_live_comparison_run"] for run in runs)
    nonlosses = sum(row["A_avoids_loss_to_fixed"] for row in matched)
    improvements = sum(row["A_improves_on_O"] for row in matched)
    return {"matched_seed_outcomes": matched,
            "complete_declared_live_control": complete,
            "A_nonlosses_to_fixed": nonlosses, "A_improvements_on_O": improvements,
            "allocation_screen_passes": complete and nonlosses >= 4 and improvements >= 4}


def compare(label):
    # Fixed schedule: no hidden repeats, parameter grid, or old-pilot completeness rule.
    if any(run_stem(label, variant, seed).with_suffix(suffix).exists()
           for seed in SEEDS for variant in VARIANTS for suffix in (".json", ".jsonl")):
        raise FileExistsError("comparison label already has runs; preserve them and use explicit remaining run commands")
    try:
        for index, seed in enumerate(SEEDS):
            rotation = index % len(VARIANTS)
            for variant in VARIANTS[rotation:] + VARIANTS[:rotation]:
                run_once(variant, seed, SECONDS, label)
    finally:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        frozen.write_json(OUTPUT / f"{label}_live_comparison.json", report(label))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("run", "_worker"):
        command = commands.add_parser(name)
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
        worker(args)
    elif args.command == "run":
        run_once(args.variant, args.seed, args.seconds, args.label, args.max_proposals)
    elif args.command == "compare":
        compare(args.label)
    else:
        frozen.write_json(OUTPUT / f"{args.label}_live_comparison.json", report(args.label))


if __name__ == "__main__":
    main()
