"""Independent exact verifier of the predeclared J104 5-by-4 domain.

Prepared by angular_envelope_review for Yin before the author output is read.
Do not run before root's explicit go and current execution gate.
The mathematical batch has a 300-second cap, including input reads,
certificate comparison, complete-result JSON serialization and output writing.
Any incomplete/failure preservation rewrite is outside that cap and cannot
turn a capped batch into a passed result.
Only the first nonzero sign in each row is normalized during enumeration.
Gram coefficients come from squared minors of B, not author Gram helpers.
Full proper pencils are reconstructed by integer inverse/Newton identities.
All mathematical arithmetic is integral; the timer alone uses a float.
No author or previous project program is imported.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import platform
import time


PROGRAM = Path(__file__).resolve().parent
ROOT = next(p for p in PROGRAM.parents if (p / "repository/config.json").is_file())
OUTPUT = ROOT / "mathematics/computations/outputs" / PROGRAM.name
CAP_SECONDS = 300
CAP_SCOPE = ("input reads, complete mathematical verification and comparison, "
             "complete-result JSON serialization and output writing; any "
             "incomplete/failure rewrite is preservation I/O only")
NR, NC = 5, 4
TARGET = (0, -9, 18, -8, 1)
COL_PAIRS = tuple(combinations(range(NC), 2))
COL_TRIPLES = tuple(combinations(range(NC), 3))
ROW_QUADS = tuple(combinations(range(NR), 4))


class CapExceeded(RuntimeError):
    pass


def det3_values(a, b, c, d, e, f, g, h, i):
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def minor3(a, rows, cols):
    r, s, t = rows
    i, j, k = cols
    x, y, z = a[r], a[s], a[t]
    return det3_values(x[i], x[j], x[k], y[i], y[j], y[k], z[i], z[j], z[k])


def minor4(a, rows):
    r0, r1, r2, r3 = rows
    ans = 0
    for j in range(NC):
        cols = tuple(k for k in range(NC) if k != j)
        ans += (-1 if j % 2 else 1) * a[r0][j] * minor3(a, (r1, r2, r3), cols)
    return ans


def coefficient_e2(a, row_pairs, stop=None):
    ans = 0
    for r, s in row_pairs:
        ar, ass = a[r], a[s]
        for i, j in COL_PAIRS:
            v = ar[i] * ass[j] - ar[j] * ass[i]
            ans += v * v
            if stop is not None and ans > stop:
                return ans
    return ans


def coefficient_e3(a, row_triples, stop=None):
    ans = 0
    for rs in row_triples:
        for cs in COL_TRIPLES:
            v = minor3(a, rs, cs)
            ans += v * v
            if stop is not None and ans > stop:
                return ans
    return ans


def coefficient_e4(a, stop=None):
    ans = 0
    for rs in ROW_QUADS:
        v = minor4(a, rs)
        ans += v * v
        if stop is not None and ans > stop:
            return ans
    return ans


def gram_characteristic(a):
    """Cauchy--Binet: e_k(B^t B) is the sum of squared k-minors of B."""
    rows = tuple(i for i, row in enumerate(a) if any(row))
    e1 = sum(x * x for row in a for x in row)
    e2 = coefficient_e2(a, tuple(combinations(rows, 2)))
    e3 = coefficient_e3(a, tuple(combinations(rows, 3)))
    e4 = coefficient_e4(a)
    return (e4, -e3, e2, -e1, 1)


def flatten(a):
    return tuple(x for row in a for x in row)


def unflatten(values):
    assert len(values) == NR * NC
    return [list(values[NC * i:NC * (i + 1)]) for i in range(NR)]


def canonical_row_column_signs(a):
    """Exhaust the 16 column sign choices, then normalize row first signs.

    This is separate from the author's spanning-forest sign normal form.
    Row/column permutations are deliberately not quotiented.
    """
    candidates = []
    for colsigns in product((-1, 1), repeat=NC):
        out = []
        for row in a:
            changed = [x * s for x, s in zip(row, colsigns)]
            first = next((x for x in changed if x), 1)
            out.extend(changed if first > 0 else [-x for x in changed])
        candidates.append(tuple(out))
    return min(candidates)


def polynomial_multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def polynomial_add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def block_polynomial(char):
    """(t+1) t^4 char(t+t^-1+2), retaining all degree-nine factors."""
    assert len(char) == 5 and char[-1] == 1
    out = [0] * 9
    power = [1]
    for k, coeff in enumerate(char):
        out = polynomial_add(out, [0] * (NC - k) + [coeff * x for x in power])
        power = polynomial_multiply(power, [1, 2, 1])
    out = polynomial_multiply(out, [1, 1])
    assert len(out) == 10 and out[0] == out[-1] == 1 and out == out[::-1]
    return out


def matmul(a, b):
    cols = tuple(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def gram_matrix(a):
    return matmul([list(col) for col in zip(*a)], a)


def proper_matrix(b):
    nr, nc = len(b), len(b[0])
    v = [[int(i == j) for j in range(nr + nc)] for i in range(nr + nc)]
    for i in range(nr):
        for j in range(nc):
            v[i][nr + j] = -b[i][j]
    return v


def signed_cover(v):
    n = len(v)
    w = [[int(i == j) for j in range(2 * n)] for i in range(2 * n)]
    for i in range(n):
        for j in range(i + 1, n):
            entry = v[i][j]
            for sheet in range(2):
                target_sheet = sheet if entry <= 0 else 1 - sheet
                w[2 * i + sheet][2 * j + target_sheet] = -abs(entry)
    return w


def full_pencil_newton(v, check_clock):
    """Complete det(t V+V^t) by the characteristic polynomial of -V^-1 V^t."""
    n = len(v)
    assert all(v[i][i] == 1 and all(x == 0 for x in v[i][:i]) for i in range(n))
    inv = [[int(i == j) for j in range(n)] for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            inv[i][j] = -sum(v[i][k] * inv[k][j] for k in range(i + 1, j + 1))
    a = [[-x for x in row] for row in matmul(inv, [list(c) for c in zip(*v)])]
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    traces, descending = [0], [1]
    for k in range(1, n + 1):
        check_clock()
        power = matmul(power, a)
        traces.append(sum(power[i][i] for i in range(n)))
        numerator = -sum(descending[j] * traces[k - j] for j in range(k))
        assert numerator % k == 0
        descending.append(numerator // k)
    return list(reversed(descending))


class Verification:
    def __init__(self, started):
        self.started = started
        self.stages = Counter()
        self.targets = set()
        self.raw_target_count = 0

    def check_clock(self):
        if time.monotonic() - self.started >= CAP_SECONDS:
            raise CapExceeded("predeclared aggregate 300-second verifier cap")

    def visit(self, support, weights, kind):
        self.stages[kind + "_supports"] += 1
        if self.stages[kind + "_supports"] % 128 == 0:
            self.check_clock()
        occupied_rows = tuple(sorted({p // NC for p in support}))
        occupied_cols = {p % NC for p in support}
        if len(occupied_rows) < 3 or len(occupied_cols) < 3:
            self.stages[kind + "_rank_support_exclusions"] += 1
            return
        pivots = {min(p for p in support if p // NC == r) for r in occupied_rows}
        free = tuple(p for p in support if p not in pivots)
        row_pairs = tuple(combinations(occupied_rows, 2))
        row_triples = tuple(combinations(occupied_rows, 3))
        for signs in product((-1, 1), repeat=len(free)):
            b = [[0] * NC for _ in range(NR)]
            for p, weight in zip(support, weights):
                b[p // NC][p % NC] = weight
            for p, sign in zip(free, signs):
                b[p // NC][p % NC] *= sign
            self.stages[kind + "_row_sign_representatives"] += 1
            if coefficient_e2(b, row_pairs, stop=18) != 18:
                continue
            self.stages[kind + "_e2_matches"] += 1
            if coefficient_e3(b, row_triples, stop=9) != 9:
                continue
            self.stages[kind + "_e3_matches"] += 1
            if coefficient_e4(b, stop=0) != 0:
                continue
            self.stages[kind + "_target_representatives"] += 1
            self.raw_target_count += 1
            assert gram_characteristic(b) == TARGET
            self.targets.add(canonical_row_column_signs(b))

    def enumerate_domain(self):
        for support in combinations(range(NR * NC), 8):
            self.visit(support, (1,) * 8, "eight_units")
        for doubled in range(NR * NC):
            others = tuple(p for p in range(NR * NC) if p != doubled)
            for units in combinations(others, 4):
                support = tuple(sorted((doubled,) + units))
                weights = tuple(2 if p == doubled else 1 for p in support)
                self.visit(support, weights, "one_double")
        assert self.stages["eight_units_supports"] == comb(20, 8)
        assert self.stages["one_double_supports"] == 20 * comb(19, 4)
        self.check_clock()

    def complete_target_records(self):
        records, witnesses, histogram = [], {}, Counter()
        original = block_polynomial(TARGET)
        p4 = [1, -1, -1, -1, 1]
        expected = polynomial_multiply([1, -1, 1], p4)
        for _ in range(3):
            expected = polynomial_multiply(expected, [1, 1])
        assert original == expected
        for flat in sorted(self.targets):
            self.check_clock()
            b = unflatten(flat)
            absolute_b = [[abs(x) for x in row] for row in b]
            absolute_char = gram_characteristic(absolute_b)
            absolute = block_polynomial(absolute_char)
            cover = polynomial_multiply(original, absolute)
            assert len(cover) == 19 and cover[0] == cover[-1] == 1
            equality = absolute_char == TARGET
            histogram[absolute_char] += 1
            records.append({"B": b, "gram_characteristic": list(TARGET),
                            "absolute_gram_characteristic": list(absolute_char),
                            "original": original, "absolute": absolute,
                            "cover_polynomial": cover, "equality": equality})
            if absolute_char not in witnesses:
                v = proper_matrix(b)
                av = proper_matrix(absolute_b)
                w = signed_cover(v)
                actual = [full_pencil_newton(x, self.check_clock) for x in (v, av, w)]
                assert actual == [original, absolute, cover]
                witnesses[absolute_char] = {"B": b, "gram": gram_matrix(b),
                    "absolute_gram": gram_matrix(absolute_b), "V": v,
                    "absolute_V": av, "cover": w, "original": original,
                    "absolute": absolute, "cover_polynomial": cover,
                    "matrix_dimensions": [9, 9, 18], "equality": equality,
                    "pencil_method": "entire integer triangular-inverse/Newton coefficients"}
        return records, witnesses, histogram


def compare_author(author, own_targets, own_histogram, check_clock):
    """Adapt only the declared JSON container names when the author freezes them.

    Target matrices themselves are reconstructed independently here; no stored
    author coefficient, sign normal form or helper is a proof premise.
    """
    assert author["status"] == "complete", "author batch is not complete"
    entries = author["targets"]
    author_keys, author_hist = set(), Counter()
    equality_count = 0
    for entry in entries:
        check_clock()
        assert isinstance(entry, dict), "unexpected frozen author target schema"
        b = entry["B"]
        assert len(b) == NR and all(len(row) == NC for row in b)
        assert all(type(x) is int for row in b for x in row)
        assert sum(x * x for row in b for x in row) == 8
        assert gram_characteristic(b) == TARGET
        key = canonical_row_column_signs(b)
        assert key not in author_keys, "duplicate author row/column sign orbit"
        author_keys.add(key)
        absolute_b = [[abs(x) for x in row] for row in b]
        abs_char = gram_characteristic(absolute_b)
        author_hist[abs_char] += 1
        equality_count += int(abs_char == TARGET)
        checks = {"gram": gram_matrix(b),
                  "gram_characteristic": list(TARGET),
                  "absolute_gram": gram_matrix(absolute_b),
                  "absolute_gram_characteristic": list(abs_char),
                  "original": block_polynomial(TARGET),
                  "absolute": block_polynomial(abs_char),
                  "cover_polynomial": polynomial_multiply(block_polynomial(TARGET), block_polynomial(abs_char)),
                  "equality": abs_char == TARGET}
        for field, wanted in checks.items():
            assert entry[field] == wanted, "author target field mismatch: " + field
    assert author_keys == own_targets, "complete target sign-orbit sets disagree"
    assert author_hist == own_histogram, "complete canonical companion histogram disagrees"
    assert author["target_count"] == len(entries)
    assert author["equality_count"] == equality_count
    reported_hist = Counter()
    for row in author["absolute_gram_histogram"]:
        key = tuple(row["characteristic"])
        assert key not in reported_hist, "duplicate author histogram key"
        reported_hist[key] = row["count"]
    assert reported_hist == author_hist, "author reported companion histogram disagrees"
    return {"all_target_sign_orbits_equal": True, "all_reconstructed_companion_counts_equal": True,
            "all_target_gram_and_full_polynomial_fields_equal": True,
            "reported_counts_and_histogram_equal": True,
            "author_target_representatives": len(entries), "canonical_target_count": len(author_keys)}


def run(author_path, started):
    verification = Verification(started)
    input_paths = (PROGRAM / "readme.md", PROGRAM / "record.md", Path(__file__).resolve(), author_path)
    initial_bytes = {p: p.read_bytes() for p in input_paths}
    author = json.loads(initial_bytes[author_path])
    assert author["status"] == "complete", "requires completed author output and explicit root go"
    try:
        verification.check_clock()
        verification.enumerate_domain()
        records, witnesses, histogram = verification.complete_target_records()
        comparison = compare_author(author, verification.targets, histogram, verification.check_clock)
        verification.check_clock()
        assert all(p.read_bytes() == value for p, value in initial_bytes.items()), "a declared input changed during verification"
        return {"status": "passed", "complete_domain": True,
            "scope": "all integer 5-by-4 energy-eight matrices modulo row/column signs, no permutation quotient",
            "method": "row-first signs; squared B minors; 16 column actions for comparison; full inverse/Newton pencils",
            "python": platform.python_version(), "cap_seconds": CAP_SECONDS, "cap_scope": CAP_SCOPE,
            "stages": dict(verification.stages), "two_double_supports_rejected_by_rank": comb(20, 2),
            "row_normalized_target_count": verification.raw_target_count,
            "canonical_target_count": len(verification.targets),
            "equality_target_count": sum(row["equality"] for row in records),
            "targets": records,
            "absolute_gram_histogram": [{"characteristic": list(key), "count": histogram[key]} for key in sorted(histogram)],
            "distinct_companion_witnesses": [witnesses[key] for key in sorted(witnesses)],
            "author_comparison": comparison, "author_imports": False, "third_party_imports": False,
            "nonblind": "Author output is read as the comparison target; author helpers are neither read by this program nor imported.",
            "shared_implementation_limit": "Both programs use standard Python integer arithmetic; no independent runtime or formal proof is claimed."}
    except (CapExceeded, AssertionError, KeyError, ValueError) as exc:
        return {"status": "incomplete" if isinstance(exc, CapExceeded) else "failed",
            "complete_domain": False, "cap_seconds": CAP_SECONDS, "cap_scope": CAP_SCOPE, "reason": str(exc),
            "stages": dict(verification.stages), "row_normalized_target_count": verification.raw_target_count,
            "partial_canonical_target_count": len(verification.targets),
            "partial_canonical_targets": [unflatten(key) for key in sorted(verification.targets)],
            "no_complete_class_conclusion": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-output", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    result = run(args.author_output.resolve(), started)
    payload = json.dumps(result, indent=2) + "\n"
    if result["status"] == "passed" and time.monotonic() - started >= CAP_SECONDS:
        result["status"] = "incomplete"
        result["complete_domain"] = False
        result["no_complete_class_conclusion"] = True
        result["reason"] = "aggregate 300-second cap exceeded through complete-result serialization"
        payload = json.dumps(result, indent=2) + "\n"
    OUTPUT.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT / "verify_result.json"
    output_path.write_text(payload, encoding="utf-8")
    if result["status"] == "passed" and time.monotonic() - started >= CAP_SECONDS:
        result["status"] = "incomplete"
        result["complete_domain"] = False
        result["no_complete_class_conclusion"] = True
        result["reason"] = "aggregate 300-second cap exceeded through complete-result output writing"
        # Only preservation of an incomplete record may occur after the cap.
        output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "output": str(output_path),
                      "canonical_target_count": result.get("canonical_target_count"),
                      "equality_target_count": result.get("equality_target_count"),
                      "reason": result.get("reason")}, indent=2))
    raise SystemExit(0 if result["status"] == "passed" else 1)


if __name__ == "__main__":
    main()
