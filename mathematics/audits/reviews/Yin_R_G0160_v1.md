---
author: Yin
---

# Retained project review: Complete original-bridge block minorization and paid annular lower tails

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0335_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="lower-fiber-complete-independent-review"></a>

### Complete separately organized noncontributor review

Completed2026-10-10T12:12 by the coordinating root AI for Yin.
I read and checked the ENTIRE25,161-byte author body frozen at20:08:58+08:00: the assigned scope, Sections1--6, Lemma1, Theorem2, every formula(1)--(17), all reuse boundaries, failed stronger implications, contributions and freeze.
The original author prefix is preserved in full.
Root assigned the broad lower-fiber question and received progress descriptions, but supplied no derivation of these results.
This is a nonblind, separately organized noncontributor AI review, not human or formal verification.
The reviewer has earlier author/review roles in retained G materials, including authorship of the reused L256 projection interface; those older results are consumed at their fixed scope rather than claimed newly independent here.

**Whole-proof finding.**
The complete argument passes without a requested mathematical correction.
It establishes actual finite-bridge lower estimates with their full original probabilities, and an exact signed arithmetic reformulation of the remaining diffusive-moment question.
It does not establish linear second-moment growth or infinite critical mean.
The exponential annular floor and unscaled superlinear exponential-moment divergence are compatible with finite mean and do not contradict the small-parameter scaled upper moments of L332.

#### Reused interfaces and the complete original coordinates

I checked the consumed original midpoint identity in [L293](../../ledger/Yin_L_G0293_v1.md#actual-original-midpoint-overlap), the reciprocal-image identity in [L240](../../ledger/Yin_L_G0240_v1.md), the exact all-core path constants and full annular count in [L309](../../ledger/Yin_L_G0309_v1.md#quartic-full-core-linear-return), and the moment/finite-mean implications of [L332](../../ledger/Yin_L_G0332_v1.md#diffusive-lower-moment-null-test).
L329's complete finite-mean convergence is reused for only its stated conditional consequence.
I also reread L256's original-law projection convention: it supplies an upper proxy, not a lower covariance result, and is not used to prove the present lower estimates.
No new external theorem or source acquisition is a premise.

The actual reciprocal quartic has two real conjugates and one genuinely two-dimensional neutral pair.
Its already proved core is the strict strip D with BOTH real coordinates retained.
Equation(2) follows exactly by multiplying the low-power half by minus beta^(-n) under the full endpoint-zero condition; the high-power half is then the chronological midpoint.
Evaluating at zeta preserves this equality.
There is no omission of the real endpoint constraints, no replacement neutral walk and no degree normalization.
Sign reversal preserves all digit probabilities and the return event, so the complete midpoint has mean zero.

#### Section2: center maximum, measure minorization and additive covariance

For every subset of coordinates, including an empty or gapped set, the original digit law is the difference of two independent fair-binary endpoint laws.
Cauchy--Schwarz gives m_A(x)<=m_A(0) without a sharp profile assumption.
Convolving I and its complement J and using the maximum of m_J gives p<=p_J.
The subevent U_I=0 inside U=0 has probability p_I p_J/p, which is at least p_I.
All denominators are strictly positive because the all-zero word occurs.

Conditioning on this subevent is exactly conditioning both independent coordinate families to return individually.
Their observable sums therefore have the stated independent conditional laws, and the complete conditional law dominates their convolution with coefficient q_I.
Replacing q_I by p_I preserves inequality for every measurable set because the convolution is nonnegative.
This is a submeasure statement, not independence of the whole returned word.
Symmetry follows separately on both blocks by sign reversal, including when one block is empty.

For several DISJOINT blocks, conditioning on the full vector of endpoints preserves independence of the internal word choices.
The additional total-return condition is already determined by those endpoints.
The covariance of the sum given them is therefore the sum of the block covariances.
The law of total covariance adds a positive semidefinite covariance-of-means term.
For each block its remaining average is a positive combination of positive semidefinite matrices; retaining only its endpoint-zero term and using the preceding q_I>=p_I proves(5).
One need not assert joint independence of the block endpoint-zero events.
Dropping the leftover block only discards another positive semidefinite term.

In a centered interval of length2m, the power shift beta^(n-m) is invertible and cancels exactly against the observable's beta^(-n), giving the length2m midpoint with no extra neutral rotation.
The gapped complement is retained through its actual returned law and probability.
Consequently both statements in(6) follow at all n>=m, including an empty complement.
The factor p_(2m) has not been silently removed.
Convolution alone supplies no radial stochastic ordering; the later sign pairing is needed.

#### Section3: all short words, exact constants and the local-block limit

At length five, monic division by the degree-four minimal polynomial leaves a constant quotient.
The ternary leading coefficient restricts that quotient to0,+1,-1, proving exhaustively that the returned words are0,+P,-P.
Their original probabilities are1/32,1/1024,1/1024, totaling17/512.
Division gives16/17 and1/34,1/34, exactly as in(7).

For the block starting at n-k, its low-half contribution is minus zeta^(-k) times the first k coefficients of P.
At k=1 it is -zeta^(-1).
At k=4 the polynomial equation makes that contribution1.
Both intervals are inside the length2n word whenever n>=4.
Conditional covariance of this three-point block law is w_k w_k^T/17.
Multiplying by its original return probability gives w_k w_k^T/512.
The two blocks overlap, so the proof correctly averages their separately valid inequalities and pays another factor1/2; it does not add them as if disjoint.

The eigenvalues of the sum of two unit-vector outer products are1 plus or minus the absolute value of their dot product.
That absolute dot product here is |Re zeta|=(sqrt13-1)/4.
The smaller eigenvalue is(5-sqrt13)/4, positive.
After dividing by1024 this gives the exact stated positive definite floor.
Taking the trace of the FIRST matrix bound yields1/512; this stronger trace value is not confused with twice the weaker scalar eigenvalue bound.
The zero-return assertion for n<=2 follows from degree, and the theorem makes no unsupported n=3 claim.

A ball of radius strictly less than1/2 has diameter strictly less than1.
The three translated block points have pairwise distances1,1,2, so such a ball contains at most one.
Its conditional block probability is at most16/17 for every translation.
The complete bridge mixture can lose at least q_I/17>=p_5/17=1/512 outside it.
This proves(10) for every center, with the strict radius and original subevent expense retained.

For the bounded-diameter limitation, a returned block wholly before the cut has zero neutral low-half observable because the endpoint polynomial also vanishes at zeta.
A block wholly after the cut contributes zero by definition of that observable.
Each contributing block therefore crosses the cut and is contained in the indicated at-most2L coordinate neighborhood.
Pairwise disjointness gives total cardinality at most2L and each cardinality at mostL.
Its neutral observable has norm at most its cardinality, since the original digits and neutral power factors have modulus at most one.
The covariance trace is at most that squared norm bound; multiplying by a return probability no greater than one gives the sum of squares in(11), at most2L^2.
Averaging such certificates cannot increase this upper bound on the CERTIFICATE.
It is correctly not asserted as an upper bound on the actual midpoint variance.

#### Section4: whole annulus, path reversal, all probabilities and cancellation

L309 supplies a legal zero continuation of length at most A_D rho+B_D for every state of the full strict core, including states near either real boundary; the boundary-entry and terminal costs are already in those constants.
The reciprocal involution J preserves the actual order, core and neutral norm.
At an edge x->beta x+eta, applying J in reverse gives the edge from J(beta x+eta) to Jx with digit -eta.
Thus reversing a Jx-to-zero word really produces a zero-to-x word of the same length and same product probability.
The proof needs no equality between two harmonic functions.

The consumed counting estimates apply to the actual order in all four embedding coordinates.
For r>=4, the lower count at lambda_ann r minus the upper count at r is at least (c0 lambda_ann^2-4 C_up)r^2.
The chosen lambda_ann makes this at least c0 lambda_ann^2 r^2/2.
The annulus is finite by lattice discreteness and the bounded embedding region, symmetric under sign, and excludes zero.
Therefore it has exactly half as many disjoint sign pairs as states.

Both incoming and outgoing selected paths have lengths at most m(r).
Padding the incoming path at its initial zero and the outgoing path at its final zero keeps the midpoint exactly x and makes each half length m(r).
Every original digit has probability at least1/4, so the entire padded word has probability at least4^(-2m(r)); its actual zero padding is charged, not assigned probability one.
Complete words with different midpoint states are distinct.
Defining the negative word by digitwise negation preserves length and probability.
The actual complete zero-to-zero paths ensure all intermediate states remain in the core.

Inserting such a word in the centered coordinate block gives midpoint contribution exactly x.
Keeping only these internal words and complement-endpoint zero gives the displayed lower event mass divided by the FULL p_(2n), with multiplicative p_J.
For any complementary neutral displacement y and a fixed sign pair, the parallelogram identity proves that at least one of y+x and y-x is strictly outside radius r.
Equal paired weights then yield at least one complete-word weight per pair, independently of y.
Averaging over the entire complementary law is therefore legitimate and does not presume concentration or independence of the two full midpoint halves.
The center maximum gives p_J/p_(2n)>=1 in the correct direction.
These steps establish(12), including n=m(r) and the empty complement, with the factor1/2 and every exponent unchanged.

The onset n>=ceil(A_D lambda_ann r+B_D) is explicit and linear in r with fixed positive constants.
Choosing the stated r_n makes m(r_n)<=n and r_n grows linearly.
On the event rho>r_n, the nonnegative exponential observable is at least exp(t r_n^gamma); combining with(12) and weakening4^(-2m) to4^(-2n) proves(13).
For every fixed t>0 and gamma>1, the positive term of order n^gamma dominates the paid negative linear term.
This reasoning gives a full-sequence divergence of UNSCALED superlinear exponential moments.
It does not lower-bound second moments on a linear scale: the same selected words can have exponentially small total weight.
In particular it supplies no contradiction to L332's limit for exp(lambda rho^2/n) with fixed lambda<2.

If finite critical mean is separately assumed, the full midpoint laws converge in total variation by L329.
Total variation controls each fixed tail event, even though that event is infinite, so(12) passes to the stationary probability with r fixed.
No radius/time interchange and no bound on the unknown mean are introduced.

#### Section5: exact fibers and signed trace-field diagnostic

The integer c_n counts the original word weights with numerator2 for each zero digit and1 for each nonzero digit.
The complete chronological midpoint factorization is c_n(x)c_n(beta^n x)/c_(2n)(0), using sign symmetry for the latter half.
The map beta^(n-1)iota reverses the original n-digit endpoint law.
Applied to beta^n x it gives beta^(-1)iota(x)=Jx, proving(14) with a fixed involution and all multiplicities.
Only finitely many states appear at each n, and all nonzero products correspond to actual complete bridges.

For the unique four-term power-basis representation of x, multiplication by its reciprocal expansion gives s_0+s_1 u+s_2(u^2-2)+s_3(u^3-3u).
Both roots u,u_plus satisfy u^2=u+3 and u^3=4u+3.
Substitution gives exactly A=s_0+s_2+3s_3 and Bq=s_1+s_2+s_3 at both trace-field embeddings.
The neutral product is rho^2, while the real product is x_+x_- and may be negative.
This sign distinction is essential and is correctly retained.

A_n,B_n are complete signed integer sums; C_n is a positive integer.
Averaging the actual strict bounds |x_+|<B and |x_-|<S over their finite probability gives |T_n|<BS.
Subtracting the two trace embeddings yields (u-u_plus)B_n/C_n=-sqrt13 B_n/C_n, proving both assertions in(16).
Dividing by n leaves a uniformly bounded error tending to zero, so limsup of the nonnegative moment equals minus sqrt13 times the liminf of the signed ratio, as in(17).
The prior moment upper bound ensures finite limiting ranges; no numerical values of these integer sums are used.

A negative ratio bounded away from zero along infinitely many n is thus equivalent to a positive linear second-moment limsup, with an appropriately reduced positive constant if needed.
L332's finite-mean necessity and the already proved recurrence give the stated infinite-mean implication.
Conversely finite mean forces the ratio to zero by the same bounded-error identity.
This exact discriminator does not prove its own negative-sign/asymptotic premise.

#### Complete outcome and retained limitations

All sections, their original-law conventions, quantified domains and costs pass.
No program or new J was needed; no retained native data were rerun or upgraded.
The reviewer found no omitted state class, missing original probability, false covariance addition or unjustified moment passage.
The responsible author distinguishes the new finite-bridge lower envelope from L309's earlier critical-occupation floor, and does not recredit that earlier theorem.

The remaining substantial gate is a lower estimate for the COMPLETE growing-support fibers strong enough to give positive limsup E rho^2/n, equivalently a negative signed ratio in(17).
Constant covariance, persistent but exponentially rare far fibers and unscaled exponential-moment divergence leave a tight finite-mean branch possible.
Those are mathematical limits of the proved mechanism, not a decision to pause a strategy.
Coordinating fixed retention and draft retirement remain separate from this completed whole noncontributor review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete retained finding](#lower-fiber-complete-independent-review) | unknown |

The whole original mathematical finding, original date and necessary positive/negative/source/cost limits above remain unchanged.
The account records visible progress descriptions or available shared project context but does not establish their actual substantive content and timing relative to initial inspection.
The prior accepted-input authorship and own earlier reviews do not alone imply contribution to this new proof; the historical noncontributor title does not establish initial isolation.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete retained finding](#lower-fiber-complete-independent-review) | [Original full mathematical input](../../ledger/Yin_L_G0335_v1.md#lower-fiber-reuse-and-law) | Entire original Sections1--6/Lemma1/Theorem2/(1)--(17): complete original law, general block convolution/disjoint covariance, exact quartic floor, paid full annular lower tail, signed-integer diagnostic and all source/failed-implication limits. |
