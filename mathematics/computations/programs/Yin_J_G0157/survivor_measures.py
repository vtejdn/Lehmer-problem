"""Complete measures of the two C884v3 sign-and-endpoint survivors."""

from fractions import Fraction
import json
from pathlib import Path
import sys

from flint import fmpz_poly

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "Yin_J_G0156"))
import sampler


def original_lift(r, s, length, amplitude):
    p, m = r + s, r // 2
    n = (p - 1) // 2
    # (1+z^2)^2 ((1-z^r)/(1-z^2)) ((1-z^s)/(1-z)).
    even_sum = fmpz_poly([int(i % 2 == 0) for i in range(r - 1)])
    neutral = fmpz_poly([1, 0, 1]) ** 2 * even_sum * fmpz_poly([1] * s)
    coefficients = list(map(int, neutral))
    assert len(coefficients) == 2 * n + 3 and m >= 2
    # E_k(z+z^-1)=sum_{j=0}^k z^(k-2j); B_k=E_k+E_(k-1).
    k = n - length - 1
    assert k >= 0
    for order in (k, k - 1):
        for j in range(order + 1):
            exponent = order - 2 * j
            for shift in (-1, 1):
                coefficients[n + 1 + exponent + shift] -= amplitude
    assert coefficients == coefficients[::-1] and coefficients[0] == 1
    return coefficients


def main():
    rows = []
    for p, r, s, length, amplitude, lower_numerator in (
        (9, 4, 5, 3, 3, 2853749309), (11, 4, 7, 3, 3, 2759883858)):
        coefficients = original_lift(r, s, length, amplitude)
        checks = []
        for precision in (128, 256):
            sampler.PRECISION_BITS = precision
            certificate = sampler.certify_polynomial(coefficients)
            lower, upper = map(sampler.interval_fraction, certificate["measure_interval"])
            assert Fraction(lower_numerator, 10**9) < lower <= upper < Fraction(lower_numerator + 1, 10**9)
            assert all(status == "above" for status in certificate["thresholds"].values())
            assert fmpz_poly(coefficients)(-1) == 2
            checks.append(certificate)
        assert sampler.intervals_overlap(checks[0]["measure_interval"], checks[1]["measure_interval"])
        assert checks[0]["core_coefficients_ascending"] == checks[1]["core_coefficients_ascending"]
        rows.append({"p": p, "r": r, "s": s, "L": length, "amplitude": amplitude,
                     "coefficients_ascending": coefficients, "P_at_minus_one": 2,
                     "rational_measure_interval": [str(Fraction(lower_numerator, 10**9)),
                                                   str(Fraction(lower_numerator + 1, 10**9))],
                     "certificates": checks})
    output = HERE.parent.parent / "outputs" / HERE.name / "survivor_measures.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"scope": "Both exact C884v3 survivors; whole measures with every multiplicity.",
                                 "results": rows}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([{"p": row["p"], "coefficients_ascending": row["coefficients_ascending"],
                       "measure_interval": row["rational_measure_interval"]} for row in rows]))


if __name__ == "__main__":
    main()
