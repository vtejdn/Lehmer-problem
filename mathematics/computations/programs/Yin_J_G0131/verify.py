import json
from pathlib import Path

HOME = Path(__file__).resolve().parent
OUT = HOME.parents[3] / "mathematics" / "computations" / "outputs" / HOME.name
N = 16


def decode(mask):
    return {i for i in range(mask.bit_length()) if (mask >> i) & 1}


def encode(poly):
    return sum(1 << i for i in poly)


def plus(a, b):
    return a ^ b


def product(a, b, precision=None):
    answer = set()
    for i in a:
        for j in b:
            if precision is not None and i+j >= precision:
                continue
            if i+j in answer:
                answer.remove(i+j)
            else:
                answer.add(i+j)
    return answer


def exponent(a, n, precision=None):
    result = {0}
    for _ in range(n):
        result = product(result, a, precision)
    return result


def division(a, b):
    assert b
    a, quotient = set(a), set()
    while a and max(a) >= max(b):
        shift = max(a)-max(b)
        quotient.add(shift)
        a ^= {j+shift for j in b}
    return quotient, a


def exact_div(a, b):
    q, r = division(a, b)
    assert not r
    return q


def inverse(a):
    assert 0 in a
    v = a ^ {0}
    result, term = set(), {0}
    for _ in range(N):
        result ^= term
        term = product(term, v, N)
    assert product(result, a, N) == {0}
    return result


def theta(g):
    chi = {1, 3, 5}
    composed = set()
    for e in g:
        composed ^= exponent(chi, e, N)
    return product(exponent(g, 5, N), inverse(composed), N)


def text(a):
    return "+".join("1" if i == 0 else "t" if i == 1 else f"t^{i}"
                    for i in sorted(a)) or "0"


def irreducible(f):
    d = max(f)
    if d < 1 or 0 not in f:
        return False
    for e in range(1, d//2+1):
        for mask in range((1 << e) | 1, 1 << (e+1), 2):
            if not division(f, decode(mask))[1]:
                return False
    return True


def all_B():
    result = {1: {0}, 3: {0, 1}}
    for n in range(5, 130, 2):
        result[n] = {j+1 for j in result[n-2]} ^ result[n-4]
    return result


B = all_B()
W = {}
for n in range(3, 130, 2):
    w = B[n]
    for d in range(3, n, 2):
        if n % d == 0:
            w = exact_div(w, W[d])
    W[n] = w


def check_factor_data(row):
    h = decode(row["mask"])
    total, by_order = {0}, {}
    seen = set()
    for item in row["factors"]:
        f, multiplicity, n = decode(item["mask"]), item["multiplicity"], item["trace_order"]
        assert item["mask"] not in seen
        seen.add(item["mask"])
        assert 1 <= max(f) <= 7 and item["degree"] == max(f)
        assert item["polynomial"] == text(f) and irreducible(f)
        assert isinstance(multiplicity, int) and multiplicity >= 1
        assert 3 <= n <= (1 << max(f))+1 <= 129 and n % 2 == 1
        assert not division(B[n], f)[1]
        assert all(division(B[k], f)[1] for k in range(3, n, 2))
        assert ((1 << max(f))-1) % n == 0 or ((1 << max(f))+1) % n == 0
        fp = exponent(f, multiplicity)
        total = product(total, fp)
        by_order[n] = product(by_order.get(n, {0}), fp)
    assert total == h
    expected_groups = []
    for n, grouped in sorted(by_order.items()):
        whole = W[n]
        k, remainder = divmod(max(grouped), max(whole))
        complete = remainder == 0 and k > 0 and exponent(whole, k) == grouped
        expected_groups.append({"order": n, "group_mask": encode(grouped),
                                "whole_mask": encode(whole), "whole_polynomial": text(whole),
                                "whole_degree": max(whole), "complete": complete,
                                "whole_multiplicity": k if complete else None})
    assert row["order_groups"] == expected_groups
    assert row["complete_product"] == all(g["complete"] for g in expected_groups)


def main():
    inputs = json.loads((HOME / "inputs.json").read_text(encoding="utf-8"))
    data = json.loads((OUT / "classification.json").read_text(encoding="utf-8"))
    assert data["scope"] == inputs
    assert inputs["precision"] == inputs["character_modulus"] == N
    assert [(c["m"], c["Q"], c["max_degree"], c["target_character"])
            for c in inputs["cases"]] == [(12, 32, 5, 10), (14, 32, 7, 9)]
    assert all(c["epsilon"] == 0 for c in inputs["cases"])
    assert [c["id"] for c in inputs["cases"]] == ["m12_q32", "m14_q32"]
    assert inputs["maximum_irreducible_degree"] == 7 and inputs["maximum_trace_order"] == 129
    assert data["status"] == "complete" and data["unique_polynomials"] == 128
    rows = data["rows"]
    assert [r["mask"] for r in rows] == list(range(1, 256, 2))
    factor_rows = 0
    for row in rows:
        h, g, a = decode(row["mask"]), decode(row["source_g_mask"]), row["ell_mod16"]
        assert row["degree"] == max(h) and row["polynomial"] == text(h)
        assert 0 in g and max(g) < N and isinstance(a, int) and 0 <= a < 16
        assert product(theta(g), exponent({0, 1}, a, N), N) == h
        expected_passes = [c["id"] for c in inputs["cases"]
                           if max(h) <= c["max_degree"] and a == c["target_character"]]
        assert row["passes"] == expected_passes
        if expected_passes:
            check_factor_data(row)
            factor_rows += 1
    expected_cases = []
    for case in inputs["cases"]:
        eligible = [r for r in rows if r["degree"] <= case["max_degree"]]
        assert len(eligible) == case["candidate_count"] == 1 << case["max_degree"]
        passing = [r["mask"] for r in eligible if case["id"] in r["passes"]]
        expected_cases.append({**case, "passing_masks": passing, "passing_count": len(passing)})
    assert data["cases"] == expected_cases
    assert inputs["calibration_odd_indices"] == list(range(1, 64, 2))
    assert inputs["theta_calibration_exponents"] == list(range(1, 16))
    assert len(data["B_calibration"]) == 32
    for item, n in zip(data["B_calibration"], inputs["calibration_odd_indices"]):
        sign = 1 if n % 4 == 1 else -1
        expected = ((1-sign*n)//4) % 16
        assert item["n"] == n and item["character"] == item["expected"] == expected
        g = decode(item["source_g_mask"])
        assert 0 in g and max(g) < N
        assert product(theta(g), exponent({0, 1}, expected, N), N) == {i for i in B[n] if i < N}
    assert data["leading_generators_checked"] == 15 and len(data["generators"]) == 15
    for item, j in zip(data["generators"], range(1, 16)):
        source = None if j & (j-1) == 0 else j-2*(j & -j)
        expected = {0, j} if source is None else theta({0, source})
        assert item == {"order": j, "mask": encode(expected), "source_exponent": source}
        assert min(expected ^ {0}) == j
    assert data["theta_controls_checked"] == 15 and len(data["theta_controls"]) == 15
    for item, e in zip(data["theta_controls"], range(1, 16)):
        expected = theta({0, e})
        assert item["exponent"] == e and item["character"] == 0 and item["unit_mask"] == encode(expected)
        g = decode(item["source_g_mask"])
        assert 0 in g and max(g) < N and theta(g) == expected
    result = {"status": "verified", "relationship": "author verification, not independent review",
              "jet_precision": N, "character_modulus": 16,
              "complete_candidate_certificates": 128,
              "passing_factorizations_and_complete_statuses": factor_rows,
              "B_calibration_certificates": 32, "theta_control_certificates": 15,
              "leading_generator_checks": 15,
              "cases": expected_cases,
              "method": "separate coefficient-set arithmetic verifies every Theta reconstruction; full factor/order/group polynomial checks"}
    partial = OUT / "verification.json.partial"
    partial.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    partial.replace(OUT / "verification.json")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
