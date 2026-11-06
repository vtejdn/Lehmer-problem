---
author: Yin
---

# High-frequency cyclotomic denominators and primitive polarization costs

Date: 2026-11-05.
Prepared for Yin under the [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The witt_moment_compatibility delegate developed the high-frequency denominator estimate and its finite and adaptive consequences.
The three_block delegate developed the central polarization, its complete measure identity and controls, the comparison with the old two-block mechanism, and the universal central split.
The coordinating agent checked these deductions on the author side, and the witt_moment_compatibility delegate checked the supplied polarization and central-split arguments while preparing this version.
These are ordinary author development checks, not an independent review or a new Claim assessment.

<a id="original-cost-tests-scope"></a>
## Original-input question and retained interfaces

For an actual original reciprocal integer polynomial P, can a complete cyclotomic denominator or an integer two-variable construction have its full analytic cost bounded by a degree-independent constant times the total measure \(m(P)\)?
[L133 v6](Yin_L_G0133_v6.md#cyclotomic-denominator-minimal-cost) already proves that the exact minimum nonnegative Poisson expense for \(P/A\) at threshold two is
\[
 E_A(P)=\int_{\mathbb T}\bigl(\log|P/A|-\log2\bigr)_+.
 \tag{1}
\]
Its [all-denominator floor](Yin_L_G0133_v6.md#all-cyclotomic-denominators-cost-floor) is a lower bound and does not supply the missing upper comparison with \(m(P)\).
The present version tests one adaptive denominator mechanism and two explicit original-input lifts.
It continues that same cost question, while versions v1--v6 remain fixed.
The earlier [decimation, rotation norms and exact descent](Yin_L_G0133_v5.md#integral-rescaling-scope) are not rederived here.

All circle and torus integrals use normalized Haar probability measure.
Write \(a_+=\max(a,0)\), \(\log^+t=(\log t)_+\) and \(\log^-t=(-\log t)_+\).
Every one-variable boundary logarithm below uses its integrable finite-root value, with values at the finitely many zeros or poles assigned arbitrarily.
Total polynomial measure is never divided by degree.

The [C868 v2 statement](../claims/Yin_C_G0868_v2.md#statement) and its [selected assessment](../claims/Yin_C_G0868_v2.md#decision-whole-general-block-review-2026-11-05) supply only the already adopted general three-block interface where it is explicitly used.
Its constant is \(\gamma=(\sqrt5-2)^2/50\).
No part of this version depends on a later C868 version.
The existing [Jensen and measure conventions](../audits/literature/Den09/Yin_U001.md#mahler-measure), [fixed-polynomial Lawton interface, Theorem 14 and Example 15](../audits/literature/Den09/Yin_U002.md#den09-u002), and [Smyth nonreciprocal bound](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number) are reused at their actual recorded inspection scope.
In particular, the original Lawton and Smyth proofs are not newly audited here.
[L133 v2](Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap) already contains the complete fixed-pair nonreciprocal-specialization mechanism used for comparison below.
There is no new external-source acquisition or priority claim.

<a id="high-frequency-denominator-domain"></a>
## A complete high-frequency cyclotomic block

Let \(P\in\mathbb Z[z]\) be monic with \(P(0)=1\), and put \(D=\deg P\).
Let \(A_0\) be a monic cyclotomic product with constant coefficient one, put \(D_0=\deg A_0\), and set
\[
 u(\theta)=\log|P(e^{i\theta})/A_0(e^{i\theta})|,
 \qquad K=D+D_0,\qquad c=\log2.
 \tag{2}
\]
Then \(u\in L^1(\mathbb T)\) and \(\int u=m(P)\).
The estimate in this section does not require reciprocity, but it preserves the original reciprocal domain when that domain is imposed.

Choose any monic cyclotomic product B with constant coefficient one, including \(B=1\), and an integer \(N\ge7\).
Set
\[
 A(z)=A_0(z)B(z^N),\qquad v(\varphi)=\log|B(e^{i\varphi})|.
 \tag{3}
\]
The polynomial A is again a complete monic cyclotomic product with constant coefficient one.
If \(A_0,B\) are reciprocal of even degree, so is A.
The actual denominator degree is \(D_0+N\deg B\), and all root multiplicities are retained.
There is no restriction on \(\deg B\), its multiplicities, or its dependence on N.
The quotient \(P/A\) is holomorphic in the open disk and has integer Taylor coefficients and constant coefficient one, as in v6.
Also \(v\in L^1(\mathbb T)\) and \(\int v=0\).

With \(h=2\pi/N\), define
\[
 \begin{aligned}
 I&=E_{A_0B(z^N)}(P)
     =\int_{\mathbb T}(u(\theta)-c-v(N\theta))_+\,d\mu(\theta),\\
 I_t&=\int_{\mathbb T}(u(\theta-t)-c-v(N\theta))_+\,d\mu(\theta),
       \qquad 0\le t\le h,\\
 J(u,B)&=\int_{\mathbb T}\int_{\mathbb T}
                (u(\theta)-c-v(\varphi))_+\,d\mu(\varphi)\,d\mu(\theta).
 \end{aligned}
 \tag{4}
\]
All these integrals are finite because the positive part is bounded by \(|u|+|v|+c\), and the map \(\theta\mapsto N\theta\) preserves normalized Haar measure.
Changing variables from \(\theta\) to \(\theta-t\) in \(I_t\), and then averaging \(Nt\) through one full circle, gives the exact identity
\[
 \frac1h\int_0^h I_t\,dt=J(u,B).
 \tag{5}
\]
This is a deterministic translation identity for the actual input, not an independence assumption about \(u(\theta)\) and \(v(N\theta)\).
The integrability just stated justifies all changes of variables and uses of Fubini.

Since the positive-part function is one-Lipschitz,
\[
 |I-J(u,B)|
 \le\frac1h\int_0^h
          \|u(\,\cdot-t)-u\|_1\,dt.
 \tag{6}
\]
Convexity in v and \(\int v=0\) give
\[
 J(u,B)\ge\int_{\mathbb T}(u-c)_+=E_{A_0}(P).
 \tag{7}
\]
The remaining estimate must retain the actual roots of P and \(A_0\), rather than assume smooth boundary data.

<a id="root-log-translation-estimate"></a>
## Translation cost for every original root

For \(0\le q\le1\), let
\[
 V_q(\theta)=\log|1-qe^{i\theta}|.
\]
For \(q<1\), its convergent Fourier expansion is
\[
 V_q(\theta)=-\sum_{n\ge1}\frac{q^n}{n}\cos(n\theta).
 \tag{8}
\]
The same expansion holds in \(L^2\) at \(q=1\).
Indeed, the coefficient sequences converge in square sum as \(q\uparrow1\), since \(\sum n^{-2}<\infty\).
Thus (8) has an \(L^2\), hence \(L^1\), limit.
The radial \(L^1\) convergence for a circle-root logarithm proved in [v6](Yin_L_G0133_v6.md#cyclotomic-denominator-minimal-cost) identifies this limit with the actual function \(\log|1-e^{i\theta}|\).
This uses a single finite-root logarithm, not boundary convergence of a formal infinite Euler product.

Parseval now gives, including \(q=1\),
\[
 \|V_q(\,\cdot-t)-V_q\|_2^2
   =\sum_{n\ge1}\frac{q^{2n}(1-\cos nt)}{n^2}
   \le3t,\qquad 0<t\le1.
 \tag{9}
\]
To check the constant, put \(M=\lceil1/t\rceil\).
For \(n\le M\), use \(1-\cos nt\le n^2t^2/2\), so that this part is at most \(Mt^2/2\le t\).
For \(n>M\), use \(1-\cos nt\le2\), giving at most \(2\sum_{n>M}n^{-2}\le2/M\le2t\).
Since Haar measure is a probability measure, (9) also gives
\[
 \|V_q(\,\cdot-t)-V_q\|_1\le\sqrt{3t}.
 \tag{10}
\]

Write all roots of P as \(\alpha_1,\ldots,\alpha_D\), and all roots of \(A_0\) as \(\beta_1,\ldots,\beta_{D_0}\), with multiplicity.
There are no zero roots.
Set \(q_i=\min(|\alpha_i|,|\alpha_i|^{-1})\), \(\theta_i=\arg\alpha_i\), and \(\psi_j=\arg\beta_j\).
The exact rootwise decomposition is
\[
 u(\theta)
   =m(P)+\sum_{i=1}^D V_{q_i}(\theta-\theta_i)
             -\sum_{j=1}^{D_0}V_1(\theta-\psi_j).
 \tag{11}
\]
For an outside root, the extracted constant is \(\log|\alpha_i|\); for an inside or circle root, it is zero.
Their sum is exactly \(m(P)\) by Jensen's formula.
Thus no original root, radial factor or circle singularity has been discarded.

The constant in (11) disappears under translation, so the triangle inequality and (10) yield
\[
 \|u(\,\cdot-t)-u\|_1\le K\sqrt{3t},\qquad 0<t\le1.
 \tag{12}
\]
Because \(N\ge7\) implies \(h\le1\), integration of (12) in (6) proves
\[
 |E_{A_0B(z^N)}(P)-J(u,B)|
 \le\delta_N,\qquad
 \delta_N=\frac{2K}{3}\sqrt{\frac{6\pi}{N}}.
 \tag{13}
\]
The error is independent of the degree and multiplicities of the newly added B because only the original u is translated.
The integrability of the entire B block remains part of the proof.

<a id="high-frequency-variational-bound"></a>
## Variational consequence, finite exclusion and multiple steps

Combining (7) and (13) gives the complete-cost estimate
\[
 E_{A_0B(z^N)}(P)\ge E_{A_0}(P)-\delta_N.
 \tag{14}
\]
In general \(J(u,B)\) can exceed \(E_{A_0}(P)\), so (13) does not assert an upper estimate by the old cost plus \(\delta_N\).
Allowing \(B=1\) does give the exact variational sandwich
\[
 \max\{0,E_{A_0}(P)-\delta_N\}
 \le\inf_B E_{A_0B(z^N)}(P)
 \le E_{A_0}(P).
 \tag{15}
\]
The infimum may be over all B in (3), or over their reciprocal even-degree subdomain when that is the selected original domain.
For each fixed P and \(A_0\),
\[
 \lim_{N\to\infty}\inf_B E_{A_0B(z^N)}(P)=E_{A_0}(P).
 \tag{16}
\]
For every adaptive choice \(B=B_N\), with unbounded degree or multiplicity allowed, the uniform lower estimate gives
\[
 \liminf_{N\to\infty} E_{A_0B_N(z^N)}(P)\ge E_{A_0}(P).
\]
No upper-limit equality is asserted for a selected sequence; (16) is the limit of the infima.
It rules out a substantial reduction of this fixed original cost by adding only a sufficiently high-frequency complete block.

There is also a finite certificate.
For \(0\le\eta<E_{A_0}(P)\), if
\[
 N\ge7,\qquad
 N>\frac{8\pi K^2}{3(E_{A_0}(P)-\eta)^2},
 \tag{17}
\]
then every allowed B satisfies \(E_{A_0B(z^N)}(P)>\eta\).
In particular, on an actual input where \(C\ge0\) and \(E_{A_0}(P)>C\,m(P)\), (17) with \(\eta=C\,m(P)\) excludes this denominator mechanism as a way to reach that target expense.
This conditional test does not assume the existence of a sequence of positive original measures tending to zero.

For finitely many adaptive steps
\[
 A_j(z)=A_{j-1}(z)B_j(z^{N_j}),\qquad N_j\ge7,\quad 1\le j\le r,
\]
successive application of (14) gives
\[
 E_{A_r}(P)\ge E_{A_0}(P)
   -\frac23\sqrt{6\pi}
      \sum_{j=1}^r\frac{D+\deg A_{j-1}}{\sqrt{N_j}}.
 \tag{18}
\]
Here \(\deg A_j=\deg A_{j-1}+N_j\deg B_j\) is the actual cumulative denominator degree.
Replacing the numerator in every summand by the initial K would remove a real cost.
No infinite-product convergence is asserted.

Equations (15)--(18) concern high-frequency additions relative to the current original root population.
They do not determine the unrestricted infimum over all cyclotomic denominators, exclude same-scale choices, or provide a degree-independent upper bound by \(m(P)\).
They also do not require a common power dilation of P.

<a id="primitive-central-polarization"></a>
## Primitive central polarization and its complete cost

Now let P be a nonconstant monic reciprocal integer polynomial of degree \(2d\ge2\), with \(P(0)=1\).
Define
\[
 A_0=P,\qquad B_0=P^2+x^{2d},\qquad p=x^{-d}P.
 \tag{19}
\]
The actual degrees of \(A_0,B_0\) are \(2d,4d\).
Both are monic reciprocal integer polynomials with constant coefficient one.
Moreover,
\[
 \gcd(A_0,B_0)=\gcd(P,x^{2d})=1.
 \tag{20}
\]
Thus the coefficient blocks are primitive in the sense of having monic gcd one.
This does not say that their two-variable lift is irreducible.

The balanced blocks are \(A=p\) and \(B=p^2+1\), so
\[
 F(x,y)=p(y+y^{-1})-(p^2+1)
       =y^{-1}(py-1)(y-p).
 \tag{21}
\]
The sign in this factorization is positive.
Reciprocity makes p real on the circle, while \(|p|=|P|\) there.
For each fixed circle x, both linear factors in (21) have y-circle logarithmic mean \(\log\max(1,|p|)\).

Here the absolute integrability needed for Fubini can be checked directly.
For \(0\le r\le1\), the normalized linear factor \(1-re^{it}\) has logarithmic mean zero and positive part at most \(\log2\).
Its logarithm therefore has \(L^1\) norm at most \(2\log2\), including \(r=1\).
Factoring out \(\max(1,|p|)\) from either linear factor shows that its absolute logarithmic integral is at most \(\log^+|p|+2\log2\).
Since p is continuous and bounded on the circle, this is an integrable uniform bound.
Consequently (21), including its circle-zero fibers, gives
\[
 \begin{aligned}
 \tau(P):=m_2(F)
   &=2\int_{\mathbb T}\log^+|P|\\
   &=m(P)+\|\log|P|\|_1\\
   &=2m(P)+2\int_{\mathbb T}\log^-|P|.
 \end{aligned}
 \tag{22}
\]
The last term is the exact expense beyond \(2m(P)\), not a discarded boundary error.

As a cross-check, the [C868 v2 general Jensen formula](../claims/Yin_C_G0868_v2.md#general-quadratic-cost) gives \(\tau=m(A_0)+\int\phi(B/A)\).
Away from the finite zero set of p, \(B/A=p+p^{-1}\), and for real nonzero p one has \(\phi(p+p^{-1})=|\log|p||\).
This agrees with (22) and retains the denominator's original measure \(m(A_0)=m(P)\).

<a id="polarization-controls"></a>
## Zero and positive controls for the polarization expense

For every integer \(h\ge1\), take
\[
 P_h=1+x^{2h}.
\]
Then \(m(P_h)=0\), but (19) gives the coprime blocks
\[
 A_0=1+x^{2h},\qquad B_0=1+3x^{2h}+x^{4h}.
\]
Haar invariance under \(x\mapsto x^{2h}\) and linear Jensen give
\[
 \tau(P_h)=2\int_{\mathbb T}\log^+|1+x|
          =2m_2(1+x+y)>0.
 \tag{23}
\]
For an explicit lower bound, \(|P_h(e^{i\theta})|=2|\cos(h\theta)|\) is at least \(\sqrt3\) on a set of normalized measure \(1/3\).
Therefore
\[
 \tau(P_h)\ge\frac{\log3}{3}.
 \tag{24}
\]
This shows that the lift does not preserve a zero original measure; it is not a positive-measure sequence approaching zero.

There is also a fixed-positive-measure control.
Let
\[
 Q=x^2-3x+1,\qquad
 P_n=Q(1+x^2)^n,\qquad n\ge1.
 \tag{25}
\]
These are actual monic reciprocal integer inputs with constant coefficient one and degree \(2(n+1)\), and
\[
 m(P_n)=\log\frac{3+\sqrt5}{2}>0
\]
is independent of n.
On the circle, \(|Q|=3-2\cos\theta\ge1\).
On the set \(|\cos\theta|\ge\sqrt3/2\), of measure \(1/3\), one also has \(|1+x^2|\ge\sqrt3\).
Equation (22) gives
\[
 \tau(P_n)\ge\frac{n\log3}{3}\longrightarrow\infty.
 \tag{26}
\]
Hence no finite universal C can satisfy \(\tau(P)\le C\,m(P)\) for this specific lift on all positive-measure original inputs.
These \(P_n\) are reducible and contain removable cyclotomic content.
They do not exclude a construction that first removes that content, or a different cost comparison restricted to irreducible noncyclotomic P.

Conversely, the certified subdomain \(|P|\ge1\) everywhere on the circle has
\[
 \tau(P)=2m(P).
 \tag{27}
\]
For example, for \(h\ge1\) and integer \(k\ge3\),
\[
 P=x^{2h}-kx^h+1,\qquad
 |P(e^{i\theta})|=k-2\cos(h\theta)\ge1,\qquad
 m(P)=\log\frac{k+\sqrt{k^2-4}}2.
\]
The adopted coprime-block result of C868 v2 applies to (19), but its \(\gamma/2\) consequence for this subdomain supplies no new coverage beyond the stronger old mechanism below.

<a id="polarization-old-two-block-floor"></a>
## The old nonreciprocal mechanism already supplies the lift's floor

Let P now be any fixed nonconstant monic integer polynomial with \(P(0)=1\), and put \(D=\deg P\).
For every integer \(L>D\), set
\[
 Q_L=x^LP-1,\qquad Q_L^*=P^*-x^{L+D}.
 \tag{28}
\]
The polynomial \(Q_L\) is monic of degree \(L+D\) and constant coefficient minus one.
If it were reciprocal up to sign, the leading and constant coefficients would force \(Q_L^*=-Q_L\), hence
\[
 P^*-1=x^L(x^D-P).
 \tag{29}
\]
The left side has degree at most D, and every potentially nonzero term on the right has degree at least \(L>D\).
Both sides would have to vanish, forcing \(P^*=1\), impossible for this nonconstant P with \(P(0)=1\).
Thus \(Q_L\) is nonreciprocal.

In its monic integer irreducible factorization, every factor has constant coefficient in \(\{1,-1\}\).
If every factor were reciprocal up to its constant sign, their product would be reciprocal up to sign.
At least one factor is therefore the minimal polynomial of a nonzero nonreciprocal algebraic integer.
The retained Smyth interface gives
\[
 m(Q_L)\ge\log\theta_0,\qquad
 \theta_0>1,\quad \theta_0^3-\theta_0-1=0.
 \tag{30}
\]
All other monic integer factors contribute nonnegative measure.

For this fixed P, apply the retained full Lawton theorem to \(yP(x)-1\).
The least sup norm of a nonzero integer relation on \((1,L)\) is L, so
\[
 m(Q_L)\longrightarrow m_2(yP-1)
                      =\int_{\mathbb T}\log^+|P|.
 \tag{31}
\]
The linear Jensen identity and its integrability are the same ones used in (22).
Combining (30)--(31), the primitive polarization in (19) satisfies
\[
 \tau(P)\ge2\log\theta_0.
 \tag{32}
\]
This is a direct reuse of the old nonreciprocal specialization mechanism, not a new external theorem.
There is no convergence-rate claim uniform in moving P.
The lift factors into two such two-block factors, so manufacturing its coprime coefficient blocks does not by itself add original Lehmer coverage.

<a id="universal-central-split-endpoint"></a>
## A universal central split returns the original polynomial at the excluded endpoint

Return to a nonconstant monic reciprocal integer P of degree \(2d\) and constant coefficient one.
For any integer \(K>d\), take
\[
 A_0=1,\qquad
 B_0=1+x^{2K}-x^{K-d}P,\qquad
 F_K=y+y^{-1}-(x^K+x^{-K}-x^{-d}P).
 \tag{33}
\]
Because \(K-d>0\) and \(K+d<2K\), \(B_0\) is monic of actual degree \(2K\), with constant coefficient one.
Reflection about degree K preserves its shifted P block, so \(B_0\) is reciprocal.
These are legitimate even-degree integer blocks and are coprime.

The pair cannot be an exceptional ratio of C868 v2.
Its actual degree rules out \(B_0=1\), and \(B_0=1+x^{2h}\) would require \(h=K\) and then \(x^{K-d}P=0\), which is impossible.
Thus the existing C868 v2 conclusion gives \(m_2(F_K)\ge\gamma\), where \(\gamma=(\sqrt5-2)^2/50\).

Nevertheless, the original input returns exactly as
\[
 x^dF_K(x,x^K)=P.
 \tag{34}
\]
For these blocks, the notation of [C868 v2's finite return](../claims/Yin_C_G0868_v2.md#fixed-pair-and-original-target) is \(a=0\), \(b=K\).
Its preserved-degree assertion requires \(N>\max(0,b-a)=K\).
The exact return (34) uses the excluded endpoint \(N=K\).
Indeed,
\[
 x^{2K}+1-B_0=x^{K-d}P
 \tag{35}
\]
has degree \(K+d<2K\) and a zero root of multiplicity \(K-d\).
Removing that monomial recovers P of degree \(2d\).
The endpoint cancellation, rather than a degree-preserving application of the fixed-pair limit, is responsible for the return.

A zero control keeps this boundary explicit.
For \(P=1+x^{2d}\), every \(K>d\) gives
\[
 B_0=(1-x^{K-d})(1-x^{K+d})
    =1-x^{K-d}-x^{K+d}+x^{2K}.
 \tag{36}
\]
This is a monic reciprocal cyclotomic product of even degree and constant coefficient one.
The four exponents are distinct, so its coefficient square energy is four.
The complete [four-term estimate in C868 v2](../claims/Yin_C_G0868_v2.md#structural-completion) therefore gives
\[
 m_2(F_K)\ge\frac1{256},\qquad m(P)=0
 \tag{37}
\]
for every \(K>d\).
This disproves an unconditional comparison \(m_2(F_K)\le C\,m(P)\) for this transformation.
It does not disprove an irreducible-only comparison on the positive-measure hard class.

The control differs from the already retained \(\Phi_{10}(x^h)\) finite-delay example in C868 v2.
That example satisfies the strict delay inequality while its blocks vary; (34) instead returns any prescribed P at the endpoint where the actual degree drops.
Neither control is a sequence of positive measures tending to zero.

<a id="original-cost-tests-return"></a>
## Remaining original-input boundary

The high-frequency estimate retains a genuine finite obstruction for a specified denominator mechanism, with its original root count and every cumulative degree cost.
The polarization retains an exact original-input expense and both zero and fixed-positive controls, while its positive floor is already explained by the accepted Smyth and fixed-Lawton interfaces.
The universal central split retains an exact return and the precise failed delay threshold.

None supplies the still-missing degree-independent upper estimate by \(m(P)\) for an arbitrary original irreducible reciprocal noncyclotomic input.
The unrestricted infimum of (1), and any different construction proposed to realize that comparison, remain outside the proved scope.
These deductions neither complete G0001 nor reopen the already settled three-block vanishing question in place of the original task.
