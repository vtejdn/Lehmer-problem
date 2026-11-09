"""S10's bounded, exact-law comparison; coefficients are ascending throughout.

Only python-flint is required beyond Python's standard library.
The supervisor kills a run at its deadline; only committed pre-deadline work counts.
"""

from __future__ import annotations

import argparse
import bisect
from collections import Counter, OrderedDict
from fractions import Fraction
from functools import reduce
import itertools
import json
import math
import os
from pathlib import Path
import random
import statistics
import subprocess
import sys
import time

IMPORT_STARTED = time.perf_counter()
import flint
from flint import arb, ctx, fmpz_poly

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
ARMS = ("uniform", "fixed", "adaptive")
DEGREES = (14, 18, 20)
ALPHABET = tuple(range(-4, 5))
FIXED_WEIGHTS = (1, 2, 4, 8, 16, 8, 4, 2, 1)
THRESHOLDS = {"6/5": (6, 5), "5/4": (5, 4), "13/10": (13, 10), "7/5": (7, 5)}
PRECISION_BITS = 128
RANKING_RADIUS = "1e-12"
BATCH_SIZE = 256
CACHE_SIZE = 4096
PROTOCOL = "S10-first-experiment"
ctx.prec = PRECISION_BITS
ctx.threads = 1


def interval_endpoint(value):
    mantissa, exponent = value.man_exp()
    return [int(mantissa), int(exponent)]


def interval_fraction(endpoint):
    mantissa, exponent = endpoint
    return Fraction(mantissa * 2**max(exponent, 0), 2**max(-exponent, 0))


def ball_interval(value):
    return [interval_endpoint(value.lower()), interval_endpoint(value.upper())]


def intervals_overlap(left, right):
    return not (interval_fraction(left[1]) < interval_fraction(right[0]) or
                interval_fraction(right[1]) < interval_fraction(left[0]))


def classify_thresholds(value, neutral):
    if neutral:
        return {key: "neutral" for key in THRESHOLDS}
    result = {}
    for key, (numerator, denominator) in THRESHOLDS.items():
        if value > 1 and value * denominator < numerator:
            result[key] = "below"
        elif value * denominator >= numerator:
            result[key] = "above"
        else:
            result[key] = "unresolved"
    return result


def normalized_core(factors):
    """Remove all cyclotomics, compress substitutions, then normalize the sign.

    The lexicographic comparison is on monic DESCENDING coefficient lists.
    The returned representation, like every other native coefficient list, ascends.
    """
    core = fmpz_poly([1])
    for polynomial, exponent in factors:
        if not polynomial.is_cyclotomic():
            core *= polynomial**exponent
    coefficients = tuple(map(int, core))
    while len(coefficients) > 1:
        divisor = reduce(math.gcd, (i for i, value in enumerate(coefficients) if i and value), 0)
        if divisor <= 1:
            break
        coefficients = coefficients[::divisor]
    degree = len(coefficients) - 1
    opposite = tuple(value * (-1)**(degree + i) for i, value in enumerate(coefficients))
    return list(min(coefficients[::-1], opposite[::-1])[::-1])


def certify_polynomial(coefficients_ascending):
    """Enclose the COMPLETE measure using exact factorization and all Arb roots.

    No radius-only screen or numerical exclusion is used.
    A modulus ball meeting one contributes its union with {1}; dropping it would
    fail to enclose max(1, |root|). Exact cyclotomic factors contribute exactly 1.
    """
    if not coefficients_ascending or coefficients_ascending[-1] != 1 or coefficients_ascending[0] == 0:
        raise ValueError("a monic integer polynomial with nonzero constant term is required")
    if any(type(value) is not int for value in coefficients_ascending):
        raise ValueError("coefficients must be exact Python integers")
    ctx.prec = PRECISION_BITS
    ctx.threads = 1
    polynomial = fmpz_poly(coefficients_ascending)
    started = time.perf_counter()
    content, factors = polynomial.factor()
    reconstruction = fmpz_poly([content])
    for factor, exponent in factors:
        reconstruction *= factor**exponent
    assert reconstruction == polynomial and int(content) == 1
    factor_seconds = time.perf_counter() - started
    started = time.perf_counter()
    core = normalized_core(factors)
    normalization_seconds = time.perf_counter() - started
    started = time.perf_counter()
    neutral = all(bool(factor.is_cyclotomic()) for factor, _ in factors)
    total, total_roots, records = arb(1), 0, []
    for factor, exponent in factors:
        cyclotomic = bool(factor.is_cyclotomic())
        product, roots, count = arb(1), [], 0
        if cyclotomic:
            count = factor.degree()
        else:
            for root, multiplicity in factor.complex_roots():
                modulus = abs(root)
                if modulus < 1:
                    contribution, region = arb(1), "inside"
                elif modulus > 1:
                    contribution, region = modulus, "outside"
                else:
                    contribution, region = arb(1).union(modulus), "meets_one"
                product *= contribution**multiplicity
                count += multiplicity
                roots.append({"root_ball": str(root), "modulus_ball": str(modulus),
                              "contribution_ball": str(contribution),
                              "multiplicity": int(multiplicity), "region": region})
            assert count == factor.degree()
        total *= product**exponent
        total_roots += count * exponent
        records.append({"coefficients_ascending": list(map(int, factor)),
                        "degree": int(factor.degree()), "exponent": int(exponent),
                        "cyclotomic": cyclotomic, "root_count": int(count),
                        "roots": roots, "measure_ball": str(product),
                        "measure_interval": ball_interval(product),
                        "thresholds": classify_thresholds(product, cyclotomic)})
    assert total_roots == polynomial.degree()
    log_measure = total.log()
    resolved = neutral or bool(total > 1 and log_measure.rad() < arb(RANKING_RADIUS))
    return {"coefficients_ascending": coefficients_ascending,
            "precision_bits": PRECISION_BITS, "factorization_product_verified": True,
            "root_count_with_multiplicity": int(total_roots), "factors": records,
            "neutral": neutral, "core_coefficients_ascending": core,
            "measure_ball": str(total), "measure_interval": ball_interval(total),
            "log_score": float(log_measure.mid()) if resolved else None,
            "ranking_resolved": resolved, "thresholds": classify_thresholds(total, neutral),
            "cost_seconds": {"factorization": factor_seconds,
                             "normalization": normalization_seconds,
                             "root_certification": time.perf_counter() - started}}


def reciprocal_polynomial(free):
    return [1, *free, *reversed(free[:-1]), 1]


def cumulative(weights):
    return list(itertools.accumulate(weights))


class Law:
    """Exact integer-weight categorical sampling, including every adaptive update."""

    def __init__(self, half_degree, arm, seed):
        self.half_degree, self.arm, self.rng = half_degree, arm, random.Random(seed)
        self.blocks = []
        for start in range(0, half_degree, 2):
            width = min(2, half_degree - start)
            states = list(itertools.product(ALPHABET, repeat=width))
            weights = [math.prod(FIXED_WEIGHTS[x + 4] for x in state) for state in states]
            self.blocks.append({"start": start, "width": width, "states": states,
                                "weights": weights, "cumulative": cumulative(weights)})
        self.fixed_cumulative = cumulative(FIXED_WEIGHTS)

    def draw(self):
        uniform = self.arm == "uniform" or self.rng.randrange(10) == 0
        if uniform:
            return [self.rng.randrange(-4, 5) for _ in range(self.half_degree)]
        if self.arm == "fixed":
            return [ALPHABET[bisect.bisect_right(self.fixed_cumulative, self.rng.randrange(46))]
                    for _ in range(self.half_degree)]
        values = []
        for block in self.blocks:
            index = bisect.bisect_right(block["cumulative"], self.rng.randrange(block["cumulative"][-1]))
            values.extend(block["states"][index])
        return values

    def update(self, batch):
        if self.arm != "adaptive":
            return None
        # One representative per normalized core, with deterministic score/tuple tie breaking.
        representatives = {}
        for core, score, free in batch:
            item = (score, tuple(free))
            if core not in representatives or item < representatives[core]:
                representatives[core] = item
        selected = sorted(representatives.values())[:math.ceil(len(representatives) / 10)]
        if selected:
            for block in self.blocks:
                start, width = block["start"], block["width"]
                observations = Counter(free[start:start + width] for _, free in selected)
                counts = [1 + observations[state] for state in block["states"]]
                denominator = sum(counts)
                total = sum(block["weights"])
                weights = [4 * old * denominator + count * total
                           for old, count in zip(block["weights"], counts)]
                divisor = reduce(math.gcd, weights)
                block["weights"] = [value // divisor for value in weights]
                block["cumulative"] = cumulative(block["weights"])
        return {"eligible_proposals": len(batch), "unique_eligible_cores": len(representatives),
                "elite_count": len(selected), "elite_free_coefficients": [list(free) for _, free in selected]}


class DiscoveryLedger:
    """Conservative interval separation, never a rounded numeric value identity."""

    def __init__(self):
        self.values, self.cores, self.uncertain = [], {}, []

    def add(self, certificate, proposal):
        core = tuple(certificate["core_coefficients_ascending"])
        if core in self.cores:
            return {"status": "same_core", "value_id": self.cores[core]}
        overlaps = [entry["value_id"] for entry in self.values
                    if intervals_overlap(entry["measure_interval"], certificate["measure_interval"])]
        if overlaps:
            self.cores[core] = None
            self.uncertain.append({"proposal": proposal, "overlapping_value_ids": overlaps,
                                   "core_coefficients_ascending": list(core)})
            return {"status": "unresolved_equality", "overlapping_value_ids": overlaps}
        value_id = len(self.values)
        self.cores[core] = value_id
        entry = {"value_id": value_id, "proposal": proposal,
                 "measure_interval": certificate["measure_interval"],
                 "measure_ball": certificate["measure_ball"],
                 "core_coefficients_ascending": list(core), "thresholds": certificate["thresholds"]}
        self.values.append(entry)
        return {"status": "new_separated_value", "value_id": value_id}


def write_event(stream, event):
    stream.write(json.dumps(event, separators=(",", ":")) + "\n")
    stream.flush()


def worker(args):
    """Never invoked directly by the experimental operator; the supervisor owns caps."""
    deadline = args.started + args.seconds
    law = Law(args.degree // 2, args.arm, args.seed)
    cache, seen_proposals, seen_cores, batch = OrderedDict(), set(), set(), []
    ledger, factor_ledger, best = DiscoveryLedger(), DiscoveryLedger(), None
    proposal = 0
    with Path(args.events).open("x", encoding="utf-8") as stream:
        write_event(stream, {"kind": "config", "protocol": PROTOCOL, "degree": args.degree,
                            "arm": args.arm, "seed": args.seed, "seconds": args.seconds,
                            "max_proposals": args.max_proposals, "precision_bits": PRECISION_BITS,
                            "ranking_radius": RANKING_RADIUS, "batch_size": BATCH_SIZE,
                            "cache_policy": "per-run exact-polynomial LRU; no shared cache",
                            "cache_size": CACHE_SIZE,
                            "python": sys.version.split()[0], "python_flint": flint.__version__,
                            "worker_setup_seconds": time.perf_counter() - args.started})
        while time.perf_counter() < deadline:
            if args.max_proposals and proposal >= args.max_proposals:
                break
            generation_start = time.perf_counter()
            free = law.draw()
            proposal += 1
            repeated = tuple(free) in seen_proposals
            seen_proposals.add(tuple(free))
            write_event(stream, {"kind": "proposal", "proposal": proposal,
                                "free_coefficients": free, "elapsed": time.perf_counter() - args.started})
            generation_seconds = time.perf_counter() - generation_start
            cached = tuple(free) in cache
            try:
                certificate = cache[tuple(free)] if cached else certify_polynomial(reciprocal_polynomial(free))
                if not cached:
                    cache[tuple(free)] = certificate
                    if len(cache) > CACHE_SIZE:
                        cache.popitem(last=False)
                else:
                    cache.move_to_end(tuple(free))
                core = tuple(certificate["core_coefficients_ascending"])
                repeated_core = not certificate["neutral"] and core in seen_cores
                if not certificate["neutral"]:
                    seen_cores.add(core)
                if certificate["ranking_resolved"] and not certificate["neutral"]:
                    batch.append((core, certificate["log_score"], free))
                dedup_started = time.perf_counter()
                discovery, factor_discoveries, retain, is_best = None, [], False, False
                if any(status == "below" for status in certificate["thresholds"].values()):
                    discovery = ledger.add(certificate, proposal)
                    retain = True
                if not certificate["neutral"] and certificate["ranking_resolved"]:
                    if best is None or interval_fraction(certificate["measure_interval"][1]) < interval_fraction(best["measure_interval"][0]):
                        best = certificate
                        is_best = retain = True
                # These factors never contribute to whole-output yield.
                for factor in certificate["factors"]:
                    if factor["cyclotomic"] or not any(s == "below" for s in factor["thresholds"].values()):
                        continue
                    factor_certificate = dict(factor)
                    factor_certificate["core_coefficients_ascending"] = normalized_core([(fmpz_poly(factor["coefficients_ascending"]), 1)])
                    factor_result = factor_ledger.add(factor_certificate, proposal)
                    factor_discoveries.append({"coefficients_ascending": factor["coefficients_ascending"],
                                               "thresholds": factor["thresholds"], "identity": factor_result,
                                               "whole_output_below_6_5": certificate["thresholds"]["6/5"] == "below"})
                    retain = True
                dedup_seconds = time.perf_counter() - dedup_started
                update_started = time.perf_counter()
                update = law.update(batch) if proposal % BATCH_SIZE == 0 else None
                if proposal % BATCH_SIZE == 0:
                    batch.clear()
                update_seconds = time.perf_counter() - update_started
                event = {"kind": "evaluation", "proposal": proposal, "cached": cached,
                         "repeated_proposal": repeated, "repeated_positive_core": repeated_core,
                         "neutral": certificate["neutral"], "ranking_resolved": certificate["ranking_resolved"],
                         "core_coefficients_ascending": list(core), "log_score": certificate["log_score"],
                         "thresholds": certificate["thresholds"], "discovery": discovery,
                         "factor_discoveries": factor_discoveries, "is_new_best": is_best, "update": update,
                         "cost_seconds": {"generation_and_proposal_io": generation_seconds,
                                          "deduplication": dedup_seconds, "distribution_update": update_seconds,
                                          **({key: 0.0 for key in certificate["cost_seconds"]} if cached else certificate["cost_seconds"])}}
                if retain:
                    event["certificate"] = certificate
            except (ValueError, ArithmeticError) as error:
                # A numerical/library failure is explicit unresolved work, never an exclusion.
                update = law.update(batch) if proposal % BATCH_SIZE == 0 else None
                if proposal % BATCH_SIZE == 0:
                    batch.clear()
                event = {"kind": "evaluation", "proposal": proposal, "cached": cached,
                         "repeated_proposal": repeated, "unresolved_error": repr(error), "update": update}
            if time.perf_counter() >= deadline:
                break
            write_event(stream, event)
            finished = time.perf_counter() - args.started
            if finished > args.seconds:
                break
            # The large result, all arithmetic, adaptive update and deduplication are already flushed.
            write_event(stream, {"kind": "commit", "proposal": proposal, "elapsed": finished})
        if time.perf_counter() < deadline:
            write_event(stream, {"kind": "finish", "elapsed": time.perf_counter() - args.started,
                                 "reason": "proposal_limit" if args.max_proposals else "deadline"})


def read_events(path):
    events = []
    with Path(path).open(encoding="utf-8") as stream:
        for line in stream:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                # A supervisor kill may truncate the final journal record.
                break
    return events


def summarize_events(path):
    events = read_events(path)
    config = next(event for event in events if event["kind"] == "config")
    committed = {event["proposal"]: event["elapsed"] for event in events
                 if event["kind"] == "commit" and event["elapsed"] <= config["seconds"]}
    proposals = [event for event in events if event["kind"] == "proposal" and event["elapsed"] <= config["seconds"]]
    evaluations = [event for event in events if event["kind"] == "evaluation" and event["proposal"] in committed]
    counts, costs, raw, distinct, factor_distinct = Counter(), Counter(), Counter(), Counter(), Counter()
    equality_cases, factor_equality_cases, discoveries, factor_discoveries, best, first_hit = [], [], [], [], None, None
    cores = set()
    for event in evaluations:
        counts["repeated_proposals"] += event["repeated_proposal"]
        counts["cache_hits"] += event["cached"]
        counts["fresh_completed_evaluations"] += not event["cached"]
        costs.update(event.get("cost_seconds", {}))
        if "unresolved_error" in event:
            counts["unresolved_errors"] += 1
            continue
        counts["neutral"] += event["neutral"]
        counts["resolved_positive"] += not event["neutral"] and event["ranking_resolved"]
        counts["unresolved_ranking"] += not event["ranking_resolved"]
        counts["repeated_positive_cores"] += event["repeated_positive_core"]
        counts["adaptive_updates"] += event["update"] is not None
        if not event["neutral"]:
            cores.add(tuple(event["core_coefficients_ascending"]))
        for key, status in event["thresholds"].items():
            raw[key] += status == "below"
            counts["unresolved_threshold_" + key] += status == "unresolved"
        discovery = event["discovery"]
        if discovery and discovery["status"] == "new_separated_value":
            for key, status in event["thresholds"].items():
                distinct[key] += status == "below"
            discoveries.append({"proposal": event["proposal"], "elapsed": committed[event["proposal"]],
                                **discovery, "certificate": event["certificate"]})
        if discovery and discovery["status"] == "unresolved_equality":
            equality_cases.append({"proposal": event["proposal"], **discovery,
                                   "certificate": event["certificate"]})
        if event["thresholds"]["6/5"] == "below" and first_hit is None:
            first_hit = committed[event["proposal"]]
        if event["is_new_best"]:
            best = {"proposal": event["proposal"], "elapsed": committed[event["proposal"]],
                    "certificate": event["certificate"]}
        for factor in event["factor_discoveries"]:
            if factor["identity"]["status"] == "new_separated_value":
                for key, status in factor["thresholds"].items():
                    factor_distinct[key] += status == "below"
                factor_discoveries.append({"proposal": event["proposal"], **factor})
            elif factor["identity"]["status"] == "unresolved_equality":
                factor_equality_cases.append({"proposal": event["proposal"], **factor})
    for key in THRESHOLDS:
        raw[key] += 0
        distinct[key] += 0
        factor_distinct[key] += 0
    counts.update({"proposals": len(proposals), "completed_proposals": len(evaluations),
                   "incomplete_proposals": len(proposals) - len(evaluations),
                   "unique_positive_cores": len(cores)})
    return {"configuration": config, "counts": dict(counts), "accounted_stage_seconds": dict(costs),
            "last_committed_elapsed": max(committed.values(), default=0),
            "raw_whole_hits": dict(raw), "distinct_whole_values": dict(distinct),
            "raw_whole_hit_rates": {key: raw[key] / len(evaluations) if evaluations else None for key in THRESHOLDS},
            "raw_whole_hit_rates_per_proposal": {key: raw[key] / len(proposals) if proposals else None for key in THRESHOLDS},
            "neutral_mass_completed": counts["neutral"] / len(evaluations) if evaluations else None,
            "first_target_hit_seconds": first_hit,
            "first_target_hit_censored_at": config["seconds"] if first_hit is None else None,
            "best_certified_positive": best, "whole_discoveries": discoveries,
            "unresolved_value_equalities": equality_cases,
            "unresolved_factor_equalities_separate": factor_equality_cases,
            "distinct_factor_values_separate": dict(factor_distinct),
            "factor_discoveries_separate": factor_discoveries,
            "events_file": str(Path(path).name)}


def write_json(path, record):
    Path(path).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


def run_supervised(degree, arm, seed, seconds, label, max_proposals=0):
    if not 0 < seconds <= 60 or degree not in DEGREES or arm not in ARMS or seed not in range(5) or max_proposals < 0:
        raise ValueError("S10 runs require D=14,18,20, the three declared arms, seeds 0..4 and 0<seconds<=60")
    if not label or any(ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" for ch in label):
        raise ValueError("label must use only letters, numbers, '-' and '_'")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    stem = OUTPUT / f"{label}_d{degree}_{arm}_s{seed}"
    events_path = stem.with_suffix(".jsonl")
    if events_path.exists() or stem.with_suffix(".json").exists():
        raise FileExistsError(f"preserve previous output; select another label: {stem.name}")
    started = time.perf_counter()
    command = [sys.executable, "-B", str(Path(__file__).resolve()), "_worker", "--degree", str(degree),
               "--arm", arm, "--seed", str(seed), "--seconds", str(seconds), "--started", str(started),
               "--events", str(events_path), "--max-proposals", str(max_proposals)]
    process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    killed = False
    try:
        _, stderr = process.communicate(timeout=max(0, seconds - (time.perf_counter() - started)))
    except subprocess.TimeoutExpired:
        killed = True
        process.kill()
        _, stderr = process.communicate()
    supervisor_elapsed = time.perf_counter() - started
    if not events_path.exists() or not read_events(events_path):
        raise RuntimeError(f"worker produced no configuration: {stderr.decode(errors='replace')}")
    record = summarize_events(events_path)
    record["supervision"] = {"killed_at_cap": killed, "worker_returncode": process.returncode,
                              "supervisor_elapsed_seconds": supervisor_elapsed,
                              "stderr": stderr.decode(errors="replace"),
                              "summary_computed_after_cap": "bookkeeping only; no polynomial evaluation or certification",
                              "shared_dependency_import_seconds": DEPENDENCY_IMPORT_SECONDS}
    if not killed and process.returncode != 0:
        record["worker_failure"] = True
    record.update(run_validity(record))
    if record["first_target_hit_seconds"] is None:
        record["first_target_hit_censored_at"] = record["observed_run_seconds"]
    write_json(stem.with_suffix(".json"), record)
    print(json.dumps({"file": stem.with_suffix(".json").name, "counts": record["counts"],
                      "distinct_whole_values": record["distinct_whole_values"],
                      "first_target_hit_seconds": record["first_target_hit_seconds"],
                      "elapsed": supervisor_elapsed}), flush=True)
    if not record["valid_run"]:
        raise RuntimeError(record["supervision"]["stderr"] or record["termination_reason"])
    return record


def run_validity(record):
    """A saved partial journal is evidence, never automatically a complete run."""
    config = record["configuration"]
    supervision = record.get("supervision", {})
    elapsed = supervision.get("supervisor_elapsed_seconds")
    observed = min(config["seconds"], elapsed) if elapsed is not None else record.get("last_committed_elapsed", 0)
    failure = bool(record.get("worker_failure")) or (
        not supervision.get("killed_at_cap", False) and supervision.get("worker_returncode") != 0)
    reached_cap = bool(supervision.get("killed_at_cap", False)) or (
        elapsed is not None and elapsed >= config["seconds"])
    reached_proposal_limit = config["max_proposals"] > 0 and (
        record["counts"].get("completed_proposals", 0) >= config["max_proposals"])
    valid = not failure and (reached_cap or reached_proposal_limit)
    reason = ("worker_failure" if failure else "deadline" if reached_cap else
              "proposal_limit" if reached_proposal_limit else "early_exit")
    return {"valid_run": valid, "termination_reason": reason,
            "observed_run_seconds": observed,
            "eligible_full_pilot_run": valid and reached_cap and config["seconds"] == 60 and config["max_proposals"] == 0}


def replay(path):
    """Independent rerun of retained discoveries; this never alters experimental yield."""
    events = read_events(path)
    config = next(event for event in events if event["kind"] == "config")
    committed = {event["proposal"] for event in events if event["kind"] == "commit" and event["elapsed"] <= config["seconds"]}
    seen, checks = set(), []
    for event in events:
        if event["kind"] != "evaluation" or event["proposal"] not in committed or "certificate" not in event:
            continue
        original = event["certificate"]
        key = tuple(original["coefficients_ascending"])
        if key in seen:
            continue
        seen.add(key)
        fresh = certify_polynomial(list(key))
        assert fresh["neutral"] == original["neutral"]
        assert fresh["core_coefficients_ascending"] == original["core_coefficients_ascending"]
        assert fresh["thresholds"] == original["thresholds"]
        assert intervals_overlap(fresh["measure_interval"], original["measure_interval"])
        assert fresh["root_count_with_multiplicity"] == len(key) - 1
        checks.append({"proposal": event["proposal"], "coefficients_ascending": list(key),
                       "measure_ball": fresh["measure_ball"], "checked": True})
    return {"kind": "separate_reference_replay", "source": Path(path).name,
            "checked_polynomials": len(checks), "checks": checks}


def comparison_report(label):
    """Aggregate already charged run results; no fitting, certification or new discovery."""
    paths = run_paths(label)
    runs = []
    for path in paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        if "configuration" not in record:
            continue
        config = record["configuration"]
        validity = run_validity(record)
        runs.append({"degree": config["degree"], "arm": config["arm"], "seed": config["seed"],
                     **validity, "supervision": record.get("supervision"),
                     "worker_failure": bool(record.get("worker_failure")),
                     "budget_seconds": config["seconds"], "max_proposals": config["max_proposals"],
                     "counts": record["counts"], "distinct_whole_values": record["distinct_whole_values"],
                     "raw_whole_hits": record["raw_whole_hits"],
                     "first_target_hit_seconds": record["first_target_hit_seconds"],
                     "first_target_hit_censored_at": validity["observed_run_seconds"]
                     if record["first_target_hit_seconds"] is None else None,
                     "neutral_mass_completed": record["neutral_mass_completed"],
                     "best_measure_ball": record["best_certified_positive"]["certificate"]["measure_ball"]
                     if record["best_certified_positive"] else None})
    groups = []
    for degree in DEGREES:
        for arm in ARMS:
            group = [run for run in runs if (run["degree"], run["arm"]) == (degree, arm)]
            if not group:
                continue
            statistics_by_threshold = {}
            for threshold in THRESHOLDS:
                values = [run["distinct_whole_values"][threshold] for run in group if run["valid_run"]]
                statistics_by_threshold[threshold] = {"median": statistics.median(values) if values else None,
                                                      "range": [min(values), max(values)] if values else None,
                                                      "valid_runs": len(values)}
            groups.append({"degree": degree, "arm": arm, "seed_outcomes": group,
                           "distinct_value_statistics": statistics_by_threshold})
    matched = []
    for degree in (18, 20):
        comparisons = []
        for seed in range(5):
            group = {run["arm"]: run for run in runs if (run["degree"], run["seed"]) == (degree, seed)
                     and run["eligible_full_pilot_run"]}
            if set(group) == set(ARMS):
                yields = {arm: run["distinct_whole_values"]["6/5"] for arm, run in group.items()}
                comparisons.append({"seed": seed, "yields": yields,
                                    "adaptive_beats_both": all(yields["adaptive"] > yields[arm] for arm in ("uniform", "fixed")),
                                    "adaptive_loses_to_either": any(yields["adaptive"] < yields[arm] for arm in ("uniform", "fixed"))})
        matched.append({"degree": degree, "matched_seeds": comparisons,
                        "wins_against_both": sum(item["adaptive_beats_both"] for item in comparisons),
                        "losses_to_either": sum(item["adaptive_loses_to_either"] for item in comparisons)})
    return {"label": label, "groups": groups, "held_out_matched_comparisons": matched,
            "invalid_runs": [{key: run[key] for key in ("degree", "arm", "seed", "termination_reason", "observed_run_seconds")}
                             for run in runs if not run["valid_run"]],
            "complete_declared_pilot": len(runs) == 45 and all(run["eligible_full_pilot_run"] for run in runs)
            and {(run["degree"], run["arm"], run["seed"]) for run in runs}
            == set(itertools.product(DEGREES, ARMS, range(5))),
            "experimental_seconds_ceiling_represented": sum(run["budget_seconds"] for run in runs),
            "interpretation": "Independent run outcomes; no within-run Bernoulli assumption or significance claim."}


def run_paths(label):
    return [path for degree in DEGREES for arm in ARMS for seed in range(5)
            if (path := OUTPUT / f"{label}_d{degree}_{arm}_s{seed}.json").is_file()]


def export_witnesses(label, destination):
    """Retain exact native inputs selected for later replay, never generated logs."""
    selected = {}
    for path in run_paths(label):
        record = json.loads(path.read_text(encoding="utf-8"))
        if "configuration" not in record:
            continue
        candidates = [(item["certificate"]["coefficients_ascending"], "whole_threshold_value") for item in record["whole_discoveries"]]
        candidates += [(item["coefficients_ascending"], "separate_irreducible_factor") for item in record["factor_discoveries_separate"]]
        candidates += [(item["certificate"]["coefficients_ascending"], "unresolved_whole_value_equality") for item in record["unresolved_value_equalities"]]
        candidates += [(item["coefficients_ascending"], "unresolved_factor_value_equality") for item in record.get("unresolved_factor_equalities_separate", [])]
        if record["best_certified_positive"]:
            candidates.append((record["best_certified_positive"]["certificate"]["coefficients_ascending"], "best_whole_output"))
        for coefficients, role in candidates:
            key = tuple(coefficients)
            item = selected.setdefault(key, {"coefficients_ascending": coefficients, "roles": [], "runs": []})
            if role not in item["roles"]:
                item["roles"].append(role)
            if path.stem not in item["runs"]:
                item["runs"].append(path.stem)
    result = {"protocol": PROTOCOL, "source_label": label,
              "purpose": "exact replay inputs; reference replay never adds stochastic discoveries",
              "witnesses": list(selected.values())}
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    write_json(destination, result)
    return result


def self_test():
    lehmer = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
    nonunit = reciprocal_polynomial([-3, 4, -4, 3, -1, -1, 3, -4, 4, -4])
    quadratic = fmpz_poly([1, -3, 1])
    controls = [("lehmer", lehmer, Fraction(1176280818, 10**9), Fraction(1176280819, 10**9)),
                ("J147_nonunit", nonunit, Fraction(118836814, 10**8), Fraction(118836815, 10**8)),
                ("repeated_exterior_roots", list(map(int, quadratic**2)), Fraction(6854, 1000), Fraction(6855, 1000))]
    records = []
    for name, coefficients, lower, upper in controls:
        certificate = certify_polynomial(coefficients)
        lo, hi = map(interval_fraction, certificate["measure_interval"])
        assert lower < lo <= hi < upper and certificate["ranking_resolved"]
        records.append({"control": name, "certificate": certificate})
    for coefficients in ([1] + [0] * 13 + [1], list(map(int, fmpz_poly([-1, 1])**14))):
        neutral = certify_polynomial(coefficients)
        assert neutral["neutral"] and neutral["measure_interval"] == [[1, 0], [1, 0]]
    compressed = [value for coefficient in lehmer[:-1] for value in (coefficient, 0)] + [1]
    padded = list(map(int, fmpz_poly(compressed) * fmpz_poly.cyclotomic(3)))
    reference = certify_polynomial(lehmer)
    assert certify_polynomial(padded)["core_coefficients_ascending"] == reference["core_coefficients_ascending"]
    assert certify_polynomial([(-1)**i * value for i, value in enumerate(lehmer)])["core_coefficients_ascending"] == reference["core_coefficients_ascending"]
    ledger = DiscoveryLedger()
    assert ledger.add(reference, 1)["status"] == "new_separated_value"
    assert ledger.add(certify_polynomial(padded), 2)["status"] == "same_core"
    ambiguous = dict(reference, core_coefficients_ascending=[2, 1])
    assert ledger.add(ambiguous, 3)["status"] == "unresolved_equality"
    for n in (7, 9, 10):
        for arm in ARMS:
            law = Law(n, arm, 0)
            assert all(len(values := law.draw()) == n and all(-4 <= x <= 4 for x in values) for _ in range(100))
    law = Law(7, "adaptive", 0)
    old = [list(block["weights"]) for block in law.blocks]
    assert law.update([])["elite_count"] == 0
    assert [block["weights"] for block in law.blocks] == old
    batch = [(tuple([k, 1]), float(k), [0] * 7) for k in range(11)]
    batch.append((tuple([0, 1]), 0.0, [0] * 7))
    assert law.update(batch)["elite_count"] == 2
    for block, previous in zip(law.blocks, old):
        for state, weight, prior in zip(block["states"], block["weights"], previous):
            expected = Fraction(4, 5) * Fraction(prior, sum(previous)) + Fraction(1, 5) * Fraction(1 + 2 * all(x == 0 for x in state), len(block["states"]) + 2)
            assert Fraction(weight, sum(block["weights"])) == expected
    return {"self_test_passed": True, "precision_bits": PRECISION_BITS,
            "python_flint": flint.__version__, "controls": records,
            "checks": ["exact neutral and repeated roots", "all exterior roots with multiplicities",
                       "J147 nonunit control", "cyclotomic padding and substitution and sign core identity",
                       "conservative overlapping-value handling", "exact adaptive smoothing and 10-percent ceiling",
                       "declared integer boxes and singleton blocks"]}


DEPENDENCY_IMPORT_SECONDS = time.perf_counter() - IMPORT_STARTED


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    test = commands.add_parser("self-test")
    test.add_argument("--output", default=str(OUTPUT / "self_test.json"))
    for name in ("run", "_worker"):
        run = commands.add_parser(name)
        run.add_argument("--degree", type=int, choices=DEGREES, required=True)
        run.add_argument("--arm", choices=ARMS, required=True)
        run.add_argument("--seed", type=int, choices=range(5), required=True)
        run.add_argument("--seconds", type=float, default=60)
        run.add_argument("--max-proposals", type=int, default=0)
        if name == "run":
            run.add_argument("--label", required=True)
        else:
            run.add_argument("--started", type=float, required=True)
            run.add_argument("--events", required=True)
    compare = commands.add_parser("compare")
    compare.add_argument("--degrees", type=int, nargs="+", choices=DEGREES, required=True)
    compare.add_argument("--seeds", type=int, nargs="+", choices=range(5), default=list(range(5)))
    compare.add_argument("--seconds", type=float, default=60)
    compare.add_argument("--label", required=True)
    for name in ("summarize", "replay"):
        command = commands.add_parser(name)
        command.add_argument("input")
        command.add_argument("--output")
    report = commands.add_parser("report")
    report.add_argument("--label", required=True)
    export = commands.add_parser("export-witnesses")
    export.add_argument("--label", required=True)
    export.add_argument("--output", required=True)
    verify = commands.add_parser("verify-witnesses")
    verify.add_argument("input")
    verify.add_argument("--output", default=str(OUTPUT / "witness_verification.json"))
    args = parser.parse_args()
    if args.command == "_worker":
        worker(args)
    elif args.command == "self-test":
        record = self_test()
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        write_json(args.output, record)
        print(json.dumps({"self_test_passed": True, "output": args.output}))
    elif args.command == "run":
        run_supervised(args.degree, args.arm, args.seed, args.seconds, args.label, args.max_proposals)
    elif args.command == "compare":
        if len(set(args.degrees)) != len(args.degrees) or len(set(args.seeds)) != len(args.seeds):
            parser.error("degrees and seeds must not repeat")
        for degree in args.degrees:
            for seed in args.seeds:
                rotation = (DEGREES.index(degree) + seed) % len(ARMS)
                for arm in ARMS[rotation:] + ARMS[:rotation]:
                    run_supervised(degree, arm, seed, args.seconds, args.label)
        write_json(OUTPUT / f"{args.label}_comparison.json", comparison_report(args.label))
    elif args.command == "summarize":
        record = summarize_events(args.input)
        write_json(args.output or str(Path(args.input).with_suffix(".summary.json")), record)
    elif args.command == "replay":
        record = replay(args.input)
        write_json(args.output or str(Path(args.input).with_suffix(".replay.json")), record)
        print(json.dumps({"checked_polynomials": record["checked_polynomials"]}))
    elif args.command == "report":
        write_json(OUTPUT / f"{args.label}_comparison.json", comparison_report(args.label))
    elif args.command == "export-witnesses":
        record = export_witnesses(args.label, args.output)
        print(json.dumps({"retained_witnesses": len(record["witnesses"])}))
    elif args.command == "verify-witnesses":
        original = json.loads(Path(args.input).read_text(encoding="utf-8"))
        checks = [certify_polynomial(item["coefficients_ascending"]) for item in original["witnesses"]]
        write_json(args.output, {"kind": "separate_reference_replay", "certificates": checks})
        print(json.dumps({"verified_witnesses": len(checks)}))


if __name__ == "__main__":
    main()
