"""Nonmathematical subprocess/journal bookkeeping for new J156 comparisons.

Frozen callers are not changed. The caller selects the protocol, degree and
already defined Law class; the frozen sampler still performs every evaluation.
"""

import argparse
from pathlib import Path
import subprocess
import sys
import time

import sampler as frozen


def worker(args, configuration, law_class, implementation_arm):
    original_law, original_write = frozen.Law, frozen.write_event

    def write_event(stream, event):
        if event["kind"] == "config":
            assert event["degree"] == args.degree and event["seed"] == args.seed
            event = {**event, **configuration, "controlled_failure_check": args.fail_after_first_proposal}
        original_write(stream, event)
        if args.fail_after_first_proposal and event["kind"] == "proposal":
            raise RuntimeError("deliberate sampling-runtime failure after first proposal")

    frozen.Law, frozen.write_event = law_class, write_event
    try:
        frozen.worker(argparse.Namespace(degree=args.degree, arm=implementation_arm, seed=args.seed,
                                         seconds=args.seconds, started=args.started,
                                         events=args.events, max_proposals=args.max_proposals))
    finally:
        frozen.Law, frozen.write_event = original_law, original_write


def supervise(entrypoint, stem, args, configuration, failure_check=False):
    """Return an observed result, including failures; the caller persists it."""
    events = stem.with_suffix(".jsonl")
    if events.exists() or stem.with_suffix(".json").exists():
        raise FileExistsError(f"preserve existing output; choose another label: {stem.name}")
    stem.parent.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    command = [sys.executable, "-B", str(Path(entrypoint).resolve()), "_worker",
               "--degree", str(args.degree), "--variant", args.variant, "--seed", str(args.seed),
               "--seconds", str(args.seconds), "--started", str(started),
               "--events", str(events), "--max-proposals", str(args.max_proposals)]
    if failure_check:
        command.append("--fail-after-first-proposal")
    killed, returncode, stderr = False, None, b""
    try:
        process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                                   creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except OSError as error:
        stderr = repr(error).encode()
        returncode = -1
    else:
        try:
            _, stderr = process.communicate(timeout=max(0, args.seconds - (time.perf_counter() - started)))
        except subprocess.TimeoutExpired:
            killed = True
            process.kill()
            _, stderr = process.communicate()
        returncode = process.returncode
    elapsed = time.perf_counter() - started
    journal = frozen.read_events(events) if events.exists() else []
    if any(event["kind"] == "config" for event in journal):
        record = frozen.summarize_events(events)
        actual = record["configuration"]
        if any(actual.get(key) != configuration[key] for key in ("protocol", "degree", "variant", "seed")):
            record["worker_failure"] = True
            record["requested_configuration"] = configuration
            record["configuration_mismatch"] = True
    else:
        config = {**configuration, "seconds": args.seconds, "max_proposals": args.max_proposals,
                  "controlled_failure_check": failure_check}
        record = {"configuration": config, "counts": {"proposals": 0, "completed_proposals": 0},
                  "configuration_source": "requested; worker produced no configuration",
                  "last_committed_elapsed": 0, "first_target_hit_seconds": None,
                  "first_target_hit_censored_at": None, "worker_failure": True,
                  "distinct_whole_values": {key: 0 for key in frozen.THRESHOLDS},
                  "raw_whole_hits": {key: 0 for key in frozen.THRESHOLDS},
                  "best_certified_positive": None, "neutral_mass_completed": None}
    record["supervision"] = {"killed_at_cap": killed, "worker_returncode": returncode,
                              "supervisor_elapsed_seconds": elapsed, "stderr": stderr.decode(errors="replace"),
                              "summary_computed_after_cap": "bookkeeping only; no polynomial evaluation or certification",
                              "shared_dependency_import_seconds": frozen.DEPENDENCY_IMPORT_SECONDS}
    if not killed and returncode != 0:
        record["worker_failure"] = True
    validity = frozen.run_validity(record)
    validity.pop("eligible_full_pilot_run")
    record.update(validity)
    if record["first_target_hit_seconds"] is None:
        record["first_target_hit_censored_at"] = record["observed_run_seconds"]
    return record
