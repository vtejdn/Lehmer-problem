"""Independent fixed-input review of C633 and the J122 certificate.

No author modules are imported.  Direct signed monomial enclosures certify
real inequalities; generic polynomial reduction certifies ring identities.
The retained J121 table is required and every one of its verdicts is checked.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = ROOT / "mathematics" / "computations" / "outputs" / HERE.name
P = (1, -1, -1, -1, 1)
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def reduced(coefficients):
    result = list(coefficients)
    result.extend([0] * max(0, 4 - len(result)))
    for degree in range(len(result) - 1, 3, -1):
        leading = result[degree]
        for j in range(5):
            result[degree - 4 + j] -= leading * P[j]
    assert not any(result[4:])
    return tuple(result[:4])


def times(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return reduced(result)


def shift(a, exponent):
    multiplier = (0, 1, 0, 0) if exponent >= 0 else (1, 1, 1, -1)
    for _ in range(abs(exponent)):
        a = times(a, multiplier)
    return a


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def coordinate(a):
    return sum(x * y for x, y in zip(a, (2, 3, 5, 9)))


def interval(coefficients, lower, upper):
    """Independent direct-power enclosure, for a positive argument."""
    assert 0 < lower <= upper
    left = Fraction(0)
    right = Fraction(0)
    for degree, coefficient in enumerate(coefficients):
        endpoints = (coefficient * lower**degree, coefficient * upper**degree)
        left += min(endpoints)
        right += max(endpoints)
    return left, right


def absolute(bounds):
    lower, upper = bounds
    return (0 if lower <= 0 <= upper else min(abs(lower), abs(upper)),
            max(abs(lower), abs(upper)))


def encoded(bounds):
    return [[Fraction(x).numerator, Fraction(x).denominator] for x in bounds]


def strict_certificate(bounds, threshold):
    if bounds[1] < threshold:
        return True
    assert bounds[0] > threshold, (bounds, threshold)
    return False


def main():
    local = load(HERE / "inputs.json")
    assert local["root_input"] == "mathematics/computations/programs/Yin_J_G0118/inputs.json"
    assert local["pair_input"] == "mathematics/computations/outputs/Yin_J_G0121/certificate.json"
    root_input = load(ROOT / local["root_input"])
    previous = load(ROOT / local["pair_input"])
    certificate = load(OUT / "certificate.json")
    assert tuple(root_input["polynomial_ascending"]) == P
    lower = Fraction(*root_input["beta_lower"])
    upper = Fraction(*root_input["beta_upper"])
    assert Fraction(17, 10) < lower < upper < Fraction(18, 10)
    assert interval(P, lower, lower)[0] < 0 < interval(P, upper, upper)[0]
    # P(t)/t^2 = (t + 1/t)^2 - (t + 1/t) - 3 identifies
    # the unique root > 1; the opposite signs select that root.
    inverse_lower, inverse_upper = 1 / upper, 1 / lower
    b_lower, b_upper = 1 / (upper - 1), 1 / (lower - 1)
    s_lower, s_upper = upper / (upper - 1), lower / (lower - 1)
    eps_plus = Fraction(*local["epsilon_plus"])
    eps_minus = Fraction(*local["epsilon_minus"])
    assert (eps_plus, eps_minus) == (Fraction(1, 100), Fraction(1, 5))
    c0, a, cp, cm = (-3, 3, 1, -1), (-3, 2, 0, 0), (0, 3, 0, -1), (-2, 0, -1, 1)
    right = (c0, a, cp, cm, ZERO)
    left = (c0, cp, cm, ZERO)
    assert tuple(map(tuple, local["right_labels"])) == right
    assert tuple(map(tuple, local["left_base_labels"])) == left
    assert shift(shift(ONE, -4), 4) == ONE
    inverse_beta_minus_one = (-2, -1, 0, 1)
    assert times((-1, 1, 0, 0), inverse_beta_minus_one) == ONE
    for i in range(4):
        basis = tuple(int(i == j) for j in range(4))
        assert times(shift(basis, 4), inverse_beta_minus_one)[3] == coordinate(basis)
    margins = []
    for side, labels in (("right", right), ("left", left)):
        for base in labels:
            label = base if side == "right" else shift(base, 4)
            ep = eps_plus if side == "right" else upper**4 * eps_plus
            em = eps_minus if side == "right" else inverse_upper**4 * eps_minus
            expanding = b_lower - absolute(interval(label, lower, upper))[1] - ep
            stable = s_lower - absolute(interval(label, inverse_lower, inverse_upper))[1] - em
            assert expanding > 0 and stable > 0
            margins.append({"side": side, "label": label,
                            "positive_lower_margins": encoded((expanding, stable))})
    middle = (ZERO, (1, -1, -1, 0), (0, 1, 0, -1), ZERO,
              (1, -1, 0, 0), ZERO, (0, -1, 1, 0), ZERO)
    right_chain = (c0, a, a, cp, cm, cm, ZERO, ZERO)
    left_chain = tuple(shift(q, 4) for q in (c0, c0, cp, cp, cp, cm, cm, ZERO))
    for q, y, theta in zip(right_chain, left_chain, middle):
        assert plus(shift(q, 4), theta) == y
        assert set(theta) <= {-1, 0, 1}
    for i, kind in enumerate(("Y", "C", "Y", "Y", "C", "Y", "C")):
        assert (left_chain[i] == left_chain[i + 1]) == (kind == "Y")
        assert (right_chain[i] == right_chain[i + 1]) == (kind == "C")
    assert max(sum(map(abs, q)) for q in right) == 8
    assert [coordinate(q) for q in (c0, cp, cm, ZERO)] == [-1, 0, 0, 0]

    @lru_cache(None)
    def admissible(theta):
        # Multiply the unreduced polynomial by (t-1), before enclosing.
        coefficients = [0] * (len(theta) + 1)
        for i, value in enumerate(theta):
            coefficients[i] -= value
            coefficients[i + 1] += value
        return strict_certificate(absolute(interval(coefficients, lower, upper)), 2)

    words = tuple(map(tuple, previous["pattern_words"]))
    assert len(words) == 81 and set(words) == set(product((-1, 0, 1), repeat=4))
    short_patterns = [theta for theta in words if admissible(theta) and admissible(theta[::-1])]
    assert len(short_patterns) == 9 and all(sum(theta) == 0 for theta in short_patterns)
    table = previous["pairs"]
    assert previous["pair_count"] == len(table) == 6561
    assert {(r["u_index"], r["v_index"]) for r in table} == set(product(range(81), repeat=2))
    positive_occurrences = []
    translations = set()
    counts = {"YCY": 0, "CYC": 0}
    nonzero_counts = {"YCY": 0, "CYC": 0}
    for row in table:
        u, v = words[row["u_index"]], words[row["v_index"]]
        difference = minus(v, u)
        ycy_tests = (admissible(difference), admissible(u[::-1]),
                     admissible(v[::-1]), admissible(difference[::-1]))
        cyc_tests = (admissible(u), admissible(v),
                     admissible(difference), admissible(difference[::-1]))
        for kind, passes in (("YCY", all(ycy_tests)), ("CYC", all(cyc_tests))):
            assert row[kind] is passes
            delta_middle = difference if kind == "YCY" else tuple(-x for x in difference)
            increment = sum(delta_middle)
            assert row[kind + "_lambda_change"] == increment
            if passes:
                counts[kind] += 1
                assert increment in (-1, 0, 1)
                nonzero_counts[kind] += int(increment != 0)
                if increment == 1:
                    translations.add(delta_middle)
                    positive_occurrences.append((row["u_index"], row["v_index"], kind, delta_middle))
    expected = {(-2, 2, 2, -1), (-1, 1, 2, -1), (-1, 2, 0, 0),
                (-1, 2, 1, -1), (-1, 2, 2, -2), (0, 0, 2, -1)}
    assert counts == {"YCY": 183, "CYC": 183}
    assert nonzero_counts == {"YCY": 36, "CYC": 36}
    assert translations == expected and len(positive_occurrences) == 36
    blocked = (-3, 9, 1, -3)
    assert tuple(local["blocked_label"]) == blocked
    assert coordinate(blocked) == -1 and sum(map(abs, blocked)) == 16
    assert absolute(interval(shift(blocked, 4), lower, upper))[1] < b_lower
    assert absolute(interval(blocked, inverse_lower, inverse_upper))[1] < s_lower
    failures = []
    for translation in sorted(translations):
        delta = shift(translation, -4)
        target = plus(blocked, delta)
        expanding = absolute(interval(shift(target, 4), lower, upper))[0] - b_upper
        stable = absolute(interval(target, inverse_lower, inverse_upper))[0] - s_upper
        assert coordinate(delta) == 1 and (expanding > 0 or stable > 0)
        failures.append({"w": translation, "delta": delta, "target": target,
                         "fails_expanding": expanding > 0, "fails_stable": stable > 0,
                         "violation_lower_bounds": encoded((expanding, stable))})
    assert certificate["root_bracket"] == encoded((lower, upper))
    assert certificate["strict_margin_count"] == 18
    assert [(r["side"], tuple(r["label"])) for r in certificate["margin_records"]] == [
        (r["side"], r["label"]) for r in margins]
    assert certificate["reused_pair_coverage"] == counts
    assert set(map(tuple, certificate["positive_translations"])) == expected
    assert [(r["u_index"], r["v_index"], r["kind"], tuple(r["w"]))
            for r in certificate["positive_pair_occurrences"]] == positive_occurrences
    assert tuple(certificate["blocked_label"]) == blocked
    assert len(certificate["endpoint_failures"]) == 6
    for authored, independent in zip(certificate["endpoint_failures"], failures):
        for key in ("w", "delta", "target"):
            assert tuple(authored[key]) == independent[key]
        for key in ("fails_expanding", "fails_stable"):
            assert authored[key] is independent[key]
    result = {"independent_fixed_input_review": "passed", "strict_margin_count": 18,
              "short_patterns_rechecked": 81, "admissible_short_patterns": 9,
              "pair_rows_rechecked": 6561, "order_verdicts_rechecked": 13122,
              "accepted_pair_counts": counts, "nonzero_pair_counts": nonzero_counts,
              "positive_pair_occurrences": 36, "positive_translations": sorted(translations),
              "margin_records": margins, "endpoint_failures": failures,
              "limits": "Fixed exact local arithmetic and retained complete pair table; no new state or length search."}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "independent_verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "strict_margins": 18, "pair_rows": 6561,
                      "positive_occurrences": 36, "positive_translations": 6, "endpoint_failures": 6}))


if __name__ == "__main__":
    main()
