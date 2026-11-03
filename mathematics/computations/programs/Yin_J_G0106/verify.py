"""Independent exact J106 reconstruction; actual run evidence is in verifier outputs.

No author module is imported.  Counts use binary autocorrelation; carry edges
are generated from the right and marks from the right half.  The n=5 check
enumerates complete original words and conditions on complete tail words.
Aggregate limits: 60 seconds, 512 MiB process memory, 64 MiB output, no retry.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import ctypes
from ctypes import wintypes
from fractions import Fraction as F
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OUTPUT = REPO / "mathematics" / "computations" / "outputs" / HERE.name
SECONDS, MEMORY, OUTPUT_LIMIT = 60.0, 512 * 1024**2, 64 * 1024**2
P = (1, -1, -1, -1, 1)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
DEADLINE = float("inf")
SCHEMA_FINAL = True
RESERVE = 64 * 1024


def reduce_polynomial(a):
    """Full descending monic Euclidean division, not a companion update."""
    w = list(a) + [0] * max(0, 4 - len(a))
    for j in range(len(w) - 1, 3, -1):
        q = w[j]
        if q:
            for i in range(5):
                w[j - 4 + i] -= q * P[i]
    return tuple(w[:4])


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    w = [0] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            w[i + j] += x * y
    return reduce_polynomial(w)


def power_tables():
    beta = (0, 1, 0, 0)
    # P(0)+beta*(P_1+...+P_4 beta^3)=0, with P(0)=1.
    inverse = tuple(-x for x in P[1:])
    assert mul(beta, inverse) == ONE
    positive, negative = [ONE], [ONE]
    for _ in range(20):
        positive.append(mul(positive[-1], beta))
        negative.append(mul(negative[-1], inverse))
    return positive, negative


def phi(y):
    s = [sum(y[j] * y[j + h] for j in range(4 - h)) for h in range(4)]
    return (s[0] + s[2] + 3 * s[3], s[1] + s[2] + s[3])


def qa(a, b):
    return (a[0] + b[0], a[1] + b[1])


def qs(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(a, q):
    return (a[0] * q, a[1] * q)


def qm(a, b):
    return (a[0] * b[0] + 3 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def qdivide(a, b):
    det = b[0] * b[0] + b[0] * b[1] - 3 * b[1] * b[1]
    assert det
    return qm(a, (F(b[0] + b[1], det), F(-b[1], det)))


def sign_quad(q):
    # 2(a+b*u)=(2a+b)-b*sqrt(13), u=(1-sqrt(13))/2.
    a, b = 2 * q[0] + q[1], -q[1]
    if not b:
        return (a > 0) - (a < 0)
    if not a:
        return (b > 0) - (b < 0)
    if (a > 0) == (b > 0):
        return (a > 0) - (a < 0)
    diff = a * a - 13 * b * b
    assert diff != 0  # Irrationality of sqrt(13), a,b rational nonzero.
    return ((a > 0) - (a < 0)) * ((diff > 0) - (diff < 0))


def rational(q):
    q = F(q)
    return [q.numerator, q.denominator]


def quadratic(q):
    return [rational(q[0]), rational(q[1])]


def parse_rat(q):
    assert isinstance(q, list) and len(q) == 2
    assert isinstance(q[0], int) and isinstance(q[1], int) and q[1] > 0
    return F(q[0], q[1])


def parse_quad(q):
    assert isinstance(q, list) and len(q) == 2
    return tuple(parse_rat(x) for x in q)


class MemoryInfo(ctypes.Structure):
    _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD)] + [
        (x, ctypes.c_size_t) for x in (
            "PeakWorkingSetSize", "WorkingSetSize", "QuotaPeakPagedPoolUsage",
            "QuotaPagedPoolUsage", "QuotaPeakNonPagedPoolUsage", "QuotaNonPagedPoolUsage",
            "PagefileUsage", "PeakPagefileUsage", "PrivateUsage")]


def guard():
    if time.perf_counter() >= DEADLINE:
        raise RuntimeError("Verifier aggregate 60-second cap exceeded; no escalation")
    if os.name == "nt":
        info = MemoryInfo()
        info.cb = ctypes.sizeof(info)
        ps = ctypes.WinDLL("psapi", use_last_error=True)
        ps.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD]
        if not ps.GetProcessMemoryInfo(wintypes.HANDLE(-1), ctypes.byref(info), info.cb):
            raise ctypes.WinError(ctypes.get_last_error())
        if info.PeakWorkingSetSize > MEMORY or info.PrivateUsage > MEMORY:
            raise RuntimeError("Verifier 512 MiB working/private-memory cap exceeded")


def save(path, obj):
    guard()
    payload = json.dumps(obj, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    guard()
    path.parent.mkdir(parents=True, exist_ok=True)
    current = sum(p.stat().st_size for p in path.parent.rglob("*") if p.is_file())
    if current + len(payload) > OUTPUT_LIMIT - RESERVE:
        raise RuntimeError("Verifier 64 MiB native-output cap exceeded")
    part = path.with_suffix(path.suffix + ".part")
    part.write_bytes(payload)
    part.replace(path)


def counts_by_binary_autocorrelation(positive):
    tables = {}
    binary = Counter({ZERO: 1})
    for length in range(11):
        guard()
        items = list(binary.items())
        difference = Counter()
        for i, (a, wa) in enumerate(items):
            if i % 16 == 0:
                guard()
            for b, wb in items:
                difference[sub(a, b)] += wa * wb
        assert sum(binary.values()) == 2**length
        assert sum(difference.values()) == 4**length
        assert all(difference[neg(a)] == w for a, w in difference.items())
        tables[length] = dict(difference)
        if length < 10:
            new = binary.copy()
            for a, w in binary.items():
                new[add(a, positive[length])] += w
            binary = new
    for theta in itertools.product((-1, 0, 1), repeat=4):
        assert tables[4][theta] == 2**theta.count(0)
    return tables


def involution_j(a, negative):
    out = ZERO
    for i, coefficient in enumerate(a):
        out = add(out, tuple(coefficient * x for x in negative[i + 1]))
    return out


def half_word_check(table, negative):
    total, mark = 0, (0, 0)
    for i, (a, w) in enumerate(table.items()):
        if i % 1024 == 0:
            guard()
        weight = w * table.get(involution_j(a, negative), 0)
        total += weight
        mark = qa(mark, scale(phi(a), weight))
    assert total > 0
    return total, scale(mark, F(1, total))


def group_energy(groups):
    result = (F(0), F(0))
    for weight, weighted_y in groups.values():
        result = qa(result, scale(phi(weighted_y), F(1, weight)))
    return result


def add_group(groups, key, weight, y):
    old_weight, old_y = groups.get(key, (0, ZERO))
    groups[key] = (old_weight + weight,
                   tuple(a + weight * b for a, b in zip(old_y, y)))


def components_from_edges(left, right, edges):
    adjacency = defaultdict(list)
    for li, ri, *_ in edges:
        adjacency[(0, li)].append((1, ri))
        adjacency[(1, ri)].append((0, li))
    unseen = set(adjacency)
    parts = []
    vertex_component = {}
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        stack, vertices = [root], []
        while stack:
            v = stack.pop()
            vertices.append(v)
            for w in adjacency[v]:
                if w in unseen:
                    unseen.remove(w)
                    stack.append(w)
        vertices.sort()
        component = {"left": [i for side, i in vertices if side == 0],
                     "right": [i for side, i in vertices if side == 1],
                     "edges": [],
                     "weight": 0, "weighted_y": [0] * 4,
                     "weighted_phi": [0, 0]}
        for v in vertices:
            vertex_component[v] = len(parts)
        parts.append(component)
    for eidx, (li, ri, weight, *tail) in enumerate(edges):
        y = tuple(tail[:4])
        j = vertex_component[(0, li)]
        assert j == vertex_component[(1, ri)]
        component = parts[j]
        component["edges"].append(eidx)
        component["weight"] += weight
        component["weighted_y"] = list(add(component["weighted_y"], tuple(weight * x for x in y)))
        component["weighted_phi"] = list(qa(component["weighted_phi"], scale(phi(y), weight)))
    total = sum(c["weight"] for c in parts)
    for c in parts:
        w = c["weight"]
        c["mass"] = rational(F(w, total))
        c["mean"] = [rational(F(x, w)) for x in c["weighted_y"]]
        c["moment"] = quadratic(scale(c["weighted_phi"], F(1, w)))
        c["mean_square"] = quadratic(scale(phi(c["weighted_y"]), F(1, w * w)))
    return parts


def reconstruct_case(n, tables, positive, negative):
    guard()
    k = n - 2
    table = tables[k]
    middle = list(itertools.product((-1, 0, 1), repeat=4))
    middle_shifted = [(theta, mul(positive[k], theta)) for theta in middle]
    raw = {}
    attempted = 0
    for number, c in enumerate(sorted(table)):
        if number % 32 == 0:
            guard()
        shifted_c = mul(positive[k + 4], c)
        right_mark = mul(positive[2], c)
        for theta, shifted_theta in middle_shifted:
            attempted += 1
            a = neg(add(shifted_c, shifted_theta))
            if a not in table:
                continue
            y = add(right_mark, (theta[2], theta[3], 0, 0))
            w = table[a] * table[c] * 2**theta.count(0)
            assert (a, c) not in raw
            raw[(a, c)] = (w, y, theta)
    left = sorted({a for a, c in raw})
    right = sorted({c for a, c in raw})
    li, ri = {a: i for i, a in enumerate(left)}, {c: i for i, c in enumerate(right)}
    edges = [[li[a], ri[c], w, *y, *theta] for (a, c), (w, y, theta) in sorted(raw.items())]
    rows, cols = [0] * len(left), [0] * len(right)
    row_groups, col_groups = {}, {}
    total, mark = 0, (0, 0)
    for a, c, w, *tail in edges:
        y = tuple(tail[:4])
        rows[a] += w
        cols[c] += w
        total += w
        mark = qa(mark, scale(phi(y), w))
        add_group(row_groups, a, w, y)
        add_group(col_groups, c, w, y)
    assert len(left) >= 2 and len(right) >= 2
    assert all(x > 0 for x in rows + cols)
    moment = scale(mark, F(1, total))
    energy = qs(moment, scale(qa(group_energy(row_groups), group_energy(col_groups)), F(1, 2 * total)))
    assert sign_quad(moment) > 0
    assert sign_quad(energy) >= 0
    assert sign_quad(qs(moment, energy)) >= 0
    assert sign_quad(qs((4, 0), energy)) >= 0
    assert all(sum(v[1][j] for v in row_groups.values()) == 0 for j in range(4))
    half_total, half_moment = half_word_check(tables[n], negative)
    assert total == half_total and moment == half_moment
    assert max(Counter(e[0] for e in edges).values()) <= 81
    assert max(Counter(e[1] for e in edges).values()) <= 81
    result = {"n": n, "N": 2*n, "b": 2, "k": k, "left": [list(x) for x in left],
              "right": [list(x) for x in right], "row_masses": rows, "column_masses": cols,
              "row_mark_sum_beta": [list(row_groups[i][1]) for i in range(len(left))],
              "column_mark_sum_beta": [list(col_groups[i][1]) for i in range(len(right))],
              "moment_numerator_pair": list(mark),
              "edges": edges, "S": total, "m_pair": quadratic(moment),
              "D_pair": quadratic(energy), "rayleigh_pair": quadratic(qdivide(energy, moment)),
              "components": components_from_edges(left, right, edges),
              "candidate_lookups": attempted,
              "half_word_check": {"S": half_total, "m_pair": quadratic(half_moment)}}
    return result, raw


def direct_n5(raw_expected):
    """All 3^10 words, with full-word tail conditioning and direct polynomial reduction."""
    edges = Counter()
    marks = {}
    left_groups, right_groups = {}, {}
    total, mark, returned, inspected = 0, (0, 0), 0, 0
    for word in itertools.product((-1, 0, 1), repeat=10):
        inspected += 1
        if inspected % 1024 == 0:
            guard()
        if reduce_polynomial(word) != ZERO:
            continue
        returned += 1
        weight = 2**word.count(0)
        a, c = reduce_polynomial(word[:3]), reduce_polynomial(word[7:])
        y = reduce_polynomial(word[5:])
        theta = word[3:7]
        edge = (a, c)
        if edge in marks:
            assert marks[edge] == (y, theta)
        marks[edge] = (y, theta)
        edges[edge] += weight
        total += weight
        mark = qa(mark, scale(phi(y), weight))
        add_group(left_groups, word[:3], weight, y)
        add_group(right_groups, word[7:], weight, y)
    assert inspected == 3**10
    actual = {edge: (weight, *marks[edge]) for edge, weight in edges.items()}
    assert actual == raw_expected
    moment = scale(mark, F(1, total))
    energy = qs(moment, scale(qa(group_energy(left_groups), group_energy(right_groups)), F(1, 2 * total)))
    return {"words_inspected": inspected, "returned_words": returned,
            "edge_count": len(edges), "S": total, "m_pair": quadratic(moment),
            "D_pair": quadratic(energy), "complete_tail_word_conditioning": True}


def compare_author_counts(author, tables):
    assert set(author) == {"schema", "tables"}
    assert author["schema"] == "g106-counts-v1"
    assert set(author["tables"]) == {str(l) for l in range(11)}
    for length in range(11):
        rows = author["tables"][str(length)]
        assert all(len(row) == 5 and all(isinstance(x, int) for x in row) and row[4] > 0 for row in rows)
        assert rows == [[*a, w] for a, w in sorted(tables[length].items())]


def compare_author_case(author, case):
    assert author["schema"] == "g106-case-v1"
    for key in ("n", "N", "b", "k", "left", "right", "edges", "S",
                "row_mark_sum_beta", "column_mark_sum_beta", "moment_numerator_pair"):
        assert author[key] == case[key], key
    assert author["row_mass"] == case["row_masses"]
    assert author["column_mass"] == case["column_masses"]
    for key in ("m_pair", "D_pair"):
        assert parse_quad(author[key]) == parse_quad(case[key]), key
    assert parse_quad(author["rayleigh_upper_pair"]) == parse_quad(case["rayleigh_pair"])
    assert author["half_word_S"] == case["half_word_check"]["S"]
    half = parse_quad(case["half_word_check"]["m_pair"])
    assert tuple(author["half_word_moment_numerator_pair"]) == scale(half, case["S"])
    expected = {(tuple(c["left"]), tuple(c["right"])): c for c in case["components"]}
    observed = {(tuple(c["left"]), tuple(c["right"])): c for c in author["components"]}
    assert len(observed) == len(author["components"]) == len(expected)
    assert observed.keys() == expected.keys()
    for key, independent in expected.items():
        published = observed[key]
        assert published["edges"] == independent["edges"]
        assert published["mass_integer"] == independent["weight"]
        assert parse_rat(published["probability"]) == parse_rat(independent["mass"])
        assert [parse_rat(x) for x in published["mean_beta"]] == [parse_rat(x) for x in independent["mean"]]
        assert parse_quad(published["mean_square_pair"]) == parse_quad(independent["mean_square"])
        assert parse_quad(published["second_moment_pair"]) == parse_quad(independent["moment"])
    checks = author["checks"]
    assert all(checks[x] is True for x in ("complete_half_word_agreement", "energy_between_zero_and_four",
                                          "energy_at_most_moment", "centered_midpoint"))
    assert checks["maximum_left_degree"] == max(Counter(e[0] for e in case["edges"]).values())
    assert checks["maximum_right_degree"] == max(Counter(e[1] for e in case["edges"]).values())


def worker(args):
    global DEADLINE
    if sys.stdin.readline().strip() != "GO":
        raise RuntimeError("Parent resource gate missing")
    DEADLINE = args.deadline
    start = time.perf_counter()
    author_dir, output_dir = args.author, args.output
    inputs = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    expected_input = {"schema": "g106-input-v1", "polynomial_ascending": list(P),
                      "digits": [-1, 0, 1], "integer_digit_weights": [1, 2, 1],
                      "n_values": list(range(5, 11)), "b": 2, "wall_seconds": 60,
                      "worker_memory_bytes": MEMORY, "author_output_bytes": OUTPUT_LIMIT}
    assert inputs == expected_input
    execution = json.loads((author_dir / "execution.json").read_text(encoding="utf-8"))
    assert execution["status"] == "complete" and execution["returncode"] == 0
    assert execution["wall_seconds"] <= SECONDS
    assert execution["worker_job_memory_cap_bytes"] == execution["worker_working_set_cap_bytes"] == MEMORY
    for key in ("peak_worker_commit_bytes", "peak_job_commit_bytes"):
        assert execution[key] is None or 0 <= execution[key] <= MEMORY
    assert sum(p.stat().st_size for p in author_dir.rglob("*") if p.is_file()) <= OUTPUT_LIMIT
    positive, negative = power_tables()
    tables = counts_by_binary_autocorrelation(positive)
    author_counts = json.loads((author_dir / "counts.json").read_text(encoding="utf-8"))
    compare_author_counts(author_counts, tables)
    save(output_dir / "counts.json", {str(l): [[*a, w] for a, w in sorted(table.items())]
                                      for l, table in tables.items()})
    completed, lookups = [], 0
    for n in range(5, 11):
        case, raw = reconstruct_case(n, tables, positive, negative)
        lookups += case["candidate_lookups"]
        compare_author_case(json.loads((author_dir / f"case_n{n:02d}.json").read_text(encoding="utf-8")), case)
        if n == 5:
            direct = direct_n5(raw)
            assert all(direct[key] == case[key] for key in ("S", "m_pair", "D_pair"))
            case["direct_word_verification"] = direct
        case["verification"] = "complete exact reconstruction and author comparison"
        save(output_dir / f"case_n{n:02d}.json", case)
        completed.append(n)
        print(json.dumps({"completed_n": n, "edge_count": len(case["edges"]),
                          "component_count": len(case["components"])}), flush=True)
    aggregate = json.loads((author_dir / "results.json").read_text(encoding="utf-8"))
    assert aggregate["status"] == "complete" and aggregate["completed_n"] == completed
    assert aggregate["scope"] == inputs
    assert aggregate["candidate_edge_lookups"] == lookups <= 796068
    result = {"status": "complete", "completed_n": completed,
              "methods": ["binary endpoint autocorrelation", "right-endpoint carry construction",
                          "right-half midpoint", "independent half-word marks",
                          "all original n=5 words and complete-tail conditional variance"],
              "author_helpers_imported": False, "arithmetic": "exact integers and rational Q(u)",
              "candidate_edge_lookups": lookups,
              "u_embedding": "(1-sqrt(13))/2", "elapsed_worker_seconds": time.perf_counter() - start,
              "limits": {"aggregate_seconds": SECONDS, "memory_bytes": MEMORY, "output_bytes": OUTPUT_LIMIT}}
    save(output_dir / "verification.json", result)
    print(json.dumps({"status": "complete", "completed_n": completed}), flush=True)


class BasicLimit(ctypes.Structure):
    _fields_ = [("PerProcessUserTimeLimit", ctypes.c_longlong),
                ("PerJobUserTimeLimit", ctypes.c_longlong), ("LimitFlags", wintypes.DWORD),
                ("MinimumWorkingSetSize", ctypes.c_size_t), ("MaximumWorkingSetSize", ctypes.c_size_t),
                ("ActiveProcessLimit", wintypes.DWORD), ("Affinity", ctypes.c_size_t),
                ("PriorityClass", wintypes.DWORD), ("SchedulingClass", wintypes.DWORD)]


class IOCounters(ctypes.Structure):
    _fields_ = [(x, ctypes.c_ulonglong) for x in ("ReadOperationCount", "WriteOperationCount",
        "OtherOperationCount", "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]


class ExtendedLimit(ctypes.Structure):
    _fields_ = [("BasicLimitInformation", BasicLimit), ("IoInfo", IOCounters)] + [
        (x, ctypes.c_size_t) for x in ("ProcessMemoryLimit", "JobMemoryLimit",
                                      "PeakProcessMemoryUsed", "PeakJobMemoryUsed")]


def attach_memory_job(process):
    if os.name != "nt":
        raise RuntimeError("Declared verifier resource wrapper requires Windows; no unguarded fallback")
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
    kernel.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel.QueryInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p,
                                                wintypes.DWORD, ctypes.c_void_p]
    kernel.SetProcessWorkingSetSizeEx.argtypes = [wintypes.HANDLE, ctypes.c_size_t,
                                                 ctypes.c_size_t, wintypes.DWORD]
    kernel.GetProcessWorkingSetSizeEx.argtypes = [wintypes.HANDLE, ctypes.c_void_p,
                                                 ctypes.c_void_p, ctypes.c_void_p]
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    limits = ExtendedLimit()
    limits.BasicLimitInformation.LimitFlags = 0x100 | 0x200 | 0x2000
    limits.BasicLimitInformation.MinimumWorkingSetSize = 1024 * 1024
    limits.BasicLimitInformation.MaximumWorkingSetSize = MEMORY
    limits.ProcessMemoryLimit = MEMORY
    limits.JobMemoryLimit = MEMORY
    if not kernel.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    if not kernel.AssignProcessToJobObject(job, wintypes.HANDLE(process._handle)):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    # Primary memoryapi contract: disable hard minimum, enable hard maximum.
    handle = wintypes.HANDLE(process._handle)
    if not kernel.SetProcessWorkingSetSizeEx(handle, 1024 * 1024, MEMORY, 0x2 | 0x4):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    lo, hi, flags = ctypes.c_size_t(), ctypes.c_size_t(), wintypes.DWORD()
    if not kernel.GetProcessWorkingSetSizeEx(handle, ctypes.byref(lo), ctypes.byref(hi), ctypes.byref(flags)):
        kernel.CloseHandle(job)
        raise ctypes.WinError(ctypes.get_last_error())
    if hi.value > MEMORY or not (flags.value & 0x4):
        kernel.CloseHandle(job)
        raise RuntimeError("Verifier hard working-set maximum was not confirmed")
    return kernel, job


def parent(args):
    if not SCHEMA_FINAL:
        raise RuntimeError("Verifier is prepared but public-schema binding is not final; no computation started")
    if args.output.exists() and any(args.output.iterdir()):
        raise RuntimeError("Verifier output already exists; no implicit second run or overwrite")
    start = time.perf_counter()
    deadline = start + SECONDS
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", "--deadline", str(deadline),
               "--author", str(args.author), "--output", str(args.output)]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    job = None
    failure = None
    measured = None
    try:
        kernel, job = attach_memory_job(process)
        stdout, stderr = process.communicate("GO\n", timeout=max(0.001, deadline - time.perf_counter()))
        print(stdout, end="")
        if stderr:
            print(stderr, file=sys.stderr, end="")
        if process.returncode:
            failure = f"Independent worker failed with exit code {process.returncode}"
        elif time.perf_counter() > deadline:
            failure = "Verifier aggregate 60-second cap exceeded at completion; no escalation"
    except BaseException as exc:
        failure = repr(exc)
        process.kill()
        stdout, stderr = process.communicate()
        print(stdout, end="")
        print(stderr, file=sys.stderr, end="")
    finally:
        if job:
            usage = ExtendedLimit()
            if kernel.QueryInformationJobObject(job, 9, ctypes.byref(usage), ctypes.sizeof(usage), None):
                measured = {"peak_worker_commit_bytes": usage.PeakProcessMemoryUsed,
                            "peak_job_commit_bytes": usage.PeakJobMemoryUsed}
            kernel.CloseHandle(job)
    args.output.mkdir(parents=True, exist_ok=True)
    execution = {"status": "complete" if failure is None else "incomplete",
                 "returncode": process.returncode, "wall_seconds": time.perf_counter() - start,
                 "worker_memory_cap_bytes": MEMORY, "worker_working_set_cap_bytes": MEMORY,
                 "parent_monitor_excluded_from_worker_memory_limit": True,
                 "memory_measurement": measured, "stdout": stdout, "stderr": stderr}
    payload = json.dumps(execution, separators=(",", ":")).encode("utf-8")
    used = sum(p.stat().st_size for p in args.output.rglob("*") if p.is_file())
    if used + len(payload) > OUTPUT_LIMIT:
        raise RuntimeError("Verifier execution metadata would exceed the reserved native-output cap")
    (args.output / "execution.json").write_bytes(payload)
    if failure:
        # Only metadata is published after a stopped worker.  Completed cases remain.
        args.output.mkdir(parents=True, exist_ok=True)
        completed = []
        for line in stdout.splitlines():
            try:
                item = json.loads(line)
            except (ValueError, TypeError):
                continue
            if isinstance(item, dict) and isinstance(item.get("completed_n"), int):
                completed.append(item["completed_n"])
        record = {"status": "incomplete", "failure": failure, "completed_n": completed,
                  "no_escalation": True, "elapsed_parent_seconds": time.perf_counter() - start}
        path = args.output / "verification.json"
        payload = json.dumps(record, separators=(",", ":")).encode("utf-8")
        used = sum(p.stat().st_size for p in args.output.rglob("*") if p.is_file())
        if used - (path.stat().st_size if path.exists() else 0) + len(payload) <= OUTPUT_LIMIT:
            path.write_bytes(payload)
        print(json.dumps(record), file=sys.stderr)
        raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--deadline", type=float, default=float("inf"))
    parser.add_argument("--author", type=Path, default=OUTPUT / "author")
    parser.add_argument("--output", type=Path, default=OUTPUT / "verifier")
    args = parser.parse_args()
    if args.worker:
        worker(args)
    else:
        parent(args)


if __name__ == "__main__":
    main()
