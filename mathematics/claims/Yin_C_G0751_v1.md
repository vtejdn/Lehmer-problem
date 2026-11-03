---
author: Yin
---

# Whole-row residue classes and paid invisible complete-source extensions

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the low reciprocal row calculation and the invisible squared-row comparison.
The characteristic_zero_bridge agent checked the actual ordinary/divided row domains and exponent convention, derived the small invisible ordinary row and its admissibility-preserving powers, and verified every full-source, canonical, fresh-factor, degree, gap and synthetic-layer consequence.
Root read the entire saved WR1--WR11 argument.
Both agents are substantive contributors; this open fixed candidate awaits fresh isolated whole review and separate adoption.
No native computation, exponent-vector evaluation, coefficient search or source-rank calculation is used.
The separate endpoint affine investigation and true-certificate inquiry in D43 are not parts of this Claim.

## Statement

Work over F_2 with phi=X^2+X+1, chi=Xphi^2 and Psi=phi(chi).
B_n is the COMPLETE trace polynomial of all nonidentity n-th roots for positive odd n, with B_1=1; W_n is its complete primitive-order version.
Write S_n(z)=1+z+...+z^(n-1).
For a monic binary trace polynomial f set P_f(z)=z^(degf)f(z+z^(-1)), its full reciprocal transform.
All polynomial-product exponents and degree costs below are ordinary nonnegative integers; powers of units in F_2[z]/z^4 may have negative integer exponents.

### A. Actual complete starting source and the conditional endpoint class

Start with an ACTUAL bounded representative from the [C691 DG1--DG8 and Section3/5 construction](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24).
Retain

    Q=2^ell, ell>=82, m_src=Q/4-2, N=8m_src,
    L=4Q, e_pad=12Q,
    Y=Y_pre B_(n_star)^3.

Y_pre is the actual product of C664/C667's chosen ordinary B_n rows with gcd(n,15)=1 and divided D_(5ell_row)=B_(5ell_row)/phi rows with gcd(ell_row,15)=1, after their multiplicity-floor adjustment.
Trivial B_1 and D_5 rows are allowed.
Retain its original fresh index n_star>K_bound>=30L, with n_star=1 modulo10L and gcd(n_star,15)=1, and its selected irreducible psi_star of exact multiplicity3 outside the COMPLETE original B source polynomial.
Every original source factor, multiplicity and finite class remains part of the input.

Use the exact original C691 auxiliary H_aux and

    B_src=X^(Q-m_src)H_aux(chi),
    H_0=X^(2m_src)Y,
    U_0=H_0phi^(14m_src), R_0=H_0phi^(12m_src)B_src,
    d=degU_0, Dbar=P_(U_0)/(z^2+1),
    delta_i=[z^i]Dbar in{0,1}.

The original full degree gap is m_src-8-5degH_aux>5m_src/256.
Let E_pre be the sum of the exponents of the NONTRIVIAL ORDINARY rows in Y_pre, EXCLUDING B_1, all divided rows and the final fresh cubic.
Let E_all=E_pre+3 if the fresh ordinary exponent is included.
Then

    Dbar=(1+z)^(-E_pre-1)
         =(1+z)^(2-E_all) modulo z^4,
    delta_3=delta_1 delta_2.

At the algebraic endpoint a=d-3, CONDITIONAL on gcd(2d-5,15)=1, C747's exact local mask dimension is:

| E_pre modulo4 | (delta_1,delta_2,delta_3) | e |
| --- | --- | --- |
| 0 | (1,1,1) | 2 |
| 1 | (0,1,0) | 0 |
| 2 | (1,0,0) | 0 |
| 3 | (0,0,0) | 0 |

Thus e=2 if and only if E_pre=0 modulo4, equivalently E_all=3 modulo4; otherwise e=0.
The ordinary count e=delta_0delta_3+delta_1delta_2 is not addition in F_2.
The result applies to the retained actual row construction, not to an arbitrary unchosen primitive-factor representation.
The actual original E_pre, d modulo15 and endpoint admissibility are NOT evaluated.
Changing a row presentation of the SAME polynomial cannot change E_pre modulo4 with this fresh-cubic convention.

### B. A small invisible row and complete source preservation

Define

    c_ext=1 if L=1 modulo3, c_ext=2 if L=2 modulo3,
    n_ext=1+10L c_ext,
    b_ext=degB_(n_ext)=5L c_ext<=40Q.

Then n_ext is odd, coprime15 and1 modulo10L, and

    B_(n_ext)=1 modulo X^N phi^(2N),
    n_ext<=20L+1<30L<n_star.

In particular the new complete row does not contain the original order-n_star factor psi_star.
For either finite exponent set

    R_class={0,2,3,5},
    R_adm={0,3,6,9},

and every rho in the chosen set, put

    M_rho=B_(n_ext)^rho,
    Y_rho=Y M_rho, U_rho=U_0 M_rho, R_rho=R_0 M_rho.

These are ACTUAL complete polynomial extensions.
All three polynomials remain monic and complete, while Y_rho remains prime to Xphi.
The extensions preserve BOTH full Y forward divisibilities, the full multiplicity floor2, the same exact triple psi_star in Y_rho and Y_rho B_src, and both original DG3 jets.
Every DG6 identity remains at its FULL precision phi^(16m_src), with the same beta and Z_0.
The full derivative X^(8m_src)|Y_rho' is retained.
Odd rho may change other odd-multiplicity parts; equality of all old odd parts is not claimed.

Their actual all-primary identities are

    R_rho=rem_(U_rho)(U_rho(chi)^3)!=0,
    U_rho|U_rho(X^3+X).

The only unsaturated primary remains phi, of orders14m_src/12m_src; all other complete primary multiplicities are retained and saturated.
For any monic integer trace T reducing to U_rho, its actual b(T)=rem_T T(C_3)/3 has bbar=0, and its actual G(T)=rem_T(c(T)^3-2b(T)^5), c(T)=rem_T T(C_5)/5, has Gbar=R_rho.
Here C_3=X^3-3X and C_5=X^5-5X^3+5X; all scalar divisions precede binary reduction.
No dyadic canonical quotient or passing integer residual input is constructed.

### C. All four classes, exact extra costs and optional admissibility preservation

For each extension

    E_pre,new=E_pre+rho,
    Dbar_new=Dbar S_(n_ext)^rho
             =(1+z)^(-E_pre-rho-1) modulo z^4.

Both exponent sets in Part B cover every residue modulo4.
R_class costs at most200Q extra trace degree but does not automatically preserve endpoint admissibility modulo3.
R_adm costs at most360Q extra trace degree and satisfies

    d_rho=d+rho b_ext=d modulo15.

Thus R_adm preserves gcd(2d_rho-5,15)=gcd(2d-5,15).
It preserves an ALREADY admissible endpoint and does not silently make an inadmissible one admissible.
If the original endpoint is admissible, exactly one of the four R_adm representatives has e=2 at its recomputed a=d_rho-3 endpoint and the other three have e=0.

The full exact degrees and gap are

    degY_rho=degY+rho b_ext,
    d_rho=degU_rho=d+rho b_ext,
    degR_rho=degR_0+rho b_ext,
    d_rho-degR_rho=m_src-8-5degH_aux>5m_src/256.

The NEW conservative degree bounds are:

| Extension set | degY_rho | d_rho |
| --- | --- | --- |
| R_class | <=14400Q^3+1206Q^2+320Q | <=14400Q^3+1206Q^2+328Q |
| R_adm | <=14400Q^3+1206Q^2+480Q | <=14400Q^3+1206Q^2+488Q |

These are enlarged bounds for extensions of the actual original bounded witness.
They are NOT an assertion that the new representatives remain within the original DG8 numerical bound.
The original source exponent class remains unevaluated even though the four paid representatives cover all its possibilities.

### D. Raised normalization, complete synthetic layer and the squared-row comparison

For every q=2^j the trace degrees and positive gap in Part C are multiplied by q, with FULL reciprocal degree2q d_rho.
The unchanged exact triple factor proves that U_rho^q, R_rho^q and the full reciprocal binary polynomial have actual maximal Frobenius power q.
The original layer vector a_0=12m_src q and a_b=0 for b>=1 is unchanged.
If F_e denotes C691/C667's monic INTEGER trace factor for complete odd order e, the full synthetic lift is multiplied by

    product_(e|n_ext,e>1)F_e^(rho q).

It has exactly rho q b_ext extra degree and retains zero normalized circle Haar logarithmic integral, counting every factor, multiplicity and integrable zero.
This synthetic integer polynomial is not identified with the actual integer canonical G(T).

For any nontrivial ordinary row B_n with n>=5, reciprocal multiplication by its square acts by

    delta_1,new=delta_1,
    delta_2,new=delta_2+1,
    delta_3,new=delta_3+delta_1.

In particular this describes C738's ACTUAL invisible squared multiplier at its own source-preservation and cost scope.
Its exponent class shifts E_pre by2 and cannot change E_pre parity.
It cannot alone move an odd class into the e=2 class0; the odd invisible powers in Part B give that additional paid class freedom.

These small extensions do not assert Lambda(U_rho)=0, height1 sign feasibility, a numerical endpoint affine rank, a full old-primary solution, original irreducibility, total-Mahler control or characteristic-zero residual identities.
C738's separate large-multiplier argument for Lambda=0 requires its own degree lower bound and is not imported here.
No unrestricted G0001 conclusion is supplied.

## Complete argument

<a id="whole-row-congruence-and-invisible-class-control"></a>
### Whole-row congruences and paid invisible control of the endpoint class

This is the complete fixed author argument by root and characteristic_zero_bridge, separate from the certificate inquiry.
Root proposed the low reciprocal whole-row calculation and the invisible squared-row comparison; characteristic_zero_bridge checked the exact row domains, separated the pre-fresh and total ordinary exponents, and derived the small invisible ordinary-row extensions with their full source costs.
The actual inputs read here are [C691 Sections3/5 and DG1--DG8](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), [C667 FC1--FC4](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24), [C664 G4--G5](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24), and [C738 PA8--PA12](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25).
The reciprocal complete-row identity is also the accepted [C608 complete Laurent identity](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23).
This calculation consumes no finite native rank or coefficient table from those sources.
It does not evaluate the exponent class of any unspecified chosen C691 witness.

#### Actual ordinary/divided rows and the precise exponent convention

Use the retained C691 whole-row construction at Q=2^ell, ell>=82, m_src=Q/4-2 and N=8m_src.
Its safe C664/C667 parameters are L=4Q and e_pad=12Q.
After the actual coprime-three row replacements and floor adjustment, Y_pre is a nonnegative product of

    ordinary B_n, n odd, gcd(n,15)=1,
    divided D_(5ell_row)=B_(5ell_row)/phi,
                  ell_row odd, gcd(ell_row,15)=1.

The ordinary B_1=1 and divided D_5=1 may occur as trivial rows.
Every NONTRIVIAL ordinary index is at least7: indices3 and5 are excluded by the actual coprimality conditions.
C664 supplies precisely these chosen finite rows after its full predivision-period argument; this is not a claim about an arbitrary primitive-factor product using unchosen higher-five rows.
The actual final source is

    Y=Y_pre B_(n_star)^3,
    n_star>K_bound>=30L,
    n_star=1 modulo10L, gcd(n_star,15)=1.       (WR1)

Retain the originally selected exact triple factor psi_star of W_(n_star), outside the complete B source polynomial.

Let E_pre be the ordinary INTEGER sum of the exponents of all NONTRIVIAL ORDINARY rows in Y_pre.
Do not count B_1, any divided row, or the final fresh factor in E_pre.
If E_all includes the final ordinary B_(n_star)^3, then E_all=E_pre+3.
Replacing a floor-violating exponent1 by e_pad+1 changes the corresponding ordinary total by e_pad=12Q=0 modulo4, so the floor adjustment does not change E_pre modulo4.
This does not specify which exponent vector was chosen by the finite existence theorem.

For any monic binary trace polynomial f define its actual reciprocal transform by P_f(z)=z^(degf)f(z+z^(-1)).
It is multiplicative and P_1=1.
The complete Laurent identity and exact divided-row polynomial give

    P_(B_n)=S_n(z)=(1+z^n)/(1+z),
    P_phi=S_5(z)=1+z+z^2+z^3+z^4,
    P_(D_(5ell_row))
       =S_(5ell_row)(z)/S_5(z)
       =(1+z^(5ell_row))/(1+z^5)
       =S_(ell_row)(z^5).                       (WR2)

The last expression is an EXACT polynomial, not division by phi in a nonunit ring or a selected-root quotient.
In the unit ring F_2[z]/z^4, every nontrivial ordinary row therefore contributes(1+z)^(-1), while every divided row contributes1.
The row B_1 instead contributes1 and cannot be assigned the ordinary nontrivial-row contribution.
Every fresh index in WR1 is nontrivial, so its cubed factor contributes(1+z)^(-3).

#### Low reciprocal coefficients and the endpoint dimension class

For the full original U_0=X^(2m_src)Yphi^(14m_src), let d=degU_0 and Dbar=P_(U_0)/(z^2+1) as in the endpoint inquiry.
Multiplicativity and P_X=z^2+1 give the exact full identity

    Dbar=(1+z)^(4m_src-2)S_5^(14m_src)P_Y.

Since S_5=(1+z)^(-1) modulo z^4 and m_src=2 modulo4, one obtains

    Dbar=(1+z)^(4m_src-2-14m_src-E_pre-3)
         =(1+z)^(-E_pre-1) modulo z^4.         (WR3)

The exponent reduction is legitimate because(1+z)^4=1 in F_2[z]/z^4.
Equivalently, if the total E_all INCLUDES the fresh3, the exponent is2-E_all modulo4; the condition below is E_all=3 modulo4, not E_all=0.
The complete four classes are

| E_pre modulo4 | (delta_1,delta_2,delta_3) | e at the admissible a=d-3 endpoint |
| --- | --- | --- |
| 0 | (1,1,1) | 2 |
| 1 | (0,1,0) | 0 |
| 2 | (1,0,0) | 0 |
| 3 | (0,0,0) | 0 |

In particular

    delta_3=delta_1 delta_2,
    e=2 iff E_pre=0 modulo4,
    otherwise e=0.                              (WR4)

The endpoint formula is e=delta_0 delta_3+delta_1 delta_2 as an ORDINARY INTEGER count, with delta_0=1.
It uses the actual two reflected pairs{0,3},{1,2} from C747, so this row-source domain has no e=1 case at that endpoint.
The statement about the endpoint remains conditional on gcd(2d-5,15)=1.
No original E_pre value, actual degree congruence or endpoint admissibility has been evaluated.

For one fixed polynomial Y, E_pre modulo4 cannot be changed merely by rewriting its permitted row decomposition with the same fresh cubic factor: WR3 has four distinct right-hand values.
Changing that class requires a different actual polynomial, with its degree and all source conditions paid.
The following extensions do exactly that.

#### A small invisible ordinary row which misses the original fresh factor

Choose the ordinary integer c_ext by

    c_ext=1 if L=1 modulo3,
    c_ext=2 if L=2 modulo3,
    n_ext=1+10L c_ext,
    b_ext=deg B_(n_ext)=5L c_ext<=40Q.          (WR5)

The power of2 L is never0 modulo3, so the choice is defined.
The new index is odd,1 modulo5 and2 modulo3, hence coprime15.
It is1 modulo10L, and the adopted FULL safe period in C664 gives

    B_(n_ext)=B_1=1 modulo R_N,
    R_N=F_2[X]/(X^N phi^(2N)).

This is the actual complete row at the full doubled C691 precision, not just a root-level congruence.
Also

    n_ext<=20L+1<30L<n_star.

The original psi_star has primitive trace order n_star and cannot divide B_(n_ext), since that would require n_star|n_ext.
Proper-divisor overlaps with the old support cause no problem.
No claim that gcd(n_ext,n_star)=1 is needed, and no prime search or new primitive factor is required.

For an integer rho in{0,2,3,5}, put

    M_rho=B_(n_ext)^rho,
    Y_rho=Y M_rho,
    U_rho=U_0 M_rho,
    R_rho=R_0 M_rho.                            (WR6)

The positive choices have rho>=2, so every NEW irreducible factor has multiplicity at least2 and every old multiplicity only increases.
Both full forward divisibilities are preserved because B_(n_ext) is a complete squarefree odd-order row with index coprime3 and5.
In the C667 whole-row pattern it only increases ordinary multiplicities u_d, preserving v_d<=u_d.
The original psi_star occurs to EXACT multiplicity3 in Y_rho and Y_rho B, because B and psi_star are unchanged and the new row misses psi_star.
Thus Y_rho, Y_rho B, U_rho and R_rho retain the original nonsquare witness, even for the odd exponents rho that change some other odd-multiplicity factors.
No equality of all old odd parts is asserted for odd rho.

Since M_rho=1 in R_N, both original DG3 jets are unchanged.
Moreover M_rho(chi)=1 modulo phi^(2N), because its low X^N congruence acquires phi-order2N under chi.
Writing H_rho=X^(2m_src)Y_rho, V_rho=H_rho B and C_rho=X^(2m_src)Y_rho(chi)Psi^(14m_src), their full phi^(16m_src) data agree with H_0,V_0,C_00.
Every DG6 relation, the same beta and Z_0, and the derivative X^(8m_src)|Y_rho' therefore remain valid.
For the derivative, one can either differentiate the same even-depth square low jet or use N even and M_rho=1 modulo X^N.
These verifications do not use a large-multiplier lower bound such as a_mul>=d/2.

The full forward divisibility gives H_rho|C_rho.
The identity

    U_rho(chi)^3+R_rho
       =phi^(12m_src)(V_rho+C_rho^3)

vanishes on H_rho and on phi^(14m_src), by the preserved doubled identities.
Those moduli are coprime, and the original positive degree gap is unchanged.
Hence the ACTUAL complete monic remainder and forward statement are

    R_rho=rem_(U_rho)(U_rho(chi)^3)!=0,
    U_rho|U_rho(X^3+X).                         (WR7)

The sole unsaturated phi orders stay14m_src/12m_src, with every other full primary saturated.
Thus any monic integer trace reducing to U_rho has bbar=0 and ACTUAL canonical Gbar=R_rho, but no dyadic quotient or passing residual input has been supplied.

#### All four exponent classes, optional admissibility preservation and paid costs

The augmented row presentation is Y_pre B_(n_ext)^rho followed by the SAME fresh cubic, so

    E_pre,new=E_pre+rho,
    Dbar_new=Dbar S_(n_ext)^rho
             =(1+z)^(-E_pre-rho-1) modulo z^4. (WR8)

The four values rho=0,2,3,5 represent all residues modulo4.
They produce all four low coefficient classes while retaining the COMPLETE source properties just checked, with exact added trace degree rho b_ext<=200Q.
They do not by themselves preserve the admissibility of the newly recomputed endpoint2deg(U_rho)-5 modulo3.

If that endpoint admissibility is also to be preserved, use instead

    rho in{0,3,6,9}.                            (WR9)

Every positive exponent is still at least2, so all preceding source arguments apply verbatim.
These four exponents again represent all classes modulo4.
Now b_ext is divisible by5 and rho is divisible by3, so rho b_ext=0 modulo15.
The actual new degree d_rho=d+rho b_ext therefore satisfies d_rho=d modulo15, and gcd(2d_rho-5,15)=gcd(2d-5,15).
Thus an already admissible endpoint remains admissible; an inadmissible original endpoint is not silently made admissible.
This option costs at most360Q additional trace degree.

For the first choice the original DG8 bound gives the NEW conservative bounds

    degY_rho<=14400Q^3+1206Q^2+320Q,
    d_rho<=14400Q^3+1206Q^2+328Q.

For the admissibility-preserving choice the NEW bounds are

    degY_rho<=14400Q^3+1206Q^2+480Q,
    d_rho<=14400Q^3+1206Q^2+488Q.               (WR10)

More precisely degY_rho=degY+rho b_ext, degU_rho=d+rho b_ext and degR_rho=degR_0+rho b_ext.
Thus the original gap is exactly retained:

    degU_rho-degR_rho=m_src-8-5degH_aux
                                      >5m_src/256.

After raising by q=2^j, the trace degrees and gap are multiplied by q and the reciprocal degree is2q d_rho.
The unchanged exact triple factor proves the actual maximal Frobenius exponent q of U_rho^q and R_rho^q.
It also proves nonsquareness of the reciprocal base: its nonidentity odd-order trace factor pulls back to squarefree reciprocal roots, since z+z^(-1) is unramified away from z=1, and none of these order-n_star roots is1.
Their multiplicity remains3, so the reciprocal binary polynomial also has actual maximal power q after raising.

The actual layer vector a_0=12m_src q and a_b=0 for b>=1 is unchanged.
Every added complete primitive order e|n_ext,e>1 is odd and prime to5.
Using the accepted integer trace factors F_e from C691/C667, the full synthetic lift is multiplied by product_(e|n_ext,e>1)F_e^(rho q).
It has exactly rho q b_ext extra degree and still has zero normalized circle Haar logarithmic integral with all factors, multiplicities and integrable zeros retained.
This synthetic integer polynomial is not identified with the ACTUAL integer canonical G(T), and supplies no original irreducible realization or total-Mahler bound.

The new numerical bounds are NOT the original DG8 bounded-witness assertion.
The construction starts from one such actual bounded witness and pays for new complete representatives with the SAME finite source class.
The actual original E_pre remains unevaluated, although the four new representatives cover all its possible residues.
If the original endpoint is admissible, the admissibility-preserving option gives exactly one of those four new source classes with e=2 at its recomputed a=d_rho-3 endpoint, and the other three have e=0.
This is an existence/class-control statement for the paid complete extensions, not an evaluation or a free modification of the original bounded source.

#### What an invisible squared row alone can and cannot change

For ANY nontrivial ordinary row B_n with n>=5, reciprocal multiplication by B_n^2 changes the low z^4 jet by the factor

    S_n^2=(1+z)^(-2)=1+z^2 modulo z^4.

In particular the ACTUAL invisible squared row in C738, with its separately proved source preservation and enlarged expense, has exactly the effect

    delta_1,new=delta_1,
    delta_2,new=delta_2+1,
    delta_3,new=delta_3+delta_1.                (WR11)

Its ordinary-row class shifts E_pre by2, retaining the same extracted fresh cubic.
Thus a squared row preserves E_pre parity: it interchanges classes0 and2, or classes1 and3.
It cannot by itself move an odd E_pre class into the e=2 class0.
The odd invisible powers in WR6/WR9 are what permit all four classes while retaining the selected fresh multiplicity3 and paying their actual degree.
No contradiction arises with preserving finite jets, because the low reciprocal coefficients here are not those low trace jets.

These extensions do NOT establish the separate full-support parity Lambda(U_rho)=0, solve any restricted height1 sign system, or evaluate the remaining endpoint affine target/rank.
C738's large-multiplier proof of Lambda=0 used its additional degree lower bound and is not imported into the small invisible extensions.
Neither e=2 nor a paid choice of that class supplies a nonzero even mask satisfying every old primary or an irreducible original polynomial.
The useful conclusion is the explicit ordinary-row congruence and controlled full-source class freedom, with the unchanged gap and honest new cost; all height1, full residual and characteristic-zero realization questions remain separate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision whole-row-class-control-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:23 |
| status | open |
| reason | Register the entire WR1--WR11 author theorem after root read the complete actual row algebra, small-row safe period and fresh-factor separation, canonical/source recomputation, all residue classes and both paid budgets. The reciprocal z4 class is determined by the pre-fresh ordinary exponent modulo4, with B1/divided/fresh conventions exact and endpoint e conditional on admissibility. A genuine invisible ordinary row and explicit nonnegative powers preserve every complete source condition and exact original triple factor while paying <=200Q or <=360Q extra trace degree; the latter also preserves endpoint admissibility. Root and characteristic_zero_bridge are contributors, not independent reviewers; fresh isolated whole review and separate adoption remain outstanding. No original exponent value, endpoint admissibility, height1 sign solution, full parity, irreducible realization or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete row-class and extension theorem](#statement) | Parts A--D: actual retained row witness and exponent convention, conditional endpoint class, explicit complete invisible row, two finite exponent sets, every preserved source/canonical/root/multiplicity condition, exact and conservative new costs, raised normalization, synthetic layer and all realization exclusions. |
| argument | [Entire WR1--WR11 proof](#complete-argument) | Full reciprocal ordinary/divided row identities, modulus-z4 exponent calculation, safe-period invisible row and preserved exact fresh3, full canonical/root/forward reconstruction, all class choices and admissibility, actual degree/gap/layer costs and squared-row limitation. |
| dependency | [Adopted complete original doubled-precision construction](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and Sections3/5: actual bounded starting whole-row Y, Q/m/H/B, safe L=4Q/e_pad=12Q, full jets/root/canonical/gap/layer data, selected fresh n_star and exact triple psi_star. The new extensions receive NEW bounds rather than the old DG8 numerical label. |
| dependency | [Adopted complete row and fresh-factor mechanism](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC4 ordinary/divided complete products, nonnegative row inequalities and both forward maps, floor adjustment, exact primitive-order separation and full canonical remainder; retained integer trace-factor/layer/Haar interface including all multiplicities. |
| dependency | [Adopted all-depth safe finite row source](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | G4--G5 full ordinary/divided row ranges and actual coprime-three replacements, exact full predivision moduli, safe B-index period10L and finite exponent bound. Only the actual row/period interface is consumed; no native rank or source-exponent choice is inferred. |
| dependency | [Adopted complete reciprocal row identities](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete B_n Laurent geometric sum and full root/divisor partition, including B1=1. The divided reciprocal quotient and low z4 products are computed exactly here, without using the source's finite native certificate. |
| dependency | [Adopted explicit endpoint mask count](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | At admissible a=d-3, the exact two reflected pairs give e=delta0delta3+delta1delta2 as an ordinary count; no numerical original delta/e value, full sign feasibility or irreducibility is imported. New extended-source applications use their actual new degrees and the structural conditions proved here. |
| dependency | [Adopted actual invisible squared-source family](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25) | PA8--PA12 complete squared multiplier, source-preservation and cost scope for the final comparison. Its separate large-degree Lambda=0 conclusion is not assigned to the new small ordinary-row extensions. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:31 |
| status | proved |
| reason | Register the entire WR1--WR11 author theorem after root read the complete actual row algebra, small-row safe period and fresh-factor separation, canonical/source recomputation, all residue classes and both paid budgets. The reciprocal z4 class is determined by the pre-fresh ordinary exponent modulo4, with B1/divided/fresh conventions exact and endpoint e conditional on admissibility. A genuine invisible ordinary row and explicit nonnegative powers preserve every complete source condition and exact original triple factor while paying <=200Q or <=360Q extra trace degree; the latter also preserves endpoint admissibility. Adopt fresh context-isolated whole R971 after root read the entire WR1--WR11 proof, fixed standalone Parts A--D and all exact dependency scopes, then the entire independent finding. Root and characteristic_zero_bridge remain contributors; the reviewer contributed no substantive correction. All actual complete-source and extended-degree endpoint interfaces passed at their stated conditional scope. No original exponent value, endpoint admissibility, height1 sign solution, full parity, irreducible realization or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete row-class and extension theorem](#statement) | Parts A--D: actual retained row witness and exponent convention, conditional endpoint class, explicit complete invisible row, two finite exponent sets, every preserved source/canonical/root/multiplicity condition, exact and conservative new costs, raised normalization, synthetic layer and all realization exclusions. |
| argument | [Entire WR1--WR11 proof](#complete-argument) | Full reciprocal ordinary/divided row identities, modulus-z4 exponent calculation, safe-period invisible row and preserved exact fresh3, full canonical/root/forward reconstruction, all class choices and admissibility, actual degree/gap/layer costs and squared-row limitation. |
| dependency | [Adopted complete original doubled-precision construction](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and Sections3/5: actual bounded starting whole-row Y, Q/m/H/B, safe L=4Q/e_pad=12Q, full jets/root/canonical/gap/layer data, selected fresh n_star and exact triple psi_star. The new extensions receive NEW bounds rather than the old DG8 numerical label. |
| dependency | [Adopted complete row and fresh-factor mechanism](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | FC1--FC4 ordinary/divided complete products, nonnegative row inequalities and both forward maps, floor adjustment, exact primitive-order separation and full canonical remainder; retained integer trace-factor/layer/Haar interface including all multiplicities. |
| dependency | [Adopted all-depth safe finite row source](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | G4--G5 full ordinary/divided row ranges and actual coprime-three replacements, exact full predivision moduli, safe B-index period10L and finite exponent bound. Only the actual row/period interface is consumed; no native rank or source-exponent choice is inferred. |
| dependency | [Adopted complete reciprocal row identities](Yin_C_G0608_v1.md#decision-whole-reviewed-2026-10-23) | Complete B_n Laurent geometric sum and full root/divisor partition, including B1=1. The divided reciprocal quotient and low z4 products are computed exactly here, without using the source's finite native certificate. |
| dependency | [Adopted explicit endpoint mask count](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | At admissible a=d-3, the exact two reflected pairs give e=delta0delta3+delta1delta2 as an ordinary count; no numerical original delta/e value, full sign feasibility or irreducibility is imported. New extended-source applications use their actual new degrees and the structural conditions proved here. |
| dependency | [Adopted actual invisible squared-source family](Yin_C_G0738_v1.md#decision-whole-reviewed-2026-10-25) | PA8--PA12 complete squared multiplier, source-preservation and cost scope for the final comparison. Its separate large-degree Lambda=0 conclusion is not assigned to the new small ordinary-row extensions. |
| review | [Fresh independent whole row-class and extension review](../audits/reviews/Yin_R_G0971_v1.md#whole-row-class-control-finding) | Entire fixed Parts A--D and WR1--WR11, exact ordinary/divided/fresh conventions, both extension sets, full source/root/canonical/multiplicity properties, actual endpoint interfaces, degree/gap/layer costs and every conditional or unevaluated limit; independently reviewed with exact statement and argument bindings. |

