"""Exact finite evaluation of the minimal weighted q=3 invariant extension.

All inputs are embedded integers.  This is author computation, not an
independent review.  The mathematical lattice is specified in L455 v2.
"""

import json


COEFFICIENT_COUNT = 49
U_INPUT = (1, -3, 1, -3, 1)
V_INPUT = (1, -7, -15, -7, 1)
WEIGHTS = (0, 4, 4, 8, 8, 12, 8)
EXPONENTS = (0, 1, 1, 1, 2, 2, 2)
CASES = (
    (9, 25, list(range(19)) + [21, 22, 24]),
    (13, 49, list(range(46)) + [48]),
)


def convolution(a, b):
    return [sum(a[k] * b[n - k] for k in range(n + 1))
            for n in range(COEFFICIENT_COUNT)]


def subtract(a, b):
    return [x - y for x, y in zip(a, b)]


def trace_zeta(n):
    return 2 if n % 3 == 0 else -1


def rotated_pair(a):
    """Coefficients of A(zeta*x) A(zeta^2*x), with zeta^2+zeta+1=0."""
    result = []
    for n in range(COEFFICIENT_COUNT):
        residues = [sum(a[k] * a[n - k] for k in range(n + 1)
                        if (2 * n - k) % 3 == ell) for ell in range(3)]
        assert residues[1] == residues[2]
        result.append(residues[0] - residues[2])
    return result


def build_normalized_generators():
    pad = lambda a: list(a) + [0] * (COEFFICIENT_COUNT - len(a))
    u, v = pad(U_INPUT), pad(V_INPUT)
    uv = convolution(u, v)
    f = [1] + [0] * (COEFFICIENT_COUNT - 1)
    for n in range(1, COEFFICIENT_COUNT):
        numerator = uv[n] - sum(f[k] * f[n - k] for k in range(1, n))
        assert numerator % 2 == 0
        f[n] = numerator // 2
    assert convolution(f, f) == uv
    s = [trace_zeta(n) * f[n] for n in range(COEFFICIENT_COUNT)]
    u_sum = [trace_zeta(n) * u[n] for n in range(COEFFICIENT_COUNT)]
    t, c = rotated_pair(f), rotated_pair(u)
    w = [sum(u[k] * f[n - k] * trace_zeta(n + k)
             for k in range(n + 1)) for n in range(COEFFICIENT_COUNT)]
    delta_0, delta_sum, t_minus_c = subtract(f, u), subtract(s, u_sum), subtract(t, c)
    delta_12 = [t[n] - w[n] + c[n] for n in range(COEFFICIENT_COUNT)]
    generators = [pad((1,)), delta_0, delta_sum, t_minus_c,
                  convolution(delta_0, delta_sum),
                  convolution(delta_0, t_minus_c), delta_12]
    normalized = []
    for series, exponent in zip(generators, EXPONENTS):
        divisor = 1 << exponent
        assert all(value % divisor == 0 for value in series)
        normalized.append([value // divisor for value in series])
    return normalized


def independent_rows(rows):
    pivots, selected = {}, []
    for index, row in enumerate(rows):
        while row:
            pivot = (row & -row).bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                selected.append(index)
                break
    return selected


def run_case(normalized, window, row_count, expected_rows):
    columns = [(i, j) for i, weight in enumerate(WEIGHTS)
               for j in range(max(0, window - weight))]
    rows = [sum(((normalized[i][n - j] if n >= j else 0) & 1) << k
                for k, (i, j) in enumerate(columns)) for n in range(row_count)]
    selected = independent_rows(rows)
    assert selected == expected_rows
    assert len(selected) == len(columns)
    assert len(independent_rows([rows[n] for n in expected_rows])) == len(columns)
    exponents = sorted(EXPONENTS[i] for i, _ in columns)
    expected_counts = (9, 11, 2) if window == 9 else (13, 23, 11)
    counts = tuple(exponents.count(e) for e in range(3))
    assert counts == expected_counts
    return {
        "N": window, "rows": row_count, "columns": len(columns),
        "normalized_binary_rank": len(selected), "odd_minor_rows": selected,
        "dyadic_smith_exponent_counts": dict(enumerate(counts)),
        "full_minor_minimum_dyadic_valuation": sum(exponents),
    }


def main():
    normalized = build_normalized_generators()
    results = [run_case(normalized, *case) for case in CASES]
    print(json.dumps({"coefficient_count": COEFFICIENT_COUNT, "cases": results}, indent=2))


if __name__ == "__main__":
    main()
