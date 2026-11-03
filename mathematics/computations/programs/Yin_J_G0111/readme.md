---
author: Yin
---
# Exact affine residual-singleton screen

## Question and scope

Before execution, 2026-10-20T10:10, root declares this finite continuation of [the original unbuffered inquiry](../../../ledger/Yin_L_G0438_v1.md#unbuffered-reduction) under the [selected four-inquiry Task](../../../tasks/Yin_T_G0001_v1.md#decision-resume-retained-draft-inquiries-2026-10-20).
The original field is arbitrary totally real F, a,b,c are nonzero algebraic integers, s is1 or-1, and2c^2=3a^5, b^2-a^3+s(c^3-2b^5)=0, g=c^3-2b^5!=0.
The target is abs Norm_F(g)>=2^(r/2), with r=[F:Q].
This screen restricts b=u c+v to u,v in{-2,-1,1,2} and both signs s: exactly32 triples, without an adaptive enlargement.
The eight even-even triples are covered by the analytic C178 consequence below and are not factored.
The other24 triples use exact rational polynomial factorization and Sturm root counts; no approximate root or numerical integration is used.
Per-case execution is capped at15 seconds and the entire factoring pass at120 seconds.
A timeout or failed identity leaves that scope incomplete; it does not authorize a bigger parameter set or replacement conclusion.

## Analytic reduction and checking arrangement

Put b(X)=uX+v, Q(X)=b(X)^2+s(X^3-2b(X)^5), and H(X)=27Q(X)^5-8X^6.
Every original solution in this affine class has H(c)=0 and a^3=Q(c).
Conversely, for every nonzero root c of H with b(c)!=0 define a=3Q(c)^2/(2c^2).
H(c)=0 forces Q(c)!=0, a^3=Q(c) and a^5=2c^2/3, so all original equations follow with g=c^3-2b(c)^5.
These identities are also checked exactly in each retained factor field.
If c is integral then b(c) and Q(c) are integral, and a^3=Q(c) implies a is integral by transitivity of integral dependence.
For every real c!=0, H(c)=0 makes Q(c)>0 and a>0.
Thus a monic irreducible integer factor with every root real supplies the actual totally real field Q(c); a nonmonic primitive irreducible factor cannot have an algebraic-integer root.
All roots of a monic irreducible factor are real exactly when its distinct Sturm count equals its degree.
The full norm of g is the resultant of that monic factor with the actual g polynomial, with no degree or factor multiplicity discarded.
The exact inequality is Norm(g)^2>=2^degree.
The primitive field is Q(c), because b and the reconstructed a belong to it; in any larger ambient F both sides are raised by the same extension-degree factor.

For even u,v, b belongs to2O_F.
At a2-prime, the low branch G<e in [C178](../../../claims/Yin_C_G0178_v1.md#statement) would give B=G/2<e/2, contradicting B>=e.
Hence G>=e at every2-prime and abs Norm_F(g)>=2^r.
This stronger analytic floor covers those eight cases without assuming existence.

Root proposed the finite affine elimination and exact screen; entropy_attainment_bridge supplied the even-even saving and the integrality simplification from a^3=Q(c).
Both are contributors to this computational reduction; no independent review is asserted before its actual separate check.
The existing C178 whole R593 scope is reused only for the displayed local consequence.
No previous J has this affine elimination question or these parameters; J97--J102 supply unrelated original-polynomial circle diagnostics and are not rerun here.

## Files

[main.py](main.py) retains the exact input grid, coefficient construction, full factorization, Sturm counts and the conditional factor-field reconstruction and norm branch.
Complete generated evidence is written to mathematics/computations/outputs/Yin_J_G0111/results.json; incomplete evidence uses incomplete.json and is not a successful certificate.
No earlier generated output is an input.

## Reproduction

From the repository root with SymPy1.14.0, run:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0111/main.py
All polynomial coefficients and resultants use ZZ or QQ; Sturm intervals cover the entire real line.
The driver resolves its own J directory and output home independently of the caller's working directory and publishes results only after all cases finish.
A partial record is explicitly marked incomplete if a resource or arithmetic check fails.

## Results and limits

The declared pass completed with24 exact factorizations and Sturm counts, plus the eight analytically covered even-even cases.
Every computed H has one primitive irreducible factor of degree25 and multiplicity1.
Its positive leading coefficient is864 when abs(u)=1 or28991029248 when abs(u)=2; hence no computed factor can contain an algebraic-integer root c.
The exact distinct real-root counts are1 or3 and are both below the later author analytic upper bound of7, but real-root count alone is not an integrality test.
No admissible factor survived, so the field reconstruction and norm-violation branch was not exercised and no counterexample is asserted.
The complete coefficients, signed content, factors, real-root counts and grid are in results.json (`mathematics/computations/outputs/Yin_J_G0111/results.json`).

Root inspected all completed-case dispositions, degree/leading-coefficient scopes and the program's exact reconstruction check.
Irreducibility and Sturm counts rely on SymPy1.14.0 exact algorithms; the factor product was independently reconstructed within the same program, not by an independent symbolic engine or reviewer.
While this already running calculation finished, the separate author derived a broader analytic affine-family argument; that proof has its own required review and is not certified by this finite grid.
The present retained finite result is stronger on its24 computed choices than a mere norm-floor test: no original integral triple exists there.
A finite exclusion would exclude only these affine parameter choices, while an admissible norm violation would be a candidate counterexample to the general residual target pending independent verification.
A nonmonic factor, non-totally-real field, zero original value or failed reconstructed identity is not an admissible counterexample.
No conclusion about unrestricted b or all totally real integral triples follows from a finite negative screen.

## Independent verification

The separately assigned draft_inventory_later reviewer supplied [verify.py](verify.py), without importing the author program.
It reads only the actual retained results.json and rejects any missing, repeated or changed member of the declared32-case partition.
It independently constructs every Q and H by integer-list binomial coefficients and convolution, checks every coefficient, signed content, primitive factor and complete factor product, and checks both cleared rational reconstruction identities.
For each of the24 factors it recomputes a complete rational Sturm chain through a nonzero constant with Python Fraction arithmetic, retaining both infinite-endpoint sign variations.
Irreducibility is rechecked with SymPy1.14.0 over QQ, so that part shares the author's symbolic engine and is not a second-engine certificate.
The eight even-even rows are checked as scope labels; their mathematical floor still depends on the separately reviewed C178 argument.
No surviving monic totally real factor exists in the author output, so this verification does not execute an admissible-field norm branch.
The scope remains exactly the original24 computed cases and eight analytic cases, with the same15-second per-case and120-second whole-pass limits.

The verification command requires the complete actual author results.json:

    .venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0111/verify.py

Complete verification evidence is published to mathematics/computations/outputs/Yin_J_G0111/verification.json only after the full check succeeds; a failed check publishes verification-incomplete.json.
The full verification completed successfully, and its actual verification.json (`mathematics/computations/outputs/Yin_J_G0111/verification.json`) matches all24 coefficient records, signed contents, primitive irreducible factors and complete factor products.
The independently implemented full Sturm chains give14 factors with one distinct real root and10 with three, agreeing case by case with the author output.
The two cleared reconstruction identities also passed for all24 polynomials; this is separate from the unexercised admissible-field norm branch.
The [whole independent R452 finding](../../../audits/reviews/Yin_R_G0452_v1.md#affine-screen-whole-independent-finding) covers the actual reduction, complete finite result, verification execution and these limits without adopting a Claim or resolving the unrestricted residual question.

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
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0452_v1.md#affine-screen-whole-independent-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0452_v1.md#affine-screen-whole-independent-finding) |
