---
author: Yin
---

# An affine integer test beyond the selected square families

<a id="scope"></a>
## The next arithmetic question

The [local-count exploration](Yin_L_G0462_v8.md#probability-boundary) separates positive local representation densities from the missing global integer count in the paired supply.
The [completed conductor-81 controls](../computations/programs/Yin_J_G0154/energy_six.md#complete-result) show that the chosen original and paired square families miss the low-energy targets, while a single-filter moment hit fails the strict endpoint.
Changing a positive-unit representative cannot change the complete count in one square family.
The next test therefore uses the full affine integer coefficient lattice for \(h\), with no prescribed norm or square class.

This is a bounded candidate test, not a proposed exhaustive exclusion.
It asks for an actual integral residue input satisfying the prescribed moments, all original strict signs and the strict endpoint, and then measures its entire reciprocal lift.
It does not assert an arbitrary-radius positive-probability result.

The [earlier trace-cell proposal](Yin_L_G0462_v1.md#complex-trace-cells) already uses integer coefficients and linear sufficient inequalities for complete root control.
The present change is the exact moment-coordinate chart on the full odd-grid residue input and a coefficient box proved to contain its entire strict chamber.
It does not fix complex root cells or assume an output Mahler bound.

<a id="fixed-chamber"></a>
## One conductor, one cut and one profile

Fix
\[
 p=81,\qquad n=40,\qquad b_j=2\cos(2\pi j/81)
       \quad(1\le j\le40),
\]
in decreasing order.
Require
\[
 h(b_j)>0\quad(1\le j\le37),\qquad
 h(b_j)<0\quad(38\le j\le40).                              \tag{1}
\]
Thus exactly the last three residues are negative.
Take the profile \(x=0\), so the shift is \(a=0\) and the prescribed moments are exactly
\[
                              K=2,\qquad L=0.              \tag{2}
\]
No third or higher moment is fixed.

The smaller negative block moves the cut closer to \(-2\) without increasing the dimension.
The [third-moment calculation](Yin_L_G0464_v12.md#third-moment) already obstructs the \(x=0\) next-profile match when the angular midpoint is at least \(-13/8\), including the former conductor-81 cut with nine negative nodes.
The present test avoids that particular geometric obstruction.
This motivates the choice of cut; it imposes neither the next-profile moment nor a claim that the new cut suffices for a small whole measure.

Let \(E_0=1,E_1=t,E_{i+1}=tE_i-E_{i-1}\), and write
\[
 B=B_{40}=E_{40}+E_{39},\qquad D=B_{39}=E_{39}+E_{38},
 \qquad h(t)=\sum_{i=0}^{39}a_iE_i(t),\quad a_i\in\mathbb Z.
                                                                    \tag{3}
\]
This monic integral basis is unimodular relative to the ordinary monomial basis, so (3) covers every element of \(\mathbb Z[t]/B\).
The lift is
\[
 C=Dh\bmod B,\qquad Q=tB+C,\qquad P(z)=z^{41}Q(z+z^{-1}).    \tag{4}
\]
It is a monic reciprocal integer polynomial of degree 82 with constant coefficient one.

<a id="affine-moments"></a>
## The first two moments are two integer coordinates

Put \(\nu_j=(4-b_j^2)/81\) and \(r_j=\nu_jh(b_j)\).
The [full-grid quadrature](Yin_L_G0464_v5.md#odd-grid-product) is exact through degree 78, so the \(E_i\), \(0\le i<40\), are orthonormal for
\[
                     \langle f,g\rangle
                    =\sum_{j=1}^{40}\nu_jf(b_j)g(b_j).
\]
Consequently
\[
 K=\langle h,1\rangle=a_0,\qquad
 L=\langle h,t\rangle=a_1.                                 \tag{5}
\]
The entire prescribed moment domain is therefore
\[
 a_0=2,\qquad a_1=0,\qquad (a_2,\ldots,a_{39})\in\mathbb Z^{38}.
\]
For comparison, the third moment would be
\[
                \sum_j b_j^2r_j=a_0+a_2,
\]
because \(t^2=E_2+E_0\).
That integer is an output diagnostic, not an extra equation in this test.

<a id="endpoint-coordinate"></a>
## The strict endpoint is an exact linear inequality

Define
\[
                  W(t)=\sum_{i=0}^{39}(-1)^iE_i(t).
\]
The recurrence in (3) telescopes to
\[
                          (t+2)W(t)=1-B(t).               \tag{6}
\]
Hence \(W(b_j)=(2+b_j)^{-1}\), and orthogonality gives the integer
\[
 U=\sum_j\frac{r_j}{2+b_j}
   =\langle h,W\rangle
   =\sum_{i=0}^{39}(-1)^i a_i.                             \tag{7}
\]
The partial-fraction identity \(C/B=\sum_jr_j/(t-b_j)\), evaluated at \(-2\), gives \(Q(-2)/B(-2)=-2-U\).
Here \(B(-2)=1\) and \(P(-1)=-Q(-2)\), so
\[
                             P(-1)=2+U.                   \tag{8}
\]
Thus the desired strict endpoint is exactly
\[
                       \sum_{i=0}^{39}(-1)^i a_i\ge-1.     \tag{9}
\]
There is no floating endpoint tolerance and no imposed value of \(P(-1)\).

<a id="complete-coefficient-box"></a>
## A finite coefficient box covers the complete strict domain

Take the rational separator
\[
                                c=-31/16.
\]
The Jacobi Sturm recurrence gives exactly 37 eigenvalues above each of
\[
                         -193/100,\qquad -49/25,\qquad -31/16.
\]
Here is a reproducible integer check.
For a rational \(r=A/B_0\), \(B_0>0\), start \(d_0=1,d_1=A\), use
\[
 d_i=A d_{i-1}-B_0^2d_{i-2}\quad(2\le i\le39),
 \qquad
 d_{40}=(A+B_0)d_{39}-B_0^2d_{38}.
\]
These are the positive-denominator-scaled leading characteristic minors of \(rI-J\).
There are no zero entries at the three rationals.
Their signs, from \(d_0\) through \(d_{40}\), and variations are:

| \(r\) | Signs of \(d_0,\ldots,d_{40}\) | Variations |
| --- | --- | ---: |
| \(-193/100\) | \(+-+-+-+-+-++-+-+-+-+-+--+-+-+-+-+-++-+-+-\) | 37 |
| \(-49/25\) | \(+-+-+-+-+-+-+-++-+-+-+-+-+-+-+--+-+-+-+--\) | 37 |
| \(-31/16\) | \(+-+-+-+-+-+--+-+-+-+-+-+--+-+-+-+-+-++-+-\) | 37 |

Sylvester inertia through the nonzero leading pivots identifies these variations with the number of eigenvalues greater than \(r\).
In particular,
\[
 b_{37}>-193/100>c,\qquad b_{38}<-49/25<c.
\]
Every node therefore satisfies
\[
                              |b_j-c|>3/400.               \tag{10}
\]
For the positive side this follows from \(-193/100-c=3/400\); on the negative side \(c+49/25=9/400\).

For an \(h\) satisfying (1)--(2), define strictly positive weights
\[
                \mu_j=(b_j-c)\nu_jh(b_j)>0.
\]
Their sum is fixed:
\[
                       \sum_j\mu_j=L-cK=31/8.             \tag{11}
\]
By orthogonality,
\[
 a_i=\sum_j\nu_jh(b_j)E_i(b_j)
     =\sum_j\mu_j\frac{E_i(b_j)}{b_j-c}.                    \tag{12}
\]
The identity \(E_i(2\cos\theta)=\sin((i+1)\theta)/\sin\theta\) gives
\[
                          |E_i(t)|\le i+1\quad(-2\le t\le2).
\]
Combining this with (10)--(12) yields
\[
                        |a_i|<\frac{1550(i+1)}3.
\]
Thus every integral \(h\) in the full strict moment chamber belongs to the explicit box
\[
 |a_i|\le B_i,\qquad
 B_i=\left\lceil\frac{1550(i+1)}3\right\rceil-1,
                      \quad 2\le i\le39.                  \tag{13}
\]
The largest bound is \(B_{39}=20666\).
This is a consequence of the original signs and two moments, not an independently imposed height restriction.
One may replace (13) by sharper rigorously enclosed extrema in (12), but the first test needs only (13).

The same separator also gives a harmless necessary upper bound for the endpoint coordinate.
The positive sum from the [endpoint identity](Yin_L_G0464_v11.md#endpoint-moment-test) is
\[
 (4+c)K-L-4(2+c)U=33/8-U/4>0.
\]
Since \(U\) is integral, the full strict-endpoint domain has
\[
                              -1\le U\le16.                \tag{14}
\]
These inequalities merely record necessary consequences of (1), (2) and (9).

<a id="candidate-test"></a>
## One bounded integer candidate test

The formal domain consists of all integer vectors in (13), with \(a_0=2,a_1=0\), the strict signs (1), and the exact endpoint (9).
It includes every square class, every principal ideal and every nonzero resultant compatible with those conditions.
No positive-unit orbit, filter word, third moment, specified resultant or asymptotic norm ceiling is imposed.

Use one mixed-integer linear candidate model for this fixed domain.
Node evaluations are linear functions of the integer coefficients.
Approximate node or basis values only for proposing candidates; interval enclosures and the coefficient bounds can be used to make the numerical approximation explicit.
For example, if \(E_i(b_j)\in[m_{ji}-e_{ji},m_{ji}+e_{ji}]\), then every coefficient vector in the box has evaluation error at most
\[
             \epsilon_j=2e_{j0}+\sum_{i=2}^{39}B_i e_{ji}.
\]
A rational outer relaxation of each sign is
\[
 \sigma_j\sum_i m_{ji}a_i\ge-\epsilon_j,\qquad
 \sigma_j=1\ (j\le37),\quad \sigma_j=-1\ (j\ge38).
\]
Every true strict solution lies in this relaxation.
The reverse implication is false, so solver feasibility is not a sign certificate.

Use 40 integer coefficient variables with \(a_0=2,a_1=0\), the endpoint inequality, all 40 sign rows and the absolute-coefficient objective \(\sum_{i=0}^{39}|a_i|\) with the usual auxiliary variables.
The fixed first two coefficients contribute only the constant two to this objective.
It does not define a smaller mathematical domain or predict the Mahler measure.
The first test is one fixed model with a 60-second solver-time limit or 100000 branch nodes, whichever is reached first, and at most one returned integer incumbent subjected to the full validation below.
Do not restart at other conductors, cuts, profiles, coefficient bounds or objectives within this test.
The solver may stop earlier with a candidate or a reported status.
A floating sign margin may guide the proposal but supplies no exclusion of vectors outside that numerical margin.
A floating optimality or infeasibility status is not adopted as an exact conclusion.

Recover the proposed \(a_i\) as integers, verify the box, and reconstruct \(h\) exactly.
Then perform the following checks in order:

1. Verify the two moments both from \(a_0,a_1\) and from the exact polynomial or Jacobi representation.
2. Certify every strict sign in (1) by outward Arb evaluation at all 40 original nodes, refining precision as necessary.
   An interval containing zero is unresolved, while an exact zero component or a certified wrong sign rejects the candidate.
3. Verify (7)--(9) and the exact polynomial endpoint \(P(-1)\) from the lift (4).
4. Compute the complete integer resultants of the actual \(h\) and lift, retaining their exact values.
   A proposed norm budget may only be used as an explicitly justified subsequent filter with its actual finite scope; the asymptotic ceiling is not silently imposed here.
5. Enclose the whole Mahler measure over all roots of \(P\), with every multiplicity and the full degree checked.
   If the value one cannot be separated, use the necessary exact factor or cyclotomic checks rather than declaring a positive hit.

The ordinary research record should retain the actual solver model and limits, incumbent coefficients, exact matrices or polynomials, all sign and endpoint checks, full resultants and complete-measure return.
A missing candidate, a rejected incumbent, a time limit or floating infeasibility gives no exclusion of the full integer chamber.
An exact exclusion would require a separate certificate covering that full domain.
A valid strict-endpoint candidate with a large Mahler measure establishes arithmetic supply only at its actual value, without an arbitrary-radius conclusion.

<a id="discrete-law-and-return"></a>
## The resulting probability statement would be genuinely discrete

For this single test define a finite law by fixing \(a_0=2,a_1=0\) and drawing each free \(a_i\), \(2\le i\le39\), independently and uniformly from \([-B_i,B_i]\cap\mathbb Z\).
Every draw gives an actual integer \(h\) and hence an actual integer reciprocal lift through (4).
The probability of one particular free coefficient vector is exactly
\[
                  \left(\prod_{i=2}^{39}(2B_i+1)\right)^{-1}.
\]
If a returned vector is certified to satisfy all strict conditions and \(1<M(P)<1+\varepsilon\), the corresponding event under this law has at least that positive probability.
Without such a vector or an independently positive actual integer count, no positive small-shell probability follows.

This conductor has only finitely many candidates in the prescribed chamber, so it cannot by itself prove the arbitrary-\(\varepsilon\) assertion.
The discriminating return is whether a strict-endpoint integer point exists in the full coefficient domain that the selected square families did not cover, and what its entire measure actually costs.
Because this test changes both the cut and the parameter domain, a successful return alone would not identify which restriction caused the earlier failures.
A favorable return would justify investigating an all-conductor supply in these affine coordinates.
An unfavorable bounded candidate test does not establish nonexistence and does not justify enlarging a square-root ellipsoid by default.
