"""Exact integer-square traversal at energies one and two for p=81, k=9.

Use the frozen low_energy_shell.py base and verification routines. This
separate traversal has a five-million-node or 120-second stopping boundary.
"""

from collections import Counter
from fractions import Fraction
from math import isqrt
from pathlib import Path
from time import monotonic
import json

from flint import fmpz_mat

from low_energy_shell import (
    EnumerationLimit,
    balanced_base,
    identity,
    inspect_hit,
    jacobi,
    multiply_matrix,
    quadratic_value,
    separator_certificate,
    upper_pivots,
)


MAXIMUM_ENERGY = 2
MAXIMUM_NODES = 5_000_000
MAXIMUM_SECONDS = 120
TARGETS = {(1, 3): 1, (2, 6): 2}


def half_ball(rows, state):
    """Traverse every eligible integer vector modulo simultaneous negation."""
    vector = [0] * len(rows)

    def extend(index, budget, any_nonzero):
        if state["nodes"] >= MAXIMUM_NODES:
            raise EnumerationLimit("node_cap")
        if monotonic() - state["started"] >= MAXIMUM_SECONDS:
            raise EnumerationLimit("time_cap")
        state["nodes"] += 1
        if index < 0:
            if any_nonzero:
                energy = MAXIMUM_ENERGY - budget
                assert energy in (1, 2)
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
            loss = (pivot * entry + center) ** 2
            next_budget, residual = divmod(budget * previous - loss, pivot)
            assert residual == 0 and next_budget >= 0
            vector[index] = entry
            yield from extend(index - 1, next_budget, any_nonzero or entry != 0)

    yield from extend(len(rows) - 1, rows[-1][0] * MAXIMUM_ENERGY, False)


def main():
    p, cut, dimension = 81, 9, 40
    assert separator_certificate(p, cut, Fraction(-3, 2)) == 31
    word, columns, h_base, denominator, traces = balanced_base()
    J, I = jacobi(dimension), identity(dimension)
    H = multiply_matrix(h_base, J, I)
    G = (2 * J + 3 * I) * H
    assert H == H.transpose() and G == G.transpose()
    assert int(H[0, 0]) == -3 and int((J * H)[0, 0]) == 10
    assert abs(int(H.det())) == 32
    original_rows = upper_pivots(G)
    determinant = int(G.det())
    assert original_rows[-1][0] == determinant == 20436467236384
    reduced_gram, change = G.lll(transform=True, rep="gram", gram="exact")
    change_determinant = int(change.det())
    assert abs(change_determinant) == 1
    assert reduced_gram == change * G * change.transpose()
    rows = upper_pivots(reduced_gram)
    assert rows[-1][0] == determinant
    reduced_H = change * H * change.transpose()
    reduced_JH = change * (J * H) * change.transpose()
    print("Certified dimension, det(G), det(change)", dimension, determinant, change_determinant, flush=True)

    counts = Counter()
    moment_counts = Counter()
    hits = []
    state = {"nodes": 0, "started": monotonic()}
    stop_reason = "complete"
    try:
        for vector, energy in half_ball(rows, state):
            row = fmpz_mat([vector])
            assert quadratic_value(reduced_gram, row) == energy
            first = quadratic_value(reduced_H, row)
            second = quadratic_value(reduced_JH, row)
            assert energy == 3 * first + 2 * second
            counts[energy] += 1
            moment_counts[(energy, first, second)] += 1
            if (energy, first) in TARGETS:
                hit = inspect_hit(
                    vector, row * change, energy, first, TARGETS[(energy, first)],
                    h_base, denominator, traces,
                )
                hits.append(hit)
                print("Target hit", json.dumps({key: value for key, value in hit.items() if "coefficients" not in key and "vector" not in key}), flush=True)
    except EnumerationLimit as error:
        stop_reason = str(error)

    elapsed = monotonic() - state["started"]
    record = {
        "p": p,
        "cut": cut,
        "dimension": dimension,
        "base_word": word,
        "base_sign_columns": columns,
        "h_base_coefficients_ascending": list(map(int, h_base)),
        "base_K_L_U": [-3, 10, -30],
        "base_absolute_resultant": 32,
        "maximum_energy": MAXIMUM_ENERGY,
        "maximum_nodes": MAXIMUM_NODES,
        "maximum_seconds": MAXIMUM_SECONDS,
        "determinant_G": determinant,
        "determinant_change": change_determinant,
        "change_matrix": [[int(value) for value in row] for row in change.tolist()],
        "reduced_gram": [[int(value) for value in row] for row in reduced_gram.tolist()],
        "positive_pivots": [row[0] for row in rows],
        "complete": stop_reason == "complete",
        "stop_reason": stop_reason,
        "nodes": state["nodes"],
        "enumeration_seconds": elapsed,
        "half_ball_counts": {str(energy): counts[energy] for energy in (1, 2)},
        "moment_counts": [[energy, first, second, count] for (energy, first, second), count in sorted(moment_counts.items())],
        "joint_hits": hits,
    }
    output = Path(__file__).resolve().parents[2] / "outputs" / Path(__file__).resolve().parent.name
    output.mkdir(parents=True, exist_ok=True)
    (output / "two_energy_shell_81.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in ("complete", "stop_reason", "nodes", "enumeration_seconds", "half_ball_counts", "moment_counts")}), flush=True)
    print("Joint targets found", len(hits), flush=True)


if __name__ == "__main__":
    main()
