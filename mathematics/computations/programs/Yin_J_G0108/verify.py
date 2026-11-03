"""J108 independent exact verifier: formal permutation determinant, no author math helpers.

All 5040 permutations are processed in Z[t,x,y,z]; every integer grid pencil
is separately recomputed by scalar univariate permutation expansion.  The
Windows Job/working-set monitor is operational reuse only.  This is nonblind:
the protocol, author source/schema and reported zero count were available.
"""
from __future__ import annotations
import ctypes
from ctypes import wintypes
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
OUT = REPO / 'mathematics/computations/outputs' / HERE.name / 'verifier'
AUTHOR = REPO / 'mathematics/computations/outputs' / HERE.name / 'author' / 'result.json'
CAP_SECONDS = 30
CAP_MEMORY = 256 * 1024 * 1024
CAP_OUTPUT = 32 * 1024 * 1024
ZERO = (0, 0, 0, 0)


def signed_permutations(n):
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        yield perm, -1 if inversions % 2 else 1


def formal_product(p, q):
    result = {}
    for a, x in p.items():
        for b, y in q.items():
            key = tuple(a[i] + b[i] for i in range(4))
            result[key] = result.get(key, 0) + x * y
    return {key: value for key, value in result.items() if value}


def symbolic_pencil(base, positions, permutations, check):
    variable = {tuple(pos): axis + 1 for axis, pos in enumerate(positions)}
    entries = []
    for i in range(7):
        row = []
        for j in range(7):
            if i == j:
                row.append({ZERO: 1, (1, 0, 0, 0): 1})
                continue
            upper = (min(i, j), max(i, j))
            exponent = [int(i < j), 0, 0, 0]
            if upper in variable:
                exponent[variable[upper]] = 1
                row.append({tuple(exponent): 1})
            else:
                value = base[upper[0]][upper[1]]
                row.append({tuple(exponent): value} if value else {})
        entries.append(row)
    determinant = {}
    used = 0
    for perm, sign in permutations:
        used += 1
        if used % 128 == 0:
            check()
        product = {ZERO: sign}
        for i, j in enumerate(perm):
            product = formal_product(product, entries[i][j])
            if not product:
                break
        for key, value in product.items():
            determinant[key] = determinant.get(key, 0) + value
    assert used == 5040
    determinant = {key: value for key, value in determinant.items() if value}
    assert all(0 <= key[0] <= 7 and all(0 <= p <= 2 for p in key[1:]) for key in determinant)
    coefficients = [{key[1:]: value for key, value in determinant.items() if key[0] == degree}
                    for degree in range(8)]
    assert coefficients[0] == coefficients[7] == {(0, 0, 0): 1}
    assert coefficients == coefficients[::-1]
    return coefficients


def scalar_pencil(matrix, permutations, check):
    """Independent per-point univariate determinant; no t interpolation."""
    result = [0] * 8
    for index, (perm, sign) in enumerate(permutations):
        if index % 256 == 0:
            check()
        product = [sign]
        for i, j in enumerate(perm):
            constant, linear = matrix[j][i], matrix[i][j]
            if not constant and not linear:
                product = []
                break
            next_product = [0] * (len(product) + 1)
            for degree, coefficient in enumerate(product):
                next_product[degree] += constant * coefficient
                next_product[degree + 1] += linear * coefficient
            product = next_product
        for degree, coefficient in enumerate(product):
            result[degree] += coefficient
    return result


def evaluate(poly, point):
    result = 0
    for exponent, coefficient in poly.items():
        monomial = coefficient
        for axis in range(3):
            monomial *= point[axis] ** exponent[axis]
        result += monomial
    return result


def derivative(poly, axis):
    result = {}
    for exponent, coefficient in poly.items():
        if exponent[axis]:
            reduced = list(exponent)
            reduced[axis] -= 1
            result[tuple(reduced)] = coefficient * exponent[axis]
    return result


def determinant_three(matrix):
    return sum(sign * matrix[0][p[0]] * matrix[1][p[1]] * matrix[2][p[2]]
               for p, sign in signed_permutations(3))


def encode(poly):
    return [list(exponent) + [coefficient] for exponent, coefficient in sorted(poly.items())]


def worker():
    if sys.stdin.readline().strip() != 'JOB_READY':
        raise RuntimeError('hard resource guard required')
    started = time.monotonic()

    def check():
        if time.monotonic() - started > CAP_SECONDS - 1:
            raise TimeoutError('independent aggregate deadline')

    inp = json.loads((HERE / 'inputs.json').read_text(encoding='utf-8'))
    base = inp['base_matrix']
    assert base == [[1,0,0,1,0,1,1], [0,1,0,1,1,1,0], [0,0,1,1,1,0,0],
                    [0,0,0,1,2,2,0], [0,0,0,0,1,0,0], [0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,1]]
    assert inp['variable_positions'] == [[0,2],[3,4],[4,6]]
    assert inp['target_polynomial'] == [1,-1,-1,0,0,-1,-1,1]
    assert inp['grid_values'] == [0,1,2] and inp['prime'] == 3
    assert inp['caps'] == {'seconds': CAP_SECONDS, 'worker_memory_bytes': CAP_MEMORY,
                           'output_bytes': CAP_OUTPUT}
    permutations = list(signed_permutations(7))
    assert len(permutations) == 5040
    full = symbolic_pencil(base, inp['variable_positions'], permutations, check)
    triple = full[1:4]
    derivatives = [[derivative(poly, axis) for axis in range(3)] for poly in triple]
    rows, jacobians, solutions, integer_targets = [], [], [], []
    for point in itertools.product(range(3), repeat=3):
        check()
        matrix = [row[:] for row in base]
        for (i,j), value in zip(inp['variable_positions'], point):
            matrix[i][j] = value
        scalar = scalar_pencil(matrix, permutations, check)
        formal_value = [evaluate(poly, point) for poly in full]
        assert scalar == formal_value
        residual = [(scalar[degree] - inp['target_polynomial'][degree]) % 3
                    for degree in (1,2,3)]
        row = {'point': list(point), 'integer_polynomial': scalar,
               'target_residual_mod3': residual}
        rows.append(row)
        jacobian = [[evaluate(poly, point) % 3 for poly in derivative_row]
                    for derivative_row in derivatives]
        det = determinant_three(jacobian) % 3
        jacobians.append({'point': list(point), 'jacobian_mod3': jacobian,
                          'determinant_mod3': det})
        if residual == [0,0,0]:
            solutions.append({'point': list(point), 'jacobian_mod3': jacobian,
                              'determinant_mod3': det, 'integer_polynomial': scalar})
        if scalar == inp['target_polynomial']:
            integer_targets.append(list(point))
    assert len(rows) == len(jacobians) == 27
    assert len({tuple(row['point']) for row in rows}) == 27

    # Verify the separately supplied manual F3 reduction as a polynomial identity.
    total = {(0,0,0): 2}
    for poly in triple:
        for exponent, value in poly.items():
            total[exponent] = total.get(exponent, 0) + value
    total = {exponent: value % 3 for exponent, value in total.items() if value % 3}
    manual = {(0,0,0):1, (0,0,1):2, (0,0,2):2,
              (0,1,0):2, (0,2,0):1, (1,1,0):1}
    assert total == manual
    candidates_after_sum_and_a = [row for row in rows
                                   if sum(row['target_residual_mod3']) % 3 == 0
                                   and row['target_residual_mod3'][0] == 0]
    manual_points = [row['point'] for row in candidates_after_sum_and_a]
    manual_b = [row['target_residual_mod3'][1] for row in candidates_after_sum_and_a]
    assert manual_points == [[0,2,0], [1,1,1]] and manual_b == [2,1]

    # Only now inspect and compare the actual author payload.
    check()
    author = json.loads(AUTHOR.read_text(encoding='utf-8'))
    assert author['status'] == 'complete' and author['scope'] == inp
    assert author['coefficient_order'] == ['a','b','c']
    assert author['all_parameter_degree_bound'] == [2,2,2]
    assert author['coefficient_polynomials'] == [encode(poly) for poly in triple]
    assert author['grid_rows'] == rows
    assert author['prime3_solutions'] == solutions
    assert not integer_targets and author['integer_target_witnesses_in_cube'] == []
    assert not solutions
    result = {
        'status': 'complete', 'scope': inp,
        'methods': ['all5040 signed permutations over Z[t,x,y,z]',
                    'separate univariate permutation determinant at each of27 integer points',
                    'formal coefficient derivatives at all27 points modulo3',
                    'manual obstruction polynomial identity over F3'],
        'symbolic_permutation_count': 5040,
        'per_grid_point_permutation_count': 5040,
        'full_symbolic_pencil': [encode(poly) for poly in full],
        'coefficient_order': ['a','b','c'],
        'coefficient_polynomials': [encode(poly) for poly in triple],
        'grid_rows': rows,
        'all27_jacobians_mod3': jacobians,
        'prime3_solutions': solutions,
        'integer_target_points_in_cube': integer_targets,
        'manual_sum_polynomial_mod3': encode(total),
        'manual_candidates_after_sum_and_a': manual_points,
        'manual_b_residuals': manual_b,
        'author_payload_agreement': True,
        'nonblind_shared_python_runtime': True,
        'no_author_mathematical_helpers_imported': True,
    }
    check()
    payload = (json.dumps(result, indent=2) + '\n').encode('utf-8')
    assert len(payload) <= CAP_OUTPUT - 65536
    OUT.mkdir(parents=True, exist_ok=True)
    pending = OUT / 'verification.pending'
    pending.write_bytes(payload)
    check()
    pending.replace(OUT / 'verification.json')
    check()
    print(json.dumps({'status':'complete', 'symbolic_permutations':5040,
                      'integer_pencils':27, 'mod3_jacobians':27,
                      'prime3_solutions':len(solutions), 'author_payload_agreement':True}))
    return 0


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
        raise RuntimeError("verifier output already exists; do not overwrite a prior run implicitly")
    start = time.monotonic()
    kernel, job, limits = make_job()
    process = None
    try:
        process = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--worker"],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, creationflags=subprocess.CREATE_NO_WINDOW,
                                   env={**os.environ,"OPENBLAS_NUM_THREADS":"1","OMP_NUM_THREADS":"1",
                                        "MKL_NUM_THREADS":"1","NUMEXPR_NUM_THREADS":"1"})
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
                  "verifier_stdout": stdout, "verifier_stderr": stderr,
                  "completed_result_files": sorted(p.name for p in OUT.glob("verification.json")),
                  "parent_monitor_excluded_from_worker_memory_limit": True}
        OUT.mkdir(parents=True, exist_ok=True)
        payload = (json.dumps(result, indent=2) + "\n").encode("utf-8")
        used = sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
        if used + len(payload) > CAP_OUTPUT:
            raise RuntimeError("reserved execution-status output would exceed cap")
        (OUT / "execution.json").write_bytes(payload)
        if time.monotonic() - start > CAP_SECONDS:
            result["status"] = "wall_time_stop_preservation"
            result["wall_seconds"] = time.monotonic() - start
            (OUT / "execution.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
            print(json.dumps(result, indent=2))
            return 2
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
