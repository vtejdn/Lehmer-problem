"""Independent R1111v12 checks of the fixed ten D56 histories and retention.

No random worker, timed experiment, or Mahler/root solver is started.
The RNG replay uses the separately reviewed finite DP construction; the exact
factorization, metrics and native associations are checked against originals.
Fresh certificate input was produced separately by the responsible main agent.
"""

from collections import Counter, OrderedDict
from datetime import datetime, timezone
from fractions import Fraction
import argparse
import copy
import gzip
import json
from pathlib import Path
import re
import sys
import tempfile

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import independent_primitive_review as ref
import independent_pilot_review as pilot
import independent_archive_results as prior
import primitive_core_sampling as live
import primitive_core_sampling_export as export

OUTPUT = HERE.parent.parent / "outputs" / HERE.name
LABEL = "s10_primitive_core_comparison"
PLAN = [(arm, seed) for j, seed in enumerate(range(30, 35))
        for arm in (("direct", "dp_closure") if j % 2 == 0 else ("dp_closure", "direct"))]
THRESHOLDS = ("6/5", "5/4", "13/10", "7/5")
RESULT_PREFIX = "independent_primitive"


def result_path(name):
    assert name.startswith("independent_primitive_")
    return OUTPUT / (RESULT_PREFIX + name.removeprefix("independent_primitive"))


def save(name, value):
    path = result_path(name)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def originals(arm, seed):
    path = OUTPUT / f"{LABEL}_d56_{arm}_s{seed}.json"
    summary = ref.read(path)
    events, tail = [], None
    with path.with_suffix(".jsonl").open(encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            assert tail is None, "nonfinal malformed journal line"
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                assert not line.endswith("\n"), "malformed completed journal line"
                tail = {"line": number, "characters": len(line)}
    return path, summary, events, tail


def generation_accounting(events, record, replay):
    raw = [e for e in events if e["kind"] == "raw_attempt_result"]
    intents = [e for e in events if e["kind"] == "raw_attempt_intent"]
    tickets = [e for e in events if e["kind"] == "raw_attempt_ticket"]
    calls = [e for e in events if e["kind"] == "parent_call_end"]
    groups = {}
    for e in raw:
        assert e["construction_seconds"] >= 0
        groups.setdefault(e["request"], []).append(e)
    for e in calls:
        group = groups.get(e["request"], [])
        assert e["attempts_started"] == len(group) <= 4096
        assert e["height_rejections"] == sum(not r["accepted"] for r in group)
        assert e["max_attempts"] == 4096
        assert e["construction_seconds"] == sum(r["construction_seconds"] for r in group)
        assert e["last_attempt_seconds"] == (group[-1]["construction_seconds"] if group else None)
        assert e["max_attempt_seconds"] == max((r["construction_seconds"] for r in group), default=0)
        assert e["elapsed_seconds"] >= e["construction_seconds"]
        if e["status"] == "accepted":
            assert group[-1]["accepted"] and sum(r["accepted"] for r in group) == 1
        else:
            assert e["status"] == "deadline" and e["elapsed"] >= 20 and not any(r["accepted"] for r in group)
    counts = {"requests_started": replay["requests"], "journalled_whole_proposals": replay["whole_proposals"],
        "dp_attempt_intents": len(intents), "dp_attempts_with_ticket": len(tickets),
        "dp_attempts_completed": len(raw), "dp_height_rejections": sum(not e["accepted"] for e in raw),
        "dp_accepted_parents": sum(e["accepted"] for e in raw), "dp_attempts_unfinished": len(intents)-len(raw)}
    ref.same(record["generation_counts"], counts)
    assert len(intents) == len(tickets) == len(raw) == replay["raw_attempts"] == replay["completed_raw"]
    assert counts["dp_accepted_parents"] == replay["accepted_raw"]
    accounting = {"completed_raw_construction_seconds_all_journalled": sum(e["construction_seconds"] for e in raw),
        "completed_parent_call_elapsed_seconds_all_journalled": sum(e["elapsed_seconds"] for e in calls),
        "raw_attempt_intents_within_budget": sum(e["elapsed"] <= 20 for e in intents),
        "raw_attempt_results_within_budget": sum(e["elapsed"] <= 20 for e in raw),
        "scope": "construction and parent-call totals overlap; incomplete generation remains charged by the observed run clock"}
    ref.same(record["generation_accounting"], accounting)
    pending = None
    if replay["requests"] > replay["whole_proposals"]:
        assert calls[-1]["status"] == "deadline" and calls[-1]["request"] == replay["requests"]
        pending = {"request": replay["requests"], "observed_phase": "parent_deadline",
            "scope": "deterministic reconstruction of pending input; not an observed completion or discovery"}
    return {"requests_started": replay["requests"], "raw_attempt_intents": len(intents),
        "raw_attempts_completed": len(raw), "accepted_parents": replay["accepted_raw"],
        "height_rejections": counts["dp_height_rejections"], "journalled_whole_proposals": replay["whole_proposals"],
        "raw_tickets_observed": len(tickets), "pending_generation": pending}


def inspect_history(arm, seed):
    path, record, events, tail = originals(arm, seed)
    config = record["configuration"]
    for key, value in live.configuration(56, arm, seed).items():
        ref.same(config[key], value)
    assert config["seconds"] == 20 and config["max_proposals"] == 0
    assert config["controlled_failure_check"] is False and config["online_feedback"] is False
    assert events[0] == config and sum(e["kind"] == "config" for e in events) == 1
    assert all(events[i]["elapsed"] <= events[i+1]["elapsed"] for i in range(len(events)-1))
    supervision = record["supervision"]
    assert supervision["stderr"] == "" and not record.get("worker_failure", False)
    assert supervision["supervisor_elapsed_seconds"] >= 20
    assert supervision["killed_at_cap"] or supervision["worker_returncode"] == 0
    assert record["valid_run"] and record["eligible_primitive_comparison_run"]
    assert record["termination_reason"] == "deadline" and record["observed_run_seconds"] == 20
    assert not record["parent_attempt_limit_stop"]
    init = next(e for e in events if e["kind"] == "initialization")
    seed_c = init["seed_certificate"]
    prior.certificate_structure(seed_c)
    ref.structural_reference(seed_c)
    assert seed_c["coefficients_ascending"] == list(live.SEED_CORE)
    assert seed_c["thresholds"]["6/5"] == "below"
    assert record["initialization_committed"]
    init_commit = next(e for e in events if e["kind"] == "initialization_commit")
    assert 0 < config["elapsed"] < init["elapsed"] < init_commit["elapsed"] < 20
    assert all(v >= 0 for v in init["cost_seconds"].values())
    assert sum(init["cost_seconds"].values()) <= init["elapsed"]
    if arm == "direct":
        ref.same(init["direct_parents"], ref.direct_reference())
        assert init["dp_build"] is None
    else:
        assert init["direct_parents"] == []
        dp = live.ParentSampler(live.SEED_CORE, 56, 4)
        for key, value in dp.build.items():
            if key != "build_seconds":
                ref.same(init["dp_build"][key], value)
    replay = ref.generation_reference(events, config)
    portable = generation_accounting(events, record, replay)
    proposals = {e["proposal"]: e for e in events if e["kind"] == "proposal"}
    commits = {e["proposal"]: e["elapsed"] for e in events if e["kind"] == "commit"}
    assert len(commits) == sum(e["kind"] == "commit" for e in events)
    assert list(proposals) == list(range(1, len(proposals)+1))
    assert list(commits) == list(range(1, len(commits)+1)) and all(t <= 20 for t in commits.values())
    assert all(p["elapsed"] <= 20 for p in proposals.values())
    assert all(max(map(abs, p["coefficients_ascending"])) <= 4 for p in proposals.values())
    whole, primary, broad, factor_ledger = ref.Ledger(seed_c), ref.Ledger(seed_c), pilot.Ledger(), pilot.Ledger()
    seen, cache, positive, first, near_seen = set(), OrderedDict(), set(), {}, set()
    metrics, counts, costs, raw_hits, distinct_hits, factor_hits = [Counter() for _ in range(6)]
    discoveries, factor_discoveries, equality, factor_equality, primary_scopes, near_scopes = [], [], [], [], [], []
    primary_values, primary_equalities, nonseed, targets, below_seed = [], [], [], [], []
    target_cores, below_cores, primary_targets = set(), set(), set()
    best, best_observed, committed_min, minimum = None, None, None, None
    evals, eval_by_id, completed = [], {}, []
    catalog = live.archive.load_catalog()
    for event in events:
        if event["kind"] != "evaluation":
            continue
        proposal = event["proposal"]
        p = proposals[proposal]
        assert event["request"] == p["request"] and event["elapsed"] >= p["elapsed"]
        assert proposal not in eval_by_id
        eval_by_id[proposal] = event
        assert "unresolved_error" not in event, "handle any actual failed certificate explicitly"
        key = tuple(p["free_coefficients"])
        assert event["repeated_proposal"] == (key in seen)
        seen.add(key)
        assert event["cached"] == (key in cache)
        c = event["certificate"]
        assert c["coefficients_ascending"] == p["coefficients_ascending"]
        prior.certificate_structure(c)
        diagnostic = ref.diagnostic_reference(c, p["generation"])
        ref.same(event["diagnostics"], diagnostic)
        if key in cache:
            ref.same(c, cache[key])
            cache.move_to_end(key)
            assert all(event["cost_seconds"][name] == 0 for name in c["cost_seconds"])
            assert event["cost_seconds"]["structure_diagnostic"] == 0
        else:
            cache[key] = c
            if len(cache) > 4096:
                cache.popitem(last=False)
            for name, value in c["cost_seconds"].items():
                assert event["cost_seconds"][name] == value
        assert all(v >= 0 for v in event["cost_seconds"].values())
        core = tuple(c["core_coefficients_ascending"])
        assert event["repeated_positive_core"] == (not c["neutral"] and core in positive)
        if not c["neutral"]:
            positive.add(core)
        for field in ("neutral", "ranking_resolved", "thresholds", "core_coefficients_ascending", "log_score"):
            ref.same(event[field], c[field])
        discovery = broad.add(c) if any(s == "below" for s in c["thresholds"].values()) else None
        target = whole.add(c) if c["thresholds"]["6/5"] == "below" else None
        primary_target = primary.add(c) if target and diagnostic["primary_class"] else None
        ref.same(event["discovery"], discovery)
        ref.same(event["whole_target"], target)
        ref.same(event["primary_target"], primary_target)
        is_best = not c["neutral"] and c["ranking_resolved"] and (best is None or ref.interval(c)[1] < ref.interval(best)[0])
        assert event["is_new_best"] == is_best and event["update"] is None
        if is_best:
            best = c
        is_new = diagnostic["primary_class"] and core not in first
        near = diagnostic["primary_class"] and c["thresholds"]["6/5"] == "above" and c["thresholds"]["13/10"] == "below"
        assert event["primitive_new_coefficient_core"] == is_new
        assert event["primitive_near_miss"] == near
        assert event["primitive_near_miss_new_core"] == (near and core not in near_seen)
        if is_new:
            first[core] = (c, proposal)
            minimum = ref.minimum_reference(first)
        if near:
            near_seen.add(core)
        ref.same(event["primitive_best"], minimum)
        factors = []
        for f in c["factors"]:
            if f["cyclotomic"] or not any(s == "below" for s in f["thresholds"].values()):
                continue
            fc = dict(f, core_coefficients_ascending=ref.normalized(f["coefficients_ascending"]))
            factors.append({"coefficients_ascending": f["coefficients_ascending"], "thresholds": f["thresholds"],
                "identity": factor_ledger.add(fc), "whole_output_below_6_5": c["thresholds"]["6/5"] == "below",
                "strictly_below_seed_enclosure": ref.interval(f)[1] < ref.interval(seed_c)[0],
                "primitive_factor": ref.egcd(f["coefficients_ascending"]) == 1})
        ref.same(event["factor_discoveries"], factors)
        evals.append(event)
        if proposal not in commits:
            assert event["elapsed"] > 20 or event is events[-1]
            continue
        assert p["elapsed"] <= event["elapsed"] <= commits[proposal] <= 20
        completed.append(event)
        scope = {"proposal": proposal, "elapsed": commits[proposal], "branch": p["generation"]["branch"], "certificate": c}
        if is_new:
            primary_scopes.append(scope)
        if event["primitive_near_miss_new_core"]:
            near_scopes.append(scope)
        committed_min = minimum
        metrics["primitive_completed_occurrences"] += diagnostic["primary_class"]
        metrics["primitive_unique_coefficient_cores"] += is_new
        metrics["primitive_near_miss_occurrences"] += near
        metrics["neutral_factor_occurrences"] += diagnostic["cyclotomic_degree"] > 0
        metrics["output_exponent_compression_occurrences"] += diagnostic["output_exponent_gcd"] > 1
        metrics["raw_core_compression_occurrences"] += diagnostic["raw_noncyclotomic_exponent_gcd"] > 1
        metrics["noncyclotomic_reducible_occurrences"] += diagnostic["noncyclotomic_product_reducible"]
        old = diagnostic["parent_neutral"]
        metrics["retained_old_neutral_occurrences"] += old["applicable"] and old["old_neutral_gcd_degree"] > 0
        metrics["additional_neutral_occurrences"] += diagnostic["additional_neutral_degree"] is not None and diagnostic["additional_neutral_degree"] > 0
        metrics["raw_seed_recoveries"] += bool(target and target["seed_recovery"])
        metrics["raw_nonseed_whole_hits"] += bool(target and target["certified_nonseed_value"])
        metrics["primitive_raw_target_hits"] += primary_target is not None
        if target:
            if target["new_nonseed_value"]:
                nonseed.append({**scope, **target})
            if core not in target_cores:
                target_cores.add(core)
                classification = "supplied_seed_core" if core == live.SEED_CORE else "second_local_core" if core in catalog else "not_in_supplied_local_catalog"
                targets.append({**scope, **target, "local_classification": classification})
            if target["seed_relation"] == "strictly_below_seed_enclosure" and core not in below_cores:
                below_cores.add(core)
                below_seed.append(scope)
        if primary_target:
            primary_targets.add(core)
            if primary_target["new_nonseed_value"]:
                primary_values.append({**scope, **primary_target})
            if primary_target["identity"]["status"] == "unresolved_equality":
                primary_equalities.append({**scope, **primary_target})
        counts["repeated_proposals"] += event["repeated_proposal"]
        counts["cache_hits"] += event["cached"]
        counts["fresh_completed_evaluations"] += not event["cached"]
        counts["neutral"] += c["neutral"]
        counts["resolved_positive"] += not c["neutral"] and c["ranking_resolved"]
        counts["unresolved_ranking"] += not c["ranking_resolved"]
        counts["repeated_positive_cores"] += event["repeated_positive_core"]
        counts["adaptive_updates"] += event["update"] is not None
        costs.update(event["cost_seconds"])
        for threshold in THRESHOLDS:
            raw_hits[threshold] += c["thresholds"][threshold] == "below"
            counts["unresolved_threshold_"+threshold] += c["thresholds"][threshold] == "unresolved"
        if discovery and discovery["status"] == "new_separated_value":
            discoveries.append({"proposal": proposal, "elapsed": commits[proposal], **discovery, "certificate": c})
            for threshold in THRESHOLDS:
                distinct_hits[threshold] += c["thresholds"][threshold] == "below"
        if discovery and discovery["status"] == "unresolved_equality":
            equality.append({"proposal": proposal, **discovery, "certificate": c})
        if is_best:
            best_observed = {"proposal": proposal, "elapsed": commits[proposal], "certificate": c}
        for f in factors:
            if f["identity"]["status"] == "new_separated_value":
                factor_discoveries.append({"proposal": proposal, **f})
                for threshold in THRESHOLDS:
                    factor_hits[threshold] += f["thresholds"][threshold] == "below"
            elif f["identity"]["status"] == "unresolved_equality":
                factor_equality.append({"proposal": proposal, **f})
    assert set(commits) <= set(eval_by_id)
    counts.update(proposals=len(proposals), completed_proposals=len(completed), incomplete_proposals=len(proposals)-len(completed),
        unique_positive_cores=len({tuple(e["core_coefficients_ascending"]) for e in completed if not e["neutral"]}))
    metrics.update(primary_distinct_target_values=len(primary_values), whole_distinct_nonseed_target_values=len(nonseed),
        primitive_target_distinct_coefficient_cores=len(primary_targets), primitive_near_miss_distinct_cores=len(near_scopes),
        unique_completed_polynomials=len({tuple(proposals[e["proposal"]]["free_coefficients"]) for e in completed}),
        unique_journalled_proposals=len({tuple(p["free_coefficients"]) for p in proposals.values()}))
    for key, value in record["counts"].items():
        assert counts[key] == value, (arm, seed, key, counts[key], value)
    for key, value in record["primitive_metrics"].items():
        assert metrics[key] == value, (arm, seed, key, metrics[key], value)
    for threshold in THRESHOLDS:
        raw_hits[threshold] += 0
        distinct_hits[threshold] += 0
        factor_hits[threshold] += 0
    for key, value in {"accounted_stage_seconds": dict(costs), "raw_whole_hits": dict(raw_hits),
        "distinct_whole_values": dict(distinct_hits), "distinct_factor_values_separate": dict(factor_hits),
        "whole_discoveries": discoveries, "factor_discoveries_separate": factor_discoveries,
        "unresolved_value_equalities": equality, "unresolved_factor_equalities_separate": factor_equality,
        "best_certified_positive": best_observed, "primitive_coefficient_cores": primary_scopes,
        "primitive_near_miss_cores": near_scopes, "primary_discoveries": primary_values,
        "primary_unresolved_equalities": primary_equalities, "whole_nonseed_discoveries": nonseed,
        "whole_target_core_observations": targets, "strictly_below_seed_whole_values": below_seed}.items():
        ref.same(record[key], value)
    expected_best = {**committed_min, "contenders": [{"proposal": p, "elapsed": commits[p],
        "certificate": eval_by_id[p]["certificate"]} for p in committed_min["contender_proposals"]]} if committed_min else None
    ref.same(record["primitive_best"], expected_best)
    first_hit = next((commits[e["proposal"]] for e in completed if e["thresholds"]["6/5"] == "below"), None)
    assert record["first_target_hit_seconds"] == first_hit
    assert record["first_target_hit_censored_at"] == (20 if first_hit is None else None)
    assert record["first_primary_hit_seconds"] == (primary_values[0]["elapsed"] if primary_values else None)
    assert record["first_primary_hit_censored_at"] == (None if primary_values else 20)
    assert record["first_whole_nonseed_hit_seconds"] == (nonseed[0]["elapsed"] if nonseed else None)
    assert record["last_committed_elapsed"] == max(commits.values())
    for threshold in THRESHOLDS:
        assert record["raw_whole_hit_rates"][threshold] == raw_hits[threshold]/len(completed)
        assert record["raw_whole_hit_rates_per_proposal"][threshold] == raw_hits[threshold]/len(proposals)
    assert record["neutral_mass_completed"] == counts["neutral"]/len(completed)
    # Reviewed admission gate is exercised on each entire original payload as a
    # consistency check, in addition to the independent mathematics above.
    export.validate_journal_evidence(record, path.with_suffix(".jsonl"), events)
    best_c = expected_best["contenders"][0]["certificate"] if expected_best else None
    result = {"arm": arm, "seed": seed, "portable_replay": portable, "counts": dict(counts),
        "primitive_metrics": dict(metrics), "raw_whole_hits": dict(raw_hits),
        "distinct_whole_values": dict(distinct_hits), "factor_values_separate": dict(factor_hits),
        "factor_discoveries": factor_discoveries, "accounted_stage_seconds": dict(costs),
        "generation_accounting": record["generation_accounting"], "initialization_seconds": init["cost_seconds"],
        "minimum": ref.compact_reference(expected_best),
        "minimum_display": float(sum(ref.interval(best_c))/2) if best_c else None,
        "journalled_certificates": len(evals), "incomplete_proposals": sorted(set(proposals)-set(commits)),
        "uncommitted_evaluations": sorted(set(eval_by_id)-set(commits)), "partial_last_line": tail,
        "original_generation_event_count": sum(e["kind"] in export.GENERATION_KINDS for e in events),
        "last_commit": record["last_committed_elapsed"], "supervision": supervision}
    print(json.dumps({k: result[k] for k in ("arm", "seed", "journalled_certificates", "minimum_display", "incomplete_proposals")} ), flush=True)
    return result


class JsonStream:
    """Small incremental JSON reader; supports one nested array row at a time."""
    def __init__(self, stream):
        self.stream, self.buf, self.pos, self.eof = stream, "", 0, False
        self.decoder = json.JSONDecoder()

    def more(self):
        self.buf = self.buf[self.pos:]
        self.pos = 0
        chunk = self.stream.read(1024*1024)
        self.buf += chunk
        self.eof = not chunk

    def peek(self):
        while True:
            while self.pos < len(self.buf) and self.buf[self.pos].isspace():
                self.pos += 1
            if self.pos < len(self.buf):
                return self.buf[self.pos]
            assert not self.eof, "unexpected JSON end"
            self.more()

    def take(self, token):
        assert self.peek() == token, (self.peek(), token)
        self.pos += 1

    def value(self):
        self.peek()
        while True:
            try:
                value, end = self.decoder.raw_decode(self.buf, self.pos)
                if end == len(self.buf) and not self.eof:
                    self.more()
                    continue
                self.pos = end
                return value
            except json.JSONDecodeError:
                assert not self.eof
                self.more()

    def obj(self):
        self.take("{")
        if self.peek() == "}":
            self.take("}")
            return
        while True:
            key = self.value()
            self.take(":")
            yield key
            if self.peek() == "}":
                self.take("}")
                break
            self.take(",")

    def array(self):
        self.take("[")
        if self.peek() == "]":
            self.take("]")
            return
        while True:
            yield None
            if self.peek() == "]":
                self.take("]")
                break
            self.take(",")

    def finish(self):
        assert not self.buf[self.pos:].strip()
        assert not self.stream.read().strip()


def native_checks(history):
    witness_document = ref.read(HERE / "inputs" / "primitive_witnesses.json")
    witnesses = witness_document["witnesses"]
    assert witness_document["protocol"] == live.PROTOCOL and witness_document["source_label"] == LABEL
    by_id = {w["witness_id"]: w for w in witnesses}
    assert len(by_id) == len(witnesses) == len({tuple(w["coefficients_ascending"]) for w in witnesses})
    usage, expectations = {}, {}
    history_by_id = {(r["arm"], r["seed"]): r for r in history["runs"]}
    root_replay = ref.read(OUTPUT / "primitive_retained_replay.json")
    native_order, replay_order = [], []
    total_generation = total_evaluations = 0

    def witness(wid, certificate, role, run, factor=False):
        coeff = certificate["coefficients_ascending"]
        assert by_id[wid]["coefficients_ascending"] == coeff
        entry = usage.setdefault(wid, {"roles": set(), "runs": set()})
        entry["roles"].add(role)
        entry["runs"].add(run)
        expected = {"witness_id": wid, "coefficients_ascending": coeff,
            "core_coefficients_ascending": [1] if factor and certificate["cyclotomic"] else ref.normalized(coeff) if factor else certificate["core_coefficients_ascending"],
            "measure_interval": certificate["measure_interval"], "thresholds": certificate["thresholds"],
            "neutral": certificate["cyclotomic"] if factor else certificate["neutral"]}
        if wid in expectations:
            old = expectations[wid]
            assert all(expected[k] == old[k] for k in expected if k != "measure_interval")
            assert pilot.overlap(expected, old)
        else:
            expectations[wid] = expected

    def row_check(row, arm):
        nonlocal total_generation, total_evaluations
        seed = row["configuration"]["seed"]
        path, original, events, tail = originals(arm, seed)
        assert row["source_summary"] == path.name
        native_order.append((arm, seed))
        expected_summary = ref.compact_reference(original)
        expected_summary["initialization_observation"]["seed_witness_id"] = row["initialization_observation"]["seed_witness_id"]
        for key, value in expected_summary.items():
            ref.same(row[key], value)
        decoded = []
        for values in row["generation_trace"]["rows"]:
            schema = row["generation_trace"]["schemas"][values[0]]
            assert len(values) == len(schema["fields"])+1
            decoded.append(dict(zip(["kind", *schema["fields"]], [schema["kind"], *values[1:]])))
        expected_gen = [e for e in events if e["kind"] in export.GENERATION_KINDS]
        assert len(decoded) == len(expected_gen)
        for left, right in zip(decoded, expected_gen):
            ref.same(left, right)
        total_generation += len(decoded)
        ref.same(row["generation_replay"], history_by_id[arm, seed]["portable_replay"])
        replay_order.append({k: row["generation_replay"][k] for k in ("requests_started", "raw_attempt_intents", "raw_attempts_completed", "journalled_whole_proposals")})
        init = row["initialization_observation"]
        witness(init["seed_witness_id"], init["seed_certificate"], "supplied_seed_not_discovery", path.stem)
        proposals = {e["proposal"]: e for e in events if e["kind"] == "proposal"}
        commits = {e["proposal"]: e["elapsed"] for e in events if e["kind"] == "commit"}
        raw = [e for e in events if e["kind"] == "evaluation"]
        assert len(raw) == len(row["evaluation_observations"])
        for saved, observed in zip(row["evaluation_observations"], raw):
            for key, value in ref.compact_reference(observed).items():
                ref.same(saved[key], value)
            proposal = observed["proposal"]
            committed = proposal in commits and commits[proposal] <= 20
            assert saved["committed"] == committed
            assert saved["excluded_from_yield"] == (not committed or "unresolved_error" in observed)
            assert saved["commit_elapsed"] == commits.get(proposal)
            ref.same(saved["exact_proposal"], proposals[proposal])
            if "certificate" in observed:
                total_evaluations += 1
                c = observed["certificate"]
                witness(saved["whole_witness_id"], c, "completed_whole_certificate" if committed else "uncommitted_whole_certificate_no_yield", path.stem)
                assert len(saved["factor_witness_ids"]) == len(c["factors"])
                for f, wid in zip(c["factors"], saved["factor_witness_ids"]):
                    witness(wid, f, "irreducible_factor_certificate", path.stem, factor=True)
        retry = row["retry_inputs"]
        assert retry["committed_unresolved_inputs"] == []
        incomplete = set(proposals)-set(commits)
        assert {x["proposal"] for x in retry["incomplete_proposal_inputs"]} == incomplete
        indexed = {e["proposal"]: e for e in raw}
        for item in retry["incomplete_proposal_inputs"]:
            proposal = item["proposal"]
            p = proposals[proposal]
            assert item["coefficients_ascending"] == p["coefficients_ascending"]
            assert item["free_coefficients"] == p["free_coefficients"]
            assert item["proposal_elapsed"] == p["elapsed"] and item["commit_elapsed"] is None
            assert item["committed"] is False and item["reasons"] == ["no_predeadline_commit"]
            assert item["evaluation_present"] == (proposal in indexed)
            if proposal in indexed:
                event = indexed[proposal]
                assert not item["uncommitted_archive_update_present"]
                for k, v in item["evaluation_observations"].items():
                    ref.same(event[k], v)
                for k, v in item["certificate"].items():
                    if k in event["certificate"]:
                        ref.same(event["certificate"][k], v)
        print(json.dumps({"native": [arm, seed], "generation_events": len(decoded), "certificates": len(raw)}), flush=True)

    native = HERE / "inputs" / "primitive_comparison.json.gz"
    with gzip.open(native, "rt", encoding="utf-8") as stream:
        reader, meta = JsonStream(stream), {}
        for key in reader.obj():
            if key != "groups":
                meta[key] = reader.value()
                continue
            for _ in reader.array():
                arm = None
                for group_key in reader.obj():
                    if group_key == "arm":
                        arm = reader.value()
                    else:
                        assert group_key == "all_seed_outcomes" and arm is not None
                        for _ in reader.array():
                            row_check(reader.value(), arm)
        reader.finish()
    assert native_order == [(arm, seed) for arm in ("direct", "dp_closure") for seed in range(30,35)]
    ref.same(root_replay, replay_order)
    assert meta["protocol"] == live.PROTOCOL and meta["label"] == LABEL and meta["degree"] == 56
    assert meta["seeds"] == list(range(30,35)) and meta["retained_run_count"] == 10
    assert meta["complete_declared_primitive_comparison"] and meta["experimental_seconds_ceiling_represented"] == 200
    assert set(usage) == set(by_id)
    for wid, use in usage.items():
        assert use["roles"] == set(by_id[wid]["roles"]) and use["runs"] == set(by_id[wid]["runs"])
    size = 0
    with gzip.open(native, "rb") as stream:
        while chunk := stream.read(1024*1024):
            size += len(chunk)
    assert size == 245930042
    # Exercise new I/O on bounded data only; do not regenerate formal evidence.
    sample = {"integer": 2**80, "float": 1.0, "boolean": True, "null": None,
        "absent_is_distinct": {}, "coefficients": [1, -2, 0, 1], "text": "数学\n"}
    payload = json.dumps(sample, separators=(",", ":"))+"\n"
    scratch = HERE.parents[3] / ".tmp"
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="r12_gzip_", dir=scratch) as directory:
        directory = Path(directory)
        for suffix in (".json", ".json.gz"):
            path = directory/("payload"+suffix)
            export.write_native_payload(path, payload)
            ref.same(export.read_native_comparison(path), sample)
            if suffix.endswith("gz"):
                with gzip.open(path, "rb") as stream:
                    assert stream.read() == payload.encode("utf-8")
            else:
                # Path.write_text preserves the existing platform newline
                # behavior; Windows CRLF does not change parsed JSON values.
                assert path.read_text(encoding="utf-8") == payload
    save("independent_primitive_witness_expectations.json", {"source": LABEL,
        "witnesses": [expectations[w["witness_id"]] for w in witnesses]})
    return {"all_original_summary_values_and_scalar_types_preserved": True,
        "generation_events": total_generation, "whole_certificates": total_evaluations,
        "witnesses_all_roles_and_runs_checked": len(witnesses), "decompressed_json_bytes": size,
        "gzip_and_plain_bounded_semantic_roundtrip": True, "root_portable_replay_matches_independent_histories": True,
        "original_plain_byte_equality": "not personally checked: original plain was removed before reviewer release; full retained payload checked against originals"}


def fresh_checks():
    expected = ref.read(result_path("independent_primitive_witness_expectations.json"))["witnesses"]
    checked = same_intervals = 0
    with (OUTPUT / "primitive_witness_verification.json").open(encoding="utf-8") as stream:
        reader = JsonStream(stream)
        for key in reader.obj():
            if key == "kind":
                assert reader.value() == "separate_reference_replay"
            else:
                assert key == "certificates"
                for _ in reader.array():
                    c = reader.value()
                    w = expected[checked]
                    prior.certificate_structure(c)
                    for field in ("coefficients_ascending", "core_coefficients_ascending", "neutral", "thresholds"):
                        ref.same(c[field], w[field])
                    assert pilot.overlap(c, w)
                    same_intervals += c["measure_interval"] == w["measure_interval"]
                    checked += 1
                    if checked % 5000 == 0:
                        print(json.dumps({"fresh_certificate_interfaces_checked": checked}), flush=True)
        reader.finish()
    assert checked == len(expected) == 24425
    return {"fresh_certificates": checked, "ordered_exact_input_and_core_thresholds_match": True,
        "exact_intervals_identical_to_original": same_intervals, "all_intervals_overlap_original": True,
        "root_multiplicities_factor_products_and_cyclotomic_flags_checked": True,
        "reviewer_root_solver_calls": 0}


def wording_checks():
    history = ref.read(result_path("independent_primitive_histories.json"))
    rows = {(r["arm"], r["seed"]): r for r in history["runs"]}
    doc = (HERE / "primitive_core_sampling.md").read_text(encoding="utf-8")
    doc = doc.split('<a id="primitive-comparison-results"></a>', 1)[1]
    table_rows = [line.split("|")[1:-1] for line in doc.splitlines()
        if re.match(r"\| (direct|dp_closure) \| 3[0-4] \|", line)]
    assert len(table_rows) == 10
    for cells in table_rows:
        arm, seed, completed, occurrences, cores, minimum, first = [c.strip() for c in cells]
        r = rows[arm, int(seed)]
        assert [int(completed), int(occurrences), int(cores)] == [r["counts"]["completed_proposals"],
            r["primitive_metrics"]["primitive_completed_occurrences"], r["primitive_metrics"]["primitive_unique_coefficient_cores"]]
        assert f'{r["minimum_display"]:.10f}' == minimum
        assert f'{r["minimum"]["contenders"][0]["elapsed"]:.7f}' == first
        assert r["minimum"]["unique_minimizing_coefficient_core_certified"]
    aggregate = {}
    for arm in ("direct", "dp_closure"):
        selected = [rows[arm, seed] for seed in range(30,35)]
        counts, metrics, costs = Counter(), Counter(), Counter()
        for r in selected:
            counts.update(r["counts"])
            metrics.update(r["primitive_metrics"])
            costs.update(r["accounted_stage_seconds"])
        aggregate[arm] = {"counts": dict(counts), "metrics": dict(metrics), "costs": dict(costs)}
        table = next(line.split("|")[2:-1] for line in doc.splitlines() if line.startswith(f"| {arm} | ") and len(line.split("|")) == 10)
        assert [int(c.strip()) for c in table] == [counts["completed_proposals"], metrics["primitive_completed_occurrences"],
            metrics["primitive_unique_coefficient_cores"], counts["fresh_completed_evaluations"], counts["cache_hits"], counts["neutral"], metrics["raw_seed_recoveries"]]
        assert counts["cache_hits"] == counts["repeated_proposals"]
        assert metrics["primary_distinct_target_values"] == metrics["whole_distinct_nonseed_target_values"] == metrics["primitive_near_miss_occurrences"] == 0
    assert sum(r["portable_replay"]["requests_started"] for r in rows.values()) == 20388
    assert sum(r["portable_replay"]["raw_attempt_intents"] for r in rows.values()) == 383953
    assert sum(r["portable_replay"]["height_rejections"] for r in rows.values()) == 379107
    assert sum(r["portable_replay"]["accepted_parents"] for r in rows.values()) == 4846
    assert sum(r["portable_replay"]["journalled_whole_proposals"] for r in rows.values()) == 20385
    assert sum(r["counts"]["completed_proposals"] for r in rows.values()) == 20378
    assert sum(len(r["incomplete_proposals"]) for r in rows.values()) == 7
    assert sum(r["portable_replay"]["pending_generation"] is not None for r in rows.values()) == 3
    for seed in range(30,35):
        assert ref.interval({"measure_interval": rows["direct", seed]["minimum"]["minimum_measure_enclosure"]})[1] < ref.interval({"measure_interval": rows["dp_closure", seed]["minimum"]["minimum_measure_enclosure"]})[0]
    z, F = ref.fmpz_poly([0,1]), ref.fmpz_poly(list(live.SEED_CORE))
    lifted = [0]*31
    for i, a in enumerate(live.SEED_CORE):
        lifted[3*i] = a*(-1)**i
    direct = ref.fmpz_poly(lifted)*(1+z**26)+z**14*(1+z**3)*(1+z**25)
    dp = F
    for order in (3,4,7,12,15,30,60):
        dp *= ref.fmpz_poly.cyclotomic(order)
    dp += z**28
    witnesses = {w["witness_id"]: w for w in ref.read(HERE/"inputs"/"primitive_witnesses.json")["witnesses"]}
    minima = []
    for arm, seed, proposal, wid, polynomial, low, high in (
        ("direct",34,1074,"w14506",direct,"1.36061074625003","1.36061074625004"),
        ("dp_closure",32,448,"w20305",dp,"1.69514713254698","1.69514713254699")):
        r = rows[arm,seed]
        minimum = r["minimum"]
        assert minimum["selected_witness_proposal"] == proposal
        c = minimum["contenders"][0]["certificate"]
        assert c["coefficients_ascending"] == witnesses[wid]["coefficients_ascending"] == ref.values(polynomial)
        left,right = ref.interval(c)
        assert Fraction(low) < left <= right < Fraction(high)
        assert Fraction(13,10) < left
        for other in range(30,35):
            if other != seed:
                assert right < ref.interval({"measure_interval": rows[arm,other]["minimum"]["minimum_measure_enclosure"]})[0]
        minima.append({"arm":arm,"seed":seed,"proposal":proposal,"witness_id":wid,"display_bracket":[low,high],"exact_formula_agrees":True})
    initial_times, equalities = {"direct":[],"dp_closure":[]}, []
    whole_recoveries = factors_below = 0
    for arm, seed in PLAN:
        path, summary, events, tail = originals(arm, seed)
        initial_times[arm].append(summary["initialization_observation"]["elapsed"])
        assert not summary["primary_unresolved_equalities"] and not summary["unresolved_value_equalities"]
        for item in summary["whole_target_core_observations"]:
            assert item["certificate"]["core_coefficients_ascending"] == list(live.SEED_CORE)
        by_proposal = {e["proposal"]:e for e in events if e["kind"] == "evaluation"}
        committed = {e["proposal"] for e in events if e["kind"] == "commit" and e["elapsed"] <= 20}
        for e in by_proposal.values():
            assert not e.get("unresolved_error")
            for factor in e["factor_discoveries"]:
                assert not factor["strictly_below_seed_enclosure"]
            if e["proposal"] not in committed:
                continue
            if e["whole_target"]:
                whole_recoveries += 1
                assert e["whole_target"]["seed_recovery"]
            assert e["ranking_resolved"] and all(v != "unresolved" for v in e["thresholds"].values())
            for factor in e["certificate"]["factors"]:
                if factor["thresholds"]["6/5"] == "below":
                    assert ref.normalized(factor["coefficients_ascending"]) == list(live.SEED_CORE)
                    factors_below += 1
        for equality in summary["unresolved_factor_equalities_separate"]:
            assert arm == "direct"
            assert equality["thresholds"]["13/10"] == "above" and equality["thresholds"]["7/5"] == "below"
            e = by_proposal[equality["proposal"]]
            f = next(f for f in e["certificate"]["factors"] if f["coefficients_ascending"] == equality["coefficients_ascending"])
            lo,hi = ref.interval(f)
            assert Fraction(13,10) <= lo <= hi < Fraction(7,5)
            equalities.append({"arm":arm,"seed":seed,**equality,"measure_interval":f["measure_interval"]})
    assert whole_recoveries == 223 and len(equalities) == 2
    assert [f'{min(initial_times[a]):.7f}' for a in ("direct","dp_closure")] == ["0.2514032","0.2501314"]
    assert [f'{max(initial_times[a]):.7f}' for a in ("direct","dp_closure")] == ["0.2768719","0.2850354"]
    # Nine actual seed terms, at most two copies and three reciprocal moves.
    assert sum(a != 0 for a in live.SEED_CORE) == 9 and 9*2+2*3 == 24
    return {"ten_table_rows_and_aggregate_tables":True,"aggregates":aggregate,
        "two_minimum_formula_and_bracket_checks":minima,"same_seed_minimum_order":True,
        "whole_seed_recoveries":whole_recoveries,"individual_below_target_factors":factors_below,
        "factor_equalities_outside_target":equalities,"initialization_elapsed":initial_times,
        "support_bound":24,"support_theorem_scope":"existing accepted DS17 statement; positive total log measures only; no new source proof or numerical gap"}


def main():
    global RESULT_PREFIX
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("histories", "native", "fresh", "wording"))
    parser.add_argument("--output-prefix", default=RESULT_PREFIX, help="fresh reviewer-output stem; formal source label stays fixed")
    args = parser.parse_args()
    assert re.fullmatch(r"[A-Za-z0-9_-]+", args.output_prefix)
    RESULT_PREFIX = args.output_prefix
    if args.stage == "histories":
        paths = [OUTPUT / f"{LABEL}_d56_{arm}_s{seed}.jsonl" for arm, seed in PLAN]
        order = sorted(paths, key=lambda p: p.stat().st_birthtime)
        assert order == paths
        assert all(paths[i].stat().st_mtime < paths[i+1].stat().st_birthtime for i in range(9))
        result = {"protocol": live.PROTOCOL, "label": LABEL, "review_utc": datetime.now(timezone.utc).isoformat(),
            "rotated_serial_order": PLAN, "order_evidence": "reviewed serial loop and original local filesystem birth/last-write times; journals contain relative clocks",
            "runs": [inspect_history(arm, seed) for arm, seed in PLAN],
            "distinct_polynomials_independently_exact_factored": len(ref.FACTOR_CACHE),
            "new_stochastic_workers": 0, "reviewer_root_solver_calls": 0}
        save("independent_primitive_histories.json", result)
    elif args.stage == "native":
        result = native_checks(ref.read(result_path("independent_primitive_histories.json")))
        save("independent_primitive_native.json", result)
    elif args.stage == "fresh":
        result = fresh_checks()
        save("independent_primitive_fresh.json", result)
    else:
        result = wording_checks()
        save("independent_primitive_wording.json", result)
    print(json.dumps({"stage": args.stage, "status": "passed"}), flush=True)


if __name__ == "__main__":
    main()
