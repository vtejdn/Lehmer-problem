"""Deterministic balanced-base controls for the finite Galois filter model.

Keep galois_filters.py's baseline unchanged.  This separate calculation tests
the specified p=27 base and a bounded, exact p=81 unit descent, then exhausts
one and two filter labels.  Whole Mahler products are certified only for hits.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb, gcd
from pathlib import Path
import json
import sys

from flint import arb, ctx, fmpz_poly

from galois_filters import (
    filtered_moments, moments, multiply, normalize, representative,
    sparse_filter_square, sparse_multiply, trace_polynomials, trace_word,
    twice_inverse, word_polynomial,
)

PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0151"))
from exterior19683 import separator_certificate


def integral_half(word):
    assert all(value % 2 == 0 for value in word)
    return tuple(value // 2 for value in word)


def plus_unit(p, a):
    assert gcd(a, p) == 1
    half_a = (a * ((p + 1) // 2)) % p
    trace_half = trace_word(p, half_a)
    inverse_half = integral_half(twice_inverse(p, half_a))
    forward = multiply(trace_half, trace_half)
    backward = multiply(inverse_half, inverse_half)
    expected = list(trace_word(p, a))
    expected[0] += 2
    assert forward == normalize(expected)
    assert multiply(forward, backward) == (1,) + (0,) * (p - 1)
    return {"label": f"U{a}", "forward": forward, "inverse": backward}


def quotient_square_unit(p, scale, u):
    assert u % 2 and gcd(u, p // scale) == 1
    numerator = trace_word(p, scale * u)
    denominator = trace_word(p, scale)
    quotient = integral_half(multiply(numerator, twice_inverse(p, scale)))
    inverse = integral_half(multiply(denominator, twice_inverse(p, scale * u)))
    assert multiply(quotient, inverse) == (1,) + (0,) * (p - 1)
    forward, backward = multiply(quotient, quotient), multiply(inverse, inverse)
    assert multiply(forward, backward) == (1,) + (0,) * (p - 1)
    return {"label": f"J{u}(T{scale})^2", "forward": forward, "inverse": backward}


def energy(word):
    K, L = moments(word)
    return 2 * L + 3 * K


def descend(initial, units, cap=100):
    current = initial
    start = energy(current)
    assert start > 0
    history = []
    exponents = Counter()
    stop = "step_cap"
    for step in range(cap):
        incumbent = energy(current)
        best = None
        # Strict improvement alone replaces a candidate, fixing ties by order.
        for unit in units:
            for sign, key in ((1, "forward"), (-1, "inverse")):
                candidate = multiply(current, unit[key])
                value = energy(candidate)
                assert value > 0
                if value < incumbent:
                    incumbent = value
                    best = candidate, unit["label"], sign
        if best is None:
            stop = "one_step_stationary_for_this_list"
            break
        current, label, sign = best
        exponents[label] += sign
        history.append({"step": step + 1, "unit": label, "exponent": sign,
                        "energy": incumbent, "K_L": moments(current)})
    final_neighbors = [
        {"unit": unit["label"], "exponent": sign,
         "energy": energy(multiply(current, unit[key]))}
        for unit in units for sign, key in ((1, "forward"), (-1, "inverse"))
    ]
    final_minimum = min(neighbor["energy"] for neighbor in final_neighbors)
    if stop == "one_step_stationary_for_this_list":
        assert final_minimum >= energy(current)
    return current, {
        "initial_energy": start, "final_energy": energy(current),
        "steps": history, "stop": stop, "step_cap": cap,
        "final_minimum_neighbor_energy": final_minimum,
        "final_neighbors": final_neighbors,
        "net_exponents": dict(exponents), "unit_labels": [unit["label"] for unit in units],
    }


def polynomial_data(p, word, x, B, traces, expected_norm):
    n = p // 2
    h = word_polynomial(word, traces)
    D = B - traces[n]
    C = (D * h) % B
    K, L = moments(word)
    assert (K, L) == (x*x + 2, -4*x)
    assert int(C[n - 1]) == K
    assert int(C[n - 2]) - K * int(B[n - 1]) == L
    Q = (traces[1] - 2*x) * B + C
    resultant = abs(int(B.resultant(Q)))
    assert resultant == expected_norm
    d = n + 1
    lift = [
        sum(int(Q[a]) * comb(a, (a+d-index)//2)
            for a in range(abs(d-index), d+1) if (a+d-index) % 2 == 0)
        for index in range(2*d+1)
    ]
    assert lift == lift[::-1] and lift[0] == 1
    endpoint = sum(value * (-1)**index for index, value in enumerate(lift))
    assert endpoint == (-1)**d * int(Q(-2))
    return {"x": x, "K": K, "L": L, "P_minus_one": endpoint,
            "absolute_resultant": resultant, "h_word": word,
            "Q_coefficients_ascending": list(map(int, Q)),
            "P_coefficients_ascending": lift}


def certify_measure(record):
    ctx.prec = 256
    polynomial = fmpz_poly(record["P_coefficients_ascending"])
    product = arb(1)
    roots = 0
    for root, multiplicity in polynomial.complex_roots():
        modulus = abs(root)
        if modulus < 1:
            contribution = arb(1)
        elif modulus > 1:
            contribution = modulus
        else:
            contribution = arb(1).union(modulus)
        product *= contribution**multiplicity
        roots += multiplicity
    assert roots == polynomial.degree()
    assert product.rad() < arb("1e-25")
    record.update(root_count=roots, measure_ball=str(product),
                  log_measure_ball=str(product.log()),
                  strict_positive_measure=bool(product > 1))
    return product


def filter_traversal(p, base, B, traces, delta0):
    indices = [a for a in range(1, p//2+1) if gcd(a, p) == 1]
    filters = {a: sparse_filter_square(p, a) for a in indices}
    singles = {a: sparse_multiply(base, filters[a]) for a in indices}
    V = traces[5] + traces[4] - traces[2] - traces[1] - 1
    norm = abs(int(B.resultant(V)))
    assert norm > 0
    targets = {(x*x+2, -4*x): x for x in range(-2, 3)}
    result = []
    for count in (1, 2):
        histogram = Counter()
        ordered_histogram = Counter()
        first_hits = []
        hits = []
        labels = ((a,) for a in indices) if count == 1 else combinations_with_replacement(indices, 2)
        for label in labels:
            pair = moments(singles[label[0]]) if count == 1 else filtered_moments(singles[label[0]], filters[label[1]])
            histogram[pair] += 1
            multiplicity = 1 if count == 1 or label[0] == label[1] else 2
            ordered_histogram[pair] += multiplicity
            if pair[0] in (2,3,6):
                first_hits.append({"filter_labels": label, "K": pair[0], "L": pair[1],
                                   "ordered_multiplicity": multiplicity})
            if pair in targets:
                word = singles[label[0]] if count == 1 else sparse_multiply(singles[label[0]], filters[label[1]])
                assert moments(word) == pair
                record = polynomial_data(p, word, targets[pair], B, traces, delta0 * norm**(2*count))
                record["filter_labels"] = label
                record["ordered_multiplicity"] = multiplicity
                if record["P_minus_one"] > 0:
                    certify_measure(record)
                hits.append(record)
        entry = {
            "filter_count": count, "labels_tested": sum(histogram.values()),
            "ordered_labels_tested": sum(ordered_histogram.values()),
            "distinct_joint_pairs": len(histogram),
            "minimum_energy": min(3*K + 2*L for K,L in histogram),
            "target_K_counts": {str(K): sum(number for (a,b), number in histogram.items() if a == K) for K in (2,3,6)},
            "joint_target_counts": {str(x): sum(hit["x"] == x for hit in hits) for x in range(-2,3)},
            "first_moment_hits": first_hits,
            "histogram": [[K,L,number] for (K,L),number in sorted(histogram.items())],
            "ordered_histogram": [[K,L,number] for (K,L),number in sorted(ordered_histogram.items())],
            "hits": hits,
        }
        assert entry["labels_tested"] == (len(indices) if count == 1 else len(indices)*(len(indices)+1)//2)
        assert entry["ordered_labels_tested"] == len(indices)**count
        print(json.dumps({key: value for key, value in entry.items()
                          if key not in ("histogram","ordered_histogram","hits")}), flush=True)
        for hit in hits:
            print("hit", json.dumps({key:value for key,value in hit.items() if key not in ("h_word","P_coefficients_ascending","Q_coefficients_ascending")}), flush=True)
        result.append(entry)
    return {"filter_norm": norm, "indices": indices, "results": result}


def run27():
    p, cut = 27, 3
    base, columns, exponent = representative(p, cut)
    for a in (2, 2, 5, 8, 11):
        base = multiply(base, plus_unit(p, a)["forward"])
    assert moments(base) == (2, 0)
    traces = trace_polynomials(p//2)
    B = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    original = polynomial_data(p, base, 0, B, traces, 2**exponent)
    assert original["P_minus_one"] == 1
    measure = certify_measure(original)
    assert measure > arb("3.349927") and measure < arb("3.349928")
    print("p27 baseline", original["measure_ball"], flush=True)
    return {"p": p, "cut": cut, "base_word": base,
            "baseline_unit_word": {"U2": 2, "U5": 1, "U8": 1, "U11": 1},
            "original": original, **filter_traversal(p, base, B, traces, 32)}


def run81():
    p, cut = 81, 9
    assert separator_certificate(p, cut, Fraction(-3, 2)) == p//2-cut
    base, columns, exponent = representative(p, cut)
    traces = trace_polynomials(p//2)
    B = fmpz_poly([1]) + sum(traces[1:], fmpz_poly())
    units = [plus_unit(p, a) for a in range(1, p//2+1) if gcd(a,p) == 1]
    assert len(units) == 27
    extra = [quotient_square_unit(p, 3, u) for u in (5,7,11,13,17,19,23,25)]
    extra += [quotient_square_unit(p, 9, u) for u in (5,7)]
    for unit in units + extra:
        for key in ("forward", "inverse"):
            assert abs(int(B.resultant(word_polynomial(unit[key], traces)))) == 1
    after_first, first = descend(base, units)
    final, second = descend(after_first, units + extra)
    assert abs(int(B.resultant(word_polynomial(final, traces)))) == 2**exponent
    final_h = word_polynomial(final, traces)
    final_C = ((B - traces[p//2]) * final_h) % B
    endpoint_U = final[0] - final[1]
    endpoint_values = {}
    for x in range(-2,3):
        final_Q = (traces[1] - 2*x) * B + final_C
        endpoint_values[str(x)] = (-1)**(p//2+1) * int(final_Q(-2))
        assert endpoint_values[str(x)] == 2 + 2*x + endpoint_U
    print("p81 phases", first["initial_energy"], first["final_energy"], len(first["steps"]), first["stop"],
          second["final_energy"], len(second["steps"]), second["stop"], flush=True)
    original = None
    targets = {(x*x+2,-4*x): x for x in range(-2,3)}
    if moments(final) in targets:
        original = polynomial_data(p, final, targets[moments(final)], B, traces, 2**exponent)
        if original["P_minus_one"] > 0:
            certify_measure(original)
    return {"p": p, "cut": cut, "separator": "-3/2", "initial_word": base,
            "initial_K_L": moments(base), "base_word": final, "final_K_L": moments(final),
            "final_endpoint_U": endpoint_U, "final_endpoints_by_x": endpoint_values,
            "phases": [first, second], "original": original,
            **filter_traversal(p, final, B, traces, 32)}


def main():
    output = Path(__file__).resolve().parents[2] / "outputs" / Path(__file__).resolve().parent.name
    output.mkdir(parents=True, exist_ok=True)
    for function in (run27, run81):
        record = function()
        (output / f"balanced_control_{record['p']}.json").write_text(
            json.dumps(record, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
