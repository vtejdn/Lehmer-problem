"""Independent exact J95 reproduction; never imports or calls main.py.

Same declared N=2310, half-moment, B96, theta 9/10 and 99/100,
mass caps 1/4 and 1/2. Different enumeration by immediate predecessors,
ordered arithmetic lcm coefficients, bisection of reciprocal roots and W^3.
The author certificate is validated separately at every saved exact field.
The supervisor enforces a 180-second limit and reports failures directly.
"""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
import json
from math import gcd
import os
from pathlib import Path
import subprocess
import sys


PROGRAM = Path(__file__).resolve().parent
REPOSITORY = next(parent for parent in PROGRAM.parents if (parent / "repository/config.json").is_file())
GROUP = REPOSITORY / "mathematics/computations/outputs" / PROGRAM.name
PRIMES = (2, 3, 5, 7, 11)
BITS = 96
S = 2**BITS
LIMIT = 180
THETAS = (Q(9, 10), Q(99, 100))
CAPS = (Q(1, 4), Q(1, 2))


def publish(filename, payload):
    GROUP.mkdir(parents=True, exist_ok=True)
    destination = GROUP / filename
    temporary = destination.with_name("." + destination.name + ".partial")
    try:
        temporary.write_text(json.dumps(payload, indent=1) + "\n", encoding="utf-8")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def rat(q):
    q = Q(q)
    return [str(q.numerator), str(q.denominator)]


def readrat(x):
    assert isinstance(x, list) and len(x) == 2
    assert int(x[1]) > 0
    q = Q(int(x[0]), int(x[1]))
    assert rat(q) == x
    return q


def box(x):
    lo, hi = readrat(x["lower"]), readrat(x["upper"])
    assert lo <= hi
    return lo, hi


def encode(x):
    assert x[0] <= x[1]
    return {"lower": rat(x[0]), "upper": rat(x[1])}


def validate_root(j, value):
    j, value = int(j), Q(value)
    target = value.numerator * S * S
    assert j >= 0
    assert j*j*value.denominator <= target < (j+1)**2*value.denominator
    return j


@lru_cache(maxsize=None)
def root(value):
    """Exact B96 bisection; exact dyadic roots use a point interval."""
    value = Q(value)
    assert value > 0
    target, denominator = value.numerator*S*S, value.denominator
    integer_part = target // denominator
    left = 0
    right = 1 << ((integer_part.bit_length()+1)//2)
    while right*right*denominator <= target:
        right *= 2
    while right-left > 1:
        middle = (left+right)//2
        if middle*middle*denominator <= target:
            left = middle
        else:
            right = middle
    assert left*left*denominator <= target < right*right*denominator
    if left*left*denominator == target:
        return Q(left, S), Q(left, S)
    return Q(left, S), Q(right, S)


def downsets(n):
    """Choose vertices in topological numeric order, not nested-pair recursion."""
    count = 1 << n
    predecessors = []
    for m in range(count):
        predecessors.append(sum(1 << (m ^ (1 << i))
                                for i in range(n) if m & (1 << i)))
    output = []

    def visit(m, ideal):
        if m == count:
            output.append(ideal)
            return
        visit(m+1, ideal)
        if ideal & predecessors[m] == predecessors[m]:
            visit(m+1, ideal | (1 << m))

    visit(0, 0)
    assert len(output) == len(set(output))
    for ideal in output:
        for m in range(count):
            if ideal & (1 << m):
                assert ideal & predecessors[m] == predecessors[m]
    return sorted(output)


def maximum(masks, ratios):
    masks = list(masks)
    assert masks
    lower = max(ratios[m][0] for m in masks)
    upper = max(ratios[m][1] for m in masks)
    possible = [m for m in masks if ratios[m][1] >= lower]
    gap = None
    if len(possible) == 1 and len(masks) > 1:
        winner = possible[0]
        gap = ratios[winner][0] - max(ratios[m][1] for m in masks if m != winner)
        assert gap > 0
    return {"bounds": encode((lower, upper)), "possible_masks": possible,
            "unique_strict_maximum": len(possible) == 1,
            "separation_lower_bound": None if gap is None else rat(gap)}


def worker():
    data = json.loads((GROUP / "certificate.json").read_text(encoding="utf-8"))
    assert data["identity"] == "Yin_J_G0095"
    assert data["parameters"] == {
        "primes": list(PRIMES), "ambient": 2310, "s": rat(Q(1, 2)),
        "t": rat(Q(3, 2)), "bits": BITS, "scale": str(S),
        "thetas": [rat(t) for t in THETAS], "mass_ratio_caps": [rat(c) for c in CAPS]}
    levels = [downsets(n) for n in range(6)]
    counts = [len(a) for a in levels]
    assert data["ideal_counts_by_number_of_primes"] == counts
    assert data["all_ideal_count"] == len(levels[-1])
    assert data["empty_ideal_mask"] == 0
    masks = levels[-1][1:]
    assert levels[-1][0] == 0
    orders, weights = [], []
    for label in range(32):
        order, weight = 1, 1
        for ip, p in enumerate(PRIMES):
            if label & (1 << ip):
                order *= p
                weight *= p-1
        orders.append(order)
        weights.append(weight)
    order_to_label = {v: i for i, v in enumerate(orders)}
    assert len(order_to_label) == 32 and max(orders) == 2310
    lcm_labels = [[order_to_label[a*b//gcd(a, b)] for b in orders] for a in orders]
    author_kernel, own_kernel = [], []
    assert len(data["kernel_and_square_root_records"]) == 32
    for m, record in enumerate(data["kernel_and_square_root_records"]):
        assert record["label"] == m
        assert record["order"] == orders[m] and record["totient"] == weights[m]
        j = validate_root(record["floor_scaled_sqrt"], orders[m])
        lo, hi = S*S//(j+1), (S*S+j-1)//j
        assert record["reciprocal_scaled"] == [str(lo), str(hi)]
        author_kernel.append((lo, hi))
        r = root(Q(1, orders[m]))
        own_kernel.append((int(r[0]*S), int(r[1]*S)))

    @lru_cache(maxsize=None)
    def members(ideal):
        return tuple(m for m in range(32) if ideal & (1 << m))

    @lru_cache(maxsize=None)
    def coefficients(i0, i1):
        c = [0]*32
        for a in members(i0):
            for b in members(i1):
                c[lcm_labels[a][b]] += weights[a]*weights[b]
        return tuple(c)

    def energy(co, kernel):
        return tuple(sum(c*k[e] for c, k in zip(co, kernel)) for e in (0, 1))

    def as_energy(e):
        return Q(e[0], S), Q(e[1], S)

    original_ratios, own_ratios, original_energy, own_energy, masses = {}, {}, {}, {}, {}
    independent_rows = []
    native = data["all_nonempty_candidate_records"]
    assert [r["ideal_mask"] for r in native] == masks
    for ideal, record in zip(masks, native):
        mm = members(ideal)
        mass = sum(weights[m] for m in mm)
        masses[ideal] = mass
        co = coefficients(ideal, ideal)
        assert sum(co) == mass*mass
        assert record["labels"] == list(mm)
        assert record["orders"] == [orders[m] for m in mm]
        assert record["mass"] == mass
        assert record["lcm_coefficients"] == list(co)
        e = energy(co, author_kernel)
        assert record["energy_scaled"] == [str(x) for x in e]
        j = validate_root(record["floor_scaled_sqrt_mass"], mass)
        expected = Q(e[0], mass*(j+1)), Q(e[1], mass*j)
        assert box(record["ratio"]) == expected
        original_ratios[ideal] = expected
        original_energy[ideal] = as_energy(e)
        independent_e = energy(co, own_kernel)
        own_energy[ideal] = as_energy(independent_e)
        denominator = root(Q(mass**3))
        rr = own_energy[ideal][0]/denominator[1], own_energy[ideal][1]/denominator[0]
        own_ratios[ideal] = rr
        independent_rows.append({"ideal_mask": ideal, "mass": mass,
                                 "lcm_coefficients": list(co),
                                 "energy_scaled": [str(x) for x in independent_e],
                                 "sqrt_mass_cubed": encode(denominator), "ratio": encode(rr)})

    original_max = maximum(masks, original_ratios)
    own_max = maximum(masks, own_ratios)
    assert original_max == data["global_maximum"]
    assert own_max["possible_masks"] == original_max["possible_masks"]
    thresholds = [{"cutoff": d,
                   "ideal_mask": sum(1 << m for m, v in enumerate(orders) if v <= d)}
                  for d in sorted(orders)]
    assert len({r["ideal_mask"] for r in thresholds}) == 32
    assert thresholds == data["numeric_thresholds"]
    threshold_masks = [r["ideal_mask"] for r in thresholds]
    assert all(m in masses for m in threshold_masks)
    original_threshold = maximum(threshold_masks, original_ratios)
    own_threshold = maximum(threshold_masks, own_ratios)
    assert original_threshold == data["threshold_maximum"]
    assert own_threshold["possible_masks"] == original_threshold["possible_masks"]
    strict_threshold = box(original_max["bounds"])[0] > box(original_threshold["bounds"])[1]
    is_threshold = len(original_max["possible_masks"]) == 1 and original_max["possible_masks"][0] in threshold_masks
    assert data["global_lower_exceeds_threshold_upper"] == strict_threshold
    assert data["unique_global_maximum_is_threshold"] == is_threshold

    slices, base_original, base_own, base_results = {}, {}, {}, {}
    for ip, p in enumerate(PRIMES):
        allowed = sum(1 << m for m, d in enumerate(orders) if d % p != 0)
        base_masks = [i for i in masks if i & ~allowed == 0]
        # Projection onto the four surviving prime coordinates is also checked.
        projected = []
        for ideal in base_masks:
            small_mask = 0
            for label in members(ideal):
                small_label = (label & ((1 << ip)-1)) | ((label >> (ip+1)) << ip)
                small_mask |= 1 << small_label
            projected.append(small_mask)
        assert sorted(projected) == levels[4][1:]
        bm = maximum(base_masks, original_ratios)
        own_bm = maximum(base_masks, own_ratios)
        assert own_bm["possible_masks"] == bm["possible_masks"]
        expected = {"ambient_order": 2310//p, "allowed_label_mask": allowed,
                    "nonempty_ideal_count": len(base_masks), "all_ideal_masks": base_masks,
                    "maximum": bm}
        assert data["four_prime_base_maxima"][str(p)] == expected
        base_original[p] = box(bm["bounds"])
        base_own[p] = box(own_bm["bounds"])
        base_results[str(p)] = {"ambient_order": 2310//p, "all_ideal_masks": base_masks,
                                "maximum": own_bm}
        seen_pairs = set()
        for ideal in masks:
            i0 = sum(1 << m for m in members(ideal) if orders[m] % p != 0)
            i1 = sum(1 << order_to_label[orders[m]//p]
                     for m in members(ideal) if orders[m] % p == 0)
            assert i0 in masses and (i1 == 0 or i1 in masses) and i1 & ~i0 == 0
            assert masses[ideal] == masses[i0]+(p-1)*(masses[i1] if i1 else 0)
            slices[p, ideal] = i0, i1
            assert (i0, i1) not in seen_pairs
            seen_pairs.add((i0, i1))
        expected_pairs = {(i0, i1) for i0 in base_masks for i1 in [0]+base_masks
                          if i1 & ~i0 == 0}
        assert seen_pairs == expected_pairs

    original_rhos, own_rhos, own_correlation_records = {}, {}, {}

    def correlation(p, ideal):
        key = f"{p}:{ideal}"
        if key in original_rhos:
            return key
        r = data["correlation_records"][key]
        i0, i1 = slices[p, ideal]
        assert i1 != 0
        assert r["prime"] == p and r["full_ideal_mask"] == ideal
        assert r["slice0_mask"] == i0 and r["slice1_mask"] == i1
        assert r["mass0"] == masses[i0] and r["mass1"] == masses[i1]
        assert readrat(r["mass_ratio"]) == Q(masses[i1], masses[i0])
        co = coefficients(i0, i1)
        assert sum(co) == masses[i0]*masses[i1]
        assert r["cross_lcm_coefficients"] == list(co)
        e = energy(co, author_kernel)
        assert r["cross_energy_scaled"] == [str(v) for v in e]
        product = (original_energy[i0][0]*original_energy[i1][0],
                   original_energy[i0][1]*original_energy[i1][1])
        assert box(r["energy_product"]) == product
        jl = validate_root(r["floor_scaled_roots_of_product_endpoints"][0], product[0])
        jh = validate_root(r["floor_scaled_roots_of_product_endpoints"][1], product[1])
        rho = Q(e[0], jh+1), Q(e[1], jl)
        assert box(r["correlation"]) == rho and rho[0] <= 1
        original_rhos[key] = rho
        ce = as_energy(energy(co, own_kernel))
        ep = own_energy[i0][0]*own_energy[i1][0], own_energy[i0][1]*own_energy[i1][1]
        lower_root, upper_root = root(ep[0]), root(ep[1])
        independent_rho = ce[0]/upper_root[1], ce[1]/lower_root[0]
        assert 0 < independent_rho[0] <= independent_rho[1]
        assert independent_rho[0] <= 1
        own_rhos[key] = independent_rho
        own_correlation_records[key] = {"prime": p, "full_ideal_mask": ideal,
            "slice0_mask": i0, "slice1_mask": i1,
            "mass_ratio": rat(Q(masses[i1], masses[i0])),
            "cross_lcm_coefficients": list(co), "cross_energy": encode(ce),
            "energy_product": encode(ep), "product_lower_root": encode(lower_root),
            "product_upper_root": encode(upper_root), "correlation": encode(independent_rho)}
        return key

    def all_tests(ratios, base_boxes, rhos):
        tests = []
        for p in PRIMES:
            cp = base_boxes[p]
            for theta in THETAS:
                for cap in CAPS:
                    counts_by_status = [0, 0, 0]
                    included, ambiguous = [], []
                    best_upper, best_key = Q(0), None
                    for ideal in masks:
                        i0, i1 = slices[p, ideal]
                        if i1 == 0:
                            counts_by_status[0] += 1
                            continue
                        if Q(masses[i1], masses[i0]) > cap:
                            counts_by_status[1] += 1
                            continue
                        rr = ratios[i0], ratios[i1]
                        if min(b[1] for b in rr) < theta*cp[0]:
                            counts_by_status[2] += 1
                            continue
                        key = correlation(p, ideal)
                        certain = min(b[0] for b in rr) >= theta*cp[1]
                        (included if certain else ambiguous).append(key)
                        if rhos[key][1] > best_upper:
                            best_upper, best_key = rhos[key][1], key
                    assert sum(counts_by_status)+len(included)+len(ambiguous) == len(masks)
                    tests.append({"prime": p, "theta": rat(theta), "mass_ratio_cap": rat(cap),
                        "empty_slice1_count": counts_by_status[0], "over_cap_count": counts_by_status[1],
                        "definitely_excluded_count": counts_by_status[2],
                        "definitely_included_keys": included, "ambiguous_keys": ambiguous,
                        "possible_count": len(included)+len(ambiguous),
                        "possible_correlation_upper": None if best_key is None else rat(best_upper),
                        "upper_attaining_record": best_key})
        return tests

    author_tests = all_tests(original_ratios, base_original, original_rhos)
    assert author_tests == data["predeclared_near_extremal_tests"]
    own_tests = all_tests(own_ratios, base_own, own_rhos)
    for a, b in zip(author_tests, own_tests):
        for field in ("empty_slice1_count", "over_cap_count", "definitely_excluded_count",
                      "definitely_included_keys", "ambiguous_keys", "possible_count"):
            assert a[field] == b[field]
    maximizer_slices = []
    for ideal in original_max["possible_masks"]:
        for p in PRIMES:
            i0, i1 = slices[p, ideal]
            maximizer_slices.append({"full_ideal_mask": ideal, "prime": p,
                "slice0_mask": i0, "slice1_mask": i1,
                "correlation_key": correlation(p, ideal) if i1 else None})
    assert maximizer_slices == data["possible_global_maximizer_slices"]
    assert set(original_rhos) == set(data["correlation_records"])
    # A coarse exact separation is retained only if independently certified.
    winner = own_max["possible_masks"][0]
    assert len(own_max["possible_masks"]) == 1
    nonwinner_upper = max(own_ratios[m][1] for m in masks if m != winner)
    assert own_ratios[winner][0] > nonwinner_upper
    assert winner == (1 << 31)-1 and masses[winner] == 1830
    assert Q(1342, 1000) < own_ratios[winner][0]
    assert own_ratios[winner][1] < Q(1343, 1000)
    assert own_ratios[winner][0]-nonwinner_upper > Q(1, 250)
    for test in own_tests:
        assert test["ambiguous_keys"] == []
        if readrat(test["theta"]) == Q(99, 100):
            assert test["possible_count"] == 0
        else:
            bound = Q(15, 16) if readrat(test["mass_ratio_cap"]) == Q(1, 4) else Q(49, 50)
            assert readrat(test["possible_correlation_upper"]) < bound
    summary = {"all_ideal_count": len(levels[-1]), "nonempty_candidates": len(masks),
        "counts": counts, "unique_global_masks": own_max["possible_masks"],
        "unique_threshold_masks": own_threshold["possible_masks"],
        "correlation_records": len(own_rhos),
        "test_possible_counts": [t["possible_count"] for t in own_tests],
        "all_author_exact_fields_checked": True,
        "same_finite_classifications_under_independent_enclosures": True,
        "coarse_ratio_bounds": [rat(Q(1342, 1000)), rat(Q(1343, 1000))],
        "strict_global_gap_exceeds": rat(Q(1, 250)),
        "ninety_percent_rho_upper_bounds_by_cap": {
            "1/4": rat(Q(15, 16)), "1/2": rat(Q(49, 50))},
        "ninety_nine_percent_boxes_all_empty": True}
    result = {"identity": "Yin_J_G0095", "role": "independent exact reproduction",
        "parameters": data["parameters"],
        "method": "Topological predecessor enumeration; ordered integer gcd/lcm coefficients; reciprocal and mass-cubed bisection roots; no author-code import or call.",
        "summary": summary,
        "independent_reciprocal_kernel_scaled": [[str(a), str(b)] for a, b in own_kernel],
        "all_independent_nonempty_candidate_records": independent_rows,
        "global_maximum": own_max, "numeric_thresholds": thresholds,
        "threshold_maximum": own_threshold, "four_prime_base_maxima": base_results,
        "predeclared_near_extremal_tests": own_tests,
        "possible_global_maximizer_slices": maximizer_slices,
        "correlation_records": own_correlation_records,
        "limits": "Only N2310, squarefree divisors, s1/2, B96, the declared theta/cap tests. No universal inequality, other ambient, or actual polynomial realization."}
    publish("verification.json", result)
    print(json.dumps(summary, indent=2))


def supervise():
    command = [sys.executable, str(Path(__file__).resolve()), "--worker"]
    try:
        result = subprocess.run(command, cwd=PROGRAM, capture_output=True, text=True,
                                timeout=LIMIT,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
    except subprocess.TimeoutExpired as error:
        for value, stream in ((error.stdout, sys.stdout), (error.stderr, sys.stderr)):
            if value:
                stream.write(value.decode(errors="replace") if isinstance(value, bytes) else value)
        raise SystemExit("Calculation timed out; no completed replacement is claimed.") from error
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    if result.returncode:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    if sys.argv[1:] == ["--worker"]:
        worker()
    elif not sys.argv[1:]:
        supervise()
    else:
        raise SystemExit("No undeclared arguments are accepted.")
