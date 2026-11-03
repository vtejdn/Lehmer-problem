---
author: Yin
---
# Pol20-U001: fixed distinct-prime-factor counting

Date: 2026-10-15T07:27.
Human author Yin.
The delegated G0001 author located and read the source; root separately inspected the same primary PDF and the matching retained local passages.
This source inspection is not independent review of the new project argument.

<a id="pol20-u001"></a>
## Read; accepted classical statement and applicability

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Pollack, author-hosted HRmult5.pdf, undated ten-page manuscript; the work is published in Journal of Number Theory210(2020),171--182. The inspected artifact uses manuscript pagination1--10.

Passages: Proposition1 and the definition of omega on printed/PDF page1; the explanation recovering this inequality after Corollary3 on page2.

Inspection: Direct primary online and matching local-PDF statement/convention reading. State Read. The complete Pollack proof and the original Hardy--Ramanujan1917 proof were not audited.


## Exact source content and project use

The source defines omega(n) as the number of DISTINCT prime factors, with arbitrary prime-power exponents allowed.
Proposition1 supplies absolute constants C,D, enlarged if necessary, such that for every real x>=2 and integer k>=1,

    #{n<=x: omega(n)=k}
       <= C x/log(x) * (log log(x)+D)^(k-1)/(k-1)!.

Accept this established Hardy--Ramanujan upper bound at that exact scope.
Its classical attribution is via Pollack's explicit Proposition1 and historical reference; no direct inspection of HR17 is asserted.
It is an upper bound for omega, not Omega, not a squarefree-only count and not an asymptotic with a uniform error for growing k.

For the consuming fixed-K estimate, sum the finitely many cases1<=k<=K, keep n=1 separately, and use phi(n)<=x for n<=x.
This directly permits a bound of the form A_K x^2/sqrt(log x) for x>=2 after enlarging a K-dependent constant: the fixed powers of log log x are eventually bounded by sqrt(log x), and the bounded initial interval is absorbed.
No explicit numerical A_K, uniformity in growing K or whole-tree aggregation is supplied by the source.
The consuming argument must pay its own floors, original weights and summation costs.

## Source, search and use boundary

The concrete trigger was the fixed-terminal-support count in [the current G0001 inquiry](../../../claims/Yin_C_G0124_v1.md#hardy-ramanujan-source-lead).
Bounded local screens did not supply that needed quantitative counting interface.
The author's current [primary manuscript](https://www.pollack-math.net/HRmult5.pdf) provides the statement.
The [publisher record](https://www.sciencedirect.com/science/article/pii/S0022314X19303762) and [author CV](https://www.pollack-math.net/cv.html) verify the work's publication identity; they do not identify the manuscript as publisher pagination.

The [retained exact artifact](../../../literature/pdf/Pol20--author-hrmult5.pdf) matches the inspected title, author, ten-page organization and selected passages.
Bibliographic identity is in [references.bib](../../../literature/references.bib).
The standard counting input is resolved at statement/applicability depth; no proof of the proposed new aggregation theorem, mathematical program, near-one realization or G0001 completion is asserted here.
