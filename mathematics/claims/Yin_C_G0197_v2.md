---
author: Yin
---
# No simultaneous mod4 residual equations in the prescribed quadratic support family

Date: 2026-10-20T13:57.
Human author Yin.
This substantive v2 preserves the physical [v1](Yin_C_G0197_v1.md#statement), including all QR1--QR19 and its complete finite modulo2 models, without altering its original version or decision.
Root supplied the general local mod4 congruence, the eleventh/sixth-power comparison and the two characteristic-two rational-unit orders.
The draft_comparison_cleanup agent developed and checked the full arbitrary-monic domain, root existence, localized2-annihilator, quantitative quotient errors and noncancellation in the tied-order case.
Both are contributors to the new general proof, developed on2026-10-20T13:50.
The earlier leading-unit and degree30 mechanisms developed on2026-10-20T13:45 are preserved completely in the appendix with their useful unique-correction and seed distinctions.
The generic half-difference identities have the disclosed upstream contribution of root and entropy_attainment_bridge in C196v3; only their exact independently reviewed algebraic interface is reused.
No independent review or adoption of this substantive version is claimed.
No mathematical program, enumeration, floating-point calculation or new source acquisition is used.

<a id="statement"></a>
## Complete strengthened statement

Let T be ANY monic integer polynomial whose entire reduction is

    Tbar=X^A(X+1)^B phi^N,
    phi=X^2+X+1 in F_2[X],
    A>=2, B=0 or B>=2, N>6A.                     (GM1)

The three exponents are integers, and the degree of T is necessarily r=A+B+2N.
No irreducibility, separability, total reality, original unit polynomial or characteristic-zero residual solution is assumed.
Set

    C2=X^2-2, C3=X^3-3X, C5=X^5-5X^3+5X,
    theta_p=rem_T(T(C_p))/p in Z[X], p=2,3,5,
    F_res=2theta_5^2-3theta_2^5,
    E_s=theta_3^2-theta_2^3
                    +s(theta_5^3-2theta_3^5),
    s in{1,-1}.

The quotient polynomials are integral because C_p is congruent to X^p modulo p and monic division of T(C_p) has remainder divisible coefficientwise by p.
Then

    F_res and E_s cannot both belong to(4,T),     (GM2)

or equivalently they cannot both vanish in (Z/4Z)[X]/(T mod4).
Both signs, all exponents in(GM1) and EVERY higher coefficient lift of T are included.
The condition describes the whole support, not a selected subcollection of its roots.

For the original problem, take monic irreducible reciprocal nontorsion P of degree d=2r and constant1, alpha a root, delta=alpha+alpha^(-1), F=Q(delta) totally real, and the actual monic trace polynomial T with P(z)=z^r T(z+z^(-1)).
The actual quotient values a=theta_2(delta), b=theta_3(delta), c=theta_5(delta) of [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) cannot satisfy both exact residual equations with support(GM1).
Indeed exact equations in the original field imply divisibility by its monic minimal T and hence the impossible congruences(GM2).
This applies in particular to the full residual branch g=c^3-2b^5!=0, at every original Mahler measure.

The complete finite modulo2 models of [v1](Yin_C_G0197_v1.md#finite-congruence-family) remain valid: their T modulo4 correctly determines theta_2 modulo2 and both residual equations vanish modulo2.
This does not say that the equations themselves vanish modulo4.
The present theorem proves that none of those models extends to simultaneous congruences modulo4 in the stated support family.
The retained necessary ratio/parity and formal examples in v1 are not presented as nonempty actual residual coverage after this strengthening.
The appendix retains the leading-unit condition and the complete degree30 unique-correction argument, including the exact distinction among the failed and improved seeds.
No unrestricted residual nonexistence, all-support classification or uniform Mahler-transfer conclusion is asserted.

<a id="argument"></a>
## Complete arbitrary-monic proof

### 1. The actual quotient classes before any exact residual assumption

Assume for contradiction that F_res and E_s both belong to(4,T).
Write Phi=X^2+X+1 in Z[X], H=X^A(X+1)^B and

    T_0=H Phi^N,
    T=T_0+2U+4W, deg U,deg W<r.

For any integer polynomial J put Delta_2(J)=(J(C2)-J^2)/2.
The generic [C196v3 half-difference interface](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification), covered at precisely this scope by [R474](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding), gives

    theta_2=rem_T Delta_2(T),
    Delta_2(T)bar=Delta_2(T_0)bar+Ubar^2,
    Delta_2(JK)bar=Jbar^2 Delta_2(K)bar
                            +Kbar^2 Delta_2(J)bar.

These are the generic integer identities, not the specialized degree28 conclusion of that input.
The product rule shows ord_phi Delta_2(T_0)bar>=2N-2>=N: the Phi^N term leaves Phi^(2N-2), and applying the rule to the other factor retains Phi^(2N).
Thus theta_2bar=Ubar^2 modulo phi^N.
For chi=X phi^2, L=1+X phi^2 and Psi=1+X phi^2+X^2 phi^4, the odd quotients give

    theta_3bar=0 modulo phi^N,
    theta_5bar=X^A phi^(2A) L^B Psi^N
                                           modulo phi^N. (GM3)

Indeed C3bar=X^3+X preserves the two phi roots and has nonzero derivative there, while both C3bar and C3bar+1 are units at them.
Division by3 and5 is the identity modulo2 after the integral quotients have been established.
The factors after phi^(2A) in theta_5bar are units at phi.
Since N>6A, its cube has exact phi-order6A below N.
Reducing the two assumed equations modulo phi^N now forces

    ord_phi Ubar=A,
    ord_phi theta_2bar=ord_phi theta_5bar=2A,
    N<=10A.                                      (GM4)

For the first equality use Ubar^6=theta_5bar^3; for the last use theta_2bar^5=0.
Choose integer V,Z with U=Phi^A V+2Z and phi not dividing Vbar, and absorb Z into W.
The SAME monic polynomial then has the exact form

    T=H Phi^N+2Phi^A V+4W_1,
    phi does not divide Vbar.                     (GM5)

No original-field or exact characteristic-zero residual identity has been used.

<a id="small-matching-root"></a>
### 2. A root of the same monic T and the ratio forced already modulo4

Work in a finite splitting field of T Phi over Q_2, with valuation v normalized by v(2)=1.
For a root beta_0 of Phi, both beta_0 and beta_0+1 are units, and Phi(beta_0+Y)=Y(2beta_0+1+Y).
The coefficient of Y^A in T(beta_0+Y) has valuation exactly1: the first term in(GM5) starts at Y^N with N>A, the second contributes2(2beta_0+1)^A V(beta_0), and the last contributes valuation at least2.
All roots of monic T are integral, since a root of negative valuation would make its leading monomial uniquely smallest.
Reduction of the full root factorization shows that exactly N roots, counted with multiplicity, have residue beta, the image of beta_0 in the residue field.
All other root differences from beta_0 are units.
If all matching differences had valuation at least1/A, every product in the Y^A coefficient would contain at least N-A of them and have valuation at least(N-A)/A>1.
This contradicts the exact coefficient valuation.
Hence some actual root x of T satisfies

    0<t=v(x-beta_0)<1/A,
    q=Phi(x), v(q)=t.

The three terms of(GM5) evaluated at x have valuations Nt,1+At,>=2.
Since1+At<2 and the minimum cannot be unique, one obtains

    t=1/(N-A), Nt=1+At,
    u=2At=2A/(N-A)<2/5.                          (GM6)

This proves existence of the required root; no formal slope or lifting assertion substitutes for the coefficient argument.
It includes repeated roots and every higher W_1.

The congruence theta_2-U^2 modulo(2,Phi^N) gives an error of valuation at least1 at x, because Nt>1.
As U=Phi^A V+2Z, one has v(U(x))=At and hence v(theta_2(x))=u.
For chi_0=X Phi^2, the odd quotient identity theta_5 congruent T_0(chi_0) modulo(2,T) gives the same value u: chi_0(x) has valuation2t and chi_0(x)+1 and Phi(chi_0(x)) are units.
Also theta_3bar=0 modulo phi^N implies v(theta_3(x))>=1.
Thus, writing a=theta_2(x), b=theta_3(x), c=theta_5(x),

    v(a)=v(c)=u<2/5,
    v(b)>=1.                                    (GM7)

Since F_res belongs to(4,T), its value at this integral root has valuation at least2.
The two summands2c^2 and3a^5 have values1+2u<2 and5u<2.
If these values differed, their difference would have value below2.
Therefore1+2u=5u, forcing

    N=7A, t=1/(6A), v(a)=v(c)=1/3.              (GM8)

This is a consequence of the congruence modulo4 alone.
It does not invoke the earlier v1 statement proved under exact original-field equations.

<a id="localized-mod4-annihilator"></a>
### 3. Exact cancellation of2 in the localized coefficient ring

Let R_4=(Z/4Z)[X]/(T mod4), and R_2=F_2[X]/(Tbar).
Because T is monic, R_4 is free over Z/4Z with basis1,...,X^(r-1).
Consequently its annihilator of2 is exactly2R_4, and reduction R_4->R_2 has kernel2R_4.
Localize at the multiplicative set of integer polynomials whose reductions are not divisible by phi, and write these localized rings as Q_4,Q_2.
Both statements remain true there by clearing a denominator.
For example if2r/s=0, some allowed t satisfies2tr=0 in R_4, so tr=2k and r/s=2k/(ts).
The same argument applies to a fraction whose reduction is zero.
Thus

    ann_(Q_4)(2)=2Q_4,
    Q_4/2Q_4=Q_2=F_2[X]_(phi)/(phi^(7A)).        (GM9)

Here H=X^A(X+1)^B is a unit, and the other primary factors have been inverted.
This proves the exact coefficient-ring assertion needed below, rather than cancelling an arbitrary zero divisor without justification.

Set U_1=Phi^A V, so T=H Phi^(7A)+2U_1+4W_1.
The earlier phi-primary congruence shows theta_2=U_1^2+2Z in Q_4 for some Z.
Since U_1bar^8 has phi-order8A>=7A, it is zero in Q_2, and hence2U_1^8 Z=0 in Q_4.
Expanding the fifth power therefore gives theta_2^5=U_1^10 in Q_4.
The defining relation for T further yields

    U_1^10=Phi^(10A)V^10
          =-2Phi^(4A)V^11/H in Q_4.

On the other hand(GM3) gives theta_5bar^2=phi^(4A)X^(2A)L^(2B)Psi^(14A).
The assumed vanishing of F_res in Q_4, followed by(GM9), therefore implies

    Vbar^11 congruent Dbar modulo phi^(3A),
    D=X^(3A)(X+1)^B L_0^(2B) Psi_0^(14A),
    L_0=1+X Phi^2,
    Psi_0=1+X Phi^2+X^2 Phi^4.                  (GM10)

Explicitly, after removing2, the congruence modulo phi^(7A) has a factor phi^(4A); its remaining factor is consequently divisible by phi^(3A).
Multiplication by the unit H gives the displayed ordinary polynomial congruence.
No equality outside the localized component is needed for this necessary condition.

### 4. Quantified unit comparison at the actual root

Evaluate(GM10) at the root x from(GM8).
A polynomial lift of that congruence has the form V^11-D=2E+Phi^(3A)J, giving

    v(V(x)^11-D(x))>=1/2.

Both terms are units.
Their sixth powers differ by an element of valuation at least1.
Indeed in the binomial expansion the first coefficient6 has valuation1, the second coefficient15 is a unit and its error square has valuation at least1, and each remaining term also has valuation at least1.
Thus

    v(V(x)^66-D(x)^6)>=1.                        (GM11)

Use the same x,q throughout, and suppress evaluation at x in unit expressions below.
The actual quotient approximations, now with N=7A, are

    a=q^(2A)V^2+error v>=1,
    c=q^(2A)x^A L_0^B Psi_0^(7A)+error v>=1.

After division by q^(2A), both errors have valuation at least2/3.
All displayed scaled factors are units, so division and cubing preserve that error bound.
Put

    R_0=V^6/[x^(3A)L_0^(3B)Psi_0^(21A)].

Then

    v((a/c)^3-R_0)>=2/3.                         (GM12)

The second residual congruence and v(b)>=1 give v(a^3-s c^3)>=2: its other terms b^2 and2s b^5 have valuation at least2.
Since v(c^3)=1, it follows that v((a/c)^3-s)>=1, and therefore v(R_0-s)>=2/3.
Raising to the odd eleventh power and using s^11=s gives v(R_0^11-s)>=2/3.
By(GM11), R_0^11 differs by valuation at least1 from the explicit unit

    F_0=x^(-15A)(x+1)^(6B)
                      L_0^(-21B)Psi_0^(-147A).

Consequently

    v(F_0-s)>=2/3.                               (GM13)

Every denominator here is a unit at x.
The passage from the phi congruence of depth3A to the numerical bounds1/2,1 and2/3 is explicit and independent of A,B.

<a id="two-rational-unit-orders"></a>
### 5. Exact characteristic-two orders and the contradiction

In the rational function field F_2(X), localized at phi, define

    F_A=X^(-15)Psi^(-147),
    F_B=(X+1)^6 L^(-21).

The reduction of F_0 is F_A^A F_B^B.
Both basic functions have residue1.
Since X^3=1+(X+1)phi and Psi=1 modulo phi^2, one has

    F_A-1 congruent (X+1)phi modulo phi^2.

Its order is exactly1 and its leading coefficient at a root beta of phi is beta+1=beta^2.
Also(X+1)^3=1+X phi, so(X+1)^6=1+X^2 phi^2.
Combining this with L^(-21)=1+X phi^2 modulo phi^4 gives

    F_B-1 congruent phi^2 modulo phi^3.           (GM14)

Its order is exactly2 and its leading coefficient is1.
These are identities in the local rational-function ring; all the denominators are units there.

For A>0 write A=2^a A_0 with A_0 odd.
An odd power preserves the leading term of F_A-1, and the subsequent2^a-th power is Frobenius.
Thus F_A^A-1 has order2^a and leading coefficient(beta^2)^(2^a), which is either beta or beta^2 and never1.
If B>0, writing B=2^b B_0 with B_0 odd gives order2^(b+1) for F_B^B-1 and leading coefficient1.
For B=0 its order is taken to be infinity.
If the two finite orders tie, their leading coefficients do not cancel, because beta and beta^2 are different from1.
Therefore

    ord_phi(F_A^A F_B^B-1)
       =m=min{2^v_2(A),2^(v_2(B)+1)}<=A,        (GM15)

with the second entry understood as infinity when B=0.
This proves the order for all stated exponents, without a coefficient scan or an unproved no-cancellation assumption.

To pass back to characteristic zero, write the integer rational unit F_0-s with its unit polynomial denominator.
The reduction of its numerator has exact phi-order m, for either sign s, since the signs agree modulo2.
Lift that factorization as numerator=Phi^m J+2K, with Jbar(beta) nonzero.
At x the first summand has valuation m/(6A)<=1/6, while the second has valuation at least1.
The denominator is a unit, so

    v(F_0-s)=m/(6A)<=1/6.                        (GM16)

This contradicts(GM13), proving(GM2) in full.
Neither the earlier parity restriction nor an exact characteristic-zero residual identity is needed for this contradiction.
The proof applies to all monic T in(GM1), including repeated factors and all higher coefficient lifts.

<a id="retained-intermediate-mechanisms"></a>
## Appendix: leading units and the complete degree30 correction mechanism

The following retains the useful intermediate argument of2026-10-20T13:45, including its exact seed and unique-correction analysis.
The general theorem above now excludes the entire support family, so its conditional actual leading-unit statement is not presented as nonempty additional coverage.
The fixed [v1 QR1--QR19](Yin_C_G0197_v1.md#argument), its [finite model family](Yin_C_G0197_v1.md#finite-congruence-family) and [explicit degree30 model](Yin_C_G0197_v1.md#explicit-degree30-model) retain their complete proofs and original scope; they are not recopied as a new version of those earlier arguments.

### A further necessary unit in the parameterized actual family

Use the complete actual original domain and full residual equations of [C197](Yin_C_G0197_v1.md#statement).
Thus the original quotient values are a=theta_2(delta), b=theta_3(delta), c=theta_5(delta), with2c^2=3a^5 and b^2-a^3+s(c^3-2b^5)=0, for s in{1,-1}.
In the family Tbar=X^A(X+1)^B phi^N, A>=2, B=0 or B>=2, N>6A, its proof forces N=7A and gives

    T=X^A(X+1)^B Phi^(7A)+2Phi^A V+4W_1,
    phi does not divide Vbar,
    Phi=X^2+X+1, phi=Phi mod2.

Let x be the actual matching root from [the general coefficient argument](#small-matching-root), put q=Phi(x), and normalize v(2)=1.
Then v(q)=1/(6A), and the residue beta of x is a root of phi.
The integer polynomial V has residue Vbar(beta) in F_4^*.
Write this residue as v_0, to distinguish it from the valuation v.

The exact quotient estimates in [C197](Yin_C_G0197_v1.md#actual-quotient-multiplicity-ratio) give

    a(x)=q^(2A)V(x)^2+error of valuation at least1,
    residue(a(x)/q^(2A))=v_0^2,
    residue(c(x)/q^(2A))=beta^A.                 (LU1)

For the second residue, c differs by an element of valuation at least1 from

    q^(2A)x^A(1+xq^2)^B Phi(xq^2)^(7A).

Both factors after x^A have residue1.
Thus the errors after division by q^(2A), of valuation1/3, have strictly positive valuation; these are legitimate residues of units, not an unjustified limiting argument.

Divide T(x)=0 by2q^A.
The higher term2W_1(x)/q^A has valuation at least5/6.
Since q^(6A)/2 is a unit, reduction gives

    residue(q^(6A)/2)
       =-v_0/[beta^A(beta+1)^B].

The exact identity3a(x)^5/(2c(x)^2)=1 now has residue

    v_0^11/[beta^(3A)(beta+1)^B]
       =v_0^2/beta^(2B)=1.                      (LU2)

Here beta^3=1, beta+1=beta^2, and v_0^3=1 in F_4^*.
The sign disappears in characteristic2.
Squaring is a bijection on F_4, so the further necessary condition is

    Vbar(beta)=beta^B,
    Vbar congruent X^B modulo phi.               (LU3)

It holds at both conjugate roots of phi by Frobenius.
In particular the explicit C197 example with A=2,B=0 and U=X Phi^2+X^2 Phi^4 has Vbar(beta)=beta, and therefore none of its4W lifts satisfies exact f=0.
Its finite modulo2 compatibility remains exactly as proved in C197.

### The stronger finite-ring theorem for the entire degree30 shape

Let T be ANY monic integer polynomial of degree30 with

    Tbar=X^2 phi^14.                              (ME1)

No irreducibility, total reality, original unit polynomial or exact residual solution is assumed in the following finite-ring statement.
Define the actual integer quotient polynomials by

    theta_p=rem_T(T(C_p))/p,
    C2=X^2-2, C3=X^3-3X, C5=X^5-5X^3+5X.

Their integrality follows from C_p congruent X^p modulo p and monic division.
For s in{1,-1}, put

    F_res=2theta_5^2-3theta_2^5,
    E_s=theta_3^2-theta_2^3
                      +s(theta_5^3-2theta_3^5).

Then it is impossible that BOTH

    F_res=0 and E_s=0 in (Z/4Z)[X]/(T mod4).      (ME2)

Equivalently F_res and E_s cannot both belong to the ideal(4,T) of Z[X].
In particular the actual original full residual system cannot have(ME1), at any original Mahler measure.
This theorem covers every coefficient lift and both signs, rather than one seed for a proposed diagnostic.

### All compatible first lifts and the exact f condition modulo4

Write T_0=X^2 Phi^14 and T=T_0+2U+4W, with deg U,deg W<30.
Suppose for contradiction that(ME2) holds.
Since T_0 is an integer square, the generic half-difference identity gives

    theta_2bar=Ubar^2

in the full quotient R_2=F_2[X]/(X^2 phi^14).
The odd quotient reductions depend only on Tbar, not on U or W.
For chi=X phi^2 and D=X phi^7, one has

    theta_3bar=0,
    theta_5bar=(chi+chi^2)^2,
    theta_5bar^2=X^4 phi^8,
    theta_5bar^3=X^2(X+1)^2 phi^12 in R_2.        (ME3)

These are the exact odd-quotient calculations of [C197's degree30 model](Yin_C_G0197_v1.md#explicit-degree30-model), now used only at their Tbar-dependent scope.
For completeness C3bar preserves phi and is divisible by X, so Tbar divides Tbar(C3bar).
Also D(chi)=chi(1+chi+chi^2)^7 has remainder chi+chi^2 modulo D.
Squaring gives the theta_5 identity, and further squaring and cubing give the last two reductions with their full X-primary factors.
No assumption about the previously chosen U in that example is imported.

The reduction of F_res=0 gives Ubar^10=0 in R_2, forcing X|Ubar.
The reduction of E_s=0 gives Ubar^6=theta_5bar^3, whose phi-order is exactly12<14.
Thus ord_phi Ubar=2.
Choose integer K with phi not dividing Kbar, absorb the even correction into W, and write the ACTUAL T as

    T=T_0+2U+4W,
    U=X Phi^2 K, deg U<30.                       (ME4)

This represents every first lift compatible with the assumed two congruences; K has not been fixed to one monomial.

Work in R_4=(Z/4Z)[X]/(T mod4).
Monicity gives a free Z/4Z basis1,X,...,X^29, so2H=0 in R_4 if and only if Hbar=0 in R_2.
Since theta_2=U^2+2Z in R_4 for some Z, expansion of the fifth power gives

    theta_2^5=U^10+2U^8 Z=U^10 in R_4.

The discarded term vanishes because Ubar^8=X^8 phi^16 Kbar^8 is divisible by the ENTIRE Tbar.
Moreover

    U^10=T_0 X^8 Phi^6 K^10
       =-2X^9 Phi^8 K^11 in R_4.

Here T_0=-2U in R_4, independently of the arbitrary4W.
Using(ME3), the actual first residual polynomial therefore has the exact congruence

    F_res=2X^4 Phi^8(1+X^5 K^11) in R_4.          (ME5)

The X-primary requirement is automatic because X^2 divides X^4.
The free-module fact just stated and the phi-order8 give the equivalence

    F_res=0 in R_4
       if and only if X^5 Kbar^11=1 modulo phi^6. (ME6)

Division by2 has thus been justified in the coefficient module; it is not cancellation of an arbitrary zero divisor in R_4.

### The unique correction class

Every unit H in F_2[X]/(phi^6) has H^3=1+phi L, since its residue is in F_4^*.
Raising to the eighth power gives H^24=1, because phi^8=0 in this quotient.
Thus the eleventh-power map is invertible, with inverse itself:11^2=121 is1 modulo24.
In particular X^24=1.
Equation(ME6) is therefore equivalent to the unique residue class

    Kbar congruent X^(-55)=X^17 modulo phi^6.     (ME7)

Conversely X^5(X^17)^11=X^192=(X^24)^8=1, so this class really satisfies the first residual congruence.
An integer representative may be written

    K=X^17+Phi^6 L+2H, L,H in Z[X].

For instance U=X^3 Phi^2 corresponds to K=X^2 and fails(ME7), although it passes the leading-unit condition(LU3).
The corrected seed U=X^18 Phi^2 corresponds to K=X^17 and passes(ME6).
The following argument covers that seed and every other K in(ME7), with all4W.

### An actual small root and the unavoidable second residual value

The coefficient argument in [the general proof](#small-matching-root) applies to every T in(ME4) with ord_phi Ubar=2.
Its root-existence and valuation calculation uses the displayed polynomial expression and matching multiplicities only; the subsequent use of F_res modulo4 to force a general N=7A is not needed here, since N=14 is already specified.
It yields an actual2-adic root x of T, with residue beta a root of phi, such that

    q=Phi(x), v(2)=1, v(q)=1/12.                 (ME8)

Both x and x-1 are units.
All values of integer polynomials at this root are integral.
In what follows, an error of valuation at least lambda means an element of that valuation bound, allowing the value zero.

Evaluating theta_2-U^2 in the ideal(2,T) gives an error of valuation at least1.
From(ME7) and U=X Phi^2 K,

    U(x)^2=x^36 q^4+error of valuation at least4/3.

Indeed the term from q^6 L squared has q-order16 after multiplication by q^4, while its cross term has valuation at least1+10/12; terms involving2H have still larger valuation.
The exact odd-quotient reduction(ME3) similarly lifts to an error in(2,T).
Consequently at the SAME root x,

    a=theta_2(x)=x^36 q^4+error v>=1,
    c=theta_5(x)=x^2 q^4+x^4 q^8+error v>=1,
    b=theta_3(x), v(b)>=1.                       (ME9)

These estimates retain the actual divided quotients; replacing them by arbitrary elements with the same valuation would lose the next comparison.

Cubing gives

    a^3-s c^3
       =q^12 x^6(x^102-s)+error v>=4/3.          (ME10)

For a, every term involving its error has valuation at least2/3+1=5/3.
For c, the first extra term from x^4 q^8 has valuation4/3; its higher terms and all terms involving the error have at least that valuation.
This verifies the full error bound for both signs.

The exact factorization x^3-1=(x-1)q gives v(x^3-1)=1/12.
Also

    x^51-1=(x^3-1) sum_(j=0)^16 x^(3j).

The sum has residue17=1, hence is a unit.
Thus v(x^51-1)=1/12, and v(x^51+1)=1/12 as well because their difference is2.
Multiplication and then addition of2 give, for both signs,

    v(x^102-1)=1/6,
    v(x^102+1)=1/6.

The main term in(ME10) therefore has valuation1+1/6=7/6, strictly below its error bound4/3.
It follows that

    v(a^3-s c^3)=7/6.                            (ME11)

On the other hand v(b^2-2s b^5)>=2 by(ME9).
Hence

    v(E_s(x))=7/6<2.

If E_s belonged to(4,T), evaluation at the integral root x of T would have valuation at least2.
This contradiction proves(ME2).
It uses only the assumed congruences modulo4, not an exact characteristic-zero residual equality, irreducibility or total reality.

### Consequences and exact remaining boundary

The parameterized leading-unit condition(LU3) is a further necessary constraint in the actual family of C197.
The complete degree30 result(ME2) excludes every monic integer T with reduction X^2 phi^14 from simultaneous residual congruences modulo4, including all allowed choices of U,K,W and both signs.
Thus the proposed exact linear diagnostic on30 binary coefficients of W has no solutions by this proof and need not be run.
No computation is claimed to have taken place.

The finite modulo2 examples in C197 remain correct.
They are now shown not to extend to the next pair of residual congruences for A=2,B=0.
The original actual-input corollary is the nonexistence of this complete support shape, at every original measure.
This special proof alone does not cover all A>2 or B>0; those parameters are covered by the separate general proof in this version.
Neither argument excludes every residue support, every canonical remainder of degree28 or all original residual inputs.

<a id="inputs-and-boundaries"></a>
## Exact inputs and version boundaries

| Input | Exact use |
| --- | --- |
| [C196v3 generic half-difference interface](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Delta_2 definition, integer monic remainder, mod4 expansion and product/power rules only; none of its specialized degree28, Hensel or canonical-Haar conclusions is a premise. |
| [R474 exact upstream finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Actual independent coverage of those generic identities, with this proof's authors and entropy's upstream identity relationship disclosed; this is not a review of the new general theorem. |
| [C153v2 original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Only the original-input corollary: same actual P/K/F/T and nonzero integral quotient values; the arbitrary-monic main theorem does not require those extra hypotheses. |
| [Preserved v1](Yin_C_G0197_v1.md#argument) | Complete QR1--QR19 parameter ratio/parity and finite modulo2 models remain fixed; the new arbitrary-monic proof does not import its exact-residual hypothesis across domains. |
| Elementary coefficient, localization and finite-field algebra | All root-existence,2-annihilator, error, rational-unit order and tied-order arguments are proved explicitly above; no new source theorem or computation is invoked. |

The finite congruence examples and the mod4 nonexistence are compatible because T modulo4 determining quotient equations modulo2 is distinct from those quotient equations vanishing modulo4.
All v1 equations and examples remain true at their stated scope.
The new theorem does not infer that an actual input in this support has merely an even canonical polynomial; it excludes the simultaneous residual congruences themselves.
The support cases N<=6A, extra irreducible factors, all other canonical degrees and the original full transfer problem remain outside this result.
The appendix's general leading unit and degree30-specific K-class are retained as complete useful intermediate mechanisms, not independent checks of the authors' new theorem.
A whole independent review of this actual v2 remains required before adoption.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:57 |
| status | open |
| reason | Strengthen the same whole-support family from necessary ratio/parity to complete impossibility of simultaneous residual equations modulo4 for arbitrary monic T. Preserve v1, all finite modulo2 models and complete useful leading-unit/degree30 mechanisms. The new general proof, every local cancellation and all quantitative error interfaces require independent whole review; no adoption is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete arbitrary-monic exclusion](#statement) | Every stated A/B/N, entire Tbar support, both signs, all higher lifts and arbitrary monic T; actual original-input corollary and exact distinction from retained modulo2 models. |
| argument | [Complete general proof and retained appendix](#argument) | GM1--GM16, self-contained root existence under congruences alone, localized2-annihilator, full V11 comparison and error chain, tied rational-unit orders, LU1--LU3 and ME1--ME11 seed/unique-correction mechanisms. |
| dependency | [Generic divided-quotient identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Exact generic Delta_2, monic division and product/power interface only; no specialized root or degree theorem is used. |
| dependency | [Actual original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Only the original reciprocal/trace-input corollary; arbitrary monic proof is separately complete. |
| support | [Actual independent upstream review](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Generic algebraic interface already independently checked; does not cover the new GM or appendix arguments. |
| support | [Preserved entire v1](Yin_C_G0197_v1.md#argument) | All QR1--QR19 and old necessary-stage proofs remain unchanged, with no retroactive scope upgrade. |
| support | [Retained finite modulo2 family](Yin_C_G0197_v1.md#finite-congruence-family) | All even-A,B=0 formal lifts and arbitrary4W remain valid for the equations modulo2, not modulo4. |
| support | [Inputs, roles and exact limits](#inputs-and-boundaries) | Root and draft_comparison_cleanup are new-proof contributors; upstream identity role disclosed, actual source/review scope preserved, no program or broader support exclusion. |

### Decision whole-reviewed-2026-10-20

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T14:12 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the entire arbitrary-monic prescribed-support mod4 exclusion through actual whole R476. Every allowed exponent, both signs and all higher lifts are covered, together with the complete retained leading-unit and degree30 mechanisms. Preserve the physical v1, its valid equations modulo2, the earlier actual R621 scope and every original-input hypothesis. Extra support factors and the unrestricted original transfer remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete arbitrary-monic exclusion](#statement) | Every stated A/B/N, entire Tbar support, both signs, all higher lifts and arbitrary monic T; actual original-input corollary and exact distinction from retained modulo2 models. |
| argument | [Complete general proof and retained appendix](#argument) | GM1--GM16, self-contained root existence under congruences alone, localized2-annihilator, full V11 comparison and error chain, tied rational-unit orders, LU1--LU3 and ME1--ME11 seed/unique-correction mechanisms. |
| dependency | [Generic divided-quotient identities](Yin_C_G0196_v3.md#degree28-mod4-quotient-classification) | Exact generic Delta_2, monic division and product/power interface only; no specialized root or degree theorem is used. |
| dependency | [Actual original trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Only the original reciprocal/trace-input corollary; arbitrary monic proof is separately complete. |
| support | [Actual independent upstream review](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Generic algebraic interface already independently checked; does not cover the new GM or appendix arguments. |
| support | [Preserved entire v1](Yin_C_G0197_v1.md#argument) | All QR1--QR19 and old necessary-stage proofs remain unchanged, with no retroactive scope upgrade. |
| support | [Retained finite modulo2 family](Yin_C_G0197_v1.md#finite-congruence-family) | All even-A,B=0 formal lifts and arbitrary4W remain valid for the equations modulo2, not modulo4. |
| support | [Inputs, roles and exact limits](#inputs-and-boundaries) | Root and draft_comparison_cleanup are new-proof contributors; upstream identity role disclosed, actual source/review scope preserved, no program or broader support exclusion. |
| review | [Whole independent prescribed-support finding](../audits/reviews/Yin_R_G0476_v1.md#prescribed-support-mod4-whole-finding) | Entire actual GM1--GM16, LU1--LU3 and ME1--ME11, all quantified domains, every local cancellation and error, both signs, all lifts, all dependencies and support, and exact distinction between modulo2 models and modulo4 impossibility. |

