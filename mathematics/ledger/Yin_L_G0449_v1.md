---
author: Yin
---
# Original coefficient lattices: the reciprocal Mahler plateau, thin shells and critical-value slices

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This bounded 2026-11-05 comparison concerns the unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Its question is whether exact coefficient-space volumes, root Jacobians or simultaneous coefficient integrality exclude every original integer polynomial with sufficiently small positive total logarithmic Mahler measure.
The authoring agent coefficient_lattice performed the source-applicability checks and direct calculations for human author Yin; this is author-checked exploration, without independent review, a new Claim assessment or a uniform gap.
The comparison finds no covering exclusion mechanism in the inspected material.
It retains a precise distinction between the continuous volume information and the arithmetic information still missing.
The final critical-value question is a bounded diagnostic, with no established independent accessibility or selected strategy.

[C231's all-positive-power existence descent](../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) permits testing the conjecture on monic irreducible reciprocal nontorsion unit endpoints whose degrees are preserved by every positive power.
This is an existence reduction at C231's selected SELF-review and nonreciprocal-source scope.
It does not make every trace field totally real or reduce all endpoints to Salem inputs.
The volume and Jacobian comparisons below retain every real or complex trace root.
The later ordered critical-value slice concerns the all-real trace plateau and specified regular neighboring slices only.

<a id="source-and-local-comparison"></a>
## Source and local comparison

The existing bibliography key is Sin07: Christopher D. Sinclair, *The range of multiplicative functions on C[x], R[x] and Z[x]*, arXiv:math/0509591v2, 13 July 2007.
The inspected original is the existing [local v2 PDF](../literature/pdf/Sin07--arxiv-v2.pdf), whose title/version strip was read, with the [versioned public source](https://arxiv.org/abs/math/0509591v2) retained as its external locator.
The original definitions and statements read here are Section 1.3, pages 4--6; Theorem 1.8 and equation (1.7), page 7; equation (1.8) and the distribution discussion, page 8; and Theorem 1.11 with its stated degree-dependent error and argument, page 9.
The relevant root-Jacobian passage in Section 6.1 and Lemma 7.2's statement were also text-inspected.
The complete Pfaffian evaluation and the original proof of Lemma 7.2 were not independently audited.
The moment formula below is used at original statement, normalization and applicability scope; the subsequent inversion and bounds are the present author's direct calculations.

The existing [Sin07-U001](../audits/literature/Sin07/Yin_U001.md#sin07-fixed-degree-continuity) concerns fixed-degree continuity and does not inspect the volume formula.
Its historical access outcome is not rewritten; the present inspection used an actual available local v2 file.
[Smy08-U003's counting discussion](../audits/literature/Smy08/Yin_U003.md#smy08-bounded-measure-count) already distinguishes fixed-degree large-bound counting from the unbounded-degree small-measure target and records unsafe counting conventions.
Chern--Vaaler is a source lead through that unit and Sin07, not a newly audited original theorem in this comparison.
Sin07 Theorem 1.11 itself suffices to verify the relevant large-T limitation: T tends to infinity and the error constant depends on the fixed degree.

The bounded local search used coefficient lattice, Mahler volume/star body, Chern--Vaaler, Sinclair, trace, interlacing and critical-value terms.
[C243](../claims/Yin_C_G0243_v1.md#statement) supplies the original integral trace construction and discriminant identity.
[L369's Salem calculation](Yin_L_G0369_v1.md#salem-interlacing-critical-orders) concerns critical orders of a particular oscillatory phase, with input-dependent constants.
[L442's actual trace positivity comparison](Yin_L_G0442_v1.md#actual-trace-positivity-interlacing-screen) concerns an actual positive quotient, its interlacer and unpaid normalization, rather than lattice counting in a constant-coefficient slice.
Those passages were read for this comparison; no absence of other literature or mathematical novelty is asserted.
The present object is distinct from the [random-resultant and companion-minor comparisons](Yin_L_G0446_v3.md#scope-and-strategic-assessment), whose arithmetic gains and losses are not rederived here.

<a id="original-trace-lattice"></a>
## The original trace lattice and the positive-volume platform

For N>=1 write the original degree-2N reciprocal polynomial as

\[
 P(z)=z^NQ(z+z^{-1}),\qquad
 Q(t)=t^N+b_1t^{N-1}+\cdots+b_N.
 \tag{1}
\]

C243 gives Q in Z[t], irreducible of degree N when P is the original irreducible nontorsion input, and does not require its roots to be real.
More generally (1) is a bijection between monic real Q and monic reciprocal real P with constant coefficient one.
Comparing the highest remaining Laurent powers shows that the affine transformation from b to the N independent nonleading reciprocal coefficients is triangular with diagonal one and integer entries.
Its inverse is obtained by successive subtraction of powers of z+z^(-1), also with integer coefficients.
Thus it preserves both the integer lattice and Lebesgue volume in these independent coefficient coordinates.

For w in C let rho(w) be the larger modulus of the two roots of z^2-wz+1.
Their product is one, so rho(w)>=1.
If w_1,...,w_N are all roots of Q, with multiplicity, then

\[
 M(P)=\prod_{j=1}^N\rho(w_j),\qquad
 m(P)=\sum_{j=1}^N\log\rho(w_j).
 \tag{2}
\]

This is Sin07's reciprocal measure rho(Q), not the ordinary Mahler measure M(Q) of the trace polynomial.
No division by N or 2N is made.
Define the compact monic coefficient body

\[
 B_N(\varepsilon)=\{b\in\mathbb R^N:m(z^NQ(z+z^{-1}))\le\varepsilon\},
 \qquad \varepsilon\ge0.
 \tag{3}
\]

Compactness follows, for example, because each rho(w_j)<=exp(epsilon), hence |w_j|<=2cosh(epsilon), and the elementary symmetric coefficients are bounded.
One has rho(w)=1 exactly when w belongs to [-2,2].
Consequently B_N(0) consists exactly of the monic real polynomials with all roots in that interval.
This set has nonempty interior: a polynomial with distinct roots strictly inside the interval retains these properties under sufficiently small real coefficient perturbations, by simple-root continuity and conjugation.
The monic integer polynomial C_N(t)=2T_N(t/2), with C_0=2, C_1=t and C_(n+1)=tC_n-C_(n-1), gives such a point for every N>=1.
Its reciprocal image is z^(2N)+1.
Thus a cyclotomic integer point can be interior to the zero-measure plateau in the correct reciprocal lattice slice, rather than lying on a lower-dimensional coefficient boundary.
Kronecker's theorem still identifies every integer point of B_N(0) with a product of cyclotomic factors after (1); this does not make the real plateau discrete.

<a id="sinclair-moment-and-laplace-inversion"></a>
## Exact moment normalization and the complete Laplace expansion

Let f_N(T) be the Lebesgue volume of the monic real coefficient set with reciprocal measure at most T, and put g_N(epsilon)=f_N(exp(epsilon)).
The source's real moment is

\[
 F_N(s)=\int_{\mathbb R^N}\rho(Q)^{-s}\,db,
 \qquad \operatorname{Re}s>N.
 \tag{4}
\]

It is not the complex moment, whose source exponent is -2s and whose ambient real dimension is 2N.
Since the reciprocal monic measure is at least one, f_N(T)=0 for T<1.
The source's integration-by-parts identity gives

\[
 \frac{F_N(s)}s
  =\int_1^\infty T^{-s}f_N(T)\,\frac{dT}{T}
  =\int_0^\infty e^{-s\varepsilon}g_N(\varepsilon)\,d\varepsilon.
 \tag{5}
\]

In the Stieltjes version of (5), the jump at T=1 is retained; it is the plateau volume, not an omitted boundary term.
Theorem 1.8 states

\[
 \begin{split}
 r&=\lceil N/2\rceil,\qquad a_j=N-2j\quad(0\le j<r),\\
 F_N(s)&=v_N\prod_{j=0}^{r-1}\frac{s^2}{s^2-a_j^2},\\
 v_N&=\frac{2^N}{N!}
       \prod_{n=1}^N\left(\frac{2n}{2n-1}\right)^{N+1-n}.
 \end{split}
 \tag{6}
\]

As s tends to positive infinity, the integrand in (4) decreases to the indicator of B_N(0); domination by one fixed convergent moment justifies the limit.
Thus g_N(0)=v_N, in agreement with the source's equation (1.8).

Let h_k be the complete homogeneous polynomial of degree k in a_0^2,...,a_(r-1)^2, with h_0=1.
For real s>N the geometric expansion of (6) gives

\[
 \frac{F_N(s)}s
   =v_N\sum_{k\ge0}\frac{h_k}{s^{2k+1}}.
 \tag{7}
\]

The present direct inversion is

\[
 g_N(\varepsilon)
    =v_N\sum_{k\ge0}h_k\frac{\varepsilon^{2k}}{(2k)!}.
 \tag{8}
\]

Indeed h_k<=binom(r+k-1,k)N^(2k), so the series converges absolutely on every bounded epsilon interval and has exponential order N with a possible polynomial factor.
For s>N, Tonelli and repeated integration by parts transform each term epsilon^(2k)/(2k)! into s^(-2k-1), giving exactly (7).
The coordinating agent checked the classical uniqueness statement in [DLMF Section 1.14(iii), Uniqueness](https://dlmf.nist.gov/1.14.iii) on 2026-11-05, at statement scope without reviewing its cited proof.
Apply that continuous-function statement to the integrals from zero of g_N and of the displayed series, whose Laplace transforms agree by one further division by s.
Their equality gives (8) almost everywhere; the coefficient distribution is right-continuous by continuity from above of the finite-volume nested bodies, so (8) holds at every epsilon>=0, including its previously checked value at zero.
Alternatively, partial fractions in (5)--(6) express the same function as a finite linear combination of cosh(a_j epsilon).
This establishes (8) with its actual fixed-N source input, rather than guessing a uniform thin-shell asymptotic.

The sum of the squared positive integers of the same parity as N is

\[
 A_N=\sum_{j=0}^{r-1}a_j^2=\frac{N(N+1)(N+2)}6.
 \tag{9}
\]

It follows that, for fixed N,

\[
 \operatorname{vol}(B_N(\varepsilon)\setminus B_N(0))
   =v_N\frac{N(N+1)(N+2)}{12}\varepsilon^2+O_N(\varepsilon^4).
 \tag{10}
\]

For an explicit joint-parameter bound, h_k<=A_N^k because every monomial in h_k occurs in A_N^k with coefficient at least one.
Hence

\[
 0\le\frac{g_N(\varepsilon)}{v_N}-1-\frac{A_N\varepsilon^2}{2}
   \le\cosh(\sqrt{A_N}\varepsilon)-1-\frac{A_N\varepsilon^2}{2}.
 \tag{11}
\]

The relative smallness of the last bound requires control of A_N epsilon^2; epsilon tending to zero alone gives none when N grows.
For N=1 and N=2, (8) gives respectively g_1(epsilon)=4cosh(epsilon) and g_2(epsilon)=(32/3)cosh(2epsilon), checking the coefficient and the real-moment normalization.
These are exact substitutions, not numerical experiments.

<a id="uniform-volume-and-lattice-obstruction"></a>
## A uniform volume bound and its exact lattice limitation

For s>N, the definition (4) directly implies g_N(epsilon)<=exp(s epsilon)F_N(s), because the integrand is at least exp(-s epsilon) on B_N(epsilon).
Taking s=2N in (6) gives the bound valid for every N>=1 and epsilon>=0,

\[
 g_N(\varepsilon)
   \le v_Ne^{2N\varepsilon}(4/3)^r.
 \tag{12}
\]

The size of v_N is also explicit.
Put ell_n=log(2n/(2n-1)).
The product identity product_(n=1..N)2n/(2n-1)=4^N/binom(2N,N) and Stirling's formula give sum ell_n=(1/2)log N+O(1).
For this standard input the coordinating agent checked [DLMF equation 5.11.1](https://dlmf.nist.gov/5.11.E1) on 2026-11-05; its positive-real asymptotic applies to the factorials here, without an original-proof audit.
Also n ell_n=1/2+O(1/n), so sum n ell_n=N/2+O(log N).
Inserting these estimates and log N!=N log N-N+O(log N) in (6) yields

\[
 \log v_N=-\tfrac12N\log N+O(N).
 \tag{13}
\]

Consequently, for every fixed epsilon_0>=0,

\[
 \sup_{0\le\varepsilon\le\varepsilon_0}
       \operatorname{vol}B_N(\varepsilon)\longrightarrow0.
 \tag{14}
\]

Nevertheless each B_N(0) already contains the integer point C_N.
Thus even an entire body of volume below one need not be integer-point-free in this exact coefficient lattice.
Subtracting the plateau volume does not by itself repair the inference.
For any fixed monic reciprocal integer P_0 of degree 2n_0 and positive logarithmic measure mu=m(P_0), the polynomials P_0(z)(z^2+1)^k have the same positive logarithmic measure and lie in the degree-2(n_0+k) positive shell whenever epsilon>=mu.
Their trace polynomials are Q_0(t)t^k, so these are actual shell lattice points while the bound (14) tends to zero.
This is a calibration of the proposed volume inference at any fixed shell already containing P_0, not a sequence with measure tending to zero.
The products are generally reducible and are not asserted to be C231's all-power endpoints.
Removing them requires an arithmetic argument; real volume does not enforce irreducibility or power stability.

Sin07 Theorem 1.11 counts reciprocal integer polynomials at a large multiplicative bound T, with fixed degree and a degree-dependent error.
Here T=exp(epsilon) tends toward one while the original degree may diverge.
Neither that theorem nor (12) bounds the lattice discrepancy in this regime below a single point.
A hypothetical uniformly small shell discrepancy would be a new arithmetic theorem, not a consequence of the exact volume formula.

<a id="jacobian-and-one-point-mass"></a>
## Jacobian information and the required one-point probability scale

In a root chart with L real roots and M conjugate pairs, L+2M=N, Sin07 gives the real coefficient-change Jacobian 2^M|Delta|, where Delta is the Vandermonde of all N roots.
This statement concerns the density for Lebesgue change of variables; it is not a description of the image of the integer lattice in root coordinates.
For a squarefree integer Q, |Delta|^2=|disc Q|>=1.
On the original reciprocal input C243 gives exactly

\[
 \operatorname{disc}P=(\operatorname{disc}Q)^2Q(2)Q(-2).
 \tag{15}
\]

The scalar arithmetic obtainable by simply adjoining this Jacobian is therefore already present in the actual trace discriminant and endpoint evaluations.
A determinant lower bound controls neither the smallest singular value nor the orientation and phase of a lattice relative to a thin region.
Even a determinant-one integer shear can have arbitrarily small smallest singular value.
There is no proved injection of a unit coefficient cell into the positive Mahler shell around an original lattice point.
The root Jacobian and real volume alone supply neither that cell nor a discrepancy estimate.

For completeness, arbitrary integer coefficients must remain in any proposed discrete probability comparison.
For the original monic reciprocal degree-2N polynomial with m(P)<=epsilon_0, elementary symmetric sums give

\[
 |a_k|\le e^{\varepsilon_0}\binom{2N}{k}\quad(1\le k\le N).
 \tag{16}
\]

Each root-product summand is bounded by M(P), so (16) includes arbitrary allowed original coefficients, rather than a height-one restriction.
The rectangular box of all independent integer coefficient choices has cardinality

\[
 K_N=\prod_{k=1}^N
      \left(2\left\lfloor e^{\varepsilon_0}\binom{2N}{k}\right\rfloor+1\right),
 \qquad \log K_N=\Theta_{\varepsilon_0}(N^2).
 \tag{17}
\]

For the upper bound use binom(2N,k)<=4^N in every factor.
For the lower bound take N/2<=k<=N: there are a positive proportion of N such factors and their binomial coefficients are exp(cN) for an absolute c>0, by Stirling or elementary binomial bounds.
Thus a uniform law on this complete box assigns one integer point mass K_N^(-1).
If E is the set of positive-small-measure original candidates, the identity Pr(E)=#E/K_N implies that a probability upper bound proves emptiness only when it is strictly less than K_N^(-1).
A merely small probability, including generic exp(-cN) or exp(-cN log N) upper estimates, does not meet this threshold.
The continuous root ensembles obtained from the Jacobian assign individual coefficient lattice points mass zero and have no direct one-point transfer.
Restriction to actual irreducible power-stable integer points needs its own count or minimum-atom control.

<a id="constant-coefficient-critical-value-slice"></a>
## The exact constant-coefficient slice and its restricted domain

Fix a monic integer polynomial q_0 of degree N with constant coefficient zero and put Q_c=q_0+c for c in R.
The integer original coefficients are exactly c in Z on this affine line.
Assume for this regular chart that q_0' has N-1 distinct real roots xi_1<...<xi_(N-1), all in (-2,2).
Put t_0=-2, t_i=xi_i for 1<=i<N, t_N=2 and sigma_i=(-1)^(N-i).
Then Q_c has all N roots in [-2,2], counting multiplicity, if and only if

\[
 \sigma_i\big(q_0(t_i)+c\big)\ge0\quad(0\le i\le N).
 \tag{18}
\]

Necessity follows from the alternating signs of a monic real-rooted polynomial at its endpoints and interlacing extrema.
For sufficiency, consecutive endpoints/extrema with opposite weak signs give a root in each monotonicity interval; an extremum with value zero is a double root, since the derivative root is simple, and supplies the adjacent two multiplicities.
The total multiplicity is N, so no further roots remain outside the interval.
Equivalently, the admissible constants form the possibly empty interval

\[
 I(q_0)=[L,U],\qquad
 L=\max_{\sigma_i=1}\{-q_0(t_i)\},\quad
 U=\min_{\sigma_i=-1}\{-q_0(t_i)\}.
 \tag{19}
\]

The directly inspectable object is the simultaneous tuple of the ordered critical points and values, q_0(2), q_0(-2), q_0'(2) and q_0'(-2), together with the actual integer c.
The endpoint values and endpoint derivatives are integers.
The critical values are generally algebraic nonintegers; their possible collision constants are zeros of the integer polynomial Res_t(q_0(t)+c,q_0'(t)).
For a fixed input, ordered real-root isolation and algebraic comparison can certify every inequality in (18), without replacing the critical values by their marginal sizes.
This describes a mathematical test, not an executed computation or a supplied uniform estimate.

The interval test is a description of the all-real trace plateau and regular slices meeting it.
Passing its first collision boundary can create a complex pair, but no reduction of arbitrary complex-trace original endpoints to these charts has been proved.
Even a genuine Salem trace can have its largest derivative root at or above 2, as the actual domain analysis in L369 allows; that input cannot silently be placed in the present chart.
Salem examples are necessary controls, not a covering reduction.

If an endpoint evaluation is the active boundary in (19), its c-threshold is an integer, so an exterior integer c lies at least one unit beyond that threshold.
This does not imply a uniform Mahler cost: the local root displacement also depends on the endpoint slope and the positions of all other roots.
For the genuine Salem calibration, write the trace roots as 2cosh(m), beta_2,...,beta_N, with every beta_j in (-2,2), and m=m(P)>0.
The exact original norm gives

\[
 1\le |Q(2)|
   =(2\cosh m-2)\prod_{j=2}^N(2-\beta_j).
 \tag{20}
\]

The trivial product bound is 4^(N-1), giving only a degree-dependent restriction.
Keeping Q'(2) or the Jacobian without a further simultaneous critical-value estimate does not eliminate that expense.
Critical-value boundaries also need the distance of the actual integer c from generally nonintegral algebraic thresholds, not merely the existence of a nonzero discriminant integer.

<a id="chebyshev-slice-calibration"></a>
## Chebyshev calibration and the remaining joint question

Take the integer monic C_N(t)=2T_N(t/2) from above and now let Q_c=C_N+c; c is an integer shift of its fixed integer constant coefficient.
Its interval (19) is exactly [-2,2], all interior critical values are +2 or -2, and C_N'(2)=N^2.
These facts follow directly from C_N(2cos theta)=2cos(N theta), including the endpoint derivative by its limit at theta=0.
Its original reciprocal polynomial is

\[
 P_c(z)=z^{2N}+cz^N+1.
 \tag{21}
\]

For |c|<=2 the two roots of y^2+cy+1 have modulus one, so m(P_c)=0.
For |c|>2 their moduli are r and r^(-1), with log r=arcosh(|c|/2).
Taking their N-th roots produces N exterior roots of modulus r^(1/N), so their complete total contribution is

\[
 m(P_c)=\operatorname{arcosh}(|c|/2).
 \tag{22}
\]

Thus the first exterior integer shift has cost arcosh(3/2), independent of N, despite the endpoint slope N^2.
Following only one exterior root would incorrectly retain a factor 1/N and lose the simultaneous root escape.
This favorable calibration does not supply a covering argument: P_c is a polynomial in z^N, and any irreducible member of full degree 2N with N>1 has a degree drop after the N-th power.
No all-power endpoint reduction to this family is claimed.

The unresolved joint question is whether, on actual admissible integer inputs, a very large endpoint slope or a nearly integral collision threshold can coexist with all the remaining critical-value inequalities permitting only a small total escape.
The tuple and inequalities (18)--(19) retain information beyond one endpoint norm, while using only (20) or a discriminant determinant returns to the old scalar income.
The Chebyshev example demonstrates the distinction, but does not furnish the missing bound for general integral critical-value configurations.
No theorem controlling that compatibility, no uniform extension beyond the stated real-trace charts and no independent accessibility reason was found in the bounded comparison.
Consequently this is a precise possible discriminating question, not an established strategy, a uniform lattice-avoidance result or a refutation sequence.

## Checks and limits

The author checked the original coefficient-lattice transformation, all-root measure convention, source real-versus-complex moment exponents, plateau atom, complete Laplace-series calculation, fixed-degree versus joint-parameter distinction, uniform bound, coefficient-box counting scale, slice signs and multiplicities, and the full Chebyshev root contribution.
The N=1 and N=2 substitutions and the explicit polynomial identity (21) are exact hand checks.
No numerical enumeration, theorem-proof audit of Sinclair's Pfaffian calculation, independent mathematical review or new C/R registration is asserted.
The useful conclusion is the precise failure of volume/Jacobian information alone to exclude original integer points and the stated limited critical-value diagnostic.
