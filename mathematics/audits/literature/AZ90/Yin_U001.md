---
author: Yin
---

<a id="az90-u001"></a>
# AZ90-U001: total-derivative elimination and boundary costs

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [AZ90](../../../literature/pdf/AZ90.pdf), coauthor-hosted23-page version; artifact.

Passages: Internal/PDFpp.1--4, Introduction, equations(2)--(4), stated boundary decay and explicit total-derivative integration.

Inspection: 2026-10-11, Yin; root AI text-read pp.1--4 and visually inspected complete p.2. Selected method attribution only; full-paper proof and algorithm audit not performed.


Source: [AZ90](../../../literature/pdf/AZ90.pdf), the coauthor-hosted 23-page version of Almkvist--Zeilberger, *The method of differentiating under the integral sign*.
Its title header identifies Journal of Symbolic Computation 10 (1990), 571--591.
The [coauthor page](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/duis.html) describes conversion from the original Troff source and includes a 15 December 1999 note.
The [publisher's indexed article record](https://www.sciencedirect.com/science/article/pii/S0747717108801599) independently gives 10(6), December 1990, 571--591 and DOI 10.1016/S0747-7171(08)80159-9.
The direct publisher-page request was unavailable.
The contrary final page 592 in secondary catalogues is not adopted; no journal-byte identity is claimed.

2026-10-11, root AI for Yin: text-read retained internal/PDFpp.1--4 and visually inspected complete p.2.
The recurrence author separately checked the same introductory context.
Selected locators are the Introduction on p.1, equations(2)--(3) and the decay hypothesis on p.2, equation(4) and the elimination discussion on p.3, and the explicit vanishing-boundary integration on p.4.
This is a selected mechanism/attribution check, not a complete paper or algorithm audit.

## Exact mechanism and current role

The source seeks a relation between an operator in an external parameter and a total derivative in the integration variable.
After integration, the total derivative contributes its boundary values.
The displayed whole-real-line argument sets that contribution to zero only with the stated decay; it does not justify ignoring arbitrary finite-interval boundary terms.
The source also stresses that the auxiliary certificate may depend on the integration variable.

The current G0001 moment construction instead integrates a polynomial times sqrt(4-x^2) over [-2,2].
Its actual boundary primitive vanishes at both endpoints, and its derivative is integrable.
The explicit elementary integration-by-parts identity, nonzero triangular coefficient, exact integer division, state size and bit costs are locally derived.
No holonomic existence theorem, order bound, elimination algorithm, field descent or software from AZ90 is adopted as a proof premise.
The source supplies verified classical context only; neither priority for this particular recurrence nor historical novelty is asserted.

## Search and limits

The trigger was recognition of parameterized moment elimination during the one-Haar integer determinant investigation.
Search located the coauthor's HTML/PDF and the indexed publisher record.
Primary metadata resolved the page-range choice; the retained source and exact selected passage suffice for the limited attribution.
Original holonomic foundations, detailed algorithms, examples beyond p.4 and appendices remain unreviewed.
This unit supplies no Mahler gap, numerical certificate or input-uniform tail estimate.
