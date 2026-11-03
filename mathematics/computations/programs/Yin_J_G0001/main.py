"""Exact independent terminal check for McKee--Smyth 2605.19013v1, Theorem 1.

Python standard library only. All root counts and comparisons use rational
Sturm arithmetic. Decimal numbers are display-only. Coefficients are ascending.
This does not verify the analytic n <= 13 reduction or any length-six claim.
"""
from fractions import Fraction as F
from math import gcd
from decimal import Decimal, localcontext
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def zero(p):
    return len(p) == 1 and p[0] == 0


def sub(a, b):
    return trim([(a[i] if i < len(a) else 0) -
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def divrem(a, b):
    a, b = trim(a), trim(b)
    assert not zero(b)
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    while not zero(a) and len(a) >= len(b):
        k, c = len(a) - len(b), a[-1] / b[-1]
        q[k] += c
        a = sub(a, [F(0)] * k + [c * x for x in b])
    return trim(q), trim(a)


def deriv(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def monic(p):
    return trim([x / p[-1] for x in p]) if not zero(p) else p


def pgcd(a, b):
    while not zero(b):
        a, b = b, divrem(a, b)[1]
    return monic(a)


def value(p, x):
    y = F(0)
    for c in reversed(p):
        y = y * x + c
    return y


def sign(x):
    return (x > 0) - (x < 0)


def sturm(p):
    # Square-free part first; classical Sturm counts distinct real roots.
    g = pgcd(p, deriv(p))
    p, rem = divrem(p, g)
    assert zero(rem)
    seq = [p]
    if len(p) > 1:
        seq.append(deriv(p))
    while len(seq) > 1:
        r = divrem(seq[-2], seq[-1])[1]
        if zero(r):
            break
        seq.append([-x for x in r])
    return seq


def variations(seq, x):
    signs = []
    for p in seq:
        if x == "-inf":
            s = sign(p[-1]) * (-1 if (len(p) - 1) % 2 else 1)
        elif x == "+inf":
            s = sign(p[-1])
        else:
            s = sign(value(p, x))
        if s:
            signs.append(s)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def distinct_count(p, a, b):
    seq = sturm(p)
    return variations(seq, a) - variations(seq, b)


def multiplicity_count(p, a, b):
    # Repeated gcd layers count a root of multiplicity m exactly m times.
    total = 0
    while len(p) > 1:
        total += distinct_count(p, a, b)
        p = pgcd(p, deriv(p))
    return total


def isolate_above_two(p):
    assert distinct_count(p, F(2), F(3)) == 1
    lo, hi = F(2), F(3)
    for _ in range(80):
        mid = (lo + hi) / 2
        if value(p, mid) == 0:
            return mid, mid
        if distinct_count(p, lo, mid):
            hi = mid
        else:
            lo = mid
    return lo, hi


def int_coeffs(p):
    assert all(c.denominator == 1 for c in p)
    return [int(c) for c in p]


# C_j(x) = z^j + z^-j at x=z+z^-1, by C_0=2, C_1=x,
# C_(j+1)=x C_j-C_(j-1).
C = [[F(2)], [F(0), F(1)]]
for j in range(1, 13):
    C.append(sub([F(0)] + C[j], C[j-1]))

# Transcribed directly from Table 1, PDF p.3, in its printed order.
table_pairs = [(6,5),(7,3),(10,1),(7,2),(5,4),(9,1),(5,3),(8,1),
               (5,2),(7,1),(4,3),(6,1),(5,1),(3,2),(4,1),(3,1),(2,1)]
table_expected = set(table_pairs)
rows, accepted, h_by_pair = [], [], {}
for n in range(2, 14):
    for k in range(1, n):
        if gcd(n, k) != 1:
            continue
        h = sub(sub(C[n], C[n-k]), [F(1)])
        h_by_pair[(n,k)] = h
        counts = {
            "below_minus_two": multiplicity_count(h, "-inf", F(-2)),
            "inside_minus_two_two": multiplicity_count(h, F(-2), F(2)),
            "above_two": multiplicity_count(h, F(2), "+inf"),
            "above_three": multiplicity_count(h, F(3), "+inf"),
        }
        endpoints = {str(x): str(value(h, F(x))) for x in [-2,2,3]}
        assert all(value(h, F(x)) != 0 for x in [-2,2,3])
        real = sum(counts[t] for t in ["below_minus_two", "inside_minus_two_two", "above_two"])
        counts["nonreal"] = n - real
        # The bound 3 is complete: height-one monic q has |root|<2, so
        # its Salem trace is <5/2. A trace in (2,3) also excludes a
        # reciprocal quadratic Pisot factor, whose trace is integral.
        ok = (counts["below_minus_two"] == 0 and
              counts["inside_minus_two_two"] == n-1 and
              counts["above_two"] == 1 and counts["above_three"] == 0)
        if ok:
            accepted.append((n,k))
        rows.append({"n":n, "k":k, "H_coefficients_ascending":int_coeffs(h),
                     "derivative_gcd_degree":len(pgcd(h,deriv(h)))-1,
                     "endpoint_values":endpoints, "root_counts_with_multiplicity":counts,
                     "is_Salem_polynomial":ok, "in_source_Table1":(n,k) in table_expected})

assert set(accepted) == table_expected, (accepted, table_pairs)

# Identify equal Salem numbers without numerical comparisons: two accepted H's
# have the same >2 root iff their polynomial gcd has a root in (2,3).
groups = []
for pair in table_pairs:
    h = h_by_pair[pair]
    for group in groups:
        if distinct_count(pgcd(h, h_by_pair[tuple(group[0])]), F(2), F(3)) == 1:
            group.append(pair)
            break
    else:
        groups.append([pair])
assert len(groups) == 13

isolations = []
for group in groups:
    lo, hi = isolate_above_two(h_by_pair[group[0]])
    with localcontext() as ctx:
        ctx.prec = 45
        x = Decimal((lo+hi).numerator) / Decimal((lo+hi).denominator) / 2
        tau = (x + (x*x-4).sqrt())/2
    isolations.append({"pairs":group,"trace_lower":str(lo),"trace_upper":str(hi),
                       "Salem_decimal_display_only":str(tau)})
# Source table orders the distinct groups by their Salem numbers. Certify that
# order with disjoint rational trace intervals; tau=(x+sqrt(x^2-4))/2 increases.
assert all(F(a["trace_upper"]) < F(b["trace_lower"])
           for a,b in zip(isolations, isolations[1:]))
assert groups[0] == [(6,5),(7,3)]

# Exact identification of the minimum with the standard Lehmer polynomial.
p_lehmer = [1,1,0,-1,-1,-1,-1,-1,0,1,1]
q_lehmer = [0]*13
for i,c in [(0,1),(5,-1),(6,-1),(7,-1),(12,1)]:
    q_lehmer[i] = c
assert mul(p_lehmer,[1,-1,1]) == list(map(F,q_lehmer))

result = {
    "source":"McKee--Smyth, Short Salem polynomials, arXiv:2605.19013v1",
    "scope":"Terminal enumeration only, 2<=n<=13, 1<=k<n, gcd(n,k)=1",
    "arithmetic":"fractions.Fraction; exact Sturm with multiplicity via repeated gcd layers",
    "candidate_count":len(rows), "accepted_count":len(accepted),
    "distinct_Salem_number_count":len(groups), "Table1_exact_pair_set_match":True,
    "minimum_is_Lehmer_exactly":True,
    "analytic_large_n_reduction_verified_by_this_script":False,
    "all_rows":rows, "exact_groups_and_isolations":isolations,
}
out = (_J_OUTPUT / "result.json")
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k not in ["all_rows","exact_groups_and_isolations"]},indent=2))
print("Accepted (n,k):", accepted)
print("Output:", out)
