---
author: Yin
---

<a id="ap18-u001"></a>
# AP18-U001: Standard Representation and Commutant Traces

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: Undated 338-page Anantharaman–Popa author draft, retained as [AP18.pdf](../../../literature/pdf/AP18.pdf).

Source passages: Section 7.1.1 and Theorem 7.1.1, printed pp. 97–99 / PDF pp. 103–105; Section 8.4, Proposition 8.4.2 and the following paragraph, printed pp. 127–129 / PDF pp. 133–135.

Inspection: On 2026-10-16, the standard-representation and commutant statements, the displayed trace construction, the \(M=\mathbb C\) specialization, and the orthonormal-basis statement were read from the retained PDF text.
The theorem proofs and surrounding chapters were not audited; no visual inspection was performed.

## Statement and hypotheses

Section 7.1.1 identifies the tracial GNS representation on \(L^2(M,\tau)\) as the standard representation and treats its conjugation.
Theorem 7.1.1 identifies the left and right multiplication algebras and their commutants in this representation, so the commutant of the left representation is right multiplication.
For a right \(M\)-module \(H_M\), Section 8.4 constructs a normal faithful semifinite trace \(\widehat{\tau}\) on the commutant \(\mathcal B(H_M)\), using the usual trace \(\operatorname{Tr}\) on \(\mathcal B(\ell^2(\mathbb N))\) in its displayed representation.
The paragraph following Proposition 8.4.2 states that when \(M=\mathbb C\), \(\widehat{\tau}\) is the usual trace \(\operatorname{Tr}\) on \(\mathcal B(H)\), defined through any orthonormal basis of \(H\).

## Notation and conventions

The source distinguishes the ordinary trace on \(\mathcal B(H)\) from the canonical trace on the commutant of a right \(M\)-module.
The \(M=\mathbb C\) specialization is the stated bridge between the two settings.
The commutant identity applies to the specified tracial standard representation, not to an arbitrary representation of \(M\).

## Proof mechanism and inspection depth

The standard-representation, commutant and trace statements were read at the displayed passages.
The proofs of Theorems 7.1.1 and Proposition 8.4.2 and their module-theoretic foundations were not audited.

## Limits and unresolved questions

The ordinary trace \(\operatorname{Tr}\) and the canonical module trace \(\widehat{\tau}\) are not interchangeable names for one object when \(M\) is nontrivial.
This unit does not audit other sections on module dimension.

## Additional retained tracial-conjugation source reading

The separate 2026-09-10 account below was retained from L_F0081 at 2026-10-21T01:35.
It adds the exact canonical-conjugation construction and original notation checks to this existing standard-representation home.
The source-reading date and depth differ from the separate 2026-10-16 statement-reading event recorded above; neither event certifies a whole-chapter proof or a dated 2018 source revision.
The corresponding MSY23 name and Delta convention are retained in [MSY23-U002](../MSY23/Yin_U002.md#tomita-conjugation).
No source was reopened and no original PDF bytes or acquisition facts changed in this retention.

<a id="tomita-foundational-reference"></a>
### Follow-up: Foundational Reference for the Tracial Conjugation

Date/reviewer: 2026-09-10; the coordinating agent, self-review following the user's request for a foundational reference beyond MSY23 and ACSY24.
The already registered [AP18 author draft](https://www.math.ucla.edu/~popa/Books/IIun.pdf) supplies the required construction.
Section 7.1.1, printed pp. 97-98 / PDF pp. 103-104, treats a general tracial von Neumann algebra and extends \(J\widehat{x}=\widehat{x^*}\) to an antilinear surjective isometry.
Section 7.1.3, printed p. 100 / PDF p. 106, explicitly gives \(J\pi(x)\xi_0=\pi(x^*)\xi_0\); taking the tracial GNS representation and \(\xi_0=\Omega\) gives \(J(x\Omega)=x^*\Omega\).

The source calls this the **canonical conjugation operator**.
It is a suitable foundational exposition citation, not an origin attribution; the chapter does not require a factor assumption.
Search stopped after these passages supplied the exact construction and applicable hypotheses.
Scope: extracted source text and notation checked, no independent whole-chapter proof audit.
The online 338-page draft is undated; the citation key does not verify a 2018 revision.
