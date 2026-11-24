---
author: Yin
---

# Negative trace forms and the radii of the exterior conjugates

Recorded at 2026-11-24T17:37 UTC.

<a id="bound"></a>
## A lower bound from a negative trace value

Let \(P\) be the monic reciprocal irreducible polynomial of a nontorsion algebraic unit \(\alpha\).
Write \(d=\deg P\), list the positive logarithms of the exterior root moduli with multiplicity as \(t_1,\ldots,t_s\), put \(R=\max_i t_i>0\), and let \(J\) count the \(t_i\) equal to \(R\).
The total logarithmic Mahler measure is \(m(P)=\sum_i t_i\).
The [integral trace form](Yin_C_G0214_v1.md#statement) takes the value
\[
 Q_P(A)=\sum_{P(z)=0}A(z)A(z^{-1})
\]
on an integer polynomial \(A(X)=\sum_j a_jX^j\).
For \(u>0\) define
\[
 g_u(A,c)=\sum_j |a_j|\sinh(u|j-c|),\qquad
 g_u(A)=\inf_{c\in\mathbb R}g_u(A,c).
\]
For an integer width \(B\ge0\), let \(D_P(B)\) be the supremum of
\(\max(0,-Q_P(A))/(2g_R(A)^2)\) over integer polynomials of exponent span at most \(B\) with at least two nonzero coefficients.
The supremum of the empty set is taken to be zero.
Then
\[
 D_P(B)\le\sum_{i=1}^s(t_i/R)^2,\qquad
 J\le\lim_{B\to\infty}D_P(B)\le \frac{\sum_i t_i^2}{R^2}.
\]
In particular \(R D_P(B)\le m(P)\).
Even allowing arbitrarily large width, the optimized lower bound recovers \(m(P)\) exactly if and only if all exterior roots have the same modulus.

Indeed a root on the unit circle contributes \(|A(z)|^2\ge0\).
Pair each exterior root \(z=e^{t+i\theta}\) with \(1/\bar z\).
The real part of the contribution at either member of the pair is the real part of
\[
 \left(\sum_j a_je^{ij\theta}e^{(j-c)t}\right)
 \overline{\left(\sum_j a_je^{ij\theta}e^{-(j-c)t}\right)} .
\]
Its real part is the squared modulus of the sum with \(\cosh((j-c)t)\) in place of the exponentials minus that of the sum with \(\sinh((j-c)t)\).
Consequently it is at least \(-g_t(A,c)^2\).
Convexity on \([0,R]\) gives \(g_t(A,c)\le(t/R)g_R(A,c)\).
Sum over all pairs and take the infimum over \(c\) to obtain the upper bound.

For the other inequality take \(A=1-X^k\).
Its centered cost is \(2\sinh(kR/2)\) by convexity, and \(Q_P(A)=2d-2\sum_z z^k\) by reciprocity.
There are integers \(k\to\infty\) along which all the phases of the roots of modulus \(e^R\), raised to \(k\), tend simultaneously to one.
For instance take increasingly separated pairs from a convergent subsequence of powers of the phase vector in the compact torus and use the differences of their exponents.
Along this sequence \(e^{-kR}\sum_z z^k\to J\), while \(4e^{-kR}\sinh^2(kR/2)\to1\).
This proves the lower bound for the limit.
If some \(0<t_i<R\), then \(\sum_i t_i^2/R<\sum_i t_i\).
If every \(t_i=R\), the two estimates for the limit coincide.

<a id="dilation"></a>
## Exact width cost under power substitution

For an integer \(n\ge1\), take \(P_n(X)=P(X^n)\) and use the same definitions over all its roots, including when \(P_n\) factors.
Its largest exterior logarithm is \(R/n\).
For each \(B\ge0\),
\[
 D_{P_n}(B)=n D_P(\lfloor B/n\rfloor).
\]
Thus the lower bound \((R/n) D_{P_n}(B)\) agrees exactly with the original lower bound at the compressed width.
The least width at which the integral trace form takes a negative value is multiplied by \(n\), even though the total Mahler measure is preserved.
The [irreducible substitutions](../claims/Yin_C_G0345_v403.md#statement) show that this obstruction to a bounded-width test occurs for minimal polynomials of unbounded degree.

To prove the identity, decompose \(A(X)=\sum_{r=0}^{n-1}X^r A_r(X^n)\).
Summing over all \(n\)-th roots of each root of \(P\) cancels every cross term with different residues and gives \(Q_{P_n}(A)=n\sum_r Q_P(A_r)\).
Each nonempty component has span at most \(\lfloor B/n\rfloor\).
For every real \(c\) one has
\[
 g_{R/n}(A,c)=\sum_r g_R(A_r,(c-r)/n)\ge\sum_r g_R(A_r).
\]
Zero components and monomials contribute no negative trace.
Since the sum of squares of the component costs is at most the square of their sum, these identities give \(D_{P_n}(B)\le nD_P(\lfloor B/n\rfloor)\).
Polynomials of the form \(A(X)=F(X^n)\) give the reverse inequality by taking suprema, with no attainment assumption.

This calculation bounds the contribution of every test in terms of the actual radial distribution.
It leaves open how to obtain an absolute positive lower bound on \(R D_P(B)\) for units of growing degree after power descent, or how to recover the contribution of smaller radii by a different estimate.

## Assessment history

### Decision radial-trace-test

| Field | Value |
| --- | --- |
| date | 2026-11-24T17:46 |
| status | proved |
| reason | The archimedean estimate and dilation law have been checked on the full multiset of roots. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#bound) | The optimized negative trace quotient, the equality criterion for full measure and its exact width scaling. |
| argument | [Bound](#bound) | Archimedean inequality and saturation at a single exterior modulus. |
| argument | [Dilation](#dilation) | Residue-class decomposition and equality of the optimized quotients. |
| review | [Independent review](../audits/reviews/Yin_R_G0562_v1042.md#finding) | The fixed statement, argument and qualifications at the specified inputs. |

## Current assessment

[Selected decision](#decision-radial-trace-test)
