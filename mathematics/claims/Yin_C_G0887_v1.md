---
author: Yin
---

# A uniform 6/5 exclusion for Gaussian single-coordinate cyclic kicks

<a id="statement"></a>
## Exact family and conclusion

For every integer \(m\ge1\) and integer \(b\), define
\[
g_{m,b}(z)=(z^m-1)\bigl(z^2+(1-ib)z-1\bigr)+2z,
\qquad
P_{m,b}(z)=g_{m,b}(z)\overline{g_{m,b}}(z),
\tag{1}
\]
where the bar conjugates coefficients.
Then \(P_{m,b}\) is a monic reciprocal integer polynomial of degree \(2m+4\), with constant coefficient one.
Its complete multiplicative Mahler measure satisfies
\[
M(P_{m,b})=1
\quad\hbox{or}\quad
M(P_{m,b})>6/5.
\tag{2}
\]
Equality to one occurs exactly at
\[
(m,b)=(1,0),(1,1),(1,-1),(3,0).
\tag{3}
\]
For \(m\ge5\), the stronger bound \(M(P_{m,b})>36/25\) holds, even for every real \(b\).

The statement concerns the entire norm polynomial, including all factors and multiplicities.
It does not assert a uniform gap for all Gaussian Hermitian isometries, longer words, different translation vectors or arbitrary integer polynomials.
Its [matrix realization](../computations/programs/Yin_J_G0160/readme.md#polynomial-input) motivates this input family but is not a proof dependency of (2).
The present project deduction was developed by the strategic collaborator and main researcher and is adopted at the [selected decision](#decision-gaussian-one-coordinate-gap) after complete independent inspection.

<a id="argument"></a>
## Complete proof and actual dependencies

The analytic part uses the classical Rouché theorem for a disk: a strict boundary inequality \(|h|<|f|\) preserves the number of zeros of \(f\) and \(f+h\) in that disk, counting multiplicity.
The accepted source statement is [Sha23-U001](../audits/literature/Sha23/Yin_U001.md#sha23-u001), Corollary 7.44 with the multiplicity convention of Theorem 7.43, at that unit's recorded statement and short-proof inspection depth.
The finite part uses the exact complete-polynomial inputs and all-root enclosures in [J160](../computations/programs/Yin_J_G0160/readme.md#small-degree-boundary).
No original-unitary classification, degree-normalized height, fixed-support gap or preliminary numerical root screen enters this proof.

Write
\[
a(z)=z^2+(1-ib)z-1,\qquad
a^\#(z)=z^2\overline a(1/z)=1+(1+ib)z-z^2.
\]
Then \(g_{m,b}=z^ma+a^\#\), and reversing and conjugating at degree \(m+2\) returns the same polynomial.
Writing its real and imaginary coefficient parts as \(A\) and \(B\) gives \(P=A^2+B^2\).
For integer \(b\), this proves integer coefficients; the endpoint coefficients, degree and reciprocal identity follow directly.
Conjugating coefficients does not change root moduli, so
\[
M(P_{m,b})=M(g_{m,b})^2.
\tag{4}
\]
Every root and every multiplicity is included in this equality.

<a id="rouche-large-cycle"></a>
## A uniform rational-radius comparison for every large cycle

Set \(r=6/5\) and \(\delta=r-r^{-1}=11/30\).
For real \(b\) and \(1\le|z|\le r\),
\[
\Re\left(\frac{a(z)}z\right)
=\Re(z-z^{-1})+1
\ge1-\delta=19/30>0.
\tag{5}
\]
In particular, \(a\) has no root in this closed annulus.
It has no unit-circle root, and the product of the moduli of its two roots is one because its constant coefficient is minus one.
Thus it has one root inside the unit circle and one root outside \(|z|=r\), counting multiplicity.

On \(|z|=r\), put \(Y=a(z)/z=x+iy\).
One has \(19/30\le x\le41/30\) and \(a^\#(z)/z=2-Y\).
For \(x\ge1\),
\[
\left|\frac{2-Y}{Y}\right|^2
=1+\frac{4(1-x)}{x^2+y^2}\le1.
\]
For \(19/30\le x\le1\), dropping \(y^2\) in the positive term gives
\[
\left|\frac{2-Y}{Y}\right|
\le\frac{2-x}{x}
\le\frac{41}{19}.
\]
Consequently
\[
\left|\frac{a^\#(z)}{a(z)}\right|\le\frac{41}{19}
<\left(\frac65\right)^5
\le |z|^m
\qquad(m\ge5).
\tag{6}
\]
The strict rational comparison follows from \(41\cdot3125=128125<147744=19\cdot7776\).
There are no zeros of \(a\) on the circle, by (5).

Rouché applied to \(z^ma\) and \(a^\#\) now counts exactly \(m+1\) roots of \(g_{m,b}\) in \(|z|<r\), with none on the boundary.
The degree is \(m+2\), so a remaining root has modulus greater than \(r\).
Therefore \(M(g_{m,b})>6/5\), and (4) gives \(M(P_{m,b})>36/25\).
This argument does not assume that \(b\) is integral.

<a id="small-degree-reduction"></a>
## The exact finite set at small degree

It remains to consider \(1\le m\le4\).
Assume \(M(P_{m,b})\le6/5\), and put \(d=m+2\), so \(3\le d\le6\).
By (4), every root \(\alpha\) of the monic \(g_{m,b}\) has
\[
|\alpha|\le M(g_{m,b})\le\sqrt{6/5}<7/6.
\]
The imaginary part of the coefficient of \(z^{d-1}\) in \(g_{m,b}\) is \(-b\), including the overlapping terms at \(m=1\).
The first root sum therefore has imaginary part \(b\), whence
\[
|b|\le\sum_{\alpha:g_{m,b}(\alpha)=0}|\alpha|
\le d\sqrt{6/5}<d+1.
\]
Integrality gives \(|b|\le d=m+2\).
Replacing \(b\) by \(-b\) conjugates \(g\) and leaves \(P\) unchanged.
Thus exactly the following 22 nonnegative-parameter inputs cover every possible small-measure case:
\[
m=1,2,3,4,\qquad b=0,1,\ldots,m+2.
\tag{7}
\]
No assertion that a large parameter is unlikely replaces this finite reduction.

The completed [J160 boundary calculation](../computations/programs/Yin_J_G0160/readme.md#small-degree-boundary) factors each complete integer \(P\), verifies the factor product, and encloses the contribution of every root with every multiplicity.
Its three neutral nonnegative inputs are exactly \((1,0),(1,1),(3,0)\).
Their identities are
\[
\begin{split}
P_{1,0}&=(z+1)^2(z^2-z+1)^2,\\
P_{1,1}&=(z^2+1)(z^4+1),\\
P_{3,0}&=(z+1)^2(z^4-z^2+1)^2.
\end{split}
\tag{8}
\]
Every factor in (8) is cyclotomic.
All other nineteen enclosures in (7) lie strictly above \(6/5\); the smallest is at \((m,b)=(4,1)\), with
\[
2.83097660999535<M(P_{4,1})<2.83097660999537.
\tag{9}
\]
These are complete-measure enclosures, not a count of approximated exterior roots.

The finite results, the integer-parameter reduction and the large-cycle argument prove (2) and (3).
The finite arithmetic relies on the exact factorization and Arb root-isolation implementations at the explicitly recorded [J156 implementation-review scope](../audits/reviews/Yin_R_G1111_v1.md#sampler-implementation-review).
The [complete independent finding](../audits/reviews/Yin_R_G1107_v37.md#gaussian-one-kick-gap-review) checks this proof, its exact source interface and all 22 finite inputs at that computational trust boundary.

## Current assessment
[Selected decision](#decision-gaussian-one-coordinate-gap)

## Assessment history

### Decision gaussian-one-coordinate-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T08:49 |
| status | proved |
| reason | Complete independent review verifies the all-parameter analytic exclusion, exact small-degree integer reduction, all 22 complete-measure certificates and the four neutral parameter pairs. The result closes this one family only. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact family and conclusions](#statement) | Every positive integer m and integer b, exact measure-one cases, complete 6/5 gap and the stronger real-b large-cycle bound. |
| argument | [Complete proof and dependencies](#argument) | Norm product, reciprocal identity and actual source and computational boundaries. |
| argument | [Large-cycle comparison](#rouche-large-cycle) | Uniform rational-radius inequality, strict disk comparison and all root multiplicities. |
| argument | [Finite integer reduction](#small-degree-reduction) | Every omitted integer parameter, negative-b symmetry, exact neutral identities and complete 22-input conclusion. |
| dependency | [Classical disk theorem](../audits/literature/Sha23/Yin_U001.md#sha23-u001) | Corollary 7.44 with the zero-order convention of Theorem 7.43 at the retained source depth. |
| dependency | [Complete finite boundary](../computations/programs/Yin_J_G0160/readme.md#small-degree-boundary) | All 22 exact inputs, three nonnegative neutral cases, nineteen strict complete-measure exclusions and exact minima. |
| dependency | [Native boundary program](../computations/programs/Yin_J_G0160/one_kick.py) | Boundary branch only, exact coefficients, full factor and root multiplicities and completed-output semantics. |
| dependency | [Full-product evaluator](../computations/programs/Yin_J_G0156/sampler.py) | The actual complete-polynomial evaluator and used helpers, with trusted FLINT/Arb arithmetic. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v37.md#gaussian-one-kick-gap-review) | Entire fixed statement, proof, source interface and all finite inputs; excludes the matrix motivation and initial twelve-input exploration. |
