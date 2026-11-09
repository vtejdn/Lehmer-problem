"""Post-run conditional target mass; reference targets never enter a live law.

The exact prescribed updates are replayed from committed journal events.
The final mass sums use binary64 only as an explicitly approximate diagnostic.
This program does not change an experiment's proposals, certificates or yield.
"""

import argparse
import json
from pathlib import Path

from sampler import Law, OUTPUT


def target_mass(law, targets):
    probabilities = []
    for block in law.blocks:
        total = sum(block["weights"])
        probabilities.append({state: weight / total
                              for state, weight in zip(block["states"], block["weights"])})
    biased = 0.0
    for target in targets:
        mass = 1.0
        for block, probability in zip(law.blocks, probabilities):
            start, width = block["start"], block["width"]
            mass *= probability[tuple(target[start:start + width])]
        biased += mass
    return len(targets) / (10 * 9 ** law.half_degree) + 0.9 * biased


def diagnose(path, reference):
    config = law = row = proposal = evaluation = None
    batch, points = [], []
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                break
            kind = event["kind"]
            if kind == "config":
                config = event
                if config["arm"] != "adaptive":
                    raise ValueError("this diagnostic inspects an adaptive run")
                row = next(item for item in reference["results"] if item["degree"] == config["degree"])
                law = Law(config["degree"] // 2, "adaptive", config["seed"])
                initial = target_mass(law, row["target_prefixes"])
                expected = row["static_mixture_target_probability"]["decimal"]
                assert abs(initial / expected - 1) < 1e-12
                points.append({"proposal": 0, "elapsed": 0, "conditional_target_mass_approx": initial})
            elif kind == "proposal":
                proposal, evaluation = event, None
            elif kind == "evaluation":
                evaluation = event
            elif kind == "commit" and event["elapsed"] <= config["seconds"]:
                assert proposal["proposal"] == evaluation["proposal"] == event["proposal"]
                if not evaluation.get("unresolved_error") and evaluation["ranking_resolved"] and not evaluation["neutral"]:
                    batch.append((tuple(evaluation["core_coefficients_ascending"]),
                                  evaluation["log_score"], proposal["free_coefficients"]))
                if event["proposal"] % 256 == 0:
                    assert law.update(batch) == evaluation["update"]
                    batch.clear()
                    points.append({"proposal": event["proposal"], "elapsed": event["elapsed"],
                                   "conditional_target_mass_approx": target_mass(law, row["target_prefixes"])})
    if config is None:
        raise ValueError("journal has no configuration")
    initial = points[0]["conditional_target_mass_approx"]
    final = points[-1]["conditional_target_mass_approx"]
    return {"source_journal": path.name, "degree": config["degree"], "seed": config["seed"],
            "updates_replayed": len(points) - 1, "initial_target_mass_approx": initial,
            "final_target_mass_approx": final, "final_to_initial_ratio_approx": final / initial,
            "points": points,
            "interpretation": "Post-run approximate probability of a whole-polynomial target under the current law; not distinct-value yield, training data or a uniform-population estimate."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("journal", type=Path)
    parser.add_argument("--reference", type=Path, default=OUTPUT / "baseline_mass.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    reference = json.loads(args.reference.read_text(encoding="utf-8"))
    result = diagnose(args.journal, reference)
    destination = args.output or args.journal.with_suffix(".law_mass.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "points"}))


if __name__ == "__main__":
    main()
