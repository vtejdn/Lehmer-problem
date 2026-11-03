---
author: Yin
---

# GM16-U001: explicit conditional Dedekind prime-power error

Date: 2026-10-09.
Source statement and applicability checked by assigned growth_arithmetic_status AI and the coordinator for Yin, for the finite joint-matching test in G0001/S_G0008.
Bibliography and acquisition.

<a id="gm16-u001"></a>
## Read; accepted conditional external statement

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Loic Grenie and Giuseppe Molteni, Explicit versions of the prime ideal theorem for Dedekind zeta functions under GRH; retained arXiv:1312.4463v4, 17 September 2015, 17 pages, identified as the final version; journal Mathematics of Computation 85(298), 2016, 889--906.

Passages: Printed/PDF p.1 definitions of absolute degree, absolute field discriminant and ideal Chebyshev sum; p.2 GRH convention; p.3 Corollary1.2 and equation(1.5).

Inspection: The assigned agent initially text-read the corresponding institutional v2 passages. The coordinator text-read retained v4 pp.1--3, visually read locally rendered pp.2--3, and checked the displayed bound, constants, x-range and GRH scope against that transcription. Only this selected statement is carried to v4; no whole-version equivalence, analytic-proof review or verification of auxiliary programs/constants computations is claimed.


Let E be a number field, n_E=[E:Q], and D_E the positive absolute field discriminant.
Define

    psi_E(x)=sum_(q finite prime ideal, j>=1, (Norm q)^j<=x)
                         log(Norm q).

Under GRH for the Dedekind zeta function zeta_E, for every real x>=100, the source's Corollary1.2 states

    |psi_E(x)-x|<=E_E(x),
    E_E(x)=sqrt(x)[(log x/(2pi)+2)log D_E
                         +(log(x)^2/(8pi)+2)n_E].

GRH remains an explicit hypothesis about nontrivial zeros; it is not proved or removed here.
All logarithms are natural.
The sum includes prime powers and every finite prime ideal, including ramification.
It is not a count of rational primes alone or only degree-one prime ideals.

## Applicability and acceptance

The current local objects are K=Q(alpha), F=Q(alpha+alpha^(-1)), [K:Q]=d and [F:Q]=s=d/2.
Assuming GRH separately for zeta_K and zeta_F, the displayed statement applies to each field directly; no Galois hypothesis, normal-closure substitution or GRH for the whole splitting field is needed for these two applications.

The coordinator accepts this established conditional theorem at statement/applicability scope for those substitutions.
The local joint-character inequality, prime-power/ramification removal, explicit sufficient prime range and its budget comparison are additional project deductions with their own review.
This source statement does not by itself force large matching, supply the degree-uniform p<=B d log p target, or remove the trace-action restriction in a consuming argument.

The source's Theorem1.1 and adjacent Corollaries1.3--1.4 were seen for orientation but are not selected inputs.
Its proofs, zero-sum estimates, numerical verifications and linked programs were not audited or executed.
This is Read with an accepted conditional statement, not a full source-proof or formal audit.

## Bounded search and version boundary

Local reuse of L75/L163/L164, BS96 and JR17 found only least-prime statements or placeholder psi errors.
The agent's sole mathematical query was `Grenie Molteni explicit Chebyshev function number fields GRH 2016 psi error theorem arxiv`.
The coordinator's acquisition-only query was `"Explicit versions of the prime ideal theorem for Dedekind zeta functions under GRH" arxiv`.
The institutional v2 was initially readable as indexed text to the agent; the coordinator's later web opening returned HTTP403.
The agent's arXiv v2 openings returned a web-layer DisabledError, not a successful download.
No blocked endpoint was retried.

The current official arXiv record identifies v4 as final, with misprints corrected.
The separately public fixed v4 artifact was therefore acquired and the exact used statement checked there.
The selected Corollary1.2 formula and hypotheses agree with the agent's earlier v2 transcription.
No claim about uninspected version differences is made.
The search stops with this one usable explicit interface; no claim of an optimal current bound or absence of a sharper theorem is made.
