---
author: Yin
---
# Actual trace-quotient income under total ramification at two

Date: 2026-10-20T11:56.
Human author Yin.
The entropy_attainment_bridge agent identified the actual degree-five self-composition obstruction and supplied its complete extension to every totally ramified trace degree, including the stronger valuation and norm bounds below.
Root independently developed the parallel all-degree low-branch contradiction and coordinated its use as an original-input interface.
Both are contributors; neither supplies an independent review of this candidate.
The earlier abstract residual work and its possible unit-g existence do not supply an actual self-composition realization.
No computation, parameter scan or new external source theorem is used here.

## Statement

Let P be a monic irreducible reciprocal nontorsion integer-unit polynomial with constant coefficient1 and degree d=2r.
For a root alpha put K=Q(alpha), delta=alpha+alpha^(-1), F=Q(delta), and let T in Z[X] be its actual monic irreducible trace polynomial, so

    P(z)=z^r T(z+z^(-1)), [K:F]=2, [F:Q]=r.

Assume F is totally real and that2 is totally ramified in F: there is one prime p over2, with ramification index r and residue degree1.
Use the original trace quotients

    C2(X)=X^2-2, C3(X)=X^3-3X,
    C5(X)=X^5-5X^3+5X,
    a=T(C2(delta))/2, b=T(C3(delta))/3,
    c=T(C5(delta))/5.

These are nonzero algebraic integers in Z[delta] by the accepted exact trace interface.
For r>=2 normalize v_p by v_p(2)=r, and write A=v_p(a), C=v_p(c).
Then

    A=0 OR A>=r.                                  (1)

In particular, if2c^2=3a^5, then

    A>=r, C>=2r,
    Norm_(F/Q)(a)>=2^r,
    abs(Norm_(F/Q)(c))>=2^(2r),
    Res(P(z),P(z^2))>=2^(2d).                     (2)

The positive sign of Norm_F(a) in(2) follows from total positivity under the stated equation.
If in addition, for s in{1,-1},

    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0,

then

    v_p(g)=3C>=6r,
    abs(Norm_(F/Q)(g))>=2^(6r),
    abs(Norm_(K/Q)(g))>=2^(6d).                    (3)

For r=1 the complete residual system is impossible by the accepted unramified2 exclusion; the valuation assertion(1) and the f-only implications(2) are asserted only for r>=2.
The norms in(2)--(3) retain the complete original trace and degree-d fields.
This is a theorem for the actual coupled self-composition quotients, not for arbitrary integral triples in a totally ramified field.
It provides arithmetic income only, with no assertion of a uniform original Archimedean transfer price or a Mahler gap.

<a id="argument"></a>
## Complete proof

The accepted [C153v2 exact trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain), itself retaining the [L66 trace field](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) and [integral quotient](../ledger/Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module), proves all the displayed field degrees and the nonzero integrality of a,b,c.
In particular the equality a=T(C2(delta))/2 is exact, including its factor2 and its original phase when returned to P.
Neither a different generator of F nor an arbitrary totally positive element may replace this a.

Since O_F/p=F_2, there is epsilon in{0,1} with delta congruent to epsilon modulo p.
Put x=delta-epsilon and j=v_p(x).
For r>=2, delta cannot equal the rational integer epsilon, since delta generates the degree-r field.
Thus j is a finite positive integer.
Extend v_p to Qbar_2 with v_p(2)=r.
For EVERY Q-embedding tau:F->Qbar_2, the induced prime of F lies above2 and hence is the same unique p.
Consequently

    v_p(tau(delta)-epsilon)=j                      (4)

for all r conjugates, including every multiplicity of the actual degree-r minimal polynomial exactly once.
This is a uniqueness-of-prime consequence; it does not assume that F/Q is Galois, that Z[delta] is maximal or that x is a uniformizer.

The exact Chebyshev difference is

    C2(delta)-epsilon=x^2+2epsilon x-2.             (5)

If1<=j<r, all three terms on the right have valuation strictly greater than j: their valuations are2j, r+j when present, and r.
Possible equality or cancellation among the smallest of these values only increases the valuation and does not affect the strict comparison with j.
For each conjugate delta_i, (4) and the non-Archimedean strict-minimum rule therefore give

    v_p(C2(delta)-delta_i)=j.

Factoring the ACTUAL monic T over Qbar_2 and retaining all r roots proves

    v_p(T(C2(delta)))=rj,
    A=rj-r=r(j-1).                                (6)

Thus A=0 when j=1, and A>=r when2<=j<r.

If j>=r, equation(5) has valuation at least r, and(4) has valuation at least r at every conjugate.
Every factor C2(delta)-delta_i then has valuation at least r, so

    v_p(T(C2(delta)))>=r^2,
    A>=r^2-r>=r                                  (7)

because r>=2.
The original nonvanishing of a excludes an infinite valuation; the lower bound itself would remain valid if a factor vanished, but no such vanishing is used.
Equations(6)--(7) prove(1) in every case, including j=r and all ramified-order indices.

Now assume2c^2=3a^5.
Its valuation gives

    5A=r+2C>0.

Therefore A is positive, and(1) forces A>=r.
It follows that C=(5A-r)/2>=2r.
The unique prime has residue degree1, so its contributions to the rational norms of a and c are exactly A and C.
At every other finite prime these integral elements have nonnegative valuation, giving the first two norm bounds in(2).
All real conjugates of a are positive, so Norm_F(a)>0.

The original phase relation is

    P(alpha^2)=2 alpha^d a.

Since the original monic reciprocal polynomial has constant1 and even degree, Norm_(K/Q)(alpha)=1.
Since a belongs to F and [K:F]=2, the original resultant is exactly

    Res(P(z),P(z^2))
      =2^d Norm_(K/Q)(a)
      =2^d Norm_(F/Q)(a)^2
      >=2^(d+2r)=2^(2d).                          (8)

Thus no root, phase, denominator or original norm multiplicity is omitted.
This argument uses only f=0; it does not use a residual equation to obtain(8).

Finally impose the complete residual system and g!=0.
The [C178 exact two-adic identity](Yin_C_G0178_v1.md#statement) applies to these three nonzero integral elements in the actual totally real F, and gives

    v_p(g)=3v_p(c)=3C.

Using C>=2r proves the first inequality in(3).
Because the unique2-prime has residue degree1 and g is integral, the full absolute F-norm is at least2^(6r).
The quadratic original tower gives

    abs(Norm_(K/Q)(g))
      =abs(Norm_(F/Q)(g))^2>=2^(12r)=2^(6d).       (9)

The identity v_p(g)=3C is used ONLY in this full residual branch, not under f=0 alone.
When r=1, the prime over2 is unramified; C178 directly excludes the complete residual system, as stated separately.

<a id="inputs-and-boundaries"></a>
## Exact inputs and remaining boundary

| Input | Exact scope used |
| --- | --- |
| [C153v2 actual trace interface](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual T, complete original degrees, nonzero integral theta2,theta3,theta5 and their exact original phases. |
| [L66 trace field and order](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | T is the actual minimal polynomial of delta; K/F has degree2, without an unwarranted Galois or powered-degree assumption. |
| [C178 exact residual valuation](Yin_C_G0178_v1.md#statement) | G=3C only with both residual equations and g nonzero; its separate unramified2 exclusion handles r=1. |
| Elementary local field and norm facts | Every embedding induces the unique prime above2, strict minimum valuations, monic factorization over Qbar_2 and complete residue-weighted rational norms. |

The proof does not infer total ramification from repeated polynomial reduction or from a chosen nonmaximal order.
Total ramification in the actual F is an explicit hypothesis; the equal-conjugate valuation argument does not discard the possible index of Z[delta] in O_F.
The hypothesis is on the original trace field F, not merely on a smaller coordinate field Q(a).
No rational proportional relation between b and c is assumed.
The assertion about arbitrary abstract residual triples is not strengthened, and a possible abstract unit-g construction would not realize the required self-composition quotient at this trace input.
Any further return from the increased arithmetic income to total Mahler measure must retain the original coefficient and Archimedean costs.
No such estimate or automatic all-input total-ramification condition is claimed.

## Current assessment
[Selected decision](#decision-initial)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T11:56 |
| status | open |
| reason | Register a complete actual original-trace self-composition theorem with every local conjugate and original norm cost; a noncontributor whole review and adoption remain separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete original-trace theorem](#statement) | Totally ramified2 trace fields, precise r>=2/r=1 branches, f-only income and stronger complete-residual norm. |
| argument | [Entire local and original-norm proof](#argument) | All conjugate valuations, j finite and both j ranges, original theta2 normalization, full resultant and quadratic norm tower. |
| dependency | [Actual trace quotients](Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Nonzero integral quotient values in the actual order, exact phases and original degree2r. |
| dependency | [Residual two-adic theorem](Yin_C_G0178_v1.md#statement) | Its exact G=3C identity in the complete residual branch and unramified2 exclusion for r=1. |
| support | [Exact inputs and boundaries](#inputs-and-boundaries) | Parallel contributor roles, original-field hypothesis, no maximal-order assumption and no unpriced gap inference. |
