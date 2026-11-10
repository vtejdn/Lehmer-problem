"""Native evidence and portable generation replay for the fixed D56 comparison.

Exact raw tickets reconstruct all rejected and accepted parents.  Write-ahead
intents also recover deterministic pending inputs, labelled as reconstructed,
never as observed completed work.  Replay performs no Mahler certification.
"""

import argparse
import copy
import gzip
import json
from pathlib import Path
import random

import primitive_core_sampling as live
import prior_strength_live_export as common
from archive_sampling_export import retain_failure_inputs, journal_events

GENERATION_KINDS = {"generation_start", "generation_branch", "raw_attempt_intent", "raw_attempt_ticket",
                    "raw_attempt_result", "parent_call_end", "direct_parent_choice", "parent_ready",
                    "mutation_intent", "proposal", "proposal_diagnostics"}


def read_native_comparison(path):
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def write_native_payload(path, payload):
    path = Path(path)
    if path.suffix == ".gz":
        with path.open("xb") as target:
            with gzip.GzipFile(filename="", mode="wb", fileobj=target, mtime=0) as stream:
                stream.write(payload.encode("utf-8"))
    else:
        path.write_text(payload, encoding="utf-8")


def replay_generation(events, config):
    """Rebuild exact candidates including after-cap records; ignore elapsed time."""
    rng = random.Random(config["seed"])
    degree, variant = config["degree"], config["variant"]
    parents = live.direct_parents(degree) if variant == "direct" else []
    dp = live.ParentSampler(live.SEED_CORE, degree, 4) if variant == "dp_closure" else None
    request = attempt = completed = accepted = rejected = proposals = 0
    state = None
    tickets_observed, reconstructed = 0, {}
    for event in events:
        kind = event["kind"]
        if kind == "generation_start":
            request += 1
            assert event["request"] == request
            assert state is None or state["phase"] == "proposed"
            state = {"request": request, "phase": "branch_selection_pending", "branch_ticket": None,
                     "branch": None, "parent": None, "prefix": None, "mutation": None,
                     "attempts": 0, "results": [], "ticket": None}
        elif kind == "generation_branch":
            ticket = rng.randrange(10)
            branch = "uniform_box" if ticket == 0 else variant
            assert event["request"] == request and event["branch_ticket"] == ticket and event["branch"] == branch
            state.update(branch_ticket=ticket, branch=branch, phase="parent_selection_pending")
            if branch == "uniform_box":
                state.update(prefix=[rng.randrange(-4, 5) for _ in range(degree // 2)], phase="uniform_polynomial_pending")
        elif kind == "direct_parent_choice":
            index = rng.randrange(len(parents))
            assert event["request"] == request and event["template_index"] == index
            state.update(parent=parents[index], phase="parent_record_pending")
        elif kind == "raw_attempt_intent":
            assert state["branch"] == "dp_closure"
            assert not any(state["results"])
            attempt += 1
            state["attempts"] += 1
            assert (event["request"], event["attempt"], event["request_attempt"]) == (request, attempt, state["attempts"])
            substitution_ticket = rng.randrange(dp.weight_sum)
            index = dp.select_k(substitution_ticket)
            sign_ticket = rng.randrange(2)
            neutral_ticket = rng.randrange(dp.weights[index - 1])
            ticket = {"substitution_ticket": substitution_ticket, "substitution_index": index,
                      "sign_ticket": sign_ticket, "sign": (-1, 1)[sign_ticket], "neutral_ticket": neutral_ticket}
            state.update(ticket=ticket, phase="raw_selection_pending")
        elif kind == "raw_attempt_ticket":
            assert event["attempt"] == attempt and event["request"] == request
            assert state["phase"] == "raw_selection_pending"
            assert all(event[key] == value for key, value in state["ticket"].items())
            tickets_observed += 1
            state["phase"] = "raw_construction_pending"
        elif kind == "raw_attempt_result":
            assert event["attempt"] == attempt and event["request"] == request
            assert state["phase"] == "raw_construction_pending"
            ticket = state["ticket"]
            candidate = dp.construct(ticket["substitution_index"], ticket["sign"], ticket["neutral_ticket"])
            for key in ("substitution_index", "sign", "neutral_ticket", "observed_height", "accepted"):
                assert event[key] == candidate[key]
            if candidate["accepted"]:
                for key in ("coefficients_ascending", "neutral_factor_powers"):
                    assert event[key] == candidate[key]
            completed += 1
            accepted += candidate["accepted"]
            rejected += not candidate["accepted"]
            state["results"].append(candidate["accepted"])
            state.update(candidate=candidate, phase="parent_call_return_pending" if candidate["accepted"] else "next_raw_attempt_pending")
        elif kind == "parent_call_end":
            assert event["request"] == request
            assert event["attempts_started"] == len(state["results"]) == state["attempts"]
            assert event["height_rejections"] == sum(not value for value in state["results"])
            assert event["max_attempts"] == live.MAX_ATTEMPTS
            if event["status"] == "accepted":
                assert state["results"][-1] and sum(state["results"]) == 1
                state.update(parent=live.parent_with_neutral(state["candidate"]), phase="parent_record_pending")
            elif event["status"] == "attempt_limit":
                assert len(state["results"]) == live.MAX_ATTEMPTS and not any(state["results"])
                state["phase"] = "parent_attempt_limit"
            else:
                assert event["status"] == "deadline" and not any(state["results"])
                state["phase"] = "parent_deadline"
        elif kind == "parent_ready":
            assert event["request"] == request and event["parent"] == state["parent"]
            state["phase"] = "mutation_not_started"
        elif kind == "mutation_intent":
            assert event["request"] == request and state["parent"] is not None
            prefix, mutation = live.mutate(state["parent"], rng, degree)
            state.update(prefix=prefix, mutation=mutation, phase="mutated_polynomial_pending")
        elif kind == "proposal":
            proposals += 1
            assert event["proposal"] == proposals and event["request"] == request
            assert event["free_coefficients"] == state["prefix"]
            assert event["coefficients_ascending"] == live.frozen.reciprocal_polynomial(state["prefix"])
            generation = {"status": "proposed", "free_coefficients": state["prefix"], "branch": state["branch"],
                          "parent": state["parent"], "mutation": state["mutation"]}
            assert event["generation"] == generation
            reconstructed[proposals] = generation
            state["phase"] = "proposed"
        elif kind == "proposal_diagnostics":
            generation = reconstructed[event["proposal"]]
            assert live.parent_diagnostics(generation, live.frozen.reciprocal_polynomial(generation["free_coefficients"])) == event["parent_neutral"]
    pending = None
    if state is not None and state["phase"] != "proposed":
        pending = {"request": request, "observed_phase": state["phase"],
                   "scope": "deterministic reconstruction of pending input; not an observed completion or discovery"}
        if state["ticket"] is not None and state["phase"] in ("raw_selection_pending", "raw_construction_pending"):
            pending["raw_ticket"] = state["ticket"]
            pending["reconstructed_raw_candidate"] = dp.construct(state["ticket"]["substitution_index"],
                state["ticket"]["sign"], state["ticket"]["neutral_ticket"])
        if state["prefix"] is not None:
            pending["coefficients_ascending"] = live.frozen.reciprocal_polynomial(state["prefix"])
            pending["free_coefficients"] = state["prefix"]
        if state["parent"] is not None:
            pending["parent"] = state["parent"]
        if state["phase"] == "parent_call_return_pending":
            pending["observed_accepted_parent_candidate"] = state["candidate"]
        if state["phase"] == "parent_selection_pending" and state["branch"] == "direct":
            index = rng.randrange(len(parents))
            pending["reconstructed_template_index"] = index
            pending["parent"] = parents[index]
        if state["phase"] == "branch_selection_pending":
            pending["reconstructed_branch_ticket"] = rng.randrange(10)
    return {"requests_started": request, "raw_attempt_intents": attempt, "raw_attempts_completed": completed,
            "accepted_parents": accepted, "height_rejections": rejected, "journalled_whole_proposals": proposals,
            "raw_tickets_observed": tickets_observed, "pending_generation": pending}


def pack_events(events):
    """Lossless native row table, preserving missing versus explicit null fields."""
    schemas, indexed, rows = [], {}, []
    for event in events:
        fields = tuple(sorted(key for key in event if key != "kind"))
        key = (event["kind"], fields)
        if key not in indexed:
            indexed[key] = len(schemas)
            schemas.append({"kind": event["kind"], "fields": list(fields)})
        rows.append([indexed[key], *(event[field] for field in fields)])
    return {"encoding": "each row is schema_index followed by values in that schema's field order",
            "schemas": schemas, "rows": rows}


def unpack_events(table):
    for row in table["rows"]:
        schema = table["schemas"][row[0]]
        assert len(row) == len(schema["fields"]) + 1
        yield {"kind": schema["kind"], **dict(zip(schema["fields"], row[1:]))}


def compact_certificate(certificate):
    result = common.compact_whole(certificate)
    result["factors"] = [common.compact_factor(factor) for factor in certificate["factors"]]
    result["root_certificate_reproduction"] = "sampler.certify_polynomial on the exact coefficients at retained precision"
    return result


def compact_tree(value):
    if isinstance(value, dict):
        if "coefficients_ascending" in value and "measure_interval" in value and "factors" in value and "neutral" in value:
            return compact_certificate(value)
        return {key: compact_tree(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact_tree(item) for item in value]
    return value


def validate_journal_evidence(record, journal, events):
    """Require the recorded summary to agree with the still-available evidence.

    A failed run can also have required generated or pending inputs.  Only the
    runtime's explicit no-configuration startup record permits no journal.
    Rebuilding uses recorded certificates and arithmetic bookkeeping, no roots.
    """
    configured = any(event["kind"] == "config" for event in events)
    if configured:
        expected = live.frozen.summarize_events(journal)
        # These are supervisor observations, not facts inferred from a journal.
        for key in ("worker_failure", "requested_configuration", "configuration_mismatch"):
            if key in record:
                expected[key] = copy.deepcopy(record[key])
    else:
        if events or record.get("configuration_source") != "requested; worker produced no configuration":
            raise ValueError(f"required journal evidence missing or incomplete: {journal.name}")
        expected = {"configuration": copy.deepcopy(record["configuration"]),
                    "counts": {"proposals": 0, "completed_proposals": 0},
                    "configuration_source": "requested; worker produced no configuration",
                    "last_committed_elapsed": 0, "first_target_hit_seconds": None,
                    "first_target_hit_censored_at": None, "worker_failure": True,
                    "distinct_whole_values": {key: 0 for key in live.frozen.THRESHOLDS},
                    "raw_whole_hits": {key: 0 for key in live.frozen.THRESHOLDS},
                    "best_certified_positive": None, "neutral_mass_completed": None}
    expected["supervision"] = copy.deepcopy(record["supervision"])
    expected.update(live.validity(expected))
    if expected["first_target_hit_seconds"] is None:
        expected["first_target_hit_censored_at"] = expected["observed_run_seconds"]
    live.enrich(expected, events)
    # Compare the complete raw summary, including scalar types, not merely its
    # valid/invalid label or within-budget completion count.  Generation fields
    # also cover after-cap proposals and interruptions before a whole proposal.
    encode = lambda value: json.dumps(value, sort_keys=True, separators=(",", ":"))
    different = [key for key in sorted(set(record) | set(expected))
                 if key not in record or key not in expected or encode(record[key]) != encode(expected[key])]
    if different:
        raise ValueError(f"journal/summary evidence mismatch for {journal.name}: {', '.join(different)}")
    return configured


def retain_run(record, path, witnesses):
    journal = path.with_suffix(".jsonl")
    events = list(journal_events(journal)) if journal.is_file() else []
    configured = validate_journal_evidence(record, journal, events)
    config = record["configuration"]
    budget = config["seconds"]
    commits = {event["proposal"]: event["elapsed"] for event in events if event["kind"] == "commit"}
    proposals = {event["proposal"]: event for event in events if event["kind"] == "proposal"}
    row = compact_tree(copy.deepcopy(record))
    if not configured:
        row["generation_evidence_scope"] = "recorded startup failure with no complete configuration or generation event; no candidate input is invented"
    row.update(degree=config["degree"], arm=config["variant"], seed=config["seed"], source_summary=path.name)
    generation_events = [event for event in events if event["kind"] in GENERATION_KINDS]
    row["generation_trace"] = pack_events(generation_events)
    assert list(unpack_events(row["generation_trace"])) == generation_events
    row["retry_inputs"] = retain_failure_inputs(events, budget)
    row["evaluation_observations"] = []
    initialization = row["initialization_observation"]
    if initialization:
        initialization["seed_witness_id"] = witnesses.add(initialization["seed_certificate"]["coefficients_ascending"], "supplied_seed_not_discovery", path.stem)
    for event in events:
        if event["kind"] != "evaluation":
            continue
        item = compact_tree(event)
        proposal = event["proposal"]
        committed = proposal in commits and commits[proposal] <= budget
        item.update(committed=committed, commit_elapsed=commits.get(proposal),
                    exact_proposal=proposals[proposal], excluded_from_yield=not committed or "unresolved_error" in event)
        if "certificate" in item:
            item["whole_witness_id"] = witnesses.add(item["certificate"]["coefficients_ascending"],
                "completed_whole_certificate" if committed else "uncommitted_whole_certificate_no_yield", path.stem)
            item["factor_witness_ids"] = [witnesses.add(factor["coefficients_ascending"], "irreducible_factor_certificate", path.stem)
                                          for factor in item["certificate"]["factors"]]
        row["evaluation_observations"].append(item)
    row["generation_replay"] = replay_generation(unpack_events(row["generation_trace"]), config)
    return row


def build_exports(label, allow_partial=False, paths=None):
    if paths is not None and not label.startswith("control_"):
        raise ValueError("explicit paths are restricted to controls")
    paths = live.run_paths(label) if paths is None else list(map(Path, paths))
    if not paths or (len(paths) != 10 and not allow_partial):
        raise ValueError("ten runs required; partial observations need explicit --allow-partial")
    report = live.report(label, paths)
    witnesses = common.Witnesses()
    indexed = {}
    for path in paths:
        record = common.read_json(path)
        config = record["configuration"]
        key = (config["variant"], config["seed"])
        assert key not in indexed
        indexed[key] = (record, path)
    for group in report["groups"]:
        group["all_seed_outcomes"] = [retain_run(*indexed[(row["arm"], row["seed"])], witnesses)
                                      for row in group["all_seed_outcomes"]]
    document = {"protocol": live.PROTOCOL, "source_label": label,
                "scope": "exact certificate replay inputs; no replay adds historical discovery credit",
                "witnesses": list(witnesses.by_coefficients.values())}
    report["retained_run_count"] = len(paths)
    report["retention_scope"] = "All started raw inputs and generated proposals, compact complete certificates for every journalled successful evaluation, original costs, failed inputs and pending-generation stages; no timing reconstruction."
    validate(report, document)
    return report, document


def validate(report, witnesses):
    by_id = {item["witness_id"]: item["coefficients_ascending"] for item in witnesses["witnesses"]}
    assert len(by_id) == len(witnesses["witnesses"]) == len({tuple(item) for item in by_id.values()})
    used = set()
    for group in report["groups"]:
        for row in group["all_seed_outcomes"]:
            if row["initialization_observation"]:
                item = row["initialization_observation"]
                assert by_id[item["seed_witness_id"]] == item["seed_certificate"]["coefficients_ascending"]
                used.add(item["seed_witness_id"])
            for item in row["evaluation_observations"]:
                if "certificate" not in item:
                    continue
                assert by_id[item["whole_witness_id"]] == item["certificate"]["coefficients_ascending"] == item["exact_proposal"]["coefficients_ascending"]
                used.add(item["whole_witness_id"])
                assert len(item["certificate"]["factors"]) == len(item["factor_witness_ids"])
                for factor, witness_id in zip(item["certificate"]["factors"], item["factor_witness_ids"]):
                    assert by_id[witness_id] == factor["coefficients_ascending"]
                    used.add(witness_id)
    assert used == set(by_id)


def write_exports(label, comparison, witnesses, allow_partial=False, paths=None):
    comparison, witnesses = Path(comparison), Path(witnesses)
    if comparison.resolve() == witnesses.resolve() or comparison.exists() or witnesses.exists():
        raise FileExistsError("preserve occupied or coincident export paths")
    result, document = build_exports(label, allow_partial, paths)
    payloads = [(comparison, json.dumps(result, separators=(",", ":")) + "\n"), (witnesses, json.dumps(document, indent=2) + "\n")]
    for path, payload in payloads:
        path.parent.mkdir(parents=True, exist_ok=True)
        write_native_payload(path, payload)
    return result, document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export")
    export.add_argument("--label", required=True)
    export.add_argument("--allow-partial", action="store_true")
    export.add_argument("--comparison", type=Path, default=live.HERE / "inputs" / "primitive_comparison.json.gz")
    export.add_argument("--witnesses", type=Path, default=live.HERE / "inputs" / "primitive_witnesses.json")
    commands.add_parser("replay-retained").add_argument("comparison", type=Path)
    args = parser.parse_args()
    if args.command == "export":
        comparison, witnesses = write_exports(args.label, args.comparison, args.witnesses, args.allow_partial)
        print(json.dumps({"runs": comparison["retained_run_count"], "witnesses": len(witnesses["witnesses"])}))
    else:
        record = read_native_comparison(args.comparison)
        assert record["protocol"] == live.PROTOCOL
        results = []
        for group in record["groups"]:
            for row in group["all_seed_outcomes"]:
                replay = replay_generation(unpack_events(row["generation_trace"]), row["configuration"])
                assert replay == row["generation_replay"]
                results.append({key: replay[key] for key in ("requests_started", "raw_attempt_intents", "raw_attempts_completed", "journalled_whole_proposals")})
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
