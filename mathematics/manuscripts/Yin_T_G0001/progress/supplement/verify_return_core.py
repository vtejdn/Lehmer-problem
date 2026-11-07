"""Standalone verification of the finite premise of the Lehmer core theorem.

Inputs beside this file:
  return-core.json       signed-axis word supports and an enclosing ellipsoid;
  return-paths.bin.gz    original-digit ancestry, not a numerical search log.

The three checks below implement the mathematical argument in the report:
  1. normalized displacement bodies contain a ball giving descent at rho >= 8;
  2. a rigorous enclosing ellipsoid is traversed completely, retaining every
     possible compact residue state, with exactly 797507 conservative candidates;
  3. integer edges lead to zero, apart from 70 rigorously excluded outer states.

Only NumPy and python-flint are required beyond Python's standard library.
Arb balls enclose every algebraic calculation; the branch traversal uses Python
integers; NumPy is used only for integer batches after an explicit overflow proof.
No optimizer, random search, saved floating roots, repository import, or network
access is used.  All checks remain active under Python -O.  This program checks
the finite premises, not the report's subsequent analytic and lattice arguments.
"""

from array import array
from fractions import Fraction
import gzip
import json
from math import isqrt
from pathlib import Path
import struct

import numpy as np
from flint import acb, arb, arb_mat, ctx, fmpq, fmpz_poly


POLYNOMIAL = (1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1)
COEFFICIENT_BOUNDS = (7, 6, 7, 7, 6, 5, 5, 5, 5, 6)
HERE = Path(__file__).resolve().parent


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def real(value):
    """Embed a rational exactly before outward Arb rounding."""
    q = Fraction(value)
    return arb(fmpq(q.numerator, q.denominator))


def length(vector):
    return sum((v * v for v in vector), arb(0)).sqrt()


def trace_polynomial(x):
    return ((((x + 1) * x - 5) * x - 5) * x + 4) * x + 3


def algebraic_embeddings():
    """Five sign changes account for all roots of the degree-five trace polynomial.

    The identity t^5 Q(t+t^-1)=P(t) is checked by Laurent arithmetic.
    Four trace roots lie in (-2,2); the fifth exceeds 2.  These facts give the
    four upper unit-circle conjugates, beta and beta^-1 without floating roots.
    Factoring the original integer polynomial checks irreducibility separately.
    """
    power = {0: 1}
    expansion = {}
    for coefficient in (3, 4, -5, -5, 1, 1):
        for exponent, value in power.items():
            expansion[exponent + 5] = expansion.get(exponent + 5, 0) + coefficient * value
        following = {}
        for exponent, value in power.items():
            for step in (-1, 1):
                following[exponent + step] = following.get(exponent + step, 0) + value
        power = following
    require(tuple(expansion.get(i, 0) for i in range(11)) == POLYNOMIAL,
            "The trace identity has changed")
    require(all(0 <= i <= 10 or v == 0 for i, v in expansion.items()),
            "Unexpected Laurent term")
    content, factors = fmpz_poly(list(POLYNOMIAL)).factor()
    require(content == 1 and len(factors) == 1 and factors[0][1] == 1,
            "The original degree-ten polynomial is not irreducible")

    brackets = [(-19, -18), (-15, -14), (-6, -5), (9, 10), (20, 21)]
    isolated = []
    for left, right in brackets:
        low, high = Fraction(left, 10), Fraction(right, 10)
        low_sign = trace_polynomial(low)
        require(low_sign * trace_polynomial(high) < 0, "Trace root is not bracketed")
        while high - low > Fraction(1, 2**260):
            middle = (low + high) / 2
            middle_sign = trace_polynomial(middle)
            require(middle_sign != 0, "Unexpected rational trace root")
            if low_sign * middle_sign < 0:
                high = middle
            else:
                low, low_sign = middle, middle_sign
        isolated.append(real((low + high) / 2) + arb(0, fmpq(
            (high - low).numerator, 2 * (high - low).denominator)))
    require(all(-2 < u and u < 2 for u in isolated[:4]) and isolated[4] > 2,
            "Incorrect real/unit-circle root classification")
    u = isolated[-1]
    beta = (u + (u * u - 4).sqrt()) / 2
    require(real(Fraction(117, 100)) < beta < real(Fraction(118, 100)),
            "The expanding root lies outside its declared interval")
    conjugates = [acb(u / 2, (1 - u * u / 4).sqrt()) for u in isolated[:4]]
    rows = [[beta**i for i in range(10)], [beta**(-i) for i in range(10)]]
    rows += [[(z**i).real for i in range(10)] for z in conjugates]
    rows += [[(z**i).imag for i in range(10)] for z in conjugates]
    return beta, conjugates, rows


def normalized_descent(table, beta, conjugates):
    """Verify the actual two-cell, 32-axis, 217-word certificate.

    For each word, forward Horner evaluation followed by division by z^ell
    independently reconstructs c_w.  Nine normalized vertices express each
    signed axis target with positive barycentric coordinates.  Their convex
    hull therefore contains the cross-polytope and its radius r/sqrt(8) ball.
    At rho >= 8 the drop is at least min ||c_w||^2 (16 r/sqrt(8)-1).
    """
    require(table['grid'] == 100, "Unexpected displacement grid")
    require([r['cell'] for r in table['cells']] == [[50, 75], [75, 100]],
            "The two full closed cells are required")
    cache = {}
    uses = 0
    strip = 1 / (beta - 1)
    for row, radius in zip(table['cells'], (Fraction(101, 500), Fraction(207, 1000))):
        require(Fraction(row['target_numerator'], row['target_denominator']) == radius,
                "The adopted signed-axis radius has changed")
        certificates = row['certificates']
        require(sorted((c['coordinate'], c['sign']) for c in certificates) ==
                [(i, s) for i in range(8) for s in (-1, 1)], "An axis target is missing")
        costs = []
        for certificate in certificates:
            words = certificate['digits']
            require(len(words) == 9, "Each barycentric certificate needs nine words")
            vertices = []
            for digits in words:
                require(1 <= len(digits) <= 11 and
                        all(type(d) is int and d in (-1, 0, 1) for d in digits),
                        "Invalid original digit word")
                endpoints = [real(Fraction(n, 100)) for n in row['cell']]
                for digit in digits:
                    endpoints = [beta * x + digit for x in endpoints]
                    require(endpoints[0] > -strip and endpoints[1] < strip,
                            "An intermediate word state leaves the expanding strip")
                require(endpoints[0] > -1 and endpoints[1] < 1,
                        "The word does not map its full closed cell into (-1,1)")
                word = tuple(digits)
                if word not in cache:
                    complex_displacements = []
                    for z in conjugates:
                        value = acb(0)
                        for digit in word:
                            value = value * z + digit
                        complex_displacements.append(value / (z**len(word)))
                    vector = [v.real for v in complex_displacements]
                    vector += [v.imag for v in complex_displacements]
                    squared = sum(v * v for v in vector)
                    require(squared > 0, "A normalized displacement denominator is not positive")
                    cache[word] = ([v / squared for v in vector], squared)
                vertex, squared = cache[word]
                vertices.append(vertex)
                costs.append(squared.lower())
                uses += 1
            augmented = arb_mat([[vertex[i] for vertex in vertices] for i in range(8)] +
                                [[arb(1)] * 9])
            target = [arb(0)] * 8 + [arb(1)]
            target[certificate['coordinate']] = certificate['sign'] * real(radius)
            weights = augmented.solve(arb_mat([[x] for x in target]))
            require(all(weights[i, 0] > 0 for i in range(9)),
                    "A signed axis target has no positive certified barycentric representation")
        drop = min(costs) * (16 * real(radius) / arb(8).sqrt() - 1)
        require(drop >= real(Fraction(57, 100)), "The uniform squared-radius drop fails")
        print('Closed expanding cell', row['cell'], 'drop >= 57/100; 16 axis certificates passed.')
    require(uses == 288 and len(cache) == 217 and max(map(len, cache)) == 11,
            "The complete adopted word family was not checked")


def rational_inverse(matrix):
    """Small exact Gauss-Jordan calculation, used only on the integer transform."""
    n = len(matrix)
    work = [[Fraction(v) for v in row] + [Fraction(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if work[i][j]), None)
        require(pivot is not None, "Singular integer transformation")
        work[j], work[pivot] = work[pivot], work[j]
        divisor = work[j][j]
        work[j] = [v / divisor for v in work[j]]
        for i in range(n):
            if i != j:
                multiplier = work[i][j]
                work[i] = [a - multiplier * b for a, b in zip(work[i], work[j])]
    return [row[n:] for row in work]


def enclosing_ellipsoid(certificate, beta, embedding):
    """Prove every actual compact point lies inside the enumerated integer region.

    K has |x+|<=1, |x-|<=S and rho<8.  Weighting the first two real coordinates
    by sqrt(8) and sqrt(8)/(67/10) gives norm at most sqrt(80), since S<67/10.
    B/Q approximates this weighted embedding in the power basis.  For a=b U,
    rational LDL of (U B)(U B)^T/Q^2 gives an exact triangular norm.  The two
    explicitly bounded approximation errors justify replacing it by T/H.
    """
    c = certificate
    for name in ('integer_rounded_weighted_embedding_basis', 'unimodular_U',
                 'integer_triangular_T', 'embedding_lower', 'embedding_upper'):
        matrix = c[name]
        require(len(matrix) == 10 and all(len(r) == 10 for r in matrix) and
                all(type(v) is int for r in matrix for v in r), 'Invalid integer matrix: ' + name)
    original = c['original_coefficient_bounds']
    require(tuple(original) == COEFFICIENT_BOUNDS, "Changed original finite coefficient domain")
    stable = beta / (beta - 1)
    require(stable < real(Fraction(67, 10)), "The containing stable bound fails")
    inverse_embedding = arb_mat(embedding).inv()
    for i, bound in enumerate(original):
        real_cost = abs(inverse_embedding[i, 0]) + stable * abs(inverse_embedding[i, 1])
        neutral_cost = 8 * length([inverse_embedding[i, j] for j in range(2, 10)])
        require(real_cost + neutral_cost < bound + 1, "An integer coefficient bound is insufficient")
    transform = c['unimodular_U']
    # An integral inverse proves unimodularity without trusting a saved determinant.
    inverse = rational_inverse(transform)
    require(all(v.denominator == 1 for row in inverse for v in row),
            "The integer transformation is not unimodular")
    reduced_bounds = [sum(original[i] * abs(int(inverse[i][j])) for i in range(10))
                      for j in range(10)]
    require(reduced_bounds == c['reduced_coefficient_bounds'], "Incorrect reduced coefficient bounds")
    Q, H, E = (c[k] for k in ('B_scale', 'T_scale', 'embedding_scale'))
    require((Q, H, E) == (10**8, 10**5, 10**6), "Changed rounding scales")
    B, T = c['integer_rounded_weighted_embedding_basis'], c['integer_triangular_T']
    basis = [[sum(transform[i][k] * B[k][j] for k in range(10)) for j in range(10)]
             for i in range(10)]
    gram = [[Fraction(sum(basis[i][k] * basis[j][k] for k in range(10)), Q * Q)
             for j in range(10)] for i in range(10)]
    lower = [[Fraction(i == j) for j in range(10)] for i in range(10)]
    diagonal = []
    for j in range(10):
        d = gram[j][j] - sum(lower[j][k]**2 * diagonal[k] for k in range(j))
        require(d > 0, "Nonpositive Gram pivot")
        diagonal.append(d)
        for i in range(j + 1, 10):
            lower[i][j] = (gram[i][j] - sum(lower[i][k] * lower[j][k] * diagonal[k]
                                          for k in range(j))) / d
    triangular_errors = []
    for j in range(10):
        require(T[j][j] > 0 and all(T[i][j] == 0 for i in range(j)), "Invalid triangular array")
        triangular_errors.append(sum(reduced_bounds[i] * abs(
            real(lower[i][j]) * real(diagonal[j]).sqrt() - real(Fraction(T[i][j], H)))
            for i in range(j, 10)))
    weights = [arb(8).sqrt(), arb(8).sqrt() / real(Fraction(67, 10))] + [arb(1)] * 8
    basis_errors = [sum(original[i] * abs(embedding[j][i] * weights[j] -
                                        real(Fraction(B[i][j], Q))) for i in range(10))
                    for j in range(10)]
    radius = c['squared_enumeration_radius']
    require(radius == 800554833912, "Changed enumeration ellipsoid")
    required_norm = arb(80).sqrt() + length(basis_errors) + length(triangular_errors)
    require(real(Fraction(radius, H * H)) > required_norm * required_norm,
            "The rounded ellipsoid does not contain every compact state")
    low, high = c['embedding_lower'], c['embedding_upper']
    for j in range(10):
        for i in range(10):
            require(real(Fraction(low[j][i], E)) <= embedding[j][i].lower() and
                    real(Fraction(high[j][i], E)) >= embedding[j][i].upper(),
                    "A coordinate filter rounds inward")
    require(real(Fraction(c['stable_outer_bound_scaled'], E)) >= stable.upper(),
            "The stable coordinate filter rounds inward")

    # All batch operations below are bounded *before* NumPy int64 is used.
    # The transform is applied before the original coefficient filter, so its
    # larger prefilter coordinate bound must also be checked.
    limit = 2**63 - 1
    require(all(sum(reduced_bounds[i] * abs(transform[i][j]) for i in range(10)) < limit
                for j in range(10)), "A prefilter basis conversion could overflow")
    coordinate_bound = [sum(original[i] * max(abs(low[j][i]), abs(high[j][i]))
                            for i in range(10)) for j in range(10)]
    require(max(coordinate_bound) < limit and
            sum(v * v for v in coordinate_bound[2:]) < limit and 64 * E * E < limit,
            "An outward embedding filter could overflow")
    require(all(abs(v) < limit for row in transform + low + high for v in row) and
            all(0 <= b < limit for b in reduced_bounds), "An int64 input is outside its range")
    return stable


def enumerate_compact(c):
    """Exhaust the certified integer ellipsoid; no supplied state list is trusted.

    Fix b_9,...,b_(j+1).  The j-th triangular coordinate is
    b_j*T[j,j]+sum_(i>j)b_i*T[i,j].  Integer square roots and ceiling/floor
    division enumerate precisely every integer b_j permitted by the remaining
    squared radius.  Conservative interval filters can remove no actual K_8
    state.  All ambiguity at a strip or neutral boundary remains retained.
    """
    T, bounds = c['integer_triangular_T'], c['reduced_coefficient_bounds']
    U = np.asarray(c['unimodular_U'], dtype=np.int64)
    low = np.asarray(c['embedding_lower'], dtype=np.int64)
    high = np.asarray(c['embedding_upper'], dtype=np.int64)
    original = np.asarray(c['original_coefficient_bounds'], dtype=np.int64)
    scale, stable = c['embedding_scale'], c['stable_outer_bound_scaled']
    require(c['node_cap'] == 50000000 and c['candidate_cap'] == 2000000, "Changed finite caps")
    targets = set()
    b = [0] * 10
    batch = []
    nodes = leaves = 0

    def process_batch():
        if not batch:
            return
        a = np.asarray(batch, dtype=np.int64) @ U
        batch.clear()
        a = a[np.all(np.abs(a) <= original, axis=1)]
        if len(a) == 0:
            return
        positive = np.maximum(a, 0)
        negative = np.minimum(a, 0)
        left = positive @ low.T + negative @ high.T
        right = positive @ high.T + negative @ low.T
        keep = (left[:, 0] <= scale) & (right[:, 0] >= -scale)
        keep &= (left[:, 1] <= stable) & (right[:, 1] >= -stable)
        smallest = np.where((left <= 0) & (right >= 0), 0,
                            np.minimum(np.abs(left), np.abs(right)))
        keep &= np.sum(smallest[:, 2:]**2, axis=1, dtype=np.int64) < 64 * scale * scale
        a = a[keep]
        # Use the ancestry encoding directly: ten five-bit coefficients +16.
        packed = np.zeros(len(a), dtype=np.uint64)
        for i in range(10):
            packed |= (a[:, i] + 16).astype(np.uint64) << np.uint64(5 * i)
        before = len(targets)
        targets.update(int(v) for v in packed)
        require(len(targets) == before + len(a), "Duplicate enumerated compact state")
        require(len(targets) < c['candidate_cap'], "Candidate cap reached")

    def descend(j, remaining):
        nonlocal nodes, leaves
        nodes += 1
        require(nodes < c['node_cap'] and remaining >= 0, "Incomplete ellipsoid traversal")
        if j == -1:
            leaves += 1
            batch.append(b.copy())
            if len(batch) >= 40000:
                process_batch()
            return
        center = sum(b[i] * T[i][j] for i in range(j + 1, 10))
        span, step = isqrt(remaining), T[j][j]
        first = max(-bounds[j], -((span + center) // step))
        last = min(bounds[j], (span - center) // step)
        for value in range(first, last + 1):
            b[j] = value
            coordinate = value * step + center
            descend(j - 1, remaining - coordinate * coordinate)

    descend(9, c['squared_enumeration_radius'])
    process_batch()
    require((nodes, leaves, len(targets)) == (4818379, 3077691, 797507),
            "The full adopted finite domain was not reproduced")
    print('Complete enumeration:', nodes, 'nodes;', leaves, 'leaves;', len(targets), 'distinct candidates.')
    return targets


def digits_from_key(key):
    return [(key >> (5 * i) & 31) - 16 for i in range(10)]


def paths_and_exclusions(targets, embedding, stable):
    """Check all saved integer edges and prove every uncovered target lies outside K_8.

    Record n is <QIB in little-endian order: state key, earlier parent index,
    digit+1.  The first record is zero.  At every other record, strict decrease
    of the parent index proves termination.  The exact monic reduction of
    t*a(t)+digit modulo P must equal the parent's complete coefficient vector.
    Its depth is therefore the actual length of an original-digit zero word.
    """
    raw = gzip.decompress((HERE / 'return-paths.bin.gz').read_bytes())
    require(len(raw) == 13 * 1044588, "Incomplete ancestry input")
    keys, depths = array('Q'), array('I')
    seen = set()
    maximum = 0
    for key, parent, code in struct.iter_unpack('<QIB', raw):
        index = len(keys)
        require(key < 1 << 50 and key not in seen and code in (0, 1, 2), "Invalid ancestry record")
        coefficients = digits_from_key(key)
        if index == 0:
            require(coefficients == [0] * 10 and parent == 0 and code == 1, "The ancestry root is not zero")
            depth = 0
        else:
            require(parent < index, "Nondecreasing ancestry parent")
            top = coefficients[9]
            successor = [code - 1 - top]
            successor += [coefficients[i - 1] - top * POLYNOMIAL[i] for i in range(1, 10)]
            require(successor == digits_from_key(keys[parent]), "An integer original-digit edge fails")
            depth = depths[parent] + 1
        keys.append(key)
        depths.append(depth)
        seen.add(key)
        targets.discard(key)
        maximum = max(maximum, depth)
    require(len(keys) == 1044588 and maximum == 25 and len(targets) == 70,
            "The adopted ancestry/coverage scope has changed")
    reasons = {'neutral': 0, 'contracting': 0}
    for key in sorted(targets):
        a = digits_from_key(key)
        values = [sum((a[i] * row[i] for i in range(10)), arb(0)) for row in embedding]
        neutral = sum(v * v for v in values[2:])
        if abs(values[1]) > stable:
            reasons['contracting'] += 1
        elif neutral >= 64:
            reasons['neutral'] += 1
        else:
            raise ValueError('Uncovered actual compact state: ' + str(a))
    require(reasons == {'neutral': 68, 'contracting': 2}, "Unexpected exact exclusion partition")
    print('Exact paths:', len(keys), 'acyclic nodes; 797437 covered candidates; maximum length', maximum)
    print('All 70 others excluded: 68 by rho^2 >= 64, 2 by the contracting strip.')


def main():
    ctx.prec = 360
    payload = json.loads((HERE / 'return-core.json').read_text(encoding='utf-8'))
    require(payload['polynomial_ascending'] == list(POLYNOMIAL), "Wrong original polynomial")
    beta, conjugates, embedding = algebraic_embeddings()
    print('Original polynomial, trace identity, irreducibility and all conjugates verified.')
    normalized_descent(payload['normalized_descent'], beta, conjugates)
    stable = enclosing_ellipsoid(payload['enumeration'], beta, embedding)
    targets = enumerate_compact(payload['enumeration'])
    paths_and_exclusions(targets, embedding, stable)
    print('PASS: the complete finite neutral-descent and compact-termination premise of the return-core theorem.')


if __name__ == '__main__':
    main()
