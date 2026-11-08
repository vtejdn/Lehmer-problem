---
author: Yin
---

# A moving rational cut and the cost of clearing its denominator

For the [original Chebyshev-grid construction](Yin_L_G0462_v2.md#moving-sign-test), the [cyclotomic control](Yin_L_G0464_v3.md#central-control) places the transition at zero.
The following integral family places it beyond an unbounded number of positive grid points and has exactly one nonreal trace pair.
A delegated AI agent derived and self-checked the construction and the obstruction for numerators of varying degree for Yin on 2026-11-08.

<a id="moving-rational-family"></a>
## An integral family crossing exactly \(2m\) positive grid points

Write \(U_k\) for the Chebyshev polynomial of the second kind and set
\[
 B(t)=U_{d-1}(t/2),\quad D(t)=U_{d-2}(t/2),\quad G(t)=D(t)/B(t),\quad
 b_j=2\cos\theta_j,\quad \theta_j=j\pi/d,\quad w_j=2\sin^2\theta_j/d
 \qquad(1\le j<d).
\]
The sine formula gives \(D(b_j)=(-1)^{j+1}\), \(B'(b_j)=(-1)^{j+1}/w_j\), and \(G(t)=\sum_j w_j/(t-b_j)\).
Discrete sine orthogonality gives \(\sum_jw_j=1\), \(\sum_jw_j b_j=0\) and \(\sum_jw_j b_j^2=1\) for \(d\ge3\).
For any \(h\in\mathbb Z[t]\) let \(C\) be the remainder of \(Dh\) on division by \(B\), take \(Q=tB+C\), and form the original monic reciprocal polynomial \(P(z)=z^dQ(z+z^{-1})\).
Then \(Q/B=t+\sum_j r_j/(t-b_j)\), with \(r_j=w_j h(b_j)\).

For integers \(m\) tending to infinity put
\[
 d=4\lfloor\pi m^2\rfloor+1,\qquad n=d-1,\qquad
 c=1/m,\qquad u=m^n B(c),\qquad s=u/m .
\]
Write \(\theta_c=\arccos(c/2)=\pi/2-\delta_m\).
Taylor's formula gives \(d\delta_m=d\arcsin(1/(2m))=2\pi m+O(m^{-1})\).
Since \(d\equiv1\pmod4\), the sine formula gives \(B(c)=\cos(d\delta_m)/\sin\theta_c\to1\) and \(G(c)=\cos\theta_c-\sin\theta_c\tan(d\delta_m)=O(m^{-1})\).
In particular \(u>0\) for all sufficiently large \(m\), and \(s\sim m^{d-2}\).
The angular index \(d\theta_c/\pi=d/2-2m+O(m^{-1})\) stays a distance \(1/2+O(m^{-1})\) from the nearest integer.
Exactly \(2m\) grid points lie strictly between \(0\) and \(c\) for all sufficiently large \(m\).

Choose the integral polynomial
\[
 h(t)=(2+t)^2\,\frac{u-m^nB(t)}{mt-1}.
\]
Indeed each term \(m^n(c^\ell-t^\ell)/(mt-1)\) of the quotient, for \(1\le\ell\le n\), equals \(-m^{n-\ell}\sum_{v=0}^{\ell-1}(mt)^v\).
The residues on the original grid are therefore
\[
 r_j=s\,w_j\,\frac{(2+b_j)^2}{b_j-c}.
\]
They are strictly negative below \(c\) and strictly positive above it.
Their weighted total, signed total \(K\), and original left endpoint value are
\[
 \sum_j(b_j-c)r_j=5s,\qquad
 K=\sum_jr_j=s\big[4+c-(2+c)^2G(c)\big]\sim4s,\qquad
 \frac{Q(-2)}{B(-2)}=-2-s\big[1-(2+c)G(c)\big]<0
\]
for large \(m\), by polynomial division in \(b_j-c\) and the preceding three discrete moments.

<a id="variation-and-whole-measure"></a>
## Variation and both exceptional roots of the same polynomial

The total variation \(V=\sum_j|r_j|\) satisfies
\[
 \frac{V}{s}
   =\frac{2\sin\theta_c(2+c)^2}{\pi}\log d+O(1)
   \sim \frac8\pi\log d .
\]
Indeed the function \(2\sin^2\theta(2+2\cos\theta)^2/|2\cos\theta-c|\) differs from \(\sin\theta_c(2+c)^2/|\theta-\theta_c|\) by a uniformly bounded amount on \(0\le\theta\le\pi\), \(\theta\ne\theta_c\).
This follows from Taylor expansion in a fixed neighborhood of \(\pi/2\) and separation from the denominator zero on its complement.
The average of the singular term on the grid involves \(\sum_{j=1}^{d-1}|j-d\theta_c/\pi|^{-1}=2\log d+O(1)\), by comparison on each side with the harmonic sum, using the half-grid separation above.

At every same-sign gap \(Q/B\) has opposite infinite one-sided limits, and the left endpoint sign supplies another real zero to the left of the smallest pole.
These intervals give \(d-2\) distinct zeros in \((-2,2)\).
For complex \(t\) with \(|t|>2\), the partial fractions give
\[
 \left|\frac{Q(t)}{B(t)}-t-\frac Kt\right|
     \le \frac{2V}{|t|(|t|-2)} .
\]
Consequently \(Q(\sqrt K\,v)/(\sqrt K\,B(\sqrt K\,v))\) tends uniformly to \(v+1/v\) on each closed disk of radius less than \(1/2\) centered at \(i\) or \(-i\), with error \(O(V/K^{3/2})=O(\log d/\sqrt{s})\).
The rescaled poles are real, and the limiting function has a simple zero in each disk and no boundary zero.
Rouché's theorem on each boundary gives the remaining two zeros \(q,\bar q\), with \(q/\sqrt K\to i\).
All the \(d-2\) real trace roots lift to the unit circle.
The exterior lift \(\lambda+\lambda^{-1}=q\) has \(\lambda/q\to1\), and its conjugate accounts for the other exterior root.
The whole multiplicative Mahler measure is
\[
                     M(P)=|\lambda|^2\sim K\sim4m^{d-2}.
\]
Thus the moving cut, growing variation and strictly positive log measure occur on the same original polynomial, and the nonreal pair leaves every fixed exterior ellipse.

<a id="fixed-numerator-obstruction"></a>
<a id="numerator-degree-obstruction"></a>
## A uniform lower bound in terms of numerator degree

Take any \(W\in\mathbb Z[t]\) of degree \(0\le k\le d-2\), allowing its degree and coefficients to vary with the original grid.
Allow any reduced \(c=p/q\in(-2,2)\) with \(q\ge2\), any \(N\in\mathbb Z_{>0}\), and any \(h\in\mathbb Z[t]\) satisfying
\[
                 (qt-p)h(t)\equiv N W(t)\pmod{B(t)} .
\]
Require \(W(c)\ne0\), both sign blocks to be nonempty, and \(W(b_j)>0\) at every pole.
Allow any integer \(a\) in \(Q=(t-a)B+\operatorname{rem}_B(Dh)\), with \(Q(-2)/B(-2)<0\), and use its own lift \(P\).
There is an absolute constant \(C_0\) such that
\[
                         q^{\,d-k-2}\le C_0 (k+1)^3 M(P)^3 .
\]
For bounded \(M(P)\) this requires \(d-k-2=O(\log(d)/\log(q))\) as \(d\to\infty\), independently of how closely \(c\) approaches a grid point.
In particular every fixed numerator fails the fixed-ellipse construction, and \(q\ge d^\varepsilon\) with fixed \(\varepsilon>0\) allows at most a bounded degree deficit.

Let \(n=d-1\), \(u=q^nB(c)\ne0\), and \(g=q^kW(c)\ne0\).
The nonintegral rational \(c\) cannot be a root of the monic integral \(B\), and \(u\equiv p^n\pmod q\).
Evaluating the congruence in \(\mathbb Z[1/q]\) shows \(u\mid Ng\) there and hence in \(\mathbb Z\), since \(\gcd(u,q)=1\).
Evaluation at \(c\) identifies \(\mathbb Z[t]/(qt-p)\) with \(\mathbb Z[1/q]\) by primitivity and Bézout's identity for \(p,q\).
Passing to the quotient by \(B\) gives \(\mathbb Z[t]/(qt-p,B)\cong\mathbb Z[1/q]/(u)\cong\mathbb Z/|u|\mathbb Z\).
Thus the smallest admissible positive scalar in the displayed congruence is \(|u|/\gcd(|u|,|g|)\).

Write \(M=M(P)\), \(r_j=(N/q)w_jW(b_j)/(b_j-c)\), \(K=\sum_jr_j\), and \(J=\sum_j b_j r_j\).
The [matching and Newton-sum identities](Yin_L_G0462_v2.md#central-sign-test) give \(|a|\ll M\), \(|K|\ll M^2\), and \(|J|\ll M^3\).
Indeed the disjoint interior matches contribute bounded errors to each of the first three trace-power differences, the unmatched pole has absolute value at most two, and each of the two remaining trace roots has absolute value at most \(M+1\) by its reciprocal lift.
The identities \(a=\Delta_1\), \(2K=a^2-\Delta_2\), \(3J=a^3-3aK-\Delta_3\) then give the stated bounds.
Set \(\widetilde W=(N/q)W\) and \(T=\sum_j w_j\widetilde W(b_j)=J-cK\), so \(0<T\ll M^3\).
Write \(E_\ell(t)=U_\ell(t/2)\).
Discrete sine orthogonality on this grid gives \(\sum_jw_j E_\ell(b_j)E_h(b_j)=\mathbf 1_{\ell=h}\) for \(0\le\ell,h\le d-2\).
Hence \(\widetilde W=\sum_{\ell=0}^k A_\ell E_\ell\) has \(|A_\ell|=|\sum_jw_j\widetilde W(b_j)E_\ell(b_j)|\le(\ell+1)T\), since \(|E_\ell|\le\ell+1\) on \([-2,2]\) and \(\widetilde W\) is positive at every pole.
It follows that \(|\widetilde W(c)|\le(k+1)^3T\).

For a polynomial \(f\) write \(L_c(f)=\sum_jw_j(f(b_j)-f(c))/(b_j-c)\).
One has \(L_c(E_0)=0\), \(L_c(E_1)=1\), and \(L_c(E_\ell)=E_{\ell-1}(c)\) for \(1\le\ell\le d-2\).
Indeed \(L_c(tE_\ell)=\sum_j w_j E_\ell(b_j)+cL_c(E_\ell)\), the sum vanishes for \(1\le\ell\le d-2\), and the Chebyshev recurrence proves the formula.
The same coefficient bound now gives \(|L_c(\widetilde W)|\le(k+1)^3 T\).
Using \(\sum_jw_j/(b_j-c)=-G(c)\), the identity \(K=L_c(\widetilde W)-\widetilde W(c)G(c)\) yields
\[
 |\widetilde W(c)|+|\widetilde W(c)G(c)|\ll (k+1)^3 M^3 .
\]
The nonzero integer \(Ng/u\) has absolute value at least one.
Consequently
\[
 q^{n-k-1}|B(c)|\le (N/q)|W(c)|,\qquad
 q^{n-k-1}|D(c)|\le (N/q)|W(c)G(c)|.
\]
The two right sides are \(|\widetilde W(c)|\) and \(|\widetilde W(c)G(c)|\).
The Chebyshev recurrence gives \(B(c)^2+D(c)^2-cB(c)D(c)=1\), which implies \(|B(c)|+|D(c)|\ge1\) for \(|c|<2\).
Adding the two estimates proves the claimed degree-dependent lower bound, including the minimum scalar allowed by integrality.
The construction above has \(W(t)=(2+t)^2\).
When \(W(c)=0\), the primitive factor \(qt-p\) already divides \(W\) in \(\mathbb Z[t]\), and the nonzero integer \(Ng/u\) used in this estimate is absent.
