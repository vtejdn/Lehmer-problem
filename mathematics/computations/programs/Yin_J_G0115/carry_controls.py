from collections import Counter
from fractions import Fraction as F
from math import log2
import json
import platform

def times_x(v, p):
    # p lists coefficients below the leading monic term.
    top = v[-1]
    return tuple((v[i-1] if i else 0) - top*p[i]
                 for i in range(len(p)))

def plus_digit(v, digit):
    return (v[0] + digit,) + v[1:]

def distributions(p, stop):
    vals = Counter({(0,)*len(p): 1})
    out = []
    for n in range(stop+1):
        assert sum(vals.values()) == 2**n
        energy = sum(c*c for c in vals.values())
        out.append((len(vals), F(energy, 4**n)))
        if n < stop:
            nxt = Counter()
            for v, c in vals.items():
                xv = times_x(v, p)
                nxt[xv] += c
                nxt[plus_digit(xv, 1)] += c
            vals = nxt
    return out

def divide_x(v, p):
    assert p[0] in (-1, 1)
    top = -v[0] // p[0]
    return tuple(v[i+1] + p[i+1]*top
                 for i in range(len(p)-1)) + (top,)

def golden_certificate():
    p = (-1, -1)
    states = [(0, 0), (-1, 1), (1, -1), (1, 0), (-1, 0)]
    weights = [F(1), F(1,4), F(1,4), F(3,5), F(3,5)]
    idx = {v: j for j, v in enumerate(states)}
    matrix = [[0]*5 for _ in states]
    for i, v in enumerate(states):
        for digit, multiplicity in [(-1,1), (0,2), (1,1)]:
            dest = divide_x(plus_digit(v, digit), p)
            if dest in idx:
                matrix[i][idx[dest]] += multiplicity
    for i in range(5):
        assert sum(F(matrix[i][j],4)*weights[j]
                   for j in range(5)) <= F(5,8)*weights[i]
    row = [1,0,0,0,0]
    returns = []
    for n in range(21):
        returns.append(F(row[0],4**n))
        row = [sum(row[i]*matrix[i][j] for i in range(5))
               for j in range(5)]
    return matrix, returns

base = distributions((-1,-1), 20)
matrix, returns = golden_certificate()
assert [row[1] for row in base] == returns

def row_summary(row, n):
    size, qcoll = row
    return {"n": n, "support": size,
            "collision_probability": str(qcoll),
            "finite_H2_per_digit": -log2(float(qcoll))/n}

radicals = {}
for r in (1,2,4,8):
    p = [-1] + [0]*(2*r-1)
    p[r] = -1
    rows = distributions(tuple(p), 16)
    for n, (size, qcoll) in enumerate(rows):
        q, s = divmod(n, r)
        assert size == base[q+1][0]**s * base[q][0]**(r-s)
        assert qcoll == base[q+1][1]**s * base[q][1]**(r-s)
    radicals[str(r)] = row_summary(rows[-1], 16)

controls = {}
for name, p in [
    ("lambda=1", (-1,)),
    ("primitive_cube_root", (1,1)),
    ("root_t8_minus_2", (-2,0,0,0,0,0,0,0)),
]:
    rows = distributions(p, 16)
    controls[name] = row_summary(rows[-1], 16)

print(json.dumps({
    "python": platform.python_version(),
    "golden_integer_transition_matrix": matrix,
    "golden_exact_return_checks": "n=0..20 passed",
    "radical_exact_factorization_checks": "r=1,2,4,8; n=0..16 passed",
    "golden_all_length_certificate_theta": "5/8",
    "radicals": radicals,
    "controls": controls,
}, indent=2))
