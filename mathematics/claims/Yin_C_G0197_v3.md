---
author: Yin
---
# Necessary odd support and degree costs for a quadratic residual component

Date: 2026-10-20T14:14.
Human author Yin.
Root and entropy_attainment_bridge developed the complete generalized QX1--QX21 argument on2026-10-20; the author draft's first complete bridge was recorded at22:03 and its odd-part refinement was completed at22:10.
Root supplied the generalized rational-unit factorization, the short A=2 noncancellation, the original degree budget and the common-Frobenius/logarithmic-derivative refinement.
Entropy_attainment_bridge checked and developed the generalized coefficient-root, localized mod4, quantitative error and odd-part arguments, including every original-degree cost.
Both are contributors to this substantive extension.

The older local-module and unit-error method was developed by root and draft_comparison_cleanup in [C197v2](Yin_C_G0197_v2.md#localized-mod4-annihilator).
Its actual whole independent [R476 finding](../audits/reviews/Yin_R_G0476_v1.md#prescribed-support-mod4-whole-finding) has been read, and the version is [adopted](Yin_C_G0197_v2.md#decision-whole-reviewed-2026-10-20).
Only those generic rules are reused, with their complete generalized application written below; the old theorem restricted to the three-factor support is not a premise for extra Q_i.
A reviewer who authored that older bridge must disclose that upstream relationship and reuse its actual independent evidence rather than call it a new independent reproof.
The generic half-difference and actual canonical-graph input in C196v3 has the disclosed root/entropy_attainment_bridge author relationship and the actual [R474 independent coverage](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding).
No independent review or adoption of the present QX proof is claimed.

Physical [v1](Yin_C_G0197_v1.md#argument) and [v2](Yin_C_G0197_v2.md#argument), their findings and their exact mathematical scopes remain unchanged.
In particular the formal modulo2 models, the old necessary-stage argument and the complete leading-unit/degree30 mechanisms remain at their fixed homes.
The old actual three-factor support is excluded by v2; its earlier conditional necessary stage is not described as a nonempty original class after that exclusion.
No new program, parameter scan, numerical root isolation or source acquisition is used.

<a id="quadratic-primary-extra-support-obstruction"></a>
<a id="statement"></a>
## Complete generalized statement


Put Phi=X^2+X+1 in Z[X] and phi=Phi mod2.
Let T be a monic integer polynomial with ENTIRE reduction

    Tbar=X^A phi^N product_i Q_i^(B_i),
    A>=2, N>6A, B_i>=2,                         (QX1)

where the Q_i are distinct monic irreducibles over F_2, different from X and phi.
The product may be empty and may include X+1.
Choose the coefficient0/1 integer lift of each Q_i, denoted by the same letter; in particular Q_i(0)=1.
Set C2=X^2-2, C3=X^3-3X, C5=X^5-5X^3+5X and theta_p=rem_T T(C_p)/p in Z[X].
Their integrality follows by reducing modulo p and dividing by the monic T, exactly as in the fixed generic interface.
Suppose, for a fixed s in{1,-1}, that both actual quotient equations vanish modulo(4,T):

    2theta_5^2-3theta_2^5 in(4,T),
    theta_3^2-theta_2^3+s(theta_5^3-2theta_3^5)
                                                   in(4,T). (QX2)

No irreducibility, total reality or characteristic-zero solution is needed for the local statement.
Then

    N=7A, A is even,
    A=2 implies that some nonlinear Q_i
                       has odd B_i>=3.          (QX3)

For a standalone description of the additional necessary condition, define the following units in F_2(X) localized at phi:

    chi=X phi^2, Psi=phi(chi),
    F_A=X^(-15)Psi^(-147),
    F_Q=Q(X)^6/Q(chi)^21,
    F=F_A^A product_i F_(Q_i)^(B_i).

Then ord_phi(F-1)>=4A, equivalently F=1 modulo phi^(4A), with infinite order allowed at this stage.
All Q_i and every higher coefficient lift of T are retained in this necessary condition.
More precisely, let k be the minimum of the integer2-adic orders of A and all B_i, taking k=v_2(A) when the product is empty, and put A_0=A/2^k,B_i0=B_i/2^k.
Then A_0 is even, some B_i0 is odd, and the squarefree polynomial W_odd=product_(B_i0 odd)Q_i satisfies deg W_odd>=2A_0+1, as proved in(QX17)--(QX20).
All these assertions are necessary conditions, not sufficiency or existence claims.

For the original corollary, use monic irreducible reciprocal nontorsion P in Z[z] of degree d=2r and constant1, a root alpha, delta=alpha+alpha^(-1), the actual totally real F=Q(delta), and its monic minimal trace polynomial T with P(z)=z^r T(z+z^(-1)).
Use the actual nonzero integral quotient values of the [C153v2 trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain), assume the full exact residual equations, nonzero g=c^3-2b^5 and the actual canonical R=G_can mod2.
If its quadratic component phi is unsaturated, meaning ord_phi R<N_phi in Tbar, then

    deg R>=41;
    if the target multiplicity A at X is>=4,
                       then deg R>=52.          (QX4)

The degree is that of the nonzero reduced polynomial, allowing integer degree drop.
This is conditional on an unsaturated quadratic component, not a global bound for every other residue graph or a claim that degree41 occurs.

<a id="argument"></a>
## Complete proof

<a id="quadratic-primary-generalized-root"></a>
### Actual quotient classes and the same small root with extra factors

Write H=X^A product_i Q_i^(B_i), T_0=H Phi^N and T=T_0+2U+4W, with deg U,deg W<deg T.
The [generic half-difference identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification), independently checked at that exact scope by [R474](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding), give

    theta_2=rem_T Delta_2(T),
    Delta_2(T)bar=Delta_2(T_0)bar+Ubar^2,
    Delta_2(JK)bar=Jbar^2 Delta_2(K)bar
                              +Kbar^2 Delta_2(J)bar.

Here Delta_2(J)=(J(C2)-J^2)/2 is an integer polynomial.
The product/power rule gives ord_phi Delta_2(T_0)bar>=2N-2>=N, independently of the other factors of H.
Thus theta_2bar=Ubar^2 modulo phi^N.
Define

    chi=X phi^2,
    Psi=phi(chi)=1+X phi^2+X^2 phi^4,
    J=product_i Q_i(chi)^(B_i).

C3bar=X^3+X sends either root beta of phi to beta^2, with nonzero derivative there.
Every other factor of Tbar is a unit at beta^2, since none is phi.
Consequently the complete phi^N factor survives composition, and the odd quotients give

    theta_3bar=0 modulo phi^N,
    theta_5bar=X^A phi^(2A) J Psi^N
                                      modulo phi^N. (QX5)

Each Q_i(chi) has residue Q_i(0)=1, so J and Psi are units at phi.
The second congruence(QX2) reduced modulo phi^N has theta_2bar^3=theta_5bar^3, of exact order6A<N.
The first has theta_2bar^5=0.
It follows that

    ord_phi Ubar=A,
    ord_phi theta_2bar=ord_phi theta_5bar=2A,
    N<=10A.                                     (QX6)

Choose integer V,Z with U=Phi^A V+2Z and Vbar not divisible by phi, and absorb Z into W.
The SAME T has the exact form

    T=H Phi^N+2Phi^A V+4W_1.                    (QX7)

Work in a finite splitting field of T Phi over Q_2 with v(2)=1, and let beta_0 be a root of Phi.
The factors of H and V are units at beta_0.
Since Phi(beta_0+Y)=Y(2beta_0+1+Y), the coefficient of Y^A in T(beta_0+Y) has valuation exactly1: the first term starts at Y^N, the second contributes2(2beta_0+1)^A V(beta_0), and the final term contributes valuation at least2.
All roots of monic T are integral, and its full reduction shows that exactly N roots, counted with multiplicity, have residue beta=beta_0 mod2.
Every other root difference from beta_0 is a unit.
If each matching difference had valuation at least1/A, every product in the Y^A coefficient would contain at least N-A matching factors and have valuation at least(N-A)/A>1.
This contradicts the exact coefficient value, even allowing roots equal to beta_0 with infinite difference valuation.
Hence an actual root x of T satisfies0<t=v(x-beta_0)<1/A and v(Phi(x))=t.
At this root, the three terms of(QX7) have values Nt,1+At,>=2.
The second is below2, so the minimum must be shared and

    t=1/(N-A), Nt=1+At,
    u=2At=2A/(N-A)<2/5.                         (QX8)

The quotient congruence theta_2-U^2 modulo(2,Phi^N) leaves error of valuation at least1 at x, while U(x) has value At.
For theta_5, use the integral lift chi_0=X Phi^2: theta_5-T_0(chi_0) belongs to(2,T), and T_0(chi_0(x)) has value2At because all Q_i(chi_0(x)) and Phi(chi_0(x)) are units.
Similarly theta_3 belongs to(2,Phi^N), so its value at x is at least1.
Thus, writing a=theta_2(x),b=theta_3(x),c=theta_5(x), one has v(a)=v(c)=u and v(b)>=1.
The first congruence(QX2) has value at least2 at the integral root x.
Both summands have value below2, namely1+2u and5u, so those values must coincide.
Consequently

    N=7A, v(Phi(x))=1/(6A),
    v(a)=v(c)=1/3, v(b)>=1.                     (QX9)

This uses the congruence modulo4 alone, not an exact residual assumption or an unproved Newton slope.

There is also a preliminary parity restriction.
In characteristic2, cancel phi^(6A) from the second residual congruence modulo phi^(7A), obtaining

    Vbar^6 congruent X^(3A) J^3 Psi^(21A)
                                           modulo phi^A.

Every derivative contribution from J and Psi has phi-order at least2, because chi'=Psi'=phi^2.
If A were odd, the derivative of X^(3A) would give a unit at phi, so the derivative of the right side would have order0.
The derivative of Vbar^6 is zero, whereas a multiple of phi^A has derivative order at least A-1>=2 for odd A>=3.
This contradiction proves A even.

<a id="quadratic-primary-local-mod4-bridge"></a>
### The complete localized mod4 comparison

Let R_4=(Z/4Z)[X]/(T mod4), and localize at all integer polynomials whose reductions are not divisible by phi; call the resulting ring Q_4.
Monicity makes R_4 free over Z/4Z, so ann_(R_4)(2)=2R_4 and the reduction kernel is2R_4.
Both assertions survive localization by clearing a denominator: if2r/s=0, an allowed multiplier h gives2hr=0, hence hr=2k and r/s=2k/(hs).
The same denominator argument treats a fraction of zero reduction.
Therefore

    ann_(Q_4)(2)=2Q_4,
    Q_4/2Q_4=F_2[X]_(phi)/(phi^(7A)).            (QX10)

All other primary factors are inverted here, without dropping them from the formulas for H or the quotients.
Put U_1=Phi^A V, so T=H Phi^(7A)+2U_1+4W_1.
The theta_2 congruence gives theta_2=U_1^2+2Z_1 in Q_4.
As U_1bar^8 has order8A>=7A, it is zero after reduction, so2U_1^8 Z_1=0 in Q_4.
Expanding the fifth power yields theta_2^5=U_1^10, and the defining relation of T gives

    U_1^10=-2Phi^(4A)V^11/H in Q_4.

Use the first congruence(QX2), cancel2 by(QX10), multiply by the unit H and cancel phi^(4A) in the resulting characteristic-two congruence modulo phi^(7A).
Writing J_0=product_i Q_i(chi_0)^(B_i) and Psi_0=Phi(chi_0)=1+X Phi^2+X^2 Phi^4, this gives

    Vbar^11 congruent Dbar modulo phi^(3A),
    D=H X^(2A) J_0^2 Psi_0^(14A).               (QX11)

The factor3 from the residual equation reduces to1; no arbitrary zero divisor was cancelled in Q_4.
The ordinary polynomial congruence follows because a denominator prime to phi can be inverted modulo phi^(3A).

At the same root x from(QX9), an integer lift of(QX11) has error2E+Phi^(3A)K and hence valuation at least1/2.
All displayed comparison terms are units.
The sixth powers have error at least1: for an error e of value at least1/2, the first binomial term6D^5e has value at least3/2, the second15D^4e^2 has value at least1, and every remaining term has value at least1.
Thus v(V(x)^66-D(x)^6)>=1.

Suppress evaluation at x, and write q=Phi(x).
The actual quotient estimates are

    a=q^(2A)V^2+error v>=1,
    c=q^(2A)x^A J_0 Psi_0^(7A)+error v>=1.

Dividing by q^(2A), of value1/3, makes both errors at least2/3.
Inversion of units and cubing preserve that lower error bound, so for

    R_0=V^6/[x^(3A)J_0^3 Psi_0^(21A)]

one has v((a/c)^3-R_0)>=2/3.
The second congruence(QX2) and v(b)>=1 give v(a^3-s c^3)>=2.
After division by c^3, of value1, this gives v((a/c)^3-s)>=1 and hence v(R_0-s)>=2/3.
An eleventh power preserves the latter bound, and s^11=s.
Replacing V^66 by D^6 changes the resulting unit by valuation at least1.
It follows that the explicit integer rational unit

    F_0(x)=x^(-15A) Psi_0(x)^(-147A)
              product_i [Q_i(x)^6/
                          Q_i(chi_0(x))^21]^(B_i)

satisfies

    v(F_0(x)-s)>=2/3.                           (QX12)

Every denominator is a unit at this actual root.
In particular the factors Q_i(x), which may carry nontrivial residue in F_4, have been retained; omitting them would change the conclusion.

### A necessary characteristic-two rational-function order

In F_2(X), localized at phi, put

    F_A=X^(-15)Psi^(-147),
    F_Q=Q(X)^6/Q(chi)^21,
    F=F_A^A product_i F_(Q_i)^(B_i).             (QX13)

Every factor is a unit with residue1: Q_i(beta) belongs to F_4^*, whose sixth power is1, and Q_i(chi(beta))=Q_i(0)=1.
The same holds for F_A because beta^3=1 and Psi(beta)=1.
Let ell=ord_phi(F-1), with ell=infinity if F=1 as a rational function.
Using a common integer polynomial denominator of F_0-s, its reduction has this exact order since s=1 modulo2 and the denominator is a unit at phi.
If ell<4A, lift the numerator as Phi^ell K+2L, where Kbar(beta) is nonzero.
At x the two summands have values ell/(6A)<2/3 and at least1, so the rational unit difference has exact value ell/(6A), contradicting(QX12).
Consequently the full necessary condition is

    F congruent1 modulo phi^(4A),
    equivalently ord_phi(F-1)>=4A.              (QX14)

The infinite-order case is included.
This implication does not assert equality of valuations once ell>=6A, where the integer2-error could compete.

For any allowed irreducible Q, Q(X)^3-1 is divisible by phi because its value at beta is zero.
Squaring gives Q(X)^6=1 modulo phi^2.
Also Q(chi)=1 modulo phi^2 because Q(0)=1 and chi=Xphi^2.
Hence

    F_Q=1 modulo phi^2.                          (QX15)

For the only other linear factor Q=X+1 the leading order is explicit.
The exact identities X^3=1+(X+1)phi and (X+1)^3=1+Xphi give

    F_A-1 congruent (X+1)phi modulo phi^2,
    F_(X+1)-1 congruent phi^2 modulo phi^3.       (QX16)

For the second line, (X+1)^6=1+X^2phi^2 and (1+Xphi^2)^(-21)=1+Xphi^2 modulo phi^4; their phi^2 coefficient reduces to X^2+X=1 modulo phi.
For the first, Psi=1 modulo phi^2 and X^(-15)=(X^3)^(-5).

Suppose A=2 and every nonlinear Q_i has even B_i.
By(QX15) and Frobenius, all those powered factors are1 modulo phi^4.
The phi^2 coefficient of F_A^2-1 at beta is(beta+1)^2=beta.
If X+1 occurs, its powered factor contributes coefficient0 for even multiplicity and1 for odd multiplicity; if absent it contributes0.
The total coefficient is thus beta or beta+1, both nonzero.
Therefore ord_phi(F-1)=2, contradicting(QX14), which requires at least8.
This proves the final assertion of(QX3), with odd B_i>=3 because every B_i>=2.
No assertion that the extra odd factor is sufficient is made.

<a id="quadratic-primary-odd-part-derivative"></a>
### Common Frobenius powers and the squarefree odd part

The preceding short A=2 argument is retained as a weaker direct test.
The following unified necessary condition quantifies the full set of extra factors.
Let

    k=min{v_2(A),v_2(B_i) for all i},
    A_0=A/2^k, B_i0=B_i/2^k,
    F_red=F_A^(A_0) product_i F_(Q_i)^(B_i0).    (QX17)

For an empty product the minimum is v_2(A).
These v_2 values refer only to positive integers, not the normalized field valuation at x.
In characteristic2, F=F_red^(2^k), and therefore
ord_phi(F-1)=2^k ord_phi(F_red-1), with the same convention for infinity.
Condition(QX14) consequently requires

    ord_phi(F_red-1)>=4A_0.                     (QX18)

If A_0 were odd, the F_A factor in(QX16) would contribute an exact order1 term to F_red-1, while every F_Q factor has order at least2 by(QX15).
This contradicts(QX18).
Thus A_0 is even.
The definition of k now forces at least one B_i0 to be odd, since the minimum of their2-adic orders together with that of A_0 is zero.
In particular an empty product is impossible under(QX2).
Set

    W_odd=product_(B_i0 odd) Q_i.

This is nonconstant and squarefree, and W_odd(0)=1.
Its derivative W_odd' is nonzero: a polynomial over F_2 with zero derivative is a square, whereas a nonconstant product of distinct irreducibles cannot be a square.

Compute the characteristic-two logarithmic derivative in the rational function field.
The F_A term contributes zero because A_0 is even, and each Q_i(X)^6 numerator also has zero derivative.
The exponent21 in the denominator is odd, so only the odd B_i0 factors survive, with minus and plus equal in characteristic2.
Since chi'=phi^2, the exact identity is

    F_red'/F_red
       =phi^2 W_odd'(chi)/W_odd(chi).             (QX19)

The denominator is a unit at phi because W_odd(0)=1.
Writing j=ord_X W_odd', the substitution chi=Xphi^2 has exact phi-order2 and gives ord_phi W_odd'(chi)=2j.
Thus the right side of(QX19) has exact finite order2+2j.

On the other hand, F_red-1 is a multiple of phi^(4A_0) in the local rational-function ring by(QX18).
The exponent4A_0 is even, so its derivative is still divisible by phi^(4A_0): the derivative of that power of phi vanishes and differentiation preserves the local ring.
Division by the unit F_red leaves the same lower order bound.
Consequently2+2j>=4A_0, or j>=2A_0-1.
Every nonzero monomial of the derivative of an F_2 polynomial has even exponent.
Therefore its least exponent j is even, and this sharpens to

    ord_X W_odd'>=2A_0,
    deg W_odd>=2A_0+1.                          (QX20)

The second inequality uses W_odd'!=0 and deg W_odd'<=deg W_odd-1.
This proof also handles the possible infinite order in(QX18): a zero logarithmic derivative would contradict the nonzero right side of(QX19).
No assumption that the odd-part product has generic coefficients or a simple real root is used.

For A=2, evenness of A_0 forces k=0 and A_0=2.
Thus W_odd is the product of factors with ORIGINAL odd B_i, each at least3, and has degree at least5.
This both implies the previous nonlinear-odd-factor requirement and provides its stronger total degree cost.
For support with no extra factors or only X+1, the degree of W_odd would be at most1, so the necessary conditions are already impossible; the earlier narrower-support theorem is consistent with this generalized test.

<a id="quadratic-primary-degree35-consequence"></a>
<a id="quadratic-primary-degree41-consequence"></a>
### Full original-support degree cost

Return to the actual original residual system and its canonical R=G_can mod2.
The [accepted complete C196 graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) retains every local factor and gives

    R=rem_(Tbar)(Tbar(chi)^3),
    every factor multiplicity of Tbar is>=2,
    ord_Q R>=min{3,N_Q}
                          for each Q dividing Tbar.

The stronger exact unsaturated formula in that input is also used here.
The unique irreducible quadratic over F_2 is phi, and chi=Xphi^2 maps its roots to0 with local multiplicity2.
Therefore an unsaturated phi component is exactly the condition N>6A, where A is the multiplicity at X, and then ord_phi R=6A.
This puts the entire support in(QX1), with all remaining distinct factors Q_i and their actual multiplicities B_i retained.
The original exact equations imply(QX2) by minimal-polynomial divisibility, so(QX3) applies.

Since chi is divisible by X, both Tbar(chi)^3 and Tbar are divisible by X^A.
The canonical remainder R is consequently divisible by X^A, not merely by the weaker X^min(3,A).
The two separate components alone therefore cost

    deg R>=2(6A)+A=13A.                         (QX21)

If A>=4, its evenness gives the claimed bound52.
If A=2, an additional nonlinear Q_i has odd B_i>=3.
It is distinct from the only irreducible quadratic phi and from the linear factors, so deg Q_i>=3.
Its original canonical multiplicity is at least min(3,B_i)=3, contributing at least9 beyond the separate26 from X and phi.
This already gives the earlier weaker deg R>=35.
The full odd-part refinement now gives deg W_odd>=5 when A=2, with every factor having original odd B_i>=3.
Each such factor contributes at least three times its degree to R, by the same original multiplicity bound, and none is X or phi.
The extra cost is therefore at least3deg W_odd>=15 beyond the26 already charged.
This proves deg R>=41, while the A>=4 bound52 remains valid.
All these costs concern factors of the same actual reduced canonical polynomial; no graph vertex count or independent auxiliary degree replaces its degree.
The argument does not constrain the reduced leading degree to equal the integer leading degree and does not assert a full all-support bound41.

<a id="exact-inputs"></a>
## Exact inputs and limits

| Input | Scope used |
| --- | --- |
| [C153v2 original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Original corollary only: actual minimal T, full original quotients and exact field identities implying polynomial divisibility. |
| [C196v3 generic half-difference interface](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Integer Delta_2, product/power rules, expansion before reduction and monic remainder compatibility only. |
| [C196v3 complete C196 graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Original all-cluster multiplicities, canonical remainder, exact unsaturated quadratic arrow and positive support at every additional factor. |
| [R474 whole input finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Actual coverage of those adopted interfaces, with initial review context currently unknown; the present authors' upstream roles are not described as independent re-review. |
| [C197v2 generic local module and unit-error rules](Yin_C_G0197_v2.md#localized-mod4-annihilator) | The monic free Z/4Z module, localization of ann(2) and the following sixth-power error rule; the generalized Q_i application is derived completely here, not inferred from the old support theorem. |
| [R476 whole predecessor finding](../audits/reviews/Yin_R_G0476_v1.md#prescribed-support-mod4-whole-finding) | Actual complete coverage of the older localized/error interface and its authorship, with initial review context currently unknown, not an advance review of the present generalization. |
| [Physical C197v1 and finite models](Yin_C_G0197_v1.md#finite-congruence-family) | All old QR1--QR19 remain fixed; equations modulo2 and the mod4 dependence of theta2 are not equations modulo4. |
| [Adopted C197v2 exclusion and appendix](Yin_C_G0197_v2.md#decision-whole-reviewed-2026-10-20) | Whole narrower-support exclusion and complete LU/ME mechanisms remain at their fixed adopted scope; they are not recopied or weakened here. |
| Elementary local algebra proved here | Every matching root, localized2-annihilator, actual quotient error, generalized rational unit, noncancellation, Frobenius extraction, odd-part derivative and complete degree cost. |

The complete mod4 bridge here is proved for the stated arbitrary monic T and is not imported from a candidate's original-field-only statement.
The final degree bound uses the additional accepted original-residual graph interface; arbitrary monic congruence models are not assigned that original positive-support input.
The argument leaves open other unsaturated orbit types, the A=2 cases whose full odd part satisfies the necessary derivative constraint, the A>=4 cases and the full all-degree logarithmic-transfer problem.
It supplies necessary constraints for those remaining cases, not their existence.
No finite computation or exact original residual realization has been supplied.


## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:14 |
| status | open |
| reason | Register the complete arbitrary-monic generalized phi-primary mod4 necessary conditions, common-Frobenius odd-part derivative theorem, and actual unsaturated-quadratic canonical degree41/52 costs. Preserve the physical earlier versions and their exact finite-model/exclusion scopes. New whole independent consumer review is required, with upstream author relationships disclosed and R474/R476 reused only at their precise scopes. No all-support degree theorem or adoption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete generalized conditions and original consequence](#statement) | Entire support with arbitrary distinct extra Q_i and their full multiplicities, both signs, all monic lifts, N=7A and parity, full rational-unit order, common Frobenius odd-part derivative/degree constraint, and actual phi-unsaturated degree41/52 including reduction degree drop. |
| argument | [Complete QX1--QX21 argument](#argument) | All root counts and valuations, exact monic quotient and localized2-annihilator, complete unit-error chain, rational orders, initial short test, Frobenius derivative refinement and full original degree accounting. |
| dependency | [Generic half-difference identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Integral Delta_2, product/power identities, expansion before reduction and monic remainder compatibility; no specialized Hensel construction is used. |
| dependency | [Actual canonical C196 graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Only the original corollary: all factor multiplicities, exact canonical remainder, unsaturated quadratic arrow, and support expense at every extra factor. |
| dependency | [Actual original trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Only original P/F/T domain, nonzero integral quotient values and exact field equations implying divisibility by the actual minimal T. |
| dependency | [Generic localized module and unit-error rules](Yin_C_G0197_v2.md#localized-mod4-annihilator) | Free monic Z/4Z module, localization of ann(2), and following sixth-power error amplification; their new generalized application is fully checked here, not the old whole-support conclusion applied beyond its scope. |
| support | [Actual independent C196v3 finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Exact independent generic algebraic and canonical-graph coverage, retaining the present authors' upstream contributions. |
| support | [Actual whole predecessor finding](../audits/reviews/Yin_R_G0476_v1.md#prescribed-support-mod4-whole-finding) | Entire prior local/error proof and its declared domains, with no automatic extension to new Q_i, odd-part or degree41 claims. |
| support | [Preserved original finite models](Yin_C_G0197_v1.md#finite-congruence-family) | Complete physical v1 remains unchanged, including QR1--QR19, actual quotient equations modulo2 and integer-leading-degree limitations. |
| support | [Adopted narrower-support result](Yin_C_G0197_v2.md#decision-whole-reviewed-2026-10-20) | Full earlier mod4 impossibility and its original corollary remain proved at the narrower complete-support scope. |
| support | [Preserved leading-unit and correction mechanisms](Yin_C_G0197_v2.md#retained-intermediate-mechanisms) | Full LU1--LU3 and ME1--ME11, failed/improved seeds and unique correction class remain fixed rather than duplicated or discarded. |
| support | [Exact inputs and boundaries](#exact-inputs) | Full generic-versus-original distinction, root/entropy new contributions, comparison's older local-method role, existing independent evidence, no program, no existence claim and no global all-support bound41. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:22 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the entire generalized QX1--QX21 through actual whole consumer R477. The arbitrary-monic necessary constraints retain all extra factors, both signs and every lift; the common Frobenius and nonzero odd-part derivative give the complete degree cost. The actual unsaturated quadratic branch has reduction degree at least41, or52 when A>=4. Preserve all upstream author relationships and independently checked scopes, prior physical models, and the distinction from an all-orbit degree bound or an existence assertion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete generalized conditions and original consequence](#statement) | Entire support with arbitrary distinct extra Q_i and their full multiplicities, both signs, all monic lifts, N=7A and parity, full rational-unit order, common Frobenius odd-part derivative/degree constraint, and actual phi-unsaturated degree41/52 including reduction degree drop. |
| argument | [Complete QX1--QX21 argument](#argument) | All root counts and valuations, exact monic quotient and localized2-annihilator, complete unit-error chain, rational orders, initial short test, Frobenius derivative refinement and full original degree accounting. |
| dependency | [Generic half-difference identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Integral Delta_2, product/power identities, expansion before reduction and monic remainder compatibility; no specialized Hensel construction is used. |
| dependency | [Actual canonical C196 graph](Yin_C_G0196_v3.md#canonical-c5-residue-graph) | Only the original corollary: all factor multiplicities, exact canonical remainder, unsaturated quadratic arrow, and support expense at every extra factor. |
| dependency | [Actual original trace domain](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Only original P/F/T domain, nonzero integral quotient values and exact field equations implying divisibility by the actual minimal T. |
| dependency | [Generic localized module and unit-error rules](Yin_C_G0197_v2.md#localized-mod4-annihilator) | Free monic Z/4Z module, localization of ann(2), and following sixth-power error amplification; their new generalized application is fully checked here, not the old whole-support conclusion applied beyond its scope. |
| support | [Actual C196v3 finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Exact independent generic algebraic and canonical-graph coverage, retaining the present authors' upstream contributions. |
| support | [Actual whole predecessor finding](../audits/reviews/Yin_R_G0476_v1.md#prescribed-support-mod4-whole-finding) | Entire prior local/error proof and its declared domains, with no automatic extension to new Q_i, odd-part or degree41 claims. |
| support | [Preserved original finite models](Yin_C_G0197_v1.md#finite-congruence-family) | Complete physical v1 remains unchanged, including QR1--QR19, actual quotient equations modulo2 and integer-leading-degree limitations. |
| support | [Adopted narrower-support result](Yin_C_G0197_v2.md#decision-whole-reviewed-2026-10-20) | Full earlier mod4 impossibility and its original corollary remain proved at the narrower complete-support scope. |
| support | [Preserved leading-unit and correction mechanisms](Yin_C_G0197_v2.md#retained-intermediate-mechanisms) | Full LU1--LU3 and ME1--ME11, failed/improved seeds and unique correction class remain fixed rather than duplicated or discarded. |
| support | [Exact inputs and boundaries](#exact-inputs) | Full generic-versus-original distinction, root/entropy new contributions, comparison's older local-method role, existing independent evidence, no program, no existence claim and no global all-support bound41. |
| review | [Whole generalized consumer finding](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Entire actual QX1--QX21, nine input rows and all selected dependencies/supports; complete arbitrary-monic conditions and actual original degree41/52 with degree drop, author-overlapping upstream evidence reused only at its independent R474/R476 scope. |

