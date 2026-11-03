"""Fixed length-24 discovery for five declared tails; no length scan."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[3] / 'mathematics' / 'computations' / 'outputs' / HERE.name


def beta(a):
    return (-a[3], a[0]+a[3], a[1]+a[3], a[2]+a[3])


def inverse(a):
    return (a[0]+a[1], a[0]+a[2], a[0]+a[3], -a[0])


def power(a, n):
    for _ in range(abs(n)):
        a = (beta if n >= 0 else inverse)(a)
    return a


def decode(code):
    out = []
    for _ in range(12):
        code, d = divmod(code, 3)
        out.append(d-1)
    return out


def main():
    table = {(0,0,0,0): 0}
    p = (1,0,0,0)
    operations = 0
    for j in range(12):
        new = {}
        for q, code in table.items():
            for d in (-1,0,1):
                key = tuple(q[i]+d*p[i] for i in range(4))
                new.setdefault(key, code+(d+1)*3**j)
                operations += 1
        assert len(new) <= 3**(j+1)
        table = new
        p = beta(p)
    cp = (0,3,0,-1)
    cm = (-2,0,-1,1)
    targets = {'right_a': (-3,2,0,0), 'right_cp': cp, 'right_cm': cm,
               'left_cp': tuple(-x for x in power(cp,28)),
               'left_cm': tuple(-x for x in power(cm,28))}
    witnesses = {}
    for name, target in targets.items():
        found = None
        for q, code in table.items():
            residual = power(tuple(target[i]-q[i] for i in range(4)), -12)
            if residual in table:
                found = decode(code)+decode(table[residual])
                break
        witnesses[name] = {'target': target, 'digits': found}
    payload = {'tail_length': 24, 'half_table_size': len(table),
               'candidate_operations': operations, 'witnesses': witnesses}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'discovery.json').write_text(json.dumps(payload,indent=2)+'\n', encoding='utf-8')
    print(json.dumps(payload))


if __name__ == '__main__':
    main()
