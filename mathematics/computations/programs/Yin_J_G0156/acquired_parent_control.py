"""Offline mutation control using each finished A run's actually seen parents.

Extraction reads all committed target evaluations, deduplicating exact free
prefixes rather than normalized cores. It reconstructs the polynomial LRU and
retains target occurrence provenance, including cache/repetition flags.
The unchanged unit-mutation kernel is evaluated only after extraction, with
known targets used for evaluation. This is not live acquisition or a new run.
"""

from __future__ import annotations

import argparse
from collections import Counter, OrderedDict
from fractions import Fraction as F
import json
from pathlib import Path
from time import perf_counter

import core_mass_diagnostic as core
import mutation_kernel_control as kernel

HERE = Path(__file__).resolve().parent
OUTPUT = core.OUTPUT
DEFAULT_INPUT = HERE/"inputs"/"acquired_parent_states.json"
PROTOCOL = "S10-observed-parent-offline-mutation-control"
CERTIFICATE_FIELDS = ("core_coefficients_ascending","measure_interval","measure_ball","neutral","thresholds",
                      "precision_bits","root_count_with_multiplicity","factorization_product_verified")


def source_rows(comparison):
    assert comparison["protocol"] == core.SOURCE_PROTOCOL and comparison["complete_declared_degree_validation"]
    rows = [row for group in comparison["groups"] for row in group["all_seed_outcomes"] if row["arm"] == "A"]
    assert len(rows) == 10 and {(row["degree"],row["seed"]) for row in rows} == {
        (degree,seed) for degree in core.DEGREES for seed in core.SEEDS}
    assert all(row["valid_run"] and row["eligible_degree_validation_run"] for row in rows)
    return sorted(rows,key=lambda row:(row["degree"],row["seed"]))


def check_certificate(certificate, prefix, degree):
    assert certificate["coefficients_ascending"] == [1,*prefix,*reversed(prefix[:-1]),1]
    assert len(prefix) == degree//2 and certificate["root_count_with_multiplicity"] == degree
    assert certificate["precision_bits"] == 128 and certificate["factorization_product_verified"]
    assert not certificate["neutral"] and certificate["ranking_resolved"]
    assert certificate["thresholds"]["6/5"] == "below"
    lower,upper = (F(endpoint[0])*F(2)**endpoint[1] for endpoint in certificate["measure_interval"])
    assert 1 < lower <= upper < F(6,5)


def observe_parent(parents, prefix, certificate, occurrence):
    key = tuple(prefix)
    if key not in parents:
        assert not occurrence[2] and not occurrence[3]
        parents[key] = {"free_coefficients":list(prefix),"first_certificate":certificate,"occurrences":[]}
    else:
        assert occurrence[3]
    parents[key]["occurrences"].append(occurrence)


def extract_run(path, source, check_budget):
    config = proposal = evaluation = None
    seen,cache,parents = set(),OrderedDict(),{}
    counts = Counter()
    last_commit = 0
    with Path(path).open(encoding="utf-8") as stream:
        for line_number,line in enumerate(stream,1):
            if line_number % 1024 == 0:
                check_budget()
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                break
            if event["kind"] == "config":
                assert config is None and event == source["configuration"]
                config = event
                assert config["variant"] == "A" and config["protocol"] == core.SOURCE_PROTOCOL
            elif event["kind"] == "proposal":
                proposal,evaluation = event,None
                counts["proposals_in_cap"] += event["elapsed"] <= config["seconds"]
            elif event["kind"] == "evaluation":
                evaluation = event
            elif event["kind"] == "commit" and event["elapsed"] <= config["seconds"]:
                number = event["proposal"]
                assert proposal["proposal"] == evaluation["proposal"] == number == counts["committed"]+1
                counts["committed"] += 1
                last_commit = event["elapsed"]
                prefix = proposal["free_coefficients"]
                assert len(prefix) == source["degree"]//2 and all(type(value) is int and value in core.ALPHABET for value in prefix)
                key = tuple(prefix)
                assert evaluation["repeated_proposal"] == (key in seen)
                assert evaluation["cached"] == (key in cache)
                assert not evaluation.get("unresolved_error"), "cannot infer a failed evaluation's cache insertion"
                seen.add(key)
                cache[key] = True
                cache.move_to_end(key)
                if len(cache) > config["cache_size"]:
                    cache.popitem(last=False)
                counts["all_cache_hits"] += evaluation["cached"]
                counts["all_repeated_proposals"] += evaluation["repeated_proposal"]
                if evaluation["thresholds"]["6/5"] != "below":
                    continue
                counts["all_target_evaluations"] += 1
                certificate = evaluation["certificate"]
                check_certificate(certificate,prefix,source["degree"])
                assert certificate["core_coefficients_ascending"] == evaluation["core_coefficients_ascending"]
                if tuple(certificate["core_coefficients_ascending"]) != core.LEHMER:
                    counts["other_core_target_evaluations"] += 1
                    continue
                counts["Lehmer_target_evaluations"] += 1
                occurrence = [number,event["elapsed"],evaluation["cached"],evaluation["repeated_proposal"]]
                observe_parent(parents,prefix,{name:certificate[name] for name in CERTIFICATE_FIELDS},occurrence)
    check_budget()
    assert config is not None and counts["committed"] == source["counts"]["completed_proposals"]
    assert counts["proposals_in_cap"] == source["counts"]["proposals"]
    assert counts["all_cache_hits"] == source["counts"]["cache_hits"]
    assert counts["all_repeated_proposals"] == source["counts"]["repeated_proposals"]
    assert counts["all_target_evaluations"] == source["raw_whole_hits"]["6/5"]
    assert last_commit == source["last_committed_elapsed"]
    records = sorted(parents.values(),key=lambda item:item["occurrences"][0][0])
    return {"degree":source["degree"],"seed":source["seed"],"source_summary":source["source_summary"],
            "source_journal":Path(path).name,"committed_proposals":counts["committed"],
            "all_target_evaluations":counts["all_target_evaluations"],
            "Lehmer_target_evaluations":counts["Lehmer_target_evaluations"],
            "other_core_target_evaluations":counts["other_core_target_evaluations"],
            "distinct_parent_count":len(records),"parents":records,
            "cache_check":"Exact LRU and seen-prefix flags reconstructed across every committed evaluation."}


def validate_acquired(data, comparison):
    assert data["protocol"] == PROTOCOL and data["source_label"] == comparison["label"]
    assert data["occurrence_columns"] == ["proposal","committed_elapsed","cached","repeated_proposal"]
    sources = {(row["degree"],row["seed"]):row for row in source_rows(comparison)}
    assert len(data["runs"]) == 10 and {(row["degree"],row["seed"]) for row in data["runs"]} == set(sources)
    for row in data["runs"]:
        source = sources[(row["degree"],row["seed"])]
        assert row["source_summary"] == source["source_summary"] and row["source_journal"] == source["events_file"]
        assert row["committed_proposals"] == source["counts"]["completed_proposals"]
        assert row["all_target_evaluations"] == source["raw_whole_hits"]["6/5"]
        assert row["Lehmer_target_evaluations"]+row["other_core_target_evaluations"] == row["all_target_evaluations"]
        parents = row["parents"]
        assert len(parents) == row["distinct_parent_count"] == len({tuple(parent["free_coefficients"]) for parent in parents})
        observations = []
        for parent in parents:
            prefix,certificate = parent["free_coefficients"],parent["first_certificate"]
            assert len(prefix) == row["degree"]//2 and all(type(value) is int and value in core.ALPHABET for value in prefix)
            assert tuple(certificate["core_coefficients_ascending"]) == core.LEHMER
            assert certificate["root_count_with_multiplicity"] == row["degree"] and certificate["factorization_product_verified"]
            assert certificate["precision_bits"] == source["configuration"]["precision_bits"] == 128
            assert not certificate["neutral"] and certificate["thresholds"]["6/5"] == "below"
            lower,upper = (F(endpoint[0])*F(2)**endpoint[1] for endpoint in certificate["measure_interval"])
            assert 1 < lower <= upper < F(6,5)
            occurrence = parent["occurrences"]
            assert occurrence and not occurrence[0][2] and not occurrence[0][3]
            assert all(len(item) == 4 and type(item[0]) is int and 1 <= item[0] <= row["committed_proposals"]
                       and 0 <= item[1] <= source["configuration"]["seconds"] and type(item[2]) is bool and type(item[3]) is bool for item in occurrence)
            assert all(item[3] for item in occurrence[1:])
            assert all(left[0] < right[0] and left[1] <= right[1] for left,right in zip(occurrence,occurrence[1:]))
            observations.extend(occurrence)
        assert len(observations) == row["Lehmer_target_evaluations"] == len({item[0] for item in observations})
        if observations and row["other_core_target_evaluations"] == 0:
            assert min(item[1] for item in observations) == source["first_target_hit_seconds"]


def extract(comparison_path, journals, seconds):
    started = perf_counter()
    def check_budget():
        if perf_counter()-started > seconds:
            raise TimeoutError("bounded parent extraction exceeded its ceiling; no result published")
    comparison = core.read_json(comparison_path)
    runs = [extract_run(Path(journals)/source["events_file"],source,check_budget) for source in source_rows(comparison)]
    data = {"protocol":PROTOCOL,"source_label":comparison["label"],
            "occurrence_columns":["proposal","committed_elapsed","cached","repeated_proposal"],"runs":runs,
            "scope":"All distinct Lehmer free prefixes actually observed in committed whole-target evaluations, grouped separately by original run. Occurrence multiplicity does not weight the later uniform-parent kernel. Extraction reads no complete target/parent reference library."}
    validate_acquired(data,comparison)
    check_budget()
    return data


def evaluate_parent_kernel(parents, targets, n):
    if not parents:
        return {"kernel_defined":False,"reason":"empty observed parent set; no reference parent or fallback kernel supplied",
                "mixture_second_core_probability":None,"second_core_prefixes_reachable_by_mutation":0,
                "compatible_pairs_by_k":None,"mutation_branch_outcomes_by_k":None,"boundary_returns_by_k":None,
                "compatible_pair_witnesses":[]}
    counts,_,witnesses = kernel.cross_pair_counts(parents,targets,n)
    hits,returned,totals = kernel.enumerate_mutations(parents,targets,n)
    assert all(hits[k] == counts[k] for k in kernel.K_VALUES)
    probability = F(len(targets),10*9**n)+F(9,10)*kernel.mutation_mass(counts,len(parents),n)
    return {"kernel_defined":True,"mixture_second_core_probability":core.fraction_record(probability),
            "second_core_prefixes_reachable_by_mutation":len({tuple(item["second_core_prefix"]) for item in witnesses}),
            "compatible_pairs_by_k":dict(counts),"mutation_branch_outcomes_by_k":dict(totals),
            "boundary_returns_by_k":dict(returned),"compatible_pair_witnesses":witnesses}


def evaluate(data, states, comparison, masses, full_control):
    validate_acquired(data,comparison)
    core.validate_input(states,comparison)
    assert masses["protocol"] == core.PROTOCOL and masses["source_label"] == comparison["label"]
    assert full_control["protocol"] == kernel.PROTOCOL
    partitions = {part["degree"]:part for part in states["target_partitions"]}
    full_rows = {row["degree"]:row for row in full_control["results"]}
    assert len(full_control["results"]) == 2 and set(full_rows) == set(core.DEGREES)
    mass_rows = {(row["degree"],row["seed"]):row for row in masses["runs"]}
    assert len(masses["runs"]) == 10 and set(mass_rows) == {(row["degree"],row["seed"]) for row in data["runs"]}
    libraries = {}
    for degree,partition in partitions.items():
        groups = {tuple(group["core_coefficients_ascending"]):group for group in partition["core_groups"]}
        full = [tuple(prefix) for prefix in groups[core.LEHMER]["target_prefixes"]]
        targets = [tuple(prefix) for prefix in groups[core.SECOND]["target_prefixes"]]
        counts,_,_ = kernel.cross_pair_counts(full,targets,degree//2)
        full_probability = F(len(targets),10*9**(degree//2))+F(9,10)*kernel.mutation_mass(counts,len(full),degree//2)
        assert full_probability == core.fraction_value(full_rows[degree]["mixture_second_core_probability"])
        assert {str(k):value for k,value in counts.items()} == full_rows[degree]["compatible_pairs_by_k"]
        libraries[degree] = (set(full),targets,full_probability,core.fraction_value(groups[core.SECOND]["census_initial_probability"]))
    rows = []
    for acquired in data["runs"]:
        degree,seed = acquired["degree"],acquired["seed"]
        full,targets,full_probability,fixed = libraries[degree]
        parents = [tuple(parent["free_coefficients"]) for parent in acquired["parents"]]
        assert set(parents) <= full
        result = evaluate_parent_kernel(parents,targets,degree//2)
        second = next(group for group in mass_rows[(degree,seed)]["core_groups"] if tuple(group["core_coefficients_ascending"]) == core.SECOND)
        assert second["target_count"] == len(targets) and core.fraction_value(second["initial_probability"]) == fixed
        final = core.fraction_value(second["final_probability"])
        occurrences = [item for parent in acquired["parents"] for item in parent["occurrences"]]
        row = {"degree":degree,"seed":seed,"distinct_observed_parents":len(parents),"complete_parent_library_size":len(full),
               "raw_Lehmer_target_hits":len(occurrences),"cached_target_hits":sum(item[2] for item in occurrences),
               "repeated_target_hits":sum(item[3] for item in occurrences),
               "fresh_repeated_target_hits":sum(item[3] and not item[2] for item in occurrences),
               "first_parent_elapsed":min((parent["occurrences"][0][1] for parent in acquired["parents"]),default=None),
               "last_new_parent_elapsed":max((parent["occurrences"][0][1] for parent in acquired["parents"]),default=None),
               **result,"complete_library_probability":core.fraction_record(full_probability),
               "fixed_bias_probability":core.fraction_record(fixed),"A_final_probability":core.fraction_record(final)}
        if result["kernel_defined"]:
            probability = core.fraction_value(result["mixture_second_core_probability"])
            row["ratios"] = {"to_complete_library":core.fraction_record(probability/full_probability),
                             "to_fixed_bias":core.fraction_record(probability/fixed),"to_A_final":core.fraction_record(probability/final)}
        else:
            row["ratios"] = None
        rows.append(row)
    return {"protocol":PROTOCOL,"source_label":data["source_label"],
            "kernel":{**full_control["kernel"],"parent_choice":"uniform over this run's distinct observed Lehmer prefixes"},"runs":rows,
            "parent_choice_override":"uniform over each run's distinct actually observed Lehmer prefixes; duplicates carry no additional weight",
            "scope":"Post hoc finite mechanism calculation on each completed history. Parents were selected after the run by known target/core status. This is not live acquisition, a learned proposal comparison, new random sampling, a cost advantage or a new Mahler value. The full library and second-core census supply evaluation baselines only."}


def self_test():
    parents = {}
    marker = {"scope":"synthetic bookkeeping control only"}
    observe_parent(parents,[0,1,2],marker,[1,0.1,False,False])
    observe_parent(parents,[0,1,2],marker,[2,0.2,True,True])
    observe_parent(parents,[1,1,2],marker,[3,0.3,False,False])
    observe_parent(parents,[0,1,2],marker,[4,0.4,False,True])
    assert len(parents) == 2 and [len(parent["occurrences"]) for parent in parents.values()] == [3,1]
    assert sum(item[2] for parent in parents.values() for item in parent["occurrences"]) == 1
    assert sum(item[3] and not item[2] for parent in parents.values() for item in parent["occurrences"]) == 1
    empty = evaluate_parent_kernel([],[(0,0,0)],3)
    assert not empty["kernel_defined"] and empty["mixture_second_core_probability"] is None
    actual = evaluate_parent_kernel([(0,0,0)],[(1,0,0)],3)
    assert actual["compatible_pairs_by_k"] == {1:1,2:0,3:0}
    assert core.fraction_value(actual["mixture_second_core_probability"]) == F(1,10*9**3)+F(9,10)*F(1,18)
    return {"passed":True,"checks":["exact-prefix deduplication keeps distinct parents sharing a core",
            "cached and fresh repeated hits do not reweight parents","all selected occurrence provenance retained",
            "empty parent kernel explicitly undefined","same fixed unit-mutation formula and endpoint enumeration"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command",required=True)
    commands.add_parser("self-test")
    extraction = commands.add_parser("extract")
    extraction.add_argument("--comparison",type=Path,default=core.DEFAULT_COMPARISON)
    extraction.add_argument("--journals",type=Path,default=OUTPUT)
    extraction.add_argument("--seconds",type=float,default=60)
    extraction.add_argument("--output",type=Path,default=DEFAULT_INPUT)
    run = commands.add_parser("run")
    run.add_argument("--input",type=Path,default=DEFAULT_INPUT)
    run.add_argument("--states",type=Path,default=core.DEFAULT_STATES)
    run.add_argument("--comparison",type=Path,default=core.DEFAULT_COMPARISON)
    run.add_argument("--masses",type=Path,default=HERE/"inputs"/"degree_core_mass.json")
    run.add_argument("--full-control",type=Path,default=HERE/"inputs"/"mutation_kernel_control.json")
    run.add_argument("--output",type=Path,default=OUTPUT/"acquired_parent_control.json")
    args = parser.parse_args()
    if args.command == "self-test":
        print(json.dumps(self_test()))
    elif args.command == "extract":
        if not 0 < args.seconds <= 60:
            raise ValueError("extraction requires a positive ceiling of at most 60 seconds")
        if args.output.exists():
            raise FileExistsError("preserve the existing parent input; use a fresh destination")
        data = extract(args.comparison,args.journals,args.seconds)
        core.write_new(args.output,data)
        print(json.dumps({"runs":len(data["runs"]),"raw_Lehmer_hits":sum(row["Lehmer_target_evaluations"] for row in data["runs"]),
                          "distinct_parent_counts":[row["distinct_parent_count"] for row in data["runs"]],"kernel_evaluated":False}))
    else:
        if args.output.exists():
            raise FileExistsError("preserve the existing exact result; use a fresh destination")
        result = evaluate(core.read_json(args.input),core.read_json(args.states),core.read_json(args.comparison),
                          core.read_json(args.masses),core.read_json(args.full_control))
        core.write_new(args.output,result)
        print(json.dumps({"runs":len(result["runs"]),"undefined_kernels":sum(not row["kernel_defined"] for row in result["runs"]),
                          "scope":result["scope"]}))


if __name__ == "__main__":
    main()
