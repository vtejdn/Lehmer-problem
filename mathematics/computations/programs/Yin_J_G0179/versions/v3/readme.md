---
author: Yin
---

# Reflected Newton sums and Graeffe tests in degrees 56 and 58

<a id="counts"></a>
## Complete reciprocal candidates at measure 1.089

Put \(T=1089/1000\) and consider monic, reciprocal, irreducible noncyclotomic integer polynomials of degree \(D=56\) or \(58\) with \(M(P)\le T\).
There are no such polynomials in either degree.
At the [prime-223 frontier](../../../../../ledger/Yin_L_G0462_v264.md#frontier), the smaller factor has these properties and admits no nontrivial power substitution.
The [version-two sieve](../v2/readme.md#counts) gives all coefficient representatives for this search after identification of \(P(X)\) with \(P(-X)\).
The following table gives successive numbers of complete representatives.

| Condition | Degree 56 | Degree 58 |
| --- | ---: | ---: |
| Version-two prefix tests and symmetries | 914,510,217 | 2,476,894,466 |
| First power sum beyond the middle coefficient | 55,681,068 | 106,805,888 |
| All additional power sums through index 120 | 1,459,613 | 2,643,465 |
| Also nonzero at both \(1\) and \(-1\) | 590,561 | 1,076,716 |
| No tested cyclotomic divisor of order at most \(2D\) | 59,545 | 115,896 |
| Also within the tested Graeffe coefficient bounds | 0 | 1 |
| Also distinct from \(\Phi_{118}\) | 0 | 0 |

The cyclotomic-divisor tests removed 531,016 and 960,820 endpoint survivors, respectively.
The exact Graeffe tests removed 59,545 and 115,895, all by the eighth squaring.
The remaining degree-58 polynomial is \(1-X+X^2-\cdots-X^{57}+X^{58}=\Phi_{118}(X)\).
These exclusions originally enumerate the representatives without power substitutions.
If an irreducible candidate had the form \(S(X^q)\) for \(q\ge2\), then \(1<M(S)=M(P)\le T\) at degree at most 29.
The [Mossinghoff–Rhin–Wu theorem](../../../../../audits/literature/MRW08/Yin_U001.md#degree) excludes this, since \(T\) is below Lehmer's measure.
For a rational comparison its degree-ten polynomial has negative value at \(T>1\) and a unique exterior root.
Thus the result covers every polynomial in the stated irreducible reciprocal class and excludes the smaller factor required at prime 223.

<a id="recurrence"></a>
## Enumerating coefficients and testing reflected sums

Write \(P=X^D+c_1X^{D-1}+\cdots+c_D\), with \(c_0=1\), \(h=D/2\) and \(c_{D-i}=c_i\).
For the power sums \(s_k=\sum_{P(\alpha)=0}\alpha^k\), let \(B_k\) be the [certified bounds](../../readme.md#bounds) for \(1\le k\le h\).
Given the first \(k-1\) coefficients and sums, set \(A=\sum_{j=1}^{k-1}c_{k-j}s_j\).
Choose each integer \(s_k\in[-B_k,B_k]\) with \(s_k\equiv-A\pmod k\) and put \(c_k=-(A+s_k)/k\).
Newton's identities give exactly this necessary and sufficient condition for the next coefficient to be integral.
At index fifteen apply every [version-two trace-box inequality](../v2/readme.md#sieve), including its shorter prefixes and all five orders.
The native code uses floors at the same fixed scale as version two and an uncertainty margin \(\sum_{j\le k}|s_j|\); it tests the original integers with their common denominator if this margin meets the boundary.

At the center discard polynomials in \(\mathbb Z[X^q]\) for \(q\mid D\), \(q>1\), by testing whether every \(c_j\) with \(q\nmid j\) vanishes through \(h\).
Reflection gives the other half of this test.
Choose the sign for which the first nonzero odd-indexed sum through \(h\) is positive.
If all these odd sums vanish, Newton's identities successively give zero for every odd-indexed coefficient through \(h\), and the polynomial belongs to \(\mathbb Z[X^2]\).
The fourteen slices obtained by choosing the degree and \(s_1\in\{0,1,\ldots,6\}\) exhaust the representatives.
When \(s_1>0\), \(c_1=-s_1\ne0\) already excludes any power substitution.

After reflection no free coefficients remain.
Newton's identities give the higher sums by
\[
  s_k=-\boldsymbol{1}_{k\le D}\,k c_k-
        \sum_{j=1}^{\min(D,k-1)}c_j s_{k-j}.
\]
The indicator term is omitted when \(k>D\).
For \(h<k\le120\) require
\[
                         |s_k|\le\lfloor D-2+T^k+T^{-k}\rfloor.
\]
This follows from reciprocal pairs and the Mahler bound by the [convexity estimate](../../../../../ledger/Yin_L_G0462_v266.md#linear).
The program computes the integer caps from rational powers of \(T\).
At either degree, any representative vanishing at \(1\) or \(-1\) has a proper linear divisor.

For the native integer arithmetic take \(C_0=1\) and \(C_k=\lfloor\sum_{i=1}^k B_i C_{k-i}/k\rfloor\) up to \(h\).
Induction gives \(|c_j|\le C_j\).
At the two degrees the largest \(C_j\) are respectively 459,483 and 670,668, and the sums including \(C_0\) are 2,262,290 and 3,329,784.
These bounds put the partial Newton numerators through \(h\) within signed 32-bit range.
Write \(L\) for the maximum of \(D\) and all the trace caps through 120.
At a new index, every earlier sum has passed, so \(2L\sum_{j=0}^h C_j\) bounds the entire sum of absolute terms, including the Newton coefficient term.
This is within signed 64-bit range in both runs.
The score estimates at the fifteen-index prefix have their separate [integer error control](../v2/readme.md#sieve).

<a id="last-tests"></a>
## Cyclotomic divisibility and Graeffe coefficients

For each surviving coefficient vector test divisibility successively by \(\Phi_n\) with \(1\le n\le2D\) and \(\varphi(n)\le D\).
The monic polynomial \(\Phi_n\) is computed by dividing \(X^n-1\) by all earlier \(\Phi_d\) for \(d\mid n\).
A nonzero polynomial remainder modulo two rules out the divisor.
For a zero remainder modulo two, test the original integer polynomials by monic long division.
An actual cyclotomic divisor excludes an irreducible noncyclotomic input, including the case of equality.

For the remaining candidates put \(P_0=P\) and \(P_{j+1}(X^2)=P_j(X)P_j(-X)\).
The even degree makes every iterate monic with roots the \(2^j\)-th powers of the original roots.
If \(M(P)\le T\), every coefficient \(a_i\) of \(P_j\) satisfies
\[
                       |a_i|\le {D\choose i} T^{2^j}.
\]
Indeed each product contributing to the elementary symmetric sum has absolute value at most \(M(P_j)=M(P)^{2^j}\).
All expansions and comparisons with the rational right side use arbitrary-precision integers.
The first index \(0\le j\le12\) at which some coefficient strictly exceeds this bound excludes the candidate.
The nonzero rejection counts at indices \(5,6,7,8\) are respectively \(31,52216,7294,4\) in degree 56 and \(81,103616,12188,10\) in degree 58.
For every vector remaining after the Graeffe tests, multiply by \(X+1\) over the integers and compare the coefficients with \(X^{59}+1\).
Exactly one vector reaches this test, and equality holds.
Since 59 is prime, the quotient is \(\Phi_{118}\).

<a id="reproduction"></a>
## Reproducing the complete census

Generate the [first-half inputs](../../readme.md#reproduction) and the [version-two total](../v2/readme.md#reproduction).
From the repository root run the [enumeration driver](reciprocal.py) and the [integer finishing tests](finish.py).

~~~text
python mathematics/computations/programs/Yin_J_G0179/versions/v3/reciprocal.py
python mathematics/computations/programs/Yin_J_G0179/versions/v3/finish.py
~~~

The driver compiles [the native recurrence](Reciprocal.cs) with the .NET Framework C# compiler on Windows.
On a system with Mono it selects the corresponding compiler and runtime.
One degree and one first sum can be supplied to run a single slice.
The generated [summary](../../../../outputs/Yin_J_G0179/versions/v3/summary.json) records counts for each slice, the first successful cyclotomic order or Graeffe index, and any unresolved coefficient vectors.
The adjacent per-slice files store counts through every higher index and the half coefficients of every endpoint survivor.
