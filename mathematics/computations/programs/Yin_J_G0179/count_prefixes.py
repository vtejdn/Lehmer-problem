"""Count integral Newton prefixes in specified symmetric power-sum boxes."""

import json
from fractions import Fraction
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np


GROUP = Path(__file__).resolve().parent
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name


def prime_powers(k):
    """Yield (prime, exact prime-power divisor) for the factors of k."""
    remaining = k
    for prime in range(2, k + 1):
        if remaining % prime:
            continue
        power = 1
        while remaining % prime == 0:
            remaining //= prime
            power *= prime
        yield prime, power
        if remaining == 1:
            break


def count_box(bounds):
    """Count all prefixes before any cyclotomic, sign or irreducibility filter."""
    if not bounds or any(type(b) is not int or b < 0 for b in bounds):
        raise ValueError("Expected a nonempty list of nonnegative integer bounds")
    sizes = {k: 2*b + 1 for k, b in enumerate(bounds, 1)}
    branch_bound = prod((n + k - 1) // k for k, n in sizes.items())
    # The exact count is at most branch_bound, since earlier sums prescribe
    # s_k modulo k. Unsigned tensor operations compute in Z/(2**64).
    dtype = np.uint64 if branch_bound < 2**64 else object
    values = {k: np.arange(-b, b+1) for k, b in enumerate(bounds, 1)}
    factors = [((k,), np.ones(size, dtype=dtype)) for k, size in sizes.items()]
    for k in sizes:
        for prime, modulus in prime_powers(k):
            predecessor = k // prime
            difference = values[predecessor][:, None] - values[k][None, :]
            factors.append(((predecessor, k), (difference % modulus == 0).astype(dtype)))

    remaining = list(sizes)
    largest_table = 0
    while remaining:
        bags = {k: sorted(set().union(*(scope for scope, _ in factors if k in scope)))
                for k in remaining}
        table_sizes = {k: prod(sizes[j] for j in bag) for k, bag in bags.items()}
        k = min(remaining, key=table_sizes.get)
        bag = bags[k]
        largest_table = max(largest_table, table_sizes[k])
        new_factors = []
        joint = np.array(1, dtype=dtype)
        for scope, table in factors:
            if k not in scope:
                new_factors.append((scope, table))
                continue
            shape = tuple(sizes[j] if j in scope else 1 for j in bag)
            joint = joint * table.reshape(shape)
        new_scope = tuple(j for j in bag if j != k)
        new_factors.append((new_scope, joint.sum(axis=bag.index(k), dtype=dtype)))
        factors = new_factors
        remaining.remove(k)

    count = prod(int(table) for _, table in factors)
    if dtype is np.uint64:
        count %= 2**64
    assert 1 <= count <= branch_bound
    return {"bounds": bounds, "count": count, "branch_bound": branch_bound,
            "largest_table_entries": largest_table}


def elementary_bounds(degree, length=8):
    """Use both nonzero resultants with X**k +/- 1 and the root-product bound."""
    radius = Fraction(1089, 1000)
    return [int((degree - 2 + radius**(2*k) + radius**(-2*k)) / 2)
            for k in range(1, length+1)]


def full_reciprocal_box(degree, bounds):
    """Also count one sign representative per polynomial with no power substitution."""
    result = count_box(bounds)
    if len(bounds) != degree//2:
        return result
    primes = [prime for prime, _ in prime_powers(degree)]
    primitive = result["count"]
    for size in range(1, len(primes)+1):
        for selected in combinations(primes, size):
            modulus = prod(selected)
            restricted = [bound if k % modulus == 0 else 0
                          for k, bound in enumerate(bounds, 1)]
            primitive += (-1)**size * count_box(restricted)["count"]
    assert primitive % 2 == 0
    result["no_power_substitution_up_to_sign"] = primitive//2
    return result


def direct_newton(bounds):
    """Independent recursion for the first few coefficients of the monic input."""
    prefixes = [([1], [])]
    for k, bound in enumerate(bounds, 1):
        extended = []
        for coefficients, sums in prefixes:
            fixed = sum(c*s for c, s in zip(coefficients[1:], reversed(sums)))
            for s in range(-bound, bound+1):
                if (s + fixed) % k == 0:
                    extended.append((coefficients + [-(s + fixed)//k], sums + [s]))
        prefixes = extended
    return len(prefixes)


def main():
    certificates = json.loads((OUTPUT / "results.json").read_text(encoding="utf-8"))
    results = {}
    for degree in (56, 58):
        verified = certificates["degrees"][str(degree)]
        fixed = certificates["fixed_degrees"][str(degree)]
        if len(verified) != degree//2 or len(fixed) != degree//2:
            raise ValueError("Every coefficient through the middle degree needs a bound")
        if any(stronger > original for stronger, original in zip(verified, fixed)):
            raise ValueError("The combined box exceeds the fixed-weight box")
        short = count_box(verified[:3])
        assert short["count"] == direct_newton(verified[:3])
        results[str(degree)] = {
            "certified_first_three": short,
            "certified_all_available": full_reciprocal_box(degree, verified),
            "fixed_weight_box": full_reciprocal_box(degree, fixed),
            "elementary_first_eight": count_box(elementary_bounds(degree)),
        }
    (OUTPUT / "prefixes.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
