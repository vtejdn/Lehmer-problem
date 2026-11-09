---
author: Yin
---

# Complete-measure bounds and the degree-seven obstruction for the N=7 branch

<a id="statement"></a>
## Statement and exact scope

Set \(p=19683\), \(n=9841\), \(k=1990\), and \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\), in decreasing order.
Use the odd-grid polynomials \(B_0=1\), \(B_1=t+1\), and \(B_m=tB_{m-1}-B_{m-2}\), so \(B=B_n=\prod_{j=1}^n(t-b_j)\) and \(D=B_{n-1}\).
Let \(h\in\mathbb Z[t]\) satisfy
\[
 h(b_j)>0\quad(1\le j\le7851),\qquad
 h(b_j)<0\quad(7852\le j\le9841),\qquad
 \prod_{j=1}^n|h(b_j)|=2^{4391}.
\]
Define the negative-one branch by
\[
 r_j=\frac{(4-b_j^2)h(b_j)}p,\qquad C=Dh\bmod B,\qquad
 Q=(t+2)B+C,\qquad P(z)=z^{n+1}Q(z+z^{-1}).
\]
Assume
\[
 K=\sum_jr_j=3,\qquad L=\sum_jb_jr_j=4,\qquad
 N=\sum_jb_j^2r_j=7,\qquad P(-1)>0.
\]
Write
\[
 U=\sum_j\frac{r_j}{2+b_j},\qquad
 (O,V,W)=\left(\sum_jb_j^3r_j,\sum_jb_j^4r_j,\sum_jb_j^5r_j\right).
\]
The inherited necessary conditions give \(U=1\) and the eighteen integer triples partitioned in the following table.
For every input satisfying the hypotheses, each indicated strict bound holds for the complete multiplicative Mahler measure \(M(P)\).
No entry in the necessary table is asserted to be realizable.

| \(O\) | \(V\) | \(W\) | Conclusion |
| ---: | ---: | --- | --- |
| 10 | 17 | 25, 26 | \(M(P)>26/25\) |
| 10 | 18 | 26 | \(M(P)>101/100\) |
| 10 | 18 | 27 | Residual interface obstruction below |
| 10 | 18 | 28 | \(M(P)>26/25\) |
| 11 | 19 | 30, 31, 32 | \(M(P)>26/25\) |
| 11 | 20 | 32 | \(M(P)>26/25\) |
| 11 | 20 | 33, 34 | Residual interface obstruction below |
| 11 | 20 | 35 | \(M(P)>101/100\) |
| 11 | 21 | 36, 37 | Residual interface obstruction below |
| 12 | 22 | 39, 40 | \(M(P)>26/25\) |
| 12 | 23 | 42, 43 | \(M(P)>26/25\) |

In particular, \(M(P)\le101/100\) requires
\[
 (O,V,W)\in\mathcal R
 =\{(10,18,27),(11,20,33),(11,20,34),(11,21,36),(11,21,37)\}.
\]
This is only a necessary restriction and leaves all five original realization questions unresolved.

For a triple in \(\mathcal R\), define the linear functional \(\mathcal D\) on polynomials of degree at most seven by
\[
\begin{split}
 \mathcal D(1)&=1,\qquad \mathcal D(t)=\mathcal D(t^2)=\mathcal D(t^3)=-2,\qquad
 \mathcal D(t^4)=-10,\\
 \mathcal D(t^5)&=48-5O,\qquad
 \mathcal D(t^6)=-44+12O-6V,\qquad
 \mathcal D(t^7)=-7O+14V-7W-2.
\end{split}
\]
For every
\[
 b\in I=\left[-\frac{1609663}{10^6},-\frac{1609662}{10^6}\right]
\]
there exist a positive measure \(\nu_b\) of total mass two on \([-2,2]\) and a step function \(w_b:[-2,2]\to[0,1]\) such that, simultaneously for every real polynomial \(f\) of degree at most seven,
\[
 \mathcal D(f)+f(b)=\int f\,d\nu_b-\int_{-2}^2w_b(t)f'(t)\,dt.
 \tag{1}
\]
The actual unpaired pole \(b_*=b_{7851}\) belongs to the interior of \(I\).
Consequently every such \(f\) satisfies
\[
 \mathcal D(f)+f(b_*)-\int_{-2}^2\max(0,-f'(t))\,dt
 \le2\max_{[-2,2]}f.
 \tag{2}
\]
Thus the negative-variation and twice-maximum interface cannot give a positive separation margin for these five triples using any degree-at-most-seven real polynomial, even at radial cost zero.
This assertion concerns the exact interface, not just a finite grid of tests, and does not assert that an original polynomial has \(M(P)=1\).

## Inputs and retained boundaries

[C882v5 statement](Yin_C_G0882_v5.md#statement) supplies the exact integral construction, the consequence \(U=1\), and the complete necessary eighteen-triple table for \(N=7\).
Its [localized moment proof](Yin_C_G0882_v5.md#positive-moments) and [norm restriction](Yin_C_G0882_v5.md#higher-norm) justify that table without any additional profile-matching assumption.
The current hypotheses are exactly that branch with the additional equality \(N=7\), so those conclusions apply.
The preceding \(N=8\) measure bound and the different branches at [C882v3](Yin_C_G0882_v3.md#statement) and [C882v4](Yin_C_G0882_v4.md#statement) are retained there and are not reasserted as new conclusions here.

[J151 fixed certificate program](../computations/programs/Yin_J_G0151/negative_one_seven.py) supplies the thirteen integer coefficient rows in `CERTIFICATES`, the five finite rational specifications in `RELAXATIONS`, and their exact default verifier.
[J151 certificate specifications](../computations/programs/Yin_J_G0151/negative_one_seven.md#full-measure-certificates) identify each coefficient row, threshold and strict rational margin.
[J151 model specifications](../computations/programs/Yin_J_G0151/negative_one_seven.md#exact-relaxed-models) identify the finite matrix and forty control-vector systems.
These exact fixed inputs, including their existing native helpers, are the computational premises used below; optional numerical search modes provide no proof premise.

[R1107v16](../audits/reviews/Yin_R_G1107_v16.md#negative-one-seven-review) records the independent inspection of those fixed native inputs and their mathematical interfaces.
Its [separate assembly finding](../audits/reviews/Yin_R_G1107_v16.md#negative-one-seven-assembly) covers the complete statement, argument and dependency applicability of this version.
The assessment below selects these two actual review findings at their respective scopes.

<a id="whole-measure"></a>
## Complete-root pairing and the radial cost

The residue identity is
\[
 \frac{Q(t)}{B(t)}=t+2+\sum_j\frac{r_j}{t-b_j}.
\]
On each interval between adjacent poles with the same residue sign, the two infinite limits have opposite signs, so the interval contains a real root of \(Q\).
There is also a root in \((-2,b_n)\), because \(Q(-2)/B(-2)=-U=-1\) and the limit at the negative-residue pole \(b_n\) from the left is positive infinity.
Choose one root from each of these disjoint intervals and pair it with the interval's right pole.
There are \(7850+1989+1=n-1\) chosen roots in \((-2,2)\), and the sole unpaired pole is \(b_*=b_{7851}\).
The two remaining roots of \(Q\), denoted \(v_1,v_2\), are counted with multiplicity and may be real, nonreal or repeated.

For a real polynomial \(f\), let
\[
 \mathcal D(f)=\sum_{Q(v)=0}f(v)-\sum_{B(b)=0}f(b),\qquad
 V_-(f)=\int_{-2}^2\max(0,-f'(t))\,dt.
\]
Each paired root \(u\) lies to the left of its pole \(b\), and \(f(u)-f(b)=-\int_u^bf'(t)\,dt\).
The pairing intervals are disjoint, so their summed contribution is at most \(V_-(f)\).
Subtracting it from the complete trace difference gives
\[
 \sum_{i=1}^2\operatorname{Re}f(v_i)
 \ge\mathcal D(f)+f(b_*)-V_-(f).
 \tag{3}
\]

Every chosen trace root lifts to two unit-circle roots under \(t=z+z^{-1}\).
Write the exterior root in each remaining reciprocal pair as \(\rho_i e^{\mathrm i\theta_i}\), with \(\rho_i\ge1\).
The monic lift therefore has complete measure \(M(P)=\rho_1\rho_2\).
Use \(T_j(z+z^{-1})=z^j+z^{-j}\) and write \(f=c_0+\sum_{j=1}^7c_jT_j\).
The difference between \(\operatorname{Re}T_j(v_i)\) and \(T_j(2\cos\theta_i)\) has absolute value at most \(\rho_i^j+\rho_i^{-j}-2\).
For \(a_i=j\log\rho_i\ge0\), the addition formula gives
\[
 \cosh(a_1+a_2)-1\ge(\cosh a_1-1)+(\cosh a_2-1).
\]
Hence, if \(M(P)\le R\) for \(R\ge1\),
\[
 \sum_{i=1}^2\operatorname{Re}f(v_i)
 \le2\max_{[-2,2]}f+
 \mathcal E_R(f),\qquad
 \mathcal E_R(f)=\sum_{j=1}^7|c_j|(R^j+R^{-j}-2).
 \tag{4}
\]
This uses the product of both exterior radii and the whole root multiset; no house bound or nonreal-root hypothesis is substituted.

The formal expansion
\[
 \frac{Q(t)}{tB(t)}=1+\frac2t+\frac3{t^2}+\frac4{t^3}
 +\frac7{t^4}+\frac O{t^5}+\frac V{t^6}+\frac W{t^7}+\mathcal O(t^{-8})
\]
gives the displayed values of \(\mathcal D(t^j)\) by its formal logarithm.
Equivalently, writing \(D_j=\mathcal D(t^j)\) and \((a_0,\ldots,a_7)=(1,2,3,4,7,O,V,W)\), they obey
\[
 D_j=-ja_j-\sum_{i=1}^{j-1}a_iD_{j-i}\quad(1\le j\le7),
 \qquad D_0=1.
\]
The value \(D_0=1\) follows from the degree difference and includes the constant terms of the even \(T_j\).

<a id="strict-certificates"></a>
## Deduction of the thirteen strict bounds

The exact odd-grid recurrence places \(b_*\) strictly between \(y=-161/100\) and \(z=-1006/625\).
For each of the thirteen nonresidual triples, take its fixed integer coefficient vector \(c\), threshold \(R\), and positive integer \(m_0\) from the J151 `CERTIFICATES` table.
Eleven rows use \(R=26/25\), while the rows \((10,18,26)\) and \((11,20,35)\) use \(R=101/100\).
The finite certificate in each row is the exact inequality
\[
 \mathcal D(f)+\min_{[y,z]}f-V_-(f)
 -2\max_{[-2,2]}f-\mathcal E_R(f)>m_0>0.
 \tag{5}
\]
All thirteen displayed \(m_0\) are at least 208.
Here and in the native verifier, \(\mathcal D(f)\) uses the row's actual \((O,V,W)\); no unspecified moment is optimized or presumed.

For completeness, the rigorous finite enclosure supporting (5) has the following analytic justification.
On a rational interval \([a,b]\), write \(q(a+(b-a)s)=\sum_{j=0}^dA_js^j\).
Its degree-\(d\) Bernstein controls are
\[
 \beta_i=\sum_{j=0}^iA_j\frac{\binom ij}{\binom dj},\qquad 0\le i\le d.
\]
The Bernstein basis is nonnegative and sums to one, so its smallest and largest controls bound \(q\) on the entire interval.
The fixed verifier subdivides \([-2,2]\) into 1024 equal rational intervals and applies this fact to \(f'\).
A certified nonnegative derivative contributes zero negative variation and an endpoint maximum, while a certified nonpositive derivative contributes exactly \(f(a)-f(b)\) and an endpoint maximum.
Otherwise a derivative lower bound \(l\) gives variation at most \((b-a)\max(0,-l)\), and the polynomial's own Bernstein upper bound controls the maximum.
The sum of those variation bounds and maximum of those maximum bounds have the directions required for a lower bound in (5).
A separate Bernstein lower bound on \([y,z]\), together with the exact trace and rational radial cost, completes every row's certificate.
Thus the fixed integer coefficient table and exact rational comparisons establish (5), without a numerical extremum or floating-point sign decision.

If a corresponding input had \(M(P)\le R\), inequalities (3) and (4) would contradict (5).
This proves every strict complete-measure bound in the statement.
The thirteen certified triples and the five members of \(\mathcal R\) form a disjoint partition of the inherited eighteen-triple table, as the fixed verifier also checks.
Since \(26/25>101/100\), the stated five-triple necessity for \(M(P)\le101/100\) follows.

<a id="relaxation-barrier"></a>
## Exact relaxed models for every cut position

The exact recurrence also places \(b_*\) strictly between the two endpoints of \(I\), counting 7851 poles above its lower endpoint and 7850 above its upper endpoint.
We prove (1) on that whole interval by the fixed rational systems in J151, rather than assuming feasibility at finitely many cut positions.

Put \(t_i=-2+i/64\) for \(0\le i\le256\), and use \(q_0=1\), \(q_j=T_j\) for \(1\le j\le7\).
For each residual triple form the rational \(8\) by \(513\) matrix
\[
 A_{j,i}=q_j(t_i)\quad(0\le i\le256),\qquad
 A_{j,257+i}=q_j(t_i)-q_j(t_{i+1})\quad(0\le i<256).
\]
The first 257 coordinates are atomic masses \(\alpha_i\ge0\); the remaining coordinates are occupancies \(0\le\omega_i\le1\).
Let \(\nu=\sum_i\alpha_i\delta_{t_i}\) and let \(w=\omega_i\) on the \(i\)-th interval.
With \(g_j(b)=\mathcal D(q_j)+q_j(b)\), the equation \(Au=g(b)\) is precisely (1) on this basis, because the occupancy column is the negative integral of \(q_j'\) over its cell.
The constant row enforces \(\sum_i\alpha_i=\mathcal D(1)+1=2\).

For each triple, the J151 `RELAXATIONS` row specifies a set of occupancy coordinates fixed at one and eight distinct free columns; all other coordinates are zero.
The sets are disjoint, and their finite specification is part of the fixed computational input.
Write \(a=-1609663/10^6\) and \(\delta=10^{-6}\).
The components of \(g(a+\delta s)\) are polynomials of degree at most seven, so their degree-seven Bernstein expansion is
\[
 g(a+\delta s)=\sum_{r=0}^7g^{(r)}\binom7r s^r(1-s)^{7-r}.
\]
The preceding Bernstein coefficient formula, with degree elevation to seven, computes all vectors \(g^{(r)}\) exactly over \(\mathbb Q\).
For each of the five triples and each \(r\), subtract the fixed-one columns and solve the specified eight-column system for \(g^{(r)}\).
The fixed verifier checks nonsingularity by exact elimination and verifies every solution by direct rational substitution.
In all forty systems every free coordinate is strictly greater than \(1/40\), and every free occupancy coordinate is strictly less than \(19/20\).
The fixed zero and one coordinates already satisfy their required bounds.
These finite checks therefore supply vectors \(u^{(r)}\) with nonnegative masses, occupancies in \([0,1]\), and \(Au^{(r)}=g^{(r)}\).

For any \(0\le s\le1\), set
\[
 u(a+\delta s)=\sum_{r=0}^7u^{(r)}\binom7r s^r(1-s)^{7-r}.
\]
This convex combination preserves nonnegative masses, mass two, the occupancy bounds, and all fixed coordinates.
By linearity it satisfies \(Au(a+\delta s)=g(a+\delta s)\).
The basis \(1,T_1,\ldots,T_7\) spans every real polynomial of degree at most seven, which proves (1) simultaneously for all those polynomials and every \(b\in I\).

Finally, \(0\le w_b\le1\) implies pointwise \(-w_bf'\le\max(0,-f')\).
Using (1),
\[
 \mathcal D(f)+f(b)-V_-(f)
 =\int f\,d\nu_b-\int w_bf'-V_-(f)
 \le\int f\,d\nu_b
 \le2\max_{[-2,2]}f.
\]
Taking \(b=b_*\) proves (2).
At \(R=1\), the separation margin from (3) and (4) is already nonpositive for every permitted test; at \(R>1\), subtracting the nonnegative \(\mathcal E_R(f)\) cannot improve it.
The same conclusion holds if an enclosure lower bound replaces the exact cut value.

The relaxed measure need not consist of two unit atoms at actual exceptional trace roots, and the occupancy need not be an indicator of actual pairing intervals.
Equation (1) does not reconstruct an integral \(h\), impose its complete resultant, or produce an actual polynomial \(Q\).
This is a precise obstruction to the specified degree-seven interface, not an impossibility theorem for stronger arguments using the discarded constraints or independently justified higher moments.
No degree-eight statement, new conductor, or enlarged parameter range is asserted.

## Assessment history

### Decision negative-one-seven-whole-19683

| Field | Value |
| --- | --- |
| date | 2026-11-09T14:09 |
| status | proved |
| reason | Independent native and complete-assembly reviews verified the thirteen strict full-Mahler bounds and the exact degree-seven obstruction for the five residual triples, with no original-input realization or unrestricted-gap conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [N=7 complete statement](#statement) | Fixed conductor, cut, norm, endpoint and moments; full eighteen-triple partition, thirteen strict bounds and five quantified interface obstructions. |
| argument | [Complete root measure](#whole-measure) | Disjoint real-root pairing, all multiplicities, both exterior radii, exact trace differences and complete radial cost. |
| argument | [Thirteen strict certificates](#strict-certificates) | Fixed coefficient rows, rational Bernstein bounds, positive margins and the five-triple necessary consequence. |
| argument | [Exact residual models](#relaxation-barrier) | Forty rational systems, whole-cut-interval convex combinations, simultaneous degree-seven test identities and the precise method boundary. |
| dependency | [Inherited N=7 table](Yin_C_G0882_v5.md#statement) | U=1 and all eighteen necessary integer triples under exactly the current hypotheses. |
| dependency | [Localized moment restrictions](Yin_C_G0882_v5.md#positive-moments) | Strict moment matrices and exhaustive integer intervals used to obtain that table. |
| dependency | [Inherited norm restriction](Yin_C_G0882_v5.md#higher-norm) | Exact positive norm weight and fifth-moment filter. |
| dependency | [Fixed native certificates](../computations/programs/Yin_J_G0151/negative_one_seven.py) | All thirteen CERTIFICATES, five RELAXATIONS and the exact default verifier, including necessary unchanged helpers; no exploratory mode as a premise. |
| review | [Independent native finding](../audits/reviews/Yin_R_G1107_v16.md#negative-one-seven-review) | Complete finite inputs, independent thirteen-margin and forty-system computations, brackets and analytic interface. |
| review | [Independent assembly finding](../audits/reviews/Yin_R_G1107_v16.md#negative-one-seven-assembly) | Entire statement, complete argument and actual dependency applicability of this fixed C version. |

## Current assessment

[Selected decision](#decision-negative-one-seven-whole-19683)
