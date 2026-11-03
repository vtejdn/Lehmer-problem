"""Independent check of normalized joint Lehmer axis certificates.

Reuses only this reviewer's J23 root-isolation and endpoint-displacement
helpers. New normalized geometry is checked through 8x8 edge systems.
Author J24 outputs remain untouched; its direct rerun is routed here.
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
from flint import arb, arb_mat, fmpq, ctx
import sympy as sp

HERE = (_J_PROGRAM / 'verify.py').parent
AUTHOR = (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0024')
PRECISION = 300


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rerun_author():
    before = ((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0024/verification.json')).read_bytes()
    module = load("j24_author_verifier", (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0024/verify.py'))

    with redirect_stdout(io.StringIO()):
        module.main(output_path=_J_OUTPUT / "source-verification.json")
    assert ((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0024/verification.json')).read_bytes() == before
    old = json.loads(before)
    new = json.loads(((_J_OUTPUT / 'source-verification.json')).read_text())
    assert old == new
    return new


def main():
    source = rerun_author()
    helper = load("reviewer_j23_helpers", (_J_ROOT / 'mathematics/computations/programs/Yin_J_G0023/verify.py'))
    ctx.prec = PRECISION
    beta, roots, root_intervals = helper.independent_roots()
    table = json.loads(((_J_ROOT / 'mathematics/computations/outputs/Yin_J_G0024/pilot.json')).read_text())
    assert table["grid"] == 100
    assert [cell["cell"] for cell in table["cells"]] == [[50,75],[75,100]]
    strip = 1/(beta-1)
    word_uses = 0
    distinct = set()
    rows = []
    for index, cell in enumerate(table["cells"]):
        target = arb(fmpq(cell["target_numerator"],cell["target_denominator"]))
        assert target > 0
        certs = cell["certificates"]
        assert sorted((a["coordinate"],a["sign"]) for a in certs) == [
            (i,s) for i in range(8) for s in (-1,1)]
        min_norm2, min_weight = None, None
        axis_rows = []
        for certificate in certs:
            coordinate, sign = certificate["coordinate"], certificate["sign"]
            assert type(coordinate) is int and type(sign) is int
            assert 0 <= coordinate < 8 and sign in (-1,1)
            assert len(certificate["digits"]) == 9
            vertices = []
            for word in certificate["digits"]:
                assert 1 <= len(word) <= 11
                assert all(type(d) is int and d in (-1,0,1) for d in word)
                lo,hi = [arb(fmpq(a,100)) for a in cell["cell"]]
                for digit in word:
                    lo = beta*lo+digit
                    hi = beta*hi+digit
                    assert lo > -strip and hi < strip
                assert lo > -1 and hi < 1
                displacement = helper.vertex(word, roots)
                norm2 = sum(a*a for a in displacement)
                assert norm2 > 0
                lower = norm2.lower()
                min_norm2 = lower if min_norm2 is None else min(min_norm2,lower)
                vertices.append([a/norm2 for a in displacement])
                word_uses += 1
                distinct.add(tuple(word))
            # Solve for the eight nonbase barycentric coordinates at this
            # rational axis point. Recover the base weight by sum-to-one.
            edge = arb_mat([[vertices[j+1][i]-vertices[0][i]
                             for j in range(8)] for i in range(8)])
            rhs = arb_mat([[(sign*target if i == coordinate else 0)-vertices[0][i]]
                           for i in range(8)])
            solution = edge.solve(rhs, algorithm="lu")
            weights = [solution[i,0] for i in range(8)]
            weights.append(1-sum(weights))
            assert all(weight > 0 for weight in weights)
            local_min = min(weight.lower() for weight in weights)
            min_weight = local_min if min_weight is None else min(min_weight,local_min)
            axis_rows.append({"coordinate":coordinate,"sign":sign,
                              "minimum_barycentric_weight":local_min.str(45)})
        radius = (target/arb(8).sqrt().upper()).lower()
        positive_factor = 16*radius-1
        assert positive_factor > 0
        drop = min_norm2*positive_factor
        assert drop >= arb(source["cells"][index]["squared_descent_drop_lower"])
        assert drop >= arb(fmpq(57,100))
        assert min_norm2 >= arb(source["cells"][index]["norm_squared_min_lower"])
        assert min_weight >= arb(source["cells"][index]["barycentric_weight_min_lower"])
        rows.append({"cell":cell["cell"],"axis_radius":target.str(45),
                     "minimum_norm_squared_lower":min_norm2.str(45),
                     "minimum_barycentric_weight_lower":min_weight.str(45),
                     "euclidean_ball_radius_lower":radius.str(45),
                     "positive_descent_factor":positive_factor.str(45),
                     "squared_norm_drop_lower":drop.str(45),"axes":axis_rows})
    assert word_uses == 288 and len(distinct) == 217
    result = {'arb_precision_bits': PRECISION, 'source_payload_matched': True, 'reused_reviewer_helpers': 'J23 independent_roots and vertex only', 'root_isolation_bits': 240, 'root_intervals': root_intervals, 'cells': rows, 'axis_certificates': 32, 'word_uses': word_uses, 'distinct_words': len(distinct), 'max_word_length': max(map(len, distinct)), 'joint_real_dimension': 8, 'neutral_threshold': 8, 'uniform_squared_norm_drop_lower': '57/100', 'limits': 'Finite independent normalized geometry check. D23 owns the full proof review; compact termination and infinite actual core are not established.'}
    ((_J_OUTPUT / 'independent-verification.json')).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(f"Source payload reproduced without author writes; independently checked 32 normalized axis targets, {word_uses} word uses, {len(distinct)} distinct words and uniform drop 57/100.")


if __name__ == "__main__":
    main()
