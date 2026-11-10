---
author: Yin
---

# Independent review of rational linear-cut square prefix rigidity

<a id="scope"></a>
## Review act, relationship and final inputs

This independent whole-proof review was performed at 2026-11-09T19:40 UTC by a separately arranged agent acting for Yin.
The reviewer did not participate in developing [C880v4](../../claims/Yin_C_G0880_v4.md#statement), received no development discussion and supplied no proof repair.
After the responsible main agent renamed the constant intercept to \(\beta\), the reviewer reread the complete stable final text, with the polynomial \(B_0=1\) retained separately.
That notification concerned notation only and supplied no mathematical explanation or repair for this review.
The review uses the fixed argument directly, not an author summary.

This new R family concerns the prefix classification of a rational linear factor times an integer square and its exact finite-grid interfaces.
The earlier single-term and adjacent-perturbation reviews concern different objects and supply no finding for this proof.
The present scope includes the whole classification for arbitrary degree, every quadratic-form and endpoint formula, the complete small-control polynomial, the Newton lower bound and the precise limits of the comparison with older C880 versions.
Only the necessary fixed predecessor interfaces were checked; the older gap theorems were not re-audited in full.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v4 setup and comparison](../../claims/Yin_C_G0880_v4.md#scope) | Exact no-wrap domain, original trace/lift, rational cut and scoped comparison with existing square-input results. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v4 statement](../../claims/Yin_C_G0880_v4.md#statement) | Entire if-and-only-if classification, next-prefix obstruction, all-conductor sign/endpoint assertion and small-control lower bound. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v4 quadratic forms](../../claims/Yin_C_G0880_v4.md#quadratic-forms) | Semicircle normalization, all coordinate forms, moment forms, equivalent prefix equations and exact finite-grid degree ranges. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v4 endpoint](../../claims/Yin_C_G0880_v4.md#endpoint) | Negative moment, tail-sum form, exact finite interpolation and integer endpoint equivalence. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v4 classification proof](../../claims/Yin_C_G0880_v4.md#classification-proof) | Norm reduction, all four parameter pairs, every degree branch and both signs of the final residual coefficient. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v4 small control](../../claims/Yin_C_G0880_v4.md#small-control) | Unique input's signs and endpoint for all odd p at least nine, complete p=9 polynomial and Newton lower bound. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v4 limitations](../../claims/Yin_C_G0880_v4.md#limits) | No-wrap restriction, failure of transfer to higher-degree reduced inputs, original-subfamily gap scope and unresolved finite targets. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C881v3 prefix coordinates](../../claims/Yin_C_G0881_v3.md#prefix-coordinates) | Exact x=0 coefficient requirements, indexing and permitted prefix range. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [L464v5 full odd grid](../../ledger/Yin_L_G0464_v5.md#odd-grid-product) | Exact residue weights, original lift and semicircle quadrature through degree 2n-2. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v3 square-family statement](../../claims/Yin_C_G0880_v3.md#statement) | Application only to A=N, beta=2N-1 with N at least two and all original strict sign and endpoint hypotheses. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v2 fixed-cut consequence](../../claims/Yin_C_G0880_v2.md#moving-cut) | N=1 comparison at the fixed algebraic separator, retaining the strict chamber and endpoint hypotheses. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [C880v1 original lift domain](../../claims/Yin_C_G0880_v1.md#statement) | Only the general monic integral simple-pole domain inherited by the fixed-cut comparison. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [L462v6 residual comparison](../../ledger/Yin_L_G0462_v6.md#integer-residual) | Contextual distinction: full quotient-lattice subfamily and x=-1 residual sphere, not a premise of the new classification. |
| [Linear-cut prefix finding](#linear-cut-prefix-review) | [L464v10 square ellipsoid comparison](../../ledger/Yin_L_G0464_v10.md#moment-ellipsoid) | Contextual distinction: chosen representative times a unit square, without an automatic long-prefix conclusion. |

<a id="coordinate-checks"></a>
## Coordinate forms and their finite-grid scope

Because \(A>0\) and \(g\ne0\), the degree of \(h\) is exactly \(2d+1\), so the hypothesis gives \(2d+1<n\) without possible leading cancellation.
The monic integral triangular Chebyshev basis makes every \(u_i\) integral.
The sine substitution verifies the stated probability normalization and orthogonality.
The exact product rule gives the entry condition for \(H_k\), including parity and both endpoint inequalities, and the recurrence with \(E_{-1}=0\) proves equation (6) also at \(k=0\).

The first moment uses the half-line tridiagonal multiplication matrix with zero lower boundary.
The coefficients \(y_i\) include the extra top coefficient \(y_{d+1}=u_d\); this verifies both the norm formula for \(M_2\) and the adjacent-coefficient formula for \(M_3\).
The equations (8) are obtained by integrating \(h,(t+2)h,(t+2)^2h\), respectively.
Since \((t+2)^2=E_2+4E_1+5E_0\), the target right sides are exactly \(2,4,14\), and the triangular relation proves the claimed equivalences.
No moment condition has been silently substituted for the wrong prefix index.

For \(0\le k<n\), \(\deg(hE_k)\le2n-2\), so every actual coordinate matches the original finite grid.
For \(M_\ell\), the necessary range is precisely \(2d+\ell\le2n-2\), as stated.
In particular \(2d+2\le n\le2n-2\) for \(n\ge2\), which covers the first two equations.
For the third equation, \(2d+3\le n+1\le2n-2\) when \(n\ge3\); this is exactly the range where \(a_2\) is available.
The small n boundary is therefore accounted for, and no unrestricted moment or rational-function quadrature is assumed.

<a id="endpoint-checks"></a>
## Negative moment and original endpoint

The density divided by \(t+2\) is integrable at the left endpoint.
The displayed substitution gives \(I_0=1\), and \(t/(t+2)=1-2/(t+2)\) gives \(I_1=-1\).
The recurrence for the remaining integrals has zero \(\int E_k\,d\mu\) term for every \(k\ge1\), proving \(I_k=(-1)^k\).
In the product expansion, all \(\min(i,j)+1\) terms have the same parity, yielding the signed minimum matrix in (10).
Expanding the tail squares counts each coefficient pair exactly \(\min(i,j)+1\) times, proving the second expression for \(M_{-1}\).

The identity \((t+2)W_n=1+(-1)^{n-1}B_n\) has the stated sign and constant term.
The product \(hW_n\) has degree at most \(2n-2\), so quadrature legitimately identifies the finite endpoint sum with \(\sum(-1)^ia_i\).
Substituting \(-2\) in the original partial fractions gives \(-2-U\), and \(B_n(-2)=(-1)^n\) converts this to \(P(-1)=2+U\).
As U is an integer, strict endpoint positivity is exactly \(U\ge-1\), with no lost equality case.
For the separate finite interpretation of \(M_{-1}\), the product \(g^2W_n\) has degree at most \(2n-3\), and \(\deg g^2<n\) allows the same alternating-coefficient integral argument.
Thus this rational-looking endpoint identity is an exact polynomial interpolation consequence at the original nodes.

<a id="classification-checks"></a>
## Exhaustion of all degrees and parameter pairs

The two prescribed coordinates give both \(\langle g,w\rangle=2\) and \(\|w\|^2=2\beta\).
The latter norm is strictly positive and its leading term contributes \(A^2u_d^2\), so \(\beta>0\) and \(A^2\le2\beta<4A\).
The integer possibilities are exactly the four displayed pairs, and each permits only \(|u_d|=1\).
The sign replacement therefore loses no input.
These deductions require no bound on d, support or coefficient size beyond the exact original hypotheses.

For \((2,2)\), the leading norm exhausts the budget and leaves w orthogonal to g, contradicting the required inner product.
For \((3,5)\), the constant case is impossible, and the coefficient at degree d must be minus one by its residue modulo three.
It forces \(u_{d-1}=-2\), while the zero coefficient at the next index and \(w\equiv2g\pmod3\) require divisibility by three.
The contradiction includes \(d=1\).

For \((1,1)\), the norm leaves just one additional signed coefficient at some index q.
Descending above that index gives the exact periodic values \(1,-1,0\), so \(u_q\) lies in that set even when \(q=d\).
The inner product is consequently in \(\{-1,0,1\}\), never two.
This handles every degree without a truncation argument.

For \((2,3)\), the odd coefficient at degree d must be \(\varepsilon=\pm1\), leaving exactly one other signed coefficient below it.
The congruence \(w\equiv g\pmod2\) is valid coefficientwise in the integral Chebyshev basis.
When \(\varepsilon=1\), it forces \(q=d-1\), then \(u_{d-2}=0\) and \(\delta=-1\).
The boundary \(d=1\) gives the survivor; \(d=2\) gives the impossible zero-coefficient equation \(-2=0\), and every \(d\ge3\) gives an odd coefficient at an index where parity requires an even one.

When \(\varepsilon=-1\), the successive equations give \(u_{d-1}=-2\), \(u_{d-2}=2\), \(u_{d-3}=-1\), and \(q=d-3\), with the indicated lower-degree impossibilities enforced by parity.
The next equation and boundary or parity give \(u_{d-4}=0\) and \(\delta=1\).
Degree four then has \(-2=0\), while every degree at least five has the next parity contradiction.
The sole remaining degree-three polynomial has inner product minus two, so it fails the required coordinate rather than becoming another solution.
Both signs and every boundary degree in (14) are exhausted.

Independent exact polynomial arithmetic confirmed the two surviving norm-six branch forms:
\[
\begin{array}{c|c|c}
g&w&\langle g,w\rangle\\
E_1-E_0&2E_2+E_1-E_0&2\\
E_3-2E_2+2E_1-E_0&2E_4-E_3+E_0&-2.
\end{array}
\]
For the accepted branch, direct multiplication gives \(h=2E_0-E_2+2E_3\).
Hence the if-and-only-if statement, its \(n\ge4\) condition and its failure of \(a_2=4\) all follow before any chamber or endpoint assumption.
The converse input is actually within the original domain whenever \(n\ge4\).

<a id="small-control-checks"></a>
## All-conductor signs and the complete p=9 lower bound

For \(g=t-1\), the tail-square expression gives \(M_0=2\), \(M_{-1}=5\), hence \(U=-1\) and \(P(-1)=1\).
No odd-grid node equals one, and no node equals the nonintegral rational cut \(-3/2\), since \(B_n\) is monic integral.
The largest pole is positive and the smallest is below \(-3/2\) for every odd \(p\ge9\).
Thus the linear factor with positive slope and the nonvanishing square give precisely a nonempty initial positive block followed by a nonempty terminal negative block.
This is an actual admissible short-prefix supply for every such conductor.

At \(p=9\), direct remainder arithmetic confirmed
\[
Q=t^5+t^4-t^3-4t-1,
\]
and an independent binomial lift gave the ascending coefficient list
\[
(1,1,4,4,3,5,3,4,4,1,1).
\]
It is the complete degree-ten polynomial in (15), with endpoint one.
Newton's identities give \((-1,-7,-1,21)\) for the first four power sums, including all complex roots with their multiplicities.
The triangle inequality therefore gives \(21\le10R^4\) for the largest root modulus, and the full monic Mahler measure is at least R.
The final strict comparison is the exact rational identity
\[
\frac{21}{10}-\left(\frac65\right)^4=\frac{33}{1250}>0.
\]
No factor, root multiplicity or nonreal-root contribution is discarded in this lower bound.
It establishes neither the exact measure nor a common numerical bound for the larger-conductor inputs.

The bounded checks also confirmed the displayed moment and endpoint forms on the two explicit branch polynomials and the W identity at its small boundary cases.
They are arithmetic controls of the written proof, not a search over degrees or a replacement for the all-degree recurrence argument.
No new parameter search, timing experiment or root-isolation run was performed.

<a id="scope-boundaries"></a>
## Older theorem comparison and remaining limits

The map \(r=N,v=g,a=0\) matches the selected C880v3 family exactly for \(A=N,\beta=2N-1,N\ge2\).
That fixed theorem allows arbitrary-degree integer squares, including after reduction in the original quotient, but still requires nonvanishing on the grid, a nonempty strict cut and the endpoint.
For N=1, the fixed algebraic-cut consequence in C880v2 applies only under its same strict chamber and endpoint conditions.
The full odd grid satisfies the original monic simple-pole input domain inherited there.
These are applicable qualitative whole-measure statements for the named subfamily, not ingredients in the new norm classification.
Their existing proofs and external inputs were not re-audited here.

If the unreduced h has higher degree and is reduced modulo \(B_n\), its actual prefix coefficients need not equal the continuum integrals of that unreduced h.
The leading-coefficient norm argument then has no asserted force for the enlarged domain.
Conversely the new classification makes no whole-measure gap claim for arbitrary varying pairs \((A,\beta)\).
The earlier residual-sphere and unit-ellipsoid descriptions are accurate contextual comparisons and do not fill either missing assertion.
The qualitative gap for the named old subfamily supplies no stated numerical constant excluding all isolated values below \(6/5\).

<a id="linear-cut-prefix-review"></a>
## Verdict

No mathematical defect was found in the complete stable C880v4 argument at its declared scope.
The first two x=0 prefix coordinates classify every allowed no-wrap rational linear-cut integer-square input as \((A,\beta)=(2,3)\), \(g=\pm(t-1)\); its next coordinate is minus one rather than four.
The quadratic-form and finite-endpoint interfaces are exact at the stated degree ranges.
The unique short-prefix input satisfies the strict chamber and endpoint for all odd conductors at least nine, and its smallest complete lift is rigorously outside \(1<M<6/5\).
The limitations distinguish this no-wrap classification from the older whole-measure subfamily theorem and from the unrestricted problem.

This finding is independent proof-review evidence for the exact bound inputs and scope above.
It changes no C assessment, Task or execution state and supplies no theorem beyond the fixed statement.
No C, D, S, T, E, navigation, program or Git material was changed by the reviewer; adoption remains with the responsible main agent.
