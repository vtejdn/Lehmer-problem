"""Certified three-rotation Hadamard screen, before any parameter sampling."""
from __future__ import annotations

from itertools import permutations
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "repository/config.json").is_file())
INPUT = ROOT / "mathematics/computations/programs/Yin_J_G0097/input.json"
OUTPUT = ROOT / "mathematics/computations/outputs" / HERE.name
EXPECTED = {
    "quartic_Salem_seed": [1, -1, -1, -1, 1],
    "Lehmer_degree10": [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1],
}
L = 972000
TIMEOUT = 300


class Unresolved(Exception):
    pass


def save(name, value):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT / (name + ".writing")
    pending.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    pending.replace(OUTPUT / name)


def worker(name):
    import flint
    from flint import acb_poly, arb, ctx, fmpz_poly

    source = json.loads(INPUT.read_text(encoding="utf-8"))
    selected = {p["name"]: p["coefficients_ascending"]
                for p in source["inputs"] if p["name"] in EXPECTED}
    assert selected == EXPECTED and name in EXPECTED
    pc = EXPECTED[name]
    d = len(pc)-1
    assert d % 2 == 0 and pc == pc[::-1] and pc[0] == pc[-1] == 1

    def inflate(k):
        result = [0]*(k*d+1)
        for i, coefficient in enumerate(pc):
            result[k*i] = coefficient
        return fmpz_poly(result)

    P2, P3, P5 = (inflate(k) for k in (2, 3, 5))
    H23, H25, H35 = 9*P2**3-8*P3**2, 75*P2**5-64*P5**2, 250*P3**5-243*P5**3
    assert (H23.degree(), H25.degree(), H35.degree()) == (6*d, 10*d, 15*d)
    assert (int(H23[6*d]), int(H25[10*d]), int(H35[15*d])) == (1, 11, 7)
    rows = []
    for H, scalar, shift in ((H23, -13500, 3*d), (H25, -1215, 5*d), (H35, -32, 15*d//2)):
        entries = []
        for residue in range(3):
            terms = {(i-shift-residue)//3: scalar*int(c)
                     for i, c in enumerate(H) if c and (i-shift) % 3 == residue}
            offset = min(terms) if terms else 0
            coefficients = [terms.get(k, 0) for k in range(offset, max(terms)+1)] if terms else []
            entries.append((offset, fmpz_poly(coefficients)))
        rows.append(entries)
    determinant = {}
    for permutation in permutations(range(3)):
        inversions = sum(permutation[i] > permutation[j] for i in range(3) for j in range(i+1, 3))
        sign = (-1)**inversions
        offset = sum(rows[j][permutation[j]][0] for j in range(3))
        polynomial = fmpz_poly([sign])
        for j in range(3):
            polynomial *= rows[j][permutation[j]][1]
        for i, coefficient in enumerate(polynomial):
            determinant[i+offset] = determinant.get(i+offset, 0)+int(coefficient)
    determinant = {k: v for k, v in determinant.items() if v}
    payload = {
        "name": name, "complete": False, "p_coefficients_ascending": pc, "degree": d,
        "common_scalar": L, "residue_modulus": 3,
        "residue_matrix": [[{"offset": offset, "coefficients_ascending": [int(c) for c in polynomial]}
                            for offset, polynomial in row] for row in rows],
        "determinant_nonzero": bool(determinant), "flint_version": flint.__version__,
    }
    if not determinant:
        payload.update({"complete": True, "excludes_below_log2": False,
                        "finding": "exact zero determinant; screen inconclusive"})
        save(name + "_screen.json", payload)
        return
    offset = min(determinant)
    K = fmpz_poly([determinant.get(k, 0) for k in range(offset, max(determinant)+1)])
    assert K[0] != 0
    payload.update({"determinant_offset": offset, "K_coefficients_ascending": [int(c) for c in K],
                    "K_degree": K.degree(), "attempts": []})
    save(name + "_screen.json", payload)

    def persist(value):
        if not value.is_finite() or not value.rad() < arb("1e-12"):
            raise Unresolved("insufficient scalar enclosure")
        text = value.str(50, more=True)
        assert arb(text).contains(value)
        return text

    for bits in (256, 512):
        ctx.prec = bits
        try:
            content, factors = K.factor_squarefree()
            restored = fmpz_poly([content])
            measure = arb(abs(int(K[K.degree()]))).log()
            root_count = 0
            witnesses = []
            for factor, multiplicity in factors:
                restored *= factor**multiplicity
                assert factor.gcd(factor.derivative()).degree() == 0
                roots = acb_poly(factor).roots(tol=arb("1e-30"), maxprec=bits)
                if len(roots) != factor.degree():
                    raise Unresolved("incomplete root count")
                assert all(not roots[i].overlaps(roots[j]) for i in range(len(roots)) for j in range(i))
                records = []
                for root in roots:
                    contribution = arb(1).max(abs(root)).log()
                    measure += multiplicity*contribution
                    records.append({"real": root.real.str(50, more=True),
                                    "imag": root.imag.str(50, more=True),
                                    "log_plus_modulus": persist(contribution)})
                root_count += multiplicity*len(roots)
                witnesses.append({"coefficients_ascending": [int(c) for c in factor],
                                  "multiplicity": multiplicity, "roots": records})
            assert restored == K and root_count == K.degree()
            lower = arb(3).log() + (arb(2).log()+2*measure-6*arb(L).log())/3
            surplus = lower-arb(2).log()
            payload.update({"complete": True, "precision_bits": bits,
                            "factorization_content": int(content), "factors": witnesses,
                            "root_count_with_multiplicity": root_count,
                            "mahler_K": persist(measure), "mahler_W": persist(measure-3*arb(L).log()),
                            "haar_lower_bound": persist(lower), "surplus_over_log2": persist(surplus),
                            "surplus_over_margin_target": persist(surplus+arb(1)/16),
                            "excludes_below_log2": bool(surplus >= 0),
                            "excludes_operational_margin": bool(surplus+arb(1)/16 > 0)})
            save(name + "_screen.json", payload)
            print(name, "determinant degree", K.degree(), "uniform lower bound", lower.str(20),
                  "surplus", surplus.str(20), flush=True)
            return
        except (Unresolved, ValueError) as error:
            payload["attempts"].append({"precision_bits": bits, "error": str(error)})
            save(name + "_screen.json", payload)
    raise Unresolved("both declared precision attempts failed")


def main():
    statuses = []
    for name, pc in EXPECTED.items():
        save(name + "_screen.json", {"name": name, "p_coefficients_ascending": pc,
                                    "complete": False, "state": "current worker not yet completed"})
        try:
            process = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()), "--worker", name],
                                     timeout=TIMEOUT)
            statuses.append({"name": name, "exit_code": process.returncode, "timed_out": False})
        except subprocess.TimeoutExpired:
            statuses.append({"name": name, "exit_code": 124, "timed_out": True})
    inputs = [json.loads((OUTPUT/(name+"_screen.json")).read_text(encoding="utf-8")) for name in EXPECTED]
    complete = all(v["exit_code"] == 0 for v in statuses) and all(v["complete"] for v in inputs)
    save("screen.json", {"complete": complete, "statuses": statuses, "inputs": inputs})
    raise SystemExit(0 if complete else 1)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--worker" and sys.argv[2] in EXPECTED:
        worker(sys.argv[2])
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("Only the two declared determinant screens are supported.")
