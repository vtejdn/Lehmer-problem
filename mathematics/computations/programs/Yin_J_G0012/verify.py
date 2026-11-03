"""Independent exact checks for the single Mercat/Bre20 binary counterexample.

Uses pairwise integer polynomial division, not the author's recursive power
table, and standard-library rational arithmetic. Numerical roots and library
factorizations are exploratory fields, not premises or comparison gates.
"""
from fractions import Fraction as F
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_REPOSITORY = next(parent for parent in _J_PROGRAM.parents if (parent / "repository/config.json").is_file())
_J_OUTPUT = _J_REPOSITORY / "mathematics/computations/outputs" / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

BASE = _J_OUTPUT
data = json.loads((BASE / "probe.json").read_text(encoding="utf-8"))
p = [1, 1, 1, -1, 1, 1, 1]


def remainder(poly):
    work = list(poly)
    for degree in range(len(work) - 1, 5, -1):
        leading = work[degree]
        for j, coefficient in enumerate(p):
            work[degree - 6 + j] -= leading * coefficient
    return tuple(work[:6] + [0] * max(0, 6 - len(work)))


assert data["coefficients_ascending"] == p
powers = []
for j in range(8):
    powers.append(list(remainder([0] * j + [1])))
assert powers == data["powers_mod_p"]
words = [[(mask >> j) & 1 for j in range(8)] for mask in range(256)]
pairs = []
comparisons = 0
for a in range(256):
    for b in range(a + 1, 256):
        comparisons += 1
        if not any(remainder([x - y for x, y in zip(words[a], words[b])])):
            pairs.append([a, b])
assert comparisons == 32640
assert pairs == data["nontrivial_fibers_bitmask_low_power_first"]
assert len(pairs) == 4
assert len({a for pair in pairs for a in pair}) == 8
assert data["support_size_n8"] == 256 - len(pairs) == 252


def trace_value(u):
    return ((u + 1) * u - 2) * u - 3


def radius_value(measure, u):
    x = measure + 1 / measure
    return (x + 2 - u * u - u) * x + 1 - u * u


cert = data["final_certificate"]
ul, uu = F(cert["u_lower"]), F(cert["u_upper"])
ml, mu = F(cert["M_lower"]), F(cert["M_upper"])
assert (ul, uu, ml, mu) == (F(3867, 2500), F(1547, 1000), F(511, 256), F(2))
values = {
    "T_u_lower": trace_value(ul),
    "T_u_upper": trace_value(uu),
    "G_Mlower_ulower": radius_value(ml, ul),
    "G_Mupper_uupper": radius_value(mu, uu),
}
for key, value in values.items():
    assert value == F(cert[key]), (key, value, cert[key])
assert values["T_u_lower"] < 0 < values["T_u_upper"]
assert values["G_Mlower_ulower"] < 0 < values["G_Mupper_uupper"]
assert 0 < ul < uu < F(8, 5) < 2
assert 6 - uu * uu - uu > 0  # dF/dx at x=2, worst u.
assert 1 < ml < mu == 2
assert ml**8 > 252
# Preserve and check the unsuccessful coarse endpoint instead of hiding it.
coarse = data["discarded_coarse_upper_u"]
assert trace_value(F(coarse["u"])) == F(coarse["T"])
assert radius_value(F(2), F(coarse["u"])) == F(coarse["G_M2"]) < 0
for row in data["initial_endpoint_probes"]:
    u = F(row["u"])
    assert trace_value(u) == F(row["T"])
    for measure, value in row["G"].items():
        assert radius_value(F(measure), u) == F(value)
assert F(19961, 10000)**8 - 252 == F(data["initial_M8_minus_252"])

result = {
        "status": "passed",
    "scope": "one degree-six input, all unordered pairs of eight binary digits; exact rational endpoint signs",
    "pairwise_division_checks": comparisons,
    "power_remainder_checks": 8,
    "support_size_n8": 252,
    "collision_pairs": pairs,
    "rational_certificate": {key: str(value) for key, value in values.items()},
    "strict_M_lower_power_check": "(511/256)^8 > 252",
    "exploratory_fields_not_certified": ["numerical_roots_exploratory_default_15_digits", "factor_list_exact_library_output", "discriminant"],
    "limits": "The written proof owns irreducibility, root locations, norm interpretation and all-length consequence; no uniform near-one claim.",
}
(BASE / "verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
