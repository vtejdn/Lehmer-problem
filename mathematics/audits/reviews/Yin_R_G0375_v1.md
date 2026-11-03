---
author: Yin
---
# Independent finite review of the existing-B3 logarithmic diagnostic

Date: 2026-10-18T08:23.
Human record author Yin.
The main agent separately assigned this review under Yin's bounded G0001 resumption for exactly the four J97 inputs and the existing C155 B3.
The reviewer owns the separate J98 checker and this finding, and did not develop the author direct-integral program.
This is a finite computational and interface review, not a Task-completion review or a new whole-proof audit of C155.

The arrangement is non-blind.
Shared task history, the C155 normalization, the proposed Jensen checking route and the prior R374 finite eligibility findings were available before the new arithmetic.
The reviewer inspected the C149 original numerator formulas, the C153v2 phase/trace interface, C155 Section 2 and the existing F109 scalar Jensen normalization.
The complete independent numerator, resultant and Jensen calculation finished before the reviewer read the author's new program or numerical result payload.
The reviewer then read the whole author program, added exact mathematical-payload comparisons, reran the checker, and inspected the completed J98 README and its displayed table.
Both implementations use python-flint 0.9.0 and its FLINT Arb/Acb primitives; the author additionally uses SymPy 1.14.0 for exact trace algebra and input-domain checks.
Independence here concerns the separately organized reconstruction, formulas, numerical algorithms and code, not independent numerical libraries or formal verification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [J98 account](../../computations/programs/Yin_J_G0098/readme.md#certified-results) | Entire completed account, exact object, both certification methods, all displayed finite quantities, ordering consequences and limits. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [Fixed original inputs](../../computations/programs/Yin_J_G0097/input.json) | Exactly the ordered degree-2, degree-4 Salem, degree-4 radical and degree-10 Lehmer coefficient lists, with no change of original polynomial. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [Author program](../../computations/programs/Yin_J_G0098/main.py) | Whole trace construction, unreduced circle integrand, positivity, full trace norm, analytic ball quadrature and reported scalar error certification. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [Independent checker](../../computations/programs/Yin_J_G0098/verify.py) | Direct integer numerator and full original resultant, exact squarefree factorization, complete isolated-root Jensen sum, exact identity and numerical payload comparisons. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [C149 numerators](../../claims/Yin_C_G0149_v1.md#original-polynomials-and-norms) | H23, H25 and H35 and their exact supplied denominators only. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [C153v2 phase and trace interface](../../claims/Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) | P(t)=t^r T(t+t^(-1)), actual degree r=d/2 and the phases connecting the original polynomial and trace defects. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [C155 original completion](../../claims/Yin_C_G0155_v1.md#original-polynomial-return) | The unchanged B3=t^(-15d)A3/972000^2, positive trace value, full norm identity and scalar logarithmic normalization. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [F109 scalar normalization](../../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) | Accepted scalar Jensen root formula with leading coefficient, all multiplicities and possible circle roots. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [Prior R374 input checks](Yin_R_G0374_v1.md#fixed-2d-finite-finding) | Reused finite eligibility of exactly the same four original polynomials and actual totally real trace fields; no reuse of J97 generated arithmetic as a generator. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0098/readme.md#recorded-runs) | All four inputs, exact defect data and norms, six scalar enclosures per input, displayed decimals and strict signs. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0098/results.json`; this target locates that original run's computation account. |
| [Finite logarithmic finding](#four-input-logarithmic-finding) | [Output of the recorded run](../../computations/programs/Yin_J_G0098/readme.md#recorded-runs) | Complete A3 coefficients, resultants and full norms, every squarefree factor/root ball/multiplicity, certified scalar enclosures and all comparison results. Recorded-run output: `mathematics/computations/outputs/Yin_J_G0098/verification.json`; this target locates that original run's computation account. |

<a id="four-input-logarithmic-finding"></a>
## Finite logarithmic finding

**PASS at the declared four-input scope.**
The direct analytic integral and the separate complete-root Jensen calculation each certify their own enclosures and agree on every requested scalar comparison.
For each input, the certified strict ordering is Lambda_P>I_P>log2.
Every twelve-decimal value in the J98 table has absolute error below 1e-10, including the displayed differences and reference log2.
Thus none of these four inputs satisfies I_P<=log2-eta for any eta>0.
This conclusion concerns these exact existing auxiliaries and inputs; it supplies neither a universal obstruction nor a resolution of the unrestricted Task.

### Obligations and decisive checks

| Obligation | Actual check and conclusion |
| --- | --- |
| Unchanged original input | Both programs hard-bind the four ordered original integer coefficient lists; the checker compares the complete payload names, degrees and coefficients. The original eligibility is already independently covered by R374, and the author freshly checks irreducibility, noncyclotomic status, exact reciprocal trace identity and all r real simple trace roots. |
| Exact original B3 | The checker forms H23=9P(t^2)^3-8P(t^3)^2, H25=75P(t^2)^5-64P(t^5)^2 and H35=250P(t^3)^5-243P(t^5)^3 directly in integer polynomial arithmetic. It constructs A3 using weights 13500^2,1215^2,32^2 and supports 9d,5d,0, then checks reciprocity, exact degree 30d and leading/constant coefficient 50176. |
| Circle integrand identity | From the author's unreduced rational e,f,g coefficient arrays, the checker exactly reconstructs 972000^2 t^(15d)[e(t+t^(-1))^2+f(t+t^(-1))^2+g(t+t^(-1))^2] and compares all coefficients with its independent A3. No reduction modulo T enters the circle integrand. |
| Strict positivity and logarithm | The exact gcd of the three unreduced rational defects has degree zero, independently rechecked using FLINT rational polynomials. Their real sum of squares is therefore everywhere positive on the real trace line. There is no omitted logarithmic singularity, regularization or discarded circle zero for these inputs. |
| Haar normalization and analytic quadrature | The trigonometric expression is even and 2pi-periodic, so its normalized full-circle integral equals the integral over u in [0,1] at theta=pi u. The interval value of pi encloses the true constant. The integrator's analytic flag is forwarded to q.log, enforcing branch/zero checks on complex boxes; the returned finite real ball encloses the real integral, and its imaginary ball contains zero. |
| Complete Jensen certification | Exact squarefree factors multiply back to A3. Each factor's Acb root call succeeds for its entire degree; all returned root balls within each factor are pairwise disjoint, and the sum of degrees with multiplicities is 30d. The rigorous sum is log50176+sum log(max(1,abs(beta)))-2log972000. The interval maximum remains valid even for a root enclosure meeting the unit circle. |
| Full original mean | The independent integer resultant Res(P,A3) is divided exactly by 972000^(2d). Norm(alpha)=1 retains the centering monomial without loss. The resulting full original norm equals the square of the author's positive trace norm and is at least 2^d; log Norm_K/d agrees with log Norm_F/r. No smaller own field, selected roots or missing multiplicities are substituted. |
| Actual error and signs | Both methods return finite enclosures and check actual radii, rather than accepting tolerance requests alone. The checker parses persisted author balls, checks all six scalar signs and ball overlaps, and verifies each displayed decimal against its independent enclosure with strict absolute error below 1e-10. Exact normalization and norm comparisons precede these scalar checks. |

The four A3 polynomials are in fact squarefree, of degrees 60,120,120,300.
The isolated root balls respectively split into 30/30,60/60,60/60,150/150 inside/outside the unit circle, with no unresolved circle overlap in this run.
The checker nevertheless retains general squarefree multiplicities and interval maxima, so the certification does not rely on a guessed root classification.
The complete root balls are reproducible local output, not a floating list promoted to a certificate by decimal agreement.

The exact positive trace norms, in the fixed input order, are

    58480901,
    418460896331,
    625764150774534826734436,
    391219560896987086331.

The direct resultant recovers their squares in the original fields of degrees 2,4,4,10.
The certified I_P-log2 values, rounded to twelve decimals, are 5.798747925259,2.279714374189,8.436993781128,3.874957767037.
The certified Lambda_P-I_P values are 11.392315674445,10.407063087666,18.266489286829,4.915055175023.
These positive lower margins certify the asserted ordering independently of a decision based on rounded table entries.

### Execution facts and limits

The independent initial run completed all four numerator/resultant/Jensen calculations.
After the author payload and complete program became available, one further run added the exact Laurent identity, norm, interval, sign and decimal-error comparisons and passed all four inputs.
There was no failed root isolation, tolerance scan, new polynomial input, auxiliary change, regularization or broadened research search.
Both full invocations have an actual 300-second subprocess cap and atomic complete-output publication; the completed evidence is retained in J98.
The final README was read in full before this fixed finding was created.

The existing C155 theorem, C153v2 field interface, prior finite eligibility and F109 Jensen identity are used at their inspected and accepted scopes; their full proof/source chains are not re-audited here.
FLINT's exact algebra and Arb/Acb's enclosure algorithms are trusted computational primitives, not formally verified within this review.
The author and verifier share that numerical-library boundary, which limits software diversity despite distinct integral and root algorithms.
Overlap of outputs is only a consistency check; each method's actual enclosing arithmetic and mathematical reduction supply its certification.

The finite failure of I_P<log2 on these four inputs does not refute such a condition on an untested sufficiently-small-positive-measure class.
The positive original/Haar discrepancies prohibit replacing the original mean by the Haar mean on these inputs without paying a transfer cost; they do not determine any degree-uniform law as m(P) tends to zero.
No new arithmetic-income theorem, auxiliary, input class, Mahler-gap theorem or Task completion is established.
The README's recommendations are future options only, and this review grants no continuation beyond the authorized finite diagnostic and closeout.

## Reviewed computation runs

The numerical binding rows concern the original runs and outputs identified in their scopes.
Their targets locate those runs' computation accounts and do not assert a check of the present README or a newly reproduced run.
Generated outputs remain local; reproduce the documented program, inputs and parameters and repeat the applicable checks when output verification is needed.
