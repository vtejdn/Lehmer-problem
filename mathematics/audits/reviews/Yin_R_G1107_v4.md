---
author: Yin
---

# Review of positive-unit moment shells and finite ternary exclusions

On 2026-11-08 at 06:18 UTC a separately assigned agent completed this review of the fixed ledger arguments and finite computations for Yin.
The reviewer took no part in their development and received the fixed input paths and review scope without proof-generation dialogue or a development summary.
The unit signature image, the odd-grid quadrature and the prefix implication used below were read in their cited fixed sources.
The findings concern the ternary chamber and the specified finite runs.

<a id="square-moment-review"></a>
## Square roots, moment forms and the whole lift

In the order \(\mathcal O=\mathbb Z[t]/B\), evaluation embeds its additive group as a full lattice in \(\mathbb R^n\).
The logarithms of absolute unit values have component sum zero on each of the \(m\) disjoint layers, and bounded logarithms come from a finite set of lattice elements.
The logarithmic image is therefore free of rank at most \(n-m\).
Each torsion sign is constant on a field component, and reduction of an integral representative modulo three at \(2\) forces the same sign on every component.
Thus the logarithmic kernel has order two.
The [signature criterion](../../ledger/Yin_L_G0464_v8.md#arbitrary-input-lower-bound) gives \(2^{n-m+1}\) possible unit signatures, since there are \(m-1\) independent equal-parity equations.
The signature quotient attains the upper bound for the number of square classes, proving equality of the totally positive units and the squares and giving exactly two roots for each square.

The odd-grid quadrature applies to products \(U_i(t/2)U_j(t/2)\), whose degrees are at most \(2n-2\).
Multiplication by \(t\) has symmetric Jacobi matrix \(J\) with a final diagonal \(-1\) from \(U_n=-U_{n-1}\) at the nodes.
The orthogonal weighted evaluations conjugate \(J\) and \(H=h_0(J)\) to their evaluations, which gives the two forms, the positive gap form and its stated determinant.
The integral determinant test on \(v(J)\) is equivalent to the existence of \(v^{-1}\in\mathcal O\).
The ellipsoid is bounded for each strict separator, and substituting a unit square into the base induces unimodular congruence by its square root.
At an angular midpoint \(|B(c)|\ge1\), while \(L-cK\le8+2\cdot6=20\).
The Gaussian majorant with parameter \(n/(2S_0)\) gives the stated volume bound, and \(40\pi\mathrm e<364\).
Volume gives the mean count over translations and does not decide occupancy at the specified origin.

Under the strict endpoint, \(n-2\) same-sign gaps and the interval below the least pole contain \(n-1\) distinct interior trace roots.
Their lifts supply \(2(n-1)\) unit-circle roots, and each of the two remaining trace roots supplies at most one exterior lift root.
With two or more unit-circle roots, the product of the two largest moduli equals the whole Mahler measure, including multiplicities.
Triangularizing the companion matrix gives precisely these pair products among the eigenvalues of its second exterior power.
The finite accepted unit set yields the eventual exponent-box probability, using injectivity of multiplication by the nonvanishing \(h_0\) and uniform counting in a basis of the rank \(n-m\) positive unit group.
The assertion concerning positive mass across conductors uses positive mass on each allowed joint sample.

<a id="shell-enumeration-review"></a>
## Exhaustive enumeration at \(p=27,\ k=8,\ \Delta=32\)

I replayed [J151](../../computations/programs/Yin_J_G0151/shell.py) on all five profiles and constructed a separate finite calculation.
I enumerated all \(2^{13}\) column subsets to recover the unique sign columns \(4,5,6,8,9,10,13\).
I formed their trace product and divided the even scale factors in \(\mathbb Q[t]/B\), checking that the representative was integral with the required resultant.
In the different basis \(1,T_1,\ldots,T_{12}\), where \(T_i(z+z^{-1})=z^i+z^{-i}\), take \(\ell(f)\) to be the coefficient of \(t^{12}\) in \(Df\bmod B\).
The Gram entries are \(\ell((2t-1)h_0 T_iT_j)\), using \(1\) at index zero.
An integral Gram reduction with checked unimodular change followed by rational \(LDL^T\) completion of squares enumerated both global signs, retaining the lexicographically larger member of each pair at the leaf.
Exact integer square roots bound each interval in the rational recursion.
The determinant is \(372384\).
I recomputed both moments and the unit resultant on the resulting polynomials.

| \(x\) | Target \(2L-K\) | Half shell | Both moments | Units | Strict endpoints |
| ---: | ---: | ---: | ---: | ---: | ---: |
| \(-2\) | 10 | 1481 | 18 | 2 | 0 |
| \(-1\) | 5 | 37 | 1 | 0 | 0 |
| \(0,1,2\) | \(-2,-11,-22\) | 0 | 0 | 0 | 0 |

The fraction-free recursion in J151 itself also enumerates the whole shell.
With \(D_i\) the leading principal minor of order \(i\), \(D_0=1\), fixing the final \(n-i\) coordinates leaves the budget \(D_i\) times the target less \(D_i\) times the Schur-complement contribution of that tail.
This budget is an integer because \(D_i\) times the Schur complement is integral by the adjugate formula.
The next completed-square term has denominator \(D_iD_{i-1}\), so J151's division giving the next budget is exact.
Its two bounds include both integer endpoints, and its sign convention keeps the unique member of each nonzero pair with last nonzero coordinate positive.

For each of the two unit polynomials I isolated all 14 trace roots in rational real intervals and complex rectangles of width at most \(10^{-13}\).
Each has eleven real roots in \((-2,2)\), one below \(-2\), and a nonreal conjugate pair.
For each trace \(q\), set \(s=(|q-2|+|q+2|)/2\).
Its exterior factor is \((s+\sqrt{s^2-4})/2\) for \(s>2\), and the interior real traces contribute one.
Outward-rounded multiplication gave \(5.744036640666<M(P)<5.744036640669\) for \(P(-1)=-1\), and \(7.773973645300<M(P)<7.773973645302\) for \(P(-1)=-33\).
These bounds agree with J151's independent full-lift complex-root products.
Each example has three exterior roots and fails the strict endpoint hypothesis of the exterior-square formula.

<a id="finite-cuts-review"></a>
## Endpoint exclusion and the two-adic strata

Expanding \((b-y)(2-b)/(2+b)\) against \(r_j\) gives \(J=(4+y)K-L-4(2+y)U\), and \(|B(-2)|=1\) makes the endpoint quantity \(U\) integral.
Taking products of \((4-b^2)\) and \((2-b)^2\) on a layer gives respectively \(3\) and \(9\), proving both arithmetic-geometric mean bounds.
On the whole grid \(p|B(y)|>2>(p/(p-1))^n\) suffices for the strict one-half bounds.
I recomputed the signs of the integer recurrence at every displayed rational separator, finding \(5,22,77,254,809\) poles above them and \(p|B(y)|>2\) in all five cases.
The profile inequalities from these bounds leave respectively \(\varnothing,\{0\},\{-1,0\},\{-1,0\},\{-1,0\}\) before the stronger layer tests.

Two generates the primitive trace indices modulo signs and Frobenius in characteristic two permutes them transitively, so the monic layer polynomials are irreducible modulo two and pairwise coprime there.
Their roots are distinct because the odd-order roots are separable and two roots with the same trace are inverses.
Dividing by the common coefficient content at two leaves odd layer norm, hence absolute norm one after extracting the prescribed two-power for an input with pure two-power resultant.
Congruence of all signed norms at three gives constant \(\eta_\ell+t_\ell\bmod 2\).
I independently enumerated these valuation vectors and compared the stated positive rational bounds after raising them to the exact layer degrees.
At \(p=81\) the unique vector \((1,1,0,0)\) gives \(T>5131/8100>14/25\).
At \(p=243\) all seven possible vectors violate the \(x=-1\) budget, with the smallest lower bound \(23236/24300>33/40\).
For \(x=0\) the five rejected vectors exceed the budget \(T=33/20\), while the lower bounds for the other two are \(20839/24300\) and \(32098/24300\).
Applying those latter bounds to \(K-(2+y)U\) forces \(U\le0\), and the integral endpoint then gives \(P(-1)=2+U\in\{1,2\}\).
This proves the displayed profile exclusions, including the qualifications on the chosen resultant.

For common layer valuations, \(2^E h/h_0\in R\) by the adjugate, and the layer units imply divisibility there by \(2^E\) on every component.
The component moduli remain pairwise comaximal modulo \(2^E\) by lifting a Bézout relation over \(\mathbb F_2\).
The Chinese remainder theorem descends this divisibility to \(R\), which shows that \(h/h_0\) is an integral unit of the required signs.
This includes the unique orbit at \(p=27\) by \((2,1,0)\), so the shell enumeration covers all integral inputs with the indicated signs and \(\Delta=32\).
At \(p=243\), \(T_3^8/T_9^2\) is positive and adds \((6,-2,0,0,0)\) to the valuation vector of the constructed representative.
Its denominator has two-power norm and the resulting input is integral on each layer, so the same descent verifies the second representative in the original order.
The existence of representatives in these two strata does not show that either hits both moments and the endpoint.

For the layer-triple filter, the trace of \(T_a\) is the Ramanujan sum at \(3^\ell\), which equals \(0,-d_\ell\), or \(2d_\ell\) by subtracting the two geometric sums.
Normalized traces of integral polynomials are therefore integral.
The product \((2-b)(b-z)(1-vb+v^2)f_\ell(b)\) has the required sign at each node of a mixed layer.
Its average is \((1+v)^2(s_\ell-(2+z)u_\ell)-v(w_\ell-zs_\ell)\), and multiplying its final quadratic factors over inverse pairs gives \(\Phi_{3^\ell}(v)=1+v^{d_\ell}+v^{2d_\ell}\).
This verifies the layer-trace inequality as a necessary test.

<a id="finite-box-review"></a>
## Three finite exponent boxes

I checked all three boxes in [J150](../../computations/programs/Yin_J_G0150/readme.md#whole-measures) with a separate implementation using monomial remainders in \(\mathbb Z[t]/B\).
The sign-column equations were solved by column elimination, and the two factors of each sampled word used alternating generator positions.
For each left polynomial \(f\), I enumerated \(\ell(t^i f)\) for \(0\le i\le n\), with \(\ell(g)\) the coefficient of \(t^{n-1}\) in \(Dg\bmod B\).
Taking dot products with the right polynomial's monomial coefficients at offsets zero and one gives the moments \(K,L\).
I screened \(K\) modulo \(65536\), rechecked each modular match over the integers, formed the actual \(Q\) for each joint match, deduplicated on all coefficients of \(Q\), and multiplied every root contribution of its reciprocal lift with multiplicity using complex ball arithmetic.
This also checks the J150 treatment of a remaining conjugate pair via its two focal distances and the first two Newton sums.

| \((p,k)\) | Word count | Counts for \(K=2,3,6\) | Joint words | Different \(P\) | Strict-endpoint words |
| --- | ---: | --- | ---: | ---: | ---: |
| \((27,8)\) | 282475249 | 6391, 6218, 6236 | 2 | 2 | 0 |
| \((81,18)\) | 47775744 | 33843, 33786, 34367 | 70 | 14 | 0 |
| \((27,3)\) | 9765625 | 1211, 1309, 1363 | 48 | 48 | 1 |

All three reported ranges of whole measures agree to the displayed millionths.
At \(p=81\) the minimum is between \(7.162445\) and \(7.162446\) and the maximum between \(18.538189\) and \(18.538190\).
At \((27,3)\) they are between \(2.867493\) and \(2.867494\) and between \(32.452990\) and \(32.452991\), respectively.
I evaluated the two displayed exponent witnesses for \((27,8)\) and the single strict witness for \((27,3)\) directly in the prescribed generator order.
For the latter \(x=0,\ P(-1)=1,\ 3.349927<M(P)<3.349928\), so the specified uniform joint sampling has probability \(1/(5\cdot5^{10})\) for this event.
The exhaustive orbit conclusion for \((27,8)\) uses the separate square-shell and valuation arguments above.
The \((27,3)\) counts concern just its specified exponent box.

<a id="third-moment-review"></a>
## The third moment at \(p=243\)

For \(F(t)=4+4t-t^2\), the signs at \(-5/6,-33/40\) have numerators \(-1,31\) over the positive squared denominators.
The two rational endpoints each have exactly 77 poles above them, so the smaller zero of \(F\) is a strict sign separator.
The other zero exceeds every trace.
Thus \(F(b_j)r_j>0\), and their product is \(p^{1-n}\Delta|\operatorname{Res}(B,F)|\).
For an independent resultant calculation I reduced \(B\) in the quadratic ring with \(t^2=4t+4\), using the odd-grid recurrence.
Writing its remainder as \(u+vt\), its absolute norm \(|u(u+4v)-4v^2|\) agrees with the program's resultant.
I checked \(n^np\Delta|\operatorname{Res}(B,F)|>(jp)^n\) with \((\Delta,j)=(1,2),(2^{53},3)\).
The arithmetic-geometric mean lower bound for \(\sum F(b_j)r_j=8-N\), together with the integral coefficient \(N\) in \(C/B\), gives \(N\le5\) for every nonzero resultant and \(N\le4\) at the prescribed one.
The arcsine fourth moment is \(6\), so the \(x=0\) next-moment condition fails even without an endpoint test.
The argument tests every input with the specified sign cut and first two moments at this single conductor.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Square and moment review](#square-moment-review) | independently reviewed |
| [Finite shell review](#shell-enumeration-review) | independently reviewed |
| [Finite cut review](#finite-cuts-review) | independently reviewed |
| [Finite box review](#finite-box-review) | independently reviewed |
| [Third moment review](#third-moment-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Square and moment review](#square-moment-review) | [Positive squares](../../ledger/Yin_L_G0464_v10.md#positive-squares) | Unit square classes in the original order, using the established signature image. |
| [Square and moment review](#square-moment-review) | [Moment ellipsoid](../../ledger/Yin_L_G0464_v10.md#moment-ellipsoid) | Quadrature, determinant, integral shell, unit test, congruence and volume. |
| [Square and moment review](#square-moment-review) | [Whole measure and probability](../../ledger/Yin_L_G0464_v10.md#whole-measure-and-probability) | Strict endpoint root count, exterior square, finite unit support and sampling. |
| [Finite shell review](#shell-enumeration-review) | [J151 program](../../computations/programs/Yin_J_G0151/shell.py) | All five \(p=27\) profiles, unit and endpoint counts and whole Mahler measures. |
| [Finite shell review](#shell-enumeration-review) | [J151 whole class](../../computations/programs/Yin_J_G0151/readme.md#complete-27) | Entire prescribed sign and resultant class, counts and strict outward enclosures at \(p=27\). |
| [Finite shell review](#shell-enumeration-review) | [J151 traversal](../../computations/programs/Yin_J_G0151/readme.md#enumeration) | Exact bounds, integer budget recurrence and full-lift product with multiplicity. |
| [Finite cut review](#finite-cuts-review) | [Endpoint sums](../../ledger/Yin_L_G0464_v11.md#endpoint-moment-test) | Integer endpoint, two positive sums and layer bounds. |
| [Finite cut review](#finite-cuts-review) | [Finite exclusions](../../ledger/Yin_L_G0464_v11.md#finite-exclusions) | Five separators, universal inequalities and fixed-resultant exclusions at 81 and 243. |
| [Finite cut review](#finite-cuts-review) | [Valuation orbits](../../ledger/Yin_L_G0464_v11.md#layer-valuations-and-orbits) | Integral descent, orbit uniqueness at 27 and 81, two surviving strata and the endpoint values at 243. |
| [Finite cut review](#finite-cuts-review) | [Layer trace test](../../ledger/Yin_L_G0464_v11.md#layer-trace-test) | Normalized trace integrality and the mixed-layer positive-product inequality. |
| [Finite box review](#finite-box-review) | [J150 generator choices](../../computations/programs/Yin_J_G0150/readme.md#fixed-cut-moments) | Ordered positive units and the three actual exponent sets. |
| [Finite box review](#finite-box-review) | [J150 finite results](../../computations/programs/Yin_J_G0150/readme.md#whole-measures) | Every word in all three boxes, counts, witnesses, whole-measure ranges and stated sampling probability. |
| [Finite box review](#finite-box-review) | [J150 computation](../../computations/programs/Yin_J_G0150/moments.py) | Bilinear moment sieve, coefficient checks and whole-root contribution for real and nonreal traces. |
| [Third moment review](#third-moment-review) | [J151 quadratic separator](../../computations/programs/Yin_J_G0151/readme.md#quadratic-separator) | Gap, full product, integral certificate and failure of the third moment at \(p=243\). |
| [Third moment review](#third-moment-review) | [J151 integer check](../../computations/programs/Yin_J_G0151/shell.py) | Exact comparison for the two stated resultant bounds at 243. |
