"""Independent exact reproduction of Yin J_G0094; no import of author code.

Declared scope: every prime prefix <=97, exponent8, B96, eta512/1024.
Alternative path: bisection roots of n^-3 and finite max-level chain sums.
All author certificate intermediates are checked separately as exact data.
"""

from __future__ import annotations

from fractions import Fraction as Q
import json
import os
from pathlib import Path
import subprocess
import sys
import time

PROGRAM = Path(__file__).resolve().parent
REPOSITORY = next(parent for parent in PROGRAM.parents if (parent / "repository/config.json").is_file())
GROUP = REPOSITORY / "mathematics/computations/outputs" / PROGRAM.name
S = 2**96
LIMIT = 180


def publish(filename, payload):
    GROUP.mkdir(parents=True, exist_ok=True)
    destination = GROUP / filename
    temporary = destination.with_name("." + destination.name + ".partial")
    try:
        temporary.write_text(json.dumps(payload, indent=1) + "\n", encoding="utf-8")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def fraction(record):
    value = Q(int(record["numerator"]), int(record["denominator"]))
    assert value.denominator > 0
    return value


def box(record):
    a, b = fraction(record["lower"]), fraction(record["upper"])
    assert a <= b
    return a, b


def encoded(value):
    if isinstance(value, tuple):
        return {"lower": encoded(value[0]), "upper": encoded(value[1])}
    value = Q(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def subtract(a, b):
    return a[0] - b[1], a[1] - b[0]


def multiply(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def divide(a, b):
    assert 0 < b[0] <= b[1]
    return multiply(a, (1 / b[1], 1 / b[0]))


def point(value):
    value = Q(value)
    return value, value


def independent_root(value):
    """Integer bisection, not math.isqrt; return exact dyadic enclosure."""
    value = Q(value)
    assert value > 0
    target = value.numerator * S * S
    denominator = value.denominator
    left, right = 0, S
    while right * right * denominator <= target:
        right *= 2
    while right - left > 1:
        middle = (left + right) // 2
        if middle * middle * denominator <= target:
            left = middle
        else:
            right = middle
    assert left * left * denominator <= target < right * right * denominator
    if left * left * denominator == target:
        return point(Q(left, S))
    return Q(left, S), Q(right, S)


def validate_saved_root(record, value):
    value = Q(value)
    assert fraction(record["argument"]) == value
    assert int(record["scale"]) == S
    j = int(record["floor_scaled_root"])
    assert j * j * value.denominator <= value.numerator * S * S
    assert (j + 1)**2 * value.denominator > value.numerator * S * S
    expected = Q(j, S), Q(j + 1, S)
    assert box(record["bounds"]) == expected
    return expected


def paired_eta(terms, m):
    total = point(0)
    for i in range(0, m, 2):
        total = add(total, subtract(terms[i], terms[i + 1]))
    return total[0], total[1] + terms[m][1]


def sieve_primes():
    composite = bytearray(98)
    for d in range(2, 98):
        if not composite[d]:
            for multiple in range(d * d, 98, d):
                composite[multiple] = 1
    return [d for d in range(2, 98) if not composite[d]]


def worker():
    started = time.monotonic()
    saved = json.loads((GROUP / "certificate.json").read_text(encoding="utf-8"))
    assert saved["status"] == "complete author computation"
    assert saved["parameters"] == {
        "s": "1/2", "t": "3/2", "exponent": 8, "prime_limit": 97,
        "precision_bits": 96, "scale": str(S), "eta_truncations": [512, 1024]}
    assert len(saved["signed_sum_terms"]) == 1025
    own_terms3, own_terms2, reproduced_terms = [], [], []
    for n, data in enumerate(saved["signed_sum_terms"], 1):
        assert data["n"] == n
        j = int(data["floor_scaled_sqrt_n"])
        assert j*j <= n*S*S < (j + 1)**2
        a3, b3 = map(int, data["term_three_halves_scaled"])
        a2, b2 = map(int, data["term_two_scaled"])
        assert a3 == S*S // (n*(j + 1))
        assert b3 == -(-S*S // (n*j))
        assert a2 == S // (n*n)
        assert b2 == -(-S // (n*n))
        assert Q(a3, S)**2 <= Q(1, n**3) <= Q(b3, S)**2
        assert Q(a2, S) <= Q(1, n*n) <= Q(b2, S)
        # Independent half-power path: enclose sqrt(1/n^3) directly.
        u = independent_root(Q(1, n**3))
        v = Q(a2, S), Q(b2, S)
        own_terms3.append(u)
        own_terms2.append(v)
        reproduced_terms.append({"n": n, "direct_half_power": encoded(u),
                                 "inverse_square": encoded(v)})
    saved_sqrt2 = validate_saved_root(saved["sqrt_two"], 2)
    saved_factor = subtract(point(1), divide(point(1), saved_sqrt2))
    assert box(saved["eta_three_halves_factor"]) == saved_factor
    own_factor = subtract(point(1), independent_root(Q(1, 2)))
    own_constants, author_constants, constant_records = {}, {}, []
    assert [x["truncation"] for x in saved["constant_enclosures"]] == [512, 1024]
    for record in saved["constant_enclosures"]:
        m = record["truncation"]
        author_etas = []
        for field, key in [("eta_three_halves", "term_three_halves_scaled"),
                           ("eta_two", "term_two_scaled")]:
            section = record[field]
            terms = [tuple(map(int, v[key])) for v in saved["signed_sum_terms"]]
            low = sum(terms[i][0] - terms[i + 1][1] for i in range(0, m, 2))
            high = sum(terms[i][1] - terms[i + 1][0] for i in range(0, m, 2))
            eta = Q(low, S), Q(high + terms[m][1], S)
            assert section["even_truncation"] == m
            assert list(map(int, section["partial_sum_scaled"])) == [low, high]
            assert tuple(map(int, section["first_omitted_scaled"])) == terms[m]
            assert box(section["eta_bounds"]) == eta
            author_etas.append(eta)
        az3 = divide(author_etas[0], saved_factor)
        az2 = multiply(point(2), author_etas[1])
        ak = divide(az3, az2)
        assert box(record["zeta_three_halves"]) == az3
        assert box(record["zeta_two"]) == az2
        assert box(record["K_half"]) == ak
        oe3, oe2 = paired_eta(own_terms3, m), paired_eta(own_terms2, m)
        ok = divide(oe3, multiply(own_factor, multiply(point(2), oe2)))
        assert max(ok[0], ak[0]) <= min(ok[1], ak[1])
        own_constants[m], author_constants[m] = ok, ak
        constant_records.append({"truncation": m, "eta_half": encoded(oe3),
                                 "eta_two": encoded(oe2), "K_half": encoded(ok)})

    primes = sieve_primes()
    assert len(primes) == 25 and primes[-1] == 97
    assert len(saved["candidate_rows"]) == len(primes)
    own_full, saved_full, prime_product = point(1), point(1), 1
    phi_integer, records, successes = 1, [], []
    for index, (p, row) in enumerate(zip(primes, saved["candidate_rows"]), 1):
        assert row["prime_prefix"] == primes[:index]
        assert row["max_prime"] == p and row["exponent"] == 8
        prime_product *= p
        N = prime_product**8
        phi_integer *= p**7 * (p - 1)
        W = N - phi_integer
        c = Q(phi_integer, N)
        assert int(row["N"]) == N and int(row["phi_N"]) == phi_integer
        assert int(row["remaining_mass"]) == W
        assert int(row["proper_divisor_label_count"]) == 9**index - 1
        assert fraction(row["phi_N_over_N"]) == c
        rp = validate_saved_root(row["sqrt_prime"], p)
        invp = divide(point(1), multiply(point(p), rp))
        kp = divide(point(1 - Q(1, p*p)), subtract(point(1), invp))
        local = add(multiply(point(1 - Q(1, p**12)), kp), point(Q(1, p**12)))
        assert box(row["local_infinite_factor"]) == kp
        assert box(row["local_finite_factor"]) == local
        saved_full = multiply(saved_full, local)
        assert box(row["full_divisor_ratio"]) == saved_full
        numerator = add(saved_full, point(c*c - 2*c))
        assert box(row["removed_normalized_numerator"]) == numerator
        ry = validate_saved_root(row["sqrt_remaining_fraction"], 1-c)
        denominator = multiply(point(1-c), ry)
        ratio = divide(numerator, denominator)
        assert box(row["removed_normalized_denominator"]) == denominator
        assert box(row["removed_ratio"]) == ratio
        energy_scale = N * prime_product**4
        assert box(row["full_energy"]) == multiply(saved_full, point(energy_scale))
        assert box(row["removed_energy"]) == multiply(numerator, point(energy_scale))

        # Independent local formula: sum all maximum-exponent increments.
        inverse_root = independent_root(Q(1, p))
        local_energy = point(1)
        for j in range(1, 9):
            increment = p**(2*j) - p**(2*j - 2)
            if j % 2:
                term = multiply(point(Q(increment, p**((j-1)//2))), inverse_root)
            else:
                term = point(Q(increment, p**(j//2)))
            local_energy = add(local_energy, term)
        own_local = divide(local_energy, point(p**12))
        own_full = multiply(own_full, own_local)
        own_numerator = add(own_full, point(c*c - 2*c))
        own_denominator = independent_root((1-c)**3)
        own_ratio = divide(own_numerator, own_denominator)
        assert max(ratio[0], own_ratio[0]) <= min(ratio[1], own_ratio[1])
        checks = {}
        for m in (512, 1024):
            lower_gap = ratio[0] - author_constants[m][1]
            comparison = row["comparisons"][str(m)]
            assert fraction(comparison["certified_lower_difference"]) == lower_gap
            assert comparison["strictly_above_product_constant"] == (lower_gap > 0)
            own_gap = own_ratio[0] - own_constants[m][1]
            assert (own_gap > 0) == (lower_gap > 0)
            checks[str(m)] = {"lower_gap": encoded(own_gap), "strict_separation": own_gap > 0}
        if checks["1024"]["strict_separation"]:
            successes.append(p)
        if p == 73:
            assert own_ratio[0] > Q(7943, 5000)
            assert own_constants[1024][1] < Q(7941, 5000)
            assert own_ratio[0] - own_constants[1024][1] > Q(1, 2500)
            assert ratio[0] > Q(7943, 5000)
            assert author_constants[1024][1] < Q(7941, 5000)
        records.append({"max_prime": p, "N": str(N), "phi_N": str(phi_integer),
                        "remaining_mass": str(W), "max_level_local_factor": encoded(own_local),
                        "full_ratio": encoded(own_full), "proper_ratio": encoded(own_ratio),
                        "comparisons": checks})
        if time.monotonic() - started >= LIMIT:
            raise TimeoutError("Independent worker exceeded declared ceiling")
    assert successes == [73, 79, 83, 89, 97]
    assert saved["summary"]["candidate_count"] == 25
    assert saved["summary"]["successful_prefix_ends_1024"] == successes
    assert saved["summary"]["first_certified_prefix_end"] == 73
    result = {"status": "complete independent verification", "parameters": saved["parameters"],
              "method": "independent bisection, direct n^-3 roots, paired eta, max-level local sums",
              "verified_saved_term_count": 1025, "verified_candidate_count": 25,
              "successful_prefix_ends_1024": successes, "first_certified_prefix_end": 73,
              "strict_simple_rational_bounds": True,
              "inverse_sqrt_two": encoded(independent_root(Q(1, 2))),
              "independent_terms": reproduced_terms, "constant_enclosures": constant_records,
              "candidate_rows": records,
              "limits": "finite declared evidence; arbitrary-e extension and density follow from separately reviewed proof"}
    publish("verification.json", result)
    print(json.dumps({k: result[k] for k in ["status", "verified_saved_term_count",
                     "verified_candidate_count", "successful_prefix_ends_1024",
                     "strict_simple_rational_bounds"]}))


def supervise():
    command = [sys.executable, str(Path(__file__).resolve()), "--worker"]
    try:
        result = subprocess.run(command, cwd=PROGRAM, capture_output=True, text=True,
                                timeout=LIMIT,
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
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        supervise()
    else:
        raise SystemExit("Usage: python verify.py [--worker]")
