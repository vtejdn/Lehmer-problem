"""Exact vertex-evaluation resultant bound for one fixed degree-56 trace cell.

This is an author calculation, not an independent review of trace56_cell.
The input is the frozen 29-node mathematical cell in trace56_cell.json.
No random sampling, factorization, MILP or numerical root solver is used.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
QL = (3, 4, -5, -5, 1, 1)  # Ascending, positive-exterior-root convention.
BISECTIONS = 80
COARSE_BRACKETS = (
    (Fraction(-2), Fraction(-3, 2)),
    (Fraction(-3, 2), Fraction(-1)),
    (Fraction(-1), Fraction(0)),
    (Fraction(0), Fraction(1)),
    (Fraction(2), Fraction(5, 2)),
)


def evaluate(polynomial, point):
    value = Fraction(0)
    for coefficient in reversed(polynomial):
        value = point * value + coefficient
    return value


def multiply_intervals(left, right):
    products = [a * b for a in left for b in right]
    return min(products), max(products)


def absolute_interval(interval):
    lower, upper = interval
    maximum = max(abs(lower), abs(upper))
    minimum = 0 if lower <= 0 <= upper else min(abs(lower), abs(upper))
    return Fraction(minimum), maximum


def rational_record(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def interval_record(interval):
    return [rational_record(value) for value in interval]


def decimal_enclosure(interval, places=12):
    """Outward-rounded decimal endpoints, using integer arithmetic only."""
    scale = 10**places
    lower, upper = interval
    below = (lower.numerator * scale) // lower.denominator
    above = -((-upper.numerator * scale) // upper.denominator)

    def render(integer):
        sign = "-" if integer < 0 else ""
        whole, fraction = divmod(abs(integer), scale)
        return f"{sign}{whole}.{fraction:0{places}d}"

    return [render(below), render(above)]


def irreducibility_and_brackets():
    """Check irreducibility mod 2 and five disjoint real-root brackets."""
    modulus = sum((coefficient % 2) << i for i, coefficient in enumerate(QL))
    assert modulus.bit_length() == 6
    remainders = []
    # Any reducible degree-five polynomial has a factor of degree at most two.
    for divisor in range(2, 8):
        remainder = modulus
        while remainder.bit_length() >= divisor.bit_length():
            remainder ^= divisor << (remainder.bit_length() - divisor.bit_length())
        assert remainder
        remainders.append([divisor, remainder])

    brackets = []
    for original_lower, original_upper in COARSE_BRACKETS:
        lower, upper = original_lower, original_upper
        lower_value, upper_value = evaluate(QL, lower), evaluate(QL, upper)
        assert lower_value * upper_value < 0
        for _ in range(BISECTIONS):
            midpoint = (lower + upper) / 2
            value = evaluate(QL, midpoint)
            assert value  # The irreducible degree-five polynomial has no rational root.
            if value * lower_value > 0:
                lower, lower_value = midpoint, value
            else:
                upper, upper_value = midpoint, value
        assert lower_value * upper_value < 0
        assert upper - lower == (original_upper - original_lower) / 2**BISECTIONS
        brackets.append((lower, upper))
    assert all(a[1] < b[0] for a, b in zip(brackets, brackets[1:]))
    # Five distinct roots exhaust degree five, so each bracket contains one simple root.
    return remainders, brackets


def vertex_value(nodes, omitted, bracket):
    """Enclose V_i(alpha)=product_{k != i}(alpha-s_k) by exact intervals."""
    interval = (Fraction(1), Fraction(1))
    for index, node in enumerate(nodes):
        if index != omitted:
            factor = (bracket[0] - node, bracket[1] - node)
            interval = multiply_intervals(interval, factor)
    return interval


def calculate(nodes):
    assert len(nodes) == 29
    assert all(a < b for a, b in zip(nodes, nodes[1:]))
    assert nodes[0] == -2 and nodes[-2] == 2 and nodes[-1] == Fraction(61, 30)
    binary_remainders, brackets = irreducibility_and_brackets()
    assert all(not (lower <= node <= upper)
               for lower, upper in brackets for node in nodes)
    root_records, maxima = [], []
    for root_index, bracket in enumerate(brackets):
        intervals = [vertex_value(nodes, omitted, bracket) for omitted in range(29)]
        absolute = [absolute_interval(interval) for interval in intervals]
        bound = (max(item[0] for item in absolute), max(item[1] for item in absolute))
        maxima.append(bound)
        root_records.append({
            "root_index": root_index,
            "root_bracket": interval_record(bracket),
            "vertex_value_intervals": [interval_record(item) for item in intervals],
            "maximum_absolute_interval": interval_record(bound),
            "maximum_absolute_decimal_enclosure": decimal_enclosure(bound),
            "lower_maximizer_indices": [i for i, item in enumerate(absolute) if item[0] == bound[0]],
            "upper_maximizer_indices": [i for i, item in enumerate(absolute) if item[1] == bound[1]],
        })
    product_interval = (prod(item[0] for item in maxima), prod(item[1] for item in maxima))
    if product_interval[1] < 1:
        status = "sufficient_bound_forces_qL_divisor"
    elif product_interval[0] >= 1:
        status = "simple_maximum_product_criterion_insufficient"
    else:
        status = "fixed_enclosure_does_not_decide_criterion"
    return {
        "schema": "trace56-resultant-vertex-bound-1",
        "qL_coefficients_ascending": list(QL),
        "nodes": [rational_record(node) for node in nodes],
        "root_bisections_per_bracket": BISECTIONS,
        "binary_factor_checks_divisor_remainder": binary_remainders,
        "coarse_root_brackets": [interval_record(item) for item in COARSE_BRACKETS],
        "roots": root_records,
        "product_interval": interval_record(product_interval),
        "product_decimal_enclosure": decimal_enclosure(product_interval),
        "status": status,
        "scope": "One fixed 29-node simplex; no height-box restriction or common-weight optimization.",
        "arithmetic": "Exact integer and Fraction arithmetic, with fixed 80-step root bisection and outward decimal rendering.",
        "review_scope": "Author calculation; not an independent mathematical or implementation review.",
    }


def load_fixed_cell(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["protocol"] == "S10-fixed-D56-all-real-trace-cell"
    assert (data["degree"], data["trace_degree"]) == (56, 28)
    assert data["qL_ascending"] == list(QL)
    assert data["parent_cyclotomic_orders"] == [6, 4, 14, 12, 15, 30, 60]
    source = data["source_parent"]
    assert (source["observation"], source["arm"], source["seed"], source["proposal"]) == (
        11542, "dp_closure", 32, 448)
    assert source["whole_variable_change"] == "z -> -z"
    nodes = []
    for pair in data["nodes"]:
        assert len(pair) == 2 and all(type(value) is int for value in pair)
        assert pair[1] > 0
        nodes.append(Fraction(*pair))
    parent = data["parent_trace_ascending"]
    assert len(parent) == 29 and parent[-1] == 1
    assert all(type(coefficient) is int for coefficient in parent)
    assert all((-1)**index * evaluate(parent, node) > 0
               for index, node in enumerate(nodes))
    remainder = parent[:]
    for degree in range(28, 4, -1):
        leading = remainder[degree]
        for index, coefficient in enumerate(QL):
            remainder[degree - 5 + index] -= leading * coefficient
    assert not any(remainder)
    return nodes, {
        "protocol": data["protocol"],
        "source_parent": source,
        "parent_trace_ascending": parent,
        "parent_cyclotomic_orders": data["parent_cyclotomic_orders"],
        "checks": "Exact qL identity, specified source locator, ordered-node input, strict parent signs and qL divisibility.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=HERE / "trace56_cell.json")
    parser.add_argument("--output", type=Path, default=OUTPUT / "trace56_resultant.json")
    arguments = parser.parse_args()
    if arguments.output.exists():
        raise FileExistsError("Use a fresh output path; existing results are not overwritten.")
    nodes, input_scope = load_fixed_cell(arguments.input)
    result = calculate(nodes)
    result["fixed_input_scope"] = input_scope
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    with arguments.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(result["status"])
    print("Product enclosure:", result["product_decimal_enclosure"])
    for record in result["roots"]:
        print("Root", record["root_index"], "maximum enclosure:",
              record["maximum_absolute_decimal_enclosure"])


if __name__ == "__main__":
    main()
