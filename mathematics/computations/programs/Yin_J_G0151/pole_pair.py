"""Complete one fixed R=101/100 cover using the original integer pole.

Only the first N=7 triple (10,18,27), the prior four retained duals,
and the stated 4096-cell partition are checked. No optimizer is called.
"""

from fractions import Fraction as F
import json
from pathlib import Path

from flint import ctx
from endpoint_cover import prepare, bound, CELLS, S_LEFT, S_RIGHT, D_LEFT, D_RIGHT
from endpoint_dual import ball


def pole_gap(left, right):
    s = ball(left).union(ball(right))
    d = ball(D_LEFT).union(ball(D_RIGHT))
    y = ball(F(-161, 100))
    z_at_pole = (s + 1) * (s + 1) - d
    available = 1 - 3 * s * s - d + 2 * y * s
    # Every original input requires z_at_pole * available > required.
    required = ball(F(9 * 61 * 32, 100 * 19683))
    result = required - z_at_pole * available
    assert result.is_finite()
    return result


def main():
    ctx.prec = 256
    source = Path(__file__).resolve()
    native = json.loads((source.parent / 'inputs/endpoint_first_duals.json').read_text())
    assert native['triple'] == [10, 18, 27]
    assert len(native['certificates']) == 4
    prepared = [prepare(item) for item in native['certificates']]
    counts = [0] * 5
    unresolved = []
    gap_lower = None
    for i in range(CELLS):
        left = S_LEFT + (S_RIGHT - S_LEFT) * F(i, CELLS)
        right = S_LEFT + (S_RIGHT - S_LEFT) * F(i + 1, CELLS)
        # Preserve the old four-dual order to identify exactly its former gap.
        for j, data in enumerate(prepared):
            if bound(data, left, right) > 0:
                counts[j] += 1
                break
        else:
            gap = pole_gap(left, right)
            if gap > 0:
                counts[4] += 1
                lower = gap.lower()
                gap_lower = lower if gap_lower is None or lower < gap_lower else gap_lower
            else:
                unresolved.append([str(left), str(right), str(gap)])
    assert sum(counts) + len(unresolved) == CELLS
    result = {
        'triple': [10, 18, 27], 'measure_target': '101/100',
        'cells': CELLS, 's': [str(S_LEFT), str(S_RIGHT)],
        'd': [str(D_LEFT), str(D_RIGHT)], 'h_at_minus_one': 32,
        'cut_scope': 'whole inherited interval',
        'first_success_counts': counts, 'pole_gap_lower': str(gap_lower),
        'unresolved_count': len(unresolved), 'unresolved': unresolved,
        'complete': not unresolved,
    }
    output = source.parents[2] / 'outputs' / source.parent.name
    output.mkdir(parents=True, exist_ok=True)
    (output / 'pole_pair_cover.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)
    assert result['complete']


if __name__ == '__main__':
    main()
