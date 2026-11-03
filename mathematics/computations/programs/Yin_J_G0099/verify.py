"""Independent Stage 1 Jensen certification for the two fixed balanced inputs.

The construction uses only the original integer P coefficients and H numerators.
No author program, trace defect or generated author value enters this arithmetic.
The fixed 256/512-bit attempts and 300-second subprocess cap cannot be expanded
through command-line parameters.  Author comparisons are added only after the
independent calculation is complete.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
INPUT = HERE.parent / "Yin_J_G0097/input.json"
EXPECTED = (
    ("quartic_Salem_seed", [1, -1, -1, -1, 1]),
    ("Lehmer_degree10", [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]),
)
PRECISIONS = (256, 512)
TIMEOUT_SECONDS = 300
DENOMINATOR = 972000
ROOT_TOLERANCE = "1e-30"


def save(name, value):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT / (name + ".writing")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT / name)


def worker():
    import flint
    from flint import acb_poly, arb, ctx, fmpq, fmpq_poly, fmpz_poly

    specification = json.loads(INPUT.read_text(encoding="utf-8"))
    assert specification["window_multiple"] == 2 and specification["threshold"] == 4
    original = {item["name"]: item["coefficients_ascending"] for item in specification["inputs"]}
    assert all(original.get(name) == values for name, values in EXPECTED)
    completed = []
    attempts = []

    def coefficients(poly):
        return [int(value) for value in poly]

    def sign(value):
        return "positive" if value > 0 else "negative" if value < 0 else "undetermined"

    def enclosure(value):
        assert value.is_finite()
        text = value.str(50, more=True)
        saved = arb(text)
        assert saved.contains(value)
        assert saved.rad() < arb("1e-10")
        return text

    def quantity(value):
        text = enclosure(value)
        decimal = f"{float(value.mid()):.12f}"
        assert abs(value - arb(decimal)) < arb("1e-10")
        return {"ball": text, "decimal": decimal,
                "absolute_error_bound": "1e-10", "sign": sign(value)}

    def jensen(poly, precision):
        assert poly.degree() >= 0 and poly != 0
        content, factors = poly.factor_squarefree()
        product = fmpz_poly([content])
        total_degree = 0
        measure = arb(abs(int(poly[poly.degree()]))).log()
        factor_records = []
        for factor, multiplicity in factors:
            product *= factor**multiplicity
            assert factor.gcd(factor.derivative()).degree() == 0
            roots = acb_poly(factor).roots(tol=arb(ROOT_TOLERANCE), maxprec=precision)
            assert len(roots) == factor.degree()
            assert all(not roots[i].overlaps(roots[j])
                       for i in range(len(roots)) for j in range(i))
            total_degree += multiplicity * len(roots)
            root_records = []
            for root in roots:
                modulus = abs(root)
                # This interval maximum remains enclosing even when the root
                # ball intersects the unit circle.  No side guess is made.
                log_plus = arb(1).max(modulus).log()
                measure += multiplicity * log_plus
                root_records.append({"real": enclosure(root.real),
                                     "imag": enclosure(root.imag),
                                     "log_plus_modulus": enclosure(log_plus),
                                     "circle_side": "outside" if modulus > 1 else
                                                    "inside" if modulus < 1 else "overlaps"})
            factor_records.append({"coefficients_ascending": coefficients(factor),
                                   "multiplicity": multiplicity, "roots": root_records})
        assert product == poly and total_degree == poly.degree()
        return measure, {"coefficients_ascending": coefficients(poly),
                         "degree": poly.degree(),
                         "leading_coefficient": int(poly[poly.degree()]),
                         "squarefree_content": int(content),
                         "root_degree_with_multiplicity": total_degree,
                         "factors": factor_records,
                         "mahler_log": quantity(measure)}

    try:
        for name, values in EXPECTED:
            d = len(values) - 1
            assert d % 2 == 0 and values == values[::-1] and values[0] == values[d] == 1
            t = fmpz_poly([0, 1])

            def power_substitution(exponent):
                result = [0] * (exponent * d + 1)
                for index, coefficient in enumerate(values):
                    result[exponent * index] = coefficient
                return fmpz_poly(result)

            P2, P3, P5 = (power_substitution(exponent) for exponent in (2, 3, 5))
            H23 = 9 * P2**3 - 8 * P3**2
            H25 = 75 * P2**5 - 64 * P5**2
            H35 = 250 * P3**5 - 243 * P5**3
            AU = 13500**2 * t**(9*d) * H23**2 + 32**2 * H35**2
            assert H23.degree() == 6*d and H23[6*d] == 1
            assert H25.degree() == 10*d and H25[10*d] == 11
            assert H35.degree() == 15*d and H35[15*d] == 7
            assert AU.degree() == 30*d and AU[0] == AU[30*d] == 50176
            assert coefficients(AU) == coefficients(AU)[::-1]
            assert coefficients(H25) == coefficients(H25)[::-1]
            record = None
            for precision in PRECISIONS:
                ctx.prec = precision
                try:
                    mU, numerator_u = jensen(AU, precision)
                    mV, numerator_v = jensen(H25, precision)
                    JU = mU - 2 * arb(DENOMINATOR).log()
                    JV = 2 * mV - 2 * arb(800).log()
                    component_sum = JU + JV
                    log2 = arb(2).log()
                    lower_envelope = log2 + component_sum / 2
                    assert sign(component_sum) != "undetermined"
                    quantities = {"J_U": quantity(JU), "J_V": quantity(JV),
                                  "component_sum": quantity(component_sum),
                                  "lower_envelope": quantity(lower_envelope),
                                  "lower_envelope_minus_log2": quantity(component_sum/2),
                                  "log2": quantity(log2)}
                    record = {"name": name, "p_coefficients_ascending": values,
                              "degree": d, "precision_bits": precision,
                              "root_max_precision_bits": precision,
                              "U_numerator": numerator_u, "V_H25": numerator_v,
                              "H23_coefficients_ascending": coefficients(H23),
                              "H35_coefficients_ascending": coefficients(H35),
                              "U_denominator": DENOMINATOR**2,
                              "U_centering_exponent": -15*d,
                              "V_denominator": 800**2,
                              "V_centering_exponent": -10*d,
                              "quantities": quantities,
                              "screen": "excludes_all_positive_q" if component_sum > 0 else
                                        "eligible_for_fixed_grid_only"}
                    attempts.append({"name": name, "precision_bits": precision, "success": True})
                    break
                except (ValueError, ArithmeticError, AssertionError) as error:
                    attempts.append({"name": name, "precision_bits": precision,
                                     "success": False, "error": repr(error)})
                    if precision == PRECISIONS[-1]:
                        raise
            assert record is not None
            completed.append(record)
            save("verification-partial.json", {"complete": False, "attempts": attempts, "inputs": completed})
            print(name, {key: value["decimal"] for key, value in record["quantities"].items()},
                  record["screen"], flush=True)
        # All independent arithmetic has finished before the author's payload
        # is consulted.  Comparisons do not generate the Jensen enclosures.
        author = json.loads((OUTPUT / "results.json").read_text(encoding="utf-8"))
        assert author["complete"] is True and author["weighted_grid_evaluations"] == 0
        assert author["precision_schedule_bits"] == list(PRECISIONS)
        assert author["batch_timeout_seconds"] == TIMEOUT_SECONDS
        assert author["reported_absolute_error_bound"] == "1e-10"
        assert len(author["inputs"]) == len(completed)
        tq, zp = fmpq_poly([0, 1]), fmpq_poly([1, 0, 1])

        def lift(poly):
            n = poly.degree()
            return sum((poly[k] * zp**k * tq**(n-k) for k in range(n+1)), fmpq_poly([0]))

        for own, other in zip(completed, author["inputs"]):
            assert own["name"] == other["name"]
            assert own["p_coefficients_ascending"] == other["p_coefficients_ascending"]
            assert own["degree"] == other["degree"]
            assert other["precision_bits"] in PRECISIONS and other["weighted_grid_evaluations"] == 0
            d = own["degree"]
            T = fmpq_poly([fmpq(value) for value in other["trace_coefficients_ascending"]])
            assert T.degree() == d//2
            assert lift(T) == fmpq_poly(own["p_coefficients_ascending"])
            defects = {key: fmpq_poly([fmpq(value) for value in values])
                       for key, values in other["global_defect_coefficients"].items()}
            assert set(defects) == {"e", "f", "g"}
            assert defects["e"].gcd(defects["g"]).degree() == 0
            H23 = fmpq_poly(own["H23_coefficients_ascending"])
            H25 = fmpq_poly(own["V_H25"]["coefficients_ascending"])
            H35 = fmpq_poly(own["H35_coefficients_ascending"])
            assert defects["e"].degree() == 3*d
            assert defects["f"].degree() == 5*d
            assert defects["g"].degree() == 15*d//2
            assert -72*lift(defects["e"]) == H23
            assert -800*lift(defects["f"]) == H25
            assert -30375*lift(defects["g"]) == H35
            AU = fmpq_poly(own["U_numerator"]["coefficients_ascending"])
            reconstructed = sum((DENOMINATOR**2 * tq**(15*d-2*defects[key].degree()) *
                                 lift(defects[key])**2 for key in ("e", "g")), fmpq_poly([0]))
            assert reconstructed == AU
            assert other["V_centering_shift"] == 5*d
            Vpoly = fmpq_poly(other["V_centered_f_polynomial"])
            assert other["V_scalar_denominator"] > 0
            assert other["V_scalar_denominator"] * H25 == -800 * Vpoly
            assert other["U_evidence"]["method"] == "analytic acb quadrature theta=pi*u"
            assert set(other["quantities"]) == set(own["quantities"])
            comparisons = {}
            for key, value in own["quantities"].items():
                own_ball = arb(value["ball"])
                other_ball = arb(other["quantities"][key]["ball"])
                assert own_ball.is_finite() and other_ball.is_finite()
                assert own_ball.rad() < arb("1e-10") and other_ball.rad() < arb("1e-10")
                assert own_ball.overlaps(other_ball)
                assert sign(own_ball) == sign(other_ball) == other["quantities"][key]["sign"]
                assert other["quantities"][key]["absolute_error_bound"] == "1e-10"
                assert abs(own_ball - arb(other["quantities"][key]["decimal"])) < arb("1e-10")
                comparisons[key] = {"independent_enclosures_overlap": True,
                                    "sign": sign(own_ball),
                                    "author_decimal_error_lt_1e_minus_10": True}
            expected_screen = "excluded_all_positive_q" if own["screen"] == "excludes_all_positive_q" else "stage2_pending"
            assert other["screen"] == expected_screen
            own["author_comparison"] = {"same_original_input": True,
                                         "exact_trace_identity": True,
                                         "exact_unreduced_defect_numerators": True,
                                         "exact_component_laurent_identity": True,
                                         "U_exact_gcd_degree_zero": True,
                                         "screen_agrees": True,
                                         "quantities": comparisons}
        save("verification.json", {"complete": True, "independent_complete": True,
                                   "comparison_pending": False,
                                   "scope": "Stage 1 only; two fixed original inputs",
                                   "arithmetic": "exact integer FLINT polynomials and rigorous Arb/Acb Jensen balls",
                                   "flint_version": flint.__version__,
                                   "allowed_precision_bits": list(PRECISIONS),
                                   "root_tolerance": ROOT_TOLERANCE,
                                   "reported_absolute_error_bound": "1e-10",
                                   "attempts": attempts, "inputs": completed})
        (OUTPUT / "verification-partial.json").unlink()
    except Exception as error:
        save("verification-partial.json", {"complete": False, "error": repr(error),
                                           "attempts": attempts, "inputs": completed})
        raise


if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        try:
            result = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker"],
                                    timeout=TIMEOUT_SECONDS)
            raise SystemExit(result.returncode)
        except subprocess.TimeoutExpired:
            print("Stopped: independent invocation exceeded 300 seconds; partial output is incomplete.",
                  file=sys.stderr)
            raise SystemExit(124)
    else:
        raise SystemExit("No scope-changing command-line options are supported.")
