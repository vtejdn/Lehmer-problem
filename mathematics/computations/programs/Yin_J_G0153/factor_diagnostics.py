"""Exact factor diagnostics for the original 72 rotating-shear labels.

Use rotating_shears.json when present; otherwise regenerate the same labelled
matrices and exact characteristic polynomials.  --recompute forces regeneration.
No floating root modulus is used to classify a factor or a positive measure.
"""

import argparse
import json
from pathlib import Path

from flint import fmpz_mat
from sympy import Poly, Symbol

from rotating_shears import numerical_record, shear_matrix


LABELS = [(g, k, s) for g in (12, 24, 48)
          for k in (2, 4, 8) for s in range(8)]


def label(record):
    return tuple(record[key] for key in ("genus", "site_count", "sample"))


def exact_inputs(recompute):
    output_dir = Path(__file__).resolve().parents[2] / "outputs" / "Yin_J_G0153"
    retained = output_dir / "rotating_shears.json"
    if retained.exists() and not recompute:
        certificates = json.loads(retained.read_text(encoding="utf-8"))["certificates"]
        assert sorted(label(item["input"]) for item in certificates) == LABELS
        for item in certificates:
            regenerated = numerical_record(*label(item["input"]))
            for key in ("sites", "first_signs", "second_signs"):
                assert item["input"][key] == regenerated[key]
        return certificates, "rotating_shears.json", output_dir

    certificates = []
    for g, k, s in LABELS:
        record = numerical_record(g, k, s)
        matrix = shear_matrix(g, record["sites"], record["first_signs"], record["second_signs"])
        coefficients = [int(value) for value in fmpz_mat(matrix.tolist()).charpoly()]
        certificates.append({"input": record, "coefficients_ascending": coefficients})
    return certificates, "original generator and exact FLINT charpoly", output_dir


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recompute", action="store_true")
    args = parser.parse_args()
    certificates, source, output_dir = exact_inputs(args.recompute)
    variable = Symbol("t")
    diagnostics = []
    polynomials = {}
    for item in certificates:
        coefficients = item["coefficients_ascending"]
        assert coefficients == coefficients[::-1] and coefficients[0] == 1
        polynomial = Poly.from_list(coefficients[::-1], variable)
        assert polynomial.degree() == 2 * item["input"]["genus"]
        content, factors = polynomial.factor_list()
        assert content == 1
        rebuilt = Poly(1, variable)
        descriptions = []
        for factor, multiplicity in factors:
            rebuilt *= factor ** multiplicity
            descending = [int(value) for value in factor.all_coeffs()]
            reciprocal = (descending == descending[::-1]
                          or descending == [-value for value in descending[::-1]])
            descriptions.append({
                "degree": factor.degree(), "multiplicity": multiplicity,
                "coefficients_ascending": descending[::-1],
                "cyclotomic": bool(factor.is_cyclotomic), "reciprocal": reciprocal,
            })
        assert rebuilt == polynomial
        noncyclotomic = [factor for factor in descriptions if not factor["cyclotomic"]]
        diagnostics.append({"label": label(item["input"]), "factors": descriptions,
                            "positive_measure": bool(noncyclotomic),
                            "has_nonreciprocal_noncyclotomic_factor":
                                any(not factor["reciprocal"] for factor in noncyclotomic)})
        polynomials[label(item["input"])] = polynomial

    positive = [item for item in diagnostics if item["positive_measure"]]
    split = [item for item in positive if item["has_nonreciprocal_noncyclotomic_factor"]]
    reciprocal_only = [item for item in positive if not item["has_nonreciprocal_noncyclotomic_factor"]]
    assert (len(positive), len(split), len(reciprocal_only)) == (48, 8, 40)

    minimum_label = (12, 8, 6)
    expected = ((variable - 1)**2 * (variable + 1)**2
                * (variable**2 - variable + 1) * (variable**2 + variable + 1)
                * (variable**2 + 1)**2 * (variable**6 - variable**2 - 1)
                * (variable**6 + variable**4 - 1))
    assert polynomials[minimum_label] == Poly(expected, variable)

    core_examples = []
    for g, k, s, degree in ((12, 2, 2, 20), (24, 2, 0, 44),
                          (24, 2, 7, 44), (48, 2, 1, 92)):
        item = next(item for item in diagnostics if item["label"] == (g, k, s))
        core = [factor for factor in item["factors"] if not factor["cyclotomic"]]
        assert len(core) == 1
        assert (core[0]["degree"], core[0]["multiplicity"], core[0]["reciprocal"]) == (degree, 1, True)
        core_examples.append({"label": (g, k, s), "irreducible_reciprocal_degree": degree})

    summary = {"input_source": source, "label_count": len(diagnostics),
               "positive_count": len(positive),
               "nonreciprocal_factor_count": len(split),
               "reciprocal_only_positive_count": len(reciprocal_only),
               "nonreciprocal_labels": [item["label"] for item in split],
               "minimum_factorization_label": minimum_label,
               "irreducible_reciprocal_core_examples": core_examples}
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "factor_diagnostics.json").write_text(
        json.dumps({"summary": summary, "diagnostics": diagnostics}, indent=2) + "\n",
        encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
