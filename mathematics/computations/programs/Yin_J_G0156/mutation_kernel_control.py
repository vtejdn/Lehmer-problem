"""Exact reference-seeded unit-mutation control on the two known target classes.

The kernel is 1/10 uniform on the complete coefficient box and 9/10 mutation:
choose a uniform parent from the COMPLETE retained Lehmer prefix class, choose
k uniformly from {1,2,3}, choose k distinct coordinates uniformly, and make
independent uniform +/-1 changes. Any box exit returns the unchanged parent.
This is a fixed finite reference control, never a self-learned/live search.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import itertools
import json
from math import comb
from pathlib import Path

import core_mass_diagnostic as core
import target_geometry

HERE = Path(__file__).resolve().parent
OUTPUT = core.OUTPUT
PROTOCOL = "S10-reference-seeded-unit-mutation-control"
K_VALUES = (1, 2, 3)


def check_sets(parents, targets, n):
    assert n >= 3 and parents
    assert len(parents) == len(set(parents)) and len(targets) == len(set(targets))
    assert set(parents).isdisjoint(targets)
    assert all(len(prefix) == n and all(type(value) is int and -4 <= value <= 4 for value in prefix)
               for prefix in (*parents,*targets))


def cross_pair_counts(parents, targets, n):
    check_sets(parents,targets,n)
    counts, histogram, witnesses = Counter({k:0 for k in K_VALUES}),Counter(),[]
    for parent in parents:
        for target in targets:
            differences = [b-a for a,b in zip(parent,target)]
            changed = [index for index,difference in enumerate(differences) if difference]
            hamming, l1 = len(changed),sum(abs(value) for value in differences)
            geometry = target_geometry.distances(parent,target)
            assert geometry["hamming"] == hamming and geometry["l1"] == l1
            histogram[hamming] += 1
            if hamming in K_VALUES and l1 == hamming:
                counts[hamming] += 1
                witnesses.append({"k":hamming,"parent_prefix":list(parent),"second_core_prefix":list(target),
                                  "changed_coordinates_zero_based":changed,
                                  "signed_unit_changes":[differences[index] for index in changed]})
    assert sum(histogram.values()) == len(parents)*len(targets)
    return counts,histogram,witnesses


def enumerate_mutations(parents, targets, n):
    """Independent finite endpoint enumeration, including every boundary return."""
    check_sets(parents,targets,n)
    targets = set(targets)
    hits, returned, totals = Counter(),Counter(),Counter()
    for k in K_VALUES:
        for parent in parents:
            for coordinates in itertools.combinations(range(n),k):
                for signs in itertools.product((-1,1),repeat=k):
                    child = list(parent)
                    for index,sign in zip(coordinates,signs):
                        child[index] += sign
                    if any(value < -4 or value > 4 for value in child):
                        child = parent
                        returned[k] += 1
                    totals[k] += 1
                    hits[k] += tuple(child) in targets
        assert totals[k] == len(parents)*comb(n,k)*2**k
    return hits,returned,totals


def mutation_mass(counts, parent_count, n):
    return sum((F(counts[k],3*parent_count*comb(n,k)*2**k) for k in K_VALUES),F(0))


def compare(states, comparison, saved_masses):
    core.validate_input(states,comparison)
    assert saved_masses["protocol"] == core.PROTOCOL and saved_masses["source_label"] == states["source_label"]
    mass_rows = {(row["degree"],row["seed"]):row for row in saved_masses["runs"]}
    assert len(saved_masses["runs"]) == 10 and set(mass_rows) == {(degree,seed) for degree in core.DEGREES for seed in core.SEEDS}
    rows = []
    for part in states["target_partitions"]:
        degree, n = part["degree"],part["degree"]//2
        groups = {tuple(group["core_coefficients_ascending"]):group for group in part["core_groups"]}
        parents = [tuple(prefix) for prefix in groups[core.LEHMER]["target_prefixes"]]
        targets = [tuple(prefix) for prefix in groups[core.SECOND]["target_prefixes"]]
        counts,histogram,witnesses = cross_pair_counts(parents,targets,n)
        hits,returned,totals = enumerate_mutations(parents,targets,n)
        assert all(hits[k] == counts[k] for k in K_VALUES)
        mutation = mutation_mass(counts,len(parents),n)
        assert mutation == sum((F(hits[k],3*totals[k]) for k in K_VALUES),F(0))
        uniform = F(len(targets),10*9**n)
        total = uniform+F(9,10)*mutation
        fixed = core.fraction_value(groups[core.SECOND]["census_initial_probability"])
        assert 0 <= uniform <= total <= 1 and 0 < fixed < 1
        comparisons = []
        for seed in core.SEEDS:
            saved = mass_rows[(degree,seed)]
            saved_groups = {tuple(group["core_coefficients_ascending"]):group for group in saved["core_groups"]}
            assert len(saved["core_groups"]) == 2 and set(saved_groups) == {core.LEHMER,core.SECOND}
            saved_second = saved_groups[core.SECOND]
            assert saved_second["target_count"] == len(targets)
            assert core.fraction_value(saved_second["initial_probability"]) == fixed
            final = core.fraction_value(saved_second["final_probability"])
            assert final > 0
            comparisons.append({"seed":seed,"A_final_second_core_probability":saved_second["final_probability"],
                                "kernel_to_A_final_ratio":core.fraction_record(total/final),
                                "comparison":"greater" if total>final else "less" if total<final else "equal"})
        reachable = {tuple(witness["second_core_prefix"]) for witness in witnesses}
        rows.append({"degree":degree,"free_coordinates":n,"Lehmer_parent_count":len(parents),
                     "second_core_target_count":len(targets),"minimum_cross_class_hamming":min(histogram),
                     "cross_pair_hamming_histogram":dict(sorted(histogram.items())),
                     "compatible_pairs_by_k":dict(counts),"mutation_branch_outcomes_by_k":dict(totals),
                     "boundary_returns_by_k":dict(returned),
                     "mutation_only_second_core_probability":core.fraction_record(mutation),
                     "uniform_component_second_core_probability":core.fraction_record(uniform),
                     "mixture_second_core_probability":core.fraction_record(total),
                     "fixed_bias_second_core_probability":core.fraction_record(fixed),
                     "kernel_to_fixed_ratio":core.fraction_record(total/fixed),
                     "kernel_vs_fixed":"greater" if total>fixed else "less" if total<fixed else "equal",
                     "second_core_prefixes_reachable_by_mutation":len(reachable),
                     "compatible_pair_witnesses":witnesses,"A_final_comparisons":comparisons,
                     "verification":"Cross-pair counts equal independent exhaustive endpoint counts for every k; out-of-box branches return their unchanged parent and cannot hit the disjoint second-core target."})
    return {"protocol":PROTOCOL,"parent_reference":"complete retained Lehmer prefix class at the same degree",
            "kernel":{"uniform_whole_box_probability":"1/10","mutation_probability":"9/10",
                      "parent_choice":"uniform over all distinct retained Lehmer prefixes",
                      "k_choice":[1,2,3],"k_probability":"1/3 each",
                      "coordinate_choice":"uniform k-subset of the n free reciprocal coefficients",
                      "sign_choice":"independent uniform -1/+1 for each selected coordinate",
                      "box_exit":"return the unchanged parent; do not reject and resample"},
            "results":rows,
            "scope":"Exact reference-seeded finite mechanism control. The complete known parent class supplies privileged reference data. This is not a learned/live law, observed success rate, cost-normalized comparison, new candidate, or novel Mahler value. Unit changes at a chosen coordinate subset preserve the unmutated parent template; no nearest-reference restoration or new fitting is performed."}


def self_test():
    parents = [(4,0,0),(-4,0,0)]
    targets = [(3,0,0),(-3,0,0),(4,1,-1),(-4,1,-1),(3,1,1),(-3,1,1)]
    counts,histogram,witnesses = cross_pair_counts(parents,targets,3)
    hits,returned,totals = enumerate_mutations(parents,targets,3)
    assert dict(counts) == {1:2,2:2,3:2}
    assert all(hits[k] == counts[k] and returned[k] > 0 for k in K_VALUES)
    assert mutation_mass(counts,2,3) == F(1,8)
    assert sum(F(totals[k],3*2*comb(3,k)*2**k) for k in K_VALUES) == 1
    assert all(len(witness["changed_coordinates_zero_based"]) == witness["k"]
               and all(sign in (-1,1) for sign in witness["signed_unit_changes"]) for witness in witnesses)
    empty,_,_ = cross_pair_counts(parents,[],3)
    assert mutation_mass(empty,2,3) == 0
    # Hamming one is insufficient when the coordinate difference is two.
    invalid_unit,_,_ = cross_pair_counts([(0,0,0)],[(2,0,0)],3)
    assert sum(invalid_unit.values()) == 0
    return {"passed":True,"checks":["known hand-counted k=1/2/3 cases","independent endpoint enumeration",
            "boundary returns remain in parent class","kernel branch normalization","empty target set",
            "unit-step condition excludes larger coordinate differences"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command",required=True)
    commands.add_parser("self-test")
    run = commands.add_parser("run")
    run.add_argument("--states",type=Path,default=core.DEFAULT_STATES)
    run.add_argument("--comparison",type=Path,default=core.DEFAULT_COMPARISON)
    run.add_argument("--masses",type=Path,default=HERE/"inputs"/"degree_core_mass.json")
    run.add_argument("--output",type=Path,default=OUTPUT/"mutation_kernel_control.json")
    args = parser.parse_args()
    if args.command == "self-test":
        print(json.dumps(self_test()))
    else:
        if args.output.exists():
            raise FileExistsError("preserve an existing result; choose a fresh output")
        result = compare(core.read_json(args.states),core.read_json(args.comparison),core.read_json(args.masses))
        core.write_new(args.output,result)
        print(json.dumps({"degrees":[row["degree"] for row in result["results"]],
                          "enumerated_mutation_branches":sum(sum(row["mutation_branch_outcomes_by_k"].values()) for row in result["results"]),
                          "scope":result["scope"]}))


if __name__ == "__main__":
    main()
