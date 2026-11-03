"""Exact finite identities for the actual-order block-alphabet obstruction.

Only standard-library integer and Fraction arithmetic is used.
"""
from fractions import Fraction as F
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

D = 6
ZERO = (0,)*D
ONE = (1, 0, 0, 0, 0, 0)
BETA = (0, 1, 0, 0, 0, 0)
INV_BETA = (1, 0, 1, 0, 1, -1)


def add(a, b): return tuple(x+y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def sub(a, b): return add(a, neg(b))


def mul(a, b):
    work = [0]*(2*D-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): work[i+j] += x*y
    for k in range(len(work)-1, D-1, -1):
        coefficient = work[k]
        # t^6=t^5+t^3+t-1.
        for shift, sign in ((5, 1), (3, 1), (1, 1), (0, -1)):
            work[k-D+shift] += sign*coefficient
        work[k] = 0
    return tuple(work[:D])


def power(a, n):
    value = ONE
    for _ in range(n): value = mul(value, a)
    return value


def determinant(matrix):
    A = [list(row) for row in matrix]
    sign, previous = 1, 1
    for k in range(D-1):
        pivot = next(i for i in range(k, D) if A[i][k])
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        p = A[k][k]
        for i in range(k+1, D):
            for j in range(k+1, D):
                numerator = A[i][j]*p-A[i][k]*A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator//previous
            A[i][k] = 0
        previous = p
    return sign*A[-1][-1]


def solve(matrix, rhs):
    A = [[F(value) for value in row]+[F(r)] for row, r in zip(matrix, rhs)]
    for k in range(D):
        pivot = next(i for i in range(k, D) if A[i][k])
        A[k], A[pivot] = A[pivot], A[k]
        p = A[k][k]
        A[k] = [value/p for value in A[k]]
        for i in range(D):
            if i == k: continue
            q = A[i][k]
            A[i] = [x-q*y for x, y in zip(A[i], A[k])]
    solution = tuple(row[-1] for row in A)
    assert all(sum(F(a)*b for a, b in zip(row, solution)) == value
               for row, value in zip(matrix, rhs))
    return solution


def apply_word(state, digits):
    path = [state]
    for digit in digits:
        assert digit in (-1, 0, 1)
        state = add(mul(BETA, state), (digit, 0, 0, 0, 0, 0))
        path.append(state)
    return state, path


def interval_mul(left, right):
    products = [x*y for x in left for y in right]
    return min(products), max(products)


def evaluate_interval(coefficients, domain):
    result = (F(0), F(0))
    for coefficient in reversed(coefficients):
        result = interval_mul(result, domain)
        result = tuple(value+coefficient for value in result)
    return result


def main():
    assert mul(BETA, INV_BETA) == ONE
    theta = power(BETA, 6)
    columns = [power(theta, i) for i in range(D)]
    matrix = [[column[i] for column in columns] for i in range(D)]
    det = determinant(matrix)
    assert det == 1024
    beta_coordinates = solve(matrix, BETA)
    assert beta_coordinates == tuple(F(x, 16) for x in (7, 41, 14, 14, -13, 1))
    a = sub(ONE, power(INV_BETA, 3))
    assert a == (-1, -1, -2, 0, 0, 1)
    g = mul(theta, a)
    assert g == (-1, 1, 0, 0, 0, 1)
    w = (-1, 0, 0, 0, -1, 1)
    assert apply_word(a, w)[0] == ZERO
    assert apply_word(ZERO, w)[0] == neg(g)

    x1 = mul(a, sub(BETA, ONE))
    y1 = mul(power(INV_BETA, 6), sub(BETA, ONE))
    assert mul(g, y1) == x1
    original_return = (0, 0, -1, -1, 1, 0)
    end, return_path = apply_word(x1, original_return)
    assert end == ZERO
    assert mul(theta, x1) == (0, -1, 1, 1, 0, 0)
    y1_coordinates = solve(matrix, y1)
    assert any(value.denominator != 1 for value in y1_coordinates)

    y2 = mul(power(INV_BETA, 3), power(sub(BETA, ONE), 2))
    x2 = mul(sub(power(BETA, 3), ONE), power(sub(BETA, ONE), 2))
    assert mul(g, y2) == x2
    y2_coordinates = solve(matrix, y2)
    assert any(value.denominator != 1 for value in y2_coordinates)

    lower, upper = F(3, 2), F(151, 100)
    # S=beta/(beta-1)>1. These sufficient rational bounds validate
    # both real coordinates of x1 and the smaller macro strips for y2.
    x1_plus_bound = upper-1
    x1_minus_bound = (upper**3-1)*(1-1/upper)
    assert x1_plus_bound < 1 and x1_minus_bound < 1
    y2_plus_bound = (upper-1)**2/lower**3
    y2_minus_bound = upper*(upper-1)**2
    assert y2_plus_bound < 1/(upper**6-1)
    assert y2_minus_bound < 1

    v = (-1, 0, -1, 0, -1, 1)
    endpoint, prefixes = apply_word(ONE, v)
    assert endpoint == ZERO
    assert prefixes[5] == neg(INV_BETA)
    prefix_bounds = [evaluate_interval(state, (lower, upper)) for state in prefixes]
    assert all(-1 <= low <= high <= 1 for low, high in prefix_bounds)
    prefix_columns = prefixes[:D]
    prefix_matrix = [[column[i] for column in prefix_columns] for i in range(D)]
    assert determinant(prefix_matrix) == 1

    # One exact finite illustration of the symbolic all-h argument in D68.
    # It is not an enumeration over h and is not its proof.
    h = 7
    cyclic_word = v+(1,)
    cyclic_generator = sub(power(BETA, h), ONE)
    assert apply_word(ONE, cyclic_word)[0] == ONE
    a_h = sub(ONE, power(INV_BETA, h))
    assert apply_word(a_h, cyclic_word)[0] == ZERO
    cyclic_records = []
    for j in range(h):
        rotated = cyclic_word[j:]+cyclic_word[:j]
        translation = apply_word(ZERO, rotated)[0]
        divided_digit = neg(apply_word(ONE, cyclic_word[:j])[0])
        assert translation == mul(cyclic_generator, divided_digit)
        cyclic_records.append({'rotation': j, 'word': rotated,
                               'translation': translation, 'divided_digit': divided_digit})

    output = {'power_coordinate_matrix': matrix, 'determinant': det,
              'beta_in_theta_basis': list(map(str, beta_coordinates)),
              'a': a, 'g': g, 'generator_return': w,
              'first_witness': {'x': x1, 'scaled_y': y1,
                                'scaled_y_theta_coordinates': list(map(str, y1_coordinates)),
                                'original_return': original_return, 'integer_path': return_path},
              'inner_strip_witness': {'x': x2, 'scaled_y': y2,
                                      'scaled_y_theta_coordinates': list(map(str, y2_coordinates)),
                                      'plus_upper_bound': str(y2_plus_bound),
                                      'macro_plus_radius_lower_bound': str(1/(upper**6-1)),
                                      'minus_upper_bound': str(y2_minus_bound)},
              'real_interval': [str(lower), str(upper)],
              'first_witness_real_bounds': [str(x1_plus_bound), str(x1_minus_bound)],
              'return_of_one': {'word': v, 'prefixes': prefixes,
                                'rational_prefix_bounds': [[str(x) for x in pair] for pair in prefix_bounds],
                                'prefix_basis_determinant': determinant(prefix_matrix)},
              'cyclic_rotation_illustration': {'h': h, 'word': cyclic_word,
                                               'generator': cyclic_generator,
                                               'rotations': cyclic_records}}
    (_J_OUTPUT / 'verification.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output))


if __name__ == '__main__': main()
