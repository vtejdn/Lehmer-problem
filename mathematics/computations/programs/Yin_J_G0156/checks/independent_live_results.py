"""Reconstruct the completed 15-run S10 live control without new sampling.

Original journals and summaries are required for the proposal-level checks.
Optional native inputs are compared with those observations and fresh complete
polynomial certificates; generated results stay in the same J output home.
"""

import argparse
from collections import Counter, OrderedDict
import itertools
import json
from pathlib import Path
import statistics
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import prior_strength_live as live
from independent_live_review import exact_update, probabilities
from independent_pilot_review import Ledger, bounds, check_thresholds, compact, factor_core, overlap, subset_equal

THRESHOLDS = ("6/5", "5/4", "13/10", "7/5")


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def reconstruct(path, summary, *, protocol=live.PROTOCOL, degree=14, seeds=range(5, 10),
                variants=("fixed", "O", "A"), validity_function=live.live_validity,
                eligibility_field="eligible_live_comparison_run"):
    from fractions import Fraction

    config = summary["configuration"]
    variant, seed = config["variant"], config["seed"]
    required = {"protocol": protocol, "degree": degree, "arm": variant, "seconds": 10,
                "max_proposals": 0, "precision_bits": 128, "ranking_radius": "1e-12", "batch_size": 256,
                "cache_size": 4096, "cache_policy": "per-run exact-polynomial LRU; no shared cache",
                "controlled_failure_check": False, "law_class": live.law_class(variant).__name__,
                "implementation_arm": live.base_arm(variant)}
    assert all(config[key] == value for key, value in required.items())
    assert variant in variants and seed in seeds
    assert config["pair_prior_total"] == (1 if variant == "A" else 81 if variant == "O" else None)
    assert config["singleton_prior_total"] == (9 if variant != "fixed" and (degree // 2) % 2 else None)
    supervision = summary["supervision"]
    assert not summary.get("worker_failure", False) and supervision["stderr"] == ""
    assert supervision["killed_at_cap"] and supervision["supervisor_elapsed_seconds"] >= 10
    validity = validity_function(summary)
    assert validity == {"valid_run": True, "termination_reason": "deadline", "observed_run_seconds": 10,
                        eligibility_field: True}
    assert all(summary[key] == value for key, value in validity.items())
    law = live.law_class(variant)(degree // 2, live.base_arm(variant), seed)
    exact_probabilities = probabilities(law)
    counts, costs, raw, distinct, factor_distinct = (Counter() for _ in range(5))
    cache, seen, cores, target_cores = OrderedDict(), set(), set(), set()
    ledger, factor_ledger = Ledger(), Ledger()
    discoveries, equalities, factor_discoveries, factor_equalities, batch = [], [], [], [], []
    proposal = evaluation = first = best = None
    completed = proposed = on_time_proposals = updates = 0
    last_time, truncated, saw_config = 0, False, False
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                assert not stream.read(), "only a truncated final record is allowed"
                truncated = True
                break
            kind = event["kind"]
            if kind == "config":
                assert not saw_config and event == config
                saw_config = True
            elif kind == "proposal":
                assert saw_config and proposed == completed
                proposed += 1
                assert event["proposal"] == proposed and event["elapsed"] >= last_time
                free = event["free_coefficients"]
                assert len(free) == degree // 2 and all(type(value) is int and -4 <= value <= 4 for value in free)
                assert law.draw() == free, (path.name, proposed, "proposal law replay")
                on_time_proposals += event["elapsed"] <= 10
                proposal, evaluation = event, None
            elif kind == "evaluation":
                assert evaluation is None and event["proposal"] == proposal["proposal"]
                evaluation = event
            elif kind == "commit":
                assert proposal["proposal"] == evaluation["proposal"] == event["proposal"] == completed + 1
                assert last_time <= proposal["elapsed"] <= event["elapsed"] <= 10
                completed, last_time = completed + 1, event["elapsed"]
                e, free = evaluation, tuple(proposal["free_coefficients"])
                assert "unresolved_error" not in e
                assert e["repeated_proposal"] == (free in seen)
                seen.add(free)
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
                assert e["repeated_positive_core"] == (not e["neutral"] and core in cores)
                if not e["neutral"]:
                    cores.add(core)
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
                    update = law.update(batch)
                    assert update == e["update"]
                    if variant != "fixed":
                        exact_probabilities = exact_update(law.blocks, exact_probabilities,
                                                           update["elite_free_coefficients"],
                                                           Fraction(1, 81) if variant == "A" else Fraction(1))
                        assert probabilities(law) == exact_probabilities
                        updates += 1
                    batch.clear()
                else:
                    assert e["update"] is None
                cert = e.get("certificate")
                if cert:
                    assert cert["coefficients_ascending"] == [1, *free, *free[-2::-1], 1]
                    for key in ("core_coefficients_ascending", "thresholds", "neutral", "ranking_resolved", "log_score"):
                        assert cert[key] == e[key]
                    assert cert["root_count_with_multiplicity"] == degree and cert["precision_bits"] == 128
                    check_thresholds(cert)
                identity = None
                if any(value == "below" for value in e["thresholds"].values()):
                    assert cert is not None
                    identity = ledger.add(cert)
                assert e["discovery"] == identity
                if identity and identity["status"] == "new_separated_value":
                    discoveries.append({"proposal": completed, "elapsed": last_time, **identity, "certificate": cert})
                    for threshold in THRESHOLDS:
                        distinct[threshold] += e["thresholds"][threshold] == "below"
                elif identity and identity["status"] == "unresolved_equality":
                    equalities.append({"proposal": completed, **identity, "certificate": cert})
                if e["thresholds"]["6/5"] == "below":
                    target_cores.add(core)
                    if first is None:
                        first = {"proposal": completed, "elapsed": last_time, "free_coefficients": list(free),
                                 "certificate": cert}
                if e["is_new_best"]:
                    assert cert is not None and not e["neutral"] and e["ranking_resolved"]
                    assert best is None or bounds(cert)[1] < bounds(best["certificate"])[0]
                    best = {"proposal": completed, "elapsed": last_time, "certificate": cert}
                expected_factors = []
                if cert:
                    for factor in cert["factors"]:
                        if factor["cyclotomic"] or not any(value == "below" for value in factor["thresholds"].values()):
                            continue
                        factor_cert = {**factor, "core_coefficients_ascending": factor_core(factor["coefficients_ascending"])}
                        check_thresholds(factor_cert)
                        factor_identity = factor_ledger.add(factor_cert)
                        item = {"coefficients_ascending": factor["coefficients_ascending"], "thresholds": factor["thresholds"],
                                "identity": factor_identity, "whole_output_below_6_5": e["thresholds"]["6/5"] == "below"}
                        expected_factors.append(item)
                        if factor_identity["status"] == "new_separated_value":
                            factor_discoveries.append({"proposal": completed, **item})
                            for threshold in THRESHOLDS:
                                factor_distinct[threshold] += factor["thresholds"][threshold] == "below"
                        elif factor_identity["status"] == "unresolved_equality":
                            factor_equalities.append({"proposal": completed, **item})
                assert e["factor_discoveries"] == expected_factors
            elif kind == "finish":
                assert event["elapsed"] <= 10
            else:
                raise AssertionError(kind)
    assert saw_config
    counts.update({"proposals": on_time_proposals, "completed_proposals": completed,
                   "incomplete_proposals": on_time_proposals - completed, "unique_positive_cores": len(cores)})
    assert counts == Counter(summary["counts"])
    assert dict(costs) == summary["accounted_stage_seconds"] and sum(costs.values()) <= 10
    for counter in (raw, distinct, factor_distinct):
        for threshold in THRESHOLDS:
            counter[threshold] += 0
    rebuilt = {"last_committed_elapsed": last_time, "raw_whole_hits": dict(raw), "distinct_whole_values": dict(distinct),
               "distinct_factor_values_separate": dict(factor_distinct), "whole_discoveries": discoveries,
               "unresolved_value_equalities": equalities, "factor_discoveries_separate": factor_discoveries,
               "unresolved_factor_equalities_separate": factor_equalities, "best_certified_positive": best,
               "first_target_hit_seconds": first["elapsed"] if first else None,
               "first_target_hit_censored_at": None if first else 10,
               "neutral_mass_completed": counts["neutral"] / completed,
               "raw_whole_hit_rates": {key: raw[key] / completed for key in THRESHOLDS},
               "raw_whole_hit_rates_per_proposal": {key: raw[key] / on_time_proposals for key in THRESHOLDS}}
    for key, value in rebuilt.items():
        assert summary[key] == value, (path.name, key)
    return {"variant": variant, "seed": seed, "completed_proposals": completed,
            "incomplete_proposals": on_time_proposals - completed, "proposals_replayed": proposed,
            "exact_updates_checked": updates, "first_target_hit": compact(first),
            "target_cores": [list(core) for core in sorted(target_cores)], "truncated_final_record": truncated}


def statistics_and_screen(comparison, originals):
    rows = [row for group in comparison["groups"] for row in group["all_seed_outcomes"]]
    assert len(rows) == 15 and {(row["arm"], row["seed"]) for row in rows} == set(itertools.product(("fixed", "O", "A"), range(5, 10)))
    for row in rows:
        original = originals[row["arm"], row["seed"]]
        for key in ("valid_run", "termination_reason", "observed_run_seconds", "eligible_live_comparison_run", "counts",
                    "distinct_whole_values", "raw_whole_hits", "first_target_hit_seconds", "first_target_hit_censored_at",
                    "neutral_mass_completed", "supervision"):
            assert row[key] == original[key]
        assert row["budget_seconds"] == 10 and row["max_proposals"] == 0
        assert row["best_measure_ball"] == original["best_certified_positive"]["certificate"]["measure_ball"]
    for group in comparison["groups"]:
        group_rows = group["all_seed_outcomes"]
        assert len(group_rows) == 5 and all(row["arm"] == group["arm"] for row in group_rows)
        for threshold in THRESHOLDS:
            values = [row["distinct_whole_values"][threshold] for row in group_rows]
            assert group["distinct_value_statistics"][threshold] == {"median": statistics.median(values), "range": [min(values), max(values)]}
        hits = [row["first_target_hit_seconds"] for row in group_rows if row["first_target_hit_seconds"] is not None]
        assert group["first_hit_statistics_among_hits"] == ({"median": statistics.median(hits), "range": [min(hits), max(hits)]} if hits else None)
        assert group["censored_no_hit_runs"] == 5 - len(hits)
    matched = []
    for seed in range(5, 10):
        count = {variant: originals[variant, seed]["distinct_whole_values"]["6/5"] for variant in ("fixed", "O", "A")}
        times = {variant: originals[variant, seed]["first_target_hit_seconds"] for variant in ("fixed", "O", "A")}
        improves = count["A"] > count["O"] or (count["A"] == count["O"] > 0 and times["A"] < times["O"])
        matched.append({"seed": seed, "target_counts": count, "first_hit_seconds": times,
                        "A_avoids_loss_to_fixed": count["A"] >= count["fixed"], "A_improves_on_O": improves})
    nonlosses = sum(item["A_avoids_loss_to_fixed"] for item in matched)
    improvements = sum(item["A_improves_on_O"] for item in matched)
    assert matched == comparison["matched_seed_outcomes"]
    assert comparison["complete_declared_live_control"] and not comparison["invalid_or_ineligible_runs"]
    assert comparison["A_nonlosses_to_fixed"] == nonlosses and comparison["A_improvements_on_O"] == improvements
    assert comparison["allocation_screen_passes"] == (nonlosses >= 4 and improvements >= 4)
    assert comparison["experimental_seconds_ceiling_represented"] == 150
    return matched


def verify_witnesses(originals, reconstructed, native_witnesses=None, previous=None):
    selected, retained = {}, []
    for key, original in originals.items():
        for field in ("whole_discoveries", "unresolved_value_equalities"):
            retained.extend(item["certificate"] for item in original[field])
        retained.append(original["best_certified_positive"]["certificate"])
        for field in ("factor_discoveries_separate", "unresolved_factor_equalities_separate"):
            for factor in original[field]:
                selected[tuple(factor["coefficients_ascending"])] = None
    retained.extend(item["first_target_hit"]["certificate"] for item in reconstructed if item["first_target_hit"])
    for certificate in retained:
        selected[tuple(certificate["coefficients_ascending"])] = None
    if native_witnesses:
        for witness in native_witnesses["witnesses"]:
            selected[tuple(witness["coefficients_ascending"])] = None
    previous = previous or {}
    computed = 0
    for coefficients in selected:
        if coefficients in previous:
            selected[coefficients] = previous[coefficients]
        else:
            selected[coefficients] = live.frozen.certify_polynomial(list(coefficients))
            computed += 1
        assert selected[coefficients]["coefficients_ascending"] == list(coefficients)
        assert selected[coefficients]["factorization_product_verified"]
        assert selected[coefficients]["root_count_with_multiplicity"] == len(coefficients) - 1
    for certificate in retained:
        fresh = selected[tuple(certificate["coefficients_ascending"])]
        assert overlap(certificate, fresh)
        for key in ("core_coefficients_ascending", "thresholds", "neutral"):
            assert certificate[key] == fresh[key]
        check_thresholds(certificate)
    for original in originals.values():
        for field in ("factor_discoveries_separate", "unresolved_factor_equalities_separate"):
            for factor in original[field]:
                assert factor["thresholds"] == selected[tuple(factor["coefficients_ascending"])]["thresholds"]
        certificates = [item["certificate"] for item in original["whole_discoveries"]]
        assert len({tuple(cert["core_coefficients_ascending"]) for cert in certificates}) == len(certificates)
        assert all(not overlap(left, right) for index, left in enumerate(certificates) for right in certificates[index + 1:])
    return selected, computed


def verify_native(comparison, native, witnesses, originals, directory, label, certificates,
                  *, protocol=live.PROTOCOL, expected_runs=15):
    subset_equal(comparison, native)
    assert native["retained_run_count"] == expected_runs
    assert witnesses["protocol"] == protocol and witnesses["source_label"] == label
    entries = witnesses["witnesses"]
    by_id = {item["witness_id"]: item for item in entries}
    assert len(by_id) == len(entries) == len(certificates)
    assert {tuple(item["coefficients_ascending"]) for item in entries} == set(certificates)
    used = {}
    whole_fields = ("coefficients_ascending", "core_coefficients_ascending", "measure_interval", "measure_ball",
                    "thresholds", "neutral", "precision_bits", "factorization_product_verified",
                    "root_count_with_multiplicity", "ranking_resolved", "log_score")
    factor_fields = ("coefficients_ascending", "measure_interval", "measure_ball", "thresholds", "degree",
                     "exponent", "root_count", "cyclotomic")

    def reference(witness_id, coefficients, role, run):
        assert by_id[witness_id]["coefficients_ascending"] == coefficients
        record = used.setdefault(witness_id, {"roles": set(), "runs": set()})
        record["roles"].add(role)
        record["runs"].add(run)

    def whole_certificate(retained, source):
        assert retained == {key: source[key] for key in whole_fields}
        fresh = certificates[tuple(retained["coefficients_ascending"])]
        for key in ("core_coefficients_ascending", "thresholds", "neutral"):
            assert retained[key] == fresh[key]
        assert overlap(retained, fresh)
        check_thresholds(retained)

    parent_count = factor_count = 0
    for group in native["groups"]:
        for row in group["all_seed_outcomes"]:
            degree = row.get("degree", 14)
            key = (degree, row["arm"], row["seed"]) if "degree" in row else (row["arm"], row["seed"])
            original = originals[key]
            run = f"{label}_d{degree}_{row['arm']}_s{row['seed']}"
            assert row["source_summary"] == run + ".json"
            special = {"whole_discoveries", "unresolved_value_equalities", "best_certified_positive",
                       "factor_discoveries_separate", "unresolved_factor_equalities_separate"}
            for key, value in original.items():
                if key not in special:
                    assert row[key] == value
            for field, role in (("whole_discoveries", "whole_threshold_value"),
                                ("unresolved_value_equalities", "unresolved_whole_value_equality")):
                assert len(row[field]) == len(original[field])
                for item, source in zip(row[field], original[field]):
                    assert {key: value for key, value in item.items() if key not in ("certificate", "witness_id")} == {
                        key: value for key, value in source.items() if key != "certificate"}
                    whole_certificate(item["certificate"], source["certificate"])
                    reference(item["witness_id"], item["certificate"]["coefficients_ascending"], role, run)
            item, source = row["best_certified_positive"], original["best_certified_positive"]
            assert {key: value for key, value in item.items() if key not in ("certificate", "witness_id")} == {
                key: value for key, value in source.items() if key != "certificate"}
            whole_certificate(item["certificate"], source["certificate"])
            reference(item["witness_id"], item["certificate"]["coefficients_ascending"], "best_whole_output", run)
            wanted = {item["proposal"] for field in ("factor_discoveries_separate", "unresolved_factor_equalities_separate")
                      for item in original[field]}
            parents, pending = {}, None
            with (directory / (run + ".jsonl")).open(encoding="utf-8") as stream:
                for line in stream:
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        break
                    if event["kind"] == "evaluation" and event["proposal"] in wanted:
                        pending = event
                    elif event["kind"] == "commit" and event["proposal"] in wanted:
                        assert pending is not None and pending["proposal"] == event["proposal"] and event["elapsed"] <= 10
                        parents[event["proposal"]] = (event["elapsed"], pending)
                        if set(parents) == wanted:
                            break
            assert set(parents) == wanted
            retained_parents = {item["proposal"]: item for item in row["factor_parent_outputs"]}
            assert len(retained_parents) == len(row["factor_parent_outputs"]) == len(parents)
            assert set(retained_parents) == wanted
            parent_count += len(parents)
            for proposal, item in retained_parents.items():
                elapsed, event = parents[proposal]
                assert item["elapsed"] == elapsed
                whole_certificate(item["certificate"], event["certificate"])
                reference(item["witness_id"], item["certificate"]["coefficients_ascending"], "factor_parent_whole_output", run)
            for field, role in (("factor_discoveries_separate", "separate_irreducible_factor"),
                                ("unresolved_factor_equalities_separate", "unresolved_factor_value_equality")):
                assert len(row[field]) == len(original[field])
                for item, source in zip(row[field], original[field]):
                    factor_count += 1
                    subset_equal(source, item)
                    elapsed, event = parents[item["proposal"]]
                    assert {key: value for key, value in source.items() if key != "proposal"} in event["factor_discoveries"]
                    assert item["elapsed"] == elapsed
                    parent = retained_parents[item["proposal"]]
                    assert item["parent_witness_id"] == parent["witness_id"]
                    source_factor = next(f for f in event["certificate"]["factors"] if f["coefficients_ascending"] == item["coefficients_ascending"])
                    assert item["certificate"] == {**{key: source_factor[key] for key in factor_fields},
                                                   "neutral": source_factor["cyclotomic"],
                                                   "scope": "measure of the single factor; exponent records its multiplicity in the parent"}
                    fresh = certificates[tuple(item["coefficients_ascending"])]
                    assert overlap(item["certificate"], fresh) and item["thresholds"] == fresh["thresholds"]
                    fresh_parent = certificates[tuple(parent["certificate"]["coefficients_ascending"])]
                    fresh_factor = next(f for f in fresh_parent["factors"] if f["coefficients_ascending"] == item["coefficients_ascending"])
                    assert fresh_factor["exponent"] == item["certificate"]["exponent"]
                    assert item["whole_output_below_6_5"] == (parent["certificate"]["thresholds"]["6/5"] == "below")
                    reference(item["factor_witness_id"], item["coefficients_ascending"], role, run)
    assert set(used) == set(by_id)
    for witness_id, selection in used.items():
        assert set(by_id[witness_id]["roles"]) == selection["roles"]
        assert set(by_id[witness_id]["runs"]) == selection["runs"]
    return {"retained_witnesses": len(entries), "factor_parent_outputs": parent_count,
            "factor_associations": factor_count, "all_observations_and_per_run_witness_references_match": True}


def main():
    if not __debug__:
        raise RuntimeError("run without -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", default="s10_prior_live")
    parser.add_argument("--originals", type=Path, default=live.OUTPUT)
    parser.add_argument("--native-comparison", type=Path)
    parser.add_argument("--native-witnesses", type=Path)
    parser.add_argument("--reuse-verification", type=Path,
                        help="reuse an explicitly selected earlier certificate calculation; missing coefficients are certified")
    parser.add_argument("--output", type=Path, default=live.OUTPUT / "independent_live_results_review.json")
    args = parser.parse_args()
    originals, reconstructed = {}, []
    for variant, seed in itertools.product(("fixed", "O", "A"), range(5, 10)):
        base = args.originals / f"{args.label}_d14_{variant}_s{seed}"
        original = read(base.with_suffix(".json"))
        originals[variant, seed] = original
        result = reconstruct(base.with_suffix(".jsonl"), original)
        reconstructed.append(result)
        print(json.dumps({"checked": base.name, "completed": result["completed_proposals"], "updates": result["exact_updates_checked"]}), flush=True)
    comparison = read(args.originals / f"{args.label}_live_comparison.json")
    matched = statistics_and_screen(comparison, originals)
    native = read(args.native_comparison) if args.native_comparison else None
    witnesses = read(args.native_witnesses) if args.native_witnesses else None
    assert (native is None) == (witnesses is None), "provide both native inputs together"
    previous = ({tuple(cert["coefficients_ascending"]): cert for cert in read(args.reuse_verification)["certificates"]}
                if args.reuse_verification else None)
    certificates, computed = verify_witnesses(originals, reconstructed, witnesses, previous)
    write(live.OUTPUT / "independent_live_witness_verification.json", {"kind": "separate_reference_replay", "certificates": list(certificates.values())})
    native_result = verify_native(comparison, native, witnesses, originals, args.originals, args.label, certificates) if native else None
    result = {"scope": "Completed separate live control; exact committed law replay, all summaries and selected complete-measure witnesses",
              "runs_checked": 15, "completed_proposals": sum(row["completed_proposals"] for row in reconstructed),
              "incomplete_proposals": sum(row["incomplete_proposals"] for row in reconstructed),
              "exact_updates_checked": sum(row["exact_updates_checked"] for row in reconstructed),
              "polynomial_certificates_checked": len(certificates), "certificates_computed_this_call": computed,
              "certificates_reused_from_selected_prior_check": len(certificates) - computed, "matched_seed_outcomes": matched,
              "native_comparison_checked": bool(args.native_comparison), "native_witnesses_checked": bool(args.native_witnesses),
              "native_retention": native_result,
              "runs": reconstructed}
    write(args.output, result)
    print(json.dumps({key: value for key, value in result.items() if key not in ("runs", "matched_seed_outcomes")}))


if __name__ == "__main__":
    main()
