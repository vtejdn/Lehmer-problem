---
author: Yin
---

# Finite transition-product averaging and its multiplier budget

## Current complete mathematical home

The complete current theorem and argument are retained in [C331v1](../claims/Yin_C_G0331_v1.md#statement), actually adopted at 2026-10-21T09:54 through the fresh complete isolated finding in [R557](../audits/reviews/Yin_R_G0557_v1.md#complete-corrected-fejer-gram).
The original two specification findings, uncertain old check timing and known later shared-context check retain their actual scopes in R36; the new whole corrected-chain review does not backdate them.
The full original mathematical input, costs, source/failure and checking history below remain unchanged and supply no current Task/E authority.

Date: 2026-10-07.
Direct bounded G0001 work by the assigned review_matrix_completion AI for Yin.
This note tests integer multiples and many pigeonhole pairs as ways to improve the transition product in [L G0123](Yin_L_G0123_v1.md#mixed-trace-transition-product).
It gives exact finite averaging statements.
It then identifies why the presently supplied collision and occupancy estimates alone do not close their own height and tail budgets in the small-Mahler window.
That certificate failure is not an impossibility assertion about actual good multiples, actual good pairs, or sharper arithmetic information.
No new source, computation, or novelty claim is involved.

<a id="finite-fejer-transition-average"></a>
## An exact finite average with the zero multiplier removed

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
## The trace window has an actual algebraic collision contribution

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
The [integer norm-grid estimate](Yin_L_G0091_v1.md#norm-grid-support-bound) therefore supplies
\[
 R_r\leq U_r:=
    \min\{2^r,(4r)^d e^{(r-1)m}\},\qquad
 p_{\theta,J}\geq U_r^{-1}.
 \tag{4}
\]
Using an exact collision probability or the actual larger resonance mass in (2) can improve this estimate.
Formula (4) is only the presently available unconditional input to this particular averaging argument.

<a id="many-pair-transition-gram-bound"></a>
## Many candidates in one cell give a Gram-matrix test

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
## Why the supplied estimates do not close the tail budget

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



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0036_v1.md#scope-and-review), with its original inspected scope and relationship.
