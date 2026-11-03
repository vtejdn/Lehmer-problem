"""Complete actual ideal-slice isolation and exact integer return identities."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import time
from exact import (roots, embeddings, inverse, point, absolute, add, mul,
                   div, sub, total, square, sqrt_interval, floor)

RADIUS = F(5, 2)
BOUNDS = (2, 2, 2, 1, 1, 2)
EXPECTED = {(-1, -1, -2, 0, 0, 1), (0, 0, 0, 0, 0, 0), (1, 1, 2, 0, 0, -1)}


def residue(coeff):
    value = 0
    for a, power in zip(coeff, (1, 2, 3, 1, 2, 3)):
        if a % 2: value ^= power
    return value


def step(coeff, digit):
    # beta^6=-1+beta+beta^3+beta^5.
    tail = coeff[-1]
    return (digit-tail, coeff[0]+tail, coeff[1], coeff[2]+tail, coeff[3], coeff[4]+tail)


def main():
    started = time.monotonic()
    beta, zs = roots()
    S = div(beta, sub(beta, point(1)))
    E = embeddings(beta, zs)
    inv = inverse(E)
    coefficient_upper = []
    for row, bound in zip(inv, BOUNDS):
        real = add(absolute(row[0]), mul(S, absolute(row[1])))
        neutral = mul(point(RADIUS), sqrt_interval(total(square(x) for x in row[2:])))
        upper = add(real, neutral)[1]
        assert floor(upper) == bound
        coefficient_upper.append(str(F(-floor(-upper*10**6), 10**6)))
    tested = 0
    counts = {'nonzero_residue': 0, 'real_excluded': 0, 'stable_excluded': 0,
              'neutral_excluded': 0, 'retained': 0}
    retained = []
    for coeff in product(*(range(-bound, bound+1) for bound in BOUNDS)):
        tested += 1
        if residue(coeff):
            counts['nonzero_residue'] += 1
            continue
        values = [total(mul(point(a), e) for a, e in zip(coeff, row)) for row in E]
        if absolute(values[0])[0] > 1:
            counts['real_excluded'] += 1
            continue
        if absolute(values[1])[0] > S[1]:
            counts['stable_excluded'] += 1
            continue
        norm2 = total(square(value) for value in values[2:])
        if norm2[0] > RADIUS**2:
            counts['neutral_excluded'] += 1
            continue
        # Every possible undecided state must be retained; here all retained
        # states are also proved to belong to the complete closed slice.
        assert absolute(values[0])[1] <= 1
        assert absolute(values[1])[1] <= S[0]
        assert norm2[1] <= RADIUS**2
        counts['retained'] += 1
        retained.append({'coefficients': list(coeff),
                         'real_enclosure': [str(x) for x in values[0]],
                         'stable_enclosure': [str(x) for x in values[1]],
                         'neutral_squared_enclosure': [str(x) for x in norm2]})
    assert tested == 5625
    assert {tuple(row['coefficients']) for row in retained} == EXPECTED
    a = (-1, -1, -2, 0, 0, 1)
    beta3a = a
    for _ in range(3): beta3a = step(beta3a, 0)
    assert beta3a == (-1, 0, 0, 1, 0, 0)
    word = (-1, 0, 0, 0, -1, 1)
    returns = []
    for sign in (1, -1):
        state = tuple(sign*x for x in a)
        path = [list(state)]
        for digit in word:
            state = step(state, sign*digit)
            path.append(list(state))
        assert state == (0,)*6
        returns.append({'initial': [sign*x for x in a],
                        'digits': [sign*x for x in word], 'integer_path': path})
    output = {'coefficient_bounds': list(BOUNDS), 'coefficient_upper_bounds': coefficient_upper, 'all_box_tuples': tested, 'classification': counts, 'retained': retained, 'radius': str(RADIUS), 'exact_returns': returns}
    (_J_OUTPUT / 'compact_verification.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v for k, v in output.items() if k not in ('retained', 'exact_returns')}))


if __name__ == '__main__': main()
