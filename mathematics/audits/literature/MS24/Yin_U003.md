---
author: Yin
---

# MS24: The Determinant Formula

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Retained arXiv:2406.15922v1, 19 pages; margin date 2024-06-22 and distinct title-page date 2024-06-25.

Passages: Source: [MS24 PDF](../../../literature/pdf/MS24.pdf), Theorem 1.2, Remark 3.1, Proposition 3.4 and Sections 3.2-3.4, printed/PDF pp. 3, 9, 11-14.

Inspection: Date/reviewer: 2026-09-12, assigned MS24 reviewer.


The registered artifact and acquisition record retain both dates.

## MS24-U003

Source: [MS24 PDF](../../../literature/pdf/MS24.pdf), Theorem 1.2, Remark 3.1, Proposition 3.4 and Sections 3.2-3.4, printed/PDF pp. 3, 9, 11-14.
Date/reviewer: 2026-09-12, assigned MS24 reviewer.
The complete local two-inequality proof was reconstructed.
Primary hypotheses and external dependencies are specified below and in [U005](Yin_U005.md#ms24-u005); this does not claim an independent reproof of those foundations.

### Exact Statement

Let (M,tau) be a finite tracial von Neumann algebra with faithful normal tracial state.
Let s_1,...,s_n be freely independent standard semicircular elements of M, a_i arbitrary elements of M_m(C), and

\[
S=\sum_i a_i\otimes s_i\in M_m(M),
\qquad \eta(b)=\sum_i a_i b a_i^*.
\]

With capacity as in [U001](Yin_U001.md#capacity-and-scaling) and Delta calculated using tr_m tensor tau,

\[
\boxed{\Delta(S)=e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}}.
\]

No selfadjointness, integrality, irreducibility, or attained-minimum assumption on the a_i is required.
Zero capacity is allowed and gives Delta(S)=0.
The rank/capacity equivalence, the finite-tracial kernel argument in the [scaling supplement](Yin_U006.md#ms24-scaling-dependency-review), and the determinant formula additionally give

\[
\operatorname{cap}(\eta)>0
\iff S\text{ has an affiliated inverse}
\iff\Delta(S)>0.
\]

All inverses here are in M_m(L^0(M,tau)), unless explicitly stated otherwise.

### Zero Capacity and Exact Scaling

The dependency-focused recheck on 2026-09-12 gives a direct zero-capacity argument using only the determinant facts already needed below.
If eta(I) is singular, its kernel is a common kernel of all a_i*, so S* has nonzero kernel and Delta(S)=0.
Otherwise eta(b)>0 for every b>0.
For det b=1, let S_b=(eta(b)^(-1/2) tensor 1)S(b^(1/2) tensor 1).
Its normalized second moment is one.
Multiplicativity and the determinant/trace inequality give

\[
\Delta(S)=\det\eta(b)^{1/(2m)}\Delta(S_b)
\leq\det\eta(b)^{1/(2m)}.
\]

Taking the infimum proves Delta(S)=0 when cap(eta)=0.
This includes S=0 and the scalar zero map, and does not require a free-field realization or the rank/capacity equivalence.
The [scaling dependency review](Yin_U006.md#ms24-scaling-dependency-review) independently checks this argument.
The earlier source-following argument through nonfull linear matrices and MSY23 remains valid, but is unnecessary for the formula itself; the separate affiliated-invertibility equivalence still uses the rank interface.

Suppose next that eta is indecomposable and cap(eta)>0.
Gur04's positive minimizer theorem supplies c>0 with det c=1, det eta(c)=cap(eta), for which tilde eta=eta_(eta(c)^(-1/2),c^(1/2)) is doubly stochastic.
Set

\[
\widetilde S=\sum_i\eta(c)^{-1/2}a_i c^{1/2}\otimes s_i.
\]

The positive scaling factors avoid the arbitrary-star error in Lemma 3.5(i).
By [U002](Yin_U002.md#ms24-u002), the hermitization of tilde S has standard semicircular scalar distribution.
Thus Delta(tilde S)=e^(-1/2), while determinant multiplicativity gives

\[
\Delta(S)=\left(\frac{\det\eta(c)}{\det c}\right)^{1/(2m)}
              \Delta(\widetilde S).
\]

This proves Proposition 3.4 at the positive-capacity scope needed below.
The nonzero scalar case is also immediate from the same calculation.

### General Lower Bound

For cap(eta)>0, adjoin a free semicircular family if necessary and construct a selfadjoint M_m(C)-valued semicircular B, free from S with amalgamation over M_m(C), whose covariance is beta(b)=tr_m(b)I.
Choose a Hermitian matrix basis h_1,...,h_(m^2) orthonormal for the **unnormalized** Hilbert-Schmidt inner product Tr_m(x y*).
Then sum_alpha h_alpha b h_alpha=Tr_m(b)I, so coefficients h_alpha/sqrt(m) and a fresh standard semicircular family realize B with the required covariance.
Passing to this tracial free extension preserves S and its determinant.

Put S_t=S+sqrt(t)B and eta_t=eta+t beta.
For t>0, eta_t is strictly positive and therefore admits the preceding exact-scaling treatment.
Monotonicity of capacity yields

\[
\Delta(S_t)^2=e^{-1}\operatorname{cap}(\eta_t)^{1/m}
\ge e^{-1}\operatorname{cap}(\eta)^{1/m}.
\]

The fixed construction gives ||S_t-S||<=sqrt(t)||B||, hence norm convergence of the hermitizations H_t to H and of H_t^2 to H^2.
This directly provides moment convergence and a common finite norm bound; it is an elementary clarification of the source's covariance-continuity route and does not require the separate BM23/Mai22 continuity estimates cited there.
The positive-operator determinant semicontinuity from U001 gives

\[
\Delta(S)^2=\Delta(H^2)
\ge\limsup_{t\downarrow0}\Delta(H_t^2)
\ge e^{-1}\operatorname{cap}(\eta)^{1/m}.
\]

For t>0, the already proved exact formula for the strictly positive eta_t gives Delta(S_t)>0 and hence trivial kernel.
This is only needed if one uses the source's narrower stated version of semicontinuity.

For this lower bound only the strictly positive maps eta_t need an attained minimum.
The [scaling dependency review](Yin_U006.md#ms24-scaling-dependency-review) proves the required attainment directly by a compact sublevel-set argument and derives double stochasticity by differentiation.
The general uniqueness theorem for indecomposable maps is therefore not an additional premise of this passage.

### General Upper Bound

For 0<delta<=1/6 choose c_delta>0 such that

\[
\operatorname{cap}(\eta)\le
d_\delta:=\frac{\det\eta(c_\delta)}{\det c_\delta}
\le e^\delta\operatorname{cap}(\eta).
\]

Existence follows from the defining infimum and its positive value; attainment is not assumed.
The expanded GGOW Lemma 3.10, recorded as MS24 Proposition 2.10 and checked in [GGOW20-U003](../GGOW20/Yin_U003.md#ggow20-u003), gives ds(tilde eta_delta)<=6delta for the corresponding normalized map.
With tilde S_delta and its hermitization H_delta,

\[
\Delta(S)=d_\delta^{1/(2m)}\Delta(H_\delta)
\le\operatorname{cap}(\eta)^{1/(2m)}
      e^{\delta/(2m)}\Delta(H_\delta).
\]

The identity ds(tilde eta_delta^h)=2ds(tilde eta_delta), with the unnormalized traces, implies ||tilde eta_delta^h(I)-I||->0.
U002 gives convergence of H_delta to a standard semicircular s in all scalar moments and a finite uniform norm bound.

The printed equation (3.7) applies Proposition 2.4 directly to the signed selfadjoint H_delta.
To fit its positive-operator hypotheses, apply it instead to H_delta^2 and s^2.
Moment convergence and boundedness survive squaring, so

\[
e^{-1}=\Delta(s^2)\ge\limsup_{\delta\downarrow0}\Delta(H_\delta^2),
\qquad
\limsup_{\delta\downarrow0}\Delta(H_\delta)\le e^{-1/2}.
\]

Take the limsup in the preceding fixed-left-hand-side inequality to get the desired upper bound.
Both directions are now proved with identical normalizations.

The dependency recheck also supplies an independent short proof of the needed near-minimizer implication in [the scaling supplement](Yin_U006.md#ms24-scaling-dependency-review), using capacity duality and the scalar function x-1-log x.
Thus this use does not rely on GGOW20's numerical precision, quantitative continuity theorem, invariant-degree estimates, or integral-capacity lower bound.
The [complete dependency map](../../../ledger/Yin_L_F0003_v1.md#ms24-dependency-chain) separates the formula from the additional algebraic and arithmetic inputs to the integer-capacity theorem.

### Checks and Scope

For n=1 and invertible a, cap(b->aba*)=|det a|^2, and the formula becomes Delta(a tensor s)=|det a|^(1/m)e^(-1/2), as multiplicativity requires.
A singular a gives zero on both sides.
For m=1 and complex a_i, cap(eta)=sum_i|a_i|^2, so the same formula includes nonselfadjoint scalar semicircular linear combinations.
The proof does not identify their full distribution with a real semicircle; it uses the hermitization after normalization.

The formula settles positivity of a logarithmic integral.
It makes no claim that S^(-1) lies in M_m(M), nor that it belongs to L2.
The standard scalar s already has Delta(s)>0 and an unbounded inverse.
