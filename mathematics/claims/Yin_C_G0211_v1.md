---
author: Yin
---

# A real reciprocal short-window family with fixed Gram surplus and vanishing measure

The complete original exact boundary argument is retained from [L13](../ledger/Yin_L_G0013_v1.md), dated 2026-10-06.
It is a counterexample to a root-geometric sufficiency inference in the stated real-coefficient domain, not an integer-polynomial counterexample or a new research run.

## Statement

For every integer k>=1, let r=4k, c=log16, tau=exp(c/r)=2^(1/k), d=r+2 and

    p_r(t)=[t^2-(tau+tau^(-1))t+1](t^r+1).

This is monic, real, reciprocal and squarefree, with exactly the positive real off-circle pair tau,tau^(-1) and r nonreal unit-circle roots.
It is nonintegral since its coefficient -(tau+tau^(-1)) has magnitude strictly between 2 and 3, and it is reducible over R.
For the actual companion power-remainder matrix V_N in degree d, put W_N=V_NV_N^T, G_N=det W_N and R_N=|disc p_r|G_N/N^d for every N>=d.
Then

    m(p_r)=c/r ->0,
    R_(2r)=(1+cosh c)^2/4 * [(sinh c/[r sinh(c/r)])^2-1]>120,
    R_(2d)>15/2>1

for all k>=1.
Thus fixed positive short-window Gram surplus, even with a single real reciprocal off-circle pair, does not imply a uniform positive polynomial measure in this real domain.
This does not refute such a consequence with additional integral-irreducible arithmetic hypotheses.
The algebraic number tau instead has actual integral minimal polynomial t^k-2 and multiplicative algebraic Mahler measure 2; its full conjugates cannot be replaced by this real quadratic factor.
No integral inverse-trace claim, numerical enumeration or unverified asymptotic determinant is used.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:20 |
| status | open |
| reason | Register the exact retained statement and complete argument; actual current statement-and-proof checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The entire exact r=4k family, actual companion and both finite windows, uniform numerical surplus, vanishing real-polynomial measure and explicit exclusion from the integral Lehmer domain. |
| argument | [Argument](#argument) | Full original root-row projection, Schur-complement constant, both monotonicity arguments, coefficient/minimal-polynomial and degree-penalty boundaries. |
| dependency | [Root-Gram identity](Yin_C_G0209_v1.md#statement) | Only the actual real companion, root-evaluation equality and Hadamard normalization; no integer-lattice assertion is transferred to this real-coefficient family. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:26 |
| status | proved |
| reason | Adopt the actual current statement and complete retained argument with its resolved exact inputs and sufficient constructor self-review. Original targeted findings retain their own historical scopes; no new research execution, independent certification or unrestricted gap follows. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Whole r=4k real family, actual companion, exact two-window constants and monotonicity, vanishing polynomial versus full algebraic measure and integral-domain exclusions. |
| argument | [Argument](#argument) | Complete physically retained proof and all required local deductions, with the exact domains, source depths and limitations in the Statement. |
| dependency | [Root-Gram identity](Yin_C_G0209_v1.md#statement) | Only the actual real companion, root-evaluation equality and Hadamard normalization; no integer-lattice assertion is transferred to this real-coefficient family. |
| review | [Actual complete current finding](../audits/reviews/Yin_R_G0502_v1.md#real-family-current-finding) | Whole r=4k real family, actual companion, exact two-window constants and monotonicity, vanishing polynomial versus full algebraic measure and integral-domain exclusions. |

## Argument

For each integer k>=1, set r=4k, c=log(16), tau=exp(c/r)=2^(1/k), and

\[
p_r(t)=\bigl(t^2-(\tau+\tau^{-1})t+1\bigr)(t^r+1),
\qquad d=r+2.
\]

This is a monic real reciprocal squarefree polynomial.
It has two positive real reciprocal roots tau,tau^(-1), with tau>1; its other r roots are on the unit circle and are nonreal because r is even.
Its logarithmic polynomial Mahler measure is

\[
m(p_r)=\log\tau=c/r\longrightarrow0.
\tag{1}
\]

But p_r is nonintegral: the coefficient of t^(r+1) is -(tau+tau^(-1)), and 2<tau+tau^(-1)<=5/2.
It is also reducible over the real coefficient field.
In particular (1) is not the algebraic Mahler measure of tau: the latter has Eisenstein minimal polynomial t^k-2 and M(tau)=2.
Retaining every conjugate and the actual integral minimal polynomial removes the apparent small-measure family, as required by the Task.

Use the actual companion orbit, not a substituted matrix.
With V_N, W_N=V_NV_N^T and G_N=det W_N defined by the C209 power-remainder construction, set

\[
R_N(p_r)=|\operatorname{disc}p_r|G_N/N^d.
\]

All these objects exist for the real squarefree polynomial.
The [complete C209 root-Gram argument](Yin_C_G0209_v1.md#argument) gives

\[
|\operatorname{disc}p_r|G_N=\det(E_NE_N^*),
\]

where E_N has the root-evaluation rows (alpha^j)_(0<=j<N).
Thus the determinant can be calculated by orthogonal projection of genuine root-evaluation rows.

<a id="fixed-surplus-vanishing-measure"></a>
### Exact determinant at the first window

First take N_0=2r.
If zeta ranges over the roots of t^r+1, the r evaluation rows are mutually orthogonal, each with squared norm 2r.
Their span in C^(2r) is exactly

\[
\{(z,-z):z\in\mathbb C^r\},
\]

because zeta^r=-1 and the first r coordinates form an invertible Vandermonde matrix.
Its orthogonal complement is {(z,z)}.
The rows for tau and tau^(-1) project onto that complement as

\[
\frac{1+e^c}{2}(a,a),\quad a_j=\tau^j;
\qquad
\frac{1+e^{-c}}{2}(b,b),\quad b_j=\tau^{-j},
\quad 0\le j<r.
\]

The Schur-complement determinant formula for a Gram matrix now gives

\[
|\operatorname{disc}p_r|G_{2r}
=(2r)^r(1+\cosh c)^2
\left(\left(\frac{\sinh c}{\sinh(c/r)}\right)^2-r^2\right).
\]

Indeed a^T b=r and ||a||^2||b||^2=(sinh c/sinh(c/r))^2.
The two projection factors, including their duplicated-coordinate norms, multiply to (1+cosh c)^2 in the two-by-two determinant.
Since d=r+2, division by (2r)^d yields the exact formula

\[
R_{2r}(p_r)=\frac{(1+\cosh c)^2}{4}
\left[\left(\frac{\sinh c}{r\sinh(c/r)}\right)^2-1\right].
\tag{2}
\]

For fixed c>0, r sinh(c/r) decreases as r increases: its derivative has the sign of sinh(x)-x cosh(x)<0, x=c/r.
Since r>=4 and c=log16,

\[
r\sinh(c/r)\le4\sinh(\log2)=3,\quad
\sinh c=255/32,\quad 1+\cosh c=289/32.
\]

Consequently the first factor in (2) is 83521/4096>20 and the bracket is at least (85/32)^2-1=6201/1024>6.
Therefore

\[
R_{2r}(p_r)>120\qquad(r=4k,\ k\ge1).
\tag{3}
\]

### Transfer to the required N=2d window

For N>=d, W_N is positive definite and W_(N+1)=W_N+v_Nv_N^T.
Thus G_(N+1)>=G_N; for example the determinant lemma gives the multiplier 1+v_N^T W_N^(-1)v_N>=1.
This monotonicity is asserted for G, not for R.

Since 2d=2r+4,

\[
R_{2d}(p_r)\ge R_{2r}(p_r)
\left(\frac{2r}{2r+4}\right)^{r+2}.
\]

The function (r/(r+2))^(r+2) is increasing for r>0.
Differentiating its logarithm gives 2/r-log(1+2/r)>0.
Hence for r>=4 it is at least (2/3)^6=64/729>1/16.
Equation (3) proves

\[
R_{2d}(p_r)>15/2>1\quad\text{for every }k\ge1,
\qquad m(p_r)\longrightarrow0.
\tag{4}
\]

### Exact consequence for the strategy

The real monic squarefree reciprocal class, even restricted to one positive real off-circle pair, admits the very same N=2d positivity condition with a uniform numerical surplus and vanishing polynomial measure.
Positivity with a fixed surplus is therefore not enough for a uniform Mahler gap in this continuous root-geometric domain.
A conclusion for integer irreducible polynomials would have to use their additional arithmetic restrictions; the family above does not refute such a conclusion.
Its inverse-trace entries are not asserted integral.

Equation (4) also does not contradict the valid lower certificate m>=log(R_N)/(2(N-1)): its denominator grows with r.
No numerical enumeration, additional literature input, or unverified asymptotic determinant is used.
All estimates are exact displayed algebra.
The root-variable parameter tau itself has fixed integral Mahler measure 2, as noted above.
