"""Independent positive-witness verifier for J107; no author math imports.

Prepared before verification execution.  Exact triangular inversion and Newton
traces replace author Bareiss interpolation; step-two coefficient differences
replace its formal Boolean derivatives.  The Windows resource guard is copied
from this reviewer's existing J106 verifier solely as operational code reuse.
Negative/exhausted outcomes require a separately declared complete verifier.
"""
from __future__ import annotations

import argparse
import ast
import ctypes
from ctypes import wintypes
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import zipfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OUTPUT = REPO / "mathematics/computations/outputs" / HERE.name
SECONDS = 300
MEMORY = 512 * 1024 * 1024
OUTPUT_LIMIT = 64 * 1024 * 1024
SCHEMA_FINAL = True
POSITIONS = [(i, j) for i in range(7) for j in range(i + 1, 7)]
TARGETS = {
    "phi2_phi6_p4": [1, -1, -1, 0, 0, -1, -1, 1],
    "phi2_p6": [1, 0, -1, -1, -1, -1, 0, 1],
}


def multiply(a, b):
    n, k, m = len(a), len(b), len(b[0])
    assert all(len(row) == k for row in a)
    return [[sum(a[i][r] * b[r][j] for r in range(k))
             for j in range(m)] for i in range(n)]


def polynomial_product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return out


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def pencil_by_newton(u):
    """det(tU+U^T) via the actual integer C=-U^-1 U^T and Newton identities."""
    n = len(u)
    assert all(len(row) == n for row in u)
    assert all(u[i][i] == 1 for i in range(n))
    assert all(u[i][j] == 0 for i in range(n) for j in range(i))
    inv = identity(n)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            inv[i][j] = -sum(u[i][k] * inv[k][j] for k in range(i + 1, j + 1))
    assert multiply(u, inv) == identity(n) == multiply(inv, u)
    c = [[-v for v in row] for row in multiply(inv, list(map(list, zip(*u))))]
    power = identity(n)
    traces = [0]
    coefficients = [1]
    for k in range(1, n + 1):
        power = multiply(power, c)
        traces.append(sum(power[i][i] for i in range(n)))
        numerator = -sum(coefficients[k - j] * traces[j] for j in range(1, k + 1))
        assert numerator % k == 0
        coefficients.append(numerator // k)
    p = coefficients[::-1]
    assert p[0] == p[-1] == 1 and p == p[::-1]
    return p


def from_bits(mask, correction=0):
    assert type(mask) is int and type(correction) is int
    assert 0 <= mask < 2 ** 21 and 0 <= correction < 2 ** 21
    out = identity(7)
    for bit, (i, j) in enumerate(POSITIONS):
        out[i][j] = (mask // 2 ** bit) % 2 + 2 * ((correction // 2 ** bit) % 2)
    return out


def negative_absolute(u):
    n = len(u)
    result = identity(n)
    for i in range(n):
        for j in range(i + 1, n):
            result[i][j] = -abs(u[i][j])
    return result


def literal_cover(u):
    n = len(u)
    result = identity(2 * n)
    for i in range(n):
        for j in range(i + 1, n):
            a = u[i][j]
            if a <= 0:
                result[2 * i][2 * j] = a
                result[2 * i + 1][2 * j + 1] = a
            else:
                result[2 * i][2 * j + 1] = -a
                result[2 * i + 1][2 * j] = -a
    return result


def xor_image(columns):
    # Independent closure of a subset of the eight-element vector space.
    image = {0}
    for column in columns:
        image |= {x ^ column for x in image}
    return sorted(image)


def selected_native_rows(archive_path, mask):
    """Read only the three selected native rows; no NumPy or table recomputation."""
    expected = {"coefficient_residues.npy": (2 ** 21, 3),
                "derivative_columns.npy": (2 ** 21, 21),
                "image_bits.npy": (2 ** 21,)}
    rows = {}
    with zipfile.ZipFile(archive_path) as archive:
        assert set(archive.namelist()) == set(expected)
        for name, shape in expected.items():
            with archive.open(name) as stream:
                assert stream.read(6) == b"\x93NUMPY"
                version = tuple(stream.read(2))
                assert version in ((1, 0), (2, 0), (3, 0))
                size = 2 if version == (1, 0) else 4
                length = int.from_bytes(stream.read(size), "little")
                header = ast.literal_eval(stream.read(length).decode("utf-8"))
                assert header == {"descr": "|u1", "fortran_order": False, "shape": shape}
                offset = stream.tell()
                width = shape[1] if len(shape) == 2 else 1
                assert archive.getinfo(name).file_size == offset + shape[0] * width
                stream.seek(offset + mask * width)
                row = list(stream.read(width))
                assert len(row) == width
                rows[name] = row
    return rows


def check_witness(target, witness, deadline):
    mask = witness["binary_mask"]
    correction = witness["correction_mask"]
    base_matrix = from_bits(mask)
    base_polynomial = pencil_by_newton(base_matrix)
    residues = [x % 4 for x in base_polynomial[1:4]]
    assert residues == witness["base_coefficient_residues"]
    assert [x % 2 for x in residues] == [x % 2 for x in target[1:4]]
    columns, increment_polynomials = [], []
    for i, j in POSITIONS:
        assert time.perf_counter() < deadline
        perturbed = [row[:] for row in base_matrix]
        perturbed[i][j] += 2
        changed = pencil_by_newton(perturbed)
        differences = [changed[k] - base_polynomial[k] for k in (1, 2, 3)]
        assert all(x % 2 == 0 for x in differences)
        columns.append(sum(((differences[k] // 2) % 2) << k for k in range(3)))
        increment_polynomials.append(changed)
    assert columns == witness["derivative_columns"]
    image = xor_image(columns)
    assert image == witness["derivative_image"]
    rhs = sum((((target[k + 1] - residues[k]) // 2) % 2) << k for k in range(3))
    assert rhs == witness["right_side"] and rhs in image
    actual = 0
    for j, column in enumerate(columns):
        if (correction >> j) & 1:
            actual ^= column
    assert actual == rhs
    matrix = from_bits(mask, correction)
    absolute = negative_absolute(matrix)
    cover = literal_cover(matrix)
    for key, value in (("matrix", matrix), ("absolute_matrix", absolute), ("cover_matrix", cover)):
        assert witness[key] == value
    integer_p = pencil_by_newton(matrix)
    absolute_p = pencil_by_newton(absolute)
    cover_p = pencil_by_newton(cover)
    assert cover_p == polynomial_product(integer_p, absolute_p)
    assert [x % 4 for x in integer_p] == [x % 4 for x in target]
    for key, value in (("integer_polynomial", integer_p), ("absolute_polynomial", absolute_p),
                       ("cover_polynomial", cover_p)):
        assert witness[key] == value
    energy = sum(matrix[i][j] ** 2 for i, j in POSITIONS)
    height = max(abs(x) for row in matrix for x in row)
    assert witness["energy"] == energy and witness["height"] == height
    assert time.perf_counter() < deadline
    return {"status": "complete_positive_witness", "target_polynomial": target,
            "binary_mask": mask, "correction_mask": correction,
            "base_polynomial": base_polynomial, "base_coefficient_residues": residues,
            "step_two_increment_polynomials": increment_polynomials,
            "derivative_columns": columns, "derivative_image": image, "right_side": rhs,
            "matrix": matrix, "absolute_matrix": absolute, "cover_matrix": cover,
            "integer_polynomial": integer_p, "absolute_polynomial": absolute_p,
            "cover_polynomial": cover_p, "energy": energy, "height": height,
            "exact_integer_target_equal": integer_p == target}


def save(path, payload, output):
    data = (json.dumps(payload, indent=2) + "\n").encode("utf-8")
    used = sum(p.stat().st_size for p in output.rglob("*") if p.is_file())
    assert used + len(data) < OUTPUT_LIMIT - 65536
    temporary = path.with_suffix(".pending")
    temporary.write_bytes(data)
    temporary.replace(path)


def worker(args):
    if sys.stdin.readline().strip() != "GO":
        raise RuntimeError("Independent worker requires its declared memory/time guard")
    started = time.perf_counter()
    assert started < args.deadline
    author = json.loads((args.author / "result.json").read_text(encoding="utf-8"))
    execution = json.loads((args.author / "execution.json").read_text(encoding="utf-8"))
    assert author["status"] == execution["status"] == "complete"
    assert execution["returncode"] == 0 and execution["wall_seconds"] <= SECONDS
    assert execution["worker_job_memory_cap_bytes"] == MEMORY
    assert execution["worker_working_set_cap_bytes"] == MEMORY
    for key in ("peak_worker_commit_bytes", "peak_job_commit_bytes"):
        assert execution[key] is None or 0 <= execution[key] <= MEMORY
    assert sum(p.stat().st_size for p in args.author.rglob("*") if p.is_file()) <= OUTPUT_LIMIT
    assert polynomial_product([1, 1], polynomial_product([1, -1, 1], [1, -1, -1, -1, 1])) == TARGETS["phi2_phi6_p4"]
    assert polynomial_product([1, 1], [1, -1, 0, -1, 0, -1, 1]) == TARGETS["phi2_p6"]
    assert author["target_polynomials"] == TARGETS
    assert author["binary_bases"] == 2 ** 21 and author["permutations"] == 5040
    assert author["all_binary_derivative_maps_evaluated"] == 2 ** 21
    assert set(author["targets"]) == set(TARGETS)
    histogram = author["coefficient_residue_histogram"]
    assert len(histogram) == 64 and all(type(x) is int and x >= 0 for x in histogram)
    assert sum(histogram) == 2 ** 21
    # These are author aggregate sanity checks only; the histogram is not rerun.
    for name, target in TARGETS.items():
        entry = author["targets"][name]
        if entry["modular_status"] != "compatible" or entry["witness"] is None:
            raise RuntimeError("Negative/incomplete branch needs separate complete-domain verification; no scan started")
        assert entry["derivative_bases_checked"] == entry["target_parity_bases"]
        assert 1 <= entry["compatible_binary_bases"] <= entry["target_parity_bases"] <= 2 ** 21
        parity_count = sum(count for code, count in enumerate(histogram)
                           if [(code // (4 ** k)) % 2 for k in range(3)] == [v % 2 for v in target[1:4]])
        assert parity_count == entry["target_parity_bases"]
    args.output.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, target in TARGETS.items():
        results[name] = check_witness(target, author["targets"][name]["witness"], args.deadline)
        checked = results[name]
        rows = selected_native_rows(args.author / "tables.npz", checked["binary_mask"])
        assert rows["coefficient_residues.npy"] == checked["base_coefficient_residues"]
        assert rows["derivative_columns.npy"] == checked["derivative_columns"]
        assert rows["image_bits.npy"] == [sum(1 << x for x in checked["derivative_image"])]
        checked["selected_native_table_rows"] = rows
        print(json.dumps({"verified_target": name, "derivative_columns": 21}), flush=True)
    result = {"status": "complete", "scope": "two explicit positive modular witnesses only",
              "targets": results, "independent_derivative_columns": 42,
              "author_math_helpers_imported": False,
              "methods": ["triangular inverse plus Newton traces", "exact step-two coefficient differences",
                          "literal rank-14 cover reconstruction"],
              "not_independently_recomputed": ["whole binary residue histogram and feasible-base counts", "first-mask minimality",
                                               "negative complete-domain obstruction"],
              "shared_runtime": "Python integer arithmetic and Windows operational resource guard",
              "elapsed_worker_seconds": time.perf_counter() - started,
              "limits": {"aggregate_seconds": SECONDS, "worker_memory_bytes": MEMORY,
                         "output_bytes": OUTPUT_LIMIT}}
    assert time.perf_counter() < args.deadline
    save(args.output / "verification.json", result, args.output)
    assert time.perf_counter() < args.deadline
    print(json.dumps({"status": "complete", "verified_targets": list(results)}), flush=True)


# The following launcher is operational reuse of the reviewer's J106 guard.

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
            failure = "Verifier aggregate 300-second cap exceeded at completion; no escalation"
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
            if isinstance(item, dict) and isinstance(item.get("verified_target"), str):
                completed.append(item["verified_target"])
        record = {"status": "incomplete", "failure": failure, "completed_targets": completed,
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
