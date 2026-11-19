"""First two one-norm minima in the width-nine quartic Salem signed lattices."""

import json
import runpy
from itertools import combinations
from math import gcd
from pathlib import Path


GROUP = Path(__file__).resolve().parents[2]
QUARTIC = runpy.run_path(str(GROUP / "versions" / "v5" / "quartic_circuits.py"))
BASE = QUARTIC["BASE"]
WIDTH = 9
EXPONENTS = (16, 32, 64, 128, 256)
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v6" / "results.json"


def minors(u, v):
    return [u[i] * v[j] - u[j] * v[i] for i, j in combinations(range(len(u)), 2)]


def minimum_witness(n, sign, candidates):
    """The candidates are sorted by norm and contain one vector per sign pair."""
    row = candidates[0]
    value = BASE["norm_one"](row)
    count = sum(BASE["norm_one"](r) == value for r in candidates)
    assert count == 1
    if next(a for a in row if a) < 0:
        row = [-a for a in row]
    # None denotes full support in the quartic long-division check.
    QUARTIC["check_row"](n, WIDTH, sign, None, row)
    return {"one_norm": value, "coefficients": row, "count_up_to_sign": count}


def record(n, sign, basis, width_eight_norm):
    assert len(basis) == 2
    u, v = BASE["reduce_plane"](*basis)
    dot = BASE["dot"]
    norm = BASE["norm_one"]
    a, b, c = dot(u, u), dot(u, v), dot(v, v)
    plucker = minors(u, v)
    determinant = a * c - b * b
    assert gcd(*plucker) == 1 and determinant == sum(m * m for m in plucker) > 0
    ceiling = max(norm(u), norm(v))
    candidates = sorted(BASE["short_vectors"]((u, v), ceiling), key=norm)
    first = minimum_witness(n, sign, candidates)
    independent = [row for row in candidates if any(minors(first["coefficients"], row))]
    second = minimum_witness(n, sign, independent)
    assert gcd(*minors(first["coefficients"], second["coefficients"])) == 1

    omission_norms = []
    for j in range(WIDTH + 1):
        line = BASE["combine"](u, v[j], v, -u[j])
        content = gcd(*line)
        assert content
        row = [coefficient // content for coefficient in line]
        QUARTIC["check_row"](n, WIDTH, sign, j, row)
        omission_norms.append(norm(row))
    assert first["one_norm"] < second["one_norm"] < width_eight_norm < min(omission_norms)
    return {
        "n": n,
        "sign": sign,
        "reduced_basis": [u, v],
        "gram_entries": [a, b, c],
        "covolume_squared": determinant,
        "one_norm_ceiling": ceiling,
        "candidates_up_to_sign": len(candidates),
        "first": first,
        "second": second,
        "omission_norms": omission_norms,
        "width_eight_generator_norm": width_eight_norm,
    }


if __name__ == "__main__":
    seed = QUARTIC["multiply"](QUARTIC["P"], QUARTIC["P2"])
    results = []
    for n in EXPONENTS:
        _, kernels = BASE["row_system"](seed, n, WIDTH)
        for control, basis in zip(QUARTIC["records"](n, WIDTH - 1), kernels):
            results.append(record(n, control["sign"], basis, control["one_norm"]))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"Computed both minima and all ten omission norms in {len(results)} lattices.")
