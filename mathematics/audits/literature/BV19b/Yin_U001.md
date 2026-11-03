---
author: Yin
---

<a id="bv19b-u001"></a>
# BV19b-U001: Polynomial growth, low-order reductions and the reverse implication

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [BV19b retained article](../../../literature/pdf/BV19b.pdf), arXiv:1810.13363v2, 20 May 2019, journal layout, 8 pages. Acquisition.

Passages: Theorem 1, Corollary 2 and conventions, pp.1--3; complete Section 1, Lemmas 5--6 and Remark 7, p.4. Printed and PDF page numbers coincide.

Inspection: 2026-10-11, human author Yin, direct AI reading and self-review. All eight source pages were read and rendered pages inspected. This unit reconstructs the actual algebraic-unit application and norm argument; prior entropy inspection is reused by an exact link below. Original Chebotarev, prime-number and Erdős--Murty proofs were not audited. No independent second reviewer or formal check.


## Assessment

**Audited within scope**, with F01--F04 below, for the qualitative growth interface, the corrected low-order lemma, and Theorem 4(b) implies (a), using the standard nonzero Lehmer domain.
**Questioned at literal scope** for the zero-inclusive Lehmer/Corollary 2 wording, the claimed numerical constant, and the printed Lemma 6 and relative-field norm estimate.
Lemma 5's full nonintegral formulation is read, but only its algebraic-unit case, actually needed here, is reconstructed.

<a id="bv19b-polynomial-families"></a>
## Polynomial families and growth

All logs denoted by log in this record are base 2.
Write ln explicitly for a natural logarithm.
For integers d >= 0 and K >= 1, put
\[
S_d=\left\{\sum_{i=0}^{d}a_iX^i:a_i\in\{0,1\}\right\},\qquad
S_d^K=\left\{\sum_{i=0}^{d}a_iX^i:a_i\in\mathbb Z,\ |a_i|\le K\right\}.
\]
Evaluation means a set of distinct values, not a multiset.
Noninteger bounds on d or K mean their integer parts.
The zeroth power is one, including at zero.

For z in C let
\[
B_n(z)=S_{n-1}(z),\quad n\ge1,\qquad
\lambda(z)=\lim_{n\to\infty}|B_n(z)|^{1/n}.
\]
The exact block identity B_(m+n)=B_m+z^m B_n gives submultiplicativity, so Fekete's lemma yields
\[
\lambda(z)=\inf_{n\ge1}|B_n(z)|^{1/n},
\qquad |S_d(z)|\ge\lambda(z)^{d+1}.
\]
It also gives the source's limit with exponent 1/d.
In fact |S_(d+e)| <= |S_d||S_e| for positive d,e by using the second block of degree e-1; the source's unshifted submultiplicativity assertion is valid.

For algebraic z, M(z) uses its primitive integer minimal polynomial, including the absolute leading coefficient.
Theorem 1's qualitative statement is
\[
\min\{2,M(z)\}^{c_*}\le\lambda(z)\le\min\{2,M(z)\},
\quad c_*>0\ \hbox{absolute}.
\]
The source's reference [BV16] is the registered [BV20](../../../literature/pdf/BV20.pdf).
Its Theorem 5 and Lemma 16 were reread at retained v4 pp.3--4,18; the [existing proof audit](../BV20/Yin_U001.md#bv20-u001) owns the analytic repairs and constant limitation.
The affine conversion from fair signs to digits 0,1 preserves support cardinality and entropy.
This inspection accepts the positive qualitative constant, not 0.44.

A nonzero algebraic nonunit has M >= 2, so the upper support bound 2 is enough there.
The algebraic-unit upper estimate is supplied by the lattice counting argument of BV20 Lemma 16.
At z=0 the rate is one directly.
A transcendental z has |S_d(z)|=2^(d+1).
A root of unity of fixed order m has at most (d+2)^m evaluations, hence rate one.

<a id="bv19b-lehmer-domain"></a>
## Correct Lehmer domain and Corollary 2

The standard uniform-gap assertion is: some kappa > 0 satisfies M(z) > 1+kappa for every **nonzero** algebraic z that is not a root of unity.
With that domain, Theorem 1 proves the uniform complex support-growth formulation in Corollary 2; transcendental numbers have rate two.
Conversely the upper estimate transfers a support-growth gap to M.
Strict versus non-strict gaps can be settled by decreasing the constant.

**F01 -- missing zero exclusion, p.2.**
Literally, both the stated Lehmer domain and Corollary 2 include z=0, although M(0)=1 and |S_d(0)|=2.
Add z != 0.
The finite-field proofs already use nonzero elements.

**F02 -- unverified numerical strengthening, p.2.**
The unconditional assertion that c=0.44 can be used is stronger than the retained BV20 proof evidence: that source describes its calculation as non-rigorous and supplies no integration error certificate.
The existential constant suffices for every qualitative implication here.
This is the previously recorded BV20 limitation propagated to this new consumer; no numerical certification is claimed.

## Lemma 5 in the actual unit domain

For a fixed algebraic unit z, its integer-ring Minkowski embedding is a lattice.
At each real or complex embedding sigma, a value of S_d^K(z) has modulus at most
\[
K(d+1)\max\{1,|\sigma(z)|\}^{d}.
\]
Lattice-cell counting in the corresponding real/complex boxes, with complex coordinates counted twice, gives
\[
|S_d^K(z)|\le C_z(Kd)^{C_z}M(z)^d,\qquad d,K\ge1.
\]
Constants depend on z, not on d,K.
This is the unit specialization of source Lemma 5; the broader nonintegral statement's original cited proof is not certified by this unit.
A selected counting passage was also read in the retained [Bre07](../../../literature/pdf/Bre07.pdf), preprint pp.15--16; its layout is not assumed to be the source's cited journal Section 8.

## Corrected Lemma 6 and its proof

Let F/Q be a fixed finite Galois extension and z in O_F be nonzero and **not a root of unity**.
Let P_z contain primes having a degree-one prime ideal above them at which z is nonzero and has order at most sqrt(p/log p).
Then
\[
|P_z\cap[1,X]|=o(\pi(X)).
\]

Put N=floor(sqrt(X/log X)) and r=[F:Q]/[Q(z):Q].
Every p in P_z intersect [sqrt(X),X] divides at least one nonzero integer N_(F/Q)(z^n-1), n <= N.
Nonvanishing is essential.
Since embeddings of Q(z) repeat r times,
\[
|N_{F/\mathbb Q}(z^n-1)|
\le 2^{[F:\mathbb Q]}M(z)^{rn}.
\]
Taking logs of the product gives
\[
|P_z\cap[\sqrt X,X]|\tfrac12\log X
\le [F:\mathbb Q]N+
r\log M(z)\,\tfrac{N(N+1)}2.
\]
Adding primes below sqrt(X) yields, for fixed F,z,
\[
|P_z\cap[1,X]|=O_{F,z}(X/(\log X)^2+\sqrt X)=o(\pi(X)),
\]
using the standard lower bound pi(X) >> X/log X.
No field-uniform estimate is asserted.

**F03 -- false hypothesis range, Lemma 6 p.4.**
Take F=Q and z=1.
Every prime qualifies, its residue order is one, and the claimed zero density is false.
The proposed product of norms then contains zeros.
Excluding roots of unity repairs the lemma and matches its intended application.

**F04 -- missing embedding multiplicity, Lemma 6 p.4.**
The printed exponent M(z)^n must be M(z)^(rn).
For F=Q(sqrt(2)), z=2 and n=4, the norm is 225, whereas the printed upper bound is 4*16=64.
This arithmetic witness was rerun on 2026-10-11.
The corrected fixed-field factor does not affect the density conclusion.

Remark 7's unconditional replacement of the threshold by sqrt(p)*epsilon(p), for positive epsilon(p) tending to zero, follows by using sup_(t >= sqrt(X)) epsilon(t)=o(1) in the same product bound.
Its separately reported RH-dependent Erdős--Murty refinement was not primary-source checked and is not used.

## Theorem 4(b) implies (a)

Suppose the standard Lehmer gap fails.
For any small delta > 0 choose a non-torsion algebraic unit z with M(z)<1+delta^2/2.
Choose epsilon > 0 so that C_z epsilon < delta^2/4.
Lemma 5 gives
\[
|S_d^{\lfloor 2^{\epsilon d}\rfloor}(z)|\le 2^{\delta^2d}
\]
for all sufficiently large d: log_2(1+delta^2/2) <= delta^2/(2 ln 2), and 1/(2 ln 2)+1/4 < 1.
The finitely many smaller d have bounded K and bounded cardinality, so for sufficiently large p they also satisfy the required p^delta bound.

Let F be the Galois closure of Q(z).
Retain the established Chebotarev input, invoked at BV19b p.4: completely split primes have positive natural density among rational primes for this fixed F.
At such primes the reduction lies in F_p and, being a unit, is nonzero.
Reduction cannot increase evaluation cardinality; for every d <= (log p)/delta and every integer K <= 2^(epsilon d), the upper bound is p^delta.
Corrected Lemma 6 discards only a zero-density set of primes with insufficient order.
Thus (delta,epsilon)-very bad primes have positive density, contradicting Theorem 4(b).

Chebotarev and the prime-counting lower bound are accepted established inputs at their stated fixed-field interfaces; their original proofs are retained externally.
The norm-product deduction and all finite-degree/floor completions above were checked directly.

## Verification and boundaries

The source's zero, torsion and repeated-embedding issues are existing defects in the unchanged v2 bytes, newly recorded here; F02 was already known in BV20.
No author-confirmed erratum was located by the bounded exact-title/erratum search on 2026-10-11.
This does not establish that no erratum exists.
Theorems 3--4 reformulate a conjecture; this audit proves no Lehmer gap and adopts no research Task or project Claim.
