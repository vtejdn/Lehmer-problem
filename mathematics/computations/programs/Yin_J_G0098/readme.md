---
author: Yin
---
# Certified logarithmic averages of the existing C155 B3 on four fixed inputs

## Question and scope

Yin authorized only the [bounded direct-logarithm diagnostic](../../../tasks/Yin_T_G0001_v1.md#decision-bounded-b3-log-diagnostic-2026-10-18), followed by result organization and renewed pause.
The four unchanged original polynomials are exactly those in [J97's retained input](../Yin_J_G0097/input.json): t^2-3t+1, t^4-t^3-t^2-t+1, t^4-4t^2+1, and t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1.
There is no new input, altered auxiliary, representative optimization or enlarged search.

Use the original [C155 B3](../../../claims/Yin_C_G0155_v1.md#original-polynomial-return), with L=972000, A3 of degree 30d and B3=t^(-15d)A3/L^2.
The three quantities are

    I_P = integral_T log(B3) dmu = integral_T log(Q_P) dmu,
    Lambda_P = log Norm_K(B3(alpha))/d = log Norm_F(h)/r,
    log2, where d=2r and mu is Haar probability measure.

B3 equals the nonnegative real symbol Q_P on the circle, and h=B3(alpha) is the totally positive original trace-field value.
The Haar average is NOT divided by d.
The original-conjugate average retains all d conjugates and every smaller-own-field multiplicity.
The requested error certification concerns these four fixed inputs only.

## Files

| File | Role |
| --- | --- |
| [J97 input.json](../Yin_J_G0097/input.json) | Sole required cross-J original input; both programs hard-bind its four ordered coefficient lists. |
| [main.py](main.py) | Author exact trace reconstruction, positivity check and certified direct analytic quadrature. |
| [verify.py](verify.py) | Separate integer-numerator/resultant reconstruction and certified complete-root Jensen calculation. |
| results.json (`mathematics/computations/outputs/Yin_J_G0098/results.json`) | Author quantity balls, display values, exact trace data and certification parameters. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0098/verification.json`) | Independent exact A3/resultant data, complete root balls with multiplicities, certified means and comparisons. |

The generated output is local and Git-ignored; these programs and the explicit original input reproduce it.
No generated J97 output is an input to either calculation.
The verifier requires the author's J98 results.json for its final comparison, after independently generating its own values.
Author and independent outputs remain distinct.
A complete result is atomically published only after every required check succeeds; partial output is marked incomplete.

## Reproduction

Use the repository Python environment, with python-flint 0.9.0 and SymPy 1.14.0.
From the repository root:

~~~powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0098/main.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0098/verify.py
~~~

Each full invocation has a live 300-second subprocess bound.
Paths resolve from the actual J location, not the caller's current working directory.
There are no random choices or unreported parameter scans.
The author uses 192-bit Arb/Acb arithmetic, absolute and relative integration tolerance goals 1e-18, degree limit 100, evaluation limit 200000 and depth limit 30.
Each reported author scalar has an actual computed ball radius below 1e-12, and its displayed twelve-decimal number is explicitly checked to have absolute error below 1e-10.
The independent calculation uses 256-bit Arb/Acb, root tolerance 1e-40 and maximum root precision 2048 bits.
A tolerance request alone is not a certificate: finite enclosing output balls and their actual radii are checked before completion.

## Exact object and direct-integral certification

For P(t)=t^r T(t+t^(-1)), define C_0(z)=2,C_1(z)=z,C_(n+1)(z)=z C_n(z)-C_(n-1)(z).
For a circle angle theta, put

    a(theta)=T(2cos(2theta))/2,
    b(theta)=T(2cos(3theta))/3,
    c(theta)=T(2cos(5theta))/5,
    e=b^2-a^3, f=2c^2-3a^5, g=c^3-2b^5.

The actual reciprocal phases in [C153v2](../../../claims/Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) and the original H numerators give Q_P(theta)=e(theta)^2+f(theta)^2+g(theta)^2.
In this circle integrand, T(C_p(z))/p is UNREDUCED.
Reducing modulo T is used only to recover the original trace-field value h and its full norm; integrating that remainder instead would change B3 and answer a different question.

The author checks the original polynomial's monicity, reciprocity, irreducibility and noncyclotomic status, the exact reciprocal trace identity, and all r real simple roots of T.
For each input the three unreduced rational defect polynomials have exact gcd 1.
They therefore have no common real zero, and their sum of squares is strictly positive on the entire real trace line, in particular on [-2,2].
No regularization, zero deletion or singular-tail approximation is used.

Q_P is even in theta, so I_P=integral_0^1 log Q_P(pi u) du.
The program integrates this analytic expression with complex ball quadrature at exact endpoints 0 and 1, using an enclosing Arb value of pi.
It forwards the integrator's analytic flag to the complex logarithm, so a complex box crossing the logarithm branch cut or containing a zero is rejected rather than incorrectly declared analytic.
The rigorous real part of the returned integral encloses I_P; its imaginary part contains zero, consistently with the proved real integrand.
The exact rational polynomial construction and the ball integrator's truncation/rounding enclosure supply the error bound, not agreement of two precision levels or a sampled quadrature rule.

The original mean is computed from the exact integer resultant Norm_F(h)=Res(T,h) and Lambda_P=log Norm_F(h)/r.
Every original C155 domain condition and its predicted full norm floor are checked on the four original inputs.
The original mean is not approximated by sampling selected conjugates.

## Separate Jensen and full-resultant certification

The checker independently constructs the C149 integer numerators directly from P(t^2),P(t^3),P(t^5):

    H23=9P(t^2)^3-8P(t^3)^2,
    H25=75P(t^2)^5-64P(t^5)^2,
    H35=250P(t^3)^5-243P(t^5)^3,
    A3=13500^2 t^(9d)H23^2+1215^2 t^(5d)H25^2+32^2 H35^2.

It checks degree 30d, reciprocity and constant/leading coefficient 50176.
Exact squarefree factorization retains every multiplicity and is multiplied back to recover A3.
Certified Acb isolation covers every root of every squarefree factor; the total degree with multiplicity equals 30d.
The reused [scalar Jensen identity](../../../ledger/Yin_L_F0005_v1.md#scalar-capacity-normalization) gives

    I_P=log50176+sum_j log max(1,abs(beta_j))-2log972000,

with every A3 root beta_j counted with multiplicity.
The interval maximum is used for a root ball meeting the unit circle; no uncertified inside/outside classification is needed.
The full original integer resultant gives

    Norm_K(B3(alpha))=Res(P,A3)/972000^(2d).

The centering monomial has norm 1 because the original monic reciprocal polynomial has even degree and constant 1.
Exact division, the full original norm and the trace-norm square are checked.
Both root-Jensen and direct-integral calculations certify their own enclosures; mutual agreement is a separate consistency check.

<a id="certified-results"></a>
## Results and limits

Both finite calculations completed all four inputs on 2026-10-18.
Every decimal displayed below, including each difference, has certified absolute error less than 1e-10.
The reference value is log2=0.693147180560 with the same conservative error bound.

| Input | I_P | Lambda_P | I_P-log2 | Lambda_P-I_P |
| --- | --- | --- | --- | --- |
| Quadratic A3 | 6.491895105819 | 17.884210780264 | 5.798747925259 | 11.392315674445 |
| Quartic Salem seed | 2.972861554749 | 13.379924642415 | 2.279714374189 | 10.407063087666 |
| Quartic radical A4 | 9.130140961688 | 27.396630248517 | 8.436993781128 | 18.266489286829 |
| Lehmer degree10 | 4.568104947597 | 9.483160122619 | 3.874957767037 | 4.915055175023 |

The four exact trace norms are 58480901, 418460896331, 625764150774534826734436 and 391219560896987086331.
The original norms are their squares, with original degrees 2,4,4,10 respectively.
The native output also supplies Lambda_P-log2, all enclosing balls and exact reconstruction data.

All four certified orderings are Lambda_P>I_P>log2.
Thus none of these inputs satisfies the proposed Haar-margin condition I_P<=log2-eta for any positive eta.
The discrepancy Lambda_P-I_P is also strictly positive on each actual input; replacing the original-conjugate mean by the Haar mean would discard the displayed nonzero expense.
These finite observations do not establish a uniform error law as m(P) tends to zero or refute a target restricted to an untested sufficiently-small-positive-measure class.
No sequence approaching zero measure was constructed or sampled.
There is no new Mahler lower bound, refutation of Lehmer's conjecture or Task completion.

## Inspection summary

Root authored the direct-integral program and this account.
A separately assigned reviewer independently reconstructed A3 and its full original resultant, then computed the complete-root Jensen intervals without importing the author program or using author values as generators.
[R375](../../../audits/reviews/Yin_R_G0375_v1.md#four-input-logarithmic-finding) accepts the complete finite diagnostic, exact object and norm identities, certified scalar comparisons and reported error bounds.
It records the shared context and actual independently checked scope.
Both methods use the same installed FLINT Arb/Acb interval primitives; they are independent formulas and implementations, not independent numerical libraries or formal verification.
The existing C155 theorem and scalar Jensen interface are reused at their accepted scopes, without a new audit of their full external proof chains.

## Consequences for the paused handoff

Close this first diagnostic on the four declared inputs.
More digits, repeated quadrature or a larger unchanged sample would not repair the observed failure of the specific Haar-margin condition on these inputs.
Do not use the smaller Haar mean as an upper bound for the original-conjugate mean; the positive discrepancy must remain explicit.
A future authorized continuation would need a justified different input-class hypothesis, a different auxiliary with a new arithmetic-income proof, or a genuinely changed paid logarithmic mechanism.
Those are recommendations only; no such construction or exploration was executed here.
The broad direct-logarithmic route and the unrestricted G0001 objective remain unresolved.

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
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0375_v1.md#four-input-logarithmic-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0375_v1.md#four-input-logarithmic-finding) |
