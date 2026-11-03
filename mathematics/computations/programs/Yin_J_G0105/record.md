---
author: Yin
---
# Odd-cross quadratic norms and a four-candidate original-input test

Date: 2026-10-18T14:50.
Human author Yin.
Root develops this changed S4/S8 norm candidate under the continuing all-strategies-active instruction.
This is author mathematics and an unrun bounded protocol, without independent review or adoption.

<a id="odd-cross-norm-question"></a>
## Changed arithmetic and exact reused inputs

[C167](../../../claims/Yin_C_G0167_v1.md#signed-defect-statement) and J103 concern (X+s g)^2-pg^2 with integer s.
Their selected witnesses have positive Haar cost; that finite result excludes neither all parameters nor a different integral quadratic generator.
The present candidate uses omega=(1+sqrt5)/2, which is integral because omega^2-omega-1=0, and its conjugate1-omega.
The EXACT identity

    Norm_(F(sqrt5)/F)(X+eta omega g)
        =X^2+eta Xg-g^2, eta in{-1,1},                    (1)

has an ODD mixed coefficient without clearing an additional scalar denominator.
No maximal-order classification theorem is needed: the displayed monic equation proves the integrality used here.
The local reuse search found no fixed G-line application of this odd-cross expression to the actual three trace defects.
The underlying quadratic norm identity is elementary and is not claimed as new number theory.

Use C153v2's nonzero integral a,b,c in the ACTUAL totally real trace field F, and set e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.
For X=e or f, the accepted pairwise exclusion gives (X,g)!=(0,0).
Assume sqrt5 is not in F.
Then

    U_eta=X^2+eta Xg-g^2 in O_F is nonzero,
    |Norm_(F/Q) U_eta|>=1.                               (2)

Indeed if g=0 then X!=0.
If g!=0 and U_eta=0, the identity (2X/g+eta)^2=5 puts sqrt5 in F, a contradiction.
All coefficients of U_eta are integers, proving its integrality directly as well as through(1).
Its nonzero norm is therefore a nonzero rational integer.
This floor cannot be enlarged abstractly: F=Q,a=b=c=1,X=e=0,g=-1 gives U_eta=-1 for either eta.
No original polynomial realizing that abstract triple is asserted.

<a id="odd-cross-full-original-return"></a>
## Full original scalar, phases and logarithm

Let P be monic irreducible reciprocal nontorsion in Z[z], constant1, degree d=2r, with actual totally real trace field F=Q(alpha+alpha^-1), original K=Q(alpha), [F:Q]=r and [K:F]=2.
Use the GLOBAL unreduced C167 quantities

    H23=9P(z^2)^3-8P(z^3)^2,
    H25=75P(z^2)^5-64P(z^5)^2,
    H35=250P(z^3)^5-243P(z^5)^3,
    E=-z^(-3d)H23/72,
    F0=-z^(-5d)H25/800,
    G=-z^(-15d/2)H35/30375,
    L=972000,
    W_e=13500 z^(9d/2)H23,
    W_f=1215 z^(5d/2)H25,
    Z=32H35.

For J_X=E or F0 with the corresponding W_X, define

    A_eta=W_X^2+eta W_X Z-Z^2 in Z[z],
    N_eta=z^(-15d)A_eta/L^2=J_X^2+eta J_X G-G^2.           (3)

The common negative phase W_X=-L z^(15d/2)J_X and Z=-L z^(15d/2)G makes the mixed sign exactly eta.
The accepted original trace congruences give N_eta(alpha)=U_eta.
Only -Z^2 reaches exponents0 and30d, so

    deg A_eta=30d,
    A_eta(0)=lc(A_eta)=-50176,
    A_eta is reciprocal.                                (4)

No content, leading sign, neutral factor or original embedding is discarded.
The complete norm and Haar identities are

    Norm_(K/Q) N_eta(alpha)=(Norm_(F/Q) U_eta)^2>=1,
    Res(P,A_eta)=L^(2d)(Norm_F U_eta)^2,
    I_eta=integral_T log|N_eta|=m(A_eta)-2log L.             (5)

The source phase has original norm1 and all proper-subfield repetitions remain present.
The nonzero ordinary polynomial A_eta has only finitely many circle zeros with finite multiplicities; its log absolute value is integrable, so complete-root Jensen applies even when the circle function changes sign.
C140's actual ordinary representative A_eta/L^2 has degree30d, integral original value alpha^(15d)U_eta and full norm at least1.
The same paid supremum return therefore gives

    0<=d^(-1)log Norm_K N_eta(alpha)
       <=log sup_T|N_eta|+30m(P).                         (6)

No uniform Haar-to-original-conjugate transfer or new coefficient-budget bound is inferred.
The arithmetic logarithmic threshold is ZERO, not log2.
The relation 4N_eta=(2J_X+eta G)^2-5G^2 does not justify dividing the old norm floor by4: here integrality and nonvanishing of the quotient were proved before its floor was assigned.
It is precisely this integral odd-cross quotient that changes the candidate, with no increased width or degree.

<a id="odd-cross-four-candidate-protocol"></a>
## Bounded first test and its limits

Use exactly the original quartic_Salem_seed and Lehmer_degree10 coefficient arrays in [J97 input](../Yin_J_G0097/input.json).
Their actual trace fields are Q(sqrt13) and a totally real degree-five field, respectively, at C167/J103's retained exact interfaces.
Neither contains sqrt5: distinct quadratic fields exclude it in the first case, and the tower degree would force2 to divide5 in the second.
Thus(2)--(6) apply to both complete original inputs without an extra field search.

The entire proposed finite set is ONLY X in{E,F0}, eta in{-1,1}, four candidates per input.
Rank by the finite midpoint average of log absolute N at8192 and16384 equally spaced midpoints of[0,pi], with no clipping, zero replacement or third resolution.
Any zero or nonfinite sample makes that candidate unresolved for ranking.
Select at most ONE witness per input by least finite16384 average, with exact-floating ties ordered E before F0 then eta=-1 before1.
The sample choice is not a certified finite minimum.
The selected witness is built as the complete INTEGER A_eta from(3), including signed content and every squarefree multiplicity.
Certify I_eta by all-root Jensen at256 bits, allowing exactly one512-bit escalation and root radius goal1e-30, with aggregate300 seconds per input.
Also compute the actual trace norm, the full original norm and conjugate mean Lambda=log|Norm_F U_eta|/r, and compare I_eta against0 and the operational threshold-1/16.
A mathematical, precision or time failure remains unresolved/incomplete; do not silently enlarge the set or limit.

A new native J should own this changed four-form question and its separate verifier; J103 stays unchanged.
Independent exact reconstruction must check the four candidate numerators, the original trace/full norm and the selected complete-root certificate using a separate polynomial/value path.
It may share the certified ball engine while disclosing that limit.
No run is authorized by a parser check alone; complete the separate mathematical precheck before executing this defined finite batch.
If neither selected witness has negative certified I, retain that finite outcome and the actual discrepancy rather than infer an all-family failure or launch a larger parameter grid.
If a witness does have negative I, the original-root/Haar transfer and input-uniform coefficient costs remain separate open obligations.
Either result redirects research within the still active Task; it is not the run stopping condition.

Author check covers nonzero pair/field exclusion, integral odd coefficient, all common signs and half-degree exponents, exact endpoints, full norms, circle-zero integrability, every original degree cost and the limited numerical selection claim.
