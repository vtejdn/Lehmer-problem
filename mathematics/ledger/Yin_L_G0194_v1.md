---
author: Yin
---

# Frobenius saturation and exact primitive auxiliary denominators

Date: 2026-10-10.
The coordinating AI for Yin adopts the complete D G0062 proof and its separate full review at the exact scope below.

<a id="saturated-resultant-fixed-scope"></a>
## Adopted scope

For every monic reciprocal irreducible nontorsion unit polynomial of degree d>=4 whose complete doubling resultant has absolute value2^d, the actual common ideal is(P,2).
The least interpolation scalar is exactly2 and the actual L174 adjugate seed has content2^(d-1).
This is a theorem on the full saturated class, with no maximal-order assumption.

Odd irreducible lifts of a fixed saturated base retain the exact scalar and a bounded coefficient norm and whole complementary measure depending only on that base.
The original Lehmer base and all prime lifts q>40 supply actual unbounded-degree inputs with8q unit-circle conjugates, at the retained L159 statement-level source scope.
Their total measure remains fixed positive and they need not be Salem.
No uniform inverse or cofactor estimate as total measure tends to zero is adopted.
The coordinating AI authored all new deductions; resultant_research supplied the complete separate noncontributor review.

Historical pending-review wording records chronology; this adoption and the full retained finding determine current status.
Only heading depth and relative navigation are transformed.
G0001 remains active and unresolved.

<a id="retained-saturated-resultant-proof"></a>
## Frobenius saturation forces exact primitive scalar two

Date: 2026-10-10.
Direct follow-up proof by the coordinating AI for Yin.
The trigger is [D61's exact content control](Yin_L_G0193_v1.md#exact-resultant-content-collapse), developed by this coordinator and separately reviewed.
The proof below is the coordinator's own new derivation; no assigned agent contributed its mathematics.
It is pending full separate review.
No new program, source acquisition or external theorem is needed.

### Reuse and precise question

Reuse the [L174 doubling-auxiliary proof](Yin_L_G0174_v1.md#doubling-auxiliary-factor-universality), [L66's exact original-Lehmer mixed resultant](Yin_L_G0066_v1.md#reciprocal-trace-lehmer-control), and [L159's actual irreducible Lehmer radical family](Yin_L_G0159_v1.md#irreducible-lehmer-radical-control).
L66 already studies normalized Frobenius modules; no novelty for that module is asserted.
The changed question is its consequence for the exact L174 adjugate representative, primitive interpolation scalar and full auxiliary cost.
D61 has no unit-circle conjugates; the present application also tests the stronger height argument obtained by evaluating at an actual unit-circle conjugate.
The accepted statement-level degree-only input used by L159 remains at that recorded scope; this work does not claim a new source-proof inspection.

<a id="saturated-resultant-primitive-scalar"></a>
### 1. Saturation gives the exact ideal and interpolation scalar

Let P be monic, reciprocal, irreducible and nontorsion in Z[t], of degree d>=4 and constant term one.
Let Q=P^[2] be the full degree-d polynomial of all conjugate squares, including every multiplicity.
Assume its nonzero signed resultant R satisfies

    |R|=2^d.                                                  (1)

Then

    (P,Q)=(P,2) in Z[t].                                      (2)

In particular the additive group Z[t]/(P,Q) is (Z/2Z)^d, and the least positive integer D admitting integral f with

    f = D t modulo P,
    f = D(t^2-1) modulo Q                                    (3)

is exactly2.

To prove (2), Q is congruent to P modulo2.
One direct verification uses even d and the full identity Q(z^2)=P(z)P(-z): reduction modulo2 gives P(z)^2=P(z^2), hence equality of the corresponding polynomials in z^2.
Put W=(Q-P)/2 in Z[t].
In the order O=Z[t]/(P), multiplication by W is an integer d by d matrix and

    det(mult_W)=Norm(W(alpha))=R/2^d=+1 or -1.

This is the determinant of multiplication in the actual monic power basis; it does not assume the maximal order.
Its inverse matrix is integral by the adjugate identity.
Thus W is a unit of O: applying that inverse to1 gives an integral element B_2 with B_2 W=1 in O.
Choose its unique representative of degree less than d.
Since Q=P+2W,

    A_2 P+B_2 Q=2                                            (4)

for an integral A_2 of degree less than d.
Indeed B_2 Q-2 is divisible by the monic P in Z[t], and its degree is less than2d.
Equation(4) and Q congruent to P modulo2 prove both inclusions in(2).

If (3) holds, reduction in the common quotient (2) forces D(t^2-t-1)=0.
The quotient over F2 has the monic basis1,t,...,t^(d-1), and 2<d, so D must be even.
Conversely the seed in the next section realizes D=2.
This exact interpolation minimum uses d>=4; no degree-two exception is silently included.

### 2. Exact content of the actual resultant representative

Put

    f_2=t B_2 Q+(t^2-1)A_2 P.                              (5)

It is nonzero, of degree at most2d+1, and has exactly the residues (3) with D=2.
It is primitive.
For the last assertion, let its positive coefficient content be c.
Evaluation at alpha gives f_2(alpha)/alpha=2; alpha is a unit.
Therefore f_2(alpha)/(c alpha)=2/c is both rational and an algebraic integer, and c divides2.
If c=2, divide each residue identity by2: the quotients also have even coefficients, since P and Q are monic and their nonzero reductions lie in the integral domain F2[t].
Thus f_2/2 would satisfy(3) with D=1, contradicting Section1.
Hence c=1.

The degree-less-than-d Bezout pair for any fixed scalar is unique over Q because P and Q are coprime.
Comparing (4) with the pair for signed R in L174 proves

    A_R=(R/2) A_2,
    B_R=(R/2) B_2,
    f_R=(R/2) f_2,
    content(f_R)=2^(d-1).                                 (6)

Consequently the primitive seed of that exact adjugate construction is f_2 up to sign; its remaining signed scalar is R/content(f_R)=+2 or -2.
The entire exponential resultant floor has been reduced to the least permitted constant.
This does not bound ||A_2||, ||B_2||, ||f_2|| or its complementary measure uniformly over all saturated inputs.
Saturation removes the proposed scalar floor, not every possible height or cost obstruction.

### 3. Odd radical lifts preserve saturation and bounded seed cost

Fix one input P_0 satisfying Section1, of degree e, and fix its integral degree-bounded pair A_0 P_0+B_0 Q_0=2.
Let q be any odd positive integer for which

    P_q(t)=P_0(t^q)

is irreducible over Q.
Then it is an actual reciprocal nontorsion unit input of degree d=e q.
The full powered polynomial is

    Q_q(t)=Q_0(t^q).                                         (7)

Indeed for each conjugate alpha_i of P_0, its qth roots form one full fiber; squaring permutes the qth roots of unity because q is odd.
Their squares are precisely the qth roots of alpha_i^2.
This argument retains all fibers and multiplicities, even if different alpha_i^2 coincide.

Evaluation at every fiber gives the signed resultant and complete measure identities

    Res(P_q,Q_q)=Res(P_0,Q_0)^q,
    |Res(P_q,Q_q)|=2^(e q)=2^d,
    m(P_q)=m(P_0)>0.                                        (8)

Each base resultant factor is repeated q times.
For Mahler measure, the q roots above alpha_i have modulus |alpha_i|^(1/q), whose product of max(1,modulus) values is max(1,|alpha_i|).

Substitution in the base identity gives exactly

    A_0(t^q) P_q+B_0(t^q) Q_q=2.

Both coefficients have degree less than d and therefore are the unique pair of Section1.
Accordingly the exact primitive seed is

    f_q=t B_0(t^q) Q_0(t^q)+(t^2-1) A_0(t^q) P_0(t^q),
    deg f_q <= (2e-1)q+2,
    ||f_q||_1 <= C_0,
    C_0=||B_0||_1 ||Q_0||_1+2||A_0||_1 ||P_0||_1.           (9)

Substitution preserves coefficient norm, and the displayed triangle bound includes any overlaps.
C_0 is a finite computable constant depending on the fixed base only; no numerical value is claimed or needed.
Section2 proves that f_q is primitive, without relying on its possibly cancelling leading terms.
Its remaining scalar is2 at every degree, and the actual adjugate representative has content2^(d-1).

Apply the complete L174 nonvanishing, integrality and actual-reversal proof to f_q.
The full auxiliary G_(f_q) is nonzero and integral, and after its maximal monomial is removed it has the form

    G_(f_q)=t^ell P_q C_q,
    C_q in Z[t] nonzero and reciprocal,
    deg G_(f_q) <= 4[(2e-1)q+2],
    0<=m(C_q)<=3 log C_0-m(P_0).                            (10)

The bound uses ||G_f||_1<=||f||_1^3, the whole-polynomial circle norm and Mahler multiplicativity.
Every scalar and noncyclotomic complementary factor is retained.
C_q is not asserted cyclotomic or of vanishing cost.
All degree and reversal statements use the actual seed degree if cancellation lowers it.

### 4. Actual original-Lehmer application, including unit-circle conjugates

For the original degree-ten Lehmer polynomial

    P_0=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1,

L66 retains Res(P_0,P_0^[2])=2^10 exactly.
Thus it satisfies Section1.
L159 proves P_0(t^q) irreducible for every prime q>40, at its explicitly accepted degree-only source scope.
Each such q is odd, so Sections2--3 apply to an unbounded-degree family of actual minimal polynomials.
Its total measure is the fixed original Lehmer measure, not a sequence tending to one.

Every base unit-circle conjugate contributes q unit-circle conjugates to P_q; the original eight such roots yield8q.
Hence this family has actual unit-circle embeddings at every degree, while its exact primitive seeds have the bounded coefficient norm(9), constant interpolation scalar2, and bounded full complementary measure(10).
The stronger unnormalized L174 height estimate from unit-circle evaluation therefore also cannot be carried through content normalization as an exponential lower bound.
It remains valid for the unnormalized f_R itself, whose scalar is precisely the one removed in(6).

These radical inputs generally have many expanding roots and are not asserted Salem.
Their individual off-circle moduli tend to one, but their total positive measure stays fixed.
They are legitimate unrestricted reciprocal-unit controls; they do not constitute a G0001 counterexample or rule out an obstruction using total m tending to zero essentially.

### Contribution, self-check and continuation

The coordinator supplied every new implication: saturated determinant to a unit in the actual order, the exact ideal and interpolation minimum, primitivity and exact adjugate content, substituted bounded-cost seeds, and the unit-circle radical application.
The proof reuses L174's already reviewed auxiliary argument, L66's retained exact resultant, and L159's actual irreducibility theorem at its disclosed source depth.
No fresh numerical calculation, J, source proof audit or exhaustive literature search is claimed.
Full noncontributor review is pending.

This result replaces a possible exponential scalar obstruction by the exact constant2 throughout the saturated class.
The next substantive issue is the size and structure of the inverse W^(-1) in the actual order, or direct full-cofactor control as total m becomes small.
The scalar conclusion alone gives no useful uniform bound for those inverses over all inputs, and the fixed-base radical family supplies no vanishing-measure sequence.
All eight candidate directions and the unrestricted Task remain active.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0093_v1.md#separate-complete-noncontributor-review), with its original inspected scope and relationship.

## Retention and review bindings

The [complete noncontributor finding](../audits/reviews/Yin_R_G0093_v1.md#saturated-resultant-independent-review) covers the entire [retained argument](#retained-saturated-resultant-proof) and its stated interfaces, quantitative boundaries and actual evidence.
It discloses prior foundation contributions and does not relabel source-statement reuse as a new proof audit.

The complete D G0062 proof and noncontributor finding are retained here at their original scopes.
Routine consumer relocation changes no proof or executed result and does not complete the Task.
