---
author: Yin
---

# Moving mixed maps: inverse factors and an exact resultant unit constraint

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The source contributor proposed the inverse-factor parameterization and checked the resultant, field and integrality arguments.
The coordinating contributor supplied the full resultant identity, the quartic unit deduction and its residue-ring refinement.
These are ordinary same-author derivations and checks, not an independent review, a new Claim assessment or a construction of small factors.

<a id="inverse-factor-scope"></a>
## The fixed family and the proposed change of construction order

[V5](Yin_L_G0450_v5.md#moving-map-actual-inputs) retains the complete integer output, its bounded full measure and the uniform factor-height asymptotic.
[V6](Yin_L_G0450_v6.md#moving-map-factorwise-involution) retains the factorwise involution, real-root description, unit budget and source-applicability boundaries.
Those versions remain fixed; this version adds exact necessary equations for constructing a factor before forming a large output.

For odd n>=3, set
\[
 q_n(z)=z^{n-1}(z+u)-(az+1),\qquad
 u=(1+\alpha)^{-1},\quad a=1-u,
\]
where alpha is the real Lehmer root, K=Q(alpha), and tau(alpha)=alpha^(-1).
Put
\[
 F=K^\tau,\quad \theta=\alpha+\alpha^{-1},\quad
 \delta=u-a=2u-1.
 \tag{I1}
\]
The field F=Q(theta) is totally real of degree five; K has degree ten and signature (2,4).
Its trace minimal polynomial, retained in v6, is
\[
 Q(y)=y^5+y^4-5y^3-5y^2+4y+3.
 \tag{I2}
\]
The [integral Mobius calculation](Yin_L_G0450_v5.md#moving-map-integral-mobius-height) gives u,a,au-1 in O_K^times.
Also delta=(1-alpha)/(1+alpha) is a unit: the source endpoint values P_L(1)=-1 and P_L(-1)=1 make both numerator and denominator units.
We have tau(delta)=-delta and
\[
                  q_n(1)=\delta,\qquad q_n(-1)=-1.
 \tag{I3}
\]

For an actual monic irreducible K-factor p of degree r with root beta, v6 proves K is contained in Q(beta) and that the rational minimal polynomial is exactly N_(K/Q)(p), with degree 10r.
There is no extra norm multiplicity.
The full rational outputs have bounded total logarithmic measure, and, as n tends to infinity uniformly over its actual irreducible factors, the asymptotic is
\[
 m\bigl(N_{K/\mathbb Q}(p)\bigr)
       =\frac{10r}{n-2}(E+o(1)),\qquad E>0.
 \tag{I4}
\]
A small-factor sequence therefore requires r/n tending to zero.
By [v6's relative norm budget](Yin_L_G0450_v6.md#moving-map-relative-unit-balance), such a sequence eventually lies on the branch
\[
                    p(0)=(-1)^r,\qquad
                    p^*=(-1)^r\tau(p).
 \tag{I5}
\]
All degree-one and degree-two exclusions and the coefficient parameterizations below concern this norm-one branch.
They are not assertions that every K-factor has norm one.

Since q_n is monic integral, an actual monic factor and its monic quotient have coefficients in O_K.
Equation (I3) implies
\[
                         p(1),p(-1)\in O_K^\times.
 \tag{I6}
\]
For any element of F, integrality and unit status descend from K, because O_K intersect F equals O_F, also applied to its inverse.

<a id="inverse-factor-low-degrees"></a>
## The first possible coefficient shapes

For r=1, equation (I5) gives p=z-1, excluded by q_n(1) nonzero.
For r=2, it gives
\[
                       p=z^2+bz+1,\qquad \tau(b)=b.
\]
This p is ordinarily reciprocal.
The [ordinary-reversal calculation in v5](Yin_L_G0450_v5.md#moving-map-factorization-sources) gives gcd_K(q_n,q_n*)=1, so this quadratic cannot divide q_n.

For r=3, the possible shape is
\[
                    p_b=z^3+bz^2-\tau(b)z-1,
                    \qquad b\in O_K.
 \tag{I7}
\]
Its endpoint values are b-tau(b) and b+tau(b)-2.
The first is anti-invariant, so division by the anti-invariant unit delta gives an element of F.
Using (I6), the exact endpoint-unit parameterization is
\[
 b-\tau(b)=\delta\varepsilon,\quad
 b+\tau(b)-2=\eta,\quad
 \varepsilon,\eta\in O_F^\times,\quad
 b=\frac{\eta+2+\delta\varepsilon}{2}\in O_K.
 \tag{I8}
\]
The displayed integrality is a condition, not a consequence of arbitrarily choosing two units.
In particular b is not tau-fixed.
The choice b=u is exactly q_3, an existing input, not a newly supplied factor.

For r=4, equation (I5) gives
\[
              p=z^4+bz^3+cz^2+\tau(b)z+1,
              \qquad b\in O_K,\quad c\in O_F.
 \tag{I9}
\]
Here b cannot belong to F, since that would again make p ordinarily reciprocal.
Define
\[
 \eta_+=2+c+b+\tau(b),\qquad
 \eta_-=2+c-b-\tau(b).
 \tag{I10}
\]
These are p(1) and p(-1), respectively, and both belong to O_F^times.
Put
\[
 s=\frac{\eta_+-\eta_-}{2},\quad
 c=\frac{\eta_++\eta_-}{2}-2,\quad
 v=\frac{b-\tau(b)}\delta,\quad
 b=\frac{s+\delta v}{2}.
 \tag{I11}
\]
Endpoint conditions alone give v in O_F, nonzero, but do not establish that it is a unit.
The actual-divisibility resultant below supplies that additional conclusion.

<a id="inverse-factor-full-resultant"></a>
## The full reciprocal resultant has only one possible nonunit contribution

Write ell=n-2, which is odd, and S(z)=z^ell+1.
The exact ordinary reversal identity is
\[
 q_n^*=-\tau(q_n),\qquad
                    q_n+q_n^*=\delta zS(z).
 \tag{I12}
\]
Use the resultant convention Res(f,g)=product g(beta) for monic f, with roots counted with multiplicity.
Since q_n is monic with odd degree and constant coefficient -1, Res(q_n,z)=1.
Evaluation at its roots gives
\[
 \operatorname{Res}_K(q_n,q_n^*)
       =\delta^n\operatorname{Res}_K(q_n,S).
\]
At a root of S, reduction of q_n gives
\[
                q_n(z)=-(z^2+z+1)=-\Phi_3(z).
\]
Swapping the two odd degrees in Res(q_n,S) contributes a minus sign, and replacing q_n by -Phi_3 in the degree-ell root product contributes another minus sign.
They cancel.
Therefore
\[
 \operatorname{Res}_K(q_n,q_n^*)
      =\delta^n c_n,\qquad
 c_n=\operatorname{Res}(S,\Phi_3)
      =\begin{cases}4,&3\mid n-2,\\1,&3\nmid n-2.\end{cases}
 \tag{I13}
\]
Indeed, if omega is a primitive cube root, the last resultant is
(1+omega^ell)(1+omega^(2ell)), which is four when 3 divides ell and one otherwise.
For odd n, the first case is exactly n congruent to five modulo six.
In particular the full resultant is nonzero.

Let p be any actual monic integral factor and write q_n=ph with h monic in O_K[z].
Ordinary reversal is multiplicative, so q_n*=p*h*.
Resultant multiplicativity gives
\[
 \operatorname{Res}(q_n,q_n^*)
 =\operatorname{Res}(p,p^*)\operatorname{Res}(p,h^*)
  \operatorname{Res}(h,p^*)\operatorname{Res}(h,h^*).
 \tag{I14}
\]
Every factor on the right belongs to O_K.
Thus Res(p,p*) divides the full resultant in O_K.
This integral divisibility does not require h or p to be irreducible, although actual irreducible factors are the construction target.

For the quartic (I9), ordinary reversal gives
\[
                   p^*-p=(\tau(b)-b)z(z^2-1).
\]
Since its degree is four and its constant coefficient is one, root evaluation yields the exact identity
\[
             \operatorname{Res}(p,p^*)
                  =(b-\tau(b))^4p(1)p(-1).
 \tag{I15}
\]
All endpoint factors and delta are units.
Combining (I13)--(I15) consequently gives
\[
                              v^4\mid c_n
                              \quad\hbox{in }O_F.
 \tag{I16}
\]
First the divisibility holds in O_K; its quotient c_n/v^4 belongs to F and hence to O_K intersect F=O_F.
When c_n=1 it already makes v a unit.
When c_n=4 it implies v^2 divides two in O_F: the element 2/v^2 has square 4/v^4 in O_F and is integral over O_F, so integral closure places it in O_F.

<a id="inverse-factor-quartic-unit"></a>
## Reduction modulo two forces the quartic skew parameter to be a unit

The reduction of the actual trace minimal polynomial is
\[
                 \overline Q=y^5+y^4+y^3+y^2+1.
 \tag{I17}
\]
It has no root in F_2.
Its remainder modulo the only monic irreducible quadratic y^2+y+1 is y.
A reducible polynomial of degree five has an irreducible factor of degree one or two, so Qbar is irreducible.
No polynomial factorization computation is being assumed here.

This gives a direct finite-ring argument without an index condition or a Dedekind factorization criterion.
The ring O_F is a free integer module of rank five, so O_F/2O_F has dimension five over F_2.
The integral element theta and (I17) induce a unital homomorphism
\[
             \mathbb F_2[y]/(\overline Q)
                         \longrightarrow O_F/2O_F.
\]
The target is nonzero, because 1/2 is not an algebraic integer.
The source is the field with 32 elements, so the homomorphism is injective.
Both sides have dimension five, hence
\[
                              O_F/2O_F\simeq\mathbb F_{32}.
 \tag{I18}
\]
In prime-ideal language, two is inert and unramified in F.
No corresponding assertion about ramification in K is needed.

For c_n=4, write v^2w=2 with w in O_F, as obtained after (I16).
If v were zero modulo two, then v=2t and 2t^2w=1, which would make 1/2 integral, a contradiction.
Thus v is nonzero in the field (I18), and reducing v^2w=2 makes w zero modulo two.
Write w=2t; cancellation gives v^2t=1.
Together with the c_n=1 case, this proves
\[
              \boxed{\ v=(b-\tau(b))/\delta\in O_F^\times\ }
 \tag{I19}
\]
for every actual norm-one quartic factor and every odd n for which it occurs.
The proof uses only the usual ring-of-integers lattice and integral-closure facts and the displayed finite-ring calculation.
It does not import an uninspected number-field irreducibility theorem or a new source proof claim.

Consequently the quartic parameterization (I11) uses three units eta_+, eta_-, v in O_F, subject to its integrality conditions.
Those conditions have a useful exact form.
Both s and c in (I11) are integral if and only if eta_+ and eta_- are congruent modulo 2O_F.
Since delta=2u-1,
\[
                    b=(s-v)/2+uv
\]
is integral if and only if s-v belongs to 2O_F; this uses O_K intersect F=O_F.
Because v is a unit and (I18) is a field, s is then nonzero modulo two.
In particular
\[
                 \eta_+-\eta_-\in2O_F\setminus4O_F.
 \tag{I20}
\]
This is a necessary coefficient-integrality filter for this factor construction.
It is not a new divisibility assertion about a normalized S9 Taylor module.

<a id="inverse-factor-archimedean-filters"></a>
## Actual root conditions and an exact return test

At either real source embedding, v6 proves q_n has exactly one positive real root and no negative real root.
Thus an actual irreducible odd-degree K-factor is unique and contains that positive root.
An actual irreducible even-degree K-factor has no real root at either real embedding.
In particular the cubic is the only possible odd-degree factor at its input, while a quartic must pass this no-real-root test.

At each nonreal source embedding where |sigma(u)|<1, all q_n roots lie on the circle.
At the other nonreal embeddings, [v6's off-circle pair analysis](Yin_L_G0450_v6.md#moving-map-off-circle-pairs) supplies, for large n, one uniformly separated reciprocal-conjugate pair.
A factor whose rational total measure tends to zero must omit every such pair.
Thus all its roots at all eight nonreal embeddings eventually lie on the circle.
These restrictions concern actual small-factor sequences; they are not asserted for every factor at every n.

For a cubic satisfying this circle restriction, elementary symmetric sums give |sigma(b)|<=3.
For either extension sigma:K to C of an associated embedding of F, (I8) therefore gives
\[
                   -8\le\sigma(\eta)\le4,\qquad
                   |\sigma(\delta\varepsilon)|\le6.
\]
For a quartic, the corresponding bounds are |sigma(b)|<=4 and |sigma(c)|<=6.
They are useful necessary filters on the unit parameters, not divisibility certificates or existence statements.

For any proposed p, the actual factor test is the exact congruence
\[
                z^{n-1}(z+u)=az+1\pmod p.
 \tag{I21}
\]
It can be evaluated by a power recurrence in K[z]/(p).
It does not follow from endpoint units, the involution, residue splitting or the archimedean filters.
A candidate that passes (I21) still requires its actual irreducible-factor decomposition, unless irreducibility has been separately proved.
The rational factors and their full costs must then be taken through the norm correspondence, not guessed from a selected root.

No one nontorsion K-factor can divide q_n and q_m for distinct indices in this fixed-u fiber.
For a common root beta, beta and beta+u are nonzero; the latter follows since q_n(-u)=au-1 is nonzero.
The two defining equations imply beta^(n-m)=1, a contradiction.
This is a statement inside the fixed K-fiber and makes no unproved assertion about a rational factor recurring across different source embeddings.
It also shows why the already known cubic b=u cannot produce later returns.

<a id="inverse-factor-explicit-quartic-control"></a>
## An explicit unit candidate pair fails the circle test for every index

There is a concrete pair that satisfies all the displayed unit and integrality conditions but still cannot be an actual factor.
Choose
\[
 \eta_+=\theta+1,\qquad \eta_-=\theta-1,\qquad
 s=1,\quad c=\theta-2,\quad v=\pm1.
 \tag{I22}
\]
The exact values Q(1)=Q(-1)=-1 show that theta-1 and theta+1 are units.
Formula (I11) then gives b=u or b=a, respectively.
Thus the two integral candidates are
\[
 p_+(z)=z^4+uz^3+(\theta-2)z^2+az+1,\qquad
 p_-(z)=z^4+az^3+(\theta-2)z^2+uz+1.
 \tag{I23}
\]
They are exchanged by tau and by ordinary reversal.
Their endpoint units are theta+1 and theta-1.
Also eta_+-eta_-=2, and s-v is either zero or two, so the exact conditions (I19)--(I20) and the preceding integrality equivalences hold.

Both candidates pass the necessary real-root test.
At the two real embeddings of K, theta has the same value theta_0=lambda+lambda^(-1)>2, while u and a lie in (0,1).
All coefficients are positive there, so the polynomials are positive on the nonnegative real axis.
For t>0, either candidate satisfies
\[
 p_\pm(-t)\ge t^4+1-t^3-t+(\theta_0-2)t^2
 =(t-1)^2(t^2+t+1)+(\theta_0-2)t^2>0.
\]
At zero their value is one.
Hence neither has a real root at either real embedding.

The failure occurs at a different, explicitly supplied trace embedding.
The rational endpoint calculation is
\[
                 Q(0)=3,\qquad
                 Q(11/12)=-8137/248832<0.
 \tag{I24}
\]
The intermediate value theorem gives a root xi of Q in (0,11/12), and irreducibility of Q identifies an embedding of F sending theta to xi.
Extend it to sigma:K to C.
Since sigma(alpha)+sigma(alpha)^(-1)=xi is in (0,2), sigma(alpha) lies on the circle and is nonreal.
Writing w=sigma(u), the same identities as in v6 give
\[
 \operatorname{Re}w=1/2,\quad
 |w|^2=(2+\xi)^{-1}<1,\quad
 \sigma(\delta)=\pm i d,\quad
 d^2=\frac{2-\xi}{2+\xi}<1,
 \qquad d>0.
 \tag{I25}
\]
At this embedding the finite-Blaschke argument of v6 puts every root of sigma(q_n) on the circle for every odd n>=3.

For z=exp(it), either centered candidate is real and equals
\[
 z^{-2}\sigma(p_\pm)(z)
       =4\cos^2t+\cos t+\xi-4\mp d\sin t,
 \tag{I26}
\]
where the two signs may be interchanged by the choice of extension sigma.
On the closed left semicircle put x=cos t<=0 and y=|sin t|.
Then x=-sqrt(1-y^2)<=-1+y^2, and d<1 gives
\[
 z^{-2}\sigma(p_\pm)(z)
 \le \xi-1-3y^2+y
 \le \xi-1+1/12
 <0.
\]
The middle inequality follows from -3y^2+y=1/12-3(y-1/6)^2.
Therefore neither candidate has a zero on that closed semicircle.

If all four roots of a candidate lay on the circle, every one would have strictly positive real part.
Their sum would then have positive real part.
But the sum of roots is minus its cubic coefficient and therefore has real part -1/2 by (I25).
This contradiction proves that neither sigma(p_+) nor sigma(p_-) has all its roots on the circle.
Consequently neither p_+ nor p_- divides q_n for any odd n>=3.
No irreducibility assumption on the candidates is used.
This is a complete symbolic failure of a specific candidate pair, not an exclusion of other unit parameters or higher factor degrees.

<a id="inverse-factor-next-question"></a>
## Remaining construction and inspection limits

The concrete next question is whether the integral unit parameters in (I8), or the three-unit quartic parameters in (I11) and (I19)--(I20), produce a new exact return (I21) with n large relative to r.
No such new return is supplied here.
The resultant has strengthened a necessary condition on an actual factor; it has not proved that any proposed parameter tuple is a factor.

One fixed r, or even a bounded range of r, cannot supply a positive-to-zero sequence.
The rational degrees would be bounded by 10r, and bounded measure gives only finitely many monic integer polynomials of bounded degree by the elementary symmetric-coefficient bounds.
Their positive measures cannot tend to zero.
An eventual counterexample from this family must still have
\[
                         r\longrightarrow\infty,
                         \qquad r/n\longrightarrow0.
\]
The inverse-factor test is therefore a small diagnostic within the existing mixed-map route, not a new strategy or a long-term existence claim.

The bounded source comparison reused the exact nonreciprocal-part and function-field boundaries retained in v2 and v6.
Public searches for reciprocal lacunary factorization, the rational specialization conjecture and many positive factors supplied no newly inspected theorem giving the required reciprocal global factors.
Bhawesh Mishra's [Superpolynomially Large Support in Every Irreducible Factor of Lacunary Polynomials](https://arxiv.org/abs/2609.22286) was identified only through the [author's publication list](https://bhaweshmishra.com/publications/) and abstract metadata; its original text was not obtained and none of its conclusions is used here.
There is no new bibliography entry, U adoption, native mathematical computation or formal R in this version.
The coordinating and source contributors developed and checked the resultant and quartic unit deduction in discussion.
The coordinating contributor supplied the explicit unit candidate pair and its all-index circle obstruction; the source contributor checked the rational endpoint, centered expressions and root-sum contradiction.
The source contributor read the saved version, including the elementary finite-ring proof, the concrete control and its source-use limits.
The construction contributor read the saved version before the explicit control was added and checked (I12)--(I20) with their necessary inputs, including the resultant signs, finite-ring argument and exact integrality conditions.
The coordinating contributor read the complete final version, including (I22)--(I26).
These are ordinary author checks, not independent or formal review.
