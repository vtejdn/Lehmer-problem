"""Compare full-slice coverage with the separate prefix tensor count."""

import argparse
from collections import Counter
from itertools import combinations
import json
from math import prod
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parents[3] / "outputs" / HERE.parents[1].name / "versions" / "v6"


def prefix_total(degree):
    data = json.loads((OUTPUT / "boxes.json").read_text())[str(degree)]["certified_all_available"]
    v2 = runpy.run_path(str(HERE.parent / "v2" / "cyclotomic_prefixes.py"))
    bounds = data["bounds"]
    tests = v2["inequalities"](degree,bounds)
    primes = [p for p,_ in v2["prime_powers"](degree)]
    total = rejected = 0
    for size in range(len(primes)+1):
        for selected in combinations(primes,size):
            divisor = prod(selected)
            restricted = [b if k%divisor==0 else 0 for k,b in enumerate(bounds,1)]
            table, _ = v2["count_selection"](degree,restricted,tests)
            total += (-1)**size * table["total"]
            rejected += (-1)**size * table["trace_box_through_15_all_orders"]
    assert total == 2*data["no_power_substitution_up_to_sign"] and rejected%2==0
    result = {"degree":degree,"original":total//2,"excluded":rejected//2}
    (OUTPUT/f"d{degree}_prefix.json").write_text(json.dumps(result,indent=2)+"\n")
    print(result,flush=True)


def remaining_cyclotomics(degree, divide):
    """Construct every untested cyclotomic polynomial of degree at most degree."""
    # phi(n)^2 >= n/2, and the totient of a divisor never exceeds phi(n).
    totients = list(range(2*degree**2+1))
    for p in range(2,len(totients)):
        if totients[p] == p:
            for n in range(p,len(totients),p):
                totients[n] -= totients[n]//p
    polynomials = {}
    for n in range(1,len(totients)):
        if totients[n] > degree:
            continue
        phi = [-1]+[0]*(n-1)+[1]
        for m,known in polynomials.items():
            if n % m == 0:
                phi, remainder = divide(phi,known)
                assert not any(remainder)
        assert len(phi)-1 == totients[n]
        polynomials[n] = phi
    return {n:p for n,p in polynomials.items() if n>2*degree}


def summarize(degree):
    data = json.loads((OUTPUT / "boxes.json").read_text())[str(degree)]["certified_all_available"]
    slices = [json.loads((OUTPUT/f"d{degree}_s{first}.json").read_text())
              for first in range(data["bounds"][0]+1)]
    totals = json.loads((OUTPUT/f"d{degree}_prefix.json").read_text())
    accepted = sum(row["prefix_survivors"] for row in slices)
    assert accepted == totals["original"]-totals["excluded"]
    labels = Counter()
    for row in slices:
        labels.update(row["classifications"])
    unclassified = [half for row in slices for half in row["unresolved"]]
    unresolved = []
    if unclassified:
        divide = runpy.run_path(str(HERE.parent / "v3" / "finish.py"))["divide"]
        polynomials = remaining_cyclotomics(degree,divide)
        for half in unclassified:
            polynomial = half+half[-2::-1]
            divisor = next((n for n,phi in polynomials.items()
                            if not any(divide(polynomial,phi)[1])),None)
            if divisor is None:
                unresolved.append(half)
            else:
                labels["unresolved"] -= 1
                labels[f"late_cyclotomic_{divisor}"] += 1
        if labels["unresolved"] == 0:
            del labels["unresolved"]
    report = {"degree":degree,"original":totals["original"],"prefix_survivors":accepted,
              "first_reflected_trace":sum(row["higher_traces"][0] for row in slices),
              "through_120":sum(row["higher_traces"][-1] for row in slices),
              "nonzero_at_endpoints":sum(row["nonzero_at_endpoints"] for row in slices),
              "classifications":dict(labels),"unresolved":unresolved}
    assert sum(labels.values())==report["nonzero_at_endpoints"]
    (OUTPUT/f"d{degree}_summary.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("degree",type=int,choices=(60,62))
    parser.add_argument("--prefix-only",action="store_true")
    args=parser.parse_args()
    if args.prefix_only:
        prefix_total(args.degree)
    else:
        summarize(args.degree)
