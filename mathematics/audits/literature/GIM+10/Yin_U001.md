---
author: Yin
---

# GIM+10: the published 0.427800 bound and its integral-congruence transfer

Date: 2026-10-07.
Narrow inspection by assigned AI ms25_source for Yin, during [G0001](../../../tasks/Yin_T_G0001_v1.md#contract).

## Source and inspection

[Source and edition notes](readme.md).

Source edition: J. Garza, M. I. M. Ishak, M. J. Mossinghoff, C. G. Pinner and B. Wiles, *Heights of roots of polynomials with odd coefficients*, JTNB22(2)(2010),369--381, DOI10.5802/jtnb.721; journal archive PDF,796714 bytes,14 pages including cover; retained [GIM+10.pdf](../../../literature/pdf/GIM%2B10.pdf); acquisition.

Passages: Theorem1.1 printed370/PDF3; m=2 proof and equation(3.5), printed373--375/PDF6--8. These pages were rendered and viewed; surrounding normalization and preliminaries read in text.

Inspection: Published theorem and explicit auxiliary mechanism inspected. The local arithmetic and the integral-input nonvanishing repair below are directly checked. The published numerical supremum evaluation is an external statement-level input; it has not been independently reproduced or certified.


<a id="gim+10-u001"></a>
## GIM+10-U001: accepted published calculation

State: **Read** for the numerical bound, with the selected arithmetic proof steps checked.
Acceptance does not certify the original computation.

Theorem1.1 asserts `h(alpha)>=0.427800/(n+1)` for a root of an all-odd-coefficient degree-n polynomial, excluding the 2(n+1)-st roots of unity.
This is a historical verified source bound, not a claim that 0.427800 is currently the best constant.

The retained calculation uses the seven explicitly displayed factors on printed373--374 and exponents (3977,780,328,96,24,16,16) on printed375.
For the polynomial g and nonnegative circle expression L of those pages, deg g=6005, its dyadic weight is 11206, and equation(3.5) is

    h(beta)>=[16407 log2-log L]/24020.

The printed numerical evaluation of this expression is 0.4278003111...
The source's rounded lower bound 0.427800 is accepted as an established external input for precisely this displayed polynomial and expression.
No source code, exact interval certificate or independently rerun supremum computation was obtained.
This is not a current-best-constant claim.

The general integral-congruence application and its nonvanishing argument are separate local deductions in [the retained original L69 argument](../../../claims/Yin_C_G0246_v1.md#gim%2B10-integral-congruence-transfer).
That proof retains all original embeddings, requires (alpha^a-1)/2 to be integral, and uses a direct unit-circle/Kronecker check in place of the source's degree-based irreducibility argument.
The arbitrary-prime scalar consequence is a separate [complete local argument](../../../claims/Yin_C_G0246_v1.md#gim%2B10-arbitrary-prime-scalar-transfer), rather than a source theorem.

Actual review: the source agent read and rendered the stated passages; the coordinator read the retained proof text on printed373--375 and visually checked PDF8, including the exact formula and exponents.
Assigned AI review_matrix_completion separately read the same proof interface and checked all seven polynomial identities, arithmetic weights and circle normalization in the transfer argument; the [original whole finding](../../reviews/Yin_R_G0021_v1.md#original-integral-transfer-whole-check) records its unknown initial isolation at that precise scope.
These checks do not include the numerical supremum margin, the source's complete irreducibility argument, its general-m bounds or the remainder of the paper.

The bounded source search stopped after locating this exact primary-source interface and the Sam07 factor statement.
No unresolved citation is needed for this adopted expression.
Uniform modular coverage of the small-Mahler core remains an unproved project obligation; this paper does not supply it.
