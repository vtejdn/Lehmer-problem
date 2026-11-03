---
author: Yin
---
# Fixed 2d prescribed-C155-value energy-four diagnostic

## Question and scope

This is the first finite test of the [retained specification](../../../strategies/Yin_S_G0001.md#c155-fixed-2d-energy-four-test-2026-10-16), authorized by the [bounded Task decision](../../../tasks/Yin_T_G0001_v1.md#decision-bounded-fixed-2d-test-2026-10-18).
Root authored the input list, main program and interpretation.
The four original inputs were fixed before execution from the existing [C148 controls](../../../claims/Yin_C_G0148_v1.md#quartic-exact-classification); no search, adaptive replacement or window expansion was performed.
Every input is monic, irreducible over Q, reciprocal, a noncyclotomic integer unit, and has an actual totally real trace field.
These are checked properties of these four inputs, not assumptions inferred merely from reciprocity.

The target is the SAME [C155 value](../../../claims/Yin_C_G0155_v1.md#original-polynomial-return) h=e^2+f^2+g^2 in the original order Z[alpha].
No minimum over other residue vectors or convenient abstract triples is taken.
The ordinary allowed degrees are 0 through 2d-1, so A has exactly 2d coefficient columns.

## Files

| File | Role |
| --- | --- |
| [input.json](input.json) | Ordered original input coefficients, fixed window multiple 2 and threshold 4. |
| [main.py](main.py) | Author exact trace-polynomial construction, original-value checks, energy minimizer and circle-contact certificates. |
| [verify.py](verify.py) | Separately implemented original-field quotient reconstruction and finite-scope verification. |
| results.json (`mathematics/computations/outputs/Yin_J_G0097/results.json`) | Complete author result, exact native certificates and display-only decimal energies. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0097/verification.json`) | Completed independent verification output. |

Generated results are local ignored output and can be regenerated from these programs and fixed inputs.
No earlier generated output is an input to the author calculation.
The verifier requires the actual author result for comparison; that result is not a generator for the independently reconstructed arithmetic.

## Reproduction

From the repository root, using the repository Python environment with SymPy 1.14.0:

~~~powershell
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0097/main.py
.venv/Scripts/python.exe -B -X utf8 mathematics/computations/programs/Yin_J_G0097/verify.py
~~~

Both commands resolve their own J program and output homes independently of the caller's working directory.
Each complete invocation is bounded by 180 seconds.
All deciding arithmetic is integral or rational; no tolerance, random seed or floating-point sign decision is used.
The decimal energies and approximate root locations are display aids only.
The author atomically publishes a complete result only after all four inputs pass; a failure preserves incomplete data in partial.json without calling it a complete result.

## Mathematical reduction and exact checks

Write P(t)=t^r T(t+t^(-1)), d=2r, and define C_0=2,C_1=z,C_(n+1)=z C_n-C_(n-1).
The actual [C153v2 trace interface](../../../claims/Yin_C_G0153_v2.md#exact-reciprocal-phase-and-trace-domain) gives theta_p=rem_T T(C_p)/p for p=2,3,5.
The program verifies coefficientwise integrality, nonzero quotients, the exact reciprocal identity and the original-field identities alpha^(rp)theta_p(alpha+alpha^(-1))=P(alpha^p)/p.
It then constructs a=theta_2,b=theta_3,c=theta_5 and the exact defects e=b^2-a^3,f=2c^2-3a^5,g=c^3-2b^5 in Q[z]/(T).
Irreducibility and noncyclotomic status are checked exactly.
Rational isolating intervals account for all r distinct roots of T, so the actual trace field is totally real.
The resultant norm in the original field is checked against the square of the trace-field norm and the C155 floor.

Let r_h be the complete integral original power-basis residue of h and A=[rem_P(1),...,rem_P(t^(2d-1))].
The first d columns are I_d, so G=A A^T is positive definite.
The retained rational certificate is y=G^(-1)r_h and x_*=A^T y, with exact checks G y=r_h, A x_*=r_h and E=r_h^T y=x_*^T x_*.
For any other legal rational x, write x=x_*+v with A v=0.
Then x_*^T v=y^T A v=0 and ||x||_2^2=E+||v||_2^2>=E.
Thus the certificate proves the actual minimum over the whole affine residue fiber, not only the energy of one convenient representative.
This specializes the existing [C16 least-representative interface](../../../claims/Yin_C_G0016_v1.md#weighted-quotient-lattice-certificate); no new general minimization theorem is claimed.

For each trace-root interval contained in (-2,2), rational interval Horner evaluation of the reduced h polynomial bounds its exact value.
The corresponding roots of t^2-z t+1 lie on the unit circle and are original roots of P.
Every representative of the same original residue takes that same h value there, at every window length.
Consequently one certified h>2 excludes strict circle supremum below 2 for the same value on that input, independently of the coefficient-window width.
This is the previously specified circle-contact criterion, now evaluated on the declared finite inputs.

<a id="finite-results"></a>
## Results and limits

The author calculation completed all four declared inputs on 2026-10-18.
All four exact energies are strictly greater than 4.

| Original P(t) | Degree | Exact E_(2d)(h) | Display approximation | E-4 sign |
| --- | --- | --- | --- | --- |
| t^2-3t+1 | 2 | 14887127520653722/5 | 2.9774255041307444e15 | Positive |
| t^4-t^3-t^2-t+1 | 4 | 663452827142605678890/119 | 5.5752338415345015e18 | Positive |
| t^4-4t^2+1 | 4 | 37858731121859357017433378/65 | 5.8244201725937472e23 | Positive |
| t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1 | 10 | 1656102182918999/2943 | 5.6272585216411791e11 | Positive |

The corresponding reduced trace values are h=58480901; h=994047254+763022483z; h=791052558794; and h=434995+293904z-944186z^2-177856z^3+316258z^4, respectively.
Their trace minimal polynomials are z-3, z^2-z-3, z^2-6 and z^5+z^4-5z^3-5z^2+4z+3.
The exact native result preserves every remainder column, Gram entry, target residue, dual solution, minimizer, norm and rational root/value enclosure.

For the quadratic control the explicit trace values are (a,b,c)=(2,5,24), (e,f,g)=(17,1056,7574), and h=58480901.
Its remainder matrix has rows (1,0,-1,-3) and (0,1,3,8), so G has rows (11,-27) and (-27,74), determinant 85 and E=(74/85)h^2.
This direct check explains why preserving the prescribed arithmetic value yields an enormous energy even in the smallest control; it is not the shortest nonzero residue problem.

The quartic Salem input has one trace root in (-2,2), with 152<h<153.
The Lehmer input has four such trace roots; in increasing trace-root order their h values lie strictly in (1720721,1720722), (2034,2035), (12907,12908) and (8,9).
These integer enclosures follow from the retained exact rational interval endpoints, not rounded root evaluations.
Thus each of these two inputs has an immutable original-circle obstruction, and changing only the window cannot produce a strict-supremum-below-2 representative of this same h.
The quadratic and radical quartic have no original unit-circle roots; this particular contact test supplies no conclusion for them beyond their fixed-window energy certificates.

No input crossed the necessary energy threshold, so no least-energy supremum optimization, correlation search or sample expansion was performed.
The declared first round is complete at its finite scope.
Four certified failures do not prove E_(2d)(h)>=4 for all admissible P, for a degree class, or for all sufficiently small positive measures.
They supply no counterexample to Lehmer's conjecture and no new Mahler lower bound.
The circle obstruction concerns a strict supremum certificate for this same h; it does not exclude a paid logarithmic estimate or a different auxiliary value with its own arithmetic proof.

## Inspection summary

Root checked the exact input domain, trace phases, integral residue, full-norm identity, whole-fiber optimality certificate, positive signs of E-4 and the rational circle-contact enclosures.
A separately assigned reviewer who did not develop the author program or select its inputs reconstructed the original-field arithmetic using Fraction quotient operations, independently solved the rational system and reproduced all four payloads and five circle contacts.
The reviewer supplied the quadratic hand-control explanation after its independent reconstruction.
Its first comparison stopped at a trailing-zero polynomial representation difference; the correction preserved the exact input and mathematical scope, and the complete subsequent verification passed.
[R374](../../../audits/reviews/Yin_R_G0374_v1.md#fixed-2d-finite-finding) accepts the complete finite calculation, whole-fiber reduction and five contact certificates at this actual scope.
Both implementations use the same installed SymPy for rational irreducibility; the independent quotient, norm, root-count, interval and linear-system arithmetic uses a separate Fraction implementation.
Neither implementation supplies formal verification or a universal result.

## Consequences for the paused handoff

Close the fixed-2d strict-supremum attempt on these four inputs.
Do not enlarge an unchanged sample or a window merely to seek a smaller number.
For the quartic Salem and Lehmer inputs, the same-value strict-supremum branch is excluded at every window length by original-circle contact.
A future authorized round would need a changed, justified input-class question, a paid logarithmic method, or a different auxiliary with a fresh norm-income argument.
The direct-logarithm and general-coverage questions were not executed in this round.

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
| `results.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0374_v1.md#fixed-2d-finite-finding) |
| `verification.json` | [Original finding and inspected scope](../../../audits/reviews/Yin_R_G0374_v1.md#fixed-2d-finite-finding) |
