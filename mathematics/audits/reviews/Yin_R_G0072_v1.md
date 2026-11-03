---
author: Yin
---

# Retained project review: Original-law long-block norms, exact collision radius and approximation boundaries

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0173_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="separated-digit-strip-independent-review"></a>

### Complete independent written review

On 2026-10-10 the separately assigned resultant_research AI for Yin read and checked the entire proof, equations (1)--(4), the prefactor assertion and all scope statements.
No mathematical defect, missing hypothesis or necessary correction was found.
The reviewer did not contribute any of these deductions.
The coordinator described the intended argument and disclosed its self-check before review, and the reviewer had previously independently checked D30's operator conventions; this is separately organized noncontributor review, not blind review.
The separate exact-radius/collision-rate investigation was not read or used as a premise of this finding.

**Greedy exponents and interval concentration.**
The threshold S_(j-1)+1 exceeds every earlier selected weight, so the least exponent exists and is strictly greater than its predecessor.
In particular e_j>=1 when minimality of its predecessor is invoked.
Minimality gives beta^(e_j-1)<=S_(j-1)+1.
Consequently S_j+1<=(1+beta)(S_(j-1)+1), with initial value S_0+1=2, and beta^(e_j)<=2beta(1+beta)^(j-1).
The last step to (1+beta)^(j+1) uses 2beta<=(1+beta)^2, so the written e_j<=(j+1)a is valid.
If q_n>=1, every selected index j<=q_n-1 satisfies (j+1)a<=q_n a<=n-1, except that e_0=0 already gives the endpoint directly.
Thus precisely the q_n selected bits used later are available within the word.
The q_n=0 argument is separately valid and does not presume a nonempty selection.

For two selected binary sums, the largest differing selected weight dominates all smaller ones by strictly more than one unless it is e_0, in which case the difference is exactly one.
Thus the sums are pairwise separated by at least one, not merely distinct.
Ordering any finite set of such values inside an interval of length 2B bounds its cardinality by floor(2B)+1; this safe bound also covers integer interval length and either endpoint convention.
Conditioning on all second-copy bits and all unselected first-copy bits leaves exactly 2^(q_n) equally likely translated selected sums.
This proves the interval bound uniformly in its location.
It retains all original eta probabilities and any collisions after the conditioning is removed; there is no assumption that unrestricted algebraic digit sums are distinct.

**Uniform row and column sums.**
The affine endpoint from x is beta^n*x plus a sum with exponents n-1,...,0.
Independence and identical digit laws give the same endpoint distribution as Z_n after reversal of those indices.
The row sum of the killed K^n counts exactly the probability of staying in D through n steps and is at most the probability of its endpoint satisfying the expanding strip inequality.
This proves the uniform row estimate without using endpoint sufficiency or a general co-return theorem.

The reviewer rechecked the invoked D30 identities: the reciprocal field automorphism preserves O, T is a counting-measure-preserving involution of D, and reversal changes eta to -eta with equal weight.
Hence (K^n)*=UK^nU, so a column sum is the corresponding relabeled row sum.
This holds on the entire countable state set; no truncation is inserted.
With both sums bounded by R=M2^(-q_n), nonnegative weighted Cauchy--Schwarz gives

    sum_x |sum_y (K^n)_(xy) f_y|^2
        <=R sum_y |f_y|^2 sum_x (K^n)_(xy)
        <=R^2 ||f||_2^2.

The argument first applies to finite support and extends by density, proving the full l2 norm bound.
Finally floor((n-1)/a)>(n-1)/a-1 gives the displayed factor 2 exp(gamma), with no reversed inequality.
The complete prefactor depends on beta only, while it is allowed to grow as beta approaches one.

**Spectral bounds, lower support interface and limits.**
For each fixed beta, the nth root of the explicit prefactor tends to one.
The spectral-radius formula for a bounded operator therefore gives r_2(K)<=exp(-gamma).
The necessary finite prefix/suffix geometric bounds put every true zero-to-zero word inside the strict strip, while every path contributing to K^n(0,0) has the original digits and product weight.
Thus p_n=K^n(0,0) at the general Salem scope asserted here, independent of whether other strip points are returnable.

The reviewer read the original collision convention in [L154](../../ledger/Yin_L_G0154_v1.md#actual-first-return-paths), the displayed argument in [L30](../../ledger/Yin_L_G0030_v1.md#one-expanding-comparison), and the precise accepted [L7 support interface](../../ledger/Yin_L_G0007_v1.md#pisot-salem-attainment).
The Bernoulli-difference representation gives p_n=sum_x nu_n(x)^2, and finite-support Cauchy--Schwarz gives p_n>=1/|supp nu_n|.
A Salem beta in (1,2) has exactly the one-expanding-conjugate scope of that retained support estimate.
Therefore

    ||K^n|| >= p_n >= C_beta^(-1) n^(-s) beta^(-n).

Taking nth roots for this fixed input proves r_2(K)>=beta^(-1), without needing existence of a separate diagonal-coefficient limit.
The accepted external support theorem keeps its earlier statement/applicability and proof-review boundary; its original source proof was not re-audited here.

These inequalities put the spectral radius strictly between zero and one, permitting all displayed logarithms.
Rearrangement yields 0<=m+log r_2(K)<=m-gamma.
Writing log(1+exp(m))=log2+m/2+log cosh(m/2), the bound log cosh(m/2)<=m^2/8 and log2<=2 give m-gamma<=m^2/(2log2).
The ratio conclusion follows from gamma/m=log2/log(1+exp(m)) tending to one.
The n limit is taken separately for each beta before considering any hypothetical family with m tending to zero.
No degree-uniform support constant or interchange of these limits is required or claimed.

The proof consequently supplies the asserted bound for the full infinite operator and its near-one spectral scale.
It does not identify spectral radius with a diagonal return rate, improve the earlier scalar collision lower exponent, establish same-exponent arithmetic income, or exclude a near-one Salem family.
This review was entirely written and made no computational claim.
No changes to the author proof, new external theorem adoption, fixed-ledger decision or G0001 completion follow from this finding.

## Independent review of the actual collision and operator spectral-radius chain

Date: 2026-10-10.
Responsible working review of the frozen [D37](../../ledger/Yin_L_G0173_v1.md#core-operator-collision-sandwich), Sections1--8, by the separately assigned structural-research AI for Yin.
The complete finding below is ready for the coordinator's fixed-retention decision.
No C acceptance or G0001 completion is asserted.

<a id="collision-radius-complete-independent-review"></a>

### Complete independent written finding

At 2026-10-09T17:04 the reviewer completed the full read and mathematical check of D37, including every statement and proof in Sections1--8, the introduction, contribution account and limits.
No mathematical defect, missing hypothesis or requested mathematical correction was found.
The supported conclusions are the fixed-input polynomial norm sandwich and exact spectral identification for every algebraic unit, the stated Salem-strip extension and all-power essential-norm equality, and the nontorsion finite-prime exhaustion with its correct approximation direction.

This was a separately assigned, noncontributor review.
The drafting orbit-research agent supplied Sections1--6 and parts of the small-real construction; the coordinator contributed Sections7--8 as disclosed in D37.
This reviewer supplied none of those derivations.
It previously reviewed and mechanically retained other fixed operator/core results, and its sole prior edit to D37 relocated the unchanged D30 reference to L172.
Author and coordinator progress explanations, contributions and desired review obligations were provided before this review, so it was not blind.
The reviewer first read the complete frozen source, reconstructed the obligations and estimates, then checked the cited interfaces.
No prior whole-D37 independent verdict was used as evidence.

#### Original law, actual domain and all embedding constants

The original walk and the binary collision convention agree with [L154](../../ledger/Yin_L_G0154_v1.md#actual-first-return-paths): digits have weights1/2,1/4,1/4 and the polynomial order reverses independent indices only.
D37 explicitly extends the domain of its own Sections1--5 to any algebraic unit, including torsion, and proves its needed estimates on that domain.
It does not import L154's default nontorsion restriction or its other results to justify that extension.

Every actual core state has a finite path from zero and a finite continuation back to zero.
At a contracting embedding, the first path gives the finite geometric sum with exponents0 through a-1; at an expanding embedding, solving the second path backward gives exponents-1 through-b.
Both bounds are strictly smaller than the stated positive R_v.
Empty paths cause no exception because then the relevant state is zero.
The bounds use modulus and therefore hold at complex as well as real embeddings.
They supply containment in a cylinder, without asserting that every algebraic point in it belongs to the actual core.

The full norm-grid injection is exactly [L91's accepted interface](../../ledger/Yin_L_G0091_v1.md#norm-grid-support-bound).
Half-open cells of real width1 and complex Cartesian width1/sqrt(2) make every conjugate of the difference of two points in one cell strictly smaller than1 in modulus.
The difference is a nonzero algebraic integer, so its field norm is a nonzero integer, a contradiction.
The order need not be maximal.
This also implies finiteness in bounded full-coordinate boxes.
A translation of the region does not change this injection or the cell-count constants.

For a fixed row and neutral place, the endpoint is in a radius-n interval or disk centered at the n-fold image of the starting coordinate.
For a fixed column, solving backward gives a radius-n interval or disk centered at the inverse n-fold image of the terminal coordinate.
The center may escape and is never replaced by zero.
Both directions restrict the other state to the actual core and hence have the same fixed nonneutral bounds.
At real neutral places the cell count is at most2(n+1).
At a complex neutral place it is at most(2sqrt(2)n+2)^2<=8(n+1)^2.
The nonneutral factors are exactly2R_v+2 and(2sqrt(2)R_v+2)^2.
Multiplication over real places and one representative per complex pair proves the displayed C_alpha and q=r_0+2s_0 for both row and column supports.
There is no missing complex multiplicity, dependence on the translated center, lattice covolume assumption or undisclosed uniform constant.
At n=0, C_alpha>=1 and the claimed estimate also holds.

#### Maximum displacement atom and the operator limit

The full displacement law is the autocorrelation of the same finitely supported fair-binary probability function with itself.
Cauchy--Schwarz therefore bounds every atom by its value at zero, exactly p_n.
No assumption of independent sums after conditioning on a core path is used.
The killed kernel entry is at most the full displacement probability because its admissible paths are a subset.
The source's stronger equality for actual core endpoints is also valid: prepend an actual zero-to-x word and append an actual y-to-zero word to any ambient x-to-y word.
Every intermediate state then belongs to a closed word.
In particular the zero matrix coefficient is exactly p_n, with all excursions and original weights included.

Multiplying the atom bound by the separately proved support counts gives both row and column sums at most A_n=C_alpha(n+1)^q p_n.
Weighted Cauchy--Schwarz for a finitely supported vector, followed by nonnegative summation and the column bound, gives ||K_act^n f||_2<=A_n||f||_2.
Density supplies the bounded extension.
Independently, each fixed digit has at most one successor and one predecessor, so one-step row and column sums are at most1 and K_act is a contraction.
The finite-path matrix multiplication is the actual bounded operator power.
Evaluating at the zero basis vector supplies the lower norm bound.

Closed-word concatenation proves p_(n+m)>=p_n p_m, and the all-zero word gives p_n>=2^(-n)>0.
Thus the logarithmic rate exists, as also recorded in [L30](../../ledger/Yin_L_G0030_v1.md#renyi-rates), and its root limit is positive.
At a fixed input, C_alpha^(1/n)(n+1)^(q/n) tends to1.
The spectral-radius formula applies to the bounded operator in the complex unital Banach algebra B(l2(D_act)), including when the core is finite.
Taking roots of the two-sided inequality proves the stated equality; neither irreducibility, normality nor an unjustified interchange of input and time limits is used.

#### Salem full strip and the asymptotic comparison

For a Salem input, the only nonneutral places have radii B=1/(beta-1) and S=beta/(beta-1), and the other d-2 real dimensions are neutral.
Every closed word obeys the two strict bounds.
Consequently the full-strip zero coefficient is p_n even without an actual-core equality theorem.
Restriction of other entries still gives the same maximum-atom bound, while strip membership supplies both fixed nonneutral bounds in the row/column counts.
The specialization C_beta=(2B+2)(2S+2)8^s and q=d-2 is correct.
No returnability of all strip points is smuggled into this argument.

The identification of strip and actual core for the two named fixed inputs uses [L170's exact conditional-strip theorem](../../ledger/Yin_L_G0170_v1.md#exact-salem-return-strip) with its independently supported narrow co-return premise.
It is not asserted for every Salem input.
The logarithmic finite-time overhead follows directly by taking logs of positive quantities.
Its degree and input dependence remains explicit.
The small-m comparison h_2/m->1 is exactly the accepted one-expanding-conjugate scope of [L30](../../ledger/Yin_L_G0030_v1.md#one-expanding-comparison).
The contrasting one-step behavior from [L172](../../ledger/Yin_L_G0172_v1.md#reciprocal-kernel-fiber-norm) follows from N=ceil(2B), lambda_N=cos^2(pi/(2(N+1))), B asymptotic to1/m and the elementary cosine expansion.
It gives -log lambda_N asymptotic to pi^2 m^2/16.
These statements concern different time scales and do not assert an input-uniform convergence time or a Mahler gap.

#### Every power has its full essential norm on the Salem strip

The small-real construction uses three integer coefficients and degree at least4, making all (N+1)^3 elements distinct.
Their two-real images lie in a rectangle with side lengths O_beta(N), which uses O_(beta,epsilon)((N+1)^2) fixed-epsilon cells.
For sufficiently large N, two images are in one cell, and their nonzero algebraic difference has both real coordinates of absolute value less than epsilon.
Field-embedding injectivity excludes a nonzero difference with a zero real coordinate.
Choosing epsilon tending to zero cannot leave a bounded subsequence in the neutral coordinates: together with eventually bounded real coordinates this would place infinitely many required values in a full bounded grid box, containing only finitely many algebraic integers.
Hence one can choose neutral norms tending to infinity and separated as far as the finite support requires.
This establishes infinitely many distinct strip points without relying on the co-return premise.

A finitely supported unit vector can approximate the norm of a bounded power.
Its image has finite support because every column has at most3^n predecessors.
For strip endpoints, every ambient word has all intermediate states in the strip: the stable bound is invariant forward since beta^(-1)S+1=S, and the expanding bound is invariant backward since (B+1)/beta=B.
Strictness is preserved in both directions.
The kernel between endpoints is consequently the full displacement kernel.

For fixed finite input and image supports, sufficiently small real coordinates of h preserve all their strict inequalities after the two distinct translations F+h and G+beta^(-n)h.
Unit status puts beta^(-n)h in the same order.
The displayed displacement identity has the correct sign and power and gives exact equality for every retained entry.
Thus the translated image agrees on the retained translated rows; other rows can only increase its squared norm, even for complex test vectors, because they are additional coordinates rather than extra summands on those rows.

The input translates may be made disjoint using neutral norm separation larger than the finite neutral diameter of F.
Their unit vectors are orthonormal and therefore weakly null.
Compact operators send this sequence to zero in norm.
The triangle inequality then gives the lower bound ||K_strip^n-A||>=||K_strip^n||-epsilon for every compact A.
Taking the infimum and letting epsilon tend to zero proves full essential norm.
The reverse inequality is immediate.
This includes n=0, where the same infinite sequence proves the identity has essential norm1 and the compact ideal is proper.
The quotient is a complex unital Banach algebra, its power norm is exactly the corresponding essential norm, and the spectral-radius formula gives the stated essential radius.
The reasoning is restricted to the full Salem strip, so it does not contradict finite general-unit cores.

#### Finite-prime exhaustion and its direction

Section8 explicitly adds nontorsion, matching the accepted [L157 finite restricted-core theorem](../../ledger/Yin_L_G0157_v1.md#finite-prime-return-core).
The reviewer reread its original-digit, integral-order, maximal-order prime and actual restricted-language definitions and its finiteness conclusion.
D_S is the set of states on fully restricted closed words, not the ambient intersection of the core with S-units.
Its finite original weighted kernel is therefore exactly the required object.
The [ESS02 accepted counting interface](../literature/ESS02/Yin_U001.md#ess-exact-counting-bound) remains the source of L157's finiteness; neither its original proof nor the old fixed theorem is newly re-audited here.

For nested S, every smaller admissible word remains admissible, so the domains and path kernels increase.
Extending by zero to the common space gives entrywise domination by the larger powers.
Replacing a complex test vector by its coordinatewise absolute value and using the l2 norm proves power-norm domination, and hence radius domination.
No monotonicity theorem for arbitrary nonnormal operators is assumed.

There are finitely many words of length at most n, and each of their finitely many nonzero integral states has finite prime-ideal support.
Thus S_n is finite and nested.
Every length-n closed word is included in the associated restricted core, giving exact equality of its zero coefficient with p_n.
Concatenating k such words gives a coefficient at least p_n^k at time kn.
The finite-matrix spectral-radius formula along these multiples yields r(K_(S_n))>=p_n^(1/n).
Supermultiplicativity gives sup_n p_n^(1/n)=lim_n p_n^(1/n), so the nested finite radii approach the already identified full radius from below.
Zero belongs to every core and has its weight1/2 self-loop, making all radii at least1/2 and all negative logarithms finite.
The entropy approximants approach from above.
No effective error bound, bounded prime set or uniform rate follows.

The coexistence of finite-prime exhaustion and full essential norm is logically consistent: the former proves scalar radius approximation through closed words, not operator-norm convergence of finite compressions.
The stated tail-control limitation follows in the correct direction.

#### Source completeness and the performed verification boundary

The reviewer directly text-read the author-hosted [Pet20 edition dated 27 April 2020](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), its title/date, Proposition1.1.6 on pp.7--8, Exercise1.1.14 on p.10, and Theorem3.3.1 plus the following compact-ideal paragraph on p.41.
The first supplies norm-root spectral radius for complex unital Banach algebras; the second supplies the distance-to-ideal quotient norm; the third supplies weak-to-norm continuity on the unit ball for compact operators, with the following paragraph identifying their closed two-sided ideal.
These statements and actual applicability match [Pet20-U001](../literature/Pet20/Yin_U001.md#pet20-u001).
The quotient here has a proper ideal, as established above.
The source proofs were not independently audited.
Its existing bounded-acquisition exception remains truthful; this review obtained no local PDF or new source artifact.

The old L91 norm-grid, L30 entropy comparison, L170 fixed-input core and L172 operator interfaces were reused only at their stated scopes.
Their historical reviews are not relabelled as new reviews of those complete sources.
The present proof's new deductions have all been checked above.
No program, numerical experiment, J allocation, formal verification, broad novelty search, whole-source proof audit or user-personal inspection is claimed.
No mathematical correction arose during this review.
The complete D37 chain is ready for the coordinator's fixed-adoption decision at its exact stated scopes; the unrestricted G0001 gap remains unresolved.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete collision-radius finding](#collision-radius-complete-independent-review) | [General-unit statement and complete proof](../../ledger/Yin_L_G0173_v1.md#core-operator-collision-sandwich) | Entire Sections1--5: original law, actual core, strict nonneutral bounds, explicit translated row/column counts, maximum atom, bounded power norm sandwich and fixed-input spectral identification, including n=0 and torsion inputs. |
| [Complete collision-radius finding](#collision-radius-complete-independent-review) | [Salem full-strip corollary](../../ledger/Yin_L_G0173_v1.md#salem-strip-exact-collision-radius) | Complete Section6 and exact constant, every Salem beta in(1,2) without assuming full-strip co-return, two fixed actual-core identifications, explicit degree overhead and L30/L172 rate comparison. |
| [Complete collision-radius finding](#collision-radius-complete-independent-review) | [All-power essential-norm equality](../../ledger/Yin_L_G0173_v1.md#salem-strip-all-power-essential-norm) | Entire Section7 for Salem full strips only: small-real algebraic translations, neutral escape, finite supports, endpoint legality, exact displacement preservation, compact lower bound for all n>=0, proper quotient and essential radius. |
| [Complete collision-radius finding](#collision-radius-complete-independent-review) | [Finite-prime radius exhaustion](../../ledger/Yin_L_G0173_v1.md#finite-prime-spectral-exhaustion) | Entire Section8 for nontorsion algebraic units, accepted L157/ESS finiteness boundary, actual restricted languages, monotone kernel/radius comparison, all closed-word prime sets and below-radius/above-entropy approximation with no effective rate. |
| [Complete separated-digit finding](#separated-digit-strip-independent-review) | [Separated-digit statement and complete proof](../../ledger/Yin_L_G0173_v1.md#separated-digit-strip-norm) | Entire original D36 Sections1--2 and equation(1): every Salem beta in(1,2), original law, full open strip, greedy exponents including q_n=0, one-separated sums, interval concentration, uniform rows/reciprocal columns and beta-only prefactor; no co-return premise. |
| [Complete separated-digit finding](#separated-digit-strip-independent-review) | [Spectral interval and small-measure comparison](../../ledger/Yin_L_G0173_v1.md#strip-radius-small-measure-comparison) | Entire original D36 Section3, equations(3)--(4) and stated limitations: bounded-operator spectral-radius formula, original zero coefficient, fixed-beta L30/L7 support interface and order of limits; source proof not re-audited and no operator/diagonal equality assumed by this separate proof. |
| [Original complete separated-digit author check](#separated-digit-original-author-check-finding) | [Original entire separated-digit statement/proof](../../ledger/Yin_L_G0173_v1.md#separated-digit-strip-norm) | Actual original2026-10-10coordinator-author self-check of the complete D36 argument, including strict greedy exponents/q_n=0/fixed-distance separation/original-law conditioning/reciprocal column bound and order of limits, as explicitly recorded in its original Checking and attribution paragraph; not a new historical event or noncontributor review. |
| [Original complete separated-digit author check](#separated-digit-original-author-check-finding) | [Original spectral comparison](../../ledger/Yin_L_G0173_v1.md#strip-radius-small-measure-comparison) | The same actual complete author check includes all original equations(1)--(4), exact beta-only upper prefactor versus fixed-input support constant, spectral interval/quadratic width and n-before-input limit; original date has day precision. |
| [Original entire collision-chain author check](#collision-radius-original-author-check-finding) | [Original general-unit theorem and proof](../../ledger/Yin_L_G0173_v1.md#core-operator-collision-sandwich) | Actual original2026-10-10entire-proof author self-check recorded after Sections1--8: general-unit original law/actual core/nonneutral bounds/all-place translated grid/maximum atom/n=0 and torsion/norm-spectral sandwich, at its original contributor scope. |
| [Original entire collision-chain author check](#collision-radius-original-author-check-finding) | [Original Salem full-strip corollary](../../ledger/Yin_L_G0173_v1.md#salem-strip-exact-collision-radius) | The same actual entire-proof author check includes Section6 full-strip probability without general co-return, explicit degree overhead, fixed input application and rate comparison; no new date or separate coordinator whole check. |
| [Original entire collision-chain author check](#collision-radius-original-author-check-finding) | [Original every-power essential norm](../../ledger/Yin_L_G0173_v1.md#salem-strip-all-power-essential-norm) | The same actual entire-proof author check includes coordinator-supplied Section7 translation mechanism and the drafting agent's explicit small-real construction and finite-support/domain checks, compact lower bound/proper quotient/all n>=0, for Salem strips only. |
| [Original entire collision-chain author check](#collision-radius-original-author-check-finding) | [Original finite-prime exhaustion](../../ledger/Yin_L_G0173_v1.md#finite-prime-spectral-exhaustion) | The same actual entire-proof author check includes coordinator-supplied Section8 and the drafting agent's monotonicity checks, nontorsion/C375-original-L157/accepted ESS scope, actual D_S versus ambient V_S, all closed-word prime sets and below-radius/above-entropy direction; no effective approximation rate. |

## Review relationships

The entire original mathematical/source/checking account, every date and inspected input, all six original binding rows and both original no-correction conclusions remain unchanged above.
The following declarations preserve the actual historical arrangements and explicit complete author checks; they perform no new historical mathematical or source/native inspection.

For the original whole D36 noncontributor finding, the record says the coordinator described the intended argument and disclosed an author self-check before review.
It does not preserve the actual communicated target-mathematical content, author-check result account supplied at that stage, or initial arrangement sufficient to establish isolation or known substantive prior sharing.
The earlier D30 operator convention is a necessary frozen interface, not automatically the new separated-digit proof.
That entire original equations(1)--(4)/prefactor/full-strip/concentration/spectral/source/limit target therefore remains unknown for independent-review purposes.

For the original whole D37 finding, generic author/coordinator progress explanations, contributions and desired review obligations are disclosed, but their actual pre-review mathematical content and initial context are not established.
The known authorship of Sections1--6 and7--8 in the frozen target and normal reading of fixed upstream interfaces do not by themselves decide the reviewer's prior isolation.
A statement that no earlier whole-D37 independent verdict was used does not establish absence of other substantive target context.
The complete original Sections1--8/general-unit/Salem-essential/nontorsion-exhaustion target therefore remains unknown, with all distinct scope and source depths intact.
Fresh isolated coverage is still needed for both whole unknown targets; the original noncontributor titles are not a substitute, and later current self-checks do not close those obligations.

The separate complete author checks are explicitly recorded in the original L173.
The coordinator authored and self-checked the entire D36 argument with its named steps.
The drafting agent's entire D37 proof was author self-checked after the disclosed coordinator contributions to Sections7--8 and its own finite-support/domain/monotonicity checks.
Those actual whole author arrangements are known self-review.
They are retained here at the original day precision, without inventing an additional coordinator whole-chain inspection, a finer timestamp or an independent conclusion.

| Review | Relationship |
| --- | --- |
| [Original complete collision-radius noncontributor finding](#collision-radius-complete-independent-review) | unknown |
| [Original complete separated-digit noncontributor finding](#separated-digit-strip-independent-review) | unknown |
| [Original complete separated-digit author check](#separated-digit-original-author-check-finding) | self-reviewed |
| [Original entire collision-chain author check](#collision-radius-original-author-check-finding) | self-reviewed |

<a id="separated-digit-original-author-check-finding"></a>
## Original complete separated-digit author check

Date: 2026-10-10.
The original D36 Checking and attribution paragraph states that the coordinator authored and self-checked the complete argument, including strict exponent selection, q_n=0, fixed separation, original-law conditioning, reciprocal column bound and order of limits.
It records a written proof without a computational premise and a then-pending noncontributor review.
This retains exactly that actual complete author-check scope as self-reviewed, without a new old event, minute, separate verdict or noncontributor inspection.
The separately retained original whole noncontributor account remains unknown under its distinct initial-context boundary.

<a id="collision-radius-original-author-check-finding"></a>
## Original entire collision-chain author check

Date: 2026-10-10.
The original D37 contribution/verification paragraph records that the entire proof is author self-checked and ready for separately assigned review.
The drafting agent supplied the maximum atom, translated counts, general-unit sandwich and identification.
The coordinator supplied the Section7 all-power essential-norm mechanism and Section8 finite-prime deduction, while the drafting agent supplied the small-real construction and checked finite-support/domain/monotonicity steps.
The retained scope is that actual entire author check of Sections1--8, with their different domains and source limits.
It is self-reviewed, without inventing a separate complete coordinator check, finer timestamp, new source inspection or additional original event.
The original01:04whole noncontributor finding and its unknown initial-context relation remain separately preserved.
