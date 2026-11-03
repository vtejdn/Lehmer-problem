"""Author-only exact finite divisor-ideal certificate for Yin D_G0032.

The complete parameter and proof declaration predates this source in D_G0032.
No floating point value supplies a mathematical comparison. The supervisor's
timer is operational metadata only. Independent verification is a separate job.
"""

from __future__ import annotations

from fractions import Fraction as F
import json
import math
import os
from pathlib import Path
import subprocess
import sys


PROGRAM = Path(__file__).resolve().parent
REPOSITORY = next(parent for parent in PROGRAM.parents if (parent / "repository/config.json").is_file())
ROOT = REPOSITORY / "mathematics/computations/outputs" / PROGRAM.name
PRIMES = (2, 3, 5, 7, 11)
BITS = 96
SCALE = 1 << BITS
THETAS = (F(9, 10), F(99, 100))
CAPS = (F(1, 4), F(1, 2))
RUN_LIMIT_SECONDS = 180


def publish(filename, payload):
    ROOT.mkdir(parents=True, exist_ok=True)
    destination = ROOT / filename
    temporary = destination.with_name("." + destination.name + ".partial")
    try:
        temporary.write_text(json.dumps(payload, indent=1) + "\n", encoding="utf-8")
        temporary.replace(destination)
    finally:
        temporary.unlink(missing_ok=True)


def rat(x):
    x = F(x)
    return [str(x.numerator), str(x.denominator)]


def interval(box):
    assert box[0] <= box[1]
    return {"lower": rat(box[0]), "upper": rat(box[1])}


def ceil_div(a, b):
    assert a >= 0 and b > 0
    return (a + b - 1) // b


def sqrt_box(x):
    x = F(x)
    assert x > 0
    j = math.isqrt((x.numerator * SCALE * SCALE) // x.denominator)
    assert j * j * x.denominator <= x.numerator * SCALE * SCALE
    assert (j + 1) ** 2 * x.denominator > x.numerator * SCALE * SCALE
    assert j > 0
    return (F(j, SCALE), F(j + 1, SCALE)), str(j)


def all_ideals():
    ideals = [0, 1]
    counts = [len(ideals)]
    for n in range(1, len(PRIMES) + 1):
        shift = 1 << (n - 1)
        ideals = [i0 | (i1 << shift) for i0 in ideals for i1 in ideals
                  if i1 & ~i0 == 0]
        assert len(set(ideals)) == len(ideals)
        counts.append(len(ideals))
    for ideal in ideals:
        for m in range(1 << len(PRIMES)):
            if not (ideal >> m) & 1:
                continue
            h = m
            while True:
                assert (ideal >> h) & 1
                if h == 0:
                    break
                h = (h - 1) & m
    return sorted(ideals), counts


def worker():
    labels = 1 << len(PRIMES)
    divisors = [math.prod(p for i, p in enumerate(PRIMES) if m & (1 << i))
                for m in range(labels)]
    weights = [math.prod(p - 1 for i, p in enumerate(PRIMES) if m & (1 << i))
               for m in range(labels)]
    assert len(set(divisors)) == labels and max(divisors) == 2310
    kernel = []
    kernel_lo, kernel_hi = [], []
    for m, d in enumerate(divisors):
        j = math.isqrt(d * SCALE * SCALE)
        assert j * j <= d * SCALE * SCALE < (j + 1) ** 2
        lo = SCALE * SCALE // (j + 1)
        hi = ceil_div(SCALE * SCALE, j)
        assert F(lo, SCALE) <= F(SCALE, j + 1)
        assert F(hi, SCALE) >= F(SCALE, j)
        kernel_lo.append(lo)
        kernel_hi.append(hi)
        kernel.append({"label": m, "order": d, "totient": weights[m],
                       "floor_scaled_sqrt": str(j),
                       "reciprocal_scaled": [str(lo), str(hi)]})

    def coeff(members0, members1=None):
        out = [0] * labels
        if members1 is None:
            for a_pos, a in enumerate(members0):
                for b in members0[a_pos:]:
                    out[a | b] += weights[a] * weights[b] * (1 if a == b else 2)
        else:
            for a in members0:
                for b in members1:
                    out[a | b] += weights[a] * weights[b]
        return out

    def energy_bounds(co):
        return (sum(c * k for c, k in zip(co, kernel_lo)),
                sum(c * k for c, k in zip(co, kernel_hi)))

    ideals, counts = all_ideals()
    rows, native_rows = {}, []
    for ideal in ideals:
        if ideal == 0:
            continue
        members = [m for m in range(labels) if (ideal >> m) & 1]
        mass = sum(weights[m] for m in members)
        co = coeff(members)
        assert sum(co) == mass * mass
        elo, ehi = energy_bounds(co)
        jw = math.isqrt(mass * SCALE * SCALE)
        assert jw * jw <= mass * SCALE * SCALE < (jw + 1) ** 2
        rb = (F(elo, mass * (jw + 1)), F(ehi, mass * jw))
        eb = (F(elo, SCALE), F(ehi, SCALE))
        assert 0 < rb[0] <= rb[1] and 0 < eb[0] <= eb[1]
        rows[ideal] = {"members": members, "mass": mass, "coeff": co,
                       "energy": eb, "ratio": rb}
        native_rows.append({"ideal_mask": ideal, "labels": members,
                            "orders": [divisors[m] for m in members],
                            "mass": mass, "lcm_coefficients": co,
                            "energy_scaled": [str(elo), str(ehi)],
                            "floor_scaled_sqrt_mass": str(jw),
                            "ratio": interval(rb)})

    def maximum(masks):
        assert masks
        lower = max(rows[m]["ratio"][0] for m in masks)
        upper = max(rows[m]["ratio"][1] for m in masks)
        possible = [m for m in masks if rows[m]["ratio"][1] >= lower]
        unique = len(possible) == 1
        gap = None
        if unique and len(masks) > 1:
            winner = possible[0]
            runner_upper = max(rows[m]["ratio"][1] for m in masks if m != winner)
            gap = rows[winner]["ratio"][0] - runner_upper
            assert gap > 0
        return {"bounds": interval((lower, upper)), "possible_masks": possible,
                "unique_strict_maximum": unique,
                "separation_lower_bound": None if gap is None else rat(gap)}, (lower, upper)

    global_max, global_box = maximum(list(rows))
    threshold_masks, threshold_rows, mask = [], [], 0
    for m in sorted(range(labels), key=lambda m: divisors[m]):
        mask |= 1 << m
        assert mask in rows
        threshold_masks.append(mask)
        threshold_rows.append({"cutoff": divisors[m], "ideal_mask": mask})
    threshold_max, threshold_box = maximum(threshold_masks)
    assert len(threshold_masks) == labels

    base_data, base_boxes, slices = {}, {}, {}
    for ip, p in enumerate(PRIMES):
        pbit = 1 << ip
        allowed = sum(1 << m for m in range(labels) if not m & pbit)
        base_masks = [i for i in rows if i & ~allowed == 0]
        bm, bb = maximum(base_masks)
        base_boxes[p] = bb
        base_data[str(p)] = {"ambient_order": 2310 // p, "allowed_label_mask": allowed,
                             "nonempty_ideal_count": len(base_masks),
                             "all_ideal_masks": base_masks, "maximum": bm}
        for ideal in rows:
            i0 = ideal & allowed
            i1 = sum(1 << m for m in range(labels)
                     if not m & pbit and (ideal >> (m | pbit)) & 1)
            assert i0 in rows and i1 & ~i0 == 0 and (i1 == 0 or i1 in rows)
            assert rows[ideal]["mass"] == rows[i0]["mass"] + (p - 1) * (
                rows[i1]["mass"] if i1 else 0)
            slices[p, ideal] = i0, i1

    correlation_data = {}

    def correlation(p, ideal):
        key = f"{p}:{ideal}"
        if key in correlation_data:
            return key, correlation_data[key]["_rho"]
        i0, i1 = slices[p, ideal]
        assert i1 != 0
        r0, r1 = rows[i0], rows[i1]
        co = coeff(r0["members"], r1["members"])
        assert sum(co) == r0["mass"] * r1["mass"]
        elo, ehi = energy_bounds(co)
        cross = F(elo, SCALE), F(ehi, SCALE)
        product = r0["energy"][0] * r1["energy"][0], r0["energy"][1] * r1["energy"][1]
        sqrt_lo, jl = sqrt_box(product[0])
        sqrt_hi, jh = sqrt_box(product[1])
        rho = cross[0] / sqrt_hi[1], cross[1] / sqrt_lo[0]
        assert 0 < rho[0] <= rho[1]
        # The PSD kernel ensures rho<=1 analytically; no truncation to one is used.
        assert rho[0] <= 1
        correlation_data[key] = {
            "prime": p, "full_ideal_mask": ideal, "slice0_mask": i0,
            "slice1_mask": i1, "mass0": r0["mass"], "mass1": r1["mass"],
            "mass_ratio": rat(F(r1["mass"], r0["mass"])),
            "cross_lcm_coefficients": co,
            "cross_energy_scaled": [str(elo), str(ehi)],
            "energy_product": interval(product),
            "floor_scaled_roots_of_product_endpoints": [jl, jh],
            "correlation": interval(rho), "_rho": rho}
        return key, rho

    tests = []
    for p in PRIMES:
        cp = base_boxes[p]
        for theta in THETAS:
            for cap in CAPS:
                included, ambiguous = [], []
                empty_small_slice, over_cap, excluded = 0, 0, 0
                rho_upper = F(0)
                rho_upper_key = None
                for ideal in rows:
                    i0, i1 = slices[p, ideal]
                    if i1 == 0:
                        empty_small_slice += 1
                        continue
                    x = F(rows[i1]["mass"], rows[i0]["mass"])
                    if x > cap:
                        over_cap += 1
                        continue
                    rr = rows[i0]["ratio"], rows[i1]["ratio"]
                    if any(rb[1] < theta * cp[0] for rb in rr):
                        excluded += 1
                        continue
                    certain = all(rb[0] >= theta * cp[1] for rb in rr)
                    key, rh = correlation(p, ideal)
                    (included if certain else ambiguous).append(key)
                    if rh[1] > rho_upper:
                        rho_upper, rho_upper_key = rh[1], key
                assert empty_small_slice + over_cap + excluded + len(included) + len(ambiguous) == len(rows)
                tests.append({"prime": p, "theta": rat(theta), "mass_ratio_cap": rat(cap),
                              "empty_slice1_count": empty_small_slice,
                              "over_cap_count": over_cap, "definitely_excluded_count": excluded,
                              "definitely_included_keys": included,
                              "ambiguous_keys": ambiguous,
                              "possible_count": len(included) + len(ambiguous),
                              "possible_correlation_upper": None if rho_upper_key is None else rat(rho_upper),
                              "upper_attaining_record": rho_upper_key})

    maximizer_slices = []
    for ideal in global_max["possible_masks"]:
        for p in PRIMES:
            i0, i1 = slices[p, ideal]
            maximizer_slices.append({"full_ideal_mask": ideal, "prime": p,
                                     "slice0_mask": i0, "slice1_mask": i1,
                                     "correlation_key": correlation(p, ideal)[0] if i1 else None})
    for record in correlation_data.values():
        del record["_rho"]
    certificate = {
        "identity": "Yin_J_G0095", "author_role": "author computation, not independent verification",
        "parameters": {"primes": PRIMES, "ambient": 2310, "s": rat(F(1, 2)),
                       "t": rat(F(3, 2)), "bits": BITS, "scale": str(SCALE),
                       "thetas": [rat(x) for x in THETAS], "mass_ratio_caps": [rat(x) for x in CAPS]},
        "ideal_counts_by_number_of_primes": counts,
        "empty_ideal_mask": 0, "all_ideal_count": len(ideals),
        "kernel_and_square_root_records": kernel, "all_nonempty_candidate_records": native_rows,
        "global_maximum": global_max, "numeric_thresholds": threshold_rows,
        "threshold_maximum": threshold_max,
        "global_lower_exceeds_threshold_upper": global_box[0] > threshold_box[1],
        "unique_global_maximum_is_threshold": (len(global_max["possible_masks"]) == 1 and
                                                global_max["possible_masks"][0] in threshold_masks),
        "four_prime_base_maxima": base_data,
        "predeclared_near_extremal_tests": tests,
        "possible_global_maximizer_slices": maximizer_slices,
        "correlation_records": correlation_data,
        "limits": "Only the declared finite squarefree ambient and boxes; no universal bound or polynomial realization."
    }
    publish("certificate.json", certificate)
    print(json.dumps({"counts": counts, "global_possible_masks": global_max["possible_masks"],
                      "unique_global": global_max["unique_strict_maximum"],
                      "unique_global_is_threshold": certificate["unique_global_maximum_is_threshold"],
                      "nonthreshold_strictly_better": certificate["global_lower_exceeds_threshold_upper"],
                      "correlation_records": len(correlation_data),
                      "test_possible_counts": [r["possible_count"] for r in tests]}, indent=2))


def supervise():
    command = [sys.executable, str(Path(__file__).resolve()), "--worker"]
    try:
        result = subprocess.run(command, cwd=PROGRAM, capture_output=True, text=True,
                                timeout=RUN_LIMIT_SECONDS,
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
