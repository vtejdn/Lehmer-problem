---
author: Yin
---

# G0001 bounded countersearch for the degree-two Gram window

Host locations in historical commands and records below are normalized; relative historical paths, arguments and execution facts are unchanged.
This records no new run.

<a id="bounded-countersearch"></a>

Date: 2026-10-06.
Human author: Yin; implementation and assessment by the assigned countersearch agent.
This continues the same Task and the exact candidate in [L G0004](Yin_L_G0004_v1.md#degree-window-tests):
\[
|\operatorname{disc}p|G_{2d}>(2d)^d
\]
for monic irreducible reciprocal noncyclotomic unit polynomials of degree \(d\).
Failure of this sufficient finite positivity certificate would not refute Lehmer or the proved lower inequality.

## Fixed scope and reuse before execution

The finite pattern bound is all 3,905 reciprocal coefficient patterns with \(d=2,4,6,8,10\) and independent coefficients in \(\{-2,-1,0,1,2\}\), followed by all 8,748 patterns with \(d=14,16\) and coefficients in \(\{-1,0,1\}\).
Leading and constant coefficients are 1.
Total maximum: 12,653 patterns.
The wall-clock cap is 180 seconds, checked between samples and certification attempts.
A single atomic arithmetic operation may finish after the cap; no additional search batch is authorized by this record.

The existing exact Bareiss determinant, discriminant, orbit Gram and finite-field/trace certification code in L G0004 is reused.
Its complete mathematical arguments and first-batch review were read before this search.
No new external theorem, source acquisition or larger irreducibility method is needed.
This targeted search changes the coefficient/degree windows and reverses the screening order; it does not count unchanged source interfaces as new mathematics.

The program removes any polynomial having a cyclotomic divisor by exact integer division.
Orders up to \(2d_{\max}^2=512\) cover all possible cyclotomic factors of degree at most 16 by L G0004's bound \(\varphi(n)\ge\sqrt{n/2}\).
Such samples cannot be irreducible noncyclotomic core examples.
It then tests squarefreeness by the exact discriminant and computes the finite inequality for every remaining squarefree survivor.
Only failures and eight smallest exact surplus ratios in each completed/prefix window receive attempted irreducibility certificates.
Uncertified failures remain uncertified, never core counterexamples.

The Gram determinant is evaluated from the equivalent Toeplitz relation matrix in L G0004.
Before the search, three control polynomials are checked against its independently implemented orbit Gram determinant.
Ordering of surplus uses exact fractions; no floating-point roots or sign decisions occur.

## Native computation and original review

The [complete original program and JSON](../computations/programs/Yin_J_G0116/readme.md) retain the exact finite inputs, all 12,653 enumerated patterns, every output field and original execution/replay facts.
The actual L4 helper blocks remain required native inputs; their source text is preserved.
The [original coordinating program/replay finding](../audits/reviews/Yin_R_G0799_v1.md#parent-program-and-replay-finding) is retained with its exact finite scope and unknown initial context.
No new run or larger window is performed by this maintenance.

## Execution and assessment

One execution completed the entire finite scope in 6.203 seconds, well before the 180-second cap.
The native interpreter reported CPython 3.12.14.
The process returned exit code 0.
Its complete exact output is retained in [J116 original-output.json](../computations/programs/Yin_J_G0116/original-output.json); the timing is observational, not part of a mathematical comparison.

| Degree | Coefficient height bound | Patterns | Removed for a cyclotomic divisor | Squarefree survivors tested | Positivity failures |
| --- | --- | --- | --- | --- | --- |
| 2 | 2 | 5 | 5 | 0 | 0 |
| 4 | 2 | 25 | 15 | 10 | 0 |
| 6 | 2 | 125 | 53 | 72 | 0 |
| 8 | 2 | 625 | 265 | 360 | 0 |
| 10 | 2 | 3,125 | 1,213 | 1,912 | 0 |
| 14 | 1 | 2,187 | 935 | 1,252 | 0 |
| 16 | 1 | 6,561 | 2,717 | 3,844 | 0 |
| **Total** | specified above | **12,653** | **5,203** | **7,450** | **0** |

No additional nonsquarefree survivors remained after the cyclotomic-factor exclusion.
All 7,450 survivors passed the exact integer comparison, regardless of whether their irreducibility was classified.
Every irreducible noncyclotomic polynomial in the stated windows survives that exclusion, so the finite no-counterexample conclusion covers the **entire specified core in these windows**; it is not limited to the subsequently certified shortlist.
This is not a full irreducibility classification, and the coefficient/degree limits cannot be omitted.

For each nonempty window, the eight smallest ratios received certificates, 48 records altogether.
All 48 were certified irreducible by the displayed modular or trace data.
In particular each window's minimum among all survivors is itself in the core and is therefore also that window's exact core minimum.
Write \(R(p)=|\operatorname{disc}p|G_{2d}/(2d)^d\).
The minima are:

| Degree | Exact minimum \(R\) | Ascending coefficients of one minimizer |
| --- | --- | --- |
| 4 | \(60333/1024\) | \(1,-1,-1,-1,1\) |
| 6 | \(111017597/2985984\) | \(1,0,-1,-1,-1,0,1\) |
| 8 | \(69266544625/4294967296\) | \(1,0,0,-1,1,-1,0,0,1\) |
| 10 | \(105844516006149/10240000000000\) | \(1,-1,0,1,-1,1,-1,1,0,-1,1\) |
| 14 | \(59412581618545130859/1625527855624486912\) | \(1,0,0,0,-1,0,0,-1,0,0,-1,0,0,0,1\) |
| 16 | \(15122683448314424731711333/1208925819614629174706176\) | \(1,0,0,-1,-1,0,0,1,1,1,0,0,-1,-1,0,0,1\) |

The global minimum in these windows is the degree-ten row, the substitution \(p_{\mathrm{Lehmer}}(-t)\), with unchanged \(\Delta=1332031009\) and \(G_{20}=79461\).
Thus increasing coefficient height to 2 through degree 10 did not improve the smallest ratio.
The degree-16 minimizer is a different certified irreducible reciprocal unit; its \(\Delta=6288431159537641\), \(G_{32}=2404842013\), and trace polynomial is certified modulo 2 with a real root bracket \((-2,-7/4)\).
These exact data identify the weakest structures actually encountered without asserting a root-distribution classification or an infinite family.

**Assessment and stopping decision.** The candidate was not falsified in this bounded search.
None of the observed surplus minima is close to the failure boundary \(R=1\); nevertheless their finite lower entropy certificates retain the divisor \(2(2d-1)\).
Positive ratios above 1 do not supply a degree-uniform exponential surplus.
The useful next mathematical question is what constrains \(\Delta G_{2d}\) in an arbitrary irreducible reciprocal unit polynomial, rather than adding another unmotivated batch of passing samples.
No larger window, higher-degree enumeration, new source acquisition or second search run was performed.

The original PowerShell execution extracted the retained program and captured stdout in its working draft; adding the assessment did not run it again.
The current [J116 reproduction command](../computations/programs/Yin_J_G0116/readme.md#reproduction) prints to stdout and does not append to this fixed record.
The [original author-side finding](../audits/reviews/Yin_R_G0799_v1.md#author-finite-scope-check) preserves the actual table/JSON comparison and its original review limitations.
The general scalar-Gram theorem now has its complete current proof in [C209](../claims/Yin_C_G0209_v1.md#statement), while the original L4 input and dated execution remain distinct.
