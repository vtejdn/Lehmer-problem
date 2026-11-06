---
author: Yin
---

# Moving mixed maps: exact quartic root tests and an inverse-endpoint exclusion

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The source contributor derived the exact Cayley and critical-value tests and the inverse-power endpoint exclusion.
The coordinating contributor supplied the inverse-endpoint candidate pair and checked the critical-value criteria and the inverse-power bounds.
These are ordinary same-author derivations, not independent review, a new Claim assessment or a construction of small factors.

<a id="quartic-root-test-scope"></a>
## The unit candidates and the actual factor question

[V7](Yin_L_G0450_v7.md#inverse-factor-scope) retains the fixed fields, exact resultant and low-degree inverse-factor conditions.
Keep K=Q(alpha), F=K^tau=Q(theta), theta=alpha+alpha^(-1), u=(1+alpha)^(-1), a=1-u and delta=2u-1.
The source alpha is the real Lehmer root, and tau(alpha)=alpha^(-1).
For odd n>=3 the K-fiber remains
\[
                         q_n=z^{n-1}(z+u)-(az+1).
\]
The norm-one quartic candidates are
\[
 p=z^4+bz^3+cz^2+\tau(b)z+1,\qquad
 b=\frac{s+\delta v}{2},\quad
 s=\frac{\eta_+-\eta_-}{2},\quad
 c=\frac{\eta_++\eta_-}{2}-2.
 \tag{A1}
\]
The three parameters eta_+,eta_-,v are units in O_F, with the exact [v7 integrality conditions](Yin_L_G0450_v7.md#inverse-factor-quartic-unit).
In particular b is in O_K, s,c are in O_F, and p(1)=eta_+, p(-1)=eta_- are nonzero.
Here p*=tau(p), with star meaning ordinary reversal at actual degree four.
These arithmetic conditions are necessary for an actual factor, not sufficient.
The tests below supply exact archimedean conditions while leaving the exact divisibility test p|q_n separate.

Four of the five real embeddings of F extend to nonreal embeddings of K; at these embeddings tau acts as complex conjugation.
These will be called the compact embeddings in this account.
The remaining real embedding of F extends to the two real embeddings of K.
At a compact embedding, the source trace xi lies in (-2,2).
Choose an extension sigma:K to C for which
\[
 \sigma(\delta)=i d,\qquad
 d>0,\qquad d^2=\frac{2-\xi}{2+\xi}.
\]
Changing the extension replaces d by -d and conjugates the polynomial, which does not change the circle-root question.

<a id="quartic-cayley-polynomial"></a>
## An exact real quartic for each circle-root question

At the selected compact embedding write
\[
 A=\sigma(\eta_-),\quad E=\sigma(\eta_+),\quad
 k=d\,\sigma(v),\quad
 x=\tfrac12\sigma(s),\quad y=\tfrac12 k.
\]
Thus sigma(b)=x+iy and sigma(c) is real.
Both A and E are nonzero.
Under the Cayley substitution z=(1+it)/(1-it), direct expansion gives the real polynomial
\[
 \begin{split}
 C(t)&=(1-it)^4\sigma(p)\!\left(\frac{1+it}{1-it}\right)\\
 &=A t^4-2k t^3+(A+E-16)t^2-2k t+E.
 \end{split}
 \tag{A2}
\]
For completeness, the leading and constant coefficients are 2-2x+sigma(c)=A and 2+2x+sigma(c)=E.
The cubic and linear coefficients are both -4y=-2k, while the quadratic coefficient is 2sigma(c)-12=A+E-16.
This accounts for every coefficient and its normalization.

The substitution maps the real line bijectively to the unit circle with the point -1 removed.
Its inverse is a fractional linear map, so finite root multiplicities are preserved.
The omitted point is not a root because sigma(p)(-1)=A is nonzero.
Also C has actual degree four because its leading coefficient is A.
Consequently
\[
 \boxed{\ \text{all four roots of sigma(p) lie on the circle}
       \quad\Longleftrightarrow\quad
       \text{all four roots of C are real},\ }
 \tag{A3}
\]
with multiplicities counted on both sides.
Distinct roots correspond to distinct roots.
Replacing the extension sigma by its conjugate sends k to -k and C(t) to C(-t).

<a id="quartic-critical-value-criterion"></a>
## Necessary and sufficient critical-value conditions

Normalize H=C/A so that H is monic, regardless of the sign of A.
Its derivative is the explicit real cubic
\[
 H'(t)=4t^3-\frac{6k}{A}t^2
              +\frac{2(A+E-16)}{A}t-\frac{2k}{A}.
 \tag{A4}
\]
A necessary and sufficient condition for (A3) is that H' have three real roots counted with multiplicity,
\[
 \rho_1\le\rho_2\le\rho_3,
\]
and that
\[
                    H(\rho_1)\le0,\qquad
                    H(\rho_2)\ge0,\qquad
                    H(\rho_3)\le0.
 \tag{A5}
\]
For four distinct circle roots, the necessary and sufficient conditions are three distinct real critical points and the three strict inequalities in (A5).
In particular the signs are evaluated on H=C/A; using signs of C without accounting for the sign of A would give the wrong test.

Here is the complete elementary justification.
If a monic real quartic has four real zeros counted with multiplicity, its derivative has three real zeros counted with multiplicity by the zeros inherited from repeated roots and the zeros between successive distinct roots.
The first and last critical values are nonpositive and the middle one is nonnegative, as follows from the alternating interval signs of a monic quartic.
Distinct roots make the critical points and these signs strict.

Conversely, suppose the derivative roots are distinct and (A5) holds.
The two infinite ends have positive sign, and the successive critical values have the displayed alternating weak signs.
The four resulting intervals therefore give four real roots, counting a critical zero with its multiplicity at least two when neighboring intervals share it.
Strict signs give one distinct root in each interval.
If two adjacent derivative roots coincide, (A5) forces their common critical value to be zero.
The quartic then has a real zero of multiplicity at least three, and its remaining factor is linear over the reals.
If all three derivative roots coincide, their value is zero and the monic quartic is the fourth power of the corresponding linear factor.
These cases prove (A5), including its multiple-root boundary.

An actual divisor of q_n must have distinct roots, because [v6 proves the fiber squarefree](Yin_L_G0450_v6.md#moving-map-factorwise-involution).
The strict test is therefore the relevant all-circle test for an actual quartic factor.
At compact embeddings with |sigma(u)|<1 it is necessary for every actual factor at every odd n>=3.
At the other compact embeddings, an actual factor can contain the separated off-circle pair.
Applying the all-circle test there is justified for an eventual positive-to-zero factor sequence, whose members must omit those pairs by [v6](Yin_L_G0450_v6.md#moving-map-off-circle-pairs); it is not justified for every factor without that qualification.

<a id="quartic-real-root-criterion"></a>
## An exact test at the real source embeddings

At the distinguished real embedding of K, let
\[
 P(t)=t^4+b_0t^3+c_0t^2+b_1t+1,
\]
where b_0 is the real value of b, b_1 is the value of tau(b), and c_0 is the value of c.
Then
\[
             P'(t)=4t^3+3b_0t^2+2c_0t+b_1.
 \tag{A6}
\]
The exact no-real-root condition is
\[
                  P(t)>0\quad\text{at every real root of }P'.
 \tag{A7}
\]
Indeed P tends to positive infinity at both ends, so it attains its global minimum at a real critical point.
Thus (A7) makes P positive everywhere.
Conversely, if P has no real root, monicity and continuity make it positive everywhere and therefore at every real critical point.
This proof includes repeated critical points.

The two real embeddings are exchanged by tau, and p*=tau(p) exchanges their nonzero real roots by inversion.
The constant coefficient one excludes zero as a root.
It therefore suffices to apply (A7) at one of the two embeddings.
An actual irreducible quartic factor must pass this test, by the real-root parity result in v6.
The inequalities eta_+>0 and eta_->0 at the distinguished real embedding are necessary endpoint checks, but do not replace (A7).

<a id="quartic-inverse-endpoint-control"></a>
## The inverse-endpoint candidate pair is excluded without a factorization

There is a second explicit pair satisfying the arithmetic conditions of v7.
Take
\[
 \eta_+=\frac1{\theta+1},\qquad
 \eta_-=\frac1{\theta-1},\qquad
 s=-\frac1{\theta^2-1},\qquad
 v=\pm s,\qquad
 c=\frac\theta{\theta^2-1}-2.
 \tag{A8}
\]
The exact values Q(1)=Q(-1)=-1 make theta+1 and theta-1 units, so both endpoint parameters and s are integral units.
The corresponding b is su or sa, respectively, hence is integral.
Also s-v is zero or 2s, and eta_+-eta_-=2s, so the exact conditions modulo two and four from v7 hold.
This establishes arithmetic admissibility, not factorhood or the real-root test.

Use the same trace polynomial as in v7, now with the exact tighter interval
\[
             Q(9/10)=15159/100000>0,\qquad
             Q(11/12)=-8137/248832<0.
 \tag{A9}
\]
There is therefore a trace embedding xi in (9/10,11/12).
It extends to a compact embedding with |sigma(u)|^2=1/(2+xi)<1, so every root of sigma(q_n) lies on the circle for every odd n>=3.
At this embedding the middle coefficient of either candidate (A8) satisfies
\[
 \sigma(c)=-\frac\xi{1-\xi^2}-2
                     <-\frac{90}{19}-2=-\frac{128}{19}<-6.
 \tag{A10}
\]
If all four roots of a monic quartic lie on the circle, its quadratic coefficient is the sum of their six pairwise products and has absolute value at most six.
Thus (A10) excludes both candidates from dividing any q_n.
No numerical approximation, irreducibility assertion or polynomial factorization is used.

<a id="quartic-inverse-power-endpoints"></a>
## A whole inverse-power endpoint family fails the same coefficient test

The same embedding excludes every endpoint choice
\[
                  \eta_+=(\theta+1)^{-j},\qquad
                  \eta_-=(\theta-1)^{-j},\qquad j\ge1,
 \tag{A11}
\]
for any remaining parameter v for which the quartic is integral and satisfies the other candidate conditions.
The endpoint parameters are units, but that alone makes no assertion about the remaining conditions.
Their middle coefficient is forced by (A1).
At the embedding in (A9),
\[
 0<(\xi+1)^{-j}<1,\qquad
 (\xi-1)^{-j}=(-1)^j(1-\xi)^{-j},\qquad
 (1-\xi)^{-j}>10^j.
\]
For odd j this gives
\[
                    \sigma(c)<-(10^j+3)/2\le-13/2.
\]
For even j, necessarily j>=2, it gives
\[
                    \sigma(c)>10^j/2-2\ge48.
\]
Thus |sigma(c)|>6 for every j>=1, independently of v.
The entire inverse-power endpoint family is excluded from every q_n by the same all-circle coefficient bound.
This is a restriction on this particular endpoint family, not an exclusion of arbitrary unit triples.

<a id="quartic-root-test-outcome"></a>
## What the root tests decide and what remains missing

Equations (A2)--(A5) give a necessary and sufficient all-circle test at a specified compact embedding, with the distinction between distinct and multiple roots explicit.
Equations (A6)--(A7) give the independent no-real-root test at the real source embeddings.
They can reject unit triples before the exact quotient-ring return test in v7.
The inverse-endpoint pair and its whole inverse-power extension are concrete failures of that kind.
No new surviving quartic factor or exact return is produced here.

Passing all applicable archimedean tests still supplies neither p|q_n nor irreducibility.
The [v7 exact return condition and norm correspondence](Yin_L_G0450_v7.md#inverse-factor-archimedean-filters) remain necessary, with every actual rational factor and its total measure retained.
A single fixed relative degree cannot yield a positive-to-zero sequence; the eventual target still requires r tending to infinity and r/n tending to zero.
This account supplies a more precise bounded diagnostic, not a replacement for that missing construction.

The proofs use direct polynomial expansion, elementary real-root calculus and the exact field and root-distribution results already retained in v5--v7.
No additional external theorem, numerical scan, native computation, bibliography entry or source-unit adoption is used.
The coordinating contributor checked the critical-value equivalence and inverse-power inequalities in discussion, and the source contributor checked the complete algebra and the preserved domain limits.
These are ordinary author checks; no formal R or independent review is asserted.
The source and coordinating contributors each read the complete saved version, including the repeated-root boundary and the all-index inverse-power exclusion.
