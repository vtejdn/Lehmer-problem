"""Exact trace-root counts for the fixed central-minus-one N=1155 quotient.

The specified cyclotomic block is reused from L457 v2. Its exact division and
the complete reciprocal lift are checked afresh. Root counts do not require a
new assertion that this block exhausts the cyclotomic factors: any omitted
cyclotomic factors would have only unit-circle roots.

Sturm chains use exact rational Euclidean remainders, cleared only by positive
denominators and positive contents. Full multiplicities are restored through
a verified square-free decomposition. No numerical roots or Mahler estimates
are used. The two small fixed trace polynomials are arithmetic controls.
"""

import argparse
import json
import math
from pathlib import Path
import platform
import time

import flint
from flint import fmpq_poly, fmpz_poly


N = 1155
BLOCK = [(1, 2), (2, 2), (3, 1), (4, 1), (5, 1), (6, 1),
         (8, 1), (10, 1), (12, 1), (24, 1)]


def ints(poly):
    return [int(c) for c in poly.coeffs()]


def sign(value):
    return (value > 0) - (value < 0)


def primitive_positive_scale(poly):
    """Keep the sign; divide only by a positive coefficient gcd."""
    values = ints(poly)
    divisor = math.gcd(*values)
    assert divisor > 0
    return fmpz_poly([value // divisor for value in values])


def sturm_chain(poly):
    chain = [primitive_positive_scale(poly),
             primitive_positive_scale(poly.derivative())]
    while True:
        remainder = -(fmpq_poly(chain[-2]) % fmpq_poly(chain[-1]))
        if not remainder:
            break
        assert int(remainder.denom()) > 0
        chain.append(primitive_positive_scale(remainder.numer()))
    assert chain[-1].degree() == 0, "The supplied factor is not square-free"
    return chain


def variations(signs):
    nonzero = [s for s in signs if s]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def sign_vector(chain, point):
    if point == "-infinity":
        return [sign(int(p.leading_coefficient())) * (-1) ** int(p.degree())
                for p in chain]
    if point == "+infinity":
        return [sign(int(p.leading_coefficient())) for p in chain]
    return [sign(int(p(point))) for p in chain]


def shape(poly):
    assert poly.degree() > 0
    assert poly(-2) != 0 and poly(2) != 0
    content, factors = poly.factor_squarefree()
    rebuilt = fmpz_poly([content])
    factor_results = []
    totals = {"real_trace_roots": 0, "trace_roots_in_minus2_2": 0,
              "real_trace_roots_outside": 0, "nonreal_trace_roots": 0}
    previous = []
    for factor, multiplicity in factors:
        multiplicity = int(multiplicity)
        assert factor.gcd(factor.derivative()).degree() == 0
        assert all(factor.gcd(other).degree() == 0 for other in previous)
        previous.append(factor)
        rebuilt *= factor ** multiplicity
        chain = sturm_chain(factor)
        vectors = {str(point): sign_vector(chain, point)
                   for point in ("-infinity", -2, 2, "+infinity")}
        counts = {point: variations(values) for point, values in vectors.items()}
        real = counts["-infinity"] - counts["+infinity"]
        inside = counts["-2"] - counts["2"]
        nonreal = int(factor.degree()) - real
        assert 0 <= inside <= real <= factor.degree()
        assert nonreal % 2 == 0
        totals["real_trace_roots"] += multiplicity * real
        totals["trace_roots_in_minus2_2"] += multiplicity * inside
        totals["real_trace_roots_outside"] += multiplicity * (real - inside)
        totals["nonreal_trace_roots"] += multiplicity * nonreal
        factor_results.append({
            "coefficients_ascending": ints(factor),
            "multiplicity": multiplicity,
            "sturm_degrees": [int(p.degree()) for p in chain],
            "sturm_signs": vectors,
            "variations": counts,
        })
    assert rebuilt == poly
    degree = int(poly.degree())
    assert totals["real_trace_roots"] + totals["nonreal_trace_roots"] == degree
    exterior = totals["real_trace_roots_outside"] + totals["nonreal_trace_roots"]
    return {
        "trace_coefficients_ascending": ints(poly),
        "trace_degree": degree,
        "endpoint_values": [int(poly(-2)), int(poly(2))],
        "squarefree_components": factor_results,
        **totals,
        "complete_exterior_roots": exterior,
        "complete_interior_roots": exterior,
        "complete_unit_circle_roots": 2 * totals["trace_roots_in_minus2_2"],
    }


def trace_polynomial(poly):
    values = ints(poly)
    degree = int(poly.degree())
    assert degree % 2 == 0 and values == values[::-1]
    half = degree // 2
    variable = fmpz_poly([0, 1])
    trace = fmpz_poly([values[half]])
    previous, current = fmpz_poly([2]), variable
    for k in range(1, half + 1):
        trace += values[half + k] * current
        previous, current = current, variable * current - previous
    reconstructed = [0] * (degree + 1)
    for j, coefficient in enumerate(ints(trace)):
        for k in range(j + 1):
            reconstructed[half + j - 2 * k] += coefficient * math.comb(j, k)
    assert reconstructed == values
    assert trace.degree() == half and trace.leading_coefficient() == 1
    return trace


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[2] / "outputs" /
                        "Yin_J_G0138" / "core_shape.json")
    args = parser.parse_args()
    started = time.monotonic()
    t10 = fmpz_poly([-1, 5, 4, -5, -1, 1])
    t18 = fmpz_poly([1, 2, -13, -16, 19, 20, -8, -8, 1, 1])
    controls = {"degree10": shape(t10), "degree18": shape(t18)}
    assert controls["degree10"]["trace_roots_in_minus2_2"] == 3
    assert controls["degree18"]["trace_roots_in_minus2_2"] == 7
    assert all(c["complete_exterior_roots"] == 2 for c in controls.values())
    controls["degree10"]["trace_discriminant"] = int(t10.discriminant())
    assert controls["degree10"]["trace_discriminant"] == -18583
    for label, trace in (("degree10", t10), ("degree18", t18)):
        derivative_bound = sum(k * abs(int(trace[k])) * 2 ** (k - 1)
                               for k in range(1, int(trace.degree()) + 1))
        controls[label]["endpoint_derivative_bound"] = derivative_bound
    assert controls["degree10"]["endpoint_derivative_bound"] == 193
    assert controls["degree18"]["endpoint_derivative_bound"] == 10902
    assert 484 * 193 < 49 * 45 ** 2
    assert 484 * 10902 < 49 * 329 ** 2

    variable = fmpz_poly([0, 1])
    cyclotomic = fmpz_poly.cyclotomic(N)
    assert cyclotomic.degree() == 480
    numerator = cyclotomic - variable ** 240
    block = fmpz_poly([1])
    for order, multiplicity in BLOCK:
        block *= fmpz_poly.cyclotomic(order) ** multiplicity
    quotient, remainder = divmod(numerator, block)
    assert not remainder and quotient * block == numerator
    assert block.degree() == 34 and quotient.degree() == 446
    assert quotient[0] == 1 and quotient.leading_coefficient() == 1
    trace = trace_polynomial(quotient)
    result = shape(trace)
    output = {
        "python_version": platform.python_version(),
        "python_flint_version": flint.__version__,
        "arithmetic": "exact integer and rational Sturm chains",
        "N": N,
        "central_exponent": 240,
        "specified_cyclotomic_block": BLOCK,
        "original_coefficients_ascending": ints(numerator),
        "block_coefficients_ascending": ints(block),
        "quotient_coefficients_ascending": ints(quotient),
        "controls": controls,
        "result": result,
        "passes_necessary_exterior_count": result["complete_exterior_roots"] == 2,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "Only the fixed N=1155 quotient; no other N and no Mahler evaluation",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    temporary.replace(args.output)
    print(json.dumps({"N": N, "quotient_degree": int(quotient.degree()),
                      **{k: v for k, v in result.items()
                         if isinstance(v, int)},
                      "elapsed_seconds": output["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
