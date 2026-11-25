"""Compare measures with squares of every real exterior root in the primitive catalogue."""

from collections import Counter, defaultdict
from math import comb, isqrt
from pathlib import Path
import sys


PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0188"))
from radial_cores import graeffe, signature, sturm, table_rows, trace_from_half


SCALE = 1 << 22


def homogeneous_sign(polynomial, numerator, denominator):
    """Return the sign at a rational point using ascending integer coefficients."""
    value = polynomial[-1]
    denominator_power = 1
    for coefficient in reversed(polynomial[:-1]):
        denominator_power *= denominator
        value = numerator * value + coefficient * denominator_power
    return (value > 0) - (value < 0)


def variations_at(chain, numerator, denominator):
    signs = [homogeneous_sign(row, numerator, denominator) for row in chain]
    if signs[0] == 0:
        raise ArithmeticError("Sturm endpoint is a trace root.")
    nonzero = [sign for sign in signs if sign]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def measure_square_root_interval(powered, binomials, step):
    """Enclose sqrt(M(P)) at denominator SCALE from the step-th Graeffe row."""
    lower = max(SCALE * abs(c) // b for c, b in zip(powered, binomials))
    upper = SCALE * sum(map(abs, powered))
    for _ in range(step + 1):
        lower = isqrt(SCALE * lower)
        radicand = SCALE * upper
        upper = isqrt(radicand)
        if upper * upper < radicand:
            upper += 1
    return lower, upper


def trace_endpoint(scaled_root):
    return scaled_root**2 + SCALE**2, scaled_root * SCALE


def compare_real_roots(polynomial, trace, negative, positive):
    chain = sturm(trace)
    degree = len(polynomial) - 1
    binomials = [comb(degree, j) for j in range(degree + 1)]
    powered = polynomial
    for step in range(17):
        if step >= 5:
            low, high = measure_square_root_interval(powered, binomials, step)
            if SCALE < low <= high < 2 * SCALE:
                left, den_left = trace_endpoint(low)
                right, den_right = trace_endpoint(high)
                below = above = 0
                if negative:
                    below += variations_at(chain, -left, den_left) - variations_at(chain, -2, 1)
                    above += negative - (variations_at(chain, -right, den_right)
                                         - variations_at(chain, -2, 1))
                if positive:
                    below += variations_at(chain, 2, 1) - variations_at(chain, left, den_left)
                    above += positive - (variations_at(chain, 2, 1)
                                         - variations_at(chain, right, den_right))
                if below + above == negative + positive:
                    return step, below, above
        if step < 16:
            powered = graeffe(powered)
    raise ArithmeticError("Could not separate every real exterior square from the measure.")


def main():
    counts = Counter()
    steps = Counter()
    real_roots = Counter()
    lifts = defaultdict(list)
    positive_source = []
    smallest = []
    for line, degree, _, _, polynomial in table_rows():
        if degree > 44:
            continue
        trace = trace_from_half(polynomial[:degree // 2 + 1])
        _, (negative, _, positive, nonreal_pairs) = signature(trace)
        if negative + positive == 0:
            counts["no real exterior"] += 1
            continue
        if negative + positive == 1 and nonreal_pairs == 0:
            counts["signed Salem"] += 1
            real_roots["above"] += 1
            if degree <= 22:
                sign = 1 if positive else -1
                if homogeneous_sign(polynomial, sign * 8, 7) != -1:
                    raise ArithmeticError(f"Salem root on line {line} does not exceed 8/7 in modulus.")
                threshold = homogeneous_sign(polynomial, sign * 59, 50)
                if threshold == 0:
                    raise ArithmeticError("Rational upper comparison is a polynomial root.")
                if threshold > 0:
                    smallest.append(line)
                lifts[degree].append(line)
                if positive:
                    positive_source.append(line)
            continue
        counts["other with real exterior"] += 1
        step, below, above = compare_real_roots(polynomial, trace, negative, positive)
        steps[step] += 1
        real_roots["below"] += below
        real_roots["above"] += above

    expected = {"no real exterior": 534, "signed Salem": 46, "other with real exterior": 364}
    if (counts != expected or real_roots != {"below": 304, "above": 123}
            or sum(map(len, lifts.values())) != 27 or smallest != [154]):
        raise ArithmeticError(f"Unexpected catalogue totals: {counts}, {real_roots}, {smallest}")
    print("Primitive rows:", dict(counts))
    print("Real exterior squares relative to measure:", dict(real_roots))
    print("Mixed rows separated at each Graeffe step:", dict(sorted(steps.items())))
    for degree, lines in sorted(lifts.items()):
        print(f"Degree {degree} signed Salem rows:", *lines)
    print("Rows already oriented with a positive exterior root:", *positive_source)
    print("Only eligible Salem row below 59/50:", *smallest)


if __name__ == "__main__":
    main()
