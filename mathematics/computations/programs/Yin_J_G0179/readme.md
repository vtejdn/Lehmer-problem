---
author: Yin
---

# Certified Newton sum bounds in degrees 56 and 58 at measure 1.089

The [nine-degree census at 1.06](versions/v11/readme.md#census) uses the [larger ellipse certificates](versions/v7/readme.md#weights) to cover even degrees 68 through 84.
The [four degree-specific censuses](versions/v12/readme.md#census) use separate measure cutoffs to test the remaining degree pairs at prime 251, with the certificates and reproduction commands at those versions.
The [thirteen higher-degree censuses](versions/v13/readme.md#census) bound measures in degrees 86 through 110 and restrict the first possible triple of qualifying degrees to prime 499.
The [degree-72 census](versions/v14/readme.md#census) raises its cutoff to 1.068 and excludes that triple.
The [three refined cutoffs in degrees 86, 88 and 92](versions/v15/readme.md#census) exclude the four degree triples at prime 503.

<a id="bounds"></a>
## Question and scope

Let \(P\in\mathbb Z[X]\) be monic, reciprocal, irreducible and noncyclotomic of degree \(D=2d\in\{56,58\}\), with \(M(P)\le T=1089/1000\).
For its roots counted with multiplicity put \(s_k=\sum_{P(\alpha)=0}\alpha^k\).
The following lists give certified upper bounds for \(|s_1|,\ldots,|s_d|\) in order.

| Degree | Absolute Newton sum bounds through the middle coefficient |
| ---: | --- |
| 56 | 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23 |
| 58 | 6, 6, 7, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 12, 13, 13, 14, 15, 15, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24 |

At the [two-value frontier at 223](../../../ledger/Yin_L_G0462_v264.md#frontier), the smaller measure in any qualifying pair is strictly below this cutoff.
Indeed the sum bound there gives \(2\log M_{\min}<(\log2)/4-p^{-1}\log((2pb+1)/(pb+1))\).
At \(p=223,b=114\), the required integer comparison is \(1089^{8p}(2pb+1)^4>1000^{8p}2^p(pb+1)^4\).
The possible pair degrees and this choice of one smaller factor justify treating both degrees here.

<a id="ellipse"></a>
### From ellipse maxima to two-sided integer bounds

Take the eleven integer polynomials \(Q_j\) in the order of the [inspected FRS06 tables](../../../audits/literature/FRS06/Yin_U001.md#printed-example), with any nonnegative rational weights \(e_j=w_j/10^8\).
Write \(g(z)=-\operatorname{Re}z+\sum_{w_j>0}e_j\log|Q_j(z)|\) and \(U(v)=\max_{|y|=\exp(v)}g(y+y^{-1})\).
The value at an active zero is \(-\infty\).
To see convexity of \(U\), multiply \(g\) by \(10^8\) and take the analytic function \(\exp(-10^8(y+y^{-1}))\prod_j Q_j(y+y^{-1})^{w_j}\) on a closed annulus.
The logarithm of its modulus is bounded by the radial harmonic function interpolating the two boundary maxima, by the maximum principle.
This is the chord inequality for \(U\) in the variable \(v\), including annuli containing zeros.
Reciprocity makes \(U\) even, hence nondecreasing for \(v\ge0\).

Select a root \(\alpha_i\) on or outside the circle from each of the \(d\) inverse pairs.
For either sign the sum of \(\log|Q_j(\pm(\alpha_i^k+\alpha_i^{-k}))|\) over these pairs is nonnegative.
Indeed \(\prod_i(Z-(\alpha_i+\alpha_i^{-1}))\) is the monic integer trace polynomial, and \(\alpha_i^k+\alpha_i^{-k}\) is an integer polynomial in \(\alpha_i+\alpha_i^{-1}\) by the two-term Chebyshev recurrence with initial terms \(2,Z\).
The absolute value of the product of the auxiliary values is therefore the absolute value of an integer resultant.
To verify it is nonzero, substitute \(Z=y+y^{-1}\) and clear \(y\) from each of the first ten auxiliary polynomials.
The results in order are \(\Phi_4,\Phi_3,\Phi_2^2,\Phi_8,\Phi_5,\Phi_{12},\Phi_7,\Phi_9,\Phi_{30},\Phi_{11}\).
Neither \(\alpha_i^k\) nor \(-\alpha_i^k\) is torsion.
The last auxiliary reduces modulo two to \(Z^5+Z^4+Z^3+Z^2+1\), which equals one at zero and one and has remainder \(Z\) modulo \(Z^2+Z+1\).
Thus this quintic has no irreducible factor of degree one or two over \(\mathbb F_2\) and is irreducible over \(\mathbb Q\).
A root in \(\mathbb Q(\alpha_i)\) would force \(5\mid D\), which neither test degree satisfies.

The two signed traces of each root pair lie on the same ellipse with radius parameter \(|\alpha_i|^k\).
The sum of \(\log |\alpha_i|\) over these pairs is \(\log M(P)\le\log T\).
Applying the chord from zero to \(k\log T\) separately at each pair and using both resultant signs gives
\[
                     |s_k|\le(d-1)U(0)+U(k\log T).
\]
This also covers one real exterior root of maximal modulus and pairs exactly on the circle.
The quantity \(s_k\) is integral by Newton's identities.
For each layer the same vector of weights is used for both signs and both radii.

<a id="certificate"></a>
### Certificates on complete ellipses

Set \(r=T^k\), \(x=\cos\theta\), and \(z=(r+r^{-1})x+i(r-r^{-1})\sqrt{1-x^2}\).
Then \(S_j(x)=|Q_j(z)|^2\) is a rational polynomial of degree at most ten.
The program expands \(Q_j(y+y^{-1})\) as a Laurent polynomial, takes the autocorrelations of its coefficients multiplied by powers of \(r\), and replaces \(\cos(m\theta)\) by the Chebyshev polynomial.
Every resulting coefficient is exact, including at \(r=1\).
It converts \(S_j(2u-1)\) to degree-ten Bernstein form and rounds every coefficient upwards to the grid \(10^{-32}\mathbb Z\).
Each bisection uses the de Casteljau midpoint averages rounded upwards on that grid, preserving coefficientwise domination.

On any subinterval let \(y_j>0\) be the largest of these upper Bernstein coefficients for \(S_j\).
The tangent inequality \(\log S_j\le\log y_j+ S_j/y_j-1\) also holds at zeros in the extended sense.
It gives a single polynomial majorant of \(-(r+r^{-1})x+\sum_j(e_j/2)\log S_j(x)\).
Its largest upper Bernstein coefficient bounds its maximum on the entire subinterval, including endpoints.
The program bisects every cell that exceeds the proposed cap and succeeds only when the accepted cells cover \([-1,1]\).

All logarithm bounds use integer arithmetic.
For a positive rational argument first extract a power of two, leaving \(1\le u\le2\), and put \(v=(u-1)/(u+1)\).
Use the first 25 terms of \(2\sum_{j\ge0}v^{2j+1}/(2j+1)\), with outward integer rounding in units of \(10^{-24}\), and bound the remainder by \(9/(4\cdot51\cdot3^{51})\).
The same procedure at two handles the extracted power, with the interval endpoints exchanged for a negative exponent.
A floating-point search selects rational witness points for the adjusted weights.
Both the witness values and every reported upper cap are checked independently by the rational arithmetic.
There were 584 terminal cells for the fixed weights and 9,185 for the adjusted weights, with maximum bisection depth 14.

<a id="printed"></a>
### Check of the published unit-circle example

For the eleven weights printed together in the degree-34 example, \(f=-g\).
At the real coordinate \(z=-30253/20000=-1.51265\), equivalently \(x=-30253/40000\), the certified interval is
\[
        -0.269965199260\le f(z)\le-0.269965199258 .
\]
Over the full segment the certificate gives \(-0.269968\le\min_{[-2,2]} f\le-0.269965199258\).
Thus the printed minimum \(-0.20529481\ldots\) cannot be the minimum for the displayed polynomials and weights.
The fixed-weight calculation here uses those coefficients as explicit rational inputs and gives first-layer bounds 7 and 8 before adjustment.
The source audit records the printed scope and an independent point enclosure. [FRS06 example](../../../audits/literature/FRS06/Yin_U001.md#printed-example)

<a id="counts"></a>
## Results and limits

| Degree | First three integral prefixes | Whole refined box | Without power substitutions, up to sign | Fixed-weight box under the same symmetries |
| ---: | ---: | ---: | ---: | ---: |
| 56 | 373 | 2,712,147,567 | 1,356,059,655 | 52,255,067,228 |
| 58 | 425 | 6,985,779,621 | 3,492,875,690 | 177,624,501,632 |

There are **4,848,935,345** sign representatives in the two refined boxes after excluding power substitutions.
Each is one monic reciprocal integer polynomial determined by its first \(d\) power sums.
The counts include reducible and cyclotomic polynomials and candidates of measure larger than \(T\).
The degree restriction from L264 excludes power substitutions for either minimum at the prime 223.
For the broader class of polynomials stated at the start, the full box counts apply before that exclusion.

For the counting method write \(1+c_1X+\cdots\equiv\prod_{j=1}^d(1-X^j)^{e_j}\pmod{X^{d+1}}\).
Successively canceling the coefficient at each degree shows existence and uniqueness of the integers \(e_j\) for any integer coefficient prefix.
The logarithmic derivative gives \(s_k=\sum_{j\mid k}j e_j\).
Thus for every prime power \(q^v\Vert k\), \(s_k\equiv s_{k/q}\pmod{q^v}\).
Conversely, in \(\sum_{u\mid k}\mu(u)s_{k/u}\) pair the terms indexed by \(u\) and \(qu\) for \(q\nmid u\).
The pair differences are divisible by \(q^v\), so Möbius inversion gives integral \(e_k\).
These congruences therefore count exactly the possible Newton prefixes, and reflection then completes the coefficients.

The counting program eliminates variables from the finite congruence system using products of indicator arrays and sums over the eliminated variable.
Since earlier sums determine \(s_k\) modulo \(k\), the final count is at most \(\prod_k\lceil(2B_k+1)/k\rceil\) for bounds \(B_k\).
When this bound is less than \(2^{64}\), unsigned array arithmetic determines the exact count by its residue modulo \(2^{64}\), regardless of intermediate wraparound.
Larger bounds select Python integer array entries.
For a prime \(q\mid D\), membership in \(\mathbb Z[X^q]\) is equivalent to vanishing of \(s_k\) for \(q\nmid k\) through \(d\), by Newton's identities and reflection of the coefficients.
Inclusion and exclusion remove all such primes, and the remaining sign orbits have size two under \(P(X)\mapsto P(-X)\).
An independent direct Newton recursion checks the first three levels.

The separate eight-layer comparison follows from the nonzero integer resultants with \(X^k\pm1\).
The arithmetic-geometric mean inequality applied to the squared absolute values gives \(2|s_k|\le\sum_i|\alpha_i|^{2k}\).
Convexity over the nonnegative reciprocal-pair logarithms of total at most \(\log T\) bounds this sum by \(D-2+T^{2k}+T^{-2k}\).
The output gives 2,881,303,075 and 3,798,602,663 integral prefixes respectively using just these elementary eight bounds.

## Files

The [ellipse program](trace_bounds.py) contains the fixed source coefficients and all range and interval tests.
The [adjusted integer weights](refined_weights.json) are the rational inputs for each degree and layer, in the same auxiliary order with denominator \(10^8\).
They were chosen by a linear program with 750 sample angles \((j+1/2)\pi/750\) on each of the two circles, weights between zero and three, and objective \((d-1)u_0+u_k\) for the two sample upper bounds.
The resulting coefficients were rounded to multiples of \(10^{-6}\) before certification.
The [counting program](count_prefixes.py) reads the resulting integer boxes.

## Reproduction

Run these commands in order from the repository root.
The observed run used Python 3.14.3 and NumPy 2.4.4 for counting.
The certificate program uses the Python standard library, and the fixed adjusted inputs suffice to repeat the run.

```text
python mathematics/computations/programs/Yin_J_G0179/trace_bounds.py
python mathematics/computations/programs/Yin_J_G0179/count_prefixes.py
```

The [ellipse results](inputs/results.json) give the lower witness, its upper enclosure and the cap in units of \(10^{-12}\) for each certificate.
The [counting results](inputs/prefixes.json) give both weight choices, comparison boxes, exact counts and the largest intermediate table sizes.

<a id="retained-censuses"></a>
## Checking the retained censuses

The [bounds and final reports](inputs/) preserve the data used in the reviews, including the rational ellipse certificates, classification summaries and the two prime-budget lists.
The [degree-56 and degree-58 survivor files](inputs/degree-56-58-survivors.tar.xz) preserve all fourteen complete v3 slices, their higher-trace counts and the half-coefficient vectors inspected in the [census review](../../../audits/reviews/Yin_R_G0562_v551.md#finding).
The [verification data for the other censuses](inputs/census-verification.tar.xz) contain the individual slices for v6 and v8 through v15, the additional degree-64 eight-trace control inspected in the [degree-64 review](../../../audits/reviews/Yin_R_G0562_v558.md#finding), and the prefix counts, selected bounds and census parameters read by their verifiers.
The degree-60 vector passed from the first sieve to the final \(\Phi_{122}\) test is preserved in the v6 slice with \(s_1=1\).
These fixed files are the existing reports from the completed computations and retain their original JSON contents.

From an empty J179 output directory, run the following from the repository root to place the reports at the paths used by the existing finishing and verification programs.

~~~text
python -B mathematics/computations/programs/Yin_J_G0179/restore_census.py
~~~

The [restore program](restore_census.py) uses the Python standard library and accepts \(\texttt{--destination}\) followed by a separate directory for inspecting the data.
The reproduction sections of the individual versions give the enumeration and checking commands.
To check an existing completed census from its fixed reports, restore them first and use the corresponding finishing or verification command, covering each listed degree.
The separate [radial counts](versions/v5/radial_counts.py) and [fixed-prefix comparison](versions/v7/affine_tail.py) can be regenerated by the commands at those versions from their stored programs and the restored inputs.
