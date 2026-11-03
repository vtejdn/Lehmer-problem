"""Author cross-check: forward rational interval bounds and polynomial residues.

Does not import the interval-search implementation. This is not an independent
review: both programs were written by the drafting agent.
"""

from fractions import Fraction as F
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)


def product_bounds(x, y):
    values = [a * b for a in x for b in y]
    return min(values), max(values)


def image_range(point, word, beta):
    interval = (point, point)
    for digit in word:
        interval = tuple(v + digit for v in product_bounds(interval, beta))
    return interval


def residue_after(start, word):
    # Independent polynomial reduction using b^2=b+1 over F2.
    a, b = start & 1, (start >> 1) & 1
    for digit in word:
        a, b = (b + digit) % 2, (a + b) % 2
    return a + 2*b


def main():
    path = (_J_OUTPUT / 'certificate.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    beta = tuple(map(F, data['beta_interval']))
    assert beta == (F(3, 2), F(151, 100))
    assert [c['initial_residue'] for c in data['covers']] == list(range(4))
    checked = []
    for cover in data['covers']:
        rows = cover['selected']
        intervals = [tuple(map(F, row['inner_interval'])) for row in rows]
        boundaries = [F(-1)]
        assert intervals[0][0] < -1
        assert intervals[-1][1] > 1
        for first, second in zip(intervals, intervals[1:]):
            left, right = max(first[0], second[0]), min(first[1], second[1])
            assert left < right
            boundaries.append((left+right)/2)
        boundaries.append(F(1))
        assert all(a < b for a, b in zip(boundaries, boundaries[1:]))
        for row, left, right in zip(rows, boundaries, boundaries[1:]):
            word = row['word']
            assert len(word) <= 4 and all(d in (-1, 0, 1) for d in word)
            assert residue_after(cover['initial_residue'], word) == 0
            # For fixed beta, the word is strictly increasing in x. Enclose
            # the two closed-cell endpoints independently for every beta.
            low = image_range(left, word, beta)[0]
            high = image_range(right, word, beta)[1]
            assert -1 < low <= high < 1, (cover['initial_residue'], word, low, high)
            checked.append({'initial_residue': cover['initial_residue'],
                            'word': word, 'closed_cell': [str(left), str(right)],
                            'image_enclosure': [str(low), str(high)],
                            'strict_margin': str(min(low+1, 1-high))})
    result = {'verified_closed_cells': len(checked), 'max_length': 4,
              'minimum_strict_margin': str(min(F(c['strict_margin']) for c in checked)),
              'cells': checked}
    (_J_OUTPUT / 'verification.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'cells'}))


if __name__ == '__main__':
    main()
