"""Distinct exact AUTHOR verification of the saved K8 boundary certificate.

Imports only the earlier generic polynomial/interval helper, not the boundary
producer, its searches, or the BFS implementation.  Rebuilds every needed
local predecessor/successor row, verifies all words and closed-domain zeros,
uses finite Boolean matrix closure for the boundary partition, and checks
every first-step diagonal-transfer term.  No additional graph vertices or
larger depth are generated.  Bounds: 417 supplied vertices, 16 MiB inputs,
120 seconds.  This is not an independent-agent R review.
"""

from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path
from time import monotonic

import verify_shortest_witness as exact

OUT = exact.OUT
INPUTS = ("shortest_first_hit_24.json", "geodesic_level9_check.json",
          "finite_core_resummation_8.json", "boundary_channels_8_existing.json")


def enc(q):
    return [q.numerator, q.denominator]


def main():
    started = monotonic()

    def guard():
        if monotonic() - started > 120:
            raise RuntimeError("120-second existing-boundary verification limit reached")

    assert sum((OUT / n).stat().st_size for n in INPUTS) <= 16 * 1024 * 1024
    data, cert, core, result = [json.loads((OUT / n).read_text(encoding="utf-8")) for n in INPUTS]
    assert data["status"] == core["status"] == result["status"] == "complete"
    assert cert["status"] == "passed" and cert["complete_states_through9"] == 57
    states = [tuple(r["state"]) for r in data["states"]]
    assert len(states) == len(set(states)) == 417
    index = {x: i for i, x in enumerate(states)}
    saved_rows = {r["id"]: r for r in data["rows"]}
    assert set(saved_rows) == set(range(1, 417))
    certified = {tuple(r["state"]): r["distance"] for r in cert["verified_distances_and_masses"]}
    assert sum(d <= 9 for d in certified.values()) == 57
    assert all(x in index for x, d in certified.items() if d <= 9)
    K = {index[x] for x, d in certified.items() if d <= 8}
    assert K == set(result["K"]) == set(range(47))
    assert sorted(K - {0}) == core["core_states"]
    assert result["state_cap"] == 417 and result["new_graph_vertices"] == 0

    lo, hi = F(43, 25), F(173, 100)

    def root_poly(t):
        return sum(c * t**i for i, c in enumerate(exact.POLY))

    assert root_poly(lo) < 0 < root_poly(hi)
    assert 4 * lo**3 - 3 * hi**2 - 2 * hi - 1 > 0
    for _ in range(60):
        midpoint = (lo + hi) / 2
        if root_poly(midpoint) > 0:
            hi = midpoint
        else:
            lo = midpoint
    exact.LOWER, exact.UPPER = lo, hi
    allowed = lru_cache(None)(lambda x: exact.certificate(x)["strict_core"])
    assert all(allowed(x) for x in states)
    inverse = (1, 1, 1, -1)
    assert exact.times((0, 1, 0, 0), inverse) == (1, 0, 0, 0)
    forward, backward = {}, {}
    unknown_f, unknown_b = [], []
    for i, x in enumerate(states):
        guard()
        forward[i], backward[i] = [], []
        for digit in (-1, 0, 1):
            weight = F(2 if digit == 0 else 1, 4)
            y = exact.step(x, digit)
            ok = allowed(y)
            if i:
                row = next(e for e in saved_rows[i]["successors"] if e["digit"] == digit)
                assert tuple(row["state"]) == y and row["legal"] == ok
                assert row["integer_weight"] == (2 if digit == 0 else 1)
                if ok:
                    assert row["distance_known"] == (y in index)
                    if y in index:
                        assert row["id"] == index[y]
            if ok:
                forward[i].append((index.get(y), digit, weight, y))
                if y not in index:
                    unknown_f.append((i, digit, y))
            shifted = tuple(c - (digit if j == 0 else 0) for j, c in enumerate(x))
            y = exact.times(inverse, shifted)
            assert exact.step(y, digit) == x
            if allowed(y):
                backward[i].append((index.get(y), digit, weight, y))
                if y not in index:
                    unknown_b.append((i, digit, y))
    assert unknown_f == [(r["queried_id"], r["digit"], tuple(r["tuple"])) for r in result["unknown_forward_rows"]]
    assert unknown_b == [(r["queried_id"], r["digit"], tuple(r["tuple"])) for r in result["unknown_predecessor_rows"]]
    assert all(j is not None for i in K for j, _, _, _ in forward[i] + backward[i])
    U = {j for i in K for j, _, _, _ in forward[i] if j not in K}
    V = {j for i in K for j, _, _, _ in backward[i] if j not in K}
    A = U | V
    assert sorted(U) == result["U"] == core["exit_targets"]
    assert sorted(V) == result["V"] == list(range(47, 57))
    assert sorted(A) == result["A"] and len(A) == 18
    local_certificates = []
    local_records = {r["id"]: r for r in result["core_and_boundary_local_rows"]}
    assert len(local_records) == len(result["core_and_boundary_local_rows"]) == len(K | A)
    assert set(local_records) == K | A
    for i, record in sorted(local_records.items()):
        assert tuple(record["state"]) == states[i]
        checked = {"id": i, "state": list(states[i])}
        for name in ("successors", "predecessors"):
            checked[name] = []
            assert [e["digit"] for e in record[name]] == [-1, 0, 1]
            for edge in record[name]:
                digit = edge["digit"]
                y = exact.step(states[i], digit) if name == "successors" else exact.times(
                    inverse, tuple(c - (digit if j == 0 else 0) for j, c in enumerate(states[i])))
                cert_y = exact.certificate(y)
                assert tuple(edge["tuple"]) == y and edge["legal"] == cert_y["strict_core"]
                assert edge["id"] == (index.get(y) if cert_y["strict_core"] else None)
                assert edge["original_weight"] == enc(F(2 if digit == 0 else 1, 4))
                checked[name].append(dict(edge, margin_intervals=cert_y["margin_intervals"]))
        local_certificates.append(checked)
    for row in result["boundary_states"]:
        i = row["id"]
        assert tuple(row["state"]) == states[i]
        assert row["in_U"] == (i in U) and row["in_V"] == (i in V)
        assert row["saved_distance"] == data["states"][i]["distance"]

    word_count, maximum_word_length = 0, 0

    def check_word(word, first=None, last=None, first_A=False):
        nonlocal word_count, maximum_word_length
        ids, digits = word["ids"], word["digits"]
        assert len(ids) == len(digits) + 1 and word["length"] == len(digits)
        assert all(isinstance(i, int) and 0 <= i < 417 and i not in K for i in ids)
        if first is not None:
            assert ids[0] == first
        if last is not None:
            assert ids[-1] == last
        if first_A:
            assert digits and all(i not in A for i in ids[1:-1])
        weight = F(1)
        for x, digit, y in zip(ids, digits, ids[1:]):
            assert digit in (-1, 0, 1)
            assert exact.step(states[x], digit) == states[y]
            assert allowed(states[x]) and allowed(states[y])
            weight *= F(2 if digit == 0 else 1, 4)
        assert enc(weight) == word["original_weight"] and weight > 0
        word_count += 1
        maximum_word_length = max(maximum_word_length, len(digits))

    domains = {}
    for key, rows, reverse in (("forward_domains", forward, False), ("backward_domains", backward, True)):
        recorded = {r["start_id"]: r for r in result[key]}
        assert set(recorded) == A
        domains[key] = {}
        for a, record in recorded.items():
            guard()
            seen, pending, hits, unknown = {a}, [a], set(), set()
            while pending:
                x = pending.pop()
                for y, digit, _, target in rows[x]:
                    if y is None:
                        unknown.add((x, digit, target))
                    elif y in K:
                        continue
                    elif y in A:
                        hits.add(y)
                    elif y not in seen:
                        seen.add(y)
                        pending.append(y)
            assert set(record["interior_ids"]) == seen - {a}
            assert record["closed"] == (not unknown)
            assert unknown == {(r["queried_id"], r["digit"], tuple(r["tuple"])) for r in record["unknown_frontier"]}
            assert hits == {r["other_id"] for r in record["known_boundary_hits"]}
            for hit in record["known_boundary_hits"]:
                b = hit["other_id"]
                check_word(hit["witness"], b if reverse else a, a if reverse else b, True)
            domains[key][a] = (seen - {a}, not unknown, hits)

    channels = {(r["from"], r["to"]): r for r in result["first_A_channels"]}
    assert set(channels) == {(a, b) for a in A for b in A}
    vertices = sorted(A)
    position = {a: i for i, a in enumerate(vertices)}
    lower = [[i == j for j in range(18)] for i in range(18)]
    upper = [[i == j for j in range(18)] for i in range(18)]
    positive, zero, finite = 0, 0, 0
    positive_polynomials = []
    for (a, b), rec in channels.items():
        Fset, Fclosed, Fhits = domains["forward_domains"][a]
        Bset, Bclosed, Bhits = domains["backward_domains"][b]
        assert (b in Fhits) == (a in Bhits)
        is_positive = b in Fhits
        is_finite = Fclosed or Bclosed
        is_zero = is_finite and not is_positive
        assert rec["known_positive"] == is_positive
        assert rec["complete_finite_channel"] == is_finite and rec["certified_zero"] == is_zero
        assert rec["finite_reason"] == [name for name, ok in
               (("forward_domain_closed", Fclosed), ("backward_domain_closed", Bclosed)) if ok]
        positive += is_positive
        zero += is_zero
        finite += is_finite
        if is_positive:
            check_word(rec["witness"], a, b, True)
            lower[position[a]][position[b]] = True
        if not is_zero:
            upper[position[a]][position[b]] = True
        if is_finite:
            assert rec["interior_ids"] == sorted(Fset & Bset)
            # In this exact saved K8 case every closed channel has empty interior.
            assert not rec["interior_ids"] and rec["cyclic_components"] == []
            assert rec["extra_cyclic_representatives"] == []
            weight = sum((w for j, _, w, _ in forward[a] if j == b), F(0))
            expected = [[1, *enc(weight)]] if weight else []
            assert rec["polynomial"] == expected
            assert rec["maximum_length"] == (1 if weight else 0)
            if weight:
                positive_polynomials.append([a, b, *enc(weight)])

    for matrix in (lower, upper):
        for k in range(18):
            for i in range(18):
                for j in range(18):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

    def matrix_components(matrix):
        pending, groups = set(vertices), []
        while pending:
            a = min(pending)
            group = sorted(b for b in pending if matrix[position[a]][position[b]] and matrix[position[b]][position[a]])
            groups.append(group)
            pending.difference_update(group)
        return groups

    known_groups, possible_groups = matrix_components(lower), matrix_components(upper)
    assert result["known_communication_blocks"] == known_groups
    assert result["possible_merged_blocks"] == possible_groups
    assert result["actual_scc_partition_certified"] == (known_groups == possible_groups)
    unresolved = [[a, b] for a in vertices for b in vertices if not lower[position[a]][position[b]] and upper[position[a]][position[b]]]
    absent = [[a, b] for a in vertices for b in vertices if not upper[position[a]][position[b]]]
    assert result["unresolved_reachability_pairs"] == unresolved
    assert result["certified_unreachable_pairs"] == absent
    pairs = set()
    for row in result["positive_boundary_words"]:
        a, b = row["from"], row["to"]
        assert (a, b) not in pairs and lower[position[a]][position[b]]
        pairs.add((a, b))
        check_word(row["witness"], a, b)
    assert pairs == {(a, b) for a in A for b in A if lower[position[a]][position[b]]}

    forced = result["forced_first_step"]
    anchor = forced["anchor"]
    block = next(g for g in known_groups if anchor in g)
    assert forced["boundary_block"] == block
    sources = {r["from"]: r for r in forced["sources"]}
    assert set(sources) == {72, 85, 88, 105}
    targets, expected_terms = set(), set()
    for a, record in sources.items():
        actual = [(j, e, w) for j, e, w, _ in forward[a] if j not in K]
        assert actual and all(j is not None for j, _, _ in actual)
        assert record["complete_outside_successors"] == [
            {"digit": e, "target_id": j, "original_weight": enc(w)} for j, e, w in actual]
        assert record["no_outside_predecessor"] == all(j in K for j, _, _, _ in backward[a])
        assert record["no_outside_predecessor"]
        for j, e, w in actual:
            targets.add(j)
            for b in block:
                expected_terms.add((a, b, j, e, w))
    assert forced["connector_targets"] == sorted(targets) == [61, 66, 74, 83, 113, 122]
    assert {r["target_id"] for r in forced["connector_words"]} == targets
    for row in forced["connector_words"]:
        check_word(row["anchor_to_target"], anchor, row["target_id"])
        check_word(row["target_to_anchor"], row["target_id"], anchor)
    actual_terms = set()
    max_closing = 0
    for row in forced["transfer_terms"]:
        a, b, z, e = row["from"], row["to"], row["first_target"], row["first_digit"]
        value = F(*row["first_weight"])
        term = (a, b, z, e, value)
        assert term not in actual_terms
        actual_terms.add(term)
        assert exact.step(states[a], e) == states[z]
        assert value == F(2 if e == 0 else 1, 4)
        check_word(row["closing_word"], b, z)
        max_closing = max(max_closing, row["closing_word"]["length"])
    assert actual_terms == expected_terms and len(actual_terms) == 60
    group_index = {a: i for i, g in enumerate(known_groups) for a in g}
    cross = [(a, b) for (a, b), r in channels.items()
             if not r["certified_zero"] and group_index[a] != group_index[b]]
    unpaid = [(a, b) for a, b in cross if not (a in sources and b in block)
              and "polynomial" not in channels[a, b]]
    assert forced["unpaid_crossings"] == [list(p) for p in unpaid]
    assert forced["all_crossings_paid_conditionally_on_diagonal_series"] == (not unpaid and known_groups == possible_groups)
    assert not unpaid and len(cross) == 42
    guard()
    report = {"status": "passed", "scope": "distinct exact AUTHOR row/word/closure verifier; not independent R",
              "inputs": list(INPUTS), "vertices": 417, "new_graph_vertices": 0,
              "input_cap_bytes": 16 * 1024 * 1024, "seconds_cap": 120,
              "root_interval": [str(lo), str(hi)], "K_count": len(K), "U": sorted(U), "V": sorted(V), "A": vertices,
              "forward_probes": 3 * 417, "predecessor_probes": 3 * 417,
              "core_and_boundary_local_certificates": local_certificates,
              "unknown_forward_edges": len(unknown_f), "unknown_predecessor_edges": len(unknown_b),
              "positive_first_A_channels": positive, "certified_zero_channels": zero, "finite_channels": finite,
              "positive_polynomial_channels": positive_polynomials,
              "actual_boundary_components": known_groups, "actual_scc_partition_certified": known_groups == possible_groups,
              "positive_reachability_pairs": len(pairs), "certified_unreachable_pairs": len(absent),
              "unresolved_reachability_pairs": unresolved,
              "checked_words": word_count, "maximum_checked_word_length": maximum_word_length,
              "forced_sources": sorted(sources), "connector_targets": sorted(targets),
              "complete_transfer_terms": len(actual_terms), "maximum_closing_word_length": max_closing,
              "crossing_channels": len(cross), "unpaid_crossings": unpaid,
              "mathematical_condition": "All boundary Green entries are finite IF D_K(t)<infinity; no diagonal estimate is proved here",
              "authority_limit": "K/level9 reuses its accepted exact scope; no independent full417 BFS or new R asserted"}
    target = OUT / "boundary_channels_8_check.json"
    pending = target.with_suffix(".json.tmp")
    pending.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    pending.replace(target)
    print(json.dumps({k: report[k] for k in ("status", "vertices", "positive_first_A_channels", "certified_zero_channels",
                     "actual_boundary_components", "actual_scc_partition_certified", "checked_words", "complete_transfer_terms",
                     "unpaid_crossings")}))


if __name__ == "__main__":
    main()
