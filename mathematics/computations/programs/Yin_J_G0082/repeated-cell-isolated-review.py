"""Exact C348 review on the original J82 domain, with stdout as the only sink.

Run from the repository root:
  .venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0082/repeated-cell-isolated-review.py

The author worker runs in memory after its mkdir/main/save entrypoints are
disabled. Independent matrix characteristic polynomials and Fraction Sturm
chains then verify the complete result before the retained payload is read.
No search domain or precision is enlarged, and no result file is created.
"""
from __future__ import annotations

import ast
from fractions import Fraction
import json
from math import comb
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True

import sympy as sp

PROGRAM = Path(__file__).resolve().parent
ROOT = next(parent for parent in PROGRAM.parents if (parent / "repository/config.json").is_file())
AUTHOR = PROGRAM / "repeated-cell-author.py"
PAYLOAD = ROOT / "mathematics/computations/outputs" / PROGRAM.name / "repeated-cell-output.json"
T = sp.Symbol("t")
START = time.perf_counter()


def gate():
    if time.perf_counter() - START > 120:
        raise TimeoutError("C348 isolated review exceeded its 120-second checkpoint limit")


def fresh_native():
    source_bytes = AUTHOR.read_bytes()
    tree = ast.parse(source_bytes.decode("utf8"), filename=str(AUTHOR))
    body = []
    removed_mkdir = removed_main = 0
    for node in tree.body:
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Attribute)
                and node.value.func.attr == "mkdir"):
            removed_mkdir += 1
            continue
        if (isinstance(node, ast.If) and isinstance(node.test, ast.Compare)
                and isinstance(node.test.left, ast.Name)
                and node.test.left.id == "__name__"):
            removed_main += 1
            continue
        body.append(node)
    assert removed_mkdir == removed_main == 1
    tree.body = body
    namespace = {"__name__": "c348_isolated_stdout", "__file__": str(AUTHOR)}
    exec(compile(tree, str(AUTHOR), "exec"), namespace)

    def memory_save(path, out):
        namespace["memory_result"] = out

    namespace["save"] = memory_save
    namespace["START"] = time.perf_counter()
    exit_code = namespace["worker"](None)
    result = namespace["memory_result"]
    assert exit_code == 0 and result["status"] == "complete"
    assert result["counts"] == {
        "subsets": 120, "companion_polynomials": 22,
        "pencil_evaluations": 3084, "full_selected_matrices": 12,
    }
    assert AUTHOR.read_bytes() == source_bytes
    return result, source_bytes


def graph(k):
    n = 4 * k + 1
    matrix = sp.eye(n)
    for cell in range(k):
        a, b, c = 3 * cell, 3 * cell + 1, 3 * cell + 2
        right = 3 * cell + 3 if cell + 1 < k else n - 1
        for i, j, value in [(a, b, -1), (a, c, -1), (b, right, -1), (c, right, 1)]:
            matrix[i, j] = value
    path = [0] + list(range(3 * k, 4 * k)) + [n - 1]
    for i, j in zip(path, path[1:]):
        matrix[i, j] = -1
    matrix[0, n - 1] = -1
    return matrix


def basis(k, selected):
    matrix = sp.eye(4 * k + 1)
    for cell in selected:
        a, b, c = 3 * cell, 3 * cell + 1, 3 * cell + 2
        for row in (a, b, c):
            matrix[row, a] = int(row == b)
            matrix[row, b] = int(row == c)
            matrix[row, c] = 1
    return matrix


def absolute(matrix):
    return sp.Matrix(matrix.rows, matrix.cols,
                     lambda i, j: 1 if i == j else -abs(matrix[i, j]))


def cover(matrix):
    n = matrix.rows
    result = sp.eye(2 * n)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i, j]:
                for sheet in (0, 1):
                    result[2 * i + sheet, 2 * j + (sheet if matrix[i, j] < 0 else 1 - sheet)] = -abs(matrix[i, j])
    return result


def pencil_polynomial(matrix):
    return sp.Poly((-matrix.inv() * matrix.T).charpoly(T).as_expr(), T)


def polynomial(coefficients):
    return sp.Poly.from_list(list(reversed(coefficients)), T)


def ascending(poly):
    return [int(poly.nth(i)) for i in range(poly.degree() + 1)]


def check_cost(matrix, k, multiple=1):
    n = matrix.rows
    assert n == multiple * (4 * k + 1) and matrix.det() == 1
    assert all(matrix[i, i] == 1 and all(matrix[i, j] == 0 for j in range(i)) for i in range(n))
    assert max(abs(x) for x in matrix) == 1
    assert sum(matrix[i, j] ** 2 for i in range(n) for j in range(i + 1, n)) == multiple * (5 * k + 2)
    assert sum(x * x for x in matrix) == multiple * (9 * k + 3)


def check_matrices(fresh):
    counts = {"subsets": 0, "pencils": 0, "selected": 0,
              "polynomial_arrays": 0, "factorizations": 0}
    assert [row["k"] for row in fresh["inputs"]] == [3, 4, 5, 6]
    for record in fresh["inputs"]:
        gate()
        k = record["k"]
        n = 4 * k + 1
        original_matrix = graph(k)
        assert original_matrix.tolist() == record["original_matrix"]
        original = pencil_polynomial(original_matrix)
        assert ascending(original) == record["original_coefficients"]
        assert [row["s"] for row in record["companions"]] == list(range(k + 1))
        companions = {row["s"]: polynomial(row["coefficients"]) for row in record["companions"]}
        for row in record["companions"]:
            product = sp.Poly(row["factorization"]["unit"], T)
            for factor in row["factorization"]["factors"]:
                product *= polynomial(factor["coefficients"]) ** factor["multiplicity"]
            assert product == companions[row["s"]]
            counts["factorizations"] += 1
        assert len(record["subsets"]) == 1 << k
        for mask, item in enumerate(record["subsets"]):
            gate()
            selected = [i for i in range(k) if mask >> i & 1]
            assert item["mask"] == mask and item["selected_cells"] == selected
            assert item["companion_s"] == len(selected) and item["det_Q"] == 1
            change = basis(k, selected)
            assert change.tolist() == item["Q"] and change.det() == 1
            matrix = change.T * original_matrix * change
            assert matrix.tolist() == item["X"]
            check_cost(matrix, k)
            negative = absolute(matrix)
            poly = pencil_polynomial(negative)
            assert poly == companions[len(selected)]
            assert item["pencil_nodes"] == list(range(n + 1))
            assert [int(poly.eval(x)) for x in item["pencil_nodes"]] == item["pencil_values"]
            counts["subsets"] += 1
            counts["pencils"] += n + 1
            counts["polynomial_arrays"] += 1
            if len(selected) == k:
                objects = [
                    ("original", matrix, original, 1),
                    ("absolute", negative, poly, 1),
                    ("proper_cover", cover(matrix), original * poly, 2),
                ]
                assert {row["name"] for row in record["all_selected_complete"]} == {row[0] for row in objects}
                for name, full_matrix, full_poly, multiple in objects:
                    stored = next(row for row in record["all_selected_complete"] if row["name"] == name)
                    assert full_matrix.tolist() == stored["matrix"]
                    check_cost(full_matrix, k, multiple)
                    assert pencil_polynomial(full_matrix) == full_poly
                    assert ascending(full_poly) == stored["coefficients"]
                    assert stored["nodes"] == list(range(full_matrix.rows + 1))
                    assert [int(full_poly.eval(x)) for x in stored["nodes"]] == stored["values"]
                    counts["selected"] += 1
                    counts["pencils"] += full_matrix.rows + 1
    assert counts == {"subsets": 120, "pencils": 3084, "selected": 12,
                      "polynomial_arrays": 120, "factorizations": 22}
    return counts


def fraction(record):
    return Fraction(record["numerator"], record["denominator"])


def trim(values):
    values = list(values)
    while len(values) > 1 and not values[-1]:
        values.pop()
    return values


def derivative(values):
    return trim([i * values[i] for i in range(1, len(values))] or [Fraction(0)])


def evaluate(values, x):
    result = Fraction(0)
    for coefficient in reversed(values):
        result = result * x + coefficient
    return result


def divide(a, b):
    a, b = trim(a), trim(b)
    assert any(b)
    quotient = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while any(a) and len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1] / b[-1]
        quotient[shift] = coefficient
        for j, value in enumerate(b):
            a[j + shift] -= coefficient * value
        a = trim(a)
    return trim(quotient), a


def gcd(a, b):
    while any(b):
        _, remainder = divide(a, b)
        a, b = b, remainder
    return [x / a[-1] for x in a]


def sturm(values):
    common = gcd(values, derivative(values))
    squarefree, remainder = divide(values, common)
    assert not any(remainder)
    sequence = [squarefree, derivative(squarefree)]
    while any(sequence[-1]):
        _, remainder = divide(sequence[-2], sequence[-1])
        if not any(remainder):
            break
        sequence.append([-x / abs(remainder[-1]) for x in remainder])
    return sequence, common


def variation(sequence, x=None, side=1):
    signs = []
    for values in sequence:
        value = evaluate(values, x) if x is not None else values[-1] * side ** (len(values) - 1)
        if value:
            signs.append((value > 0) - (value < 0))
    return sum(a != b for a, b in zip(signs, signs[1:]))


COARSE = {
    (3, 0): ("15.92153", "15.92154"), (3, 1): ("7.79516", "7.79517"),
    (3, 2): ("6.56895", "6.56896"), (3, 3): ("6.75877", "6.75878"),
    (4, 0): ("25.77728", "25.77730"), (4, 3): ("49.30795", "49.30796"),
    (5, 4): ("88.58443", "88.58445"), (6, 5): ("117.92208", "117.92209"),
}


def check_roots(fresh):
    counts = {"trace_identities": 0, "intervals": 0, "real_multiplicities": 0,
              "nonreal_cases": 0, "complete_products": 0,
              "comparisons": 0, "decided_comparisons": 0}
    scope = []
    for record in fresh["inputs"]:
        k = record["k"]
        bounds = {}
        for row in record["companions"]:
            gate()
            poly = polynomial(row["coefficients"])
            quotient, remainder = sp.div(poly, sp.Poly(T + 1, T))
            assert remainder.is_zero
            h = quotient.degree() // 2
            remaining = quotient.as_expr()
            coefficients = [0] * (h + 1)
            for j in range(h, -1, -1):
                coefficients[j] = int(sp.Poly(remaining, T).nth(h + j))
                binomial_basis = sum(comb(j, a) * T ** (h + j - 2 * a) for a in range(j + 1))
                remaining = sp.expand(remaining - coefficients[j] * binomial_basis)
            assert remaining == 0
            certificate = row["root_certificate"]
            assert coefficients == certificate["trace_coefficients"] and h == certificate["trace_degree"]
            values = [Fraction(v) for v in coefficients]
            layers = []
            while len(values) > 1:
                sequence, common = sturm(values)
                layers.append(sequence)
                values = common
            real_count = sum(variation(sequence, side=-1) - variation(sequence, side=1) for sequence in layers)
            assert real_count == certificate["real_root_count"]
            lower = upper = Fraction(1)
            covered = True
            previous = None
            for interval in certificate["real_intervals"]:
                a, b = fraction(interval["lower"]), fraction(interval["upper"])
                multiplicity = interval["multiplicity"]
                assert a <= b and b - a <= Fraction(1, 1 << 24)
                assert previous is None or previous < a
                previous = b
                if a == b:
                    count = sum(evaluate(sequence[0], a) == 0 for sequence in layers)
                else:
                    assert all(evaluate(sequence[0], a) != 0 and evaluate(sequence[0], b) != 0 for sequence in layers)
                    count = sum(variation(sequence, a) - variation(sequence, b) for sequence in layers)
                assert count == multiplicity
                if -2 <= a <= b <= 2:
                    kind = "unit-circle"
                elif a > 2 or b < -2:
                    kind = "exterior-pair"
                    x, y = (a, b) if a > 2 else (-b, -a)
                    lo, hi = fraction(interval["outer_lower"]), fraction(interval["outer_upper"])
                    sqrt_lower, sqrt_upper = 2 * lo - x, 2 * hi - y
                    assert sqrt_lower >= 0 and sqrt_upper >= 0
                    assert sqrt_lower ** 2 <= x * x - 4 and sqrt_upper ** 2 >= y * y - 4
                    assert 1 < lo <= hi
                    lower *= lo ** multiplicity
                    upper *= hi ** multiplicity
                else:
                    kind = "boundary-undecided"
                    covered = False
                assert kind == interval["type"]
                counts["intervals"] += 1
                counts["real_multiplicities"] += multiplicity
            assert sum(item["multiplicity"] for item in certificate["real_intervals"]) == real_count
            complete = covered and real_count == h
            assert complete == certificate["complete_mahler_product_certified"]
            assert (real_count == h) == certificate["all_trace_roots_real"]
            if complete:
                assert lower == fraction(certificate["mahler_product_bounds"]["lower"])
                assert upper == fraction(certificate["mahler_product_bounds"]["upper"])
                coarse_lower, coarse_upper = map(Fraction, COARSE[(k, row["s"])])
                assert coarse_lower < lower <= upper < coarse_upper
                bounds[row["s"]] = (lower, upper)
                counts["complete_products"] += 1
            else:
                assert h - real_count == 2
                counts["nonreal_cases"] += 1
            counts["trace_identities"] += 1
            scope.append([k, row["s"], h, real_count, complete])
        for comparison in record["pairwise_measure_comparisons"]:
            a, b = comparison["s_first"], comparison["s_second"]
            decision = "undecided"
            if a in bounds and b in bounds:
                if bounds[a][1] < bounds[b][0]:
                    decision = "first-strictly-smaller"
                elif bounds[b][1] < bounds[a][0]:
                    decision = "second-strictly-smaller"
            assert decision == comparison["decision"]
            counts["comparisons"] += 1
            counts["decided_comparisons"] += decision != "undecided"
    assert counts == {"trace_identities": 22, "intervals": 149, "real_multiplicities": 180,
                      "nonreal_cases": 14, "complete_products": 8,
                      "comparisons": 52, "decided_comparisons": 7}
    return counts, scope


def compare_payload(a, b, counts, path="$"):
    assert type(a) is type(b), (path, type(a), type(b))
    if isinstance(a, dict):
        counts["dicts"] += 1
        assert a.keys() == b.keys(), (path, a.keys(), b.keys())
        for key in a:
            compare_payload(a[key], b[key], counts, path + "." + key)
    elif isinstance(a, list):
        counts["lists"] += 1
        assert len(a) == len(b), (path, len(a), len(b))
        for i, (x, y) in enumerate(zip(a, b)):
            compare_payload(x, y, counts, path + "[" + str(i) + "]")
    else:
        counts["scalars"] += 1
        assert a == b, (path, a, b)


def main():
    fresh, source_bytes = fresh_native()
    matrix_counts = check_matrices(fresh)
    root_counts, root_scope = check_roots(fresh)
    # Historical results are consulted only after the independent reconstruction.
    payload_bytes = PAYLOAD.read_bytes()
    retained = json.loads(payload_bytes)
    supervisor_keys = {"outer_deadline_triggered", "worker_returncode"}
    assert retained.keys() == fresh.keys() | supervisor_keys
    mathematical_payload = {key: value for key, value in retained.items() if key not in supervisor_keys}
    counts = {"scalars": 0, "dicts": 0, "lists": 0}
    compare_payload(fresh, mathematical_payload, counts)
    assert counts == {"scalars": 141082, "dicts": 967, "lists": 6491}
    assert AUTHOR.read_bytes() == source_bytes and PAYLOAD.read_bytes() == payload_bytes
    gate()
    report = {
        "status": "pass", "domain_k": [3, 4, 5, 6], "matrix_checks": matrix_counts,
        "rational_sturm_and_squared_bounds": root_counts, "root_scope": root_scope,
        "fresh_vs_retained_math_payload": counts,
        "excluded_historical_supervisor_fields": sorted(supervisor_keys),
        "python": sys.version.split()[0], "sympy": sp.__version__,
        "elapsed_seconds": time.perf_counter() - START,
    }
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

