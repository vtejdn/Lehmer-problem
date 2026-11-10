"""Exact preparation and checks for one fixed all-real degree-56 trace cell.

Preparation is not a solver search.  The only selected parent is the sign image
of the retained J156 DP seed32/proposal448 parent.  All arithmetic here is exact.
"""

import argparse
from fractions import Fraction
from functools import reduce
import json
from math import gcd, lcm
from pathlib import Path

from flint import fmpq, fmpq_poly, fmpz_poly
from trace64_cell import chebyshev_basis, dot

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[1] / "outputs" / HERE.name
INPUT = HERE / "trace56_cell.json"
ROOT_INPUT = HERE.parent / "Yin_J_G0156" / "inputs" / "primitive_root_diagnostics.json"
CORE_INPUT = HERE.parent / "Yin_J_G0156" / "inputs" / "degree_core_mass_states.json"
N, HEIGHT = 28, 4
SEED, NODE_CAP, WALL_SECONDS = 56003, 100000, 120
F = [1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1]
ORDERS = [6, 4, 14, 12, 15, 30, 60]
BASIS = chebyshev_basis()[:N + 1]  # The constant element is one, not C_0=2.


def rational(value):
    if isinstance(value, Fraction):
        return value
    return Fraction(int(value.numerator), int(value.denominator))


def pair(value):
    value = rational(value) if not isinstance(value, int) else Fraction(value)
    return [value.numerator, value.denominator]


def fraction(value):
    return Fraction(*value)


def primitive(poly):
    values = [rational(x) for x in poly]
    denominator = lcm(*(x.denominator for x in values))
    integers = [int(x * denominator) for x in values]
    common = reduce(gcd, integers, 0)
    return [x // common for x in integers] if common else []


def sturm(poly):
    a = fmpq_poly(poly)
    b = a.derivative()
    chain = [primitive(a), primitive(b)]
    while b:
        _, remainder = divmod(a, b)
        if not remainder:
            break
        next_poly = primitive(-remainder)
        chain.append(next_poly)
        a, b = b, fmpq_poly(next_poly)
    return chain


def scaled_eval(poly, x):
    numerator, denominator = x.numerator, x.denominator
    result, power = poly[-1], denominator
    for coefficient in reversed(poly[:-1]):
        result = result * numerator + coefficient * power
        power *= denominator
    return result


def variations(chain, x):
    signs = [1 if value > 0 else -1 for poly in chain if (value := scaled_eval(poly, x))]
    return sum(left != right for left, right in zip(signs, signs[1:]))


def root_count(chain, left, right):
    return variations(chain, left) - variations(chain, right)


def trace(polynomial):
    assert polynomial == polynomial[::-1] and len(polynomial) % 2 == 1
    half = len(polynomial) // 2
    result = fmpz_poly([polynomial[half]])
    for k in range(1, half + 1):
        result += polynomial[half - k] * fmpz_poly(BASIS[k])
    return list(map(int, result))


def from_free(free):
    assert len(free) == N
    polynomial = fmpq_poly(BASIS[N])
    for coefficient, basis in zip(free, reversed(BASIS[:N])):
        coefficient = Fraction(coefficient)
        polynomial += fmpq(coefficient.numerator, coefficient.denominator) * fmpq_poly(basis)
    return polynomial


def to_free(polynomial):
    work = fmpq_poly(polynomial)
    assert work.degree() == N and work[N] == 1
    work -= fmpq_poly(BASIS[N])
    descending = []
    for k in range(N - 1, -1, -1):
        coefficient = rational(work[k])
        descending.append(coefficient)
        work -= fmpq(coefficient.numerator, coefficient.denominator) * fmpq_poly(BASIS[k])
    assert not work
    return descending


def whole_polynomial(free):
    return [1, *free, *reversed(free[:-1]), 1]


def separators(poly):
    """First nonroot dyadic bisection point with each desired left-root count."""
    chain = sturm(poly)
    left_count = variations(chain, Fraction(-2))
    selected, steps = [], []
    for target in range(1, 27):
        left, right = Fraction(-2), Fraction(2)
        for step in range(1, 257):
            midpoint = (left + right) / 2
            count = left_count - variations(chain, midpoint)
            if scaled_eval(poly, midpoint) != 0 and count == target:
                selected.append(midpoint)
                steps.append(step)
                break
            # At a simple root, the zero-skipping Sturm variation is the
            # right-hand variation; count includes that root.  The next gap
            # therefore lies to its right when count equals target.
            if count <= target:
                left = midpoint
            else:
                right = midpoint
        else:
            raise ArithmeticError("fixed preparation bisection cap exceeded")
    nodes = [Fraction(-2), *selected, Fraction(2), Fraction(61, 30)]
    assert len(nodes) == 29 and all(a < b for a, b in zip(nodes, nodes[1:]))
    assert all(root_count(chain, a, b) == 1 for a, b in zip(nodes, nodes[1:]))
    return nodes, steps, chain


def sign_rows(nodes):
    rows, scales = [], []
    for i, x in enumerate(nodes):
        # Descending free coefficients, followed by the fixed monic constant.
        values = [Fraction(scaled_eval(b, x), x.denominator ** (len(b) - 1))
                  for b in [*reversed(BASIS[:N]), BASIS[N]]]
        denominator = lcm(*(value.denominator for value in values))
        raw = [int((-1) ** i * denominator * value) for value in values]
        common = reduce(gcd, raw, 0)
        rows.append([value // common for value in raw])
        scales.append(pair(Fraction(denominator, common)))
    return rows, scales


def vertices(nodes):
    result = []
    for omitted in range(len(nodes)):
        polynomial = fmpq_poly([1])
        for j, x in enumerate(nodes):
            if j != omitted:
                polynomial *= fmpq_poly([-fmpq(x.numerator, x.denominator), 1])
        result.append(to_free(polynomial))
    return result


def ceil(value):
    return -((-value.numerator) // value.denominator)


def remainder_map(core, bounds):
    divisor = fmpz_poly(core)
    degree = divisor.degree()
    remainder_vectors = []
    for basis in [BASIS[N], *reversed(BASIS[:N])]:
        _, remainder = divmod(fmpz_poly(basis), divisor)
        remainder_vectors.append([int(remainder[j]) for j in range(degree)])
    constants = remainder_vectors[0]
    rows = [[vector[j] for vector in remainder_vectors[1:]] for j in range(degree)]
    limits, branches = [], []
    for j, (constant, row) in enumerate(zip(constants, rows)):
        lower = constant + sum(min(c * lo, c * hi) for c, (lo, hi) in zip(row, bounds))
        upper = constant + sum(max(c * lo, c * hi) for c, (lo, hi) in zip(row, bounds))
        limits.append([lower, upper])
        for sign in (1, -1):
            minimum = lower if sign == 1 else -upper
            big_m = max(0, 1 - minimum)
            branches.append({"component": j, "sign": sign, "big_M": big_m,
                             "coefficients": [sign * c for c in row],
                             "binary_coefficient": -big_m, "rhs": 1 - big_m - sign * constant})
    return {"core": core, "constants": constants, "rows": rows,
            "component_bounds": limits, "nonzero_branches": branches,
            "selector_constraint": "sum of this core's binary selectors >= 1"}


def exact_check(free, data):
    if len(free) != N or any(type(x) is not int or abs(x) > HEIGHT for x in free):
        return {"accepted": False, "reason": "coefficient_box"}
    values = [dot(row, [*free, 1]) for row in data["strict_sign_integer_rows"]]
    remainders = {name: [constant + dot(row, free) for constant, row in zip(mapping["constants"], mapping["rows"])]
                  for name, mapping in data["remainder_maps"].items()}
    valid_signs = all(value >= 1 for value in values)
    nonzero = {name: any(values) for name, values in remainders.items()}
    return {"accepted": valid_signs and all(nonzero.values()), "box": True,
            "strict_signs": valid_signs, "sign_integer_values": values,
            "failed_sign_indices": [i for i, value in enumerate(values) if value < 1],
            "remainders": remainders, "nonzero_remainders": nonzero,
            "reason": "exact_cell_and_old_core_exclusion" if valid_signs and all(nonzero.values()) else "sign_or_old_core_fiber"}


def prepare():
    original = json.loads(ROOT_INPUT.read_text(encoding="utf-8"))["lower_tail_witnesses"]["11542"]
    proposal = original["exact_proposal"]
    assert proposal["proposal"] == 448 and proposal["generation"]["mutation"]["delta_coefficients_ascending"] == [0] * 28 + [1] + [0] * 28
    old_parent = proposal["generation"]["parent"]["coefficients_ascending"]
    parent = [(-1) ** j * coefficient for j, coefficient in enumerate(old_parent)]
    product = fmpz_poly([(-1) ** j * coefficient for j, coefficient in enumerate(F)])
    for order in ORDERS:
        product *= fmpz_poly.cyclotomic(order)
    assert parent == list(map(int, product)) and max(map(abs, parent)) == 2
    q_parent = trace(parent)
    qL = trace([(-1) ** j * coefficient for j, coefficient in enumerate(F)])
    assert qL == [3, 4, -5, -5, 1, 1]
    groups = json.loads(CORE_INPUT.read_text(encoding="utf-8"))["target_partitions"][0]["core_groups"]
    H = next(group["core_coefficients_ascending"] for group in groups if len(group["core_coefficients_ascending"]) == 19)
    qH = trace(H)
    qH_opposite = trace([(-1) ** j * coefficient for j, coefficient in enumerate(H)])
    core_checks = {}
    for name, core in (("qL", qL), ("qH", qH), ("qH_opposite", qH_opposite)):
        chain = sturm(core)
        core_checks[name] = {"inner_roots": root_count(chain, Fraction(-2), Fraction(2)),
                             "positive_outer_roots": root_count(chain, Fraction(2), Fraction(61, 30)),
                             "negative_outer_roots": root_count(chain, Fraction(-61, 30), Fraction(-2)),
                             "at_minus_two": scaled_eval(core, Fraction(-2)), "at_two": scaled_eval(core, Fraction(2))}
    assert core_checks["qL"]["inner_roots"] == 4 and core_checks["qL"]["positive_outer_roots"] == 1
    assert core_checks["qH"]["inner_roots"] == 8 and core_checks["qH"]["positive_outer_roots"] == 1
    assert core_checks["qH_opposite"]["negative_outer_roots"] == 1 and core_checks["qH_opposite"]["positive_outer_roots"] == 0
    for core in (qL, qH):
        content, factors = fmpz_poly(core).factor()
        assert content == 1 and len(factors) == 1 and factors[0][1] == 1
        assert list(map(int, factors[0][0])) == core
    nodes, steps, chain = separators(q_parent)
    assert root_count(chain, Fraction(-2), Fraction(2)) == 27
    assert root_count(chain, Fraction(2), Fraction(61, 30)) == 1
    assert len(chain[-1]) == 1
    rows, scales = sign_rows(nodes)
    hull = vertices(nodes)
    bounds = [[max(-HEIGHT, ceil(min(vertex[j] for vertex in hull))),
               min(HEIGHT, max(vertex[j] for vertex in hull).__floor__())] for j in range(N)]
    assert all(lo <= hi for lo, hi in bounds)
    free = parent[1:29]
    assert to_free(q_parent) == list(map(Fraction, free)) and list(map(int, from_free(free))) == q_parent
    weights = []
    for i, x in enumerate(nodes):
        numerator = Fraction(scaled_eval(q_parent, x), x.denominator ** N)
        denominator = reduce(lambda a, b: a * b, (x - y for j, y in enumerate(nodes) if i != j), Fraction(1))
        weights.append(numerator / denominator)
    assert all(weight > 0 for weight in weights) and sum(weights) == 1
    assert all(sum(weight * vertex[j] for weight, vertex in zip(weights, hull)) == free[j] for j in range(N))
    data = {"protocol": "S10-fixed-D56-all-real-trace-cell", "degree": 56, "trace_degree": N, "height": HEIGHT,
            "formal_parameters": {"seed": SEED, "threads": 1, "node_cap": NODE_CAP, "wall_seconds_from_prelaunch": WALL_SECONDS},
            "source_parent": {"native_input": "../Yin_J_G0156/inputs/primitive_root_diagnostics.json", "observation": 11542,
                              "arm": "dp_closure", "seed": 32, "proposal": 448, "whole_variable_change": "z -> -z"},
            "known_core_source": "../Yin_J_G0156/inputs/degree_core_mass_states.json target_partitions[0].core_groups",
            "F_ascending": F, "H_ascending": H, "parent_cyclotomic_orders": ORDERS,
            "parent_ascending": parent, "parent_trace_ascending": q_parent, "parent_free_descending": free,
            "qL_ascending": qL, "qH_ascending": qH, "qH_opposite_ascending": qH_opposite,
            "basis": "1,C1,...,C28 with Ck(z+1/z)=z^k+z^-k; free order C27,...,C1,1",
            "separator_rule": "For each target count i=1..26, bisect [-2,2]; choose the first nonroot dyadic midpoint with exactly i parent roots to its left; at a root with count i continue to its right. Hard preparation cap 256 steps per gap.",
            "nodes": [pair(x) for x in nodes], "separator_bisection_steps": steps,
            "parent_sturm_variations_at_nodes": [variations(chain, x) for x in nodes],
            "strict_sign_integer_rows": rows, "strict_sign_positive_scalings": scales,
            "vertices_free_descending": [[pair(value) for value in vertex] for vertex in hull],
            "closed_simplex_height_box_integer_bounds": bounds,
            "parent_lagrange_weights": [pair(weight) for weight in weights],
            "remainder_maps": {name: remainder_map(core, bounds) for name, core in (("qL", qL), ("qH", qH))},
            "core_sign_and_irreducibility_controls": core_checks}
    parent_check = exact_check(free, data)
    child = list(free)
    child[-1] += 1
    child_check = exact_check(child, data)
    assert parent_check["strict_signs"] and not parent_check["nonzero_remainders"]["qL"]
    assert not child_check["strict_signs"]
    assert whole_polynomial(child) == [(-1) ** j * coefficient for j, coefficient in enumerate(proposal["coefficients_ascending"])]
    data["controls"] = {"parent": parent_check, "observed_center_plus_one_child": child_check,
                        "parent_open_simplex_weights_checked": True, "all_vertex_coefficients_reconstructed": True,
                        "preparation_only_no_solver_search": True}
    return data


def check_input(data):
    nodes = list(map(fraction, data["nodes"]))
    assert data["protocol"] == "S10-fixed-D56-all-real-trace-cell"
    assert (data["degree"], data["trace_degree"], data["height"]) == (56, N, HEIGHT)
    assert data["formal_parameters"] == {"seed": SEED, "threads": 1, "node_cap": NODE_CAP, "wall_seconds_from_prelaunch": WALL_SECONDS}
    assert data["F_ascending"] == F and data["parent_cyclotomic_orders"] == ORDERS
    parent = fmpz_poly([(-1) ** j * coefficient for j, coefficient in enumerate(F)])
    for order in ORDERS:
        parent *= fmpz_poly.cyclotomic(order)
    assert list(map(int, parent)) == data["parent_ascending"]
    assert trace(data["parent_ascending"]) == data["parent_trace_ascending"]
    assert trace([(-1) ** j * coefficient for j, coefficient in enumerate(F)]) == data["qL_ascending"]
    assert trace(data["H_ascending"]) == data["qH_ascending"]
    fixed_nodes, steps, _ = separators(data["parent_trace_ascending"])
    assert nodes == fixed_nodes and steps == data["separator_bisection_steps"]
    rows, scales = sign_rows(nodes)
    assert rows == data["strict_sign_integer_rows"] and scales == data["strict_sign_positive_scalings"]
    hull = vertices(nodes)
    assert [[pair(x) for x in vertex] for vertex in hull] == data["vertices_free_descending"]
    bounds = [[max(-HEIGHT, ceil(min(v[j] for v in hull))), min(HEIGHT, max(v[j] for v in hull).__floor__())] for j in range(N)]
    assert bounds == data["closed_simplex_height_box_integer_bounds"]
    for name in ("qL", "qH"):
        assert remainder_map(data[name + "_ascending"], bounds) == data["remainder_maps"][name]
    chain = sturm(data["parent_trace_ascending"])
    assert [variations(chain, x) for x in nodes] == data["parent_sturm_variations_at_nodes"]
    assert all(root_count(chain, a, b) == 1 for a, b in zip(nodes, nodes[1:]))
    assert exact_check(data["parent_free_descending"], data) == data["controls"]["parent"]
    child = list(data["parent_free_descending"])
    child[-1] += 1
    assert exact_check(child, data) == data["controls"]["observed_center_plus_one_child"]
    # Basis vectors verify every affine remainder coefficient independently by
    # polynomial division; this is an identity check, not a candidate scan.
    for free in ([0] * N, *([int(i == j) for i in range(N)] for j in range(N))):
        polynomial = from_free(free)
        for name, mapping in data["remainder_maps"].items():
            _, remainder = divmod(polynomial, fmpq_poly(mapping["core"]))
            assert [int(remainder[j]) for j in range(len(mapping["core"]) - 1)] == [c + dot(row, free) for c, row in zip(mapping["constants"], mapping["rows"])]
    return {"exact_fixed_input_checks": "pass", "nodes": len(nodes), "vertices": len(hull),
            "qH_ascending": data["qH_ascending"], "parent_admitted_to_cell_but_excluded_by_qL": True,
            "center_plus_one_failed_sign_indices": data["controls"]["observed_center_plus_one_child"]["failed_sign_indices"],
            "formal_solver_search": "not run"}


def write_new(path, value):
    if path.exists():
        raise FileExistsError("preserve fixed input or previous result")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "check"))
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        if (args.output or INPUT).exists():
            raise FileExistsError("preserve fixed input")
        data = prepare()
        result = check_input(data)
        write_new(args.output or INPUT, data)
    else:
        result = check_input(json.loads(args.input.read_text(encoding="utf-8")))
        if args.output:
            write_new(args.output, result)
    print(json.dumps(result, indent=2))
