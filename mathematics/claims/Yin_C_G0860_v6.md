---
author: Yin
---
# Bad-reduction pole excess and an actual nonrational original unit

This project deduction extends the rational-approximation question of [C860 v5](Yin_C_G0860_v5.md#pade-statement) beyond its good-reduction hypothesis.
The complete fixed-center rank and precision theorem remains at [v4](Yin_C_G0860_v4.md#statement), with its [selected assessment](Yin_C_G0860_v4.md#decision-whole-independent-review-2026-11-04).
The exact Padé normalization, good-reduction minimum and stated consequences remain at [v5](Yin_C_G0860_v5.md#pade-statement), with its [selected assessment](Yin_C_G0860_v5.md#decision-whole-independent-review-2026-11-04).
The earlier [v1](Yin_C_G0860_v1.md#statement) and [v2](Yin_C_G0860_v2.md#statement) results retain their complete fixed statements, proofs and actual assessments at those homes.
No prior review is transferred to this new argument.

The precision-varying-approximants contributor developed the new proof for Yin.
The coordinating agent checked the homogeneous degree accounting, finite gcd form and rank-one control as a contributor.
Those contributor checks are distinct from this version's selected independent whole assessment.
No numerical probe or rolling Draft is a proof premise.
The control has total measure greater than log 2; no sharp all-rank profile, uniformly favorable near-one input supply or unrestricted total Mahler gap is claimed.

## Exact inputs and source scope

The argument uses [C860 v5 (P1)--(P2)](Yin_C_G0860_v5.md#pade-integrality) for its explicit Padé polynomials, integral normalization and exact first error; that input applies without good reduction.
Its [integral rational denominator lemma](Yin_C_G0860_v5.md#integral-rational-denominator) supplies the normalized integral polynomial pair for every approximant, without a coefficient-size restriction.
Its formal rational-rank convention, composition degree and fixed-unit rank comparison retain the exact adopted Par88/BR10 and Kou11 source scopes already recorded there; no fresh source inspection or novelty claim is made.
The new homogeneous divisor count and the complete original control are proved below.

[C857 v2's coherent-center construction](Yin_C_G0857_v2.md#coherent-centers), at its [selected assessment](Yin_C_G0857_v2.md#decision-whole-independent-review-2026-11-04), identifies the first binary center of the control; its original polynomial and the Artin--Schreier identity are explicitly verified here.
[C858's finite determinant comparison and nonrationality interface](Yin_C_G0858_v1.md#all-place-hankel-budget), at its [selected assessment](Yin_C_G0858_v1.md#decision-whole-independent-review-2026-11-04), supply the all-level arithmetic quadratic coefficient and infinitely many nonzero determinants for the same original germ.
Its [disk calculation](Yin_C_G0858_v1.md#cauchy-radius-cost) and [C855 v2's actual all-root contour](Yin_C_G0855_v2.md#statement), at the latter's [selected assessment](Yin_C_G0855_v2.md#decision-whole-independent-review-2026-11-04), supply only the paid control consequences at the end.
The original-input conditions for those uses are checked in the control itself.

The bounded reuse check found [C135 v2's bad-prime control](Yin_C_G0135_v2.md), which concerns a different two-binomial annihilator budget and is not a proof input here.
The bad-reduction examples in C860 v5 are rational square roots; the present example retains a genuinely nonrational original power-stable germ.
Neither that distinction nor the bounded search establishes novelty.

<a id="bad-reduction-statement"></a>
## Statement

Let \(z=E/D\in\mathbb Q_2(x)\) be nonconstant and reduced, with
\[
 E,D\in\mathbb Z_2[x],\qquad E(0)=0,\qquad D(0)=1,\qquad
 z\notin2\mathbb Z_2[[x]],\qquad
 \delta=\max(\deg E,\deg D)\ge1.
\]
Let \(\lambda\ge3\), \(a=\lambda-2\), and
\[
              y=\sqrt{1+2^\lambda z},\qquad y(0)=1.
\]
For \(s\ge1\), let \(r_s(y)\) be the least shifted Hankel rank over \(\mathbb Q_2\) of an integral rational power series agreeing with \(y\) modulo \(2^s\), exactly as in C860 v5.
No good-reduction condition is imposed.

Homogenize \(E,D\) to the same degree \(\delta\), and denote their nonzero reductions in \(\mathbb F_2[X,Y]\) by \(\overline E_h,\overline D_h\).
Thus, for example, a degree drop in the reduced affine denominator contributes a zero at infinity to \(\overline D_h\).
For every geometric point \(\beta\) of \(\mathbb P^1_{\overline{\mathbb F}_2}\), put
\[
 \mu_\beta=\operatorname{ord}_\beta\overline D_h,\qquad
 \nu_\beta=\operatorname{ord}_\beta\overline E_h.
\]
These are nonnegative zero multiplicities of homogeneous forms.
Both forms are nonzero, and each has total zero multiplicity \(\delta\).
Define, for \(t\ge0\),
\[
 \begin{split}
 L_t&=\sum_\beta
      \max\bigl((t+1)\mu_\beta-(2t+1)\nu_\beta,0\bigr)\\
    &=(t+1)\delta-
       \deg\gcd\bigl(\overline D_h^{\,t+1},
                    \overline E_h^{\,2t+1}\bigr),\\
 \omega&=\sum_\beta\max(\mu_\beta-2\nu_\beta,0)
        =\delta-\deg\gcd(\overline D_h,\overline E_h^2).
 \end{split}                                                    \tag{BR1}
\]
The gcd degrees are homogeneous and include the factor corresponding to infinity.
These formulas are finite calculations on the actual normalized residual.

If \(s>a(2t+1)+1\), then
\[
                             r_s(y)\ge L_t.                \tag{BR2}
\]
More explicitly, for \(s\ge a+2\), set
\[
                 t_s=\left\lfloor
                         \frac{s-a-2}{2a}\right\rfloor .
\]
Then the complete bounds at integer precision levels are
\[
 \max_{0\le t\le t_s}L_t
       \le r_s(y)
       \le\delta\left\lceil\frac{s-a-1}{2a}\right\rceil .
                                                               \tag{BR3}
\]
For \(1\le s\le a+1\), one has \(r_s(y)=0\).
The sequence \(L_t\) is not asserted to be increasing.
Its asymptotic form is
\[
                L_t=t\omega+O(1),
 \qquad
 \frac{\omega}{2a}s+O(1)\le r_s(y)
              \le\frac{\delta}{2a}s+O(1).                 \tag{BR4}
\]
The lower estimate is allowed to have \(\omega=0\).

Let
\[
          \delta_{\rm red}
             =\delta-\deg\gcd(\overline E_h,\overline D_h)
             =\deg(\overline E/\overline D).
\]
At the first precision beyond the constant approximant, there is the exact equality
\[
                         r_{a+2}(y)=\delta_{\rm red}.       \tag{BR5}
\]
If the residual has good reduction, (BR1)--(BR3) recover the exact minimum-rank formula of C860 v5.
Under bad reduction, no equality between the two asymptotic slopes in (BR4) is asserted.

If \(S\in\mathbb Q_2(x)\) and \(S,S^{-1}\in\mathbb Z_2[[x]]\), set \(G=Sy\) and \(h=\rho(S)\).
Define \(r_s(G)\) by the same approximant class with \(G\) in place of \(y\).
Then
\[
                         |r_s(G)-r_s(y)|\le h.             \tag{BR6}
\]
In particular every bound above transfers to a fixed rational unit multiplier with an additive error independent of precision.

<a id="argument"></a>
<a id="bad-reduction-argument"></a>
## Complete lower-bound proof

Use C860 v5's explicit odd Padé approximant \(P_t/Q_t\) with
\[
 P_t=D^t p_t(1+2^\lambda z),\qquad
 Q_t=D^t q_t(1+2^\lambda z),\qquad n=2t+1.
\]
The adopted formulas (P1)--(P2), which require no good reduction, give integral polynomials of degrees at most \(t\delta\), constant terms one, and
\[
 \overline{P_t}=\overline{Q_t}=\overline D^{\,t},
 \qquad
 \overline{\frac{y-P_t/Q_t}{2^{a(2t+1)+1}}}
                     =(\overline E/\overline D)^{2t+1}.
                                                               \tag{BR7}
\]
The error depth is exact.
Homogenizing \(P_t,Q_t\) to degree \(t\delta\) therefore gives reductions \(\overline D_h^t\), including all factors at infinity.

Let \(A/B\) be any integral rational approximant of shifted rank \(r\) at a precision \(s>a(2t+1)+1\).
The integral-denominator lemma in C860 v5 gives a reduced representation with \(A,B\in\mathbb Z_2[x]\), \(B(0)=1\), and \(\deg A,\deg B\le r\).
Put \(s_t=a(2t+1)+1\).
The polynomial
\[
                        H=(A Q_t-P_t B)/2^{s_t}
\]
is integral and has degree at most \(r+t\delta\).
Indeed the difference of the two integral rational series has depth \(s_t\), and multiplication by the integral units \(B Q_t\) preserves coefficient divisibility.
Homogenize \(A,B\) to degree \(r\), \(P_t,Q_t\) to degree \(t\delta\), and \(H\) to degree \(r+t\delta\).
Equation (BR7) gives the identity of homogeneous rational expressions
\[
          \overline H_h
             =\frac{\overline B_h\,
                         \overline E_h^{\,2t+1}}
                        {\overline D_h^{\,t+1}}.           \tag{BR8}
\]
Both sides have degree \(r+t\delta\).
The form \(\overline B_h\) is nonzero because \(B(0)=1\).
The right side, and hence \(\overline H_h\), is nonzero.

At every projective point \(\beta\), regularity of the polynomial form on the left forces
\[
       \operatorname{ord}_\beta\overline B_h
          \ge\max\bigl((t+1)\mu_\beta-(2t+1)\nu_\beta,0\bigr).
\]
A nonzero homogeneous form of degree \(r\) has exactly \(r\) zeros counted with multiplicity on the projective line over the algebraic closure.
Summing proves (BR2).
Writing the sum through common zero multiplicities proves the gcd expression for \(L_t\).
For each fixed pair of multiplicities,
\[
 \max\bigl(t(\mu_\beta-2\nu_\beta)+\mu_\beta-\nu_\beta,0\bigr)
          =t\max(\mu_\beta-2\nu_\beta,0)+O(1).
\]
Only finitely many terms occur, so this also proves the expression for \(\omega\) and the asymptotic lower bound in (BR4).
No zero or common factor at infinity has been discarded.

For a fixed precision \(s\), all \(t\) from zero through \(t_s\) are available, proving the lower part of (BR3).
C860 v5's explicit approximant at index \(\max(0,\lceil(s-a-1)/(2a)\rceil)\) supplies the upper part and the zero-rank range.
This proves all the claimed integer-precision bounds without presuming monotonicity of \(L_t\).

For (BR5), the lower bound at \(t=0\) is \(L_0=\delta_{\rm red}\).
Write the reduced residue rational function as \(e_0/d_0\), normalized by \(e_0(0)=0,d_0(0)=1\), and choose coefficient lifts \(E_0,D_0\) of the same degrees to \(\mathbb Z_2[x]\).
The rational function
\[
                        1+2^{a+1}E_0/D_0
\]
has shifted rank at most \(\delta_{\rm red}\) and agrees with \(y\) modulo \(2^{a+2}\).
The first binomial term is \(2^{a+1}z\); all subsequent terms are divisible by \(2^{2a+1}\), which is contained in \(2^{a+2}\) because \(a\ge1\).
The lift changes the first term by a multiple of \(2^{a+2}\).
This proves the matching upper bound.

Finally, multiplication or division by \(S\) preserves all the coefficientwise congruences because both are integral series.
The elementary rational-degree inequalities
\[
 \rho(FS)\le\rho(F)+\rho(S),\qquad
 \rho(F)\le\rho(FS)+\rho(S)
\]
give (BR6).
This part of C860 v5's multiplier argument does not need good reduction.

<a id="actual-quadratic-bad-reduction-control"></a>
## An actual original polynomial with a strictly better bad-reduction approximation family

Take the original polynomial
\[
                  P(t)=t^2-4t+1,\qquad \alpha=2+\sqrt3.
\]
Its roots are \(\alpha,\alpha^{-1}\); it is irreducible, reciprocal and monic with constant term one.
All positive powers retain degree two, since the two real positive conjugate powers are distinct.
Its total measure is
\[
                       m(P)=\log(2+\sqrt3)>\log2.
\]
Thus this is an actual power-stable unit, but is already above the old gap range and supplies no near-one family.
Its original powered polynomials and radical are
\[
 U=1-14x+x^2,\qquad V=1-194x+x^2,\qquad
 G=\sqrt{V/U},\quad G(0)=1.
                                                               \tag{BR9}
\]
The four roots of \(UV\) are distinct, so \(G\) is nonrational.
Every root and the original variable have been retained.

The first original residual is
\[
 \overline{(V-U)/(4U)}
       =\frac{x}{(1+x)^2}
       =\left(\frac{x}{1+x}\right)^2+\frac{x}{1+x}.
\]
C857's binary coherent lift therefore gives the center
\[
            S_0=\frac{1+3x}{1+x},\qquad R_0=\frac{G^2}{S_0^2}.
\]
The exact polynomial identity is
\[
 V(1+x)^2-U(1+3x)^2
                  =-8x(23+39x+9x^2+x^3).                  \tag{BR10}
\]
Its coefficient depth is exactly three.
The reduced characteristic-zero degree of \((R_0-1)/8\) is four, whereas its residue function is
\[
                      \frac{x}{1+x}.
\]
Indeed its numerator and denominator reductions before cancellation are \(x(1+x)^3\) and \((1+x)^4\).
The homogeneous pole-excess coefficient \(\omega\) is zero for this presentation.
The failure of good reduction is a common-factor loss of three degrees, on a genuinely nonrational original germ.

A different degree-one rational center is
\[
            S_1=\frac{1-45x}{1+45x},\qquad R_1=\frac{G^2}{S_1^2}.
\]
Here
\[
 \begin{split}
 V(1+45x)^2-U(1-45x)^2
    &=-18720x^2-364320x^3\\
    &=-32\cdot45x^2(13+253x).
 \end{split}                                                    \tag{BR11}
\]
The depth is exactly five.
The residual \(z_1=(R_1-1)/32=E/D\) is reduced over \(\mathbb Q_2\), with
\[
          E=-45x^2(13+253x),\qquad
          D=U(1-45x)^2,\qquad \delta=4.
\]
Reducedness follows also directly by evaluating (BR11) at the roots of \(U\) and \(1-45x\), where the complementary term \(V(1+45x)^2\) is nonzero.
Its homogeneous reductions are
\[
        \overline D_h=(X+Y)^4,\qquad
        \overline E_h=X^2Y(X+Y).                           \tag{BR12}
\]
Thus the only positive pole-excess contribution comes from \(X+Y=0\), with \(\mu=4,\nu=1\).
Consequently
\[
                \omega=2,\qquad L_t=2t+3,\qquad
                \delta_{\rm red}=3.                       \tag{BR13}
\]
This presentation still has bad reduction; its residue is \(x^2/(1+x)^3\).
Good-reduction optimality has not been silently imported.

For \(\ell=0,1\), take the explicit odd Padé approximant for \(\sqrt{R_\ell}\) and multiply by \(S_\ell\).
Their exact error depths and exact shifted ranks, for every \(t\ge0\), are
\[
 \begin{array}{c|c|c}
 \text{center}&v_2(G-\text{approximant})&\text{shifted rank}\\ \hline
 S_0&2t+2&4t+1\\
 S_1&6t+4&4t+1 .
 \end{array}                                                    \tag{BR14}
\]
The exact errors follow from C860 v5 (P2), since both centers are integral rational units.
For the ranks, each \(R_\ell\) is a reduced degree-four rational map.
The degree-\(t\) rational Padé function has neither zero nor pole at zero or infinity: its values there are \(1/(2t+1)\) and \(2t+1\), respectively.
All of its \(4t\) pulled-back poles are therefore away from the zero and pole of \(S_\ell\).
There is also no pole at the original point infinity.
Indeed \(R_0(\infty)=1/9\), \(R_1(\infty)=1\), and the Padé denominator has positive coefficients and does not vanish at either positive value.
Multiplication by \(S_\ell\) adds exactly its one pole, with no cancellation.
The formal rational-rank identity proves the ranks in (BR14), including \(t=0\).

Applying (BR3) and (BR6) to \(S_1\), whose rank is one, gives, for every \(s\ge5\),
\[
 2\left\lfloor\frac{s-5}{6}\right\rfloor+2
       \le r_s(G)
       \le4\max\!\left(0,\left\lceil\frac{s-4}{6}\right\rceil\right)+1.
                                                               \tag{BR15}
\]
In particular
\[
 \frac13\le\liminf_{s\to\infty}\frac{r_s(G)}s
       \le\limsup_{s\to\infty}\frac{r_s(G)}s\le\frac23 .
                                                               \tag{BR16}
\]
The new explicit family has a strictly smaller rank-growth upper bound than the slope \(2\) of the old \(S_0\) family.
Since multiplication by \(S_0\) changes minimum ranks by only a bounded amount, this actual nonrational example also disproves extension of C860 v5's equality \(r_s=\delta s/(2a)+O(1)\) to arbitrary bad reduction.
No sharp all-rank slope for this control is asserted.

## Exact rank-one optimum

For this \(G\), one has
\[
 r_1(G)=0,\qquad r_s(G)=1\quad(2\le s\le4),\qquad
 r_s(G)\ge2\quad(s\ge5).                                   \tag{BR17}
\]
The first coefficient of \(G\) is \(-90\), so a constant approximant cannot reach precision two.
Equation (BR10) gives \(G\equiv S_0\equiv1\pmod2\), so precision one is attained by the constant one.
The center \(S_1\) reaches precision four by (BR11).
It remains to exclude every rank-one integral rational approximant at precision five.

By the integral-denominator lemma, such an approximant has the form
\((c_0+cx)/(1+bx)\), with \(b,c,c_0\in\mathbb Z_2\).
Precision five forces \(c_0\equiv1\pmod{32}\).
Replacing \(c_0\) by one preserves that precision and does not increase rank.
The resulting rational function \(T=(1+cx)/(1+bx)\) satisfies \(T\equiv G\equiv1\pmod2\).
Hence \((G+T)/2\) is an integral series with constant coefficient one.
The identity
\[
 V(1+bx)^2-U(1+cx)^2
           =U(1+bx)^2(G-T)(G+T)
\]
shows that precision five would force every coefficient on the left to be divisible by \(64\).

Put \(d_0=b-c\) and \(e_0=b+c\).
The coefficients of \(x,x^2,x^4\), respectively, on that left side are
\[
       2(d_0-90),\qquad
       e_0(d_0-180)-208d_0,\qquad d_0e_0.
                                                               \tag{BR18}
\]
The first coefficient forces \(d_0\equiv90\pmod{32}\), so \(v_2(d_0)=1\).
The last coefficient then forces \(e_0\in32\mathbb Z_2\).
It follows that \(e_0(d_0-180)\) is divisible by \(64\), whereas \(208d_0\) has valuation exactly five.
The middle coefficient in (BR18) therefore has valuation five, a contradiction.
This proves (BR17) for all integral \(\mathbb Q_2\)-rational approximants, without a coefficient-size restriction.

## Original-input return and remaining scope

The improved family in (BR14) has precision \(6t+4\) and rank \(4t+1\).
C858's all-level determinant comparison therefore gives the arithmetic quadratic coefficient \((3/4)\log2\) on the same original shifted Hankel determinants.
The old disk comparison yields
\[
                         m(P)\ge\frac{3\log2}{16}.
\]
C855 v2's actual all-root contour, with one used rotation and \(E_2=m(P)^2\) on this quadratic unit, also gives the coarse consequence
\[
                         m(P)\ge\sqrt{\frac{3\log2}{20}}.
\]
These are paid consequences of the same original function, not new estimates on a variable near-one family.
The actual control already has \(m(P)>\log2\).

The general result (BR1)--(BR6) supplies a finite bad-reduction lower bound for arbitrary rational approximants and an exact first-step rank.
It does not classify all higher layers when common factors make the bounds different.
The example establishes that genuine nonrational original inputs can beat the apparent rank slope of a bad presentation, while keeping every degree and precision cost.
A sharp all-rank profile, a corresponding uniformly favorable near-one supply, and the unrestricted positive total Mahler gap remain unresolved.

## Current assessment
[Selected decision](#decision-whole-independent-review-2026-11-04)

## Assessment history

### Decision whole-independent-review-2026-11-04

| Field | Value |
| --- | --- |
| date | 2026-11-04T22:09 |
| status | proved |
| reason | Adopt complete BR1--BR18 and both paid original-input consequences after independent R1076 v5. The projective pole-excess bound covers all integral Q2-rational approximants under bad reduction, with infinity retained, exact first-step rank and fixed-unit transfer. The actual nonrational quadratic control has rigorously better approximants and an exact rank-one precision limit, while its higher-rank slope remains between the stated bounds. Earlier fixed scopes and accepted-source limits remain unchanged; no favorable near-one supply or unrestricted G0001 conclusion is established. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [General statement](#bad-reduction-statement) | Complete BR1--BR6, all integer precisions, homogeneous gcd bounds including infinity, first-step equality and fixed rational-unit comparison. |
| argument | [Complete argument and original control](#argument) | All BR1--BR18, actual power-stable input, both exact families, universal rank-one exclusion, global integer germ and the same-determinant disk/contour consequences. |
| dependency | [Exact Pade identities](Yin_C_G0860_v5.md#pade-integrality) | P1--P2 normalization, exact errors and characteristic-zero map degree without the good-reduction hypothesis. |
| dependency | [Integral rational denominators](Yin_C_G0860_v5.md#integral-rational-denominator) | All integral Q2-rational Taylor series and polynomial-inclusive shifted rank, with no coefficient-size restriction. |
| dependency | [Coherent original center](Yin_C_G0857_v2.md#coherent-centers) | Actual binary h=x/(1+x), integer lifts, S0 and global original-series integrality. |
| dependency | [Finite Hankel and nonrationality interfaces](Yin_C_G0858_v1.md#all-place-hankel-budget) | All-level valuation summation and accepted shifted leading-Hankel criterion for the newly verified integral germ, without importing the old uncentered modulo-eight premise. |
| dependency | [Original disk cost](Yin_C_G0858_v1.md#cauchy-radius-cost) | Same original radius and h-squared cost, nonzero subsequence and fixed-input order of limits. |
| dependency | [All-root contour](Yin_C_G0855_v2.md#statement) | Only accepted Part C for the same germ and determinants, one rotation, E2=m(P)^2 and Phi1(0)<=5E2. |
| review | [Independent whole finding](../audits/reviews/Yin_R_G1076_v5.md#bad-reduction-whole) | Complete BR1--BR18, actual control, rank-one optimum, exact source interfaces and both paid original-input returns, preserving all unresolved scope. |
