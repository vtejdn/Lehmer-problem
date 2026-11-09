---
author: Yin
---

# Independent review of the complete signed-amplitude classification

<a id="scope"></a>
## Review act and actual relationship

This whole-proof review was performed at 2026-11-09T18:09 UTC by a separately arranged agent acting for Yin.
The reviewer read the complete fixed [C884v3](../../claims/Yin_C_G0884_v3.md#statement) after its proposing agent confirmed that the file was stable.
Only that confirmation and exact input locators were supplied; the reviewer received no development discussion, proof summary or author explanation and did not read D20.
The reviewer supplied no proof step or repair to v3.

This reviewer had already independently checked the finite signed census in [R1110v1](Yin_R_G1110_v1.md#signed-amplitude-review) and the complete positive-amplitude proof in [R1110v2](Yin_R_G1110_v2.md#positive-amplitude-review).
Those prior facts were known when this review began, and the unchanged fixed predecessor checks were reused at their actual scopes.
The finite J157 census is not a premise of C884v3 or of the present unrestricted verdict.
The newly inspected work is the complete analytic negative-amplitude exclusion and its assembly with the proof's selected positive-amplitude predecessor.

The actual mathematical inputs are [C884v1's original domain](../../claims/Yin_C_G0884_v1.md#inputs), [its all-r pole identity](../../claims/Yin_C_G0884_v1.md#all-r-pole-values), [its amplitude and endpoint calculation](../../claims/Yin_C_G0884_v1.md#fixed-amplitude), and [C884v2's positive-amplitude statement](../../claims/Yin_C_G0884_v2.md#statement).
The exact v1 interfaces and complete v2 proof had been read and checked directly in the current unchanged context.
Their earlier findings are reused only for those fixed inputs; the new signed argument is checked below in full.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete signed-amplitude finding](#signed-amplitude-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 statement](../../claims/Yin_C_G0884_v3.md#statement) | Entire signed-real necessity, signed-integer classification with the endpoint, both successes and stated limitations. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 signed reduction](../../claims/Yin_C_G0884_v3.md#signed-reduction) | Zero amplitude, necessary sign parity, half-integral lower bound and independent endpoint. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 negative-even setup](../../claims/Yin_C_G0884_v3.md#negative-even-proof) | Complete negative-amplitude domain and real-magnitude exclusion without the endpoint. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 offset identities](../../claims/Yin_C_G0884_v3.md#offset-bound) | Exact pole values, threshold inequality and both original-grid offset lists. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 positive witness](../../claims/Yin_C_G0884_v3.md#positive-witness) | Both open witness intervals, containment in the original grid range, width and signs. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 direct parities](../../claims/Yin_C_G0884_v3.md#direct-parities) | Both direct combinations, valid nodes, strict constants and temporal order along the grid. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 opposite low branch](../../claims/Yin_C_G0884_v3.md#opposite-low) | Congruence excluding equality, all p<6q cases, the unique q=5/2 case and later witnesses. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 opposite high branch](../../claims/Yin_C_G0884_v3.md#opposite-high) | All p>6q cases, positive denominators, strict threshold bounds, strengthened q=5/2 last-pole estimate and later witnesses. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v3 assembly](../../claims/Yin_C_G0884_v3.md#signed-classification) | Exhaustion of zero, negative and positive real amplitudes and both directions of the integer classification. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v1 original domain](../../claims/Yin_C_G0884_v1.md#inputs) | Exact neutral trace, original full grid, strict terminal chamber and endpoint convention. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v1 full-grid identity](../../claims/Yin_C_G0884_v1.md#all-r-pole-values) | Neutral and linearly perturbed node values for every permitted r, including unreduced coordinate polynomials. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v1 amplitude and endpoint](../../claims/Yin_C_G0884_v1.md#fixed-amplitude) | Exact last-pole calculation and endpoint identity, with the signed extension explicitly checked in v3. |
| [Complete signed-amplitude finding](#signed-amplitude-review) | [C884v2 positive classification](../../claims/Yin_C_G0884_v2.md#statement) | Complete fixed positive-real necessity and positive-integer sufficiency and necessity, previously independently checked in R1110v2. |

<a id="signed-interface"></a>
## Signed reduction and offset identities

The claimed real-amplitude necessity and the integer classification were treated as distinct obligations.
At zero amplitude, all node values are nonnegative, so a nonempty strict negative block is impossible.
For nonzero amplitude, the last-node neutral term and all unsigned factors in its perturbation coefficient are strictly positive on the stated domain.
This forces \(\lambda=(-1)^{L+1}\beta\) with \(\beta>0\).
The sine comparison remains valid when \(q=(L+1)/2\) is half-integral: \(q\le m\), \(mu<\pi/2\), and strict tangent convexity give \(\beta>q\).
The separate endpoint becomes \(4m-2\beta\), so it is exactly the condition \(\beta<2m\) on that necessary parity.
The negative-amplitude exclusion does not invoke this endpoint.

For even \(L\ge4\), one has half-integral \(q\ge5/2\), \(\sigma=\sin(q\pi)\in\{1,-1\}\), and \(p\ge4q+1\).
At either offset \(\theta=\pi/2\pm\delta\), the identity \(\cos(q\pi)=0\) gives \(\sin(2q\theta)=\sigma\cos(2q\delta)\).
Substituting \(b=2\tau\sin\delta\) and \(\sin\theta=\cos\delta\) verifies the displayed expressions for \(U\), \(V\), and \(U/(-V)\).
Every selected negative node has strict \(V<0\), and every witness has strict \(V>0\), so no equality or zero denominator is implicitly accepted.

Writing \(p=4j_0+a\) derives exactly the positive-side offsets \(au/2+2ku\) and negative-side offsets \((4-a)u/2+2ku\).
An offset in \((0,\pi/2)\) from either list gives an actual index between 1 and \(n\): on the positive side its angle is positive, and on the negative side its angle is less than \(\pi\).
Thus the node constructions retain the original grid rather than introducing arbitrary test angles.

<a id="witness-check"></a>
## Witness intervals and exhaustive parity split

On the negative-b side the sign of \(V\) is the opposite of \(\sigma\cos x\).
The interval \((\pi/2,3\pi/2)\) has the needed cosine sign when \(\sigma=1\); \((3\pi/2,5\pi/2)\) has it when \(\sigma=-1\).
Their angular widths are \(\pi/(2q)>2\pi/p\), so each contains an original grid angle strictly inside the open interval.
Their upper offsets are less than \(\pi/2\), using respectively \(q\ge5/2\) and \(q\ge7/2\).
Both intervals therefore lie entirely in the original negative-b angular range, and every selected witness has a strictly positive residue for every positive \(\beta\).

There are exactly four possible pairs \((\sigma,a)\).
The direct cases are \((1,3)\) and \((-1,1)\), leaving precisely \((1,1)\) and \((-1,3)\).
For the latter pairs, writing \(q=k+1/2\) gives the stated residues of \(6q\) modulo four and hence \(p-6q\equiv2\pmod4\).
Equality \(p=6q\) is impossible, and the low and high branches exhaust the remainder.
In the high branch the same congruence gives the indispensable bound \(p-6q\ge2\).

<a id="branch-checks"></a>
## Negative-node thresholds and ordering

In each direct case, the selected offset is \(u/2\), the side gives \(\tau\sigma=-1\), and the phase satisfies \(0<qu<\pi/4\).
Hence \(V<0\) and the threshold is strictly below \(2\sqrt2\tan(u/2)<2\sqrt{2/3}<2<q\).
The smallest possible conductor is at least 11, which justifies the tangent comparison.
The selected negative-side node for \(\sigma=1\) has phase below the witness interval, while the selected positive-side node for \(\sigma=-1\) precedes every negative-side witness.

For the opposite low branch, the offset \(5u/2\) is the second node on the specified side.
The exact inequalities \(p<6q\) and \(p>4q\) place its phase in \((5\pi/6,5\pi/4)\), where \(\cos x<0\) and \(|\cos x|>\sqrt2/2\).
The selected side gives \(V<0\).
When \(q\ge7/2\), \(p\ge15\) bounds the tangent by \(\tan(\pi/6)\), producing a threshold strictly below 2 and therefore below \(q\).
For \(q=5/2\), the low branch and \(a=1\) leave only \(p=13\).
The comparison \(5\pi/26<2/3\), the increasing rational function \(t/(1-t^2/2)\), and the usual strict sine and cosine bounds give \(\tan(5\pi/26)<6/7\).
The resulting constant \(12\sqrt2/7<5/2\) is strict.
For \(\sigma=1\), this negative node is on the positive-b side; for \(\sigma=-1\), its phase is below \(5\pi/4<3\pi/2\).
The witness is later in both cases.

For the opposite high branch, the nearest indicated node has offset \(3u/2\), phase \(3qu\in(0,\pi/2)\), and \(V<0\).
The angle \((p-6q)u/2\) lies between \(u\) and \(\pi/2\), which justifies \(\cos(3qu)\ge\sin u\) by sine monotonicity.
Strict sine concavity gives \(\sin(3u/2)<(3/2)\sin u\); all denominators are positive.
Since \(p\ge17\), the resulting threshold is strictly below \(2\sqrt3<7/2\).
This is below the necessary magnitude whenever \(q\ge7/2\).

For the remaining \(q=5/2\), integrality of \(m\) gives \(m\ge3\).
The polynomial \(D_0=16c^4-12c^2+1\) equals \(\sin(5u)/\sin u>0\), and its factorization gives \(D_0<5c^2\).
The explicit lower bound \(c>284/289>35/36\), together with monotonicity from \(3u\) to \(mu<\pi/2\), yields the stronger necessary inequality \(\beta>18c/5>7/2\).
It therefore also exceeds the constructed node's threshold, including the smallest high-branch conductor 17.
For \(\sigma=1\) that negative node has phase below \(\pi/2\), while for \(\sigma=-1\) it is on the positive-b side.
The witness again follows strictly later.
Thus every branch contains a negative node followed by a positive node, contradicting every strict terminal negative block.

<a id="exact-checks"></a>
## Exact arithmetic and small-parameter checks

Independent exact polynomial arithmetic verified
\[
D_0-5c^2=(c^2-1)(16c^2-1),\qquad
(4c^2-1)^2=D_0+4c^2.
\]
Exact rational comparisons verified \(284/289>35/36\), \((18/5)(35/36)=7/2\), and the squared strict constants \(288/49<25/4\), \(8/3<4\), and \(12<49/4\).
The bound \(5\pi/26<2/3\) follows already from \(\pi^2<10\), since \(250/676<4/9\).
The endpoint value of the tangent majorant is exactly \((2/3)/(1-(2/3)^2/2)=6/7\).

As a check of small index boundaries, direct rational-angle enumeration for every admissible even \(L\) at odd conductors 11 through 33 confirmed that each indicated negative index is valid and that the prescribed open interval contains a strictly later witness.
The smallest instances are:

| \(p\) | \(L\) | Branch | Negative index | A later positive-witness index |
| --- | --- | --- | ---: | ---: |
| 11 | 4 | Direct | 3 | 4 |
| 13 | 4 | Opposite, low | 2 | 4 |
| 15 | 4 | Direct | 4 | 5 |
| 15 | 6 | Opposite, low | 5 | 6 |
| 17 | 4 | Opposite, high | 5 | 6 |
| 17 | 6 | Direct | 4 | 7 |

The table checks actual indices and interval containment; negativity uses the proof's necessary magnitude bounds.
These finite controls are supplementary checks of the explicit analytic construction, not evidence extrapolated to larger conductors.
The unrestricted conclusion follows from the complete interval, parity and threshold arguments above.

<a id="signed-amplitude-review"></a>
## Verdict and exact limits

No defect was found in the complete fixed C884v3 argument.
The analytic negative-even exclusion covers every permitted conductor, even matching length and negative real amplitude without using the endpoint.
Together with zero-amplitude exclusion, necessary signed parity and the selected fixed positive-amplitude theorem, this proves that a strict chamber for any real amplitude forces \(L=3\), \(r=4\), and \(\lambda>2\).
The strict endpoint further forces \(\lambda<4\).
For integer amplitude, necessity and sufficiency therefore give exactly
\[
(p,r,s,L,\lambda)=(9,4,5,3,3),\qquad(11,4,7,3,3),
\]
with \(\kappa=1\) and \(P(-1)=2\), as supplied by the fixed positive-amplitude predecessor.

This finding covers the complete signed one-term family at the statement's exact hypotheses.
It does not classify more general perturbations, establish a shrinking Mahler shell, compute a complete measure or close the unrestricted Task.
No finite census or numerical sign estimate is a premise of the all-conductor proof.
No proof repair or assessment selection was made by this reviewer; adoption remains with the responsible C decision.
