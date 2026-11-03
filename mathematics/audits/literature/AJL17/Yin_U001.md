---
author: Yin
---

<a id="ajl17-u001"></a>
# AJL17-U001: complex FIR delay factors and the rational-field boundary

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [AJL17 arXiv:1410.0280v2](../../../literature/pdf/AJL17--arxiv-v2.pdf),16November2014; artifact. Formal publication2017 is distinct from this inspected preprint.

Passages: Section3.2, Theorem3.5, equations(3.10)--(3.13), printed/PDFpp.12--13; title/version header p.1.

Inspection: 2026-10-11, Yin; mathematical author and separate reviewer directly read selected primary statements and displayed arguments. Root independently text-read these pages and visually inspected p.12. No complete source or earlier Potapov proof audit.


For a complex rectangular FIR/Laurent matrix of McMillan degree d that is isometric or coisometric on the unit circle, the theorem gives a constant isometry/coisometry and rank-one orthogonal factors I+(z-1)vv* or I+(z^-1-1)vv*, with v*v=1.
The displayed inverse identity converts the factor forms.
The proof specializes the preceding rational factorization to poles at zero and infinity.
The text warns that mixed forward/backward factors can cancel, so arbitrary d-factor parameters yield degree at most d; equality is not automatic.

This is verified classical attribution and a related complex result.
The G0001 construction instead proves rational H=diag(1,2) projections directly using r(r^TH)/(r^THr), avoiding normalization by square roots.
The source supplies no rational-coefficient descent, prescribed algebraic quotient interpolation, finite word-length bound for that target, or identification of McMillan degree with its union support width.
None is adopted.
Its earlier general factorization/completion dependencies and remaining paper are unreviewed; [AJL16-U001](../AJL16/Yin_U001.md#ajl16-u001) records the companion selected interface.

The attribution search was triggered by the local rational delay-projection argument.
The coauthor's [Chapman record](https://digitalcommons.chapman.edu/scs_articles/442/) and [publication list](https://www1.chapman.edu/~alpay/pub.html) verify Journal of Applied Mathematics and Computing 54 (2017), 395--423, DOI 10.1007/s12190-016-1015-x; the direct publisher request was unavailable.
No equivalence of all preprint and published statements is asserted.
This limited source check resolves the actual context needed; no priority claim follows.

The distinct original [R_G206 selected source check](../../reviews/Yin_R_G0206_v1.md#rational-delay-whole-finding) directly text-read the selected primary passages after its initial local reconstruction.
Its report was completed2026-10-11T14:53; the source-reading minute was not separately recorded and is not inferred from that review clock.
This occurrence adds neither visual inspection nor original-Potapov/completion/full-paper proof coverage; the separate author and root text/visual occurrences above retain their own scopes.
The current complete local factor/pole proof is [C_G441](../../../claims/Yin_C_G0441_v1.md#complete-rational-delay-factorization); the source remains attribution only.
