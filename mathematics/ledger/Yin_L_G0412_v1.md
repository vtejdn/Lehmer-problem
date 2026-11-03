---
author: Yin
---
# A nonsingular two-adic rank-seven realization of the complete quartic target

Current complete proof home: [C525](../claims/Yin_C_G0525_v1.md#two-adic-rank-seven-fixed-scope), with its actual current decision selecting [the current complete independent finding](../audits/reviews/Yin_R_G0732_v1.md#current-c533-v1-complete-independent-finding) at the exact C Statement and Argument.
The [original R419 whole](../audits/reviews/Yin_R_G0419_v1.md#two-adic-rank-seven-whole-independent-finding) retains its explicit independent relationship, 2026-10-18T16:10 date, original L412/J107/R418 bindings and complete PASS verdict.
The substantive content of the recorded contribution/scope messages is not established by that account; fixed draft reading, necessary R418 input and the word non-blind alone do not establish SELF.
The following original dated proof preserves the actual local realization, fixed finite inputs, contributions and separate integral/complete-cost obligations.

Date: 2026-10-18T16:09.
Human author Yin.
Root authors this analytic continuation from the already independently verified first J107 witness.
No higher-modulus computation, new target scan, numerical root calculation or native run is used.
This fixed exploration proves a local two-adic realization and preserves the separate integral and complete-cost obligations.

<a id="two-adic-coefficient-question"></a>
## Changed question and exact reuse

The [J107 first complete witness](../computations/programs/Yin_J_G0107/readme.md#rank-seven-mod-four-results), through [R418](../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding), has a FULL three-dimensional derivative image for the original seven-dimensional coefficient map.
This suggests a different conclusion from a modulus8 scan: a coherent exact realization over Z_2 for the entire target polynomial.
The fixed [L279 rank-six obstruction](Yin_L_G0279_v1.md#universal-rank-six-coefficient-congruence) remains untouched.
The [L270 lifting argument](Yin_L_G0270_v1.md#odd-prime-coherent-triangular-basis) addresses odd-prime bases of a fixed bilinear form; the present variable is the actual rank-seven upper matrix itself, at prime2.
[L270's attribution](Yin_L_G0270_v1.md#local-triangular-lifting-source-and-execution) already identifies the classical simple-root/Hensel mechanism and the inspected Stacks Tag04GE scope.
The complete elementary multivariable iteration is given below; no new external lifting theorem or source-proof acceptance is needed.
A bounded reuse read does not assert historical novelty.

<a id="two-adic-fixed-witness"></a>
## 1. Fixed integer input and an explicit nonsingular minor

Use EXACTLY J107's independently reconstructed first integer matrix

    U_*=[
      [1,0,0,1,0,1,1],
      [0,1,0,1,1,1,0],
      [0,0,1,1,1,0,0],
      [0,0,0,1,2,2,0],
      [0,0,0,0,1,0,0],
      [0,0,0,0,0,1,0],
      [0,0,0,0,0,0,1]].                              (1)

Its complete polynomial, ascending, is

    p_*(t)=[1,-1,-5,-8,-8,-5,-1,1].                  (2)

For any upper-unitriangular7-by7 matrix U over a commutative ring, let f(U)=(a,b,c) be coefficients1,2,3 of det(tU+U^t).
Determinant transposition gives the complete polynomial[1,a,b,c,c,b,a,1], so equality of these three coefficients is equality of the ENTIRE pencil.
Each coefficient is an integer polynomial in the21 upper entries.
Keep every entry of U_* fixed except positions(0,2),(3,4),(4,6), with indices starting at0.
Let E_1,E_2,E_3 be those three elementary matrices.

The actual J107 derivative columns at the binary base are, in their bit encoding,5,4,2 for these positions1,15,19 in the full21-entry order.
R418 independently reconstructs ALL21 columns by exact step-two coefficient differences.
The bit convention puts the a coefficient first, so the selected matrix is

    J=[[1,0,0],[0,0,1],[1,1,0]] over F_2,
    det J=1 over F_2.                                 (3)

The derivative is unchanged modulo2 at EVERY matrix congruent to U_* modulo2, since the coefficient derivatives are integer polynomials and U_* reduces to that same binary base.
Thus (3) is not a numerical nonsingularity claim at just one real matrix.
For a right side(y_1,y_2,y_3), its explicit inverse is

    J^-1 y=(y_1,y_3+y_1,y_2) over F_2.                 (4)

Only the independently verified selected rows are needed; author-only global enumeration counts and earliest-mask minimality are irrelevant.

<a id="two-adic-complete-realization"></a>
## 2. Exact local coefficient bijection and the target

Define Z_2 as the inverse limit of the rings Z/2^m Z, with compatible reduction maps.
Integer polynomial evaluation is defined coordinatewise and respects those maps.
The following precise conclusion holds.
For EVERY b=(b_1,b_2,b_3) in Z_2^3 satisfying

    b=(-1,-5,-8) modulo4,                            (5)

there exists a UNIQUE x=(x_1,x_2,x_3) in(4 Z_2)^3 such that

    f(U_*+x_1 E_1+x_2 E_2+x_3 E_3)=b.                (6)

Uniqueness is only inside this specified three-coordinate neighborhood with every other entry fixed.
It is not uniqueness among all upper-unitriangular realizations or among all bilinear forms.

Here is the full construction, avoiding an imported multivariable existence theorem.
Start x^(2)=0 modulo4.
Suppose an integral representative x^(m), divisible by4 in every coordinate, satisfies f(U_*+sum x_i^(m)E_i)=b modulo2^m for m>=2.
The next error

    e_m=[b-f(U_*+sum x_i^(m)E_i)]/2^m modulo2

is well-defined from the next residue of b and this integral evaluation.
Choose the UNIQUE binary vector epsilon_m=J^-1 e_m using (4), and set

    x^(m+1)=x^(m)+2^m epsilon_m.                       (7)

For every integer polynomial, expanding these increments gives

    f(U+2^m sum epsilon_i E_i)
       =f(U)+2^m J epsilon modulo2^(m+1).              (8)

All terms with at least two increments contain2^(2m), divisible by2^(m+1), and the first derivatives reduce to (3).
Consequently (7) corrects the full triple modulo2^(m+1) while keeping every previous residue.
These coherent triples define x in(4 Z_2)^3, and polynomial compatibility gives (6) at every modulus, hence exactly in Z_2.

For uniqueness, two different triples in this neighborhood have a least finite2-adic order m>=2 among their coordinate differences.
Their difference is2^m epsilon with a nonzero binary reduction epsilon.
The same expansion gives coefficient difference2^m J epsilon modulo2^(m+1), which is nonzero because J is invertible.
They cannot have equal coefficient triples.
This proves both directions of the claimed local bijection without presuming an integer or rational limit.

Take b=(-1,-1,0), which satisfies (5).
Let

    F(t)=Phi6(t)P4(t),
    P4(t)=t^4-t^3-t^2-t+1,
    Phi6(t)=t^2-t+1.

The complete target is

    (t+1)F(t)=[1,-1,-1,0,0,-1,-1,1].                 (9)

Equations (6) and reciprocity therefore give an ACTUAL upper-unitriangular U_2 in M_7(Z_2) with

    det(tU_2+U_2^t)=(t+1)Phi6(t)P4(t) in Z_2[t].     (10)

Only three entries vary from the explicit integer U_*; every diagonal remains1 and determinant U_2 is1.
For EVERY m>=2, reduction gives a compatible proper matrix modulo2^m whose complete polynomial is the target modulo2^m.
Choosing least nonnegative representatives of the three variable entries gives an actual integer upper-unitriangular representative at that modulus.
Its complete integer polynomial is not claimed equal to (9).
There is no higher-modulus mathematical execution behind this all-m result.

<a id="two-adic-realization-boundaries"></a>
## 3. What the local solution decides and leaves open

No congruence obstruction using only SOME finite power of2 can exclude all rank-seven realizations of the complete target (9), because (10) supplies a coherent solution at EVERY such power.
This is stronger than the independently computed modulus4 compatibility, while keeping the same target and rank.
It does not contradict L279's rank-six nonexistence, L287's fixed-core coupling obstruction, L214's common-stabilization obstruction or J104's bipartite full-cost minimum.
The three selected entries are allowed to vary in Z_2 and the construction does not fix an earlier bilinear congruence class.

A2-adic limit is not an integer realization: the iteration supplies no bounded real height, rationality or finite termination.
The integer representatives at different moduli can have unbounded entries, coefficients and absolute-companion expenses.
There is no real absolute-value operation on the resulting Z_2 entries being used to define a signed cover or assign Mahler measure.
The complete original/absolute/cover polynomials of the starting U_* remain exactly those retained in J107; they are not transported as invariants through this changing family.
All other primes, integral realizability and the complete original/absolute cost problem remain separate obligations.
No claim about the second J107 target follows from this chosen nonsingular minor.

This is a substantive change in the next structural question: for this first rank-seven target, further2-power exclusion scans cannot settle existence negatively.
A useful next step would need an integral or different-prime obstruction, an actual integer construction with all factors paid, or a proved global interpretation of these local solutions.
No such step is asserted completed here, and no new modulus or native computation is selected.

## Exact inputs and contribution limits

| Input | Actual role |
| --- | --- |
| [J107 first witness](../computations/programs/Yin_J_G0107/readme.md#rank-seven-mod-four-results) | Exact U_*, all polynomial coefficients, full21-entry order and selected derivative columns; no aggregate count or minimality premise. |
| Actual verifier payload (`mathematics/computations/outputs/Yin_J_G0107/verifier/verification.json`) | Complete independent step-two polynomials/columns, selected matrices and full original/absolute/cover evidence. |
| [R418 whole finite review](../audits/reviews/Yin_R_G0418_v1.md#rank-seven-mod-four-whole-independent-finding) | Independent finite witness scope only; it does NOT review the new all-depth proof. |
| [L270 classical mechanism](Yin_L_G0270_v1.md#local-triangular-lifting-source-and-execution) | Existing Hensel attribution and source-inspection limit; the new direct iteration is fully proved here. |
| [L279 old obstruction](Yin_L_G0279_v1.md#universal-rank-six-coefficient-congruence) | Exact rank-six comparison, not a restriction on the new rank-seven matrices. |
| [L287 fixed-core boundary](Yin_L_G0287_v1.md#quartic-core-complete-extension-classification), [L214 stable boundary](Yin_L_G0214_v1.md#stable-cancellation-fixed-scope), [J104](../computations/programs/Yin_J_G0104/readme.md#rank-ten-minimum-conclusion) | Comparison only; no fixed bilinear class, bipartite shape or cheap cover is assumed. |

Root supplied all new analytic mathematics; the previously independent J107 witness evidence is reused at its finite scope.
No mathematical computation or source-proof upgrade was performed.
