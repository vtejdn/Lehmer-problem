---
author: Yin
---

# Explicit simultaneous modulo-four lifts for square characteristic-two data

Human author Yin.
Root developed the square-input half-remainder argument, exact low-odd-coefficient criterion, bounded CRT construction and application to every nontrivial Frobenius power below.
This is author mathematics and has not yet received an independent whole review.
The active [G0001 Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes the continuation.
Focused reuse read the entire adopted C669 actual same-T calculation and C668v2 canonical families, and compared the new generic existential C671 statement.
C671 is not a premise: the square case and its complete counts are proved directly from C669 below.
No native calculation, parameter enumeration or external source theorem is used.

## Statement

Let A>=2 be even, Phi=X^2+X+1 over Z, phi=Phi modulo2, chi=Xphi^2 and Psi=phi(chi).
Let Y in F_2[X] be a monic SQUARE prime to Xphi, and assume

    Y|Y(chi), Y|Y(X^3+X).

Put H_0=X^A Y, U=H_0phi^(7A), h=degH_0, d=h+14A and C_0=X^A Y(chi)Psi^(7A).
Assume the old support identity H_0^6=C_0^21 modulo phi^(4A).
All irreducible multiplicities in H_0 are even and at least2, and Y'=0 gives the required low derivative.
For every irreducible psi|H_0 choose a monic integer lift P_psi, with P_X=X, and use its FULL exponent N_psi to set

    mathcal_H=product_psi P_psi^(N_psi)=X^A mathcal_Y,
    J_H=product_psi psi^(N_psi/2), j_H=degJ_H=h/2.

In particular mathcal_H and mathcal_Y are actual squares in Z[X], not merely squares after reduction.
Let Z be the unique eleventh root of H_0 C_0^2 modulo phi^(3A).
The entire allowed coefficient family is

    Kbar=Z modulo phi^(3A), J_H|Kbar, degK<d-2A,
    T_(K,W)=mathcal_H Phi^(7A)+2Phi^A K+4W, degW<d.       (SQ1)

Every T is monic of degree d with reduction U.
Use its actual monic integer divisions, with C_2=X^2-2, C_3=X^3-3X and C_5=X^5-5X^3+5X,

    a=rem_T(T(C_2))/2, b=rem_T(T(C_3))/3,
    c=rem_T(T(C_5))/5,
    F(T)=rem_T(2c^2-3a^5),
    X_s(T)=rem_T(b^2-a^3+s(c^3-2b^5)), s in{1,-1}.

All residual congruences refer to the coefficients of these actual canonical integer remainders.
For a fixed admissible K, there exists W solving BOTH F(T)=X_s(T)=0 modulo4 if and only if

    [X^i]Kbar=0 for every odd i with A/2<=i<3A/2.         (SQ2)

The criterion is independent of the sign and the integer lift of Kbar.
Whenever it holds, exactly2^(d-3A) distinct coefficient classes T modulo8 above that fixed T modulo4 solve both residuals for either FIXED sign.
The signs have corresponding solution sets, not necessarily identical T solutions.

There is always an admissible K satisfying SQ2.
For example take the coefficient0/1 integer lift of the unique CRT polynomial

    Kbar=Z modulo phi^(3A),
    Kbar=0 modulo J_H X^A,
    degK<j_H+7A<d-2A.                                   (SQ3)

The low condition implies X^(3A/2)|Kbar, so it implies every zero in SQ2.
With n_K=h+6A-j_H, the complete allowed Kbar family has2^n_K elements, and EXACTLY2^(n_K-A/2) of them satisfy SQ2.
Consequently the total number of distinct T modulo8 in SQ1 solving both modulo4 residuals, for either fixed sign, is

    2^(n_K+d-7A/2)>0.                                   (SQ4)

These are modulo8 COEFFICIENT classes satisfying modulo4 residual equations, not solutions of residual equations modulo8.

### Application to the full canonical families

Take ANY canonical polynomial data from adopted C667 with normalized m,H,B,Y_0 and

    U_0=X^(2m)Y_0phi^(14m), R_0=X^(2m)Y_0phi^(12m)B,

and choose any q=2^k with k>=1.
Set U=U_0^q, A=2mq, Y=Y_0^q and h=q(2m+degY_0), d=q(30m+degY_0).
Then the entire square-input theorem applies.
For every such q there are actual monic integer T with T modulo2=U whose SAME divided remainders solve both canonical residuals coefficientwise modulo4, for either chosen sign.
This includes every large dyadic m>=2^70 and the separate m14 family of adopted C668v2, at EVERY q>=2.
The exact fixed-K fiber count is2^(q(24m+degY_0)); the total SQ4 exponent is

    q(36m+3degY_0/2).                                   (SQ5)

It is an integer because q is even.
The actual global maximal Frobenius q of U and R, all original integer layers, full gate and complete canonical degrees remain those of the same C667/C668 data.
The characteristic-two canonical R and its synthetic integer zero-Haar lift stay compatible data; the constructed T is not shown to have that chosen integer lift as its actual G_can.
No q=1 assertion, modulo8 residual solution, characteristic-zero residual identity, irreducibility, total reality, original realization or unrestricted G0001 conclusion follows.

## Argument

### 1. Exact all-primary interface and the legitimate error

All C669 hypotheses hold: A is even, every Y multiplicity is at least2, both forward divisibilities are assumed, the low derivative vanishes identically and the old support is prescribed.
The factorized integer base is exactly its required base, not an arbitrary coefficient lift.
Thus for every K,W in SQ1 the first residual is zero modulo4, the second is even, and both residuals already vanish on every non-phi primary.
Let k=Kbar and work in R=F_2[X]/phi^(3A).
For the actual integer polynomials

    chi_0=X Phi^2, Psi_0=Phi(chi_0),
    C=X^A mathcal_Y(chi_0)Psi_0^(7A),
    D_K=((K(C_2)-K^2)/2)bar+k^2,

perform actual monic division

    sC^3-K^6=Phi^A L_s+2M_s, degM_s<2A.

C669 proves that the remainder is even and L_sbar is divisible by phi^(3A).
Its complete error, with the polynomial division performed before local reduction, is

    eta_s=(L_sbar/phi^(3A))/(H_0 k^3)
       +phi^(2A)(M_sbar/k^4+D_K)
       +C_0^2Psi^A k(chi)/k^4 in R.                    (SQ6)

C669 gives the GLOBAL simultaneous iff Wbar^2=eta_s in R, equivalent to eta_s'=0, and the fixed-K count2^(d-3A).
The first term in SQ6 is the actual changing-divisor term; it remains present throughout this argument.
No local cancellation is substituted for the other primary conditions.

### 2. The actual square base and its integer half-remainder

Since every N_psi is even, write mathcal_Y=mathcal_V^2 over Z and put

    D=X^(A/2)mathcal_V(chi_0)Psi_0^(7A/2).

The exponents are integers and C=D^2 as an exact integer polynomial.
The adopted root consequence is k^6=C_0^3 modulo phi^(4A).
Thus

    (k^3+Dbar^3)^2=0 modulo phi^(4A),
    phi^(2A)|(k^3+Dbar^3).

In particular the integer remainder of K^3-D^3 after monic division by Phi^A is even.
There are actual integer Q,V with K^3-D^3=Phi^A Q+2V.
Squaring this identity BEFORE monic reduction gives

    K^6-D^6
      =Phi^A(2D^3 Q+Phi^A Q^2+4QV)+4D^3 V+4V^2.

Therefore its remainder modulo Phi^A is coefficientwise divisible by4.
For s=+1 this proves M_+bar=0.
For s=-1, subtract the preceding difference to obtain

    M_-bar=rem_(phi^A)(k^6).

The sign is immaterial modulo2.
Since k^6 is a square and phi^A=(phi^(A/2))^2, this remainder is itself a square: divide k^3 by phi^(A/2) and square its quotient/remainder identity.
Hence M_sbar'=0 for BOTH signs as polynomial identities.
This is an integer half-remainder argument; square reduction alone would not justify dividing the original remainder by2.

### 3. Every other derivative term and the exact low criterion

Differentiate the defining root identity k^11=H_0 C_0^2 in R.
The derivative is well-defined since3A is even, and H_0'=0 because H_0 is a square.
Thus k^10 k'=0 and k'=0 in R, since k is a unit there.
For the actual half-difference, differentiation over Z gives

    ((K(C_2)-K^2)/2)'=X K'(X^2-2)-KK'.

After reduction this yields

    D_K'=X(k')^2+kk'=0 in R.                            (SQ7)

No derivative of a quotient by2 is guessed inside characteristic2.

The numerator in the first SQ6 term is

    L_sbar/phi^(3A)=(C_0^3+k^6)/phi^(4A).

It is a square polynomial: the numerator is a square and its exact divisor phi^(4A) is a square.
Its derivative is therefore identically zero.
The derivative of its denominator H_0 k^3 is zero in R by H_0'=0 and k'=0 there, so the full first term has zero derivative in R.
The middle term also has zero derivative by evenness of2A, the square denominator k^4, the integer-remainder result and SQ7.
The prefactor of the final term is a square unit because A is even.
Consequently the COMPLETE remaining derivative is

    eta_s'=C_0^2Psi^A k^(-4) phi^2 k'(chi) in R.         (SQ8)

This formula holds for every admissible K, not only the eventual CRT choice.

Write k=sum_i k_i X^i.
The factor J_H includes X^(A/2), so k_i=0 for i<A/2.
For odd i the contribution of k_i to phi^2 k'(chi) is phi^2 chi^(i-1), of EXACT phi-order2i, since X is a phi-unit.
For i>=3A/2 this term vanishes in R.
The terms from different smaller odd indices have distinct exact orders, so their lowest nonzero one cannot cancel.
The unit prefactor in SQ8 cannot change vanishing.
Thus eta_s'=0 if and only if all the coefficients in SQ2 vanish, proving the exact criterion for every integer lift and either sign.
The already adopted square-image iff then proves simultaneous sufficiency, rather than a necessary derivative bound alone.

### 4. Bounded CRT construction and complete counts

The polynomials J_H X^A and phi^(3A) are coprime, because Y is prime to Xphi.
CRT gives SQ3 with degree below (j_H+A)+6A=j_H+7A.
Since j_H<=h and A>0, this is less than h+12A=d-2A.
The coefficient0/1 lift has the same actual degree, and its X^(3A/2) divisibility implies SQ2.
Taking a square root of eta_s in R fixes Wbar modulo phi^(3A/2); any polynomial representative of degree below d gives an actual integer W and thus a monic T.
This explicitly proves existence without evaluating a huge coefficient list.

For the exact count, let k_* be the CRT representative modulo J_H phi^(3A) of degree below j_H+6A.
Every admissible k has the UNIQUE form

    k=k_*+phi^(3A)J_H V, degV<n_K=h+6A-j_H.

Write J_H=X^(A/2)J_0 with J_0(0)=1.
The factor phi^(3A)J_0 is a unit modulo X^A, so as V ranges over polynomials of degree below A the coefficients of phi^(3A)J_H V through degree below3A/2 range freely over all A low coefficients starting at A/2.
Such V are permitted since n_K>=6A>A.
The A/2 odd coefficient conditions in SQ2 are therefore independent linear equations on the full n_K-dimensional affine family, with2^(n_K-A/2) solutions.
Every one has exactly2^(d-3A) allowed Wbar by C669.
Distinct k give distinct T modulo4, since multiplication by phi^A is injective in the polynomial domain and the resulting degree is below d.
For a fixed integer lift K, distinct Wbar give distinct T modulo8.
Replacing K by K+2V merely translates W by Phi^A V of degree below d, so the count has no duplication from integer representatives.
Multiplying the two fiber counts proves SQ4.
The C669 sign translation gives equal solvability and counts for the two signs without identifying their T classes.

### 5. Actual q and the two adopted synthetic families

For the C667 input and q>=2, Y=Y_0^q is a square and every H_0 exponent is even.
Both forward divisibilities and the old support congruence raise to the q-th power, giving exactly the hypotheses with A=2mq.
The derivative Y'=0 is an identity.
The actual factorized integer lift, with the full q-multiplied exponents, is a square as required; no normalized exponent is substituted in the integer construction.
The full degree is d=q(30m+degY_0), h=q(2m+degY_0), and j_H=h/2.
Thus d-3A=q(24m+degY_0), while

    n_K+d-7A/2=h/2+d+5A/2
               =q(36m+3degY_0/2),

proving SQ5.
The same original U and its canonical characteristic-two R have actual maximal Frobenius power q by their preserved fresh factor of multiplicity3q.
The all-primary characteristic-two remainder, full corrected root/gate and exact original integer layer weights stay unchanged.
The constructed T preserves this U and supplies actual theta_p and both modulo4 canonical residual congruences.
It does not show that the actual integer canonical residual equals the separately chosen G_int; the latter's complete integer factors and Haar mean remain synthetic compatibility data.
C668v2 supplies the normalized canonical inputs for both its complete parameter ranges, so this theorem applies to every q>=2 there, with all original polynomial costs retained.
The q=1 nonsquare case and all higher residual/characteristic-zero conditions remain open.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:37 |
| status | open |
| reason | Register the full square-input same-T modulo4 theorem, exact integer half-remainder, complete derivative criterion, bounded CRT existence and all coefficient counts, with every q>=2 application to the adopted canonical families. This is root author mathematics requiring fresh independent whole review. No native, q1 claim, modulo8 residual solution, original characteristic-zero realization or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire square-input theorem](#statement) | SQ1--SQ5, every even A and square Y in the full stated domain, every allowed K, exact criterion, actual simultaneous T/W existence and counts, every q>=2 canonical application and all limits. |
| argument | [Complete square-input proof](#argument) | Five sections and SQ6--SQ8, integer square and half-remainder, all-primary actual error, exact derivatives and lowest-order separation, globally bounded CRT and all coefficients/fibers, full original normalization and costs. |
| dependency | [Adopted exact same-T modulo4 theorem](Yin_C_G0669_v1.md#decision-whole-reviewed-2026-10-24) | Entire actual factorized-base and all-primary calculation, complete eta with changing-divisor term, root consequence, square-image iff, sign translation and fixed-K count at the verified square-input hypotheses. |
| support | [Canonical data for the application](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Exact U_0/R_0, both forward divisibilities, old support, every full q/layer/root/gate and degree assertion; does not itself supply integer residual solutions. |
| support | [Both adopted complete synthetic families](Yin_C_G0668_v2.md#decision-whole-reviewed-2026-10-24) | Application only: all dyadic m>=2^70 and separate m14 canonical inputs, every q and full costs/zero-Haar compatibility, without assuming G_int=G_can. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T02:45 |
| status | proved |
| reason | Adopt the whole square-input theorem after actual full main readback and fresh isolated whole R893. The integer square and legitimate half-remainder reduce the complete actual obstruction to precisely the stated low odd K coefficients. Bounded CRT supplies actual same-T simultaneous modulo4 solutions, with exact full-family coefficient counts, for every q>=2 canonical input and both C668 families. The counts are modulo8 coefficient classes satisfying modulo4 residuals. The q1 nonsquare case, residuals modulo8, G_int=G_can, characteristic-zero equations and original realization remain unresolved; no Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire square-input theorem](#statement) | SQ1--SQ5, every even A and square Y in the full stated domain, every allowed K, exact criterion, actual simultaneous T/W existence and counts, every q>=2 canonical application and all limits. |
| argument | [Complete square-input proof](#argument) | Five sections and SQ6--SQ8, integer square and half-remainder, all-primary actual error, exact derivatives and lowest-order separation, globally bounded CRT and all coefficients/fibers, full original normalization and costs. |
| dependency | [Adopted exact same-T modulo4 theorem](Yin_C_G0669_v1.md#decision-whole-reviewed-2026-10-24) | Entire actual factorized-base and all-primary calculation, complete eta with changing-divisor term, root consequence, square-image iff, sign translation and fixed-K count at the verified square-input hypotheses. |
| support | [Canonical data for the application](Yin_C_G0667_v1.md#decision-whole-reviewed-2026-10-24) | Exact U_0/R_0, both forward divisibilities, old support, every full q/layer/root/gate and degree assertion; does not itself supply integer residual solutions. |
| support | [Both adopted complete synthetic families](Yin_C_G0668_v2.md#decision-whole-reviewed-2026-10-24) | Application only: all dyadic m>=2^70 and separate m14 canonical inputs, every q and full costs/zero-Haar compatibility, without assuming G_int=G_can. |
| review | [Independent entire square-input finding](../audits/reviews/Yin_R_G0893_v1.md#whole-square-input-mod-four-finding) | Whole SQ1--SQ8 and all five proof sections, exact integer square/half-remainder for both signs, every derivative and changing-divisor term, actual all-primary iff, bounded CRT, full K/W/distinct-T counts and all actual-q canonical applications. |

