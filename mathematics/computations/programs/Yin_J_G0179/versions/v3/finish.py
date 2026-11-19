"""Complete the screen with integer cyclotomic divisibility and exact Graeffe bounds."""

import argparse
import json
from collections import Counter
from math import comb
from pathlib import Path


GROUP = Path(__file__).resolve().parents[2]
OUTPUT = GROUP.parents[1] / "outputs" / GROUP.name / "versions" / "v3"


def bit_polynomial(a):
    return sum((c % 2) << j for j,c in enumerate(a))


def bit_remainder(a,b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


def divide(f, g):
    work = f[:]
    quotient = [0] * (len(f)-len(g)+1)
    for j in reversed(range(len(quotient))):
        lead = work[j+len(g)-1]
        quotient[j] = lead
        if lead:
            for i,c in enumerate(g):
                work[j+i] -= lead*c
    return quotient, work[:len(g)-1]


def cyclotomics(degree):
    # Only orders <= 2*d are used; an untested order passes to Graeffe.
    polynomials = {}
    tests = []
    for order in range(1,2*degree+1):
        poly = [-1] + [0]*(order-1) + [1]
        for divisor,known in polynomials.items():
            if order % divisor == 0:
                poly, remainder = divide(poly,known)
                assert not any(remainder)
        polynomials[order] = poly
        if len(poly)-1 <= degree:
            tests.append((order,poly,bit_polynomial(poly)))
    return tests


def graeffe(f):
    # Even degree, monic; the even-power coefficients of f(X) f(-X).
    out = [0]*len(f)
    degree = len(f)-1
    for i in range(degree+1):
        out[i] = (-1 if i%2 else 1)*f[i]**2
        for j in range(max(0,2*i-degree),i):
            out[i] += (-2 if j%2 else 2)*f[j]*f[2*i-j]
    return out


def classify(first_half, degree, tests, binomials):
    f = first_half+first_half[-2::-1]
    bits = bit_polynomial(f)
    for order,poly,mod2 in tests:
        if bit_remainder(bits,mod2) == 0 and not any(divide(f,poly)[1]):
            return f"cyclotomic_{order}"
    numerator, denominator = 1089, 1000
    for k in range(13):
        if any(abs(c)*denominator > b*numerator for c,b in zip(f,binomials)):
            return f"graeffe_{k}"
        if k < 12:
            f=graeffe(f)
            numerator,denominator=numerator**2,denominator**2
    return "unresolved"


def finish(paths):
    summary = {}
    for path in paths:
        data = json.loads(path.read_text())
        degree = data["degree"]
        tests = cyclotomics(degree)
        binomials = [comb(degree,j) for j in range(degree+1)]
        counts = Counter()
        unresolved = []
        for coeff in data["first_halves"]:
            label = classify(coeff,degree,tests,binomials)
            counts[label] += 1
            if label == "unresolved":
                unresolved.append(coeff)
        assert sum(counts.values())==data["nonzero_at_endpoints"]
        summary[path.stem] = {"degree":degree, "s1":data["s1"], "s2":data["s2"],
                              "version_two_orbits":data["version_two_orbits"],
                              "first_reflected_trace":data["higher_traces"][0],
                              "through_120":data["higher_traces"][-1],
                              "nonzero_at_endpoints":data["nonzero_at_endpoints"],
                              "classifications":dict(counts),"unresolved":unresolved}
        print(path.stem, data["version_two_orbits"], data["higher_traces"][-1],
              sum(n for name,n in counts.items() if name.startswith("graeffe")), len(unresolved),flush=True)
    return summary


def certify_remaining(rows):
    """Test the exact X^59+1 identity on every vector surviving the Graeffe tests."""
    for row in rows.values():
        remaining = []
        for half in row["unresolved"]:
            polynomial = half + half[-2::-1]
            product = [polynomial[0]]
            product.extend(a+b for a,b in zip(polynomial,polynomial[1:]))
            product.append(polynomial[-1])
            if product == [1] + [0]*58 + [1]:
                counts = row["classifications"]
                counts["final_phi118"] = counts.get("final_phi118",0) + 1
                counts["unresolved"] -= 1
                if counts["unresolved"] == 0:
                    del counts["unresolved"]
            else:
                remaining.append(half)
        row["unresolved"] = remaining
    return rows


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files",nargs="*",type=Path)
    args=parser.parse_args()
    if args.files:
        certify_remaining(finish(args.files))
    else:
        rows=certify_remaining(finish(
            [OUTPUT/f"d{degree}_s{first}_99.json" for degree in (56,58) for first in range(7)]))
        version_two=json.loads((OUTPUT.parent/"v2"/"results.json").read_text())
        for degree in (56,58):
            previous=version_two[str(degree)]["no_power_substitution_up_to_sign"]
            assert sum(row["version_two_orbits"] for row in rows.values() if row["degree"]==degree)==(
                previous["total"]-previous["trace_box_through_15_all_orders"])
        (OUTPUT/"summary.json").write_text(json.dumps(rows,indent=2)+"\n",encoding="ascii")
