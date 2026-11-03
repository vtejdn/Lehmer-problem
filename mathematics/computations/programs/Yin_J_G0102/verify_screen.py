"""Independent exact/Jensen verification of the two declared J102 screens.

The coefficient construction uses Python integer Laurent dictionaries and
cofactors, without importing the author's program or generated polynomials.
An additional determinant expansion in Z[omega], omega^2+omega+1=0, checks
the complete three-rotation identity before any numerical root calculation.
FLINT's certified ball-root engine is shared with the author; this is not a
second numerical library or a blind review of the announced author values.
Author data enter only after each independent construction and Jensen bound.
"""
from __future__ import annotations

from itertools import permutations
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
INPUT = HERE.parent / "Yin_J_G0097/input.json"
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
EXPECTED = {
    "quartic_Salem_seed": [1, -1, -1, -1, 1],
    "Lehmer_degree10": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
}
L = 972000
PRECISIONS = (256, 512)
TIMEOUT = 300
TOLERANCE = "1e-30"


def save(name, payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT / (name + ".writing")
    pending.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT / name)


def add(*polynomials):
    result = {}
    for poly in polynomials:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {n: c for n, c in result.items() if c}


def scale(poly, scalar):
    return {n: scalar*c for n, c in poly.items() if scalar*c}


def multiply(left, right):
    result = {}
    for n, a in left.items():
        for m, b in right.items():
            result[n+m] = result.get(n+m, 0) + a*b
    return {n: c for n, c in result.items() if c}


def power(poly, exponent):
    result = {0: 1}
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def determinant_cofactors(matrix):
    a, b, c = matrix
    minors = [add(multiply(b[1], c[2]), scale(multiply(b[2], c[1]), -1)),
              add(multiply(b[0], c[2]), scale(multiply(b[2], c[0]), -1)),
              add(multiply(b[0], c[1]), scale(multiply(b[1], c[0]), -1))]
    return add(multiply(a[0], minors[0]),
               scale(multiply(a[1], minors[1]), -1), multiply(a[2], minors[2]))


def eisenstein_product(a, b):
    # (a0+a1*w)(b0+b1*w), reduced using w^2=-1-w.
    return (a[0]*b[0]-a[1]*b[1],
            a[0]*b[1]+a[1]*b[0]-a[1]*b[1])


def eisenstein_poly_product(left, right):
    result = {}
    for n, a in left.items():
        for m, b in right.items():
            c = eisenstein_product(a, b)
            old = result.get(n+m, (0, 0))
            result[n+m] = (old[0]+c[0], old[1]+c[1])
    return {n: c for n, c in result.items() if c != (0, 0)}


def full_rotation_determinant(centered):
    roots = ((1, 0), (0, 1), (-1, -1))
    matrix = [[{n: (c*roots[(j*n) % 3][0], c*roots[(j*n) % 3][1])
                for n, c in poly.items()} for poly in centered] for j in range(3)]
    result = {}
    for perm in permutations(range(3)):
        parity = sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
        term = {0: ((-1)**parity, 0)}
        for row in range(3):
            term = eisenstein_poly_product(term, matrix[row][perm[row]])
        for n, c in term.items():
            old = result.get(n, (0, 0))
            result[n] = (old[0]+c[0], old[1]+c[1])
    return {n: c for n, c in result.items() if c != (0, 0)}


def ordinary(poly):
    if not poly:
        return 0, []
    offset = min(poly)
    return offset, [poly.get(n, 0) for n in range(offset, max(poly)+1)]


def worker(name):
    import flint
    from flint import acb, acb_poly, arb, ctx, fmpz_poly

    source = json.loads(INPUT.read_text(encoding="utf-8"))
    assert source["window_multiple"] == 2 and source["threshold"] == 4
    selected = {v["name"]: v["coefficients_ascending"] for v in source["inputs"]
                if v["name"] in EXPECTED}
    assert selected == EXPECTED and name in EXPECTED
    pc = selected[name]
    d = len(pc)-1
    assert d % 2 == 0 and pc == pc[::-1] and pc[0] == pc[-1] == 1

    def substitute(k):
        return {k*n: c for n, c in enumerate(pc) if c}

    p2, p3, p5 = (substitute(k) for k in (2, 3, 5))
    hs = [add(scale(power(p2, 3), 9), scale(power(p3, 2), -8)),
          add(scale(power(p2, 5), 75), scale(power(p5, 2), -64)),
          add(scale(power(p3, 5), 250), scale(power(p5, 3), -243))]
    assert [(min(h), max(h), h[0], h[max(h)]) for h in hs] == [
        (0, 6*d, 1, 1), (0, 10*d, 11, 11), (0, 15*d, 7, 7)]
    assert all(h.get(n, 0) == h.get(max(h)-n, 0)
               for h in hs for n in range(max(h)+1))
    centered = [{n-shift: scalar*c for n, c in h.items()}
                for h, scalar, shift in zip(hs, (-13500, -1215, -32), (3*d, 5*d, 15*d//2))]
    residues = []
    for poly in centered:
        row = [{}, {}, {}]
        for n, c in poly.items():
            quotient, residue = divmod(n, 3)
            row[residue][quotient] = c
        assert add(*({3*n+r: c for n, c in row[r].items()} for r in range(3))) == poly
        residues.append(row)
    determinant = determinant_cofactors(residues)
    direct = full_rotation_determinant(centered)
    # det(D_omega)=-3-6*omega and the diagonal contributes z^3.
    assert direct == {3*n+3: (-3*c, -6*c) for n, c in determinant.items()}
    residue_records = [[dict(zip(("offset", "coefficients_ascending"), ordinary(p)))
                        for p in row] for row in residues]
    payload = {"name": name, "complete": False, "p_coefficients_ascending": pc,
               "degree": d, "common_scalar": L, "residue_modulus": 3,
               "construction": "Python integer convolutions and Laurent cofactors",
               "full_rotation_check": "exact Z[omega] six-term expansion equals (-3-6omega)z^3 W(z^3)",
               "residue_matrix": residue_records, "determinant_nonzero": bool(determinant),
               "flint_version": flint.__version__, "precision_schedule_bits": list(PRECISIONS),
               "root_radius_target": TOLERANCE, "timeout_seconds_per_input": TIMEOUT}
    if not determinant:
        author = json.loads((OUTPUT / (name+"_screen.json")).read_text(encoding="utf-8"))
        assert author["complete"] and author["name"] == name and not author["determinant_nonzero"]
        assert author["residue_matrix"] == residue_records
        payload.update({"complete": True, "author_comparison_passed": True,
                        "finding": "exact zero determinant; no logarithm evaluated"})
        save(name+"_screen-verification.json", payload)
        return

    offset, kc = ordinary(determinant)
    assert kc[0] and kc[-1]
    K = fmpz_poly(kc)
    payload.update({"determinant_offset": offset, "K_coefficients_ascending": kc,
                    "K_degree": len(kc)-1, "K_leading_coefficient": kc[-1], "attempts": []})
    save(name+"_screen-verification.json", payload)

    def ball_text(value):
        assert value.is_finite()
        text = value.str(55, more=True)
        assert arb(text).contains(value)
        return text

    def quantity(value):
        assert value.is_finite() and value.rad() < arb("1e-12")
        decimal = format(float(value.mid()), ".15g")
        assert abs(value-arb(decimal)) < arb("1e-10")
        return {"ball": ball_text(value), "decimal": decimal,
                "reported_absolute_error_bound": "1e-10"}

    for bits in PRECISIONS:
        ctx.prec = bits
        try:
            content, factors = K.factor_squarefree()
            restored = fmpz_poly([content])
            degree_count = 0
            measure = arb(abs(kc[-1])).log()
            factor_records, native_roots = [], {}
            for factor, multiplicity in factors:
                assert multiplicity >= 1 and factor.gcd(factor.derivative()).degree() == 0
                restored *= factor**multiplicity
                roots = acb_poly(factor).roots(tol=arb(TOLERANCE), maxprec=bits)
                assert len(roots) == factor.degree()
                assert all(not roots[i].overlaps(roots[j]) for i in range(len(roots)) for j in range(i))
                records = []
                for root in roots:
                    assert root.real.is_finite() and root.imag.is_finite()
                    assert root.real.rad() <= arb(TOLERANCE) and root.imag.rad() <= arb(TOLERANCE)
                    assert acb_poly(factor)(root).contains(0)
                    term = arb(1).max(abs(root)).log()
                    measure += multiplicity*term
                    records.append({"real": ball_text(root.real), "imag": ball_text(root.imag),
                                    "log_plus_modulus": ball_text(term)})
                fc = [int(c) for c in factor]
                native_roots[tuple(fc)] = (multiplicity, roots)
                factor_records.append({"coefficients_ascending": fc, "multiplicity": multiplicity,
                                       "roots": records})
                degree_count += multiplicity*len(roots)
            assert restored == K and degree_count == K.degree()
            mw = measure-3*arb(L).log()
            lower = arb(3).log()+(arb(2).log()+2*mw)/3
            surplus = lower-arb(2).log()
            margin = surplus+arb(1)/16
            quantities = {"mahler_K": quantity(measure), "mahler_W": quantity(mw),
                          "haar_lower_bound": quantity(lower), "surplus_over_log2": quantity(surplus),
                          "surplus_over_margin_target": quantity(margin)}
            assert surplus > 0 or surplus < 0
            assert margin > 0 or margin < 0
            break
        except (ValueError, ArithmeticError, AssertionError) as error:
            payload["attempts"].append({"precision_bits": bits, "error": repr(error)})
            save(name+"_screen-verification.json", payload)
            if bits == PRECISIONS[-1]:
                raise

    # Only now consult the actual author certificate; it generates no arithmetic.
    author = json.loads((OUTPUT / (name+"_screen.json")).read_text(encoding="utf-8"))
    assert author["complete"] is True and author["name"] == name
    assert author["p_coefficients_ascending"] == pc and author["degree"] == d
    assert author["common_scalar"] == L and author["residue_modulus"] == 3
    assert author["residue_matrix"] == residue_records and author["determinant_nonzero"]
    assert author["determinant_offset"] == offset and author["K_coefficients_ascending"] == kc
    assert author["K_degree"] == K.degree() and author["precision_bits"] in PRECISIONS
    assert author["root_count_with_multiplicity"] == degree_count
    author_restored = fmpz_poly([author["factorization_content"]])
    used_factors = set()
    for fact in author["factors"]:
        fc, multiplicity = tuple(fact["coefficients_ascending"]), fact["multiplicity"]
        assert fc in native_roots and fc not in used_factors
        used_factors.add(fc)
        own_multiplicity, own_roots = native_roots[fc]
        assert multiplicity == own_multiplicity
        author_restored *= fmpz_poly(list(fc))**multiplicity
        reported_roots = [acb(arb(v["real"]), arb(v["imag"])) for v in fact["roots"]]
        assert len(reported_roots) == len(own_roots)
        assert all(not reported_roots[i].overlaps(reported_roots[j])
                   for i in range(len(reported_roots)) for j in range(i))
        matches = []
        for root, record in zip(reported_roots, fact["roots"]):
            assert root.real.is_finite() and root.imag.is_finite()
            match = [j for j, own in enumerate(own_roots) if root.overlaps(own)]
            assert len(match) == 1
            matches.append(match[0])
            term = arb(1).max(abs(root)).log()
            assert term.overlaps(arb(record["log_plus_modulus"]))
        assert len(set(matches)) == len(own_roots)
    assert used_factors == set(native_roots) and author_restored == K
    comparisons = {}
    for key, own in quantities.items():
        reported = arb(author[key])
        assert reported.is_finite() and reported.rad() < arb("1e-12")
        assert arb(own["ball"]).overlaps(reported)
        comparisons[key] = {"author_ball": author[key], "independent_ball": own["ball"],
                            "enclosures_overlap": True}
    assert author["excludes_below_log2"] == bool(surplus >= 0)
    assert author["excludes_operational_margin"] == bool(margin > 0)
    payload.update({"complete": True, "precision_bits": bits,
                    "factorization_content": int(content), "factors": factor_records,
                    "root_count_with_multiplicity": degree_count, "quantities": quantities,
                    "excludes_below_log2": bool(surplus >= 0),
                    "excludes_operational_margin": bool(margin > 0),
                    "author_comparison_passed": True, "author_comparisons": comparisons,
                    "parameter_grid_evaluations": 0,
                    "method_boundary": "independent integer construction and native code; shared certified FLINT engine"})
    save(name+"_screen-verification.json", payload)
    print(name, "K degree", K.degree(), "lower", quantities["haar_lower_bound"]["decimal"],
          "log2 surplus", quantities["surplus_over_log2"]["decimal"],
          "margin surplus", quantities["surplus_over_margin_target"]["decimal"], flush=True)


def main():
    statuses = []
    for name in EXPECTED:
        save(name+"_screen-verification.json", {"name": name, "complete": False})
        try:
            process = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker", name],
                                     timeout=TIMEOUT)
            statuses.append({"name": name, "exit_code": process.returncode, "timed_out": False})
        except subprocess.TimeoutExpired:
            statuses.append({"name": name, "exit_code": 124, "timed_out": True})
    records = [json.loads((OUTPUT/(name+"_screen-verification.json")).read_text(encoding="utf-8"))
               for name in EXPECTED]
    complete = all(v["exit_code"] == 0 for v in statuses) and all(v["complete"] for v in records)
    if complete:
        author = json.loads((OUTPUT/"screen.json").read_text(encoding="utf-8"))
        assert author["complete"] and len(author["inputs"]) == len(EXPECTED)
        assert [v["name"] for v in author["inputs"]] == list(EXPECTED)
        for item in author["inputs"]:
            assert item == json.loads((OUTPUT/(item["name"]+"_screen.json")).read_text(encoding="utf-8"))
    save("screen-verification.json", {"complete": complete, "independent_complete": complete,
                                      "precision_schedule_bits": list(PRECISIONS),
                                      "timeout_seconds_per_input": TIMEOUT,
                                      "parameter_grid_evaluations": 0,
                                      "statuses": statuses, "inputs": records})
    raise SystemExit(0 if complete else 1)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--worker" and sys.argv[2] in EXPECTED:
        worker(sys.argv[2])
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("Only the two declared independent screens are supported.")
