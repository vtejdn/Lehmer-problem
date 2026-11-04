---
author: Yin
---
# Jen25-U001: explicit height bound for Galois generators

Date: 2026-10-15.
Root records strategy_critique's SOURCE-only primary statement/applicability reading, used to verify the existing scope and explicit constants before evaluating a new project branch.

<a id="jen25-u001"></a>
## Read; accepted exact statement and original-degree scope

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Jonathan Jenvrin, Explicit lower bounds for the height in Galois extensions of number fields, Journal de Theorie des Nombres de Bordeaux37(2)(2025),469--477. Actual published PDF has10 pages including a cover and printed469--477.

Passages: Introduction printed469--471; Theorem1.1 and Corollary1.2 on printed471/PDF4.

Inspection: Exact primary statements, original-field hypotheses, height normalization and parameter formulas checked. No full proof audit or transfer of other source results.


Theorem1.1 assumes nonzero alpha in Qbar, not a root of unity, d=[Q(alpha):Q], and Q(alpha)/Q Galois.
It states

    h(alpha)>=10^(-8) exp[-(49/2)(log(3d))^(3/4) log(log(3d))].

For every epsilon>0, Corollary1.2 gives h(alpha)>=c(epsilon)d^(-epsilon), where

    c(epsilon)=10^(-8)3^(-epsilon)
       *exp[-181(724/(5epsilon))^4-(724/(5epsilon))^5].

The printed corollary does not repeat alpha!=0, but it follows the explicitly nonzero theorem and is accepted here ONLY on that inherited nonzero domain.
It is not interpreted to include zero.
The height is absolute logarithmic Weil height; for the original primitive minimal polynomial, m=d*h.
No prime choice, Frobenius conjugacy restriction or ramification bound occurs in these statements.
They are accepted as established exact source statements without claiming inspection of their full proofs.

This explicit result confirms that the whole original Galois-generator class already has quantitative positive Mahler bounds.
It does not allow substitution of the degree of a non-Galois Q(alpha) for the degree of a larger Galois field containing it.
The project must retain that distinction in any normal-closure or intermediate-field argument.
No automatic coverage of all original inputs is imported.

The [actual published PDF](../../../literature/pdf/Jen25--published.pdf) identifies the artifact and edition.
There is no printed contents list.
The bounded reading stopped after the exact stronger prior coverage, constants and applicable domain were established; no source-wide or original-reference proof audit is asserted.
