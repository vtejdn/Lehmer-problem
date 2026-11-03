"""Independent C836 check: fixed H95, times0..512, midpoint256, cap500000.

No author mathematical modules are imported.  The unchanged earlier reviewer
module supplies only integral coordinate/transition maps, rational floor/ceil,
and its independently derived Chebyshev norm mark.  Its H48 calculation and
prior result are not run or imported as evidence.  New integer slicing and
original-coordinate graph searches enumerate this declared H95 scope; gathering
predecessors counts returns and zero-killed first returns independently of the
author's quotient scatter/renewal inversion.  The full midpoint vectors are
matched by states with the forward/backward reversal explicitly respected.
Memory stops: working set >=4GiB or available physical memory <1GiB; inability
to monitor also stops.  Checks are periodic, not an allocator hard limit.
Only a successful complete comparison atomically replaces the complete output.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import ctypes
import json
import os
import sys

from reviewer_midpoint_verify import (ZERO, floor, ceil, to_original,
    to_quotient, next_original, previous_original, norm_mark, ratio)

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'repository/config.json').is_file())
OUTPUT = ROOT / 'mathematics/computations/outputs' / HERE.name
H, LIMIT, MID, CAP, SCALE = 95, 512, 256, 500000, 10**6


def memory():
    if os.name != 'nt':
        raise RuntimeError('Windows live memory monitor required')
    class Global(ctypes.Structure):
        _fields_ = [('size', ctypes.c_ulong), ('load', ctypes.c_ulong)] + [
            (x, ctypes.c_ulonglong) for x in ('total', 'available', 'page_total',
                'page_available', 'virtual_total', 'virtual_available', 'extended')]
    class Process(ctypes.Structure):
        _fields_ = [('size', ctypes.c_ulong), ('faults', ctypes.c_ulong)] + [
            (x, ctypes.c_size_t) for x in ('peak', 'working', 'paged_peak', 'paged',
                'nonpaged_peak', 'nonpaged', 'page', 'page_peak')]
    kernel, psapi = ctypes.WinDLL('kernel32', use_last_error=True), ctypes.WinDLL('psapi', use_last_error=True)
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    kernel.GlobalMemoryStatusEx.argtypes = [ctypes.POINTER(Global)]
    psapi.GetProcessMemoryInfo.argtypes = [ctypes.c_void_p, ctypes.POINTER(Process), ctypes.c_ulong]
    global_status, process_status = Global(), Process()
    global_status.size, process_status.size = ctypes.sizeof(Global), ctypes.sizeof(Process)
    if not kernel.GlobalMemoryStatusEx(ctypes.byref(global_status)):
        raise OSError(ctypes.get_last_error(), 'GlobalMemoryStatusEx')
    if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(), ctypes.byref(process_status), process_status.size):
        raise OSError(ctypes.get_last_error(), 'GetProcessMemoryInfo')
    if process_status.working >= 4*1024**3 or global_status.available < 1024**3:
        raise RuntimeError('Declared memory stop reached')
    return {'working_set_bytes': process_status.working, 'available_physical_bytes': global_status.available}


def progress(stage, **kw):
    print(json.dumps({'stage': stage, **kw, **memory()}), flush=True)


def polynomial(x):
    return (((x-1)*x-1)*x-1)*x+1


def enumerate_original_states():
    lo, hi, root_low = Q(861, 500), Q(1723, 1000), Q(721, 200)
    assert polynomial(lo) < 0 < polynomial(hi)
    assert root_low**2 < 13
    assert (hi**2+1/lo)/((lo-1)*root_low*(lo-1/lo)) < Q(6, 5)
    assert 4/(13*(1+root_low)/2) < Q(11, 30)**2
    assert Q(6, 5)+Q(11, 30)*(LIMIT//2) == Q(1426, 15) < H+1
    strips = []
    grid = range(-H, H+1)
    for low, high, bound in ((lo, hi, 1/(lo-1)), (1/hi, 1/lo, lo/(lo-1))):
        assert low > Q(1, 2)
        endpoints = [(-1/low, -1/high), (low*low-low-1, high*high-high-1), (low-1, high-1)]
        intervals = [(floor(a*SCALE), ceil(b*SCALE)) for a, b in endpoints]
        tables = [[(min(q*a, q*b), max(q*a, q*b)) for q in grid] for a, b in intervals]
        strips.append((tables, ceil(bound*SCALE)))
    universe = set()
    for i, q0 in enumerate(grid):
        memory()
        for j, q1 in enumerate(grid):
            partial = [(tables[0][i][0]+tables[1][j][0],
                        tables[0][i][1]+tables[1][j][1], tables[2], bound)
                       for tables, bound in strips]
            for k, q2 in enumerate(grid):
                lower, upper = -H, H
                for left, right, last_table, bound in partial:
                    left += last_table[k][0]
                    right += last_table[k][1]
                    lower = max(lower, -((bound+right)//SCALE))
                    upper = min(upper, (bound-left)//SCALE)
                for q3 in range(lower, upper+1):
                    q = (q0, q1, q2, q3)
                    a = to_original(q)
                    assert to_quotient(a) == q
                    universe.add(a)
        if i % 32 == 0:
            progress('slice_enumeration', slices=i+1, total_slices=2*H+1, allowed=len(universe))
    return universe


def reach(universe, transition, label):
    found, stack, processed = {ZERO}, [ZERO], 0
    while stack:
        if processed % 4096 == 0:
            memory()
        a = stack.pop()
        processed += 1
        for digit in (-1, 0, 1):
            b = transition(a, digit)
            if b in universe and b not in found:
                if len(found) >= CAP:
                    raise RuntimeError('Declared reached-state cap reached')
                found.add(b)
                stack.append(b)
    progress(label, reached=len(found))
    return found


def step(values, rows):
    # Missing predecessor uses the final permanent zero sentinel.
    return [values[a]+2*values[b]+values[c] for a, b, c in rows]+[0]


def calculate():
    universe = enumerate_original_states()
    original_forward = reach(universe, next_original, 'original_forward_graph')
    quotient_forward = reach(universe, previous_original, 'quotient_forward_graph')
    states = sorted(original_forward & quotient_forward)
    graph = {'allowed_lattice_points': len(universe), 'original_forward_reached': len(original_forward),
             'forward_reached_states': len(quotient_forward), 'returning_graph_states': len(states),
             'height': H, 'full_box_states': (2*H+1)**4, 'cap': CAP}
    del universe, original_forward, quotient_forward
    indices = {a: i for i, a in enumerate(states)}
    zero, count = indices[ZERO], len(states)
    incoming, outgoing = [], []
    for i, a in enumerate(states):
        if i % 4096 == 0:
            memory()
        incoming.append(tuple(indices.get(previous_original(a, d), -1) for d in (-1, 0, 1)))
        outgoing.append(tuple(indices.get(next_original(a, d), -1) for d in (-1, 0, 1)))
    graph['retained_edges'] = sum(j >= 0 for row in outgoing for j in row)
    progress('graph_complete', **graph)
    values = [int(i == zero) for i in range(count)]+[0]
    killed, returns, firsts = values.copy(), [1], [0]
    for t in range(1, LIMIT+1):
        values, killed = step(values, incoming), step(killed, incoming)
        returns.append(values[zero])
        firsts.append(killed[zero])
        killed[zero] = 0
        assert returns[t] == sum(firsts[j]*returns[t-j] for j in range(1, t+1))
        if t == MID:
            midpoint_forward = values[:-1]
        if t % 16 == 0:
            progress('return_and_killed_first_return', time=t)
    del values, killed, incoming
    terminal = [int(i == zero) for i in range(count)]+[0]
    for t in range(1, MID+1):
        terminal = step(terminal, outgoing)
        assert terminal[zero] == returns[t]
        if t % 16 == 0:
            progress('terminal', time=t)
    del outgoing
    terminal.pop()
    sums, means, total, positive = [0, 0], [0]*4, 0, 0
    for i, (a, left, right) in enumerate(zip(states, midpoint_forward, terminal, strict=True)):
        if i % 4096 == 0:
            memory()
        weight = left*right
        if not weight:
            continue
        positive += 1
        total += weight
        mark = norm_mark(a)
        for k in (0, 1):
            sums[k] += weight*mark[k]
        q = to_quotient(a)
        for k in range(4):
            means[k] += weight*q[k]
    assert total == returns[LIMIT] and means == [0]*4
    sqrt_lo, sqrt_hi = Q(3605551275463989, 10**15), Q(3605551275463990, 10**15)
    assert sqrt_lo**2 < 13 < sqrt_hi**2
    aa, bb = (Q(v, 2*total) for v in sums)
    mlo, mhi = sorted((aa+bb*sqrt_lo, aa+bb*sqrt_hi))
    overlap = Q(total, returns[MID]**2)
    assert Q(36968603, SCALE) < overlap < Q(36968604, SCALE)
    assert Q(228798, SCALE) < mlo/MID < mhi/MID < Q(228799, SCALE)
    assert mlo > Q(MID, 5) and positive == 58669
    midpoint = {'midpoint_time': MID, 'total_time': LIMIT, 'complete_bridge_integer_weight': total,
        'positive_midpoint_states': positive, 'moment_integer_A_sum': sums[0], 'moment_integer_B_sum': sums[1],
        'moment_rational_part': ratio(aa), 'moment_sqrt13_part': ratio(bb), 'moment_lower': ratio(mlo),
        'moment_upper': ratio(mhi), 'scaled_moment_lower': ratio(mlo/MID), 'scaled_moment_upper': ratio(mhi/MID),
        'scaled_moment_rational_enclosure': [ratio(Q(228798, SCALE)), ratio(Q(228799, SCALE))],
        'overlap_D_n': ratio(overlap), 'overlap_rational_enclosure': [ratio(Q(36968603, SCALE)), ratio(Q(36968604, SCALE))],
        'zero_midpoint_probability': ratio(Q(returns[MID]**2, total)), 'weighted_quotient_coordinate_means': means}
    lo, hi = Q(861, 500), Q(1723, 1000)
    for _ in range(40):
        mid = (lo+hi)/2
        assert polynomial(mid)
        if polynomial(mid) < 0:
            lo = mid
        else:
            hi = mid
    assert polynomial(lo) < 0 < polynomial(hi)
    assert lo == Q(1893451168414823, 1099511627776000)
    assert hi == Q(236681396051853, 137438953472000)
    assert all(returns[t]*hi.numerator**t < (4*hi.denominator)**t for t in range(1, LIMIT+1))
    # Horner evaluation independently forms both complete finite first-return sums.
    pressure = []
    for root in (lo, hi):
        value = Q(0)
        for t in range(LIMIT, 0, -1):
            value = (value+firsts[t])*(root/4)
        pressure.append(value)
    assert Q(954048, SCALE) < pressure[0] < pressure[1] < Q(954049, SCALE) < 1
    p512 = Q(returns[LIMIT], 4**LIMIT)
    assert p512 == Q(5298548391970129745344684892772394289057669827956111368871272718708030755799876567240009996275901111428878134985202079634126536883620984644784010837788567749143910392852997044503323399, 2**1019)
    result = {'status': 'complete', 'scope': {'height': H, 'times_including_zero': [0, LIMIT],
        'midpoint_time': MID, 'reached_state_cap': CAP, 'digit_weights': [1, 2, 1], 'digit_denominator': 4,
        'reused_reviewer_helpers': 'reviewer_midpoint_verify.py:coordinate maps, transitions, floor/ceil, ratio, Chebyshev norm_mark',
        'working_set_stop_bytes': 4*1024**3, 'available_memory_floor_bytes': 1024**3},
        'graph': graph, 'complete_return_integer_weights': returns, 'complete_first_return_integer_weights': firsts,
        'midpoint': midpoint, 'pressure_beta_interval': [ratio(lo), ratio(hi)],
        'partial_first_return_at_beta_lower_bracket': ratio(pressure[0]),
        'partial_first_return_at_beta_upper_bracket': ratio(pressure[1]),
        'partial_first_return_beta_interval_display': [ratio(Q(954048, SCALE)), ratio(Q(954049, SCALE))],
        'selected_complete_returns': {str(t): ratio(Q(returns[t], 4**t)) for t in (128, 256, 512)},
        'all_times_fail_strict_pressure_crossing': True, 'partial_first_return_upper_is_below_one': True}
    progress('independent_values_complete', positive_midpoint_states=positive)
    return result, states, indices, midpoint_forward, terminal


def write_atomic(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(payload, separators=(',', ':'))+'\n', encoding='utf-8')
    temporary.replace(path)


def main():
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--author-input', type=Path, default=OUTPUT/'return_midpoint_512.json')
    parser.add_argument('--old-prefix-input', type=Path, default=OUTPUT/'midpoint_continuation.json')
    parser.add_argument('--output', type=Path, default=OUTPUT/'reviewer_return512_result.json')
    args = parser.parse_args()
    try:
        progress('declared_scope', height=H, last_time=LIMIT, midpoint=MID, reached_cap=CAP)
        result, states, index, forward, backward = calculate()
        author = json.loads(args.author_input.read_text(encoding='utf-8'))
        old = json.loads(args.old_prefix_input.read_text(encoding='utf-8'))
        assert author['status'] == 'complete'
        for k, v in {'polynomial_coefficients_ascending': [1,-1,-1,-1,1],
            'digit_integer_weights': {'-1': 1, '0': 2, '1': 1}, 'digit_denominator': 4,
            'complete_return_times_including_zero': [0,LIMIT], 'midpoint_times': [MID],
            'deterministic_complete_height': H, 'state_cap': CAP, 'old_helper_cap_unchanged': 100000,
            'working_set_stop_bytes': 4*1024**3, 'available_physical_memory_stop_below_bytes': 1024**3,
            'memory_checks_graph_states': 4096, 'memory_checks_dp_steps': 16,
            'real_strip_coefficient_scale': SCALE, 'pressure_root_bisections': 40}.items():
            assert author['scope'][k] == v, k
        assert old['scope']['complete_return_times'] == [1,256]
        assert old['scope']['digit_integer_weights'] == {'-1':1,'0':2,'1':1} and old['scope']['digit_denominator'] == 4
        for key in ('complete_return_integer_weights', 'complete_first_return_integer_weights'):
            assert len(result[key]) == 513 and result[key] == author[key]
            assert result[key][:257] == old[key] and len(old[key]) == 257
        for key in ('midpoint', 'pressure_beta_interval', 'partial_first_return_at_beta_lower_bracket',
                    'partial_first_return_at_beta_upper_bracket', 'partial_first_return_beta_interval_display',
                    'selected_complete_returns', 'all_times_fail_strict_pressure_crossing',
                    'partial_first_return_upper_is_below_one'):
            assert result[key] == author[key], key
        for key, value in author['graph'].items():
            assert result['graph'][key] == value, key
        assert len(author['quotient_states']) == len(author['forward256']) == len(author['backward256']) == len(states)
        seen = set()
        for i, (q, f, b) in enumerate(zip(author['quotient_states'], author['forward256'], author['backward256'], strict=True)):
            if i % 4096 == 0:
                memory()
            a = to_original(q)
            assert a in index and a not in seen
            seen.add(a)
            j = index[a]
            assert (f, b) == (backward[j], forward[j]), (q, 'full reversed vector alignment')
        assert len(seen) == len(states)
        result['comparison'] = {'all_513_returns_equal': True, 'all_513_first_returns_equal': True,
            'all_257_old_return_and_first_return_entries_equal': True,
            'all_254775_state_forward_and_backward_pairs_equal_under_reversal': True,
            'all_midpoint_fields_and_exact_pressure_fractions_equal': True}
        progress('all_exact_comparisons_passed', **result['comparison'])
        write_atomic(args.output, result)
        print(json.dumps({'status':'complete', 'output':str(args.output), 'graph':result['graph'], 'comparison':result['comparison']}), flush=True)
    except BaseException as error:
        write_atomic(args.output.with_suffix('.incomplete.json'), {'status':'incomplete', 'height':H,
            'last_time':LIMIT, 'midpoint':MID, 'cap':CAP, 'failure_type':type(error).__name__, 'failure':str(error)})
        raise


if __name__ == '__main__':
    main()
