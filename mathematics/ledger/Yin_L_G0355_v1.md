---
author: Yin
---

# Norm-one finite comparisons: exact improvements and a retained certificate failure

Date: 2026-10-10T15:38.
Human author: Yin.
Fixed finite comparison for [G0001](../tasks/Yin_T_G0001_v1.md#contract), developed in D221 and reviewed at the scope below.

<a id="unit-cap-fixed-scope"></a>
## Current adopted scope

For the three retained original inputs at degrees10/20/32 and windows20/40/64, keep every monomial and admit only retained residues with absolute full original norm1 and normalized energy at most1.
The exact true-surplus constraint is S>=2, equivalent to eta>=log2/2.
The complete real-weight normalization, weak-duality proof, compression/lifting and original integer costs are reviewed below.
The actual finite families have39/63/105 columns; no complete unit or energy-ellipsoid enumeration is claimed.

Five exact primal/dual certificates are adopted: P10 baseline/enlarged have kappa in[3.0845,3.0846)/[3.0617,3.0618), n18 baseline/enlarged in[4.0386,4.0387)/[4.0185,4.0186), and n30 baseline in[4.6211,4.6212).
Both completed pairs strictly improve the genuinely optimized monomial baseline without nonunit norm income.
All five have S=2.
The n18 enlarged finite optimum remains above4.
Complete rational values, all original columns, weights, multiplicities, signed norms, contents, aggregate polynomials and radial expenses remain in the proof and [J79 native evidence](../computations/programs/Yin_J_G0079/readme.md#unit-cap-first-author-outcome).

The n30 enlarged instance has a reviewed exact feasible primal only.
Its reconstructed dual fails |y_9|<=1 despite zero algebraic gap; its saved floating basis tableau also fails an independent original-equation check.
No optimum or negative unit-direction conclusion is adopted for this instance.
The author run ended at that first exact failure, with unreached completion fields absent.
It was not retried.

The [complete noncontributor finding](../audits/reviews/Yin_R_G0179_v1.md#unit-cap-complete-independent-review) covers the whole frozen argument and all reached new native fields through two distinct actual scopes.
The first full native review passed all304 original directions and five complete certificates, then FAILED on the sixth floating tableau.
The separately authorized previously unexecuted exact remainder passed; it leaves the first failure and invalid dual intact.
This is not a passed full numerical report or a repaired all-six certificate.
Root supplied the comparison design; the noncontributor reviewer supplied none of the present derivation and disclosed its prior upstream reviews, shared context and helper-method reuse.

The unrestricted G0001 contract remains unresolved.
These fixed inputs and finite improvements supply neither all-unit optimality nor near-one uniformity.

## Material provenance

D221's complete mathematical argument, exact results, substantive failure and review findings are retained here.
Programs, computation protocols, native certificates, unsuccessful outputs and inspection facts belong to [J79](../computations/programs/Yin_J_G0079/readme.md#unit-cap-pre-run).
The dated author-freeze and review descriptions below identify the original inspected D221 revision; their byte counts and historical inspection statements do not describe the current maintained file.
The mathematical statements, dependencies, evidence and review conclusions are unchanged by this organization.

## Question

Compare the genuinely optimized monomial baseline with an enlarged finite family using only retained original direction records for n18/n30 from L341 and the original degree-ten Lehmer input from L348.
Every original monomial is retained, and every retained residue with absolute full norm1 and normalized energy at most1 is admitted.
Both families use the identical true-surplus target log2/2.
The complete original degrees, polynomials, norms, contents, weights, signed correlations and radial costs remain part of the comparison.
There is no new seed, LLL reduction, exponent box, input polynomial, energy-cap enlargement or full-ellipsoid enumeration.
Root supplied this comparison design; the derivation and implementation were by joint_boundary_research AI for Yin, and the separately organized review below discloses those roles.

<a id="unit-capped-exact-normalization"></a>
## 1. Responsible exact normalization and reused domain

Root supplied the finite comparison design; joint_boundary_research AI for Yin derives/checks the following normalization and implements the prescribed test.
The exact accepted interfaces are [L318](Yin_L_G0318_v1.md#weighted-integral-bundle-bound), [L341](Yin_L_G0341_v1.md#residual-lattice-fixed-scope), [L348](Yin_L_G0348_v1.md#lehmer-bundle-fixed-scope), and [L344](Yin_L_G0344_v1.md#joint-budget-fixed-scope).
Their complete original polynomials, irreducibility and native norms are reused as accepted inputs, not rerun or extended.
[L347](Yin_L_G0347_v1.md#full-surplus-fixed-scope) and [L351](Yin_L_G0351_v1.md#strict-budget-gap-fixed-scope) distinguish a sufficient norm-funded budget from true surplus.
The present norm-one restriction removes that distinction exactly, not approximately.
Root is a design contributor; the noncontributor review below was separately organized.

For each retained F=qB-PU with absolute full original norm |Res(P,B)|=1, define e=||F||^2/q^2>0 and h_l=sum_i F_i F_(i+l)/q^2.
For nonnegative masses v with sum e_j v_j=1, put S=sum v_j>0 and w_j=v_j/S.
Then

    E=sum w_j||F_j||^2=q^2/S,
    I=sum w_j log|Res(P,F_j)|/d=log q,
    eta=I-log(E)/2=log(S)/2,
    kappa=2 sum_l |sum_j v_j h_(l,j)|.             (1)

Thus the TRUE constraint eta>=log2/2 is EXACTLY S>=2.
No logarithm enclosure, norm subsidy, tangent budget or assumed equality case is needed.
Zero weights omit columns.
Every original norm is q^d, all contents stay in F, and neither individual primitive rescaling nor discarding original roots is allowed.

The finite LP is therefore v>=0,e dot v=1,1 dot v>=2 minimizing the last expression in(1).
For any |y_l|<=1,mu>=0 and unrestricted lambda with

    2H^T y-lambda e-mu*1>=0,                       (2)

multiplication by v gives kappa>=lambda+2mu.
An exact feasible primal and dual with equal values certifies the global optimum of THIS finite family.
This is the directly proved weak-duality step; the existing [BV04 attribution](../audits/literature/BV04/readme.md#selected-weak-duality-attribution) is reused, without assuming solver convergence or strong duality.
Mirrored monomial columns are compressed only after their complete e/h equality is checked; equal splitting restores all original columns.
Other retained residues are not silently identified or removed.

All original monomials have e_j=R_jj<=1, full norm1 and sum e_j=d; with N=2d the masses v_j=1/d give energy1 and S=2.
Thus every baseline and enlarged instance has an actual common feasible point.
Additional residues are admitted ONLY when their already retained full norm has absolute value1 and e<=1.
This is a finite selected list, not all integer points in the energy ellipsoid or all order units.
Enlargement can only lower the exact optimum, when both are actually certified.

## 2. Finite computation domain and original costs

The only source inputs are the old n18/n30 C matrices and all58/94 L341 residue records, and all48 original P10 L348 records.
The author computation used those retained norms and directions without a new input, seed, norm determinant, LLL reduction, exponent search, ellipsoid enumeration or energy-cap enlargement.
The instance order was P10 baseline/enlarged, n18 baseline/enlarged, n30 baseline/enlarged.
The unchanged candidate and rational-reconstruction settings, aggregate deadline and first-failure protocol are recorded in the [J79 declaration](../computations/programs/Yin_J_G0079/readme.md#unit-cap-resumed-implementation).

The [J79 computation record](../computations/programs/Yin_J_G0079/readme.md#unit-cap-pre-run) retains the complete schema, program and native data.
Every selected and excluded source residue retains its full B,F,kernel multiplier,norm,content,energy,correlations and decision; all original monomials remain.
Each started instance retains complete columns/matrices, candidate provenance if returned, all exact primal/dual systems and constraints if reached, and honest partial stages.
Completed certificates retain all weights, integer multiplicities, aggregate polynomial, complete arithmetic product q^(d sum multiplicities), energy q^2/S and true surplus log(S)/2.
Degrees/windows are original d10/20/32 and N20/40/64; radial costs are19m/10,39m/20,63m/32 with TOTAL m.
The original fixed inputs are not a sequence tending to measure zero.

<a id="unit-cap-unrun-quota-handoff"></a>
## Historical preparation boundary

At the original 2026-10-10T13:52 checkpoint, only normalization(1)--(2), the finite comparison domain and its proposed computation protocol had been prepared.
No comparison program or mathematical run existed, and no optimum, positive result or negative result was asserted.
[J79](../computations/programs/Yin_J_G0079/readme.md#unit-cap-unrun-stop) records the then-unexecuted computation state.
The completed argument and actual finite results below supersede that preparation stage without treating an unrun comparison as a mathematical failure.

<a id="unit-cap-bounded-resumption"></a>
## 3. Complete finite certificate interface

The exact correspondence in(1) goes both ways.
Given any normalized real weights w_j>=0 with sum w_j=1, put E_0=sum w_j e_j>0 and v_j=w_j/E_0.
Then e dot v=1, S=1/E_0 and w=v/S.
Since EVERY included residue has absolute full degree-d norm1, I=log q for the original integer auxiliaries F_j, regardless of their contents.
Hence eta>=log2/2 if and only if S>=2.
Conversely every feasible v gives precisely such a bundle, omitting only zero-weight columns.
Therefore a matched exact primal/dual witness proves the global optimum over all real weights on the specified finite family at the true surplus lower target, not merely over rational weights or a sufficient linear relaxation.

For completeness, write H_(lj)=h_(l,j).
For any feasible v and any dual in(2),

    2||Hv||_1 >= 2 y dot Hv
               >= lambda(e dot v)+mu(sum v_j)
               >= lambda+2mu.                         (3)

The first inequality uses |y_l|<=1, the second all original coordinate slacks, and the last mu>=0 and S>=2.
Thus exact feasibility and equal objectives are sufficient, with no theorem about floating convergence, strong duality or candidate recovery as a premise.
Energy positivity bounds every v_j by1/e_j; the existing uniform original-monomial point is feasible.
These facts also rule out interpreting a solver failure as mathematical infeasibility.
We do not require a solver to finish merely because the finite feasible set is nonempty and bounded.

The only compression identifies the mirrored original monomial columns after equality of EVERY energy and lag correlation is checked.
Replacing their two masses by their sum preserves all constraints and the objective; splitting that sum equally lifts any compressed solution back to all original columns.
All admitted residue labels remain separate, even if some give the same energy/correlations or the same unit.
Each dual slack is checked again on every uncompressed column.
Excluded residues remain in the output with both exact filter tests and their complete original coefficients, multipliers, signed norms, contents and costs; they are not premises of an all-lattice exclusion theorem.

Let the certified rational weights have least common denominator M and nonnegative integer multiplicities m_j=Mw_j.
The actual integer aggregate and its complete norm expense are

    A(t)=sum_j m_j F_j(t)t^(N-1)F_j(t^(-1)),
    A_(N-1)=M q^2/S,
    A_(N-1+l)=(M q^2/S)(Hv)_l,
    |product_j Res(P,F_j)^m_j|=q^(dM).             (4)

The signed product is also retained, using every original norm sign and multiplicity parity.
The native factored representation of q^(dM) records its exact base and exponent without expanding an integer whose length may be enormous.
Every positive auxiliary still has its actual coefficient degree at most N-1, content, coefficient height and l1 cost; no primitive polynomial replaces it.
The complete radial expense is (N-1)m(P)/d with TOTAL original m(P), as in Section2.
These fixed d10/20/32 inputs do not supply near-zero-total-measure coverage or a complete list of unit directions with e<=1.

The [author implementation and protocol](../computations/programs/Yin_J_G0079/readme.md#unit-cap-resumed-implementation) use the retained coefficient identities, energies, correlations and norms to propose rational certificates.
Numerical discovery is not a premise of the exact inequalities above.

<a id="unit-cap-actual-first-result"></a>
## 4. First result: two strict unit-only improvements and a rejected last dual

The single prescribed author computation produced the following five exact optimum certificates and a sixth feasible primal with a rejected dual.
Its native report (`mathematics/computations/outputs/Yin_J_G0079/unit-cap-output.json`) remains incomplete overall, preserving every successful preceding stage and the first exact failure.
No different candidate or missing completion stage was supplied afterward.
[J79](../computations/programs/Yin_J_G0079/readme.md#unit-cap-first-author-outcome) retains the actual run, termination facts and reproduction details.

All304 source directions were processed before the six solves.
The exact selector admitted19 of28 P10 residues,23 of58 n18 residues and41 of94 n30 residues; every excluded label remains with its exact tests and full original data.
Thus the original enlarged families have39,63,105 columns, versus20,40,64 baseline columns.
Compressing only proved-equal monomial mirrors gives29,43,73 enlarged variables and10,20,32 baseline variables.
Neither repeated labels nor equal residue columns were silently removed.

| Actual input and family | Original columns | Certified kappa interval | Exact status |
| --- | --- | --- | --- |
| P10 baseline |20|[3.0845,3.0846)|Complete primal/dual optimum|
| P10 enlarged |39|[3.0617,3.0618)|Complete primal/dual optimum; strict improvement|
| n18 baseline |40|[4.0386,4.0387)|Complete primal/dual optimum|
| n18 enlarged |63|[4.0185,4.0186)|Complete primal/dual optimum; strict improvement|
| n30 baseline |64|[4.6211,4.6212)|Complete primal/dual optimum|
| n30 enlarged |105|No optimum certified|Exact primal feasible; reconstructed dual rejected|

All five complete certificates have S=2, hence true surplus EXACTLY log2/2, and zero rational primal/dual gap.
Their complete original slacks, weights, integer multiplicities and aggregates are retained.
The baseline certificates at n18/n30 reproduce the fixed L333 monomial-optimum values; the P10 baseline is now actually optimized, unlike the uniform-only comparison in L348.
These repeated baselines are controls for the changed finite comparison, not new independent derivations of L333.

The exact P10 pair is

    K_base=48507669494542/15726261655503,
    K_unit=3891813173848329936/1271097706518260747,
    K_base-K_unit
      =25888378641843687011871634/1139074313203939238088577209>0.  (5)

The enlarged optimum's positive monomial source indices are4,5,6,7,12,13,14,15, and its only positive residue indices are33,34 (all indices are zero-based in the retained48-column source family).
These are respectively the actual integer seeds

    B_33=-1+t^3+t^5+t^6+t^7,
    B_34=-1-t+t^5+t^6+t^7.

Their signed full degree-ten norms are+1 and-1.
With the unchanged q=26487, their e values are2153/2943 and16787/26487.
F_33 has content3, height9747 and coefficient l1 cost85119; F_34 has content1, height9386 and l1 cost78391.
Both have actual degree19.
The content3 auxiliary remains the original F_33: replacing it by its primitive part without changing the income/energy bookkeeping would invalidate this stated bundle.
The least denominator of the COMPLETE optimized weights is46645787395165532, with all ten positive multiplicities and all zero weights retained.
The radial multiplier is19/10 on the original TOTAL m(P10).
This unit-only optimum differs from L348's smaller sufficient norm-funded optimum, which could spend the norm9 direction and optimized a different admitted family/budget.

For n18 the exact enlarged optimum is

    K_unit=3840771960023991440990053299529082872205493130905163
           /955762962098170303544175821939577961854544878148028.  (6)

The saved positive rational difference from its baseline proves strict improvement.
The positive original monomial indices are0,2,3,5,8,15,18,21,24,31,34,36,37,39; the only positive residue is source57, the old basis17 unit witness from L341, with norm+1, content1 and e=19325311/36887312.
Its full degree-below20 seed is the already retained vector[-36,9,7,41,-5,32,-12,27,-16,24,-18,23,-19,22,-20,21,-20,21,16,48]; its original F has degree39, height7308940 and coefficient l1 cost145959014.
The complete weight denominator is2901958585515666579254885583889461279469456228.
All costs use q=36887312 and radial39/20 on TOTAL m(P).
This proves what the one-direction L341 step did not: the global optimum of the whole prescribed63-column unit family at this exact surplus.
It remains above4 and supplies no uniform varying-input conclusion.

The sixth instance illustrates why exact feasibility is mandatory.
It returned a numerical candidate and both rational active systems had rank11 in11 unknowns, without free-coordinate approximation.
Its original primal masses passed v>=0, e dot v=1 and S=2, so its saved exact objective is a feasible upper bound for that105-column problem.
This is the full extent of its mathematical optimization conclusion.
The reconstructed dual has, at lag9,

    y_9=1250219600952020615518359902017890571723595934078126182947316886673692860099756472755062996000312
        /520463645430827783431694946531536913247130193491482178915911692497465315333918297999572546108191
        >1.                                                     (7)

It therefore fails the box constraint in(2), even though the saved algebraic objective gap is0.
Such equality cannot bypass the missing dual feasibility.
The program stopped at this first exact failure.
No global optimum, equality to the baseline, absence of improvement or failure of unit directions is inferred for n30.
In particular the overall report is not promoted to complete.
Its last status is dual-reconstructed; normalized weights, least multiplicities and aggregate for this failed instance were NOT reached and are not fabricated afterward.
All these fields exist for the five genuinely complete instances.
This failure is distinct from the older n30 norm-funded10000-pivot failure, which is unchanged and was not retried.

<a id="unit-cap-self-check-and-freeze"></a>
## 5. Complete scope, self-check and author freeze

The new finite conclusion is that norm-one, e<=1 directions already retained in the two actual P10/n18 families can strictly improve their genuinely optimized monomial baselines without any nonunit norm subsidy.
The complete two matched pairs prove this at their actual fixed polynomials and original windows.
The third baseline is also exactly optimized; its prescribed enlargement remains uncertified beyond the saved feasible primal.
There is no claim of an optimum over all units, a complete energy ellipsoid, primitive rescaling invariance, a sequence of inputs with total measure tending to zero, or an unrestricted G0001 resolution.

The author self-check covered both directions of the w/v normalization, actual full degree-d norm signs and q^d scale, zero-column omission, all-real finite-weight scope, strict preservation of the common feasible point, every mirror-pair equality and full-column dual inequality, exact rather than approximate filter boundaries, full norm/content/degree/height/multiplicity/aggregate expenses, all five matched optimum certificates, both positive exact differences, and the sixth failure's invalid y_9 despite zero gap.
Source scope is the accepted L318/L341/L344/L348 interfaces and existing BV04 weak-duality attribution; no new source theorem, norm computation, LLL or independently verified float-optimization guarantee is a premise.
Historical unrun and original contributor statements remain above.
The original root contribution is the comparison design; the implementation and mathematical normalization are by joint_boundary_research AI for Yin.

The complete author argument was frozen on2026-10-10T15:21 as D221 Sections1--5, equations(1)--(7), with its costs, limitations, historical preparation boundary and actual finite results.
At that point only the author's self-check had been completed; the separately organized noncontributor review was pending.
The [J79 author record](../computations/programs/Yin_J_G0079/readme.md#unit-cap-first-author-outcome) identifies the inspected program and first native output.
The subsequent complete review is retained below with its original scope and conclusion.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0179_v1.md#6-displayed-results-attribution-corrections-and-final-boundary), with its original inspected scope and relationship.
