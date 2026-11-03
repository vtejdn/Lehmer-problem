"""Independent reconstruction of the two fixed J103 selected witnesses.

Preparation is not execution.  This verification-only program requires the
author's actual results.json and per-input certificates after the arithmetic
gate has been adopted and the coordinator has authorized execution.

Python integer convolutions generate every grid numerator.  Triangular Laurent
elimination reconstructs the trace polynomial, and multiplication matrices in
the two quotient fields give the selected exact norms without resultants.
SymPy supplies a separate squarefree decomposition.  The complete-root Jensen
calculation shares FLINT's certified root/ball engine with the author; midpoint
reproduction shares NumPy.  No author helper or generated coefficient is a
generator for the independent exact arithmetic.  This is a non-blind check,
not a second numerical library or a certification of the sampled grid minimum.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
from math import comb, gcd, isfinite, isqrt
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
INPUT = HERE.parent / "Yin_J_G0097/input.json"
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
EXPECTED = {
    "quartic_Salem_seed": [1, -1, -1, -1, 1],
    "Lehmer_degree10": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
}
COMPONENTS = ("E", "F_0")
SHEARS = (-2, -1, 0, 1, 2)
PRIMES = (2, 3, 5, 7)
COUNTS = (8192, 16384)
PRECISIONS = (256, 512)
L = 972000
TIMEOUT = 300
TOLERANCE = "1e-30"


class Unresolved(Exception):
    pass


def save(name, payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT / (name + ".writing")
    pending.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT / name)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        c[i] += value
    for i, value in enumerate(b):
        c[i] += value
    return trim(c)


def scale(a, scalar):
    return trim([scalar * value for value in a])


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def power(a, n):
    result = [1]
    for _ in range(n):
        result = multiply(result, a)
    return result


def remainder(a, modulus):
    assert modulus[-1] == 1
    a = trim(a)
    while len(a) >= len(modulus) and a != [0]:
        shift, top = len(a) - len(modulus), a[-1]
        for j, value in enumerate(modulus):
            a[shift + j] -= top * value
        a = trim(a)
    return a


def qmul(a, b, modulus):
    return remainder(multiply(a, b), modulus)


def qpower(a, exponent, modulus):
    result = [1]
    while exponent:
        if exponent & 1:
            result = qmul(result, a, modulus)
        exponent //= 2
        if exponent:
            a = qmul(a, a, modulus)
    return result


def qevaluate(coefficients, value, modulus):
    result = [0]
    for coefficient in reversed(coefficients):
        result = add(qmul(result, value, modulus), [coefficient])
    return remainder(result, modulus)


def integer_coefficients(a):
    values = [Fraction(c) for c in a]
    assert all(c.denominator == 1 for c in values)
    return trim([c.numerator for c in values])


def determinant_bareiss(matrix):
    """Exact integer determinant with row pivots and checked exact divisions."""
    a = [row[:] for row in matrix]
    n, previous, sign = len(a), 1, 1
    assert n and all(len(row) == n for row in a)
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
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def quotient_norm(value, modulus):
    n = len(modulus) - 1
    columns = []
    for j in range(n):
        column = integer_coefficients(remainder([0] * j + value, modulus))
        columns.append(column + [0] * (n - len(column)))
    matrix = [[columns[j][i] for j in range(n)] for i in range(n)]
    return determinant_bareiss(matrix), matrix


def trace_polynomial(pc):
    """Eliminate the highest powers of x from P(x)/x^r using (x+x^-1)^k."""
    r = (len(pc) - 1) // 2
    residual = {i - r: c for i, c in enumerate(pc) if c}
    tc = [0] * (r + 1)
    while residual:
        k = max(residual)
        assert k >= 0
        leading = residual[k]
        tc[k] = leading
        for j in range(k + 1):
            exponent = k - 2 * j
            residual[exponent] = residual.get(exponent, 0) - leading * comb(k, j)
            if not residual[exponent]:
                del residual[exponent]
    assert tc[-1] == 1
    return tc


def primitive_key(coefficients):
    divisor = 0
    for coefficient in coefficients:
        divisor = gcd(divisor, abs(coefficient))
    assert divisor
    if coefficients[-1] < 0:
        divisor = -divisor
    return tuple(c // divisor for c in coefficients)


def worker(name):
    import numpy as np
    import sympy as sp
    import flint
    from flint import acb, acb_poly, arb, ctx, fmpz_poly

    source = json.loads(INPUT.read_text(encoding="utf-8"))
    records = [item for item in source["inputs"] if item["name"] in EXPECTED]
    assert len(records) == 2
    inputs = {item["name"]: item["coefficients_ascending"] for item in records}
    assert inputs == EXPECTED and name in EXPECTED
    pc = inputs[name]
    d, r = len(pc) - 1, (len(pc) - 1) // 2
    assert d == 2 * r and pc == pc[::-1] and pc[0] == pc[-1] == 1
    tc = trace_polynomial(pc)
    symbol = sp.Symbol("x")
    psp = sp.Poly.from_list(pc[::-1], symbol, domain=sp.ZZ)
    tsp = sp.Poly.from_list(tc[::-1], symbol, domain=sp.ZZ)
    assert psp.is_irreducible and not psp.is_cyclotomic and tsp.is_irreducible
    assert tsp.count_roots(-sp.oo, sp.oo) == r
    if r % 2:
        exclusion = {"criterion": "odd trace-field degree excludes every quadratic subfield", "degree": r}
    else:
        assert r == 2
        discriminant = tc[1] ** 2 - 4 * tc[0] * tc[2]
        assert discriminant == 13
        for prime in PRIMES:
            ratio = Fraction(discriminant, prime)
            assert not (isqrt(ratio.numerator) ** 2 == ratio.numerator
                        and isqrt(ratio.denominator) ** 2 == ratio.denominator)
        exclusion = {"criterion": "quadratic trace field with discriminant13", "discriminant": discriminant}

    def substitute(k):
        values = [0] * (k * d + 1)
        for i, coefficient in enumerate(pc):
            values[k * i] = coefficient
        return values

    p2, p3, p5 = (substitute(k) for k in (2, 3, 5))
    h23 = add(scale(power(p2, 3), 9), scale(power(p3, 2), -8))
    h25 = add(scale(power(p2, 5), 75), scale(power(p5, 2), -64))
    h35 = add(scale(power(p3, 5), 250), scale(power(p5, 3), -243))
    assert [(len(h) - 1, h[0], h[-1]) for h in (h23, h25, h35)] == [
        (6 * d, 1, 1), (10 * d, 11, 11), (15 * d, 7, 7)]
    assert all(h == h[::-1] for h in (h23, h25, h35))
    aligned = {"E": [0] * (9 * d // 2) + scale(h23, 13500),
               "F_0": [0] * (5 * d // 2) + scale(h25, 1215)}
    zg = scale(h35, 32)
    keys = list(product(COMPONENTS, SHEARS, PRIMES))
    numerators, means = {}, {key: {} for key in keys}
    for key in keys:
        component, shear, prime = key
        numerator = add(power(add(aligned[component], scale(zg, shear)), 2),
                        scale(power(zg, 2), -prime))
        assert len(numerator) == 30 * d + 1 and numerator == numerator[::-1]
        assert numerator[0] == numerator[-1] == 50176 * (shear ** 2 - prime) != 0
        numerators[key] = numerator

    def horner(array):
        value = np.full(array.shape, float(tc[-1]), dtype=np.float64)
        for coefficient in reversed(tc[:-1]):
            value = value * array + coefficient
        return value

    for count in COUNTS:
        theta = (np.arange(count, dtype=np.float64) + 0.5) * np.pi / count
        av, bv, cv = [horner(2 * np.cos(k * theta)) / k for k in (2, 3, 5)]
        ev, fv, gv = bv ** 2 - av ** 3, 2 * cv ** 2 - 3 * av ** 5, cv ** 3 - 2 * bv ** 5
        for key in keys:
            component, shear, prime = key
            xv = ev if component == "E" else fv
            values = (xv + shear * gv) ** 2 - prime * gv ** 2
            valid = bool(np.all(np.isfinite(values)) and np.all(values != 0))
            means[key][str(count)] = float(np.mean(np.log(np.abs(values)))) if valid else None

    # Author output is consulted only after every independent candidate and grid mean.
    author = json.loads((OUTPUT / (name + ".json")).read_text(encoding="utf-8"))
    assert author["complete"] and author["name"] == name
    assert author["p_coefficients_ascending"] == pc and author["degree"] == d
    assert [Fraction(c) for c in author["trace_coefficients_ascending"]] == tc
    assert author["field_exclusion"] == exclusion and author["ranking_certified"] is False
    assert len(author["grid"]) == len(keys) == 40
    author_grid = {(row["component"], row["s"], row["p"]): row for row in author["grid"]}
    assert len(author_grid) == 40 and set(author_grid) == set(keys)
    for key in keys:
        declared = author_grid[key]["midpoint_means"]
        assert set(declared) == {str(n) for n in COUNTS}
        for count in COUNTS:
            own, reported = means[key][str(count)], declared[str(count)]
            assert (own is None) == (reported is None)
            if own is not None:
                assert isfinite(reported) and own == reported
    rankable = [key for key in keys if all(value is not None for value in means[key].values())]
    assert rankable, "No selected witness exists under the declared finite-sample rule."
    winner = min(rankable, key=lambda key: (means[key]["16384"], key))
    expected_selection = dict(zip(("component", "s", "p"), winner))
    assert author["selected"] == expected_selection
    component, shear, prime = winner
    numerator = numerators[winner]
    assert author["numerator_coefficients_ascending"] == numerator
    assert author["numerator_degree"] == 30 * d and author["center_shift"] == 15 * d
    assert author["scalar_denominator"] == L ** 2

    cheb = [[2], [0, 1]]
    for _ in range(2, 6):
        cheb.append(add(qmul([0, 1], cheb[-1], tc), scale(cheb[-2], -1)))
    av, bv, cv = [scale(qevaluate(tc, cheb[k], tc), Fraction(1, k)) for k in (2, 3, 5)]
    ev = add(qpower(bv, 2, tc), scale(qpower(av, 3, tc), -1))
    fv = add(scale(qpower(cv, 2, tc), 2), scale(qpower(av, 5, tc), -3))
    gv = add(qpower(cv, 3, tc), scale(qpower(bv, 5, tc), -2))
    xv = ev if component == "E" else fv
    value = integer_coefficients(add(qpower(add(xv, scale(gv, shear)), 2, tc),
                                     scale(qpower(gv, 2, tc), -prime)))
    assert value != [0]
    padded_value = value + [0] * (r - len(value))
    assert [Fraction(c) for c in author["trace_value_coefficients_ascending"]] == padded_value
    trace_norm, trace_matrix = quotient_norm(value, tc)
    assert trace_norm != 0 and int(author["trace_norm"]) == trace_norm

    inverse_x = [-c for c in pc[1:]]  # P(0)=1 gives x^-1=-p1-...-pd*x^(d-1).
    assert qmul([0, 1], inverse_x, pc) == [1]
    trace_x = add([0, 1], inverse_x)
    full_value = integer_coefficients(qevaluate(value, trace_x, pc))
    centered_numerator = qmul(remainder(numerator, pc), qpower(inverse_x, 15 * d, pc), pc)
    assert centered_numerator == scale(full_value, L ** 2)
    full_norm, full_matrix = quotient_norm(full_value, pc)
    assert full_norm == trace_norm ** 2 >= 1 and int(author["full_original_norm"]) == full_norm
    assert author["exact_original_value_identity_checked"] is True

    payload = {
        "complete": False, "name": name, "p_coefficients_ascending": pc, "degree": d,
        "trace_coefficients_ascending": tc, "field_exclusion": exclusion,
        "selected": expected_selection, "all_grid_numerators_reconstructed": True,
        "all_midpoint_means_exact_float_equal": True, "ranking_certified": False,
        "grid": [{"component": k[0], "s": k[1], "p": k[2], "midpoint_means": means[k],
                  "numerator_coefficients_ascending": numerators[k]} for k in keys],
        "numerator_coefficients_ascending": numerator, "numerator_degree": 30 * d,
        "signed_leading_coefficient": numerator[-1], "scalar_denominator": L ** 2,
        "center_shift": 15 * d, "trace_value_coefficients_ascending": padded_value,
        "original_value_coefficients_ascending": full_value,
        "trace_multiplication_matrix": trace_matrix, "original_multiplication_matrix": full_matrix,
        "trace_norm": str(trace_norm), "full_original_norm": str(full_norm),
        "exact_original_value_identity_checked": True,
        "construction": "Python integer polynomials; trace Laurent elimination; quotient multiplication matrices",
        "versions": {"numpy": np.__version__, "sympy": sp.__version__, "flint": flint.__version__},
        "shared_engines": ["NumPy exploratory midpoint arithmetic", "FLINT certified roots and balls"],
        "precision_schedule_bits": list(PRECISIONS), "root_radius_target": TOLERANCE,
        "timeout_seconds_per_input": TIMEOUT, "attempts": [],
    }
    save(name + "-verification.json", payload)
    print(name, "independent grid/numerator/two field norms agree", expected_selection, flush=True)

    # Separate exact squarefree construction; never factor the author's supplied coefficients.
    asp = sp.Poly.from_list(numerator[::-1], symbol, domain=sp.ZZ)
    content, factors = asp.sqf_list()
    content = int(content)
    restored = [content]
    exact_factors = []
    for factor, multiplicity in factors:
        coefficients = [int(factor.nth(i)) for i in range(factor.degree() + 1)]
        assert factor.gcd(factor.diff()).degree() == 0 and multiplicity >= 1
        restored = multiply(restored, power(coefficients, multiplicity))
        exact_factors.append((coefficients, int(multiplicity)))
    assert restored == numerator
    payload["factorization_content"] = content

    def ball_text(value):
        if not value.is_finite():
            raise Unresolved("Nonfinite native interval.")
        text = value.str(55, more=True)
        assert arb(text).contains(value)
        return text

    def quantity(value):
        if not value.is_finite() or not value.rad() < arb("1e-12"):
            raise Unresolved("Insufficient scalar enclosure.")
        decimal = format(float(value.mid()), ".15g")
        assert abs(value - arb(decimal)) < arb("1e-10")
        return {"ball": ball_text(value), "decimal": decimal, "absolute_error_bound": "1e-10"}

    for bits in PRECISIONS:
        ctx.prec = bits
        try:
            measure = arb(abs(numerator[-1])).log()
            root_count, factor_records, native_roots = 0, [], {}
            for coefficients, multiplicity in exact_factors:
                polynomial = acb_poly(fmpz_poly(coefficients))
                roots = polynomial.roots(tol=arb(TOLERANCE), maxprec=bits)
                if len(roots) != len(coefficients) - 1:
                    raise Unresolved("Incomplete native distinct-root count.")
                assert all(not roots[i].overlaps(roots[j]) for i in range(len(roots)) for j in range(i))
                root_records = []
                for root in roots:
                    if not (root.real.is_finite() and root.imag.is_finite()
                            and root.real.rad() <= arb(TOLERANCE) and root.imag.rad() <= arb(TOLERANCE)):
                        raise Unresolved("Native root ball misses the fixed radius target.")
                    assert polynomial(root).contains(0)
                    contribution = arb(1).max(abs(root)).log()
                    measure += multiplicity * contribution
                    root_records.append({"real": ball_text(root.real), "imag": ball_text(root.imag),
                                         "log_plus_modulus": quantity(contribution)})
                root_count += multiplicity * len(roots)
                key = primitive_key(coefficients)
                assert key not in native_roots
                native_roots[key] = (multiplicity, roots)
                factor_records.append({"factor_coefficients_ascending": coefficients,
                                       "multiplicity": multiplicity, "roots": root_records})
            assert root_count == 30 * d
            haar = measure - 2 * arb(L).log()
            original = arb(full_norm).log() / d
            assert original.overlaps(arb(abs(trace_norm)).log() / r)
            quantities = {"haar": haar, "original": original, "mahler_numerator": measure,
                          "haar_minus_margin_target": haar + arb(1) / 16,
                          "original_minus_haar": original - haar}
            own_quantities = {key: quantity(value) for key, value in quantities.items()}
            comparisons = {}
            assert set(author["quantities"]) == set(quantities)
            for key, own in quantities.items():
                reported = author["quantities"][key]
                reported_ball = arb(reported["ball"])
                assert reported["absolute_error_bound"] == "1e-10"
                assert reported_ball.is_finite() and reported_ball.rad() < arb("1e-12")
                assert own.overlaps(reported_ball)
                assert abs(reported_ball - arb(reported["decimal"])) < arb("1e-10")
                comparisons[key] = {"independent_ball": ball_text(own), "author_ball": reported["ball"]}

            author_restored = [int(author["factorization_content"])]
            seen, author_count = set(), 0
            for factor in author["factors"]:
                coefficients = factor["factor_coefficients_ascending"]
                multiplicity = factor["multiplicity"]
                assert isinstance(multiplicity, int) and multiplicity >= 1
                author_restored = multiply(author_restored, power(coefficients, multiplicity))
                key = primitive_key(coefficients)
                assert key in native_roots and key not in seen
                seen.add(key)
                own_multiplicity, own_roots = native_roots[key]
                assert multiplicity == own_multiplicity
                assert len(factor["roots"]) == len(coefficients) - 1 == len(own_roots)
                matching = set()
                for item in factor["roots"]:
                    ball = acb(arb(item["real"]), arb(item["imag"]))
                    assert ball.real.is_finite() and ball.imag.is_finite()
                    assert ball.real.rad() <= arb(TOLERANCE) and ball.imag.rad() <= arb(TOLERANCE)
                    overlaps = [i for i, root in enumerate(own_roots) if ball.overlaps(root)]
                    assert len(overlaps) == 1 and overlaps[0] not in matching
                    matching.add(overlaps[0])
                    reported_term = item["log_plus_modulus"]
                    term = arb(reported_term["ball"])
                    assert term.is_finite() and term.rad() < arb("1e-12")
                    assert reported_term["absolute_error_bound"] == "1e-10"
                    assert abs(term - arb(reported_term["decimal"])) < arb("1e-10")
                    assert term.overlaps(arb(1).max(abs(own_roots[overlaps[0]])).log())
                assert len(matching) == len(own_roots)
                author_count += multiplicity * len(own_roots)
            assert seen == set(native_roots) and author_restored == numerator
            assert author_count == author["root_count_with_multiplicity"] == root_count
            assert author["precision_bits"] in PRECISIONS
            assert [attempt["precision_bits"] for attempt in author["attempts"]] == (
                [] if author["precision_bits"] == 256 else [256])
            assert author["negative_haar"] == bool(haar < 0)
            assert author["margin_reached"] == bool(haar < -arb(1) / 16)
            payload.update({"complete": True, "precision_bits": bits,
                            "root_count_with_multiplicity": root_count, "factors": factor_records,
                            "quantities": own_quantities, "author_comparisons": comparisons,
                            "negative_haar": bool(haar < 0), "margin_reached": bool(haar < -arb(1) / 16),
                            "author_payload_checked": True})
            save(name + "-verification.json", payload)
            print(name, "independent complete Jensen agrees", own_quantities["haar"]["decimal"], flush=True)
            return
        except (Unresolved, ValueError) as error:
            payload["attempts"].append({"precision_bits": bits, "error": str(error)})
            save(name + "-verification.json", payload)
    raise Unresolved("The fixed two-precision certification allowance is exhausted.")


def main():
    author = json.loads((OUTPUT / "results.json").read_text(encoding="utf-8"))
    assert author["complete"] and len(author["inputs"]) == len(EXPECTED)
    assert [row["name"] for row in author["inputs"]] == list(EXPECTED)
    assert [row["name"] for row in author["statuses"]] == list(EXPECTED)
    assert all(row["exit_code"] == 0 and not row["timed_out"] for row in author["statuses"])
    for row in author["inputs"]:
        assert row == json.loads((OUTPUT / (row["name"] + ".json")).read_text(encoding="utf-8"))
    statuses = []
    for name in EXPECTED:
        save(name + "-verification.json", {"name": name, "complete": False})
        try:
            process = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker", name],
                                     timeout=TIMEOUT)
            statuses.append({"name": name, "exit_code": process.returncode, "timed_out": False})
        except subprocess.TimeoutExpired:
            statuses.append({"name": name, "exit_code": 124, "timed_out": True})
    records = [json.loads((OUTPUT / (name + "-verification.json")).read_text(encoding="utf-8"))
               for name in EXPECTED]
    complete = all(row["exit_code"] == 0 for row in statuses) and all(row["complete"] for row in records)
    save("verification.json", {"complete": complete, "statuses": statuses, "inputs": records,
                                "precision_schedule_bits": list(PRECISIONS),
                                "timeout_seconds_per_input": TIMEOUT,
                                "shared_root_engine": "python-flint / FLINT; not a second numerical library",
                                "ranking_certified": False})
    raise SystemExit(0 if complete else 1)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--worker" and sys.argv[2] in EXPECTED:
        worker(sys.argv[2])
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("Only the two declared independent signed-form witness checks are supported.")
