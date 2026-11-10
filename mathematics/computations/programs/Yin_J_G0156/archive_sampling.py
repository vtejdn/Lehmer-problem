"""S10 reference-seeded template comparison, D24/30, fixed/direct/closure.

Only the Lehmer core enters the worker as reference information.  The unchanged
sampler evaluates every proposal; its cache, precision, commit and supervisor
contracts are reused.  Archive construction and target bookkeeping occur before
the same evaluation commit, inside the run's deadline.  The local two-core
catalog is loaded only by post-run reporting, never by a proposal worker.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import random
import time

import cyclotomic_closure as closure
import sampling_runtime as runtime

frozen = runtime.frozen
HERE, OUTPUT = frozen.HERE, frozen.OUTPUT
PROTOCOL = "S10-cyclotomic-archive-comparison"
DEGREES, VARIANTS, SEEDS = (24, 30), ("fixed", "direct", "closure"), tuple(range(20, 25))
SECONDS = 20.0
SEED_CORE = closure.LEHMER
CATALOG = HERE / "inputs" / "degree_core_mass_states.json"
OriginalLaw = frozen.Law


def sparse_completions(core, degree):
    """Exact sparse completions from S10; no census or second-core input."""
    core, prefixes = tuple(core), set()
    d = len(core) - 1
    if d < 2 or d % 2 or core != core[::-1] or core[0] != 1 or core[-1] != 1:
        raise ValueError("expected an even monic reciprocal core")
    for k in range(1, degree // d + 1):
        remainder = degree - k * d
        for sign in (-1, 1):
            lifted = [0] * (k * d + 1)
            for i, value in enumerate(core):
                lifted[k * i] = value * sign**i
            neutral = [1] if not remainder else [1] + [0] * (remainder - 1) + [1]
            polynomial = closure.multiply(lifted, neutral)
            assert len(polynomial) == degree + 1 and polynomial == polynomial[::-1]
            if max(map(abs, polynomial)) <= 4:
                prefixes.add(polynomial[1:degree // 2 + 1])
    return sorted(prefixes)


class ArchiveLaw:
    """Uniform core then uniform distinct template; insertion order is explicit."""

    def __init__(self, degree, variant, seed):
        self.degree, self.half_degree, self.variant = degree, degree // 2, variant
        self.rng = random.Random(seed)
        self.fixed = OriginalLaw(self.half_degree, "fixed", seed) if variant == "fixed" else None
        self.cores, self.last_draw = {}, None

    def add_core(self, core):
        core = tuple(core)
        if core in self.cores:
            raise ValueError("core already present")
        if self.variant == "closure":
            generated, construction = closure.generate(core, self.degree, 4)
        elif self.variant == "direct":
            generated, construction = sparse_completions(core, self.degree), None
        else:
            raise ValueError("fixed bias has no template archive")
        self.cores[core] = {"generated": set(generated), "observed": set(),
                            "templates": list(generated), "membership": set(generated)}
        return {"core_coefficients_ascending": list(core),
                "generated_templates": [list(prefix) for prefix in generated],
                "construction_counts": construction}

    def initialize(self):
        return None if self.variant == "fixed" else self.add_core(SEED_CORE)

    def observe_target(self, core, free):
        if self.variant == "fixed":
            return None
        core, free = tuple(core), tuple(free)
        created = self.add_core(core) if core not in self.cores else None
        state = self.cores[core]
        if self.variant == "closure" and free not in state["membership"]:
            raise ValueError("certified whole target is absent from its generated closure")
        new_observed = free not in state["observed"]
        added_template = free not in state["membership"]
        state["observed"].add(free)
        if added_template:
            state["templates"].append(free)
            state["membership"].add(free)
        if not state["templates"]:
            raise ValueError("a stored core must have a template")
        return {"core_coefficients_ascending": list(core), "new_core": created,
                "observed_free_coefficients": list(free), "new_observed_template": new_observed,
                "added_template": added_template, **self.counts(core)}

    def counts(self, core):
        state = self.cores[tuple(core)]
        return {"generated_template_count": len(state["generated"]),
                "observed_template_count": len(state["observed"]),
                "observed_nongenerated_template_count": len(state["observed"] - state["generated"]),
                "distinct_template_count": len(state["templates"])}

    def draw(self):
        if self.fixed is not None:
            free = self.fixed.draw()
            self.last_draw = {"branch": "unchanged_fixed_law"}
            return free
        if self.rng.randrange(10) == 0:
            free = [self.rng.randrange(-4, 5) for _ in range(self.half_degree)]
            self.last_draw = {"branch": "uniform_box"}
            return free
        core_index = self.rng.randrange(len(self.cores))
        core = list(self.cores)[core_index]
        templates = self.cores[core]["templates"]
        template_index = self.rng.randrange(len(templates))
        parent = templates[template_index]
        k = self.rng.randrange(1, 4)
        coordinates = sorted(self.rng.sample(range(self.half_degree), k))
        signs = [self.rng.choice((-1, 1)) for _ in coordinates]
        free = list(parent)
        for coordinate, sign in zip(coordinates, signs):
            free[coordinate] += sign
        boundary_return = any(abs(value) > 4 for value in free)
        if boundary_return:
            free = list(parent)
        self.last_draw = {"branch": "archive_mutation", "core_index": core_index,
                          "core_coefficients_ascending": list(core), "template_index": template_index,
                          "parent_free_coefficients": list(parent), "k": k,
                          "coordinates": coordinates, "signs": signs, "boundary_return": boundary_return}
        return free

    def update(self, batch):
        # The frozen worker retains its batching/accounting, but no coordinate fit
        # is performed.  Whole-target archive changes use the evaluation hook.
        return None


class SeededLedger:
    def __init__(self, seed_certificate):
        self.seed_certificate = seed_certificate
        self.ledger = frozen.DiscoveryLedger()
        assert self.ledger.add(seed_certificate, 0) == {"status": "new_separated_value", "value_id": 0}

    def add(self, certificate, proposal):
        identity = self.ledger.add(certificate, proposal)
        same_seed_core = tuple(certificate["core_coefficients_ascending"]) == SEED_CORE
        interval, seed = certificate["measure_interval"], self.seed_certificate["measure_interval"]
        if same_seed_core:
            relation = "same_normalized_seed_core"
        elif frozen.interval_fraction(interval[1]) < frozen.interval_fraction(seed[0]):
            relation = "strictly_below_seed_enclosure"
        elif frozen.interval_fraction(interval[0]) > frozen.interval_fraction(seed[1]):
            relation = "strictly_above_seed_enclosure"
        else:
            relation = "unresolved_overlap_with_seed"
        value_id = identity.get("value_id")
        return {"identity": identity, "seed_relation": relation, "seed_recovery": same_seed_core,
                "certified_nonseed_value": value_id is not None and value_id > 0,
                "new_nonseed_value": identity["status"] == "new_separated_value" and value_id > 0}


def configuration(degree, variant, seed):
    return {"protocol": PROTOCOL, "degree": degree, "arm": variant, "variant": variant,
            "seed": seed, "implementation_arm": "fixed", "law_class": "ArchiveLaw",
            "supplied_seed_core_coefficients_ascending": list(SEED_CORE), "seed_is_discovery": False,
            "archive_scope": "completed whole targets only; no factor-only training",
            "core_order": "seed first, then first committed whole-target encounter",
            "template_order": "sorted generated prefixes, then new observed prefixes in encounter order",
            "mutation": "uniform k=1,2,3; uniform distinct coordinates sorted before independent signs; box exit returns parent",
            "initialization": "fresh seed certification and template construction inside each run cap",
            "reporting_catalog": "inputs/degree_core_mass_states.json two cores; post-run only"}


def worker(args):
    original_law, original_write = frozen.Law, frozen.write_event
    law = ArchiveLaw(args.degree, args.variant, args.seed)
    seeded_ledger = None

    def write_event(stream, event):
        nonlocal seeded_ledger
        kind = event["kind"]
        if kind == "config":
            event = {**event, **configuration(args.degree, args.variant, args.seed),
                     "controlled_failure_check": args.fail_after_first_proposal}
            original_write(stream, event)
            original_write(stream, {"kind": "archive_initialization_started",
                                    "elapsed": time.perf_counter() - args.started})
            started = time.perf_counter()
            seed_certificate = frozen.certify_polynomial(list(SEED_CORE))
            assert seed_certificate["thresholds"]["6/5"] == "below"
            assert tuple(seed_certificate["core_coefficients_ascending"]) == SEED_CORE
            seeded_ledger = SeededLedger(seed_certificate)
            certification_seconds = time.perf_counter() - started
            started = time.perf_counter()
            archive = law.initialize()
            initialization = {"kind": "archive_initialization", "seed_certificate": seed_certificate,
                              "initial_archive": archive,
                              "cost_seconds": {"seed_certification_and_ledger": certification_seconds,
                                               "initial_template_construction": time.perf_counter() - started}}
            original_write(stream, initialization)
            finished = time.perf_counter() - args.started
            if finished <= args.seconds:
                original_write(stream, {"kind": "archive_initialization_commit", "elapsed": finished})
            return
        if kind == "proposal":
            event = {**event, "sampling": law.last_draw}
        elif kind == "evaluation" and event.get("thresholds", {}).get("6/5") == "below":
            certificate = event["certificate"]
            started = time.perf_counter()
            target = seeded_ledger.add(certificate, event["proposal"])
            metric_seconds = time.perf_counter() - started
            started = time.perf_counter()
            update = law.observe_target(certificate["core_coefficients_ascending"],
                                        certificate["coefficients_ascending"][1:args.degree // 2 + 1])
            event = {**event, "seeded_target": target, "archive_update": update,
                     "cost_seconds": {**event["cost_seconds"], "seeded_value_deduplication": metric_seconds,
                                      "archive_update": time.perf_counter() - started}}
        original_write(stream, event)
        if args.fail_after_first_proposal and kind == "proposal":
            raise RuntimeError("deliberate archive-runtime failure after first proposal")

    frozen.Law = lambda half_degree, arm, seed: law
    frozen.write_event = write_event
    try:
        frozen.worker(argparse.Namespace(degree=args.degree, arm="fixed", seed=args.seed,
                                         seconds=args.seconds, started=args.started,
                                         events=args.events, max_proposals=args.max_proposals))
    finally:
        frozen.Law, frozen.write_event = original_law, original_write


def load_catalog():
    document = json.loads(CATALOG.read_text(encoding="utf-8"))
    groups = document["target_partitions"][0]["core_groups"]
    catalog = {tuple(group["core_coefficients_ascending"]):
               {key: group[key] for key in ("core_coefficients_ascending", "measure_interval", "measure_ball")}
               for group in groups}
    assert len(catalog) == 2 and SEED_CORE in catalog
    return catalog


def apply_retained_update(states, update):
    """Pure journal bookkeeping; never regenerate a closure after the cap."""
    created = update.get("new_core")
    core = tuple(update["core_coefficients_ascending"])
    if created is not None:
        assert core not in states
        generated = [tuple(prefix) for prefix in created["generated_templates"]]
        states[core] = {"generated": generated, "observed": [], "templates": list(generated)}
    state = states[core]
    prefix = tuple(update["observed_free_coefficients"])
    assert update["new_observed_template"] == (prefix not in state["observed"])
    assert update["added_template"] == (prefix not in state["templates"])
    if update["new_observed_template"]:
        state["observed"].append(prefix)
    if update["added_template"]:
        state["templates"].append(prefix)
    assert len(state["templates"]) == update["distinct_template_count"]
    assert len(state["observed"]) == update["observed_template_count"]


def enrich_record(record, events):
    """Only committed observations affect yields and retained archive state."""
    budget = record["configuration"]["seconds"]
    commits = {event["proposal"]: event["elapsed"] for event in events
               if event["kind"] == "commit" and event["elapsed"] <= budget}
    init_commit = next((event for event in events if event["kind"] == "archive_initialization_commit"
                        and event["elapsed"] <= budget), None)
    initial = next((event for event in events if event["kind"] == "archive_initialization"), None) if init_commit else None
    catalog = load_catalog()  # The worker does not call this reporting function.
    metrics = Counter()
    discoveries, uncertain, below_seed, core_observations, archive_changes = [], [], [], [], []
    states, seen_cores, below_seed_cores = {}, set(), set()
    first_nonseed, first_seed = None, None
    if initial and initial["initial_archive"]:
        item = initial["initial_archive"]
        prefixes = [tuple(prefix) for prefix in item["generated_templates"]]
        states[SEED_CORE] = {"generated": prefixes, "observed": [], "templates": list(prefixes)}
    for event in events:
        if event["kind"] != "evaluation" or event["proposal"] not in commits or "seeded_target" not in event:
            continue
        assert initial is not None
        target, certificate = event["seeded_target"], event["certificate"]
        core = tuple(certificate["core_coefficients_ascending"])
        item = {"proposal": event["proposal"], "elapsed": commits[event["proposal"]],
                **target, "certificate": certificate}
        metrics["raw_seed_recovery_hits"] += target["seed_recovery"]
        metrics["raw_certified_nonseed_hits"] += target["certified_nonseed_value"]
        metrics["raw_unresolved_nonseed_hits"] += not target["seed_recovery"] and not target["certified_nonseed_value"]
        if target["seed_recovery"] and first_seed is None:
            first_seed = {"proposal": item["proposal"], "elapsed": item["elapsed"]}
        if target["new_nonseed_value"]:
            discoveries.append(item)
            if first_nonseed is None:
                first_nonseed = {"proposal": item["proposal"], "elapsed": item["elapsed"]}
        if target["identity"]["status"] == "unresolved_equality":
            uncertain.append(item)
        if core not in seen_cores:
            seen_cores.add(core)
            classification = "supplied_seed_core" if core == SEED_CORE else "second_local_core" if core in catalog else "not_in_supplied_local_catalog"
            core_observations.append({**item, "local_classification": classification})
        if target["seed_relation"] == "strictly_below_seed_enclosure" and core not in below_seed_cores:
            below_seed_cores.add(core)
            below_seed.append(item)
        update = event.get("archive_update")
        if update:
            apply_retained_update(states, update)
            metrics["archive_target_update_calls"] += 1
            if update["new_core"] is not None or update["new_observed_template"]:
                archive_changes.append({"proposal": item["proposal"], "elapsed": item["elapsed"],
                                        "cost_seconds": event["cost_seconds"]["archive_update"], **update})
    for key in ("raw_seed_recovery_hits", "raw_certified_nonseed_hits", "raw_unresolved_nonseed_hits", "archive_target_update_calls"):
        metrics[key] += 0
    metrics["distinct_nonseed_target_values"] = len(discoveries)
    final = [{"core_coefficients_ascending": list(core),
              "generated_templates": [list(prefix) for prefix in state["generated"]],
              "observed_templates": [list(prefix) for prefix in state["observed"]],
              "generated_template_count": len(state["generated"]),
              "observed_template_count": len(state["observed"]),
              "observed_nongenerated_template_count": len(set(state["observed"]) - set(state["generated"])),
              "distinct_template_count": len(state["templates"])} for core, state in states.items()]
    record.update({"archive_initialization_committed": init_commit is not None,
                   "archive_initialization_elapsed": init_commit["elapsed"] if init_commit else None,
                   "archive_initialization": initial,
                   "archive_metrics": dict(metrics), "final_archive": final,
                   "committed_archive_changes": archive_changes,
                   "nonseed_discoveries": discoveries, "unresolved_nonseed_equalities": uncertain,
                   "strictly_below_seed_values": below_seed, "whole_target_core_observations": core_observations,
                   "first_nonseed_hit_seconds": first_nonseed["elapsed"] if first_nonseed else None,
                   "first_nonseed_hit_proposal": first_nonseed["proposal"] if first_nonseed else None,
                   "first_nonseed_hit_censored_at": None if first_nonseed else record["observed_run_seconds"],
                   "first_seed_recovery": first_seed,
                   "local_catalog": {"source": "inputs/degree_core_mass_states.json", "scope": "two reference cores; post-run classification, not a completeness certificate from this sampler",
                                     "cores": list(catalog.values())}})
    return record


def check_label(label):
    if not label or any(ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for ch in label):
        raise ValueError("label must use letters, digits, '-' or '_'")


def run_stem(label, degree, variant, seed):
    check_label(label)
    return OUTPUT / f"{label}_d{degree}_{variant}_s{seed}"


def archive_validity(record):
    validity = frozen.run_validity(record)
    validity.pop("eligible_full_pilot_run")
    config = record["configuration"]
    validity["eligible_archive_comparison_run"] = bool(
        validity["valid_run"] and validity["termination_reason"] == "deadline"
        and config["protocol"] == PROTOCOL and config["degree"] in DEGREES
        and config["variant"] in VARIANTS and config["seed"] in SEEDS
        and config["seconds"] == SECONDS and config["max_proposals"] == 0
        and not config.get("controlled_failure_check", False))
    return validity


def run_once(degree, variant, seed, seconds, label, max_proposals=0, *, failure_check=False, raise_on_failure=True):
    if degree not in DEGREES or variant not in VARIANTS or type(seed) is not int or seed < 0 or not 0 < seconds <= SECONDS or max_proposals < 0:
        raise ValueError("D24/30, fixed/direct/closure, nonnegative integer seed, 0<seconds<=20 required")
    if seed not in SEEDS and not label.startswith("control_"):
        raise ValueError("nonformal seeds require an explicit control_ label")
    args = argparse.Namespace(degree=degree, variant=variant, seed=seed, seconds=seconds, max_proposals=max_proposals)
    stem = run_stem(label, degree, variant, seed)
    record = runtime.supervise(__file__, stem, args, configuration(degree, variant, seed), failure_check)
    events = frozen.read_events(stem.with_suffix(".jsonl")) if stem.with_suffix(".jsonl").exists() else []
    enrich_record(record, events)
    record.update(archive_validity(record))
    frozen.write_json(stem.with_suffix(".json"), record)
    print(json.dumps({"file": stem.with_suffix(".json").name, "valid_run": record["valid_run"],
                      "termination_reason": record["termination_reason"], "completed_proposals": record["counts"]["completed_proposals"],
                      "archive_initialization_elapsed": record["archive_initialization_elapsed"],
                      "archive_metrics": record["archive_metrics"]}), flush=True)
    if raise_on_failure and not record["valid_run"]:
        raise RuntimeError(record["supervision"]["stderr"] or record["termination_reason"])
    return record


def run_paths(label):
    return [path for degree in DEGREES for seed in SEEDS for variant in VARIANTS
            if (path := run_stem(label, degree, variant, seed).with_suffix(".json")).is_file()]


def improves(left, right):
    a, b = left["archive_metrics"]["distinct_nonseed_target_values"], right["archive_metrics"]["distinct_nonseed_target_values"]
    return a > b or (a == b and a > 0 and left["first_nonseed_hit_seconds"] < right["first_nonseed_hit_seconds"])


def allocation_screen(runs):
    expected = {(degree, variant, seed) for degree in DEGREES for variant in VARIANTS for seed in SEEDS}
    actual = {(row["degree"], row["arm"], row["seed"]) for row in runs}
    complete = len(runs) == 30 and actual == expected and all(row["eligible_archive_comparison_run"] for row in runs)
    screens = []
    for degree in DEGREES:
        matched = []
        for seed in SEEDS:
            arms = {row["arm"]: row for row in runs if row["degree"] == degree and row["seed"] == seed
                    and row["eligible_archive_comparison_run"]}
            if set(arms) != set(VARIANTS):
                continue
            counts = {variant: row["archive_metrics"]["distinct_nonseed_target_values"] for variant, row in arms.items()}
            wins = {variant: improves(arms["closure"], arms[variant]) for variant in ("fixed", "direct")}
            matched.append({"seed": seed, "nonseed_target_counts": counts,
                            "first_nonseed_hit_seconds": {variant: row["first_nonseed_hit_seconds"] for variant, row in arms.items()},
                            "closure_nonloss": {variant: counts["closure"] >= counts[variant] for variant in ("fixed", "direct")},
                            "closure_improvement": wins, "closure_joint_improvement": all(wins.values())})
        screens.append({"degree": degree, "matched_seed_outcomes": matched,
                        "closure_nonlosses": {variant: sum(row["closure_nonloss"][variant] for row in matched) for variant in ("fixed", "direct")},
                        "closure_joint_improvements": sum(row["closure_joint_improvement"] for row in matched)})
    nonloss = complete and all(all(n >= 4 for n in row["closure_nonlosses"].values()) for row in screens)
    wins = complete and any(row["closure_joint_improvements"] >= 3 for row in screens)
    return {"complete_declared_archive_comparison": complete, "degree_screens": screens,
            "nonloss_screen_passes_at_both_degrees": nonloss, "joint_improvement_screen_passes_at_one_degree": wins,
            "allocation_screen_passes": nonloss and wins}


def report(label, paths=None):
    rows = []
    for path in run_paths(label) if paths is None else paths:
        record = json.loads(Path(path).read_text(encoding="utf-8"))
        config = record["configuration"]
        if config["protocol"] != PROTOCOL or run_stem(label, config["degree"], config["variant"], config["seed"]) != Path(path).with_suffix(""):
            raise ValueError(f"wrong protocol or identity: {path}")
        rows.append({**record, **archive_validity(record), "degree": config["degree"], "arm": config["variant"], "seed": config["seed"]})
    groups = [{"degree": degree, "arm": variant,
               "all_seed_outcomes": [row for row in rows if row["degree"] == degree and row["arm"] == variant]}
              for degree in DEGREES for variant in VARIANTS]
    return {"protocol": PROTOCOL, "label": label, "degrees": list(DEGREES), "seeds": list(SEEDS),
            "groups": groups, **allocation_screen(rows),
            "experimental_seconds_ceiling_represented": sum(row["configuration"]["seconds"] for row in rows),
            "interpretation": "Reference-seeded finite comparison; supplied seed is excluded from primary yield; local catalog has two cores only; no literature novelty or significance claim."}


def schedule():
    schedule_rows = []
    for degree_index, degree in enumerate(DEGREES):
        for seed_index, seed in enumerate(SEEDS):
            offset = (degree_index + seed_index) % 3
            schedule_rows.extend((degree, variant, seed) for variant in VARIANTS[offset:] + VARIANTS[:offset])
    return schedule_rows


def compare(label):
    if any(run_stem(label, degree, variant, seed).with_suffix(suffix).exists()
           for degree, variant, seed in schedule() for suffix in (".json", ".jsonl")):
        raise FileExistsError("preserve existing runs; use explicit remaining run commands")
    try:
        for degree, variant, seed in schedule():
            run_once(degree, variant, seed, SECONDS, label)
    finally:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        frozen.write_json(OUTPUT / f"{label}_archive_comparison.json", report(label))


def replay_journal(path):
    """Reproduce proposal RNG and archive updates, without roots or new sampling."""
    events = frozen.read_events(path)
    config = next(event for event in events if event["kind"] == "config")
    assert config["protocol"] == PROTOCOL
    commits = {event["proposal"] for event in events if event["kind"] == "commit" and event["elapsed"] <= config["seconds"]}
    initial = next((event for event in events if event["kind"] == "archive_initialization"), None)
    initialized = any(event["kind"] == "archive_initialization_commit" and event["elapsed"] <= config["seconds"] for event in events)
    law = ArchiveLaw(config["degree"], config["variant"], config["seed"])
    if not initialized:
        assert not commits
        return {"initialization_committed": False, "checked_proposals": 0, "checked_updates": 0}
    assert law.initialize() == initial["initial_archive"]
    ledger = SeededLedger(initial["seed_certificate"])
    proposals = updates = 0
    for event in events:
        if event["kind"] == "proposal":
            assert law.draw() == event["free_coefficients"]
            assert law.last_draw == event["sampling"]
            proposals += 1
        elif event["kind"] == "evaluation" and event["proposal"] in commits and "seeded_target" in event:
            cert = event["certificate"]
            assert ledger.add(cert, event["proposal"]) == event["seeded_target"]
            update = law.observe_target(cert["core_coefficients_ascending"], cert["coefficients_ascending"][1:config["degree"] // 2 + 1])
            assert update == event["archive_update"]
            updates += 1
    return {"initialization_committed": True, "checked_proposals": proposals, "checked_updates": updates}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("run", "_worker"):
        command = commands.add_parser(name)
        command.add_argument("--degree", type=int, choices=DEGREES, required=True)
        command.add_argument("--variant", choices=VARIANTS, required=True)
        command.add_argument("--seed", type=int, required=True)
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
    commands.add_parser("replay").add_argument("events", type=Path)
    args = parser.parse_args()
    if args.command == "_worker":
        worker(args)
    elif args.command == "run":
        run_once(args.degree, args.variant, args.seed, args.seconds, args.label, args.max_proposals)
    elif args.command == "compare":
        compare(args.label)
    elif args.command == "report":
        frozen.write_json(OUTPUT / f"{args.label}_archive_comparison.json", report(args.label))
    else:
        print(json.dumps(replay_journal(args.events)))


if __name__ == "__main__":
    main()
