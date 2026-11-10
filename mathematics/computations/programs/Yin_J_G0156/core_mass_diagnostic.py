"""Exact post-run A-law probabilities partitioned by normalized target core.

Extraction verifies committed journal updates before reading reference targets.
It retains final integer block states and the exact census partition, without
copying journals or supplying reference data to the learner. The separate run
command uses only standard-library integer/Fraction arithmetic on fixed inputs.
No stochastic experiment or new root certificate is performed by this program.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import itertools
import json
from math import gcd, prod
from pathlib import Path
from time import perf_counter

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
DEFAULT_STATES = HERE / "inputs" / "degree_core_mass_states.json"
DEFAULT_COMPARISON = HERE / "inputs" / "degree_comparison.json"
PROTOCOL = "S10-degree-validation-core-mass-postrun"
SOURCE_PROTOCOL = "S10-degree-validation"
DEGREES = (18, 20)
SEEDS = tuple(range(10, 15))
ALPHABET = tuple(range(-4, 5))
FIXED_WEIGHTS = (1, 2, 4, 8, 16, 8, 4, 2, 1)
LEHMER = (1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1)
SECOND = (1, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 1)
CORE_COUNTS = {18: {LEHMER: 174, SECOND: 2}, 20: {LEHMER: 344, SECOND: 10}}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_new(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def fraction_record(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator), "decimal": float(value)}


def fraction_value(record):
    return F(int(record["numerator"]), int(record["denominator"]))


def initial_blocks(half):
    return [{"start": start, "width": min(2, half-start),
             "weights": [prod(FIXED_WEIGHTS[value+4] for value in state)
                         for state in itertools.product(ALPHABET, repeat=min(2, half-start))]}
            for start in range(0, half, 2)]


def validate_blocks(blocks, half):
    expected = [(start, min(2, half-start)) for start in range(0, half, 2)]
    assert [(block["start"],block["width"]) for block in blocks] == expected
    for block in blocks:
        weights = block["weights"]
        assert len(weights) == 9**block["width"]
        assert all(type(weight) is int and weight > 0 for weight in weights)
        assert gcd(*weights) == 1


def state_index(prefix, block):
    value = 0
    for coefficient in prefix[block["start"]:block["start"]+block["width"]]:
        value = 9*value + coefficient + 4
    return value


def exact_mass(blocks, targets, half):
    """Two aggregate Fractions; no per-prefix rational normalization."""
    denominator = prod(sum(block["weights"]) for block in blocks)
    numerator = sum(prod(block["weights"][state_index(prefix,block)] for block in blocks) for prefix in targets)
    return F(len(targets), 10*9**half) + F(9*numerator, 10*denominator)


def validate_input(data, comparison):
    assert data["protocol"] == PROTOCOL and comparison["protocol"] == SOURCE_PROTOCOL
    assert comparison["complete_declared_degree_validation"]
    assert data["source_label"] == comparison["label"]
    assert data["law_source"] == "prior_strength_live.py:UnitPairPriorLaw"
    assert data["state_order"] == "lexicographic product of (-4,-3,-2,-1,0,1,2,3,4), first coordinate major"
    partitions = data["target_partitions"]
    assert len(partitions) == 2 and {part["degree"] for part in partitions} == set(DEGREES)
    for part in partitions:
        degree, seen = part["degree"], set()
        assert len(part["core_groups"]) == 2
        assert {tuple(group["core_coefficients_ascending"]) for group in part["core_groups"]} == set(CORE_COUNTS[degree])
        for group in part["core_groups"]:
            core = tuple(group["core_coefficients_ascending"])
            targets = group["target_prefixes"]
            assert len(targets) == group["count"] == CORE_COUNTS[degree][core]
            assert tuple(group["core_coefficients_ascending"]) in (LEHMER, SECOND)
            for prefix in targets:
                assert len(prefix) == degree//2 and all(type(value) is int and value in ALPHABET for value in prefix)
                assert tuple(prefix) not in seen
                seen.add(tuple(prefix))
        assert len(seen) == part["strict_target_count"] == sum(CORE_COUNTS[degree].values())
    source_rows = {(row["degree"],row["seed"]):row for group in comparison["groups"]
                   for row in group["all_seed_outcomes"] if row["arm"] == "A"}
    expected = {(degree,seed) for degree in DEGREES for seed in SEEDS}
    assert set(source_rows) == expected
    assert len(data["final_laws"]) == 10
    assert {(row["degree"],row["seed"]) for row in data["final_laws"]} == expected
    for row in data["final_laws"]:
        source = source_rows[(row["degree"],row["seed"])]
        config = source["configuration"]
        assert source["valid_run"] and source["eligible_degree_validation_run"]
        assert config["protocol"] == SOURCE_PROTOCOL and config["variant"] == "A"
        assert config["degree"] == row["degree"] and config["seed"] == row["seed"]
        assert config["law_class"] == "UnitPairPriorLaw" and config["implementation_arm"] == "adaptive"
        assert config["pair_prior_total"] == 1 and config["batch_size"] == 256
        assert config["singleton_prior_total"] == (9 if row["degree"] == 18 else None)
        assert row["source_summary"] == source["source_summary"]
        assert row["completed_proposals"] == source["counts"]["completed_proposals"]
        assert row["updates_replayed"] == source["counts"]["adaptive_updates"] == row["completed_proposals"]//256
        assert row["last_committed_update_proposal"] == 256*row["updates_replayed"]
        assert 0 <= row["last_committed_update_elapsed"] <= source["last_committed_elapsed"] <= config["seconds"]
        validate_blocks(row["blocks"],row["degree"]//2)


def replay_final_state(path, source, check_budget):
    # Only extraction imports the existing law and FLINT-backed sampler.
    from prior_strength_live import UnitPairPriorLaw

    law = config = proposal = evaluation = None
    batch = []
    committed = proposals_in_cap = draws = updates = 0
    last_update_proposal, last_update_elapsed, last_committed_elapsed = 0, 0, 0
    with Path(path).open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream,1):
            if line_number % 1024 == 0:
                check_budget()
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                break
            kind = event["kind"]
            if kind == "config":
                assert config is None
                config = event
                assert config == source["configuration"]
                assert config["variant"] == "A" and config["protocol"] == SOURCE_PROTOCOL
                law = UnitPairPriorLaw(config["degree"]//2,"adaptive",config["seed"])
                assert [{key:block[key] for key in ("start","width","weights")} for block in law.blocks] == initial_blocks(config["degree"]//2)
            elif kind == "proposal":
                proposal, evaluation = event, None
                draws += 1
                assert event["proposal"] == draws and law.draw() == event["free_coefficients"]
                proposals_in_cap += event["elapsed"] <= config["seconds"]
            elif kind == "evaluation":
                evaluation = event
            elif kind == "commit" and event["elapsed"] <= config["seconds"]:
                number = event["proposal"]
                assert proposal["proposal"] == evaluation["proposal"] == number == committed+1
                committed += 1
                last_committed_elapsed = event["elapsed"]
                if not evaluation.get("unresolved_error") and evaluation["ranking_resolved"] and not evaluation["neutral"]:
                    batch.append((tuple(evaluation["core_coefficients_ascending"]),evaluation["log_score"],proposal["free_coefficients"]))
                if number % 256 == 0:
                    assert law.update(batch) == evaluation["update"]
                    updates += 1
                    last_update_proposal, last_update_elapsed = number, event["elapsed"]
                    batch.clear()
                else:
                    assert evaluation["update"] is None
    check_budget()
    assert config is not None and committed == source["counts"]["completed_proposals"]
    assert proposals_in_cap == source["counts"]["proposals"]
    assert last_committed_elapsed == source["last_committed_elapsed"]
    assert updates == source["counts"]["adaptive_updates"]
    return {"degree":config["degree"],"seed":config["seed"],"source_summary":source["source_summary"],
            "completed_proposals":committed,"updates_replayed":updates,
            "last_committed_update_proposal":last_update_proposal,"last_committed_update_elapsed":last_update_elapsed,
            "blocks":[{key:block[key] for key in ("start","width","weights")} for block in law.blocks]}


def partition_reference(reference, check_budget):
    from flint import fmpz_poly
    from sampler import normalized_core, reciprocal_polynomial

    rows = [row for row in reference["results"] if row["degree"] in DEGREES]
    assert len(rows) == 2 and {row["degree"] for row in rows} == set(DEGREES)
    result = []
    for row in sorted(rows,key=lambda row:row["degree"]):
        degree = row["degree"]
        assert row["height"] == 4 and row["strict_target_count"] == sum(CORE_COUNTS[degree].values())
        targets = row["target_prefixes"]
        assert len(targets) == len({tuple(prefix) for prefix in targets}) == row["strict_target_count"]
        core_reference = {tuple(group["core_coefficients_ascending"]):group for group in row["certified_core_groups"]}
        assert len(row["certified_core_groups"]) == 2 and set(core_reference) == set(CORE_COUNTS[degree])
        groups = {core:[] for core in core_reference}
        for prefix in targets:
            check_budget()
            assert len(prefix) == degree//2 and all(type(value) is int and value in ALPHABET for value in prefix)
            polynomial = fmpz_poly(reciprocal_polynomial(prefix))
            content, factors = polynomial.factor()
            reconstructed = fmpz_poly([content])
            for factor, exponent in factors:
                reconstructed *= factor**exponent
            assert reconstructed == polynomial and int(content) == 1
            core = tuple(normalized_core(factors))
            assert core in groups
            groups[core].append(prefix)
        assert {tuple(prefix) for group in groups.values() for prefix in group} == {tuple(prefix) for prefix in targets}
        retained = []
        for core in (LEHMER,SECOND):
            original = core_reference[core]
            assert len(groups[core]) == original["count"] == CORE_COUNTS[degree][core]
            retained.append({"core_coefficients_ascending":list(core),"count":len(groups[core]),
                             "target_prefixes":sorted(groups[core]),
                             "measure_interval":original["measure_interval"],"measure_ball":original["measure_ball"],
                             "census_initial_probability":original["static_mixture_probability"]})
        result.append({"degree":degree,"strict_target_count":row["strict_target_count"],"core_groups":retained})
    return result


def extract(comparison_path, journals, reference_path, seconds):
    started = perf_counter()
    def check_budget():
        if perf_counter()-started > seconds:
            raise TimeoutError("bounded extraction elapsed ceiling exceeded; no result published")
    comparison = read_json(comparison_path)
    assert comparison["protocol"] == SOURCE_PROTOCOL and comparison["complete_declared_degree_validation"]
    rows = sorted((row for group in comparison["groups"] for row in group["all_seed_outcomes"] if row["arm"] == "A"),
                  key=lambda row:(row["degree"],row["seed"]))
    assert len(rows) == 10 and {(row["degree"],row["seed"]) for row in rows} == {(degree,seed) for degree in DEGREES for seed in SEEDS}
    snapshots = [replay_final_state(Path(journals)/row["events_file"],row,check_budget) for row in rows]
    # The complete law replay finishes before this first reference-target read.
    partitions = partition_reference(read_json(reference_path),check_budget)
    data = {"protocol":PROTOCOL,"scope":"fixed final-law/target inputs for post-run probability evaluation; no new discoveries",
            "source_comparison":Path(comparison_path).name,"source_label":comparison["label"],
            "law_source":"prior_strength_live.py:UnitPairPriorLaw",
            "reference_source":"baseline_mass.py complete H=4 target census; partition uses sampler.normalized_core",
            "state_order":"lexicographic product of (-4,-3,-2,-1,0,1,2,3,4), first coordinate major",
            "extraction_check":"Every recorded proposal and committed elite update matched the existing A law; all final states precede reference reads. Every target was exactly factored and assigned by the frozen normalized core, with partition union and reference group counts checked.",
            "target_partitions":partitions,"final_laws":snapshots}
    validate_input(data,comparison)
    check_budget()
    return data


def evaluate(data, comparison):
    validate_input(data,comparison)
    partitions = {row["degree"]:row for row in data["target_partitions"]}
    rows = []
    for state in data["final_laws"]:
        degree, half = state["degree"],state["degree"]//2
        initial = initial_blocks(half)
        groups = []
        initial_total = final_total = F(0)
        for group in partitions[degree]["core_groups"]:
            targets = group["target_prefixes"]
            before, after = exact_mass(initial,targets,half),exact_mass(state["blocks"],targets,half)
            assert before == fraction_value(group["census_initial_probability"])
            floor = F(len(targets),10*9**half)
            assert floor <= before <= 1 and floor <= after <= 1
            initial_total += before
            final_total += after
            groups.append({"core_coefficients_ascending":group["core_coefficients_ascending"],"target_count":len(targets),
                           "initial_probability":fraction_record(before),"final_probability":fraction_record(after),
                           "final_to_initial_ratio":fraction_record(after/before),"uniform_exploration_floor":fraction_record(floor),
                           "comparison":"increase" if after>before else "decrease" if after<before else "equal"})
        all_targets = [prefix for group in partitions[degree]["core_groups"] for prefix in group["target_prefixes"]]
        assert initial_total == exact_mass(initial,all_targets,half)
        assert final_total == exact_mass(state["blocks"],all_targets,half)
        rows.append({"degree":degree,"seed":state["seed"],"updates_replayed":state["updates_replayed"],
                     "last_committed_update_proposal":state["last_committed_update_proposal"],"core_groups":groups,
                     "initial_total_target_probability":fraction_record(initial_total),
                     "final_total_target_probability":fraction_record(final_total),
                     "total_final_to_initial_ratio":fraction_record(final_total/initial_total)})
    return {"protocol":PROTOCOL,"source_label":data["source_label"],"runs":rows,
            "arithmetic":"exact integer products and sums, then aggregate Fraction normalization; decimal fields only display",
            "interpretation":"Initial and final conditional next-proposal mass on known whole-polynomial target core groups. References are post-run evaluation only. This is neither new discovery, distinct-value yield, an independent Bernoulli model along the path, nor an unseen-benchmark claim."}


def self_test():
    def independent_mass(blocks,targets,half):
        biased = sum((prod(F(block["weights"][state_index(prefix,block)],sum(block["weights"]))
                           for block in blocks) for prefix in targets),F(0))
        return F(len(targets),10*9**half)+F(9,10)*biased
    cases = 0
    for half in (1,2,3):
        blocks = initial_blocks(half)
        validate_blocks(blocks,half)
        targets = [list(prefix) for prefix in itertools.product((-4,0,4),repeat=half)]
        assert exact_mass(blocks,[],half) == 0
        assert exact_mass(blocks,targets,half) == independent_mass(blocks,targets,half)
        for block in blocks:
            block["weights"] = [1]*len(block["weights"])
        assert exact_mass(blocks,targets,half) == F(len(targets),9**half)
        assert exact_mass(blocks,[list(prefix) for prefix in itertools.product(ALPHABET,repeat=half)],half) == 1
        for block in blocks:
            block["weights"] = [2**(index+1)+1 for index in range(len(block["weights"]))]
        assert exact_mass(blocks,targets,half) == independent_mass(blocks,targets,half)
        cases += 1
    return {"passed":True,"half_degree_cases":cases,"checks":["independent Fraction-product mass agreement",
            "initial and arbitrary positive integer blocks","empty target set","uniform probability and full-box normalization"],
            "scope":"small exact formula controls; no actual final-law mass evaluated"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command",required=True)
    extract_parser = commands.add_parser("extract")
    extract_parser.add_argument("--comparison",type=Path,default=DEFAULT_COMPARISON)
    extract_parser.add_argument("--journals",type=Path,default=OUTPUT)
    extract_parser.add_argument("--reference",type=Path,default=OUTPUT/"baseline_mass.json")
    extract_parser.add_argument("--seconds",type=float,default=60)
    extract_parser.add_argument("--output",type=Path,default=DEFAULT_STATES)
    run_parser = commands.add_parser("run")
    run_parser.add_argument("--input",type=Path,default=DEFAULT_STATES)
    run_parser.add_argument("--comparison",type=Path,default=DEFAULT_COMPARISON)
    run_parser.add_argument("--output",type=Path,default=OUTPUT/"degree_core_mass.json")
    commands.add_parser("self-test")
    args = parser.parse_args()
    if args.command == "self-test":
        print(json.dumps(self_test()))
    elif args.command == "extract":
        if not 0 < args.seconds <= 60:
            raise ValueError("extraction ceiling must be positive and at most 60 seconds")
        if args.output.exists():
            raise FileExistsError("preserve the fixed state input; select a fresh output")
        data = extract(args.comparison,args.journals,args.reference,args.seconds)
        write_new(args.output,data)
        print(json.dumps({"runs":len(data["final_laws"]),"updates_replayed":sum(row["updates_replayed"] for row in data["final_laws"]),
                          "target_prefixes":sum(row["strict_target_count"] for row in data["target_partitions"]),
                          "final_probabilities_evaluated":False}))
    else:
        if args.output.exists():
            raise FileExistsError("preserve an existing exact result; select a fresh output")
        result = evaluate(read_json(args.input),read_json(args.comparison))
        write_new(args.output,result)
        print(json.dumps({"runs":len(result["runs"]),"core_probabilities":sum(len(row["core_groups"]) for row in result["runs"]),
                          "scope":result["interpretation"]}))


if __name__ == "__main__":
    main()
