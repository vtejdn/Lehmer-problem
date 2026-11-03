---
author: Yin
---
# Unbounded averaged short-lcm energy on squarefree divisor downsets

Date: 2026-10-13T04:24.
Human author Yin.
The averaged_lcm author supplied the entire original D23 frozen at12:20.
Root independently whole-reviewed that original in R332 and NOW authors this fixed statement/extraction, becoming a contributor to this actual wrapper.
R332 covers the original only.
This newly authored extraction awaits a distinct noncontributor review before adoption.

## Statement

For a positive squarefree integer Q and real t>=1 put

    D_Q(t)={a:a divides Q, a<=t},
    W_Q(t)=sum_(a in D_Q(t))phi(a),
    E_Q(t)=sum_(a,b in D_Q(t),lcm(a,b)<=t)phi(a)phi(b),
    K_Q=max_(N divides Q) E_Q(N)/(N W_Q(N)).

Pairs are ORDERED and include every diagonal; every active capacity is the full INTEGER phi(a).
The support is nonempty and divisor-closed.
Then

    K_Q >= (1/2) product_(p divides Q)
                          (2-p^(-2))/(2-p^(-1)).

For ANY fixed real B>=1, let p_j be the increasing primes exceeding B, Q_j their successive products, and N_j the LEAST divisor attaining the displayed finite maximum.
The product lower bound diverges, and therefore

    E_(Q_j)(N_j)/(N_j W_(Q_j)(N_j)) -> infinity,
    M_(N_j)/N_j -> infinity,
    N_j -> infinity,
    W_(Q_j)(N_j)/N_j -> infinity.

Here M_N is exactly C91's maximum of ordered compatible-pair mass divided by total mass over 0<=x_a<=phi(a), 1<=a<=N.
Thus NO absolute finite K satisfies M_N<=K*N for every N.
Equivalently, C91's proposed universal short-pair bound P_2(Y)<=K*Y*W is false, even on squarefree full-capacity divisor downsets excluding any specified finite set of prime factors.
This is a theorem refuting the auxiliary universal premise, not a refutation of C91's valid conditional implication.

For these same selected arrays, at any1<=n<=N_j,

    h(n)=sum_(a in D_(Q_j)(N_j),a divides n)phi(a)
        =gcd(n,Q_j),
    H_(N_j)=max_(1<=n<=N_j)h(n)=N_j,
    H_(N_j)/W_(Q_j)(N_j) -> 0.

No uniformly positive ordered triple density T_(N_j)/W^3 has been proved for this family.
It therefore does NOT refute the direct positive-triple-density-to-linear-capture question.
Nor does it realize these inventories by actual irreducible nontorsion integer-unit polynomials of near-one TOTAL Mahler measure.
Excluding a residue prime only gives necessary order coprimality, without good reduction, actual roots, valuation depths or original norm costs.
The unrestricted same-exponent income gate and G0001 remain unresolved.

The proof is finite: integrate E_Q(t)<=K_Q*t*W_Q(t) against t^-3 on[1,infinity), including t>=Q, and factor the resulting two finite sums into the four exact local pair factors.
Prime-reciprocal divergence alone makes their ratio unbounded; its complete elementary proof and existing DLMF attribution are retained.
Q1, p2, all real thresholds and the exact finite choice of N_j are included.
No native mathematical program, asymptotic prime estimate, numerical optimizer or new external theorem is a premise.

## Current assessment
[Selected decision](#decision-current-prime-input-homes)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:24 |
| status | open |
| reason | Register the unbounded averaged full-capacity divisor-downset family and exact small-capture comparison, preserving the complete original12:20 proof, source/history and whole R332. The universal K premise is refuted by the candidate theorem; this actual wrapper still needs a distinct noncontributor extraction review before acceptance. Triple density, actual near-one realization and G0001 remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Full finite product lower bound, diverging integer family, finite-prime exclusions, H=N and explicit triple/actual-input boundaries. |
| argument | [Complete original proof and history](#argument) | ENTIRE original D23 freeze12:20, all seven anchors, equations1--13, finite integrals, alternate probabilities, sources and limitations. |
| dependency | [C91 exact extremum and premise](Yin_C_G0091_v1.md#statement) | Definition of M_N and interpretation of the proposed universal K; no extremal reduction is needed for this admissible lower construction. Its valid conditional implication remains logically unchanged. |
| dependency | [L17 prime divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only elementary prime-reciprocal divergence and its existing DLMF attribution; the full argument is repeated locally. |
| support | [C94 earlier boundary](Yin_C_G0094_v1.md#statement) | Historical comparison: its row obstruction did not settle the averaged bound. No theorem from its argument is required here. |
| support | [Original whole review](../audits/reviews/Yin_R_G0332_v1.md#averaged-short-lcm-whole-independent-finding) | Complete original12:20 proof only, not prospective review of this new extraction. |


### Decision organized-reviewed

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-13T04:28 |
| status | proved |
| reason | Adopt original whole R332 and distinct actual extraction R334 for the unbounded MASS-NORMALIZED short-lcm counterfamily, all finite prime exclusions and exact H=N comparison. The universal K antecedent in C91 is now refuted; its logical conditional implication remains valid. This theorem does not supply positive uniform triple density, an actual near-one polynomial realization or G0001 completion. Root authored this wrapper and relies on the distinct noncontributor actual finding; all original proof/search/history is retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Full finite product lower bound, diverging integer family, finite-prime exclusions, H=N and explicit triple/actual-input boundaries. |
| argument | [Complete original proof and history](#argument) | ENTIRE original D23 freeze12:20, all seven anchors, equations1--13, finite integrals, alternate probabilities, sources and limitations. |
| dependency | [C91 exact extremum and premise](Yin_C_G0091_v1.md#statement) | Definition of M_N and interpretation of the proposed universal K; no extremal reduction is needed for this admissible lower construction. Its valid conditional implication remains logically unchanged. |
| dependency | [L17 prime divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only elementary prime-reciprocal divergence and its existing DLMF attribution; the full argument is repeated locally. |
| support | [C94 earlier boundary](Yin_C_G0094_v1.md#statement) | Historical comparison: its row obstruction did not settle the averaged bound. No theorem from its argument is required here. |
| support | [Original whole review](../audits/reviews/Yin_R_G0332_v1.md#averaged-short-lcm-whole-independent-finding) | Complete original12:20 proof only, not prospective review of this new extraction. |
| review | [Actual independent extraction](../audits/reviews/Yin_R_G0334_v1.md#c96-averaged-short-lcm-actual-extraction-finding) | Entire actual statement and retained D23, finite threshold and moment factors, divergence, prime exclusions, H=N, source scope and unchanged original/actual boundaries. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:03 |
| status | proved |
| reason | Select adopted C220 as the current complete home of the identical retained L17 elementary prime-reciprocal divergence. Its actual selected adoption and complete needed finite Euler-product/harmonic-series argument were read and matched to the fixed L17 section. Reuse is limited to that elementary divergence and its original attribution, with no discriminant theorem, reciprocal counterexample family or prime-distribution rate added to this input. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Full finite product lower bound, diverging integer family, finite-prime exclusions, H=N and explicit triple/actual-input boundaries. |
| argument | [Complete original proof and history](#argument) | ENTIRE original D23 freeze12:20, all seven anchors, equations1--13, finite integrals, alternate probabilities, sources and limitations. |
| dependency | [C91 exact extremum and premise](Yin_C_G0091_v1.md#statement) | Definition of M_N and interpretation of the proposed universal K; no extremal reduction is needed for this admissible lower construction. Its valid conditional implication remains logically unchanged. |
| dependency | [Retained elementary divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Only elementary prime-reciprocal divergence and its existing DLMF attribution; the full argument is repeated locally. |
| support | [C94 earlier boundary](Yin_C_G0094_v1.md#statement) | Historical comparison: its row obstruction did not settle the averaged bound. No theorem from its argument is required here. |
| support | [Original whole review](../audits/reviews/Yin_R_G0332_v1.md#averaged-short-lcm-whole-independent-finding) | Complete original12:20 proof only, not prospective review of this new extraction. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0334_v1.md#c96-averaged-short-lcm-actual-extraction-finding) | Entire actual statement and retained D23, finite threshold and moment factors, divergence, prime exclusions, H=N, source scope and unchanged original/actual boundaries. |

## Registration and complete preservation

The complete original follows after removal only of its duplicate author/framework frontmatter and demotion of its first heading; all mathematical text, source/search/history, seven explicit anchors and freeze are retained.
After actual extraction review and adoption, root compared the entire original body and repaired exact incoming locators to the retained anchors; the redundant working draft is retired.
No original proof or failed starting direction is abridged.

## Argument

## Averaged short-lcm energy: prime-support and compensation analysis

Current question: decide whether an absolute finite K bounds M_N/N for every positive integer N, where M_N is the supremum of the ordered short-lcm quadratic energy divided by mass under capacities 0<=x_a<=phi(a).
The current C91 reduction permits full-capacity divisor-closed supports.
C94 supplies M_10/10>=66/65 and unbounded oriented single rows but leaves the weighted average open.

This author-owned draft continues that exact unresolved average.
The starting candidates are disjoint-prime amplification and an averaged compensation inequality.
No uniform bound, unbounded family, actual polynomial realization or positive arithmetic income is assumed.

## Starting inputs

- [C91 short-pair reduction and actual conditional transfer](Yin_C_G0091_v1.md).
- [C94 finite lower control and oriented-row obstruction](Yin_C_G0094_v1.md).
- [Active Task contract](../tasks/Yin_T_G0001_v1.md#contract).

## Current status

Exploratory author work started 2026-10-13; not independently reviewed.
Substantive arguments and useful failures will be developed here.
No native mathematical program has yet been run in this pass.

<a id="averaged-short-lcm-reuse"></a>
## Reuse and source boundary

2026-10-13.
The author read the complete C91 statement and finite reduction, the entire C94 proof, and L17's exact `discriminant-divergence` passage.
C91 supplies the definition of M_N and the meaning of the universal K hypothesis; the construction below is already a full-capacity divisor downset, so its lower bound does not require the extremal rounding theorem.
C94's unbounded individual rows are a starting warning only.
The proof below refutes the mass-normalized universal K itself.

The bounded local screen queried short-lcm, short-pair, divisor-downset and totient/lcm terminology in Claims, ledger, source audits, strategies and the canonical bibliography/registry; only C91/C94 and their current route consumers supplied relevant interfaces.
The existing C94 external screen was reused.
An additional primary-source screen on 2026-10-13 used "lcm totient inequality sum pairs divisor closed" and "least common multiple weighted divisor closed sum".
It returned matrix determinant/factor-closed papers and hyperbolic summation leads, but no checked theorem covering the needed truncated quotient.
Their proofs are not inputs.
This bounded screen does not establish novelty or exhaustive coverage.

The only classical divergence used is sum_p 1/p=infinity, already proved and attributed in the argument retained at [C220](Yin_C_G0220_v1.md#discriminant-divergence).
The author re-opened [DLMF 27.11.E8](https://dlmf.nist.gov/27.11.E8), whose displayed prime-reciprocal asymptotic implies that divergence.
Only the divergence, not its rate, is needed.
The self-contained Euler-product/harmonic argument is recalled below; DLMF is source attribution, not an imported unchecked proof, and its original book proof has not been inspected in this pass.
No new source registration or native mathematical program was needed.

<a id="averaged-short-lcm-counterfamily"></a>
## Statement: the averaged short-lcm ratios are unbounded

For a positive squarefree integer Q and real t>=1 define

    D_Q(t)={a:a divides Q and a<=t},
    W_Q(t)=sum_(a in D_Q(t)) phi(a),
    E_Q(t)=sum_(a,b in D_Q(t), lcm(a,b)<=t) phi(a)phi(b).

Pairs are ordered and include every diagonal.
D_Q(t) is a nonempty divisor downset because it contains1, and if b divides a in D_Q(t), then b divides Q and b<=a<=t.
Since lcm(a,b)>=a,b, the membership restrictions on a,b in E_Q(t) are redundant once a,b divide Q and lcm(a,b)<=t.
Every active capacity is exactly the integer phi(a).

Define the finite number

    K_Q=max_(N divides Q) E_Q(N)/(N W_Q(N)).             (1)

Then

    K_Q >= (1/2) product_(p divides Q)
                       (2-p^(-2))/(2-p^(-1)).          (2)

This includes Q1 with the empty product1 and K_1=1.
In particular, for every fixed real cutoff B>=1, list in increasing order the primes p_1,p_2,... exceeding B and set Q_j=product_(i=1)^j p_i.
If N_j is the least divisor of Q_j attaining the finite maximum(1), then

    E_(Q_j)(N_j)/(N_j W_(Q_j)(N_j)) -> infinity.         (3)

Thus M_(N_j)/N_j tends to infinity, and NO absolute finite K can bound M_N<=KN for all positive integers N.
The counterfamily may exclude every prime up to any prescribed fixed B, and hence every prescribed finite set of forbidden prime factors.
It still uses nonempty full INTEGER totient capacities and exact divisor-closed supports, not real relaxations.

Formula(1) is a deterministic finite definition of N_j; no asymptotic estimate, numerical optimizer or uncomputed floating certificate is being used to assert a particular maximizer.
It produces a rigorously specified sequence with the lower bound(2).
It does not give an efficient numerical way to locate a small witness for a desired K.

<a id="averaged-short-lcm-finite-moment-proof"></a>
## Complete finite moment proof

First, the maximum over all real t>=1 of E_Q(t)/(t W_Q(t)) equals the finite maximum(1).
Both W_Q and E_Q change only when t reaches a divisor of Q, because every occurring a and every lcm(a,b) divides Q.
Between successive divisors both numerators W_Q,E_Q are constant, while division by t makes the ratio nonincreasing.
At each jump the right-continuous value is the value at that integer divisor.
For t>=Q, the full divisor identity gives W_Q(t)=Q and E_Q(t)=Q^2, so the ratio Q/t decreases from1.
There is no zero denominator on t>=1; t<1 is not used.
Thus for every real t>=1,

    E_Q(t)<=K_Q t W_Q(t).                               (4)

All sums are finite and all integrals below converge.
Integrating(4) against t^(-3)dt on[1,infinity) yields

    (1/2) sum_(a,b divide Q) phi(a)phi(b)/lcm(a,b)^2
       <= K_Q sum_(a divides Q) phi(a)/a.               (5)

Indeed each ordered pair contributes its weight times the elementary integral from lcm(a,b) to infinity of t^(-3), which is1/[2 lcm(a,b)^2].
Each divisor a on the right contributes its weight times the integral from a to infinity of t^(-2), which is1/a.
Endpoint equalities do not affect an integral.
The integral includes the tail t>=Q explicitly; it is finite on both sides and is not being dropped.

The two finite sums factor exactly over the distinct primes of squarefree Q.
For the denominator sum, a prime may be absent with factor1 or present with factor phi(p)/p=(p-1)/p, so

    sum_(a divides Q) phi(a)/a
       =product_(p divides Q) (2-p^(-1)).               (6)

For the ordered pair sum, at each p the four choices for membership in(a,b) have factors

    1, (p-1)/p^2, (p-1)/p^2, (p-1)^2/p^2.

Their sum is

    1+[2(p-1)+(p-1)^2]/p^2=2-p^(-2),

and therefore

    sum_(a,b divide Q) phi(a)phi(b)/lcm(a,b)^2
       =product_(p divides Q) (2-p^(-2)).               (7)

Equations(5)--(7), whose denominator is positive, prove(2).
They use ordinary totient multiplicativity only for products of distinct primes and keep every ordered pair and diagonal.
The identity sum_(a|Q)phi(a)=Q follows here directly from product_(p|Q)[1+(p-1)]=Q.

<a id="averaged-short-lcm-divergence-and-finite-exclusions"></a>
## Divergence and all finite exclusions

For each prime p>=2 the factor in(2) satisfies

    (2-p^(-2))/(2-p^(-1))
       =1+(p-1)/[p(2p-1)]
       >=1+1/(3p).                                     (8)

The inequality follows from3(p-1)>=2p-1, equivalent to p>=2.
For0<=u<=1, the elementary integral for log gives log(1+u)>=u/2.
Hence(8) implies

    log[(2-p^(-2))/(2-p^(-1))]>=1/(6p).                 (9)

The sum of prime reciprocals still diverges after removing the finitely many primes at most B.
To recall the sufficient self-contained proof: if the full sum converged, then the logarithms of the finite products product_(p<=y)(1-1/p)^(-1) would stay bounded, since -log(1-1/p)<=2/p for every p>=2.
Each such finite Euler product, expanded into geometric series, is the sum of reciprocals of all positive integers whose prime factors are<=y.
It therefore dominates sum_(n<=floor(y))1/n, which is unbounded.
This contradiction proves divergence, and deleting finitely many terms preserves it.
This is the exact elementary argument already retained and attributed in L17; no prime-number theorem or prime-gap result enters.

Apply(9) to Q_j.
Its product lower bound in(2) tends to infinity, proving(3).
For the selected integer N_j, put x_a=phi(a) if a divides Q_j and a<=N_j and x_a=0 otherwise on1<=a<=N_j.
This is an admissible array in the definition of M_(N_j), so

    M_(N_j)/N_j >= E_(Q_j)(N_j)/(N_j W_(Q_j)(N_j)).      (10)

Every active a is coprime to all primes<=B.
This verifies the finite-exclusion assertion without any appeal to an arbitrary-prime-support transport or reuse of the N10 witness's small primes.

For completeness, the diverging ratio cannot hide at finitely many N values: for any admissible capacity array of mass W, its ordered short-pair energy is at most W^2, and W<=sum_(a<=N)phi(a)<=N(N+1)/2.
Consequently M_N/N<=(N+1)/2.
Thus N_j itself tends to infinity.
The same trivial E<=W^2 gives

    W_(Q_j)(N_j)/N_j >= K_(Q_j) -> infinity.            (11)

<a id="averaged-short-lcm-tail-interpretation"></a>
## Equivalent finite probability check

An independent description checks the normalization in(5)--(7), although it is not needed by the proof.
Choose a divisor A of Q with probability phi(A)/Q; these probabilities sum to1.
For squarefree Q, inclusion of p in A is independent across primes and has probability(p-1)/p.
Thus U=Q/A includes p with probability1/p.
Take an independent copy V and put G=gcd(U,V).
Then inclusion of p in G is independent across primes with probability1/p^2.
For R=Q/t with1<=t<=Q,

    W_Q(t)=Q Pr(U>=R),
    E_Q(t)=Q^2 Pr(G>=R),
    E_Q(t)/(t W_Q(t))=R Pr(G>=R)/Pr(U>=R).             (12)

The second equality holds because G=Q/lcm(A,A'), and G>=R already implies U,V>=R.
In particular no extra independence is falsely imposed after conditioning on membership in D_Q(t).
The exact moments are

    E[U]=product_(p|Q)(2-p^(-1)),
    E[G^2]=product_(p|Q)(2-p^(-2)).                    (13)

A uniform tail inequality R Pr(G>=R)<=K_Q Pr(U>=R), also valid for0<R<1 because K_Q>=1 and then both probabilities are1, integrates to E[G^2]<=2K_Q E[U].
For R>Q both probabilities vanish.
This recovers(2) with the same factor1/2; it does not reverse a Markov inequality or use an asymptotic tail approximation.

<a id="averaged-short-lcm-actual-scope"></a>
## Consequence and remaining arithmetic boundary

Before this argument, C91's universal averaged K was open and C94 ruled out only constant1 and a stronger uniform oriented-row method.
Equations(1)--(11) now refute the universal averaged K hypothesis ITSELF on an explicit class of full-capacity divisor downsets.
C91's proved finite reduction and its logically conditional implication remain valid; the false antecedent cannot be invoked as a route to positive-linear actual income.
This does not refute C91's ordinary global-triple-density-to-linear-capture question, which may require another proof or extra actual-input restrictions.

The construction supplies an exact abstract small-capture comparison.
For the particular array at a selected divisor N of Q and any1<=n<=N,

    h(n)=sum_(a in D_Q(N), a divides n) phi(a)
        =sum_(a divides gcd(n,Q))phi(a)=gcd(n,Q).

All divisors of gcd(n,Q) are<=n<=N, so no term is lost.
Thus H_N=max_(1<=n<=N)h(n)=N, attained at n=N because N divides Q.
Equations(3) and(11) therefore give H_(N_j)/W_(Q_j)(N_j)->0.
This comparison has NO positive uniform ordered triple-density premise; none was established or assumed.
A large pair-energy-to-NW ratio is not a lower bound for T_N/W^3.
The abstract family is not being promoted to a counterexample to that missing triple-density implication.

Likewise, no actual monic irreducible nontorsion polynomial with these precise root-order groups, near-one total Mahler measure, good reduction, original-degree interpretation or full norm income has been constructed.
Excluding a fixed residue prime from the orders removes only a necessary elementary obstruction; it does not prove such a realization.
No prime valuation depths, all-prime norm total or paid auxiliary costs have been discarded to claim success.
The same-exponent requirement A(n)>=eta*d at n<=C*d in the unchanged G0001 contract remains unresolved, as does an unrestricted positive Mahler gap or an actual zero-gap family.

The useful next step is therefore to pursue the true triple-density implication directly, or identify and prove an additional restriction on ACTUAL small-measure residue inventories that rules out this abstract counterfamily.
Repeating the now-refuted universal K argument, or transporting the unbounded pair ratio into a triple-density claim without proof, would not advance that task.

<a id="averaged-short-lcm-author-freeze"></a>
## Entire author freeze

2026-10-13T04:20.
Entire author-complete artifact held for review.

The author has checked all definitions, finite maximum endpoints, the t>=Q tail, absence of zero denominators, termwise elementary integrals, four local ordered-pair factors, squarefree multiplicativity, Q1, p2, fixed-prime exclusions, the exact prime-divergence use, admissibility in M_N, N_j escape, H_N=N and the missing triple-density/actual-realization boundary.
Root assigned the question and later asked for complete endpoints/source scope; root supplied no mathematical derivation.
The draft's author derived both the initial probability formulation and the finite-integral proof.
All new mathematics is author-checked only, pending a separate whole independent review.
No native research program, numerical optimization, computation group, formal assistant or remote Git operation occurred in this pass.
This entire artifact, including its starting question, search history, formulas(1)--(13), source limits and unsuccessful earlier candidate descriptions, is now held unchanged for whole review.
