---
author: Yin
---
# AM16-U001: the existing whole Galois-generator height scope

Date: 2026-10-15.
Root records strategy_critique's exact SOURCE-only inspection, after root's primary-source search identified a potentially stronger antecedent.
This changes the project's reuse assessment; it is not a new project lower-bound proof.

<a id="am16-u001"></a>
## Read; accepted theorem statement and degree boundary

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Francesco Amoroso and David Masser, Lower bounds for the height in Galois extensions, institutional author postprint dated3 August2016,6 PDF pages including cover and printed1--5. Published Bulletin of the London Mathematical Society48(6)(2016),1008--1012.

Passages: Printed1 introduction and Section3 printed2--4, especially Theorem 3.3 printed3/PDF4; Theorem3.1 and Corollary3.2 for the distinct ambient-degree scope. Separate publisher erratum bdw066 short body inspected online.

Inspection: Exact statements, degree conventions and Section3 proof direction read. The deep external height theorems used in the proof were not re-audited; not a complete independent proof audit.


Theorem 3.3 states that for every epsilon>0 there is a positive c(epsilon) such that h(alpha)>=c(epsilon)d^(-epsilon) for nonzero non-root-of-unity alpha with Q(alpha)/Q Galois and d=[Q(alpha):Q].
Here h is absolute logarithmic Weil height.
The theorem has no fixed-prime, central-Frobenius, bounded-conjugacy-class or ramification hypothesis.
This established statement is accepted at its checked scope.

The introduction also credits Amoroso--David 1999 Corollary 1.7 for the earlier Lehmer conclusion when Q(alpha) itself is Galois, with a separate almost-Galois generalization in Corollary 1.8.
Those are source reports; their original text/proofs were not independently read in this round.
The actual Theorem 3.3 already suffices to identify whole-Galois-generator coverage: for an original degree-d polynomial m=d*h, so choosing any fixed epsilon<1 yields a positive lower bound on m in that class.
This does not settle the unrestricted non-Galois case.

The source's different ambient statement must not be conflated with Theorem 3.3.
If alpha merely belongs to a Galois field F of degree D, Corollary 3.2 has h(alpha)>=c(epsilon)D^(-1/2-epsilon), with its own source constants and hypotheses.
The ambient D is not automatically d=[Q(alpha):Q].
Passing to a normal closure can therefore destroy an apparent original-degree gain.
No replacement of D by d is accepted here.

### Actual erratum boundary

The complete short [publisher erratum](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms/bdw066), first published 29 December 2016, was checked online on 2026-10-15.
It corrects the reversed author order in the initial 16 September 2016 online publication and says the online and print versions are corrected.
It contains no mathematical correction.
This resolves that concrete version concern at the inspected scope; it is not a search claim that no other criticism exists.
Its actual HTML acquisition failed with HTTP 403, and no local AM16b artifact was retained.

The [actual postprint](../../../literature/pdf/AM16--author-postprint.pdf) preserve the selected edition.
It has no printed contents list.
The author URL's redirect-limit failure is not a second retained version.
Any project fixed-prime argument restricted to original Galois fields is a refinement or method comparison inside this already covered class, not newly established gap coverage; a new non-Galois extension requires its own full proof and degree accounting.
