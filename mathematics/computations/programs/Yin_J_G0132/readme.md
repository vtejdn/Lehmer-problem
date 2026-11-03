---
author: Yin
---

# Exact finite cyclotomic probes on the remaining fifteenth-order canonical component

Human author Yin; root authored the original four-case computation, and the later author extension is attributed separately below.

## Question and scope

The [adopted C760 theorem](../../../claims/Yin_C_G0760_v1.md#decision-whole-reviewed-2026-10-25) leaves odd-root orders divisible by15 unresolved for fully cyclotomic inputs with own F modulo4 and X modulo2.
The original bounded scope retains exactly four exploratory inputs, all genuine integer cyclotomic traces:

    T=X^A F_3^B F_5^D F_15^K F_30(C_w) F_30(C_(w/2))^e,
    (A,B,D,K,w,e)=(2,2,3,2,16,0),
                    (2,8,12,4,16,1),
                    (4,8,12,4,16,1),
                    (2,4,6,2,8,1).

Here F_j denotes the complete monic primitive-order trace factor and C_j the integer trace Chebyshev polynomial; canonical F is a different symbol.
Use each SAME original T for a=rem_T T(C_2)/2, b=rem_T T(C_3)/3, c=rem_T T(C_5)/5, F=rem_T(2c^2-3a^5), G=rem_T(c^3-2b^5), X_plus=rem_T(b^2-a^3+G), and X_minus=rem_T(b^2-a^3-G).
The finite question is the coefficient residues of this actual system modulo4 and the nonzero binary G.
Those original programs test no other parameters, degree cutoff, source completion, all-order exclusion or original G0001 conclusion.

## Files

The exact modular producer is [main.py](main.py), and the separate full-integer reconstruction is [verify.py](verify.py).
The result (`mathematics/computations/outputs/Yin_J_G0132/result.json`) retains all four parameter tuples, degrees, complete integer T coefficient arrays and all seven actual canonical residue arrays modulo4.
The verification (`mathematics/computations/outputs/Yin_J_G0132/verification.json`) compares all these mathematical arrays and records the full-integer coefficient valuations.
Both are reconstructible generated files in the group's ignored output home, with no cross-J inputs or previous-output dependency for the producer.
Verification requires the actual producer output; a missing input fails without silently generating a replacement.

## Reproduction

Run from the repository root, in this order:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/main.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify.py
```

Each program resolves its own J and repository paths from its saved location.
The modular program uses exact standard-library integer arithmetic, monic polynomial division modulo4p followed by actual coefficient division by p, and reduction modulo4 at the unchanged original divisor.
Because the integer monic remainder is coefficientwise divisible by p, its canonical representatives modulo4p are divisible by p and their quotients are the true remainder/p coefficients modulo4.
This statement uses an integer division before modular reduction, never an inverse of2 modulo4.
The separate SymPy program reconstructs each F_j from Phi_j's symmetric Laurent coefficients and performs full integer monic divisions before comparing the actual modulo4 arrays.
It imports no producer code or hard-coded trace-factor coefficients from the producer.
No floating point, randomness, approximate roots or finite-field irreducibility test is involved.

## Results and limits

Root ran both retained programs successfully and read their complete source and actual finite results.
All four complete T arrays and all28 canonical residue arrays agree between modular monic arithmetic and the separate full-integer calculation.
These are two author implementations, not a fresh independent agent review or a proof-assistant verification.

| A,B,D,K,w,e | Trace degree | v_2(F) | v_2(X_plus) | v_2(X_minus) | v_2(G) |
| --- | --- | --- | --- | --- | --- |
| 2,2,3,2,16,0 | 82 | 1 | 0 | 0 | 0 |
| 2,8,12,4,16,1 | 146 | 1 | 0 | 0 | 0 |
| 4,8,12,4,16,1 | 148 | 1 | 1 | 1 | 0 |
| 2,4,6,2,8,1 | 74 | 1 | 1 | 1 | 0 |

Every entry is an exact coefficient valuation of the actual integer remainder; none is a root-evaluation estimate or merely a lower bound from a zero modular result.
In particular the degree74 and148 inputs have both first-bit residual signs and nonzero binary canonical G, but their first residual is not divisible by4.
All four full reciprocal polynomials are cyclotomic by their actual trace factorization, so their total Mahler measure is0.
The calculation supplies no example satisfying the first-four premise of C760 and does not exclude such an example at another parameter or another input.
The first parameter tuple also illustrates the limits of the [adopted C763 necessary multiplicity conditions](../../../claims/Yin_C_G0763_v1.md#decision-whole-reviewed-2026-10-25).
At h=15 it has E=18, w=16, u=2, B=2 and D=3, satisfying the displayed arithmetic intervals, equality w=10u-2B and first parity branch, while the actual computed F fails modulo4 and both X signs fail modulo2.
Thus this one arithmetic profile and actual lift do not establish the unit cancellations or coefficientwise realization left open by C763.
It supplies neither a positive nearzero Mahler family nor any all-order or all-profile inference.
The original four-case producer and verification pair ran no additional parameter, source completion or coefficient search.

## One larger-radical derivative-completion candidate

The separate bounded author extension proposed by root and implemented by characteristic_zero_bridge tests exactly

    T=(X-2)^2 F_480 F_15^2 F_3^2 F_5^3 B_91,
    B_91=1+sum_(j=1..45)C_j=F_7 F_13 F_91,
    F_480=F_30(C_16).

Its trace degree is127 and full reciprocal degree254.
This is one additional explicit input, not a parameter scan or an alteration of the four cases above.
The question is whether a larger complete radical and the proposed derivative divisibility at the lower third-order component suffice for its OWN F modulo4 and X modulo2.
The producer [odd_support_probe.py](odd_support_probe.py) explicitly reuses this group's standard-library polynomial functions in main.py, computes all seven original canonical arrays modulo4, and saves the single-case result (`mathematics/computations/outputs/Yin_J_G0132/odd_support_result.json`).
The different implementation [verify_odd_support.py](verify_odd_support.py) imports no producer code, reconstructs all actual cyclotomic factors with SymPy, performs the FULL integer monic divisions, and compares the complete arrays plus all binary-primary remainders in the verification (`mathematics/computations/outputs/Yin_J_G0132/odd_support_verification.json`).
It also tests actual integer divisibility by R=T/F_480 without replacing T's canonical system by R's own system.
Generated output is reconstructible and may be overwritten by rerunning these exact commands from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/odd_support_probe.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_odd_support.py
```

Both programs have now completed at this exact one-case scope, with all integer T/R/B91 coefficient arrays, all seven modulo4 canonical arrays and every full binary-primary remainder agreeing.
The second program uses SymPy1.14.0 and exact integer arithmetic.
Both programs were written and inspected by the author agent; the different implementation is an additional author self-check, NOT independent native evidence or a fresh review.
The verification requires the actual single-case producer output and fails if it is absent.

The exact coefficient valuations are v_2(a)=v_2(b)=v_2(c)=v_2(G)=v_2(X_plus)=v_2(X_minus)=0 and v_2(F)=1.
Thus the candidate fails both F modulo4 and either sign of X modulo2.
Its full radical degree is53 and the odd-multiplicity factor J=f_5 B_91 has degree47.
The exact lower-order diagnostics are ord_(f_3)(B_91+F_5)=16 and ord_(f_3)(J')=32, so the derivative-flatness proposal itself succeeds.
At the full fifteenth-order component the exact binary orders of a,b,c,G,X_plus,X_minus are4,3,2,6,8,8, respectively, while E_15=18.
The genuine integer F is even and ord_(f_15)((F/2)bar)=4.
After removing these f_15 powers, both (F/2)bar and X_plusbar=X_minusbar have initial unit X^2+X modulo f_15.
All other full binary primary remainders of the residuals vanish, and R divides each of a,b,c,F,G,X_plus,X_minus over Z.
These finite facts do not turn a zero factor restriction into a global pass or exclude another larger-radical input.
Complete reconstructible arrays and the full-integer verification remain in the two single-case output files above.

## Four periodic restrictions for the derivative-flat family

The next explicitly bounded calculation concerns n_s=3*2^s-5, s>=6, and T_s=R_0 F_480 B_(n_s), where R_0=(X-2)^2 F_15^2 F_3^2 F_5^3.
It computes ONLY the four factor restrictions corresponding to n modulo960 equal to187,379,763,571, with trace quotient degree64 in every case.
No unbounded-degree T_s is expanded, and these data are not full original remainder arrays.
The producer [odd_support_family.py](odd_support_family.py) uses modular Chebyshev recurrences in Z/4[X]/F_480 and the true C773 cofactor weights of the ORIGINAL canonical system.
The verification [verify_odd_support_family.py](verify_odd_support_family.py) imports no producer code and instead computes exact Laurent kernel sums and divided canonical values in Z[z]/Phi_480, of degree128.
The original four-case scripts, the degree127 full-remainder test and these four local restrictions have distinct output files and scopes.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/odd_support_family.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_odd_support_family.py
```

The generated four-class result (`mathematics/computations/outputs/Yin_J_G0132/odd_support_family.json`) and separate-implementation verification (`mathematics/computations/outputs/Yin_J_G0132/odd_support_family_verification.json`) are replaceable outputs of those commands.
The verification requires the actual producer file.
Both are author implementations, not independent native review.
Both family programs have completed, with all28 restricted canonical arrays agreeing under the trace substitution into Z[z]/Phi_480.
Every class has restricted coefficient valuations0 for a,b,c,G,X_plus,X_minus and1 for F.
The binary X order at f_15 is6 for representatives187 and763, and8 for379 and571, strictly below the full quotient exponent16.
The half of the even restricted F has f_15 order4 in every class.
These results are author self-checks, not independent native evidence.
The exact integer period reduction remains in [D6 UF12--UF13](../../../drafts/Yin_D_G0006.md#cyclotomic-derivative-flat-family-unit-failure).
The separate computation-free root-unit proof is fixed in [adopted C810](../../../claims/Yin_C_G0810_v1.md#decision-whole-reviewed-2026-10-26); it shows v(F_s(theta))=5/4 at every primitive480 trace and normalized dyadic place for every s>=5, despite ord_(f_3)(J_s')=2^s.
That Claim selects only the analytic first-residual and related source/valuation conclusions, without these native second-residual observations as a proof dependency.
A nonzero factor restriction refutes the original global congruence; a zero restriction would not establish a global pass.
No full unbounded-degree remainder was computed and no arbitrary larger-radical exclusion is claimed.
The analytic C810 theorem is independently reviewed and adopted at its separate scope; these native second-residual observations remain unadopted author evidence.

## One prescribed unit-adjusted degree187 input

After closing the preceding family calculation, root proposed the single new candidate

    T=(X-2)^2 F_480 F_15^2 F_3^2 F_5^3 F_9^4 B_187,
    B_187=F_11 F_17 F_187.

The actual trace degree is187, the reciprocal degree374, and the complete binary radical degree104.
This changes the cofactor from the preceding family and is outside C810's fixed statement.
The producer [unit_adjusted_probe.py](unit_adjusted_probe.py) computes ALL original canonical and residual coefficients modulo4 at the full T, using the same explicitly retained modular helper.
The separate [verify_unit_adjusted.py](verify_unit_adjusted.py) uses only the earlier SymPy-side helpers, imports no producer code, reconstructs all cyclotomic factors and performs the actual integer monic divisions before comparing every array and full binary primary.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/unit_adjusted_probe.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_unit_adjusted.py
```

The separate generated full result (`mathematics/computations/outputs/Yin_J_G0132/unit_adjusted_result.json`) and integer verification (`mathematics/computations/outputs/Yin_J_G0132/unit_adjusted_verification.json`) are replaceable outputs; verification requires the producer file.
Both programs are author implementations, not independent native review.
Both one-case programs have completed, with the full T/R/B_187 integer arrays, all seven modulo4 canonical arrays and every full binary-primary remainder agreeing.
The exact coefficient valuations are0 for a,b,c,G,X_plus,X_minus and1 for F.
The actual leading-unit adjustment holds, but both full original gates still fail.
The new first-half error has exact f_15 order6 and initial unit X^2+X^3, while both binary X signs have exact f_15 order8 below the full exponent18.
The new f_9^4 component has bbar order2 and all binary residuals zero at its full exponent4.
The derivative order ord_(f_3)(J') is64 and the complete radical degree104.
The complete algebraic unit check, precise finite failure and its actual root-value consequence v(F(theta))=11/8 are retained in [D6](../../../drafts/Yin_D_G0006.md#cyclotomic-f9-unit-adjusted-degree187-probe).
No second candidate, scan, higher-precision success or arbitrary-cofactor conclusion is inferred.
These remain two distinct author implementations and self-checks, with no fresh independent native or whole mathematical review.

## One paired move tested by the exact degree72 global reduction

The sole selected new move is Q=Pi_11 Pi_59 on the preceding degree187 input, with Pi_n=B_n*(B_n(C_3)/B_n)^2 and the quotient taken over Z.
The complete original trace degree is357, reciprocal degree714 and binary radical degree201.
The fixed divisor is J=F_15^2 F_480, of degree72, and H=T/J has binary polynomial coprime to Jbar.
The complete [D6 reduction GR1--GR8](../../../drafts/Yin_D_G0006.md#cyclotomic-degree72-global-gate-reduction) proves H divides the original residuals and that their global F modulo4 / X modulo2 gates are EQUIVALENT to their restrictions at J.
It treats repeated/overlapping moves, the endpoint and pure ninth-order base factors before using the coefficient equivalence.
This is stronger than checking only F_480, which would not give that equivalence.

The producer [paired_move72.py](paired_move72.py) constructs Pi_11 and Pi_59 by exact integer monic division, computes theta_p(J) with precision4p before division by p, and uses the actual cofactor weights H(C_p).
The separate [verify_paired_move72.py](verify_paired_move72.py) reconstructs the moves as F_11 F_33^2 and F_59 F_177^2 with full-Z SymPy arithmetic, checking the factors, weights, canonical J values and all seven original restricted remainders.
It imports no producer code and does not expand the full degree357 T or its degree285 cofactor.
Only this ONE prescribed pair is included; there is no other parameter, generator or group search.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/paired_move72.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_paired_move72.py
```

The generated degree72 result (`mathematics/computations/outputs/Yin_J_G0132/paired_move72_result.json`) and integer verification (`mathematics/computations/outputs/Yin_J_G0132/paired_move72_verification.json`) are distinct replaceable outputs.
The verification requires the actual producer file.
Both programs have completed, with all factor inputs, three actual theta_p(J) arrays, three cofactor weights and seven original restriction arrays agreeing modulo4.
The exact integer restriction has coefficient valuation1 for F and0 for a,b,c,G,X_plus,X_minus.
The proved GR6 equivalence gives the SAME original global conclusions v_2(F)=1 and v_2(X_plus)=v_2(X_minus)=v_2(G)=0, so the sole paired move fails both global gates and retains nonzero binary G.
The f_15 orders of a,b,c,G,X_plus,X_minus are4,3,2,6,8,8, with full exponent18.
The even first residual's half has f_15 order6 and initial unit X^3; integer linearity of rem_J transfers that half information to the original F, giving the actual root-value11/8 as detailed in D43 GR10.
No full degree357 input was expanded and no other move was tested.
They are author implementations and self-checks, not independent native evidence; the analytic reduction and this retained finite result have no new adopted assessment or fresh whole review.

## Complete256-class first-gate image character certificate

Root authorized ALL256 admissible residue classes n modulo960, with the excluded representative1 replaced by the actual admissible n=961, solely for the first-four homomorphism image.
The [complete period NP1--NP13](../../../drafts/Yin_D_G0006.md#full-degree72-move-periodicity) supplies this full alphabet, including the repeated-factor carry and the C_15 denominator case.
The [actual-base criterion UG5--UG6](../../../drafts/Yin_D_G0006.md#fixed-fifteen-unit-group-method) identifies F4 with L(Q)=kappa in R_7=F_2[X]/f_15^7, where

    h_n=L(Pi_n)=Pi_nbar(C_5)/Pi_nbar(X)^5,
    kappa=d*(H_0bar*deltabar)^5/gamma,
    d=X^12(1+X)^16, deltabar=d^2,
    gamma=(c_0bar/f_15^2) modulo f_15^7.

Here c_0 is the ACTUAL original degree187 base c restricted to J, not a freely chosen binary target.
The new programs retain every one of the256 images; NP13's period120 is only a checked duplication identity.
No subgroup elements, actual cofactor candidates, simultaneous second-residual solutions or other generator family are enumerated.

The separating character used here is

    ell(u)=Tr_(F16/F2)(x*u'(x)/u(x)), f_15(x)=0.

It is well-defined on R_7 units because changing a polynomial representative by f_15^7 A changes its derivative at x by0.
This does NOT assert that ordinary differentiation descends to a derivation of R_7 with its odd modulus exponent.
The product rule and additivity of field trace give ell(uv)=ell(u)+ell(v), so it annihilates the entire generated subgroup whenever it vanishes on every generator.
If ell(kappa)=1, the one-bit character supplies a complete separating certificate without requiring the generated subgroup's rank, order or enumeration.
The separate analytic all-n character proof belongs to earlier_bit_obstruction's author work; the programs check the explicitly bounded complete alphabet and actual target through different arithmetic.

The producer [first_gate_character.py](first_gate_character.py) uses bit-packed F_2 polynomials, bounded Chebyshev recurrences in degree28 and the exact displayed target formula.
The different implementation [verify_first_gate_character.py](verify_first_gate_character.py) imports no producer code: it computes finite centered Laurent sums in F_2[z]/Phi_15^7, recovers trace coefficients by a triangular Laurent basis, and independently rebuilds gamma from a full-Z restricted c_0 and deltabar from the true integer half(F_480-F_15^16)/2.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/first_gate_character.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_first_gate_character.py
```

The generated 256-image certificate (`mathematics/computations/outputs/Yin_J_G0132/first_gate_character.json`) and separate verification (`mathematics/computations/outputs/Yin_J_G0132/first_gate_character_verification.json`) retain exact polynomial bit encodings, every class and character, the actual target data and the checked outcome.
Verification requires the producer file and does not silently regenerate missing input.
Both programs have completed at the full declared256-class scope.
The different Laurent implementation matched all512 Pi-at-X/Pi-at-C5 component images, all256 h_n images and all256 character values, and its true integer base reconstruction matched every target coefficient.
All generator characters are0.
The actual target has logarithmic derivative kappa'(x)/kappa(x)=1, weighted logarithmic derivative x and trace1.
Its degree<28 representative has exact bit encoding182570536 under the displayed coefficient convention.
Thus the complete generated subgroup is separated from the actual target by ell; no full subgroup order or membership normal form is needed for this negative result.
There are16 distinct GENERATOR images among the256 retained classes, not a claimed subgroup of order16.
Every predicted period120 duplicate agrees, while all256 allowed classes remain explicitly present in the certificate.
The complete period and actual-base criterion therefore turn this finite separator into nonmembership for every allowed finite product of Pi_n; it is not an exclusion for other cofactors or the unrestricted cyclotomic domain.
No actual cofactor candidates, subgroup elements or second-residual solutions were enumerated.
These are two distinct author implementations and self-checks, not independent native review or an adopted global theorem.
The analytic all-n character proof and any fixed assessment remain at their separate responsible scope; this record supplies complete bounded corroborating evidence.

## Complete subgroup test for the next actual doubled profile

The new exact input is T_(2,0)=F_15^4 F_960 H_0^2 of trace degree374, with H_0=(X-2)^2F_3^2F_5^3F_9^4B_187 and actual single F_960, NOT F_480^2.
The complete [DP1--DP9 proof](../../../drafts/Yin_D_G0006.md#doubled-profile-exact-first-gate) establishes its integer carry, full outside-primary divisor and exact GLOBAL first-four criterion L(Q)=kappa_old^2 in R_14=F_2[X]/f_15^14.
It also proves the complete h_n period240, so precisely64 allowed residue classes are used, with1 replaced by the actual n=241.
The original first-jet character vanishes on this square target and is not assumed to settle the new question.

The producer [doubled_first_gate_group.py](doubled_first_gate_group.py) computes those64 images and uses actual ring multiplication and inverse operations to build a triangular principal-unit basis.
Every inserted pivot retains an exact word in the original generators and queues its SQUARE; the final certificate checks every original principal projection and every pivot-square closure.
The principal group has52 possible leading bits, while the order15 residue part is treated separately with a field-log Bezout certificate.
No actual cofactor candidates or second-residual solutions are enumerated.
An eventual positive word would carry its exact nonnegative exponents and original degree cost; a negative result must retain a nonzero reduced target and the complete closed-basis certificate.

The distinct [verify_doubled_first_gate_group.py](verify_doubled_first_gate_group.py) checks all images via a larger Laurent quotient, reconstructs the NEW single-F_960 integer base a/c and actual delta half, then validates every pivot word, original-generator reduction and later-layer square relation using SymPy arithmetic.
It does not import the producer's arithmetic or discovery algorithm.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/doubled_first_gate_group.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_doubled_first_gate_group.py
```

The generated group certificate (`mathematics/computations/outputs/Yin_J_G0132/doubled_first_gate_group.json`) retains all64 image polynomials, pivot words, square relations, target reduction and actual membership outcome.
Both the producer and the distinct verification (`mathematics/computations/outputs/Yin_J_G0132/doubled_first_gate_group_verification.json`) have completed.
The verifier matched all64 generators and128 Pi components, rebuilt the actual single-F_960 target from integer a_2,c_2 and the genuine delta_32 half, and checked40 pivot words,64 original principal reductions and40 later-layer square relations.
The exact generated subgroup has odd order3 and principal relative-order-two rank40, hence total order3*2^40=3298534883328.
This is not a claim that the principal part is an elementary Abelian group.
The target kappa_old^2, bit encoding19232663035708480, is NOT a member.
After the recorded position4 normalization, the remaining unit is1+X^2 f_15^3 modulo f_15^4, with first missing position10; its full bit encoding is33705785055175302.
The complete closed-basis argument in D43 DP10--DP12 makes this a genuine separating graded certificate, not a failed test against an incomplete linear span.
Via the actual DP8 criterion and complete period, every allowed doubled-profile Pi_n product fails F4; the analytic binary-primary argument makes its global coefficient valuation exactly1.
No actual cofactor candidate, further doubled profile or second-residual solution was enumerated or tested.
These are different author implementations and self-checks, not independent native review or an adopted mathematical result.

## Enlarged128-generator B and Gamma image at the same doubled profile

This is a separately authorized image extension after the exact old64 Pi_n-only failure.
The actual cofactor monoid now has generators B_n and Gamma_n=B_n(C_3), for n>1 odd and prime to15, at the SAME single-F_960 doubled base.
The complete [EG1--EG6 interface](../../../drafts/Yin_D_G0006.md#enlarged-doubled-cofactor-first-gate) pays all new parent/child multiplicities, preserves the global degree144 reduction and the target kappa_old^2, and proves period240 for each image type.
Thus the exact finite alphabet has BOTH types at all64 allowed classes, with1 represented by241, giving128 labeled generators.
The old64 programs, proofs and outputs remain separate and unchanged.

The new producer [enlarged_doubled_gate_group.py](enlarged_doubled_gate_group.py) retains the same actual multiplication, inverse, tracked-word and square-closure checks with128 labels.
The separate [verify_enlarged_doubled_gate_group.py](verify_enlarged_doubled_gate_group.py) rebuilds every image through Laurent sums, checks the true single-F_960 integer target and validates the complete subgroup certificate with different SymPy arithmetic.
If membership holds, both programs check the actual nonnegative B/Gamma word, every complete cyclotomic factor multiplicity and its full degree cost, without expanding the cofactor or testing X.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/enlarged_doubled_gate_group.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_enlarged_doubled_gate_group.py
```

The generated 128-image certificate (`mathematics/computations/outputs/Yin_J_G0132/enlarged_doubled_gate_group.json`) and distinct verification (`mathematics/computations/outputs/Yin_J_G0132/enlarged_doubled_gate_group_verification.json`) have their own output names and do not overwrite the smaller-family evidence.
Verification requires the corresponding producer file.
Both programs have completed and the different verifier has checked all128 images,256 evaluated components,45 pivot words,128 original principal reductions and45 later-square relations, together with the actual single-F_960 target.
The exact subgroup has odd order3 and principal relative-order-two rank45, hence order3*2^45=105553116266496.
The target IS a member.
The retained witness has31 nonzero B/Gamma terms at19 indices, all exponents0 through239, with cofactor trace degree112665, full trace degree113039 and reciprocal degree226078.
Every complete cofactor/full cyclotomic multiplicity and its degree cost has been checked by different divisor/totient arithmetic.
Its full binary radical degree is801 and maximal global binary Frobenius exponent1; in particular its f_11 exponent227 is odd.
The [tracked one-word input](inputs/enlarged_doubled_positive_word.json) preserves the exact selected mathematical word and all counts independently of ignored output availability.
The complete table and original first-gate consequence are in D43 EG7--EG8.
This establishes an author-checked ORIGINAL F4 witness through the exact criterion; Gbar is nonzero, but the second residual is NOT part of this subgroup test.
The two implementations remain author self-checks, not independent native review or an adopted joint result.
No actual cofactor candidates, higher profile or second-residual solutions were enumerated.

## One retained positive word: original second-residual diagnostic

The [tracked31-term word](inputs/enlarged_doubled_positive_word.json) is the sole input; its first-gate-only flags describe the source membership certificate, not this later diagnostic.
[positive_word_residuals.py](positive_word_residuals.py) computes its actual original weighted a,b,c,F,G,X_plus,X_minus modulo4 at J_2=F_15^4 F_960 of degree144.
Every canonical numerator is reduced modulo4p before integer division by p; all positive powers are taken in the actual quotient, without expanding Q or T.
[verify_positive_word_residuals.py](verify_positive_word_residuals.py) uses a different degree288 Laurent quotient, reconstructs complete primitive-factor weights, checks all93 term values and powers, and compares all seven full residue arrays.
It imports no producer arithmetic and uses exact packed integer convolution followed by monic reduction.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/positive_word_residuals.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_positive_word_residuals.py
```

The result (`mathematics/computations/outputs/Yin_J_G0132/positive_word_residuals.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/positive_word_residuals_verification.json`) agree: original F is zero modulo4, both X signs are nonzero modulo2, and G is nonzero modulo2.
Each X sign has exact binary f_15 order13 and initial unit1+X+X^2+X^3; its full global coefficient valuation is0.
The original a,b,c,G binary f_15 orders are8,6,4,12.
The global transfer, complete diagnostic and same-word derivative explanation are retained at [D6 WP1--WP6](../../../drafts/Yin_D_G0006.md#positive-first-gate-word-second-residual-failure).
In particular Qbar'(1)=1 from exactly B7,B29,B41 among its odd-exponent terms, so Qbar(C_5) fails the necessary square condition already at the first residue-field derivative.
The word retains full trace/reciprocal degrees113039/226078, radical degree801 and maximal binary Frobenius exponent1.
The two programs are author self-checks, not independent review; this one-word failure does not exclude the entire B/Gamma family.
No other word or second-residual solver was tested.

## Complete256-generator necessary joint filter

The separate [DS1--DS6 proof](../../../drafts/Yin_D_G0006.md#doubled-second-gate-square-filter) shows that simultaneous original F4/X2 requires M(Q)=(kappa_old^2,0), where M(Q)=(L(Q) in R_14,Dlog(Qbar(C_5)) in R_24).
Its complete safe n-period480 gives both B and Gamma types at all128 admissible classes, with1 represented by481: exactly256 labels.
The old modulo240 alphabet is not presumed complete for this stronger filter.
The [producer](joint_necessary_filter_group.py) uses actual pair multiplication, tracked words and square closure; the [different verifier](verify_joint_necessary_filter_group.py) reconstructs all images from Laurent kernels and checks them with SymPy pair arithmetic.
It also reconstructs the target from the ACTUAL single-F_960 integer canonical data.
Run from the repository root:

```text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/joint_necessary_filter_group.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_joint_necessary_filter_group.py
```

The complete certificate (`mathematics/computations/outputs/Yin_J_G0132/joint_necessary_filter_group.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/joint_necessary_filter_group_verification.json`) are separate from all earlier output scopes.
The verifier requires the corresponding producer certificate; the producer needs no generated input file.
All256 generators,512 R_14 evaluated components,256 R_24 logarithmic derivatives,51 tracked pivot words/squares,256 original principal reductions and the actual single-F_960 target have been checked.
The exact subgroup has odd order3 and principal rank51, split into45 unit-coordinate pivots and6 pure-additive pivots, hence order3*2^51=6755399441055744.
The target is NOT a member.
After recorded normalization it has unit coordinate1 and additive polynomial X^23+X^31+X^47+X^63+X^71+X^79+X^87+X^95, with first missing coordinate75 (additive bit23).
The full closure/normal-form argument and all actual-family limits are in [D6 MF1--MF6](../../../drafts/Yin_D_G0006.md#doubled-joint-necessary-filter-computation).
Combined with the proved necessary condition and full period, this excludes joint original F4/X2 for EVERY B/Gamma product at the specified doubled base.
No rectangular image, cubic solution, new word or further actual residual was tested.
These two implementations remain author self-checks; independent whole/native review and adoption are outstanding.

## Independent finite corroboration of C812

The isolated whole review [R1032](../../../audits/reviews/Yin_R_G1032_v1.md#whole-finding) retains [reviewer_c858_whole_check.py](reviewer_c858_whole_check.py), a separate standard-library implementation written from the fixed integer definitions.
It reads no author program, author output or exploration Draft.
Run from the repository root with `.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/reviewer_c858_whole_check.py`.
The program prints its replaceable result directly and needs no generated input file.
The actual degree82 base has f15 orders(a,c,F/2,G)=(4,2,4,6), and the degree187 empty Pi word has(4,2,6,6); the three displayed modulo4 expansions also agree.
These are independently performed finite corroborations only; [adopted C812](../../../claims/Yin_C_G0812_v1.md#decision-whole-reviewed-2026-10-26) rests on R1032's complete symbolic proof review, not these two cases or the separate author256-class certificate.

## Independent C860 native interface corroboration

The [whole independent C860 finding](../../../audits/reviews/Yin_R_G1034_v1.md#whole-finding) records cold inspection and successful reproduction of the selected joint-filter and positive-word producer/verifier pairs above.
The separate [review_c860_native_interfaces.py](review_c860_native_interfaces.py) imports no author arithmetic and checks the fixed Claim table, complete divisor counts and the interface between the group-word images and actual Q(C2),Q(C5) residue weights.
After those four selected commands, run `.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/review_c860_native_interfaces.py` from the repository root.
It requires the tracked selected-word input and the regenerated joint certificate and positive-word residue output, and writes the replaceable reviewer interface result (`mathematics/computations/outputs/Yin_J_G0132/review_c860_native_interfaces.json`).
The word's directly reconstructed L is19232663035708480 and its nonzero Dlog is64863481640943321376678543636, agreeing with the generator-image product.
The reviewer program supplies finite interface corroboration; R1034 owns the complete mathematical/native conclusion and its source, definition-registration and verification limits.

## Complete10240 local source-jet pairs

The [fixed C815 LJ1--LJ5 parametrization](../../../claims/Yin_C_G0815_v1.md#complete-local-source-parametrization) specifies exactly2048 source units S=1+sum_(k=1..11)s_k(Y+1)^k and five fifteenth-order branches.
This phase uses only those10240 pairs and the actual C860 DP/DS constants; it enumerates no actual cofactor words or generator images.
[local_source_jet_enumeration.py](local_source_jet_enumeration.py) obtains beta_old and gamma_old from the full old binary U_0(C_3)/U_0(C_5) remainders at f^18 and the genuine integer delta_16 difference.
[verify_local_source_jet_enumeration.py](verify_local_source_jet_enumeration.py) independently builds full integer T_187, computes its own b_0,c_0 divisions before restriction, reconstructs delta_16, and verifies EVERY pair with different SymPy arithmetic and low-pivot source-image elimination.
Run from the repository root:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/local_source_jet_enumeration.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_local_source_jet_enumeration.py
~~~

The producer has no generated-input dependency; the verifier consumes this phase's complete output (`mathematics/computations/outputs/Yin_J_G0132/local_source_jet_enumeration.json`).
The verification output (`mathematics/computations/outputs/Yin_J_G0132/local_source_jet_enumeration_verification.json`) retains actual integer constant reconstruction, all10240 checks and all exact surviving triples.
The source-image basis rank is24.
Exactly64 pairs survive, all at j=2, with masks25 XOR span_F2{32,88,138,266,512,1024}.
There are8 distinct Q15 classes and64 distinct classes at each of the two source coordinates.
Every survivor passes both original normalized equations at the required R_14/R_24 precisions.
The complete interpretation, source-polynomial formula, example triple and local-versus-actual realization distinction are in [fixed C815 LJE1--LJE6](../../../claims/Yin_C_G0815_v1.md#complete-local-enumeration).
The programs are two author implementations of an exhaustive LOCAL classification.
The separate [whole independent R1035 review](../../../audits/reviews/Yin_R_G1035_v1.md#whole-finding) inspected and reproduced both complete commands, supporting [adopted C815](../../../claims/Yin_C_G0815_v1.md#decision-whole-reviewed-2026-10-26) without asserting actual cyclotomic/global realization.
No further cofactor image, word, parameter profile or modulus is tested.

## Complete4192 endpoint-extended full-triple image

The complete image and selected-word mod8 phases are adopted in [C818](../../../claims/Yin_C_G0818_v1.md#decision-whole-reviewed-2026-10-26), through [whole independent R1038](../../../audits/reviews/Yin_R_G1038_v1.md#whole-finding), which inspected and reproduced all four declared commands.
The implementations retain their author roles; this separate review covers the exact two phases and no later kernel-jet work.

The exact author interface [fixed C818 EPX1--EPX12](../../../claims/Yin_C_G0818_v1.md#actual-endpoint-global-interface) gives4192 actual labels: E=X-2 and all127 admissible n in2 through479 times the33 paid actual smooth q representatives.
[endpoint_full_triple_image.py](endpoint_full_triple_image.py) computes the full multiplicative triple in R_14^* x S_(3,24)^* x S_(5,12)^*, tracks the actual C_15 x C_3 odd subgroup and97-coordinate principal carry closure, and decides ALL64 adopted C815 targets.
Its explicit required input is local_source_jet_enumeration.json (`mathematics/computations/outputs/Yin_J_G0132/local_source_jet_enumeration.json`); it does not rerun that10240-pair phase.
[verify_endpoint_full_triple_image.py](verify_endpoint_full_triple_image.py) rebuilds every triple from faithful Phi15^14/Phi3^24/Phi5^12 Laurent rings, uses different exact integer-convolution arithmetic, and checks all words, odd identities, pivot squares, generator reductions, target normalforms and actual positive-word costs.
Run from the repository root:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/endpoint_full_triple_image.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_endpoint_full_triple_image.py
~~~

The complete certificate (`mathematics/computations/outputs/Yin_J_G0132/endpoint_full_triple_image.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/endpoint_full_triple_image_verification.json`) cover all4192 labels and all64 targets.
The exact principal rank is85, with component counts45,23,17; the actual odd subgroup has order45 and is C_15 x C_3.
The full image order is45*2^85=1740853180245066011576893440.
Exactly32 fixed local targets are attained; all positive words and negative normalforms are retained.
The [tracked selected-word input](inputs/endpoint_full_triple_positive_word.json) has65 nonzero terms, endpoint exponent211 and full trace/reciprocal degrees3390998/6781996.
It is the lowest-degree word among the32 recovered certificates, with no global minimality assertion.
All full factor counts and degrees are checked; actual q values, not their residues, determine costs.
The complete interpretation and current boundaries are in [fixed C818 EF1--EF7](../../../claims/Yin_C_G0818_v1.md#complete-endpoint-image-certificate).
Both implementations remain author self-checks.
No original mod4 residual probe, full integer-word expansion or additional word optimization has occurred in this image phase.

## One selected endpoint word: original mod8 residuals

This phase uses ONLY [inputs/endpoint_full_triple_positive_word.json](inputs/endpoint_full_triple_positive_word.json), the65-term source-mask819 certificate word of trace degree3390998.
[endpoint_word_mod8.py](endpoint_word_mod8.py) computes true full degree374 base canonical numerators at precisions16,24,40, divides by the actual primes before restriction, and retains every original cofactor weight at J_2 of degree144.
Its actual rectangle argument C_(p q) uses exact doubling with the original q, without assuming a modulo8 period.
[verify_endpoint_word_mod8.py](verify_endpoint_word_mod8.py) rebuilds the true full-Z base/J divisions and uses direct centered Laurent kernels modulo Phi_15^4 Phi_960 of degree288.
It checks all195 term values/powers, all three base/Q/H weights and independently recovers all seven full mod8 trace arrays.
Run from the repository root:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/endpoint_word_mod8.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_endpoint_word_mod8.py
~~~

The producer output (`mathematics/computations/outputs/Yin_J_G0132/endpoint_word_mod8.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/endpoint_word_mod8_verification.json`) agree on exact global coefficient valuations v2(F)=2, v2(X_plus)=v2(X_minus)=1 and v2(a,b,c,G)=0.
Thus original F4/X2 passes, while F8 and both X4 fail.
The normalized binary classes F/4 and X_plus/2,X_minus/2 have exact f_15 order4, with units X^3 and X^2,X^2 respectively.
The complete original-divisor mod8 transfer, result table and every-root consequences17/8 and9/8 are retained at [fixed C818 W8.1--W8.6](../../../claims/Yin_C_G0818_v1.md#selected-original-mod-eight).
The word retains endpoint exponent211, full endpoint multiplicity215, full trace/reciprocal degrees3390998/6781996 and maximal binary Frobenius exponent1.
All mathematical fields in the tracked word remain identical to the source certificate; only its prior not-run scope metadata is updated.
Both calculations are author self-checks, not independent review.
No full large polynomial, other word or profile, endpoint480 variation, optimization or further modulus is computed.


## Complete augmented Xi16 image and all256 kernel jets

The author proof [fixed C821 AK1--AK3](../../../claims/Yin_C_G0821_v1.md#complete-augmented-kernel-image) retains the actual endpoint/rectangle monoid and proves the same4192 actual labels at first precision f^16, with unchanged source precisions24 and12 and exact exponent480.
The only native targets are ALL256 triples(1+f^14 h,1,1), deg h<8.
[augmented_endpoint_kernel_image.py](augmented_endpoint_kernel_image.py) computes the complete odd/principal closed-basis image, all256 decisions, every positive kernel word and the exact projection to the adopted C818 image.
[verify_augmented_endpoint_kernel_image.py](verify_augmented_endpoint_kernel_image.py) reconstructs all4192 triples in faithful Laurent rings Phi15^16/Phi3^24/Phi5^12, checks every word/relation/decision and independently recomputes the requested old-word target from actual integer trace data.
Explicit required inputs are the adopted C818 outputs endpoint_full_triple_image.json, endpoint_word_mod8.json and endpoint_word_mod8_verification.json in this J output home.
No missing input is regenerated or replaced automatically.
The target is derived from those actual normalized quarter/c arrays and genuine delta half; no supplied numerical h is used as an oracle.
Run from the repository root:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/augmented_endpoint_kernel_image.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_augmented_endpoint_kernel_image.py
~~~

The complete producer certificate (`mathematics/computations/outputs/Yin_J_G0132/augmented_endpoint_kernel_image.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/augmented_endpoint_kernel_image_verification.json`) cover all4192 labels, all256 targets and every old-image projection.
The augmented image has principal rank92 with component counts53,22,17, odd order45 and full order45*2^92.
Exactly128 kernel jets are attained; for h=sum h_i X^i their complete decision list is equivalent to h_0+h_4+h_6=0.
Both programs recompute gamma_Q=17, delta16=17, g_Q=21524, rho=230 and the requested h=189 from the adopted original arrays and genuine integer trace halves.
The requested target is attained by the [new complete73-term K word](inputs/augmented_endpoint_kernel_positive_word.json), with endpoint exponent0, trace degree3129360 and reciprocal degree6258720.
The exact proof, input scope, image interpretation and limits are retained at [fixed C821 AK1--AK6](../../../claims/Yin_C_G0821_v1.md#complete-augmented-kernel-image).
The different verifier checks every positive word and every negative normalform, as well as the chosen word's complete factor multiplicities and costs.
The new tracked K word records only augmented kernel attainment; the old65-term word and all selected C818 files remain unchanged.
The result can certify kernel-jet attainment, not original residual gates for the product with the old word.
No product residual probe, full large polynomial expansion, larger precision, other profile or word optimization is part of this phase.
Both implementations are author self-checks, with later cold independent review separate.


## One specified QK product: original modulo-eight diagnostic

This phase uses ONLY [inputs/endpoint_kernel_product_word.json](inputs/endpoint_kernel_product_word.json), the literal concatenation of the adopted65-term Q and specified73-term h189 kernel K.
The input retains all138 actual terms, unreduced exponents, actual q values and complete costs: trace degree6520358 and reciprocal degree13040716.
[endpoint_kernel_product_mod8.py](endpoint_kernel_product_mod8.py) uses unchanged original trace helpers; [verify_endpoint_kernel_product_mod8.py](verify_endpoint_kernel_product_mod8.py) uses a different degree288 Laurent calculation and full integer canonical divisions.
Required original inputs are the two source words and the adopted endpoint_word_mod8.json / endpoint_word_mod8_verification.json outputs; the verifier additionally requires the new producer output.
No missing original input is regenerated.

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/endpoint_kernel_product_mod8.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_endpoint_kernel_product_mod8.py
~~~

The complete trace output (`mathematics/computations/outputs/Yin_J_G0132/endpoint_kernel_product_mod8.json`) and different Laurent verification (`mathematics/computations/outputs/Yin_J_G0132/endpoint_kernel_product_mod8_verification.json`) agree on all414 factor values/powers, separate Q/K and complete weights, true prime divisions and all seven entire mod8 arrays.
The lowest binary quarter cancels modulo f^8, but its exact order is8 with initial unit1+X; global v2(F) remains2.
Both second signs have exact global v2=1, with binary half order4 and initial unitX^2; thus F8 and both X4 fail while F4/X2 remain valid.
The complete proof and everyprimitive960-place values9/4 and9/8 are retained in the linked K8 result.
The exact proof and intended scope are [fixed C821 K8](../../../claims/Yin_C_G0821_v1.md#complete-product-mod-eight).
All selected C818 and augmented-image programs, source inputs and outputs remain unchanged.
No new image, other word, exponent optimization, larger profile/modulus or full high-degree expansion is part of this phase.
Both implementations are author self-checks; independent review is separate.

[Whole independent R1041](../../../audits/reviews/Yin_R_G1041_v1.md#whole-finding) covers the complete augmented-image and one-product phases above, including unchanged four-command reproduction and a cold product-native helper.
[Adopted C821](../../../claims/Yin_C_G0821_v1.md#decision-whole-reviewed-2026-10-26) selects that finding at its exact bounded scope.
The original programs remain author implementations; the independent relationship belongs to the performed R review.


## Complete full-eighth Xi16-kernel image and one specified-fiber target

The complete reduction and mixed normal form are retained in [fixed C823](../../../claims/Yin_C_G0823_v1.md#complete-native-kernel-proof), using adopted C866, C821 and C868 at their exact scopes.
The complete joint alphabet has4193 ACTUAL labels: the4192 augmented-image labels and B_481, without an Omega((X-2)^240) assumption.
The finite evidence must cover45 lifted odd words,92 lifted principal words and all6310 relation vectors:4193 generator-section,92 later-square and2025 ordered odd-table relations.
All relation reductions and all basis positive kernel words/costs are retained; word exponents use the JOINT bound960.

The producer is full_eighth_kernel_image.py and the different verifier is verify_full_eighth_kernel_image.py.
They require the adopted augmented_endpoint_kernel_image.json, endpoint_kernel_product_mod8.json and endpoint_kernel_product_mod8_verification.json plus the unchanged tracked product input.
Their outputs belong in this J's existing generated home.
The ONE target is recomputed from the actual original quarter and c arrays as gamma^(-2)(qbar/f^8) in R_28.
Both new image commands have completed the entire scope; their certificate (`mathematics/computations/outputs/Yin_J_G0132/full_eighth_kernel_image.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/full_eighth_kernel_image_verification.json`) agree on every4193 image,45/92 lifts and6310 relation identity/reduction.
The exact additive rank is54; the complete joint image has order45*2^146.
The ONE recomputed target1097715512823540921521368963822440 is attained with normal remainder0.
Every54 basis word and the selected126-term correction word has a complete positive960-exponent realization and full factor/degree accounting.
The [selected correction L](inputs/full_eighth_kernel_positive_word.json) has endpoint exponent240 and trace degree86641990.
The full author result and limits are retained in [fixed C823 JC8](../../../claims/Yin_C_G0823_v1.md#complete-native-kernel-proof).
No original residual probe of a new word, larger precision/profile, other fiber, optimization or full high-degree expansion is authorized by this record.
Different author implementations do not constitute independent review.


## One full-eighth positive product: original modulo-eight diagnostic

The only input is [inputs/full_eighth_positive_product_word.json](inputs/full_eighth_positive_product_word.json), the literal138-term Q_0 plus126-term verified correction L.
It retains all264 actual factor occurrences and original exponents/q, with full trace/reciprocal degree93162348/186324696.
The producer is [full_eighth_positive_product_mod8.py](full_eighth_positive_product_mod8.py); the different verifier is verify_full_eighth_positive_product_mod8.py.
They require the two unchanged source words and adopted C821 original Q_0 arrays; the verifier also requires the new producer output.
The exact original-divisor scope is [fixed C823 FP](../../../claims/Yin_C_G0823_v1.md#complete-original-f8-diagnostic).

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/full_eighth_positive_product_mod8.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_full_eighth_positive_product_mod8.py
~~~

The complete producer result (`mathematics/computations/outputs/Yin_J_G0132/full_eighth_positive_product_mod8.json`) and different Laurent verification (`mathematics/computations/outputs/Yin_J_G0132/full_eighth_positive_product_mod8_verification.json`) agree on every792 value/power, separate Q_0/L/full weights, true integer scalar divisions and all seven fullmod8 arrays.
The original global F8 gate passes, with coefficient valuation established only as at least3.
Both original X4 gates fail with exact coefficient valuation1; both halves have binary f-order4 and initial unitX^2+X^3.
Original X2 and nonzero binary G are retained; the complete author interpretation and costs are in [fixed C823 FP1--FP5](../../../claims/Yin_C_G0823_v1.md#complete-original-f8-diagnostic).
Zero modulo8 gives only valuation at least3; no F/8 class or modulo16 inference is permitted.
No other word, new image, larger modulus/profile, optimization or full high-degree expansion occurs.
Different author implementations remain separate from later cold independent review.


<a id="one-product-second-half-ambient-eight-bit-image"></a>
## One-product ambient eight-bit lowest-second-half image

The only actual input is the literal264-term Q_1=Q_0L in [inputs/full_eighth_positive_product_word.json](inputs/full_eighth_positive_product_word.json), with the completed original-mod8 result (`mathematics/computations/outputs/Yin_J_G0132/full_eighth_positive_product_mod8.json`) and its different verification arrays (`mathematics/computations/outputs/Yin_J_G0132/full_eighth_positive_product_mod8_verification.json`).
These files are required inputs; neither new program regenerates an original residual or substitutes another word.
The original source account remains the exact scope selected by [C823](../../../claims/Yin_C_G0823_v1.md#decision-whole-reviewed-2026-10-26), now adopted after its separate whole mathematical/native review.
The complete algebra and bounded fiber theorem are fixed in [adopted C824](../../../claims/Yin_C_G0824_v1.md#decision-whole-reviewed-2026-10-27), with its exact [normalized second-half definition](../../../claims/Yin_C_G0824_v1.md#normalized-second-half-response).

The exact binary producer is [second_half_ambient_response.py](second_half_ambient_response.py); the different SymPy implementation is [verify_second_half_ambient_response.py](verify_second_half_ambient_response.py).
Run from the repository root, in this order:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/second_half_ambient_response.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_second_half_ambient_response.py
~~~

The producer uses integer monic J/P^4 division and a genuine delta half, binary polynomial arithmetic, direct source substitutions and XOR elimination.
The verifier imports no producer arithmetic: it reconstructs P and V from full integer cyclotomic polynomials, reads the prior different verifier's complete original arrays, forms true halves and uses SymPy1.14.0 polynomial arithmetic and DomainMatrix elimination over GF(2).
Both reconstruct beta,gamma,delta and BOTH normalized second-half targets without numerical oracles.
The verifier evaluates all256 source polynomials directly before comparing the new producer output.

The complete result (`mathematics/computations/outputs/Yin_J_G0132/second_half_ambient_response.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/second_half_ambient_response_verification.json`) retain exactly8 columns, all256 source masks/images, all genuine half arrays and reconstructed coefficients, rank6 and64 distinct images.
Both targets equal X^14 and are outside the ambient image; both augmented ranks are7.
The functional with coefficient mask17412, namely coefficient2+coefficient10+coefficient14, vanishes on every image and equals1 on each target.
The native arithmetic, basis witnesses, target remainders and separator agree.
These are different AUTHOR implementations, not independent review.

Only the ambient necessary map for this one actual input is computed.
There is no120-bit image, cofactor construction, other word, original-residual rerun, larger modulus/profile, F/8 calculation or higher-precision conclusion.
The entire specified Xi16-fiber X4 exclusion and old-mask819 joint F8/either-X4 exclusion are proved in [C824 SX8](../../../claims/Yin_C_G0824_v1.md#sx8-the-ambient-separator-excludes-the-entire-specified-xi_16-fiber), with the original C823 input's scope retained.
Both new generated outputs may be replaced by these exact scoped commands; the retained original source arrays and word are not modified.

[Whole independent R1043](../../../audits/reviews/Yin_R_G1043_v1.md#whole-finding) covers the full-eighth kernel image and literal264-term product phases, with complete reproduction of both different verifiers, all four implementations inspected and a cold binding/cost helper.
[Adopted C823](../../../claims/Yin_C_G0823_v1.md#decision-whole-reviewed-2026-10-26) selects that exact mathematical/native scope.
The separate [whole independent R1044](../../../audits/reviews/Yin_R_G1044_v1.md#whole-finding) covers the C824 second-half proof, both new ambient programs and all256 images, and reproduced both commands.
C824 selects that exact review; the implementations themselves retain their AUTHOR provenance.

<a id="complete-local-target-second-half-screen"></a>
## Complete32-target first-eighth and second-half screen: complete author result

The complete proof, exhaustive conditional branches and verified16/16 classification are fixed in [adopted C825](../../../claims/Yin_C_G0825_v1.md#decision-whole-reviewed-2026-10-27).
The general second-half input is [adopted C824](../../../claims/Yin_C_G0824_v1.md#decision-whole-reviewed-2026-10-27) at its actual X2-only transport scope.
The producer is [complete_local_target_second_half_screen.py](complete_local_target_second_half_screen.py), and the different verifier is [verify_complete_local_target_second_half_screen.py](verify_complete_local_target_second_half_screen.py).
Both NEW programs completed the entire bounded scope without repair; they are different AUTHOR implementations, not cold independent review.

The required retained inputs are endpoint_full_triple_image.json, endpoint_full_triple_image_verification.json, augmented_endpoint_kernel_image.json and augmented_endpoint_kernel_image_verification.json in this J's output home.
They supply the exact32 C818 positive Q_i words and the complete256 C821 kernel-jet decisions with their128 retained positive K_h words.
Use each actual label q and literal exponent; no word search, optimization or exponent reduction occurs.
C821's historical resulting_T_* cost fields refer only to Q819; new product costs use each Q_i degree plus the selected kernel_trace_degree.

The producer computed all32 complete original mod8 references and32 conditional actual Q_i K_h references, sharing252 factor values and1530 literal powers from84 actual labels.
It retains every literal binding, all seven original arrays, true base scalar divisions, all first-quarter classes/derivatives/required jets and all relevant second-half columns, complete ambient images, basis/rank, target remainders and separators.
The verifier uses degree288 faithful Laurent arithmetic and SymPy over ZZ/GF(2), independently chooses every required branch and reference, and checks the entire payload.
Ambient membership remains unresolved; no120-bit actual kernel image or full high-degree polynomial is computed.

The executed reproduction commands from the repository root are:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/complete_local_target_second_half_screen.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_complete_local_target_second_half_screen.py
~~~

The complete producer output (`mathematics/computations/outputs/Yin_J_G0132/complete_local_target_second_half_screen.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/complete_local_target_second_half_screen_verification.json`) retain all32 independently checked records and all64 complete references.
Exactly16 fibers are excluded by ambient nonmembership; the other16 remain unresolved by this necessary screen.
All32 first-quarter low classes and derivatives vanish, and all required jets44,55,166,189 are attained by the prior adopted kernel certificate.
Every second-half system has rank6; jets55/189 give nonmember targets26156/8748 with separator17412, while jets44/166 give ambient members25762/26169.
No ambient membership is promoted to an actual kernel realization or full X4 solution.
The exact source-mask lists, actual costs and whole-fiber inference are fixed in [C825](../../../claims/Yin_C_G0825_v1.md#complete-native-screen), with separate [whole independent R1046](../../../audits/reviews/Yin_R_G1046_v1.md#whole-finding) covering the new proof and complete different-verifier reproduction.
The old selected programs, words and outputs remain unchanged inputs.

<a id="extended-joint-kernel-and-sixteen-targets"></a>
## Extended joint kernel and all sixteen remaining targets: complete author image

The exact [C826 criterion](../../../claims/Yin_C_G0826_v1.md#decision-whole-reviewed-2026-10-27) governs this new phase, with actual [C825 references](../../../claims/Yin_C_G0825_v1.md#decision-whole-reviewed-2026-10-27).
The complete fixed scope is [adopted C828](../../../claims/Yin_C_G0828_v1.md#decision-whole-reviewed-2026-10-28).
The new producer is [joint_eighth_second_half_kernel_image.py](joint_eighth_second_half_kernel_image.py); the different verifier is [verify_joint_eighth_second_half_kernel_image.py](verify_joint_eighth_second_half_kernel_image.py), the different AUTHOR implementation.
Both new programs completed the entire scope without repair; [whole independent R1048v2](../../../audits/reviews/Yin_R_G1048_v2.md#whole-finding) subsequently checked the complete fixed mathematics and native scope.

Required inputs are the unchanged full_eighth_kernel_image.json and full_eighth_kernel_image_verification.json, plus complete_local_target_second_half_screen.json and its different verification, all in this J's output home.
The adopted4193 Omega values/6310 genuine A coordinates are reused; only source depths28/14, their complete lifted relations and the120-bit span are newly computed.
Every one of the16 actual references is retained, with a128-bit target, exact actual costs and positive-word or negative certificate scope.
There is no old mixed-image regeneration, original residual probe of a new product, higher modulus/profile, optimization or full large-degree expansion.
A positive result means F8 and lowest-half cancellation only, not full X4.

The executed reproduction commands are:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/joint_eighth_second_half_kernel_image.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_joint_eighth_second_half_kernel_image.py
~~~

The complete producer certificate (`mathematics/computations/outputs/Yin_J_G0132/joint_eighth_second_half_kernel_image.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/joint_eighth_second_half_kernel_image_verification.json`) agree on all4193 new source images,6310 relations,59-dimensional actual kernel and57-dimensional projected image.
All16 actual targets are members, with eight distinct positive kernel words and complete individual costs; all16 A-only reductions are also members.
The complete image, all16 actual targets and exact cost table are fixed in [adopted C828](../../../claims/Yin_C_G0828_v1.md#complete-joint-image-certificate), through [whole independent R1048v2](../../../audits/reviews/Yin_R_G1048_v2.md#whole-finding).
The image phase contains no original product-residual probe; the subsequent sole mask203 diagnostic is retained separately below, while the other15 products remain unprobed.

<a id="joint-mask203-original-mod-eight"></a>
## One canonical mask203 joint-kernel product: original modulo8

The exact separate original-divisor scope is fixed in [adopted C828](../../../claims/Yin_C_G0828_v1.md#mask203-original-mod-eight).

The sole actual input is [joint_mask203_product_word.json](inputs/joint_mask203_product_word.json), containing Q20369 terms, K4472 terms and the new joint kernel127 terms, with all268 occurrences and actual q/exponents retained.
The original trace degree is65635185 and reciprocal degree131270370; the cofactor endpoint exponent is811 and full endpoint multiplicity815.
The producer is [joint_mask203_product_mod8.py](joint_mask203_product_mod8.py); the different degree288 Laurent verifier is [verify_joint_mask203_product_mod8.py](verify_joint_mask203_product_mod8.py).
Both require the completed all32 screen and joint-kernel outputs with their different verifications, and bind the exact mask203 reference and positive word before any residue calculation.

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/joint_mask203_product_mod8.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_joint_mask203_product_mod8.py
~~~

The complete producer output (`mathematics/computations/outputs/Yin_J_G0132/joint_mask203_product_mod8.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/joint_mask203_product_mod8_verification.json`) agree on all804 factor values/powers, three separate bundles, full weights, true integer prime divisions and seven complete original mod8 arrays.
F8 passes with ONLY v2(F)>=3; both X4 gates fail with v2(X_plus)=v2(X_minus)=1.
Both genuine halves have binary f-order8 and initial unitX; binary G is nonzero.
These remain different AUTHOR implementations; the separate [whole independent R1048v2](../../../audits/reviews/Yin_R_G1048_v2.md#whole-finding) covers their full selected scope and completed reproduction/payload comparisons.
There is no F/8 class, modulo16 inference, other word, optimization or whole-fiber exclusion from this one failure.

<a id="complete-four-coset-next-half-screen"></a>
## Complete sixteen-by-four next-half screen: complete author verification

The complete statement/proof and all64 target/degree tuples are fixed in [adopted C831](../../../claims/Yin_C_G0831_v1.md#decision-whole-reviewed-2026-10-28), with [adopted C830](../../../claims/Yin_C_G0830_v1.md#decision-whole-reviewed-2026-10-28) supplying the symbolic four-coset/next-half theorem.
The [producer](complete_four_coset_next_half_screen.py) and [different AUTHOR verifier](verify_complete_four_coset_next_half_screen.py) completed the entire64-case scope without repair.
The verifier uses separate GF(2) matrix/coefficient checks, accepted-Theta multiplication with distinct arithmetic, faithful degree288 Laurent original arrays and SymPy direct ambient-source evaluation.
The programs remain AUTHOR implementations; the separate [whole independent R1051](../../../audits/reviews/Yin_R_G1051_v1.md#whole-finding) reproduced all64 cases and checked the complete fixed mathematics, native payload and every statement value.

Required files in this J output home are joint_eighth_second_half_kernel_image.json and its verification, plus complete_local_target_second_half_screen.json and its verification.
They supply exactly the adopted C828 complete59/57 kernel/reference data and C825 original reference data.
The new programs do not regenerate the old4193/6310 image.
They check all59 coefficient/image reductions, both actual null words, all64 selected representatives and all448 original mod8 arrays with true integer prime division and complete weights.
Actual selected q values and final0..959 kernel exponents pay their complete degrees; old R_i literal bundles remain unchanged.

Both executed reproduction commands require those four retained inputs, with the producer preceding its verifier:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/complete_four_coset_next_half_screen.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_complete_four_coset_next_half_screen.py
~~~

The complete producer certificate (`mathematics/computations/outputs/Yin_J_G0132/complete_four_coset_next_half_screen.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/complete_four_coset_next_half_screen_verification.json`) agree on the full mathematical payload.
The actual computation has129 labels,387 factor values,9150 powers and17444 literal occurrences, and respects the input-derived caps129/387/31728/17536, respectively.
All64 next-half systems retain all256 source images and both-sign target certificates.
No exact elapsed time or peak memory was measured.

The exact result is32 negative Theta fibers and32 ambient members, with two members in every old fiber.
Thus no additional entire old Xi fiber is excluded, and no full X4 or actual Sigma2 attainment is established.
All64 selected words pass F8 with only v2(F)>=3 and fail both complete X4 gates with v2(X_plus)=v2(X_minus)=1.
Their complete original trace degrees range from61761887 to102098754; this is only the range of the selected words, not a degree optimum.
The full inputs are reducible cyclotomic polynomials of total logarithmic Mahler measure0.
No higher group image, other word choice, optimization, F/8 class, modulo16 or full cofactor expansion is part of this phase.

<a id="full-second-half-ambient-screen"></a>
## Complete full-second-half ambient screen: complete author verification

The complete combined result is fixed in [adopted C836](../../../claims/Yin_C_G0836_v1.md#decision-whole-reviewed-2026-10-28), through [whole independent R1056](../../../audits/reviews/Yin_R_G1056_v1.md#whole-finding).

[Adopted C834](../../../claims/Yin_C_G0834_v1.md#decision-whole-reviewed-2026-10-28) supplies the complete60-bit source bound and conditional whole-family implication.
Its symbolic proof has [whole independent R1054](../../../audits/reviews/Yin_R_G1054_v1.md#whole-finding); that review does not cover the later native values.
The [producer](full_second_half_ambient_screen.py) and [different AUTHOR verifier](verify_full_second_half_ambient_screen.py) completed the declared entire scope without repair.
[D6 SP1--SP3](../../../drafts/Yin_D_G0006.md#full-second-half-ambient-screen-preparation) retains the exact selected input and certificate scope.

The required inputs are complete_four_coset_next_half_screen.json and complete_four_coset_next_half_screen_verification.json in this J's output home.
Select exactly their32 prior ambient-member reference cases after comparing all64 input bindings.
Compute all60 columns from each reference's actual beta/gamma/delta, and test BOTH genuine full112-bit normalized half targets.
Retain all1920 columns, complete image bases and both span certificates, all64 ambient preimages or separators and the s=1 sign-translation identity.
Canonical epsilon lifts are mandatory.
No actual cofactor attainment, new group/weight image, original residual probe, larger modulus or profile is included.

The executed reproduction commands are:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/full_second_half_ambient_screen.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_full_second_half_ambient_screen.py
~~~

The complete producer output (`mathematics/computations/outputs/Yin_J_G0132/full_second_half_ambient_screen.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/full_second_half_ambient_screen_verification.json`) agree on all32 mathematical case records.
Each image has rank48 and all64 full targets are ambient members.
There are no new Theta exclusions or entire-old-fiber exclusions and no actual correction or full X4 witness.
This ambient method limit is adopted as one phase of C836; the separately complete actual-word image below supplies the attainment decisions.

<a id="full-fourth-gate-known-word-span"></a>
## Actual old-alphabet full-fourth-gate source span: complete author verification

The complete combined result is fixed in [adopted C836](../../../claims/Yin_C_G0836_v1.md#decision-whole-reviewed-2026-10-28), through [whole independent R1056](../../../audits/reviews/Yin_R_G1056_v1.md#whole-finding).

The [small-source result and scope](../../../drafts/Yin_D_G0006.md#small-source-full-gate-span-preparation) retain the exact complete native scope and limits.
[Adopted C834](../../../claims/Yin_C_G0834_v1.md#decision-whole-reviewed-2026-10-28) supplies the full source-response formula; [adopted C835](../../../claims/Yin_C_G0835_v1.md#decision-whole-reviewed-2026-10-28) supplies the source character and complete old-alphabet presentation.
The [producer](full_fourth_gate_known_word_span.py) and [different AUTHOR verifier](verify_full_fourth_gate_known_word_span.py) completed the entire scope without repair.
Their complete output (`mathematics/computations/outputs/Yin_J_G0132/full_fourth_gate_known_word_span.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/full_fourth_gate_known_word_span_verification.json`) agree on every selected mathematical payload.
The source rank is53, all32 projected ranks are44, and32 full targets are attained while32 are absent.
Positive corrections have complete actual words and costs; negative results have the exact old-alphabet scope, not full-M force.

Required inputs in this J's output home are joint_eighth_second_half_kernel_image.json and its verification, plus complete_four_coset_next_half_screen.json and its verification.
These are the exact adopted C828/C831 mathematical inputs; the later ambient-screen native ranks are not a premise.
The new producer reconstructs all4193 labels in two actual source rings (8386 values), all45/92 lifts,6310 recipes,59 basis constructions and6369 actual Theta-kernel words, then one complete60-coordinate span and all32 reference maps/both full112-bit targets.
It retains every zero/repeated word, all literal exponent bindings and all span reductions, with full factor costs for selected basis and positive correction words.
Actual q values pay degrees; final exponent reduction is modulo960, not480.
No full original product, new original-mod8 probe, larger profile, new full-M alphabet or optimization is included.

The executed producer and different-verifier reproduction commands are:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/full_fourth_gate_known_word_span.py --max-seconds 1800 --max-working-mib 1024
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_full_fourth_gate_known_word_span.py --max-seconds 1800 --max-working-mib 1024
~~~

The completed outputs are full_fourth_gate_known_word_span.json and full_fourth_gate_known_word_span_verification.json in this J output home.
The producer publishes it atomically after complete success and uses a single full_fourth_gate_known_word_span.incomplete.json checkpoint for a completed stage if a later failure occurs.
The default elapsed/own-process peak-working-set caps are30 minutes/1GiB; actual resource observations remain in the completed outputs.
The different implementations remain AUTHOR work; R1056 supplies the separate whole independent inspection and complete reproduction of all three verifier phases.
No original-mod8 corrected-product probe was part of this source-span phase.

<a id="canonical-two-sign-full-gate-products"></a>
## Two literal canonical203/0 full-gate products: complete author verification

The [two-product Preparation](../../../drafts/Yin_D_G0006.md#canonical-two-sign-full-gate-products-preparation) retains the exact source selection and mathematical/global-gate limits.
The required tracked input is [inputs/full_fourth_gate_canonical_products.json](inputs/full_fourth_gate_canonical_products.json), which binds both203/0 corrections to the completed full_fourth_gate_known_word_span.json and its verification.
Both literal products preserve R's69/72/127 bundles and their respective164/163-term correction, giving432/431 occurrences, degrees181259583/181259103 and reciprocal degrees362519166/362518206.
Their exact integer difference is multiplication of the minus product by(X-2)^480; C863 is a separate check, not a substitute for either actual calculation.

The [producer](full_fourth_gate_canonical_products_mod8.py) and [different degree288 Laurent verifier](verify_full_fourth_gate_canonical_products_mod8.py) completed the exact two-product scope without repair.
The combined statement and full proof are fixed in [adopted C836](../../../claims/Yin_C_G0836_v1.md#decision-whole-reviewed-2026-10-28), through [whole independent R1056](../../../audits/reviews/Yin_R_G1056_v1.md#whole-finding).
Both original F8 gates pass; each selected X has coefficient valuation exactly2, its opposite sign exactly1, and G is odd.
Only v2(F)>=3 is certified, with no F/8 class or modulo16.
The complete input-derived cache scope is495 factor values,1263 powered values and2589 explicitly bound literal-prime occurrences, with all14 original arrays and both full signs.
True base/J prime divisions use numerator precisions16,24,40 before integer division; all actual q and original exponents remain unchanged.
The complete producer output (`mathematics/computations/outputs/Yin_J_G0132/full_fourth_gate_canonical_products_mod8.json`) and different verification (`mathematics/computations/outputs/Yin_J_G0132/full_fourth_gate_canonical_products_mod8_verification.json`) agree on all selected mathematical payloads.
All incomplete checkpoints were removed after successful atomic publication.
The default30-minute/1GiB caps are bounds, not measured resource use.
No other word, full-M image, F/8 class, modulo16, optimization or full high-degree polynomial is included.

The executed reproduction commands are:

~~~text
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/full_fourth_gate_canonical_products_mod8.py --max-seconds 1800 --max-working-mib 1024
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0132/verify_full_fourth_gate_canonical_products_mod8.py --max-seconds 1800 --max-working-mib 1024
~~~

The separately [adopted C837](../../../claims/Yin_C_G0837_v1.md#decision-whole-reviewed-2026-10-28) proves nonvanishing and a uniform effective logarithmic original-F precision bound for the ENTIRE fixed cofactor monoid.
It is a symbolic theorem using the accepted Yu99 statement with its original proof unreviewed, not a new J132 computation or a tighter precision measured by these mod8 arrays.

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
| `augmented_endpoint_kernel_image.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1046_v1.md#whole-finding) |
| `augmented_endpoint_kernel_image_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1046_v1.md#whole-finding) |
| `complete_four_coset_next_half_screen.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1051_v1.md#whole-finding) |
| `complete_four_coset_next_half_screen_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1051_v1.md#whole-finding) |
| `complete_local_target_second_half_screen.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1046_v1.md#whole-finding) |
| `complete_local_target_second_half_screen_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1046_v1.md#whole-finding) |
| `endpoint_full_triple_image.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1046_v1.md#whole-finding) |
| `endpoint_full_triple_image_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G1046_v1.md#whole-finding) |
