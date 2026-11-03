---
author: Yin
---

# Paid complete sources with an unconditionally admissible two-dimensional endpoint mask

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the safe-unit B_7 degree adjustment followed by an invisible ordinary row selecting the exponent class and the remaining degree class.
The characteristic_zero_bridge agent checked the full unit exponent, source preservation and exact degree costs, and supplied the optimized two-candidate selection with total increment at most396Q.
Root read the complete saved UC1--UC10 argument.
Both agents are substantive contributors; fresh isolated whole review and separate adoption remain outstanding.
No native coefficient expansion, source-exponent evaluation or affine-rank calculation is used.
The [endpoint affine investigation](../drafts/Yin_D_G0006.md#next-endpoint-edge-sign-and-old-x-interface) and [true-certificate inquiry](../drafts/Yin_D_G0006.md#finite-construction-true-certificate-boundary) are separate unresolved work, not parts of this Claim.

## Statement

Work over F_2 with phi=X^2+X+1, chi=Xphi^2, lambda=X^3+X and Psi=phi(chi).
For positive odd n, B_n is the COMPLETE trace polynomial of all nonidentity n-th roots, with B_1=1 and degB_n=(n-1)/2.
For a monic binary trace polynomial f, write P_f(z)=z^(degf)f(z+z^(-1)), its full reciprocal transform.
All polynomial exponents and degree costs are ordinary nonnegative integers; negative powers below are only powers of units in the specified finite quotient.

### A. Actual starting source and finite parameter choices

Start with ANY ACTUAL bounded whole-row witness of [adopted C691](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), retaining all its complete factors, multiplicities and finite source data.
In particular retain

    Q=2^ell, ell>=82, m_src=Q/4-2,
    N=8m_src=2Q-16, L=4Q, e_pad=3L=12Q,
    Y=Y_pre B_(n_star)^3,
    H_0=X^(2m_src)Y,
    U_0=H_0phi^(14m_src), d=degU_0,
    B_src=X^(Q-m_src)H_aux(chi),
    R_0=H_0phi^(12m_src)B_src.

H_aux and B_src are the original complete C691 auxiliary and source polynomials.
Y_pre is the actual C664/C667 product of complete ordinary B_n rows with gcd(n,15)=1 and divided rows B_(5ell_row)/phi with gcd(ell_row,15)=1, after their multiplicity-floor adjustment.
The original fresh index n_star>30L=120Q and its selected order-n_star factor psi_star have the exact C691 meaning: psi_star has multiplicity3 in Y and Y B_src.
Let E_pre be the ordinary integer sum of the NONTRIVIAL ORDINARY row exponents in Y_pre, excluding B_1, every divided row and the final fresh cubic.
The original E_pre and d modulo15 are not evaluated, and original endpoint admissibility is NOT assumed.

Define the first parameter by the actual degree class:

    s_7=0 if5 does not divide d, and s_7=1 if5 divides d,
    d_1=d+36Q s_7.

Define the second complete row by

    c_ext=1 if L=1 modulo3, and c_ext=2 if L=2 modulo3,
    n_ext=1+10L c_ext,
    b_ext=degB_(n_ext)=5L c_ext<=40Q.

Then b_ext=2 modulo3 and0 modulo5, and n_ext<30L<n_star.
Let r_class=-E_pre modulo4.
Choose rho to be the LEAST member of the following pair for which d_1+rho b_ext is not1 modulo3:

| r_class | Candidate pair |
| --- | --- |
| 0 | {0,4} |
| 1 | {5,9} |
| 2 | {2,6} |
| 3 | {3,7} |

This finite choice always exists.
Every positive chosen exponent is at least2 and rho<=9.
Set

    M=B_7^(s_7 e_pad)B_(n_ext)^rho,
    Y_sharp=Y M, U_sharp=U_0 M, R_sharp=R_0 M,
    Delta_d=36Q s_7+rho b_ext,
    d_sharp=d+Delta_d.

These ACTUAL complete polynomial extensions satisfy

    E_pre,sharp=E_pre+s_7 e_pad+rho=0 modulo4,
    d_sharp!=0 modulo5, d_sharp!=1 modulo3,
    gcd(2d_sharp-5,15)=1,
    Delta_d<=396Q.

Thus admissibility and the desired exponent class are achieved simultaneously for every actual starting witness by finite choices based on that witness.
No original exponent value or original degree residue is inferred.

### B. Complete source preservation and actual canonical binary remainder

In the FULL ring R_N=F_2[X]/(X^N phi^(2N)), every unit f satisfies f^(e_pad)=1, and

    B_7^(e_pad)=1, B_(n_ext)=1, M=1 in R_N.

Y_sharp is monic, complete and prime to Xphi, every occurring irreducible factor has multiplicity at least2, and BOTH full forward divisibilities hold:

    Y_sharp | Y_sharp(lambda),
    Y_sharp | Y_sharp(chi).

The original psi_star still has EXACT multiplicity3 in Y_sharp and Y_sharp B_src.
The original DG3 finite class is unchanged, and X^(8m_src) divides Y_sharp'.
Other odd-multiplicity parts need not remain identical.

With the SAME original beta and Z_0, put

    H_sharp=X^(2m_src)Y_sharp,
    V_sharp=H_sharp B_src,
    C_sharp=X^(2m_src)Y_sharp(chi)Psi^(14m_src).

At FULL precision phi^(16m_src), retain all identities

    H_sharp=B_src^(-7), C_sharp=beta^2B_src^(-2),
    V_sharp+C_sharp^3=0, H_sharp^6=C_sharp^21,
    Z_0=beta^2B_src^(-1), Z_0^11=H_sharp C_sharp^2,
    Z_0(V_sharp+C_sharp^3)=0.

Here beta has the original specified cube-one residue, and Z_0 is the unique eleventh root at the stated precision.
Globally,

    R_sharp=rem_(U_sharp)(U_sharp(chi)^3)!=0,
    U_sharp | U_sharp(lambda),
    d_sharp-degR_sharp
        =m_src-8-5degH_aux>5m_src/256.

The only unsaturated primary remains phi, with orders14m_src/12m_src; every other full primary is saturated.

For a monic integer trace T, define its OWN canonical polynomials using C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X:

    a_T=rem_T(T(C_2))/2,
    b_T=rem_T(T(C_3))/3,
    c_T=rem_T(T(C_5))/5,
    F_T=rem_T(2c_T^2-3a_T^5),
    G_T=rem_T(c_T^3-2b_T^5),
    X_(s,T)=rem_T(b_T^2-a_T^3+sG_T), s in{1,-1}.

All monic remainders and scalar divisions are actual integer operations at that SAME T before reduction.
Every such T reducing to U_sharp has b_Tbar=0 and G_Tbar=R_sharp.
No dyadic divided-remainder choice or full integer residual equation is solved here.

### C. Exact new costs, raised sources and complete synthetic layer

The exact degrees are

    degY_sharp=degY+Delta_d,
    degU_sharp=d+Delta_d,
    degR_sharp=degR_0+Delta_d.

From the actual original DG8 budget one obtains the NEW bounds

    degY_sharp<=14400Q^3+1206Q^2+516Q,
    d_sharp<=14400Q^3+1206Q^2+524Q.

These are enlarged paid budgets, not the original DG8 numerical bound.
For every q=2^j, j>=0, all binary canonical and root identities raise to their full q-scaled precisions, with trace degree q d_sharp, FULL reciprocal degree2q d_sharp and full positive gap q(m_src-8-5degH_aux).
The exact triple factor proves that U_sharp^q, R_sharp^q and the full reciprocal binary polynomial have maximal Frobenius power exactly q.
For every monic integer trace reducing to U_sharp^q, its actual b_Tbar=0 and G_Tbar=R_sharp^q.

The original integer layer vector a_0=12m_src q, a_b=0 for b>=1 and zero strict-window correction remain unchanged.
If F_e denotes the accepted complete monic INTEGER trace factor for odd primitive order e, the synthetic integer polynomial is the original G_int multiplied by

    F_7^(s_7 e_pad q)
      product_(e|n_ext,e>1)F_e^(rho q).

If7 divides n_ext, the displayed multiplicities add.
Its exact degree increment is q Delta_d and its normalized circle Haar logarithmic integral remains0, counting every complete factor, multiplicity and integrable zero.
This synthetic polynomial is not identified with the actual integer canonical G_T, and supplies no original irreducible or controlled-total-Mahler realization.

### D. Actual endpoint mask and the distinct outer polynomial

Put

    Dbar_sharp=P_(U_sharp)/(z^2+1).

Then

    Dbar_sharp=(1+z)^(-1)=1+z+z^2+z^3 modulo z^4.

The endpoint a_end=d_sharp-3 is NOW admissible, with n_end=2a_end+1=2d_sharp-5 coprime15.
This is an application of C747's structural local mask proof with the actual new source data and degree.
Its two reflected pairs {0,3} and {1,2} are present, so the mask dimension is EXACTLY2, with basis

    J_0=1+z+z^2, J_1=z.

The unique nonzero mask satisfying J(1)=0 is J_0+J_1=1+z^2.
These are actual local mask conclusions; they do not evaluate an old-primary affine target, rank or sign solution.

The complete source to which Parts B--C apply is U_sharp of trace degree d_sharp.
The endpoint height1 problem THEN introduces a further outer factor:

    U_end=U_sharp B_(n_end)^2,
    degU_end=3d_sharp-6,
    full reciprocal degree at q=2q(3d_sharp-6).

The outer multiplier lies in C747's algebraic local domain, including possible overlap with the old source, but is NOT asserted to preserve every DG3/DG6 jet or the actual global canonical remainder by C775's special source-preserving multiplier theorem.
All complete-source preservation and synthetic-layer claims above concern U_sharp BEFORE that outer step.
The endpoint reciprocal binary polynomial remains nonsquare, so every monic reciprocal height1 lift of its q-th power is exactly a dyadic substitution P(z^q) of a base height1 lift, with the own trace and full degree retained.

No claim is made that Lambda(U_sharp)=0, that all old-primary sign equations are consistent, that a nonzero even mask has an irreducible realization, or that any passing full height1 residual input has been constructed.
No characteristic-zero identity, original total-Mahler bound or unrestricted G0001 conclusion is supplied.

## Complete argument

<a id="unconditional-admissible-endpoint-class-two-source"></a>
### Paid complete sources with an admissible two-dimensional endpoint mask

This is the complete fixed author argument by root and characteristic_zero_bridge, separate from the endpoint affine calculation and certificate inquiry.
Root proposed using the safe unit exponent on B_7 to remove the degree-modulo5 obstruction, followed by an invisible ordinary row fixing the exponent class while avoiding the bad degree-modulo3 class.
Characteristic_zero_bridge checked the complete unit exponent, both finite selections, every full-source and degree interface, and the smaller two-candidate selection below.
The actual source inputs are [adopted C691](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24), [C664 HG7's safe full unit exponent](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24), [C667's full ordinary-row/forward/fresh mechanism](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24), and [C747's actual endpoint mask interface](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25).
The [adopted C751 WR1--WR11 proof](Yin_C_G0751_v1.md#decision-whole-reviewed-2026-10-25) was read for its explicit row and class identities; the new B_7 degree adjustment and simultaneous admissibility selection below are separately proved here.
The present argument checks the new powers directly and supplies no original integer residual or irreducible realization.

#### Full safe exponent and the first invisible ordinary factor

Start with ANY actual bounded C691 row witness Y=Y_pre B_(n_star)^3 and retain all its complete source data, including

    Q=2^ell, ell>=82, m_src=Q/4-2,
    N=8m_src=2Q-16, L=4Q, e_pad=3L=12Q,
    U_0=X^(2m_src)Yphi^(14m_src), d=degU_0,
    n_star>30L=120Q,
    E_pre=sum of nontrivial ordinary-row exponents in Y_pre.

Write phi=X^2+X+1, chi=Xphi^2 and Psi=phi(chi) over F_2.
The original auxiliary and canonical source polynomials are H_aux, B_src=X^(Q-m_src)H_aux(chi) and R_0=X^(2m_src)Yphi^(12m_src)B_src, with their complete C691 meanings.
As before E_pre excludes B_1, every divided row and the final fresh cubic.
No actual value of E_pre or d modulo15 is assumed.
The ring is the COMPLETE R_N=F_2[X]/(X^N phi^(2N)), with phi=X^2+X+1.

Every unit f of this ring satisfies f^(e_pad)=1.
Indeed at X its residue is1, so f=1+Xg and f^L=1 because L>=N and Frobenius raises X to X^L.
At phi the nonzero residue lies in F_4 and has cube1, so f^3=1+phi h and (f^3)^L=1 because L>=2N.
CRT gives the exact full statement

    f^(3L)=1 in R_N for every f in R_N^*.     (UC1)

This proves the required safe exponent directly; minimality is not claimed.
The complete ordinary B_7 has degree3, constant1, and is prime to Xphi because its nonidentity seventh-root traces contain neither trace0 nor primitive-fifth traces.
Its index is coprime3 and5, so it has both full forward divisibilities by the complete-root argument.
Also7<n_star, so B_7 misses the originally selected order-n_star factor psi_star.
Thus

    B_7^(e_pad)=1 in R_N,
    deg B_7^(s_7 e_pad)=36Q s_7.                (UC2)

Choose s_7=0 when5 does not divide d, and s_7=1 when5 divides d.
This is a legitimate invisible ordinary extension, and every positive added multiplicity is e_pad>=2.
Its change to E_pre is s_7 e_pad=0 modulo4.
Its degree change is0 modulo3 and is Q s_7 modulo5, since36=1 modulo5 and Q is a unit modulo5.
Therefore this explicit choice gives

    d_1=d+36Q s_7 is nonzero modulo5,
    d_1=d modulo3, 36Q s_7<=36Q.               (UC3)

No value of the original degree class is asserted; the rule defines the required choice for each actual source witness.

#### The second row fixes E_pre and the remaining admissibility condition

Use the actual small ordinary row from WR5, with the SAME original Q,L,n_star:

    c_ext=1 if L=1 modulo3, c_ext=2 if L=2 modulo3,
    n_ext=1+10L c_ext,
    b_ext=deg B_(n_ext)=5L c_ext<=40Q.

It satisfies n_ext<=20L+1<30L<n_star, gcd(n_ext,15)=1 and B_(n_ext)=1 in the FULL R_N.
Also L c_ext=1 modulo3, hence

    b_ext=2 modulo3, b_ext=0 modulo5.          (UC4)

Put r_class=-E_pre modulo4 and restrict rho to the corresponding pair:

| r_class | candidates for rho |
| --- | --- |
| 0 | {0,4} |
| 1 | {5,9} |
| 2 | {2,6} |
| 3 | {3,7} |

Choose the least candidate satisfying

    rho=-E_pre modulo4,
    d_1+rho b_ext!=1 modulo3.                  (UC5)

Such a choice ALWAYS exists.
Each pair has the required class modulo4, contains no1, and has two distinct residues modulo3 because its entries differ by4.
The second condition excludes exactly one residue modulo3, since b_ext is a unit modulo3, so at most one of the two candidates is excluded.
Every positive permitted rho is at least2, preserving the full factor-multiplicity floor.
This explicit rule has rho<=9 and second-step fee rho b_ext<=360Q.

Put

    M=B_7^(s_7 e_pad) B_(n_ext)^rho,
    Y_sharp=Y M, U_sharp=U_0 M, R_sharp=R_0 M,
    Delta_d=36Q s_7+rho b_ext,
    d_sharp=d+Delta_d.                          (UC6)

The pre-fresh ordinary exponent is E_pre,sharp=E_pre+s_7 e_pad+rho=0 modulo4.
By UC3--UC5, d_sharp is nonzero modulo5 and is not1 modulo3.
Thus, with the ACTUAL new degree,

    gcd(2d_sharp-5,15)=1,
    E_pre,sharp=0 modulo4,
    Delta_d<=396Q.                             (UC7)

There is no assumption that the original endpoint was admissible.
These are actual changes of the complete polynomial, not a change in notation or the choice of a representative of the same reciprocal support.

#### Complete source, canonical remainder and raised normalization are retained

Both factors of M are actual complete ordinary rows, with indices coprime15 and below n_star, raised either to exponent0 or to an integer at least2.
Thus Y_sharp is monic, complete and prime to Xphi, has every occurring irreducible multiplicity at least2, and has BOTH full global forward divisibilities under X^3+X and chi=Xphi^2.
Every ordinary multiplicity only increases in the C667 row pattern, so v_d<=u_d remains true.
The original psi_star still has EXACT multiplicity3 in Y_sharp and Y_sharp B_src, because neither added row contains its primitive order and the original complete B_src is unchanged.
No new fresh-order search and no equality of other odd-multiplicity parts is asserted.

By UC1--UC4, M=1 in R_N, so the full original DG3 finite class is unchanged.
Moreover M(chi)=1 modulo phi^(2N) because its low X^N congruence acquires phi-order2N under chi.
Keep the same H_aux,B_src,beta,Z_0 from the original C691 construction and define

    H_sharp=X^(2m_src)Y_sharp,
    V_sharp=H_sharp B_src,
    C_sharp=X^(2m_src)Y_sharp(chi)Psi^(14m_src).

At the FULL precision phi^(16m_src)=phi^(2N) the original identities persist:

    H_sharp=B_src^(-7), C_sharp=beta^2B_src^(-2),
    V_sharp+C_sharp^3=0, H_sharp^6=C_sharp^21,
    Z_0=beta^2B_src^(-1), Z_0^11=H_sharp C_sharp^2,
    Z_0(V_sharp+C_sharp^3)=0.                   (UC8)

The old beta retains its specified cube-one residue, and Z_0 remains the unique eleventh root of H_sharp C_sharp^2 at that precision.
The unchanged square low jet, with N even, also gives X^(8m_src)|Y_sharp'.
These are consequences of the exact invisible products, not assumptions imported from a newly constructed integer trace.

The complete forward divisibility gives H_sharp|C_sharp, and

    U_sharp(chi)^3+R_sharp
      =phi^(12m_src)(V_sharp+C_sharp^3)

vanishes on both coprime factors H_sharp and phi^(14m_src).
The strict original degree gap remains positive, so

    R_sharp=rem_(U_sharp)(U_sharp(chi)^3)!=0,
    U_sharp|U_sharp(X^3+X),
    degU_sharp-degR_sharp
        =m_src-8-5degH_aux>5m_src/256.           (UC9)

The only unsaturated primary is still phi with orders14m_src/12m_src.
For any monic integer trace with reduction U_sharp, actual odd divided remainders therefore give bbar=0 and canonical Gbar=R_sharp; the dyadic quotient and full residual equations have not been solved.

For every q=2^j the original exact triple witness gives maximal Frobenius exponent q separately for U_sharp^q and R_sharp^q.
The reciprocal binary polynomial has it too: the retained nonidentity odd-order trace factor pulls back without ramification to reciprocal roots of multiplicity3, so the base is not a square.
All characteristic-two canonical and root identities raise to their full original q-scaled precisions, and the source reciprocal degree is2q d_sharp.

#### Exact costs, synthetic layer and the actual endpoint conclusion

For the explicit selection in UC3/UC5,

    degY_sharp=degY+Delta_d,
    degU_sharp=d+Delta_d,
    degR_sharp=degR_0+Delta_d.

The complete new bounds from the original DG8 witness are

    Delta_d=36Q s_7+rho b_ext<=396Q,
    degY_sharp<=14400Q^3+1206Q^2+516Q,
    d_sharp<=14400Q^3+1206Q^2+524Q.

These are NEW paid budgets, not the original bounded-witness numerical assertion.
At q the degrees and gap are multiplied by q, with every original factor and multiplicity retained.
The integer layer vector a_0=12m_src q, a_b=0 for b>=1 and its zero strict-window correction remain unchanged.
With the accepted complete integer trace factors F_e, the new synthetic lift is the old G_int multiplied by

    F_7^(s_7 e_pad q)
      product_(e|n_ext,e>1) F_e^(rho q).

If7 also divides n_ext, the two displayed contributions simply add their actual multiplicities.
Its exact degree increment is q Delta_d and its normalized circle Haar logarithmic integral remains0, with all roots, multiplicities and integrable zeros counted.
It is not identified with the actual integer canonical G(T), and supplies no original irreducible or controlled-Mahler realization.

Since E_pre,sharp=0 modulo4, the complete row reciprocal calculation gives

    Dbar_sharp=(1+z)^(-1)=1+z+z^2+z^3 modulo z^4.

At the NOW admissible endpoint a_end=d_sharp-3, the two actual reflected pairs{0,3},{1,2} are therefore present and the mask dimension is EXACTLY2.
The explicit basis is J_0=1+z+z^2,J_1=z, and the unique nonzero even mask is1+z^2.
This applies the structural proof of C747 with the full source facts verified above and the actual NEW degree; its original numerical source budget is not reused.
No original E_pre value or original endpoint admissibility has been inferred: both desired properties have been achieved by the paid extensions.

The complete source on which UC8--UC9 hold is U_sharp, of trace degree d_sharp.
To form the endpoint height1 question one THEN introduces the further outer multiplier B_(n_end)^2 with n_end=2d_sharp-5, giving

    U_end=U_sharp B_(n_end)^2,
    degU_end=3d_sharp-6,
    full reciprocal degree at q=2q(3d_sharp-6). (UC10)

The outer multiplier is admissible for C747's algebraic local mask argument, but is not asserted to preserve all DG3/DG6 jets or the ACTUAL global canonical remainder by an unproved use of C775's special multiplier theorem.
The complete-source degree/gap/canonical/synthetic preservation in UC8--UC9 concerns U_sharp before that outer step.
The endpoint binary polynomial remains nonsquare because the outer reciprocal factor is a square, and exact height1 descent retains the actual base-sign problem at q.
The actual e=2 conclusion supplies the two-dimensional local mask domain; it does not evaluate EP10's reference target/rank, impose every old primary or establish irreducibility.
No claim that Lambda(U_sharp)=0, no passing full height1 residual solution, no characteristic-zero identity and no unrestricted G0001 conclusion is made.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision admissible-endpoint-source-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:42 |
| status | open |
| reason | Register the complete UC1--UC10 author construction after root read the whole saved proof. For every actual bounded C691 whole-row witness, a safe-unit B7 adjustment and a two-candidate invisible-row choice achieve exponent class0 and endpoint admissibility together with extra degree at most396Q, preserving all original complete-source data at new paid bounds. The resulting endpoint has a two-dimensional local mask space and one nonzero even mask, with the preserved source and the further outer endpoint polynomial kept separate. Root and characteristic_zero_bridge are contributors, not independent reviewers; fresh isolated whole review and separate adoption remain outstanding. No original residue evaluation, old-primary affine rank, full sign solution, irreducible realization or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete paid admissible-source theorem](#statement) | Parts A--D: actual starting witness and finite choices without original admissibility, full source/root/canonical preservation, exact and enlarged degree/gap/layer costs, raised normalization, actual endpoint mask and distinct outer-polynomial limits. |
| argument | [Entire UC1--UC10 proof](#complete-argument) | Full unit exponent, B7 degree repair, explicit two-candidate rho table, all-primary source and canonical recomputation, preserved exact fresh3, optimized396Q cost, complete synthetic factors and algebraic endpoint application with all unresolved realization boundaries. |
| dependency | [Adopted original complete doubled-precision source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and Sections3/5: actual bounded whole-row Y, Q/m/H_aux/B_src, original full finite jets/root/canonical/gap/layer data and selected fresh order with exact triple factor. The new witnesses receive NEW enlarged bounds. |
| dependency | [Adopted complete finite unit and row source](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | HG7 full finite-unit exponent and G4--G5 actual complete row domain and safe B-index period; the needed safe exponent is also proved directly in UC1. No source exponent vector or native rank is evaluated. |
| dependency | [Adopted full ordinary-row and fresh mechanism](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Complete ordinary/divided row products, both global forward maps, multiplicity-floor and fresh-order separation, and complete integer trace-factor/layer/Haar interface with every multiplicity. |
| dependency | [Adopted whole-row class and invisible extension theorem](Yin_C_G0751_v1.md#decision-whole-reviewed-2026-10-25) | WR1--WR11: exact pre-fresh exponent convention, reciprocal z4 class, small invisible ordinary row with its safe period and fresh-factor separation, and actual full-source reconstruction. The new simultaneous degree/exponent choices and396Q budget are proved here. |
| dependency | [Adopted explicit local endpoint mask and descent theorem](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Structural reflection basis and exact J(1) parity at admissible a=d-3, with actual source conditions verified here; old-source overlap and exact raised height1 descent. Its special complete-multiplier budget is not transferred to the arbitrary outer endpoint factor. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T21:49 |
| status | proved |
| reason | Register the complete UC1--UC10 author construction after root read the whole saved proof. For every actual bounded C691 whole-row witness, a safe-unit B7 adjustment and a two-candidate invisible-row choice achieve exponent class0 and endpoint admissibility together with extra degree at most396Q, preserving all original complete-source data at new paid bounds. The resulting endpoint has a two-dimensional local mask space and one nonzero even mask, with the preserved source and the further outer endpoint polynomial kept separate. Adopt fresh isolated whole R973 after root read the complete UC1--UC10 proof, fixed Parts A--D, exact input scopes and the entire independent finding. Root and characteristic_zero_bridge remain contributors. Every finite choice, full-source, raised, cost and actual local-mask obligation passed; the independent reviewer contributed no repair and the distinct outer-polynomial limitation remains explicit. No original residue evaluation, old-primary affine rank, full sign solution, irreducible realization or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete paid admissible-source theorem](#statement) | Parts A--D: actual starting witness and finite choices without original admissibility, full source/root/canonical preservation, exact and enlarged degree/gap/layer costs, raised normalization, actual endpoint mask and distinct outer-polynomial limits. |
| argument | [Entire UC1--UC10 proof](#complete-argument) | Full unit exponent, B7 degree repair, explicit two-candidate rho table, all-primary source and canonical recomputation, preserved exact fresh3, optimized396Q cost, complete synthetic factors and algebraic endpoint application with all unresolved realization boundaries. |
| dependency | [Adopted original complete doubled-precision source](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | DG1--DG8 and Sections3/5: actual bounded whole-row Y, Q/m/H_aux/B_src, original full finite jets/root/canonical/gap/layer data and selected fresh order with exact triple factor. The new witnesses receive NEW enlarged bounds. |
| dependency | [Adopted complete finite unit and row source](Yin_C_G0664_v1.md#decision-whole-reviewed-2026-10-24) | HG7 full finite-unit exponent and G4--G5 actual complete row domain and safe B-index period; the needed safe exponent is also proved directly in UC1. No source exponent vector or native rank is evaluated. |
| dependency | [Adopted full ordinary-row and fresh mechanism](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Complete ordinary/divided row products, both global forward maps, multiplicity-floor and fresh-order separation, and complete integer trace-factor/layer/Haar interface with every multiplicity. |
| dependency | [Adopted whole-row class and invisible extension theorem](Yin_C_G0751_v1.md#decision-whole-reviewed-2026-10-25) | WR1--WR11: exact pre-fresh exponent convention, reciprocal z4 class, small invisible ordinary row with its safe period and fresh-factor separation, and actual full-source reconstruction. The new simultaneous degree/exponent choices and396Q budget are proved here. |
| dependency | [Adopted explicit local endpoint mask and descent theorem](Yin_C_G0747_v1.md#decision-whole-reviewed-2026-10-25) | Structural reflection basis and exact J(1) parity at admissible a=d-3, with actual source conditions verified here; old-source overlap and exact raised height1 descent. Its special complete-multiplier budget is not transferred to the arbitrary outer endpoint factor. |
| review | [Fresh independent whole paid admissible-source review](../audits/reviews/Yin_R_G0973_v1.md#whole-paid-admissible-source-finding) | Entire fixed Parts A--D and UC1--UC10, every actual starting witness and finite choice, full source/root/canonical and raised data, optimized396Q cost, complete synthetic layer, actual endpoint mask and separate outer-polynomial scope; independently reviewed with exact statement and argument bindings. |

