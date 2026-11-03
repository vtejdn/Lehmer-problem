---
author: Yin
---

<a id="sin07-u001"></a>
<a id="sin07-fixed-degree-continuity"></a>
# Sin07-U001: Fixed-degree continuity of Mahler measure

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Christopher D. Sinclair, *The range of multiplicative functions on C[x], R[x] and Z[x]*, arXiv:math/0509591v2, 13 July 2007, 41 pages. The online PDF version strip was checked. The related journal DOI does not establish journal/preprint identity.

Passages: Introduction, axioms A1--A4 on p. 1; Mahler example and Theorem 1.1 on p. 2; Jensen equation (1.2) on p. 3; Section 2, pp. 12--14. Printed and PDF page numbering coincide.

Inspection: 2026-10-13T06:31, human author Yin; the assigned F0010 coefficient-dependence AI read the named statement, example, and Section 2 online. This is attribution and applicability inspection, not an independent audit of the whole source proof.


Access: [versioned arXiv PDF](https://arxiv.org/pdf/math/0509591v2).
The coordinator's bounded artifact attempts failed with DNS resolution error 11001; the registered local PDF is unavailable.
No retained artifact or hash is claimed.

## Exact result and application

The source defines a multiplicative distance function on complex polynomials to be continuous on each finite coefficient space, positive except at the zero polynomial, absolutely homogeneous, and multiplicative.
Theorem 1.1 states, in its converse direction, that a continuous positive function psi on C satisfying psi(gamma)/|gamma| -> 1 as |gamma| -> infinity determines such a function by

\[
\Psi\!\left(c\prod_j(z-\gamma_j)\right)
=|c|\prod_j\psi(\gamma_j),\qquad \Psi(0)=0.
\]

Taking psi(gamma)=max(1,|gamma|) recovers Mahler measure.
The source separately identifies this example and attributes its continuity to Mahler's 1961 paper.
Jensen's equation (1.2) matches the logarithmic circle integral.
The F0010 application fixes the coefficient interval and removes a Laurent monomial, which does not change the measure.
Thus degree drops and the zero coefficient vector are inside the finite-dimensional continuity statement.

This unit supplies established-result attribution.
The consuming [coefficient account](../../../claims/Yin_C_F0007_v1.md#coefficient-global-continuity) supplies its own compact-factor proof including the zero vector and does not present continuity as a new project theorem.
It does not use the stronger unbounded-degree compact-open assertion discussed in Section 2, any distribution-volume formula, or the source's potential-theoretic capacity constructions.
No claim of earliest attribution or independent inspection of Mahler's 1961 original is made.
