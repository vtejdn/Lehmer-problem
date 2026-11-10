"""Independent exact and interval checks for the two fixed J159 jet branches.

Run from the repository root with Python 3.14 and -B.
Only python-flint is required, from the existing J156 package directory by default.
No author module, optimizer, repair routine or measure evaluator is imported.
The earlier reviewer-owned real_cell_independent module supplies exact full geometric-block lifts, recurrence jets and 2048-bit E-basis Clenshaw checks.
The new affine conversion uses full monomial B polynomials and triangular division, independently of the author's sparse multiplication transform.
Floating record comparisons are labelled as such and certify no optimum.
"""

import argparse
from fractions import Fraction as F
import json
import math
from math import lcm
from pathlib import Path
import sys

from real_cell_independent import (
    DEFAULT_FLINT, FIXED, J_HOME, L, OUT_HOME,
    exact_polynomial, interval_signs, zero_jets,
)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def b_basis(degree):
    basis = [[1], [1, 1]]
    for j in range(1, degree):
        next_b = [0] + basis[j]
        for k, value in enumerate(basis[j - 1]):
            next_b[k] -= value
        basis.append(next_b)
    return basis[:degree + 1]


def monomial_sum(values, basis):
    result = [0] * len(values)
    for value, polynomial in zip(values, basis):
        for j, coefficient in enumerate(polynomial):
            result[j] += value * coefficient
    return result


def triangular_coordinates(polynomial, basis):
    residue = list(polynomial)
    result = [0] * len(residue)
    for j in range(len(residue) - 1, -1, -1):
        result[j] = residue[j]
        for k, coefficient in enumerate(basis[j]):
            residue[k] -= result[j] * coefficient
    assert not any(residue)
    return result


def fixed_jets(n):
    b, derivative = zero_jets(n)
    return (sum(value * b[n - 1 - i] for i, value in enumerate(FIXED)),
            b[n] + sum(value * derivative[n - 1 - i]
                       for i, value in enumerate(FIXED)))


def coefficients_from_monomial_branch(u, n, basis):
    assert len(u) == n - L - 1
    denominator = lcm(*(F(value).denominator for value in u))
    scaled = [int(F(value) * denominator) for value in u]
    monomial = [0, 0] + monomial_sum(scaled, basis)
    q0, qp = fixed_jets(n)
    monomial[0] -= q0 * denominator
    monomial[1] += (-1 - qp) * denominator
    free = triangular_coordinates(monomial, basis)
    return list(map(F, FIXED)) + [F(value, denominator) for value in reversed(free)]


def recover_monomial_branch(a, basis):
    n = len(a)
    free = list(reversed(a[L - 1:]))
    denominator = lcm(*(value.denominator for value in free))
    monomial = monomial_sum([int(value * denominator) for value in free], basis)
    q0, qp = fixed_jets(n)
    monomial[0] += q0 * denominator
    monomial[1] -= (-1 - qp) * denominator
    assert monomial[:2] == [0, 0]
    return [F(value, denominator)
            for value in triangular_coordinates(monomial[2:], basis)]


def rational_comparisons():
    p = 1009
    tests = {
        "last_gap_upper": F(22, 7*p)**2 < F(1, 25000),
        "last_gap_lower": F(9, p)**2 - F(9, p)**4/12 > F(1, 25000),
        "zero_jet": F(3*(p+2), 171465) == F(3033, 171465) < 1,
        "positive_node": F(31, 10*p)-F(29791, 24000*p**3) > F(1, 326),
        "negative_node": F(93, 10*p)-F(804357, 24000*p**3) > F(1, 109),
        "first_cross_product": 16*2400*p*p > 29791*326,
        "second_cross_product": 47*2400*p*p > 804357*109,
        "chord": 109*326 == 35534 and 326-109 == 217,
        "derivative": F(6, 171465)*35751 == F(214506, 171465) < 2,
    }
    assert all(tests.values())
    return tests


def signed_sine_float(a):
    n, p = len(a), 2*len(a)+1
    return [(1 if j < n else -1) * math.fsum(
        float(value)*math.sin(2*math.pi*j*(i+1)/p)
        for i, value in enumerate(a)) for j in range(1, n+1)]


def signed_sine_ball(a, j, arb):
    n, p = len(a), 2*len(a)+1
    theta = 2*arb.pi()*j/p
    node = 2*theta.cos()
    after_next = next_value = arb(0)
    for value in reversed(a):
        current = arb(value.numerator)/value.denominator + node*next_value-after_next
        after_next, next_value = next_value, current
    return (1 if j < n else -1)*theta.sin()*next_value


def exact_jet_values(a):
    b, derivative = zero_jets(len(a))
    return (sum(value*b[len(a)-1-i] for i, value in enumerate(a)),
            b[len(a)]+sum(value*derivative[len(a)-1-i]
                          for i, value in enumerate(a)))


def repair_records(record, cfg, basis, arb):
    repair = record["integer_repair"]
    attempts = repair["attempts"]
    assert len(attempts) == cfg["restarts"] == 6
    assert sum(item["descent_moves"] for item in attempts) == repair["total_descent_moves"] == 1118
    assert not repair["soft_deadline_reached"]
    reports = []
    for attempt, item in enumerate(attempts):
        assert item["attempt"] == attempt
        assert item["kicks"] == cfg["kicks_per_restart"] == 8
        assert item["descent_moves"] <= cfg["steps_per_restart"] == 400
        assert item["loss_scaling"] == ("raw" if attempt % 2 == 0 else "divide_by_trace_squared")
        u = item["u_integer"]
        assert len(u) == 860 and all(type(value) is int for value in u)
        a = coefficients_from_monomial_branch(u, 1001, basis)
        assert all(value.denominator == 1 for value in a)
        assert exact_jet_values(a) == (0, -1)
        assert recover_monomial_branch(a, basis) == u
        endpoint = 2+sum((-1)**i*value for i, value in enumerate(a))
        assert endpoint == 2006+4*sum((-1)**j*value for j, value in enumerate(u))
        values = signed_sine_float(a)
        failed = sum(value <= 0 for value in values)
        final = item["final"]
        assert failed == final["nonpositive_sign_rows"]
        assert abs(min(values)-final["minimum_signed_sine"]) < 1e-7
        assert endpoint == final["endpoint"]
        assert final["Q0"] == 0 and final["Qprime0"] == -1
        assert max(map(abs, a)) == final["max_abs_a"]
        assert max(map(abs, u)) == final["max_abs_u"]
        common_loss = math.fsum(min(value-cfg["sine_margin"], 0)**2 for value in values)
        common_loss += min(float((endpoint-2)/4), 0)**2
        assert abs(common_loss-item["common_loss"]) < 1e-4
        local_loss = 0.0
        for j, value in enumerate(values, 1):
            scale = 1 if attempt % 2 == 0 else 1/(2*math.cos(2*math.pi*j/2003))**2
            local_loss += min(scale*(value-cfg["sine_margin"]), 0)**2
        local_loss += min(float((endpoint-2)/4), 0)**2
        assert abs(local_loss-item["local_scaled_loss"]) < 1e-3
        worst = min(range(len(values)), key=values.__getitem__)+1
        counterexample = signed_sine_ball(a, worst, arb)
        assert counterexample < 0
        reports.append({"attempt":attempt, "endpoint":str(endpoint),
                        "Q0":"0", "Qprime0":"-1", "all_parameters_integer":True,
                        "failed_rows_float_recomputed":failed,
                        "minimum_signed_sine_float_recomputed":min(values),
                        "common_loss_float_recomputed":common_loss,
                        "local_loss_float_recomputed":local_loss,
                        "max_abs_a":int(max(map(abs,a))),
                        "exact_counterexample_node":worst,
                        "signed_sine_counterexample_ball":str(counterexample)})
    selected = min(attempts, key=lambda item:item["common_loss"])
    assert selected["attempt"] == 0
    assert repair["best_u_integer"] == selected["u_integer"]
    a_best = coefficients_from_monomial_branch(repair["best_u_integer"],1001,basis)
    assert a_best == record["best_integer_coefficients"]
    assert record["best_integer_metrics"] == selected["final"]
    signs = interval_signs(a_best,[record["best_integer_check"]],arb)
    assert signs["opposite_strict_signs"] == 490
    rounded = [round(value) for value in record["branch_lp"]["u_float"]]
    initial = coefficients_from_monomial_branch(rounded,1001,basis)
    initial_values = signed_sine_float(initial)
    assert sum(value <= 0 for value in initial_values) == 456
    assert abs(min(initial_values)-attempts[0]["initial"]["minimum_signed_sine"]) < 1e-7
    assert attempts[0]["initial"] == attempts[1]["initial"]
    return {"starts":reports, "selected_attempt":0, "selected_full_interval_signs":signs,
            "initial_rounding_failed_rows_float":456,
            "reported_accepted_moves":1118, "reported_elapsed_seconds":repair["elapsed_seconds"],
            "limits":"final records verified; no optimization rerun, path replay, optimality or infeasibility claim"}


def p1009_model(lp, mip):
    n,p = 504,1009
    b, derivative = zero_jets(n)
    for record in (lp,mip):
        assert tuple(record[key] for key in ("p","n","x","kappa","prefix_L")) == (p,n,0,1,140)
        assert record["fixed_coefficients"] == FIXED
        assert record["free_indices"] == list(range(139,n))
        assert record["endpoint_row"] == [(-1)**i for i in range(139,n)]
        assert record["endpoint_rhs"] == -279
        assert record["q0_row"] == [b[n-1-i] for i in range(139,n)]
        assert record["qprime_row"] == [derivative[n-1-i] for i in range(139,n)]
        assert (record["q0_fixed"],record["qprime_fixed"]) == (2,365)
        assert (record["requested_Q0"],record["requested_Qprime0"]) == (0,-1)
        assert record["options"]["threads"] == 1
        assert record["options"]["random_seed"] == 0
        assert record["options"]["time_limit"] == 60
        for key in ("primal_feasibility_tolerance","dual_feasibility_tolerance","mip_feasibility_tolerance"):
            assert record["options"][key] == 1e-9
    assert lp["floating_signed_sine_rows"] == mip["floating_signed_sine_rows"]
    assert lp["floating_fixed_signed_sine"] == mip["floating_fixed_signed_sine"]
    error = fixed_error = 0.0
    for j,row in enumerate(lp["floating_signed_sine_rows"],1):
        assert len(row) == 365
        sign = 1 if j < n else -1
        for i,value in enumerate(row,139):
            reference = sign*math.sin(2*math.pi*j*(i+1)/p)
            error = max(error,abs(value-reference))
        reference_fixed = sign*math.fsum(value*math.sin(2*math.pi*j*(i+1)/p)
                                        for i,value in enumerate(FIXED))
        fixed_error = max(fixed_error,abs(lp["floating_fixed_signed_sine"][j-1]-reference_fixed))
    assert len(lp["floating_signed_sine_rows"]) == 504
    assert error < 3e-12 and fixed_error < 1e-9
    assert lp["mode"] == "lp" and lp["model_status"] == "HighsModelStatus.kOptimal"
    assert lp["solution_value_valid"]
    raw = list(map(F,FIXED))+[F(str(value)) for value in lp["raw_tail"]]
    assert list(map(F,lp["candidate"]["coefficients_rational"])) == raw
    exact = exact_polynomial(raw,prefix=True)
    assert (exact["Q0"],exact["Qprime0"]) == (
        F(-624399,50000000000000000),F(-199999999992496431,200000000000000000))
    assert not lp["candidate"]["requested_jets_satisfied"]
    for key in ("Q0","Qprime0","endpoint"):
        assert F(lp["candidate"][key]) == exact[key]
    minimum = min(signed_sine_float(raw))
    assert abs(minimum-lp["observed_signed_sine_minimum"]) < 1e-7
    assert abs(float(exact["endpoint"])-lp["observed_endpoint"]) < 1e-7
    assert mip["mode"] == "integer" and mip["model_status"] == "HighsModelStatus.kTimeLimit"
    assert not mip["solution_value_valid"] and mip["candidate"] is None
    assert mip["integer_coefficient_bound"] == 16 and mip["integer_search_sine_margin"] == 1e-7
    return raw, {"matrix_shape":[504,365],"maximum_float_coefficient_error":error,
                 "maximum_float_fixed_row_error":fixed_error,
                 "LP_reported_margin":lp["optimized_margin"],
                 "LP_recomputed_float_minimum":minimum,
                 "LP_exact_raw_Q0":str(exact["Q0"]),"LP_exact_raw_Qprime0":str(exact["Qprime0"]),
                 "MIP_status":mip["model_status"],"MIP_reported_elapsed_seconds":mip["elapsed_seconds"],
                 "MIP_box":[-16,16],"MIP_variables":365,"MIP_sine_margin":1e-7,
                 "limits":"floating model consistency; numerical LP observation and one timeout, no exact optimum or infeasibility"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--flint-path",type=Path,default=DEFAULT_FLINT)
    args = parser.parse_args()
    sys.path.insert(0,str(args.flint_path))
    import flint
    from flint import arb,ctx
    ctx.prec,ctx.threads = 2048,1
    inputs = J_HOME/"inputs"
    cfg = load(inputs/"jet_lattice.json")
    data2003 = load(inputs/"jet_lattice_real.json")
    record2003 = load(OUT_HOME/"jet_lattice.json")
    check2003 = load(OUT_HOME/"jet_lattice_real_verification.json")
    assert cfg == record2003["configuration"]
    assert tuple(data2003[key] for key in ("p","prefix_L","Q0","Qprime0")) == (2003,140,0,-1)
    assert tuple(cfg[key] for key in ("lp_seconds","repair_seconds","seed","restarts","steps_per_restart",
                                     "kicks_per_restart","kick_coordinates","max_step","sine_margin")) == (45,45,20261110,6,400,8,4,4,1e-7)
    assert fixed_jets(1001) == (-2,861) and fixed_jets(504) == (2,365)
    basis2003 = b_basis(861)
    u2003 = list(map(F,data2003["u_rational"]))
    assert u2003 == [F(str(value)) for value in record2003["branch_lp"]["u_float"]]
    a2003 = coefficients_from_monomial_branch(u2003,1001,basis2003)
    assert recover_monomial_branch(a2003,basis2003) == u2003
    exact2003 = exact_polynomial(a2003,prefix=True)
    assert (exact2003["Q0"],exact2003["Qprime0"]) == (0,-1)
    assert exact2003["endpoint"] == F(339957315800243528021,250000000000000000)
    assert not exact2003["all_coefficients_integer"] and not exact2003["polynomial_is_integer"]
    for check in (check2003,record2003["real_branch_check"]):
        assert F(check["endpoint"]) == exact2003["endpoint"] and check["endpoint_positive"]
    signs2003 = interval_signs(a2003,[check2003,record2003["real_branch_check"]],arb)
    assert signs2003["all_required_signs"]
    print("Independent p2003 monomial branch, full polynomial and all signs passed.",flush=True)

    data1009 = load(inputs/"jet_p1009_witness.json")
    lp = load(OUT_HOME/"prefix_cell_lp_p1009_Q0_0_Qp_neg1.json")
    mip = load(OUT_HOME/"prefix_cell_integer_p1009_Q0_0_Qp_neg1.json")
    raw,model = p1009_model(lp,mip)
    a1009 = list(map(F,data1009["coefficients_rational"]))
    assert len(a1009) == 504 and a1009[:139] == FIXED
    assert tuple(data1009[key] for key in ("p","n","x","kappa","prefix_L","Q0","Qprime0")) == (1009,504,0,1,140,0,-1)
    assert (data1009["free_tail_dimension"],data1009["jet_branch_dimension"]) == (365,363)
    increments = [new-old for new,old in zip(a1009,raw)]
    assert all(value == 0 for value in increments[:502])
    assert increments[502:] == [F(-7503569,200000000000000000),F(2000233,40000000000000000)]
    correction = data1009["correction"]
    raw_exact = exact_polynomial(raw,prefix=True)
    exact1009 = exact_polynomial(a1009,prefix=True)
    assert (exact1009["Q0"],exact1009["Qprime0"]) == (0,-1)
    assert exact1009["endpoint"] == F(20721501956983266601,50000000000000000)
    assert exact1009["endpoint"] == raw_exact["endpoint"]+increments[502]-increments[503]
    expected_correction = {
        "original_Q0":raw_exact["Q0"],"original_Qprime0":raw_exact["Qprime0"],
        "index_502_B1_increment":increments[502],"index_503_B0_increment":increments[503],
        "original_endpoint":raw_exact["endpoint"],"corrected_endpoint":exact1009["endpoint"]}
    assert {key:F(value) for key,value in correction.items()} == expected_correction
    basis1009 = b_basis(364)
    u1009 = recover_monomial_branch(a1009,basis1009)
    assert len(u1009) == 363 and coefficients_from_monomial_branch(u1009,504,basis1009) == a1009
    assert exact1009["endpoint"] == -450-4*sum((-1)**j*value for j,value in enumerate(u1009))
    assert not exact1009["all_coefficients_integer"] and not exact1009["polynomial_is_integer"]
    checks1009 = [load(OUT_HOME/name) for name in ("jet_p1009_preparation.json","jet_p1009_verification.json")]
    for check in checks1009:
        assert F(check["endpoint"]) == exact1009["endpoint"] and check["endpoint_positive"]
        assert check["Q0"] == "0" and check["Qprime0"] == "-1"
        assert check["fixed_Q0"] == 2 and check["fixed_Qprime0"] == 365
        assert not check["all_coefficients_integer"]
    signs1009 = interval_signs(a1009,checks1009,arb)
    raw_signs = interval_signs(raw,[lp["candidate"]],arb)
    assert signs1009["all_required_signs"] and raw_signs["all_required_signs"]
    print("Independent p1009 correction, full polynomial, lattice and all signs passed.",flush=True)

    repairs = repair_records(record2003,cfg,basis2003,arb)
    result = {
        "scope":"two fixed rational jet-branch witnesses, p1009 applicability and finite failure records; no integer supply or nonneutrality",
        "python":sys.version.split()[0],"python_flint":flint.__version__,"precision_bits":2048,
        "method":"reviewer-owned monomial branch conversion, geometric-block full lift, recurrence jets and E-basis Clenshaw signs",
        "p1009_exact_comparisons":rational_comparisons(),
        "p2003_witness":exact2003,"p2003_witness_signs":signs2003,
        "p1009_witness":exact1009,"p1009_witness_signs":signs1009,
        "p1009_raw_LP_signs":raw_signs,"p1009_exact_correction":expected_correction,
        "p1009_recovered_branch_parameters":[str(value) for value in u1009],
        "p1009_model":model,"p2003_finite_repair":repairs,
        "not_performed":"No author module, optimizer, repair, root or Mahler evaluator was executed; no D22 was read."}
    output = OUT_HOME/"jet_branches_independent.json"
    output.write_text(json.dumps(result,indent=2,default=str,allow_nan=False)+"\n",encoding="utf-8")
    print(json.dumps({"output":str(output),"p2003_signs":signs2003,"p1009_signs":signs1009,
                      "p2003_endpoint":str(exact2003["endpoint"]),"p1009_endpoint":str(exact1009["endpoint"]),
                      "p2003_noninteger_parameters":exact2003["noninteger_parameter_count"],
                      "p1009_noninteger_parameters":exact1009["noninteger_parameter_count"],
                      "p2003_polynomial_denominator":exact2003["polynomial_minimum_common_denominator"],
                      "p1009_polynomial_denominator":exact1009["polynomial_minimum_common_denominator"],
                      "six_start_failure_counts":[item["failed_rows_float_recomputed"] for item in repairs["starts"]]},indent=2))


if __name__ == "__main__":
    main()
