---
author: Yin
---
# Strict short-lcm lower control and failure of uniform oriented-row bounds

Date: 2026-10-13T03:46.
Human author Yin.
The delegated c91_extremum author supplied the entire original D49.
Root independently whole-reviewed that original in R328 and NOW authors this fixed statement/extraction, becoming a contributor to this actual wrapper.
R328 covers only the original entire freeze and does not certify this new extraction.
A distinct noncontributor must inspect the actual statement and retained argument before adoption.

## Statement

For an integer N>=1 define

    M_N=max_{0<=x_a<=phi(a), 1<=a<=N, sum x_a>0}
        sum_{a,b<=N, lcm(a,b)<=N} x_a*x_b / sum_{a<=N}x_a.

Every pair is ORDERED and diagonals are included; phi is Euler's totient.
The accepted C91 permits maximization over full-capacity divisor-closed supports, with the same value even though the displayed variables may be real.

**A. A strict finite lower bound.**
At N=10 the divisor-closed support D={1,2,3,4,5,6,8,9,10}, with x_a=phi(a), has total mass W=26 and ordered compatible mass E=264.
Consequently

    M_10>=132/13, and M_10/10>=66/65>1.

This is a feasible lower certificate, not equality or an optimality assertion.
Hence M_N=N for every N is false.
The finite example forces any putative absolute K with M_N<=K*N to satisfy K>=66/65.
The later [C96](Yin_C_G0096_v1.md#statement) proves that no such finite absolute K exists; that conclusion is distinct from this Claim's finite example and row obstruction.

**B. No absolute constant bounds every oriented smaller-neighbor row.**
Put

    B_N(a)=sum_{1<=b<=a, lcm(a,b)<=N}phi(b), 1<=a<=N.

For every integer R>=2 there is a finite squarefree a whose prime factors all exceed R and whose phi(a)<=a/2.
For EVERY such a, at N=R*a, with F_R=sum_{r=1}^R phi(r),

    B_(Ra)(a)>=phi(a)+(a-phi(a))*F_R,
    B_(Ra)(a)/(R*a)>=F_R/(2R)>=sqrt(R)/8.

In particular sup_{N>=1,1<=a<=N} B_N(a)/N is infinite.
The constructed lower mass consists of b=a and all distinct b=r*g with r<=R and g a proper divisor of a; it uses true integer orders and full totient capacities.
This disproves the stronger row estimate that would suffice, after orienting pairs, for a uniform averaged bound.
It does NOT show that M_N/N is unbounded: the heavy row need not control the mass-normalized average.

**C. Conditional multiplication requires disjoint prime support.**
Suppose D1,D2 are nonempty finite divisor-closed sets whose prime supports are disjoint.
For positive integers N1,N2 with Di subset{1,...,Ni}, let Wi=sum_{a in Di}phi(a) and Ei=sum_{a,b in Di,lcm(a,b)<=Ni}phi(a)phi(b).
Then D={a*b:a in D1,b in D2} is a divisor-closed subset of{1,...,N1*N2} with W=W1*W2, and its short-pair mass E at threshold N1*N2 satisfies

    E>=E1*E2,
    E/((N1*N2)*W)>=(E1/(N1*W1))*(E2/(N2*W2)).

This is an implication under the disjoint-prime hypothesis, not an asserted infinite sequence of strict witnesses.
The single witness in A uses primes2,3,5 and cannot be repeatedly tensored with itself by this rule.
Additional compatible pairs may occur, so no numerator equality is asserted.

**D. Original arithmetic limits.**
The original averaged uniform-K question is now refuted by C96.
The later [C142 v2](Yin_C_G0142_v2.md#statement) supplies the abstract positive-density capture implication at these capacities; automatic positive-density coverage by actual polynomial inputs remains unresolved.
Under C91's retained conditional uniform-K premise, its retained implication still gives one n<=C*d with full original local income at least delta^2*gamma^2*log(2)*d/(4K*C), for positive ordered repeated-label triple density delta, selected original root mass W>=gamma*d and window X<=C*d.
Nothing in A--C realizes the abstract capacities by an actual irreducible nontorsion integer-unit polynomial, supplies a near-one family, establishes positive actual global triple density, bounds all-prime income or resolves G0001.
All original roots, depths, norms and physical costs remain necessary in any arithmetic application.

The proofs use exact elementary finite counts, coprime totient multiplication and the prime-reciprocal divergence argument retained in L17.
DLMF27.11.E8 is existing checked attribution for divergence; its stronger asymptotic is not used.
The original Tao2024 search lead is comparison-only and no theorem from it is a premise.
No native mathematical computation, exhaustive finite optimizer or novelty claim is made.

## Current assessment
[Selected decision](#decision-current-prime-input-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T03:46 |
| status | open |
| reason | Register exact finite lower control, entire arbitrary-row obstruction and disjoint-prime conditional multiplication with the complete original D49 retained. Root reviewed the original whole in R328 and now authors this actual wrapper; a separate noncontributor actual-extraction review is required before adoption. The uniform averaged K premise and unrestricted G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, ordered/diagonal capacities, lower-only finite witness, all-R row theorem, disjoint-prime condition and actual-input exclusions. |
| argument | [Complete original argument](#argument) | ENTIRE original D49 at11:40 freeze, initial question, search roles, nine-row witness, equations1--4, tensor limitation and all unresolved boundaries. |
| dependency | [C91 exact extremum](Yin_C_G0091_v1.md#statement) | Actual definition and full-capacity downset interface; only the explicitly conditional uniform-K-to-income implication is retained, not adopted as unconditional. |
| dependency | [L17 divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only self-contained prime-reciprocal divergence for existence of a finite product with all primes>R; no discriminant theorem or prime-distribution rate is used. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0328_v1.md#short-pair-whole-independent-finding) | Complete actual D49 reviewed before this wrapper; no prospective actual-extraction coverage. Finding relationship: self-reviewed. |


### Decision organized-reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T03:55 |
| status | proved |
| reason | Adopt original whole R328 and distinct actual extraction R330. The finite N10 lower certificate forces any uniform K to be at least66/65; the all-R construction disproves every absolute oriented smaller-neighbor row bound. The disjoint-prime multiplication rule remains explicitly conditional on its actual hypotheses. The averaged M_N/N bound, actual arithmetic density coverage and G0001 remain unresolved. Root authored this wrapper and relies on the noncontributor actual finding; all original source/search/failure history is retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, ordered/diagonal capacities, lower-only finite witness, all-R row theorem, disjoint-prime condition and actual-input exclusions. |
| argument | [Complete original argument](#argument) | ENTIRE original D49 at11:40 freeze, initial question, search roles, nine-row witness, equations1--4, tensor limitation and all unresolved boundaries. |
| dependency | [C91 exact extremum](Yin_C_G0091_v1.md#statement) | Actual definition and full-capacity downset interface; only the explicitly conditional uniform-K-to-income implication is retained, not adopted as unconditional. |
| dependency | [L17 divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only self-contained prime-reciprocal divergence for existence of a finite product with all primes>R; no discriminant theorem or prime-distribution rate is used. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0328_v1.md#short-pair-whole-independent-finding) | Complete actual D49 reviewed before this wrapper; no prospective actual-extraction coverage. Finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0330_v1.md#c94-short-lcm-actual-extraction-finding) | Entire actual statement, complete retained D49, exact counts, all-R construction, tensor condition, source roles, conditional arithmetic interface and preservation; distinct noncontributor finding. Referenced finding relationship: self-reviewed. |


### Decision averaged-premise-resolved

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:34 |
| status | proved |
| reason | Retain the exact already-reviewed finite lower certificate, arbitrary-row obstruction and disjoint-prime conditional multiplication rule. The later independently adopted C96 now proves the averaged quotient itself unbounded, resolving the earlier open boundary beyond this Claim. The original proofs and R328/R330 scope remain unchanged; this decision supplies no triple-density, actual near-one or Task-completion conclusion. See [C96 exact adopted result](Yin_C_G0096_v1.md#decision-organized-reviewed). |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, ordered/diagonal capacities, lower-only finite witness, all-R row theorem, disjoint-prime condition and actual-input exclusions. |
| argument | [Complete original argument](#argument) | ENTIRE original D49 at11:40 freeze, initial question, search roles, nine-row witness, equations1--4, tensor limitation and all unresolved boundaries. |
| dependency | [C91 exact extremum](Yin_C_G0091_v1.md#statement) | Actual definition and full-capacity downset interface; only the explicitly conditional uniform-K-to-income implication is retained, not adopted as unconditional. |
| dependency | [L17 divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only self-contained prime-reciprocal divergence for existence of a finite product with all primes>R; no discriminant theorem or prime-distribution rate is used. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0328_v1.md#short-pair-whole-independent-finding) | Complete actual D49 reviewed before this wrapper; no prospective actual-extraction coverage. Finding relationship: self-reviewed. |
| review | [Actual extraction](../audits/reviews/Yin_R_G0330_v1.md#c94-short-lcm-actual-extraction-finding) | Entire actual statement, complete retained D49, exact counts, all-R construction, tensor condition, source roles, conditional arithmetic interface and preservation; distinct noncontributor finding. Referenced finding relationship: self-reviewed. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:03 |
| status | proved |
| reason | Select adopted C220 as the current complete home of the identical retained L17 elementary prime-reciprocal divergence. Its actual selected adoption and complete needed finite Euler-product/harmonic-series argument were read and matched to the fixed L17 section. Reuse is limited to that elementary divergence and its original attribution, with no discriminant theorem, reciprocal counterexample family or prime-distribution rate added to this input. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--D, ordered/diagonal capacities, lower-only finite witness, all-R row theorem, disjoint-prime condition and actual-input exclusions. |
| argument | [Complete original argument](#argument) | ENTIRE original D49 at11:40 freeze, initial question, search roles, nine-row witness, equations1--4, tensor limitation and all unresolved boundaries. |
| dependency | [C91 exact extremum](Yin_C_G0091_v1.md#statement) | Actual definition and full-capacity downset interface; only the explicitly conditional uniform-K-to-income implication is retained, not adopted as unconditional. |
| dependency | [Retained elementary divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Only self-contained prime-reciprocal divergence for existence of a finite product with all primes>R; no discriminant theorem or prime-distribution rate is used. |
| support | [Original whole finding](../audits/reviews/Yin_R_G0328_v1.md#short-pair-whole-independent-finding) | Complete actual D49 reviewed before this wrapper; no prospective actual-extraction coverage. Finding relationship: self-reviewed. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0330_v1.md#c94-short-lcm-actual-extraction-finding) | Entire actual statement, complete retained D49, exact counts, all-R construction, tensor condition, source roles, conditional arithmetic interface and preservation; distinct noncontributor finding. |

## Registration and complete preservation

The entire original D49 follows, after removing only its duplicate author/framework front matter and demoting its first title; all anchors, original author status, search and failure history, full proofs and freeze remain.
D49 was retained until actual extraction review, adoption, whole-body comparison and incoming-locator repair completed; its redundant draft path is now retired.
No original mathematical text is abridged or silently superseded by this wrapper.

## Argument

## Uniform short-lcm pair extremum under totient capacities

Date: 2026-10-13T03:29.
Human author Yin.
Continuing AUTHOR inquiry by delegated c91_extremum under the root's active G0001 adoption.
This draft owns all new substantive argument and useful failed directions.

## Question and starting scope

Resolve or sharply distinguish the OPEN assertion in [C91](Yin_C_G0091_v1.md#short-pair-finite-downset-reduction): there exists an absolute K with M_N <= K N for every positive integer N, where M_N is the maximum of the short-lcm ordered pair mass divided by total mass under capacities 0 <= x_a <= phi(a).
C91 proves the exact restriction to full-capacity divisor-downsets and M_N >= N.
These are accepted inputs, not new contributions.
Actual polynomial realizations, fixed good primes, full original degrees and local norm costs retain their separate scope.

The first author step is bounded reuse and source search, followed by the smallest discriminating analytic argument.
No new computation is a premise at creation.
An apparent finite identity, a failed stronger K=1 conjecture, or an abstract extremizer must not be promoted to an actual irreducible nontorsion polynomial counterexample.


<a id="reuse-scope-and-primary-leads"></a>
## Reuse scope and bounded primary-source screen

The author inspected the entirety of C91, including its actual input conventions, exact downset reduction and conditional implication.
Direct reused interfaces are C86's circular-capacity/residual-bucket argument, L159's good-prime capacities, and L74's original norm and automatic floors.
The pre-existing C91 argument is sufficient for the conditional arithmetic transfer; no fresh all-prime or near-one assertion is imported.

The local screen queried divisor-closed/downset, short-pair, totient inequalities and lcm extremal terminology in the Claims, ledger, strategies, source-audit collection and canonical literature registry/bibliography.
No existing uniform short-pair theorem was located in that bounded scope.
The local literature file inventory contained no additional unregistered source with those terms supplying the estimate.
This is a bounded result, not a novelty claim.

The external primary-source screen on 2026-10-13 used the exact query families "lcm totient inequality sum pairs", "divisor closed least common multiple sum", "Jordan totient sum inequality", "lcm phi(a) phi(b) inequality", and "least common multiples weights totient".
An author-written exposition, Terence Tao, [Dense sets of natural numbers with unusually large least common multiples](https://terrytao.wordpress.com/2024/07/08/dense-sets-of-natural-numbers-with-unusually-large-least-common-multiples/), 2024-07-08, was read for the displayed reciprocal-lcm/GCD reformulation and its explanation of prime-factor anatomy.
Its weighted reciprocal-energy question differs from C91's truncated short-lcm mass divided by totient mass; it is a related mechanism only, not an accepted proof input.
Search results for Jordan-function means, lcm-sum identities and matrix spectral bounds did not provide the needed capacity-uniform conclusion.
No theorem, source acquisition, earliest-attribution or exhaustive-coverage claim is made.
The exact self-contained finite calculation below needs no unverified external theorem.

<a id="constant-one-short-pair-counterexample"></a>
## A strict finite lower control: the constant one is false

Take N=10 and the divisor-closed set

    D={1,2,3,4,5,6,8,9,10}.

Its full capacities, in the same order, are

    (phi(a))_(a in D)=(1,1,2,2,4,2,4,6,4),
    W=26.

The exact compatible-neighbor masses

    B_a=sum_(b in D, lcm(a,b)<=10)phi(b)

are respectively

    (26,20,12,8,10,6,8,9,10).

These follow from the explicit compatible-neighbor lists:

| a | Compatible b in D | B_a | phi(a) B_a |
| --- | --- | ---: | ---: |
| 1 | 1,2,3,4,5,6,8,9,10 | 26 | 26 |
| 2 | 1,2,3,4,5,6,8,10 | 20 | 20 |
| 3 | 1,2,3,6,9 | 12 | 24 |
| 4 | 1,2,4,8 | 8 | 16 |
| 5 | 1,2,5,10 | 10 | 40 |
| 6 | 1,2,3,6 | 6 | 12 |
| 8 | 1,2,4,8 | 8 | 32 |
| 9 | 1,3,9 | 9 | 54 |
| 10 | 1,2,5,10 | 10 | 40 |

Summing the last column gives the ordered-pair numerator E=264, including every diagonal and both orientations of unequal pairs.
Thus

    M_10 >= E/W = 132/13 > 10,
    M_10/10 >= 66/65.

The explicit neighbor lists independently check the finite summation without requiring a program, floating arithmetic, or a Jordan-function formula.

Consequently the tempting sharpening M_N=N is false and any universal K in C91 must satisfy K>=66/65.
This does NOT disprove existence of any finite universal K, does NOT settle C91's ordinary global-triple-density implication, and does NOT produce an actual irreducible nontorsion polynomial.
It is a fully finite capacity-array lower control.
In particular the threshold10 is a physical time bound, not a claim that W26 is an original polynomial degree already realized.


<a id="oriented-row-bound-failure"></a>
## Why bounding every smaller-neighbor row cannot prove a uniform constant

One natural sufficient method would orient every unequal pair toward its larger integer order and try to bound

    B_N(a)=sum_(1<=b<=a, lcm(a,b)<=N)phi(b) <= K0 N

uniformly in1<=a<=N.
Such a bound would yield E<=2K0 N W for every capacity array.
This PARTICULAR sufficient estimate is false for every absolute K0.
The following complete construction proves that failure; it does not say that the weighted average E/W itself is unbounded.

Fix an integer R>=2.
Choose a squarefree integer a all of whose prime factors exceed R, with

    phi(a)<=a/2.                                             (1)

Such a finite a exists for every R: the sum of reciprocals of primes larger than R diverges, so the finite products of(1-1/p) tend to zero, using log(1-u)<=-u.
This elementary classical fact and its self-contained harmonic/Euler-product proof are already retained in [C220, retained elementary divergence](Yin_C_G0220_v1.md#discriminant-divergence); [DLMF27.11.E8](https://dlmf.nist.gov/27.11.E8) is its already registered source attribution.
The present author read that whole L17 passage and rechecked the displayed DLMF statement online.
No rate of prime distribution is needed, and no new attribution is claimed.

Set N=Ra.
For each1<=r<=R and each proper divisor g of a, put b=rg.
Every prime factor of a exceeds R, so gcd(r,a)=1, every proper g<=a/(R+1), and hence b<a.
Also gcd(rg,a)=g and

    lcm(a,b)=ar<=N,
    phi(b)=phi(r)phi(g).

These b are all DISTINCT as(r,g) varies: their prime factors at most R occur only in r and their prime factors greater than R occur only in g, so that factor split recovers the pair uniquely.
They are distinct from b=a.
The term b=a is separately compatible and has weight phi(a).
Therefore, writing F_R=sum_(r=1)^R phi(r) and using sum_(g|a)phi(g)=a,

    B_(Ra)(a) >= phi(a)+(a-phi(a))F_R
              >= (a/2)F_R,
    B_(Ra)(a)/(Ra) >= F_R/(2R).                           (2)

The last ratio is unbounded as R grows.
An elementary lower estimate avoids importing any asymptotic totient theorem.
For every n>=1,

    phi(n)>=sqrt(n/2).                                    (3)

Indeed for each odd prime power p^e, phi(p^e)>=sqrt(p^e): for e1 this is p-1>=sqrt(p), and for e>=2 it is immediate from p^(e-1)(p-1).
For powers of2 the same inequality holds for e>=2, whereas phi(2)=sqrt(2)/sqrt(2).
Multiplication over prime powers loses at most the one factor1/sqrt(2).
The n1 case holds directly.
Thus there are at least R/2 integers r with R/2<=r<=R, each with phi(r)>=sqrt(R)/2, and

    F_R>=R^(3/2)/4,
    B_(Ra)(a)/(Ra)>=sqrt(R)/8.                            (4)

Equations(1)--(4) prove that no absolute oriented-row constant K0 exists.
All b in the construction are positive distinct integer orders and use the exact full totient capacities; a itself is a valid order no larger than N.
One may take the whole divisor-closed support{1,...,a} to contain the construction.
This does not furnish an extremal lower bound for E/(NW), because that support has substantial total mass and the single heavy row can be exceptional.
Neither arbitrary realization by a polynomial nor positive global triple density has been shown.

The general obstruction includes a particularly transparent R3 calculation.
When a has only prime factors greater than3, the selected b consist of all proper g|a, their doubles and triples, plus a, and have total mass

    phi(a)+(a-phi(a))(phi(1)+phi(2)+phi(3))
      =4a-3phi(a).

If phi(a)<a/3 this already exceeds N=3a.
The unrestricted argument above is stronger: increasing R makes the row/N ratio unbounded, while leaving C91's averaged short-pair question open.

<a id="tensorization-boundary-and-unresolved-average"></a>
## The remaining averaged problem and a bounded next direction

The N10 example cannot be raised to arbitrary powers by reusing its same prime factors.
If two full-capacity downsets D1,D2 use disjoint prime supports, then their product set has unique factorization, is divisor-closed, and has W=W1 W2.
Every pair whose two component lcms are<=N1 and<=N2 has product lcm<=N1 N2.
Consequently its ratio E/(N W) is at least the product of the two component ratios.
This is a direct conditional construction rule.
To deduce unboundedness from it one would need suitable strict lower ratios on infinitely many DISJOINT prime blocks with a divergent product.
The one N10 witness uses primes2,3,5 and supplies no such family.
No disjoint-block amplification or unboundedness theorem is claimed.

The failed reciprocal-energy constant1 estimate is already in C91.
The new calculations rule out both M_N=N and a uniform bound on each smaller-neighbor row.
They leave genuinely different possibilities: a bound after averaging with the actual totient capacities; a prime-by-prime argument that controls exceptional high-degree rows; or a counterfamily with an actually divergent mass-normalized pair ratio.
A bounded next inquiry should test the averaged inequality on divisor-downsets with controlled prime support, preserving the distinction between a heavy row, a lower bound for a finite M_N, and an asymptotic family.
Repeating finite constant tuning alone would not settle the uniform question.

For actual C91 inputs, the mathematical implication remains exactly conditional: IF some absolute K bounds every M_N/N, then positive ordered repeated-label triple density delta, selected mass W>=gamma d and window X<=Cd yield ONE actual n<=Cd with full original income

    A_p(n)>=delta^2 gamma^2 log(2) d/(4KC).

The same original nonzero norm, all d original roots, all actual depths, the physical auxiliary t^n-1 and L168's existing full cost remain mandatory.
None of the negative auxiliary findings here proves failure of that actual density-to-income conclusion, and none removes its open uniform K premise.
No unrestricted Mahler gap or zero-gap family has been obtained.

<a id="entire-short-pair-author-freeze"></a>
## Entire author freeze and review scope

2026-10-13T03:40.
Freeze the entire D49, including the exact starting question, bounded local/primary search and attribution scope, full N10 neighbor table, complete arbitrary-row obstruction(1)--(4), disjoint-prime conditional multiplication rule, every actual-input and unresolved-average boundary, and this freeze.
The author hand-checked all nine neighbor lists and264/26, divisor closure, ordered diagonals, factor uniqueness, proper-divisor bound, coprime totient multiplicativity, the n1/2 cases of(3), finite-prime existence, and the difference between a single row and the weighted average.
No mathematical native program or new J was run.
Root supplied the question and a bounded-pass instruction only, not these constructions or arguments.
All new reasoning is author-checked; a separate whole review is still required before adopting it as reviewed support.
