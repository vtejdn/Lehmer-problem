---
author: Yin
---

# Mahler-nonincreasing operations: normalized derivatives and radical factors

Date: 2026-11-07.
Human author: Yin.
This bounded discussion retains two actual Mahler-nonincreasing operations and their arithmetic, root and strictness limits.
It complements the [integer finite free variants](Yin_L_G0460_v1.md#scope-and-source-interfaces), rather than treating preservation of real roots as a Mahler estimate.
The coordinating AI agent checked the source statements, coefficient conversions and exact examples as ordinary checks within this exposition.
No independent project review, new Claim assessment or unrestricted Lehmer resolution is asserted.

<a id="sources-and-scope"></a>
## Sources and scope

The normalized derivative and convolution estimate use Pri08, Igor E. Pritsker, Polynomial inequalities, Mahler's measure, and multipliers, in Number Theory and Polynomials (2008), printed pp. 255-276.
The selected [author-hosted original](https://math.okstate.edu/people/igor/multineq.pdf), printed pp. 255-256/PDF pp. 1-2, supplies the coefficient-composition convention, Theorem 1.1 and Corollary 1.2.
The chapter attributes Theorem 1.1 to de Bruijn and Springer and the derivative estimate to Mahler, explaining how the latter follows from the former.
These precise established statements are accepted for use, without a new audit of their original proofs or a priority claim.
The [Pri08 source notes](../audits/literature/Pri08/readme.md) retain the exact reading and source-access scope.

[L460](Yin_L_G0460_v1.md#binomial-coefficient-classes) supplies the already fixed binomial coefficient class and [MSS15-U001](../audits/literature/MSS15/Yin_U001.md#finite-free-definitions) the finite free multiplicative formula.
[Smy08 normalization and Kronecker precision](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) supply multiplicativity, the nonnegative Mahler measure of monic integer factors and the zero-measure boundary.
[C7 Part A](../claims/Yin_C_G0007_v1.md#statement) already fixes M(P(x^k))=M(P), under its nonzero-root hypotheses, as part of a larger exact radical-lift comparison.
The elementary root-product check below also includes zero roots explicitly; no broader resultant statement or new irreducibility theorem is invoked.
The [unrestricted Lehmer contract](../tasks/Yin_T_G0001_v1.md#contract) remains unchanged and unresolved.

<a id="normalized-derivative-descent"></a>
## Normalized differentiation

**Definition (monic normalized derivative).**
For a monic polynomial P of degree d>=1, put
\[
 \mathcal D_dP=\frac1dP'.
\]
It is monic of degree d-1, with the constant polynomial 1 when d=1.
Pri08 Corollary 1.2 states M(P')<=d M(P) for complex polynomials of degree d.
Since M(cF)=|c|M(F), it follows that
\[
 M(\mathcal D_dP)\le M(P),\qquad
 m(\mathcal D_dP)\le m(P).
\tag{1}
\]
For real-rooted P, Rolle's theorem keeps all derivative roots real and inside the interval spanned by the original roots, including multiplicities.
In particular nonnegative real-rootedness is preserved.

For P(x)=sum_(j=0)^d c_j x^j in Z[x], the exact integer-coefficient condition is
\[
 d\mid j c_j\qquad(1\le j\le d).
\tag{2}
\]
It is not automatic: for x^2-3x+1 the normalized derivative is x-3/2.
However, in the binomial coefficient class
\[
 P(x)=\sum_{i=0}^d(-1)^i\binom di A_i x^{d-i},
 \qquad A_i\in\mathbb Z,\quad A_0=1,
\]
one has exactly
\[
 \mathcal D_dP(x)=\sum_{i=0}^{d-1}(-1)^i
                 \binom{d-1}{i}A_i x^{d-1-i}.
\tag{3}
\]
Thus normalized differentiation preserves monic integer coefficients and the corresponding coefficient class at the new degree.
The coefficient identity is ((d-i)/d)binomial(d,i)=binomial(d-1,i).
It may be iterated within that class, but degree decreases at each step.

A strict positive example satisfying the nonnegative-root restriction is
\[
 P(x)=x^2-4x+1,\qquad
 \mathcal D_2P=x-2,
\]
with
\[
 M(P)=2+\sqrt3>2=M(\mathcal D_2P)>1.
\tag{4}
\]
The input is an irreducible unit polynomial and the output is monic integer and real-rooted, but the output is no longer a unit polynomial.
Positivity of m is also not preserved in general: x^2-2x-1 has positive Mahler measure and normalized derivative x-1 has measure one.
Repeated differentiation eventually reaches 1, so this finite-degree operation does not itself produce an infinite positive-to-zero Mahler sequence.

<a id="finite-free-contractive-kernels"></a>
## Finite free multiplication with a measure-one kernel

Pri08 Theorem 1.1 says that if
\[
 \Lambda(z)=\sum_{j=0}^d\binom dj\lambda_j z^j,
 \qquad P(z)=\sum_{j=0}^d c_j z^j,
\]
then the Szego composition Lambda P=sum_j lambda_j c_j z^j satisfies
\[
 M(\Lambda P)\le M(\Lambda)M(P).
\]
With the signed convention for MSS15's multiplicative convolution, take Lambda(z)=(-1)^d q(-z).
Its coefficient multiplier is exactly the multiplier defining p boxtimes_d q, and M(Lambda)=M(q).
Therefore
\[
 M(p\boxtimes_dq)\le M(p)M(q).
\tag{5}
\]
In particular any kernel with M(q)=1 makes this operation Mahler-nonincreasing.
The coefficient denominators still require their own arithmetic check.
If p is in the binomial class and q is monic integer of degree d, the output coefficients are integers because each binomial denominator cancels the corresponding factor in p.
Real-rootedness remains subject to the convolution's actual root hypotheses.

For 0<=r<=d, the kernel
\[
 q_r(x)=x^{d-r}(x-1)^r
\]
is monic integer with nonnegative real roots and M(q_r)=1.
These are all monic integer, nonnegative real-rooted kernels of measure one: Kronecker's theorem makes every nonzero root a root of unity, and a positive real root of unity is 1.
If the kernel is also a unit polynomial, it must be q_d=(x-1)^d and the resulting convolution is the identity.
The exact identity is
\[
 p\boxtimes_dq_r
 =x^{d-r}\frac{r!}{d!}p^{(d-r)}(x).
\tag{6}
\]
It follows by comparing the coefficient ratio binomial(r,i)/binomial(d,i), with zero coefficients for i>r.
For r=d-1 this is x times the normalized derivative, so it has the same Mahler measure as that derivative.
For r=0 the output is x^d and has measure one.
Thus measure-one kernels give genuine contractions, but they can also eliminate all positive Mahler measure.

<a id="radical-substitution-and-factor-selection"></a>
## Radical substitution followed by factor selection

For a monic integer P and k>=2, put
\[
 F(x)=P(x^k)\in\mathbb Z[x].
\]
For every nonzero original root alpha, its k roots in F have modulus |alpha|^(1/k), and their combined Mahler contribution is max(1,|alpha|).
A zero original root yields k zero roots, each contributing one.
Hence
\[
 M(F)=M(P),\qquad m(F)=m(P).
\tag{7}
\]
Factor F into monic irreducible integer factors, with all multiplicities retained:
\[
 F=\prod_{j=1}^sQ_j.
\]
Each m(Q_j)>=0, and
\[
 \sum_{j=1}^s m(Q_j)=m(P).
\tag{8}
\]
Thus selecting any factor makes total logarithmic Mahler measure nonincreasing.
If P(0)=1 or -1, every Q_j also has constant coefficient 1 or -1, so this operation preserves the unit condition.
If P is irreducible and noncyclotomic with P(0)!=0, every Q_j is noncyclotomic and has no zero root: a root of unity beta of Q_j would make beta^k a root of unity of P.
In this case all m(Q_j)>0, and any genuine factorization of F into at least two factors makes every selected m(Q_j) strictly smaller than m(P).
If F remains irreducible, the operation gives no Mahler decrease.

The exact irreducible-unit example is
\[
 P(x)=x^2-3x+1,\qquad
 P(x^2)=(x^2-x-1)(x^2+x-1).
\tag{9}
\]
Writing phi=(1+sqrt(5))/2, one has
\[
 M(P)=\phi^2,\qquad
 M(x^2-x-1)=M(x^2+x-1)=\phi.
\tag{10}
\]
Thus choosing either factor strictly decreases positive Mahler measure while preserving monicity, integer coefficients and the algebraic-unit condition.
All polynomials in this example are real-rooted.
More generally, if P has only nonnegative real roots and k=2, then every root of P(x^2) is real and every factor remains real-rooted, though a factor need not keep nonnegative roots.
Without factor selection, repeated radical substitutions keep total M fixed even as root moduli approach one, as already emphasized in C7's fixed-measure radical controls.

The polynomial factorization in (9) and the normalized derivative coefficient identity were checked by exact integer and Fraction arithmetic.
The examples have explicit roots, so their Mahler values require no numerical approximation or separate computation record.

<a id="strictness-and-lehmer-boundary"></a>
## Strictness and the remaining Lehmer boundary

Both operations supply actual strict-decrease examples.
Neither supplies a universally repeatable strict decrease while preserving positive logarithmic Mahler measure.
Normalized derivatives can lose integrality outside their coefficient domain, lose the unit condition and terminate at measure one.
Radical substitution preserves total measure until a useful factorization occurs, and no such factorization is guaranteed at the next chosen exponent.
Strict decreases alone do not imply that the positive values tend to zero; they can stop or remain above a positive limit.
An infinite iteration with 0<m(P_(n+1))<=theta m(P_n) for a fixed theta<1 would establish a zero-gap family, but no such iteration is constructed here.
The existence of these operations therefore does not settle the unrestricted Lehmer question.
