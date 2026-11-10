"""Retain the D18/20 fixed/A comparison, its observations and exact witnesses.

Only degree_validation.run_paths/report select runs: twenty identities with
seeds 10..14 and protocol S10-degree-validation. Certificate compaction and
committed factor-parent associations reuse the checked live export helpers.
No proposals, factorization, roots or new certificates are computed here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import degree_validation as validation
import prior_strength_live_export as shared

HERE = Path(__file__).resolve().parent


def identity(config):
    return config["degree"], config["variant"], config["seed"]


def build_exports(label, allow_partial=False):
    paths = validation.run_paths(label)
    if not paths:
        raise ValueError("no degree-validation run summaries found")
    expected = {(degree, variant, seed) for degree in validation.DEGREES
                for variant in validation.VARIANTS for seed in validation.SEEDS}
    if len(paths) != len(expected) and not allow_partial:
        raise ValueError("expected all 20 run summaries; explicit --allow-partial is needed to retain a partial control")
    comparison = validation.report(label)
    indexed = {}
    for path in paths:
        record = shared.read_json(path)
        config = record["configuration"]
        key = identity(config)
        if config.get("protocol") != validation.PROTOCOL or key not in expected or key in indexed:
            raise ValueError(f"unexpected protocol or duplicate/foreign run identity: {path.name}")
        if validation.run_stem(label, *key) != path.with_suffix(""):
            raise ValueError(f"run identity differs from summary path: {path.name}")
        indexed[key] = (record, path)
    witnesses = shared.Witnesses()
    represented = set()
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            key = (row["degree"], row["arm"], row["seed"])
            record, path = indexed[key]
            assert key not in represented
            represented.add(key)
            assert record["eligible_degree_validation_run"] == row["eligible_degree_validation_run"]
            first_hit_fields = {name: row[name] for name in ("first_target_hit_proposal", "A_hit_in_initial_batch")}
            shared.retain_run(row, record, path, witnesses)
            assert all(row[name] == value for name, value in first_hit_fields.items())
    assert represented == set(indexed)
    comparison["retained_run_count"] = len(paths)
    comparison["expected_run_count"] = len(expected)
    comparison["missing_run_identities"] = [
        {"degree": degree, "variant": variant, "seed": seed}
        for degree, variant, seed in sorted(expected - represented)]
    comparison["retention_role"] = (
        "Observed D18/20 fixed/A summaries, original counts, times and configuration; compact whole, best and "
        "unresolved certificates; separate factor outcomes and their committed parent outputs; first-hit proposal "
        "and initial-batch fields. Exact witnesses permit certificate replay. Timing prefixes and observed counts "
        "remain retained data. Partial or invalid runs retain their status and cannot establish a passing screen.")
    witness_document = {"protocol": validation.PROTOCOL, "source_label": label,
                        "purpose": "exact replay inputs; verification never adds stochastic discoveries",
                        "witnesses": list(witnesses.by_coefficients.values())}
    shared.validate_references(comparison, witness_document)
    return comparison, witness_document


def write_exports(label, comparison_path, witnesses_path, allow_partial=False):
    comparison_path, witnesses_path = Path(comparison_path), Path(witnesses_path)
    if comparison_path.resolve() == witnesses_path.resolve():
        raise ValueError("comparison and witnesses need different destinations")
    if comparison_path.exists() or witnesses_path.exists():
        raise FileExistsError("preserve existing retained data; use explicit fresh destinations")
    comparison, witnesses = build_exports(label, allow_partial)
    payloads = [(comparison_path, json.dumps(comparison, indent=2) + "\n"),
                (witnesses_path, json.dumps(witnesses, indent=2) + "\n")]
    # Validate both payloads first; exclusive creation also prevents a racing overwrite.
    for path, payload in payloads:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8") as stream:
            stream.write(payload)
    return comparison, witnesses


def check_preserved_fields(comparison):
    special = {field for field, _ in shared.WHOLE_COLLECTIONS + shared.FACTOR_COLLECTIONS} | {"best_certified_positive"}
    original_rows = {(row["degree"], row["arm"], row["seed"]): row
                     for group in validation.report(comparison["label"])["groups"]
                     for row in group["all_seed_outcomes"]}
    for group in comparison["groups"]:
        for row in group["all_seed_outcomes"]:
            source = shared.read_json(validation.OUTPUT / row["source_summary"])
            for key, value in source.items():
                if key not in special:
                    assert row[key] == value
            original_row = original_rows[(row["degree"], row["arm"], row["seed"])]
            for key in ("first_target_hit_proposal", "A_hit_in_initial_batch", "whole_value_observations"):
                assert row[key] == original_row[key]
            for field, _ in shared.WHOLE_COLLECTIONS:
                assert len(row[field]) == len(source.get(field, []))
                for item, original in zip(row[field], source.get(field, [])):
                    assert item["certificate"] == shared.compact_whole(original["certificate"])
                    assert all(item[key] == value for key, value in original.items() if key != "certificate")
            if source.get("best_certified_positive"):
                best, original = row["best_certified_positive"], source["best_certified_positive"]
                assert best["certificate"] == shared.compact_whole(original["certificate"])
                assert all(best[key] == value for key, value in original.items() if key != "certificate")
            for field, _ in shared.FACTOR_COLLECTIONS:
                assert len(row[field]) == len(source.get(field, []))
                for item, original in zip(row[field], source.get(field, [])):
                    assert all(item[key] == value for key, value in original.items())


def self_test(label, short_label, failure_label):
    validation.prior.check_label(label)
    results = []
    for role, source_label, count in (("short", short_label, 4), ("failed", failure_label, 1)):
        try:
            build_exports(source_label)
        except ValueError as error:
            assert "all 20" in str(error)
        else:
            raise AssertionError("partial input accepted without explicit allow_partial")
        comparison_path = validation.OUTPUT / f"{label}_{role}_comparison.json"
        witnesses_path = validation.OUTPUT / f"{label}_{role}_witnesses.json"
        comparison, witnesses = write_exports(source_label, comparison_path, witnesses_path, True)
        assert shared.read_json(comparison_path) == comparison and shared.read_json(witnesses_path) == witnesses
        assert comparison["protocol"] == witnesses["protocol"] == validation.PROTOCOL
        assert comparison["retained_run_count"] == count and len(comparison["missing_run_identities"]) == 20-count
        assert not comparison["complete_declared_degree_validation"] and not comparison["allocation_screen_passes"]
        check_preserved_fields(comparison)
        shared.validate_references(comparison, witnesses)
        assert all(all(type(value) is int for value in item["coefficients_ascending"]) for item in witnesses["witnesses"])
        try:
            write_exports(source_label, comparison_path, witnesses_path, True)
        except FileExistsError:
            assert shared.read_json(comparison_path) == comparison and shared.read_json(witnesses_path) == witnesses
        else:
            raise AssertionError("existing output was overwritten")
        rows = [row for group in comparison["groups"] for row in group["all_seed_outcomes"]]
        if role == "short":
            assert {(row["degree"],row["arm"],row["seed"]) for row in rows} == {
                (degree, variant, 10) for degree in validation.DEGREES for variant in validation.VARIANTS}
            assert all(row["counts"]["completed_proposals"] == 257 for row in rows)
        else:
            assert not witnesses["witnesses"]
            row = rows[0]
            assert row["termination_reason"] == "worker_failure" and not row["valid_run"]
            assert row["first_target_hit_censored_at"] == row["observed_run_seconds"] < row["budget_seconds"]
        results.append({"control":role,"runs_retained":count,"witness_arrays":len(witnesses["witnesses"]),
                        "factor_parent_outputs":sum(len(row["factor_parent_outputs"]) for row in rows),
                        "comparison_file":comparison_path.name,"witness_file":witnesses_path.name})
    return {"passed":True,"controls":results,
            "checks":["degree-specific 20-run identities and protocol", "explicit partial option required",
                      "all original scalar/count/time/configuration fields preserved exactly",
                      "whole/best/unresolved certificates and first-hit proposal/initial-batch fields retained",
                      "factor associations joined to committed whole parents", "exact witness arrays deduplicated",
                      "all witness references resolved", "failed-run validity and actual censor retained",
                      "partial controls cannot pass", "existing destinations cannot be overwritten"],
            "scope":"export bookkeeping only; no sampling or new root certificates"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export")
    export.add_argument("--label", required=True)
    export.add_argument("--comparison", type=Path, default=HERE / "inputs" / "degree_comparison.json")
    export.add_argument("--witnesses", type=Path, default=HERE / "inputs" / "degree_witnesses.json")
    export.add_argument("--allow-partial", action="store_true")
    check = commands.add_parser("self-test")
    check.add_argument("--label", required=True)
    check.add_argument("--short-label", default="degree_checks_257")
    check.add_argument("--failure-label", default="degree_checks_failure")
    args = parser.parse_args()
    if args.command == "self-test":
        result = self_test(args.label, args.short_label, args.failure_label)
        validation.runtime.frozen.write_json(validation.OUTPUT / f"{args.label}_checks.json", result)
        print(json.dumps(result))
    else:
        comparison, witnesses = write_exports(args.label, args.comparison, args.witnesses, args.allow_partial)
        print(json.dumps({"retained_runs":comparison["retained_run_count"],
                          "complete_declared_degree_validation":comparison["complete_declared_degree_validation"],
                          "witness_arrays":len(witnesses["witnesses"])}))


if __name__ == "__main__":
    main()
