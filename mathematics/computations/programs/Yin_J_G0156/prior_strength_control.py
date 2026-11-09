"""Exact fixed-elite mechanism control in the existing J156 computation.

O adds one pseudocount to each pair state (total 81).
A adds 1/81 to each pair state (total 1); singleton pseudocounts stay one.
Both retain 4/5 of the previous law and use the SAME 13 recorded elite batches.
No new proposals, roots, scores, or factorization are computed.
A uses the recorded elites; extraction checks O's original elite selection.
Target coefficients enter only the later evaluation of the already replayed laws.

`extract` verifies the source journal with the frozen sampler.Law and retains
only the 13 elite batches and necessary source parameters.
`run` uses only Python's standard library, Fraction arithmetic, those native
elites, and the separately reproducible degree-14 reference census.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import itertools
import json
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
DEFAULT_INPUT = HERE / "inputs" / "prior_strength_elites_d14.json"
ALPHABET = tuple(range(-4, 5))
FIXED_WEIGHTS = (1, 2, 4, 8, 16, 8, 4, 2, 1)
HALF_DEGREE = 7
UPDATES = 13
COMMITTED_PROPOSALS = 3432
FOCUS_UPDATES = (1, 13)
BLOCKS = tuple((start, min(2, HALF_DEGREE - start),
                tuple(itertools.product(ALPHABET, repeat=min(2, HALF_DEGREE - start))))
               for start in range(0, HALF_DEGREE, 2))


def initial_law():
    return tuple(tuple(prod(F(FIXED_WEIGHTS[k + 4], 46) for k in state)
                       for state in states) for _, _, states in BLOCKS)


def update_law(law, elite, variant):
    if variant not in ("O", "A"):
        raise ValueError("variant must be O or A")
    if not elite:
        return law
    updated = []
    for (start, width, states), probabilities in zip(BLOCKS, law):
        counts = Counter(tuple(vector[start:start + width]) for vector in elite)
        prior = F(1, 81) if variant == "A" and width == 2 else F(1)
        denominator = len(elite) + len(states) * prior
        values = tuple(F(4, 5) * old + F(1, 5) * (counts[state] + prior) / denominator
                       for old, state in zip(probabilities, states))
        assert all(value > 0 for value in values) and sum(values) == 1
        updated.append(values)
    return tuple(updated)


def fraction_record(value):
    # Decimal fields are displays; every decision below uses exact Fraction.
    return {"numerator": str(value.numerator), "denominator": str(value.denominator),
            "decimal": float(value)}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def write_elites(path, value):
    """One compact native row per batch, without copying the full event journal."""
    metadata = {key: item for key, item in value.items() if key != "batches"}
    prefix = json.dumps(metadata, indent=2)[:-2]
    rows = ",\n".join("    " + json.dumps(batch, separators=(",", ":")) for batch in value["batches"])
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(prefix + ',\n  "batches": [\n' + rows + "\n  ]\n}\n", encoding="utf-8")


def validate_input(data):
    source = data["source"]
    assert source["degree"] == 14 and source["arm"] == "adaptive" and source["seed"] == 0
    assert source["committed_proposals"] == COMMITTED_PROPOSALS
    assert len(data["batches"]) == UPDATES
    for index, batch in enumerate(data["batches"], 1):
        assert batch["proposal"] == 256 * index
        elite = batch["elite_free_coefficients"]
        assert 1 <= len(elite) <= 26
        assert len(elite) == (batch["unique_eligible_cores"] + 9) // 10
        assert len({tuple(vector) for vector in elite}) == len(elite)
        for vector in elite:
            assert len(vector) == HALF_DEGREE
            assert all(type(value) is int and value in ALPHABET for value in vector)


def extract(journal):
    # The import is limited to extraction; the actual control is Fraction-only.
    from sampler import Law

    law, config, proposal, evaluation = None, None, None, None
    original = initial_law()
    batch, retained, committed = [], [], []
    with Path(journal).open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                break
            if event["kind"] == "config":
                config = event
                assert (config["degree"], config["arm"], config["seed"]) == (14, "adaptive", 0)
                assert config["batch_size"] == 256
                law = Law(HALF_DEGREE, "adaptive", 0)
            elif event["kind"] == "proposal":
                proposal, evaluation = event, None
            elif event["kind"] == "evaluation":
                evaluation = event
            elif event["kind"] == "commit" and event["elapsed"] <= config["seconds"]:
                number = event["proposal"]
                assert proposal["proposal"] == evaluation["proposal"] == number
                assert number == len(committed) + 1
                committed.append(number)
                if not evaluation.get("unresolved_error") and evaluation["ranking_resolved"] and not evaluation["neutral"]:
                    batch.append((tuple(evaluation["core_coefficients_ascending"]),
                                  evaluation["log_score"], proposal["free_coefficients"]))
                if number % 256 == 0:
                    checked_update = law.update(batch)
                    assert checked_update == evaluation["update"]
                    elite = checked_update["elite_free_coefficients"]
                    assert elite
                    original = update_law(original, elite, "O")
                    for probabilities, block in zip(original, law.blocks):
                        assert probabilities == tuple(F(weight, sum(block["weights"])) for weight in block["weights"])
                    retained.append({"proposal": number,
                                     "unique_eligible_cores": checked_update["unique_eligible_cores"],
                                     "elite_free_coefficients": elite})
                    batch.clear()
    assert len(committed) == COMMITTED_PROPOSALS and len(retained) == UPDATES
    result = {"scope": "Fixed-data pair-prior-strength mechanism control; not new sampling or pilot data.",
              "source": {"program": "sampler.py", "journal_name": Path(journal).name,
                         "degree": 14, "arm": "adaptive", "seed": 0,
                         "seconds_ceiling": config["seconds"], "max_proposals": config["max_proposals"],
                         "committed_proposals": len(committed), "precision_bits": config["precision_bits"],
                         "ranking_radius": config["ranking_radius"],
                         "regenerate_journal_arguments": ["run", "--degree", "14", "--arm", "adaptive", "--seed", "0",
                                                          "--seconds", "60", "--max-proposals", "3432",
                                                          "--label", "diagnostic_reproduction"],
                         "extraction_check": "Every retained update and all exact O block probabilities matched frozen sampler.Law replay."},
              "batches": retained}
    validate_input(result)
    return result


def replay_laws(data):
    """This stage has no reference-target argument or reference-target reads."""
    validate_input(data)
    original = alternative = initial_law()
    snapshots = [(0, original, alternative)]
    for index, batch in enumerate(data["batches"], 1):
        elite, m = batch["elite_free_coefficients"], len(batch["elite_free_coefficients"])
        previous_original, previous_alternative = original, alternative
        original = update_law(original, elite, "O")
        alternative = update_law(alternative, elite, "A")
        for block_index, (start, width, states) in enumerate(BLOCKS):
            if width == 1:
                assert original[block_index] == alternative[block_index]
                continue
            counts = Counter(tuple(vector[start:start + width]) for vector in elite)
            for state_index, state in enumerate(states):
                # Exact common-data difference identity, independent of target mass.
                difference = alternative[block_index][state_index] - original[block_index][state_index]
                retained_difference = F(4, 5) * (previous_alternative[block_index][state_index] - previous_original[block_index][state_index])
                expected = F(80 * m, 5 * (m + 1) * (m + 81)) * (F(counts[state], m) - F(1, 81))
                assert difference - retained_difference == expected
            moment = sum(probability * sum(map(abs, state)) for probability, state in zip(original[block_index], states))
            lower_bound = F(4, 5)**index * F(52, 23) + (1 - F(4, 5)**index) * F(360, 107)
            assert moment >= lower_bound
        snapshots.append((index, original, alternative))
    return snapshots


def target_mass(law, targets):
    probabilities = [dict(zip(states, block)) for (_, _, states), block in zip(BLOCKS, law)]
    biased_mass = sum(prod(probability[tuple(target[start:start + width])]
                           for (start, width, _), probability in zip(BLOCKS, probabilities))
                      for target in targets)
    return F(len(targets), 10 * 9**HALF_DEGREE) + F(9, 10) * biased_mass


def block_moments(law):
    return [sum(probability * sum(map(abs, state)) for state, probability in zip(states, block))
            for (_, _, states), block in zip(BLOCKS, law)]


def classify(original_final, alternative_final, initial):
    if alternative_final <= original_final:
        return "no_improvement_on_fixed_data_path"
    if alternative_final < initial:
        return "partial_recovery_below_initial_mass"
    return "restored_or_exceeded_initial_mass_on_fixed_data_path"


def run_control(input_path, reference_path):
    data = read_json(input_path)
    snapshots = replay_laws(data)
    # Read the target set only AFTER all laws have been reconstructed.
    reference = read_json(reference_path)
    row = next(row for row in reference["results"] if row["degree"] == 14)
    targets = row["target_prefixes"]
    assert len(targets) == len({tuple(vector) for vector in targets}) == 26
    assert all(len(vector) == 7 and all(type(k) is int and -4 <= k <= 4 for k in vector) for vector in targets)
    initial = target_mass(snapshots[0][1], targets)
    expected = row["static_mixture_target_probability"]
    assert initial == F(int(expected["numerator"]), int(expected["denominator"]))
    records = []
    for index, original, alternative in snapshots:
        record = {"update": index, "proposal": index * 256}
        for name, law in (("O", original), ("A", alternative)):
            mass = target_mass(law, targets)
            record[name] = {"target_mass": fraction_record(mass),
                            "relative_to_initial": fraction_record(mass / initial),
                            "block_expected_absolute_sums": [fraction_record(value) for value in block_moments(law)]}
        records.append(record)
    original_final = target_mass(snapshots[-1][1], targets)
    alternative_final = target_mass(snapshots[-1][2], targets)
    return {"question": "Does reducing only pair prior strength remove target-mass loss on this fixed elite path?",
            "arithmetic": "exact Fraction for laws, masses, moments and decisions; decimal fields are displays only",
            "degree": 14, "seed_of_source": 0, "updates": UPDATES,
            "input_name": Path(input_path).name, "reference_name": Path(reference_path).name,
            "original_pair_prior_total": 81, "alternative_pair_prior_total": 1,
            "prior_center": "uniform for both O and A", "singleton_prior_total_both": 9,
            "focus_updates_fixed_in_advance": list(FOCUS_UPDATES),
            "three_way_rule": ["A_final <= O_final: no improvement on the fixed path",
                               "O_final < A_final < initial: partial recovery below initial",
                               "A_final > O_final and A_final >= initial: restored or exceeded initial"],
            "decision": classify(original_final, alternative_final, initial),
            "focus": [record for record in records if record["update"] in FOCUS_UPDATES],
            "snapshots": records,
            "checks": {"normalization_and_positive_probabilities": True,
                       "exact_pair_difference_identity_all_13_updates": True,
                       "singleton_laws_identical_all_13_updates": True,
                       "original_pair_moment_lower_bound_all_13_updates": True,
                       "initial_mass_matches_reference_exactly": True},
            "interpretation": "Fixed-elite mechanism replay only; alternative proposals and elite selection would differ in a live run. No new search yield, root certification, pilot outcome or blind evaluation is supplied."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    extraction = commands.add_parser("extract")
    extraction.add_argument("--journal", type=Path, required=True)
    extraction.add_argument("--output", type=Path, default=DEFAULT_INPUT)
    run = commands.add_parser("run")
    run.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    run.add_argument("--reference", type=Path, default=OUTPUT / "baseline_mass.json")
    run.add_argument("--output", type=Path, default=OUTPUT / "prior_strength_control.json")
    args = parser.parse_args()
    if args.command == "extract":
        result = extract(args.journal)
        write_elites(args.output, result)
        assert read_json(args.output) == result
        print(json.dumps({"updates_extracted": len(result["batches"]),
                          "original_Law_exact_matches": len(result["batches"]),
                          "elite_counts": [len(batch["elite_free_coefficients"]) for batch in result["batches"]],
                          "output": str(args.output)}))
    else:
        result = run_control(args.input, args.reference)
        write_json(args.output, result)
        print(json.dumps({"decision": result["decision"],
                          "focus": [{"update": item["update"],
                                     "O_mass": item["O"]["target_mass"]["decimal"],
                                     "A_mass": item["A"]["target_mass"]["decimal"],
                                     "O_relative_initial": item["O"]["relative_to_initial"]["decimal"],
                                     "A_relative_initial": item["A"]["relative_to_initial"]["decimal"]}
                                    for item in result["focus"]]}))


if __name__ == "__main__":
    main()
