---
author: Yin
---

# Quantitative concentration cost behind strict binary entropy loss

The current complete mathematical proof is retained in [C293](../claims/Yin_C_G0293_v1.md#argument).
The original mathematical text below remains the fixed old input, with its original date and old review bindings.
The existing [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-strictness-reread-2026-10-07) owns the original10/7 source reread at its exact retained depth.

Date: 2026-10-07.
Bounded continuation of G0001 by the assigned AI ms25_source for Yin.
This note reuses the strictness proof of BV20 and the cubic comparison of L G0097.
It supplies explicit packing constants and a concentration-time inequality.
It does not claim a uniform entropy gap or an effective singularity rate from the source.
No numerical computation or new source is used.

<a id="strict-deficit-source-scope"></a>
## Retained source and the missing quantitative step

The retained [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-u001) audits arXiv:1510.04043v4, 23 April 2021.
For this continuation, the assigned agent reread and visually inspected the retained PDF's printed/PDF pages 19--21: Proposition 17, Lemma 18, and their complete proofs.
All source logarithms are base 2; all logarithms below are natural.
The fair-sign and fair-bit laws have identical fibers by an injective affine change.

The accepted strictness statement, with the retained zero correction, is

\[
 \alpha\ne0,\quad M(P)<2,\quad
 P\text{ has no unit-circle root}
 \quad\Longrightarrow\quad h_1(\alpha)<m=\log M(P).       \tag{1}
\]

In this range \(\alpha\) is an algebraic unit.
The proof first obtains a positive nondecaying Fourier product, then uses the retained pure-type interface to infer singularity of the stable self-affine law.
A compact set carrying nearly all mass can consequently have arbitrarily small volume.
The last step waits until its shrinking anisotropic neighborhood is sufficiently small.
The source does not bound this waiting time in terms of degree, measure, or its Fourier product.
Its final entropy gain is a fixed positive amount divided by that input-dependent time.

The complete original proof was inspected only at the scope just specified, retaining the existing pure-type interface; no original proof of that external pure-type theorem is newly audited here.
Unit-circle conjugates are excluded throughout the strictness and concentration arguments below.

<a id="explicit-stable-packing-deficit"></a>
## Explicit stable packing and a finite deficit

Let \(P\) be monic irreducible of degree \(d\), let \(\alpha\) be a unit, and suppose no conjugate has modulus one.
Write the stable embedding space as \(\mathbb R^r\times \mathbb C^c\), with one member of each nonreal conjugate pair and real dimension \(s=r+2c\).
Then \(1\le s<d\).
Use \(\iota\) for this embedding map.
For each stable conjugate \(\beta\), let \(r_\beta=|\beta|<1\), and put

\[
 K_N=\prod_{\beta\ {\rm real,stable}}[-r_\beta^N,r_\beta^N]
       \ \times\!\prod_{\beta\ {\rm complex,stable}}
                         \{z:|z|\le r_\beta^N\},
\]
\[
 V_0=2^r\pi^c,\quad \operatorname{vol}(K_N)=V_0 e^{-mN},
 \quad T=\max_{\beta\ {\rm stable}}\frac1{1-|\beta|},
 \quad a=\left(\prod_{|\beta|>1}(|\beta|-1)\right)^{1/s},
\]
\[
 \gamma=(a/2)^s V_0,\qquad C=(1+2T/a)^s.                 \tag{2}
\]

The expanding product includes both members of each complex pair.
The volume identity uses the unit norm and includes the same multiplicities.
Complex discs make the body exactly invariant under the relevant rotations.
In particular, \(\iota(\alpha)^N K_0=K_N\) under coordinatewise multiplication; no square is incorrectly treated as rotation-invariant.

For independent fair bits \(X_j\), define

\[
 Y_N=\sum_{j<N}X_j\iota(\alpha^j),\qquad
 Y=\sum_{j\ge0}X_j\iota(\alpha^j).
\]

The infinite sum converges absolutely.
Deterministically, \(Y_N\in TK_0\) and \(Y-Y_N\in TK_N\).
Stable projection preserves all algebraic fibers, since each field embedding is injective; thus \(H(Y_N)=H_N\) for the original walk.

Here is an explicit separation bound.
If distinct length-N sums have difference \(x\ne0\), then \(\alpha^{-N}x\) is a nonzero algebraic integer, and for each expanding conjugate,

\[
 |\beta^{-N}x(\beta)|
 \le\sum_{l=1}^{N}|\beta|^{-l}<\frac1{|\beta|-1}.
\]

If \(\iota(x)\in aK_N\), the product of its normalized stable absolute values, with complex multiplicity two, would be at most \(a^s\).
The absolute field norm of \(\alpha^{-N}x\) would then be strictly less than \(a^s\prod_{|\beta|>1}(|\beta|-1)^{-1}=1\), impossible.
Therefore distinct atoms differ by a vector outside \(aK_N\).
Their translates of \((a/2)K_N\) are disjoint, and are contained in \((T+a/2)K_0\).
Comparing volumes gives

\[
 |\operatorname{supp}(Y_N)|\le C e^{mN}.                 \tag{3}
\]

Now let \(A\) be a compact set with \(\mathbb P(Y\in A)\ge1-\varepsilon\), where \(0\le\varepsilon\le1/2\).
Suppose that for some \(N\ge1\) and \(0<u<1\),

\[
 \operatorname{vol}\bigl(A+(T+a/2)K_N\bigr)\le\gamma u.
                                                               \tag{4}
\]

The selected atoms \(\operatorname{supp}(Y_N)\cap(A+TK_N)\) carry mass at least \(1-\varepsilon\).
Their disjoint \((a/2)K_N\) translates lie in the set in (4), so they number at most \(u e^{mN}\).
Let \(p\le\varepsilon\) be the remaining mass.
Conditioning on membership in the selected set and bounding conditional entropy by log cardinality give

\[
 H_N\le Nm+h_{\rm bin}(p)+(1-p)\log u+p\log C,
 \quad h_{\rm bin}(p)=-p\log p-(1-p)\log(1-p).
\]

The expression after \(Nm\) increases for \(0\le p\le\varepsilon\le1/2\), since its derivative is \(\log((1-p)C/(pu))\ge0\).
Empty complementary sets are handled by \(p=0\).
Consequently, with

\[
 \kappa=(1-\varepsilon)\log(1/u)
             -h_{\rm bin}(\varepsilon)-\varepsilon\log C,
\]
\[
 \boxed{\ Nm-H_N\ge\kappa,\qquad
             m-h_1\ge\kappa/N.\ }                       \tag{5}
\]

The second assertion uses subadditivity, \(h_1\le H_N/N\), not a limit of strict finite inequalities.
Formula (5) is useful when \(\kappa>0\).
It displays separately the high-mass error, relative volume, total packing cost, and waiting time.

<a id="strictness-concentration-time-barrier"></a>
## The cubic comparison forces slow concentration

Let \(D(m)\) denote the explicit lower entropy function in [L G0097](Yin_L_G0097_v1.md#cubic-mahler-comparison-error):

\[
 D(m)=\max\left\{g(\sqrt{1-e^{-2m}}),
       F(1-e^{-2m})\right\},\qquad
 F(l)=l/2+l^2(3-2l)^4/324.
\]

For every \(N\), that record proves \(H_N\ge ND(m)\).
Thus every occurrence of (4)--(5) necessarily satisfies

\[
 \boxed{\ \kappa\le N\,[m-D(m)].\ }                    \tag{6}
\]

This statement is valid without dividing by a possibly zero quantity.
If \(\kappa>0\), then the bracket must be positive and \(N\ge\kappa/[m-D(m)]\).
For sufficiently small positive \(m\), the fourth-moment branch is the larger one and

\[
 m-D(m)=\tfrac{20}{3}m^3+O(m^4),\qquad
 N\ge\left(\tfrac3{20}+O(m)\right)\kappa m^{-3}.          \tag{7}
\]

The absolute local Taylor constants and the nonlinear comparison are exactly those of L G0097.
Equation (7) is a necessary scale for a prescribed entropy saving; it does not assert that this scale is attainable.

To make the qualitative singularity argument concrete, set

\[
 u=e^{-4},\qquad
 \varepsilon=\min\{1/4,\,[4(1+\log C)]^{-1}\}.
                                                               \tag{8}
\]

Then \(\kappa\ge3-\log2-1/4>1\).
Under (1), the retained singularity statement supplies a compact Lebesgue-null set \(A\) of mass at least \(1-\varepsilon\), by regularity of the probability law on its compact support.
The compact sets \(A+(T+a/2)K_N\) decrease to \(A\).
They have finite volume, so continuity from above makes (4) eventually true.
This proves existence of a certificate with \(\kappa>1\), but (6)--(7) show that its first possible time is at least order \(m^{-3}\).
The compact set and its required mass also depend on the input through \(C\).

For the no-unit-circle branch, a sufficient new uniform input would be: every sufficiently small positive \(m\) admits (4) with

\[
 \frac{\kappa}{Nm^3}>\frac{20}{3}+\delta                 \tag{9}
\]

for one fixed \(\delta>0\).
This would contradict (6) for all sufficiently small \(m\).
In particular, fixed \(\kappa\ge\kappa_0>0\) and a uniform bound \(N\le C_0m^{-b}\) with \(b<3\) would suffice.
A bound with extra uncontrolled degree dependence does not suffice: the degree is unbounded, and the height \(m/d\) cannot be silently substituted for \(m\).
A bound proportional to \(m^{-3}\) needs its constants compared with (9).
Even a successful proof of this criterion would cover only the branch with no unit-circle conjugate; the full Lehmer problem includes the excluded branch.

<a id="trace-fourier-quantitative-boundary"></a>
## What the trace Fourier product actually controls

The inspected source proof uses fair signs; their infinite stable sum is an affine image of \(Y\), so singularity is equivalent.
Let \(u_j\) be the sum of all stable conjugates of \(\alpha^j\), with both members of each complex pair, and \(v_j\) the sum of all expanding conjugates.
For every integer \(j\), \(u_j+v_j\in\mathbb Z\).
The trace frequencies \(\zeta_t\) of source p.19 satisfy

\[
 |\widehat\mu(\zeta_t)|\ge c(P),\qquad
 c(P)=\prod_{j=-\infty}^{-1}|\cos(2\pi v_j)|
             \prod_{j=0}^{\infty}|\cos(2\pi u_j)|>0.
                                                               \tag{10}
\]

Here \(\|\zeta_t\|\to\infty\).
Each finite factor is nonzero: \(u_j\) is an algebraic integer, whereas a zero of \(\cos(2\pi x)\) requires the nonintegral rational number \(x\in1/4+(1/2)\mathbb Z\).
This uses the retained correction to the source's stated zero set.

There is an explicit tail estimate, but it retains further input dependence.
Put

\[
 \sigma=\max\{\max_{|\beta|<1}|\beta|,
                      \max_{|\beta|>1}|\beta|^{-1}\}<1,
\]

and choose \(J\ge0\) with \(d\sigma^{J+1}\le1/(4\pi)\).
For \(|x|\le1/2\), \(\cos x\ge e^{-x^2}\): integrate \(\tan x\le2x\), which follows from \(\sin x\le x\) and \(\cos x\ge1-x^2/2\).
The positive and negative tails in (10) are bounded using \(|u_j|\le s\sigma^j\) and \(|v_{-j}|\le(d-s)\sigma^j\).
Since \(s^2+(d-s)^2\le d^2\),

\[
 c(P)\ge
 \left(\prod_{j=-J}^{J}|\cos(2\pi u_j)|\right)
 \exp\left[-\frac{4\pi^2d^2\sigma^{2(J+1)}}{1-\sigma^2}\right].
                                                               \tag{11}
\]

For negative indices the finite factors may be expressed using \(u_j\) because the integral trace identifies their cosines with those of \(v_j\).
Formula (11) makes the archimedean separation from the unit circle and the finite cosine factors visible.
The proof establishes their positivity, not an input-uniform lower bound for the finite product.
Nor does (10) or (11) itself estimate the high-mass null set's neighborhood volume in (4).
The source's passage from Fourier nondecay to pure singularity, and then to a compact null set, is qualitative.

Consequently the retained trace construction does not currently discharge (9).
This is a boundary of the checked argument, not a theorem that such a quantitative deduction is impossible.
No new search or additional article was needed: the decisive missing item is a uniform relation between that Fourier information and the specific concentration cost \(\kappa/N\).

## Finite arithmetic interface and actual review

If the fibers of the length-N binary sum have integer sizes \(f_N(x)\), put \(U_N=\prod_x f_N(x)^{f_N(x)}\), as in L G0092.
Then \(H_N=N\log2-2^{-N}\log U_N\).
Given a separately certified rational lower bound \(q_0=a_0/b_0\le M(P)\), where \(a_0,b_0\) are positive integers, the condition

\[
 U_N a_0^{N2^N}>(2b_0)^{N2^N}                            \tag{12}
\]

certifies a positive finite deficit, of size at least \(N\log q_0-H_N\).
This exact integer test does not provide a uniform saving or bound its first time.
It is included only to connect (5) to an actual finite certificate, not as the new quantitative conclusion.

The complete original author/source-reread and coordinator direct-proof checks are retained in [R539](../audits/reviews/Yin_R_G0539_v1.md#complete-original-l100-checking-account).
Their original inputs, date, precision requests and verdicts are unchanged; the finding-specific relationships retain the source-inspection limitation.
