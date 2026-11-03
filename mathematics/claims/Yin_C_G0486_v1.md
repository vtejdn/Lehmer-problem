---
author: Yin
---

# Complete determinant price for all constant positive definite three-defect forms

This retains the complete necessary mathematical argument from [complete original L401](../ledger/Yin_L_G0401_v1.md#constant-spd-determinant-screen).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Use exactly the two original J102 reciprocal inputs P4=t^4-t^3-t^2-t+1 and P10=t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, of original degrees d=4,10.
Keep their original unreduced C157v3 numerators

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    E=-z^(-3d)H23/72,
    F0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375.

They are real on the unit circle; all scalars, phases, leading coefficients and original multiplicities remain.
Let mu be normalized circle Haar measure, omega=exp(2pi i/3), v=(E,F0,G)^t and V the matrix whose rows are v(z)^t,v(omega z)^t,v(omega^2 z)^t.
For EVERY constant real symmetric positive definite3-by-3 matrix Q put B_Q=v^t Q v and I_Q=integral log B_Q dmu.
Constancy requires the same Q at all three rotated points.
Let L=972000 and K_P be J102's nonzero ordinary integer polynomial obtained from the determinant of the three-by-three residue matrix of LE,LF0,LG by stripping only its least Laurent monomial.
Keep its entire content, leading coefficient and every root multiplicity, and put

    Lambda_P=log3+[log2+2m(K_P)-6log L]/3.

Then log B_Q and log abs(det V) are integrable, including their finite-order circle zeros, and

    I_Q>=Lambda_P+(log det Q-log2)/3.

This follows from product_(j=0)^2 B_Q(omega^j z)>=det Q abs(det V(z))^2 and J102's exact integral identity (3/2)log3+m(K_P)-3log L.
For every real target tau,

    I_Q<tau ==> log det Q<3tau-3Lambda_P+log2.

In particular I_Q<log2 requires log det Q<4log2-3Lambda_P; neither necessary implication is reversed.
For the Lehmer input the retained complete certificate gives Lambda_P>2.3906764770>7/3.
If Q is rational and ONE positive integer D<=4 clears EVERY MATRIX ENTRY, then det(DQ) is a positive integer, det Q>=D^(-3)>=1/64 and

    I_Q>=Lambda_P-(7/3)log2>7/10>log2.

No entry-height, off-diagonal-size or eigenvalue-ratio bound is assumed.
This includes every positive definite integer or unimodular Gram matrix.
More generally every real positive definite Q with det Q>=1 satisfies I_Q>21/10>2 on this same Lehmer input.
The matrix-entry D differs from a denominator clearing the expanded coefficients2Q_ij, and from the separate Laurent L already paid in Lambda_P.
The quantitative denominator consequence is not transferred to the quartic, another input or a z-dependent matrix.
Both fixed native certificates are reused at their complete original-degree/scalar/root-count/precision/shared-engine limits; Lambda_P is a certified LOWER BOUND EXPRESSION, not an evaluated family integral or attained minimum.
This supplies no arithmetic norm floor for arbitrary Q, original-root/Haar transfer or uniform coefficient/regularization budget.
A different separately proved arithmetic income must use its own tau in the necessary condition.
Rank-two positive semidefinite forms, indefinite forms, sufficiently small positive determinants and nonconstant matrices remain outside the exclusion.
The entire original proof of SPD1--SPD6, all rational strict comparisons, source/reuse/contribution and remaining limits follow below.
No native program, root isolation, grid, integral or new numerical estimate is executed by this construction.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:27 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Complete J102 analytic determinant input](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) | Only original real centered defects, full residue/rotation determinant, nonzero K, L^3 normalization and exact integrable Jensen identity at its two actual inputs. |
| dependency | [Existing J102 complete finite certificates](../computations/programs/Yin_J_G0102/readme.md#certified-results) | Only actual degrees4/10, full K degrees40/102, all nonmonic/content/root multiplicities and safe certified Lambda bounds at actual256-bit/shared-FLINT/no-fallback scope; no new execution. |
| dependency | [Exact unreduced centered defects and denominator comparison](Yin_C_G0157_v3.md#statement) | Only named H/E/F0/G definitions and the distinct expanded-polynomial clearing convention; its special arithmetic floor is not transferred to arbitrary SPD Q. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T00:30 |
| status | proved |
| reason | Adopt the entire exact registered statement and retained original proof after direct whole SELF inspection, preserving all original source/author/review/native/date and conditional/negative/remaining boundaries. This current construction supplies no old-date review, new source proof, native experiment or Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) | Only original real centered defects, full residue/rotation determinant, nonzero K, L^3 normalization and exact integrable Jensen identity at its two actual inputs. |
| dependency | [Exact dependency](../computations/programs/Yin_J_G0102/readme.md#certified-results) | Only actual degrees4/10, full K degrees40/102, all nonmonic/content/root multiplicities and safe certified Lambda bounds at actual256-bit/shared-FLINT/no-fallback scope; no new execution. |
| dependency | [Exact dependency](Yin_C_G0157_v3.md#statement) | Only named H/E/F0/G definitions and the distinct expanded-polynomial clearing convention; its special arithmetic floor is not transferred to arbitrary SPD Q. |
| review | [Exact review](../audits/reviews/Yin_R_G0698_v1.md#complete-constant-spd-whole-self-finding) | Every constant real SPD matrix, both exact controls, complete determinant-price and strict matrix-entry denominator consequence, all zero/scalar/target/nonclaim domains. Entire original L401 account/SPD1--SPD6, exact rational proof, full fixed native reuse, source/contribution/author/remaining boundaries. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

<a id="constant-spd-determinant-screen"></a>
## Constant positive definite forms and their determinant cost

Date: 2026-10-18T13:36.
Root proposed the extension to arbitrary constant positive definite matrices, the small-denominator exclusion and its exact target-dependent determinant condition.
The loglog_cyclic_review agent develops and author-checks this complete continuation for Yin.
Both are contributors to this new argument.
The same agent independently reviewed the earlier J102 argument in [R397](../audits/reviews/Yin_R_G0397_v1.md#three-rotation-j102-whole-independent-finding); that review retains its original scope and does not review this later extension.
This complete argument remains author-only pending its separate whole review; no new numerical calculation or arithmetic norm-floor theorem is supplied.

The actual [J102 three-rotation argument](../computations/programs/Yin_J_G0102/record.md#three-rotation-screen) and its [complete certified results](../computations/programs/Yin_J_G0102/readme.md#certified-results) supply the reused determinant and finite evidence.
The original [Schur-residual comparison, retained in C587](Yin_C_G0587_v2.md#schur-residual-screen) controls one effective component coefficient, whereas the present inequality uses the full three-by-three determinant.
[C155](Yin_C_G0155_v1.md#statement) proves the norm floor for the original sum of three squares, and [C157v3](Yin_C_G0157_v3.md#statement) proves it for its specified rational two-shear family; neither statement supplies that floor for arbitrary positive definite Q.
The distinct [original unbuffered singleton responsibility](../ledger/Yin_L_G0438_v1.md#unbuffered-reduction) and its [bounded-family conclusions](../ledger/Yin_L_G0438_v1.md#unbuffered-balanced-reassessment) retain their dated author scope.
The bounded reuse check also read [C154's actual statement](Yin_C_G0154_v1.md#statement): its complete diagonal-sign Frobenius determinant averages and matched coefficient volumes are different objects from this constant quadratic form in three defects.
These comparisons fix the applicable interfaces; no absence-of-prior-work or mathematical novelty claim is made for the elementary Hadamard extension.

### The exact inequality for every constant real positive definite matrix

Let P be either of the two retained J102 inputs, with the same original unreduced real centered functions E,F,G used in this draft; F is denoted F_0 in J102.
Let mu be normalized circle Haar measure, let omega=exp(2pi i/3), put v(z)=(E(z),F(z),G(z))^t, and let V(z) have rows v(z)^t,v(omega z)^t,v(omega^2 z)^t.
For ANY constant real symmetric positive definite three-by-three matrix Q define

    B_Q(z)=v(z)^t Q v(z),
    I_Q=integral log B_Q dmu.

Constancy means that the same matrix acts at all three rotated points.
The J102 exact residue calculation gives a nonzero ordinary integer polynomial K_P for each of these two inputs, with every leading coefficient, content and root multiplicity retained.
Write L=972000 and define the EXACT real number

    Lambda_P=log3+[log2+2m(K_P)-6log L]/3.

Lambda_P is the expression certified in J102, not an evaluated family integral or an attained minimum.
Then

    I_Q >= Lambda_P+(log det Q-log2)/3.             (SPD1)

To prove this, choose a real invertible matrix C with Q=C C^t and det C=sqrt(det Q)>0.
Explicitly, if Q=U diag(lambda_1,lambda_2,lambda_3)U^t with U orthogonal and every lambda_i>0, take C=U diag(sqrt(lambda_1),sqrt(lambda_2),sqrt(lambda_3))U^t.
The rows of V(z)C have squared Euclidean lengths B_Q(z),B_Q(omega z),B_Q(omega^2 z), and its determinant has squared absolute value det Q times abs(det V(z))^2.
The same finite row Hadamard inequality proved in J102 therefore gives

    product_(j=0)^2 B_Q(omega^j z)
        >= det Q abs(det V(z))^2.                  (SPD2)

Let lambda_min>0 be the least eigenvalue of Q.
The lower bound B_Q>=lambda_min(E^2+F^2+G^2)>=lambda_min G^2 and boundedness above on the circle show that log B_Q is integrable, because G is a nonzero Laurent polynomial with only finitely many finite-order circle zeros.
J102 proves det V is a nonzero Laurent polynomial on both retained inputs, so log abs(det V) is integrable as well.
Taking logarithms off the finite zero sets and using Haar rotation invariance in (SPD2) yields

    3I_Q >= log det Q+2 integral log abs(det V) dmu.

The exact J102 identity is

    integral log abs(det V) dmu
        =(3/2)log3+m(K_P)-3log L.

Substitution proves (SPD1), including the full scalar L^3 from the residue determinant.
No unit-circle zero or multiplicity is dropped.
The argument would give the same formula for another input after its corresponding nonzero determinant and normalization were established, but the two retained certificates are not evidence for that new input.

For any real target tau, (SPD1) gives the necessary condition

    I_Q<tau  ==>  log det Q<3tau-3Lambda_P+log2.    (SPD3)

In particular, possible saving below log2 requires

    log det Q<4log2-3Lambda_P.                     (SPD4)

These implications are necessary only; a sufficiently small determinant does not construct a successful form or prove its arithmetic norm floor.
No exponentiated decimal threshold is needed.

### All matrix-entry denominators at most four fail on the Lehmer input

For P=Lehmer_degree10, the actual J102 enclosure and R397 check give

    Lambda_P>2.3906764770>7/3.                     (SPD5)

The second comparison is an exact rational inequality, not a fresh numerical estimate.
Also exp(7/10)>1+7/10+49/200+343/6000=12013/6000>2, so log2<7/10.

Suppose Q is rational symmetric positive definite and there EXISTS a positive integer D<=4 such that EVERY MATRIX ENTRY of DQ is an integer.
The integer matrix DQ is positive definite, hence det(DQ) is a positive integer and is at least1.
Consequently

    det Q=det(DQ)/D^3>=D^(-3)>=1/64,
    log det Q>=-6log2.

Combining these inequalities with (SPD1) and (SPD5) gives

    I_Q >= Lambda_P-(7/3)log2
         > 7/3-49/30=7/10>log2.                   (SPD6)

Thus this entire rational positive definite family cannot attain a Haar logarithm below log2 on the original Lehmer input.
There is no bound on the sizes of its integer matrix entries, eigenvalue ratio or off-diagonal entries beyond positive definiteness and the stated clearing denominator.
In particular the conclusion includes every positive definite integer Gram matrix and every such unimodular Gram matrix.
More generally any real positive definite Q with det Q>=1 obeys I_Q>7/3-7/30=21/10>2 by the same proof.

The denominator condition is about the entries Q_ij, not just the coefficients of the expanded polynomial v^tQv.
The latter has off-diagonal coefficients 2Q_ij, so a denominator that clears that polynomial need not clear Q itself.
The clearing integer in C157v3 was defined for its expanded quadratic coefficients; it must not be substituted for the present D without checking every matrix entry.
The fixed Laurent denominator L is a separate normalization and has already been fully charged in Lambda_P.

### Exact consequence and remaining possibilities

This is a wider circle obstruction than the two-shear family alone: all constant positive definite rational three-defect forms with a matrix-entry clearing integer at most four fail the fixed log2 Haar target on the Lehmer control.
The argument establishes no original-field norm lower bound for arbitrary Q and no equality between original-conjugate and Haar averages.
If another form has a separately proved larger arithmetic income, its relevant target changes and must be tested with that actual target in (SPD3).
No exclusion is asserted for rank-two positive semidefinite forms, for indefinite matrices, or for all positive definite forms with smaller determinant; at determinant zero the finite logarithmic determinant bound is unavailable.
The quantitative denominator conclusion is not transferred to the quartic input, other original polynomials or matrices depending on z.
The unresolved original-root transfer and coefficient/regularization budgets remain separate even when a new circle candidate survives a necessary screen.
Author self-check covers the row orientation, determinant factor, all logarithmic zero cases, the full L^3 normalization, strict inequalities, exact rational constants and both denominator conventions.
Independent review of this new extension and any resulting strategy adoption remain separate from the preserved R397 finding.

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0102](../computations/programs/Yin_J_G0102/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
