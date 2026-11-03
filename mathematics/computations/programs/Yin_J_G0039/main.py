"""Exact bounded real-entry certificate; standard-library rational arithmetic."""

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)

BETA = (F(3, 2), F(151, 100))
MUL_B = (0, 2, 3, 1)  # polynomial-basis bit encoding 0,1,b,b+1
MAX_LENGTH = 4
SIMPLE_INTERVALS = {
    (1, 1, -1): ('-11/10', '-53/100'),
    (): ('-1', '1'),
    (0, -1, -1, -1): ('3/4', '11/10'),
    (1, 1): ('-3/2', '-2/3'),
    (1, 0, -1, 1): ('-3/4', '-2/5'),
    (1, -1): ('-13/20', '1/5'),
    (-1, 1): ('-1/5', '13/20'),
    (-1, 0, -1, 1): ('3/5', '9/10'),
    (-1, -1): ('2/3', '3/2'),
    (1, 0, 1): ('-6/5', '-2/3'),
    (0, 1): ('-4/5', '0'),
    (0, 0, -1, 1): ('-9/100', '1/4'),
    (0, -1): ('0', '4/5'),
    (-1, 0, -1): ('2/3', '6/5'),
    (1,): ('-13/10', '0'),
    (0, -1, 1): ('-7/50', '2/5'),
    (-1,): ('0', '13/10'),
}


def divide_positive(interval, denominator):
    quotients = [a / b for a in interval for b in denominator]
    return min(quotients), max(quotients)


def endpoint_range(word, endpoint):
    value = (F(endpoint), F(endpoint))
    for digit in reversed(word):
        value = divide_positive(tuple(a - digit for a in value), BETA)
    return value


def inner_interval(word):
    return endpoint_range(word, -1)[1], endpoint_range(word, 1)[0]


def final_residue(start, word):
    state = start
    for digit in word:
        state = MUL_B[state] ^ (digit % 2)
    return state


def encode(value):
    return str(value)


def main():
    words = [w for n in range(MAX_LENGTH + 1)
             for w in product((-1, 0, 1), repeat=n)]
    covers = []
    admissible_counts = []
    for state in range(4):
        candidates = [(inner_interval(w), w) for w in words
                      if final_residue(state, w) == 0]
        admissible_counts.append(len(candidates))
        frontier = F(-1)
        chosen = []
        while frontier <= 1:
            choices = [(bounds, w) for bounds, w in candidates
                       if bounds[0] < frontier < bounds[1]]
            assert choices, (state, frontier, 'uncovered point')
            bounds, word = max(choices, key=lambda row: (row[0][1], -len(row[1])))
            chosen.append({'word': list(word),
                           'inner_interval': [encode(v) for v in bounds]})
            frontier = bounds[1]
        covers.append({'initial_residue': state, 'selected': chosen})

    # Replace discovery endpoints by simple exact inward rational bounds.
    # The forward verifier independently checks the resulting closed cover.
    for cover in covers:
        for row in cover['selected']:
            lo, hi = map(F, row['inner_interval'])
            a, b = map(F, SIMPLE_INTERVALS[tuple(row['word'])])
            assert lo <= a < b <= hi
            row['inner_interval'] = [str(a), str(b)]

    # Isolate the already known unique real Salem root above one.
    def P(x):
        return x**6 - x**5 - x**3 - x + 1
    assert P(BETA[0]) < 0 < P(BETA[1])
    output = {'beta_interval': [encode(v) for v in BETA],
              'max_length': MAX_LENGTH, 'candidate_words': len(words),
              'admissible_counts': admissible_counts,
              'covers': covers,
              'P6_endpoint_values': [encode(P(v)) for v in BETA]}
    target = (_J_OUTPUT / 'certificate.json')
    target.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'candidate_words': len(words),
                      'selected_per_state': [len(c['selected']) for c in covers],
                      'max_length': MAX_LENGTH,
                      'P6_endpoint_values': output['P6_endpoint_values']}))


if __name__ == '__main__':
    main()
