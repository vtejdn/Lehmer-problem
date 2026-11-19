---
author: Yin
---

# Degree 64 at Mahler measure 1.091

<a id="census"></a>
## Complete classification

There is no monic irreducible noncyclotomic reciprocal polynomial in \(\mathbb Z[X]\) of degree 64 with \(M(P)\le T=1091/1000\).
The [certified first-half box](../v7/readme.md#bounds) contains 20,557,031,095 representatives after removing power substitutions and identifying \(P(X)\) with \(P(-X)\).
A power substitution \(P(X)=S(X^q)\), \(q>1\), would give \(1<M(S)=M(P)\le T\) in degree at most 32, contrary to the [published degree bound below Lehmer's measure](../../../../../audits/literature/MRW08/Yin_U001.md#degree).
Write \(s_k=\sum_\alpha\alpha^k\), over the roots of \(P\) with multiplicity.
Beyond the center we use the necessary bound \(\lvert s_k\rvert\le\lfloor62+T^k+T^{-k}\rfloor\) from [reciprocal pairing and convexity](../../../../../ledger/Yin_L_G0462_v266.md#linear).

| Applied condition | Representatives remaining |
| --- | ---: |
| First-half box and symmetries | 20,557,031,095 |
| First reflected sum \(s_{33}\) | 1,082,384,125 |
| All reflected sums through \(s_{41}\) | 69,297,361 |
| Nonzero at \(1\) and \(-1\) | 24,042,058 |
| All reflected sums through \(s_{120}\) | 7,056,496 |
| Indivisible by \(\Phi_3,\Phi_4,\Phi_6\) | 1,488,235 |
| Also pass the modular Graeffe comparisons | 12,184 |
| Also pass exact cyclotomic division | 0 |

Every one of the 12,184 polynomials in the last division step has a cyclotomic divisor.
The [summary](../../../../outputs/Yin_J_G0179/versions/v8/summary.json) gives the counts by order and the direct checks on three fixed prefixes.
This census covers only degree 64 at the stated cutoff.

<a id="suffix"></a>
## Nine reflected sums from two lists

The first sixteen sums are chosen by the [integral Newton recursion](../v3/readme.md#recurrence).
If the first nonzero odd-indexed sum is negative, change \(X\) to \(-X\).
If all odd sums through 15 vanish, then every later odd sum through 32 vanishes.
Indeed the [prime-power congruences](../../readme.md#counts) give zero modulo \(j\) for the next odd \(s_j\) when its proper-divisor sums vanish, and the box has \(B_j<j\) at these odd indices.
Thus all odd coefficients vanish by Newton's identities and reciprocity, giving a power substitution.
Conversely any power substitution in degree 64 has even exponents only, so the first nonzero odd sum rule selects exactly one member of every required sign pair.

Fix a retained prefix and take the smallest possible \(s_j\) in each successive congruence class for \(17\le j\le32\), giving a base reciprocal polynomial \(P_0=\sum c_iX^i\).
All proper divisors of these \(j\) are at most 16.
The permitted sums vary independently as \(s_j+j b_j\), where \(b_j=0\) or \(1\) according to the bounds.
For each \(j\) let \(V_j\) agree with \(X^j P_0\) through degree 32 and reflect its coefficients about degree 32, counting the middle term once.
The [suffix coefficient identity](../../../../../ledger/Yin_L_G0462_v271.md#affine) gives \(P'=P_0-\sum b_jV_j\) in every degree.
Write \(U_j=V_j/P_0\) as a power series at zero, so \(U_j=X^j+O(X^{33})\).
Since \(\sum b_jU_j\) has order at least 17, the linear and quadratic terms of \(-\log(1-\sum b_jU_j)\) give the exact change through degree 41.
For \(33\le k\le41\) this reads
\[
 s'_k-s_k=k\sum_{j=17}^{32}b_j[X^k]U_j+
             \frac{k}{2}\sum_{i+j=k}b_i b_j.
\]
Here the second sum ranges over ordered suffix indices, since errors in replacing \(U_iU_j\) by \(X^{i+j}\) start in degree at least 50.
In particular every quadratic term uses only indices \(17,\ldots,24\).
The lower eight digits and upper eight digits therefore each give a separate list of at most 256 vectors of nine integers whose pairwise sums, added to the base traces, give every completion exactly once.

For \(d_t=[X^t](V_j-X^jP_0)\) the implementation computes \([X^k]U_j=\sum_{t=33}^k d_t[X^{k-t}]P_0^{-1}\) in the required range.
Here \(d_t=c_{64-t-j}-c_{t-j}\), with a negative coefficient index interpreted as zero.
Only the first eight inverse coefficients after the constant term are needed.
Adding a new nonzero digit \(b_j\) contributes \(j\) at \(2j\), and \(i+j\) for each previously selected \(b_i\) at \(i+j\), whenever that index is at most 41.
The native search checks the first component of each pair, then compares the remaining eight until one fails.
For each survivor it reconstructs the reciprocal polynomial using \(P'=P_0-\sum b_jV_j\).

<a id="finishing"></a>
## Integer arithmetic and final tests

The unsigned residue arithmetic used for the two lists computes their entries modulo \(2^{32}\), via unchecked signed machine operations.
To justify comparison with the small trace caps, put \(C_0=1\) and \(C_k=\lfloor\sum_{i=1}^k B_i C_{k-i}/k\rfloor\) for \(k\le32\), and reflect \(C_k\) through degree 64.
Then \(\lvert c_k\rvert\le C_k\), with \(C_{32}=424102\) and \(\sum_{k=0}^{32} C_k=2308089\).
Consequently the first-half Newton numerators have absolute value at most \(69242670\), so signed division reconstructs the correct integer coefficients.
At any later comparison, with \(L_j\) the applicable trace cap, the absolute Newton numerator is at most
\[
 \mathbf1_{k\le64}\,kC_k+\sum_{i=1}^{\min(64,k-1)} C_i L_{k-i}
\]
whenever the earlier traces have passed.
The maximum of this bound through indices 33 to 41 is \(41530163\).
Thus, inductively until the first failed comparison, the centered 32-bit residue is the actual trace.
At indices 42 to 120 the largest bound is \(10510999295\), and the program takes the Newton sum directly in signed 64-bit integers.
Both endpoint evaluations are exact since \(\sum_{i=0}^{64} C_i<2^{31}\).
The remainders modulo \(\Phi_3,\Phi_4,\Phi_6\) likewise fit signed 32-bit integers since the coordinates of every monomial in the basis \(1,X\) have absolute value at most one.

For the [Graeffe iterates](../v3/readme.md#last-tests) the coefficient of index \(i\) after \(g\) squarings satisfies \(\lvert a_i\rvert\le\binom{64}{i}T^{2^g}\) if \(M(P)\le T\).
The program computes the first ten iterates in \((\mathbb Z/2^{64}\mathbb Z)[X]\), using reciprocity to recover the second half.
For a residue \(r\in[0,2^{64})\), \(\min(r,2^{64}-r)\le\lvert a_i\rvert\).
It discards a candidate only if this lower bound strictly exceeds the exact integer floor of the rational upper bound.
All surviving polynomials are tested against the [cyclotomic divisors](../v6/readme.md#census) with \(\varphi(n)\le64\) by monic division over the integers, optionally preceded by reduction modulo two.

<a id="reproduction"></a>
## Reproduction and count checks

From the repository root run the following commands using Python and NumPy, with the .NET Framework C# compiler on Windows or the Mono compiler and runtime on Unix.
The first command regenerates the [input box](../v7/readme.md#weights) from the tracked rational weights.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/versions/v7/larger_boxes.py
python -B mathematics/computations/programs/Yin_J_G0179/versions/v8/sieve.py --workers 6
python -B mathematics/computations/programs/Yin_J_G0179/versions/v8/verify.py
~~~

The [driver](sieve.py) compiles the [native search](Sieve64.cs) and writes one result for every pair \(s_1\ge0,\ s_2\equiv s_1\bmod2\) in the given box.
Each worker writes just the polynomials requiring final division, then stores the counts and any unclassified polynomials.
The [verification program](verify.py) sums the completions of each of the 39 pairs independently using the [prime-power congruence tensors](../v2/cyclotomic_prefixes.py).
In all 39 cases the count agrees with the enumeration, and the aggregate agrees with the original sign and power-substitution count.
The program also enumerates three sixteen-sum prefixes directly with arbitrary-precision Newton arithmetic for every completion, ordinary cyclotomic division, and exact Graeffe polynomials before taking residues.
It compares the complete vector of counts with the native routine at each prefix.
The sign transform of the [five-prime example](../v7/readme.md#weights) has 2,048 completions and two survive through index 41.
The constant prefix \(s_j=5\) has 65,536 completions, of which 9,120 survive through index 41 and all vanish at an endpoint.
The prefix \(s_j=3\mathbf1_{3\mid j}\) has four completions, all surviving through index 41, with two endpoint exclusions, one quadratic cyclotomic divisor and one Graeffe exclusion.
