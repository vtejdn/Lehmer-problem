"""Separate exact checker for the fixed four-input C155 diagnostic.

The prescribed values are rebuilt in Q[t]/(P) from P(alpha**p)/p,
with their phases removed before forming e, f, g and h.
All polynomial arithmetic, root counts and elimination below use Fraction.
SymPy is used only for the separate finite irreducibility check over Q.
No author program or author-generated value is an arithmetic input.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import subprocess
import sys
import time

EXPECTED = (
    (1, -3, 1),
    (1, -1, -1, -1, 1),
    (1, 0, -4, 0, 1),
    (1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1),
)
EXPECTED_NAMES = ("quadratic_A3", "quartic_Salem_seed", "quartic_radical_A4", "Lehmer_degree10")
START = time.monotonic()
LIMIT = 175


def budget():
    if time.monotonic() - START > LIMIT:
        raise TimeoutError("Verification computation exceeded its 175-second internal limit")


def trim(a):
    a = [Q(x) for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [Q(0)]


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, s):
    return trim([Q(s) * x for x in a])


def mul(a, b):
    budget()
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def divrem(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    out = [Q(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        budget()
        k, c = len(a) - len(b), a[-1] / b[-1]
        out[k] = c
        a = add(a, [Q(0)] * k + scale(b, -c))
    return trim(out), a


def rem(a, p):
    return divrem(a, p)[1]


def mpow(a, n, p):
    assert n >= 0
    ans = [Q(1)]
    while n:
        if n & 1:
            ans = rem(mul(ans, a), p)
        a = rem(mul(a, a), p)
        n //= 2
    return ans


def evaluate_at(a, b, p):
    out = [Q(0)]
    for c in reversed(a):
        out = add(rem(mul(out, b), p), [c])
    return rem(out, p)


def pad(a, n):
    assert len(a) <= n
    return list(a) + [Q(0)] * (n - len(a))


def dot(a, b):
    assert len(a) == len(b)
    return sum((x * y for x, y in zip(a, b)), Q(0))


def mv(a, x):
    return [dot(row, x) for row in a]


def transpose(a):
    return [list(x) for x in zip(*a)]


def gram(rows):
    return [[dot(a, b) for b in rows] for a in rows]


def solve(a, b):
    n = len(a)
    m = [[Q(x) for x in row] + [Q(v)] for row, v in zip(a, b)]
    assert n == len(b) and all(len(row) == n + 1 for row in m)
    for k in range(n):
        budget()
        pivot = next(i for i in range(k, n) if m[i][k])
        m[k], m[pivot] = m[pivot], m[k]
        m[k] = [x / m[k][k] for x in m[k]]
        for i in range(n):
            if i != k and m[i][k]:
                v = m[i][k]
                m[i] = [x - v * y for x, y in zip(m[i], m[k])]
    return [row[-1] for row in m]


def det(a):
    m = [[Q(x) for x in row] for row in a]
    out = Q(1)
    for k in range(len(m)):
        pivot = next((i for i in range(k, len(m)) if m[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            out = -out
        v = m[k][k]
        out *= v
        for i in range(k + 1, len(m)):
            factor = m[i][k] / v
            m[i] = [x - factor * y for x, y in zip(m[i], m[k])]
    return out


def norm(a, p):
    n = len(p) - 1
    return det(transpose([pad(rem([Q(0)] * j + a, p), n) for j in range(n)]))


def sturm(p):
    seq = [trim(p), trim([i * p[i] for i in range(1, len(p))])]
    while seq[-1] != [0]:
        rr = scale(rem(seq[-2], seq[-1]), -1)
        if rr == [0]:
            break
        seq.append(rr)
    return seq


def value(p, x):
    a = Q(0)
    for c in reversed(p):
        a = a * x + c
    return a


def variations(seq, x):
    signs = []
    for p in seq:
        if x == "-inf":
            v = p[-1] * (-1 if (len(p) - 1) % 2 else 1)
        elif x == "+inf":
            v = p[-1]
        else:
            v = value(p, x)
        if v:
            signs.append(1 if v > 0 else -1)
    return sum(a != b for a, b in zip(signs, signs[1:]))


def count(seq, lo, hi):
    return variations(seq, lo) - variations(seq, hi)


def interval_value(p, lo, hi):
    lower = upper = Q(0)
    for c in reversed(p):
        products = (lower * lo, lower * hi, upper * lo, upper * hi)
        lower, upper = min(products) + c, max(products) + c
    return lower, upper


def trace_poly(p):
    r = (len(p) - 1) // 2
    cheb = [[Q(2)], [Q(0), Q(1)]]
    for j in range(2, r + 1):
        cheb.append(add([Q(0)] + cheb[-1], scale(cheb[-2], -1)))
    out = [p[r]]
    for j in range(1, r + 1):
        out = add(out, scale(cheb[j], p[r + j]))
    return trim(out)


def reconstruct(p):
    p = trim(p)
    d, r = len(p) - 1, (len(p) - 1) // 2
    assert d % 2 == 0 and p[0] == p[-1] == 1 and p == list(reversed(p))
    import sympy as sp
    t = sp.Symbol("t")
    assert sp.Poly(sum(int(c) * t**j for j, c in enumerate(p)), t).is_irreducible
    tp = trace_poly(p)
    seq = sturm(tp)
    assert count(seq, "-inf", "+inf") == r
    assert value(tp, Q(-2)) != 0 and value(tp, Q(2)) != 0
    assert count(seq, Q(-2), Q(2)) < r  # Some original root lies off the circle.
    alpha = [Q(0), Q(1)]
    inverse = scale(p[1:], -1)
    assert rem(mul(alpha, inverse), p) == [1]
    z = add(alpha, inverse)
    assert evaluate_at(tp, z, p) == [0]
    zcolumns = [pad(mpow(z, j, p), d) for j in range(r)]
    zgram = gram(zcolumns)

    def to_trace(q):
        coordinates = solve(zgram, [dot(col, pad(q, d)) for col in zcolumns])
        assert mv(transpose(zcolumns), coordinates) == pad(q, d)
        assert all(c.denominator == 1 for c in coordinates)
        return coordinates

    theta_original = {}
    for prime in (2, 3, 5):
        quotient = scale(evaluate_at(p, mpow(alpha, prime, p), p), Q(1, prime))
        theta = rem(mul(quotient, mpow(inverse, prime * r, p)), p)
        assert theta != [0] and all(c.denominator == 1 for c in theta)
        theta_original[str(prime)] = theta
    a, b, c = (theta_original[str(q)] for q in (2, 3, 5))
    e = add(mpow(b, 2, p), scale(mpow(a, 3, p), -1))
    f = add(scale(mpow(c, 2, p), 2), scale(mpow(a, 5, p), -3))
    g = add(mpow(c, 3, p), scale(mpow(b, 5, p), -2))
    h = rem(add(add(mpow(e, 2, p), mpow(f, 2, p)), mpow(g, 2, p)), p)
    rh = pad(h, d)
    assert all(x.denominator == 1 for x in rh)
    columns = [pad(mpow(alpha, k, p), d) for k in range(2 * d)]
    arows = transpose(columns)
    assert [row[:d] for row in arows] == [[Q(i == j) for j in range(d)] for i in range(d)]
    grow = gram(arows)
    y = solve(grow, rh)
    xstar = mv(columns, y)
    assert mv(grow, y) == rh and mv(arows, xstar) == rh
    energy = dot(xstar, xstar)
    assert energy == dot(rh, y)
    htrace = to_trace(h)
    ntrace, noriginal = norm(htrace, tp), norm(h, p)
    assert ntrace > 0 and noriginal == ntrace**2 and noriginal >= 2**d
    return dict(
        degree=d, trace_coefficients_ascending=tp,
        theta_coefficients={k: to_trace(v) for k, v in theta_original.items()},
        defect_trace_coefficients={k: to_trace(v) for k, v in zip(("e", "f", "g"), (e, f, g))},
        h_trace_coefficients=htrace, r_h=rh, A_rows=arows, gram_rows=grow,
        y=y, x_star=xstar, energy=energy, energy_minus_four=energy-4,
        energy_sign="below" if energy < 4 else "above" if energy > 4 else "equal",
        trace_norm=ntrace, original_norm=noriginal,
    )


def compare(actual, expected, path):
    if isinstance(expected, dict):
        assert isinstance(actual, dict), path
        for key, val in expected.items():
            compare(actual[key], val, path + "." + key)
    elif isinstance(expected, list):
        assert isinstance(actual, list) and len(actual) == len(expected), path
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, path + f"[{i}]")
    elif isinstance(expected, str):
        assert actual == expected, (path, actual, expected)
    else:
        assert Q(actual) == expected, (path, actual, str(expected))


def check_intervals(record, expected):
    tp = expected["trace_coefficients_ascending"]
    seq = sturm(tp)
    all_intervals = []
    for lo, hi, multiplicity in record["trace_isolating_intervals"]:
        lo, hi = Q(lo), Q(hi)
        assert multiplicity == 1 and lo <= hi
        if lo == hi:
            assert value(tp, lo) == 0
        else:
            assert value(tp, lo) and value(tp, hi) and count(seq, lo, hi) == 1
            assert hi - lo <= Q(1, 2**80)
        all_intervals.append((lo, hi))
    assert len(all_intervals) == expected["degree"] // 2
    assert all(a[1] < b[0] for a, b in zip(all_intervals, all_intervals[1:]))
    contacts = []
    contact_intervals = []
    for contact in record["circle_contacts"]:
        lo, hi = map(Q, contact["trace_interval"])
        assert (lo, hi) in all_intervals and -2 < lo <= hi < 2
        lower, upper = interval_value(expected["h_trace_coefficients"], lo, hi)
        compare(contact["h_interval"], [lower, upper], "circle_contact.h_interval")
        assert contact["strict_gt_two"] == (lower > 2)
        contacts.append({"trace_interval": [str(lo), str(hi)],
                         "h_interval": [str(lower), str(upper)],
                         "strict_gt_two": lower > 2})
        contact_intervals.append((lo, hi))
    assert contact_intervals == [(lo, hi) for lo, hi in all_intervals if -2 < lo <= hi < 2]
    return contacts


def run(args):
    specification = json.loads((Path(__file__).resolve().parent / "input.json").read_text(encoding="utf-8"))
    assert specification["window_multiple"] == 2 and specification["threshold"] == 4
    assert len(specification["inputs"]) == len(EXPECTED)
    for i, (item, coefficients, name) in enumerate(zip(specification["inputs"], EXPECTED, EXPECTED_NAMES)):
        compare(item["coefficients_ascending"], list(coefficients), f"specification[{i}].P")
        assert item["name"] == name
    source = json.loads(args.results.read_text(encoding="utf-8"))
    assert source["complete"] is True and len(source["inputs"]) == len(EXPECTED)
    assert source["window_multiple"] == 2 and source["threshold"] == 4
    verified = []
    for i, (record, coefficients) in enumerate(zip(source["inputs"], EXPECTED)):
        assert record["name"] == EXPECTED_NAMES[i]
        compare(record["p_coefficients_ascending"], list(coefficients), f"input[{i}].P")
        rebuilt = reconstruct(coefficients)
        compare(record, rebuilt, f"input[{i}]")
        contacts = check_intervals(record, rebuilt)
        verified.append({"name": record["name"], "degree": rebuilt["degree"],
                         "energy": str(rebuilt["energy"]),
                         "energy_sign": rebuilt["energy_sign"],
                         "circle_contacts": contacts,
                         "exact_payload_and_optimality_verified": True})
        print(record["name"], "verified", rebuilt["energy_sign"], flush=True)
    output = {
        "complete": True,
        "scope": "Exactly the four fixed inputs; ordinary columns 0 through 2d-1; prescribed C155 h",
        "implementation": "Fraction quotient arithmetic, original-field Frobenius values and phase removal, rational elimination, rational Sturm counts and interval Horner; SymPy Q irreducibility only",
        "shared_library_limit": "Author and checker use the same installed SymPy only for irreducibility; all value, energy, root-count, norm and interval arithmetic is independently implemented here",
        "inputs": verified,
    }
    budget()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    staging = args.output.with_suffix(".pending.json")
    staging.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    staging.replace(args.output)
    print("All four independent exact checks passed.", flush=True)


def main():
    group = Path(__file__).resolve().parent
    output_home = group.parents[2] / "computations" / "outputs" / group.name
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=output_home / "results.json")
    parser.add_argument("--output", type=Path, default=output_home / "verification.json")
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker:
        run(args)
    else:
        command = [sys.executable, str(Path(__file__).resolve()), "--worker",
                   "--results", str(args.results), "--output", str(args.output)]
        subprocess.run(command, check=True, timeout=180)


if __name__ == "__main__":
    main()
