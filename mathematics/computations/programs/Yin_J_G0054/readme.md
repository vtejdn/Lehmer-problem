---
author: Yin
---

# Unbounded path-basis replacement equations for the prescribed quartic completion

## Question and scope

[C415v2](../../../claims/Yin_C_G0415_v2.md#statement) owns the current complete theorem and proof, with its [actual whole SELF finding](../../../audits/reviews/Yin_R_G0617_v1.md#complete-path-column-whole-self-finding).
The original L250 input, construction failures and original R114 finding remain fixed.
For the ordered path basis Q0 in the L246 conference lattice, replace one column by any integral norm-two vector while retaining a unimodular basis.
The full target Phi6 P4 is excluded at every position and coefficient size by the written congruence proofs.
Arbitrary later orderings, simultaneous multicolumn changes, other lattices and other neutral factors are outside this theorem.

## Files

| Program | Actual output | Scope |
| --- | --- | --- |
| [equations.py](equations.py) | equations.json (`mathematics/computations/outputs/Yin_J_G0054/equations.json`) | Exact norm, first-coefficient and Pfaffian polynomials at columns2 and3, followed by both Pfaffian signs and the smallest-coefficient linear elimination. |
| [residues.py](residues.py) | residues.json (`mathematics/computations/outputs/Yin_J_G0054/residues.json`) | Declared26568 tuples: four systems modulo3 and9, with every survivor retained. Column3 has no mod9 survivors; column2 does. |
| [solve_column.py](solve_column.py) | solve_column.json (`mathematics/computations/outputs/Yin_J_G0054/solve_column.json`) | Declared137842 triples, both signs and three remaining parameters in[-20,20]. Solve the fourth variable without a bound, including all singular linear cases via exact quadratic discriminants. No target found. |
| [two_adic.py](two_adic.py) | two_adic.json (`mathematics/computations/outputs/Yin_J_G0054/two_adic.json`) | Declared8736 tuples: column2 systems modulo2,4,8; also checks all printed general formulas for columns2 and3 symbolically. |
| [other_columns.py](other_columns.py) | other_columns.json (`mathematics/computations/outputs/Yin_J_G0054/other_columns.json`) | Exact equations at the other parity-compatible positions1 and4. Position1 forces a nonintegral coordinate1/5 or4/5; these are exclusions, not accepted bases. |
| [last_column_residues.py](last_column_residues.py) | last_column_residues.json (`mathematics/computations/outputs/Yin_J_G0054/last_column_residues.json`) | Declared13828 tuples: column4 systems modulo2,4,3,9, preserving both vanishing and nonvanishing survivor sets. |
| [verify.py](verify.py) | verification.json (`mathematics/computations/outputs/Yin_J_G0054/verification.json`) | Separate author calculation using plain-integer polynomial subset determinants and Pfaffians, without importing the equation generator:84 full determinant calculations on21 unisolvent quadratic-interpolation points per column;24 actual norm-two endpoint checks; printed column4 formulas and gradient test. |

The actual input seed and path basis are written in the programs and in the responsible fixed proof.
J53 is an unchanged prior comparison, not a writable input.
All mathematical parameters, output lists and ranges are retained; no private input, external root oracle, floating tolerance or incidental byte/hash gate is used.

## Reproduction

The programs require Python and SymPy.
From the repository root, execute in dependency order; each writes its corresponding result in this J output home:

~~~powershell
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0054/equations.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0054/residues.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0054/solve_column.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0054/two_adic.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0054/other_columns.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0054/last_column_residues.py
.venv/Scripts/python.exe mathematics/computations/programs/Yin_J_G0054/verify.py
~~~

Before the first successful equations output, two attempts failed visibly: syntactic symbolic equality did not expand V*Vinv-I; then the eliminator expected a unit coefficient although the actual Pfaffian coefficients were even.
Exact expansion and a general nonzero-coefficient solve repaired them.
The final smallest-magnitude coefficient choice avoids unnecessary denominators for the central columns but deliberately exposes the unavoidable nonintegrality at column1.
Both failures preceded a retained mathematical output; no target was fabricated or lost.
One handwritten generic constant in D117 was corrected during author self-check to match the already correct symbolic output; the printed-equation verifier then passed.
These corrections are not independent-review findings.

## Results and limits

For each Pfaffian sign, column2 has10 and90 survivors modulo3 and9, but only2 modulo2 and none modulo4 or8.
Column3 has3 modulo3 and none modulo9.
Column4 has1,0,10,90 at moduli2,4,3,9 respectively.
All survivor lists remain in native JSON, including those that do not exclude a system.
The bounded column2 solve completed137842 triples,838 singular linear cases and2953 nonsingular integral derived-coordinate cases, with no target.
Its parameter cap alone proves no unbounded absence.

L250 retains D117's full written lifting obstructions: column2 modulo4, column3 modulo9, column4 modulo4, position1 by Pfaffian divisibility by5, and end positions0/5 by the exact eight-vertex parity model.
The84 independent author determinant calculations certify the displayed polynomial coefficients by degree-at-most-two interpolation.
They are a distinct calculation by the SAME author, not a noncontributor review.
Programs checking residual counts are likewise exact finite evidence at their stated scope; the whole-family theorem retains its explicit written reductions.

The requested complete polynomial remains unrealized.
L191's actual Phi2^2 P4 and L246's different unpadded sextic remain separately costed controls; all original, absolute and cover factors, ranks, heights and energies are preserved in L250.
Nothing here deletes a neutral factor, suspends another construction route, proves a uniform near-one mechanism, or resolves G0001.
The two reviewer-only files below are distinct from the fifteen original author files (seven programs, seven outputs and this readme).

### Current fixed adoption and separate executed review

The original [complete finding](../../../audits/reviews/Yin_R_G0114_v1.md#unbounded-column-complete-independent-review) records its actual whole shared-context SELF relationship; its separate mathematical implementation and original execution are retained below.
The current C415v2 adoption selects R617, whose whole SELF and original-domain read-only replay do not constitute a fresh isolated review.

The separately assigned structural reviewer executed [review_independent.py](review_independent.py), retaining review_result.json (`mathematics/computations/outputs/Yin_J_G0054/review_result.json`).
Its method imports no author implementation: seven scalar Bareiss determinants and rational Newton interpolation recover each complete polynomial; a6! alternating sum supplies the signed Pfaffian; a different signed21-point stencil recovers the full identities.
It independently recovered84 polynomials from588 scalar determinants, checked36 saved expression identities and every modular survivor list, repeated all137842 triples by solving the norm quadratic before the linear condition, and checked all64 binary classes at each of six positions.
The complete independent computation passed.
The mathematical payload, not time/path metadata or byte observations, is the verification target.
The checker remains runnable after draft retirement.
The full finding owns the actual review relationship.

The initial implementation failures, handwritten-constant correction, finite search boundaries and nonempty residue sets remain part of the mathematical account above.

Source scope is unchanged: HPM22 supplies only the previously inspected conference-matrix attribution from the L246 round.
Its earlier actual v3 pp.1--2 inspection is historical reused evidence, not a fresh PDF reading in the D117 review.
L246's direct matrix and quadratic-model proofs, L191's comparison and the retained signed reflection identity are the mathematical inputs.
No new source intake, conference classification or general Coxeter-gap theorem was adopted in this round.

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
| `review_result.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0114_v1.md#unbounded-column-complete-independent-review); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0617_v1.md#complete-path-column-whole-self-finding) |
