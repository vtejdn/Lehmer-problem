"""Independent reconstruction for J93, only n=7,8,9,10. NOT RUN.

New reviewer implementation: parity enumeration, outside-word partitions,
union-find components, quadratic trace-ring norms, and quotient-based paths.
Never imports the author's program, J92 helpers, or mathematical payloads as
generation oracles. Requires a new specific ONE-run confirmation from root.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, lcm
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

BASE = (_J_PROGRAM / 'verify.py').parent
POLY = (1, -1, -1, -1, 1)
SIZES = (7, 8, 9, 10)
WORK_SECONDS = 115
TOTAL_SECONDS = 120
MEMORY_CAP = 512 * 1024 * 1024
JSON_CAP = 64 * 1024 * 1024
CAPS = {"halfwords": 60000, "vertices": 100000,
        "global_fibers": 100000, "directed_conditional_entries": 5000000,
        "aggregated_directed_entries": 5000000}
INPUT_NAMES = ("main.py", "result.json")
OUTPUT_NAMES = ("verification.json", "verification.pending.json",
                "verification.writing.json", "verification_progress.json",
                "verification_failure.json")
BEGAN = None
PEAK = 0
PHASE = {"phase": "not run"}
DONE = []
SAVED = []
COMPARED = 0
ZERO = (0, 0, 0, 0)


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


def insist(condition, detail):
    if not condition:
        raise AssertionError(detail)


def memory_bytes():
    from ctypes import wintypes
    class MemoryInfo(ctypes.Structure):
        _fields_ = [("size", wintypes.DWORD), ("faults", wintypes.DWORD),
                    ("peak", ctypes.c_size_t), ("working", ctypes.c_size_t),
                    ("paged_peak", ctypes.c_size_t), ("paged", ctypes.c_size_t),
                    ("nonpaged_peak", ctypes.c_size_t), ("nonpaged", ctypes.c_size_t),
                    ("pagefile", ctypes.c_size_t), ("pagefile_peak", ctypes.c_size_t)]
    handle = ctypes.windll.kernel32.GetCurrentProcess
    handle.restype = wintypes.HANDLE
    query = ctypes.windll.psapi.GetProcessMemoryInfo
    query.argtypes = [wintypes.HANDLE, ctypes.POINTER(MemoryInfo), wintypes.DWORD]
    query.restype = wintypes.BOOL
    info = MemoryInfo()
    info.size = ctypes.sizeof(info)
    insist(bool(query(handle(), ctypes.byref(info), info.size)), "Working-set query failed")
    return max(int(info.peak), int(info.working))


def guard(**details):
    global PEAK
    PHASE.update(details)
    insist(BEGAN is not None, "Verifier clock not initialized")
    insist(time.monotonic() - BEGAN <= WORK_SECONDS, "115-second verifier deadline")
    PEAK = max(PEAK, memory_bytes())
    insist(PEAK <= MEMORY_CAP, "512 MiB verifier memory limit")


def note(name, value):
    (((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def checkpoint(payload):
    guard(phase="serialize independent checkpoint")
    written = 0
    stream = json.JSONEncoder(ensure_ascii=True, separators=(",", ":")).iterencode(payload)
    with (_J_OUTPUT / 'verification.writing.json').open("w", encoding="utf-8", newline="\n") as out:
        for index, fragment in enumerate(stream):
            if index % 8192 == 0:
                guard(serialization_chunks=index, serialization_bytes=written)
            written += len(fragment)
            insist(written < JSON_CAP, "Independent JSON exceeds 64 MiB")
            out.write(fragment)
        out.write("\n")
    guard(serialization_bytes=written + 1)
    (_J_OUTPUT / 'verification.writing.json').replace(_J_OUTPUT / 'verification.pending.json')


def compare(expected, observed, path):
    """Reject extra/omitted keys as well as any unequal mathematical leaf."""
    global COMPARED
    COMPARED += 1
    if COMPARED % 16384 == 0:
        guard(phase="compare every retained mathematical field", comparison_nodes=COMPARED)
    if isinstance(expected, dict):
        insist(isinstance(observed, dict) and set(expected) == set(observed),
               "Object-key mismatch at " + path)
        for key, value in expected.items():
            compare(value, observed[key], path + "." + key)
    elif isinstance(expected, (list, tuple)):
        insist(isinstance(observed, list) and len(expected) == len(observed),
               "List mismatch at " + path)
        for index, (left, right) in enumerate(zip(expected, observed)):
            compare(left, right, path + "[" + str(index) + "]")
    else:
        insist(type(expected) is type(observed) and expected == observed,
               "Mismatch at " + path + ": expected " + repr(expected)[:180]
               + ", observed " + repr(observed)[:180])


def rational(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def pair_json(pair):
    return [rational(value) for value in pair]


def divide(coefficients):
    """Ordinary HIGH-end monic polynomial division, keeping the full quotient."""
    rem = list(coefficients)
    if len(rem) < 4:
        rem += [0] * (4 - len(rem))
    quotient = [0] * max(0, len(rem) - 4)
    for top in range(len(rem) - 1, 3, -1):
        leading = rem[top]
        quotient[top - 4] = leading
        for j in range(5):
            rem[top - 4 + j] -= leading * POLY[j]
    insist(not any(rem[4:]), "Monic division retained a high remainder")
    return tuple(rem[:4]), quotient


def multiply(left, right):
    coeff = [0] * 7
    for i in range(4):
        for j in range(4):
            coeff[i + j] += left[i] * right[j]
    return divide(coeff)[0]


def expand(quotient, length):
    coeff = [0] * length
    insist(len(quotient) == length - 4, "Quotient length")
    for i, value in enumerate(quotient):
        for j in range(5):
            coeff[i + j] += value * POLY[j]
    return tuple(coeff)


def powers():
    forward = [divide([0] * exponent + [1])[0] for exponent in range(21)]
    inverse = tuple(-POLY[j] // POLY[0] for j in range(1, 5))
    insist(multiply(forward[1], inverse) == (1, 0, 0, 0), "Original unit inverse")
    backwards = [(1, 0, 0, 0)]
    for _ in range(10):
        backwards.append(multiply(backwards[-1], inverse))
    return forward, backwards


def evaluate(word, basis, stride=1, offset=0):
    result = [0, 0, 0, 0]
    for i, digit in enumerate(word):
        if digit:
            row = basis[stride * i + offset]
            for axis in range(4):
                result[axis] += digit * row[axis]
    return tuple(result)


def trace_multiply(a, b):
    # In Z[u], u^2=u+3; no author's inverse-power norm table is used.
    return (a[0] * b[0] + 3 * a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] + a[1] * b[1])


def neutral_square(value):
    # z^2=u*z-1 and z^3=(u+2)*z-u give value=A(u)+z*B(u).
    a = (value[0] - value[2], -value[3])
    b = (value[1] + 2 * value[3], value[2] + value[3])
    aa, bb = trace_multiply(a, a), trace_multiply(b, b)
    cross = trace_multiply((0, 1), trace_multiply(a, b))
    return tuple(aa[j] + bb[j] + cross[j] for j in range(2))


def neutral_sign(pair):
    x = 2 * Fraction(pair[0]) + Fraction(pair[1])
    y = -Fraction(pair[1])
    if y == 0:
        return (x > 0) - (x < 0)
    if x == 0 or (x > 0) == (y > 0):
        return (y > 0) - (y < 0)
    gap = x * x - 13 * y * y
    insist(gap != 0, "Nonrational radical falsely rational")
    return ((gap > 0) - (gap < 0)) * ((x > 0) - (x < 0))


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def all_returns(n, basis):
    insist(3 ** n <= CAPS["halfwords"], "Halfword cap")
    even, odd = defaultdict(list), defaultdict(list)
    contiguous_endpoints = set()
    total_mass = 0
    count = 0
    for word in product((-1, 0, 1), repeat=n):
        if count % 512 == 0:
            guard(phase="independent parity halfwords", n=n, counter=count)
        even[evaluate(word, basis, 2)].append(word)
        odd[evaluate(word, basis, 2, 1)].append(word)
        contiguous_endpoints.add(evaluate(word, basis))
        total_mass += 2 ** word.count(0)
        count += 1
    insist(count == 3 ** n and total_mass == 4 ** n, "Complete parity halfword law")
    found = {}
    for index, (key, right_words) in enumerate(odd.items()):
        if index % 512 == 0:
            guard(phase="independent parity return matching", n=n, counter=index)
        for left in even.get(tuple(-x for x in key), ()):
            for right in right_words:
                full = tuple(digit for pair in zip(left, right) for digit in pair)
                insist(full not in found, "Duplicate parity return")
                insist(divide(full)[0] == ZERO, "False full original return")
                found[full] = 2 ** full.count(0)
                insist(len(found) <= CAPS["vertices"], "Returned vertex cap")
    insist((0,) * (2 * n) in found, "Zero word missing")
    return sorted(found), found, len(contiguous_endpoints)


def all_local(basis):
    groups = defaultdict(list)
    for word in product((-1, 0, 1), repeat=6):
        groups[divide(word)[0]].append(word)
    insist(sum(map(len, groups.values())) == 729, "Local word completeness")
    result, lookup = [], {}
    for identifier, key in enumerate(sorted(groups)):
        words = sorted(groups[key])
        mass = sum(2 ** word.count(0) for word in words)
        records = [{"digits": word, "zero_count": word.count(0),
                    "weight": 2 ** word.count(0),
                    "conditional_probability": rational(Fraction(2 ** word.count(0), mass))}
                   for word in words]
        result.append({"id": identifier, "endpoint_basis": key,
                       "weight_sum": mass, "words": records})
        lookup[key] = (identifier, words, mass)
    insist(sum(row["weight_sum"] for row in result) == 4 ** 6, "Local original mass")
    return result, lookup


def moments(members, weights, midpoints, squares):
    mass = sum(weights[i] for i in members)
    mean = tuple(sum(weights[i] * midpoints[i][j] for i in members) for j in range(4))
    second = tuple(sum(weights[i] * squares[i][j] for i in members) for j in range(2))
    mean_square = neutral_square(mean)
    # Centered integer vectors provide an independent variance calculation.
    centered = [0, 0]
    for i in members:
        delta = tuple(mass * midpoints[i][j] - mean[j] for j in range(4))
        square = neutral_square(delta)
        for axis in range(2):
            centered[axis] += weights[i] * square[axis]
    insist(all(value % mass == 0 for value in centered), "Centered variance denominator")
    variance = tuple(value // mass for value in centered)
    insist(variance == tuple(mass * second[j] - mean_square[j] for j in range(2)),
           "Centered moment identity")
    insist(neutral_sign(variance) >= 0, "Negative exact variance")
    return {"weight_mass": mass, "midpoint_mean_numerator_basis": mean,
            "midpoint_mean_denominator": mass,
            "midpoint_second_moment_numerator_u_pair": second,
            "midpoint_second_moment_denominator": mass,
            "midpoint_mean_square_numerator_u_pair": mean_square,
            "midpoint_mean_square_denominator": mass * mass,
            "midpoint_variance_numerator_u_pair": variance,
            "midpoint_variance_denominator": mass * mass}


def witness_paths(n, ids, weights, midpoints, squares, memberships, fibers, rows, component_ids):
    length = 2 * n
    m = (length - 8) // 5
    padding = length - 8 - 5 * m
    leading, trailing = min(2, padding), padding - min(2, padding)
    quotient = [0] * (length - 4)
    quotient[leading] += 1
    quotient[leading + 3] += 1
    for a in range(m):
        for shift, coefficient in ((0, -1), (1, 1), (4, 1)):
            quotient[leading + 4 + 5 * a + shift] += coefficient
    core = ((0,) * leading + (1, -1, -1, 0)
            + (-1, 1, -1, 1, -1) * m + (0, -1, -1, 1) + (0,) * trailing)
    insist(expand(quotient, length) == core, "Independent core quotient")
    zero_id = ids[(0,) * length]
    paths = []
    for sign in (1, -1):
        q = [sign * value for value in quotient]
        word = expand(q, length)
        first = ids[word]
        states, steps = [first], []
        event = Fraction(1)
        operations = [("transport", leading + 3 + 5 * a,
                       ((0, -1), (1, 1)), Fraction(1, 2)) for a in range(m)]
        operations.append(("cap", leading + 5 * m + 2, ((1, -1),), Fraction(2, 3)))
        operations += [("erase", leading + 5 * a, ((0, -1),), Fraction(8, 9))
                       for a in range(m, -1, -1)]
        for kind, start, differences, prescribed in operations:
            guard(phase="independent quotient path", n=n, path_sign=sign, path_kind=kind)
            source = ids[word]
            for offset, change in differences:
                q[start + offset] += sign * change
            target_word = expand(q, length)
            insist(set(target_word) <= {-1, 0, 1} and target_word in ids, "Illegal quotient path")
            insist(word[:start] == target_word[:start]
                   and word[start + 6:] == target_word[start + 6:], "Path changed outside block")
            target = ids[target_word]
            insist(target != source and 0 <= start <= length - 6, "Path interval/nontriviality")
            fid = memberships[source][start]
            fiber = fibers[fid]
            insist(target in fiber["members"], "Path target not in independent fiber")
            conditional = Fraction(weights[target], fiber["full_weight_mass"])
            insist(conditional == prescribed, "C76 path conditional probability")
            selected = conditional / (length - 5)
            insist(rows[source][target] >= selected, "Path aggregated transition")
            insist(weights[source] >= weights[first], "Path original mass")
            insist(component_ids[source] == component_ids[zero_id], "Path zero component")
            steps.append({"kind": kind, "source": source, "target": target,
                          "block_start": start, "fiber_id": fid,
                          "conditional_probability": rational(conditional),
                          "selected_interval_transition_probability": rational(selected),
                          "aggregated_transition_probability": rational(rows[source][target]),
                          "source_zero_count": word.count(0),
                          "target_zero_count": target_word.count(0)})
            states.append(target)
            event *= selected
            word = target_word
        insist(word == (0,) * length and len(states) == len(set(states)), "Complete path")
        insist(len(steps) == 2 * m + 2, "Path length")
        expected_event = (Fraction(1, length - 5) ** (2 * m + 2)
                          * Fraction(1, 2) ** m * Fraction(2, 3) * Fraction(8, 9) ** (m + 1))
        insist(event == expected_event and weights[first] == 2 ** (2 + padding), "Path full law")
        phase_norm = ((5, -2), (2, -1), (7, -3), (7, -3), (2, -1))[n % 5]
        insist(squares[first] == phase_norm, "C76 path true midpoint")
        paths.append({"sign": sign, "initial_vertex": first, "state_ids": states,
                      "steps": steps, "specified_event_probability": rational(event),
                      "initial_original_weight": weights[first],
                      "initial_midpoint_basis": midpoints[first],
                      "initial_midpoint_norm_u_pair": squares[first]})
    insist(set(paths[0]["state_ids"]) & set(paths[1]["state_ids"]) == {zero_id}, "Signed paths")
    return {"m": m, "padding": padding, "leading_zeros": leading,
            "trailing_zeros": trailing, "path_length": 2 * m + 2, "paths": paths}


def reconstruct(n, basis, inverse_basis, local_lookup):
    words, weight_map, contiguous_count = all_returns(n, basis)
    ids = {word: index for index, word in enumerate(words)}
    weights = [weight_map[word] for word in words]
    count, length, clock = len(words), 2 * n, 2 * n - 5
    total = sum(weights)
    zero_id = ids[(0,) * length]
    midpoints, squares, quotients, negatives = [], [], [], []
    for index, word in enumerate(words):
        if index % 128 == 0:
            guard(phase="independent vertex arithmetic", n=n, counter=index)
        remainder, quotient = divide(word)
        insist(remainder == ZERO and expand(quotient, length) == word, "Full quotient identity")
        prefix = divide(word[:n])[0]
        midpoint = tuple(-value for value in multiply(inverse_basis[n], prefix))
        insist(midpoint == divide(word[n:])[0], "Independent true midpoint identity")
        square = neutral_square(midpoint)
        insist(neutral_sign(square) >= 0 and ((square == (0, 0)) == (midpoint == ZERO)),
               "Neutral square positivity/injectivity")
        midpoints.append(midpoint)
        squares.append(square)
        quotients.append(quotient)
        negatives.append(ids[tuple(-value for value in word)])
    memberships = [[None] * clock for _ in words]
    rows = [defaultdict(Fraction) for _ in words]
    parents = list(range(count))

    def root(vertex):
        while parents[vertex] != vertex:
            parents[vertex] = parents[parents[vertex]]
            vertex = parents[vertex]
        return vertex

    def unite(left, right):
        a, b = root(left), root(right)
        if a != b:
            parents[max(a, b)] = min(a, b)

    fibers = []
    conditional_count = 0
    fiber_energy = [Fraction(0), Fraction(0)]
    for start in range(clock):
        # Independently partition ALL full returns by their actual outside word.
        partitions = defaultdict(list)
        for index, word in enumerate(words):
            partitions[word[:start] + word[start + 6:]].append(index)
        for outside, members in sorted(partitions.items(), key=lambda item: item[1][0]):
            if len(fibers) % 256 == 0:
                guard(phase="outside-word partitions", n=n, start=start, fibers=len(fibers))
            key = divide(words[members[0]][start:start + 6])[0]
            local_id, local_words, local_mass = local_lookup[key]
            actual_blocks = [words[index][start:start + 6] for index in members]
            insist(actual_blocks == local_words, "Full outside partition lacks a local alternative")
            mass = sum(weights[index] for index in members)
            outside_weight = 2 ** outside.count(0)
            insist(mass == outside_weight * local_mass, "Outside original mass factor")
            fid = len(fibers)
            insist(fid < CAPS["global_fibers"], "Global fiber cap")
            targets = [[index, *rational(Fraction(weights[index], mass))] for index in members]
            fibers.append({"id": fid, "block_start": start, "outside_digits": outside,
                           "relative_endpoint_basis": key, "local_fiber_id": local_id,
                           "members": members, "outside_original_weight": outside_weight,
                           "local_weight_sum": local_mass, "full_weight_mass": mass,
                           "stationary_mass": rational(Fraction(mass, total)),
                           "conditional_targets": targets})
            conditional_count += len(members) ** 2
            insist(conditional_count <= CAPS["directed_conditional_entries"], "Conditional cap")
            variance_numerator = [0, 0]
            for position, source in enumerate(members):
                insist(memberships[source][start] is None, "Duplicate outside membership")
                memberships[source][start] = fid
                unite(members[0], source)
                for target in members:
                    rows[source][target] += Fraction(weights[target], mass * clock)
                # Pairwise differences, independent of the author's moment subtraction.
                for target in members[position + 1:]:
                    square = neutral_square(subtract(midpoints[source], midpoints[target]))
                    for axis in range(2):
                        variance_numerator[axis] += weights[source] * weights[target] * square[axis]
            for axis in range(2):
                fiber_energy[axis] += Fraction(variance_numerator[axis], mass * total * clock)
    insist(all(None not in membership for membership in memberships), "Outside membership complete")
    insist(sum(len(f["members"]) for f in fibers) == count * clock, "Fiber incidence count")
    entries = sum(map(len, rows))
    insist(entries <= CAPS["aggregated_directed_entries"], "Aggregated entry cap")
    directed = sum(len(row) - 1 for row in rows)
    matrix_energy = [Fraction(0), Fraction(0)]
    for source, row in enumerate(rows):
        if source % 64 == 0:
            guard(phase="all independent transition rows", n=n, counter=source)
        insist(sum(row.values(), Fraction(0)) == 1 and row.get(source, 0) > 0, "Kernel row law")
        insist(weights[source] == weights[negatives[source]], "Sign-reflected mass")
        insist(midpoints[negatives[source]] == tuple(-x for x in midpoints[source]), "Midpoint sign")
        for target, probability in row.items():
            insist(probability > 0, "Nonpositive transition")
            insist(weights[source] * probability == weights[target] * rows[target].get(source, 0),
                   "Original detailed balance")
            insist(rows[negatives[source]].get(negatives[target], 0) == probability, "Kernel sign")
            square = neutral_square(subtract(midpoints[target], midpoints[source]))
            for axis in range(2):
                matrix_energy[axis] += Fraction(weights[source], 2 * total) * probability * square[axis]
    insist(directed % 2 == 0 and matrix_energy == fiber_energy, "Graph symmetry/independent energies")
    lower = (Fraction(6, 1024 * clock), Fraction(-2, 1024 * clock))
    upper = (Fraction(38, clock), Fraction(0))
    insist(neutral_sign(subtract(matrix_energy, lower)) >= 0, "C76 lower energy bound")
    insist(neutral_sign(subtract(upper, matrix_energy)) >= 0, "C76 upper energy bound")

    partitions = defaultdict(list)
    for vertex in range(count):
        partitions[root(vertex)].append(vertex)
    groups = sorted(partitions.values(), key=lambda members: members[0])
    components, component_ids = [], [None] * count
    projection, residual = [Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]
    for identifier, members in enumerate(groups):
        guard(phase="independent component moments", n=n, component=identifier)
        for vertex in members:
            component_ids[vertex] = identifier
        moment = moments(members, weights, midpoints, squares)
        mass = moment["weight_mass"]
        components.append({"id": identifier, "members": members,
                           "representative": members[0], "vertex_count": len(members),
                           "stationary_mass": rational(Fraction(mass, total)), **moment})
        for axis in range(2):
            projection[axis] += Fraction(moment["midpoint_mean_square_numerator_u_pair"][axis], total * mass)
            residual[axis] += Fraction(moment["midpoint_variance_numerator_u_pair"][axis], total * mass)
    frozen = [i for i in range(count)
              if all(len(fibers[fid]["members"]) == 1 for fid in memberships[i])]
    insist(frozen == [i for i, row in enumerate(rows) if len(row) == 1], "Two frozen-state criteria")
    global_moment = moments(list(range(count)), weights, midpoints, squares)
    insist(global_moment["midpoint_mean_numerator_basis"] == ZERO, "Global original centering")
    second = tuple(Fraction(value, total)
                   for value in global_moment["midpoint_second_moment_numerator_u_pair"])
    insist(tuple(projection[j] + residual[j] for j in range(2)) == second, "Component decomposition")
    insist(neutral_sign(second) > 0, "Global true midpoint second moment")
    zero_component = components[component_ids[zero_id]]
    paths = witness_paths(n, ids, weights, midpoints, squares, memberships, fibers, rows, component_ids)
    vertices = [{"id": i, "digits": word, "zero_count": word.count(0), "weight": weights[i],
                 "quotient": quotients[i], "midpoint_basis": midpoints[i],
                 "midpoint_norm_u_pair": squares[i], "negative_vertex": negatives[i],
                 "component": component_ids[i], "fiber_by_block_start": memberships[i],
                 "transitions": [[target, *rational(probability)]
                                 for target, probability in sorted(rows[i].items())]}
                for i, word in enumerate(words)]
    summary = {"n": n, "N": length, "vertices": count, "original_integer_mass": total,
               "block_count": clock, "global_fibers": len(fibers),
               "directed_conditional_entries": conditional_count,
               "aggregated_directed_entries": entries,
               "undirected_nontrivial_edges": directed // 2,
               "components": len(components), "frozen_vertices": len(frozen),
               "zero_vertex": zero_id, "zero_component": zero_component["id"],
               "zero_component_size": zero_component["vertex_count"],
               "zero_component_mass": zero_component["weight_mass"],
               "midpoint_second_moment_u_pair": pair_json(second),
               "midpoint_dirichlet_energy_u_pair": pair_json(matrix_energy),
               "invariant_component_midpoint_energy_u_pair": pair_json(projection)}
    case = {"case_status": "complete finite case", "summary": summary,
            "unconditional_original_probability_denominator": 4 ** length,
            "fresh_halfwords": 3 ** n, "half_endpoint_fibers": contiguous_count,
            "vertices": vertices, "fibers": fibers, "components": components,
            "frozen_vertex_ids": frozen, "global_midpoint_moments": global_moment,
            "dirichlet_from_fibers_u_pair": pair_json(fiber_energy),
            "dirichlet_from_aggregated_matrix_u_pair": pair_json(matrix_energy),
            "component_centered_midpoint_energy_u_pair": pair_json(residual),
            "long_core_paths": paths}
    # Check the ACTUAL finite D33 interpretation only after reconstruction.
    w = (-1, 1, 0, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, 0, -1, 1)
    qw = (-1, 0, -1, -1, 0, -1, 0, 1, 0, 1, 1, 0, 1)
    insist(expand(qw, 17) == w, "D33 displayed frozen quotient")
    if n < 9:
        insist(not frozen and len(components) == 1 and projection == [0, 0], "D33 finite n7/8 claim")
    else:
        candidates = (w + (0,), (0,) + w) if n == 9 else ((0,) + w + (0, 0), (0, 0) + w + (0,))
        expected_words = set(candidates) | {tuple(-digit for digit in word) for word in candidates}
        insist({words[i] for i in frozen} == expected_words and len(components) == 5,
               "D33 exact finite frozen words and five components")
        for word, z in zip(candidates, ((-2, -1, 1, 0), (0, -2, -1, 1))):
            insist(midpoints[ids[word]] == z, "D33 frozen midpoint basis")
        insist(all(squares[i] == (4, -1) and weights[i] == (16 if n == 9 else 64)
                   for i in frozen), "D33 frozen norm and original mass")
        denominator = 104431 if n == 9 else 128731
        insist(projection == [Fraction(32, denominator), Fraction(-8, denominator)],
               "D33 exact finite invariant midpoint energy")
        insist(zero_component["midpoint_mean_numerator_basis"] == ZERO, "D33 main component centering")
    return case


def worker():
    global BEGAN
    BEGAN = time.monotonic()
    try:
        guard(phase="read frozen author input artifacts")
        originals = {name: (((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)).read_bytes() for name in INPUT_NAMES}
        insist(len(originals["result.json"]) <= JSON_CAP, "Author payload input size cap")
        author = json.loads(originals["result.json"])
        expected_keys = {"status", "author_role", "domain", "arithmetic", "enumeration", "reuse_limit",
                         "proof_interface", "structural_caps_per_n", "local_fibers",
                         "cases", "limits", "checked_n"}
        insist(set(author) == expected_keys, "Unexpected top-level author schema")
        insist(author["status"] == "complete finite author computation; not independent verification",
               "Author result completion status")
        insist(len(author["cases"]) == 4 and author["checked_n"] == list(SIZES), "Author result scope")
        domain = {"P_low_to_high": POLY, "n": SIZES, "N": "2*n", "digits": [-1, 0, 1],
                  "original_digit_weights": [1, 2, 1], "original_digit_denominator": 4,
                  "interval_rule": "uniform among N-5 six-digit intervals",
                  "conditional_rule": "all same-endpoint words at weight 2^zeros",
                  "neutral_u": "(1-sqrt(13))/2", "u_squared": "u+3", "local_word_count": 729}
        compare(domain, author["domain"], "domain")
        compare(CAPS, author["structural_caps_per_n"], "structural_caps_per_n")
        basis, inverse_basis = powers()
        local, lookup = all_local(basis)
        compare(local, author["local_fibers"], "local_fibers")
        payload = {'status': 'incomplete independent verification', 'domain': domain, 'method': 'parity enumeration; outside partitions; trace-ring norms; union-find; quotient paths', 'role': 'separate noncontributor reconstruction, not author crosscheck', 'source_inputs': [{'name': name, 'bytes': len(data)} for name, data in originals.items()], 'structural_caps_per_n': CAPS, 'local_fibers': local, 'cases': [], 'comparison': {'every_mathematical_field': False, 'checked_n': []}, 'limits': ['ONLY n7--10 and all729 local words; no expanded domain', 'No mathematical floats, source-helper import, spectral solve or retry', 'Finite verification does not prove all-n connectivity or asymptotic behavior']}
        checkpoint(payload)
        for index, n in enumerate(SIZES):
            case = reconstruct(n, basis, inverse_basis, lookup)
            compare(case, author["cases"][index], "cases[" + str(index) + "]")
            payload["cases"].append(case)
            DONE.append(n)
            payload["comparison"].update({"checked_n": list(DONE), "compared_nodes": COMPARED})
            checkpoint(payload)
            SAVED[:] = DONE
            note('verification_progress.json', {'status': 'incomplete', 'checked_n': list(DONE), 'successfully_checkpointed_n': list(SAVED), 'phase': dict(PHASE)})
            print(json.dumps({"independently_compared_case": case["summary"]}), flush=True)
        for name, original in originals.items():
            insist((((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)).read_bytes() == original, "Author input modified during verification: " + name)
        insist(tuple(DONE) == SIZES, "Incomplete independent domain")
        payload["status"] = "complete independent finite reconstruction; every mathematical field matched"
        payload['comparison'].update({'every_mathematical_field': True, 'compared_nodes': COMPARED, 'd33_exact_frozen_word_interpretation_checked': True})
        pass
        checkpoint(payload)
        guard(phase="publish independent canonical verification")
        insist(not ((_J_OUTPUT / 'verification.json')).exists(), "Independent result already exists")
        (_J_OUTPUT / 'verification.pending.json').replace((_J_OUTPUT / 'verification.json'))
        (_J_OUTPUT / "verification_progress.json").unlink(missing_ok=True)
        print("INDEPENDENT ALL-FIELD RECONSTRUCTION COMPLETE; finite scope only", flush=True)
        return 0
    except BaseException:
        failure = {'status': 'failed; no repair or automatic rerun', 'phase': dict(PHASE), 'checked_n_in_memory': list(DONE), 'successfully_checkpointed_n': list(SAVED), 'compared_nodes': COMPARED, 'traceback': _record_text(traceback.format_exc())}
        note("verification_failure.json", failure)
        note("verification_progress.json", failure)
        print(failure["traceback"], file=sys.stderr, flush=True)
        return 1


def supervisor():
    command = [sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'verify.py'), '--independent-worker']
    try:
        process = subprocess.run(command, cwd=_J_PROGRAM, timeout=120,
                                 text=True, encoding="utf-8", capture_output=True)
    except subprocess.TimeoutExpired as error:
        (_J_OUTPUT / "verification_failure.json").write_text(
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
    if sys.argv[1:] == ["--independent-worker"]:
        raise SystemExit(worker())
    raise SystemExit(supervisor())
