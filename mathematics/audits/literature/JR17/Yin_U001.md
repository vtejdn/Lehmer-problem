---
author: Yin
---

# JR17-U001: permutation zeta functions, direct sums and Artin conductor normalization

Original source reading: 2026-10-09.
Current retention: 2026-10-21T15:58.
The original statement/applicability and inspected-version comparison are retained here without new source inspection.
The publisher article/header discrepancy remains unresolved.
The exact original search and stopping record remains in [the source entrance](readme.md#search-and-stopping-scope).

<a id="jr17-u001"></a>
## Source and inspection

Source edition: John W. Jones and David P. Roberts, Artin L-functions of small conductor, Research in Number Theory3 (2017), DOI10.1007/s40993-017-0079-5, publisher open HTML as read2026-10-09; separately retained arXiv:1610.01228v1, submitted4 October2016. These are two actual inspected versions, without whole-paper equivalence.

Passages: Publisher HTML Sections2.2,2.4,2.5, especially equation(2.3); retained arXiv v1 Sections2.2/2.4 on printed/PDF p3 and Section2.5/(2.3) on p4. First page text supplied title/authors/version identity.

Inspection: Original assigned entropy_status statement reading and coordinator passage comparison, including visual reading of retained pp3--4. The selected identities agree. No whole-paper proof audit, table verification, later analytic theorem adoption or whole-version equivalence; current maintenance performs no new PDF read, source acquisition or source-proof audit.


## Precise standard input

Let E be a number field over Q, let L be a finite Galois normal closure containing E and let chi_E be the complex permutation character of Gal(L/Q) on the Q-embeddings of E into L.
At the standard finite Artin L-function and absolute Artin conductor conventions of the inspected passages,

    L(w,chi_E)=zeta_E(w),
    conductor(chi_E)=abs(disc E).

The Euler identities may be used on Re(w)>1, their domain of absolute convergence, without importing an analytic continuation or holomorphy assertion.
For genuine finite-dimensional complex representations with characters chi and psi, their direct sum has L-function L(w,chi)L(w,psi) and conductor conductor(chi)conductor(psi).
No degree-zero virtual cancellation or conductor-free error estimate follows from that multiplicativity.
The project establishes its actual representation decomposition separately before applying these identities.
These standard statements are accepted for that exact use at the retained Read statement/applicability depth; their source proofs and later analytic estimates are not newly audited.

## Original reading, exact application and limits

**Read; standard statement and attribution scope.**
The assigned entropy_status AI read the publisher's open HTML Sections 2.2, 2.4 and 2.5, especially equation (2.3).
The coordinator independently read those passages, compared the corresponding retained arXiv v1 Sections 2.2/2.4 on printed/PDF p.3 and Section 2.5/(2.3) on p.4, and visually read the locally rendered pp.3--4.
The first page was text-read for title, authors and version.
These selected identities agree between the inspected versions; no whole-paper equivalence, full proof audit, table verification or later theorem adoption is claimed.

## Exact use and boundary

The source identifies the Artin L-function of a number field's permutation character with its Dedekind zeta function and its Artin conductor with the absolute field discriminant.
Equation (2.3) makes both quantities multiplicative under direct sums.
For K/F quadratic and the actual inverse-even/odd decomposition, chi_K=chi_F+chi_-, this gives

    L(w,chi_-)=zeta_K(w)/zeta_F(w),
    conductor(chi_-)=D_K/D_F.

This is known-result attribution for these standard conventions.
The project's matching-character identification, local Euler calculation, finite prime-power removal bound and first-moment limitation are separate local deductions.
The source supplies no new effective error term or large-matching-prime coverage in this use.
Its analytic conductor lower bounds and enumerated fields are not used; no Artin holomorphy or class-field-theoretic Hecke identification is needed for the direct Euler calculation.

The complete current project deductions have their [C_G387v2 proof home](../../../claims/Yin_C_G0387_v2.md#argument).
The [original L_G164 mathematical input](../../../ledger/Yin_L_G0164_v1.md) and [original R_G63 review account](../../reviews/Yin_R_G0063_v1.md#matching-character-independent-review) retain their actual historical scope and relationship.
That project review does not extend the source-inspection scope above.

## Current boundary

The source supplies the standard identities and their normalization, rather than the project's induced-character theorem, positive quadratic Euler calculation, finite prime-removal bound or scalar-moment countermodel.
The publisher-HTML and retained-v1 comparison is restricted to the selected passages.
The bibliographic header discrepancy remains unresolved, and the failed publisher download is distinct from the successful separate arXiv acquisition; this selected mathematical agreement does not resolve those source limitations.
No new analytic prime estimate, Artin holomorphy, Hecke-character identification, original-source proof audit or formal verification is claimed.
