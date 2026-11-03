---
author: Yin
---

# Nat26-U002: Original log-Chebyshev generating-function attribution

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Original NIST DLMF online equation18.12.9 read on2026-10-11; neither original occurrence records a page release/revision or retained snapshot.
No other Nat26 occurrence supplies one.

Passages: Equation18.12.9 and its source note identifying Szego(1975), equation4.7.25.

Inspection: Original single-Haar author formula/attribution reading and the separate original R_G184 reviewer formula/application reading; no original Szego proof or historical-priority audit.


<a id="nat26-u002"></a>
## Exact original readings and consumed identity

The author of [L_G358](../../../ledger/Yin_L_G0358_v1.md#single-haar-moment-lower-certificate), dated2026-10-11, directly read [DLMF18.12.9](https://dlmf.nist.gov/18.12.E9) for the standard logarithmic generating identity.
The reviewer separately read that same primary equation in [R_G184](../../reviews/Yin_R_G0184_v1.md#2-finite-lower-direction-chebyshev-moments-and-source).

The actually consumed local case is x in[-1,1], with T_n(cos theta)=cos(n theta), and complex z with |z|<1:

    -log(1-2xz+z^2)=2 sum_(n>=1) T_n(x) z^n/n.

The analytic logarithm is normalized to vanish at z=0.
The two scalar log factors have an absolutely uniformly convergent series on every smaller closed disk.
The project's substitution z=-rho with0<rho<1 gives its alternating finite-moment expansion and explicit positive tail bound.
Those complete local derivations, integer Laurent recurrence and regularization/lower-bound direction belong to the project proof, not an additional theorem attributed to DLMF.

The page note attributes the formula to Szego(1975), (4.7.25).
Neither original reader claims to have read that original book proof, established earliest priority, or acquired its bytes through this note.
The original page release and snapshot bytes remain unrecorded for these occurrences; they are not inferred from the other Nat26 units or present web state.

<a id="retained-original-check"></a>
## Formula and attribution in the retained original

Equation 18.12.9, its surrounding x in [-1,1] convention and its source note were read in the [retained official Section 18.12](readme.md#retained-selected-pages).
The formula, |z|<1 domain and principal-logarithm notation agree with the consumed identity above, and the page note names Szegő (1975), equation (4.7.25).
The retained page displays version 1.2.8, released 15 September 2026; that identifies this copy and does not reconstruct the original author or reviewer's unknown page release or snapshot.
This later formula/attribution check does not inspect Szegő's book proof, establish historical priority or extend either earlier review.
