"""Complete independent J78 check: binary enumeration and exact integer square.

No author or project program is imported. All four declared domains are checked;
time/path metadata are inspected, not a mathematical reproducibility target.
No draft is required. No historical bytes or hashes are acceptance inputs.
"""
from collections import Counter
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import argparse
import json
import math
import time

BASE = (_J_PROGRAM / 'review_independent.py').parent
CAP = 120


def compare_exact(actual, expected, path="root"):
    """Check full schema, exact scalar types and every mathematical value."""
    assert type(actual) is type(expected), (path, type(actual), type(expected))
    if isinstance(expected, dict):
        assert set(actual) == set(expected), (path, set(actual), set(expected))
        return sum(compare_exact(actual[k], v, path + "." + k)
                   for k, v in expected.items())
    if isinstance(expected, list):
        assert len(actual) == len(expected), (path, len(actual), len(expected))
        return sum(compare_exact(a, b, path + "[" + str(i) + "]")
                   for i, (a, b) in enumerate(zip(actual, expected)))
    assert actual == expected, (path, actual, expected)
    return 1


def complete_map(rank, deadline):
    # Bit construction, rather than the author's Cartesian-product columns.
    b = 1 << (rank - 1)
    columns = [[1] + [2 * ((j >> k) & 1) - 1
                       for k in range(rank - 2, -1, -1)]
               for j in range(b)]
    # Integral parity-lattice coordinates: u0=z0; ui=(z0-zi)/2.
    transformed = [[1] + [(1 - x) // 2 for x in a[1:]] for a in columns]
    maxima = [b] + [b // 2] * (rank - 1)
    radices = [2 * v + 1 for v in maxima]
    strides = [1]
    for radix in radices[:-1]:
        strides.append(strides[-1] * radix)
    enc = [sum(x * s for x, s in zip(a, strides)) for a in transformed]
    max_index = sum(enc)
    box_size = math.prod(radices)
    assert max_index * 2 + 1 == box_size
    # Every one of the 2^b actual binary words is visited exactly once.
    binary = Counter({0: 1})
    old_gray = 0
    point = 0
    for k in range(1, 1 << b):
        gray = k ^ (k >> 1)
        changed = gray ^ old_gray
        bit = changed.bit_length() - 1
        point += enc[bit] if gray & changed else -enc[bit]
        binary[point] += 1
        old_gray = gray
    assert sum(binary.values()) == 1 << b
    assert all(binary[max_index - u] == c for u, c in binary.items())
    # The coefficient radix exceeds the sum of ALL two-word coefficients.
    # The spatial radices exceed every possible coordinate in the product.
    width = (2 * b + 1 + 7) // 8
    coefficient_radix = 1 << (8 * width)
    assert coefficient_radix > 4 ** b
    buf = bytearray((max_index + 1) * width)
    for u, c in binary.items():
        buf[u * width:(u + 1) * width] = c.to_bytes(width, "little")
    packed = int.from_bytes(buf, "little")
    del buf
    assert time.perf_counter() < deadline, "Reviewer cap before integer square"
    product = packed * packed
    del packed
    assert time.perf_counter() < deadline, "Reviewer cap after integer square"
    raw = product.to_bytes(box_size * width, "little")
    del product
    counts = {}
    zero_chunk = bytes(width)
    # Inspect the ENTIRE encoding box, not just native saved endpoints.
    for index in range(box_size):
        chunk = raw[index * width:(index + 1) * width]
        if chunk == zero_chunk:
            continue
        count = int.from_bytes(chunk, "little")
        code = index
        coords = []
        for radix, maximum in zip(radices, maxima):
            coords.append(code % radix - maximum)
            code //= radix
        assert code == 0
        endpoint = (coords[0],) + tuple(coords[0] - 2 * x for x in coords[1:])
        assert endpoint not in counts
        counts[endpoint] = count
    del raw
    assert sum(counts.values()) == 4 ** b
    assert all(counts[tuple(-x for x in z)] == c for z, c in counts.items())
    gram = [[b if i == j else 0 for j in range(rank)] for i in range(rank)]
    assert all(sum(a[i] * a[j] for a in columns) == gram[i][j]
               for i in range(rank) for j in range(rank))
    c0 = counts[(0,) * rank]
    threshold = pow(c0, b)
    rows = []
    failures = []
    for z, c in sorted(counts.items()):
        squared = sum(x * x for x in z)
        passes = (pow(c, b) << squared) <= threshold
        row = [list(z), c, squared, passes]
        rows.append(row)
        if not passes:
            failures.append(row)
    assert time.perf_counter() < deadline, "Reviewer cap after complete map"
    case = dict(rank=rank, b=b, columns=columns, gram=gram,
                denominator=4 ** b, center_count=c0, endpoint_count=len(counts),
                endpoints=rows, failures=failures)
    detail = dict(rank=rank, b=b, binary_words=1 << b,
                  binary_endpoints=len(binary), spatial_radices=radices,
                  coefficient_bytes=width, inspected_encoding_positions=box_size,
                  endpoint_count=len(counts), center_count=c0,
                  failures=len(failures), normalization=True, symmetry=True)
    return case, detail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=(_J_OUTPUT / 'review_result.json'))
    args = parser.parse_args()
    output = args.output.resolve()
    if output.parent != _J_OUTPUT:
        raise ValueError("Select a reviewer output inside this responsible J")
    if output.exists():
        raise FileExistsError("Preserve the first report; choose another --output")
    started = time.perf_counter()
    native_names = ("main.py", "result.json", "readme.md")
    before = {name: (((_J_PROGRAM if name in ('main.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / name)).read_bytes() for name in native_names}
    data = json.loads(before["result.json"])
    assert set(data) == {'domain', 'law', 'cases', 'total_endpoints', 'total_failures'}
    pass
    pass
    pass
    pass
    pass
    expected_cases, details = [], []
    for rank in (2, 3, 4, 5):
        case, detail = complete_map(rank, started + CAP)
        expected_cases.append(case)
        details.append(detail)
        print(json.dumps(detail), flush=True)
    expected = dict(domain="r=2,3,4,5; all columns (1,+/-1,...,+/-1); all original endpoints",
                    law=[1, 2, 1], cases=expected_cases,
                    total_endpoints=sum(c["endpoint_count"] for c in expected_cases),
                    total_failures=sum(len(c["failures"]) for c in expected_cases))
    mathematical = {k: v for k, v in data.items() if k != "execution"}
    leaves = compare_exact(mathematical, expected)
    unchanged = {name: before[name] == (((_J_PROGRAM if name in ('main.py', 'readme.md', 'review_independent.py') else _J_OUTPUT) / name)).read_bytes() for name in native_names}
    # This observation is not a content gate, nor a stored revision fingerprint.
    elapsed = time.perf_counter() - started
    assert elapsed <= CAP, "Declared complete reviewer cap exceeded"
    report = dict(status='passed', method='complete binary Gray-code words; carry-free mixed-radix integer-square convolution', author_imports=False, prior_reviewer_imports=False, complete_mathematical_schema_and_types=True, mathematical_scalar_leaves=leaves, cases=details, total_endpoints=expected['total_endpoints'], total_failures=expected['total_failures'])
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
