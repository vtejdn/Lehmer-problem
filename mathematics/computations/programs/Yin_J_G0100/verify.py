"""Independent H35/Jensen check of the fixed two-input buffered-shear screen.

Only J_G is newly evaluated.  J_V is explicitly reused from the complete J99
independent payload accepted by R522; missing prior evidence is not recomputed.
No author program or new author numerical output generates this arithmetic.
The precision schedule and subprocess bound are fixed, and there is no grid.
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
PRIOR_LOCATOR = "mathematics/computations/outputs/Yin_J_G0099/verification.json"
PRIOR = ROOT / PRIOR_LOCATOR
EXPECTED = (
    ("quartic_Salem_seed", [1, -1, -1, -1, 1]),
    ("Lehmer_degree10", [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]),
)
PRECISIONS = (256, 512)
TIMEOUT_SECONDS = 300
ROOT_TOLERANCE = "1e-30"


def save(name, payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT / (name + ".writing")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT / name)


def worker():
    import flint
    from flint import acb_poly, arb, ctx, fmpq, fmpq_poly, fmpz_poly

    source = json.loads(INPUT.read_text(encoding="utf-8"))
    selected = [(item["name"], item["coefficients_ascending"])
                for item in source["inputs"] if item["name"] in dict(EXPECTED)]
    assert selected == list(EXPECTED)
    # This is the declared, already accepted mathematical dependency.
    # No root finding or new integral for J_V is performed in this program.
    prior = json.loads(PRIOR.read_text(encoding="utf-8"))
    assert prior["complete"] is True and prior["independent_complete"] is True
    assert prior["comparison_pending"] is False
    assert prior["reported_absolute_error_bound"] == "1e-10"
    assert [(item["name"], item["p_coefficients_ascending"])
            for item in prior["inputs"]] == list(EXPECTED)
    prior_by_name = {item["name"]: item for item in prior["inputs"]}
    completed, attempts = [], []

    def coefficients(poly):
        return [int(value) for value in poly]

    def sign(value):
        return "positive" if value > 0 else "negative" if value < 0 else "undetermined"

    def enclosure(value):
        assert value.is_finite()
        text = value.str(50, more=True)
        saved = arb(text)
        assert saved.contains(value) and saved.rad() < arb("1e-10")
        return text

    def quantity(value):
        text = enclosure(value)
        decimal = f"{float(value.mid()):.12f}"
        assert abs(arb(text)-arb(decimal)) < arb("1e-10")
        return {"ball": text, "decimal": decimal,
                "absolute_error_bound": "1e-10", "sign": sign(value)}

    def jensen(poly, precision):
        content, factors = poly.factor_squarefree()
        product = fmpz_poly([content])
        count = 0
        value = arb(abs(int(poly[poly.degree()]))).log()
        factor_records = []
        for factor, multiplicity in factors:
            product *= factor**multiplicity
            assert factor.gcd(factor.derivative()).degree() == 0
            roots = acb_poly(factor).roots(tol=arb(ROOT_TOLERANCE), maxprec=precision)
            assert len(roots) == factor.degree()
            assert all(not roots[i].overlaps(roots[j])
                       for i in range(len(roots)) for j in range(i))
            count += multiplicity*len(roots)
            records = []
            for root in roots:
                modulus = abs(root)
                contribution = arb(1).max(modulus).log()
                value += multiplicity*contribution
                records.append({"real": enclosure(root.real), "imag": enclosure(root.imag),
                                "log_plus_modulus": enclosure(contribution),
                                "circle_side": "outside" if modulus > 1 else
                                               "inside" if modulus < 1 else "overlaps"})
            factor_records.append({"coefficients_ascending": coefficients(factor),
                                   "multiplicity": multiplicity, "roots": records})
        assert product == poly and count == poly.degree()
        return value, {"squarefree_content": int(content),
                       "degree_with_multiplicity": count, "factors": factor_records}

    try:
        for name, values in EXPECTED:
            d = len(values)-1
            assert d % 2 == 0 and values == values[::-1] and values[0] == values[d] == 1
            old = prior_by_name[name]
            assert old["degree"] == d and old["V_denominator"] == 800**2
            assert old["V_centering_exponent"] == -10*d
            assert old["author_comparison"]["quantities"]["J_V"]["independent_enclosures_overlap"] is True

            def power_substitution(exponent):
                result = [0]*(exponent*d+1)
                for index, coefficient in enumerate(values):
                    result[exponent*index] = coefficient
                return fmpz_poly(result)

            H35 = 250*power_substitution(3)**5 - 243*power_substitution(5)**3
            assert H35.degree() == 15*d and H35[0] == H35[15*d] == 7
            assert coefficients(H35) == coefficients(H35)[::-1]
            record = None
            for precision in PRECISIONS:
                ctx.prec = precision
                try:
                    # Reparse the same prior enclosing ball at the current
                    # precision; this propagates its original uncertainty.
                    JV = arb(old["quantities"]["J_V"]["ball"])
                    assert JV.is_finite() and JV.rad() < arb("1e-10")
                    assert old["quantities"]["J_V"]["absolute_error_bound"] == "1e-10"
                    assert sign(JV) == old["quantities"]["J_V"]["sign"]
                    assert abs(JV-arb(old["quantities"]["J_V"]["decimal"])) < arb("1e-10")
                    mH35, roots = jensen(H35, precision)
                    JG = 2*mH35-2*arb(30375).log()
                    log2 = arb(2).log()
                    total = JG+JV+log2
                    assert sign(total) != "undetermined"
                    quantities = {"J_G": quantity(JG), "J_V": quantity(JV), "log2": quantity(log2),
                                  "screen_sum": quantity(total),
                                  "all_parameter_envelope": quantity(log2+total/2),
                                  "envelope_minus_log2": quantity(total/2)}
                    # This is a consequence of the same component screen,
                    # not another integral or a claim of an attained minimum.
                    margin_excluded = total/2 > -arb(1)/16
                    assert margin_excluded
                    record = {"name": name, "p_coefficients_ascending": values, "degree": d,
                              "H35_coefficients_ascending": coefficients(H35),
                              "H35_degree": H35.degree(), "H35_leading_coefficient": 7,
                              "G_squared_denominator": 30375**2, "G_centering_exponent": -15*d//2,
                              "H35_mahler_log": quantity(mH35), "H35_roots": roots,
                              "precision_bits": precision, "root_max_precision_bits": precision,
                              "J_V_reused": {"source": PRIOR_LOCATOR,
                                             "source_quantity": old["quantities"]["J_V"],
                                             "source_input_checked": True,
                                             "source_complete_checked": True,
                                             "recomputed": False},
                              "quantities": quantities,
                              "screen": "excludes_all_real_s_positive_q" if total > 0 else "not_excluded",
                              "operational_margin_one_sixteenth_excluded": bool(margin_excluded),
                              "parameter_grid_evaluations": 0}
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
            print(name, "bits", record["precision_bits"],
                  {key: value["decimal"] for key, value in record["quantities"].items()},
                  record["screen"], flush=True)
        # Consult the new author's payload only after both independent H35
        # Jensen calculations are finished.  It is never a generator input.
        author = json.loads((OUTPUT/"results.json").read_text(encoding="utf-8"))
        assert author["complete"] is True and author["parameter_grid_evaluations"] == 0
        assert author["new_distinct_component_integrals"] == 2
        assert author["precision_schedule_bits"] == list(PRECISIONS)
        assert author["batch_timeout_seconds"] == TIMEOUT_SECONDS
        assert author["reported_absolute_error_bound"] == "1e-10"
        assert author["prior_V_source"] == "mathematics/computations/outputs/Yin_J_G0099/results.json"
        author_prior = json.loads((ROOT/author["prior_V_source"]).read_text(encoding="utf-8"))
        assert author_prior["complete"] is True
        assert [(item["name"], item["p_coefficients_ascending"])
                for item in author_prior["inputs"]] == list(EXPECTED)
        assert len(author["inputs"]) == len(completed)
        tq, zp = fmpq_poly([0, 1]), fmpq_poly([1, 0, 1])

        def lift(poly):
            n = poly.degree()
            return sum((poly[k]*zp**k*tq**(n-k) for k in range(n+1)), fmpq_poly([0]))

        mapping = {"J_G": "J_G", "J_V": "J_V_reused", "log2": "log2",
                   "screen_sum": "screen_sum", "all_parameter_envelope": "all_s_q_lower_envelope",
                   "envelope_minus_log2": "envelope_minus_log2"}
        for own, other, previous_author in zip(completed, author["inputs"], author_prior["inputs"]):
            assert own["name"] == other["name"] == previous_author["name"]
            assert own["p_coefficients_ascending"] == other["p_coefficients_ascending"]
            assert own["degree"] == other["degree"]
            assert other["precision_bits"] in PRECISIONS and other["parameter_grid_evaluations"] == 0
            d = own["degree"]
            T = fmpq_poly([fmpq(value) for value in other["trace_coefficients_ascending"]])
            assert T.degree() == d//2 and lift(T) == fmpq_poly(own["p_coefficients_ascending"])
            g = fmpq_poly([fmpq(value) for value in other["global_g_coefficients_ascending"]])
            H35 = fmpq_poly(own["H35_coefficients_ascending"])
            assert g.degree() == other["centering_shift"] == 15*d//2
            assert -30375*lift(g) == H35
            centered = fmpq_poly(other["centered_g_integer_coefficients_ascending"])
            assert other["centered_g_scalar_denominator"] > 0
            assert other["centered_g_scalar_denominator"]*H35 == -30375*centered
            assert set(other["quantities"]) == set(mapping.values())
            original_author_jv = arb(previous_author["quantities"]["J_V"]["ball"])
            repeated_author_jv = arb(other["quantities"]["J_V_reused"]["ball"])
            assert repeated_author_jv.contains(original_author_jv)
            comparisons = {}
            for key, author_key in mapping.items():
                own_ball = arb(own["quantities"][key]["ball"])
                other_ball = arb(other["quantities"][author_key]["ball"])
                assert own_ball.is_finite() and other_ball.is_finite()
                assert own_ball.rad() < arb("1e-10") and other_ball.rad() < arb("1e-10")
                assert own_ball.overlaps(other_ball)
                assert sign(own_ball) == sign(other_ball) == other["quantities"][author_key]["sign"]
                assert other["quantities"][author_key]["absolute_error_bound"] == "1e-10"
                assert abs(own_ball-arb(other["quantities"][author_key]["decimal"])) < arb("1e-10")
                comparisons[key] = {"independent_enclosures_overlap": True,
                                    "sign": sign(own_ball),
                                    "author_decimal_error_lt_1e_minus_10": True}
            expected_screen = ("excluded_all_real_s_positive_q" if
                               own["screen"] == "excludes_all_real_s_positive_q" else "screen_inconclusive")
            assert other["screen"] == expected_screen
            own["author_comparison"] = {"same_original_input": True, "exact_trace_identity": True,
                                         "exact_unreduced_g_H35_identity": True,
                                         "exact_centered_scalar_identity": True,
                                         "prior_author_J_V_enclosure_retained": True,
                                         "screen_agrees": True, "quantities": comparisons}
        save("verification.json", {"complete": True, "independent_complete": True,
                                   "comparison_pending": False,
                                   "scope": "H35 logarithm on exactly two original inputs; J_V reused",
                                   "flint_version": flint.__version__,
                                   "allowed_precision_bits": list(PRECISIONS),
                                   "root_tolerance": ROOT_TOLERANCE,
                                   "batch_timeout_seconds": TIMEOUT_SECONDS,
                                   "reported_absolute_error_bound": "1e-10",
                                   "new_distinct_component_integrals": 2,
                                   "parameter_grid_evaluations": 0,
                                   "attempts": attempts, "inputs": completed})
        (OUTPUT/"verification-partial.json").unlink()
    except Exception as error:
        save("verification-partial.json", {"complete": False, "error": repr(error),
                                           "attempts": attempts, "inputs": completed})
        raise


if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        try:
            run = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker"],
                                 timeout=TIMEOUT_SECONDS)
            raise SystemExit(run.returncode)
        except subprocess.TimeoutExpired:
            print("Stopped at the independent 300-second bound; incomplete output remains explicit.",
                  file=sys.stderr)
            raise SystemExit(124)
    else:
        raise SystemExit("No scope-changing command-line options are supported.")
