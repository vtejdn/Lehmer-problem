"""Complete factor measures for three fixed original rotating-shear inputs.

These are the three labels in the original 72-input factor inventory having
two reciprocal noncyclotomic irreducible factors. Regenerate the original
seeded sites and signs, the exact integer matrix and its full characteristic
polynomial. No previous generated output is required and no new labels are
sampled. The J156 evaluator certifies all roots of every positive factor.
"""

import importlib.util
import json
from pathlib import Path
import platform
import random

import flint
from flint import fmpz_mat


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name / "reciprocal_factor_measures.json"
EVALUATOR = HERE.parent / "Yin_J_G0156" / "sampler.py"
LABELS = ((12, 8, 3), (48, 8, 2), (48, 8, 6))
EXPECTED_DEGREES = ((8, 12), (40, 40), (40, 40))


def exact_input(genus, site_count, sample):
    seed = 196830000 + 10000*genus + 100*site_count + sample
    generator = random.Random(seed)
    sites = sorted(generator.sample(range(genus), site_count))
    epsilon = [1]*(site_count//2) + [-1]*(site_count//2)
    eta = list(epsilon)
    generator.shuffle(epsilon)
    generator.shuffle(eta)
    assert sum(epsilon) == sum(eta) == 0
    d, e = fmpz_mat(genus, genus), fmpz_mat(genus, genus)
    for site, first_sign, second_sign in zip(sites, epsilon, eta, strict=True):
        following = (site+1) % genus
        for row, first_value, second_value in ((site, 1, 1), (following, -1, 1)):
            for column, first_other, second_other in ((site, 1, 1), (following, -1, 1)):
                d[row, column] += first_sign * first_value * first_other
                e[row, column] += second_sign * second_value * second_other
    assert d.transpose() == d and e.transpose() == e
    de = d*e
    matrix = fmpz_mat(2*genus, 2*genus)
    for row in range(genus):
        source = (row-1) % genus
        for column in range(genus):
            unit = int(source == column)
            matrix[row, column] = de[source, column] + unit
            matrix[row, genus+column] = d[source, column]
            matrix[genus+row, column] = e[source, column]
            matrix[genus+row, genus+column] = unit
    coefficients = list(map(int, matrix.charpoly()))
    assert len(coefficients) == 2*genus+1
    assert coefficients == coefficients[::-1]
    assert coefficients[0] == coefficients[-1] == 1
    return {"genus": genus, "site_count": site_count, "sample": sample,
            "seed": seed, "sites": sites, "first_signs": epsilon,
            "second_signs": eta}, coefficients


def main():
    specification = importlib.util.spec_from_file_location("j156_factor_measure", EVALUATOR)
    evaluator = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(evaluator)
    records = []
    for label, expected_degrees in zip(LABELS, EXPECTED_DEGREES, strict=True):
        original_input, coefficients = exact_input(*label)
        certificate = evaluator.certify_polynomial(coefficients)
        assert certificate["root_count_with_multiplicity"] == 2*label[0]
        positive_factors = [row for row in certificate["factors"] if not row["cyclotomic"]]
        assert sorted(row["degree"] for row in positive_factors) == list(expected_degrees)
        for row in positive_factors:
            assert row["exponent"] == 1
            assert row["coefficients_ascending"] == row["coefficients_ascending"][::-1]
            assert row["root_count"] == row["degree"]
        records.append({"label": list(label), "input": original_input,
                        "certificate": certificate})
    result = {"python_version": platform.python_version(),
              "python_flint_version": flint.__version__,
              "scope": "Six reciprocal factors of three fixed original labels; no new sampling or family exclusion.",
              "records": records}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    temporary.replace(OUTPUT)
    summary = [{"label": row["label"],
                "parent_measure": row["certificate"]["measure_ball"],
                "positive_factors": [
                    {"degree": factor["degree"], "measure": factor["measure_ball"],
                     "threshold_6_5": factor["thresholds"]["6/5"]}
                    for factor in row["certificate"]["factors"] if not factor["cyclotomic"]]}
               for row in records]
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
