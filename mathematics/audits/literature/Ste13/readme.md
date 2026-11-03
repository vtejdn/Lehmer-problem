---
author: Yin
---

# Ste13: exceptional units and cyclotomic resultant estimates

<a id="ste13-discovery-screen"></a>
## Compact discovery and statement screen

| Field | Recorded scope |
| --- | --- |
| Source/version | C. L. Stewart, *Exceptional units and cyclic resultants, II*. The retained public author manuscript has printed/PDF pages 1--10; it is not identified as the publisher's final PDF. |
| Scope/locator | Introduction and normalization, pp.1--3; Theorems 1.1 and 1.2 and equations (1.11)--(1.12), p.3/PDF3; selected proof discussion and dependencies, pp.4--6/PDF4--6. |
| Trigger/intended use | Bounded G0001 [S_G8](../../../strategies/Yin_S_G0008.md#next-coverage-test) screen for quantitative cyclic-resultant mass beyond primitive-divisor existence. Compare the needed actual excess with [L_G152](../../../ledger/Yin_L_G0152_v1.md#primitive-mass-next-obligation). |
| Date/reviewer and state | 2026-10-09, assigned execution_and_deliverables AI for Yin. **Read**: exact statement and notation screen with selected proof inspection; authoring-agent self-check only. No complete or independent proof audit and no accepted proof dependency. |
| Acquisition | Title, author and ten-page length checked. Pages 1, 3 and 4--6 were rendered and visually inspected as well as text-read. |
| Dependencies/unchecked scope | The source invokes Dobrowolski, Baker--Wustholz, Silverman and elementary prime estimates. Their proofs and the full paper were not audited. Theorem 1.3 and the later computational section are outside this screen. |

### Statements actually read

Use K=Q(alpha), d=[K:Q], M=M(alpha), and D_n=|Norm_(K/Q)(Phi_n(alpha))|.
Theorems 1.1--1.2 assume that alpha is a nonzero algebraic integer which is not a root of unity; they do not require alpha to be a unit or exclude unit-circle conjugates.
For every epsilon>0, put

    t_epsilon(d)=(log 2+epsilon)/log log(d+2).

Theorem 1.1 asserts an effectively computable positive C_epsilon, depending only on epsilon, for which

    n>C_epsilon d^(3+t_epsilon(d))
        implies
    M^((1-epsilon)phi(n)) < D_n
        < M^((1+epsilon)phi(n)).

Theorem 1.2 bounds the number of positive integers n satisfying

    D_n < M^((1-epsilon)phi(n))

by C'_epsilon d^(1+t_epsilon(d)), with another effectively computable positive constant depending only on epsilon.
The strict inequality defining the exception set and the distinction between the two constants are retained.
No numerical value of either constant is supplied or computed by this screen.

These are estimates for the full cyclotomic layer D_n.
They do not by themselves identify its ideal-primitive part, its largest prime factor, or additional primitive valuation mass.
With m=log M and 0<epsilon<1, the lower comparison is still log D_n>(1-epsilon)phi(n)m.
Its useful degree-dependent threshold and exception count do not replace the unknown m by a common positive constant.
This source is therefore not adopted here as a uniform-gap input or as a new proof dependency.

### Proof inspection and unresolved display detail

The selected pp.4--6 explicitly retain phi(n)log M as the main term.
Section 3 uses Mobius inversion and Lemma 2.2's linear-form bound, then Lemma 2.1's degree-dependent Dobrowolski bound to obtain the threshold.
Section 4 normalizes the conjugates to the closed unit disc and compares their distances to primitive roots of unity to count exceptional indices.
Reading these passages did not produce a degree-uniform positive lower bound independent of m.

One literal display needs attention before any future proof adoption: on p.6, equation (4.7) prints the inner minimum with 1<=j<=d and (j,d)=1, whereas (4.3) on p.5 and the following n_1,n_2 argument use primitive n-th roots and the corresponding n-dependent range.
This was checked on the rendered page, not inferred from OCR.
No repair or full-proof verdict is made here; the publication version has not been compared.
The exact p.3 theorem statements are readable.

### Search evidence and stopping decision

The bounded local check found no existing Ste13 key, matching DOI, matching work title, author-PDF locator, or artifact.
The specifically queried primary links were the [author's institutional proceedings bibliography](https://uwaterloo.ca/pure-mathematics/cameron-stewart/refereed-conference-proceedings) and its [linked author PDF](https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/exceptional_units-5_0.pdf).
The bibliography identifies Contemporary Mathematics 587 (2013), pp.191--200.
The [Crossref DOI metadata](https://api.crossref.org/works/10.1090/conm/587/11698) was retrieved directly with HTTP200 and confirms the title, author, 2013 date, pages and AMS publisher; its volume field is absent, so the volume attribution comes from the institutional bibliography.
The web-reader attempt at the DOI landing page was unavailable; no publisher final-text comparison is claimed.

Stop this intake at **Read**, with no fixed U or L allocated.
Reopen only for a specified use of the degree/exception estimate with its full mass-transfer costs, or to resolve the display/version issue before proof adoption.
The current source screen neither rules out a useful later specialization nor advances an unrestricted gap by replacing actual primitive excess with a result proportional to m.
