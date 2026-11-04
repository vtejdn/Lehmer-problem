#!/usr/bin/env python3
"""Replay the retained exact norm-one finite comparison certificates.

Run ``python verify_unit_cap_inputs.py`` from this program directory, or invoke
the script by path from any directory.
Only Python's standard library is used; the sole input is inputs/unit-cap-certificates.json in this J group.  The calculation
checks existing witnesses.  It neither searches for directions nor optimizes.

The mathematical interface is deliberately small.  Every coefficient list is
in ascending order.  For each monic P of degree d, N=2d and q>0, the retained input
gives the complete integer triples B,F,U with F=qB-PU.  We compute the signed
norm of B as the determinant of multiplication by B on Q[t]/(P), and compute
the energy and every correlation directly from the original F coefficients.

For the chosen columns, write e_j=||F_j||^2/q^2 and
H[l,j]=sum_i F_j[i] F_j[i+l]/q^2, 1 <= l < N.  The primal problem is

    minimize 2 ||H v||_1 subject to v>=0, e.v=1, sum(v)>=2.

If |y_l|<=1, mu>=0 and 2 H^T y-lambda e-mu>=0 coordinatewise, then every
primal feasible v has objective at least lambda+2mu.  Thus feasible rational
primal and dual witnesses with equal objective certify the optimum over all
REAL weights in the stated finite family.  No solver theorem is a premise.

The sixth witness is intentionally incomplete as a certificate: its primal
is feasible but its dual fails at lag 9.  A successful verifier run must
detect that rejection.  It must never count it as a sixth optimum.
"""

import json
import math
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    """Checks remain active even if Python is invoked with -O."""
    if not condition:
        raise ValueError(message)


def integer(value):
    require(type(value) is int, "Expected an exact JSON integer")
    return value


def vector(values, size):
    require(type(values) is list and len(values) == size,
            "Unexpected coefficient-vector length")
    return [integer(value) for value in values]


def rational(pair):
    numerator, denominator = vector(pair, 2)
    require(denominator > 0 and math.gcd(numerator, denominator) == 1,
            "Rationals must be reduced, with a positive denominator")
    return Fraction(numerator, denominator)


def rational_vector(values, size):
    require(type(values) is list and len(values) == size,
            "Unexpected rational-vector length")
    return [rational(pair) for pair in values]


def convolution(left, right):
    """Ordinary polynomial multiplication, including stored zero endpoints."""
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def multiply_by_t(remainder, P, constant=0):
    """Return t*remainder+constant modulo the monic polynomial P."""
    top = remainder[-1]
    return [constant - top * P[0]] + [
        remainder[i - 1] - top * P[i] for i in range(1, len(remainder))
    ]


def multiplication_matrix(B, P):
    """Build every column B*t^j mod P by the defining quotient relation."""
    d = len(P) - 1
    remainder = [0] * d
    for coefficient in reversed(B):
        remainder = multiply_by_t(remainder, P, coefficient)
    columns = []
    for _ in range(d):
        columns.append(remainder)
        remainder = multiply_by_t(remainder, P)
    return [[column[i] for column in columns] for i in range(d)]


def determinant(matrix):
    """Fraction-free elimination with exact division and row pivoting.

    The update is the two-by-two determinant identity divided by the previous
    pivot.  For an integer matrix every such division is exact.  Checking this
    identity explicitly guards against an accidental truncating division.
    """
    a = [row[:] for row in matrix]
    n = len(a)
    sign, previous = 1, 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, previous)
                require(remainder == 0, "Nonexact determinant division")
                a[i][j] = quotient
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def expected_polynomial(name):
    if name == "P10":
        return [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
    # The other two inputs are P_n/(1+t), where
    # P_n=t^n(t^3-t-1)+1-t^2-t^3, with n=18 or n=30.
    n = {"P20": 18, "P32": 30}[name]
    numerator = [0] * (n + 4)
    for exponent, coefficient in ((0, 1), (2, -1), (3, -1),
                                  (n, -1), (n + 1, -1), (n + 3, 1)):
        numerator[exponent] += coefficient
    quotient = []
    previous = 0
    for coefficient in numerator[:-1]:
        previous = coefficient - previous
        quotient.append(previous)
    require(convolution([1, 1], quotient) == numerator,
            "Input polynomial factor identity failed")
    return quotient


def verify_input(item):
    name = item["name"]
    P = expected_polynomial(name)
    require(item["P"] == P, name + ": wrong input polynomial")
    d, N, q = len(P) - 1, integer(item["window"]), integer(item["q"])
    require(N == 2 * d and q > 0 and abs(P[0]) == P[-1] == 1,
            name + ": wrong degree, window or denominator")
    require(q == {"P10": 26487, "P20": 36887312, "P32": 257188436220}[name],
            name + ": unexpected original denominator")
    source_count = {"P10": 48, "P20": 98, "P32": 158}[name]
    require(len(item["columns"]) == source_count,
            name + ": incomplete finite source family")
    columns, enlarged = [], []
    for j, column in enumerate(item["columns"]):
        B = vector(column["B"], N)
        F = vector(column["F"], N)
        U = vector(column["U"], d)
        require([q * b - f for b, f in zip(B, F)] == convolution(P, U),
                f"{name} column {j}: F=qB-PU failed")
        # Orthogonality to all t^k P (0<=k<d) verifies that F/q is the
        # least-energy residual of B.  No saved projection matrix is used.
        require(all(sum(F[k + i] * P[i] for i in range(d + 1)) == 0
                    for k in range(d)),
                f"{name} column {j}: residual is not orthogonal")
        norm = determinant(multiplication_matrix(B, P))
        require(norm == integer(column["norm_B"]),
                f"{name} column {j}: signed full-degree norm mismatch")
        require(math.gcd(*F) == integer(column["content_F"]),
                f"{name} column {j}: original content mismatch")
        # The central coefficient of F(t)*t^(N-1)*F(t^-1) is ||F||^2;
        # its right half gives every positive-lag signed correlation.
        product = convolution(F, F[::-1])
        energy = Fraction(product[N - 1], q * q)
        correlations = [Fraction(value, q * q) for value in product[N:]]
        require(energy > 0, f"{name} column {j}: zero energy")
        admitted = abs(norm) == 1 and energy <= 1
        if j < N:
            require(B == [int(i == j) for i in range(N)],
                    f"{name}: missing original monomial {j}")
            require(admitted, f"{name}: monomial {j} excluded")
        if admitted:
            enlarged.append(j)
        columns.append({"F": F, "norm": norm, "e": energy,
                        "h": correlations, "product": product})
    require(enlarged == item["enlarged_indices"],
            name + ": finite norm-one/energy selector differs")
    require(len(enlarged) == {"P10": 39, "P20": 63, "P32": 105}[name],
            name + ": unexpected enlarged family size")
    # The actual uncompressed monomial family supplies a common feasible point:
    # v_j=1/d has energy 1 and sum(v)=2.  Check every mirror equivalence too.
    require(sum(c["e"] for c in columns[:N]) == d,
            name + ": uniform monomial energy failed")
    for j in range(d):
        left, right = columns[j], columns[N - 1 - j]
        require((left["e"], left["h"]) == (right["e"], right["h"]),
                name + ": monomial mirror equality failed")
    print(f"{name}: all {source_count} signed norms, residual identities and "
          f"correlations checked; {len(enlarged)-N} residues admitted")
    return {"d": d, "N": N, "q": q, "columns": columns,
            "enlarged": enlarged}


def verify_integer_realization(cert, columns, v, S, Hv, input_data):
    """Check the retained original-polynomial expenses of a complete witness."""
    q, d, N = input_data["q"], input_data["d"], input_data["N"]
    weights = [value / S for value in v]
    require(weights == rational_vector(cert["weights"], len(v)),
            "Normalized original weights differ")
    M = math.lcm(*(value.denominator for value in weights))
    require(M == integer(cert["weight_denominator"]),
            "Weight denominator is not the least common denominator")
    multiplicities = [int(M * weight) for weight in weights]
    require(multiplicities == vector(cert["multiplicities"], len(v))
            and sum(multiplicities) == M, "Integer multiplicities differ")
    aggregate = [sum(m * column["product"][k]
                     for m, column in zip(multiplicities, columns))
                 for k in range(2 * N - 1)]
    require(aggregate == vector(cert["aggregate"], 2 * N - 1),
            "Original aggregate coefficients differ")
    E = Fraction(q * q, 1) / S
    require(E == rational(cert["energy"]) and aggregate[N - 1] == M * E,
            "Original aggregate energy differs")
    require(all(aggregate[N + lag] == M * E * value
                for lag, value in enumerate(Hv)),
            "Aggregate lag identity failed")
    sign = math.prod(column["norm"] ** (m % 2)
                     for m, column in zip(multiplicities, columns))
    require(cert["arithmetic_product"] == {
        "sign": sign, "q_base": q, "q_exponent": d * M},
        "Full-degree resultant product differs")
    # F=qB modulo P proves Res(P,F)=q^d Res(P,B).  Consequently the
    # checked factored product is exact even if expanding q^(d*M) is impractical.
    # No primitive rescaling of any F has occurred at any point.


def verify_certificate(cert, input_data):
    name, family = cert["input"], cert["family"]
    require(family in ("baseline", "enlarged"), "Unknown finite family")
    indices = (list(range(input_data["N"])) if family == "baseline"
               else input_data["enlarged"])
    require(cert["column_indices"] == indices, "Certificate family differs")
    columns = [input_data["columns"][j] for j in indices]
    N = input_data["N"]
    v = rational_vector(cert["v"], len(columns))
    y = rational_vector(cert["y"], N - 1)
    lam, mu = rational(cert["lambda"]), rational(cert["mu"])
    S = sum(v)
    require(min(v) >= 0 and S == 2,
            f"{name}/{family}: nonnegative primal at S=2 required")
    require(sum(c["e"] * mass for c, mass in zip(columns, v)) == 1,
            f"{name}/{family}: primal energy is not one")
    Hv = [sum(c["h"][lag] * mass for c, mass in zip(columns, v))
          for lag in range(N - 1)]
    objective = 2 * sum(abs(value) for value in Hv)
    require(objective == rational(cert["kappa"]), "Primal objective differs")
    slacks = [2 * sum(a * b for a, b in zip(c["h"], y)) - lam*c["e"] - mu
              for c in columns]
    require(mu >= 0 and min(slacks) >= 0,
            f"{name}/{family}: dual multiplier or column slack is negative")
    require(objective == lam + 2 * mu, "Algebraic objective gap is nonzero")
    rejected = [lag for lag, value in enumerate(y, 1) if abs(value) > 1]
    if cert["status"] == "optimum":
        require(not rejected, f"{name}/{family}: dual box constraint failed")
        lower, upper = vector(cert["decimal_bin"], 2)
        require(upper == lower + 1 and
                Fraction(lower, 10000) <= objective < Fraction(upper, 10000),
                "Displayed rational interval is incorrect")
        verify_integer_realization(cert, columns, v, S, Hv, input_data)
        print(f"{name}/{family}: OPTIMUM in "
              f"[{lower//10000}.{lower%10000:04d}, "
              f"{upper//10000}.{upper%10000:04d}); all {len(columns)} "
              "primal/dual columns and integer expenses checked")
    else:
        require(cert["status"] == "invalid-dual" and
                (name, family) == ("P32", "enlarged"),
                "Unexpected certificate status")
        require(rejected == cert["rejected_box_lags"] == [9] and y[8] > 1,
                "The retained lag-9 dual rejection was not reproduced")
        require(not ({"weights", "multiplicities", "aggregate",
                      "arithmetic_product", "weight_denominator"} & cert.keys()),
                "Unreached sixth realization fields must remain absent")
        print(f"{name}/{family}: PRIMAL FEASIBLE; "
              "DUAL REJECTED at lag 9; zero algebraic gap proves no optimum")
    return objective


def main():
    path = Path(__file__).resolve().parent / "inputs/unit-cap-certificates.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    require(data["format"] == "exact-unit-comparison-v1", "Unknown data format")
    require([item["name"] for item in data["inputs"]] == ["P10", "P20", "P32"],
            "Unexpected input domain or order")
    inputs = {item["name"]: verify_input(item) for item in data["inputs"]}
    expected = [(name, family) for name in inputs
                for family in ("baseline", "enlarged")]
    require([(c["input"], c["family"]) for c in data["certificates"]] == expected,
            "The six finite comparisons are incomplete or reordered")
    require([c["status"] for c in data["certificates"]] ==
            ["optimum"] * 5 + ["invalid-dual"], "Unexpected conclusion domain")
    values = {}
    for cert in data["certificates"]:
        values[cert["input"], cert["family"]] = verify_certificate(
            cert, inputs[cert["input"]])
    for name in ("P10", "P20"):
        improvement = values[name, "baseline"] - values[name, "enlarged"]
        require(improvement > 0, name + ": no strict improvement")
        print(f"{name}: strict improvement = {improvement}")
    print("PASS: 304 source columns; 5 exact finite-family optima; "
          "2 strict improvements; sixth feasible primal with rejected dual.")
    print("Not checked here: irreducibility/root classification, historical "
          "floating tableaus, candidate discovery, all-unit or varying-input claims.")


if __name__ == "__main__":
    main()
