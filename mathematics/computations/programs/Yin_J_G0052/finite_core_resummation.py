"""Exact d<=8 core resummation at t=173/100 on existing shortest data.

No new state or graph is generated.  The finite core inverse must be paid:
a positive solution and an eight-step strict killed-row contraction are
checked before the inverse is used as a nonnegative chronological series.
Outside unknown successor contributions give lower bounds only.
"""

from fractions import Fraction as F
import json
from pathlib import Path
from time import monotonic

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / "outputs" / HERE.name
T = F(173, 100)
CORE_DEPTH = 8


def enc(q):
    return [q.numerator, q.denominator]


def invert(a, check_time):
    n = len(a)
    work = [row[:] + [F(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        check_time()
        pivot = next(i for i in range(j, n) if work[i][j])
        work[j], work[pivot] = work[pivot], work[j]
        q = work[j][j]
        work[j] = [x / q for x in work[j]]
        for i in range(n):
            if i != j and work[i][j]:
                q = work[i][j]
                work[i] = [x - q*y for x, y in zip(work[i], work[j])]
    assert all(work[i][j] == (i == j) for i in range(n) for j in range(n))
    return [row[n:] for row in work]


def matvec(a, x):
    return [sum((q*y for q, y in zip(row, x) if q), F(0)) for row in a]


def main():
    started = monotonic()

    def check_time():
        if monotonic() - started > 120:
            raise RuntimeError("Existing-data core calculation exceeded 120 seconds")

    data = json.loads((OUT / "shortest_first_hit_24.json").read_text())
    verified = json.loads((OUT / "geodesic_level9_check.json").read_text())
    assert data["status"] == "complete" and data["completed_depth"] == 24
    assert verified["status"] == "passed"
    states = data["states"]
    assert len(states) == 417 and data["known_rows"] == 354
    rows = {r["id"]: r for r in data["rows"]}
    distances = [s["distance"] for s in states]
    cert = {tuple(s["state"]): s for s in verified["verified_distances_and_masses"]}
    core = [i for i in range(1, len(states)) if distances[i] <= CORE_DEPTH]
    outside = [i for i in range(1, len(states)) if distances[i] > CORE_DEPTH]
    assert len(core) == 46 and len(outside) == 370
    pos = {i: j for j, i in enumerate(core)}
    required = set(core)
    for i in core:
        assert rows[i]["all_legal_successor_distances_known"]
        required.update(e["id"] for e in rows[i]["successors"] if e["legal"])
    for i in required:
        q = cert[tuple(states[i]["state"])]
        assert q["distance"] == distances[i]
        assert q["mass_numerator_over_4_to_d"] == states[i]["shortest_mass_numerator"]

    n = len(core)
    a = [[F(i == j) for j in range(n)] for i in range(n)]
    bcc = [[F(0) for _ in core] for _ in core]
    rhs = [F(0) for _ in core]
    exits = set()
    for i in core:
        for e in rows[i]["successors"]:
            if not e["legal"]:
                continue
            j, weight = e["id"], F(e["integer_weight"], 4)
            if j == 0:
                rhs[pos[i]] += T * weight
            elif j in pos:
                bcc[pos[i]][pos[j]] += weight
                a[pos[i]][pos[j]] -= T * weight
            else:
                exits.add(j)
    z = invert(a, check_time)
    assert all(q >= 0 for row in z for q in row)
    # Multiplication checks the actual unmodified rational system.
    for j in range(n):
        check_time()
        assert matvec(a, [z[i][j] for i in range(n)]) == [F(i == j) for i in range(n)]
    u = matvec(z, rhs)
    assert min(u) > 0 and matvec(a, u) == rhs
    killed = [[T * bcc[i][j] * u[j] / u[i] for j in range(n)] for i in range(n)]
    assert all(sum(row) <= 1 for row in killed)
    survival = [F(1)] * n
    for _ in range(CORE_DEPTH):
        survival = matvec(killed, survival)
    assert max(survival) < 1

    baseline = [F(1)] + [F(0)] * (len(states)-1)
    for i in core:
        baseline[i] = u[pos[i]]
    for i in outside:
        check_time()
        for e in rows[i]["successors"]:
            if e["legal"] and e["distance_known"] and distances[e["id"]] == distances[i]-1:
                assert e["id"] < i
                baseline[i] += T * F(e["integer_weight"],4) * baseline[e["id"]]
        assert baseline[i] > 0

    exit_rhs = [F(0)] * n
    for i in core:
        for e in rows[i]["successors"]:
            if e["legal"] and e["id"] in exits:
                exit_rhs[pos[i]] += T * F(e["integer_weight"],4) * baseline[e["id"]]
    feedback = matvec(z, exit_rhs)
    assert matvec(a, feedback) == exit_rhs
    # Numerator of the new normalized row: whole core exit feedback plus
    # first nongeodesic edges before reaching that core.
    numerator = [F(0)] * len(states)
    exact = [True] * len(states)
    for i in core:
        numerator[i] = feedback[pos[i]]
    for i in outside:
        check_time()
        for e in rows[i]["successors"]:
            if not e["legal"]:
                continue
            if not e["distance_known"]:
                exact[i] = False
                continue
            j, weight = e["id"], T*F(e["integer_weight"],4)
            if distances[j] == distances[i]-1:
                numerator[i] += weight * numerator[j]
                exact[i] = exact[i] and exact[j]
            else:
                assert distances[j] >= distances[i] >= 9
                numerator[i] += weight * baseline[j]
    costs = [numerator[i]/baseline[i] for i in range(len(states))]
    levels = []
    for d in range(9,25):
        ids = data["levels"][d]
        lo, hi = min(ids,key=lambda i:costs[i]), max(ids,key=lambda i:costs[i])
        levels.append({"distance":d,"states":len(ids),"all_costs_exact":all(exact[i] for i in ids),
                       "minimum_lower_cost":enc(costs[lo]),"minimum_state_id":lo,
                       "maximum_lower_cost":enc(costs[hi]),"maximum_state_id":hi,
                       "minimum_above_one":costs[lo]>1})
    payload = {"status":"complete","scope":"existing417 states only; C=1<=d<=8; no new graph",
               "t":enc(T),"core_depth":8,"core_states":core,"exit_targets":sorted(exits),
               "core_and_exit_verified_targets":len(required),"core_matrix":
               [[enc(q) for q in row] for row in bcc],"core_u":[enc(q) for q in u],
               "core_inverse":[[enc(q) for q in row] for row in z],
               "inverse_check":"nonnegative and (I-t B_CC) Z=I exactly",
               "normalized_core_survival8":[enc(q) for q in survival],
               "strict_core_contraction8":enc(max(survival)),
               "baseline":[enc(q) for q in baseline],"core_exit_rhs":[enc(q) for q in exit_rhs],
               "core_exit_feedback":[enc(q) for q in feedback],
               "state_costs":[{"id":i,"exact":exact[i],"lower_cost":enc(costs[i])} for i in range(len(states))],
               "levels":levels,"exact_outside_cost_count":sum(exact[i] for i in outside),
               "unknown_policy":"omitted positive nongeodesic targets produce lower bounds only",
               "limits":"one fixed t; no all-state upper bound, mean or R_f conclusion"}
    target = OUT / "finite_core_resummation_8.json"
    tmp = target.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload,separators=(",",":"))+"\n",encoding="utf-8")
    tmp.replace(target)
    print(json.dumps({"status":"complete","core_states":n,"exit_targets":len(exits),
                      "core_survival8_display":float(max(survival)),
                      "exact_outside_cost_count":payload["exact_outside_cost_count"],
                      "first_level_minimum_above_one":next((x for x in levels if x["minimum_above_one"]),None),
                      "display_only_levels":[[x["distance"],float(F(*x["minimum_lower_cost"])),
                                                float(F(*x["maximum_lower_cost"])),x["all_costs_exact"]] for x in levels]}))


if __name__ == "__main__":
    main()
