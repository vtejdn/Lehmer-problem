"""Reviewer-owned bounded checks of the fixed S10 archive implementation.

This performs deterministic finite checks and reads labelled implementation
controls.  It starts no worker, samples no research experiment and computes no
root certificates.  The closure generator is the dependency checked in R1111v7.
Synthetic ledger and screen fixtures establish program behavior, not mathematics.
"""

import argparse
import copy
import json
from pathlib import Path
import random
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import archive_sampling as subject
import archive_sampling_export as exporter


def sparse(core, degree):
    """Direct coefficient formula, with no call to the author multiplier."""
    result = set()
    for dilation in range(1, degree // (len(core) - 1) + 1):
        gap = degree - dilation * (len(core) - 1)
        for sign in (-1, 1):
            full = [0] * (degree + 1)
            for power, coefficient in enumerate(core):
                full[dilation * power] += coefficient * sign**power
                if gap:
                    full[dilation * power + gap] += coefficient * sign**power
            assert full == full[::-1] and full[0] == full[-1] == 1
            if all(abs(coefficient) <= 4 for coefficient in full):
                result.add(tuple(full[1:degree // 2 + 1]))
    return sorted(result)


class ReferenceLaw:
    def __init__(self, degree, variant, seed):
        self.degree, self.variant = degree, variant
        self.rng = random.Random(seed)
        self.states = {}
        self.fixed = subject.OriginalLaw(degree // 2, "fixed", seed) if variant == "fixed" else None
        if variant != "fixed":
            self.insert(subject.SEED_CORE)

    def insert(self, core):
        core = tuple(core)
        generated = (sparse(core, self.degree) if self.variant == "direct" else
                     subject.closure.generate(core, self.degree, 4)[0])
        self.states[core] = {"generated": list(generated), "observed": [], "templates": list(generated)}

    def observe(self, core, prefix):
        if self.fixed is not None:
            return
        core, prefix = tuple(core), tuple(prefix)
        if core not in self.states:
            self.insert(core)
        state = self.states[core]
        if prefix not in state["observed"]:
            state["observed"].append(prefix)
        if self.variant == "closure":
            assert prefix in state["generated"]
        elif prefix not in state["templates"]:
            state["templates"].append(prefix)

    def draw(self):
        if self.fixed is not None:
            return self.fixed.draw(), {"branch": "unchanged_fixed_law"}
        rng, dimension = self.rng, self.degree // 2
        branch = rng.randrange(10)
        if branch == 0:
            return [rng.randrange(-4, 5) for _ in range(dimension)], {"branch": "uniform_box"}
        core_index = rng.randrange(len(self.states))
        core = tuple(self.states)[core_index]
        library = self.states[core]["templates"]
        template_index = rng.randrange(len(library))
        parent = library[template_index]
        k = rng.randrange(1, 4)
        coordinates = sorted(rng.sample(range(dimension), k))
        signs = [rng.choice((-1, 1)) for _ in range(k)]
        delta = dict(zip(coordinates, signs))
        candidate = [value + delta.get(index, 0) for index, value in enumerate(parent)]
        exits = not all(-4 <= value <= 4 for value in candidate)
        return (list(parent) if exits else candidate), {
            "branch": "archive_mutation", "core_index": core_index,
            "core_coefficients_ascending": list(core), "template_index": template_index,
            "parent_free_coefficients": list(parent), "k": k, "coordinates": coordinates,
            "signs": signs, "boundary_return": exits}


def deterministic_laws():
    catalog = subject.load_catalog()
    second = next(core for core in catalog if core != subject.SEED_CORE)
    checks, uniform, boundary, multiple_core = 0, 0, 0, 0
    for degree in (24, 30):
        for variant in ("fixed", "direct", "closure"):
            for seed in (0, 23):
                actual = subject.ArchiveLaw(degree, variant, seed)
                actual.initialize()
                reference = ReferenceLaw(degree, variant, seed)
                for index in range(600):
                    if variant != "fixed" and index in (31, 32, 201):
                        core = subject.SEED_CORE if index != 201 else second
                        library = subject.closure.generate(core, degree, 4)[0]
                        prefix = next((entry for entry in library if entry not in sparse(core, degree)), library[0])
                        reference.observe(core, prefix)
                        actual.observe_target(core, prefix)
                    expected, metadata = reference.draw()
                    assert actual.draw() == expected and actual.last_draw == metadata
                    assert len(expected) == degree // 2 and all(-4 <= value <= 4 for value in expected)
                    uniform += metadata["branch"] == "uniform_box"
                    boundary += metadata.get("boundary_return", False)
                    multiple_core += metadata.get("core_index", 0) == 1
                    checks += 1
                assert list(actual.cores) == list(reference.states)
                for core, state in reference.states.items():
                    assert actual.cores[core]["templates"] == state["templates"]
                    assert actual.cores[core]["observed"] == set(state["observed"])
    assert uniform and boundary and multiple_core
    return {"draws": checks, "uniform_branches": uniform, "boundary_returns": boundary,
            "second_core_choices": multiple_core, "insertion_repeat_and_order": True}


def ledger_controls():
    def certificate(core, low, high):
        return {"core_coefficients_ascending": list(core), "measure_interval": [[low, -8], [high, -8]],
                "measure_ball": "synthetic interval fixture", "thresholds": {"6/5": "below"}}
    seed = certificate(subject.SEED_CORE, 299, 300)
    ledger = subject.SeededLedger(seed)
    cases = [(seed, "same_normalized_seed_core", False, True),
             (certificate([1, 0, 1], 298, 301), "unresolved_overlap_with_seed", False, False),
             (certificate([1, 1, 1], 288, 289), "strictly_below_seed_enclosure", True, False),
             (certificate([1, 2, 1], 301, 302), "strictly_above_seed_enclosure", True, False),
             (certificate([1, 3, 1], 287, 290), "strictly_below_seed_enclosure", False, False),
             (certificate([1, 0, 1], 285, 286), "strictly_below_seed_enclosure", False, False)]
    for proposal, (cert, relation, is_new, recovery) in enumerate(cases, 1):
        result = ledger.add(cert, proposal)
        assert result["seed_relation"] == relation and result["new_nonseed_value"] == is_new
        assert result["seed_recovery"] == recovery
    assert len(ledger.ledger.values) == 3 and len(ledger.ledger.uncertain) == 2
    events = [{"kind": "archive_initialization", "seed_certificate": seed, "initial_archive": None},
              {"kind": "archive_initialization_commit", "elapsed": 0.1}]
    repeat = subject.SeededLedger(seed)
    for proposal, cert in enumerate((cases[1][0], cases[-1][0]), 1):
        events.extend([{"kind": "evaluation", "proposal": proposal, "certificate": cert,
                        "seeded_target": repeat.add(cert, proposal), "archive_update": None},
                       {"kind": "commit", "proposal": proposal, "elapsed": proposal / 5}])
    row = {"configuration": {"seconds": 2}, "observed_run_seconds": 2}
    subject.enrich_record(row, events)
    assert len(row["whole_target_core_observations"]) == 1
    assert len(row["unresolved_nonseed_equalities"]) == 1
    assert row["archive_metrics"]["distinct_nonseed_target_values"] == 0
    assert row["strictly_below_seed_values"][0]["proposal"] == 2
    return {"synthetic_cases": len(cases), "uncertain_not_counted": True, "later_strict_seed_separation_retained": True}


def screen_controls():
    rng = random.Random(117)
    checked = 0
    identities = [(degree, variant, seed) for degree in (24, 30)
                  for variant in ("fixed", "direct", "closure") for seed in range(20, 25)]
    for trial in range(500):
        rows = []
        for degree, variant, seed in identities:
            count = rng.randrange(4)
            rows.append({"degree": degree, "arm": variant, "seed": seed,
                         "eligible_archive_comparison_run": True,
                         "archive_metrics": {"distinct_nonseed_target_values": count},
                         "first_nonseed_hit_seconds": rng.randrange(1, 20) if count else None})
        if trial % 10 == 0:
            rows.pop()
        elif trial % 10 == 1:
            rows[-1] = copy.deepcopy(rows[0])
        elif trial % 10 == 2:
            rows[-1]["eligible_archive_comparison_run"] = False
        by_id = {(row["degree"], row["arm"], row["seed"]): row for row in rows}
        complete = len(by_id) == 30 and len(rows) == 30 and all(row["eligible_archive_comparison_run"] for row in rows)
        expected = False
        if complete:
            nonlosses, joint = {}, {}
            for degree in (24, 30):
                nonlosses[degree], joint[degree] = [0, 0], 0
                for seed in range(20, 25):
                    ordered = [by_id[(degree, variant, seed)] for variant in ("closure", "fixed", "direct")]
                    counts = [row["archive_metrics"]["distinct_nonseed_target_values"] for row in ordered]
                    times = [row["first_nonseed_hit_seconds"] for row in ordered]
                    wins = []
                    for i in (1, 2):
                        nonlosses[degree][i - 1] += counts[0] >= counts[i]
                        wins.append(counts[0] > counts[i] or
                                    (counts[0] != 0 and counts[0] == counts[i] and times[0] < times[i]))
                    joint[degree] += wins == [True, True]
            expected = min(value for pair in nonlosses.values() for value in pair) >= 4 and max(joint.values()) >= 3
        result = subject.allocation_screen(rows)
        assert result["complete_declared_archive_comparison"] == complete
        assert result["allocation_screen_passes"] == expected
        checked += 1
    return {"independent_synthetic_screens": checked}


def actual_controls(label, export_label):
    results = []
    for role, suffix in (("proposals", ""), ("deadline", "_deadline"), ("failure", "_failure")):
        native = json.loads((subject.OUTPUT / f"{export_label}_{role}.json").read_text(encoding="utf-8"))
        witness = json.loads((subject.OUTPUT / f"{export_label}_{role}_witnesses.json").read_text(encoding="utf-8"))
        exporter.validate_references(native, witness)
        assert not native["allocation_screen_passes"]
        for group in native["groups"]:
            for row in group["all_seed_outcomes"]:
                path = subject.OUTPUT / row["source_summary"]
                original = json.loads(path.read_text(encoding="utf-8"))
                config = original["configuration"]
                assert path == subject.run_stem(label + suffix, config["degree"], config["variant"], config["seed"]).with_suffix(".json")
                events = subject.frozen.read_events(path.with_suffix(".jsonl"))
                commits = {event["proposal"]: event["elapsed"] for event in events
                           if event["kind"] == "commit" and event["elapsed"] <= config["seconds"]}
                evaluations = {event["proposal"]: event for event in events if event["kind"] == "evaluation"}
                proposals = {event["proposal"]: event for event in events if event["kind"] == "proposal"}
                reference = ReferenceLaw(config["degree"], config["variant"], config["seed"])
                for event in events:
                    if event["kind"] == "proposal":
                        prefix, metadata = reference.draw()
                        assert prefix == event["free_coefficients"] and metadata == event["sampling"]
                    elif event["kind"] == "evaluation" and event["proposal"] in commits:
                        is_target = event.get("thresholds", {}).get("6/5") == "below"
                        assert ("seeded_target" in event) == is_target
                        if is_target:
                            reference.observe(event["certificate"]["core_coefficients_ascending"],
                                              proposals[event["proposal"]]["free_coefficients"])
                assert len(commits) == row["counts"]["completed_proposals"]
                assert len(reference.states) == len(row["final_archive"])
                for final, (core, state) in zip(row["final_archive"], reference.states.items()):
                    assert final["core_coefficients_ascending"] == list(core)
                    assert final["observed_templates"] == [list(prefix) for prefix in state["observed"]]
                    assert final["generated_template_count"] == len(state["generated"])
                    assert final["distinct_template_count"] == len(state["templates"])
                for parent in row["factor_parent_outputs"]:
                    number = parent["proposal"]
                    event = evaluations[number]
                    assert number in commits and parent["elapsed"] == commits[number]
                    assert parent["certificate"] == exporter.common.compact_whole(event["certificate"])
                    assert parent["cost_seconds"] == event["cost_seconds"]
                    assert parent["all_parent_factor_associations"] == event["factor_discoveries"]
                for retry in row["committed_unresolved_inputs"] + row["incomplete_proposal_inputs"]:
                    proposal = proposals[retry["proposal"]]
                    assert retry["free_coefficients"] == proposal["free_coefficients"]
                    assert retry["proposal_elapsed"] == proposal["elapsed"]
                    assert retry["coefficients_ascending"] == subject.frozen.reciprocal_polynomial(proposal["free_coefficients"])
                    assert retry["committed"] == (retry["proposal"] in commits)
                for key in ("configuration", "supervision", "counts", "accounted_stage_seconds", "archive_metrics",
                            "first_nonseed_hit_seconds", "first_nonseed_hit_censored_at", "local_catalog"):
                    assert row.get(key) == original.get(key)
                replay = exporter.replay_retained_run(row)
                results.append({"source": path.name, "proposals_independently_replayed": len(proposals),
                                "completed": len(commits), "compact_replay": replay,
                                "factor_parents": len(row["factor_parent_outputs"]),
                                "unresolved_retry_inputs": len(row["committed_unresolved_inputs"]),
                                "incomplete_retry_inputs": len(row["incomplete_proposal_inputs"])})
    return results


def deadline_suffix_controls(export_label):
    document = json.loads((subject.OUTPUT / f"{export_label}_deadline.json").read_text(encoding="utf-8"))
    original = next(row for group in document["groups"] for row in group["all_seed_outcomes"])
    fixture = copy.deepcopy(original)
    final = fixture["incomplete_proposal_inputs"][-1]
    assert final["proposal"] == fixture["counts"]["proposals"]
    assert final["proposal"] == fixture["counts"]["completed_proposals"] + 1
    final["proposal_elapsed"] = fixture["configuration"]["seconds"] + 0.000001
    fixture["counts"]["proposals"] -= 1
    fixture["counts"]["incomplete_proposals"] -= 1
    checked = exporter.replay_retained_run(fixture)
    assert checked["proposals"] == final["proposal"]
    assert checked["within_budget_proposals"] == final["proposal"] - 1
    assert checked["checked_retry_inputs"] == 1
    assert fixture["final_archive"] == original["final_archive"]
    assert fixture["archive_metrics"] == original["archive_metrics"]
    journal = subject.frozen.read_events((subject.OUTPUT / original["source_summary"]).with_suffix(".jsonl"))
    first = next(event for event in journal if event["kind"] == "proposal")
    committed_fixture = {"proposal": first["proposal"], "free_coefficients": first["free_coefficients"],
                         "coefficients_ascending": subject.frozen.reciprocal_polynomial(first["free_coefficients"]),
                         "committed": True, "proposal_elapsed": first["elapsed"],
                         "reasons": ["synthetic_unresolved_ranking_fixture"]}
    fixture["committed_unresolved_inputs"].append(committed_fixture)
    assert exporter.replay_retained_run(fixture)["checked_retry_inputs"] == 2
    rejected = 0
    for field in ("incomplete_proposal_inputs", "committed_unresolved_inputs"):
        for change_full_only in (False, True):
            altered = copy.deepcopy(fixture)
            candidate = altered[field][-1]
            if change_full_only:
                candidate["coefficients_ascending"][1] += 1
            else:
                candidate["free_coefficients"][0] += -1 if candidate["free_coefficients"][0] == 4 else 1
                candidate["coefficients_ascending"] = subject.frozen.reciprocal_polynomial(candidate["free_coefficients"])
            try:
                exporter.replay_retained_run(altered)
            except AssertionError:
                rejected += 1
            else:
                raise AssertionError("altered retry input accepted")
    return {"scope": "synthetic final elapsed/count boundary and retry-integrity fixtures; no new sampling or yield",
            "final_retained_proposal": final["proposal"], "after_cap_elapsed": final["proposal_elapsed"],
            "within_budget_proposals": checked["within_budget_proposals"],
            "replayed_proposals": checked["proposals"], "unchanged_archive_changes": checked["changes"],
            "committed_and_incomplete_retry_inputs_checked": 2, "altered_inputs_rejected": rejected}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control-label", required=True)
    parser.add_argument("--export-label", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--retention-only", action="store_true")
    args = parser.parse_args()
    assert args.control_label.startswith("control_") and args.export_label.startswith("control_")
    assert not args.output.exists(), "preserve existing review output"
    result = {"scope": "independent bounded implementation checks; no formal comparison or root recertification"}
    if not args.retention_only:
        result.update({"law": deterministic_laws(), "ledger": ledger_controls(), "screen": screen_controls()})
    result.update({"actual_controls": actual_controls(args.control_label, args.export_label),
                   "deadline_suffix_controls": deadline_suffix_controls(args.export_label)})
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
