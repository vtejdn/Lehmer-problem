---
author: Yin
---

# A uniform Pisot gap for every fixed Chebyshev offset and its sparse perturbations

<a id="statement"></a>
## The first nonconstant term of a sparse trace numerator

Fix \(d,s\ge1\) integral and \(\epsilon>0\).
Let \(f\) be a positive-constant Pisot minimal polynomial on branch \(j=2\), with exterior root \(\theta\), constant \(q\ge2\), and [trace numerator](Yin_C_G0345_v7.md#trace) \(C\) of degree \(h\).
Put \(\Pi(z)=(1-z^2)z^h C(z+z^{-1})\).
If \(\Pi\) has at most \(s\) nonzero terms and agrees with \(2-z^d\) through degree \(\lfloor\epsilon h\rfloor\), then \(q\) is bounded in terms of \(d,s,\epsilon\) alone.
Consequently \(\theta-q\) has a uniform positive lower bound on this class by the [derivative identity](../ledger/Yin_L_G0462_v36.md#second).
For odd \(d\) the same conclusions hold with \(2+z^d\) in place of \(2-z^d\).

In particular, no sequence from the inverse construction with
\[
             C(x)=2U_h(x/2)-U_{h-d}(x/2),\qquad h\ge d,
\]
and any fixed \(d\) can have \(q\to\infty\), in either degree parity of \(f\).
Its lift is \(2-z^d+z^{2h+2-d}(1-2z^d)\).
The bounds here need not be uniform as \(d\) grows.
Agent-S obtained the finite primitive slope calculation used below.
The main researcher developed the finite-shape criterion, the specialization at large prime orders and the exclusion of all remaining fixed offsets.

<a id="harmonics"></a>
## Integral Laurent polynomials at every frequency

Suppose \(q\to\infty\).
The argument for [sparse perturbations at offset one](../ledger/Yin_L_G0462_v51.md#stability) gives \(h\to\infty\), bounded \(\|\Pi\|_\infty\), and a subsequential rational limit \(K\) of the normalized series \(K_q\).
Write \(A=2-z^d\).
In the plus case with odd \(d\) replace every series argument by \(-z\), which preserves integrality, rationality, circle norms and the vanishing mass of the negative atom.
In both cases \(B^\sharp=z^{h+1}B(z+z^{-1})\) (with the same rotation if used) satisfies \(K_qB^\sharp=\Pi\), and \(B_\infty=A/K\) has integer Taylor coefficients.
The [fixed-offset classification](../ledger/Yin_L_G0462_v55.md#fixed) gives \(K=A U/V\) with \(U,V\) coprime signed cyclotomic products, normalized at zero.
Its primitive slope table applies also to the perturbations: the proof uses only the limiting numerator \(A\), the integral limit \(A/K\), rationality and positivity of \(K\) and its nonzero integer trigonometric-polynomial density \(\rho=2\Re K\) away from atoms.
All these facts hold on the common prefix as in [the offset-one reduction](../ledger/Yin_L_G0462_v51.md#limit).

Put \(J_q=2/K_q\) and \(J=2/K\).
If \(n\) is the first discrepancy of \(B^\sharp\) from \(B_\infty=V/U\), then \(n\to\infty\) and \(n/h\to0\).
Indeed, if the two \(B\)'s agree through a positive fraction of the degree, \(J_q-J\) vanishes on such a prefix by \(\Pi J_q=2B^\sharp\).
Apply the [two bounded cutoffs](../ledger/Yin_L_G0462_v51.md#window) to
\[
             A U B^\sharp -V\Pi=(A U/2)\Pi(J_q-J).
\]
The coefficients of \(J_q-J\) at positive indices again come from a measure of bounded variation, and the factors \(A,U,\Pi\) have uniformly bounded circle suprema.
Choose the cutoff length \(L\) there larger than both polynomial degrees by including the fixed degree \(d\).
Since \(|A|\ge1\) on the circle, this gives bounded \(L^1\) norm of the integer polynomial \(UB^\sharp\), hence a bounded number of terms.
Its measure tends to one strictly from above, contradicting the [fixed-support gap](../ledger/Yin_L_G0462_v32.md#boyd-return).
The argument also covers equality with the entire series \(B_\infty\) on a subsequence.

Every index \(kn+l\), with fixed \(k\ge1,\ l\in\mathbb Z\), now belongs to the prefix where \(B^\sharp=(A/2)J_q\).
Use the [reflected two-circle measure and its harmonic comparison](../ledger/Yin_L_G0462_v52.md#harmonics).
At the first discrepancy the limiting difference of the \(J\) coefficients vanishes at every negative offset, since the factor \(A/2\) has constant one.
This identifies the atomic first moment with that of the shifted limiting atoms, by averaging the vanishing Fourier coefficients in [the departure proof](../ledger/Yin_L_G0462_v49.md#departure).
Equality of its modulus to the whole fiber mass then identifies every atomic harmonic, just as for \(d=1\).
The continuous part supplies circle probabilities with moments \(c_k(v)\), continuous at each regular circle point where the continuous marginal density \(\sigma=2\Re J>0\).
More precisely
\[
       H_k(v)=(1-v^d/2)\sigma(v)c_k(v)\ \in\mathbb Z[v,v^{-1}],
       \qquad |H_k(v)|\le D(v):=|1-v^d/2|\sigma(v),\qquad H_1\ne0.       \tag{1}
\]
Indeed multiplication by \(1-v^d/2\) gives integral coefficient differences at every fixed offset, by the common prefix including the offset \(l-d\).
The continuous density of the rational Herglotz function is bounded after separating the finitely many atoms, so Parseval leaves finitely many nonzero integer coefficients for each \(k\).
Formula (1) first holds almost everywhere, and positivity of all finite Toeplitz matrices extends to every regular point by continuity.
With \(M\) denoting multiplicative Mahler measure,
\[
              M(D)=M(\rho)/2,                                         \tag{2}
\]
because \(\sigma=2\rho/|K|^2\), \(M(K)=M(A)=2\), and \(M(1-z^d/2)=1\).

<a id="finite-shapes"></a>
## A finite set of polynomials when the envelope has small measure

If \(D\) is a bounded nonnegative circle function with \(M(D)<\sqrt2\), there are only finitely many nonzero integer Laurent polynomials \(P\), up to monomial shift, satisfying \(|P|\le D\).
In fact their squared coefficient sums are bounded by \(\int D^2\).
Normalize their least exponent to zero.
If infinitely many remained, extract a sequence with fixed term count and coefficients, but unbounded degrees.
Pass to a subsequence on which each consecutive exponent difference is fixed or tends to infinity.
The resulting separated blocks are monomial translates of fixed nonzero integer polynomials \(P_i\), with at least two blocks.
The squared moduli converge weakly against continuous tests to \(\sum_i |P_i|^2\), since cross terms have frequencies escaping in absolute value.
Consequently \(\sum_i |P_i|^2\le D^2\) almost everywhere.
For any two blocks the pointwise inequality \(|P_1|^2+|P_2|^2\ge2|P_1P_2|\) yields \(M(D)^2\ge2 M(P_1)M(P_2)\ge2\).
This contradicts the hypothesis.

<a id="torsion"></a>
## Specializing a finite set of shapes at a large prime

We now show that (1) is impossible whenever \(M(D)<2\) and the nonzero \(H_k\) range over finitely many Laurent polynomials up to monomial shifts.
Let \(P\) range over a finite list of representatives that actually occur.
Each \(M(P)\le M(D)<2\), and in particular \(A\) cannot divide any \(P\), since \(A\) is irreducible by Eisenstein at two and \(M(A)=2\).
Define the rational function
\[
        R_P(z)=\frac{P(z)(2-z^{-d})}{P(z^{-1})(2-z^d)} .
\]
It has a pole at the real point \(2^{1/d}>1\).
Thus \(R_P(z^2)=R_P(z)^2\) cannot be a rational identity, as iteration would give infinitely many distinct poles.
For all sufficiently large odd primes \(p\) and every primitive \(p\)-th root \(\xi\), the rational functions here are regular and nonzero at \(\xi,\xi^2\), as are \(\sigma\) and \(D\) in (1) where used.
This excludes only finitely many roots since the circle density is represented by a fixed nonzero rational function on regular points.
Moreover \(R_P(\xi)\notin\mu_p\): otherwise the automorphism \(\xi\mapsto\xi^2\) of the cyclotomic field would give \(R_P(\xi^2)=R_P(\xi)^2\).
The nonidentity just established allows only finitely many such \(\xi\) for the entire list.
At a prime beyond these exceptions any nonzero \(c_k(\xi)\) is nonreal, since its quotient by its conjugate is \(\xi^{2e}R_P(\xi)\) for \(H_k=z^eP\).

Fix such a prime.
The two-sided moment sequence \(c_k(\xi)\), with \(c_0=1\) and \(c_{-k}=\overline{c_k}\), is eventually periodic for positive \(k\).
To verify this, multiply by a common positive integer \(m\) so that all the values lie in \(\mathbb Z[\xi]\).
One denominator depending on \(\xi\) suffices in (1), since \((1-\xi^d/2)\sigma(\xi)\) is a fixed nonzero cyclotomic field element and each \(H_k(\xi)\) belongs to \(\mathbb Z[\xi]\).
At every Galois conjugate of \(\xi\) we again have Fourier coefficients of a probability, by positivity at every regular point, and the formulas are Galois compatible by rational coefficients and complex conjugation in an abelian extension.
The integer coordinates of \(m c_k(\xi)\) in the power basis of \(\mathbb Z[\xi]\) are fixed complex linear combinations of these conjugate sequences, by inversion of their Vandermonde matrix.
Each coordinate sequence is therefore an integer Fourier–Stieltjes transform on \(\mathbb Z\).
The [integer Fourier–Stieltjes theorem](../audits/literature/San20/Yin_U001.md#fourier-stieltjes) makes every one periodic outside a finite set.
Taking a common period gives the claim.

With that period \(T\), the positive-tail value at multiples of \(T\) is the mass of \(\mu_T\) for the specialized probability, by Cesàro averaging its moments.
Since a nonzero value there cannot be real, this mass vanishes.
The same averages on \(Tl+a\) integrate \(u^a\) over \(\mu_T\) and vanish for every \(a\).
All sufficiently late \(c_k(\xi)\) are zero.
None of our shapes vanishes at \(\xi\), so only finitely many \(H_k\) are nonzero.
Let \(r\ge1\) be the largest such \(k\).
Pushing each regular conditional probability through \(u\mapsto u^r\) leaves just its constant and first conjugate pair of moments.
Its density \(1+2\Re(c_r(v)\bar u)\) is nonnegative, so \(|c_r(v)|\le1/2\).
Therefore \(1\le M(H_r)\le M(D)/2<1\), a contradiction.

<a id="brackets"></a>
## Checking the primitive slope possibilities

For the [primitive table](../ledger/Yin_L_G0462_v55.md#fixed) put \(w=z^g,\ a=d/g\), and denote the sign in its bracket by \(\delta\).
The measure \(M(\rho)\) equals the measure of
\[
       (2-w^a)+\delta w^b(2w^a-1),
\]
since monomial shifts, cyclotomic factors in the rational quotient and power substitutions do not change the measure.
For \(a=1\) the [offset-one bracket factorizations](../ledger/Yin_L_G0462_v44.md#phase) give \(M(\rho)\le(3+\sqrt5)/2<2\sqrt2\) except in two cases.
For \(b=-1,\delta=+\) there are no torsion factors and \(K=2-z^d\).
For \(b=0,\delta=-\) the only odd-order bracket zeros are the \(d\) simple roots of \(1-z^d\), and the degree difference \(\deg V-\deg U=d\) puts every one in \(V\).
Thus \(K=(2-z^d)/(1-z^d)\).
These identifications allow arbitrary factor splitting over \(\mathbb Q\) after \(w=z^g\).

For \(a\ge2\) all seven entries have \(M(\rho)<2\sqrt2\).
At \(a=2,\ b=-1\) the noncyclotomic part is \(w^2\mp3w+1\), of measure \((3+\sqrt5)/2\).
At \((a,b,\delta)=(3,-4,+),(4,-3,+),(4,-3,-)\) it consists of the cubic \(w^3+w-1\) and its reciprocal, up to sign and \(w\mapsto-w\).
Indeed the remaining linear factor is \(w+1\) in the first two cases and \(w-1\) in the last.
The cubic has exactly one real root \(\gamma\in(2/3,1)\) by monotonicity, so its two conjugate nonreal roots each have modulus \(\gamma^{-1/2}\).
The product measure is \(\gamma^{-2}<9/4\).
At \((3,-1,-)\) the bracket is cyclotomic up to a monomial and sign.
At \((3,-2,-)\) division by the linear factor leaves \(w^4+w^3+3w^2+w+1\), whose traces satisfy \(x^2+x+1=0\).
If \(R>1\) is the modulus of an exterior root, the trace coordinates give
\[
       \frac{1}{4(R+R^{-1})^2}+\frac{3}{4(R-R^{-1})^2}=1.
\]
Hence \(R^2+R^{-2}=(1+\sqrt{21})/2\), so \(M(\rho)=R^2<5/2\).
In every case with \(M(\rho)<2\sqrt2\), (2) and the [finite-shape lemma](#finite-shapes) apply, and the prime specialization rules the case out.

<a id="exceptions"></a>
## Finiteness for the two larger envelopes

For \(K=2-z^d\), put \(w=z^d,\ x=w+w^{-1}\).
Then \(D^2=(4-x)^2/(5-2x)\le4\), with equality only at \(w=\pm1\) and circle mean \(7/2\), unchanged by substitution.
The [trinomial fourth-moment argument](../ledger/Yin_L_G0462_v50.md#shapes) needs only this upper bound and mean and shows each \(H_k\) has at most two unit terms.
After a monomial shift and sign a binomial is \(1\pm z^l\).
At every point of modulus-two alignment one must have \(z^d=\pm1\).
There are \(l\) distinct alignment points and only \(2d\) preimages of \(\{\pm1\}\), so \(l\le2d\).
This gives finitely many shapes, while \(M(D)=(2+\sqrt3)/2<2\).

For \(K=(2-z^d)/(1-z^d)\), we have \(D=3|1-z^d|^2/|2-z^d|\).
Every \(H_k\) is divisible as a Laurent polynomial by \((1-z^d)^2\), since (1) forces at least quadratic vanishing at every \(d\)-th root of unity.
The integer quotient \(P_0\) has \(|P_0|^2\le9/|2-z^d|^2\), whose mean is three.
Equality of means would force \((2-z^d)P_0\) to have constant nonzero circle modulus, so it would be a monomial and could not vanish at \(2^{1/d}\).
Thus up to monomial shift and overall sign \(P_0\) is 1 or \(1\pm z^l\).
For \(l\ne d\) the latter gives mean ten for \(|(2-z^d)P_0|^2\) by orthogonality, exceeding nine.
This already leaves finitely many shapes, and \(M(D)=3/2<2\).
Applying the prime specialization in both exceptional cases completes the proof.

## Assessment history

### Decision fixed-offset-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T14:42 |
| status | open |
| reason | Submit the fixed-offset bound, including bounded-support perturbations outside a linear prefix. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed offsets](#statement) | All fixed offsets for the minus sign, odd offsets for the plus sign, uniform over the stated perturbations. |
| argument | [Harmonic rows](#harmonics) | Fixed numerator reduction, sublinear first departure and the positive two-circle limit with integral Laurent rows. |
| argument | [Finite shapes](#finite-shapes) | Bounded energy and separated integer polynomial blocks. |
| argument | [Prime specialization](#torsion) | Nonmonomial phase ratio, cyclotomic coordinates, eventual periodicity and the last harmonic. |
| argument | [Primitive measures](#brackets) | Measures for the finite list and identification of the two exceptional limits. |
| argument | [Exceptional shapes](#exceptions) | Direct finiteness from the pointwise envelope when its measure exceeds the small-measure threshold. |
| dependency | [Primitive offset table](../ledger/Yin_L_G0462_v55.md#fixed) | All possible arithmetic slopes and prescribed factors. |
| dependency | [Sparse perturbations](../ledger/Yin_L_G0462_v51.md#window) | Bounded cutoffs for the reciprocal series and common numerator prefix. |
| dependency | [Integral moving harmonics](../ledger/Yin_L_G0462_v52.md#harmonics) | Conditional positivity, reflected coefficient identities and atomic cancellation. |
| dependency | [Sanders's theorem](../audits/literature/San20/Yin_U001.md#san20-u001) | Locally compact integer Fourier–Stieltjes theorem at its recorded applicability. |

### Decision fixed-offset-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T14:55 |
| status | proved |
| reason | Adopt the fixed-offset theorem and sparse perturbation bound after independent inspection of all harmonics and all primitive slopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed offsets](#statement) | All fixed offsets for the minus sign, odd offsets for the plus sign, uniform over the stated perturbations. |
| argument | [Harmonic rows](#harmonics) | Fixed numerator reduction, sublinear first departure and the positive two-circle limit with integral Laurent rows. |
| argument | [Finite shapes](#finite-shapes) | Bounded energy and separated integer polynomial blocks. |
| argument | [Prime specialization](#torsion) | Nonmonomial phase ratio, cyclotomic coordinates, eventual periodicity and the last harmonic. |
| argument | [Primitive measures](#brackets) | Measures for the finite list and identification of the two exceptional limits. |
| argument | [Exceptional shapes](#exceptions) | Direct finiteness from the pointwise envelope when its measure exceeds the small-measure threshold. |
| dependency | [Primitive offset table](../ledger/Yin_L_G0462_v55.md#fixed) | All possible arithmetic slopes and prescribed factors. |
| dependency | [Sparse perturbations](../ledger/Yin_L_G0462_v51.md#window) | Bounded cutoffs for the reciprocal series and common numerator prefix. |
| dependency | [Integral moving harmonics](../ledger/Yin_L_G0462_v52.md#harmonics) | Conditional positivity, reflected coefficient identities and atomic cancellation. |
| dependency | [Sanders's theorem](../audits/literature/San20/Yin_U001.md#san20-u001) | [Locally compact Corollary 12.4](../audits/literature/San20/Yin_U001.md#fourier-stieltjes) applied to integer coordinates on the discrete group of integers. |
| review | [Independent fixed-offset review](../audits/reviews/Yin_R_G0562_v9.md#fixed-offset-review) | Whole fixed-offset proof, including the separated-block bound, Galois coordinates, exceptional envelopes and branch excess. |

## Current assessment

[Selected decision](#decision-fixed-offset-reviewed)
