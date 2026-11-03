---
author: Yin
---

<a id="jks24-u001"></a>
# JKS24-U001: A primary quantitative L1 theorem for integer Fourier support

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [JKS24](../../../literature/pdf/JKS24.pdf), arXiv:2303.10919v2,24July2023,25pages. Canonical publication: Math.Ann.389(2024),1939--1961; DOI10.1007/s00208-023-02692-w. Artifact.

Passages: Own Theorem1.1(i), printed/PDFp.3; integer-frequency long-average equality on p.4. Primary title/version p.1 and historical TheoremB p.2 read for identification only.

Inspection: Original source unit recorded 2026-10-11T13:37 for Yin; the distinct author text reading, central first4pages/p.3 visual check and later original R_G198 pp.3--4 text/visual reading are distinguished below. Exact statement/applicability only; original proof and pp.5--25 remain unreviewed, without a whole-source or formal audit.


## Distinct original reading occurrences

The original mathematical author checked v2 Theorem1.1(i) on p.3 and the integer-period interface on p.4 by text during the 2026-10-11 argument.
No separate reading minute is established in that author account; screenshot attempts supplied no inspectable image, so the author did not claim visual inspection.
The original central source unit was recorded at 2026-10-11T13:37 and separately records root's complete first4pages text reading and visual inspection of retained p.3.
The original [R_G198 whole SELF review](../../reviews/Yin_R_G0198_v1.md#fixed-constant-whole-finding), recorded 2026-10-11T13:46, separately text-read complete pp.3--4 and rendered and visually inspected both pages, with first-page identity/version checked by text.
That review's known initial author-self-check exposure concerns the project argument relationship, not whether these source pages were actually read.
This relocation preserves the three occurrences and their actual precision and depth; it performs no new PDF reading, acquisition, proof audit or version-equivalence check.

## Exact accepted input

For N>=1 distinct ordered real frequencies lambda_1<...<lambda_N and arbitrary complex coefficients a_k, the authors' own Theorem1.1(i) states

    lim_(T→infinity) (1/T) integral_(-T/2)^(T/2)
             |sum_(k=1)^N a_k exp(2pi i lambda_k t)| dt
         >=(1/26)sum_(k=1)^N |a_k|/(k+1).

This exact established theorem is accepted for use at statement/applicability depth.
No lower bound on coefficient magnitudes or frequency separation is needed for part(i).
Part(iii)'s finite-T/separation assumptions are not transferred to it.
The integer-frequency equality on p.4 converts the limit into normalized integration over a single period.
This can also be checked directly by splitting into complete periods and bounded remainders.

For a finite integer trigonometric polynomial with N nonzero coefficients, each has magnitude at least1.
The displayed theorem therefore gives

    ||f||_L1(T) >=(1/26)sum_(k=1)^N1/(k+1)
                 >=(1/52)log(N+1).

The last inequality uses1/(k+1)>=1/(2k) and sum1/k>=log(N+1).
Negative and zero frequencies are included by ordinary ordering, and complex signs are retained inside the absolute value.
For a nonnegative f, its L1 norm equals its actual constant coefficient.
This is the precise support-count interface consumed by the G argument.

## Provenance and limits

The original MPS1981 theorem is reported as TheoremB on p.2, but the current input uses Jaming--Kellay--Saba's OWN Theorem1.1(i), not an uninspected original-MPS proof or a same-coefficient-only theorem.
Earlier bounded attempts to obtain original AMS/Annals/MPS copies did not supply usable proof text; the author located this direct primary alternative.
Its original proof remains unaudited but the statement and local applicability are resolved under the established-external-input rule.

The publisher verifies first online publication7August2023, formal volume389 and issue year2024.
The arXiv record identifies v2 and says its appendices are absent from the final journal version.
No preprint/journal byte or complete-proof equivalence is asserted.
The canonical key follows the known2024publication year; source-version locators remain2023v2.

The source supplies neither original-circle discrepancy nor an integer trace-order/unit lift or residual covariance realization.
Those new G deductions require their own whole review.
No historical best-constant, earliest-priority, whole-paper audit or Lehmer gap is certified here.
