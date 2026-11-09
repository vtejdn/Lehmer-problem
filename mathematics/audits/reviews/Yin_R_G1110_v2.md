---
author: Yin
---

# Independent review of the complete positive-amplitude classification

<a id="scope"></a>
## Review act, relationship and exact inputs

This review was performed at 2026-11-09T17:56 UTC by a separately arranged agent acting for Yin.
The reviewer read the complete fixed [C884v2](../../claims/Yin_C_G0884_v2.md#statement) after its proposing agent confirmed that the file was stable.
The reviewer supplied no proof step or repair to that material and received no development discussion, working draft, mathematical summary or author explanation of its argument.
D20 and development messages were not read.
The proposing agent supplied only the stable-file notification and exact input and argument locators.

The same reviewer had already independently inspected J157 and its fixed mathematical interfaces, with that finite finding retained in [R1110v1](Yin_R_G1110_v1.md#signed-amplitude-review).
That earlier finite result was known before reading C884v2, but was not used as a premise or substituted for any unrestricted proof obligation.
The present finding is a separately performed whole-proof inspection of C884v2, including its assertion for arbitrary positive real amplitudes and its narrower integer classification with the endpoint.
It preserves the distinct finite-computation finding in v1 and supplies no classification of negative amplitudes beyond that earlier finite scope.

The direct mathematical inputs are [C884v1's domain](../../claims/Yin_C_G0884_v1.md#inputs), [all-r pole identity](../../claims/Yin_C_G0884_v1.md#all-r-pole-values), [positive-amplitude constraints](../../claims/Yin_C_G0884_v1.md#fixed-amplitude), [coefficient-three classification](../../claims/Yin_C_G0884_v1.md#length-three), and [endpoint calculation](../../claims/Yin_C_G0884_v1.md#endpoint).
Their original-grid and neutral-lift interfaces were checked directly using [C881v3's domain](../../claims/Yin_C_G0881_v3.md#original-domain), [recurrence](../../claims/Yin_C_G0881_v3.md#prefix-coordinates), and [L462v11's neutral supply](../../ledger/Yin_L_G0462_v11.md#neutral-integer-supply), reusing the actual unchanged current-context reading from the preceding independent review.
No earlier R finding about C884v2 was consulted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete positive-amplitude finding](#positive-amplitude-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 statement](../../claims/Yin_C_G0884_v2.md#statement) | Complete real-positive-amplitude necessity, positive-integer classification with the strict endpoint, both finite successes and stated limits. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 reused identities](../../claims/Yin_C_G0884_v2.md#reused-identities) | Original full-grid values, sign thresholds, positive weights and separate endpoint. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 uniform threshold](../../claims/Yin_C_G0884_v2.md#threshold) | Parameter deductions, threshold upper bound, nearest positive node and its phase coordinates. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 odd-q exclusion](../../claims/Yin_C_G0884_v2.md#odd-q) | Complete odd q at least three, strict threshold estimate and actual later grid node with positive residue. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 phase selection](../../claims/Yin_C_G0884_v2.md#phase-selection) | All step-size and parity classes, sine margin and valid earlier positive-grid indices. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 even-q exclusion](../../claims/Yin_C_G0884_v2.md#even-q) | Every even q at least six and every constant in the strict threshold estimate. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 q-four exclusion](../../claims/Yin_C_G0884_v2.md#q-four) | All conductors at least 33 and all eight exact remaining odd-conductor rows. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v2 length-three argument](../../claims/Yin_C_G0884_v2.md#length-three) | Positive threshold denominators, ratio identity, m at least three exclusion, endpoint integer selection and final successes. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v1 input domain](../../claims/Yin_C_G0884_v1.md#inputs) | Exact integral neutral trace and original strict chamber and endpoint conventions used by v2. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v1 full-grid values](../../claims/Yin_C_G0884_v1.md#all-r-pole-values) | Values on every original node for all permitted r and linear extension to arbitrary positive real amplitude. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v1 amplitude constraints](../../claims/Yin_C_G0884_v1.md#fixed-amplitude) | Even-length obstruction, strict lower amplitude bound and endpoint equivalence. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v1 coefficient-three classification](../../claims/Yin_C_G0884_v1.md#length-three) | Exact final classification for m=2, L=3 and amplitude three, including strict cut sizes. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C884v1 endpoint](../../claims/Yin_C_G0884_v1.md#endpoint) | Neutral endpoint and lifted perturbation, including the value two in both successes. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C881v3 original domain](../../claims/Yin_C_G0881_v3.md#original-domain) | Full decreasing grid, positive residue weights and strict endpoint equivalence. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [C881v3 recurrence](../../claims/Yin_C_G0881_v3.md#prefix-coordinates) | Exact residue-coordinate congruence used by the unchanged pole interface. |
| [Complete positive-amplitude finding](#positive-amplitude-review) | [L462v11 neutral supply](../../ledger/Yin_L_G0462_v11.md#neutral-integer-supply) | Exact neutral lift and specialized original-pole residue formula. |

<a id="obligations"></a>
## Scope and interface checks

The statement has two logically different conclusions, and both were checked.
For every real positive amplitude, the chamber alone forces \(L=3\) and \(r=4\).
Only after that implication does the argument use the strict endpoint and integrality to select amplitude three and the two conductors.
The proof never assumes bounded amplitude, primality of the conductor, a reduced-degree neutral representative, or the endpoint in its earlier chamber exclusions.

The residue identity \(h(b_j)=U_j-\lambda V_j\) follows from the exact neutral formula and the recurrence congruence by linearity.
The denominator \(\sin\theta_j\) is positive for every original node, and the residue weights are positive.
For \(V_j>0\), the stated threshold inequalities are exact; for \(V_j<0\), positivity is strict even if \(U_j=0\).
The selected contradiction nodes always have strict nonzero \(V_j\), so no unhandled equality or zero-threshold case is used.
Reduction of the coordinate polynomial modulo \(B_n\) leaves all required values unchanged.

Even \(L\) is excluded at the last node before any other step.
For odd \(L=2q-1\), the hypotheses imply \(q\le m\), \(n\ge2q\), \(p\ge4q+1\), and the necessary strict inequality \(\lambda>q\).
For a positive pole with positive \(\sin(2q\theta)\), the threshold expression follows by cancelling the sine formula, and \(\sin^2(m\theta)\le1\) supplies the displayed upper bound independently of \(m\).
A negative residue followed by a later positive residue is incompatible with every allowed terminal negative block, regardless of its size.

<a id="odd-case"></a>
## Odd q and the later-node interval

For odd \(q\ge3\), the nearest positive node has \(2q\delta_0=qa\pi/p<3\pi/4\) and \(0<\delta_0<\pi/4\).
The tangent upper chord and sine lower chord have the stated directions.
Their constants give \(3\sqrt2/q<q\) already at \(q=3\), with stronger separation thereafter.
Together with \(\lambda>q\), this makes the chosen residue strictly negative.

The later interval lies inside \((0,\pi)\) and has length \(\pi/(2q)>2\pi/p\).
Every open interval longer than the grid spacing contains a grid angle, and an angle in \((0,\pi)\) has an integer index between 1 and \(n\).
This establishes an actual original node, not merely a continuous test point.
Writing its angle as \(\pi/2+\varepsilon\), with \(2q\varepsilon\in(\pi,2\pi)\), verifies \(\sin(2q\theta)>0\) when \(q\) is odd.
The negative cosine then makes \(V<0\), so the later residue is strictly positive and the chamber fails.

<a id="even-cases"></a>
## Even q, phase progression and finite exceptions

For even \(q\), the nearest positive node has negative \(V\) and hence a strictly positive residue.
The phases of earlier positive-grid candidates are exactly \(x_k=d(k+a/4)\), with \(d=4q\pi/p<\pi\).
The small-step construction reaches \([5\pi/4,7\pi/4]\): its initial phase is below \(3\pi/4\), and its overshoot is at most the step \(d\le\pi/2\).

The four large-step subcases have exactly the endpoint ranges displayed in the proof.
Direct multiplication of the rational step endpoints by \(5/4,9/4,7/4,11/4\) verifies all four ranges, and each remains inside \([15\pi/14,27\pi/14]\).
Thus every selected phase lies strictly between \(\pi\) and \(2\pi\) and has \(-\sin x\ge\sin(\pi/14)\).
The initial phase is below \(3\pi/4\), so the selected index has \(k\ge1\).
For \(q\ge4\), its \(\delta=x/(2q)<\pi/q\le\pi/4\) implies \(j_0-k>0\) through the exact angle formula.
It is therefore an actual positive-grid index earlier than \(j_0\), as required.
The even-q phase sign makes its \(V\) positive.

For even \(q\ge6\), monotonicity of tangent gives the bound by \(2/(\sqrt3\sin(\pi/14))\).
The strict sine chord on \((0,\pi/6)\) gives \(\sin(\pi/14)>3/14\), and \(28/(3\sqrt3)<6\) follows by squaring positive quantities.
The resulting threshold is strictly below \(q\), so this earlier residue is negative while the later nearest positive node remains positive.

For \(q=4\), every odd \(p\ge33\) has the small-step case and the stronger sine margin \(\sqrt2/2\), proving the strict bound \(2\sqrt2<4\).
The only remaining possible conductors are exactly the eight odd integers from 17 to 31.
All eight displayed rows were checked by exact rational arithmetic using \(x/\pi=4-16j/p\).
Every row satisfies \(1\le j<\lfloor p/4\rfloor\), \(7/6\le x/\pi\le11/6\), and \(0<x/(8\pi)<1/4\).
Consequently \(-\sin x\ge1/2\) and \(\tan(x/8)<1\), giving the necessary strict threshold bound below 4.
The table supplies exact symbolic angle comparisons rather than approximate signs, and leaves no permitted conductor unhandled.

These branches cover every \(q\ge3\); together with the even-length obstruction, they exclude every \(L\ge4\) for every positive real amplitude.

<a id="length-three-check"></a>
## Length three, endpoint selection and successes

For \(L=3\), both first and last threshold denominators are strictly positive for \(p\ge9\).
The first and last pole factors \(V\) are positive, so the chamber really requires \(\lambda<T_1\) and \(\lambda>T_n\).
Cancellation using \(\sin(2mu)=2\sin(mu)\cos(mu)\), \(\sin(2u)=2\sin u\cos u\), and \(\sin(8u)=2\sin(4u)\cos(4u)\) yields the displayed ratio exactly.
The factor \(\cos(4u)\) is positive on the whole range and cannot reverse the comparison.
When \(m\ge3\), one has \(p\ge11\), \(3u\le mu<\pi/2\), and the monotonicity of \(\cos^2\) gives the claimed upper bound with \(3u\).

An independent exact polynomial expansion verified
\[
(2z-1)z(4z-3)^2-z(8z^2-8z+1)
=2z(z-1)(16z^2-20z+5),
\]
with coefficient vector \((0,-10,50,-72,32)\).
The exact comparisons \(10/121<1/12\), \((16z^2-20z+5)|_{z=11/12}=1/9\), and \((32z-20)|_{z=11/12}=28/3>0\) were also checked.
Together with \(\pi^2<10\) and \(\sin u<u\), these prove the strict ratio bound \(T_1/T_n<1\), contradicting simultaneous first positivity and last negativity.
This rules out every \(m\ge3\) without using the endpoint or integrality.

The remaining value is \(m=2\), equivalently \(r=4\).
The last-node bound gives \(\lambda>2\), while the independent endpoint gives \(\lambda<4\); positive integer amplitude is therefore exactly three.
At \(m=2,L=3,\lambda=3\), the fixed predecessor's identity is \(h(b)=2b^2(3-b^2)\).
The odd grid has none of its zeros, the first sign fails for every odd \(p\ge13\), and the conductors 9 and 11 have exactly one negative node at the end.
This verifies both directions of the final classification, including \(\kappa=1\) and the separate endpoint value \(P(-1)=2\).

<a id="positive-amplitude-review"></a>
## Verdict and limits

No defect was found in the complete fixed C884v2 argument.
The proof establishes that the strict original chamber for a positive real amplitude forces \(L=3\) and \(r=4\), and that positive integer amplitude together with the strict endpoint permits exactly
\[
(p,r,s,L,\lambda)=(9,4,5,3,3),\qquad(11,4,7,3,3).
\]
All parameter branches, discrete node selections, strict inequalities, finite rational rows and invoked predecessor interfaces were checked at their declared scope.
The independent exact arithmetic checks support identities already fully displayed in the proof; no finite-conductor census is a premise of the unrestricted conclusion.

This is a whole-proof independent finding for the stated positive-amplitude family, not a classification of negative amplitudes or arbitrary central perturbations.
It establishes no complete Mahler-measure value, nonreal residual pair, unrestricted integer supply or Task completion.
The earlier finite signed-amplitude evidence remains separately scoped in R1110v1.
No proof repair or mathematical assessment was made by this reviewer; adoption belongs to the responsible C decision.
