"""Enumerate positive Toeplitz prefixes for C_h with q=h+3 and B(2)=-1."""

import argparse
from math import lcm


def exact_div(numerator, denominator):
    quotient, remainder = divmod(numerator, denominator)
    if remainder:
        raise ArithmeticError("Nonintegral scaled predictor or determinant")
    return quotient


def endpoint_test(coeff, h):
    # coeff starts with the monic endpoint of B-sharp and ends at its center.
    m = h + 1
    plus = coeff[-1] + 2 * sum(coeff[:-1])
    minus = coeff[-1] + 2 * sum(
        v * (-1)**(m - i) for i, v in enumerate(coeff[:-1])
    )
    return plus == -1 and (-1)**h * minus * (h + 4) <= -(3*h + 2)


def enumerate_range(first, last):
    if not 3 <= first <= last:
        raise ValueError("The moment recursion here uses h >= 3")
    # One positive correction works throughout the specified interval.
    q_min, q_max = first + 3, last + 3
    scale = 8 * lcm(2*(q_min - 1), 2*(q_max + 1))
    plus_mass = scale // (2*(q_min - 1))
    minus_mass = scale // (2*(q_max + 1))
    mass = scale + plus_mass - minus_mass
    prefixes = [0] * (last + 2)
    matched = {h: 0 for h in range(first, last + 1)}
    completions = {h: [] for h in matched}

    def walk(n, previous, current, prediction, moments, scaled_j, coeff, fixed_h):
        # At order n, the predictors are scaled by det(T_n) = previous.
        if fixed_h is None:
            prefixes[n] += 1
            h = n - 1
            if h in matched and endpoint_test(coeff, h):
                matched[h] += 1
                walk(n, previous, current, prediction, moments, scaled_j, coeff, h)
            if n == last + 1:
                return
        else:
            depth = n - (fixed_h + 1)
            levels = completions[fixed_h]
            if len(levels) == depth:
                levels.append(0)
            levels[depth] += 1
            if n == 2*fixed_h - 1:
                return

        k = n + 1
        power = 1 << k
        # The new scaled moment 2^k * scale * moment(k) is affine in b_k.
        constant_moment = scale * scaled_j // 2
        constant_moment += (plus_mass - (-1)**k * minus_mass) * power
        predicted = sum(
            p * (y << i)
            for i, (p, y) in enumerate(zip(prediction, reversed(moments[1:])), 1)
        )
        offset = exact_div(previous * constant_moment - predicted, power)
        step = previous * (scale // 2)
        lower = max(-3, (-current - offset) // step + 1)
        upper = min(3, (current - 1 - offset) // step)
        if fixed_h is not None:
            reflected = coeff[2*(fixed_h + 1) - k]
            lower = max(lower, reflected)
            upper = min(upper, reflected)

        for b in range(lower, upper + 1):
            cross = offset + b * step
            next_det = exact_div(current**2 - cross**2, previous)
            next_prediction = [
                exact_div(current*p - cross*r, previous)
                for p, r in zip(prediction, reversed(prediction))
            ] + [cross]
            next_moment = constant_moment + b * (scale // 2) * power
            walk(k, current, next_det, next_prediction, moments + [next_moment],
                 scaled_j + b*power, coeff + [b], fixed_h)

    walk(0, 1, mass, [], [mass], 1, [1], None)
    for h, levels in completions.items():
        free = h + 1
        terminal = 2*h - 1
        if not levels:
            first_empty = free
        elif len(levels) == terminal - free + 1:
            first_empty = None
        else:
            first_empty = free + len(levels)
        print(f"h={h} q={h+3} free_prefixes={prefixes[free]} "
              f"endpoint_matches={matched[h]} first_empty={first_empty} "
              f"terminal_survivors={levels[-1] if first_empty is None else 0}")
        if first == last:
            print("Free prefix counts:", prefixes)
            print("Counts after endpoint tests and reflection:", levels)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first", type=int, default=74)
    parser.add_argument("--last", type=int)
    args = parser.parse_args()
    enumerate_range(args.first, args.last if args.last is not None else args.first)
