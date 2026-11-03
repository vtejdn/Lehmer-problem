---
author: Yin
---
# Full norm floor for integer affine residual triples

Date: 2026-10-20T10:21.
Human author Yin.
The draft_inventory_later agent supplied the exact3-prime companion calculation.
Root proposed the affine test and supplied its elimination and rational reconstruction.
The entropy_attainment_bridge agent supplied the real-degree bound, complete prime-cost argument, infinite integer-affine conclusion and odd-offset exclusion, and authored this fixed candidate.
These three agents are contributors, not independent reviewers of the present proof.
The entropy_attainment_bridge author also authored C178; its independent R447 and accepted assessment are reused at their exact scopes.
All three agents contributed to C180; its independent R451 and accepted assessment are likewise reused without a new independent upstream-proof claim.

## Statement

Let F be any totally real number field of degree r and let a,b,c be nonzero algebraic integers in F.
Suppose s in{1,-1} and

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.                                  (S1)

At every prime p over3, in the integer valuation normalization, write

    e=v_p(3), A=v_p(a), B=v_p(b), C=v_p(c), G=v_p(g).

Then2C=e+5A, C>A, 5B<3C, G=5B and C>B.
If B>0, also2B=3A.
In particular b/c is not integral at any prime over3.
These assertions do not require an affine relation.

Now suppose additionally b=u c+v for some rational integers u,v.
Then

    abs(Norm_F(g))>=2^r.                            (S2)

No such triple exists if u=0, v=0 or v is odd.
When u,v are nonzero, its actual primitive field H=Q(a,b,c) equals Q(c), has degree at most7, and in fact has degree in{2,3,4,6}.
These conclusions retain the original ambient norm and exponent r.
They do not assert existence in any of the remaining even-offset cases.
They prove the desired2^(r/2) floor on the entire integer affine family, while leaving arbitrary nonaffine integral b,c outside the statement.

<a id="argument"></a>
## Complete proof

The two complete proof sections below retain the author deductions originally numbered R16--R22 in the continuing singleton inquiry.
Only their relevant mathematics is retained here; the unrelated primitive-field and source-existence investigations remain outside this candidate.
C178 and C180 are the accepted fixed inputs identified in the final table.

<a id="singleton-three-adic-companion"></a>
### The corresponding exact3-prime calculation

The draft_inventory_later agent supplied this complete local deduction in the author discussion.
Fix p over3 and again write e=v_p(3), A=v_p(a), B=v_p(b), C=v_p(c), G=v_p(g).
Now f=0 gives

    2C=e+5A, C>A,
    5B<3C, G=5B.                                  (R16)

Indeed, if5B>=3C, then G>=3C>3A.
The residual equation forces2B=3A, but then5B=15A/2<3C=(3e+15A)/2, a contradiction.
The unequal valuations in g therefore give G=5B.
If B>0, this is greater than2B, so the residual equation further gives2B=3A.
It follows in either case B=0 or B>0 that C>B.
In particular b/c cannot be integral at a prime over3.
The conclusion is local and does not by itself yield the desired global exponential norm floor.

<a id="singleton-integral-affine-family"></a>
### A complete norm floor on every integer affine b,c relation

2026-10-20T10:18.
Root proposed the bounded affine test b=u c+v with u,v in{1,-1,2,-2} and supplied its exact elimination and reconstruction.
The following author argument by entropy_attainment_bridge proves the entire integer affine family using that elimination and the preceding3-prime input from draft_inventory_later.
No root search, factorization or Sturm computation is used in this argument.
It is separate from root's actual J111 finite calculation, whose stronger finite factor conclusion is not needed here.

For EVERY pair of rational integers u,v, the original residual system with b=u c+v satisfies

    abs(Norm_F(g))>=2^[F:Q].                        (R17)

There is no such solution if u=0, if v=0, or if v is odd.
Thus the original2^([F:Q]/2) target is established on this infinite two-parameter affine family, without asserting that the remaining even-offset cases actually occur.
The general nonaffine residual system remains unresolved.

If u=0, b is a nonzero rational integer and C180 excludes the triple.
If v=0, b/c=u is integral, contrary to C>B at every3-prime in(R16).
Hence assume u,v are nonzero.
Set

    Q(X)=(uX+v)^2+s[X^3-2(uX+v)^5],
    P(X)=27Q(X)^5-8X^6.                            (R18)

Then a^3=Q(c), P(c)=0, and a=3Q(c)^2/(2c^2).
The last formula follows from a^6/a^5 and f=0.
It also verifies directly from P(c)=0 that a^3=Q(c) and a^5=2c^2/3.
In particular H=Q(c) is the actual primitive triple field for an affine solution.
If an exact finite computation ever finds a monic irreducible factor with all real nonzero roots, this reconstruction gives a integral automatically from the monic equation a^3=Q(c); it must still check b!=0 and g!=0 and the actual norm.
A merely nonmonic primitive irreducible factor cannot supply an algebraic-integer c.

The polynomial Q has degree5 because u!=0.
Every nonzero real root of P has Q(X)>0 and obeys

    Q(X)/abs(X)^(6/5)=(8/27)^(1/5).

On either open half-line, the derivative of the left side vanishes precisely when

    X Q'(X)-(6/5)Q(X)=0.

This is a nonzero polynomial of degree5.
If P has N_+ distinct positive and N_- distinct negative roots, Rolle's theorem gives at least max(N_+-1,0)+max(N_--1,0) distinct derivative zeros on those disjoint half-lines.
Thus N_++N_-<=7.
Every conjugate of the nonzero integral c is a distinct real nonzero root of P, so

    r_0=[H:Q]=[Q(c):Q]<=7.                         (R19)

Possible zero roots or multiplicities of P do not enter this count.
The minimal polynomial of c is separable, so a repeated root of P cannot enlarge r_0.

Next consider all3-primes of H.
Use the integer normalization and variables of(R16).
If3 does not divide v, then C>0 and b=u c+v is a3-adic unit.
The residual equation is

    b^2(1-2s b^3)=a^3-s c^3.

Since C>A, its right side has valuation3A.
Put D_0=1-2s v^3, a fixed nonzero rational integer.
For every integer v prime to3, v^3 is congruent to1 or-1 modulo9.
Thus D_0 is congruent to-1 or3 modulo9, and its rational3-adic valuation is exactly0 or1.
In expanding 1-2s(u c+v)^3-D_0, the three nonconstant terms have valuations at least e+C, e+2C and3C.
Since C=(e+5A)/2>=e/2>0, all three exceed e.
Consequently

    3A=v_p(D_0)
       =0 for EVERY3-prime if v_3(D_0)=0,
       =e for EVERY3-prime if v_3(D_0)=1.           (R20)

In the first global case A=0 and2C=e, so every3-prime ramification index is even and r_0 is even.
In the second global case A=e/3 and C=4e/3, so every such index is divisible by3 and3 divides r_0.
This uniform alternative is determined by ONE fixed rational D_0.
It is not a primewise arbitrary alternative permitting a mixture of indices2 and3 in degree5.

If3 divides v, let k=v_3(v)>=1, independent of the prime of H.
Both c and v have positive valuation, so B>0.
By(R16), 2B=3A and C>B.
In b=u c+v the first summand has valuation at least C>B, so B=v_p(v)=k e.
It follows that

    A=2k e/3, C=(3+10k)e/6.                        (R21)

Since3+10k is odd and C is an integer, e must be even at every3-prime.
Thus r_0 is even in this case also.
Combining all cases with(R19) gives

    r_0 in{2,3,4,6}.                               (R22)

The complete weighted identity r_0=sum_(p|3)e_p f_p is used here, with every prime and its residue degree retained.

For r_0<=4, C178 already gives abs(Norm_H(g))>=2^r_0.
If r_0=6, every2-prime has e<=6.
An index e=5 would force its residue degree to be1 and leave total degree1 for the other2-primes.
That would give an unramified2-prime, excluded by C178.
Every remaining index is one of1,2,3,4,6; index1 is itself excluded, and for2,3,4,6 one has min(e,6rem_5(e))=e.
C178's full weighted bound therefore again gives abs(Norm_H(g))>=2^r_0.
Finally the norm tower gives

    abs(Norm_F(g))=abs(Norm_H(g))^[F:H]
                 >=2^(r_0[F:H])=2^[F:Q],

which proves(R17) without replacing the original exponent by an unpaid smaller degree.

For the additional odd-v impossibility, first suppose u is odd too.
At a2-prime, C>0 would make b=u c+v a unit, contrary to C178's equivalence B=0 iff C=0.
Thus b and c are both units at every2-prime, e is divisible by5, and reduction gives

    cbar^3+(cbar+1)^2=cbar^3+cbar^2+1=0.

The cubic X^3+X^2+1 has no root in F_2 and is irreducible there.
Each residue degree is consequently divisible by3.
Every product e_p f_p is divisible by15, contradicting(R19).
If u is even and v odd, b is a unit at every2-prime directly.
Again C=0 and5 divides every e, so5 divides r_0, contrary to(R22).
This proves the entire odd-offset exclusion.

The affine result establishes a genuine restricted norm floor and a complete impossibility branch.
It does not prove that arbitrary integral b,c satisfy an integer affine relation, and no monogenic-order or bounded-coordinate assertion is inserted.
It therefore leaves the original nonaffine D37 question open.
No larger coefficient scan, new numerical evidence or relaxation of total reality is used.

<a id="inputs-and-boundaries"></a>
## Exact inputs and checking boundaries

| Input | Actual role and limit |
| --- | --- |
| [C178 local theorem](Yin_C_G0178_v1.md#statement) and [complete proof](Yin_C_G0178_v1.md#argument) | Exact2-prime G=3C, unit equivalences, low-ramification full norm bound, and exclusion of any unramified2-prime. Used after the actual affine field H is identified. |
| [C178 accepted assessment](Yin_C_G0178_v1.md#decision-whole-reviewed-2026-10-20) and [R447](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Independent upstream finding and adoption at that exact local scope; this author does not independently re-review his own C178. |
| [C180 rational-b exclusion](Yin_C_G0180_v1.md#rational-b-exclusion) and [accepted assessment](Yin_C_G0180_v1.md#decision-whole-reviewed-2026-10-20) | Only the u=0 case, where b is a nonzero rational integer. No nonrational residual bound is imported. |
| [R451](../audits/reviews/Yin_R_G0451_v1.md#c180-whole-rational-branch-finding) | Independent upstream whole review of the three contributors' C180 argument; not a review of this affine extension. |
| [Original singleton inquiry](../ledger/Yin_L_G0438_v1.md#unbuffered-reduction) | Original question and extraction context only; no mutable draft supplies a logical premise. |

The remaining proof uses elementary valuations, integer residue fields, Rolle's theorem, separability and full field-norm/prime-decomposition identities, with every specific application supplied above.
The proposed finite affine test motivated the elimination but no J111 output, factorization, root approximation or finite scan is an input.
This result does not strengthen any unexamined source theorem or claim an independent source-proof audit.
The author reconstructed every3-prime cancellation, both complete constant-term cases, the globally uniform D_0 alternative, the two-half-line root count, actual primitive degree, r_0=6 index5 exclusion, original norm tower, zero parameters and both parity cases.
No missing general residual norm bound is assumed at any step.
Independent whole review and adoption remain separate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:21 |
| status | open |
| reason | Register the complete3-prime companion theorem and infinite integer-affine norm floor, including the rational/zero/odd-offset impossibilities and full original norm cost, for independent review. The arbitrary nonaffine singleton remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete companion and affine theorem](#statement) | Full original totally real integral domain, every3-prime, all integers u,v, primitive-field range, full2^r norm floor and u=0/v=0/odd-v impossibilities. |
| argument | [Complete proof](#argument) | Both retained proof sections and R16--R22, all valuation alternatives, real-root count, field reconstruction, residue weights, r_0=6 boundary and original norm tower. |
| dependency | [C178 complete local proof](Yin_C_G0178_v1.md#argument) | Exact2-prime formulas, unit equivalence, restricted norm floor and unramified-prime impossibility; no unrestricted conclusion. |
| dependency | [C180 rational-b proof](Yin_C_G0180_v1.md#rational-b-exclusion) | Excludes u=0 after rational integrality is explicit. |
| support | [Complete input and contributor boundaries](#inputs-and-boundaries) | Three proof contributors, elementary inputs, exact upstream independent findings and no numerical or general-nonaffine transfer. |
| support | [C178 independent review](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | The accepted upstream valuation theorem only. |
| support | [C180 independent review](../audits/reviews/Yin_R_G0451_v1.md#c180-whole-rational-branch-finding) | The accepted upstream rational-coordinate theorem only. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T10:28 |
| status | proved |
| authority | Internal adoption within Yin's selected residual-singleton continuation. |
| reason | Adopt the exact3-prime companion and full integer-affine theorem after noncontributor whole R453. Every pair u,v of rational integers is covered with the original2^r norm floor; u=0, v=0 and odd offsets are excluded. The full proof uses no finite computation and does not extend to arbitrary nonaffine integral pairs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete companion and affine theorem](#statement) | Full original totally real integral domain, every3-prime, all integers u,v, primitive-field range, full2^r norm floor and u=0/v=0/odd-v impossibilities. |
| argument | [Complete proof](#argument) | Both retained proof sections and R16--R22, all valuation alternatives, real-root count, field reconstruction, residue weights, r_0=6 boundary and original norm tower. |
| dependency | [C178 complete local proof](Yin_C_G0178_v1.md#argument) | Exact2-prime formulas, unit equivalence, restricted norm floor and unramified-prime impossibility; no unrestricted conclusion. |
| dependency | [C180 rational-b proof](Yin_C_G0180_v1.md#rational-b-exclusion) | Excludes u=0 after rational integrality is explicit. |
| support | [Complete input and contributor boundaries](#inputs-and-boundaries) | Three proof contributors, elementary inputs, exact upstream independent findings and no numerical or general-nonaffine transfer. |
| support | [C178 valuation finding](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | The accepted upstream valuation theorem only. |
| support | [C180 rational-coordinate finding](../audits/reviews/Yin_R_G0451_v1.md#c180-whole-rational-branch-finding) | The accepted upstream rational-coordinate theorem only. |
| review | [Whole integer-affine finding](../audits/reviews/Yin_R_G0453_v1.md#c182-whole-integer-affine-finding) | Entire statement and R16--R22, all valuation and real-root cases, global three-adic alternative, actual primitive-field range and original norm tower. |

