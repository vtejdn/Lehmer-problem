"""Reviewer rerun plus separately implemented joint-simplex ball check.

Reads J22's integer words; never writes into the author's group. The rerun
uses the original verifier unchanged except for routing its output pathname.
The independent calculation uses 8x8 edge matrices instead of 9x9 augmented
matrices, exact SymPy real-root isolation and Arb arithmetic instead of the
author's Fraction interval functions.
"""

from contextlib import redirect_stdout
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import importlib.util
import io
import json

import flint
from flint import arb, acb, arb_mat, fmpq, fmpz_poly, ctx
import sympy as sp

HERE = (_J_PROGRAM / 'verify.py').parent
REPOSITORY = next(parent for parent in HERE.parents if (parent / "repository/config.json").is_file())
AUTHOR = REPOSITORY / "mathematics/computations/outputs/Yin_J_G0022"
AUTHOR_PROGRAM = REPOSITORY / "mathematics/computations/programs/Yin_J_G0022"
PRECISION = 300


def rerun_author():
    before = (AUTHOR / "verification.json").read_bytes()
    spec = importlib.util.spec_from_file_location("j22_author_verifier", AUTHOR_PROGRAM / "verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    with redirect_stdout(io.StringIO()):
        module.main(output_path=(_J_OUTPUT / 'source-verification.json'))
    assert (AUTHOR / "verification.json").read_bytes() == before
    old = json.loads(before)
    new = json.loads(((_J_OUTPUT / 'source-verification.json')).read_text())
    assert old == new
    return new


def ratio(q):
    q = sp.Rational(q)
    return fmpq(int(q.p), int(q.q))


def rootbox(lo, hi):
    return arb(ratio((lo+hi)/2), ratio((hi-lo)/2))


def independent_roots():
    x, u = sp.symbols("x u")
    coeff = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
    px = sum(c*x**i for i,c in enumerate(coeff))
    q = sp.Poly(u**5+u**4-5*u**3-5*u**2+4*u+3, u)
    assert sp.expand(x**5*q.as_expr().subs(u, x+1/x)-px) == 0
    _, factors = fmpz_poly(coeff).factor()
    assert len(factors) == 1 and factors[0][1] == 1
    intervals = q.intervals(eps=sp.Rational(1, 2**240))
    assert len(intervals) == 5 and all(mult == 1 for _,mult in intervals)
    roots = []
    beta = None
    for (lo,hi),_ in intervals:
        v = rootbox(lo,hi)
        if lo > 2:
            assert beta is None
            beta = (v+(v*v-4).sqrt())/2
        else:
            assert -2 < lo <= hi < 2
            roots.append(acb(v/2, (1-v*v/4).sqrt()))
    assert len(roots) == 4 and beta > arb("1.17") and beta < arb("1.18")
    return beta, roots, [[str(lo),str(hi)] for (lo,hi),_ in intervals]


def vertex(word, zs):
    # Evaluate the endpoint translation forward, then divide out zeta^k.
    # This checks the inverse-exponent word convention by another formula.
    components = []
    for z in zs:
        translated = acb(0)
        for digit in word:
            translated = z*translated+digit
        components.append(translated/(z**len(word)))
    return [z.real for z in components]+[z.imag for z in components]


def simplex_geometry(vertices):
    # v0+E*lambda gives the 8 edge-coordinate barycentric functions.
    edges = arb_mat([[vertices[j+1][i]-vertices[0][i]
                      for j in range(8)] for i in range(8)])
    inv = edges.inv()
    gradients = [[inv[i,j] for j in range(8)] for i in range(8)]
    intercepts = [-sum(row[j]*vertices[0][j] for j in range(8))
                  for row in gradients]
    gradients.append([-sum(row[j] for row in gradients) for j in range(8)])
    intercepts.append(1-sum(intercepts))
    distances = []
    for gradient, intercept in zip(gradients, intercepts):
        assert intercept > 0
        norm = sum(a*a for a in gradient).sqrt()
        assert norm > 0
        distances.append((intercept.lower()/norm.upper()).lower())
    radius = min(distances)
    m2 = max(sum(v*v for v in vertex).upper() for vertex in vertices)
    margin = 3000*radius-m2
    assert margin >= arb(fmpq(5589,1000))
    return radius, m2, margin


def main():
    source = rerun_author()
    ctx.prec = PRECISION
    beta, zs, root_intervals = independent_roots()
    data = json.loads((AUTHOR / "reused-cover.json").read_text())
    assert data["grid"] == 100
    assert [row["j"] for row in data["cells"]] == list(range(50,100))
    cached, rows = {}, []
    endpoint_count = 0
    bstrip = 1/(beta-1)
    for row in data["cells"]:
        words = row["digits"]
        assert len(words) == 9
        vertices = []
        for word in words:
            assert 1 <= len(word) <= 11
            assert all(type(d) is int and d in (-1,0,1) for d in word)
            low = arb(fmpq(row["j"],100))
            high = arb(fmpq(row["j"]+1,100))
            # Endpoint order is preserved by beta>0; checking both therefore
            # verifies the whole closed cell at every intermediate step.
            for digit in word:
                low = beta*low+digit
                high = beta*high+digit
                assert low > -bstrip and high < bstrip
            assert low > -1 and high < 1
            endpoint_count += 1
            vertices.append(vertex(word,zs))
        key = tuple(map(tuple,words))
        if key not in cached:
            cached[key] = simplex_geometry(vertices)
        radius,m2,margin = cached[key]
        rows.append({"cell":row["j"], "radius_lower":radius.str(45),
                     "max_squared_norm_upper":m2.str(45),
                     "descent_margin":margin.str(45)})
    result = {'arb_precision_bits': PRECISION, 'root_isolation_bits': 240, 'source_result_payload_matched': True, 'source_verified_blocks': source['verified_blocks'], 'independently_checked_full_cell_words': endpoint_count, 'independent_edge_simplex_count': len(cached), 'input_irreducibility_checked_by_exact_factorization': True, 'trace_root_intervals': root_intervals, 'joint_real_dimension': 8, 'threshold': 1500, 'every_margin_at_least': '5589/1000', 'rows': rows, 'limits': 'Finite certificate independently reimplemented. Full proof and real-strip/iteration/compactness arguments are reviewed in D G0019; no compact termination, return-core infinity or gap is established.'}
    ((_J_OUTPUT / 'independent-verification.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(f"Source payload reproduced without author writes; independently checked {endpoint_count} full-cell words and {len(cached)} joint edge simplices.")


if __name__ == "__main__":
    main()
