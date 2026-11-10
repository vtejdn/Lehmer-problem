"""Fixed Lehmer-parent comparison at D56; no online core/template feedback.

The evaluator and hard supervisor are imported unchanged.  The dedicated worker
adds write-ahead generation records, primitive-class diagnostics and independent
seed-excluding whole/primary ledgers.  Only predeadline evaluation commits count.
"""

from __future__ import annotations

import argparse
from collections import Counter, OrderedDict
from functools import reduce
import json
from math import gcd
from pathlib import Path
import random
import sys
import time

import archive_sampling as archive
from cyclotomic_parent_sampling import ParentSampler
import sampling_runtime as runtime

frozen = runtime.frozen
HERE, OUTPUT = frozen.HERE, frozen.OUTPUT
PROTOCOL = "S10-primitive-core-comparison"
DEGREE, SECONDS, MAX_ATTEMPTS = 56, 20.0, 4096
VARIANTS, SEEDS = ("direct", "dp_closure"), tuple(range(30, 35))
SEED_CORE = archive.SEED_CORE


def coefficients(poly):
    return list(map(int, poly)) or [0]


def exponent_gcd(poly):
    return reduce(gcd, (i for i, value in enumerate(poly) if i and value), 0)


def exact_quotient(numerator, denominator):
    q, r = divmod(frozen.fmpz_poly(numerator), frozen.fmpz_poly(denominator))
    assert not r
    return coefficients(q)


def direct_parents(degree=DEGREE):
    parents = {}
    for index in range(1, degree // (len(SEED_CORE) - 1) + 1):
        remainder = degree - index * (len(SEED_CORE) - 1)
        neutral = [1] if not remainder else [1] + [0] * (remainder - 1) + [1]
        for sign in (-1, 1):
            lifted = [0] * (index * (len(SEED_CORE) - 1) + 1)
            for i, value in enumerate(SEED_CORE):
                lifted[index * i] = value * sign**i
            polynomial = list(archive.closure.multiply(lifted, neutral))
            if max(map(abs, polynomial)) <= 4:
                key = tuple(polynomial[1:degree // 2 + 1])
                parents.setdefault(key, {"substitution_index": index, "sign": sign,
                                         "neutral_coefficients_ascending": neutral,
                                         "coefficients_ascending": polynomial})
    assert set(parents) == set(archive.sparse_completions(SEED_CORE, degree))
    return [parents[key] for key in sorted(parents)]


class Writer:
    def __init__(self, stream, started):
        self.stream, self.started = stream, started

    def emit(self, kind, **fields):
        frozen.write_event(self.stream, {"kind": kind, "elapsed": time.perf_counter() - self.started, **fields})


class LoggedParentSampler(ParentSampler):
    """Same three integer choices and unchanged construction, with prelogging."""

    def __init__(self, degree, writer):
        super().__init__(SEED_CORE, degree, 4)
        self.writer, self.request, self.global_attempt, self.local_attempt = writer, 0, 0, 0

    def draw_raw(self, rng):
        self.global_attempt += 1
        self.local_attempt += 1
        ids = {"request": self.request, "attempt": self.global_attempt, "request_attempt": self.local_attempt}
        self.writer.emit("raw_attempt_intent", **ids)
        substitution_ticket = rng.randrange(self.weight_sum)
        index = self.select_k(substitution_ticket)
        sign_ticket = rng.randrange(2)
        neutral_ticket = rng.randrange(self.weights[index - 1])
        self.writer.emit("raw_attempt_ticket", **ids, substitution_ticket=substitution_ticket,
                         substitution_index=index, sign_ticket=sign_ticket, sign=(-1, 1)[sign_ticket],
                         neutral_ticket=neutral_ticket)
        return self.construct(index, (-1, 1)[sign_ticket], neutral_ticket)

    def completed_attempt(self, ordinal, candidate, seconds):
        assert ordinal == self.local_attempt
        fields = {key: candidate[key] for key in ("substitution_index", "sign", "neutral_ticket", "observed_height", "accepted")}
        if candidate["accepted"]:
            fields.update({key: candidate[key] for key in ("coefficients_ascending", "neutral_factor_powers")})
        self.writer.emit("raw_attempt_result", request=self.request, attempt=self.global_attempt,
                         request_attempt=ordinal, construction_seconds=seconds, **fields)

    def parent(self, rng, request, deadline):
        self.request, self.local_attempt = request, 0
        return self.sample_accepted(rng, max_attempts=MAX_ATTEMPTS, deadline=deadline,
                                    on_attempt=self.completed_attempt)


def parent_with_neutral(candidate):
    parent = dict(candidate)
    index, sign = parent["substitution_index"], parent["sign"]
    lifted = [0] * (index * (len(SEED_CORE) - 1) + 1)
    for i, value in enumerate(SEED_CORE):
        lifted[index * i] = value * sign**i
    parent["neutral_coefficients_ascending"] = exact_quotient(parent["coefficients_ascending"], lifted)
    return parent


def mutate(parent, rng, degree):
    original = parent["coefficients_ascending"]
    prefix = list(original[1:degree // 2 + 1])
    size = rng.randrange(1, 4)
    coordinates = sorted(rng.sample(range(degree // 2), size))
    signs = [rng.choice((-1, 1)) for _ in coordinates]
    for coordinate, sign in zip(coordinates, signs):
        prefix[coordinate] += sign
    boundary_return = any(abs(value) > 4 for value in prefix)
    if boundary_return:
        prefix = list(original[1:degree // 2 + 1])
    child = frozen.reciprocal_polynomial(prefix)
    return prefix, {"mutation_size": size, "coordinates": coordinates, "signs": signs,
                    "boundary_return": boundary_return,
                    "delta_coefficients_ascending": [a - b for a, b in zip(child, original)]}


def generate(rng, request, degree, variant, parents, dp, writer, deadline):
    writer.emit("generation_start", request=request)
    branch_ticket = rng.randrange(10)
    branch = "uniform_box" if branch_ticket == 0 else variant
    writer.emit("generation_branch", request=request, branch=branch, branch_ticket=branch_ticket)
    if branch == "uniform_box":
        return {"status": "proposed", "free_coefficients": [rng.randrange(-4, 5) for _ in range(degree // 2)],
                "branch": branch, "parent": None, "mutation": None}
    if variant == "direct":
        index = rng.randrange(len(parents))
        parent = parents[index]
        writer.emit("direct_parent_choice", request=request, template_index=index)
    else:
        result = dp.parent(rng, request, deadline)
        writer.emit("parent_call_end", request=request, **{key: value for key, value in result.items() if key != "parent"})
        if result["status"] != "accepted":
            return {"status": result["status"]}
        parent = parent_with_neutral(result["parent"])
    writer.emit("parent_ready", request=request, parent=parent)
    if time.perf_counter() >= deadline:
        return {"status": "deadline"}
    writer.emit("mutation_intent", request=request)
    prefix, mutation = mutate(parent, rng, degree)
    return {"status": "proposed", "free_coefficients": prefix, "branch": branch,
            "parent": parent, "mutation": mutation}


def parent_diagnostics(generation, polynomial):
    if generation["parent"] is None:
        return {"applicable": False, "reason": "uniform whole-box branch has no parent"}
    neutral = generation["parent"]["neutral_coefficients_ascending"]
    delta = generation["mutation"]["delta_coefficients_ascending"]
    common = coefficients(frozen.fmpz_poly(neutral).gcd(frozen.fmpz_poly(delta)))
    assert not frozen.fmpz_poly(polynomial) % frozen.fmpz_poly(common)
    return {"applicable": True, "neutral_coefficients_ascending": neutral,
            "delta_coefficients_ascending": delta, "old_neutral_gcd_coefficients_ascending": common,
            "old_neutral_gcd_degree": len(common) - 1,
            "noncyclotomic_degree_upper_bound": len(polynomial) - len(common)}


def structural_diagnostics(certificate, target_degree=DEGREE):
    polynomial = certificate["coefficients_ascending"]
    neutral, raw, irreducibles = frozen.fmpz_poly([1]), frozen.fmpz_poly([1]), []
    for factor in certificate["factors"]:
        coefficients_ascending = factor["coefficients_ascending"]
        poly = frozen.fmpz_poly(coefficients_ascending)
        if factor["cyclotomic"]:
            neutral *= poly**factor["exponent"]
        else:
            raw *= poly**factor["exponent"]
        irreducibles.append({"coefficients_ascending": coefficients_ascending, "degree": factor["degree"],
                              "multiplicity": factor["exponent"], "cyclotomic": factor["cyclotomic"],
                              "exponent_gcd": exponent_gcd(coefficients_ascending),
                              "noncyclotomic_normalization_applicable": not factor["cyclotomic"],
                              "compressed_sign_normalized_coefficients_ascending": None if factor["cyclotomic"] else frozen.normalized_core([(poly, 1)]),
                              "primitive_noncyclotomic_factor": not factor["cyclotomic"] and exponent_gcd(coefficients_ascending) == 1})
    raw_coefficients = coefficients(raw)
    irreducible = (len(certificate["factors"]) == 1 and certificate["factors"][0]["exponent"] == 1
                   and certificate["factors"][0]["coefficients_ascending"] == polynomial)
    output_gcd = exponent_gcd(polynomial)
    return {"output_degree": len(polynomial) - 1, "output_exponent_gcd": output_gcd,
            "output_irreducible": irreducible,
            "primary_class": irreducible and not certificate["neutral"] and output_gcd == 1 and len(polynomial) - 1 == target_degree,
            "cyclotomic_part_coefficients_ascending": coefficients(neutral),
            "cyclotomic_degree": int(neutral.degree()),
            "raw_noncyclotomic_product_coefficients_ascending": raw_coefficients,
            "raw_noncyclotomic_degree": int(raw.degree()), "raw_noncyclotomic_exponent_gcd": exponent_gcd(raw_coefficients),
            "noncyclotomic_product_reducible": sum(f["exponent"] for f in certificate["factors"] if not f["cyclotomic"]) > 1,
            "normalized_whole_core_coefficients_ascending": certificate["core_coefficients_ascending"],
            "normalized_whole_core_degree": len(certificate["core_coefficients_ascending"]) - 1,
            "normalized_whole_core_irreducibility": "not inferred from this aggregate normalization",
            "individual_irreducible_factors": irreducibles}


def combine_diagnostics(structure, old_neutral):
    result = dict(structure, parent_neutral=old_neutral)
    if old_neutral["applicable"]:
        common = old_neutral["old_neutral_gcd_coefficients_ascending"]
        additional = exact_quotient(structure["cyclotomic_part_coefficients_ascending"], common)
        assert structure["raw_noncyclotomic_degree"] <= old_neutral["noncyclotomic_degree_upper_bound"]
        result["additional_neutral_coefficients_ascending"] = additional
        result["additional_neutral_degree"] = len(additional) - 1
    else:
        result["additional_neutral_coefficients_ascending"] = None
        result["additional_neutral_degree"] = None
    return result


class PrimitiveBest:
    """Finite minimum enclosure and all coefficient cores not proved worse."""
    def __init__(self):
        self.contenders, self.seen, self.upper = {}, set(), None

    def add(self, certificate, proposal):
        core = tuple(certificate["core_coefficients_ascending"])
        if core in self.seen:
            return self.snapshot()
        self.seen.add(core)
        low, high = map(frozen.interval_fraction, certificate["measure_interval"])
        if self.upper is None or high < self.upper:
            self.upper = high
            self.contenders = {key: value for key, value in self.contenders.items()
                               if frozen.interval_fraction(value["measure_interval"][0]) <= high}
        if low <= self.upper:
            self.contenders[core] = {"proposal": proposal, "measure_interval": certificate["measure_interval"]}
        return self.snapshot()

    def snapshot(self):
        if not self.contenders:
            return None
        values = list(self.contenders.values())
        selected = min(values, key=lambda item: (frozen.interval_fraction(item["measure_interval"][1]), item["proposal"]))
        lower = min((item["measure_interval"][0] for item in values), key=frozen.interval_fraction)
        return {"selected_witness_proposal": selected["proposal"],
                "contender_proposals": [item["proposal"] for item in values],
                "minimum_measure_enclosure": [lower, selected["measure_interval"][1]],
                "unique_minimizing_coefficient_core_certified": len(values) == 1}


def configuration(degree, variant, seed):
    return {"protocol": PROTOCOL, "degree": degree, "arm": variant, "variant": variant, "seed": seed,
            "supplied_core_coefficients_ascending": list(SEED_CORE), "online_feedback": False,
            "max_parent_attempts": MAX_ATTEMPTS, "dp_max_order_bound": 20000,
            "precision_bits": frozen.PRECISION_BITS, "ranking_radius": frozen.RANKING_RADIUS,
            "cache_size": frozen.CACHE_SIZE, "cache_policy": "per-run exact-polynomial LRU; no shared cache",
            "primary_class": "whole output irreducible, degree56, exponent gcd1; seed excluded",
            "hard_censoring": "no conditional-uniform claim for returned parents selected by the hard cap"}


def worker(args):
    deadline = args.started + args.seconds
    with Path(args.events).open("x", encoding="utf-8") as stream:
        writer = Writer(stream, args.started)
        writer.emit("config", **configuration(args.degree, args.variant, args.seed), seconds=args.seconds,
                    max_proposals=args.max_proposals, controlled_failure_check=args.fail_after_first_proposal,
                    python=sys.version.split()[0], python_flint=frozen.flint.__version__)
        writer.emit("initialization_start")
        started = time.perf_counter()
        seed = frozen.certify_polynomial(list(SEED_CORE))
        assert seed["thresholds"]["6/5"] == "below" and tuple(seed["core_coefficients_ascending"]) == SEED_CORE
        seed_seconds = time.perf_counter() - started
        started = time.perf_counter()
        parents = direct_parents(args.degree) if args.variant == "direct" else []
        dp = LoggedParentSampler(args.degree, writer) if args.variant == "dp_closure" else None
        whole, primary = archive.SeededLedger(seed), archive.SeededLedger(seed)
        broader, factor_ledger = frozen.DiscoveryLedger(), frozen.DiscoveryLedger()
        writer.emit("initialization", seed_certificate=seed, direct_parents=parents,
                    dp_build=dp.build if dp else None,
                    cost_seconds={"seed_certification": seed_seconds, "parent_setup_and_ledgers": time.perf_counter() - started})
        if time.perf_counter() >= deadline:
            return
        writer.emit("initialization_commit")
        rng, cache = random.Random(args.seed), OrderedDict()
        seen, seen_cores, primitive_cores, near_cores = set(), set(), set(), set()
        best, primitive_best = None, PrimitiveBest()
        request = proposal = 0
        reason = "deadline"
        while time.perf_counter() < deadline:
            if args.max_proposals and proposal >= args.max_proposals:
                reason = "proposal_limit"
                break
            request += 1
            started = time.perf_counter()
            generation = generate(rng, request, args.degree, args.variant, parents, dp, writer, deadline)
            if generation["status"] != "proposed":
                reason = "parent_attempt_limit" if generation["status"] == "attempt_limit" else "deadline"
                break
            proposal += 1
            prefix = generation["free_coefficients"]
            polynomial = frozen.reciprocal_polynomial(prefix)
            repeated, cached = tuple(prefix) in seen, tuple(prefix) in cache
            seen.add(tuple(prefix))
            writer.emit("proposal", proposal=proposal, request=request, free_coefficients=prefix,
                        coefficients_ascending=polynomial, generation=generation)
            generation_seconds = time.perf_counter() - started
            if args.fail_after_first_proposal:
                raise RuntimeError("deliberate primitive-worker failure after first whole proposal")
            started = time.perf_counter()
            old_neutral = parent_diagnostics(generation, polynomial)
            old_seconds = time.perf_counter() - started
            writer.emit("proposal_diagnostics", proposal=proposal, request=request,
                        parent_neutral=old_neutral, cost_seconds=old_seconds)
            evaluation_started = time.perf_counter()
            costs = {"generation_and_proposal_io": generation_seconds, "parent_neutral_diagnostic": old_seconds}
            certificate = None
            try:
                if cached:
                    started = time.perf_counter()
                    certificate, structure = cache[tuple(prefix)]
                    cache.move_to_end(tuple(prefix))
                    costs["cache_access_and_maintenance"] = time.perf_counter() - started
                    costs.update({key: 0.0 for key in certificate["cost_seconds"]})
                    costs["structure_diagnostic"] = 0.0
                else:
                    certificate = frozen.certify_polynomial(polynomial)
                    costs.update(certificate["cost_seconds"])
                    started = time.perf_counter()
                    structure = structural_diagnostics(certificate)
                    costs["structure_diagnostic"] = time.perf_counter() - started
                    started = time.perf_counter()
                    cache[tuple(prefix)] = (certificate, structure)
                    if len(cache) > frozen.CACHE_SIZE:
                        cache.popitem(last=False)
                    costs["cache_access_and_maintenance"] = time.perf_counter() - started
                started = time.perf_counter()
                diagnostics = combine_diagnostics(structure, old_neutral)
                core = tuple(certificate["core_coefficients_ascending"])
                repeated_core = not certificate["neutral"] and core in seen_cores
                if not certificate["neutral"]:
                    seen_cores.add(core)
                discovery = broader.add(certificate, proposal) if any(value == "below" for value in certificate["thresholds"].values()) else None
                whole_target = whole.add(certificate, proposal) if certificate["thresholds"]["6/5"] == "below" else None
                primary_target = primary.add(certificate, proposal) if whole_target and diagnostics["primary_class"] else None
                is_best = not certificate["neutral"] and certificate["ranking_resolved"] and (
                    best is None or frozen.interval_fraction(certificate["measure_interval"][1]) < frozen.interval_fraction(best["measure_interval"][0]))
                if is_best:
                    best = certificate
                primary_new_core = diagnostics["primary_class"] and core not in primitive_cores
                near = diagnostics["primary_class"] and certificate["thresholds"]["6/5"] == "above" and certificate["thresholds"]["13/10"] == "below"
                near_new_core = near and core not in near_cores
                if diagnostics["primary_class"]:
                    primitive_cores.add(core)
                    primitive_best.add(certificate, proposal)
                if near:
                    near_cores.add(core)
                factors = []
                for factor, detail in zip(certificate["factors"], diagnostics["individual_irreducible_factors"]):
                    if factor["cyclotomic"] or not any(value == "below" for value in factor["thresholds"].values()):
                        continue
                    factor_certificate = dict(factor, core_coefficients_ascending=detail["compressed_sign_normalized_coefficients_ascending"])
                    factors.append({"coefficients_ascending": factor["coefficients_ascending"], "thresholds": factor["thresholds"],
                                    "identity": factor_ledger.add(factor_certificate, proposal),
                                    "whole_output_below_6_5": certificate["thresholds"]["6/5"] == "below",
                                    "strictly_below_seed_enclosure": frozen.interval_fraction(factor["measure_interval"][1]) < frozen.interval_fraction(seed["measure_interval"][0]),
                                    "primitive_factor": detail["primitive_noncyclotomic_factor"]})
                costs["combined_diagnostics_and_ledgers"] = time.perf_counter() - started
                event = {"proposal": proposal, "request": request, "cached": cached, "repeated_proposal": repeated,
                         "repeated_positive_core": repeated_core, "neutral": certificate["neutral"],
                         "ranking_resolved": certificate["ranking_resolved"], "core_coefficients_ascending": list(core),
                         "log_score": certificate["log_score"], "thresholds": certificate["thresholds"],
                         "discovery": discovery, "factor_discoveries": factors, "is_new_best": is_best, "update": None,
                         "certificate": certificate, "diagnostics": diagnostics,
                         "whole_target": whole_target, "primary_target": primary_target,
                         "primitive_new_coefficient_core": primary_new_core, "primitive_near_miss": near,
                         "primitive_near_miss_new_core": near_new_core, "primitive_best": primitive_best.snapshot(), "cost_seconds": costs}
            except (ValueError, ArithmeticError) as error:
                event = {"proposal": proposal, "request": request, "cached": cached, "repeated_proposal": repeated,
                         "unresolved_error": repr(error), "update": None, "parent_neutral": old_neutral,
                         "cost_seconds": {"generation_and_proposal_io": generation_seconds,
                                          "parent_neutral_diagnostic": old_seconds,
                                          "failed_evaluation_total": time.perf_counter() - evaluation_started}}
                if certificate is not None:
                    event["certificate"] = certificate
            writer.emit("evaluation", **event)
            finished = time.perf_counter() - args.started
            if finished > args.seconds:
                break
            writer.emit("commit", proposal=proposal, elapsed=finished)
        if time.perf_counter() < deadline or reason == "parent_attempt_limit":
            writer.emit("finish", reason=reason)


def validity(record):
    result = frozen.run_validity(record)
    result.pop("eligible_full_pilot_run")
    if record.get("parent_attempt_limit_stop"):
        result.update(valid_run=False, termination_reason="parent_attempt_limit")
    config = record["configuration"]
    result["eligible_primitive_comparison_run"] = bool(result["valid_run"] and result["termination_reason"] == "deadline"
        and config["protocol"] == PROTOCOL and config["degree"] == DEGREE and config["variant"] in VARIANTS
        and config["seed"] in SEEDS and config["seconds"] == SECONDS and config["max_proposals"] == 0
        and not config.get("controlled_failure_check", False))
    return result


def enrich(record, events):
    budget = record["configuration"]["seconds"]
    commits = {event["proposal"]: event["elapsed"] for event in events if event["kind"] == "commit" and event["elapsed"] <= budget}
    evaluations = [event for event in events if event["kind"] == "evaluation" and event["proposal"] in commits]
    proposals = {event["proposal"]: event for event in events if event["kind"] == "proposal"}
    result = Counter()
    primary_values, primary_equalities, whole_nonseed, target_cores, near, below, primary_cores = [], [], [], [], [], [], []
    seen_target, seen_below, seen_primary_target = set(), set(), set()
    catalog = archive.load_catalog()
    best_snapshot = None
    for event in evaluations:
        if "unresolved_error" in event:
            continue
        diagnostic, certificate = event["diagnostics"], event["certificate"]
        core = tuple(certificate["core_coefficients_ascending"])
        scope = {"proposal": event["proposal"], "elapsed": commits[event["proposal"]],
                 "branch": proposals[event["proposal"]]["generation"]["branch"], "certificate": certificate}
        result["primitive_completed_occurrences"] += diagnostic["primary_class"]
        result["primitive_unique_coefficient_cores"] += event["primitive_new_coefficient_core"]
        result["primitive_near_miss_occurrences"] += event["primitive_near_miss"]
        result["neutral_factor_occurrences"] += diagnostic["cyclotomic_degree"] > 0
        result["output_exponent_compression_occurrences"] += diagnostic["output_exponent_gcd"] > 1
        result["raw_core_compression_occurrences"] += diagnostic["raw_noncyclotomic_exponent_gcd"] > 1
        result["noncyclotomic_reducible_occurrences"] += diagnostic["noncyclotomic_product_reducible"]
        old = diagnostic["parent_neutral"]
        result["retained_old_neutral_occurrences"] += old["applicable"] and old["old_neutral_gcd_degree"] > 0
        result["additional_neutral_occurrences"] += diagnostic["additional_neutral_degree"] is not None and diagnostic["additional_neutral_degree"] > 0
        if event["primitive_near_miss_new_core"]:
            near.append(scope)
        if event["primitive_new_coefficient_core"]:
            primary_cores.append(scope)
        best_snapshot = event["primitive_best"]
        target = event["whole_target"]
        if target:
            result["raw_seed_recoveries"] += target["seed_recovery"]
            result["raw_nonseed_whole_hits"] += target["certified_nonseed_value"]
            if target["new_nonseed_value"]:
                whole_nonseed.append({**scope, **target})
            if core not in seen_target:
                seen_target.add(core)
                classification = "supplied_seed_core" if core == SEED_CORE else "second_local_core" if core in catalog else "not_in_supplied_local_catalog"
                target_cores.append({**scope, **target, "local_classification": classification})
            if target["seed_relation"] == "strictly_below_seed_enclosure" and core not in seen_below:
                seen_below.add(core)
                below.append(scope)
        target = event["primary_target"]
        if target:
            seen_primary_target.add(core)
            result["primitive_raw_target_hits"] += 1
            if target["new_nonseed_value"]:
                primary_values.append({**scope, **target})
            if target["identity"]["status"] == "unresolved_equality":
                primary_equalities.append({**scope, **target})
    for key in ("primitive_completed_occurrences", "primitive_unique_coefficient_cores", "primitive_near_miss_occurrences",
                "neutral_factor_occurrences", "output_exponent_compression_occurrences", "raw_core_compression_occurrences",
                "noncyclotomic_reducible_occurrences", "retained_old_neutral_occurrences", "additional_neutral_occurrences",
                "raw_seed_recoveries", "raw_nonseed_whole_hits", "primitive_raw_target_hits"):
        result[key] += 0
    result.update({"primary_distinct_target_values": len(primary_values), "whole_distinct_nonseed_target_values": len(whole_nonseed),
                   "primitive_target_distinct_coefficient_cores": len(seen_primary_target), "primitive_near_miss_distinct_cores": len(near),
                   "unique_completed_polynomials": len({tuple(proposals[event["proposal"]]["free_coefficients"]) for event in evaluations}),
                   "unique_journalled_proposals": len({tuple(event["free_coefficients"]) for event in proposals.values()})})
    best = None
    if best_snapshot:
        indexed = {event["proposal"]: event for event in evaluations}
        best = {**best_snapshot, "contenders": [{"proposal": p, "elapsed": commits[p],
                 "certificate": indexed[p]["certificate"]} for p in best_snapshot["contender_proposals"]]}
    attempts = [event for event in events if event["kind"] == "raw_attempt_intent"]
    finished_attempts = [event for event in events if event["kind"] == "raw_attempt_result"]
    initialization_committed = any(event["kind"] == "initialization_commit" and event["elapsed"] <= budget for event in events)
    initialization = next((event for event in events if event["kind"] == "initialization"), None)
    record.update({"primitive_metrics": dict(result), "primary_discoveries": primary_values,
                   "primary_unresolved_equalities": primary_equalities, "whole_nonseed_discoveries": whole_nonseed,
                   "whole_target_core_observations": target_cores, "primitive_coefficient_cores": primary_cores,
                   "primitive_near_miss_cores": near, "strictly_below_seed_whole_values": below,
                   "primitive_best": best, "initialization_committed": initialization_committed,
                   "initialization_observation": initialization,
                   "first_primary_hit_seconds": primary_values[0]["elapsed"] if primary_values else None,
                   "first_primary_hit_censored_at": None if primary_values else record["observed_run_seconds"],
                   "first_whole_nonseed_hit_seconds": whole_nonseed[0]["elapsed"] if whole_nonseed else None,
                   "generation_counts": {"requests_started": sum(event["kind"] == "generation_start" for event in events),
                     "journalled_whole_proposals": len(proposals), "dp_attempt_intents": len(attempts),
                     "dp_attempts_with_ticket": sum(event["kind"] == "raw_attempt_ticket" for event in events),
                     "dp_attempts_completed": len(finished_attempts), "dp_height_rejections": sum(not event["accepted"] for event in finished_attempts),
                     "dp_accepted_parents": sum(event["accepted"] for event in finished_attempts),
                     "dp_attempts_unfinished": len(attempts) - len(finished_attempts)},
                   "generation_accounting": {
                     "completed_raw_construction_seconds_all_journalled": sum(event["construction_seconds"] for event in finished_attempts),
                     "completed_parent_call_elapsed_seconds_all_journalled": sum(event["elapsed_seconds"] for event in events if event["kind"] == "parent_call_end"),
                     "raw_attempt_intents_within_budget": sum(event["elapsed"] <= budget for event in attempts),
                     "raw_attempt_results_within_budget": sum(event["elapsed"] <= budget for event in finished_attempts),
                     "scope": "construction and parent-call totals overlap; incomplete generation remains charged by the observed run clock"},
                   "parent_attempt_limit_stop": any(event["kind"] == "parent_call_end" and event["status"] == "attempt_limit" for event in events),
                   "local_catalog_scope": "inputs/degree_core_mass_states.json two known cores, reporting only; no novelty inference"})
    record.update(validity(record))
    if not primary_values:
        record["first_primary_hit_censored_at"] = record["observed_run_seconds"]
    return record


def run_stem(label, degree, variant, seed):
    archive.check_label(label)
    return OUTPUT / f"{label}_d{degree}_{variant}_s{seed}"


def run_once(variant, seed, seconds, label, max_proposals=0, *, failure_check=False, raise_on_failure=True):
    if variant not in VARIANTS or type(seed) is not int or seed < 0 or not 0 < seconds <= SECONDS or max_proposals < 0:
        raise ValueError("invalid primitive comparison run parameters")
    if seed not in SEEDS and not label.startswith("control_"):
        raise ValueError("nonformal seeds require control_ labels")
    args = argparse.Namespace(degree=DEGREE, variant=variant, seed=seed, seconds=seconds, max_proposals=max_proposals)
    stem = run_stem(label, DEGREE, variant, seed)
    record = runtime.supervise(__file__, stem, args, configuration(DEGREE, variant, seed), failure_check)
    events = frozen.read_events(stem.with_suffix(".jsonl")) if stem.with_suffix(".jsonl").exists() else []
    enrich(record, events)
    frozen.write_json(stem.with_suffix(".json"), record)
    print(json.dumps({"file": stem.with_suffix(".json").name, "valid_run": record["valid_run"],
                     "termination_reason": record["termination_reason"], "completed": record["counts"]["completed_proposals"],
                     "generation_counts": record["generation_counts"], "primitive_metrics": record["primitive_metrics"]}), flush=True)
    if raise_on_failure and not record["valid_run"]:
        raise RuntimeError(record["supervision"]["stderr"] or record["termination_reason"])
    return record


def schedule():
    return [(variant, seed) for j, seed in enumerate(SEEDS) for variant in (VARIANTS if j % 2 == 0 else VARIANTS[::-1])]


def run_paths(label):
    return [path for variant, seed in schedule() if (path := run_stem(label, DEGREE, variant, seed).with_suffix(".json")).is_file()]


def report(label, paths=None):
    rows = []
    for path in run_paths(label) if paths is None else paths:
        record = json.loads(Path(path).read_text(encoding="utf-8"))
        config = record["configuration"]
        if config["protocol"] != PROTOCOL or run_stem(label, config["degree"], config["variant"], config["seed"]) != Path(path).with_suffix(""):
            raise ValueError("wrong protocol or identity")
        rows.append({**record, **validity(record), "degree": DEGREE, "arm": config["variant"], "seed": config["seed"]})
    expected = set(schedule())
    complete = len(rows) == 10 and {(row["arm"], row["seed"]) for row in rows} == expected and all(row["eligible_primitive_comparison_run"] for row in rows)
    return {"protocol": PROTOCOL, "label": label, "degree": DEGREE, "seeds": list(SEEDS),
            "groups": [{"arm": variant, "all_seed_outcomes": [row for row in rows if row["arm"] == variant]} for variant in VARIANTS],
            "complete_declared_primitive_comparison": complete,
            "experimental_seconds_ceiling_represented": sum(row["configuration"]["seconds"] for row in rows),
            "interpretation": "Seeded finite primitive-core comparison; no online feedback; zero-zero is not improvement; no automatic reruns, significance or novelty claim."}


def compare(label):
    if any(run_stem(label, DEGREE, variant, seed).with_suffix(suffix).exists()
           for variant, seed in schedule() for suffix in (".json", ".jsonl")):
        raise FileExistsError("preserve prior run evidence")
    try:
        for variant, seed in schedule():
            run_once(variant, seed, SECONDS, label)
    finally:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        frozen.write_json(OUTPUT / f"{label}_primitive_comparison.json", report(label))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("run", "_worker"):
        command = commands.add_parser(name)
        command.add_argument("--degree", type=int, choices=(DEGREE,), default=DEGREE)
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
    args = parser.parse_args()
    if args.command == "_worker":
        worker(args)
    elif args.command == "run":
        run_once(args.variant, args.seed, args.seconds, args.label, args.max_proposals)
    elif args.command == "compare":
        compare(args.label)
    else:
        frozen.write_json(OUTPUT / f"{args.label}_primitive_comparison.json", report(args.label))


if __name__ == "__main__":
    main()
