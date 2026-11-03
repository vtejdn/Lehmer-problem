---
author: Yin
---

# Keh25-U001: the Hilbert representation input for bounded smoothing energies

Date: 2026-10-10.
Inspected by the assigned structural_research AI for Yin during its separately organized D91 review.
The coordinating AI accepted this standard foundation at the checked application scope and registered the source.

<a id="keh25-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Christoph Kehle, *Introduction to Functional Analysis*, MIT18.102 Spring2025 lecture notes, dated May2025 in the front matter; [registered public author-hosted PDF](../../../literature/pdf/Keh25.pdf),76pages. This is a modern course-author exposition of a classical theorem, not the original Riesz publication.

Passages: Section5.2, Theorem5.17, printed p.53 / PDF page53. The front matter on PDF page1 identifies the author, course, term and May2025 version.

Inspection: Exact theorem and its short proof read in the primary online indexed text, then rechecked in extracted text from the registered local PDF page53. Statement and application accepted; selected proof inspected. No full-notes audit, audit of the prior orthogonal-projection theorem, original-publication priority search or formal verification is claimed.


## Accepted standard statement

Every bounded linear functional on a real or complex Hilbert space is represented by inner product with a unique vector of the same norm.
Keh25 uses the complex convention with the representing vector in the first, conjugate-linear argument.
The real form, or the corresponding conjugation adjustment, gives integration against an L2 function.
The short proof uses the one-dimensional orthogonal complement of the closed functional kernel, then checks uniqueness and the norm identity.
Its standard orthogonal-projection foundation is not a newly audited theorem here.

## Actual use and limits

[D91 retained in L_G224, bounded-energy converse](../../../ledger/Yin_L_G0224_v1.md#expanding-square-density-pressure) has a probability measure nu on a finite-dimensional expanding space U and normalized smoothing densities f_n with ||f_n||_2<=sqrt(C).
Their smoothing supports shrink to zero.
For every compactly supported continuous phi, the local proof obtains

    |integral phi dnu|<=sqrt(C)||phi||_2.

The test functions are dense in L2(U); this bound extends their integration functional continuously to that Hilbert space.
The accepted representation theorem gives a representing L2 function with norm at most sqrt(C).
Equality on those tests identifies nu with the corresponding density measure, and positivity of nu gives a nonnegative density.
This checks the exact Hilbert-space, continuity and norm hypotheses.
It is the standard foundational input for the converse from UNIFORMLY BOUNDED smoothing energies to an L2 density.

It does not establish bounded energies for any Bernoulli measure, replace boundedness by subexponential growth, prove a Salem density theorem, supply the correlation/packing estimates, classify critical returns or imply a Mahler gap.
Those are separate local deductions or explicitly unresolved conditions.
The [complete D91 review retained in L224](../../reviews/Yin_R_G0793_v1.md#expanding-correlation-complete-independent-review) records the end-to-end mathematical inspection; this source unit supplies only the standard representation interface.

## Bounded search and provenance boundary

The trigger was the recognized Hilbert representation step in D91.
The local source screen found the registered Hor89 notes, but their existing U001 concerns a different result.
Their primary PDF initially opened online; the subsequent targeted page/text request timed out and did not provide a checked representation locator.
That failed locator attempt is historical access information, not an unresolved mathematical premise.
A bounded primary-source search then located Kehle's MIT notes and the exact theorem above.
The search stopped after checking that statement, short proof, version and applicability; no novelty or earliest-source claim is made.
The coordinator subsequently acquired and registered the PDF normally.
This unit does not broaden Hor89's earlier recorded inspection or claim that the reviewer registered or modified shared source records.
