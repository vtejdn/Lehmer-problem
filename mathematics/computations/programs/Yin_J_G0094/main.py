"""Yin J_G0094: author-only exact proper-divisor half-moment certificate.

Proof and prior declaration: mathematics/claims/Yin_C_G0105_v1.md.
No floating arithmetic supplies a mathematical bound. The supervisor's timer
is operational metadata only. Independent verification belongs to another file.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
from fractions import Fraction as F


PROGRAM = Path(__file__).resolve().parent
REPOSITORY = next(parent for parent in PROGRAM.parents if (parent / "repository/config.json").is_file())
ROOT = REPOSITORY / "mathematics/computations/outputs" / PROGRAM.name
BITS = 96
SCALE = 1 << BITS
TRUNCATIONS = (512, 1024)
PRIME_LIMIT = 97
EXPONENT = 8
RUN_LIMIT_SECONDS = 180


def publish(filename, payload):
    ROOT.mkdir(parents=True, exist_ok=True)
    destination = ROOT / filename
    temporary = destination.with_name("." + destination.name + ".partial")
    try:
        temporary.write_text(json.dumps(payload, indent=1) + "\n", encoding="utf-8")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def rat(x):
    x = F(x)
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def interval(x):
    lo, hi = x
    assert lo <= hi
    return {"lower": rat(lo), "upper": rat(hi)}


def mul(x, y):
    assert 0 <= x[0] <= x[1] and 0 <= y[0] <= y[1]
    return x[0] * y[0], x[1] * y[1]


def div(x, y):
    assert 0 <= x[0] <= x[1] and 0 < y[0] <= y[1]
    return x[0] / y[1], x[1] / y[0]


def sqrt_box(x):
    x = F(x)
    assert x > 0
    j = math.isqrt((x.numerator * SCALE * SCALE) // x.denominator)
    assert j * j * x.denominator <= x.numerator * SCALE * SCALE
    assert (j + 1) ** 2 * x.denominator > x.numerator * SCALE * SCALE
    box = (F(j, SCALE), F(j + 1, SCALE))
    assert box[0] > 0
    return box, {"argument": rat(x), "floor_scaled_root": str(j),
                 "scale": str(SCALE), "bounds": interval(box)}


def ceil_div(a, b):
    assert a >= 0 and b > 0
    return (a + b - 1) // b


def term_data(n):
    j = math.isqrt(n * SCALE * SCALE)
    assert j * j <= n * SCALE * SCALE < (j + 1) ** 2
    lo3 = (SCALE * SCALE) // (n * (j + 1))
    hi3 = ceil_div(SCALE * SCALE, n * j)
    lo2 = SCALE // (n * n)
    hi2 = ceil_div(SCALE, n * n)
    # Check the outward rational rounding independently of JSON serialization.
    assert F(lo3, SCALE) <= F(SCALE, n * (j + 1))
    assert F(hi3, SCALE) >= F(SCALE, n * j)
    assert F(lo2, SCALE) <= F(1, n * n) <= F(hi2, SCALE)
    return {"n": n, "floor_scaled_sqrt_n": str(j),
            "term_three_halves_scaled": [str(lo3), str(hi3)],
            "term_two_scaled": [str(lo2), str(hi2)]}


def eta_box(data, m, key):
    assert m > 0 and m % 2 == 0
    low = high = 0
    for row in data[:m]:
        lo, hi = map(int, row[key])
        if row["n"] % 2:
            low += lo
            high += hi
        else:
            low -= hi
            high -= lo
    omitted = tuple(map(int, data[m][key]))
    box = (F(low, SCALE), F(high + omitted[1], SCALE))
    assert box[0] > 0
    return box, {"even_truncation": m,
                 "partial_sum_scaled": [str(low), str(high)],
                 "first_omitted_scaled": list(map(str, omitted)),
                 "eta_bounds": interval(box)}


def worker():
    t0 = time.monotonic()

    def within_limit():
        if time.monotonic() - t0 >= RUN_LIMIT_SECONDS:
            raise TimeoutError("Declared author worker ceiling reached")

    terms = []
    for n in range(1, max(TRUNCATIONS) + 2):
        within_limit()
        terms.append(term_data(n))
    sqrt2, sqrt2_record = sqrt_box(F(2))
    eta_factor = (1 - 1 / sqrt2[0], 1 - 1 / sqrt2[1])
    assert 0 < eta_factor[0] <= eta_factor[1]
    constants = {}
    constant_records = []
    for m in TRUNCATIONS:
        e3, e3_record = eta_box(terms, m, "term_three_halves_scaled")
        e2, e2_record = eta_box(terms, m, "term_two_scaled")
        z3 = div(e3, eta_factor)
        z2 = (2 * e2[0], 2 * e2[1])
        k = div(z3, z2)
        constants[m] = k
        constant_records.append({"truncation": m, "eta_three_halves": e3_record,
                                 "eta_two": e2_record, "zeta_three_halves": interval(z3),
                                 "zeta_two": interval(z2), "K_half": interval(k)})

    primes = [n for n in range(2, PRIME_LIMIT + 1)
              if all(n % d for d in range(2, math.isqrt(n) + 1))]
    assert primes and primes[-1] == 97
    q = 1
    c = F(1)
    full_ratio = (F(1), F(1))
    rows = []
    for index, p in enumerate(primes, start=1):
        within_limit()
        sqrtp, root_record = sqrt_box(F(p))
        p_inverse_three_halves = (1 / (p * sqrtp[1]), 1 / (p * sqrtp[0]))
        local_denominator = (1 - p_inverse_three_halves[1],
                             1 - p_inverse_three_halves[0])
        kp = div((1 - F(1, p * p),) * 2, local_denominator)
        z = F(1, p ** 12)  # e=8 and t=3/2: p^(-te)=p^-12 exactly.
        local_finite = (kp[0] * (1 - z) + z, kp[1] * (1 - z) + z)
        full_ratio = mul(full_ratio, local_finite)
        q *= p
        c *= F(p - 1, p)
        n_integer = q ** EXPONENT
        phi = c * n_integer
        assert phi.denominator == 1
        phi_integer = phi.numerator
        mass = n_integer - phi_integer
        y = 1 - c
        sqrt_y, sqrt_y_record = sqrt_box(y)
        denominator = (y * sqrt_y[0], y * sqrt_y[1])
        numerator = (full_ratio[0] - 2 * c + c * c,
                     full_ratio[1] - 2 * c + c * c)
        assert numerator[0] > 0
        removed_ratio = div(numerator, denominator)
        n_sqrt = math.isqrt(n_integer)
        assert n_sqrt * n_sqrt == n_integer
        energy_scale = n_integer * n_sqrt
        comparisons = {}
        for m, k in constants.items():
            lower_difference = removed_ratio[0] - k[1]
            comparisons[str(m)] = {"strictly_above_product_constant": lower_difference > 0,
                                   "certified_lower_difference": rat(lower_difference)}
        rows.append({"prime_prefix": primes[:index], "max_prime": p,
                     "exponent": EXPONENT, "N": str(n_integer), "phi_N": str(phi_integer),
                     "remaining_mass": str(mass), "proper_divisor_label_count": str(9 ** index - 1),
                     "phi_N_over_N": rat(c), "sqrt_prime": root_record,
                     "local_infinite_factor": interval(kp), "local_finite_factor": interval(local_finite),
                     "full_divisor_ratio": interval(full_ratio),
                     "removed_normalized_numerator": interval(numerator),
                     "sqrt_remaining_fraction": sqrt_y_record,
                     "removed_normalized_denominator": interval(denominator),
                     "removed_ratio": interval(removed_ratio),
                     "full_energy": interval((full_ratio[0] * energy_scale, full_ratio[1] * energy_scale)),
                     "removed_energy": interval((numerator[0] * energy_scale, numerator[1] * energy_scale)),
                     "comparisons": comparisons})
    successes = [row["max_prime"] for row in rows
                 if row["comparisons"]["1024"]["strictly_above_product_constant"]]
    within_limit()
    certificate = {"author": "Yin", "status": "complete author computation",
                   "parameters": {"s": "1/2", "t": "3/2", "exponent": EXPONENT,
                                  "prime_limit": PRIME_LIMIT, "precision_bits": BITS,
                                  "scale": str(SCALE), "eta_truncations": list(TRUNCATIONS)},
                   "formula_scope": "all full divisors of N except N; exact formula, no divisor enumeration",
                   "sqrt_two": sqrt2_record, "eta_three_halves_factor": interval(eta_factor),
                   "signed_sum_terms": terms, "constant_enclosures": constant_records,
                   "candidate_rows": rows,
                   "summary": {"candidate_count": len(rows), "successful_prefix_ends_1024": successes,
                               "first_certified_prefix_end": successes[0] if successes else None,
                               "result": "product constant exceeded" if successes else "no separation certified",
                               "scope_limit": "does not refute a larger universal weak constant or assert a near-one family"}}
    publish("certificate.json", certificate)
    print(json.dumps(certificate["summary"]))


def supervisor():
    command = [sys.executable, str(Path(__file__).resolve()), "--worker"]
    try:
        result = subprocess.run(command, cwd=PROGRAM, capture_output=True, text=True,
                                timeout=RUN_LIMIT_SECONDS,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
    except subprocess.TimeoutExpired as error:
        for value, stream in ((error.stdout, sys.stdout), (error.stderr, sys.stderr)):
            if value:
                stream.write(value.decode(errors="replace") if isinstance(value, bytes) else value)
        raise SystemExit("Calculation timed out; no completed replacement is claimed.") from error
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    if result.returncode:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--worker":
        worker()
    elif len(sys.argv) == 1:
        supervisor()
    else:
        raise SystemExit("Usage: python main.py [--worker]")
