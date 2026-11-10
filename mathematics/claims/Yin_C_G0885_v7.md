---
author: Yin
---

# Complete cyclic expansion and short adjacent parameters

<a id="statement"></a>
## Expansion from the smallest adjacent product

Use the real positive space and hyperbolic plane of [C885 v5](Yin_C_G0885_v5.md#statement).
Let \(R\) be any positive real isometry extended to fix \(e,f\), let \(k\ge2\) be even, and take
\[
A=R E_{v_1}F_{w_1}\cdots E_{v_{k/2}}F_{w_{k/2}},
\]
with every parameter nonzero.
Set
\[
(p_1,p_2,\ldots,p_k)=(v_1,-w_1,\ldots,v_{k/2},-w_{k/2}),
\qquad l_i=\|p_i\|>0,
\]
and use cyclic indices \(l_{k+1}=l_1\).
Define
\[
\delta=\min_{1\le i\le k}l_i l_{i+1}.
\]
For \(\delta>8\), put
\[
\gamma(\delta)=\frac{\delta-4+\sqrt{\delta(\delta-8)}}4>1.
\]
Then the full original matrix has a positive real eigenvalue \(\Lambda\) satisfying
\[
\Lambda\ge\gamma(\delta)^k,\qquad
M(P_A)\ge\gamma(\delta)^k.                              \tag{1}
\]
Here \(P_A(z)=\det(zI-A)\), and the full monic characteristic-product measure is used even for real parameters.

In the actual positive integral lattice setting, with \(R\) integral and every parameter an allowed nonzero even-norm vector, put \(a_i=l_i^2/2\in\mathbb Z_{\ge1}\).
Then
\[
M(P_A)\le2
\quad\Longrightarrow\quad
a_i a_{i+1}\le16
\quad\hbox{for at least one cyclic adjacent pair}.       \tag{2}
\]
Both vectors of that pair have squared norm at most 32 and their squared-norm product is at most 64.
For \(k\ge4\), actual integral conjugacies and a cusp exchange can place that chosen edge into an interior pair \(F_wE_u\).
The associated integer defect then satisfies
\[
0\le 1-(u,w)+(u,u)(w,w)/4\le25.                         \tag{3}
\]
All these operations preserve the complete polynomial.

These conclusions hold at every even length, with no rank, direction, lattice determinant or positive-isometry-order bound.
For \(k\ge6\), they strengthen the v5 minimum-length test: the globally shortest e-vector and globally shortest f-vector need not be adjacent.
The [adopted v6 five-factor gap](Yin_C_G0885_v6.md#decision-at-most-five-transvection-gap), together with its unchanged retained results, remains valid.
The adjacent-pair conclusion is a necessary condition, not an arbitrary-length gap or a sufficient construction of small measure.

<a id="argument"></a>
## Complete proof and exact inherited inputs

The proof uses the exact null-vector actions, global inversion-distance identity and geometric-tail fixed-point argument of [v5](Yin_C_G0885_v5.md#boundary-action).
It replaces one common exterior domain by cyclically matched exterior domains.
The integer comparison uses the exact strict radical inequality already proved in [v5](Yin_C_G0885_v5.md#integer-short-pair).
Cyclic placement is proved below at arbitrary even length; the four-factor enumeration alone is not used as a general-length premise.

The author-side calculation originated in the continuing adjacent-pair inquiry and is fixed here with its complete statement and proof.
No numerical search, mathematical program or new external theorem is needed.

<a id="cyclic-exterior-domains"></a>
### Actual domains for the entire ordered cycle

Put \(J=s_{e+f}\), \(n(x)=f+x-\|x\|^2e/2\), and \(I(x)=2x/\|x\|^2\).
The retained full-vector identities give
\[
A=R E_{p_1}J\cdots E_{p_k}J,\qquad
E_{p_i}J n(x)=\frac{\|x\|^2}{2}\,n(p_i+I(x)).
\]
Every scalar multiplier is retained.
Write \(f_i(x)=p_i+I(x)\).

Assume \(\delta>8\) and set
\[
\theta=\frac{1+\sqrt{1-8/\delta}}2,\qquad
X_i=\{x:\|x\|\ge\theta l_i\},\qquad X_{k+1}=X_1.
\]
Each \(X_i\) is nonempty and closed in a finite-dimensional positive metric space.
In particular it is complete and excludes zero.
The exact identities
\[
1-\frac2{\theta\delta}=\theta,\qquad
\frac{\theta^2\delta}{2}=\gamma(\delta)>1
\]
follow by expanding the chosen quadratic root.

For \(x\in X_{i+1}\), the actual boundary map satisfies
\[
\|f_i(x)\|
\ge l_i-\frac2{\theta l_{i+1}}
\ge l_i\left(1-\frac2{\theta\delta}\right)
=\theta l_i.
\]
Thus \(f_i:X_{i+1}\to X_i\) for every cyclic index, including \(i=k\).
The positive isometry \(R\) preserves \(X_1\), regardless of the direction of \(p_1\).
Consequently the entire ordered map
\[
F=R\circ f_1\circ\cdots\circ f_k
\]
takes \(X_1\) into itself.
The rightmost map is evaluated first, so its input domain is exactly \(X_{k+1}=X_1\).

<a id="full-eigenvalue"></a>
### Global contraction and the complete eigenvalue

The exact identity
\[
\|I(x)-I(y)\|=\frac{2\|x-y\|}{\|x\|\|y\|}
\]
gives Lipschitz constant at most \(2/(\theta^2l_{i+1}^2)\) for \(f_i\) on its actual input set.
Some individual constants may exceed one; only their full product is used.
Since every intermediate pair of points lies in the next verified input set,
\[
\operatorname{Lip}(F)
\le\frac{2^k}{\theta^{2k}\prod_i l_i^2}
\le\left(\frac2{\theta^2\delta}\right)^k
=\gamma(\delta)^{-k}<1.                                \tag{4}
\]
The middle inequality uses
\[
\prod_i l_i^2=\prod_i(l_i l_{i+1})\ge\delta^k.
\]
No convexity of any \(X_i\) is needed.

Iterating \(F\) from a point of \(X_1\) gives a sequence whose successive differences have a summable geometric bound.
Completeness places its limit in \(X_1\), and continuity makes that limit a fixed point \(x_*\).
In the right-to-left evaluation at \(x_*\), let \(y_i\) be the input to \(f_i\).
The domain calculation gives \(y_i\in X_{i+1}\).
Multiplying all actual full-vector scalars yields
\[
A n(x_*)=\Lambda n(x_*),\qquad
\Lambda=\prod_i\frac{\|y_i\|^2}{2}
\ge\frac{\theta^{2k}\prod_i l_i^2}{2^k}
\ge\gamma(\delta)^k.                                  \tag{5}
\]
The final \(R\) introduces no scalar.
The vector \(n(x_*)\) is nonzero because its f-coordinate is one.
Thus (5) is an actual positive real eigenvalue of the complete original matrix.
Every factor in the full monic Mahler product is at least one, proving (1).

<a id="integer-adjacent-pair"></a>
### The exact discrete consequence

Return to the original integral data.
If every adjacent \(a_i a_{i+1}\) were at least 17, then
\[
\delta\ge2\sqrt{17}>4+3\sqrt2.
\]
The last inequality and \(\gamma(4+3\sqrt2)=\sqrt2\) have already been checked exactly in v5.
Strict monotonicity of \(\gamma\) on its domain therefore gives
\[
M(P_A)\ge\gamma(\delta)^k>2^{k/2}\ge2.
\]
This contradicts \(M(P_A)\le2\), proving (2).
Since both half-norms are positive integers, each is at most 16 on the selected edge.
The individual squared-norm and product bounds follow.

This includes neutral integral outputs with all displayed parameters nonzero.
A zero parameter is removed before this statement is used, and a shorter remaining word need not satisfy a bound on every displayed parameter.
No estimate is asserted at the real boundary \(\delta=8\).

<a id="arbitrary-length-cyclic-placement"></a>
### Exact cyclic placement at arbitrary even length

Write the unsigned alternating parameter list as
\[
(q_1,\ldots,q_k)=(v_1,w_1,\ldots,v_{k/2},w_{k/2}).
\]
Its last factor is \(F_{q_k}\).
Conjugating the full word by that factor gives
\[
F_{q_k}AF_{-q_k}
=R F_{R^{-1}q_k}E_{q_1}F_{q_2}\cdots E_{q_{k-1}}.
\]
The integral isometry exchanging \(e,f\) and fixing the positive space commutes with \(R\).
Its conjugation changes this to the alternating word with parameter list
\[
\sigma(q_1,\ldots,q_k)
=(R^{-1}q_k,q_1,\ldots,q_{k-1}).                       \tag{6}
\]
This proves the general rotation formula directly.

Every step is an integral conjugacy, and every vector transported across the positive factor keeps its norm because \(R^{-1}\) is a positive integral isometry.
Iteration moves each cyclic edge into any chosen adjacent position.
For \(k\ge4\), choose positions two and three, giving an interior \(F_wE_u\) pair.
This includes the original edge crossing the positive factor; its actual twisted parameter is used, not an untwisted vector substituted into the word.
For \(k=2\), the two parameters already satisfy the stated norm bounds; no interior pair is claimed.

For the selected interior pair, put \(a=(u,u)/2\), \(b=(w,w)/2\), \(c=(u,w)\).
Then \(a,b\ge1\), \(ab\le16\), and Cauchy--Schwarz gives
\[
0\le(\sqrt{ab}-1)^2
\le1-c+ab
\le1+2\sqrt{ab}+ab
\le25.
\]
The defect is an integer, proving (3).
Its exact zero classification and integral shortening remain those of the retained [v4 cusp-defect result](Yin_C_G0885_v4.md#cusp-defect-reduction).

<a id="limits"></a>
## What the necessary adjacent pair leaves unresolved

A low-measure word of any even length has an actual adjacent short pair after the stated cyclic placement.
The result does not bound the other parameters.
It does not imply that several disjoint short pairs exist, nor that the pair decomposition can be repeated while preserving an integral positive factor.

The [v6 rational pair decomposition](Yin_C_G0885_v6.md#middle-pair-decomposition) introduces a cusp scaling and a generally rational positive isometry.
At greater length, further transvections remain, and the effect of the changed lattice, denominators and possible zero parameters must be handled on that complete word.
No finite-order assertion about the rational positive factor follows from its orthogonality.

The unchanged five-factor and bounded-count/bounded-norm gaps retain their exact scopes.
No arbitrary-length gap, new value below \(6/5\), numerical sampling outcome or positive-to-one sequence is proved here.
The [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Assessment history

### Decision cyclic-adjacent-short-pair

| Field | Value |
| --- | --- |
| date | 2026-11-10T05:32 |
| status | proved |
| reason | The complete independent review verifies every cyclic domain, product contraction, full-vector multiplier, actual eigenvalue, integer threshold and arbitrary-length integral cyclic placement without a gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cyclic expansion and adjacent short pair](#statement) | Every stated even length, real positive factor and nonzero parameter list, with the full integral consequence, placement and defect range. |
| argument | [Complete cyclic proof](#argument) | Matched exterior domains, actual ordered contraction, full eigenvalue and measure, integer comparison and general cyclic conjugacy. |
| dependency | [Adopted five-factor theorem](Yin_C_G0885_v6.md#decision-at-most-five-transvection-gap) | The entire retained theorem and its inherited scope, unchanged. |
| dependency | [Full boundary action](Yin_C_G0885_v5.md#boundary-action) | Exact reflection signs, null-vector normalization, inversion and every scalar multiplier. |
| dependency | [Global distance and fixed-point argument](Yin_C_G0885_v5.md#exterior-contraction) | Exact inversion-distance identity and geometric-tail proof on a complete exterior set. |
| dependency | [Exact integer threshold](Yin_C_G0885_v5.md#integer-short-pair) | Strict radical comparison, gamma value and monotonicity for the product threshold sixteen. |
| dependency | [Cusp-defect reduction](Yin_C_G0885_v4.md#cusp-defect-reduction) | Retained exact equality classification and local integer shortening at a zero-defect pair. |
| dependency | [Integer covariance](../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Positive-factor movement, transvection inverses and integral complete-polynomial-preserving conjugacy. |
| review | [Complete independent cyclic finding](../audits/reviews/Yin_R_G1114_v14.md#cyclic-adjacent-expansion-review) | Whole statement, argument and actual retained interfaces, including zero exclusions, the real boundary and the limits of one necessary pair. |

## Current assessment

[Selected decision](#decision-cyclic-adjacent-short-pair)
