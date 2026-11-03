"""Exact original-weight carry graphs; default entry enforces the declared caps.

The --worker entry is internal to the Windows Job Object launcher.
No author helper is an independent verification oracle.
"""
from __future__ import annotations

import ctypes
from ctypes import wintypes
from fractions import Fraction as F
from itertools import product
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OUT = REPO / "mathematics" / "computations" / "outputs" / HERE.name / "author"
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
CAP_SECONDS = 60
CAP_MEMORY = 512 * 1024 * 1024
CAP_OUTPUT = 64 * 1024 * 1024
RESERVE = 64 * 1024


class CapStop(RuntimeError):
    pass


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def beta(a):
    a0, a1, a2, a3 = a
    return (-a3, a0 + a3, a1 + a3, a2 + a3)


def beta_inv(a):
    a0, a1, a2, a3 = a
    return (a0 + a1, a0 + a2, a0 + a3, -a0)


def shift(a, power):
    fn = beta if power >= 0 else beta_inv
    for _ in range(abs(power)):
        a = fn(a)
    return a


def j_map(a):
    result, p = [0] * 4, ONE
    for coefficient in a:
        for i in range(4):
            result[i] += coefficient * p[i]
        p = beta_inv(p)
    return beta_inv(tuple(result))


def phi(a):
    s = [sum(a[j] * a[j + l] for j in range(4 - l)) for l in range(4)]
    return (s[0] + s[2] + 3 * s[3], s[1] + s[2] + s[3])


def pair_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def pair_scale(a, c):
    return (a[0] * c, a[1] * c)


def pair_mul(a, b):
    return (a[0] * b[0] + 3 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def pair_div(a, b):
    norm = b[0] * (b[0] + b[1]) - 3 * b[1] * b[1]
    if not norm:
        raise ZeroDivisionError("zero quadratic-field divisor")
    return pair_scale(pair_mul(a, (b[0] + b[1], -b[1])), F(1) / norm)


def pair_sign(a):
    p, q = F(a[0]) + F(a[1], 2), -F(a[1], 2)
    if not q:
        return (p > 0) - (p < 0)
    if not p:
        return (q > 0) - (q < 0)
    if (p > 0) == (q > 0):
        return 1 if p > 0 else -1
    v = p * p - 13 * q * q
    return ((v > 0) - (v < 0)) * (1 if p > 0 else -1)


def rat(x):
    x = F(x)
    return [x.numerator, x.denominator]


def encode_pair(x):
    return [rat(x[0]), rat(x[1])]


class Budget:
    def __init__(self):
        self.start = time.monotonic()
        self.completed = []
        self.lookups = 0

    def check(self):
        if time.monotonic() - self.start >= CAP_SECONDS:
            raise CapStop("worker wall-clock cap")

    def write(self, name, value):
        """Atomic output with a byte cap that includes the current temporary file."""
        self.check()
        target = OUT / name
        temporary = OUT / (name + ".partial")
        baseline = sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
        total = baseline
        try:
            with temporary.open("wb") as stream:
                encoder = json.JSONEncoder(separators=(",", ":"), ensure_ascii=True)
                for index, chunk in enumerate(encoder.iterencode(value)):
                    raw = chunk.encode("ascii")
                    if total + len(raw) > CAP_OUTPUT - RESERVE:
                        raise CapStop("author native-output cap")
                    stream.write(raw)
                    total += len(raw)
                    if index % 4096 == 0:
                        self.check()
                if total + 1 > CAP_OUTPUT - RESERVE:
                    raise CapStop("author native-output cap")
                stream.write(b"\n")
            os.replace(temporary, target)
        finally:
            if temporary.exists():
                temporary.unlink()


def count_tables(budget):
    tables = [{ZERO: 1}]
    power = ONE
    for length in range(1, 11):
        previous, current = tables[-1], {}
        for index, (a, weight) in enumerate(previous.items()):
            for digit, digit_weight in ((-1, 1), (0, 2), (1, 1)):
                endpoint = tuple(a[i] + digit * power[i] for i in range(4))
                current[endpoint] = current.get(endpoint, 0) + digit_weight * weight
            if index % 128 == 0:
                budget.check()
        assert sum(current.values()) == 4 ** length
        assert all(current.get(neg(a)) == w for a, w in current.items())
        tables.append(current)
        power = beta(power)
    return tables


def case(n, tables, budget):
    k = n - 2
    counts = tables[k]
    middle = [(theta, 2 ** theta.count(0)) for theta in product((-1, 0, 1), repeat=4)]
    temporary_edges = []
    row_mass, col_mass = {}, {}
    for index, (a, wa) in enumerate(sorted(counts.items())):
        x = shift(a, -k)
        for theta, wt in middle:
            budget.lookups += 1
            c = neg(shift(add(x, theta), -4))
            wc = counts.get(c)
            if wc is None:
                continue
            weight = wa * wc * wt
            y = neg(shift(add(x, (theta[0], theta[1], 0, 0)), -2))
            temporary_edges.append((a, c, weight, y, theta))
            row_mass[a] = row_mass.get(a, 0) + weight
            col_mass[c] = col_mass.get(c, 0) + weight
        if index % 32 == 0:
            budget.check()
    left, right = sorted(row_mass), sorted(col_mass)
    li, ri = {a: i for i, a in enumerate(left)}, {a: i for i, a in enumerate(right)}
    edges = [[li[a], ri[c], w, *y, *theta] for a, c, w, y, theta in temporary_edges]
    del temporary_edges
    edges.sort(key=lambda e: (e[0], e[1]))
    assert len({(e[0], e[1]) for e in edges}) == len(edges)
    rm, cm = [row_mass[a] for a in left], [col_mass[c] for c in right]
    parent = list(range(len(left) + len(right)))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(v, w):
        v, w = find(v), find(w)
        if v != w:
            parent[max(v, w)] = min(v, w)

    row_marks = [[0] * 4 for _ in left]
    col_marks = [[0] * 4 for _ in right]
    row_degree, col_degree = [0] * len(left), [0] * len(right)
    mark_sum = [0, 0]
    total = 0
    for index, e in enumerate(edges):
        i, j, w = e[:3]
        y = e[3:7]
        union(i, len(left) + j)
        total += w
        row_degree[i] += 1
        col_degree[j] += 1
        for z in range(4):
            row_marks[i][z] += w * y[z]
            col_marks[j][z] += w * y[z]
        q = phi(y)
        mark_sum[0] += w * q[0]
        mark_sum[1] += w * q[1]
        if index % 128 == 0:
            budget.check()
    assert max(row_degree) <= 81 and max(col_degree) <= 81
    assert total == sum(rm) == sum(cm)
    assert all(sum(row[z] for row in row_marks) == 0 for z in range(4))
    moment = pair_scale(mark_sum, F(1, total))
    removed = (F(0), F(0))
    for masses, marks in ((rm, row_marks), (cm, col_marks)):
        for index, (mass, mark) in enumerate(zip(masses, marks)):
            removed = pair_add(removed, pair_scale(phi(mark), F(1, mass)))
            if index % 32 == 0:
                budget.check()
    energy = pair_add(moment, pair_scale(removed, F(-1, 2 * total)))
    assert pair_sign(moment) > 0
    assert pair_sign(energy) >= 0
    assert pair_sign(pair_add(moment, pair_scale(energy, -1))) >= 0
    assert pair_sign(pair_add((4, 0), pair_scale(energy, -1))) >= 0
    half_total, half_mark = 0, [0, 0]
    for index, (a, wa) in enumerate(tables[n].items()):
        weight = wa * tables[n].get(j_map(a), 0)
        half_total += weight
        q = phi(a)
        half_mark[0] += weight * q[0]
        half_mark[1] += weight * q[1]
        if index % 128 == 0:
            budget.check()
    assert half_total == total and half_mark == mark_sum
    groups = {}
    for index, e in enumerate(edges):
        groups.setdefault(find(e[0]), []).append(index)
    components = []
    for edge_ids in groups.values():
        lset, rset, mass, mean_numerator, second = set(), set(), 0, [0] * 4, [0, 0]
        for eidx in edge_ids:
            e = edges[eidx]
            i, j, w = e[:3]
            y = e[3:7]
            lset.add(i)
            rset.add(j)
            mass += w
            for z in range(4):
                mean_numerator[z] += w * y[z]
            q = phi(y)
            second[0] += w * q[0]
            second[1] += w * q[1]
        mean = [F(v, mass) for v in mean_numerator]
        components.append({
            "left": sorted(lset), "right": sorted(rset), "edges": edge_ids,
            "mass_integer": mass, "probability": rat(F(mass, total)),
            "mean_beta": [rat(v) for v in mean],
            "mean_square_pair": encode_pair(phi(mean)),
            "second_moment_pair": encode_pair(pair_scale(second, F(1, mass))),
        })
        budget.check()
    components.sort(key=lambda c: c["left"])
    return {
        "schema": "g106-case-v1", "n": n, "N": 2 * n, "b": 2, "k": k,
        "left": [list(a) for a in left], "right": [list(c) for c in right],
        "row_mass": rm, "column_mass": cm,
        "row_mark_sum_beta": row_marks, "column_mark_sum_beta": col_marks,
        "edges": edges, "components": components,
        "S": total, "moment_numerator_pair": mark_sum,
        "m_pair": encode_pair(moment), "D_pair": encode_pair(energy),
        "rayleigh_upper_pair": encode_pair(pair_div(energy, moment)),
        "half_word_S": half_total, "half_word_moment_numerator_pair": half_mark,
        "checks": {"complete_half_word_agreement": True, "energy_between_zero_and_four": True,
                   "energy_at_most_moment": True, "centered_midpoint": True,
                   "maximum_left_degree": max(row_degree), "maximum_right_degree": max(col_degree)},
    }


def worker():
    if sys.stdin.readline().strip() != "JOB_READY":
        raise RuntimeError("worker requires the guarded launcher")
    budget = Budget()
    inputs = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    expected = {"schema": "g106-input-v1", "polynomial_ascending": [1, -1, -1, -1, 1],
                "digits": [-1, 0, 1], "integer_digit_weights": [1, 2, 1],
                "n_values": list(range(5, 11)), "b": 2, "wall_seconds": CAP_SECONDS,
                "worker_memory_bytes": CAP_MEMORY, "author_output_bytes": CAP_OUTPUT}
    if inputs != expected:
        raise RuntimeError("input differs from the declared six-case scope")
    OUT.mkdir(parents=True, exist_ok=True)
    try:
        tables = count_tables(budget)
        budget.write("counts.json", {"schema": "g106-counts-v1", "tables": {
            str(l): [[*a, w] for a, w in sorted(table.items())]
            for l, table in enumerate(tables)}})
        for n in inputs["n_values"]:
            result = case(n, tables, budget)
            budget.write(f"case_n{n:02}.json", result)
            budget.completed.append(n)
            budget.write("results.json", {"status": "partial", "completed_n": budget.completed,
                                           "candidate_edge_lookups": budget.lookups})
        assert budget.lookups <= 796068
        budget.write("results.json", {"status": "complete", "completed_n": budget.completed,
                                       "candidate_edge_lookups": budget.lookups,
                                       "scope": inputs, "arithmetic": "exact integers and rational Q(u) pairs"})
        print(json.dumps({"status": "complete", "completed_n": budget.completed}))
        return 0
    except (CapStop, MemoryError) as exc:
        print(json.dumps({"status": "stopped", "reason": type(exc).__name__ + ": " + str(exc),
                          "completed_n": budget.completed}))
        return 2


def make_job():
    """Hard worker commit/job-memory and working-set limits; fail closed."""
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    class Basic(ctypes.Structure):
        _fields_ = [("process_time", ctypes.c_longlong), ("job_time", ctypes.c_longlong),
                    ("flags", wintypes.DWORD), ("min_ws", ctypes.c_size_t), ("max_ws", ctypes.c_size_t),
                    ("active", wintypes.DWORD), ("affinity", ctypes.c_size_t),
                    ("priority", wintypes.DWORD), ("scheduling", wintypes.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(name, ctypes.c_ulonglong) for name in
                    ("read_ops", "write_ops", "other_ops", "read_bytes", "write_bytes", "other_bytes")]
    class Extended(ctypes.Structure):
        _fields_ = [("basic", Basic), ("io", IO), ("process_memory", ctypes.c_size_t),
                    ("job_memory", ctypes.c_size_t), ("peak_process", ctypes.c_size_t),
                    ("peak_job", ctypes.c_size_t)]
    kernel.CreateJobObjectW.argtypes = (ctypes.c_void_p, wintypes.LPCWSTR)
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = (wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD)
    kernel.AssignProcessToJobObject.argtypes = (wintypes.HANDLE, wintypes.HANDLE)
    kernel.SetProcessWorkingSetSizeEx.argtypes = (wintypes.HANDLE, ctypes.c_size_t,
                                                  ctypes.c_size_t, wintypes.DWORD)
    kernel.GetProcessWorkingSetSizeEx.argtypes = (wintypes.HANDLE, ctypes.c_void_p,
                                                  ctypes.c_void_p, ctypes.c_void_p)
    kernel.TerminateJobObject.argtypes = (wintypes.HANDLE, wintypes.UINT)
    kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
    kernel.QueryInformationJobObject.argtypes = (wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p,
                                                 wintypes.DWORD, ctypes.c_void_p)
    handle = kernel.CreateJobObjectW(None, None)
    if not handle:
        raise ctypes.WinError(ctypes.get_last_error())
    limits = Extended()
    limits.basic.flags = 0x100 | 0x200 | 0x2000
    limits.basic.min_ws, limits.basic.max_ws = 1024 * 1024, CAP_MEMORY
    limits.process_memory = limits.job_memory = CAP_MEMORY
    if not kernel.SetInformationJobObject(handle, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        kernel.CloseHandle(handle)
        raise ctypes.WinError(ctypes.get_last_error())
    return kernel, handle, limits


def launch():
    if os.name != "nt":
        raise RuntimeError("the declared hard-memory launcher requires Windows")
    if OUT.exists() and any(OUT.iterdir()):
        raise RuntimeError("author output already exists; do not overwrite a prior run implicitly")
    kernel, job, limits = make_job()
    start = time.monotonic()
    process = None
    try:
        process = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--worker"],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        if not kernel.AssignProcessToJobObject(job, wintypes.HANDLE(process._handle)):
            process.kill()
            raise ctypes.WinError(ctypes.get_last_error())
        child_handle = wintypes.HANDLE(process._handle)
        if not kernel.SetProcessWorkingSetSizeEx(child_handle, 1024 * 1024, CAP_MEMORY, 0x2 | 0x4):
            raise ctypes.WinError(ctypes.get_last_error())
        minimum, maximum, flags = ctypes.c_size_t(), ctypes.c_size_t(), wintypes.DWORD()
        if not kernel.GetProcessWorkingSetSizeEx(child_handle, ctypes.byref(minimum),
                                                ctypes.byref(maximum), ctypes.byref(flags)):
            raise ctypes.WinError(ctypes.get_last_error())
        if maximum.value > CAP_MEMORY or not flags.value & 0x4:
            raise RuntimeError("worker hard working-set limit was not confirmed")
        try:
            stdout, stderr = process.communicate("JOB_READY\n", timeout=max(0.001, CAP_SECONDS - (time.monotonic() - start)))
            status = "complete" if process.returncode == 0 else "failed_or_stopped"
        except subprocess.TimeoutExpired:
            kernel.TerminateJobObject(job, 3)
            stdout, stderr = process.communicate(timeout=5)
            status = "wall_time_stop"
        queried = bool(kernel.QueryInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits), None))
        result = {"status": status, "returncode": process.returncode,
                  "wall_seconds": time.monotonic() - start,
                  "worker_job_memory_cap_bytes": CAP_MEMORY, "worker_working_set_cap_bytes": CAP_MEMORY,
                  "peak_worker_commit_bytes": limits.peak_process if queried else None,
                  "peak_job_commit_bytes": limits.peak_job if queried else None,
                  "author_stdout": stdout, "author_stderr": stderr,
                  "completed_case_files": sorted(p.name for p in OUT.glob("case_n*.json")),
                  "parent_monitor_excluded_from_worker_memory_limit": True}
        OUT.mkdir(parents=True, exist_ok=True)
        payload = (json.dumps(result, indent=2) + "\n").encode("utf-8")
        used = sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
        if used + len(payload) > CAP_OUTPUT:
            raise RuntimeError("reserved execution-status output would exceed cap")
        (OUT / "execution.json").write_bytes(payload)
        print(json.dumps(result, indent=2))
        return 0 if status == "complete" else 2
    finally:
        if process is not None and process.poll() is None:
            kernel.TerminateJobObject(job, 4)
            process.wait(timeout=5)
        kernel.CloseHandle(job)


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["--worker"]:
            raise SystemExit(worker())
        if sys.argv[1:]:
            raise RuntimeError("no scope-changing command-line parameters are permitted")
        raise SystemExit(launch())
    except Exception:
        traceback.print_exc()
        raise SystemExit(1)
