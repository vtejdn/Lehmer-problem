"""Verify the retained rational real-cell witness without an optimizer."""

from fractions import Fraction
import json
from pathlib import Path

from prefix_cell import interval_check, save


def main():
    path = Path(__file__).resolve().parent / "inputs" / "real_p2003_coefficients.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert (data["p"], data["n"], data["x"], data["kappa"], data["prefix_L"]) == (2003, 1001, 0, 1, 140)
    coefficients = [Fraction(value) for value in data["coefficients_rational"]]
    assert len(coefficients) == data["n"]
    assert coefficients[:139] == [2 if i == 0 else 4 if i % 2 == 0 else 0 for i in range(139)]
    result = interval_check(coefficients, data["kappa"])
    assert result["endpoint_positive"] and result["all_strict_signs_certified"]
    result["p"], result["n"], result["prefix_L"] = data["p"], data["n"], data["prefix_L"]
    result["scope"] = "exact rational real input; no integer completion or counterexample"
    out = save(result, "real_p2003_verification.json")
    print(json.dumps({"prefix_verified": True, "strict_signs_verified": True,
                      "endpoint": result["endpoint"], "output": str(out)}))


if __name__ == "__main__":
    main()
