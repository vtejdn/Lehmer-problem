---
author: Yin
---

# No integral graph partner for the 10,236 tabulated short coordinates

<a id="pole-norms"></a>
## No positive norm-one value at any height in the source table

For each of the 10,236 reciprocal polynomials \(S\) in Mossinghoff's May 31, 2026 table, each \(\sigma=\pm1\), and every integer \(q\ge2\),
\[
 q^{D}S\bigl(\sigma(q+1)/q\bigr)\ne1,\qquad D=\deg S .
\]
Thus every listed input fails the positive signed pole norm before any further test of its signature or dependence of the two units.
This excludes the [norm-one construction](../../../claims/Yin_C_G0345_v883.md#criterion) for the tabulated polynomials as minimal polynomials of the short coordinate \(T\).
The [endpoint test](#endpoint) below excludes the other possible pole divisors for every signed input as well.
Consequently no root of these polynomials, in either orientation, can serve as the short coordinate \(T\) of an integral unit pair on the curve, for any integer \(q\ge2\).
This conclusion applies to a proposed generator \(\beta\) when its signed short power \(T=\pm\beta^u\) has one of the tested minimal polynomials.

The [fixed table](https://github.com/mossinghoff/Mahler-Measure-Database/blob/7e3798516710370a758e16eb5de6bccbee98bb6a/AllSmallMeasures_200.txt) lists known primitive irreducible noncyclotomic polynomials of multiplicative Mahler measure less than \(1.3\) through degree 200, up to reflection.
Its author reports completeness in this joint size and degree range through degree 44, accounting for 944 of the inputs.
Rows above degree 44 are tested individually.
The calculation uses the coefficient columns; the displayed decimal measures and exterior root counts do not enter the arithmetic. [Source scope](../../../audits/literature/Mos26/readme.md#complete-small-cores)

<a id="filter"></a>
## A finite test for all heights at a fixed polynomial

Fix either orientation and write \(S_\sigma(X)=S(\sigma X)=X^D+c_1X^{D-1}+\cdots+1\), since \(D\) is even.
The polynomial \(F(Q)=Q^D S_\sigma(1+1/Q)\) is integral.
Its constant and linear terms are \(1\) and \((D+c_1)Q\).
Reciprocity and even degree give \(F(-Q-1)=F(Q)\) by reversing the roles of \(Q\) and \(Q+1\).
Thus if \(F(q)=1\), both \(q\) and \(-q-1\) are roots of \(F-1\).
After dividing out the lowest power of \(Q\), the rational-root theorem forces both \(q\) and \(q+1\) to divide the first nonzero coefficient, so their product divides it.
In particular \(q(q+1)\mid D+c_1\) when \(D+c_1\ne0\).
An identically constant \(F=1\) would require \(S_\sigma(X)=(X-1)^D\), which is outside the source.

All 20,472 signed inputs have \(D+c_1\ge8\).
Divisibility by \(q(q+1)\) leaves 7,965 evaluations, all at \(q\le13\).
The [program](pole_catalogue.py) reconstructs both halves of each reciprocal polynomial, tests both orientations and computes each remaining \(F(q)\) by homogeneous Horner evaluation over the integers.
None equals one.
A separate implementation used only \(q\mid D+c_1\) and evaluated the homogeneous monomials directly modulo 65,537 for 102,735 signed input-height pairs.
Three modular values equaled one; exact integer evaluation excluded all three.

<a id="endpoint"></a>
## All pole divisors for an integral second coordinate

Write \(p=q+1\) and \(Y=(pT-q)/(p-qT)\) at a root \(T\) of \(S_\sigma\).
The denominator is nonzero since \(T\) is a unit and \(p/q>1\) is rational.
The identity
\[
 (p-qT)(Y+1)=T+1
\]
shows that an integral \(Y\) requires \(p-qT\) to divide \(T+1\) in the ring of integers of \(\mathbb Q(T)\).
Taking norms implies that \(K=F(q)\) is a signed divisor of the nonzero integer \(S_\sigma(-1)\).
Also \(F(0)=F(-1)=1\), so \(Q(Q+1)\) divides \(F(Q)-1\) in \(\mathbb Z[Q]\).
If \(K\ne1\), it follows that
\[
 q(q+1)\le |K-1|\le |S_\sigma(-1)|+1.
\]
This gives a second finite test, independent of any restrictions on the other conjugates of \(T\).
Over all signed inputs the largest endpoint norm is 89.
For all 3,793 input-height pairs left by the second bound, exact evaluation found no \(K\ne1\) dividing the endpoint norm.
Together with the positive norm-one test this proves the assertion for all listed short coordinates.

<a id="reproduction"></a>
## Reproduction

From the repository root run the following commands with Python 3, retrieving the [registered local original](../../../literature/pdf/Mos26/AllSmallMeasures_200.txt) if it is missing.

~~~sh
curl --fail --location --create-dirs --output mathematics/literature/pdf/Mos26/AllSmallMeasures_200.txt https://raw.githubusercontent.com/mossinghoff/Mahler-Measure-Database/7e3798516710370a758e16eb5de6bccbee98bb6a/AllSmallMeasures_200.txt
python -B mathematics/computations/programs/Yin_J_G0185/pole_catalogue.py
~~~
