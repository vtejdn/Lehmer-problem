---
author: Yin
---

# Retained project review: Minimal-Frobenius local rigidity and bounded-residue mass exclusion near one

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0205_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="minimal-frobenius-local-complete-independent-review"></a>

### Complete separate noncontributor review and source attribution

At2026-10-09T19:59 the coordinating AI for Yin completed a full separate noncontributor review of the frozen Sections1--5, equations(1)--(15), reuse/contribution statements and all scope boundaries.
The assigned resultant_research AI supplied the new argument; the coordinator supplied only the broad question before this review and none of the new mathematical deductions.
The coordinator's retained dependency history includes earlier arithmetic contributions such as L72/L194/L200 and the complete review of L202.
Those prior roles are disclosed and are not recast as independent re-proofs here.
Shared Task context and the author's interim findings were available; this is not blind, human or formal review.
No mathematical defect or required proof correction was found.

The reviewer directly read L202's complete minimal-Frobenius actual quotient, L64's complete local lifting construction, L70's lattice period and conductor interfaces, L72's full ramified valuation/exponent estimate, L74's actual-field normalization and finite local table, and L78's cyclotomic inversion.
Each is used at its retained fixed scope.
The source-completeness check identified the recognized principal-maximal-ideal/DVR characterization.
Its classical attribution is now explicit: existing source The26b, official Tag00PD/Lemma10.119.7 and the retained algebra chapter Lemma119.7 on pp.285--286.
Both statement and displayed proof were directly read; foundational references were not recursively audited.
[The exact reading](../literature/The26b/readme.md#principal-maximal-ideal-dvr-attribution) identifies the existing unchanged artifact and the use as attribution only.
D72 already gives the needed complete local proof and does not gain an uninspected theorem dependency.
This source clarification adds no mathematical derivation and does not alter the frozen author text.

For Section1, taking n as the least common multiple of all nonzero reduced-root orders is prime to p and makes L202's quotient precisely the product of the distinct residue fields.
Finite free completion preserves that finite p-primary quotient.
Idempotent lifting through p-adic completeness is valid even when each local residue factor is nonreduced: the derivative2e-1 is invertible, and products/sums identify the orthogonal lifts.
A residue nonzero modulo phi has an inverse first in F_p[t]/phi^e and then in the complete local component.
Thus each component is local, and the field quotient by z identifies its actual maximal ideal with zS_phi.

The domain argument is not circular.
The nontorsion condition makes z invertible in the product of p-adic fields after inverting p, and finite freeness makes multiplication by z injective before that.
Nilpotence modulo p gives z^E in pS, so separated p-adic powers imply separated z-powers.
A nonzero element therefore has finite z-order and a unit quotient.
Injectivity then proves both uniqueness and absence of zero divisors.
Writing p=z^b times a unit and comparing the complete F_p-length gives b=e_phi with residue degree f_phi.
Inverting p inverts z, giving the component fraction field and the exact e_phi f_phi degree.
Negative valuation contradicts any monic integral equation by its unique lowest-valuation term; finite module elements are integral.
This proves the full local valuation ring and hence the completed maximal order.
The finite-index passage uses O_K/O only at the existing L70 scope.
Finally the prime-to-p unit-sum factor proves that alpha^(r_phi)-1 itself, rather than only alpha^n-1, has valuation one.

For Section2, alpha-stability and determinant norm plus or minus1 give equality alpha L=L.
Completion is stable under S, and its idempotents split each full lattice into fractional ideals.
Finite generation and a least uniformizer valuation prove principality directly.
Multiplication by the componentwise generator is a Z_p-linear isomorphism commuting with alpha, so every matrix reduction is conjugate at each finite p-power level.
The period computation retains the semisimple residue orders and all primary multiplicities; the least p-power at least e_max is necessary and sufficient.
L70's projective period is used with its own semisimple scalar convention.
No integral global conjugacy or small period follows.

For Section3, among the intermediate binomial terms the linear term has uniquely lowest valuation e+t, and the last has valuation pt.
The minimum is therefore exact unless these two tie, including p=2.
Starting at t_0=1, all steps below the threshold multiply by p.
A tie occurs exactly when e=(p-1)p^a, at s=a; its next value is strictly above the threshold even at the smallest permitted value, so every subsequent step adds e.
Nontorsion ensures the possible tie value is finite, and no upper bound is smuggled into the recurrence.
The norm sums use f times the uniformizer valuation, without an erroneous additional factor e.
L78's complete Mobius inversion gives(9) also at u=1 and s=1.
For(10), the cardinalities of every reduction modulo p^j determine the additive elementary divisors; the formula handles b=0 and exponent a=0 and is explicitly not a ring-product assertion.

For Section4, the selected reduction factors count exactly W original root indices in an algebraic p-adic splitting field.
Each individual root field has degree and ramification at most d; the proof never gives that bound to the common splitting field.
Its initial positive valuation is at least1/d.
The L72 capped binomial induction reaches one after k with p^k>=d, and then gains at least one in each of R further steps.
All roots are units, so omitted roots have nonnegative valuation.
The entire original norm at the single exponent L consequently gives gamma d(R+1)log p income.
Its full archimedean expense remains d log2+Lm.
The bound p^k<=pd yields L<=N p^(R+1)d, including d=1.
Since gamma R>=1, the remaining numerator is at least gamma d log2.
This verifies every constant, the ceiling and the original-degree normalization in(12).

For a fixed lower fraction delta, the same proof with R=ceil(1/delta) proves(14) directly, avoiding any unstated monotonicity through ceiling jumps.
Its contrapositive proves(15) along every hypothetical total-measure-to-zero sequence, with each p,F held fixed.
Without minimal Frobenius valuation the e_phi remain polynomial multiplicities; the argument needs no normality, unramifiedness or bounded power-basis index.
Under that extra condition they equal actual ramification by the independently checked first section.
No conclusion is drawn when p,F or reciprocal fraction costs grow with the input.

The complete review supports the stated maximal-order theorem, all-level lattice rigidity, exact later local profiles and additive groups, and the all-input bounded-residue-mass exclusion.
The inverse's archimedean height, near-one saturation coverage, growing residue-degree distribution, multi-prime income and exceptional tie depth remain open at exactly the stated scope.
The review used no numerical program, new J, source acquisition, material fingerprint or whole-source audit.
The preceding complete author text is preserved.
G0001 is not completed by these restricted structural and necessary-condition results.

## Original relationship declaration retained as history

The original administrative relationship table below declared independently reviewed.
It is preserved verbatim as a past declaration, not used to infer the missing initial target context or to supply the current justified relationship.
The complete original whole prose above, its03:59 completion, verdict, source reading and unchanged-author assertion are untouched.

~~~markdown
## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete local rigidity and near-one mass review](#minimal-frobenius-local-complete-independent-review) | independently reviewed |
~~~

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original whole minimal-Frobenius local finding](#minimal-frobenius-local-complete-independent-review) | unknown |
| [Original complete local-rigidity author checks](#minimal-frobenius-local-original-author-check-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original whole minimal-Frobenius local finding](#minimal-frobenius-local-complete-independent-review) | [Entire original frozen proof](../../ledger/Yin_L_G0205_v1.md#retained-local-rigidity-proof) | Original2026-10-09T19:59 whole: Entire original D72 reuse/Sections1--5/equations1--15, every actual monic irreducible nontorsion unit/every rational prime/full powered multiplicities/minimal p-resultant valuation d including repeated reduction, complete actual-order p-adic decomposition/idempotent lifts/local units/principal maximal ideals/injective z/separated powers/domain proof/p=z^e unit/full rank and residue degrees/integrality and actual completed maximal order/index/uniformizer, every full alpha-stable lattice/component fractional ideal/principal generator/all-level Z_p conjugacy/exact identity and semisimple projective periods/no global or cheap-period assertion, all exact local t0=1 binomial cases/unique-lowest-term and single tie including p2/unbounded exceptional surplus/full cyclic and cyclotomic f-weight/noextrae/all additive primary-group quotient cardinalities including a0/b0/not-ring-product/other-prime limits, separate all-input no-minimal/no-index-or-ramification-hypothesis degree-weighted bounded-residue mass theorem/full original-root counting/individual-field degree<=d rather than splitting field/initial1d/capped lift/k and R/single exponent L/full dlog2 expense/exact ceiling bound/delta proof/each fixedpF nearone necessary mass exclusion, exact The26b officialHTML and retained chapter statement/proof attribution/version/date/foundation limits/direct local proof/no new external premise, full author/source/nonexecution/period/growingdegree/tie/inverse/cofactor/multiprime/nearone/Task boundaries. |
| [Original complete local-rigidity author checks](#minimal-frobenius-local-original-author-check-finding) | [Entire original proof and complete author-check account](../../ledger/Yin_L_G0205_v1.md#retained-local-rigidity-proof) | Original2026-10-10day-precision complete author check: nonreduced completed decomposition/injectivity/separation/proved domain/ramification rank/index/full lattice and levels/binomial unique minimum and tie/full norm and Smith multiplicities/actual individual-root field versus splitting field/original bad-prime root counts/all exponent and measure costs, exact contribution/reuse/no-other-agent derivation/then-pending scope. No new historical whole event or review minute is inferred. |

## Exact retained initial-arrangement and source boundary

The original whole account before its old relationship table,03:59 completion, no-defect/no-correction verdict, source-completeness clarification and all mathematical/input/nonexecution limits remain unchanged.
The original explicit independent declaration is preserved as history above; it is not evidence establishing the initial arrangement.
The coordinator supplied the broad question and none of this target's new deductions, but shared Task context and the author's interim findings were available.
Their actual prior additional target mathematical contents and complete initial reconstruction order are not established, so the entire original whole is UNKNOWN for independent-review purposes.
Earlier L72/L194/L200 contributions and L202 review are disclosed fixed-interface history, not automatic target contribution or isolated re-proof.
The exact original951-character complete author account below remains SELF at its original day precision.
The [precise original Tag00PD reading](../literature/The26b/Yin_U005.md#the26b-u005) retains official HTML and ed88ff78/2026-07-14 chapter pp285--286 statement/displayed-proof reading, with foundational ancestors uninspected and no reading minute inferred from03:59.
It is a source-attribution clarification adding no derivation or uninspected external proof dependency to the already complete local proof.
Current authored whole SELF cannot close this UNKNOWN, turn the historical independent declaration into established isolation, or invent another historical author-review event.
No new source/PDF inspection, acquisition, program/J, native run or research Task/E occurs.

<a id="minimal-frobenius-local-original-author-check-finding"></a>
## Original complete local-rigidity author checks

Date: 2026-10-10, retaining original day precision.
The complete original contribution/reuse/listed checking/then-pending account follows.

### Contribution and author checking

The coordinator supplied only the broad round question.
The assigned resultant_research AI developed Sections1-5, with the existing results explicitly reused above.
No derivation was supplied by another agent.
Author checking includes the completed product decomposition with nonreduced residue rings, injectivity and separated powers, derivation of a domain rather than assuming it, ramification/rank equality, finite-index passage, full-lattice fractional ideals and all finite levels, the unique-lowest binomial term and single-tie exception, norm and Smith multiplicities, actual root-field ramification rather than splitting-field degree, original-root counting at bad primes, and all exponent/measure normalizations.
The author self-check is complete.
The complete author proof is ready for full noncontributor review; no independent review is asserted here.
Fixed adoption remains separate and pending.
