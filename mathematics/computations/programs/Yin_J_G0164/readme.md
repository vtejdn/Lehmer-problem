---
author: Yin
---

# Integer levels and endpoint Taylor quotients for Boyd's 45 Salem numbers

<a id="boyd-descent-search"></a>
## Complete maps inside the sample

For [Yin's Lehmer Task](../../../tasks/Yin_T_G0001_v1.md#contract), the computation contributor tested all 45 rows of Boyd's table and obtained seven strictly smaller Salem numbers counted by source and level, with five distinct targets.
Row 36 reaches Lehmer's number exactly.
No output lies below it.
The following table gives every successful directed edge, using Boyd's row labels and the convention \(S_{\rm source}(X)=b\).
The last column reports the separate enumeration of every nonconstant [endpoint Taylor quotient](../../../claims/Yin_C_G0345_v115.md#statement).

| Source | Target | Salem degrees | Integer level \(b\) | Successful Taylor order |
| --- | --- | --- | --- | --- |
| 13 | 7 | \(18\to10\) | \(-1\) | none |
| 27 | 22 | \(30\to8\) | \(-1\) | none |
| 35 | 12 | \(26\to12\) | \(-1\) | 1 |
| 36 | 1 (Lehmer) | \(24\to10\) | \(-2\) | 1 |
| 37 | 19 | \(20\to10\) | \(-1\) | none |
| 39.5 | 22 | \(34\to8\) | \(-1\) | 1 |
| 42 | 7 | \(26\to10\) | \(-1\) | 1 |

All targets are terminal under both operations within these data, so the seven displayed arrows are also all nonempty maximal chains.
Of 185 source-level pairs tested, 88 have at least one distinct trace in the open window and account for 114 such roots.
Of 436 source-order pairs tested, 21 meet the window and each has one root there.
Exactly four of those produce a Salem output, all at order one, where subtracting \(S(2)\) and removing \(X-2\) already gives the listed level operation.
The search imposed no preliminary degree drop on an output.
The finite set of inputs and these two families of operations determine the scope of the result.

<a id="inputs"></a>
## Source coefficients and their orientation

The [fixed input](inputs/boyd.tsv) retains the number, degree, decimal value and half-polynomial of each displayed row, including the center coefficient.
The half-polynomial runs from the monic leading term down to the middle, and reflection gives the omitted coefficients.
Boyd identifies rows 1–39 with *Small Salem numbers* (Boy77), rows 21.5, 40, 41 and 42 with *Pisot and Salem numbers in intervals of the real line* (Boy78), and rows 39.5 and 41.5 with Michael Mossinghoff's February 1996 search. [Boyd's original table](https://www.cecm.sfu.ca/organics/papers/boyd/paper/html/Salem.html)

The coefficients in Boyd's row 39.5 give \(P(1)=1\) for the printed polynomial, whose exterior real root is negative.
Substituting \(-X\) gives the orientation with the listed positive Salem root \(1.2962106596\).
The author of the computation compared all 45 rows against Mossinghoff's list of June 1, 2026, by degree, decimal and the complete coefficient list.
Its row 43 confirms exactly that substitution, and every other Boyd coefficient list agrees without a substitution.
The code applies the change to row 39.5 while preserving the transcribed input.
The search scope uses Boyd's 45 rows. [Mossinghoff's SalemList](https://github.com/mossinghoff/Mahler-Measure-Database/blob/main/SalemList.txt)

<a id="method"></a>
## Exhaustion and exact arithmetic

From the input half-polynomial the program recovers \(S\) by the integer recurrence \(D_0=2,\ D_1=X,\ D_{j+1}=XD_j-D_{j-1}\), with the center coefficient used once.
For each row it checks that \(S\) is monic and irreducible over \(\mathbb Q\), with exactly one root \(T>2\) and all other roots in \((-2,2)\).
The neutral embedding makes \(T^2-4\) a nonsquare in the totally real trace field, so the lift has twice the trace degree and the specified Salem signature.
The displayed decimal is used only for an exact bracket of radius \(10^{-10}\) that is checked by signs at the rational images \(s+s^{-1}\) of its endpoints.
In particular \(T<13/10+10/13=2+9/130\) on every row.

On \(2<X<T\) one has \(S(X)<0\), so all nonzero integer levels there are negative.
Write \(S(2+z)=\sum_j h_j z^j\), with \(0<z<R=9/130\).
Then \(-S(2+z)\le\sum_{h_j<0}(-h_j)R^j\).
The program factors \(S+n\) for every integer \(1\le n\le\lfloor\sum_{h_j<0}(-h_j)R^j\rfloor\).
It also factors \(Q_k=(S-\sum_{j<k}h_j(X-2)^j)/(X-2)^k\) for every \(1\le k<\deg S\) by exact successive division.
At \(k=\deg S\) the quotient is the constant one.

For each monic irreducible factor, rational isolating intervals locate all its real roots.
Comparisons against \(-2,2\), the actual parent trace \(T\), and the degree-five trace of Lehmer's number use interval refinement until the intervals separate, with polynomial identity handling equality.
An output factor must have degree at least two, as many real roots as its degree, a single root in \((2,T)\), and all its other roots in \((-2,2)\).
These conditions are necessary and sufficient by the lifting quadratic and its negative discriminant at a neutral embedding.
The map \(r\mapsto (r+\sqrt{r^2-4})/2\) is strictly increasing for \(r>2\), so the trace comparisons determine the comparison of the Salem numbers.
Polynomial equality with the input table determines each target label.
The calculation reconstructs every tested polynomial from its factorization with multiplicities.

<a id="reproduction"></a>
## Reproduction

Run the [program](search.py) from the project root.

~~~powershell
python mathematics/computations/programs/Yin_J_G0164/search.py
~~~

The contributor ran it with Python 3.14.3 and SymPy 1.14.0, using integer polynomials, rational arithmetic, exact factorization and real-root isolation throughout.
The [generated results](../../outputs/Yin_J_G0164/results.json) retain each source polynomial, the integer-level bound and every candidate parameter, with factor coefficients in descending order, factor multiplicities, real-root counts, zero-based real-root indices inside the window and exact Salem hits.
The program prints the aggregate counts and every successful edge.

<a id="independent-verification"></a>
## Independent verification

A separate verifier compared all 45 input rows with Boyd's original table and Mossinghoff's corresponding rows, then used exact signs at the listed decimal brackets to select the orientation independently.
Only Boyd's row 39.5 required \(Z\mapsto-Z\), giving Mossinghoff's row 43.
The [independent program](verify.py) reconstructs the trace coefficients by triangular binomial inversion, tests divisibility by each smaller catalogue target, and checks every saved factor's irreducibility, multiplicity and product.
Signed Sturm variations at rational cuts recover the real-root counts without root isolation.
Bernstein coefficients on each source's own certified interval bound the sum of possible level counts by 116, all included among the 185 tested.
Running `python mathematics/computations/programs/Yin_J_G0164/verify.py` confirmed the seven level maps, four Taylor maps and all the window counts above. [Boyd's table](https://www.cecm.sfu.ca/organics/papers/boyd/paper/html/Salem.html) · [Mossinghoff's catalogue](https://github.com/mossinghoff/Mahler-Measure-Database/blob/main/SalemList.txt)

Every successful integer level in this sample has a rational trace root.
In the displayed order of sources, the complete rational-root sets of \(S-b\) are \(\{-2,1\}\), \(\{-2,1\}\), \(\{-2,-1,0,1,2\}\), \(\{2\}\), \(\{0\}\), \(\{-2,-1,0,2\}\) and \(\{-2,-1,1,2\}\).
For row 36, removing \(X-2\) and the degree-five trace polynomial of Lehmer's number from \(S+2\) leaves the irreducible sextic \(X^6-5X^4+X^3+6X^2-X-1\).
Its Sturm count gives four real roots, so this level produces a Salem factor even though the complete trace polynomial has a nonreal pair.
