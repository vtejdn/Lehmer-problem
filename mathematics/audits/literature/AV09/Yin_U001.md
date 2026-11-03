---
author: Yin
---

# AV09: located improved nondegenerate-equation count and access boundary

Date: 2026-10-07.
Bounded follow-up by assigned AI ms25_source for Yin.
This source unit records a located source and an explicit access limitation; its external theorem is not adopted.

<a id="av09-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso and Evelina Viada, *Small points on subvarieties of a torus*, Duke Mathematical Journal 150 (2009), no.3, 407--442, DOI `10.1215/00127094-2009-056`. The [Torino institutional record](https://iris.unito.it/handle/2318/1944876?mode=complete) identifies its open Duke5.pdf attachment as the author's final postprint. An [author-hosted published rendering](https://amoroso.users.lmno.cnrs.fr/files-heightGmn/Duke.pdf) was also located. No local PDF was obtained; neither artifact has a verified local hash.

Passages: Theorem 6.2, equation (6.24), internally numbered p.26 of the institutional postprint. This locator and the complete theorem wording appeared in the primary PDF's search extraction. The journal page mapping has not been verified.

Inspection: Publisher identity was cross-checked through the institutional record and the author's indexed title page. The complete theorem paragraph and its following proof paragraph were located in a primary-source search extraction. Attempts to open the underlying PDFs failed, so this record does not yet label the original theorem statement as read/accepted. No visual source inspection or source-proof audit occurred.


**Located, with an access limitation.**
A search extract alone is not silently upgraded to an inspected original theorem under the repository's literature rules.
The exact displayed candidate and its direct consequence are preserved below so that a successful original-page inspection can resolve this one specific remaining input.
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

## Bounded acquisition outcome

The following public primary routes were attempted without disabling TLS verification or contacting the authors:

- The author-hosted published PDF URL returned an HTTP 302 redirect loop, both through the web reader and a direct Python HTTPS request.
- The Torino UUID endpoint `https://iris.unito.it/retrieve/92f49bf5-bb0c-4d6e-a1b5-1022e0f59195/Duke5.pdf` returned HTTP 403 to direct acquisition.
- The already indexed Torino bitstream endpoint `https://iris.unito.it/bitstream/2318/1944876/1/Duke5.pdf` also returned HTTP 403.

No AV09.pdf was created.

The institutional metadata itself was successfully read.
No repeated identical requests, third source adoption or recursive reference acquisition followed these bounded attempts.
The unresolved step is an actual original theorem-page inspection, not a mathematical objection to the stated formula.

The coordinator checked the complete record and the conditional parameter substitution.
Its further attempts to open the located primary PDF endpoints also failed, without resolving the original-page inspection.
The explicit exception remains Located.
[C_G276](../../../claims/Yin_C_G0276_v1.md#conditional-polynomial-shape-window) retains the complete stronger-window proof conditional on precisely (2); it does not adopt (1) as an inspected source theorem.
The [actual original targeted check](../../reviews/Yin_R_G0534_v1.md#historical-block-conditional-targeted-finding) retains its fixed L85 input and unknown initial-context relationship; the [current whole finding](../../reviews/Yin_R_G0534_v1.md#current-block-energy-finding) is self-reviewed.
