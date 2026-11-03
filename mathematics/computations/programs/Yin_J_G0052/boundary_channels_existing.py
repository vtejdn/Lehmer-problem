"""Author probe of K={d<=8} boundary channels using only 417 saved states.

No graph vertex is generated or appended.  All three original successors and
predecessors are checked locally; legal tuples outside the supplied vertex set
are UNKNOWN frontier tuples and are never searched.  A closed forward or
reverse first-A domain gives a complete finite channel, not an extrapolation
from absence in an induced graph.  Limits: 417 vertices, 16 MiB total inputs,
120 seconds.  Existing data and its prior checks are not independent review
of this new calculation.
"""

from collections import deque
from fractions import Fraction
from functools import lru_cache
import json
from pathlib import Path
from time import monotonic

from shortest_first_hit import StrictCore

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / "outputs" / HERE.name
INPUTS = ("shortest_first_hit_24.json", "geodesic_level9_check.json",
          "finite_core_resummation_8.json")
TARGET = "boundary_channels_8_existing.json"
STATE_CAP = 417
INPUT_CAP = 16 * 1024 * 1024
SECONDS = 120


def forward(x, digit):
    a, b, c, d = x
    return (-d + digit, a + d, b + d, c + d)


def predecessor(y, digit):
    a, b, c, d = y
    return (a + b - digit, a + c - digit, a + d - digit, digit - a)


def fraction(q):
    return [q.numerator, q.denominator]


def witness(nodes, digits):
    assert len(nodes) == len(digits) + 1
    weight = Fraction(1)
    for digit in digits:
        weight *= Fraction(2 if digit == 0 else 1, 4)
    return {"ids": list(nodes), "digits": list(digits), "length": len(digits),
            "original_weight": fraction(weight)}


def components(vertices, adjacency, guard):
    vertices = set(vertices)
    reachable = {}
    for start in sorted(vertices):
        guard()
        seen, stack = {start}, [start]
        while stack:
            x = stack.pop()
            for y in adjacency[x]:
                if y in vertices and y not in seen:
                    seen.add(y)
                    stack.append(y)
        reachable[start] = seen
    pending, answer = set(vertices), []
    while pending:
        x = min(pending)
        group = sorted(y for y in pending if y in reachable[x] and x in reachable[y])
        answer.append(group)
        pending.difference_update(group)
    return answer, reachable


def run():
    started = monotonic()

    def guard():
        if monotonic() - started > SECONDS:
            raise RuntimeError("120-second existing-state boundary limit reached")

    assert sum((OUT / name).stat().st_size for name in INPUTS) <= INPUT_CAP
    data, level9, old_core = [json.loads((OUT / name).read_text(encoding="utf-8"))
                              for name in INPUTS]
    assert data["status"] == "complete" and data["completed_depth"] == 24
    assert level9["status"] == "passed" and old_core["status"] == "complete"
    states = [tuple(row["state"]) for row in data["states"]]
    assert len(states) == len(set(states)) == STATE_CAP and states[0] == (0, 0, 0, 0)
    ids = {x: i for i, x in enumerate(states)}
    distances = [row["distance"] for row in data["states"]]
    saved = {row["id"]: row for row in data["rows"]}
    assert set(saved) == set(range(1, STATE_CAP))
    certified = {tuple(row["state"]): row for row in level9["verified_distances_and_masses"]}
    assert level9["complete_states_through9"] == 57
    for i, x in enumerate(states):
        if distances[i] <= 9:
            assert certified[x]["distance"] == distances[i]
    K = set(i for i, d in enumerate(distances) if d <= 8)
    assert K == set(range(47)) and sorted(K - {0}) == old_core["core_states"]
    strip = StrictCore()
    assert all(strip.allowed(x) for x in states)
    rows, reverse_rows = {}, {}
    unknown_forward, unknown_reverse = [], []
    for i, x in enumerate(states):
        guard()
        rows[i], reverse_rows[i] = [], []
        for digit in (-1, 0, 1):
            weight = 2 if digit == 0 else 1
            y = forward(x, digit)
            legal = strip.allowed(y)
            j = ids.get(y)
            if i:
                rec = next(e for e in saved[i]["successors"] if e["digit"] == digit)
                assert tuple(rec["state"]) == y and rec["integer_weight"] == weight
                assert rec["legal"] == legal
                if legal:
                    assert rec["distance_known"] == (j is not None)
                    if j is not None:
                        assert rec["id"] == j
            if legal:
                edge = (j, digit, weight, y)
                rows[i].append(edge)
                if j is None:
                    unknown_forward.append({"queried_id": i, "digit": digit, "tuple": list(y)})
            p = predecessor(x, digit)
            assert forward(p, digit) == x
            if strip.allowed(p):
                j = ids.get(p)
                reverse_rows[i].append((j, digit, weight, p))
                if j is None:
                    unknown_reverse.append({"queried_id": i, "digit": digit, "tuple": list(p)})
        if i:
            assert saved[i]["all_legal_successor_distances_known"] == all(e[0] is not None for e in rows[i])
    # These are complete LOCAL row checks, not an appeal to depth-24 coverage.
    assert all(j is not None for i in K for j, _, _, _ in rows[i])
    assert all(j is not None for i in K for j, _, _, _ in reverse_rows[i])
    U = {j for i in K for j, _, _, _ in rows[i] if j not in K}
    V = {j for i in K for j, _, _, _ in reverse_rows[i] if j not in K}
    assert sorted(U) == old_core["exit_targets"]
    assert sorted(V) == data["levels"][9] == list(range(47, 57))
    A = U | V
    assert len(A) == 18
    exterior = set(range(STATE_CAP)) - K
    local_rows = []
    for i in sorted(K | A):
        local = {"id": i, "state": list(states[i])}
        for name, operation in (("successors", forward), ("predecessors", predecessor)):
            local[name] = []
            for digit in (-1, 0, 1):
                y = operation(states[i], digit)
                legal = strip.allowed(y)
                local[name].append({"digit": digit, "tuple": list(y), "legal": legal,
                                    "id": ids.get(y) if legal else None,
                                    "original_weight": fraction(Fraction(2 if digit == 0 else 1, 4))})
        local_rows.append(local)

    def first_search(start, backward=False):
        selected = reverse_rows if backward else rows
        paths = {start: ([start], [])}
        queue = deque([start])
        hits, frontier = {}, []
        while queue:
            guard()
            x = queue.popleft()
            node_path, digit_path = paths[x]
            for y, digit, _, target in selected[x]:
                if y is None:
                    frontier.append({"queried_id": x, "digit": digit, "tuple": list(target)})
                    continue
                if y in K:
                    continue
                if backward:
                    new_nodes, new_digits = [y] + node_path, [digit] + digit_path
                else:
                    new_nodes, new_digits = node_path + [y], digit_path + [digit]
                if y in A:
                    if y not in hits:
                        hits[y] = witness(new_nodes, new_digits)
                elif y not in paths:
                    paths[y] = (new_nodes, new_digits)
                    queue.append(y)
        return {"start_id": start, "direction": "backward" if backward else "forward",
                "interior_ids": sorted(set(paths) - {start}), "closed": not frontier,
                "unknown_frontier": frontier,
                "known_boundary_hits": [{"other_id": y, "witness": hits[y]} for y in sorted(hits)]}

    forward_domains = {a: first_search(a) for a in sorted(A)}
    backward_domains = {a: first_search(a, True) for a in sorted(A)}
    hits = {a: {row["other_id"]: row["witness"]
                for row in forward_domains[a]["known_boundary_hits"]} for a in A}
    reverse_hits = {a: {row["other_id"] for row in backward_domains[a]["known_boundary_hits"]} for a in A}
    assert all((b in hits[a]) == (a in reverse_hits[b]) for a in A for b in A)
    known_adj = {i: [j for j, _, _, _ in rows[i] if j is not None and j in exterior]
                 for i in exterior}
    scc_cache = {}

    def finite_structure(interior):
        key = tuple(sorted(interior))
        if key not in scc_cache:
            groups, _ = components(interior, known_adj, guard)
            cyclic = [g for g in groups if len(g) > 1 or (g and g[0] in known_adj[g[0]])]
            scc_cache[key] = cyclic
        return scc_cache[key]

    def polynomial(a, b, interior):
        indegree = {i: 0 for i in interior}
        for i in interior:
            for j in known_adj[i]:
                if j in interior:
                    indegree[j] += 1
        queue = deque(sorted(i for i in interior if indegree[i] == 0))
        order = []
        while queue:
            i = queue.popleft()
            order.append(i)
            for j in known_adj[i]:
                if j in interior:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        queue.append(j)
        assert len(order) == len(interior)
        mass = {i: {} for i in interior}
        result = {}
        for j, _, w, _ in rows[a]:
            if j == b:
                result[1] = result.get(1, Fraction(0)) + Fraction(w, 4)
            elif j in interior:
                mass[j][1] = mass[j].get(1, Fraction(0)) + Fraction(w, 4)
        for i in order:
            guard()
            for j, _, w, _ in rows[i]:
                if j != b and j not in interior:
                    continue
                target = result if j == b else mass[j]
                for length, value in mass[i].items():
                    target[length + 1] = target.get(length + 1, Fraction(0)) + value * Fraction(w, 4)
        return [[n, *fraction(value)] for n, value in sorted(result.items()) if value]

    channels, lower, upper = [], {a: [] for a in A}, {a: [] for a in A}
    for a in sorted(A):
        for b in sorted(A):
            guard()
            positive = b in hits[a]
            finite = forward_domains[a]["closed"] or backward_domains[b]["closed"]
            zero = finite and not positive
            rec = {"from": a, "to": b, "known_positive": positive,
                   "certified_zero": zero, "complete_finite_channel": finite,
                   "finite_reason": [name for name, ok in
                       (("forward_domain_closed", forward_domains[a]["closed"]),
                        ("backward_domain_closed", backward_domains[b]["closed"])) if ok]}
            if positive:
                rec["witness"] = hits[a][b]
                lower[a].append(b)
            if not zero:
                upper[a].append(b)
            if finite:
                interior = set(forward_domains[a]["interior_ids"]) & set(backward_domains[b]["interior_ids"])
                cyclic = finite_structure(interior)
                rec.update(interior_ids=sorted(interior), cyclic_components=cyclic,
                           extra_cyclic_representatives=[g[0] for g in cyclic])
                if not cyclic:
                    rec["polynomial"] = polynomial(a, b, interior)
                    rec["maximum_length"] = max((r[0] for r in rec["polynomial"]), default=0)
            channels.append(rec)
    lower_scc, lower_reach = components(A, lower, guard)
    upper_scc, upper_reach = components(A, upper, guard)
    # Complete positive reachability witnesses may revisit A, but never K.
    positive_words, path_maps = [], {}
    for a in sorted(A):
        paths = {a: ([a], [])}
        queue = deque([a])
        while queue:
            x = queue.popleft()
            nodes, digits = paths[x]
            for y, digit, _, _ in rows[x]:
                if y is None or y in K or y in paths:
                    continue
                paths[y] = (nodes + [y], digits + [digit])
                queue.append(y)
        path_maps[a] = paths
        for b in sorted(A & set(paths)):
            assert b in lower_reach[a]
            positive_words.append({"from": a, "to": b, "witness": witness(*paths[b])})
    unresolved = [[a, b] for a in sorted(A) for b in sorted(A)
                  if b not in lower_reach[a] and b in upper_reach[a]]
    unreachable = [[a, b] for a in sorted(A) for b in sorted(A) if b not in upper_reach[a]]
    # Complete first-step rows may lead to interior states in the same TRUE
    # exterior communication class as a boundary block.  Positive words in
    # both directions suffice; no full infinite SCC enumeration is asserted.
    anchor = 47
    anchor_block = next(g for g in lower_scc if anchor in g)
    reverse_paths = {anchor: ([anchor], [])}
    queue = deque([anchor])
    while queue:
        guard()
        x = queue.popleft()
        nodes, digits = reverse_paths[x]
        for y, digit, _, _ in reverse_rows[x]:
            if y is None or y in K or y in reverse_paths:
                continue
            reverse_paths[y] = ([y] + nodes, [digit] + digits)
            queue.append(y)
    first_steps, connector_targets, transfers = [], set(), []
    for a in sorted(A - set(anchor_block)):
        outside_edges = [e for e in rows[a] if e[0] not in K]
        if not outside_edges or any(e[0] is None for e in outside_edges):
            continue
        if not all(e[0] in path_maps[anchor] and e[0] in reverse_paths for e in outside_edges):
            continue
        edges = []
        for z, digit, weight, _ in outside_edges:
            connector_targets.add(z)
            edges.append({"digit": digit, "target_id": z, "original_weight": fraction(Fraction(weight, 4))})
            for b in anchor_block:
                nodes1, digits1 = path_maps[b][anchor]
                nodes2, digits2 = path_maps[anchor][z]
                closing = witness(nodes1 + nodes2[1:], digits1 + digits2)
                transfers.append({"from": a, "to": b, "first_target": z, "first_digit": digit,
                                  "first_weight": fraction(Fraction(weight, 4)), "closing_word": closing})
        first_steps.append({"from": a, "complete_outside_successors": edges,
                            "no_outside_predecessor": all(e[0] in K for e in reverse_rows[a])})
    forced_sources = {r["from"] for r in first_steps}
    connector_words = [{"target_id": z, "anchor_to_target": witness(*path_maps[anchor][z]),
                        "target_to_anchor": witness(*reverse_paths[z])} for z in sorted(connector_targets)]
    block_index = {a: i for i, group in enumerate(lower_scc) for a in group}
    remaining_crossings = [[r["from"], r["to"]] for r in channels
                          if not r["certified_zero"] and block_index[r["from"]] != block_index[r["to"]]]
    unpaid = [[a, b] for a, b in remaining_crossings
              if not (a in forced_sources and b in anchor_block)
              and not any(c["from"] == a and c["to"] == b and "polynomial" in c for c in channels)]
    return {"status": "complete", "scope": "existing 417 vertices only; local full rows; AUTHOR probe",
            "inputs": list(INPUTS), "state_cap": STATE_CAP, "total_input_cap_bytes": INPUT_CAP,
            "seconds_cap": SECONDS, "new_graph_vertices": 0,
            "K": sorted(K), "U": sorted(U), "V": sorted(V), "A": sorted(A),
            "core_and_boundary_local_rows": local_rows,
            "boundary_states": [{"id": i, "state": states[i], "saved_distance": distances[i],
                                 "in_U": i in U, "in_V": i in V} for i in sorted(A)],
            "unknown_forward_rows": unknown_forward, "unknown_predecessor_rows": unknown_reverse,
            "forward_domains": list(forward_domains.values()), "backward_domains": list(backward_domains.values()),
            "first_A_channels": channels, "positive_boundary_words": positive_words,
            "known_communication_blocks": lower_scc, "possible_merged_blocks": upper_scc,
            "actual_scc_partition_certified": lower_scc == upper_scc,
            "certified_unreachable_pairs": unreachable, "unresolved_reachability_pairs": unresolved,
            "forced_first_step": {"anchor": anchor, "boundary_block": anchor_block,
                                  "sources": first_steps, "connector_targets": sorted(connector_targets),
                                  "connector_words": connector_words, "transfer_terms": transfers,
                                  "unpaid_crossings": unpaid,
                                  "all_crossings_paid_conditionally_on_diagonal_series": not unpaid and lower_scc == upper_scc,
                                  "condition": "D_K(t)<infinity at the actual parameter t>0; no such bound is computed here"},
            "limits": "Unknown frontier tuples never become searched states; induced nonreachability is not actual nonreachability. No diagonal-tail, radius, mean or independent-review assertion."}


def main():
    try:
        payload = run()
    except Exception as error:
        failure = {"status": "incomplete", "scope": "existing417 boundary probe", "error": str(error),
                   "new_graph_vertices": 0}
        (OUT / "boundary_channels_8_existing.incomplete.json").write_text(json.dumps(failure, indent=2) + "\n", encoding="utf-8")
        raise
    target = OUT / TARGET
    pending = target.with_suffix(".json.tmp")
    pending.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
    pending.replace(target)
    print(json.dumps({"status": payload["status"], "boundary": payload["A"],
                      "known_communication_blocks": payload["known_communication_blocks"],
                      "possible_merged_blocks": payload["possible_merged_blocks"],
                      "actual_scc_partition_certified": payload["actual_scc_partition_certified"],
                      "positive_first_A_channels": sum(c["known_positive"] for c in payload["first_A_channels"]),
                      "certified_zero_channels": sum(c["certified_zero"] for c in payload["first_A_channels"]),
                      "finite_channels": sum(c["complete_finite_channel"] for c in payload["first_A_channels"]),
                      "unresolved_pairs": len(payload["unresolved_reachability_pairs"]),
                      "forced_sources": [r["from"] for r in payload["forced_first_step"]["sources"]],
                      "connector_targets": payload["forced_first_step"]["connector_targets"],
                      "unpaid_crossings": payload["forced_first_step"]["unpaid_crossings"]}))


if __name__ == "__main__":
    main()
