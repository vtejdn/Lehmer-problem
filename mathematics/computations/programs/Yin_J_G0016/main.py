"""Exact signed Coxeter controls; finite randomized orbit sampling only."""
from __future__ import annotations

import json
import random
from collections import deque
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

import sympy as sp

X = sp.Symbol("t")


def coxeter_poly(v):
    return sp.Poly((-v.inv() * v.T).charpoly(X).as_expr(), X)


def energy(v):
    return sum(int(v[i, j]) ** 2 for i in range(v.rows) for j in range(i + 1, v.rows))


def absolute(v):
    return sp.eye(v.rows) - (v - sp.eye(v.rows)).applyfunc(abs)


def mutate(v, i, inverse=False):
    a = v[i, i + 1]
    p = sp.eye(v.rows)
    p[i:i + 2, i:i + 2] = sp.Matrix([[-a, 1], [1, 0]]) if inverse else sp.Matrix([[0, 1], [1, -a]])
    w = p.T * v * p
    assert w.is_upper and all(w[j, j] == 1 for j in range(w.rows))
    return w


def cover(v):
    w = sp.eye(2 * v.rows)
    swap = sp.Matrix([[0, 1], [1, 0]])
    for i in range(v.rows):
        for j in range(i + 1, v.rows):
            a = int(v[i, j])
            w[2*i:2*i+2, 2*j:2*j+2] = a * sp.eye(2) if a <= 0 else -a * swap
    return w


def switchable(v):
    signs = {}
    for start in range(v.rows):
        if start in signs:
            continue
        signs[start] = 1
        pending = [start]
        while pending:
            i = pending.pop()
            for j in range(v.rows):
                if i == j:
                    continue
                a = v[min(i, j), max(i, j)]
                if not a:
                    continue
                required = -sp.sign(a) * signs[i]
                if j in signs and signs[j] != required:
                    return False
                if j not in signs:
                    signs[j] = required
                    pending.append(j)
    return True


def reduce_energy(v):
    steps = 0
    while True:
        candidates = [(energy(w), i, inverse, w)
                      for i in range(v.rows - 1)
                      for inverse in (False, True)
                      for w in [mutate(v, i, inverse)]]
        score, i, inverse, w = min(candidates, key=lambda z: z[:3])
        if score >= energy(v):
            return v, steps
        v = w
        steps += 1


def plateau_escape(v, node_cap=4000):
    """Search equal-energy moves until a strictly lower-energy endpoint is found."""
    level = energy(v)
    pending = deque([(v, [])])
    seen = {tuple(v)}
    while pending and len(seen) <= node_cap:
        current, path = pending.popleft()
        for i in range(v.rows - 1):
            for inverse in (False, True):
                w = mutate(current, i, inverse)
                steps = path + [[i, inverse]]
                if energy(w) < level:
                    return w, steps, len(seen)
                if energy(w) == level and tuple(w) not in seen:
                    seen.add(tuple(w))
                    pending.append((w, steps))
    return None, [], len(seen)


def lehmer_matrix():
    # Center plus branches of lengths 1, 2, 6: the Y_(2,3,7) tree.
    v = sp.eye(10)
    edges = [(0, 1), (0, 2), (2, 3), (0, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
    for i, j in edges:
        v[i, j] = -1
    return v


def fixed_lehmer_growth_witness():
    # Discovered by seed 10109 after 3151 adjacent mutation choices; the
    # witness is certified directly, so its discovery walk is not a premise.
    return sp.Matrix([
        [1, 2, -4, 4, 4, 0, -1, 1, 1, 0],
        [0, 1, -3, 3, 3, 0, -1, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, 1, 1, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ])


def main():
    out = {"exact_controls": []}
    for n in range(2, 13):
        v = sp.Matrix(n, n, lambda i, j: int(bool(i <= j)))
        p = coxeter_poly(v)
        assert p == sp.Poly(sum(X**j for j in range(n + 1)), X)
        # Explicit congruence to lower bidiagonal form, then reverse order.
        change = sp.eye(n)
        for i in range(n - 1):
            change[i + 1, i] = -1
        r = sp.zeros(n)
        for i in range(n):
            r[i, n - 1 - i] = 1
        chain = r.T * change.T * v * change * r
        assert chain == sp.eye(n) - sp.Matrix(n, n, lambda i, j: int(bool(j == i + 1)))
        assert coxeter_poly(chain) == p
        reduced, count = reduce_energy(v)
        assert coxeter_poly(reduced) == p
        if n <= 7:
            assert coxeter_poly(cover(v)) == p * coxeter_poly(absolute(v))
        out["exact_controls"].append({"n": n, "input_energy": energy(v), "output_energy": energy(reduced),
                                       "mutations": count, "switchable": switchable(reduced),
                                       "absolute_polynomial": str(coxeter_poly(absolute(v)).as_expr()),
                                       "reduced_absolute_polynomial": str(coxeter_poly(absolute(reduced)).as_expr())})
        if n == 5:
            escaped, path, explored = plateau_escape(reduced)
            assert escaped is not None and energy(escaped) == 4
            assert coxeter_poly(escaped) == p and switchable(escaped)
            out["rank_five_trap"] = {"matrix": [list(map(int, reduced.row(i))) for i in range(5)],
                                     "one_move_energy_changes": [[i, inverse, energy(mutate(reduced, i, inverse)) - energy(reduced)]
                                                                 for i in range(4) for inverse in (False, True)],
                                     "escape_path": path, "explored": explored,
                                     "escaped_matrix": [list(map(int, escaped.row(i))) for i in range(5)]}

    seed = lehmer_matrix()
    p = coxeter_poly(seed)
    target = sp.Poly(X**10 + X**9 - X**7 - X**6 - X**5 - X**4 - X**3 + X + 1, X)
    assert p == target
    growth = fixed_lehmer_growth_witness()
    assert coxeter_poly(growth) == target
    # Check the alternate determinant directly at eleven points. Both
    # polynomials are monic of degree ten, so this suffices independently
    # of the inverse/characteristic-polynomial implementation above.
    for z in range(-5, 6):
        assert (z * growth + growth.T).det() == target.eval(z)
    growth_records = []
    for k in range(7):
        assert coxeter_poly(growth) == target
        trace = int((-absolute(growth).inv() * absolute(growth).T).trace())
        assert trace >= energy(growth) - 10
        growth_records.append({"k": k, "energy": energy(growth), "coupling_row": [int(growth[0, 1]), int(growth[0, 2])], "absolute_trace": trace})
        growth = mutate(mutate(growth, 1), 1)
    out["fixed_degree_growth"] = {"matrix": fixed_lehmer_growth_witness().tolist(), "records": growth_records,
                                   "polynomial": str(target.as_expr())}
    rng = random.Random(926104)
    samples = 80
    max_energy = 60
    minima = {}
    for trial in range(samples):
        v = seed.copy()
        moves = []
        for _ in range(24):
            options = [(i, inverse, w) for i in range(9) for inverse in (False, True)
                       for w in [mutate(v, i, inverse)] if energy(w) <= max_energy]
            i, inverse, v = rng.choice(options)
            moves.append([i, inverse])
        reduced, count = reduce_energy(v)
        assert coxeter_poly(reduced) == p
        key = tuple(int(x) for x in reduced)
        if key not in minima:
            minima[key] = {"trial": trial, "energy": energy(reduced), "switchable": switchable(reduced),
                           "max_entry": max(abs(int(x)) for x in reduced), "matrix": [list(map(int, reduced.row(i))) for i in range(10)],
                           "walk": moves, "descent_steps": count}
    out["orbit_sample"] = {"seed": 926104, "samples": samples, "walk_length": 24, "energy_cap": max_energy,
                           "distinct_terminal_matrices": len(minima), "energy_values": sorted({v["energy"] for v in minima.values()}),
                           "nonswitchable_terminal_count": sum(not v["switchable"] for v in minima.values()),
                           "terminals": list(minima.values())}
    path = (_J_OUTPUT / "results.json")
    path.write_text(json.dumps(out, indent=2, default=int) + "\n", encoding="utf-8")
    compact = dict(out)
    compact["orbit_sample"] = {k: v for k, v in out["orbit_sample"].items() if k != "terminals"}
    print(json.dumps(compact, indent=2, default=int))


if __name__ == "__main__":
    main()
