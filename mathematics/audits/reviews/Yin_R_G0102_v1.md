---
author: Yin
---

# Retained project review: Bounded-measure interlaced realizations with unbounded irreducible degree

These are the original review accounts relocated from [the inspected material](../../ledger/Yin_L_G0203_v1.md).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="pendant-chain-complete-independent-review"></a>

### Complete separate noncontributor review

At 2026-10-09T19:39 the assigned resultant_research AI for Yin completed a separately organized review of the frozen D70, all Sections1-6, equations(1)-(10), all-parameter conclusions and boundaries, together with the complete J42 verifier and retained output.
The orbit_research AI authored all new mathematics and the coordinator supplied only the broad question.
This reviewer contributed no D70 derivation.
The reviewer authored the earlier L175 block-Gram trace obstruction, which is reused at its fixed scope here; that is disclosed prior dependency work, not an independently rediscovered result of this review.
Shared Task context and the author's freeze/scope explanation were available.
This is a full noncontributor written and computational review of the new argument, not a blind, human or formal review.
No mathematical defect or required correction was found.

**Determinants, actual presentations and cover.**
The leaf expansion has one diagonal contribution and one transposition contribution, the latter exactly minus t times the principal deletion determinant.
This gives the first attachment and subsequent two-term recurrence, including the k=0 initial condition.
Substitution of the geometric sum C_k proves(1).
Reversal at the core's degree d is necessary for p-q: its zero constant coefficient gives the exact t factor and moves the actual seed to degree three.
For the displayed interlaced core, the L196 determinant is p=t^4+7t^3+16t^2+7t+1 and the deleted tree has two weights of magnitude2, giving q=t^3-5t^2-5t+1.
Thus p-q=tH and p-tq=H^*, with the stated H.
For the absolute core, the sign of the full cycle changes while the deleted tree stays the same; r-q=tJ and r-tq=J^*.
Equations(2)-(3) are consequently the full degree k+4 determinants, including constant term one, rather than chosen factors.
Reversal of any tV+V^T determinant proves their reciprocity.
There are k new unit edges, so rank, maximum entry and squared-entry sum are exactly k+4,3,k+21.
The reviewer checked D9's actual two-sheet convention: its invariant equal/opposite sheet subspaces give V^- and V, with no normalization.
Every edge is doubled, so the full cover has determinant p_k r_k, rank2k+8, unchanged height3 and energy2k+42.

**Degree six and all-k original roots.**
Substituting t+t^(-1) directly produces(4).
The positive derivative and endpoint values give one real trace in(-2,-1), and no integer root, hence irreducibility of U.
In its cubic field the real embedding makes u^2-4 negative, so the quadratic discriminant is not a square in that field.
The quadratic extension has degree two and proves irreducibility of the entire degree-six p_2.
Its two nonreal traces give the two complex expanding roots and their reciprocals; the real trace gives the remaining unit-circle pair.

For a monic real F without circle zeros, the e<1 comparison has degree N+deg F throughout and strict boundary inequality.
Rouche therefore counts N plus the interior-root count of F inside the unit circle; the complement has exactly F's exterior count.
At e=1 every strictly exterior root persists locally with multiplicity, proving the upper bound without making an assertion about roots landing on the circle.
The small exterior-disk argument also correctly retains each limiting multiplicity and requires no integral limit interchange.

For H, its strictly positive derivative and the rational endpoints locate the only real root at -alpha, 2/3<alpha<3/4.
The product of the other two roots is12/alpha>16, so they both have modulus greater than4.
The |t|=2 product bound is strictly greater than5, and |H^*|<=193.
For every N>=6 this gives exactly two roots outside radius2, since t^N H has just one seed root inside that radius.
The real-axis exclusions have the correct signs: H and H^* are both negative at -r for r>=2; the displayed lower/upper magnitude bounds give a ratio at most(9/4)r^2<r^N for even N>=4, while odd N gives a positive numerator.
The positive half-line follows from N>=2 and the positive k=0 polynomial.
Thus those two exterior roots are nonreal.

For the four smaller N, the displayed quartic/quartic/cubic/cubic trace controls cover precisely k=0,1,2,3.
The cubic real roots and their products give the stated nonreal trace modulus bounds, all strictly greater than5/2.
A root of modulus between1 and2 has trace modulus at most5/2, and each nonreal trace has one expanding member of its reciprocal pair.
Hence each control has two nonreal roots beyond radius2.
Combining this lower count with the general upper count proves exactly two simple conjugate expanding roots at every k.
Reciprocity gives exactly two contracting roots, and all remaining k roots are on the circle with multiplicity.
The full logarithmic measure is therefore2 log R_k>log4; no neutral root has been silently removed.

**Absolute roots and irreducible-factor coverage.**
The exact negative discriminant of J and its signs at41,42 put the sole real root rho there; its conjugate pair has squared modulus36/rho<1.
Hence J has exactly one exterior root and no circle zero.
The preceding bound gives at most one exterior root for r_k, while the differentiated identity r_k(1)=-56k-64 and monicity force a positive root above1.
This is the one exterior root, simple, and reciprocity accounts for its contracting reciprocal and all other circle roots.
Thus m(r_k)=log rho_k counts the complete absolute determinant without an irreducibility assumption.

Gauss's lemma makes every monic rational factor of p_k integral with constant term plus or minus one.
An irreducible factor containing one nonreal expanding root must contain its conjugate.
Absolute norm one then forces both contracting roots into that same factor, because their moduli are the only moduli available to cancel R_k^2.
This proves uniqueness of the positive-measure irreducible factor, and the exact exterior multiplicity proves it occurs once.
Its monic reciprocal shares a contracting/expanding root, hence is the same irreducible polynomial.
It has no rational root plus or minus one; reciprocal pairing therefore gives constant term one.
Every other irreducible factor has all roots on the circle and is cyclotomic by the usual monic integral criterion.
This proves(7) including all multiplicities and the degree bound, not a classification of the individual cyclotomic orders or an assertion that all k circle roots are cyclotomic factors.

H is irreducible because its only real root lies strictly between-1 and0.
Its reciprocal is irreducible over Q and cannot be its scalar multiple, so their gcd is one.
At a common root of two different p_k, neither seed evaluation can vanish, and division of the two numerator identities gives a root of unity.
In particular their positive-measure irreducible factors are pairwise distinct.
The coefficient bound from elementary symmetric functions and the common measure bound makes the set of bounded-degree monic integral possibilities finite.
Distinctness therefore proves unbounded irreducible degrees.
This does not prove equality with presentation degree or bounded cyclotomic degree.
Every such factor has nonreal traces from its nonreal off-circle roots, so the exact L175 real block-Gram trace restriction excludes divisibility even after further cyclotomic multiplication.

**Full costs, limits and coverage limits.**
The unit-circle triangle inequality integrates to m(p_k)<=m(H)+log2 and m(r_k)<=m(J)+log2; the finite zeros have integrable logarithms and the divided factor t-1 has measure zero.
Here M(H)=12/alpha and M(J)=rho, which gives exactly the bounds in(8).
Combining them with R_k>2 gives the stated bound on extra/original cost and the total cover bound log3024.
Exterior roots approaching the two roots of H and the one root of J exhaust all possible exterior roots because the counts were already exact.
This proves all limits and the ratio in(9), with no hidden tail of exterior roots, rate or monotonicity claim.
The coefficient formula(10) follows from the exact numerator and includes k=2 without an empty or overlapping middle range.
All coefficients are positive, including the separately displayed k=0,1 cases, so no positive real root can occur.
This excludes every stated Salem target from this fixed family even with a cyclotomic multiplier.
Finally the leaf recurrence preserves the next-to-leading coefficient because its two new leading contributions cancel.
These are genuine limitations of this construction, not restrictions proved for all integral interlaced presentations.

**Source and execution scope.**
The reviewer directly read Hir06's retained source record and registry entry and printed pp.505-506 (PDF pages10-11), including Lemmas10-11 and Theorem12 and their relevant proof steps.
They support the stated established Salem-Boyd exterior-root/convergence attribution.
The proof under review uses the fully written no-circle-zero argument for the two actual seeds; no topological realization or sign transfer, general reciprocal-factor-removal proof, angular theorem, monotonicity theorem or complete source audit is adopted.
L196's core determinant and D9's cover were checked at their displayed interfaces; unrelated earlier arguments and computations are not recertified here.

The complete J42 verify.py was inspected and rerun.
Its write to verification.json was intercepted in memory, and every resulting mathematical JSON field agreed exactly with the retained author output.
All assertions for fourteen actual matrices at k=0,...,6 passed, including the formulas, costs, reciprocity, degree-six irreducibility/trace checks, k=3 trace control, seed discriminants/signs, gcd and endpoint checks.
This uses the author's checker with the same installed SymPy backend, not an independently implemented algebra system.
The finite run supplements the separately checked all-k proof; it does not certify unspecified all-k factorizations.
No new program, output artifact, source intake or J was created.

This complete review supports the new pendant-chain family, exact all-k root and factor structure, unbounded positive-factor degrees, bounded full measures and explicit coverage obstruction at precisely their stated scope.
It establishes no arbitrary prescribed-input realization, small-total-measure family, optimized universal cover cost or unrestricted G0001 gap.
Fixed adoption remains a separate coordinator action.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original whole pendant-chain finding](#pendant-chain-complete-independent-review) | unknown |
| [Original listed pendant-chain author checks](#pendant-chain-original-author-check-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original whole pendant-chain finding](#pendant-chain-complete-independent-review) | [Entire original fixed chain proof](../../ledger/Yin_L_G0203_v1.md#retained-pendant-chain-proof) | Original2026-10-09T19:39 whole: Entire original D70 reuse/Sections1--6/equations1--10, arbitrary integral upper-unitriangular core/selected deletion/all k>=0 actual unit-edge chain and degree-correct reversal/t cancellation, fixed H/J seeds/full original and absolute determinants/ranks/heights/entry energies/full signed two-sheet factor, actual p2 irreducible degree6/nonreal trace and entire no-circle-zero Rouche/exterior multiplicity proof/radius2/real half-lines/all four small-k controls/exact all-k expanding and circle-root counts, unique positive reciprocal irreducible factor/entire cyclotomic multiplier with multiplicities/degree bounds/pairwise distinctness/unbounded degree by coefficient finiteness, complete full measures/uniform bounds/positive limits/extra-original ratio/no rate or monotonicity, complete positive coefficients/no-positive-real-target and next-leading-preservation obstruction, all14 original J42 actual matrix/coefficients/factors/cost/trace/gcd/sign finite evidence and same-implementation reviewer replay limits, exact Hir06 published two-occurrence source/version/pagination/sign-convention/attribution-not-full-audit scope, original author/contribution/source/native/all-k-versus-finite/near-one/Task and remaining-cost boundaries. |
| [Original listed pendant-chain author checks](#pendant-chain-original-author-check-finding) | [Original proof and complete listed author-check account](../../ledger/Yin_L_G0203_v1.md#retained-pendant-chain-proof) | Original2026-10-10day-precision formula derivation/checking and exact J42 author execution, complete Hir06 attribution/acquisition distinction/fixed reuse/broad coordination/then-pending account. No second historical whole author-review event or source-proof scope is invented. |

## Exact retained arrangement, source and execution boundary

The original11030-character118-line complete whole account,03:39 completion, no-defect/no-correction verdict, all mathematical/all-k/finite/source/input limitations remain fixed.
Orbit_research authored the target and resultant_research supplied no target derivation.
Shared Task context and the author's freeze/scope explanation were available.
Their actual initial additional target mathematical contents and reconstruction order are not established, so the entire original whole relationship is UNKNOWN for independent-review purposes.
Earlier L175 block-trace authorship is disclosed fixed input, not automatic target contribution or an independent rediscovery of that prior proof.
The complete old computational review reran the same author J42 checker with the same SymPy backend and intercepted output; it was not an independently implemented algebra system.
The finite14-matrix replay supplements the separately recorded all-k proof, without all-k factorization certification.
The original Hir06 reader/page/depth distinctions remain at [Hir06-U001](../literature/Hir06/Yin_U001.md#hir06-u001), without a new reading.
Current authoring/SELF cannot establish old isolation or fabricate another historical whole review.
No new source/PDF inspection, acquisition, program/J, native run or research Task/E occurs.

<a id="pendant-chain-original-author-check-finding"></a>
## Original author contribution and listed checks

Date: 2026-10-10, retaining original day precision.
The exact original source-role/contribution/fixed-input/formula/program-check/then-pending account follows.

The selected Hir06 comparison was acquired through the source writer after checking the declared flat PDF destination and existing identity.
Its source-local reading record and sole registry retain the published artifact and actual inspection limits.
The general Salem-Boyd form, exterior-root bound and convergence are established background; the new local contribution is this explicit interlaced plus-sign realization, exact cubic pair, all-k root exclusion and full factor/cost/coverage analysis.
The coordinator assigned only the broad question and supplied no derivation.
Earlier L196/D9/L184 inputs retain their original contributions and reviews.
The author derived and checked every new formula and wrote/executed the exact J42 certificate; complete noncontributor review and fixed adoption remain pending.
