"""Complete bounded reverse BFS for the actual quartic first-hit distance.

Original weights (1,2,1)/4; ascending (1,beta,beta^2,beta^3) coordinates.
No independent neutral-radius cutoff.  Default limits: depth 24, 100000
states, 120 seconds.  Incomplete runs publish a separate partial result.
Root isolation and strict-strip sign logic adapt the inspected J33 core.py
method, with integer common-denominator enclosures rather than its phase
coordinate enumeration.  No J33 or older J52 function is imported.
All legal successors must have known distances before a row is certified.
This is author computation; a finite row failure excludes only the stated
unmodified shortest-distance candidate, not arbitrary finite repairs.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from functools import lru_cache
import json
from pathlib import Path
from time import monotonic


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
BETA = (0, 1, 0, 0)
INV = (1, 1, 1, -1)
B = (-2, -1, 0, 1)
S = (-1, -1, 0, 1)
WEIGHTS = {-1: 1, 0: 2, 1: 1}
OUTPUT = Path(__file__).resolve().parents[2] / "outputs" / Path(__file__).resolve().parent.name


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def negate(a):
    return tuple(-x for x in a)


def multiply(a, b):
    c = [0] * 7
    for i in range(4):
        for j in range(4):
            c[i + j] += a[i] * b[j]
    for j in range(6, 3, -1):
        z = c[j]
        for i, coefficient in enumerate((1, -1, -1, -1)):
            c[j - 4 + i] -= z * coefficient
    return tuple(c[:4])


def forward(x, e):
    a, b, c, d = x
    return (-d + e, a + d, b + d, c + d)


def predecessor(y, e):
    a, b, c, d = y
    return (a + b - e, a + c - e, a + d - e, e - a)


def root_polynomial_numerator(n, denominator):
    return (n**4 - n**3 * denominator - n**2 * denominator**2
            - n * denominator**3 + denominator**4)


class StrictCore:
    def __init__(self):
        lo, hi, denominator = 172, 173, 100
        assert root_polynomial_numerator(lo, denominator) < 0
        assert root_polynomial_numerator(hi, denominator) > 0
        # A positive termwise lower bound for P' on the initial interval.
        assert 4 * lo**3 - 3 * hi**2 * denominator - 2 * hi * denominator**2 - denominator**3 > 0
        for _ in range(150):
            middle = lo + hi
            sign = root_polynomial_numerator(middle, 2 * denominator)
            assert sign != 0
            lo, hi = (2 * lo, middle) if sign > 0 else (middle, 2 * hi)
            denominator *= 2
        self.lo, self.hi, self.denominator = lo, hi, denominator
        self.lower_powers = tuple(lo**i * denominator**(3-i) for i in range(4))
        self.upper_powers = tuple(hi**i * denominator**(3-i) for i in range(4))
        powers = [ONE]
        for _ in range(3):
            powers.append(multiply(powers[-1], INV))
        self.sigma_powers = tuple(powers)
        assert multiply(BETA, INV) == ONE
        assert multiply(B, (-1, 1, 0, 0)) == ONE
        assert multiply(BETA, B) == S

    @lru_cache(None)
    def sign(self, x):
        if x == ZERO:
            return 0
        lower = sum(c * (self.lower_powers[i] if c >= 0 else self.upper_powers[i])
                    for i, c in enumerate(x))
        upper = sum(c * (self.upper_powers[i] if c >= 0 else self.lower_powers[i])
                    for i, c in enumerate(x))
        if lower > 0:
            return 1
        if upper < 0:
            return -1
        raise ArithmeticError(f"Unresolved rational sign at {x}")

    def sigma(self, x):
        return tuple(sum(x[i] * self.sigma_powers[i][j] for i in range(4)) for j in range(4))

    @lru_cache(None)
    def allowed(self, x):
        if self.sign(add(B, x)) <= 0 or self.sign(add(B, negate(x))) <= 0:
            return False
        stable = self.sigma(x)
        return self.sign(add(S, stable)) > 0 and self.sign(add(S, negate(stable))) > 0


class StopLimit(RuntimeError):
    pass


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(path.suffix + ".tmp")
    pending.write_text(json.dumps(payload, separators=(",", ":")) + "\n", encoding="utf-8")
    pending.replace(path)


def run(depth, state_cap, seconds):
    started = monotonic()
    def guard():
        if monotonic() - started >= seconds:
            raise StopLimit("time cap reached")
    core = StrictCore()
    distance = {ZERO: 0}
    mass_numerator = {ZERO: 1}
    chosen = {}
    levels = [[ZERO]]
    status, limitation = "complete", None
    completed_depth = 0
    try:
        for step in range(1, depth + 1):
            next_mass = {}
            next_chosen = {}
            for y in levels[-1]:
                guard()
                for e, weight in WEIGHTS.items():
                    x = predecessor(y, e)
                    assert forward(x, e) == y
                    if x in distance or not core.allowed(x):
                        continue
                    if x not in next_mass:
                        if len(distance) + len(next_mass) >= state_cap:
                            raise StopLimit("state cap reached before completing next level")
                        next_mass[x] = 0
                        next_chosen[x] = (e, y)
                    next_mass[x] += weight * mass_numerator[y]
            next_level = sorted(next_mass)
            for x in next_level:
                distance[x] = step
                mass_numerator[x] = next_mass[x]
                chosen[x] = next_chosen[x]
            levels.append(next_level)
            completed_depth = step
            print(json.dumps({"completed_depth": step, "level_size": len(next_level),
                              "states": len(distance)}), flush=True)
        guard()
    except (StopLimit, ArithmeticError) as exc:
        status, limitation = "incomplete", str(exc)

    states = [x for level in levels for x in level]
    index = {x: i for i, x in enumerate(states)}
    rows, patterns = [], {}
    known_row_count, unknown_row_count = 0, 0
    row_analysis_complete = False
    if status == "complete":
        try:
            for x in states[1:]:
                guard()
                successors = []
                complete = True
                coefficients = Counter()
                for e, weight in WEIGHTS.items():
                    y = forward(x, e)
                    legal = core.allowed(y)
                    known = y in distance if legal else False
                    row = {"digit": e, "integer_weight": weight, "state": y, "legal": legal}
                    if legal:
                        row["distance_known"] = known
                        if known:
                            row["distance"] = distance[y]
                            row["id"] = index[y]
                            assert distance[y] >= distance[x] - 1
                            if y != ZERO:
                                coefficients[distance[x] - distance[y]] += weight
                        else:
                            complete = False
                    successors.append(row)
                rows.append({"id": index[x], "all_legal_successor_distances_known": complete,
                             "successors": successors})
                if complete:
                    known_row_count += 1
                    key = tuple(sorted(coefficients.items()))
                    if key not in patterns:
                        patterns[key] = {"count": 0, "witness": x, "id": index[x]}
                    patterns[key]["count"] += 1
                else:
                    unknown_row_count += 1
            row_analysis_complete = True
        except (StopLimit, ArithmeticError) as exc:
            status, limitation = "incomplete", str(exc)

    def word(x):
        result = []
        while x != ZERO:
            e, x = chosen[x]
            result.append(e)
        return result

    records = []
    for x in states:
        item = {"state": x, "distance": distance[x], "shortest_mass_numerator": mass_numerator[x]}
        if x != ZERO:
            e, y = chosen[x]
            item.update({"chosen_digit": e, "chosen_next_id": index[y]})
        records.append(item)
    pattern_records = []
    for coefficients, values in sorted(patterns.items()):
        x = values["witness"]
        pattern_records.append({"coefficients": coefficients, "denominator": 4,
                                "count": values["count"], "witness_id": values["id"],
                                "witness_state": x, "witness_distance": distance[x],
                                "witness_shortest_word": word(x)})
    return {"status": status, "limitation": limitation,
            "scope": {"polynomial_ascending": [1,-1,-1,-1,1], "coordinate_order": "ascending beta powers",
                      "digit_integer_weights": WEIGHTS, "digit_denominator": 4,
                      "requested_depth": depth, "state_cap": state_cap, "seconds_cap": seconds,
                      "neutral_radius_cutoff": None, "root_bisections": 150,
                      "mass_denominator": "4^distance", "raw_row_denominator": 4,
                      "row_policy": "only all-legal-successor-distance-complete rows enter patterns",
                      "root_interval": {"lo": str(core.lo), "hi": str(core.hi), "denominator": str(core.denominator)}},
            "completed_depth": completed_depth, "levels": [[index[x] for x in level] for level in levels],
            "states": records, "rows": rows, "row_analysis_complete": row_analysis_complete,
            "known_rows": known_row_count, "unknown_rows": unknown_row_count, "patterns": pattern_records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=24)
    parser.add_argument("--state-cap", type=int, default=100000)
    parser.add_argument("--seconds", type=float, default=120)
    parser.add_argument("--output", type=Path, default=OUTPUT / "shortest_first_hit_24.json")
    args = parser.parse_args()
    if not 1 <= args.depth <= 24 or not 1 <= args.state_cap <= 100000 or not 0 < args.seconds <= 120:
        parser.error("This bounded program requires depth<=24, states<=100000 and seconds<=120")
    payload = run(args.depth, args.state_cap, args.seconds)
    target = args.output if payload["status"] == "complete" else args.output.with_suffix(".incomplete.json")
    write_json(target, payload)
    print(json.dumps({"status": payload["status"], "completed_depth": payload["completed_depth"],
                      "states": len(payload["states"]), "known_rows": payload["known_rows"],
                      "unknown_rows": payload["unknown_rows"], "patterns": payload["patterns"],
                      "output": str(target), "limitation": payload["limitation"]}), flush=True)
    return 0 if payload["status"] == "complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
