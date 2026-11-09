---
author: Yin
---

# Exceptional-root localization and admissible double-atom models

<a id="statement"></a>
## Complete mathematical assertions

### Exact setting and the residual quadratic

Use \(p=19683\), \(n=9841\), \(m=7851\), \(k=1990\), and decreasing poles \(b_j=2\cos(2\pi j/p)\).
Let \(B_0=1\), \(B_1=t+1\), \(B_i=tB_{i-1}-B_{i-2}\), and put \(B=B_n=\prod_{j=1}^n(t-b_j)\), \(D=B_{n-1}\).
Let \(h\in\mathbb Z[t]\) be positive at \(b_1,\ldots,b_m\), negative at \(b_{m+1},\ldots,b_n\), and satisfy \(\prod_j|h(b_j)|=2^{4391}\).
Set
\[
 r_j=(4-b_j^2)h(b_j)/p,\qquad C=Dh\bmod B,\qquad
 Q=(t+2)B+C,\qquad P(z)=z^{n+1}Q(z+z^{-1}).
\]
Assume \(K=\sum r_j=3\), \(L=\sum b_jr_j=4\), \(N=\sum b_j^2r_j=7\), and \(P(-1)>0\).
The inherited endpoint consequence is \(U=\sum r_j/(2+b_j)=1\).

Choose one real root of \(Q\) in each adjacent same-sign pole interval and one in \((-2,b_n)\), as in [C882v6](Yin_C_G0882_v6.md#whole-measure).
These are \(n-1\) distinct chosen roots \(u_1,\ldots,u_{n-1}\), and define
\[
 F(t)=\prod_{i=1}^{n-1}(t-u_i),\qquad Z(t)=Q(t)/F(t).
\]
Then \(Z\) is a real monic quadratic and
\[
                    Z(b_j)>0\quad(1\le j\le n),\qquad Z(-2)>0.
 \tag{1}
\]
This holds for every such choice of the mandatory roots, with all original root multiplicities retained.

If the two roots \(v_1,v_2\) of \(Z\) are real, both belong to the same connected component of
\[
             \mathbb R\setminus\{-2,b_n,b_{n-1},\ldots,b_1\}.
 \tag{2}
\]
They may coincide with each other or with a chosen root, but neither can equal a pole or \(-2\).
For \(R\ge1\), assume \(M(P)\le R\) and write \(A_R=R+R^{-1}\).
Each root satisfies \(|v_i|\le A_R\).
For real roots their separation satisfies the following bounds according to their common component:
\[
 |v_1-v_2|\le
 \begin{cases}
 A_R-2,&(-\infty,-2),\\
 4\pi/p,&\text{a bounded component between }-2\text{ and }b_1,\\
 A_R-b_1=(A_R-2)+(2-b_1),&(b_1,\infty).
 \end{cases}
 \tag{3}
\]
The left component is impossible when \(R=1\).
For a nonreal pair the two roots are conjugate, share their real part, and satisfy
\[
             |\operatorname{Im}v_i|\le\sqrt R-1/\sqrt R.
 \tag{4}
\]

<a id="diagonal-statement"></a>
### Five exact double-atom models

Retain the exact residual triples and cut interval of [C882v6](Yin_C_G0882_v6.md#statement):
\[
 \mathcal R=\{(10,18,27),(11,20,33),(11,20,34),(11,21,36),(11,21,37)\},
 \qquad I=[-1609663/10^6,-1609662/10^6].
\]
For each triple define \(\mathcal D\) on polynomials of degree at most seven by
\[
\begin{split}
 \mathcal D(1)&=1,\qquad
 \mathcal D(t)=\mathcal D(t^2)=\mathcal D(t^3)=-2,\qquad
 \mathcal D(t^4)=-10,\\
 \mathcal D(t^5)&=48-5O,\qquad
 \mathcal D(t^6)=-44+12O-6V,\qquad
 \mathcal D(t^7)=-7O+14V-7W-2.
\end{split}
\]
These are the inherited trace differences, not additional prescribed residue moments.
Use the following fixed locations:

| \((O,V,W)\) | \(s\) |
| --- | --- |
| \((10,18,27)\) | \(-15/16\) |
| \((11,20,33)\) | \(-31/32\) |
| \((11,20,34)\) | \(-31/32\) |
| \((11,21,36)\) | \(-17/16\) |
| \((11,21,37)\) | \(-17/16\) |

For every \(c\in I\), there exists a step function \(w_c:[-2,2]\to[0,1]\), constant on the 256 cells with endpoints \(t_i=-2+i/64\), such that simultaneously for every real polynomial \(f\) of degree at most seven,
\[
        \mathcal D(f)+f(c)=2f(s)-\int_{-2}^2w_c(t)f'(t)\,dt.
 \tag{5}
\]
Each location lies in \((-2,2)\), is distinct from every actual pole and from \(-2\), and gives
\[
                Z_s(t)=(t-s)^2>0\quad
                \text{at }t=-2,b_n,\ldots,b_1.
 \tag{6}
\]
Thus these relaxed models retain two unit atoms at a common location, satisfy the strict quadratic pole signs, and obey the real-root same-component condition with separation zero.
Their two reciprocal trace lifts have exterior radii one.
They do not reconstruct \(Q\), the mandatory root factors or an integral \(h\), and do not assert \(M(P)=1\) for an original input.

## Inputs and computation boundary

[C882v6](Yin_C_G0882_v6.md#statement) supplies the original input scope, \(U=1\), the five-triple residual restriction and the functional \(\mathcal D\).
Its [complete-root argument](Yin_C_G0882_v6.md#whole-measure) supplies existence of the mandatory roots and the complete-measure interpretation of the remaining two reciprocal pairs.
Its [cut enclosure](Yin_C_G0882_v6.md#relaxation-barrier) places the actual unpaired pole \(b_{7851}\) in the interior of \(I\).
[C882v7](Yin_C_G0882_v7.md#statement) is the preceding comparison with distinct unit atoms; its existence statement is not used to infer (5).

[J151 diagonal certificate program](../computations/programs/Yin_J_G0151/diagonal_atom_scan.py) supplies the five exact `MODELS` rows, seven free occupancy columns per row, all fixed-one columns and the default rational verifier.
Its default verifies all forty control systems, strict coordinate bounds, exact five-triple coverage, and nonvanishing of \(B(s)\).
The existing J151 polynomial and cut helpers are retained unchanged.
The optional 129-position LP scan is exploratory; numerical feasibility and numerical failure are not proof premises.
The [independent complete finding](../audits/reviews/Yin_R_G1107_v21.md#diagonal-localization-review) checks the localization argument and all five exact diagonal models; the assessment below adopts that precise scope.

<a id="quadratic-signs"></a>
## Signs at every pole and the strict endpoint

The residue identity is \(Q/B=t+2+\sum_jr_j/(t-b_j)\), so
\[
                 Q(b_j)=r_jB'(b_j).
\]
Because the poles decrease with \(j\), \(\operatorname{sgn}B'(b_j)=(-1)^{j-1}\).
There are exactly \(j-1\) chosen mandatory roots above \(b_j\) when \(j\le m\), and exactly \(j-2\) when \(j>m\).
Indeed the positive-residue block supplies \(m-1\) intervening roots, the negative-residue block supplies \(n-m-1\), and the left endpoint supplies one root below all poles; the sign-changing interval supplies none of the chosen roots.
The counts depend only on their disjoint intervals, not on any additional roots or multiplicities of \(Q\).
Since \(F\) is monic, these counts give
\[
 \operatorname{sgn}F(b_j)=
 \begin{cases}
 (-1)^{j-1},&j\le m,\\
 (-1)^{j-2},&j>m.
 \end{cases}
\]
These are exactly the signs of \(r_jB'(b_j)\), because \(r_j\) changes from positive to negative after \(m\).
Neither numerator nor denominator vanishes at a pole, proving \(Z(b_j)>0\).

At the strict endpoint, \(Q(-2)/B(-2)=-U=-1\).
All poles and chosen roots exceed \(-2\), so \(\operatorname{sgn}B(-2)=(-1)^n\) and \(\operatorname{sgn}F(-2)=(-1)^{n-1}\).
Consequently \(Z(-2)=Q(-2)/F(-2)>0\), proving (1).
The distinct chosen real roots make \(F\) a divisor of \(Q\) over \(\mathbb R\); removing one copy at each preserves any extra multiplicity in the real monic quadratic quotient.
In particular, the proof does not assume that \(Q\) is squarefree.

<a id="root-location"></a>
## Location and complete-measure bounds

If \(Z(t)=(t-\alpha)(t-\beta)\) with real \(\alpha\le\beta\), then a test point between distinct roots gives a nonpositive value, and a test point equal to a repeated root gives zero.
Strict positivity at every point of \(\{-2,b_n,\ldots,b_1\}\) therefore puts \(\alpha,\beta\) in the same component of its complement and excludes equality with any removed point.
This argument includes a double root; it also allows coincidence with a chosen root, which merely increases the original multiplicity in \(Q\).

Let \(\rho_i\ge1\) be the exterior radius of the reciprocal pair lifting \(v_i\).
All chosen mandatory roots lie in \((-2,2)\) and lift to the unit circle, so the complete measure is \(M(P)=\rho_1\rho_2\).
For \(v_i=\rho_i e^{\mathrm i\theta_i}+\rho_i^{-1}e^{-\mathrm i\theta_i}\),
\[
 |v_i|\le\rho_i+\rho_i^{-1}\le R+R^{-1}
\]
whenever \(M(P)\le R\), since \(1\le\rho_i\le R\).
For real roots in the two unbounded components this gives the first and third bounds in (3).
The left component is empty inside the allowed real interval when \(R=1\).

Adjacent interior poles have angular separation \(2\pi/p\), and the derivative of \(2\cos\theta\) has absolute value at most two, so \(b_j-b_{j+1}\le4\pi/p\).
The additional leftmost bounded component has width \(b_n+2=2(1-\cos(\pi/p))\le2\pi/p\), and hence also satisfies the displayed bound.
Thus every bounded component in (2) has width at most \(4\pi/p\), proving the middle case of (3).
The rightmost width has the exact additional term \(2-b_1\); it cannot be replaced by an interior-gap bound without also controlling the exterior radial term.

If the roots are nonreal, the real coefficients of \(Z\) make them conjugate.
Their exterior reciprocal lifts consequently have equal radii \(\rho\), so \(M(P)=\rho^2\) and \(\rho\le\sqrt R\).
They share their real part, and
\[
 |\operatorname{Im}v_i|
   =|(\rho-\rho^{-1})\sin\theta_i|
   \le\sqrt R-1/\sqrt R,
\]
proving (4).
No nonreal hypothesis was used in the earlier real-root analysis or in the complete product formula.

<a id="diagonal-certificate"></a>
## Exact common-location models on the whole cut interval

Fix one row of the diagonal table and let \(q_j=T_j\) for \(1\le j\le7\), with \(T_j(z+z^{-1})=z^j+z^{-j}\).
The seven-row, 256-column occupancy matrix and right side are
\[
 A_{j,i}=q_j(t_i)-q_j(t_{i+1}),\qquad
 g_j(c)=\mathcal D(q_j)+q_j(c)-2q_j(s).
\]
The constant-polynomial equation is identically \(\mathcal D(1)+1=2\).
Each occupancy column is the negative integral of \(q_j'\) over its cell, so \(A\omega=g(c)\) is exactly (5) on the seven nonconstant basis elements.
The factor two fixes two unit masses at the same location and introduces no free atomic weight.

Write \(c=c_0+10^{-6}u\), with \(c_0=-1609663/10^6\) and \(0\le u\le1\).
Expand the right side in the degree-seven Bernstein basis:
\[
 g(c_0+10^{-6}u)=\sum_{r=0}^7g^{(r)}\binom7r u^r(1-u)^{7-r}.
\]
If a component has shifted monomial coefficients \(A_j\), its \(r\)-th Bernstein control is \(\sum_{j=0}^rA_j\binom rj/\binom7j\).
Thus every control is rational, including the constant subtraction \(2q_j(s)\).

For each row, the fixed native data specify seven free columns and a disjoint set of columns fixed at one; all other coordinates are zero.
Subtract the fixed-one columns from each \(g^{(r)}\) and solve for the seven free coordinates.
The default verifier performs exact elimination and direct substitution for all forty \(7\times7\) systems.
Every free control value satisfies
\[
                    1/10<\omega_i^{(r)}<999/1000.
\]
Reinserting the fixed zero and one coordinates gives solutions \(\omega^{(r)}\in[0,1]^{256}\).
Their Bernstein convex combination stays in that cube and solves \(A\omega(c)=g(c)\) for every \(c\in I\).
Defining \(w_c\) by these cell occupancies proves (5) for the basis \(1,T_1,\ldots,T_7\), and hence simultaneously for every real polynomial of degree at most seven.

All retained \(s\) are nonintegral rationals in \((-2,2)\).
Since \(B\) is monic integral, none is a root of \(B\); equivalently, the native scaled integer recurrence verifies \(B(s)\ne0\).
They are also different from \(-2\), proving (6).
The double root has separation zero and belongs to a single allowed component, while \(z^2-sz+1\) has both roots on the unit circle.
This verifies the claimed sign and location compatibility at radial cost zero.

The same rational-root observation also shows that these particular \(s\) cannot be roots of an actual monic integral \(Q\).
The models are exact feasibility certificates for the stated moment-and-occupancy relaxation, including its restored quadratic signs and root clustering, not integer-polynomial witnesses.
The fractional occupancies need not be indicators of actual root-to-pole intervals, and the full integer and resultant constraints remain outside the model.
No claim about an original residual branch being realizable or impossible follows from these certificates.

## Assessment history

### Decision diagonal-localization-19683

| Field | Value |
| --- | --- |
| date | 2026-11-09T14:43 |
| status | proved |
| reason | Complete independent review verifies all original-input quadratic signs and root bounds, and all five whole-interval diagonal certificates by a separate rational reconstruction; actual integer realization remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete localization and diagonal-model statement](#statement) | Every allowed root selection and multiplicity, strict signs, all complete-Mahler root bounds, and all five fixed residual triples with common unit-atom locations, all cut positions and all real tests of degree at most seven. |
| argument | [Quadratic signs](#quadratic-signs) | Exact pole and endpoint signs without a squarefreeness assumption. |
| argument | [Root location](#root-location) | All bounded and exterior components, full radius product and conjugate-height bound. |
| argument | [Whole-interval certificates](#diagonal-certificate) | Forty rational systems, strict control bounds, Bernstein convex combinations, non-pole locations and original-realization limits. |
| dependency | [Inherited input and functional](Yin_C_G0882_v6.md#statement) | Exact original scope, endpoint consequence and five residual data sets. |
| dependency | [Complete-root interpretation](Yin_C_G0882_v6.md#whole-measure) | Mandatory roots, original multiplicities and the full Mahler product. |
| dependency | [Actual cut enclosure](Yin_C_G0882_v6.md#relaxation-barrier) | Inclusion of the unpaired pole in the fixed interval. |
| dependency | [Native exact diagonal data](../computations/programs/Yin_J_G0151/diagonal_atom_scan.py) | Five retained MODELS rows, all forty exact systems and necessary inherited helpers; no historical LP status as proof. |
| review | [Independent complete finding](../audits/reviews/Yin_R_G1107_v21.md#diagonal-localization-review) | Whole C/L/J assembly, complete default verification and independent monomial-basis rational reconstruction, with the historical-scan limit retained. |

## Current assessment

[Selected decision](#decision-diagonal-localization-19683)
