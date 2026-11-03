"""Exact full original-return update graphs, ONLY n=4,...,10.

Author exploration for D15. One bounded run after root confirmation.
No imported J91 helpers or outputs; C55 counts are secondary checks.
"""
from collections import defaultdict, deque
from itertools import product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import ctypes
import json
import os
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'main.py').parent
P = (1, -1, -1, -1, 1)
SCOPE = tuple(range(4, 11))
EXPECTED = {
    6: (75, 7296), 7: (201, 35120), 8: (547, 170848),
    9: (1481, 835448), 10: (4083, 4119392),
}
OUTPUTS = (
    "result.json", "result.pending.json", "progress.json",
    "failure.json",
)
START = None
COMPLETED = []
PEAK_OBSERVED_WORKING_SET = 0


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


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def write_json(name, data):
    (((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def working_set_bytes():
    require(os.name == "nt", "Declared resource monitor requires Windows")
    from ctypes import wintypes

    class Counters(ctypes.Structure):
        _fields_ = [
            ("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD),
            ("PeakWorkingSetSize", ctypes.c_size_t),
            ("WorkingSetSize", ctypes.c_size_t),
            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
            ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
            ("PagefileUsage", ctypes.c_size_t),
            ("PeakPagefileUsage", ctypes.c_size_t),
        ]

    current = ctypes.windll.kernel32.GetCurrentProcess
    current.restype = wintypes.HANDLE
    info = ctypes.windll.psapi.GetProcessMemoryInfo
    info.argtypes = [wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
    info.restype = wintypes.BOOL
    counters = Counters()
    counters.cb = ctypes.sizeof(counters)
    require(bool(info(current(), ctypes.byref(counters), counters.cb)),
            "Working-set query failed")
    return int(counters.WorkingSetSize)


def resources():
    global PEAK_OBSERVED_WORKING_SET
    require(time.monotonic() - START <= 115, "Worker 115-second deadline")
    memory = working_set_bytes()
    PEAK_OBSERVED_WORKING_SET = max(PEAK_OBSERVED_WORKING_SET, memory)
    require(memory <= 512 * 1024 * 1024, "512 MiB working-set cap")


def beta_times(value):
    a, b, c, d = value
    # beta^4 = -1 + beta + beta^2 + beta^3, ORIGINAL basis.
    return (-d, a + d, b + d, c + d)


def endpoint(word):
    value = (0, 0, 0, 0)
    for digit in reversed(word):
        a, b, c, d = beta_times(value)
        value = (a + digit, b, c, d)
    return value


def beta_power_times(value, n):
    for _ in range(n):
        value = beta_times(value)
    return value


def quotient(word):
    residual = list(word)
    result = [0] * (len(word) - 4)
    for degree in range(len(word) - 1, 3, -1):
        coefficient = residual[degree]
        result[degree - 4] = coefficient
        for j in range(5):
            residual[degree - 4 + j] -= coefficient * P[j]
    require(all(x == 0 for x in residual), "Nonzero original P remainder")
    expanded = [0] * len(word)
    for i, coefficient in enumerate(result):
        for j, p in enumerate(P):
            expanded[i + j] += coefficient * p
    require(tuple(expanded) == word, "Original quotient reconstruction")
    return tuple(result)


def returned_words(n):
    require(3 ** n <= 60000, "Declared halfword cap")
    by_endpoint = defaultdict(list)
    half_mass = 0
    for index, word in enumerate(product((-1, 0, 1), repeat=n)):
        if index % 1024 == 0:
            resources()
        weight = 1 << word.count(0)
        by_endpoint[endpoint(word)].append((word, weight))
        half_mass += weight
    require(sum(map(len, by_endpoint.values())) == 3 ** n,
            "Missing or duplicate original halfwords")
    require(half_mass == 4 ** n, "Original halfword probability mass")
    returned = {}
    for index, (high_endpoint, high_fiber) in enumerate(by_endpoint.items()):
        if index % 1024 == 0:
            resources()
        low_target = tuple(-x for x in beta_power_times(high_endpoint, n))
        for low, low_weight in by_endpoint.get(low_target, ()):
            for high, high_weight in high_fiber:
                word = low + high
                require(word not in returned, "Duplicate complete returned word")
                require(endpoint(word) == (0, 0, 0, 0), "Original full return")
                weight = low_weight * high_weight
                require(weight == 1 << word.count(0), "Original wholeword weight")
                returned[word] = weight
                require(len(returned) <= 100000, "Returned-vertex resource cap")
    require((0,) * (2 * n) in returned, "Zero return missing")
    if n in EXPECTED:
        require((len(returned), sum(returned.values())) == EXPECTED[n],
                "Secondary adopted C55 count/mass crosscheck")
    return returned, len(by_endpoint)


def graph_at(n):
    returned, endpoint_count = returned_words(n)
    words = sorted(returned)
    labels = {word: index for index, word in enumerate(words)}
    quotients = [quotient(word) for word in words]
    neighbors = []
    isolated = []
    directed_entries = 0
    sites = 2 * n - 4
    for index, word in enumerate(words):
        if index % 128 == 0:
            resources()
        adjacent = set()
        for site in range(sites):
            for delta in (-2, -1, 1, 2):
                candidate = list(word)
                for j in range(5):
                    candidate[site + j] += delta * P[j]
                if not all(-1 <= x <= 1 for x in candidate):
                    continue
                candidate = tuple(candidate)
                require(candidate in labels, "Legal move missing from complete return set")
                target = labels[candidate]
                changed_quotient = list(quotients[index])
                changed_quotient[site] += delta
                require(tuple(changed_quotient) == quotients[target],
                        "Move does not change exactly one quotient coordinate")
                adjacent.add(target)
        signed_frozen = all(
            min(P[j] * word[site + j] for j in range(5)) == -1 and
            max(P[j] * word[site + j] for j in range(5)) == 1
            for site in range(sites)
        )
        require(signed_frozen == (not adjacent), "Independent frozen-window criterion")
        neighbors.append(sorted(adjacent))
        directed_entries += len(adjacent)
        require(directed_entries <= 5000000, "Directed-neighbor resource cap")
        if not adjacent:
            isolated.append(index)
    for index, adjacent in enumerate(neighbors):
        for target in adjacent:
            require(index in neighbors[target], "Graph edge symmetry")
    require(directed_entries % 2 == 0, "Even directed-edge count")
    component_ids = [-1] * len(words)
    components = []
    for first in range(len(words)):
        if component_ids[first] >= 0:
            continue
        component_id = len(components)
        queue = deque([first])
        component_ids[first] = component_id
        members = []
        while queue:
            if len(members) % 128 == 0:
                resources()
            vertex = queue.popleft()
            members.append(vertex)
            for target in neighbors[vertex]:
                if component_ids[target] < 0:
                    component_ids[target] = component_id
                    queue.append(target)
        members.sort()
        components.append({
            "id": component_id, "members": members, "size": len(members),
            "original_integer_mass": sum(returned[words[i]] for i in members),
            "representative": members[0],
        })
    require(sum(row["size"] for row in components) == len(words), "Component partition")
    weight_total = sum(returned.values())
    require(sum(row["original_integer_mass"] for row in components) == weight_total,
            "Component original mass partition")
    zero_id = labels[(0,) * (2 * n)]
    zero_component = component_ids[zero_id]
    require(neighbors[zero_id], "Zero word unexpectedly frozen")
    summary = {
        "n": n, "original_word_length": 2 * n, "quotient_sites": sites,
        "halfwords": 3 ** n, "half_endpoint_count": endpoint_count,
        "returned_words": len(words), "original_integer_mass": weight_total,
        "unconditional_denominator": 4 ** (2 * n),
        "undirected_edges": directed_entries // 2,
        "components": len(components), "isolated_vertices": len(isolated),
        "zero_component_size": components[zero_component]["size"],
        "zero_component_integer_mass": components[zero_component]["original_integer_mass"],
    }
    vertices = [{
        "id": i, "word": list(word), "quotient": list(quotients[i]),
        "original_integer_weight": returned[word], "component": component_ids[i],
        "neighbors": neighbors[i],
    } for i, word in enumerate(words)]
    return {"summary": summary, "vertices": vertices, "components": components,
            "isolated_vertex_ids": isolated, "zero_vertex_id": zero_id}


def worker():
    global START
    START = time.monotonic()
    results = []
    for n in SCOPE:
        row = graph_at(n)
        results.append(row)
        COMPLETED.append(n)
        write_json("progress.json", {"status": "partial", "completed_n": COMPLETED,
                                    "summaries": [r["summary"] for r in results]})
        print(json.dumps(row["summary"], sort_keys=True), flush=True)
    resources()
    output = {'status': 'complete', 'scope_n': list(SCOPE), 'P_ascending': list(P), 'digit_probabilities': ['1/4', '1/2', '1/4'], 'arithmetic': 'Python exact integers; all original four-coordinate returns', 'results': results}
    write_json("result.pending.json", output)
    resources()
    (_J_OUTPUT / 'result.pending.json').replace((_J_OUTPUT / 'result.json'))
    ((_J_OUTPUT / 'progress.json')).unlink()
    print("COMPLETE exact n=4..10 connectivity scope", flush=True)


def supervisor():
    command = [sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'main.py'), '--worker']
    try:
        process = subprocess.run(command, cwd=_J_PROGRAM, timeout=120,
                                 text=True, encoding="utf-8", capture_output=True)
    except subprocess.TimeoutExpired as error:
        (_J_OUTPUT / "failure.json").write_text(
            json.dumps({"status": "timeout", "completed_output": False}) + "\n", encoding="utf-8")
        print(str(error), file=sys.stderr)
        return 124
    if process.stdout:
        print(process.stdout, end="")
    if process.stderr:
        print(process.stderr, end="", file=sys.stderr)
    if process.returncode:
        return process.returncode
    payload = json.loads((_J_OUTPUT / 'result.json').read_text(encoding="utf-8"))
    assert payload["status"].startswith("complete") or payload["status"].startswith("independent")
    return 0



if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        try:
            worker()
        except Exception as error:
            write_json("failure.json", {"status": "failed", "kind": type(error).__name__,
                                        "message": _record_text(str(error)), "completed_n": COMPLETED,
                                        "traceback": _record_text(traceback.format_exc())})
            raise
    else:
        require(not sys.argv[1:], "No scope override is permitted")
        raise SystemExit(supervisor())
