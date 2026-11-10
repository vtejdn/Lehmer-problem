"""Independent R1111v9 reconstruction of the completed archive comparison.

Requires the thirty original journals/summaries, compact native inputs, and the
separate exact-input witness recertification.  Replays deterministic laws and
checks exact products, intervals, associations and the frozen screen.  Starts no
sampling worker, changes no author input, and performs no root calculations.
"""

import argparse
from collections import Counter, OrderedDict
import copy
from fractions import Fraction
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import archive_sampling as live
import archive_sampling_export as export
from flint import fmpz_poly
from independent_archive_review import ReferenceLaw, sparse
from independent_pilot_review import Ledger, bounds, check_thresholds, factor_core, overlap

LABEL = "s10_archive_comparison"
THRESHOLDS = ("6/5", "5/4", "13/10", "7/5")
WHOLE_FIELDS = ("coefficients_ascending", "core_coefficients_ascending", "measure_interval", "measure_ball",
                "thresholds", "neutral", "precision_bits", "factorization_product_verified",
                "root_count_with_multiplicity", "ranking_resolved", "log_score")
FACTOR_FIELDS = ("coefficients_ascending", "measure_interval", "measure_ball", "thresholds", "degree",
                 "exponent", "root_count", "cyclotomic")
EXTRA = ("nonseed_discoveries", "unresolved_nonseed_equalities", "strictly_below_seed_values",
         "whole_target_core_observations")


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def compact(certificate):
    return {key: certificate[key] for key in WHOLE_FIELDS if key in certificate}


def certificate_structure(certificate):
    """Check exact factor product/core, root multiplicities and rational bounds."""
    coefficients = certificate["coefficients_ascending"]
    assert all(type(value) is int for value in coefficients) and coefficients[-1] == 1
    assert certificate["precision_bits"] == 128 and certificate["factorization_product_verified"]
    whole, core, root_count = fmpz_poly([1]), fmpz_poly([1]), 0
    for factor in certificate["factors"]:
        polynomial = fmpz_poly(factor["coefficients_ascending"])
        exponent = factor["exponent"]
        assert type(exponent) is int and exponent > 0
        assert polynomial.degree() == factor["degree"] == factor["root_count"]
        assert bool(polynomial.is_cyclotomic()) == factor["cyclotomic"]
        whole *= polynomial**exponent
        root_count += factor["root_count"] * exponent
        if factor["cyclotomic"]:
            assert factor["roots"] == [] and bounds(factor) == (Fraction(1), Fraction(1))
        else:
            core *= polynomial**exponent
            assert sum(root["multiplicity"] for root in factor["roots"]) == factor["degree"]
            assert all(type(root["multiplicity"]) is int and root["multiplicity"] > 0 for root in factor["roots"])
            assert all(root["region"] in ("inside", "outside", "meets_one") for root in factor["roots"])
        check_thresholds({**factor, "neutral": factor["cyclotomic"]})
    assert list(map(int, whole)) == coefficients
    assert root_count == len(coefficients) - 1 == certificate["root_count_with_multiplicity"]
    assert factor_core(list(map(int, core))) == certificate["core_coefficients_ascending"]
    assert certificate["neutral"] == (core.degree() == 0)
    check_thresholds(certificate)


def generated_record(core, state, degree, variant):
    construction = live.closure.generate(core, degree, 4)[1] if variant == "closure" else None
    return {"core_coefficients_ascending": list(core),
            "generated_templates": [list(prefix) for prefix in state["generated"]],
            "construction_counts": construction}


def state_counts(state):
    return {"generated_template_count": len(state["generated"]),
            "observed_template_count": len(state["observed"]),
            "observed_nongenerated_template_count": len(set(state["observed"]) - set(state["generated"])),
            "distinct_template_count": len(state["templates"])}


def compact_generated(item, degree, variant):
    expected = copy.deepcopy(item)
    prefixes = expected.pop("generated_templates")
    expected["generated_template_count"] = len(prefixes)
    expected["generated_template_reproduction"] = {
        "source": "cyclotomic_closure.py:generate" if variant == "closure" else "archive_sampling.py:sparse_completions",
        "degree": degree, "height": 4, "input": "core_coefficients_ascending in this object",
        "order": "lexicographically sorted distinct free prefixes"}
    return expected


def reconstruct(path, summary, catalog):
    config = summary["configuration"]
    degree, variant, seed = config["degree"], config["variant"], config["seed"]
    assert degree in (24, 30) and variant in ("fixed", "direct", "closure") and seed in range(20, 25)
    required = {"protocol": live.PROTOCOL, "arm": variant, "seconds": 20.0, "max_proposals": 0,
                "precision_bits": 128, "ranking_radius": "1e-12", "batch_size": 256,
                "cache_size": 4096, "cache_policy": "per-run exact-polynomial LRU; no shared cache",
                "controlled_failure_check": False, "law_class": "ArchiveLaw", "implementation_arm": "fixed",
                "seed_is_discovery": False, "supplied_seed_core_coefficients_ascending": list(live.SEED_CORE)}
    assert all(config[key] == value for key, value in required.items())
    assert all(config[key] == value for key, value in live.configuration(degree, variant, seed).items())
    assert summary["local_catalog"]["cores"] == list(catalog.values())
    assert summary["local_catalog"]["source"] == "inputs/degree_core_mass_states.json"
    supervision = summary["supervision"]
    assert not summary.get("worker_failure", False) and supervision["stderr"] == ""
    assert supervision["killed_at_cap"] and supervision["supervisor_elapsed_seconds"] >= 20
    for key, value in {"valid_run": True, "termination_reason": "deadline", "observed_run_seconds": 20,
                       "eligible_archive_comparison_run": True}.items():
        assert summary[key] == value
    reference = ReferenceLaw(degree, variant, seed)
    ledger, factors, seeded = Ledger(), Ledger(), Ledger()
    counters = [Counter() for _ in range(6)]
    counts, costs, raw, distinct, factor_distinct, metrics = counters
    seen, cores, observed_cores, below_cores, cache = set(), set(), set(), set(), OrderedDict()
    discoveries, equalities, factor_discoveries, factor_equalities = [], [], [], []
    nonseed, uncertain, below_seed, observations, changes = [], [], [], [], []
    initial = seed_certificate = None
    init_time = last_time = 0
    proposal = evaluation = best = first = first_nonseed = first_seed = None
    proposed = on_time = completed = 0
    target_calls = 0
    parents, targets, certificate_examples = {}, {}, {}
    wanted_parents = {item["proposal"] for field in ("factor_discoveries_separate", "unresolved_factor_equalities_separate")
                      for item in summary[field]}
    truncated, saw_config, transition = False, False, None
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                assert not stream.read(), "only a truncated final event is permitted"
                truncated = True
                break
            kind = event["kind"]
            if kind == "config":
                assert not saw_config and event == config
                saw_config = True
            elif kind == "archive_initialization_started":
                assert saw_config and initial is None and event["elapsed"] >= config["worker_setup_seconds"]
            elif kind == "archive_initialization":
                assert initial is None
                initial, seed_certificate = event, event["seed_certificate"]
                certificate_structure(seed_certificate)
                assert seed_certificate["coefficients_ascending"] == list(live.SEED_CORE)
                assert seed_certificate["thresholds"]["6/5"] == "below"
                assert seeded.add(seed_certificate) == {"status": "new_separated_value", "value_id": 0}
                archive = event["initial_archive"]
                assert archive == (generated_record(live.SEED_CORE, reference.states[live.SEED_CORE], degree, variant)
                                   if variant != "fixed" else None)
                assert all(value >= 0 for value in initial["cost_seconds"].values())
            elif kind == "archive_initialization_commit":
                assert initial is not None and 0 < event["elapsed"] <= 20 and not init_time
                init_time = last_time = event["elapsed"]
                assert sum(initial["cost_seconds"].values()) <= init_time
            elif kind == "proposal":
                assert init_time and proposed == completed
                proposed += 1
                assert event["proposal"] == proposed and last_time <= event["elapsed"]
                prefix, metadata = reference.draw()
                assert event["free_coefficients"] == prefix and event["sampling"] == metadata
                assert len(prefix) == degree // 2 and all(type(value) is int and -4 <= value <= 4 for value in prefix)
                on_time += event["elapsed"] <= 20
                proposal, evaluation = event, None
            elif kind == "evaluation":
                assert proposal is not None and evaluation is None and event["proposal"] == proposed
                evaluation = event
            elif kind == "commit":
                assert proposal is not None and evaluation is not None and event["proposal"] == proposed == completed + 1
                assert last_time <= proposal["elapsed"] <= event["elapsed"] <= 20
                completed, last_time = proposed, event["elapsed"]
                e, prefix = evaluation, tuple(proposal["free_coefficients"])
                assert "unresolved_error" not in e, "this dataset is claimed to contain no committed arithmetic failures"
                assert e["repeated_proposal"] == (prefix in seen)
                seen.add(prefix)
                assert e["cached"] == (prefix in cache)
                cache[prefix] = True
                cache.move_to_end(prefix)
                if len(cache) > 4096:
                    cache.popitem(last=False)
                counts["repeated_proposals"] += e["repeated_proposal"]
                counts["cache_hits"] += e["cached"]
                counts["fresh_completed_evaluations"] += not e["cached"]
                assert all(value >= 0 for value in e["cost_seconds"].values())
                if e["cached"]:
                    assert all(e["cost_seconds"][key] == 0 for key in ("factorization", "normalization", "root_certification"))
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
                assert e["update"] is None
                for threshold, status in e["thresholds"].items():
                    raw[threshold] += status == "below"
                    counts["unresolved_threshold_" + threshold] += status == "unresolved"
                cert = e.get("certificate")
                if cert:
                    coefficients = [1, *prefix, *prefix[-2::-1], 1]
                    assert cert["coefficients_ascending"] == coefficients
                    for key in ("core_coefficients_ascending", "thresholds", "neutral", "ranking_resolved", "log_score"):
                        assert cert[key] == e[key]
                    assert cert["root_count_with_multiplicity"] == degree and cert["precision_bits"] == 128
                    check_thresholds(cert)
                    certificate_examples.setdefault(tuple(coefficients), cert)
                identity = ledger.add(cert) if any(status == "below" for status in e["thresholds"].values()) else None
                assert e["discovery"] == identity
                if identity and identity["status"] == "new_separated_value":
                    discoveries.append({"proposal": completed, "elapsed": last_time, **identity, "certificate": cert})
                    for threshold in THRESHOLDS:
                        distinct[threshold] += e["thresholds"][threshold] == "below"
                elif identity and identity["status"] == "unresolved_equality":
                    equalities.append({"proposal": completed, **identity, "certificate": cert})
                if e["is_new_best"]:
                    assert cert and not e["neutral"] and e["ranking_resolved"]
                    assert best is None or bounds(cert)[1] < bounds(best["certificate"])[0]
                    best = {"proposal": completed, "elapsed": last_time, "certificate": cert}
                expected_factors = []
                if cert:
                    for factor in cert["factors"]:
                        if factor["cyclotomic"] or not any(status == "below" for status in factor["thresholds"].values()):
                            continue
                        factor_cert = {**factor, "core_coefficients_ascending": factor_core(factor["coefficients_ascending"])}
                        check_thresholds(factor_cert)
                        if factor["thresholds"]["6/5"] == "below":
                            assert tuple(factor_cert["core_coefficients_ascending"]) in catalog
                        factor_identity = factors.add(factor_cert)
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
                if completed in wanted_parents:
                    parents[completed] = {"event": e, "elapsed": last_time}
                is_target = e["thresholds"]["6/5"] == "below"
                assert ("seeded_target" in e) == is_target and ("archive_update" in e) == is_target
                if is_target:
                    if first is None:
                        first = last_time
                    target_calls += 1
                    target_identity = seeded.add(cert)
                    is_seed = core == live.SEED_CORE
                    lo, hi = bounds(cert)
                    seed_lo, seed_hi = bounds(seed_certificate)
                    relation = ("same_normalized_seed_core" if is_seed else "strictly_below_seed_enclosure" if hi < seed_lo
                                else "strictly_above_seed_enclosure" if lo > seed_hi else "unresolved_overlap_with_seed")
                    value_id = target_identity.get("value_id")
                    target = {"identity": target_identity, "seed_relation": relation, "seed_recovery": is_seed,
                              "certified_nonseed_value": value_id is not None and value_id > 0,
                              "new_nonseed_value": target_identity["status"] == "new_separated_value" and value_id > 0}
                    assert e["seeded_target"] == target
                    item = {"proposal": completed, "elapsed": last_time, **target, "certificate": cert}
                    metrics["raw_seed_recovery_hits"] += is_seed
                    metrics["raw_certified_nonseed_hits"] += target["certified_nonseed_value"]
                    metrics["raw_unresolved_nonseed_hits"] += not is_seed and not target["certified_nonseed_value"]
                    if is_seed and first_seed is None:
                        first_seed = {"proposal": completed, "elapsed": last_time}
                    if target["new_nonseed_value"]:
                        nonseed.append(item)
                        if first_nonseed is None:
                            first_nonseed = {"proposal": completed, "elapsed": last_time}
                    if target_identity["status"] == "unresolved_equality":
                        uncertain.append(item)
                    if core not in observed_cores:
                        observed_cores.add(core)
                        classification = ("supplied_seed_core" if is_seed else "second_local_core" if core in catalog
                                          else "not_in_supplied_local_catalog")
                        observations.append({**item, "local_classification": classification})
                    if hi < seed_lo and core not in below_cores:
                        below_cores.add(core)
                        below_seed.append(item)
                    targets[prefix] = cert
                    update = e["archive_update"]
                    if variant == "fixed":
                        assert update is None
                    else:
                        new_core = core not in reference.states
                        new_observed = new_core or prefix not in reference.states[core]["observed"]
                        added = new_core or prefix not in reference.states[core]["templates"]
                        reference.observe(core, prefix)
                        state = reference.states[core]
                        if new_core:
                            added = prefix not in state["generated"]
                        expected = {"core_coefficients_ascending": list(core),
                                    "new_core": generated_record(core, state, degree, variant) if new_core else None,
                                    "observed_free_coefficients": list(prefix), "new_observed_template": new_observed,
                                    "added_template": added, **state_counts(state)}
                        assert update == expected
                        metrics["archive_target_update_calls"] += 1
                        if new_core or new_observed:
                            changes.append({"proposal": completed, "elapsed": last_time,
                                            "cost_seconds": e["cost_seconds"]["archive_update"], **update})
                    if (degree, variant, seed, completed) == (24, "closure", 20, 7209):
                        transition = {"proposal": proposal, "evaluation": e, "elapsed": last_time}
            elif kind == "finish":
                assert event["elapsed"] <= 20
            else:
                raise AssertionError(kind)
    assert saw_config and initial and init_time and proposed == completed + 1
    assert set(parents) == wanted_parents
    counts.update({"proposals": on_time, "completed_proposals": completed,
                   "incomplete_proposals": on_time - completed, "unique_positive_cores": len(cores)})
    assert counts == Counter(summary["counts"])
    assert dict(costs) == summary["accounted_stage_seconds"]
    assert sum(costs.values()) + sum(initial["cost_seconds"].values()) <= 20
    for counter in (raw, distinct, factor_distinct):
        for key in THRESHOLDS:
            counter[key] += 0
    for key in ("raw_seed_recovery_hits", "raw_certified_nonseed_hits", "raw_unresolved_nonseed_hits", "archive_target_update_calls"):
        metrics[key] += 0
    metrics["distinct_nonseed_target_values"] = len(nonseed)
    final = [{"core_coefficients_ascending": list(core),
              "generated_templates": [list(prefix) for prefix in state["generated"]],
              "observed_templates": [list(prefix) for prefix in state["observed"]], **state_counts(state)}
             for core, state in reference.states.items()]
    rebuilt = {"last_committed_elapsed": last_time, "raw_whole_hits": dict(raw), "distinct_whole_values": dict(distinct),
               "distinct_factor_values_separate": dict(factor_distinct), "whole_discoveries": discoveries,
               "unresolved_value_equalities": equalities, "factor_discoveries_separate": factor_discoveries,
               "unresolved_factor_equalities_separate": factor_equalities, "best_certified_positive": best,
               "first_target_hit_seconds": first, "first_target_hit_censored_at": None if first is not None else 20,
               "neutral_mass_completed": counts["neutral"] / completed,
               "raw_whole_hit_rates": {key: raw[key] / completed for key in THRESHOLDS},
               "raw_whole_hit_rates_per_proposal": {key: raw[key] / on_time for key in THRESHOLDS},
               "archive_initialization_committed": True, "archive_initialization_elapsed": init_time,
               "archive_initialization": initial, "archive_metrics": dict(metrics), "final_archive": final,
               "committed_archive_changes": changes, "nonseed_discoveries": nonseed,
               "unresolved_nonseed_equalities": uncertain, "strictly_below_seed_values": below_seed,
               "whole_target_core_observations": observations, "first_seed_recovery": first_seed,
               "first_nonseed_hit_seconds": first_nonseed["elapsed"] if first_nonseed else None,
               "first_nonseed_hit_proposal": first_nonseed["proposal"] if first_nonseed else None,
               "first_nonseed_hit_censored_at": None if first_nonseed else 20}
    for key, value in rebuilt.items():
        assert summary[key] == value, (path.name, key)
    assert not summary["counts"]["unresolved_ranking"]
    assert not any(summary["counts"]["unresolved_threshold_" + key] for key in THRESHOLDS)
    return {"degree": degree, "arm": variant, "seed": seed, "proposals_replayed": proposed,
            "completed_proposals": completed, "truncated_final_record": truncated, "counts": dict(counts),
            "metrics": dict(metrics), "archive_changes": len(changes), "target_calls": target_calls,
            "final_archive_counts": [{"core_coefficients_ascending": state["core_coefficients_ascending"],
                                       **{key: value for key, value in state.items() if key.endswith("count")}} for state in final],
            "first_nonseed": first_nonseed, "initialization_elapsed": init_time,
            "stage_seconds": dict(costs), "supervisor_excess": supervision["supervisor_elapsed_seconds"] - 20,
            "last_committed_elapsed": last_time}, parents, targets, certificate_examples, (proposal, evaluation), transition


def verify_native(row, original, parents, targets, last, witnesses, certificates, used):
    degree, variant = row["degree"], row["arm"]
    run = row["source_summary"].removesuffix(".json")
    special = set(EXTRA) | {"whole_discoveries", "unresolved_value_equalities", "best_certified_positive",
                            "factor_discoveries_separate", "unresolved_factor_equalities_separate",
                            "archive_initialization", "final_archive", "committed_archive_changes"}
    for key, value in original.items():
        if key not in special:
            assert row[key] == value, (run, key)

    def reference(witness_id, coefficients, role):
        assert witnesses[witness_id]["coefficients_ascending"] == coefficients
        state = used.setdefault(witness_id, {"roles": set(), "runs": set()})
        state["roles"].add(role)
        state["runs"].add(run)

    def whole(retained, source):
        assert retained == compact(source)
        fresh = certificates[tuple(retained["coefficients_ascending"])]
        assert overlap(retained, fresh)
        for key in ("core_coefficients_ascending", "thresholds", "neutral"):
            assert retained[key] == fresh[key]
        check_thresholds(retained)

    for field, role in [("whole_discoveries", "whole_threshold_value"),
                        ("unresolved_value_equalities", "unresolved_whole_value_equality"), *[(field, field) for field in EXTRA]]:
        assert len(row[field]) == len(original[field])
        for retained, source in zip(row[field], original[field]):
            whole(retained["certificate"], source["certificate"])
            assert {key: value for key, value in retained.items() if key not in ("certificate", "witness_id")} == {
                key: value for key, value in source.items() if key != "certificate"}
            reference(retained["witness_id"], retained["certificate"]["coefficients_ascending"], role)
    if original["best_certified_positive"]:
        retained, source = row["best_certified_positive"], original["best_certified_positive"]
        whole(retained["certificate"], source["certificate"])
        assert retained["proposal"] == source["proposal"] and retained["elapsed"] == source["elapsed"]
        reference(retained["witness_id"], retained["certificate"]["coefficients_ascending"], "best_whole_output")
    initial, source_initial = row["archive_initialization"], original["archive_initialization"]
    whole(initial["seed_certificate"], source_initial["seed_certificate"])
    reference(initial["seed_witness_id"], list(live.SEED_CORE), "supplied_seed_not_discovery")
    assert initial["kind"] == source_initial["kind"] and initial["cost_seconds"] == source_initial["cost_seconds"]
    assert initial["initial_archive"] == (compact_generated(source_initial["initial_archive"], degree, variant)
                                          if source_initial["initial_archive"] else None)
    assert len(row["final_archive"]) == len(original["final_archive"])
    for retained, source in zip(row["final_archive"], original["final_archive"]):
        assert {key: value for key, value in retained.items() if key != "observed_template_witness_ids"} == compact_generated(source, degree, variant)
        assert len(retained["observed_templates"]) == len(retained["observed_template_witness_ids"])
        for prefix, witness_id in zip(retained["observed_templates"], retained["observed_template_witness_ids"]):
            cert = targets[tuple(prefix)]
            reference(witness_id, cert["coefficients_ascending"], "observed_archive_whole_target")
            assert cert["thresholds"]["6/5"] == "below"
    assert len(row["committed_archive_changes"]) == len(original["committed_archive_changes"])
    for retained, source in zip(row["committed_archive_changes"], original["committed_archive_changes"]):
        expected = copy.deepcopy(source)
        if expected["new_core"]:
            expected["new_core"] = compact_generated(expected["new_core"], degree, variant)
        assert retained == expected
    native_parents = {parent["proposal"]: parent for parent in row["factor_parent_outputs"]}
    assert set(native_parents) == set(parents)
    for number, retained in native_parents.items():
        source, elapsed = parents[number]["event"], parents[number]["elapsed"]
        whole(retained["certificate"], source["certificate"])
        assert retained["elapsed"] == elapsed
        for key in ("cost_seconds", "cached", "repeated_proposal"):
            assert retained[key] == source[key]
        assert retained["all_parent_factor_associations"] == source["factor_discoveries"]
        reference(retained["witness_id"], retained["certificate"]["coefficients_ascending"], "factor_parent_whole_output")
    for field, role in (("factor_discoveries_separate", "separate_irreducible_factor"),
                        ("unresolved_factor_equalities_separate", "unresolved_factor_value_equality")):
        assert len(row[field]) == len(original[field])
        for retained, source in zip(row[field], original[field]):
            assert all(retained[key] == value for key, value in source.items())
            parent = native_parents[source["proposal"]]
            event = parents[source["proposal"]]["event"]
            factor = next(factor for factor in event["certificate"]["factors"]
                          if factor["coefficients_ascending"] == source["coefficients_ascending"])
            expected = {key: factor[key] for key in FACTOR_FIELDS}
            expected.update({"neutral": factor["cyclotomic"],
                             "scope": "measure of the single factor; exponent records its multiplicity in the parent"})
            assert retained["certificate"] == expected
            assert retained["parent_witness_id"] == parent["witness_id"] and retained["elapsed"] == parent["elapsed"]
            fresh = certificates[tuple(source["coefficients_ascending"])]
            assert overlap(factor, fresh) and factor["thresholds"] == fresh["thresholds"]
            reference(retained["factor_witness_id"], source["coefficients_ascending"], role)
    assert row["committed_unresolved_inputs"] == []
    assert len(row["incomplete_proposal_inputs"]) == 1
    retry, (proposal, evaluation) = row["incomplete_proposal_inputs"][0], last
    assert retry["proposal"] == proposal["proposal"] and retry["proposal_elapsed"] == proposal["elapsed"]
    assert retry["free_coefficients"] == proposal["free_coefficients"]
    assert retry["coefficients_ascending"] == live.frozen.reciprocal_polynomial(proposal["free_coefficients"])
    assert not retry["committed"] and retry["commit_elapsed"] is None
    assert retry["evaluation_present"] == (evaluation is not None)
    reasons = []
    if evaluation:
        if "unresolved_error" in evaluation:
            reasons.append("unresolved_error")
        if evaluation.get("ranking_resolved") is False:
            reasons.append("unresolved_ranking")
        reasons += ["unresolved_threshold_" + key for key, value in evaluation.get("thresholds", {}).items() if value == "unresolved"]
        fields = ("unresolved_error", "ranking_resolved", "thresholds", "neutral", "core_coefficients_ascending", "cached", "repeated_proposal", "cost_seconds")
        assert retry["evaluation_observations"] == {key: evaluation[key] for key in fields if key in evaluation}
        assert retry["uncommitted_archive_update_present"] == (evaluation.get("archive_update") is not None)
        if "certificate" in evaluation:
            assert retry["certificate"] == compact(evaluation["certificate"])
    assert retry["reasons"] == reasons + ["no_predeadline_commit"]


def screen_and_tables(native, rows):
    by_id = {(row["degree"], row["arm"], row["seed"]): row for row in rows}
    expected_ids = {(degree, arm, seed) for degree in (24, 30) for arm in ("fixed", "direct", "closure") for seed in range(20, 25)}
    assert len(rows) == len(by_id) == 30 and set(by_id) == expected_ids
    screens, tables = [], []
    for degree in (24, 30):
        matched = []
        for seed in range(20, 25):
            selected = {arm: by_id[(degree, arm, seed)] for arm in ("fixed", "direct", "closure")}
            counts = {arm: row["archive_metrics"]["distinct_nonseed_target_values"] for arm, row in selected.items()}
            times = {arm: row["first_nonseed_hit_seconds"] for arm, row in selected.items()}
            wins = {arm: counts["closure"] > counts[arm] or
                    (counts["closure"] == counts[arm] > 0 and times["closure"] < times[arm]) for arm in ("fixed", "direct")}
            matched.append({"seed": seed, "nonseed_target_counts": counts, "first_nonseed_hit_seconds": times,
                            "closure_nonloss": {arm: counts["closure"] >= counts[arm] for arm in ("fixed", "direct")},
                            "closure_improvement": wins, "closure_joint_improvement": all(wins.values())})
        screens.append({"degree": degree, "matched_seed_outcomes": matched,
                        "closure_nonlosses": {arm: sum(row["closure_nonloss"][arm] for row in matched) for arm in ("fixed", "direct")},
                        "closure_joint_improvements": sum(row["closure_joint_improvement"] for row in matched)})
        for arm in ("fixed", "direct", "closure"):
            group = [by_id[(degree, arm, seed)] for seed in range(20, 25)]
            totals = Counter()
            for row in group:
                totals.update(row["counts"])
            tables.append({"degree": degree, "arm": arm, "counts": dict(totals),
                           "nonseed_values": [row["archive_metrics"]["distinct_nonseed_target_values"] for row in group],
                           "first_nonseed_seconds": [row["first_nonseed_hit_seconds"] for row in group],
                           "seed_hits": sum(row["archive_metrics"]["raw_seed_recovery_hits"] for row in group),
                           "nonseed_hits": sum(row["archive_metrics"]["raw_certified_nonseed_hits"] for row in group),
                           "initialization_range": [min(row["archive_initialization_elapsed"] for row in group),
                                                     max(row["archive_initialization_elapsed"] for row in group)]})
    assert native["degree_screens"] == screens
    nonloss = all(value >= 4 for screen in screens for value in screen["closure_nonlosses"].values())
    wins = any(screen["closure_joint_improvements"] >= 3 for screen in screens)
    assert native["complete_declared_archive_comparison"]
    assert native["nonloss_screen_passes_at_both_degrees"] == nonloss
    assert native["joint_improvement_screen_passes_at_one_degree"] == wins
    assert native["allocation_screen_passes"] == (nonloss and wins)
    return screens, tables


def transition_check(transition, catalog):
    assert transition is not None
    event, certificate = transition["proposal"], transition["evaluation"]["certificate"]
    metadata = event["sampling"]
    assert metadata["k"] == 1 and metadata["coordinates"] == [2] and metadata["signs"] == [-1]
    assert not metadata["boundary_return"]
    parent = live.frozen.reciprocal_polynomial(metadata["parent_free_coefficients"])
    child = certificate["coefficients_ascending"]
    expected = [0] * 25
    for power, value in ((0, 1), (10, -1), (12, -1), (14, -1), (24, 1)):
        expected[power] = value
    assert parent == expected
    expected[3] -= 1
    expected[21] -= 1
    assert child == expected
    second = next(core for core in catalog if core != live.SEED_CORE)
    phi3, phi12 = fmpz_poly([1, 1, 1]), fmpz_poly([1, 0, -1, 0, 1])
    lifted = [0] * 21
    for i, value in enumerate(live.SEED_CORE):
        lifted[2 * i] = value * (-1)**i
    assert fmpz_poly(lifted) * phi12 == fmpz_poly(parent)
    assert fmpz_poly(list(second)) * phi3 * phi12 == fmpz_poly(child)
    assert tuple(parent[1:13]) not in sparse(live.SEED_CORE, 24)
    assert tuple(parent[1:13]) in live.closure.generate(live.SEED_CORE, 24, 4)[0]
    assert certificate["core_coefficients_ascending"] == list(second)
    return {"degree": 24, "arm": "closure", "seed": 20, "proposal": 7209,
            "elapsed": transition["elapsed"], "parent_coefficients_ascending": parent,
            "child_coefficients_ascending": child, "coordinate": 2, "sign": -1,
            "two_exact_product_identities": True, "outside_initial_direct_templates": True}


def readme_tables(tables, rows):
    text = (HERE / "readme.md").read_text(encoding="utf-8")
    section = text.split('<a id="archive-comparison-results"></a>', 1)[1].split('<a id="uniform-parent-preparation"></a>', 1)[0]
    observed = []
    for line in section.splitlines():
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if cells and cells[0] in ("24", "30"):
            observed.append(cells)
    assert len(observed) == 12
    by_id = {(item["degree"], item["arm"]): item for item in tables}
    for cells in observed:
        group = by_id[(int(cells[0]), cells[1])]
        if len(cells) == 4:
            assert [int(value.strip()) for value in cells[2].split(",")] == group["nonseed_values"]
            if cells[3] == "all censored":
                assert group["first_nonseed_seconds"] == [None] * 5
            else:
                parsed = [None if value.strip() == "censored" else float(value.strip()) for value in cells[3].split(",")]
                assert parsed == [round(value, 7) if value is not None else None for value in group["first_nonseed_seconds"]]
        else:
            assert len(cells) == 9
            expected = [group["counts"][key] for key in ("completed_proposals", "fresh_completed_evaluations", "cache_hits",
                                                          "repeated_proposals", "neutral")]
            assert list(map(int, cells[2:])) == expected + [group["seed_hits"], group["nonseed_hits"]]
    for row in rows:
        for item in row["nonseed_discoveries"]:
            lo, hi = bounds(item["certificate"])
            stated = Fraction("1.18836814750822358814")
            assert max(abs(stated - lo), abs(stated - hi)) < Fraction(5, 10**21)
    return {"table_rows_checked": len(observed), "target_measure_display_checked": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert not args.output.exists(), "preserve prior review evidence"
    native = read(HERE / "inputs" / "archive_comparison.json")
    document = read(HERE / "inputs" / "archive_witnesses.json")
    verification = read(live.OUTPUT / "archive_witness_verification.json")
    supplied_replay = read(live.OUTPUT / "archive_retained_replay.json")
    assert native["protocol"] == document["protocol"] == live.PROTOCOL
    assert native["label"] == document["source_label"] == LABEL
    assert native["retained_run_count"] == 30 and native["experimental_seconds_ceiling_represented"] == 600
    assert native["degrees"] == [24, 30] and native["seeds"] == list(range(20, 25))
    assert [(group["degree"], group["arm"]) for group in native["groups"]] == [
        (degree, arm) for degree in (24, 30) for arm in ("fixed", "direct", "closure")]
    assert all(row["degree"] == group["degree"] and row["arm"] == group["arm"]
               for group in native["groups"] for row in group["all_seed_outcomes"])
    assert verification["kind"] == "separate_reference_replay"
    entries = document["witnesses"]
    witnesses = {entry["witness_id"]: entry for entry in entries}
    certificates = {tuple(cert["coefficients_ascending"]): cert for cert in verification["certificates"]}
    assert len(witnesses) == len(entries) == len(certificates) == len(verification["certificates"]) == 3386
    assert {tuple(entry["coefficients_ascending"]) for entry in entries} == set(certificates)
    assert [entry["coefficients_ascending"] for entry in entries] == [cert["coefficients_ascending"] for cert in verification["certificates"]]
    for certificate in certificates.values():
        certificate_structure(certificate)
    catalog = live.load_catalog()
    rows = [row for group in native["groups"] for row in group["all_seed_outcomes"]]
    assert len(rows) == len(supplied_replay) == 30
    rebuilt, used, chronology, transition, all_examples = [], {}, [], None, {}
    totals = Counter()
    for index, row in enumerate(rows):
        stem = live.run_stem(LABEL, row["degree"], row["arm"], row["seed"])
        assert row["source_summary"] == stem.with_suffix(".json").name
        original = read(stem.with_suffix(".json"))
        result, parents, targets, examples, last, actual_transition = reconstruct(stem.with_suffix(".jsonl"), original, catalog)
        verify_native(row, original, parents, targets, last, witnesses, certificates, used)
        replay = export.replay_retained_run(row)
        assert replay == supplied_replay[index]
        assert replay["proposals"] == result["proposals_replayed"]
        assert replay["within_budget_proposals"] == row["counts"]["proposals"]
        assert replay["checked_retry_inputs"] == 1 and replay["changes"] == result["archive_changes"]
        rebuilt.append(result)
        all_examples.update(examples)
        transition = actual_transition or transition
        stat = stem.with_suffix(".jsonl").stat()
        chronology.append((stat.st_birthtime, stat.st_mtime, row["degree"], row["arm"], row["seed"]))
        for field in ("whole_discoveries", "factor_discoveries_separate", "unresolved_factor_equalities_separate", "factor_parent_outputs",
                      "committed_archive_changes", "committed_unresolved_inputs", "incomplete_proposal_inputs", *EXTRA):
            totals[field] += len(row[field])
        for item in row["unresolved_factor_equalities_separate"]:
            assert bounds(item["certificate"])[0] > Fraction(13, 10)
        for field in ("factor_discoveries_separate", "unresolved_factor_equalities_separate"):
            for item in row[field]:
                if item["thresholds"]["6/5"] == "below":
                    assert tuple(factor_core(item["coefficients_ascending"])) in catalog
        assert not row["strictly_below_seed_values"] and not row["unresolved_nonseed_equalities"]
        assert all(item["local_classification"] in ("supplied_seed_core", "second_local_core") for item in row["whole_target_core_observations"])
        print(json.dumps({"checked_run": stem.name, "completed": result["completed_proposals"],
                          "logged_proposals": result["proposals_replayed"], "nonseed_values": result["metrics"]["distinct_nonseed_target_values"]}), flush=True)
    assert set(used) == set(witnesses)
    for witness_id, references in used.items():
        assert references["roles"] == set(witnesses[witness_id]["roles"])
        assert references["runs"] == set(witnesses[witness_id]["runs"])
        assert len(references["roles"]) == len(witnesses[witness_id]["roles"])
        assert len(references["runs"]) == len(witnesses[witness_id]["runs"])
    for certificate in all_examples.values():
        certificate_structure(certificate)
    chronology.sort()
    expected_order = []
    arms = ("fixed", "direct", "closure")
    for degree_index, degree in enumerate((24, 30)):
        for seed_index, seed in enumerate(range(20, 25)):
            offset = (degree_index + seed_index) % 3
            expected_order.extend((degree, arm, seed) for arm in arms[offset:] + arms[:offset])
    assert [tuple(item[2:]) for item in chronology] == expected_order
    assert all(left[1] <= right[0] for left, right in zip(chronology, chronology[1:]))
    screens, tables = screen_and_tables(native, rows)
    result = {"scope": "independent actual-evidence review; no new stochastic runs or root calculations",
              "runs": rebuilt, "groups": tables, "screens": screens, "allocation_screen_passes": native["allocation_screen_passes"],
              "totals": dict(totals), "unique_witnesses": len(witnesses), "unique_journal_certificates_checked": len(all_examples),
              "completed_evaluations": sum(row["completed_proposals"] for row in rebuilt),
              "logged_proposals_replayed": sum(row["proposals_replayed"] for row in rebuilt),
              "rotated_serial_order_corresponds_to_original_file_creation_and_finish": True,
              "supervisor_excess_range": [min(row["supervisor_excess"] for row in rebuilt), max(row["supervisor_excess"] for row in rebuilt)],
              "readme_tables": readme_tables(tables, rows),
              "actual_intercore_transition": transition_check(transition, catalog)}
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key not in ("runs", "groups", "actual_intercore_transition")}, indent=2))


if __name__ == "__main__":
    main()
