---
author: Yin
---

<a id="laz78-u001"></a>
# Lazami's fixed polynomial families below two

<a id="compact-pisot-families"></a>
## The compact interval and the fixed pair on a subsequence

Let \(S\) be the set of Pisot numbers and fix \(0<\lambda<1\).
On pp. 3-05 and 3-06 of the [seminar text](readme.md#edition), the final theorem represents the minimal polynomial \(U\) of every element of \(S\) in the indicated interval below \(2-\lambda\), apart from finitely many possible exceptions, in the form
\[
                       WU=A+\delta z^t P,\qquad \delta\in\{1,-1\}.
\]
Here \(t\) is positive, \(P\) is the signed minimal polynomial of an accumulation point of \(S\) below two, and \(A\) is the numerator of an associated rational function \(A/Q\), with \(Q\) the normalized reciprocal polynomial for that point.
Page 3-01 gives \(|A|\le |Q|=|P|\) on the unit circle, with equality at only finitely many points.
The theorem specifies \(W\) as a divisor of a polynomial \(D\) determined by \(A/Q\).

The subsequence in the proof is important when the degree of \(U\) varies.
From any infinite subset of the indicated interval the argument selects a sequence with a fixed \(A/Q\) and \(W\), and exponents \(\lambda_\nu-k\) tending to infinity.
The two nonconstant alternatives for \(K/H\) on p. 3-05 are excluded before the final formula on p. 3-06.
Only the constant sign and the advancing exponent occur there.
For a closed cutoff \(b<2\), one may choose \(2-\lambda>b\).

For each minimal polynomial \(U\), minimize the number of terms of \(UE\) over all products \(E\) of monic cyclotomic polynomials, allowing \(E=1\).
This minimum is bounded on \([1,b]\).
Indeed the extracted subsequence has numerators with at most \(\#\operatorname{supp}P+\#\operatorname{supp}A\) terms, and their coefficient absolute sums are bounded by \(\|P\|_1+\|A\|_1\).
For large exponents the numerators are monic up to sign and their factors outside the Pisot minimal polynomial are cyclotomic by the [circle argument](../Boy96/Yin_U001.md#regular-cofactor).
The constant terms in these associated numerators are nonzero.
Consequently the same contradiction works for an unbounded least coefficient absolute sum.
Any specified finite exceptional set can use its minimal polynomials with multiplier one.
The argument supplies no numerical bound for the exceptional polynomials as \(b\) varies.

This reading checks the statements and fixed-data extraction on pp. 3-01, 3-04, 3-05 and 3-06.
It uses Lazami's compactness theorem and the exclusion of the nonconstant alternatives as established inputs.
Several details of the seminar proof are referred to earlier work and were outside this inspection.
