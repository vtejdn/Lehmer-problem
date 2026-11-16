---
author: Yin
---

# Review of the radial lower bound and the half-degree obstruction

An agent outside the development of C345v3 reviewed the complete fixed claim for Yin on 2026-11-16T12:52 UTC.
The assignment supplied its scope and fixed targets without development discussion or a previous verdict on the proof.

<a id="radial-half-degree-review"></a>
## Interior radius selection and both encoded seeds

The two radial estimates hold with the stated constants for every permitted real monic seed and complex phase.
Their application gives the finite square-root bound and both lower limits for either choice of half-degree seed at every index.

### One radius for all exterior roots

Writing \(g(z)=\prod_\alpha(1-\alpha z)\), the reality of \(f\) permits conjugation of the multiset of \(\alpha\)'s in the denominator of \(f/g\).
An interior root gives a Blaschke factor of modulus at most one, and a unit root gives a constant factor of modulus one after cancellation.
An exterior root gives a unimodular constant times the inverse Blaschke factor at \(1/\bar\alpha\).
If \(b=1/|\alpha|\), then on \(|z|=\rho\) the squared modulus of the direct Blaschke factor is
\[
 \frac{\rho^2+b^2-2\rho b\cos\phi}{1+\rho^2 b^2-2\rho b\cos\phi}.
\]
Its minimum occurs at \(\cos\phi=1\) because the denominator exceeds the numerator by \((1-\rho^2)(1-b^2)>0\).
Putting \(\rho=1-t\), \(b=1-x\), the maximum inverse modulus is \((x+t-xt)/|x-t|\), bounded by the expression used in (3).

When \(0<x\le u/2\), the logarithm is \(\log(1+2x/(t-x))\le4x/u\).
When \(x\ge4u\), the quotient is at most three throughout the interval.
For \(1/2\le x/u\le4\), scaling to an interval of length one bounds the average by \(\log 6+2\), since \(\int_{-1}^1-\log|y|\,dy=2\).
This is less than \(8\min(1,x/u)\) throughout the middle range.
The finitely many singular radii have integrable logarithms.
Summing before selecting the radius includes all multiplicities and gives a finite value at most \(8L(u)/u\) somewhere, since \(x=1-e^{-s_i}\le s_i\).
At any such radius \(g\) is nonzero on the whole circle.
If there are no exterior roots, \(g\) is nonzero throughout the open disk and every candidate radius works.

Thus \(|z^Nf/g|\le\exp(-Nu+8L(u)/u)<1\) on one circle.
The reverse triangle inequality against \(|\tau|=1\) gives the stated positive pointwise lower bound on \(|D|/|g|\).
Jensen's formula bounds the mean of \(\log|D|\) on this circle from above by its mean on the unit circle.
For \(g\), each factor \(1-\alpha z\) contributes \(\log^+(\rho|\alpha|)\), so the loss from the unit-circle mean is exactly \(\sum_i\min(s_i,-\log\rho)\).
Since \(t\le2u\le1/2\), this loss is at most \(\sum_i\min(s_i,4u)\le4L(u)\).
This proves (1), including circle roots of \(f\) and common factors of \(f,g\).
In (2), \(u=(8k+v)/N\le1/4\), \(Nu-8L(u)/u\ge v>0\), and \(4L(u)\le4k(8k+v)/N\).
Taking the measure of a factor is justified in the stated case when its complementary factors all have measure one.

### The original reciprocal input

For each sign \(e\), C345v1 gives a monic integral degree-\(N+1\) seed with constant \(e\) and \(z^N f_e+f_e^*=(z+1)P\).
In that formula the two overlapping coefficients sum to the identical middle coefficients of \((z+1)P\), and the remaining coefficients pair by reversal.
If \(f_e^*=e f_e\), then \(z^N+e\) would divide \((z+1)P\).
It is coprime to the irreducible \(P\) since \(N<2N\), and \(N\ge2\) rules out divisibility of \(z+1\).
Thus both choices are nonreciprocal, independently of which choice removes the reciprocal gcd.
If all the monic irreducible factors of a seed were reciprocal up to sign, its product would also be.
Each factor is an integral unit polynomial by the unit constant of the seed.
Applying Smyth to one nonreciprocal factor and using nonnegative logarithmic measure for the remaining monic factors gives \(m(f_e)\ge m_0\).
In particular \(k\ge1\), and the exact identity with \((z+1)P\) gives \(m(D)=m(P)\).

For \(N\ge512k^2\) the condition \(N\ge4(8k+4)\) holds and \(4k(8k+4)/N\le3/32\).
For an explicit strict comparison, \(e^4>50\) by the exponential series, so \(-\log(1-e^{-4})<1/49\).
Thus \(3/32-\log(1-e^{-4})<3/26<\tfrac12\log(13/10)<m_0/2\), using \(\log(1+x)>x/(1+x)\) and the plastic cubic at \(13/10\).
This verifies (4) and its contrapositive \(k>\sqrt d/32\) when \(m(P)\le m_0/2\).

For a positive sequence \(m(P)\to0\), bounded degree along a subsequence would bound the integer coefficients there by the elementary symmetric expansion and bounded measure, which permits only finitely many positive measures.
Consequently \(N\to\infty\).
Fix \(a>0\) and put \(u=a/\sqrt N\), eventually in the permitted radial range.
If \(L(u)\) were below both \(m_0/4\) and \(a^2/8\) by a fixed \(\epsilon>0\) along a subsequence, the exponent \(-Nu+8L(u)/u\) would be at most \(-8\epsilon\sqrt N/a\).
The logarithmic correction would tend to zero while \(m(f)-4L(u)\ge4\epsilon\).
The resulting positive lower bound for \(m(P)\) contradicts the hypothesis.
This proves the first lower limit in (5).
Taking \(a=\sqrt{2m_0}\) makes its two competing lower bounds equal to \(m_0/4\), and \(L(u)\le ak/\sqrt N\) gives \(\liminf k/\sqrt N\ge\sqrt{m_0/32}\).
All the constants used in these deductions allow the seed sign to vary with the input, and no root-separation premise enters the estimates.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Radial and half-degree finding](#radial-half-degree-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Radial and half-degree finding](#radial-half-degree-review) | [C345v3 statement](../../claims/Yin_C_G0345_v3.md#statement) | Both moving-seed lower bounds, full polynomial or sole positive factor, all complex phases and both root-count boundaries. |
| [Radial and half-degree finding](#radial-half-degree-review) | [C345v3 radial proof](../../claims/Yin_C_G0345_v3.md#circle) | Inverse factors, three radial ranges, integrable singularities, common circle, Jensen losses and substitution for (2). |
| [Radial and half-degree finding](#radial-half-degree-review) | [C345v3 reciprocal application](../../claims/Yin_C_G0345_v3.md#half-degree) | Each seed, the strict finite implication, degree growth and both pointwise-in-\(a\) and optimized lower limits. |
| [Radial and half-degree finding](#radial-half-degree-review) | [C345v1 two seeds](../../claims/Yin_C_G0345_v1.md#universal-half-degree-delay-encoding) | Exact integral unit construction, both signs nonreciprocal, and the complete factorization \((z+1)P\). |
| [Radial and half-degree finding](#radial-half-degree-review) | [Smy08 nonreciprocal integer](../literature/Smy08/Yin_U002.md#smy08-reciprocal-number) | Plastic-number lower bound for a nonreciprocal monic irreducible factor at the recorded statement scope. |
| [Radial and half-degree finding](#radial-half-degree-review) | [C345v1 previous alternative](../../claims/Yin_C_G0345_v1.md#encoding-inverse-and-cyclic-cost) | Comparison with the previous conditional separated-root argument. |
| [Radial and half-degree finding](#radial-half-degree-review) | [Hir06 fixed-seed background](../literature/Hir06/Yin_U001.md#hir06-u001) | Context for exterior-root convergence with a fixed seed. |
