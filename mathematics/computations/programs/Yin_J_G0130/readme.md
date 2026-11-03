---
author: Yin
---
# Full multiplicity-sixteen support membership at two prescribed parities

Human author Yin.
Root assigned this exact finite preflight; paid_comparison prepared the contract and two author implementations from the retained J129 mechanisms.
Same_trace supplied a bounded author-side algebraic sanity check of the periods, representatives, group exponent and insertion counts, without executing a program.
These are author contributions, not independent review.
Status: the declared generation and separate author verification both completed after explicit execution authorization.
Both prescribed full targets are nonmembers of the complete image.
Their original mathematical consequence remains subject to fresh isolated whole review and the responsible fixed Claim decision.

## Question and scope

Work ONLY in F_2[X], with

    phi=X^2+X+1, chi=Xphi^2,
    M=X^32phi^64, M_pre=X^32phi^65.

The fixed [C649v1 HC6 at eta=0](../../../claims/Yin_C_G0649_v1.md#statement), actually adopted by its [selected whole-review decision](../../../claims/Yin_C_G0649_v1.md#decision-whole-reviewed-2026-10-23), prescribes exactly two targets, epsilon=0,1, in that order:

    Y=1+X^16 modulo X^32,
    Y=X^8+epsilon X^24(X+1)^64phi^32 modulo phi^64.

They are the unique CRT classes at degree below160.
Test their membership in the image of EVERY complete odd-order trace polynomial W_n, n>1 odd and n!=5, at arbitrary finite nonnegative multiplicities.
Here W_n is the monic polynomial whose roots are all traces zeta+zeta^(-1) of primitive nth roots in an algebraic closure of F_2, taking one root for each inverse pair.
The full primitive-order group is used, rather than a selected irreducible factor.
No other A_0, complement eta, modulus, order cutoff, coefficient search or precision extension is authorized here.
The full surviving original complement is B=X^24, but this finite membership question is not an original characteristic-zero realization question.
Both outcomes and complete certificate vectors must be retained.
If a target is positive, retain the returned640-coordinate nonnegative vector only; do not append an invisible factor, expand a huge witness, construct a canonical support representative or choose integer layers.

## Complete finite reduction

Use A=[[X,1],[1,0]], B_1=1, B_3=X+1 and B_(n+2)=XB_n+B_(n-2) for odd n>=3.
The exact identities are

    A^2=XA+I,
    A^64-I=X^32A^32,
    A^5-I=phi[phi A+(X+1)I].

The second follows by five successive squarings of A^2-I=XA.
For the third, Cayley reduction gives A^5=(X^4+X^2+1)A+X^3I, with phi^2=X^4+X^2+1 and X^3+1=(X+1)phi.
Hence A^640-I is divisible by phi^128, by taking the128th power of A^5-I.
It is also divisible by X^32, since A^64=I there and640=10*64.
The two coprime factors show A^640=I modulo BOTH M and M_pre.
This is a proved common period, not a minimal-period assertion.
One matrix step advances the odd B index by2, so B_(n+1280)=B_n in both quotients for all positive odd n.

There are exactly512 ordinary rows B_n, n odd,1<=n<1280 and5 not dividing n.
Use the global representative m=n unless3 divides n, in which case m=n+1280.
Every such m is coprime15, m<=2559, and B_m has the same whole class modulo M_pre.

There are exactly128 divided rows D_(5r)=B_(5r)/phi, r odd,1<=r<256.
For each r, choose the least k in{0,1,2} with ell=r+256k coprime15 and take m=5ell.
Because256 is1 modulo3 and5, these three choices lose exactly one candidate to divisibility by3 and at most one to divisibility by5.
Thus a permitted ell always exists, ell<=767,m<=3835, and m=5r+1280k.
The exact identity D_(5ell)=B_ell(chi) holds for ell coprime5.
To see the whole identity, put X=z+z^(-1) in F_2[z,z^(-1)] and use the geometric-sum form of B_n.
The quotient B_(5ell)(X)/B_5(X) is the symmetric sum with exponents 5j for -(ell-1)/2<=j<=(ell-1)/2, which is B_ell(z^5+z^(-5)).
Since z^5+z^(-5)=X^5+X^3+X=chi and substitution into the Laurent ring is injective, this proves the polynomial identity.
The verifier reconstructs this identity as a WHOLE polynomial for every chosen divided representative, not only its jets.

For every odd n divisible by5 the complete B_n has EXACTLY one phi factor.
Indeed the nontrivial nth roots of unity are simple in characteristic2, and inversion pairs give all distinct trace roots; phi is precisely the complete primitive-order5 trace group.
Before dividing, reduce B_n modulo the FULL M_pre.
If B_n=R+M_pre Q, then phi divides R and

    B_n/phi=R/phi+M Q.

Thus exact polynomial division of R by phi gives its class modulo M while preserving the entire low-X component.
No inversion of phi in M_pre is performed.
Reducing only the phi component and ignoring the low-X quotient would not establish this question.

For all odd n, B_n=product_(d|n,d>1)W_d.
If5 does not divide n, its B_n class occurs in the512-row list by the proved period.
If5 divides n, D_n=B_n/W_5 is the product of every allowed W_d for d|n and its class occurs in the128-row list; D_5=1.
Strong induction on n, removing the proper-divisor factors in the finite unit group, therefore recovers every allowed W_n from these640 rows, including arbitrarily high powers of5 in n.
Conversely every selected whole representative is a product of allowed W_d and omits W_5.
Each is a unit at phi and has constant coefficient1, so is a unit at X.
Consequently the640 rows generate the EXACT all-order image, not an image truncated at source order3835.
The upper representative bound is a finite-generation certificate, not a support-order restriction on the original problem.
The nonnegative-multiplicity image equals this subgroup because all units have finite order.

The generator uses the recurrence modulo M_pre.
The separate verifier reconstructs whole B_n and B_m from their symmetric Laurent identity

    B_n(z+z^-1)=sum_(j=-(n-1)/2)^((n-1)/2)z^j.

Triangular inversion in powers of z+z^-1 uses only the exact characteristic-two binary-product expansion.
It checks the original and chosen representative modulo M_pre, then exact division, and the full B_ell(chi) identity.
No generated result from J129 is an input.

## Finite group algorithm and complete bounds

The target ring is the product of F_2[X]/X^32 and F_2[X]/phi^64.
Its unit group has order

    2^31 * (3*4^63)=3*2^157

and exponent192: its principal-unit exponents are32 and64 and its residue-field factor has order3.
The exponent192 is used ONLY for units in M or its two factors.
The phi^65 component of M_pre instead requires principal exponent128; no192-based inverse is used there.
There are31 low-X principal coordinates and126 phi-principal coordinates, the latter using basis1,X in each order1 through63.

The exact order-three factor is t=(X+1)^64 modulo M.
It is1 modulo X^32, has nontrivial residue of order3 and satisfies t^3=1, since(X+1)^3=1+Xphi.
It is supplied by the ordinary n=3 row, whose chosen whole representative is B_1283.

Remove each row's residue-field factor using t, then insert its principal unit in increasing filtration order.
At its first nonzero coordinate, either cancel by an existing pivot or install that unit as a new pivot.
Queue the square of each newly installed pivot exactly once.
Every cancellation strictly increases the first nonzero coordinate; a square also increases it or becomes1.
There are at most157 pivots,640+157=797 insertion events,157 cancellations per event and314 total cancellations for the two targets.
Each full pivot and target expression has640 exponents in{0,...,191}.
No enumeration of the ambient3*2^157 group is performed.

The full certificate records all original indices, chosen representatives and predivision remainders, all640 resulting units, the order-three element, every pivot and its complete exponent vector, generator and pivot-square reductions, and both targets' exact CRT components, returned vectors, cancellation traces and residuals.
The generator checks its pivot expressions, square closure, original-generator reductions and each target product identity before publication.
The verifier independently checks all these mathematical data without importing the generator arithmetic or rerunning the insertion algorithm.
Distinct first coordinates make all binary pivot products different.
Square closure makes them a subgroup by carrying to higher coordinates, and every original generator reduces into it.
Since every pivot also has a checked expression in the original generators, this proves exact subgroup equality and order3*2^(number of pivots).
A target's remaining first missing coordinate proves nonmembership; residual1 and its full vector prove membership.
This normal-form proof is the reason the certificate is complete.

## Files

The two executed implementations are [main.py](main.py) and [verify.py](verify.py) in this J program home.
Main uses bit-packed characteristic-two arithmetic, the recurrence, finite-exponent inverses in M, and pivot insertion.
Verify uses coefficient arrays, carry-free integer-packed dense convolution, Euclidean inversion and whole symmetric-Laurent traces; it never imports main.py or constructs the subgroup by insertion.
These are separate AUTHOR implementations, not independent agent review.
The prior [J129](../Yin_J_G0129/readme.md) code and analytic reduction are reused as mechanisms only; its programs and outputs remain unchanged, and its old membership outcomes are not inputs here.
The generated complete certificate (`mathematics/computations/outputs/Yin_J_G0130/certificate.json`) and second author verification (`mathematics/computations/outputs/Yin_J_G0130/verification.json`) are actually retained in this J's output home.
The certificate contains all 640 row definitions and values, all 152 pivot values and complete vectors, every source/square closure trace and both complete target vectors and residuals.

## Reproduction

The following commands were actually executed, in this order, from the repository root under the responsible main agent's explicit instruction:

```powershell
python mathematics/computations/programs/Yin_J_G0130/main.py --execute --max-seconds 1800
python mathematics/computations/programs/Yin_J_G0130/verify.py --execute --max-seconds 1800
```

Each entry requires --execute to start arithmetic; imports and a missing execution flag do not calculate the group.
Python standard-library exact arithmetic only, no randomness or tolerance; ordinary non-optimized Python is required.
Each program has a default 1800-second live deadline, with --max-seconds restricted to integers from 1 through 7200, and aborts without publishing a new complete result if a limit or check fails.
The generation command requires no generated prior input.
The verification-only command requires this J's actual certificate.json and refuses an absent file.
It rejects an input larger than 64 MiB before parsing.
Source and output paths resolve from this program home, independently of the working directory.
The declared output home is mathematics/computations/outputs/Yin_J_G0130/.
An authorized generation creates certificate.json; the subsequent author verification creates verification.json.
Preflight itself produced no output; the linked files were generated only by the authorized executions.
The output directory is created only when a program reaches publication after completing its mathematical checks; a failed write may leave an empty directory.
Complete JSON publication is atomic; any pending-write file stays in that same output home and is not a successful certificate.
There is no checkpoint or partial-result resumption interface.
Once generated, these two outputs may be replaced by the same declared commands only when their actual consumers remain coherent.

## Results and limits

The generator and second author checker completed all declared checks with exact arithmetic.
The complete image has 152 pivots, order 3*2^152 and ambient index 32.
Its missing ordered principal coordinates are exactly 36,44,60,92,156.
Generation used 792 insertion events and 20877 insertion cancellations, within the predeclared bounds.
All 640 source reductions, 152 complete pivot expressions and 152 pivot-square closures passed the separate implementation.

With bit i denoting the coefficient of X^i, the complete results are:

| epsilon | Full CRT target | Final residual | Membership |
| --- | --- | --- | --- |
| 0 | 0x1010100000000000101010000000000010001 | 0x56ace74b76e70f3ec03c62884dfd331800000001 | false |
| 1 | 0x1010101000000010101010100000000010001 | 0xe0778afdad8bb9e51b50d453204ae87500000001 | false |

Both targets use the same retained 640-coordinate expression vector and 38 pivot cancellations, stopping at missing coordinate 92, the X coefficient in phi order 31.
For each target the certificate and checker establish target=(full generator-vector product)*residual modulo M, together with the complete normal-form obstruction.
No declared check failed or timed out.
These are two author implementations, not independent agent review.
C649v1 is an adopted fixed proof input; the original A_0=16 exclusion uses its complete hypotheses and actual factor bridge, followed by this verified all-order obstruction.
It still requires the new fixed result's own applicable whole review and adoption.
The full fixed statement, analytic certificate argument and original consequence are retained in [C651v1](../../../claims/Yin_C_G0651_v1.md#statement), initially open for that review.
No characteristic-zero P/T, all-primary canonical witness, nonsquareness, maximal q or original layer realization is constructed.
No A_0=14 input, other modulus, additional order search, invisible-factor insertion or huge witness construction is part of this contract.

## Inspection summary

The author read both prepared programs and checked the targets against actual C649v1 HC6 at eta=0 and its selected adoption decision.
The all-order reduction, common periods, exact predivision step, unit-group exponent, complete normal form and finite insertion bounds were checked analytically before execution.
The two implementations retain separate polynomial arithmetic, whole-row construction, inversion and CRT recombination paths.
The second implementation checks the mathematical normal-form certificate and recorded resource-bound consistency; it does not reproduce the generator's insertion history or certify an observed running time.
Before authorization, both source files passed AST syntax parsing as text without importing or executing either module, and the output home was absent.
After explicit authorization, the two declared commands executed sequentially and the author read their complete summaries and actual certificate fields at the declared scope.
The verifier reported verified=true for all 640 reconstructed rows, both matrix periods, all 152 pivot expressions and square closures, all 640 source reductions and both full target product identities.
The material structure check supplies no mathematical review; the author inspections and second implementation do not supply an independent agent relationship.

## Independent whole reconstruction and adoption

The distinct reviewer retained [its reconstruction contract](reviewer_contract.md) before native execution and before inspecting the author implementations.
The [independent program](reviewer_check.py) uses whole binomial Fibonacci-polynomial reconstruction, four-coefficient convolution, Euclidean inverses and Bezout CRT, without author imports or earlier-J native inputs.
Its actual successful result (`mathematics/computations/outputs/Yin_J_G0130/reviewer_verification.json`) checks every640 source row/lift, all152 complete pivot expressions and square closures, all640 source reductions, both full CRT/product identities and the reported insertion statistics.
Both targets again stop after38 cancellations at missing coordinate92.
The entire mathematical/native finding is [R861](../../../audits/reviews/Yin_R_G0861_v1.md#whole-a16-full-support-native-finding).
After reading the entire C and R and actual independent result, main adopted [C651](../../../claims/Yin_C_G0651_v1.md#decision-whole-reviewed-2026-10-23) at2026-10-23T22:53.
Author execution history remains distinct from the reviewer's actual reconstruction; neither program supplies an original realization or unrestricted Task completion.

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0861_v1.md#whole-a16-full-support-native-finding) |
| `reviewer_verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0861_v1.md#whole-a16-full-support-native-finding); [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0866_v1.md#whole-density-refined-finite-character-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0861_v1.md#whole-a16-full-support-native-finding) |
