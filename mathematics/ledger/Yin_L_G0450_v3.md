---
author: Yin
---

# Mixed all-pass pullbacks: torsion norm escape and an iterative binomial obstruction

Date: 2026-11-06.
Author exploration for Yin under the [unrestricted Lehmer Task](../tasks/Yin_T_G0001_v1.md#contract).
The construction contributor selected the mixed quadratic pullback, checked its integral output and complete root costs, and assembled the arguments below.
The coordinating contributor selected the genuine growing-degree iteration, established its endpoint and cyclotomic controls, and supplied the bounded-degree parity extension.
The bottleneck-diagnosis contributor supplied the irreducible torsion-norm control, checked the fiber-cost multiplicities and identified the direct accepted binomial-norm bound.
These are ordinary author-development contributions, not an independent project review or a new Claim assessment.
The bottleneck-diagnosis contributor subsequently read the complete version and found no mathematical defect in (M5)--(M29), including the norm multiplicities, exact fiber costs, iteration signs, original-degree binomial return and finite-ring extension.
That ordinary cross-check does not constitute a formal project review or extend an external-source or computational inspection scope.

<a id="mixed-allpass-revision-scope"></a>
## Question and retained predecessor

[V2](Yin_L_G0450_v2.md#fixed-source-proliferation-revision) remains fixed with its complete finite-Blaschke factor bound, primitive-content proof, Poisson-cost identity and mixed-delay specialization boundary.
Its factor bound uses the fact that all relative conjugates in a finite-Blaschke fiber lie on the same side of the unit circle.
This version tests circle-preserving rational functions with poles inside the disk, for which that fact is false.
The original target is positive total logarithmic Mahler measure tending to zero, possibly obtained by selecting positive irreducible factors from reducible integer outputs.
No normalized height is substituted for total measure, and no whole-output irreducibility is assumed.

A genuine unit example below has relative norm -1 and positive measure, so the old equality between factor measure and norm measure cannot be extended to all mixed maps.
Nevertheless, the selected integral quadratic iteration supplies a short integral binomial at every actual output root.
It follows that every one of its positive irreducible factors has a measure lower bound proportional to its own degree, and the complete output measure grows at least linearly in its degree.
The bounded-degree parity extension has explicit additional hypotheses and does not classify arbitrary mixed maps of growing degree.

Write
\[
 P_L(x)=x^{10}+x^9-x^7-x^6-x^5-x^4-x^3+x+1
\]
for the fixed Lehmer polynomial.
It is monic, irreducible and reciprocal, has constant coefficient one and satisfies P_L(1)=-1 and P_L(-1)=1.
Its roots consist of a real pair lambda,lambda^{-1}, with lambda>1, and four conjugate pairs on the unit circle.
The trace form, also used in the existing [central-coefficient control](Yin_L_G0374_v1.md#capacity-and-lehmer-central-control), is
\[
 P_L(z)=z^5Q(z+z^{-1}),\qquad
 Q(y)=y^5+y^4-5y^3-5y^2+4y+3.
 \tag{M1}
\]
The logarithmic measure convention and the implication that a noncyclotomic monic unit polynomial has positive measure are the accepted [Kronecker normalization](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization).

<a id="mixed-allpass-content-and-norm-loss"></a>
## Exact coefficient costs and the missing norm term

Let g in Z[z] be primitive of degree k>=1, with a=g(0) nonzero and b its nonzero leading coefficient.
Put
\[
 g^*(z)=z^kg(1/z),\qquad R(z)=g^*(z)/g(z),\qquad
 F_g(z)=g(z)^{10}P_L(R(z)).
 \tag{M2}
\]
For the analytic discussion suppose that g has no unit-circle roots, has both interior and exterior roots, and that g and g^* are coprime.
The last condition removes common denominator factors before interpreting the map.
Without it, any common factor contributes its tenth power to the displayed polynomial, so canceling the rational function would discard real output cost.

Expansion of P_L proves that F_g is an integer polynomial.
Its leading and constant coefficients are respectively b^{10}P_L(a/b) and a^{10}P_L(b/a), and reciprocity of P_L makes them equal:
\[
 \ell=b^{10}P_L(a/b)=a^{10}P_L(b/a)\ne0.
 \tag{M3}
\]
Nonvanishing follows because the irreducible P_L has no rational root.
Consequently F_g has degree 10k and is reciprocal.

The [primitive-content proof in v2](Yin_L_G0450_v2.md#primitive-blaschke-content) does not require the disk hypothesis.
For completeness, if a prime p divided all coefficients of F_g, reduction modulo p would give
\[
 \overline P_L(\overline g^*/\overline g)=0
 \quad\hbox{in }\mathbb F_p(z).
\]
Primitivity and fixed-length reversal ensure that both reduced polynomials are nonzero, even when their degrees drop.
A rational function over F_p algebraic over F_p is constant, so the ratio would be c in F_p^*.
Applying fixed-length k reversal to \overline g^*=c\overline g gives c^2=1.
But P_L(1) and P_L(-1) are both units modulo p, a contradiction.
Thus F_g has content one.
In particular, |ell|>=2 already forces m(F_g)>=log 2; any positive-to-zero whole-output construction of this form must eventually solve ell=1 or ell=-1.
This is only an exact coefficient constraint, not a classification of its integral solutions.

On the unit circle |R(z)|=1, but the pushforward of circle measure need not be Haar measure or the Poisson measure used in v2.
With normalized circle measure mu the complete identity is
\[
 m(F_g)=10m(g)+\int_{\mathbb T}\log|P_L(R(z))|\,d\mu(z).
 \tag{M4}
\]
All logarithmic singularities here are integrable because the nonconstant rational map has no circle pole and F_g is a nonzero polynomial.
Equation (M4) retains the whole denominator cost; circle preservation alone does not evaluate its second term.

The norm failure can be stated exactly.
Let beta be an algebraic unit, let alpha=R(beta), let K=Q(alpha) be a subfield of L=Q(beta), and put gamma=Norm_(L/K)(beta).
For each embedding sigma:K into C define
\[
 A_\sigma=\sum_{\tau|_K=\sigma}\log^+|\tau\beta|,
 \qquad
 B_\sigma=\sum_{\tau|_K=\sigma}\log^-|\tau\beta|,
 \qquad \log^-r=\max(0,-\log r).
\]
If f is the monic minimal polynomial of beta, then
\[
 m(f)=[K:\mathbb Q(\gamma)]m(\gamma)
       +\sum_\sigma\min(A_\sigma,B_\sigma).
 \tag{M5}
\]
Indeed log|sigma gamma|=A_sigma-B_sigma and
A_sigma=max(A_sigma-B_sigma,0)+min(A_sigma,B_sigma).
The multiplicity of each embedding of Q(gamma) in the sum over K is [K:Q(gamma)].
The same-side fiber property in v2 makes every minimum zero.
Mixed fibers may instead have a torsion norm while their entire positive cost lies in this additional term.

There is also a useful boundary for the norm of a complete fiber.
If the actual relative degree [L:K] equals k, then the full fiber polynomial g^*-alpha g is a scalar multiple of the minimal polynomial over K, and
\[
 \gamma=(-1)^k\,\frac{b-a\alpha}{a-b\alpha}.
 \tag{M6}
\]
The denominator is assumed nonzero, as required for a degree-k fiber.
For real integers a,b with a^2 unequal to b^2,
\[
 |\sigma\gamma|^2-1
 =\frac{(a^2-b^2)(|\sigma\alpha|^2-1)}
        {|a-b\sigma\alpha|^2}.
 \tag{M7}
\]
Thus a nontorsion unit alpha forces this complete-fiber norm to be nontorsion.
When a=b the norm in (M6) is (-1)^k, and when a=-b it is (-1)^{k+1}.
Neither the formula for a full fiber nor nontorsion of its complete product establishes the corresponding assertion for every proper irreducible factor of that fiber.

<a id="actual-torsion-norm-control"></a>
## A genuine torsion relative norm

Take
\[
 g(z)=z^2-z-1,\qquad g^*(z)=-z^2-z+1,\qquad
 \alpha=(1+\sqrt5)/2.
\]
The two roots of g have product -1, one is inside the unit circle and one is outside.
The polynomials g and g^* have no common root.
For the unit source polynomial P(x)=x^2-x-1, the pullback is
\[
 (g^*)^2-gg^*-g^2
 =f(z)=z^4+4z^3-3z^2-4z+1.
 \tag{M8}
\]
Set
\[
 u=\frac{\alpha-1}{\alpha+1}=2\alpha-3=\sqrt5-2.
\]
Its fiber equation is beta^2-u beta-1=0.

The polynomial f is irreducible over Q.
It has no rational linear factor because f(1)=f(-1)=-1 and the constant coefficient is one.
A factorization into monic integer quadratics would have both constant coefficients +1 or both -1.
In the first case the coefficients of z^3 and z would be equal, contrary to 4 and -4.
In the second case the linear coefficients a,b would satisfy a+b=4 and ab=-1, which have no integer solution.
Gauss's lemma exhausts all possible factorizations.

Thus beta is a unit of degree four, Q(alpha) is contained in Q(beta), and the actual relative degree is two.
The inclusion follows either from alpha=R(beta) or from u=beta-beta^{-1} and alpha=(u+3)/2.
The actual relative norm is therefore
\[
 \operatorname{Norm}_{\mathbb Q(\beta)/\mathbb Q(\alpha)}(\beta)=-1.
 \tag{M9}
\]
For the two source embeddings, u takes the values sqrt5-2 and -sqrt5-2.
Each real quadratic beta^2-u beta-1 has one root inside and one outside the circle.
Its positive logarithmic cost cancels in the norm.
This is a concrete failure of the old norm equality outside its hypotheses, not a Lehmer counterexample or a statement that arbitrary mixed maps admit measure descent.

<a id="quadratic-mixed-pullback-full-cost"></a>
## The quadratic family and every root cost

For a nonzero integer t put
\[
 g_t(z)=z^2-tz-1,\qquad
 g_t^*(z)=-z^2-tz+1,\qquad
 H_t(z)=g_t(z)^{10}P_L(g_t^*(z)/g_t(z)).
 \tag{M10}
\]
The roots of g_t have product -1 and distinct moduli on opposite sides of the unit circle.
A common root of g_t and g_t^* would, by their sum -2tz, be zero, which is impossible.
Their leading and constant coefficients are 1 and -1.
Equation (M3) and P_L(-1)=1 therefore make H_t a monic reciprocal integer polynomial of degree 20 with constant coefficient one and content one.

For each of the ten source roots alpha_sigma put
\[
 u_\sigma=\frac{\alpha_\sigma-1}{\alpha_\sigma+1}.
\]
Direct expansion gives
\[
 g_t^*-\alpha_\sigma g_t
 =-(1+\alpha_\sigma)(z^2-tu_\sigma z-1).
\]
Since the product of the ten scalar factors equals P_L(-1)=1, the complete factorization over the source splitting field is
\[
 H_t(z)=\prod_{\sigma=1}^{10}(z^2-tu_\sigma z-1).
 \tag{M11}
\]
No relative irreducibility assumption is used.
Also alpha_sigma+1 is a unit because P_L(-1)=1.
Thus u_sigma is an algebraic integer and every root of every quadratic in (M11) is an algebraic unit, consistently with the monic integer output.

Let x_0=lambda+lambda^{-1}>2 be the exterior trace root of Q and let y_1,...,y_4 be its four roots in (-2,2).
Define
\[
 u_0=\frac{\lambda-1}{\lambda+1}
     =\sqrt{\frac{x_0-2}{x_0+2}}>0,\qquad
 \Psi(v)=
 \begin{cases}0,&0\le v\le1,\\
 \operatorname{arcosh}(v),&v>1.
 \end{cases}
\]
For a real parameter a, the roots of z^2-az-1 contribute asinh(|a|/2) to the sum of positive logarithms.
For a purely imaginary parameter is, the roots of z^2-is z-1 lie on the unit circle when |s|<=2.
When |s|>2, exactly one root is outside and its logarithm is arcosh(|s|/2).
The conjugate source embedding contributes the same amount.
Since
\[
 \frac{e^{i\theta}-1}{e^{i\theta}+1}
   =i\tan(\theta/2),\qquad
 |\tan(\theta/2)|=\sqrt{\frac{2-y}{2+y}},
\]
the exact full measure is
\[
 m(H_t)=
 2\operatorname{asinh}\left(\frac{|t|u_0}{2}\right)
 +2\sum_{j=1}^{4}
   \Psi\left(\frac{|t|}{2}\sqrt{\frac{2-y_j}{2+y_j}}\right).
 \tag{M12}
\]
The factor two in each circle term counts the two conjugate source embeddings, not two exterior roots of a single quadratic.
The leading coefficient has already been fully paid in (M11).

This expression is strictly increasing as a function of |t|>0 because the real-pair term is strictly increasing and all other terms are nondecreasing.
Moreover
\[
 Q(-2)=-1,\qquad Q(-3/2)=3/32>0.
\]
At least one trace root therefore lies in (-2,-3/2).
Its square-root ratio in (M12) is greater than sqrt7, and for every nonzero integer t,
\[
 m(H_t)>2\operatorname{arcosh}(\sqrt7/2)>\log2.
 \tag{M13}
\]
The second strict inequality follows from
arcosh(sqrt7/2)=log((sqrt7+sqrt3)/2) and ((sqrt7+sqrt3)/2)^2>2.
The complete output cost is consequently large; for t=1 this occurs even though the positive real source pair contracts.

For t=1 the circle map is explicitly
\[
 R(e^{i\theta})
 =\frac{1+2i\sin\theta}{1-2i\sin\theta}.
 \tag{M14}
\]
Its image is the arc with real part at least -3/5.
The omitted source arc accounts for the nonunit-modulus fibers charged in (M12).
At t=0, excluded above, g_0^*=-g_0 and the output is (z^2-1)^{10}, so this boundary degenerates to zero measure and a constant rational map.

<a id="iterated-mixed-pullback-normalization"></a>
## The actual growing-degree iteration

Fix g=g_1 and R=g^*/g.
To keep all signs visible, first define raw polynomials
\[
 W_0=P_L,\qquad D_n=10\cdot2^n,\qquad
 W_{n+1}(z)=g(z)^{D_n}W_n(R(z)).
 \tag{M15}
\]
This is a genuine iteration of the quadratic rational map, not substitution by a monomial.
The initial polynomial has even degree, and the identities
\[
 R(1)=R(-1)=1,\quad R(0)=R(\infty)=-1,\quad
 g(1)=-1,\quad g(-1)=1,\quad g(0)=-1
 \tag{M16}
\]
give, inductively,
\[
 W_n(1)=-1\quad(n\ge0),\qquad
 W_0(-1)=1,\qquad W_n(-1)=-1\quad(n\ge1).
 \tag{M17}
\]
The leading and constant coefficients of W_{n+1} both equal W_n(-1).
They are nonzero, so its degree is exactly 2D_n.
Expansion proves integer coefficients at every stage, while reversal and reciprocity of W_n prove reciprocity of W_{n+1}.
The leading coefficient is +1 for W_0,W_1 and -1 for W_n with n>=2.
There is no nontrivial content.

The positive-leading normalization is
\[
 P_0=W_0,\qquad P_1=W_1,\qquad P_n=-W_n\quad(n\ge2).
 \tag{M18}
\]
Thus P_n is monic reciprocal of degree D_n with constant coefficient one.
Its endpoint values are
\[
 (P_0(1),P_0(-1))=(-1,1),\quad
 (P_1(1),P_1(-1))=(-1,-1),\quad
 (P_n(1),P_n(-1))=(1,1)\ (n\ge2).
 \tag{M19}
\]
These sign changes do not change roots or measures.

No root of an output is a zero of g.
Indeed, at a zero of g the homogeneous expression for W_{n+1} reduces to the nonzero leading coefficient of W_n times (g^*)^{D_n}, which is nonzero because g and g^* are coprime.
Hence if beta is a root of P_n, n>=1, then alpha=R(beta) is a well-defined root of P_{n-1}.
Repeating this gives a root R^n(beta) of P_L, with no pole along the orbit.

No P_n has a cyclotomic factor.
For n=0 this is part of the source description.
For n>=1, suppose that a root beta were a root of unity.
Every conjugate of beta is on the unit circle.
The map R has no pole on that circle and maps it into itself, so every conjugate of R^n(beta) lies on the unit circle.
Every embedding of Q(R^n(beta)) extends to Q(beta), so this would put every conjugate of the root R^n(beta) of the irreducible P_L on the unit circle.
That contradicts lambda>1.
Thus every irreducible factor of P_n is a noncyclotomic monic unit polynomial and has positive measure.

<a id="iterated-mixed-pullback-half-value"></a>
## An integral binomial at every actual factor root

Let n>=1, let f be any irreducible factor of P_n, choose its monic representative, let beta be a root, and write e=deg f.
The preceding section makes beta an actual nontorsion unit of degree e.
Let alpha=R(beta), a root of P_{n-1}.
The endpoint unit P_{n-1}(-1)=+/-1 gives an explicit integral inverse:
write
\[
 P_{n-1}(x)=P_{n-1}(-1)+(x+1)B(x),\qquad B\in\mathbb Z[x].
\]
Then
\[
 (\alpha+1)^{-1}=-B(\alpha)/P_{n-1}(-1)
 \in\mathbb Z[\alpha]\subseteq O_{\mathbb Q(\beta)}.
 \tag{M20}
\]
In particular this uses the original full ring of integers and no reduction-order or squarefreeness assumption.

The fiber equation is
\[
 \beta^2-u\beta-1=0,\qquad
 u=\frac{\alpha-1}{\alpha+1}
   =1-\frac{2}{\alpha+1}.
\]
Consequently
\[
 \beta^2-\beta-1=-\frac{2\beta}{\alpha+1}
       \in2O_{\mathbb Q(\beta)},\qquad
 \beta^2+\beta+1\in2O_{\mathbb Q(\beta)}.
\]
Multiplication by beta-1 yields the supplied binomial
\[
 v=\frac{\beta^3-1}{2}
   =(\beta-1)\left(\beta+1-\frac{\beta}{\alpha+1}\right)
   \in O_{\mathbb Q(\beta)}.
 \tag{M21}
\]
Its period is three at every level and for every actual factor.
It does not require that an entire fiber be irreducible or that taking powers preserve degree.

<a id="iterated-mixed-pullback-factor-floor"></a>
## The original norm pays each factor and the whole output

The needed return is exactly the accepted [original binomial norm argument](../claims/Yin_C_G0864_v2.md#original-binomial-norm-return), equations (BP13)--(BP14).
Here is its direct specialization, retaining the original degree e.
Since beta is nontorsion, v and v+1 are nonzero, and (M21) gives
\[
 \frac{\beta^6-1}{4}=v(v+1)
        \in O_{\mathbb Q(\beta)}\setminus\{0\}.
\]
Taking its nonzero integral norm proves
\[
 \left|\operatorname{Norm}_{\mathbb Q(\beta)/\mathbb Q}
       (\beta^6-1)\right|\ge4^e.
 \tag{M22}
\]
For the e actual conjugates beta_j,
\[
 |\beta_j^6-1|
 \le1+|\beta_j|^6
 \le2\max(1,|\beta_j|^6).
\]
At least one beta_j has modulus different from one, by Kronecker and nontorsion, so the second inequality is strict for at least one conjugate.
Multiplying gives
\[
 4^e
 \le\left|\operatorname{Norm}(\beta^6-1)\right|
 <2^e\exp(6m(f)).
\]
Therefore every actual irreducible factor satisfies
\[
                 m(f)>\frac{e\log2}{6}.
 \tag{M23}
\]
In fact Q(R^n(beta)) is a degree-ten subfield of Q(beta), so e is a positive multiple of ten and m(f)>(5/3)log2.
The degree-proportional form is the useful complete-output statement.

All factors are positive and their degrees, counted with multiplicities, sum to D_n.
Additivity of logarithmic measure therefore gives
\[
       m(P_n)>\frac{D_n\log2}{6}
             =\frac{10\cdot2^n\log2}{6}
       \qquad(n\ge1).
 \tag{M24}
\]
Even if the number of irreducible factors grows, none can supply a positive-to-zero sequence.
This is stronger than merely observing that the whole measure fails to decrease.
It uses neither a conjecture about factor production nor the finite-Blaschke norm equality invalidated by (M9).

<a id="bounded-degree-parity-extension"></a>
## A bounded-degree parity extension and its iteration boundary

A finite extension identifies which part of this obstruction survives beyond the selected quadratic.
Let P be a monic integer polynomial with constant coefficient +/-1 and P(-1)=+/-1.
Let g in Z[z] have degree k>=1, leading and constant coefficients each in {1,-1}, gcd(g,g^*)=1 over Q[z], and
\[
                         g^*\equiv g\pmod2.
 \tag{M25}
\]
Consider an actual positive irreducible unit factor f of the primitive output g^{deg P}P(g^*/g), with root beta and degree e.
Coprimality makes alpha=R(beta) well defined.
It is a root of P, and the same polynomial division as in (M20) gives (alpha+1)^{-1} in O_Q(beta).
Put h=(g+g^*)/2 in Z[z].
Since g^*(beta)=alpha g(beta),
\[
                    \frac{g(\beta)}2
                 =\frac{h(\beta)}{\alpha+1}
                 \in O_{\mathbb Q(\beta)}.
 \tag{M26}
\]

The finite ring A=F_2[z]/(\overline g) has exactly 2^k elements, and the residue of z is a unit because the constant coefficient of \overline g is one.
Its multiplicative order L therefore satisfies
\[
       1\le L\le|A^\times|\le2^k-1,\qquad
       \overline g\mid z^L-1.
 \tag{M27}
\]
This uses the full finite ring, so repeated factors of \overline g are retained.
Lift the quotient polynomial to Z[z] and write z^L-1=qg+2s with q,s in Z[z].
Equation (M26) then gives
\[
                    (\beta^L-1)/2
                     =q(\beta)g(\beta)/2+s(\beta)
                     \in O_{\mathbb Q(\beta)}.
\]
The same nonzero norm proof with 3 replaced by L proves
\[
        m(f)>\frac{e\log2}{2L}
             \ge\frac{e\log2}{2(2^k-1)}.
 \tag{M28}
\]
If an actual primitive positive-leading irreducible factor is not a monic unit polynomial, its measure is instead at least log2.
Indeed a leading coefficient of absolute value at least two pays log2 directly; otherwise a nonunit constant coefficient pays it by the product of its nonzero roots.
A zero constant coefficient cannot occur in an irreducible representative other than z, whose measure is zero and which is excluded by the positive-factor hypothesis.
Thus bounded k gives a uniform positive-factor floor for this supplied class, while (M28) itself decays as k grows.

The conditions on g do not automatically preserve the source condition P(-1)=+/-1 under iteration.
For example g=z^2-3z-1 satisfies all conditions in (M25), including coprimality, and the Lehmer source gives leading and constant coefficients one.
But g(-1)=3 and R(-1)=1, so
\[
 \bigl(g^{10}P_L(R)\bigr)(-1)=3^{10}P_L(1)=-59049.
 \tag{M29}
\]
Therefore (M28) can be iterated only when the required source endpoint unit is independently verified at every step.
Equations (M17)--(M19) establish precisely that inheritance for g=z^2-z-1.
The extension is an obstruction with explicit supply hypotheses, not a statement about every mixed rational iteration.

<a id="mixed-allpass-reuse-boundary"></a>
## Reuse and actual inspection boundary

The bounded local comparison found related but different previously retained constructions.
[C166](../claims/Yin_C_G0166_v1.md) concerns integral positive linear Mobius contractions.
[C167](../claims/Yin_C_G0167_v1.md) concerns signed quadratic norms of actual trace defects.
[C866 v6](../claims/Yin_C_G0866_v6.md) treats rational linear combinations of Cayley values and their degree and raw second-moment costs.
Those statements do not by themselves cover the inverse quadratic unit fibers in (M11).
The existing [plastic-family phase discussion](Yin_L_G0174_v1.md#primitive-plastic-phase-moments) already uses a rational circle map with mixed interior and exterior zeros, for a different phase and resultant calculation.
No novelty claim about mixed rational circle maps is made here.

The exact source used for the final arithmetic return is C864 v2, whose original full-field binomial-norm paragraph was inspected and whose argument is reproduced in (M22)--(M23).
Its larger four-pair constant is not needed.
No powered-degree-preservation hypothesis or C139 constant comparison is used.
No new external source or numerical factorization is used for this version.
The finite delayed-family results and source-edition limits remain at [v2](Yin_L_G0450_v2.md#mixed-delay-positive-factor-question) and are not broadened by this mixed-map calculation.

<a id="mixed-allpass-outcome-and-limits"></a>
## Outcome and remaining scope

The true torsion norm in (M9) establishes that mixed fibers escape the particular same-side norm mechanism of v2.
The complete cost formula (M12) shows why shrinking the selected real pair does not reduce the full measure for the quadratic integer family.
The degree-growing iteration is excluded more strongly by (M23): every actual factor has a degree-proportional positive lower measure bound.
Its complete measure satisfies (M24), with all coefficients, content, root multiplicities and endpoint signs retained.

The bounded-degree extension (M28) requires both the parity supply and the actual source endpoint unit.
It supplies no degree-uniform assertion when the map degree grows, and (M29) shows that its iteration hypothesis is substantive.
No conclusion is asserted about arbitrary mixed maps, integer sources without these endpoint units, or a new mechanism that avoids the short integral binomial while controlling complete logarithmic cost.
