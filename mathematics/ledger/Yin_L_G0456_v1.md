---
author: Yin
---

# Chebyshev lattice rounding and an endpoint-kernel counterexample test

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The delegated research agent developed and checked the Chebyshev-basis rounding bound, the positive real target, and the explicit integer endpoint-kernel correction.
The coordinating agent checked the cotangent integral used below.
These are ordinary author derivations and checks, not an independent project review or a new Claim assessment.
No numerical root search or finite enumeration is an input.

<a id="chebyshev-rounding-scope-and-reuse"></a>
## Question and retained inputs

Can a concrete correlated integer rounding of a shrinking-capacity trace model produce an actual integer polynomial with positive total logarithmic Mahler measure tending to zero?
An irreducible trace polynomial is not required.
A positive-to-zero sequence of whole monic integer reciprocal outputs would already suffice, since a positive irreducible factor could be selected from each output.

[L454's prescribed-residue construction](Yin_L_G0454_v1.md#prescribed-residue-adaptation) supplies the prior rounding comparison and its actual coefficient and root-localization costs.
Its [total Green-function budget](Yin_L_G0454_v1.md#total-green-function-budget) retains every root and the total, rather than degree-normalized, measure.
Its [scaled-Chebyshev control](Yin_L_G0454_v1.md#equilibrium-and-scaled-chebyshev-control) supplies the complete midpoint-root measure estimate reused below.
[L449's Chebyshev calibration](Yin_L_G0449_v1.md#chebyshev-slice-calibration) already prices a constant integer shift and warns against counting only one escaping root.

The accepted [DS17 univariate fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) says that for every fixed integer K there is eta_K>0 such that a nonzero integer polynomial with at most K nonzero monomials has total logarithmic measure either zero or at least eta_K.
It bounds neither the degree nor coefficient height and does not require irreducibility.
Its accepted statement and source-proof inspection limits remain exactly those of the linked source unit.
[C221's bounded-support completion](../claims/Yin_C_G0221_v1.md#controlled-entropy-completion) and [support-escape consequence](../claims/Yin_C_G0221_v1.md#cyclotomic-support-escape) already own that general obstruction.
The applications below do not claim a new sparse-gap theorem.

The bounded local comparison read these actual materials and searched the existing ledger and drafts for Chebyshev rounding, scaled Chebyshev targets, coefficient rounding and second-kind endpoint corrections.
It found the preceding adequate general inputs but no retained account of the specific L2 rounding calculation below.
This is not an exhaustive search or a novelty claim.
No new external theorem is needed for the elementary estimates.

All logarithms are natural.
For a trace polynomial Q of degree n, its reciprocal lift is P(z)=z^n Q(z+z^{-1}).
Its complete logarithmic Mahler measure is the sum of the Green-function contributions of all trace roots, as in L454.
When Q is real but not integral, that fact is stated explicitly.

<a id="nearest-chebyshev-integer-rounding"></a>
## Nearest Chebyshev-lattice rounding at a shrinking capacity

Use the integer monic polynomials
\[
 C_j(t)=2T_j(t/2)\qquad(j\ge1),
\]
and use 1, rather than C_0=2, for the constant basis element.
Their triangular monic coefficients make
\[
                         1,C_1,\ldots,C_n
\]
an integral basis of Z[t]_{\le n}.
For the arcsine probability measure mu_0 on [-2,2],
\[
 C_j(2\cos\theta)=2\cos(j\theta),\qquad
 \|1\|_{L^2(\mu_0)}^2=1,\qquad
 \|C_j\|_{L^2(\mu_0)}^2=2\quad(j\ge1),
\]
and distinct basis elements are orthogonal.
These identities follow by direct integration with dtheta/pi on [0,pi].

Consider the actual scaled-Chebyshev target from L454:
\[
 A_{n,\kappa}(t)=\kappa^n C_n(t/\kappa),\qquad
 \kappa>1,\qquad a=n\log\kappa.
 \tag{1}
\]
It is monic of degree n, with all roots explicitly retained.
We test nearest rounding in the displayed integer basis without imposing a finite-field residue or irreducibility.

For 0<a<=1, the uniform bound is
\[
 \boxed{\|A_{n,\kappa}-C_n\|_{L^2(\mu_0)}^2\le64a.}
 \tag{2}
\]
To prove it, put
\[
 \phi(\theta)=\arccos(\kappa^{-1}\cos\theta),
 \qquad 0<\theta<\pi.
\]
Integrating the derivative of arccos(s cos(theta)) for s in [kappa^{-1},1] gives
\[
 |\phi(\theta)-\theta|
 \le(1-\kappa^{-1})|\cot\theta|.
 \tag{3}
\]
Indeed sqrt(1-s^2 cos^2(theta))>=sin(theta) throughout that interval.
Since n(1-kappa^{-1})<=n log(kappa)=a,
\[
 \begin{aligned}
 |A_{n,\kappa}(2\cos\theta)-C_n(2\cos\theta)|
 &\le2(e^a-1)+2\min\{2,a|\cot\theta|\}.
 \end{aligned}
 \tag{4}
\]
The bound at the two omitted endpoints is irrelevant to the integral.

Define
\[
 I(a)=\frac1\pi\int_0^\pi
             \min\{4,a^2\cot^2\theta\}\,d\theta.
\]
The switch occurs at tau=arctan(a/2) and at pi-tau.
Since
\[
 \int_\tau^{\pi/2}\cot^2\theta\,d\theta
       =\cot\tau+\tau-\pi/2,
\]
direct integration gives
\[
 \begin{aligned}
 I(a)
 &=\frac2\pi
 \left(4\tau+a^2(\cot\tau+\tau-\pi/2)\right)\\
 &=\frac2\pi
 \left((4+a^2)\tau+2a-\frac{\pi a^2}{2}\right)\\
 &\le\frac{9a}{\pi}<3a\qquad(0<a\le1).
 \end{aligned}
 \tag{5}
\]
For the last inequality, use tau<=a/2 and a^3<=a.
Using (x+y)^2<=2x^2+2y^2 in (4), and e^a-1<2a for 0<a<=1, now yields
\[
 \begin{aligned}
 \|A_{n,\kappa}-C_n\|_2^2
 &\le8(e^a-1)^2+8I(a)\\
 &<32a^2+24a\le56a<64a.
 \end{aligned}
 \tag{6}
\]
This proves (2).

Expand the monic target in the integral basis:
\[
 A_{n,\kappa}=C_n+b_0+\sum_{j=1}^{n-1}b_jC_j.
\]
Orthogonality gives
\[
 \|A_{n,\kappa}-C_n\|_2^2
                 =b_0^2+2\sum_{j=1}^{n-1}b_j^2.
 \tag{7}
\]
If a<1/256, every b_j has absolute value strictly below 1/2.
Nearest integer rounding of every coordinate therefore produces exactly C_n.

This is also the unique global L2(mu_0)-nearest monic integer polynomial of degree n.
The integral basis describes the entire coefficient lattice, and the squared distance is a diagonal sum of coordinate errors with positive weights.
Consequently allowing correlated choices of integer coefficients does not improve this particular L2 minimization.

The resulting reciprocal lift is exactly
\[
                   z^nC_n(z+z^{-1})=z^{2n}+1.
 \tag{8}
\]
All of its roots are roots of unity.
Its total logarithmic Mahler measure is zero, so this rounding mechanism fails the required positive-measure condition.

<a id="positive-real-target-cyclotomic-rounding"></a>
## An explicit positive real target that rounds to zero measure

The failure occurs even for explicit real targets whose complete measure is positive and tends to zero.
Take
\[
 \kappa_n=e^{2/n^2},\qquad A_n=A_{n,\kappa_n},\qquad n\ge2.
 \tag{9}
\]
The largest trace root is
\[
              t_{\max}=2\kappa_n\cos\frac{\pi}{2n}>2.
 \tag{10}
\]
Indeed,
\[
 e^{2/n^2}\cos\frac{\pi}{2n}
 \ge
 \left(1+\frac2{n^2}\right)
 \left(1-\frac{\pi^2}{8n^2}\right)>1
 \qquad(n\ge2).
\]
For the last strict inequality, pi^2<10 bounds the difference from one below by
3/(4n^2)-5/(2n^4)>0 when n>=2.

Let
\[
                   \widetilde P_n(z)=z^nA_n(z+z^{-1}).
\]
The complete midpoint-root estimate in [L454, equation (36)](Yin_L_G0454_v1.md#equilibrium-and-scaled-chebyshev-control) gives
\[
 \begin{aligned}
 0<m(\widetilde P_n)
 &\le n\log\kappa_n+2\operatorname{arcosh}\kappa_n\\
 &\le \frac{2+4e^{1/4}}n<\frac8n.
 \end{aligned}
 \tag{11}
\]
The first inequality is strict by (10).
For the second upper bound, use arcosh(1+x)<=sqrt(2x) for x>=0 and
\[
              e^{2/n^2}-1\le(2/n^2)e^{1/2}\qquad(n\ge2).
\]
All n trace roots and all 2n lifted roots are included in (11).

These targets have real coefficients, not an asserted integer construction.
For n>=513 one has a=2/n<1/256.
Their unique nearest integer output is therefore (8).
The obstruction is a verified loss of noncyclotomicity under this rounding rule, rather than a failure to bound the ideal target's total measure.

<a id="bounded-energy-integer-repair"></a>
## Bounded-energy integer repairs retain bounded support

Suppose a different monic integer output Q_n of degree n satisfies
\[
        \|Q_n-A_{n,\kappa_n}\|_{L^2(\mu_0)}\le B
 \tag{12}
\]
for a fixed B, while a_n=n log(kappa_n) tends to zero.
The target satisfies |A_{n,kappa_n}(t)|<=2e^{a_n} on [-2,2], so
\[
       \|A_{n,\kappa_n}\|_2\le2e^{a_n}.
\]
The triangle inequality makes ||Q_n||_2 uniformly bounded.

Write
\[
 Q_n=b_{0,n}+\sum_{j=1}^n b_{j,n}C_j,\qquad
 b_{j,n}\in\mathbb Z.
\]
Its actual reciprocal lift is
\[
 P_n(z)=b_{0,n}z^n+
        \sum_{j=1}^n b_{j,n}(z^{n+j}+z^{n-j}).
 \tag{13}
\]
The displayed exponents are distinct.
Integer coefficients and orthogonality consequently give
\[
 \#\operatorname{supp}(P_n)
 \le b_{0,n}^2+2\sum_{j=1}^n b_{j,n}^2
 =\|Q_n\|_2^2.
 \tag{14}
\]
Thus these outputs have a uniform finite support bound K.
The accepted DS17 input gives
\[
                m(P_n)=0\quad\hbox{or}\quad m(P_n)\ge\eta_K>0.
 \tag{15}
\]
Irreducibility is unnecessary for this application.

This is a direct use of the existing support-escape principle.
It shows that a successful positive-to-zero integer repair of this target must leave every fixed L2-error budget.
It does not exclude corrections with growing quadratic energy but small complete logarithmic cost.

<a id="integer-endpoint-kernel-correction"></a>
## A positive integer endpoint-kernel correction and its exact completion

To test growing energy concretely, define integer second-kind polynomials by
\[
 S_0(t)=1,\quad S_1(t)=t,\quad
 S_j(t)=tS_{j-1}(t)-S_{j-2}(t)\quad(j\ge2).
\]
Their exact circle identities are
\[
 S_{n-1}(2\cos\theta)=\frac{\sin(n\theta)}{\sin\theta},
 \qquad
 S_{n-1}(z+z^{-1})
 =z^{n-1}+z^{n-3}+\cdots+z^{-(n-1)}.
 \tag{16}
\]
Both follow from the displayed recurrence, with the endpoint values defined by limits.

For n>=1 and c in Z, consider
\[
 Q_{n,c}(t)=C_n(t)-cS_{n-1}(t),\qquad
 P_{n,c}(z)=z^nQ_{n,c}(z+z^{-1}).
\]
The trace lift is a monic reciprocal integer polynomial of degree 2n with constant coefficient one.
Equation (16) gives the full polynomial
\[
 P_{n,c}(z)
 =z^{2n}+1-c(z^{2n-1}+z^{2n-3}+\cdots+z).
 \tag{17}
\]
Multiplication by one cyclotomic factor gives exactly
\[
 \boxed{
 (z^2-1)P_{n,c}(z)
 =
 z^{2n+2}-cz^{2n+1}-z^{2n}
 +z^2+cz-1.}
 \tag{18}
\]
The right side has at most six nonzero monomials, including coincident-exponent or zero-coefficient cases.

For c=1 and n>=3,
\[
                         Q_{n,1}(2)=2-n<0,
\]
whereas the monic polynomial Q_{n,1}(t) tends to positive infinity as t tends to positive infinity.
It therefore has an actual real trace root above 2.
The corresponding reciprocal quadratic has a root outside the unit circle, and
\[
                         m(P_{n,1})>0.
 \tag{19}
\]
This establishes noncyclotomicity without an irreducibility premise.

The correction genuinely escapes the bounded-energy regime.
For even n,
\[
 S_{n-1}=C_{n-1}+C_{n-3}+\cdots+C_1,
\]
and for odd n,
\[
 S_{n-1}=C_{n-1}+C_{n-3}+\cdots+C_2+1.
\]
Orthogonality therefore gives
\[
              \|S_{n-1}\|_2^2=n,\qquad
              \|Q_{n,c}\|_2^2=2+c^2n.
 \tag{20}
\]
The cross term vanishes since S_{n-1} has degree below n.

Nevertheless m(z^2-1)=0, so (18), additivity of Mahler measure, and DS17 imply
\[
 \boxed{
 m(P_{n,c})=0
 \quad\hbox{or}\quad
 m(P_{n,c})\ge\eta_6>0.}
 \tag{21}
\]
This covers varying integer c as well as varying n.
For c=1 and n>=3, the positive alternative holds by (19).
All roots and factors of P_{n,c} remain included in this identity; no individual escaping root is substituted for the total measure.

Thus this explicit endpoint kernel achieves a positive integer output and unbounded quadratic energy, but its bounded-support cyclotomic completion prevents positive measure from tending to zero.
The argument classifies this displayed family, not arbitrary localized integer corrections.

<a id="rounding-counterexample-boundary"></a>
## Irreducibility, actual outcomes and the next test

The counterexample objective requires neither an irreducible trace polynomial nor an irreducible whole reciprocal output.
Both tests above keep that weaker requirement.
They fail respectively through cyclotomic output and through a complete positive-measure floor, not because irreducibility was left unproved.

Within the particular L454 prescribed-residue proof, removing parity replaces coefficient meshes of width two by width one and improves the corresponding rounding constants.
It does not by itself replace that proof's growing bound n^(C_0+C_0 sqrt(n)) or resolve its shrinking-capacity localization problem.
This observation concerns those displayed construction steps and sufficient bounds, not all possible arithmetic realization methods.
The direct Chebyshev rounding considered here bypasses the prescribed-residue construction entirely.

The original scaled-Chebyshev integrality obstruction concerns exact scaled models.
The new calculation instead prices a specific lattice rounding, identifies its actual output on an explicit positive real target sequence, and tests one integer correction that leaves the bounded-energy regime.
The ordinary author checks cover the full arcsine normalization, the cotangent antiderivative and cutoff, the coefficient-lattice minimization, the strict endpoint root, every root in the retained Green bound, the integer kernel recurrence, the full six-term identity and the exact scope of the external sparse-gap input.

A further useful candidate must avoid both demonstrated failures: bounded-energy rounding that locks onto a cyclotomic lattice point, and growing-energy corrections with uniformly sparse cyclotomic completions.
The next bounded test should specify an actual integer correction with growing completed support and estimate the full logarithmic measure directly.
No such successful correction, positive-to-zero integer sequence or unrestricted Task conclusion has been obtained here.
