"""Validated damped-root cyclotomic tails, with exact input checks.

The analytic reduction and scope are in D G0015. Ball strings retain radii.
Exact rational resultants are recomputed from retained integer inputs; the
potentially very large fractions need not be copied into the output.
"""

from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import math

import flint
from flint import arb, acb, fmpq, fmpq_poly, fmpz_poly, ctx
import sympy as sp


HERE = _J_OUTPUT
PRECISION = 280
ROOT_BITS = 240
N = 2
ORDERS = (1, 2, 3, 4, 6)
LIFTS = (1, 2, 3, 41, 101, 1009)
SIGNS = (1, -1)
SEEDS = {
    "lehmer10": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
    "salem18": [1, -1, 1, -1, 0, 0, -1, 1, -1, 1,
                -1, 1, -1, 0, 0, -1, 1, -1, 1],
    "salem14a": [1, 0, 0, -1, -1, 0, 0, 1, 0, 0, -1, -1, 0, 0, 1],
    "salem14b": [1, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 1],
    "salem10b": [1, 0, 0, 0, -1, -1, -1, 0, 0, 0, 1],
    "quartic_control": [1, -1, -1, -1, 1],
}


def rational(value):
    value = sp.Rational(value)
    return fmpq(int(value.p), int(value.q))


def root_ball(lo, hi):
    # Both endpoints are exact rationals enclosing the isolated real root.
    return arb(rational((lo + hi) / 2), rational((hi - lo) / 2))


def poly_eval(coefficients, value):
    out = value * 0
    for coefficient in reversed(coefficients):
        out = out * value + coefficient
    return out


def powersums(coefficients, upto):
    degree = len(coefficients) - 1
    out = [degree]
    for n in range(1, upto + 1):
        if n <= degree:
            value = -n * coefficients[degree - n]
            value -= sum(coefficients[degree - j] * out[n-j]
                         for j in range(1, n))
        else:
            value = -sum(coefficients[degree - j] * out[n-j]
                         for j in range(1, degree + 1))
        out.append(value)
    return out


def ramanujan(order, n):
    # Exact divisor expression, no trigonometric approximation.
    return sum(int(k * sp.mobius(order // k))
               for k in sp.divisors(math.gcd(order, n)))


def inspect_seed(coefficients):
    degree = len(coefficients) - 1
    assert degree % 2 == 0 and coefficients == coefficients[::-1]
    assert coefficients[0] == coefficients[-1] == 1
    _, factors = fmpz_poly(coefficients).factor()
    assert len(factors) == 1 and factors[0][1] == 1
    x, y = sp.symbols("x y")
    half = degree // 2
    cheb = [sp.Integer(2), y]
    for j in range(2, half + 1):
        cheb.append(sp.expand(y * cheb[-1] - cheb[-2]))
    trace = sp.Poly(coefficients[half] + sum(
        coefficients[half+j] * cheb[j] for j in range(1, half+1)), y)
    px = sum(c*x**i for i, c in enumerate(coefficients))
    assert sp.expand(x**half * trace.as_expr().subs(y, x+1/x)-px) == 0
    brackets = trace.intervals(eps=sp.Rational(1, 2**ROOT_BITS))
    assert len(brackets) == half and all(mult == 1 for _, mult in brackets)
    unit, exterior = [], []
    for (lo, hi), _ in brackets:
        if lo > 2:
            exterior.append((lo, hi))
        else:
            assert -2 < lo <= hi < 2
            unit.append(root_ball(lo, hi))
    assert len(exterior) == 1
    ybox = root_ball(*exterior[0])
    alpha = (ybox + (ybox*ybox-4).sqrt()) / 2
    assert alpha > 1
    return alpha, unit, {
        "irreducible_over_Q": True,
        "trace_polynomial_ascending": [int(c) for c in reversed(trace.all_coeffs())],
        "trace_root_intervals": [[str(lo), str(hi)] for (lo, hi), _ in brackets],
        "salem_configuration_checked": True,
        "alpha": alpha.str(40),
        "total_log_mahler": alpha.log().str(40),
    }


def full_sum(coefficients, alpha, sign, lift, order):
    degree = (len(coefficients) - 1) * lift
    t_exact = fmpq(degree-1, degree)
    u_exact = t_exact**lift
    reduced = order // math.gcd(order, lift)
    mult = int(sp.totient(order) // sp.totient(reduced))
    x = sp.symbols("x")
    phi = [int(c) for c in reversed(sp.Poly(sp.cyclotomic_poly(reduced, x), x).all_coeffs())]
    scaled = fmpq_poly([c * (sign*u_exact)**i for i, c in enumerate(coefficients)])
    # Product P(sign*u*zeta) over primitive roots, exactly over Q.
    exact_product = fmpq_poly(phi).resultant(scaled)
    assert exact_product != 0
    u = arb(u_exact)
    top = poly_eval(phi, sign*u/alpha)
    bottom = poly_eval(phi, sign*u*alpha)
    assert not top.contains(0) and not bottom.contains(0)
    answer = -mult * (abs(arb(exact_product)).log()
                      + abs(top).log() - abs(bottom).log())
    return answer, {
        "reduced_order": reduced,
        "primitive_multiplicity": mult,
        "exact_scaled_resultant_nonzero": True,
        "exact_resultant_numerator_bits": abs(int(exact_product.p)).bit_length(),
        "exact_resultant_denominator_bits": int(exact_product.q).bit_length(),
    }


def root_product_sum(alpha, unit_trace, sign, lift, order, degree):
    """Separate interval formula: no P-evaluation or resultant quotient."""
    t = arb(fmpq(degree-1, degree))
    answer = arb(0)
    for j in range(1, order+1):
        if math.gcd(j, order) != 1:
            continue
        zeta = acb(fmpq(2*j, order)).exp_pi_i()
        w = (t*zeta)**lift
        value = (1-sign*w/alpha)**2
        for beta in unit_trace:
            value *= 1-sign*beta*w+w*w
        assert not abs(value).contains(0)
        answer -= abs(value).log()
    return answer


def damped_mode(sums, alpha, sign, lift, n):
    if n % lift:
        return arb(0), 0
    k = n // lift
    exact = lift * sign**k * sums[k]
    correction = lift * sign**k * (alpha**k-alpha**(-k))
    return exact-correction, exact


def bound_string(value):
    assert value.is_finite()
    # A coarse decimal rational interval is a readable certificate in addition
    # to the ball. Its containment is explicitly checked before it is saved.
    denominator = 10**8
    midpoint = float(value.mid())
    lo = math.floor(midpoint*denominator)-1
    hi = math.ceil(midpoint*denominator)+1
    assert value >= arb(fmpq(lo, denominator))
    assert value <= arb(fmpq(hi, denominator))
    return {"ball": value.str(40), "lower": f"{lo}/{denominator}",
            "upper": f"{hi}/{denominator}"}


def main():
    ctx.prec = PRECISION
    rows, seed_checks = [], {}
    representation_checks = 0
    for name, coefficients in SEEDS.items():
        alpha, unit_trace, checks = inspect_seed(coefficients)
        seed_checks[name] = checks
        sums = powersums(coefficients, N)
        for sign in SIGNS:
            for lift in LIFTS:
                degree = (len(coefficients)-1)*lift
                t = arb(fmpq(degree-1, degree))
                h = alpha.log()-degree*t.log()/2
                modes = [damped_mode(sums, alpha, sign, lift, n)
                         for n in range(1, N+1)]
                for order in ORDERS:
                    actual, exact_info = full_sum(coefficients, alpha, sign, lift, order)
                    low = sum(t**n*ramanujan(order, n)*modes[n-1][0]/n
                              for n in range(1, N+1))
                    tail = actual-low
                    # These are required arithmetic inequalities, not empirical targets.
                    slack = int(sp.totient(order))*h-actual
                    assert slack >= 0
                    root_check = lift <= 3
                    if root_check:
                        by_roots = root_product_sum(alpha, unit_trace, sign, lift, order, degree)
                        assert actual.overlaps(by_roots), (name, sign, lift, order)
                        representation_checks += 1
                    rows.append({
                        "seed": name, "sign": sign, "lift": lift,
                        "degree": degree, "order": order, "cutoff_N": N,
                        "t": f"{degree-1}/{degree}",
                        "integer_powersums": [s for _, s in modes],
                        "damped_modes": [bound_string(b) for b, _ in modes],
                        "full_sum": bound_string(actual),
                        "low_part": bound_string(low),
                        "tail": bound_string(tail),
                        "tail_over_sqrt_degree": bound_string(tail/arb(degree).sqrt()),
                        "smoothing_H": bound_string(h),
                        "norm_inequality_slack": bound_string(slack),
                        "separate_root_factor_check": root_check,
                        **exact_info,
                    })
    output = {
        "working_precision_bits": PRECISION,
        "root_isolation_bits": ROOT_BITS, "coefficient_order": "ascending",
        "seeds": SEEDS, "seed_checks": seed_checks, "orders": ORDERS,
        "lifts": LIFTS, "signs": SIGNS, "cutoff_N": N,
        "row_count": len(rows), "root_factor_cross_check_count": representation_checks,
        "scope": "Validated finite tails. Seed irreducibility and Salem root pattern checked exactly. Lift irreducibility is not checked here; all lifts have fixed total log Mahler measure, not a sequence tending to zero.",
        "rows": rows,
    }
    destination = HERE / "results.json"
    destination.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(f"Certified {len(rows)} signed tails; {representation_checks} root-factor checks.")
    for name in SEEDS:
        selected = [r for r in rows if r["seed"] == name and r["sign"] == 1 and r["lift"] == 1]
        print(name, "m=", seed_checks[name]["total_log_mahler"],
              "tails=", [round(float(arb(r["tail"]["ball"]).mid()), 6) for r in selected])


if __name__ == "__main__":
    main()
