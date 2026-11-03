---
author: Yin
---
# Exact small complement in the normalized actual cyclotomic unit gate

Date: 2026-10-20T17:20.
Human author Yin.
This substantive v5 retains the complete [adopted physical v4 theorem](Yin_C_G0199_v4.md#statement), including the preceding physical v3 conclusions at their separate domains, and adds the complete A_0=2 complement classification below.
Root and draft_inventory_later are the new mathematical authors.
The actual new proof date, author roles and elementary reuse boundary are retained with QC1--QC16.
The predecessor's complete UR13--UR23 proof and its R489 whole-chain adoption remain fixed; no earlier physical file or historical decision is rewritten.
This version requires a new whole independent review of its actual statement, complete new argument and full use of the adopted predecessor.
No original-input construction, scan, higher-modulus iteration or new source acquisition was performed.

<a id="statement"></a>
## Complete theorem statement and exact additional domains

### Common original residual domain

Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree d=2r.
For a root alpha set K=Q(alpha), delta=alpha+alpha^(-1), and assume its actual trace field F=Q(delta) is totally real.
Let T in Z[X] be its actual monic degree-r minimal polynomial, so P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    a,b,c nonzero,
    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0, s in{1,-1},
    g=c^3-2b^5!=0.

Set G=rem_T(theta_5^3-2theta_3^5), w=deg G<r, U=T mod2, R=G mod2, Phi=X^2+X+1 in Z[X] and phi=Phi mod2.
Let I_can be the normalized circle Haar integral of log(G(z+z^(-1))^2), using the integrable logarithm at circle zeros.
The common domain by itself assumes neither I_can=0 nor a unique unsaturated factor.
All [v3 statement Parts A--F](Yin_C_G0199_v3.md#statement) remain part of this version at their exact original domains: in particular UP needs unique unsaturation but no zero-Haar hypothesis, whereas the actual unit gate uses zero Haar and an unsaturated phi without requiring uniqueness.
The following normalized conclusions use BOTH additional hypotheses:

    I_can=0,
    ord_phi R<ord_phi U,
    ord_psi R>=ord_psi U
                    for every irreducible psi|U, psi!=phi.

The zero R, whose factor orders are infinite, cannot satisfy these conditions.
No bound on degree or Mahler measure is imposed.

### A. Maximal common Frobenius power and actual normalized units

The complete inherited factorization and exponent are

    U=X^A phi^(7A) product_i Q_i^(B_i),
    A>=2, B_i>=2, ord_phi R=6A,

where the Q_i are ALL distinct remaining monic irreducibles, different from X and phi.
Put

    k=min{v_2(A), v_2(B_i) for all i}, q=2^k,
    A_0=A/q, B_i0=B_i/q,
    H_0=X^(A_0) product_i Q_i^(B_i0),
    U_0=H_0 phi^(7A_0),
    R_0=rem_(U_0)(U_0(chi)^3), chi=X phi^2.

For an empty product take k=v_2(A); that case is excluded by the inherited odd-support theorem under the actual hypotheses.
Here q is an integer Frobenius power, not the value Phi(x) denoted q in the v3 selected-root proof.
Then A_0 is even and at least2, U=U_0^q, R=R_0^q!=0, and q is the maximal common Frobenius power of each polynomial.
In particular R_0 is not a square and deg R_0<deg U_0.

In O_loc=F_2[X]_(phi), define

    Psi=phi(chi), J_0=product_i Q_i(chi)^(B_i0),
    C_00=X^(A_0)J_0 Psi^(7A_0),
    V_0=R_0/phi^(6A_0), D_0=V_0+C_00^3.

Their original counterparts are H=H_0^q, C_0=C_00^q and V=V_0^q, with D=D_0^q and D_0 in phi^(A_0) O_loc.
All are reductions of the same original input; no normalized characteristic-zero realization is asserted.

### B. Exact original-layer gate after normalization

The zero-Haar factorization retains every original integer cyclotomic multiplicity.
For m>=3 write Phi_m(z)=z^(phi(m)/2)F_m(z+z^(-1)), where phi(m) is Euler's totient, and factor the SAME G as

    G=V_int product_(b>=0) F_(2^b*5)^(a_b),
    V=V_int mod2,
    lambda_0=lambda_1=1,
    lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=6qA_0.

The factor V_int includes the sign and all other odd-order factors, including the m=1,2 endpoint factors whose cyclotomic multiplicities are even.
Each occurring lambda_b is strictly below6qA_0.
With these original integers a_b and original indices, put

    S_star=sum_(a_b odd, lambda_b>2qA_0)
          X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                       phi^(6A_0-lambda_b/q),
    L_star=sum_(a_b odd, lambda_b>2qA_0)
          X^(lambda_b/(4q))(X+1)^(lambda_b/(2q))
                       phi^(3A_0-lambda_b/(2q)).

All displayed exponents are nonnegative integers, S_star=L_star^2, and empty sums are allowed.
These formulas do not require q to divide a_b and do not assign freely relabeled normalized cyclotomic multiplicities.
Let Z_0 be the unique unit class satisfying

    Z_0^11=H_0 C_00^2 modulo phi^(3A_0).

The original full UJ gate is EXACTLY equivalent to

    Z_0D_0+H_0V_0S_star=0 modulo phi^(4A_0).

This condition is necessary, not sufficient for the characteristic-zero original residual system.
Any lift of Z_0 gives the same condition.
The old support relation also descends exactly to

    H_0^6/C_00^21=1 modulo phi^(4A_0).

Under that old relation, the normalized gate is equivalent to the conjunction

    S_star in phi^(A_0) O_loc,
    V_0=[Z_0^3/(1+(Z_0^5/C_00)L_star)]^2
                                      modulo phi^(4A_0).

The denominator is a unit, and the3A_0 root precision is used at4A_0 only after the additional A_0 divisibility has been paid.

### C. Nontrivial actual odd part and complete low-degree complement

The normalized gate implies ord_phi V_0'>=4A_0.
Write uniquely V_0=J_G0^2 W_G0 with W_G0 monic and squarefree.
Then

    W_G0 is nonconstant,
    ord_phi W_G0'>=4A_0,
    deg W_G0>=8A_0+1.

For every odd order n!=5, each complete order group Omega_n occurs in W_G0 precisely when the common integer nu_n/q is odd; X occurs precisely when nu_1/q is odd.
The divisibility q|nu_n follows from R=R_0^q, not from divisibility of the individual original integers a_b.
The nonsquare conclusion concerns V_0; the original V may already be a square when q>1.

There is also a unique monic polynomial B such that

    R_0=H_0 phi^(6A_0)B,
    V_0=H_0B, phi not dividing B,
    0<=deg B<2A_0.

This B includes EVERY surplus multiplicity at saturated factors and every extra factor of R_0, with reduction degree drop allowed.
Consequently ord_phi(H_0B)'>=4A_0 and H_0B is not a square.
These assertions give no upper bound on deg H_0 and do not identify W_G0 with the T-support odd part W_U.
The large W_G0 degree is not a proved lower bound on deg B or an automatic payment of the unique phi deficit.
No overall exclusion, actual realization, smaller original field, new all-degree Haar transfer or stronger Mahler gap is asserted.

### D. Exact complement when the normalized multiplicity is two

Add only A_0=2 to the complete hypotheses of Parts A--C, allowing every original q=2^k and hence original A=2q.
Write H_0=X^2Y with Y=product_i Q_i^(B_i0), retaining all remaining factors and their entire normalized multiplicities.
Then the UNIQUE complete complement from Part C is B=X^3, and

    Y=1+X^2 modulo X^4,
    U_0=X^2 phi^14 Y,
    R_0=X^5 phi^12 Y,
    V_0=X^5Y,
    W_G0=X W_U,
    w=r-q, 2w=d-2q.

Every reduced factor other than X and phi has exactly the same multiplicity in U_0 and R_0, and Y consists of complete odd-order groups Omega_n for n other than1 and5.
The original cyclotomic factorization satisfies sum_m a_m phi(m)=d-2q, where phi(m) is Euler's totient; the original resultant and norm expense in QC16 is unchanged.
No divisibility q|a_m is asserted for individual integer cyclotomic exponents.
This determines necessary data on this subclass only; the full normalized depth-eight gate, complete original residual equations and unbounded degree of Y remain.
In particular this is neither a contradiction nor an original-input existence theorem, and it supplies no unrestricted original-root/Haar estimate.

<a id="argument"></a>
## Complete argument and exact predecessor reuse

Parts A--C and all inherited conclusions use the [entire fixed v4 proof](Yin_C_G0199_v4.md#argument), with every original assumption, separate v3 domain and scalar cost retained as explicitly stated above.
Its actual whole-chain evidence is [R489 for v4](../audits/reviews/Yin_R_G0489_v1.md#normalized-unit-v4-whole-chain-finding), including [R489's separate v3 finding](../audits/reviews/Yin_R_G0489_v1.md#cyclotomic-unit-v3-whole-chain-finding).
Those findings do not review the new Part D proof that follows.

<a id="normalized-a2-exact-complement"></a>
## Complete new normalized A_0=2 proof

Date: 2026-10-20T17:17.
Human author Yin.
Root supplied the complete proposed specialization, precision chain, finite local calculation and resulting multiplicity bridge.
The draft_inventory_later agent checked and completed the explicit local-ring identification, the exhaustion of the small complement, every truncation and the original-degree and factor bookkeeping below.
Both are mathematical contributors; this is new author work, not an independent review of C199 or a consequence already included in R489.
The substantive new question is to determine the actual small complement on the normalized A_0=2 class, not to improve a finite canonical-degree cutoff.
The reuse check read the adopted C199v4 full gate and complement, the C197v3 common-Frobenius odd-part theorem and the existing L441 comparison; none supplied the exact complement conclusion below.
No mathematical program, order search, coefficient enumeration or new source acquisition is used.

### Complete actual-input hypotheses and normalized objects

Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree d=2r.
For an original root alpha let delta=alpha+alpha^(-1), K=Q(alpha), and let the actual trace field F=Q(delta) be totally real.
Let T in Z[X] be its monic degree-r minimal polynomial, with P(z)=z^r T(z+z^(-1)) and [K:F]=2.
Use the integer polynomials C_p defined by C_p(z+z^(-1))=z^p+z^(-p).
Use the actual integral trace quotients and exact full residual system

    theta_p=rem_T(T(C_p))/p in Z[X], p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta),
    a,b,c nonzero,
    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0, s in{1,-1},
    g=c^3-2b^5!=0.                              (QC1)

Put G=rem_T(theta_5^3-2theta_3^5), U=T mod2, R=G mod2 and phi=X^2+X+1 in F_2[X].
Let I_can be the integral of log G(z+z^(-1))^2 against normalized circle Haar probability, with the integrable logarithm at circle zeros.
Assume I_can=0 and assume phi is the ONLY unsaturated irreducible factor:

    ord_phi R<ord_phi U,
    ord_psi R>=ord_psi U
                       for every psi|U, psi!=phi. (QC2)

These are the complete additional hypotheses of [adopted C199v4](Yin_C_G0199_v4.md#statement).
Use its maximal common Frobenius power q=2^k and restrict only the NORMALIZED multiplicity to A_0=2.
Thus the original multiplicity is A=2q, which need not be2.
Its exact normalized polynomials and complement have the form

    Y=product_i Q_i^(B_i0), H_0=X^2Y,
    U_0=X^2 phi^14 Y, U=U_0^q,
    R=R_0^q, R_0=H_0 phi^12 B,
    B monic, 0<=deg B<4, phi not dividing B.     (QC3)

Here the Q_i are ALL distinct remaining irreducibles, different from X and phi, and Y retains their full normalized positive integer multiplicities B_i0.
The polynomial Y is monic and coprime to X phi, and Y(0)=1.
There is no freely chosen characteristic-zero polynomial realizing U_0 or R_0.
The identities (QC3), including the nonsquare R_0 and complete complement expense, are the [fixed UR14--UR23 statements](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate), used through their actual [whole R489 finding](../audits/reviews/Yin_R_G0489_v1.md#normalized-unit-v4-whole-chain-finding).

### The old support condition fixes the first odd coefficients of Y

Let W_U be the squarefree product of those Q_i for which B_i0 is odd.
The [C197v3 QX20 input](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative), in exactly this maximal normalization, gives

    W_U nonconstant, W_U(0)=1,
    ord_X W_U'>=4.                              (QC4)

Write Y=J_Y^2 W_U in F_2[X].
All three polynomials have constant coefficient1, and differentiation in characteristic two gives Y'/Y=W_U'/W_U.
Since the denominators are units at X=0, (QC4) implies X^4 divides Y'.
Writing y_j for the coefficient of X^j in Y, this proves

    y_0=1, y_1=y_3=0,
    Y=1+y_2 X^2 modulo X^4, y_2 in F_2.         (QC5)

No restriction on all the later coefficients or on deg Y is inferred here.
This use preserves W_U as the odd part of the ACTUAL normalized T support.

### The original layer window first forces a depth-four identity

Keep the original nonnegative cyclotomic multiplicities a_b of the trace factors of orders2^b*5, and lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2.
They satisfy sum_b a_b lambda_b=12q.
The [normalized correction UR17](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) uses only original odd multiplicities with4q<lambda_b<12q.
The ratio lambda_b/q is a power of2 strictly between4 and12, so it must be8.
This is a consequence of the fixed layer window, not an enumeration of possible orders or an assumption that q divides a_b.
There is just one such index b=k+4, and hence

    S_star=epsilon X^4(X+1)^8 phi^4,
    epsilon=a_(k+4) mod2 in{0,1}.               (QC6)

In particular S_star is divisible by phi^4, including epsilon=0.
Both small layers b=0,1 lie outside this window.

Work now in the characteristic-two local ring F_2[X]_(phi) and put

    chi=X phi^2, Psi=phi(chi),
    C_00=X^2 Y(chi) Psi^14,
    V_0=H_0 B, D_0=V_0+C_00^3.

All H_0,C_00,V_0,B are units there.
The complete C199v4 gate has Z_0D_0+H_0V_0S_star=0 modulo phi^8, with Z_0 a unit.
Reducing this gate modulo phi^4 using (QC6) gives the necessary relation

    H_0 B=C_00^3 modulo phi^4.                  (QC7)

Only this projection of the full gate is used at this step; the correction at exact order4 is not discarded from the still-required depth-eight condition.

The normalized OLD support condition is H_0^6=C_00^21 modulo phi^8.
In characteristic two, the sixth-power difference has only error powers2,4,6:

    (A+E)^6=A^6+A^4E^2+A^2E^4+E^6.

Thus raising (QC7) to the sixth power raises its error order from4 to at least8.
Combining the resulting H_0^6 B^6=C_00^18 modulo phi^8 with the old support identity, then dividing by the unit C_00^18, gives

    B^6 C_00^3=1 modulo phi^8.                  (QC8)

No depth-eight assertion has been inferred directly from a depth-four first-power approximation.

### The remaining cube condition has only three small representatives

Since chi has phi-order2, (QC5) yields

    Y(chi)=1+y_2 X^2 phi^4
           =(1+y_2 X phi^2)^2 modulo phi^8.

The omitted X^j terms with j>=4 have phi-order at least8 after composition.
Using the definition of C_00 in (QC8), define

    W=B X Psi^7(1+y_2 X phi^2).

Then (QC8) is equivalent to W^6=1 modulo phi^8.
For a polynomial or local fraction, the phi-order of a square is twice its phi-order, including infinity.
Since W^6-1=(W^3-1)^2 in characteristic two, the precise resulting condition is

    W^3=1 modulo phi^4.                         (QC9)

This uses the order of an actual local-ring expression rather than cancellation of a Frobenius power inside a nonreduced quotient.

For a self-contained description of this small quotient, let beta in F_4 satisfy beta^2+beta+1=0 and put p=phi.
There is an explicit isomorphism

    F_2[X]/(phi^4) = F_4[p]/(p^4),
    X=beta+p+p^2.                              (QC10)

Indeed substituting the displayed X gives X^2+X+1=p modulo p^4.
Conversely the image contains p=phi(X) and beta=X+p+p^2, so it contains both generators of the right side.
Both rings have dimension8 over F_2, proving the isomorphism without an additional lifting theorem.

The units whose cube is1 in this ring are exactly the three nonzero CONSTANTS1,beta,beta^2.
To see this, write a unit as c(1+u) with c in F_4^* and u in pF_4[p]/(p^4).
Then c^3=1, while (1+u)^3-1=u+u^2+u^3.
If u is nonzero, its least p-order is between1 and3, and that leading term cannot cancel against the higher orders in u^2 or u^3.
Thus the cube condition is equivalent to u=0.

The factor Psi^7(1+y_2 Xp^2) is1 modulo p^2.
Equation (QC9) consequently requires BX to be one of1,beta,beta^2 modulo p^2.
Multiplication by X is invertible in F_2[X]/(phi^2), and each class has a unique representative B of degree below4.
Those three forced representatives are precisely

    BX=1 modulo p^2:       B=X^3+X;
    BX=beta modulo p^2:    B=X^3;
    BX=beta^2 modulo p^2:  B=X.                (QC11)

For verification, X^4=beta modulo p^4 and X^2=beta^2+p^2, so the respective products BX are1+p^2,beta,beta^2+p^2.
They have the stated constant residues modulo p^2, and uniqueness proves that no other degree-below4 polynomial can meet the necessary condition.
This exhausts the possibilities by the residue equation and monic remainder uniqueness, without scanning coefficient choices.

Set c_*=1+y_2 in F_2.
Because Psi=1+Xp^2+X^2p^4, the complete remaining multiplier has expansion

    Psi^7(1+y_2 Xp^2)
      =1+c_* beta p^2+c_* p^3 modulo p^4.

Multiplying this by the three EXACT products in (QC11) gives

    B=X^3+X: W=1+(1+c_* beta)p^2+c_* p^3;
    B=X^3:   W=beta+c_* beta^2 p^2+c_* beta p^3;
    B=X:     W=beta^2+(1+c_*)p^2+c_* beta^2 p^3
                                                   modulo p^4. (QC12)

In every line the p^3 coefficient forces c_*=0 if W is a constant.
With c_*=0 the first and third lines still have a nonzero p^2 term, whereas the middle line is the constant beta.
The necessary cube condition therefore forces exactly

    B=X^3, y_2=1,
    Y=1+X^2 modulo X^4.                        (QC13)

The calculation works at either conjugate choice of beta and specifies the same polynomials over F_2.
It determines the complement as a necessary consequence; it does not show that the full depth-eight gate or the characteristic-zero residual equations hold for arbitrary Y with (QC13).

<a id="normalized-a2-odd-part-and-degree-return"></a>
### Exact support bridge and the paid original degree

Substituting (QC13) in the ACTUAL normalized remainder identity gives

    U_0=X^2 phi^14 Y,
    R_0=X^5 phi^12 Y,
    V_0=X^5Y,
    Y=1+X^2 modulo X^4.                        (QC14)

At X the normalized multiplicity changes from2 to5, and at phi it changes from14 to12.
Every other irreducible factor has EXACTLY the same multiplicity in U_0 and R_0.
There are no extra remainder factors outside the original support.
These are identities of the complete characteristic-two reductions, not equalities between the integer factors of T and G.

Every odd-order trace group in R has the full uniform multiplicity from the [adopted C199v2 factor theorem](Yin_C_G0199_v2.md#statement), and C199v4 proves the exact divisibility of those multiplicities by q.
Consequently Y consists of complete Omega_n groups for n other than1 and5, with their full normalized multiplicities; no proper selected subset of an order group is introduced.
The exceptional groups are exactly X for n=1 and phi for n=5.
Their original multiplicities are respectively2q versus5q, and14q versus12q, in U and R.

Writing again Y=J_Y^2 W_U, the exact normalized G-unit factorization is

    V_0=(X^2 J_Y)^2 (X W_U),
    W_G0=X W_U.                                (QC15)

The product X W_U is squarefree because X does not divide Y.
Thus the two previously distinct odd-part polynomials acquire this precise relationship ONLY on the present A_0=2 class.
The conclusion does not identify W_G0 and W_U outright and does not extend the relationship to other normalized multiplicities.
Their inherited derivative and size restrictions still concern the full polynomial XW_U, not just the degree-three complement.

Subtracting the complete degrees in (QC14) yields

    deg R_0=deg U_0-1,
    deg R=r-q.

Zero canonical Haar gives lc(G)=+/-1, so reduction modulo2 has no leading-degree drop and w=deg G=deg R.
The exact original return is therefore

    w=r-q,
    2w=d-2q,
    sum_m a_m phi(m)=d-2q,
    sum_m a_m log|Res(P,Phi_m)|
                 =2log|Norm_F(g)| >=(6d/11)log2. (QC16)

In (QC16), phi(m) is Euler's totient and a_m are the original complete integer cyclotomic multiplicities indexed by m.
The notation a_b in (QC6) abbreviates the original exponent a_(2^b*5); neither notation divides those integers by q.
Every original resultant and all original K/F degrees retain the already proved C199 expenses.
No individual divisibility q|a_m, smaller original input, rescaled Mahler measure or new norm income follows from the characteristic-two normalization.

### Scope after this exact complement determination

This completes the bounded A_0=2 complement calculation under the full actual-input, zero-Haar and unique-unsaturated hypotheses.
The full depth-eight gate still retains epsilon in (QC6), all later coefficients of Y and the corresponding uniquely determined root Z_0.
Conditions (QC13)--(QC16) are necessary, not sufficient for that full gate or an original residual realization.
The degree of Y remains unbounded, and the large odd-part degree cannot be charged solely to B=X^3.
No contradiction, input construction, general A_0 classification, new degree cutoff or unrestricted original-root/Haar comparison is asserted.
The sole mathematical inputs beyond the displayed elementary calculations are the exact C197 odd-support theorem and the adopted C199v2/v3/v4 statements identified above, with their original source and independent-review boundaries.
Root and draft_inventory_later have contributor-overlapping earlier work in that chain; its actual R477/R489 evidence is reused rather than described as an independent self-review.
R477, both R489 findings and the current R492 finding now declare unknown initial context at their exact unchanged scopes, without altering the original mathematical findings or adoption dates.
This new QC1--QC16 author argument is fixed here and awaits a separately arranged noncontributor review; registration does not adopt it.

<a id="exact-inputs"></a>
## Exact inputs and review obligations

The complete new proof uses the adopted v4 normalized gate and full complement, the exact C197v3 odd-support input and the complete cyclotomic multiplicities already contained in the predecessor chain.
Its polynomial expansions, local-ring identification, cube-root argument and small-complement exhaustion are proved in full above without a new external theorem.
Root and draft_inventory_later contributed to earlier C199 material, and draft_inventory_later authored R637 for the distinct C202 theorem; neither fact is independent review of this version.
The separate reviewer must cover the entire present statement and argument, all selected inputs, original q and layer parity, every precision change, complete complement exhaustion, support bridge and original norm/degree return.
No past adoption is silently extended to QC1--QC16.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-21)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T17:20 |
| status | open |
| reason | Retain the complete adopted v4 statement at its distinct domains and the new QC1--QC16 actual A_0=2 classification: unique B=X^3, low Y coefficients, exact reduced multiplicities, W_G0=XW_U and original w=r-q. Every original q, integer layer and norm cost remains; no full-gate feasibility, impossibility or uniform transfer is claimed. Await a new complete independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire retained and extended theorem](#statement) | Common actual original residual domain, all inherited v3/v4 domains and Parts A--C, plus Part D only with A_0=2 and arbitrary original q, complete group/degree/norm bookkeeping and unresolved feasibility. |
| argument | [Complete current proof](#argument) | Exact adopted predecessor reuse and full QC1--QC16, actual original quotients, odd-support coefficients, original layer window, both precisions, explicit quotient ring, complete cube/complement exhaustion and original return. |
| dependency | [Complete adopted v4 proof](Yin_C_G0199_v4.md#argument) | All retained theorem domains, UR13--UR23, exact whole v3 chain, maximal q and nonsquare R_0, full actual normalized gate and complete low-degree complement; no freely chosen local units. |
| dependency | [Actual normalized T odd support](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | QX20 under the same maximal normalization: nonconstant W_U and ord_X W_U prime >=2A_0, used at A_0=2 with exact full normalized multiplicities. |
| support | [Complete cyclotomic order theorem](Yin_C_G0199_v2.md#statement) | Uniform complete Omega_n multiplicities and original product/resultant expense retained through the adopted v4 chain; no independent original input from a reduction. |
| support | [Actual v4 whole-chain evidence](../audits/reviews/Yin_R_G0489_v1.md#normalized-unit-v4-whole-chain-finding) | Exact independent coverage of the entire adopted predecessor and its actual dependency chain, preserving contributor overlaps and source-proof limits; not prospective QC coverage. |
| support | [Actual v3 whole evidence](../audits/reviews/Yin_R_G0489_v1.md#cyclotomic-unit-v3-whole-chain-finding) | Whole inherited v3 domains, UJ/UR/UP and earlier full inputs, including author-overlapping earlier work. |
| support | [Actual generalized odd-support evidence](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Exact adopted C197v3 QX20 and maximal-normalization scope; preserved earlier authorship, not self-review or coverage of the new calculation. |

### Decision whole-reviewed-2026-10-21

| Field | Value |
| --- | --- |
| date | 2026-10-20T17:25 |
| status | proved |
| authority | Internal adoption within Yin's selected retained-draft inquiries. |
| reason | Adopt the entire inherited theorem and new QC1--QC16 through the actual complete noncontributor R492 finding. On normalized A_0=2 only, with arbitrary original q, the exact complement is X^3, Y=1+X^2 modX^4, complete reduced multiplicities coincide off X/phi, W_G0=XW_U and w=r-q. Preserve the full old gate, all integer layers and original norm expenses; no global contradiction, characteristic-zero realization or unrestricted transfer is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire retained and extended theorem](#statement) | Common actual original residual domain, all inherited v3/v4 domains and Parts A--C, plus Part D only with A_0=2 and arbitrary original q, complete group/degree/norm bookkeeping and unresolved feasibility. |
| argument | [Complete current proof](#argument) | Exact adopted predecessor reuse and full QC1--QC16, actual original quotients, odd-support coefficients, original layer window, both precisions, explicit quotient ring, complete cube/complement exhaustion and original return. |
| dependency | [Complete adopted v4 proof](Yin_C_G0199_v4.md#argument) | All retained theorem domains, UR13--UR23, exact whole v3 chain, maximal q and nonsquare R_0, full actual normalized gate and complete low-degree complement; no freely chosen local units. |
| dependency | [Actual normalized T odd support](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | QX20 under the same maximal normalization: nonconstant W_U and ord_X W_U prime >=2A_0, used at A_0=2 with exact full normalized multiplicities. |
| support | [Complete cyclotomic order theorem](Yin_C_G0199_v2.md#statement) | Uniform complete Omega_n multiplicities and original product/resultant expense retained through the adopted v4 chain; no independent original input from a reduction. |
| support | [Actual v4 whole-chain evidence](../audits/reviews/Yin_R_G0489_v1.md#normalized-unit-v4-whole-chain-finding) | Exact independent coverage of the entire adopted predecessor and its actual dependency chain, preserving contributor overlaps and source-proof limits; not prospective QC coverage. |
| support | [Actual v3 whole evidence](../audits/reviews/Yin_R_G0489_v1.md#cyclotomic-unit-v3-whole-chain-finding) | Whole inherited v3 domains, UJ/UR/UP and earlier full inputs, including author-overlapping earlier work. |
| support | [Actual generalized odd-support evidence](../audits/reviews/Yin_R_G0477_v1.md#quadratic-primary-generalized-consumer-whole-finding) | Exact adopted C197v3 QX20 and maximal-normalization scope; preserved earlier authorship, not self-review or coverage of the new calculation. |
| review | [Whole exact-complement finding](../audits/reviews/Yin_R_G0492_v1.md#normalized-a2-complement-whole-finding) | Entire actual statement and argument, two dependencies/four supports, all original and normalized domains, every QC1--QC16 precision and exhaustive local step, complete support/odd-part identification, original degree/norm return and unresolved feasibility; no reviewer contribution or proof repair. |

