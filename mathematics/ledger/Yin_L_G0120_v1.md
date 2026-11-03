---
author: Yin
---

# A finite-window Gaussian entropy interface retaining central embeddings

Date: 2026-10-07.
Direct bounded G0001 work by the assigned AI review_matrix_completion for Yin, from the coordinator's proposed finite-window construction.
All logarithms are natural.
This note extends the finite smoothing mechanism in [L G0102](Yin_L_G0102_v1.md#disjoint-smoothing-relative-entropy) to algebraic units with unit-circle conjugates.
It constructs no stationary central coding and assumes no nondecaying Fourier amplitude.
No new external source, computation, or novelty claim is involved.

<a id="finite-window-stable-central-smoothing"></a>
## Domain, coordinates, and exact separation

Let \(\alpha\) be any algebraic unit, \(P\) its monic irreducible polynomial of degree \(d\), and \(m=\log M(P)\geq0\).
Partition its embeddings into stable, central, and expanding places according as \(|\beta|<1\), \(|\beta|=1\), or \(|\beta|>1\).
Take one representative of each complex-conjugate pair, and write

\[
 E_s=\mathbb R^{r_s}\times\mathbb C^{c_s},\qquad
 E_c=\mathbb R^{r_c}\times\mathbb C^{c_c},\qquad
 s=r_s+2c_s,\quad q=r_c+2c_c,\quad t=s+q.
 \tag{1}
\]

The product norm of all conjugates of a unit is one, so \(t\geq1\).
Each complex coordinate is identified with its ordinary two-dimensional Euclidean plane: its contribution to squared Euclidean norm is \(|z|^2\), not \(2|z|^2\).
Norms of algebraic numbers, by contrast, count both complex embeddings.
Let \(\iota_{sc}\) denote the projection of the Minkowski embedding to \(E_s\oplus E_c\).
This map is injective on \(\mathbb Q(\alpha)\), since even one field embedding is injective.

For independent fair signs \(\xi_j\), put

\[
 S_N=\sum_{j=0}^{N-1}\xi_j\alpha^j,\quad
 Y_N=\iota_{sc}(S_N),\quad H_N=H(S_N)=H(Y_N),\qquad N\geq1.
\]

Let \(K_N\) be the product of intervals or complex discs with radius \(|\beta|^N\) at stable places and radius one at central places.
Define

\[
 B_e=\prod_{|\beta|>1}(|\beta|-1),\qquad
 a=\tfrac12 B_e^{1/t},\qquad
 V_0=2^{r_s+r_c}\pi^{c_s+c_c},\qquad \gamma=a^tV_0.
 \tag{2}
\]

The product defining \(B_e\) counts each complex embedding and is one if there are no expanding places.
The factor \(1/2\) in \(a\) gives a single strict separation proof that also includes \(m=0\).
For \(m>0\) the larger choice \(a=B_e^{1/t}\) also works by the strict expanding geometric-series bound below; it changes only constants.

If two distinct values of \(S_N\) differ by \(2x\), then \(x=\sum_{j<N}\delta_j\alpha^j\ne0\), where \(\delta_j\in\{-1,0,1\}\).
Suppose \(\iota_{sc}(x)\in aK_N\).
The nonzero number \(\alpha^{-N}x\) is an algebraic integer.
At every stable or central place its modulus is at most \(a\), while at an expanding place

\[
 |\beta^{-N}x(\beta)|
 \leq\sum_{l=1}^{N}|\beta|^{-l}
 <\frac1{|\beta|-1}.
\]

Consequently its absolute integer norm is at most \(a^t/B_e=2^{-t}<1\), a contradiction.
Since \(aK_N-aK_N=2aK_N\), the translates \(y+aK_N\) indexed by the distinct atoms \(y\) of \(Y_N\) are pairwise disjoint.
The unit norm identity also gives

\[
 \operatorname{vol}(aK_N)=\gamma e^{-Nm}.
 \tag{3}
\]

<a id="finite-window-central-kl-identity"></a>
## Exact entropy and the anisotropic Gaussian

Let \(U_N\) be independent uniform noise on \(aK_N\), and let \(f_N\) be the density of \(X_N=Y_N+U_N\).
Disjointness, including when many sign words represent the same atom, gives the exact identity

\[
 h_{\mathrm{diff}}(f_N)=H_N+\log\gamma-Nm.
 \tag{4}
\]

For clarity define sums below over the chosen real and complex representatives, without duplicating complex terms:

\[
 \begin{split}
 K_s&=\sum_{\beta\ \text{stable representative}}
                \frac1{1-|\beta|^2},\qquad
 \eta_s=\frac{r_s}{3}+\frac{c_s}{2},\\
 \kappa_c&=r_c+c_c,\qquad
 \eta_c=\frac{r_c}{3}+\frac{c_c}{2},\\
 b_{s,N}&=\sum_{\beta\ \text{stable representative}}
            \frac{1-|\beta|^{2N}}{1-|\beta|^2}
       +a^2\left(\frac13\sum_{\beta\ \text{real stable}}|\beta|^{2N}
                  +\frac12\sum_{\beta\ \text{complex stable}}|\beta|^{2N}
            \right).
 \end{split}
 \tag{5}
\]

Empty sums vanish.
Mean zero and independence of the signs give \(\mathbb E|\sum_{j<N}\xi_j\beta^j|^2=\sum_{j<N}|\beta|^{2j}\) at each representative.
Uniform interval and disc noises have second moments respectively radius squared divided by three and by two.
Thus

\[
 \mathbb E\|(X_N)_s\|^2=b_{s,N}\leq K_s+a^2\eta_s,
 \qquad
 \mathbb E\|(X_N)_c\|^2=N\kappa_c+a^2\eta_c.
 \tag{6}
\]

There is no assertion that the central coordinate covariance is \(NI_q\): different embeddings use the same signs.
In particular the exact central squared moment is \(N\kappa_c\), not \(Nq\), before adding noise.

Take as reference the centered Gaussian with covariance \(\Sigma_N=\operatorname{diag}(I_s,NI_q)\), whose density is

\[
 \varphi_N(x)=(2\pi)^{-t/2}N^{-q/2}
       \exp\left[-\tfrac12(\|x_s\|^2+\|x_c\|^2/N)\right].
\]

Equations (4) and (6) prove

\[
 \begin{split}
 D(f_N\Vert\varphi_N)
 &=Nm-H_N+\frac q2\log N+c_{P,N},\\
 c_{P,N}
 &=-\log\gamma+\frac t2\log(2\pi)
            +\frac12\left(b_{s,N}+\kappa_c+\frac{a^2\eta_c}{N}\right),\\
 |c_{P,N}|&\leq C_P:=|\log\gamma|+\frac t2\log(2\pi)
          +\frac12(K_s+a^2\eta_s+\kappa_c+a^2\eta_c).
 \end{split}
 \tag{7}
\]

All constants are explicit and finite for the fixed input.
This is an identity for every \(N\), including \(m=0\).
In particular nonnegativity of relative entropy yields \(H_N\leq Nm+(q/2)\log N+C_P\).
The usual splitting of the independent sum makes \(H_N\) subadditive; therefore \(h_1=\lim H_N/N\) exists, and (7) gives \(h_1\leq m\).
This consequence recovers an existing rate bound, rather than providing a positive entropy deficit by itself.

<a id="central-whitening-fourier-test"></a>
## Fourier tests and their exact frequency cost

Use the real Euclidean pairing, including the two real coordinates of each complex place, and the Fourier convention \(\widehat\mu(\zeta)=\int e^{2\pi i\langle\zeta,x\rangle}\,d\mu(x)\).
Put \(B_N=\operatorname{diag}(I_s,\sqrt N I_q)\).
Whitening the primal variable by \(B_N^{-1}\) transforms a covector \(\zeta\) into

\[
 \nu=B_N^T\zeta=(\zeta_s,\sqrt N\zeta_c),\qquad
 \widehat\varphi_N(\zeta)=e^{-2\pi^2\|\nu\|^2}.
 \tag{8}
\]

In particular center frequencies are multiplied, not divided, by \(\sqrt N\) in the Gaussian test.
The exact smoothed characteristic function is

\[
 \widehat f_N(\zeta)=\widehat U_N(\zeta)
        \prod_{j=0}^{N-1}
              \cos(2\pi\langle\zeta,\iota_{sc}(\alpha^j)\rangle).
 \tag{9}
\]

For an explicit sufficient control on the noise define the support function

\[
 h_{K_N}(\zeta)=
   \sum_{\text{stable real}}|\beta|^N|\zeta_\beta|
  +\sum_{\text{stable complex}}|\beta|^N\|\zeta_\beta\|
  +\sum_{\text{central real}}|\zeta_\beta|
  +\sum_{\text{central complex}}\|\zeta_\beta\|.
\]

Symmetry and \(\cos x\geq1-x^2/2\) show that, for \(0<\eta<1\),

\[
 2\pi a h_{K_N}(\zeta)\leq\sqrt{2\eta}
 \quad\Longrightarrow\quad \widehat U_N(\zeta)\geq1-\eta.
 \tag{10}
\]

Fix \(N\), and suppose that \(\zeta_1,\ldots,\zeta_K\) have whitened frequencies \(\nu_l=B_N^T\zeta_l\) satisfying

\[
 \|\nu_l\|\geq4^l,\qquad
 \|\nu_{l+1}\|\geq4\|\nu_l\|.
 \tag{11}
\]

The dimension-independent [Gaussian lacunary bound of L G0102](Yin_L_G0102_v1.md#gaussian-lacunary-riesz-bound) has the following weighted form, contributed here by the coordinator.
For arbitrary signs \(\varepsilon_l\) and arbitrary \(u_l\geq0\),

\[
 \log\mathbb E_{\varphi_N}
      \exp\left(\sum_{l=1}^K u_l\varepsilon_l
                       \cos(2\pi\langle\zeta_l,X\rangle)\right)
 \leq \sum_{l=1}^K\log\cosh u_l+\log2.
\]

For completeness, apply the convex chord inequality separately and put \(b_l=\tanh u_l\).
A nonconstant term with largest frequency index \(l\) has total absolute coefficient at most \(b_l\prod_{i<l}(1+b_i)\leq2^{l-1}\).
Every nonzero signed frequency sum with that largest index has norm at least \((2/3)4^l\).
After Gaussian integration, the total nonconstant contribution is at most \(\sum_{l\geq1}2^{l-1}\exp[-(8\pi^2/9)16^l]<1\), exactly the convergent bound used in L G0102.
The remaining constant term is one.
This proves the weighted form without assuming independent scales.

Choose the signs according to the real Fourier coefficients in (9).
The relative-entropy variational inequality and separate optimization in every \(u_l\) then yield, with \(g(b)=\tfrac12[(1+b)\log(1+b)+(1-b)\log(1-b)]\),

\[
 D(f_N\Vert\varphi_N)\geq
       \sum_{l=1}^K g(|\widehat f_N(\zeta_l)|)-\log2,
 \qquad
 Nm-H_N\geq
       \sum_{l=1}^K g(|\widehat f_N(\zeta_l)|)
                  -\frac q2\log N-C_P-\log2.
 \tag{12}
\]

Here \(g(1)=\log2\) by continuity; an amplitude equal to one is handled by taking the corresponding finite test parameter to infinity after applying the inequality.
Thus (12) retains the actual spectral budget and requires no uniform lower amplitude assumption.

As a conditional corollary, if every smoothed amplitude is at least \(b\), the sum in (12) is at least \(K g(b)\).
For example this follows if the unsmoothed product in (9) has modulus at least \(c\) at every chosen frequency and (10) holds there, with \(b=(1-\eta)c\).
Neither premise is supplied by this construction.
If such tests with a fixed positive \(b\) and \(\liminf K/N>0\) were proved along an unbounded sequence of windows, (12) would imply a positive rate deficit.
This is explicitly conditional.

The normalization also exposes a restricted cost: if one uses only pure central covectors and insists on (10) with fixed \(\eta\), then \(\|\nu_l\|\leq \sqrt{2\eta N}/(2\pi a)\), since \(h_{K_N}(\zeta)\geq\|\zeta_c\|\).
Consequently (11) permits at most \(K\leq(\log N)/(2\log4)+O_{P,\eta}(1)\) such tests.
This statement concerns that sufficient small-phase condition and that lacunary selection; it is not an impossibility theorem for other Fourier tests.

## Scope and review

For \(q=0\), (7) reduces to the hyperbolic smoothing interface already used in L G0102, up to the harmless fixed choice of noise radius.
For \(q>0\), the actual algebraic sums and their original entropy are retained, with a logarithmic central Gaussian cost.
The laws \(f_N\) and Gaussian references depend on \(N\); no stationary central lift, toral coding, Fourier nondecay, or uniform entropy gap follows.
Thus this finite-window construction does not reverse the retained central-lift obstructions.

The authoring agent checked the complete derivation.
The coordinator contributed the proposed stable-plus-central construction and Gaussian comparison, and pointed out the distinction between complex-coordinate second moments and real dimension.
The coordinator completed a full collaborator check of the initial (1)–(12).
The independent reviewing agent assess_shortness_route checked that full initial proof, including the all-unit domain, complex normalization, exact KL identity, whitening, and restricted central frequency count, and identified only a TeX-label defect, now repaired.
The coordinator subsequently contributed the weighted Gaussian test and actual-amplitude budget.
The same independent reviewer then checked the complete written strengthening, including every coefficient and Gaussian cross-term constant, separate optimization and the amplitude-one limiting case, and reread the repaired TeX labels.
Together these reviews cover the entire final (1)–(12), with no remaining mathematical defect.
No computation or new source acquisition was performed.

The coordinator additionally read and checked the final weighted proof as written: the separate convex chords, largest-index coefficient sum, Gaussian frequency bound, optimization in each parameter and the limiting amplitude-one case.
This completes its collaborator check of the final text; it does not supply another independent review.
