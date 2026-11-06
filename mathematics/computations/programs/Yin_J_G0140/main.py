"""Exact finite factorizations and uncertified full root measures for A_N.

A_N = P_L(z)*(z**(2*N)+1) + z**(N+5), with the fixed Lehmer polynomial P_L.
The positive factor count is internal to each A_N and includes multiplicities.
No degree normalization or count of new factors across N is used.
"""

import argparse
import json
import math
from pathlib import Path
import platform

import numpy as np
import sympy as sp


SMALL_INPUTS = (1, 2, 3, 4, 5, 6, 10, 12, 15)
REMAINING_INPUTS = (20, 24, 30)
LEHMER_ASCENDING = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1)


def ascending_coefficients(polynomial):
    return [int(polynomial.nth(k)) for k in range(polynomial.degree() + 1)]


def root_measure(polynomial):
    roots = np.roots([float(c) for c in polynomial.all_coeffs()])
    # Every computed root contributes log(max(1, |root|)); the exterior count
    # threshold below is only a separate numerical screen, not a measure cutoff.
    return {
        "approximate_total_log_measure": math.fsum(
            math.log(max(1.0, abs(root))) for root in roots
        ),
        "root_count": len(roots),
        "roots_real_imaginary": [[float(root.real), float(root.imag)] for root in roots],
        "exterior_count_at_modulus_threshold_1_plus_1e_minus7": sum(
            bool(abs(root) > 1 + 1e-7) for root in roots
        ),
    }


def exact_input(n):
    z = sp.symbols("z")
    lehmer = sp.Poly.from_list(LEHMER_ASCENDING[::-1], z, domain=sp.ZZ)
    polynomial = lehmer * sp.Poly(z ** (2 * n) + 1, z, domain=sp.ZZ)
    polynomial += sp.Poly(z ** (n + 5), z, domain=sp.ZZ)
    assert polynomial.LC() == 1 and polynomial.TC() == 1
    assert polynomial.degree() == 2 * n + 10
    return polynomial


def factor_and_measure(polynomial):
    z = polynomial.gens[0]
    content, factors = sp.factor_list(polynomial)
    assert content == 1
    reconstructed = sp.Poly(1, z, domain=sp.ZZ)
    records = []
    cyclotomic_degree = 0
    positive_degree = 0
    positive_count = 0
    weighted_positive_measures = []
    positive_measures = []
    weighted_raw_measures = []
    for index, (factor, multiplicity) in enumerate(factors):
        assert factor.degree() > 0 and factor.LC() == 1
        assert abs(int(factor.TC())) == 1
        reconstructed *= factor ** multiplicity
        cyclotomic = bool(factor.is_cyclotomic)
        numerical = root_measure(factor)
        weighted_raw_measures.append(
            multiplicity * numerical["approximate_total_log_measure"]
        )
        if cyclotomic:
            cyclotomic_degree += multiplicity * factor.degree()
        else:
            positive_count += multiplicity
            positive_degree += multiplicity * factor.degree()
            positive_measures.append(numerical["approximate_total_log_measure"])
            weighted_positive_measures.append(
                multiplicity * numerical["approximate_total_log_measure"]
            )
        records.append({
            "factor_index": index,
            "coefficients_ascending": ascending_coefficients(factor),
            "degree": factor.degree(),
            "multiplicity": multiplicity,
            "is_cyclotomic": cyclotomic,
            "positive_measure_by_irreducibility_and_kronecker": not cyclotomic,
            "uncertified_roots": numerical,
        })
    assert reconstructed == polynomial
    assert cyclotomic_degree + positive_degree == polynomial.degree()
    return {
        "factorization_status": "complete_over_Z",
        "factorization_content": int(content),
        "exact_product_reconstructs_input": True,
        "factors": records,
        "cyclotomic_degree_with_multiplicity": cyclotomic_degree,
        "positive_degree_with_multiplicity": positive_degree,
        "r_plus_with_multiplicity": positive_count,
        "approximate_total_log_measure_from_positive_factors": math.fsum(
            weighted_positive_measures
        ),
        "approximate_raw_root_sum_including_cyclotomic_roundoff": math.fsum(
            weighted_raw_measures
        ),
        "approximate_minimum_positive_factor_log_measure": min(positive_measures)
        if positive_measures else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("small", "remaining", "all"), default="all")
    arguments = parser.parse_args()
    inputs = {
        "small": SMALL_INPUTS,
        "remaining": REMAINING_INPUTS,
        "all": SMALL_INPUTS + REMAINING_INPUTS,
    }[arguments.phase]
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name / f"{arguments.phase}_results.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "scope": {
            "N_values": inputs,
            "lehmer_coefficients_ascending": LEHMER_ASCENDING,
            "formula": "A_N=P_L(z)*(z^(2*N)+1)+z^(N+5)",
            "factorization_domain": "ZZ",
            "r_plus_counts_multiplicities_within_each_input": True,
        },
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "sympy": sp.__version__,
        },
        "limits": (
            "SymPy integer factorization and coefficient reconstruction are exact. "
            "Every noncyclotomic irreducible monic unit factor has positive measure "
            "by Kronecker. All numerical roots and log measures use double precision "
            "without certified error bounds. The total and factor measures are not "
            "divided by degree. No asymptotic factor-count growth is inferred."
        ),
        "status": "in_progress",
        "inputs": [],
    }

    def save():
        output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    save()
    for n in inputs:
        polynomial = exact_input(n)
        record = {
            "N": n,
            "degree": polynomial.degree(),
            "coefficients_ascending": ascending_coefficients(polynomial),
            "factorization_status": "not_completed",
        }
        payload["inputs"].append(record)
        save()
        print(f"factoring N={n}, degree={polynomial.degree()}", flush=True)
        try:
            record.update(factor_and_measure(polynomial))
        except (KeyboardInterrupt, Exception) as error:
            record["failure_type"] = type(error).__name__
            payload["status"] = "partial"
            save()
            raise
        save()
        print({
            "N": n,
            "cyclotomic_degree": record["cyclotomic_degree_with_multiplicity"],
            "r_plus": record["r_plus_with_multiplicity"],
            "positive_degrees_and_multiplicities": [
                (factor["degree"], factor["multiplicity"])
                for factor in record["factors"] if not factor["is_cyclotomic"]
            ],
            "m_total_approx": record["approximate_total_log_measure_from_positive_factors"],
            "min_positive_m_approx": record["approximate_minimum_positive_factor_log_measure"],
        }, flush=True)
    payload["status"] = "complete"
    save()
    print(output.relative_to(group.parents[3]), flush=True)


if __name__ == "__main__":
    main()
