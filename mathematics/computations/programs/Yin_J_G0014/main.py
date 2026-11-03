"""Exact composition-resultant diagnostics; no root numerics or gap claim."""

from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json
import math

import flint
import sympy as sp


ROOT = _J_OUTPUT
SEEDS = {
    "lehmer": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
    "quartic_salem": [1, -1, -1, -1, 1],
    "quadratic_unit": [1, -3, 1],
}
QS = (1, 2, 3, 5, 7, 41)
PS = (2, 3)


def substitute(coefficients, power):
    out = [0] * ((len(coefficients) - 1) * power + 1)
    for i, coefficient in enumerate(coefficients):
        out[i * power] = coefficient
    return out


def direct_resultant(coefficients, power):
    f = flint.fmpz_poly(coefficients)
    fp = flint.fmpz_poly(substitute(coefficients, power))
    # Absolute Res(F(t),F(t^p)) equals the full powered resultant.
    return abs(int(f.resultant(fp)))


def powered_polynomial_check(coefficients, power):
    # A second representation forms every powered root with multiplicity.
    x, y = sp.symbols("x y")
    fy = sum(c * y**i for i, c in enumerate(coefficients))
    fx = fy.subs(y, x)
    powered = sp.resultant(fy, x - y**power, y)
    return abs(int(sp.resultant(fx, powered, x)))


def main():
    rows = []
    cross_checks = 0
    for name, seed in SEEDS.items():
        base_degree = len(seed) - 1
        for p in PS:
            base = direct_resultant(seed, p)
            assert base > 0
            for q in QS:
                coefficients = substitute(seed, q)
                degree = base_degree * q
                actual = direct_resultant(coefficients, p)
                expected = base**q
                assert actual == expected, (name, p, q, actual, expected)
                assert actual % (p**degree) == 0
                cross = None
                if q <= 3:
                    cross = powered_polynomial_check(coefficients, p)
                    assert cross == actual, (name, p, q, cross, actual)
                    cross_checks += 1
                rows.append({
                    "seed": name,
                    "p": p,
                    "q": q,
                    "degree": degree,
                    "gcd_p_q": math.gcd(p, q),
                    "absolute_resultant": str(actual),
                    "base_absolute_resultant": str(base),
                    "composition_identity_passed": True,
                    "frobenius_floor_quotient": str(actual // p**degree),
                    "second_representation_checked": cross is not None,
                })
    result = {
        "coefficient_order": "ascending",
        "seeds": SEEDS,
        "q_values": QS,
        "p_values": PS,
        "row_count": len(rows),
        "second_representation_count": cross_checks,
        "limits": "Exact finite resultants only. No irreducibility test, numerical root computation, near-one family, or gap certificate.",
        "rows": rows,
    }
    (ROOT / "results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Passed {len(rows)} exact resultant identities and {cross_checks} powered-polynomial cross-checks.")


if __name__ == "__main__":
    main()
