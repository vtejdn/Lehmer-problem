---
author: Yin
---

# Retained project review: Simultaneous root-basis experiments and complete ordering reductions

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0254_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="two-column-complete-independent-review"></a>

### Complete separately organized noncontributor review

Review time: 2026-10-10T00:43.
Reviewer: structural_research AI for Yin, assigned separately by the coordinating AI.
Preliminary reading and preparation occurred while the author finished the changed-order extension; the complete verdict and execution below concern the explicit final08:39 author freeze.
The reviewer read every part of Sections1--6 and equations(1)--(6), all nine native J55 author files, and the consumed L250, L246, D9 and L191 interfaces.
This was non-blind: the assignment and shared conversation supplied the construction question, claimed counts and limits.
The reviewer supplied none of D121's new two-column reduction, symmetry reduction, enumerations, secondary-target deductions or cost bounds.
The reviewer authored the earlier D9 signed-cover identity and previously independently reviewed D113/L246 and D117/L250.
Those upstream roles are disclosed; their retained findings are not represented as newly independent reviews of the reviewer's own derivations.
The author orbit_research did not participate in this reviewer implementation or finding.

**Finding.**
The complete proof and all finite mathematical output claims pass at the stated scope, with no mathematical defect, required author repair or unresolved consumed premise found.
The completed exclusion covers every genuine pair of replacement roots in the declared cube, all subsequent orders and independent column signs of those admitted bases, for BOTH displayed scalar targets.
It is not an unbounded two-column exclusion.
In particular the discarded3220 old single-column controls are NOT covered under arbitrary reorderings by this theorem; the final author text correctly says so.
The unbounded linear/quadratic system is an exact reduction, not a solved continuation or a modular nonexistence theorem.

#### Exact integer construction and full scalar tests

The displayed H matches the actual Q0^T G0 Q0, with Q0 integral unimodular and G0 the retained even unimodular signature(3,3) seed.
Expanding the replacement coordinate matrix along its four unchanged columns gives the signed minor c_i d_j-c_j d_i with the written order i<j.
Its being +/-1 is necessary and sufficient for an actual standard integral basis.
Both norm-two equations are necessary and sufficient for the two changed diagonal entries, while the other four already have norm two.
The mutual product is retained unrestricted.
The new upper-unitriangular reconstruction therefore has exactly the new symmetric Gram and determinant at t=1 equal to-1; no claim of preserving the prior bilinear polynomial is made.

Reciprocity, constant/leading coefficient one and p_V(1)=-1 give c0=-3-2a-2b.
The full alternating endpoint is Pf^2=5+4b.
Consequently the conditions a=-2,Pf=+/-3 determine every coefficient of Phi6 P4, while a=0,Pf=+/-1 determine every coefficient of S6.
These are full polynomial equivalences, not truncated coefficient comparisons.
The sign in a=tr(V^(-1)V^T) agrees with p_V=det(tI+V^(-1)V^T).
Column signs give V -> D V D with D diagonal +/-1, preserving the original polynomial and leaving the absolute companion unchanged.
Every root used in the finite test has actual G0-norm two; its path coordinates are the exact suffix sums because Q0 is the unit upper-bidiagonal difference basis.
No rational relaxation or fractional module is used.

The fixed-first-root continuation(4) was separately checked.
With c fixed, ell_c(d) is linear, each alternating perfect matching uses the varying row/column once and hence Pf_c(d) is linear, and each determinant term meets at most that row and that column, so a_c(d) has degree at most two.
The imposed diagonal of V remains one during this polynomial calculation; d^T H d=2 supplies the separate admissibility condition.
Independent linear equations leave four rational parameters, but integrality and divisibility constraints remain.
Dependent and inconsistent cases are explicitly retained.
This exact interface neither solves the quadratic system nor extends the finite residue observations to arbitrary integer roots.

#### Ordering, sign normalization and the precisely covered finite class

The actual signed reflection-product identity from L246 is applicable to every ordered norm-two basis here.
Each individual reflection squares to the identity, independently of whether the entire Gram form is degenerate.
Cyclically shifting a product of invertible reflections conjugates it.
Reversing their order gives its inverse.
The determinant of this six-reflection product is one and the characteristic polynomial is reciprocal, so reversal preserves the full polynomial.
For the absolute companion the Gram is2 on the diagonal and -|G_ij| off it, and the identical coordinate-update identity applies.
Its reflections are likewise invertible even for a degenerate full form.
This proves the two symmetries simultaneously for the complete original AND companion polynomials, not merely for the first coefficient or Mahler measure.
Literal-cover factorization and costs inherit that invariance.

Every cyclic orbit of six distinct labels has one representative beginning with0.
Reversal on that120-element set has no fixed point, so the exact number of representatives is60.
Independent signs can be normalized by the first nonzero coordinate; an admitted basis has no two columns equal up to sign.
Sorting the six normalized columns therefore gives a genuine finite unordered-basis key, and all its orderings/signs are covered by the60 representatives and the proved sign invariance.
The sign action on the two nonzero inserted roots is free with four choices, explaining the cap61516/4=15379.
Additional overlaps can only decrease the number of keys; the exact7446 is separately verified below.

The filter declaring a pair genuine removes a candidate whenever either inserted column equals its own old column up to sign.
L250 excludes those old controls only at its fixed-order target scope.
It does not exclude their arbitrary reorderings or automatically exclude S6.
The final D121 and J55 explicitly restrict the changed-order theorem to the genuine class, so no inadmissible extension of L250 occurs.
A key may have more than one genuine representation, which is exactly what deduplication handles; no excluded representation is needed to prove the coverage asserted here.

#### Independent completeness and coefficient verification

The reviewer created and actually ran only [review_independent.py](../../computations/programs/Yin_J_G0055/review_independent.py) and its review_result.json (`mathematics/computations/outputs/Yin_J_G0055/review_result.json`).
No author implementation is imported, called or re-executed.
The program independently enumerates all729 cube vectors and obtains exactly the same114 actual roots.
It constructs every one of194940 ordered replacement pairs and uses a FULL six-by-six integer Bareiss determinant of the actual basis for admission, checking that it equals the author's two-coordinate minor in every case.
This independently validates both the shortcut and every admitted/excluded case.

For signed Pfaffians the checker starts from the6! alternating-permutation definition, sorts each pair with its sign, and collects exactly15 perfect matchings, each with coefficient +/-48 before the defining division by48.
It does not call the author's recursive Pfaffian.
For all11248 fixed-order target-Pfaffian candidates it computes the full reciprocal degree-six polynomial using scalar Bareiss evaluations at t=2,3 and the verified endpoint e=p(1).
Explicitly, if u=p(2),w=p(3), then

    a=(w-9u-235+45e)/30,
    b=(u-49-8e-18a)/4,
    c0=e-2-2a-2b.

Every division is checked exact.
With e=-1 this recovers the original whole polynomial.
For absolute companions the separate scalar determinant at1 supplies their actual e.
The method differs from both the author's triangular-inverse first-coefficient calculation and the author's subset polynomial expansion.
Each recovered original polynomial is also checked at-1 against the independent signed Pfaffian square.

The complete first-run counts match exactly:194940 pairs,64736 unimodular,3220 old controls,61516 genuine and11248 target-Pfaffian, with no target.
Every root entry, every position-specific counter and the full signed-Pfaffian histogram agrees.
The checker reconstructs all7446 normalized unordered bases independently.
It forms dihedral classes from ALL720 permutations rather than using the author's first/last-label filter; every orbit has12 elements and there are60.
The resulting complete446760 ordered representatives have79867 cases with |Pf|=3 and71095 with |Pf|=1.
It recovers ALL150962 corresponding full polynomials with the determinant method above.
Every coefficient-frequency histogram and every zero-target conclusion matches the saved output.
Thus the absence claims are not accepted merely because the author's exact code returned no hits.

All energy bins over the7446 bases match, including the full range17--69 and maximum entry height3.
The observed missing residue classes a=2 modulo4 for |Pf|=3 and a=0 modulo4 for |Pf|=1 were checked against the complete coefficient histograms.
They remain finite observations at precisely that scope.
This program supplies no unbounded modular-lifting theorem from them.

A separately declared deterministic symmetry check used25 bases (the first12, last12 and middle key) and all720 labelled orders.
It checked36000 full original/absolute polynomials, their dihedral equality, and each polynomial again at t=4 by a scalar determinant.
This finite sample corroborates the general written symmetry proof; the proof, not that sample, covers all bases and degenerate companions.

The reviewer also checked EVERY mathematical payload in the added author verifier.
Its three stored actual bases, labels, norms, determinant signs, Grams, original/absolute polynomials, energies and complete rank12 cover polynomials were reconstructed.
Its4320 degree-six/order checks were performed with the different scalar-determinant method.
The three literal covers were built directly, their energy doubling verified, and their full product coefficients compared with the saved lists.
Thirteen distinct integer determinant evaluations per cover,39 in total, independently prove each full degree-at-most12 identity.
These are additional independently executed checks, not a claim that the author's self-verifier was already independent review.

The complete independent calculation passed at the mathematical scope described above.
D121 is not a mathematical input; the checker remains runnable after its retirement.

#### Secondary scalar, full costs and source limits

The local trace identity S6=t^3[(t+t^(-1))^3-4(t+t^(-1))-1] was expanded directly.
The only possible rational roots of its monic trace cubic are +/-1, and neither is a root.
Its values -1,2,-1,-1,89/64 at -2,-1,0,2,9/4 place exactly one simple root in each of the three disjoint intervals stated by the author.
The trace field is totally real.
Negative values of u^2-4 at its first two real embeddings exclude a square, and the quadratic extension together with u=t+t^(-1) inside Q(t) proves degree-six irreducibility.
The full root configuration therefore consists of the positive reciprocal exterior pair and four nonreal unit-circle roots.
No cyclotomic factor is removed.
Since sqrt13>7/2, u4>9/4, so monotonicity of t+t^(-1) for t>1 gives the strict comparison lambda<beta4.
This proves the scalar target is smaller without claiming that any tested matrix realizes it or that it is minimal in its degree.

Every admitted original matrix has p_V(1)=-1 and positive monic leading term, so the intermediate value theorem gives a real root greater than one and positive complete measure.
The absolute polynomial remains monic with nonnegative Mahler measure.
For any ordering, the entry multiset gives height at most3 and the recorded energy.
On the unit circle each determinant entry has modulus at most3, including the diagonal bound2, so the6! expansion is bounded by720*3^6=524880.
The logarithmic-integral formula yields the written coarse bounds, with integrable circle zeros.
These are upper bounds, not exact measures or energy substitutes.

The literal cover has rank12, height at most3 and exactly twice the energy.
Its sheet decomposition gives the ENTIRE original times ENTIRE absolute polynomial, retaining every neutral or repeated factor and ordinary unnormalized additive measure.
The reviewer authored that older D9 identity and checked its consumed orientation/sign convention here; this is not mislabeled an independent re-audit of that older proof.
The unchanged L191 k=4 control has rank6/height1/energy5 and Phi2^2 P4 with identical companion; its cover has rank12/height1/energy10 and Phi2^4 P4^2.
The L246 different sextic and its high companion/cover ratios remain at their already completely reviewed scopes.
No new target was found and no unknown target companion is assigned a small value.

The prior HPM22 conference attribution is reused at its exact retained passage scope; the displayed seed identity is direct integer algebra.
No new conference existence/classification theorem, Coxeter gap theorem or E8 theorem is required.
The McMullen and Lanneau--Thiffeault web snippets remain explicitly unadopted discovery leads.
This review does not verify their identity, page, attribution or minimality scope from snippets, and none is a premise of the locally proved scalar facts.
The author's failed optional PDF extraction is preserved as an operational access boundary, not concealed as a completed source inspection.
No new source acceptance or source-wide proof audit occurs.

#### Disposition

The complete finite theorem, general ordering invariances, exact unrestricted-second-root reduction, local secondary-target facts, recorded executions and full cost boundaries are valid at their stated scopes.
There is no author correction or unresolved mathematical premise.
The next unbounded congruence/elimination test, three-column changes, arbitrary changes of lattice and general near-one coverage remain open.
Repeating the same7446 bases/orders cannot change these exact finite outcomes, but their failure neither excludes all two-column integer replacements nor suspends other routes.
G0001 remains active and unresolved.
This completed independent review is separate from subsequent coordinator adoption, fixed retention and navigation/retirement work.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original complete finding](#two-column-complete-independent-review) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original complete finding](#two-column-complete-independent-review) | [Original entire L254](../../ledger/Yin_L_G0254_v1.md#complete-retained-proof-and-review) | Complete final08:39 Sections1--6/equations1--6, all genuine finite roots/bases/orders/signs, both targets, unrestricted integer interface, secondary scalar, complete factors/costs and source/execution/contribution limits. |
| [Original complete finding](#two-column-complete-independent-review) | [Original J55 group](../../computations/programs/Yin_J_G0055/readme.md) | Every nine native author files, their exact original mathematical payloads, complete729-vector/194940-pair/7446-base/446760-order checks, all counts and histograms. |
| [Original complete finding](#two-column-complete-independent-review) | [Original distinct reviewer program](../../computations/programs/Yin_J_G0055/review_independent.py) | Original no-author-import full basis Bareiss, alternating-permutation Pfaffian, scalar determinant interpolation,25-base symmetry and entire three-cover/sample domain. |
| [Original complete finding](#two-column-complete-independent-review) | [Original fixed-order one-column input](../../ledger/Yin_L_G0250_v1.md#unbounded-path-column-fixed-scope) | Exact original full reciprocal target/endpoint and fixed-order one-column control only; no arbitrary-order or S6 extension. |
| [Original complete finding](#two-column-complete-independent-review) | [Original conference seed/interface](../../ledger/Yin_L_G0246_v1.md#rank-six-root-basis-discovery) | Consumed actual G0/Q0/norm/reflection and HPM22 attribution boundary, original changed sextic/full companion costs, not a new source-wide proof audit. |
| [Original complete finding](#two-column-complete-independent-review) | [Original D9 signed cover](../../claims/Yin_C_G0002_v1.md#signed-cover-identity) | Exact consumed block/sign convention and full sheet factorization; the original reviewer authored this upstream identity, not newly independently re-audited here. |
| [Original complete finding](#two-column-complete-independent-review) | [Original achieved quartic comparison](../../ledger/Yin_L_G0191_v1.md#irreducible-quartic-gram-family) | Actual rank6/height1/energy5 Phi2^2 P4, identical companion and rank12/height1/energy10 full cover comparison. |
| [Original complete finding](#two-column-complete-independent-review) | [Output of the recorded run](../../computations/programs/Yin_J_G0055/readme.md#recorded-runs) | Whole original executed result:11248 and150962 full target-Pfaffian polynomials, all finite histograms,36000 symmetry polynomials,4320 author-sample polynomials and39 cover values. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0055/review_result.json`; this target locates that original run's computation account. |

The original record explicitly states that the assignment/shared conversation supplied the construction question, claimed counts and limits before this complete finding.
That known substantive target context makes the whole original finding SELF.
Its separate implementation, no contribution to the target derivations and original noncontributor execution account remain true; upstream D9 authorship/prior reviews alone are not the classification reason.
The original date, verdict, complete mathematics, every negative/source boundary and actual execution scope are unchanged.
These bindings stay on the actual original inputs; no later C or present replay is backdated into the finding.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
