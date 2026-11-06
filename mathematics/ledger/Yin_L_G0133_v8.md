---
author: Yin
---

# Actual integral matrix realizations and their original-input costs

Date: 2026-11-05.
Prepared for Yin under the [unrestricted G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
The coordinating agent supplied the concrete two-dimensional rational unitary block, the power-pullback normalization and the integral sum-of-squares control.
The matrix_integer_return delegate checked those constructions, developed the power-pullback pole obstruction and prepared this comparison.
The matrix_integer_return and pell_family_probe delegates independently found the shorter same-input commutator used below.
The witt_moment_compatibility delegate developed the exact standard-companion norm and the integral trace-basis comparison, with coordinating-agent checks.
These are author-side deductions and ordinary checks, not an independent review or a new Claim assessment.

<a id="matrix-original-input-scope"></a>
## The original-input question and fixed interfaces

The missing comparison is an actual construction for every positive-measure original irreducible reciprocal monic integer polynomial P with P(0)=1 of a nonconstant integral matrix germ F, normalized by F(0)=I, with disk-holomorphic Euclidean contractions Q and U satisfying U=FQ near zero and
\[
 \tau=-\log|\det Q(0)|\le C_{\rm tr}m(P)
 \tag{1}
\]
for one absolute positive constant C_tr.
Q(0) must be invertible, and total logarithmic Mahler measure m(P) is never divided by degree.
The [matrix theorem in C868 v3](../claims/Yin_C_G0868_v3.md#matrix-column-determinant-gap), at its [selected assessment](../claims/Yin_C_G0868_v3.md#decision-whole-matrix-review-2026-11-05), would then give a uniform positive original-input gap.
Its actual first-coefficient estimate is
\[
 \tau\ge\frac12\log\left(1+\frac{\|C_N\|_{\rm op}^2}{4}\right)
 \ge\frac12\log\frac54,
 \qquad F=I+C_Nz^N+O(z^{N+1}),\quad C_N\ne0.
 \tag{2}
\]
The proof and the positive-metric and scalar-copy costs remain at that fixed Claim.

[L133 v7](Yin_L_G0133_v7.md#original-cost-tests-scope) retains the earlier denominator, polarization and central-split cost tests; versions v1--v7 are unchanged.
This version supplies an actual matrix realization on one already separated input family, then tests three possible ways to extend it.
It retains the useful construction and the precise failures, without supplying (1) on the unrestricted domain.
All matrix norms here are Euclidean operator norms unless a positive metric is explicitly displayed.
Circle measure is normalized Haar measure.

The [C65](../claims/Yin_C_G0065_v1.md#statement) and [C67](../claims/Yin_C_G0067_v1.md#statement) rigidity statements require rational Laurent matrices with universal original-order membership and their stated flat-support and row-width hypotheses.
The rational matrix germs below instead have genuine finite poles and integer Taylor coefficients at zero, so those are different domains.
[C36](../claims/Yin_C_G0036_v1.md#statement) retains the costs of its particular rational completion; its denominator or pole charges are not silently dropped here.
[C90](../claims/Yin_C_G0090_v1.md#statement) concerns a fixed independent power dictionary and the actual coefficient quotient, not these Taylor matrix germs.
No factorization theorem is being used as an automatic integer-realization or cost theorem.

<a id="actual-pell-matrix"></a>
## A concrete original polynomial and an integral rational unitary block

Put
\[
 P(z)=z^2-3z+1,\qquad A(z)=z^2-z+1,\qquad
 a(z)=\frac{A(z)}{P(z)},\qquad b(z)=\frac{2(1-z)}{P(z)},
\]
\[
 T(z)=\begin{pmatrix}a(z)&b(z)\\zb(z)&a(z)\end{pmatrix}.
 \tag{3}
\]
Since A=P+2z and P+z=(1-z)^2, direct multiplication gives
\[
 A^2-P^2=4z(P+z)=4z(1-z)^2,
 \qquad a^2-zb^2=1.
 \tag{4}
\]
Consequently
\[
 \det T=1,\qquad
 T^{-1}=\begin{pmatrix}a&-b\\-zb&a\end{pmatrix}.
 \tag{5}
\]
Both T and its inverse have integer Taylor coefficients at zero because their numerators are integral and P(0)=1.
Their constant terms and first coefficients are
\[
 T_0=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
 T(z)=T_0+z\begin{pmatrix}2&4\\2&2\end{pmatrix}+O(z^2).
 \tag{6}
\]

For |z|=1, reciprocity of A and P gives conjugate(a)=a, while
\[
 \overline{b(z)}=-zb(z).
\]
The adjoint of T on the circle is therefore exactly the inverse in (5).
The roots of P are
\[
 \lambda=\frac{3+\sqrt5}{2}>1,\qquad \rho=\lambda^{-1}\in(0,1),
\]
so P has no circle zero and T is unitary everywhere on the circle.
The original total measure is m(P)=log lambda.
This quadratic input belongs to the already explicit positive-measure class in [C20](../claims/Yin_C_G0020_v1.md#statement); no new small-measure family is supplied by (3).

<a id="matrix-power-pullback-realization"></a>
## A rank-two realization with its complete determinant price

Define
\[
 F(z)=T(z)T(z^2)^{-1}.
 \tag{7}
\]
Then F(0)=I_2, F has integer Taylor coefficients and F is unitary on the circle.
Its entries have the common denominator P(z)P(z^2), with cancellation allowed rather than required.
From (6), the first coefficient is
\[
 F(z)=I_2+z\begin{pmatrix}2&0\\2&-2\end{pmatrix}+O(z^2),
 \tag{8}
\]
so the germ is genuinely nonconstant.

For the actual inside root rho, set
\[
 B(z)=\frac{\rho-z}{1-\rho z},\qquad
 q(z)=B(z)B(z^2),\qquad Q(z)=q(z)I_2,\qquad U(z)=F(z)Q(z).
 \tag{9}
\]
B and B(z^2) are scalar inner functions, with constant coefficient rho each.
Their zeros cancel all possible disk poles contributed by P(z) and P(z^2), respectively, with their actual multiplicities.
The resulting U is rational and holomorphic on a neighborhood of the closed disk.
On the circle q has modulus one and F is unitary, so U is unitary there.
For any unit vectors v and w, the scalar function w*U(z)v is holomorphic and has boundary modulus at most one.
The maximum principle, followed by the supremum over v and w, proves ||U(z)||op<=1 throughout the disk.
The same bound for Q follows directly from the inner scalar q.
Thus these are actual Euclidean contractions with baseline one, not formal determinant data alone.

At zero,
\[
 Q(0)=\rho^2I_2,\qquad
 \tau=-\log|\det Q(0)|=4\log\lambda=4m(P).
 \tag{10}
\]
The factor four includes both polynomial pullbacks and both matrix columns.
The damping scalar need not have integer coefficients; the arithmetic hypothesis of C868 v3 is imposed on F, where it has been verified.
The identity U=FQ is an identity of germs near zero and of rational functions wherever defined; poles of F inside the disk do not obstruct the required holomorphy of U.

More generally, if an integral rational matrix germ T is nonconstant, T(0) is unimodular integral and T is circle-unitary, then T(z)T(z^2)^(-1) has constant coefficient I and integer Taylor coefficients.
If N is the first positive coefficient index of T, its coefficient at N is T_N T(0)^(-1), which is nonzero.
This proves nonconstancy without assuming the full germ is disk-holomorphic.
It does not give a general price formula: zeros of det T can introduce additional poles of T^(-1), which must be charged.
The exact inverse (5) is what makes (10) valid for the present input.

For every h>=1, replacing z by z^h in (3)--(10) gives the same rank-two realization for P_h(z)=P(z^h), with first nonzero coefficient at h and price 4m(P_h).
There are h roots of modulus lambda^(1/h) and h roots of modulus lambda^(-1/h), so
\[
 m(P_h)=\log\lambda
 \tag{11}
\]
is independent of h.
This gives unbounded degree but no positive measures approaching zero, and irreducibility of the composed polynomials is not assumed.

<a id="matrix-same-p-commutator"></a>
## A comparison using only the original polynomial as denominator

Embed the two-by-two block T in coordinate positions (1,2) or (1,3) of a three-by-three identity matrix, and denote the results by T_12 and T_13.
Put
\[
 F_{\rm same}=T_{12}T_{13}T_{12}^{-1}T_{13}^{-1}.
 \tag{12}
\]
At zero the two embedded blocks are I_3+2E_12 and I_3+2E_13, which commute.
Hence F_same(0)=I_3.
Every factor and inverse factor has integral Taylor coefficients, circle-unitary boundary values and common denominator P, so F_same has the same arithmetic and boundary properties with common denominator P^4.
A direct row-column multiplication gives the exact entry
\[
 (F_{\rm same})_{32}=-zb^2
       =-\frac{4z(1-z)^2}{P(z)^2}.
 \tag{13}
\]
For example, after the first three factors the third row is (azb,-zb^2,a), and multiplication by T_13^(-1) leaves its second entry unchanged.
Thus F_same is nonconstant.

Taking Q_same=B^4 I_3 and U_same=F_same Q_same cancels all disk poles and gives the same closed-disk holomorphy and boundary-unitarity argument as (9).
Both functions are Euclidean contractions, and
\[
 Q_{\rm same}(0)=\rho^4 I_3,\qquad
 \tau_{\rm same}=12m(P).
 \tag{14}
\]
This is a genuine original-P-only realization, at a larger complete price than the power-pullback construction.
The scalar reciprocal ratio P*/P would be constant, so the example shows that this particular scalar degeneracy does not prohibit every nonconstant integral matrix realization on a no-circle-root input.
It does not establish a uniform supply of such blocks for other original polynomials.

<a id="power-pullback-circle-pole-rigidity"></a>
## Power pullbacks retain the unit-circle conjugate obstruction

Let P in Q[z] be irreducible, with P(0) nonzero and a root beta on the unit circle.
For every positive integer h, every Q-irreducible factor R of P(z^h) has a root on the unit circle.
Indeed, take a root gamma of R and put alpha=gamma^h.
Then alpha is a root of P.
There is a Q-embedding of Q(alpha) into C taking alpha to beta because P is irreducible.
Extend this embedding to the finite algebraic extension Q(gamma): concretely, send gamma to a root of the polynomial obtained by applying the embedding to its minimal polynomial over Q(alpha).
This defines an injective field embedding since that minimal polynomial is irreducible.
Its image delta satisfies delta^h=beta and R(delta)=0, so |delta|=1.
This argument allows P(z^h) to be reducible.

Fix any finite list h_1,...,h_l of positive integers and any matrix size r.
Suppose W has rational-function entries in
\[
 \mathbb Q[z,z^{-1},P(z^{h_1})^{-1},\ldots,P(z^{h_l})^{-1}],
 \tag{15}
\]
is holomorphic near zero, satisfies W(0)=I_r and is unitary almost everywhere on the circle.
Every possible nonzero finite pole factor of a reduced scalar entry is a Q-irreducible factor R of one of those pullbacks.
The preceding argument gives a circle root delta of R.
A numerator coprime to R cannot vanish at delta, since R is its rational minimal polynomial up to a scalar.
Thus any occurrence of R in the reduced denominator would produce a genuine pole at delta.
Along a punctured circle arc approaching delta, the modulus of that entry would become unbounded, contradicting its almost-everywhere bound by one from unitarity.
Every such factor, including every possible multiplicity, is therefore absent from the reduced denominator.
The possible Laurent pole at zero is excluded by the assumed holomorphy.
Consequently W is polynomial.

Write W=sum_n W_n z^n.
For each row i, polynomial Parseval and circle unitarity give
\[
 \sum_{n,j}|(W_n)_{ij}|^2=1.
 \tag{16}
\]
The constant row of W_0=I_r already has squared norm one, so every nonconstant coefficient vanishes.
Thus W=I_r.

This is the [C868 v3 original-pole mechanism](../claims/Yin_C_G0868_v3.md#original-circle-pole-rigidity) with the power-pullback factors checked explicitly, not a claim that composition preserves irreducibility.
Allowing finitely many power pullbacks of an irreducible input with a circle conjugate therefore does not evade that rational circle-unitary obstruction.
Additional denominator factors unrelated to these pullbacks, nonrational coefficient fields and nonunitary Schur quotients remain outside the argument.
The conclusion does not prohibit every possible realization satisfying (1).

<a id="positive-polynomial-integer-sos-control"></a>
## Strict positivity does not supply an integral sum of squares

A possible arithmetic completion step would ask for an integral sum-of-squares representation of a positive reciprocal Laurent polynomial.
The concrete input
\[
 P_4(z)=z^4+z^3+3z^2+z+1,\qquad
 p(z)=z^{-2}P_4(z)=3+z+z^{-1}+z^2+z^{-2}
 \tag{17}
\]
shows that positivity alone does not supply this representation, even with unrestricted finite rank and Laurent width.
The polynomial P_4 already appears as the noncyclotomic factor of C_D=(t^2-1)P_4 in [C480's retained auxiliary comparison](../claims/Yin_C_G0480_v1.md#complete-sextic-leading-root-cost).
Only that exact-polynomial correspondence is reused here; no new numerical measure or source-classification claim is made.

For z=e^(i theta) and c=cos theta,
\[
 p(z)=4c^2+2c+1=4(c+1/4)^2+3/4\ge3/4.
 \tag{18}
\]
Thus P_4 is monic reciprocal integral with constant coefficient one and has no circle zero.
Suppose, nevertheless, that
\[
 p(z)=\sum_{j=1}^{r}|v_j(z)|^2\quad\hbox{on the circle},
 \qquad v_j\in\mathbb Z[z,z^{-1}].
 \tag{19}
\]
After collecting each polynomial's coefficients, the constant Fourier coefficient on the right is the sum of the squares of all its integer coefficients.
The constant coefficient three on the left forces exactly three nonzero coefficients in total, all equal to +1 or -1.
Zero polynomials can be omitted.
There are only three ways to distribute these coefficients among the summands.

If they occur in three separate monomials, all positive Fourier coefficients vanish.
If they occur in a binomial and a monomial, exactly one positive frequency can occur, whereas p has nonzero coefficients at both frequencies one and two.
Finally, if they occur in one trinomial, order its three distinct exponents as u<v<w.
Its highest positive frequency is w-u, with the unique coefficient epsilon_u epsilon_w in {+1,-1}; it cannot cancel.
Since p has highest positive frequency two, w-u=2 and the exponents, after a monomial shift, are 0,1,2.
The coefficient at frequency one is then
\[
 \epsilon_1(\epsilon_0+\epsilon_2)\in\{-2,0,2\},
\]
which cannot equal the coefficient one of p.
This exhausts every possible rank and width in (19), and proves that no such integral representation exists.

The failure concerns exactly the proposed integral sum of absolute squares of Laurent polynomials.
It does not exclude rational-coefficient sums of squares, representations of a different polynomial such as a multiple of p, or every matrix realization with a denominator and its actual cost.
It supplies no counterexample to Lehmer's problem.

<a id="standard-companion-first-coefficient-cost"></a>
## Exact coefficient price for the standard companion candidate

Let
\[
 P(t)=t^d+\sum_{j=0}^{d-1}a_jt^j\in\mathbb Z[t],
 \qquad a_0\in\{+1,-1\},\qquad d\ge1.
\]
Use the standard column companion C, with zero-based coordinate vectors e_0,...,e_(d-1):
\[
 Ce_j=e_{j+1}\ (0\le j<d-1),\qquad
 Ce_{d-1}=-(a_0,\ldots,a_{d-1})^T.
 \tag{20}
\]
The [C868 v3 companion candidate](../claims/Yin_C_G0868_v3.md#companion-reversal-cost) is
\[
 G_C(z)=(I-zC^{-T})(I-zC)^{-1}
       =I+zD+O(z^2),\qquad D=C-C^{-T}.
 \tag{21}
\]
For d>=2, set
\[
 v=(a_1,\ldots,a_{d-1},0)^T,\qquad
 w=(0,a_1,\ldots,a_{d-1})^T,\qquad
 S_0=\sum_{j=1}^{d-1}a_j^2.
\]
The inverse equations C^(-1)e_(j+1)=e_j and
\[
 C^{-1}e_0=-a_0e_{d-1}-a_0\sum_{j=1}^{d-1}a_je_{j-1}
\]
give
\[
 D=a_0e_0v^T-we_{d-1}^T.
 \tag{22}
\]
Here v is perpendicular to e_(d-1), w is perpendicular to e_0, and both v and w have squared norm S_0.
Therefore
\[
 D^TD=vv^T+S_0e_{d-1}e_{d-1}^T,
 \qquad \|D\|_{\rm op}^2=S_0.
 \tag{23}
\]
When S_0>0, D has rank two and both nonzero singular values equal sqrt(S_0).
For d=1, the empty sum is zero, C=[-a_0] and D=0.
Whenever S_0=0, C is a signed permutation and G_C is identically I.
The assumption a_0=+1 or -1 is essential to this integer inverse and the displayed cancellation; nonunit constant coefficients are not included.

If S_0>0, (23) is the first nonzero coefficient of the integral germ G_C.
For every actual pair of Euclidean disk contractions Q,U with U=G_C Q near zero and Q(0) invertible, (2) yields
\[
 \tau\ge\frac12\log(1+S_0/4).
 \tag{24}
\]
The determinant cost is total and is not divided by d.
Such realizations with some finite cost exist: write H_C(z)=det(I-zC), take a sufficiently small positive constant epsilon, and set
\[
 Q=\varepsilon H_C I_d,\qquad
 U=\varepsilon(I-zC^{-T})\operatorname{adj}(I-zC).
\]
These are polynomial, satisfy U=G_C Q and Q(0)=epsilon I_d, and are both contractions when epsilon is chosen using their finite closed-disk suprema.
This observation supplies no bound on their price in terms of m(P).

For an odd prime p and P=Phi_p=1+t+...+t^(p-1), one has d=p-1, S_0=p-2 and m(P)=0.
Thus (24) grows as (1/2)log((p+2)/4), while the original measure is zero.
The prime two is the d=1 exception already treated.
This is a zero control, not a positive-measure sequence tending to zero.

The fixed-positive-measure family already used in [v7's polarization control](Yin_L_G0133_v7.md#polarization-controls) gives a different cost test here:
\[
 P_n(t)=(t^2-3t+1)(1+t^2)^n
       =(1+t^2)^{n+1}-3t(1+t^2)^n,\qquad n\ge1.
 \tag{25}
\]
It has degree 2n+2, constant coefficient one and total measure log lambda, independent of n.
Its even and odd coefficients have disjoint support, so the full coefficient square sum is
\[
 \sum_j ([t^j]P_n)^2
   =\binom{2n+2}{n+1}+9\binom{2n}{n},\qquad
 S_0=\binom{2n+2}{n+1}+9\binom{2n}{n}-2.
 \tag{26}
\]
In (26), [t^j]P_n denotes the coefficient before squaring.
The identities follow by taking the central coefficient in (1+t)^k(1+t)^k, which gives sum_j binom(k,j)^2=binom(2k,k).
Also binom(2n,n)>=4^n/(2n+1), since it is the largest of the 2n+1 coefficients of (1+t)^(2n), whose sum is 4^n.
Hence the lower bound (24) tends to infinity on this fixed-positive-measure family.
There is no uniform finite C_tr giving (1) for this standard-companion construction on all positive-measure inputs.
The family is reducible and has removable cyclotomic content, so this does not exclude an irreducible-only construction or one which first removes that content.

<a id="integral-trace-basis-countercontrol"></a>
## An actual integral basis change prevents an all-bases inference

The preceding coefficient-norm divergence is a property of the standard companion and must not be promoted to every integral basis of the same original order.
For the very same P_n in (25), put r=n+1 and introduce the trace variable s=t+t^(-1).
Then
\[
 q_n(s)=s^n(s-3),\qquad P_n(t)=t^r q_n(t+t^{-1}).
 \tag{27}
\]
Consider the two integral rings
\[
 R_n=\mathbb Z[t]/(P_n),\qquad
 A_n=\mathbb Z[s,t]/(q_n(s),t^2-st+1).
\]
They are isomorphic with the same distinguished t.
Indeed, t is a unit in R_n because P_n has constant coefficient one, and s=t+t^(-1) satisfies both relations of A_n by (27).
Conversely, t^(-1)=s-t in A_n and (27) gives P_n(t)=0, defining the reverse map.
The two maps are inverse because they fix t and send s back to t+t^(-1).

Monic division first by q_n in s, and then by t^2-st+1 in t, makes
\[
 1,s,\ldots,s^n,\ t,ts,\ldots,ts^n
 \tag{28}
\]
a Z-basis of A_n and therefore of the same R_n.
Thus its change from the original power basis is genuinely unimodular integral.
No rational enlargement of the lattice, change of order, reduced polynomial or deletion of repeated factors is involved.
Let S be the r-by-r standard companion of q_n on the s-basis.
Multiplication by t in the ordered basis (28) has matrix
\[
 C_{\rm trace}=\begin{pmatrix}0&-I_r\\I_r&S\end{pmatrix},\qquad
 C_{\rm trace}^{-1}=\begin{pmatrix}S&I_r\\-I_r&0\end{pmatrix}.
 \tag{29}
\]
The second identity follows either by multiplication or from t^(-1)=s-t.
Consequently its normalized-reversal first coefficient is
\[
 C_{\rm trace}-C_{\rm trace}^{-T}
       =\begin{pmatrix}-S^T&0\\0&S\end{pmatrix}.
 \tag{30}
\]

For n>=1, the first r-1 columns of S are the successive unit shifts and its last column is 3e_(r-1).
The final two nonzero columns are multiples 1 and 3 of that same coordinate vector, while all other nonzero columns occupy distinct coordinates.
Hence
\[
 \|S\|_{\rm op}^2=10,\qquad
 \|C_{\rm trace}-C_{\rm trace}^{-T}\|_{\rm op}^2=10.
 \tag{31}
\]
For the unused endpoint n=0, S=[3] and the corresponding square is nine.
The first-coefficient lower bound (2) for the trace-basis candidate is only the fixed value (1/2)log(7/2), rather than the divergence of (24)--(26).
This statement concerns that particular first-coefficient bound; it does not establish that the actual least Schur-realization cost is bounded.

There is a second distinction in using the basis change.
If B is the integral change-of-basis matrix and C_trace=B^(-1)CB, the Euclidean transpose in (21) generally means
\[
 G_{C_{\rm trace}}\ne B^{-1}G_C B.
 \tag{32}
\]
Merely conjugating an existing F,Q,U by B preserves the determinant of Q(0) and guarantees contraction in the positive metric H=B^T B in the new coordinates.
This distinction of norms is recorded in the [C868 v3 metric interface](../claims/Yin_C_G0868_v3.md#matrix-metric-and-copy-costs); it does not itself certify Euclidean contraction for the conjugated pair.
If instead one constructs the new Euclidean candidate G_(C_trace) from (29), its actual Q,U and upper price must be supplied afresh.
The basis calculation is therefore a countercontrol to an all-bases impossibility claim, not an actual solution of the original realization problem.

<a id="matrix-realization-return-boundary"></a>
## What the actual constructions leave to supply

The rank-two construction gives a nonconstant integral matrix germ, true disk contractions and a complete price 4m(P) on one explicit quadratic input and its power substitutions.
The same-P commutator gives a second actual realization with price 12m(P).
Their original measures already have a fixed positive lower bound, so these are nonempty models of the desired interface rather than new coverage of the difficult near-one regime.

For an irreducible original polynomial with a unit-circle conjugate, allowing finitely many power pullbacks as the only rational pole sources still forces a normalized circle-unitary matrix to be constant.
For a positive reciprocal Laurent polynomial with no circle zero, positivity alone does not even guarantee the proposed integral sum-of-squares completion.
The standard companion can incur an unbounded first-coefficient price on a fixed-positive-measure family, but an actual unimodular trace basis removes that particular divergence without supplying the missing contraction cost.
These are distinct restrictions and cannot be combined into an impossibility theorem for all integral matrix germs.

The remaining concrete obligation is to supply an integer-normalized germ for the original positive-measure irreducible inputs together with bounded analytic Q,U and the uniform upper price (1).
A proposed alternative using extra pole factors, nonrational intermediate coefficients, nonunitary Schur quotients or a changed basis must prove its actual integrality and its full determinant price.
No such general construction is supplied here, and the unrestricted G0001 objective remains unresolved.
