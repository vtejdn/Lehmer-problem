---
author: Yin
---

<a id="cr94-u001"></a>
# CR94-U001: Representation Interfaces Used by Reu96

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: [CR94, local published journal copy](../../../literature/pdf/CR94.pdf); canonical bibliographic identity is in [references.bib](../../../literature/references.bib).

Source passages: The transduction definition, normalization, equivalence order, and section hypotheses were checked directly on rendered pp. 518-522 and 524-527.

Inspection: Record: 2026-09-08, the commutator-interface source reviewer agent; primary statement and applicability checks for [Reu96 free-field source audit](../Reu96/readme.md#reu96-free-field-source-audit).

- Source: [CR94, local published journal copy](../../../literature/pdf/CR94.pdf); canonical bibliographic identity is in [references.bib](../../../literature/references.bib).
- Record: 2026-09-08, the commutator-interface source reviewer agent; primary statement and applicability checks for [Reu96 free-field source audit](../Reu96/readme.md#reu96-free-field-source-audit).
- Reading state: **Read** for the passages below; their original proofs were not independently audited.
  The entire paper is not marked audited.
- Reliance decision: **accepted external inputs** for the specified Reu96 interfaces, with the hypotheses and inspection limits below.

## Checked Statements and Assumptions

Write \(R=D_k\langle X\rangle\), \(S=D_k\langle\!\langle X\rangle\!\rangle\), and \(F(R)\) for the universal field.
A representation \((\lambda,M,\rho)\) has left family \(M^{-1}\rho\) and right family \(\lambda M^{-1}\), with left and right \(D\)-independence respectively.

Section 2 assumes finite \(X\) and \(k\subseteq Z(D)\).
Sections 3.2-4.1 additionally assume \(k=Z(D)\), \(|k|=\infty\), and \([D:k]=\infty\).

| Input | Printed / PDF locator | Selected mathematical content checked |
| --- | --- | --- |
| Proposition 2.3 | 520 / 4 | Rationality is equivalent to \(\dim_D L(f)<\infty\), where \(L(f)\) is the transduction-stable left space defined on p. 519. |
| Lemma 2.6; Corollary 2.7 | 520-521 / 4-5 | A finite stable basis constructs a normalized representation; minimal dimension equals \(\dim_D L(f)=\dim_D R(f)\). |
| Proposition 2.10 | 522 / 6 | A series representation is minimal exactly when both families are independent on their respective sides. |
| Theorem 3.2 | 525 / 9 | The canonical ring embeddings extend to \(F(k\langle X\rangle)\hookrightarrow F(R)\hookrightarrow F(S)\). |
| Theorem 4.1, minimal case | 526 / 10 | Minimal representations of the same element are equivalent: \((\lambda',M',\rho')=(\lambda P,QMP,Q\rho)\), with \(P,Q\in GL_n(D)\). |
| Corollary 4.2 | 527 / 11 | The two-family criterion also characterizes minimal free-field representations. |

The article prints result numbers within each section; the section-prefixed numbering above is the convention used by Reu96.
The transduction definition, normalization, equivalence order, and section hypotheses were checked directly on rendered pp. 518-522 and 524-527.

## Applicability to Reu96

[Reu96-U002-U002](../Reu96/Yin_U002.md#reu96-u002) use the Section 2 inputs.
[Reu96-U004](../Reu96/Yin_U004.md#reu96-u004) and [U005](../Reu96/Yin_U005.md#reu96-u005) use the free-field interfaces under the matching stronger hypotheses.

In particular, Proposition 2.10 makes a minimal normalized series representation's two families independent in \(S\).
The comparison embedding puts its free-field and series families in the same field \(F(S)\), so those families remain independent when viewed in \(F(R)\).
Corollary 4.2 then proves free-field minimality.
This is an applicability check using the accepted statements, not a new proof of their underlying representation theory.

No hypothesis mismatch was found for these finite-variable uses.
Arbitrary scalar extensions, arbitrary coefficient rings, and a replacement of right independence by left independence are outside the accepted interface.

## Acquisition and Inspection Evidence

The trigger was the critical secondary-only reference [10] in Reu96.
The [author-hosted PDF](https://reutenauer.math.uqam.ca/wp-content/uploads/2024/04/Normal-form.pdf) was downloaded on 2026-09-08; the [publisher record](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/normal-form-in-free-fields/49C8E6861D278833D2CA949D3791A1C8) independently matched the title, authors, journal, year, pages, and DOI.
The first-page identity and all 15 pages were checked.

Local text extraction and rendered-page inspection, including the original formulas and inequalities, support the table.
The PDF contains old cross-reference-pointer warnings in pypdf; extraction and rendering succeeded.
No file repair or content substitution was performed.

Search stopped once the primary statements and required hypotheses were accessible and matched their consumers.
No full original-proof review, erratum search, computation, or formal verification was performed.

Cohn's specialization lemma is restated on p. 525 but attributed there to the separate book reference [C2], Lemma 6.3.1.
This acquisition therefore does not claim primary inspection of that book's proof.
The retained book dependency remains separately visible in Reu96-U004.

## Revision Effect

On 2026-09-08, the listed [10] interfaces moved from secondary-only reporting in Reu96 to primary-statement-checked, accepted inputs.
Their original-proof status remains unreviewed; the change does not upgrade reading coverage to a full audit of CR94.

## Additional original definition reading

<a id="cr94-definition-recheck"></a>

This additional actual source-reading account was retained from L_F0062 at 2026-10-21T01:08.
This maintenance does not reopen the source or extend its original proof audit.

The free-field algebra agent reread the entire existing audit on 2026-09-10.
It freshly read and visually checked Section 2, printed pp. 518-519 / PDF pp. 2-3, and checked Section 3.1 p. 524 / PDF p. 8 plus statements on pp. 526-527 / PDF pp. 10-11 in extracted primary text.
No original normal-form proof was freshly audited.
The general free tensor-series, inverse closure, normalized/full affine representation, sided state and transduction definitions remain at the sufficient Reu96-U001/U002 homes cited by the original note.
<a id="representation-rank-convention"></a>
In Section 2, the source's rank of a series means its minimal representation dimension, not affiliated trace rank or the range dimension of an arbitrary Hilbert operator.
Normalized representations have constant matrix I; full free-field affine representations need not.
Their constant equivalence is (lambda P,QMP,Q rho), not an unqualified similarity.
The stronger Sections 3.2-4.1 hypotheses and original section-prefixed result-number convention remain those of the original checked interface.
<a id="cr94-no-additional-entry"></a>
The word rational for its formal-series scalar inverse closure is translated to division closure; it establishes no unconditional matrix rational-closure equality.
