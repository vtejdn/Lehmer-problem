"""Reproducible finite probe of coupled, rotating integral symplectic shears.

NumPy supplies exploratory spectra. FLINT certifies every full root product.
Exact cyclotomic factorization resolves balls containing one.
No finite sample proves a gap for the unbounded family.
"""

import json
import random
from pathlib import Path

import numpy as np
from flint import arb, ctx, fmpz_mat
from sympy import Poly, Symbol


def shear_matrix(genus, sites, first_signs, second_signs):
    identity = np.eye(genus, dtype=np.int64)
    first = np.zeros((genus, genus), dtype=np.int64)
    second = np.zeros_like(first)
    for site, first_sign, second_sign in zip(sites, first_signs, second_signs):
        difference = identity[site] - identity[(site + 1) % genus]
        total = identity[site] + identity[(site + 1) % genus]
        first += first_sign * np.outer(difference, difference)
        second += second_sign * np.outer(total, total)
    rotation = np.roll(identity, 1, axis=0)
    return np.block([
        [rotation @ (identity + first @ second), rotation @ first],
        [rotation @ second, rotation],
    ])


def numerical_record(genus, count, sample):
    generator = random.Random(196830000 + 10000 * genus + 100 * count + sample)
    sites = sorted(generator.sample(range(genus), count))
    first_signs = [1] * (count // 2) + [-1] * (count // 2)
    second_signs = list(first_signs)
    generator.shuffle(first_signs)
    generator.shuffle(second_signs)
    matrix = shear_matrix(genus, sites, first_signs, second_signs)
    roots = np.linalg.eigvals(matrix.astype(float))
    radii = np.abs(roots)
    return {
        "genus": genus,
        "site_count": count,
        "sample": sample,
        "sites": sites,
        "first_signs": first_signs,
        "second_signs": second_signs,
        "log_measure_float": float(np.log(np.maximum(1, radii)).sum()),
        "house_float": float(radii.max()),
        "expanding_count_float": int((radii > 1 + 1e-7).sum()),
    }


def certify(record):
    matrix = shear_matrix(record["genus"], record["sites"], record["first_signs"], record["second_signs"])
    genus = record["genus"]
    identity = np.eye(genus, dtype=np.int64)
    zero = np.zeros_like(identity)
    form = np.block([[zero, identity], [-identity, zero]])
    assert np.array_equal(matrix.T @ form @ matrix, form)
    polynomial = fmpz_mat(matrix.tolist()).charpoly()
    coefficients = [int(value) for value in polynomial]
    assert coefficients == coefficients[::-1]
    ctx.prec = 256
    measure = arb(1)
    root_count = 0
    for root, multiplicity in polynomial.complex_roots():
        radius = abs(root)
        # max(1, r) is monotone, so clipping both certified endpoints encloses it.
        lower = max(arb(1), radius.lower())
        upper = max(arb(1), radius.upper())
        clipped = arb((lower + upper) / 2, (upper - lower) / 2)
        measure *= clipped**multiplicity
        root_count += multiplicity
    assert root_count == 2 * genus
    assert measure.rad() < arb("1e-30")
    cyclotomic = False
    if not measure > 1:
        variable = Symbol("t")
        exact = Poly.from_list(coefficients[::-1], variable)
        content, factors = exact.factor_list()
        assert content == 1 and all(factor.is_cyclotomic for factor, _ in factors)
        cyclotomic = True
    return {"input": record, "coefficients_ascending": coefficients,
            "root_count": root_count, "measure_ball": str(measure),
            "log_measure_ball": str(measure.log()), "cyclotomic": cyclotomic}


def main():
    records = [numerical_record(genus, count, sample)
               for genus in (12, 24, 48)
               for count in (2, 4, 8)
               for sample in range(8)]
    summaries = []
    for genus in (12, 24, 48):
        for count in (2, 4, 8):
            selected = [item for item in records if item["genus"] == genus and item["site_count"] == count]
            summaries.append({"genus": genus, "site_count": count,
                              "min_log_measure_float": min(item["log_measure_float"] for item in selected),
                              "max_log_measure_float": max(item["log_measure_float"] for item in selected)})
    certificates = [certify(record) for record in records]
    positive = [item for item in certificates if not item["cyclotomic"]]
    best = min(positive, key=lambda item: item["input"]["log_measure_float"])
    best_upper = arb(best["measure_ball"]).upper()
    assert all(item is best or arb(item["measure_ball"]).lower() > best_upper
               or item["coefficients_ascending"] == best["coefficients_ascending"]
               for item in positive)
    output = Path(__file__).resolve().parents[2] / "outputs" / "Yin_J_G0153" / "rotating_shears.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"summaries": summaries, "records": records,
                                  "certificates": certificates}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"summaries": summaries, "cyclotomic_count": len(records) - len(positive),
                      "positive_count": len(positive), "smallest_positive": best}, indent=2))


if __name__ == "__main__":
    main()
