---
author: Yin
---

# Exact finite Fejer and Gram transition selection with complete multiplier-budget failures

This retains the complete original [L126 mathematical argument](../ledger/Yin_L_G0126_v1.md), with its original 2026-10-07 precision and attribution.
The original review_matrix_completion agent derived these finite selection and certificate bounds for Yin; the two original corrected specification findings and exact later checking limits remain at R36.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

For every finite real phase vector, every integer K>=2 and the exact resonance return mass p in (1), the Fejer identity proves max_(1<=k<K) Q(k)^2>=(Kp-1)/(K-1), excluding the zero multiplier with its full cost.
For the actual algebraic transition window of a positive-Mahler unit with central conjugates, the resonance mass is at least its true collision probability and the explicit inverse support bound U_r^(-1).
For every M distinct integral candidates whose phase vectors have rank at most R_r, M>R_r guarantees a nonzero candidate difference satisfying the exact Gram bound (5).
For coefficient candidates in {0,...,Q}^d, require explicitly integer Q>=1 and 0<epsilon<=1; one central cell has the guaranteed occupancy (6), and every selected difference preserves the stated nonzero, central-radius and height bounds.
In the target range 0<m<log2, the exact simultaneous tail certificate has h lambda<=2m and U_r>=(16dH')^h.
The available return-mass and occupancy estimates consequently fail their own sufficient multiplier and rank comparisons by (9)--(10), for every stated parameter choice.
The seed central bound epsilon/K is a sufficient uniform choice, not a necessary condition for an actually selected k<K.
No actual return mass upper bound, reverse actual occupancy/rank bound, impossible good selection, positive limiting amplitude or uniform Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-isolated-complete-corrected-chain-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:26 |
| status | open |
| reason | Retain the complete corrected original theorem and argument; the separate isolated whole-target and corrected-chain review obligation remains open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire corrected original (1)--(10): finite Fejer normalization and exact resonances, actual collision/support and Gram-rank selection, strict cell domain and true height, all simultaneous-tail comparisons and ceiling/strict guards, sufficient-versus-necessary seed distinction and all certificate-versus-actual limits. |
| argument | [Complete argument](#argument) | Entire corrected original (1)--(10): finite Fejer normalization and exact resonances, actual collision/support and Gram-rank selection, strict cell domain and true height, all simultaneous-tail comparisons and ceiling/strict guards, sufficient-versus-necessary seed distinction and all certificate-versus-actual limits. |
| dependency | [Exact retained input](Yin_C_G0328_v1.md#mixed-trace-transition-product) | Exact algebraic transition phases, cell/height constants and simultaneous tail-window definitions. |
| dependency | [Exact retained input](Yin_C_G0281_v1.md#norm-grid-support-bound) | Complete absolute norm-grid support estimate, preserved under sign/bit affine conversion and a unit monomial shift. |


### Decision complete-self-check-isolated-review-pending

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:31 |
| status | open |
| reason | The entire corrected theorem and used logical chain pass the current whole self-check; retain open until a separate isolated whole-target and corrected-chain review discharges the original correction obligation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire corrected original (1)--(10): finite Fejer normalization and exact resonances, actual collision/support and Gram-rank selection, strict cell domain and true height, all simultaneous-tail comparisons and ceiling/strict guards, sufficient-versus-necessary seed distinction and all certificate-versus-actual limits. |
| argument | [Complete argument](#argument) | Entire corrected original (1)--(10): finite Fejer normalization and exact resonances, actual collision/support and Gram-rank selection, strict cell domain and true height, all simultaneous-tail comparisons and ceiling/strict guards, sufficient-versus-necessary seed distinction and all certificate-versus-actual limits. |
| dependency | [Exact retained input](Yin_C_G0328_v1.md#mixed-trace-transition-product) | Exact algebraic transition phases, cell/height constants and simultaneous tail-window definitions. |
| dependency | [Exact retained input](Yin_C_G0281_v1.md#norm-grid-support-bound) | Complete absolute norm-grid support estimate, preserved under sign/bit affine conversion and a unit monomial shift. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0553_v1.md#current-fejer-gram-finding) | Exact current statement, complete retained proof and used interfaces; self-reviewed. This does not discharge the separate isolated corrected-chain review obligation. |


### Decision isolated-complete-corrected-chain-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:54 |
| status | proved |
| reason | Adopt the actual fresh isolated complete corrected-target finding and full affected input chain, followed by complete R36/R553 comparison; both old specification defects and all actual-versus-certificate boundaries remain explicit without backdating old reviews. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire corrected original (1)--(10): finite Fejer normalization and exact resonances, actual collision/support and Gram-rank selection, strict cell domain and true height, all simultaneous-tail comparisons and ceiling/strict guards, sufficient-versus-necessary seed distinction and all certificate-versus-actual limits. |
| argument | [Complete argument](#argument) | Entire corrected original (1)--(10): finite Fejer normalization and exact resonances, actual collision/support and Gram-rank selection, strict cell domain and true height, all simultaneous-tail comparisons and ceiling/strict guards, sufficient-versus-necessary seed distinction and all certificate-versus-actual limits. |
| dependency | [Exact retained input](Yin_C_G0328_v1.md#mixed-trace-transition-product) | Exact algebraic transition phases, cell/height constants and simultaneous tail-window definitions. |
| dependency | [Exact retained input](Yin_C_G0281_v1.md#norm-grid-support-bound) | Complete absolute norm-grid support estimate, preserved under sign/bit affine conversion and a unit monomial shift. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0553_v1.md#current-fejer-gram-finding) | Exact current statement, complete retained proof and used interfaces; self-reviewed. This does not discharge the separate isolated corrected-chain review obligation. |
| review | [Actual complete independent finding](../audits/reviews/Yin_R_G0557_v1.md#complete-corrected-fejer-gram) | Entire corrected (1)–(10), both repaired specifications and all Fejer/resonance/Gram/cell/height/tail/ceiling interfaces and necessary complete C328/C281 inputs; independently reviewed. |


## Complete retained argument

<a id="argument"></a>
<a id="finite-fejer-transition-average"></a>
### An exact finite average with the zero multiplier removed

For arbitrary real phases \(x_1,\ldots,x_r\), let
\[
 Q(k)=\prod_{j=1}^r|\cos(2\pi kx_j)|,\qquad k\in\mathbb Z.
\]
Let \(\xi_j,\xi'_j\) be two independent fair-sign vectors and put
\[
 Z=\sum_{j=1}^r(\xi_j-\xi'_j)x_j,\qquad
 p=\mathbb P(Z\in\mathbb Z).
 \tag{1}
\]
Thus \(Q(k)^2=\mathbb E e^{2\pi i kZ}\).
The exact return mass \(p\) includes every integer resonance, not only equality of the two sign words; in particular \(p\geq2^{-r}\).

For an integer \(K\geq2\), direct expansion gives the nonnegative trigonometric identity
\[
 F_K(z):=\sum_{|k|<K}(1-|k|/K)e^{2\pi ikz}
       =\frac1K\left|\sum_{a=0}^{K-1}e^{2\pi iaz}\right|^2.
\]
At integers \(F_K=K\), so
\[
 1+2\sum_{k=1}^{K-1}(1-k/K)Q(k)^2
       =\mathbb E F_K(Z)\geq Kp.
\]
Since the total weight on the nonzero indices is \(K-1\),
\[
 \max_{1\leq k<K}Q(k)^2\geq
             \frac{Kp-1}{K-1}.
 \tag{2}
\]
The bound is useful when \(Kp>1\).
If only a certified \(p\geq p_0>0\) is known, taking \(K=\lceil2/p_0\rceil\) guarantees some nonzero \(k<K\) with \(Q(k)\geq\sqrt{p_0/2}\).
For example the universal \(p_0=2^{-r}\) gives \(K=2^{r+1}\) and \(Q(k)\geq2^{-(r+1)/2}\).
No equidistribution, rational independence, or limiting average is used.
The cost of excluding \(k=0\), whose product is one, is the explicit subtraction in (2).

<a id="algebraic-transition-return-mass"></a>
### The trace window has an actual algebraic collision contribution

Let \(\alpha\), \(P\), \(d\), \(m>0\), and its stable, central, and expanding embeddings have the hypotheses of L G0123.
Fix \(\theta\in\mathbb Z[\alpha]\setminus\{0\}\), and write
\[
 \psi_\theta(x)=\sum_{\text{stable or central }\sigma}
                                      \sigma(\theta x).
\]
This real-valued additive map need not be injective.
For \(J\geq0\) put \(r=2J+1\), and let
\[
 S=\sum_{j=-J}^{J}\xi_j\alpha^j,\qquad
 R_r=|\operatorname{supp}S|.
\]
The integer trace identity changes the negative-index factors in L G0123's transition product to these same mixed phases.
Consequently its product for multiplier \(k\theta\) is exactly
\[
 C(k\theta,J)=
   \left|\mathbb E e^{2\pi i k\psi_\theta(S)}\right|.
\]
The return mass in (1) is now
\[
 p_{\theta,J}=\mathbb P\bigl(\psi_\theta(S-S')\in\mathbb Z\bigr)
       \geq \mathbb P(S=S')
       \geq R_r^{-1}.
 \tag{3}
\]
The equality event on the right uses independent copies with their actual, possibly nonuniform, algebraic-sum law.
It is not asserted that integer trace resonances are only algebraic collisions.
The second inequality is Cauchy--Schwarz.

Multiplication by \(\alpha^J\) and the injective conversion between signs and bits preserve support cardinality.
The [integer norm-grid estimate](Yin_C_G0281_v1.md#norm-grid-support-bound) therefore supplies
\[
 R_r\leq U_r:=
    \min\{2^r,(4r)^d e^{(r-1)m}\},\qquad
 p_{\theta,J}\geq U_r^{-1}.
 \tag{4}
\]
Using an exact collision probability or the actual larger resonance mass in (2) can improve this estimate.
Formula (4) is only the presently available unconditional input to this particular averaging argument.

<a id="many-pair-transition-gram-bound"></a>
### Many candidates in one cell give a Gram-matrix test

Take distinct integral candidates \(\theta_1,\ldots,\theta_M\), and fix the same algebraic word \(S\).
If its distinct values are \(z_1,\ldots,z_{R_r}\), with probabilities \(p_a\), associate to each candidate the unit vector
\[
 v_i=\bigl(\sqrt{p_a}\,e^{2\pi i\psi_{\theta_i}(z_a)}
                                    \bigr)_{a=1}^{R_r}.
\]
Their Gram matrix \(G\) is positive semidefinite, has trace \(M\), and rank at most \(R_r\).
By Cauchy--Schwarz on its nonnegative eigenvalues, \(\sum_{i,j}|G_{ij}|^2\geq M^2/R_r\).
The diagonal contributes \(M\), and \(|G_{ij}|=C(\theta_i-\theta_j,J)\).
Thus, if \(M>R_r\), there are distinct \(i,j\) such that
\[
 C(\theta_i-\theta_j,J)^2
       \geq \frac{M/R_r-1}{M-1}.
 \tag{5}
\]
The actual rank of \(G\), if known to be smaller, may replace \(R_r\).
This is a genuine finite selection theorem, not an independence assertion about the phase vectors.

Let Q>=1 be an integer and let 0<epsilon<=1.
If the candidates are in one central coordinate cell of side \(\epsilon/\sqrt2\), their difference has every central conjugate of modulus less than \(\epsilon\).
Using coefficient vectors in \(\{0,\ldots,Q\}^d\), its coefficients have modulus at most \(Q\), so its full height is at most \(H=L_P Q\), with \(L_P\) as in L G0123.
The difference is nonzero since its polynomial has degree less than \(d\).

Writing \(h=d-q\) and \(A_d=2\sqrt2\,d+2\), the same finite cell count as L G0123 ensures some cell contains at least
\[
 M\geq\lceil G_Q\rceil,\qquad
 G_Q=\frac{(Q+1)^d}{(A_dQ/\epsilon)^q}.
 \tag{6}
\]
If actual occupancy and actual rank satisfy (5), this yields an admissible small-center pair without an additional integer multiplier.
It preserves the stated coefficient and height budgets exactly.

<a id="transition-averaging-certificate-feedback"></a>
### Why the supplied estimates do not close the tail budget

Now assume the target range \(0<m<\log2\).
Write \(s,u>0\) for the stable and expanding field counts, \(h=s+u\geq2\), and set
\[
 \rho=\max\{\max_{\rm stable}|\beta|,
                  \max_{\rm expanding}|\beta|^{-1}\},\qquad
 \lambda=-\log\rho.
\]
The unit norm gives both \(\sum_{\rm stable}-\log|\beta|=m\) and \(\sum_{\rm expanding}\log|\beta|=m\).
Hence
\[
 h\lambda\leq2m.
 \tag{7}
\]
For a height bound \(H'\geq1\), L G0123 uses
\[
 J=\left\lceil\frac{\log(16dH')}{\lambda}\right\rceil,
 \qquad r=2J+1.
\]
It follows that
\[
 e^{(r-1)m}=e^{2Jm}\geq(16dH')^h,\qquad
 U_r\geq(16dH')^h.
 \tag{8}
\]
For the second inequality, both quantities in the minimum defining \(U_r\) exceed \(e^{(r-1)m}\), since \(m<\log2\).

First consider the multiples in (2).
To certify the same tail bounds for all \(1\leq k<K\), start with seed height \(H\geq1\) and use \(H'=KH\).
To retain a desired central bound \(\epsilon\) uniformly, it suffices to impose seed central moduli at most \(\epsilon/K\); under this choice norm forces \(H\geq(K/\epsilon)^{q/h}\).
Even without charging this last cost, (8) gives
\[
 K\,U_r^{-1}\leq\frac{K}{(16dKH)^h}<1.
 \tag{9}
\]
Thus the lower return-mass estimate (4) never makes the nonzero-multiplier criterion \(Kp_0>1\) hold in this simultaneous tail certificate.
This is not an upper bound on \(Kp_{\theta,J}\): the actual return mass can be larger.
Keeping the old window while allowing \(k\) to grow avoids (9) only by leaving the corresponding larger hyperbolic tails unaccounted for.

Next consider the many-pair construction.
Take \(H'=L_P Q\), \(Q\geq1\), and \(0<\epsilon\leq1\).
Equations (6) and (8) imply
\[
 \frac{G_Q}{U_r}
 \leq\frac{2^d}{A_d^q(16dL_P)^h}
 \leq(8d)^{-h},\qquad U_r\geq(16d)^h.
 \tag{10}
\]
In particular \(\lceil G_Q\rceil\leq G_Q+1<U_r\).
The available lower occupancy and upper rank bounds therefore cannot certify \(M>R_r\) through the sufficient comparison \(\lceil G_Q\rceil>U_r\), at any choice of \(Q,\epsilon\).
Again neither actual occupancy nor actual rank has been bounded in the reverse direction.
Better rank, collision, or resonance information could change this finite test.

Equations (9)–(10) are precise failures of the supplied estimates, not failures of (2) or (5).
They also explain why the apparently better \(e^{-O(r)}\) finite product furnished by averaging cannot be inserted into L G0123 while silently keeping its old height, center radius, or transition length.
