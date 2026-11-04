---
author: Yin
---

<a id="bv20-u001"></a>
# BV20-U001: Entropy and Mahler measure

## Source and inspection

[Source and edition notes](readme.md).

Source edition: BV20, [retained PDF](../../../literature/pdf/BV20.pdf): E. Breuillard and P. P. Varju, *Entropy of Bernoulli convolutions and uniform exponential growth for linear groups*, arXiv:1510.04043v4, 23 April 2021, 33 pages.
Published article: J. Anal. Math. 140 (2020), 443--481.
This audit belongs to v4, not automatically to journal or earlier preprint bytes.

Passages: Theorem 5 and Remark 6, pp.3--4; Sections 2 and 3.1--3.3, pp.6--21, including Lemmas 9, 11--12, 14, 16, 18, Theorem 10, Proposition 13, Corollary 15 and Proposition 17 (= Proposition 7). Printed and PDF page numbers coincide.

Inspection: 2026-10-06; human author Yin, prepared by an assigned AI source-review agent.
All mathematical body pp.1--31 was read; this unit records the analytic proof and its actual repairs/limits.
Delicate formulas on rendered pp.3--5,12--13,15--17,20 were checked.
The agent self-checked this record; a separate root agent independently confirmed the conditioning, Gaussian-tail and zero-parameter findings.
No formal verification or recursive audit of external originals is asserted.


## Assessment and scope

**Audited within scope**, with the elementary repairs below, for the qualitative entropy--Mahler estimate of Theorem 5 and its proof mechanism.
**Questioned at literal scope** for the truncation/majorant steps, the zero case of Propositions 7/17, and adoption of the numerical constant `0.44` as a certified bound.
The strictly positive unspecified constant is sufficient for the qualitative applications in [U002](Yin_U002.md#bv20-u002) and [U003](Yin_U003.md#bv20-u003).

The source supplies no numerical integration certificate.
This audit did not rerun MATLAB or certify an explicit constant.
The flagged steps are not counterexamples to the qualitative main estimate.

<a id="bv20-mahler-measure"></a>
## Mahler measure and units

For an algebraic number \(\lambda\), choose its primitive irreducible polynomial \(\pi_\lambda(X)=a_r\prod_{j=1}^r(X-\lambda_j)\in\mathbb Z[X]\), determined up to sign, and put

\[
M_\lambda=|a_r|\prod_j\max\{1,|\lambda_j|\}.
\]

The leading coefficient is essential for nonintegral numbers.
An **algebraic unit** is a nonzero algebraic integer whose inverse is also integral; equivalently its minimal polynomial is monic with constant coefficient \(\pm1\).
Then \(\widetilde M_\lambda:=\prod_{|\lambda_j|<1}|\lambda_j|^{-1}=M_\lambda\).
This equality is the reason the general-digit argument in Remark 6 requires a unit.
It need not hold for nonunits: \(\lambda=2\) has \(\widetilde M_2=1\) and \(M_2=2\).

All logarithms in BV20 are **base 2**.
Its \(\log M\) is \((\log M)_{\rm natural}/\log 2\); numerical entropy rates cannot be transferred unchanged to natural logarithms.

<a id="bv20-random-walk-entropy"></a>
## Finite random walks and entropy rates

Let \(\xi_i\) be independent fair signs and let \(\mu_\lambda^{(n)}\) be the law of \(\sum_{i=0}^{n-1}\xi_i\lambda^i\), with the zeroth power equal to one, including when \(\lambda=0\).
Define

\[
H(\mu)=-\sum_x\mu(x)\log_2\mu(x),\qquad
h_\lambda=\lim_{n\to\infty}\frac{H(\mu_\lambda^{(n)})}{n},\qquad
\rho_\lambda=\lim_{n\to\infty}\frac{\log_2|\operatorname{supp}\mu_\lambda^{(n)}|}{n}.
\]

The two limits exist by subadditivity under the block convolution decomposition; multiplication by \(\lambda^n\) preserves entropy/cardinality for \(\lambda\ne0\).
The zero case is direct.
Always \(0\le h_\lambda\le\rho_\lambda\le1\).
The finite walk is meaningful for any complex \(\lambda\), unlike the infinite Bernoulli convolution.

For finitely supported rational digits with law \(\nu_0\), use the same definition with the corresponding digits and write \(h_{\lambda,\nu_0}\).
The source's selected v4 Remark 6 assumes **\(\lambda\) is an algebraic unit** and gives

\[
c(\nu_0)\min\{1,\log_2M_\lambda\}
\le h_{\lambda,\nu_0}
\le\min\{H(\nu_0),\log_2M_\lambda\}.
\]

For a nonconstant digit law the proof gives \(c(\nu_0)>0\); a point mass has zero entropy and only the trivial constant zero.
Remark 6 itself does not explicitly call its constant positive, so this is a necessary reuse distinction, not a counterexample to its literal wording.
The same law \(\nu_0\) and constant must work uniformly over the units in this statement.
For each \(\varepsilon>0\), the source also permits a suitable finite rational law with \(c(\nu_0)>1-\varepsilon\).

## Reusable theorem and checked proof structure

**Theorem 5.** There is an absolute \(c_0>0\) such that for every algebraic \(\lambda\),

\[
c_0\min\{1,\log_2M_\lambda\}
\le h_\lambda\le\min\{1,\log_2M_\lambda\}.
\]

The following steps were checked against the printed argument.

1. **Reduction to units.**
   For \(\lambda\ne0\), a collision of two sign sums gives a polynomial with coefficients \(0,\pm1\).
   Remove its initial power of \(X\); its first and last nonzero coefficients are \(\pm1\), so its nonzero roots are units.
   A nonzero nonunit therefore has \(2^n\) equiprobable distinct sums and \(h=\rho=1\).
   Its measure is at least two: either the leading or constant integer coefficient has absolute value at least two.
   Treat \(\lambda=0\) separately, where \(h=\rho=0\) and \(M=1\).
   Units of measure one have zero rate by the counting argument below.
2. **Information inequalities.**
   Sections 2.3--2.4 distinguish discrete entropy from differential entropy \(-\int f\log_2f\).
   Change of variables adds \(\log_2|\det A|\) only in the differential case.
   The submodularity inequality
   \[
   H(X+Y+Z)+H(Y)\le H(X+Y)+H(Y+Z)
   \]
   holds for independent \(X,Y,Z\), with the four displayed distributions absolutely continuous and of finite differential entropy.
   The source's joint-entropy proof, Gaussian smoothing and conditioning limit were checked with the corrections in F1--F2.
3. **Many scales.**
   For a contracting real matrix \(A\) with distinct eigenvalues the inside-disk conjugates of a nonzero unit, form \(X_A=\sum\xi_i A^i\).
   Rational polynomial relations give \(H(X_\lambda^{(n)})=H(X_A^{(n)})\ge H(X_A^{(n)}x)\).
   Proposition 13 uses self-similarity, Lemma 9 and a telescoping sum over the scales \(A^i\) to obtain
   \[
   h_{\lambda,\nu_0}\ge H(X_Ax;A\mid I)\ge H(\xi_0x;A\mid I).
   \]
   The covariance order follows from \(AA^t\le I\), including for a nonnormal \(A\); it is not an assumption that \(A\) is diagonal or symmetric.
4. **Compress the contraction to one direction.**
   The alternative proof on pp.15--16 avoids dependence on Horn's theorem: for a cyclic vector \(v\), the positive form \(q_v(x)=\sum_{n\ge0}\langle A_0^nx,v\rangle^2\) satisfies \(q_v-q_v\circ A_0=\langle x,v\rangle^2\).
   In this metric all but one singular value are one; the last is \(M_\lambda^{-1}\).
   Gaussian rotation/change of variables then gives
   \[
   h_{\lambda,\nu_0}\ge\Phi_{\nu_0}(M_\lambda),\quad
   \Phi_{\nu_0}(a)=\sup_{t>0}\{H(at\xi_0+G)-H(t\xi_0+G)\},
   \]
   for standard real Gaussian \(G\) independent of the digits.
   This step applies only to the nontrivial contracting-conjugate case; the zero/measure-one cases were separated above.
5. **A qualitative uniform constant.**
   Lemma 14 proves monotonicity and \(\Phi(a^2)\le2\Phi(a)\).
   Iterated squaring reduces every \(1<a<2\) to \(\sqrt2\le a^{2^k}<2\), giving Corollary 15.
   Positivity for nonconstant finite digits needs no numerical integration: \(F(t)=H(t\xi_0+G)\) tends to \(H(G)\) as \(t\downarrow0\) and to \(H(G)+H(\nu_0)\) as \(t\to\infty\).
   Thus for every \(a>1\), some \(t\) has \(F(at)>F(t)\); otherwise iteration would contradict the different limits.
   Monotonicity consequently bounds \(\Phi(a)/\log_2a\) away from zero throughout \([\sqrt2,2]\).
   These are the elementary positivity details implicit in the source's calculus step, not a certification of `0.44`.
6. **Counting upper bound.**
   For a unit, the algebraic norm separates distinct finite sums after projecting onto the conjugates of modulus at least one.
   Packing disjoint balls into an anisotropic box gives
   \(|\operatorname{supp}\mu_\lambda^{(n)}|\le C_\lambda n^kM_\lambda^n\), where \(k\) counts unit-circle conjugates with multiplicity.
   Polynomial factors disappear in the rate.
   The rational finite-digit version follows by clearing one common denominator; constants may depend on the digit support and \(\lambda\), but not on \(n\).

<a id="bv20-gaussian-scale-entropy"></a>
## Gaussian scale entropy

For a bounded random vector \(X\in\mathbb R^d\) and **invertible** \(B\), let \(G_B\) have covariance \(BB^t\) and be independent of \(X\), and set
\[
H(X;B)=H(X+G_B)-H(G_B),\qquad
H(X;B_1\mid B_2)=H(X;B_1)-H(X;B_2).
\]
Write \(B_1\preceq B_2\) when \(B_2B_2^t-B_1B_1^t\) is positive semidefinite.
Lemma 9 gives positivity, convolution subadditivity, decrease with scale, and increase of the scale difference under independent convolution.
Every Gaussian-smoothed law used here has finite differential entropy.
The difference notation is not Shannon conditioning on a sigma-algebra.
Although p.8 mentions \(B_i\in M_d(\mathbb R)\), the displayed differential entropies require nonsingular \(B_i\); no singular-scale extension is supplied or used.

## Strictness below measure two

The reusable version of Propositions 7/17 requires **\(\lambda\ne0\)**, \(M_\lambda<2\), and no unit-circle conjugate.
Such a \(\lambda\) is a unit.
Then \(h_\lambda<\log_2M_\lambda\).

Lemma 18 embeds the walk in its contracting real/complex conjugates.
Frequencies formed from inverse powers tend to infinity, while the Fourier transform stays away from zero: traces of powers are integers, the expanding conjugates control one tail of the cosine product, and the contracting conjugates control the other.
No cosine factor vanishes because the relevant sums are algebraic integers whereas its zeros would require a nonintegral rational number.
The usual pure-type property of the invariant self-affine law then turns nonabsolute continuity into singularity.
This property is retained here at that interface; no original proof of the general pure-type theorem was audited.

The source then packs the finite walk into shrinking boxes.
A compact set carrying almost all singular mass occupies arbitrarily small Lebesgue volume, so almost all mass lies on at most \(C\varepsilon M^n\) atoms.
The remaining atoms number at most \(C'M^n\) and carry mass at most \(\varepsilon\).
The two-part Shannon bound gives \(H(\mu^{(n)})<n\log_2M\) for some sufficiently large \(n\); subadditivity, not merely passage to a limit of strict inequalities, gives strictness of the rate.

<a id="bv20-strictness-reread-2026-10-07"></a>
### Original bounded strictness reread

The original2026-10-07 [L_G100 record](../../../ledger/Yin_L_G0100_v1.md#strict-deficit-source-scope) reports that the assigned ms25_source agent reread and visually inspected the same retained arXivv4 PDF's printed/PDF pp.19–21, Proposition17, Lemma18 and their complete proofs.
This later reread retains the nonzero and cosine-zero corrections, source-base2/natural-log conversion, no-unit-circle scope and external pure-type interface above.
It does not inspect an original proof of the external pure-type theorem or establish a quantitative singularity/concentration time.
The coordinator's actual direct mathematical review used this reported reread and the existing U001 premise; it did not newly inspect the source PDF in that round.
The complete local explicit packing, Fourier-tail and concentration-time arguments are now retained in [C_G293](../../../claims/Yin_C_G0293_v1.md#argument).
These are the original10/7 reading facts, not a new source inspection during material construction; the separate10/6 accepted source depth, version, repairs and proof boundaries remain unchanged.
This scope concerns strictness pp.19–21, separately from U002's p.31 Mercat source report and later visual-reading facts.

<a id="bv20-u001-findings"></a>
## Findings and exact effect

All findings below concern existing source text, identified on 2026-10-06; they do not change the PDF.

- **F1 -- medium, Theorem 10 proof p.13: conditioning destroys independence.**
  The event \(A_n=\{\|X\|+\|Y\|+\|Z\|<n\}\) does not preserve the independence needed to apply the bounded theorem.
  For independent uniform \([0,1]\) variables, conditioning on \(X+Y+Z<1\) gives \(E[X]=E[Y]=1/4\), \(E[XY]=1/20\), and covariance \(-1/80\).
  Replace \(A_n\) by the product event \(\{\|X\|<n,\|Y\|<n,\|Z\|<n\}\).
  Independence is then preserved, the events increase to probability one, and Lemma 12 applies to each sum law.
  This repairs the printed limiting argument and Lemma 9's uses of it.
- **F2 -- low, Lemma 11 p.12: the printed Gaussian majorant is too small.**
  Uniformly for all \(0<\varepsilon<1\), the claimed bound \((f*g_\varepsilon)(x)<e^{-(\|x\|-R)^2}\) is false.
  Take \(X\) uniform on \([-1,1]\), \(\varepsilon=0.9\); its convolution tail has quadratic exponent \(-x^2/(2\varepsilon^2)+O(|x|)\), which decays more slowly than the printed bound for every fixed \(R\).
  For the required limit restrict to \(\varepsilon\le1/2\), and use a constant multiple of an integrable Gaussian-tail majorant for \(-f*g_\varepsilon\log_2(f*g_\varepsilon)\).
  The constant also accounts for the base-2 logarithm.
  Reverse Fatou and the lower entropy inequality then give the stated convergence.
- **F3 -- medium reuse limitation, pp.3,16--17: `0.44` is not certified.**
  The source explicitly says its MATLAB integration supplies no error estimates.
  Theorem 5's existential \(c_0>0\) follows analytically; the value \(c_0\ge0.44\), the numerical Corollary 8 threshold, and the fixed constants later obtained from it do not inherit that proof.
  Use an unspecified \(c_0\), or obtain an independent rigorous lower bound before quantitative reuse.
- **F4 -- low, Propositions 7/17 pp.4,19: missing zero exclusion.**
  For \(\lambda=0\), \(M_0=1\), no conjugate lies on the unit circle, and \(h_0=0\), so the literal conclusion is \(0<0\).
  Add \(\lambda\ne0\).
  The unit proof and the growth application already operate in this nonzero domain.
- **F5 -- low, local transcription/domain slips.**
  On p.20 the zero set of \(\cos(2\pi u)\) is \(1/4+(1/2)\mathbb Z\), not the cited half-integers; all these values are still nonintegral rationals, so the algebraic-integer argument works.
  On p.18 the real coordinate formula with denominator \(|\sigma_i(\lambda)|-1\) needs its limiting value \(n\) when the modulus is one (in particular \(\lambda=\pm1\)).
  On p.21 the tail display must be an absolute-value bound \(\sum_{j\ge n}|\sigma_i(\lambda)|^j\), not an equality with an unsigned sum lacking the random signs.
  These corrections were included in checking the packing argument.

## Dependencies and reuse boundary

The entropy identities and submodularity proof were checked in BV20 itself, so citing Madiman [35] is attribution rather than an unchecked substitute for that argument.
The alternative cyclic-vector construction supplies the needed singular values without importing Horn [28].
Algebraic norm integrality, Gaussian change of variables, dominated/reverse-Fatou convergence and the Riemann--Lebesgue lemma are retained standard inputs at their stated domains.
The pure-type interface is retained as described above.
No source in the bibliography receives a whole-proof audit from this record.

Remark 6's near-one constants use finite rational approximations to a Gaussian in the displayed \(\Phi\)-formula.
The approximation argument and its bounded-parameter applicability were inspected at proof-outline depth; no quantitative approximation rate or specific digit law is certified.
Its dimension application is recorded in U002.
No project Task or Claim is created by these source records.
