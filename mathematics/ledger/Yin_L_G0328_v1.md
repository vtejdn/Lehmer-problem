---
author: Yin
---

# Exact adaptive integer bundles and fixed-surplus rational descent

The complete current mathematical statement and necessary proofs are adopted in [Yin_C_G0596_v2](../claims/Yin_C_G0596_v2.md#decision-complete-current-self-adoption), with [actual whole constructor SELF](../audits/reviews/Yin_R_G0765_v1.md#current-g328-complete-self-finding).
The original mathematical dates, authors, complete arguments, native/source evidence, useful failures, actual freezes and old review/adoption scopes remain below.
Original2026-10-10 pending/active labels describe their historical stage; the current G0001 execution remains paused and unresolved.


Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="adaptive-bundle-fixed-scope"></a>
## Current adopted scope

For the full original residual integer auxiliary family, nonnegative weights admit an exact normalization preserving all resultant income, energy and surplus.
Explicit weak certificates bound the entire real-weight feasible family, and reciprocal reversal gives a lossless pair reduction.
At a differentiable uniform point in N=2d, a rational projected gradient vanishes exactly when equal weights globally minimize coherence on the fixed S=2 slice; otherwise an explicit positive rational step strictly improves it.
Two certified actual H4 counterexamples admit such improvements at unchanged surplus log2/2 and full original costs, with every native field separately reconstructed.
Both improved coherences remain greater than4.
The earlier exact-simplex timeout remains incomplete evidence, not an optimum or obstruction.
No uniform near-one control or unrestricted gap is claimed.

The complete D195 author proof and review follow without abridgment.
Historical pending-review, pending-adoption and stopped-execution handoff sentences are superseded only by this current adoption paragraph.
Heading depths and relative navigation are relocated; all statements, proofs, source boundaries, unsuccessful-test scope and review history are preserved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## Adaptive integral bundles after failure of uniform residual coherence

Date: 2026-10-10.

<a id="adaptive-residue-weight-reuse"></a>
### 1. Exact changed mechanism and retained inputs

H4's actual failure, now fixed in [L326](Yin_L_G0326_v1.md#h4-counterexample-fixed-scope), concerns equal weights on all residual columns at N=2d.
It does not determine the best weights on these SAME actual integer auxiliary polynomials.
The present question keeps the full original income and asks exactly how far rational nonnegative reweighting can improve coherence while preserving at least the original surplus log2/2.
This is a different optimization problem, not replacement of4 by another guessed constant.

The sufficient arithmetic inequality and actual integral residual columns are already proved in [L318](Yin_L_G0318_v1.md#weighted-integral-bundle-bound).
[L321](Yin_L_G0321_v1.md#monomial-residue-complementarity-obstruction) excludes positive-surplus exact complementarity for all monomial-residue bundles on circle-root inputs; approximate adaptive weighting remains within its open scope.
Its radical identity also rules out treating copied blocks as independent evidence.
These precise interfaces, D193's frozen actual counterexample, and the full J79 native matrices were read before this new derivation.
[L136](Yin_L_G0136_v1.md) already uses explicit rational dual certificates in a different constrained coefficient problem; that problem's feasible set and conclusion are not transferred here.
The local BV04 source inspection initially covered only quadratic conjugacy and Schur complements, so a bounded additional weak-duality method attribution was requested.
The inequality below is proved directly and imports neither strong duality nor a solver-correctness theorem.

Let P be any monic irreducible nontorsion integer unit polynomial of ACTUAL degree d, N>d, T=N-1.
Use the full original L318 projection R and one positive integer q clearing R and the kernel multipliers.
For0<=j<N let F_j have coefficient vector q R e_j.
Each F_j is a nonzero integral polynomial with

    F_j(alpha_i)=q alpha_i^j at every original root,
    |Res(P,F_j)|=q^d.                               (1)

Write

    r_j=R_(j,j)>0,
    H_(h,j)=sum_(i=0)^(N-1-h) R_(i,j)R_(i+h,j),
                           1<=h<N,0<=j<N.          (2)

The strict positivity of r_j follows from R^2=R and F_j nonzero: r_j is the squared Euclidean norm of R e_j.
The complete original roots, including nonreal roots, and the actual arithmetic unit are used in(1); q, every original coefficient and all primitive contents remain in the construction.

<a id="adaptive-normalized-primal-dual"></a>
### 2. An exact weight normalization and verifiable dual obstruction

Take any nonnegative rational vector v of length N with

    r dot v=1, S=sum_j v_j>=S0>1.                  (3)

Discard zero coordinates and put w_j=v_j/S on the remaining auxiliaries.
These are positive rational weights summing to1.
Their complete L318 quantities are

    E=q^2/S, I=log q,
    I-log(E)/2=(log S)/2,
    A_h=q^2(Hv)_h/S,
    kappa=2 sum_h |(Hv)_h|.                         (4)

Indeed E_j=q^2 r_j by idempotence, while the individual autocorrelation is q^2 H_(h,j).
Substituting w=v/S gives(4).
Thus the income is retained exactly, and the same constraint S>=2 preserves at least the equal-weight surplus log2/2 at N=2d.
Conversely every nonnegative original weight vector w with positive energy coefficient e=r dot w and e<=1/S0 gives v=w/e, satisfying(3), with the identical kappa and S=1/e.
This is an exact bijection, not a relaxation losing the energy/income condition.

There is therefore a finite rational linear-program description of the best coherence within this auxiliary family: minimize2 sum_h s_h subject to(3), s_h>=(Hv)_h and s_h>=-(Hv)_h.
The choice v_j=1/d is always feasible for S0<=N/d because trace R=d.
Every feasible v_j<=1/r_j, so the v domain is compact; whenever it is nonempty, the continuous objective2||Hv||_1 attains its minimum.
This observation establishes existence only, without importing a rational optimal-vertex or dual-attainment theorem.
The computations below must supply their own exact rational certificates before claiming an optimum.

**Proposition (direct certificate).** Suppose rational y in[-1,1]^(N-1), lambda in Q and rational mu>=0 satisfy EVERY coordinate inequality

    2(H^T y)_j >= lambda r_j+mu, 0<=j<N.            (5)

Then every bundle(3) obeys

    kappa>=lambda+mu S>=lambda+mu S0.              (6)

*Proof.* For each h, |(Hv)_h|>=y_h(Hv)_h.
Sum and use(5) with v_j>=0.
The result is2||Hv||_1>=lambda(r dot v)+mu sum v, which is exactly(6).
The direction of the final inequality uses mu>=0.
No duality/existence theorem is needed.
If a feasible rational v attains lambda+mu S0, this lower certificate and that actual bundle prove its GLOBAL optimum among all real nonnegative weights with the required surplus, including irrational weights.
If the values differ, retain the exact gap; a solver status is not an optimum certificate.

This is a falsifiable constructive sufficient condition for the original arithmetic mechanism: any actually supplied rational v satisfying(3) and2||Hv||_1<=K yields an original integer bundle with surplus at least(log S0)/2, unchanged degree T and all original norm/scale costs.
Uniform S0>1,K and T/d across an actual class would invoke L318's conditional gap.
No such uniform coverage is assumed.
The dual certificate can instead exclude a proposed K on the entire reweighting family at a fixed input; this is stronger than failure of one chosen weight vector.

For reciprocal P there is an exact symmetry reduction.
Let J reverse all N coefficient coordinates.
Reversing a multiple t^jP gives another allowed multiple t^(N-d-1-j)P, so J preserves the kernel space and commutes with its orthogonal projection R.
Thus R e_(N-1-j)=J R e_j, and autocorrelation is invariant under reversal.
Consequently

    r_(N-1-j)=r_j, H_(h,N-1-j)=H_(h,j).             (7)

Averaging v with its reversal preserves S, r dot v and Hv EXACTLY.
At even N one may optimize over N/2 pair masses b_j=v_j+v_(N-1-j) using one representative of each identical H column and r entry, then lift v_j=v_(N-1-j)=b_j/2.
This covers all possible original weights rather than imposing an unproved symmetry ansatz.
The complete output must retain and check the full matrices and full lifted weights.

The rational weight denominator is not an omitted scalar expense.
If the reduced w_j have least common denominator L, the very same average can be represented by L integer-polynomial copies with multiplicities Lw_j.
Each copy keeps q, its own full resultant q^d, degree at most T and full content.
This representation can be large; no uniform bound on L, q, number of copies or bit complexity is claimed.
It changes neither(4) nor the exact weighted income.
Independently making each column primitive while retaining w would change both quantities and is not performed.

<a id="direct-rational-weight-descent"></a>
#### 2.1 A constructive strict-improvement criterion requiring no optimizer

At N=2d let v0=(1/d,...,1/d), so r dot v0=1 and sum v0=2.
Suppose every coordinate a_h=(Hv0)_h is nonzero.
Define the exact rational signed gradient

    g_j=2 sum_h sign(a_h) H_(h,j).

Let B have independent columns spanning the rational vectors1 and r: take B=[1,r] if they are independent, and B=[1] otherwise.
Put

    z=g-B(B^T B)^(-1)B^T g, delta=-z.              (8)

All entries are rational, r dot delta=sum delta=0, and g dot delta=-||z||^2.
If z is nonzero, set tau to the minimum of1 and the following nonempty applicable positive rational ratios:

    v0_j/(2|delta_j|) for delta_j<0,
    |a_h|/(2|(H delta)_h|) for (H delta)_h!=0.       (9)

Then v1=v0+tau delta has every coordinate strictly positive, satisfies the same r dot v1=1 and sum v1=2, and gives

    kappa(v1)=kappa(v0)-tau||z||^2<kappa(v0).       (10)

*Proof.* The projection in(8) is onto the orthogonal complement of both normalization vectors.
Hence its indicated dot products vanish, and projecting g gives g dot delta=-||z||^2.
Nonzero delta with zero sum has a negative coordinate, so the first set of ratios is nonempty.
Every decreasing coordinate of v remains at least half its positive starting value.
The second set bounds each correlation perturbation by half its initial absolute value, so no sign changes.
On this entire segment the absolute-value objective is exactly linear with gradient g.
Formula(10) follows, with a strict rational decrement.
Thus the actual integer bundle changes only its rational positive weights, retaining exactly the surplus log2/2, original q, full norm income and degree/radial expense.
No algorithmic convergence, floating gradient or asymptotic window argument is used.

Conversely, under the same nonzero-correlation premise, z=0 proves that equal weights are already a GLOBAL minimum over all real nonnegative v with r dot v=1 and sum v=2.
For every such v the absolute-value supporting inequality gives kappa(v)>=g dot v.
Since g is then in span{1,r}, this equals g dot v0=kappa(v0).
Together with(10), this is an exact necessary and sufficient criterion for optimality of equal weights on the fixed-surplus slice.
It does not address all S>2 when z=0, nor applies differentiability at a vanishing correlation without a separate subgradient argument.
This construction can be checked directly from the retained actual rational matrices, even if a general linear-program solver fails to finish.

<a id="adaptive-test-and-source-boundary"></a>
### 3. Exact discriminator and source boundary

Root coordinated precisely two fixed actual inputs from L326/J79: selected factors at n18 and n30, their original N=2d windows and surplus mass S0=2.
No third input or longer window is included.
The separate [J79 adaptive declaration](../computations/programs/Yin_J_G0079/readme.md#adaptive-weights-pre-run) was saved before running weights-author.py, with an aggregate180-second outer deadline covering both exact primal and dual searches.
SymPy exact linear programming generates candidates; all reported conclusions require direct rational verification of(3),(5) and all original quantities.
The complete full matrices and lifted weights are retained, including zero entries that are omitted from the positive-weight arithmetic family.
A failed solver or timeout is not a mathematical lower bound or a test of all weights.
There is no automatic fallback experiment or alteration of the old native evidence.

The fresh [BV04 selected weak-duality inspection](../audits/literature/BV04/readme.md#selected-weak-duality-attribution) now resolves the classical method attribution.
Root directly read the retained Boyd--Vandenberghe text at printed215--219, with the exact Section5.1.3 printed216 equation(5.2) and its full proof; visual checking confirmed the nonnegative inequality multiplier convention.
This author read the canonical inspection record.
The source's unrestricted equality multipliers and nonnegative inequality multipliers match lambda and mu in the direct argument.
No strong-duality theorem, simplex correctness, solver termination or existence of matching rational certificates is imported.
The written proof(6) is complete whether the bounded solver succeeds or fails.

For comparison with L321's circle-root obstruction, the same dual arithmetic gives its natural baseline without promising better cancellation.
If zeta is an actual circle root, put y_h=Re(zeta^h).
Each residual polynomial R e_j has value zeta^j at zeta, so its Fourier square gives2 sum_h y_h H_(h,j)=1-r_j.
Thus the real certificate lambda=-1,mu=1 proves kappa>=S-1.
Formula(6)'s proof is valid for real y as well; rationality is required only for the proposed finite exact data format.
At S>=2 the lower bound is1.
This is the old exact-complementarity obstruction expressed in the present dual variables, not a new gap theorem or proof that the bound1 is attained.
Multiple circle roots cannot be replaced by an arbitrarily chosen phase in an alleged exact rational certificate.

<a id="adaptive-complete-outcomes"></a>
### 4. The incomplete optimizer and the complete direct construction

The first declared exact-simplex attempt started2026-10-10T11:23.
It retained the complete n18 input/r/H matrices and exact uniform coherence, then remained in its first primal solver call.
The outer deadline killed that sole worker at180seconds; observed time including kill/cleanup was180.0151932000008seconds.
No primal or dual candidate returned, and n30 was not started in that attempt.
The complete incomplete record (`mathematics/computations/outputs/Yin_J_G0079/weights-output.json`) and [program](../computations/programs/Yin_J_G0079/weights-author.py) remain unchanged.
The report's worker_returncode124 is a supervisor timeout sentinel, not a captured native killed-process status; that metadata limitation is explicitly retained in J79.
No optimum, infeasibility or full-weight obstruction follows from the timeout.
It is a computational failure to resolve the problem within the cap, not evidence against the mathematical normalization or certificate proposition.

Only after root separately coordinated a second finite stage did [direct-author.py](../computations/programs/Yin_J_G0079/direct-author.py) test the explicit construction(8)--(10).
Its domain was exactly the same two actual factors n18,n30, N=2d, one predefined tau per input, aggregate30seconds, with no line search or iteration.
The first and sole direct run started2026-10-10T11:29, Python3.12.14 standard-library Fraction only; both inputs completed in0.5261384999903385seconds at the outer supervisor and3.2142819seconds at the shell.
There was no failed/partial direct run, mathematical rerun or new input.
The complete direct-output.json (`mathematics/computations/outputs/Yin_J_G0079/direct-output.json`) retains both full rational certificates and every scalar/weight/coefficient cost.

For each input every uniform correlation was nonzero, the span{1,r} had rank2, and z was nonzero.
Thus(10) applies with a positive rational decrement.
The entire polynomial input, original q and C, all column contents, full r/H, both span coefficients, every gradient and projected-gradient entry, every positive/sign breakpoint, chosen tau, full v0/v1 and w, all original and new correlations and complete cost fields were saved.
The new correlations were recomputed directly from H v1 as well as checked against a+tau H delta.
All new weights are strictly positive.
No original polynomial has been replaced or made primitive independently.

| Actual selected factor | d | Exact old kappa | Certified new kappa interval | Certified decrement interval | Positive weights |
| --- | --- | --- | --- | --- | --- |
| n18 | 20 | 190272899/46109140 | [4125/1000,4126/1000) | [1/1000,2/1000) | 40 |
| n30 | 32 | 1632569807113/342917914960 | [4734/1000,4735/1000) | [26/1000,27/1000) | 64 |

These are exact rational enclosing intervals computed by integer division, not rounded floating estimates.
The exact new values are respectively

    1511686341158107376658159559155696473
      /366469071103248940541807785491697360,

    1627865201420885514559112250986710807019839397774406211
      /343836159048834716441351378573678498523524527735255360.

The exact squared projected-gradient norms are respectively

    8410394251501974118721138149
      /7593328342273611326053378560,

    42067507191478678320423978749282171379900331
      /21488360577225149968682407828398930636561600,

which are strictly positive, and the positive tau values are retained with every ratio determining their minimum.
These provide actual falsifiable strict-improvement witnesses; they are not merely observations of a solver objective.

Every improved bundle keeps S=2, so E=q^2/2, I=log q and surplus log2/2 EXACTLY.
Its degrees remain at most39 and63 and its full radial charge is respectively39m/20 and63m/32.
The least normalized weight denominators are1351136501083132756154361663080 and32085687593330136834222993533967543498307712, and all resulting positive integral multiplicities are saved.
These large denominators illustrate a real representation cost; the construction promises no bounded weights, common-scalar size or bit complexity.
L318's weighted inequality permits the rational weights directly and does not require counting repeated copies as extra arithmetic income.

Both new values still exceed4.
Hence this single step does not repair the old failed H4 inequality, show an optimal weight choice, or supply a uniform K for a near-one input class.
It does prove that equal weights are NOT even locally optimal on the same exact-surplus slice for two actual H4 counterexamples.
Those inputs are already certified in L326/J79 and retain fixed positive TOTAL measure; n18 has the explicit lower bound log(13/10), and the selected n30 factor has its own actual root in(1,2) with all roots included in m.
No change in their root radii or degree normalization creates near-zero coverage.

<a id="adaptive-full-self-check"></a>
### 5. Complete author self-check and remaining question

The complete original whole author checklist and its actual date precision are retained at [the responsible original SELF finding](../audits/reviews/Yin_R_G0765_v1.md#original-g328-author-self-finding).


This round supplies an explicit rational reweighting mechanism and a necessary/sufficient fixed-surplus optimality test at differentiable uniform points, together with two complete actual improvements.
The solver timeout leaves the GLOBAL best reweighting over S>=2 unresolved on both inputs.
The next mathematical obligation is structurally controlled nontrivial improvement with uniform useful size or an exact full-weight lower obstruction on the intended small-total-m domain, not another unverified uniform constant.

ENTIRE AUTHOR FREEZE at2026-10-10T11:31: Sections1--5 including2.1, equations(1)--(10), both directions of the fixed-surplus optimality criterion, explicit two-input direct construction, the complete retained optimizer timeout and all source/arithmetic/cost boundaries.
The four new J79 program/output artifacts are frozen with their distinct complete versus incomplete scopes.
The complete author body is ready for whole separately organized noncontributor review and all native results for different-method verification; no further author mutation is planned before that review.


POST-FREEZE TERMINOLOGY CORRECTION at 2026-10-10T11:39.
Following the noncontributor review, the sentence after equation(2) now specifies the complete ORIGINAL roots, including nonreal roots, instead of the potentially misleading phrase complete real roots.
The formulas and all-root domain were already correct; no mathematical formula, result, native program or output changed.
This sentence and this explicit correction record are the sole post-freeze author changes.
The complete author body is refrozen at this time for completion of the whole review.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0153_v1.md#complete-separate-noncontributor-review), with its original inspected scope and relationship.
