---
author: Yin
---

# Cyclotomic central-minus-two perturbations: small real roots and the remaining total measure

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The external_structural_lead delegate developed the candidate, endpoint calculation, cyclotomic exclusion and numerical probe.
The coordinating main agent identified the applicable dyadic scalar-congruence test and the need to charge only actual positive-factor degrees; the delegate supplied the complete no-cyclotomic-factor argument and the resulting all-root bound.
These are author-development contributions and ordinary checks, without independent review, a new Claim assessment or a counterexample to the Task.

<a id="cyclotomic-central-minus-two-scope"></a>
## Candidate, reuse and outcome

For an odd squarefree integer n having at least two distinct prime factors, consider
\[
 D=\varphi(n)=2d,\qquad P_n(z)=\Phi_n(z)-2z^d.
 \tag{1}
\]
The proposed varying-input construction allows the number of prime factors to grow, changing the cyclotomic block rather than substituting into one fixed seed.
The finite controls n=15,105,1155 have respectively 7,33,343 nonzero coefficients after the central subtraction.
No claim that these finite support counts classify the whole family is needed.

[C414's central-shift criterion](../claims/Yin_C_G0414_v1.md#real-trace-shift-criterion) already owns the general perturbation mechanism and its warning that nonreal trace roots must be charged.
The present calculation applies that viewpoint to a specified cyclotomic family, proving its small exterior real-root bounds, excluding all cyclotomic factors and retaining the complete remaining cost.
It is not a newly claimed perturbation method.
[L450's fixed-seed obstruction](Yin_L_G0450_v1.md#unit-ray-saturation) does not itself classify these changing cyclotomic inputs.
[L133 v2's separated-delay result](Yin_L_G0133_v2.md#cyclotomic-boundary-log-gap) retains its actual delay hypothesis and is not applied to the central specialization (1).
[L454's arithmetic-realization comparison](Yin_L_G0454_v1.md#arithmetic-realization-scope) supplies the nearby distinction between limiting root distribution and total measure; no realization theorem from that account is a premise below.

The construction gives positive measure and two exterior real roots whose logarithmic contributions become small as J_2(n) grows.
However, other exterior roots have the explicit lower cost (10) below, and the three finite numerical totals increased.
Neither the lower bound nor those observations exclude positive total measures tending to zero throughout the entire parameter domain.
This attempt supplies no such sequence and no Salem reduction of the unrestricted Task.

<a id="actual-trace-and-endpoint-roots"></a>
## Actual integer input and the two exterior real roots

The integer D is divisible by four, so d is even.
The reciprocal cyclotomic polynomial has the unique monic integral trace expression
\[
 \Phi_n(z)=z^d\Psi_n(z+z^{-1}),\qquad \deg\Psi_n=d.
 \tag{2}
\]
For completeness, integrality follows by expressing each symmetric Laurent pair z^k+z^{-k} through the recurrence C_0=2, C_1=y, C_{k+1}=yC_k-C_{k-1} and collecting the reciprocal coefficients.
The d distinct roots of Psi_n are the inverse-pair traces of primitive nth roots of unity, all strictly between -2 and 2.
Denote them by beta_1,...,beta_d.
The elementary cyclotomic evaluation gives Phi_n(1)=1 because n is not a prime power.
Also Phi_n(-1)=Phi_(2n)(1)=1, since n is odd and 2n is not a prime power.
These evaluations follow directly from the cyclotomic product formula at one; the prime contributions cancel when there are at least two distinct prime factors.
Since d is even, (2) gives
\[
 \Psi_n(2)=\Psi_n(-2)=1,\qquad
 P_n(z)=z^d(\Psi_n(z+z^{-1})-2).
 \tag{3}
\]
Thus P_n is a monic reciprocal integer polynomial with constant coefficient one and P_n(1)=-1.
It is not assumed irreducible.

For y>2 every factor y-beta_i is positive and increasing, so Psi_n is strictly increasing from one to infinity.
For y<-2 the even number of negative factors gives a positive product, strictly decreasing from infinity to one as y increases.
Consequently Psi_n(y)=2 has exactly one solution above 2 and exactly one below -2.
These give exactly one positive exterior real root e^(t_+) and exactly one negative exterior real root -e^(t_-) of P_n, with t_+,t_->0, and their contracting reciprocals.
Any other exterior roots are nonreal.
In particular m(P_n)>0, where m always means total logarithmic Mahler measure with every root and multiplicity retained.

<a id="jordan-endpoint-bound"></a>
## Exact endpoint derivative and real-root cost

Put
\[
 J_2(n)=n^2\prod_{p\mid n}(1-p^{-2}).
\]
The cyclotomic product formula is
\[
 \Phi_n(z)=\prod_{r\mid n}(z^r-1)^{\mu(n/r)}.
\]
For positive t tending to zero, use
\[
 \log(e^{rt}-1)=\log r+\log t+\frac{rt}{2}
                 +\frac{r^2t^2}{24}+O(t^4).
\]
The divisor sums of mu, mu times r and mu times r squared are respectively zero, phi(n) and J_2(n); the constant sum is log Phi_n(1)=0.
Hence
\[
 \log\bigl(e^{-dt}\Phi_n(e^t)\bigr)
   =\frac{J_2(n)}{24}t^2+O(t^4).
\]
By (2), its left side is log Psi_n(2 cosh t), proving
\[
 \Psi_n'(2)=\frac{J_2(n)}{24}.
 \tag{4}
\]
Applying the same expansion to Phi_n(-z)=Phi_(2n)(z), using J_2(2n)=3J_2(n) and the evenness of d, gives
\[
 -\Psi_n'(-2)=\frac{J_2(n)}8.
 \tag{5}
\]

All coefficients of the expansion
\[
 \Psi_n(2+\delta)=\prod_i(2-\beta_i+\delta)
\]
are positive, with constant coefficient one.
If its value is two at delta_+>0, then (4) yields delta_+<=24/J_2(n).
Because delta_+=2(cosh t_+-1)>=t_+^2, this gives
\[
 0<t_+\le\sqrt{24/J_2(n)}.
 \tag{6}
\]
The same argument applied to the positive product Psi_n(-2-delta)=product_i(2+beta_i+delta), with (5), gives
\[
 0<t_-\le\sqrt{8/J_2(n)}.
 \tag{7}
\]
Thus both real exterior contributions are small; (6)--(7) are not upper bounds on m(P_n).

<a id="no-cyclotomic-factors"></a>
## All factors have positive measure

No P_n in (1) has a cyclotomic factor.
Indeed, modulo two one has bar P_n=bar Phi_n, which is squarefree because n is odd.
Suppose Phi_k divides P_n over Z and write k=2^a m with m odd.
The reduction of Phi_k has the same distinct roots as bar Phi_m, all of exact multiplicative order m in characteristic two.
For a=0 its multiplicity is one; for a>=1 the reduction is bar Phi_m raised to the power 2^(a-1).
These statements follow modulo two from Phi_(2m)(z)=(-1)^phi(m) Phi_m(-z) for odd m and Phi_(2^a m)(z)=Phi_(2m)(z^(2^(a-1))) for a>=1.
Since it divides the squarefree bar Phi_n, equality of the root orders forces m=n and the multiplicity forces a<=1.

If k=n, divisibility is impossible because P_n-Phi_n=-2z^d and Phi_n has no zero root.
If k=2n, the monic divisor Phi_(2n) has the same degree as P_n, so P_n=Phi_(2n)=Phi_n(-z).
But Phi_n(z)-Phi_n(-z) has only odd powers of z, whereas 2z^d has even exponent d.
This contradiction proves the exclusion.

Every monic irreducible factor of P_n has constant coefficient 1 or -1 because their integer constant coefficients multiply to one.
All are algebraic-unit polynomials.
By the accepted [Kronecker normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), a monic irreducible integer unit polynomial of zero measure is cyclotomic.
Therefore all irreducible factors here have positive measure, and their degrees, counted with multiplicity, sum to the entire D.
No unsupported assertion of irreducibility is needed for this conclusion.

<a id="complete-exterior-root-cost"></a>
## The complete dyadic and nonreal exterior costs

Since bar P_n=bar Phi_n divides z^n-1 modulo two, lifting the quotient gives
\[
 z^n-1=P_n(z)H(z)+2B(z),\qquad H,B\in\mathbb Z[z].
 \tag{8}
\]
For every root alpha of an actual irreducible factor f, evaluation gives alpha^n congruent to one modulo 2 Z[alpha].
The factor is a nontorsion unit by the preceding section.
[C244's exact dyadic certificate](../claims/Yin_C_G0244_v1.md#dyadic-log-five-norm-certificate) therefore gives
\[
 m(f)\ge\frac{\deg f}{n}\frac{\log5}{4}.
\]
Adding over every irreducible factor with its multiplicity gives the full measure bound
\[
 m(P_n)\ge\frac{\varphi(n)}n\frac{\log5}{4}.
 \tag{9}
\]
C244 retains its actual order, original-embedding and SELF-review scope; no powered-degree preservation or maximal-order hypothesis is added.
The no-cyclotomic-factor proof is what permits using the full degree in (9).

There are exactly the two exterior real roots already counted.
Subtracting their upper contributions (6)--(7) from the full lower bound (9) yields
\[
 \sum_{\substack{P_n(\alpha)=0,\ |\alpha|>1\\\alpha\notin\mathbb R}}
       \log|\alpha|
 \ge \frac{\varphi(n)}n\frac{\log5}{4}
       -\frac{\sqrt{24}+\sqrt8}{\sqrt{J_2(n)}}.
 \tag{10}
\]
The sum retains multiplicities.
For n=105, D=48 and J_2(n)=9216, the right side is positive, approximately 0.10344.
For n=1155, D=480 and J_2(n)=1105920, it is also positive, approximately 0.15987.
The exact expression (10), rather than those rounded values, is the proved bound.
Thus these inputs necessarily have nonreal exterior roots and cannot be Salem polynomials times cyclotomic factors.

The ratio phi(n)/n may tend to zero as the number of distinct prime factors grows.
Consequently (9)--(10) do not exclude all positive-to-zero sequences in this construction.
They show that the rapid real-endpoint gain cannot stand in for a total-measure estimate.

<a id="finite-central-minus-two-probe"></a>
## Finite numerical comparison and remaining possibility

The native program, exact input generation, parameters, completed factorization scopes and replaceable output are retained in [J138](../computations/programs/Yin_J_G0138/readme.md).
The FFT quadrature and root screens use floating point without interval error bounds or certified root counts.
They are exploratory observations, not premises of (4)--(10) or asymptotic claims.

| n | Degree | Approximate full logarithmic measure | Positive real exterior contribution |
| --- | --- | --- | --- |
| 15 | 8 | 0.64456923 | Approximately 0.32228462 |
| 105 | 48 | Approximately 0.94243 by the finest boundary grid; 0.942436 by the numerical root sum | Approximately 0.04671623 |
| 1155 | 480 | Approximately 1.15160 | At most sqrt(24/1105920), rigorously |

Exact factorization at n=15 gives P_15=(z^4-z^3-1)(z^4+z-1).
The completed SymPy factorization at n=105 returned one irreducible degree-48 factor.
An attempted n=1155 factorization was stopped and establishes no irreducibility fact; the general argument above makes it unnecessary for the degree accounting.
The numerical root screens counted four and sixteen exterior roots at the first two inputs and found full-measure sums close to the boundary estimates.
Those numerical counts are not certified by the analytic argument, which proves only the stated existence and cost of nonreal exterior roots.

The finite totals increased while the positive real contribution decreased.
This is a useful failure of the endpoint-only heuristic, not a proof that the whole family is bounded away from zero.
Further use of this construction would require a mechanism that suppresses the nonreal exterior cost or a valid estimate showing its complete sum tends to zero.
Extending the same numerical primorial scan alone supplies neither mechanism nor counterexample.
