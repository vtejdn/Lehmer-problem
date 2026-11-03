---
author: Yin
---
# Exact two-adic cost of the unbuffered residual singleton

Date: 2026-10-20T09:44.
Human author Yin.
The entropy_attainment_bridge agent supplied the complete new valuation argument and its field parametrization.
Root assigned the question and coordinated retention, but contributed no step of this argument.
Root's subsequent source-existence and archimedean suggestions are outside this candidate proof.
The author previously contributed the distinct integer-q>=2 comparison in the continuing D37 inquiry; this is author work, not an independent review of that contribution.

<a id="statement"></a>
## Exact theorem statement

Let F be a totally real number field of degree r and let a,b,c be nonzero elements of its ring of integers.
Fix s in{1,-1} and suppose

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.                                  (1)

For each prime ideal p over2, normalize v_p to have value group Z, and write

    e_p=v_p(2), f_p=[O_F/p:F_2],
    A_p=v_p(a), B_p=v_p(b), C_p=v_p(c), G_p=v_p(g).

All these element valuations are finite nonnegative integers and e_p>0.
Then

    5A_p=e_p+2C_p, A_p>0,
    e_p+5B_p>3C_p, G_p=3C_p.                         (2)

If G_p<e_p, there is an integer k_p>=0 with

    C_p=2k_p, B_p=3k_p,
    A_p=(e_p+4k_p)/5,
    k_p congruent e_p modulo5, G_p=6k_p<e_p.           (3)

Consequently, with rem_5(e) the least residue in{0,1,2,3,4},

    v_2(abs(Norm_F(g)))
      >= sum_(p|2) f_p min{e_p,6 rem_5(e_p)}.         (4)

If the right side is at least r/2, then abs(Norm_F(g))>=2^(r/2).
If every e_p<=4, the stronger bound abs(Norm_F(g))>=2^r holds.
In particular this stronger implication holds for every possible triple(1) in a totally real field of degree at most4.
The existence of even one unramified prime over2 excludes(1) altogether.
At each p over2,

    G_p=0 iff C_p=0 iff B_p=0,
    G_p=0 implies5A_p=e_p.                           (5)

Thus if g is a global unit then every e_p is divisible by5 and5 divides r.
These necessary conditions do not assert existence of a local or global residual triple.
They do not give the original exponential norm floor for arbitrary ramification.

The exact field parameter t=c/(3a^2) satisfies

    a=6t^2, c=108t^5,
    b^2-216t^6+s(1259712t^15-2b^5)=0.                (6)

Here t need not be integral, while a is totally positive.
The valuation conclusions use no total-reality premise beyond the stated original domain; total positivity is used only in this last assertion about a.
Every norm is the full F-norm, with no smaller own-field degree substituted for r.

<a id="argument"></a>
## Complete argument

Fix p over2 and suppress its subscript.
Since3 is a p-adic unit, the first equation of(1) gives5A=e+2C.
Since A,C are nonnegative and e>0, A>0.
Suppose e+5B<=3C.
The defining two terms of g would then give G>=e+5B>2B.
The residual identity b^2-a^3=-s g forces v_p(b^2-a^3)>2B, which is possible only if2B=3A.
The first valuation identity would now imply

    e+5B=e+15A/2
         >15A/2-3e/2=3C,

contradicting the supposition.
Therefore e+5B>3C.
The two summands defining g have distinct valuations, and the smaller is3C, so G=3C.
This proves(2) without discarding possible cancellation at the initially hypothesized equality.

If G=3C<e, the identity5A=e+2C gives C<A.
Since v_p(b^2-a^3)=3C<3A, the b^2 term must have valuation2B=3C.
Hence C=2k and B=3k for some integer k>=0.
The first identity gives A=(e+4k)/5; its integrality gives k congruent e modulo5.
This proves(3).
If3C>=e, then G>=e directly.
In the other case k>=rem_5(e), and thus in all cases

    G>=min{e,6 rem_5(e)}.                            (7)

The ideal norm and complete prime-decomposition identities are

    v_2(abs(Norm_F(g)))=sum_(p|2) f_p G_p,
    sum_(p|2) e_p f_p=r.                            (8)

They retain every prime over2 and every embedding of F.
The first equality and(7) give(4).
Because g is nonzero and integral, its absolute norm is a positive rational integer; its2-primary divisor alone therefore gives the stated lower bounds.
When e<=4, rem_5(e)=e, so min{e,6 rem_5(e)}=e and(8) gives the stronger bound2^r.
Every e_p is at most r, proving the degree-at-most4 specialization.
No claim of residual existence is needed for these implications.

For(5), G=0 is equivalent to C=0 by(2).
Since A>0, the identity v_p(b^2-a^3)=G shows that G=0 is equivalent to B=0.
When C=0, the first identity in(2) reads5A=e.
If g is a global unit these conditions hold at every prime over2, so each e_p is divisible by5.
Then(8) gives5 divides r.
A nonunit norm bound of merely2 would not imply the desired2^(r/2) in arbitrary degree; this unit obstruction is therefore kept separate from(4).

Suppose some p is unramified over2, so e=1.
The low case(3) would require k congruent1 modulo5 and6k<1, impossible.
Thus3C>=1.
The equation5A=1+2C makes A odd, while

    C-A=(3A-1)/2>0.

Consequently v_p(b^2-a^3)=3C>3A, forcing2B=3A and making A even, a contradiction.
This proves the full local impossibility at an unramified prime.

Finally t=c/(3a^2) is a well-defined element of F.
The identity2c^2=3a^5 gives6t^2=2c^2/(3a^4)=a and c^4=9a^10/4, whence108t^5=4c^5/(9a^10)=c.
Substitution into the second equation of(1) proves(6).
At each real embedding, 3a^5=2c^2>0, so a is positive.
Neither this fact nor(6) makes t integral.
This finishes the complete restricted theorem.

<a id="inputs-and-boundaries"></a>
## Inputs, reuse and remaining scope

The logical proof uses only the explicit equations(1), nonzero integral elements, elementary valuation laws and the standard full ideal-norm/prime-decomposition identities(8).
It does not invoke a source theorem with uninspected applicability.
The reuse search reread the actual unbuffered draft and the following fixed comparisons before developing the new argument.
No existing fixed result in that search supplied the full residual valuation calculation.

| Input or relation | Exact role and limit |
| --- | --- |
| [C153v2 radical exclusions](Yin_C_G0153_v2.md#argument) | Context for the original unbuffered reduction; its exclusions are not needed once all hypotheses(1), including g!=0, are explicit. |
| [C155 norm argument](Yin_C_G0155_v1.md#argument) | Comparison only: its stronger singleton estimate assumes e=f=0, a different residual system. |
| [C157v2 buffered family](Yin_C_G0157_v2.md#statement) | Comparison only: the coefficient2 of g^2 supplies a different arithmetic gate. |
| [Original unbuffered inquiry](../ledger/Yin_L_G0438_v1.md#unbuffered-reduction) | Extraction and application context only; no mutable draft supplies a logical premise of this fixed proof. |

This candidate retains exactly the completed R1--R8 deduction originally authored in D37 on2026-10-20.
Its standalone statement also makes explicit every consequence proved in those paragraphs.
No whole-D37 resolution, new numerical calculation, new source acquisition, Haar-to-original transfer or unrestricted Mahler conclusion is asserted.
The later high-ramification field control and source-existence screen are outside this proof.
Root's later suggestions about sparse parametrizations, global points and archimedean products supplied no step used here.
The author checked the two-term cancellation split, the congruence and zero-residue branch, full norm weights, low-ramification floor, unit equivalences, unramified contradiction and nonintegral parameter boundary.
Independent whole review and any adoption remain separate.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-20)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-20T09:44 |
| status | open |
| reason | Register the completed exact local valuation theorem and its full-norm restricted consequence for independent review. The arbitrary-field residual singleton remains unresolved; the candidate does not adopt its own proof or expand the ongoing Task target. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact residual valuation theorem](#statement) | Equations(1)--(6), every2-prime, full norm and r, the low-ramification floor, unit obstruction, unramified exclusion and exact nonintegral parametrization. |
| argument | [Complete elementary proof](#argument) | All cancellation cases, congruences and complete norm identities(7)--(8), followed by the unit, unramified and parametrization arguments. |
| support | [Input and scope account](#inputs-and-boundaries) | Actual elementary inputs, comparison-only C153/C155/C157 scopes, extraction origin and author/nonreview boundaries. |

### Decision whole-reviewed-2026-10-20

| Field | Value |
| --- | --- |
| date | 2026-10-20T09:48 |
| status | proved |
| authority | Internal adoption within Yin's selected continuation of the retained unbuffered singleton inquiry. |
| reason | Adopt the complete exact local valuation theorem after whole independent R447. The result gives the displayed weighted norm floor, all low-ramification consequences, unit restrictions and unramified impossibility; it does not close the arbitrary-field residual norm target or infer existence from necessary conditions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact residual valuation theorem](#statement) | Equations(1)--(6), every2-prime, full norm and r, the low-ramification floor, unit obstruction, unramified exclusion and exact nonintegral parametrization. |
| argument | [Complete elementary proof](#argument) | All cancellation cases, congruences and complete norm identities(7)--(8), followed by the unit, unramified and parametrization arguments. |
| support | [Input and scope account](#inputs-and-boundaries) | Actual elementary inputs, comparison-only C153/C155/C157 scopes, extraction origin and author/nonreview boundaries. |
| review | [Whole valuation finding](../audits/reviews/Yin_R_G0447_v1.md#residual-two-adic-whole-independent-finding) | Exact registered statement and complete self-contained argument, all eight equations and input roles; nonblind coordination and upstream comparison authorship are disclosed. |

