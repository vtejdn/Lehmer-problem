"""Exact E<=6 scans in three fixed p=81, k=9 integer-square families.

Each invocation selects one previously fixed base, reconstructs it from
source, and uses an explicit 20-million-node or 120-second traversal limit.
No imported traversal constants or frozen source files are changed.
"""

import argparse
from collections import Counter
from fractions import Fraction
from math import isqrt
from pathlib import Path
from time import monotonic
import json

from flint import arb, ctx, fmpq, fmpz_mat, fmpz_poly

from balanced_control import certify_measure, polynomial_data
from galois_filters import moments, trace_polynomials, word_polynomial
from low_energy_shell import (
    EnumerationLimit, identity, jacobi, multiply_matrix, quadratic_value,
    root_poly, separator_certificate, upper_pivots,
)
from nonsquare_control import lll_certificate, matrix_list, polynomial_word
from signed_filters import balanced_base as balanced_word, construct


MAXIMUM_ENERGY = 6
MAXIMUM_NODES = 20_000_000
MAXIMUM_SECONDS = 120
BASE_NORMS = {"original": 32, "single": 5216, "paired": 850208}
FILTERS = {"original": [], "single": [1], "paired": [1, 2]}


def half_ball(rows, maximum_energy, maximum_nodes, maximum_seconds, state):
    """Exact fraction-free traversal with explicit scope and stopping bounds."""
    vector = [0] * len(rows)

    def extend(index, budget, any_nonzero):
        stop = None
        if state["nodes"] >= maximum_nodes:
            stop = "node_cap"
        elif monotonic() - state["started"] >= maximum_seconds:
            stop = "time_cap"
        if stop:
            state["first_unentered_call"] = {
                "index": index, "scaled_budget": budget,
                "higher_coordinates": vector[index + 1:],
                "higher_nonzero": any_nonzero,
            }
            raise EnumerationLimit(stop)
        state["nodes"] += 1
        if index < 0:
            if any_nonzero:
                energy = maximum_energy - budget
                assert 0 < energy <= maximum_energy
                yield tuple(vector), energy
            return
        pivot, *cross = rows[index]
        previous = rows[index - 1][0] if index else 1
        center = sum(value * entry for value, entry in zip(cross, vector[index + 1:]))
        bound = isqrt(budget * previous)
        first = -((bound + center) // pivot)
        last = (bound - center) // pivot
        if not any_nonzero:
            first = max(0, first)
        for entry in range(first, last + 1):
            loss = (pivot * entry + center)**2
            next_budget, remainder = divmod(budget * previous - loss, pivot)
            assert remainder == 0 and next_budget >= 0
            vector[index] = entry
            yield from extend(index - 1, next_budget, any_nonzero or entry != 0)

    yield from extend(len(rows) - 1, rows[-1][0] * maximum_energy, False)


def reconstruct(name, B, traces):
    p, dimension, cut = 81, 40, 9
    if name == "original":
        word = balanced_word()
        one = (1,) + (0,) * (p - 1)
        first, second = moments(word)
        construction = {
            "p": p, "cut": cut, "filter_indices": [],
            "input_word": word, "input_norm": 32, "multiplier_norm": 1,
            "rectifier_word": one, "inverse_rectifier_word": one,
            "positive_multiplier_word": one, "K_L": [first, second],
            "energy_2L_plus_3K": 3 * first + 2 * second,
            "endpoint_U": word[0] - word[1],
        }
        assert (first, second) == (-3, 10)
    else:
        construction = construct(FILTERS[name])
    assert construction["input_norm"] == BASE_NORMS[name]
    h_base = word_polynomial(construction["input_word"], traces)
    q = word_polynomial(construction["rectifier_word"], traces)
    inverse_q = word_polynomial(construction["inverse_rectifier_word"], traces)
    positive = word_polynomial(construction["positive_multiplier_word"], traces)
    assert (q * inverse_q) % B == 1
    assert abs(int(B.resultant(q))) == 1
    assert abs(int(B.resultant(positive))) == construction["multiplier_norm"]
    assert abs(int(B.resultant(h_base))) == BASE_NORMS[name]
    ctx.prec = 512
    for index in range(1, dimension + 1):
        node = 2 * arb.cos_pi_fmpq(fmpq(2 * index, p))
        assert positive(node) > 0
        value = h_base(node)
        assert value > 0 if index <= dimension - cut else value < 0
    return construction, h_base


def inspect_hit(name, vector, original, h_base, B, traces, base_norm):
    """The only target here is x=0: E=6, K=2 and L=0."""
    root = root_poly(original.entries(), traces[1])
    root_resultant = int(B.resultant(root))
    record = {
        "x": 0, "energy": 6, "K": 2, "L": 0,
        "reduced_vector": vector,
        "basis_vector": list(map(int, original.entries())),
        "v_coefficients_ascending": list(map(int, root)),
        "root_resultant": root_resultant,
        "root_is_unit": abs(root_resultant) == 1,
        "strict_original_signs": root_resultant != 0,
        "whole_measure_computed": False,
    }
    if root_resultant == 0:
        return record
    h = (h_base * root**2) % B
    word = polynomial_word(h, 81)
    assert word_polynomial(word, traces) == h
    record.update(polynomial_data(81, word, 0, B, traces,
                                  base_norm * root_resultant**2))
    record["strict_endpoint"] = record["P_minus_one"] > 0
    if record["strict_endpoint"]:
        print("Starting full Mahler roots", name, "resultant", record["absolute_resultant"],
              "endpoint", record["P_minus_one"], flush=True)
        root_start = monotonic()
        certify_measure(record)
        record["root_seconds"] = monotonic() - root_start
        record["whole_measure_computed"] = True
        print("Full Mahler result", name, record["measure_ball"], flush=True)
    return record


def run(name):
    p, cut, dimension = 81, 9, 40
    base_norm = BASE_NORMS[name]
    assert separator_certificate(p, cut, Fraction(-3, 2)) == 31
    traces = trace_polynomials(dimension)
    B = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    construction, h_base = reconstruct(name, B, traces)
    J, I = jacobi(dimension), identity(dimension)
    H = multiply_matrix(h_base, J, I)
    JH = J * H
    separator = 2 * J + 3 * I
    G = separator * H
    assert H == H.transpose() and JH == JH.transpose() and G == G.transpose()
    assert [int(H[0, 0]), int(JH[0, 0])] == construction["K_L"]
    assert int(G[0, 0]) == construction["energy_2L_plus_3K"]
    determinant_H = int(H.det())
    determinant_separator = int(separator.det())
    assert abs(determinant_H) == base_norm
    original_rows = upper_pivots(G)
    determinant = int(G.det())
    assert original_rows[-1][0] == determinant
    assert determinant == determinant_separator * determinant_H
    assert determinant == 20436467236384 * (base_norm // 32)
    reduced_gram, change = G.lll(transform=True, rep="gram", gram="exact")
    change_determinant = int(change.det())
    assert abs(change_determinant) == 1
    assert reduced_gram == change * G * change.transpose()
    rows = upper_pivots(reduced_gram)
    assert rows[-1][0] == determinant
    reduction = lll_certificate(rows)
    reduced_H = change * H * change.transpose()
    reduced_JH = change * JH * change.transpose()
    print("Certified base, det(H), det(G), det(change)",
          name, determinant_H, determinant, change_determinant, flush=True)

    counts, moment_counts = Counter(), Counter()
    leaves, hits = [], []
    state = {"nodes": 0, "started": monotonic(), "first_unentered_call": None}
    stop_reason = "complete"
    try:
        for vector, energy in half_ball(
                rows, MAXIMUM_ENERGY, MAXIMUM_NODES, MAXIMUM_SECONDS, state):
            row = fmpz_mat([vector])
            assert quadratic_value(reduced_gram, row) == energy
            first = quadratic_value(reduced_H, row)
            second = quadratic_value(reduced_JH, row)
            assert energy == 3 * first + 2 * second
            counts[energy] += 1
            moment_counts[(energy, first, second)] += 1
            leaves.append({"E": energy, "K": first, "L": second,
                           "reduced_vector": vector})
            if (energy, first, second) == (6, 2, 0):
                print("Joint moment hit", name, "nodes", state["nodes"], flush=True)
                hit = inspect_hit(name, vector, row * change, h_base, B, traces, base_norm)
                hits.append(hit)
                print("Target inspection", name, json.dumps({
                    key: value for key, value in hit.items()
                    if "coefficients" not in key and "vector" not in key
                    and key != "h_word"}), flush=True)
    except EnumerationLimit as error:
        stop_reason = str(error)
    elapsed = monotonic() - state["started"]
    record = {
        "base": name, "p": p, "cut": cut, "dimension": dimension,
        "filter_indices": FILTERS[name], "construction": construction,
        "h_base_coefficients_ascending": list(map(int, h_base)),
        "base_absolute_resultant": base_norm,
        "maximum_energy": MAXIMUM_ENERGY, "maximum_nodes": MAXIMUM_NODES,
        "maximum_seconds": MAXIMUM_SECONDS,
        "time_cap_scope": "traversal and leaf processing after construction and LLL",
        "determinant_H": determinant_H, "determinant_separator": determinant_separator,
        "determinant_G": determinant,
        "original_positive_pivots": [row[0] for row in original_rows],
        "determinant_change": change_determinant,
        "change_matrix": matrix_list(change), "reduced_gram": matrix_list(reduced_gram),
        "positive_pivots": [row[0] for row in rows], "lll_certificate": reduction,
        "complete": stop_reason == "complete", "stop_reason": stop_reason,
        "nodes": state["nodes"], "enumeration_seconds": elapsed,
        "first_unentered_call": state["first_unentered_call"],
        "half_ball_counts": {str(energy): counts[energy] for energy in range(1, 7)},
        "moment_counts": [[energy, first, second, count]
                          for (energy, first, second), count in sorted(moment_counts.items())],
        "leaves": leaves, "joint_hits": hits, "target_count": len(hits),
        "nonzero_resultant_target_count": sum(hit["root_resultant"] != 0 for hit in hits),
        "strict_endpoint_target_count": sum(hit.get("strict_endpoint", False) for hit in hits),
        "whole_measure_count": sum(hit["whole_measure_computed"] for hit in hits),
        "distinct_P_count": len({tuple(hit["P_coefficients_ascending"]) for hit in hits
                                  if "P_coefficients_ascending" in hit}),
    }
    source = Path(__file__).resolve()
    output = source.parents[2] / "outputs" / source.parent.name
    output.mkdir(parents=True, exist_ok=True)
    (output / f"energy_six_{name}_81.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in (
        "base", "complete", "stop_reason", "nodes", "enumeration_seconds",
        "half_ball_counts", "moment_counts", "target_count",
        "nonzero_resultant_target_count", "strict_endpoint_target_count",
        "whole_measure_count", "distinct_P_count")}), flush=True)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, choices=list(BASE_NORMS))
    args = parser.parse_args()
    run(args.base)


if __name__ == "__main__":
    main()
