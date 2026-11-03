---
author: Yin
---

# Complete actual-height modulus and growing residue-degree mass escape

The complete necessary original D76 proof is retained from [L209](../ledger/Yin_L_G0209_v1.md#complete-retained-proof-and-review).
The resultant_research author supplied the quantitative modulus, degree-adapted exponents, uniform mass escape, factor-complexity and multi-prime arguments; the coordinator supplied the broad exploration question only.
The [complete original R727 whole and source account](../audits/reviews/Yin_R_G0727_v1.md#original-growing-residue-review-account) keeps its 2026-10-09T20:32 completion and every actual mathematical/source/input/nonexecution fact.
Actual prior additional shared-context/progress mathematical contents and initial order are not established, so its justified original whole relationship is UNKNOWN rather than inferred from its independent label.
The [complete original author-check/contribution account](../audits/reviews/Yin_R_G0727_v1.md#growing-residue-original-author-check-finding) remains separately SELF at its original 2026-10-10 day precision.
The sufficient Pri11 and retained Dim19 v1 source units are reused directly, with distinct original R108 reading facts retained and no new source unit, PDF inspection or external proof audit.
No native program, producer, research Task/E or new mathematical exploration occurs.

The currently selected [whole independent finding R727](../audits/reviews/Yin_R_G0727_v1.md#current-growing-residue-whole-independent-finding) records the independent mathematical initial finding at 12:20, completion of the whole and original-account/source comparison at 12:28, publication at 12:47 and actual adoption at 2026-10-22T04:51.
The earlier R713 whole SELF at 10:07 and C504's adoption at 10:08 retain their actual scope and chronology.

## Statement

Let alpha be any nontorsion algebraic unit, P its monic irreducible integer minimal polynomial of actual degree d>=2, m=log M(P)>0 and C_n=|Norm_(Q(alpha)/Q)(alpha^n-1)| for every integer n>=1.
No reciprocity, squarefree reduction, small coefficient height, minimal-Frobenius valuation or local-maximal-order assumption is made.
For beta=alpha^n of actual degree N, retain the exact absolute powered height and field-norm multiplicity:

    h=h_abs(beta)=n m/d,
    log C_n/d=(1/N)sum_(i=1)^N log|1-beta_i|.

The sum uses the distinct powered conjugates and repeats their field norm d/N times in C_n; degree preservation is not assumed.
Use natural logarithms and the already accepted Dim19 v1 and Pri11 statement/application interfaces at their original inspection depths.
Put

    c=log2/4,h_0=c exp(-20),
    b(h)=max{h,sqrt(h/c)log sqrt(c/h)}, 0<h<=h_0,
    Omega(h)=19 b(h)^(1/6).

Then b and Omega are increasing on this interval, b(h)<=exp(-6), and for every n with h<=h_0,

    0<=log C_n/d<=Omega(h).

The full proof keeps the actual N>=sqrt(c/h)>=exp(10)>55, the compact support radius 2R, Lipschitz constant 3exp(T)+T/R and complete inequality

    log C_n/d<=h+exp(-T)/2+1/R
               +(3exp(T)+T/R)(4R+1)sqrt(max(log N/N,h)),

with T=(1/6)log(1/b),R=b^(-1/6).
No finite polynomial enumeration or new external proof is hidden in the explicit bound.
In particular Omega(h)=O(h^(1/12)(1+log(1/h))^(1/6)) as h tends to zero; the explicit function, threshold and accepted-source boundaries remain controlling.

For each rational prime p factor the COMPLETE reduction

    Pbar=product_phi phi^e_phi,
    w_(p,f)=sum_(deg phi=f)e_phi f,
    W_(p,F)=sum_(1<=f<=F)w_(p,f).

All reduction multiplicities remain, including discriminant and order-index primes.
They are not identified with local ramification indices.
For every integer 1<=f<=d put

    k_f=min{k>=0:p^k>=d/f},n_f=(p^f-1)p^k_f.

Then, at this one exponent for this degree class,

    v_p C_(n_f)>=w_(p,f),
    n_f/d<=p(p^f-1)/f.

Each selected original root has an individual local field of degree at most d and residue degree at least f, hence ramification index at most d/f and initial valuation at least f/d.
This bound is not assigned to the common splitting field.
The complete capped binomial lift, original root count and nonzero original degree-d norm prove the income with no omitted or extra multiplicity.

For every integer F>=1 and prime p with H=m p^(F+1)<=h_0,

    W_(p,F)/d<=min{1,F Omega(m p^(F+1))/log p}.

Each degree class first receives its own fully charged exponent and norm bound; only the resulting upper bounds on disjoint DEGREE MASSES are summed.
This is not an arithmetic income bound at one common exponent.
Absent degrees or F>d contribute no missing terms.

Fix any real epsilon in(0,1).
On a hypothetical sequence of actual nontorsion units with total m tending to zero, uniformly over all primes p and integers F>=1 satisfying

    p^(F+1)<=m^(-1+epsilon),

one has W_(p,F)/d tending to zero.
For sufficiently small m an explicit bound is

    sup W_(p,F)/d
       <=min{1,[log(1/m)/(log2)^2]Omega(m^epsilon)}
       =O_epsilon(m^(epsilon/12)(1+log(1/m))^(7/6)).

An empty admissible range is vacuous.
This includes linear factors at all p<=m^(-(1-epsilon)/2) and the fixed-prime cutoffs F<=(1-epsilon)log_p(1/m)-1, without an existence claim for a near-one sequence.

For each fixed p let L=log_p(1/m) and

    B_p(P)=sum_phi e_phi,
    bar_f_p(P)=(1/d)sum_phi e_phi(deg phi)^2.

Then the precise necessary factor-complexity bounds are

    liminf_(m->0)bar_f_p(P)/L>=1,
    limsup_(m->0)L B_p(P)/d<=1.

The proof keeps F=floor((1-epsilon)L-1), the explicit rate L W_(p,F)/d->0, and takes m to zero before epsilon decreases to zero.
It supplies no factorization algorithm or assertion of irreducible reduction.

For every fixed integer F>=1 and real 0<kappa<1/(F+13),

    (1/d)sum_(p<=m^(-kappa))(log p)W_(p,F)->0,

with the full explicit bound

    (1/d)sum_(p<=m^(-kappa))(log p)W_(p,F)
       <=F m^(-kappa)Omega(m^(1-kappa(F+1)))
       =O_(F,kappa)(m^((1-kappa(F+13))/12)
                                    (1+log(1/m))^(1/6)).

The count uses only the elementary upper bound on the number of primes, with no prime-number theorem or independence of reductions.
It remains a sum of separate modular masses, not total valuation at arbitrary times or a common-exponent lower income.
The sufficient exponent 13 belongs to this explicit expense modulus and is not claimed optimal.

For squarefree Pbar the older distinct-root capacity separately gives W_(p,F)<=F p^F and W_(p,F)/d<=F m p^F/c.
It does not extend to repeated reduction by deleting e_phi; the full theorem above retains every multiplicity and actual local ramification cost.
Growing residue orders beyond the charged height range, unusually deep valuation on small mass, same-exponent coverage and inverse/full-cofactor costs remain unresolved.
The theorem establishes neither an actual near-one family nor positive-linear income coverage at n<=Cd nor an unrestricted Mahler gap.
The recognized discrepancy and house theorems remain accepted statement/applicability inputs, without a new source proof, version substitution, PDF reading, native computation or research Task/E.

## Current assessment
[Selected decision](#decision-complete-current-independent-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:05 |
| status | open |
| reason | Register the complete actual-powered-height expense, fully charged original-root local exponents and all-multiplicity growing mass/factor-complexity/multi-prime theorem, preserving every source, limit-order and noncoverage boundary. Actual current whole SELF and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire exact statement](#statement) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. |
| argument | [Entire complete retained argument](#argument) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. |
| dependency | [Complete actual-powered-degree norm expense](Yin_C_G0391_v1.md#general-unit-actual-product-cost) | Full norm tower, actual height, compact globally Lipschitz truncation, radius2R/factor4R+1 and all costs in original equation4; N is the actual powered degree, no degree preservation. |
| dependency | [Exact accepted Pri11 statement](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Only retained arXiv1307.5734v1 Theorem3.1/(3.2), normalized circle probability, integral simple-root polynomial, global Lipschitz support factor and N>=55, at checked statement/applicability depth. No potential-theory proof reaudit. |
| dependency | [Exact retained Dim19v1 house interface](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only retained 2019v1 Theorem1 house>=2^(1/(4N)) for noncyclotomic monic irreducible N>1, hence logM>=c/N. No later accepted text, publication-version comparison or external proof audit. |
| dependency | [Complete original house-to-Mahler consequence](Yin_C_G0267_v1.md#degree-only-primitive-escape) | Only m>=c/d and its exact actual-degree use, not the separate primitive-certificate algorithm or a uniform Mahler gap. |
| dependency | [Complete original-root capped ramified lift](Yin_C_G0254_v1.md#ramified-valuation-capture) | Full capped p-power binomial inequality at real initial f/d and all original root indices, without equality of polynomial multiplicity and local ramification. |
| dependency | [Complete individual-root-field guard](Yin_C_G0256_v1.md#finite-exact-local-cyclic-table) | Each individual root local field has degree<=d, residue degree at least f and ramification at most d/f; no such bound on the common splitting field or an unramified/index-good assumption. |
| support | [Complete earlier all-input bounded-residue result](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape) | Only prior fixed p,F mass comparison with all multiplicities and full same-exponent cost; no minimal-Frobenius premise is imported into the new theorem. |
| support | [Complete squarefree capacity comparison](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Only distinct reduced-root cardinality at good primes in Section5; repeated e_phi are not removed in the main theorem. |
| support | [Complete separate-time normalization boundary](Yin_C_G0450_v1.md#cyclic-layer-spreading-fixed-scope) | Only the actual distinction between complete layer/mass sums and fully charged same-exponent norm income; the new sum controls degree masses and claims no common-exponent coverage. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T02:08 |
| status | proved |
| reason | Adopt after actual full current whole SELF of the complete actual-powered-degree norm/height modulus with all Pri11 truncation constants, individual-root ramified exponents and all polynomial multiplicities, growing-prime/residue mass estimates, fixed-prime complexity limits in their exact order, weighted multi-prime range and every original comparison/source/noncoverage boundary. No substantive mathematical defect or missing hypothesis was found. The old whole UNKNOWN and complete original author SELF keep their actual scopes. No external proof, source/PDF reading, native program or research Task/E was executed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. |
| argument | [Exact retained argument](#argument) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#general-unit-actual-product-cost) | Full norm tower, actual height, compact globally Lipschitz truncation, radius2R/factor4R+1 and all costs in original equation4; N is the actual powered degree, no degree preservation. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Only retained arXiv1307.5734v1 Theorem3.1/(3.2), normalized circle probability, integral simple-root polynomial, global Lipschitz support factor and N>=55, at checked statement/applicability depth. No potential-theory proof reaudit. |
| dependency | [Exact retained dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only retained 2019v1 Theorem1 house>=2^(1/(4N)) for noncyclotomic monic irreducible N>1, hence logM>=c/N. No later accepted text, publication-version comparison or external proof audit. |
| dependency | [Exact retained dependency](Yin_C_G0267_v1.md#degree-only-primitive-escape) | Only m>=c/d and its exact actual-degree use, not the separate primitive-certificate algorithm or a uniform Mahler gap. |
| dependency | [Exact retained dependency](Yin_C_G0254_v1.md#ramified-valuation-capture) | Full capped p-power binomial inequality at real initial f/d and all original root indices, without equality of polynomial multiplicity and local ramification. |
| dependency | [Exact retained dependency](Yin_C_G0256_v1.md#finite-exact-local-cyclic-table) | Each individual root local field has degree<=d, residue degree at least f and ramification at most d/f; no such bound on the common splitting field or an unramified/index-good assumption. |
| support | [Exact retained support](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape) | Only prior fixed p,F mass comparison with all multiplicities and full same-exponent cost; no minimal-Frobenius premise is imported into the new theorem. |
| support | [Exact retained support](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Only distinct reduced-root cardinality at good primes in Section5; repeated e_phi are not removed in the main theorem. |
| support | [Exact retained support](Yin_C_G0450_v1.md#cyclic-layer-spreading-fixed-scope) | Only the actual distinction between complete layer/mass sums and fully charged same-exponent norm income; the new sum controls degree masses and claims no common-exponent coverage. |
| review | [Actual complete current whole SELF](../audits/reviews/Yin_R_G0713_v1.md#current-growing-residue-complete-whole-self-finding) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. Actual current relationship is self-reviewed; original whole UNKNOWN and complete original author SELF remain separate. |


### Decision complete-current-independent-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:51 |
| status | proved |
| reason | Adopt the complete unchanged C504 Statement and Argument through R727 after its actual fresh-context initial finding at12:20, whole historical/source comparison completed12:28 and publication12:47. The actual-degree modulus, every individual-root/repeated-factor income and separate charged mass estimate, all growing ranges and both complexity limit orders were wholly inspected. Original source statement/application depths, original author SELF and UNKNOWN old arrangement remain exact; no source proof, native program or new mathematical research was run. Existing mathematics, other selected inputs and every earlier decision remain unchanged; the old10:07/10:08 SELF events are not rewritten. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. |
| argument | [Exact argument](#argument) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. |
| dependency | [Exact dependency](Yin_C_G0391_v1.md#general-unit-actual-product-cost) | Full norm tower, actual height, compact globally Lipschitz truncation, radius2R/factor4R+1 and all costs in original equation4; N is the actual powered degree, no degree preservation. |
| dependency | [Exact dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Only retained arXiv1307.5734v1 Theorem3.1/(3.2), normalized circle probability, integral simple-root polynomial, global Lipschitz support factor and N>=55, at checked statement/applicability depth. No potential-theory proof reaudit. |
| dependency | [Exact dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only retained 2019v1 Theorem1 house>=2^(1/(4N)) for noncyclotomic monic irreducible N>1, hence logM>=c/N. No later accepted text, publication-version comparison or external proof audit. |
| dependency | [Exact dependency](Yin_C_G0267_v1.md#degree-only-primitive-escape) | Only m>=c/d and its exact actual-degree use, not the separate primitive-certificate algorithm or a uniform Mahler gap. |
| dependency | [Exact dependency](Yin_C_G0254_v1.md#ramified-valuation-capture) | Full capped p-power binomial inequality at real initial f/d and all original root indices, without equality of polynomial multiplicity and local ramification. |
| dependency | [Exact dependency](Yin_C_G0256_v1.md#finite-exact-local-cyclic-table) | Each individual root local field has degree<=d, residue degree at least f and ramification at most d/f; no such bound on the common splitting field or an unramified/index-good assumption. |
| support | [Exact support](Yin_C_G0491_v1.md#bounded-residue-mass-near-one-escape) | Only prior fixed p,F mass comparison with all multiplicities and full same-exponent cost; no minimal-Frobenius premise is imported into the new theorem. |
| support | [Exact support](Yin_C_G0376_v2.md#good-prime-short-order-capacity) | Only distinct reduced-root cardinality at good primes in Section5; repeated e_phi are not removed in the main theorem. |
| support | [Exact support](Yin_C_G0450_v1.md#cyclic-layer-spreading-fixed-scope) | Only the actual distinction between complete layer/mass sums and fully charged same-exponent norm income; the new sum controls degree masses and claims no common-exponent coverage. |
| review | [Exact review](../audits/reviews/Yin_R_G0727_v1.md#current-growing-residue-whole-independent-finding) | Entire original D76 reuse/Sections1--5/equations1--18 plus full contribution/source limits: every nontorsion unit/actual d/m/n/degree-dropping beta/field-norm tower, accepted Pri11 simple-root/integral/globalLipschitz/support/N55 and Dim19v1 house scopes, exact c/h0/b/Omega/monotonicity/X threshold/truncation T,R/all constants and asymptotic; every prime/original root/repeated polynomial factor/index prime, individual local residue degree>=f/ramification<=d/f rather than common splitting field, capped binomial k_f/n_f income and complete exponent cost, separate degree-mass upper bounds not merged income, all F including absent or F>d; uniform growing p,F range and explicit epsilon-rate/empty range/hypothetical input quantifiers, fixed-p factor count and root-index weighted average with precise floor and m-before-epsilon limit order, fixedF/kappa<1/(F+13) full prime-mass bound/rate/elementary prime count, squarefree-only capacity comparison and all retained multiplicity/depth/same-time/inverse/cofactor/near-one/gap/source-proof/nonexecution limits. Actual current relationship is independently reviewed after fresh direct whole-proof inspection and subsequent complete historical/source comparison; original whole UNKNOWN and complete original author SELF retain their actual scopes. |

## Complete retained argument

<a id="argument"></a>
<a id="complete-retained-proof-and-review"></a>
<a id="growing-residue-fixed-scope"></a>

### Reuse and the changed discriminator

Read [complete C491](Yin_C_G0491_v1.md#local-rigidity-near-one-mass-fixed-scope) and S8's current all-input mass question, then [C254's complete ramified lift](Yin_C_G0254_v1.md#ramified-valuation-capture), [C256's complete actual-root field guard](Yin_C_G0256_v1.md#finite-exact-local-cyclic-table), [C376v2's complete good-prime capacity](Yin_C_G0376_v2.md#good-prime-short-order-capacity), [C391's complete cyclic-product expense](Yin_C_G0391_v1.md#general-unit-actual-product-cost), and [C450's complete normalization obstruction](Yin_C_G0450_v1.md#cyclic-layer-spreading-fixed-scope).
A bounded G-ledger screen found no existing form of the growing-prime/growing-degree conclusion below.
This is a local reuse observation, not a historical novelty claim.

The new deduction keeps separate exponents for separate factor degrees, applies an actual norm upper bound to each, and only then sums upper bounds on their degree mass.
It never adds different-time arithmetic incomes and calls their sum income at one time.
Quantifying the height-to-powered-degree step in L168 allows the residue cutoff and the prime range to grow with the input.
This is an all-input near-one necessary condition; it does not assume minimal Frobenius valuation or reciprocal/small-height coefficients.

The only external statement inputs are already accepted: Pri11 Theorem3.1 through [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001), and the retained Dim19 v1 house bound through [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-house) and its explicit [complete C267 consequence](Yin_C_G0267_v1.md#degree-only-primitive-escape).
Their exact statement/applicability records were read.
No newer edition, external proof re-audit, fresh source acquisition or stronger Mahler theorem is being used.
The new mathematics is the quantitative actual-height modulus and its degree-adapted local application, not the accepted discrepancy or house theorem.

<a id="height-uniform-cyclic-cost-modulus"></a>
### 1. A cyclic-norm expense depending only on the actual powered height

Let alpha be a nontorsion algebraic unit with actual degree d, m=log M(P)>0, and C_n=|Norm_(Q(alpha)/Q)(alpha^n-1)|.
For n>=1, let beta=alpha^n, N=deg beta and

    h=h_abs(beta)=n m/d,
    c=log2/4,
    h_0=c exp(-20),
    b(h)=max(h,sqrt(h/c) log sqrt(c/h)),       0<h<=h_0,
    Omega(h)=19 b(h)^(1/6).                                 (1)

Then

    0<=log C_n/d <= Omega(h)             if h<=h_0.          (2)

Every degree drop in beta is retained.
Indeed the field-norm tower gives log C_n/d=(1/N)sum_beta_i log|1-beta_i|, using the N distinct conjugates, and absolute height is exactly h.
The accepted house bound implies log M(P_beta)>=c/N, so

    h>=c/N^2,       N>=sqrt(c/h)=:X.                        (3)

The noncyclotomic unit beta has N>=2; degree-one units would be roots of unity.
At h<=h_0, X>=exp(10)>55.
The function log x/x is decreasing for x>exp(1), hence

    max(log N/N,h)<=b(h).

Here b is increasing on(0,h_0]: log X/X increases as h increases because X>exp(1), and h itself increases.
Also b(h)<=exp(-6), since log X/X<=10 exp(-10)<exp(-6) and h<=c exp(-20)<exp(-6).

Use the already proved L168 expense with its actual support and Lipschitz constants:

    log C_n/d <= h+exp(-T)/2+1/R
           +(3exp(T)+T/R)(4R+1)sqrt(max(log N/N,h)),          (4)

valid for N>=55, T>=1 and R>=2.
Set T=(1/6)log(1/b), R=b^(-1/6)=exp(T).
The preceding bound on b makes these parameters legitimate.
Since4R+1<=5R, the last term in(4) is at most

    15 b^(1/6)+5T sqrt(b).

The elementary maximum of x exp(-x/3)/6 for x>=0 is1/(2exp(1)); equivalently T b^(1/3)<=1/(2exp(1)).
Moreover h<=b<=b^(1/6).
Substitution gives

    log C_n/d
       <=[1+1/2+1+15+5/(2exp(1))] b^(1/6)
       <19 b^(1/6),                                       (5)

which proves(2).
No compactness-only degree escape or unperformed finite polynomial enumeration is needed for this quantitative version.
It retains the accepted source threshold and the cutoff costs; no optimality of the exponent1/6 or constant19 is claimed.

In particular

    Omega(h)=O(h^(1/12)(1+log(1/h))^(1/6)) as h->0.         (6)

The constant is absolute because c is fixed.
This asymptotic is only shorthand for the explicit function(1), which will control every varying parameter below.

<a id="factor-degree-adapted-single-exponent"></a>
### 2. A separate affordable exponent for each actual factor degree

Fix a prime p and factor the complete reduction as

    Pbar=product_phi phi^(e_phi),
    w_(p,f)=sum_(deg phi=f) e_phi f,
    W_(p,F)=sum_(1<=f<=F) w_(p,f).                           (7)

All multiplicities are included.
A bad discriminant or power-basis index prime is allowed; e_phi is a polynomial multiplicity and is not called a local ramification index here.

For an integer1<=f<=d set

    k_f=min{k>=0:p^k>=d/f},
    n_f=(p^f-1)p^k_f.                                      (8)

Then the actual local income at this one exponent satisfies

    v_p C_(n_f)>=w_(p,f),
    n_f/d <= p(p^f-1)/f.                                  (9)

To check the full ramification cost, label all original d roots in a p-adic splitting field.
The multiset of their reductions is precisely the root multiset of Pbar.
Each root in a factor of degree f has residue generating F_(p^f).
Its own local field Q_p(alpha_i) therefore has residue degree at least f, so its ramification index is at most d/f.
This does not give that bound to the common splitting field and does not assume the actual local field is unramified or generated by the residue alone.
The root's residue order divides p^f-1, whence

    v(alpha_i^(p^f-1)-1)>=f/d,

for v(p)=1.
L72's capped binomial inequality raises this positive valuation to at least one after k_f p-powerings.
Thus each of the w_(p,f) selected original root indices contributes at least one to v_p C_(n_f); the other roots contribute nonnegatively.
This proves the first part of(9).
Minimality of k_f gives p^k_f<=p d/f, including k_f=0, proving the cost.
No power-degree preservation, saturation hypothesis or change of integer order is used.

Suppose an integer F>=1 and p satisfy

    H=m p^(F+1)<=h_0.                                      (10)

For f<=min(F,d), the actual height at exponent n_f is at most H by(9).
Monotonicity of Omega and(2) therefore give, separately for each f,

    (w_(p,f)/d)log p <=log C_(n_f)/d<=Omega(H).

Now sum these upper bounds on disjoint degree masses.
The result is

    W_(p,F)/d <= min(1, F Omega(m p^(F+1))/log p).           (11)

An absent degree contributes zero.
Formula(11) is a distribution restriction derived from different actual norms, each with its own fully charged exponent.
It is not a lower bound on C_n for any common n, and no conclusion adds those different-time incomes without expense.
Compared with L205's least common multiple over all f<=F, the new conclusion avoids requiring one exponent to contain every residue degree's period.
It does so by proving separate upper bounds on mass, not by producing cheaper common-exponent income.

<a id="uniform-growing-prime-residue-escape"></a>
### 3. Uniform escape across a growing prime-and-degree range

Fix0<epsilon<1.
As total m tends to zero among nontorsion algebraic units, one has uniformly over every rational prime p and integer F>=1 with

    p^(F+1)<=m^(-1+epsilon),                               (12)

that

    W_(p,F)/d ->0.                                         (13)

For small enough m, H in(10) is at most m^epsilon<=h_0.
Also(12) gives F<=log(1/m)/log2 and log p>=log2.
Thus the explicit uniform bound is

    sup_((p,F) satisfying(12)) W_(p,F)/d
       <= [log(1/m)/(log2)^2] Omega(m^epsilon) ->0.          (14)

An empty set of pairs imposes no condition.
The last limit follows directly from(6): its right side is O_epsilon(m^(epsilon/12)(1+log(1/m))^(7/6)).
The displayed bound can be replaced by its minimum with one.
This is stronger than keeping both p and F fixed.
For example the entire growing range of linear factors at primes p<=m^(-(1-epsilon)/2) is covered at once, and for fixed p the cutoff can be any F<= (1-epsilon)log_p(1/m)-1.

No existence of a sequence with total m tending to zero is asserted.
The conclusion is an input-uniform necessary condition on any such hypothetical sequence, applies to nonreciprocal and reciprocal units alike, and allows all bad reductions.
It says nothing when the actual local exponent cost makes m p^(F+1) large.

For each fixed p there are also concise factor-complexity consequences.
Put L=log_p(1/m) and

    B_p(P)=sum_phi e_phi,
    bar_f_p(P)=(1/d)sum_phi e_phi (deg phi)^2.              (15)

Here B_p counts the mod-p irreducible factors with polynomial multiplicity; bar_f_p is the factor degree averaged over all original root indices.
Taking F=floor((1-epsilon)L-1), which is positive for small enough m, gives

    liminf_(m->0) bar_f_p(P)/L >=1,
    limsup_(m->0) L B_p(P)/d <=1.                          (16)

Indeed the degree mass above F is1-o(1), so bar_f_p>=(F+1)(1-W_(p,F)/d).
Also

    B_p/d=sum_f (w_(p,f)/d)/f
         <=W_(p,F)/d+1/(F+1).

The explicit rate(14) implies L W_(p,F)/d->0.
First let m tend to zero with epsilon fixed, then let epsilon decrease to zero.
This proves both statements in(16) with their order of limits explicit.
They are necessary complexity bounds, not a factorization algorithm or a claim that every reduction is irreducible.

<a id="growing-prime-total-low-degree-mass"></a>
### 4. A genuinely growing multi-prime mass bound

Fix an integer F>=1 and a real exponent0<kappa<1/(F+13).
Then, as m tends to zero through actual nontorsion inputs,

    (1/d)sum_(p<=m^(-kappa)) (log p) W_(p,F) ->0.           (17)

This positive sum records separate modular degree masses at different primes; it is not assigned to any single cyclic norm.
No prime-number theorem or independence of reductions is needed.
There are at most m^(-kappa) such primes.
At each one, m p^(F+1)<=m^(1-kappa(F+1)), whose exponent is positive.
Formula(11), monotonicity of Omega, and the elementary prime-count bound give

    (1/d)sum_(p<=m^(-kappa)) (log p) W_(p,F)
       <= F m^(-kappa) Omega(m^(1-kappa(F+1))).             (18)

By(6), this is

    O_(F,kappa)(m^((1-kappa(F+13))/12)
                          (1+log(1/m))^(1/6)),

which tends to zero exactly in the claimed sufficient range.
The exponent13 reflects the explicit expense modulus used here, not an asserted sharp barrier.
Enlarging this prime range by optimizing that exponent is not proposed as the missing G0001 mechanism.

Equation(17) does not bound the total valuation of those primes at arbitrary exponents.
A small number of local roots can in principle have large depths, and their relevant exponents may lie outside this degree-adapted window.
It does not omit that possibility or turn low multiplicity mass into an upper bound for all arithmetic income.
Its content is that a polynomially growing collection of bounded-degree modular clusters still has vanishing total degree-weighted mass at the stated costs on a hypothetical near-one sequence.

### 5. What changes, and what remains open

L205 excluded fixed bounded-residue-degree concentration without a saturation hypothesis.
The present result excludes such concentration uniformly on the growing region(12), quantifies average reduction-factor complexity, and controls the multi-prime total(17).
All roots, repeated factors, actual local ramification costs and powered-degree drops are included.
This is a new growing-input consequence of the explicitly accepted discrepancy/house interfaces, not an actual near-one construction or another fixed-base peak calculation.

The good-prime part also has an easier retained-capacity comparison.
When Pbar is squarefree, a degree-f factor contributes distinct roots in F_(p^f), so W_(p,F)<=sum_(f<=F)(p^f-1)<=F p^F.
The accepted house consequence m>=c/d then gives W_(p,F)/d<=F m p^F/c.
This already excludes concentration in much of the displayed good-prime range.
The new all-input proof is needed for arbitrary repeated reductions and index primes, where their e_phi cannot be deleted from the mass.
No new good-prime capacity theorem is claimed; the point is the uniform extension with those multiplicities and their real p-adic costs retained.

The result moves the useful search away from positive degree mass in these affordable small residue-degree classes.
It leaves growing residue orders at and beyond the boundary m p^(F+1), unusually deep contributions carried by small mass, and genuinely coordinated same-exponent information as possible arithmetic mechanisms.
It supplies no theorem that one of them must produce positive-linear income at n<=Cd.
The consequences are compatible with a near-one hypothesis and therefore do not prove a Mahler gap.
Neither the minimal-Frobenius class nor local maximal orders are assumed, and no inverse/full-cofactor estimate is inferred.

## Original checking, source and fixed-input boundary

The exact complete original author-check/contribution/then-pending account remains in [its separately declared original SELF finding](../audits/reviews/Yin_R_G0727_v1.md#growing-residue-original-author-check-finding).
The [original R727 whole account](../audits/reviews/Yin_R_G0727_v1.md#original-growing-residue-review-account) retains its actual 04:32 completion, no-defect verdict, complete fixed L209 input, source-reading passages and all proof/inspection limits.
The original reviewer directly text-read retained Dim19v1 PDF p1 and Pri11 PDF pp2,7 at statement/application scope; those reading minutes were not separately recorded and are not inferred from the review completion.
The current complete local proof uses exactly those accepted source statements, not a later version or an uninspected stronger theorem.
All original L209 proof, history, fixed inputs and active/pending language remain unchanged and select no present research execution.
The earlier whole SELF could not by itself close the old UNKNOWN, identify a near-one family, merge different-time income or supply unresolved inverse/full-cofactor coverage.
