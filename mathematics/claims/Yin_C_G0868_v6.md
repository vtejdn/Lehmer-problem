---
author: Yin
---

# Integer Hermitian-square certificates and their exact original-input price

Date: 2026-11-05.
This candidate gives a uniform positive total Mahler bound for the original irreducible reciprocal inputs that actually possess the stated degree-bounded integral Hermitian-square certificate.
It also identifies the exact common-content condition under which a general integer-multiplier certificate gives an integer reflection germ.
The coordinating agent developed the reflection, the original pole-price return and the stronger constant-involution dichotomy.
The witt_moment_compatibility delegate checked and completed those arguments, the content criterion, the doubled-quartic minimum-rank proof and the finite feasibility and source comparisons.
These are ordinary author contributions for Yin, not independent review or an assessment of this version.

## Inputs and retained scope

[C868 v4](Yin_C_G0868_v4.md#gram-loewner-determinant), at its [selected assessment](Yin_C_G0868_v4.md#decision-whole-integral-metric-review-2026-11-05), supplies the Euclidean integer-germ bound with total determinant price at least c_mat=(1/2)log(5/4).
[C868 v5](Yin_C_G0868_v5.md#circle-unitary-exact-price), at its [selected assessment](Yin_C_G0868_v5.md#decision-whole-rational-price-review-2026-11-05), supplies exact inner cancellation with every actual pole-module multiplicity retained.
Its statement normalizes the germ at zero to I.
The limited extension to an arbitrary invertible constant value, needed for one branch below, is explicitly justified from its same cancellation construction rather than assumed from that statement.
Earlier versions remain fixed at their own statements and selected scopes.

[C34](Yin_C_G0034_v1.md#minimal-rational-gram-ldl-and-boundaries), at its [selected assessment](Yin_C_G0034_v1.md#decision-organized-reviewed), is used only in the comparison about input-dependent rational weights and denominator clearing.
It is not an existence input for a multiplier-one or multiplier-two integral certificate.
[L133 v8](../ledger/Yin_L_G0133_v8.md#positive-polynomial-integer-sos-control) already proves that the undoubled positive quartic in the control below has no integral Hermitian-square representation, even with arbitrary finite rank and Laurent width.
That sufficient proof is reused by reference.

The [MSEDSV22 source account](../audits/literature/MSEDSV22/Yin_U001.md#msedsv22-u001) is sufficient for the existing rational weighted Gram/rounding interface.
The YY22 comparison below uses only inspected definitions and theorem statements and is not a premise of the reflection theorem.
The [native bounded enumeration](../computations/programs/Yin_J_G0136/readme.md) is retained as exploratory computation with an explicitly uncertified floating positivity screen.
None of its output is a proof input below.

## Statement

<a id="integer-reflection-certificate-statement"></a>
### IR1. The actual integral certificate class

Let d>=1 and let P in Z[z] be monic, irreducible over Q, reciprocal of degree 2d and have P(0)=1.
Choose epsilon in {+1,-1}, and put
\[
 p(z)=\varepsilon z^{-d}P(z).
 \tag{IR1}
\]
The involution on real-coefficient Laurent polynomials is f^star(z)=f(z^{-1}); on the unit circle this equals complex conjugation of the value.
Suppose that for some finite r>=1 there are nonzero polynomials v_1,...,v_r in Z[z], each of degree at most d, such that
\[
 2p(z)=\sum_{j=1}^r v_j(z)v_j(z^{-1}).
 \tag{IR2}
\]
This is an exact Laurent-polynomial identity.
There are no rational weights, omitted multiplicities or unstated support enlargements.
Zero summands can be deleted.

Then p is strictly positive on the unit circle, P has no unit-circle root, and its total logarithmic Mahler measure satisfies
\[
 \boxed{\displaystyle m(P)\ge c_{\rm mat}
       =\frac12\log\frac54.}
 \tag{IR3}
\]
The original degree is 2d and the measure is not divided by that degree.
The bound is independent of d, r and the certificate's coefficient sizes.
A certificate p=sum_j |u_j|^2 with the same degree restriction is included, by repeating its summands to give (IR2).
No assertion that every original input has either certificate is made.

### IR2. Reflection, exact pole price and the constant-value alternatives

Let v=(v_1,...,v_r)^T and define
\[
 A(z)=z^d v(z)v(z^{-1})^T,\qquad
 W(z)=I_r-\varepsilon\frac{A(z)}{P(z)}.
 \tag{IR4}
\]
Then W has an integer Taylor germ at zero, W^2=I_r, det W=-1, and W is unitary on the unit circle.
Its constant value W_0 is an integer involution.
At every root alpha of the original P, W has a simple pole with residue of rank one and pole-cancellation length delta_alpha(W)=1.
Consequently its complete disk pole cost is exactly
\[
 N(W)=\sum_{P(\alpha)=0,\ |\alpha|<1}\log\frac1{|\alpha|}
     =m(P).
 \tag{IR5}
\]
Every root in this sum is retained once; simplicity follows from characteristic zero and irreducibility.
Constant determinant does not remove these pole costs.

If W_0 is orthogonal, F=W W_0^{-1} is a nonconstant normalized integer germ and has the same exact pole cost m(P).
An actual rational inner pair for F has total determinant price m(P), so the v4 integer-germ theorem gives (IR3).
If W_0 is not orthogonal, an actual rational inner pair Q,U for W with U=WQ has price m(P), and already its values at zero force
\[
 m(P)\ge\sum_{j=1}^r\log^+\sigma_j(W_0)
       \ge\frac12\log2>c_{\rm mat}.
 \tag{IR6}
\]
Here sigma_j are the Euclidean singular values, with all r multiplicities.
This second branch does not apply the normalized integer-germ theorem directly to W.

### IR3. The exact multiplier and content gate

More generally suppose, for the same primitive p in (IR1), that
\[
 cp=\sum_{j=1}^r v_jv_j^\star,\qquad
 c\in\mathbb Z_{>0},\quad v_j\in\mathbb Z[z],\quad \deg v_j\le d,
 \tag{IR7}
\]
with zero summands deleted.
Let g>0 be the gcd of all coefficients of all v_j.
For the actual rational reflection
\[
 W_c=I_r-\frac{2\varepsilon}{c}\frac{z^dv(z)v(z^{-1})^T}{P(z)}
 \tag{IR8}
\]
one has
\[
 g^2\mid c,\qquad
 W_c\text{ has an integer germ at zero}
 \quad\Longleftrightarrow\quad
 c/g^2\in\{1,2\}.
 \tag{IR9}
\]
Thus an integral reflection of this form, after removing common coefficient content, gives precisely a multiplier-one or multiplier-two integral SOS certificate with unchanged degree support.
An arbitrary denominator-clearing multiplier supplies no additional integral-reflection case.

## Argument

<a id="certificate-positivity-and-circle-exclusion"></a>
### 1. Positivity and the exact excluded domain

Reciprocity makes z^(-d)P real on the circle.
The right side of (IR2) is a sum of squared absolute values there, so p>=0.
If P had a unit-circle root alpha, each v_j(alpha) would vanish.
Every nonzero v_j has degree at most d<2d, whereas the minimal polynomial of alpha is P.
This is impossible.
Therefore P has no unit-circle root and p>0 everywhere on the circle.

The same argument applies to (IR7), since c>0.
The one-summand case is also impossible: multiplying its identity by z^d would express a nonzero scalar multiple of the irreducible P as v_1(z) times z^d v_1(z^{-1}), two polynomials of degree at most d<2d.
Irreducibility would force P to divide one of those lower-degree nonzero factors.
In particular no irreducible Salem polynomial with its unit-circle conjugates can satisfy these degree-bounded certificates.
This is a genuine exclusion of part of the original problem's domain, not a contradiction to the original problem.
The sign epsilon allows either constant sign of z^(-d)P.
For example z^2-3z+1 has negative phase-balanced value on the circle; positivity should not silently fix epsilon=+1.

<a id="reflection-and-exact-original-poles"></a>
### 2. Arithmetic reflection and all original pole lengths

Write
\[
 v(z)=\sum_{k=0}^d a_k z^k,\qquad a_k\in\mathbb Z^r.
\]
Each entry of A in (IR4) is a polynomial with integer coefficients, since its least possible exponent is d+0-d=0.
As P(0)=1, the formal inverse 1/P has integer Taylor coefficients by coefficient recursion.
Hence W is an integer germ.

Taking the coefficient of z^d in (IR2) gives
\[
 a_d^T a_0=2\varepsilon,\qquad
 W_0=I_r-\varepsilon a_0a_d^T.
 \tag{1}
\]
Thus W_0^2=I_r and det W_0=1-\varepsilon a_d^Ta_0=-1.
The full Laurent identity gives
\[
 v(z^{-1})^Tv(z)=2\varepsilon z^{-d}P(z).
 \tag{2}
\]
Substituting (2) in the square of (IR4) shows W^2=I_r as a rational identity.
The rank-one determinant identity gives det W=-1 as a rational identity as well.

On the circle,
\[
 W=I_r-\frac{vv^*}{p}
   =I_r-2\frac{vv^*}{v^*v}.
 \tag{3}
\]
The denominator is positive by the first section.
Consequently W is a Hermitian unitary reflection there.

Irreducibility in characteristic zero makes every root alpha of P simple.
The constant term excludes alpha=0.
At such a root the residue is
\[
 R_\alpha=-\frac{\varepsilon\alpha^d}{P'(\alpha)}
                v(\alpha)v(\alpha^{-1})^T.
 \tag{4}
\]
A nonzero component v_j cannot vanish at alpha, by its degree bound.
Reciprocity implies that alpha^(-1) is also a root with minimal polynomial P, so the same assertion holds at alpha^(-1).
Both vectors in (4) are therefore nonzero, and R_alpha has rank one.
Every original root is a genuine pole; in particular W is nonconstant.

For an analytic column h near alpha, the product Wh is analytic precisely when R_alpha h(alpha)=0.
Indeed W has at most a simple pole and its only negative Laurent coefficient is R_alpha.
The evaluation map h -> R_alpha h(alpha) has one-dimensional image, so
\[
 \delta_\alpha(W)
 =\dim_{\mathbb C}\bigl(O_\alpha^r/K_\alpha(W)\bigr)=1.
 \tag{5}
\]
There are no other finite poles.
This establishes the full cancellation cost without replacing it by a scalar denominator copied r times.

For a monic polynomial with constant term one, the sum of log|alpha| over all roots is zero.
By the defining root formula for total Mahler measure,
\[
 m(P)=\sum_{|\alpha|>1}\log|\alpha|
     =-\sum_{|\alpha|<1}\log|\alpha|.
 \tag{6}
\]
Equations (5)--(6) give (IR5).
No root orbit, pole rank or factor of the degree has been discarded.

<a id="circle-unitary-invertible-origin-extension"></a>
### 3. Exact inner cancellation with an invertible, unnormalized constant value

The following is the limited extension of v5 needed here.
Let R be a square rational matrix, holomorphic near zero with R(0) invertible, and unitary on the circle.
Then there are rational matrix functions Q,U, holomorphic on a neighborhood of the closed disk and contractive in the disk, such that
\[
 U=RQ,\qquad \det Q(0)\ne0,\qquad
 -\log|\det Q(0)|=N(R).
 \tag{7}
\]
The actual hypothesis R(0)=I is unnecessary for this circle-unitary construction.

To check this precisely, use the [polynomial cancellation module in v5](Yin_C_G0868_v5.md#minimal-pole-module-inner-factor).
Its construction takes the polynomial columns whose products with R are analytic at every disk pole and forms a basis matrix M.
It gives
\[
 \det M(z)=c_0\prod_{a\in\mathbb D}(z-a)^{\delta_a(R)},\qquad c_0\ne0,
 \tag{8}
\]
with no other determinant zero.
The absence of a pole at zero makes M(0) invertible.
No step in that polynomial module, its local jet comparison or (8) uses R(0)=I.

The same adopted finite polynomial matrix factorization gives an outer polynomial H with M^*M=H^*H on the circle.
The [outer-to-disk-invertibility argument in v5](Yin_C_G0868_v5.md#minimal-pole-module-inner-factor) makes H invertible on the closed disk.
Set B=MH^(-1).
Then B is rational inner, RB has no disk poles, and scalar determinant Jensen with (8) gives
\[
 -\log|\det B(0)|
   =\sum_{a\in\mathbb D}\delta_a(R)\log\frac1{|a|}
   =N(R).
 \tag{9}
\]
A rational circle-unitary matrix cannot have a genuine circle pole: one of its reduced entries would be unbounded along a punctured circle arc.
Thus RB has no circle pole and is unitary on the circle.
The scalar maximum principle applied to all fixed matrix coefficients makes B and RB disk contractions.
Taking Q=B and U=RB proves (7).

For completeness this price is minimal even without normalizing R(0).
For any admissible Q with RQ analytic, the local module argument in v5 gives ord_a det Q>=delta_a(R).
The determinant of a disk-contractive Q has boundary size at most one on every inner circle.
Scalar Jensen and a limit through inner radii therefore imply -log|det Q(0)|>=N(R).
This uses the zeros of det Q with multiplicity and does not require R(0)=I.
No coefficient-field descent for B or U is asserted or needed.

<a id="constant-involution-cost-dichotomy"></a>
### 4. The stronger price from the constant involution

First suppose W_0 is orthogonal.
Its inverse is an integer matrix, because W_0 is an integer involution.
The matrix
\[
 F(z)=W(z)W_0^{-1}
 \tag{10}
\]
is therefore an integer germ with F(0)=I_r.
It is nonconstant, since W is nonconstant.
Right multiplication by a constant orthogonal matrix preserves circle unitarity and every pole-cancellation length.
Equations (5)--(7), or directly the adopted v5 normalized statement, give an actual admissible pair for F with price m(P).
The [v4 Euclidean determinant estimate](Yin_C_G0868_v4.md#gram-loewner-determinant) applied to its first nonzero integer coefficient gives
\[
 m(P)\ge\frac12\log\frac54.
 \tag{11}
\]

Now suppose W_0 is not orthogonal.
For any pair Q,U with both disk-contractive and U=WQ, put V=Q(0)Q(0)^* and K=W_0^*W_0.
Both are positive definite, and the contractions at zero give
\[
 V\le I_r,\qquad W_0VW_0^*\le I_r,
 \qquad\text{hence}\qquad V\le K^{-1}.
 \tag{12}
\]
In an orthonormal eigenbasis of K, each diagonal entry of V is at most both 1 and the corresponding reciprocal eigenvalue.
Hadamard's determinant inequality yields
\[
 |\det Q(0)|^2=\det V
 \le\prod_{j=1}^r\min(1,\sigma_j(W_0)^{-2}),
\]
and hence
\[
 -\log|\det Q(0)|
 \ge\sum_{j=1}^r\log^+\sigma_j(W_0).
 \tag{13}
\]

Every column of the invertible integer matrix W_0 has positive integer squared norm.
If all those norms were one, its columns would be signed coordinate vectors.
Invertibility would make them distinct, and W_0 would be orthogonal.
Thus some column has squared norm at least two, so sigma_max(W_0)>=sqrt(2).
It follows from (13) that the price is at least (1/2)log2.

The actual pair in (7), now with R=W, has price exactly N(W)=m(P).
Therefore
\[
 m(P)\ge\frac12\log2>\frac12\log\frac54.
 \tag{14}
\]
This proves (IR3) in both cases.
There is no power-pullback step, and no scalar replication by the certificate rank.
The nonorthogonal branch uses (13), not a mistaken application of a normalized-germ theorem to W.

<a id="primitive-sos-content-gate"></a>
### 5. Exactly which multiplier certificates give an integral reflection

Consider (IR7)--(IR8).
Set h_j=cont(v_j)>0, the gcd of the coefficients of the nonzero polynomial v_j, and g=gcd_j h_j.
With reversal padded to degree d, put
\[
 v_j^{R,d}(z)=z^dv_j(z^{-1}),\qquad
 A_{ij}=v_i v_j^{R,d}.
\]
These are integer polynomials and cont(v_j^{R,d})=h_j.
Gauss content multiplication gives
\[
 \operatorname{cont}(A_{ij})=h_i h_j.
 \tag{15}
\]
One elementary justification is prime by prime: after removing the smallest coefficient valuation from each factor, both reductions are nonzero polynomials over a field, and their product is nonzero.
Thus the smallest coefficient valuation of a product is the sum of the two smallest valuations.

Every h_i h_j is divisible by g^2.
The gcd of the diagonal products h_i^2 is already g^2.
Consequently the gcd of all coefficients of all A_ij is exactly g^2.

The identity (IR7), after writing v_j=g u_j, says that every Laurent coefficient of cp is divisible by g^2.
Since p is primitive, those coefficients have gcd c, so g^2 divides c.
Write k=c/g^2 in Z_(>0).

Because P and its formal inverse at zero have integer coefficients,
\[
 \frac{2\varepsilon}{c}\frac{A_{ij}}{P}
 \text{ has an integer Taylor germ}
 \quad\Longleftrightarrow\quad
 \frac2c A_{ij}\in\mathbb Z[z].
 \tag{16}
\]
The forward implication follows by multiplication by P; the reverse by multiplication by its integer formal inverse.
Therefore W_c is an integer germ precisely when c divides twice every coefficient of every A_ij, equivalently c divides 2g^2.
Together with g^2|c, this is k|2, proving (IR9).
Dividing the SOS identity by g^2 gives
\[
 k p=\sum_j u_j u_j^\star,\qquad k\in\{1,2\}.
 \tag{17}
\]
The degrees are unchanged and the u_j have collective coefficient content one.
For k=1, duplicate each u_j to obtain a certificate of the form (IR2).
The same original-input bound follows.

This is a criterion for this actual rank-one reflection formula.
It does not exclude other matrix constructions from a larger multiplier or another arithmetic structure.

<a id="doubled-quartic-minimum-rank"></a>
### 6. An irreducible positive control that needs doubling

Take
\[
 P_4=z^4+z^3+3z^2+z+1,\qquad
 p_4=z^{-2}P_4=3+z+z^{-1}+z^2+z^{-2}.
 \tag{18}
\]
For c=cos(theta),
\[
 p_4(e^{i\theta})=4c^2+2c+1
                =4(c+1/4)^2+3/4>0.
\]
This polynomial is irreducible over Q.
Indeed it has no rational root: the possible integer roots of a monic constant-one polynomial are +1 and -1, and neither is a root.
If it factors, Gauss's lemma gives two monic integer quadratics with constant terms both +1 or both -1.
In the first case their linear coefficients a,b must satisfy a+b=1 and ab=1, impossible for integers.
In the second case the coefficients of z^3 and z have opposite signs, whereas both are +1 in P_4.
Thus no such factorization exists.

The earlier [L133 v8 proof](../ledger/Yin_L_G0133_v8.md#positive-polynomial-integer-sos-control) excludes an integer SOS of p_4 itself for every finite rank and Laurent width.
That result does not exclude the following exact doubled certificate:
\[
 2p_4=|1+z+z^2|^2+|1+z^2|^2+1.
 \tag{19}
\]
All three terms have degree at most two, so this is an actual instance of (IR2).
The reflection theorem applies at the original degree four and total m(P_4).

Moreover three is the smallest number of nonzero integer squares in this degree-at-most-two window.
A hypothetical one-square representation could be padded with a zero second row, so it suffices to exclude two rows.
Let their coefficient columns be a,b,c in Z^2.
Comparing the three autocorrelation coefficients gives
\[
 \|a\|^2+\|b\|^2+\|c\|^2=6,\qquad
 a\mathbin{\cdot}c=2,\qquad (a+c)\mathbin{\cdot}b=2.
\]
Put u=a+c and w=a-c.
Then
\[
 \|w\|^2+\|b\|^2=2,\qquad
 \|u\|^2=\|w\|^2+8,\qquad u\equiv w\pmod2.
 \tag{20}
\]
If ||w||^2=0, then a=c has squared norm two, so u=(+/-2,+/-2) and b=(+/-1,+/-1); u dot b is 0 or +/-4.
If ||w||^2=1, then b is a signed coordinate vector and u has squared norm nine.
In Z^2 such a u has its sole nonzero coordinate equal to +/-3; the parity relation places it in the same coordinate as w.
Thus u dot b is 0 or +/-3.
If ||w||^2=2, then b=0.
No case allows u dot b=2.
This proves the claimed minimum within the actual degree window, not for arbitrary larger Laurent support.
The argument is exact and does not rely on enumeration or floating root tests.

<a id="finite-sos-feasibility-and-source-limits"></a>
### 7. A finite actual-support test and the source boundaries

Write p=p_0+sum_(k=1)^d p_k(z^k+z^(-k)) with integer coefficients.
Under a certificate (IR2), p_0>0 and the sum of squares of all integer coefficients of all summands is 2p_0.
Each nonzero row therefore has energy at least one, there are at most 2p_0 rows, and every coefficient has magnitude at most sqrt(2p_0).
Define the finite set of integer rows
\[
 {\cal A}=\{a=(a_0,\ldots,a_d)\in\mathbb Z^{d+1}:
                         1\le\sum_i a_i^2\le2p_0\},
\]
and their autocorrelation vectors
\[
 t(a)_k=\sum_{i=0}^{d-k}a_i a_{i+k},\qquad 0\le k\le d.
 \tag{21}
\]
An actual degree-at-most-d certificate exists if and only if there are nonnegative integers n_a with
\[
 \sum_{a\in{\cal A}}n_a t(a)=(2p_0,2p_1,\ldots,2p_d).
 \tag{22}
\]
The forward direction groups equal coefficient rows.
For the reverse direction, repeat the polynomial sum_i a_i z^i exactly n_a times.
The coordinate k=0 bounds every multiplicity and the total number of rows, so this is a finite exact decision problem.
This equivalence alone gives no efficient degree-uniform algorithm or universal solvability theorem.
Allowing larger support changes the finite problem; no integral degree-compression theorem is assumed.

[J136](../computations/programs/Yin_J_G0136/readme.md) retains actual small exploratory native programs, their parameters and reproduction.
Its p4 two-row test returned no pair; the proof above independently supplies that result.
Its d=3,4,5 scan uses exact integer autocorrelations but only a floating Chebyshev positivity filter and found no failure among the screened inputs.
That screen is not a positivity classification, a representation theorem or a premise of (IR3), (IR9), (20) or (22).

For the original strictly positive integral p, viewed as a rational input of actual support radius d, the adopted C34 real-rational Gram result gives
\[
 p=\sum_j w_j|f_j|^2,\qquad
 w_j\in\mathbb Q_{>0},\quad f_j\in\mathbb Q[z],\quad\deg f_j\le d.
\]
Choose positive integers D,B with D f_j integral and B w_j positive integers.
Then
\[
 D^2B\,p=\sum_j (B w_j)|D f_j|^2.
 \tag{23}
\]
Repeating each summand according to its integer weight gives some integral-multiplier SOS of the same degree.
Equation (IR9) identifies the missing arithmetic step exactly: after common-content removal, that multiplier must be one or two to produce this integral reflection.
No such conclusion follows merely by clearing denominators.

The sufficient [MSEDSV22 account](../audits/literature/MSEDSV22/Yin_U001.md#msedsv22-u001) concerns arXiv:2202.06544v2, Section 4 and Section 5 Algorithm 3, at its stated selected inspection depth.
The relevant output is positive rational weights and degree-bounded Gaussian-rational polynomial factors, not an unweighted integer decomposition of 2p.
This comparison reuses that account and asserts no whole algorithm-proof audit, coefficient-field descent or multiplier-two theorem.

YY22, Qianqian Yang and Kiyoto Yoshino, [Embedding theory of lattices and its application to 2-integrable lattices](https://math.colgate.edu/~integers/w57/w57.pdf), Integers 22 (2022), A57, supplies a separate limited comparison.
The actual inspected passages are the definition on printed pages 1--2 and Theorems 1 and 3 on printed pages 2--3.
A lattice is 2-integrable when its scaling by sqrt(2) embeds into some standard integer lattice.
Those theorem statements give rank-twelve positive definite integral lattices that are not 2-integrable, with determinants seven and fifteen.
Accordingly an arbitrary integral Gram cannot always be made an integer sum of rank-one squares merely by doubling and increasing the target dimension.
The complete classification, computer-assisted nonintegrability proof and algorithms were not audited here, and this source is not a dependency of the reflection theorem.
Its matrix obstruction is not a scalar Laurent counterexample: the same scalar diagonal-sum fiber might contain a different Gram admitting the required representation.

<a id="certificate-original-input-boundary"></a>
### 8. Original-input return and what remains unsupplied

The conclusion is a genuine total-measure bound for every irreducible monic reciprocal original P with a supplied degree-bounded certificate (IR2), or with (IR7) satisfying the exact integral-reflection criterion.
The actual matrix dimension r, original degree 2d, all pole multiplicities and full determinant price have been retained.
The bound uses the actual original P, not a measure-preserving assertion about an auxiliary polynomial.
It does not depend on a bounded rank, rational metric choice, scalar-copy shortcut, probability argument or numerical absence of small examples.

Neither the rational Gram theorem nor the lattice comparison supplies such certificates for every no-circle-root input.
The circle-root argument excludes irreducible Salem inputs from this certificate class outright.
No positive-measure sequence tending to zero, universal multiplier-two theorem, all-input realization or unrestricted completion of the [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) is asserted.

## Assessment history

### Decision whole-integral-reflection-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:57 |
| status | proved |
| reason | Adopt the complete integer-reflection certificate theorem after independent whole-proof finding R1091 v6. The actual original polynomial has exact pole price m(P), and the constant-involution dichotomy yields m(P)>=log(5/4)/2 on the stated certificate class. The exact multiplier/content gate, control, finite feasibility criterion and source/computation limits are included. Neither universal certificate existence nor coverage of circle-root inputs or unrestricted G0001 completion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete integral-reflection statement](#statement) | IR1-IR9, the original degree-bounded integer certificate class, all original pole lengths, uniform total Mahler bound, constant-value alternatives and exact common-content criterion. |
| argument | [Complete integral-reflection proof](#argument) | All eight sections, including positivity and excluded circle roots, invertible-origin extension, the stronger price dichotomy, quartic control, finite feasibility and actual source/computation boundaries. |
| dependency | [Euclidean integer-germ estimate](Yin_C_G0868_v4.md#gram-loewner-determinant) | H=I total determinant bound for normalized nonconstant integer germs; no arithmetic condition on the contracting pair. |
| dependency | [Exact inner cancellation construction](Yin_C_G0868_v5.md#minimal-pole-module-inner-factor) | Actual polynomial pole module, exact multiplicities, outer factor and determinant Jensen; the extension to an invertible unnormalized constant is proved explicitly in v6. |
| dependency | [Accepted polynomial factorization](../audits/literature/DR10/Yin_U002.md#dr10-u002) | Inherited finite square Fejer--Riesz theorem and outer convention at the accepted statement/applicability depth, without a new original-proof or coefficient-field audit. |
| dependency | [Undoubled quartic obstruction](../ledger/Yin_L_G0133_v8.md#positive-polynomial-integer-sos-control) | Only the complete coefficient-energy-three proof excluding an undoubled p4 integer SOS for arbitrary finite rank and Laurent width. |
| support | [Rational Gram and LDL comparison](Yin_C_G0034_v1.md#minimal-rational-gram-ldl-and-boundaries) | Strict real rational positivity gives degree-bounded positive rational weighted squares and some clearing multiplier; neither multiplier two nor later physical-window claims are inferred. |
| support | [Existing algorithm interface](../audits/literature/MSEDSV22/Yin_U001.md#msedsv22-u001) | Retained selected statement/method inspection of Gaussian-rational weighted factors, with its actual source and algorithm-proof limits. |
| support | [Bounded native enumeration](../computations/programs/Yin_J_G0136/readme.md) | Exploratory integer autocorrelations and uncertified floating positivity screen only; no computation output is a premise of the theorem or the exact controls. |
| review | [Independent integral-reflection whole-proof finding](../audits/reviews/Yin_R_G1091_v6.md#integral-reflection-whole-proof-finding) | Entire IR1-IR9 statement and eight-section argument, all controls and source/computation interfaces; isolated reproduction retains its nonproof scope, and no substantive reviewer repair was required. |

## Current assessment

[Selected decision](#decision-whole-integral-reflection-review-2026-11-05)

