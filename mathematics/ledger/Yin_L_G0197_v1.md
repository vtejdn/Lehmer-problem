---
author: Yin
---

# Saturated doubling and exact short cyclic quotients

Date: 2026-10-10.
The coordinating AI for Yin adopts the complete D G0064 proof and independent noncontributor finding.
The resultant_research AI supplied all new derivations; the coordinator independently checked the entire argument.
No new program or external theorem is used.

<a id="saturated-short-cyclic-fixed-scope"></a>
## Adopted scope

For every actual reciprocal irreducible nontorsion input of degree d>=4 saturating the doubling floor2^d, the actual trace ideal is(T,U)=(T,2), and T(2),T(-1) each have absolute value at most2.
The principal quotients at alpha-1 and Phi3(alpha) are exactly zero or F2, and zero or F4, respectively.
Their explicit comaximality gives the entire quotient at alpha^3-1 and the divisibilities of2 retained below.
All odd-prime reduced root orders satisfy the stated Frobenius/inverse exclusion, including non-squarefree reductions.

The full cyclic income at exponents1 and3 is bounded independently of degree, so those constraints cannot themselves supply degree-linear income.
An exhaustive exact degree-four calculation leaves only three cyclotomic polynomials; there is no nontorsion quartic saturated input.
No classification in higher degree, variable-input inverse bound, near-one saturation theorem or uniform gap is adopted.
Historical pending-review text remains chronology, and only heading depth and relative navigation are transformed.
G0001 remains active and unresolved.

<a id="retained-saturated-short-cyclic-proof"></a>
## Actual-order inverse cost under saturated doubling resultants

Date: 2026-10-10.
Author inquiry by resultant_research for Yin.
Starting question: Determine a new discriminating arithmetic consequence or a precisely verified cost obstruction for the actual inverse W^(-1), W=(P^[2]-P)/2, on the saturated class from L194.
Preserve total small Mahler measure, actual integer order, primitive normalization and complete complementary factors; a fixed-base radical replay is not a new test.
The coordinator assigned the question but supplied no derivation.
G0001 remains active and unresolved.


<a id="saturated-short-return-unit-constraints"></a>
### 1. Precise domain, reused structure and changed question

Let P be monic, reciprocal, irreducible and nontorsion in Z[t], of degree d=2s>=4 and constant coefficient one.
Put Q=P^[2], retaining all conjugate squares with multiplicity, and assume

    |Res(P,Q)|=2^d.                                           (1)

Write alpha for one root and O=Z[alpha].
[L194](Yin_L_G0194_v1.md#saturated-resultant-fixed-scope) gives the actual inverse of W=(Q-P)/2 in O and the primitive scalar2.
The outstanding question is the size of that inverse or the whole primitive auxiliary/cofactor cost as the total logarithmic Mahler measure m=log M(P) becomes small.
A determinant-one inverse has no coefficient bound from that fact alone.
The argument below does not supply such a bound.
Instead it extracts exact short-return constraints on the entire saturated class, including its hypothetical m-to-zero portion, and a complete degree-four exclusion.
These are actual algebraic constraints, not a fixed-base radical replay or a model of independent angular data.

The reuse screen read the normalized trace Frobenius modules and mixed-resultant square identity in [L66](Yin_L_G0066_v1.md#reciprocal-frobenius-two-copy-module), the saturation proof in L194 and its S8 continuation boundary.
A bounded G-ledger text screen found no matching retained statement of the exact endpoint quotients or the degree-four conclusion below.
This is a local reuse statement, not a literature-priority claim.
The trace construction and square-resultant identity are explicitly reused rather than claimed new.

Put z=alpha+alpha^(-1), F=Q(z) and B=Z[z].
The inverse-pair involution and [L66's trace-order interface](Yin_L_G0066_v1.md#reciprocal-mixed-resultant-square) give a monic irreducible T in Z[x] of degree s with

    P(t)=t^s T(t+t^(-1)).

Define the full trace-powered polynomial

    U(x)=product_(j=1)^s [x-(z_j^2-2)],
    Q(t)=t^s U(t+t^(-1)),
    Res(P,Q)=Res(T,U)^2.                                    (2)

Every inverse pair is retained, even if two powered trace values coincide.
Consequently (1) gives |Res(T,U)|=2^s.
Modulo2, the complete squared-root construction gives U=T.
Equivalently, elementary symmetric functions of z_j^2 are the squares of the corresponding integer coefficients modulo2.
Thus V=(U-T)/2 is integral, and multiplication by V(z) on the actual order B has determinant

    Norm_(F/Q)(V(z))=Res(T,U)/2^s=+1 or -1.

Its inverse is integral in B.
Applying it to1 and using monic division gives a degree-bounded integral pair a,b with

    a T+b U=2,                 deg a,deg b<s,
    (T,U)=(T,2) in Z[x].                                    (3)

This is the trace counterpart of L194, obtained in the actual monic power basis without a maximal-order or good-prime assumption.

### 2. Fixed-point evaluations give degree-free exact norms

The fixed points of x -> x^2-2 are2 and-1.
The full product defining U gives

    U(2)=(-1)^s T(2) T(-2),
    U(-1)=(-1)^s T(1) T(-1).                                (4)

Evaluating (3) at those two points therefore shows that T(2) and T(-1) each divide2 in Z.
Neither vanishes: T(2)=0 would make alpha=1, and T(-1)=0 would make alpha a primitive third root of unity, both excluded by the domain.
Hence

    T(2) in {1,-1,2,-2},
    T(-1) in {1,-1,2,-2}.                                   (5)

In particular these are not merely unspecified powers of2 whose exponents might grow with degree.
With Phi_3(t)=t^2+t+1,

    Norm_(Q(alpha)/Q)(alpha-1)=P(1)=T(2),
    Norm_(Q(alpha)/Q)(Phi_3(alpha))=T(-1)^2,
    |Norm(alpha^3-1)|=|T(2)| T(-1)^2 in {1,2,4,8}.             (6)

For the second formula use Phi_3(alpha)=alpha(z+1), Norm(alpha)=1 and [Q(alpha):F]=2.
The first uses even d.
The last is multiplicativity, retaining the entire cyclic norm, not just a selected prime layer.

These identities sharpen to exact quotients in the actual order.
Set epsilon=0 or1 according as |T(2)|=1 or2, and delta=0 or1 according as |T(-1)|=1 or2.
Then

    O/(alpha-1)O = 0                     if epsilon=0,
                    F_2                 if epsilon=1;
    O/Phi_3(alpha)O = 0                  if delta=0,
                       F_4              if delta=1.          (7)

Here0 denotes the zero ring.
Indeed the first quotient is Z/(P(1)).
In Z[t]/Phi_3(t), t is a unit, t+t^(-1)=-1 and P(t)=t^s T(-1).
Thus the second quotient is Z[t]/(Phi_3,T(-1)); when |T(-1)|=2 this is F_2[t]/(t^2+t+1), the field with four elements.
This computation uses the actual presentation O=Z[t]/P and remains valid at ramified or nonmaximal-order primes.

Both ideals in (7) contain2O.
Their sum also contains3, since Phi_3(t)-(t+2)(t-1)=3.
Their sum is therefore O, because it contains both2 and3.
The integral Chinese remainder theorem for these demonstrably comaximal ideals gives

    O/(alpha^3-1)O isomorphic to F_2^epsilon x F_4^delta,      (8)

where an absent factor is the zero quotient.
In particular

    2/(alpha-1), 2/Phi_3(alpha), 2/(alpha^3-1) belong to O.    (9)

All denominators are nonzero by nontorsion.
If both factors in (8) are absent, the quotient is zero.
Otherwise its additive exponent is exactly2, while its cardinality is2^(epsilon+2delta).
The three divisions in (9) say that the indicated algebraic integers divide2 in O; they do not say their halves are integral.

<a id="saturated-modular-order-exclusion"></a>
### 3. An all-odd-prime root-order exclusion and the income boundary

There is also a uniform finite-field restriction without a squarefree-reduction hypothesis.
Let ell be any odd rational prime and let r be the multiplicative order of any root a of P modulo ell in the algebraic closure.
Constant coefficient one ensures a is nonzero.
Then

    2 is not congruent to +ell^j or -ell^j modulo r
    for every integer j>=0.                                (10)

Indeed reciprocity and the Frobenius automorphism put every a^(+ell^j) and a^(-ell^j) among the roots of P modulo ell.
If one were a^2, that value would also be a root of the full Q modulo ell.
This contradicts (P,Q)=(P,2), which reduces to the unit ideal over F_ell.
Polynomial formation of Q commutes with reduction because it is the symmetric full squared-root polynomial; repeated roots do not affect this reasoning.
Equation(10) in particular forbids orders1 and3 at odd primes.
For even r the congruence in(10) is automatically impossible, so no additional exclusion of all even orders is asserted.

For the actual logarithmic cyclic income A_all(n)=log|Norm(alpha^n-1)|, (6) gives

    A_all(1)<=log2,
    A_all(3)<=3 log2.                                       (11)

Any selected-prime lower certificate is bounded above by this complete income.
Therefore along any unbounded-degree sequence in the saturated class, including a hypothetical sequence with total m tending to zero, neither n=1 nor n=3 can supply A(n)>=eta*d for a fixed eta>0.
Their automatic or selected-prime layers cannot fix this deficiency, because the bound already includes all primes and depths.
This is an exact obstruction to deriving the [L168 same-exponent income gate](Yin_L_G0168_v1.md) from these short unit constraints.
It does not exclude suitable different exponents n<=C*d or a different use of the constraints.

<a id="quartic-saturation-torsion-only"></a>
### 4. Complete degree-four consequence

For d=4 write

    P(t)=t^4+a t^3+b t^2+a t+1,
    T(x)=x^2+a x+b-2.

Put A=T(2)=b+2a+2 and B=T(-1)=b-a-1.
Conditions(5) imply A,B are each in {1,-1,2,-2}, and

    A-B=3(a+1).

Their difference can only be-3,0 or3.
This yields exactly the eight integer pairs (a,b) in the table below, with no height cutoff or omitted coefficient range.

For the two trace roots r,s, write

    H=(r+2-s^2)(s+2-r^2)
      =a^3-2a^2-3ab+4a+b^2+b-2.

The last equality follows by r+s=-a, rs=b-2, r^3+s^3=-a^3+3a(b-2).
Pairing the four factors of Res(T,U) into its two diagonal factors and two off-diagonal factors gives exactly

    Res(T,U)=A B H.                                         (12)

For the diagonal product use (r-r^2+2)(s-s^2+2)=(2-r)(r+1)(2-s)(s+1)=T(2)T(-1).
The eight evaluations are elementary integer substitutions into (12):

| a | b | A | B | H | Res(T,U) |
|---:|---:|---:|---:|---:|---:|
| -1 | -2 | -2 | -2 | -13 | -52 |
| -1 | -1 | -1 | -1 | -12 | -12 |
| -1 | 1 | 1 | 1 | -4 | -4 |
| -1 | 2 | 2 | 2 | 3 | 12 |
| 0 | -1 | 1 | -2 | -2 | 4 |
| 0 | 0 | 2 | -1 | -2 | 4 |
| -2 | 0 | -2 | 1 | -26 | 52 |
| -2 | 1 | -1 | 2 | -18 | 36 |

Since the full resultant is the square of this trace resultant, saturation at d=4 requires its absolute value to be4.
The only remaining polynomials are

    t^4-t^3+t^2-t+1 = Phi_10(t),
    t^4-t^2+1       = Phi_12(t),
    t^4+1          = Phi_8(t).

Their torsion status is also immediate from their respective divisibility into t^5+1, t^6+1 and t^8-1.
All violate the nontorsion hypothesis.
Therefore there is no degree-four input in the actual saturated class.
This is a complete finite argument from exact endpoint constraints, not an empirical bounded scan.
It makes no classification claim for degree six or higher and gives no degree-uniform gap.

### Contribution, checks and continuation boundary

The assigned resultant_research AI supplied the complete trace-ideal deduction, fixed-point norm and exact-quotient arguments, modular order exclusion, short-income consequence and quartic elimination in this round.
The coordinator supplied the broad inverse/cofactor question and received interim findings but supplied none of these derivations.
L66 supplies the established trace-order and square-resultant structure, and L194 supplies the original full-order saturation interface.
No new literature theorem, source acquisition, numerical scan or program is used; the eight-row table is the full displayed elementary coefficient calculation.
The argument has been self-checked and is ready for separately organized full review; no such review is asserted here yet.

The initial hope of extracting a coefficient bound directly from unimodularity remains unproved.
Instead, saturation forces the actual short cyclic quotients(7)--(8) to have degree-independent size, identifies their entire dyadic structure, and excludes all nontorsion quartic inputs.
The bound at n=3 uses an actual comaximality argument and retains the full valuation; it is stronger than merely saying no odd primes occur.
These conditions hold on any hypothetical saturated m-to-zero family, but no such family is constructed.
They do not estimate the coordinates of W^(-1), bound the full primitive cofactor uniformly as m tends to zero, imply that every near-one input is saturated, or solve the unrestricted Task.

A discriminating next use would have to connect the three actual divisibilities in(9), together with the odd-prime order exclusion(10), to growing exponents or to a norm estimate for the inverse in the original power basis.
Reusing their small fixed cyclic norms as linear arithmetic income is ruled out by(11).
General nonsaturated inputs and the other candidate routes remain open.
G0001 remains active and unresolved.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0096_v1.md#complete-separate-noncontributor-review), with its original inspected scope and relationship.

## Retention and review bindings

The [complete noncontributor finding](../audits/reviews/Yin_R_G0096_v1.md#saturated-short-return-independent-review) covers the full [retained argument](#retained-saturated-short-cyclic-proof), including actual trace-order inversion, all endpoint signs, exact quotients and comaximality, all-prime order restrictions, full income scope and the exhaustive eight-row quartic elimination.
The reviewer supplied none of these derivations.

The complete D G0064 argument and its noncontributor finding are retained here at their original scopes.
This retention does not complete the Task.
