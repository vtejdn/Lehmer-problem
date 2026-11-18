"""Factor the primitive quartic section at a=3 and count each trace signature."""

from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from math import gcd
from pathlib import Path
from tempfile import NamedTemporaryFile
import json

from flint import fmpq_poly, fmpz_poly


X = fmpz_poly([0, 1])
ONE = fmpz_poly([1])
DEFAULT_BOUND = 720
GROUP = Path(__file__).resolve().parent
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name


def reciprocal_trace(factor):
    """Use the J170 Chebyshev recurrence, then recover the full X-polynomial."""
    degree = factor.degree()
    if degree % 2 or factor.coeffs() != factor.coeffs()[::-1]:
        raise ValueError(f"Expected an even-degree reciprocal core factor: {factor}")
    n = degree // 2
    trace = fmpz_poly([factor[n]])
    previous, current = fmpz_poly([2]), X
    for j in range(1, n + 1):
        trace += factor[n+j] * current
        previous, current = current, X * current - previous

    lifted = fmpz_poly([trace[n]])
    for j in range(1, n + 1):
        lifted = (X**2 + 1) * lifted + trace[n-j] * X**j
    if lifted != factor:
        raise ArithmeticError("Trace lift did not reconstruct the factor")
    return trace


def sturm_variations(trace):
    """Count sign changes at -infinity, -2, 2, +infinity by exact remainders."""
    if trace(-2) == 0 or trace(2) == 0:
        raise ValueError("A nontorsion trace meets an endpoint")
    previous, current = trace, trace.derivative()
    last_signs = [0] * 4
    variations = [0] * 4
    while True:
        leading = previous.leading_coefficient()
        values = (leading * (-1)**previous.degree(), previous(-2), previous(2), leading)
        for j, value in enumerate(values):
            if value:
                sign = 1 if value > 0 else -1
                variations[j] += last_signs[j] == -sign
                last_signs[j] = sign
        if previous.degree() == 0:
            return variations
        if not current:
            raise ArithmeticError("Nontorsion trace is not squarefree")
        if current.degree() == 0:
            previous = current
        else:
            remainder = (-(fmpq_poly(previous) % fmpq_poly(current))).numer()
            if remainder:
                remainder //= remainder.content()
            previous, current = current, remainder


def factor_direction(b):
    parent = 1 + X**3 - X**12 + X**b * (X**12 + X**9 - 1)
    unit, factors = parent.factor()
    if unit != 1 or parent.degree() != b + 12:
        raise ArithmeticError("Unexpected degree or content")
    recovered = ONE
    torsion, other = [], []
    for factor, multiplicity in factors:
        recovered *= factor**multiplicity
        order = int(factor.is_cyclotomic())
        if order:
            if factor != fmpz_poly.cyclotomic(order):
                raise ArithmeticError("Cyclotomic identity failed")
            torsion.append([order, multiplicity])
            continue
        trace = reciprocal_trace(factor)
        variations = sturm_variations(trace)
        below, inside, above = [a - b for a, b in zip(variations, variations[1:])]
        nonreal = trace.degree() - below - inside - above
        if min(below, inside, above, nonreal) < 0 or nonreal % 2:
            raise ArithmeticError("Inconsistent trace signature")
        exterior = below + above + nonreal
        if exterior == 0:
            raise ArithmeticError("Kronecker test contradicts cyclotomic classification")
        other.append({
            "coefficients_descending": [int(c) for c in reversed(factor.coeffs())],
            "degree": factor.degree(), "multiplicity": multiplicity,
            "sturm_variations": variations, "unit_circle": 2 * inside,
            "negative_real_exterior": below, "positive_real_exterior": above,
            "nonreal_exterior_pairs": nonreal // 2, "exterior": exterior,
            "salem_after_negation": below == 1 and exterior == 1 and inside > 0,
            "positive_salem": above == 1 and exterior == 1 and inside > 0,
        })
    if recovered != parent:
        raise ArithmeticError(f"Rational factors failed to reconstruct parent at b={b}")
    return {"b": b, "cyclotomic": sorted(torsion), "nontorsion": other}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--bound", type=int, default=DEFAULT_BOUND)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    if min(args.bound, args.workers) < 1:
        parser.error("The inclusive b bound and the worker count must be positive.")
    admissible = [b for b in range(1, args.bound + 1) if gcd(3, b) == 1]
    if args.workers == 1:
        rows = list(map(factor_direction, admissible))
    else:
        with ProcessPoolExecutor(args.workers) as executor:
            rows = list(executor.map(factor_direction, admissible, chunksize=4))
    payload = {"s": 4, "a": 3, "b_max": args.bound, "directions": rows}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT / f"census_b{args.bound}.json"
    with NamedTemporaryFile("w", encoding="utf-8", dir=OUTPUT, delete=False) as temporary:
        staged = Path(temporary.name)
        try:
            json.dump(payload, temporary, separators=(",", ":"))
            temporary.write("\n")
        except BaseException:
            temporary.close()
            staged.unlink()
            raise
    try:
        staged.replace(destination)
    finally:
        staged.unlink(missing_ok=True)
    print(f"Completed {len(rows)} coprime directions through b={args.bound}.")


if __name__ == "__main__":
    main()
