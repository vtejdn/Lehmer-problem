---
author: Yin
---

# Polynomial-height central approximation with complete mixed-frequency transition and consistency costs

This retains the complete original 2026-10-07 [L123 mathematical argument](../ledger/Yin_L_G0123_v1.md).
The original review_matrix_completion agent derived this construction for Yin; the coordinator supplied the finite consistency interface (13)--(14), with exact original checking retained at R35.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

Fix a positive-Mahler algebraic unit P with actual degree d, q>0 central conjugates and h=d-q>0 noncentral conjugates.
For every 0<epsilon<=1, the explicit finite integer construction (1)--(2) supplies a nonzero theta in Z[alpha] with all central abs(sigma(theta))<epsilon and total conjugate height H<=C_P epsilon^(-q/h).
Integer norm forces H>=epsilon^(-q/h), giving the stated optimal common noncentral height exponent.
For fixed 0<kappa<=1/(16q), epsilon_N=kappa/sqrt(N), fixed noise margin eta and every sufficiently large N, the full transition, tail, noise and whitening constants (4)--(10) give k_N=N/ell_0-O(log N) actual ratio-four frequencies, with smoothed amplitudes at least b_N=(1-eta)exp(-4pi^2 E0) C(theta_N,J_N)>0.
The exact finite Gaussian deficit certificate is (11).
The transition product has the effective splitting-field lower bound (12), at least exp(-O((log(N+1))^2)), which proves no fixed positive limiting amplitude.
Every window meeting the displayed conditions obeys the necessary finite consistency inequality (13) using the actual all-unit k=1 entropy upper error C(m); the limsup restriction (14) holds with its stated inverse-g domain and input-dependent ell_0.
No stronger transition-product floor, actual product decay, cube feasibility, stationary lift, positive actual rate deficit or uniform Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:16 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(14): strict real/complex pigeonholing and optimal integer norm height, all mixed transition/nonzero phase/tail constants, actual noise support and whitening/frequency guards, splitting-field norm product, finite and limiting entropy consistency with every conditional/input-dependent limit. |
| argument | [Complete argument](#argument) | Entire original (1)--(14): strict real/complex pigeonholing and optimal integer norm height, all mixed transition/nonzero phase/tail constants, actual noise support and whitening/frequency guards, splitting-field norm product, finite and limiting entropy consistency with every conditional/input-dependent limit. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#central-whitening-fourier-test) | Complete all-unit finite-window exact KL, actual noise/amplitudes and separately optimized weighted Fourier budget. |
| dependency | [Exact retained input](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) | Exact k=1 all-unit algebraic-sum upper deficit C(m), not a hyperbolic-only toral equality. |
| dependency | [Exact retained input](Yin_C_G0302_v1.md#bounded-multiplier-family-obstruction) | Only fixed-height finiteness/low-frequency comparison context; the new moving construction proves its own height and frequency bounds. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:20 |
| status | proved |
| reason | Adopt the exact complete original theorem and retained argument after actual whole self-review with resolved used inputs, preserving every nonlinear, boundary, moment, actual-noise, finite-window and input-dependent limitation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(14): strict real/complex pigeonholing and optimal integer norm height, all mixed transition/nonzero phase/tail constants, actual noise support and whitening/frequency guards, splitting-field norm product, finite and limiting entropy consistency with every conditional/input-dependent limit. |
| argument | [Complete argument](#argument) | Entire original (1)--(14): strict real/complex pigeonholing and optimal integer norm height, all mixed transition/nonzero phase/tail constants, actual noise support and whitening/frequency guards, splitting-field norm product, finite and limiting entropy consistency with every conditional/input-dependent limit. |
| dependency | [Exact retained input](Yin_C_G0321_v1.md#central-whitening-fourier-test) | Complete all-unit finite-window exact KL, actual noise/amplitudes and separately optimized weighted Fourier budget. |
| dependency | [Exact retained input](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence) | Exact k=1 all-unit algebraic-sum upper deficit C(m), not a hyperbolic-only toral equality. |
| dependency | [Exact retained input](Yin_C_G0302_v1.md#bounded-multiplier-family-obstruction) | Only fixed-height finiteness/low-frequency comparison context; the new moving construction proves its own height and frequency bounds. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0552_v1.md#current-central-height-finding) | Exact current statement, complete original proof and directly used interfaces; self-reviewed, with exact original findings and actual relationships retained separately. |

## Complete retained argument

<a id="argument"></a>
Let \(\alpha\) be an algebraic unit with monic irreducible polynomial \(P\), degree \(d\), and \(m=\log M(P)>0\), with \(q>0\) central conjugates of modulus one.
Count all field embeddings, including both members of each complex pair.
Let \(s>0\) and \(u>0\) be the stable and expanding counts, and put \(h=s+u=d-q\).
No conjugate is a root of unity, so central conjugates are nonreal and \(q\) is even.

<a id="polynomial-height-central-approximation"></a>
### A direct integral construction with the optimal height exponent

For \(0<\epsilon\leq1\), set
\[
 A_d=2\sqrt2\,d+2,\qquad
 Q=\left\lceil(2A_d^q\epsilon^{-q})^{1/h}\right\rceil,\qquad
 L_P=\sum_{i=0}^{d-1}\max(1,\max_\beta|\beta|)^i .
 \tag{1}
\]
Consider the \((Q+1)^d\) algebraic integers \(\sum_{i=0}^{d-1}n_i\alpha^i\), with \(0\leq n_i\leq Q\).
In every real coordinate of the central embedding their values lie in \([-dQ,dQ]\).
Partition that interval into half-open cells of width \(\epsilon/\sqrt2\), with a final endpoint cell if necessary.
The number of cells in each coordinate is at most \(2\sqrt2\,dQ/\epsilon+2\leq A_dQ/\epsilon\).
Thus all \(q\) coordinates have at most \((A_dQ/\epsilon)^q\) cell labels, whereas \(Q^d\geq2(A_dQ/\epsilon)^q\).

Two distinct coefficient vectors have the same label.
Their difference gives \(\theta=\sum_{i<d}b_i\alpha^i\ne0\) in \(\mathbb Z[\alpha]\), with \(|b_i|\leq Q\), and
\[
 |\sigma(\theta)|<\epsilon\quad\text{at every central place},
 \qquad
 H:=\max_\sigma|\sigma(\theta)|
       \leq L_P Q\leq C_P\epsilon^{-q/h},
 \quad
 C_P=L_P\bigl((2A_d^q)^{1/h}+1\bigr).
 \tag{2}
\]
Nonvanishing follows from \(\deg P=d\), since the coefficient difference has degree less than \(d\).
A complex difference has modulus strictly less than \(\epsilon\), because its two real coordinate differences have modulus less than \(\epsilon/\sqrt2\).
This is a finite pigeonhole construction, not a complexity bound for finding the pair.

The exponent \(q/h\) cannot be decreased in a bound that controls all noncentral conjugates by the same \(H\).
Indeed integer norm gives
\[
 1\leq|\operatorname{Norm}\theta|
       \leq H^h\epsilon^q,\qquad H\geq\epsilon^{-q/h}.
 \tag{3}
\]
In particular \(H\geq1\).
This also shows that these multipliers leave every bounded conjugate-height set as \(\epsilon\) tends to zero, as required by the fixed-multiplier boundary of [L G0105](Yin_C_G0302_v1.md#bounded-multiplier-family-obstruction).

<a id="mixed-trace-transition-product"></a>
### Mixed traces isolate a logarithmic transition window

Fix \(0<\kappa\leq1/(16q)\).
For each \(N\geq1\), choose a multiplier from (2) with \(\epsilon=\epsilon_N=\kappa/\sqrt N\).
Thus \(H=O_P(N^{q/(2h)})\), with constants also depending on the fixed choice of \(\kappa\).
For all integers \(k\), write
\[
 u_k=\sum_{\rm stable}\sigma(\theta)\beta^k,\qquad
 v_k=\sum_{\rm expanding}\sigma(\theta)\beta^k,\qquad
 w_k=\sum_{\rm central}\sigma(\theta)\beta^k.
\]
Each sum is real.
Since \(\alpha\) is a unit, \(u_k+v_k+w_k=\operatorname{Tr}(\theta\alpha^k)\) is an integer even for negative \(k\).

Use the stable-plus-central coordinates of L G0120.
The trace covector \(\zeta_{\theta,0}\) has coordinate \(\sigma(\theta)\) at a real place and \((2\Re\sigma(\theta),-2\Im\sigma(\theta))\) at a chosen complex place.
If \(A_{sc}\) is multiplication by \(\alpha\) on that space, put \(\zeta_{\theta,t}=(A_{sc}^{\mathsf T})^{-t}\zeta_{\theta,0}\).
Then the actual fair-sign law \(\mu_N\) obeys
\[
 \langle\zeta_{\theta,t},\iota_{sc}(\alpha^j)\rangle=u_{j-t}+w_{j-t},
 \qquad
 |\widehat\mu_N(\zeta_{\theta,t})|
  =\prod_{k=-t}^{N-1-t}|\cos(2\pi(u_k+w_k))|.
 \tag{4}
\]
For \(k<0\), the corresponding factor equals \(|\cos(2\pi v_k)|\), by the integer trace identity.
This is the reason for retaining the central covector: the negative tail has no persistent central term.

Set
\[
 \rho=\max\{\max_{\rm stable}|\beta|,
                   \max_{\rm expanding}|\beta|^{-1}\}<1,\qquad
 J=\left\lceil\frac{\log(16dH)}{-\log\rho}\right\rceil,
\]
and define the finite transition product
\[
 C(\theta,J)=
   \prod_{k=-J}^{-1}|\cos(2\pi v_k)|
   \prod_{k=0}^{J}|\cos(2\pi(u_k+w_k))| .
 \tag{5}
\]
Every factor is strictly positive.
Its phase is an algebraic integer, being a sum of conjugates of algebraic integers.
It cannot equal an odd integer divided by four, since the rational algebraic integers are the integers.

For \(|k|>J\), the hyperbolic trace terms have absolute value at most \(dH\rho^{|k|}\leq1/16\), and \(|w_k|\leq q\epsilon\leq1/16\).
Thus all tail phases used in (4) have modulus at most \(1/8\).
Their squared sum is at most
\[
 E_0:=\frac{3}{256(1-\rho^2)}+2q^2\kappa^2.
 \tag{6}
\]
Indeed the negative tail contributes at most \(u^2H^2\rho^{2J+2}/(1-\rho^2)\).
The positive tail is bounded using \((u_k+w_k)^2\leq2u_k^2+2w_k^2\), contributing at most \(2s^2H^2\rho^{2J+2}/(1-\rho^2)+2Nq^2\epsilon^2\).
The definition of \(J\) gives (6), with slack.

On \(|x|\leq1/8\), the second derivative of \(-\log\cos(2\pi x)\) is at most \(8\pi^2\), so \(|\cos(2\pi x)|\geq e^{-4\pi^2x^2}\).
Therefore, whenever \(J\leq t\leq N-1-J\),
\[
 |\widehat\mu_N(\zeta_{\theta,t})|
       \geq C(\theta,J)e^{-4\pi^2E_0}.
 \tag{7}
\]
The transition product, containing \(2J+1=O_P(\log N)\) factors, is independent of \(t\) throughout this window.

<a id="linear-mixed-lacunary-frequency-count"></a>
### Smoothing and whitening leave linearly many usable frequencies

Fix \(0<\eta<1\), and retain the noise radius \(a\), noise body \(K_N\), and smoothed law \(f_N\) from L G0120.
Let \(\rho_s=\max_{\rm stable}|\beta|<1\).
The exact support function of the mixed covector satisfies
\[
 h_{K_N}(\zeta_{\theta,t})
   =\sum_{\rm stable}|\sigma(\theta)|\,|\beta|^{N-t}
       +\sum_{\rm central}|\sigma(\theta)|
   \leq dH\rho_s^{N-t}+q\epsilon .
 \tag{8}
\]
Both sums count the two members of a complex pair; this matches the factor two in its real trace covector.
For all sufficiently large \(N\), \(q\epsilon\leq\sqrt{2\eta}/(4\pi a)\).
Define
\[
 R_N=\max\left\{J+1,\ 0,\
       \left\lceil
        \frac{\log(4\pi a dH/\sqrt{2\eta})}{-\log\rho_s}
       \right\rceil\right\}.
\]
For \(t\leq N-R_N\), (8) and L G0120's small-phase bound give \(\widehat U_N(\zeta_{\theta,t})\geq1-\eta\).
Together with (7), the smoothed modulus is at least
\[
 b_N=(1-\eta)e^{-4\pi^2E_0} C(\theta,J)>0.
 \tag{9}
\]

There is also a quantitative lower bound on the stable covector, which excludes the low-frequency escape of unit-power multipliers in L G0105.
Every conjugate of the nonzero integral \(\theta\) has modulus at least \(H^{-(d-1)}\), by its integer norm.
As a stable place exists, \(\|(\zeta_{\theta,0})_s\|\geq H^{-(d-1)}\).
The stable multiplication is normal in these real coordinates, so, with \(r_t=\|(\zeta_{\theta,t})_s\|\),
\[
 r_t\geq \rho_s^{-t}H^{-(d-1)},\qquad
 r_{t+\ell}\geq \rho_s^{-\ell}r_t.
\]
The whitened central covector has constant norm in \(t\), bounded by \(\sqrt{2qN}\epsilon=\sqrt{2q}\kappa=:C_c\).
Use
\[
 T_N=\max\left\{J,\
    \left\lceil
       \frac{\log(\max(4,C_c)H^{d-1})}{-\log\rho_s}
    \right\rceil\right\},\qquad
 \ell_0=\left\lceil\frac{\log(4\sqrt2)}{-\log\rho_s}\right\rceil.
\]
For \(t\geq T_N\), \(r_t\geq\max(4,C_c)\).
Thus the whitened frequencies \(\nu_t=((\zeta_{\theta,t})_s,\sqrt N(\zeta_{\theta,t})_c)\) have
\[
 \|\nu_t\|\geq4,\qquad
 \|\nu_{t+\ell_0}\|/\|\nu_t\|
        \geq \rho_s^{-\ell_0}/\sqrt2\geq4.
\]
Select \(t=T_N,T_N+\ell_0,\ldots\leq N-R_N\).
For sufficiently large \(N\) there are
\[
 k_N=\left\lfloor\frac{N-R_N-T_N}{\ell_0}\right\rfloor+1
       =\frac N{\ell_0}-O_{P,\kappa,\eta}(\log N)
 \tag{10}
\]
such frequencies.
They satisfy exactly the normalization in L G0120, including \(\|\nu_j\|\geq4^j\) when relabelled from \(j=1\).
The covariance normalization is essential here: the central frequency is multiplied by \(\sqrt N\), but (2) keeps its whitened norm bounded; it does not swamp the growing stable frequencies.

The unconditional conclusion is the finite certificate
\[
 Nm-H_N\geq k_N g(b_N)-\frac q2\log N-C_{\!P}^{\,\mathrm{KL}}-\log2,
 \tag{11}
\]
where \(C_{\!P}^{\,\mathrm{KL}}\) is the explicit constant in L G0120 and \(g(x)=((1+x)\log(1+x)+(1-x)\log(1-x))/2\).
For example a positive lower bound on \(C(\theta_N,J_N)\) along an unbounded sequence would imply a positive rate deficit.
No such lower bound independent of \(N\) has been established.

<a id="transition-cosine-integral-norm-bound"></a>
### Integrality bounds the transition loss but does not remove it

The nonzero-factor statement in (5) has an effective refinement.
Let \(F\) be the splitting field of \(P\), \(D=[F:\mathbb Q]\), and \(\Lambda=\max_\beta\max(|\beta|,|\beta|^{-1})\).
For a phase \(x=v_k\) or \(u_k+w_k\), \(|k|\leq J\), every embedding of \(F\) sends it to a sum of at most \(d\) terms, each of modulus at most \(H\Lambda^J\).
Put \(B=dH\Lambda^J\).
Choose the nearest odd integer \(n\) to \(4x\); then \(|4x-n|\leq1\) and \(|n|\leq4B+1\).

The algebraic integer \(y=4x-n\) is nonzero, and every other conjugate has modulus at most \(8B+1\).
Integer norm therefore gives \(|y|\geq(8B+1)^{-(D-1)}\).
For \(|y|\leq1\), \(|\cos(2\pi x)|=|\sin(\pi y/2)|\geq|y|\).
Hence
\[
 C(\theta,J)\geq
       (8dH\Lambda^J+1)^{-(D-1)(2J+1)}
       \geq \exp[-O_{P,\kappa}((\log(N+1))^2)].
 \tag{12}
\]
The field is fixed; no growing-degree premise enters this estimate.
This is a proved positive amplitude bound, but it decreases with the window.
Substitution of this lower bound into (11) does not certify a positive asymptotic deficit: the explicit lower estimate it supplies for \(g(b_N)\) tends to zero.
It does not prove the actual transition products tend to zero.

<a id="finite-transition-product-consistency-test"></a>
### A single-window arithmetic consistency test

The coordinator contributed the following use of the retained [convolution entropy estimate](Yin_C_G0305_v1.md#quantitative-convolution-entropy-convergence).
At its \(k=1\) specialization,
\[
 0\leq m-h_1\leq \mathcal C(m)
   :=\frac5{12}(e^{2m}-1)^2(1-e^{-4m}).
\]
Subadditivity gives \(H_N\geq Nh_1\), so \(Nm-H_N\leq N\mathcal C(m)\) for every \(N\).
Combining this with (11), and putting \(A_*=(1-\eta)e^{-4\pi^2E_0}\), proves the necessary finite bound
\[
 k_N\,g\!\left(A_*C(\theta_N,J_N)\right)
 \leq N\mathcal C(m)+\frac q2\log N
                         +C_{\!P}^{\,\mathrm{KL}}+\log2.
 \tag{13}
\]
Every sufficiently large \(N\) in the construction satisfies this inequality.
More generally it holds at any one window for which the displayed tail, noise, and frequency conditions have been verified.
A certified lower bound for the transition product violating (13) at a single finite window would exclude that putative input, with no limiting or uniform-amplitude hypothesis.
The decreasing norm lower bound (12) alone does not certify such a violation.

Since \(k_N/N\to1/\ell_0\), (13) also implies, when \(\ell_0\mathcal C(m)<\log2\),
\[
 \limsup_{N\to\infty} C(\theta_N,J_N)
 \leq \min\left\{1,\,
       \frac{g^{-1}(\ell_0\mathcal C(m))}{A_*}\right\}.
 \tag{14}
\]
Here \(g^{-1}\) is the increasing inverse on \([0,\log2]\).
If \(\ell_0\mathcal C(m)\geq\log2\), this argument supplies only the elementary bound by one.
The constants retain the actual contraction rates of \(P\); no degree-free efficacy of (13) or nontriviality of (14) is asserted.

The reduction is therefore precise.
Center shrinkage, polynomial height, logarithmic hyperbolic transients, noise preservation, and linearly many effective mixed frequencies are all achieved.
What remains is stronger information on the actual transition cosine product or on L G0120's summed actual-amplitude budget.
Neither the fixed-forcing scattering lower bound nor smallness of the central conjugates alone supplies that information.
No rounding cube, bilateral decaying defect, stationary central lift, or uniform Mahler gap is asserted.
