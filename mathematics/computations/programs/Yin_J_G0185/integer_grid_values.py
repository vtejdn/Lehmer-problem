"""Enclose integer evaluations over full boxes surrounding rational trace grids."""

from math import prod

from adaptive_grid import propose


def integer_window(nodes, q, a, radius, denominator):
    """Enclose all integral H(-a) on the positive-pole branch for moving nodes."""
    modulus = q * (q + 1)
    numerators = [t * denominator for t in nodes]
    if any(x.denominator != 1 for x in numerators):
        raise ValueError("Nodes must have the indicated common denominator")
    centers = [-a * denominator - int(x) for x in numerators]
    boxes = [(c, c) if i in (0, len(centers)-1) else (c-radius, c+radius)
             for i, c in enumerate(centers)]
    sizes = [max(abs(lo), abs(hi)) for lo, hi in boxes]
    if any(size == 0 for size in sizes):
        raise ValueError("A fixed endpoint coincides with the evaluation")
    product = prod(sizes)
    negatives = sum(hi < 0 for lo, hi in boxes)
    uncertain = sum(lo <= 0 <= hi for lo, hi in boxes)
    lower, upper = 0, 0

    def include(size, negative, uncertain_count):
        nonlocal lower, upper
        if uncertain_count or negative % 2:
            lower = min(lower, -size)
        if uncertain_count or not negative % 2:
            upper = max(upper, size)

    include(modulus * product, negatives, uncertain)
    for size, (lo, hi) in zip(sizes, boxes):
        bound = (1+a*modulus) * denominator * (product // size)
        include(bound, 1 + negatives - (hi < 0), uncertain - (lo <= 0 <= hi))
    scale = modulus * denominator**len(nodes)
    return -((-lower) // scale), upper // scale


if __name__ == "__main__":
    denominator = 2**40
    trials = ((5, 121, 4, 3), (5, 481, 8, 2), (5, 981, 16, 1),
              (6, 643, 12, 1), (40, 1643, 4, 2))
    for q, n, fitted, a in trials:
        nodes = propose(q, n, fitted, denominator)
        modulus = q * (q + 1)
        step = 1 + a * modulus
        residue = (4*modulus+1) * pow(-a, n, step) % step
        low, high = integer_window(nodes, q, a, denominator//65536, denominator)
        first = low + (residue-low) % step
        print(f"q={q} n={n} x={-a} integers=[{low},{high}] "
              f"residue={residue} modulus={step}")
        assert first > high
