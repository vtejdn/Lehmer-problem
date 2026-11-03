---
author: Yin
---

# vdB59-U001: the unimodular characteristic-vector congruence

Date: 2026-10-10.
Statement inspection and acceptance by the orbit research AI for Yin within G0001.
Bibliographic and acquisition facts are maintained.

<a id="vdb59-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: F. van der Blij, *An invariant of quadratic forms mod8*, original1959 published three-page scan, printed pages291--293; [registered PDF](../../../literature/pdf/vdB59.pdf), from Andrew Ranicki's University of Edinburgh collection. This is the original article, not a modern exposition or a Milgram paper.

Passages: Printed p.291 defines the integral form, characteristic-vector condition and signature. Printed p.292, Theorem2 and its unimodular specialization equation(7), is the adopted result. These are PDF pages1--2.

Inspection: All three scanned pages were rendered and visually read. The exact equation(7), its determinant assumption D=+1 or -1, the characteristic-vector convention and the absence of a definiteness hypothesis were checked. The surrounding Gauss-sum mechanism was read, but its Fourier/oscillatory-integral justification was not independently audited. Coverage is Read; the stated classical theorem is accepted for use with this proof-inspection limit.


## Adopted statement and conventions

Let L be a finite-rank free abelian group with a nondegenerate integral symmetric bilinear form b.
Unimodular means that a Gram matrix has determinant+1 or -1.
Write sigma(b) for the number of positive eigenvalues minus the number of negative eigenvalues of its real extension.
An element w in L is characteristic when

    b(x,x)=b(x,w) modulo2 for every x in L.

The adopted statement is

    b(w,w)=sigma(b) modulo8.

This is the source's equation(7), obtained there for determinant D=+1 or -1.
The source uses f and tau for b and sigma.
It does not divide b(x,x) by two.
In particular, if b is even, meaning b(x,x) is an even integer for every x, then w=0 is characteristic and sigma(b) is divisible by8.
The even specialization is the entire external theorem used by the project deduction; no assumption of positive definiteness is introduced.

## Proof inspection, dependencies and acceptance

The article reaches Theorem2 by comparing a finite Gaussian sum with an oscillatory integral, and then specializes its auxiliary sum to1 for D=+1 or -1.
The characteristic-vector condition and the displayed specialization were directly checked.
The earlier positive-definite statement on p.291 is equation(3), a different passage; it is not substituted for equation(7).
This distinction permits the indefinite even unimodular lattice used locally.

The analytic regularization and Fourier-expansion steps underlying equations(4)--(5), and the source's referenced theta-function work, were not independently reproved or audited.
There is no claim of full-source proof review, a checked proof assistant artifact, or a fresh proof of this classical congruence.
Under the framework's accepted-external-input rule, the exact identified primary statement is accepted as a resolved input after its hypotheses and local use were verified.
No concrete objection to this standard congruence arose in the inspected scope.
This acceptance does not change the source coverage from Read to Audited within scope.

## Local adaptation and scope

[D77, retained in L_G210](../../../ledger/Yin_L_G0210_v1.md#determinant-two-signature-constraint) uses the even specialization only after constructing an actual even integral unimodular overlattice.
Its independent local proof adjoins a one-dimensional form of norm+2 or -2 to an even determinant-two lattice, then enlarges by a specified dual class.
The index, integrality, evenness, unimodularity and real signature of this construction are checked in D77.
The conclusion for determinant2 is not attributed directly to the source's odd-determinant theorem and is not assumed from a lattice-classification result.

The later rank-seven inertia and coefficient-energy consequences are local deductions.
This source supplies no upper-unitriangular realization, graph classification, eigenvalue energy estimate, neutral-padding minimality or absolute-cover Mahler bound.

## Access, search and verification facts

The query concerned the signature modulo8 for an even lattice with discriminant group of order2.
A bounded primary-source search located Ranicki's Edinburgh collection and its original van der Blij scan.
The collection's bibliographic listing and the scanned title/author/pages were read; the DOI's Crossref metadata was checked directly for title, author, publication year, volume62 and pages291--293.
The parallel traditional citation is Indagationes Mathematicae21.
The publisher DOI page was inaccessible to the web reader, so no publisher-page inspection is claimed.
The scan itself was obtained successfully and opened by pdfinfo.

The artifact has no usable text layer: pdftotext produced only page separators.
All mathematical passage checks therefore used rendered page images.
The source was registered with one bounded successful artifact attempt and no retry queue.
The preliminary downloaded scan and registered artifact were compared directly before operational cleanup.
No new material hash is maintained here.

All three pages were read for context, but only the characteristic-vector congruence and immediate specialization are adopted.
The local-field reformulations on pp.292--293 and cited secondary works are not inputs.
No full errata search, alternative-edition comparison, source-proof reconstruction or formal verification was performed.
The bounded search stops because the exact required primary statement and its applicability have been resolved; it makes no novelty assertion.
