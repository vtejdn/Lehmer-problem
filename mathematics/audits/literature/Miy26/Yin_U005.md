---
author: Yin
---

# Homogeneous polynomials and products of circular increments

## Miy26-U005

- Source: [Miy26](../../../literature/pdf/Miy26.pdf), arXiv:2603.19528v2, 2026-04-21.
- Locator: Example 4.3, pp. 14-15; Proposition 4.4, p. 15; Example 4.5, pp. 16-17.
- Record: 2026-09-08, circular-section agent; local reconstruction and exact finite verification, with independent quadratic-agent review recorded below.
- Kind: two explicit spectral computations and their Brown-support interfaces.
- Reading state: audited within the stated scope, retaining the identified external cumulant and Brown-measure inputs.

### Setting and reusable statements

Use the standard free circular normalization and the distinction between full `L2(M,tau)` and holomorphic `H2_c` in [Miy26-U004](Yin_U004.md#miy26-u004).
All coefficients are scalar, and `tau` is faithful and normal on the finite von Neumann algebra `M`.

For a positive integer `n>=1`, let

\[
f=\sum_{|w|=n}a_w c_w,\qquad
r=\|f\|_2=\left(\sum_{|w|=n}|a_w|^2\right)^{1/2}.
\]

Example 4.3 and Proposition 4.4 give

\[
\operatorname{spec}(f)=\operatorname{supp}\mu_f
=\{\lambda:|\lambda|\le r\},
\]

and `f` is R-diagonal.
The zero polynomial is included, with spectrum and Brown support `{0}`.
Degree zero is excluded: a nonzero scalar does not satisfy this centered-disk or R-diagonal conclusion.

For `k>=1`, a free circular family `c_1,...,c_k`, and real `t`, Example 4.5 concerns

\[
F_{k,t}=(1+tc_1)\cdots(1+tc_k).
\]

The formula valid at every complex `lambda` and every real `t` is

\[
\operatorname{spec}(F_{k,t})=
\left\{\lambda:\ |\lambda-1|^2
\le t^2 S_k(|\lambda|^{2/k})\right\},
\qquad S_k(b)=\sum_{j=0}^{k-1}b^j.
\tag{3}
\]

It also equals the Brown-measure support, using the precise external result in [U008](Yin_U008.md#miy26-u008).
Formula (3) replaces the source's quotient at `|lambda|=1` by its continuous value and avoids its intermediate divisions by `t`.

### Homogeneous coefficient calculation and sufficiency

If `(lambda-f)^(-1)` is square-integrable, U004 puts its vector in the positive-word subspace.
The vacuum coefficient equation is `lambda alpha_empty=1`, so `lambda!=0`.
The remaining equations uniquely determine

\[
\alpha_w=0\quad(n\nmid |w|),\qquad
\alpha_{w_1\cdots w_j}
=\lambda^{-j-1}a_{w_1}\cdots a_{w_j}
\quad(|w_1|=\cdots=|w_j|=n).
\]

Unique segmentation into blocks of length `n` is essential here.
Consequently

\[
\sum_w|\alpha_w|^2
=|\lambda|^{-2}\sum_{j\ge0}(r/|\lambda|)^{2j}.
\]

Necessity gives `|lambda|>r`.
For the converse, when this inequality holds, the displayed coefficients define `X in H2_c`; multiplication by the bounded polynomial gives `(lambda-f)X=1` by the coefficient recursion.
The finite-algebra inverse argument in U004 identifies `X` as the affiliated inverse, and Corollary 1.2 makes it bounded.
This explicitly closes the sufficiency direction that is compressed into the source's phrase “if and only if.”
The point `lambda=0` is never a resolvent point, by the same vacuum equation.
For `r=0`, all nonzero `lambda` work.

### R-diagonality and the Brown inner radius

The source invokes the cumulant product formula and the powers argument in [NS06](https://rolandspeicher.com/wp-content/uploads/2020/06/nica-speicher-book.pdf), Theorem 11.12 and Proposition 15.22, printed pp. 180 and 253-254.
The exact product-formula statement and the mixed-cumulant theorem (Theorem 11.16, p. 183) were checked directly and accepted for this scalar tracial setting; their complete proofs are not independently re-audited.
Proposition 15.22's relevant combinatorial proof was directly inspected.

Here is the precise adaptation.
Multilinearity expands a cumulant in `f,f*` into words of the same length `n`.
The product formula sums over noncrossing partitions whose join with those consecutive length-`n` blocks is connected.
A surviving block cumulant must have one variable label and alternating adjoint signs, by freeness and R-diagonality of the circular family.
The color-independent connectivity argument of Proposition 15.22 then excludes adjacent equal signs of the outer blocks: the block meeting their boundary either starts there or has a preceding opposite sign, and in either case balance and noncrossingness isolate an interval of complete length-`n` blocks.
Odd outer length is excluded by sign balance.
Thus only alternating even cumulants survive.
This checks the source's multilinear extension; its accidentally displayed `f^n,f^n` should be `f,f` at that step.

The same argument establishes the source's R-diagonality remark for homogeneous polynomials in any star-free R-diagonal tuple.
It does **not** extend the circular coefficient norm or centered-disk formulas to that broader tuple.

R-diagonality alone does not prove a zero Brown inner radius.
For this `f`, if an affiliated inverse belonged to `L2`, U004 applied at `lambda=0` would make it holomorphic; `-f X=1` would then contradict the vacuum coefficient.
Hence `||f^(-1)||_2=infinity`, with the usual infinite value if there is a kernel.
The retained Haagerup-Larsen support theorem in U008 gives inner radius zero and outer radius `||f||_2`.
The nonzero constant-modulus exceptional case would make `f` invertible and is ruled out by `0 in spec(f)`; `f=0` is handled directly.
Therefore the Brown support is the disk already found for the spectrum.
There is no appeal here to an unproved general equality of spectrum and Brown support.

### Product coefficients and the transfer matrix

Assume first `lambda!=1`.
Every nonempty word `w` over `{1,...,k}` has a unique decomposition into maximal strictly increasing consecutive runs.
Let `N=|w|` and let `m` be the number of runs.
Equivalently `N-m` is the number of ascents `w_j<w_(j+1)`, with `1<=j<N`.
Expanding the product and comparing coefficients yields

\[
\alpha_\varnothing=(\lambda-1)^{-1},\qquad
\alpha_w=\frac{t^N\lambda^{N-m}}{(\lambda-1)^{N+1}}.
\tag{4}
\]

Indeed, for a maximal initial run of length `h`, the coefficient equation sums over all possible nonempty increasing prefixes.
Iterating it amounts to the compositions of `h`; their sum is

\[
t^h\sum_{j=1}^{h}\binom{h-1}{j-1}(\lambda-1)^{-j}
=t^h\lambda^{h-1}(\lambda-1)^{-h}.
\]

Multiplying these run factors proves (4), including `lambda=0` with the polynomial convention `0^0=1`.
The source's count of ascents should stop at `N-1`, since there is no `(N+1)`st letter.

Set `a_N=sum_(|w|=N)|alpha_w|^2`, `a=|lambda|^2`, and

\[
M(a)_{ij}=\begin{cases}a,&i<j,\\1,&i\ge j.\end{cases}
\]

The row index is the earlier letter, so an increasing transition carries the weight `a`; reversing this convention transposes the matrix and must be done consistently.
Direct word summation gives, for `N>=1`,

\[
a_N=\frac{t^2}{|\lambda-1|^4}\,
\mathbf1^T\left(\frac{t^2 M(a)}{|\lambda-1|^2}\right)^{N-1}\mathbf1.
\tag{5}
\]

All entries and both boundary vectors are nonnegative.
For `t!=0` and `lambda!=0,1`, positivity makes the Perron mode visible in this scalar expression.
Thus `a_N->0` and `sum_N a_N<infinity` are equivalent here, and both hold precisely when `t^2 rho(M(a))<|lambda-1|^2`.
This equivalence is justified by the positive finite recurrence, not by a general claim that scalar coefficients of every recurrence must detect its largest eigenvalue.

At `lambda=0`, `M(0)` is lower triangular with every diagonal entry one, and

\[
\mathbf1^T M(0)^j\mathbf1=\binom{j+k}{k-1}.
\]

Hence (5) is summable exactly when `t^2<1`; it fails to tend to zero at equality.
At `t=0`, the product is the identity and is treated directly.
At `lambda=1`, the vacuum coefficient equation has no solution, so this point belongs to the spectrum for every `t`.

### Perron eigenvalue, removable singularities, and boundaries

For `a!=1`, the source's characteristic polynomial is

\[
\det(xI-M(a))=\frac{(x-1+a)^k-a x^k}{1-a}.
\]

Subtracting successive rows of the eigenvector equations gives `x(v_i-v_(i+1))=(a-1)v_(i+1)`, from which this polynomial and its eigenvalues follow.
The quotient requires continuation at `a=1`, where `M(1)` is the all-ones matrix and the characteristic polynomial is `x^(k-1)(x-k)`.

A simpler nonsingular derivation of the eigenvalue needed for (5) works for every `a>=0`: put `b=a^(1/k)`, `rho=S_k(b)`, and `v_i=b^(k-i)`.
Direct substitution yields `M(a)v=rho v`.
For `a>0`, this vector is strictly positive, so positivity (or the weighted maximum norm) proves that `rho` is the spectral radius.
For `a=0`, triangularity gives `rho=1`.
Thus

\[
\rho(M(|\lambda|^2))=S_k(|\lambda|^{2/k})
\]

also at `|lambda|=1`, where its value is `k`.
Combining this with (5), the explicit boundary cases, and the same `AX=1` sufficiency argument used above proves (3).

Useful exact checks are: `k=1` gives the disk `|lambda-1|<=|t|`; `t=0` gives `{1}`; `0` belongs to the spectrum exactly when `|t|>=1`; on the unit circle (3) reads `|lambda-1|^2<=k*t^2`.
These checks include the parameters excluded by the printed intermediate divisions.
The original quotient `(|lambda|^(2/k)-1)/(|lambda|^2-1)` has the value `1/k` on that circle, not zero or infinity.

### Brown support for the product and retained interface

The primary interface checked by the external-input agent is [DHH+25](https://arxiv.org/html/2510.10712v1) (cited as DHH+25 in Miy26), Theorems 1.25 and 1.27-1.28, in [U008](Yin_U008.md#miy26-u008).
In its notation use `u_0=1` and `t_DHH=k*t^2`, so every circular increment is multiplied by `sqrt(t_DHH/k)=|t|`.
For negative `t`, simultaneous multiplication of the circular family by `-1` preserves its joint star-distribution and hence its Brown measure and spectrum.

For the circular input, the inverse-square integrability parameter is infinite and the theorem's possible excluded inner disk is empty.
Its threshold function is `k*|lambda-1|^2/S_k(|lambda|^(2/k))`.
The degenerate `t=0` distribution is `delta_1` and is checked directly.
These are precise uses of that primary support theorem; its 109-page original proof is not independently audited here.
U008 records the actual version, theorem hypotheses, acceptance decision, and remaining coverage limits.

For completeness, the boundary conversion is local, not an assumption imported from that theorem.
Put `g(lambda)=|lambda-1|^2/S_k(|lambda|^(2/k))`.
For `t!=0`, every point on `g=t^2` is approached by points with smaller `g`: off the nonnegative real ray, rotate its argument toward zero at fixed modulus; at zero, move a small positive distance; on that ray, move the radius toward `1`.
The last assertion follows because `(r-1)^2/S_k(r^(2/k))` decreases for `0<r<1` and increases for `r>1`: writing the denominator as `D(r)`, one has `0<=D'(r)/D(r)<2/r`, so its logarithmic derivative has the required sign.
The point `1` has `g=0` and is not on this positive boundary.
Continuity then proves that the closure of the strict sublevel set is precisely (3).

### Verification facts, searches, and downstream effects

On 2026-09-08 source pp. 14-17 were read from extracted text and the rendered pages were inspected.
The homogeneous recursion, one-sided-inverse sufficiency, the Brown inner-radius obstruction, increasing-run calculation, transfer orientation, Perron argument, and all stated degenerate cases were reconstructed.
The exact check passed 134,443 checks for the Example 4.5 formulas and matrix specializations, as part of 193,363 total checks shared with U004.
The native program and execution account are located at [original J_F0006](readme.md#original-native-checks).
The source-only fixed program encodes its required finite inputs and needs no separate dataset.
The recorded result and rerun scope remain historical evidence; this locator repair performs no new run.

The suspected compression in the R-diagonality proof triggered the primary-source query `Nica Speicher Lectures combinatorics free probability Proposition 15.22 pdf R-diagonal homogeneous`.
The author-hosted NS06 PDF and its [author errata page](https://rolandspeicher.com/literature/nica-speicher/) were inspected on 2026-09-08; the latter reports a 2026-01-11 update and no affected correction to Proposition 15.22.
Exercise 15.25(2), printed p. 255, independently confirms that the quadratic multilinear extension is an intended application.
The search stopped when the necessary color-independent mechanism was found.
No whole-book audit or author confirmation of Miy26's typographical corrections is claimed.

The quadratic-spectrum agent independently read this unit and the NS06 Proposition 15.22 proof on 2026-09-08.
That review checked the color-independent extension, zero Brown inner radius, product coefficients, transfer matrix, and degenerate parameters.
Its request to spell out the strict-to-weak sublevel closure was resolved by the explicit angular/radial argument above.
No unresolved gap was found in that scope; this is independent AI review.

These units support [Miy26 spectral source audit](readme.md#miy26-spectral-source-audit).
No general spectrum/Brown-support conjecture, arbitrary R-diagonal spectral extension, formal verification, or external human review is claimed.

## Source and inspection

Source edition: Miy26, arXiv:2603.19528v2, dated 2026-04-21; the registered 23-page artifact. Printed page numbers equal PDF page numbers. Other works retain the separate versions and limitations stated in the body.

Passages: Example 4.3, pp. 14-15; Proposition 4.4, p. 15; Example 4.5, pp. 16-17.

Inspection: 2026-09-08: coefficients, the R-diagonal adaptation, transfer matrix, inverse construction and all stated scalar boundary cases reconstructed and independently cross-reviewed, with exact finite checks. Specified Brown-support statements retain their accepted external-interface scope; no whole-book audit, general spectrum/Brown-support claim, formal verification or external human review.
