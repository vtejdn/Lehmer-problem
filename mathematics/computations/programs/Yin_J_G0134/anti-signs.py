"""Uncertified finite sign-lift screens for binary reciprocal supports.

The logarithmic circle sums have no rigorous error bounds, particularly near
zeros.  They select analytic questions, not proved Mahler inequalities.
"""

import argparse
import cmath
import itertools
import json
import math
from pathlib import Path
import sys


def positive_seed_screen(points, shift):
    zs = [cmath.exp(2j * math.pi * (j + shift) / points) for j in range(points)]
    powers = [[z**e for z in zs] for e in range(45)]
    high = []
    count = 0
    for k in range(3, 13):
        for a, b in itertools.combinations(range(1, k), 2):
            h = {0: 1, a: 1, b: 1, k: 1}
            for n in range(1, 9):
                values = []
                for sigma in (-1, 1):
                    coefficients = {}
                    for e, c in h.items():
                        coefficients[e + n] = coefficients.get(e + n, 0) + c
                        coefficients[k - e] = coefficients.get(k - e, 0) + sigma * c
                    terms = [(e, c) for e, c in coefficients.items() if c]
                    value = sum(
                        math.log(abs(sum(c * powers[e][j] for e, c in terms)))
                        for j in range(points)
                    ) / points
                    values.append(value)
                count += 1
                if min(values) > math.log(2) + 0.01:
                    high.append({"k": k, "a": a, "b": b, "n": n, "means": values})
    return {"case_count": count, "both_signs_above_log2_plus_001": high}


def anti_sign_screen(points, shift):
    sines = [
        [2 * math.sin(2 * math.pi * a * (j + shift) / points) for j in range(points)]
        for a in range(1, 21)
    ]
    results = []
    for frequencies in itertools.combinations(range(1, 15), 4):
        rows = []
        for last_signs in itertools.product((-1, 1), repeat=3):
            signs = (1,) + last_signs
            value = sum(
                math.log(max(1e-300, abs(sum(
                    c * sines[a - 1][j] for a, c in zip(frequencies, signs)
                ))))
                for j in range(points)
            ) / points
            rows.append({"signs": signs, "mean": value})
        results.append({
            "frequencies": frequencies,
            "best_mean": min(row["mean"] for row in rows),
            "average_mean": sum(row["mean"] for row in rows) / len(rows),
            "sign_rows": rows,
        })
    results.sort(key=lambda row: row["best_mean"], reverse=True)
    return {
        "frequency_tuple_count": len(results),
        "signs_per_tuple": 8,
        "best_mean_above_log2_plus_001_count": sum(
            row["best_mean"] > math.log(2) + 0.01 for row in results
        ),
        "largest_best_means": results[:10],
        "largest_average_mean": max(results, key=lambda row: row["average_mean"]),
        "largest_individual_mean": max(
            ({"frequencies": row["frequencies"], **sign_row}
             for row in results for sign_row in row["sign_rows"]),
            key=lambda row: row["mean"],
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--points", type=int, default=2048)
    parser.add_argument("--shift", type=float, default=0.371)
    parser.add_argument("--screen", choices=("both", "positive", "anti"), default="both")
    args = parser.parse_args()
    if args.points < 1 or not 0 < args.shift < 1:
        parser.error("points must be positive and shift must lie strictly between zero and one")
    result = {
        "python": sys.version.split()[0],
        "points": args.points,
        "shift": args.shift,
        "screen": args.screen,
        "certified": False,
        "small_value_floor_for_anti_log": 1e-300,
    }
    if args.screen in ("both", "positive"):
        result["positive_seed"] = positive_seed_screen(args.points, args.shift)
    if args.screen in ("both", "anti"):
        result["anti_sign"] = anti_sign_screen(args.points, args.shift)
    group = Path(__file__).resolve().parent
    output = group.parent.parent / "outputs" / group.name / "anti-signs.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    summary = {"output": str(output), "certified": False}
    if "positive_seed" in result:
        summary["positive_cases"] = result["positive_seed"]["case_count"]
        summary["positive_both_signs_high"] = len(result["positive_seed"]["both_signs_above_log2_plus_001"])
    if "anti_sign" in result:
        summary["anti_tuples"] = result["anti_sign"]["frequency_tuple_count"]
        summary["worst_best"] = result["anti_sign"]["largest_best_means"][0]
        summary["worst_average"] = result["anti_sign"]["largest_average_mean"]
        summary["worst_individual"] = result["anti_sign"]["largest_individual_mean"]
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
