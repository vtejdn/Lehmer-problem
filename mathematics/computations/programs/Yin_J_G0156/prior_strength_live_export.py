"""Retain observed live-control outcomes and exact replay witnesses in J156.

Sources are explicitly prior_strength_live.run_paths: D14, seeds 5..9,
fixed/O/A. This does not use the original 45-run pilot's path enumeration.
No proposals, factorization, roots or new certificates are computed here.
Selected factor associations are joined to their actually committed parent
events so the factor and its original whole output remain reproducible.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import prior_strength_live as live

HERE = Path(__file__).resolve().parent
WHOLE_REQUIRED = ("coefficients_ascending", "core_coefficients_ascending", "measure_interval",
                  "measure_ball", "thresholds", "neutral")
WHOLE_EXTRA = ("precision_bits", "factorization_product_verified", "root_count_with_multiplicity",
               "ranking_resolved", "log_score")
FACTOR_REQUIRED = ("coefficients_ascending", "measure_interval", "measure_ball", "thresholds",
                   "degree", "exponent", "root_count", "cyclotomic")
WHOLE_COLLECTIONS = (("whole_discoveries", "whole_threshold_value"),
                     ("unresolved_value_equalities", "unresolved_whole_value_equality"))
FACTOR_COLLECTIONS = (("factor_discoveries_separate", "separate_irreducible_factor"),
                      ("unresolved_factor_equalities_separate", "unresolved_factor_value_equality"))


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def compact_whole(certificate):
    result = {key: copy.deepcopy(certificate[key]) for key in WHOLE_REQUIRED}
    result.update({key: copy.deepcopy(certificate[key]) for key in WHOLE_EXTRA if key in certificate})
    return result


def compact_factor(certificate):
    result = {key: copy.deepcopy(certificate[key]) for key in FACTOR_REQUIRED}
    result["neutral"] = certificate["cyclotomic"]
    result["scope"] = "measure of the single factor; exponent records its multiplicity in the parent"
    return result


class Witnesses:
    def __init__(self):
        self.by_coefficients = {}

    def add(self, coefficients, role, run):
        key = tuple(coefficients)
        if key not in self.by_coefficients:
            self.by_coefficients[key] = {"witness_id": f"w{len(self.by_coefficients) + 1}",
                                         "coefficients_ascending": list(coefficients), "roles": [], "runs": []}
        item = self.by_coefficients[key]
        if role not in item["roles"]:
            item["roles"].append(role)
        if run not in item["runs"]:
            item["runs"].append(run)
        return item["witness_id"]

    def document(self, label):
        return {"protocol": live.PROTOCOL, "source_label": label,
                "purpose": "exact replay inputs; verification never adds stochastic discoveries",
                "witnesses": list(self.by_coefficients.values())}


def committed_factor_parents(record, summary_path):
    wanted = {item["proposal"] for field, _ in FACTOR_COLLECTIONS for item in record.get(field, [])}
    if not wanted:
        return {}
    journal = summary_path.with_suffix(".jsonl")
    parents, pending = {}, None
    with journal.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                break
            if event["kind"] == "evaluation" and event["proposal"] in wanted:
                pending = event
            elif event["kind"] == "commit" and event["proposal"] in wanted:
                if event["elapsed"] > record["configuration"]["seconds"]:
                    continue
                assert pending is not None and pending["proposal"] == event["proposal"]
                assert "certificate" in pending
                parents[event["proposal"]] = {"elapsed": event["elapsed"], "certificate": pending["certificate"],
                                               "factor_associations": pending["factor_discoveries"]}
                pending = None
                if set(parents) == wanted:
                    break
    if set(parents) != wanted:
        raise ValueError(f"missing committed parent certificates in {journal.name}: {sorted(wanted - set(parents))}")
    return parents


def retain_run(row, record, path, witnesses):
    run = path.stem
    # Preserve all observed scalar/count/time/configuration fields, then compact
    # only the certificate-bearing collections. Derived live validity must agree.
    for key in ("valid_run", "termination_reason", "observed_run_seconds", "eligible_live_comparison_run"):
        if key in record:
            assert record[key] == row[key]
    retained = copy.deepcopy(record)
    for field, role in WHOLE_COLLECTIONS:
        retained[field] = []
        for source in record.get(field, []):
            item = copy.deepcopy(source)
            item["certificate"] = compact_whole(source["certificate"])
            item["witness_id"] = witnesses.add(item["certificate"]["coefficients_ascending"], role, run)
            retained[field].append(item)
    if record.get("best_certified_positive"):
        source = record["best_certified_positive"]
        retained["best_certified_positive"] = {**copy.deepcopy(source), "certificate": compact_whole(source["certificate"]),
                                               "witness_id": witnesses.add(source["certificate"]["coefficients_ascending"],
                                                                           "best_whole_output", run)}
    parents = committed_factor_parents(record, path)
    parent_ids = {}
    retained["factor_parent_outputs"] = []
    for proposal, source in sorted(parents.items()):
        certificate = compact_whole(source["certificate"])
        witness_id = witnesses.add(certificate["coefficients_ascending"], "factor_parent_whole_output", run)
        parent_ids[proposal] = witness_id
        retained["factor_parent_outputs"].append({"proposal": proposal, "elapsed": source["elapsed"],
                                                  "certificate": certificate, "witness_id": witness_id})
    for field, role in FACTOR_COLLECTIONS:
        retained[field] = []
        for source in record.get(field, []):
            item = copy.deepcopy(source)
            parent = parents[item["proposal"]]
            association = {key: value for key, value in source.items() if key != "proposal"}
            assert association in parent["factor_associations"]
            factor = next(factor for factor in parent["certificate"]["factors"]
                          if factor["coefficients_ascending"] == item["coefficients_ascending"])
            assert factor["thresholds"] == item["thresholds"]
            item["certificate"] = compact_factor(factor)
            item["elapsed"] = parent["elapsed"]
            item["factor_witness_id"] = witnesses.add(item["coefficients_ascending"], role, run)
            item["parent_witness_id"] = parent_ids[item["proposal"]]
            retained[field].append(item)
    retained["source_summary"] = path.name
    row.update(retained)


def build_exports(label, allow_partial=False):
    paths = live.run_paths(label)
    if not paths:
        raise ValueError("no live-control run summaries found")
    if len(paths) != 15 and not allow_partial:
        raise ValueError("expected all 15 run summaries; explicit --allow-partial is needed to preserve a partial control")
    comparison = live.report(label)
    indexed = {}
    for path in paths:
        record = read_json(path)
        config = record["configuration"]
        assert config["protocol"] == live.PROTOCOL
        key = (config["variant"], config["seed"])
        assert key not in indexed
        indexed[key] = (record, path)
    witnesses = Witnesses()
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            record, path = indexed[(row["arm"], row["seed"])]
            retain_run(row, record, path, witnesses)
    comparison["retained_run_count"] = len(paths)
    comparison["retention_role"] = (
        "Observed live-control summaries, exact counts, timing, configuration, compact whole/best/unresolved certificates, "
        "separate factor outcomes and their committed parent outputs. Whole/factor root certificates can be recomputed "
        "from the exact witnesses; the wall-clock prefix, counts and first-hit times are preserved observations. "
        "Partial or failed controls retain their original validity and cannot establish a passing screen.")
    witness_document = witnesses.document(label)
    validate_references(comparison, witness_document)
    return comparison, witness_document


def validate_references(comparison, witness_document):
    entries = witness_document["witnesses"]
    by_id = {item["witness_id"]: item["coefficients_ascending"] for item in entries}
    assert len(by_id) == len(entries) == len({tuple(item["coefficients_ascending"]) for item in entries})
    used = set()
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            whole_items = row["whole_discoveries"] + row["unresolved_value_equalities"] + row["factor_parent_outputs"]
            if row.get("best_certified_positive"):
                whole_items.append(row["best_certified_positive"])
            for item in whole_items:
                assert by_id[item["witness_id"]] == item["certificate"]["coefficients_ascending"]
                used.add(item["witness_id"])
            parent_ids = {item["proposal"]: item["witness_id"] for item in row["factor_parent_outputs"]}
            for field, _ in FACTOR_COLLECTIONS:
                for item in row[field]:
                    assert by_id[item["factor_witness_id"]] == item["coefficients_ascending"]
                    assert item["parent_witness_id"] == parent_ids[item["proposal"]]
                    used.add(item["factor_witness_id"])
    assert used == set(by_id)


def write_exports(label, comparison_path, witnesses_path, allow_partial=False):
    comparison_path, witnesses_path = Path(comparison_path), Path(witnesses_path)
    if comparison_path.resolve() == witnesses_path.resolve():
        raise ValueError("comparison and witnesses need different destinations")
    if comparison_path.exists() or witnesses_path.exists():
        raise FileExistsError("preserve existing retained data; use explicit fresh destinations")
    comparison, witnesses = build_exports(label, allow_partial)
    # Complete and validate both payloads before publishing either destination.
    payloads = [(comparison_path, json.dumps(comparison, indent=2) + "\n"),
                (witnesses_path, json.dumps(witnesses, indent=2) + "\n")]
    for path, payload in payloads:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload, encoding="utf-8")
    return comparison, witnesses


def self_test(label, short_label, failure_label):
    results = []
    for role, source_label in (("short", short_label), ("failed", failure_label)):
        comparison_path = live.OUTPUT / f"{label}_{role}_comparison.json"
        witnesses_path = live.OUTPUT / f"{label}_{role}_witnesses.json"
        comparison, witnesses = write_exports(source_label, comparison_path, witnesses_path, True)
        assert read_json(comparison_path) == comparison and read_json(witnesses_path) == witnesses
        assert not comparison["complete_declared_live_control"] and not comparison["allocation_screen_passes"]
        for group in comparison["groups"]:
            for row in group["all_seed_outcomes"]:
                source = read_json(live.OUTPUT / row["source_summary"])
                special = {field for field, _ in WHOLE_COLLECTIONS + FACTOR_COLLECTIONS} | {"best_certified_positive"}
                for key, value in source.items():
                    if key not in special:
                        assert row[key] == value
                for field, _ in WHOLE_COLLECTIONS:
                    assert len(row[field]) == len(source.get(field, []))
                    for item, original in zip(row[field], source.get(field, [])):
                        assert item["certificate"] == compact_whole(original["certificate"])
                        assert all(item[key] == value for key, value in original.items() if key != "certificate")
                if source.get("best_certified_positive"):
                    assert row["best_certified_positive"]["certificate"] == compact_whole(source["best_certified_positive"]["certificate"])
                for field, _ in FACTOR_COLLECTIONS:
                    assert len(row[field]) == len(source.get(field, []))
                    for item, original in zip(row[field], source.get(field, [])):
                        assert all(item[key] == value for key, value in original.items())
        if role == "short":
            assert comparison["retained_run_count"] == 3
        else:
            assert comparison["retained_run_count"] == 1 and not witnesses["witnesses"]
            failed_row = next(row for group in comparison["groups"] for row in group["all_seed_outcomes"])
            assert failed_row["termination_reason"] == "worker_failure" and not failed_row["valid_run"]
            assert failed_row["first_target_hit_censored_at"] == failed_row["observed_run_seconds"] < failed_row["budget_seconds"]
        results.append({"control": role, "runs_retained": comparison["retained_run_count"],
                        "witness_arrays": len(witnesses["witnesses"]),
                        "factor_parent_outputs": sum(len(row["factor_parent_outputs"]) for group in comparison["groups"] for row in group["all_seed_outcomes"]),
                        "comparison_file": comparison_path.name, "witness_file": witnesses_path.name})
    return {"passed": True, "controls": results,
            "checks": ["source observation fields preserved exactly", "whole/best/unresolved compact fields retained",
                       "factor associations checked against committed parent events", "exact witness arrays deduplicated",
                       "all witness references resolved", "failure validity and observed censor preserved",
                       "no partial-control pass or old-pilot path enumeration"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export")
    export.add_argument("--label", required=True)
    export.add_argument("--comparison", type=Path, default=HERE / "inputs" / "prior_live_comparison.json")
    export.add_argument("--witnesses", type=Path, default=HERE / "inputs" / "prior_live_witnesses.json")
    export.add_argument("--allow-partial", action="store_true")
    check = commands.add_parser("self-test")
    check.add_argument("--label", required=True)
    check.add_argument("--short-label", default="live_checks_257")
    check.add_argument("--failure-label", default="live_checks_failure")
    args = parser.parse_args()
    if args.command == "self-test":
        result = self_test(args.label, args.short_label, args.failure_label)
        live.frozen.write_json(live.OUTPUT / f"{args.label}_checks.json", result)
        print(json.dumps(result))
    else:
        comparison, witnesses = write_exports(args.label, args.comparison, args.witnesses, args.allow_partial)
        print(json.dumps({"retained_runs": comparison["retained_run_count"],
                          "complete_declared_live_control": comparison["complete_declared_live_control"],
                          "witness_arrays": len(witnesses["witnesses"])}))


if __name__ == "__main__":
    main()
