"""Whole-cell Arb certificate, with an explicit prior component enclosure."""
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'repository/config.json').is_file())
OUTPUT = ROOT / 'mathematics/computations/outputs' / HERE.name
INPUT = ROOT / 'mathematics/computations/programs/Yin_J_G0097/input.json'
PRIOR = ROOT / 'mathematics/computations/outputs/Yin_J_G0100/results.json'
PC = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
CELLS, BITS, THRESHOLD, TIMEOUT = 8192, 192, 4, 120


def save(payload):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pending = OUTPUT / 'results.json.writing'
    pending.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    pending.replace(OUTPUT / 'results.json')


def worker():
    import flint
    from flint import arb, ctx
    ctx.prec = BITS
    native = json.loads(INPUT.read_text(encoding='utf-8'))
    selected = [r for r in native['inputs'] if r['name'] == 'Lehmer_degree10']
    assert len(selected) == 1 and selected[0]['coefficients_ascending'] == PC
    assert PC == PC[::-1] and PC[0] == PC[-1] == 1
    old = json.loads(PRIOR.read_text(encoding='utf-8'))
    assert old['complete'] and old['reported_absolute_error_bound'] == '1e-10'
    rows = [r for r in old['inputs'] if r['name'] == 'Lehmer_degree10']
    assert len(rows) == 1 and rows[0]['p_coefficients_ascending'] == PC
    old_sum = rows[0]['quantities']['screen_sum']
    assert old_sum['absolute_error_bound'] == '1e-10'
    screen = arb(old_sum['ball'])
    assert screen.is_finite() and screen.rad() < arb('1e-10') and screen < 0

    def centered(x):
        return PC[5] + sum(2 * PC[5 + k] * (2 * k * x).cos_pi()
                           for k in range(1, 6) if PC[5 + k])

    positive, negative = [], []
    for k in range(CELLS):
        # Both arguments are exact dyadic rationals, and Arb encloses endpoints.
        phase = arb(arb(2 * k + 1) / (2 * CELLS), arb(1) / (2 * CELLS))
        assert phase.contains(arb(k) / CELLS)
        assert phase.contains(arb(k + 1) / CELLS)
        a, b, c = centered(2 * phase) / 2, centered(3 * phase) / 3, centered(5 * phase) / 5
        e, g = b**2 - a**3, c**3 - 2 * b**5
        if g.contains(0):
            continue
        ratio = e / g
        if ratio > THRESHOLD:
            positive.append(k)
        elif ratio < -THRESHOLD:
            negative.append(k)
    assert not set(positive).intersection(negative)
    count = min(len(positive), len(negative))
    assert count > 0
    eta = arb(count) / CELLS
    delta = eta * arb(9).log()
    strengthened = screen + delta
    margin = strengthened / 2
    lower = arb(2).log() + margin
    assert strengthened > 0

    def enclosing(x):
        result = x.str(55, more=True)
        assert arb(result).contains(x)
        return result

    payload = {'complete': True, 'input_name': 'Lehmer_degree10',
               'p_coefficients_ascending': PC, 'flint_version': flint.__version__,
               'precision_bits': BITS, 'cell_count': CELLS, 'threshold': THRESHOLD,
               'batch_timeout_seconds': TIMEOUT,
               'positive_cells': positive, 'negative_cells': negative,
               'positive_count': len(positive), 'negative_count': len(negative),
               'eta_numerator': count, 'eta_denominator': CELLS,
               'prior_source': 'mathematics/computations/outputs/Yin_J_G0100/results.json',
               'prior_screen_sum': old_sum,
               'quantities': {'delta': enclosing(delta),
                              'strengthened_screen': enclosing(strengthened),
                              'margin_above_log2': enclosing(margin),
                              'all_real_s_positive_q_lower_bound': enclosing(lower)},
               'scope': 'Every real s and positive real q, only this original input and buffered family.'}
    save(payload)
    print(json.dumps({k: payload[k] for k in ('complete', 'positive_count', 'negative_count', 'quantities')}, indent=2))


if __name__ == '__main__':
    if '--worker' in sys.argv:
        worker()
    else:
        try:
            result = subprocess.run([sys.executable, '-B', str(Path(__file__).resolve()), '--worker'],
                                    text=True, capture_output=True, timeout=TIMEOUT)
            print(result.stdout, end='')
            if result.returncode:
                save({'complete': False, 'failure': result.stderr, 'cell_count': CELLS,
                      'precision_bits': BITS, 'threshold': THRESHOLD})
                print(result.stderr, file=sys.stderr)
            raise SystemExit(result.returncode)
        except subprocess.TimeoutExpired:
            save({'complete': False, 'failure': 'subprocess timeout', 'seconds': TIMEOUT})
            raise
