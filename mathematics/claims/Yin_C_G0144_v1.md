---
author: Yin
---
# Torsion controls for sparse auxiliaries and linear-window arithmetic coverage

Opened: 2026-10-15T11:15.
Human author Yin.
Delegated new G0001 author inquiry by g_bridge_audit under root's continuing authorization.
Root supplied the actual-coverage direction, not a proof step.
C142v1 is the preceding complete capacity candidate under independent whole review and is NOT used as an adopted premise at opening.
The frozen D44 is untouched.

## Responsible question and exact boundary

For an actual monic irreducible nontorsion integer unit P of original degree d, seek a checkable arithmetic bridge that genuinely uses small total m(P)=log M(P), rather than only reciprocity, Salem root geometry or bounded coefficient height.
Positive good-prime root mass, an original linear time window and positive original triple density would suffice if C142 is adopted, but none is to be manufactured from an abstract capacity array or CRT lift.
A useful alternative must retain every original embedding, full signed norm, prime-size price, bad-prime/index loss and degree cost.
No existence of a near-one sequence is presumed.

## Opening bounded reuse

Read C100's exact efficiency-two/prime-power coverage and genuine fixed control; L395's bounded relative-core theorem with its complete scaling and superlinear-window star obstruction; L159's original Frobenius capacities, automatic-average limitations, genuine small-measure controls and excluded bad primes; C116's actual original norm/prime-price budget; C136's Salem all-depth failure at5 and successful prime3 on the SAME far-from-one family; and C141's simultaneous finite-pool sparse-auxiliary obstruction with its explicit positive Mahler floor.
These controls do not refute a sufficiently-near-one coverage theorem.

The next bounded search concerns original integral traces/Frobenius congruences and their actual small-measure errors, and possible use of the full monogenic order when good-prime selection loses actual norm income.
Recognized source results must be checked before adoption; no new source theorem is assumed here.
All substantive deductions and useful failed routes will be retained below.
No mathematical native computation or J is proposed at opening.

<a id="near-one-trace-screen"></a>
## 1. What the opening trace screen actually supplies

The exact existing [C1 radial-to-integer-trace estimate](Yin_C_G0001_v1.md#statement) is

    |Tr(alpha^n)-sum_i exp(in theta_i)|<=2n exp(nm)m.       (1)

It has no hidden degree factor, but it does not make the angular sum small on the absolute integer scale.
[C8](Yin_C_G0008_v1.md#fixed-mode-forced-tail-interface) already isolates the actual high-frequency compensation left by cyclotomic norm tests; its o(sqrt(d)) fixed-trace target is not an adopted theorem.
The Frobenius congruence s_(pn)=s_n modulo p by itself supplies no missing small absolute error.
Thus simply combining (1), integer traces and ordinary weak angular equidistribution would repeat an unresolved old step.
No such bridge is asserted here.

The different control below tests an even stronger set of proposed inputs at EXACT zero measure.
It is not an actual nontorsion counterexample: its purpose is to determine whether nonvanishing on just the tested linear window and the local/complex constraints visible there can replace the global nontorsion hypothesis.
The answer is negative at the precise scope proved below.

<a id="squarefree-cyclotomic-code"></a>
<a id="argument"></a>
## 2. Exact sparse-multiple bound in every characteristic

Let N>1 be SQUAREFREE, with prime divisors q_1,...,q_r, and let q_min=min q_i.
For EVERY field k, including characteristic dividing N, the least support size of a nonzero polynomial F in k[t] satisfying

    deg F<N,  Phi_N mod k divides F

is exactly

    q_min.                                                (2)

Here Phi_N mod k denotes the full reduced polynomial with every multiplicity; it need not be separable or irreducible over k.
The statement concerns divisibility by that full polynomial, not vanishing at one finite-field root or one factor.

First construct an INTEGRAL tensor model, before any reduction.
Put S_q(x)=1+x+...+x^(q-1) and

    B= tensor_(q|N) Z[x_q]/S_q(x_q),  z=product_(q|N)x_q.

Each factor is free over Z of rank q-1, with basis1,x_q,...,x_q^(q-2), and x_q^q=1.
Choose by CRT an integer e_q>=0 that is1 modulo q and0 modulo every other prime dividing N.
Then z^(e_q)=x_q, so the map Z[t]->B, t->z, is SURJECTIVE.
After tensoring with C the factors split at their nontrivial q-th roots; each value of z is a primitive N-th root.
Hence Phi_N(z)=0 in B tensor C.
Since B is free over Z this identity already holds in B.
Consequently there is a surjection

    Z[t]/Phi_N(t) -> B.                                   (3)

Both sides are free Z modules of rank phi(N)=product(q-1).
The kernel is zero: after tensoring with Q the surjective map has equal finite dimensions, and a subgroup of the torsion-free source cannot be nonzero torsion.
Thus(3) is an isomorphism.
This integral argument is the reason BAD characteristics are included; a separable Fourier evaluation only would not justify them.

Base-changing (3) to any field k gives the same tensor description.
In k[x]/S_q, ANY proper subset of the q classes1,x,...,x^(q-1) is linearly independent.
Indeed a relation of degree at most q-1 lies in the ideal of the monic S_q and therefore is a scalar multiple of S_q; a missing coefficient forces that scalar to0.
This remains valid in characteristic q.

Suppose F has h<q_min distinct exponents0<=a_j<N and all h coefficients nonzero.
The corresponding tensor columns are tensor_q x_q^(a_j mod q).
For a fixed j and each q, the distinct q-coordinate classes appearing among these h columns form an independent set of size at most h<q.
Choose a linear functional on that factor which takes value1 on the j-th coordinate class and0 on every OTHER coordinate class actually appearing.
Extend it arbitrarily to a basis.
The tensor product of these functionals takes value1 on column j and0 on every other column: two distinct exponents below N differ modulo at least one q by CRT.
Applying it to the putative relation gives the j-th coefficient, a contradiction.
Thus h>=q_min.

For equality, take any smallest prime q|N and

    F(t)=1+t^(N/q)+...+t^((q-1)N/q).                      (4)

It has q nonzero coefficients in every field, degree N-N/q<N, and is divisible by Phi_N over Z because it vanishes at every primitive N-th root.
Monic division preserves this divisibility after reduction to any field.
This completes(2), including its exact upper witness.

This elementary tensor-check distance mechanism is classical linear algebra, not claimed novel coding theory.
A bounded primary-source search read Fan--Li--Hsieh--Chen, On Quantum Tensor Product Codes, published Quantum Information and Computation17(2017),1105--1122, Section2.2 and Lemma4 on printed1109--1110, at https://www.rintonpress.com/xxqic17/qic-17-1314/1105-1122.pdf.
It discusses minimum-distance minima for tensor products of check matrices, with an extension-field convention.
That different convention is NOT imported as the proof of(2); the integral cyclotomic model and all-characteristic column proof are supplied completely here.
The broader coding results and cited original Wolf proofs were not audited.
The attempted arXiv1605.09598v4 PDF open failed and supplies no source evidence.
No new source acceptance or acquisition is claimed.

The standard monicity, irreducibility and degree of Phi_N, and the equality O_(Q(zeta_N))=Z[zeta_N], are already accepted at the exact [Bel17 scoped reading](../audits/literature/Bel17/readme.md).
That record was actually read before use; its original Washington/Lang proofs were not newly audited.
A separate Stanford lecture-note search supplied only an unnecessary corroborating lead and is not an additional premise.

<a id="zero-measure-all-prime-control"></a>
## 3. Actual zero-measure controls at every prime

Fix an integer K>=1, a real C>0 and any finite prime pool Pi (possibly empty).
Choose a squarefree odd N with

    q_min>max(K,2,max(Pi)),  N/phi(N)>C,                  (5)

where max(empty)=1.
Such N exist in arbitrarily large degree: removing finitely many primes does not change divergence of their reciprocal sum, and product_(q|N)(1-1/q)^(-1) can be made arbitrarily large.
This is exactly [C220's retained elementary prime-reciprocal argument](Yin_C_G0220_v1.md#discriminant-divergence), not an invoked prime-number asymptotic.
Use the ACTUAL monic irreducible reciprocal unit

    P=Phi_N, d=phi(N), alpha=zeta_N, m(P)=0.              (6)

These are torsion inputs, deliberately outside the unrestricted task's nontorsion core.
They are not CRT lifts and have no hidden noncyclotomic factors or ignored original roots.

For every rational prime p, (2) and Cd<N show that NO nonzero polynomial over F_p with degree at most floor(Cd) and at most K terms is divisible by the FULL P mod p.
This statement includes every bad prime and all reduction multiplicities.
It is simultaneous over ALL primes, stronger than avoidance merely at the preselected finite pool.

For every p not dividing N, t^N-1 is separable modulo p and its cyclotomic factorization shows that the roots of P mod p are exactly the distinct primitive N-th roots.
In particular p is good, and ALL d original roots have residue order N.
For every integer1<=X<=Cd<N, every positive selection of complete order groups therefore has

    H_X=0,  delta_(k,X)=0 for every integer k>=1.          (7)

The full group has W=d and obeys w_N=d=phi(N).
Thus the linear mass and linear time requirements themselves do hold; it is actual eligibility and density which fail.
At primes dividing N the full-polynomial sparse obstruction above still holds, but no false distinct-root capacity or good-prime order statement is assigned to those nonreduced reductions.

There is also NO nonzero integer F with degree at most floor(Cd), at most K terms, and ANY integer b>=2 such that

    F(alpha)/b belongs to O_(Q(alpha)),
    m(F)-log b<0.                                         (8)

The denominator has no restriction on its primes or their depths.
To prove this, use the already accepted O_K=Z[alpha].
Let c be the positive content of F, g=gcd(c,b), F1=F/g and b1=b/g.
If b1=1 then F1 is a nonzero integer polynomial and m(F)-log b=m(F1)>=0, contradicting(8).
If b1>1, choose p|b1.
The content of F1 is prime to p.
Integrality gives F1(alpha) in pZ[alpha]; monic remainder uniqueness therefore says P mod p divides the NONZERO F1 mod p.
Its degree and support do not exceed those of F, contradicting(2) and(5).
The value F(alpha)=0 cannot be a loophole: by (2) in characteristic0 no such sparse F of degree<N is divisible by P.
This proves the claim with maximal-order, content, good/bad primes and all original degrees retained.

The same argument yields the useful exact integral statement: for any integer b>=2 and degree<N polynomial F with fewer than q_min terms, F(alpha) in bO_K forces EVERY coefficient of F divisible by b.
For each prime power p^e|b first use the modulo-p independence to divide all coefficients by p, then repeat e times in the free ring Z[alpha].
This pays arbitrary bad-prime depths instead of discarding them.
Consequently the full norm of F(alpha)/b, when integral, is simply the norm of an integer-coefficient sparse representative after that common-content division; no primitive local gain has been obtained.

<a id="zero-measure-full-window-budget"></a>
## 4. The original short-window norms are nonzero and small as well

The controls can be chosen in a sequence N_j with q_min(N_j)->infinity and N_j/phi(N_j)->infinity: for each j take a finite product of primes greater than max(j,2) whose reciprocal Euler product exceeds j.
Put d_j=phi(N_j).
For EVERY fixed C>0, eventually N_j>Cd_j.
Thus throughout the original linear window1<=n<=floor(Cd_j),

    D_n=Norm_(Q(zeta_N)/Q)(zeta_N^n-1)
       =Res(Phi_N,t^n-1) is a NONZERO signed integer.     (9)

Let h=N/gcd(N,n)>1.
The value zeta_N^n is a primitive h-th root.
The actual cyclotomic field degree/tower gives

    |D_n|=Phi_h(1)^(phi(N)/phi(h)).                     (10)

Since N is squarefree, h is squarefree.
If h has at least two prime factors, the accepted Bel17 Phi_h(1) identity gives |D_n|=1.
If h=q is prime, then Phi_q(1)=q directly from S_q, and

    log|D_n|/d=log q/(q-1).

The function log x/(x-1) decreases for x>1, since log x>1-1/x.
Therefore the COMPLETE original budget, including all rational primes and every local depth, satisfies

    0<=U_C(Phi_N):=max_(1<=n<=floor(Cd))log|D_n|/d
       <=log(q_min)/(q_min-1) ->0.                       (11)

The maximum is understood only for a nonempty window, which holds eventually because d_j->infinity.
This is an exact computation using the full original norm tower, not an upper bound merely on good-prime first layers.
For these n all norm prime factors, when any occur, are primes dividing N; the good-prime zero-return result(7) is consistent with that complete accounting.
At n=N the norm IS zero, and the original time ratio N/d is unbounded.
Global nontorsion cannot be replaced by nonvanishing on each preassigned fixed degree-linear window.

For every FIXED positive integer k, eventually q_min>k.
CRT decomposition of primitive roots gives the exact original integer trace

    Tr(zeta_N^k)=product_(q|N)sum_(a=1)^(q-1)zeta_q^(ak)
               =(-1)^(# {q:q|N}).                        (12)

All conjugates are on the circle, so the radial error in(1) is exactly0.
These controls therefore satisfy bounded absolute fixed-mode traces, not merely normalized equidistribution.
Ordinary Frobenius trace congruences hold for them as for any integer polynomial.
Neither those facts nor the full short-window norm decay(11) force the missing sparse auxiliary or good-prime positive density.
The nontrivial argument still needed for positive m must use more than those local consequences shared with torsion.

<a id="actual-near-one-obligation"></a>
## 5. The precise failed transfer and the still-live positive target

Sections2--4 refute the enlarged coverage assertion obtained by replacing actual nontorsion with m(P)<=epsilon plus nonzero cyclic norms throughout a FIXED linear window.
They also refute any derivation using only reciprocity, exact circle geometry, bounded fixed traces, goodness of the selected finite prime pool, maximal-order integrality and small full budgets on such windows.
Every one of those facts holds on the actual controls above, while all good-prime densities are0 and bounded-term linear-degree integral auxiliaries with a positive normalized Mahler margin are absent at EVERY denominator.

This is NOT a counterexample to sufficiently-near-one NONTORSION coverage, and no sequence with0<m(P)->0 has been constructed or assumed.
The exact m=0 boundary is essential, not a concealed strengthening of the task.
In particular C136/C141's far-from-one controls and the present torsion controls bracket different missing hypotheses; neither fills the genuinely small-positive-measure regime.
C142's candidate general capacity theorem remains logically independent of this obstruction because(7) has no positive-density premise.

A viable positive arithmetic bridge must distinguish a nontorsion input quantitatively from this torsion behavior at a price compatible with original O(d) auxiliary degree.
Merely testing nonzero norms up to Cd does not do so.
Using the actual global torsion exponent of these controls would first reach n=N, whose ratio N/d diverges, and that is precisely a time expense which cannot be suppressed.
This round does not replace the missing step by a newly named statistic or an assumed low-complexity selection; it retains the complete obstruction to the tested shortcut and leaves the original positive-m question open.

<a id="statement"></a>
## 6. Complete statement, dependencies and author checks

**All-characteristic sparse-multiple statement.**
For every squarefree N>1 and every field k, the full-polynomial code {F in k[t]:deg F<N, Phi_N mod k divides F} has minimum nonzero support q_min(N).
This includes characteristics dividing N and all multiplicities.
Equations(2)--(4) give the complete proof and attaining witness.
This is a claim about full polynomial divisibility; a single irreducible factor of Phi_N mod k may obey a different sparse-relation bound.

**Actual torsion boundary sequence.**
There exist squarefree odd N_j with q_min(N_j)->infinity and N_j/phi(N_j)->infinity, and actual monic irreducible reciprocal polynomials P_j=Phi_(N_j) of degree d_j=phi(N_j), such that m(P_j)=0 and the following hold for EVERY fixed C>0 and K>=1, eventually in j.
Every cyclic norm D_n is nonzero for1<=n<=floor(Cd_j), and its complete normalized maximum is at most log(q_min)/(q_min-1), tending to0.
Every p not dividing N_j is good and all original reduced orders equal N_j, so every positive original selection has zero capture and zero ordered tuple density at all such windows.
The full P_j mod p divides no nonzero polynomial of degree at most floor(Cd_j) with at most K terms, for EVERY rational prime p including bad primes.
For EVERY integer b>=2, no nonzero integer F in that degree/support class has both F(zeta_(N_j))/b integral in the FULL ring of integers and m(F)<log b; more precisely that integrality forces coefficientwise divisibility by b.
For each fixed trace index k, the exact original trace is eventually(-1)^(omega(N_j)).
Every fixed finite prime pool consists of good primes eventually, because q_min tends to infinity.

These quantifiers do NOT permit C or K to grow with j without verifying the actual finite tests Cd_j<N_j and K<q_min(N_j).
The sequence is wholly torsion.
It disproves the shortcut that replaces nontorsion by short-window nonvanishing and its listed geometric/budget consequences, not a sufficiently-small-POSITIVE-measure coverage theorem.
C142, whether candidate or subsequently adopted, is not a proof dependency of any assertion here.

The direct mathematical inputs are the existing [Bel17-U001 accepted cyclotomic statements](../audits/literature/Bel17/Yin_U001.md#bel17-u001): monic irreducibility/degree, full integral power basis and Phi_h(1) for a non-prime-power h; and [C220's retained elementary prime-reciprocal divergence](Yin_C_G0220_v1.md#discriminant-divergence).
The latter proof is used only for the existence of finite prime products satisfying the stated inequalities.
Prime Phi_q(1)=q and the all-characteristic code claim are proved here.
The finite norm tower, CRT, monic division, linear functionals and scalar Mahler content identity are used at their elementary exact scopes.
C1/C8 supply the opening comparison; C100/L395/L159/C116/C136/C141 delimit the actual research question, not missing premises of the torsion control.
The inspected coding paper is mechanism attribution/comparison only, not a substitute for the integral proof.

Author checking reconstructed the integral tensor surjection and equal free ranks before reduction, the CRT identification of all N exponent columns, factorwise independence in every characteristic, the tensor functional for each selected column, exact sharp witness and squarefree restriction.
It separately checked the common-content and EVERY-prime-power argument in the full actual cyclotomic integer ring, including F(alpha)=0, constant F and b supported on bad primes; actual original degree/time and complete selections; the nonempty eventual time window; the exact norm tower and all h cases; the monotone log q/(q-1) bound; fixed versus varying C/K/trace quantifiers; and the precise exclusion of any nontorsion or near-one positive realization claim.
No source-proof audit beyond the inherited declared scopes, native mathematical computation, new J or global record edit was performed.

<a id="author-freeze-2026-10-15"></a>
## 7. Entire author freeze

2026-10-15T11:24.
Freeze the ENTIRE original, including its responsibility/reuse screen, Sections1--7, equations(1)--(12), the exact all-characteristic sparse-multiple proof, all-denominator original-integer-ring obstruction, complete short-window norm and fixed-trace controls, and the explicit still-open positive-m scope.
Main statement is [#statement](#statement); argument begins at [#argument](#argument).
The root supplied the direction and read progress but no proof step.
The present author supplied the tensor adaptation and arithmetic control.
This is author checking only and requires a separately organized review of the actual fixed artifact before any adoption.
The structural material check is not a mathematical review.


## Fixed organization and source completion

Retain the complete author account, all12 formulas, squarefree/all-characteristic code proof, all-denominator integral statement, actual zero-measure sequence, full-window norms, fixed traces and exact exclusion of any small-positive-measure conclusion.
This quantified torsion-boundary theorem has no existing adequate fixed home.
Root supplied direction only; g_bridge_audit supplied the new proof; f_unitary_scope supplied later source-only verification, not a project proof step.

The fresh [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001) now canonically retains the same exact cyclotomic inputs used above, with successful actual-source acquisition, precise original-proof limits and correction of the old readme's Lang attribution to Neukirch.
This changes no mathematical premise.
[FLHC17-U001](../audits/literature/FLHC17/Yin_U001.md#flhc17-u001) records the already recognized coding mechanism at its actual extension-field, related-attribution scope; it is not a premise of the local integral proof.
The opening C142 status and earlier reading dates remain historical; C142 is not used by this argument.

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-15T11:46 |
| status | open |
| reason | Retain the complete all-characteristic cyclotomic sparse-distance theorem and all-prime torsion boundary controls. They rule out the specified replacement of global nontorsion by short-window nonvanishing; actual positive-measure coverage and G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete torsion-control statement](#statement) | Entire Section6, exact squarefree/all-field code distance, all-denominator statement and all fixed-window quantifiers, including torsion limitation. |
| argument | [Complete argument](#argument) | Whole Sections1--7 and12 formulas, with full source, reuse and contribution scope. |
| dependency | [Accepted cyclotomic inputs](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Monic irreducibility/degree, full integer power basis and Phi_h(1) at non-prime-powers; source-proof limits explicit. |
| dependency | [Prime reciprocal divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only the elementary finite Euler-product existence argument, not its separate discriminant conclusion. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:04 |
| status | proved |
| reason | Select adopted C220 as the current complete home of the identical retained L17 elementary prime-reciprocal divergence. Its actual selected adoption and complete needed finite Euler-product/harmonic-series argument were read and matched to the fixed L17 section. Reuse is limited to that elementary divergence and its original attribution, with no discriminant theorem, reciprocal counterexample family or prime-distribution rate added to this input. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete torsion-control statement](#statement) | Entire Section6, exact squarefree/all-field code distance, all-denominator statement and all fixed-window quantifiers, including torsion limitation. |
| argument | [Complete argument](#argument) | Whole Sections1--7 and12 formulas, with full source, reuse and contribution scope. |
| dependency | [Accepted cyclotomic inputs](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Monic irreducibility/degree, full integer power basis and Phi_h(1) at non-prime-powers; source-proof limits explicit. |
| dependency | [Prime reciprocal divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Only the elementary finite Euler-product existence argument, not its separate discriminant conclusion. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0801_v1.md#cyclotomic-sparse-control-whole-independent-finding) | Whole actual argument, both direct inputs, every characteristic and denominator depth, full original norm/trace and all fixed-parameter torsion limits. |

### Decision isolated-whole-review-20261023-m04

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:52 |
| status | proved |
| reason | Select the newly performed isolated whole review of this exact fixed statement, complete argument and all selected input interfaces at their stated restricted scopes. Preserve the proved mathematical status, unchanged statement and argument, every nonreview relation and scope, and all historical decisions. The retained older unknown finding keeps its actual date, checks and limits; this new finding supplies new evidence at its actual date without certifying old isolation, backdating adoption, or completing or resuming G0001. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete torsion-control statement](#statement) | Entire Section6, exact squarefree/all-field code distance, all-denominator statement and all fixed-window quantifiers, including torsion limitation. |
| argument | [Complete argument](#argument) | Whole Sections1--7 and12 formulas, with full source, reuse and contribution scope. |
| dependency | [Accepted cyclotomic inputs](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Monic irreducibility/degree, full integer power basis and Phi_h(1) at non-prime-powers; source-proof limits explicit. |
| dependency | [Prime reciprocal divergence](Yin_C_G0220_v1.md#discriminant-divergence) | Only the elementary finite Euler-product existence argument, not its separate discriminant conclusion. |
| review | [New isolated whole finding](../audits/reviews/Yin_R_G0801_v1.md#g0144-m04-isolated-whole-finding) | Complete exact fixed statement, whole argument, every selected input, all parameter/domain/original-degree costs, exceptional branches and source/noncompletion limits. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-15"></a>

### Historical assessment whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-15T11:54 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt the actual whole independent review of the all-characteristic cyclotomic minimum-support theorem and all-denominator, complete-norm torsion controls. The precise failure is replacing global nontorsion by the listed short-window properties; actual small-positive-measure coverage and G0001 remain open. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete torsion-control statement](#statement) | Entire Section6, exact squarefree/all-field code distance, all-denominator statement and all fixed-window quantifiers, including torsion limitation. |
| argument | [Complete argument](#argument) | Whole Sections1--7 and12 formulas, with full source, reuse and contribution scope. |
| dependency | [Accepted cyclotomic inputs](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Monic irreducibility/degree, full integer power basis and Phi_h(1) at non-prime-powers; source-proof limits explicit. |
| dependency | [Prime reciprocal divergence](../ledger/Yin_L_G0017_v1.md#discriminant-divergence) | Only the elementary finite Euler-product existence argument, not its separate discriminant conclusion. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0801_v1.md#cyclotomic-sparse-control-whole-independent-finding) | Whole actual argument, both direct inputs, every characteristic and denominator depth, full original norm/trace and all fixed-parameter torsion limits. |
