---
author: Yin
---

# Exact multi-prime cyclic-norm certificates over every positive exponent

Context: [G0001](../../../tasks/Yin_T_G0001_v1.md#contract), [the finite local-table and tail proofs](../../../claims/Yin_C_G0256_v1.md#finite-exact-local-cyclic-table), and [intrinsic lattice periods](../../../claims/Yin_C_G0251_v1.md#intrinsic-scalar-period).

## Question and scope

Use precisely the two retained inputs of [J G0010](../Yin_J_G0010/readme.md):
the degree-ten Lehmer polynomial and the degree-22 polynomial

    P_22=(t^24-t^17-t^12-t^7+1)/(t^2-t+1).

Their irreducibility, positive small Mahler measure, unit and reciprocal scope, and all-power degree preservation are inherited from the fixed records linked there.
No new irreducibility over Q or root numerics are inferred from this experiment.
Both complete coefficient vectors are retained and independently reconstructed by integer polynomial division.

The selected rational primes are exactly

    S={2,3,5,7,11,13,17,19,23,29,31}.

First determine the exact identity period T_p and projective scalar period N_p at each of these primes.
Then determine the maximum, over **every integer n>=1**, of the automatic cyclic-norm certificate

    [sum_(p in S) k_p(n)(1+v_p(n))log p - d log2]/n,

where k_p(n) counts individual reduced roots of multiplicative order dividing n.
Finally replace that floor by the exact S-part of

    C_n=|Res(P,t^n-1)|,

and determine its all-n optimum for the same archimedean upper bound C_n<=2^d M(P)^n.
This is an optimization within one specified norm certificate, not over all auxiliary polynomials or primes.
No uniform near-one coverage or Lehmer resolution is inferred from two inputs.

## Exact reductions and verification

All 22 reductions are squarefree.
Complete factorizations are verified by recombination and Rabin tests; multiplicative orders are certified by equality and every prime-divisor minimality test.
Full companion matrix powers independently check both T_p and N_p.
By [C251](../../../claims/Yin_C_G0251_v1.md#intrinsic-scalar-period) these squarefree periods are also the intrinsic periods on every invariant full lattice.
The general author routine also handles repeated-factor Jordan costs, but this execution contains no repeated-prime case.

For these reciprocal polynomials a scalar residue c necessarily has c^2=1: inversion permutes the roots (and gives the same automorphism of the quotient algebra).
Thus at odd p the projective period is T_p/2 when the half-power is -I, and T_p otherwise; at p=2 it is T_p.
The author uses general scalar-minimality tests; the verifier checks this additional reciprocal restriction separately.

For the first floor, each reduced-order group (o,w) contributes w log p at every divisibility event op^j|n, j>=0.
The author uses an integer sieve; the verifier directly computes every n by order divisibility.
With R=product_(p in S)p, [C256](../../../claims/Yin_C_G0256_v1.md#good-prime-aggregation-and-global-tail) proves the global tail

    score(n)<=d log(Rn/2)/n.

This is decreasing here.
A certified positive winner and a strictly smaller tail bound exclude all n above the finite range.
The retained ranges are 1..4096 for Lehmer and 1..8192 for P_22; they are justified cutoffs, not guessed search limits.

For the actual S-part, [C256's finite table](../../../claims/Yin_C_G0256_v1.md#finite-exact-local-cyclic-table) groups original roots by their residue order o.
At good odd primes one initial value B_o,0 suffices; at p=2 the initial pair B_o,0 and B_o,1 suffices, followed by the exact linear valuation slope.
The author probes C_o and, at p=2, C_(2o) modulo p^64, reduces t^n-1 modulo P, and computes its integer polynomial resultant modulo p^64.
Every residue is nonzero at that precision, so every recorded valuation is exact.
The generic precision loop would increase precision if necessary; no precision increase occurred in this run.

The independent verifier reconstructs these probes by full companion matrix powers and exact integer Bareiss determinants.
It uses no author polynomial-power or resultant routine.
It checks all 54 local probes (21 and 33 respectively) and 22 additional direct probes at the winning exponents.
Divisor-order subtraction and the LTE table then determine the actual S-part for every n.
The exact table provides its own decreasing all-n tail and finite optimum verification.

No floating-point comparison is used.
The author bounds logarithms by 100 terms of a rational atanh series, with its geometric tail bounded explicitly, and rounds outward at 128 binary bits.
The verifier uses 160 terms and 192 bits.
Negative coefficients reverse interval endpoints.
Every nonwinning exponent and the infinite tail have strictly smaller upper bounds than the winner's lower bound; exact prime-product equality handles possible ties.
Both actual winners are unique.
The displayed decimals below are certified truncations.

## Results

| Input | Minimum N_p/d within S | Prime minimizing T_p/(d log p) within S | Unique maximizing n | Exact maximum of the stated norm certificate |
| --- | --- | --- | --- | --- |
| Lehmer, d=10 | 31/10, at p=2 | p=2 | 124 | (20 log2+2 log3)/124 > 0.1295174853 |
| P_22, d=22 | 2047/22, at p=2 | p=2 | 120 | (4 log5+2 log7+6 log11+2 log23-22 log2)/120 > 0.1311557837 |

Both rows are lower bounds for the original algebraic entropy m(P).
The periods at every selected prime are retained in result.json.
In particular P_22 has no scalar exponent below 2047 at any p in S, yet the partial-return norm succeeds at n=120.
At that exponent:

- p=5 contributes two roots of order 6, with v_5(120)=1, for weight 4;
- p=7 contributes two roots of order 8, for weight 2;
- p=11 contributes two roots of order 5 and four of order 60, for weight 6;
- p=23 contributes two roots of order 24, for weight 2.

No single one of these primes returns every root.
The Lehmer winner instead uses all ten roots at p=2 and two roots of order 4 at p=3.

In fact every retained initial B entry equals its automatic depth floor.
By the exact table formula, the S-part equals the first-floor expression for **all n**, not just at the winner.
Thus deeper actual valuations at these same primes cannot improve this particular certificate on either input.
Other primes or a different archimedean estimate remain separate possibilities.

Using only the common scalar coefficient from L G0069, the best bound on P_22 among these primes would be 0.427800*22/2047, much smaller than the aggregate certificate.
For the Lehmer input that scalar bound is 0.427800*10/31 and is stronger than this aggregate one.
Hence aggregation is useful on the non-Salem control, but is not a uniform dominance assertion over every known auxiliary estimate.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact finite-field periods, first-floor sieve, rigorous logs and all-n tail. |
| result.json (`mathematics/computations/outputs/Yin_J_G0011/result.json`) | Complete integer inputs, factors/order certificates, period remainders and first-floor optima. |
| [actual.py](actual.py) | Finite modular-resultant probes, exact local tables and actual S-part all-n optima; imports adjacent main.py. |
| actual-result.json (`mathematics/computations/outputs/Yin_J_G0011/actual-result.json`) | Every probe remainder/residue, isolated local valuation, actual winner and tail. |
| [verify.py](verify.py), verification.json (`mathematics/computations/outputs/Yin_J_G0011/verification.json`) | Separately authored factor/matrix/direct-sum and rational-log verification. |
| [verify_actual.py](verify_actual.py), actual-verification.json (`mathematics/computations/outputs/Yin_J_G0011/actual-verification.json`) | Separately authored companion/Bareiss verification; imports only the same independent reviewer's verify.py helpers. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0011/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0011/actual.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0011/verify.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0011/verify_actual.py
```

The author uses SymPy and python-flint; independent verification uses Python integers and Fraction.
There is no random seed or approximate numerical root computation.
`actual.py` imports the author's `main.py` helpers, and `verify_actual.py` imports only the same reviewer's `verify.py` helpers.
Both verification programs also require the actual J_G0010 result (`mathematics/computations/outputs/Yin_J_G0010/result.json`).
Generate or explicitly obtain the declared inputs in this command order.

Generated output uses `mathematics/computations/outputs/Yin_J_G0011/`, independently of the caller's directory.
Actual retained output is local and Git-ignored; a clone may lack it.
Verification reports missing required inputs without substituting other data or implicitly running a producer.
These are current reproduction instructions, not a new execution or proof review.

The independent first-floor verifier passed 14,257 checks, and the actual-valuation verifier passed 169,753 checks, including fresh input/factor/order and logarithm checks.
The coordinator authored and executed main.py/actual.py and checked their mathematical payloads.
Assigned AI review_matrix_completion read both complete author programs, independently wrote and ran the verifiers, and checked the algebraic reductions.
The coordinator read both complete verifiers and separately reproduced all four programs' mathematical results.
The direct finite-table and tail theorem received the complete independent proof review disclosed in L G0074.
That is the original reported label; the actual initial context of that whole theorem finding is [unknown](../../../audits/reviews/Yin_R_G0527_v1.md#historical-cyclic-whole-finding).
The current complete proof at C256 has its own full self-review; this locator update does not rerun or newly inspect any J11 program or numerical result.

The author's initial comparison incorrectly required separate-term and combined-log2 interval endpoints to be identical.
Cancellation makes the combined interval narrower, so the correct check is interval inclusion.
A verifier display initially could not serialize an enormous Fraction; an outward-rounded display bound replaced it without changing the exact comparisons.
Neither failure produced an adopted mathematical result or changed the inputs, prime set or certificate formula.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
