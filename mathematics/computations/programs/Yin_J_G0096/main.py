"""One declared exact quartic-elimination worker, with a 180 s supervisor.

Scope and mathematical reduction: readme.md and Yin_C_G0148_v1.md.
No generated output is an input. All artifacts remain in this J group.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import subprocess
import sys
import time

HERE = (_J_PROGRAM / 'main.py').parent
ROOT = _J_ROOT
TIMEOUT_SECONDS = 180


def save(name, payload):
    path = ((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)
    partial = _J_OUTPUT / (name + ".writing")
    partial.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    partial.replace(path)


def worker():
    import sympy as sp

    t, x, A, B = sp.symbols("t x A B")

    def polynomial(expr, variables):
        poly = sp.Poly(expr, *variables, domain=sp.ZZ)
        coefficient, factors = sp.factor_list(poly)
        return {
            "variables": [str(v) for v in variables],
            "expression": sp.sstr(poly.as_expr()),
            "zero": bool(poly.is_zero),
            "terms": [[list(monomial), int(value)] for monomial, value in poly.terms()],
            "factor_coefficient": str(coefficient),
            "factors": [
                {"expression": sp.sstr(factor.as_expr()), "multiplicity": int(power)}
                for factor, power in factors
            ],
        }

    def integer_roots(expr, variable):
        poly = sp.Poly(expr, variable, domain=sp.ZZ)
        if poly.is_zero:
            return None
        roots = []
        _, factors = sp.factor_list(poly)
        for factor, _ in factors:
            if factor.degree() == 1:
                value = -sp.Rational(factor.nth(0), factor.nth(1))
                if value.q == 1:
                    roots.append(int(value))
        return sorted(set(roots))

    def inspect_original(expr, name):
        P = sp.Poly(expr, t, domain=sp.ZZ)
        P2 = sp.Poly(P.as_expr().subs(t, t**2), t, domain=sp.ZZ)
        P3 = sp.Poly(P.as_expr().subs(t, t**3), t, domain=sp.ZZ)
        HP = 9 * P2**3 - 8 * P3**2
        remainder = HP.rem(P)
        _, factors = sp.factor_list(P)
        irreducible = len(factors) == 1 and factors[0][1] == 1 and factors[0][0].degree() == P.degree()
        coefficients = P.all_coeffs()
        cyclotomic = bool(P.is_cyclotomic)
        return {
            "name": name,
            "P": polynomial(P.as_expr(), (t,)),
            "degree": int(P.degree()),
            "monic": P.LC() == 1,
            "constant": int(P.nth(0)),
            "reciprocal": coefficients == coefficients[::-1],
            "irreducible_over_Q": irreducible,
            "is_cyclotomic": cyclotomic,
            "H_remainder": polynomial(remainder.as_expr(), (t,)),
            "H_divisible_by_P": bool(remainder.is_zero),
            "admissible_nontorsion_counterexample": bool(
                P.LC() == 1 and P.nth(0) == 1 and coefficients == coefficients[::-1]
                and irreducible and not cyclotomic and remainder.is_zero
            ),
        }

    controls = [
        ("quadratic_A3", t**2 - 3*t + 1),
        ("quadratic_Aminus3", t**2 + 3*t + 1),
        ("quartic_Salem_seed", t**4 - t**3 - t**2 - t + 1),
        ("quartic_positive_trace", t**4 - 3*t**3 + 3*t**2 - 3*t + 1),
        ("quartic_radical_A4", t**4 - 4*t**2 + 1),
        ("Lehmer_degree10", t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1),
        ("Phi5_torsion", sum(t**j for j in range(5))),
        ("Phi7_torsion", sum(t**j for j in range(7))),
        ("repeated_one_reducible", (t-1)**2),
    ]
    data = {'scope': 'Nine declared controls and full symbolic trace quadratic T=x^2-A*x+B only', 'arithmetic': 'Exact ZZ/QQ polynomial arithmetic; no numerical roots', 'stage': 'controls', 'controls': []}
    for name, expr in controls:
        data["controls"].append(inspect_original(expr, name))
    for row in data["controls"]:
        if row["name"] in {"Phi5_torsion", "Phi7_torsion", "repeated_one_reducible"}:
            assert row["H_divisible_by_P"], row["name"]
        if row["name"] in {"quadratic_A3", "quadratic_Aminus3"}:
            assert not row["H_divisible_by_P"], row["name"]

    domain = sp.ZZ[A, B]
    T = sp.Poly(x**2-A*x+B, x, domain=domain)
    C2 = sp.Poly(x**2-2, x, domain=domain)
    C3 = sp.Poly(x**3-3*x, x, domain=domain)
    JT = 9*T.compose(C2)**3-8*T.compose(C3)**2
    rem = JT.rem(T)
    coeff_x, coeff_1 = sp.expand(rem.nth(1)), sp.expand(rem.nth(0))
    data["trace_quadratic"] = {
        "T": "x**2-A*x+B",
        "coefficient_x": polynomial(coeff_x, (A, B)),
        "coefficient_1": polynomial(coeff_1, (A, B)),
        "coefficient_gcd": polynomial(sp.gcd(coeff_x, coeff_1), (A, B)),
    }
    data["stage"] = "symbolic_remainder_complete"

    resultant_B = sp.resultant(coeff_x, coeff_1, B)
    data["trace_quadratic"]["resultant_eliminate_B"] = polynomial(resultant_B, (A,))
    data["stage"] = "first_resultant_complete"
    resultant_A = sp.resultant(coeff_x, coeff_1, A)
    data["trace_quadratic"]["resultant_eliminate_A"] = polynomial(resultant_A, (B,))
    data["stage"] = "both_resultants_complete"

    isolated_pairs = set()
    branches = []
    if resultant_B != 0:
        for a0 in integer_roots(resultant_B, A):
            first = sp.Poly(coeff_x.subs(A, a0), B, domain=sp.ZZ)
            second = sp.Poly(coeff_1.subs(A, a0), B, domain=sp.ZZ)
            common = sp.gcd(first, second)
            b_roots = integer_roots(common.as_expr(), B)
            branches.append({
                "A": a0,
                "coefficient_x": polynomial(first.as_expr(), (B,)),
                "coefficient_1": polynomial(second.as_expr(), (B,)),
                "gcd": polynomial(common.as_expr(), (B,)),
                "all_B_survive": b_roots is None,
                "integral_B_candidates": b_roots,
            })
            if b_roots is not None:
                isolated_pairs.update((a0, b0) for b0 in b_roots)
    elif resultant_A != 0:
        for b0 in integer_roots(resultant_A, B):
            first = sp.Poly(coeff_x.subs(B, b0), A, domain=sp.ZZ)
            second = sp.Poly(coeff_1.subs(B, b0), A, domain=sp.ZZ)
            common = sp.gcd(first, second)
            a_roots = integer_roots(common.as_expr(), A)
            branches.append({
                "B": b0,
                "coefficient_x": polynomial(first.as_expr(), (A,)),
                "coefficient_1": polynomial(second.as_expr(), (A,)),
                "gcd": polynomial(common.as_expr(), (A,)),
                "all_A_survive": a_roots is None,
                "integral_A_candidates": a_roots,
            })
            if a_roots is not None:
                isolated_pairs.update((a0, b0) for a0 in a_roots)
    else:
        branches.append({"both_resultants_zero": True, "classification": "unresolved algebraic curve or degeneracy"})

    candidates = []
    for a0, b0 in sorted(isolated_pairs):
        assert coeff_x.subs({A: a0, B: b0}) == 0
        assert coeff_1.subs({A: a0, B: b0}) == 0
        P = t**4-a0*t**3+(b0+2)*t**2-a0*t+1
        row = inspect_original(P, f"trace_A{a0}_B{b0}")
        assert row["H_divisible_by_P"]
        row["A"], row["B"] = a0, b0
        candidates.append(row)
    data["trace_quadratic"]["specialized_branches"] = branches
    data["trace_quadratic"]["isolated_integer_candidates"] = candidates
    unresolved = any(row.get("all_A_survive") or row.get("all_B_survive") or row.get("both_resultants_zero") for row in branches)
    data["summary"] = {
        "control_count": len(controls),
        "control_zero_names": [row["name"] for row in data["controls"] if row["H_divisible_by_P"]],
        "isolated_integer_pairs": [list(pair) for pair in sorted(isolated_pairs)],
        "unresolved_parameter_branch": unresolved,
        "admissible_counterexamples": [row["name"] for row in data["controls"]+candidates if row["admissible_nontorsion_counterexample"]],
        "complete_projection_classification_subject_to_independent_check": not unresolved,
    }
    data["stage"] = "complete"
    save("results.json", data)
    print(json.dumps(data["summary"], ensure_ascii=False))


def supervise():
    command = [sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'main.py'), '--worker']
    try:
        process = subprocess.run(command, cwd=_J_PROGRAM, timeout=180,
                                 text=True, encoding="utf-8", capture_output=True)
    except subprocess.TimeoutExpired as error:
        (_J_OUTPUT / "failure.json").write_text(
            json.dumps({"status": "timeout", "completed_output": False}) + "\n", encoding="utf-8")
        print(str(error), file=sys.stderr)
        raise SystemExit(124)
    if process.stdout:
        print(process.stdout, end="")
    if process.stderr:
        print(process.stderr, end="", file=sys.stderr)
    if process.returncode:
        raise SystemExit(process.returncode)
    payload = json.loads((_J_OUTPUT / 'results.json').read_text(encoding="utf-8"))
    assert payload['stage'] == 'complete'
    raise SystemExit(0)



if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--worker":
        worker()
    elif len(sys.argv) == 1:
        supervise()
    else:
        raise SystemExit("Only the declared no-argument supervised run or internal --worker is supported.")
