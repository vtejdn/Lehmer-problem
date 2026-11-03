---
author: Yin
---

<a id="go08-u001"></a>
# GO08-U001: Green and Poisson--Jensen pole signs, with a literal bar correction

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Goldberg and Ostrovskii, [exact author-hosted English translation](../../../literature/pdf/GO08--author-translation.pdf),495PDF pages; artifact. Its abstract identifies an original monograph published1970. The work's English publication metadata is AMS2008/Translations of Mathematical Monographs236, independently checked from primary listings. The retained file has no verified mathematical revision date; producer timestamp2007 is not substituted for one. No equality with the published2008edition or Russian1970text is asserted.

Passages: Chapter1, Section2, Theorems2.1--2.2/equations2.1--2.2 and multiplicity footnote, printedp.6/PDFp.17; Theorem2.5/equations2.7--2.8, printedp.8/PDFp.19. To check the conjugation convention, also read Chapter1 Section1, equation1.4 and adjacent Green convention, printedp.2/PDFp.13. Cover/abstract PDFpp.1--2 checked.

Inspection: 2026-10-12T03:11. salem_integer_norm_author_finish AI for Yin text-read the complete selected pages and visually inspected rendered printedpp.2,6,8, including conjugation bars, absolute-value signs, pole/zero signs and footnote. Coverage Read for naming/conventions; the literal equation2.2pole numerator is Questioned/corrected as stated below. No whole-book or original-source proof audit.


## Exact convention and source-existing display defect

For a nonzero function meromorphic near the closed region, Theorem2.1 expresses its log modulus as the boundary Green/normal-derivative integral MINUS the Green terms of zeros PLUS those of poles.
Its footnote repeats terms according to multiplicity.
The disk case is called Poisson--Jensen; Theorem2.5 names the center Laurent-coefficient version Jensen and retains the origin order separately.

Equation1.4 displays the positive disk Green kernel with numerator R^2-zeta*conjugate(z).
In the modulus this agrees, after swapping arguments/conjugating, with the local convention

    gamma_R(z,rho)=log |(R^2-conjugate(rho)z)/(R(z-rho))|.

**Source-existing literal defect:** the rendered pole numerator in equation2.2 is R^2-b_n z, with NO conjugation bar on b_n; the zero numerator does have its bar.
For a nonreal pole that is not the disk Green term prescribed by equation1.4 and Theorem2.1.
The corrected pole numerator is R^2-conjugate(b_n)z.
For R1,z=i/4,b_n=i/2, the required numerator modulus is7/8, while the literal printed one gives9/8.
This direct substitution reproduces the mismatch without a numerical program.
The positive pole sign and multiplicities remain correct.
No claim about uninspected editions or a complete errata search follows.

## Role, proof depth and limits

This unit supplies classical naming/sign attribution and the explicit literal-source correction.
The [G0001](../../../tasks/Yin_T_G0001_v1.md#contract) rational-completion argument supplies its OWN full finite Blaschke/Poisson/reversal proof and already uses conjugate(rho).
It must not import equation2.2uncorrected, discard poles or infer a free denominator from original-root values.
No new project pole bound is proved in this U.

The selected displayed explanations were read, but their earlier Green/normal-derivative, conformal-mapping and boundary-theory foundations were not recursively audited.
No classical original1970proof, whole source, general domain theorem or equivalence between editions is accepted by this intake.
The literal source defect is documented and locally corrected; no external author confirmation was sought or claimed.

## Acquisition, metadata and inspection boundaries

Both title/ordered authors and selected formulas were checked in the retained primary file.
The PDF was downloaded from https://www.math.purdue.edu/~eremenko/dvi/GOmainfile.pdf after a default sandbox DNS failure and one authorized retry; normal register-source copied the validated bytes unchanged into the verified flat literature store.
A publisher bookstore request returned403, so no publisher artifact was obtained.
The [AMS series listing](https://www.ams.org/books/mmono/237/mmono237-endmatter.pdf), [Eremenko's primary list](https://www.math.purdue.edu/~eremenko/surveys.html) and [Langley's primary list](https://www.maths.nottingham.ac.uk/plp/pmzjkl/PAPERS/) establish English publication2008/volume236; Langley's list names translator Mikhail Ostrovskii.
Those metadata checks do not establish the retained translation's exact revision date or edition equivalence.
Stop at these bounded identity/convention checks; only the named source defect requires the stated corrected use.

## Explicit selected-domain guard

The general Green statement above retains Chapter1's bounded simply connected domain with piecewise analytic boundary and a nonzero function meromorphic on a neighborhood of its closure.
This intake uses only its disk sign/naming convention.
It does not assert that the same boundary representation holds without those domain, boundary and meromorphic hypotheses.
