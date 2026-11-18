"""Certify primitivity and trace-field exclusions for Mossinghoff's 72 Salem inputs."""

from collections import Counter
from functools import cache
from math import comb
from pathlib import Path
from runpy import run_path
from tempfile import NamedTemporaryFile

from sympy import Poly, isprime, primerange, symbols


GROUP = Path(__file__).resolve().parent
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name
X = symbols("X")
POWER_PRIMES = tuple(primerange(2, 17))


def trace_polynomial(full):
    """Return descending coefficients of Q, where P(X) = X**s Q(X+1/X)."""
    s = (len(full) - 1) // 2
    remainder = full[::-1]
    trace = []
    for j in range(s, -1, -1):
        coefficient = remainder[s + j]
        trace.append(coefficient)
        for i in range(j + 1):
            remainder[s - j + 2 * i] -= coefficient * comb(j, i)
    if any(remainder):
        raise ArithmeticError("The source polynomial failed trace reconstruction")
    return trace


def evaluate(polynomial, residue, prime):
    value = 0
    for coefficient in polynomial:
        value = (value * residue + coefficient) % prime
    return value


def power_witnesses(full):
    degree = len(full) - 1
    derivative = [(degree - i) * c for i, c in enumerate(full[:-1])]
    found = {}
    for ell in primerange(3, 728):
        eligible = [p for p in POWER_PRIMES if p not in found and (ell - 1) % p == 0]
        if not eligible:
            continue
        for a in range(1, ell):
            if evaluate(full, a, ell):
                continue
            slope = evaluate(derivative, a, ell)
            if not slope:
                continue
            for p in eligible:
                value = pow(a, (ell - 1) // p, ell)
                if p not in found and value != 1:
                    found[p] = (ell, a, slope, value)
            if all(p in found for p in eligible):
                break
        if len(found) == len(POWER_PRIMES):
            return found
    raise ArithmeticError(f"Missing simple residue for {set(POWER_PRIMES) - set(found)}")


@cache
def compatible(source, target):
    """Can the source cycles map onto the target cycles with equal fiber size?"""
    h = sum(source) // sum(target)
    if h == 1:
        return source == target
    initial = tuple(sorted((b, h * b) for b in target))

    @cache
    def assign(i, capacities):
        if i < 0:
            return True
        length = source[i]
        for j, (b, remaining) in enumerate(capacities):
            if j and capacities[j - 1] == (b, remaining):
                continue
            if length % b or length > remaining:
                continue
            updated = list(capacities)
            updated[j] = (b, remaining - length)
            if assign(i - 1, tuple(sorted(updated))):
                return True
        return False

    return assign(len(source) - 1, initial)


def factor_degrees(trace, ell):
    polynomial = Poly.from_list(trace, X, modulus=ell)
    if not polynomial.is_sqf:
        return ()
    _, factors = polynomial.factor_list()
    return tuple(sorted(f.degree() for f, _ in factors))


def format_degrees(degrees):
    return ",".join(map(str, degrees))


def field_witnesses(traces):
    degrees = {i: len(q) - 1 for i, q in traces.items()}
    pairs = {(i, j) for i in traces for j in traces
             if i != j and degrees[i] % degrees[j] == 0}
    initial_count = len(pairs)
    composite = {i for i in traces if not isprime(degrees[i])}
    excluded = {}
    primitive = {}
    for ell in primerange(2, 32):
        needed = composite | {i for pair in pairs for i in pair}
        cycles = {i: factor_degrees(traces[i], ell) for i in needed}
        for i, j in sorted(pairs):
            if not cycles[i] or not cycles[j] or compatible(cycles[i], cycles[j]):
                continue
            excluded[i, j] = (degrees[i], degrees[j], ell,
                              format_degrees(cycles[i]), format_degrees(cycles[j]))
            pairs.remove((i, j))
        for i in sorted(composite):
            for length in cycles[i]:
                if 2 * length > degrees[i] and isprime(length):
                    primitive[i] = (degrees[i], ell, length, format_degrees(cycles[i]))
                    composite.remove(i)
                    break
        if not pairs and not composite:
            break
    if pairs or composite:
        raise ArithmeticError(f"Unresolved inclusions {pairs} or subfield cases {composite}")
    if len(excluded) != initial_count:
        raise ArithmeticError("Missing field witnesses")
    return excluded, primitive


def write_table(name, header, rows):
    path = OUTPUT / name
    lines = ["\t".join(header)] + ["\t".join(map(str, row)) for row in rows]
    output = NamedTemporaryFile(dir=OUTPUT, prefix=name + ".", suffix=".tmp",
                                mode="w", encoding="utf-8", newline="\n", delete=False)
    pending = Path(output.name)
    try:
        with output:
            output.write("\n".join(lines) + "\n")
        pending.replace(path)
    finally:
        pending.unlink(missing_ok=True)


def main():
    read_rows = run_path(str(GROUP.parent / "Yin_J_G0173" / "least_exponents.py"))["source_rows"]
    source = read_rows()
    traces = {}
    powers = []
    for rank, degree, _, half in source:
        if degree > 46:
            raise ValueError("Degree exceeds the certified Voutier cutoff")
        full = half + half[-2::-1]
        traces[rank] = trace_polynomial(full)
        witnesses = power_witnesses(full)
        powers.extend((rank, p, *witnesses[p]) for p in POWER_PRIMES)
    exclusions, primitive = field_witnesses(traces)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_table("powers.tsv", ("rank", "p", "ell", "root", "derivative", "power_residue"), powers)
    write_table("inclusions.tsv", ("source", "target", "source_degree", "target_degree", "ell",
                                   "source_factor_degrees", "target_factor_degrees"),
                ((*pair, *row) for pair, row in sorted(exclusions.items())))
    write_table("subfields.tsv", ("rank", "trace_degree", "ell", "prime_factor_degree", "factor_degrees"),
                ((i, *row) for i, row in sorted(primitive.items())))
    prime_counts = Counter(row[2] for row in exclusions.values())
    print(f"{len(powers)} power witnesses for {len(source)} inputs")
    print(f"{len(exclusions)} degree-compatible exclusions: {dict(sorted(prime_counts.items()))}")
    print(f"{len(primitive)} composite and {len(source) - len(primitive)} prime trace degrees")


if __name__ == "__main__":
    main()
