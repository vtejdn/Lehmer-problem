---
author: Yin
---

# A uniform Mahler gap at every fixed transvection count

<a id="statement"></a>
## Exact fixed-count theorem and uniformity

Use the permitted positive integral lattices, standard hyperbolic plane and even-norm fixed-cusp transvections of [v7](Yin_C_G0885_v7.md#statement).
The proof combines exact rational word reductions with the original finite-order integral positive factor; ordinary complementary proof collaborators contributed to its development.
Those development contributions are distinct from the required independent inspection.

For each fixed integer \(k\ge1\), there is an \(\eta_k>0\) such that every word of at most \(k\) permitted transvections at the two fixed cusps, with arbitrary intervening positive integral isometries on any positive integral lattice \(H\), satisfies
\[
m(P_A)=0\quad\hbox{or}\quad m(P_A)\ge\eta_k.
\]
There is no bound on original vector norms, rank, lattice determinant or positive-isometry orders.
The constant may depend on \(k\).
This forces the minimum permitted word length to tend to infinity along a positive-to-one sequence in these groups, without giving an arbitrary-length uniform gap or resolving the unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).

The proof keeps the original finite-order integral positive factor throughout.
Auxiliary rational matrices need not be integral or finite order.
Their complete characteristic polynomial remains the original monic integer polynomial by exact equalities and rational conjugacies.

The [adopted v7 cyclic adjacent-pair theorem](Yin_C_G0885_v7.md#decision-cyclic-adjacent-short-pair) and all its retained results remain valid unchanged.
In particular, the more explicit five-factor integral normalization is retained; the new general proof only needs a controlled rational final representation.

<a id="argument"></a>
## Complete proof and dependencies

The direct inputs are the real boundary identities of [v5](Yin_C_G0885_v5.md#boundary-action), the real pair decomposition of [v6](Yin_C_G0885_v6.md#middle-pair-decomposition), exact integer normalization and the accepted Sanders and DS17 statements identified in the arithmetic lemma.
The Fourier argument is reconstructed at the original finite-order integral factor, with the conventions used in [v3](Yin_C_G0885_v3.md#argument).
No numerical search, mathematical program or new original-source audit is used.
The fixed theorem retains the [six-factor controls](../ledger/Yin_L_G0462_v17.md#scope) as explanations of the invalid transfers it avoids, not as a premise that the rational factor has finite order.

<a id="weighted-cycle"></a>
## A weighted cycle supplies the next bounded pair

Write \(B(p)=E_pJ\), where \(J=s_{e+f}\), and consider
\[
A=R_0D_s B(p_1)\cdots B(p_n),
\]
with \(n\ge1\), \(s>0\), \(R_0\) any positive real isometry and all \(p_i\ne0\).
Put \(l_i=\|p_i\|\) and
\[
\delta=\min\{l_1l_2,\ldots,l_{n-1}l_n,\ s l_nl_1\}.
\]
For \(n=1\), this means \(\delta=s l_1^2\).
The complete claimed estimate is
\[
\delta>8\quad\Longrightarrow\quad
P_A(\Lambda)=0,\qquad
\Lambda\ge\gamma(\delta)^n,\qquad
M(P_A)\ge\gamma(\delta)^n,                              \tag{1}
\]
with \(\gamma(x)=(x-4+\sqrt{x(x-8)})/4\).

Use the actual null-vector and inversion identities of [C885 v5](Yin_C_G0885_v5.md#boundary-action).
Set
\[
\theta=\frac{1+\sqrt{1-8/\delta}}2,\quad
X_i=\{\|x\|\ge\theta l_i\},\quad
X_*=\{\|x\|\ge s\theta l_1\}.
\]
For \(f_i(x)=p_i+I(x)\), the same reverse triangle calculation gives
\(f_i(X_{i+1})\subset X_i\) for \(i<n\), and
\(f_n(X_*)\subset X_n\) using \(s l_nl_1\ge\delta\).
The final map \(x\mapsto sR_0x\) takes \(X_1\) into \(X_*\).
Thus the entire boundary action preserves the nonempty complete set \(X_*\).

The exact inversion-distance identity bounds its full Lipschitz constant by
\[
\frac{s\,2^n}{s^2\theta^{2n}\prod_i l_i^2}
=\frac{2^n}{s\theta^{2n}\prod_i l_i^2}
\le\gamma(\delta)^{-n}<1,
\]
because \(s\prod_i l_i^2\ge\delta^n\).
Iterating the full map gives a fixed point by the same summable-tail argument as in v5.
Every actual intermediate input lies in the specified domain.
The multiplier of \(D_s\) is \(1/s\), since
\(D_sn(x)=s^{-1}n(sx)\).
Therefore the full-vector multiplier at that fixed point is at least
\[
\frac1s\frac{s^2\theta^{2n}\prod_i l_i^2}{2^n}
\ge\gamma(\delta)^n.
\]
This proves (1) for every \(n\), including odd \(n\) and \(n=1\), with all original roots retained.

Since \(\gamma(10)=(3+\sqrt5)/2>2\), the condition \(M(P_A)\le2\) forces \(\delta<10\).
Suppose now that the parameters have a common coordinate denominator \(D\) in the original integral lattice and that \(s,s^{-1}\le S\).
Every nonzero parameter has norm at least \(1/D\), by positive integral squared norm after clearing \(D\).
Thus some cyclic adjacent pair has product of lengths less than \(10S\), and each length in that pair is less than \(10SD\).
For \(n=1\), the conclusion is directly \(s\|p_1\|^2<10\).

<a id="canonical-reductions"></a>
## Exact reductions of a rational canonical word

The scale has controlled positive rational height: if \(s=\alpha/\beta\) in lowest positive terms, track both \(\alpha,\beta\), not merely its denominator.
Also track common matrix denominators for \(R_0,R_0^{-1}\) and a common parameter denominator.
All these bounds will depend on the initial count only.

The exact cyclic conjugacy is
\[
B(p_n)A B(p_n)^{-1}
=R_0D_{1/s}B(sR_0^{-1}p_n)B(p_1)\cdots B(p_{n-1}).      \tag{2}
\]
This follows by moving \(R_0D_s\) through \(E_{p_n}J\).
It keeps \(R_0\) unchanged, inverts \(s\), and scales the moved vector by \(s\).
At most \(n\) moves put any chosen cyclic edge into positions two and three when \(n\ge3\).
Each moved vector passes the boundary at most once during these moves, so a pair of norm bound \(L\) acquires at most a factor \(\max(s,s^{-1})\).
All new coordinate denominators are controlled by those of \(s,R_0^{-1}\) and the old vectors.

If a parameter is zero and \(n\ge3\), move it to position two and use
\[
B(x)B(0)B(y)=B(x+y).                                   \tag{3}
\]
This decreases \(n\) by two and adds no positive correction.
The new sum may be zero and can be treated again.

For a nonzero short pair in positions two and three, write
\[
B(v)B(-w)B(u)B(-t)=E_vF_wE_uF_t,
\]
when \(n\ge4\), and put
\[
a=u^2/2,\ b=w^2/2,\ c=(u,w),\ \kappa=1-c+ab\ge0.
\]
The inequality follows from Cauchy--Schwarz without any integer assumption.

If \(\kappa>0\), use the exact real [C885 v6 decomposition](Yin_C_G0885_v6.md#middle-pair-decomposition),
\[
F_wE_u=E_rD_{1/\kappa}QF_q,\quad
r=(u-aw)/\kappa,\quad q=(w-bu)/\kappa.
\]
It gives
\[
R_0D_sB(v)B(-w)B(u)B(-t)
=R_0Q D_{s/\kappa}B(P)B(-T),                           \tag{4}
\]
where
\[
P=\kappa Q^{-1}(v+r),\qquad T=t+q.
\]
The untouched tail is identical on both sides.
Thus \(n\) decreases by two, and \(R_0\) gains one positive orthogonal correction of rank at most two.

If \(\kappa=0\), equality in Cauchy--Schwarz gives
\(ab=1\) and \(u=aw\).
Define the actual positive reflection
\[
S_wx=x-u(w,x).
\]
Then
\[
F_wE_u=E_{-u}D_aS_wJ.                                 \tag{5}
\]
To verify (5) on the whole space, both sides send \(f\) to \(-ae\), \(e\) to \(e+w-bf\), and a positive vector \(x\) to \(S_wx-(u,x)e\).
These vectors span the space, so (5) is a full matrix identity.
Consequently
\[
R_0D_sB(v)B(-w)B(u)B(-t)
=R_0S_wD_{sa}B(P_0),                                  \tag{6}
\]
where
\[
P_0=bv-w(w,v)+w-t.
\]
This decreases \(n\) by three and adds a rank-one positive orthogonal correction.
It remains in the canonical \(B\)-word form even when the parity changes.

For \(n=3\), write the word as \(R_0D_sE_vF_wE_uJ\).
If \(\kappa>0\), put \(R'=R_0Q,\ s'=s/\kappa\), and use the same \(P\) as above.
One obtains \(A=R'D_{s'}B(P)E_{-q}\).
The exact rational conjugacy
\[
E_{-q}AE_q
=R'D_{s'}B(P-s'^{-1}R'^{-1}q)                          \tag{7}
\]
reduces it to length one.
If \(\kappa=0\), instead
\[
A=R_0S_wD_{sa}E_{a^{-1}S_w(v-u)}.                      \tag{8}
\]
This is a triangular terminal, with full characteristic polynomial
\(\chi_{R_0S_w}(z)(z-sa)(z-(sa)^{-1})\).

<a id="terminal-cases"></a>
## Neutral terminals and bounded nonneutral terminals

A triangular terminal \(R_0D_sE_p\), \(R_0D_sF_p\), or \(R_0D_s\) has complete polynomial
\[
\chi_{R_0}(z)(z-s)(z-s^{-1}).
\]
When this is the preserved monic integer polynomial and \(s\) is positive rational, both \(s,s^{-1}\) are rational algebraic integers.
They are positive integers with product one, so \(s=1\).
Every remaining root has modulus one, and the output is neutral.
This also settles (8) with \(s\) replaced by \(sa\).
No claim that a remaining unipotent factor is conjugate to the identity is needed.

For \(n=1,p_1=0\), the polynomial is
\(\chi_{R_0}(z)(z^2-1)\), since \((D_sJ)^2=I\).
This case is neutral for every \(s>0\), without forcing \(s=1\).

For \(n=2\), a zero parameter gives one of the triangular terminals just settled.
With both parameters nonzero, (1) and the rational norm floor give
\[
\min(1,s)\|p_1\|\|p_2\|<10,\qquad
\|p_1\|,\|p_2\|<10D\max(1,s^{-1}).
\]
For \(n=1,p_1\ne0\), (1) gives
\(\|p_1\|^2<10/s\).
Hence every nonneutral terminal of measure at most two has at most two \(B\)-parameters with uniformly controlled norms once the current scale and denominator bounds are fixed.

<a id="uniform-rational-bookkeeping"></a>
## Why every bound depends only on the original count

Let \(\Lambda_{\mathrm{ev}}\) be the even-norm sublattice of the original positive integral lattice.
It is closed under integer combinations.
Initially all parameters lie in \(\Lambda_{\mathrm{ev}}\).
At any finite stage choose a common integer \(D\) with every parameter in \(D^{-1}\Lambda_{\mathrm{ev}}\), an integer \(M\) clearing \(R_0,R_0^{-1}\), and a bound for the reduced numerator and denominator of \(s\).
These bounds impose no restriction on the potentially large parameter numerators.

The weighted-cycle argument supplies a pair with norms bounded in terms of these bounds.
The at-most-\(n\) cyclic moves in (2) preserve such a bound after multiplying by controlled scales.
They also preserve an even-lattice denominator bound.
Indeed, for \(x\in\Lambda_{\mathrm{ev}}\), the integral vector \(M R_0^{-1}x\) has squared norm \(M^2x^2\), which is even.
Multiplication by a rational scale and finite addition merely change the common integer denominator.

Now suppose the selected pair \(u,w\in D^{-1}\Lambda_{\mathrm{ev}}\) has norms at most \(L\).
Write
\[
a=A_1/D^2,\quad b=B_1/D^2,\quad c=C_1/D^2,
\qquad
\kappa=N/D^4,
\]
where \(A_1,B_1,C_1,N\) are integers and
\[
N=D^4-C_1D^2+A_1B_1.
\]
For \(\kappa>0\),
\[
D^{-4}\le\kappa\le(1+L^2/2)^2,\qquad
1\le N\le D^4(1+L^2/2)^2.                              \tag{9}
\]
Thus a positive defect cannot become arbitrarily small at a stage with fixed denominator bound.

Put \(h=u-aw,\ j=(1-c)w+bu\).
The exact norms are
\[
\|r\|^2=2a/\kappa,\qquad
\|j/\kappa\|^2=\|q\|^2=2b/\kappa,
\]
so all three are at most \(L^2D^4\).
The positive correction has the rank-two expansion
\[
Q=I+r\otimes w^\flat-(j/\kappa)\otimes u^\flat,         \tag{10}
\]
with bounded correction vectors.
Here \(y^\flat(x)=(y,x)_H\).
Its adjoint gives the equally controlled \(Q^{-1}\).
Directly clearing the displayed fractions shows that both matrices have denominator dividing \(N\), and \(r,q,j/\kappa\in N^{-1}\Lambda_{\mathrm{ev}}\).

The exact cancellation
\[
P=\kappa v+w(h,v)-u(j,v)+(1-c)u+aw
\]
gives \(P\in D^{-5}\Lambda_{\mathrm{ev}}\).
Also \(T=t+q\in(DN)^{-1}\Lambda_{\mathrm{ev}}\).
Thus \(D^5N\) is a conservative common parameter denominator after (4), including the unchanged tail.
The new matrix denominator is at most \(MN\).
The scale becomes \(s/\kappa\), whose positive rational height is bounded using (9).

For \(\kappa=0\), the correction is
\(S_w=I-u\otimes w^\flat\), of matrix denominator dividing \(D^2\), with correction vectors of norms at most \(L\).
Formula (6) gives \(P_0\in D^{-3}\Lambda_{\mathrm{ev}}\).
Both \(a,b=a^{-1}\) have rational heights bounded by \(D,L\); thus the scale \(sa\) and matrix denominator \(MD^2\) are controlled.
The additional transformations in (7) use only the already controlled \(q,s'^{-1},R'^{-1}\), so their denominators are controlled too.

These formulas provide a finite recursive upper bound for the new parameter denominator, positive scale height, matrix denominators and every newly introduced correction-vector norm and denominator.
The bound depends only on the previous controls and on the count bound \(k\), not on rank, lattice determinant, the order of \(R\), or any unbounded parameter numerator.
Every reduction (3), (4), (6) or (7) strictly decreases \(n\), and at most \(k\) cyclic moves are used before each reduction.
Starting at \(s=D=M=1\), at most \(k\) reductions therefore give finite uniform bounds depending only on \(k\).
No claim of a bound uniform as \(k\to\infty\) is made.

Throughout,
\[
R_0=R\,Q_1\cdots Q_j,\qquad j\le k,                    \tag{11}
\]
where \(R\) is the original integral positive isometry and every \(Q_i-I\) has rank at most two with the controlled rational vector expansion just described.
Cyclic moves and zero combinations leave \(R_0\) unchanged.
This retains \(R\) as a separate finite-order factor even if \(R_0\) has infinite order.

<a id="rational-finite-rank-gap"></a>
## A gap for bounded rational finite-rank corrections

The required arithmetic lemma is the following.
Let \(A_0=R\oplus I_U\), with \(R\) an integral positive isometry of \(H\), and suppose
\[
A=A_0+\sum_{i=1}^{r}a_i(b_i,\cdot),
\]
where the vectors are rational, \(Da_i,Db_i\) are integral for a common integer \(D\), and their positive-part norms are at most \(B\).
Assume \(P_A\in\mathbb Z[z]\).
Then there is a positive gap depending only on \(r,B,D\).
Bounds on the sizes of the rational cusp coordinates are unnecessary for this lemma.
Neither integrality nor pairing preservation of \(A\) is required.

Let \(X\) have columns \(a_i\), and \(Y\) have rows \((b_i,\cdot)\).
The rectangular determinant identity gives
\[
P_A(z)=\Gamma(z)\det(I_r-Z(z)),\qquad
\Gamma(z)=\chi_R(z)(z-1)^2,\quad
Z=Y(zI-A_0)^{-1}X.                                    \tag{12}
\]
The identity follows by eliminating either diagonal identity block in
\(\left(\begin{smallmatrix}I&X\\Y&I\end{smallmatrix}\right)\), then factoring \(zI-A_0\).
It holds without any independence assumption on the columns.

Writing \(a_j=x_j+\alpha_je+\beta_jf\) and
\(b_i=y_i+\gamma_ie+\delta_if\), one has
\[
Z_{ij}(z)=(y_i,(zI-R)^{-1}x_j)_H+
\frac{\gamma_i\beta_j+\delta_i\alpha_j}{z-1}.             \tag{13}
\]
The finite-order integral \(R\) has some order \(N_0\).
The integer cyclic function
\[
F_{ij}(t)=D^2(y_i,R^t x_j)
\]
has normalized Fourier algebra norm at most \(D^2B^2\), by the orthogonal spectral-projection and Cauchy--Schwarz argument of [C885 v3](Yin_C_G0885_v3.md#argument).
Apply the accepted [Sanders theorem](../audits/literature/San20/Yin_U001.md#san20-u001) to obtain at most
\(L=L(\max(1,D^2B^2))\) signed subgroup-coset indicators for each function.

The actual resolvent has no extra \(R\).
For a residue \(t\equiv u\pmod d\), \(0\le u<d\), its series is
\[
\sum_{\substack{t\ge0\\t\equiv u\pmod d}}z^{-t-1}
=\frac{z^{d-u-1}}{z^d-1}.
\]
Thus each positive part of (13) is a rational signed sum of at most \(L\) such monomial/binomial fractions, with common scalar \(1/D^2\).
Choose \(\Delta\) as \(z-1\) times every denominator binomial occurring in every entry, including repetitions.
It has at most \(1+r^2L\) binomial factors, is monic integral, and has measure one.

Define
\[
U(z)=\det(\Delta I_r-\Delta Z)\in\mathbb Q[z].
\]
Then the exact polynomial identity is
\[
\Gamma U=\Delta^rP_A.                                 \tag{14}
\]
The right side is integral and \(\Gamma\) is monic integral.
Monic polynomial division over \(\mathbb Z\) gives an integral quotient and remainder.
Comparison with the rational polynomial equality (14) forces the remainder to vanish by degree, hence
\[
U\in\mathbb Z[z],\qquad U\ne0.
\]
No scalar denominator clearing is inserted in (14).

Each determinant entry has at most
\((L+2)2^{1+r^2L}\) terms, including the identity term and consolidated cusp term.
Hence
\[
\#\operatorname{supp}U
\le r!(L+2)^r\,2^{r(1+r^2L)}.
\]
Since \(M(\Gamma)=M(\Delta)=1\), the complete measure identity is
\(M(U)=M(P_A)\).
The accepted [DS17 fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) therefore proves the claimed gap.
The scalar \(D^2\) affects the support bound through Sanders but creates no Mahler cost.
Zero or dependent update vectors, zero correlations, repeated eigenvalues and denominators, singular \(A\) and every root multiplicity are covered by the same polynomial identity.
The case \(r=0\) is neutral directly; an empty positive part has only the rational cusp terms.
The two source statements retain their existing inspection depths, without a new audit of their original foundational proofs.

<a id="fixed-count-assembly"></a>
## Assembly for an arbitrary fixed original count

Start with a permitted original word of count at most \(k\).
Move its positive isometries to the left, combine same-cusp neighbors and remove zero parameters.
An odd alternating count at least three can be decreased by conjugating its last factor to the front and combining the two same-cusp factors.
Thus a nonneutral word has an integral conjugate in the initial canonical form
\[
R B(p_1)\cdots B(p_n),\qquad
n\le k\ \hbox{even},\quad p_i\in\Lambda_{\mathrm{ev}},
\]
with \(s=1\), and \(R\) the actual product of original positive integral isometries.
These are the retained exact [integer normalization identities](../ledger/Yin_L_G0462_v14.md#short-word-reduction).
An empty positive summand or a zero/one-transvection terminal is neutral.

Assume \(1<M(P_A)\le2\).
Apply (1)--(11) recursively.
Neutral terminals cannot occur under this assumption.
The process therefore ends with at most two bounded rational \(B\)-parameters, a bounded positive rational cusp scale, and at most \(k\) bounded rational positive corrections to the original \(R\).
All bounds depend only on \(k\).
The full polynomial is unchanged and remains monic integral, although the resulting matrix may be rational.

Use the auxiliary positive norm
\[
\|x+\alpha e+\beta f\|_+^2=\|x\|_H^2+\alpha^2+\beta^2.
\]
Every positive correction is an isometry for this norm.
The terminal \(D_s,J,E_p\) have operator norms bounded in terms of the terminal controls.
Their deviations from the identity have bounded rational vector expansions:
\[
D_s-I=(s-1)e\otimes f^\flat+(s^{-1}-1)f\otimes e^\flat,
\]
\[
J-I=-(e+f)\otimes(e+f)^\flat,
\]
\[
E_p-I=-e\otimes p^\flat+p\otimes e^\flat
-\tfrac12(p,p)e\otimes e^\flat.
\]
For these formulas the flat notation denotes the full \(H\oplus U\) pairing.
They have ranks bounded by two, one and three respectively, and their vector norms and denominators are controlled.

For a product \(K_1\cdots K_m\) of the bounded correction factors, use
\[
K_1\cdots K_m-I
=\sum_{j=1}^{m}K_1\cdots K_{j-1}(K_j-I).
\]
The transformed update vectors have controlled auxiliary norms and common coordinate denominators.
The number of factors is bounded by \(k+5\).
Multiplication on the left by \(R\oplus I_U\) preserves the auxiliary norms and integral denominators.
Hence the final matrix is
\[
A'=(R\oplus I_U)+\sum_{i=1}^{r_k}a_i(b_i,\cdot)
\]
with \(r_k,B_k,D_k\) bounded in terms of \(k\) alone.
For example the preceding decompositions permit the loose rank count \(r_k\le2k+10\).
This is the input to (12)--(14), with the original finite-order integral \(R\), not the possibly infinite-order \(R_0\).

The rational finite-rank lemma gives a positive lower bound for \(m(P_A)\) in this low-measure branch.
For \(M(P_A)>2\), use \(m(P_A)>\log2\).
Taking the smaller of the two constants proves \(\eta_k>0\).
This argument has no bound uniform in \(k\), and gives no effective exclusion of the entire interval \((1,6/5)\).

<a id="remaining-work"></a>
## Scope and the remaining growing-length construction

The theorem combines the weighted cyclic selection, every rational reduction and terminal, uniform recursive bookkeeping, the full determinant lemma and final assembly.
The six-factor controls remain useful because they identify the two invalid shortcuts that this proof avoids.

Any positive-to-one counterexample sequence within these two-cusp groups must have minimum permitted word length tending to infinity.
The remaining construction question concerns an actual growing-length integer family whose complete measure decreases, including all accumulated rational corrections and all roots.
A denominator growth calculation alone would not establish such a family or resolve G0001.

## Assessment history

### Decision fixed-transvection-count-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T05:46 |
| status | proved |
| reason | The complete independent review checks the weighted selection, every rational reduction and terminal, uniform recursive arithmetic controls, the exact integral finite-rank determinant and the final fixed-count assembly without a remaining gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform gap at every fixed count](#statement) | Every fixed bound on permitted transvection count, with unrestricted original positive integral lattice, rank, determinant, vector norms and positive-isometry orders, and the exact minimum-length sequence consequence. |
| argument | [Complete fixed-count argument](#argument) | All weighted-cycle, rational reduction, terminal, denominator, finite-rank arithmetic and assembly sections as one proof. |
| dependency | [Adopted cyclic theorem](Yin_C_G0885_v7.md#decision-cyclic-adjacent-short-pair) | The unchanged retained cyclic and five-factor results and their inherited scopes. |
| dependency | [Full boundary action](Yin_C_G0885_v5.md#boundary-action) | Null-vector normalization, reflection signs, inversion and every full-vector multiplier. |
| dependency | [Global contraction argument](Yin_C_G0885_v5.md#exterior-contraction) | Exact inversion distance, complete exterior domains and the summable-tail fixed-point argument. |
| dependency | [Real middle-pair decomposition](Yin_C_G0885_v6.md#middle-pair-decomposition) | Complete real positive-defect identity, orthogonality and the actual rational rank-two expansion. |
| dependency | [Finite-order Fourier input](Yin_C_G0885_v3.md#argument) | Finiteness of the original integral positive isometry group and the normalized spectral-projection estimate. |
| dependency | [Integer word normalization](../ledger/Yin_L_G0462_v14.md#short-word-reduction) | Addition, inverses, covariance, cusp exchange and exact integral conjugacies, with the arbitrary odd-length application checked in the new proof. |
| dependency | [Integral generator formulas](../ledger/Yin_L_G0462_v13.md#integer-generators) | Even-norm parameters and actual integral inverses on every original integral positive lattice. |
| dependency | [Accepted Sanders statement](../audits/literature/San20/Yin_U001.md#san20-u001) | Integer-valued finite cyclic correlations, normalized Fourier algebra norm and a signed-coset count depending only on that norm, at the retained statement-level inspection depth. |
| dependency | [Accepted fixed-support gap](../audits/literature/DS17/Yin_U001.md#ds17-u001) | The nonzero univariate integer polynomial U, complete logarithmic measure and uniform support bound, with unrestricted coefficient heights and exponents and unchanged foundational-proof limits. |
| review | [Complete independent fixed-count finding](../audits/reviews/Yin_R_G1114_v15.md#fixed-count-rational-normalization-gap-review) | Whole statement and proof, every rational and degenerate branch, all exact dependency interfaces, the coupled recursion and arithmetic lemma, and the original unrestricted-goal limitation. |

## Current assessment

[Selected decision](#decision-fixed-transvection-count-gap)
