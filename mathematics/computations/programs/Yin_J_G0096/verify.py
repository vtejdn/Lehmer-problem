"""Independent native reconstruction; scope and limits are in readme.md.

Uses quotient pairs to generate the symbolic data and compares the full
mathematical payload. Shares SymPy kernels, not the author's main.py code.
"""
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import datetime as dt
import json
import subprocess
import sys
import time

HERE = (_J_PROGRAM / 'verify.py').parent


def save(name, data):
    target = ((_J_PROGRAM if name in ('main.py', 'readme.md', 'verify.py') else _J_OUTPUT) / name)
    partial = target.with_suffix(target.suffix + ".writing")
    partial.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    partial.replace(target)


def worker():
    import sympy as s
    A, B, t = s.symbols("A B t")
    saved = json.loads(((_J_OUTPUT / 'results.json')).read_text(encoding="utf-8"))
    source = saved["trace_quadratic"]

    def unpack(row, variables):
        return s.expand(sum(s.Integer(c) * s.prod(v**e for v, e in zip(variables, powers))
                            for powers, c in row["terms"]))

    # (constant, coefficient of x), using x^2=A*x-B.
    def add(u, v):
        return tuple(s.expand(a+b) for a, b in zip(u, v))

    def scale(c, u):
        return tuple(s.expand(c*a) for a in u)

    def mul(u, v):
        a, b = u
        c, d = v
        return s.expand(a*c-B*b*d), s.expand(a*d+b*c+A*b*d)

    x = (s.Integer(0), s.Integer(1))
    x2 = mul(x, x)
    c2 = add(x2, (-2, 0))
    c3 = add(mul(x2, x), scale(-3, x))

    def trace_polynomial(y):
        return add(add(mul(y, y), scale(-A, y)), (B, 0))

    a = trace_polynomial(c2)
    b = trace_polynomial(c3)
    V, U = add(scale(9, mul(mul(a, a), a)), scale(-8, mul(b, b)))
    assert s.expand(U-unpack(source["coefficient_x"], (A, B))) == 0
    assert s.expand(V-unpack(source["coefficient_1"], (A, B))) == 0
    assert s.expand(s.gcd(U, V)-unpack(source["coefficient_gcd"], (A, B))) == 0

    def verify_factorization(poly, row, variable):
        coefficient, factors = s.factor_list(poly, variable)
        product = s.Integer(coefficient)
        root_set = set()
        nonlinear_degrees = []
        for factor, power in factors:
            product *= factor**power
            fp = s.Poly(factor, variable, domain=s.QQ)
            assert fp.is_irreducible
            if fp.degree() == 1:
                root = -fp.nth(0)/fp.nth(1)
                if root.q == 1:
                    root_set.add(int(root))
            else:
                nonlinear_degrees.append(fp.degree())
        assert s.expand(product-poly) == 0
        saved_product = s.sympify(row["factor_coefficient"])
        for factor in row["factors"]:
            saved_product *= s.sympify(factor["expression"], locals={str(variable): variable})**factor["multiplicity"]
        assert s.expand(saved_product-poly) == 0
        return sorted(root_set), nonlinear_degrees

    projections = {}
    for eliminated, kept, key in ((B, A, "resultant_eliminate_B"), (A, B, "resultant_eliminate_A")):
        result = s.resultant(U, V, eliminated)
        assert result != 0
        assert s.expand(result-unpack(source[key], (kept,))) == 0
        roots, nonlinear = verify_factorization(result, source[key], kept)
        projections[str(kept)] = {"degree": s.degree(result, kept), "integer_roots": roots,
                                  "irreducible_nonlinear_degrees": nonlinear}
    assert projections["A"]["integer_roots"] == [-1, 0, 1, 4]

    pairs = []
    branches = []
    for a0 in projections["A"]["integer_roots"]:
        u = s.Poly(U.subs(A, a0), B, domain=s.QQ)
        v = s.Poly(V.subs(A, a0), B, domain=s.QQ)
        assert not (u.is_zero and v.is_zero)
        common = s.gcd(u, v).monic()
        row = next(r for r in source["specialized_branches"] if r["A"] == a0)
        assert s.expand(u.as_expr()-unpack(row["coefficient_x"], (B,))) == 0
        assert s.expand(v.as_expr()-unpack(row["coefficient_1"], (B,))) == 0
        saved_gcd = unpack(row["gcd"], (B,))
        old_gcd = s.Poly(saved_gcd, B, domain=s.QQ).monic()
        assert common == old_gcd
        roots, nonlinear = verify_factorization(saved_gcd, row["gcd"], B)
        assert roots == row["integral_B_candidates"]
        assert row["all_B_survive"] is False
        branches.append({"A": a0, "gcd": str(common.as_expr()), "integer_B": roots,
                         "irreducible_nonlinear_degrees": nonlinear})
        pairs.extend([a0, b0] for b0 in roots)
    assert pairs == [[-1, -1], [0, -4], [1, -2], [4, 4]]
    assert pairs == saved["summary"]["isolated_integer_pairs"]

    # Separate exact monic long reduction and repeated modular multiplication.
    def reduce_mod(expr, P):
        q = s.Poly(expr, t, domain=s.ZZ)
        while not q.is_zero and q.degree() >= P.degree():
            q -= s.Poly(q.LC()*t**(q.degree()-P.degree()), t)*P
        return q.as_expr()

    def power_mod(base, exponent, P):
        value = s.Integer(1)
        for _ in range(exponent):
            value = reduce_mod(value*base, P)
        return value

    def original_remainder(expr):
        P = s.Poly(expr, t, domain=s.ZZ)
        v2 = reduce_mod(expr.subs(t, t*t), P)
        v3 = reduce_mod(expr.subs(t, t*t*t), P)
        result = reduce_mod(9*power_mod(v2, 3, P)-8*power_mod(v3, 2, P), P)
        return P, result

    control_inputs = [t*t-3*t+1, t*t+3*t+1, t**4-t**3-t*t-t+1,
                      t**4-3*t**3+3*t*t-3*t+1, t**4-4*t*t+1,
                      t**10+t**9-t**7-t**6-t**5-t**4-t**3+t+1,
                      sum(t**j for j in range(5)), sum(t**j for j in range(7)), (t-1)**2]
    zero_controls = []
    for index, expr in enumerate(control_inputs):
        P, remainder = original_remainder(expr)
        row = saved["controls"][index]
        assert s.expand(P.as_expr()-unpack(row["P"], (t,))) == 0
        assert s.expand(remainder-unpack(row["H_remainder"], (t,))) == 0
        assert bool(remainder == 0) == row["H_divisible_by_P"]
        assert bool(P.is_irreducible) == row["irreducible_over_Q"]
        assert bool(P.is_cyclotomic) == row["is_cyclotomic"]
        verify_factorization(P.as_expr(), row["P"], t)
        if remainder == 0:
            zero_controls.append(row["name"])
    assert zero_controls == saved["summary"]["control_zero_names"]

    candidate_factors = []
    for a0, b0 in pairs:
        expr = t**4-a0*t**3+(b0+2)*t*t-a0*t+1
        P, remainder = original_remainder(expr)
        row = next(r for r in source["isolated_integer_candidates"] if [r["A"], r["B"]] == [a0, b0])
        assert remainder == 0
        assert unpack(row["H_remainder"], (t,)) == 0
        verify_factorization(expr, row["P"], t)
        assert bool(P.is_irreducible) == row["irreducible_over_Q"]
        assert bool(P.is_cyclotomic) == row["is_cyclotomic"]
        assert all(s.Poly(f, t).is_cyclotomic for f, _ in s.factor_list(expr, t)[1])
        candidate_factors.append(str(s.factor(expr)))

    out = {'status': 'pass', 'symbolic_pair_reconstruction': True, 'both_resultants_and_factor_products': True, 'projections': projections, 'all_branches': branches, 'integer_pairs': pairs, 'nine_control_remainders_and_factorizations': True, 'zero_controls': zero_controls, 'candidate_original_factorizations': candidate_factors, 'shared_kernel_limit': 'Independent implementation/run; same SymPy exact polynomial kernels; no formal verification'}
    # Convert SymPy integer metadata only; mathematical values were checked above.
    save("verification.json", json.loads(json.dumps(out, default=int)))
    print(json.dumps({"status": "pass", "integer_pairs": pairs, "controls": len(control_inputs)}))


def supervise():
    command = [sys.executable, '-B', '-X', 'utf8', str(_J_PROGRAM / 'verify.py'), '--worker']
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
    payload = json.loads((_J_OUTPUT / 'verification.json').read_text(encoding="utf-8"))
    assert payload['status'] == 'pass'
    raise SystemExit(0)



if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        supervise()
    else:
        raise SystemExit("Use the no-argument supervised verification.")
