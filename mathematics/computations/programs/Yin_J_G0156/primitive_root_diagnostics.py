"""Post-hoc D56 root/neutral-multiplicity diagnostics from fixed observations.

No sampling, polynomial factorization or numerical root calculation is called.
Exact printed decimal intervals establish nonreality when they exclude zero.
Log-contribution summaries are explicitly descriptive midpoint approximations.
"""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
import json
import math
from pathlib import Path
import statistics

import primitive_core_sampling as live
from archive_sampling_export import journal_events

HERE = Path(__file__).resolve().parent
DEFAULT_INPUT = HERE / "inputs" / "primitive_root_diagnostics.json"
NATIVE_REFERENCE = "inputs/primitive_comparison.json.gz"
FIELDS = ["arm", "seed", "proposal", "elapsed", "scope", "j", "mutation_size", "requested_mutation_size",
          "B", "endpoint_plus", "endpoint_minus", "gcd_degree", "primary", "cached", "repeated_proposal",
          "certificate_id", "neutral_id", "root_seconds", "factor_seconds"]


def decimal_interval(text):
    """Exact rational endpoints of an ordinary Arb decimal-ball rendering."""
    text = text.strip()
    if text.startswith("[") and text.endswith("]"):
        text = text[1:-1].strip()
    if "+/-" in text:
        midpoint, radius = text.split("+/-")
        midpoint = Fraction(midpoint.strip() or "0")
        radius = Fraction(radius.strip())
        if radius < 0:
            raise ValueError("negative printed radius")
        return midpoint - radius, midpoint + radius
    value = Fraction(text)
    return value, value


def imaginary_text(root_ball):
    if not root_ball.endswith("j"):
        decimal_interval(root_ball)
        return "0"
    # The frozen acb rendering uses a plus separator, with any negative
    # imaginary midpoint inside its own ball.  A pure imaginary ball also fits.
    return root_ball[:-1].rsplit(" + ", 1)[-1].strip()


def reality(text):
    try:
        low, high = decimal_interval(text)
    except (ValueError, ZeroDivisionError):
        return "unknown"
    if high < 0 or low > 0:
        return "certified_nonreal"
    if low == high == 0:
        return "certified_real"
    return "unknown"


def dyadic(pair):
    return Fraction(pair[0]) * Fraction(2) ** pair[1]


def midpoint(interval):
    return float((dyadic(interval[0]) + dyadic(interval[1])) / 2)


def totient(n):
    result, remaining, prime = n, n, 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            result -= result // prime
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        result -= result // remaining
    return result


@lru_cache(None)
def cyclotomic(order):
    return live.frozen.fmpz_poly.cyclotomic(order)


def neutral_record(parent):
    """Read DP atom powers or factor the sparse completion by its exact formula."""
    neutral = parent["neutral_coefficients_ascending"]
    if "neutral_factor_powers" in parent:
        atoms = parent["neutral_factor_powers"]
    else:
        degree = len(neutral) - 1
        assert neutral == [1] or neutral == [1] + [0] * (degree - 1) + [1]
        atoms = [[m, 1] for m in range(3, 2 * degree + 1) if 2 * degree % m == 0 and degree % m != 0]
    assert len({m for m, _ in atoms}) == len(atoms)
    assert all(type(m) is type(power) is int and m >= 1 and power > 0 for m, power in atoms)
    exact_powers = [[m, 2 * power if m <= 2 else power] for m, power in atoms]
    product = live.frozen.fmpz_poly([1])
    for m, power in exact_powers:
        product *= cyclotomic(m) ** power
    assert list(map(int, product)) == neutral
    powers = dict(atoms)
    B = sum((power - 1) * totient(m) // 2 for m, power in atoms if m >= 3)
    degree = sum(totient(m) * power for m, power in exact_powers)
    assert degree == len(neutral) - 1
    return {"atom_powers": atoms, "irreducible_cyclotomic_powers": exact_powers,
            "degree": degree, "B": B, "endpoint_plus": powers.get(1, 0), "endpoint_minus": powers.get(2, 0)}


def root_record(certificate):
    counts = Counter({key: 0 for key in ("inside", "outside", "meets_one", "cyclotomic_exact")})
    outside, factors = [], []
    for index, factor in enumerate(certificate["factors"]):
        exponent = factor["exponent"]
        assert factor["root_count"] == factor["degree"]
        if factor["cyclotomic"]:
            assert not factor["roots"]
            counts["cyclotomic_exact"] += factor["degree"] * exponent
            factors.append([factor["degree"], exponent, True, {"cyclotomic_exact": factor["degree"]}])
            continue
        local = Counter()
        for ordinal, root in enumerate(factor["roots"]):
            region, multiplicity = root["region"], root["multiplicity"]
            assert region in ("inside", "outside", "meets_one") and type(multiplicity) is int and multiplicity > 0
            local[region] += multiplicity
            counts[region] += multiplicity * exponent
            if region == "outside":
                try:
                    imaginary = imaginary_text(root["root_ball"])
                    decimal_interval(imaginary)
                except (ValueError, ZeroDivisionError):
                    imaginary = "unparsed: " + root["root_ball"]
                # Keep the exact printed modulus and imaginary interval needed
                # for the derived nonreality and contribution calculations.
                outside.append([index, ordinal, exponent, multiplicity, imaginary, root["modulus_ball"]])
        assert sum(local.values()) == factor["degree"]
        factors.append([factor["degree"], exponent, False, dict(local)])
    assert sum(counts.values()) == certificate["root_count_with_multiplicity"] == 56
    return {"measure_interval": certificate["measure_interval"], "neutral": certificate["neutral"],
            "thresholds": certificate["thresholds"], "region_counts_with_multiplicity": dict(counts),
            "factor_root_scopes": factors, "outside_roots": outside}


def root_statistics(record):
    counts, logs, nonreal_log = Counter(), [], 0.0
    for _, _, exponent, multiplicity, imaginary, modulus in record["outside_roots"]:
        count = exponent * multiplicity
        classification = reality(imaginary)
        counts[classification] += count
        low, high = decimal_interval(modulus)
        assert high > 0
        # Region is the original certification.  Decimal midpoints and these
        # log shares are descriptive, never new root or threshold decisions.
        contribution = max(0.0, math.log(float((low + high) / 2)))
        logs.extend([contribution] * count)
        if classification == "certified_nonreal":
            nonreal_log += contribution * count
    assert len(logs) == record["region_counts_with_multiplicity"]["outside"]
    logs.sort(reverse=True)
    measure = midpoint(record["measure_interval"])
    full_log = math.log(measure)
    result = {"M_center": measure, "logM_center": full_log,
              "outside": len(logs), "nonreal_outside": counts["certified_nonreal"],
              "real_outside": counts["certified_real"], "unknown_outside": counts["unknown"],
              "inside": record["region_counts_with_multiplicity"]["inside"],
              "meets_one": record["region_counts_with_multiplicity"]["meets_one"],
              "cyclotomic_exact": record["region_counts_with_multiplicity"]["cyclotomic_exact"]}
    for size in (1, 2, 4):
        result[f"top{size}_log_share_center"] = sum(logs[:size]) / full_log if full_log > 0 else None
    result["outside_log_share_center"] = sum(logs) / full_log if full_log > 0 else None
    result["nonreal_outside_log_share_center"] = nonreal_log / full_log if full_log > 0 else None
    return result


def observation(row):
    assert len(row) == len(FIELDS)
    return dict(zip(FIELDS, row))


def distribution(values):
    values = sorted(value for value in values if value is not None)
    if not values:
        return {"n": 0}
    # Explicit nearest-rank quartiles avoid interpolating tiny sparse strata.
    rank = lambda q: values[max(0, math.ceil(q * len(values)) - 1)]
    return {"n": len(values), "mean": statistics.fmean(values), "min": values[0],
            "q25": rank(0.25), "median": statistics.median(values), "q75": rank(0.75), "max": values[-1]}


def aggregate(data):
    rows = [observation(row) for row in data["observations"]]
    stats = [root_statistics(item) for item in data["certificates"]]
    result = {}
    dimensions = {
        "scope": lambda r: (r["arm"], r["scope"], r["primary"]),
        "matched_j_mutation": lambda r: (r["arm"], r["j"], r["mutation_size"], r["primary"]),
        "j1_B_endpoint": lambda r: (r["arm"], r["mutation_size"], r["B"], r["endpoint_plus"], r["endpoint_minus"], r["primary"]),
        "j1_repetition": lambda r: (r["arm"], r["mutation_size"],
            "interior_repeated" if r["B"] > 0 else "endpoint_repeated_only" if max(r["endpoint_plus"], r["endpoint_minus"]) > 1 else "trace_simple", r["primary"]),
        "j1_endpoint_zero_B": lambda r: (r["arm"], r["mutation_size"], "B_positive" if r["B"] else "B_zero", r["primary"]),
    }
    metrics = ("M_center", "outside", "nonreal_outside", "real_outside", "unknown_outside", "meets_one",
               "top1_log_share_center", "top2_log_share_center", "top4_log_share_center", "nonreal_outside_log_share_center")
    selected_witnesses = set()
    for name, key_function in dimensions.items():
        groups = defaultdict(list)
        for index, row in enumerate(rows):
            if name != "scope" and row["scope"] != "mutated_G1":
                continue
            if name.startswith("j1_") and row["j"] != 1:
                continue
            if name == "j1_endpoint_zero_B" and (row["endpoint_plus"] or row["endpoint_minus"]):
                continue
            groups[key_function(row)].append(index)
        output = []
        for key, indices in sorted(groups.items()):
            entries = [rows[index] for index in indices]
            values = [stats[row["certificate_id"]] for row in entries]
            chosen = min(indices, key=lambda index: (dyadic(data["certificates"][rows[index]["certificate_id"]]["measure_interval"][1]), rows[index]["seed"], rows[index]["proposal"]))
            low = min((data["certificates"][row["certificate_id"]]["measure_interval"][0] for row in entries), key=dyadic)
            high = min((data["certificates"][row["certificate_id"]]["measure_interval"][1] for row in entries), key=dyadic)
            item = {"key": list(key), "n": len(entries), "cached": sum(row["cached"] for row in entries),
                    "repeated_proposals": sum(row["repeated_proposal"] for row in entries),
                    "seed_counts": {str(seed): count for seed, count in sorted(Counter(row["seed"] for row in entries).items())},
                    "minimum_measure_enclosure": [low, high], "selected_lower_tail_observation": chosen,
                    "descriptive": {metric: distribution(value[metric] for value in values) for metric in metrics}}
            output.append(item)
            if name in ("j1_repetition", "scope") and rows[chosen]["primary"]:
                selected_witnesses.add(chosen)
        result[name] = output
    # Preserve the primary minimum for each formal arm/seed regardless of branch.
    for arm in live.VARIANTS:
        for seed in live.SEEDS:
            available = [i for i, r in enumerate(rows) if r["arm"] == arm and r["seed"] == seed and r["primary"]]
            if available:
                selected_witnesses.add(min(available, key=lambda i: dyadic(data["certificates"][rows[i]["certificate_id"]]["measure_interval"][1])))
    result["selected_lower_tail_observations"] = sorted(selected_witnesses)
    result["dimensions"] = {
        "scope": ["arm", "scope", "primary"], "matched_j_mutation": ["arm", "j", "actual_mutation_size", "primary"],
        "j1_B_endpoint": ["arm", "actual_mutation_size", "B", "endpoint_plus", "endpoint_minus", "primary"],
        "j1_repetition": ["arm", "actual_mutation_size", "repetition_class", "primary"],
        "j1_endpoint_zero_B": ["arm", "actual_mutation_size", "B_class", "primary"]}
    return result


def extract(label):
    if label != "s10_primitive_core_comparison":
        raise ValueError("this diagnostic is restricted to the completed frozen comparison")
    data = {"schema": "D56-root-diagnostics-1", "source_label": label, "native_comparison_reference": NATIVE_REFERENCE,
            "scope": "post-hoc committed-observation diagnostic, not a frozen metric or causal comparison",
            "root_scope": "original certified outside/inside/meets_one; cyclotomic roots exact separately; nonreality only when printed imaginary interval excludes zero",
            "log_share_scope": "descriptive centers; top1/2/4 individual roots expanded by root and irreducible-factor multiplicities, divided by log of full-M enclosure center",
            "observation_fields": FIELDS, "certificates": [], "neutral_templates": [], "observations": [], "runs": []}
    neutral_ids, certificate_ids = {}, {}
    for arm, seed in live.schedule():
        path = live.run_stem(label, 56, arm, seed).with_suffix(".json")
        summary = json.loads(path.read_text(encoding="utf-8"))
        assert summary["valid_run"] and summary["eligible_primitive_comparison_run"]
        expected = {"completed": summary["counts"]["completed_proposals"],
                    "primary": summary["primitive_metrics"]["primitive_completed_occurrences"]}
        run = {"arm": arm, "seed": seed, "source_summary": path.name, "source_journal": path.with_suffix(".jsonl").name,
               "seconds": summary["configuration"]["seconds"], "summary_counts": summary["counts"],
               "generation_counts": summary["generation_counts"], "primary_occurrences": expected["primary"]}
        del summary
        proposal = evaluation = None
        completed = primary = unresolved = all_proposals = 0
        first_index = len(data["observations"])
        for event in journal_events(path.with_suffix(".jsonl")):
            if event["kind"] == "proposal":
                assert evaluation is None
                proposal = event
                all_proposals += 1
            elif event["kind"] == "evaluation":
                assert proposal is not None and proposal["proposal"] == event["proposal"]
                evaluation = event
            elif event["kind"] == "commit":
                assert proposal is not None and evaluation is not None
                assert event["proposal"] == evaluation["proposal"] == proposal["proposal"]
                assert event["elapsed"] <= run["seconds"]
                completed += 1
                if "unresolved_error" in evaluation:
                    unresolved += 1
                    evaluation = proposal = None
                    continue
                certificate = evaluation["certificate"]
                diagnostic = evaluation["diagnostics"]
                assert certificate["coefficients_ascending"] == proposal["coefficients_ascending"]
                root_data = root_record(certificate)
                # Mathematical payload, not timings, determines diagnostic reuse.
                certificate_key = json.dumps(root_data, sort_keys=True, separators=(",", ":"))
                if certificate_key not in certificate_ids:
                    certificate_ids[certificate_key] = len(data["certificates"])
                    root_data["source"] = {"arm": arm, "seed": seed, "proposal": event["proposal"]}
                    data["certificates"].append(root_data)
                certificate_id = certificate_ids[certificate_key]
                generation = proposal["generation"]
                parent, mutation = generation["parent"], generation["mutation"]
                neutral_id = j = size = requested = B = endpoint_plus = endpoint_minus = gcd_degree = None
                if parent is None:
                    scope = "uniform"
                    assert not diagnostic["parent_neutral"]["applicable"]
                else:
                    j, requested = parent["substitution_index"], mutation["mutation_size"]
                    delta = mutation["delta_coefficients_ascending"]
                    assert delta == [a - b for a, b in zip(proposal["coefficients_ascending"], parent["coefficients_ascending"])]
                    size = sum(value != 0 for value in delta[1:29])
                    assert size in (0, requested)
                    assert (size == 0) == mutation["boundary_return"]
                    key = tuple(parent["neutral_coefficients_ascending"])
                    if key not in neutral_ids:
                        neutral_ids[key] = len(data["neutral_templates"])
                        neutral = neutral_record(parent)
                        neutral["source"] = {"arm": arm, "seed": seed, "proposal": event["proposal"]}
                        data["neutral_templates"].append(neutral)
                    neutral_id = neutral_ids[key]
                    neutral = data["neutral_templates"][neutral_id]
                    B, endpoint_plus, endpoint_minus = (neutral[k] for k in ("B", "endpoint_plus", "endpoint_minus"))
                    gcd_degree = diagnostic["parent_neutral"]["old_neutral_gcd_degree"]
                    assert gcd_degree == len(diagnostic["parent_neutral"]["old_neutral_gcd_coefficients_ascending"]) - 1
                    scope = "delta_zero" if size == 0 else "G_positive" if gcd_degree > 0 else "mutated_G1"
                primary += diagnostic["primary_class"]
                row = [arm, seed, event["proposal"], event["elapsed"], scope, j, size, requested, B, endpoint_plus, endpoint_minus,
                       gcd_degree, diagnostic["primary_class"], evaluation["cached"], evaluation["repeated_proposal"],
                       certificate_id, neutral_id, evaluation["cost_seconds"].get("root_certification", 0),
                       evaluation["cost_seconds"].get("factorization", 0)]
                assert len(row) == len(FIELDS)
                data["observations"].append(row)
                evaluation = proposal = None
        assert completed == expected["completed"] and primary == expected["primary"]
        assert all_proposals == run["generation_counts"]["journalled_whole_proposals"]
        run.update(observations=len(data["observations"]) - first_index, committed_unresolved=unresolved,
                   uncommitted_whole_proposals=all_proposals - completed,
                   final_uncommitted_certificate=bool(evaluation and "certificate" in evaluation),
                   observed_final_proposal=proposal["proposal"] if proposal else None)
        data["runs"].append(run)
        print(json.dumps({"arm": arm, "seed": seed, "committed": completed, "primary": primary}), flush=True)
    data["analysis"] = aggregate(data)
    selected = { (observation(data["observations"][index])["arm"], observation(data["observations"][index])["seed"],
                  observation(data["observations"][index])["proposal"]): index
                 for index in data["analysis"]["selected_lower_tail_observations"] }
    witnesses = {}
    for arm, seed in live.schedule():
        wanted = {p for a, s, p in selected if (a, s) == (arm, seed)}
        proposal = None
        for event in journal_events(live.run_stem(label, 56, arm, seed).with_suffix(".jsonl")):
            if event["kind"] == "proposal" and event["proposal"] in wanted:
                proposal = event
            elif event["kind"] == "evaluation" and event["proposal"] in wanted:
                index = selected[(arm, seed, event["proposal"])]
                witnesses[str(index)] = {"exact_proposal": proposal, "certificate": event["certificate"], "diagnostics": event["diagnostics"]}
    assert set(map(int, witnesses)) == set(data["analysis"]["selected_lower_tail_observations"])
    data["lower_tail_witnesses"] = witnesses
    return data


def self_test():
    assert decimal_interval("[+/- 1e-3]") == (Fraction(-1, 1000), Fraction(1, 1000))
    assert reality("[-2 +/- 1e-20]") == "certified_nonreal"
    assert reality("[0 +/- 1e-20]") == "unknown"
    assert reality("0") == "certified_real" and reality("unparsed") == "unknown"
    assert imaginary_text("[1 +/- .1] + [-2 +/- .01]j") == "[-2 +/- .01]"
    assert imaginary_text("[1 +/- .1]") == "0"
    assert imaginary_text("[+/- .1]j") == "[+/- .1]"
    c = live.frozen.fmpz_poly([-1, 1])**4 * live.frozen.fmpz_poly([1, 1])**2 * cyclotomic(3)**3
    record = neutral_record({"neutral_coefficients_ascending": list(map(int, c)), "neutral_factor_powers": [[1, 2], [2, 1], [3, 3]]})
    assert (record["B"], record["endpoint_plus"], record["endpoint_minus"]) == (2, 2, 1)
    for parent in live.direct_parents():
        record = neutral_record(parent)
        assert (record["B"], record["endpoint_plus"], record["endpoint_minus"]) == (0, 0, 0)
    record = {"measure_interval": [[64, 0], [64, 0]], "region_counts_with_multiplicity":
              {"outside": 6, "inside": 0, "meets_one": 0, "cyclotomic_exact": 50},
              "outside_roots": [[0, 0, 3, 2, "[2 +/- .1]", "2"]]}
    stats = root_statistics(record)
    assert stats["outside"] == stats["nonreal_outside"] == 6
    for k in (1, 2, 4):
        assert abs(stats[f"top{k}_log_share_center"] - k / 6) < 1e-14
    return {"exact_decimal_and_nonreality_fixtures": "pass", "trace_endpoint_atom_semantics": "pass",
            "ten_direct_simple_neutral_parents": "pass", "root_and_factor_multiplicity_expansion": "pass",
            "new_sampling_factorization_or_root_solving": 0}


def write_new(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError("preserve existing diagnostic input or output")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, separators=(",", ":"))
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("self-test").add_argument("--output", type=Path, required=True)
    build = commands.add_parser("extract")
    build.add_argument("--label", default="s10_primitive_core_comparison")
    build.add_argument("--output", type=Path, default=DEFAULT_INPUT)
    analyze = commands.add_parser("analyze")
    analyze.add_argument("input", type=Path)
    analyze.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("preserve existing diagnostic input or output")
    if args.command == "self-test":
        result = self_test()
    elif args.command == "extract":
        self_test()
        result = extract(args.label)
    else:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = aggregate(data)
        assert result == data["analysis"]
    write_new(args.output, result)
    print(json.dumps({"output": str(args.output), "bytes": args.output.stat().st_size, "command": args.command}))


if __name__ == "__main__":
    main()
