"""Exact distances between the two already known finite target-core classes.

This post-run diagnostic reads only the retained target partition. It supplies
no proposals, training data, new target or Mahler certificate. Distances concern
free reciprocal coefficients, so a mutation of one coordinate can change two
coefficients of the complete polynomial. Output is reproducible from inputs.
"""

import argparse
from collections import Counter
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name
LEHMER = (1, -1, 0, 1, -1, 1, -1, 1, 0, -1, 1)


def distances(left, right):
    assert len(left) == len(right)
    return {
        "hamming": sum(a != b for a, b in zip(left, right)),
        "l1": sum(abs(a-b) for a, b in zip(left, right)),
        "squared_l2": sum((a-b)**2 for a, b in zip(left, right)),
        "changed_pair_blocks": sum(left[k:k+2] != right[k:k+2]
                                   for k in range(0, len(left), 2)),
    }


def evaluate(data):
    rows = []
    for partition in data["target_partitions"]:
        groups = partition["core_groups"]
        assert len(groups) == 2
        first = next(g for g in groups if tuple(g["core_coefficients_ascending"]) == LEHMER)
        second = next(g for g in groups if tuple(g["core_coefficients_ascending"]) != LEHMER)
        for group in groups:
            prefixes = group["target_prefixes"]
            assert len(prefixes) == len({tuple(p) for p in prefixes}) == group["count"]
            assert all(len(p) == partition["degree"]//2 for p in prefixes)
            assert all(type(a) is int and -4 <= a <= 4 for p in prefixes for a in p)
        assert not ({tuple(p) for p in first["target_prefixes"]} &
                    {tuple(p) for p in second["target_prefixes"]})
        outcomes, histogram = [], Counter()
        for target in second["target_prefixes"]:
            pairs = [(prefix, distances(prefix, target)) for prefix in first["target_prefixes"]]
            histogram.update(result["hamming"] for _, result in pairs)
            minima = {}
            for name in pairs[0][1]:
                best = min(result[name] for _, result in pairs)
                witnesses = [prefix for prefix, result in pairs if result[name] == best]
                minima[name] = {"minimum": best, "nearest_count": len(witnesses),
                                "one_nearest_Lehmer_prefix": witnesses[0]}
            outcomes.append({"second_core_prefix": target, "minima": minima})
        rows.append({"degree": partition["degree"], "Lehmer_prefixes": first["count"],
                     "second_core_prefixes": second["count"],
                     "cross_pair_hamming_histogram": dict(sorted(histogram.items())),
                     "second_core_outcomes": outcomes})
    return {"scope": "Exact finite target-class geometry; no discovery or trained proposal law.",
            "results": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=HERE / "inputs" / "degree_core_mass_states.json")
    parser.add_argument("--output", type=Path, default=OUTPUT / "target_geometry.json")
    args = parser.parse_args()
    result = evaluate(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
