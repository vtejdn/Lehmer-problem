"""Test a necessary discriminant-action condition for the fixed-cusp generators.

An integral even-norm transvection acts trivially on L-dual/L. Moving every
positive isometry to the left uses the exact covariance identity from L462v14.
The product of those isometries is a finite-order integer matrix of rank 16.
Every eigenvalue order n has phi(n) <= 16, hence divides
E = 2**5 * 3**2 * 5 * 7 * 11 * 13 * 17. Consequently any permitted word acts
on L-dual/L with E-th power equal to the identity. This is only a necessary
condition, not a generator decomposition algorithm.

For the fixed Gram G, the condition is exactly
(C**E - I) * adj(G) == 0 modulo abs(det(G)). All powers below are modular;
no enormous integer C**E, eigenvalues, polynomial roots or field norms are
approximated. A nonzero residue disproves the necessary condition on this
specific invariant lattice; a zero residue supplies no factorization.
"""

from fractions import Fraction
from pathlib import Path
import json

from trace_lattice import ROOT, identity, multiply, determinant


HERE = Path(__file__).resolve().parent
INPUT = ROOT / "mathematics/computations/outputs/Yin_J_G0158/trace_lattice.json"
OUTPUT = ROOT / "mathematics/computations/outputs/Yin_J_G0158/discriminant_action.json"
EXPONENT = 2**5 * 3**2 * 5 * 7 * 11 * 13 * 17


def adjugate(g):
    n, det = len(g), determinant(g)
    assert det != 0
    one = identity(n)
    aug = [[Fraction(x) for x in row + one[i]] for i, row in enumerate(g)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        divisor = aug[k][k]
        aug[k] = [x / divisor for x in aug[k]]
        for i in range(n):
            if i != k:
                coefficient = aug[i][k]
                aug[i] = [x - coefficient * y for x, y in zip(aug[i], aug[k])]
    adj = [[det * x for x in row[n:]] for row in aug]
    assert all(x.denominator == 1 for row in adj for x in row)
    adj = [[int(x) for x in row] for row in adj]
    target = [[det * x for x in row] for row in one]
    assert multiply(g, adj) == target and multiply(adj, g) == target
    return det, adj


def multiply_mod(a, b, modulus):
    return [[x % modulus for x in row] for row in multiply(a, b)]


def power_mod(a, exponent, modulus):
    value = identity(len(a))
    a = [[x % modulus for x in row] for row in a]
    while exponent:
        if exponent & 1:
            value = multiply_mod(value, a, modulus)
        exponent >>= 1
        if exponent:
            a = multiply_mod(a, a, modulus)
    return value


def main():
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    g, c = source["trace_gram"], source["companion"]
    assert len(g) == 18 and len(source["splitting"]["positive_gram"]) == 16
    det, adj = adjugate(g)
    modulus = abs(det)
    power = power_mod(c, EXPONENT, modulus)
    difference = [[power[i][j] - int(i == j) for j in range(18)] for i in range(18)]
    defect = multiply_mod(difference, adj, modulus)
    witness = next(([i, j, defect[i][j]] for i in range(18) for j in range(18) if defect[i][j]), None)
    result = {"polynomial_ascending": source["polynomial_ascending"], "positive_rank": 16,
              "finite_order_exponent": EXPONENT, "gram_determinant": det,
              "modulus": modulus, "gram_adjugate": adj,
              "companion_power_modulus": power, "discriminant_defect": defect,
              "nonzero_entry_witness": witness,
              "necessary_generator_condition": witness is None}
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": OUTPUT.relative_to(ROOT).as_posix(), "exponent": EXPONENT,
                      "nonzero_entry_witness": witness,
                      "necessary_generator_condition": witness is None}, indent=2))


if __name__ == "__main__":
    main()
