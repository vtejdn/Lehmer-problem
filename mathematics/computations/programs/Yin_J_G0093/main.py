"""Complete original six-digit heat-bath graphs, ONLY n=7,8,9,10.

AUTHOR program for D33. NOT RUN at preparation. One bounded invocation only
after root reads the declaration and complete code and specifically confirms.
No J92 payload/helper imports: its accepted counts are secondary crosschecks.
All mathematical decisions use integers/Fraction; time/memory are operational.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product
from math import gcd
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
SCOPE = (7, 8, 9, 10)
EXPECTED = {7: (201, 35120), 8: (547, 170848),
            9: (1481, 835448), 10: (4083, 4119392)}
OUTPUTS = ("result.json", "result.pending.json", "result.writing.json",
           "progress.json", "failure.json")
CAP_HALFWORDS = 60000
CAP_VERTICES = 100000
CAP_FIBERS = 100000
CAP_CONDITIONAL_ENTRIES = 5000000
CAP_AGGREGATED_ENTRIES = 5000000
CAP_JSON_BYTES = 64 * 1024 * 1024
CAP_WORKING_SET = 512 * 1024 * 1024
WORKER_SECONDS = 115
SUPERVISOR_SECONDS = 120
START = None
PEAK_MEMORY = 0
STAGE = {"stage": "not started", "n": None}
COMPLETED = []
ZERO4 = (0, 0, 0, 0)
INVERSE_POWERS = ((1, 0, 0, 0), (1, 1, 1, -1),
                  (2, 2, 0, -1), (4, 2, 1, -2))
X = (0, -1, 1, -1, 1, -1)
Y = (-1, 1, 1, -1, -1, 0)
CAP0 = (-1, 0, 0, -1, -1, 1)
CAP1 = (-1, -1, 1, 0, 0, 0)


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


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def small_json(name, data):
    (((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def working_set_bytes():
    require(os.name == "nt", "Declared resource monitor requires Windows")
    from ctypes import wintypes

    class Counters(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD),
                    ("PeakWorkingSetSize", ctypes.c_size_t),
                    ("WorkingSetSize", ctypes.c_size_t),
                    ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                    ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                    ("PagefileUsage", ctypes.c_size_t),
                    ("PeakPagefileUsage", ctypes.c_size_t)]

    current = ctypes.windll.kernel32.GetCurrentProcess
    current.restype = wintypes.HANDLE
    query = ctypes.windll.psapi.GetProcessMemoryInfo
    query.argtypes = [wintypes.HANDLE, ctypes.POINTER(Counters), wintypes.DWORD]
    query.restype = wintypes.BOOL
    counters = Counters()
    counters.cb = ctypes.sizeof(counters)
    require(bool(query(current(), ctypes.byref(counters), counters.cb)),
            "Windows memory query failed")
    return max(int(counters.WorkingSetSize), int(counters.PeakWorkingSetSize))


def resources(**stage):
    global PEAK_MEMORY
    STAGE.update(stage)
    require(START is not None, "Worker clock not initialized")
    require(time.monotonic() - START <= WORKER_SECONDS,
            "Worker 115-second deadline: " + repr(STAGE))
    memory = working_set_bytes()
    PEAK_MEMORY = max(PEAK_MEMORY, memory)
    require(memory <= CAP_WORKING_SET,
            "512 MiB working-set cap: " + repr(STAGE))


def checkpoint(payload):
    """Stream a complete checkpoint, retaining the older one until success."""
    resources(stage="serialize checkpoint")
    encoder = json.JSONEncoder(ensure_ascii=True, separators=(",", ":"))
    written = 0
    with (_J_OUTPUT / 'result.writing.json').open("w", encoding="utf-8", newline="\n") as out:
        for index, chunk in enumerate(encoder.iterencode(payload)):
            if index % 4096 == 0:
                resources(serialization_chunks=index, serialization_bytes=written)
            written += len(chunk)  # ensure_ascii means character count is bytes.
            require(written < CAP_JSON_BYTES, "64 MiB JSON payload cap")
            out.write(chunk)
        out.write("\n")
    resources(serialization_bytes=written + 1)
    (_J_OUTPUT / 'result.writing.json').replace(_J_OUTPUT / 'result.pending.json')


def pack(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def pack_pair(value):
    return [pack(value[0]), pack(value[1])]


def beta_times(value):
    a, b, c, d = value
    return (-d, a + d, b + d, c + d)


def beta_inverse_times(value):
    a, b, c, d = value
    return (a + b, a + c, a + d, -a)


def endpoint(word):
    value = ZERO4
    for digit in reversed(word):
        a, b, c, d = beta_times(value)
        value = (a + digit, b, c, d)
    return value


def field_product(left, right):
    coefficients = [0] * 7
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            coefficients[i + j] += a * b
    for degree in range(6, 3, -1):
        coefficient = coefficients[degree]
        for j, p in enumerate(P):
            coefficients[degree - 4 + j] -= coefficient * p
    require(coefficients[4:] == [0, 0, 0], "Field reduction tail")
    return tuple(coefficients[:4])


def norm_u(value):
    """Exact neutral |value(zeta)|^2=A+B*u, u=(1-sqrt(13))/2."""
    reflected = tuple(sum(value[i] * INVERSE_POWERS[i][j] for i in range(4))
                      for j in range(4))
    square = field_product(value, reflected)
    b = square[2]
    a = square[0] - b
    require(square[1] == 2 * b and square[3] == -b,
            "Reciprocal-fixed subfield coordinates: " + repr((value, square)))
    require(sign_u((a, b)) >= 0, "Negative exact neutral square")
    require(((a, b) == (0, 0)) == (value == ZERO4),
            "Neutral embedding injectivity/zero test")
    return (a, b)


def sign_u(value):
    a, b = map(Fraction, value)
    x, y = 2 * a + b, -b  # twice the value is x+y*sqrt(13).
    denominator = x.denominator * y.denominator // gcd(x.denominator, y.denominator)
    x = x.numerator * (denominator // x.denominator)
    y = y.numerator * (denominator // y.denominator)
    if not y:
        return (x > 0) - (x < 0)
    if not x:
        return (y > 0) - (y < 0)
    if x > 0 and y > 0:
        return 1
    if x < 0 and y < 0:
        return -1
    comparison = x * x - 13 * y * y if x > 0 else 13 * y * y - x * x
    return (comparison > 0) - (comparison < 0)


def midpoint(word, n):
    value = tuple(-x for x in endpoint(word[:n]))
    for _ in range(n):
        value = beta_inverse_times(value)
    require(value == endpoint(word[n:]), "True midpoint prefix/right-half identity")
    return value


def quotient(word):
    """Low-end monic-constant recurrence, with full reconstruction."""
    result = [0] * (len(word) - 4)
    for i in range(len(result)):
        result[i] = word[i] - sum(P[j] * result[i - j]
                                  for j in range(1, 5) if i >= j)
    expanded = [0] * len(word)
    for i, a in enumerate(result):
        for j, p in enumerate(P):
            expanded[i + j] += a * p
    require(tuple(expanded) == word, "Full original P quotient reconstruction")
    return result


def enumerate_returns(n):
    require(3 ** n <= CAP_HALFWORDS, "Halfword structural cap")
    halves = defaultdict(list)
    half_mass = 0
    for index, word in enumerate(product((-1, 0, 1), repeat=n)):
        if index % 512 == 0:
            resources(stage="fresh halfword enumeration", n=n, counter=index)
        weight = 1 << word.count(0)
        halves[endpoint(word)].append((word, weight))
        half_mass += weight
    require(sum(len(v) for v in halves.values()) == 3 ** n, "All halfwords retained")
    require(half_mass == 4 ** n, "Original halfword mass")
    returned = {}
    for index, (high_endpoint, high_words) in enumerate(halves.items()):
        if index % 512 == 0:
            resources(stage="full return matching", n=n, counter=index)
        shifted = high_endpoint
        for _ in range(n):
            shifted = beta_times(shifted)
        low_words = halves.get(tuple(-x for x in shifted), ())
        for low, low_weight in low_words:
            for high, high_weight in high_words:
                word = low + high
                require(word not in returned, "Duplicate complete return")
                require(endpoint(word) == ZERO4, "False original field return")
                weight = low_weight * high_weight
                require(weight == 1 << word.count(0), "Full original word weight")
                returned[word] = weight
                require(len(returned) <= CAP_VERTICES, "Returned-vertex structural cap")
    require((len(returned), sum(returned.values())) == EXPECTED[n],
            "Secondary accepted J92 count/mass mismatch at n=" + str(n))
    require((0,) * (2 * n) in returned, "All-zero return missing")
    return returned, len(halves)


def local_fibers():
    buckets = defaultdict(list)
    for index, word in enumerate(product((-1, 0, 1), repeat=6)):
        if index % 128 == 0:
            resources(stage="complete local six-digit fibers", counter=index)
        buckets[endpoint(word)].append(word)
    require(sum(map(len, buckets.values())) == 729, "Local table is not complete")
    require(sum(1 << w.count(0) for words in buckets.values() for w in words) == 4 ** 6,
            "Local original weight mass")
    require(set(buckets[endpoint(X)]) == {X, Y}, "D31 exact transport fiber")
    require(endpoint(X) == (0, 0, 0, -2), "D31 nonzero transport endpoint")
    require(set(buckets[endpoint(CAP0)]) == {CAP0, CAP1}, "D31 exact cap fiber")
    require(endpoint(CAP0) == (-1, -1, 1, 0), "D31 nonzero cap endpoint")
    zero_words = {(0,) * 6, P + (0,), tuple(-x for x in P) + (0,),
                  (0,) + P, (0,) + tuple(-x for x in P)}
    require(set(buckets[ZERO4]) == zero_words, "D31 entire zero fiber")
    records, lookup = [], {}
    for identifier, key in enumerate(sorted(buckets)):
        words = sorted(buckets[key])
        weights = [1 << word.count(0) for word in words]
        mass = sum(weights)
        record = {"id": identifier, "endpoint_basis": key, "weight_sum": mass,
                  "words": [{"digits": w, "zero_count": w.count(0), "weight": q,
                             "conditional_probability": pack(Fraction(q, mass))}
                            for w, q in zip(words, weights)]}
        records.append(record)
        lookup[key] = (identifier, words, weights, mass)
    require(lookup[ZERO4][3] == 72, "Zero fiber mass72")
    require(lookup[endpoint(X)][3] == 4, "Transport fiber mass4")
    require(lookup[endpoint(CAP0)][3] == 12, "Cap fiber mass12")
    return records, lookup


def weighted_moments(members, weights, midpoints, norms):
    mass = sum(weights[i] for i in members)
    mean = tuple(sum(weights[i] * midpoints[i][j] for i in members) for j in range(4))
    second = tuple(sum(weights[i] * norms[i][j] for i in members) for j in range(2))
    mean_square = norm_u(mean)
    variance = tuple(mass * second[j] - mean_square[j] for j in range(2))
    require(sign_u(variance) >= 0, "Negative exact weighted midpoint variance")
    return {"weight_mass": mass, "midpoint_mean_numerator_basis": mean,
            "midpoint_mean_denominator": mass,
            "midpoint_second_moment_numerator_u_pair": second,
            "midpoint_second_moment_denominator": mass,
            "midpoint_mean_square_numerator_u_pair": mean_square,
            "midpoint_mean_square_denominator": mass * mass,
            "midpoint_variance_numerator_u_pair": variance,
            "midpoint_variance_denominator": mass * mass}


def long_core_paths(n, words, word_ids, weights, midpoints, norms,
                    memberships, fibers, rows, component_ids, zero_id):
    length = 2 * n
    m = (length - 8) // 5
    padding = length - (8 + 5 * m)
    left = min(2, padding)
    right = padding - left
    core = (1, -1, -1, 0) + (-1, 1, -1, 1, -1) * m + (0, -1, -1, 1)
    positive = (0,) * left + core + (0,) * right
    expected_norm = ((5, -2), (2, -1), (7, -3), (7, -3), (2, -1))[n % 5]
    expected_event = (Fraction(1, length - 5) ** (2 * m + 2)
                      * Fraction(1, 2) ** m * Fraction(2, 3)
                      * Fraction(8, 9) ** (m + 1))
    paths = []
    for sign in (1, -1):
        current = tuple(sign * d for d in positive)
        require(current in word_ids, "D31 initial original core missing")
        initial_id = word_ids[current]
        initial_weight = weights[initial_id]
        require(initial_weight == 1 << (2 + padding), "D31 original core weight")
        require(norms[initial_id] == expected_norm, "D31 true midpoint phase norm")
        state_ids = [initial_id]
        steps = []
        event = Fraction(1)

        def advance(start, old, new, expected_probability, kind):
            nonlocal current, event
            old = tuple(sign * d for d in old)
            new = tuple(sign * d for d in new)
            require(0 <= start <= length - 6, "D31 actual block start")
            require(current[start:start + 6] == old,
                    "D31 actual path substring " + repr((n, sign, kind, start, current)))
            successor = current[:start] + new + current[start + 6:]
            require(successor in word_ids, "D31 legal successor absent from full graph")
            source, target = word_ids[current], word_ids[successor]
            require(source != target, "D31 nontrivial step became self-loop")
            fiber = fibers[memberships[source][start]]
            probabilities = {entry[0]: Fraction(entry[1], entry[2])
                             for entry in fiber["conditional_targets"]}
            require(target in probabilities, "D31 successor absent from complete fiber")
            probability = probabilities[target]
            require(probability == expected_probability, "D31 exact conditional probability")
            chosen_probability = probability / (length - 5)
            require(rows[source].get(target, Fraction(0)) >= chosen_probability,
                    "Aggregated transition below chosen interval contribution")
            require(weights[source] >= initial_weight, "D31 path mass fell below original")
            require(component_ids[source] == component_ids[zero_id],
                    "D31 path outside zero component")
            steps.append({"kind": kind, "source": source, "target": target,
                          "block_start": start, "fiber_id": fiber["id"],
                          "conditional_probability": pack(probability),
                          "selected_interval_transition_probability": pack(chosen_probability),
                          "aggregated_transition_probability": pack(rows[source][target]),
                          "source_zero_count": current.count(0),
                          "target_zero_count": successor.count(0)})
            event *= chosen_probability
            current = successor
            state_ids.append(target)

        for a in range(m):
            advance(left + 3 + 5 * a, X, Y, Fraction(1, 2), "transport")
            require(current.count(0) == 2 + padding, "Transport zero count")
        advance(left + 5 * m + 2, CAP0, CAP1, Fraction(2, 3), "cap")
        require(current.count(0) == 3 + padding, "Cap zero count")
        for a in range(m, -1, -1):
            advance(left + 5 * a, P + (0,), (0,) * 6, Fraction(8, 9), "erase")
        require(current == (0,) * length, "D31 path did not end at zero")
        require(len(steps) == 2 * m + 2, "D31 actual path length")
        require(len(set(state_ids)) == len(state_ids), "D31 path repeated a vertex")
        require(event == expected_event, "D31 fully paid event probability")
        paths.append({"sign": sign, "initial_vertex": initial_id, "state_ids": state_ids,
                      "steps": steps, "specified_event_probability": pack(event),
                      "initial_original_weight": initial_weight,
                      "initial_midpoint_basis": midpoints[initial_id],
                      "initial_midpoint_norm_u_pair": norms[initial_id]})
    require(set(paths[0]["state_ids"]) & set(paths[1]["state_ids"]) == {zero_id},
            "D31 signed paths share a nonzero state")
    return {"m": m, "padding": padding, "leading_zeros": left, "trailing_zeros": right,
            "path_length": 2 * m + 2, "paths": paths}


def build_case(n, local_lookup):
    resources(stage="begin full case", n=n)
    returned, half_fiber_count = enumerate_returns(n)
    words = sorted(returned)
    word_ids = {word: i for i, word in enumerate(words)}
    weights = [returned[word] for word in words]
    full_mass = sum(weights)
    length, block_count, vertex_count = 2 * n, 2 * n - 5, len(words)
    zero_id = word_ids[(0,) * length]
    midpoints, norms, quotients, negative_ids = [], [], [], []
    for i, word in enumerate(words):
        if i % 128 == 0:
            resources(stage="exact original vertex data", n=n, counter=i)
        z = midpoint(word, n)
        midpoints.append(z)
        norms.append(norm_u(z))
        quotients.append(quotient(word))
        negated = tuple(-d for d in word)
        require(negated in word_ids, "Original sign partner missing")
        negative_ids.append(word_ids[negated])
    for i, partner in enumerate(negative_ids):
        require(weights[i] == weights[partner], "Original sign weights disagree")
        require(midpoints[partner] == tuple(-z for z in midpoints[i]),
                "Original true midpoint sign symmetry")

    memberships = [[None] * block_count for _ in words]
    rows = [defaultdict(Fraction) for _ in words]
    fibers = []
    conditional_entries = 0
    entry_operations = 0
    dirichlet_fibers = [Fraction(0), Fraction(0)]
    for start in range(block_count):
        seen_outside = set()
        for i, word in enumerate(words):
            if i % 128 == 0:
                resources(stage="complete six-digit graph fibers", n=n,
                          block_start=start, counter=i, fibers=len(fibers))
            outside = word[:start] + word[start + 6:]
            if outside in seen_outside:
                continue
            seen_outside.add(outside)
            key = endpoint(word[start:start + 6])
            local_id, alternatives, local_weights, local_mass = local_lookup[key]
            member_words = [word[:start] + alternative + word[start + 6:]
                            for alternative in alternatives]
            require(all(w in word_ids for w in member_words),
                    "A complete endpoint-fiber replacement is missing from return enumeration")
            members = [word_ids[w] for w in member_words]
            require(members == sorted(set(members)), "Fiber members/order duplicated")
            outside_weight = 1 << outside.count(0)
            fiber_mass = sum(weights[j] for j in members)
            require(fiber_mass == outside_weight * local_mass, "Full fiber original mass")
            require(all(weights[j] == outside_weight * q
                        for j, q in zip(members, local_weights)), "Fiber probability factors")
            conditional_entries += len(members) ** 2
            require(conditional_entries <= CAP_CONDITIONAL_ENTRIES,
                    "Directed conditional-entry structural cap")
            identifier = len(fibers)
            require(identifier < CAP_FIBERS, "Global-fiber structural cap")
            target_probabilities = [(j, Fraction(q, local_mass))
                                    for j, q in zip(members, local_weights)]
            record = {"id": identifier, "block_start": start, "outside_digits": outside,
                      "relative_endpoint_basis": key, "local_fiber_id": local_id,
                      "members": members, "outside_original_weight": outside_weight,
                      "local_weight_sum": local_mass, "full_weight_mass": fiber_mass,
                      "stationary_mass": pack(Fraction(fiber_mass, full_mass)),
                      "conditional_targets": [[j, probability.numerator, probability.denominator]
                                              for j, probability in target_probabilities]}
            fibers.append(record)
            moment = weighted_moments(members, weights, midpoints, norms)
            variance = moment["midpoint_variance_numerator_u_pair"]
            for axis in range(2):
                dirichlet_fibers[axis] += Fraction(variance[axis],
                                                 fiber_mass * full_mass * block_count)
            for source in members:
                require(memberships[source][start] is None, "Duplicate vertex/block membership")
                memberships[source][start] = identifier
                for target, probability in target_probabilities:
                    rows[source][target] += probability / block_count
                    entry_operations += 1
                    if entry_operations % 2048 == 0:
                        resources(stage="all exact conditional transitions", n=n,
                                  counter=entry_operations)
    require(entry_operations == conditional_entries, "Conditional entry accounting")
    require(all(all(x is not None for x in membership) for membership in memberships),
            "Missing vertex/block fiber")
    require(sum(len(f["members"]) for f in fibers) == vertex_count * block_count,
            "Complete vertex/block incidence count")

    aggregated_entries = sum(len(row) for row in rows)
    require(aggregated_entries <= CAP_AGGREGATED_ENTRIES, "Aggregated-transition structural cap")
    directed_edges = 0
    dirichlet_rows = [Fraction(0), Fraction(0)]
    for source, row in enumerate(rows):
        if source % 64 == 0:
            resources(stage="row sums balance and true midpoint energy", n=n, counter=source)
        require(sum(row.values(), Fraction(0)) == 1, "Exact kernel row sum")
        require(row.get(source, Fraction(0)) > 0, "Positive conditional self-transition missing")
        for target, probability in row.items():
            require(probability > 0, "Nonpositive retained transition")
            require(weights[source] * probability == weights[target] * rows[target].get(source, 0),
                    "Complete original detailed balance")
            require(rows[negative_ids[source]].get(negative_ids[target], 0) == probability,
                    "Exact full-kernel sign symmetry")
            if target != source:
                directed_edges += 1
            if target > source and midpoints[source] != midpoints[target]:
                difference = tuple(midpoints[target][j] - midpoints[source][j] for j in range(4))
                square = norm_u(difference)
                for axis in range(2):
                    dirichlet_rows[axis] += Fraction(weights[source], full_mass) * probability * square[axis]
    require(directed_edges % 2 == 0, "Undirected graph symmetry count")
    require(dirichlet_rows == dirichlet_fibers, "Two exact midpoint Dirichlet computations disagree")
    lower = (Fraction(6, 1024 * block_count), Fraction(-2, 1024 * block_count))
    upper = (Fraction(38, block_count), Fraction(0))
    require(sign_u(tuple(dirichlet_rows[j] - lower[j] for j in range(2))) >= 0,
            "D31 original-clock midpoint energy lower bound")
    require(sign_u(tuple(upper[j] - dirichlet_rows[j] for j in range(2))) >= 0,
            "D31 arbitrary-endpoint midpoint energy upper bound")

    components, component_ids = [], [None] * vertex_count
    projection = [Fraction(0), Fraction(0)]
    residual = [Fraction(0), Fraction(0)]
    for seed in range(vertex_count):
        if component_ids[seed] is not None:
            continue
        identifier = len(components)
        queue, members = deque([seed]), []
        component_ids[seed] = identifier
        while queue:
            source = queue.popleft()
            members.append(source)
            if len(members) % 256 == 0:
                resources(stage="complete components", n=n, counter=len(members))
            for target in rows[source]:
                if component_ids[target] is None:
                    component_ids[target] = identifier
                    queue.append(target)
        members.sort()
        moment = weighted_moments(members, weights, midpoints, norms)
        mass = moment["weight_mass"]
        for axis in range(2):
            projection[axis] += Fraction(moment["midpoint_mean_square_numerator_u_pair"][axis],
                                         full_mass * mass)
            residual[axis] += Fraction(moment["midpoint_variance_numerator_u_pair"][axis],
                                       full_mass * mass)
        components.append({"id": identifier, "members": members,
                           "representative": members[0], "vertex_count": len(members),
                           "stationary_mass": pack(Fraction(mass, full_mass)), **moment})
    require(sum(c["vertex_count"] for c in components) == vertex_count, "Component partition count")
    require(sum(c["weight_mass"] for c in components) == full_mass, "Complete component masses")
    frozen = [i for i, row in enumerate(rows) if len(row) == 1]
    zero_component = components[component_ids[zero_id]]
    global_moment = weighted_moments(list(range(vertex_count)), weights, midpoints, norms)
    require(global_moment["midpoint_mean_numerator_basis"] == ZERO4, "Original global midpoint centering")
    second = tuple(Fraction(a, full_mass)
                   for a in global_moment["midpoint_second_moment_numerator_u_pair"])
    require(tuple(projection[j] + residual[j] for j in range(2)) == second,
            "Full component midpoint decomposition")
    require(sign_u(second) > 0, "True original midpoint second moment vanished")
    paths = long_core_paths(n, words, word_ids, weights, midpoints, norms,
                            memberships, fibers, rows, component_ids, zero_id)
    vertices = []
    for i, word in enumerate(words):
        vertices.append({"id": i, "digits": word, "zero_count": word.count(0),
                         "weight": weights[i], "quotient": quotients[i],
                         "midpoint_basis": midpoints[i], "midpoint_norm_u_pair": norms[i],
                         "negative_vertex": negative_ids[i], "component": component_ids[i],
                         "fiber_by_block_start": memberships[i],
                         "transitions": [[target, value.numerator, value.denominator]
                                         for target, value in sorted(rows[i].items())]})
    summary = {"n": n, "N": length, "vertices": vertex_count, "original_integer_mass": full_mass,
               "block_count": block_count, "global_fibers": len(fibers),
               "directed_conditional_entries": conditional_entries,
               "aggregated_directed_entries": aggregated_entries,
               "undirected_nontrivial_edges": directed_edges // 2,
               "components": len(components), "frozen_vertices": len(frozen),
               "zero_vertex": zero_id, "zero_component": zero_component["id"],
               "zero_component_size": zero_component["vertex_count"],
               "zero_component_mass": zero_component["weight_mass"],
               "midpoint_second_moment_u_pair": pack_pair(second),
               "midpoint_dirichlet_energy_u_pair": pack_pair(dirichlet_rows),
               "invariant_component_midpoint_energy_u_pair": pack_pair(projection)}
    resources(stage="complete case checked", n=n)
    return {"case_status": "complete finite case", "summary": summary,
            "unconditional_original_probability_denominator": 4 ** length,
            "fresh_halfwords": 3 ** n, "half_endpoint_fibers": half_fiber_count,
            "vertices": vertices, "fibers": fibers, "components": components,
            "frozen_vertex_ids": frozen, "global_midpoint_moments": global_moment,
            "dirichlet_from_fibers_u_pair": pack_pair(dirichlet_fibers),
            "dirichlet_from_aggregated_matrix_u_pair": pack_pair(dirichlet_rows),
            "component_centered_midpoint_energy_u_pair": pack_pair(residual),
            "long_core_paths": paths}


def worker():
    global START
    START = time.monotonic()
    checkpointed = []
    try:
        resources(stage="worker initialization", n=None)
        local_records, local_lookup = local_fibers()
        payload = {'status': 'incomplete; only listed cases have passed all local checks', 'author_role': 'new author computation; not independent verification', 'domain': {'P_low_to_high': P, 'n': SCOPE, 'N': '2*n', 'digits': [-1, 0, 1], 'original_digit_weights': [1, 2, 1], 'original_digit_denominator': 4, 'interval_rule': 'uniform among N-5 six-digit intervals', 'conditional_rule': 'all same-endpoint words at weight 2^zeros', 'neutral_u': '(1-sqrt(13))/2', 'u_squared': 'u+3', 'local_word_count': 729}, 'arithmetic': 'integer and reduced Fraction; no mathematical floats', 'enumeration': 'fresh complete 3^n halfwords and all full-field matches', 'reuse_limit': 'J92 counts/masses secondary only; no imported payload/helper', 'proof_interface': 'C76 six-digit heat-bath theorem, original D31 body', 'structural_caps_per_n': {'halfwords': CAP_HALFWORDS, 'vertices': CAP_VERTICES, 'global_fibers': CAP_FIBERS, 'directed_conditional_entries': CAP_CONDITIONAL_ENTRIES, 'aggregated_directed_entries': CAP_AGGREGATED_ENTRIES}, 'local_fibers': local_records, 'cases': [], 'limits': ['ONLY n7,8,9,10 and the declared original-law kernel', 'No all-n connectivity, gap, mixing or diffusion conclusion', 'No independent native verification claimed']}
        checkpoint(payload)
        for n in SCOPE:
            case = build_case(n, local_lookup)
            payload["cases"].append(case)
            COMPLETED.append(n)
            payload["checked_n"] = list(COMPLETED)
            checkpoint(payload)
            checkpointed = list(COMPLETED)
            small_json('progress.json', {'status': 'incomplete', 'checked_n': COMPLETED, 'checkpointed_n': checkpointed, 'stage': dict(STAGE)})
            print(json.dumps({"completed_case": case["summary"]}), flush=True)
        require(tuple(COMPLETED) == SCOPE, "Complete declared n scope missing")
        resources(stage="all four cases checked", n=None)
        payload["status"] = "complete finite author computation; not independent verification"
        pass
        checkpoint(payload)
        resources(stage="publish complete canonical result", n=None)
        require(not ((_J_OUTPUT / 'result.json')).exists(), "Canonical output already exists")
        (_J_OUTPUT / 'result.pending.json').replace((_J_OUTPUT / 'result.json'))
        (_J_OUTPUT / "progress.json").unlink(missing_ok=True)
        print("ALL FOUR DECLARED CASES COMPLETE; author output only", flush=True)
        return 0
    except BaseException:
        diagnostic = _record_text(traceback.format_exc())
        failure = {'status': 'failed; no automatic retry', 'stage': dict(STAGE), 'checked_n_in_memory': list(COMPLETED), 'successfully_checkpointed_n': checkpointed, 'traceback': _record_text(diagnostic)}
        small_json("failure.json", failure)
        small_json("progress.json", failure)
        print(diagnostic, file=sys.stderr, flush=True)
        return 1


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
        raise SystemExit(worker())
    raise SystemExit(supervisor())
