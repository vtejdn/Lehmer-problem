"""Certify the Newton boxes needed at the next primes, using the degree-58 weights."""

from pathlib import Path
import json
import sys


GROUP = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(GROUP))
import count_prefixes
import trace_bounds


def main():
    all_weights = json.loads((GROUP / "refined_weights.json").read_text(encoding="utf-8"))
    weights = all_weights["58"]
    unit_caps = {}
    outer_caps = {}
    report = {}
    for degree in (60, 62):
        half = degree // 2
        bounds = []
        layers = []
        for k in range(1, half + 1):
            row = tuple(weights[min(k, len(weights)) - 1])
            if row not in unit_caps:
                unit_caps[row] = trace_bounds.certify(0, row, trace_bounds.guide(0, row), 10**7)
            if (k, row) not in outer_caps:
                outer_caps[k, row] = trace_bounds.certify(k, row, trace_bounds.guide(k, row), 10**7)
            unit, outer = unit_caps[row], outer_caps[k, row]
            bounds.append(((half - 1) * unit["upper"] + outer["upper"]) // trace_bounds.LOG_SCALE)
            layers.append({"k": k, "unit": unit, "outer": outer})
        count = count_prefixes.full_reciprocal_box(degree, bounds)
        report[str(degree)] = {"certificates": layers, "certified_all_available": count}
        print(degree, bounds, count["no_power_substitution_up_to_sign"], flush=True)
    target = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v6"
    target.mkdir(parents=True, exist_ok=True)
    (target / "boxes.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
