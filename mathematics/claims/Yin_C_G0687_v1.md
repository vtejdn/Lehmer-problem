---
author: Yin
---

# A zero-correction gate prevents a stronger old support jet at the homogeneous endpoint

Human author Yin.
Root derived the actual gate-to-cube obstruction below as sole contributor.
This is an author-checked project deduction, initially open for fresh isolated whole review, under the [active G0001 Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
The [C643v2 sharp homogeneous-cube theorem](Yin_C_G0643_v2.md#statement) and its complete endpoint argument were directly read.
The new step is to force a sufficiently long square low jet from the stronger old relation itself, rather than assume global squareness of Y or a freely chosen high-precision root.
No native computation, new source acquisition or external result is used.
The responsible fixed Claims retain the original gate and its sharp cube classification but not this stronger-support obstruction.

## Statement

Work over F_2 and put phi=X^2+X+1, chi=X phi^2 and Psi=phi(chi).
Let m>=1 be an integer and Q a power of2 satisfying

    2m<Q<=4m.

Let H in F_2[t] be monic with H(0)=1 and5degH<5m-Q.
Put B=X^(Q-m)H(chi), so B is a phi-unit and degB<4m.
Let Y in F_2[X] satisfy Y(0)=1 and gcd(Y,phi)=1, with no assumed global square property, factor completeness or degree bound.
Define the actual polynomials

    H_0=X^(2m)Y,
    C_00=X^(2m)Y(chi)Psi^(14m),
    D_0=H_0B+C_00^3.

Assume the zero-correction gate precision

    phi^(8m) divides D_0.                                  (ZG1)

Then

    phi^(4Q) does NOT divide H_0^6+C_00^21.                (ZG2)

In particular, it is impossible simultaneously to retain ZG1 and strengthen the old support relation to phi^(16m).
This is a statement about every actual polynomial Y in the displayed domain, not only a selected complete representative or a particular formal lift.
No assumption X^(4m)|Y' is required.

The full C649 gate with S=0 implies ZG1 because its eleventh-root factor is a phi-unit at the specified precision.
Consequently its Q<=4m branches obey ZG2.
For the adopted C668v2 branch m=14,Q=32,H=W_3W_21,S=0, every such Y retains the proved old relation at precision112 but fails the stronger precision128; a proposed precision224 is therefore impossible.
At Q=4m the forbidden precision is exactly16m.
These conclusions do not refute a canonical residual lift modulo16, which need not impose this additional old-support strengthening.
They do not exclude the Q>4m branch, change an actual maximal Frobenius power, or establish an original characteristic-zero obstruction or Task completion.

## Argument

Write C=C_00 and work in the phi-adic completion when using inverses or cube roots.
The polynomials B,C,H_0 are phi-units: Y is prime to phi, Y(chi) has residue Y(0)=1, and Psi has residue1.
Suppose, for a contradiction, that H_0^6+C^21 is divisible by phi^(4Q).

### 1. The actual gate forces a square class for C

From H_0B=C^3+D_0 the characteristic-two sixth-power expansion gives the EXACT identity

    H_0^6 B^6+C^18=C^12 D_0^2+C^6 D_0^4+D_0^6.

Every term on the right is divisible by phi^(16m) by ZG1.
Adding B^6(H_0^6+C^21) therefore shows

    C^18(1+B^6 C^3) in (phi^(4Q)),

because4Q<=16m.
Since C is a unit, this yields

    (B^2 C)^3=1 modulo phi^(4Q).                          (ZG3)

There is a unique cube-one unit gamma in the phi-adic completion with the residue of B^2 C, and ZG3 implies B^2 C=gamma modulo phi^(4Q).
For completeness, the three nonzero residues lie in F_4^*.
Each root of Z^3-1 lifts uniquely through every phi-power, because its derivative is Z^2, a unit; equivalently, successive coefficient equations have a unique solution.
If two units with the same residue have equal cubes modulo phi^n, their difference times a unit is zero modulo phi^n, since u^2+uv+v^2 has nonzero residue.
Thus the conclusion at the full4Q precision uses neither a chosen independent root nor a weaker root precision.

Formal differentiation is continuous on this completion: differentiation of a term divisible by phi^n has order at least n-1.
Differentiating gamma^3=1 gives gamma'=0, because gamma is a unit.
Both B^(-2) and the even power phi^(4Q) have zero derivative.
The congruence C=gamma B^(-2) modulo phi^(4Q) consequently gives

    C'=0 modulo phi^(4Q).                                (ZG4)

This step does not infer global squareness of C from a local equality.

### 2. The forced low square jet is long enough

The exponents2m and14m are even, and chi'=phi^2.
Thus the actual polynomial derivative is

    C'=X^(2m)Psi^(14m)Y'(chi)phi^2.

If Y'=0 the following conclusion is immediate.
Otherwise let e=ord_XY'.
Every nonzero coefficient of a derivative over F_2 has even exponent, so e is an even nonnegative integer.
Since chi=Xphi^2 and the constant term of X^(-e)Y' is1, its value at chi is a phi-unit.
Hence the exact order is

    ord_phi C'=2e+2.

Equation ZG4 gives e>=2Q-1.
Evenness of e strengthens this to e>=2Q.
Therefore all odd coefficients of Y of degree below2Q vanish, and there is a polynomial L in F_2[t], L(0)=1 and degL<Q, such that

    Y=L(X)^2 modulo X^(2Q).

Substitution into the ACTUAL C gives

    C=Q_aux^2 modulo phi^(4Q),
    Q_aux=X^m Psi^(7m)L(chi).                            (ZG5)

The modulus is paid by chi^(2Q), which has phi-order4Q.
No higher coefficient of Y has been discarded at a precision where it could contribute.
Combining ZG3 and ZG5 gives

    ((B Q_aux)^3+1)^2=0 modulo phi^(4Q).

Since phi is irreducible, exact square valuations give

    (B Q_aux)^3=1 modulo phi^(2Q).                        (ZG6)

### 3. The sharp homogeneous endpoint is impossible

Put m_star=Q/2, an integer since Q>2m>=2.
Set

    f=X^m B=X^Q H(chi),
    A(t)=phi(t)^(7m)L(t).

Then A(0)=1, f is a phi-unit, X^(m_star) divides f, and

    deg f=m+degB<5m<5m_star.

Also ord_Xf=Q=2m_star.
Equation ZG6 is exactly

    [f A(chi)]^3=1 modulo phi^(4m_star).

The adopted C643v2 homogeneous-cube classification applies at this ACTUAL parameter m_star and degree domain.
Its sharp endpoint requires ord_Xf>2m_star, whereas this f has equality.
This contradiction proves ZG2.
The classification includes all auxiliary A coefficients, so allowing new higher coefficients in Y cannot evade the argument.

### 4. Precise applications and remaining scope

Since4Q<=16m, divisibility by phi^(16m) would imply the forbidden divisibility by phi^(4Q).
For a C649 zero-correction gate, multiplication by the local inverse of its unit root yields D_0=0 modulo phi^(8m), independently of the representative of that root.
At m=14,Q=32 the forbidden exponent is128, and the already adopted exponent is112; the statement does not identify the greatest possible intermediate exponent for every Y.
At Q=4m the exponents4Q and16m agree.

The failed proposal is to add a stronger old support jet while preserving this actual zero-correction gate and homogeneous endpoint range.
A higher canonical residual congruence has its own changing-divisor and coupled-coefficient conditions and does not require that proposal.
No impossibility of modulo16 residuals, Q>4m, an original remaining multiplicity or the unrestricted problem follows.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:22 |
| status | open |
| reason | Register the complete zero-correction stronger-support obstruction, deriving the needed low square jet from the actual gate and assumed stronger relation before applying the sharp homogeneous endpoint. Root is sole contributor; fresh isolated whole review is required. This rules out the specified extra jet, not modulo16 residual solvability or original realization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole stronger-support obstruction](#statement) | Every stated m,Q,H,Y, actual zero-correction gate, forbidden4Q support precision,16m consequence and precise m14 application; no global-square hypothesis or higher-residual exclusion. |
| argument | [Complete actual gate-to-endpoint proof](#argument) | Actual sixth-power identity, unit cube and derivative, forced low square jet, paid composition/root precision, exact new endpoint parameter and all limits. |
| dependency | [Adopted sharp homogeneous cube theorem](Yin_C_G0643_v2.md#statement) | Exact SC5 endpoint exclusion for all actual f,A in its degree/unit domain, applied at m_star=Q/2 after proving every hypothesis. |
| dependency | [Full zero-correction gate](Yin_C_G0649_v1.md#statement) | Application only: S=0 and the actual local root unit imply D_0 in phi^(8m); no higher old support or original sufficiency is supplied by this input. |
| support | [Adopted m14 canonical branch](Yin_C_G0668_v2.md#decision-whole-reviewed-2026-10-24) | Actual m14,Q32,H=W3W21,S0 data and old precision112, whose prospective128 strengthening is ruled out here; original and finite-residual conclusions are unchanged. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:35 |
| status | proved |
| reason | The complete fixed ZG1--ZG6 statement and four-part argument were directly read, followed by all of fresh isolated R909. Adopt the actual zero-correction stronger-support obstruction, including the forced low square jet, full derivative and composition precision, sharp endpoint applicability and m14 forbidden128 consequence. It rules out this added jet for Q<=4m, not modulo16 residual solvability, Q>4m or original realization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Whole stronger-support obstruction](#statement) | Every stated m,Q,H,Y, actual zero-correction gate, forbidden4Q support precision,16m consequence and precise m14 application; no global-square hypothesis or higher-residual exclusion. |
| argument | [Complete actual gate-to-endpoint proof](#argument) | Actual sixth-power identity, unit cube and derivative, forced low square jet, paid composition/root precision, exact new endpoint parameter and all limits. |
| dependency | [Adopted sharp homogeneous cube theorem](Yin_C_G0643_v2.md#statement) | Exact SC5 endpoint exclusion for all actual f,A in its degree/unit domain, applied at m_star=Q/2 after proving every hypothesis. |
| dependency | [Full zero-correction gate](Yin_C_G0649_v1.md#statement) | Application only: S=0 and the actual local root unit imply D_0 in phi^(8m); no higher old support or original sufficiency is supplied by this input. |
| support | [Adopted m14 canonical branch](Yin_C_G0668_v2.md#decision-whole-reviewed-2026-10-24) | Actual m14,Q32,H=W3W21,S0 data and old precision112, whose prospective128 strengthening is ruled out here; original and finite-residual conclusions are unchanged. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0909_v1.md#whole-zero-correction-stronger-support-finding) | Entire ZG1--ZG6 and all four sections, every local unit/precision and actual new endpoint hypothesis, all applications and exact higher-residual limits. |
