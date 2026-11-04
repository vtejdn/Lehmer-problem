---
author: Yin
---
# Nat26-U003: Original Gaussian theta formula readings

## Source and inspection

Source edition: Official NIST DLMF online version1.2.8, released2026-09-15, actually read in the original2026-10-10 author and separate reviewer occurrences; no snapshot or HTML/PDF was retained for these passages at that time.

Passages: Author: equations20.2.3 and20.7.32 with upper-half-plane/nome/principal-square-root conventions.
Separate reviewer: those same formulas plus20.1 notation q=exp(i pi tau), Im(tau)>0.

Inspection: Exact classical statement/formula/application depth for the shifted Gaussian transform; the local three-consecutive-point truncation and integer elimination are project proofs.
The historical book proofs, source-wide audit and priority question remain outside this scope.


<a id="nat26-u003"></a>
## Exact original reading scope

<a id="original-gaussian-theta-author-reading"></a>
### Original coordinator reading

On2026-10-10 the coordinator author of [L_G256](../../../ledger/Yin_L_G0256_v1.md#three-point-gaussian-maximum) read [DLMF20.2.3](https://dlmf.nist.gov/20.2.E3), [20.7.32](https://dlmf.nist.gov/20.7.E32) and their surrounding nome/upper-half-plane/principal-square-root conventions.
The [original supplemental note](readme.md#gaussian-theta-attribution-20261010) records the same actual occurrence; it is not a later second reading.
The original formula acceptance is at statement/application depth; the cited historical book proofs were not read.

For a>0 and real x, the actual consumer sets tau=i a/pi and z=i a x, then tau'=-1/tau=i pi/a and z tau'=-pi x.
The theta_3 cosine series is even, both relevant Gaussian series converge absolutely, the principal square root is sqrt(a/pi), and the transformation's exponential is exp(a x^2).
Multiplication by exp(-a x^2) yields the exact locally specialized identity

    Theta_a(x)=sum_(n in Z)exp[-a(n-x)^2]
       =sqrt(pi/a)[1+2sum_(n>=1)exp(-pi^2 n^2/a)cos(2pi n x)]
       <=Theta_a(0).

The nonnegative Fourier coefficients give the last inequality.
The source formula is used on all a>0; the project's further three-consecutive-point estimate uses a>=log2, nearest-integer centering and convexity of the omitted tails on y>=3/2.
That truncation, all integral quotient constraints, sequential Gram elimination and Mahler/entropy comparison are project arguments, not extra theorems read from DLMF.

<a id="original-gaussian-theta-reviewer-reading"></a>
### Separate original reviewer occurrence

The original resultant-research reviewer of [L_G256](../../../ledger/Yin_L_G0256_v1.md#three-point-gaussian-maximum) separately inspected the same two official formulas and [20.1 notation](https://dlmf.nist.gov/20.1) on2026-10-10 at that same displayed edition.
Its original finding is retained in [R653](../../reviews/Yin_R_G0653_v1.md#return-projection-isolated-whole), with the original unknown relationship preserved.
It checked q=exp(i pi tau), Im(tau)>0, the principal square root and the entire tau/z specialization at exact statement/formula/application depth.
This distinct occurrence does not establish the original project review's agent-context isolation or a source-book proof audit.

<a id="retained-original-check"></a>
## Selected formulas and notation in the retained originals

Equations 20.2.3 and 20.7.32, their surrounding conventions and Section 20.1's notation were read in the [retained official pages](readme.md#retained-selected-pages).
All three display version 1.2.8, released 15 September 2026.
The theta_3 cosine series, tau'=-1/tau transformation, principal square roots, q=exp(i pi tau) and Im(tau)>0 agree with the source interfaces retained above.
The selected formulas and notation are complete in the embedded MathML and TeX alternate text.
This separate later check preserves both original author/reviewer occurrences and their historical no-snapshot limits, without a source-book proof audit, new project review or change to the local specialization.
