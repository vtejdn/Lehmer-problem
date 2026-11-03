---
author: Yin
---
# A necessary dyadic multiplicity ratio in the actual quadratic support family

Date: 2026-10-20T13:34.
Human author Yin.
The complete author argument QR1--QR19 was developed on2026-10-20T13:28 and is retained here at its original mathematical scope.
Root supplied the three-factor support family, the coefficient argument producing a small matching root, the ratio N=7A, the derivative parity refinement and the square-lift construction.
The draft_comparison_cleanup agent developed the full proof, checked both actual divided-quotient valuations and all multiplicities, and supplied the explicit A=2 finite-ring example.
Both are contributors to this theorem.
The generic half-difference identities were already used in the earlier specific-shape development by root and entropy_attainment_bridge, now fixed in C196v3; that upstream contribution is disclosed separately from the new parameterized argument.
No independent review or adoption of the present theorem is claimed.
No mathematical program, coefficient scan or new source theorem is used.

<a id="statement"></a>
## Complete statement

Let P, K, F, delta and T have the complete original meaning of [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
In particular P is monic irreducible reciprocal nontorsion in Z[z], its degree is d=2r, its constant coefficient is1, F=Q(delta) is totally real with actual monic degree-r trace polynomial T, and P(z)=z^r T(z+z^(-1)).
Set C2=X^2-2, C3=X^3-3X and C5=X^5-5X^3+5X.
Write theta_p=rem_T(T(C_p))/p in Z[X] for p=2,3,5 and use the actual nonzero integral values a=theta_2(delta), b=theta_3(delta), c=theta_5(delta).
Assume the FULL exact residual equations

    2c^2-3a^5=0,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0, s in{1,-1}.                  (QR1)

Define G_can=rem_T(theta_5^3-2theta_3^5) in Z[X], the actual canonical representative of g.
The uppercase parameters below are multiplicities, distinct from the actual lowercase coordinates a,b,c.
Put Phi=X^2+X+1 in Z[X] and phi=Phi mod2.
Suppose the ENTIRE reduction of T has the prescribed support

    Tbar=X^A(X+1)^B phi^N,
    A>=2, B=0 or B>=2, N>6A.                    (QR2)

There are no additional irreducible factors in this hypothesis.
Then necessarily

    N=7A, r=15A+B,
    A is even,
    either A=2 or B is even.                     (QR3)

Moreover some actual2-adic conjugate delta_0 of the original trace generator satisfies

    v_2(theta_2(delta_0))
       =v_2(theta_5(delta_0))=1/3,                (QR4)

where the extension of the valuation is normalized by v_2(2)=1.
No conclusion that such an original input exists follows from these necessary conditions.

There are also finite-ring-compatible lifts at this necessary ratio for every even A>=2 and B=0, as constructed explicitly in(QR16)--(QR17).
Their actual divided quotients satisfy both residual equations modulo2, including the required mod4 dependence of theta_2, and their canonical gbar is nonzero of exact phi-order6A.
An arbitrary added4W with degree below15A preserves these facts.
For A=2, the explicit family(QR18) has degree30 and canonical reduction X^2(X+1)^2 phi^12 of degree28.
These are statements about the actual quotient polynomials of monic integer T, not claims of irreducibility, total reality or an exact characteristic-zero residual solution for those formal lifts.
They do not determine the parity of the actual integer leading coefficient when canonical degree can drop modulo2.

<a id="argument"></a>
## Complete proof

### Actual quotient classes in the quadratic primary component

Set T_0=X^A(X+1)^B Phi^N, a monic polynomial of the same degree as T.
Write

    T=T_0+2U+4W, U,W in Z[X], deg U,deg W<r.

The polynomial Ubar is determined by T modulo4 relative to this T_0.
Its chosen integer lift and W need not be unique.
The generic half-difference and product identities below reuse the exact algebraic interface in [C196v3](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification).
Only those identities are reused: its specialized degree28 conclusion, its Hensel argument and its global degree bound are not premises here.
The application to all parameters in(QR2) is proved explicitly.
For any integer polynomial F define

    Delta_2(F)=(F(C2)-F^2)/2 in Z[X].

The characteristic-two congruence proves its integrality, and monic division gives theta_2=rem_T Delta_2(T).
A direct expansion and the product rule give

    Delta_2(T) mod2=Delta_2(T_0) mod2+Ubar^2,
    Delta_2(FG) mod2=Fbar^2 Delta_2(G)bar
                         +Gbar^2 Delta_2(F)bar.

Every contribution to Delta_2(T_0) has phi-order at least2N-2.
Indeed applying this product rule to the Phi^N factor leaves Phi^(2N-2), while the contributions from X^A(X+1)^B retain Phi^(2N).
Since N>=2, reduction modulo phi^N therefore yields

    theta_2bar congruent Ubar^2 modulo phi^N.     (QR5)

Passing to the canonical remainder does not change this assertion, because Tbar is divisible by phi^N.
This calculation pays the division by2 before reduction.

Write

    chi=C5bar=X phi^2,
    Psi=phi(chi)=1+X phi^2+X^2 phi^4.

The polynomial C3bar=X^3+X sends a root beta_bar of phi to beta_bar^2, another root of phi.
Its derivative at that root is nonzero.
Both C3bar and C3bar+1 are units at these roots.
Consequently Tbar(C3bar) is divisible by phi^N and

    theta_3bar=0 modulo phi^N,
    theta_5bar congruent
       X^A phi^(2A)(1+X phi^2)^B Psi^N
                                      modulo phi^N. (QR6)

All factors after phi^(2A) on the second line are units at phi.
As N>6A, theta_5bar has exact phi-order2A, and its cube has exact order6A strictly below N.
The second equation in(QR1), reduced modulo phi^N, now gives theta_2bar^3=theta_5bar^3.
The first gives theta_2bar^5=0.
Together with(QR5) these imply

    ord_phi Ubar=A,
    ord_phi theta_2bar=ord_phi theta_5bar=2A,
    N<=10A.                                     (QR7)

These are necessary orders only; equality of those orders is not asserted to suffice for the finite-ring residual equations.
Since ord_phi Ubar=A, choose integer V,Z with U=Phi^A V+2Z and phi not dividing Vbar.
Absorb Z into W, obtaining the exact expression

    T=X^A(X+1)^B Phi^N+2Phi^A V+4W_1,
    phi does not divide Vbar.                    (QR8)

No maximal power-order hypothesis or equality of residue-field degree with2 is used.

<a id="coefficient-forced-matching-root"></a>
### A small matching root from one exact coefficient

Work in a finite splitting field over Q_2 of T Phi, with valuation v normalized by v(2)=1.
Let beta be either root of Phi.
Its residue has degree2, and beta, beta+1 and u_0=2beta+1 are units.
The exact identity

    Phi(beta+Y)=Y(u_0+Y)

shows that the coefficient of Y^A in T(beta+Y) has valuation exactly1.
The first term in(QR8) starts at Y^N, with N>A.
The second contributes precisely2u_0^A V(beta) to this coefficient, of valuation1.
The coefficient contributed by4W_1(beta+Y) has valuation at least2.
Thus

    v([Y^A]T(beta+Y))=1.                         (QR9)

This conclusion is independent of B, because beta and beta+1 are units.

All roots delta_i of the monic integer T are integral.
For example, a root of negative valuation would make the leading monomial in T uniquely smallest in valuation, which cannot sum to zero.
Reducing their full factorization shows that exactly N roots, counted with multiplicity, have residue beta_bar.
For these matching roots put t_i=v(delta_i-beta)>0, allowing infinity when delta_i=beta.
All other roots have v(delta_i-beta)=0.
There are r roots in the product

    T(beta+Y)=product_(i=1)^r (Y-(delta_i-beta)).

Suppose every matching t_i were at least1/A.
Each product contributing to its Y^A coefficient contains r-A root differences and hence at least N-A matching differences.
Every such term has valuation at least(N-A)/A>1.
Their sum has valuation at least the same lower bound, contradicting(QR9).
Therefore some actual root delta_0 of T has

    0<t=v(delta_0-beta)<1/A,
    v(Phi(delta_0))=t.                            (QR10)

The last equality uses the unit u_0+delta_0-beta.
This argument proves the root's existence by the complete coefficient product; it neither assumes a Newton-polygon slope nor invokes a root-lifting theorem.

At delta_0 the three terms of(QR8) have respective valuations

    Nt, 1+At, and at least2.

Here delta_0, delta_0+1 and V(delta_0) are units, and1+At<2.
Since T(delta_0)=0, the minimum cannot be unique.
It follows that Nt=1+At, or

    t=1/(N-A), Nt=1+At,
    0<2At=2A/(N-A)<2/5<1.                       (QR11)

The inequality uses N>6A.
Both the existence and value hold for every higher lift W_1, rather than a specially selected polynomial.

<a id="actual-quotient-multiplicity-ratio"></a>
### The two actual quotients and the forced ratio

Equation(QR5) lifts to an integer polynomial identity

    theta_2-U^2=2E+Phi^N H

for some E,H in Z[X].
At delta_0 its right side has valuation at least1, because Nt=1+At>1.
The decomposition U=Phi^A V+2Z gives v(U(delta_0))=At<1.
As2At<1, the unequal-order rule yields

    v(theta_2(delta_0))=2At.

For theta_5, use the integer polynomial chi_0=X Phi^2, whose reduction is chi.
The actual remainder identity gives theta_5 congruent T_0(chi_0) modulo the ideal(2,T).
Thus at delta_0 the difference theta_5(delta_0)-T_0(chi_0(delta_0)) has valuation at least1.
One has v(chi_0(delta_0))=2t, while chi_0(delta_0)+1 and Phi(chi_0(delta_0)) are units.
Hence v(T_0(chi_0(delta_0)))=2At<1, proving

    v(theta_2(delta_0))
       =v(theta_5(delta_0))=2A/(N-A).             (QR12)

This retains the actual division by2 in theta_2 and by5 in theta_5.
In particular neither quotient has been replaced by a freely chosen nilpotent coordinate.

The original exact equation f=0 is a polynomial identity modulo the minimal polynomial T, and therefore holds at every root of T, including delta_0.
Both quotient values in(QR12) are nonzero.
Equality of the valuations in2theta_5(delta_0)^2=3theta_2(delta_0)^5 gives

    1+4A/(N-A)=10A/(N-A),
    N=7A, v(theta_2(delta_0))
                =v(theta_5(delta_0))=1/3.        (QR13)

Since T is monic and its full reduction is(QR2), r=A+B+2N=15A+B.
This proves the ratio and valuation assertions without a restriction on the original Mahler measure.
Equal valuations at N=7A are only a necessary condition for the exact equation; they do not prove its equality.

<a id="multiplicity-parity-refinement"></a>
### A derivative refinement of the multiplicity parities

Continue with N=7A and write Ubar=phi^A Vbar.
The same quadratic-primary residual identity used in(QR7), after division by phi^(6A), is

    Vbar^6 congruent H_0 modulo phi^A,
    H_0=X^(3A)(1+X phi^2)^(3B) Psi^(3N).         (QR14)

The derivative of Vbar^6 is zero in characteristic2.
Also(1+X phi^2)'=Psi'=phi^2.
If A is odd, the derivative of the X^(3A) factor in H_0 is a unit at phi, while every derivative contribution from the other factors has order at least2.
Thus ord_phi H_0'=0.
But a polynomial divisible by phi^A has derivative of order at least A-1.
Since odd A>=2 means A>=3, differentiating(QR14) is then impossible.
Therefore A is even, and N=7A is even as well.

With A and N even, the derivatives of X^(3A) and Psi^(3N) vanish identically.
If B is odd, the remaining derivative has exact phi-order2.
For even A, the derivative of phi^A Q is phi^A Q', of order at least A.
Differentiating(QR14) therefore forces2>=A.
Since A>=2, this branch requires A=2.
If B is even this argument gives no further restriction.
The necessary parity condition is precisely

    A even and (A=2 or B even).                  (QR15)

This completes(QR3).
It does not assert that every multiplicity triple satisfying(QR3) is realized.

<a id="finite-congruence-family"></a>
### Nonzero formal lifts at the allowed ratio

The necessary ratio and parity conditions do not force the canonical reduction to vanish.
For every even A>=2 take B=0 and N=7A, so Tbar=X^A phi^(7A).
Put

    Sbar=X^(A/2) phi^A Psi^(7A/2),
    Ubar=rem_(Tbar)(Sbar).

Choose an integer lift U and an integer W, both of degree below15A, and set

    T=X^A Phi^(7A)+2U+4W.                        (QR16)

These are monic integer polynomials of degree15A.
No irreducibility, total reality or exact residual identity is asserted for them.

The polynomial T_0=X^A Phi^(7A) is an integer square, so Delta_2(T_0) mod2=0 globally.
In the full quotient F_2[X]/(Tbar), the actual quotient reductions therefore satisfy

    theta_2bar=Ubar^2,
    theta_5bar=Sbar^2,
    theta_2bar=theta_5bar.

The C3 residue preserves phi and is divisible by X.
Thus Tbar divides Tbar(C3bar), giving theta_3bar=0 in the same FULL quotient.
The fifth power of theta_5bar is divisible by X^(5A)phi^(10A) and hence by Tbar.
Consequently both complete finite residual equations hold:

    theta_2bar^5=0,
    theta_3bar^2+theta_2bar^3+theta_5bar^3=0.      (QR17)

Both signs s give the same equations modulo2.
These statements use the actual quotient polynomials of the monic T in(QR16), including the required mod4 data for theta_2.
They are not assignments to unrelated elements of a finite ring.

Nevertheless the canonical gbar has exact phi-order6A<7A, because theta_5bar has exact order2A.
Thus gbar is nonzero for every member of this finite-ring-compatible family.
The free4W term changes neither this conclusion nor(QR17).
The construction establishes finite congruence compatibility only; it does not supply an exact solution of(QR1).

<a id="explicit-degree30-model"></a>
For a completely explicit smallest parameter choice, take A=2, B=0, N=14 and write

    T=X^2 Phi^14+2(X Phi^2+X^2 Phi^4)+4W,
    deg W<30.                                   (QR18)

In characteristic2 put D=X phi^7 and chi=X phi^2.
The identity(1+Y+Y^2)^7 congruent1+Y modulo Y^3 shows

    rem_D(D(chi))=chi+chi^2.

Indeed D(chi)=chi Psi^7 differs from chi+chi^2 by a multiple of chi^4, which is divisible by D, and the proposed remainder has degree10<15.
Squaring this identity proves theta_5bar=(chi+chi^2)^2 in the quotient by Tbar=D^2.
The choice of U in(QR18) gives the same value for theta_2bar.
Finally

    rem_D((chi+chi^2)^3)
       =rem_D(chi^3)=X(X+1)phi^6.

Here all terms of degree at least4 in chi are divisible by D, and chi^3-X(X+1)phi^6=X phi^7 in characteristic2.
Squaring gives the actual canonical reduction for(QR18):

    gbar=X^2(X+1)^2 phi^12,
    deg gbar=28, deg T=30.                       (QR19)

It is nonzero and monic as a polynomial over F_2.
This finite-ring example does not determine whether a corresponding characteristic-zero canonical G_can has degree28 or a larger degree with an even leading coefficient.
In general a nonzero reduction does not imply that the integer leading coefficient is odd.
No leading-even conclusion is established by the present argument, and no actual leading-odd residual solution is claimed.

### Exact progress and remaining boundary

The full support hypothesis(QR2), the actual divided quotient definitions and both exact residual equations force the narrower multiplicity relation(QR3) and an actual conjugate with(QR4).
The root proof uses one coefficient of the original monic T and all its root multiplicities, with the parameter B retained throughout.
The derivative argument adds a genuine parity restriction.
The formal family(QR16) shows why these restrictions cannot be promoted to complete coefficient evenness or to nonexistence merely from the displayed modulo2 equations.
Its explicit example(QR18)--(QR19) has canonical reduction degree28, with the exact degree and lifting limits stated above.

No claim that the exact residual system survives at N=7A is made.
Further characteristic-zero quotient identities, the other primary components when B>0, and the full canonical degree and coefficient expenses remain to be controlled.
This is a necessary condition for one specified complete residue-support family, not a classification of all residue graphs or a uniform original Mahler bound.

<a id="inputs-and-boundaries"></a>
## Exact inputs, contributions and remaining scope

| Input | Exact use |
| --- | --- |
| [C153v2 original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original P/K/F/T degrees, actual nonzero integral quotient values and the canonical integer representative. |
| [C196v3 generic half-difference interface](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Only Delta_2(F), monic remainder compatibility, its mod4 expansion and product/power identities preceding the specialized B0 calculation; no degree28, Hensel or global canonical-degree conclusion is used. |
| Elementary local root products and polynomial identities | The complete Y^A coefficient bound, every matching and nonmatching root, all derivative orders, finite-ring lifts and the explicit degree30 example are proved in this argument. |

For every monic integer T in the formal family, the same quotients are integral: C_p is congruent to X^p modulo p, so monic division of T(C_p) by T has every remainder coefficient divisible by p.
No irreducibility is needed for that fact or for the finite-ring examples.
The exact residual equation f=0 in the original field, in contrast, is used through its full polynomial divisibility by the actual minimal T at(QR13).
The support in(QR2) is the entire reduction, not a selected subcollection of roots.
Both signs, arbitrary B in its stated range, every higher lift4W and canonical degree drop retain their stated scope.
The generic upstream identity has an author relationship to entropy_attainment_bridge; an independent review of this new consumer must disclose and correctly handle that upstream relationship, rather than silently describe the entire reused input as noncontributor work.
No external source proof, new numerical computation, all-support classification, actual residual existence or unrestricted Mahler-transfer conclusion is asserted.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:34 |
| status | open |
| reason | Register the complete parameterized necessary ratio and parity theorem for the prescribed whole dyadic support, its actual quotient valuations, and the nonzero finite-congruence family with exact degree-drop limitations. This is separate from the global low-degree canonical obstruction; independent whole review and adoption remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete parameterized theorem and formal boundary](#statement) | Full original actual domain, A/B/N support, N=7A, parity and degree consequences, an actual conjugate of quotient valuation1/3, all even-A finite lifts and exact no-existence/leading-parity boundaries. |
| argument | [Complete QR1--QR19 proof](#argument) | Divided quotient reduction, every root in the coefficient bound, exact local valuations, full characteristic-zero ratio, parity derivatives and complete formal examples. |
| dependency | [Original actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual P/K/F/T and nonzero integral quotient definitions; no arbitrary residual triple replaces them. |
| dependency | [Generic half-difference identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Only the generic Delta_2 definition, mod4 expansion, product/power identities and monic remainder compatibility; specialized degree28 statements and root construction are not premises. |
| support | [Inputs, contributions and exact boundaries](#inputs-and-boundaries) | Root and draft_comparison_cleanup author roles, disclosed upstream identity contribution, finite-ring versus exact residual scope, no program or new source, and unresolved actual leading-degree parity. |
