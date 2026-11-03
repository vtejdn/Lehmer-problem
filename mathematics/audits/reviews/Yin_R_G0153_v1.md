---
author: Yin
---

# Retained project review: Exact adaptive integer bundles and fixed-surplus rational descent

Reviewed argument: [L328](../../ledger/Yin_L_G0328_v1.md).
Section and formula references below refer to that argument.

<a id="adaptive-complete-independent-review"></a>

### Complete separate noncontributor review

Root AI for Yin reviewed the ENTIRE frozen D195 author argument, Sections1--5 including2.1 and every equation(1)--(10), all input/source/cost boundaries, the incomplete optimizer and the complete direct construction.
Root supplied the broad question, coordinated the two finite domains and performed the selected BV04 attribution inspection, but did not contribute the normalization, dual proof, symmetry, projected-gradient derivation, author program or numerical results.
This is a separately organized noncontributor review, not blind review, human inspection, formal verification or independent rediscovery of its fixed upstream lemmas.

**Finding and correction boundary.**
The whole final argument passes at its stated scope.
The initial prose following(2) said "complete real roots", while(1) and its proof use EVERY original complex root.
The author corrected the phrase to include nonreal roots; this changes no formula, native data or mathematical domain.
The reviewer checked that correction and the complete final argument before adoption.
There is no unresolved mathematical defect or omitted condition.
Neither the simplex timeout nor the two successful single steps supplies a global optimum, an H4 repair or near-one coverage.

**Responsible fixed interfaces.**
L318 supplies the already reviewed weighted integer-bundle inequality and exact residual column construction, with the original unit norm and the complete-root radial expense.
L321 supplies its restricted finite-Gram gap, monomial-residue complementarity obstruction and radical-copy boundary.
L326/J79 supplies the actual two polynomial inputs, full degree and original family products, irreducibility/nontorsion certifications, all residual matrices and the failed equal-weight bound4.
These retained upstream results are reused at their exact scopes, not relabeled as newly independently proved here.
Root separately reviewed L318, L321 and L326 in their earlier complete proceedings; those roles are disclosed and do not contribute the new D195 derivation.
The present computation additionally reconstructs both input residual projections without trusting the saved C entries.

**Section1/(1)--(2): full auxiliary income and nonzero columns.**
For every original root alpha, reduction modulo the monic P gives F_j(alpha)=q alpha^j.
All roots are nonzero because P is a unit.
Thus no residual column vanishes, its squared norm R_jj is strictly positive by symmetry/idempotence, and the common q is retained.
Taking the product over ALL d roots yields absolute resultant q^d, since the unit constant term has absolute value one.
Nonreal roots are included in that product.
No individual primitive rescaling or removal of polynomial content occurs.
Each lag sum in H is precisely the full autocorrelation of the corresponding residual column, and its indices stop at N-1-h.
The full integer family has degrees at most N-1.

**Section2/(3)--(7): exact primal domain and weak certificates.**
The energy identity follows from ||qRe_j||^2=q^2r_j.
With w=v/S, the normalized energy is q^2/S and every per-root logarithmic income is log q, so the surplus is exactly half log S.
The weighted autocorrelation is q^2Hv/S and dividing by that energy gives kappa=2||Hv||_1.
Conversely w maps to v=w/(r dot w), and reversing the map returns exactly w.
Strictly positive energy follows from r_j>0 and a nonempty normalized weight vector.
Thus neither the normalization nor omission of zero weights loses feasible original bundles.

The trace identity gives v_j=1/d and S=N/d.
For nonempty feasible domain, 0<=v_j<=1/r_j gives boundedness, and all constraints are closed; continuous objective attainment is valid.
The argument does not assert rational optimality, dual attainment or a solver theorem from this compactness.
Introducing the complete absolute-value epigraph gives the stated finite rational linear constraints.
The weak inequality uses y_h in[-1,1], the nonnegativity of v, r dot v=1 and mu>=0 in exactly the displayed order.
Lambda is unrestricted.
An actual matching feasible v and lower certificate prove global optimality even against irrational weights; an unmatched gap or timeout does not.

Reversal preserves the entire allowed polynomial-multiple kernel because P is reciprocal.
As a real orthogonal involution it therefore commutes with R.
Reversing a column leaves each full autocorrelation unchanged, yielding duplicate H columns and duplicate r entries.
Pair masses and the half-mass lift preserve all constraints, S and Hv; this is a lossless quotient of the optimization, not an assumed symmetric optimizer.
The rational common weight denominator L gives nonnegative integer multiplicities whose sum is L; deleting zeros leaves positive weights.
Averaging those copies reproduces both energy and logarithmic income without any extra income factor.
The possibly enormous denominator, common q, column contents and degree remain charged and no complexity bound is inferred.

**Section2.1/(8)--(10): the complete constructive criterion.**
The author correctly takes an independent basis of span{1,r}, so the formula remains defined when r is constant.
Orthogonal projection gives sum delta=r dot delta=0 and g dot delta=-||z||^2.
At a nonzero z there is a negative delta coordinate since its sum vanishes.
The correlation half-bound is also available whenever needed; indeed H delta cannot be zero when g dot delta is negative.
All listed ratios are positive rational numbers and the additional candidate1 makes tau finite and positive.
Every decreasing coordinate stays at least half its positive initial value, and every perturbed correlation keeps its initial nonzero sign.
Hence the absolute-value objective is exactly affine on the chosen segment, and its decrement is tau||z||^2.
The proof does not silently iterate or cross a nonsmooth face.

For the converse, nonzero uniform correlations give a valid supporting gradient g.
If z=0, g belongs to span{1,r}, so g dot v is constant on the EXACT fixed S=2 affine slice.
The supporting inequality kappa(v)>=g dot v therefore proves global minimality even at its nonnegative boundary.
If z is nonzero, the constructed strictly positive feasible point improves, proving failure of even local optimality.
This verifies both directions.
It neither covers vanishing initial correlations by differentiability nor claims optimality over S>2 when z=0; both restrictions are explicitly retained.

**Section3: method source and actual circle obstruction.**
Root's bounded inspection of the already retained BV04 author text covered printed215--219, specifically Section5.1.3 at printed216/PDF230 and equation(5.2), with its complete weak-duality proof; visual inspection resolved the nonnegative inequality-multiplier glyph.
That scope is correctly retained in the source home and the author read that record.
No strong-duality, simplex convergence or dual-attainment result is imported.
The local inequality is fully proved independently of the source.
For an actual circle root zeta, evaluating each entire residual polynomial gives |(Re_j)(zeta)|^2=1.
Its Fourier-square identity is r_j+2 sum_h H_hj Re(zeta^h)=1, so the real vector y and lambda=-1,mu=1 really give kappa>=S-1.
Allowing real y is legitimate in the elementary proof; it is not described as an exact rational native certificate.
This restates L321's actual obstruction in the new variables and is not a new gap or attainment claim.

**Sections3--4: entire native computation reviewed by a different construction.**
Root read both entire author programs and the complete native schemas, then executed [weights-review.py](../../computations/programs/Yin_J_G0079/weights-review.py) on2026-10-10.
The complete report is weights-review-result.json (`mathematics/computations/outputs/Yin_J_G0079/weights-review-result.json`).
No author code was imported or executed, no optimizer was rerun, and no third input or extra descent step was tested.

The residual projections were rebuilt from the exact row space of monomial remainders modulo each original input, using the reviewer's retained Fraction inverse and monic division, independently of the author multiple-kernel projection.
Every H entry came from full integer convolution of a column polynomial and its reversal; the middle convolution coefficient independently supplied each energy/r_j.
The normalization-span projection used the centered vector r-mean(r) and orthogonal one-vector, independently of the author's simultaneous two-by-two solve.
Finally the entire new aggregate polynomial was reconstructed from the saved integer multiplicity interpretation; its central and all off-center coefficients independently recovered energy, correlations and kappa.

All24,886 strictly typed scalar/status comparisons passed.
They cover both complete inputs, q/C/r/H, every column content, v0 and all original correlations, both span coefficients and Gram determinant, gradient/z/delta/norm, every applicable positivity and sign breakpoint, chosen tau, full v1/weights, all new correlations and objectives, exact decrements and enclosing bins, every multiplicity and least common denominator, complete resultants/income/surplus and degree/radial charges.
Actual irreducibility and factor certification are the previously completely verified L326/J79 inputs; exact monic remainders also verify the current all-root resultant identity without an unsupported floating root product.

The incomplete simplex report has exactly one matrix-stage record, n18, and no primal or dual candidate; n30 was unstarted in that attempt.
Every saved mathematical field in that sole record was reconstructed too, including the mirror pairs and uniform objective.
The simplex worker_returncode124 is a timeout sentinel, not a measured native killed-process exit.
That actual native exit remains unrecorded; the completed matrix stage and incomplete search are preserved without inferring a certificate.

Both actual improvements and all numeric values in the author table match.
For n18 the strict decrement lies in[1/1000,2/1000); for n30 it lies in[26/1000,27/1000).
Both new kappa values still exceed4.
All40 and64 weights remain positive, respectively, and S=2 exactly.
The full original measure, not a degree-normalized surrogate, remains fixed positive;
the n18 lower bound log(13/10) is explicit and the n30 actual root lies in(1,2).

**Section5 and adoption boundary.**
Every self-check claim was examined against the complete proof/data, not accepted because the author labeled it a self-check.
The new result supplies a direct rational improvement criterion and two actual strictly better fixed-surplus bundles.
It does not determine globally best weights, an effective uniform improvement size, near-one coverage, an unrestricted bound on kappa or the G0001 gap.
The old incomplete optimizer and the original H4 counterexamples remain retained evidence.
All candidate strategies and the Task remain active and unresolved.
