---
author: Yin
---

# NV11: fixed-parameter inverse concentration and the exponential-range boundary

Date: 2026-10-07.
Bounded source-statement and applicability inspection by assigned AI ms25_source for Yin, within [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).

<a id="nv11-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Hoi Nguyen and Van Vu, *Optimal inverse Littlewood-Offord theorems*, Advances in Mathematics 226(6) (2011), 5298--5319, DOI `10.1016/j.aim.2011.01.005`. Retained [NV11.pdf](../../../literature/pdf/NV11.pdf) is the public author's `optimalILO-final.pdf`, 23 internally paginated pages, 300527 bytes. It has no verified source-upload date or numbered revision label; its PDF creation timestamp is not treated as a publication/version date. It is not asserted byte-identical to either the publisher PDF or arXiv:1004.3967v2. The latter is a separately checked identity/version locator, revised 16 January 2011.

Passages: Main paper: definitions and fair-sign convention, internal/PDF pp.1--4; Theorem2.1 p.6 and Theorem2.5 p.7. Associated author erratum: introduction pp.1--2, particularly the final paragraph before Section2 on p.2.

Inspection: The title/authors and journal identity were checked against the retained source and author's bibliography. Both theorem statements were extracted and visually read. The corresponding fixed-parameter/rank/exception interpretation was checked, but the inverse-theorem proofs were not audited. The erratum's declared correction target was read and visually checked on p.2; its repair proof was not audited. No continuous inverse result or general-noise extension is adopted.


**Read at statement and applicability depth.**
This unit records why the displayed fixed-parameter results do not supply the proposed uniform exponential-range conclusion.
It neither identifies an error in those theorem statements nor upgrades them to a proof audit.

<a id="nv11-fixed-parameter-interface"></a>
## Exact screened statements

For an indexed multiset V=(v_1,...,v_n) of integers, let eta_i be independent fair signs and put

    rho(V)=max_x P(sum_i eta_i v_i=x).

A generalized arithmetic progression of rank r is the image of a finite integer box under an affine map with r generators.
It is symmetric when the base point is zero and the coefficient ranges are symmetric; it is proper when its integer-box parametrization is injective.
The number r is a progression parameter, not automatically the rational rank of its elements.
All exception counts below include multiplicity.

Theorem2.1 fixes C>0 and 0<delta<1.
Under rho(V)>=n^(-C), it gives a proper symmetric progression Q of rank r=O_(C,delta)(1), with at most delta n weights outside Q, and

    |Q|=O_(C,delta)(rho(V)^(-1)n^(-r/2)).                 (1)

Theorem2.5 fixes the same types of constants.
For every integer n' with n^delta<=n'<=n, it permits at most n' exceptional weights, with rank O_(C,delta)(1) and

    |Q|=O_(C,delta)(rho(V)^(-1)(n')^(-r/2)).              (2)

The source's epsilon has been renamed delta to avoid confusion with the exponential concentration exponent below.
The original fair-sign and fair-bit sums are injectively affinely related in a torsion-free group: sum eta_i v_i=2 sum X_i v_i-sum v_i.
Their atom probabilities agree.
This conversion does not alter the source's quantifiers on C or delta.

<a id="nv11-exponential-screen"></a>
## Why this does not supply the required uniform rank

For the proposed hypothesis rho>=exp(-epsilon n), rewriting the threshold as n^(-C) sets C=epsilon n/log n when n>1.
This C grows with n for a fixed epsilon>0.
Both the displayed rank bound and the size constant depend on C; the source statement supplies no control uniform in this substitution.
If the theorem uses an implicit lower threshold on n depending on C, that threshold also cannot be suppressed.

Thus neither (1) nor (2) proves that an exponential-concentration family has bounded progression rank independently of n.
Substitution may produce a bound depending on n; it is not an input-independent constant.
No theorem with explicit dependence on C is ruled out by this statement inspection, and no claim about the best available inverse theorem is made.
The direct generic rank obstruction and power-orbit time cost are separate local arguments in [C G0287](../../../claims/Yin_C_G0286_v1.md#generic-exponential-rank-obstruction); they do not rely on the truth of (1)--(2).

<a id="nv11-erratum-scope"></a>
## The linked erratum has a different target

The author's bibliography links [NV11--erratum.pdf](../../../literature/pdf/NV11--erratum.pdf), titled *Erratum for "Inverse Littlewood-Offord Problem"*, by Hoi H. Nguyen and Van H. Vu.
The retained five-page author artifact has 238854 bytes .
Its upload date and separate journal-publication status were not established.

The introduction identifies the incomplete deduction as the continuous Corollary2.10 from Theorem2.9 in the original AppendixB, specifically an approximation property of a progression in its Case2.
It supplies a replacement argument.
The inspected scope declaration does not change the discrete statements (1)--(2).
This is only an identification of the declared correction target; no claim that the full paper is error-free or that the erratum proof has been verified is made.
The erratum and main paper are separate retained artifacts of the same selected work, rather than two new research inputs.

## Actual review and use

The search was limited to inverse concentration at rho>=exp(-epsilon n), after reusing L G0088 and Li26.
The coordinator selected this one work for retaining the exact rejected-use evidence.
The drafting agent checked the statements, fair-law convention, rank/exception dependencies, artifact identity and declared erratum scope as recorded above.
No source-proof acceptance, recursive reference audit or numerical computation occurred.
The coordinator independently read the complete source unit, inspected the original PDF text at the stated definition scope, and visually checked the retained original pages 6 and 7 and erratum page 2.
It verified the fixed-C rank/size dependencies, multiplicity and exception quantifiers, fair-sign conversion and the declared continuous correction target.
No substantive defect was found.
This is a bounded statement/applicability review, not verification of the inverse theorem proofs or the erratum repair.
