"""Noncontributor certificate check using exact Bernstein bounds.

Imports no author program.  Verifies a separately chosen rational partition,
then validates the author open intervals and saved closed-cell enclosures.
All real tests cover the full parameter interval, not sampled beta values.
"""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import json


LO, HI = F(3, 2), F(151, 100)
WORDS = [
    [(1, 1, -1), (), (0, -1, -1, -1)],
    [(1, 1), (1, 0, -1, 1), (1, -1), (-1, 1),
     (-1, 0, -1, 1), (-1, -1)],
    [(1, 0, 1), (0, 1), (0, 0, -1, 1), (0, -1), (-1, 0, -1)],
    [(1,), (0, -1, 1), (-1,)],
]
CUTS = [
    ['-1', '-3/4', '7/8', '1'],
    ['-1', '-7/10', '-1/2', '0', '5/8', '4/5', '1'],
    ['-1', '-3/4', '-1/20', '1/8', '3/4', '1'],
    ['-1', '-1/10', '1/5', '1'],
]


def bernstein(point, word):
    """Coefficients of T_word(point) at beta=LO+(HI-LO)*u, u in[0,1]."""
    n = len(word)
    coefficients = [F(d) for d in reversed(word)] + [F(point)]
    power = [sum(coefficients[i] * comb(i, j) * LO**(i-j)
                 * (HI-LO)**j for i in range(j, n+1))
             for j in range(n+1)]
    return [sum(power[j] * F(comb(k, j), comb(n, j))
                for j in range(k+1)) for k in range(n+1)]


def residue(start, word):
    # Carry the whole polynomial as bits, reducing by t^2+t+1.
    value = start
    for digit in word:
        value = (value << 1) ^ (digit & 1)
        while value.bit_length() > 2:
            value ^= 0b111 << (value.bit_length()-3)
    return value


def cell_bounds(left, right, word):
    assert left < right
    assert len(word) <= 4 and all(d in (-1, 0, 1) for d in word)
    return min(bernstein(left, word)), max(bernstein(right, word))


def multiply_mod2(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def main():
    directory = (_J_PROGRAM / 'review_exact.py').parent
    author_names = ['main.py', 'verify.py', 'certificate.json',
                    'verification.json', 'readme.md']
    fingerprints = {name: sha256((((_J_PROGRAM if name in ('main.py', 'readme.md', 'review_exact.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()).hexdigest()
                    for name in author_names}
    certificate = json.loads(((_J_OUTPUT / 'certificate.json')).read_text())
    saved = json.loads(((_J_OUTPUT / 'verification.json')).read_text())
    assert tuple(map(F, certificate['beta_interval'])) == (LO, HI)
    assert certificate['max_length'] == 4
    assert [c['initial_residue'] for c in certificate['covers']] == list(range(4))
    cells = []
    for state, words in enumerate(WORDS):
        cuts = list(map(F, CUTS[state]))
        assert cuts[0] == -1 and cuts[-1] == 1
        assert len(cuts) == len(words)+1
        assert [tuple(row['word']) for row in certificate['covers'][state]['selected']] == words
        for word, left, right in zip(words, cuts, cuts[1:]):
            assert residue(state, word) == 0
            low, high = cell_bounds(left, right, word)
            assert -1 < low <= high < 1
            cells.append({'residue': state, 'word': list(word),
                          'closed_cell': [str(left), str(right)],
                          'bernstein_enclosure': [str(low), str(high)],
                          'margin': str(min(1+low, 1-high))})

    # The author's open intervals allow equality at an endpoint. Positive
    # slope beta^length makes every interior point strictly admissible.
    open_count = 0
    for cover in certificate['covers']:
        state = cover['initial_residue']
        intervals = []
        for row in cover['selected']:
            word = tuple(row['word'])
            left, right = map(F, row['inner_interval'])
            low, high = cell_bounds(left, right, word)
            assert -1 <= low <= high <= 1
            assert residue(state, word) == 0
            intervals.append((left, right))
            open_count += 1
        assert intervals[0][0] < -1 and intervals[-1][1] > 1
        assert all(max(a[0], b[0]) < min(a[1], b[1])
                   for a, b in zip(intervals, intervals[1:]))

    # Validate the soundness of each saved author enclosure using a different
    # polynomial representation; do not claim to reproduce its interval code.
    saved_margins = []
    for state in range(4):
        rows = [row for row in saved['cells'] if row['initial_residue'] == state]
        assert [tuple(row['word']) for row in rows] == WORDS[state]
        assert F(rows[0]['closed_cell'][0]) == -1
        assert F(rows[-1]['closed_cell'][1]) == 1
        for first, second in zip(rows, rows[1:]):
            assert F(first['closed_cell'][1]) == F(second['closed_cell'][0])
        for row in rows:
            left, right = map(F, row['closed_cell'])
            low, high = cell_bounds(left, right, tuple(row['word']))
            stored_low, stored_high = map(F, row['image_enclosure'])
            assert -1 < stored_low <= low <= high <= stored_high < 1
            margin = min(1+stored_low, 1-stored_high)
            assert margin == F(row['strict_margin'])
            saved_margins.append(margin)
    assert len(saved_margins) == saved['verified_closed_cells'] == 17
    assert min(saved_margins) == F(saved['minimum_strict_margin']) == F(27, 320)

    all_words = [w for n in range(5) for w in product((-1, 0, 1), repeat=n)]
    counts = [sum(residue(r, w) == 0 for w in all_words) for r in range(4)]
    assert len(all_words) == certificate['candidate_words'] == 121
    assert counts == certificate['admissible_counts'] == [33, 28, 26, 34]
    polynomial = [1, -1, 0, -1, 0, -1, 1]
    values = [sum(F(c)*beta**i for i, c in enumerate(polynomial))
              for beta in (LO, HI)]
    assert values == list(map(F, certificate['P6_endpoint_values']))
    assert values[0] < 0 < values[1]
    assert multiply_mod2(multiply_mod2(0b111, 0b111), 0b111) == sum((c & 1) << i for i, c in enumerate(polynomial))
    assert fingerprints == {name: sha256((((_J_PROGRAM if name in ('main.py', 'readme.md', 'review_exact.py', 'verify.py') else _J_OUTPUT) / name)).read_bytes()).hexdigest()
                            for name in author_names}
    output = {'method': 'independent rational Bernstein polynomial bounds and polynomial-bit quotient arithmetic', 'author_files': list(author_names), 'independent_closed_cells': len(cells), 'independent_minimum_margin': str(min((F(c['margin']) for c in cells))), 'author_open_intervals_validated': open_count, 'author_closed_enclosures_validated': len(saved_margins), 'author_claimed_minimum_margin_validated': str(min(saved_margins)), 'candidate_words': len(all_words), 'residue_admissible_counts': counts, 'P6_endpoint_values': list(map(str, values)), 'P6_mod2_identity_verified': True, 'cells': cells}
    ((_J_OUTPUT / 'review_verification.json')).write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in output.items()
                      if k != 'cells'}))


if __name__ == '__main__':
    main()
