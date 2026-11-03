---
author: Yin
---

# Retained project review: A certified infinite original-digit return core for a quartic Salem unit

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0169_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="quartic-full-review-retention"></a>

## Independent review of the fixed quartic actual return core

Date: 2026-10-09.
Separately assigned whole-chain review of D G0013, D G0014, J G0018 and J G0019.
This rolling review records the findings below; it is not itself a fixed-ledger or Claim adoption.

### Arrangement and exact scope

The reviewer agent contributed none of the neutral descent, compact enumeration, timing estimate, reciprocal reachability bridge or finite-core equivalence.
This is a separately organized mathematical review for Yin, not a personal human inspection and not a blind review: parent/author progress descriptions and the existing coordinator/contributor review passages were supplied or read before these findings.
Initial obligations are root and order identification; interval enclosure and triangle descent; zero-prefix and iteration bounds; completeness of compact coefficient bounds and enumeration; every saved original-digit continuation; reciprocal word signs/order; lattice infinitude; and the accepted L G0157 interface.
The old ESS proof is not being re-audited.
Author drafts remain unedited by this reviewer.

The inspected mathematical artifacts are the complete [D G0013 Sections 1--7](../../ledger/Yin_L_G0169_v1.md#quartic-neutral-descent), complete [D G0014 Sections 1--4](../../ledger/Yin_L_G0169_v1.md#quartic-compact-termination), and all programs and the retained digit/state certificates of [J G0018](../../computations/programs/Yin_J_G0018/readme.md) and [J G0019](../../computations/programs/Yin_J_G0019/readme.md), as held by their authors for this review on 2026-10-09.
The exact acceptance interface inspected is [L G0157 v1 Sections 4--5 and its adoption account](../../ledger/Yin_L_G0157_v1.md#global-prime-support-finite-core-equivalence).
The earlier [Mer13-U001 scoped reading](../literature/Mer13/Yin_U001.md#mer13-u001) was read for method attribution and the boundary between its different quartic and the present new table.

<a id="quartic-full-chain-review"></a>

### Full-chain finding

At 2026-10-09T15:39 the separately assigned structural_research AI for Yin completed the following review and found no substantive mathematical defect or missing hypothesis in the stated fixed-input result.
No correction is requested.
The supported conclusion is:

    For the expanding root beta of t^4-t^3-t^2-t+1,
    every x in Z[beta] with |x(beta)|<=1 and
    |x(beta^(-1))|<=beta/(beta-1) admits an original
    {-1,0,1}-digit continuation to zero.

    The actual zero-to-zero returning-state set is infinite.

The radius-dependent timing/probability corollary and the L G0157 consequences are also supported at precisely the scopes checked below.
This is a separately organized independent written review, with the nonblind input conditions declared above.
The decisive reasoning is recorded here rather than inferred from successful script execution.

#### 1. Algebraic domain and exact interval arithmetic

The trace factorization t^(-2)P(t)=u^2-u-3 with u=t+t^(-1) has two real roots, one above 2 and the other strictly between -2 and 2.
The first defines beta>1.
Its quadratic discriminant u^2-4 is negative under the other embedding of Q(sqrt(13)); a square in that totally real quadratic field could not have a negative image.
Thus [Q(beta):Q]=4, P is the minimal polynomial, and its roots are beta, beta^(-1), zeta, conjugate(zeta) with |zeta|=1.
The constant term one gives beta^(-1)=-beta^3+beta^2+beta+1 in Z[beta].
In particular beta is a nontorsion algebraic unit, and its four distinct embeddings give an invertible real embedding matrix for the rank-four order.
The asserted full lattice and injectivity are justified, not additional assumptions.

The J G0018 interval primitives were checked directly: endpoint addition and negation, four-corner multiplication, reciprocal division only away from zero, a square that includes zero when appropriate, and integer-square-root lower/upper rounding all enclose the represented exact quantity.
In particular, taking the integer square root of the floor of a scaled nonnegative rational gives a valid lower endpoint; adding one to the upper integer square root gives a valid upper endpoint even at a perfect square.
The formulas enclose the specified beta and upper-half-plane zeta, with 17/10<beta<18/10.
Complex multiplication and squared norms preserve enclosure despite dependencies between intervals; such dependencies can enlarge intervals but cannot invalidate their bounds.

The independently implemented [J G0021 verifier](../../computations/programs/Yin_J_G0021/review.py) does not import any author interval or discovery helper.
It isolates beta by rational sign bisection on (17/10,18/10); uniqueness there follows, for example, from P'(t)>=4(17/10)^3-3(18/10)^2-2(18/10)-1>0.
It uses outward integer intervals at scale 10^25.
Its separately coded operations, root construction and subsequent checks were inspected as part of this review.
The new verifier is reviewer evidence, not a formally verified arithmetic library or an additional independent review of the reviewer.

#### 2. Complete descent mechanism, including endpoints

The fifty closed cells exactly cover [1/2,1].
Each has three saved words over the original alphabet, of length at most nine.
Both the author verifier and the independent verifier check the affine image of the entire cell, with strict image bounds (-1,1).
Each oriented cross product between consecutive displacement vertices is strictly positive.
These three half-plane inequalities put zero strictly inside the triangle, and dividing the oriented cross product by an upper bound on edge length gives a valid lower bound on its distance to that edge.
Hence the disk with radius the smallest such lower bound lies inside the triangle.

Minimizing the real linear functional c -> Re(conjugate(z)c) over this triangle occurs at a vertex and is at most its value -r|z| at the disk point opposite z.
Since the endpoint neutral coordinate is zeta^k(z+c), the bound 20r-m>=557/500 gives the asserted drop whenever |z|>=10.
The independently recovered minimum lower margin, rounded down to six decimal places, is 1114267/1000000, which exceeds 557/500.
This validates the advertised weaker rational constant.

Negating the state and every digit treats the negative cells.
An algebraic state with zero expanding coordinate is zero by injectivity, so it cannot have neutral magnitude at least ten.
For a small nonzero expanding coordinate, the first zero-prefix crossing of magnitude 1/2 is finite and lies below beta/2<1; its stable coordinate contracts and its neutral magnitude does not change.
The contracting strip is invariant under each individual digit because beta^(-1)S+1=S.
Backward evaluation from a strict final expanding bound gives, with r digits remaining, beta^(-r)+(1-beta^(-r))/(beta-1)<B; the zero-prefix states also lie below B.
This checks all intermediate real bounds as well as the block endpoints.
Shared cell boundaries, initial magnitude exactly 1 or 1/2, and neutral magnitude exactly ten are covered.

At successive endpoints the neutral square drops by at least the positive constant 557/500 while both narrow real bounds are preserved.
Infinite descent before entry into |z|<10 is therefore impossible.
Each individual zero prefix is finite, so this is finite actual-word reachability of K, not just a decrease in an abstract potential.
Boundedness of all four embedding coordinates and the full lattice imply K is finite, even though its neutral inequality is strict.

#### 3. Compact enumeration is complete

For the real embedding matrix M and inverse A, the coordinate estimate

    |a_i| <= |A_(i,0)| + S|A_(i,1)|
             + 10 sqrt(A_(i,2)^2+A_(i,3)^2)

follows by applying each inverse row and the Euclidean bound on the two neutral coordinates.
J G0019 computes A by interval adjugate/determinant: the minor removes row j and column i for entry (i,j), the sign is correct, and the determinant interval excludes zero.
The code takes upper bounds on both absolute real coefficients and the neutral row norm, then floors the resulting upper bound only because each |a_i| is an integer.
This establishes the coefficient box (5,7,7,4).

Every subsequent embedding entry is rounded outward to the integer scale.
For a fixed tail (a_1,a_2,a_3), if its expanding value lies in [l/Q,h/Q], the necessary interval for a_0 is [-1-h/Q,1-l/Q]; the ceiling/floor slice in the author program is exactly this interval intersected with the proved coefficient bound.
Thus no possible member of K is lost in slicing.
A stable-coordinate interval is rejected only if entirely beyond an outward upper bound for S.
The neutral rejection uses the sum of the separate squared-distance lower bounds from zero; these are lower bounds on the true squared modulus.
Rejection at lower bound >=100 is legitimate because K has the strict inequality |z|<10.
Ambiguous interval boundaries are retained.

As an implementation-independent check, J G0021 encloses M^(-1) by interval Gaussian elimination, rather than the author's adjugate formula, and tests all 22,275 tuples of the proved coefficient box, rather than using the author's a_0 slicing.
It obtains the same coefficient bounds, 841 tuples surviving the expanding test and exactly the same set of 259 retained candidates.
Equality of the two retained finite sets is checked, not inferred from matching counts.
Both enumerations produce a certified superset of K; neither needs to assert exact membership of boundary candidates.

#### 4. Every retained point has a valid actual continuation

The integer transition in J G0019 is the correct consequence of beta^4=-1+beta+beta^2+beta^3.
Its checker validates integer state coordinates, original digits, no repeated start state, membership in the enumerated candidate set, a zero terminal state and full set coverage.
The empty path for zero is permitted.
No floating-point membership decision enters those checks.

The independent J G0021 check instead forms, for each saved state a and word w of length n, the integer polynomial

    t^n(a_0+a_1 t+a_2 t^2+a_3 t^3)
       + sum_(i=1)^n eta_i t^(n-i)

and performs exact monic polynomial long division by P.
All 259 remainders are zero, all targets are covered exactly once, and the maximum length is 25.
Irreducibility and the power basis make this polynomial calculation an actual algebraic endpoint check.
Discovery's floating-point radius-twelve pruning and its 433 visited nodes are unnecessary for completeness of this certificate; they only explain how the selected words were found.
Both discovery source programs were read, but neither numerical discovery run was repeated.

Appending these finite continuations to the descent words proves co-return for every actual order element in the full narrow real domain, without a prior reachability assumption and with no bound on its initial neutral coordinate.

#### 5. Timing and original probabilities

At every nonzero pre-K endpoint, norm integrality gives 1<=|x_+x_-||z|^2.
From S<17/7 and |z|<=R this yields |x_+|>7/(17R^2).
With the defined K_R, multiplication by beta for at most K_R zero digits makes its magnitude exceed 1/2; the first crossing therefore takes no more than that many digits.
Subsequent endpoints retain |z|<=R because the neutral square decreases.
For N_R=floor((R^2-100)/(557/500))+1 the strict inequality R^2-N_R(557/500)<100 holds, including R=10.
Thus L_R=N_R(K_R+9) is a valid upper bound to K, with zero time allowed for an initial point already in K.
Adding 25 gives the claimed continuation bound to zero.

Each chosen word of length l has original product probability at least 4^(-l), since the digits have probabilities (1/4,1/2,1/4).
The event following that prefix is contained in the event of hitting the target by the stated time.
Therefore the lower bounds 4^(-L_R) and 4^(-(L_R+25)) are justified even when different inputs choose different words.
The estimate is uniform on the displayed bounded-radius domain for this fixed beta, and is not uniform in an unbounded radius or a varying Salem input.
It gives no bound on the full departure-and-reentry law or its tail.

#### 6. Reciprocal conversion and infinitude

The reciprocal irreducible polynomial and beta^(-1) in Q(beta) define an automorphism sigma of this same field with sigma(beta)=beta^(-1), sigma^2=id and sigma(Z[beta])=Z[beta].
Consequently T=beta^(-1)sigma preserves the order and T^2=id.
Solving the zero endpoint equation gives y=-sum eta_i beta^(-i); applying T gives -sum eta_i beta^(i-1), precisely the state obtained from zero by the reversed, negated digits -eta_n,...,-eta_1.
Both the sign and the order in D G0013 Section 7 are correct.

For x in Omega, beta<S follows from beta<2.
Thus x lies in the co-return domain.
Moreover T(x)_+=x_-/beta and T(x)_-=beta x_+, so T(x) lies in that domain too.
Its continuation to zero reverses and negates to a path from zero to x; concatenating this with x's own continuation gives an actual original-digit zero-to-zero word containing x.
No claim about a relaxed ambient projection or a wider alphabet is needed.

The (N+1)^4 coefficient-box elements are distinct by the degree-four power basis.
Their two real coordinates lie in a rectangle with side lengths bounded by constants times N.
Partitioning into half-open cells of widths 1 and beta uses O(N^2) cells, so one cell contains at least cN^2 points for some fixed c>0 for all sufficiently large N.
Subtraction from one selected point gives that many minus one distinct order elements with real coordinate magnitudes strictly below 1 and beta.
The growing lower bound on their number proves Omega infinite even though the occupied cell may change with N.
Thus the actual core is infinite, not merely a computed large finite subset.

#### 7. Accepted inputs, attribution and the exact conclusion boundary

L G0157 v1 Sections 4--5 require a nontorsion algebraic unit, its actual order Z[alpha], the original alphabet and true zero-to-zero states.
All hold here.
The fixed accepted equivalence therefore supplies unbounded absolute integer norms of nonzero actual states, infinitely many prime ideals across their supports, absence of one finite prime-support cover, and unbounded coefficient height of integer q with H(Pq)<=1.
It also supplies nonregularity of the finite zero-word language if that consequence is desired.
The old fixed review and ESS input are reused at their retained scope, not newly independently proved here.

Method attribution is present and appropriately scoped: Mer13 concerns a different quartic and motivates neutral descent followed by a finite residual check; its numerical table and theorem are not transferred as mathematical premises.
The existing scoped source unit identifies the primary source and exact geometric locators, while explicitly recording the acquisition/inspection limits.
This review read that retained source account, not the original Mercat geometric proof or its computer certificate.
The present argument provides its own table, complete compact certificate and reciprocal conversion.
No literature novelty claim or exhaustive priority search has been made.
Beyond the accepted L G0157 equivalence, all mathematical steps needed for this new quartic are displayed and checked locally.

The whole chain supports a proved fixed-input special result once the responsible coordinator records its adoption.
It does not establish the unrestricted Lehmer gap, an infinite actual core for the degree-ten Lehmer polynomial, a theorem for every Salem input, a near-one family, or a uniform entropy/return-tail estimate.
These are substantive scope limits, not missing steps in the stated quartic theorem.
This finding does not complete G0001.

### Executed verification and retention

The reviewer implementation and complete outputs are retained in [J G0021](../../computations/programs/Yin_J_G0021/readme.md).
On Python 3.12.14, `review.py` independently verified the 150 block words, all 22,275 coefficient tuples and all 259 exact continuations.
`replay_authors.py` also ran J G0018 `verify.py`, J G0019 `enumerate.py` and J G0019 `verify_paths.py`, redirecting their writes into J G0021 so author artifacts remained untouched.
Their regenerated mathematical outputs match the saved outputs, apart from allowed Python-version metadata.
The latter replay checks reproducibility and is not claimed as an independently implemented algorithm; the separate `review.py` supplies the implementation distinction described above.

This is a written mathematical and computational review.
It is not a formal proof-assistant check, a personal human review, a fresh audit of accepted ESS mathematics, or an independent reconstruction of the numerical searches.
No later substantive change to the inspected source is covered automatically.

<a id="quartic-consolidation-review"></a>

### Final consolidation interface review

On 2026-10-09T15:43 the same separately assigned reviewer read the complete [D G0018 consolidation](../../ledger/Yin_L_G0169_v1.md#quartic-infinite-core-theorem), assembled by the coordinator from the component arguments reviewed above.
The reviewer did not contribute to that assembly.
This is a further interface review under the same disclosed nonblind arrangement, not a rerun of unchanged computations.

The initial reread found two statements requiring clarification before the consolidated theorem could be accepted.
First, numbered theorem item 4 stated the neutral-radius bound without repeating the essential assumptions |x_+|<=1 and |x_-|<=S, although its proof retained them.
Read as an independent numbered assertion, that omitted the real-domain restrictions.
Its wording also needed to identify an existing finite continuation and a lower probability of hitting, rather than implying a deterministic bound on every random path's hitting time.
Second, the computation summary could be read as asserting equality of the intermediate 841-element expanding-strip sets.
The independent check retained and compared the complete 259-element candidate sets; 841 was checked as a count, because the author output did not retain the intermediate set.
These two corrections were sent to the assembling coordinator before acceptance; the reviewer made no change to D G0018.

All other mathematical components, constants and direct dependencies in the inspected consolidation agree with the reviewed component chain: the exact algebraic input and original alphabet, descent constant557/500, 50 cells/150 words of length at most nine, complete coefficient bounds (5,7,7,4), 259 compact candidates with continuations of at most25 digits, N_R/K_R/L_R formulas, reciprocal sign/order and slab inclusions, infinitude argument and the accepted L157 interface.
The old unresolved compact premise has been legitimately discharged by the following exact certificate; removing that pending wording introduces no new assumption.
Final disposition awaits checking the two scoped wording corrections.

#### Corrected consolidation: final disposition

At 2026-10-09T15:48 the reviewer reread both corrected locations in D G0018.
Theorem item 4 now explicitly quantifies over x in Z[beta] satisfying |x_+|<=1, |x_-|<=S and |z|<=R with R>=10; asserts the existence of an original-digit continuation of length at most L_R+25; and separately states the original-law probability of hitting zero by that time.
It also explicitly excludes an interpretation as a bound on every random trajectory.
These are exactly the reviewed hypotheses and conclusions of the timing argument.

The J G0021 evidence paragraph now reports agreement of the 841 expanding-strip tuple count and equality of the 259 retained-state sets.
It explicitly states that the intermediate 841-tuple set was not retained or compared as a set.
This matches the actual implementation and retained outputs.

Both initial findings are therefore resolved.
The complete consolidation, together with these checked corrections, has no remaining mathematical or evidence-scope objection from this review and is supported at the exact fixed-quartic scope of the full-chain finding above.
No new hypothesis, constant, dependency or generalization has entered through consolidation.
The unchanged code and certificates were not rerun for this wording-only recheck.
The reviewer did not edit D G0018, and the previously disclosed independently organized, nonblind relationship remains unchanged.
The coordinator may retain the consolidated argument and this complete review history in fixed mathematical material; that adoption does not complete G0001 or broaden the result to other Salem inputs or a uniform entropy bound.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Full-chain finding](#quartic-full-chain-review) | [Complete quartic proof](../../ledger/Yin_L_G0169_v1.md#quartic-infinite-core-proof) | Original D G0013/D G0014 component chain, all exact certificate/completeness obligations, reciprocal reachability and infinitude, radius-dependent timing, and the accepted L157 interface; fixed retention preserves the checked argument. |
| [Corrected consolidation finding](#quartic-consolidation-review) | [Exact consolidated theorem](../../ledger/Yin_L_G0169_v1.md#quartic-infinite-core-theorem) | All four conclusions at this fixed beta, including the explicitly restored real-strip and radius assumptions and the existence/probability distinction in item 4. |
| [Corrected consolidation finding](#quartic-consolidation-review) | [Complete quartic proof](../../ledger/Yin_L_G0169_v1.md#quartic-infinite-core-proof) | Complete D G0018 assembly of the already independently reviewed chain, unchanged constants and dependencies, plus the checked corrections and accurate 841-count/259-set evidence wording. |
| [Original corrected-locations reread](#quartic-original-corrected-locations-finding) | [Original corrected theorem item4](../../ledger/Yin_L_G0169_v1.md#quartic-infinite-core-theorem) | Exactly the actual2026-10-09T15:48 reread of item4 restoring both real-strip hypotheses, abs(z)<=R with R>=10, existence of one original-digit continuation and the separate lower hitting probability, with every-random-trajectory interpretation expressly excluded; not an additional whole corrected-proof inspection. |
| [Original corrected-locations reread](#quartic-original-corrected-locations-finding) | [Original computation summary](../../ledger/Yin_L_G0169_v1.md#sources-computation-and-contributions) | Exactly the same23:48 actual reread distinguishing agreement of the841 expanding-strip count from equality of the259 retained candidate sets, with the intermediate841 set not retained or compared; unchanged code/certificates were not rerun. |

## Review relationships

These declarations preserve the complete original23:39 full-chain and23:43 consolidation inspections, both initial scope/evidence findings, actual23:48 two-location reread, original dates, mathematical/native inputs, verdicts and every fixed-input/source/tail limit above.
The original arrangement explicitly supplied or consulted the existing coordinator/contributor review passages before initial findings.
Those retained L169 passages actually contain target-mathematical norm, zero-prefix/timing and reciprocal-bridge checking/conclusions, in addition to generic progress descriptions.
This establishes substantive prior target context; the old noncontributor and independently organized labels do not make either whole arrangement isolated under the current rule.
The same disclosed arrangement continues through consolidation and the targeted reread.
The arithmetic implementation distinction in J21 remains a true program-level fact, not an independent agent-review classification.
This administrative clarification performs no new mathematical or native execution and does not invent an additional corrected-whole inspection.
The earlier exploratory/local checks and their exact contribution/order remain fixed in L169, without retroactively making an earlier check a later proof contribution.

| Review | Relationship |
| --- | --- |
| [Original full-chain finding](#quartic-full-chain-review) | self-reviewed |
| [Original consolidation finding and preserved initial objections](#quartic-consolidation-review) | self-reviewed |
| [Original corrected-locations reread](#quartic-original-corrected-locations-finding) | self-reviewed |

<a id="quartic-original-corrected-locations-finding"></a>
## Original corrected-locations reread

Date: 2026-10-09T15:48.
The original23:43 consolidation inspection identified two precise findings before acceptance.
Theorem item4 needed the real-strip hypotheses and an explicit existence/lower-hitting-probability interpretation rather than a bound on every random trajectory.
The computation summary needed to distinguish the841 intermediate count from the259 complete set equality.
At23:48 the same reviewer actually reread those two corrected locations and closed both findings.
No new hypothesis, constant, dependency or generalization entered the complete component chain, and unchanged code/certificates were not rerun.
This finding preserves that targeted scope rather than reporting an additional whole corrected-proof inspection.
It remains self-reviewed under the same known substantive prior-context arrangement disclosed above.
The original full-chain/consolidation mathematical accounts and native evidence above retain their actual input and scope; no new independent obligation is claimed discharged by this administrative declaration or by a later self-check.
