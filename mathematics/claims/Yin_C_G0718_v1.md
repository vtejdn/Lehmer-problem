---
author: Yin
---

# Actual full-primary modulo512 control from the strong original integer factors

Human author Yin.
Provenance: project deduction with the actual coefficient and monic-module inputs below.
Root proposed that the same seven-eighth and three-quarter factors might control several later bits, and suggested checking the genuine dyadic half rather than relying on a valuation heuristic.
Salem_completion derived the exact Delta expansion and the complete coefficient/module proof below.
This is separate new author mathematics; it is not an amendment to the fixed C717 review target.
The actual component setting and original full forward inputs are the generic SF1 domain of [C717](Yin_C_G0717_v1.md#statement), now with q>=256; that candidate remains pending independent review, while all needed component mathematics is proved directly here.
C694's actual monic-local module conventions and C675's Delta mechanism were directly read; no external result or native computation is used.

## Statement

### H512.1. Exact bounded statement

Let H_b0=X^aY_b, a>=2 even, with Y_b monic prime to Xphi and Y_b dividing both Y_b(chi) and Y_b(X^3+X), where phi=X^2+X+1 and chi=Xphi^2 over F_2.
Choose fixed monic integer lifts P_psi for every FULL psi^(n_b,psi) of H_b0, with P_X=X, and form H_b.
For any dyadic q>=256 set A=aq, H_0=H_b0^q, S=(H_bPhi^(7a))^(q/2), U=H_0phi^(7A), d=degU, and Phi=X^2+X+1 over Z.
For ANY actual integer K,W with

    degK<d-2A, degW<d,
    H_b^(7q/8)|K, H_b^(3q/4)|W over Z,
    T=S^2+2Phi^AK+4W,

define the ACTUAL canonical integer polynomials, for either sign s separately,

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a_T=rem_T T(C_2)/2, b_T=rem_T T(C_3)/3,
    c_T=rem_T T(C_5)/5,
    F(T)=rem_T(2c_T^2-3a_T^5),
    X_s(T)=rem_T(b_T^2-a_T^3+s(c_T^3-2b_T^5)).

The coefficient half for a_T is integral because T(C_2)=T^2 modulo2; the odd quotients are integral by the analogous congruences modulo3 and5.
Each remainder uses the SAME actual monic divisor T.
Then on EVERY full H_0-primary in the actual localized quotient modulo512,

    a_T=0 modulo64, b_T^2=c_T^2=0 modulo512,
    F(T)=X_s(T)=0 modulo512.                       (H512.1)

No phi root, old8a support, global residual congruence, source multiplicity floor, irreducibility or integral-closure valuation premise is used.
The coefficients and all original multiplicities are retained.
This is a primary-component statement and does not imply global modulo512.

## Complete argument

### H512.2. Actual module filtration and composition precision

Fix psi, N=q n_b,psi and z=P_psi^(N/8).
Write S=z^4s, P=Phi^AK=z^7p and W=z^6w as ACTUAL integer factors, with u=s^2 a unit in the psi localization of(Z/512Z)[X]/T.
The SAME divisor relation is

    z^8=-2z^7(p/u)-4z^6(w/u).                     (H512.2)

It implies directly in this module, for every integer j>=7,

    z^j belongs to2^(j-7)Q_psi,                   (H512.3)

with2^rQ_psi={0} for r>=9.
For j=7 the assertion is tautological, and for j=8 it follows from H512.2.
For j>=9 multiply H512.2 by z^(j-8); the two terms are2z^(j-1) and4z^(j-2), whose induction exponents both give j-7.
This proves the statement without assigning a valuation to z or replacing the monic coefficient ring by an integral closure.
Its reduction gives the same filtration in the corresponding quotient modulo64 or128.

The elementary actual-power bound used here is: if 2^r divides m, then(B+2E)^m=B^m modulo2^(r+1).
For1<=j<=m, binom(m,j)=(m/j)binom(m-1,j-1) gives valuation at least r-v_2(j); the extra2^j contributes j, and j-v_2(j)>=1.
Thus every error term has the claimed coefficient divisibility, including j=m.
This is a polynomial coefficient statement over Z.

For C_3 and C_5, full binary forward divisibility gives an ACTUAL monic division H_b(C_i)=P_psi^(n_b,psi)R_i+2E_i.
At the endpoint q=256, the exponents q/2,7q/8,3q/4 have2-adic valuations7,5,6 respectively, and these only increase with q.
Therefore

    S(C_i)=z^4r_i modulo256,
    P(C_i)=z^7t_i modulo64,
    W(C_i)=z^6v_i modulo128, i=3,5.               (H512.4)

The extra factors Phi(C_i) and the actual quotient K/H_b^(7q/8) or W/H_b^(3q/4) introduce no denominator or smaller coefficient precision.
For C_2, H_b(C_2)bar=H_b0^2, so its ACTUAL division by P_psi^(2n_b,psi) has even remainder.
The same exponent bounds give

    P(C_2)=z^14t_2 modulo64,
    W(C_2)=z^12v_2 modulo128.                      (H512.5)

All these compositions take place on the full original integer polynomials, before reduction or localization.

### H512.3. Odd divided remainders and their complete squares

Using H512.4 in the actual numerator S(C_i)^2+2P(C_i)+4W(C_i) gives, modulo128 in the SAME quotient,

    i a_i=z^8r_i^2+2z^7t_i+4z^6v_i,

where a_3=b_T and a_5=c_T.
The actual monic divisor multiple is zero in this quotient, and division by i is multiplication by an odd unit.
Substitute H512.2 to obtain

    b_T=2z^7B+4z^6C modulo128,
    c_T=2z^7D+4z^6E modulo128.                       (H512.6)

For either expression the square modulo512 is

    4z^14B^2+16z^13BC+16z^12C^2.

The three coefficient/module divisibilities from H512.3 are at least2^(2+7),2^(4+6),2^(4+5), respectively, so every term is zero modulo512.
The omitted128-multiple contributes only cross terms divisible by512, because the displayed representative is even, and a square divisible by16384.
This proves both square conclusions with their full multiplicities.

### H512.4. The legitimate dyadic polynomial and exact Delta identity

For any integer polynomial B put Delta(B)=(B(C_2)-B^2)/2; its coefficients are integers by reduction modulo2.
Write S=F_0^m with F_0=H_bPhi^(7a) and m=q/2.
The ACTUAL expansion F_0(C_2)=F_0^2+2Delta(F_0) shows

    Delta(S)=sum_(j=1)^m binom(m,j)
                    F_0^(2(m-j))2^(j-1)Delta(F_0)^j.

Because m is a power of2, binom(m,j) has valuation at least v_2(m)-v_2(j), so each displayed coefficient has valuation at least v_2(m)+j-1-v_2(j)>=v_2(m).
Therefore Delta(S) is coefficientwise divisible by m=q/2, in particular by128 at q>=256.
No half of a zero class has been selected.

The canonical a_T is exactly rem_T Delta(T): if T(C_2)=TQ_2+2a_T, then Q_2bar=Tbar and the integer quotient(Q_2-T)/2 supplies this identity.
Expanding Delta(T) over Z and substituting only the SAME actual relation S^2=-2P-4W gives the exact class

    a_T=P(C_2)+2W(C_2)+2P^2+8PW+8W^2
                     -4PDelta(S)-8WDelta(S)+2Delta(S)^2. (H512.7)

For clarity the starting identity is Delta(S^2)=2S^2Delta(S)+2Delta(S)^2, while expansion of T^2 retains the terms4S^2P,8S^2W,4P^2,16PW and16W^2.
Their substitution yields precisely the five displayed non-Delta terms and their signs; no canonical-divisor term is discarded by taking an illegal half.

Modulo64, every Delta(S) term vanishes by its ACTUAL coefficient divisor.
The first two remaining terms are z^14t_2 and2z^12v_2 by H512.5.
The other three are2z^14p^2,8z^13pw and8z^12w^2.
Their module divisibilities from H512.3 are at least128,64,256,512 and256, respectively.
Hence the actual a_T is zero modulo64 in the localized free monic coefficient module.
Equivalently it is a64-multiple in the modulo512 module; these reduction kernels are exact because T is monic and localization preserves them.
Thus a_T^3 and a_T^5 vanish modulo512.
Together with b_T^2=c_T^2=0, this proves H512.1 for both residuals.

### H512.5. Scope for the actual new source

Every strengthened-factor output of candidate C717 has original q>=1048576 and retains its ACTUAL S, Kfactor and Wfactor without a final trace pullback.
If that fixed construction is adopted, the complete generic theorem above therefore gives both non-phi components through512 for that same output and every subsequent actual correction retaining those factors.
It does not by itself construct a global64 or128 input, determine any phi-primary error, or justify moving these factors through a different degree-changing construction.
No independent review of this new512 argument is claimed, and the fixed C717 statement and review scope remain unchanged.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision actual-primary-five-twelve-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T15:26 |
| status | open |
| reason | Register the complete generic actual full-primary512 theorem for every dyadic q>=256 with exact seven-eighth K and three-quarter W factors. The same-divisor module filtration, every C2/C3/C5 composition precision, legitimate coefficient divisor of Delta(S), exact dyadic expansion and complete odd squares prove a64 and both residuals512 on all original H0 primaries. The proof is independent of a passing phi construction; application to the newly fixed C717 source remains conditional on its adoption. No global512 or characteristic-zero claim is made; fresh whole independent review remains outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact generic original-primary theorem](#statement) | H512.1 for every full source factor, any stated K/W and dyadic q>=256, same actual monic divisor, both signs, a64 and complete odd-square/residual512, with no phi or global-residual premise. |
| argument | [Complete coefficient and module proof](#complete-argument) | H512.2--H512.5 and H512.2--H512.7 equations, full local module recurrence, binomial coefficient precision at the actual endpoint, global compositions before localization, odd quotient/square terms, integer Delta(S) divisor and exact Delta(T) class, and stated source-application limits. |
| dependency | [Adopted actual monic-primary module interface](Yin_C_G0694_v1.md#decision-whole-reviewed-2026-10-24) | NP1--NP3 same-divisor localized coefficient conventions, unit denominator from the original full factorization and legitimate monic reduction kernels. All new coefficient precision and filtration conclusions are proved directly here. |
| support | [Adopted actual dyadic mechanism](Yin_C_G0675_v1.md#decision-whole-reviewed-2026-10-24) | MQ3 actual integral Delta identity and canonical same-divisor principle; H512.4 repeats the full integer expansion at the new modulus, without merely rescaling its old conclusion. |
| support | [Pending strong-factor source construction](Yin_C_G0717_v1.md#decision-strong-factors-thirty-two-open) | Comparison and precise conditional source application only: its candidate original q>=1048576 output has the same actual factors and unchanged-degree shape. No existence or other conclusion of that pending construction is a premise of the generic H512 proof. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T15:47 |
| status | proved |
| reason | Adopt the entire generic H512.1 statement and H512.2--H512.5 proof after complete main-agent reading and fresh isolated whole R939. For every stated q>=256 and actual strong-factor input, full global compositions, exact monic-module filtration, complete odd squares, the genuine Delta(S) coefficient divisor and exact Delta(T) identity prove a64 and both residuals512 on every full H0-primary. No passing phi construction or C717 existence theorem is a premise of this generic proof; its separate source application retains that exact boundary. There is no global512, characteristic-zero identity or unrestricted Task conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact generic original-primary theorem](#statement) | H512.1 for every full source factor, any stated K/W and dyadic q>=256, same actual monic divisor, both signs, a64 and complete odd-square/residual512, with no phi or global-residual premise. |
| argument | [Complete coefficient and module proof](#complete-argument) | H512.2--H512.5 and H512.2--H512.7 equations, full local module recurrence, binomial coefficient precision at the actual endpoint, global compositions before localization, odd quotient/square terms, integer Delta(S) divisor and exact Delta(T) class, and stated source-application limits. |
| dependency | [Adopted actual monic-primary module interface](Yin_C_G0694_v1.md#decision-whole-reviewed-2026-10-24) | NP1--NP3 same-divisor localized coefficient conventions, unit denominator from the original full factorization and legitimate monic reduction kernels. All new coefficient precision and filtration conclusions are proved directly here. |
| support | [Adopted actual dyadic mechanism](Yin_C_G0675_v1.md#decision-whole-reviewed-2026-10-24) | MQ3 actual integral Delta identity and canonical same-divisor principle; H512.4 repeats the full integer expansion at the new modulus, without merely rescaling its old conclusion. |
| support | [Pending strong-factor source construction](Yin_C_G0717_v1.md#decision-strong-factors-thirty-two-open) | Comparison and precise conditional source application only: its candidate original q>=1048576 output has the same actual factors and unchanged-degree shape. No existence or other conclusion of that pending construction is a premise of the generic H512 proof. |
| review | [Independent whole actual-primary512 review](../audits/reviews/Yin_R_G0939_v1.md#whole-actual-primary512-finding) | Whole generic statement and complete coefficient/module proof, every full primary and endpoint binomial term, all C2/C3/C5 precisions, odd-square cross terms, legitimate integer Delta half and exact identity, local reduction kernels and conditional source-application limits. |

