"""Decide a prefix of the all-grid trace search using one discriminant budget."""

from argparse import ArgumentParser
from collections import Counter
from math import comb, isqrt, lcm

from free_trace_moments import has_signature


def prefix_search(q, n, depth):
    if q < 2 or n < 2 or depth < 1:
        raise ValueError("Require q,n>=2 and depth>=1")
    d = 2 * n
    modulus = q * (q + 1)
    depth = min(depth, n)
    scale = lcm(*range(1, depth + 1))
    # ln d <= (7/10) ceil(log2 d), and rho^j >= (d-depth)/d.
    bound_numerator = d * d * (7*q*(d-1).bit_length() + 5*q + 20) * scale
    bound = bound_numerator // (10 * q * (d-depth))
    # Store the reciprocal and trace prefixes, Newton sums, pole carry and
    # the part of the common integer upper bound still available.
    states = [((1,), (1,), (), 4, bound)]
    for j in range(1, depth + 1):
        weight = scale // j
        divisor = modulus**j
        center = ((q+1)**(2*j) + q**(2*j)) // divisor
        shifts = [(-1)**(j-i) * comb(d-2*i, j-i) for i in range(j)]
        next_states = []
        for reciprocal, trace, moments, carry, remaining in states:
            shift = sum(c * a for c, a in zip(trace, shifts))
            prior = -sum(c * t for c, t in zip(reciprocal[1:], reversed(moments)))
            residue = prior - j*(carry + shift)
            radius = isqrt(remaining // weight)
            lower = center - 3 - radius
            upper = center + 1 + radius
            first = lower + (residue - lower) % (j*modulus)
            for moment in range(first, upper + 1, j*modulus):
                cost = weight * max(0, moment-center-1, center-3-moment)**2
                digit = (prior-moment) // j
                ordinary = digit - shift
                next_states.append(((*reciprocal, digit), (*trace, ordinary),
                                    (*moments, moment), (carry-ordinary)//modulus,
                                    remaining-cost))
        states = next_states
        if not states:
            return "moment", j, []
    if depth < n:
        return "open", depth, []
    witnesses = [trace for _, trace, _, carry, _ in states
                 if carry == 0 and has_signature(trace, q)]
    return ("realized" if witnesses else "terminal"), n, witnesses


def census(q, minimum, maximum, depth):
    if maximum < minimum:
        raise ValueError("Empty degree range")
    counts = Counter()
    examples = []
    for n in range(minimum, maximum + 1):
        result, stage, witnesses = prefix_search(q, n, depth)
        counts[result, stage] += 1
        if result in {"open", "realized"} and len(examples) < 10:
            examples.append((n, result, witnesses))
    return counts, examples


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("q", type=int)
    parser.add_argument("minimum", type=int)
    parser.add_argument("maximum", type=int)
    parser.add_argument("--depth", type=int, default=16)
    args = parser.parse_args()
    counts, examples = census(args.q, args.minimum, args.maximum, args.depth)
    print(sorted(counts.items()))
    if examples:
        print("first unresolved or realized cases", examples)
