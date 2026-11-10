"""Check fixed core-mass arithmetic, optionally its committed-journal provenance.

The default mode requires only the three native JSON inputs and the standard
library. Provenance mode additionally reads the ten original A journals, both
previous census outputs, and the separately replayed extraction/evaluation. It uses FLINT
only for exact target factorization, with no new roots or sampling run.
"""

import argparse
from collections import Counter
from fractions import Fraction as F
import itertools
import json
from math import gcd, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
ALPHABET = tuple(range(-4, 5))
WEIGHTS = (1, 2, 4, 8, 16, 8, 4, 2, 1)
LEHMER = (1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1)


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def rational(record):
    value = F(int(record["numerator"]), int(record["denominator"]))
    assert value.numerator == int(record["numerator"])
    assert value.denominator == int(record["denominator"])
    assert record["decimal"] == float(value)
    return value


def distributions(blocks):
    result = []
    for block in blocks:
        states = list(itertools.product(ALPHABET, repeat=block["width"]))
        weights = block["weights"]
        assert len(states) == len(weights) and gcd(*weights) == 1
        assert all(type(weight) is int and weight > 0 for weight in weights)
        result.append(dict(zip(states, (F(weight, sum(weights)) for weight in weights))))
    assert all(sum(distribution.values()) == 1 for distribution in result)
    return result


def independent_mass(blocks, targets, half, initial=False):
    # Each prefix is independently normalized; this does not use the author's
    # aggregate numerator, common denominator, or base-nine index function.
    state_probabilities = distributions(blocks)
    biased = F(0)
    for prefix in targets:
        if initial:
            biased += prod(F(WEIGHTS[value + 4], 46) for value in prefix)
        else:
            value = F(1)
            for block, distribution in zip(blocks, state_probabilities):
                start, width = block["start"], block["width"]
                value *= distribution[tuple(prefix[start:start + width])]
            biased += value
    return F(len(targets), 10 * 9**half) + F(9, 10) * biased


def fixed_checks(states, comparison, result):
    assert states["protocol"] == result["protocol"] == "S10-degree-validation-core-mass-postrun"
    assert comparison["protocol"] == "S10-degree-validation" and comparison["complete_declared_degree_validation"]
    assert states["source_label"] == result["source_label"] == comparison["label"]
    source = {(row["degree"], row["seed"]): row for group in comparison["groups"]
              for row in group["all_seed_outcomes"] if row["arm"] == "A"}
    expected = set(itertools.product((18, 20), range(10, 15)))
    assert set(source) == expected and len(states["final_laws"]) == len(result["runs"]) == 10
    laws = {(row["degree"], row["seed"]): row for row in states["final_laws"]}
    rows = {(row["degree"], row["seed"]): row for row in result["runs"]}
    assert set(laws) == set(rows) == expected
    partitions = {part["degree"]: part for part in states["target_partitions"]}
    assert len(states["target_partitions"]) == 2 and set(partitions) == {18, 20}
    for degree, partition in partitions.items():
        groups = partition["core_groups"]
        assert len(groups) == 2 and len({tuple(group["core_coefficients_ascending"]) for group in groups}) == 2
        assert sorted(group["count"] for group in groups) == ([2, 174] if degree == 18 else [10, 344])
        prefixes = [tuple(prefix) for group in groups for prefix in group["target_prefixes"]]
        assert len(prefixes) == len(set(prefixes)) == partition["strict_target_count"] == (176 if degree == 18 else 354)
        assert all(len(prefix) == degree // 2 and all(type(value) is int and value in ALPHABET for value in prefix)
                   for prefix in prefixes)
    observed = []
    for key in sorted(expected):
        degree, seed = key
        state, actual, original = laws[key], rows[key], source[key]
        blocks, half = state["blocks"], degree // 2
        assert original["valid_run"] and original["eligible_degree_validation_run"]
        assert state["source_summary"] == original["source_summary"]
        assert state["completed_proposals"] == original["counts"]["completed_proposals"]
        assert state["updates_replayed"] == actual["updates_replayed"] == original["counts"]["adaptive_updates"]
        assert state["last_committed_update_proposal"] == actual["last_committed_update_proposal"] == 256 * state["updates_replayed"]
        assert 0 <= state["last_committed_update_elapsed"] <= original["last_committed_elapsed"] <= 10
        assert [(block["start"], block["width"]) for block in blocks] == [(start, min(2, half-start)) for start in range(0, half, 2)]
        actual_groups = {tuple(group["core_coefficients_ascending"]): group for group in actual["core_groups"]}
        assert len(actual["core_groups"]) == 2
        assert set(actual_groups) == {tuple(group["core_coefficients_ascending"]) for group in partitions[degree]["core_groups"]}
        initial_total = final_total = F(0)
        group_rows = []
        for group in partitions[degree]["core_groups"]:
            core, targets = tuple(group["core_coefficients_ascending"]), group["target_prefixes"]
            actual_group = actual_groups[core]
            assert len(targets) == group["count"] == actual_group["target_count"]
            before = independent_mass(blocks, targets, half, initial=True)
            after = independent_mass(blocks, targets, half)
            floor = F(len(targets), 10 * 9**half)
            assert rational(group["census_initial_probability"]) == rational(actual_group["initial_probability"]) == before
            assert rational(actual_group["final_probability"]) == after
            assert rational(actual_group["final_to_initial_ratio"]) == after / before
            assert rational(actual_group["uniform_exploration_floor"]) == floor
            assert 0 < floor < before <= 1 and floor < after <= 1
            direction = "increase" if core == LEHMER else "decrease"
            assert actual_group["comparison"] == direction
            assert (after > before) if core == LEHMER else (after < before)
            initial_total += before
            final_total += after
            group_rows.append({"core": "Lehmer" if core == LEHMER else "second", "initial": float(before),
                               "final": float(after), "ratio": float(after / before), "floor": float(floor)})
        assert rational(actual["initial_total_target_probability"]) == initial_total
        assert rational(actual["final_total_target_probability"]) == final_total
        assert rational(actual["total_final_to_initial_ratio"]) == final_total / initial_total
        observed.append({"degree": degree, "seed": seed, "core_groups": group_rows})
    return {"fixed_runs": 10, "exact_core_probabilities": 20,
            "retained_integer_weights": sum(len(block["weights"]) for row in states["final_laws"] for block in row["blocks"]),
            "target_prefixes": sum(part["strict_target_count"] for part in partitions.values()),
            "independent_fraction_products_match_all_exact_results": True, "rows": observed}


def journal_final_state(path, original, retained):
    blocks = retained["blocks"]
    probabilities = [{state: prod(F(WEIGHTS[value + 4], 46) for value in state)
                      for state in itertools.product(ALPHABET, repeat=block["width"])} for block in blocks]
    batch = []
    proposal = evaluation = None
    completed = updates = last_update = last_elapsed = 0
    with Path(path).open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                assert not stream.read(), "only a final truncated record may be ignored"
                break
            kind = event["kind"]
            if kind == "config":
                assert event == original["configuration"]
            elif kind == "proposal":
                proposal, evaluation = event, None
            elif kind == "evaluation":
                evaluation = event
            elif kind == "commit":
                assert event["elapsed"] <= 10
                completed += 1
                assert proposal["proposal"] == evaluation["proposal"] == event["proposal"] == completed
                if not evaluation["neutral"] and evaluation["ranking_resolved"]:
                    batch.append((tuple(evaluation["core_coefficients_ascending"]), evaluation["log_score"],
                                  tuple(proposal["free_coefficients"])))
                if completed % 256:
                    assert evaluation["update"] is None
                    continue
                representatives = {}
                for core, score, free in batch:
                    candidate = score, free
                    if core not in representatives or candidate < representatives[core]:
                        representatives[core] = candidate
                elites = [free for score, free in sorted(representatives.values())[:(len(representatives) + 9)//10]]
                assert evaluation["update"] == {"eligible_proposals": len(batch), "unique_eligible_cores": len(representatives),
                                                "elite_count": len(elites), "elite_free_coefficients": [list(free) for free in elites]}
                if elites:
                    for block, distribution in zip(blocks, probabilities):
                        start, width = block["start"], block["width"]
                        frequencies = Counter(free[start:start + width] for free in elites)
                        prior = F(1, 81) if width == 2 else F(1)
                        denominator = len(elites) + len(distribution) * prior
                        for state in distribution:
                            distribution[state] = F(4, 5) * distribution[state] + F(1, 5) * (frequencies[state] + prior) / denominator
                updates += 1
                last_update, last_elapsed = completed, event["elapsed"]
                batch.clear()
    assert completed == retained["completed_proposals"]
    assert updates == retained["updates_replayed"]
    assert (last_update, last_elapsed) == (retained["last_committed_update_proposal"], retained["last_committed_update_elapsed"])
    assert probabilities == distributions(blocks)
    return updates


def provenance_checks(states, comparison, result, directory):
    sys.path.insert(0, str(HERE))
    from flint import fmpz_poly
    from sampler import normalized_core, reciprocal_polynomial

    assert read(directory / "independent_core_mass_states_replay.json") == states
    assert read(directory / "independent_core_mass_recomputed.json") == result
    original_census = read(directory / "baseline_mass.json")
    prior_independent_census = read(directory / "independent_baseline_mass.json")
    ref = {row["degree"]: row for row in original_census["results"]}
    independent_ref = {row["degree"]: row for row in prior_independent_census["results"]}
    factored = 0
    for partition in states["target_partitions"]:
        degree = partition["degree"]
        assert ref[degree]["height"] == independent_ref[degree]["height"] == 4
        assert ref[degree]["strict_target_count"] == independent_ref[degree]["strict_target_count"] == partition["strict_target_count"]
        retained_prefixes = {tuple(prefix) for group in partition["core_groups"] for prefix in group["target_prefixes"]}
        assert retained_prefixes == {tuple(prefix) for prefix in ref[degree]["target_prefixes"]}
        assert retained_prefixes == {tuple(prefix) for prefix in independent_ref[degree]["target_prefixes"]}
        source_groups = {tuple(group["core_coefficients_ascending"]): group for group in ref[degree]["certified_core_groups"]}
        independent_groups = {tuple(group["core_coefficients_ascending"]): group for group in independent_ref[degree]["certified_core_groups"]}
        for group in partition["core_groups"]:
            core = tuple(group["core_coefficients_ascending"])
            for original in (source_groups[core], independent_groups[core]):
                assert group["count"] == original["count"]
                assert rational(group["census_initial_probability"]) == rational(original["static_mixture_probability"])
                assert group["measure_interval"] == original["measure_interval"]
                assert group["measure_ball"] == original["measure_ball"]
            for prefix in group["target_prefixes"]:
                polynomial = fmpz_poly(reciprocal_polynomial(prefix))
                content, factors = polynomial.factor()
                assert int(content) == 1
                assert prod((factor**exponent for factor, exponent in factors), start=fmpz_poly([1])) == polynomial
                assert tuple(normalized_core(factors)) == core
                factored += 1
    originals = {(row["degree"], row["seed"]): row for group in comparison["groups"]
                 for row in group["all_seed_outcomes"] if row["arm"] == "A"}
    updates = 0
    for state in states["final_laws"]:
        original = originals[state["degree"], state["seed"]]
        count = journal_final_state(directory / original["events_file"], original, state)
        updates += count
        print({"state_checked": [state["degree"], state["seed"]], "committed_updates": count}, flush=True)
    return {"prior_independent_census_targets_match": True, "exact_target_factorizations": factored,
            "actual_extraction_and_evaluation_match_all_retained_fields": True, "independent_fraction_updates": updates,
            "final_block_probabilities_match_committed_histories": True}


def main():
    if not __debug__:
        raise RuntimeError("run without -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--states", type=Path, default=HERE / "inputs" / "degree_core_mass_states.json")
    parser.add_argument("--comparison", type=Path, default=HERE / "inputs" / "degree_comparison.json")
    parser.add_argument("--result", type=Path, default=HERE / "inputs" / "degree_core_mass.json")
    parser.add_argument("--with-provenance", action="store_true")
    parser.add_argument("--originals", type=Path, default=OUTPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT / "independent_core_mass_review.json")
    args = parser.parse_args()
    states, comparison, result = read(args.states), read(args.comparison), read(args.result)
    checked = fixed_checks(states, comparison, result)
    if args.with_provenance:
        checked["provenance"] = provenance_checks(states, comparison, result, args.originals)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(checked, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(checked))


if __name__ == "__main__":
    main()
