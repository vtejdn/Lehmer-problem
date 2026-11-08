"""Full conductor-6561 split-field sieve for sparse positive-unit adjustments."""
from collections import Counter
from math import comb, isqrt
import os
from pathlib import Path
import sys
from typing import NamedTuple

if "--select" in sys.argv:
    os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
from flint import arb, ctx, fmpq

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Yin_J_G0148"))
from cuts import target_cut

P = 3**8
N = P//2
K_TARGET, L_TARGET = 3, 4
CUT = 746
MODULI = (39367, 52489)
SEEDS = ("original", "alternating", "balanced", "balanced transferred")
BALANCED_FLIPS = int(
    "410300000000000400000008902c270882324120080850080012020028c000401118200200800000"
    "230403018442040000020049a008010400010b002000148500600502d400001014800400008040809"
    "20000c0100080b800080844800080100000a000100000084008001220000494084800009002204400"
    "000000680040401008200080d40001000201810084000000000282000000020990114400407b080084"
    "410800000005080060141801040800000900640140008040000004c00002008001208004100000",16)
DIRECTIONS = np.array([d for d in range(1, N+1) if d % 3], dtype=np.int64)
ANCHORS = 16


class FieldData(NamedTuple):
    frequencies: tuple
    weights: np.ndarray
    cosine: np.ndarray


def signature_columns():
    """Solve and check the v8 full-grid sign system over F_2."""
    indices = np.arange(1,N+1,dtype=np.int64)
    rows = []
    for j in range(1,N+1):
        residues = 4 * ((j*indices) % P)
        bits = np.packbits((P < residues) & (residues < 3*P), bitorder='little')
        rows.append(int.from_bytes(bits.tobytes(),'little') | (int(j>N-CUT) << N))
    for a in range(N):
        bit = 1 << a
        pivot = next(i for i in range(a,N) if rows[i] & bit)
        rows[pivot], rows[a] = rows[a], rows[pivot]
        value = rows[a]
        for i,row in enumerate(rows):
            if i != a and row & bit:
                rows[i] = row ^ value
    selected = [i+1 for i,row in enumerate(rows) if row >> N]
    labels = np.array(selected,dtype=np.int64)
    for j in range(1,N+1):
        r = 4 * ((j*labels) % P)
        assert np.count_nonzero((P < r) & (r < 3*P)) % 2 == (j > N-CUT)
    return selected


def scale(a):
    s = 1
    while a % (3*s) == 0:
        s *= 3
    return s


def split_spectra(selected, q):
    assert (q-1) % P == 0 and all(q % d for d in range(2,isqrt(q)+1))
    root = next(pow(a,(q-1)//P,q) for a in range(2,q)
                if pow(a,(q-1)//3,q) != 1)
    assert pow(root,P,q) == 1 and pow(root,P//3,q) != 1
    powers = [pow(root,j,q) for j in range(P)]
    b = np.array([(powers[j]+powers[-j]) % q for j in range(P)],dtype=np.int64)
    inverse_b = np.array([pow(int(v),-1,q) for v in b],dtype=np.int64)
    indices = np.arange(1,N+1,dtype=np.int64)
    h = np.ones((len(SEEDS),N),dtype=np.int64)
    counts = Counter()
    # Alternate starting with the original quotient in each valuation group.
    for i,a in enumerate(selected):
        s = scale(a)
        direct = (b[(a*indices)%P]*inverse_b[(s*indices)%P])%q
        inverse = (b[(s*indices)%P]*inverse_b[(a*indices)%P])%q
        h[0] = (h[0]*direct)%q
        flip = counts[s] % 2
        h[1] = (h[1]*(inverse if flip else direct))%q
        h[2] = (h[2]*(inverse if flip ^ (BALANCED_FLIPS>>i & 1) else direct))%q
        counts[s] += 1
    for s, count in counts.items():
        if count % 2:
            h = (h*b[(s*indices)%P])%q
    assert sum((s-1)//2 for s,count in counts.items() if count%2) == 1502
    correction = np.array([
        (pow(int(b[3*j%P]),8,q)*pow(int(b[9*j%P]),-2,q))%q for j in indices
    ],dtype=np.int64)
    h[3] = (h[2]*correction)%q
    # Independently check the signed layer norms of both representatives.
    for ell in range(1,9):
        d = 3**(ell-1)
        norder = 3*d
        layer = (indices%(P//norder) == 0) & (indices%(3*(P//norder)) != 0)
        assert np.count_nonzero(layer) == d
        negative = int(np.count_nonzero(layer & (indices>N-CUT)))
        valuation = sum(c%2 for s,c in counts.items() if s>=norder)
        assert valuation == (5,4,3,3,2,2,1,0)[ell-1]
        for i, seed in enumerate(h):
            v = valuation + ((6,-2,0,0,0,0,0,0)[ell-1] if i==3 else 0)
            norm = (-1)**negative * 2**(d*v)
            result = 1
            for v in seed[layer]:
                result = (result*int(v))%q
            assert result == norm%q
    nu = (((4-b[indices]**2)%q)*pow(P,-1,q))%q
    moments = (h*nu)%q
    weights = np.concatenate((moments,(moments*b[indices])%q)).T
    assert N*q*q < 2**63
    # Rows are K for both centers, then L for both centers.
    full = np.zeros((2*len(SEEDS),P),dtype=np.int64)
    for start in range(0,N+1,128):
        freq = np.arange(start,min(start+128,N+1),dtype=np.int64)
        cosine = b[(freq[:,None]*indices)%P]
        values = (cosine@weights)%q
        full[:,freq] = values.T
        full[:,(-freq)%P] = values.T
    return tuple(FieldData((full[i],full[i+len(SEEDS)]),weights[:,[i,i+len(SEEDS)]],b)
                 for i in range(len(SEEDS)))


def value_at(selected, seed, j):
    if seed not in range(len(SEEDS)):
        raise ValueError("unknown center")
    ctx.prec = 160
    cosine = [2*arb.cos_pi_fmpq(fmpq(2*j*a % (2*P),P)) for a in range(P)]
    counts = Counter()
    value = arb(1)
    for i,a in enumerate(selected):
        s = scale(a)
        ratio = cosine[a]/cosine[s]
        flip = (counts[s] % 2) ^ ((BALANCED_FLIPS>>i & 1) if seed in (2,3) else 0)
        if seed and flip:
            ratio = 1/ratio
        value *= ratio
        counts[s] += 1
    for s,c in counts.items():
        if c % 2:
            value *= cosine[s]
    if seed == 3:
        value *= cosine[3]**8 / cosine[9]**2
    b = cosine[1]
    return (4-b*b)*(b+arb(68)/45)*value/P


def protected_node(selected, seed, j, binary_exponent, length):
    """Bound a single positive summand of L+68K/45 on an entire word ball."""
    contribution = value_at(selected,seed,j)
    assert contribution > 2**binary_exponent
    assert contribution < 2**(binary_exponent+1)
    assert 15*2**binary_exponent > 128*P**(2*length)
    print(SEEDS[seed], "protected node, floor log2 contribution, excluded length:",
          j,binary_exponent,length,flush=True)


def balancing_mask(selected):
    """Numerically choose quotient flips; the exact stored input is checked separately."""
    j = np.arange(1,N+1)
    b = 2*np.cos((2*np.pi/P)*np.arange(P))
    logcos = np.log(abs(b))
    steps = np.array([logcos[(a*j)%P]-logcos[(scale(a)*j)%P] for a in selected])
    counts = Counter()
    signs = np.ones(len(selected),dtype=np.int8)
    for i,a in enumerate(selected):
        s = scale(a)
        if counts[s]%2:
            signs[i] = -1
        counts[s] += 1
    initial = signs.copy()
    offset = np.log((4-b[j]**2)*abs(b[j]+68/45)/P)
    for s,count in counts.items():
        if count%2:
            offset += logcos[(s*j)%P]
    for alpha in (0.02,0.05,0.10,0.20,0.40,0.70,1.0):
        minus, plus = np.exp(-2*alpha*steps), np.exp(2*alpha*steps)
        for iteration in range(1000):
            weights = np.exp(alpha*(offset+signs@steps))
            costs = np.where(signs>0,minus@weights,plus@weights)
            best = costs.min()
            if best >= (1-1e-11)*weights.sum():
                break
            i = np.flatnonzero(costs <= best*(1+1e-12))[0]
            signs[i] *= -1
        else:
            raise RuntimeError("selector did not finish a stage")
        print("balancing stage, flips:",alpha,iteration,flush=True)
    return sum(1<<int(i) for i in np.flatnonzero(signs!=initial))


def balanced_certificate(selected):
    ctx.prec = 160
    exponents = Counter()
    counts = Counter()
    for i,a in enumerate(selected):
        s = scale(a)
        flip = (counts[s]%2) ^ (BALANCED_FLIPS>>i & 1)
        sign = -1 if flip else 1
        exponents[a] += sign
        exponents[s] -= sign
        counts[s] += 1
    for s,count in counts.items():
        exponents[s] += count%2
    b = [2*arb.cos_pi_fmpq(fmpq(2*i,P)) for i in range(P)]
    logs = [abs(v).log() for v in b]
    weighted = [(a,e) for a,e in exponents.items() if e]
    moments = [[arb(0),arb(0)] for _ in range(2)]
    for j in range(1,N+1):
        logabs = sum((e*logs[a*j%P] for a,e in weighted),arb(0))
        r = (4-b[j]**2)*logabs.exp()/P
        if j>N-CUT:
            r = -r
        transfer = b[3*j%P]**8 / b[9*j%P]**2
        for row, value in zip(moments,(r,r*transfer),strict=True):
            row[0] += value
            row[1] += b[j]*value
    exact = []
    for row in moments:
        k,l = (v.unique_fmpz() for v in row)
        assert k is not None and l is not None
        exact.append((int(k),int(l)))
    numerator = 45*exact[0][1]+68*exact[0][0]
    assert 45*2**69 < numerator < 45*2**70
    assert value_at(selected,0,1640) > (64*P**1290)*value_at(selected,2,1640)
    component = value_at(selected,2,1892)
    assert component > P**10*value_at(selected,1,1892)
    assert 2_270_280_229 < component < 2_270_280_230
    print("balanced center exact K,L,45T:",*exact[0],numerator,flush=True)
    print("transferred center exact K,L,45T:",*exact[1],45*exact[1][1]+68*exact[1][0],flush=True)
    return exact


def adjusted(s, f, q):
    if f is None:
        return s
    return (2*s+np.roll(s,f)+np.roll(s,-f))%q


def short_moment(s, q, labels):
    """Recover a sparse word at a single entry without a batch mask."""
    result = s
    for a in labels:
        result = adjusted(result,a,q)
    return int(result[0])*pow(2,-1,q)%q


def direct_pair(data, q, labels):
    indices = np.arange(1,N+1,dtype=np.int64)
    product = np.ones(N,dtype=np.int64)
    for d in labels:
        product = (product*(2+data.cosine[(d*indices)%P]))%q
    return tuple(int(v)%q for v in product@data.weights)


def scan(spectra, seed, restrict=False):
    q, q2 = MODULI
    field1, field2 = spectra[0][seed], spectra[1][seed]
    first, second = field1.frequencies, field2.frequencies
    counts = Counter()
    unresolved = []
    admissible = DIRECTIONS
    if restrict:
        assert seed == 2
        residues = (1892*DIRECTIONS)%P
        admissible = DIRECTIONS[3*np.minimum(residues,P-residues) <= P]

    def candidate(labels, first_l):
        assert direct_pair(field1,q,labels) == (K_TARGET,first_l%q)
        counts["K mod q"] += 1
        if first_l % q == L_TARGET:
            counts["both mod q"] += 1
        direct_k, direct_l = direct_pair(field2,q2,labels)
        assert direct_k == short_moment(second[0],q2,labels)
        if direct_k == K_TARGET:
            counts["K both moduli"] += 1
            unresolved.append((labels, first_l%q, direct_l))

    # Empty word and single units.
    for length in (0,1):
        if length == 0:
            labels_list = [()]
        else:
            labels_list = [(int(d),) for d in admissible]
        for labels in labels_list:
            counts["words"] += 1
            if short_moment(first[0],q,labels) == K_TARGET:
                candidate(labels,short_moment(first[1],q,labels))

    # All ordered-by-size pairs, plus sorted triples with prescribed smallest index.
    anchors = admissible[admissible <= DIRECTIONS[ANCHORS-1]]
    for anchor in (None,*map(int,anchors)):
        directions = admissible if anchor is None else admissible[admissible>=anchor]
        k,l = (adjusted(s,anchor,q) for s in first)
        base_k, base_l = 2*int(k[0]), 2*int(l[0])
        for i,d in enumerate(directions):
            e = directions[i:]
            counts["words"] += len(e)
            sums, diffs = (d+e)%P, (d-e)%P
            values = (base_k+2*k[d]+2*k[e]+k[sums]+k[diffs])%q
            for j in np.flatnonzero(values==K_TARGET):
                v = int(e[j])
                labels = (int(d),v) if anchor is None else (anchor,int(d),v)
                value_l = base_l+2*l[d]+2*l[v]+l[sums[j]]+l[diffs[j]]
                candidate(labels,int(value_l))
    size = len(admissible)
    expected = 1+size+comb(size+1,2)+sum(comb(size-i+1,2) for i in range(len(anchors)))
    assert counts["words"] == expected
    name = SEEDS[seed] + (" restricted" if restrict else "")
    print(name, "directions, parameter words, K mod q, (K,L) mod q, K both moduli:",
          size,*[counts[k] for k in ("words","K mod q","both mod q","K both moduli")],flush=True)
    return unresolved


if __name__ == "__main__":
    assert target_cut(P) == CUT
    selected = signature_columns()
    if "--select" in sys.argv:
        assert balancing_mask(selected) == BALANCED_FLIPS
    assert BALANCED_FLIPS.bit_count()==208 and BALANCED_FLIPS.bit_length()<=len(selected)
    print("selected columns by scale:",sorted(Counter(map(scale,selected)).items()),flush=True)
    protected_node(selected,0,1640,16374,645)
    protected_node(selected,1,940,153,5)
    exact = balanced_certificate(selected)
    spectra = [split_spectra(selected,q) for q in MODULI]
    for q,rows in zip(MODULI,spectra,strict=True):
        for i,(k,l) in enumerate(exact,2):
            assert direct_pair(rows[i],q,()) == (k%q,l%q)
    scopes = [(i,False) for i in range(len(SEEDS))] + [(2,True)]
    pending = [scan(spectra,i,restrict) for i,restrict in scopes]
    if any(pending):
        # Never report a modular survivor as an integer hit or a negative census.
        q3 = 131221
        third = split_spectra(selected,q3)
        pending = [[row for row in rows if direct_pair(third[i],q3,row[0])[0]==K_TARGET]
                   for (i,_),rows in zip(scopes,pending,strict=True)]
        print("K candidates after third modulus:",list(map(len,pending)),flush=True)
    if any(pending):
        raise RuntimeError(f"exact reconstruction still required for {pending}")
    print("exact K=3 and exact joint (3,4) counts are zero for each listed seed")
