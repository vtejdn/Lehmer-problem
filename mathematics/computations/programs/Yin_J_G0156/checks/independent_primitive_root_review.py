"""Independent review of the fixed D56 post-hoc root diagnostic.

Read the original observations and native evidence.  Use exact multiplication,
rational parsing and descriptive recomputation only: no polynomial
factorization, numerical root solving, worker or sampling call is made.
"""

from collections import Counter, defaultdict
from decimal import Decimal
from fractions import Fraction
from functools import lru_cache, reduce
import gzip
import json
import math
from pathlib import Path
import re
import statistics
import sys

import flint
from flint import arb, acb, ctx, fmpz_poly

HERE = Path(__file__).resolve().parents[1]
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
INPUT = HERE / "inputs"
LABEL = "s10_primitive_core_comparison"
FIELDS = ("arm", "seed", "proposal", "elapsed", "scope", "j", "mutation_size", "requested_mutation_size",
          "B", "endpoint_plus", "endpoint_minus", "gcd_degree", "primary", "cached", "repeated_proposal",
          "certificate_id", "neutral_id", "root_seconds", "factor_seconds")
SCHEDULE = [(arm, seed) for i, seed in enumerate(range(30, 35))
            for arm in (("direct", "dp_closure") if i % 2 == 0 else ("dp_closure", "direct"))]
SOURCE_FORMATS = Counter()
MEASURE_KEYS = ("coefficients_ascending", "core_coefficients_ascending", "measure_interval", "measure_ball",
                "thresholds", "neutral", "precision_bits", "factorization_product_verified",
                "root_count_with_multiplicity", "ranking_resolved", "log_score")
FACTOR_KEYS = ("coefficients_ascending", "measure_interval", "measure_ball", "thresholds",
               "degree", "exponent", "root_count", "cyclotomic")


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def exact(left, right):
    assert json.dumps(left, sort_keys=True, separators=(",", ":")) == json.dumps(
        right, sort_keys=True, separators=(",", ":"))


def events(path):
    with Path(path).open(encoding="utf-8") as stream:
        for line in stream:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                break


NUMBER = re.compile(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?\Z")


def number(text):
    text = text.strip()
    assert NUMBER.fullmatch(text), text
    return Fraction(Decimal(text))


def decimal_ball(text):
    text = text.strip()
    if text.startswith("["):
        assert text.endswith("]")
        text = text[1:-1].strip()
    if "+/-" not in text:
        value = number(text)
        return value, value
    parts = text.split("+/-")
    assert len(parts) == 2
    middle, radius = number(parts[0]) if parts[0].strip() else Fraction(0), number(parts[1])
    assert radius >= 0
    return middle - radius, middle + radius


def complex_parts(text):
    """Parse bracket-aware real/imaginary components independently."""
    if not text.endswith("j"):
        return decimal_ball(text), (Fraction(0), Fraction(0)), "0"
    body, depth, separator = text[:-1], 0, None
    for i, char in enumerate(body):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        if depth == 0 and body[i:i+3] in (" + ", " - "):
            assert separator is None
            separator = i
    assert depth == 0
    if separator is None:
        return (Fraction(0), Fraction(0)), decimal_ball(body), body.strip()
    real = decimal_ball(body[:separator])
    imaginary_text = body[separator+3:].strip()
    imaginary = decimal_ball(imaginary_text)
    if body[separator+1] == "-":
        imaginary = -imaginary[1], -imaginary[0]
        imaginary_text = "-" + imaginary_text
    return real, imaginary, imaginary_text


def reality(interval):
    low, high = interval
    if low > 0 or high < 0:
        return "certified_nonreal"
    return "certified_real" if low == high == 0 else "unknown"


def dyadic(pair):
    mantissa, exponent = pair
    assert type(mantissa) is int and type(exponent) is int
    return Fraction(mantissa * 2**max(exponent, 0), 2**max(-exponent, 0))


def center(interval):
    return float((dyadic(interval[0]) + dyadic(interval[1])) / 2)


def integers(poly):
    return list(map(int, poly))


def printing_checks():
    assert flint.__version__ == "0.9.0" and flint.__FLINT_VERSION__ == "3.6.0"
    assert not ctx.unicode
    old_precision = ctx.prec
    ctx.prec = 128
    values = [arb(0), arb(1), arb(-2), arb((5, -3)),
              arb((2**120+1, -123)), arb((2**110+3, -100), (1, -200)),
              arb((-2**105+7, -100), (1, -180)), arb(0, (1, -160))]
    samples = []
    for value in values:
        rendered = str(value)
        assert rendered == value.str()
        low, high = decimal_ball(rendered)
        midpoint, radius = dyadic(tuple(map(int, value.mid().man_exp()))), dyadic(tuple(map(int, value.rad().man_exp())))
        assert low <= midpoint - radius <= midpoint + radius <= high
        samples.append(rendered)
    pairs = [(arb(1), arb(-2)), (values[4], values[6]), (arb(0), values[6]), (arb(1), arb(0))]
    for real, imag in pairs:
        rendered = str(acb(real, imag))
        rr, ii, _ = complex_parts(rendered)
        for original, bounds in ((real, rr), (imag, ii)):
            m = dyadic(tuple(map(int, original.mid().man_exp())))
            r = dyadic(tuple(map(int, original.rad().man_exp())))
            assert bounds[0] <= m-r <= m+r <= bounds[1]
    ctx.prec = old_precision
    assert reality(decimal_ball("[+/- 1e-12]")) == "unknown"
    assert reality(decimal_ball("0")) == "certified_real"
    assert reality(decimal_ball("[-1e-12 +/- 1e-13]")) == "certified_nonreal"
    return {"python_flint": flint.__version__, "flint": flint.__FLINT_VERSION__,
            "eight_fixed_real_balls_enclosed_by_exact_decimal_parse": True,
            "four_fixed_complex_renderings_checked": True, "examples": samples,
            "scope": "Interface checks only; no root calculation."}


@lru_cache(None)
def phi(order):
    return sum(math.gcd(k, order) == 1 for k in range(1, order+1))


@lru_cache(None)
def cyclotomic(order):
    return fmpz_poly.cyclotomic(order)


def neutral_reference(parent):
    c = parent["neutral_coefficients_ascending"]
    if "neutral_factor_powers" in parent:
        atoms = parent["neutral_factor_powers"]
    else:
        degree = len(c)-1
        assert c == [1] + [0]*(degree-1) + [1]
        atoms = [[m, 1] for m in range(1, 2*degree+1) if (2*degree) % m == 0 and degree % m != 0]
    assert all(type(m) is int and type(e) is int and m > 0 and e > 0 for m, e in atoms)
    assert len({m for m, _ in atoms}) == len(atoms)
    exact_powers = [[m, e*(2 if m in (1, 2) else 1)] for m, e in atoms]
    product = fmpz_poly([1])
    for m, e in exact_powers:
        atom = cyclotomic(m)
        assert atom.degree() == phi(m)
        product *= atom**e
    assert integers(product) == c
    interior = sum((e-1)*phi(m)//2 for m, e in exact_powers if m > 2)
    endpoints = dict(exact_powers)
    assert endpoints.get(1, 0) % 2 == endpoints.get(2, 0) % 2 == 0
    return {"atom_powers": atoms, "irreducible_cyclotomic_powers": exact_powers,
            "degree": sum(phi(m)*e for m, e in exact_powers), "B": interior,
            "endpoint_plus": endpoints.get(1, 0)//2, "endpoint_minus": endpoints.get(2, 0)//2}


def certificate_reference(certificate):
    regions = Counter({"inside": 0, "outside": 0, "meets_one": 0, "cyclotomic_exact": 0})
    scopes, outside, product = [], [], fmpz_poly([1])
    for index, factor in enumerate(certificate["factors"]):
        degree, exponent = factor["degree"], factor["exponent"]
        assert type(exponent) is int and exponent > 0
        assert degree == len(factor["coefficients_ascending"])-1 == factor["root_count"]
        product *= fmpz_poly(factor["coefficients_ascending"])**exponent
        local = Counter()
        if factor["cyclotomic"]:
            assert factor["roots"] == []
            local["cyclotomic_exact"] = degree
        else:
            for ordinal, root in enumerate(factor["roots"]):
                multiplicity, region = root["multiplicity"], root["region"]
                assert type(multiplicity) is int and multiplicity > 0
                assert region in ("inside", "outside", "meets_one")
                local[region] += multiplicity
                bounds = decimal_ball(root["modulus_ball"])
                if region == "inside":
                    assert bounds[1] < 1
                elif region == "outside":
                    assert bounds[0] > 1
                    _, imaginary, literal = complex_parts(root["root_ball"])
                    SOURCE_FORMATS["outside_records"] += 1
                    SOURCE_FORMATS["outside_no_j"] += not root["root_ball"].endswith("j")
                    SOURCE_FORMATS["outside_minus_separator"] += " - " in root["root_ball"]
                    SOURCE_FORMATS["outside_pure_imaginary"] += root["root_ball"].endswith("j") and " + " not in root["root_ball"] and " - " not in root["root_ball"]
                    assert decimal_ball(literal) == imaginary
                    outside.append([index, ordinal, exponent, multiplicity, literal, root["modulus_ball"]])
                else:
                    assert bounds[0] <= 1 <= bounds[1]
        assert sum(local.values()) == degree
        for name, count in local.items():
            regions[name] += count*exponent
        scopes.append([degree, exponent, factor["cyclotomic"], dict(local)])
    assert integers(product) == certificate["coefficients_ascending"]
    assert sum(regions.values()) == certificate["root_count_with_multiplicity"] == 56
    factors = certificate["factors"]
    gcd = reduce(math.gcd, (i for i, value in enumerate(certificate["coefficients_ascending"]) if i and value), 0)
    primary = (len(factors) == 1 and factors[0]["exponent"] == 1 and not factors[0]["cyclotomic"]
               and factors[0]["degree"] == 56 and gcd == 1)
    assert certificate["neutral"] == all(f["cyclotomic"] for f in factors)
    if primary:
        assert certificate["thresholds"]["13/10"] == "above"
        assert dyadic(certificate["measure_interval"][0]) >= Fraction(13, 10)
    return {"measure_interval": certificate["measure_interval"], "neutral": certificate["neutral"],
            "thresholds": certificate["thresholds"], "region_counts_with_multiplicity": dict(regions),
            "factor_root_scopes": scopes, "outside_roots": outside}, primary


def stats_reference(payload):
    logs, nonreal, counts = [], [], Counter()
    for _, _, exponent, multiplicity, imaginary, modulus in payload["outside_roots"]:
        copies = exponent*multiplicity
        cls = reality(decimal_ball(imaginary))
        counts[cls] += copies
        low, high = decimal_ball(modulus)
        value = max(0.0, math.log(float((low+high)/2)))
        logs.extend([value]*copies)
        if cls == "certified_nonreal":
            nonreal.extend([value]*copies)
    logs.sort(reverse=True)
    measure = center(payload["measure_interval"])
    denominator = math.log(measure)
    regions = payload["region_counts_with_multiplicity"]
    assert len(logs) == regions["outside"]
    result = {"M_center": measure, "logM_center": denominator, "outside": len(logs),
              "nonreal_outside": counts["certified_nonreal"], "real_outside": counts["certified_real"],
              "unknown_outside": counts["unknown"], "inside": regions["inside"], "meets_one": regions["meets_one"],
              "cyclotomic_exact": regions["cyclotomic_exact"]}
    for k in (1, 2, 4):
        result[f"top{k}_log_share_center"] = math.fsum(logs[:k])/denominator if denominator > 0 else None
    result["outside_log_share_center"] = math.fsum(logs)/denominator if denominator > 0 else None
    result["nonreal_outside_log_share_center"] = math.fsum(nonreal)/denominator if denominator > 0 else None
    return result


def native_certificate(full, compact):
    for key in MEASURE_KEYS:
        if key in full:
            exact(full[key], compact[key])
    assert len(full["factors"]) == len(compact["factors"])
    for original, saved in zip(full["factors"], compact["factors"]):
        for key in FACTOR_KEYS:
            exact(original[key], saved[key])


def inspect_sources(data, native, witnesses):
    assert data["observation_fields"] == list(FIELDS)
    assert data["native_comparison_reference"] == "inputs/primitive_comparison.json.gz"
    native_runs = {(r["arm"], r["seed"]): r for group in native["groups"] for r in group["all_seed_outcomes"]}
    assert set(native_runs) == set(SCHEDULE) and native["complete_declared_primitive_comparison"]
    witness_coefficients = {w["witness_id"]: w["coefficients_ascending"] for w in witnesses["witnesses"]}
    next_observation, known_certificates, known_neutrals, known_parents = 0, {}, {}, {}
    reports, total_regions, reality_counts, checked_witnesses = [], Counter(), Counter(), set()
    expected_runs = {(r["arm"], r["seed"]): r for r in data["runs"]}
    statistics_by_id = [stats_reference(c) for c in data["certificates"]]
    for arm, seed in SCHEDULE:
        stem = OUTPUT / f"{LABEL}_d56_{arm}_s{seed}"
        summary, retained = load(stem.with_suffix(".json")), native_runs[(arm, seed)]
        assert summary["valid_run"] and summary["eligible_primitive_comparison_run"]
        assert retained["valid_run"] and retained["eligible_primitive_comparison_run"]
        assert summary["configuration"]["seed"] == seed and summary["configuration"]["variant"] == arm
        native_evaluations = {e["proposal"]: e for e in retained["evaluation_observations"]}
        assert len(native_evaluations) == len(retained["evaluation_observations"])
        for field in ("configuration", "counts", "generation_counts", "primitive_metrics"):
            exact(summary[field], retained[field])
        expected = expected_runs[(arm, seed)]
        for key, actual in (("summary_counts", summary["counts"]), ("generation_counts", summary["generation_counts"]),
                            ("primary_occurrences", summary["primitive_metrics"]["primitive_completed_occurrences"])):
            exact(expected[key], actual)
        assert expected["source_summary"] == stem.with_suffix(".json").name
        assert expected["source_journal"] == stem.with_suffix(".jsonl").name
        assert expected["seconds"] == summary["configuration"]["seconds"] == 20
        seed_coefficients = summary["initialization_observation"]["seed_certificate"]["coefficients_ascending"]
        proposals = completed = primary_count = unresolved = evaluations = 0
        generated = Counter()
        proposal = evaluation = None
        first_observation = next_observation
        for event in events(stem.with_suffix(".jsonl")):
            kind = event["kind"]
            generated[kind] += 1
            if kind == "proposal":
                assert evaluation is None
                proposal = event
                proposals += 1
            elif kind == "evaluation":
                assert event["proposal"] == proposal["proposal"]
                evaluation = event
                evaluations += 1
                saved = native_evaluations[event["proposal"]]
                exact(saved["exact_proposal"], proposal)
                for key in ("cached", "repeated_proposal", "diagnostics", "cost_seconds"):
                    if key in event:
                        exact(saved[key], event[key])
                if "certificate" in event:
                    native_certificate(event["certificate"], saved["certificate"])
                    assert witness_coefficients[saved["whole_witness_id"]] == event["certificate"]["coefficients_ascending"]
                    assert len(saved["factor_witness_ids"]) == len(event["certificate"]["factors"])
                    for factor, identifier in zip(event["certificate"]["factors"], saved["factor_witness_ids"]):
                        assert witness_coefficients[identifier] == factor["coefficients_ascending"]
            elif kind == "commit":
                assert event["elapsed"] <= 20
                assert event["proposal"] == proposal["proposal"] == evaluation["proposal"]
                completed += 1
                saved = native_evaluations[event["proposal"]]
                assert saved["committed"] and saved["commit_elapsed"] == event["elapsed"]
                if "unresolved_error" in evaluation:
                    unresolved += 1
                    proposal = evaluation = None
                    continue
                c = evaluation["certificate"]
                assert c["coefficients_ascending"] == proposal["coefficients_ascending"]
                payload, is_primary = certificate_reference(c)
                primary_count += is_primary
                assert is_primary == evaluation["diagnostics"]["primary_class"]
                row = dict(zip(FIELDS, data["observations"][next_observation]))
                assert (row["arm"], row["seed"], row["proposal"], row["elapsed"]) == (arm, seed, event["proposal"], event["elapsed"])
                cid = row["certificate_id"]
                expected_payload = data["certificates"][cid]
                exact(payload, {k: v for k, v in expected_payload.items() if k != "source"})
                payload_key = json.dumps(payload, sort_keys=True, separators=(",", ":"))
                if payload_key not in known_certificates:
                    assert cid == len(known_certificates)
                    known_certificates[payload_key] = cid
                    exact(expected_payload["source"], {"arm": arm, "seed": seed, "proposal": event["proposal"]})
                assert known_certificates[payload_key] == cid
                generation = proposal["generation"]
                parent, mutation = generation["parent"], generation["mutation"]
                group = dict(scope="uniform", j=None, mutation_size=None, requested_mutation_size=None,
                             B=None, endpoint_plus=None, endpoint_minus=None, gcd_degree=None, neutral_id=None)
                if parent is not None:
                    parent_coefficients = parent["coefficients_ascending"]
                    parent_key = (tuple(parent["neutral_coefficients_ascending"]), parent["substitution_index"], parent["sign"])
                    if parent_key not in known_parents:
                        j, sign = parent["substitution_index"], parent["sign"]
                        assert 1 <= j <= 5 and sign in (-1, 1)
                        lifted = [0]*((len(seed_coefficients)-1)*j+1)
                        for power, value in enumerate(seed_coefficients):
                            lifted[j*power] = value*sign**power
                        known_parents[parent_key] = integers(fmpz_poly(lifted)*fmpz_poly(parent["neutral_coefficients_ascending"]))
                    assert known_parents[parent_key] == parent_coefficients
                    delta = [a-b for a, b in zip(c["coefficients_ascending"], parent_coefficients)]
                    exact(delta, mutation["delta_coefficients_ascending"])
                    assert delta == delta[::-1] and delta[0] == 0
                    size = sum(bool(x) for x in delta[1:29])
                    assert size == (0 if mutation["boundary_return"] else mutation["mutation_size"])
                    g = evaluation["diagnostics"]["parent_neutral"]
                    assert g["applicable"]
                    assert len(g["old_neutral_gcd_coefficients_ascending"])-1 == g["old_neutral_gcd_degree"]
                    if is_primary:
                        assert g["old_neutral_gcd_degree"] == 0
                    neutral_key = tuple(parent["neutral_coefficients_ascending"])
                    nid = row["neutral_id"]
                    if neutral_key not in known_neutrals:
                        neutral = neutral_reference(parent)
                        assert nid == len(known_neutrals)
                        known_neutrals[neutral_key] = nid
                        exact(neutral, {k: v for k, v in data["neutral_templates"][nid].items() if k != "source"})
                        exact(data["neutral_templates"][nid]["source"], {"arm": arm, "seed": seed, "proposal": event["proposal"]})
                    assert known_neutrals[neutral_key] == nid
                    neutral = data["neutral_templates"][nid]
                    group = dict(scope="delta_zero" if size == 0 else "G_positive" if g["old_neutral_gcd_degree"] else "mutated_G1",
                                 j=parent["substitution_index"], mutation_size=size, requested_mutation_size=mutation["mutation_size"],
                                 B=neutral["B"], endpoint_plus=neutral["endpoint_plus"], endpoint_minus=neutral["endpoint_minus"],
                                 gcd_degree=g["old_neutral_gcd_degree"], neutral_id=nid)
                else:
                    assert not evaluation["diagnostics"]["parent_neutral"]["applicable"]
                for key, value in group.items():
                    exact(row[key], value)
                for key, value in (("primary", is_primary), ("cached", evaluation["cached"]),
                                   ("repeated_proposal", evaluation["repeated_proposal"]),
                                   ("root_seconds", evaluation["cost_seconds"].get("root_certification", 0)),
                                   ("factor_seconds", evaluation["cost_seconds"].get("factorization", 0))):
                    exact(row[key], value)
                total_regions.update(payload["region_counts_with_multiplicity"])
                values = statistics_by_id[cid]
                reality_counts.update({name: values[name] for name in ("nonreal_outside", "real_outside", "unknown_outside")})
                if str(next_observation) in data["lower_tail_witnesses"]:
                    exact(data["lower_tail_witnesses"][str(next_observation)],
                          {"exact_proposal": proposal, "certificate": c, "diagnostics": evaluation["diagnostics"]})
                    checked_witnesses.add(next_observation)
                next_observation += 1
                proposal = evaluation = None
        assert evaluations == len(native_evaluations)
        assert completed == summary["counts"]["completed_proposals"]
        assert primary_count == summary["primitive_metrics"]["primitive_completed_occurrences"]
        assert proposals == summary["generation_counts"]["journalled_whole_proposals"]
        for field, kind in (("requests_started", "generation_start"), ("dp_attempt_intents", "raw_attempt_intent"),
                            ("dp_attempts_with_ticket", "raw_attempt_ticket"), ("dp_attempts_completed", "raw_attempt_result")):
            assert generated[kind] == summary["generation_counts"][field]
        result = {"arm": arm, "seed": seed, "completed": completed, "primary": primary_count,
                  "observations": next_observation-first_observation, "committed_unresolved": unresolved,
                  "uncommitted_whole_proposals": proposals-completed,
                  "final_uncommitted_certificate": bool(evaluation and "certificate" in evaluation),
                  "observed_final_proposal": proposal["proposal"] if proposal else None}
        for key in ("observations", "committed_unresolved", "uncommitted_whole_proposals",
                    "final_uncommitted_certificate", "observed_final_proposal"):
            exact(result[key], expected[key])
        if proposal:
            retry = retained["retry_inputs"]["incomplete_proposal_inputs"]
            assert proposal["proposal"] in {r["proposal"] for r in retry}
            if evaluation:
                assert not native_evaluations[evaluation["proposal"]]["committed"]
        reports.append(result)
        print(json.dumps({"original_run_checked": [arm, seed], "committed": completed}), flush=True)
    assert next_observation == len(data["observations"]) == 20378
    assert len(known_certificates) == len(data["certificates"]) == 15612
    assert len(known_neutrals) == len(data["neutral_templates"]) == 4834
    assert checked_witnesses == set(map(int, data["lower_tail_witnesses"]))
    assert sum(total_regions.values()) == 20378*56
    exact(dict(total_regions), {"inside": 209896, "outside": 209896, "meets_one": 631612, "cyclotomic_exact": 89764})
    exact(dict(reality_counts), {"nonreal_outside": 189510, "real_outside": 20386, "unknown_outside": 0})
    return {"runs": reports, "committed_observations": next_observation, "distinct_root_payloads": len(known_certificates),
            "neutral_products_checked": len(known_neutrals), "parent_products_checked": len(known_parents),
            "original_and_native_lower_tail_witnesses": len(checked_witnesses),
            "root_region_counts_with_all_multiplicities": dict(total_regions),
            "exterior_reality_counts_with_all_multiplicities": dict(reality_counts),
            "original_text_inventory": dict(SOURCE_FORMATS)}, statistics_by_id


def distribution(values):
    ordered = sorted(x for x in values if x is not None)
    if not ordered:
        return {"n": 0}
    n = len(ordered)
    middle = ordered[n//2] if n % 2 else (ordered[n//2-1]+ordered[n//2])/2
    return {"n": n, "mean": math.fsum(ordered)/n, "min": ordered[0], "max": ordered[-1],
            "q25": ordered[(n+3)//4-1], "median": middle, "q75": ordered[(3*n+3)//4-1]}


def close_tree(left, right):
    if isinstance(left, dict):
        assert left.keys() == right.keys()
        for key in left:
            close_tree(left[key], right[key])
    elif isinstance(left, list):
        assert len(left) == len(right)
        for a, b in zip(left, right):
            close_tree(a, b)
    elif type(left) is float:
        assert type(right) is float or type(right) is int
        assert math.isclose(left, right, rel_tol=2e-14, abs_tol=2e-14), (left, right)
    else:
        assert type(left) is type(right) and left == right, (left, right)


def aggregate_reference(data, stats):
    exact(data["analysis"]["dimensions"], {
        "scope": ["arm", "scope", "primary"],
        "matched_j_mutation": ["arm", "j", "actual_mutation_size", "primary"],
        "j1_B_endpoint": ["arm", "actual_mutation_size", "B", "endpoint_plus", "endpoint_minus", "primary"],
        "j1_repetition": ["arm", "actual_mutation_size", "repetition_class", "primary"],
        "j1_endpoint_zero_B": ["arm", "actual_mutation_size", "B_class", "primary"]})
    rows = [dict(zip(FIELDS, row)) for row in data["observations"]]
    partitions = {name: defaultdict(list) for name in ("scope", "matched_j_mutation", "j1_B_endpoint", "j1_repetition", "j1_endpoint_zero_B")}
    for index, r in enumerate(rows):
        a, k, p = r["arm"], r["mutation_size"], r["primary"]
        partitions["scope"][(a, r["scope"], p)].append(index)
        if r["scope"] != "mutated_G1":
            continue
        partitions["matched_j_mutation"][(a, r["j"], k, p)].append(index)
        if r["j"] != 1:
            continue
        b, plus, minus = r["B"], r["endpoint_plus"], r["endpoint_minus"]
        partitions["j1_B_endpoint"][(a, k, b, plus, minus, p)].append(index)
        cls = "interior_repeated" if b else "endpoint_repeated_only" if plus > 1 or minus > 1 else "trace_simple"
        partitions["j1_repetition"][(a, k, cls, p)].append(index)
        if plus == minus == 0:
            partitions["j1_endpoint_zero_B"][(a, k, "B_positive" if b else "B_zero", p)].append(index)
    measures = [c["measure_interval"] for c in data["certificates"]]
    selected = set()
    metric_names = ("M_center", "outside", "nonreal_outside", "real_outside", "unknown_outside", "meets_one",
                    "top1_log_share_center", "top2_log_share_center", "top4_log_share_center", "nonreal_outside_log_share_center")
    results = {}
    for name, groups in partitions.items():
        built = []
        for key, indices in sorted(groups.items()):
            records = [rows[i] for i in indices]
            metrics = [stats[r["certificate_id"]] for r in records]
            selected_index = min(indices, key=lambda i: (dyadic(measures[rows[i]["certificate_id"]][1]), rows[i]["seed"], rows[i]["proposal"]))
            lower = min((measures[r["certificate_id"]][0] for r in records), key=dyadic)
            upper = min((measures[r["certificate_id"]][1] for r in records), key=dyadic)
            entry = {"key": list(key), "n": len(indices), "cached": sum(r["cached"] for r in records),
                     "repeated_proposals": sum(r["repeated_proposal"] for r in records),
                     "seed_counts": {str(k): v for k, v in sorted(Counter(r["seed"] for r in records).items())},
                     "minimum_measure_enclosure": [lower, upper], "selected_lower_tail_observation": selected_index,
                     "descriptive": {field: distribution(v[field] for v in metrics) for field in metric_names}}
            built.append(entry)
            if name in ("scope", "j1_repetition") and rows[selected_index]["primary"]:
                selected.add(selected_index)
        close_tree(built, data["analysis"][name])
        results[name] = built
    for arm, seed in SCHEDULE:
        indices = [i for i, r in enumerate(rows) if r["arm"] == arm and r["seed"] == seed and r["primary"]]
        assert indices
        selected.add(min(indices, key=lambda i: (dyadic(measures[rows[i]["certificate_id"]][1]), rows[i]["proposal"])))
    assert sorted(selected) == data["analysis"]["selected_lower_tail_observations"]
    assert selected == set(map(int, data["lower_tail_witnesses"]))
    positive_payloads = [s for s in stats if s["outside_log_share_center"] is not None]
    discrepancy = max(abs(s["outside_log_share_center"]-1) for s in positive_payloads)
    assert discrepancy < 3e-15
    return results, {"all_nonempty_groups_independently_recomputed": {k: len(v) for k, v in results.items()},
                     "selected_lower_tail_observations": sorted(selected),
                     "maximum_relative_center_log_discrepancy": discrepancy,
                     "derived_float_comparison_tolerance": "relative and absolute 2e-14; exact counters and interval endpoints"}


def prose_checks(data, results, stats):
    principal = [g for g in results["j1_endpoint_zero_B"] if g["key"][-1]]
    expected = [
        ("direct", 2, "B_zero", 480, "2.048358", "6.883", "0.4397", "0.7052"),
        ("direct", 3, "B_zero", 247, "2.245001", "7.174", "0.4497", "0.7218"),
        ("dp_closure", 1, "B_zero", 60, "2.594599", "10.733", "0.3169", "0.5656"),
        ("dp_closure", 1, "B_positive", 75, "2.929884", "12.373", "0.2895", "0.5079"),
        ("dp_closure", 2, "B_zero", 56, "2.742316", "10.536", "0.3411", "0.5946"),
        ("dp_closure", 2, "B_positive", 48, "3.069567", "11.375", "0.2946", "0.5302"),
        ("dp_closure", 3, "B_zero", 55, "3.102725", "10.691", "0.3434", "0.6056"),
        ("dp_closure", 3, "B_positive", 60, "3.296555", "11.467", "0.3608", "0.5989")]
    actual = {}
    for g in principal:
        d = g["descriptive"]
        assert g["cached"] == (16 if g["key"][:2] == ["direct", 2] else 0)
        actual[tuple(g["key"][:3])] = (g["n"], f'{d["M_center"]["median"]:.6f}', f'{d["nonreal_outside"]["mean"]:.3f}',
                                    f'{d["top2_log_share_center"]["median"]:.4f}', f'{d["top4_log_share_center"]["median"]:.4f}')
    assert actual == {tuple(row[:3]): row[3:] for row in expected}
    endpoint = {tuple(g["key"]): g for g in results["j1_repetition"]}
    for k, n, m, share in ((1, 45, "3.011894", "0.4115"), (2, 12, "3.603781", "0.4851"), (3, 51, "3.640690", "0.5161")):
        g = endpoint[("dp_closure", k, "endpoint_repeated_only", True)]
        assert (g["n"], f'{g["descriptive"]["M_center"]["median"]:.6f}', f'{g["descriptive"]["top2_log_share_center"]["median"]:.4f}') == (n, m, share)
    for k, n, m in ((1, 172, "2.644162"), (2, 99, "2.775180"), (3, 180, "3.132053")):
        g = endpoint[("dp_closure", k, "trace_simple", True)]
        assert (g["n"], f'{g["descriptive"]["M_center"]["median"]:.6f}') == (n, m)
    matches = {}
    for g in results["matched_j_mutation"]:
        arm, j, k, primary = g["key"]
        if j == 1:
            matches[(arm, k, primary)] = g["n"]
    assert [(matches.get((a, k, True), 0), matches.get((a, k, False), 0))
            for a in ("direct", "dp_closure") for k in (1, 2, 3)] == [(0, 461), (480, 153), (247, 379), (689, 43), (264, 16), (756, 46)]
    rows = [dict(zip(FIELDS, row)) for row in data["observations"]]
    totals = {}
    for arm in ("direct", "dp_closure"):
        selected = [r for r in rows if r["arm"] == arm]
        totals[arm] = {"n": len(selected), "primary": sum(r["primary"] for r in selected),
                       "cached": sum(r["cached"] for r in selected),
                       "repeated": sum(r["repeated_proposal"] for r in selected),
                       "scopes": dict(Counter(r["scope"] for r in selected))}
    exact(totals["direct"], {"n": 15014, "primary": 4521, "cached": 2417, "repeated": 2417,
                            "scopes": {"uniform": 1568, "G_positive": 3691, "mutated_G1": 9755}})
    exact(totals["dp_closure"], {"n": 5364, "primary": 2538, "cached": 0, "repeated": 0,
                                "scopes": {"uniform": 520, "delta_zero": 208, "G_positive": 2398, "mutated_G1": 2238}})
    lower = []
    for arm, expected_index, seed, proposal, expected_center in (
            ("direct", 17351, 34, 1074, 1.3606107462500372),
            ("dp_closure", 11542, 32, 448, 1.6951471325469833)):
        indices = [i for i, r in enumerate(rows) if r["arm"] == arm and r["primary"]]
        chosen = min(indices, key=lambda i: dyadic(data["certificates"][rows[i]["certificate_id"]]["measure_interval"][1]))
        assert chosen == expected_index
        r = rows[chosen]
        assert r["j"] == (3 if arm == "direct" else 1)
        assert (r["seed"], r["proposal"], r["mutation_size"], r["B"], r["endpoint_plus"], r["endpoint_minus"], r["gcd_degree"]) == (
            seed, proposal, 2 if arm == "direct" else 1, 0, 0, 0, 0)
        s = stats[r["certificate_id"]]
        assert s["M_center"] == expected_center
        assert (s["outside"], s["nonreal_outside"], s["real_outside"], s["meets_one"]) == (
            (8, 8, 0, 40) if arm == "direct" else (11, 10, 1, 34))
        shares = tuple(f'{s[f"top{k}_log_share_center"]:.6f}' for k in (1, 2, 4))
        assert shares == (("0.267387", "0.534774", "0.739543") if arm == "direct" else ("0.299859", "0.408434", "0.600013"))
        lower.append({"arm": arm, "seed": seed, "proposal": proposal, "observation": chosen, **s})
    return {"principal_table_eight_rows_match": True, "all_six_primary_nonprimary_denominators_match": True,
            "endpoint_only_and_trace_simple_text_matches": True, "committed_arm_totals": totals,
            "two_whole_arm_primary_lower_tail_witnesses": lower}


def mechanical_interfaces():
    # Fixed artificial payload: this is an arithmetic interface fixture, not
    # a certified polynomial, experimental input or root computation.
    sys.path.insert(0, str(HERE))
    import primitive_root_diagnostics as diagnostic
    fixture = {"measure_interval": [[576, 0], [576, 0]],
               "region_counts_with_multiplicity": {"outside": 8, "inside": 0, "meets_one": 0, "cyclotomic_exact": 48},
               "outside_roots": [[0, 0, 3, 2, "[1 +/- .1]", "2"], [1, 0, 2, 1, "0", "3"]]}
    result = diagnostic.root_statistics(fixture)
    close_tree(result, stats_reference(fixture))
    assert (result["outside"], result["nonreal_outside"], result["real_outside"]) == (8, 6, 2)
    denominator = 6*math.log(2)+2*math.log(3)
    for k, numerator in ((1, math.log(3)), (2, 2*math.log(3)), (4, 2*math.log(3)+2*math.log(2))):
        assert math.isclose(result[f"top{k}_log_share_center"], numerator/denominator, rel_tol=1e-14)
    c = fmpz_poly([-1, 1])**4 * fmpz_poly([1, 1])**2 * fmpz_poly([1, 1, 1])**3
    parent = {"neutral_coefficients_ascending": integers(c), "neutral_factor_powers": [[1, 2], [2, 1], [3, 3]]}
    reference = neutral_reference(parent)
    exact(reference, diagnostic.neutral_record(parent))
    assert (reference["B"], reference["endpoint_plus"], reference["endpoint_minus"], reference["degree"]) == (2, 2, 1, 12)
    return {"factor_and_root_multiplicities_with_two_moduli": "8 individual roots; 6 nonreal and 2 real",
            "top1_top2_top4_individual_contributions_checked": True,
            "endpoint_squared_atom_fixture": {"B": 2, "endpoint_plus": 2, "endpoint_minus": 1, "degree": 12},
            "scope": "Synthetic arithmetic fixtures only; no certificate or experimental observation is claimed."}


def retained_evidence_checks(data):
    assert data["schema"] == "D56-root-diagnostics-1" and data["source_label"] == LABEL
    exact(data["analysis"], load(OUTPUT / "primitive_root_diagnostics_recomputed.json"))
    assert (INPUT / "primitive_root_diagnostics.json").read_bytes() == (
        OUTPUT / "primitive_root_diagnostics_draft.json").read_bytes()
    self_test = load(OUTPUT / "primitive_root_diagnostics_self_test.json")
    assert self_test["new_sampling_factorization_or_root_solving"] == 0
    pending = []
    for run in data["runs"]:
        requests = run["generation_counts"]["requests_started"]
        proposals = run["generation_counts"]["journalled_whole_proposals"]
        assert requests-proposals in (0, 1)
        if requests != proposals:
            pending.append([run["arm"], run["seed"]])
    assert pending == [["dp_closure", 31], ["dp_closure", 32], ["dp_closure", 33]]
    assert sum(r["uncommitted_whole_proposals"] for r in data["runs"]) == 7
    assert sum(r["final_uncommitted_certificate"] for r in data["runs"]) == 4
    return {"retained_native_and_present_draft_bytes_agree": True,
            "author_saved_reanalysis_exactly_equals_native_analysis": True,
            "author_saved_self_test_read": self_test,
            "generation_only_final_requests": pending,
            "uncommitted_whole_proposals": 7, "of_these_with_uncommitted_certificate": 4}


def main():
    destination = OUTPUT / "independent_primitive_root_review.json"
    if destination.exists():
        raise FileExistsError(destination)
    printing = printing_checks()
    data = load(INPUT / "primitive_root_diagnostics.json")
    with gzip.open(INPUT / "primitive_comparison.json.gz", "rt", encoding="utf-8") as stream:
        native = json.load(stream)
    witnesses = load(INPUT / "primitive_witnesses.json")
    source, stats = inspect_sources(data, native, witnesses)
    del native, witnesses
    groups, aggregate = aggregate_reference(data, stats)
    prose = prose_checks(data, groups, stats)
    result = {"scope": "Independent fixed post-hoc extraction and descriptive review; no new experiment.",
              "printing_interface": printing, "source_and_retention_checks": source,
              "all_group_statistics": aggregate, "prose_tables_and_witnesses": prose,
              "independent_mechanical_interfaces": mechanical_interfaces(),
              "retained_evidence_checks": retained_evidence_checks(data),
              "new_sampling_workers_factorizations_or_root_solves": 0,
              "limits": ["Original root certification and irreducible-factor declarations are reused from the frozen evaluator.",
                         "Shares use decimal/dyadic centers and floating logarithms; they are not certified ratio bounds.",
                         "Occurrences are conditioned, repeated and time-censored observations, not independent trials or causal evidence."]}
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
