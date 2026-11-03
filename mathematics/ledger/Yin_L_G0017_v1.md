---
author: Yin
---

# Unbounded discriminant parameter inside the reciprocal integer core

Date: 2026-10-06.
Coordinating AI agent for Yin under [T G0001](../tasks/Yin_T_G0001_v1.md#contract).
Question: can the D bound in L G0015--16 be imposed on the entire irreducible reciprocal noncyclotomic unit core?
The family below refutes that stronger auxiliary assertion, even with all-power degree preservation.
Its measures exceed 2, so the small-measure question and Lehmer remain unresolved.

## Search and source boundary

The current local records did not supply an unbounded-D family inside that core.
Bounded web searches used "discriminant defect Mahler", "Matveev defect polynomial discriminant Lehmer", "Brunault Zudilin Many variations Mahler measures pdf 2.3 discriminant", and "cyclotomic polynomial discriminant formula Phi n 1 prime power pdf".
A MathOverflow discussion supplied a cyclotomic lead only; none of its relative-field or descent assertions is used as a theorem.
The book preview did not supply the proposed section.
The resulting construction uses the [checked Bell inputs](../audits/literature/Bel17/readme.md) and the standard prime-reciprocal divergence, with the local arguments below.
Both attempted acquisitions failed with HTTP403; no nonexistent PDF is claimed.
No novelty or exhaustive-search claim is made.

<a id="reciprocal-discriminant-family"></a>
## An irreducible reciprocal unit family

Let N be a product of the first k odd primes, k>=2, so N>=15.
Write d=phi(N)/2, zeta=exp(2 pi i/N), and let C_N(y) be the monic minimal polynomial of zeta+zeta^(-1).
Its degree is d: Q(zeta) is quadratic over its real trace field, since zeta satisfies t^2-(zeta+zeta^(-1))t+1 and is nonreal.
Its distinct real roots are t_a=2 cos(2 pi a/N), with a coprime to N modulo sign.
Thus

\[
 \Phi_N(x)=x^d C_N(x+x^{-1}).
\]

Define

\[
 Q_N(y)=C_N(y-1),\qquad
 P_N(x)=x^dQ_N(x+x^{-1}). \tag{1}
\]

P_N is monic integral, reciprocal of degree 2d and constant coefficient 1.
Put theta=1+2 cos(2 pi/N)>2 and choose alpha>1 with alpha+alpha^(-1)=theta.
The field K=Q(theta) is totally real of degree d.
The conjugate corresponding to a=(N-1)/2 is theta_a=1-2 cos(pi/N), which lies in (-1,1).
Hence theta^2-4 has a negative real conjugate and is not a square in K.
It follows that [K(alpha):K]=2.
Since theta belongs to Q(alpha), alpha has degree 2d, so P_N is its irreducible minimal polynomial.
It is a noncyclotomic algebraic unit.

All trace roots lie in (-1,3).
Those above 2 give positive real reciprocal root pairs; the others give unit-circle roots.
The trace root theta above is uniquely maximal, because the primitive residue pair +/-1 uniquely maximizes cosine.
The associated alpha is consequently the unique root of largest modulus.
Every positive power preserves its degree: each conjugate fiber of the power map has the same size, while the fiber over alpha^n has just one element by that unique modulus.
Thus deg(alpha^n)=2d for every n>=1.

<a id="discriminant-divergence"></a>
## Exact discriminant and divergence

For any monic squarefree Q of degree d and P(x)=x^dQ(x+x^(-1)), with no trace root +/-2, the quadratic factorization gives

\[
 |\operatorname{disc}P|
 =|Q(2)Q(-2)|\,|\operatorname{disc}Q|^2. \tag{2}
\]

Indeed, the factor for trace root u is x^2-u x+1 with discriminant u^2-4; the resultant of factors for u,v is (u-v)^2.
Multiplying individual discriminants and squared pairwise resultants proves (2).
The trace roots in (1) cannot equal 2: that would make a primitive odd-order N-th root satisfy zeta_a+zeta_a^(-1)=1 and have order 6.
They cannot equal -2 because t_a>-2.

For the unshifted C_N, the checked values Phi_N(1)=Phi_N(-1)=1 imply |C_N(2)C_N(-2)|=1.
Hence (2) and the classical cyclotomic formula give

\[
 |\operatorname{disc}C_N|^2=|\operatorname{disc}\Phi_N|,
 \qquad
 |\operatorname{disc}C_N|^{1/d}
 =\frac{N}{\prod_{p\mid N}p^{1/(p-1)}}. \tag{3}
\]

Translation preserves discriminant, so disc Q_N=disc C_N.
Each theta_a in (-1,3) satisfies |theta_a^2-4|<=5.
Put A_N=|Q_N(2)Q_N(-2)|^(1/(2d)); then 0<A_N<=sqrt(5).
For the actual minimal polynomial P_N the parameter is therefore

\[
 D(P_N)=\frac{2d}{|\operatorname{disc}P_N|^{1/(2d)}}
 =\frac1{A_N}\prod_{p\mid N}(1-1/p)p^{1/(p-1)}
 \ge\frac1{\sqrt5}\prod_{p\mid N}(1-1/p)p^{1/(p-1)}. \tag{4}
\]

For primes p>=11,

\[
 \log((1-1/p)p^{1/(p-1)})
 \ge\frac{\log p-1}{p-1}\ge\frac1p.
\]

The first inequality uses log(1-x)>=-x/(1-x).
The sum of prime reciprocals diverges, so (4) tends to infinity.
For completeness, the elementary divergence argument needs no prime-number asymptotic: if that sum converged, product_p(1-1/p)^(-1) would converge; its finite partial products, expanded as sums over integers with those prime factors, would bound every harmonic partial sum.
This contradicts divergence of the harmonic series.
DLMF 27.11.E8 is checked attribution for the standard divergence fact, not a new unproved premise.

## Why this does not refute Lehmer or the small-measure route

Because N>=15, 2 pi/N<pi/6 and theta>1+sqrt(3)>5/2.
The increasing map x+1/x on x>1 therefore gives alpha>2.
In particular M(P_N)>=alpha>2 and m(P_N)>log2 for every member.
The family cannot provide vanishing positive entropy.

The uniform-D assertion fails on the full reciprocal integer core, including the all-prime-preserving subclass used in L G0015.
A proposed discriminant proof must restrict to a stated small-measure class (for example M<2), or use a bound depending on measure that actually forces a gap.
Formula (4) does not refute either possibility.
The arbitrary-degree family also shows why the full-domain discriminant bound is an unnecessary strengthening of the original goal.

As a hand-checkable first member, C_15(y)=y^4-y^3-4y^2+4y+1, Q_15(y)=y^4-5y^3+5y^2+5y-5, and

\[
 P_{15}(x)=x^8-5x^7+9x^6-10x^5+11x^4-10x^3+9x^2-5x+1.
\]

Here disc C_15=1125, Q_15(2)=1, Q_15(-2)=61 and |disc P_15|=61*1125^2=77203125.
These are direct algebraic checks of (1)--(3); the asymptotic conclusion is proved above, not inferred from samples.

## Review and continuation

The original author check is retained at [R509](../audits/reviews/Yin_R_G0509_v1.md#original-reciprocal-family-author-check).
The complete current family and elementary divergence proof is [C220](../claims/Yin_C_G0220_v1.md#argument), adopted after the [whole current self-review](../audits/reviews/Yin_R_G0509_v1.md#current-reciprocal-family-finding).
Next work must focus on the low-measure domain or another arithmetic mechanism, not try to prove a uniform D bound contradicted by this family.
