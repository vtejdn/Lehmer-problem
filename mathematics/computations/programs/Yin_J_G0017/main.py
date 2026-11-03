"""Exact bounded plateau descent, with replayable sign/mutation paths."""
from __future__ import annotations

from collections import deque
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import time

N = 10
NODE_CAP = 4000
SEGMENT_CAP = 12
HERE = _J_OUTPUT


def energy(v):
    return sum(a * a for a in v) - N


def mutation(v, i, inverse):
    a = v[i * N + i + 1]
    w = list(v)
    w[i * N + i + 1] = -a
    for k in range(i):
        x, y = v[k * N + i], v[k * N + i + 1]
        w[k * N + i], w[k * N + i + 1] = (y - a*x, x) if inverse else (y, x - a*y)
    for k in range(i + 2, N):
        x, y = v[i * N + k], v[(i + 1) * N + k]
        w[i * N + k], w[(i + 1) * N + k] = (y - a*x, x) if inverse else (y, x - a*y)
    return tuple(w)


def normalize(v):
    """Make a deterministic spanning forest negative by diagonal signs."""
    signs = [0] * N
    balanced = True
    for root in range(N):
        if signs[root]:
            continue
        signs[root] = 1
        pending = deque([root])
        while pending:
            i = pending.popleft()
            for j in range(N):
                a = v[min(i, j) * N + max(i, j)] if i != j else 0
                if not a:
                    continue
                required = (-1 if a > 0 else 1) * signs[i]
                if signs[j] and signs[j] != required:
                    balanced = False
                elif not signs[j]:
                    signs[j] = required
                    pending.append(j)
    w = tuple(v[i * N + j] * signs[i] * signs[j] for i in range(N) for j in range(N))
    return w, signs, balanced


def descend_segment(v):
    """Breadth-first equal-energy graph, stopping at a decrease or goal."""
    level = energy(v)
    pending = deque([v])
    parents = {v: None}
    frontier_truncated = False
    while pending:
        current = pending.popleft()
        for i in range(N - 1):
            for inverse in (False, True):
                raw = mutation(current, i, inverse)
                if energy(raw) > level:
                    continue
                w, signs, goal = normalize(raw)
                move = {"index": i, "inverse": inverse, "signs": signs}
                if goal or energy(w) < level:
                    path = [move]
                    cursor = current
                    while parents[cursor] is not None:
                        previous, prior_move = parents[cursor]
                        path.append(prior_move)
                        cursor = previous
                    path.reverse()
                    return w, path, len(parents), "goal" if goal else "decrease"
                if w not in parents:
                    if len(parents) >= NODE_CAP:
                        frontier_truncated = True
                    else:
                        parents[w] = current, move
                        pending.append(w)
    return v, [], len(parents), "node_cap" if frontier_truncated else "exhausted_plateau"


def main():
    started = time.monotonic()
    source = json.loads((HERE.parent / "Yin_J_G0016" / "results.json").read_text(encoding="utf-8"))
    terminals = [item for item in source["orbit_sample"]["terminals"] if not item["switchable"]]
    records = []
    for number, item in enumerate(terminals):
        initial = tuple(a for row in item["matrix"] for a in row)
        current, initial_signs, balanced = normalize(initial)
        assert not balanced and energy(current) == item["energy"]
        record = {"source_trial": item["trial"], "initial_matrix": item["matrix"],
                  "initial_signs": initial_signs, "initial_energy": energy(initial), "segments": [], "moves": []}
        for _ in range(SEGMENT_CAP):
            before = energy(current)
            current, path, nodes, outcome = descend_segment(current)
            record["segments"].append({"from_energy": before, "to_energy": energy(current), "nodes": nodes,
                                       "move_count": len(path), "outcome": outcome})
            record["moves"].extend(path)
            if outcome != "decrease":
                break
        record["outcome"] = record["segments"][-1]["outcome"]
        if record["outcome"] == "decrease":
            record["outcome"] = "segment_cap"
        record["final_matrix"] = [list(current[i * N:(i + 1) * N]) for i in range(N)]
        record["final_energy"] = energy(current)
        records.append(record)
        if (number + 1) % 10 == 0 or record["outcome"] != "goal":
            print(json.dumps({"processed": number + 1, "outcome": record["outcome"], "energy": energy(current),
                              "moves": len(record["moves"]), "elapsed_seconds": round(time.monotonic() - started, 2)}), flush=True)
    summary = {"inputs": len(records), "goals": sum(r["outcome"] == "goal" for r in records),
               "outcomes": sorted({r["outcome"] for r in records}),
               "final_energies": sorted({r["final_energy"] for r in records}),
               "max_moves": max(len(r["moves"]) for r in records),
               "max_nodes_in_segment": max(s["nodes"] for r in records for s in r["segments"]),
               "total_nodes": sum(s["nodes"] for r in records for s in r["segments"])}
    result = {"parameters": {"node_cap_per_segment": NODE_CAP, "segment_cap": SEGMENT_CAP},
              "source": "../Yin_J_G0016/results.json", "summary": summary, "records": records}
    (HERE / "paths.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
