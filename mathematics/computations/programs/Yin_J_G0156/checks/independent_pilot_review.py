"""Reproduce the finite-data checks supporting R1111 v3.

The fixed mode needs the three native pilot inputs and a separately generated
sampler.py verify-witnesses result.
It checks observations, certificates and statistics;
it cannot reconstruct timing or every proposal from compact inputs.
The journals mode additionally needs the original 45 pilot JSON/JSONL pairs,
pilot_comparison.json, 15 generated law-mass results and baseline_mass.json.
It streams the journals without proposing or timing a new experiment.
Both modes reuse the previously reviewed certification/law interfaces.
Run with ordinary Python (not -O); python-flint is required by those interfaces.
"""

import argparse
from collections import Counter, OrderedDict
from fractions import Fraction
from functools import reduce
import itertools
import json
import math
from pathlib import Path
import statistics
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from sampler import Law, OUTPUT
from law_mass_diagnostic import target_mass

DEGREES = (14, 18, 20)
ARMS = ("uniform", "fixed", "adaptive")
THRESHOLDS = ("6/5", "5/4", "13/10", "7/5")
CERTIFICATE_FIELDS = ("coefficients_ascending", "core_coefficients_ascending",
                      "measure_interval", "thresholds", "neutral")
IDS = set(itertools.product(DEGREES, ARMS, range(5)))
LEHMER_CORE = [1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1]


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dyadic(pair):
    mantissa, exponent = pair
    assert type(mantissa) is int and type(exponent) is int
    return Fraction(mantissa * 2 ** max(exponent, 0), 2 ** max(-exponent, 0))


def bounds(certificate):
    lo, hi = map(dyadic, certificate["measure_interval"])
    assert lo <= hi
    return lo, hi


def overlap(left, right):
    lo, hi = bounds(left)
    other_lo, other_hi = bounds(right)
    return lo <= other_hi and other_lo <= hi


def check_thresholds(certificate):
    lo, hi = bounds(certificate)
    for threshold in THRESHOLDS:
        status = certificate["thresholds"][threshold]
        if certificate.get("neutral", False):
            assert status == "neutral" and lo <= 1 <= hi
        elif status == "below":
            assert 1 < lo <= hi < Fraction(threshold)
        elif status == "above":
            assert lo >= Fraction(threshold)
        else:
            assert status == "unresolved"


def compact(item):
    if item is None:
        return None
    return {**{key: value for key, value in item.items() if key != "certificate"},
            "certificate": {key: item["certificate"][key] for key in CERTIFICATE_FIELDS}}


def subset_equal(original, retained):
    """The fixed observation adds fields but must preserve every original one."""
    if isinstance(original, dict):
        assert isinstance(retained, dict)
        for key, value in original.items():
            assert key in retained
            subset_equal(value, retained[key])
    elif isinstance(original, list):
        assert isinstance(retained, list) and len(original) == len(retained)
        for left, right in zip(original, retained):
            subset_equal(left, right)
    else:
        assert original == retained, (original, retained)


def rows(comparison):
    return [run for group in comparison["groups"] for run in group["seed_outcomes"]]


def identity(run):
    return run["degree"], run["arm"], run["seed"]


def stem(run):
    return f"pilot_d{run['degree']}_{run['arm']}_s{run['seed']}"


def fixed_check(inputs, verification):
    comparison = read(inputs / "pilot_comparison.json")
    witnesses = read(inputs / "pilot_witnesses.json")["witnesses"]
    laws = read(inputs / "pilot_law_mass.json")["results"]
    runs = rows(comparison)
    assert len(runs) == 45 and {identity(run) for run in runs} == IDS
    assert sum(run["counts"]["completed_proposals"] for run in runs) == 1906599
    assert sum(run["counts"]["incomplete_proposals"] for run in runs) == 43
    assert sum(run["raw_whole_hits"]["6/5"] for run in runs) == 224
    assert comparison["complete_declared_pilot"] and not comparison["invalid_runs"]
    assert comparison["experimental_seconds_ceiling_represented"] == 2700
    verified = read(verification)["certificates"]
    certificates = {tuple(cert["coefficients_ascending"]): cert for cert in verified}
    assert len(certificates) == len(verified) == len(witnesses) == 1331
    assert set(certificates) == {tuple(item["coefficients_ascending"]) for item in witnesses}
    for cert in verified:
        assert cert["factorization_product_verified"] and cert["precision_bits"] == 128
        assert cert["root_count_with_multiplicity"] == len(cert["coefficients_ascending"]) - 1
        check_thresholds(cert)

    selected = {}

    def select(coefficients, role, run):
        item = selected.setdefault(tuple(coefficients), {"roles": set(), "runs": set()})
        item["roles"].add(role)
        item["runs"].add(stem(run))

    def check_certificate(cert):
        fresh = certificates[tuple(cert["coefficients_ascending"])]
        for key in ("core_coefficients_ascending", "thresholds", "neutral"):
            assert cert[key] == fresh[key]
        check_thresholds(cert)
        assert overlap(cert, fresh)
        if cert["thresholds"]["6/5"] == "below":
            assert cert["core_coefficients_ascending"] == LEHMER_CORE

    for run in runs:
        counts = run["counts"]
        completed, proposals = counts["completed_proposals"], counts["proposals"]
        assert run["valid_run"] and run["eligible_full_pilot_run"] and not run["worker_failure"]
        assert run["termination_reason"] == "deadline"
        assert run["budget_seconds"] == run["observed_run_seconds"] == 60
        assert run["max_proposals"] == 0
        supervision = run["supervision"]
        assert supervision["killed_at_cap"] and supervision["stderr"] == ""
        assert supervision["supervisor_elapsed_seconds"] >= 60
        assert completed + counts["incomplete_proposals"] == proposals
        assert counts["cache_hits"] + counts["fresh_completed_evaluations"] == completed
        assert counts["neutral"] + counts["resolved_positive"] == completed
        assert not any(value for key, value in counts.items() if key.startswith("unresolved"))
        assert counts["adaptive_updates"] == (completed // 256 if run["arm"] == "adaptive" else 0)
        assert 0 <= run["last_committed_elapsed"] <= 60
        assert all(cost >= 0 for cost in run["accounted_stage_seconds"].values())
        assert sum(run["accounted_stage_seconds"].values()) <= 60
        assert run["neutral_mass_completed"] == counts["neutral"] / completed
        hit = run["first_target_hit_seconds"]
        assert (hit is None) == (run["raw_whole_hits"]["6/5"] == 0)
        assert run["first_target_hit_censored_at"] == (60 if hit is None else None)
        assert hit is None or 0 <= hit <= 60
        distinct = Counter({threshold: 0 for threshold in THRESHOLDS})
        previous, cores = [], set()
        for index, item in enumerate(run["whole_discoveries"]):
            cert = item["certificate"]
            check_certificate(cert)
            assert item["status"] == "new_separated_value" and item["value_id"] == index
            assert 0 <= item["elapsed"] <= 60 and 1 <= item["proposal"] <= completed
            core = tuple(cert["core_coefficients_ascending"])
            assert core not in cores and all(not overlap(cert, old) for old in previous)
            cores.add(core)
            previous.append(cert)
            for threshold in THRESHOLDS:
                distinct[threshold] += cert["thresholds"][threshold] == "below"
            select(cert["coefficients_ascending"], "whole_threshold_value", run)
        assert dict(distinct) == run["distinct_whole_values"]
        for item in run["unresolved_value_equalities"]:
            check_certificate(item["certificate"])
            assert item["status"] == "unresolved_equality"
            select(item["certificate"]["coefficients_ascending"], "unresolved_whole_value_equality", run)
        if run["best_certified_positive"]:
            cert = run["best_certified_positive"]["certificate"]
            check_certificate(cert)
            assert bounds(cert)[0] > 1
            select(cert["coefficients_ascending"], "best_whole_output", run)
        factor_counts = Counter({threshold: 0 for threshold in THRESHOLDS})
        for field, role in (("factor_discoveries_separate", "separate_irreducible_factor"),
                            ("unresolved_factor_equalities_separate", "unresolved_factor_value_equality")):
            for item in run[field]:
                fresh = certificates[tuple(item["coefficients_ascending"])]
                assert item["thresholds"] == fresh["thresholds"]
                select(item["coefficients_ascending"], role, run)
                if field == "factor_discoveries_separate":
                    assert item["identity"]["status"] == "new_separated_value"
                    for threshold in THRESHOLDS:
                        factor_counts[threshold] += item["thresholds"][threshold] == "below"
        assert dict(factor_counts) == run["distinct_factor_values_separate"]
        for threshold in THRESHOLDS:
            raw = run["raw_whole_hits"][threshold]
            assert distinct[threshold] <= raw <= completed
            assert run["raw_whole_hit_rates"][threshold] == raw / completed
            assert run["raw_whole_hit_rates_per_proposal"][threshold] == raw / proposals

    assert len(selected) == len(witnesses)
    for item in witnesses:
        expected = selected[tuple(item["coefficients_ascending"])]
        assert set(item["roles"]) == expected["roles"]
        assert set(item["runs"]) == expected["runs"]
    for group in comparison["groups"]:
        group_runs = group["seed_outcomes"]
        assert len(group_runs) == 5 and {run["seed"] for run in group_runs} == set(range(5))
        assert all((run["degree"], run["arm"]) == (group["degree"], group["arm"]) for run in group_runs)
        for threshold in THRESHOLDS:
            values = [run["distinct_whole_values"][threshold] for run in group_runs if run["valid_run"]]
            assert group["distinct_value_statistics"][threshold] == {
                "median": statistics.median(values), "range": [min(values), max(values)], "valid_runs": 5}
    matched = []
    for degree in (18, 20):
        seeds = []
        for seed in range(5):
            yields = {run["arm"]: run["distinct_whole_values"]["6/5"] for run in runs
                      if (run["degree"], run["seed"]) == (degree, seed) and run["eligible_full_pilot_run"]}
            assert set(yields) == set(ARMS)
            seeds.append({"seed": seed, "yields": yields,
                          "adaptive_beats_both": all(yields["adaptive"] > yields[a] for a in ("uniform", "fixed")),
                          "adaptive_loses_to_either": any(yields["adaptive"] < yields[a] for a in ("uniform", "fixed"))})
        matched.append({"degree": degree, "matched_seeds": seeds,
                        "wins_against_both": sum(item["adaptive_beats_both"] for item in seeds),
                        "losses_to_either": sum(item["adaptive_loses_to_either"] for item in seeds)})
    assert matched == comparison["held_out_matched_comparisons"]
    screen = any(row["wins_against_both"] >= 4 and other["losses_to_either"] == 0
                 for row, other in (matched, matched[::-1]))
    assert len(laws) == 15 and {(row["degree"], row["seed"]) for row in laws} == set(itertools.product(DEGREES, range(5)))
    law_stats = []
    for row in laws:
        run = next(run for run in runs if identity(run) == (row["degree"], "adaptive", row["seed"]))
        assert row["source_journal"] == stem(run) + ".jsonl"
        assert row["updates_replayed"] == run["counts"]["adaptive_updates"]
        assert row["final_to_initial_ratio_approx"] == row["final_target_mass_approx"] / row["initial_target_mass_approx"]
    for degree in DEGREES:
        values = [row["final_to_initial_ratio_approx"] for row in laws if row["degree"] == degree]
        law_stats.append({"degree": degree, "median": statistics.median(values), "range": [min(values), max(values)]})
    result = {"runs_checked": 45, "native_witnesses_checked_against_separate_certificates": 1331,
              "all_threshold_intervals_and_whole_value_separations_passed": True,
              "export_roles_and_run_memberships_match": True,
              "matched_screen": [{key: value for key, value in row.items() if key != "matched_seeds"} for row in matched],
              "frozen_continuation_screen_passed": screen,
              "target_seed_counts": [{"degree": g["degree"], "arm": g["arm"],
                                      "values": [r["distinct_whole_values"]["6/5"] for r in sorted(g["seed_outcomes"], key=lambda r: r["seed"])]}
                                     for g in comparison["groups"]],
              "post_run_diagnostic_rows_checked": 15, "law_mass_ratio_statistics": law_stats,
              "scope": "Fixed observations and independently generated witness certificates; no original-journal comparison in this mode."}
    return comparison, laws, result


class Ledger:
    """Independent rational-interval reconstruction of conservative value IDs."""

    def __init__(self):
        self.cores, self.values = {}, []

    def add(self, certificate):
        core = tuple(certificate["core_coefficients_ascending"])
        if core in self.cores:
            return {"status": "same_core", "value_id": self.cores[core]}
        overlaps = [index for index, old in enumerate(self.values) if overlap(certificate, old)]
        if overlaps:
            self.cores[core] = None
            return {"status": "unresolved_equality", "overlapping_value_ids": overlaps}
        value_id = len(self.values)
        self.values.append(certificate)
        self.cores[core] = value_id
        return {"status": "new_separated_value", "value_id": value_id}


def factor_core(coefficients):
    coefficients = tuple(coefficients)
    while len(coefficients) > 1:
        divisor = reduce(math.gcd, (i for i, value in enumerate(coefficients) if i and value), 0)
        if divisor <= 1:
            break
        coefficients = coefficients[::divisor]
    degree = len(coefficients) - 1
    opposite = tuple(value * (-1) ** (degree + i) for i, value in enumerate(coefficients))
    return list(min(coefficients[::-1], opposite[::-1])[::-1])


def journal_check(run, original, path, reference, law_row):
    counts, costs, raw, distinct, factor_distinct = (Counter() for _ in range(5))
    cache, seen_proposals, seen_cores = OrderedDict(), set(), set()
    whole_ledger, factor_ledger = Ledger(), Ledger()
    discoveries, equalities, factors, factor_equalities, batch = [], [], [], [], []
    config = law = proposal = evaluation = best = first = None
    last_time, proposed, completed, on_time_proposals, updates = 0, 0, 0, 0, 0
    truncated = False
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                assert stream.read() == "", "only a truncated final record is allowed"
                truncated = True
                break
            kind = event["kind"]
            if kind == "config":
                assert config is None and event == original["configuration"]
                config = event
                assert (config["degree"], config["arm"], config["seed"]) == identity(run)
                required = {"protocol": "S10-first-experiment", "seconds": 60, "max_proposals": 0,
                            "precision_bits": 128, "ranking_radius": "1e-12", "batch_size": 256,
                            "cache_size": 4096, "cache_policy": "per-run exact-polynomial LRU; no shared cache"}
                assert all(config[key] == value for key, value in required.items())
                law = Law(config["degree"] // 2, config["arm"], config["seed"])
                if law_row is not None:
                    targets = next(row for row in reference["results"] if row["degree"] == config["degree"])["target_prefixes"]
                    initial_mass = target_mass(law, targets)
            elif kind == "proposal":
                assert proposed == completed
                proposed += 1
                assert event["proposal"] == proposed and event["elapsed"] >= last_time
                free = event["free_coefficients"]
                assert len(free) == config["degree"] // 2 and all(type(value) is int and -4 <= value <= 4 for value in free)
                on_time_proposals += event["elapsed"] <= 60
                proposal, evaluation = event, None
            elif kind == "evaluation":
                assert event["proposal"] == proposal["proposal"] and evaluation is None
                evaluation = event
            elif kind == "commit":
                assert proposal["proposal"] == evaluation["proposal"] == event["proposal"] == completed + 1
                assert last_time <= proposal["elapsed"] <= event["elapsed"] <= 60
                last_time, completed = event["elapsed"], completed + 1
                e, free = evaluation, tuple(proposal["free_coefficients"])
                assert "unresolved_error" not in e, "this completed pilot reported no numerical errors"
                assert e["repeated_proposal"] == (free in seen_proposals)
                seen_proposals.add(free)
                assert e["cached"] == (free in cache)
                cache[free] = True
                cache.move_to_end(free)
                if len(cache) > 4096:
                    cache.popitem(last=False)
                counts["repeated_proposals"] += e["repeated_proposal"]
                counts["cache_hits"] += e["cached"]
                counts["fresh_completed_evaluations"] += not e["cached"]
                costs.update(e["cost_seconds"])
                core = tuple(e["core_coefficients_ascending"])
                if e["thresholds"]["6/5"] == "below":
                    assert list(core) == LEHMER_CORE
                assert e["repeated_positive_core"] == (not e["neutral"] and core in seen_cores)
                if not e["neutral"]:
                    seen_cores.add(core)
                counts["neutral"] += e["neutral"]
                counts["resolved_positive"] += not e["neutral"] and e["ranking_resolved"]
                counts["unresolved_ranking"] += not e["ranking_resolved"]
                counts["repeated_positive_cores"] += e["repeated_positive_core"]
                counts["adaptive_updates"] += e["update"] is not None
                for threshold in THRESHOLDS:
                    raw[threshold] += e["thresholds"][threshold] == "below"
                    counts["unresolved_threshold_" + threshold] += e["thresholds"][threshold] == "unresolved"
                if not e["neutral"] and e["ranking_resolved"]:
                    batch.append((core, e["log_score"], list(free)))
                if completed % 256 == 0:
                    assert law.update(batch) == e["update"]
                    batch.clear()
                    updates += config["arm"] == "adaptive"
                else:
                    assert e["update"] is None
                cert = e.get("certificate")
                if cert:
                    assert cert["coefficients_ascending"] == [1, *free, *free[-2::-1], 1]
                    for key in ("core_coefficients_ascending", "thresholds", "neutral", "ranking_resolved", "log_score"):
                        assert cert[key] == e[key]
                    assert cert["precision_bits"] == 128 and cert["root_count_with_multiplicity"] == config["degree"]
                    check_thresholds(cert)
                discovery = None
                if any(status == "below" for status in e["thresholds"].values()):
                    assert cert is not None
                    discovery = whole_ledger.add(cert)
                assert e["discovery"] == discovery
                if discovery and discovery["status"] == "new_separated_value":
                    discoveries.append({"proposal": completed, "elapsed": last_time, **discovery, "certificate": cert})
                    for threshold in THRESHOLDS:
                        distinct[threshold] += e["thresholds"][threshold] == "below"
                elif discovery and discovery["status"] == "unresolved_equality":
                    equalities.append({"proposal": completed, **discovery, "certificate": cert})
                if first is None and e["thresholds"]["6/5"] == "below":
                    first = last_time
                if e["is_new_best"]:
                    assert cert is not None and not e["neutral"] and e["ranking_resolved"]
                    assert best is None or bounds(cert)[1] < bounds(best["certificate"])[0]
                    best = {"proposal": completed, "elapsed": last_time, "certificate": cert}
                expected_factors = []
                if cert:
                    for factor in cert["factors"]:
                        if factor["cyclotomic"] or not any(status == "below" for status in factor["thresholds"].values()):
                            continue
                        factor_cert = {**factor, "core_coefficients_ascending": factor_core(factor["coefficients_ascending"])}
                        check_thresholds(factor_cert)
                        factor_identity = factor_ledger.add(factor_cert)
                        item = {"coefficients_ascending": factor["coefficients_ascending"], "thresholds": factor["thresholds"],
                                "identity": factor_identity, "whole_output_below_6_5": e["thresholds"]["6/5"] == "below"}
                        expected_factors.append(item)
                        if factor_identity["status"] == "new_separated_value":
                            factors.append({"proposal": completed, **item})
                            for threshold in THRESHOLDS:
                                factor_distinct[threshold] += factor["thresholds"][threshold] == "below"
                        elif factor_identity["status"] == "unresolved_equality":
                            factor_equalities.append({"proposal": completed, **item})
                assert expected_factors == e["factor_discoveries"]
            elif kind == "finish":
                assert event["elapsed"] <= 60
            else:
                raise AssertionError(f"unknown event kind {kind}")
    assert config is not None
    counts.update({"proposals": on_time_proposals, "completed_proposals": completed,
                   "incomplete_proposals": on_time_proposals - completed, "unique_positive_cores": len(seen_cores)})
    assert counts == Counter(original["counts"])
    assert dict(costs) == original["accounted_stage_seconds"]
    for threshold in THRESHOLDS:
        raw[threshold] += 0
        distinct[threshold] += 0
        factor_distinct[threshold] += 0
    rebuilt = {"last_committed_elapsed": last_time, "raw_whole_hits": dict(raw), "distinct_whole_values": dict(distinct),
               "distinct_factor_values_separate": dict(factor_distinct), "whole_discoveries": discoveries,
               "unresolved_value_equalities": equalities, "factor_discoveries_separate": factors,
               "unresolved_factor_equalities_separate": factor_equalities, "best_certified_positive": best,
               "first_target_hit_seconds": first, "first_target_hit_censored_at": 60 if first is None else None}
    for key, value in rebuilt.items():
        assert value == original[key], (path.name, key)
    if law_row is not None:
        final_mass = target_mass(law, targets)
        assert law_row["updates_replayed"] == updates
        assert law_row["initial_target_mass_approx"] == initial_mass
        assert law_row["final_target_mass_approx"] == final_mass
        assert law_row["final_to_initial_ratio_approx"] == final_mass / initial_mass
    return {"degree": run["degree"], "arm": run["arm"], "seed": run["seed"], "completed": completed,
            "incomplete": on_time_proposals - completed, "target_distinct": distinct["6/5"],
            "truncated_final_record": truncated, "all_fields_matched": True, "law_diagnostic_matched": law_row is not None}


def journals_check(comparison, laws, directory, reference_path):
    subset_equal(read(directory / "pilot_comparison.json"), comparison)
    reference = read(reference_path)
    results = []
    for run in rows(comparison):
        base = directory / stem(run)
        original = read(base.with_suffix(".json"))
        for key in ("counts", "supervision", "accounted_stage_seconds", "last_committed_elapsed", "raw_whole_hits",
                    "distinct_whole_values", "raw_whole_hit_rates", "raw_whole_hit_rates_per_proposal", "neutral_mass_completed",
                    "first_target_hit_seconds", "first_target_hit_censored_at", "distinct_factor_values_separate",
                    "factor_discoveries_separate", "unresolved_factor_equalities_separate", "valid_run",
                    "termination_reason", "observed_run_seconds", "eligible_full_pilot_run"):
            assert run[key] == original[key]
        assert not original.get("worker_failure", False)
        for key in ("whole_discoveries", "unresolved_value_equalities"):
            assert run[key] == [compact(item) for item in original[key]]
        assert run["best_certified_positive"] == compact(original["best_certified_positive"])
        assert run["best_measure_ball"] == original["best_certified_positive"]["certificate"]["measure_ball"]
        law_row = None
        if run["arm"] == "adaptive":
            law_row = next(row for row in laws if (row["degree"], row["seed"]) == (run["degree"], run["seed"]))
            generated = read(base.with_suffix(".law_mass.json"))
            assert law_row == {key: value for key, value in generated.items() if key != "points"}
        result = journal_check(run, original, base.with_suffix(".jsonl"), reference, law_row)
        results.append(result)
        print(json.dumps({"checked_journal": base.name, "completed": result["completed"]}), flush=True)
    return {"runs_checked": len(results), "total_completed": sum(row["completed"] for row in results),
            "native_observations_match_original": True, "all_metrics_rebuilt_from_journals": True,
            "adaptive_law_rows_replayed": sum(row["law_diagnostic_matched"] for row in results), "runs": results}


def main():
    if not __debug__:
        raise RuntimeError("run without -O so the exact checks remain active")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("fixed", "journals"))
    parser.add_argument("--inputs", type=Path, default=HERE / "inputs")
    parser.add_argument("--verification", type=Path, default=OUTPUT / "independent_pilot_witness_verification.json")
    parser.add_argument("--originals", type=Path, default=OUTPUT)
    parser.add_argument("--reference", type=Path, default=OUTPUT / "baseline_mass.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    comparison, laws, result = fixed_check(args.inputs, args.verification)
    if args.mode == "journals":
        result = journals_check(comparison, laws, args.originals, args.reference)
    destination = args.output or OUTPUT / ("independent_pilot_summary_check.json" if args.mode == "fixed"
                                            else "independent_pilot_journal_check.json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"mode": args.mode, "runs_checked": result["runs_checked"], "output": str(destination)}))


if __name__ == "__main__":
    main()
