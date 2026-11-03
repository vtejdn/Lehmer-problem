---
author: Yin
---
# The actual canonical residual has no nonzero dyadic reduction below degree28

Date: 2026-10-20T13:29.
Human author Yin.
This substantive v3 strengthens the same actual-residual multiplicity and canonical-degree problem as [v2](Yin_C_G0196_v2.md#statement), preserving the physical v1/v2 versions, v2's [adopted decision](Yin_C_G0196_v2.md#decision-whole-reviewed-2026-10-20) and its [whole R473 finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding).
The present argument does not retrospectively extend those review scopes.
Root supplied the C5-composition route, low-degree budget and equality-shape refinements, the explicit mod4 model, and the candidate higher-adic slope and valuation contradiction.
The draft_comparison_cleanup agent supplied the complete small-degree finite-field graph, direct degree4 exclusion, full degree budget and formal equality model.
The entropy_attainment_bridge agent independently reached the same mod4 model during author work, supplied the complete classification of mod4 lifts, the scaled simple-root Hensel construction and quotient valuation proof, and assembled this fixed version.
All three are mathematical contributors, not independent reviewers of this version.
The necessary older C191 and C196v2 proof inputs retain their actual independent R468/R473 scope and disclosed upstream authorship.
No numerical computation, symbolic enumeration, chosen numerical parameter, new source acquisition or new original-input realization is used.

<a id="statement"></a>
## Complete statement

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient1 and degree d=2r.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta), and assume that the actual trace field F is totally real.
Let T in Z[X] be its monic degree-r minimal trace polynomial, so P(z)=z^r T(z+z^(-1)) and [K:F]=2.
For p=2,3,5 define C_p(z+z^(-1))=z^p+z^(-p) and the ACTUAL integer quotient polynomials

    theta_p=rem_T(T(C_p(X)))/p in Z[X],
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta).

The values a,b,c are nonzero algebraic integers in the original F.
For some s in{1,-1}, assume the complete quotient identities

    2theta_5^2-3theta_2^5=0,
    theta_3^2-theta_2^3
       +s(theta_5^3-2theta_3^5)=0 in Z[X]/(T),
    g=c^3-2b^5!=0.                               (CR1)

For an actual irreducible T these are exactly f=e+s g=0 in F, with e=b^2-a^3 and f=2c^2-3a^5; monicity keeps the integral quotient and all coefficient divisibilities.
No abstract integral triple or realization of only its ambient field replaces these self-compositions.
Put

    G_can=rem_T(theta_5^3-2theta_3^5) in Z[X],
    w=deg G_can<r,
    R=G_can mod2.

Then

    R!=0 implies deg R>=28 and w>=28;
    w<=27 implies every coefficient of G_can is even.
                                                            (CR2)

In particular, with normalized Haar probability mu,

    w<=27 implies
    I_can=integral_T log G_can(z+z^(-1))^2 dmu
                                      >=2log2.    (CR3)

No small-m(P), bounded ramification, one-prime or full residue-degree-one assumption is imposed.
The entire zero reduction is allowed, and degree drop modulo2 is retained.
The conclusion does not assert that actual residual inputs of larger canonical degree exist or that all residual inputs are impossible.

The following exact intermediate mechanisms are part of the statement and are retained completely.

1. For U=T mod2 and chi=C5 mod2=X^5+X^3+X, the actual canonical identity is R=rem_U(U(chi)^3).
   The full finite-field graph, actual cluster multiplicities and this identity imply deg R>=27 whenever R!=0.
   Equality27 has the unique necessary form U=X^2 phi^13, R=X^3 phi^12, r=28, where phi=X^2+X+1.
   That form is an exact formal equality model for the stated finite-field graph and remainder conditions, including all multiplicities; it is not an original integer-field realization.
2. For Phi=X^2+X+1 in Z[X], every monic integer T of degree28 with T mod2=X^2 phi^13 can be written T=X^2 Phi^13+2U_1+4W with deg U_1,deg W<28.
   Its ACTUAL divided quotient obeys theta2bar=U_1bar^2 in F_2[X]/(X^2 phi^13).
   The full residual equations modulo2 hold exactly when X divides U_1bar and ord_phi U_1bar=2.
   This gives3*2^21 compatible mod4 lifts and, for each, arbitrary4W modifications; no lift count is obtained by execution.
3. Every such compatible integer lift has an actual root delta0 in a finite2-adic extension with v_2(Phi(delta0))=1/11 and v_2(theta2(delta0))=v_2(theta5(delta0))=4/11.
   Hence the two sides of its exact f=0 equation have distinct valuations19/11 and20/11.
   This excludes the finite-field equality shape as an actual full residual input and yields(CR2).
   This local obstruction even holds without irreducibility or real-root hypotheses on the monic degree28 T, provided the quotient identities are imposed in Q[X]/(T).

The general integer-representative multiplicities, squarefree impossibility, periodic unramified-lift sublemma and preserved SF1--SF13 comparison of v2 remain at their [exact fixed proof](Yin_C_G0196_v2.md#argument).
They are not discarded or duplicated as a new proof here.
This version strengthens the canonical conclusion using the actual C5 quotient, which is absent from a free-coordinate nilpotence model.
The original norm/Haar transfer for larger canonical degree, other rational representatives and the unrestricted G0001 objective remain unresolved.

<a id="argument"></a>
## Complete proof

<a id="canonical-c5-residue-graph"></a>
## PartI. The exact C5 graph and the formal degree27 boundary

### Actual original input and the stronger remainder identity

Use the complete original domain of [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain).
Thus P is monic irreducible reciprocal nontorsion in Z[z], of degree d=2r and constant coefficient1; for a root alpha put delta=alpha+alpha^(-1), F=Q(delta), and let T in Z[X] be the actual monic degree-r trace polynomial.
The actual trace field F is totally real, P(z)=z^r T(z+z^(-1)), and the original quotient polynomials are

    theta_p=rem_T(T(C_p(X)))/p in Z[X],
    a=theta_2(delta), b=theta_3(delta),
    c=theta_5(delta), e=b^2-a^3,
    f=2c^2-3a^5, g=c^3-2b^5.

Assume the FULL actual residual system f=e+s g=0, g!=0, s in{1,-1}.
Let

    G_can=rem_T(theta_5^3-2theta_3^5) in Z[X],
    w=deg G_can<r,
    U=T mod2, R=G_can mod2,
    chi=C5 mod2=X^5+X^3+X,
    phi=X^2+X+1, so chi=X phi^2.                 (CG1)

In this section R is assumed nonzero; the entire zero reduction remains a separate possibility.
The integer degree w need not equal deg R, since reduction may lower degree.
The new conclusion is the necessary bound and equality implication

    deg R>=27, hence w>=27;
    deg R=27 implies
       U=X^2 phi^13, R=X^3 phi^12, r=28.          (CG2)

In particular w=27 has this same necessary shape.
This conclusion holds at every original Mahler measure; no small-measure or favorable-Haar hypothesis is used.

The actual quotient formula is stronger than a congruence involving an unspecified theta_5.
Monic division commutes with reduction modulo2, and5 is1 in F_2.
Consequently

    theta_5 mod2=rem_U(U(chi)),
    R=rem_U(U(chi)^3).                            (CG3)

The first equality follows by reducing the integer identity T(C5)=T Q+5theta_5.
The second follows from the canonical definition and the first congruence, since the term2theta_3^5 vanishes modulo2.
It is an identity of polynomial remainders, not only an equality of values at the reduced generator.

The complete cluster input is [C191v2 Sections1--3](Yin_C_G0191_v2.md#argument), with the independent [R468 finding](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding).
For an irreducible factor psi of U of degree h, the maximal-order filtration gives its full exponent

    N_psi=sum_(p in the psi cluster) e_p f_p/h.

The [C178 full residual theorem](Yin_C_G0178_v1.md#statement) excludes every unramified prime above2, so every e_p>=2 and N_psi>=2.
It also gives5A_p=e_p+2C_p and G_p=3C_p, for A_p=v_p(a), C_p=v_p(c), G_p=v_p(g).
The per-cluster C191 estimate therefore gives

    sum_(p in the psi cluster) f_p G_p
       >=(6/11)h N_psi>0.                        (CG4)

Thus psi divides R in EVERY cluster.
At a root x of psi, (CG3) yields U(chi(x))=0.
In particular the complete geometric root set Sigma(U) is chi-stable.
A global positive norm exponent alone would not prove this per-cluster assertion.
The multiplicity and canonical gates overlap the existing [C196v2 interface](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape); the additional actual self-composition in(CG3) is used here explicitly.

### Composition multiplicities and an unsaturated orbit

For a geometric root x of U in an algebraic closure of F_2, let N_x be its multiplicity, put y=chi(x), and let e_5(x) be the order of chi(X)-chi(x) at X=x.
All roots of one irreducible factor have the same N_x.
Since y belongs to Sigma(U), local polynomial factorization gives

    ord_x U(chi)=e_5(x) N_y.

Equation(CG3) now implies, with nu_x=ord_x R,

    nu_x>=min{3e_5(x)N_y,N_x}>=2;
    nu_x<N_x implies nu_x=3e_5(x)N_y.             (CG5)

Indeed R-U(chi)^3 is divisible by U, so its order at x is at least N_x.
If nu_x<N_x, the two unequal orders force equality with the order of U(chi)^3.
The lower bound2 uses both N_x>=2 and N_y>=2.
Orders at conjugate roots are equal, so an irreducible orbit of degree h and order nu contributes h nu to deg R.

Because R is nonzero and deg R<deg U, not all orbits can be saturated, where saturated means nu_x>=N_x.
Otherwise U would divide R.
Fix an unsaturated orbit, and call its degree h.
The polynomial chi has F_2 coefficients, so it commutes with Frobenius and sends this orbit onto a single orbit whose degree divides h.
If it sends the orbit to itself, then N_y=N_x, and(CG5) forces saturation.
Thus an unsaturated orbit must have a DISTINCT target orbit.

The derivative is chi'=X^4+X^2+1=phi^2.
At a root of phi the factorization chi=X phi^2 shows local degree2, since x is nonzero and phi has simple roots.
At every other point the derivative is nonzero and the local degree is1.
These facts account for all local multiplicities, including the critical degree2 orbit.

### The complete small-degree graph without a scan

The complete list of irreducible orbits of degrees at most4 and their targets is

| Source minimal polynomial | Target minimal polynomial | Local degree e_5 |
| --- | --- | --- |
| X | X | 1 |
| X+1 | X+1 | 1 |
| phi=X^2+X+1 | X | 2 |
| A3=X^3+X+1 | A3 | 1 |
| B3=X^3+X^2+1 | B3 | 1 |
| A4=X^4+X+1 | C4 | 1 |
| B4=X^4+X^3+1 | X+1 | 1 |
| C4=X^4+X^3+X^2+X+1 | A4 | 1 |

Here C4 is a label for the displayed irreducible quartic, not the integer Chebyshev polynomial.
The list and arrows follow from the following exact identities.
Both0 and1 are fixed by chi.
The only irreducible quadratic is phi, and chi=X phi^2 sends both its roots to0 with local degree2.

A monic irreducible cubic has constant coefficient1 and no root1, leaving exactly A3 and B3.
For a root x of A3, the relation x^3=x+1 gives chi(x)=x^4.
For a root x of B3, the relation x^3=x^2+1 gives chi(x)=x^2.
Each is a Frobenius power of x, proving that BOTH degree3 orbits are individually preserved.
They therefore cannot be unsaturated.

A monic quartic with constant1 and no root1 has an odd sum of its three middle coefficients.
The four possibilities are A4, B4, C4 and X^4+X^2+1=phi^2.
The first three reduce modulo phi to1, X and X+1 respectively.
None has a linear or irreducible quadratic factor, so they are irreducible and exhaust the degree4 orbits.
The factorization

    chi+1=(X+1)B4                              (CG6)

gives the B4 arrow.
For x a root of C4, one has x^5=1, and y=chi(x)=x^3+x+1 satisfies

    y^2=x^2+x+1, y^4=x^3+x,
    y^4+y+1=0.

Hence y is a root of A4.
For x a root of A4, one has x^4=x+1, and y=chi(x)=x^3+x^2 satisfies

    y^2=x^3+x^2+x+1, y^3=x^3, y^4=x^3+x,
    y^4+y^3+y^2+y+1=0.

Hence y is a root of C4.
This proves both remaining arrows by exact polynomial reduction and completes the graph.
No assumption about the degrees of the full local residue fields is made from these generator-orbit degrees.

### The degree budget and the two possible branches below28

The unsaturated source cannot have degree1 or3, because those orbits are preserved.
For the degree2 source phi, its target0 has multiplicity N_0>=2, and(CG5) gives

    nu_phi=6N_0, N_phi>6N_0.

The fixed point0 is saturated, so its contribution to deg R is at least N_0.
The combined contribution of these two distinct orbits is at least

    2nu_phi+N_0=13N_0>=26.                       (CG7)

For any unsaturated source of degree h>=4, the local degree is1.
Its target has some degree k>=1 and multiplicity at least2, so source and target contribute at least

    6h+2k.                                      (CG8)

If h>=5 this is at least32.
For A4 or C4, the target also has degree4, giving at least32.
The only remaining degree4 possibility is B4 mapping to1.
Writing N_1 for the target multiplicity, source and fixed target contribute at least13N_1>=26.

Suppose temporarily that deg R<=27.
The source is therefore either phi or B4, and its linear target has multiplicity exactly2.
There are no other orbits in U: any additional orbit contributes at least2 to deg R by(CG5), beyond the already required26.
Thus there are exactly two possible forms before the exact remainder is used:

    U=X^2 phi^N, N>=13,
    R=X^2 phi^12 L, deg L<=1;                    (CG9)

or

    U=(X+1)^2 B4^N, N>=7,
    R=(X+1)^2 B4^6 L, deg L<=1.                 (CG10)

The polynomial L in each line is nonzero over F_2.
Its possible extra factors are not asserted to be factors of U.
The source order is exactly12 or6 respectively, so L is not divisible by the source polynomial.
These statements also cover degree26 or smaller; the earlier budgets already exclude degree below26.

In(CG10), use(CG6) in the exact remainder identity:

    U(chi)^3=(X+1)^6 B4^6 B4(chi)^(3N).

Modulo B4, one has chi=1 and B4(1)=1.
Since N>=7, comparison with R modulo B4^7 and division by B4^6 give

    (X+1)^2 L congruent (X+1)^6 modulo B4,
    L congruent (X+1)^4 congruent X^3 modulo B4.  (CG11)

The factor X+1 is invertible modulo B4.
A polynomial of degree at most1 cannot be congruent to X^3 modulo the degree4 polynomial B4.
This excludes the entire B4 branch under deg R<=27.
It uses no additional C3-closure claim.

### The unique degree27 shape and its exact formal attainability

In(CG9), put

    V=phi(chi)=1+X phi^2+X^2 phi^4,
    U(chi)^3=X^6 phi^12 V^(3N).                  (CG12)

Since N>=13, reducing R congruent U(chi)^3 modulo phi^13 gives, after division by phi^12,

    X^2 L congruent X^6 modulo phi,
    L congruent X^4 congruent X modulo phi.

The unique representative of degree at most1 in this residue class is L=X.
Thus R=X^3 phi^12 and deg R=27.
In particular degree26 is impossible.

To determine N, use V congruent1 modulo phi^2 in(CG12).
The difference from this forced R is

    U(chi)^3-R=X^3 phi^12 [X^3 V^(3N)-1].

The bracket is congruent to X^3-1=(X+1)phi modulo phi^2.
Its phi-adic order is exactly1, because X+1 is coprime to phi.
Hence the complete difference has phi-adic order exactly13.
Divisibility by U forces N<=13, while unsaturation already gave N>=13.
Therefore

    N=13, U=X^2 phi^13, R=X^3 phi^12,
    deg U=28, deg R=27.                          (CG13)

This proves(CG2).

There is an exact formal equality model over F_2.
Set U_0=X^2 phi^13.
Its root set is chi-stable, its geometric root multiplicities are2 and13, and both are at least2.
Formula(CG12) with N=13 shows

    rem_(U_0)(U_0(chi)^3)=X^3 phi^12.

Indeed the difference has a factor phi^13 and a factor X^3, so is divisible by X^2 phi^13, while the displayed remainder has degree27<28.
Thus27 is sharp for the stated finite-field conditions: nonzero canonical remainder, chi-stability, multiplicities at least2, and the exact self-composition congruence.

This formal model is not asserted to lift to an irreducible integer T, to an actual totally real trace field, or to the original pair of residual equations.
It verifies sharpness of these particular necessary finite-field conditions only.
PartII below excludes the equality case by its actual divided quotient and a higher-adic valuation, without contradicting this formal calculation.
No conclusion that an actual input of degree28 exists is supplied.
This finite-field section does not classify all larger residue graphs or resolve the original transfer problem; PartIII gives the precise combined canonical-degree and Haar consequence.

<a id="degree28-divided-quotient-lift"></a>
## PartII. Complete mod4 compatibility and the higher-adic obstruction

The quotient identities used here are precisely(CR1), with C2=X^2-2, C3=X^3-3X and C5=X^5-5X^3+5X.
This part proves its local polynomial statement for any monic integer T with the specified reduction, rather than assuming irreducibility or total reality.
Its uses as an original input retain the exact C153 field/quotient interpretation in the statement.
The symbol U below denotes the mod4 lift correction; it is distinct from U=T mod2 used in PartI.

### Exact finite-ring statement and stronger integer obstruction

Put

    Phi(X)=X^2+X+1 in Z[X],
    phi=Phi mod2, B0(X)=X^2 Phi(X)^13,
    Bbar=X^2 phi^13,
    A=F_2[X]/(Bbar).                              (DQ1)

Let T be ANY monic integer polynomial of degree28 with T mod2=Bbar.
Write

    T=B0+2U+4W, U,W in Z[X], deg U,deg W<28.

The residue Ubar is fixed by T mod4 relative to this chosen B0; its integer lift and W need not be unique.
For p=2,3,5 let

    theta_p=rem_T(T(C_p(X)))/p in Z[X],
    C2=X^2-2, C3=X^3-3X, C5=X^5-5X^3+5X.

These quotients are integral by C_p congruent X^p modulo p and monic division, irrespective of irreducibility or total reality of T.
Bars on theta_p below mean their classes in A.
For both signs s, the complete residual equations modulo2 are equivalent to

    theta2bar^5=0,
    theta3bar^2+theta2bar^3+theta5bar^3=0 in A.    (DQ2)

They hold if and only if

    X divides Ubar, ord_phi(Ubar)=2.              (DQ3)

Every such compatible lift has

    theta3bar=0,
    gbar=theta5bar^3=X^3 phi^12 in A,             (DQ4)

whose unique degree-below28 representative is nonzero of degree27.
In particular T=B0+2X Phi^2+4W gives an explicit compatible family for every integer W of degree below28.

Nevertheless, NO integer polynomial in the compatible family(DQ3) can satisfy

    2theta5^2-3theta2^5=0 in Q[X]/(T).            (DQ5)

Consequently no original irreducible integer trace polynomial with reduction Bbar can satisfy BOTH exact residual equations, even though their full modulo2 reductions with the actual divided quotient are compatible.
This is a higher-adic obstruction for this one prescribed shape, not a statement that all original residual inputs are impossible.
The proof of(DQ5) needs neither irreducibility nor real-root hypotheses.

<a id="degree28-mod4-quotient-classification"></a>
### 1. The actual divided self-composition depends on T modulo4

For any integer polynomial F define the integer polynomial

    Delta_2(F)=(F(C2(X))-F(X)^2)/2.

Its integrality follows from the exact characteristic-two congruence.
Since rem_T(T^2)=0 and integer division by a monic polynomial commutes with multiplication by2,

    theta2=rem_T Delta_2(T).

Expanding T=B0+2U+4W before reduction gives

    Delta_2(T) mod2
       =Delta_2(B0) mod2+Ubar(X^2)
       =Delta_2(B0) mod2+Ubar^2.                 (DQ6)

Thus the division by2 is paid before passing to A; theta2bar is not an arbitrary nilpotent variable.
For products the direct identity is
Delta_2(FG) congruent F^2 Delta_2(G)+G^2 Delta_2(F) modulo2.
It gives Delta_2(F^n) congruent n F^(2n-2)Delta_2(F) modulo2.
Here

    Delta_2(X^2) mod2=0,
    Delta_2(Phi) mod2=X^3+X^2+X+1=(X+1)^3,
    Delta_2(B0) mod2=X^4 phi^24 (X+1)^3.

The last polynomial is divisible by the FULL Bbar=X^2 phi^13.
Therefore

    theta2bar=Ubar^2 in A.                       (DQ7)

Every Ubar of degree below28 occurs as a mod4 lift, so the possible theta2bar values are precisely the image of the squaring map A->A.
No derivative condition on a hypothetical free coordinate replaces this exact lift calculation.
Adding any4W leaves(DQ7) unchanged.

### 2. The two odd quotients and complete residual compatibility

Division by3 and5 is the identity modulo2.
Thus theta3bar and theta5bar depend only on Bbar, not on the mod4 lift Ubar or the higher coefficients W.
In F_2[X],

    C3bar=X^3+X, C5bar=X^5+X^3+X=X phi^2.

The polynomial C3bar has a factor X, and if beta is a root of phi then beta^3=1 and C3bar(beta)=1+beta=beta^2, again a root of phi.
Therefore Bbar divides Bbar(C3bar), with the full exponents2 and13, and theta3bar=0.
For C5bar put

    Psi=1+X phi^2+X^2 phi^4=phi(C5bar).

Then

    theta5bar=X^2 phi^4 Psi^13 in A,
    Psi congruent1 modulo phi^2,
    theta5bar^3=X^3 phi^12 in A.                 (DQ8)

To check the last identity, cubing the first expression gives X^6 phi^12 Psi^39.
The factor Psi^39-1 is divisible by phi^2.
Also X^6-X^3=X^3(X+1)phi in characteristic2.
These two differences are divisible by X^2 phi^13, retaining the X-primary component as well as the phi-primary one.
The polynomial X^3 phi^12 has degree27 and is nonzero, so it is already the canonical representative of this class.

Equations(DQ2) are now exactly

    Ubar^10=0, Ubar^6=X^3 phi^12 in A.            (DQ9)

In the X-primary component, the second equality forces X|Ubar.
In the phi-primary component, its right side has exact phi-order12, smaller than13.
Thus 6 ord_phi(Ubar)=12 and ord_phi(Ubar)=2.
This proves necessity of(DQ3).

Conversely assume(DQ3) and write Ubar=phi^2 Z with phi not dividing Z.
Modulo phi the nonzero residue Z belongs to the field with four elements, so Z^3=1 there.
It follows that Ubar^6=phi^12 modulo phi^13.
The right side of(DQ9) has the same residue because X^3=1 modulo phi.
Both sides vanish modulo X^2, and coprimality of X and phi gives the full second equality in A.
The first equality follows from the X-order at least10 and the phi-order20 of Ubar^10.
This proves sufficiency, including both residual signs since1=-1 modulo2.

For a finite algebraic description of all lifts, condition(DQ3) is equivalently
Ubar=X phi^2 Z with deg Z<23 and phi not dividing Z.
There are3*2^21 such Ubar among the2^28 possible mod4 lifts: evaluation modulo phi maps that23-dimensional binary coefficient space onto F_4, and each of its four fibers has2^21 elements.
This is an exact vector-space count, not an executed enumeration.

Taking U=X Phi^2 gives the explicit compatible T=B0+2X Phi^2+4W.
At W=0 it visibly factors as X Phi^2(X Phi^11+2), so it is not an actual irreducible trace input.
An arbitrary4W preserves compatibility but does not establish irreducibility, total reality or either integer residual equation.
The following argument rules out the latter exact equations for every compatible lift, not just this visibly reducible example.

<a id="degree28-scaled-hensel-obstruction"></a>
### 3. An actual root with valuation1/11, using only simple-root Hensel

For a compatible Ubar, choose integer V,Z with

    U=Phi^2 V+2Z, phi not dividing V mod2.

Such choices exist by lifting the quotient Ubar/phi^2 coefficientwise.
Absorb Z into W and write the ACTUAL integer polynomial as

    T=X^2 Phi^13+2Phi^2 V+4W1,
    phi not dividing V mod2.                     (DQ10)

Only ord_phi Ubar=2 is needed for this local obstruction; the X-divisibility from full finite compatibility is not used in the construction.
Choose a root beta of Phi in an algebraic closure of Q_2 and an element pi with pi^11=2.
Work in the finite complete extension L=Q_2(beta,pi), with valuation v normalized by v(2)=1.
Both beta and pi are integral, v(pi)=1/11, and the residue of beta generates F_4 because phi is irreducible over F_2.
The element u0=2beta+1 is a unit.
No assumption about the degree or maximal power order of L is needed.

Substitute X=beta+pi Y.
The exact identity Phi(beta+pi Y)=pi Y(u0+pi Y) gives the integral polynomial

    F(Y)=T(beta+pi Y)/pi^13
       =(beta+pi Y)^2 Y^13(u0+pi Y)^13
          +Y^2(u0+pi Y)^2 V(beta+pi Y)
          +pi^9 W1(beta+pi Y) in O_L[Y].         (DQ11)

All its coefficients are integral by the displayed expression; division by pi^13 is not asserted integral without this calculation.
The identity4/pi^13=pi^9 uses pi^11=2.
In the residue field,

    Fbar(Y)=Y^2(beta_bar^2 Y^11+v0),
    v0=Vbar(beta_bar) in F_4^*.

The eleventh-power map on F_4^* is the square map, hence a bijection.
For example y0=(v0/beta_bar^2)^2 satisfies beta_bar^2 y0^11=v0.
Thus y0 is a nonzero root of Fbar, and
Fbar'(y0)=beta_bar^2 y0^12 is nonzero.
Lift y0 to any integral element of L.
The accepted [Con26e-U001 simple-root Hensel theorem](../audits/literature/Con26e/Yin_U001.md#con26e-u001) applies: the polynomial value has positive valuation and the derivative is a unit.
It gives a unit y in O_L with F(y)=0 and residue y0.
The actual root

    delta0=beta+pi y, T(delta0)=0,
    v(Phi(delta0))=1/11                          (DQ12)

therefore exists.
The valuation is exact because y and u0+pi y are units.
This proof neither assumes a Newton-polygon slope is realized nor imports a separate unramified-field existence theorem.

### 4. The actual quotient valuations contradict f=0

All evaluations in this paragraph use delta0 and the SAME T of(DQ10).
Since Phi(delta0) has valuation1/11 and V(delta0) is a unit,
U(delta0)=Phi(delta0)^2 V(delta0)+2Z(delta0) has exact valuation2/11.
Equation(DQ7), interpreted in the integer quotient before evaluation, says
theta2-U^2=T A1+2A2 for some A1,A2 in Z[X].
Thus at delta0 the difference theta2(delta0)-U(delta0)^2 has valuation at least1.
Because4/11<1,

    v(theta2(delta0))=4/11.

Similarly lift the polynomial in(DQ8) to
Cstar=X^2 Phi^4(1+X Phi^2+X^2 Phi^4)^13 in Z[X].
The same quotient congruence gives theta5-Cstar=T A3+2A4 with A3,A4 integral.
At delta0, both delta0 and1+delta0 Phi(delta0)^2+delta0^2 Phi(delta0)^4 are units, so Cstar(delta0) has valuation4/11.
Its difference from theta5(delta0) has valuation at least1.
Consequently

    v(theta2(delta0))=v(theta5(delta0))=4/11,
    v(2theta5(delta0)^2)=19/11,
    v(3theta2(delta0)^5)=20/11.                  (DQ13)

The two nonzero terms have different valuations and cannot be equal.
Therefore T does not divide2theta5^2-3theta2^5 even in Q[X], proving(DQ5).
Monicity makes Z[X]/(T) a free Z-module, so exact rational-quotient residual identities among these integral elements would first imply(DQ2) in the full reduction.
If T is the actual irreducible trace polynomial of an original input, equality f=0 in Q(delta) would force precisely that polynomial divisibility and would hold at every root of T, including delta0.
The constructed root gives the contradiction without any loss of original quotient normalization.

The finite-ring compatibility(DQ2)--(DQ4) is genuine, but does not extend to an exact characteristic-zero residual solution.
The higher-adic contradiction(DQ13) excludes the prescribed Tbar=X^2 phi^13 shape with the full original quotients.
No claim about every other factor-multiplicity shape follows from this one local calculation.
PartIII combines this local obstruction with the complete graph argument in PartI; the local calculation alone excludes only the displayed degree28 residue shape.
No numerical near-one input, full trace realization, irreducibility certificate, unrestricted Haar transfer or completion of D35/D36 is asserted.

<a id="canonical-degree28-global-consequence"></a>
## PartIII. Global degree and the full integer Haar consequence

Suppose R=G_can mod2 is nonzero and deg R<=27.
PartI, specifically(CG2), forces deg R=27 and the exact equality shape T mod2=X^2 phi^13 with r=28.
The exact identities(CR1) imply their reductions(DQ2), because monic division makes Z[X]/(T) free over Z.
PartII classifies those reductions and then rules out the exact f=0 identity for every compatible lift.
This contradiction proves deg R>=28 whenever R is nonzero.
Since deg R<=w, it also proves the first line of(CR2).
If w<=27, the reduction is consequently zero and EVERY coefficient of G_can is even; this is stronger than a statement only about its leading coefficient.

The nonzero g ensures G_can is not the zero polynomial.
Define the nonzero integer polynomial

    H_1(z)=z^w (G_can/2)(z+z^(-1)).

For w>=1 it has degree2w and nonzero leading and constant coefficient; for w=0 it is a nonzero integer constant.
The [Smy08-U001 scalar Jensen interface](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) gives m(H_1)>=0, with all root multiplicities and integrable circle zeros included.
The monomial has modulus1 on the circle, so

    I_can=2log2+2m(H_1)>=2log2.

This proves(CR3) without dividing by r, d or the degree of H_1 and without an m(P) hypothesis.
It is stronger than the earlier guaranteed residual threshold(12/11)log2, but supplies no original-field norm comparison for an unrelated auxiliary polynomial.
The formal finite-field sharpness at27 is compatible with the stronger actual bound28: those finite-field conditions omit the higher-adic and exact divided-quotient obstruction proved in PartII.
No actual input attaining28 or any larger degree is constructed.

<a id="exact-inputs"></a>
## Exact inputs and boundaries

| Input | Exact scope used |
| --- | --- |
| [C153v2](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual original reciprocal and trace fields, quotient values and nonzero integrality; all three self-compositions use the same T. |
| [C178](Yin_C_G0178_v1.md#statement) | Full residual G_p=3C_p,5A_p=e_p+2C_p and exclusion of each unramified2-prime. |
| [C191v2](Yin_C_G0191_v2.md#argument) | Complete exponent formula from the maximal-order filtration and per-cluster positive norm income, including all residue weights and nonmaximal power orders. |
| [C196v2](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | Accepted arbitrary-representative saturation interface and exact prior scope; its stronger preserved source/valuation arguments remain in that fixed version. |
| [Con26e-U001](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Simple-root Hensel in the explicitly constructed complete finite extension of Q_2, with integral scaled polynomial, residue unit root and unit derivative checked locally. |
| [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Scalar Jensen/root-product convention, nonzero constants and integrable circle zeros, with the factor2log2 and full degree retained. |
| Elementary polynomial and finite-field algebra | Complete degree1--4 orbit list, all local composition multiplicities, full degree budget/equality model, mod4 lift classification/count and actual quotient valuation contradiction; no native enumeration or new external theorem. |

The polynomial phi=X^2+X+1 used for the explicit finite-field orbit has simple roots; the original T mod2 retains every repeated factor and is never replaced by its squarefree part.
The local Hensel proof uses an actual root in a finite extension and does not assume that a formal slope is realized.
The full model over F_2 and its compatible mod4 lifts are retained precisely because those necessary levels do not supply a characteristic-zero solution.
This result does not establish the full canonical-Haar obstruction for all degrees or complete the original Task.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:29 |
| status | open |
| reason | Register the complete actual C5 composition graph and unique formal degree27 boundary, the full divided-quotient mod4 compatibility classification and higher-adic Hensel obstruction, and their global canonical degree28/even-coefficient Haar consequence. Prior physical versions and adopted R473 scope remain unchanged. Whole noncontributor review of this substantive strengthening is required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual canonical theorem](#statement) | Every original full residual input, nonzero and zero reductions, degree drop, all-measure degree28 and2log2 conclusions, formal graph equality model and every compatible mod4 lift. |
| argument | [Complete assembled proof](#argument) | Entire CG1--CG13 and DQ1--DQ13 with the final original canonical combination; no mutable draft is a logical premise. |
| dependency | [Actual trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same original P/T/K/F, three nonzero integral quotients and monic divisibility. |
| dependency | [Exact full residual valuations](Yin_C_G0178_v1.md#statement) | All2-prime identities and unramified exclusion under both residual equations only. |
| dependency | [Complete local factor and cluster proof](Yin_C_G0191_v2.md#argument) | Actual exponent sum, every repeated factor and per-cluster positive income; no full-residue-degree or maximal-order simplification. |
| dependency | [Adopted multiplicity predecessor](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | Exact general integer-representative saturation facts and prior scope; its adopted proof remains fixed and separate from the new C5 graph/compatibility theorem. |
| dependency | [Complete-field simple-root lifting](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Exact source unit, complete finite extension L of Q_2, scaled integral polynomial and nonzero simple residue root. |
| dependency | [Scalar Jensen and zero convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact unit's height-normalization subsection for nonzero integer H_1, all circle zeros and the unchanged scalar2. |
| support | [Whole independent upstream C191](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Accepted cluster proof with this version's authorship overlap disclosed; no self-review substituted. |
| support | [Whole independent predecessor finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Actual complete C196v2 review, not an advance review of this substantive v3. |
| support | [Preserved earlier valuation mechanism](Yin_C_G0196_v2.md#retained-squarefree-valuation-argument) | Complete SF1--SF13, periodic unramified-lift lemma and cubic comparison remain physically fixed with their precise vacuous-conditional boundary. |
| support | [Complete current input boundaries](#exact-inputs) | Seven input rows, three contributors, fixed prior scope, finite-field versus characteristic-zero distinction and no computation or unrestricted gap. |

### Decision whole-reviewed-2026-10-20

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T13:51 |
| status | proved |
| authority | Internal adoption within Yin's selected actual residual and original-transfer inquiries. |
| reason | Adopt the complete C5 graph, divided-quotient lift and higher-adic obstruction through whole R474. A nonzero canonical reduction has degree at least28; integer canonical degree at most27 forces every coefficient even and the full Haar logarithm at least2log2, at every original measure. Preserve all formal finite-field and mod4-coefficient lift models at their precise weaker scopes, every actual original quotient and source boundary, and the prior versions/reviews. No larger-degree or unrestricted transfer conclusion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual canonical theorem](#statement) | Every original full residual input, nonzero and zero reductions, degree drop, all-measure degree28 and2log2 conclusions, formal graph equality model and every compatible mod4 lift. |
| argument | [Complete assembled proof](#argument) | Entire CG1--CG13 and DQ1--DQ13 with the final original canonical combination; no mutable draft is a logical premise. |
| dependency | [Actual trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Same original P/T/K/F, three nonzero integral quotients and monic divisibility. |
| dependency | [Exact full residual valuations](Yin_C_G0178_v1.md#statement) | All2-prime identities and unramified exclusion under both residual equations only. |
| dependency | [Complete local factor and cluster proof](Yin_C_G0191_v2.md#argument) | Actual exponent sum, every repeated factor and per-cluster positive income; no full-residue-degree or maximal-order simplification. |
| dependency | [Adopted multiplicity predecessor](Yin_C_G0196_v2.md#dyadic-multiplicity-exact-shape) | Exact general integer-representative saturation facts and prior scope; its adopted proof remains fixed and separate from the new C5 graph/compatibility theorem. |
| dependency | [Complete-field simple-root lifting](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Exact source unit, complete finite extension L of Q_2, scaled integral polynomial and nonzero simple residue root. |
| dependency | [Scalar Jensen and zero convention](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Exact unit's height-normalization subsection for nonzero integer H_1, all circle zeros and the unchanged scalar2. |
| support | [Whole independent upstream C191](../audits/reviews/Yin_R_G0468_v1.md#actual-trace-cluster-and-return-whole-finding) | Accepted cluster proof with this version's authorship overlap disclosed; no self-review substituted. |
| support | [Whole independent predecessor finding](../audits/reviews/Yin_R_G0473_v1.md#residual-dyadic-multiplicity-whole-finding) | Actual complete C196v2 review, not an advance review of this substantive v3. |
| support | [Preserved earlier valuation mechanism](Yin_C_G0196_v2.md#retained-squarefree-valuation-argument) | Complete SF1--SF13, periodic unramified-lift lemma and cubic comparison remain physically fixed with their precise vacuous-conditional boundary. |
| support | [Complete current input boundaries](#exact-inputs) | Seven input rows, three contributors, fixed prior scope, finite-field versus characteristic-zero distinction and no computation or unrestricted gap. |
| review | [Whole independent canonical-degree28 finding](../audits/reviews/Yin_R_G0474_v1.md#canonical-degree28-whole-finding) | Entire actual CR1--CR3, CG1--CG13 and DQ1--DQ13, all inputs, complete degree-drop and all-coefficient scope, every formal lift, actual same-T Hensel root and quotient value, and exact all-measure Haar normalization; prior author overlap is disclosed and independently covered upstream evidence reused. |

