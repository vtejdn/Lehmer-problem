---
author: Yin
---

# Retained project review: Shannon constraints and near-one stationary quantile escape

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0216_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="stationary-quantile-complete-independent-review"></a>

### Complete separate noncontributor review

At 2026-10-09T20:50 the assigned resultant_research AI for Yin completed a separately organized full review of the frozen D83 author proof, all Sections 1--5, equations (1)--(23), dependency interfaces and final scope.
The coordinating AI authored every new deduction.
This reviewer contributed none of the repeated-block, Shannon, ball-count or quantile argument.
The author's earlier short direction summary and the later assignment were available, together with shared G0001 context; they were not treated as verification or a prior review conclusion.
The reviewer had separately reviewed L201 and L212 and earlier return-law dependencies, whose fixed scopes are reused rather than claimed as independent discoveries here.
The complete D83 argument was checked directly.
This is a full noncontributor AI review, not a blind, human or formal audit.
No mathematical defect or required correction was found.
The entire frozen author byte prefix was preserved when this finding was appended.

**Actual operator, adjoint and repeated smoothing.**
The actual monic integral power basis identifies O/qO with d copies of Z/qZ, including composite q and nonfield quotients.
Because alpha is a unit, multiplication by alpha^d permutes that quotient.
Under the convention (Tf)(x)=E_x f(X_d), the d independent chronological noise digits give exactly T=U C_q^(tensor d), with U evaluating at alpha^d x.
The cyclic convolution is selfadjoint, so the adjoint is C_q^(tensor d)U^(-1).
Both operators preserve positivity, constants and normalized uniform mean; the proof keeps the intervening permutation in each block rather than replacing all later noise by a single product law.

The reviewer read L211's exact finite cyclic contraction and tensorization at #cyclic-noise-tensor-contraction and checked that its p_q and normalized Lp conventions are the ones used here.
Norm preservation of U and U^(-1) transfers the contraction to both T and T*.
The interpolation equation gives theta_q=2(p_q-1)/p_q, which is strictly between zero and one.
A mean-one density has L1 norm one, so each application raises its previous L2 norm to at most this theta_q power.
All intermediate functions meet those hypotheses.
Starting from M times a point indicator therefore gives M^(theta_q^k/2), with exponent theta_q^k rather than k theta_q.

For the pointwise bound, the row density M T^k(x,z) is (T*)^k of the density at x and the column density M T^k(z,y) is T^k of the density at y.
Their normalized pairing is M T^(2k)(x,y); dividing the Cauchy--Schwarz upper bound M^(theta_q^k) by M proves (4) with the correct factor and orientation.
This does not assume reversibility.
The identity 1-theta_q=epsilon_q/p_q, p_q<2, and L211's delta_q>=4/q^2 give (5).
All estimates include q=2, where actual uniformization provides an even stronger fact but is not needed.
Their chronological observation time is exactly 2kd.

**Stationary path information and Shannon entropy.**
The comparison process starts from the same actual stationary pi and uses the full original independent digit law.
Each finite-step row likelihood has uniformly bounded expected absolute value, so the finite path relative entropy is exactly 2kd I even when H(pi) or neutral moments are infinite.
Reducing both endpoints modulo qO gives the reference law nu T^(2k), because original quotient transitions depend only on the starting residue.
The Q projection need not be Markov.
Full stationarity supplies both J marginals nu, and data processing proves (6).

Every J-supported endpoint pair has positive original transition probability.
On that support the relative-entropy expansion in (7) subtracts only a finite conditional entropy, not full-state Shannon entropies.
The pointwise transition bound gives the log M term, and H_J(Y|X)<=H(nu) gives the stated direction.
Since log M=d log q, (8) and (9) follow with every factor d, k and two retained.
This is a Shannon deficit bound, not an inference from a Renyi deficit.

For a residue image of uniform mass b and stationary mass v, binary relative entropy is at least v log(1/b)-H_binary(v).
Its omitted complement term is nonnegative.
With v>=pi(A), b<=N_A/M and N_A<M, this implies (10) without any premise v>=b.
The empty-set and real-upper-bound conventions are legitimate.
The image of the single state zero has one element even if other actual states share its residue; its residue mass is at least pi(0).
Rearranging the resulting inequality gives (11) exactly.
Taking the infimum over L212's same prescribed-mass admissible class preserves the bound whether or not that infimum is attained.
It adds a necessary lower bound and does not replace the exact frontier or assert sharpness.

**Actual Euclidean counting and the finite probability bound.**
The Salem restriction is introduced precisely at Section 3; Sections 1--2 remain all-unit statements.
The set counted in (13) consists of actual returning states satisfying the necessary expanding and stable strips.
Two distinct order elements in the same product cell have real differences strictly below one and all complex differences strictly below one in modulus.
Their difference is a nonzero algebraic integer, so its nonzero integer norm contradicts that product bound.
This argument needs neither a maximal order nor a covolume or discriminant estimate.

The neutral cells live in 2s real dimensions, each has volume 2^(-s) and diameter sqrt(s).
Their disjoint union, restricted to cells meeting the radius-R ball, lies in the radius-(R+sqrt(s)) ball.
The exact even-dimensional ball volume gives (2 pi_number)^s(R+sqrt(s))^(2s)/s!.
The elementary factorial inequality in the text gives the constant C=sqrt(2 pi_number exp(1)) and the factor 1+R/sqrt(s).
The two real-strip cell counts multiply this by A_real, proving (13)--(14).
In particular replacing the ball by a cube would lose precisely the dimension normalization used later.
The residue image has cardinality at most this actual count.
When the displayed denominator is positive, (10) therefore gives (15), without any second-moment assumption, full-strip sufficiency or finite-support premise.

**All varying-input and integer-parameter costs.**
For fixed A>1/2, b=(A+1/2)/2 satisfies 1/2<b<A.
As L tends to infinity, both m^(-1/2)L^(-b) and m^(-1/2)L^(-A) diverge, so the stated floor inequalities and q>=2 eventually hold with a threshold depending only on A.
The ceiling defining k is at least q^2(2+log q)log L and at most that quantity plus one.
Equation (5) then gives theta_q^k<=L^(-2), while log q<=L/2 and I<=2m give exactly the two terms in (18), including the ceiling cost 4m.
The leading term L^(1-2b)log L tends to zero because b>1/2.

For 0<m<=1, B<=1/m and S=B+1 yield A_real<=24/m^2.
The nonzero integer P(1) has absolute value (BS)^(-1) times the full neutral product, so BS<=4^s.
The elementary exp(m)-1<=exp(1)m gives BS>=exp(-2)m^(-2).
Hence d=2s+2 obeys both inequalities in (20).
This uses the actual Salem degree and needs no house theorem.
Dividing log A_real by that degree gives the stated absolute C_0 for L>=2.

The floor contributes at most a factor two loss in q; the inequality 1+x<=2x contributes another factor two.
These are exactly the 4C in (21).
The difference between d and d-2 leaves the nonnegative term 2log(C(1+x)), so dropping it has the claimed lower-bound direction.
Thus the denominator divided by d is at least G_A(L), which is eventually positive because A-b>0.
Also (log2)/d<=(log2)^2/L.
This proves the fully explicit (22).
Finally 2b-1=A-1/2 and G_A(L) has order log L, so division of the leading cost term gives L^(-(A-1/2)); all remaining terms have the order stated in (23).
No uncharged interchange of input, q, k and d limits is used.

**Complete conclusion, reuse and boundaries.**
The uniform probability limit applies to every admissible stationary law with I<=2m at every actual Salem input in the stated small-m range, if such inputs exist.
It therefore yields the claimed fixed-positive-quantile consequence.
It allows infinite support and infinite variance and is not obtained from L211's lower second moment.
The logarithmic loss and fixed A>1/2 are retained; the proof does not extend to A=1/2 or give a constant-times-sqrt(s/m) quantile bound.

The reviewer checked L201's finite actual Perron approximation interface: for each positive m, finite admissible laws can approach h_2<=m closely enough to satisfy I<=2m.
L212's feasibility and exact prescribed-mass frontier are unchanged and used only to identify the common competitor class and the additional necessary constraint.
L211's elementary contraction, original-law path normalization, necessary strip and P(1) interfaces were checked at their actual scopes, including its explicit distinction between support, moment and concentration.
No new external theorem, source acquisition, numerical calculation, J or material fingerprint was introduced.
The classical interpolation and entropy mechanisms are identified as such; no historical novelty claim or fresh source-proof audit is made.

The complete chain supports the actual repeated-block transition bound, all-modulus Shannon and subset constraints, Euclidean state count and input-uniform logarithmic-loss probability escape in (16)--(23).
It proves no conflicting upper quantile, critical attainment classification, full-strip equality or unrestricted reciprocal-unit gap.
Fixed adoption remains the coordinator's separate action.
