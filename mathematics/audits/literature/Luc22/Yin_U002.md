---
author: Yin
---

<a id="luc22-u002"></a>
# Luc22-U002: Algebraic reduction, abelian specialization and geometric examples

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Luc22, [retained PDF](../../../literature/pdf/Luc22.pdf), arXiv:1901.00827v2, 16 September 2020.

Passages: Section 6, pp.10--11; Section 8, pp.15--19; Sections 10--13, pp.19--20. The unit uses the determinant conventions in U001 and distinguishes Section 7's separate approximation conjecture.

Inspection: 2026-10-06T06:51, human record author Yin. The assigned AI reviewer read the complete mathematical body and checked all in-paper proof mechanisms in this scope, including the iterated-limit order, rank preservation and determinant normalization. Rendered pp.11 and 17 were inspected. A separately assigned AI reviewer checked the late-section complex-coefficient interface and limit/constant implications, then shared findings; this is a targeted second check, not a second full-paper audit or human review.


## Assessment

**Audited within scope** for the arguments proving Theorem 8.4 and Theorem 10.1, with the complex-coefficient justification supplied below and the explicitly retained scalar Mahler approximation input.
Section 6's general Ore-localization theorems are stated external interfaces, not proofs furnished by Luc22.
Sections 11--13 describe an obstruction and a geometric upper bound, conditional on the identified outside structural and torsion formulas.
The sign and typing corrections below do not invalidate the abelian equalities.

All determinants and constants use [Luc22-U001](Yin_U001.md#luc22-u001), in particular the kernel-removed determinant and the unnormalized matrix trace.
No new project result is asserted beyond checking and explaining these source arguments.

<a id="luc22-ore-determinant-interface"></a>
## Ore localization and the weak determinant

Section 6 assumes $G$ amenable and $\mathbb QG$ a domain.
It cites torsionfree elementary amenable groups as examples.
With $S=\mathbb QG\setminus\{0\}$, the Ore localization $K=S^{-1}\mathbb QG$ is a skewfield.
For $A\in GL_r(K)$, choose a common nonzero left denominator $a$ with $A[a]=(aI_r)A\in M_r(\mathbb QG)$ and set

$$
\Delta([A])=
\frac{\det_{\mathcal N(G)}r_{A[a]}^{(2)}}
{\det_{\mathcal N(G)}r_{aI_r}^{(2)}}.
$$

The denominator includes all $r$ diagonal copies; it is not a single scalar determinant when $r>1$.
Determinants of injective rational matrices are positive and finite: after clearing an integer denominator, amenability gives the integral Determinant Conjecture, and rescaling a weak isomorphism multiplies its determinant by the corresponding scalar to power $r$.

The source imports well-definedness and the homomorphism property from [28, the discussion following (7.14)], with field $\mathbb Q$ and the trivial one-dimensional representation.
It also imports Lemma 6.4 from [28, Lemma 7.23]: for square $A$ over $\mathbb QG$, algebraic injectivity, injectivity/invertibility over $K$, and analytic injectivity/weak invertibility are equivalent, and

$$
\det_{\mathcal N(G)}r_A^{(2)}
=\Delta\!\left(\iota(\det_D A)\right).
$$

Here $\det_D:K_1(K)\to K^\times/[K^\times,K^\times]$ is the Dieudonné determinant isomorphism and $\iota$ its inverse represented by scalar matrices.
These precise source statements and their parameter match were read, but the original proofs in [28] and the cited Ore/domain theorems were not independently audited.
This unit does not promote that reported proof coverage.

The result gives a **quotient** of scalar determinants, not necessarily the determinant of an integral scalar.
Thus it does not prove $\Lambda^w(G)=\Lambda_1^w(G)$ for general amenable domains.
For abelian $G$, the ordinary commutative determinant supplies a scalar in the same ring.
In particular an integral matrix over $\mathbb Z[\mathbb Z^d]$ has an integral scalar determinant, which proves Lemma 6.7.

Example 6.5 takes $G=\mathbb Z\wr\mathbb Z$, with commuting $x_i$ and $y^{-1}x_i y=x_{i+1}$.
For $a=2-x_0$, the inverse $a^{-1}=\frac12\sum_{j\ge0}(x_0/2)^j$ exists in $\ell^1(G)$.
The distinct group elements in $y(1-x_1/2)\sum_{j\ge0}(x_0/2)^j$ cannot cancel to finite support, so $aya^{-1}\notin\mathbb QG$.
This checks the claimed failure of that particular representative to lie in the group ring.
The determinant class for the displayed matrix is $[-aya^{-1}]=[-y]$, so it in fact has the group-ring representative $-y$.
The source's following Remark 6.8 correctly says this example does **not** disprove existence of some group-ring representative in general.

<a id="luc22-abelian-matrix-approximation"></a>
## The precise abelian approximation

For $d\ge2$, substitution

$$
q(k_2,\ldots,k_d)(a_1,\ldots,a_d)
=a_1+\sum_{j=2}^d k_ja_j
$$

induces $A\mapsto A[k_2,\ldots,k_d]$, replacing $z_j$ by $z^{k_j}$ and $z_1$ by $z$.
The scalar Boyd--Lawton input, stated in Remark 8.1 and (8.2), is equality of Mahler measure with the **iterated** limit $\lim_{k_2\to\infty}\lim_{k_3\to\infty}\cdots\lim_{k_d\to\infty}$.
The $k_d$ limit is innermost.
It applies to complex Laurent polynomials; monomial factors do not affect either determinant.
The cited primary Boyd/Lawton proofs were not read here; their exact specialization as stated in Luc22 is the retained scalar input.

Theorem 8.4 extends this formula to every rectangular $A\in M_{r,s}(\mathbb C[\mathbb Z^d])$, including maps with kernels:

$$
\det_{\mathcal N(\mathbb Z^d)}r_A^{(2)}
=\lim_{k_2\to\infty}\cdots\lim_{k_d\to\infty}
\det_{\mathcal N(\mathbb Z)}r_{A[k_2,\ldots,k_d]}^{(2)}.
$$

It is not a claim about all paths of exponents escaping to infinity, nor about arbitrary finite quotients; it does not establish Conjecture 7.1 for $\mathbb Z^d$.
Complex coefficients here are compatible with the separate warning about arbitrary-quotient approximation in Remark 7.2.

The complete reduction in Lemma 8.3 and Theorem 8.4 was checked:

1. Over the fraction field of $\mathbb C[\mathbb Z^d]$, choose a basis of the kernel of right multiplication by $A$.
   Clearing a common denominator yields $B\in M_{q,r}(\mathbb C[\mathbb Z^d])$, with $BA=0$.
   Nonzero minors ensure the generic ranks agree with the fraction-field ranks.
   On the torus, exceptional polynomial zero sets have measure zero; hence $r_B$ is injective and its image is dense in $\ker r_A$.
   This explains the source's cited weak-exactness interface.
2. Put $D_1=B^*B+AA^*$ and $D_2=BB^*$.
   Kernel intersection for the positive sum and injectivity of $B$ show that both $D_i$ are injective.
   The decomposition into $\ker r_A$ and its orthogonal complement, or the stated Laplacian/torsion formula, gives
   $$\det r_A=\left(\frac{\det r_{D_1}}{\det r_{D_2}}\right)^{1/2}.$$
   On $\ker r_A$, the positive operator associated to $B^*B$ supplies the nonzero singular-value square factor of $B$; on the complement, the operator associated to $AA^*$ supplies that of $A$.
   The quotient removes the auxiliary $B$ factor, respecting the source's row-vector convention.
3. Each $\det_{\mathbb C[\mathbb Z^d]}D_i$ is a nonzero Laurent polynomial.
   Fourier transformation gives
   $$\log\det_{\mathcal N(\mathbb Z^d)}r_{D_i}
   =\int_{\mathbb T^d}\log|\det D_i(z)|\,d\mu.$$
   This is valid for complex coefficients: almost-everywhere invertibility follows from the nonzero determinant polynomial; its logarithm is integrable.
   The product of singular values equals $|\det D_i(z)|$, and boundedness bounds their positive logarithmic parts, so their negative parts are integrable too.
   This supplies the complex version not literally covered by Lemma 6.4's $\mathbb QG$ statement.
4. Let $b_j$ bound the absolute $j$th exponents in the supports of both scalar determinant polynomials and $c_i=2\sum_{j\le i}b_j$.
   Choosing $k_2>c_1$, $k_3>c_2k_2$, and so on separates their support exponents: the highest differing coordinate outweighs all earlier coordinates.
   Neither specialized determinant vanishes.
   A zero-rank auxiliary matrix uses the usual $0\times0$ determinant $1$.
5. Specialization commutes with involution and preserves $BA=0$.
   Invertibility of the two specialized Laplacians gives weak exactness after specialization, so the same quotient formula holds there.
   Apply scalar approximation to numerator and denominator.
   Their limits are positive finite Mahler measures, which justifies division, square roots and the successive limits.
   The case $A=0$ gives determinant $1$ throughout.

The source quotes the Hilbert-complex identities from [26, Lemmas 3.30 and 3.39].
Their exact role is identified above; their original proofs were not recursively inspected.
The Fourier calculation explicitly verifies the coefficient and normalization interface; Luc22 does not write out that argument.

## What Theorem 10.1 proves

For every integer $d\ge1$,

$$
\Lambda_1(\mathbb Z^d)=\Lambda_1^w(\mathbb Z^d)
=\Lambda^w(\mathbb Z^d)
=\Lambda_1(\mathbb Z)=\Lambda_1^w(\mathbb Z)=\Lambda^w(\mathbb Z),
\qquad
\Lambda(\mathbb Z^d)=\Lambda(\mathbb Z).
$$

Nonzero scalar Laurent polynomials are injective multipliers; the zero scalar has determinant $1$ and does not enter any candidate set.
Ordinary determinant reduces weak square matrices to scalar integral polynomials.
This checks the first equalities without losing integrality.
For the remaining comparisons, subgroup inclusion gives one inequality.
If a determinant in dimension $d$ is greater than $1$, successive scalar/matrix approximation produces values arbitrarily close to it and eventually greater than $1$.
Each such value is bounded below by the appropriate constant for $\mathbb Z$; the limit gives the reverse inequality.
This concerns infima and does not require attainment.

The theorem does **not** identify $\Lambda(\mathbb Z)$ with $\Lambda^w(\mathbb Z)$.
The source explicitly leaves even $\Lambda^w(\mathbb Z)>1\Rightarrow\Lambda(\mathbb Z)>1$ open.
No positivity of any of these nontrivial abelian constants is proved by Theorem 10.1.

## Free groups and hyperbolic examples

Section 11 reports the semifir and skewfield properties of free-group rings as cited external structure, not a general solution to Lehmer's problem.
Its concrete obstruction is verified: the tree chain boundary $\mathbb C[F_r]^r\to\mathbb C[F_r]$ with entries $s_i-1$ is algebraically injective because the universal-cover tree has no finite-support cycles.
On $\ell^2$, its kernel has von Neumann dimension $r-1$ for $r\ge2$: the adjoint kernel consists of invariant $\ell^2$ functions and is zero for infinite $F_r$, so the boundary has dense image and corrected dimension additivity gives the result.
Thus algebraic injectivity of rectangular maps does not replace analytic injectivity.
Problem 12.1 remains a question.

For a closed hyperbolic three-manifold $M$, Section 13 imports two external inputs: $-\rho^{(2)}(\widetilde M)=\operatorname{vol}(M)/(6\pi)$ ([26, Theorem 3.152]) and realization of $-\rho^{(2)}$ as the logarithm of the determinant of a weakly invertible square integral group-ring matrix ([25, proof of Theorem 2.4]).
If these inputs are supplied, positivity of volume makes that determinant an admissible value, and

$$
\Lambda^w(\pi_1M)\le \exp\bigl(\operatorname{vol}(M)/(6\pi)\bigr).
$$

The quoted Weeks-manifold volume in $(0.942,0.943)$ yields an upper bound less than $1.06$, hence less than Lehmer's number.
This disproves a universal equality to Lehmer's number for weak matrix constants of torsionfree groups; it does not show the weak scalar constant is smaller, or that the matrix constant equals $1$.
The volume/torsion realization and minimum-volume classification are reported cited inputs whose original proofs and optimality scope were not independently audited here; existence of the stated example and its volume bound, rather than uniqueness of a minimizer, are all this argument uses.

## Located corrections and limits

| ID and priority | Source | Correction and effect |
| --- | --- | --- |
| F07, P3 | Example 6.5, p.11 | The displayed $2\times2$ formula gives $-aya^{-1}$ for the displayed matrix, not $aya^{-1}$. Restore the minus sign. Infinite support and the warning about representatives remain valid. |
| F08, P2 | Lemma 8.3(3), p.17, and the use of Lemma 6.4 on p.18 | The referenced Lemma 6.4 is stated over $\mathbb QG$, whereas the current matrices are over $\mathbb C[\mathbb Z^d]$. The direct Fourier/determinant-polynomial argument above fills this coefficient-interface gap. Theorems 8.4 and 10.1 survive; the rational lemma alone does not cover the displayed hypotheses. |
| F09, P3 | Remark 8.1 and Theorem 8.4 proof, pp.15--18 | Use $\ell^2(\mathbb Z^d)$ for unspecialized scalar spaces and $\ell^2(\mathbb Z^d)^q$ for the auxiliary domain. In (8.7), the denominator's group is $\mathbb Z^d$, not $\mathbb Z$. The exponent-separation map is $q(k_2,k_3,\ldots,k_d)$, not the printed $q(k_1,k_3,\ldots,k_d)$. Determinants of specialized matrices are over $\mathbb C[\mathbb Z]$; unspecialized ones over $\mathbb C[\mathbb Z^d]$. These type corrections make the otherwise valid calculation well-formed. |

The entire in-paper proof of matrix approximation and its use in Theorem 10.1 was inspected.
The second-agent scope was the complex-coefficient bridge and the distinction between iterated specialization and general quotient approximation; it does not extend to all outside citations.
No stronger noncommutative determinant realization, general free-group lower bound, arbitrary-path Mahler limit, or formal proof is supplied by this audit.
