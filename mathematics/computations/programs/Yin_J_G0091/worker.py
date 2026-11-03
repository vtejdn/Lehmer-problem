"""Exact original-law parity and contiguous-half groupings at n=6,...,10."""
from fractions import Fraction
from itertools import product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import time
import traceback

HERE = (_J_PROGRAM / 'worker.py').parent
P = (1, -1, -1, -1)
Q = (1, -3, 1, -3)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
BETA = (0, 1, 0, 0)
BETA_INV = (1, 1, 1, -1)
START = time.monotonic()
COMPLETED = []


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


def save(name, obj):
    target = _J_OUTPUT / name
    temporary = target.with_suffix(target.suffix + ".writing")
    temporary.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
    temporary.replace(target)


def tick(stage, n, visited=0):
    if time.monotonic() - START > 175:
        raise TimeoutError("Declared worker cap at " + stage)
    save("progress.json", {"status": "in-progress", "stage": stage, "n": n,
                           "visited": visited, "completed": COMPLETED})


def mul(a, b, mod=P):
    out = [0] * 7
    for i in range(4):
        for j in range(4):
            out[i + j] += a[i] * b[j]
    for k in range(6, 3, -1):
        c = out[k]
        for i in range(4):
            out[k - 4 + i] -= c * mod[i]
    return tuple(out[:4])


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, k):
    return tuple(k * x for x in a)


def powers(base, count, mod=P):
    result = [ONE]
    for _ in range(1, count):
        result.append(mul(result[-1], base, mod))
    return result


INV_POWERS = powers(BETA_INV, 4)
BP = powers(BETA, 21)
GP = powers(BETA, 11, Q)


def sigma(a):
    return tuple(sum(a[j] * INV_POWERS[j][i] for j in range(4)) for i in range(4))


def trace_pair(a):
    b = a[2]
    assert a[1] == 2 * b and a[3] == -b, ("not trace field", a)
    return (a[0] - b, b)


def norm_pair(a):
    return trace_pair(mul(a, sigma(a)))


def cross_pair(a, b):
    return trace_pair(add(mul(a, sigma(b)), mul(sigma(a), b)))


def to_beta(a):
    return tuple(sum(a[j] * BP[2 * j][i] for j in range(4)) for i in range(4))


def sign_pair(value):
    # a+b*tau_minus = ((2a+b)-b*sqrt(13))/2, all rational.
    a, b = map(Fraction, value)
    c, e = 2 * a + b, -b
    if c == 0:
        return (e > 0) - (e < 0)
    if e == 0:
        return (c > 0) - (c < 0)
    sc, se = (c > 0) - (c < 0), (e > 0) - (e < 0)
    if sc == se:
        return sc
    delta = c * c - 13 * e * e
    assert delta != 0
    return sc if delta > 0 else se


def pair_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def pair_scale(a, c):
    return (a[0] * c, a[1] * c)


def pair_json(a):
    return [str(Fraction(a[0])), str(Fraction(a[1]))]


def beta_step(a):
    # Independent companion step for contiguous-half enumeration.
    x0, x1, x2, x3 = a
    return (-x3, x0 + x3, x1 + x3, x2 + x3)


def beta_inverse_step(a):
    x0, x1, x2, x3 = a
    return (x0 + x1, x0 + x2, x0 + x3, -x0)


def horner_beta(digits):
    value = ZERO
    for digit in reversed(digits):
        value = beta_step(value)
        value = (value[0] + digit, *value[1:])
    return value


def division_by_p(coeffs):
    rem = list(coeffs)
    quo = [0] * max(0, len(rem) - 4)
    for k in range(len(rem) - 1, 3, -1):
        c = rem[k]
        quo[k - 4] = c
        for j, pj in enumerate((*P, 1)):
            rem[k - 4 + j] -= c * pj
    assert all(x == 0 for x in rem), ("nonzero original remainder", rem)
    return quo


def prefix_beta(digits, cut, even=True):
    out = [0] * 4
    for k in range(cut):
        vec = BP[2 * k] if even else BP[k]
        for i in range(4):
            out[i] += digits[k] * vec[i]
    return tuple(out)


def original_candidate(n, candidate, bins, matched, total_weight):
    key, digits, j, aa, bb = candidate
    y = matched[key]
    other = list(digits)
    other[j:j + 6] = [aa - 1, 1, 1, 1, 1, bb - 1]
    other = tuple(other)
    odd = bins[y][6]
    whole_a = tuple(value for pair in zip(digits, odd) for value in pair)
    whole_b = tuple(value for pair in zip(other, odd) for value in pair)
    assert all(x in (-1, 0, 1) for x in whole_a + whole_b)
    assert horner_beta(whole_a) == horner_beta(whole_b) == ZERO
    qa, qb = division_by_p(whole_a), division_by_p(whole_b)
    cut = (n + 1) // 2
    diff = add(prefix_beta(digits, cut), scale(prefix_beta(other, cut), -1))
    diff_norm = norm_pair(diff)
    assert sign_pair(diff_norm) > 0
    wa, wb, wo = 2 ** digits.count(0), 2 ** other.count(0), 2 ** odd.count(0)
    wx, wy = bins[key][0], bins[y][0]
    factor = Fraction(wa * wb * wy, wx * total_weight)
    bound = pair_scale(diff_norm, factor)
    assert sign_pair(bound) > 0
    outside = list(digits)
    outside[j:j + 6] = [0] * 6
    z = tuple(sum(outside[k] * GP[k][i] for k in range(n)) for i in range(4))
    assert z != ZERO, "C51 forbids an unshifted dead endpoint witness"
    return {"n": n, "shift": j, "A": aa, "B": bb, "even_a": digits,
            "even_b": other, "odd": odd, "outside_even_digits": outside,
            "outside_translation_gamma_basis": z, "even_endpoint_gamma_basis": key,
            "odd_endpoint_gamma_basis": y, "original_return_word_a": whole_a,
            "original_return_word_b": whole_b, "original_p_quotient_a": qa,
            "original_p_quotient_b": qb, "zero_remainders": True,
            "even_a_integer_weight": wa, "even_b_integer_weight": wb,
            "odd_word_integer_weight": wo, "whole_a_integer_weight": wa * wo,
            "whole_b_integer_weight": wb * wo, "whole_probability_denominator": 16 ** n,
            "even_total_integer_weight": wx, "odd_total_integer_weight": wy,
            "return_weight_numerator": total_weight,
            "actual_conditional_endpoint_probability": str(Fraction(wx * wy, total_weight)),
            "midpoint_difference_square_trace_pair": pair_json(diff_norm),
            "pair_bound_multiplier": str(factor),
            "actual_weighted_innovation_lower_trace_pair": pair_json(bound)}


def parity_group(n, need_candidate):
    bins = {}
    candidates = []
    ce, co = (n + 1) // 2, n // 2
    tick("parity-enumeration", n)
    for count, digits in enumerate(product((-1, 0, 1), repeat=n), 1):
        if count % 4096 == 0:
            tick("parity-enumeration", n, count)
        key = tuple(sum(digits[k] * GP[k][i] for k in range(n)) for i in range(4))
        le = prefix_beta(digits, ce)
        lo = le if ce == co else prefix_beta(digits, co)
        be = norm_pair(le)
        bo = be if ce == co else norm_pair(lo)
        weight = 2 ** digits.count(0)
        row = bins.setdefault(key, [0, 0, [0] * 4, [0] * 4, [0] * 2, [0] * 2, digits])
        row[0] += weight
        row[1] += 1
        for i in range(4):
            row[2][i] += weight * le[i]
            row[3][i] += weight * lo[i]
        for i in range(2):
            row[4][i] += weight * be[i]
            row[5][i] += weight * bo[i]
        if need_candidate:
            for j in range(max(0, ce - 5), min(n - 6, ce - 1) + 1):
                if (digits[j] in (0, 1) and digits[j + 5] in (0, 1)
                        and digits[j + 1:j + 5] == (-1, -1, -1, -1)):
                    candidates.append((key, digits, j, digits[j], digits[j + 5]))
    assert count == 3 ** n
    assert sum(v[0] for v in bins.values()) == 4 ** n
    assert sum(v[1] for v in bins.values()) == 3 ** n
    assert bins[ZERO][0] == 2 ** n and bins[ZERO][1] == 1
    for key, row in bins.items():
        neg = bins[scale(key, -1)]
        assert row[0:2] == neg[0:2]
        assert all(a == -b for a, b in zip(row[2], neg[2]))
        assert all(a == -b for a, b in zip(row[3], neg[3]))
        assert row[4:6] == neg[4:6]
    matched = {}
    rows = []
    ctotal = returned_word_count = rejected_order = rejected_support = 0
    ttotal = (0, 0)
    atotal = (Fraction(0), Fraction(0))
    htotal = (Fraction(0), Fraction(0))
    full_mean = ZERO
    tick("parity-matching", n, count)
    for serial, (key, row) in enumerate(sorted(bins.items()), 1):
        if serial % 2048 == 0:
            tick("parity-matching", n, serial)
        numerator = mul((4, 2, 5, -2), key, Q)
        order_ok = all(x % 3 == 0 for x in numerator)
        assert order_ok == (sum(key[i] * (-1) ** i for i in range(4)) % 3 == 0)
        if not order_ok:
            rejected_order += 1
            continue
        y = tuple(-x // 3 for x in numerator)
        assert add(to_beta(key), mul(BETA, to_beta(y))) == ZERO
        if y not in bins:
            rejected_support += 1
            continue
        matched[key] = y
        other = bins[y]
        wx, wy = row[0], other[0]
        me, mo = tuple(row[2]), tuple(other[3])
        base = pair_add(pair_scale(row[4], wy), pair_scale(other[5], wx))
        cross = cross_pair(me, mul(BETA, mo))
        penalty = pair_add(pair_scale(norm_pair(me), Fraction(wy, wx)),
                           pair_scale(norm_pair(mo), Fraction(wx, wy)))
        total = pair_add(base, cross)
        within = pair_add(base, pair_scale(penalty, -1))
        means = pair_add(penalty, cross)
        assert pair_add(within, means) == total
        assert sign_pair(total) >= 0 and sign_pair(within) >= 0 and sign_pair(means) >= 0
        ctotal += wx * wy
        returned_word_count += row[1] * other[1]
        ttotal = pair_add(ttotal, total)
        atotal = pair_add(atotal, within)
        htotal = pair_add(htotal, means)
        full_mean = add(full_mean, add(scale(me, wy), scale(mul(BETA, mo), wx)))
        rows.append({"x_gamma": key, "y_gamma": y, "even_weight": wx, "odd_weight": wy,
                     "even_word_count": row[1], "odd_word_count": other[1],
                     "even_prefix_first_beta": me, "odd_prefix_first_beta": mo,
                     "even_prefix_second_trace": row[4], "odd_prefix_second_trace": other[5],
                     "raw_total_trace": pair_json(total), "raw_within_trace": pair_json(within),
                     "raw_means_trace": pair_json(means)})
    assert full_mean == ZERO
    assert ctotal >= 4 ** n
    assert pair_add(atotal, htotal) == ttotal
    witness = None
    for candidate in candidates:
        if candidate[0] in matched:
            witness = original_candidate(n, candidate, bins, matched, ctotal)
            break
    result = {"n": n, "original_length": 2 * n, "words_enumerated": 3 ** n,
              "raw_half_mass": 4 ** n, "unique_gamma_endpoints": len(bins),
              "ambiguous_gamma_endpoints": sum(v[1] > 1 for v in bins.values()),
              "order_rejected_endpoints": rejected_order,
              "order_ok_support_rejected_endpoints": rejected_support,
              "matched_endpoints": len(matched), "full_return_word_count": returned_word_count,
              "positive_innovation_matched_rows": sum(sign_pair(tuple(map(Fraction, r["raw_within_trace"]))) > 0 for r in rows),
              "return_integer_numerator": ctotal, "return_denominator": 16 ** n,
              "return_probability": str(Fraction(ctotal, 16 ** n)),
              "midpoint_second_trace_pair": pair_json(pair_scale(ttotal, Fraction(1, ctotal))),
              "within_parity_trace_pair": pair_json(pair_scale(atotal, Fraction(1, ctotal))),
              "conditional_mean_trace_pair": pair_json(pair_scale(htotal, Fraction(1, ctotal))),
              "raw_total_trace_pair": pair_json(ttotal), "matched_rows": rows,
              "complete_sign_symmetry_and_centering": True,
              "all_covariance_trace_signs_exact": True}
    return result, witness


def contiguous_check(n, parity):
    bins = {}
    tick("contiguous-enumeration", n)
    for count, digits in enumerate(product((-1, 0, 1), repeat=n), 1):
        if count % 4096 == 0:
            tick("contiguous-enumeration", n, count)
        endpoint = horner_beta(digits)
        weight = 2 ** digits.count(0)
        row = bins.setdefault(endpoint, [0, 0])
        row[0] += weight
        row[1] += 1
    assert count == 3 ** n and sum(v[0] for v in bins.values()) == 4 ** n
    ctotal = returned = 0
    ttotal = (0, 0)
    tick("contiguous-matching", n, count)
    for serial, (x, (wx, nx)) in enumerate(bins.items(), 1):
        if serial % 2048 == 0:
            tick("contiguous-matching", n, serial)
        y = scale(x, -1)
        for _ in range(n):
            y = beta_inverse_step(y)
        if y not in bins:
            continue
        wy, ny = bins[y]
        ctotal += wx * wy
        returned += nx * ny
        ttotal = pair_add(ttotal, pair_scale(norm_pair(x), wx * wy))
    assert ctotal == parity["return_integer_numerator"]
    assert returned == parity["full_return_word_count"]
    assert pair_json(ttotal) == parity["raw_total_trace_pair"]
    return {"words_enumerated": count, "unique_beta_endpoints": len(bins),
            "return_integer_numerator": ctotal, "full_return_word_count": returned,
            "raw_second_trace_pair": pair_json(ttotal), "exact_agreement": True}


def main():
    assert mul(BETA, BETA_INV) == ONE
    assert sigma(BETA) == BETA_INV
    assert norm_pair(BETA) == (1, 0)
    assert to_beta(GP[1]) == BP[2]
    witness = None
    for n in (6, 7, 8, 9, 10):
        parity, new_witness = parity_group(n, witness is None)
        check = contiguous_check(n, parity)
        parity["contiguous_half_crosscheck"] = check
        COMPLETED.append(parity)
        if witness is None and new_witness is not None:
            witness = new_witness
        tick("completed-n", n)
        print(json.dumps({"n": n, "matched": parity["matched_endpoints"],
                          "positive_innovation_rows": parity["positive_innovation_matched_rows"],
                          "candidate_found": witness is not None}), flush=True)
    assert sum(row["words_enumerated"] for row in COMPLETED) == 88209
    save('result.json', {'status': 'complete', 'scope_n': [6, 7, 8, 9, 10], 'original_P_ascending': [1, -1, -1, -1, 1], 'powered_Q_ascending': [1, -3, 1, -3, 1], 'digit_probabilities': {'-1': '1/4', '0': '1/2', '1': '1/4'}, 'trace_pair_meaning': 'a+b*tau_minus; tau_minus=(1-sqrt(13))/2', 'word_visits_per_grouping': 88209, 'results': COMPLETED, 'first_matched_additive_witness': witness, 'independent_review': False, 'limits': 'Exact declared finite domain only; no diffusive asymptotic or uniform gap.'})
    ((_J_OUTPUT / 'progress.json')).unlink()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        save('failure.json', {'status': 'failed', 'error': _record_text(repr(exc)), 'type': type(exc).__name__, 'completed_n': [r['n'] for r in COMPLETED], 'traceback': _record_text(traceback.format_exc())})
        raise
