---
author: Yin
---
# An explicit first eighth-error with both actual canonical-divisor carries

Human author Yin.
Root developed this integer calculation under the [renewed G0001 continuation](../tasks/Yin_T_G0001_v1.md#decision-resume-until-two-percent-remaining-2026-10-25).
This is author mathematics awaiting independent whole review.
The [C603 first quarter](Yin_C_G0603_v1.md#statement), [C675 MQ9--MQ12 representatives](Yin_C_G0675_v1.md#argument) and [C689 next first-error image](Yin_C_G0689_v1.md#statement) were actually read before proof investment.
They supply the earlier precision and actual representatives, not the next integer half and two-divisor formula proved here.
The common content decision selects a new fixed C for this missing substantive calculation, without a duplicate process draft.
No native computation or new external theorem is used.

## Statement

Let A>=2 be even, Phi=X^2+X+1 over Z and phi its reduction.
Let Y_1 be monic over Z with reduction prime to Xphi, and put

    H=X^A Y_1^2, H_0=Hbar, h=degH, d=h+14A,
    S=X^(A/2)Y_1 Phi^(7A/2), U=H_0phi^(7A).

Choose integer K,W with degK<d-2A, degW<d and phi not dividing k=Kbar.
Set P=Phi^A K and T=S^2+2P+4W, an actual monic degree-d polynomial of reduction U.
Define the ACTUAL canonical integer polynomials

    a=rem_T(T(C_2))/2, c=rem_T(T(C_5))/5,
    F=rem_T(2c^2-3a^5),
    C_2=X^2-2, C_5=X^5-5X^3+5X.

Assume every coefficient of F is divisible by8.
No second-residual, forward-divisibility or characteristic-zero realization assumption is imposed.
Let Delta(B)=(B(C_2)-B^2)/2 and set

    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    C=X^A Y_1(chi_0)^2 Psi_0^(7A), P_5=P(C_5),
    Xi=Delta(P)+P^2+W(C_2)-2PDelta(S)+Delta(S)^2.     (FE16.1)

These are ACTUAL integer polynomials; write their reductions C_0,p_5,xi and put w=Wbar.
Perform these TWO specified monic INTEGER divisions:

    H C^2+3K^11=Phi^(3A)L+2M, degM<6A,
    N=-Phi^A K L+H Phi^(4A)M
                  +3H Phi^(3A)K^10W-H Phi^(2A)K^9Xi,
    N=Phi^(7A)L_N+2M_N, degM_N<14A.                 (FE16.2)

Both remainders are even, as proved below.
In B_phi=F_2[X]/phi^(7A), the actual coefficient eighth E_F=(F/8)bar is

    E_F=M_Nbar/H_0^2+phi^A k L_Nbar/H_0^3
          +w Lbar/H_0^2+phi^A k^8 w xi/H_0
          +phi^(6A)k^6 xi^2+phi^(2A)C_0 p_5+p_5^2. (FE16.3)

All denominators are units.
The term involving L_N is the next canonical-divisor carry; wL retains the preceding carry at this precision.
Define the binary polynomial

    N_F=H_0 M_Nbar+phi^A k L_Nbar+H_0 w Lbar
           +phi^A H_0^2 k^8 w xi+phi^(6A)H_0^3 k^6 xi^2
           +phi^(2A)H_0^3 C_0 p_5+H_0^3 p_5^2.      (FE16.4)

For EVERY integer 0<=r<=7A,

    E_F=0 modulo phi^r iff phi^r divides N_F.        (FE16.5)

At r=7A this is exactly the first-residual modulo16 test at phi, with no conclusion at other primaries.
If additionally X^(3A/2) divides k as a full binary POLYNOMIAL, then for every integer 0<=r<=9A/2 the test simplifies to

    phi^r divides H_0 M_Nbar+phi^A k L_Nbar
                      +H_0 w Lbar+phi^A H_0^2 k^8 w xi. (FE16.6)

For a complete C689 input with this extra X factor, SX4's first phi-image test is exactly FE16.6 with r=9A/2.
No claim is made that arbitrary C689 low odd-coefficient conditions imply the stronger X factor.
The other primary test and all second-residual conditions remain separate.
No chosen input is proved to pass this formula; increasing q or old support is not presumed to force it.

## Complete argument

### 1. Integer representatives at the required precision

The congruences C_p=X^p modulo p and actual monic division prove the integrality of a,c.
The exact expansion of Delta(S^2+2P+4W), using Delta(S^2)=2S^2Delta(S)+2Delta(S)^2 and then the SAME relation S^2=-2P-4W, gives

    a=P^2+2Xi modulo8.                               (FE16.7)

This is the universal C675 MQ9 expansion and uses no forward assumption.
Let E_5=(C_5-chi_0)/2 and R_5=S(chi_0)E_5S'(chi_0)+E_5^2S'(chi_0)^2.
Integer Taylor expansion and squaring give S(C_5)^2=S(chi_0)^2+4R_5 modulo8.
Since S(chi_0)^2=Phi^(2A)C exactly and5 is its inverse modulo8,

    c=5Phi^(2A)C+2P_5+4[W(C_5)+R_5] modulo8.         (FE16.8)

Work in Q_16, the localization of (Z/16Z)[X]/T at polynomials whose reductions are prime to phi.
Its reduction is B_phi and H is a unit.
FE16.7 gives abar=phi^(2A)k^2, so abar^4=0 and a^4 belongs to2Q_16.
Replacing a by its modulo8 representative changes a^5 by40a^4 times a class modulo16, hence by zero because a^4 is even.
All higher terms vanish as well.
Replacing c by its modulo8 representative changes2c^2 by a multiple of32.
Therefore FE16.7--FE16.8 suffice for F modulo16, although neither is asserted as a modulo16 representative of a or c separately.

### 2. Complete binomial expansions and the first divisor reduction

Expanding over the integers yields

    -3(P^2+2Xi)^5=-3P^10+2P^8Xi+8P^6Xi^2 modulo16,
    2[5Phi^(2A)C+2P_5+4(W(C_5)+R_5)]^2
        =2Phi^(4A)C^2+8Phi^(2A)CP_5+8P_5^2 modulo16.

All C5 correction terms have coefficient divisible by16 after the factor2 is included.
The actual relation H Phi^(7A)=-2Phi^A K-4W gives in Q_16

    -3P^10=6Phi^(4A)K^11/H+12Phi^(3A)K^10W/H,
    2P^8Xi=-4Phi^(2A)K^9Xi/H-8Phi^A K^8WXi/H.

Modulo4 these formulas give F=2Phi^(4A)(HC^2+3K^11)/H.
F=0 modulo4 and the exact free-module annihilator ann(2)=2Q_4 imply phi^(4A)(H_0C_0^2+k^11)=0 modulo phi^(7A).
Consequently phi^(3A) divides H_0C_0^2+k^11 in the polynomial domain.
Thus the remainder in the FIRST actual division FE16.2 is even.
This verifies the earlier C603 mechanism directly at the present hypotheses.

Substituting that division into the full modulo16 expression gives

    F=4B+8D in Q_16,
    B=-Phi^A K L/H^2+Phi^(4A)M/H
                   +3Phi^(3A)K^10W/H-Phi^(2A)K^9Xi/H,
    D=-WL/H^2-Phi^A K^8WXi/H
                   +Phi^(6A)K^6Xi^2+Phi^(2A)CP_5+P_5^2. (FE16.9)

In particular -8WL/H^2 is retained: it comes from reducing2Phi^(7A)L/H by the SAME actual T.
The numerator H^2B is exactly N in FE16.2.
No canonical remainder is replaced by a single root evaluation.

### 3. The second even remainder and the globally legitimate eighth

The quotient by monic T is free over Z/16Z.
Its exact annihilator identities ann(2^j)=2^(4-j)Q_16 persist under localization, which preserves kernels and images.
Since F has actual coefficients divisible by8, FE16.9 shows4B belongs to8Q_16.
This implies B belongs to2Q_16: if4B=8b, then B-2b belongs to ann(4)=4Q_16.
Hence Nbar=H_0^2 Bbar=0 in B_phi, and the SECOND actual monic remainder in FE16.2 is even.
Both L_N and M_N are thus uniquely specified integer polynomials.

Using this division and the SAME T again gives

    B=Phi^(7A)L_N/H^2+2M_N/H^2
      =-2Phi^A K L_N/H^3-4W L_N/H^3+2M_N/H^2.

Its legitimate half therefore has reduction

    (B/2)bar=phi^A k L_Nbar/H_0^3+M_Nbar/H_0^2.      (FE16.10)

This local half is unique modulo2 because ann(2)=8Q_16 is contained in2Q_16.
Finally FE16.9 and ann(8)=2Q_16 give (F/8)bar=(B/2)bar+Dbar.
Here F/8 is the globally defined actual coefficient eighth; the local calculation computes its reduction rather than inventing a half of a characteristic-two class.
Substitution proves all seven FE16.3 terms and both canonical-divisor carries.
Multiplication by the unit H_0^3 proves FE16.4--FE16.5, including r=0 and r=7A.

### 4. Full-polynomial X constraint and exact low test

The reduced composition is p_5=phi(chi)^A k(chi), where chi=Xphi^2 and phi(chi) is prime to phi.
The full-polynomial condition X^(3A/2)|k implies phi^(3A)|k(chi), hence phi^(3A)|p_5.
The last three FE16.3 terms have respective phi-orders at least6A,5A and6A.
They therefore vanish at every integer0<=r<=9A/2, and unit multiplication by H_0^3 yields exactly FE16.6.

A full C689 input has the actual square factorization H=X^A Y_1^2 and the same canonical a,c,F.
Its F8 and phi-unit k conditions match this theorem.
With the explicitly added X^(3A/2) factor, its first phi-image test is FE16.6 at r=9A/2.
This is a complete calculation of that test, not evidence that it vanishes for any particular earlier K,W choices.
The non-phi first condition, both second conditions, original layers, degree costs, synthetic/canonical equality and characteristic-zero realization remain separate obligations.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision first-eighth-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T05:29 |
| status | open |
| reason | Register the complete actual first eighth-error with two legitimate integer half-remainders, both canonical-divisor carries, the full seven-term local formula, every phi-order iff and exact lower-X four-term truncation. No first-image test is claimed to pass, and no other primary or second residual is silently discharged. The author-complete proof awaits fresh independent whole review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete first-eighth theorem](#statement) | FE16.1--FE16.6, all stated square inputs with F8, both even integer remainders, exact seven-term error and polynomial criterion, every r and the full-polynomial lower-X specialization with its limits. |
| argument | [Entire integer proof](#complete-argument) | FE16.7--FE16.10 and Sections1--4: sufficient representative precision, full binomial expansion, both same-divisor reductions, exact localized annihilators and globally legitimate eighth, all order/truncation and C689 hypothesis matching. |
| support | [Earlier first-quarter mechanism](Yin_C_G0603_v1.md#statement) | Existing first integer J division and lower-precision quarter; the extra integer numerator, second half and full eighth are proved here without attributing them to C603. |
| support | [Actual dyadic and C675 representatives](Yin_C_G0675_v1.md#argument) | Universal MQ9--MQ12 expansions at the exact square-factorized base, reconstructed here with modulo16 sufficiency; no strong-forward whole theorem is imported. |
| dependency | [Next first-error image](Yin_C_G0689_v1.md#statement) | Application only: SX4 phi^(9A/2) condition restricted to actual inputs with the extra X^(3A/2) factor; no passing test, non-phi result or second-error implication is inferred. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T06:16 |
| status | proved |
| reason | Adopt the already preserved fresh independent whole R921 after the responsible main agent read its complete actual finding under the renewed continuation. All FE16.1--FE16.10, integer representative precisions, both even remainders and canonical-divisor carries, legitimate localized eighth and every order criterion are supported at their exact scope. The four-term low test computes the first phi obstruction but proves no particular input passes; other primaries, second residuals and original realization remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete first-eighth theorem](#statement) | FE16.1--FE16.6, all stated square inputs with F8, both even integer remainders, exact seven-term error and polynomial criterion, every r and the full-polynomial lower-X specialization with its limits. |
| argument | [Entire integer proof](#complete-argument) | FE16.7--FE16.10 and Sections1--4: sufficient representative precision, full binomial expansion, both same-divisor reductions, exact localized annihilators and globally legitimate eighth, all order/truncation and C689 hypothesis matching. |
| support | [Earlier first-quarter mechanism](Yin_C_G0603_v1.md#statement) | Existing first integer J division and lower-precision quarter; the extra integer numerator, second half and full eighth are proved here without attributing them to C603. |
| support | [Actual dyadic and C675 representatives](Yin_C_G0675_v1.md#argument) | Universal MQ9--MQ12 expansions at the exact square-factorized base, reconstructed here with modulo16 sufficiency; no strong-forward whole theorem is imported. |
| dependency | [Next first-error image](Yin_C_G0689_v1.md#statement) | Application only: SX4 phi^(9A/2) condition restricted to actual inputs with the extra X^(3A/2) factor; no passing test, non-phi result or second-error implication is inferred. |
| review | [Independent whole first-eighth finding](../audits/reviews/Yin_R_G0921_v1.md#whole-first-eighth-finding) | Entire fixed statement and proof, all integer halves and carries, every r and extra full-polynomial X-factor application, with exact direct-input and remaining limits; independently reviewed. |
