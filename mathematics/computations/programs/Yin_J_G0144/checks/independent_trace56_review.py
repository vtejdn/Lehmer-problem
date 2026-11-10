"""Independent exact preparation and fixed auxiliary-bound review.

No solver is imported or run.  The author builder and saved controls are
comparison targets, not oracles for the independent polynomial arithmetic.
"""

from fractions import Fraction as Q
from functools import lru_cache, reduce
import argparse
import json
from math import gcd, lcm, prod
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
ROOT_INPUT = HERE.parent / "Yin_J_G0156" / "inputs" / "primitive_root_diagnostics.json"
CORE_INPUT = HERE.parent / "Yin_J_G0156" / "inputs" / "degree_core_mass_states.json"
F = [1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1]
ORDERS = [6, 4, 14, 12, 15, 30, 60]


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def equal(left, right):
    assert json.dumps(left, sort_keys=True, separators=(",", ":")) == json.dumps(
        right, sort_keys=True, separators=(",", ":"))


def pair(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0)+(q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def multiply(p, q):
    answer = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            answer[i+j] += a*b
    return trim(answer)


def divide(p, q):
    remainder = list(map(Q, trim(p)))
    q = trim(q)
    assert q[-1]
    quotient = [Q(0)]*max(1, len(remainder)-len(q)+1)
    while any(remainder) and len(remainder) >= len(q):
        shift, coefficient = len(remainder)-len(q), remainder[-1]/q[-1]
        quotient[shift] += coefficient
        for j, value in enumerate(q):
            remainder[shift+j] -= coefficient*value
        remainder = trim(remainder)
    return trim(quotient), remainder


def evaluate(p, t):
    value = Q(0)
    for a in reversed(p):
        value = value*t+a
    return value


def primitive(p):
    p = list(map(Q, trim(p)))
    denominator = lcm(*(v.denominator for v in p))
    values = [int(v*denominator) for v in p]
    common = reduce(gcd, values, 0)
    return [v//common for v in values] if common else [0]


def sturm(p):
    p = primitive(p)
    derivative = primitive([i*p[i] for i in range(1, len(p))])
    chain = [p, derivative]
    while any(chain[-1]):
        _, remainder = divide(chain[-2], chain[-1])
        if not any(remainder):
            break
        chain.append(primitive([-v for v in remainder]))
    return chain


def variations(chain, t):
    values = [evaluate(p, t) for p in chain]
    signs = [1 if value > 0 else -1 for value in values if value]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def roots(chain, a, b):
    return variations(chain, a)-variations(chain, b)


def irreducible_mod_two(p):
    n = len(p)-1
    integer = sum((value % 2) << i for i, value in enumerate(p))
    assert integer.bit_length() == n+1
    remainders = []
    # A proper factorization has a factor of degree <= floor(n/2).
    for divisor in range(2, 2**(n//2+1)):
        remainder = integer
        while remainder.bit_length() >= divisor.bit_length():
            remainder ^= divisor << (remainder.bit_length()-divisor.bit_length())
        assert remainder, (p, divisor)
        remainders.append([divisor, remainder])
    return remainders


def basis():
    polynomials = [[2], [0, 1]]
    for k in range(2, 29):
        polynomials.append(add([0]+polynomials[k-1], [-x for x in polynomials[k-2]]))
    polynomials[0] = [1]
    return polynomials


BASIS = basis()


def trace(p):
    assert p == p[::-1] and len(p) % 2
    n = len(p)//2
    answer = [p[n]]
    for k in range(1, n+1):
        answer = add(answer, [p[n-k]*v for v in BASIS[k]])
    return answer


def to_free(p):
    work = add(p, [-v for v in BASIS[28]])
    answer = []
    for degree in range(27, -1, -1):
        coefficient = work[degree] if degree < len(work) else Q(0)
        answer.append(Q(coefficient))
        work = add(work, [-coefficient*x for x in BASIS[degree]])
    assert not any(work)
    return answer


@lru_cache(None)
def cyclotomic(n):
    polynomial = [-1]+[0]*(n-1)+[1]
    for d in range(1, n):
        if n % d == 0:
            polynomial, remainder = divide(polynomial, cyclotomic(d))
            assert not any(remainder) and all(x.denominator == 1 for x in polynomial)
            polynomial = list(map(int, polynomial))
    return polynomial


def prepare_reference(data):
    equal(data["source_parent"], {"native_input": "../Yin_J_G0156/inputs/primitive_root_diagnostics.json",
                                  "observation": 11542, "arm": "dp_closure", "seed": 32,
                                  "proposal": 448, "whole_variable_change": "z -> -z"})
    source = read(ROOT_INPUT)
    witness = source["lower_tail_witnesses"]["11542"]
    observation = dict(zip(source["observation_fields"], source["observations"][11542]))
    assert (observation["arm"], observation["seed"], observation["proposal"]) == ("dp_closure", 32, 448)
    proposal = witness["exact_proposal"]
    assert proposal["proposal"] == 448
    assert proposal["generation"]["mutation"]["delta_coefficients_ascending"] == [0]*28+[1]+[0]*28
    old_parent = proposal["generation"]["parent"]["coefficients_ascending"]
    parent = [(-1)**i*x for i, x in enumerate(old_parent)]
    product = [(-1)**i*x for i, x in enumerate(F)]
    for order in ORDERS:
        product = multiply(product, cyclotomic(order))
    assert product == parent and max(map(abs, parent)) == 2
    equal(data["F_ascending"], F)
    equal(data["parent_cyclotomic_orders"], ORDERS)
    equal(data["parent_ascending"], parent)
    equal(data["formal_parameters"], {"seed": 56003, "threads": 1, "node_cap": 100000, "wall_seconds_from_prelaunch": 120})
    assert (data["protocol"], data["degree"], data["trace_degree"], data["height"]) == ("S10-fixed-D56-all-real-trace-cell", 56, 28, 4)
    q = trace(parent)
    equal(q, data["parent_trace_ascending"])
    free = parent[1:29]
    equal(data["parent_free_descending"], free)
    assert to_free(q) == list(map(Q, free))
    groups = read(CORE_INPUT)["target_partitions"][0]["core_groups"]
    assert any(g["core_coefficients_ascending"] == F for g in groups)
    h = next(g["core_coefficients_ascending"] for g in groups if len(g["core_coefficients_ascending"]) == 19)
    equal(h, data["H_ascending"])
    cores = {"qL": trace([(-1)**i*x for i, x in enumerate(F)]), "qH": trace(h),
             "qH_opposite": trace([(-1)**i*x for i, x in enumerate(h)])}
    irreducibility = {}
    for name, polynomial in cores.items():
        equal(polynomial, data[name+"_ascending"])
        chain = sturm(polynomial)
        assert len(chain[-1]) == 1
        actual = {"inner_roots": roots(chain, Q(-2), Q(2)),
                  "positive_outer_roots": roots(chain, Q(2), Q(61, 30)),
                  "negative_outer_roots": roots(chain, Q(-61, 30), Q(-2)),
                  "at_minus_two": int(evaluate(polynomial, -2)), "at_two": int(evaluate(polynomial, 2))}
        equal(actual, data["core_sign_and_irreducibility_controls"][name])
        assert actual["inner_roots"] == len(polynomial)-2
        assert actual["positive_outer_roots"] == (0 if name == "qH_opposite" else 1)
        assert actual["negative_outer_roots"] == (1 if name == "qH_opposite" else 0)
        if name != "qH_opposite":
            irreducibility[name] = irreducible_mod_two(polynomial)
    chain = sturm(q)
    assert len(chain[-1]) == 1 and roots(chain, Q(-2), Q(2)) == 27
    assert roots(chain, Q(2), Q(61, 30)) == 1
    nodes, steps = [Q(-2)], []
    count_left = variations(chain, Q(-2))
    for target in range(1, 27):
        lo, hi = Q(-2), Q(2)
        for step in range(1, 257):
            middle = (lo+hi)/2
            count = count_left-variations(chain, middle)
            if evaluate(q, middle) and count == target:
                nodes.append(middle)
                steps.append(step)
                break
            if count > target:
                hi = middle
            else:
                lo = middle
        else:
            raise AssertionError("separator rule did not finish")
    nodes += [Q(2), Q(61, 30)]
    equal([pair(x) for x in nodes], data["nodes"])
    equal(steps, data["separator_bisection_steps"])
    assert all(a < b for a, b in zip(nodes, nodes[1:]))
    assert [variations(chain, x) for x in nodes] == data["parent_sturm_variations_at_nodes"] == list(range(28, -1, -1))
    rows, scalings = [], []
    columns = [*reversed(BASIS[:28]), BASIS[28]]
    for i, node in enumerate(nodes):
        values = [(-1)**i*evaluate(column, node) for column in columns]
        denominator = lcm(*(x.denominator for x in values))
        integers = [int(value*denominator) for value in values]
        common = reduce(gcd, integers, 0)
        rows.append([x//common for x in integers])
        scalings.append(pair(Q(denominator, common)))
        assert all(type(x) is int for x in rows[-1]) and Q(*scalings[-1]) > 0
    equal(rows, data["strict_sign_integer_rows"])
    equal(scalings, data["strict_sign_positive_scalings"])
    vertices, weights = [], []
    for omitted, node in enumerate(nodes):
        polynomial = [Q(1)]
        for i, point in enumerate(nodes):
            if i != omitted:
                polynomial = multiply(polynomial, [-point, 1])
        coordinates = to_free(polynomial)
        vertices.append(coordinates)
        for i, point in enumerate(nodes):
            assert (evaluate(polynomial, point) != 0) == (i == omitted)
        weights.append(evaluate(q, node)/evaluate(polynomial, node))
    equal([[pair(x) for x in v] for v in vertices], data["vertices_free_descending"])
    equal([pair(x) for x in weights], data["parent_lagrange_weights"])
    assert all(x > 0 for x in weights) and sum(weights) == 1
    assert [sum(w*v[j] for w, v in zip(weights, vertices)) for j in range(28)] == free
    ceiling = lambda x: -((-x.numerator)//x.denominator)
    bounds = [[max(-4, ceiling(min(v[j] for v in vertices))), min(4, max(v[j] for v in vertices).__floor__())] for j in range(28)]
    equal(bounds, data["closed_simplex_height_box_integer_bounds"])
    remainders = {}
    for name in ("qL", "qH"):
        core = cores[name]
        dimension = len(core)-1
        vectors = []
        for polynomial in [BASIS[28], *reversed(BASIS[:28])]:
            _, remainder = divide(polynomial, core)
            assert all(x.denominator == 1 for x in remainder)
            vectors.append([int(remainder[i]) if i < len(remainder) else 0 for i in range(dimension)])
        constants = vectors[0]
        matrix = [[v[i] for v in vectors[1:]] for i in range(dimension)]
        limits, branches = [], []
        for i, (constant, row) in enumerate(zip(constants, matrix)):
            lo = constant+sum(a*(l if a >= 0 else u) for a, (l, u) in zip(row, bounds))
            hi = constant+sum(a*(u if a >= 0 else l) for a, (l, u) in zip(row, bounds))
            limits.append([lo, hi])
            for sign in (1, -1):
                minimum = lo if sign == 1 else -hi
                m = max(0, 1-minimum)
                branch = {"component": i, "sign": sign, "big_M": m, "coefficients": [sign*a for a in row],
                          "binary_coefficient": -m, "rhs": 1-m-sign*constant}
                # Inactive branch is automatic on the box; active means the
                # signed integer remainder is at least one.
                assert minimum >= 1-m
                assert branch["rhs"]+m+sign*constant == 1
                branches.append(branch)
        expected = {"core": core, "constants": constants, "rows": matrix, "component_bounds": limits,
                    "nonzero_branches": branches, "selector_constraint": "sum of this core's binary selectors >= 1"}
        equal(expected, data["remainder_maps"][name])
        remainders[name] = expected
    controls = {}
    for name, vector in (("parent", free), ("observed_center_plus_one_child", [*free[:-1], free[-1]+1])):
        signs = [sum(a*b for a, b in zip(row, [*vector, 1])) for row in rows]
        rems = {key: [c+sum(a*b for a, b in zip(row, vector)) for c, row in zip(m["constants"], m["rows"])]
                for key, m in remainders.items()}
        nonzero = {key: any(v) for key, v in rems.items()}
        accepted = min(signs) >= 1 and all(nonzero.values())
        expected = {"accepted": accepted, "box": True, "strict_signs": min(signs) >= 1, "sign_integer_values": signs,
                    "failed_sign_indices": [i for i, v in enumerate(signs) if v < 1],
                    "remainders": rems, "nonzero_remainders": nonzero,
                    "reason": "exact_cell_and_old_core_exclusion" if accepted else "sign_or_old_core_fiber"}
        equal(expected, data["controls"][name])
        controls[name] = {"strict_signs": expected["strict_signs"], "failed_sign_indices": expected["failed_sign_indices"],
                          "remainders": rems, "accepted": accepted}
    child = [1, *free[:-1], free[-1]+1, *reversed(free[:-1]), 1]
    assert child == [(-1)**i*x for i, x in enumerate(proposal["coefficients_ascending"])]
    assert Q(6, 5)+Q(5, 6) == nodes[-1]
    return {"source_parent_and_two_actual_core_identities": True,
            "independent_mod_two_irreducibility_remainders": irreducibility,
            "nodes": [pair(x) for x in nodes], "parent_sturm_variations": list(range(28, -1, -1)),
            "exact_strict_rows": 29, "exact_simplex_vertices": 29, "positive_parent_weights": True,
            "integer_coordinate_bounds": bounds, "affine_remainder_dimensions": [5, 9],
            "big_M_integer_disjunction_branches": sum(len(m["nonzero_branches"]) for m in remainders.values()),
            "controls": controls, "formal_solver_runs": 0}


def interval_product(a, b):
    candidates = [x*y for x in a for y in b]
    return min(candidates), max(candidates)


def interval_pairs(interval):
    return [pair(x) for x in interval]


def decimal_outward(interval):
    scale = 10**12
    lo = interval[0].numerator*scale//interval[0].denominator
    hi = -((-interval[1].numerator*scale)//interval[1].denominator)
    def render(n):
        whole, fraction = divmod(abs(n), scale)
        return ("-" if n < 0 else "")+str(whole)+"."+str(fraction).rjust(12, "0")
    return [render(lo), render(hi)]


def resultant_reference(data):
    saved = read(OUTPUT / "trace56_resultant.json")
    assert saved["schema"] == "trace56-resultant-vertex-bound-1"
    assert len(saved["roots"]) == 5
    a = data["qL_ascending"]
    nodes = [Q(*p) for p in data["nodes"]]
    coarse = [(Q(-2), Q(-3, 2)), (Q(-3, 2), Q(-1)), (Q(-1), Q(0)), (Q(0), Q(1)), (Q(2), Q(5, 2))]
    equal(irreducible_mod_two(a), saved["binary_factor_checks_divisor_remainder"])
    equal([interval_pairs(interval) for interval in coarse], saved["coarse_root_brackets"])
    assert saved["root_bisections_per_bracket"] == 80
    maxima = []
    for root, initial in enumerate(coarse):
        lo, hi = initial
        assert evaluate(a, lo)*evaluate(a, hi) < 0
        for _ in range(80):
            middle = (lo+hi)/2
            assert evaluate(a, middle)
            if evaluate(a, middle)*evaluate(a, lo) < 0:
                hi = middle
            else:
                lo = middle
        assert hi-lo == (initial[1]-initial[0])/2**80
        assert evaluate(a, lo)*evaluate(a, hi) < 0
        assert all(not lo <= t <= hi for t in nodes)
        intervals, absolute = [], []
        for omitted in range(29):
            value = (Q(1), Q(1))
            for i, node in enumerate(nodes):
                if i != omitted:
                    value = interval_product(value, (lo-node, hi-node))
            intervals.append(value)
            absolute.append((min(map(abs, value)) if value[0]*value[1] > 0 else Q(0), max(map(abs, value))))
        maximum = max(v[0] for v in absolute), max(v[1] for v in absolute)
        maxima.append(maximum)
        record = saved["roots"][root]
        assert record["root_index"] == root
        equal(record["root_bracket"], interval_pairs((lo, hi)))
        equal(record["vertex_value_intervals"], [interval_pairs(v) for v in intervals])
        equal(record["maximum_absolute_interval"], interval_pairs(maximum))
        equal(record["maximum_absolute_decimal_enclosure"], decimal_outward(maximum))
        equal(record["lower_maximizer_indices"], [i for i, v in enumerate(absolute) if v[0] == maximum[0]])
        equal(record["upper_maximizer_indices"], [i for i, v in enumerate(absolute) if v[1] == maximum[1]])
    product = prod(v[0] for v in maxima), prod(v[1] for v in maxima)
    equal(saved["nodes"], data["nodes"])
    equal(saved["qL_coefficients_ascending"], a)
    equal(saved["product_interval"], interval_pairs(product))
    equal(saved["product_decimal_enclosure"], decimal_outward(product))
    assert product[0] > 537718784 > 1
    assert saved["status"] == "simple_maximum_product_criterion_insufficient"
    scope = saved["fixed_input_scope"]
    for key in ("protocol", "source_parent", "parent_trace_ascending", "parent_cyclotomic_orders"):
        equal(scope[key], data[key])
    return {"five_exact_root_brackets": True, "bisections_each": 80, "vertex_interval_pairs": 145,
            "all_saved_rational_intervals_and_maximizers_match": True,
            "maximum_decimal_enclosures": [decimal_outward(v) for v in maxima],
            "product_decimal_enclosure": decimal_outward(product),
            "product_lower_bound_exceeds_one": True,
            "conclusion": "The fixed separate-maximum sufficient criterion fails; no feasibility or cell-exclusion conclusion.",
            "new_nodes_common_weight_optimization_or_solver": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT / "independent_trace56_preparation_review.json")
    destination = parser.parse_args().output
    if destination.exists():
        raise FileExistsError(destination)
    data = read(HERE / "trace56_cell.json")
    result = {"scope": "Independent frozen preparation and fixed resultant auxiliary review only.",
              "preparation": prepare_reference(data), "resultant": resultant_reference(data),
              "formal_solver_search": "not run"}
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
