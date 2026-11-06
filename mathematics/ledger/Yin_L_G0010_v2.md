---
author: Yin
---

# Integer reciprocal moments near a positive Toeplitz boundary

Date: 2026-11-05.
Author exploration for Yin under [the unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
This version retains a bounded failure test for integer power-sum moments and proximity to positive semidefinite Toeplitz matrices.
The responsible delegate developed and checked the calculations; this is author work, not independent review.
No novelty, original-input counterexample, uniform Mahler gap or adoption into the Task completion chain is asserted.

<a id="integer-moment-near-psd-scope"></a>
## Question, existing input and outcome

The attempted mechanism was that reciprocity makes radial errors quadratic, after which integer moments or Schur elimination might force a dimension-independent distance from the positive semidefinite boundary.
The relevant earlier mathematics remains in [L10 v1](Yin_L_G0010_v1.md#general-reciprocal-necessary-bound) and its complete retained statement in [C215 v1](../claims/Yin_C_G0215_v1.md#statement).
Their inverse-conjugate pairing already bounds the total negative spectrum by
\[
\frac{\nu(K_N)}N\le f_N(m)-1,\qquad
f_N(x)=\frac{\sinh(Nx)}{N\sinh x},\qquad f_N(0)=1.
\]
The right-hand side has expansion beginning with \((N^2-1)m^2/6\).
Those materials also retain the exact integer moments, rank-two displacement, inertia and discriminant-times-integer-square maximal minors.
Their proofs and actual review scopes are reused, not reproduced or extended here.

The present test concerns a fixed three-by-three matrix as its integer diagonal \(d\) tends to infinity.
It supplies integer first and second moments, compatible first two Newton coefficients, a positive semidefinite comparison with the same diagonal, and a vanishing negative eigenvalue.
A real reciprocal root construction additionally has total logarithmic measure tending to zero while preserving those two integer moments.
Its full polynomial is demonstrably not integral and has repeated circle roots.
Consequently the test rules out a dimension-independent rounding margin from these specified local data, but supplies no counterexample in the original irreducible integer domain.
The new calculations are retained as this local mechanism test, not as an additional formal Claim or an accepted completion-chain theorem.

The 2026-11-05 local comparison inspected L9, L10 v1, C26, C30 and C215 and searched Claims, ledgers, drafts and source audits for power-sum Toeplitz moments, Schur parameters, near-positive-semidefinite rounding and the displayed quadratic relation.
No matching account of this particular three-by-three test was located in that inspected scope.
No external theorem or new external source is used in the calculations below, and no literature novelty conclusion follows from that local search.
In particular, the explicit elimination identity below requires no general Schur algorithm or positive moment-extension theorem.

<a id="integer-near-psd-three-moment-construction"></a>
## An infinite integer family and its exact matrix

Choose integers \(x,a\) by starting at
\[
(x,a)=(65,23)
\]
and iterating
\[
x'=17x+48a,\qquad a'=6x+17a.
\tag{1}
\]
Set \(d=(x-1)/2\).
The initial pair has \(x^2-8a^2=-7\), \(x\equiv1\pmod4\), \(a\) odd and \(d=32\).
Direct expansion gives
\[
(17x+48a)^2-8(6x+17a)^2=x^2-8a^2.
\]
Also \(x'\equiv x\pmod4\), and \(a'\) is odd whenever \(a\) is odd.
Thus every pair has even \(d\ge32\), odd positive \(a\), and
\[
2a^2=d^2+d+2.
\tag{2}
\]
Both positive coordinates strictly increase under (1), so this gives infinitely many such pairs with \(d\to\infty\).
No classification of solutions of a Pell equation is invoked.

Consider the integer moment prefix \(s_0=d,s_1=a,s_2=1\) and its real symmetric Toeplitz matrix
\[
T=\begin{pmatrix}
d&a&1\\
a&d&a\\
1&a&d
\end{pmatrix}.
\tag{3}
\]
Its one-by-one principal minors equal \(d>0\).
Its two-by-two principal minors are \(d^2-1>0\) or
\[
d^2-a^2=\frac{(d-2)(d+1)}2>0.
\]
All proper principal minors are therefore positive.
The full determinant is
\[
\det T=(d-1)(d^2+d-2a^2)=-2(d-1)<0.
\tag{4}
\]

The vector \((1,0,-1)\) has eigenvalue \(d-1\).
On the remaining symmetric subspace, the matrix in the orthonormal basis \((1,0,1)/\sqrt2,(0,1,0)\) is
\[
\begin{pmatrix}d+1&\sqrt2a\\ \sqrt2a&d\end{pmatrix}.
\]
Using (2), its smaller eigenvalue is exactly
\[
\lambda_{\min}(T)
=\frac{2d+1-\sqrt{(2d+1)^2+8}}2
=\frac{-4}{\sqrt{(2d+1)^2+8}+2d+1}.
\tag{5}
\]
The other two eigenvalues are positive, while this negative eigenvalue tends to zero with magnitude asymptotic to \(1/d\).
The integral nonzero determinant in (4) thus coexists with a vanishing negative spectral margin.

The first two Newton coefficient equations give
\[
c_1=-s_1=-a,\qquad
c_2=\frac{s_1^2-s_2}{2}=\frac{a^2-1}{2}\in\mathbb Z.
\tag{6}
\]
This verifies exactly these initial coefficient-integrality conditions.
It asserts neither the remaining Newton conditions nor the existence of a full integer polynomial realizing the prefix with the later root geometry.

<a id="integer-near-psd-boundary-elimination"></a>
## Fixed-diagonal positive comparison and elimination scale

Put
\[
a_*=\sqrt{\frac{d(d+1)}2},\qquad
T_*=\begin{pmatrix}d&a_*&1\\a_*&d&a_*\\1&a_*&d\end{pmatrix}.
\]
Choose \(\theta_*\in(0,\pi/2)\) with \(\cos\theta_*=a_*/d\).
A multiset consisting of \(d/2\) copies of each of \(e^{i\theta_*}\) and \(e^{-i\theta_*}\) has moments \(d,a_*,1\), because
\[
d\cos(2\theta_*)=2a_*^2/d-d=1.
\]
Its Toeplitz moment matrix is \(T_*\) and is a sum of positive rank-one Hermitian matrices.
It has rank two and is positive semidefinite.
This is a repeated-root circle multiset, not an asserted irreducible integer polynomial.

Equation (2) gives
\[
a-a_*=\frac1{a+a_*}\longrightarrow0.
\tag{7}
\]
The diagonal and second lag are unchanged.
The maximum entry difference is (7), and the operator norm difference is \(\sqrt2(a-a_*)\), obtained from the three-vertex off-diagonal matrix.
Hence an integer Toeplitz matrix with all proper principal minors positive can lie arbitrarily close to the positive semidefinite cone even with its diagonal fixed.

For the proposed Schur-parameter implementation, the relevant second elimination ratio is explicitly
\[
\kappa_2=\frac{d s_2-s_1^2}{d^2-s_1^2}
=\frac{d-a^2}{d^2-a^2}
=-1-\frac2{d^2-a^2}.
\tag{8}
\]
Its relation to the determinant follows by direct factorization:
\[
\det T
=\frac{(d^2-a^2)^2}{d}\left(1-\kappa_2^2\right).
\tag{9}
\]
Thus the first two-by-two block is positive definite, but the next elimination ratio lies outside \([-1,1]\) by
\[
|\kappa_2|-1
=\frac4{(d-2)(d+1)}
=O(d^{-2}).
\tag{10}
\]
The rational denominator carries the degree dependence.
Changing from minors or eigenvalues to this ratio therefore does not create a dimension-independent escape margin.

<a id="integer-near-psd-real-root-model"></a>
## Real reciprocal roots with the same integer prefix and small total measure

The same pair \((d,a)\) admits an explicit real reciprocal root model realizing (3) with positive total logarithmic measure tending to zero.
This model will be proved nonintegral below.

For \(y\ge1\), define
\[
D_1(y)=d+4(y-1),\qquad
D_2(y)=d+8(y^2-1),
\]
\[
H(y)=D_2(y)\left(\frac{2a^2}{D_1(y)^2}-1\right)-1.
\tag{11}
\]
The function is continuous on \([1,1+1/d]\), and (2) gives \(H(1)=2/d>0\).
At \(y_+=1+1/d\), one has
\[
D_1(y_+)=d+4/d,\qquad
D_2(y_+)=d+16/d+8/d^2\le d+1,
\]
\[
2a^2-D_1(y_+)^2=d-6-16/d^2>0.
\]
Consequently
\[
H(y_+)+1
=\frac{D_2(y_+)\,[2a^2-D_1(y_+)^2]}{D_1(y_+)^2}
\le\frac{(d+1)(d-6)}{d^2}<1.
\]
There is therefore a \(y\in(1,1+1/d)\) with \(H(y)=0\).

Set
\[
t=\operatorname{arcosh}y>0,\qquad
c=\frac{a}{D_1(y)},\qquad \theta=\arccos c.
\tag{12}
\]
Equation (2) gives \(a<d\) and \(2a>d+1\).
Since \(d<D_1(y)<d+4/d<d+1\), it follows that
\[
\frac12<c<1.
\tag{13}
\]
Take \((d-4)/2\) copies of each root \(e^{i\theta},e^{-i\theta}\), together with the four roots
\[
e^{t+i\theta},\quad e^{t-i\theta},\quad
e^{-t+i\theta},\quad e^{-t-i\theta}.
\tag{14}
\]
This defines a monic real polynomial \(P_{d,a}\) of degree \(d\), constant coefficient one, whose roots are closed under conjugation and inversion.
It is reciprocal.
There are precisely two expanding roots, each of logarithmic modulus \(t\).
The power sums are
\[
s_1=(d-4+4\cosh t)\cos\theta=D_1(y)c=a,
\]
\[
s_2=(d-4+4\cosh(2t))\cos(2\theta)
=D_2(y)(2c^2-1)=1.
\tag{15}
\]
Its total logarithmic measure is therefore
\[
0<m(P_{d,a})=2t
<2\operatorname{arcosh}(1+1/d)
\le2\sqrt{2/d}\longrightarrow0.
\tag{16}
\]
The last inequality uses \(\cosh t\ge1+t^2/2\).

Radially projecting this actual multiset to the circle leaves \(d/2\) copies of each of \(e^{i\theta},e^{-i\theta}\).
Its positive semidefinite moment matrix has first two lags
\[
b_1=dc,\qquad b_2=d(2c^2-1)=d/D_2(y).
\]
The projection errors obey the explicit bounds
\[
0<s_1-b_1=4(y-1)c<4/d,
\]
\[
0<s_2-b_2
=\frac{8(y^2-1)}{D_2(y)}
<16/d^2+8/d^3.
\tag{17}
\]
Thus the small-measure model also supplies its own natural radial positive comparison, rather than only the separate comparison \(T_*\).

The full polynomial \(P_{d,a}\) is not in \(\mathbb Z[t]\).
Indeed, the two unit-circle roots each have multiplicity \(q=(d-4)/2>1\), whereas the four off-circle roots are distinct and simple.
If \(P_{d,a}\) were integral, every rational conjugate of \(z=e^{i\theta}\) would have the same multiplicity \(q\).
The only possible such roots are \(z,\bar z\).
As \(z\) is nonreal, its monic minimal polynomial would then have degree two and equal
\[
X^2-2cX+1.
\]
Integrality of \(P_{d,a}\) would make \(z\) an algebraic integer, so this minimal polynomial would have integer coefficients.
That would require \(2c\in\mathbb Z\), contradicting (13).
This identifies an actual failure of full integrality, not merely a missing verification.

The model has repeated circle roots and does not satisfy the squarefree or irreducible original-input hypotheses.
No all-positive-power degree-preserving endpoint is supplied.
Its first two integer coefficients from (6), reciprocal symmetry and small total measure cannot be substituted for the complete integer polynomial required by the Task.

<a id="integer-near-psd-return-boundary"></a>
## Return to the original question and author-check limits

The decisive negative finding is local: integer moments through \(s_2\), their first two Newton coefficient conditions, all proper principal minors of \(T\), reciprocal real-root geometry and a small radial error do not furnish a dimension-independent positive-semidefinite rounding threshold.
The matrix size is fixed at three; the parameter tending to infinity is the root-multiset degree and diagonal \(d\).
This is not an example satisfying all arithmetic hypotheses of the original Task.

The first unsupported return step would have to use the full integer coefficient list, the remaining Newton compatibility conditions and the actual irreducible conjugate structure to exclude such near-boundary behavior with a cost uniform in \(d\).
The present comparison supplies no independently accessible mechanism for that step.
Calling it uniform moment rigidity would only rename the missing input.
The existing C215 maximal-minor and inertia identities remain available, but do not become a new arithmetic gain through (8).

This test does not justify further parameter scans or general matrix classification.
A substantive reopening would require a concrete cross-order arithmetic constraint and an explanation of what it adds beyond the already retained moment and discriminant identities.
Failure of this finite-order implementation does not rule out a method genuinely using the complete arithmetic structure.

The author directly checked the recurrence invariant and parity, all principal minors and eigenvalues, the fixed-diagonal positive comparison, the elimination factorization, the interval signs in (11), the complete root multiset, both power sums, total measure and nonintegrality argument.
No native mathematical program or numerical experiment was used.
These checks retain their author-development relationship and are not a formal independent review or a new Claim assessment.
