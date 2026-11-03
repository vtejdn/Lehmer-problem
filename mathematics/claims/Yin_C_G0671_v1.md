---
author: Yin
---
# An exact existential coefficient invariant for simultaneous modulo-four residuals

Human author Yin.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Root proposed the complete phi^(3A) variation and its derivative under the fixed eleventh root.
Same_trace checked the exact integer remainder, all lift choices and the entire coefficient space, proved the full image with bounded global preimages, and derived the existential invariant and exact fibers below.
These are author contributions, not independent review.
Focused reuse of adopted C669 supplies the all-primary actual residual calculation, square-image criterion, sign translation and fixed-K count.
The new issue is eliminating the quantifier over ALL admissible K.
The direct half-difference identities and finite polynomial coefficient calculation suffice; no new source theorem, native computation or parameter enumeration is used.

The [D1 existential section](../drafts/Yin_D_G0001.md#existential-same-t-mod4-invariant) retains development provenance and is not a proof dependency.
This whole theorem is initially open for fresh isolated whole mathematical review.

## Statement

Let A>=2 be EVEN, Phi=X^2+X+1 over Z, phi=Phi mod2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be monic and prime to Xphi, with every occurring irreducible multiplicity at least2, and assume

    Y|Y(chi), Y|Y(X^3+X), X^(2A)|Y'.

Put H_0=X^A Y, U=H_0phi^(7A), h=degH_0, d=h+14A, and C_0=X^A Y(chi)Psi^(7A).
Assume H_0^6=C_0^21 modulo phi^(4A).
Choose a monic integer lift P_psi of every irreducible psi|H_0, with P_X=X, using its FULL exponent N_psi to define

    mathcal_H=product_psi P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product_psi psi^(ceil(N_psi/2)), j_H=degJ_H.

Thus J_H=X^(A/2)J_0 with J_0(0)=1 and j_H<=h.
Let Z be the unique unit eleventh root of H_0C_0^2 modulo phi^(3A).
The COMPLETE coefficient family considered here is

    Kbar=Z modulo phi^(3A), J_H|Kbar, degK<d-2A,
    T_(K,W)=mathcal_H Phi^(7A)+2Phi^A K+4W, degW<d.       (EK1)

The degree bound applies to the actual integer K.
Every T_(K,W) is monic of degree d with reduction U.
Set C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X, and use the SAME monic integer divisor T=T_(K,W) to define

    a=rem_T(T(C_2))/2, b=rem_T(T(C_3))/3,
    c=rem_T(T(C_5))/5,
    F(T)=rem_T(2c^2-3a^5),
    X_s(T)=rem_T(b^2-a^3+s(c^3-2b^5)), s in{1,-1}.

All residual congruences mean coefficientwise congruences of these actual canonical remainders.
For each K use the concrete definitions

    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    C=X^A mathcal_Y(chi_0)Psi_0^(7A),
    D_K=((K(C_2)-K^2)/2)bar+Kbar^2,
    sC^3-K^6=Phi^A L_s+2M_s, degM_s<2A,
    eta_s(K)=(L_sbar/phi^(3A))/(H_0 Kbar^3)
       +phi^(2A)(M_sbar/Kbar^4+D_K)
       +C_0^2Psi^A Kbar(chi)/Kbar^4
                      in R=F_2[X]/phi^(3A).             (EK2)

The L_s,M_s definition uses ACTUAL monic integer division by Phi^A with its even remainder.
The quotient L_sbar/phi^(3A) is an exact polynomial quotient before reduction, and all denominators are units in R.
Adopted C669 proves these facts, F(T)=0 modulo4 for every W, and the all-primary equivalence

    F(T)=X_s(T)=0 modulo4 iff Wbar^2=eta_s(K) in R.       (EK3)

Let K_* be the coefficient0/1 lift of the unique CRT representative Z modulo phi^(3A), zero modulo J_H, of degree<6A+j_H.
Define

    n_K=h+6A-j_H,
    Omega=C_0^2Psi^(4A)/K_*bar^4 in R,
    S_A={f in R:f'=0},
    I_A=span_F2{Omega phi^2 chi^(i-1):
                         i odd, A/2<=i<3A/2}.           (EK4)

The derivative is well-defined because3A is even.
The space S_A is both the square image and the derivative image in R, with dimension3A.
Omega is a square unit and I_A is a subspace of S_A of dimension A/2.
The quotient S_A/I_A therefore has dimension5A/2.
Define

    O(U,mathcal_H)=[eta_s(K_*)'] in S_A/I_A.             (EK5)

This class is independent of s, of the integer lift of an admissible base K, and of the admissible base representative used to compute it.
The specified factorized mathcal_H remains part of the input.

For either sign, there exist K,W in EK1 solving both residuals modulo4 if and only if O(U,mathcal_H)=0.
Equivalently eta_s(K_*)' belongs to the explicit subspace I_A.
If O=0, precisely2^(n_K-A/2) of the2^n_K admissible Kbar classes admit W, each with precisely2^(d-3A) monic T classes modulo8 above its fixed modulo4 class.
The total number of distinct T modulo8 in the entire family solving the two residuals for either FIXED sign is

    2^(n_K+d-7A/2) if O=0, and0 otherwise.              (EK6)

The two signs have equivalent existence and equal counts, without asserting the same T solves both.

This is a necessary-and-sufficient criterion within the entire explicitly stated family EK1, not a classification of every possible monic lift of U.
Its zero or nonzero value on C667's candidate data remains to be established.
Actual Frobenius q, all original integer layers and degree costs retain their roles as spelled out in EK6.
No modulo8 residual sufficiency, characteristic-zero realization or original A_0 exclusion is claimed.

## Argument

### EK2: complete variation at the required precision

Take integer K_1=K_0+Phi^(3A)L with both in EK1, and write k=K_0bar and ell=Lbar.
Their denominators in EK2 are identical in R.
The difference of sC^3-K_1^6 and sC^3-K_0^6 is divisible by Phi^(3A) over Z, so their ACTUAL remainders after division by Phi^A coincide exactly.
Thus M_s(K_1)=M_s(K_0).
Writing mathscr_L_s=L_sbar/phi^(3A), the binomial expansion modulo2 gives

    mathscr_L_s(K_1)+mathscr_L_s(K_0)
       =phi^(2A)k^4 ell^2+phi^(8A)k^2 ell^4
                           +phi^(14A)ell^6.

Only the first term survives in R.
The division by phi^(4A) precedes truncation; its order2A contribution is retained.

For Delta_2(P)=(P(C_2)-P^2)/2, use Delta_2(P+Q)=Delta_2(P)+Delta_2(Q)-PQ.
The product rule and evenness of3A give Delta_2(Phi^(3A))bar=0.
For delta=Phi^(3A)L this yields

    D_(K_0+delta)+D_(K_0)
      =phi^(6A)Delta_2(L)bar+phi^(3A)k ell
                              +phi^(6A)ell^2 modulo2.

This has phi-order at least3A, so its contribution to EK2 vanishes in R.
Finally delta(chi)bar=Psi^(3A)ell(chi).
The complete identity is therefore

    eta_s(K_1)+eta_s(K_0)
       =phi^(2A)(k/H_0)ell^2+Omega ell(chi) in R.        (EK7)

Omega can be computed with any admissible base because their k agree in R.
Differentiate k^11=H_0C_0^2 in R.
The modulus has zero derivative, giving k^10 k'=H_0'C_0^2, and division by the root identity gives k'/k=H_0'/H_0.
Hence(k/H_0)'=0 in R.
The first term of EK7 has zero derivative; Omega'=0 because Omega is a square unit.
Since chi'=phi^2,

    eta_s(K_1)'+eta_s(K_0)'
                        =Omega phi^2 ell'(chi) in R.    (EK8)

This is the full3A-precision variation, with no omitted half-difference term.

### EK3: integer lifts and the entire global coefficient space

For any integer V with K+2V still satisfying the degree bound,

    T_(K+2V,W)=T_(K,W+Phi^A V),

and the translated W has degree<d.
Comparing C669's full half-errors on the two sides and cancelling their common factor phi^(4A)Kbar^4 against modulus phi^(7A) gives

    eta_s(K+2V)+eta_s(K)=(phi^A Vbar)^2 in R.           (EK9)

This comparison uses the actual residual formula, not an assumed solution.
Its derivative is zero, so the obstruction only depends on Kbar.
C669's sign identity eta_-+eta_+=(phi^A Kbar)^2 likewise has zero derivative.

Every admissible Kbar has a UNIQUE expression

    Kbar=K_*bar+phi^(3A)J_H V,
                             V in F_2[X], degV<n_K.     (EK10)

Indeed the difference is divisible by the coprime moduli phi^(3A),J_H, and the allowed degree is<d-2A=h+12A.
The CRT base has smaller degree, so exact polynomial division gives n_K=h+6A-j_H.
Conversely every V with that bound gives an admissible Kbar.
This covers all2^n_K classes.
Lift J_H and V coefficientwise and take K=K_*+Phi^(3A)L with L their product to get an integer representative with the same degree bound; EK9 handles every other integer lift.

### EK4: exact image and globally bounded preimages

Write ell=J_H V=X^(A/2)J_0V=sum_i ell_i X^i.
Equation EK8 becomes

    Omega phi^2 ell'(chi)
      =sum_(i odd, A/2<=i<3A/2)
                       ell_i Omega phi^2 chi^(i-1).     (EK11)

Indices below A/2 are absent because of J_H.
Indices at least3A/2 have phi-order2i>=3A and vanish.
The displayed vectors have distinct EXACT phi-orders2i<3A, since Omega and X are units at phi.
They are linearly independent over F_2.
There are A/2 odd integers in this half-open interval of length A.

For any specified coefficients c_i at those odd indices put

    P(X)=sum_(i odd, A/2<=i<3A/2)c_i X^(i-A/2),
    V_P=rem_(X^A)(J_0^(-1)P), ell_P=J_H V_P.           (EK12)

The inverse is modulo X^A, where J_0(0)=1.
Thus degV_P<A and ell_P has exactly the specified coefficients through degree<3A/2, with all other coefficients there zero.
Since n_K>=6A>A, this parameter is globally allowed in EK10.
For the coefficientwise integer lift L_P of ell_P,

    degell_P<j_H+A,
    deg(K_*+Phi^(3A)L_P)<h+7A<h+12A=d-2A.

Every primary constraint remains valid: J_H|ell_P and the root residue is unchanged.
This proves that the FULL variation image is exactly I_A, and gives a bounded polynomial preimage for each vector.

Represent classes of R by polynomials of degree<6A.
Their derivatives are precisely all polynomials in even powers of degree<6A.
These are also precisely the representatives with zero derivative and precisely the square image.
Thus dim S_A=3A; EK11--EK12 give dim I_A=A/2 and dim(S_A/I_A)=5A/2.
In particular eta_s(K_*)' is in S_A.

### EK5: existential equivalence, independence and fiber counts

All possible eta_s(K)' form the affine space eta_s(K_*)'+I_A.
The linear map from the n_K-dimensional parameter space in EK10 onto I_A has rank A/2, so each value has2^(n_K-A/2) preimages.
The affine space contains zero if and only if EK5 vanishes.
By adopted C669, zero derivative is equivalent to the square image and hence to one shared W solving both actual residuals.
This proves sufficiency as well as necessity.

If O=0, express eta_s(K_*)' in the displayed basis and apply EK12 to construct one soluble K; adding the kernel of EK11 gives all soluble classes.
Obtain W by taking a polynomial square root of eta_s(K) modulo phi^(3A/2), then any degree<d representative with that residue.
All other primary conditions are already settled for every such K by C669.

Changing the admissible base adds an element of I_A and leaves Omega unchanged in R.
Changing its integer lift or sign has zero derivative by EK9 and the sign identity.
This proves the stated independence of EK5, without changing Y or the specified factorized mathcal_H.

For each soluble Kbar, C669 gives2^(d-3A) choices of Wbar among the2^d degree<d classes.
Distinct admissible Kbar give distinct T modulo4: their difference divided by2 is Phi^A(Kbar_1+Kbar_0), nonzero of degree<d.
For one fixed integer representative K, distinct Wbar give distinct T modulo8.
Changing that representative only translates W by EK9, so there is no double counting.
The product of the two exact fiber counts is EK6.

### EK6: actual input, original costs and remaining obligation

The result eliminates K and W within the COMPLETE stated family EK1, without assuming this family classifies every possible monic lift of U.
It does not prove that O vanishes for C667's canonical candidates, or that it is nonzero for all of them.
Determining or structurally controlling this exact invariant for those actual Y remains open.
The quotient dimension5A/2 counts ambient obstruction coordinates, not necessarily the set of invariants realized as Y varies.

If U=U_0^q comes from C667 with U_0=X^(2m)Y_0phi^(14m), use A=2mq, Y=Y_0^q, H_0=(X^(2m)Y_0)^q and d=q(30m+degY_0).
Forward divisibility and old support raise to the q-th power.
The low derivative X^(2A)|Y' follows from the original condition for q=1 and from Y'=0 for q>1.
Every exponent in J_H, n_K, the root precision and the counts belongs to this actual U; no smaller q or quotient field is inferred.
Any full C649 gate and integer-layer data prescribed for the same U/Y remain attached to that input throughout EK10 and are not substituted for either actual residual.
The original layer weight12mq, canonical degree gap q(5m-Q-5degH), maximal normalization and synthetic integer G_int remain exactly at their C667 scopes.
No equality of G_int with the actual G_can of T is asserted.
A successful modulo4 reconstruction gives neither the separate modulo8 conditions, characteristic-zero residual equations, irreducible reciprocal nontorsion P, total reality nor an original realization.
No new original A_0 exclusion or Task completion is claimed.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:30 |
| status | open |
| reason | Register the complete existential K/W criterion at actual modulo4 precision, full error variation, exact rank A/2 and obstruction quotient, globally bounded preimages, integer-lift/base/sign independence and all coefficient fiber counts. The invariant is not evaluated on all canonical candidates. No native calculation, original exclusion or higher-modulus/characteristic-zero realization is claimed. Fresh isolated whole review is required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire existential criterion](#statement) | EK1--EK6, every actual even A and complete stated U, specified integer factorized base, actual residuals, full K family, finite obstruction iff, independence, exact counts and original limits. |
| argument | [Whole variation and reconstruction](#argument) | EK7--EK12 and the complete EK2--EK6 proof sections, exact integer remainder and half-difference, full3A variation, all K/lifts, exact image, bounded preimages, fibers and original costs. |
| dependency | [Adopted actual fixed-K calculation](Yin_C_G0669_v1.md#statement) | Entire explicit polynomial domain, actual all-primary first residual and eta half-error, square-image iff, derivative equivalence, sign translation and fixed-K fiber count. |
| dependency | [Exact fixed-K proof](Yin_C_G0669_v1.md#argument) | MT2--MT5, actual changing-divisor half and phi^(4A)K^4 cancellation used for lift independence; no unstated residual-coordinate freedom. |
| support | [Canonical candidate input](Yin_C_G0667_v1.md#statement) | EK6 application only: actual U_0^q, forward support, derivative/root data, maximal q, prescribed layers and all paid costs; no invariant evaluation or original realization is imported. |
| support | [Full formal gate](Yin_C_G0649_v1.md#statement) | The optional full CRT/gate data attached to the fixed U/Y remain unchanged during coefficient variation; they are not assumed to force the new invariant to vanish. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:39 |
| status | proved |
| reason | Adopt the complete existential coefficient theorem after full main reading and fresh isolated whole R892. The full actual error variation, all integer lifts and admissible coefficient classes, exact image rank A/2, bounded global preimages and precise fibers give a necessary-and-sufficient obstruction for the entire specified K/W family. Its value on canonical candidates is not determined by this theorem. The factorized integer base, actual q and every degree/layer remain fixed; no general monic-lift classification, higher-modulus residual solution or characteristic-zero realization is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire existential criterion](#statement) | EK1--EK6, every actual even A and complete stated U, specified integer factorized base, actual residuals, full K family, finite obstruction iff, independence, exact counts and original limits. |
| argument | [Whole variation and reconstruction](#argument) | EK7--EK12 and the complete EK2--EK6 proof sections, exact integer remainder and half-difference, full3A variation, all K/lifts, exact image, bounded preimages, fibers and original costs. |
| dependency | [Adopted actual fixed-K calculation](Yin_C_G0669_v1.md#statement) | Entire explicit polynomial domain, actual all-primary first residual and eta half-error, square-image iff, derivative equivalence, sign translation and fixed-K fiber count. |
| dependency | [Exact fixed-K proof](Yin_C_G0669_v1.md#argument) | MT2--MT5, actual changing-divisor half and phi^(4A)K^4 cancellation used for lift independence; no unstated residual-coordinate freedom. |
| support | [Canonical candidate input](Yin_C_G0667_v1.md#statement) | EK6 application only: actual U_0^q, forward support, derivative/root data, maximal q, prescribed layers and all paid costs; no invariant evaluation or original realization is imported. |
| support | [Full formal gate](Yin_C_G0649_v1.md#statement) | The optional full CRT/gate data attached to the fixed U/Y remain unchanged during coefficient variation; they are not assumed to force the new invariant to vanish. |
| review | [Independent entire existential finding](../audits/reviews/Yin_R_G0892_v1.md#whole-existential-coefficient-invariant-finding) | Whole EK1--EK12 and all statement/proof sections, actual integer remainder and complete3A variation, lift/base/sign independence, full K space, exact image and bounded preimages, every fiber/distinct-T count and original-q application. |

