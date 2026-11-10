"""Independent finite review of the D56 composition and retained controls.

This command reads the two named sets of already executed five-child controls.
It starts no worker and computes no Mahler roots. Exact FLINT factorization,
independent RNG/metric reconstruction and native-payload comparisons are used.
"""

from __future__ import annotations

from collections import Counter, OrderedDict
import argparse
import copy
from fractions import Fraction
from functools import reduce
import json
from math import gcd
from pathlib import Path
import random
import sys
import tempfile
from unittest import mock

from flint import fmpz_poly

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
sys.path.insert(0, str(HERE))
import primitive_core_sampling as live
import primitive_core_sampling_export as export
import primitive_core_sampling_checks as controls

SOURCE_LABEL = "control_primitive_impl_v1"
REVIEW_LABEL = "control_independent_primitive_review"
PLAN = (("direct", 100), ("dp_closure", 101), ("direct", 102), ("dp_closure", 103), ("dp_closure", 104))
FACTOR_CACHE = {}


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def same(left, right):
    assert json.dumps(left, sort_keys=True, separators=(",", ":")) == json.dumps(right, sort_keys=True, separators=(",", ":"))


def values(poly):
    return list(map(int, poly)) or [0]


def egcd(poly):
    return reduce(gcd, (i for i, a in enumerate(poly) if i and a), 0)


def normalized(poly):
    poly = list(poly)
    divisor = egcd(poly)
    if divisor > 1:
        poly = poly[::divisor]
    opposite = [a * (-1)**(len(poly) - 1 + i) for i, a in enumerate(poly)]
    return min(poly[::-1], opposite[::-1])[::-1]


def interval(certificate):
    def endpoint(pair):
        a, e = pair
        return Fraction(a * 2**max(e, 0), 2**max(-e, 0))
    return tuple(endpoint(x) for x in certificate["measure_interval"])


def direct_reference():
    parents = {}
    for k in range(1, 6):
        r = 56 - 10 * k
        neutral = [1] + [0] * (r - 1) + [1]
        for sign in (-1, 1):
            p = [0] * 57
            for i, a in enumerate(live.SEED_CORE):
                p[k * i] += a * sign**i
                p[k * i + r] += a * sign**i
            if max(map(abs, p)) <= 4:
                parents[tuple(p[1:29])] = {"substitution_index": k, "sign": sign,
                    "neutral_coefficients_ascending": neutral, "coefficients_ascending": p}
    return [parents[key] for key in sorted(parents)]


def mutate_reference(parent, rng):
    p = parent["coefficients_ascending"]
    prefix = p[1:29].copy()
    size = rng.randrange(1, 4)
    coordinates = sorted(rng.sample(range(28), size))
    signs = [(-1, 1)[rng.randrange(2)] for _ in coordinates]
    for i, sign in zip(coordinates, signs):
        prefix[i] += sign
    boundary = max(map(abs, prefix)) > 4
    if boundary:
        prefix = p[1:29].copy()
    whole = [1, *prefix, *prefix[-2::-1], 1]
    return prefix, {"mutation_size": size, "coordinates": coordinates, "signs": signs,
        "boundary_return": boundary, "delta_coefficients_ascending": [a-b for a, b in zip(whole, p)]}


def generation_reference(events, config):
    parents = direct_reference()
    dp = live.ParentSampler(live.SEED_CORE, 56, 4)
    rng = random.Random(config["seed"])
    requests = OrderedDict()
    for event in events:
        if event["kind"] in export.GENERATION_KINDS:
            requests.setdefault(event["request"], []).append(event)
    raw = complete_raw = accepted = proposals = 0
    for request, group in requests.items():
        by_kind = {}
        for event in group:
            by_kind.setdefault(event["kind"], []).append(event)
        assert request == list(requests).index(request) + 1
        branch_ticket = rng.randrange(10)
        branch = "uniform_box" if branch_ticket == 0 else config["variant"]
        if "generation_branch" not in by_kind:
            break
        branch_event = by_kind["generation_branch"][0]
        assert (branch_event["branch_ticket"], branch_event["branch"]) == (branch_ticket, branch)
        parent = mutation = None
        if branch == "uniform_box":
            prefix = [rng.randrange(-4, 5) for _ in range(28)]
        elif branch == "direct":
            index = rng.randrange(len(parents))
            if "direct_parent_choice" not in by_kind:
                break
            assert by_kind["direct_parent_choice"][0]["template_index"] == index
            parent = parents[index]
        else:
            tickets = {e["attempt"]: e for e in by_kind.get("raw_attempt_ticket", [])}
            results = {e["attempt"]: e for e in by_kind.get("raw_attempt_result", [])}
            for local, intent in enumerate(by_kind.get("raw_attempt_intent", []), 1):
                raw += 1
                assert (intent["attempt"], intent["request_attempt"]) == (raw, local)
                ticket = rng.randrange(sum(dp.weights))
                residual, k = ticket, 1
                while residual >= dp.weights[k-1]:
                    residual -= dp.weights[k-1]
                    k += 1
                bit = rng.randrange(2)
                rank = rng.randrange(dp.weights[k-1])
                candidate = dp.construct(k, (-1, 1)[bit], rank)
                if raw in tickets:
                    observed = tickets[raw]
                    assert [observed[key] for key in ("substitution_ticket", "substitution_index", "sign_ticket", "sign", "neutral_ticket")] == [ticket, k, bit, (-1, 1)[bit], rank]
                if raw not in results:
                    break
                complete_raw += 1
                for key in ("substitution_index", "sign", "neutral_ticket", "observed_height", "accepted"):
                    assert results[raw][key] == candidate[key]
                if candidate["accepted"]:
                    accepted += 1
                    same(results[raw]["coefficients_ascending"], candidate["coefficients_ascending"])
                    same(results[raw]["neutral_factor_powers"], candidate["neutral_factor_powers"])
                    parent = dict(candidate)
                    lifted = [0] * (10*k + 1)
                    for i, a in enumerate(live.SEED_CORE):
                        lifted[k*i] = a * (-1 if bit == 0 else 1)**i
                    q, r = divmod(fmpz_poly(parent["coefficients_ascending"]), fmpz_poly(lifted))
                    assert not r
                    parent["neutral_coefficients_ascending"] = values(q)
                    assert local == len(by_kind["raw_attempt_intent"])
        if branch != "uniform_box":
            if "parent_ready" in by_kind:
                same(by_kind["parent_ready"][0]["parent"], parent)
            if "mutation_intent" not in by_kind:
                assert "proposal" not in by_kind
                continue
            assert parent is not None
            prefix, mutation = mutate_reference(parent, rng)
        if "proposal" in by_kind:
            proposals += 1
            observed = by_kind["proposal"][0]
            assert observed["proposal"] == proposals and observed["free_coefficients"] == prefix
            assert observed["coefficients_ascending"] == [1, *prefix, *prefix[-2::-1], 1]
            same(observed["generation"], {"status": "proposed", "free_coefficients": prefix,
                "branch": branch, "parent": parent, "mutation": mutation})
    return {"requests": len(requests), "raw_attempts": raw, "completed_raw": complete_raw,
            "accepted_raw": accepted, "whole_proposals": proposals}


def structural_reference(certificate):
    p = certificate["coefficients_ascending"]
    key = tuple(p)
    if key not in FACTOR_CACHE:
        content, exact = fmpz_poly(p).factor()
        assert content == 1
        FACTOR_CACHE[key] = {(tuple(map(int, f)), int(e)) for f, e in exact}
    records = certificate["factors"]
    assert {(tuple(f["coefficients_ascending"]), f["exponent"]) for f in records} == FACTOR_CACHE[key]
    neutral, raw, items, whole = fmpz_poly([1]), fmpz_poly([1]), [], fmpz_poly([1])
    for f in records:
        poly = fmpz_poly(f["coefficients_ascending"])
        assert f["degree"] == int(poly.degree()) and f["cyclotomic"] == bool(poly.is_cyclotomic())
        whole *= poly**f["exponent"]
        if f["cyclotomic"]:
            neutral *= poly**f["exponent"]
        else:
            raw *= poly**f["exponent"]
        items.append({"coefficients_ascending": f["coefficients_ascending"], "degree": f["degree"],
            "multiplicity": f["exponent"], "cyclotomic": f["cyclotomic"],
            "exponent_gcd": egcd(f["coefficients_ascending"]),
            "noncyclotomic_normalization_applicable": not f["cyclotomic"],
            "compressed_sign_normalized_coefficients_ascending": None if f["cyclotomic"] else normalized(f["coefficients_ascending"]),
            "primitive_noncyclotomic_factor": not f["cyclotomic"] and egcd(f["coefficients_ascending"]) == 1})
    assert values(whole) == p
    assert certificate["neutral"] == (int(raw.degree()) == 0)
    assert certificate["core_coefficients_ascending"] == normalized(values(raw))
    irreducible = len(records) == 1 and records[0]["exponent"] == 1
    return {"output_degree": len(p)-1, "output_exponent_gcd": egcd(p), "output_irreducible": irreducible,
        "primary_class": irreducible and not certificate["neutral"] and egcd(p) == 1 and len(p) == 57,
        "cyclotomic_part_coefficients_ascending": values(neutral), "cyclotomic_degree": int(neutral.degree()),
        "raw_noncyclotomic_product_coefficients_ascending": values(raw), "raw_noncyclotomic_degree": int(raw.degree()),
        "raw_noncyclotomic_exponent_gcd": egcd(values(raw)),
        "noncyclotomic_product_reducible": sum(f["exponent"] for f in records if not f["cyclotomic"]) > 1,
        "normalized_whole_core_coefficients_ascending": normalized(values(raw)),
        "normalized_whole_core_degree": len(normalized(values(raw)))-1,
        "normalized_whole_core_irreducibility": "not inferred from this aggregate normalization",
        "individual_irreducible_factors": items}


def diagnostic_reference(certificate, generation):
    result = structural_reference(certificate)
    if generation["parent"] is None:
        result.update(parent_neutral={"applicable": False, "reason": "uniform whole-box branch has no parent"},
                      additional_neutral_coefficients_ascending=None, additional_neutral_degree=None)
        return result
    c = generation["parent"]["neutral_coefficients_ascending"]
    delta = generation["mutation"]["delta_coefficients_ascending"]
    g = fmpz_poly(c).gcd(fmpz_poly(delta))
    assert not fmpz_poly(certificate["coefficients_ascending"]) % g
    extra, remainder = divmod(fmpz_poly(result["cyclotomic_part_coefficients_ascending"]), g)
    assert not remainder
    result.update(parent_neutral={"applicable": True, "neutral_coefficients_ascending": c,
        "delta_coefficients_ascending": delta, "old_neutral_gcd_coefficients_ascending": values(g),
        "old_neutral_gcd_degree": int(g.degree()), "noncyclotomic_degree_upper_bound": 56-int(g.degree())},
        additional_neutral_coefficients_ascending=values(extra), additional_neutral_degree=int(extra.degree()))
    assert result["raw_noncyclotomic_degree"] <= 56-int(g.degree())
    return result


def historical_structure(value):
    value = copy.deepcopy(value)
    for f in value["individual_irreducible_factors"]:
        f["noncyclotomic_normalization_applicable"] = not f["cyclotomic"]
        if f["cyclotomic"]:
            assert f["compressed_sign_normalized_coefficients_ascending"] in ([1], None)
            f["compressed_sign_normalized_coefficients_ascending"] = None
    return value


def certificate_checks(c):
    lo, hi = interval(c)
    assert lo <= hi and c["precision_bits"] == 128 and c["factorization_product_verified"]
    assert c["root_count_with_multiplicity"] == len(c["coefficients_ascending"])-1
    assert sum(f["root_count"] * f["exponent"] for f in c["factors"]) == len(c["coefficients_ascending"])-1
    for factor in c["factors"]:
        assert factor["root_count"] == factor["degree"]
        if not factor["cyclotomic"]:
            assert sum(root["multiplicity"] for root in factor["roots"]) == factor["degree"]
    for key, pair in live.frozen.THRESHOLDS.items():
        limit = Fraction(*pair)
        expected = "neutral" if c["neutral"] else "below" if lo > 1 and hi < limit else "above" if lo >= limit else "unresolved"
        assert c["thresholds"][key] == expected


class Ledger:
    def __init__(self, seed):
        self.seed, self.cores, self.values = seed, {}, []
        self.add(seed)

    def add(self, c):
        core = tuple(c["core_coefficients_ascending"])
        low, high = interval(c)
        if core in self.cores:
            identity = {"status": "same_core", "value_id": self.cores[core]}
        else:
            overlaps = [i for i, old in enumerate(self.values) if not (high < interval(old)[0] or interval(old)[1] < low)]
            if overlaps:
                self.cores[core] = None
                identity = {"status": "unresolved_equality", "overlapping_value_ids": overlaps}
            else:
                self.cores[core] = len(self.values)
                self.values.append(c)
                identity = {"status": "new_separated_value", "value_id": self.cores[core]}
        same_seed = core == tuple(self.seed["core_coefficients_ascending"])
        relation = "same_normalized_seed_core" if same_seed else "strictly_below_seed_enclosure" if high < interval(self.seed)[0] else "strictly_above_seed_enclosure" if low > interval(self.seed)[1] else "unresolved_overlap_with_seed"
        value_id = identity.get("value_id")
        return {"identity": identity, "seed_relation": relation, "seed_recovery": same_seed,
                "certified_nonseed_value": value_id is not None and value_id > 0,
                "new_nonseed_value": identity["status"] == "new_separated_value" and value_id > 0}


def minimum_reference(first):
    if not first:
        return None
    upper = min(interval(c)[1] for c, _ in first.values())
    contenders = [(c, proposal) for c, proposal in first.values() if interval(c)[0] <= upper]
    selected = min(contenders, key=lambda item: (interval(item[0])[1], item[1]))
    lower = min(contenders, key=lambda item: interval(item[0])[0])[0]["measure_interval"][0]
    return {"selected_witness_proposal": selected[1], "contender_proposals": [p for _, p in contenders],
        "minimum_measure_enclosure": [lower, selected[0]["measure_interval"][1]],
        "unique_minimizing_coefficient_core_certified": len(contenders) == 1}


def inspect_run(label, variant, seed):
    path = OUTPUT / f"{label}_d56_{variant}_s{seed}.json"
    record = read(path)
    events = list(export.journal_events(path.with_suffix(".jsonl")))
    replay = generation_reference(events, record["configuration"])
    proposals = {e["proposal"]: e for e in events if e["kind"] == "proposal"}
    commits = {e["proposal"]: e["elapsed"] for e in events if e["kind"] == "commit" and e["elapsed"] <= 2}
    seed_certificate = record["initialization_observation"]["seed_certificate"]
    certificate_checks(seed_certificate)
    whole, primary = Ledger(seed_certificate), Ledger(seed_certificate)
    seen, cache, first, near_seen, primary_targets = set(), OrderedDict(), {}, set(), set()
    metric, evaluations, checked, committed_best = Counter(), [], 0, None
    for event in events:
        if event["kind"] != "evaluation":
            continue
        proposal = event["proposal"]
        p = proposals[proposal]
        key = tuple(p["free_coefficients"])
        assert event["repeated_proposal"] == (key in seen)
        seen.add(key)
        assert event["cached"] == (key in cache)
        if "unresolved_error" in event:
            continue
        c, diagnostic = event["certificate"], diagnostic_reference(event["certificate"], p["generation"])
        certificate_checks(c)
        same(historical_structure(event["diagnostics"]), diagnostic)
        if key in cache:
            cache.move_to_end(key)
            assert all(event["cost_seconds"][name] == 0 for name in c["cost_seconds"])
        else:
            cache[key] = c
            if len(cache) > 4096:
                cache.popitem(last=False)
        core = tuple(c["core_coefficients_ascending"])
        target = whole.add(c) if c["thresholds"]["6/5"] == "below" else None
        main_target = primary.add(c) if target and diagnostic["primary_class"] else None
        same(event["whole_target"], target)
        same(event["primary_target"], main_target)
        is_new = diagnostic["primary_class"] and core not in first
        near = diagnostic["primary_class"] and c["thresholds"]["6/5"] == "above" and c["thresholds"]["13/10"] == "below"
        assert event["primitive_new_coefficient_core"] == is_new
        assert event["primitive_near_miss"] == near and event["primitive_near_miss_new_core"] == (near and core not in near_seen)
        if is_new:
            first[core] = (c, proposal)
        if near:
            near_seen.add(core)
        same(event["primitive_best"], minimum_reference(first))
        checked += 1
        if proposal not in commits:
            continue
        evaluations.append(event)
        committed_best = minimum_reference(first)
        metric["primitive_completed_occurrences"] += diagnostic["primary_class"]
        metric["primitive_unique_coefficient_cores"] += is_new
        metric["primitive_near_miss_occurrences"] += near
        metric["neutral_factor_occurrences"] += diagnostic["cyclotomic_degree"] > 0
        metric["output_exponent_compression_occurrences"] += diagnostic["output_exponent_gcd"] > 1
        metric["raw_core_compression_occurrences"] += diagnostic["raw_noncyclotomic_exponent_gcd"] > 1
        metric["noncyclotomic_reducible_occurrences"] += diagnostic["noncyclotomic_product_reducible"]
        old = diagnostic["parent_neutral"]
        metric["retained_old_neutral_occurrences"] += old["applicable"] and old["old_neutral_gcd_degree"] > 0
        metric["additional_neutral_occurrences"] += diagnostic["additional_neutral_degree"] is not None and diagnostic["additional_neutral_degree"] > 0
        metric["raw_seed_recoveries"] += bool(target and target["seed_recovery"])
        metric["raw_nonseed_whole_hits"] += bool(target and target["certified_nonseed_value"])
        metric["primitive_raw_target_hits"] += main_target is not None
        metric["primary_distinct_target_values"] += bool(main_target and main_target["new_nonseed_value"])
        metric["whole_distinct_nonseed_target_values"] += bool(target and target["new_nonseed_value"])
        if main_target:
            primary_targets.add(core)
    metric.update(primitive_target_distinct_coefficient_cores=len(primary_targets),
        primitive_near_miss_distinct_cores=len({tuple(e["core_coefficients_ascending"]) for e in evaluations if e["primitive_near_miss"]}),
        unique_completed_polynomials=len({tuple(proposals[e["proposal"]]["free_coefficients"]) for e in evaluations}),
        unique_journalled_proposals=len({tuple(p["free_coefficients"]) for p in proposals.values()}))
    for key, value in record["primitive_metrics"].items():
        assert metric[key] == value, (label, variant, seed, key, metric[key], value)
    assert len(commits) == record["counts"]["completed_proposals"]
    assert replay["raw_attempts"] == record["generation_counts"]["dp_attempt_intents"]
    assert replay["completed_raw"] == record["generation_counts"]["dp_attempts_completed"]
    assert replay["accepted_raw"] == record["generation_counts"]["dp_accepted_parents"]
    assert replay["whole_proposals"] == record["generation_counts"]["journalled_whole_proposals"]
    assert not record["eligible_primitive_comparison_run"]
    best_center = None
    if committed_best is None:
        assert record["primitive_best"] is None
    else:
        for key, value in committed_best.items():
            same(record["primitive_best"][key], value)
        indexed = {e["proposal"]: e for e in evaluations}
        assert [c["proposal"] for c in record["primitive_best"]["contenders"]] == committed_best["contender_proposals"]
        for contender in record["primitive_best"]["contenders"]:
            proposal = contender["proposal"]
            same(contender["certificate"], indexed[proposal]["certificate"])
            assert contender["elapsed"] == commits[proposal]
        lo, hi = interval({"measure_interval": committed_best["minimum_measure_enclosure"]})
        best_center = float((lo + hi) / 2)
    return path, record, events, {"arm": variant, "seed": seed, **replay,
        "certificates_and_structures": checked, "completed": len(commits),
        "primary_occurrences": metric["primitive_completed_occurrences"], "termination": record["termination_reason"],
        "minimum_enclosure_center_display": best_center}


WHOLE = ("coefficients_ascending", "core_coefficients_ascending", "measure_interval", "measure_ball",
         "thresholds", "neutral", "precision_bits", "factorization_product_verified",
         "root_count_with_multiplicity", "ranking_resolved", "log_score")
FACTOR = ("coefficients_ascending", "measure_interval", "measure_ball", "thresholds",
          "degree", "exponent", "root_count", "cyclotomic")


def compact_reference(value):
    if isinstance(value, dict):
        if {"coefficients_ascending", "measure_interval", "factors", "neutral"} <= set(value):
            c = {k: copy.deepcopy(value[k]) for k in WHOLE if k in value}
            c["factors"] = [{**{k: copy.deepcopy(f[k]) for k in FACTOR}, "neutral": f["cyclotomic"],
                "scope": "measure of the single factor; exponent records its multiplicity in the parent"} for f in value["factors"]]
            c["root_certificate_reproduction"] = "sampler.certify_polynomial on the exact coefficients at retained precision"
            return c
        return {k: compact_reference(v) for k, v in value.items()}
    if isinstance(value, list):
        return [compact_reference(v) for v in value]
    return value


def inspect_native(label, prefix, runs):
    native = read(OUTPUT / f"{prefix}_native_comparison.json")
    witnesses = read(OUTPUT / f"{prefix}_native_witnesses.json")
    by_id = {w["witness_id"]: w for w in witnesses["witnesses"]}
    expected_usage, generation_count, certificate_count = {}, 0, 0
    by_source = {path.name: (path, record, events) for path, record, events, _ in runs}

    def witness(witness_id, coeff, role, run):
        item = by_id[witness_id]
        assert item["coefficients_ascending"] == coeff
        entry = expected_usage.setdefault(witness_id, {"roles": set(), "runs": set()})
        entry["roles"].add(role)
        entry["runs"].add(run)

    for group in native["groups"]:
        for row in group["all_seed_outcomes"]:
            path, record, events = by_source[row["source_summary"]]
            expected_record = compact_reference(record)
            if expected_record["initialization_observation"]:
                expected_record["initialization_observation"]["seed_witness_id"] = row["initialization_observation"]["seed_witness_id"]
            for key, value in expected_record.items():
                same(row[key], value)
            decoded = []
            for raw in row["generation_trace"]["rows"]:
                schema = row["generation_trace"]["schemas"][raw[0]]
                assert len(raw) == len(schema["fields"]) + 1
                decoded.append(dict(zip(["kind", *schema["fields"]], [schema["kind"], *raw[1:]])))
            expected = [e for e in events if e["kind"] in export.GENERATION_KINDS]
            same(decoded, expected)
            generation_count += len(decoded)
            same(export.replay_generation(decoded, record["configuration"]), row["generation_replay"])
            init = row["initialization_observation"]
            if init:
                witness(init["seed_witness_id"], init["seed_certificate"]["coefficients_ascending"],
                        "supplied_seed_not_discovery", path.stem)
            raw_evaluations = [e for e in events if e["kind"] == "evaluation"]
            assert len(raw_evaluations) == len(row["evaluation_observations"])
            proposals = {e["proposal"]: e for e in events if e["kind"] == "proposal"}
            commits = {e["proposal"]: e["elapsed"] for e in events if e["kind"] == "commit"}
            for original, saved in zip(raw_evaluations, row["evaluation_observations"]):
                for key, value in compact_reference(original).items():
                    same(saved[key], value)
                proposal = original["proposal"]
                committed = proposal in commits and commits[proposal] <= record["configuration"]["seconds"]
                assert saved["committed"] == committed
                assert saved["excluded_from_yield"] == (not committed or "unresolved_error" in original)
                same(saved["exact_proposal"], proposals[proposal])
                assert saved["commit_elapsed"] == commits.get(proposal)
                if "certificate" in original:
                    certificate_count += 1
                    witness(saved["whole_witness_id"], original["certificate"]["coefficients_ascending"],
                        "completed_whole_certificate" if committed else "uncommitted_whole_certificate_no_yield", path.stem)
                    for f, witness_id in zip(original["certificate"]["factors"], saved["factor_witness_ids"]):
                        witness(witness_id, f["coefficients_ascending"], "irreducible_factor_certificate", path.stem)
            incomplete = {p for p in proposals if p not in commits or commits[p] > record["configuration"]["seconds"]}
            assert {x["proposal"] for x in row["retry_inputs"]["incomplete_proposal_inputs"]} == incomplete
            for retry in row["retry_inputs"]["incomplete_proposal_inputs"]:
                assert retry["coefficients_ascending"] == proposals[retry["proposal"]]["coefficients_ascending"]
    assert set(expected_usage) == set(by_id)
    for witness_id, usage in expected_usage.items():
        assert usage["roles"] == set(by_id[witness_id]["roles"]) and usage["runs"] == set(by_id[witness_id]["runs"])
    assert native["retained_run_count"] == 5 and not native["complete_declared_primitive_comparison"]
    return {"generation_events": generation_count, "whole_certificates": certificate_count,
            "witnesses_and_all_associations": len(by_id), "all_original_summary_and_event_payloads_preserved": True}


def extra_fixtures(source_runs):
    assert direct_reference() == live.direct_parents()
    x = fmpz_poly([0, 1])
    primitive = (x+1)**56 + 2*x**28
    # After z=y-1 this is Eisenstein at 2: constant 2, all other nonleading
    # coefficients even, leading coefficient 1. It is a structural-only fixture.
    assert controls.factor_structure(values(primitive))["primary_class"]
    parent = direct_reference()
    parent = next(p for p in parent if p["substitution_index"] == 1 and p["sign"] == 1)
    child = parent["coefficients_ascending"].copy()
    child[2] -= 1
    child[54] -= 1
    delta = [a-b for a, b in zip(child, parent["coefficients_ascending"])]
    assert fmpz_poly(parent["neutral_coefficients_ascending"]).gcd(fmpz_poly(delta)) == 1
    assert fmpz_poly(child)(1) == 0
    fixture = controls.factor_structure(child)
    assert fixture["cyclotomic_degree"] >= 2 and not fixture["primary_class"]
    expected_schedule = [(arm, seed) for j, seed in enumerate(range(30, 35))
                         for arm in (("direct", "dp_closure") if j % 2 == 0 else ("dp_closure", "direct"))]
    assert live.schedule() == expected_schedule and len(set(expected_schedule)) == 10
    record = copy.deepcopy(source_runs[0][1])
    record["configuration"].update(seed=30, seconds=20, max_proposals=0, controlled_failure_check=False)
    record["supervision"].update(killed_at_cap=True, worker_returncode=0, supervisor_elapsed_seconds=20)
    assert live.validity(record)["eligible_primitive_comparison_run"]
    for key, bad in (("protocol", "wrong"), ("degree", 54), ("variant", "other"), ("seed", 29),
                     ("seconds", 2), ("max_proposals", 1), ("controlled_failure_check", True)):
        wrong = copy.deepcopy(record)
        wrong["configuration"][key] = bad
        assert not live.validity(wrong)["eligible_primitive_comparison_run"]
    wrong = copy.deepcopy(record)
    wrong["parent_attempt_limit_stop"] = True
    assert not live.validity(wrong)["eligible_primitive_comparison_run"]
    dp_events = source_runs[1][2]
    interesting = ("generation_start", "generation_branch", "raw_attempt_intent", "raw_attempt_ticket",
                   "raw_attempt_result", "parent_call_end", "parent_ready", "mutation_intent", "proposal")
    phases, checked = {}, 0
    for i, event in enumerate(dp_events):
        kind = event["kind"]
        if kind not in interesting or kind in phases:
            continue
        replay = export.replay_generation(dp_events[:i+1], source_runs[1][1]["configuration"])
        phases[kind] = replay["pending_generation"]["observed_phase"] if replay["pending_generation"] else None
        checked += 1
        if checked == len(interesting):
            break
    assert phases["raw_attempt_intent"] == "raw_selection_pending"
    assert phases["raw_attempt_ticket"] == "raw_construction_pending"
    assert phases["mutation_intent"] == "mutated_polynomial_pending" and phases["proposal"] is None
    fixture_events = [{"kind": "fixture", "i": 1, "b": True, "float": 1.0},
                      {"kind": "fixture", "i": None}, {"kind": "fixture", "b": False}]
    same(list(export.unpack_events(export.pack_events(fixture_events))), fixture_events)
    return {"positive_degree56_Eisenstein_structure_fixture": True,
            "gcd_one_with_new_neutral_factor_fixture": True, "exact_schedule_and_invalid_identity_fixtures": True,
            "pending_prefix_phases": phases, "missing_null_boolean_integer_float_roundtrip": True}


def evidence_boundary(original, current):
    """Independent missing/prefix/type boundaries; never launches a child."""
    checked, rejected, accepted = 0, [], []
    for path, record, events, _ in original + current:
        assert export.validate_journal_evidence(record, path.with_suffix(".jsonl"), events)
        checked += 1
    temporary_root = HERE.parents[3] / ".tmp"
    temporary_root.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="independent_primitive_evidence_", dir=temporary_root) as temporary:
        directory = Path(temporary).resolve()
        assert directory.is_relative_to(temporary_root.resolve()) and directory != temporary_root.resolve()

        def fixture(name, record, events=None, tail=""):
            path = directory / (name + ".json")
            copied = copy.deepcopy(record)
            if "events_file" in copied:
                copied["events_file"] = path.with_suffix(".jsonl").name
            if events is not None:
                path.with_suffix(".jsonl").write_text(
                    "".join(json.dumps(event) + "\n" for event in events) + tail, encoding="utf-8")
            return copied, path

        def reject(name, record, events=None):
            copied, path = fixture(name, record, events)
            witnesses = export.common.Witnesses()
            try:
                export.retain_run(copied, path, witnesses)
            except ValueError:
                assert not witnesses.by_coefficients
                rejected.append(name)
            else:
                raise AssertionError("lost or inconsistent evidence accepted: " + name)

        for index, (_, record, events, _) in enumerate(original + current):
            reject(f"known_work_{index}_missing", record)
            reject(f"known_work_{index}_empty", record, [])
        _, complete, complete_events, _ = original[0]
        reject("completed32_config_only", complete, complete_events[:1])
        cut = next(i for i, event in enumerate(complete_events)
                   if event["kind"] == "commit" and event["proposal"] == 31)
        reject("completed32_prefix31", complete, complete_events[:cut+1])
        for key, value in (("completed_proposals", 32.0), ("cache_hits", False)):
            mistyped = copy.deepcopy(complete)
            assert type(mistyped["counts"][key]) is int
            assert mistyped["counts"][key] == value
            mistyped["counts"][key] = value
            reject("summary_type_" + key, mistyped, complete_events)

        # The observed first DP intent is stopped synthetically before a whole
        # proposal; only the failure supervision is manufactured.
        _, dp_record, dp_events, _ = original[1]
        raw_start = next(i for i, event in enumerate(dp_events) if event["kind"] == "raw_attempt_intent")
        zero_events = dp_events[:raw_start+1]
        _, zero_path = fixture("zero_whole_pending_raw_present", dp_record, zero_events)
        zero = live.frozen.summarize_events(zero_path.with_suffix(".jsonl"))
        zero.update(worker_failure=True, supervision={"killed_at_cap": False, "worker_returncode": 1,
                    "supervisor_elapsed_seconds": zero_events[-1]["elapsed"], "stderr": "synthetic review prefix"})
        zero.update(live.validity(zero))
        zero["first_target_hit_censored_at"] = zero["observed_run_seconds"]
        live.enrich(zero, zero_events)
        assert zero["counts"]["proposals"] == zero["counts"]["completed_proposals"] == 0
        assert zero["generation_counts"]["dp_attempts_unfinished"] == 1
        retained = export.retain_run(zero, zero_path, export.common.Witnesses())
        assert retained["generation_replay"]["pending_generation"]["observed_phase"] == "raw_selection_pending"
        assert not retained["evaluation_observations"]
        accepted.append("zero_whole_pending_raw_present")
        reject("zero_whole_pending_raw_missing", zero)
        reject("zero_whole_pending_raw_empty", zero, [])
        reject("zero_whole_pending_raw_config_only", zero, zero_events[:1])

        # This is an actually observed current control, not a synthetic raw kill.
        _, pending, pending_events, _ = current[3]
        assert export.replay_generation(pending_events, pending["configuration"])[
            "pending_generation"]["observed_phase"] == "parent_deadline"
        final_request = max(i for i, event in enumerate(pending_events) if event["kind"] == "generation_start")
        reject("actual_parent_deadline_request_removed", pending, pending_events[:final_request])
        copied, path = fixture("actual_parent_deadline_present", pending, pending_events)
        retained = export.retain_run(copied, path, export.common.Witnesses())
        assert retained["generation_replay"]["pending_generation"]["observed_phase"] == "parent_deadline"
        accepted.append("actual_parent_deadline_present")

        # An actual saved final whole proposal also remains required when no
        # predeadline commit exists for it.
        _, deadline, deadline_events, _ = original[2]
        final_proposal = max(i for i, event in enumerate(deadline_events) if event["kind"] == "proposal")
        reject("actual_incomplete_whole_proposal_removed", deadline, deadline_events[:final_proposal])
        copied, path = fixture("deadline_complete_prefix_partial_tail", deadline, deadline_events, '{"kind":')
        retained = export.retain_run(copied, path, export.common.Witnesses())
        assert retained["valid_run"] and retained["counts"] == deadline["counts"]
        assert not any(event["kind"] == "finish" for event in deadline_events)
        accepted.append("deadline_complete_prefix_partial_tail")

        # Independently invoke the real supervisor exception branch; Popen is
        # intercepted before any subprocess can be created.
        args = argparse.Namespace(degree=56, variant="direct", seed=100, seconds=2, max_proposals=0)
        with mock.patch.object(live.runtime.subprocess, "Popen",
                               side_effect=OSError("independent startup fixture")) as start:
            startup = live.runtime.supervise(live.__file__, directory / "startup_runtime", args,
                                            live.configuration(56, "direct", 100))
        start.assert_called_once()
        live.enrich(startup, [])
        assert not startup["valid_run"] and startup["supervision"]["worker_returncode"] == -1
        for name, events, tail in (("startup_missing", None, ""), ("startup_empty", [], ""),
                                    ("startup_unfinished_config_line", [], '{"kind":"config"')):
            copied, path = fixture(name, startup, events, tail)
            witnesses = export.common.Witnesses()
            retained = export.retain_run(copied, path, witnesses)
            assert not witnesses.by_coefficients and not retained["valid_run"]
            assert retained["generation_replay"]["requests_started"] == 0
            assert not retained["evaluation_observations"] and not retained["generation_trace"]["rows"]
            accepted.append(name)
        mistaken = copy.deepcopy(startup)
        mistaken["generation_counts"]["dp_attempt_intents"] = 1
        reject("startup_marker_contradicted_by_pending_attempt", mistaken)
        reject("startup_marker_with_complete_generation_event", startup,
               [next(e for e in pending_events if e["kind"] == "generation_start")])
    assert not directory.exists()
    return {"full_original_and_reviewer_summaries_reconstructed": checked,
            "independently_rejected_cases": rejected, "independently_accepted_cases": accepted,
            "rejection_precedes_witness_insertion": True, "temporary_fixtures_removed": True,
            "actual_additional_workers_or_root_certifications": 0}


def corrected_retention(original, current):
    for suffix in ("comparison", "witnesses"):
        assert (OUTPUT / f"control_primitive_retention_v2_native_{suffix}.json").read_bytes() == (
            OUTPUT / f"control_primitive_retention_v7_native_{suffix}.json").read_bytes()
    rebuilt = []
    for label, prefix, runs in ((SOURCE_LABEL, "control_primitive_retention_v7", original),
                                (REVIEW_LABEL, REVIEW_LABEL, current)):
        comparison, witnesses = export.build_exports(label, True, [row[0] for row in runs])
        same(comparison, read(OUTPUT / f"{prefix}_native_comparison.json"))
        same(witnesses, read(OUTPUT / f"{prefix}_native_witnesses.json"))
        rebuilt.append({"source": label, "runs": comparison["retained_run_count"],
                        "all_original_native_fields_preserved": True,
                        "witnesses": len(witnesses["witnesses"])})
    return {"author_v2_v7_comparison_and_witnesses_byte_identical": True,
            "fresh_reexports_compared_in_memory": rebuilt}


def main():
    destination = OUTPUT / "independent_primitive_review.json"
    if destination.exists():
        raise FileExistsError(destination)
    original = [inspect_run(SOURCE_LABEL, *identity) for identity in PLAN]
    current = [inspect_run(REVIEW_LABEL, *identity) for identity in PLAN]
    result = {
        "scope": "Independent D56 implementation/control review; no formal comparison or new search.",
        "original_control_runs": [row[3] for row in original],
        "reviewer_control_runs": [row[3] for row in current],
        "original_native": inspect_native(SOURCE_LABEL, "control_primitive_retention_v2", original),
        "reviewer_native": inspect_native(REVIEW_LABEL, REVIEW_LABEL, current),
        "independent_extra_fixtures": extra_fixtures(original),
        "author_mechanisms": controls.mechanism_checks(),
        "author_stopping_replay": controls.stopping_and_replay_checks(),
        "author_ledgers": controls.ledger_checks(),
        "retention_revision": controls.compare_retention(
            OUTPUT / "control_primitive_impl_v1_native_comparison.json",
            OUTPUT / "control_primitive_retention_v2_native_comparison.json"),
        "historical_structure_interface": controls.structure_controls(SOURCE_LABEL,
            OUTPUT / "control_primitive_retention_v2_native_comparison.json"),
        "independent_journal_evidence_boundary": evidence_boundary(original, current),
        "corrected_complete_retention_chain": corrected_retention(original, current),
        "actual_new_worker_budget_ceiling_seconds": 10,
        "root_certification_scope": "Unchanged evaluator review reused; original complete root/factor counts and threshold intervals inspected; no standalone new root computation."
    }
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
