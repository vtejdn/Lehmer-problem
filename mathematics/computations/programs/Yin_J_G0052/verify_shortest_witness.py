"""Distinct exact AUTHOR check of the depth-two shortest-distance witness.

No author BFS helper is imported.  Direct unrestricted word enumeration
through length four and generic polynomial reduction verify all claimed
distances/masses; coarse rational Horner intervals check every used state.
This is not an independent-agent review or a whole depth-24 reproduction.
"""

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / "outputs" / HERE.name
ZERO = (0, 0, 0, 0)
POLY = (1, -1, -1, -1, 1)
LOWER, UPPER = F(43, 25), F(173, 100)
X = (-1, -1, 1, 0)
MINUS = (-1, -1, -1, 1)
MIDDLE = (0, -1, -1, 1)
PLUS = (1, -1, -1, 1)


def reduce_polynomial(coefficients):
    p = list(coefficients)
    while len(p) < 4:
        p.append(0)
    for degree in range(len(p)-1, 3, -1):
        leading = p[degree]
        for j, coefficient in enumerate(POLY):
            p[degree-4+j] -= leading * coefficient
    return tuple(p[:4])


def times(a, b):
    result = [0] * (len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            result[i+j] += c*d
    return reduce_polynomial(result)


def step(x, digit):
    p = [digit] + list(x)
    return reduce_polynomial(p)


def interval(coefficients):
    lo = hi = F(0)
    for coefficient in reversed(coefficients):
        corners = (lo*LOWER, lo*UPPER, hi*LOWER, hi*UPPER)
        lo, hi = min(corners)+coefficient, max(corners)+coefficient
    return lo, hi


def reciprocal(x):
    inverse = (1, 1, 1, -1)
    out = [0]*4
    power = (1, 0, 0, 0)
    for coefficient in x:
        for i in range(4):
            out[i] += coefficient*power[i]
        power = times(power, inverse)
    return tuple(out)


def certificate(x):
    stable = reciprocal(x)
    polys = [tuple(c+s*a for c, a in zip(cap, coordinate))
             for cap, coordinate in (((-2,-1,0,1),x), ((-1,-1,0,1),stable))
             for s in (-1, 1)]
    bounds = [interval(p) for p in polys]
    assert all(lo > 0 or hi < 0 or p == ZERO for p, (lo, hi) in zip(polys, bounds))
    return {"state": x, "strict_core": all(lo > 0 for lo, _ in bounds),
            "margin_intervals": [[str(lo),str(hi)] for lo,hi in bounds]}


def direct_words(x, maximum):
    results = []
    for length in range(1, maximum+1):
        accepted = []
        mass = F(0)
        for word in product((-1,0,1), repeat=length):
            current, states, numerator = x, [x], 1
            for digit in word:
                current = step(current, digit)
                states.append(current)
                numerator *= 2 if digit == 0 else 1
            if current == ZERO:
                accepted.append(list(word))
                mass += F(numerator, 4**length)
                assert all(certificate(y)["strict_core"] for y in states)
        results.append({"length": length, "return_words": accepted,
                        "mass": [mass.numerator, mass.denominator]})
        if accepted:
            return results
    raise AssertionError("No asserted shortest word found")


def main():
    assert interval(POLY)[0] < 0 < interval(POLY)[1]
    def value(t):
        return sum(c*t**i for i,c in enumerate(POLY))
    assert value(LOWER)<0<value(UPPER)
    assert 4*LOWER**3-3*UPPER**2-2*UPPER-1>0
    assert [step(X,e) for e in (-1,0,1)] == [MINUS,MIDDLE,PLUS]
    certs = [certificate(x) for x in (X,MINUS,MIDDLE,PLUS)]
    assert [c["strict_core"] for c in certs] == [True,True,True,False]
    tests = {"x":direct_words(X,2), "minus":direct_words(MINUS,1), "middle":direct_words(MIDDLE,4)}
    assert tests["x"][-1] == {"length":2,"return_words":[[-1,1]],"mass":[1,16]}
    assert tests["minus"][-1] == {"length":1,"return_words":[[1]],"mass":[1,4]}
    assert tests["middle"][-1] == {"length":4,"return_words":[[0,-1,-1,1]],"mass":[1,128]}
    # The symbolic minimum proof uses 2z+z^-2-3=(z-1)^2(2z+1)/z^2.
    factored = [0]*4
    for i,c in enumerate((1,-2,1)):
        for j,d in enumerate((1,2)):
            factored[i+j] += c*d
    assert factored == [1,0,-3,2]
    assert 51**3 > 2*40**3  # 3/(4*cuberoot(2)) > 10/17.
    assert F(68883,40000)>F(17,10)
    supplied = json.loads((OUT/"shortest_first_hit_24.json").read_text(encoding="utf-8"))
    assert supplied["status"]=="complete" and supplied["completed_depth"]==24
    for state, expected_d, expected_num in ((X,2,1),(MINUS,1,1),(MIDDLE,4,2)):
        actual=next(r for r in supplied["states"] if tuple(r["state"])==state)
        assert (actual["distance"],actual["shortest_mass_numerator"])==(expected_d,expected_num)
    report={"status":"passed", "scope":"distinct exact author witness check only",
            "state":X, "root_interval":[str(LOWER),str(UPPER)],
            "strict_core_certificates":certs, "direct_word_checks":tests,
            "row_coefficients":[[-2,2],[1,1]],"row_denominator":4,
            "minimum":"3/(4*cuberoot(2))", "strict_rational_lower_bound":"10/17",
            "conclusion":"unmodified W_lambda fails at this state for every lambda>0 and t>=17/10",
            "limit":"does not exclude finite-exception repair or classify the critical mean"}
    (OUT/"shortest_first_hit_witness_check.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report),flush=True)


if __name__=="__main__":
    main()
