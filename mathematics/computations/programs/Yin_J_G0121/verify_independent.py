"""Independent C631 check using polynomial division and monomial interval bounds.

No contributor module is imported.
Reconstruct the finite data from native inputs, then compare the contributor
certificate and discovery output; neither generated file is a correctness oracle.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = ROOT / "mathematics" / "computations" / "outputs" / HERE.name
P = (1, -1, -1, -1, 1)
Z = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)


def reduce_poly(coefficients):
    a = list(coefficients) + [0] * max(0, 4 - len(coefficients))
    for j in range(len(a) - 1, 3, -1):
        lead = a[j]
        for i, coefficient in enumerate(P):
            a[j - 4 + i] -= lead * coefficient
    return tuple(a[:4])


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return reduce_poly(out)


def shifted(a, exponent):
    factor = (0, 1, 0, 0) if exponent >= 0 else (1, 1, 1, -1)
    while exponent:
        if abs(exponent) % 2:
            a = multiply(a, factor)
        factor = multiply(factor, factor)
        exponent = abs(exponent) // 2
    return a


def negative(a):
    return tuple(-v for v in a)


def difference(a, b):
    return tuple(x - y for x, y in zip(a, b))


def bounds(coefficients, interval):
    """Termwise enclosure, independent of contributor's interval Horner code."""
    lower, upper = interval
    assert 0 < lower <= upper
    lows, highs = [], []
    for j, coefficient in enumerate(coefficients):
        endpoints = (coefficient * lower**j, coefficient * upper**j)
        lows.append(min(endpoints))
        highs.append(max(endpoints))
    return sum(lows), sum(highs)


def scaled_absolute(coefficients, interval, factor):
    lower, upper = bounds(coefficients, interval)
    near = 0 if lower <= 0 <= upper else min(abs(lower), abs(upper))
    far = max(abs(lower), abs(upper))
    assert 0 < factor[0] <= factor[1]
    return near * factor[0], far * factor[1]


def below_two(interval):
    assert interval[1] < 2 or interval[0] > 2, interval
    return interval[1] < 2


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    native = read_json(HERE / "inputs.json")
    assert native["starting_word_input"] == "mathematics/computations/programs/Yin_J_G0118/inputs.json"
    original = read_json(ROOT / native["starting_word_input"])
    assert original["polynomial_ascending"] == list(P)
    lo = Fraction(*original["beta_lower"])
    hi = Fraction(*original["beta_upper"])
    assert Fraction(17, 10) < lo < hi < Fraction(18, 10)
    assert bounds(P, (lo, lo))[0] < 0 < bounds(P, (hi, hi))[0]
    # P' is positive throughout the encompassing [1.7,1.8] bracket.
    assert 4 * Fraction(17, 10)**3 - 3 * Fraction(18, 10)**2 - 2 * Fraction(18, 10) - 1 > 0
    real_interval = (lo, hi)
    reciprocal_interval = (1 / hi, 1 / lo)
    factor = (lo - 1, hi - 1)
    assert multiply((0, 1, 0, 0), (1, 1, 1, -1)) == ONE
    unit_inverse = (-2, -1, 0, 1)
    assert multiply((-1, 1, 0, 0), unit_inverse) == ONE
    multiplier = shifted(unit_inverse, 4)
    assert tuple(shifted(multiplier, j)[3] for j in range(4)) == (2, 3, 5, 9)

    def coordinate(q):
        return multiply(multiplier, q)[3]

    measures = {}
    for theta in product(range(-2, 3), repeat=4):
        a = below_two(scaled_absolute(theta, real_interval, factor))
        r = below_two(scaled_absolute(theta[::-1], real_interval, factor))
        measures[theta] = (a, r)
        assert multiply(unit_inverse, theta)[3] == sum(theta)
    patterns = list(product((-1, 0, 1), repeat=4))
    expected_pairs = []
    counts = dict(YCY=0, CYC=0, YCY_lambda_change=0, CYC_lambda_change=0)
    for i, u in enumerate(patterns):
        for j, v in enumerate(patterns):
            delta = difference(v, u)
            a_u, r_u = measures[u]
            a_v, r_v = measures[v]
            a_d, r_d = measures[delta]
            ycy = a_d and r_d and r_u and r_v
            cyc = a_u and a_v and a_d and r_d
            increment = sum(delta)
            assert coordinate(shifted(delta, -4)) == increment
            expected_pairs.append(dict(u_index=i, v_index=j, YCY=ycy, CYC=cyc,
                                       YCY_lambda_change=increment, CYC_lambda_change=-increment))
            counts["YCY"] += ycy
            counts["CYC"] += cyc
            counts["YCY_lambda_change"] += ycy and increment != 0
            counts["CYC_lambda_change"] += cyc and increment != 0
    assert counts == dict(YCY=183, CYC=183, YCY_lambda_change=36, CYC_lambda_change=36)
    for i, u in enumerate(patterns):
        for j, v in enumerate(patterns):
            reversed_pair = expected_pairs[patterns.index(u[::-1]) * 81 + patterns.index(v[::-1])]
            assert expected_pairs[i * 81 + j]["YCY"] == reversed_pair["CYC"]
    short_patterns = [p for p in patterns if all(measures[p])]
    h_basis = [(-1, 1, 0, 0), (0, -1, 1, 0), (0, 0, -1, 1)]
    extra = (-1, 1, 1, -1)
    assert set(short_patterns) == {Z, *h_basis, *(negative(p) for p in h_basis), extra, negative(extra)}
    for h in h_basis:
        pair = expected_pairs[patterns.index(Z) * 81 + patterns.index(h)]
        assert pair["YCY"] and pair["CYC"]
    special_u, special_v = tuple(native["u"]), tuple(native["v"])
    assert special_u == (1, -1, -1, 0) and special_v == (0, 1, 0, -1)
    assert expected_pairs[patterns.index(special_u) * 81 + patterns.index(special_v)]["YCY"]
    assert coordinate(shifted(difference(special_v, special_u), -4)) == 1

    k = native["tail_length"]
    assert k == original["tail_length"] == 24
    c0, ca, cp, cm = (-3, 3, 1, -1), (-3, 2, 0, 0), (0, 3, 0, -1), (-2, 0, -1, 1)
    assert original["c"] == list(c0)
    assert difference(cp, c0) == shifted(difference(special_v, special_u), -4) == (3, 0, -1, 0)
    assert (coordinate(c0), coordinate(cp), coordinate(cm)) == (-1, 0, 0)
    for q in (c0, ca, cp, cm, Z, shifted(c0, 4), shifted(cp, 4), shifted(cm, 4)):
        assert scaled_absolute(q, real_interval, factor)[1] < 1
        assert scaled_absolute(q, reciprocal_interval, factor)[1] < lo
    targets = {"right_a": ca, "right_cp": cp, "right_cm": cm,
               "left_cp": negative(shifted(cp, 28)), "left_cm": negative(shifted(cm, 28))}
    for name, target in targets.items():
        assert len(native[name]) == 24 and set(native[name]) <= {-1, 0, 1}
        assert reduce_poly(native[name]) == target
    assert reduce_poly(original["right"]) == c0
    assert reduce_poly(original["left"]) == negative(shifted(c0, 28))
    assert native["short_middle_one"] == [1, -1, 0, 0]
    assert native["short_middle_two"] == [0, -1, 1, 0]
    words = [original["left"] + [0]*4 + original["right"],
             original["left"] + list(special_u) + native["right_a"],
             native["left_cp"] + list(special_v) + native["right_a"],
             native["left_cp"] + [0]*4 + native["right_cp"],
             native["left_cp"] + [1, -1, 0, 0] + native["right_cm"],
             native["left_cm"] + [0]*4 + native["right_cm"],
             native["left_cm"] + [0, -1, 1, 0] + [0]*24,
             [0]*52]
    assert all(len(w) == 52 and set(w) <= {-1, 0, 1} and reduce_poly(w) == Z for w in words)
    zeros = [w.count(0) for w in words]
    assert zeros == [15, 13, 15, 16, 14, 16, 32, 52]
    endpoints = [shifted(c0, 4), negative(shifted(ca, 28)), shifted(cp, 4),
                 shifted(cp, 4), negative(shifted(cm, 28)), shifted(cm, 4), Z]
    zero_blocks = [8, 8, 10, 8, 10, 26, 28]
    transitions = []
    for j, (a, b) in enumerate(zip(words, words[1:])):
        left_fixed, right_fixed = a[:24] == b[:24], a[28:] == b[28:]
        assert left_fixed != right_fixed
        varied = b[24:] if left_fixed else b[:28]
        assert reduce_poly(varied) == endpoints[j] and varied.count(0) == zero_blocks[j]
        transitions.append(dict(**{"from": j, "to": j + 1}, type="Y" if left_fixed else "C",
                                conditional_length=28, conditional_endpoint=list(endpoints[j]),
                                target_variable_zero_count=zero_blocks[j],
                                K_numerator_power_two=zero_blocks[j]-1,
                                K_denominator="c_28(conditional_endpoint)",
                                Q_numerator_power_two=zeros[j]+zero_blocks[j]-1,
                                Q_denominator="c_52(0) c_28(conditional_endpoint)"))
    assert [t["type"] for t in transitions] == ["Y", "C", "Y", "Y", "C", "Y", "C"]
    exponent = sum(zero_blocks) - 7 * (2 * 28 + 1)
    assert exponent == -301 and zeros[0] - 2 * 52 == -89

    # Reconstruct the discovery table with endpoint sets and generic reduction.
    half = {Z}
    operations = 0
    for j in range(12):
        operations += 3 * len(half)
        p = reduce_poly([0] * j + [1])
        half = {tuple(q[i] + d * p[i] for i in range(4)) for q in half for d in (-1, 0, 1)}
        assert len(half) <= 3**(j+1)
    assert len(half) == 62029 and operations == 165528
    discovery = read_json(OUT / "discovery.json")
    assert discovery["half_table_size"] == len(half) and discovery["candidate_operations"] == operations
    assert discovery["tail_length"] == 24 and set(discovery["witnesses"]) == set(targets)
    for name, target in targets.items():
        entry = discovery["witnesses"][name]
        assert entry["digits"] == native[name] and tuple(entry["target"]) == target
        assert reduce_poly(entry["digits"][:12]) in half and reduce_poly(entry["digits"][12:]) in half
    certificate = read_json(OUT / "certificate.json")
    assert certificate["pairs"] == expected_pairs and certificate["count"] == counts
    assert certificate["pair_count"] == 6561 and certificate["n"] == 26
    assert certificate["pattern_words"] == [list(p) for p in patterns]
    assert certificate["chain"] == words and certificate["word_zero_counts"] == zeros
    assert certificate["transitions"] == transitions
    assert certificate["selected_seven_update_lower_bound_exponent"] == exponent
    assert (OUT / "certificate.json").stat().st_size < 4 * 1024 * 1024
    result = dict(result="PASS", pair_count=6561, counts=counts, short_patterns=len(short_patterns),
                  states=8, transitions=7, word_zero_counts=zeros, target_zero_counts=zero_blocks,
                  following_lower_bound_exponent=exponent, half_endpoints=len(half),
                  discovery_candidate_operations=operations,
                  method="independent polynomial division, termwise rational intervals and endpoint sets",
                  limits="No complete c_28 or c_52 values, finite component census, uniform mass or load computed.")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "independent_verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
