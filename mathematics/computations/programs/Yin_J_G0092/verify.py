"""Independent exact reconstruction of J92, fixed n=4,...,10 only.

Authored by the separately assigned noncontributor reviewer.  No author helper
is imported.  Even/odd-position matching and quotient-coordinate fibers replace
the author's contiguous-half matching and digit-perturbation edge enumeration.
One supervisor execution; existing verification outputs cause refusal.
"""
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import ctypes
from ctypes import wintypes
import json
import os
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'verify.py').parent
POLYNOMIAL = (1, -1, -1, -1, 1)
DOMAIN = tuple(range(4, 11))
OWN_OUTPUTS = (
    "verification.json", "verification.pending.json", "verification-progress.json",
    "verification-failure.json",
)
START = 0.0
COMPLETED = []
PEAK = 0


# Public metadata uses logical locators; actual subprocess/file paths stay resolved.
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


def _record_path(value):
    try:
        return Path(value).resolve().relative_to(_J_ROOT).as_posix()
    except ValueError:
        return '<external-location>'


def _record_command(values):
    result = []
    for value in values:
        option, separator, argument = value.partition('=')
        if separator and option.startswith('-') and Path(argument).is_absolute():
            result.append(option + '=' + _record_path(argument))
        else:
            result.append('python' if value == sys.executable else
                          _record_path(value) if Path(value).is_absolute() else value)
    return result


def need(ok, message):
    if not ok:
        raise AssertionError(message)


def save(name, value):
    (((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


class ProcessMemory(ctypes.Structure):
    _fields_ = [
        ("cb", wintypes.DWORD), ("faults", wintypes.DWORD),
        ("peak_working_set", ctypes.c_size_t), ("working_set", ctypes.c_size_t),
        ("peak_paged", ctypes.c_size_t), ("paged", ctypes.c_size_t),
        ("peak_nonpaged", ctypes.c_size_t), ("nonpaged", ctypes.c_size_t),
        ("pagefile", ctypes.c_size_t), ("peak_pagefile", ctypes.c_size_t),
    ]


def guard():
    global PEAK
    need(os.name == "nt", "This declared resource monitor requires Windows")
    need(time.monotonic() - START <= 115, "115-second worker limit")
    memory = ProcessMemory()
    memory.cb = ctypes.sizeof(memory)
    handle = ctypes.windll.kernel32.GetCurrentProcess
    handle.restype = wintypes.HANDLE
    query = ctypes.windll.psapi.GetProcessMemoryInfo
    query.argtypes = [wintypes.HANDLE, ctypes.POINTER(ProcessMemory), wintypes.DWORD]
    query.restype = wintypes.BOOL
    need(bool(query(handle(), ctypes.byref(memory), memory.cb)), "Memory query failed")
    PEAK = max(PEAK, int(memory.working_set))
    need(memory.working_set <= 512 * 1024 * 1024, "512 MiB working-set limit")


def monomial_remainder(degree):
    """Generic descending monic polynomial division of t^degree by P."""
    coefficients = [0] * (degree + 1)
    coefficients[degree] = 1
    for top in range(degree, 3, -1):
        factor = coefficients[top]
        for j, entry in enumerate(POLYNOMIAL):
            coefficients[top - 4 + j] -= factor * entry
    return tuple((coefficients + [0] * 4)[:4])


def linear_remainder(word, vectors):
    return tuple(sum(digit * vector[j] for digit, vector in zip(word, vectors))
                 for j in range(4))


def low_end_quotient(word):
    """Constant term 1 determines quotient successively from LOW degree."""
    coefficients = list(word)
    quotient = []
    for low in range(len(word) - 4):
        factor = coefficients[low]
        quotient.append(factor)
        for j, entry in enumerate(POLYNOMIAL):
            coefficients[low + j] -= factor * entry
    need(not any(coefficients), "Independent low-end quotient has nonzero tail")
    expanded = [sum(quotient[j] * POLYNOMIAL[k - j]
                    for j in range(max(0, k - 4), min(k + 1, len(quotient))))
                for k in range(len(word))]
    need(expanded == list(word), "Independent convolution failed")
    return tuple(quotient)


def reconstruct(n):
    need(3 ** n <= 60000, "Halfword cap")
    length, sites = 2 * n, 2 * n - 4
    powers = [monomial_remainder(j) for j in range(length)]
    odds = defaultdict(list)
    contiguous_endpoints = set()
    enumerated = mass = 0
    for index, word in enumerate(product((-1, 0, 1), repeat=n)):
        if index % 1024 == 0:
            guard()
        odds[linear_remainder(word, powers[1::2])].append(word)
        contiguous_endpoints.add(linear_remainder(word, powers[:n]))
        enumerated += 1
        mass += 2 ** word.count(0)
    need(enumerated == 3 ** n and mass == 4 ** n, "Complete halfword law")
    returned = set()
    for index, even in enumerate(product((-1, 0, 1), repeat=n)):
        if index % 1024 == 0:
            guard()
        target = tuple(-x for x in linear_remainder(even, powers[::2]))
        for odd in odds.get(target, ()):
            word = tuple(digit for pair in zip(even, odd) for digit in pair)
            need(word not in returned, "Duplicate parity reconstruction")
            need(linear_remainder(word, powers) == (0, 0, 0, 0), "Full original return")
            returned.add(word)
            need(len(returned) <= 100000, "Returned-vertex cap")
    words = sorted(returned)
    del odds, returned
    quotients = [low_end_quotient(word) for word in words]
    need(len(set(quotients)) == len(words), "Quotient injection")
    weights = [2 ** word.count(0) for word in words]
    neighbors = [set() for _ in words]
    parent = list(range(len(words)))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for site in range(sites):
        guard()
        fibers = defaultdict(list)
        for i, quotient in enumerate(quotients):
            fibers[quotient[:site] + quotient[site + 1:]].append(i)
        for fiber in fibers.values():
            need(len(fiber) <= 3, "One-coordinate fiber has more than three legal states")
            for i, j in combinations(fiber, 2):
                delta = quotients[j][site] - quotients[i][site]
                need(delta in (-2, -1, 1, 2), "Coordinate jump exceeds exact interval")
                for k in range(length):
                    expected = delta * POLYNOMIAL[k - site] if site <= k <= site + 4 else 0
                    need(words[j][k] - words[i][k] == expected, "Fiber edge differs from shifted P")
                neighbors[i].add(j)
                neighbors[j].add(i)
                parent[root(j)] = root(i)
        need(sum(map(len, neighbors)) <= 5000000, "Directed-neighbor cap")
    groups = defaultdict(list)
    for i in range(len(words)):
        groups[root(i)].append(i)
    member_lists = sorted(groups.values(), key=lambda members: members[0])
    component_ids = [None] * len(words)
    components = []
    for component_id, members in enumerate(member_lists):
        for i in members:
            component_ids[i] = component_id
        components.append({
            "id": component_id, "members": members, "size": len(members),
            "original_integer_mass": sum(weights[i] for i in members),
            "representative": members[0],
        })
    isolated = [i for i, adjacent in enumerate(neighbors) if not adjacent]
    for i, word in enumerate(words):
        if i % 128 == 0:
            guard()
        frozen = True
        for site in range(sites):
            signed = [POLYNOMIAL[r] * word[site + r] for r in range(5)]
            lower, upper = -1 - min(signed), 1 - max(signed)
            need(lower <= 0 <= upper, "Current word outside its interval")
            frozen = frozen and lower == upper == 0
        need(frozen == (not neighbors[i]), "Signed interval and coordinate-fiber graph disagree")
    zero_id = words.index((0,) * length)
    need(neighbors[zero_id], "Zero word has no neighbor")
    zero_component = components[component_ids[zero_id]]
    summary = {
        "n": n, "original_word_length": length, "quotient_sites": sites,
        "halfwords": 3 ** n, "half_endpoint_count": len(contiguous_endpoints),
        "returned_words": len(words), "original_integer_mass": sum(weights),
        "unconditional_denominator": 4 ** length,
        "undirected_edges": sum(map(len, neighbors)) // 2,
        "components": len(components), "isolated_vertices": len(isolated),
        "zero_component_size": zero_component["size"],
        "zero_component_integer_mass": zero_component["original_integer_mass"],
    }
    vertices = [{
        "id": i, "word": list(word), "quotient": list(quotients[i]),
        "original_integer_weight": weights[i], "component": component_ids[i],
        "neighbors": sorted(neighbors[i]),
    } for i, word in enumerate(words)]
    need(sum(c["original_integer_mass"] for c in components) == sum(weights), "Component mass partition")
    return {"summary": summary, "vertices": vertices, "components": components,
            "isolated_vertex_ids": isolated, "zero_vertex_id": zero_id}


def first_difference(left, right, path="payload"):
    if type(left) is not type(right):
        return path + ": differing type"
    if isinstance(left, dict):
        if left.keys() != right.keys():
            return path + ": differing keys"
        for key in left:
            if left[key] != right[key]:
                return first_difference(left[key], right[key], path + "." + str(key))
    elif isinstance(left, list):
        if len(left) != len(right):
            return path + ": differing length"
        for i, (a, b) in enumerate(zip(left, right)):
            if a != b:
                return first_difference(a, b, path + "[" + str(i) + "]")
    elif left != right:
        return path + ": independent=" + repr(left) + ", author=" + repr(right)
    return "equal"


def worker():
    global START
    START = time.monotonic()
    author = json.loads(((_J_OUTPUT / 'result.json')).read_text(encoding="utf-8"))
    need(author["status"] == "complete" and author["scope_n"] == list(DOMAIN), "Author domain/status")
    need(author["P_ascending"] == list(POLYNOMIAL), "Author original polynomial")
    need(author["digit_probabilities"] == ["1/4", "1/2", "1/4"], "Author original law")
    need(len(author["results"]) == len(DOMAIN), "Author row count")
    rebuilt = []
    for n, original in zip(DOMAIN, author["results"]):
        independent = reconstruct(n)
        need(independent == original, first_difference(independent, original, "n=" + str(n)))
        rebuilt.append(independent)
        COMPLETED.append(n)
        save("verification-progress.json", {"status": "partial", "completed_n": COMPLETED,
                                           "summaries": [r["summary"] for r in rebuilt]})
        print(json.dumps(independent["summary"], sort_keys=True), flush=True)
    guard()
    result = {'status': 'complete', 'scope_n': list(DOMAIN), 'P_ascending': list(POLYNOMIAL), 'digit_probabilities': ['1/4', '1/2', '1/4'], 'method': 'Independent even/odd residue matching, low-end division, quotient-fiber cliques, union-find', 'comparison': 'Every mathematical result-row field equals author output; no author helper imported', 'results': rebuilt}
    save("verification.pending.json", result)
    guard()
    (_J_OUTPUT / 'verification.pending.json').replace((_J_OUTPUT / 'verification.json'))
    (_J_OUTPUT / 'verification-progress.json').unlink()
    print("COMPLETE independent exact n=4..10 graph reconstruction and all-payload comparison", flush=True)


def supervisor():
    command = [sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'verify.py'), '--worker']
    try:
        process = subprocess.run(command, cwd=_J_PROGRAM, timeout=120,
                                 text=True, encoding="utf-8", capture_output=True)
    except subprocess.TimeoutExpired as error:
        (_J_OUTPUT / "verification-failure.json").write_text(
            json.dumps({"status": "timeout", "completed_output": False}) + "\n", encoding="utf-8")
        print(str(error), file=sys.stderr)
        return 124
    if process.stdout:
        print(process.stdout, end="")
    if process.stderr:
        print(process.stderr, end="", file=sys.stderr)
    if process.returncode:
        return process.returncode
    payload = json.loads((_J_OUTPUT / 'verification.json').read_text(encoding="utf-8"))
    assert payload["status"].startswith("complete") or payload["status"].startswith("independent")
    return 0



if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        try:
            worker()
        except Exception as error:
            save("verification-failure.json", {
                "status": "failed", "kind": type(error).__name__, "message": _record_text(str(error)),
                "completed_n": COMPLETED, "traceback": _record_text(traceback.format_exc()),
            })
            raise
    else:
        need(not sys.argv[1:], "No scope override permitted")
        raise SystemExit(supervisor())
