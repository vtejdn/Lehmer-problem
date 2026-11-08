"""Two fixed, balanced positive-unit boxes at conductor 243."""
from collections import Counter
from math import gcd

import numpy as np
import sympy as sp

from moments import functional, measure, normalize, sign_columns

P = 243
N = 121
ONE = (1,) + (0,) * (P - 1)
# Positive indices are squares of the selected signed cosine quotients.
# Negative indices denote T_{|a|}^2, with order-coprime |a|.
CENTERS = (
    {
        -1: (2, 7, 8, 28, 29, 30, 44, 47, 49, 52, 57, 58, 60, 64, 65, 71, 79,
             80, 87, 92, 93, 94, 97, 99, 101, 102, 105, 107, 113, 114, 116,
             -13, -19, -22, -70, -73, -76, -77, -82, -85, -89, -121),
    },
    {
        -1: (4, 7, 8, 13, 22, 26, 29, 30, 34, 44, 50, 52, 58, 67, 70, 71,
             72, 74, 79, 85, 86, 94, 97, 99, 101, 102, 107, 114, 116, 121,
             -2, -28, -35, -64, -65, -110),
        -2: (-1,),
        1: (65, -83),
    },
)
AXES = (
    (-8, -77, -13, -82, -103, -76, -71, -106, -44, -109, -73, -23, -79, -46, 89, 44),
    (-7, -1, -17, -38, -89, -91, -107, -97, -46, -70, -55, -83, -82, -64, -62, -113),
)
VALS = ((2, 2, 2, 1, 0), (8, 0, 2, 1, 0))


def multiply(a, b):
    # Adding any constant vector vanishes in this normalized cyclic quotient.
    # Nonnegative digit packing then implements cyclic convolution with no carries.
    ma, mb = min(a), min(b)
    bound = P * (max(a) - ma) * (max(b) - mb)
    width = max(1, (bound.bit_length() + 7) // 8)
    def pack(word, minimum):
        return int.from_bytes(b''.join((x-minimum).to_bytes(width, 'little') for x in word), 'little')
    radix_power = 1 << (8 * width * P)
    residue = (pack(a, ma) * pack(b, mb)) % (radix_power - 1)
    data = residue.to_bytes(width * P, 'little')
    return normalize([int.from_bytes(data[i:i+width], 'little') for i in range(0, len(data), width)])


def trace_word(a):
    w = [0] * P
    w[a % P] += 1
    w[-a % P] += 1
    return normalize(w)


def twice_inverse(a):
    w = [0] * P
    for j in range(P // gcd(P, a)):
        w[(2*j+1)*a % P] += (-1)**j
    result = normalize(w)
    assert multiply(result, trace_word(a)) == tuple(2*c for c in ONE)
    return result


def integral_division(w, divisor):
    assert all(c % divisor == 0 for c in w)
    return tuple(c // divisor for c in w)


def power(w, e):
    result = ONE
    for _ in range(e):
        result = multiply(result, w)
    return result


def generators():
    factors = {}
    units = {}
    parity = Counter()
    for a in sign_columns(P, 44):
        s = 1
        while a % (3*s) == 0:
            s *= 3
        parity[s] += 1
        # Compute T_a / T_s and its inverse, including the constant quotient one.
        direct = integral_division(multiply(trace_word(a), twice_inverse(s)), 2)
        inv = integral_division(multiply(trace_word(s), twice_inverse(a)), 2)
        assert multiply(direct, inv) == ONE
        factors[a] = direct
        units[a] = (power(direct, 2), power(inv, 2))
    for a in range(1,N+1):
        if a % 3:
            t = trace_word(a)
            inv = integral_division(twice_inverse(a), 2)
            units[-a] = (power(t, 2), power(inv, 2))
    baseline = ONE
    for q in factors.values():
        baseline = multiply(baseline, q)
    for s, number in parity.items():
        if number % 2:
            baseline = multiply(baseline, trace_word(s))
    corrected = integral_division(multiply(multiply(baseline, power(trace_word(3),8)),
                                           power(twice_inverse(9),2)), 4)
    assert multiply(corrected, power(trace_word(9),2)) == multiply(baseline,power(trace_word(3),8))
    return (baseline, corrected), units


def polynomial_data():
    t = sp.Symbol("t")
    v, one = sp.Poly(t,t), sp.Poly(1,t)
    traces = [2*one, v]
    for _ in range(2,N+1):
        traces.append(v*traces[-1]-traces[-2])
    return one+sum(traces[1:],0*one), traces


def layer_norms(center, traces):
    # Compute h mod each separate monic real cyclotomic trace factor.
    t = traces[1].gens[0]
    h = sp.Poly(center[0],t) + sum((center[i]*traces[i] for i in range(1,N)),sp.Poly(0,t))
    norms = []
    for degree in (1,3,9,27,81):
        F = 1 + traces[degree]
        norms.append(abs(int(F.resultant(h.rem(F)))))
    return norms


def halves(initial, axes, units):
    words = [(initial, ())]
    for a in axes:
        direct, inverse = units[a]
        words = [(w if e==0 else multiply(w, m), exps+(e,))
                 for w,exps in words for e,m in ((-1,inverse),(0,ONE),(1,direct))]
    return words


def run(orbit, baseline, units, B, traces):
    center = baseline
    for e, labels in CENTERS[orbit].items():
        for a in labels:
            center = multiply(center, power(units[a][e<0], abs(e)))
    norms = layer_norms(center, traces)
    assert norms == [2**(t*d) for t,d in zip(VALS[orbit], (1,3,9,27,81), strict=True)]
    center_k, center_l = center[0]-center[2], center[1]-center[3]
    print("orbit, center K,L, 40L+33K, norms:",orbit,center_k,center_l,40*center_l+33*center_k,norms,flush=True)
    left = halves(center, AXES[orbit][:8], units)
    right = halves(ONE, AXES[orbit][8:], units)
    modulus = 100_000_007
    assert N*modulus**2 < 2**63
    right_mod = np.array([[a%modulus for a in w[:N]] for w,_ in right],dtype=np.int64).T
    first = 0
    best_abs_l = None
    best_count = 0
    min_t = 40*center_l + 33*center_k
    min_t_count = 0
    hits = []
    for start in range(0,len(left),64):
        block = left[start:start+64]
        rows = [functional(w,0,2) for w,_ in block]
        l_rows = [functional(w,1,3) for w,_ in block]
        t_rows = [tuple(33*k+40*l for k,l in zip(kr,lr,strict=True))
                  for kr,lr in zip(rows,l_rows,strict=True)]
        # The exact 40L+33K is positive by the prescribed cut. Its
        # residue is a lower bound even when the dot product is huge.
        t_mod = np.array([[a%modulus for a in v] for v in t_rows],dtype=np.int64)
        for i,j in zip(*np.nonzero((t_mod@right_mod)%modulus <= min_t)):
            w = right[j][0]
            value = sum(a*b for a,b in zip(t_rows[i],w))
            assert value > 0
            if value < min_t:
                min_t, min_t_count = value, 0
            if value == min_t:
                min_t_count += 1
        rows_mod = np.array([[a%modulus for a in v] for v in rows],dtype=np.int64)
        for i,j in zip(*np.nonzero((rows_mod@right_mod)%modulus==2)):
            w, right_e = right[j]
            if sum(a*b for a,b in zip(rows[i],w)) != 2:
                continue
            first += 1
            v,left_e = block[i]
            L = sum(a*b for a,b in zip(l_rows[i],w))
            if best_abs_l is None or abs(L)<best_abs_l:
                best_abs_l, best_count = abs(L), 0
            if abs(L) == best_abs_l:
                best_count += 1
            if L == 0:
                h = multiply(v,w)
                assert (h[0]-h[2],h[1]-h[3]) == (2,0)
                hits.append((left_e+right_e,*measure(B,traces,h,0,2**53)))
    print("orbit, words, K=2, minimum |L| among K=2, ties, joint:",
          orbit,len(left)*len(right),first,best_abs_l,best_count,len(hits),flush=True)
    print("minimum positive 40L+33K, number attaining:", min_t, min_t_count,flush=True)
    for hit in hits:
        print("exponents, P(-1), whole measure:",*hit)


if __name__ == "__main__":
    bases, unit_words = generators()
    B, traces = polynomial_data()
    for orbit, base in enumerate(bases):
        run(orbit, base, unit_words, B, traces)
