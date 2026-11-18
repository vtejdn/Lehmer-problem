"""Certify the small-prime graph obstructions and a reciprocal degree-six measure bound."""

from itertools import product
from math import comb
from pathlib import Path
from tempfile import TemporaryDirectory
import json

from sympy import Poly, ZZ, cyclotomic_poly, symbols


X = symbols("x")
T = Poly(X, X, domain=ZZ)
G = T**3 - T - 1
B = 1 - T**2 - T**3
# At primitive roots of these orders, -G/B is sign times the indicated power.
TORSION_VALUES = {
    1: (-1, 0), 2: (1, 0), 3: (-1, 2), 5: (-1, 3),
    8: (1, 1), 12: (1, 2), 18: (1, 4), 30: (1, 9),
}


def coefficients(poly):
    return list(map(int, poly.all_coeffs()))


def graph_certificate(prime):
    one = Poly(1, X, modulus=prime)
    torsion = one
    for order, (sign, power) in TORSION_VALUES.items():
        phi = cyclotomic_poly(order, X, polys=True)
        if not (G + sign*T**power*B).rem(phi).is_zero:
            raise ArithmeticError(f"Incorrect torsion value at order {order}")
        if order % prime:
            torsion *= phi.set_modulus(prime)
    invalid = (T*G*B).set_modulus(prime)

    def classify(poly):
        unit, factors = poly.factor_list()
        restored = one * unit
        records = []
        for factor, multiplicity in factors:
            restored *= factor**multiplicity
            if invalid.rem(factor).is_zero:
                kind = "outside_unit_graph"
            elif torsion.rem(factor).is_zero:
                kind = "torsion_coordinate"
            else:
                kind = "other"
            records.append({"coefficients_descending": coefficients(factor),
                            "multiplicity": multiplicity, "kind": kind})
        if restored != poly:
            raise ArithmeticError("Factor product differs from its input")
        return records

    numerator = G.compose(T**prime)*B**prime + (-G)**prime * B.compose(T**prime)
    correction = numerator.exquo_ground(prime).set_modulus(prime)
    obstruction = classify(correction)
    if any(record["kind"] == "other" for record in obstruction):
        raise ArithmeticError("An additional unit-graph correction root occurs")
    slopes = []
    for slope in range(prime):
        critical = (T*(G.diff()*B-G*B.diff())-slope*G*B).set_modulus(prime)
        factors = classify(critical)
        outside = max((r["multiplicity"] for r in factors if r["kind"] == "other"),
                      default=0)
        budget = sum((len(r["coefficients_descending"])-1)*r["multiplicity"]
                     for r in factors if r["kind"] == "torsion_coordinate")
        if outside + 1 >= prime or budget > 6:
            raise ArithmeticError(f"Insufficient critical-point bound at {(prime, slope)}")
        slopes.append({"slope": slope, "factors": factors,
                       "maximum_other_multiplicity": outside,
                       "torsion_degree_with_multiplicities": budget})
    return {"prime": prime, "correction_descending": coefficients(correction),
            "correction_factors": obstruction, "slopes": slopes}


def graeffe(poly):
    """Ascending even-degree coefficients of the polynomial on squared roots."""
    result = [0]*len(poly)
    for parity, sign in ((0, 1), (1, -1)):
        part = poly[parity::2]
        for i, a in enumerate(part):
            for j, b in enumerate(part):
                result[i+j+parity] += sign*a*b
    return result


def small_reciprocals(degree):
    n = degree//2
    binomials = [comb(degree, i) for i in range(degree+1)]
    ranges = []
    for i in range(1, n+1):
        bound = 27*binomials[i]//20
        ranges.append(range(-bound, bound+1))
    powers = [1, 2, 4, 8, 16, 32, 64]
    bounds = [[c*27**k//20**k for c in binomials] for k in powers]
    totals = [0]*len(powers)
    certificates = []
    cyclotomics = {}
    for order in range(1, 2*degree**2+1):
        phi = cyclotomic_poly(order, X, polys=True)
        if phi.degree() <= degree:
            cyclotomics[order] = phi
    for interior in product(*ranges):
        half = (1, *interior)
        polynomial = half + half[-2::-1]
        powered = polynomial
        for stage, limit in enumerate(bounds):
            if any(abs(c) > cap for c, cap in zip(powered, limit)):
                break
            totals[stage] += 1
            if stage+1 < len(bounds):
                powered = graeffe(powered)
        else:
            # Reciprocal coefficients read the same in either order.
            remainder = Poly.from_list(polynomial, X, domain=ZZ)
            orders = []
            for order, phi in cyclotomics.items():
                while remainder.rem(phi).is_zero:
                    orders.append(order)
                    remainder = remainder.exquo(phi)
            if not remainder.is_one:
                raise ArithmeticError(f"Unresolved polynomial {polynomial}")
            certificates.append({"coefficients_descending": polynomial,
                                 "cyclotomic_orders_with_repetition": orders})
    return {"degree": degree, "powers": powers, "stage_counts": totals,
            "survivors": certificates}


def main():
    local = [graph_certificate(prime) for prime in (3, 5, 7)]
    low = [small_reciprocals(degree) for degree in (2, 4, 6)]
    if local[0]["slopes"][0]["torsion_degree_with_multiplicities"] != 0:
        raise ArithmeticError("The three-adic slope-zero exception persists")
    group = Path(__file__).resolve().parent
    output = group.parents[1]/"outputs"/group.name/"certificate.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    scratch = group.parents[3]/".tmp"
    scratch.mkdir(exist_ok=True)
    with TemporaryDirectory(dir=scratch) as directory:
        checked = Path(directory)/output.name
        checked.write_text(json.dumps({"local": local, "low_degree": low},
                                      separators=(",", ":"))+"\n", encoding="utf-8")
        checked.replace(output)
    for case in local:
        print(case["prime"], [(s["maximum_other_multiplicity"],
                              s["torsion_degree_with_multiplicities"]) for s in case["slopes"]])
    for case in low:
        print(case["degree"], case["stage_counts"])


if __name__ == "__main__":
    main()
