---
author: Yin
---

# Reciprocal midpoint decompositions and the symmetric-word return tail

Date: 2026-10-10T14:59.
Human author: Yin.
Provenance: project deduction.
Organization requested by Yin; [G0001 remains paused](../tasks/Yin_T_G0001_v1.md#decision-human-pause-after-closeout).

## Current assessment
[Selected decision](#decision-current-first-return-proof-home)

## Assessment history
### Decision initial
The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-10T14:59 |
| status | open |
| reason | The complete local candidate is fixed for reuse; historical author self-checks are retained, but no acceptance review or proved judgment is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only the enumerated conclusions under their stated hypotheses and exclusions. |
| argument | [Argument](#argument) | The selected retained derivations and declared fixed inputs; open transfers and source-screen conclusions are excluded. |
| dependency | [Reciprocal trace domain](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Quadratic trace-field extension and monic integral trace polynomial under the exact nontorsion reciprocal minimal-polynomial hypotheses. |
| dependency | [Actual first-return law](../ledger/Yin_L_G0154_v1.md#actual-first-return-paths) | Original digit weights, first-return prefixes and absence of nontrivial returns at lengths at most d. |


### Decision open-candidate

| Field | Value |
| --- | --- |
| date | 2026-10-20T21:22 |
| status | open |
| reason | Both parity identities, the actual conditional product and the symmetric-word tail remain candidates awaiting an applicable acceptance review; the arithmetic common-factor estimate, complement tail and coupled first-return prefixes are unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only Parts A-C under the original nontorsion reciprocal-unit and unchanged digit-law hypotheses; no Salem or total-reality assumption is added. |
| argument | [Retained candidate](#argument) | Complete equations (1)-(7), both parity guards, actual nine-point law, empty mask and complete geometric sum for the two specified word classes; no full first-return factorization or entropy improvement. |
| dependency | [Trace-field domain](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Exact quadratic trace-field extension and monic trace polynomial under the stated reciprocal nontorsion hypotheses. |
| dependency | [Original first-return law](../ledger/Yin_L_G0154_v1.md#actual-first-return-paths) | Unchanged digit weights, every earlier nonreturn prefix and absence of nontrivial returns at lengths at most d. |


### Decision current-trace-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:54 |
| status | open |
| reason | Select the complete retained original trace proof at its current C243 home without changing the candidate, proof, open assessment or any unresolved transfer and acceptance obligation. Historical fixed inputs remain inspectable. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Only Parts A-C under the original nontorsion reciprocal-unit and unchanged digit-law hypotheses; no Salem or total-reality assumption is added. |
| argument | [Retained candidate](#argument) | Complete equations (1)-(7), both parity guards, actual nine-point law, empty mask and complete geometric sum for the two specified word classes; no full first-return factorization or entropy improvement. |
| dependency | [Trace-field domain](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Exact quadratic trace-field extension and monic trace polynomial under the stated reciprocal nontorsion hypotheses. |
| dependency | [Original first-return law](../ledger/Yin_L_G0154_v1.md#actual-first-return-paths) | Unchanged digit weights, every earlier nonreturn prefix and absence of nontrivial returns at lengths at most d. |


### Decision current-first-return-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T14:07 |
| status | open |
| reason | Select the complete unchanged original first-return interface at its current C365 proof home, retaining the C243 trace input, exact statement and argument scopes, complete candidate proof and open assessment. This input-location maintenance adopts no acceptance finding; every old decision and fixed input remains inspectable. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unchanged scoped input](#statement) | Only Parts A-C under the original nontorsion reciprocal-unit and unchanged digit-law hypotheses; no Salem or total-reality assumption is added. |
| argument | [Unchanged scoped input](#argument) | Complete equations (1)-(7), both parity guards, actual nine-point law, empty mask and complete geometric sum for the two specified word classes; no full first-return factorization or entropy improvement. |
| dependency | [Unchanged scoped input](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Exact quadratic trace-field extension and monic trace polynomial under the stated reciprocal nontorsion hypotheses. |
| dependency | [Unchanged scoped input](Yin_C_G0365_v1.md#actual-first-return-paths) | Unchanged digit weights, every earlier nonreturn prefix and absence of nontrivial returns at lengths at most d. |

## Statement

Let alpha be a nontorsion algebraic unit with monic irreducible reciprocal minimal polynomial P of degree d=2r.
Put x=alpha+alpha^(-1), K=Q(alpha), F=Q(x), and P(t)=t^r T(t+t^(-1)).
Use independent digits eta_i with probabilities w_0=1/2 and w_(+1)=w_(-1)=1/4, the recurrence X_0=0, X_(l+1)=alpha X_l+eta_l, and Q_n(t)=sum_(i=0)^(n-1) eta_i t^(n-1-i).

**A. Both parity decompositions.** The integral C_j,U_j,D_j,E_j bases, paired digits and polynomials A_+,A_- explicitly defined in [the midpoint identities](#masked-chebyshev-midpoint-identities), equations (1)--(3), give their displayed exact decompositions of 2 alpha^(-floor(n/2))Q_n(alpha).
For n>=1, X_n=0 if and only if T divides both A_+ and A_- in Z[X], allowing either polynomial to be zero.
No Salem or total-reality hypothesis is added.

**B. Actual conditional product.** Under the nine-point transformed law (4), condition on the entire shared mask, every inactive output and, for odd length, the central digit.
The active signs in the two paired sums are then independent fair-sign families.
The endpoint probability p_n=Pr(X_n=0) is exactly the conditional-product expectation (5), with the bases and targets defined in [that section](#shared-mask-conditional-independence).
This is not a factorization of first-return probability; earlier-prefix nonreturn conditions remain coupled.

**C. Complete tail for two specified word classes.** Let f_n^sym be the probability of first return at n with a palindromic or antipalindromic original digit word.
For 1<z<sqrt(8/3) and a=3z^2/8,

    sum_(n>2r) f_n^sym z^n <= a^r(2a+3z/2)/(1-a).

This controls only those two word classes.
It gives no complete-return tail estimate, entropy improvement or uniform Mahler gap.
The common-factor estimate beyond rank, all-length costs and earlier-prefix transfer remain unresolved.
This complete local candidate is registered without an acceptance verdict.

## Argument

Parts A--C select the complete retained sections 1--3, equations (1)--(7), including both parity guards, empty-mask convention and the full convergent geometric sum.
Section 4 retains the old rank/entropy obstruction and missing arithmetic estimate.
Section 5 is a bounded, unadopted source screen and supplies no proof premise.
The historical record contains author self-checking, not a completed fixed acceptance review.

## Organization and retained complete draft

The full original D G0006 body follows, preserving all formulas, titles, open questions, source screens, contribution disclosures and historical reviews.
Only heading depth and relocated links change.
Historical descriptions as a working draft, unadopted result or pending fixed review refer to the original date; the Current assessment above owns the present judgment.
Fixing this record does not reopen exploration.
Necessary programs/data remain in their existing J groups.
The old D can be removed only after full-body preservation and consumer repair checks.

### Unadopted candidate: midpoint trace relations with a shared random mask

Date: 2026-10-09.
Bounded G0001/S_G0007 work by the assigned execution_and_deliverables AI for Yin.
This is self-checked exploratory work, not an adopted result or a completely independently reviewed proof.
No new entropy bound, uniform gap, novelty claim, numerical enumeration, or new source premise is asserted.
The open step is an arithmetic bound for the complete weighted return law, not the midpoint identity itself.

The direct fixed interfaces read for this test were the [reciprocal trace domain](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain), its [entropy boundary](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-entropy-boundary), the [same-event warning](../ledger/Yin_L_G0032_v1.md#same-event-house-obstruction), the [basis-block bound](../ledger/Yin_L_G0094_v1.md#independent-basis-block-collision), and the [actual first-return law](../ledger/Yin_L_G0154_v1.md#actual-first-return-paths).
The complete original trace and same-event arguments are now retained in [C243](Yin_C_G0243_v1.md#reciprocal-trace-domain) and [C239](Yin_C_G0239_v1.md#same-event-house-obstruction); this adds no independent acceptance review or entropy improvement to this open candidate.
The complete original [basis-block collision proof](Yin_C_G0287_v1.md#independent-basis-block-collision) now has the same current mathematical responsible home, without changing the dated list of actual inputs read for this candidate.
The earlier proofs are reused only at those fixed scopes.

<a id="masked-chebyshev-midpoint-identities"></a>
#### 1. Exact midpoint equations at both parities

Let alpha be a nontorsion algebraic unit whose monic irreducible minimal polynomial P is reciprocal of degree d=2r.
Set x=alpha+alpha^(-1), K=Q(alpha), F=Q(x), and P(t)=t^r T(t+t^(-1)).
L66 gives [K:F]=2, with T the monic integral minimal polynomial of x, and the nontrivial automorphism sigma(alpha)=alpha^(-1).
No Salem or total-reality assumption is needed here.
In particular alpha is neither 1 nor -1.

Use the integral polynomials

    C_0=2, C_1=X, C_(j+1)=X C_j-C_(j-1),
    U_(-1)=0, U_0=1, U_(j+1)=X U_j-U_(j-1).

Then C_j(x)=alpha^j+alpha^(-j) and alpha^j-alpha^(-j)=(alpha-alpha^(-1))U_(j-1)(x).
Each U_j is monic of degree j, and each C_j for j>=1 is monic of degree j.
Let eta_i be the unchanged independent difference digits, with probabilities w_0=1/2 and w_1=w_(-1)=1/4, and put

    Q_n(t)=sum_(i=0)^(n-1) eta_i t^(n-1-i),
    X_0=0, X_(l+1)=alpha X_l+eta_l.

Thus X_n=Q_n(alpha), and a particular word has probability 2^(-n-|supp eta|).
Endpoint return means P divides Q_n; first return also requires Q_l(alpha)!=0 for every earlier prefix 1<=l<n.

For n=2h+1, let a_j=eta_(h-j), b_j=eta_(h+j), s_j=a_j+b_j, t_j=a_j-b_j, for 1<=j<=h.
Direct pairing gives

    2 alpha^(-h) Q_n(alpha)
      =A_+(x)+(alpha-alpha^(-1))A_-(x),
    A_+(X)=2eta_h+sum_(j=1)^h s_j C_j(X),
    A_-(X)=sum_(j=1)^h t_j U_(j-1)(X).               (1)

The two prefactors 1 and alpha-alpha^(-1) are F-linearly independent: the second is nonzero and changes sign under sigma.
Therefore

    X_n=0  iff  T divides A_+ and T divides A_-.       (2)

Divisibility is in Z[X], because T is monic and minimal.
A zero polynomial is allowed on either side.

For n=2h, use a_j=eta_(h-1-j), b_j=eta_(h+j), and the same s_j,t_j, now for 0<=j<h.
Set D_j=U_j-U_(j-1) and E_j=U_j+U_(j-1).
The identities

    alpha^j+alpha^(-j-1)=(1+alpha^(-1))D_j(x),
    alpha^j-alpha^(-j-1)=(1-alpha^(-1))E_j(x)

follow from the displayed recurrence, including j=0.
Hence

    2 alpha^(-h) Q_n(alpha)
      =(1+alpha^(-1))A_+(x)+(1-alpha^(-1))A_-(x),
    A_+(X)=sum_(j=0)^(h-1) s_j D_j(X),
    A_-(X)=sum_(j=0)^(h-1) t_j E_j(X).              (3)

Both prefactors are nonzero.
Their ratio (alpha-1)/(alpha+1) changes sign under sigma, so they are F-linearly independent.
Thus (2) also holds at even length, with (3)'s polynomials.

<a id="shared-mask-conditional-independence"></a>
#### 2. Actual pair law and a valid conditional product

For every disjoint pair, the transformed probabilities are exactly

    (s,t)=(0,0):                         1/4;
    (s,t)=(1,1),(1,-1),(-1,1),(-1,-1):  1/8 each;
    (s,t)=(2,0),(-2,0),(0,2),(0,-2):    1/16 each.   (4)

These exhaust the original nine possibilities for (a,b).
In particular the unconditional s and t are not independent: for example Pr(s=t=0)=1/4, whereas Pr(s=0)Pr(t=0)=(3/8)^2.

Let I_j=1 exactly when one of a_j,b_j is nonzero and the other is zero.
The I_j are independent Bernoulli(1/2).
Conditional on I_j=1, the four (s_j,t_j)=(+/-1,+/-1) have equal probability, so s_j and t_j are independent fair signs.
Conditional on I_j=0, the probabilities are 1/2 at (0,0) and 1/8 at each of the four nonzero axis points in (4).

Condition on the whole mask I and every output (s_j,t_j) at I_j=0; at odd length also condition on eta_h.
Call this information H.
At the active positions J={j:I_j=1}, the entire s-sign family and the entire t-sign family are independent fair signs, independent across j.
Write u_j,v_j for the two polynomial bases in (1) or (3), evaluated at x, and let b_+,b_- in F be minus the respective contributions from the conditioned coordinates, including 2eta_h at odd length.
If p_n=Pr(X_n=0), the exact endpoint identity is

    p_n=E_H[
      Pr(sum_(j in J) eps_j u_j=b_+ | H)
      Pr(sum_(j in J) eps'_j v_j=b_- | H)],            (5)

where eps and eps' are independent fair signs.
This also covers an empty active set with the usual empty-sum convention.
It is legitimate conditional independence of different digits after the stated change of variables; it does not multiply the same collision event at different field embeddings.

Equation (5) is not a factorization of f_n, the first-return probability.
The earlier-prefix conditions involve the original a_j,b_j and couple the two sign families.
Dropping them gives only the endpoint upper bound f_n<=p_n.
A putative first-return use must keep those conditions, or prove an adequate all-time upper bound after dropping them.

<a id="palindromic-weighted-tail-screen"></a>
#### 3. A complete weighted-tail bound for two special word classes

Call a word palindromic if eta_i=eta_(n-1-i), and antipalindromic if eta_i=-eta_(n-1-i).
At odd length the latter requires eta_h=0.
By the monic triangular bases in (1) and (3), A_- is identically zero exactly for palindromic words, and A_+ is identically zero exactly for antipalindromic words.
At odd length, the basis 1,C_1,...,C_h also makes the central condition explicit.
Consequently a returning word outside these two classes has two nonzero polynomials A_+,A_- with the common degree-r factor T.

Each pair has

    Pr(a=b)=Pr(a=-b)=sum_a w_a^2=3/8.

For n=2h the probabilities of the two classes are each (3/8)^h.
For n=2h+1 they are respectively (3/8)^h and (1/2)(3/8)^h.
Their intersection is the all-zero word, which is not a first return at n>1.
Let f_n^sym denote the probability of a genuine first return whose word is in either class.
In particular

    f_(2h)^sym <=2(3/8)^h,
    f_(2h+1)^sym <=(3/2)(3/8)^h.                    (6)

Every nontrivial first return has n>d=2r, by the nonzero leading coefficient and irreducibility argument in L154.
For any real 1<z<sqrt(8/3), put a=3z^2/8<1.
Summing all admissible lengths, not a finite truncation, gives

    sum_(n>2r) f_n^sym z^n
       <=[2a^(r+1)+(3z/2)a^r]/(1-a)
        =a^r(2a+3z/2)/(1-a).                         (7)

The even lengths start at 2r+2 and the odd lengths at 2r+1.
This is a uniform convergent upper bound for the two specified word classes, with exponential decay in r for fixed z in this interval.
It says nothing comparable about the complement.
Its probability calculation uses the digit law alone; it is not new arithmetic exclusion of actual near-one inputs.
In particular it cannot replace L154's complete-tail obligation by a small contribution from this subclass.

<a id="masked-chebyshev-unresolved-cost"></a>
#### 4. What would make this candidate substantive

In the even-length formula with h>=r, each of D_0,...,D_(r-1) and E_0,...,E_(r-1) is a monic basis of polynomials of degree below r.
Their evaluations form a Q-basis of F.
The two prefactors in (3) are independent over F.
Thus the combined rational rank of these first r pairs is exactly 2r=d; (a,b)->(s,t) is invertible over Q.
The rank calculation therefore does not improve the existing L94 basis-block budget by replacing d with r.
The odd formula must retain its central coordinate; no rank assertion obtained by deleting that coordinate is used.

Ordinary multiplication by x on Z[x] has Mahler entropy m(T), not m(P)/2; L66 already distinguishes these costs.
Neither changing to the trace field nor splitting the two polynomial equations licenses using the wrong entropy or treating the common mask as independent.

The concrete unresolved arithmetic object is the simultaneous weighted count of two nonzero polynomials (1)/(3), with the actual correlated law (4), having the fixed common factor T.
Formula (5) presents two masked Chebyshev atom problems, with correlated targets inherited from the same inactive pairs.
A useful continuation must supply an estimate beyond generic dimension/rank information, retain every length and all degree/input constants, and either enforce every nonzero earlier prefix or justify its removal in a sufficient full-tail upper bound.
No such estimate is proved here.
Rewriting renewal subcriticality or reusing only (7) does not discharge it.

The coordinator proposed the bounded reciprocal midpoint test.
The assigned AI derived and self-checked both parity identities, the exact pair law and conditional independence, the special-word tail sum and the stated rank/cost boundary.
The assigned AI was also a contributor to old L154; that proof is only reused at its fixed interface here.
No complete independent review of this new candidate has occurred.
No source theorem about random common factors is adopted by this file.


<a id="masked-chebyshev-source-screen"></a>
#### 5. Bounded source screen, 2026-10-09

The separately assigned growth_arithmetic_status AI first checked the local registry, the NV11 audit and S_G0007's retained finite-field search.
The new question was whether a common-factor or small-ball estimate could handle the actual masked pair above beyond the existing rank budget.
It then sent exactly these generic public queries in one search call:

- random Chebyshev polynomials common roots Bernoulli coefficients
- random polynomials common factors independent Bernoulli coefficients
- Salem Bernoulli convolutions entropy carry matrices operator

No local unpublished formula or manuscript text was sent.
Subsequent actions opened or located text in primary source pages/PDFs, without additional search queries.
No PDF was retained, source key allocated, source registered or external theorem adopted.

Gady Kozma and Ofer Zeitouni, *On common roots of random Bernoulli polynomials*, arXiv:1109.2316v1, 2011-09-11 ([exact version](https://arxiv.org/abs/1109.2316v1), [PDF](https://arxiv.org/pdf/1109.2316v1)), was inspected at its model definition, Theorems 1--2, Lemma 2 and related proof passages, not a full proof audit.
The model uses independent random polynomials with all monomial coefficients iid fair signs.
Its common-root bound and fixed-A inverse-concentration threshold do not directly cover a common sparse mask, different Chebyshev bases or conditioned shifts.
An invertible integral basis change does not preserve the coefficient law.
No parity refinement or theorem from this paper is used as proof support.

Jimmy He, Huy Tuan Pham and Max Wenqiang Xu, *Universality for low degree factors of random polynomials over finite fields*, arXiv:2201.06156v2, 2022-02-23 ([exact version](https://arxiv.org/abs/2201.06156v2), [PDF](https://arxiv.org/pdf/2201.06156v2)), was inspected at Section 3.1, Proposition 3.3's basis-block/Holder argument, Theorem 4.1, Proposition 6.2 (PDF page 20) and the main Section 7 statements.
This was not a complete proof audit.
It genuinely covers multiple extension-field evaluations and Hasse conditions, but for independent monomial coefficients.
Even conditionally assuming a separate valid transfer of the present law, its displayed additive error exp[-c n/(D p^2)] at total constraint dimension D does not give exp(-c_0 D) precision at n=O(D).
Achieving that precision from this displayed bound requires a sufficient time cost of order D^2 p^2.
This is neither an established transfer nor a necessary lower bound on actual mixing time.

The screen stopped at these distribution and displayed-estimate limitations.
It does not establish that no suitable theorem exists.
A new source continuation needs a verified distribution transfer and adequate time/error costs, or a result for the actual masked pair.
The earlier-prefix coupling in (5) remains an additional obligation.
These discovery findings are unadopted applicability notes, not theorem premises for Sections 1--4 or a literature proof-review milestone.