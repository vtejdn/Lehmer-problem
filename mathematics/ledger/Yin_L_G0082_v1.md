---
author: Yin
---

# Binary support need not attain Mahler entropy below measure two

Date: 2026-10-07.
Bounded source reuse and direct proof by the assigned AI ms25_source for Yin, within [G0001](../tasks/Yin_T_G0001_v1.md) and the primary algebraic-entropy strategy.
No new source or numerical theorem is assumed.
The example is explicitly attributed in the retained source to Paul Mercat; no novelty is claimed for the counterexample or its elementary reconstruction here.

<a id="binary-support-counterexample-source"></a>
## Retained source and exact question

The already retained [BV20 v4](../literature/pdf/BV20.pdf), arXiv:1510.04043v4, 23 April 2021, printed/PDF p.31, final paragraph before the references, explicitly gives

\[
 P(t)=t^6+t^5+t^4-t^3+t^2+t+1
 \tag{1}
\]

as an example with \(M(P)<2\) and strictly smaller binary support growth than \(\log M(P)\).
It attributes the observation to Mercat, bibliography item [36], “Private communication”, on p.33.
The stated check is that the eighth support has cardinality less than \(M(P)^8\).
Thus this is a published-in-the-retained-preprint report, not a separately acquired Mercat source.
The actual retained page p.31 was extracted and visually inspected in this round; no communication with the authors occurred.
Existing [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-u001) owns the artifact identity and previous inspection boundaries.
The source uses base-2 logarithms; this note uses natural logarithms.

For any root \(\alpha\) of (1), put

\[
 T_n(\alpha)=\left\{\sum_{j=0}^{n-1}\epsilon_j\alpha^j:
                    \epsilon_j\in\{0,1\}\right\},\qquad
 \rho(\alpha)=\lim_{n\to\infty}\frac{\log|T_n(\alpha)|}{n}.
\]

The limit exists by subadditivity.
Replacing binary digits by fair signs changes the values by an invertible affine transformation, so the support counts are exactly the source's counts.
We prove directly

\[
 |T_8(\alpha)|=252,
 \qquad \frac{511}{256}<M(P)<2,
 \qquad
 \rho(\alpha)\le\frac{\log252}{8}<\log M(P).
 \tag{2}
\]

This settles the general equality question negatively, even for irreducible reciprocal algebraic units.
It does not furnish a near-one family, a positive real Perron root, or a counterexample to equality on a smaller range such as \(M<\theta_0\), where \(\theta_0\) is the plastic constant.
No all-power degree-preservation claim is needed.

<a id="binary-support-counterexample-algebra"></a>
## Irreducibility and conjugate locations

Writing \(u=t+t^{-1}\), one has

\[
 t^{-3}P(t)=T(u),\qquad T(u)=u^3+u^2-2u-3.
 \tag{3}
\]

The only possible rational roots of \(T\) are \(\pm1,\pm3\), and none is a root.
Thus \(T\) is irreducible.
Its discriminant is \(-87<0\), so it has exactly one real root \(u\) and two nonreal conjugate roots.
The exact evaluations

\[
 T(3867/2500)=-2362137/15625000000<0,
 \qquad T(1547/1000)=1503323/10^9>0
 \tag{4}
\]

give \(3867/2500<u<1547/1000<2\).
In the real embedding of \(\mathbb Q(u)\), \(u^2-4<0\), hence \(u^2-4\) is not a square in that field.
Therefore \(t^2-ut+1\) is irreducible over \(\mathbb Q(u)\), and each of its roots has degree six over \(\mathbb Q\).
Since it is a root of the monic degree-six polynomial \(P\), this proves irreducibility of \(P\).
Its constant coefficient is one, so all its roots are units.

The two roots over the real trace \(u\in(-2,2)\) lie on the unit circle and are nonreal.
A root of \(t^2-zt+1\) for either nonreal trace \(z\) cannot be real or have modulus one, since both possibilities would make \(t+t^{-1}\) real.
Each such quadratic has product one, hence one root inside and one outside the circle.
Complex conjugation pairs the two outside roots and the two inside roots.
Consequently \(P\) has exactly one nonreal conjugate pair in each of the inside, unit-circle, and outside regions.
In particular, if \(\alpha\) is an outside root, then

\[
 M:=M(P)=\alpha\overline\alpha=|\alpha|^2>1.
\]

## A short rational Mahler certificate

Divide (1) by the unit-circle quadratic:

\[
 P(t)=(t^2-ut+1)
 \bigl(t^4+(1+u)t^3+(u^2+u)t^2+(1+u)t+1\bigr).
\]

Let \(s=\alpha+\overline\alpha\in\mathbb R\), with the outside pair chosen above.
The quartic is

\[
 (t^2-st+M)(t^2-(s/M)t+M^{-1}).
\]

Comparing the cubic and quadratic coefficients gives

\[
 -s(1+M^{-1})=1+u,
 \qquad M+M^{-1}+s^2/M=u^2+u.
\]

With \(x=M+M^{-1}>2\), elimination yields

\[
 F(x,u):=x^2+(2-u^2-u)x+1-u^2=0.                 \tag{5}
\]

For the interval (4), \(F\) strictly increases with \(x\ge2\): its derivative is \(2x+2-u^2-u>0\), for example using \(u<8/5\).
It strictly decreases with positive \(u\).
Exact rational arithmetic gives

\[
 F\left(\frac{511}{256}+\frac{256}{511},\frac{3867}{2500}\right)
 =-\frac{120653495247}{6684697600000000}<0,
 \qquad
 F\left(\frac52,\frac{1547}{1000}\right)=\frac{12537}{2000000}>0.
 \tag{6}
\]

Monotonicity and (4)--(5) place \(M+M^{-1}\) strictly between the two arguments in (6).
Since \(y\mapsto y+y^{-1}\) is strictly increasing for \(y>1\), this proves \(511/256<M<2\).
Finally, strict convexity, or strict Bernoulli's inequality, gives

\[
 M^8>\left(\frac{511}{256}\right)^8
 =256(1-1/512)^8>256(1-8/512)=252.               \tag{7}
\]

The exact rational signs, rather than a numerical root approximation, are the certificate.

<a id="binary-support-counterexample-collisions"></a>
## Exactly four collisions at length eight

If two binary polynomials of degree at most seven take the same value at \(\alpha\), their difference \(R\), with coefficients in \(\{-1,0,1\}\), is divisible by the irreducible monic \(P\).
Monic polynomial division gives

\[
 R(t)=P(t)(a t+b),\qquad a,b\in\mathbb Z.
\]

The constant and degree-seven coefficients give \(a,b\in\{-1,0,1\}\).
If both are nonzero, either the degree-one coefficient \(a+b\) or the degree-three coefficient \(a-b\) has absolute value two.
Hence any nonzero binary collision difference is exactly \(\pm P\) or \(\pm tP\).

Encode a binary word by the integer \(\sum_{j=0}^7\epsilon_j2^j\), with the low bit recording the constant coefficient.
The positive and negative masks of \(P\) are 119 and 8, with the free degree-seven bit; those of \(tP\) are 238 and 16, with the free constant bit.
Thus the only four unordered collision pairs are

\[
 \{8,119\},\quad\{136,247\},\quad\{16,238\},\quad\{17,239\}.
 \tag{8}
\]

Their eight endpoints are distinct, so there are no larger fibers.
The other 248 words are singletons.
Therefore \(|T_8|=248+4=252\).
The block decomposition also gives the all-length upper bound

\[
 |T_n(\alpha)|\le252^{\lfloor n/8\rfloor}2^{n\bmod8}.
 \tag{9}
\]

Equations (7) and (9) prove (2).
This is a support-count proof.
Shannon entropy is at most support entropy, but the converse comparison is not used.

## Consequences and exact remaining scope

1. A fixed binary cyclic alphabet can fail to realize the total algebraic entropy \(m(P)=\log M(P)\), although \(M(P)<2\).
   Grouping consecutive binary digits into blocks does not remove the loss: using alphabet \(T_k(\alpha)\) under multiplication by \(\alpha^k\) produces exactly \(T_{kn}(\alpha)\), so its entropy per original time remains \(\rho(\alpha)\).
2. The full expanding-place binary attractor for this example has zero two-dimensional Lebesgue measure.
   Indeed the positive-volume argument in [L G0035](Yin_L_G0035_v1.md) would give \(|T_n|\ge M^n\) at every length, contradicting (2).
   Thus even an irreducible unit with expanding determinant below two need not have a positive-volume binary attractor.
   This conclusion does not supply a dimension formula or a statement about the probability weights on that attractor.
3. A parameter-dependent finite alphabet may still attain the total entropy.
   The explicit coordinate-floor alphabet in [L G0032](Yin_L_G0032_v1.md), section “Finite-alphabet capture and the remaining arithmetic question”, supplies that fact for integral companion automorphisms.
   The obstruction here concerns the specified binary cyclic alphabet and its regroupings, not every finite alphabet.
4. The one-real-expanding Pisot/Salem equality in [L G0007](Yin_L_G0007_v1.md#pisot-salem-attainment) is consistent with this example: the outside roots here are a nonreal pair.
   The general equality can no longer be used as a route premise.
   A replacement must state its actual extra hypothesis, or retain the accepted proportional lower bound from BV20.
   No inference about a universal near-one entropy gap follows from this single counterexample near measure two.

## Evidence and review scope

A bounded primary-source search for exact support growth and Mahler measure returned the already retained BV20 interface, including its references to Mercat and finite-alphabet approximation.
Direct inspection of its final page resolved the equality question, and the search stopped.
No newly located article was adopted or downloaded.

Before writing the exact proof, one six-degree diagnostic evaluated numerical roots, the 256 binary remainders, and rational candidate endpoints.
The complete executed program and output, including the unsuccessful coarse upper endpoint, are retained in [J G0012](../computations/programs/Yin_J_G0012/readme.md).
A separate standard-library verifier checked all 32,640 unordered word pairs by direct polynomial division, the eight power remainders, and every retained rational endpoint comparison.
Its permanent execution passed on 2026-10-07.
Numerical roots and library factorization output remain exploratory fields outside that verifier's certification scope.
The exact proof above is independent of enumeration and numerical roots.
Both the source-review agent and coordinator visually inspected retained BV20 p.31 in this round.

## Current proof and retained checking scope

The complete current statement and every original mathematical proof are retained in [C273](../claims/Yin_C_G0273_v1.md#argument), with its actual selected assessment.
The [current whole finding](../audits/reviews/Yin_R_G0533_v1.md#current-mercat-sextic-finding) is self-reviewed.
The [original checking account and exact relationship findings](../audits/reviews/Yin_R_G0533_v1.md#historical-mercat-author-finding) retain their original2026-10-07 inputs, contributions, scopes and limitations.
Original independent wording records the performed checks; it does not establish unrecorded initial isolation or transfer a finding to the new C.
