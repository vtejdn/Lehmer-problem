"""Certify a finite integer-amplitude sign census on the original odd grids.

All arithmetic for deciding a sign is Arb at 128 bits or more.
A nonconstant exact gcd with B_n certifies a forbidden zero grid value.
No floating sign is used and no Mahler-measure claim is made.
"""

import argparse
from collections import Counter
import json
from pathlib import Path
from time import perf_counter

from flint import arb, ctx, fmpz_poly

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent.parent / "outputs" / HERE.name / "amplitudes.json"


def chebyshev(n):
    t = fmpz_poly([0, 1])
    result = [fmpz_poly([1]), t]
    while len(result) <= n:
        result.append(t * result[-1] - result[-2])
    return result


def grid(p, precision):
    ctx.prec = precision
    n = (p - 1) // 2
    angles = [arb.pi() * (2 * j) / p for j in range(1, n + 1)]
    b = [2 * angle.cos() for angle in angles]
    sine = [angle.sin() for angle in angles]
    E = [[((k + 1) * angle).sin() / s for angle, s in zip(angles, sine)]
         for k in range(n)]
    return b, E


def signs(H, V, amplitude):
    """Inspect necessary extremes first, then every interior node."""
    n = len(H)
    states = [None] * n
    for j in [n - 1, 0, *range(1, n - 1)]:
        value = H[j] - amplitude * V[j]
        states[j] = 1 if value > 0 else -1 if value < 0 else 0
        if j == n - 1 and states[j] == 1:
            return "last_positive", None
        if j == 0 and states[j] == -1:
            return "first_negative", None
    if 0 in states:
        return "needs_zero_check", None
    if any(left < right for left, right in zip(states, states[1:])):
        return "extra_sign_transition", None
    assert states[0] == 1 and states[-1] == -1
    return "strict_chamber", states.count(-1)


def census(max_p, signed=False):
    start = perf_counter()
    totals = Counter()
    rows, hits = [], []
    t = fmpz_poly([0, 1])
    for p in range(9, max_p + 1, 2):
        n = (p - 1) // 2
        exact_E = chebyshev(n)
        B = exact_E[n] + exact_E[n - 1]
        assert B.degree() == n
        b, E = grid(p, 128)
        counts = Counter()
        for m in range(2, (p - 5) // 2 + 1):
            s = p - 2 * m
            H = [x * x * y * y for x, y in zip(b, E[m - 1])]
            for L in range(3, min(2 * m, s, n), 1 if signed else 2):
                counts["parameter_triples"] += 1
                V = [x * y for x, y in zip(b, E[L])]
                for magnitude in range((L + 1) // 2 + 1, 2 * m):
                    amplitude = (-1) ** (L + 1) * magnitude
                    counts["integer_amplitude_cases"] += 1
                    outcome, cut = signs(H, V, amplitude)
                    if outcome == "needs_zero_check":
                        h = t * t * exact_E[m - 1] ** 2 - amplitude * t * exact_E[L]
                        gcd = h.gcd(B)
                        if gcd.degree() >= 1:
                            outcome = "exact_zero_grid_value"
                        else:
                            refined_b, refined_E = grid(p, 512)
                            refined_H = [x * x * y * y for x, y in zip(refined_b, refined_E[m - 1])]
                            refined_V = [x * y for x, y in zip(refined_b, refined_E[L])]
                            outcome, cut = signs(refined_H, refined_V, amplitude)
                            counts["precision_refinements"] += 1
                            ctx.prec = 128
                            if outcome == "needs_zero_check":
                                raise ArithmeticError(("unresolved sign", p, m, L, amplitude))
                    counts[outcome] += 1
                    if outcome == "strict_chamber":
                        hits.append({"p": p, "r": 2 * m, "s": s, "L": L,
                                     "amplitude": amplitude, "negative_block_size": cut,
                                     "P_at_minus_one": 4 * m - 2 * magnitude})
        assert counts["integer_amplitude_cases"] == sum(counts[key] for key in (
            "last_positive", "first_negative", "extra_sign_transition",
            "exact_zero_grid_value", "strict_chamber"))
        totals.update(counts)
        rows.append({"p": p, "counts": dict(counts)})
    return {
        "scope": {"amplitude_mode": "signed" if signed else "positive",
                  "odd_conductors_from": 9, "odd_conductors_through": max_p,
                  "r": "2m, m>=2", "s": "p-2m odd >=5",
                  "L": "3<=L<min(r,s), L<=n-1" + ("" if signed else "; L odd"),
                  "integer_amplitudes": "A=(-1)^(L+1) B, floor((L+1)/2)+1 <= B < 2m",
                  "excluded_without_enumeration": "other amplitude signs or B<=(L+1)/2 fail the last sign; B>=2m fails strict endpoint",
                  "initial_Arb_precision_bits": 128, "fallback_precision_bits": 512},
        "counts": dict(totals), "strict_chamber_inputs": hits,
        "by_conductor": rows, "elapsed_seconds": perf_counter() - start,
        "limitations": "Finite pole signs and endpoint only; no assertion for larger conductors or total Mahler measures.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=101)
    parser.add_argument("--signed", action="store_true", help="also test negative amplitudes at even matching lengths")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_p < 9 or args.max_p > 101 or args.max_p % 2 == 0:
        parser.error("this bounded comparison supports odd max-p between 9 and 101")
    result = census(args.max_p, args.signed)
    output = args.output or OUTPUT.with_name("amplitudes_signed.json" if args.signed else OUTPUT.name)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "by_conductor"}))


if __name__ == "__main__":
    main()
