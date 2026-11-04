---
author: Yin
---
# Independent finite review of the fixed-2d prescribed-C155 energy test

Date: 2026-10-18T08:06.
Human record author Yin.
The main agent separately assigned this review of the four-input J97 calculation under Yin's bounded G0001 resumption.
The reviewer did not select the inputs or develop the author program.
The review covers the completed J97 program, input, mathematical reduction and finite results as read on this date; it is not a Task-completion review or a new whole-proof review of C155.

The arrangement is non-blind.
Shared conversation context, the prescribed test specification, C153v2/C155 interfaces, the author's output schema and subsequent numerical result summary were available before initial findings.
The reviewer implemented the checker from the fixed polynomial inputs, without importing main.py or using its generated values as arithmetic generators.
After the separate arithmetic had passed, the reviewer read the whole author program and completed README, checked its stated table and interval consequences, and supplied the quadratic hand calculation as an explanation of the verified result.
Both programs use the same installed SymPy 1.14.0 for rational irreducibility checking; the independent value, remainder, norm, root-count, interval and linear-system calculations use separately implemented Fraction arithmetic.
This is a separately organized computational review with that shared-library boundary, not formal verification or human proof inspection.

The author's subsequent numerical-result summary was explicitly supplied before the initial findings, beyond the fixed polynomial inputs and prescribed test definitions.
The separate Fraction reconstruction, whole-fiber checks and successful arithmetic execution remain independent implementations, rather than an isolated mathematical-review context.
The affected finding relationships are self-reviewed under the current context rule.
Original independence declarations in the retained narrative describe historical wording; performed checks, dates, exact inputs, verdicts and limits remain unchanged.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite computational finding](#fixed-2d-finite-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite computational finding](#fixed-2d-finite-finding) | [J97 finite reduction and results](../../computations/programs/Yin_J_G0097/readme.md#finite-results) | Four exact minimum energies, the surrounding whole-fiber reduction, five circle-contact enclosures, same-value exclusions and stated limits in the completed README. |
| [Finite computational finding](#fixed-2d-finite-finding) | [Fixed original inputs](../../computations/programs/Yin_J_G0097/input.json) | Exactly the ordered degree-2, degree-4 Salem, degree-4 radical and degree-10 Lehmer inputs, window multiple 2 and threshold 4. |
| [Finite computational finding](#fixed-2d-finite-finding) | [Author program](../../computations/programs/Yin_J_G0097/main.py) | Complete finite construction, eligibility checks, trace-phase lift, rational optimizer, norm comparison and exact circle intervals. |
| [Finite computational finding](#fixed-2d-finite-finding) | [Separate checker](../../computations/programs/Yin_J_G0097/verify.py) | Original-field reconstruction, exact payload comparison, rational Sturm verification and certificate identities; no import of the author program. |
| [Finite computational finding](#fixed-2d-finite-finding) | [C153v2 trace interface](../../claims/Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | Actual trace degree, integral quotients, original-field phase identities and eligibility interface only. |
| [Finite computational finding](#fixed-2d-finite-finding) | [C155 original value](../../claims/Yin_C_G0155_v1.md#original-polynomial-return) | Prescribed h and original norm floor on its actual totally-real trace domain; prior accepted whole proof is not re-audited here. |
| [Finite computational finding](#fixed-2d-finite-finding) | [C16 least-representative identity](../../claims/Yin_C_G0016_v1.md#weighted-quotient-lattice-certificate) | W=I and the prescribed residue specialization, checked directly by the orthogonal-fiber identity below. |
| [Finite computational finding](#fixed-2d-finite-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0097/readme.md#recorded-runs) | Every declared input, trace/defect/target vector, A and Gram entry, dual and minimizing vector, exact energy, norm and root/value interval in the complete finite payload. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0097/results.json`; this target locates that original run's computation account. |
| [Finite computational finding](#fixed-2d-finite-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0097/readme.md#recorded-runs) | Actual successful independent reconstruction of all four inputs and all five contacts; generated evidence remains reproducible local output. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0097/verification.json`; this target locates that original run's computation account. |

<a id="fixed-2d-finite-finding"></a>
## Finite computational finding

**PASS for the four exact fixed-window energy certificates and the five original-circle contact certificates, at the stated finite scope.**
All four energies are strictly above 4.
For each of these four inputs, every rational scalar polynomial representative of the same h supported in degrees 0 through 2d-1 has coefficient energy above 4 and therefore cannot have circle supremum below 2.
For the quartic Salem and degree-ten Lehmer inputs, original-circle contacts additionally exclude circle supremum below 2 for every polynomial or Laurent representative of that same residue, regardless of window length.
There is no conclusion for an untested input or a degree-uniform class.

### Obligations and decisive checks

| Obligation | Actual verification and conclusion |
| --- | --- |
| Fixed scope and original eligibility | The checker independently hard-binds the four ordered integer coefficient arrays and names and compares the native input and result scope against them. Monicity, constant 1, even degree and reciprocity hold. Exact rational irreducibility is checked through SymPy. A separately implemented rational Sturm sequence counts all r distinct trace roots as real and finds at least one outside [-2,2], proving that these irreducible original polynomials are noncyclotomic. |
| Actual trace field | The recurrence reconstructs T from reciprocal coefficients and verifies T(alpha+alpha^(-1))=0 in Q[t]/(P). Irreducibility and the nonidentity reciprocal involution give [K:F]=2 and [F:Q]=r as in C153v2; the r real roots therefore establish total reality of the actual F. No total-reality assumption is inferred from reciprocity alone. |
| Prescribed Frobenius value | In the original quotient, the checker forms P(alpha^p)/p and multiplies by alpha^(-rp), for p=2,3,5. It verifies alpha's inverse, nonzero integral original coordinates and the coordinates of those values in the trace-power basis. It then forms e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5 and h=e^2+f^2+g^2 before comparison with the author trace construction. All coefficients agree exactly. |
| Complete window and residue | Custom polynomial division reconstructs all 2d remainder columns independently. Their first d columns are I_d, and the target vector is the full integral original residue of the reconstructed h. There is no minimization over other residue vectors or use of an abstract triple. |
| Whole-fiber optimum | Custom rational elimination gives y with G y=r_h, x_*=A^T y, A x_*=r_h and E=x_*^T x_*=r_h^T y. Since G=A A^T is positive definite, every legal x=x_*+v has A v=0 and x_*^T v=0, hence x^T x=E+v^T v. This proves the minimum over the whole affine fiber. |
| Norms and threshold | Independent multiplication-matrix determinants recover both full norms, with Norm_K(h)=Norm_F(h)^2>=2^d. Exact rational subtraction gives E-4>0 in each case. No decimal sign comparison or reduced-own-field norm substitutes for these tests. |
| Circle contacts | Rational Sturm counts verify each supplied root interval and all roots' coverage, including ordering, disjointness and the declared width. Independent rational interval Horner evaluation reproduces every h enclosure. The five intervals inside (-2,2) correspond to original unit-circle conjugates, and all five have h>2. The displayed strict integer enclosures were checked against those exact rational bounds. |

The exact energies in the fixed input order are

    14887127520653722/5,
    663452827142605678890/119,
    37858731121859357017433378/65,
    1656102182918999/2943.

For the quadratic control, z=3 gives (a,b,c)=(2,5,24), (e,f,g)=(17,1056,7574) and h=58480901.
The two remainder rows are (1,0,-1,-3) and (0,1,3,8), so G has rows (11,-27) and (-27,74), determinant 85 and E=(74/85)h^2.
This direct illustration agrees with both programs and preserves the prescribed value.

For the quartic Salem input the unique interior trace root has 152<h<153.
For the Lehmer input the four interior trace roots, in increasing order, have h in (1720721,1720722), (2034,2035), (12907,12908) and (8,9).
At each such trace root z, the roots of t^2-z t+1 are on the unit circle and are original roots of P=t^r T(t+t^(-1)).
Equality modulo P forces every value-preserving representative to attain the same h there; this proves the stated window-independent obstruction.
The quadratic and radical quartic have no such contacts, so only their fixed-window energy conclusion is supported.

### Execution facts, source scope and limits

The first checker comparison stopped after two inputs because the author records every trace vector with r coordinates while the checker had trimmed trailing zeros.
Inspection established exact agreement of the values; the checker was corrected to retain the same declared trace coordinates, without changing the fixed inputs, arithmetic target or accepted tolerance.
The completed subsequent invocation passed all four inputs and five contacts; a later completed invocation also checked the fixed input declaration and complete interval coverage explicitly.
The main program and final README were inspected after the arithmetic reconstruction passed.
The completed review found no mathematical discrepancy or required correction.

The finite computation's established interfaces are the existing C153v2 trace construction, C155 value and C16 orthogonal-fiber formula; their stated uses were checked here.
The exact C155 domain was verified on each input, and its predicted norm floor was independently computed there.
This review does not repeat the full C155 field theorem or audit SymPy's factorization implementation.
No new external theorem, attribution claim or literature search is used to obtain the finite result.

The scalar energy argument uses normalized Haar Parseval: ||f||_infinity<2 would imply sum |x_k|^2<4.
All four certified lower bounds exclude that strict supremum certificate in their specified windows, but four finite failures cannot prove an all-input barrier or coverage of sufficiently small positive Mahler measures.
The original-circle obstruction concerns these same prescribed values; it does not exclude logarithmic methods or a different value with a new arithmetic justification.
No least-energy supremum optimization, correlation search, enlarged sample or larger coefficient window was performed by the reviewer.
The original unrestricted G0001 target remains unresolved, and this finding grants no execution authority beyond the bounded test and closeout.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
