---
author: Yin
---

# Fixed and asymptotically tight overlap mixtures: full and odd gap obstructions with complete costs

The complete original mathematical argument is retained from [L424](../ledger/Yin_L_G0424_v2.md#overlap-mixture-reuse).
Its original contributions, fixed inputs, useful failures, source inspection and native-execution limits are preserved.
The [original review](../audits/reviews/Yin_R_G0438_v1.md#tight-overlap-whole-independent-finding) keeps its actual original L/J/source bindings, date, relationship declaration and checked scope; it is not retrospectively bound to this C.
The current constructor has read the original proof and historical reviews; any current whole finding by this constructor is SELF.

## Statement

Fix P=t^4-t^3-t^2-t+1, its exterior Salem root beta, a neutral conjugate zeta and O=Z[beta].
Put B=1/(beta-1),S_real=beta B=B+1,rho(q)=abs(q(zeta)) and use the ACTUAL core D={q in O:abs(q_+)<B,abs(q_-)<S_real}, where the real embeddings are beta,beta^-1.
Original chronological digits update q->beta q+eta with p_0=1/2,p_+=p_-=1/4.
Let c_l(v) be the FULL l-digit endpoint integer weight, so Pr(endpoint v)=4^-l c_l(v), and p_l=4^-l c_l(0).
For every n>=5 use ALL original 2n-digit returned words and their product probabilities divided by COMPLETE p_(2n).
For1<=b<n let A_b={0,...,n-b-1},C_b={n+b,...,2n-1}, and K_(n,b)=(E[.|A_b digits]+E[.|C_b digits])/2.
For b>=n put K_(n,b)=Pi_n, the complete-law projection onto constants.
Every kernel is a positive reversible Markov contraction commuting with full negation S eta=-eta.
Use the actual complex midpoint Z_n=-zeta^-n sum_(j<n)eta_j zeta^j.
Define ordinary and odd gaps by their original Dirichlet/variance Rayleigh quotients on nonzero centered real and nonzero odd real functions respectively.

For EVERY fixed probability sequence w_b>=0,sum_b w_b=1, put K_n^w=sum_b w_b K_(n,b),T_B=sum_(b>B)w_b.
The series converges in operator norm.
For EACH fixed B>=2, an actual finite onset N_B independent of w exists such that, for every n>=N_B,

    0<=gap_n<=gap_n^odd<=T_B.

Thus both gaps tend to zero for EVERY fixed distribution.
Finite support gives both gaps exactly zero at every sufficiently late n.
Unbounded support gives EVERY finite n>=5 a strictly positive full-refresh minorization and

    0<T_(n-1)<=gap_n<=gap_n^odd,

hence finite connectivity coexists with vanishing gaps.
The exact midpoint and work bounds are

    D_(K_n^w)(Z_n)<=sum_b w_b min(b,n)^2,
    c_n=sum_b w_b[n+min(b,n)],n+1<=c_n<=2n.

A finite raw second moment M2 gives uniform midpoint-energy majorant M2 and c_n<=n+sqrt(M2); its absence does not prove actual energy divergence.

For arbitrary deterministic STATE-INDEPENDENT arrays w_(n,b)>=0,sum_b w_(n,b)=1, define

    K_n=sum_b w_(n,b)K_(n,b),
    T_n(B)=sum_(b>B)w_(n,b),
    A_n=sum_b w_(n,b)min(b,n)^2<=n^2.

Then D_(K_n)(Z_n)<=A_n and the exact expected work satisfies c_n=n+sum_b w_(n,b)min(b,n)<=n+sqrt(A_n)<=2n.
The SAME weight-independent N_B gives gamma_n<=gamma_n^odd<=T_n(B) for all n>=N_B.
Consequently

    lim_(B->infinity) limsup_(n->infinity)T_n(B)=0

implies BOTH gaps tend to zero.
Finite limsup A_n suffices, including arrays with infinite raw second moment at some n.
Conversely an eventual positive odd-gap lower bound delta forces, for EVERY fixed B>=2, eventually T_n(B)>=delta and A_n->infinity, by the exact finite-n payment A_n>=(B+1)^2 T_n(B) when n>B.
An eventual ordinary-gap lower bound implies the same conclusion.
Escaping tails and diverging A_n are necessary, not sufficient, and A_n is a sufficient energy MAJORANT rather than an identity or necessary actual-energy cost.
The slowdown(1-1/c_n)I+K_n/c_n divides all energies and both gaps by the same c_n.
No uniform onset over growing B, efficient sampler, chronological equivalence, fixed-positive weak-defect exclusion, critical-mean classification, sharper non-tight actual-energy exclusion, state-dependent stationarity or unrestricted gap follows.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision complete-fixed-registration-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T18:55 |
| status | open |
| reason | Register the exact complete statement and original argument at their responsible C home after content/dependency judgment. Actual current whole checking and adopting review remain separate; original mathematical, source, native, contribution and historical review boundaries are retained without research resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Entire fixed-weight and arbitrary deterministic state-independent tight-array domains, full and odd gaps, positivity/nesting/full-refresh, every fixed-B onset, clipped versus raw energy, work clock and all positive weak-defect exclusions. |
| argument | [Entire complete argument](#argument) | Entire fixed-weight and arbitrary deterministic state-independent tight-array domains, full and odd gaps, positivity/nesting/full-refresh, every fixed-B onset, clipped versus raw energy, work clock and all positive weak-defect exclusions. |
| dependency | [Exact fixed input](Yin_C_G0170_v1.md#short-overlap-operator-and-energy) | Complete original per-b conditional projections, positivity, both midpoint representations, exact b^2 energy and resampled-coordinate work. |
| dependency | [Exact fixed input](Yin_C_G0540_v2.md#all-fixed-overlap-onset) | Actual distinct sign-paired persistent components with nonzero midpoint at EVERY fixed B after its actual finite onset. |
| dependency | [Exact fixed input](Yin_C_G0540_v2.md#isolated-component-energy-defect) | Complete original tail-fiber components with positive full masses and unique constant middle word; no uniform mass needed. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:07 |
| status | proved |
| reason | Under the current human maintenance authorization, adopt the exact complete current Statement and original complete Argument after the actually completed R743 constructor SELF whole inspection. Preserve all original authorship, source/native evidence, old R bindings and actual relationships, and open precision predecessors. No research or new producer is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Entire fixed-weight and arbitrary deterministic state-independent tight-array domains, full and odd gaps, positivity/nesting/full-refresh, every fixed-B onset, clipped versus raw energy, work clock and all positive weak-defect exclusions. |
| argument | [Entire complete argument](#argument) | Entire fixed-weight and arbitrary deterministic state-independent tight-array domains, full and odd gaps, positivity/nesting/full-refresh, every fixed-B onset, clipped versus raw energy, work clock and all positive weak-defect exclusions. |
| dependency | [Exact fixed input](Yin_C_G0170_v1.md#short-overlap-operator-and-energy) | Complete original per-b conditional projections, positivity, both midpoint representations, exact b^2 energy and resampled-coordinate work. |
| dependency | [Exact fixed input](Yin_C_G0540_v2.md#all-fixed-overlap-onset) | Actual distinct sign-paired persistent components with nonzero midpoint at EVERY fixed B after its actual finite onset. |
| dependency | [Exact fixed input](Yin_C_G0540_v2.md#isolated-component-energy-defect) | Complete original tail-fiber components with positive full masses and unique constant middle word; no uniform mass needed. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0743_v1.md#current-g425-complete-self-finding) | Entire exact current Statement and complete Argument with all listed actual inputs, full original-law probabilities, onsets, costs and limits; constructor SELF, not independent. |

## Complete original argument

<a id="argument"></a>

### Original account: Fixed and tight length-dependent overlap mixtures lose every uniform spectral gap

Date: 2026-10-18T17:48.
Human author Yin.
Root authors both the original fixed-weight proof and the length-dependent extension under the integrated G0001 authority.
This physical v2 retains the complete original L424v1 argument and the complete new extension, with v1/R436 preserved at their prior scope.
The first part treats fixed distributions, while PartII proves the tight length-dependent and clipped-majorant conclusions.
Angular_envelope_review performs meaning-preserving assembly and a separately recorded whole review without contributing a mathematical proof step.
No numerical graph, width scan, new input polynomial or external theorem is used.

<a id="overlap-mixture-reuse"></a>
## Actual question and reuse

The bounded G-line search inspected overlap mixtures, nested conditional projections, growing overlaps and all-interval kernels.
[C170](Yin_C_G0170_v1.md#statement) owns the actual short-overlap heat baths and the energy bound at each fixed b.
[L418](Yin_C_G0540_v2.md#all-fixed-overlap-onset) proves persistent isolated full-word components at EVERY fixed b, while explicitly leaving growing overlaps unclassified.
[C76](Yin_C_G0076_v1.md#statement) already uses nested conditional variance for another original-block comparison; the elementary conditional-expectation principle is reused rather than claimed new.
[C70](Yin_C_G0070_v1.md#statement) concerns returned-interval sign reflections and a specified uniform interval clock, not the complete endpoint-conditioned heat baths considered here.
Neither its invariant pairs nor its particular quadratic selection price is imported.
The new deduction treats arbitrary FIXED probability weights over all positive overlap lengths, using exact nesting on the original full-word space.

<a id="overlap-mixture-statement"></a>
## 1. Complete operator and conclusions

Keep the actual quartic P=t^4-t^3-t^2-t+1, its exterior root beta, neutral root zeta and original conditional returned-word law pi_(2n) from C170.
Let n>=5 and retain every word, all original digit weights and the complete return normalizer.
For1<=b<n put A_b={0,...,n-b-1}, C_b={n+b,...,2n-1}, and

    K_(n,b)=(E[ . | A_b digits]+E[ . | C_b digits])/2.

For b>=n define K_(n,b)=Pi_n, the projection onto constants, which is the same formula with both tails empty.
Let w_b>=0, sum_(b>=1)w_b=1 be fixed independently of n, and set

    K_n^w=sum_(b>=1) w_b K_(n,b),
    T_B=sum_(b>B)w_b,
    Z_n=-zeta^-n sum_(j<n)eta_j zeta^j,
    E_n^w(f)=<f,(I-K_n^w)f>_(pi_(2n)).                (1)

All sums are operator-norm convergent on a finite-dimensional probability space; the summands are positive self-adjoint contractions.
The full kernel is reversible, Markov and positive.
It commutes with the global word involution S eta=-eta, which preserves pi_(2n), and Z_n is odd.
Write gap_n and gap_n^odd for the least Dirichlet/variance quotient on nonzero centered real functions and nonzero real odd functions, respectively.
These spaces are nontrivial on the actual n>=5 supports.

The complete conclusions are

    E_n^w(Z_n)<=sum_(b>=1)w_b min(b,n)^2,             (2)
    lim_(n->infinity)gap_n=lim_(n->infinity)gap_n^odd=0. (3)

In particular a finite second moment M2=sum w_b b^2 gives a uniform actual complex midpoint-energy bound M2, but no fixed positive all-late spectral gap, even in the odd subspace.
For every fixed B>=2, a finite actual onset N_B exists such that

    n>=N_B => gap_n<=gap_n^odd<=T_B.                  (4)

No quantitative rate for N_B, or exchange with B depending on n, is asserted.
If the weights have finite support, both gaps are exactly zero at every sufficiently large n.
If they have unbounded support, then for EVERY n>=5

    0<T_(n-1)<=gap_n<=gap_n^odd,                      (5)

so each finite full-word chain is connected, while both gaps still tend to zero.
There is no contradiction between(3) and(5).

<a id="overlap-mixture-nesting"></a>
## 2. Exact nesting before any union or limit

Fix n and1<=b<=B<n.
The sigma fields generated by A_B and C_B are contained in those generated by A_b and C_b, respectively.
For nested finite sigma fields F subset G, conditional expectation and orthogonal decomposition give

    ||f-E[f|F]||_2^2
      =||f-E[f|G]||_2^2+||E[f|G]-E[f|F]||_2^2.

This proves, on the complete original law,

    E_(n,b)(f)<=E_(n,B)(f),
    ker(I-K_(n,B)) subset ker(I-K_(n,b)).             (6)

The kernel inclusion also follows because invariance under the average of two projections forces both nonnegative squared errors to vanish.
A function measurable with respect to the smaller tail is measurable with respect to the larger one.
Equivalently, every positive transition of either smaller resampling is also possible in the corresponding larger resampling, because all original word weights on the legal conditional fiber are strictly positive.
Thus the larger-b component partition is coarser, not finer.
These are finite-n statements; no identification of normalized carry vertices at different b is needed.

<a id="overlap-mixture-odd-obstruction"></a>
## 3. A genuinely odd low-energy test for every fixed cutoff

Fix B>=2.
L418 supplies an actual isolated union edge at overlap B with nonzero field midpoint Y and finite full-word appearance onset, together with its distinct sign-reversed edge.
The construction keeps the actual two real strips and original order, and its sole middle word is the all-negative or all-positive word of length2B.
All sufficiently large n have both edges with their COMPLETE original conditional word fibers.
Each is a full communicating component of K_(n,B), not merely one selected word or an unweighted edge.
The neutral embedding of nonzero Y is nonzero because it is a field embedding.
Consequently the sign-reversed component is distinct: the actual midpoint is constant on each of these fixed-endpoint, unique-middle-word components and changes sign.

Call the two components C_n^+ and C_n^-.
Their full original masses are equal and positive by S invariance.
Put

    f_n=1_(C_n^+)-1_(C_n^-),
    f_n composed with S=-f_n,
    E f_n=0,
    Var(f_n)=pi(C_n^+)+pi(C_n^-)>0.                  (7)

No uniform lower bound for this variance is asserted or needed for a Rayleigh quotient.
For b<=B, equation(6) gives E_(n,b)(f_n)=0.
For every b, positivity of K_(n,b) on centered functions gives

    0<=E_(n,b)(f_n)<=Var(f_n).

The full mixture therefore satisfies

    E_n^w(f_n)<=T_B Var(f_n).                        (8)

This is an ODD test on the complete original law, with no endpoint projection losing conditional fibers.
It proves(4), and T_B tending to zero proves both limits in(3) with the exact order: choose B first, then its actual finite onset, then all larger n.
For finite support choose B at least its maximum; then T_B=0 and the gaps vanish exactly after that onset.
No new witness family or sampled graph is needed beyond the accepted persistent components.

For unbounded support, the total weight assigned to b>=n is T_(n-1)>0 and every such operator is Pi_n.
Thus K_n^w=T_(n-1)Pi_n+(1-T_(n-1))Q_n for a positive Markov contraction Q_n, unless the first coefficient is1, in which case the conclusion is immediate.
On centered functions Pi_n=0, proving the lower bound(5).
Every transition from any word to any other legal word also has at least T_(n-1) times that word's positive pi mass.
This proves actual full-word irreducibility at each finite n, without making its minorization uniform.

<a id="overlap-mixture-energy-clock"></a>
## 4. Complete midpoint and work costs

For b<n, C170 supplies E_(n,b)(Z_n)<=b^2 with its actual complex norm and both conditional means.
For b>=n the full refresh has energy E abs(Z_n)^2, which is at most n^2 because abs(Z_n)<=n pointwise and E Z_n=0.
Linearity and bounded finite-n energies prove(2), including arbitrary weights without a second moment.
A finite M2 is a sufficient condition for this uniform majorant; its infinitude is not claimed to prove actual energy divergence.

The expected number of coordinates resampled by one mixture update is

    c_n=sum_(b>=1)w_b [n+min(b,n)],
    n+1<=c_n<=2n,
    c_n<=n+sqrt(M2) if M2<infinity.                 (9)

The last bound is Cauchy--Schwarz against the probability weights.
The declared one-coordinate expected-work clock is

    K_n^(w,cost)=(1-1/c_n)I+K_n^w/c_n.              (10)

It divides both full/odd gaps and every Dirichlet energy by c_n.
The energy-to-gap ratio is unchanged; no efficient-sampling or chronological-walk equivalence is claimed.
The noninteger expected cost is a valid slowdown factor at least1, not a rounded unpriced update count.

<a id="overlap-mixture-scope"></a>
## 5. Consequence and what is still possible

A fixed finite or countable mixture cannot restore a uniform ordinary or odd Poincare gap, even when its midpoint energy remains uniformly bounded.
For unbounded support it gives an actual example where every finite chain is connected and its optimal finite-component defect is zero, but the required zero-defect Poincare constants are not uniform in n.
This is the exact distinction needed before using finite component classification as an all-late inequality.

The test(7) may have extremely small total mass, and its oscillation is2.
A fixed positive oscillation defect can pay that test without a uniform gap.
Thus(3) does NOT refute a weak Poincare estimate with fixed defect below1/4, the proposed sign-odd fixed-defect variant, a uniformly positive self-sign component subset, or the original critical-mean conclusion.
No full component-defect lower bound near1/4 follows from a zero global or odd gap.
The fixed-weight conclusion of Sections1--5 does not by itself classify n-dependent schedules.
PartII below covers arbitrary state-independent length-dependent weights under asymptotic tightness, and proves the necessary escaping-tail and diverging-majorant costs for an eventual positive gap.
Non-tight schedules and sharper actual-energy estimates remain outside that exclusion; no uniform B-onset is assumed.
The original unrestricted Mahler and attainment objective remains unresolved.

<a id="overlap-mixture-inputs"></a>
## Actual inputs and author check

| Input | Exact role |
| --- | --- |
| [C170 original operator](Yin_C_G0170_v1.md#statement), [R803](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Complete actual full-word law, positivity, conditional projections, midpoint energy and original work divisor. Root contributed to C170; the independent accepted finding is reused at its exact scope. |
| [L418 all fixed overlaps](Yin_C_G0540_v2.md#all-fixed-overlap-onset), [R427](../audits/reviews/Yin_R_G0427_v1.md#isolated-mass-whole-independent-finding) | Actual persistent isolated components, nonzero midpoint, complete fibers and finite onset for each fixed B. Root reviewed L418 but did not author its construction. |
| [L418 internal word law](Yin_C_G0540_v2.md#isolated-component-energy-defect) | Entire conditional components, not selected words; no new total-mass or inside-component bound is inferred. |
| [C76 nested comparison](Yin_C_G0076_v1.md#statement) | Established elementary conditional-variance principle in a different original-block setting; the precise present nesting is proved directly. |
| [C70 reflected intervals](Yin_C_G0070_v1.md#statement) | Distinct operator and clock comparison only, not a premise about complete heat baths. |
| [L410 fixed defect](Yin_C_G0514_v2.md#bulk-component-defect) | Ordinary finite-component and uniform weak-inequality boundary only; no claim that its original-law sufficient condition is contradicted. |

Both new proof development and the original fixed-weight argument belong to root; the v2 assembly supplies no mathematical repair or new inference.

<a id="tight-overlap-extension"></a>
## PartII. Tight length-dependent schedules

The numbered equations in this part run separately from(1) to(6), under the original-law conventions of PartI.

<a id="tight-overlap-question"></a>
## Exact scope and prior result

[L424v1](../ledger/Yin_L_G0424_v1.md#overlap-mixture-odd-obstruction), through [whole R436](../audits/reviews/Yin_R_G0436_v1.md#overlap-mixture-whole-independent-finding), already constructs for every fixed integer B>=2 and every n beyond an actual finite onset N_B a centered ODD full-word function f_(n,B) with positive variance, zero K_(n,b) energy for every b<=B and at most its variance for every b>B.
That test depends only on the original operator and B,n, not on any mixture weights.
Its complete original mass can be arbitrarily small; no uniform mass bound is imported.
The prior statement treats fixed weights and explicitly leaves length-dependent schedules outside its scope.
The extension below uses that already proved test at its exact quantifiers.

<a id="tight-overlap-statement"></a>
## Length-dependent operator and exact conclusion

For every n>=5 let w_(n,b)>=0, sum_(b>=1)w_(n,b)=1.
Keep exactly L424's original complete quartic law and K_(n,b), including the full refresh Pi_n for b>=n, and define

    K_n=sum_(b>=1)w_(n,b) K_(n,b),
    T_n(B)=sum_(b>B)w_(n,b),
    A_n=sum_(b>=1)w_(n,b) min(b,n)^2.                 (1)

Let gamma_n and gamma_n^odd be the ordinary and odd spectral gaps in the ORIGINAL mixture-update clock.
Each finite-n operator is a positive reversible Markov contraction commuting with full word negation.
The same actual midpoint Z_n obeys

    E_n(Z_n)<=A_n<=n^2,
    c_n=n+sum_b w_(n,b)min(b,n)<=n+sqrt(A_n)<=2n.      (2)

The first quantity is the accepted sufficient energy MAJORANT, not an identity or a proved necessary energy cost.
The coordinate-work slowdown by c_n divides every energy and gap together.

For every fixed B>=2, the same N_B from L424, independent of the chosen weight array, gives

    n>=N_B => 0<=gamma_n<=gamma_n^odd<=T_n(B).         (3)

In particular the asymptotic tightness condition

    lim_(B->infinity) limsup_(n->infinity) T_n(B)=0    (4)

implies BOTH gamma_n->0 and gamma_n^odd->0.
This permits arbitrary length-dependent schedules within the stated condition; it is not restricted to a fixed or convergent distribution.
If limsup_n A_n<infinity, condition(4) holds and the same conclusion follows.

Conversely, if gamma_n^odd>=delta>0 for every sufficiently large n, then

    for every fixed B>=2, eventually T_n(B)>=delta,
    A_n -> infinity.                                (5)

An eventual lower bound for the ordinary gap implies the same statement.
These are necessary escaping-tail and diverging-MAJORANT conditions, not sufficient conditions for a gap and not actual midpoint-energy divergence.

<a id="tight-overlap-proof"></a>
## Complete proof and all limit orders

Norm convergence and the operator properties are pointwise finite-n consequences of nonnegative probability weights and the original positive contractions, exactly as in L424.
The energy majorant and c_n formula likewise follow separately for each n from C170's b^2 bound for b<n and the full-refresh n^2 bound for b>=n.
Cauchy--Schwarz against w_(n,.) proves the middle work inequality in(2).
No uniform raw moment sum w_(n,b)b^2 is needed to define these truncated quantities.

Fix B first and use the ACTUAL f_(n,B) from L424 for all n>=N_B, increasing that onset beyond B if needed.
It has zero energy for b<=B and energy at most its variance for the other original positive contractions.
Multiplying by w_(n,b), summing and dividing by its strictly positive complete original variance proves(3).
The test is chosen before and independently of the weights; no single coordinate or endpoint surrogate replaces it.
Taking limsup in n for fixed B, and only then sending B to infinity, proves the consequence of(4).
It neither assumes nor supplies a uniform bound on N_B as B grows.

For n>B, every b>B has min(b,n)>=B+1.
Thus the exact finite-n tail payment is

    A_n>=(B+1)^2 T_n(B).                             (6)

If limsup_n A_n=M<infinity, (6) gives limsup_n T_n(B)<=M/(B+1)^2 for every fixed B, proving(4).
An eventual finite bound can equally be used; finitely many early lengths are irrelevant.
The statement uses the TRUNCATED majorant A_n, so it also covers arrays having infinite untruncated b-second moment at some n.

If the odd gap is eventually at least delta, (3) implies T_n(B)>=delta for all n beyond the larger of its own onset and N_B.
For any requested finite R choose a FIXED B large enough that delta(B+1)^2>R, and then take n beyond those onsets and B.
Equation(6) gives A_n>R for every such n, proving A_n tends to infinity, rather than merely being unbounded along a subsequence.
The ordinary gap is no greater than the odd gap, so its eventual positive lower bound implies the same obstruction.
No inference is reversed: a large tail or diverging majorant does not prove a gap or actual energy growth.

<a id="tight-overlap-boundary"></a>
## Consequence for the selected mechanism

Choosing different probability weights at different lengths cannot repair a uniform ordinary or odd gap while keeping the existing overlap-squared energy majorant uniformly bounded.
The earlier fixed-mixture theorem is the special case in which T_n(B) is independent of n and its tail tends to zero.
The new argument also covers every asymptotically tight schedule, whether or not its second moment is uniformly bounded.
The operator still acts on the same full original word law and the same midpoint, with every complete component mass retained.

This does not rule out an actual energy estimate sharper than A_n for a non-tight schedule, a fixed positive weak defect, a weighted odd inequality on a selected positive-mass family, or state-dependent updates with separately proved stationarity and costs.
The actual mean and unrestricted Task remain unresolved.
This extension enlarges the fixed v1 quantifier scope; that original physical version and R436 remain preserved.
The complete fixed-weight proof above and the present extension together form the current mathematical scope.

<a id="tight-overlap-inputs"></a>
## Inputs and author check

| Input | Actual role |
| --- | --- |
| [L424 original test](../ledger/Yin_L_G0424_v1.md#overlap-mixture-odd-obstruction), [R436](../audits/reviews/Yin_R_G0436_v1.md#overlap-mixture-whole-independent-finding) | Complete fixed-B tests, all-late onset independent of weights, exact odd and positive-energy bounds; accepted original proof and whole review. |
| [L424 energy and clock](../ledger/Yin_L_G0424_v1.md#overlap-mixture-energy-clock) | Exact per-b complex energy, full refresh, complete work cost and sufficient-majorant boundary. |
| [C170 original law](Yin_C_G0170_v1.md#statement), [R803](../audits/reviews/Yin_R_G0803_v1.md#short-overlap-whole-independent-finding) | Unchanged original quartic, two full-word conditional heat baths and accepted upstream review. Root contributed to C170. |
| [L418 persistent components](Yin_C_G0540_v2.md#all-fixed-overlap-onset), [R427](../audits/reviews/Yin_R_G0427_v1.md#isolated-mass-whole-independent-finding) | Exact original construction already paid by L424; not a new union graph or an assumed uniform B-onset. |

The complete extension retains its author proof and all stated open boundaries; review and adoption are recorded separately.
