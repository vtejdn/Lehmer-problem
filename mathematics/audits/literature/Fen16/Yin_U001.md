---
author: Yin
---
# Fen16: real density of bounded-coefficient polynomial values

<a id="fen16-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: [Fen16.pdf](../../../literature/pdf/Fen16.pdf), De-Jun Feng, *On the topology of polynomials with bounded integer coefficients*, J. Eur. Math. Soc.18(2016),181--193, DOI10.4171/JEMS/587; published EMS journal edition,13 PDF pages.

Passages: Theorem1.2, printed p.182/PDF p.2; definition of Y_m(q) and Pisot-number convention at printed p.181/PDF p.1.

Inspection: On2026-10-10 the structural-research AI for Yin directly text-read the retained title, author, DOI, definition, theorem statement and surrounding hypotheses. The statement and its applicability below are accepted as an established external input. Coverage is Read / statement checked; the source proof and cited dependency proofs were not independently re-audited.


## Accepted statement and hypotheses

For every real q>1 and positive integer m, let Y_m(q) be the set of all finite sums sum_(i=0)^n epsilon_i q^i, where n>=0 and each epsilon_i belongs to{0,+/-1,...,+/-m}.
Theorem1.2 states that Y_m(q) is dense in the real line exactly when q<m+1 and q is not a Pisot number.
The source defines Pisot numbers as algebraic integers greater than1 whose other conjugates all have modulus strictly below1.

For every Salem beta in(1,2), there is a unit-circle conjugate, so beta is not Pisot.
Setting m=1 gives density of precisely the original {-1,0,1}-coefficient spectrum.
In particular there are nonzero such values arbitrarily close to0.
This is the accepted input for the [complete current local adaptation](../../../claims/Yin_C_G0427_v1.md#height-one-spectrum-neutral-growth).

## Proof and dependency boundary

The inspected theorem is an ordinary established external result.
The journal introduction states that Theorem1.2 follows from its Theorem1.6 and the Akiyama--Komornik characterization of finite accumulation points in Theorem1.5.
Those proofs and their references were not audited in this intake, and no independent verification of them is claimed.
There is no concrete objection or convention mismatch affecting the adopted statement.
Acceptance at this depth does not label the unit Audited within scope or supply a formal proof-assistant artifact.

The source concerns scalar real density, without an effective word-length bound.
It does not state that every unit-circle conjugate value is separately unbounded when the real value lies in(-1,1), nor that all coordinates can grow simultaneously.
The integer-norm inequality, endpoint/cocycle translation, fourth-degree conclusion and residual higher-dimensional gate are new local deductions requiring their own review.
No original-digit compact termination, actual return-core equality, entropy bound or unrestricted gap is imported from this theorem.

## Verification and downstream scope

The journal title/author/DOI/pages and exact statement were checked in retained bytes with pdftotext; the publisher metadata agrees.
The corresponding arXiv v3 statement was read online as a locator, without adopting a different artifact or broader proof coverage.
There was no numerical computation, whole-paper audit, errata survey or formal check.
Further local deductions are retained in [C_G427](../../../claims/Yin_C_G0427_v1.md#height-one-spectrum-neutral-growth); substantive changes to this source statement or its local use require a scoped reassessment.
