"""Four fixed cyclotomic canonical probes; exact modular monic arithmetic."""
from pathlib import Path
import json

CASES = [(2, 2, 3, 2, 16, 0), (2, 8, 12, 4, 16, 1),
         (4, 8, 12, 4, 16, 1), (2, 4, 6, 2, 8, 1)]


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, scale=1, modulus=None):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += scale * v
    if modulus:
        c = [v % modulus for v in c]
    return trim(c)


def mul(a, b, modulus=None):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    if modulus:
        c = [v % modulus for v in c]
    return trim(c)


def rem(a, t, modulus):
    assert t[-1] == 1
    a = [v % modulus for v in a]
    d = len(t) - 1
    for k in range(len(a) - 1, d - 1, -1):
        q = a[k]
        if q:
            for j in range(d + 1):
                a[k - d + j] = (a[k - d + j] - q * t[j]) % modulus
    return trim(a[:d] or [0])


def power(a, k, t=None, modulus=None):
    r = [1]
    for _ in range(k):
        r = mul(r, a, modulus)
        if t is not None:
            r = rem(r, t, modulus)
    return r


def compose(a, b, t=None, modulus=None):
    r = [0]
    for v in reversed(a):
        r = add(mul(r, b, modulus), [v], modulus=modulus)
        if t is not None:
            r = rem(r, t, modulus)
    return r


def chebyshev(n):
    if n == 0:
        return [2]
    a, b = [2], [0, 1]
    for _ in range(2, n + 1):
        a, b = b, add([0] + b, a, -1)
    return b


def build(params):
    a, b, d, k, w, e = params
    # Complete integer trace factors; independently reconstructed in verify.py.
    f3, f5 = [1, 1], [-1, 1, 1]
    f15, f30 = [1, 4, -4, -1, 1], [1, -4, -4, 1, 1]
    t = [0] * a + [1]
    for factor, exponent in ((f3, b), (f5, d), (f15, k),
                             (compose(f30, chebyshev(w)), 1),
                             (compose(f30, chebyshev(w // 2)), e)):
        t = mul(t, power(factor, exponent))
    return t


def canonical_mod4(t, p):
    r = compose(t, chebyshev(p), t, 4 * p)
    assert all(v % p == 0 for v in r)
    return trim([v // p for v in r])


def run_case(params):
    t = build(params)
    a, b, c = [canonical_mod4(t, p) for p in (2, 3, 5)]
    a3, a5 = power(a, 3, t, 4), power(a, 5, t, 4)
    b2, b5 = power(b, 2, t, 4), power(b, 5, t, 4)
    c2, c3 = power(c, 2, t, 4), power(c, 3, t, 4)
    f = rem(add([2 * v for v in c2], a5, -3), t, 4)
    g = rem(add(c3, b5, -2), t, 4)
    x_plus = rem(add(add(b2, a3, -1), g), t, 4)
    x_minus = rem(add(add(b2, a3, -1), g, -1), t, 4)
    residues = dict(a=a, b=b, c=c, F=f, G=g,
                    X_plus=x_plus, X_minus=x_minus)
    valuations = {name: (0 if any(v % 2 for v in poly)
                          else 1 if any(poly) else 'at_least_2')
                  for name, poly in residues.items()}
    return dict(parameters=list(params), degree=len(t) - 1,
                T_coefficients=t, residues_mod4=residues,
                coefficient_valuations_through_mod4=valuations)


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[3]
    output = root / 'mathematics' / 'computations' / 'outputs' / here.name
    output.mkdir(parents=True, exist_ok=True)
    rows = [run_case(params) for params in CASES]
    payload = dict(arithmetic='exact integer monic reduction modulo4p, then division by p',
                   parameter_order=['A', 'B', 'D', 'K', 'w', 'e'], cases=rows)
    temporary = output / 'result.json.partial'
    temporary.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    temporary.replace(output / 'result.json')
    print(json.dumps([dict(parameters=row['parameters'], degree=row['degree'],
                           valuations=row['coefficient_valuations_through_mod4'])
                      for row in rows]))


if __name__ == '__main__':
    main()
