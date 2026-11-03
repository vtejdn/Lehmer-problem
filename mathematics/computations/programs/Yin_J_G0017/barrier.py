"""A closed plateau certificate and a bounded one-unit energy excursion."""
from collections import deque
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

from main import N, energy, mutation, normalize

HERE = _J_OUTPUT


def search(start, ceiling, cap, goal_search):
    pending = deque([start])
    parents = {start: None}
    truncated = False
    while pending:
        v = pending.popleft()
        for i in range(N - 1):
            for inverse in (False, True):
                raw = mutation(v, i, inverse)
                if energy(raw) > ceiling:
                    continue
                w, signs, goal = normalize(raw)
                move = {"index": i, "inverse": inverse, "signs": signs}
                if goal and goal_search:
                    path = [move]
                    cursor = v
                    while parents[cursor] is not None:
                        prev, prior = parents[cursor]
                        path.append(prior)
                        cursor = prev
                    return "goal", list(reversed(path)), list(parents), w
                if w not in parents:
                    if len(parents) < cap:
                        parents[w] = v, move
                        pending.append(w)
                    else:
                        truncated = True
    return "cap" if truncated else "closed", [], list(parents), None


def main():
    data = json.loads((HERE / "paths.json").read_text())
    record = next(r for r in data["records"] if r["source_trial"] == 75)
    initial = tuple(x for row in record["final_matrix"] for x in row)
    start, signs, goal = normalize(initial)
    assert not goal and energy(start) == 10
    status, _, states, _ = search(start, 10, 1000, False)
    assert status == "closed" and len(states) == 50
    result = {"source_trial": 75, "matrix": record["final_matrix"], "initial_signs": signs,
              "closed_plateau": {"ceiling": 10, "states": [list(s) for s in states]}}
    status, path, seen, end = search(start, 11, 30000, True)
    result["excursion"] = {"ceiling": 11, "node_cap": 30000, "outcome": status, "discovered_nodes": len(seen),
                           "moves": path, "final_matrix": None if end is None else [list(end[i*N:(i+1)*N]) for i in range(N)]}
    (HERE / "barrier.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"closed_plateau_states": len(states), "excursion_outcome": status,
                      "excursion_nodes": len(seen), "excursion_moves": len(path)}))


if __name__ == "__main__":
    main()
