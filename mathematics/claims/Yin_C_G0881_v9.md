---
author: Yin
---

# Whole Mahler bounds from variable neutral reference prefixes

<a id="statement"></a>
## Statement and original grid

Let \(p=2n+1\), \(n\ge2\), and define
\[
 E_{-1}=0,\quad E_0=1,\quad E_1=t,\quad E_{j+1}=tE_j-E_{j-1},
 \qquad B_j=E_j+E_{j-1},\qquad b_j=2\cos(2\pi j/p).
\]
Take
\[
 Q=(t-a)B_n+C,\qquad a\in\mathbb R,\qquad
 C\in\mathbb R[t],\quad\deg C<n,\qquad
 P(z)=z^{n+1}Q(z+z^{-1}).
\]
For some integer \(1\le\kappa<n\), assume the strict residue signs and endpoint
\[
 r_j=\frac{Q(b_j)}{B_n'(b_j)}>0\ (j\le n-\kappa),\qquad
 r_j<0\ (j>n-\kappa),\qquad
 \frac{Q(-2)}{B_n(-2)}<0.
 \tag{1}
\]
Let \(U,V\) be nonzero complex polynomials whose roots all lie on the unit circle, with \(U(0)/V(0)=1\).
Constant polynomials are permitted.
Suppose
\[
 2\le L\le n+1<p,\qquad
 P-U/V=O(z^{L+1})\quad(z\to0),\qquad
 H=\deg U+\deg V.
 \tag{2}
\]
All numerator and denominator multiplicities count in \(H\), even when factors cancel.
For \(q=\lfloor L/2\rfloor\), the complete multiplicative Mahler measure satisfies
\[
 \boxed{\quad 1\le M(P)\le(8q+H+3)^{2/q}.\quad}
 \tag{3}
\]
The polynomial is monic reciprocal of degree \(2n+2\); its complete measure includes every root with multiplicity.
The upper bound requires neither integer coefficients nor a prior upper bound on \(M(P)\), and allows both real and nonreal residual quadratic roots.

For a sequence of such inputs, \(L\to\infty\) and \(\log(L+H)=o(L)\) imply \(m(P)=\log M(P)\to0\).
Strict positivity is not automatic under the general hypotheses.

There is a sufficient integer subcase with automatic positivity.
If \(a=0\), \(\kappa=1\), and
\[
 C=B_{n-1}h\bmod B_n,\qquad
 h=\sum_{i=0}^{n-1}a_iE_i\in\mathbb Z[t],\qquad a_0=2,
 \tag{4}
\]
then the [fixed endpoint theorem](Yin_C_G0881_v8.md#statement) gives \(M(P)>1\) and exactly one conjugate pair of nonreal exterior roots.
Consequently a sequence satisfying (1), (2), (4) and the growth condition above would give positive total logarithmic measures tending to zero.
Existence of that sequence, or of any new integer input satisfying these simultaneous conditions, is not asserted.

<a id="argument"></a>
## Inputs, changed hypothesis and proof

The main researcher and the strategic-discovery contributor developed this extension.
The [v3 interval argument](Yin_C_G0881_v3.md#original-domain) and [paired-variation identity](Yin_C_G0881_v3.md#paired-variation) are reused below at their actual root-count and matching scopes.
The changed hypothesis replaces v3's five fixed rational profiles by (2).
Only the Newton-sum estimate changes in the upper-bound argument; v3's exact coefficient profiles and its constant eight are not transferred to a new reference.
The positivity assertion uses the unchanged [v8 statement](Yin_C_G0881_v8.md#statement) only under (4) and \(\kappa=1\).
No new source theorem is assumed.

<a id="interval-root-accounting"></a>
## All original roots and disjoint matching

Partial fractions give
\[
 \frac{Q(t)}{B_n(t)}=t-a+\sum_{j=1}^{n}\frac{r_j}{t-b_j}.
\]
Between each pair of consecutive same-sign poles the opposite infinite limits force a trace root.
There are \(n-2\) such intervals.
Since \(r_n<0\), the ratio tends to positive infinity at \(b_n\) from the left; (1) supplies a further root in \((-2,b_n)\).
Choose one root in each of these \(n-1\) disjoint open intervals and remove exactly one copy of each from \(Q\).
The remaining factor is real monic quadratic, with roots \(v_1,v_2\) counted with multiplicity.
Possible repetitions among the remaining roots or with chosen roots are retained.

Choose a root \(\lambda_i\) of \(z^2-v_i z+1\) with modulus \(\rho_i\ge1\).
The chosen real interval roots lift to unit-circle pairs, so
\[
 M(P)=\rho_1\rho_2.
 \tag{5}
\]
Match each selected trace root to the right endpoint pole of its interval, including the root in \((-2,b_n)\).
These poles are distinct; precisely \(b_{n-\kappa}\) remains unmatched.
The matching intervals have disjoint interiors, so for every real polynomial \(f\),
\[
 |f(v_1)+f(v_2)|
 \le |\mathcal D(f)|+|f(b_{n-\kappa})|
       +\operatorname{Var}_{[-2,2]}(f),\qquad
 \mathcal D(f)=\sum_{Q(u)=0}f(u)-\sum_{j=1}^{n}f(b_j).
 \tag{6}
\]
The sum over \(Q\) retains all multiplicities.
This follows by subtracting every matched pair and bounding their changes by the total variation over the disjoint intervals.
There is no factor of \(n\) in this variation cost.

<a id="neutral-newton-sums"></a>
## Newton sums of a variable neutral reference

Write \(s_j(P)\) for the sum of all \(j\)-th root powers of \(P\).
Since \(P\) is reciprocal with constant coefficient one,
\[
 s_j(P)=-j[z^j]\log P(z).
\]
In general the formal logarithm on the right sums inverse-root powers; reciprocity makes those the same multiset here.
The normalized rational reference has the factorization
\[
 \frac{U(z)}{V(z)}
 =\frac{\prod_{\nu=1}^{\deg U}(1-z/u_\nu)}
        {\prod_{\nu=1}^{\deg V}(1-z/v_\nu)},
 \qquad |u_\nu|=|v_\nu|=1.
\]
Prefix agreement through index \(L\) implies equality of the formal logarithm coefficients through that index.
Therefore
\[
 s_j(P)=\sum_\nu u_\nu^{-j}-\sum_\nu v_\nu^{-j},
 \qquad |s_j(P)|\le H,\qquad 1\le j\le L.
 \tag{7}
\]

Let \(T_j(z+z^{-1})=z^j+z^{-j}\) be the trace Chebyshev polynomial.
The lift
\[
 z^nB_n(z+z^{-1})=\frac{1-z^p}{1-z}
\]
has all nontrivial \(p\)-th roots of unity, whose power sum equals \(-1\) for \(1\le j<p\), including composite \(p\).
Thus (2) and (7) give
\[
 |\mathcal D(T_j)|=|s_j(P)+1|\le H+1.
\]
On \([-2,2]\), one has \(|T_j|\le2\) and
\[
 \operatorname{Var}_{[-2,2]}(T_j)
 =\int_0^\pi 2j|\sin(j\theta)|\,d\theta=4j.
\]
Applying (6) yields
\[
 |T_j(v_1)+T_j(v_2)|\le4j+H+3,\qquad 1\le j\le L.
 \tag{8}
\]

<a id="real-and-nonreal"></a>
## Complete bound in both quadratic cases

Put \(q=\lfloor L/2\rfloor\ge1\).
If \(v_1,v_2\) are nonreal, they are conjugate and their exterior lifts are \(\rho e^{i\theta},\rho e^{-i\theta}\) for \(\rho>1\).
Hence
\[
 T_j(v_1)+T_j(v_2)=2(\rho^j+\rho^{-j})\cos(j\theta),
 \qquad M(P)=\rho^2.
\]
At least one of \(|\cos(q\theta)|\) and \(|\cos(2q\theta)|\) is at least \(1/2\), since otherwise the double-angle identity is contradicted.
For that \(j\in\{q,2q\}\), (8) gives
\[
 \rho^j+\rho^{-j}\le8q+H+3.
\]
As \(j\ge q\), this implies (3).

If both residual roots are real, put \(\rho=\max(\rho_1,\rho_2)\).
The case \(\rho=1\) has measure one.
Otherwise an exterior real trace contributes at least \(\rho^{2q}\) at the even frequency \(2q\); the other real trace contributes at least \(-2\) if it is in \([-2,2]\) and at least \(2\) otherwise.
Thus
\[
 \rho^{2q}\le8q+H+5,\qquad
 M(P)\le\rho^2\le(8q+H+5)^{1/q}
                     \le(8q+H+3)^{2/q}.
\]
The last step uses \(8q+H+5\le(8q+H+3)^2\).
This also covers coincident real roots and retained multiplicities.
Equation (5) gives the lower bound \(M(P)\ge1\).

<a id="growing-reference-consequence"></a>
## Positivity and growing references

The logarithm of (3) is at most \(2\log(8q+H+3)/q\).
Since \(q\) is comparable to \(L\), the condition \(\log(L+H)=o(L)\) makes this tend to zero.
In particular polynomial growth of \(H\) in \(L\), or more generally \(\log H=o(L)\) when \(H\ge1\), is permitted.
This analytic flexibility does not supply the required signs.

Under (4), the integer lift and its first residue sum are exactly those of v8, and all its other sign and endpoint hypotheses are (1) with \(\kappa=1\).
That fixed result gives strict positivity and its exact nonreal exterior pair without using any old fixed prefix.
Applying (3) then proves the stated conditional positive-to-zero consequence.
Neither the reference's neutrality nor its integer coefficients alone proves that consequence for a constructed polynomial.

## Assessment history

### Decision variable-neutral-reference-bound

| Field | Value |
| --- | --- |
| date | 2026-11-10T11:43 |
| status | proved |
| reason | Adopt the complete independently reviewed bound for variable unit-circle-root rational reference prefixes, including both residual quadratic types, all original multiplicities and the conditional integer positive-to-zero interface. No admissible growing integer family is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every stated real-domain bound, reference, prefix range, growth condition and sufficient integer positivity subcase. |
| argument | [Complete proof and inputs](#argument) | Changed-reference argument and exact use of the earlier fixed results. |
| argument | [Interval accounting](#interval-root-accounting) | Every selected and residual root, unpaired pole and disjoint variation bound. |
| argument | [Neutral Newton sums](#neutral-newton-sums) | Full numerator and denominator multiplicities, inverse-root powers and exact constants. |
| argument | [Both quadratic cases](#real-and-nonreal) | Complete measure for real, repeated and nonreal residual roots. |
| argument | [Growing reference consequence](#growing-reference-consequence) | Exact asymptotic condition and strict positivity only under the additional integer hypotheses. |
| dependency | [Original grid](Yin_C_G0881_v3.md#original-domain) | Reciprocal lift, strict endpoint and mandatory interval roots at the unchanged scope. |
| dependency | [Disjoint matching](Yin_C_G0881_v3.md#paired-variation) | Actual right-pole pairing and variation identity, without its fixed-profile Newton constant. |
| dependency | [Integer endpoint theorem](Yin_C_G0881_v8.md#statement) | Strict complete measure and the exact nonreal exterior pair only for a=0, a0=2, kappa=1 integer inputs with the stated signs and endpoint. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v40.md#neutral-reference-bound-review) | Entire final statement, proof, required input interfaces, multiplicities, constants and existence limitations. |

## Current assessment

[Selected decision](#decision-variable-neutral-reference-bound)

