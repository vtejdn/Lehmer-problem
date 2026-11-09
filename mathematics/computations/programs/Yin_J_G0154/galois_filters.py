"""Exact one- and two-filter supply on slow ternary sign cuts.

The complete finite label set is traversed with integer cyclic arithmetic.
Every moment hit is retained for a subsequent endpoint and complete root-product
test.  No floating-point screen is used to omit a label.
"""

import argparse
from collections import Counter
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path
import json
import sys

from flint import fmpz_poly

PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0150"))
from moments import sign_columns, setup


def normalize(word):
    offset = word[len(word) // 2]
    result = tuple(value - offset for value in word)
    assert result == (result[0], *result[:0:-1])
    return result


def multiply(left, right):
    """Exact carry-free cyclic multiplication, modulo the all-one word."""
    p = len(left)
    assert len(right) == p
    lower_left, lower_right = min(left), min(right)
    bound = p * (max(left) - lower_left) * (max(right) - lower_right)
    width = max(1, (bound.bit_length() + 7) // 8)

    def pack(word, lower):
        return int.from_bytes(
            b"".join((value - lower).to_bytes(width, "little") for value in word),
            "little",
        )

    modulus = (1 << (8 * width * p)) - 1
    product = (pack(left, lower_left) * pack(right, lower_right)) % modulus
    data = product.to_bytes(width * p, "little")
    return normalize([
        int.from_bytes(data[index:index + width], "little")
        for index in range(0, len(data), width)
    ])


def trace_word(p, index):
    result = [0] * p
    result[index % p] += 1
    result[-index % p] += 1
    return normalize(result)


def twice_inverse(p, index):
    result = [0] * p
    order = p // gcd(p, index)
    for step in range(order):
        result[(2 * step + 1) * index % p] += (-1) ** step
    result = normalize(result)
    assert multiply(result, trace_word(p, index)) == (2,) + (0,) * (p - 1)
    return result


def choose_cut(p):
    m, remaining = 0, p
    while remaining > 1 and remaining % 3 == 0:
        remaining //= 3
        m += 1
    assert remaining == 1 and m >= 3
    s = 0
    while 3**s < m:
        s += 1
    s = max(2, s)
    assert 1 < s < m
    return m, s, 3 ** (m - s)


def representative(p, cut):
    """Use exactly L464 v8's sign-column construction and parity payments."""
    one = (1,) + (0,) * (p - 1)
    columns = sign_columns(p, cut)
    result = one
    parity = Counter()
    inverse_cache = {}
    for column in columns:
        scale = 1
        while column % (3 * scale) == 0:
            scale *= 3
        parity[scale] += 1
        if scale not in inverse_cache:
            inverse_cache[scale] = twice_inverse(p, scale)
        numerator = multiply(trace_word(p, column), inverse_cache[scale])
        assert all(value % 2 == 0 for value in numerator)
        quotient = tuple(value // 2 for value in numerator)
        assert multiply(quotient, trace_word(p, scale)) == trace_word(p, column)
        result = multiply(result, quotient)
    exponent = 0
    for scale, count in parity.items():
        if count % 2:
            result = multiply(result, trace_word(p, scale))
            exponent += (scale - 1) // 2
    return result, columns, exponent


def sparse_filter_square(p, index):
    """V_index^2, with equal cyclic exponents already collected."""
    first = Counter({0: -1})
    for degree, coefficient in ((5, 1), (4, 1), (2, -1), (1, -1)):
        first[(degree * index) % p] += coefficient
        first[(-degree * index) % p] += coefficient
    squared = Counter()
    for left, left_value in first.items():
        for right, right_value in first.items():
            squared[(left + right) % p] += left_value * right_value
    return tuple(sorted((power, value) for power, value in squared.items() if value))


def sparse_multiply(word, sparse):
    p = len(word)
    return normalize([
        sum(value * word[(index - power) % p] for power, value in sparse)
        for index in range(p)
    ])


def moments(word):
    return word[0] - word[2], word[1] - word[3]


def filtered_moments(word, sparse):
    p = len(word)
    return tuple(
        sum(value * (word[(a - power) % p] - word[(b - power) % p])
            for power, value in sparse)
        for a, b in ((0, 2), (1, 3))
    )


def trace_polynomials(n):
    result = [fmpz_poly([2]), fmpz_poly([0, 1])]
    for index in range(2, n + 1):
        result.append(result[1] * result[-1] - result[-2])
    return result


def word_polynomial(word, traces):
    n = len(word) // 2
    assert word[n] == word[n + 1] == 0
    return fmpz_poly([word[0]]) + sum(
        (word[index] * traces[index] for index in range(1, n)), fmpz_poly()
    )


def low_dimensional_control(p, cut, base, indices, filters, singles, B, traces):
    """At 27, compare every label with ordinary integer polynomial arithmetic."""
    assert p == 27
    old_B, old_traces, old_base, _, old_norm, old_cut, _ = setup(p, cut)
    assert old_base == base and old_norm == 32 and old_cut == cut
    assert [int(value) for value in old_B.all_coeffs()][::-1] == list(map(int, B))
    h0 = word_polynomial(base, traces)
    D = B - traces[p // 2]
    polynomial_filters = {}
    for index in indices:
        # Independent polynomial composition, not reduction of sparse words.
        t = traces[index]
        polynomial_filters[index] = (t**5 + t**4 - 5*t**3 - 5*t**2 + 4*t + 3) % B
        polynomial_h = (h0 * polynomial_filters[index]**2) % B
        assert polynomial_h == word_polynomial(singles[index], traces)
    checked = 0
    for left, right in combinations_with_replacement(indices, 2):
        word = sparse_multiply(singles[left], filters[right])
        polynomial_h = (h0 * (polynomial_filters[left] * polynomial_filters[right])**2) % B
        assert polynomial_h == word_polynomial(word, traces)
        remainder = (D * polynomial_h) % B
        expected = (int(remainder[p//2-1]),
                    int(remainder[p//2-2]) - int(B[p//2-1]) * int(remainder[p//2-1]))
        assert moments(word) == filtered_moments(singles[left], filters[right]) == expected
        checked += 1
    assert checked == 45
    return {"single_polynomials": len(indices), "double_polynomials_and_moments": checked,
            "baseline_matches_J150_setup": True}


def run_conductor(p):
    m, s, cut = choose_cut(p)
    base, columns, exponent = representative(p, cut)
    assert exponent == 2 * 3 ** (s - 1) - 1
    indices = [index for index in range(1, p // 2 + 1) if gcd(index, p) == 1]
    assert len(indices) == 3 ** (m - 1)
    traces = trace_polynomials(p // 2)
    B = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    base_polynomial = word_polynomial(base, traces)
    delta0 = abs(int(B.resultant(base_polynomial)))
    assert delta0 == 2**exponent
    lehmer_trace = traces[5] + traces[4] - traces[2] - traces[1] - 1
    filter_norm = abs(int(B.resultant(lehmer_trace)))
    assert filter_norm > 0
    # Galois multiplication permutes every nonzero residue modulo p.
    # Check the ring representation and norm independently at three labels.
    for index in sorted({indices[0], indices[len(indices) // 2], indices[-1]}):
        sparse = sparse_filter_square(p, index)
        raw = [0] * p
        for power, value in sparse:
            raw[power] = value
        square_polynomial = word_polynomial(normalize(raw), traces)
        assert abs(int(B.resultant(square_polynomial))) == filter_norm**2
    filters = {index: sparse_filter_square(p, index) for index in indices}
    singles = {index: sparse_multiply(base, filters[index]) for index in indices}
    control = low_dimensional_control(p, cut, base, indices, filters, singles, B, traces) if p == 27 else None
    results = []
    targets = { (x*x + 2, -4*x): x for x in range(-2, 3) }
    for count in (1, 2):
        histogram = Counter()
        first_counts = Counter()
        first_hits = []
        hits = []
        labels = ((index,) for index in indices) if count == 1 else combinations_with_replacement(indices, 2)
        for label in labels:
            value = moments(singles[label[0]]) if count == 1 else filtered_moments(singles[label[0]], filters[label[1]])
            histogram[value] += 1
            if value[0] in (2, 3, 6):
                first_counts[value[0]] += 1
                first_hits.append({"filter_labels": label, "K": value[0], "L": value[1]})
            if value in targets:
                word = singles[label[0]] if count == 1 else sparse_multiply(singles[label[0]], filters[label[1]])
                assert moments(word) == value
                hit = {"x": targets[value], "K": value[0], "L": value[1],
                       "predicted_absolute_resultant": delta0 * filter_norm**(2 * count),
                       "h_word": word, "filter_labels": label}
                hits.append(hit)
        expected = len(indices) if count == 1 else len(indices) * (len(indices) + 1) // 2
        assert sum(histogram.values()) == expected
        entry = {
            "filter_count": count, "labels_tested": expected,
            "distinct_K_L_pairs": len(histogram),
            "K_min": min(K for K, L in histogram), "K_max": max(K for K, L in histogram),
            "L_min": min(L for K, L in histogram), "L_max": max(L for K, L in histogram),
            "target_K_counts": {str(K): first_counts[K] for K in (2, 3, 6)},
            "first_moment_hits": first_hits,
            "joint_target_counts": {str(x): sum(hit["x"] == x for hit in hits) for x in range(-2, 3)},
            "histogram": [[K, L, number] for (K, L), number in sorted(histogram.items())],
            "hits": hits,
        }
        results.append(entry)
        print(json.dumps({key: value for key, value in entry.items()
                          if key not in ("histogram", "hits", "K_min", "K_max", "L_min", "L_max")}), flush=True)
    return {"p": p, "m": m, "s": s, "cut": cut, "sign_columns": columns,
            "base_word": base, "base_norm": delta0, "filter_norm": filter_norm,
            "base_K_L": moments(base), "low_dimensional_control": control,
            "indices": indices, "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conductors", nargs="+", type=int, default=[27, 81, 243, 729])
    args = parser.parse_args()
    output = Path(__file__).resolve().parents[2] / "outputs" / Path(__file__).resolve().parent.name
    output.mkdir(parents=True, exist_ok=True)
    for p in args.conductors:
        print("Conductor", p, flush=True)
        record = run_conductor(p)
        (output / f"galois_filters_{p}.json").write_text(
            json.dumps(record, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
