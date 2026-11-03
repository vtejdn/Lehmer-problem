---
author: Yin
---

<a id="ope26c-u002"></a>
# Ope26c-U002: singularity for every fixed quartic Salem parameter

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Ope26c; [retained PDF](../../../literature/pdf/Ope26c.pdf).

Passages: Manuscript dated 3 October 2026 at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; complete Section 5, Theorem 5.1, Lemmas 5.2--5.3, Corollary 5.4, printed/PDF pp. 12--17.

Inspection: 2026-10-07, AI reviewers working for human author Yin at his explicit request to acquire and audit OpenAI Math families 153 and 148. Separately assigned reviewer read the complete Section 5 PDF text and salem.tex and visually checked pp. 13--14. It rederived the source proof before reading local transition drafts; the assignment had identified the topic but supplied no local derivation. The coordinator adopted the detailed report below at this scope. No proof-assistant check is asserted.


## Finding and exact scope

**Audited within scope; no mathematical defect found in the complete Section 5 proof.**
The reviewed assertion is Theorem 5.1: for every fixed degree-four Salem number beta in (1,2), the unbiased law of `sum_{ell>=0} epsilon_ell beta^{-ell}` is singular with respect to Lebesgue measure.
The review also covers Lemmas 5.2-5.3 and Corollary 5.4 in full.
This is an ordinary mathematical proof review, not formal verification, external expert endorsement, or a verdict on the rest of the paper.

The source's quantitative transition-product claim is stronger than mere smallness of central conjugates, but does not claim that the whole product stays bounded away from zero.
The proof establishes the exact rate it uses.

## Checked obligations

### 1. Algebraic trace and initial cosine floor

Locators: PDF p. 12, equations (5.1)-(5.2); p. 13, start of Lemma 5.2 proof; TeX lines 29-55 and 94-126.

For the four embeddings beta, beta^{-1}, z, conjugate(z), beta is a unit.
Thus every `u_{m,j}=A_m beta^j` with integer j is an algebraic integer, and its integer trace is exactly `u_{m,j}+(-1)^m u_{m,-j}+2 Re(c_m z^j)`.
The inverse embedding takes each factor to its negative, which accounts for the parity sign.
An algebraic integer cannot be a rational half-integer, so none of the cosine factors vanishes.

Irrationality of theta/pi follows because a root-of-unity conjugate forces the irreducible polynomial to be cyclotomic, contrary to beta>1.
Dirichlet pigeonhole approximation supplies unbounded good denominators; otherwise their finitely many nonzero approximation errors would have positive minimum.
It therefore supplies k1 with A1>1 and delta1<1/16.
As j tends to negative infinity the cosine tends to one; reflection bounds the other tail below by a positive number.
Only finitely many middle factors remain, all nonzero.
This proves gamma1>0 without assuming an unproved uniform arithmetic bound.

### 2. All constants and both Dirichlet branches in Lemma 5.2

Locators: PDF pp. 13-14, (5.3)-(5.10); TeX lines 116-202.

The k2 bound delta2<=2*pi*delta1/k2 gives k2<=2*pi*delta1*exp(L2), which indeed implies log(K2)<=1.1 L2 once L2 is sufficiently large.
There is no reversal of this inequality.
An arbitrarily unusually good approximation only makes L2 larger and remains harmless.

For N=floor(exp(1.9 L)), the q>=K branch gives k=q<=N, L'>=2.9 L-O(1), b'<=2 exp(1.9 L).
The q<K branch sets k=ceil(K/q)q in [K,2K); the elementary bound `||ceil(K/q)q theta/pi|| <= ceil(K/q)/N <= 2K/N` gives L'>=2.9L-log K-O(1), hence at least 1.75L for the bootstrap.
In this branch b'<=3 exp(1.1L).
The upper bound k<=exp(1.9L) also holds for all sufficiently large L, since 2 exp(1.1L)<exp(1.9L).

For the next K', use K'<=2b'+D L'+1.
The first summand is absorbed in half exp(.75L') using the strict margins `1.9 < .75*2.8` and `1.1 < .75*1.75`; the linear summand is absorbed in the other half for large L'.
No upper bound on L' is needed.
From m>=3, log K<=.75L improves the second branch to L'>=2.15L-O(1)>=2.1L.
A single sufficiently large L2 handles all thresholds because the iteration thereafter increases L geometrically.

For j<=0, the exact shift relation gives a perturbation bounded by beta^(b_m-k) beta^j.
For j>0, reflection at level m+1 adds at most 2*pi*delta_{m+1}.
Therefore the asserted floor recurrence is valid uniformly over all j, not just one half-orbit.
Its total decrement is bounded by the displayed summable series; choosing k2 large leaves gamma_m>=.9 gamma1, so gamma=gamma1/2 is valid.
The same thresholds give precisely 2delta_m<=gamma/(2pi) and beta^(b_m-k)<=exp(-10L_m) <=gamma/(2pi).
There is no circular dependence: gamma1 and k1 are fixed before k2 is made large, and the growth construction does not use gamma.

### 3. The transition-product rate in Lemma 5.3

Locators: PDF pp. 14-15, (5.11)-(5.13); TeX lines 205-269.

The negative tail sum S_m is finite by geometric decay and f(u)=O(u^2) near zero.
On a perturbation segment of length at most gamma/(2pi), the uniform cosine floor gives |cos|>=gamma/2, so f'' is uniformly bounded.
Also |f'(u)|<=(pi/gamma)*sqrt(2f(u)).
Young's inequality gives the displayed Taylor estimate with an m-independent C depending only on the already fixed beta, gamma and eta=.01.

Evenness and period one permit reflection of positive indices with perturbation at most 2delta_m; summation gives sum_{j<=n} f(u_{m,j}) <= 2.01 S_m + C n delta_m^2.
Applying the shift identity to every j<=0 and summing the geometric squared perturbations gives S_{m+1} <= 1.01*2.01 S_m + C(1+k_{m+1}delta_m^2).
Since k_{m+1}delta_m^2<=exp(-.1L_m), the additive term is uniformly bounded.
Thus S_m=O(2.0301^m), whereas L_m grows at least as 2.1^m.
Consequently S_m/L_m tends to zero.
This explicitly checks the growth-rate comparison that an arbitrary small-conjugate multiplier would not provide.

### 4. Uniform phase means and disjoint-window approximation

Locators: PDF pp. 15-16, (5.14)-(5.19); TeX lines 271-368.

The infinite cosine product has a convergent negative tail and only finitely many other factors, hence is nonzero and real.
With J=floor(exp(1.5L)), H=ceil(b+DL), one has H<=K<=exp(.75L) and M=floor((J-H)/(2H+1))+1 >=exp(.7L) eventually.
The loss bound and Jdelta^2<=exp(-.5L) prove the uniform lower mean exp(-L/20) for all 0<=n<=J; the fixed constants merely affect how late this holds.

For j>H, replacing u_j by its integer trace produces the deterministic factor (-1)^{T_j}, since each sign is +/-1.
This does not introduce a random sign into the prefactor.
The phase error can be represented modulo 2pi by the independent, centered sign sum with coefficients u_j-T_j for j>H and u_j for j<-H.
Its L2 variance is therefore the sum of squared coefficients.
The trace relation bounds it by C(beta^(2(b-H))+n delta^2)<=C exp(-L/2).
The retained inclusive index windows [n-H,n+H] have length 2H+1; consecutive n differ by exactly 2H+1, so they are disjoint and contain only nonnegative sign indices.
The truncated random variables are independent.
Subtracting approximation means costs at most a factor two, yielding centered L2 norm <=M^(-1/2)+C exp(-L/4).

### 5. Lebesgue separation really yields singularity

Locators: PDF pp. 16-17, (5.20) and conclusion; TeX lines 370-410.

The true Fourier frequencies pi*A_m*beta^n are separated by at least pi*(beta-1), since A_m>=1 and distinct n are nonnegative integers.
The rank-difference harmonic sum bounds the Lebesgue L2 norm squared of the average by C(1+log M)/M, regardless of the deterministic signs.
The threshold exp(-L/20)/2 lies below half the real mean.
Chebyshev therefore gives complementary convolution mass tending to zero, because the squared error times exp(L/10) has exponents at most -.6L and -.4L.
The same multiplier times the Lebesgue L2 bound tends to zero.

The summable subsequence and limsup argument then produce a Borel set of Lebesgue measure zero carrying full convolution measure.
The proof does not infer singularity merely from Fourier decay/nondecay, nor from small supports at one finite scale.
It proves the defining null-set property directly, so the pure-type theorem from Section 2 is not a dependency of Theorem 5.1.

### 6. Explicit quartics

Locators: PDF p. 17, Corollary 5.4; TeX lines 413-445.

For the two given reciprocal quartics the y=x+x^{-1} substitutions give y^2-y-3 and y^2-2y-1.
Their larger roots lie in (2,5/2), and the other roots lie in (-2,2).
Thus each polynomial has one root in (1,2), its reciprocal, and a nonreal unit-circle pair.
In each real quadratic field, y^2-4 has a negative conjugate and cannot be a square; therefore x^2-yx+1 is irreducible over that field and the degree is four.
The four displayed roots are consequently algebraic conjugates and the Salem hypotheses apply.
The passage to Corollary 5.4 is complete.

## Dependencies and excluded scope

The Section 5 argument is self-contained relative to elementary field trace/integrality, pigeonhole approximation, calculus, independent-sign variance, elementary oscillatory integrals, and measure subadditivity.
The references to Erdos, Salem and Peyriere are historical/mechanism attribution or analogy; no additional asserted theorem from them is needed for the deductions above.
Their original proofs and priority attributions were not re-audited here.
No result in Sections 2-4, Section 6, the degree-31 computation, or Appendix A is required by this proof.

No numerical test substitutes for any infinite construction.
The review does not extend the result to higher-degree Salem numbers: the single unit-circle conjugate pair is used by the one-dimensional Dirichlet estimate and its numerical exponent margins.

## Comparison with current G0001 drafts

After completing the source review, the reviewer read [central-small transition draft](../../../ledger/Yin_L_G0125_v1.md) and [transition averaging draft](../../../ledger/Yin_L_G0126_v1.md), plus the G0001 task contract and selected local interfaces.
This comparison is not a fresh review or adoption of those local proofs.

There is no exhibited contradiction.
The local transition result asserts product convergence to zero without an effective rate.
The source proves a lower bound exp(-o(L_m)), which can still tend to zero; its uniform floor is for individual factors, not for their entire growing product.
Also the local mixed trace product uses a 2pi normalization, whereas this source's sign Fourier product uses pi, so exact product identification would require stating the multiplier/normalization conversion.

Likewise an o(N) smoothed full-orbit entropy budget does not forbid the source's shrinking-threshold separation by sublinear collections of phases.
Source Theorem 5.1 asserts measure singularity, not a dimension deficit, a positive linear entropy saving, an entropy equality, or a degree-independent Mahler gap.
It does not resolve Yin_T_G0001.

The local finite Fejer/Gram argument concerns only what its currently supplied occupancy/collision estimates certify.
The source instead constructs a specific recursively factored multiplier and proves the cosine loss rate directly.
The two statements have different hypotheses and conclusions; failed certification by the local estimates is not a refutation of the source construction.
