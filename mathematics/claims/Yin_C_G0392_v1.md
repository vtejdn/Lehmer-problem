---
author: Yin
---

# Primitive prediction cofactors, actual cokernel order and fixed-input normalizer divergence

This retains the complete necessary mathematical argument from [complete original L363](../ledger/Yin_L_G0363_v1.md#primitive-prediction-normalizer).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be any nonzero integer polynomial after removal of a Laurent monomial, B=|P|^2 on the unit circle with Haar probability, and G_n=(integral B z^i conjugate(z^j)) for 0<=i,j<n, D_n=det G_n with D_0=1.
For each integer n>=0, q_n is the unique complex polynomial minimizer of degree<=n with q_n(0)=1, and r_n=||Pq_n||_2^2.
Every G_n is positive definite, every nonempty D_n is a positive integer, q_n has rational real coefficients and no root in the closed unit disk, and r_n=D_(n+1)/D_n.
For n>=1 put v_n=adj(G_(n+1))e_0 and g_n=gcd of all its entries, including v_(n,0)=D_n>0.
Then Q_n=v_n/g_n as a coefficient polynomial is primitive, k_n=Q_n(0)=D_n/g_n is the least positive integer clearing all coefficients of q_n, and k_n equals the order of the actual boundary class [b] in Z^n/G_n Z^n, where G_(n+1) is partitioned into its constant row and trailing G_n block.
It divides the largest positive Smith factor and D_n; the exact integer energy is k_n^2D_(n+1)/D_n=D_nD_(n+1)/g_n^2, and D_n/gcd(D_n,D_(n+1)) divides k_n^2, only as a necessary condition.
For n=0 use q_0=Q_0=1 and k_0=1.
For every fixed P, r_n decreases to M(P)^2; if P is nonmonomial, every finite value is strictly larger and k_n tends to infinity without a uniform rate or monotonicity assertion.
For P=1-t^s, every integer s>=1 and n=sL+r with L>=0 and 0<=r<s, the complete residue-chain optimizer and formulas(9)--(11) hold: D_n=(L+2)^r(L+1)^(s-r), r_n=(L+2)/(L+1), k_n=L+1, and the complete cofactor gcd for n>=1 and primitive energy have the displayed exact values.
The moving-window n=s gives D_n=2^s and k_n=2; this cyclotomic control does not refute a theorem specific to irreducible noncyclotomic inputs.
All complete Sections1--5/(1)--(11), zero-cofactor/empty-window/content/circle-zero cases, exact nonattainment and fixed-input approximation limits, original contributions and non-novelty boundaries are retained below.
Residuals are upper estimates for M(P)^2; no uniform normalizer rate, near-one gap, new source audit, experiment or research execution is asserted.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:27 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete proof](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Complete fixed-input multiplier theorem](Yin_C_G0380_v3.md#argument) | Only the complete original Jensen lower bound, strict nonattainment for nonmonomials and rational zero-free approximation including circle zeros, with no uniform approximation rate. |
| dependency | [Original finite Gram interface](../ledger/Yin_L_G0004_v1.md#degree-window-tests) | Only the original full Toeplitz/autocorrelation and finite residual convention; no original program or numerical scan is rerun. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:31 |
| status | proved |
| reason | Adopt the entire retained original argument after actual whole SELF checking, all-domain statement verification and full original review/source/contribution comparison. Original exact fixed inputs, dates, useful limits and true historical relationships are preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated domain, all numbered equations and every explicit finite-family, source, sign, boundary and expense limit. |
| argument | [Complete selected argument](#argument) | Complete necessary original mathematical derivations and exact fixed native certificates, with routine allocation and freeze chronology left at its existing responsible home. |
| dependency | [Exact accepted input](Yin_C_G0380_v3.md#argument) | Only the complete original Jensen lower bound, strict nonattainment for nonmonomials and rational zero-free approximation including circle zeros, with no uniform approximation rate. |
| dependency | [Exact accepted input](../ledger/Yin_L_G0004_v1.md#degree-window-tests) | Only the original full Toeplitz/autocorrelation and finite residual convention; no original program or numerical scan is rerun. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0596_v1.md#primitive-normalizer-current-whole-finding) | Entire exact current statement and all mathematical sections, including every small/empty/circle-zero boundary, all full coefficients, original scope/source/finite limits and complete index/direction/shift costs. |

## Complete retained argument

<a id="argument"></a>

The original dated proofs and input descriptions below refer to the 2026-10-11 mathematics.
Their necessary fixed evidence remains at its exact original home and supplies no Task/E resumption.

<a id="primitive-prediction-normalizer"></a>
## 1. The exact optimizer and its primitive integer normalizer

Let P be a nonzero polynomial in Z[t], let B=|P|^2 on the circle, and use Haar probability.
Remove a Laurent monomial if needed.
Write
\[
\langle f,g\rangle_B=\int_{\mathbb T}Bf\overline g,\qquad
G_n=(\langle z^i,z^j\rangle_B)_{0\le i,j<n},\quad D_n=\det G_n,\quad D_0=1.
\]
All entries are integers and real.
Each G_n is positive definite: B is positive almost everywhere and a nonzero polynomial cannot vanish almost everywhere.
Thus D_n is a positive integer.

For n>=0, let q_n be the unique minimizer of ||Pq||_2^2 over complex polynomials of degree<=n with q(0)=1.
The normal equations have integer real coefficients, so q_n has rational real coefficients.
Put r_n=||Pq_n||_2^2.
For n>=1 let
\[
v_n=\operatorname{adj}(G_{n+1})e_0,\qquad
g_n=\gcd(v_{n,0},\ldots,v_{n,n})>0.
\]
The zeroth entry v_(n,0) is D_n, because the complementary Gram section is a shift of G_n.
The normal equations and Schur complement give
\[
q_n(z)=\sum_{j=0}^n\frac{v_{n,j}}{D_n}z^j,\qquad
r_n=\frac{D_{n+1}}{D_n}.                                      \tag{1}
\]
Consequently the primitive polynomial and its positive constant coefficient are
\[
Q_n=\frac1{g_n}\sum_jv_{n,j}z^j\in\mathbb Z[z],\qquad
k_n=Q_n(0)=\frac{D_n}{g_n}.                                   \tag{2}
\]
Here primitive means the complete coefficient vector has gcd1.
In particular k_n is the **least** positive integer k for which kq_n has integer coefficients.
If a smaller k worked, each reduced rational coefficient denominator would divide it; their least common multiple is D_n/g_n.
This argument covers zeros among the cofactors.
For n=0 use q_0=1,Q_0=1,k_0=1.

### The closed-disk root condition is automatic

For any root zeta of q_n, write q_n=(z-zeta)a with deg a<=n-1.
The normal equations say q_n is orthogonal to z,z^2,...,z^n, hence to za.
With the inner product linear in its first entry,
\[
0=\langle za-\zeta a,za\rangle_B
=\|a\|_B^2-\zeta\langle a,za\rangle_B.
\]
The denominator cannot vanish, and strict Cauchy--Schwarz gives
\[
|\langle a,za\rangle_B|<\|a\|_B^2.
\]
Equality would require za to be a constant multiple of a almost everywhere on the circle, impossible for a nonzero polynomial and B positive almost everywhere.
Thus |zeta|>1.
This proof permits unit-circle zeros of P because they have Haar measure zero.
It does not assume B is bounded below.
Therefore Q_n lies in the exact zero-free integer class O_(k_n) of [L359](Yin_C_G0380_v3.md#integer-multiplier-variational-formula).

<a id="cokernel-denominator-identity"></a>
## 2. A finite abelian group element measures the arithmetic cost

For n>=1, partition G_(n+1) with the constant coefficient first:
\[
G_{n+1}=
\begin{pmatrix}a&b^{\mathsf T}\\ b&T_n\end{pmatrix},\qquad
T_n=G_n
\]
as matrices after the natural shift identification; a=||P||_2^2 and b is the integer constant/positive-shift correlation vector.
The remaining coefficient vector is -T_n^-1 b.

The quotient A_n=Z^n/T_n Z^n is a finite abelian group of cardinality D_n.
Formula(2) has the equivalent intrinsic description
\[
k_n=\operatorname{ord}_{A_n}([b]).                            \tag{3}
\]
Indeed k[b]=0 precisely when kT_n^-1 b is integral, which is exactly the denominator-clearing condition for q_n.
The zero class has order1.
If s_1|...|s_n are the positive Smith invariant factors of T_n, then
\[
k_n\mid s_n,\qquad k_n\mid D_n.                               \tag{4}
\]
Thus the raw determinant cardinality is a generally loose bound for the particular element order that matters.

The primitive energy is the exact integer
\[
\|PQ_n\|_2^2
=k_n^2\frac{D_{n+1}}{D_n}
=\frac{D_nD_{n+1}}{g_n^2}.                                   \tag{5}
\]
In particular
\[
\frac{D_n}{\gcd(D_n,D_{n+1})}\mid k_n^2.                      \tag{6}
\]
This is a necessary divisibility condition obtained by reducing the fraction in(5), not a sufficient characterization of k_n.
The full cofactor gcd or the actual cokernel element is needed for the equality(2)--(3).

These are exact arithmetic consequences of the finite prediction problem, not a conversion of its residual upper bound into a Mahler lower bound.
Cokernel size, exponent and the order of [b] are three distinct quantities.

<a id="normalizer-divergence"></a>
## 3. Every nonmonomial input forces growing optimizer normalizers

The affine trial spaces increase, so r_n decreases weakly.
Every q_n is zero-free and L359's lower inequality gives r_n>=M(P)^2.
Conversely its fixed-input rational zero-free approximation supplies some finite-degree trial with energy as close to M(P)^2 as desired.
Minimization over that trial degree and all larger degrees proves
\[
r_n\downarrow M(P)^2.                                       \tag{7}
\]
This proof reuses the full L359 circle-zero approximation, rather than assuming a uniform quantitative Toeplitz limit.
For nonmonomial P, its nonattainment argument gives r_n>M(P)^2 at every finite n.

For every such fixed P,
\[
k_n\longrightarrow\infty.                                   \tag{8}
\]
To prove this, fix an integer K>=1.
If k_n<=K, then r_n is an integer energy divided by k_n^2 and r_n<=r_0.
There are only finitely many such rational values: their numerators are bounded by K^2 r_0.
All of these attained values are strictly larger than M(P)^2.
Thus they cannot occur at arbitrarily large n along the convergence(7).
This proves(8), without assuming M(P)^2 rational, a strictly decreasing residual sequence, or monotone normalizers.

This is a fixed-input necessary denominator divergence.
It gives no uniform rate in n or degree, and applies also to cyclotomic P.
In particular it cannot separate zero measure from positive measure.
The weaker integer lower floor r_n>=1+1/k_n^2 from L359 is consistent with it and has the same estimate-direction boundary.

<a id="cyclotomic-cofactor-cancellation"></a>
## 4. Exact cyclotomic cancellation of the raw determinant cost

For P=1-t^s, s a positive integer, write n=sL+r with integers L>=0 and 0<=r<s.
Residue classes split G_n into tridiagonal blocks with diagonal2 and off-diagonal-1.
A block of length j has determinant j+1, by the recurrence E_j=2E_(j-1)-E_(j-2), E_0=1,E_1=2.
There are r blocks of length L+1 and s-r blocks of length L.
Hence
\[
D_n=(L+2)^r(L+1)^{s-r},\qquad
\frac{D_{n+1}}{D_n}=\frac{L+2}{L+1}.                          \tag{9}
\]

The optimizer has no coefficients in nonzero residue chains because those chains add a positive quadratic energy independently.
On the chain 0,s,...,sL, real differences minimize their squared sum at equal differences, as in L359's exact integer control before rounding.
Thus
\[
q_n(t)=1+\frac{L}{L+1}t^s+\frac{L-1}{L+1}t^{2s}
+\cdots+\frac1{L+1}t^{sL},\qquad k_n=L+1.                    \tag{10}
\]
For L=0 the displayed tail is empty and k_n=1.
For L>=1 the final coefficient 1/(L+1) proves minimality.
Consequently
\[
g_n=\frac{D_n}{L+1},\qquad
\|PQ_n\|_2^2=(L+1)(L+2).                                    \tag{11}
\]
The cofactor gcd can therefore cancel nearly the whole determinant.
For instance at n=s, D_n=2^s while k_n=2 and g_n=2^(s-1).
This is an exact family with no numerical scan, and s is unrestricted.
A raw determinant used as the supposed unavoidable denominator would assign an exponential cost where the actual normalizer is constant at this moving window.

The control is cyclotomic and reducible when s>1.
It does not refute a theorem imposing irreducible noncyclotomic input.
It does exclude using Toeplitz integrality alone, without a theorem about the actual cofactor gcd/cokernel element, as a uniform normalizer-cost mechanism.

## 5. Outcome and continuation

The useful coupling is exact: the optimal analytic weight has a primitive integer normalizer equal to one particular order in a finite integer Gram cokernel.
Both residual energy and determinant cost admit large arithmetic cancellation.
A future noncyclotomic test should study that actual element or cofactor gcd, retaining degree, full polynomial and approximation error, rather than optimize a raw determinant bound or treat every finite residual as a lower certificate.

The initial rationality/stability mechanism was supplied by the haar_integer_research scout; root derived the primitive-cofactor and cokernel-order identities, complete denominator-divergence proof and exact all-s residue-chain cancellation.
The direct proof above rechecks the scout and keeps that contribution explicit.
Classical finite prediction and Smith form are not claimed novel; the earlier L4/L359 interfaces are reused at their actual stated scope.
No new source theorem or historical priority claim is needed.
