"""Independent finite verification: continuous halves -> full words -> parity rows.

Reviewer authored; never imports main.py or worker.py. One fixed n=6..10
execution, 180-second supervisor and 175-second internal cap; no retry.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import subprocess
import sys
import time
import traceback

HERE = (_J_PROGRAM / 'verify.py').parent
P = (1, -1, -1, -1, 1)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
SCOPE = (6, 7, 8, 9, 10)
START = None
COMPLETED = []


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


def check(ok, message):
    if not ok:
        raise AssertionError(message)


def same(actual, saved, label):
    check(actual == saved, (label, actual, saved))


def deadline():
    if time.monotonic() - START > 175:
        raise TimeoutError("Independent fixed-domain 175-second worker cap")


def save(name, data):
    target = _J_OUTPUT / name
    temporary = target.with_suffix(target.suffix + ".writing")
    temporary.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    temporary.replace(target)


def reduce_polynomial(coefficients):
    a = list(coefficients) + [0] * max(0, 4 - len(coefficients))
    while len(a) > 4:
        lead = a.pop()
        offset = len(a) - 4
        for j in range(4):
            a[offset + j] -= lead * P[j]
    return tuple(a)


def multiply(a, b):
    coefficients = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            coefficients[i + j] += x * y
    return reduce_polynomial(coefficients)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(c * x for x in a)


def powers(x, length):
    values = [ONE]
    while len(values) < length:
        values.append(multiply(values[-1], x))
    return values


def invert(matrix):
    n = len(matrix)
    a = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        c = a[col][col]
        a[col] = [x / c for x in a[col]]
        for i in range(n):
            if i != col:
                c = a[i][col]
                a[i] = [x - c * y for x, y in zip(a[i], a[col])]
    return [row[n:] for row in a]


def make_algebra():
    bp = powers((0, 1, 0, 0), 21)
    inverse = (1, 1, 1, -1)  # P(beta)/beta=0, with P(0)=1.
    same(multiply(bp[1], inverse), ONE, "inverse beta")
    ip = powers(inverse, 4)
    invbasis = invert([[bp[2 * j][i] for j in range(4)] for i in range(4)])

    @lru_cache(maxsize=None)
    def gamma_coordinates(x):
        return tuple(sum(invbase * c for invbase, c in zip(row, x)) for row in invbasis)

    def value(word, stride=1):
        return tuple(sum(c * bp[stride * k][i] for k, c in enumerate(word))
                     for i in range(4))

    def norm(x):
        sx = tuple(sum(x[j] * ip[j][i] for j in range(4)) for i in range(4))
        v = multiply(x, sx)
        b = v[2]
        same((v[1], v[3]), (2 * b, -b), "relative product in trace field")
        return (v[0] - b, b)

    same(norm(bp[1]), (1, 0), "neutral rotation norm")
    return bp, inverse, value, norm, gamma_coordinates


def sign(pair):
    # a+b*(1-sqrt(13))/2 = c+e*sqrt(13); compare rational squares.
    a, b = map(F, pair)
    c, e = a + b / 2, -b / 2
    if not c:
        return (e > 0) - (e < 0)
    if not e:
        return (c > 0) - (c < 0)
    if c > 0 and e > 0:
        return 1
    if c < 0 and e < 0:
        return -1
    gap = c * c - 13 * e * e
    check(gap != 0, "sqrt(13) irrational, nonzero rational mixed signs")
    return ((c > 0) - (c < 0)) if gap > 0 else ((e > 0) - (e < 0))


def strings(pair):
    return [str(F(x)) for x in pair]


def p_quotient(word):
    a = list(word)
    q = [0] * (len(a) - 4)
    for degree in range(len(a) - 1, 3, -1):
        q[degree - 4] = a[degree]
        for j in range(5):
            a[degree - 4 + j] -= q[degree - 4] * P[j]
    same(a, [0] * len(a), "complete original P remainder")
    return q


def verify_n(n, saved, algebra, select_candidate):
    bp, inverse, value, norm, gamma_coordinates = algebra
    entries = []
    low = defaultdict(list)
    parity = defaultdict(list)
    for index, word in enumerate(product((-1, 0, 1), repeat=n), 1):
        if index % 2048 == 0:
            deadline()
        weight = 2 ** word.count(0)
        endpoint = value(word)
        even_endpoint = value(word, 2)
        item = (word, weight)
        entries.append((word, weight, even_endpoint))
        low[endpoint].append(item)
        parity[even_endpoint].append(item)
    same(len(entries), 3 ** n, "all halfwords enumerated")
    same(sum(w for _, w, _ in entries), 4 ** n, "original half mass")
    high_targets = {scale(multiply(bp[n], y), -1): words for y, words in low.items()}
    returned = defaultdict(list)
    count = 0
    contiguous_raw = (0, 0)
    contiguous_mass = 0
    for x, leftwords in low.items():
        deadline()
        for left, wl in leftwords:
            for right, wr in high_targets.get(x, ()):
                whole = left + right
                same(value(whole), ZERO, "original complete return")
                weight = wl * wr
                endpoint = value(whole[::2], 2)
                returned[endpoint].append((whole, weight))
                contiguous_mass += weight
                contiguous_raw = add(contiguous_raw, scale(norm(x), weight))
                count += 1

    expected_rows = {tuple(r["x_gamma"]): r for r in saved["matched_rows"]}
    same(len(expected_rows), len(saved["matched_rows"]), "no duplicate saved rows")
    total = (0, 0)
    within = (F(0), F(0))
    means = (F(0), F(0))
    mean = ZERO
    mass = positive = 0
    for endpoint, fullwords in returned.items():
        deadline()
        gx = gamma_coordinates(endpoint)
        check(all(a.denominator == 1 for a in gx), "even integral gamma coordinates")
        key = tuple(int(a) for a in gx)
        check(key in expected_rows, ("missing saved row", n, key))
        other = scale(multiply(inverse, endpoint), -1)
        gy = gamma_coordinates(other)
        check(all(a.denominator == 1 for a in gy), "odd integral gamma coordinates")
        # Deduplicate actual return words, then recover both entire parity fibers.
        ew = sorted({word[::2] for word, _ in fullwords})
        ow = sorted({word[1::2] for word, _ in fullwords})
        same(ew, [word for word, _ in parity[endpoint]], "complete even fiber")
        same(ow, [word for word, _ in parity[other]], "complete odd fiber")
        same(len(fullwords), len(ew) * len(ow), "complete conditional Cartesian product")
        wsum = sum(w for _, w in fullwords)
        first = ZERO
        second = (0, 0)
        for word, w in fullwords:
            prefix = value(word[:n])
            first = add(first, scale(prefix, w))
            second = add(second, scale(norm(prefix), w))
        mean_raw = scale(norm(first), F(1, wsum))
        variance_raw = add(second, scale(mean_raw, -1))
        check(sign(second) >= 0 and sign(mean_raw) >= 0 and sign(variance_raw) >= 0,
              ("exact nonnegative conditional square/variance", n, key))
        positive += sign(variance_raw) > 0

        def marginal(words, cut):
            wsum = 0
            m = ZERO
            b = (0, 0)
            for word in words:
                w = 2 ** word.count(0)
                prefix = value(word[:cut], 2)
                wsum += w
                m = add(m, scale(prefix, w))
                b = add(b, scale(norm(prefix), w))
            return wsum, m, b

        we, me, be = marginal(ew, (n + 1) // 2)
        wo, mo, bo = marginal(ow, n // 2)
        same(wsum, we * wo, "original conditional product weight")
        actual = {"x_gamma": list(key), "y_gamma": [int(a) for a in gy],
                  "even_weight": we, "odd_weight": wo,
                  "even_word_count": len(ew), "odd_word_count": len(ow),
                  "even_prefix_first_beta": list(me), "odd_prefix_first_beta": list(mo),
                  "even_prefix_second_trace": list(be), "odd_prefix_second_trace": list(bo),
                  "raw_total_trace": strings(second), "raw_within_trace": strings(variance_raw),
                  "raw_means_trace": strings(mean_raw)}
        same(actual, expected_rows[key], ("complete matched row", n, key))
        total, within, means = add(total, second), add(within, variance_raw), add(means, mean_raw)
        mean = add(mean, first)
        mass += wsum
    same(len(returned), len(expected_rows), "all saved rows covered")
    same(mean, ZERO, "full original midpoint centered")
    same(total, contiguous_raw, "direct continuous-half moment")
    same(mass, contiguous_mass, "direct continuous-half return mass")

    rejected_order = rejected_support = 0
    for endpoint, words in parity.items():
        y = scale(multiply(inverse, endpoint), -1)
        gy = gamma_coordinates(y)
        is_integral = all(a.denominator == 1 for a in gy)
        gx = gamma_coordinates(endpoint)
        same(is_integral, sum(gx[j] * (-1) ** j for j in range(4)) % 3 == 0,
             "independent inverse-basis order criterion")
        if not is_integral:
            rejected_order += 1
        elif y not in parity:
            rejected_support += 1
        else:
            check(endpoint in returned, "no missed matched endpoint")
    actual = {"n": n, "original_length": 2 * n, "words_enumerated": 3 ** n,
              "raw_half_mass": 4 ** n, "unique_gamma_endpoints": len(parity),
              "ambiguous_gamma_endpoints": sum(len(v) > 1 for v in parity.values()),
              "order_rejected_endpoints": rejected_order,
              "order_ok_support_rejected_endpoints": rejected_support,
              "matched_endpoints": len(returned), "full_return_word_count": count,
              "positive_innovation_matched_rows": positive,
              "return_integer_numerator": mass, "return_denominator": 16 ** n,
              "return_probability": str(F(mass, 16 ** n)),
              "midpoint_second_trace_pair": strings(scale(total, F(1, mass))),
              "within_parity_trace_pair": strings(scale(within, F(1, mass))),
              "conditional_mean_trace_pair": strings(scale(means, F(1, mass))),
              "raw_total_trace_pair": strings(total),
              "complete_sign_symmetry_and_centering": True,
              "all_covariance_trace_signs_exact": True,
              "contiguous_half_crosscheck": {
                  "words_enumerated": 3 ** n, "unique_beta_endpoints": len(low),
                  "return_integer_numerator": mass, "full_return_word_count": count,
                  "raw_second_trace_pair": strings(total), "exact_agreement": True}}
    same(actual, {k: v for k, v in saved.items() if k != "matched_rows"},
         ("all original summary fields", n))
    for endpoint, words in parity.items():
        same(parity.get(scale(endpoint, -1)),
             sorted([(tuple(-a for a in word), w) for word, w in words]),
             "complete law sign symmetry")

    candidate = None
    if select_candidate:
        cut = (n + 1) // 2
        for word, wa, endpoint in entries:
            if endpoint not in returned:
                continue
            for j in range(n - 5):
                if not j < cut < j + 6:
                    continue
                aa, bb = word[j], word[j + 5]
                if aa not in (0, 1) or bb not in (0, 1) or word[j + 1:j + 5] != (-1,) * 4:
                    continue
                other_word = word[:j] + (aa - 1, 1, 1, 1, 1, bb - 1) + word[j + 6:]
                same(value(other_word, 2), endpoint, "candidate equal endpoint")
                other_endpoint = scale(multiply(inverse, endpoint), -1)
                odd = parity[other_endpoint][0][0]
                diff = add(value(word[:cut], 2), scale(value(other_word[:cut], 2), -1))
                diff_norm = norm(diff)
                if sign(diff_norm) <= 0:
                    continue
                wb, wo = 2 ** other_word.count(0), 2 ** odd.count(0)
                we = sum(w for _, w in parity[endpoint])
                wy = sum(w for _, w in parity[other_endpoint])
                wholea = tuple(a for pair in zip(word, odd) for a in pair)
                wholeb = tuple(a for pair in zip(other_word, odd) for a in pair)
                outside = word[:j] + (0,) * 6 + word[j + 6:]
                factor = F(wa * wb * wy, we * mass)
                candidate = {"n": n, "shift": j, "A": aa, "B": bb,
                    "even_a": list(word), "even_b": list(other_word), "odd": list(odd),
                    "outside_even_digits": list(outside),
                    "outside_translation_gamma_basis": [int(a) for a in gamma_coordinates(value(outside, 2))],
                    "even_endpoint_gamma_basis": [int(a) for a in gamma_coordinates(endpoint)],
                    "odd_endpoint_gamma_basis": [int(a) for a in gamma_coordinates(other_endpoint)],
                    "original_return_word_a": list(wholea), "original_return_word_b": list(wholeb),
                    "original_p_quotient_a": p_quotient(wholea), "original_p_quotient_b": p_quotient(wholeb),
                    "zero_remainders": True, "even_a_integer_weight": wa,
                    "even_b_integer_weight": wb, "odd_word_integer_weight": wo,
                    "whole_a_integer_weight": wa * wo, "whole_b_integer_weight": wb * wo,
                    "whole_probability_denominator": 16 ** n,
                    "even_total_integer_weight": we, "odd_total_integer_weight": wy,
                    "return_weight_numerator": mass,
                    "actual_conditional_endpoint_probability": str(F(we * wy, mass)),
                    "midpoint_difference_square_trace_pair": strings(diff_norm),
                    "pair_bound_multiplier": str(factor),
                    "actual_weighted_innovation_lower_trace_pair": strings(scale(diff_norm, factor))}
                break
            if candidate is not None:
                break
    actual["complete_matched_rows_independently_compared"] = len(returned)
    actual["full_return_words_independently_reconstructed"] = count
    return actual, candidate


def worker():
    global START
    START = time.monotonic()
    source = json.loads(((_J_OUTPUT / 'result.json')).read_text(encoding="utf-8"))
    same(source["status"], "complete", "original status")
    same(source["scope_n"], list(SCOPE), "exact fixed domain")
    same(source["original_P_ascending"], list(P), "original minimal polynomial")
    same(source["powered_Q_ascending"], [1, -3, 1, -3, 1], "powered polynomial")
    same(source["digit_probabilities"], {"-1": "1/4", "0": "1/2", "1": "1/4"}, "original probabilities")
    same(source["trace_pair_meaning"], "a+b*tau_minus; tau_minus=(1-sqrt(13))/2", "trace embedding")
    same(source["word_visits_per_grouping"], 88209, "declared visits")
    same([r["n"] for r in source["results"]], list(SCOPE), "ordered complete rows")
    algebra = make_algebra()
    candidate = None
    for n, saved in zip(SCOPE, source["results"]):
        row, possible = verify_n(n, saved, algebra, candidate is None)
        if possible is not None:
            candidate = possible
        COMPLETED.append(row)
        save("verification-progress.json", {"status": "in-progress", "results": COMPLETED})
        print(json.dumps({"verified_n": n, "matched_rows": row["matched_endpoints"],
                          "reconstructed_return_words": row["full_return_word_count"]}), flush=True)
    same(candidate, source["first_matched_additive_witness"], "entire deterministic first witness")
    deadline()
    save('verification-progress.json', {'status': 'worker-complete', 'scope_n': list(SCOPE), 'method': 'Independent original beta contiguous-half full-word reconstruction, then exact parity regrouping and direct conditional variance.', 'imported_author_program': False, 'arithmetic': 'integer and Fraction only', 'results': COMPLETED, 'first_matched_additive_witness': candidate, 'every_matched_row_and_summary_equal': True, 'limits': 'Only n=6..10; no asymptotic or arbitrary-input inference.'})


def supervisor():
    command = [sys.executable, "-B", "-X", "utf8", str(_J_PROGRAM / "verify.py"), "--child"]
    try:
        run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=180)
        if run.stdout:
            print(run.stdout, end="")
        if run.stderr:
            print(run.stderr, end="", file=sys.stderr)
        check(run.returncode == 0, ("independent worker failed", run.returncode))
        data = json.loads((_J_OUTPUT / "verification-progress.json").read_text(encoding="utf-8"))
        same(data["status"], "worker-complete", "worker completion")
        data["status"] = "complete"
        save("verification.json", data)
        (_J_OUTPUT / "verification-progress.json").unlink()
        return 0
    except Exception as exc:
        save("verification-failure.json", {"status":"failed", "error":_record_text(repr(exc))})
        return 1


if __name__ == "__main__":
    if sys.argv[1:] == ["--child"]:
        try:
            worker()
        except Exception:
            traceback.print_exc()
            raise
    else:
        check(not sys.argv[1:], "No adjustable domain or retry arguments")
        raise SystemExit(supervisor())
