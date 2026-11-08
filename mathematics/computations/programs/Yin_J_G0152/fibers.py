"""Bound two unrestricted full-grid unit exponents using the 9 and 27 layers."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import sys

from flint import arb, ctx, fmpq

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Yin_J_G0150"))
from moments import sign_columns


P, K_CUT = 6561, 746


def cosine_word(columns):
    """Signed multiplicities of log |T_a| in the canonical h0."""
    word = Counter(columns)
    scales = Counter()
    for a in columns:
        d = 1
        while a % 3 == 0:
            a //= 3
            d *= 3
        scales[d] += 1
    for d, count in scales.items():
        word[d] -= count - count % 2
    return word


def layer(order, word, y):
    cosines = [2*arb.cos_pi_fmpq(fmpq(2*j, order)) for j in range(order)]
    logs = [abs(b).log() for b in cosines]
    rows = {}
    for j in range(1, (order+1)//2):
        if j % 3 == 0:
            continue
        powers = Counter()
        for a, multiplicity in word.items():
            powers[(a*j) % order] += multiplicity
        b = cosines[j]
        weight = (4-b*b)*abs(b-y)
        base = weight.log() + sum(count*logs[r] for r,count in powers.items())
        rows[j] = (base, (2+b).log(), (2+cosines[2*j]).log())
    return rows


def coarse_rectangle(rows, log_budget):
    # The product of each unit over the three order-nine nodes is one.
    # The feasible triangle is the intersection of the three upper half-planes.
    vertices = []
    for (a, b, c), (f, g, h) in combinations(rows.values(), 2):
        C, F = log_budget-a, log_budget-f
        det = b*h-c*g
        assert not det.contains(0)
        vertices.append(((C*h-c*F)/det, (b*F-C*g)/det))
    bounds = []
    for axis in (0,1):
        low = min(int(pt[axis].lower().floor().unique_fmpz()) for pt in vertices)
        high = max(int(pt[axis].upper().ceil().unique_fmpz()) for pt in vertices)
        bounds.append(range(low,high+1))
    return bounds


def masses(rows, d, e):
    return {j:(a+d*b+e*c).exp() for j,(a,b,c) in rows.items()}


def lower_masses(rows, d, e, width):
    # The log of each weight is affine. Its signs select the minimizing corner.
    values = {}
    for j,(a,b,c) in rows.items():
        assert not b.contains(0) and not c.contains(0)
        left = d if b > 0 else d+width
        right = e if c > 0 else e+width
        values[j] = (a+left*b+right*c).exp()
    return values


def fiber_mean(weights, triples):
    sums = [sum(weights[j] for j in group) for group in triples]
    return 3*(sums[0]*sums[1]*sums[2]).root(3)


def balanced_lower_layers(word, y, budget):
    ratios = [(8,1,3),(10,1,-3),(7,2,-1),(11,2,6),(5,4,-1),(13,4,-2)]
    for order in (3,9,27,81):
        cosines = [2*arb.cos_pi_fmpq(fmpq(2*j,order)) for j in range(order)]
        total = arb(0)
        for j,(base,log_one,log_two) in layer(order,word,y).items():
            def trace(a):
                return cosines[(a*j) % order]
            value = base + log_one + 537*log_two
            for a,b,power in ratios:
                value += power*((2+trace(a))/(2+trace(b))).log()
            for k,power in [(5,-62),(7,-61)]:
                value += 2*power*abs(trace(3*k)/trace(3)).log()
            total += value.exp()
        if order < 81:
            # The signs turn the apparent absolute values into the trace of an
            # integral polynomial after multiplication by the denominator of y.
            exact = (45*total).unique_fmpz()
            assert exact is not None
            print('balanced center: order and 45 times the layer mass:',order,exact)
        else:
            log_ratio = (total/budget).log()/arb.const_log2()
            assert log_ratio > 1
            print('balanced center: log2(order-81 mass / budget):',log_ratio)


def run():
    columns = sign_columns(P,K_CUT)
    word = cosine_word(columns)
    y = arb(-68)/45
    budget = P*(4-3*y)
    nine = layer(9,word,y)
    twenty_seven = layer(27,word,y)
    ds, es = coarse_rectangle(nine, budget.log())
    print('columns, rectangle:',len(columns),(ds.start,ds.stop-1),(es.start,es.stop-1))
    triples = [[j for j in twenty_seven if min(j % 9,(-j) % 9)==i] for i in nine]
    assert all(len(group)==3 for group in triples)
    kept = 0
    for d in ds:
        for e in es:
            lower_nine = sum(masses(nine,d,e).values())
            if lower_nine > budget:
                continue
            assert lower_nine < budget
            kept += 1
            weights = masses(twenty_seven,d,e)
            lower_total = lower_nine + fiber_mean(weights,triples)
            assert lower_total > budget, (d,e,lower_total)
            if kept==1 or lower_total < minimum:
                minimum, minimizer = lower_total, (d,e)
            else:
                assert lower_total > minimum
    if kept:
        print('order-nine survivors, minimum lower bound and exponents:',kept,minimum,minimizer)
    print('eligible in full pullback family:',0)
    pieces = 8
    width = arb(1)/pieces
    cells = 0
    minimum_ratio = None
    for u in range(pieces*ds.start,pieces*(ds.stop-1)):
        for v in range(pieces*es.start,pieces*(es.stop-1)):
            d, e = u*width, v*width
            if sum(lower_masses(nine,d,e,width).values()) > budget:
                continue
            bound = fiber_mean(lower_masses(twenty_seven,d,e,width),triples)/budget
            cells += 1
            ratio = int(bound.lower().floor().unique_fmpz())
            minimum_ratio = ratio if minimum_ratio is None else min(minimum_ratio,ratio)
    assert minimum_ratio is not None and minimum_ratio > 1
    print('real-exponent cells retained, lower bound for fiber distortion:',cells,minimum_ratio)
    balanced_lower_layers(word,y,budget)


if __name__ == '__main__':
    with ctx.workprec(160):
        run()
