"""Independent finite review of the two fixed mutation controls and core closure.

No stochastic proposals or root certification are performed. Native target/core
and final-law evidence reuses R1111 v5/v6. Optional history mode streams only the
ten completed A journals. FLINT is used solely for exact polynomial arithmetic.
"""

from __future__ import annotations

import argparse
from collections import Counter, OrderedDict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json
from math import comb, gcd, prod
from pathlib import Path
import sys
from time import monotonic

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
sys.path.insert(0, str(HERE))
LEHMER = (1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1)
SECOND = (1, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 1)
ALPHABET = tuple(range(-4, 5))


def read(name):
    return json.loads((HERE / "inputs" / name).read_text(encoding="utf-8"))


def rational(record):
    numerator, denominator = int(record["numerator"]), int(record["denominator"])
    assert denominator > 0 and gcd(numerator, denominator) == 1
    value = Fraction(numerator, denominator)
    assert record["decimal"] == float(value)
    return value


def serialized(value):
    return json.loads(json.dumps(value))


def witness_key(value):
    return (tuple(value["parent_prefix"]), tuple(value["second_core_prefix"]),
            value["k"], tuple(value["changed_coordinates_zero_based"]),
            tuple(value["signed_unit_changes"]))


def enumerate_kernel(parents, targets):
    """Enumerate endpoints with their exact weights, independently of cross pairs."""
    assert parents and len(parents) == len(set(parents))
    assert len(targets) == len(set(targets)) and set(parents).isdisjoint(targets)
    n = len(parents[0])
    target_set = set(targets)
    hits, exits, totals = Counter(), Counter(), Counter()
    witnesses, reachable = set(), set()
    probability, total_weight = Fraction(), Fraction()
    for k in range(1, 4):
        weight = Fraction(1, len(parents) * 3 * comb(n, k) * 2**k)
        for parent in parents:
            for chosen in combinations(range(n), k):
                for signs in product((-1, 1), repeat=k):
                    changes = dict(zip(chosen, signs))
                    endpoint = tuple(value + changes.get(i, 0) for i, value in enumerate(parent))
                    if not all(-4 <= value <= 4 for value in endpoint):
                        endpoint = parent
                        exits[k] += 1
                    totals[k] += 1
                    if endpoint in target_set:
                        hits[k] += 1
                        probability += weight
                        reachable.add(endpoint)
                        witnesses.add((parent, endpoint, k, chosen, signs))
        assert totals[k] == len(parents) * comb(n, k) * 2**k
        total_weight += totals[k] * weight
    assert total_weight == 1
    assert len(witnesses) == sum(hits.values())
    return {"counts": {str(k): hits[k] for k in range(1, 4)},
            "exits": {str(k): v for k, v in exits.items()},
            "totals": {str(k): totals[k] for k in range(1, 4)},
            "witnesses": witnesses, "reachable": len(reachable), "mutation": probability,
            "mixture": Fraction(len(targets), 10 * 9**n) + Fraction(9, 10) * probability}


def check_kernel_row(row, expected):
    assert row["compatible_pairs_by_k"] == expected["counts"]
    assert row["boundary_returns_by_k"] == expected["exits"]
    assert row["mutation_branch_outcomes_by_k"] == expected["totals"]
    assert len(row["compatible_pair_witnesses"]) == len(expected["witnesses"])
    assert {witness_key(w) for w in row["compatible_pair_witnesses"]} == expected["witnesses"]
    assert row["second_core_prefixes_reachable_by_mutation"] == expected["reachable"]
    assert rational(row["mixture_second_core_probability"]) == expected["mixture"]


def fixed_mass(targets, n):
    biased = sum((prod(Fraction(2**(4-abs(a)), 46) for a in prefix) for prefix in targets), Fraction())
    return Fraction(len(targets), 10 * 9**n) + Fraction(9, 10) * biased


def final_mass(law, targets, n):
    tables = [(block["start"], block["width"],
               dict(zip(product(ALPHABET, repeat=block["width"]),
                        (Fraction(w, sum(block["weights"])) for w in block["weights"]))))
              for block in law["blocks"]]
    biased = sum((prod(table[tuple(prefix[start:start+width])] for start, width, table in tables)
                  for prefix in targets), Fraction())
    return Fraction(len(targets), 10 * 9**n) + Fraction(9, 10) * biased


def geometry_check(states):
    import target_geometry
    result = target_geometry.evaluate(states)
    summary = []
    for row, part in zip(result["results"], states["target_partitions"]):
        groups = {tuple(g["core_coefficients_ascending"]): g for g in part["core_groups"]}
        parents, targets = groups[LEHMER]["target_prefixes"], groups[SECOND]["target_prefixes"]
        histogram = Counter()
        for entry, target in zip(row["second_core_outcomes"], targets):
            assert entry["second_core_prefix"] == target
            values = []
            for parent in parents:
                differences = [b-a for a, b in zip(parent, target)]
                record = {"hamming": sum(d != 0 for d in differences),
                          "l1": sum(abs(d) for d in differences),
                          "squared_l2": sum(d*d for d in differences),
                          "changed_pair_blocks": sum(any(differences[j:j+2])
                                                     for j in range(0, len(parent), 2))}
                histogram[record["hamming"]] += 1
                values.append((parent, record))
            for metric, actual in entry["minima"].items():
                minimum = min(v[metric] for _, v in values)
                nearest = [parent for parent, v in values if v[metric] == minimum]
                assert actual == {"minimum": minimum, "nearest_count": len(nearest),
                                  "one_nearest_Lehmer_prefix": nearest[0]}
        assert dict(histogram) == row["cross_pair_hamming_histogram"]
        summary.append({"degree": part["degree"], "minimum_hamming": min(histogram)})
    return summary


def kernel_checks(states, comparison, masses, full, acquired, observed):
    import acquired_parent_control as author_acquired
    import mutation_kernel_control as author_kernel
    assert author_kernel.self_test()["passed"] and author_acquired.self_test()["passed"]
    assert serialized(author_kernel.compare(states, comparison, masses)) == full
    assert serialized(author_acquired.evaluate(acquired, states, comparison, masses, full)) == observed
    assert not author_acquired.evaluate_parent_kernel([], [(0, 0, 0)], 3)["kernel_defined"]
    laws = {(row["degree"], row["seed"]): row for row in states["final_laws"]}
    final_rows = {(row["degree"], row["seed"]): row for row in masses["runs"]}
    full_rows = {row["degree"]: row for row in full["results"]}
    observed_rows = {(row["degree"], row["seed"]): row for row in observed["runs"]}
    libraries, whole_summary, observed_summary = {}, [], []
    for partition in states["target_partitions"]:
        degree, n = partition["degree"], partition["degree"] // 2
        groups = {tuple(g["core_coefficients_ascending"]): g for g in partition["core_groups"]}
        parents = list(map(tuple, groups[LEHMER]["target_prefixes"]))
        targets = list(map(tuple, groups[SECOND]["target_prefixes"]))
        expected = enumerate_kernel(parents, targets)
        row = full_rows[degree]
        check_kernel_row(row, expected)
        histogram = Counter(sum(a != b for a, b in zip(p, t)) for p in parents for t in targets)
        assert row["cross_pair_hamming_histogram"] == {str(k): v for k, v in histogram.items()}
        assert row["minimum_cross_class_hamming"] == min(histogram)
        assert row["free_coordinates"] == n and row["Lehmer_parent_count"] == len(parents)
        assert row["second_core_target_count"] == len(targets)
        assert rational(row["mutation_only_second_core_probability"]) == expected["mutation"]
        assert rational(row["uniform_component_second_core_probability"]) == Fraction(len(targets), 10 * 9**n)
        fixed = fixed_mass(targets, n)
        assert rational(row["fixed_bias_second_core_probability"]) == fixed
        assert rational(row["kernel_to_fixed_ratio"]) == expected["mixture"] / fixed
        assert row["kernel_vs_fixed"] == "greater" and expected["mixture"] > fixed
        for final_comparison in row["A_final_comparisons"]:
            seed = final_comparison["seed"]
            final = final_mass(laws[(degree, seed)], targets, n)
            saved = next(g for g in final_rows[(degree, seed)]["core_groups"]
                         if tuple(g["core_coefficients_ascending"]) == SECOND)
            assert rational(saved["final_probability"]) == final
            assert rational(final_comparison["A_final_second_core_probability"]) == final
            assert rational(final_comparison["kernel_to_A_final_ratio"]) == expected["mixture"] / final
            assert final_comparison["comparison"] == "greater" and expected["mixture"] > final
        libraries[degree] = (set(parents), targets, expected["mixture"], fixed)
        whole_summary.append({"degree": degree, "counts": expected["counts"],
                              "branches": sum(expected["totals"].values()),
                              "boundary_returns": expected["exits"],
                              "mutation": str(expected["mutation"]), "mixture": str(expected["mixture"])})
    for group in acquired["runs"]:
        degree, seed = group["degree"], group["seed"]
        library, targets, complete, fixed = libraries[degree]
        parents = [tuple(p["free_coefficients"]) for p in group["parents"]]
        assert set(parents) <= library
        expected = enumerate_kernel(parents, targets)
        row = observed_rows[(degree, seed)]
        check_kernel_row(row, expected)
        occurrences = [o for p in group["parents"] for o in p["occurrences"]]
        assert row["kernel_defined"] and row["distinct_observed_parents"] == len(parents)
        assert row["complete_parent_library_size"] == len(library)
        assert row["raw_Lehmer_target_hits"] == len(occurrences)
        assert row["cached_target_hits"] == sum(o[2] for o in occurrences)
        assert row["repeated_target_hits"] == sum(o[3] for o in occurrences)
        assert row["fresh_repeated_target_hits"] == sum(o[3] and not o[2] for o in occurrences)
        assert row["first_parent_elapsed"] == min(p["occurrences"][0][1] for p in group["parents"])
        assert row["last_new_parent_elapsed"] == max(p["occurrences"][0][1] for p in group["parents"])
        final = final_mass(laws[(degree, seed)], targets, degree // 2)
        for name, probability in (("complete_library_probability", complete), ("fixed_bias_probability", fixed),
                                  ("A_final_probability", final)):
            assert rational(row[name]) == probability
        for name, probability in (("to_complete_library", complete), ("to_fixed_bias", fixed), ("to_A_final", final)):
            assert rational(row["ratios"][name]) == expected["mixture"] / probability
        observed_summary.append({"degree": degree, "seed": seed, "parents": len(parents),
                                 "counts": expected["counts"], "branches": sum(expected["totals"].values()),
                                 "reachable": expected["reachable"], "mixture": str(expected["mixture"])})
    assert sum(row["branches"] for row in whole_summary) == 544156
    assert sum(row["branches"] for row in observed_summary) == 55650
    return {"geometry": geometry_check(states), "complete": whole_summary, "observed": observed_summary}


def history_checks(acquired, comparison):
    """Reconstruct seen membership and LRU directly from committed event triples."""
    sources = {(r["degree"], r["seed"]): r for group in comparison["groups"]
               for r in group["all_seed_outcomes"] if r["arm"] == "A"}
    summary = []
    started = monotonic()
    for saved in acquired["runs"]:
        source = sources[(saved["degree"], saved["seed"])]
        parents, seen, lru = {}, set(), OrderedDict()
        counts = Counter()
        proposal = evaluation = config = None
        last_commit = None
        with (OUTPUT / source["events_file"]).open(encoding="utf-8") as stream:
            for number, line in enumerate(stream, 1):
                if number % 1024 == 0 and monotonic()-started > 60:
                    raise TimeoutError("review history ceiling exceeded")
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    break
                kind = event["kind"]
                if kind == "config":
                    assert config is None and event == source["configuration"]
                    config = event
                elif kind == "proposal":
                    proposal, evaluation = event, None
                    counts["proposals"] += event["elapsed"] <= config["seconds"]
                elif kind == "evaluation":
                    evaluation = event
                elif kind == "commit" and event["elapsed"] <= config["seconds"]:
                    counts["committed"] += 1
                    assert event["proposal"] == proposal["proposal"] == evaluation["proposal"] == counts["committed"]
                    prefix = tuple(proposal["free_coefficients"])
                    assert len(prefix) * 2 == saved["degree"] and all(type(a) is int and a in ALPHABET for a in prefix)
                    assert evaluation["cached"] == (prefix in lru)
                    assert evaluation["repeated_proposal"] == (prefix in seen)
                    assert not evaluation.get("unresolved_error")
                    seen.add(prefix)
                    if prefix in lru:
                        del lru[prefix]
                    lru[prefix] = True
                    if len(lru) > config["cache_size"]:
                        del lru[next(iter(lru))]
                    counts["cached"] += evaluation["cached"]
                    counts["repeated"] += evaluation["repeated_proposal"]
                    last_commit = event["elapsed"]
                    if evaluation["thresholds"]["6/5"] != "below":
                        continue
                    counts["targets"] += 1
                    cert = evaluation["certificate"]
                    assert cert["coefficients_ascending"] == [1, *prefix, *reversed(prefix[:-1]), 1]
                    assert cert["root_count_with_multiplicity"] == saved["degree"]
                    assert cert["precision_bits"] == 128 and cert["factorization_product_verified"]
                    assert cert["ranking_resolved"] and not cert["neutral"]
                    assert cert["thresholds"]["6/5"] == "below"
                    lower, upper = (Fraction(a) * Fraction(2)**b for a, b in cert["measure_interval"])
                    assert 1 < lower <= upper < Fraction(6, 5)
                    assert cert["core_coefficients_ascending"] == evaluation["core_coefficients_ascending"]
                    if tuple(cert["core_coefficients_ascending"]) != LEHMER:
                        counts["other_targets"] += 1
                        continue
                    counts["Lehmer"] += 1
                    occurrence = [event["proposal"], event["elapsed"], evaluation["cached"], evaluation["repeated_proposal"]]
                    if prefix not in parents:
                        assert not occurrence[2] and not occurrence[3]
                        names = ("core_coefficients_ascending", "measure_interval", "measure_ball", "neutral", "thresholds",
                                 "precision_bits", "root_count_with_multiplicity", "factorization_product_verified")
                        parents[prefix] = {"free_coefficients": list(prefix),
                                           "first_certificate": {key: cert[key] for key in names}, "occurrences": []}
                    else:
                        assert occurrence[3]
                    parents[prefix]["occurrences"].append(occurrence)
        assert list(parents.values()) == saved["parents"]
        assert len(parents) == saved["distinct_parent_count"]
        assert counts["committed"] == saved["committed_proposals"] == source["counts"]["completed_proposals"]
        assert counts["proposals"] == source["counts"]["proposals"]
        assert counts["cached"] == source["counts"]["cache_hits"]
        assert counts["repeated"] == source["counts"]["repeated_proposals"]
        assert counts["targets"] == saved["all_target_evaluations"] == source["raw_whole_hits"]["6/5"]
        assert counts["Lehmer"] == saved["Lehmer_target_evaluations"]
        assert counts["other_targets"] == saved["other_core_target_evaluations"]
        assert last_commit == source["last_committed_elapsed"]
        summary.append({"degree": saved["degree"], "seed": saved["seed"], **dict(counts)})
    import acquired_parent_control
    replayed = acquired_parent_control.extract(HERE / "inputs" / "degree_comparison.json", OUTPUT, 60)
    assert replayed == acquired
    assert sum(row["committed"] for row in summary) == 135269
    return summary


def totient(value):
    result, remaining, p = value, value, 2
    while p*p <= remaining:
        if remaining % p == 0:
            result -= result // p
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        result -= result // remaining
    return result


@lru_cache(None)
def neutral_by_multiplicities(degree):
    """Independent nondecreasing factor-multiset traversal, with no height cutoff."""
    from flint import fmpz_poly
    if degree == 0:
        return {(1,)}
    factors = [(2, fmpz_poly([1, -2, 1])), (2, fmpz_poly([1, 2, 1]))]
    for order in range(3, 2*degree*degree+1):
        width = totient(order)
        if width <= degree:
            factor = fmpz_poly.cyclotomic(order)
            assert factor.degree() == width
            factors.append((width, factor))
    factors.sort(key=lambda item: (item[0], tuple(item[1])))
    outputs = set()
    def visit(start, remaining, polynomial):
        if remaining == 0:
            outputs.add(tuple(map(int, polynomial)))
            return
        for index in range(start, len(factors)):
            width, factor = factors[index]
            if width > remaining:
                break
            visit(index, remaining-width, polynomial*factor)
    visit(0, degree, fmpz_poly([1]))
    return outputs


def closure_checks(states, compare_saved):
    from flint import fmpz_poly
    import cyclotomic_closure as author
    assert author.self_test()["normalized_representations_checked"] == 556
    result = []
    for core, degrees in ((LEHMER, (18, 20, 24, 30)), (SECOND, (18, 20))):
        assert core == tuple(min(core[::-1], tuple(a*(-1)**i for i, a in enumerate(core))[::-1])[::-1])
        for degree in degrees:
            constructed, counts = set(), []
            for k in range(1, degree // (len(core)-1) + 1):
                remaining = degree-k*(len(core)-1)
                neutrals = neutral_by_multiplicities(remaining)
                assert neutrals == set(author.cyclotomic_products(remaining))
                accepted = 0
                for sign in (-1, 1):
                    coefficients = [0] * (k*(len(core)-1)+1)
                    for i, a in enumerate(core):
                        coefficients[k*i] = a*sign**i
                    positive = fmpz_poly(coefficients)
                    for neutral in neutrals:
                        full = tuple(map(int, positive*fmpz_poly(list(neutral))))
                        assert len(full) == degree+1 and full == full[::-1] and full[0] == full[-1] == 1
                        if max(map(abs, full)) <= 4:
                            constructed.add(full[1:degree//2+1])
                            accepted += 1
                counts.append({"substitution_index": k, "cyclotomic_degree": remaining,
                               "neutral_product_count": len(neutrals), "constructed_count": 2*len(neutrals),
                               "accepted_count": accepted})
            generated, author_counts = author.generate(core, degree)
            assert set(generated) == constructed and author_counts == counts
            assert sum(row["accepted_count"] for row in counts) == len(constructed)
            if degree in (18, 20):
                partition = next(p for p in states["target_partitions"] if p["degree"] == degree)
                target = next(g for g in partition["core_groups"] if tuple(g["core_coefficients_ascending"]) == core)
                assert constructed == set(map(tuple, target["target_prefixes"]))
            result.append({"core_degree": len(core)-1, "degree": degree, "count": len(constructed),
                           "construction_counts": counts})
    expected = {(10, 18): 174, (10, 20): 344, (10, 24): 1170, (10, 30): 5532, (18, 18): 2, (18, 20): 10}
    assert {(r["core_degree"], r["degree"]): r["count"] for r in result} == expected
    for filename, operation in (("cyclotomic_closure.json", author.compare),
                                ("cyclotomic_closure_preparation.json", author.prepare)):
        actual = operation()
        if compare_saved:
            saved = json.loads((OUTPUT / filename).read_text(encoding="utf-8"))
            saved.pop("generation_seconds", None)
            actual.pop("generation_seconds", None)
            for obj in (saved, actual):
                for group in obj["groups"]:
                    group.pop("generation_seconds", None)
            assert actual == saved
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--with-history", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT / "independent_offline_controls_review.json")
    args = parser.parse_args()
    states, comparison, masses = (read(name) for name in ("degree_core_mass_states.json", "degree_comparison.json", "degree_core_mass.json"))
    full, acquired, observed = (read(name) for name in ("mutation_kernel_control.json", "acquired_parent_states.json", "acquired_parent_control.json"))
    result = {"scope": "Fixed offline controls only; no random sampling, root certification or future live algorithm review.",
              "kernels": kernel_checks(states, comparison, masses, full, acquired, observed),
              "closure": closure_checks(states, args.with_history)}
    if args.with_history:
        result["history"] = history_checks(acquired, comparison)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"passed": True, "complete_branches": 544156, "observed_branches": 55650,
                      "history_commits": sum(r["committed"] for r in result.get("history", [])),
                      "closure_counts": [{"core_degree": r["core_degree"], "degree": r["degree"], "count": r["count"]}
                                         for r in result["closure"]]}))


if __name__ == "__main__":
    main()
