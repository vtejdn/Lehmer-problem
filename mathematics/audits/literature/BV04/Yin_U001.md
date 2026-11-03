---
author: Yin
---

<a id="bv04-u001"></a>
# BV04-U001: finite-dimensional separation and supporting-hyperplane methods

## Source and inspection

Source edition: [BV04](../../../literature/pdf/BV04.pdf), Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, first publication2004, retained seventh printing with corrections2009; artifact. No new acquisition.

Passages: Section2.5.1, printed46--49/PDF60--63, especially nearest-point separation proof and Example2.20; Section2.5.2, printed50--51/PDF64--65, supporting-hyperplane statement and proof.

Inspection: 2026-10-11T18:34. D12 author and root independently text-read the selected retained primary pages; both visually inspected printed49 and51. The author's public-URL attempt timed out before the successful actual local read; root reused and verified the adequate registered artifact. Earlier weak-duality/tangent/Schur inspections remain at their historical scopes.


The selected finite-dimensional classical statements are: a point outside a nonempty closed convex set can be strictly separated from it; and a boundary point of a nonempty convex set has a supporting hyperplane.
The source's displayed nearest-point proof first treats the positive-distance/attained-distance case.
A point and a nonempty closed convex set satisfy those requirements in finite dimension.
Example2.20 gives the strict point-versus-closed-set conclusion; Section2.5.2 supplies the supporting statement with its nonzero normal.

These established methods are accepted at their exact finite-dimensional scope for attribution.
The selected nearest-point derivative argument and displayed inequality directions were checked; uninspected general extensions/exercises are not imported.
The source does not require every convex set to be closed for its supporting statement, but the consumer's own closest-point argument works with a specifically defined closed epigraph closure.
That use does not authorize replacing a FINITE integer moment hull by its closure.

The [responsible Toeplitz-completeness argument](../../../claims/Yin_C_G0017_v1.md#toeplitz-completeness-reuse-and-source) reconstructs its required support step locally: it must prove local lag feasibility and continuity of its finite-packet value, identify the correct epigraph boundary, and prove that the limiting vertical component is strictly positive.
None of those application-specific facts follows solely from the theorem name.
The integer-residue scaling, PSD conclusion, regularization, rational approximation and first-window companion argument likewise remain local project mathematics.

No general SDP strong-duality theorem, minimax interchange, optimizer attainment, rational maximizing form, integer hull closedness, algorithm or complexity guarantee is adopted.
This unit adds the newly inspected separation/support scope without changing the older [source account](readme.md) or its weak-duality limits.
No Lean or native mathematical program was run.
