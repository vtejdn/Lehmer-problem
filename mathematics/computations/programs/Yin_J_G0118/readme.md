---
author: Yin
---

# Exact zero-middle two-update bridge screen

## Question and scope

Certify the complete 81 ternary middle patterns satisfying the necessary two-real-strip conditions for a two-update bridge between actual quartic zero-middle fibers.
Use the exact algebraic root of P=t^4-t^3-t^2-t+1 enclosed by specified rational endpoints, and integer arithmetic in Z[t]/(P).
Check the explicit candidate c=-3+3 beta+beta^2-beta^3, its zero-middle strip membership and the proposed conserved integral coordinate.
The complete mathematical exhaustion argument and constructor scope are fixed in [C606v1](../../../claims/Yin_C_G0606_v1.md#argument), whose selected decision owns its assessment.
No carry-length or eigenvalue scan is selected.

## Files

- [inputs.json](inputs.json) retains the exact polynomial, rational root bracket, candidate c and both complete length-24 tail words.
- [main.py](main.py) checks all 81 pattern inequalities, quotient-ring identities, strict witness strips and the complete returned word using integers and rational intervals only.
- [discover.py](discover.py) retains the separately bounded, fixed-length-24 meet-in-the-middle discovery of the two tails.
- [verify.py](verify.py) independently reconstructs all finite certificate obligations by polynomial long division and signed monomial rational intervals, without importing either author program.
- certificate.json (`mathematics/computations/outputs/Yin_J_G0118/certificate.json`) contains all 81 exact interval records, the accepted list, functional coefficients and complete verified word.
- discovery.json (`mathematics/computations/outputs/Yin_J_G0118/discovery.json`) contains the actual fixed-length discovery result and its finite operation counts.
- verification.json (`mathematics/computations/outputs/Yin_J_G0118/verification.json`) contains the separately generated independent exact checks, all 81 interval records, multiplication determinant, kernel generators and complete retained word.

## Reproduction

From the repository root, run `python mathematics/computations/programs/Yin_J_G0118/main.py` with standard Python 3.
No external package, random seed, floating-point arithmetic, temporary directory or pre-existing output is required.
The exact root bracket uses denominator 10^12 and every pattern comparison must resolve strictly; an inconclusive comparison stops with an assertion rather than changing precision or scope.
The fixed output contains 81 records and one complete word and is checked to be smaller than 256 KiB before publication.
Default output resolves from the actual containing J directory to its standard ignored output home.
The same generated certificate may be replaced by reproduction of the same fixed native inputs.

The optional discovery command is `python mathematics/computations/programs/Yin_J_G0118/discover.py`.
It fixes tail length 24, builds only one length-12 endpoint table and searches only the two stated targets; it performs no length scan or scope escalation.
At each intermediate size the table is bounded by the corresponding 3^j word count with j<=12.
Its output is not an input required by main.py, since the actual discovered witness is retained explicitly in inputs.json.

The independent verification command is `python mathematics/computations/programs/Yin_J_G0118/verify.py`.
It requires only the retained inputs.json and standard Python 3, and does not read author-generated output or rerun witness discovery.
It writes the replaceable verification.json in this J's standard ignored output home, resolving that home from its own location.

## Results and limits

The exact certificate completed all 81 patterns, retaining zero and exactly eight nonzero patterns.
They are the signs of (beta-1), beta(beta-1), beta^2(beta-1), and (beta-1)(1-beta^2).
The certified invariant is lambda(c)=2c0+3c1+5c2+9c3, with lambda(-3+3beta+beta^2-beta^3)=-1.
The complete 52-digit witness has n=26, four zero middle digits, 15 zero digits altogether and exact return value zero.
Its unconditional original probability is 2^-89; complete conditioning divides by p_52.

The discovery used 62,029 distinct length-12 endpoints and 165,528 exact candidate operations, and found both stated length-24 tails.
The certificate then checks those retained words directly in Z[t]/(P), rather than trusting the search output.
The discovery and main certificate programs and their original checks are by original_law; that original evidence does not itself assert independent verification.
The analytic proof in the linked fixed Claim establishes why the 81-pattern screen exhausts every one- or two-update bridge between zero-middle events and why its translation subgroup has rank three.
The finite calculation alone does not supply that exhaustion argument.
Neither exclusion of unrestricted sign paths, a total omitted-mass bound, a uniform energy bound nor a critical-mean conclusion follows from this restricted-constructor obstruction.

## Independent verification

A separate reviewer outside the candidate's development wrote and executed verify.py from the fixed statement and native inputs, without receiving the proof-development discussion or a mathematical summary.
All 81 patterns resolved strictly with exactly the same nine retained patterns, including zero.
The independently reconstructed multiplier matrix has determinant -1 and last row (2,3,5,9), and its inverse sends the first three power-basis vectors to the declared kernel generators.
Direct quotient-ring reduction verifies both retained tail endpoints and exact return of the complete 52-digit word.
The word contains exactly 15 zero digits and its independently multiplied original probability is 2^-89.
Both strict real-place witness tests pass and its integral coordinate is -1.
The discovery code and retained discovery output were inspected, but discovery was not rerun; its table and operation counts remain the author's retained diagnostics.
This independent finite check supplies no full original tail-count enumeration, path-conductance estimate, unrestricted connectivity conclusion or source-proof re-audit.
The complete mathematical review, exact native bindings and actual independence relationship are retained in [R809](../../../audits/reviews/Yin_R_G0809_v1.md#short-bridge-whole-independent-finding).

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
| `certificate.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0809_v1.md#short-bridge-whole-independent-finding) |
| `discovery.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0809_v1.md#short-bridge-whole-independent-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0809_v1.md#short-bridge-whole-independent-finding) |
