---
author: Yin
---
# Original coefficient lattices: a paid local positive-shell neighborhood and its stratum-dependent loss

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This bounded 2026-11-05 continuation concerns the unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) and the single-original-integer-point gap left by [L449v1](Yin_L_G0449_v1.md#jacobian-and-one-point-mass).
The question is whether an actual positive-measure irreducible integer polynomial supplies enough nearby continuous coefficient volume to contradict the complete reciprocal Mahler thin-shell volume.
The authoring agent local_arithmetic_cell developed and checked the construction for human author Yin.
This is author-checked exploration, without independent review, a new Claim assessment or a uniform Mahler gap.

The construction below supplies a positive-volume neighborhood of every such original input, with its root separation, endpoint distances, real dimension, injectivity and full Jacobian paid.
Allowing interior real trace roots to move at no Mahler cost improves the elementary isotropic ball to a stratum-dependent lower bound.
The resulting comparison gives only a very weak degree-dependent bound in the one-active-real-dimension stratum, no measure restriction in the two-dimensional stratum, and the wrong direction for excluding small measure in higher active dimension.
The one-dimensional bound is already weaker than the direct endpoint integer estimate from the same input.
This disposes of the stated generic neighborhood construction, not of every possible stronger neighborhood or arithmetic constraint.

<a id="inputs-and-existing-costs"></a>
## Inputs and existing costs

[L449v1's original trace lattice](Yin_L_G0449_v1.md#original-trace-lattice) owns the integral affine triangular change of independent reciprocal coefficients, its determinant one, the original total logarithmic measure, and the bodies B_N(epsilon).
Its [Sinclair source and local comparison](Yin_L_G0449_v1.md#source-and-local-comparison) and [complete Laplace expansion](Yin_L_G0449_v1.md#sinclair-moment-and-laplace-inversion) supply the exact real-coefficient shell volume at their stated source-inspection and author-calculation scope.
The source normalization, Laplace inversion and source-proof limitations are reused, not re-audited here.

[C243](../claims/Yin_C_G0243_v1.md#reciprocal-trace-domain) supplies the actual integral trace polynomial and does not assume its roots are real.
Its [discriminant and order calculation](../claims/Yin_C_G0243_v1.md#reciprocal-trace-order-index) retains the trace discriminant and endpoint factors; the scalar identity is also stated in [L449v1](Yin_L_G0449_v1.md#jacobian-and-one-point-mass).
The integer inputs used below are precisely the nonzero discriminant of Q and its two nonzero endpoint evaluations.
They are not new independent arithmetic income.

[C209](../claims/Yin_C_G0209_v1.md#gram-lower-certificate) and [C215](../claims/Yin_C_G0215_v1.md#general-reciprocal-necessary-bound) already pay the complete Gram, discriminant and spectral boundary in their different finite-window certificates.
[L446v3's dyadic gain](Yin_L_G0446_v3.md#paid-dyadic-gain) retains its exact large integer denominator.
None of those particular formulas is the continuous neighborhood assertion below, and none is used as an additional lower factor in it.
[C231's all-positive-power existence descent](../claims/Yin_C_G0231_v1.md#all-positive-power-existence-descent) permits the original all-power endpoints as inputs but supplies no stronger local radius here.

<a id="original-input-and-separation"></a>
## Original input and explicit integer separation

Let P be monic, irreducible, reciprocal and noncyclotomic in Z[z], of degree 2N with N>=2, and put

\[
 P(z)=z^NQ(z+z^{-1}),\qquad Q\in\mathbb Z[t]\text{ monic},
 \qquad 0<\varepsilon=m(P)\le1.
\]

Retain the original arbitrary integer coefficients, without a height-one or bounded-coefficient restriction.
The polynomial Q is irreducible and separable of degree N, and Q(2) and Q(-2) are nonzero: either endpoint root would give a root 1 or -1 of the irreducible noncyclotomic P.
Write its complete root set as beta_1,...,beta_N, and set

\[
 K=\frac{N(N-1)}2,\qquad
 \Delta=|\operatorname{disc}Q|\in\mathbb Z_{\ge1}.
\]

For a trace root w, let rho(w) be the larger modulus of the two roots of z^2-wz+1, and let g(w)=log rho(w).
The complete measure identity is m(P)=sum_j g(beta_j), with every g(beta_j)>=0.
Thus rho(beta_j)<=exp(epsilon), and

\[
 |\beta_j|\le2\cosh\varepsilon<4.
\]

Define the actual separation and endpoint distance by

\[
 s=\min_{i\ne j}|\beta_i-\beta_j|,\qquad
 h=\min_{j,\,e\in\{-2,2\}}|\beta_j-e|.
\]

Their explicit uniform lower bounds are

\[
 s\ge s_N:=8^{-(K-1)},\qquad
 h\ge\eta_N:=6^{-(N-1)}. \tag{A}
\]

Indeed sqrt(Delta) is the product of the K absolute root differences, every difference is less than 8, and sqrt(Delta)>=1.
Isolating a smallest difference gives 1<=s*8^(K-1).
For the endpoint and root realizing h, the nonzero integer |Q(e)| is at most h*6^(N-1), since all remaining endpoint distances are less than 6.
This proves (A) using the actual full-root products, not a root-density or independence assumption.

<a id="full-complex-root-chart"></a>
## A root chart covering every real and complex stratum

Let r_0 be the number of real trace roots in (-2,2), r_1 the number of real trace roots outside [-2,2], and q the number of roots in the open upper half-plane.
The latter roots represent all q nonreal conjugate pairs.
Then

\[
 r_0+r_1+2q=N,\qquad n:=r_1+2q\ge1.
\]

The positive integer n is the number of active real coordinates in the construction below, not a replacement for the original degree or a division of the Mahler measure.
The inequality n>=1 follows because g vanishes exactly on [-2,2].
No total-reality or Salem assumption is made.

Choose

\[
 \tau_N=\min\left\{\frac{s_N}{8K},\frac{\eta_N}{4}\right\},
 \qquad
 \sigma_N=\min\left\{\tau_N,\frac{\varepsilon\eta_N}{8N}\right\}.
 \tag{B}
\]

Move each of the r_0 interior real roots within its open real interval of radius tau_N.
Move each of the r_1 exterior real roots within its open real interval of radius sigma_N.
Move each upper-half-plane root within its open complex disk of radius sigma_N and impose the conjugate displacement on its lower-half-plane partner.
The product of these intervals and disks is an open set of N real parameters.

All root disks are disjoint, since every movement is at most tau_N<=s_N/(8K).
An original upper-half-plane root has imaginary part at least s/2, because its conjugate is another distinct root, so its permitted disk remains in the upper half-plane.
All real-root intervals avoid both endpoints by tau_N<=eta_N/4.
Thus neither collisions, changes of conjugate pairing nor endpoint crossings occur.
The roots remain in their respective original labeled disks, so two parameter points producing the same polynomial must have the same root in every disk.
The coefficient map is therefore injective on this chart, without a factorial division for root permutations.

<a id="positive-shell-control"></a>
## Positive-shell control with both thresholds retained

On a disk of radius tau_N around any original trace root, choose a holomorphic branch a(w) of a root of z^2-wz+1.
Such a branch exists because the disk is simply connected and avoids 2 and -2.
The branch never vanishes and admits a holomorphic logarithm there.
The other quadratic root is a(w)^(-1), so

\[
 g(w)=|\operatorname{Re}\log a(w)|,\qquad
 \frac{d}{dw}\log a(w)=\frac{\pm1}{\sqrt{w^2-4}}.
\]

Throughout the disk, each of |w-2| and |w+2| is at least 3eta_N/4.
Integrating the derivative along the straight segment in the disk, and using the Lipschitz inequality for the absolute value, gives

\[
 |g(w)-g(\beta_j)|\le\frac{2}{\eta_N}|w-\beta_j|.
 \tag{C}
\]

The r_0 interior real roots continue to have g=0 identically under their permitted real movements.
For the other roots, counting both members of each conjugate pair, the change in total measure is at most

\[
 \frac{2n\sigma_N}{\eta_N}\le\frac\varepsilon4.
\]

Let U_P be the image of this parameter domain in the independent real coefficient coordinates of Q.
It follows that every P' arising from U_P satisfies

\[
 \frac{3\varepsilon}4\le m(P')\le\frac{5\varepsilon}4,
 \qquad
 U_P\subset B_N(5\varepsilon/4)\setminus B_N(0).
 \tag{D}
\]

The center is the original integer input; neighboring polynomials have real coefficients and are not claimed to be integral or irreducible.
This is a continuous mass attached to one real integer input, not a unit lattice cell and not a new discrete probability law.

<a id="full-jacobian-and-local-mass"></a>
## Full Jacobian and the quantitative coefficient mass

Write V(beta)=product_(i<j)(beta_i-beta_j) for the full trace Vandermonde.
The complex root-to-monic-coefficient Jacobian has absolute determinant |V(beta)|.
For a direct determinant verification, differentiating Q at its roots gives the matrix product of the root-evaluation Vandermonde and the coefficient derivative matrix equal, up to signs and ordering, to diag(Q'(beta_i)); taking determinants leaves one Vandermonde factor.
For a conjugate pair beta=x+iy and conjugate(beta)=x-iy, the derivative of (beta,conjugate(beta)) with respect to (x,y) has determinant of absolute value 2.
Thus the real Jacobian on the chart is exactly 2^q|V(beta')|.
This also matches the root-Jacobian convention retained in L449v1.

Every pairwise difference changes by at most 2tau_N, so

\[
 \begin{split}
 |V(\beta')|
 &\ge\left(1-\frac{2\tau_N}{s_N}\right)^K|V(\beta)|\\
 &\ge\left(1-\frac1{4K}\right)^K\sqrt\Delta
 \ge\frac34\sqrt\Delta.
 \end{split} \tag{E}
\]

The last inequality is Bernoulli's inequality for the integer K>=1.
The map is injective and has nonzero Jacobian, so ordinary change of variables over the complete product domain gives

\[
 \begin{split}
 \operatorname{vol}U_P
 &\ge\frac34\,2^q\sqrt\Delta\,
       (2\tau_N)^{r_0}(2\sigma_N)^{r_1}
       (\pi\sigma_N^2)^q\\
 &\ge\frac34\,2^N\sqrt\Delta\,
       \tau_N^{r_0}\sigma_N^n.
 \end{split} \tag{F}
\]

In the second line the discarded factor is (pi/2)^q>=1.
The affine integral triangular coefficient map in L449v1 has determinant one, so (F) is unchanged in the N original independent nonleading reciprocal coefficients of P.
It is not ambient 2N-dimensional volume in the redundant full coefficient list.

Put

\[
 c_N=\min\{\tau_N,\eta_N/(8N)\},\qquad
 D_{N,n}=\frac34\,2^N\tau_N^{N-n}c_N^n.
\]

Because 0<epsilon<=1, the minimum in (B) satisfies sigma_N>=epsilon*c_N.
Using only sqrt(Delta)>=1 in (F) yields

\[
 \operatorname{vol}U_P\ge D_{N,n}\varepsilon^n. \tag{G}
\]

The exact lower bound (F) retains the actual discriminant and minimum radii, and can be stronger for an individual input.
No further uniform discriminant income is supplied here.

For N>=3 one has

\[
 \tau_N=c_N=\frac{8^{-K}}K,\qquad
 D_{N,n}=D_N:=\frac34\left(\frac{2\,8^{-K}}K\right)^N,
 \qquad
 \log D_N=-\frac{\log8}{2}N^3+O(N^2+N\log N).
 \tag{H}
\]

To check the minimum, the needed inequality is 8N*6^(N-1)<=K*8^K.
It holds at N=3, and the ratio of its right-to-left quotient at N+1 to that at N equals N*8^N/[6(N-1)]>1.
Hence 8^(-K)/K<=eta_N/(8N)<=eta_N/4 throughout N>=3.
The logarithmic estimate follows by inserting K=N(N-1)/2 into the displayed D_N, without a sharp root-separation theorem.
For N=2, the exact constants instead are tau_2=1/24 and c_2=1/96, and (A)--(G) remain valid.

<a id="thin-shell-stratum-comparison"></a>
## Comparison with the full thin shell

Use L449v1's v_N=vol B_N(0) and

\[
 A_N=\frac{N(N+1)(N+2)}6.
\]

Its complete Laplace expansion gives the upper bound g_N(u)-v_N<=v_N[cosh(sqrt(A_N)u)-1], where g_N(u)=vol B_N(u).
Thus, when 2sqrt(A_N)*epsilon<=1,

\[
 \begin{split}
 \operatorname{vol}(B_N(2\varepsilon)\setminus B_N(0))
 &\le v_N\{\cosh(2\sqrt{A_N}\varepsilon)-1\}\\
 &\le4v_NA_N\varepsilon^2.
 \end{split} \tag{I}
\]

The last step uses cosh(x)-1<=x^2 for 0<=x<=1, which follows by bounding its positive power series by x^2(cosh(1)-1)<x^2.
This is an explicit joint-parameter range, not an unqualified fixed-N asymptotic.
Combining (D), (G) and (I) gives, for N>=3,

\[
 D_N\varepsilon^n\le4v_NA_N\varepsilon^2. \tag{J}
\]

The same comparison holds with D_(2,n) for N=2.
The consequences for the active real dimension are as follows.

| Active dimension | Actual root types | Consequence of (J) |
| --- | --- | --- |
| n=1 | One exterior real trace root, no complex pair | epsilon>=D_N/(4v_NA_N), only a degree-dependent bound |
| n=2 | Two exterior real trace roots, or one nonreal conjugate pair | D_N<=4v_NA_N, with no remaining epsilon restriction |
| n>=3 | Any allowed combination with r_1+2q=n | epsilon^(n-2)<=4v_NA_N/D_N, which becomes easier to satisfy as epsilon decreases |

In the first row, L449v1's log v_N=-(N/2)log N+O(N) and (H) put the obtained lower threshold at logarithmic scale -(log 8)N^3/2+O(N^2+N log N).
The latter two rows do not hide a possible beneficial numerical constant: for N>=3 one has D_N<4v_NA_N.
Indeed v_N>=2^N/N!, and therefore

\[
 \frac{D_N}{4v_NA_N}
 \le\frac{3\tau_N^N N!}{16A_N}
 \le\frac{3(N\tau_N)^N}{16A_N}<1.
\]

For N=2, v_2=32/3 and A_2=4 from L449v1, while D_(2,n)<=3(1/24)^2<1, so the analogous coefficient comparison is also harmless.
These observations assess the explicit universally certified lower bound (G), not every possible use of the stronger input-specific factors in (F).
Outside the joint range of (I), this small-shell comparison is not asserted; the present construction has supplied no additional uniform exclusion there.

<a id="direct-endpoint-and-discriminant-controls"></a>
## Direct integer controls already dominate the useful row

Suppose there is an exterior real trace root beta=2cosh(u) or beta=-2cosh(u), with 0<u<=epsilon.
Choose the corresponding endpoint e=2 or e=-2.
The integer endpoint norm gives directly

\[
 1\le|Q(e)|
 \le(2\cosh\varepsilon-2)6^{N-1}
 \le2\varepsilon^2 6^{N-1},\qquad
 \varepsilon\ge(2\cdot6^{N-1})^{-1/2}.
 \tag{K}
\]

For the last inequality before the conclusion, use cosh(epsilon)-1<=epsilon^2 for epsilon<=1, as above.
This is already exponentially stronger in N than the n=1 local-volume threshold, using the same scalar arithmetic input and no continuous mass comparison.
The estimate applies whenever r_1>=1, not only to the n=1 stratum.

For completeness, if q>=1, choose for each upper-half-plane trace root a reciprocal quadratic root a with |a|=exp(u)>1 and write a=exp(u+i theta).
Then beta=a+a^(-1) and

\[
 |\beta-\overline\beta|=4\sinh u\,|\sin\theta|
 \le4\sinh\varepsilon\le5\varepsilon
 \qquad(0<\varepsilon\le1).
\]

Here sinh(epsilon)<=epsilon*sinh(1) follows from the positive odd power series, and 4sinh(1)<5.
In the complete Vandermonde product retain these q distinct conjugate-pair factors, and bound all K-q remaining factors by 8.
The discriminant integer gives

\[
 1\le\sqrt\Delta\le(5\varepsilon)^q8^{K-q},\qquad
 \varepsilon\ge\frac15\,8^{-(K-q)/q}.
 \tag{L}
\]

If there is no exterior real root, positivity requires q>=1, so (L) covers the remaining original inputs.
If all roots are real and interior, then m(P)=0 and the input is outside the positive hypothesis.
The omitted N=1 case is immediate: the monic integer trace polynomial has one integer root b, and positive measure requires |b|>=3, giving m(P)>=arcosh(3/2).
These elementary degree-dependent controls are not a uniform Mahler gap.

<a id="outcome-and-checks"></a>
## Outcome, checks and continuation boundary

The explicit construction attaches nonzero N-dimensional continuous coefficient mass to every actual positive original integer input while retaining all real and complex trace roots.
It pays both endpoints, every root collision, the conjugate-pair Jacobian and the original coefficient lattice.
The full positive-shell lower threshold in (D) excludes accidental use of the positive-volume zero-measure plateau.

After those payments, the universal lower mass in (G) has epsilon exponent n, whereas the full shell upper bound in (I) has exponent 2 in its declared joint range.
Only n=1 yields an epsilon lower bound, and that bound is already weaker than (K).
The other strata do not produce a useful small-measure exclusion through (J).
No all-real-trace reduction is available to discard them.

This bounded failure does not prove that a larger structured neighborhood, a different controlled shape, or additional arithmetic information cannot succeed.
Nor does decay of the particular lower bound prove that every possible lower bound must decay at that rate.
A useful reopening should first supply a concrete new original-input constraint capable of improving the simultaneous radii, full Jacobian income or allowed shape after the Mahler cost is paid.
The present calculation supplies no reason to optimize generic separation constants, repeat endpoint nonvanishing, or promote a Salem-only comparison to the unrestricted domain.

The author checked the integer floors, all-root measure normalization, the complete root-stratum coverage, the holomorphic-branch Lipschitz estimate, chart injection, conjugate-pair factor 2^q, pairwise Vandermonde perturbation, both positive-shell thresholds, every minimum in the radii, the n=1/2/>2 comparison and the direct controls (K)--(L).
The N=2 constants and the N=1 boundary are exact hand substitutions.
No numerical enumeration, new external theorem audit, independent mathematical review or C/R registration is claimed.
