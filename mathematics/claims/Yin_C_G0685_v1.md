---
author: Yin
---

# Totally real reciprocal lifts preserving complete dyadic residual data

Human author Yin.
Root derived the explicit separated-real-root construction and its exact finite-gate compatibility below.
This is new author mathematics, initially open for fresh isolated whole review.
The active [G0001 Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) permits this continuation.
The established coefficientwise CRT and reciprocal Eisenstein mechanism was directly read in [C450](Yin_C_G0450_v1.md#reciprocal-local-realization-lemma) and [C527](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization).
That mechanism is credited rather than presented as new.
The new contribution here is its simultaneous use with explicitly separated positive trace roots, unchanged actual divided-remainder congruences and complete large Mahler cost.
No computation, parameter scan, new source acquisition or uninspected external theorem is used.

## Statement

Let d>=1 be an integer and T_0 in Z[X] any monic polynomial of degree d.
For p in{2,3,5} put

    C_2=X^2-2, C_3=X^3-3X, C_5=X^5-5X^3+5X,
    a(T)=rem_T(T(C_2))/2,
    b(T)=rem_T(T(C_3))/3,
    c(T)=rem_T(T(C_5))/5,
    F(T)=rem_T(2c(T)^2-3a(T)^5),
    X_s(T)=rem_T(b(T)^2-a(T)^3+s(c(T)^3-2b(T)^5)),
    s in{1,-1}.

These are actual monic integer divided remainders with the SAME indicated divisor T.
All are integral, as proved below.
Choose ANY positive integer M divisible by144 and satisfying

    M>max{16,288d[4(d+1)/3]^(d-1)}.                    (RL1)

For each nonleading coefficient index i, let r_i be the unique integer in[-72,71] satisfying

    r_i=[X^i]T_0 modulo16,
    r_i=[X^i]((X-2)^d+3) modulo9.

Set

    E(X)=sum_(i=0)^(d-1) r_i X^i,
    R_M(X)=product_(j=1)^d (X-Mj),
    T_M=R_M+E,
    P_M(t)=t^d T_M(t+t^(-1)).                          (RL2)

Then all following assertions hold for EVERY such M.

1. T_M is monic of degree d and has exactly one simple root x_j in each interval

    M(j-1/4)<x_j<M(j+1/4), 1<=j<=d.

All these trace roots are greater than2.
Both T_M and P_M are irreducible over Q.
The polynomial P_M is monic integral reciprocal of degree2d with constant term1, and all its2d roots are distinct positive real numbers in reciprocal pairs, none on the unit circle.
Its root is a nontorsion algebraic unit in a totally real field of degree2d.
The trace field has degree d.

2. The coefficientwise congruence T_M=T_0 modulo16 holds.
Consequently the FULL actual canonical remainder polynomials satisfy

    a(T_M)=a(T_0), b(T_M)=b(T_0), c(T_M)=c(T_0) modulo8,
    F(T_M)=F(T_0), X_s(T_M)=X_s(T_0) modulo8             (RL3)

for both fixed signs.
Thus every input solution of BOTH residuals modulo8 gives actual totally real irreducible reciprocal lifts satisfying those SAME modulo8 congruences.
No actual residual coordinate is chosen separately from T_M.
If either residual of T_0 is divisible by4, the corresponding quarter reduced modulo2 is also preserved as its full canonical coefficient polynomial.

3. In the trace field Q(x_j), each of a(T_M)(x_j), b(T_M)(x_j), c(T_M)(x_j) is NONZERO.
The conclusion holds at every embedding because T_M is irreducible; it is not a claim that every such value is positive.

4. The complete logarithmic Mahler measure has the explicit bounds

    d log(M/2)<m(P_M)<d log((d+1)M).                   (RL4)

It tends to infinity with M at fixed d and is very far from a near-one construction.
There are no uncharged or discarded reciprocal root pairs.

### Precise finite-gate and original-realization boundary

The statement applies to any specified T_0 satisfying the displayed finite congruences, independently of how that T_0 was obtained.
It supplies no such T_0 by itself.
It keeps the ACTUAL degree d and reduction T_0 modulo2, so any exact characteristic-two canonical construction, maximal Frobenius exponent or finite gate determined by that reduction stays unchanged.
Any additional inherited property must be checked at its own required precision; it is not inferred just from this sentence.
If a concrete base has the factorized form T_0=mathcal_H Phi^(7A)+2Phi^A K+4W, the new difference16Z has degree<d and is absorbed by W->W+4Z without changing K or the reduction.

These results concern finite dyadic residual congruences.
They do NOT give the characteristic-zero identities F(T_M)=X_s(T_M)=0, identify a separately constructed integer G_int with actual G_can, put the trace roots in[-2,2] with a Salem exception, or realize the original restricted trace/residual problem.
In fact all x_j>2 here, and P_M has d exterior real roots.
No unrestricted Lehmer completion, bounded Mahler measure or uniform positive-gap conclusion follows.

## Argument

### 1. Actual divided remainders and exact congruence continuity

For p=2,3,5, C_p=X^p modulo p and T(C_p)=T(X)^p modulo p.
Monic polynomial division commutes with coefficient reduction, so rem_T(T(C_p))=0 modulo p coefficientwise.
This proves integrality of the three displayed divided remainders for every monic integer T, without a root or field assumption.

Over any commutative coefficient ring, the monic division algorithm uses only addition and multiplication of coefficients.
It therefore commutes with every coefficient-ring homomorphism and with reduction modulo any integer.
If T=T_0 modulo16 and both are monic of degree d, their canonical remainders of T(C_p) agree modulo16.
For p=2, dividing the actual even integer remainders by2 proves the canonical a polynomials agree modulo8.
For p=3,5, those odd integers are units modulo8, giving the b and c congruences modulo8.
Every one of these canonical polynomials has degree below d, so the comparisons are coefficientwise, not only quotient-ring equalities.

Forming the two residual polynomials and performing their ACTUAL monic division once more commutes with reduction modulo8.
Since the divisor is the same reduced monic polynomial for both inputs, this proves every congruence in RL3.
If a residual is divisible by4, the difference of the two canonical residuals is divisible by8, so their actual integer quarters differ by a multiple of2.
This establishes the asserted quarter preservation without taking a half in characteristic two.

### 2. Credited CRT and reciprocal Eisenstein mechanism

The moduli16 and9 are coprime, so each prescribed residue has a unique representative in[-72,71].
Since M is divisible by144, every nonleading coefficient of R_M is zero modulo144.
It follows directly that

    T_M=T_0 modulo16,
    T_M=(X-2)^d+3 modulo9.

This is the same coefficientwise CRT and reciprocal Eisenstein mechanism retained in C450/C527, now with the declared larger dyadic modulus.
No local-root simplicity or unramified hypothesis from those other applications is imported.

The polynomial t^d T_M(t+t^(-1)) is integral, monic and reciprocal of degree2d with constant1: each trace monomial of degree i<=d contributes t^d(t+t^(-1))^i with no negative exponent, and only the leading i=d term supplies either endpoint coefficient.
The second congruence gives

    P_M(t)=(t-1)^(2d)+3t^d modulo9,
    P_M(t+1)=t^(2d)+3(t+1)^d modulo9.

All nonleading coefficients of this last monic polynomial are divisible by3 and its constant coefficient is3 modulo9.
Eisenstein's criterion proves its irreducibility, hence that of P_M.
For clarity its elementary reason is that any monic integral factorization, provided by Gauss's lemma from a rational one, reduces modulo3 to factors which are powers of t; both constant terms would be divisible by3, contradicting the exact constant valuation one.
Translation preserves rational reducibility.

If T_M factored into two nonconstant monic integral trace polynomials, multiplying each substituted factor by its appropriate power of t would factor P_M into two nonconstant integral polynomials.
Thus T_M is also irreducible.
This argument is independent of how T_0 factors modulo2.

### 3. Every actual real root and the explicit separation threshold

At an endpoint x=M(j+epsilon/4), epsilon in{1,-1}, its distance from the jth root of R_M is M/4.
For every other integer index l, its distance from Ml is at least3M/4.
Consequently

    |R_M(x)|>=M^d(3/4)^(d-1)/4.

The two endpoint signs are opposite, because the only root of R_M between them is the simple jth root and all its other factors keep their signs.
All endpoints satisfy |x|<(d+1)M and |x|>1 under RL1.
The entire perturbation, including all d coefficients, therefore obeys

    |E(x)|<=72 sum_(i=0)^(d-1)|x|^i
           <=72d[(d+1)M]^(d-1).

RL1 makes this strictly smaller than the displayed lower bound for |R_M(x)|.
Thus T_M retains the opposite signs at the two endpoints and has a real zero inside each of the d disjoint intervals.
A degree-d polynomial has no further roots counted with multiplicity, so there is exactly one in each interval and all are simple.
Every root is greater than3M/4>2.
This proof does not require a numerical root approximation, asymptotic perturbation statement or unpriced separation limit.

For each x_j>2 the equation t+t^(-1)=x_j has the two distinct positive real roots

    beta_j=(x_j+sqrt(x_j^2-4))/2>1, beta_j^(-1)<1.

Different trace values cannot share a reciprocal root.
These are all2d roots of P_M, and none has modulus one.
Since P_M is monic irreducible with constant1, its root is an algebraic unit of degree2d in a totally real field and is not a root of unity.
Irreducibility of T_M gives trace-field degree d.
The construction is not Salem when d>1, since it has d exterior roots rather than one exterior pair.

### 4. Original field-value nonvanishing and complete measure

Let x_d be the largest trace root.
For every x>2 one has C_p(x)>x for p=2,3,5.
For example write x=t+t^(-1) with t>1; the exact polynomial identities give C_p(x)=t^p+t^(-p), which is strictly increasing with p>=1.
The displayed identities for p=2,3,5 follow by direct expansion.
Thus C_p(x_d) is larger than every trace root and T_M(C_p(x_d)) is strictly positive.
Evaluation of the actual monic division at x_d gives

    a(T_M)(x_d)=T_M(C_2(x_d))/2>0,
    b(T_M)(x_d)=T_M(C_3(x_d))/3>0,
    c(T_M)(x_d)=T_M(C_5(x_d))/5>0.

Each is therefore a nonzero element of Q(x_d).
Every other trace root is an embedding of the same irreducible field, and embeddings are injective, so all its conjugate values are nonzero as claimed.
This does not set either characteristic-zero residual equal to zero.

The inequality x-1<(x+sqrt(x^2-4))/2<x holds for x>2.
Since x_j>3M/4 and M>16, beta_j>M/2, while x_j<(d+1)M gives beta_j<(d+1)M.
The monic reciprocal polynomial has exactly the d roots beta_j outside the unit circle and their reciprocals inside it.
Summing their logarithms proves the complete bounds RL4, with no normalization by degree or omission of any root.

All characteristic-two and higher-congruence conclusions are exactly those of Section1 and the explicit T_M=T_0 modulo16 identity.
The large real-root and Mahler expenses in Sections3--4 explain why this finite-gate lift is not a solution of the original small-measure or characteristic-zero residual problem.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-24)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:01 |
| status | open |
| reason | Register the complete generic mod16-preserving reciprocal irreducible and totally real construction, exact divided-remainder continuity, every separated trace root and field-value nonvanishing, with explicit full Mahler costs. The classical CRT/Eisenstein mechanism is credited to C450/C527; the new actual compatibility and separation estimates are proved here. Root is the sole contributor and fresh isolated whole review is required. No characteristic-zero residual identities, Salem trace location, G_int=G_can, bounded measure or unrestricted realization is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire finite-gate real-lift theorem](#statement) | Every monic T_0 of any degree d>=1, every explicit allowed multiple M, actual irreducible reciprocal lift and all real roots, full dyadic remainders/quarters, nonzero trace-field values and complete measure costs, with precise original-realization limits. |
| argument | [Complete four-part proof](#argument) | Actual monic division and p=2 half precision, coefficientwise CRT, credited reciprocal Eisenstein mechanism, all endpoint signs and perturbation expenses, full root/field and measure accounting. |
| support | [Earlier reciprocal local realization](Yin_C_G0450_v1.md#reciprocal-local-realization-lemma) | Credited trace-polynomial CRT and translated reciprocal Eisenstein mechanism; its odd-p input and unrelated valuation conclusions are not silently reused. |
| support | [Actual 3-Eisenstein trace mechanism](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization) | The directly read T=(X-2)^d+3 modulo9 and P(t+1)=t^(2d)+3(t+1)^d mechanism; no earlier measure, local simplicity, order or source theorem is imported. |

### Decision whole-reviewed-2026-10-24

| Field | Value |
| --- | --- |
| date | 2026-10-24T04:15 |
| status | proved |
| reason | The entire fixed RL1--RL4 statement and four-part proof were directly read, followed by all of fresh isolated R906. Adopt the exact mod16-preserving CRT construction for every stated monic input and allowed M, both irreducibilities, all separated positive real roots, full canonical mod8 continuity, every embedding nonvanishing and complete large Mahler cost. The credited earlier mechanism and all finite-data versus characteristic-zero, Salem, bounded-measure and original-realization limits remain. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire finite-gate real-lift theorem](#statement) | Every monic T_0 of any degree d>=1, every explicit allowed multiple M, actual irreducible reciprocal lift and all real roots, full dyadic remainders/quarters, nonzero trace-field values and complete measure costs, with precise original-realization limits. |
| argument | [Complete four-part proof](#argument) | Actual monic division and p=2 half precision, coefficientwise CRT, credited reciprocal Eisenstein mechanism, all endpoint signs and perturbation expenses, full root/field and measure accounting. |
| support | [Earlier reciprocal local realization](Yin_C_G0450_v1.md#reciprocal-local-realization-lemma) | Credited trace-polynomial CRT and translated reciprocal Eisenstein mechanism; its odd-p input and unrelated valuation conclusions are not silently reused. |
| support | [Actual 3-Eisenstein trace mechanism](Yin_C_G0527_v1.md#binary-depth-and-irreducible-realization) | The directly read T=(X-2)^d+3 modulo9 and P(t+1)=t^(2d)+3(t+1)^d mechanism; no earlier measure, local simplicity, order or source theorem is imported. |
| review | [Fresh isolated whole mathematical review](../audits/reviews/Yin_R_G0906_v1.md#totally-real-reciprocal-dyadic-lift-whole-independent-finding) | Entire actual generic finite-gate reciprocal lift, every d and allowed M, all canonical divisions and half precision, all real roots and fields, every nonzero conjugate value and full measure cost. |
