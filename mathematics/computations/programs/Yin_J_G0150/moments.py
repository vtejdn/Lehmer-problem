"""Exact two-moment search for positive-unit adjustments on a full ternary grid."""
import argparse
from math import comb, gcd, prod
from pathlib import Path
import sys

import numpy as np
import sympy as sp

PROGRAMS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROGRAMS / "Yin_J_G0148"))
from cuts import target_cut


def normalize(word):
    offset = word[len(word) // 2]
    return tuple(v - offset for v in word)


def cyclic_multiply(left, right):
    p = len(left)
    # Each normalized word is symmetric and vanishes at the last pair.
    return normalize([sum(left[i] * right[(j-i) % p] for i in range(p))
                      for j in range(p)])


def sign_columns(p, k):
    n = p // 2
    rows = []
    for j in range(1, n + 1):
        bits = sum((p < 4 * (j*a % p) < 3*p) << (a-1) for a in range(1, n+1))
        rows.append(bits | ((j > n-k) << n))
    for a in range(n):
        pivot = next(i for i in range(a, n) if (rows[i] >> a) & 1)
        rows[a], rows[pivot] = rows[pivot], rows[a]
        for i in range(n):
            if i != a and (rows[i] >> a) & 1:
                rows[i] ^= rows[a]
    selected = [a + 1 for a, row in enumerate(rows) if (row >> n) & 1]
    for j in range(1, n + 1):
        negatives = sum(p < 4 * (j * a % p) < 3 * p for a in selected)
        assert negatives % 2 == (j > n - k)
    return selected


def setup(p, k=None, flips=0):
    n = p // 2
    k = target_cut(p) if k is None else k
    assert 0 < k < n
    t = sp.Symbol("t")
    one, var = sp.Poly(1, t), sp.Poly(t, t)
    trace = [2 * one, var]
    for _ in range(2, p):
        trace.append(var * trace[-1] - trace[-2])
    B = one + sum(trace[1:n+1], 0*one)

    def as_word(h):
        w = [0] * p
        for a in h.all_coeffs():
            w = [w[(i-1) % p] + w[(i+1) % p] for i in range(p)]
            w[0] += int(a)
        return normalize(w)

    h = one
    parity = {}
    flip_units = []
    for a in sign_columns(p, k):
        scale = 1
        while a % 3 == 0:
            scale *= 3
            a //= 3
        u = a if a % 2 else p // scale - a
        parity[scale] = 1 - parity.get(scale, 0)
        quotient = trace[u].exquo(var).compose(trace[scale]).rem(B)
        h = (h * quotient).rem(B)
        if quotient.degree() > 0:
            flip_units.append(((quotient**2).rem(B), f"(T{scale*u}/T{scale})^2"))
    for scale, use in parity.items():
        if use:
            h = (h * trace[scale]).rem(B)
    delta = abs(int(B.resultant(h)))
    assert delta == 2**sum((s-1)//2 for s, use in parity.items() if use)
    # Select eight cosine squares at the top, and two cosine-quotient
    # squares at the next scale. At larger p this is an explicit slice.
    js = [j for j in range(1, n+1) if gcd(j, p) == 1][:8]
    units = [(2*one + trace[j], f"2+T{j}") for j in js]
    for u in (5, 7):
        quotient = trace[u].exquo(var).compose(trace[3]).rem(B)
        units.append(((quotient**2).rem(B), f"(T{3*u}/T3)^2"))
    if flips:
        units = flip_units + units[:flips]
    dual = []
    for unit, label in units:
        unit = unit.rem(B)
        inv = unit.invert(B)
        assert all(c.q == 1 for c in inv.all_coeffs())
        assert (unit * inv).rem(B).as_expr() == 1
        dual.append((as_word(unit), as_word(inv), label))
    return B, trace, as_word(h), dual, delta, k, len(flip_units) if flips else 0


def half_words(initial, units, choices):
    words = [(initial, ())]
    for (unit, inv, _), exponents in zip(units, choices, strict=True):
        powers = {0: (1,) + (0,) * (len(initial)-1)}
        for step, multiplier in ((1, unit), (-1, inv)):
            for i in range(1, max(map(abs, exponents))+1):
                powers[step*i] = cyclic_multiply(powers[step*(i-1)], multiplier)
        words = [(cyclic_multiply(w, powers[e]), exps+(e,)) for w, exps in words
                 for e in exponents]
    return words


def functional(w, a, b):
    # Dot with a symmetric right word to extract [a]-[b] of the cyclic product.
    p = len(w)
    n = p // 2
    return (w[a] - w[b],) + tuple(
        w[(a-j) % p]+w[(a+j) % p]-w[(b-j) % p]-w[(b+j) % p] for j in range(1,n)
    )


def measure(B, trace, word, x, delta):
    n = B.degree()
    h = sp.Poly(word[0], B.gens[0]) + sum((word[i]*trace[i] for i in range(1,n)),0*B)
    D = B - trace[n]
    C = (D*h).rem(B)
    assert C.nth(n-1) == x*x+2 and C.nth(n-2)-C.nth(n-1)*B.nth(n-1) == -4*x
    Q = (trace[1]-2*x)*B + C
    assert abs(Q.resultant(B)) == delta
    d = n + 1
    # Integer coefficients of z^d Q(z+1/z).
    lift = [sum(int(Q.nth(a))*comb(a, (a+d-i)//2) for a in range(abs(d-i),d+1)
                if (a+d-i) % 2 == 0) for i in range(2*d+1)]
    assert lift == lift[::-1] and lift[0] == 1
    endpoint = sum(v * (-1)**i for i,v in enumerate(lift))
    assert endpoint == (-1)**d * Q.eval(-2)
    # Same-sign gaps account for at least n-2 distinct real trace roots.
    # Isolate all real ones, then recover any outstanding nonreal pair
    # from the first two power sums of Q, keeping outward-rounded bounds.
    from mpmath import iv

    iv.dps = 45

    def exact(v):
        return iv.mpf(int(v.p)) / int(v.q)

    def outside(absolute):
        if absolute.b <= 2:
            return iv.mpf(1)
        assert absolute.a > 2
        return (absolute + iv.sqrt(absolute**2-4))/2

    total = iv.mpf(1)
    pair_sum = iv.mpf(-int(Q.nth(d-1)))
    pair_squares = pair_sum**2 - 2*int(Q.nth(d-2))
    missing = d
    for (a,b), mult in Q.intervals(eps=sp.Rational(1,10**20)):
        root = iv.mpf([exact(a).a,exact(b).b])
        total *= outside(abs(root))**mult
        pair_sum -= mult*root
        pair_squares -= mult*root**2
        missing -= mult
    assert missing in (0,2)
    if missing == 2:
        pair_norm = (pair_sum**2-pair_squares)/2
        s = (iv.sqrt(pair_norm+2*pair_sum+4) + iv.sqrt(pair_norm-2*pair_sum+4))/2
        total *= outside(s)**2
    scale = 10**6
    low, high = int((total*scale).a), int((total*scale).b)+1
    assert low <= total*scale and total*scale < high
    return endpoint, (low, high, scale)


def search(p, radius, center, k=None, flips=0):
    B, trace, base, units, delta, k, fixed = setup(p, k, flips)
    center = center or [0] * len(units)
    assert len(center) == len(units)
    choices = [
        (-1, 0) if j < fixed else range(c - radius, c + radius + 1)
        for j, c in enumerate(center)
    ]
    def longer_half(j):
        return max(prod(map(len, choices[:j])), prod(map(len, choices[j:])))

    split = min(range(1, len(units)), key=longer_half)
    left = half_words(base, units[:split], choices[:split])
    identity = (1,) + (0,) * (p-1)
    right = half_words(identity, units[split:], choices[split:])
    n = p//2
    modulus = 65521
    assert n*modulus**2 < 2**63
    right_mod = np.array([[i % modulus for i in w[:n]] for w,_ in right],dtype=np.int64).T
    K_counts = {2: 0, 3: 0, 6: 0}
    hits = []
    measures = {}
    for start in range(0,len(left),128):
        part = left[start:start+128]
        func = [functional(w,0,2) for w,_ in part]
        reduced = np.array([[i % modulus for i in row] for row in func],dtype=np.int64)
        residues = (reduced @ right_mod) % modulus
        for K in K_counts:
            rows, cols = np.nonzero(residues == K)
            for i,j in zip(rows.tolist(),cols.tolist()):
                word, right_exps = right[j]
                if sum(a*b for a,b in zip(func[i],word)) != K:
                    continue
                K_counts[K] += 1
                w, left_exps = part[i]
                L = sum(a*b for a,b in zip(functional(w,1,3),word))
                for x in range(-2,3):
                    if x*x+2 == K and L == -4*x:
                        h = cyclic_multiply(w,word)
                        assert (h[0]-h[2],h[1]-h[3]) == (K,L)
                        key = (x,h)
                        if key not in measures:
                            measures[key] = measure(B,trace,h,x,delta)
                        hits.append((x,left_exps+right_exps,*measures[key]))
    print("p, k, Delta, selected sign columns, positive units:",p,k,delta,
          sign_columns(p,k),[label for _,_,label in units])
    print("radius, center, words, K counts, joint count:",radius,center,len(left)*len(right),
          K_counts,len(hits))
    print("distinct lifted polynomials:",len(measures))
    for group in (hits, [v for v in hits if v[2]>0]):
        if group:
            smallest = min(group,key=lambda v:v[3][1])
            largest = max(group,key=lambda v:v[3][0])
            print("group count, minimum, maximum:",len(group),smallest,largest)
    for hit in hits:
        print("x, exponents, P(-1), whole measure interval:",*hit)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("p",type=int)
    parser.add_argument("radius",type=int)
    parser.add_argument("--center",nargs="+",type=int)
    parser.add_argument("--cut",type=int)
    parser.add_argument("--flips",type=int,default=0,help="flip selected nonconstant quotients, then add this many standard units")
    args = parser.parse_args()
    power = args.p
    while power > 1 and power % 3 == 0:
        power //= 3
    if power != 1 or args.p < 27 or args.radius < 0 or not 0 <= args.flips <= 10:
        parser.error("require conductor 3^m >= 27, nonnegative radius and 0..10 extra units")
    search(args.p,args.radius,args.center,args.cut,args.flips)
