---
author: Yin
---

# A direct quantitative entropy deficit from trace Fourier nondecay

The current complete mathematical proof is retained in [C297](../claims/Yin_C_G0297_v1.md#argument).
The original mathematical text below remains the fixed old input, with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded direct continuation of G0001 by the assigned AI ms25_source for Yin.
This proof replaces the qualitative pure-type and compact-null-set step in the retained BV20 strictness argument by a Gaussian relative-entropy witness.
It reuses the local convex-chord calculation and explicitly controls the nonzero Gaussian cross terms.
No independent scales are assumed.
No new source, computation, or novelty claim is involved.

<a id="trace-fourier-quantitative-deficit"></a>
## Statement and exact scope

Let \(\alpha\) be an algebraic unit, with monic irreducible polynomial \(P\) of degree \(d\), and suppose that \(P\) has no root of modulus one.
Put \(m=\log M(P)>0\).
All logarithms are natural.
The target range is \(M(P)<2\), although the argument below does not require this additional restriction.
Let

\[
 H_N=H\left(\sum_{j=0}^{N-1}\xi_j\alpha^j\right),\qquad
 h_1=\lim_{N\to\infty}H_N/N,
\]

where the \(\xi_j\) are independent fair signs.
The fair-bit version has exactly the same fibers and entropy.

Let \(u_j\) be the sum of the stable conjugates of \(\alpha^j\), including both members of every complex pair, and \(v_j\) the sum of its expanding conjugates.
Define

\[
 c_P=\prod_{j=-\infty}^{-1}|\cos(2\pi v_j)|
                 \prod_{j=0}^{\infty}|\cos(2\pi u_j)|,
 \quad
 \rho=\max_{|\beta|<1}|\beta|,\qquad
 L=\left\lceil\frac{\log4}{-\log\rho}\right\rceil.
                                                               \tag{1}
\]

Here \(0<c_P\le1\), \(0<\rho<1\), and \(L\ge1\).
The Fourier-product positivity is verified below at the same scope as BV20 Lemma 18.
With

\[
 g(x)=\frac{1+x}{2}\log(1+x)+\frac{1-x}{2}\log(1-x),
 \qquad 0\le x\le1,
\]

the conclusion is

\[
 \boxed{\quad m-h_1\ \ge\ \frac{g(c_P)}{L}
                    \ \ge\ \frac{c_P^2}{2L}>0.\quad}      \tag{2}
\]

Thus strictness has an explicit loss per selected scale.
The result has input-dependent Fourier amplitude and spectral spacing, not a degree-independent positive loss over the near-one core.

<a id="trace-frequencies-and-finite-prefixes"></a>
## The stable law and the same witness at every finite prefix

Use the stable embedding space \(\mathbb R^r\times\mathbb C^q \cong\mathbb R^s\), \(s=r+2q\), with one representative of each complex conjugate pair.
Denote its embedding map by \(\iota\), and let \(A\) be the real block diagonal matrix of multiplication by \(\alpha\).
Its complex blocks are ordinary multiplication by the corresponding complex roots; thus \(A\) is normal and \(\|A\|=\rho<1\).
The stable dimension satisfies \(1\le s<d\).

Write
\[
 Y_N=\sum_{j<N}\xi_j\iota(\alpha^j),\qquad
 \zeta_0=(1,\ldots,1,2,0,\ldots,2,0),\qquad
 \zeta_t=A^{-\mathsf Tt}\zeta_0.
\]
The vector \(\zeta_0\) has \(r\) real entries and one \((2,0)\) pair for each complex coordinate.
In particular \(\|\zeta_0\|^2=r+4q\ge1\).
Direct multiplication gives \(\langle\zeta_t,\iota(\alpha^j)\rangle=u_{j-t}\).
Hence

\[
 \widehat{\mu_N}(\zeta_t)
 =\mathbb E e^{2\pi i\langle\zeta_t,Y_N\rangle}
 =\prod_{j=0}^{N-1}\cos(2\pi u_{j-t}),\qquad
 |\widehat{\mu_N}(\zeta_t)|\ge c_P
       \quad(N\ge1,\ t\ge0).                             \tag{3}
\]

The last inequality holds because this finite interval of factors is a subset of the bilateral product in (1), and all omitted absolute factors are at most one.
For negative indices, \(u_j+v_j\) is an integer: it is the trace of the algebraic integer \(\alpha^j\), using that \(\alpha\) is a unit.
Consequently their cosines agree.

Every finite factor is nonzero.
The real number \(u_j\) is an algebraic integer, whereas a zero of \(\cos(2\pi x)\) would require \(x\in1/4+(1/2)\mathbb Z\), a nonintegral rational.
The tails converge to a positive product because \(u_j\) decays exponentially as \(j\to+\infty\), and \(v_j\) does so as \(j\to-\infty\).
For example the explicit tail estimate in [L G0100](Yin_L_G0100_v1.md#trace-fourier-quantitative-boundary) provides a finite positive lower bound.
This uses the actual elementary trace calculation of [BV20-U001](../audits/literature/BV20/Yin_U001.md#bv20-u001), not its pure-type or singularity conclusion.

<a id="gaussian-lacunary-riesz-bound"></a>
## A Gaussian exponential-moment bound with all cross terms retained

Put \(\nu_j=\zeta_{jL}\) for \(j\ge1\).
Since the smallest singular value of \(A^{-\mathsf T L}\) is \(\rho^{-L}\ge4\),

\[
 \|\nu_{j+1}\|\ge4\|\nu_j\|,\qquad \|\nu_j\|\ge4^j.
\]

For any nontrivial sum \(w=\sum_{j=1}^{K}\delta_j\nu_j\), with \(\delta_j\in\{-1,0,1\}\), let \(k\) be its largest nonzero index.
The triangle inequality gives

\[
 \|w\|\ge\|\nu_k\|-\sum_{j<k}\|\nu_j\|
          \ge\tfrac23\|\nu_k\|\ge\tfrac23\,4^k.           \tag{4}
\]

Let \(G\) be the standard Gaussian in \(\mathbb R^s\), and choose arbitrary signs \(\epsilon_1,\ldots,\epsilon_K\).
For any \(t\ge0\), the convex-chord inequality reused from [L G0086](Yin_L_G0086_v1.md) is
\[
 e^{tx}\le\cosh t+x\sinh t,\qquad -1\le x\le1.
\]
Apply it to \(x=\epsilon_j\cos(2\pi\langle\nu_j,G\rangle)\), multiply, and write \(b=\tanh t\in[0,1)\).
The Gaussian expectation of the resulting product is bounded by

\[
 \mathbb E\prod_{j=1}^{K}
       [1+b\epsilon_j\cos(2\pi\langle\nu_j,G\rangle)]
 \le
 1+\sum_{k=1}^{K}
     b(1+b)^{k-1}
       \exp[-(8\pi^2/9)16^k]
 <2.                                                     \tag{5}
\]

Here is the full cross-term count.
Expand each cosine into its two exponential terms.
A nonconstant term with largest selected index \(k\) has frequency as in (4), so its Gaussian expectation has absolute value at most \(\exp[-2\pi^2\|w\|^2]\).
Summing the absolute coefficients of all such terms gives exactly \(b(1+b)^{k-1}\): the last factor is selected, and each earlier one is either omitted or selected.
Phases and the signs \(\epsilon_j\) do not affect this absolute bound.
There is no zero-frequency nonconstant term, by (4).
Since \(8\pi^2/9>1\), the remainder is at most \(\sum_{k\ge1}2^{k-1}e^{-16^k}<1\).
For an explicit elementary estimate, \(16^k\ge2k>k\log4\) makes this sum at most \(\sum_{k\ge1}2^{k-1}4^{-k}=1/2\).
Thus no unproved decorrelation or late-start constant is hidden in (5).

We conclude that, uniformly in \(K\) and these signs,

\[
 \log\mathbb E\exp\left[
       t\sum_{j=1}^{K}\epsilon_j
             \cos(2\pi\langle\nu_j,G\rangle)\right]
       \le K\log\cosh t+\log2.                           \tag{6}
\]

<a id="disjoint-smoothing-relative-entropy"></a>
## Disjoint smoothing converts the Fourier test into a deficit

Use the rotation-invariant stable bodies and constants of [L G0100](Yin_L_G0100_v1.md#explicit-stable-packing-deficit):

\[
 K_N=\prod_{\beta\ {\rm real,stable}}[-|\beta|^N,|\beta|^N]
       \times\!\prod_{\beta\ {\rm complex,stable}}
                              \{z:|z|\le|\beta|^N\},
\]
\[
 V_0=2^r\pi^q,\quad
 T=\max_{|\beta|<1}(1-|\beta|)^{-1},\quad
 a=\left(\prod_{|\beta|>1}(|\beta|-1)\right)^{1/s},
 \quad \gamma=a^sV_0.
                                                               \tag{7}
\]

The expanding product includes both members of complex pairs.
We have \(K_N=A^N K_0\) and \(\operatorname{vol}(aK_N)=\gamma e^{-mN}\).
Distinct fair-bit atoms differ by a vector outside \(aK_N\), as proved by the unit-norm argument in L G0100.
Differences of fair-sign atoms are twice those differences.
Consequently the translates of \(aK_N\) around distinct fair-sign atoms are disjoint.
This factor two is why the noise body here is \(aK_N\), whereas L G0100 packed bit atoms using \((a/2)K_N\).

Let \(U_N\) be uniform on \(aK_N\), independent of \(Y_N\), and let \(Z_N=Y_N+U_N\), with density \(f_N\).
Both laws are symmetric.
Stable projection preserves the algebraic fibers, so the disjoint translates give the exact differential entropy

\[
 h_{\rm diff}(f_N)=H_N+\log\gamma-Nm.                    \tag{8}
\]

Also \(Y_N\in TK_0\) and \(U_N\in aK_0\).
Since \(K_0\) is contained in the Euclidean ball of radius \(\sqrt{s}\), comparison with the standard Gaussian density \(\varphi\) gives

\[
 D(f_N\Vert\varphi)
 =Nm-H_N-\log\gamma+\tfrac{s}{2}\log(2\pi)
                         +\tfrac12\mathbb E\|Z_N\|^2
 \le Nm-H_N+C_P,
\]
\[
 C_P=|\log\gamma|+\tfrac{s}{2}\log(2\pi)
                          +\tfrac{s}{2}(T+a)^2.          \tag{9}
\]

All these quantities are finite: \(f_N\) is piecewise constant on finitely many bounded sets, and the Gaussian density is positive.

Fix \(0<\eta<1\).
Choose an integer \(B_\eta\ge0\) such that
\[
 2\pi a\sqrt{s}\|\zeta_0\|\rho^{B_\eta}\le\sqrt{2\eta}.
                                                               \tag{10}
\]
For \(t\le N-B_\eta\), writing \(U_N=A^N U_0\) shows that the absolute Fourier phase is at most the left side of (10).
Symmetry of \(U_0\) and \(\cos x\ge1-x^2/2\) therefore give
\[
 \widehat{\operatorname{law}(U_N)}(\zeta_t)\ge1-\eta.
\]
Take \(K=\lfloor (N-B_\eta)_+/L\rfloor\).
From (3), each real Fourier coefficient of \(f_N\) at \(\nu_1,\ldots,\nu_K\) has absolute value at least \(b_\eta=(1-\eta)c_P\).
Choose its sign separately as \(\epsilon_j\); these choices can depend on \(N\).
The uniformity in (6) is sufficient, so no consistency of signs across times is required.

The relative-entropy variational inequality is
\[
 D(f\Vert\varphi)\ge\mathbb E_f F
                         -\log\mathbb E_\varphi e^F.
\]
For bounded \(F\) it follows by comparison with the probability density \(e^F\varphi/\mathbb E_\varphi e^F\) and nonnegativity of relative entropy.
Apply it to the test in (6).
This gives, for \(t\ge0\),
\[
 D(f_N\Vert\varphi)
       \ge K[tb_\eta-\log\cosh t]-\log2.
\]
Since \(b_\eta<1\), the choice \(t=\operatorname{atanh}(b_\eta)\) attains \(tb_\eta-\log\cosh t=g(b_\eta)\).
Combining with (9),

\[
 \boxed{\quad Nm-H_N\ge
  \left\lfloor\frac{(N-B_\eta)_+}{L}\right\rfloor
       g((1-\eta)c_P)-C_P-\log2.\quad}                   \tag{11}
\]

This is an explicit finite-time inequality with the boundary cost retained.
For example \(\eta=1/2\) gives gain at least \(c_P^2/8\) per selected scale.
Divide (11) by \(N\) and let \(N\to\infty\), with \(\eta\) fixed.
The additive constants disappear and \(K/N\to1/L\).
Then let \(\eta\downarrow0\).
Continuity of \(g\), including at one, proves (2).
This ordering of limits is explicit; no uniform control of \(B_\eta\) as \(\eta\to0\) is needed.

<a id="fastest-stable-trace-spacing"></a>
## A sharper rate using the fastest stable conjugate

The coordinating agent supplied the following improvement.
Put
\[
 \tau=\min_{|\beta|<1}|\beta|,\qquad
 L_*=\left\lfloor\frac{\log4}{-\log\tau}\right\rfloor+1.
\]
Then \(\tau^{-L_*}>4\).
The exact norm formula is
\[
 \|\zeta_t\|^2=
  \sum_{\beta\ {\rm real,stable}}|\beta|^{-2t}
   +4\sum_{\beta\ {\rm complex,stable}}|\beta|^{-2t}.
\]
Its dominant terms have modulus \(\tau\), so \(\|\zeta_{t+L_*}\|/\|\zeta_t\|\to\tau^{-L_*}>4\).
Choose a finite integer \(t_0\ge0\) after which this ratio is at least four.
Also \(\|\zeta_{t_0}\|\ge1\).

The choice need not remain merely existential.
Let \(A_*\) be the sum of the weights 1 and 4 of the conjugates with modulus \(\tau\), and \(W_*\) the sum of all remaining stable weights.
If \(W_*=0\), take \(t_0=0\).
Otherwise let \(\tau_2>\tau\) be the next distinct stable modulus and \(\kappa_*=\tau^{-2L_*}-16>0\).
Any integer \(t_0\ge0\) satisfying
\[
 16W_*(\tau/\tau_2)^{2t_0}\le A_*\kappa_*                 \tag{11a}
\]
works.
Indeed, after subtracting sixteen times the norm square at time \(t\), the fastest terms contribute \(A_*\kappa_*\tau^{-2t}\); all other negative contributions have total magnitude at most \(16W_*\tau^{-2t}(\tau/\tau_2)^{2t}\).

Use frequencies \(\zeta_{t_0+jL_*}\), \(j\ge1\), in the same proof.
Their norms still exceed \(4^j\); (4)--(6) are unchanged.
In (11) replace the number of scales by \(\lfloor(N-B_\eta-t_0)_+/L_*\rfloor\).
The offset disappears in the rate, giving the further bound
\[
 m-h_1\ge g(c_P)/L_*.                                   \tag{11b}
\]
Both bounds hold.
Let \(L_{\rm eff}=\min(L,L_*)\); then \(m-h_1\ge g(c_P)/L_{\rm eff}\).
The minimum preserves the original no-offset bound when the integer rounding happens to make \(L_*>L\).
The time to reach the fastest-direction regime can be large, but it is explicitly a boundary cost, not a loss in the limiting rate.

<a id="fourier-amplitude-cubic-constraint"></a>
## Comparison with the cubic upper deficit

In the unit application, L G0097 gives
\[
 0\le m-h_1\le m-D(m)
               =\tfrac{20}{3}m^3+O(m^4)
               \quad(m\downarrow0).
\]
Consequently every input in the present no-unit-circle domain satisfies the exact necessary condition

\[
 \boxed{\quad \frac{g(c_P)}{L_{\rm eff}}\le m-D(m),\qquad
              c_P^2\le2L_{\rm eff}[m-D(m)].\quad}        \tag{12}
\]

Along any hypothetical sequence in this domain with \(m\to0\), it follows that
\[
 \frac{c_P^2}{L_{\rm eff}}\le\tfrac{40}{3}m^3+O(m^4).
                                                               \tag{13}
\]
This is an arithmetic restriction on the trace Fourier amplitude and the stable spectral spacing.
Unlike the qualitative compact-set argument, it no longer has an unspecified singular-mass concentration time.

The separately reviewed [endpoint correction](Yin_L_G0101_v1.md#wiener-endpoint-strict-correction) strengthens the exact comparison further.
With \(l=1-e^{-2m}\), \(\gamma_0=(2/3)l^5(1-l)^2\), and \(f(t)=g(\sqrt t)\), \(F(t)=t/2+t^2(3-2t)^4/324\), put
\[
 E(m)=\max\{f(l+\gamma_0),\,F(l)+\gamma_0/2\},
\]
that proof gives \(h_1\ge E(m)>D(m)\), so the right side of (12) may be replaced by \(m-E(m)\).
Its leading cubic asymptotic is unchanged, since \(\gamma_0=O(m^5)\).

It still allows \(c_P\) to become small and \(L_{\rm eff}\) to become large.
Neither is bounded uniformly here.
A uniform lower bound for \(g(c_P)/L_{\rm eff}\), or a lower bound that dominates the cubic expression near zero, would exclude a near-one sequence in this branch.
The finite product and tail estimate retained in L G0100 identify the quantities that such an arithmetic argument must control.
The unit-circle branch, including the Salem case, is excluded.
The next calculation gives a precise failure of this same trace-frequency witness there.

<a id="unit-circle-trace-witness-decay"></a>
## The same trace witness decays on the unit-circle branch

This section is a complementary argument contributed by the coordinating agent.
Suppose \(P\) is irreducible, \(\alpha\) is a nontorsion unit with \(m>0\), and it has \(q_0>0\) unit-circle conjugates \(\beta_1,\ldots,\beta_{q_0}\).
The positive measure and unit norm ensure the presence of both an expanding and a stable conjugate.
Retain the stable and expanding traces \(u_j,v_j\), and put
\[
 w_k=\sum_{i=1}^{q_0}\beta_i^k.
\]
The sum is real, \(|w_k|\le q_0\), and \(w_{-k}=w_k\).
The unit-circle conjugates are distinct, and none is a root of unity, because irreducibility would then make \(\alpha\) a root of unity too.

There is an integer \(k_0\ge0\) with \(|\cos(2\pi w_{k_0})|<1\).
Otherwise \(w_k\in (1/2)\mathbb Z\) for every \(k\ge0\).
These values belong to a finite alphabet, and the sequence satisfies the fixed order-\(q_0\) linear recurrence whose characteristic roots are the \(\beta_i\).
Two of its finitely many length-\(q_0\) blocks must coincide.
Forward recurrence then makes \(w_k\) eventually periodic, say \(w_{k+p}=w_k\) for all \(k\ge a\), with \(p>0\).
Taking \(q_0\) consecutive such equalities and inverting the Vandermonde matrix gives \(\beta_i^a(\beta_i^p-1)=0\) for every \(i\).
This contradicts the preceding non-torsion property.

For completeness, the strict cosine inequality recurs with bounded gaps, without an independence assumption.
Let \(z=(\beta_1,\ldots,\beta_{q_0})\) in the compact torus, and let \(H\) be the closure of \(\{z^k:k\ge0\}\).
This closure is a group.
One direct justification is that a convergent subsequence of powers gives positive differences approaching the identity; either their exponents are unbounded, or one fixed positive power equals the identity.
Thus the inverse of \(z\) is also a limit of nonnegative powers, and closure under multiplication gives the whole group closure.
Nonnegative powers are dense in \(H\).

Choose an open neighborhood \(U\) of \(z^{k_0}\) in \(H\) and \(\varepsilon>0\) such that
\[
 \left|\cos\left(2\pi\sum_i x_i\right)\right|
                    \le1-2\varepsilon\quad(x\in U).
\]
The sum here is real on \(H\), by continuity from the actual orbit.
For every \(x\in H\), the orbit \(xz^n\) is dense in \(H\).
Therefore the sets \(Uz^{-n}\), \(n\ge0\), cover \(H\); a finite subcover supplies an integer \(B\) such that every block of \(B+1\) consecutive nonnegative indices contains a visit to \(U\).

The full trace identity now reads \(u_{-k}+v_{-k}+w_k\in\mathbb Z\).
Since \(v_{-k}\to0\), for all sufficiently late visits to \(U\) we have
\[
 |\cos(2\pi u_{-k})|
   =|\cos(2\pi(v_{-k}+w_k))|\le1-\varepsilon.
\]
All other absolute factors are at most one.
Consequently, for the infinite stable fair-sign law \(\mu\) and these exact trace frequencies,
\[
 |\widehat\mu(\zeta_t)|
 =\prod_{j=-t}^{\infty}|\cos(2\pi u_j)|
 \le C_0 e^{-\eta_0 t}\qquad(t\ge0)                     \tag{14}
\]
for some \(C_0<\infty\), \(\eta_0>0\) depending on the input.
For example the bounded-gap count gives \(\eta_0=-\log(1-\varepsilon)/(B+1)\), after absorbing the initial indices and rounding into \(C_0\).

Thus this particular nondecay witness actually collapses exponentially in the unit-circle branch.
Formula (14) does not establish general Fourier decay, absolute continuity, equality of entropy with Mahler measure, or a Salem entropy theorem.
It rules out transferring the constant-amplitude premise (3) to that branch at the same sequence of trace frequencies.

## Original contribution and actual checks

The complete original author, contributor and separate-agent checking account is retained in [R541](../audits/reviews/Yin_R_G0541_v1.md#complete-original-l102-checking-account).
Its old inputs, date, mathematical scopes and verdicts remain unchanged, with exact finding-specific relationships.
