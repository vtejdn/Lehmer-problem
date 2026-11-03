"""Independent whole-cell trace-polynomial certificate for the Lehmer screen.

The exact trace polynomial is reconstructed by triangular binomial elimination.
No author helper is imported.  The two integer H identities are checked exactly;
interval evaluation uses this trace polynomial rather than the author's Fourier
sum.  Every author-retained cell is checked, with only bounded dyadic refinement.
The already accepted J100 independent screen ball is reused without integration.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
INPUT = HERE.parent / "Yin_J_G0097/input.json"
PRIOR_LOCATOR = "mathematics/computations/outputs/Yin_J_G0100/verification.json"
AUTHOR_PRIOR_LOCATOR = "mathematics/computations/outputs/Yin_J_G0100/results.json"
EXPECTED = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
NAME = "Lehmer_degree10"
CELLS, THRESHOLD, BITS = 8192, 4, 256
MAX_DYADIC_DEPTH, TIMEOUT_SECONDS = 10, 120


def save(payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT / "verification.json.writing"
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(OUTPUT / "verification.json")


def selected(payload, coefficient_key):
    rows = [row for row in payload["inputs"] if row["name"] == NAME]
    assert len(rows) == 1 and rows[0][coefficient_key] == EXPECTED
    return rows[0]


def worker():
    import flint
    from flint import arb, ctx, fmpq_poly, fmpz_poly
    ctx.prec = BITS
    selected(json.loads(INPUT.read_text(encoding="utf-8")), "coefficients_ascending")
    d, r = len(EXPECTED)-1, (len(EXPECTED)-1)//2
    assert d == 10 and EXPECTED == EXPECTED[::-1] and EXPECTED[0] == EXPECTED[-1] == 1

    # t^r(t+t^-1)^k has binomial coefficients at exponents r+k-2j.
    # Remove these terms from highest exponent to lowest; no Chebyshev/Fourier
    # coefficient helper or author trace polynomial is used.
    remainder, trace = EXPECTED[:], [0]*(r+1)
    for k in range(r, -1, -1):
        trace[k] = remainder[r+k]
        for j in range(k+1):
            remainder[r+k-2*j] -= trace[k]*comb(k, j)
    assert all(value == 0 for value in remainder) and trace[-1] == 1

    t, zplus = fmpq_poly([0, 1]), fmpq_poly([1, 0, 1])

    def lift(poly):
        n = poly.degree()
        return sum((poly[k]*zplus**k*t**(n-k) for k in range(n+1)), fmpq_poly([0]))

    def compose(coefficients, argument):
        result = fmpq_poly([0])
        for coefficient in reversed(coefficients):
            result = result*argument+coefficient
        return result

    TP = fmpq_poly(trace)
    assert lift(TP) == fmpq_poly(EXPECTED)
    T2 = compose(trace, fmpq_poly([-2, 0, 1]))
    T3 = compose(trace, fmpq_poly([0, -3, 0, 1]))
    T5 = compose(trace, fmpq_poly([0, 5, 0, -5, 0, 1]))
    epoly = T3**2/9-T2**3/8
    gpoly = T5**3/125-2*T3**5/243

    def substituted(n):
        values = [0]*(n*d+1)
        for k, value in enumerate(EXPECTED):
            values[n*k] = value
        return fmpz_poly(values)

    H23 = 9*substituted(2)**3-8*substituted(3)**2
    H35 = 250*substituted(3)**5-243*substituted(5)**3
    assert epoly.degree() == 3*d and gpoly.degree() == 15*d//2
    assert -72*lift(epoly) == fmpq_poly(H23)
    assert -30375*lift(gpoly) == fmpq_poly(H35)
    assert H23.degree() == 6*d and H23[0] == H23[6*d] == 1
    assert H35.degree() == 15*d and H35[0] == H35[15*d] == 7

    # This is an explicitly accepted prior numerical input, not a fresh root
    # isolation.  Its actual ball, including uncertainty, is propagated below.
    previous = json.loads((ROOT/PRIOR_LOCATOR).read_text(encoding="utf-8"))
    assert previous["complete"] is True and previous["independent_complete"] is True
    assert previous["comparison_pending"] is False
    assert previous["reported_absolute_error_bound"] == "1e-10"
    old = selected(previous, "p_coefficients_ascending")
    assert old["degree"] == d and old["G_squared_denominator"] == 30375**2
    assert old["G_centering_exponent"] == -15*d//2
    assert old["H35_degree"] == H35.degree() and old["H35_leading_coefficient"] == 7
    assert old["H35_coefficients_ascending"] == [int(c) for c in H35]
    assert old["J_V_reused"]["source"] == "mathematics/computations/outputs/Yin_J_G0099/verification.json"
    for key in ("J_G", "J_V", "log2", "screen_sum"):
        item = old["quantities"][key]
        value = arb(item["ball"])
        assert value.is_finite() and value.rad() < arb("1e-10")
        assert item["absolute_error_bound"] == "1e-10"
        assert abs(value-arb(item["decimal"])) < arb("1e-10")
        assert item["sign"] == ("positive" if value > 0 else "negative" if value < 0 else "undetermined")
        assert old["author_comparison"]["quantities"][key]["independent_enclosures_overlap"] is True
    prior_sum = old["quantities"]["screen_sum"]
    screen = arb(prior_sum["ball"])
    log2 = arb(2).log()
    assert log2.overlaps(arb(old["quantities"]["log2"]["ball"]))
    assert screen < 0
    assert screen.overlaps(arb(old["quantities"]["J_G"]["ball"])
                           +arb(old["quantities"]["J_V"]["ball"])+log2)

    author = json.loads((OUTPUT/"results.json").read_text(encoding="utf-8"))
    assert author["complete"] is True and author["input_name"] == NAME
    assert author["p_coefficients_ascending"] == EXPECTED
    assert author["cell_count"] == CELLS and author["threshold"] == THRESHOLD
    assert author["precision_bits"] == 192 and author["batch_timeout_seconds"] == 120
    assert author["prior_source"] == AUTHOR_PRIOR_LOCATOR
    author_previous = json.loads((ROOT/AUTHOR_PRIOR_LOCATOR).read_text(encoding="utf-8"))
    assert author_previous["complete"] is True
    author_old = selected(author_previous, "p_coefficients_ascending")
    assert author["prior_screen_sum"] == author_old["quantities"]["screen_sum"]
    assert screen.overlaps(arb(author["prior_screen_sum"]["ball"]))
    groups = {"positive": author["positive_cells"], "negative": author["negative_cells"]}
    for side, cells in groups.items():
        assert all(type(k) is int and 0 <= k < CELLS for k in cells)
        assert cells == sorted(set(cells))
        assert len(cells) == author[side+"_count"]
    assert len(groups["positive"]) == 2062 and len(groups["negative"]) == 1206
    assert not set(groups["positive"]).intersection(groups["negative"])

    def enclosing(value):
        assert value.is_finite()
        text = value.str(55, more=True)
        assert arb(text).contains(value)
        return text

    def trace_interval(phase, multiplier):
        argument = 2*(2*multiplier*phase).cos_pi()
        value = arb(0)
        for coefficient in reversed(trace):
            value = value*argument+coefficient
        return value

    def ratio_interval(index, denominator):
        phase = arb(arb(2*index+1)/(2*denominator), arb(1)/(2*denominator))
        assert phase.contains(arb(index)/denominator)
        assert phase.contains(arb(index+1)/denominator)
        u, v, w = (trace_interval(phase, k) for k in (2, 3, 5))
        E = v**2/9-u**3/8
        G = w**3/125-2*v**5/243
        return None if G.contains(0) else E/G

    certificates, histogram, evaluations = {}, {}, 0
    for side, cells in groups.items():
        orientation = 1 if side == "positive" else -1
        certificates[side] = []
        for cell in cells:
            passed = False
            for depth in range(MAX_DYADIC_DEPTH+1):
                pieces = 2**depth
                least = None
                for j in range(pieces):
                    ratio = ratio_interval(pieces*cell+j, pieces*CELLS)
                    evaluations += 1
                    if ratio is None:
                        break
                    slack = orientation*ratio-THRESHOLD
                    if not slack > 0:
                        break
                    least = slack if least is None else least.min(slack)
                else:
                    assert least > 0
                    certificates[side].append({"cell": cell, "dyadic_depth": depth,
                                               "minimum_signed_slack": enclosing(least)})
                    histogram[str(depth)] = histogram.get(str(depth), 0)+1
                    passed = True
                    break
            assert passed, (side, cell, "fixed subdivision cap reached")

    count = min(len(certificates["positive"]), len(certificates["negative"]))
    assert (author["eta_numerator"], author["eta_denominator"]) == (count, CELLS)
    eta = arb(count)/CELLS
    correction = eta*(1+arb((THRESHOLD-(-THRESHOLD))**2)/8).log()
    strengthened, margin = screen+correction, (screen+correction)/2
    lower = log2+margin
    assert strengthened > 0 and margin > arb("0.1231807283")
    assert lower > arb("0.8163279088") and lower > log2
    own = {"delta": correction, "strengthened_screen": strengthened,
           "margin_above_log2": margin, "all_real_s_positive_q_lower_bound": lower}
    assert set(author["quantities"]) == set(own)
    comparisons = {}
    for key, value in own.items():
        other = arb(author["quantities"][key])
        assert other.is_finite() and other.rad() < arb("1e-10") and other > 0
        assert value.overlaps(other)
        comparisons[key] = {"independent_enclosures_overlap": True,
                            "author_radius_lt_1e_minus_10": True}

    payload = {"complete": True, "independent_complete": True,
               "input_name": NAME, "p_coefficients_ascending": EXPECTED,
               "trace_coefficients_ascending": trace,
               "exact_trace_and_H23_H35_identities_checked": True,
               "H23_coefficients_ascending": [int(c) for c in H23],
               "H35_coefficients_ascending": [int(c) for c in H35],
               "flint_version": flint.__version__, "precision_bits": BITS,
               "cell_count": CELLS, "threshold": THRESHOLD,
               "max_allowed_dyadic_depth": MAX_DYADIC_DEPTH,
               "batch_timeout_seconds": TIMEOUT_SECONDS,
               "certified_positive_count": len(certificates["positive"]),
               "certified_negative_count": len(certificates["negative"]),
               "subdivision_depth_histogram": histogram,
               "interval_evaluations": evaluations, "certified_cells": certificates,
               "eta_numerator": count, "eta_denominator": CELLS,
               "prior_source": PRIOR_LOCATOR, "prior_screen_sum": prior_sum,
               "prior_recomputed": False, "new_component_integrals": 0,
               "parameter_grid_evaluations": 0,
               "quantities": {key: enclosing(value) for key, value in own.items()},
               "author_comparisons": comparisons,
               "scope": "All retained original phase cells; every real s and q>0 on this one buffered Lehmer input."}
    save(payload)
    print(json.dumps({key: payload[key] for key in
                      ("complete", "certified_positive_count", "certified_negative_count",
                       "subdivision_depth_histogram", "interval_evaluations", "quantities")}, indent=2))


if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        try:
            worker()
        except Exception as error:
            save({"complete": False, "independent_complete": False,
                  "failure": repr(error), "precision_bits": BITS,
                  "max_allowed_dyadic_depth": MAX_DYADIC_DEPTH})
            raise
    elif not sys.argv[1:]:
        try:
            run = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker"],
                                 timeout=TIMEOUT_SECONDS)
            raise SystemExit(run.returncode)
        except subprocess.TimeoutExpired:
            save({"complete": False, "independent_complete": False,
                  "failure": "subprocess timeout", "seconds": TIMEOUT_SECONDS})
            raise SystemExit(124)
    else:
        raise SystemExit("No scope-changing command-line options are supported.")
