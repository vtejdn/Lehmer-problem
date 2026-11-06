---
author: Yin
---

# Moving sparse mixed maps: reciprocal factors, norm-one candidates and local splitting limits

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The construction contributor developed the factorwise involution, real-root and unit-norm restrictions.
The coordinating contributor selected the sublinear-factor question and its real-root and fixed-unit-group refinements.
The bottleneck contributor checked finite-order, rotation, commuting-map and residue-field splitting constructions.
The source contributor investigated stronger number-field factorization statements at their actual hypotheses.
These are ordinary author-development contributions, not an independent project review, an accepted Claim or a resolution of the Task.

<a id="moving-map-factor-structure-scope"></a>
## Inputs and the remaining construction target

The complete input, normalization, source properties and height argument remain fixed in [v5](Yin_L_G0450_v5.md#moving-map-actual-inputs).
For odd n>=3, they are
\[
 g_n=z^n-z-1,\quad g_n^*=1-z^{n-1}-z^n,\quad
 F_n=g_n^{10}P_L(g_n^*/g_n),
\]
where P_L is the degree-ten Lehmer polynomial and alpha=lambda>1 is its real root.
Put
\[
 K=\mathbb Q(\alpha),\quad u=(1+\alpha)^{-1},\quad a=1-u,\quad
 q_{n,u}=z^{n-1}(z+u)-(az+1),\quad
 T_u(z)=\frac{az+1}{z+u}.                             \tag{F1}
\]
The involution tau of K sends alpha to alpha^(-1), hence u to a.
The field has signature (2,4); its tau-fixed trace field is totally real of degree five.
In particular tau becomes complex conjugation at each nonreal embedding of K.

[V5](Yin_L_G0450_v5.md#moving-map-integral-mobius-height) proves that u, a and au-1 are units of O_K, and that a root beta of the fixed fiber satisfies beta^(n-1)=T_u(beta).
It also proves that all roots of F_n are nonzero nontorsion algebraic units and that
\[
 \deg F_n=10n,\quad F_n(0)=1,\quad
 F_n(1)=-1,\quad F_n(-1)=1,\quad
 m(F_n)\le B:=\log(9\cdot3^{10}).                     \tag{F2}
\]
For every actual irreducible rational factor f, the [uniform asymptotic](Yin_L_G0450_v5.md#moving-map-uniform-asymptotic) gives
\[
 m(f)=\frac{\deg f}{n-2}(E+o(1)),\qquad E>0.           \tag{F3}
\]
Thus the remaining counterexample construction must supply actual factors of degree o(n).
The present work restricts such factors and tests concrete ways to force them; it supplies neither their existence nor a proportional lower degree bound.

<a id="moving-map-factorwise-involution"></a>
## One circle embedding controls every actual factor

The source trace polynomial is
\[
 Q(y)=y^5+y^4-5y^3-5y^2+4y+3,\qquad P_L(z)=z^5Q(z+z^{-1}).
\]
Since Q(0)=3 and Q(1)=-1, there is a circle-source embedding sigma with trace y in (0,1).
For w=sigma(u), direct calculation gives
\[
 \operatorname{Re}w=\tfrac12,\qquad
 |w|=(2+y)^{-1/2}<1,\qquad \sigma(a)=\overline w.
\]
Under this embedding the fiber equation is
\[
                       z^{n-1}\frac{z+w}{1+\overline w z}=1. \tag{F4}
\]
The left side is a degree-n finite Blaschke product.
It has modulus less than one inside the circle and greater than one outside, away from its poles, so all solutions of (F4) lie on the circle.
There is no solution at a pole, since 1-|w|^2 is nonzero.
On the circle its argument derivative is
\[
                     n-1+\frac{1-|w|^2}{|z+w|^2}>0. \tag{F5}
\]
Its winding number is n, so it takes the value one at exactly n simple points.
This accounts for the entire degree-n polynomial, rather than only selected circle roots.

Let p be any monic K-factor of q_(n,u), with degree r and constant coefficient c.
All roots of sigma(p) are on the circle.
Writing star for ordinary degree reversal gives
\[
 \sigma(p^*)=\sigma(c)\overline{\sigma(p)}.
\]
Here the bar on a polynomial conjugates its coefficients.
Since conjugation of sigma(x) equals sigma(tau(x)) for x in K, injectivity of sigma gives
\[
                         p^*=c\,\tau(p),\qquad c\,\tau(c)=1. \tag{F6}
\]
This applies before assuming c is plus or minus one.
It is the factorwise field-involution relation, not ordinary reciprocity of p over K.

The same embedding proves that q_(n,u) is squarefree.
Distinct source embeddings give disjoint fibers: a common root would have two different values for R_n=g_n*/g_n, whose denominator does not vanish at any output root.
Consequently F_n is squarefree for every odd n>=3.

For an irreducible p with root beta, R_n(beta)=alpha implies K is contained in Q(beta), so the rational minimal polynomial f has degree 10r.
It divides the monic polynomial N_(K/Q)(p), which also has degree 10r, and hence
\[
                             f=N_{K/\mathbb Q}(p).     \tag{F7}
\]
Every irreducible rational factor arises this way by choosing a conjugate root above alpha.
There is only one K-orbit in that fiber for a given rational factor: an automorphism taking two roots above alpha to one another fixes alpha and therefore K.
Thus this is a bijection between the actual K-factors and rational factors.

Taking norms in (F6), using N_(K/Q)c=N_(K^tau/Q)(c tau(c))=1 and the invariance of the norm under tau, gives
\[
                               f^*=f,\qquad f(0)=1.  \tag{F8}
\]
Every actual irreducible rational factor is itself reciprocal, rather than occurring merely as one member of a pair of different reciprocal factors.

<a id="moving-map-positive-relative-norm"></a>
## Real roots and the positive relative norm

At either real embedding, u and a lie strictly between zero and one and a+u=1.
For t>=0,
\[
                   q_{n,u}(-t)=-t^n+ut^{n-1}+at-1<0. \tag{F9}
\]
For 0<t<=1, use ut^(n-1)+at<=u+a=1 and the negative term -t^n; t=0 is direct.
For t>=1, t-u>=at gives
\[
 -t^{n-1}(t-u)+at-1\le-at^n+at-1<0.
\]
Thus there are no negative real roots.
The nonzero coefficient signs of q_(n,u) are +,+,-,-, so Descartes' rule and the endpoint signs at zero and positive infinity give exactly one positive real root.
All other roots occur in complex-conjugate pairs at that real embedding.

For an actual irreducible p, the relative root product
\[
                    \gamma=N_{\mathbb Q(\beta)/K}(\beta)=(-1)^r c
\]
is therefore positive at both real embeddings.
In particular v5's necessary torsion-norm condition for r=o(n) sharpens to
\[
                            \gamma=1,\qquad c=(-1)^r \tag{F10}
\]
eventually.
The negative torsion option is unavailable.

At the chosen embedding u<1/2, q_(n,u)(1)=2u-1<0, so its unique positive root exceeds one.
At the other real embedding tau(u)>1/2, the unique positive root lies between zero and one.
They are reciprocal by q_(n,u)*=-tau(q_(n,u)).

There are no further real roots of F_n.
Indeed a real root beta in a source fiber determines
\[
             \sigma(u)=\frac{\beta+1-\beta^n}{\beta^{n-1}+\beta}. \tag{F11}
\]
The real zeros of the denominator are 0 and -1, both excluded by (F2).
The right side is real, so sigma(u), and hence sigma(alpha), is real.
Only the two real source embeddings can contribute.
The output therefore has exactly two positive real roots, reciprocal to one another, and (F8) places them in the same rational irreducible factor.
All other rational factors have no real roots.
Equivalently, q_(n,u) has exactly one odd-degree irreducible K-factor, and all its other irreducible K-factors have even degree.
None of this asserts that the factor containing the real pair is a Salem polynomial: it may have further nonreal roots off the circle.

<a id="moving-map-relative-unit-balance"></a>
## One fixed unit group and the complete norm budget

From (F6), gamma tau(gamma)=1.
At every nonreal embedding this says |sigma(gamma)|=1.
Together with (F9), the unit logarithm vector has the form
\[
                             (\log\gamma,-\log\gamma,0,\ldots,0). \tag{F12}
\]
Consider the group of O_K-units having this norm-one relation and positive values at both real embeddings.
Its logarithms on the first real embedding form a discrete additive subgroup of R.
This is the [fixed unit-line argument](Yin_L_G0450_v1.md#unit-ray-saturation); alternatively bounded logarithms here bound all conjugates, hence bound the coefficients of integer minimal polynomials of degree at most ten and leave only finitely many elements.
The logarithm map on this positive group has trivial kernel: an element with actual real value one is the element one.

The group contains alpha=lambda>1 and is therefore nontrivial.
Its positive logarithms have a least positive generator, giving a fixed unit epsilon>1 such that
\[
                \gamma=\varepsilon^t,\quad t\in\mathbb Z,\qquad
                \lambda=\varepsilon^s,\quad s\in\mathbb Z_{>0}. \tag{F13}
\]
No fundamental-unit computation or effective value for epsilon is asserted.
The only conjugate modulus greater than one in the ten-embedding height formula for epsilon is its first real value, so 10h(epsilon)=log epsilon.

Let p_i be all actual irreducible K-factors and t_i their exponents in (F13).
The complete q_(n,u) has root product one, so
\[
                                    \sum_i t_i=0.     \tag{F14}
\]
For the corresponding rational factor f_i, subadditivity of absolute height applied to the relative norm yields
\[
 m(f_i)=10r_i h(\beta_i)\ge10h(\gamma_i)
                            =|t_i|\log\varepsilon.
\]
Mahler multiplicativity and (F2) now give the complete fixed budget
\[
                       \sum_i|t_i|\le\frac{B}{\log\varepsilon}. \tag{F15}
\]
Both the number of nonzero norm exponents and their sizes are uniformly bounded.
Those factors each carry at least log epsilon of total positive measure, and by (F3) have degree proportional to n.
Any sublinear factor must eventually be on the t_i=0 branch.
The entire fiber already has t=0, so neither the integer balance nor its budget excludes that branch.

<a id="moving-map-off-circle-pairs"></a>
## Uniformly separated off-circle pairs and the surviving norm-one branch

At a nonreal source embedding put w=sigma(u).
There is no case |w|=1: that would make the source trace -1 and the source a cube root of unity, whereas P_L is irreducible and nontorsion.
When |w|<1, the argument (F4)--(F5) already places the entire fiber on the circle.

When |w|>1, write
\[
 B_w(z)=\frac{1+\overline w z}{z+w}
       =\frac{\overline w}{w}\,
                         \frac{z+1/\overline w}{1+z/w}.
\]
This is a degree-one finite Blaschke product, and the fiber equation is z^(n-1)=B_w(z).
The circle argument derivative of B_w is at most (|w|+1)/(|w|-1).
Thus for
\[
                             n-1>\frac{|w|+1}{|w|-1}, \tag{F16}
\]
the quotient z^(n-1)/B_w(z) has strictly positive argument derivative and winding number n-2 on the circle.
It gives exactly n-2 simple circle roots.
The two remaining roots lie off the circle and form one reciprocal-conjugate pair by the self-inversive relation.

The exterior root is separated from the circle by a fixed amount for all sufficiently large n.
Put rho=(|w|-1)/2 and use the circle |z+w|=rho.
There |z|>=(|w|+1)/2 and |z|<=(3|w|-1)/2, so
\[
 \rho\left(\frac{|w|+1}{2}\right)^{n-1}
       > |w|\frac{3|w|-1}{2}+1                        \tag{F17}
\]
makes z^(n-1)(z+w) dominate -(overline w z+1).
Rouche's theorem gives exactly one root in that disk, whose modulus is at least (|w|+1)/2>1.
Conditions (F16)--(F17) eventually hold for every one of the finitely many relevant embeddings.

By (F6), any actual K-factor includes both members of this off-circle pair or neither.
A corresponding rational factor containing its exterior member has measure at least log((|w|+1)/2), so (F3) forces its degree to be proportional to n.
Sublinear factors must omit all these pairs and have only circle roots at all eight nonreal source embeddings.

This does not remove radial cancellation at the two real embeddings.
For the actual 0<u<1/2 and z=e^(i theta),
\[
 |T_u(z)|^2-1
   =\frac{(1-2u)(1+2\cos\theta)}{|z+u|^2},\qquad
                 \int_{\mathbb T}\log|T_u(z)|\,d\mu_{\mathbb T}=0. \tag{F18}
\]
The first identity follows by expanding the two squared moduli.
For the second, both integrals of log|az+1| and log|z+u| are zero by Jensen, because 0<a,u<1.
There are positive and negative radial contributions whose angular mean is exactly zero.
Thus the norm-one condition is compatible with the small-height equidistribution in v5; this argument supplies no contradiction and no proportional degree bound on the remaining factors.

<a id="moving-map-forced-symmetry-obstructions"></a>
## Finite-order and rotation constructions do not force the desired factors

The first attempt is to give T_u finite projective order and exploit its cycles.
In fact that is impossible for any algebraic-integer unit alpha for which 1+alpha and alpha^2+alpha+1 are nonzero.
The matrix A=[[a,1],[1,u]] has trace one and is not scalar.
If it had finite projective order, it would be diagonalizable with eigenvalue ratio a root of unity zeta, giving
\[
 c=\frac{(\operatorname{tr}A)^2}{\det A}
     =2+\zeta+\zeta^{-1}
     =-\frac{(\alpha+1)^2}{\alpha^2+\alpha+1}.
\]
Its nonzero trace rules out zeta=-1.
Consequently c+1 is an algebraic integer all of whose conjugates are strictly greater than one, since they are 3+zeta^j+zeta^(-j).
But
\[
                         (c+1)^{-1}=-(\alpha+1+\alpha^{-1})
\]
is also an algebraic integer.
This would make c+1 a unit, contradicting the product of its strictly greater-than-one conjugates.

A whole-polynomial rotational symmetry is equally unavailable.
If q_(n,u)(zeta z)=b q_(n,u)(z), the nonzero constant term gives b=1 and the nonzero linear coefficient gives zeta=1.
The inverse-source symmetry q_(n,u)*=-q_(n,1-u) exchanges disjoint fibers, as proved in [v5](Yin_L_G0450_v5.md#moving-map-factorization-sources).
It supplies no common factor and is not a proof that either fiber is irreducible.

There is a stronger exclusion of complete rotation groups inside one K-fiber:
\[
                     H(z^k)\nmid q_{n,u}(z)
       \quad\hbox{for all }k\ge2
       \hbox{ and nonconstant }H\in K[z].             \tag{F19}
\]
Suppose such divisibility held and put w=z^k.
Since q_(n,u)(0)=-1, H(0) is nonzero.
The direct decomposition K[z]=sum_(j=0)^(k-1) z^j K[w] shows that H must divide every residue-class component of q.
A component consisting of just one nonzero monomial is impossible, since H(0) is nonzero.
The four support exponents 0,1,n-1,n must therefore be paired into equal residue classes.
Pairing 0 with 1 is impossible.
Pairing 0 with n and 1 with n-1 requires k dividing both n and n-2, hence k=2 and n even, also impossible.
The remaining possibility is k dividing n-1.
Writing n-1=kM gives
\[
                       q_{n,u}=z(w^M-a)+(uw^M-1).
\]
Then H divides both displayed components, whose linear combination is the nonzero constant au-1.
This contradiction proves (F19).
The conclusion concerns a K-fiber; a rotation that moves roots between different source embeddings is not covered by it.

Finally, a Mobius transformation commuting with z^m, m>=2, must permute the critical-point set {0,infinity}, by comparing critical points of the two compositions.
It is therefore cz or c/z, and commutation forces c^(m-1)=1.
The nonzero solutions of z^m=T(z) in either case are roots of unity.
This exact commutation mechanism yields no positive factor.
Directly imposing a fixed radical equation instead returns to the [fixed-seed saturation test](Yin_L_G0450_v1.md#unit-ray-saturation); imposing a torsion ratio of a fixed pair returns to [homogeneous layers](Yin_L_G0458_v1.md#zero-phase-cost-classification).
These comparisons do not extend either fixed-input obstruction to arbitrary changing pairs or noncommuting constructions.

<a id="moving-map-local-factor-proliferation"></a>
## Many local factors and the missing global descent

A different attempt really does force numerous factors at a finite place.
Fix a prime of K above two with residue field F_(2^s).
The matrix A is invertible over O_K by v5, so its reduction defines an element of PGL_2(F_(2^s)) of some finite order h.
Choose k divisible by s, put m=2^k and n=m+1.
For any residue root beta of q_(n,u), its denominator beta+u is nonzero and
\[
                     \beta^m=\overline T_u(\beta).
\]
The m-power Frobenius fixes the coefficients of the reduced map and commutes with it.
Iterating h times gives
\[
                       \beta^{2^{kh}}=\beta.          \tag{F20}
\]
Every residue root therefore lies in F_(2^(kh)).

The reduced polynomial is squarefree.
In characteristic two its derivative is z^m-a.
A common root would give beta^m=a and then q(beta)=au-1, contradicting the nonzero reduced determinant.
Thus every residue irreducible factor has degree at most kh/s over F_(2^s), and there are at least
\[
                         \left\lceil
                            \frac{2^k+1}{kh/s}
                         \right\rceil                \tag{F21}
\]
distinct local factors.
Hensel lifting gives the corresponding factorization over the completion K_p.

This is not a count of factors over K or Q.
A decomposition-group orbit can be a small part of one global Galois orbit; all these local pieces may belong to one global irreducible factor.
No global coefficient descent or invariant subset was produced.
The argument therefore does not meet the within-output global factor requirement, despite its unbounded local count.

Nor does (F20) give a new S9 Taylor relation.
It first holds only at one residue prime.
A full-ring assertion (beta^L-1)/2 in the original integer ring would require every prime above two and the actual ramification depths, which were not proved here.
Even if that separate step were supplied, the displayed scalar period is 2^(kh)-1, of order n^h for this fixed place.
The residue extension degree O(log n) must not be substituted for that exponent or treated as a short evaluation window.
No additional normalized Smith divisibility on the original Taylor module has been established.

<a id="moving-map-stronger-source-boundary"></a>
## Stronger number-field statements and their actual limits

The bounded follow-up search sought factor-degree information over the actual non-Kroneckerian field K, beyond the Q-coefficient statements inspected in v5.
It located [Sch99](../audits/literature/Sch99/readme.md), whose printed Theorem 3 on p.275 does allow an arbitrary algebraic coefficient field, and the [Len99a gap propositions](../audits/literature/Len99a/readme.md).
The statements, normalization and restrictions below were inspected in the original passages identified in those source notes.
Neither source supplies a proportional factor-degree bound for the present family.

<a id="moving-map-laurent-monomial-normalization"></a>
**Definition (Sch99 Laurent monomial normalization).**
For a nonzero Laurent polynomial P over a field, write P=x_1^(b_1)...x_k^(b_k)P_0, where P_0 is an ordinary polynomial and no variable x_i divides P_0.
The operator J in Sch99, printed p.273, is J(P)=P_0; it deletes the Laurent monomial factor and does not normalize scalar coefficients.
A monomial substitution is performed before this operator when the source writes JF(x^nu).
This order is explicit in the source's conventions on pp.273--274 and in the substituted expressions in the proof of Corollary 1 on p.284.

In the notation of its printed Theorem 3, K is generated by ratios of the coefficients of the specialized polynomial and Khat is its normal closure.
Condition (10) requires, for every embedding sigma:K into Khat,
\[
                    \frac{J(F(z^{-\nu}))}{J(F^\sigma(z^\nu))}
                           \notin\widehat K.          \tag{F22}
\]
This excludes a constant ratio after the monomial factors have been removed.
For the actual family, take
\[
 F(X_1,X_2,X_3)=-1-aX_1+uX_2+X_3,\qquad
 \nu=(1,n-1,n).
\]
The coefficient-ratio field is exactly Q(u)=K.
Before normalization, F(z^(-nu))=q_(n,u)(z^(-1))=z^(-n)q_(n,u)*.
After normalization the numerator in (F22) is q_(n,u)*, while for sigma=tau its denominator is tau(q_(n,u)), since that polynomial has nonzero constant coefficient.
Consequently
\[
                   \frac{J(F(z^{-\nu}))}{J(F^\tau(z^\nu))}
                     =\frac{q_{n,u}^*}{\tau(q_{n,u})}
                     =-1.                            \tag{F23}
\]
The family violates the condition printed in 1999.
The Laurent ratio before applying J would instead contain z^(-n); omitting that normalization would give the wrong applicability test.

The bounded-rank exponent alternatives in the printed corollaries also do not by themselves eliminate this line.
The support symmetry 1+(n-1)=n has the fixed representation
\[
                  (1,n-1,n)=(1,n-1)
                     \begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}.
\]
Its matrix has rank two and height one, so a rank drop or an O(T^2) count for three-dimensional exponent data is compatible with the entire one-parameter sequence.
The proof's treatment of coefficient-conjugate reciprocal specializations on p.284 explicitly uses this kind of exponent symmetry.
No irreducibility conclusion of Theorem 3 is adopted here.
A [2019 corrigendum](../audits/literature/Sch19/readme.md) was identified from publisher metadata, but its text was not obtained and its mathematical scope remains unknown.
This is therefore a comparison with the hypothesis printed in 1999, not a statement that the correction is immaterial or that every later theorem has been excluded.

Len99a, printed p.270, Propositions 2.2--2.3, gives a small-degree gap test over number fields using
\[
                    c(D)=\frac{2}{D\log^3(3D)}
                    \quad(D\ge2)
\]
as a lower bound for the positive absolute logarithmic height log H in the stated degree range.
For a polynomial with k+1 nonzero terms and multiplicative coefficient height H, a gap greater than log(kH)/c(D) makes any nontorsion root of absolute degree at most D a common root of the two separated blocks.
This is the exact interface needed here; the rest of the factorization algorithm was not audited.

The four-term q_(n,u) has k=3, low-block degree one and high-block initial exponent n-1.
Its gap is n-2, and its two blocks have no common nonzero root because au-1 is nonzero.
Its fixed multiplicative coefficient height is H_0=H(1,u,-a,-1), with finite-place contribution one.
For an actual irreducible K-factor of degree r, the absolute degree is D=10r and the root is nontorsion.
The contrapositive of the gap test therefore gives
\[
                n-2\le5r\log^3(30r)\log(3H_0).        \tag{F24}
\]
This only forces r at least a constant times n/log^3 n and still allows r=o(n).
It is weaker asymptotically than combining v5's uniform height upper bound with the [reported Dobrowolski benchmark](../audits/literature/Smy08/Yin_U001.md#section-4-checked-mechanisms-and-external-theorems), which yields a lower bound of order n(log log n/log n)^3 on r.
That comparison reuses the benchmark at its existing external-statement scope, not as a newly audited lower-bound proof.
Neither degree-dependent bound supplies the proportional degree obstruction or an actual small factor sought here.

<a id="moving-map-restricted-next-question"></a>
## Remaining input

The factorwise identities, real-root description and fixed unit budget hold for every odd n>=3.
The norm-one conclusion for a sublinear sequence is eventual, and the off-circle pair estimates retain their displayed large-n thresholds.
The existing four [J142 inputs](../computations/programs/Yin_J_G0142/readme.md) remain the complete finite scan; no new numerical calculation or parameter scan was performed.
They do not establish an all-n factor-degree theorem.

A counterexample extracted from this family would now have to come from actual reciprocal rational factors of degree o(n), corresponding eventually to norm-one K-factors satisfying p*=(-1)^r tau(p) and avoiding the uniformly separated off-circle pairs at the nonreal source embeddings.
The real-root, unit-budget, rotation and local-splitting arguments leave that possibility open.
A useful next construction must produce the global factor itself or the missing descent of a genuinely suitable root subset.
Neither finite-order cycles, complete rotations inside one fiber nor the numerous local factors supply it.
The stronger printed number-field theorem is blocked by the actual coefficient-involution symmetry, and the applicable gap estimate leaves the sublinear range open.

The construction contributor read the complete saved argument (F1)--(F21), including the factor correspondence, real-norm positivity, unit budget, circle-root count, Rouche estimate and local/global boundaries, with no substantive defect found.
The bottleneck contributor separately read the finite-order, rotation, commutation and local-splitting sections and found no missing hypothesis or uncharged period in those arguments.
The source contributor checked the saved source-comparison section against the original passages, including the J normalization, coefficient-ratio field, degree and height conventions, and the uninspected corrigendum limit.
These ordinary author checks do not include a new formal R, an independent replay of J142, or an audit of the external factorization proofs.
