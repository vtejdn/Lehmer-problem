---
author: Yin
---

# Exact actual residual-projection coherence discriminator

## Question and scope

This J retains finite residual-projection calculations, exact auxiliary-bundle certificates and their separate computation checks.
The responsible arguments are [C592v2 Gram proof](../../../claims/Yin_C_G0592_v2.md#residual-laurent-square-identity), [C592v2 actual H4 proof](../../../claims/Yin_C_G0592_v2.md#h4-actual-counterexample), [C596v2 adaptive proof](../../../claims/Yin_C_G0596_v2.md#statement), [C294](../../../claims/Yin_C_G0294_v1.md#statement), [C312](../../../claims/Yin_C_G0312_v1.md#statement), [C322](../../../claims/Yin_C_G0322_v1.md#statement), [C325v2](../../../claims/Yin_C_G0325_v2.md#statement), [C338](../../../claims/Yin_C_G0338_v1.md#statement), [L347](../../../ledger/Yin_L_G0347_v1.md), [L348](../../../ledger/Yin_L_G0348_v1.md), [L351](../../../ledger/Yin_L_G0351_v1.md) and [L355](../../../ledger/Yin_L_G0355_v1.md).
All results below concern their stated original inputs, windows and direction families.
Complete matrices, coefficients, rational witnesses, useful partial results and failed checks remain in the linked native output.
No computation here establishes a uniform near-one estimate or the unrestricted G0001 gap.

## Files

Programs and helpers are in this directory; generated evidence is in `mathematics/computations/outputs/Yin_J_G0079/`.
The table identifies the actual stage inputs and outputs; earlier output used by another stage remains a necessary input.

| Stage | Author program and output | Separate checker and output | Required earlier data |
| --- | --- | --- | --- |
| Fifteen-input pilot | [author.py](author.py), author-output.json (`mathematics/computations/outputs/Yin_J_G0079/author-output.json`) | [review_independent.py](review_independent.py), review-result.json (`mathematics/computations/outputs/Yin_J_G0079/review-result.json`) | Fixed coefficients in the programs |
| Reciprocal family | [family-author.py](family-author.py), family-output.json (`mathematics/computations/outputs/Yin_J_G0079/family-output.json`) | [family-review.py](family-review.py), family-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/family-review-result.json`) | Fixed family formula |
| Incomplete exact simplex | [weights-author.py](weights-author.py), weights-output.json (`mathematics/computations/outputs/Yin_J_G0079/weights-output.json`) | [weights-review.py](weights-review.py), weights-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/weights-review-result.json`) | Family output; the checker also reads the direct-step output |
| One direct weight step | [direct-author.py](direct-author.py), direct-output.json (`mathematics/computations/outputs/Yin_J_G0079/direct-output.json`) | The same adaptive checker | Family output |
| Exact monomial optima | [fast-optimum.py](fast-optimum.py), fast-optimum-result.json (`mathematics/computations/outputs/Yin_J_G0079/fast-optimum-result.json`) | [fast-optimum-review.py](fast-optimum-review.py), fast-optimum-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/fast-optimum-review-result.json`) | Family output |
| 600 nonmonomial directions | [nonmonomial-author.py](nonmonomial-author.py), nonmonomial-output.json (`mathematics/computations/outputs/Yin_J_G0079/nonmonomial-output.json`) | [nonmonomial-norm-review.py](nonmonomial-norm-review.py), nonmonomial-norm-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/nonmonomial-norm-review-result.json`) | Exact monomial optima; the checker covers both 600-direction passes |
| Norm-funded steps | [norm-funded-author.py](norm-funded-author.py), norm-funded-output.json (`mathematics/computations/outputs/Yin_J_G0079/norm-funded-output.json`) | The same two-pass checker | All 600 nonmonomial records |
| Residual-lattice directions | [residual-lattice-author.py](residual-lattice-author.py), residual-lattice-output.json (`mathematics/computations/outputs/Yin_J_G0079/residual-lattice-output.json`) | [residual-lattice-review.py](residual-lattice-review.py), residual-lattice-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/residual-lattice-review-result.json`) | Exact monomial optima |
| Joint linear budget | [joint-budget-author.py](joint-budget-author.py), joint-budget-output.json (`mathematics/computations/outputs/Yin_J_G0079/joint-budget-output.json`) | [joint-budget-review.py](joint-budget-review.py), joint-budget-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/joint-budget-review-result.json`) | Monomial optima and residual-lattice output |
| Signed-power classification | [power-classification-author.py](power-classification-author.py), power-classification-output.json (`mathematics/computations/outputs/Yin_J_G0079/power-classification-output.json`) | [power-classification-review.py](power-classification-review.py), power-classification-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/power-classification-review-result.json`) | Residual-lattice output |
| Nonlinear 32-cell lower bound | [nonlinear-bound-author.py](nonlinear-bound-author.py), nonlinear-bound-output.json (`mathematics/computations/outputs/Yin_J_G0079/nonlinear-bound-output.json`) | [nonlinear-bound-review.py](nonlinear-bound-review.py), nonlinear-bound-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/nonlinear-bound-review-result.json`) | Completed n18 part of joint-budget output |
| Original Lehmer bundle | [lehmer-bundle-author.py](lehmer-bundle-author.py), lehmer-bundle-output.json (`mathematics/computations/outputs/Yin_J_G0079/lehmer-bundle-output.json`) | [lehmer-bundle-review.py](lehmer-bundle-review.py), lehmer-bundle-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/lehmer-bundle-review-result.json`) | Fixed original polynomial |
| Exact budget release | [budget-release-author.py](budget-release-author.py), budget-release-output.json (`mathematics/computations/outputs/Yin_J_G0079/budget-release-output.json`) | [budget-release-review.py](budget-release-review.py), budget-release-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/budget-release-review-result.json`) | Completed n18 joint-budget certificate |
| Norm-one energy-cap comparison | [unit-cap-author.py](unit-cap-author.py), unit-cap-output.json (`mathematics/computations/outputs/Yin_J_G0079/unit-cap-output.json`) | [unit-cap-review.py](unit-cap-review.py), unit-cap-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/unit-cap-review-result.json`) | Residual-lattice, monomial-optimum and Lehmer-bundle outputs |
| Sixth-instance exact remainder | No replacement author output | [unit-cap-remainder-review.py](unit-cap-remainder-review.py), unit-cap-remainder-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/unit-cap-remainder-review-result.json`) | Unit-cap author data and the actual failed first review report |

## Reproduction

Use the programs in their existing homes, with the standard library and the actual SymPy/NumPy dependencies.
Follow the [computation tool-selection guidance](../../../../framework/rules/computations.md#computation-tool-selection) when preparing those dependencies.
Exact certificates use integers and rational numbers; floating tableau tolerances select or inspect candidates and do not certify rational feasibility or optimality.
Programs resolve their default data home from the actual repository/J location, independently of the caller's directory.
Do not reproduce by copying programs and inputs to a new per-run directory.

From the repository root, a selected stage is invoked as, for example:

```powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0079/family-author.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0079/family-review.py
```

Generate or explicitly obtain the required earlier data before a stage or checker.
A clone may lack this ignored output; absence does not trigger a producer or establish that a promised input was obtained.
Some programs refuse an existing result: for an authorized reproduction, remove only the selected replaceable output after preserving necessary evidence and its consumers, then run the same program.
Keep distinct author, independent-review and failed/remainder reports.
An explicit `--output` option, where supported, uses the responsible J output home.
The unit-cap example below shows the exact dependency-preserving procedure.

Guarded author helper reuse is explicit: residual-lattice uses the exact algebra/log helpers of nonmonomial/norm-funded programs;
joint-budget, Lehmer-bundle and unit-cap reuse the tableau/exact-reconstruction helpers in fast-optimum.py and the stated division/log helpers.
Budget release uses only the exact solve/scalar helpers, never the tableau worker.
Importing helpers does not execute an earlier main program or write its output.
Independent checkers disclose their separate reviewer-helper reuse in the stage accounts below.

Live aggregate deadlines remain part of bounded execution: pilot 120 seconds; family author/reviewer 180/240;
adaptive simplex/direct step/adaptive review 180/30/120; fast optimum author/reviewer 120/180;
each nonmonomial author pass 120 and combined review 180; residual-lattice and joint-budget author/reviewer 180;
signed-power, nonlinear-bound and budget-release author/reviewer 30; Lehmer-bundle and unit-cap author/reviewer 180;
unit-cap remainder 30.
A timeout or failed check retains only its actual completed scope.
Incremental or atomic data publication does not turn an incomplete record into a complete certificate.

## Results and limits

<a id="independent-complete-domain"></a>
<a id="complete-independent-computation-review"></a>
### Fifteen-input pilot and complete separate check

The pilot uses N=2d for six actual nontorsion inputs and nine calibration controls.
The actual inputs are t^2-3t+1, t^4-t^3-t^2-t+1, t^6-t^5-t^3-t+1, the original Lehmer polynomial P10, P10(t^2) and P10(t^4).
The quadratic has discriminant 5 and expanding root (3+sqrt5)/2;
the other bases use [C515](../../../claims/Yin_C_G0515_v1.md#small-measure-norm-moment-controls), and the lifts use [Complete prime-power irreducibility](../../../claims/Yin_C_G0481_v1.md#minimal-frobenius-p-power-irreducibility).
The dyadic lifts retain the base's fixed total Mahler measure, not its divided-by-degree height.
The calibration inputs are Phi_p for p=3,5,7,11,17 and (t-1)^d for d=2,4,8,12; torsion and repeated-root cases are outside the irreducible nontorsion domain.

The author retains the complete least-denominator matrices C=qR and U with C+A U=qI, symmetry, C^2=qC, trace C=qd, all signed diagonal sums and both endpoint diagonals.
The rational log2 lower bound is 2 sum_(k=0)^19 1/[3^(2k+1)(2k+1)]; add 2/[3^41*41*(1-1/9)] for its upper bound.
This follows by integrating the geometric derivative of log[(1+x)/(1-x)] at x=1/3 and bounding the tail denominators below by 41.
Every retained comparison was decided at this fixed precision.

| Input | Exact kappa | kappa<=2 | kappa<=1+log2 |
| --- | --- | --- | --- |
| quadratic | 16/17 | yes | yes |
| quartic | 176/119 | yes | yes |
| sextic | 227/114 | yes | no |
| Lehmer | 443186/132435 | no | no |
| Lehmer square substitution | 443186/132435 | no | no |
| Lehmer fourth substitution | 443186/132435 | no | no |
| cyclotomic3 | 8/5 | yes | yes |
| cyclotomic5 | 29/14 | no | no |
| cyclotomic7 | 62/27 | no | no |
| cyclotomic11 | 164/65 | no | no |
| cyclotomic17 | 407/152 | no | no |
| repeated2 | 7/5 | yes | yes |
| repeated4 | 5/3 | yes | yes |
| repeated8 | 70209/37145 | yes | no |
| repeated12 | 205851/103385 | yes | no |

The coordinating reviewer contributed neither the pilot program nor its derivation.
The separate standard-library checker constructs the quotient-remainder matrix B and R=B^T(BB^T)^(-1)B, using its own Fraction elimination instead of the author's coefficient-multiple complement.
Its first d remainder columns are the identity; monic division identifies the kernel with the full coefficient-multiple space.
Descending exact division reconstructs every U column and establishes that the least denominator of R also clears U.
All fifteen complete matrices, identities, scalar fields and comparisons matched.
The admissible Lehmer and sextic inputs refute the two proposed bounds respectively;
calibrations and repeated dyadic copies supply neither further admissible counterexamples nor a replacement uniform constant.

<a id="reciprocal-family-declaration"></a>
<a id="reciprocal-family-author-outcome"></a>
<a id="reciprocal-family-complete-review-declaration"></a>
<a id="reciprocal-family-complete-independent-review"></a>
### Reciprocal family and actual H4 failures

The family is exactly P_n=t^n(t^3-t-1)+(1-t^2-t^3), n=4,...,32.
Complete integer factorizations are recomposed, and a reciprocal factor F is selected by F(1)F(2)<0.
Irreducibility attempts use only primes 2,3,5,7,11,13,17,19,23,29,31.
The direct finite-field method retains complete Frobenius/gcd/Bezout witnesses;
its trace alternative constructs F=t^r Q(t+t^-1), uses the same primes and adjacent quarter-grid points a/4 with -8<=a<=8.
Absence of a modular certificate is not reducibility, and symbolic factorization alone is not the accepted oracle.

All 29 selected full projection records completed.
Twenty-seven factors were certified; n25 and n26 remain conditional and are excluded from actual H4 counterexamples.
H4 fails at the eleven certified indices n18,19,20,22,24,27,28,29,30,31,32.
The first witness is F=P_18/(t+1), degree 20, irreducible modulo 2, N=40, q=36887312, kappa=190272899/46109140>4 and theta=253/19.
The n4 factor reuses the earlier sextic.
The full six-term polynomial supplies m(F)<=log(sqrt6), without a near-zero assertion.

The noncontributing coordinating reviewer rebuilt all 29 projections from monomial-remainder row spaces, recovered U by monic division, used separate dense finite-field routines and checked every native Bezout identity.
Trace polynomials were obtained by binomial Laurent inversion; every quarter-grid value, factor product, conditional exclusion and H4 decision matched.
The actual method attribution and proof boundary are retained in [L326](../../../ledger/Yin_L_G0326_v1.md), [R151](../../../audits/reviews/Yin_R_G0151_v1.md#h4-counterexample-complete-independent-review) and [Hir06's inspected interface](../../../audits/literature/Hir06/readme.md#reciprocal-sequence-method-attribution).

<a id="adaptive-weights-pre-run"></a>
<a id="adaptive-weights-timeout"></a>
<a id="direct-weights-pre-run"></a>
<a id="direct-weights-author-outcome"></a>
<a id="adaptive-complete-review-declaration"></a>
<a id="adaptive-complete-independent-review"></a>
### Incomplete simplex and one direct rational step

Both stages use only the certified n18/n30 family factors at N=2d.
Set r_j=R_jj and H_hj=sum_i R_ij R_(i+h),j.
The exact primal minimizes 2||Hv||_1 subject to v>=0, r dot v=1 and sum v>=2;
mirror-pair compression is lossless, and the dual has y in [-1,1], mu>=0 and 2H^T y>=lambda r+mu, with objective lambda+2mu.
All original normalization, denominator, resultant and radial costs remain in the evidence.

The exact-simplex attempt completed only n18's input/r/H/pair matrices and uniform coherence before the 180-second deadline interrupted its first primal solve.
The n30 stage never began.
`weights-output.json` remains incomplete/OuterDeadline and supplies no primal/dual candidate, optimum, infeasibility result or improvement.
Its worker_returncode=124 is the supervisor's timeout sentinel; the actual killed-process exit code was not retained.
This limitation does not change the completed mathematical matrix stage.

The direct stage instead takes the rational uniform gradient, projects perpendicular to 1 and r, and uses one prescribed step bounded by 1 and all half-positivity/half-sign breakpoints.
It performs no iterative optimization or line search.
Both projected gradients are nonzero, no zero-correlation exception occurs, and all 40/64 new weights are positive.
For n18, kappa=1511686341158107376658159559155696473/366469071103248940541807785491697360 lies in [4.125,4.126), with strict decrement 52396261457783680996449236483673/33315370100295358231073435044699760 and least denominator 1351136501083132756154361663080.
For n30, kappa=1627865201420885514559112250986710807019839397774406211/343836159048834716441351378573678498523524527735255360 lies in [4.734,4.735), with decrement 9076198745706944090179280606377902437493684155604897/343836159048834716441351378573678498523524527735255360 and least denominator 32085687593330136834222993533967543498307712.
Both remain above 4 at unchanged surplus log2/2.

The noncontributing coordinator had supplied the broad adaptive question, finite-domain coordination and BV04 source inspection; this was a nonblind review.
The checker rebuilt both quotient-space projections and full polynomial autocorrelations, and used centered orthogonal normalization projection instead of the author's two-by-two solve.
It checked every completed direct-step field and the simplex's matrix-only scope without rerunning the optimizer.
The mathematical finding is [R153](../../../audits/reviews/Yin_R_G0153_v1.md#adaptive-complete-independent-review).

<a id="fast-exact-optimum-declaration"></a>
<a id="fast-exact-optimum-author-outcome"></a>
<a id="fast-optimum-independent-review-declaration"></a>
<a id="fast-optimum-complete-independent-review"></a>
### Exact monomial optima and full optimal faces

The complete current statement and proof are [C294](../../../claims/Yin_C_G0294_v1.md#argument), with the exact original input/family/window and all real-weight faces/costs retained.
The original R158 whole relationship remains unknown at its disclosed shared-context scope; its separate implementation and original run are distinct retained facts.

The two n18/n30 problems use S>=2 and one floating tableau candidate followed by one rational active reconstruction each.
Candidate settings are reduced-cost tolerance 1e-9, active-selection tolerance 1e-7, ratio tie 1e-10, at most 10000 pivots per input and denominator cap 10^6 for a free coordinate if needed.
These are discovery settings; all feasibility, complementarity and objective equality are checked exactly.
Both recovered systems are square and full rank, of sizes 8 and 10, with no free-coordinate rationalization used.
Their exact primal/dual gaps are zero, and the global monomial optima lie in [4.038,4.039) and [4.621,4.622).
Neither family repairs the bound 4.

Optimal pair supports are {0,2,5,7,8,9,15,18} and {0,1,2,4,5,7,23,24,27,30};
required zero lags are {2,8,31,32,33,36} and {1,2,8,21,23,56,60,62}.
Strict slacks/interior signs and invertible active matrices give unique pair masses, while arbitrary mirror splits give the complete 8- or 10-dimensional interval-product faces.
The proof-defined conditioning and stability constants remain input dependent.
All original q, norms, contents, weights, integer aggregate polynomials and degree/radial expenses are retained.

The reviewer authored upstream family/normalization/descent work, but contributed no optimum/face/stability derivation, candidate or program step to this stage.
The nonblind review rebuilt projections with quotient rows and fraction-free inversion, autocorrelations by polynomial convolution, and active solutions with Bareiss determinants/adjugates.
It checked all exact fields, full face matrices and proof-defined constants without author imports or an LP rerun.
The saved floating equations were separately checked at relative tolerance 2e-6 normalized by 1+absolute reference value;
maximum residuals were 1.2787250425194685e-10 and 5.200817554396053e-10.
Those observations are not exact-optimality premises.
See [R158](../../../audits/reviews/Yin_R_G0158_v1.md#exact-optimum-complete-independent-review).

<a id="nonmonomial-escape-pre-run"></a>
<a id="nonmonomial-escape-author-outcome"></a>
<a id="norm-funded-residue-pre-run"></a>
<a id="norm-funded-residue-author-outcome"></a>
<a id="nonmonomial-norm-independent-review-declaration"></a>
<a id="nonmonomial-norm-complete-independent-review"></a>
### Two complete 600-direction passes

The entire current residue/active-step proof and both distinct finite exclusions are [C312](../../../claims/Yin_C_G0312_v1.md#statement), adopted with [R551 whole independent proof/native finding](../../../audits/reviews/Yin_R_G0551_v1.md#nonmonomial-residues-whole).
The2026-10-21 read-only replay checks all1200 complete records and reports1402243 scalar fields versus saved1402245, with all mathematical and other report fields equal.
The original R164 arrangement remains unknown; its old tally and historical run statements are preserved rather than relabelled or reproduced by assertion.

The exact directions are B=t^j(1+s t^h), h=1,2,3, s=-1,+1 and 0<=j<N-h: 228 at n18 and 372 at n30.
Increasing (n,h,s,j) resolves ties; there is one prescribed step per seed and no iterative optimization.
Each record retains complete B, F=qRB, integral kernel multiplier, content/primitive data, signed full resultants, energies, correlations, active derivatives, every bound/tie, weights/multiplicities and original income/degree/radial costs.
The first step preserves S=2, energy 1 and every old zero correlation.
All 600 old reduced costs are nonnegative; neither input has a strict improvement or kappa<=4.
This yields the stated enlarged finite-family dual obstruction at S>=2, not an optimum on the nonlinear full-income domain allowing S<2.

The second pass uses 32 positive atanh terms, term floor/ceil grid 2^-32, D=2^k t with 1<=t<2 and x=(t-1)/(t+1).
The shared tail is bounded by 9/(260*3^65)<2^-32; one upper grid unit is added after summing ceilings.
Divided-by-d log bounds are rounded on grid 2^-20; D=1 has exact zero bounds.
With lower bound ell, the active right-hand side is (1+2ell,e_B,h_B,Z), and the endpoint also respects caps 1 and 1/(2ell) when ell>0.
It gives 1<=S=2-2ell tau<=2 and actual surplus at least log2/2 under the complete interval argument in [C312](../../../claims/Yin_C_G0312_v1.md#norm-funded-residue-step).
All 600 exact-log slopes are certified nonnegative, with no negative or undecided case, no strict endpoint improvement and no kappa<=4.
Absolute residue norms are {1,9,19} and {1,9,31}.

The separate reviewer imported no author implementation.
It reconstructed quotient Gram projections, integer multiplication-matrix norms and fraction-free determinants, full kernel identities and actual weighted polynomial energy/correlations;
integer-power/division and exact remainder bounds reconstructed the log certificates.
Every one of the 1,200 complete records matched.
The reviewer-method reuse and whole-proof boundary are disclosed in [R164](../../../audits/reviews/Yin_R_G0164_v1.md#nonmonomial-norm-complete-independent-review).

<a id="residual-lattice-pre-run"></a>
<a id="residual-lattice-author-outcome"></a>
<a id="residual-lattice-independent-declaration"></a>
<a id="residual-lattice-complete-independent-review"></a>
### Residual-lattice directions

The current complete lattice, Schur and finite-direction proof is [C322](../../../claims/Yin_C_G0322_v1.md#statement), adopted through [R554 whole independent inspection](../../../audits/reviews/Yin_R_G0554_v1.md#whole-c323).
Its fresh fixed-verifier replay covered every152label/304step and full schema, while original R166 dates/context and native run history remain separate.

For n18/n30, X is the complete remainder map with first d columns I_d, L is the first d columns of C, C=LX and XL=qI.
The program retains Q=XX^T, det Q and the complete rational pullback K=q^-2 L^T(2 sum y_h J_h-lambda I)L.
The leading-pivot procedure would retain its first nonpositive-pivot witness and remaining couplings, including zero pivot with nonzero coupling;
both actual K matrices instead have complete strictly positive rational decompositions.
This proves positive definiteness, not an integer minimum.

Each input uses one `Matrix.lll_transform(delta=Rational(3,4))` on the rows L^T, saving the full integral transformation, inverse and determinant -1.
The candidate list consists only of basis rows and both signed adjacent-row sums: 58+94=152 labelled directions, without deduplication.
No extra Schur witness occurred.
Every original multiplication matrix, signed norm, residual/multiplier/primitive vector, log certificate and both conservative/norm-funded endpoint payloads is retained.
The author explicitly reuses its earlier exact helpers; this is not independent verification.

Conservative improvement counts are 3/0 and norm-funded counts 9/3 for n18/n30, with no kappa<=4.
Selected indices are 17/0 and 51/27 respectively.
The n18 conservative row17 has norm 1/content 1 and kappa in [4.0283,4.0284);
the n18 norm-funded adjacent-row seed51 has norm 96721/content 1 and kappa in [4.0278,4.0279).
The n30 norm-funded row27 has norm 687965591/content 1 and kappa in [4.5860,4.5861);
its conservative tie is in [4.6211,4.6212).
No unit-group classification or complete lattice search follows.

The structural reviewer authored upstream monomial-optimum work, but none of this stage's lattice/Schur/candidate/improvement proof or code.
The nonblind check used a coefficient-multiple projection, separate sparse remainder recurrence, integer Bareiss Gram determinants, direct positive-factor multiplication and polynomial resultants rather than author norm determinants.
All 152 labels, 304 endpoint steps and 119456 full multiplication-matrix entries were checked, with disclosed reuse of earlier reviewer helpers and no author import or new LLL call.
See [R166](../../../audits/reviews/Yin_R_G0166_v1.md#residual-lattice-complete-independent-review).

<a id="joint-budget-pre-run"></a>
<a id="joint-budget-author-outcome"></a>
<a id="joint-budget-independent-review-declaration"></a>
<a id="joint-budget-complete-independent-review"></a>
### Joint linear budget: one optimum and one incomplete search

The complete [C326v1 isolated inspection](../../../audits/reviews/Yin_R_G0554_v1.md#whole-c326) supports the conditional budget, actual n18 certificate and n30 failure, but records the false arbitrary-family nonemptiness sentence.
The separate [C325v2 correction](../../../claims/Yin_C_G0325_v2.md#statement) retains all native data and actually adopted [R557 fresh complete repaired-chain finding](../../../audits/reviews/Yin_R_G0557_v1.md#complete-repaired-joint-budget).
The earlier [constructor self-check](../../../audits/reviews/Yin_R_G0555_v1.md#feasible-family-repair-self-finding) remains a distinct self-reviewed occurrence; the new reviewer supplied no repair.
The actual two families include the original monomial witnesses; no n30 optimum or arbitrary-family feasibility follows.

The families contain all original monomial columns and the 58/94 labelled residues: 98/158 original coordinates, compressed only across identical mirrored monomial columns to 78/126.
With ell the certified lower norm-log bound and a=1+2ell, substitute u=a v and minimize 2||H'u||_1 under e' dot u=1, u>=0 and sum u>=2.
The sufficient budget is S+2L>=2; it does not equal the full nonlinear constraint.
Root supplied that budget and its elementary logarithmic proof, so is a contributor to this argument.
Candidate tolerances, pivot and rationalization limits are those of the fast-optimum stage.

The n18 problem completed with a full exact primal/dual optimum in [3.7055,3.7056), below 4 and all 116 prior conservative/norm-funded endpoints.
Budget S+2L=2 is tight, 0<S<2, and full norm income certifies the same surplus log2/2.
There are 19 positive original columns, comprising 12 monomials and 7 residues.
All 98 slacks, weights/multiplicities, aggregate coefficients, factored norm product and original expenses remain in the output.

The n30 problem completed all 158 original-direction records and 126-column rational matrices, then reached the 10000-pivot cap during phase 2 before returning a candidate.
Its final numerical tableau, basis and objective and any exact primal/dual reconstruction are absent.
The retained matrices-ready status and failure describe an incomplete search, not infeasibility, lack of improvement or an optimum.
The complete output therefore remains incomplete even though its n18 certificate is usable by the nonlinear-bound and budget-release stages.

The noncontributing orbit reviewer disclosed prior review/helper reuse and rebuilt both full inputs, all 152 signed residue norms and log certificates, and the n18 exact systems by quotient-space/fraction-free methods.
It did not rerun either optimizer or infer missing n30 state.
The n18 floating basis equations had largest residual 5.478923981172557e-10 under the declared absolute 1e-6 tolerance;
exact optimality uses only rational feasibility and equality.
See [R169](../../../audits/reviews/Yin_R_G0169_v1.md#joint-budget-complete-independent-review).

<a id="signed-power-classification-pre-run"></a>
<a id="signed-power-classification-first-outcome"></a>
<a id="signed-power-independent-review-declaration"></a>
<a id="signed-power-complete-independent-review"></a>
### Signed-power classification

For every retained residue label, compare its complete quotient vector with both signs of every alpha^k for -4N<=k<=4N.
The two domains retain 321/513 powers, 834 full vectors, 133680 signed equality decisions and 31 positive-match divisibility identities.
There are 11/58 and 20/94 matched labels, all inside the original monomial windows.
The remaining 47/74 exclusions are bounded-interval statements.
The separate [C338 argument](../../../claims/Yin_C_G0338_v1.md#unit-residue-not-signed-power) proves an all-exponent exclusion for n18 row17 using its norm 1 and P(-1)=19, B(-1)=-391 congruent to 8 modulo 19.
That infinite statement is not inferred from the finite search.

The noncontributing orbit reviewer used independent modular binary exponentiation at each exponent and forward unit-constant division instead of the author's successive companion recurrence and descending division.
All vectors, decisions, quotients and original costs matched, with disclosed reuse of its earlier quotient-Gram/resultant helpers.
The complete original [R170 finding](../../../audits/reviews/Yin_R_G0170_v1.md#signed-power-complete-independent-review) remains an actual historical check with unknown initial substantive context.
The [R559 whole self-review](../../../audits/reviews/Yin_R_G0559_v1.md#complete-signed-power-current-finding) covers the entire proof, the original bounded comparison and the separate all-exponent order-unit argument.
The [whole separately arranged R561 finding](../../../audits/reviews/Yin_R_G0561_v1.md#whole-signed-power-isolated-finding) retains its complete mathematical/native check and subsequent whole R170/R559 comparison.
It corrected its relationship to self-reviewed on2026-10-21T10:38 after confirming prior conclusion summaries were read in this J documentation before initial findings.
C338 now selects the adequate complete self findings; the earlier mistaken independent-coverage adoption is historical, and R170 still requires an isolated M04 replacement.
Its stdout-only fixed-domain replay reconstructed all 834 vectors, 133680 signed decisions and 31 quotient identities; every mathematical summary record matched the original saved review.
The current scalar/schema tally is 202735 and the original tally is 202736; these are distinct execution facts, with no asserted cause for the one-count difference.
All six inspected program/native files remained byte-identical across that replay.
Static inspection also corrected the producer input path to the canonical residual-output directory after the layout migration; no producer was run, and no native output changed.
The fresh [isolated complete finding](../../../audits/reviews/Yin_R_G0566_v1.md#isolated-complete-signed-power-finding) has a dedicated [stdout-only checker](power-classification-isolated-review.py).
From the repository root, run `.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0079/power-classification-isolated-review.py --compare-saved`; it reconstructs the original domain and compares the existing saved data under a 30-second cap without writing results.

<a id="nonlinear-bound-pre-run"></a>
<a id="nonlinear-bound-author-outcome"></a>
<a id="nonlinear-bound-independent-declaration"></a>
<a id="nonlinear-bound-complete-independent-review"></a>
### Nonlinear surplus: all 32 mass cells

Only the completed n18 joint-budget certificate and its 98 original directions are used.
On the complete mass interval [A,B]=[1/max e,1/min e], use exactly 32 equal rational cells, without a solver or adaptive refinement.
For cell [a,b], certify beta_upper>=log(b/2), including negative logarithms by the correct numerator/denominator interval subtraction.
Let epsilon=max(ell_upper-ell_lower), t=beta_upper+2epsilon and b_cell=max(a,a-max(t*a,t*b)).
The minimum of lambda+mu*b_cell over all cells, clamped by zero, bounds the full nonlinear-surplus problem on this finite family.
All log certificates, endpoint products, ties, signs and exact costs are retained.

Here A=36887312/60635931, B=36887312/16716775 and epsilon=1/1048576.
Twenty-seven cells have negative t and five positive t; cell0 gives the minimum in [2.5016,2.5017).
The earlier feasible witness gives an upper bound below 3.7056.
Neither endpoint is asserted to be the exact nonlinear optimum, and no all-residue or near-one claim follows.

The structural reviewer contributed none of the tangent argument; root's contribution and the reviewer's upstream authorship/reviews are disclosed in [R172](../../../audits/reviews/Yin_R_G0172_v1.md#full-surplus-complete-independent-review).
Its self-contained checker imported no author/reviewer code, rebuilt all 3822 correlations from full coefficient vectors, and checked 122 log certificates and all 32 cells by separate integer-power/remainder and sign-case methods.
Accepted norm and irreducibility inputs retain their earlier inspection scope.
The complete current theorem and necessary argument are in [C358](../../../claims/Yin_C_G0358_v1.md#statement), with the actual present [whole SELF finding](../../../audits/reviews/Yin_R_G0573_v1.md#full-surplus-whole-current-finding).
R172 retains its recorded author-explanation availability and unknown historical relationship; its actual content/order are unestablished, and the separate checker supplies no proof of isolation.

<a id="lehmer-bundle-pre-run"></a>
<a id="lehmer-bundle-author-outcome"></a>
<a id="lehmer-bundle-independent-review-declaration"></a>
<a id="lehmer-bundle-complete-independent-review"></a>
### Original Lehmer bundle

This stage uses only P10 with ascending coefficients [1,1,0,-1,-1,-1,-1,-1,0,1,1], d=10 and N=20.
The accepted irreducibility and root domain, including beta in (1.17,1.18), are reused from the retained original-Lehmer inputs.
Both quotient and coefficient-multiple projections are computed, with q=26487, det Q=det G=79461 and integral kernel identities.
One basis reduction supplies 28 labelled residues alongside all 20 monomials, giving 48 original directions and 38 compressed variables.
Every full norm matrix, signed resultant, content and exact log/cost field is retained.

Both exact active systems have rank 5 with five unknowns.
The sufficient-budget optimum is 16019300828244880114628/5290823672429397181749, in [3.0277,3.0278), compared with the uniform-only monomial baseline 443186/132435 in [3.3464,3.3465).
The nine positive directions are C_j for j=4,5,6,7,12,13,14,15 and B=t^2+t^4.
The latter has full norm 9, content 1 and normalized energy 31535/26487;
C_7 and C_12 retain content 3 without primitive substitution.
S+2L=2, 0<S<2, and complete norm income certifies surplus log2/2, with degree 19 and radial cost 19/10.
There is no optimized-monomial-only comparison, new threshold crossing or nonlinear/global gap conclusion.

The orbit reviewer contributed none of this derivation and disclosed prior review of the sufficient-budget proof.
It independently rebuilt all 4800 norm-matrix entries and 48 signed resultants, both exact systems, full original weights and 39 aggregate coefficients.
Fraction inverse, integral-companion Horner matrices, polynomial resultants, DomainMatrix reconstruction and convolution provide the different methods, with disclosed reviewer-helper reuse and no author import.
The numerical basis-equation maximum residual 3.928857239543504e-12 was below 1e-6, separately from exact certificate checks.
See [R173](../../../audits/reviews/Yin_R_G0173_v1.md#lehmer-bundle-complete-independent-review).
The complete current theorem and necessary argument are in [C359](../../../claims/Yin_C_G0359_v1.md#statement), with the actual present [whole SELF finding](../../../audits/reviews/Yin_R_G0573_v1.md#lehmer-bundle-whole-current-finding).
R173 retains its recorded author scope/outcome availability and unknown historical relationship; their actual content/order are unestablished, and the original native programs and first-run evidence remain unchanged.

<a id="budget-release-pre-run"></a>
<a id="budget-release-author-outcome"></a>
<a id="budget-release-independent-declaration"></a>
<a id="budget-release-complete-independent-review"></a>
### Exact release of the sufficient budget

This stage uses only completed n18, its same 98 original directions and existing positive support/zero-correlation system.
One rank-13 exact solve with right-hand side (0,-1,0,...,0) preserves energy and zero lags and has slope -mu.
With S0<2 and sigma=sum delta_u/a, use M=(2-S0)^2/4 and D=1+abs(sigma)(2/S0-1).
The sole rational step is the minimum of 1, M/(2D), every mass endpoint and every original nonzero-correlation sign endpoint.
The tangent proof gives actual surplus margin at least (M-tau D)/(2S_new)>0 without a new logarithm calculation.

The limiting mass is compressed coordinate16, so original columns16/23 become zero.
All zero correlations remain zero, other signs persist, energy stays 1, and 17 original labels remain positive.
The exact coherence is in [3.7016,3.7017), with decrease mu*tau>=3916/10^6 and surplus margin at least 13395/10^6 above log2/2.
Budget 2-tau is below 2: the old sufficient-budget optimum is not the full nonlinear optimum.
This supplies a better feasible upper witness, not a new nonlinear optimum.
All 98 weights/multiplicities, 79 aggregate coefficients and complete original norm/window costs remain available.

The noncontributing orbit reviewer disclosed its upstream budget review.
It reconstructed all original polynomials/norms, 3822 lag fields, the rank-13 system by fraction-free inversion and every one of 23 step bounds/ties, using only its disclosed earlier reviewer helper.
No LP, LLL, n30 operation, new direction or numerical discovery replay occurred.
See [R176](../../../audits/reviews/Yin_R_G0176_v1.md#budget-release-complete-independent-review).

<a id="unit-cap-pre-run"></a>
<a id="unit-cap-unrun-stop"></a>
<a id="unit-cap-resumed-implementation"></a>
<a id="unit-cap-first-author-outcome"></a>
### Norm-one energy-capped comparison: five optima and one rejected dual

Root contributed the comparison design.
The domain is only the existing P10/n18/n30 source directions, retaining all original monomials and admitting an old residue exactly when abs(Res(P,B))=1 and ||F||^2/q^2<=1.
The calculation preserves all 304 source columns and every admission/exclusion decision, including rejected coefficients and available norm matrices.
It is not a new ellipsoid enumeration, norm determinant or retry of the older n30 norm-funded problem.
For norm 1, the true surplus constraint is exactly sum v>=2, so this stage does not optimize a nonlinear relaxation.
The six instances are P10 baseline/enlarged, n18 baseline/enlarged and n30 baseline/enlarged, in that order.
Candidate settings are the earlier EPS/ACTIVE/tie/pivot/free-denominator limits; first failure stops later work.

The [mathematical preparation boundary](../../../ledger/Yin_L_G0355_v1.md#unit-cap-unrun-quota-handoff) identifies the initially unexecuted comparison.
That preparation did not establish a mathematical result.

The admitted residues number 19/28, 23/58 and 41/94, giving 39/63/105 original enlarged columns and 29/43/73 compressed columns.
The first five instances have complete exact primal/dual equality, S=2 and true surplus log2/2:

| Input | Baseline kappa interval | Enlarged kappa interval | Exact conclusion |
| --- | --- | --- | --- |
| P10 | [3.0845,3.0846) | [3.0617,3.0618) | Strict improvement |
| n18 | [4.0386,4.0387) | [4.0185,4.0186) | Strict improvement |
| n30 | [4.6211,4.6212) | No certified optimum | Sixth primal is feasible; dual is invalid |

P10's positive added residues are source33/34, with norms +1/-1 and contents 3/1;
n18's positive added residue is source57, norm +1/content 1.
Every completed original weight, denominator, multiplicity, aggregate and radial/primitive cost is retained.

The sixth case has exact rank-11 primal and dual reconstructions with no free coordinates.
Its full 105-coordinate primal is nonnegative, has energy 1 and S=2, and gives only a feasible upper bound.
The dual has nonnegative mu and original slacks but violates its box only at lag9, where the saved rational y is greater than 1.
The algebraic gap zero therefore does not prove optimality.
The overall author report remains incomplete with the actual failed assertion;
normalized weights, multiplicities and aggregate fields from the unreached completion stage remain absent.
No n30 baseline/enlarged comparison or all-six-optima result is fabricated.

<a id="unit-cap-review-pre-run"></a>
<a id="unit-cap-first-review-stop"></a>
<a id="unit-cap-remainder-pre-run"></a>
<a id="unit-cap-review-outcome"></a>
### Failed full review and successful exact remainder

The separately arranged orbit reviewer contributed none of this design, normalization or author implementation.
Prior upstream reviews, coordination summaries and author explanations were available, so this is nonblind review of the present argument.
Its self-contained checker reconstructed complete source projections and retained seeds, all 304 signed norms by polynomial subresultants, full coefficient/multiplier/content/energy/correlation fields and every exact selector.
Exact active systems use normal-equation inversion and full-row checking instead of author Gauss--Jordan reconstruction.
No author module, LLL or simplex was executed.

The first review fully matched the 304-source reconstruction and all five complete certificates, including their full costs.
It then failed on the sixth floating basis-tableau equation A_basis*T=[A|rhs]: scaled residual 2.5781250000651568 exceeded the fixed 1e-6 tolerance.
Other equations at that stage had maximum residual 9.555689572948722e-13.
The first report remains failed; the sixth exact stages and later top-level checks were not reached in that run.
This negative numerical-consistency fact supplies no conclusion about the true enlarged optimum.

The separate remainder check covers only those unexecuted exact stages and the associated complete top-level/comparison fields.
It reads the actual failed first report and reuses its checked 304-source/five-certificate scope, rather than recomputing or relabelling it.
A callback records the original floating inspection as failed; it neither changes the candidate nor raises the tolerance.
Every sixth exact equation and original primal/dual constraint was then checked, confirming the feasible primal, unique lag9 box violation, absent completion-stage fields and no certified optimum.
The remainder report is `passed-remainder-only`, not a replacement whole-run pass.

The original reviewer declaration inaccurately grouped residual-lattice-review.py among its own earlier implementations.
That program was authored by structural_research, with explicit reuse of orbit's earlier serializer/convolution/log helpers.
Orbit read those projection/norm methods and its own joint-budget/Lehmer-bundle checkers before writing the self-contained unit-cap checker;
the remainder imports only that first unit-cap checker.
This actual reviewer-method reuse is disclosed without claiming author-code reuse or unrelated implementation.
The combined mathematical scope and historical correction are owned by [R179](../../../audits/reviews/Yin_R_G0179_v1.md#unit-cap-complete-independent-review).
The inconsistent sixth floating tableau remains negative evidence, while the exact limited conclusions above have been separately checked.

<a id="unit-cap-same-path-reproduction"></a>
## Unit-cap same-path cleanup and reproduction

Preserve the meaningful failed floating-tableau fact and exact remainder scope at [R179](../../../audits/reviews/Yin_R_G0179_v1.md#unit-cap-complete-independent-review).
A previous downstream report does not certify a new author run.

| Operation | Sole replaceable output | Required inputs to retain |
| --- | --- | --- |
| Author | `unit-cap-output.json` | Author program, fast-optimum/nonmonomial helpers, monomial-optimum/residual-lattice/Lehmer-bundle outputs |
| First reviewer | `unit-cap-review-result.json` | First reviewer program, author program/output and those three source JSON files |
| Remainder reviewer | `unit-cap-remainder-review-result.json` | Remainder and first reviewer programs, author program/output, **the actual failed `unit-cap-review-result.json`** |

Select one operation from the repository root after preserving needed evidence and checking actual use of the selected output:

```powershell
$operation = 'remainder' # 'author', 'reviewer' or 'remainder'
$j79Programs = (Resolve-Path -LiteralPath 'mathematics/computations/programs/Yin_J_G0079').Path
$j79Outputs = (Resolve-Path -LiteralPath 'mathematics/computations/outputs/Yin_J_G0079').Path
$selection = switch ($operation) {
    'author' { @('unit-cap-output.json', 'unit-cap-author.py') }
    'reviewer' { @('unit-cap-review-result.json', 'unit-cap-review.py') }
    'remainder' { @('unit-cap-remainder-review-result.json', 'unit-cap-remainder-review.py') }
    default { throw 'Select author, reviewer or remainder' }
}
$target = [IO.Path]::GetFullPath((Join-Path $j79Outputs $selection[0]))
if ([IO.Path]::GetDirectoryName($target) -ne $j79Outputs) { throw 'Output escaped J79' }
if (Test-Path -LiteralPath $target) {
    $item = Get-Item -LiteralPath $target -Force
    if ($item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Expected an ordinary output file' }
    Remove-Item -LiteralPath $target
}
& .venv/Scripts/python.exe -B -X utf8 (Join-Path $j79Programs $selection[1])
if ($LASTEXITCODE -ne 0) { throw 'Inspect the actual failed/incomplete report; do not infer completion or automatically retry' }
```

A full reproduction follows author, first review and only the applicable remainder, in that order.
Inspect actual native status and completed scope after each operation.
The remainder requires the original kind of first failure with its completed source/five-instance checks; another failure or a complete first pass does not satisfy that prerequisite.
Keep both dependency reports when running the remainder alone.
Do not clear a whole J directory, required input/helper, non-reconstructible witness, active output or unrelated report.
An interrupted atomic-write sibling is incomplete evidence to inspect, not a substitute for the required completed input.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.

## Recorded runs

The local output names below identify the particular recorded runs used by the linked fixed materials.
Those records retain the original inputs, parameters, known dates and checked scopes; the existing instructions above identify the programs and reproduction commands.
These links locate the original results and checks, without asserting verification of the present README or a new execution.
Generated output files remain local and are not synchronized.

| Local run output | Original result or check record |
| --- | --- |
| `budget-release-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0584_v1.md#strict-release-isolated-whole-finding) |
| `budget-release-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0579_v1.md#strict-release-whole-current-finding) |
| `family-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0542_v1.md#independent-whole-real-weight-optimum); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#nonmonomial-residues-whole); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0578_v1.md#order-unit-whole-independent-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0584_v1.md#strict-release-isolated-whole-finding) |
| `fast-optimum-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0540_v1.md#current-complete-real-optimum-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0542_v1.md#independent-whole-real-weight-optimum); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#nonmonomial-residues-whole); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0554_v1.md#whole-c323); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0554_v1.md#whole-c326); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0557_v1.md#complete-repaired-joint-budget); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0576_v1.md#isolated-full-surplus-whole); [Claim support and recorded result](../../../claims/Yin_C_G0294_v1.md) |
| `fast-optimum-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0540_v1.md#current-complete-real-optimum-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0542_v1.md#independent-whole-real-weight-optimum); [Claim support and recorded result](../../../claims/Yin_C_G0294_v1.md) |
| `joint-budget-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0554_v1.md#whole-c326); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0557_v1.md#complete-repaired-joint-budget); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0573_v1.md#full-surplus-whole-current-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0576_v1.md#isolated-full-surplus-whole) |
| `lehmer-bundle-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0173_v1.md#lehmer-bundle-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0573_v1.md#lehmer-bundle-whole-current-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0576_v1.md#isolated-lehmer-whole) |
| `lehmer-bundle-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0173_v1.md#lehmer-bundle-complete-independent-review) |
| `nonlinear-bound-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0172_v1.md#full-surplus-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0573_v1.md#full-surplus-whole-current-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0576_v1.md#isolated-full-surplus-whole); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0584_v1.md#strict-release-isolated-whole-finding) |
| `nonlinear-bound-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0172_v1.md#full-surplus-complete-independent-review) |
| `nonmonomial-norm-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#nonmonomial-residues-whole) |
| `nonmonomial-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#nonmonomial-residues-whole) |
| `norm-funded-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0551_v1.md#nonmonomial-residues-whole) |
| `power-classification-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0559_v1.md#complete-signed-power-current-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0561_v1.md#whole-signed-power-isolated-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0566_v1.md#isolated-complete-signed-power-finding) |
| `power-classification-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0566_v1.md#isolated-complete-signed-power-finding) |
| `residual-lattice-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0554_v1.md#whole-c323); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0554_v1.md#whole-c326); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0557_v1.md#complete-repaired-joint-budget); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0559_v1.md#complete-signed-power-current-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0561_v1.md#whole-signed-power-isolated-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0566_v1.md#isolated-complete-signed-power-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0576_v1.md#isolated-full-surplus-whole); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0578_v1.md#order-unit-whole-independent-finding) |
| `unit-cap-output.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0583_v1.md#unit-cap-whole-current-finding) |
| `unit-cap-remainder-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0179_v1.md#unit-cap-complete-independent-review) |
| `unit-cap-review-result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0179_v1.md#unit-cap-complete-independent-review) |
