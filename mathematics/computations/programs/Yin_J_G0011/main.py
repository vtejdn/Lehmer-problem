"""Exact multi-prime periods and all-exponent first-floor cyclic-norm optimum.

Two previously retained integer inputs; eleven primes through31. FLINT only
proposes factors; elementary polynomial arithmetic certifies them and orders.
Rational atanh series produce rigorous fixed-point logarithm intervals.
No floating point participates in any optimum or tail comparison.
"""
from fractions import Fraction
from math import gcd, lcm, prod
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import sympy as sp
import flint

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
BITS = 128
SCALE = 1 << BITS


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def rem(a, f, p):
    a = trim([int(c) % p for c in a])
    inv = pow(f[-1], -1, p)
    while len(a) >= len(f) and a != [0]:
        c, k = a[-1] * inv % p, len(a) - len(f)
        for j, b in enumerate(f):
            a[k+j] = (a[k+j] - c*b) % p
        a = trim(a)
    return a


def mul(a, b, p):
    out = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j]+x*y) % p
    return trim(out)


def sub(a, b, p):
    return trim([((a[i] if i < len(a) else 0)-(b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def ppow(a, n, f, p):
    out, a = [1], rem(a, f, p)
    while n:
        if n & 1:
            out = rem(mul(out, a, p), f, p)
        a = rem(mul(a, a, p), f, p)
        n >>= 1
    return out


def pgcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    return [(c*pow(a[-1], -1, p)) % p for c in a]


def factors(n):
    out = {int(p): int(e) for p, e in sp.factorint(n).items()}
    assert prod(p**e for p, e in out.items()) == n
    assert all(sp.isprime(p) for p in out)
    return out


def factor_record(f, multiplicity, p):
    degree, x = len(f)-1, rem([0, 1], f, p)
    assert ppow(x, p**degree, f, p) == x
    rabin = {str(q): pgcd(sub(ppow(x, p**(degree//q), f, p), x, p), f, p)
             for q in factors(degree)}
    assert all(v == [1] for v in rabin.values())
    order = p**degree-1
    candidate_factors = factors(order)
    for q in candidate_factors:
        while order % q == 0 and ppow(x, order//q, f, p) == [1]:
            order //= q
    checks = {str(q): ppow(x, order//q, f, p) for q in factors(order)}
    assert ppow(x, order, f, p) == [1]
    assert all(v != [1] for v in checks.values())
    return {"coefficients": f, "degree": degree, "multiplicity": multiplicity,
            "rabin_gcds": rabin, "root_order": order,
            "order_factorization": factors(order), "order_prime_remainders": checks}


def prime_record(coeff, p):
    f = [c % p for c in coeff]
    _, ff = flint.nmod_poly(f, p).factor()
    records = [factor_record([int(g[i]) for i in range(g.degree()+1)], int(e), p)
               for g, e in ff]
    records.sort(key=lambda r: (r["degree"], r["coefficients"]))
    rebuilt = [1]
    for r in records:
        for _ in range(r["multiplicity"]):
            rebuilt = mul(rebuilt, r["coefficients"], p)
    assert rebuilt == f
    semisimple_order = lcm(*(r["root_order"] for r in records))
    block, nilpotent_order = max(r["multiplicity"] for r in records), 1
    while nilpotent_order < block:
        nilpotent_order *= p
    identity_order = semisimple_order * nilpotent_order
    order_checks = {str(q): ppow([0, 1], identity_order//q, f, p)
                    for q in factors(identity_order)}
    assert ppow([0, 1], identity_order, f, p) == [1]
    assert all(v != [1] for v in order_checks.values())
    scalar_order = identity_order
    for q in factors(identity_order):
        while scalar_order % q == 0:
            z = ppow([0, 1], scalar_order//q, f, p)
            if len(z) != 1 or z == [0]:
                break
            scalar_order //= q
    scalar = ppow([0, 1], scalar_order, f, p)
    scalar_checks = {str(q): ppow([0, 1], scalar_order//q, f, p)
                     for q in factors(scalar_order)}
    assert len(scalar) == 1 and scalar[0] != 0
    assert all(len(v) > 1 for v in scalar_checks.values())
    assert scalar[0]**2 % p == 1  # Both inputs are reciprocal.
    return {"prime": p, "factors": records, "squarefree": block == 1,
            "identity_order": identity_order, "scalar_order": scalar_order,
            "scalar": scalar[0], "identity_prime_remainders": order_checks,
            "scalar_prime_remainders": scalar_checks}


def atanh_log_ratio(a, b, terms=100):
    assert a >= b > 0
    z = Fraction(a-b, a+b)
    assert 0 <= z <= Fraction(1, 3)
    total = sum((2*z**(2*j+1)/ (2*j+1) for j in range(terms)), Fraction())
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return total, total+tail


def log_interval(n):
    assert n >= 1
    if n == 1:
        return 0, 0
    k = n.bit_length()-1
    a, b = atanh_log_ratio(2, 1)
    c, d = atanh_log_ratio(n, 1 << k)
    low, high = SCALE*(k*a+c), SCALE*(k*b+d)
    lo = low.numerator//low.denominator
    hi = -(-high.numerator//high.denominator)
    assert hi-lo <= 2
    return lo, hi


def weights(n, records, degree):
    out = {p: 0 for p in PRIMES}
    out[2] -= degree
    for r in records:
        if not r["squarefree"]:
            continue
        p, v, q = r["prime"], 0, n
        while q % p == 0:
            v += 1
            q //= p
        count = sum(f["degree"] for f in r["factors"] if n % f["root_order"] == 0)
        out[p] += count*(1+v)
    return out


def score_interval(w, logs):
    lo = hi = 0
    for p, c in w.items():
        a, b = logs[p]
        lo += c*(a if c >= 0 else b)
        hi += c*(b if c >= 0 else a)
    return lo, hi


def optimum(records, degree):
    logs = {p: log_interval(p) for p in PRIMES}
    good = [r for r in records if r["squarefree"]]
    rad = prod(r["prime"] for r in good)
    assert rad >= 6  # d log(R n/2)/n decreases for n>=1.
    nmax = 4096
    while True:
        low = [-degree*logs[2][1]]*(nmax+1)
        high = [-degree*logs[2][0]]*(nmax+1)
        for r in good:
            p = r["prime"]
            for f in r["factors"]:
                step, weight = f["root_order"], f["degree"]
                while step <= nmax:
                    a, b = weight*logs[p][0], weight*logs[p][1]
                    for n in range(step, nmax+1, step):
                        low[n] += a
                        high[n] += b
                    step *= p
        best = 1
        for n in range(2, nmax+1):
            if low[n]*best > low[best]*n:
                best = n
        assert low[best] > 0
        tail = degree*(log_interval(rad)[1]+log_interval(nmax+1)[1]-logs[2][0])
        if tail*best < low[best]*(nmax+1):
            break
        nmax *= 2
        assert nmax <= 1048576
    wbest = weights(best, records, degree)
    direct_low, direct_high = score_interval(wbest, logs)
    # Combining the negative archimedean log2 term with positive log2
    # weights tightens the interval compared with separate sieve terms.
    assert low[best] <= direct_low <= direct_high <= high[best]
    ties, compared = [], 0
    second_upper = None
    for n in range(1, nmax+1):
        if high[n]*best < low[best]*n:
            compared += 1
            if second_upper is None or high[n]*second_upper[1] > second_upper[0]*n:
                second_upper = (high[n], n)
        else:
            wn = weights(n, records, degree)
            assert all(wn[p]*best == wbest[p]*n for p in PRIMES), (n, best)
            ties.append(n)
    first = min(ties)
    wf = weights(first, records, degree)
    lower, upper = score_interval(wf, logs)
    frac = Fraction(lower, SCALE*first)
    decimal_floor = (frac.numerator*10**10)//frac.denominator
    return {"good_primes": [r["prime"] for r in good], "radical": rad,
            "enumerated_n_max": nmax, "maximizer_exponents": ties,
            "representative_n": first, "numerator_log_weights": wf,
            "scaled_log_intervals": logs, "scale_bits": BITS,
            "numerator_lower": lower, "numerator_upper": upper,
            "strict_nonmaximizer_comparisons": compared,
            "runner_up_upper_numerator": second_upper[0], "runner_up_n": second_upper[1],
            "tail_at": nmax+1, "tail_upper_numerator": tail,
            "certified_lower_decimal_truncated": f"{decimal_floor//10**10}.{decimal_floor%10**10:010d}"}


def build():
    x = sp.Symbol("x")
    p10 = sp.Poly(x**10+x**9-x**7-x**6-x**5-x**4-x**3+x+1, x)
    p22, rr = sp.div(sp.Poly(x**24-x**17-x**12-x**7+1, x), sp.Poly(x*x-x+1, x))
    assert rr.is_zero and p22.degree() == 22
    output = []
    for name, poly in [("lehmer", p10), ("degree22", p22)]:
        coeff = [int(poly.nth(i)) for i in range(poly.degree()+1)]
        records = [prime_record(coeff, p) for p in PRIMES]
        opt = optimum(records, poly.degree())
        output.append({"name": name, "degree": int(poly.degree()), "coefficients": coeff,
                       "prime_records": records, "aggregate_optimum": opt})
        print(name, [(r["prime"], r["scalar_order"], r["identity_order"]) for r in records], flush=True)
        print("all-n aggregate optimum", opt["maximizer_exponents"], opt["certified_lower_decimal_truncated"],
              "finite range", opt["enumerated_n_max"], flush=True)
    return {"primes": PRIMES, "arithmetic": "exact polynomial, integer and rational arithmetic; rigorous binary log intervals",
            "inputs": output}


if __name__ == "__main__":
    output = build()
    (_J_OUTPUT / "result.json").write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
