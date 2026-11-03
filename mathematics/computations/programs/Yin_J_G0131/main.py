import json
from functools import lru_cache
from pathlib import Path

HOME = Path(__file__).resolve().parent
OUT = HOME.parents[3] / "mathematics" / "computations" / "outputs" / HOME.name
N = 16
MASK = (1 << N) - 1
CHI = (1 << 1) | (1 << 3) | (1 << 5)


def degree(a):
    return a.bit_length() - 1


def mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def power(a, n):
    result = 1
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n >>= 1
    return result


def divmod_poly(a, b):
    assert b
    quotient = 0
    while a and degree(a) >= degree(b):
        shift = degree(a) - degree(b)
        quotient ^= 1 << shift
        a ^= b << shift
    return quotient, a


def exact_div(a, b):
    q, r = divmod_poly(a, b)
    assert r == 0
    return q


def jet_mul(a, b):
    return mul(a, b) & MASK


def jet_power(a, n):
    result = 1
    while n:
        if n & 1:
            result = jet_mul(result, a)
        a = jet_mul(a, a)
        n >>= 1
    return result


def inverse(a):
    assert a & 1
    result = 1
    for n in range(1, N):
        coefficient = sum(((a >> i) & 1) * ((result >> (n-i)) & 1)
                          for i in range(1, n+1)) & 1
        result |= coefficient << n
    assert jet_mul(a, result) == 1
    return result


def compose(a):
    result = 0
    for i in range(degree(a), -1, -1):
        result = jet_mul(result, CHI) ^ ((a >> i) & 1)
    return result


def theta(a):
    return jet_mul(jet_power(a, 5), inverse(compose(a)))


GENERATORS = {}
for j in range(1, N):
    if j & (j-1) == 0:
        generator, source = 1 | (1 << j), None
    else:
        source = j - 2*(j & -j)
        assert source >= 1
        generator = theta(1 | (1 << source))
    assert (generator ^ 1) & ((1 << j)-1) == 0
    assert (generator >> j) & 1
    GENERATORS[j] = (generator, source)


def character(h):
    residual, source_g, value, steps = h & MASK, 1, 0, []
    assert residual & 1
    for j in range(1, N):
        if (residual >> j) & 1:
            generator, source = GENERATORS[j]
            residual = jet_mul(residual, inverse(generator))
            if source is None:
                value += j
            else:
                source_g = jet_mul(source_g, 1 | (1 << source))
            steps.append(j)
        assert residual & ((1 << (j+1))-1) == 1
    assert residual == 1 and 0 <= value < 16
    assert jet_mul(theta(source_g), jet_power(3, value)) == (h & MASK)
    return value, source_g, steps


def polynomial(a):
    return "+".join("1" if i == 0 else "t" if i == 1 else f"t^{i}"
                    for i in range(degree(a)+1) if (a >> i) & 1) or "0"


def irreducible(f):
    d = degree(f)
    if d < 1 or not f & 1:
        return False
    for e in range(1, d//2+1):
        for middle in range(1 << (e-1)):
            q = (1 << e) | (middle << 1) | 1
            if divmod_poly(f, q)[1] == 0:
                return False
    return True


B = {1: 1, 3: 3}
for n in range(5, 130, 2):
    B[n] = (B[n-2] << 1) ^ B[n-4]
IRREDUCIBLES = [f for d in range(1, 8)
               for f in range((1 << d) | 1, 1 << (d+1), 2)
               if irreducible(f)]


@lru_cache(None)
def primitive(n):
    value = B[n]
    for d in range(3, n, 2):
        if n % d == 0:
            value = exact_div(value, primitive(d))
    return value


def trace_order(f):
    d = degree(f)
    bound = (1 << d) + 1
    assert bound <= 129
    for n in range(3, bound+1, 2):
        if divmod_poly(B[n], f)[1] == 0:
            assert ((1 << d)-1) % n == 0 or ((1 << d)+1) % n == 0
            return n
    raise AssertionError("proved trace-order bound failed")


def factor_and_complete(h):
    remainder = h
    factors, groups = [], {}
    for f in IRREDUCIBLES:
        multiplicity = 0
        while remainder != 1 and divmod_poly(remainder, f)[1] == 0:
            remainder = exact_div(remainder, f)
            multiplicity += 1
        if multiplicity:
            n = trace_order(f)
            factors.append({"mask": f, "polynomial": polynomial(f),
                            "degree": degree(f), "multiplicity": multiplicity,
                            "trace_order": n})
            groups[n] = mul(groups.get(n, 1), power(f, multiplicity))
    assert remainder == 1
    reconstructed = 1
    for f in factors:
        reconstructed = mul(reconstructed, power(f["mask"], f["multiplicity"]))
    assert reconstructed == h
    order_groups = []
    for n, group in sorted(groups.items()):
        whole = primitive(n)
        exponent, rest = divmod(degree(group), degree(whole))
        complete = rest == 0 and exponent > 0 and power(whole, exponent) == group
        order_groups.append({"order": n, "group_mask": group,
                             "whole_mask": whole, "whole_polynomial": polynomial(whole),
                             "whole_degree": degree(whole), "complete": complete,
                             "whole_multiplicity": exponent if complete else None})
    return factors, order_groups, all(g["complete"] for g in order_groups)


def publish(path, value):
    partial = path.with_suffix(path.suffix + ".partial")
    partial.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    partial.replace(path)


def main():
    inputs = json.loads((HOME / "inputs.json").read_text(encoding="utf-8"))
    assert inputs["precision"] == inputs["character_modulus"] == 16
    assert inputs["maximum_irreducible_degree"] == 7
    assert inputs["maximum_trace_order"] == 129
    assert inputs["calibration_odd_indices"] == list(range(1, 64, 2))
    assert inputs["theta_calibration_exponents"] == list(range(1, 16))
    assert inputs["cases"] == [
        {"id": "m12_q32", "m": 12, "Q": 32, "epsilon": 0,
         "max_degree": 5, "candidate_count": 32, "target_character": 10},
        {"id": "m14_q32", "m": 14, "Q": 32, "epsilon": 0,
         "max_degree": 7, "candidate_count": 128, "target_character": 9}]
    calibration = []
    for n in inputs["calibration_odd_indices"]:
        sign = 1 if n % 4 == 1 else -1
        expected = ((1-sign*n)//4) % 16
        actual, source_g, _ = character(B[n])
        assert actual == expected
        calibration.append({"n": n, "character": actual, "expected": expected, "source_g_mask": source_g})
    theta_controls = []
    for e in inputs["theta_calibration_exponents"]:
        unit = theta(1 | (1 << e))
        value, source_g, _ = character(unit)
        assert value == 0
        theta_controls.append({"exponent": e, "unit_mask": unit, "character": value, "source_g_mask": source_g})
    rows = []
    for coefficients in range(128):
        h = 1 | (coefficients << 1)
        value, source_g, steps = character(h)
        passes = [case["id"] for case in inputs["cases"]
                  if degree(h) <= case["max_degree"] and value == case["target_character"]]
        row = {"mask": h, "polynomial": polynomial(h), "degree": degree(h),
               "ell_mod16": value, "source_g_mask": source_g,
               "eliminated_orders": steps, "passes": passes}
        if passes:
            factors, groups, complete = factor_and_complete(h)
            row.update(factors=factors, order_groups=groups, complete_product=complete)
        rows.append(row)
    cases = []
    for case in inputs["cases"]:
        eligible = [r for r in rows if r["degree"] <= case["max_degree"]]
        assert len(eligible) == case["candidate_count"]
        passing = [r["mask"] for r in eligible if case["id"] in r["passes"]]
        cases.append({**case, "passing_masks": passing, "passing_count": len(passing)})
    result = {"status": "complete", "scope": inputs, "unique_polynomials": 128,
              "leading_generators_checked": 15,
              "generators": [{"order": j, "mask": g, "source_exponent": e} for j, (g, e) in GENERATORS.items()],
              "B_calibration": calibration, "theta_controls_checked": 15,
              "theta_controls": theta_controls, "cases": cases, "rows": rows}
    OUT.mkdir(parents=True, exist_ok=True)
    publish(OUT / "classification.json", result)
    print(json.dumps({"output": str(OUT / "classification.json"), "cases": cases}, indent=2))


if __name__ == "__main__":
    main()
