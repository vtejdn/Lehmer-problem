"""Declared complete orthogonal sign-column profile test; standard library only."""
from collections import defaultdict
from itertools import product
import json
from pathlib import Path

_J_PROGRAM = Path(__file__).resolve().parent
_J_ROOT = next(parent for parent in _J_PROGRAM.parents if (parent / 'repository/config.json').is_file())
_J_OUTPUT = _J_ROOT / 'mathematics/computations/outputs' / _J_PROGRAM.name
_J_OUTPUT.mkdir(parents=True, exist_ok=True)
import time


def main():
    started = time.perf_counter()
    cases = []
    for rank in (2, 3, 4, 5):
        columns = [(1,) + s for s in product((-1, 1), repeat=rank - 1)]
        b = len(columns)
        zero = (0,) * rank
        counts = {zero: 1}
        for column in columns:
            fresh = defaultdict(int)
            for z, c in counts.items():
                for sign, weight in ((-1, 1), (0, 2), (1, 1)):
                    fresh[tuple(x + sign * a for x, a in zip(z, column))] += c * weight
            counts = dict(fresh)
            if time.perf_counter() - started > 120:
                raise TimeoutError('Declared aggregate author cap exceeded; no result published')
        gram = [[sum(a[i] * a[j] for a in columns) for j in range(rank)] for i in range(rank)]
        assert gram == [[b * int(i == j) for j in range(rank)] for i in range(rank)]
        assert sum(counts.values()) == 4 ** b
        assert all(counts.get(tuple(-x for x in z)) == c for z, c in counts.items())
        c0 = counts[zero]
        bound = c0 ** b
        payload, failures = [], []
        for z, c in sorted(counts.items()):
            v = sum(x * x for x in z)
            ok = (c ** b) * (2 ** v) <= bound
            row = [list(z), c, v, ok]
            payload.append(row)
            if not ok:
                failures.append(row)
        cases.append(dict(rank=rank, b=b, columns=[list(a) for a in columns], gram=gram,
                          denominator=4 ** b, center_count=c0, endpoint_count=len(counts),
                          endpoints=payload, failures=failures))
        if time.perf_counter() - started > 120:
            raise TimeoutError('Declared aggregate author cap exceeded; no result published')
    result = dict(domain='r=2,3,4,5; all columns (1,+/-1,...,+/-1); all original endpoints', law=[1, 2, 1], cases=cases, total_endpoints=sum((x['endpoint_count'] for x in cases)), total_failures=sum((len(x['failures']) for x in cases)))
    dest = (_J_OUTPUT / 'result.json')
    if dest.exists():
        raise FileExistsError('Retained first result exists')
    dest.write_text(json.dumps(result, separators=(',', ':'))+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'cases'}))
    print([(c['rank'], c['endpoint_count'], len(c['failures'])) for c in cases])


if __name__ == '__main__':
    main()
