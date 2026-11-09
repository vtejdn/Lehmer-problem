"""Bounded exact enumeration of integer square multipliers at p=81, k=9.

Enumerate 0 < v^T G v <= 6 modulo v -> -v for the specified balanced base.
The search stops after one million tree nodes or 120 seconds, whichever is
first. A stopped traversal reports partial counts and makes no exclusion.
"""

from collections import Counter
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
from time import monotonic
import json
import sys

from flint import fmpz_mat, fmpz_poly

from balanced_control import certify_measure, plus_unit, quotient_square_unit
from galois_filters import moments, multiply, representative, trace_polynomials, word_polynomial


PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0151"))
from exterior19683 import separator_certificate
from shell import identity, jacobi, multiply_matrix, root_poly, upper_pivots


MAXIMUM_ENERGY = 6
MAXIMUM_NODES = 1_000_000
MAXIMUM_SECONDS = 120
TARGETS = {(6, 2): 0, (1, 3): 1, (2, 6): 2}


class EnumerationLimit(Exception):
    pass


def balanced_base():
    p, cut = 81, 9
    word, columns, exponent = representative(p, cut)
    assert exponent == 5
    forward = plus_unit(p, 2)["forward"]
    for _ in range(6):
        word = multiply(word, forward)
    word = multiply(word, plus_unit(p, 1)["inverse"])
    word = multiply(word, quotient_square_unit(p, 3, 5)["inverse"])
    assert moments(word) == (-3, 10)
    assert word[0] - word[1] == -30
    traces = trace_polynomials(p // 2)
    polynomial = word_polynomial(word, traces)
    denominator = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    assert abs(int(denominator.resultant(polynomial))) == 32
    return word, columns, polynomial, denominator, traces


def half_ball(rows, state):
    """Exact fraction-free LDL traversal, with the highest nonzero entry positive."""
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
                assert 0 < energy <= MAXIMUM_ENERGY
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


def quadratic_value(matrix, row):
    return int((row * matrix * row.transpose())[0, 0])


def inspect_hit(reduced, original, energy, first_moment, x, h_base, denominator, traces):
    t = traces[1]
    root = root_poly(original.entries(), t)
    root_resultant = int(denominator.resultant(root))
    record = {
        "x": x,
        "energy": energy,
        "K": first_moment,
        "reduced_vector": reduced,
        "basis_vector": list(map(int, original.entries())),
        "v_coefficients_ascending": list(map(int, root)),
        "root_resultant": root_resultant,
        "unit": abs(root_resultant) == 1,
        "strict_original_signs": root_resultant != 0,
    }
    if root_resultant == 0:
        return record
    h = (h_base * root**2) % denominator
    degree = denominator.degree()
    remainder = ((denominator - traces[degree]) * h) % denominator
    second_moment = int(remainder[degree - 2] - denominator[degree - 1] * first_moment)
    assert int(remainder[degree - 1]) == first_moment
    assert second_moment == -4 * x
    assert energy == 2 * second_moment + 3 * first_moment
    trace_lift = (t - 2 * x) * denominator + remainder
    resultant = abs(int(denominator.resultant(trace_lift)))
    assert resultant == 32 * root_resultant**2
    lift_degree = degree + 1
    lift = [
        sum(
            int(trace_lift[power]) * comb(power, (power + lift_degree - index) // 2)
            for power in range(abs(lift_degree - index), lift_degree + 1)
            if (power + lift_degree - index) % 2 == 0
        )
        for index in range(2 * lift_degree + 1)
    ]
    assert lift[0] == lift[-1] == 1 and lift == lift[::-1]
    endpoint = (-1) ** lift_degree * int(trace_lift(-2))
    assert endpoint == sum(value * (-1) ** index for index, value in enumerate(lift))
    record.update(
        L=second_moment,
        absolute_resultant=resultant,
        h_coefficients_ascending=list(map(int, h)),
        Q_coefficients_ascending=list(map(int, trace_lift)),
        P_coefficients_ascending=lift,
        P_minus_one=endpoint,
        strict_endpoint=endpoint > 0,
    )
    certify_measure(record)
    return record


def main():
    p, cut, dimension = 81, 9, 40
    assert separator_certificate(p, cut, Fraction(-3, 2)) == 31
    word, columns, h_base, denominator, traces = balanced_base()
    J, I = jacobi(dimension), identity(dimension)
    H = multiply_matrix(h_base, J, I)
    G = (2 * J + 3 * I) * H
    assert H == H.transpose() and G == G.transpose()
    assert int(H[0, 0]) == -3 and int((J * H)[0, 0]) == 10
    assert int(H.det()) in (-32, 32)
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
    print("Reduced Gram diagonal", [int(reduced_gram[i, i]) for i in range(dimension)], flush=True)

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
                x = TARGETS[(energy, first)]
                hit = inspect_hit(vector, row * change, energy, first, x, h_base, denominator, traces)
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
        "half_ball_counts": {str(energy): counts[energy] for energy in range(1, 7)},
        "moment_counts": [[energy, first, second, count] for (energy, first, second), count in sorted(moment_counts.items())],
        "joint_hits": hits,
    }
    output = Path(__file__).resolve().parents[2] / "outputs" / Path(__file__).resolve().parent.name
    output.mkdir(parents=True, exist_ok=True)
    (output / "low_energy_shell_81.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in ("complete", "stop_reason", "nodes", "enumeration_seconds", "half_ball_counts", "moment_counts")}), flush=True)
    print("Joint targets found", len(hits), flush=True)


if __name__ == "__main__":
    main()
