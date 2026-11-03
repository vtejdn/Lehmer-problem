---
author: Yin
---

# AV09: improved nondegenerate-equation count and adoption boundary

The primary statement is read at the scope below; its external theorem is not adopted for the project by this maintenance.

<a id="av09-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: the [HAL hal-00424769v1 author manuscript](readme.md#retained-original) of Francesco Amoroso and Evelina Viada, *Small points on subvarieties of a torus*.
The source notes distinguish that manuscript from the earlier Torino locator and the published Duke edition.

Passages: Theorem 6.2 and equation (6.24), internal p. 26, PDF p. 27 of the retained HAL manuscript.
Its journal-page correspondence has not been established.

Earlier project reviews had only a primary-source search extraction and did not inspect the original theorem page or audit its proof.
The retained manuscript's statement was subsequently text-read and visually inspected at the [scope below](#retained-primary-statement).
The stronger-window project use remains conditional on the explicit shape bound.
The already inspected ESS bound remains available independently.

<a id="av09-located-count"></a>
## Exact located statement and conditional normalization

The primary PDF extraction labels the following as Theorem 6.2: over an algebraically closed characteristic-zero field K, for fixed nonzero coefficients a_1,...,a_n and a subgroup Gamma of (K*)^n of finite rank r, the equation

    sum_i a_i x_i=1,       x in Gamma,

has at most

    A_AV(n,r)=(8n)^[4 n^4 (n+r+1)]                         (1)

nondegenerate solutions.
The extracted statement's group is the tuple group, not one scalar group.
Its proof paragraph refers to ESS's algebraic-field reduction and induction; those dependencies are not audited here.

Conditional on acceptance of precisely that statement, the direct normalization already proved in [ESS02](../ESS02/Yin_U001.md#ess-normalized-power-shapes) gives, for each fixed ordered sign pattern of a minimal k-term power relation of one nontorsion alpha,

    B_k^AV=[8(k-1)]^[4(k-1)^4(2k-1)]                     (2)

normalized exponent shapes.
This substitutes n=k-1 and r=k-1.
Repeated exponents remain allowed and degeneracies still require a minimal-block decomposition.
For k=2 the elementary one-shape bound remains preferable.

Unlike the ESS expression exp(k[6(k-1)]^[3(k-1)]), (2) has log B_k^AV=O(k^5 log k).
This would materially improve growing-order consequences of a block-counting argument.
It still does not by itself establish a high-moment bound with one constant C for orders proportional to time, and it gives no direct Lehmer gap.
No assertion that (1) is the current best available bound is made.

## Project adoption and review limits

The original coordinator checked the conditional parameter substitution.
[C_G276](../../../claims/Yin_C_G0276_v1.md#conditional-polynomial-shape-window) retains the complete stronger-window proof conditional on precisely (2); it does not adopt (1) as an inspected source theorem.
The [actual original targeted check](../../reviews/Yin_R_G0534_v1.md#historical-block-conditional-targeted-finding) retains its fixed L85 input and unknown initial-context relationship; the [current whole finding](../../reviews/Yin_R_G0534_v1.md#current-block-energy-finding) is self-reviewed.

<a id="retained-primary-statement"></a>
## Primary statement in the retained HAL manuscript

The [HAL manuscript identity and pagination](readme.md#retained-original) were checked, and internal p. 26, PDF p. 27, was text-read and visually inspected.
Theorem 6.2 and equation (6.24) state exactly the candidate (1): K is algebraically closed of characteristic zero, every a_i is nonzero, Gamma is a subgroup of (K*)^n of finite rank r, and only nondegenerate solutions are counted.
The bound is (8n)^[4n^4(n+r+1)], with tuple-group rank rather than scalar-group rank.
This establishes an actual primary-statement reading beyond the original search extraction.
The surrounding proof has unresolved references in this manuscript and has not been audited.
The maintenance neither establishes edition equivalence nor adopts this theorem for C_G276; its stronger window remains an implication from the displayed sharper-shape hypothesis, and the earlier reviews retain their original inputs and limits.
