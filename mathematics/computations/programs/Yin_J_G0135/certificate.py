"""Exact integer certificate; no numerical roots or factorization."""
import json
import platform
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "outputs" / HERE.name / "certificate.json"


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, sign=1):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += sign * x
    return trim(out)


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def divmonic(a, b):
    assert b[-1] == 1
    a = trim(a)
    q = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        j = len(a) - len(b)
        c = a[-1]
        q[j] += c
        for i, x in enumerate(b):
            a[j + i] -= c * x
        a = trim(a)
    return trim(q), a


def det_bareiss(matrix):
    a = [row[:] for row in matrix]
    n, previous, sign = len(a), 1, 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        current = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * current - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, previous)
                assert remainder == 0, "nonintegral Bareiss division"
                a[i][j] = quotient
            a[i][k] = 0
        previous = current
    return sign * a[-1][-1]


def main():
    inputs = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    f, q = inputs["trace_F"], inputs["q16"]
    assert len(f) == 6 and f[-1] == 1
    assert len(q) == 17 and q[-1] == q[0] == 1
    assert inputs["power_sum_range"] == [1, 32]

    def times_y(a):
        shifted = [0] + a
        lead = shifted[5]
        return [shifted[j] - lead * f[j] for j in range(5)]

    def norm(a):
        columns = [a]
        for _ in range(4):
            columns.append(times_y(columns[-1]))
        matrix = [[columns[j][i] for j in range(5)] for i in range(5)]
        return det_bareiss(matrix)

    c_previous, c_current = [2, 0, 0, 0, 0], [0, 1, 0, 0, 0]
    chebyshev_remainders = []
    sums = [32]
    for n in range(1, 33):
        if n > 1:
            shifted = times_y(c_current)
            c_previous, c_current = c_current, [shifted[j] - c_previous[j] for j in range(5)]
        chebyshev_remainders.append(c_current[:])
        sums.append(norm(c_current))

    elementary = [1]
    for k in range(1, 33):
        numerator = sum((-1) ** (i - 1) * elementary[k - i] * sums[i] for i in range(1, k + 1))
        value, remainder = divmod(numerator, k)
        assert remainder == 0, "nonintegral Newton coefficient"
        elementary.append(value)
    Q32 = list(reversed([(-1) ** k * elementary[k] for k in range(33)]))
    even, odd = q[::2], q[1::2]
    P16 = add(mul(even, even), [0] + mul(odd, odd), -1)
    quotient, remainder = divmonic(Q32, P16)
    square_substitution = [0] * (2 * len(P16) - 1)
    for j, value in enumerate(P16):
        square_substitution[2 * j] = value
    q_negative = [value * (-1) ** j for j, value in enumerate(q)]
    checks = {
        "q_product_identity": mul(q, q_negative) == square_substitution,
        "P16_monic_degree16": len(P16) == 17 and P16[-1] == 1,
        "P16_divides_Q32": remainder == [0],
        "division_reconstruction": add(mul(P16, quotient), remainder) == Q32,
        "Q32_monic_degree32": len(Q32) == 33 and Q32[-1] == 1,
        "strict_root_bound_integer": 19**4 < 2 * 16**4,
        "trace_derivative_lower_fraction": 36 * 9 > 304,
    }
    result = {
        "status": "passed" if all(checks.values()) else "failed",
        "arithmetic": "Python exact integers; Bareiss determinants and Newton identities",
        "python": platform.python_version(),
        "input": inputs,
        "chebyshev_remainders_mod_F_n1_to_32": chebyshev_remainders,
        "power_sums_n0_to_32": sums,
        "Q32_ascending": Q32,
        "E_ascending": even,
        "O_ascending": odd,
        "P16_ascending": P16,
        "quotient_ascending": quotient,
        "remainder_ascending": remainder,
        "checks": checks,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "checks": checks,
                      "P16_ascending": P16, "quotient_ascending": quotient,
                      "output": OUT.as_posix()}, indent=2))


if __name__ == "__main__":
    main()
