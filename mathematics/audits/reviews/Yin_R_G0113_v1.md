---
author: Yin
---

# Retained project review: Atomless critical dual measures and subcritical integrability barriers

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0244_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="critical-dual-regularity-complete-independent-review"></a>

### Complete noncontributor independent review

Review date: 2026-10-09T23:20.
Human record author: Yin.
This is a separately organized whole-proof review by the arithmetic/resultant research agent of the complete author body frozen at 2026-10-09T23:16: the reuse section, Sections1--6, equations(1)--(18), the actual reciprocal control and all continuation boundaries.
The reviewer supplied none of these new derivations.
Shared coordination messages supplied the proposed conclusions and the author's explicit one-sided interpretation of the Lp criterion; this was not a blind review.
The reviewer had previously reviewed the upstream L236 and L240 arguments and authored other arithmetic material.
Those earlier roles are disclosed rather than called new independent verification of every upstream theorem.
The present complete proof, its actual dependencies and its new applications were read and checked directly.

The full author body remains the original byte prefix.
This review is appended by original bytes plus separately encoded review bytes; no author proof, source file, program, fixed ledger or strategy is changed.
No J or computational certificate is a premise.
The exact rational comparison in Section4 was checked as arithmetic in the written argument, not reported as a newly run numerical experiment.

#### Actual-law and source interfaces

The reviewer read L240's actual products W_n and V_n, both Abel density definitions, their Fourier coefficients on the whole order, the two measure-equation orientations, the all-order critical weak limits, the nontorsion recurrence/singularity dichotomy, the bounded-convolution criterion and the reciprocal quadratic control.
L236's original distinguished-visit identity and its separate zero correction were checked at their actual summable and possibly infinite critical scopes.
L228's complete real-coordinate collision lower bound was checked as the source of h<=m, with the input-dependent prefactor and neutral polynomial loss retained.
The sparse-position comparison in L215 was checked in its actual binary endpoint convention; the more general expanding-conjugate argument needed here is proved in Section1 itself.
No degree-uniform spacing or lower entropy statement is imported from the old particular control.

Wal18-U001 was inspected at its recorded compactness and toral-ergodicity acceptance scope.
This review reuses L240's already checked application, including its statement-level representation foundation and its selected-proof limits; it does not claim a new reading or audit of the original external foundational proofs.
Tao09's attribution remains terminology/standard Fourier background, with the required tent computation proved locally.
No external search result is used as a theorem.
The older L208 and L224 comparisons are not new logical premises, and no property of L239's normalized chain is assigned to the original law here.

#### Sections1--2: positive radius and every-center concentration

For a nontorsion unit, the actual minimal polynomial is separable and m>0, so at least one conjugate lambda has modulus greater than one.
Choosing k with |lambda|^k>2 makes the sums supported at positions0,k,2k,... distinct after conditioning on all remaining bits.
At a nonzero highest differing selected position, the triangle inequality gives a leading modulus strictly greater than the entire lower geometric sum, including for a nonreal lambda.
There are exactly ceil(n/k) selected positions for n>=1.
Each conditional endpoint atom is at most2^(-ceil(n/k)); averaging preserves that maximum-atom bound, and collision probability is at most the maximum endpoint atom.
The all-zero difference word gives p_n>=2^(-n).
Therefore(2) has the asserted direction and original probability normalization, and R>1 justifies choosing t0 in(1,R).
No uniform k is established.

In(3), the first weighted measure has density weighting at the target of S inverse, while the second pushes forward the already weighted measure.
For any Borel set B the relevant identities are respectively a_t(B)>=t integral_B w d(S^(-1)_*a_t) and b_t(SB)>=t integral_B w db_t.
These yield exactly(7) and(8).
The critical equations are valid also when eta_R>0: all source terms are nonnegative, and weak passage uses continuous w and the continuous toral automorphism.
They do not require a_t or b_t to be invariant under S.

Both required local inclusions follow from the stated row-sum matrix norms.
A representative of a point of B(0,r/L) is sent by M inverse into the real cube of radius r, proving B(0,r/L) is contained in S B(0,r); M itself proves S B(0,r/L) is contained in B(0,r).
These are local torus inclusions and do not assume a global lift.
On each small cube the first power-basis coordinate controls w>=cos^2(pi delta).
Iteration starts from mass at most one on B(0,delta).
With n=floor(log(delta/r)/log L), r<=delta L^(-n), and q^(-n)<=q(r/delta)^gamma.
This verifies the prefactor and exponent in the centered bound for every allowed r, uniformly over t in[t0,R].

The periodic one-dimensional tent is the exact indicator convolution divided by r.
Since r<1/2, the indicated support does not wrap incorrectly.
Its coefficients in(9) are nonnegative and absolutely summable, with the stated coefficient r at zero.
The product tent inherits these properties, is supported on the closed cube and is at least2^(-d) on the half-radius closed cube.
Absolute convergence permits integration against the probability, and the real nonnegative Fourier coefficients make each translated cosine contribution no larger than its centered contribution.
Thus(10) is valid without translation invariance.
Using radius2r retains exactly the factor2^d and the allowed r<=delta/2 in(6).

The all-center estimate implies no atom at any point for every t in the indicated interval, and hence at criticality.
For a recurrent nontorsion input the upstream pure singularity and the new atomlessness together justify the term singular continuous.
Transient critical inputs retain their actual L1 densities.
Averaging the translated-cube bound proves the same bound for convolution with any probability.
This does not classify a critical convolution with infinite mean, and no conclusion about the relative sizes of its continuous singular and absolutely continuous parts is added.
All matrix, degree, t0 and input dependence of the constants remains explicit.

#### Section3: full expanding multiplicities and essential Lp obstruction

The actual integer toral matrix has the conjugates of alpha as its eigenvalues.
Separability makes it real-conjugate to the stated one-dimensional real and two-dimensional rotation-dilation blocks.
The block max norm, Q and K bound every power-basis coordinate.
The product of expanding block moduli with their real dimensions equals exp(m), counting each nonreal pair twice.
Unit norm makes the corresponding product for M inverse identical; it does not require reciprocal pairing of the individual conjugates.

For E_N^+, multiplication by M^j,0<=j<=N, preserves the bounds before reduction modulo the lattice.
Each expanding radius was shrunk by rho_b^(-N), while contracting and neutral blocks retain their fixed local radii.
Hence all relevant factors of W_N are at least kappa_epsilon.
The region itself lies in an injective cube of radius less than1/4, so its Haar measure equals its real volume.
Multiplying all block volumes gives exactly C epsilon^d exp(-Nm), with C positive and independent of N but allowed to depend on the input and degree.
The same calculation for inverse blocks supplies the V_N factors at indices-1,...,-N.
Neutral directions cost fixed local volume in this argument and have not been silently discarded.

A single nonnegative term of the actual L1 Abel series gives the stated lower bound for its density on each region, almost everywhere.
Raising to a finite p and integrating yields(14) for every N; no disjointness of different regions is required.
If p log t>m, epsilon can be fixed small enough that p log(t kappa_epsilon)-m>0, and those lower bounds tend to infinity.
Separately, t kappa_epsilon>1 makes the values diverge on sets of positive measure, which proves essential unboundedness rather than a statement only about the exceptional point zero.
These arguments apply to both f_t and g_t in precisely their genuine density ranges.

The conclusion is deliberately one-sided: no assertion of membership at p log t<=m, optimality of the threshold, or classification of equality is supported.
The reuse phrase 'sharp-direction' is read only with that explicit scope, not as a sharp necessary-and-sufficient threshold.
Since log t<h<=m, the finite-p criterion does not contradict L1 normalization.
At transient criticality finite U(R) permits the same proof; at recurrence it cannot be used to create a Haar density by dividing a divergent series by infinity.
Formula(15) has the correct nonempty-interval condition ph>m and does not infer h=m for Salem inputs.

#### Sections4--5: actual control and full occupation coefficient bound

For alpha=2+sqrt3 the retained actual zero core is{0}.
Its all-zero words give p_n=2^(-n), F(t)=t/2, R=2, and its full product coefficient is delta_0 for every allowed t, hence its convolution is Haar.
The fixed total measure is log(2+sqrt3).
At t=31/16, U(t)=32 and t<2.
The exact comparison t^2-2=449/256>sqrt3 follows from449^2=201601>196608=3*256^2.
Thus2 log t>m, and(11) really proves failure of L2 for both actual subcritical L1 factors.
This establishes the intended counterboundary to an L2-factor requirement, while retaining exact bounded convolution and the true reciprocal-image relationship.
Critical singular continuity follows from Section2 and L240.
The input has no neutral conjugates and has fixed positive measure; it supplies neither a Salem recurrence classification nor a near-one family.

For the Fourier box, r=1/(4N) gives |pi j r|<=pi/4 for |j|<=N.
The stated elementary monotonicity of sin u/u on that interval yields the lower coefficient r(8/pi^2), with no missing square or Fourier normalization.
Taking d products and retaining only the nonnegative Fourier summands in the desired box is legitimate because the full tent expansion is absolutely summable and every probability coefficient has absolute value at most one.
Applying the centered cube bound and dividing by r^d(8/pi^2)^d gives exactly(18), including(4N)^(d-gamma), delta^(-gamma), and the input-dependent constant.
The box is in the actual integer character coordinates, distinct from the torus cube used for the mass estimate.

The product satisfies0<=A_t(x)B_t(x)<=min(A_t(x),B_t(x)) on the entire order.
The same finite-box bound therefore applies to sigma_t with its correct zero value and full support.
L236 identifies sigma_t as the corrected occupation below criticality; when F(R)=1, sigma_R is the unnormalized critical excursion occupation with mass one at zero, including infinite total mean.
No infinite sum is declared finite from the sub-volume estimate, and no nonexistent stationary probability is normalized in the infinite-mean case.

#### Complete finding and limits

No mathematical defect was found in the complete frozen argument.
All new conclusions are supported in their stated input-dependent original-law scope, and the complete proof is suitable for the coordinator's fixed retention after this review.
The result proves quantitative atomlessness, a one-sided actual Mahler-scale Lp obstruction, the exact non-L2/Haar control and the whole-order coefficient-box bound.
It does not give a degree-independent concentration exponent, an upper Lp estimate, a joint convolution estimate sufficient for infinite Salem finite mean, a return classification, or an unrestricted positive Mahler gap.
Existing G0001 routes remain open.
This finding is a full separate noncontributor proof review; it is not a fixed promotion, source-proof re-audit, new program execution, or Task completion.
