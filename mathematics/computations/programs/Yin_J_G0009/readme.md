---
author: Yin
---

# Exact arithmetic surplus on the retained Lehmer control

Current mathematical context: [G0001](../../../tasks/Yin_T_G0001_v1.md#contract), the accepted [original control in C226](../../../claims/Yin_C_G0226_v1.md#lehmer-joint-prime-control), the complete [C230 finite arithmetic proof](../../../claims/Yin_C_G0230_v1.md#confluent-arithmetic-lower-bound), and [C231 order/cyclic and all-power norm proof](../../../claims/Yin_C_G0231_v1.md#powered-order-index).
The original native inputs and retained execution facts preserve their L55/L57/L59 context, without a new run or Task resumption.

## Question and scope

Compute the exact positive-integer surplus discarded from the Matveev finite determinant for the standard degree-ten Lehmer polynomial, using the selected primes 2 and 3.
Determine its dependence on the base-node multiplicity k.
Test only k=1, the case with no repeated base node, and k=2, the first confluent case, against the exact block-volume bound.
Also compute precisely the cyclic resultants c_1,...,c_6 required by the reciprocal factor extraction for pairs (1,2), (1,3), (2,3) and the two powered-index identities in [C231 retained L59 proof](../../../claims/Yin_C_G0231_v1.md#explicit-cyclic-surplus-bound).
This is a single accepted input and two motivated settings, with no parameter scan, floating-point root calculation, or new irreducibility claim.
The algebraic-unit and degree-preservation domain is inherited from the retained L G0055 control and its existing source dependencies.

All coefficient vectors are ascending:

    P  = [1,1,0,-1,-1,-1,-1,-1,0,1,1],
    Q2 = [1,-1,0,-1,1,-1,1,-1,0,-1,1],
    Q3 = [1,-2,0,2,-1,-1,-1,2,0,-2,1].

Here Qp(t)=product_i(t-alpha_i^p), with all ten conjugates retained.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Generates powered polynomials by symbolic resultants, obtains their discriminants and pairwise resultants, and evaluates the two exact block certificates. |
| result.json (`mathematics/computations/outputs/Yin_J_G0009/result.json`) | Original input, full powered-polynomial coefficients, exact arithmetic factors, all-k surplus formula, block constants and integer comparisons. |
| [verify.py](verify.py) | Reads `result.json` from the J output home without importing `main.py`; reconstructs powered polynomials by Newton identities, resultants by Sylvester/Bareiss determinants, and block constants from the actual integer binomial Gram matrices. |
| verification.json (`mathematics/computations/outputs/Yin_J_G0009/verification.json`) | The 67 successful mathematical-payload comparisons from the second algorithm. No byte/hash or execution-metadata gate is imposed. |

## Reproduction

From the repository root:

```powershell
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0009/main.py
.venv/Scripts/python.exe -B mathematics/computations/programs/Yin_J_G0009/verify.py
```

The author method uses SymPy; verification uses only the standard library.
Run the author program first or explicitly obtain its actual result before verification.
All arithmetic is integer/rational, with no precision parameter, tolerance, random seed, truncation or numerical sign certification.

Generated output uses `mathematics/computations/outputs/Yin_J_G0009/`, independently of the caller's directory.
Actual retained output is local and Git-ignored; a clone may lack it.
Verification reports missing required inputs without substituting other data or implicitly running a producer.
These are current reproduction instructions, not a new execution or proof review.

## Results and limits

The generating method and the separate exact algorithms agree on all 67 enumerated comparisons, including the six targeted cyclic-resultant additions.
Both programs were written and first run by assigned AI ms25_source: algorithmic independence is not an independent-author proof review.
The original complete coordinator code/interface check and successful retained reruns are recorded in [R515](../../../audits/reviews/Yin_R_G0515_v1.md#historical-surplus-code-finding), with its genuinely unknown initial substantive-context arrangement and exact67-comparison scope.
The native author checks remain self-review, as also retained in R515; these current reproduction instructions do not run either program.
The earlier irreducibility and degree-preservation evidence remains the source of this control's accepted mathematical domain.

The exact arithmetic output is:

| Quantity | Value |
| --- | --- |
| Delta=abs(disc P) | 1332031009 |
| abs(disc Q2) | 11988279081=9 Delta |
| abs(disc Q3) | 1332031009=Delta |
| b2 squared, b3 squared | 9, 1 |
| Res(P,Q2), normalized by 2^10 | 1024, 1 |
| Res(P,Q3), normalized by 3^10 | 59049, 1 |
| Res(Q2,Q3) | 1 |

The six required cyclic resultants c_n=Res(P,t^n-1) are

    c_1=c_2=c_3=c_5=c_6=-1,       c_4=-9.

Consequently the reciprocal index-factor squares are c_4/c_2=9 and c_6/c_2=1.
The cyclic divisor for the base pair (1,3) is |c_2 c_4|=9, but it is entirely contained in the Frobenius floor 3^10: dividing by gcd(9,3^10) leaves normalized cyclic floor one.
The pair (1,2) already has |c_1 c_3|=1, while the cross pair (2,3) has |c_1 c_5|=1.
The gcd-corrected cyclic lower product in L G0059 is therefore exactly 9 for every k, attaining the actual surplus on this input.
Omitting the gcd correction would falsely add a factor 9^(2k) to that lower product.
These computations are a finite normalization and overlap diagnostic, not a parameter scan.

The exact product identity in L G0057 therefore gives, for every integer k>=1 with this fixed input and these two primes,

    Q_arith(k)=b2^2 b3^2
                 [Res(P,Q2)/2^10]^(2k)
                 [Res(P,Q3)/3^10]^(2k)
                 Res(Q2,Q3)^2
              =9.

This all-k conclusion follows from the displayed identity and the finitely computed factors; the block comparisons themselves cover only k=1 and k=2.
Define N=10(k+2), let A_(N,k) be the binomial Gram determinant of L G0057, and put

    R_k = 9 Delta^(k^2+2) 6^(20k) / [N^2 A_(N,k)]^10,
    E_k = 2[k(N-k)+5(N-1)].

The complete determinant value is the numerator before division by the block cost, and L G0057 yields M(P)^E_k>=R_k.
The retained integer comparisons establish:

| k | N | A_(N,k) | E_k | Exact comparison and consequence |
| --- | --- | --- | --- | --- |
| 1 | 30 | 30 | 348 | R_1=9 Delta^3 6^20/30^30<1; retaining the full surplus still supplies no positive logarithmic lower bound. |
| 2 | 40 | 213200 | 542 | R_2=9 Delta^6 6^40/(341120000)^10>27; hence m(P)>log(27)/542. Already R_2/9>3, so the bound without the surplus is positive as well. |

Thus the exact factor 9 increases the k=2 logarithmic certificate by log(9)/542, but it does not change positivity in either tested case.
The positive k=2 certificate already comes from the confluent/block estimate.
This distinguishes two contributions on a concrete accepted control and does not establish a degree-independent entropy gap, rule out a general arithmetic-surplus growth law, optimize over all k or prime sets, or bound the true entropy from above.
It does not alter the uniform-ceiling scope in L G0058, which deliberately used Q_arith>=1 rather than the actual surplus.

## Reproducing reviewed runs

The review findings concern outputs of particular recorded runs.
Generated output files are kept locally and are not synchronized.
To verify a recorded result, reproduce the documented program, inputs and parameters and repeat the applicable verifier checks.
A fresh run does not retrospectively change the historical finding date or inspected scope.
