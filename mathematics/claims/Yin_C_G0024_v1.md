---
author: Yin
---

# Exact obstruction for a finite original-Lehmer first-window atom family

Date: 2026-10-11T19:55.
Human author Yin.
Provenance: project deduction with exact finite computational evidence.
The responsible author developed D18/J88 after root supplied the research question.
Root's coordinating metadata-bug discovery and changed exact-validation scope are author contributions, not independent native review.
Internal restricted result within the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract); no main-theorem designation or full-capacity conclusion.

## Statement

Fix the ORIGINAL Lehmer polynomial P with ascending coefficients

    p=[1,1,0,-1,-1,-1,-1,-1,0,1,1],

original degree10 and actual O_0=Z[alpha].
The allowed common coefficient window is[0,10], with exact remainder A=[I_10,-p_low].
For this statement define ONLY the following finite coefficient atom family F:

Take each nonzero r in{-1,0,1}^10 with first nonzero coordinate+1 and each k in{-2,-1,0,1,2}, put c=(k-r dot p_low)/9 and f=(r,0)+cP, retain only exact coefficient energy at most4, and identify global signs by the first nonzero COEFFICIENT.
Add the11 explicit initial atoms1 and1+t^h,h=1,...,10, with the same sign/deduplication convention.
There are147631 generated labels and EXACTLY13197 distinct atoms.
Every atom has nonzero ACTUAL integral remainder and coefficients of denominator dividing9.
These restrictions select F, not the full rational domain or all denominator9 representatives.

Let a_h(f)=sum_(j=0)^(10-h) f_j f_(j+h), h=1,...,10.
The exact finite certificate is

    ||f||^2-1-a_2(f)+a_6(f)+a_7(f)
          -a_8(f)-a_9(f)+a_10(f)>=0

for EVERY f in F.
It is verified by complete exact generation and integer evaluation on all13197 atoms, with common slack denominator81.
Therefore over ANY finite positive normalized REAL weights on F with all aggregate a_h zero, the minimum weighted coefficient energy is EXACTLY1, attained by the constant atom1.
Rational weights give the same restricted minimum.
This is a finite-family statement, not a global Toeplitz/lattice certificate.

Adopted C17 proves that the FULL actual original-Lehmer first-window rational capacity is strictly below1.
Thus at least one of the declared finite-family restrictions must change to reach such a witness.
The statement does NOT identify which restriction, exclude all denominator9 packets, give an exact full-capacity optimum or yield a new positive Mahler bound.

The only returned Phase A rational packet is constant1 with weight1: actual union width0 within allowedT10, q=M=1, integer energy S=1, content1 and full signed residue/numerator norms1.
Its normalized surplus is0.
No nonconstant returned-packet norm data or new arithmetic income is inferred from the finite dual.

## Current assessment
[Selected decision](#decision-organized-reviewed)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T19:55 |
| status | open |
| reason | Register the exact restricted-family certificate and weighted-sum proof with the entire03:48 D18 author history and complete declared J88 evidence. Separate whole mathematical/native and actual extraction review are pending. The preserved first-phase metadata erratum is not silently repaired or reauthenticated. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ONE originalP/T10 and the EXACT declared finite atom family F, arbitrary positive real normalized complementary weights and restricted optimum1 ONLY. |
| argument | [Argument](#argument) | Complete03:48 D18 author freeze and direct exact-dual weighted-sum proof, all finite-domain and evidence/provenance limits retained. |
| support | [J88 declaration and complete executions](../computations/programs/Yin_J_G0088/readme.md) | Native evidence: both bounded predeclared author phases, exact domain, programs/outcomes, mutable-initial-basis erratum and known-structure restoration limit. |
| support | [Exact finite certificate and native payload](../computations/programs/Yin_J_G0088/readme.md#phase-b-completed-author-validation) | Native evidence: all13197 exact slack numerators, fixed saved dual, regenerated atoms and original-basis erratum; the responsible J section links the unchanged exact-validation.json, with no floating optimality claim. |
| support | [Exact integer-value packet domain](Yin_C_G0016_v1.md#statement) | Comparison of the restricted family with the full rational/formal-real capacity domain; not an input substituting for the finite certificate proof. |
| support | [Full-domain first-window theorem](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | The actually irreducible original input has FULL E_10<1; this distinguishes the restricted obstruction from the full domain and is not a restricted-dual proof premise. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T20:09 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | ONE originalP/T10 and the EXACT declared finite atom family F, arbitrary positive real normalized complementary weights and restricted optimum1 ONLY. |
| argument | [Argument](#argument) | Complete03:48 D18 author freeze and direct exact-dual weighted-sum proof, all finite-domain and evidence/provenance limits retained. |
| support | [Support](../computations/programs/Yin_J_G0088/readme.md) | Native evidence: both bounded predeclared author phases, exact domain, programs/outcomes, mutable-initial-basis erratum and known-structure restoration limit. |
| support | [Support](../computations/programs/Yin_J_G0088/readme.md#phase-b-completed-author-validation) | Native evidence: all13197 exact slack numerators, fixed saved dual, regenerated atoms and original-basis erratum; the responsible J section links the unchanged exact-validation.json, with no floating optimality claim. |
| support | [Support](Yin_C_G0016_v1.md#statement) | Comparison of the restricted family with the full rational/formal-real capacity domain; not an input substituting for the finite certificate proof. |
| support | [Support](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) | The actually irreducible original input has FULL E_10<1; this distinguishes the restricted obstruction from the full domain and is not a restricted-dual proof premise. |
| review | [Current independent finding](../audits/reviews/Yin_R_G0228_v1.md#c24-lehmer-finite-family-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |

## Argument

The complete D18 author argument is retained below.
The original retention comparison is recorded in [R228](../audits/reviews/Yin_R_G0228_v1.md#c24-lehmer-finite-family-extraction-finding); current storage and source-layout maintenance supplies no new mathematical review.
Its exact finite inequality, multiplying by positive normalized weights and cancelling all aggregate lags, proves the registered restricted conclusion.
The native integer assertion is supported by the full J88 certificate and the separately organized exact reconstruction recorded in R228, beyond agreement with the author's float candidate.
The constant attainer is explicit and its actual order/nonzero/norm/width conditions are checked locally.

The original mutable-list alias mislabeled Phase A's initial indices.
Known metadata-only changes were briefly made and reversed from inspected structure, with NO pre-edit raw-byte snapshot or authenticated original source baseline.
Exact original-byte equality remains independently unauthenticated.
Root's earlier direct inspection corroborates the alias line and equal saved lists.
Phase B's separately retained code/output recovers the true indices and verifies the exact finite dual independently of float optimality; it does not retroactively authenticate Phase A or rewrite that evidence.
A later independent exact certificate check likewise cannot invent such authentication.

## Original Lehmer first-window complementary packet calibration

Context: [G0001](../tasks/Yin_T_G0001_v1.md#contract).
Human author Yin; multinacci_source_intake AI now in a distinct AUTHOR role.
Root supplied only the research question and broad candidate suggestions, not a packet or proof.
This mathematical home is allocated before any native mathematical computation.

## Question and scope

Seek one explicitly verified finite rational complementary packet of energy below1 for the ORIGINAL Lehmer polynomial P=[1,1,0,-1,-1,-1,-1,-1,0,1,1] ascending, actual monogenic order Z[alpha], first allowed window[0,10].
Full nonzero integer residue coordinates, all exact lags, positive final rational weights, actual q/M/contents and signed original norms remain required.
The adopted [C16 domain](Yin_C_G0016_v1.md#statement) and [C17 strict first-window existence](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) supply the exact problem.
No optimum, uniform gap or constructive denominator bound is asserted.

## Reuse and execution boundary

The complete needed [C16 domain and quotient caution](Yin_C_G0016_v1.md#integer-moment-domain-and-energy) and [C17 first-window theorem](Yin_C_G0017_v1.md#first-low-energy-window-exact-degree) were read.
[L4](../ledger/Yin_L_G0004_v1.md#gram-lower-certificate) provides the saturated original remainder/Gram interface and its full degree cost; its old finite positivity certificate is different from this complementary packet.
[L237](../ledger/Yin_L_G0237_v1.md#scalar-sign-deep-floor-control) already gives Lehmer's scalar P-8 and projected lower-energy auxiliaries, but neither has exact constant covariance.
[L383](../ledger/Yin_L_G0383_v1.md#lehmer-bounded-candidate) and [J87](../computations/programs/Yin_J_G0087/readme.md) retain the exact original polynomial and a positive-log lower certificate; this experiment neither reruns nor improves that certificate.
[J10](../computations/programs/Yin_J_G0010/readme.md) retains the original binary period31, so the old q2/S2 binomial equality cannot be placed in width10.

The changed finite-domain comparison also read [L341](../ledger/Yin_L_G0341_v1.md#all-lattice-old-dual-criterion), [L355](../ledger/Yin_L_G0355_v1.md#unit-capped-exact-normalization), the actual J79 fast-optimum.py candidate-tableau implementation and its unit-cap author interface.
The old Lehmer norm-one comparison uses N20/T19 and optimizes residual coherence; it supplies no exact complementary first-window packet.
Its floating-discovery/exact-original-equation distinction is reused, while the present equality LP and atom class are separately authored.
Corrected directory/glob searches by first window, T10/N11 and Lehmer complementary packets found no existing exact witness at this scope.
This bounded screen is not a novelty or exhaustive-priority claim.
No new external theorem is needed: the finite witness implications below are direct algebra, and the numerical algorithm has no theorem role.

Operational runtime inspection found CPython3.12.14, existing NumPy/SymPy/flint in the repository environment, with scipy/CVXPY and other LP packages absent; no package was installed.
[J88](../computations/programs/Yin_J_G0088/readme.md) was allocated with the complete finite atom, denominator, solver and180-second one-run declaration BEFORE any mathematical execution.
Its native programs were authored and parsed without evaluation; the scoped D/J check passed.
No native mathematical program has run at this pre-run paragraph.
Numerical optimization supplies leads only; exact arithmetic must validate any claimed packet.
Finite candidate failure will not refute C17 or exclude the full capacity domain.
No remote Git or source intake is part of this AUTHOR investigation.

<a id="lehmer-first-window-exact-witness-implication"></a>
## Exact witness implication and full costs

Write P=sum_(j=0)^10 p_j t^j with the explicit original coefficients above.
In O_0 and allowed window[0,10], the remainder matrix is A=[I_10,-p_low], because alpha^10=-sum_(j=0)^9 p_j alpha^j.
Every coordinate can be written f=(r,0)+cP with r=Af.
In particular the declared atoms use nonzero integer r, so their actual values are nonzero O_0 elements; this uses the retained actual degree-ten irreducibility, not a single-embedding numerical test.
P's coefficient squared norm is9, explaining the fixed denominator9 projection offsets; changing representatives by cP preserves r but does not preserve autocorrelation, so ALL lags are imposed after representative selection.

For a returned finite rational vector of weights omega_b>=0, omit exactly zero weights and require sum omega_b=1.
The direct exact conditions

    sum_b omega_b sum_(j=0)^(10-h) f_(b,j)f_(b,j+h)=0,
    1<=h<=10,
    E=sum_b omega_b sum_(j=0)^10 f_(b,j)^2<1

prove the full constant Laurent identity sum_b omega_b f_b(t)f_b(t^-1)=E by coefficient comparison, including both positive and negative lags.
These equalities and Af_b in Z^10 minus{0} are sufficient for admissibility; no solver convergence, finite-family optimum or free PSD relaxation is used.
Exact reconstruction solves the ORIGINAL rational equalities on the discovered basis.
A negative reconstructed weight, failed lag or nonintegral residue is an actual failed witness, regardless of the float objective.

Let q be the ACTUAL least common coefficient denominator after zero labels are omitted, F_b=q f_b, M the ACTUAL least common weight denominator, m_b=M omega_b.
Retain each content gcd(F_b) without primitive rescaling.
With D_b=Norm(f_b(alpha)), the full original signed resultants obey

    Res(P,F_b)=q^10 D_b,
    product_b Res(P,F_b)^m_b=q^(10M)product_b D_b^m_b,
    S=q^2 E,
    I=log q+(1/10)sum_b omega_b log|D_b|,
    I-(1/2)log S=(1/10)sum_b omega_b log|D_b|-(1/2)log E.

The proposed verifier derives each signed D_b from the determinant of multiplication by the ACTUAL integer residue in the full degree-ten quotient and independently evaluates the exact polynomial resultant of P,F_b; equality with q^10D_b and D_b!=0 is required.
The entire copied product may be displayed as signed integer bases/exponents instead of expanding an infeasibly large integer.
Every original root and all multiplicities remain.
The generic-monic [C10 inequality](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) then charges (actualT/10)m(P); a below-one monogenic packet in this allowed window must have actualT10 by [C14](Yin_C_G0014_v2.md#short-width-power-order-obstruction).
No norm-one inventory or positive input-uniform surplus is assumed.

The proof of the finite implication is complete before execution; the existence of a verified concrete packet in this experiment remains unrun.
C17's independently adopted existence is not contingent on this selected atom screen succeeding.

<a id="lehmer-first-window-phase-a-outcome"></a>
## Phase A: completed bounded candidate search and evidence erratum

The J88 author calculation completed on 2026-10-12 using NumPy/SymPy for candidate discovery and exact reconstruction.
The 147,631 labels produced 13,197 distinct rational atoms; the heuristic used 897 floating pivots.
Exact reconstruction returned only the constant coordinate 1 at weight 1, with E=q=M=1, all ten lags zero, residue 1, signed original norm/resultant 1 and actual width 0.
No below-one witness was returned, and float termination does not prove a finite-family optimum or exclude true capacity packets.
The full [result.json](../computations/programs/Yin_J_G0088/inputs/result.json) retains this mathematical outcome.

Post-run source/output inspection found an evidence-record bug: REPORT['initial_basis']=basis retained a mutable alias, so the saved initial_basis list was changed by later simplex pivots into the FINAL basis list.
The original mathematical initial basis remains explicitly1 and1+t^h,h1--10, but its ORIGINAL index list was not retained correctly.
The final floating_lead.basis is the actual returned list, and the exact packet/lag/norm calculations do not use the mislabeled initial list.
Root independently noticed this same defect as AUTHOR coordination, not a whole independent native review.
A brief metadata/source correction was made before root's preservation message arrived; those known metadata-only edits were immediately reversed from the inspected original structure.
No pre-edit raw-byte snapshot or independently authenticated source-byte baseline existed, so exact original-byte equality is NOT independently authenticated.
Root corroborates the original alias line and both original equal index lists from its direct pre-message reading.
The erratum and this restoration limit are retained here, with no mathematical rerun or fabricated initial indices.
The original mathematical source/result were read-only inputs to the subsequent exact validation.

Phase A is closed at this scope: a finite heuristic search returned no below-one candidate, and the exact admissibility of its trivial returned packet was checked.
The actual C17 first-window existence and unrestricted Lehmer problem remain unchanged.

<a id="lehmer-first-window-exact-dual-validation-declaration"></a>
## Phase B pre-run declaration: exact unchanged-family validation

Root explicitly authorized one NEW bounded exact-validation phase after the Phase A erratum.
It uses the IDENTICAL original P/T10, finite ternary r/k/denominator9/energy4 generator and13197atoms; no LP rerun, atom enlargement, parameter retry or package installation is allowed.
A new permanent J88 validator will regenerate the original atoms ONCE, recover the true original1 and1+t^h indices, and solve the TRANSPOSE ORIGINAL rational equality system on the saved FINAL basis for a rational dual.
The original Phase A code/output remain unchanged inputs.
One aggregate execution has180seconds wall cap and stops on the first scope/resource/structural failure.
A first strictly negative EXACT reduced cost is a completed failed-dual result with the actual full atom retained, not a reason to choose a new basis.

For each atom f write e(f)=||f||^2 and a_h(f)=sum_j f_j f_(j+h).
A rational vector beta=(beta_0,...,beta_10) is sufficient for a finite-family lower bound when

    e(f)-beta_0-sum_(h=1)^10 beta_h a_h(f)>=0

for EVERY declared atom.
Multiplying by any positive normalized exact complementary weights and summing gives E>=beta_0 directly.
This is weak duality by finite summation, not reliance on the floating solver or a general LP theorem.
The final-basis transpose equations propose beta only; EVERY atom inequality must then be checked exactly.
If all13197slacks are nonnegative and beta_0=1, the retained constant coordinate proves that THIS finite family's minimum is exactly1.
A negative slack or other exact failure instead leaves the finite-family optimum unproved.
Neither outcome describes the entire C16/C17 domain.

To avoid repeated rational divisions, write f=F/9 and let L clear beta's denominators.
The exact reduced-cost numerator is

    L sum_j F_j^2-81(L beta_0)
      -sum_(h=1)^10 (L beta_h)sum_j F_jF_(j+h).

Checking its sign is exactly checking the stated rational slack, with denominator81L.
The new output must retain the true initial index list, saved final basis, exact beta/system, every checked slack numerator if successful or the first full negative atom, original input/generator count and precise execution outcome.
No independent project/native review is claimed by this author validation.

<a id="lehmer-first-window-exact-finite-family-result"></a>
## Phase B outcome: exact minimum one on the declared finite family

The separately declared exact validation completed on2026-10-12.
The regenerated original147631labels again gave EXACTLY13197atoms.
Every atom's actual residue was checked integral and nonzero, and its energy remained within the original cutoff.
The true original initial indices are

    [9704,12552,10877,10268,10044,9893,
     9798,9744,9719,9710,4563],

with all11full numerator vectors retained in [exact-validation.json](../computations/programs/Yin_J_G0088/inputs/exact-validation.json).
They differ from the original mislabeled list, as the source-code erratum predicts.
Their reconstruction is a NEW exact validation outcome, not a fabricated repair of Phase A's unavailable initial index evidence.
The saved FINAL Phase A basis and the full exact transpose system were retained separately.

The exact transpose solve gives the remarkably simple rational dual

    beta=(1,0,1,0,0,0,-1,-1,1,1,-1), L=1.

EVERY ONE of the13197reduced-cost numerators was checked nonnegative in integer arithmetic; the entire list remains in the new output, with common denominator81 and minimum numerator0.
There was no LP rerun, floating calculation, new basis selection, atom extension or negative-slack retry in this phase.
The direct finite-family inequality is therefore

    ||f||^2-1-a_2(f)+a_6(f)+a_7(f)
       -a_8(f)-a_9(f)+a_10(f)>=0                 (1)

for every declared atom.
This is an EXACT VERIFIED FINITE assertion, supported by complete enumeration of the predeclared integer residue/representative domain and exact evaluation, pending separate independent native review.
Multiplying(1) by any nonnegative normalized weights with all aggregate lags zero proves E>=1 on THIS finite family, including arbitrary real weights.
The constant atom1 is present, has nonzero actual integral residue and exact constant energy1, so the finite-family minimum is EXACTLY1.
Normalization does not require any strict-positivity issue: omit zero labels in an attaining finite combination.

This result discriminates the selected construction: the coarse denominator9 representative grid with these ternary residues and the energy4 cap cannot realize the below-one packet whose existence C17 proves in the complete rational domain.
At least one selected restriction must change to seek that packet.
The validation does NOT show which restriction is decisive, does NOT exclude all denominator9 packets, does NOT supply a whole-lattice Toeplitz certificate or prove a bound for every rational representative.
The actual Lehmer first-window capacity is still strictly below1 by adopted C17.
No nontrivial norm-income or new positive measure bound resulted here; the returned packet's q/M/contents/norm product are all1 and its surplus is0.
The original Lehmer positive-log certificate is unchanged.

<a id="lehmer-first-window-entire-author-freeze"></a>
## Entire author self-check and freeze

2026-10-11T19:48.
The author read and checked the COMPLETE D18 argument, both pre-run scopes, actual code and both native outcomes.
Checks include the original P signs and actual degree/order premise, A=[I,-p_low], all nonzero integer residue guards, exact lag conventions, rational reconstruction and weight normalization, actual versus allowed width, q/M/contents and full signed degree-ten norm/resultant formulas, and the absence of a nontrivial norm claim for the returned constant packet.
The first-run float result is not promoted to an optimum.
The mutable-initial-basis bug, author/root checking relationship, temporary correction/restoration limit and unavailable independent byte-authentication are expressly retained.

For the new exact phase the check covers unchanged deterministic atom ordering/canonical sign/deduplication and energy cutoff, all147631generated labels, every one of13197actual residue/energy guards, recovered true initial vectors, the saved final basis as the ONLY dual candidate, complete transpose equations, exact common-denominator slack formula, all13197nonnegative slacks and the direct weighted-sum proof of the restricted real-weight minimum1.
The constant attainer, no-full-capacity conclusion, all failed/positive finite boundaries and no-rerun distinction were checked against the saved payloads.
Programs were parsed and scoped D/J checks passed before both executions; the final changed materials are checked again after this paragraph.
No independent whole review is claimed by the author or root's coordinating bug finding.

The COMPLETE current D18, both scopes, outcomes, direct proof and limitations are author-frozen for separately organized noncontributor review.
The original programs, necessary first-phase/exact certificates and errata remain at J88's program/output homes; redundant operational archives are not mathematical prerequisites.
G0001 remains active and unrestrictedly unresolved.


## Registration and preservation operation

The native support locator selects the responsible J88 completed-validation section, which links the same exact JSON certificate.
This locator-only selection retains every original atom/slack and its actual inspection scope; it changes no argument, data, declared execution or review coverage.

2026-10-11T19:55: retain the COMPLETE2026-10-11T19:48 D18 author freeze, both pre-run scopes/outcomes and native erratum directly as this fixed Claim argument.
All original J88 files remain at their native responsible group; independent verification adds separately named program/output and actual scope.
Working-draft retirement waits for full-body comparison and incoming-reference maintenance.
No full-capacity, uniform-gap, new allowance or Task completion is inferred.
