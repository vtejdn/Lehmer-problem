"""Independent complete J71 check by binary words and endpoint autocorrelation.

Declared before execution: exactly the two retained domains (494 and210 maps),
all saved endpoint counts and inequalities; aggregate120-second reviewer cap.
No author module imports or ternary dynamic programming. Author native bytes
are observed within the run only, not historical fingerprints. Draft presence
is optional so this checker remains usable after fixed retention.
"""
from collections import Counter
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time

CAP = 120
HERE = (_J_PROGRAM / 'review_independent.py').parent
NATIVE = ('readme.md', 'main.py', 'result.json', 'vector.py', 'result-vector.json')


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first,) + rest


def autocorrelation(cols):
    # Enumerate every fair binary word explicitly, then pair endpoint fibers.
    dim = len(cols[0])
    binary = Counter()
    for mask in range(1 << len(cols)):
        endpoint = tuple(sum(col[j] for k, col in enumerate(cols)
                             if mask & (1 << k)) for j in range(dim))
        binary[endpoint] += 1
    result = Counter()
    for x, nx in binary.items():
        for y, ny in binary.items():
            result[tuple(a - b for a, b in zip(x, y))] += nx * ny
    assert sum(binary.values()) == 2 ** len(cols)
    assert sum(result.values()) == 4 ** len(cols)
    assert all(result[z] == result[tuple(-a for a in z)] for z in result)
    return result


def exact_types_equal(a, b):
    assert type(a) is type(b), (type(a), type(b))
    if isinstance(a, dict):
        assert a.keys() == b.keys()
        for k in a:
            exact_types_equal(a[k], b[k])
    elif isinstance(a, list):
        assert len(a) == len(b)
        for x, y in zip(a, b):
            exact_types_equal(x, y)
    else:
        assert a == b, (a, b)


def run():
    start = time.perf_counter()
    before = {name: (((_J_PROGRAM if name in ('main.py', 'readme.md', 'review_independent.py', 'vector.py') else _J_OUTPUT) / name)).read_bytes() for name in NATIVE}
    draft = (_J_ROOT / 'mathematics/drafts/Yin_D_G0153.md')
    author = draft.read_bytes() if draft.exists() else None
    scalar = json.loads(before['result.json'])
    vector = json.loads(before['result-vector.json'])
    expected_scalar = {}
    scalar_checks = 0
    for n in range(1, 9):
        for occ in compositions(n, 4):
            key = tuple(v for v, count in enumerate(occ, 1) for _ in range(count))
            counts = autocorrelation([(a,) for a in key])
            q = sum(a * a for a in key)
            zero = counts[(0,)]
            failures = []
            for (z,), count in sorted(counts.items()):
                if z:
                    scalar_checks += 1
                    if count ** q * 2 ** (z * z) > zero ** q:
                        failures.append(z)
            expected_scalar[key] = dict(columns=list(key), Q=q,
                denominator=4 ** n,
                counts=[[z, counts[(z,)]] for (z,) in sorted(counts)],
                failed_endpoints=failures)
            assert time.perf_counter() - start < CAP
    assert len(expected_scalar) == 494 and scalar_checks == 14470
    assert len(scalar['records']) == len(expected_scalar)
    seen = set()
    for record in scalar['records']:
        key = tuple(record['columns'])
        assert key not in seen
        seen.add(key)
        exact_types_equal(record, expected_scalar[key])
    assert seen == expected_scalar.keys()
    assert all(not r['failed_endpoints'] for r in expected_scalar.values())
    expected_vector = {}
    vector_checks = 0
    alphabet = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2)]
    for extra in range(5):
        for occ in compositions(extra, 6):
            cols = [(1, 0), (0, 1)] + [col for col, n in zip(alphabet, occ)
                                      for _ in range(n)]
            key = tuple(cols)
            counts = autocorrelation(cols)
            # Dot products of the two coordinate rows, computed independently.
            row0, row1 = tuple(zip(*cols))
            aa = sum(x * x for x in row0)
            ab = sum(x * y for x, y in zip(row0, row1))
            bb = sum(y * y for y in row1)
            det = aa * bb - ab * ab
            assert det > 0
            zero = counts[(0, 0)]
            failures = []
            for (x, y), count in sorted(counts.items()):
                if x or y:
                    vector_checks += 1
                    numerator = bb * x * x - 2 * ab * x * y + aa * y * y
                    assert numerator > 0
                    if count ** det * 2 ** numerator > zero ** det:
                        failures.append([x, y])
            expected_vector[key] = dict(columns=[list(c) for c in cols],
                Q=[[aa, ab], [ab, bb]], D=det, denominator=4 ** len(cols),
                counts=[[x, y, counts[(x, y)]] for x, y in sorted(counts)],
                failed_endpoints=failures)
            assert time.perf_counter() - start < CAP
    assert len(expected_vector) == 210 and vector_checks == 13200
    assert len(vector['records']) == len(expected_vector)
    seen = set()
    for record in vector['records']:
        key = tuple(map(tuple, record['columns']))
        assert key not in seen
        seen.add(key)
        exact_types_equal(record, expected_vector[key])
    assert seen == expected_vector.keys()
    assert all(not r['failed_endpoints'] for r in expected_vector.values())
    scalar_scope = dict(lengths=[1, 8], positive_column_values=[1, 2, 3, 4],
                        normalization='sorted multisets', all_nonzero_endpoints=True)
    vector_scope = dict(fixed_columns=[[1, 0], [0, 1]],
                        alphabet=[list(c) for c in alphabet],
                        extra_column_counts=[0, 4], all_nonzero_endpoints=True)
    for data, count, tests, scope in [(scalar, 494, 14470, scalar_scope),
                                      (vector, 210, 13200, vector_scope)]:
        assert set(data) == {'status', 'scope', 'pattern_count', 'endpoint_test_count', 'failure_count', 'failures', 'records'}
        for name, value in dict(status='complete', scope=scope, pattern_count=count, endpoint_test_count=tests, failure_count=0, failures=[]).items():
            exact_types_equal(data[name], value)
        pass
        pass
        pass
    assert all((((_J_PROGRAM if name in ('main.py', 'readme.md', 'review_independent.py', 'vector.py') else _J_OUTPUT) / name)).read_bytes() == value for name, value in before.items())
    if author is not None:
        assert draft.read_bytes() == author
    elapsed = time.perf_counter() - start
    assert elapsed < CAP
    return dict(status='passed', method='explicit fair binary words followed by endpoint autocorrelation; no author imports', scalar_maps=494, scalar_nonzero_endpoint_tests=14470, vector_maps=210, vector_nonzero_endpoint_tests=13200, total_maps=704, total_nonzero_endpoint_tests=27670, complete_distribution_entries=sum((len(r['counts']) for r in scalar['records'] + vector['records'])), complete_native_mathematical_payloads_equal=True, native_math_types_equal=True, universal_C1_proved=False, actual_algebraic_orbit_experiment=False)


if __name__ == '__main__':
    report = run()
    ((_J_OUTPUT / 'review_result.json')).write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
