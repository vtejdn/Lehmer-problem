"""One fixed exact Macaulay attempt on three prescribed width-five lifts."""

from fractions import Fraction as Q
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import itertools
import json
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'main.py').parent
OUTPUT = (_J_OUTPUT / 'data.json')
P = [1, -2, 1, -2, 1]
UP = [2, 0, 2, -1]
UM = [2, 0, 1, -1]
ZERO = (0, 0, 0, 0)
DEGREE = 4
CAP_SECONDS = 60


# Diagnostics retain logical program/module suffixes and their actual failure.
def _record_text(value):
    from pathlib import Path
    import sys
    checkout = _J_ROOT
    contexts = [(checkout, '.'), (Path(sys.executable), 'python')]
    for entry in sys.path:
        path = Path(entry)
        if entry and path.is_absolute():
            try:
                label = path.resolve().relative_to(checkout).as_posix()
            except ValueError:
                label = '<runtime>'
            contexts.append((path, label))
    for path, label in sorted(contexts, key=lambda pair: len(str(pair[0])), reverse=True):
        for spelling in (str(path), path.as_posix()):
            value = value.replace(spelling, label)
    return value


def save(report):
    pending = OUTPUT.with_name("data.pending.json")
    pending.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT)


def term(x):
    return {} if not x else {ZERO: Q(x)}


def plus(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Q(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(a, c):
    return {e: v * c for e, v in a.items() if v * c}


def times(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            k = tuple(x + y for x, y in zip(e, f))
            out[k] = out.get(k, Q(0)) + c * d
    return {e: c for e, c in out.items() if c}


def encode_q(x):
    x = Q(x)
    return {"numerator": x.numerator, "denominator": x.denominator}


def encode_poly(p):
    return [{"exponents": list(e), "coefficient": encode_q(c)}
            for e, c in sorted(p.items(), key=lambda z: (sum(z[0]), z[0]))]


def monomials(n):
    return sorted((e for e in itertools.product(range(n + 1), repeat=4)
                   if sum(e) <= n), key=lambda e: (sum(e), e))


def remainder(p):
    out = list(p)
    while len(out) >= len(P):
        c = out[-1]
        offset = len(out) - len(P)
        for j, a in enumerate(P):
            out[offset + j] -= c * a
        while out and not out[-1]:
            out.pop()
    return out + [0] * (4 - len(out))


def lifted(seed, first, second):
    coeff = [term(seed[j] if j < len(seed) else 0) for j in range(6)]
    e = tuple(1 if j == first else 0 for j in range(4))
    f = tuple(1 if j == second else 0 for j in range(4))
    for j, a in enumerate(P):
        coeff[j] = plus(coeff[j], {e: Q(a)})
        coeff[j + 1] = plus(coeff[j + 1], {f: Q(a)})
    return coeff


def equations(f, g):
    out = []
    for lag in range(6):
        p = term(-1 if lag == 0 else 0)
        for j in range(6 - lag):
            p = plus(p, times(f[j], f[j + lag]))
            p = plus(p, scale(times(g[j], g[j + lag]), 2))
        out.append(p)
    return out


def gauss(matrix, rhs, deadline):
    m, n = len(matrix), len(matrix[0])
    work = [[Q(a) for a in row] + [Q(b)] for row, b in zip(matrix, rhs)]
    transform = [[Q(i == j) for j in range(m)] for i in range(m)]
    pivots = []
    for col in range(n):
        if time.monotonic() >= deadline:
            raise TimeoutError("Declared aggregate exact-worker deadline reached")
        rank = len(pivots)
        pivot = next((r for r in range(rank, m) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        transform[rank], transform[pivot] = transform[pivot], transform[rank]
        divisor = work[rank][col]
        work[rank] = [x / divisor for x in work[rank]]
        transform[rank] = [x / divisor for x in transform[rank]]
        for r in range(m):
            if r == rank or not work[r][col]:
                continue
            c = work[r][col]
            work[r] = [x - c * y for x, y in zip(work[r], work[rank])]
            transform[r] = [x - c * y for x, y in zip(transform[r], transform[rank])]
        pivots.append(col)
        if len(pivots) == m:
            break
    for r in range(m):
        if not any(work[r][:-1]) and work[r][-1]:
            witness = [x / work[r][-1] for x in transform[r]]
            assert all(sum(witness[i] * matrix[i][j] for i in range(m)) == 0
                       for j in range(n))
            assert sum(witness[i] * rhs[i] for i in range(m)) == 1
            return {"consistent": False, "rank": len(pivots),
                    "augmented_rank": len(pivots) + 1, "pivots": pivots,
                    "left_null_witness": witness}
    solution = [Q(0)] * n
    for r, col in enumerate(pivots):
        solution[col] = work[r][-1]
    assert all(sum(a * x for a, x in zip(row, solution)) == b
               for row, b in zip(matrix, rhs))
    return {"consistent": True, "rank": len(pivots), "augmented_rank": len(pivots),
            "pivots": pivots, "free_variables_set_to_zero": [j for j in range(n) if j not in pivots],
            "solution": solution}


def build_case(kg):
    seed_f = remainder([0, 0] + UP)
    seed_g = remainder([0] * kg + UM)
    assert seed_f == [0, 1, 0, 1]
    assert seed_g == {2: [1, -1, 1, -1], 3: [1, -1, 0, -1],
                      4: [1, -1, 0, -2]}[kg]
    f, g = lifted(seed_f, 0, 1), lifted(seed_g, 2, 3)
    eq = equations(f, g)
    rows = monomials(DEGREE)
    row_index = {e: i for i, e in enumerate(rows)}
    columns = []
    degrees = []
    for lag, p in enumerate(eq):
        degree = max((sum(e) for e in p), default=-1)
        degrees.append(degree)
        if degree < 0:
            continue
        for e in monomials(DEGREE - degree):
            columns.append((lag, e))
    matrix = [[0] * len(columns) for _ in rows]
    for col, (lag, e) in enumerate(columns):
        for fexp, value in eq[lag].items():
            index = tuple(a + b for a, b in zip(e, fexp))
            assert sum(index) <= DEGREE and value.denominator == 1
            matrix[row_index[index]][col] += value.numerator
    rhs = [int(e == ZERO) for e in rows]
    record = {"k_f": 2, "k_g": kg, "width_bound": 5,
              "source_unit_plus": UP, "source_unit_minus": UM,
              "reduced_f_seed": seed_f, "reduced_g_seed": seed_g,
              "f_coefficients": [encode_poly(p) for p in f],
              "g_coefficients": [encode_poly(p) for p in g],
              "original_lag_equations": [encode_poly(p) for p in eq],
              "equation_degrees": degrees, "variables": ["a", "b", "c", "d"],
              "macaulay_product_degree_bound": DEGREE,
              "row_monomials": [list(e) for e in rows],
              "multiplier_columns": [{"lag": i, "exponents": list(e)} for i, e in columns],
              "matrix": matrix, "rhs": rhs, "rows": len(rows), "columns": len(columns),
              "stage": "exact-system-built"}
    return record, eq, columns


def worker():
    start = time.monotonic()
    deadline = start + CAP_SECONDS
    report = json.loads(OUTPUT.read_text(encoding="utf-8"))
    save(report)
    current = None
    try:
        for kg in (2, 3, 4):
            current, eq, columns = build_case(kg)
            report["cases"].append(current)
            save(report)
            result = gauss(current["matrix"], current["rhs"], deadline)
            current["rank"] = result["rank"]
            current["augmented_rank"] = result["augmented_rank"]
            current["pivot_columns"] = result["pivots"]
            if result["consistent"]:
                h = [{} for _ in eq]
                for value, (lag, exp) in zip(result["solution"], columns):
                    if value:
                        h[lag][exp] = value
                combo = {}
                for p, multiplier in zip(eq, h):
                    combo = plus(combo, times(p, multiplier))
                assert combo == term(1)
                current.update({"outcome": "exact-unit-ideal-certificate",
                                "multipliers": [encode_poly(p) for p in h],
                                "direct_identity": encode_poly(combo),
                                "solution": [encode_q(x) for x in result["solution"]],
                                "free_variables_set_to_zero": result["free_variables_set_to_zero"],
                                "certificate_checks": "full matrix solution and direct polynomial identity both exact"})
            else:
                current.update({"outcome": "no-certificate-in-declared-macaulay-domain",
                                "left_null_witness": [encode_q(x) for x in result["left_null_witness"]],
                                "certificate_checks": "witness times full matrix is zero and witness times rhs is one",
                                "nonlinear_feasibility": "unresolved"})
            current["stage"] = "complete-declared-attempt"
            save(report)
        report["result"] = "all three declared exact attempts completed"
        exit_code = 0
    except BaseException as exc:
        report["result"] = "native failure; remaining stages not run"
        report["failure"] = {"type": type(exc).__name__, "message": _record_text(str(exc)),
                             "traceback": _record_text(traceback.format_exc())}
        if current is not None:
            current["stage"] = "failed-after-" + current["stage"]
        exit_code = 1
    pass
    save(report)
    return exit_code


def main():
    start = time.monotonic()
    report = {'arithmetic': 'integers and fractions.Fraction only', 'original_P_ascending': P, 'scope': {'k_f': 2, 'k_g': [2, 3, 4], 'width': 5, 'macaulay_product_degree': DEGREE, 'retry': False, 'random_seed': None, 'floating_point': False}, 'cases': [], 'result': 'worker not yet started'}
    save(report)
    child = subprocess.Popen([sys.executable, str((_J_PROGRAM / 'main.py')), "--worker"],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    timeout = False
    try:
        stdout, stderr = child.communicate(timeout=CAP_SECONDS)
    except subprocess.TimeoutExpired:
        timeout = True
        child.kill()
        stdout, stderr = child.communicate()
    report = json.loads(OUTPUT.read_text(encoding="utf-8"))
    pass
    report["worker_exit_code"] = child.returncode
    report["outer_timeout"] = timeout
    if timeout:
        report["result"] = "outer timeout; all unfinished stages remain incomplete"
    if child.returncode and stdout:
        report["worker_stdout"] = stdout
    if child.returncode and stderr:
        report["worker_stderr"] = stderr
    save(report)
    print(json.dumps({"output": str(OUTPUT), "result": report["result"],
                      "outer_timeout": timeout, "worker_exit_code": child.returncode,
                      "cases": [{"k_g": c["k_g"], "stage": c["stage"],
                                 "outcome": c.get("outcome"), "rank": c.get("rank"),
                                 "rows": c["rows"], "columns": c["columns"]}
                                for c in report["cases"]]}, indent=2))
    return 1 if timeout or child.returncode else 0


if __name__ == "__main__":
    raise SystemExit(worker() if sys.argv[1:] == ["--worker"] else main())
