---
author: Yin
---
# Earlier coefficient-bit elimination of the first modulo-sixteen obstruction

Human author Yin.
The [current continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-after-account-handoff-2026-10-25) authorizes this work.
The [D1 earlier-bit section](../drafts/Yin_D_G0001.md#earlier-coefficient-bit-question) is development provenance, not a logical premise.

Root proposed varying the earlier coefficient bit and the restricted source Phi^(4A)M.
Same_trace derived the full modulo8 preservation criterion, calculated the first eighth-error from both actual integer divisions, and found the cancellation and surjective lower image.
Root independently supplied the matching cancellation, unit coefficient and exact Phi^A-factor deduction during development.
Same_trace checked the complete hypotheses, all-primary equations, actual factor lifts and degree costs below.
This is author mathematics requiring fresh whole review; it is not an adoption or a full simultaneous modulo16 construction.
The exact [C700 formula](Yin_C_G0700_v1.md#statement) is now [adopted](Yin_C_G0700_v1.md#decision-whole-reviewed-2026-10-25).
Focused reuse also read C202's changing-divisor argument, C603's actual quarter, C689 SX11--SX27, C694 NP1--NP7 and the adopted C699 construction.
The lower coefficient4 changes are proved explicitly below, not inferred by relabelling C689's coefficient8 changes.
No native computation or external theorem is used.

## Statement

### EB1: full input and statements

Retain the complete C689 square-input hypotheses, stated here to fix the actual domain.
Let A be a positive multiple of4, phi=X^2+X+1 over F_2, chi=Xphi^2, Psi=phi(chi), and Phi=X^2+X+1 over Z.
Let Y be a monic square prime to Xphi, with Y dividing both Y(chi) and Y(X^3+X).
Put H_0=X^A Y, h=degH_0, d=h+14A, U=H_0phi^(7A), and C_0=X^A Y(chi)Psi^(7A).
Assume h>=17A and H_0^6=C_0^21 modulo phi^(4A).
Retain every full even exponent n_psi of H_0, choose fixed monic integer lifts P_psi with P_X=X, and set

    H=product P_psi^(n_psi), J_H=product psi^(n_psi/2),
    S=product P_psi^(n_psi/2)Phi^(7A/2),
    P=Phi^A K, T=S^2+2P+4W,
    degK<d-2A, degW<d, k=Kbar,
    k^11=H_0 C_0^2 modulo phi^(4A), J_H|k,
    [X^i]k=0 for odd A/2<=i<3A/2.                    (EB1)

Fix s in{1,-1} and define the actual canonical integer polynomials

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a=rem_T(T(C_2))/2,
    b=rem_T(T(C_3))/3, c=rem_T(T(C_5))/5,
    F(T)=rem_T(2c^2-3a^5),
    X_s(T)=rem_T(b^2-a^3+s(c^3-2b^5)).

Assume F(T)=X_s(T)=0 coefficientwise modulo8.
All subsequent quotients by2,4 or8 are taken on their indicated actual integer coefficients before reduction.
For integer B define Delta(B)=(B(C_2)-B^2)/2.
Write B_phi=F_2[X]/phi^(7A), B_H=F_2[X]/H_0 and E_F=(F(T)/8)bar.

ALL degree-d monic coefficient classes modulo16 above T modulo4 that retain both modulo8 residuals have the unique form

    T_{M,Z}=T+4Phi^(4A)M+8Z modulo16,
    degm<d-8A, degz<d,
    M and Z the coefficient0/1 lifts of m and z,      (EB2)

where m,z satisfy

    [X^(2j+1)]m=0 for 0<=j<3A/4,
    z^2=phi^(2A)(k/H_0)m^2+Omega m(chi)
                           modulo phi^(3A),
    Omega=C_0^2Psi^(4A)/k^4.                         (EB3)

There is no restriction on z in B_H.
For each admissible m there are exactly2^(d-3A) classes z; hence EB2 has2^(2d-47A/4) classes.
Arbitrary actual integer lifts can be used instead of the coefficient lifts, with the corresponding carry absorbed in the next coefficient bit.
An additional16R affects neither modulo8 preservation nor F modulo16.

For these classes the EXACT lower first-error change is

    E_F(T_{M,Z})+E_F
      =phi^A k^11m/H_0^2+phi^(4A)k^10m^2/H_0^2
        +phi^(2A)k^9z^2/H_0+phi^(3A)k^10z/H_0
                                      modulo phi^(9A/2). (EB4)

Equivalently, after the EB3 cancellation, it is

    phi^A k^11m/H_0^2
      +phi^(2A)k^5C_0^2Psi^(4A)m(chi)/H_0
      +phi^(3A)k^10z/H_0 modulo phi^(9A/2).           (EB5)

The complete lower image in EB4 is EXACTLY phi^A modulo phi^(9A/2).
More strongly, the full set of first errors E_F(T_{M,Z}) in B_phi, as EB2--EB3 vary, is exactly the ideal phi^A B_phi.
Every such first error vanishes on B_H.
In particular there always exists an actual monic polynomial T_dagger of the SAME degree with

    T_dagger=T modulo4,
    F(T_dagger)=0 modulo16,
    X_s(T_dagger)=0 modulo8.                         (EB6)

This improves the first-error question by allowing the earlier coefficient bit; it does not assert that any fixed modulo8 class satisfies C689 SX4.
It also does not solve X_s modulo16.

For the stronger actual-factor inputs of C699, let

    J_2=product P_psi^(n_psi/2),
    J_3=product P_psi^(3n_psi/4),
    all n_psi divisible by4,
    J_3|K and J_2|W over Z.                          (EB7)

Then EB6 can be obtained with the SAME K and an actual W_dagger still divisible by J_2, within degW_dagger<d.
Consequently both residuals of T_dagger vanish modulo16 on every H_0-primary by C694 NP7.
The second phi-primary error, including its low part below phi^(4A), remains to be evaluated.
No derivative-divisibility refinement is claimed for these earlier-bit corrections.


## Argument

### EB2: necessity of the source and every modulo8-preserving class

Start with an arbitrary actual change T+4V+8Z, degV,degZ<d, and write v=Vbar.
The exact division T(C_2)=TQ_2+2a gives

    a(T+4V)=a+2H_V,
    H_V=rem_(T+4V)(V(C_2)-VQ_2), H_Vbar=v^2.        (EB8)

The odd quotients change by multiples of4.
The raw residual's change of divisor contributes a multiple of4 and hence vanishes modulo4.
Thus the second residual changes modulo4 by2alpha^2v^2, whereas the first changes by2alpha^4v^2=0, where alpha=abar.
On B_H alpha=0, and on B_phi alpha=phi^(2A)k^2 with k a unit.
Therefore retaining X_s modulo4 requires precisely phi^(3A/2)|v.
The8Z correction cannot alter that necessity.

For the first quarter C603 FE4, with K fixed and W changed to W+V, gives exactly

    delta O_F=Psi_F(v),
    Psi_F(v)=phi^(2A)k^9v^2/H_0
                         +phi^(3A)k^10v/H_0.         (EB9)

Its applicability requires F(T+4V)=0 modulo4, already verified.
On B_H C694 NP2 gives F=0 modulo16 for every W.
An8Z change leaves F modulo8 unchanged because alpha^4=0.
For v=phi^(3A/2)u, EB9 is

    phi^(9A/2)k^10/H_0*(u+t u^2), t=phi^(A/2)/k.

Modulo phi^(5A/2) the additive map N(u)=t u^2 has N^3=0, so I+N has inverse I+N+N^2.
Consequently Psi_F(v)=0 is equivalent to v=0 modulo phi^(4A).
This establishes the necessity of EB2, with no condition on the H_0 components.
Conversely any such v preserves both residuals modulo4 and F modulo8.
Because v is the full polynomial representative of degree<d, write v=phi^(4A)m with degm<d-8A.
Choose the actual V=Phi^(4A)M; the difference from any other lift of v is even and is absorbed in8Z.

Now put T_1=T+4Phi^(4A)M.
It remains to calculate its second quarter without assuming X_s modulo8.
Use the actual integer quotients

    T(C_5)=TQ_5+5c,
    b^2-a^3+s(c^3-2b^5)=TQ_X+X_s(T),
    Delta(T)=TQ_D+a, Q_2=T+2Q_D.

The exact odd changing-divisor identity gives c(T_1)=c+4J_5, with J_5bar=rem_U(v(chi)-vQ_5bar).
Its integer quotient is legitimate since5 divides rem_(T_1)(V(C_5)-VQ_5).
The b-square and b-fifth-power changes vanish modulo8 because bbar=0.
Expansion of -(a+2H_V)^3 retains the extra quadratic term -12aH_V^2.
After dividing the canonical difference by4, that extra term reduces to alpha v^4, which is zero: alpha=0 on B_H, while v^2=0 on B_phi.
The cubic term is divisible by8.
The entire quarter change is therefore

    delta O_X=(rem_T(a^2H_V)/2)bar
                           +gamma^2J_5bar+Q_Xbar v, (EB10)

where gamma=cbar.
The first remainder is even since alpha^2v^2=0.
Replacing its divisor T_1 by T changes it by a multiple of4 and therefore does not change its coefficient half modulo2.
This verifies the additional lower-bit terms rather than silently importing SX22.

Since Phi(C_2)^(4A)=Phi^(8A) modulo4, the SAME relation H Phi^(7A)=-2Phi^AK-4W yields

    H_V=-2Phi^(2A)K M(C_2)/H
                         -2Phi^(4A)M Q_D modulo4.

Multiplying by a^2 and taking the legitimate half gives phi^(6A)k^5m^2/H_0 on B_phi, exactly as in the actual calculation SX23.
The full polynomial identities

    phi^(2A)k^2=alpha+Uq_a,
    phi^(2A)C_0=gamma+UQ_5bar,
    UQ_Xbar=alpha^3+gamma^3

give the complete quotient cancellation of C689 SX24: (Q_Xbar+gamma^2Q_5bar)v=0 in B_phi.
Here k^6=C_0^3 modulo phi^(4A) follows from the old support and the eleventh-root relation, as proved in C689 SX2.
No local phi-class is composed with C_5; V(C_5) comes from the full integer polynomial and reduces to Psi^(4A)m(chi).
We obtain

    delta O_X=phi^(6A)k^5m^2/H_0
                  +phi^(4A)C_0^2Psi^(4A)m(chi).     (EB11)

On all H_0-primary components X_s(T_1)=0 modulo8 by C694 NP2.
The shared8Z change, now legitimately applied to the actual modulo4 base T_1, adds alpha^2z^2 by C202.
Therefore simultaneous modulo8 preservation is exactly the square equation in EB3.

Differentiating the eleventh-root relation gives k'=0 modulo phi^(4A), because H_0, C_0^2 and the modulus are squares.
Thus k/H_0 is square modulo phi^(3A), and Omega is a square unit there.
The first term on the right of EB3 is always square.
The derivative of the second is

    Omega phi^2 sum_(j>=0) m_(2j+1)chi^(2j).

For j<3A/4 its summands have distinct orders2+4j below3A; all later terms vanish.
Consequently it is zero exactly under the coefficient conditions in EB3.
Derivative zero is equivalent to square membership in this even-precision quotient, and each root has2^(d-3A) global representatives of degree<d.
The stated count and uniqueness of the two binary coefficient bits follow.
The actual changing-divisor identity for an additional16R changes a by8r^2 modulo16 and the odd quotients by multiples of16, so X_s modulo8 and F modulo16 are unchanged, the latter using alpha^4=0.

### EB3: both actual integer half-remainders in the first eighth change

Write H=X^A Y_1^2 over Z and define chi_0=X Phi^2, Psi_0=Phi(chi_0), and C=X^A Y_1(chi_0)^2Psi_0^(7A).
Use the exact C700 definitions, with this same H,K,W:

    H C^2+3K^11=Phi^(3A)L+2M_F, degM_F<6A,
    Xi=Delta(P)+P^2+W(C_2)-2PDelta(S)+Delta(S)^2,
    N=-Phi^AKL+H Phi^(4A)M_F
                +3H Phi^(3A)K^10W-H Phi^(2A)K^9Xi,
    N=Phi^(7A)L_N+2M_N, degM_N<14A.                 (EB12)

These are actual monic integer divisions and both remainders are even.
Write w=Wbar, xi=Xibar and p_5=P(C_5)bar.
The first pair L,M_F is independent of W.
For T_1=T+4Phi^(4A)M, let V=Phi^(4A)M.
Then Xi changes by V(C_2) and the actual numerator changes by

    N_1-N=3H Phi^(3A)K^10 V-H Phi^(2A)K^9V(C_2).

The integer congruence Phi(C_2)^(4A)=Phi^(8A) modulo4 gives

    N_1-N=Phi^(7A)
          [3HK^10M-H Phi^(3A)K^9M(C_2)] modulo4.

Monic division by the SAME fixed Phi^(7A) therefore proves

    (M_(N,1)-M_N)bar=0,
    (L_(N,1)-L_N)bar=H_0k^10m+H_0phi^(3A)k^9m^2.  (EB13)

In particular no half of a characteristic-two remainder has been chosen.
The next canonical-divisor carry in C700 is essential: multiplying the second equation by phi^A k/H_0^3 produces BOTH terms

    phi^A k^11m/H_0^2+phi^(4A)k^10m^2/H_0^2.

The remaining change in C700 FE16.3 is

    v Lbar/H_0^2
      +phi^A k^8(wv^2+v xi+v^3)/H_0
      +phi^(6A)k^6v^4.

The given root relation implies Lbar is divisible by phi^A.
Since v=phi^(4A)m, every term in this last display has order at least5A, and hence vanishes modulo phi^(9A/2).
This proves EB4 for the4V part.

The subsequent8Z part must also retain its actual canonical quotient, even if T_1 only satisfies X_s modulo4.
Write its exact first raw division and even fourth-power remainder as

    2c_1^2-3a_1^5=T_1Q_F+F(T_1),
    a_1^4=T_1Q_4+2R_4.

The exact change a_new=a_1+4H_Z and the raw first expansion modulo16 give

    delta E_F=R_4bar z^2+Q_Fbar z.

The genuine divisor change supplies Q_Fbar z.
The legitimate fourth-power half and polynomial quotient, as computed in C689 SX13--SX16, are phi^(2A)k^9/H_0 and phi^(3A)k^10/H_0 on B_phi and zero on B_H.
Their proof uses F(T_1)=0 modulo8 and the unchanged square-input data, not X_s(T_1)=0 modulo8.
This proves the8Z terms of EB4 in precisely the needed domain.
Substitution of EB3 cancels the two phi^(4A)k^10m^2/H_0^2 terms and proves EB5.
All lower terms in EB5 have order at least A.
The calculation is unchanged by higher integer lifts: a change M by2M' adds8Phi^(4A)M', which is in the first-error kernel, and a change Z by2Z' adds16Z'.

### EB4: exact image, automatic initial divisibility and the actual construction

Choose rho with

    rho^2=k/H_0 modulo phi^(3A),
    rho defined modulo phi^(3A/2).

Such a root exists by the derivative calculation above.
Restrict to the full-polynomial condition X^(3A/2)|m.
Then m(chi)=0 modulo phi^(3A), so EB3 is solved by

    z=phi^A rho m modulo phi^(3A/2).                 (EB14)

The remaining freedom in z is the ideal phi^(3A/2) and alters E_F only at order9A/2 or higher.
Equation EB5 becomes

    delta E_F=phi^A D_* m modulo phi^(9A/2),
    D_*=k^11/H_0^2+phi^(3A)k^10rho/H_0.              (EB15)

The coefficient D_* is fixed independently of m and is a unit modulo phi^(7A/2).
The choice of rho beyond its specified precision has no effect on EB15.
The coprime moduli X^(3A/2) and phi^(7A/2) have total degree17A/2, strictly less than d-8A=h+6A.
Therefore m can satisfy its zero low-X condition and any desired high residue modulo phi^(7A/2).
This proves that the lower image is exactly phi^A modulo phi^(9A/2), not merely a contained subspace.

We next evaluate the invariant below phi^A from the ACTUAL integer data, without presuming it is zero.
Every term of N in EB12 is divisible by Phi^A over Z.
Writing N=Phi^A N_0, actual monic division gives

    rem_(Phi^(7A))(N)=Phi^A rem_(Phi^(6A))(N_0).

Its evenness forces the second remainder on the right to be even as well, since reduction modulo2 and polynomial cancellation by the nonzero phi^A are valid.
Thus M_N is EXACTLY divisible by Phi^A over Z.
Also Lbar is divisible by phi^A from the fixed root modulo phi^(4A).
Finally J_H|k implies X^(A/2)|k, so p_5=Psi^A k(chi) is divisible by phi^A as a full binary polynomial.
Every summand of C700 FE16.3 consequently has order at least A.
Hence

    E_F belongs to phi^A B_phi.                     (EB16)

This argument applies to every W for which F is divisible by8 and the unchanged EB1 data hold.
No extra X^(3A/2) factor on k and no high-q hypothesis is needed.
On B_H the error is zero by C694 NP3.

To construct EB6, prescribe

    m=(E_F/phi^A)/D_* modulo phi^(7A/2),
    m=0 modulo X^(3A/2),                            (EB17)

using the actual coefficient eighth E_F and exact division allowed by EB16.
Choose M of that degree, choose Z with EB14, and set T_2=T+4Phi^(4A)M+8Z.
Then both residuals are still divisible by8 and E_F(T_2) is divisible by phi^(9A/2), with zero B_H component.
Apply the exact C689 first-error inverse SX5--SX6 at this actual T_2: an8Phi^(3A/2)U_1 correction kills the remaining first error and keeps both residuals modulo8.
Its degree is below8A<d.
The resulting T_dagger satisfies EB6.

For any other target in phi^A B_phi, replace the numerator E_F in EB17 by the desired lower difference, then use the same C689 inverse to prescribe the higher difference.
This proves the stated full image phi^A B_phi.
Necessity of its lower bound follows from EB16 on each actual output, and the all-primary first conclusion follows from C694.

### EB5: actual factor retention, original costs and the remaining interface

Under EB7, replace the lower condition in EB17 by

    m=0 modulo j_2 X^(3A/2), j_2=J_2bar.

This stronger condition still implies X^(3A/2)|m and is prime to phi.
The two CRT moduli have total degree h/2+17A/2, which is strictly less than h+6A because h>=17A.
After obtaining m, factor it by the actual reduced lower modulus and lift the quotient; this gives an integer M exactly divisible by J_2 X^(3A/2) with the same degree and high reduction.
An unmodified coefficient lift is not presumed to have that integer factor.
Thus V=Phi^(4A)M is actually J_2-divisible and has degree<d.

Choose z by EB14 and additionally z=0 modulo j_2.
Its representative has degree<h/2+3A, and an actual J_2-divisible lift Z has that same bound.
The updated W+V+2Z therefore remains exactly divisible by J_2.
For the final C689 inverse, prescribe the high class of U_1 modulo phi^(5A/2) and impose U_1bar=0 modulo j_2.
The representative degree is<h/2+5A; choosing its actual J_2-divisible lift makes8Phi^(3A/2)U_1 have degree<h/2+8A<d.
It too changes W by an actually J_2-divisible polynomial.
K never changes, so J_3|K persists, and C694 NP7 gives both residuals modulo16 on every H_0-primary.

All changes are multiples of4, retain the same U and actual degree d, and do not replace its original full multiplicities by normalized exponents.
For a paid original construction, its original q, integer layers, degree and canonical gap remain exactly those of the selected input; no additional support or degree cost is introduced here.
For example C699's d=q(30m+degY_b) and gap q(5m-Q-5degH_aux) remain unchanged, where H_aux denotes its normalized complement parameter rather than the integer H in EB1.
The theorem does not retain an unproved characteristic-zero equality between an independently selected integer cyclotomic lift and the actual canonical remainder.
It does not assert an original trace realization or any Mahler estimate.

The concrete gain is actual F modulo16 together with X_s modulo8, in the original degree and modulo4 coefficient class.
For the factor-compatible inputs the second non-phi errors are already zero modulo16.
The actual second phi error below phi^(4A) and its remaining higher compatibility have not been evaluated by this argument.
Earlier-bit factor lifts are not asserted to preserve T' modulo16 or to make that new second eighth-error square.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:30 |
| status | open |
| reason | Register the complete earlier-coefficient theorem: all modulo8-preserving classes over a fixed modulo4 input, exact actual eighth variation with both integer half-remainders, the full first-error image phi^A, automatic initial divisibility and unchanged-degree F16/X8 existence. The stronger actual-factor construction retains both non-phi residuals16. The second phi error is not eliminated and no complete modulo16 or original realization is asserted. Fresh isolated whole review remains required. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Earlier-bit theorem](#statement) | Full EB1--EB7 input, all coefficient classes and count, lower and full first-error images, unconditional first16/second8 correction and exact-factor corollary, with every unchanged-degree and remaining limit. |
| argument | [Complete author argument](#argument) | EB8--EB17 and EB2--EB5: actual lower-bit expansions, extra quadratic term, both quotient carries and integer half-remainders, square-image criterion, unit CRT construction, automatic Phi^A factor, all actual lift/degree costs. |
| dependency | [Actual coupled modulo8 correction](Yin_C_G0202_v1.md#argument) | Exact changing-divisor identity and the shared8Z map at the actual modulo4 base; no unsupported higher-precision extrapolation. |
| dependency | [Actual first quarter](Yin_C_G0603_v1.md#statement) | FE4 under fixed K and changed W, deriving necessity of the complete phi^(4A) lower-bit source. |
| dependency | [Full next-layer input and inverse](Yin_C_G0689_v1.md#statement) | Complete input, SX10--SX27 root and polynomial quotient interfaces, legitimate fourth-power half, exact first-error kernel/image and final first-error inverse; the new coefficient4 terms are proved here. |
| dependency | [Both actual first-eighth halves](Yin_C_G0700_v1.md#statement) | FE16.1--FE16.10, both even integer remainders and actual canonical-divisor carries, specialized and differenced explicitly in EB3--EB4. |
| dependency | [All non-phi components and actual factors](Yin_C_G0694_v1.md#statement) | NP2--NP3 for all W at the full square-input scope, and NP7 for the retained exact J3/J2 factors. |
| support | [Existing compatible actual inputs](Yin_C_G0699_v1.md#statement) | CP1--CP4 supplies the actual factor-compatible inputs; original q, full support, integer layers and degree/gap costs remain unchanged. CP5 derivative control is not presumed to survive the new lower-bit changes. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:39 |
| status | proved |
| reason | Adopt the entire fixed earlier-bit theorem after main reading of C702 and isolated independent whole R923. The complete modulo8-preserving classes/count above the original modulo4 input, both actual half/carry terms, exact first-error image phi^A, automatic initial membership and same-degree F16/X8 construction are checked. The actual J3/J2 factor corollary retains both non-phi residuals modulo16 with every degree cost paid. No second phi success, preserved derivative enhancement, simultaneous modulo16 or original realization is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Earlier-bit theorem](#statement) | Full EB1--EB7 input, all coefficient classes and count, lower and full first-error images, unconditional first16/second8 correction and exact-factor corollary, with every unchanged-degree and remaining limit. |
| argument | [Complete author argument](#argument) | EB8--EB17 and EB2--EB5: actual lower-bit expansions, extra quadratic term, both quotient carries and integer half-remainders, square-image criterion, unit CRT construction, automatic Phi^A factor, all actual lift/degree costs. |
| dependency | [Actual coupled modulo8 correction](Yin_C_G0202_v1.md#argument) | Exact changing-divisor identity and the shared8Z map at the actual modulo4 base; no unsupported higher-precision extrapolation. |
| dependency | [Actual first quarter](Yin_C_G0603_v1.md#statement) | FE4 under fixed K and changed W, deriving necessity of the complete phi^(4A) lower-bit source. |
| dependency | [Full next-layer input and inverse](Yin_C_G0689_v1.md#statement) | Complete input, SX10--SX27 root and polynomial quotient interfaces, legitimate fourth-power half, exact first-error kernel/image and final first-error inverse; the new coefficient4 terms are proved here. |
| dependency | [Both actual first-eighth halves](Yin_C_G0700_v1.md#statement) | FE16.1--FE16.10, both even integer remainders and actual canonical-divisor carries, specialized and differenced explicitly in EB3--EB4. |
| dependency | [All non-phi components and actual factors](Yin_C_G0694_v1.md#statement) | NP2--NP3 for all W at the full square-input scope, and NP7 for the retained exact J3/J2 factors. |
| support | [Existing compatible actual inputs](Yin_C_G0699_v1.md#statement) | CP1--CP4 supplies the actual factor-compatible inputs; original q, full support, integer layers and degree/gap costs remain unchanged. CP5 derivative control is not presumed to survive the new lower-bit changes. |
| review | [Fresh independent whole earlier-bit finding](../audits/reviews/Yin_R_G0923_v1.md#whole-earlier-bit-finding) | Entire fixed EB1--EB17 statement and argument, all actual earlier-bit expansions/halves/carries, complete classes and images, full CRT and factor degrees, exact direct-input applicability and retained limitations. |

