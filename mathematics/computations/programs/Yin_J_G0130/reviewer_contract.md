# Independent reconstruction contract

Human record author: Yin.
This is the independently organized whole review of fixed C679v1 and J130, outside their substantive development.
The responsible main agent authorized precisely the existing two targets, 640 rows and fixed moduli before this review.
This contract was retained before execution of the reviewer program and before reading the author implementations.
It records a proposed verification, not a successful run.
The complete result, including any failed check, will belong to the reviewer output and fixed R finding.

## Exact scope and independently chosen method

Use only M=X^32 phi^64 and the division modulus M_pre=X^32 phi^65, with phi=X^2+X+1.
Reconstruct all 512 ordinary rows and 128 divided rows, their specified global lifts, the certificate's complete normal form and exactly epsilon=0,1.
No additional precision, membership target, support search, full-group enumeration, invisible support factor or original characteristic-zero construction is authorized here.
The certificate and author verification JSON are inputs to inspection, not correctness oracles.
No author implementation will be imported or used as the independent reconstruction.

Reconstruct every entire B_(2d+1) as F_(d+1)+F_d, where F_0=0 and F_(j+1)=sum_i binom(j-i,i) X^(j-2i) in F_2[X].
Pascal's identity gives F_(j+1)=X F_j+F_(j-1); the resulting B has initial values B_1=1 and B_3=X+1 and satisfies the required recurrence.
This formula differs from the author's iterative B recurrence and the separate author's symmetric-Laurent inversion.
Use reviewer-owned four-coefficient block convolution, ordinary polynomial long division, exponent-doubling squaring and extended Euclidean inversion.
The earlier reviewer implementation in J129 supplies only this reviewer's arithmetic design; neither J129 inputs nor results are inputs for this new finite question.

Check both matrix periods, whole-polynomial division before reduction, the exact lifted composition B_ell(chi), every source value and unit condition.
Check all complete 640-coordinate pivot products, all square closures through later pivots, all 640 source reductions and all stored reduction traces.
Reconstruct both full CRT targets and verify every component, complete product/residual identity, identical target expression, and the missing-coordinate obstruction.
Independently replay the bounded insertion with values alone to check the reported event/cancellation counts and pivot values; subgroup completeness rests on the verified identities and triangular normal-form proof, not on the replay's rank.

## Resource and publication bounds

The largest whole index is 3835, hence whole B degree at most 1917; the divided representative degree is at most 1915.
There are at most 1280 requested whole source/lift polynomials, plus 128 composition inputs of lower degree, and no unbounded search.
Each explicit whole formula uses at most 1918 binomial coefficients.
The matrix period exponent is exactly 640 in both declared rings.
There are at most 157 pivots, 797 insertion events and 125129 insertion cancellations.
There are at most 797 source/square reductions, each with at most 157 cancellations, and at most 314 cancellations across the two targets.
Each of at most 159 pivot/target expressions has exactly 640 exponents in 0,...,191, so evaluation uses at most 814080 modular products after at most 5120 cached generator powers.
The certificate input must be at most 64 MiB, with all row/vector counts checked before expression evaluation.
Modular products have degree at most 318 in M and 322 in M_pre before reduction; entire polynomial identity checks use only the bounded degrees stated above.
Execution requires explicit --execute, non-optimized Python and a live deadline of at most 1800 seconds, checked throughout bounded loops.
Failure or timeout publishes no successful replacement.
Only a complete successful result is atomically published as mathematics/computations/outputs/Yin_J_G0130/reviewer_verification.json.
The author certificate, author verification and all older J outputs are preserved.

From the repository root, the declared command is:

```powershell
python mathematics/computations/programs/Yin_J_G0130/reviewer_check.py --execute --max-seconds 1800
```

The actual command and outcome will be retained in the fixed R finding; the main agent integrates the existing J README without changing this contract's prior-execution meaning.
