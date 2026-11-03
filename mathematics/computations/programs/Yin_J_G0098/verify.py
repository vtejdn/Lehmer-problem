"""Independent exact-numerator/Jensen check of the four fixed C155 B3 inputs.

No author program or generated value is an arithmetic input.  The original
integer H numerators are constructed directly, their complete roots are
isolated with multiplicity after exact squarefree factorization, and Jensen's
identity retains the leading scalar and the full supplied denominator.
"""
from __future__ import annotations

import json
from math import isqrt
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
EXPECTED = (
    ("quadratic_A3", [1, -3, 1]),
    ("quartic_Salem_seed", [1, -1, -1, -1, 1]),
    ("quartic_radical_A4", [1, 0, -4, 0, 1]),
    ("Lehmer_degree10", [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]),
)
TIMEOUT_SECONDS = 300
PRECISION_BITS = 256
DENOMINATOR = 972000


def save(name, value):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT / (name + ".writing")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT / name)


def worker():
    import flint
    from flint import acb_poly, arb, ctx, fmpq, fmpq_poly, fmpz_poly

    ctx.prec = PRECISION_BITS
    specification = json.loads((HERE.parent / "Yin_J_G0097/input.json").read_text(encoding="utf-8"))
    assert specification["window_multiple"] == 2 and specification["threshold"] == 4
    assert [(v["name"], v["coefficients_ascending"]) for v in specification["inputs"]] == list(EXPECTED)
    completed = []

    def coefficients(p):
        return [int(v) for v in p]

    def display(x):
        # str with radius is outward enclosing; parse again to certify the
        # actual persisted decimal enclosure, not just the in-memory ball.
        value = x.str(50, more=True)
        assert arb(value).contains(x)
        assert arb(value).rad() < arb("1e-10")
        return value

    def sign(x):
        return "positive" if x > 0 else "negative" if x < 0 else "undetermined"

    try:
        for name, coefficients_p in EXPECTED:
            d = len(coefficients_p) - 1
            P = fmpz_poly(coefficients_p)
            assert d % 2 == 0 and coefficients_p == coefficients_p[::-1]
            assert P[0] == P[d] == 1
            t = fmpz_poly([0, 1])

            def compose_power(n):
                out = [0] * (n * d + 1)
                for k, value in enumerate(coefficients_p):
                    out[n * k] = value
                return fmpz_poly(out)

            P2, P3, P5 = (compose_power(n) for n in (2, 3, 5))
            H23 = 9 * P2**3 - 8 * P3**2
            H25 = 75 * P2**5 - 64 * P5**2
            H35 = 250 * P3**5 - 243 * P5**3
            A = 13500**2 * t**(9*d) * H23**2 + 1215**2 * t**(5*d) * H25**2 + 32**2 * H35**2
            assert A.degree() == 30*d
            assert A[0] == A[A.degree()] == 50176
            assert coefficients(A) == coefficients(A)[::-1]
            # The centering monomial has norm 1 because P is monic with
            # constant coefficient 1 and even degree.  No smaller own field
            # or subset of the original roots is used in this resultant.
            scaled_norm = int(P.resultant(A))
            scale = DENOMINATOR**(2*d)
            original_norm, remainder = divmod(scaled_norm, scale)
            assert remainder == 0 and original_norm >= 2**d
            trace_norm = isqrt(original_norm)
            assert trace_norm * trace_norm == original_norm
            original_mean = arb(original_norm).log() / d
            content, factors = A.factor_squarefree()
            product = fmpz_poly([content])
            total_degree = 0
            jensen = arb(abs(int(A[A.degree()]))).log()
            factor_records = []
            for factor, multiplicity in factors:
                product *= factor**multiplicity
                assert factor.gcd(factor.derivative()).degree() == 0
                # roots() either returns the complete isolated set for this
                # squarefree factor or raises; no approximate-root fallback.
                roots = acb_poly(factor).roots(tol=arb("1e-40"), maxprec=2048)
                assert len(roots) == factor.degree()
                assert all(not roots[i].overlaps(roots[j])
                           for i in range(len(roots)) for j in range(i))
                total_degree += multiplicity * len(roots)
                records = []
                for root in roots:
                    modulus = abs(root)
                    contribution = arb(1).max(modulus).log()
                    assert contribution.is_finite()
                    jensen += multiplicity * contribution
                    records.append({"real": root.real.str(50, more=True),
                                    "imag": root.imag.str(50, more=True),
                                    "log_plus_modulus": display(contribution),
                                    "circle_side": "outside" if modulus > 1 else "inside" if modulus < 1 else "overlaps"})
                factor_records.append({"coefficients_ascending": coefficients(factor),
                                       "multiplicity": multiplicity, "roots": records})
            assert product == A and total_degree == A.degree()
            haar_mean = jensen - 2 * arb(DENOMINATOR).log()
            log_two = arb(2).log()
            differences = {"haar_minus_log_two": haar_mean-log_two,
                           "original_minus_log_two": original_mean-log_two,
                           "original_minus_haar": original_mean-haar_mean}
            record = {"name": name, "p_coefficients_ascending": coefficients_p,
                      "degree": d, "numerator_coefficients_ascending": coefficients(A),
                      "numerator_degree": A.degree(), "numerator_leading_coefficient": int(A[A.degree()]),
                      "denominator": DENOMINATOR, "denominator_exponent": 2,
                      "centering_exponent": -15*d,
                      "resultant_P_A3": str(scaled_norm), "original_norm": str(original_norm),
                      "trace_norm": str(trace_norm),
                      "squarefree_content": int(content), "root_degree_with_multiplicity": total_degree,
                      "squarefree_factors_and_root_balls": factor_records,
                      "haar_mean": display(haar_mean), "original_mean": display(original_mean),
                      "log_two": display(log_two),
                      "differences": {key: display(value) for key, value in differences.items()},
                      "difference_signs": {key: sign(value) for key, value in differences.items()}}
            assert all(value != "undetermined" for value in record["difference_signs"].values())
            completed.append(record)
            save("verification-partial.json", {"complete": False, "inputs": completed})
            print(name, "Haar", record["haar_mean"], "original", record["original_mean"], flush=True)
        # The author payload is consulted only now, after every independent
        # numerator, norm and Jensen enclosure has been generated.
        author = json.loads((OUTPUT / "results.json").read_text(encoding="utf-8"))
        assert author["complete"] is True
        assert author["reported_absolute_error_bound"] == "1e-10"
        assert len(author["inputs"]) == len(completed)
        quantity_map = {"haar": "haar_mean", "original": "original_mean", "log2": "log_two"}
        difference_map = {"haar_minus_log2": "haar_minus_log_two",
                          "original_minus_log2": "original_minus_log_two",
                          "original_minus_haar": "original_minus_haar"}
        for own, other in zip(completed, author["inputs"]):
            assert own["name"] == other["name"]
            assert own["p_coefficients_ascending"] == other["p_coefficients_ascending"]
            assert own["degree"] == other["degree"]
            assert own["original_norm"] == other["original_norm"]
            assert own["trace_norm"] == other["trace_norm"]
            d = own["degree"]
            tq = fmpq_poly([0, 1])
            zp = fmpq_poly([1, 0, 1])
            reconstructed_A = fmpq_poly([0])
            defects = []
            for label in ("e", "f", "g"):
                poly = fmpq_poly([fmpq(value) for value in other["global_defect_coefficients"][label]])
                defects.append(poly)
                n = poly.degree()
                lift = sum((poly[k] * zp**k * tq**(n-k) for k in range(n+1)), fmpq_poly([0]))
                assert 15*d - 2*n >= 0
                reconstructed_A += DENOMINATOR**2 * tq**(15*d-2*n) * lift**2
            assert defects[0].gcd(defects[1]).gcd(defects[2]).degree() == 0
            assert reconstructed_A == fmpq_poly(own["numerator_coefficients_ascending"])
            comparisons = {}
            for key in list(quantity_map) + list(difference_map):
                own_text = own[quantity_map[key]] if key in quantity_map else own["differences"][difference_map[key]]
                own_ball = arb(own_text)
                other_ball = arb(other["quantities"][key]["ball"])
                assert own_ball.is_finite() and other_ball.is_finite()
                assert own_ball.rad() < arb("1e-10") and other_ball.rad() < arb("1e-10")
                assert own_ball.overlaps(other_ball)
                assert sign(own_ball) == sign(other_ball) == other["quantities"][key]["sign"]
                assert abs(own_ball-arb(other["quantities"][key]["decimal"])) < arb("1e-10")
                assert other["quantities"][key]["absolute_error_bound"] == "1e-10"
                comparisons[key] = {"both_methods_certify": True, "enclosures_overlap": True,
                                    "sign": sign(own_ball), "author_decimal_error_lt_1e_minus_10": True}
            own["author_comparison"] = {"same_original_input_and_degree": True,
                                         "exact_norms_match": True,
                                         "exact_unreduced_defect_laurent_identity": True,
                                         "exact_defect_gcd_degree_zero": True,
                                         "quantities": comparisons}
        save("verification.json", {"complete": True, "arithmetic": "exact integer FLINT polynomials and Arb/Acb rigorous balls",
                                   "flint_version": flint.__version__, "precision_bits": PRECISION_BITS,
                                   "root_tolerance": "1e-40", "root_max_precision_bits": 2048,
                                   "required_persisted_scalar_radius_lt": "1e-10", "inputs": completed})
        (OUTPUT / "verification-partial.json").unlink()
    except Exception as error:
        save("verification-partial.json", {"complete": False, "error": repr(error), "inputs": completed})
        raise


if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        try:
            result = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker"], timeout=TIMEOUT_SECONDS)
            raise SystemExit(result.returncode)
        except subprocess.TimeoutExpired:
            print("Stopped: independent invocation exceeded 300 seconds; partial output is incomplete.", file=sys.stderr)
            raise SystemExit(124)
    else:
        raise SystemExit("No scope-changing command-line options are supported.")
