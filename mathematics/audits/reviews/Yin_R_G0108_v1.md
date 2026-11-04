---
author: Yin
---

# Retained project review: Exact information frontier at prescribed actual stationary zero mass

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0212_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="prescribed-zero-mass-complete-independent-review"></a>

### Complete separate noncontributor review

At 2026-10-09T20:33 the assigned resultant_research AI for Yin completed a separately organized full review of the frozen D79 author argument: Sections 1--7, equations (1)--(25), all feasibility and attainment clauses, finite-support realization, actual controls, and source/scope boundaries.
The coordinating AI authored the new prescribed-mass argument.
This reviewer contributed none of its derivation and received no proof-development discussion of it before this assignment.
Shared G0001 context and the author's review request were available.
The reviewer had independently reviewed the earlier L201 and L206 arguments and contributed to or reviewed some still earlier return-law dependencies; those are disclosed reused roles, not independent discovery of those earlier inputs here.
This is a complete noncontributor review of the new argument, not a blind, human or formal audit.
No mathematical defect or required correction was found.
The entire frozen author byte prefix was preserved when this review was appended.

**Statement, actual graph and entropy lower bound.**
Every nonzero core state lies within a first-return segment of a witnessing closed word.
The positive zero loop covers the remaining state.
Thus the core and all excursion constructions have the declared original state and digit domains.
L201 supplies the exact collision radius, original probabilities, complete renewal identity and rooted positive-recurrent convention.
For nonpolynomial F, the infinitely many nonzero coefficients each contain a word of weight at least 4^(-n), whereas f_n<=1.
The root test therefore gives the claimed finite radius 1<=R_f<=4; this radius is not silently identified with R.

For an admissible Q, the positive one-step log-likelihood part is at most log4 in expectation.
For the negative part, each coordinate satisfies q log(p/q)<=p/e when q<p, so the complete row bound 1/e is valid.
Multiplying by finite mean return through occupation proves absolute integrability before applying the stopped likelihood identity (5).
For every interior z, the change from log(q(w)/p(w)) to log(q(w)/nu_z(w)) adds only the integrable length term and a finite constant.
Consequently (6) is an exact complete-word relative-entropy identity.
It neither assumes finite stationary entropy nor replaces words by their length distribution.
Taking its supremum gives the required lower bound in (4), including empty feasibility classes.

**Canonical realization on both sides of R.**
A fixed positive prefix from zero to x avoiding zero after departure injects all first-hit suffixes into first-return words.
The resulting prefix inequality bounds H_z(x) whenever F(z) is finite, even if z>R and F(z)>1.
All suffix states remain in the actual core because concatenation supplies both reachability and co-return.
First-step decomposition gives the harmonic equation off zero and the exceptional normalization F(z) at zero.
Hence both rows in (7) are stochastic.
The telescoping word probability is p(w)z^|w|/F(z), with exactly one exceptional zero departure.
Its total is one, and its mean is finite inside R_f.
All allowed core edges remain positive, so finite-mean occupation makes this whole-core law admissible and proves (8).

At a finite endpoint with finite F and first derivative, the same nonnegative prefix sums and first-step equations remain valid.
They provide the asserted endpoint law without assuming a critical invariant probability in advance.
Complete excursion probabilities determine conditional continuation rows at every positively occupied state; every state in the canonical support is occupied.
This justifies uniqueness for the interior and finite-mean endpoint laws and the equality implications used later.

**Finite words and stationary-flow mixtures.**
For finite excursion support, expected departure counts balance expected arrival counts because each word is closed.
Their union is finite and communicates through zero; averaging positive counts therefore gives an irreducible chain with invariant probability c_x/mu.
Each first-return word has exactly one departure from zero, so its stationary zero mass is exactly 1/mu even though Markovization may create additional words.
The first-return words form a prefix-free family.
Their finite prefix tree gives the stopped chain-rule identity, and the log-sum inequality at all prefixes ending at the same actual state proves (10).
For the normalized original length-n word law the word likelihood ratio is the constant 1/f_n, proving all of (11).

In (12), both flow measures are invariant, so their convex combination has the stated invariant probability and exact zero mass.
The union of the two supports remains irreducible through zero.
L206's explicit invariant-probability/return-occupation lemma applies also to this countable union and gives positive recurrence; no hidden selector state or finite stationary entropy is needed.
The row log-sum inequality, followed by nonnegative summation of bounded row divergences, gives (13).
These two realization lemmas are sufficient for the actual-state upper bounds, rather than presuming arbitrary renewal laws are already Markov laws on D.

**Full nonpolynomial frontier and unattained branch.**
Interior differentiation is justified by convergence at a slightly larger parameter.
The variance in (14) is strictly positive because length one and at least one other length occur.
Thus mu ranges continuously and strictly increasingly from one to mu_c.
The derivative 1-a mu identifies the unique interior maximizer for a_c<a<1.
If mu_c is finite, divergence of F at its endpoint would force every fixed finite length set to lose all normalized mass and hence force the mean to diverge.
With finite F, an infinite endpoint first moment has the same consequence.
Therefore finite mu_c supplies precisely the two finite quantities required by the endpoint construction, with mean R_f F'(R_f)/F_c.

For 0<a<a_c, the variational expression increases to log R_f-a log F_c.
Cauchy--Hadamard supplies an unbounded sequence of actual supported lengths, despite any support gaps, for which -log f_n/n approaches log R_f.
Markovization of those lengths supplies finite chains of zero mass 1/n and the needed cost upper bound.
The coefficient lambda_j in the text lies in (0,1) for large j and enforces mass exactly a.
Mixing with the endpoint law gives the matching upper bound in (18).
At the finite-mean endpoint, (6) is still integrable under any admissible competitor, not only the endpoint law.
Equality would require the endpoint excursion distribution, hence its mean 1/a_c.
This excludes attainment for every strictly smaller positive a and proves the exact endpoint distinction.

For finite-support approximation at an interior or finite-mean endpoint mass, truncating the canonical length law gives means increasing to the required mean and masses decreasing to a.
Its word likelihood calculation is exactly (19).
A fixed supported return length n greater than that mean has mass below a.
Mixing its finite chain with the truncated chain gives mass exactly a, with a mixing error tending to zero and uniformly bounded cost.
For the affine branch, first approximate the endpoint at its exact mass and then use the long supported lengths.
This two-stage approximation proves the finite-support equality of infima; it does not assert finite attainment or a uniform support-size bound.

**Polynomial and singleton endpoints.**
If F has maximal degree L, finitely many first-return words contain every core state, so D is finite.
Every admissible complete excursion has length at most L, giving the necessary feasibility bound.
For L>1 the canonical mean ranges strictly from one to L, proving all interior feasibility and uniqueness.
At mass 1/L the z-to-infinity lower bound is -log f_L/L, while length-L Markovization realizes the mass with at most that cost.
A competitor of mean L has all excursions of length L; relative entropy against their normalized original weights proves the asserted equality condition and uniqueness on its actual support.
For a<1/L the positive coefficient of log z forces the supremum to infinity.
The L=1 case is the singleton, and mass one always forces the deterministic zero loop with cost log2.
The z-to-zero limit has that same value.
Thus (4) includes every declared polynomial boundary, not just the canonical interior.

**Critical consequences and actual examples.**
Complete nonnegative renewal proves that F(R)<1 forces R_f=R: otherwise an interval beyond R with F<1 would give convergence of U there.
Analyticity likewise excludes R<R_f when F(R)=1 and R F'(R) is infinite.
The transient defect (21) has the correct positive coefficient A, and the finite-mean case is exactly the affine endpoint formula with a_c=F(R)/(R F'(R)).
In the null case, the normalized mean tends to infinity, so g(t)/t tends to infinity as t decreases to zero.
Choosing epsilon g(t)>t proves a strictly positive separation for every mass at least epsilon.
This proves loss of zero-state mass in both nonattaining critical cases.
It establishes neither escape at every fixed state nor a bound uniform over inputs.

The reviewer rechecked (25) directly: solving a=2s/(1+s) gives s=a/(2-a), then z=4(1-a)/(2-a)^2 and F=2(1-a)/(2-a).
Substitution into log z-a log F gives the displayed curve, with endpoint limits 0 and log2; its first derivative at zero vanishes and its second derivative is 1/2, giving the stated a^2/4 term.
L206's actual dyadic cyclotomic classification supplies the transient infinite-mean q=4 and finite-mean q>=8 examples, with R_f=R by Section 6; these are torsion controls.
Its genuine reciprocal singleton family has no small-mass feasible law.
L199's degree-six strict-strip growth conclusion and L170's original-Lehmer infinite-core conclusion supply actual infinite D for the two nontorsion examples.
Infinite D forces nonpolynomial F by the proved finite-word implication.
No enumeration was rerun or critical classification inferred from those geometric premises.

**Attribution, dependencies and conclusion.**
The reviewer inspected the Zam19 source home and directly text-read the retained PDF's title/version page, pp.3--5 and pp.15--18.
They identify arXiv1904.04602v2, 18 November 2019, and support the recorded renewal/free-energy duality, finite-mean affine segment and contact-fraction comparison.
Section 4.4 indeed assumes positive waiting probability at every positive integer; D79 allows gaps and proves its own realization and optimization.
The source LDP, its appendices and the cited original proofs are not adopted or newly audited.
L201's complete-word identity and radius conventions, L206's countable invariant-probability lemma and actual controls, and the precise L199/L170 infinitude interfaces were reused at the scopes checked above.
Earlier reviews were available as dependency history, not as a substitute for checking D79's complete new chain.

This review supports the exact prescribed-zero-mass formula (4), complete feasibility and attainment classification, finite actual-support approximation, critical zero-mass consequence and stated actual controls.
It leaves the critical return classification of the Salem inputs and every degree-uniform near-one information bound unresolved.
No new source, program, J, numerical certificate or material fingerprint was created.
Fixed adoption is the coordinator's separate action.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Entire original frozen whole](#prescribed-zero-mass-complete-independent-review) | independently reviewed |
| [Original complete author contribution and checking](#original-prescribed-mass-author-check-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Entire original frozen whole](#prescribed-zero-mass-complete-independent-review) | [Actual original frozen input](../../ledger/Yin_L_G0212_v1.md#complete-retained-proof-and-review) | Entire original frozen D79 Sections1--7/equations1--25, actual complete-word/domain/integrability/canonical-realization beyond R/finite Markovization and flow mixtures/exact feasibility/all attainment and nonattainment/finite exact-mass approximation/polynomial endpoints/critical zero-mass loss/actual controls/Salem/source/contribution and remaining limits. |
| [Original complete author contribution and checking](#original-prescribed-mass-author-check-finding) | [Actual original authored input](../../ledger/Yin_L_G0212_v1.md#complete-retained-proof-and-review) | Only the complete original authored argument and exact contribution/listed author checking quoted below, at its actual original date and scope; no new independent inspection. |

## Actual original relationship and administrative retention

Administrative retention: 2026-10-22T03:56.
The original arrangement explicitly identifies a distinct assigned resultant_research reviewer of the coordinator-authored frozen new argument, with no contribution to its derivation and no proof-development discussion of this target received before assignment.
The available earlier L201/L206 reviews and other fixed mathematical dependencies are allowed review inputs.
Shared G0001 context and the review request are disclosed without asserting unrecorded target discussion or inferring contamination from a shared-context label.
The affirmative target-specific separation is retained as the original whole independent relationship; it is not a review of a later C wrapper.
The complete original review above, its original inputs, source-reading depth, verdict and actual date remain unchanged.
This declaration and retention of the original author account perform no new mathematical review, source reading, native execution or present research Task/E.

<a id="original-prescribed-mass-author-check-finding"></a>
## Original complete author contribution and checking

Original date:2026-10-10, retaining actual day precision.
The following full original account is retained verbatim from the inspected fixed input; its pending/frozen language belongs to that original development stage.

### Contribution and author checking

The coordinating AI for Yin developed the prescribed-mass question and the local actual-graph proof in this draft.
Assigned agents did not contribute to this proof.
The classical renewal comparison is explicitly attributed above.
Author checking covered complete-word rather than length-only entropy, arbitrary missing return lengths, canonical parameters beyond the collision radius, actual-state occupation Markovization, flow mixtures without hidden states, finite-mean endpoint existence, exact-mass finite approximations, all polynomial support endpoints, uniqueness, the distinction between R and R_f, and the limits of the Salem application.
The author proof is frozen for full noncontributor review; independent review and fixed adoption remain pending.
