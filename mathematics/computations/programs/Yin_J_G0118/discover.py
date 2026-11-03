"""One fixed length-24 meet-in-the-middle witness discovery; exact integers."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[3] / 'mathematics' / 'computations' / 'outputs' / HERE.name
ZERO = (0, 0, 0, 0)
C = (-3, 3, 1, -1)


def beta(a):
    a0, a1, a2, a3 = a
    return (-a3, a0 + a3, a1 + a3, a2 + a3)


def beta_inv(a):
    a0, a1, a2, a3 = a
    return (a0 + a1, a0 + a2, a0 + a3, -a0)


def power(a, n):
    step = beta if n >= 0 else beta_inv
    for _ in range(abs(n)):
        a = step(a)
    return a


def digits(code, n):
    result = []
    for _ in range(n):
        code, r = divmod(code, 3)
        result.append(r - 1)
    return result


def main():
    table = {ZERO: 0}
    p = (1, 0, 0, 0)
    total_candidates = 0
    for j in range(12):
        new = {}
        for q, code in table.items():
            for d in (-1, 0, 1):
                key = tuple(q[i] + d * p[i] for i in range(4))
                new.setdefault(key, code + (d + 1) * 3**j)
                total_candidates += 1
        assert len(new) <= 3**(j + 1)
        table = new
        p = beta(p)
    targets = {'right': C, 'left': tuple(-x for x in power(C, 28))}
    answer = {}
    for name, target in targets.items():
        found = None
        for q, code in table.items():
            residual = power(tuple(target[i] - q[i] for i in range(4)), -12)
            if residual in table:
                found = digits(code, 12) + digits(table[residual], 12)
                break
        answer[name] = {'target': target, 'digits': found}
    payload = {'tail_length': 24, 'c': C, 'half_table_size': len(table),
               'candidate_operations': total_candidates, 'witnesses': answer}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'discovery.json').write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(payload))


if __name__ == '__main__':
    main()
