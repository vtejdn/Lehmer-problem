---
author: Yin
---

# Expected Mahler measure in monic integer coefficient boxes

This material answers the bounded sampling question raised in the current discussion.
It does not select or resume an autonomous Task, and it makes no novelty or uniform Lehmer-gap assertion.
The asymptotic argument below combines an accepted external logarithmic-integrability theorem with explicit Gaussian-limit calculations for this precise integer model.

<a id="statement"></a>
## Statement and conventions

Let d>=1 and N>=1 be integers, and independently sample a_0,...,a_(d-1) uniformly from the integers -N,...,N.
Put
\[
 P_d(z)=z^d+\sum_{j=0}^{d-1}a_jz^j,\qquad
 \sigma_N^2=\mathbb E a_j^2=\frac{N(N+1)}3.
\]
Thus the probability space consists of (2N+1)^d monic integer polynomials; no real-rootedness or irreducibility condition is imposed.
The bound N applies to the non-leading coefficients and is an upper bound, not a requirement that one coefficient attain N.
Use
\[
 M(P)=\exp\!\left(\int_0^{2\pi}\log|P(e^{it})|\,\frac{dt}{2\pi}\right),
 \qquad m(P)=\log M(P),
\]
with all root multiplicities included.

For every d,N in this domain one has
\[
 \frac{N(N+1)+1}{2N+1}
 \le \mathbb E M(P_d)
 \le \sqrt{1+d\sigma_N^2},
\tag{1}
\]
and
\[
 \frac{2\log(N!)}{2N+1}
 \le \mathbb E m(P_d)
 \le \frac12\log(1+d\sigma_N^2).
\tag{2}
\]
Both lower bounds are exact when d=1.
If the non-leading-coefficient model is extended to N=0, it is deterministic: P_d=z^d, M(P_d)=1 and m(P_d)=0.

For each fixed N>=1, as d tends to infinity,
\[
 m(P_d)-\frac12\log(d\sigma_N^2)
 \longrightarrow -\frac\gamma2
 \quad\hbox{in }L^2\hbox{ and in probability},
\tag{3}
\]
where gamma is Euler's constant and convergence is with respect to the coefficient sampling.
Consequently
\[
 \boxed{\mathbb E m(P_d)=\frac12\log(d\sigma_N^2)-\frac\gamma2+o_N(1)},
\tag{4}
\]
and
\[
 \boxed{\mathbb E M(P_d)=e^{-\gamma/2}\sqrt{d\sigma_N^2}\,(1+o_N(1))}.
\tag{5}
\]
In fact M(P_d)/sqrt(d sigma_N^2) converges to exp(-gamma/2) in every finite L^p.
No error estimate uniform in an arbitrarily varying N=N(d) is asserted.

<a id="source-interface"></a>
## Accepted source interface and applicability

NNS13 is Nazarov--Nishry--Sodin, Log-integrability of Rademacher Fourier series, with applications to random analytic functions.
The selected [arXiv v1 original](../literature/pdf/NNS13--arxiv-v1.pdf) is dated 3 January 2013 and has 30 PDF pages.
Printed and PDF p. 3, Section 1.2 and Corollary 1.2, state that for independent Rademacher signs epsilon_j and deterministic complex b_j with sum_j |b_j|^2=1,
\[
 \mathbb E_{\epsilon}\int_0^{2\pi}
 \left|\log\left|\sum_j\epsilon_jb_je^{ijt}\right|\right|^p
 \frac{dt}{2\pi}\le(Cp)^{6p},\qquad p\ge1.
\tag{6}
\]
A finite collection of nonzero coefficients is allowed, with all remaining Fourier coefficients set to zero.
The original's product probability space and normalization include both the independent signs and normalized angular measure.
The selected statement and its application hypotheses were read and visually checked on p. 3; the original proof is accepted as an external theorem and was not re-audited.
The [source notes](../audits/literature/NNS13/readme.md) own the edition and publication correspondence.
Equation (6) is the sole specialized external input to the asymptotic argument.
The elementary characteristic-function calculation below establishes the required single- and two-angle Gaussian limits directly; integer coefficients are not replaced by Gaussian coefficients at the sampling stage.

<a id="argument"></a>
## Complete argument

### Finite bounds and degree one

The root formula gives M(P_d)>=1 and M(P_d)>=|a_0|.
Jensen's inequality on the circle and Parseval's identity give
\[
 M(P_d)\le\left(\int|P_d(e^{it})|^2\frac{dt}{2\pi}\right)^{1/2}
 =\left(1+\sum_{j<d}a_j^2\right)^{1/2}.
\]
Averaging max(1,|a_0|) proves the lower bound in (1), and concavity of the square root proves its upper bound.
Averaging log max(1,|a_0|) and using concavity of the logarithm similarly prove (2).
For d=1, M(z+a_0)=max(1,|a_0|), so these two lower formulas are the exact expectations.
In particular fixed d and N tending to infinity give E M(P_d) of order N, with constants depending on d, and E m(P_d)=log N+O_d(1), directly from (1)-(2) and Stirling's formula.

### Symmetry and uniform logarithmic moments

Fix N and abbreviate sigma_N to sigma.
Let
\[
 S_d=1+\sum_{j<d}a_j^2.
\]
Give the leading coefficient an additional independent sign, forming
\[
 \widetilde P_d(z)=\epsilon_d z^d+\sum_{j<d}a_jz^j.
\]
Conditional on epsilon_d, multiplication by epsilon_d makes the leading coefficient 1 and preserves the joint law of the remaining independent symmetric coefficients.
Hence the entire angular absolute-value function of this signed polynomial, together with S_d, has the same law as that of the original monic polynomial.

Independently write a_j=epsilon_j B_j in distribution, where B_j=|a_j| and the signs are independent Rademacher variables; a sign at B_j=0 is immaterial.
Put B_d=1.
Conditional on all B_j, the coefficients of the Fourier polynomial tilde P_d/sqrt(S_d) have squared moduli summing to 1.
Applying (6) conditionally and then averaging the B_j gives, for every finite p>=1,
\[
 \sup_d\mathbb E\int
 \left|\log\frac{|P_d(e^{it})|}{\sqrt{S_d}}\right|^p
 \frac{dt}{2\pi}<\infty.
\tag{7}
\]
In particular zeros on the circle cause no loss of product-measure integrability.
This is not an assertion of a bound on the logarithmic expectation at every individual angle.

The law of large numbers gives S_d/(d sigma^2) tending to 1 in probability.
There is also a constant c_N>0 with
\[
 \mathbb P\{S_d<d\sigma^2/2\}\le e^{-c_Nd}.
\]
For completeness, choose a small positive t so that E exp(-t a_0^2)<=exp(-3t sigma^2/4), which is possible by differentiation at t=0, and apply the exponential Markov inequality to sum a_j^2.
On the complementary event, log(S_d/(d sigma^2)) is bounded by constants depending only on N.
On the exceptional event its negative part is at most log(d sigma^2) when this is positive, since S_d>=1.
Thus
\[
 \log\frac{S_d}{d\sigma^2}\longrightarrow0
 \quad\hbox{in every finite }L^p,
\]
and combining this with (7) proves
\[
 L_d(t):=\log\frac{|P_d(e^{it})|}{\sigma\sqrt d},
 \qquad
 \sup_d\mathbb E\int|L_d(t)|^p\frac{dt}{2\pi}<\infty
\tag{8}
\]
for every finite p>=1.

### One- and two-angle Gaussian limits

For almost every angle t, and almost every pair (t,s), the geometric averages of exp(2ijt), exp(2ijs) and exp(ij(t+s)), exp(ij(t-s)) tend to zero.
The excluded pairs have t or s equal to 0 or pi, or t=s or t=-s modulo 2pi, and form a set of angular product measure zero.
Consequently the normalized real covariance matrix for the lower-degree sum at one angle tends to (1/2)I_2, and for the two-angle vector it tends to (1/2)I_4.

Here is a direct central-limit calculation valid for these integer coefficients.
For a fixed real linear combination of the real and imaginary coordinates, write its j-th deterministic trigonometric weight as w_j.
These weights are bounded uniformly in j and d.
Since E a_j=0 and E a_j^2=sigma^2, Taylor expansion gives
\[
 \mathbb E\exp\!\left(\frac{ia_jw_j}{\sigma\sqrt d}\right)
 =1-\frac{w_j^2}{2d}+O_{N,w}(d^{-3/2}).
\]
Independence and the geometric-average covariance identities make the product of these characteristic functions tend to the centered real Gaussian characteristic function with the covariance just computed.
The deterministic monic term, divided by sigma sqrt(d), tends to zero and does not affect the limit.
Hence, with G a standard circular complex Gaussian satisfying E|G|^2=1,
\[
 \frac{P_d(e^{it})}{\sigma\sqrt d}\Rightarrow G,
 \qquad
 \left(\frac{P_d(e^{it})}{\sigma\sqrt d},
       \frac{P_d(e^{is})}{\sigma\sqrt d}\right)
 \Rightarrow(G_1,G_2),
\tag{9}
\]
where G_1 and G_2 are independent.
These statements hold at the specified almost-everywhere fixed angles and also after independent uniform angular sampling, by bounded-test-function integration.

The square modulus |G|^2 is exponential with mean 1, so
\[
 c:=\mathbb E\log|G|
 =\frac12\int_0^\infty e^{-u}\log u\,du
 =-\frac\gamma2.
\tag{10}
\]
The moment bounds (8), with p=2 and p=4, justify passage from (9) to the first moment of L_d(t) and to the mixed moment of L_d(t)L_d(s), respectively.
Explicitly,
\[
 \mathbb E_{\omega,t,s}|L_d(t)L_d(s)|^2
 \le\left(\mathbb E_{\omega,t,s}|L_d(t)|^4\right)^{1/2}
     \left(\mathbb E_{\omega,t,s}|L_d(s)|^4\right)^{1/2}
 \le C_N,
\]
which supplies uniform integrability for the mixed products despite their sharing the coefficients.
The limiting Gaussian variables are nonzero almost surely, so the logarithm's discontinuity at zero does not prevent convergence in distribution of these sampled logarithms.

### Angular integration and the arithmetic mean

Put
\[
 A_d=\int L_d(t)\frac{dt}{2\pi}
 =m(P_d)-\frac12\log(d\sigma^2).
\]
Fubini's theorem is justified by (8).
The single- and two-angle limits give E A_d tending to c and E A_d^2 tending to c^2.
It follows that E|A_d-c|^2 tends to zero, proving (3)-(4).

Finally,
\[
 \frac{M(P_d)}{\sigma\sqrt d}=e^{A_d}
 \le\frac{\sqrt{1+dN^2}}{\sigma\sqrt d}
 \le\sqrt{\frac{1+N^2}{\sigma^2}}.
\tag{11}
\]
Convergence of A_d in probability and the deterministic bound (11) give convergence of e^(A_d) to e^c in every finite L^p, proving (5).
Thus the arithmetic-mean asymptotic is established separately; it is not obtained by incorrectly interchanging expectation and exponentiation.

<a id="potential-and-lehmer-boundary"></a>
## Potential interpretation and limits of the average

For the normalized root counting measure mu_(P_d), one has m(P_d)=d integral log^+|z| d mu_(P_d).
Since this integrand is nonnegative, averaging commutes with the integral and (4) computes the total Green cost of the expected root measure.
For fixed N that total grows like (1/2)log d, while the cost divided by d tends to zero.
The estimate concerns typical polynomials in a coefficient box and supplies no positive lower bound for every nonzero individual Mahler value.
The polynomial z^d itself occurs in the box, and exceptional cyclotomic or unusually small positive-measure polynomials are not ruled out by this average.
No conditioning on the unit condition, reciprocity, irreducibility or real-rootedness is included, and such conditioned laws require their own arguments.

## Current assessment

[Selected self-reviewed argument](#decision-coefficient-box-expectation)

## Assessment history

### Decision coefficient-box-expectation

| Field | Value |
| --- | --- |
| date | 2026-11-07T15:03 |
| status | proved |
| reason | The complete argument establishes the exact finite bounds and fixed-N asymptotics, with the accepted source input and local conversions checked in the selected self-review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Coefficient-box expectations](#statement) | The independent uniform integer law, finite bounds, degree-one exact values and fixed-N limits (1)-(5). |
| argument | [Complete argument](#argument) | Conditional-sign logarithmic moments, single- and two-angle Gaussian limits and separate bounded transfer for the arithmetic mean. |
| review | [Whole self-review](../audits/reviews/Yin_R_G1093_v1.md#coefficient-box-expectation-finding) | The exact statement, complete argument and accepted NNS13 interface; self-reviewed, with no independent-review or source-proof re-audit assertion. |
