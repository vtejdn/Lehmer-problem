"""Independent exact check of the J158 discriminant-action obstruction.

This imports only the reviewer-owned trace checker, never the author programs.
It verifies adjugates by their defining matrix identities and computes alpha**E
in (Z/mZ)[x]/(p), then reconstructs the entire multiplication matrix.
There is no word search, root computation or new lattice construction.
"""

import argparse
from math import prod
from pathlib import Path
import json

import independent_trace_lattice_review as trace_check


require = trace_check.require
GROUP = Path(__file__).resolve().parents[1]
OUTPUT_HOME = trace_check.OUTPUT_HOME


def residue_matrix(matrix, modulus):
    return [[entry % modulus for entry in row] for row in matrix]


def ring_power_left_to_right(polynomial, exponent, modulus):
    size = len(polynomial) - 1
    value = [1] + [0] * (size - 1)
    alpha = [0, 1] + [0] * (size - 2)
    for bit in bin(exponent)[2:]:
        value = [entry % modulus for entry in trace_check.ring_product(value, value, polynomial)]
        if bit == "1":
            value = [entry % modulus for entry in trace_check.ring_product(value, alpha, polynomial)]
    return value


def verify(input_path, trace_path, result_path):
    trace_report = trace_check.verify(input_path, trace_path)
    trace = json.loads(trace_path.read_text(encoding="utf-8"))
    result = json.loads(result_path.read_text(encoding="utf-8"))
    polynomial = trace_report["polynomial_ascending"]
    gram, companion = trace["trace_gram"], trace["companion"]
    size, positive_rank = 18, 16
    determinant = trace_report["gram_determinant"]
    modulus = abs(determinant)

    # Every allowed eigenvalue order has phi(n) <= 16. These are the largest
    # prime powers whose phi-value is <= 16; primes above 17 cannot occur.
    exponent_factors = {2: 32, 3: 9, 5: 5, 7: 7, 11: 11, 13: 13, 17: 17}
    primes = [p for p in range(2, 18) if all(p % q for q in range(2, p))]
    require(primes == list(exponent_factors), "complete allowed prime list")
    for prime, power in exponent_factors.items():
        require(power % prime == 0 and power - power // prime <= positive_rank,
                "allowed prime-power totient")
        require(prime * power - power > positive_rank, "next prime power is excluded")
        remaining = power
        while remaining % prime == 0:
            remaining //= prime
        require(remaining == 1, "factor really is a prime power")
    exponent = prod(exponent_factors.values())
    require(exponent == 24504480, "absolute rank-sixteen exponent")
    require(result["polynomial_ascending"] == polynomial, "same original polynomial")
    require(result["positive_rank"] == positive_rank, "same positive rank")
    require(result["finite_order_exponent"] == exponent, "reported exponent")
    require(result["gram_determinant"] == determinant and result["modulus"] == modulus,
            "verified determinant and positive modulus")

    adjugate = trace_check.integer_matrix(result["gram_adjugate"], size, "adjugate")
    target = [[determinant * x for x in row] for row in trace_check.eye(size)]
    require(trace_check.mm(gram, adjugate) == target, "every entry of GQ=dI")
    require(trace_check.mm(adjugate, gram) == target, "every entry of QG=dI")
    # Since det(G) is independently nonzero, these identities uniquely identify
    # every adjugate entry without reusing the author's rational inversion.
    power_element = ring_power_left_to_right(polynomial, exponent, modulus)
    power = residue_matrix(trace_check.multiplication_operator(power_element, polynomial), modulus)
    actual_power = trace_check.integer_matrix(result["companion_power_modulus"], size, "modular power")
    require(actual_power == power, "every entry of the independent quotient-algebra power")
    difference = [[power[i][j] - int(i == j) for j in range(size)] for i in range(size)]
    defect = residue_matrix(trace_check.mm(difference, adjugate), modulus)
    actual_defect = trace_check.integer_matrix(result["discriminant_defect"], size, "discriminant defect")
    require(actual_defect == defect, "every modular defect entry")
    witness = next(([i, j, defect[i][j]] for i in range(size) for j in range(size) if defect[i][j]), None)
    require(witness == result["nonzero_entry_witness"] == [0, 0, 2850856976087321421046],
            "actual first nonzero residue witness")
    require(0 < witness[2] < modulus, "strict nonzero residue")
    require(result["necessary_generator_condition"] is False, "necessary condition actually fails")

    # Check the discriminant-coordinate transfer using the already verified
    # integral basis, independently of the intrinsic argument in the review.
    split = trace["splitting"]
    basis, inverse = split["basis_columns_positive_then_e_f"], split["basis_inverse"]
    split_adjugate = trace_check.mm(inverse, trace_check.mm(adjugate, trace_check.tr(inverse)))
    require(trace_check.mm(split["split_gram"], split_adjugate) == target, "adjugate in split coordinates")
    split_power = residue_matrix(trace_check.mm(inverse, trace_check.mm(power, basis)), modulus)
    split_difference = [[split_power[i][j] - int(i == j) for j in range(size)] for i in range(size)]
    split_defect = residue_matrix(trace_check.mm(split_difference, split_adjugate), modulus)
    transferred_defect = residue_matrix(trace_check.mm(inverse, trace_check.mm(defect, trace_check.tr(inverse))), modulus)
    require(split_defect == transferred_defect, "complete discriminant defect basis transfer")
    require(any(entry for row in split_defect for entry in row), "obstruction remains in the displayed split basis")

    return {
        "result": "verified",
        "polynomial_ascending": polynomial,
        "positive_rank": positive_rank,
        "exponent_prime_power_factors": exponent_factors,
        "finite_order_exponent": exponent,
        "gram_determinant": determinant,
        "modulus": modulus,
        "power_element_ascending_modulus": power_element,
        "nonzero_entry_witness": witness,
        "necessary_generator_condition": False,
        "verified_matrix_fields": ["gram_adjugate", "companion_power_modulus", "discriminant_defect"],
        "complete_split_basis_transfer_verified": True,
        "arithmetic": "Python integers and fractions.Fraction; quotient-polynomial power; no author-code import",
        "scope": "This fixed lattice and its permitted-generator necessary condition at arbitrary finite word length; no word search, other invariant lattice, power substitution or Mahler-gap theorem."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=trace_check.DEFAULT_INPUT)
    parser.add_argument("--trace", type=Path, default=OUTPUT_HOME / "trace_lattice.json")
    parser.add_argument("--result", type=Path, default=OUTPUT_HOME / "discriminant_action.json")
    parser.add_argument("--output", type=Path, default=OUTPUT_HOME / "independent_discriminant_review.json")
    args = parser.parse_args()
    require(args.output.resolve() not in {args.input.resolve(), args.trace.resolve(), args.result.resolve(),
                                          Path(__file__).resolve(), Path(trace_check.__file__).resolve()},
            "review output must not overwrite a checked input or a checker")
    report = verify(args.input, args.trace, args.result)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
