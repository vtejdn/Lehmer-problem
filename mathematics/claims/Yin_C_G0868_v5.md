---
author: Yin
---

# Exact Schur realization price for rational matrix germs

Date: 2026-11-05.
This candidate identifies the complete determinant price of a rational matrix germ from its boundary singular values and its actual disk pole-cancellation multiplicities.
The price is not divided by matrix size.
The matrix_integer_return delegate developed the pole-module and polynomial-factor approximation proof and the two exact model prices.
The coordinating agent supplied the interior-circle Jensen argument, checked the construction and defined its original-input scope.
These are author-side contributions, not an independent review or an assessment of this version.

## Inputs and retained scope

[C868 v4](Yin_C_G0868_v4.md#statement) and its [selected integral-metric assessment](Yin_C_G0868_v4.md#decision-whole-integral-metric-review-2026-11-05) retain their exact arithmetic Gram, rank and determinant estimates.
Versions v1--v4 remain fixed at their own statements and selected scopes.
The only use of the v4 estimate below is the stated integral-germ consequence after the analytic price has been identified.

The existence input is the accepted [DR10 polynomial matrix Fejer--Riesz statement](../audits/literature/DR10/Yin_U002.md#dr10-u002): a nonnegative finite square matrix Laurent polynomial on the circle has a square analytic polynomial factor H with symbol H*H, and H may be chosen outer.
The accepted edition is the retained 33-page author survey, Theorem 2.1 and outer conventions on printed/PDF pages 4--7, at statement and finite-matrix applicability depth.
No full audit of its original operator proof is asserted.
[C F0008](Yin_C_F0008_v1.md#matrix-finite-gram-capacity), under its [selected assessment](Yin_C_F0008_v1.md#decision-adopted-retained-proof), already retains the finite-matrix bridge from that outer convention to disk invertibility and scalar polynomial Jensen.
That bridge is stated explicitly where needed below.
Its normalized capacity is not substituted for the total determinant price.
No general measurable spectral-factor theorem, Smirnov maximum principle or coefficient-field descent is needed for the infimum proof.

The underlying singular-value characteristic has established attribution.
Olavi Nevanlinna's [Growth of operator valued meromorphic functions](https://www.acadsci.fi/mathematica/Vol25/nevanli.pdf), Annales Academiae Scientiarum Fennicae Mathematica 25 (2000), 3--30, defines total logarithmic size in Definition 2.4, printed page 8, and the associated pole multiplicity and characteristic in Definitions 2.7 and 2.9 and Lemmas 2.8--2.9, printed pages 12--16.
Those passages were directly read from the journal PDF for this attribution, not adopted as the Schur-pair optimization theorem proved here.
The original 1996 matrix article cited there and the full operator-theoretic proof are not audited here.
No literature-priority claim is made.

[L133 v8](../ledger/Yin_L_G0133_v8.md#matrix-power-pullback-realization) retains the concrete integral model and its scalar-damping price 4m(P); its [same-P comparison](../ledger/Yin_L_G0133_v8.md#matrix-same-p-commutator) retains the actual price 12m(P).
The optimized prices below concern different matrix multipliers and do not invalidate either earlier construction.

## Statement

Let r>=1 and let F belong to M_r(C(z)), be holomorphic near zero and satisfy F(0)=I_r.
Here rational means rational as a function of z; coefficients may be arbitrary complex numbers.
Let D be the open unit disk and T its boundary with normalized Haar measure mu.
All logarithms are natural, all matrix norms are Euclidean operator norms and every determinant below is unnormalized.
The determinant of F is not identically zero.

An admissible pair consists of r-by-r functions Q and U holomorphic on D such that
\[
 \|Q(z)\|_{\rm op}\le1,\quad \|U(z)\|_{\rm op}\le1,
 \quad \det Q(0)\ne0,\quad U=FQ\ \hbox{near zero}.
 \tag{RP1}
\]
Set
\[
 \tau(Q)=-\log|\det Q(0)|,\qquad
 \tau_{\min}(F)=\inf_{(Q,U)\text{ admissible}}\tau(Q).
 \tag{RP2}
\]
No rationality, integrality or number-field condition is imposed on an admissible pair.

### The local multiplicity and the complete formula

At a finite point a, let O_a be the ring of holomorphic germs at a and define the pole-cancellation module
\[
 K_a(F)=\{v\in O_a^r:Fv\in O_a^r\},\qquad
 \delta_a(F)=\dim_{\mathbb C}(O_a^r/K_a(F)).
 \tag{RP3}
\]
This dimension is finite and is zero exactly when F has no pole at a.
Equivalently, if the local Smith--McMillan exponents of F are nu_1,...,nu_r, then
\[
 \delta_a(F)=\sum_{j=1}^r\max(0,-\nu_j).
 \tag{RP4}
\]
The proof below gives the local reduction and its equivalence to (RP3).
This is the sum of the negative partial orders, not the net pole order of det F.
In particular, det F identically one does not imply that every delta_a vanishes.

Write sigma_1,...,sigma_r for the singular values, counted with multiplicity, and put
\[
 J(F)=\int_{\mathbb T}\sum_{j=1}^r\log^+\sigma_j(F(\zeta))\,d\mu(\zeta),
 \qquad
 N(F)=\sum_{a\in\mathbb D}\delta_a(F)\log\frac1{|a|}.
 \tag{RP5}
\]
The sum is over the finitely many disk poles; none is zero because F is holomorphic there.
Boundary values at the finitely many boundary poles can be assigned arbitrarily in the integral.
Then J(F) and N(F) are finite and nonnegative, and
\[
 \boxed{\tau_{\min}(F)=J(F)+N(F).}
 \tag{RP6}
\]
The same infimum is obtained by restricting Q and U to rational functions in M_r(C(z)) that are holomorphic on a neighborhood of the closed disk.
Thus such pairs approach the displayed value arbitrarily closely.
General attainment, or attainment by rational functions, is not asserted in this part.
No rational-number or integer coefficient conclusion follows for those pairs.

### Attainment for a circle-unitary germ

If F is unitary almost everywhere on T, then J(F)=0 and there is a rational inner matrix B such that
\[
 Q=B,\qquad U=FB,\qquad
 \tau(Q)=N(F)=\tau_{\min}(F).
 \tag{RP7}
\]
Here inner means disk-holomorphic and unitary on T; the constructed B and FB are holomorphic on a neighborhood of the closed disk.
The determinant of B has a zero of exact order delta_a(F) at each disk pole a and no other disk zero.
All pole ranks and multiplicities are retained in this assertion.

### The two integral model prices

Let P(z)=z^2-3z+1, A(z)=z^2-z+1, a=A/P and b=2(1-z)/P, and define
\[
 T(z)=\begin{pmatrix}a&b\\zb&a\end{pmatrix},\qquad
 F_{\rm pull}(z)=T(z)T(z^2)^{-1}.
 \tag{RP8}
\]
For embeddings T_12,T_13 of T into the indicated coordinates of I_3, also define
\[
 F_{\rm same}=T_{12}T_{13}T_{12}^{-1}T_{13}^{-1}.
 \tag{RP9}
\]
Both germs have integer Taylor coefficients, constant coefficient I and are nonconstant and circle-unitary.
Their complete optimal prices are
\[
 \tau_{\min}(F_{\rm pull})=2m(P),\qquad
 \tau_{\min}(F_{\rm same})=4m(P),\qquad
 m(P)=\log\frac{3+\sqrt5}{2}.
 \tag{RP10}
\]
These minima are attained by rational inner matrix pairs as in (RP7).
The previously retained scalar copies give the valid larger prices 4m(P) and 12m(P), respectively.
Those are not minimum-price claims.

### Arithmetic consequence and original-input limit

If F additionally has integer Taylor coefficients and is nonconstant, let C_N be its first nonzero positive-index coefficient.
The v4 Euclidean specialization H=I gives, for every admissible pair and hence for its infimum,
\[
 J(F)+N(F)\ge\frac12\log\det\left(I_r+\frac14 C_N^*C_N\right)
              \ge\frac12\log\frac54.
 \tag{RP11}
\]
The formula identifies the full price of a supplied rational integer germ.
It does not construct such a germ for an arbitrary original positive-measure irreducible reciprocal P with J(F)+N(F)<=C_tr m(P) for an absolute C_tr.
No new unrestricted G0001 gap follows, and the [original contract](../tasks/Yin_T_G0001_v1.md#contract) remains unresolved.

## Argument

<a id="local-pole-cancellation-length"></a>
### 1. Local cancellation, determinant zeros and all multiplicities

Put t=z-a.
Choose k>=0 such that t^k F is holomorphic at a.
Then t^k O_a^r is contained in K_a(F), so the quotient in (RP3) is finite dimensional.
If its dimension is zero, each constant coordinate vector belongs to K_a, and every column of F is holomorphic; the converse is immediate.

For completeness, one obtains the local diagonal reduction using only valuation elimination.
Choose a nonzero entry of least t-order, permute it into the first position and divide its holomorphic unit factor out of its row.
The pivot is t^nu and the quotient of every entry in its row or column by that pivot is holomorphic.
Holomorphic elementary row and column operations therefore eliminate the remaining entries in that row and column.
Repeat on the remaining block.
Since det F is not identically zero, the process gives
\[
 F=L\,\operatorname{diag}(t^{\nu_1},\ldots,t^{\nu_r})\,R,
 \tag{1}
\]
where L,R and their inverses are holomorphic at a.
The exponents can be ordered nondecreasingly; equivalently their successive partial sums are the least orders of the nonzero minors of each size, since invertible holomorphic row and column operations preserve those orders.
Thus these exponents do not depend on the reduction choices.

Multiplication by R is an automorphism of O_a^r.
In its coordinates, K_a consists exactly of vectors whose j-th coordinate is divisible by t^(-nu_j) when nu_j<0, with no condition otherwise.
Its colength is therefore the sum in (RP4).
For any holomorphic matrix Q with FQ holomorphic, each column lies in K_a.
The negative-order rows of RQ have those divisibilities, and hence
\[
 \operatorname{ord}_a\det Q\ge\delta_a(F).
 \tag{2}
\]
This includes simultaneous local zeros and poles of F without canceling their separate contributions.
The net determinant order is sum_j nu_j and can be zero while (RP4) is positive.

The same elimination for a holomorphic full-rank square matrix M uses only nonnegative exponents and shows
\[
 \dim_{\mathbb C}(O_a^r/MO_a^r)=\operatorname{ord}_a\det M.
 \tag{3}
\]
These elementary local identities will also certify that the constructed denominator pays exactly the required multiplicities.

<a id="schur-price-necessary-bound"></a>
### 2. A pointwise determinant bound and interior-circle Jensen

Let (Q,U) be admissible and fix a circle of radius eta<1 avoiding the poles of F and the zeros of det Q and det F.
Such radii can be chosen tending to one: the rational exceptional sets are finite and the analytic zeros of det Q are discrete.
The germ identity U=FQ holds meromorphically throughout D by the identity theorem, with removable products at its poles.
At a regular point on this interior circle set V=QQ* and K=F*F.
The two contraction inequalities give
\[
 V\le I_r,\qquad FVF^*\le I_r,
 \quad\hbox{hence}\quad V\le K^{-1}.
\]
In a unitary eigenbasis of K, each diagonal entry of V is at most both one and the corresponding inverse eigenvalue of K.
Hadamard's determinant inequality yields
\[
 |\det Q|^2=\det V
      \le\prod_{j=1}^r\min(1,\sigma_j(F)^{-2}),
 \qquad
 -\log|\det Q|\ge\sum_{j=1}^r\log^+\sigma_j(F).
 \tag{4}
\]

Apply scalar Jensen to the holomorphic function det Q on that interior circle.
Its constant value is nonzero, and every disk pole a of F forces at least delta_a zeros by (2).
Consequently
\[
 \tau(Q)\ge
 \int_{\mathbb T}\sum_j\log^+\sigma_j(F(\eta\zeta))\,d\mu
 +\sum_{|a|<\eta}\delta_a(F)\log\frac{\eta}{|a|}.
 \tag{5}
\]
All extra zeros of det Q have nonnegative Jensen contributions and have only been discarded from this lower bound.
As eta increases to one along the permitted radii, the finite pole sum converges to N(F).
For almost every zeta on T, rational continuity gives convergence of the singular values of F(eta zeta) to those of F(zeta).
The integrands are nonnegative, so Fatou's lemma gives
\[
 \tau(Q)\ge J(F)+N(F).
 \tag{6}
\]
No boundary limit theorem for Q or U, or Smirnov hypothesis, was used.

The integral J(F) is finite: near any boundary pole, a common rational denominator bounds ||F(zeta)|| by a constant times a finite power of the inverse distance to that pole.
Thus sum_j log+ sigma_j(F)<=r log+||F|| has at worst a finite sum of integrable logarithmic singularities on T.
Elsewhere it is bounded.
This also explains why a boundary pole needs no separate positive disk Green weight in N(F); it remains in the actual boundary cost and must still be canceled in the upper construction.

<a id="minimal-pole-module-inner-factor"></a>
### 3. A polynomial cancellation module gives an exact inner denominator

Let A_D be the finite set of disk poles of F and choose k_a so that (z-a)^(k_a) F is holomorphic at each such a.
Define
\[
 d_0(z)=\prod_{a\in A_D}(z-a)^{k_a},\qquad
 \Lambda=\{v\in\mathbb C[z]^r:Fv\hbox{ is holomorphic at every }a\in A_D\}.
 \tag{7}
\]
For an empty pole set the product is one.
This is a C[z]-submodule containing d_0 C[z]^r.
It has a polynomial basis: project it to the first coordinate, whose nonzero image ideal has a generator p_1; choose a vector with first coordinate p_1, subtract its multiples, and repeat on the submodule with first coordinate zero.
Induction constructs r independent polynomial columns spanning Lambda, since at every step the residual submodule contains the corresponding d_0 coordinate vectors.
Write their matrix as M.

At a disk pole, the module generated by these columns over O_a is exactly K_a(F).
To see the nontrivial inclusion, take v in K_a and choose a polynomial vector having the same Taylor jet as v through order k_a-1 at a and zero jets through order k_b-1 at every other disk pole b.
Such simultaneous jets exist by the elementary Chinese remainder theorem for the pairwise coprime polynomials (z-b)^(k_b).
The chosen polynomial belongs to Lambda.
Its difference from v lies in (z-a)^(k_a) O_a^r, which is in M O_a^r because d_0 C[z]^r is in Lambda and d_0/(z-a)^(k_a) is a unit at a.
The reverse inclusion follows from the definition of Lambda.
Equation (3) therefore gives ord_a det M=delta_a(F).

There are no other zeros of det M.
Indeed, expressing each column of d_0 I_r in the polynomial basis gives a polynomial matrix K_0 with MK_0=d_0 I_r, so every zero of det M is a zero of d_0.
It follows that
\[
 \det M(z)=c\prod_{a\in A_D}(z-a)^{\delta_a(F)},\qquad c\ne0.
 \tag{8}
\]
In particular M is nonsingular on T and at zero.

Apply the accepted polynomial matrix Fejer--Riesz theorem to M* M on T and choose an outer polynomial H_0 with
\[
 M^*M=H_0^*H_0.
 \tag{9}
\]
Here and below a subscript zero on H_0 names this factor, not its constant coefficient.
Because det H_0 is not identically zero, the subspace in DR10's outer definition is all of C^r: a proper subspace would contain every value of H_0 and force its determinant to vanish.
The analytic multiplier by H_0 therefore has dense range in H^2(C^r).
Evaluation at any disk point is continuous and onto C^r, so H_0 cannot be singular there: a row annihilating its value would annihilate the values of that dense range.
On T it is nonsingular by (9).
This is exactly the finite-matrix outer bridge retained in C F0008.

Set
\[
 B=M H_0^{-1},\qquad G=FB.
 \tag{10}
\]
B is rational, holomorphic on a neighborhood of the closed disk and unitary on T by (9).
The scalar maximum principle on all fixed matrix coefficients w*Bv makes it a disk contraction.
G is rational and has no disk poles, since FM has none and H_0^(-1) is disk-holomorphic.
The disk zeros of det B are exactly those in (8), with the same multiplicities.

Scalar polynomial Jensen and disk invertibility of H_0 give
\[
 \log|\det H_0(0)|
   =\int_{\mathbb T}\log|\det H_0|\,d\mu
   =\int_{\mathbb T}\log|\det M|\,d\mu=\log|c|.
\]
Using (8), therefore,
\[
 -\log|\det B(0)|=N(F).
 \tag{11}
\]
Since B is unitary on T, the singular values of G=FB agree there with those of F, and J(G)=J(F).
This proves the exact pole price without identifying a nonminimal factor count or a scalar common-denominator degree with it.

<a id="boundary-majorant-schur-approximation"></a>
### 4. Polynomial majorants attain the infimum in the limit

Write the disk-holomorphic rational matrix G as N/d, where N is a polynomial matrix and d is a scalar polynomial with no zero in D.
A reduced common denominator has this property; zeros on T are allowed, and d(0) is nonzero.
On T define the continuous nonnegative Hermitian matrix
\[
 W=\max(|d|^2 I_r,N^*N).
 \tag{12}
\]
The maximum here is spectral: diagonalize N* N and replace each eigenvalue x by max(|d|^2,x).
It is well defined because one argument is scalar, and is continuous, for example from
\[
 W=\tfrac12\bigl(|d|^2 I_r+N^*N+|N^*N-|d|^2I_r|\bigr).
\]
It is at least both |d|^2 I_r and N* N and is positive definite away from the finitely many zeros of d on T.
There,
\[
 \log\det W=2r\log|d|+2\sum_j\log^+\sigma_j(G).
 \tag{13}
\]
In particular log det W is integrable: it is bounded above, while det W>=|d|^(2r) supplies an integrable lower logarithmic bound.

For every epsilon>0 choose a Hermitian Laurent polynomial V_epsilon with ||V_epsilon-W||op<=epsilon uniformly on T.
For instance, entrywise Fejer means converge uniformly for this continuous matrix field, and preserve Hermitian symmetry.
Put W_epsilon=V_epsilon+2epsilon I_r.
Then
\[
 W+\varepsilon I_r\le W_\varepsilon\le W+3\varepsilon I_r.
 \tag{14}
\]
The same accepted polynomial factorization gives an outer square polynomial H_epsilon with W_epsilon=H_epsilon* H_epsilon.
The preceding outer bridge and strict positivity on T imply that H_epsilon^(-1) is rational and holomorphic on a neighborhood of the closed disk.

Define
\[
 Q_\varepsilon=BdH_\varepsilon^{-1},\qquad
 U_\varepsilon=NH_\varepsilon^{-1}.
 \tag{15}
\]
These are rational and holomorphic on a neighborhood of the closed disk; their germ identity is U_epsilon=FQ_epsilon, and Q_epsilon(0) is invertible.
On T, unitarity of B and the two inequalities W_epsilon>=|d|^2 I_r,N* N give
\[
 Q_\varepsilon^*Q_\varepsilon\le I_r,
 \qquad U_\varepsilon^*U_\varepsilon\le I_r.
\]
The scalar maximum principle on w*Q_epsilon v and w*U_epsilon v for unit vectors v,w gives the disk contraction bounds.
The factors d in Q_epsilon cancel the possible boundary poles of G in the product; they have not been ignored through a boundary-only assertion.

Their exact determinant prices are
\[
 \tau(Q_\varepsilon)
 =N(F)+\frac12\int_{\mathbb T}\log\det W_\varepsilon\,d\mu
           -r\log|d(0)|.
 \tag{16}
\]
Polynomial Jensen justifies the H_epsilon term because its determinant has no disk zero.
As epsilon decreases to zero, (14) gives pointwise convergence of log det W_epsilon to log det W off the finite exceptional set.
For epsilon<=1 the integrands are uniformly bounded above, and are bounded below by 2r log|d|.
An integrable majorant for their absolute values follows from a constant plus 2r log^-|d|.
Dominated convergence therefore applies despite the allowed circle zeros of d.
Finally, scalar polynomial Jensen gives integral log|d|=log|d(0)|, since d has no disk zeros, including when some zeros lie on T.
Equations (13) and (16) imply
\[
 \tau(Q_\varepsilon)\longrightarrow N(F)+J(G)=N(F)+J(F).
 \tag{17}
\]
Together with (6), this proves (RP6) and the rational approximation assertion.
No quotient by r occurred at any point.

<a id="circle-unitary-exact-price"></a>
### 5. Circle unitarity gives rational attainment

Suppose F is unitary almost everywhere on T.
A reduced scalar entry cannot have a genuine circle pole, since it would be unbounded along a punctured circle arc, contradicting the almost-everywhere modulus bound one.
Thus F has no circle poles and J(F)=0.
The B in (10) already has exact price N(F), while G=FB is disk-holomorphic, has no circle poles and is unitary on T.
The same scalar maximum principle makes both B and G contractions.
Taking Q=B and U=G proves (RP7), including exact determinant-zero multiplicities and rational attainment.
No integer or rational-number coefficient assertion is made for B.

<a id="optimized-integral-model-prices"></a>
### 6. The two actual integral models

Use P,A,a,b,T from (RP8) and put lambda=(3+sqrt5)/2 and rho=lambda^(-1).
The directly retained identity A^2-4z(1-z)^2=P^2 gives det T=1 and
\[
 T^{-1}=\begin{pmatrix}a&-b\\-zb&a\end{pmatrix}.
 \tag{18}
\]
On T, reciprocity gives conjugate(a)=a and conjugate(b)=-zb, so T* equals (18).
Its Taylor coefficients and those of its inverse are integral since P(0)=1, and T(0)=I_2+2E_12.
The L133 v8 constructions therefore have all the properties in the statement; nonconstancy can also be seen from
\[
 F_{\rm pull}=I_2+z\begin{pmatrix}2&0\\2&-2\end{pmatrix}+O(z^2),
 \qquad (F_{\rm same})_{32}=-zb^2\ne0.
 \tag{19}
\]
For the second germ, the constant embedded shears I_3+2E_12 and I_3+2E_13 commute, so its constant coefficient is I_3.

At rho, T and T^(-1) have a genuine simple matrix pole.
Their numerator matrix there is nonzero, since A(rho)=2rho, and has rank one, since its determinant is P^2.
The two local exponents are therefore -1 and +1: the smallest is -1 and their sum is zero by determinant one.
Thus each such local pole has delta=1.

For F_pull the only disk poles are rho, sqrt(rho) and -sqrt(rho).
At rho the factor T(z^2)^(-1) is holomorphic and invertible because rho^2 is smaller than the smaller root of P.
At each of the other two points, T(z) is holomorphic and invertible because neither point is a root of P.
The substitution z to z^2 is locally unramified there, so the corresponding simple pole of T(z^2)^(-1) still has delta=1.
Multiplication by those invertible local factors preserves the exponents.
It follows that
\[
 N(F_{\rm pull})=\log\frac1\rho
       +2\log\frac1{\sqrt\rho}=2\log\lambda.
 \tag{20}
\]
Its boundary cost is zero and (RP7) gives the first optimum.

For F_same, every entry has common denominator P^4, so its only possible disk pole is rho, with entry orders at most four.
Direct multiplication gives
\[
 (F_{\rm same})_{11}=a^4-2azb^2.
 \tag{21}
\]
The first term has pole order four at rho, while the second has order at most three, so this is a genuine order-four pole.
Let J_23 be the constant permutation matrix interchanging coordinates two and three.
It interchanges T_12 and T_13 and hence satisfies
\[
 J_{23}F_{\rm same}J_{23}^{-1}=F_{\rm same}^{-1}.
 \tag{22}
\]
The local exponents are therefore invariant as a multiset under sign change.
There are three of them and the smallest is -4, so they are exactly -4,0,4.
Thus delta_rho(F_same)=4, N(F_same)=4log lambda and its boundary cost is zero.
Equation (RP7) proves the second optimum.

The [old rank-two scalar multiplier](../ledger/Yin_L_G0133_v8.md#matrix-power-pullback-realization) cancels all scalar denominator poles on both columns and pays 4m(P).
The [old rank-three scalar multiplier](../ledger/Yin_L_G0133_v8.md#matrix-same-p-commutator) repeats a fourth-order cancellation on all three columns and pays 12m(P).
The minima computed here use the actual module colengths, not those full scalar-copy multiplicities.
No correction to the fixed earlier price identities is needed.

<a id="exact-price-original-input-boundary"></a>
### 7. Arithmetic use and the unresolved original return

For a nonconstant integral germ, apply the adopted v4 determinant inequality with H=I to each admissible pair and pass to the infimum using (RP6).
This gives the first inequality in (RP11).
A nonzero integer C_N has a nonzero column of squared norm at least one, hence ||C_N||op>=1 and det(I+C_N* C_N/4)>=5/4, proving the final absolute bound.

The new price formula is an exact analytic test for a supplied rational germ.
It separates all boundary singular-value growth from every required disk pole multiplicity, including poles invisible in det F.
It gives neither an integral germ with cheap characteristic for each original P nor a bound of J(F)+N(F) by its total m(P).
Circle poles in a proposed original-input construction and field or metric changes retain their actual separate obligations; the formula does not remove those obstacles.
Both optimized examples still have m(P)=log lambda, and their power substitutions retain that same positive total measure.
Accordingly no positive-measure sequence approaching zero, new general original-input coverage or resolution of G0001 is asserted.

## Assessment history

### Decision whole-rational-price-review-2026-11-05

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:42 |
| status | proved |
| reason | Adopt the exact rational-matrix Schur price after the independent whole-proof finding R1091 v5. The total infimum is the boundary singular-value cost plus the complete disk pole-cancellation cost; rational approximation, circle-unitary attainment, both optimized integral models and the inherited arithmetic gap are included. No general original-input construction, literature-priority claim or unrestricted G0001 gap is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete rational price statement](#statement) | RP1-RP11 with arbitrary complex rational coefficients, all pole multiplicities, total unnormalized price, approximation and attainment distinctions, model prices and original-input limits. |
| argument | [Complete rational price proof](#argument) | All seven sections, including local cancellation modules, interior Jensen, exact inner denominators, polynomial majorants, limiting integrals and the arithmetic consequence. |
| dependency | [Polynomial matrix factorization](../audits/literature/DR10/Yin_U002.md#dr10-u002) | Accepted finite square polynomial Fejer--Riesz factorization and outer convention at the recorded statement/applicability depth; no new audit of its original operator proof. |
| dependency | [Finite-matrix outer bridge](Yin_C_F0008_v1.md#matrix-finite-gram-capacity) | Only the directly rechecked outer-to-disk-invertibility and scalar Jensen interface, also explicitly proved in v5; no normalized capacity is used. |
| dependency | [Integral-germ determinant estimate](Yin_C_G0868_v4.md#gram-loewner-determinant) | Only the adopted H=I specialization giving the complete first-coefficient determinant bound and the dimension-independent arithmetic floor. |
| support | [Earlier concrete constructions](../ledger/Yin_L_G0133_v8.md#matrix-power-pullback-realization) | Provenance of the two models and their valid scalar-copy prices; their mathematical identities and prices are independently reconstructed in v5 and R1091 v5, without extending the review to ledger history. |
| review | [Independent rational price whole-proof finding](../audits/reviews/Yin_R_G1091_v5.md#rational-price-whole-proof-finding) | Entire exact statement and seven-section argument, all model calculations, inherited mathematical interfaces, source applicability and unrestricted-goal limits; no substantive reviewer repair. |

## Current assessment

[Selected decision](#decision-whole-rational-price-review-2026-11-05)

