---
author: Yin
---

# A factorwise Mahler gap for the alternating rotating-shear family

This project deduction extends the [adopted alternating-family calculation in v1](../claims/Yin_C_G0888_v1.md#decision-fixed-periodic-symbol-growth) from the whole characteristic polynomial to each irreducible rational factor.
The [selected assessment](#decision-alternating-rational-factor-gap) adopts this extension after its [complete independent review](../audits/reviews/Yin_R_G1107_v39.md#alternating-factor-gap-review).
The selected decision and review of v1 remain at their original scope; they are not transferred to this extension.
Only this explicit alternating family is considered.

<a id="statement"></a>
## Standalone factorwise statement

Let \(g\ge6\) be even, index sites by \(\mathbb Z/g\mathbb Z\), and let \(Se_i=e_{i+1}\).
Set
\[
 D=\sum_{i=0}^{g-1}(-1)^i(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T},\qquad
 E=\sum_{i=0}^{g-1}(-1)^i(e_i+e_{i+1})(e_i+e_{i+1})^{\mathsf T},
\]
\[
 A_g=\operatorname{diag}(S,S)
 \begin{pmatrix}I&D\\0&I\end{pmatrix}
 \begin{pmatrix}I&0\\E&I\end{pmatrix},\qquad
 P_g(z)=\det(zI_{2g}-A_g).
\]
For a monic polynomial \(f\), write
\[
 m(f)=\sum_{f(\alpha)=0}\log\max\{1,|\alpha|\},\qquad M(f)=e^{m(f)},
\]
with all roots counted with their algebraic multiplicities.
If \(f\in\mathbb Q[z]\) is a nonconstant monic irreducible factor of \(P_g\), then \(f\in\mathbb Z[z]\), \(f(0)=\pm1\), and exactly one of the following holds:

- \(f=z-1\) or \(f=z+1\), and \(M(f)=1\).
- \(f\) is noncyclotomic and
  \[
  \boxed{\quad M(f)\ge\frac{1+\sqrt5}{2}>\frac65.\quad}   \tag{1}
  \]

Consequently every monic rational divisor of \(P_g\) with measure greater than one obeys (1), whether irreducible or reducible.
This statement includes proper factors, independently of how large the total measure of \(P_g\) is.
It is not a factorwise theorem for arbitrary fixed Laurent symbols, other rotating-shear sign assignments, or the different cluster families of C889.
No optimality of the constant in (1) is asserted.

<a id="dependencies"></a>
## Exact existing inputs

The [alternating identities of v1](../claims/Yin_C_G0888_v1.md#alternating-identities), equations (10)--(13), supply the actual integral symplectic model and its squared-product identity.
The [two-site symbol and full Fourier factorization](../claims/Yin_C_G0888_v1.md#alternating-fixed-symbol), equations (17)--(19), supply every fiber, with all algebraic multiplicities.
Their concrete complex-fiber form is checked below rather than inferring an arithmetic statement from whole-polynomial growth.
The [complete spectrum in v1](../claims/Yin_C_G0888_v1.md#alternating-complete-spectrum) also retains that \(1\) and \(-1\) each occur twice in the whole polynomial.
No general periodic-growth assertion or asymptotic estimate is used to prove (1).

The only additional external arithmetic input is [Bel17-U001](../audits/literature/Bel17/Yin_U001.md#bel17-u001), at its accepted statement that
\(\Phi_N\) is the monic irreducible integral product of all primitive \(N\)-th roots and has degree \(\varphi(N)\).
The unit identifies Bell's 12 April 2017 author notes, pages 3 and 6--7; irreducibility is accepted there as a standard statement, without an audit of its original proof.
No discriminant, integral-basis or value-at-one assertion from that unit is needed here, and no new original-source reading or acquisition is claimed.
The embedding-extension argument, primitive-root sum and elementary totient case distinction used below are included explicitly.
There is no computational or numerical input.

<a id="positive-fiber"></a>
## Positive fibers and recovery of their phase

Put \(q=g/2\), and use the exact two-site symbol from v1:
\[
 S_2(x)=\begin{pmatrix}0&x\\1&0\end{pmatrix},\qquad
 D_2(x)=\begin{pmatrix}0&x-1\\x^{-1}-1&0\end{pmatrix},
\]
\[
 \mathcal A(x)=\operatorname{diag}(S_2(x),S_2(x))
 \begin{pmatrix}I_2-D_2(x)^2&D_2(x)\\-D_2(x)&I_2\end{pmatrix},
\]
\[
 P_g(z)=\prod_{\zeta^q=1}p_\zeta(z),\qquad
 p_\zeta(z)=\det(zI_4-\mathcal A(\zeta)).                    \tag{2}
\]
The coefficients of \(p_\zeta\) belong to \(\mathbb Q(\zeta)\).
For \(|\zeta|=1\), abbreviate \(D_2(\zeta)\) by \(D_\zeta\), and put
\[
 u=1-\operatorname{Re}\zeta\in[0,2],\qquad
 R_\zeta=\operatorname{diag}(S_2(\zeta),S_2(\zeta)),\qquad
 B_\zeta=\begin{pmatrix}I_2-D_\zeta^2&D_\zeta\\-D_\zeta&I_2\end{pmatrix}.
\]
Here \(D_\zeta\) is Hermitian, \(D_\zeta^2=2uI_2\), and \(S_2(\zeta)\) is unitary with square \(\zeta I_2\).
Direct multiplication also gives \(S_2(\zeta)D_\zeta S_2(\zeta)^{-1}=-D_\zeta\).
Since the sign-reversed shear product is \(B_\zeta^*\), these identities give
\[
 \mathcal A(\zeta)^2=\zeta B_\zeta^*B_\zeta.              \tag{3}
\]
The matrix \(B_\zeta\) is invertible, so \(B_\zeta^*B_\zeta\) is positive definite.

Diagonalizing the Hermitian matrix \(D_\zeta\) in the two coordinate blocks reduces this positive matrix to the two matrices
\[
 K(d)=\begin{pmatrix}1-d^2+d^4&-d^3\\-d^3&1+d^2\end{pmatrix},
 \qquad d=\sqrt{2u},\ -\sqrt{2u}.
\]
Each has determinant one and trace \(2+4u^2\).
Thus their positive eigenvalues are
\[
 \mu_\pm=(\sqrt{1+u^2}\pm u)^2,
 \qquad \log\mu_\pm=\pm2\operatorname{arsinh}u,
\]
where \(\operatorname{arsinh}u=\log(u+\sqrt{1+u^2})\).
If \(\alpha\) is any root of \(p_\zeta\), then (3) gives
\[
 \alpha^2=\zeta\mu\quad\text{for some }\mu\in\{\mu_+,\mu_-\},\qquad
 \boxed{\left|\log|\alpha|\right|=\operatorname{arsinh}(1-\operatorname{Re}\zeta).}  \tag{4}
\]
In particular \(\alpha\ne0\), \(|\alpha|^2=\mu\), and
\[
 \boxed{\quad \frac{\alpha}{\overline\alpha}
       =\frac{\alpha^2}{|\alpha|^2}=\zeta.\quad}          \tag{5}
\]
Consequently the same complex number cannot be a root of two distinct fibers in (2).
No choice of an argument or square-root branch is involved in (5).

The degenerate case \(u=0\) occurs precisely at \(\zeta=1\).
Then \(D_\zeta=0\), \(B_\zeta=I_4\), and \(\mathcal A(1)\) is the direct sum of two copies of \(S_2(1)\).
Therefore
\[
 p_1(z)=(z-1)^2(z+1)^2.                                   \tag{6}
\]
For every other fiber \(u>0\), so (4) excludes every unit-circle root.
Thus a rational irreducible factor with a unit-circle root is exactly \(z-1\) or \(z+1\).

<a id="distinct-conjugates"></a>
## Extending embeddings and counting distinct conjugates

Let \(f\) be an irreducible factor other than the two in (6), choose a root \(\alpha\), and choose its fiber parameter \(\zeta\) in (2).
By (5) this parameter is unique and has some order \(N>1\) dividing \(q\).
Put \(K=\mathbb Q(\zeta)\), \(L=K(\alpha)\).
The accepted irreducibility of \(\Phi_N\) gives, for every residue \(a\) coprime to \(N\), an embedding
\[
 \sigma_a:K\longrightarrow\mathbb C,\qquad \sigma_a(\zeta)=\zeta^a.
\]
Indeed \(K\simeq\mathbb Q[X]/(\Phi_N)\), and evaluation at any primitive root defines that embedding.

Each \(\sigma_a\) extends to an embedding \(\tau_a:L\to\mathbb C\).
To see this directly, let \(r(X)\) be the minimal polynomial of \(\alpha\) over \(K\), apply \(\sigma_a\) to its coefficients, and choose a complex root of the resulting polynomial.
Irreducibility is preserved under the coefficient-field isomorphism, so evaluation at that root gives the required injective map from \(K[X]/(r)\).
Write \(\beta_a=\tau_a(\alpha)\).
Because \(f\) has rational coefficients, \(f(\beta_a)=0\).
Applying \(\tau_a\) to the determinant equation \(p_\zeta(\alpha)=0\) gives
\[
 p_{\zeta^a}(\beta_a)=0.                                  \tag{7}
\]
Now apply the positive-fiber argument (3)--(5) afresh to this actual complex fiber, obtaining
\[
 \frac{\beta_a}{\overline{\beta_a}}=\zeta^a,\qquad
 \left|\log|\beta_a|\right|
 =\operatorname{arsinh}(1-\operatorname{Re}\zeta^a).        \tag{8}
\]
If \(\beta_a=\beta_b\), the first equality in (8) forces \(\zeta^a=\zeta^b\).
Thus the chosen values give \(\varphi(N)\) distinct conjugates of \(\alpha\), all roots of \(f\).
In particular \(\deg f\ge\varphi(N)\).

The proof never applies \(\tau_a\) to (5) and never assumes \(\tau_a(\overline\alpha)=\overline{\tau_a(\alpha)}\).
It also does not require \(\zeta\in\mathbb Q(\alpha)\), normality of that field, or reciprocity of \(f\).
Only the explicitly constructed compositum \(L\) is used.

<a id="unit-cost"></a>
## Integer units and the absolute-log budget

By the reused integral symplectic normalization, \(P_g\) is monic integral with constant one.
Its monic rational factors are integral.
For completeness, clear the denominators of a monic rational factor \(f\) and its monic complementary factor \(h\) to write \(F=rf\) and \(H=sh\), with primitive integral \(F,H\) and positive integer leading coefficients \(r,s\).
Their product is primitive: modulo any prime the two nonzero polynomials have a nonzero product.
But \(FH=rsP_g\) has content \(rs\), so \(r=s=1\).
Their integer constant terms multiply to one, proving \(f(0)=\pm1\).

The roots \(\gamma_1,\ldots,\gamma_d\) of the irreducible \(f\) are distinct in characteristic zero, and their absolute product is one.
Therefore
\[
 \sum_{j=1}^d\log|\gamma_j|=0,\qquad
 2m(f)=\sum_{j=1}^d\left|\log|\gamma_j|\right|.            \tag{9}
\]
Using just the distinct conjugates from (8) gives the precise fiber-order bound
\[
 \boxed{\quad
 m(f)\ge\frac12\sum_{\substack{1\le a\le N\\(a,N)=1}}
 \operatorname{arsinh}\left(1-\cos\frac{2\pi a}{N}\right).
 \quad}                                                     \tag{10}
\]
Here \(\{\zeta^a:(a,N)=1\}\) is the full set of primitive \(N\)-th roots, so replacing the chosen primitive generator by \(e^{2\pi i/N}\) merely permutes the summands.
All omitted terms in (9) are nonnegative, so this does not assume that the selected conjugates exhaust \(f\).
No squarefreeness of the entire \(P_g\) is needed.
If an irreducible factor occurs with a higher multiplicity in a divisor, its full measure is raised to that multiplicity, rather than being counted only once.

<a id="primitive-sum"></a>
## The elementary primitive-root sum

Define \(\mu(N)=0\) if a prime square divides \(N\), and otherwise let \(\mu(N)=(-1)^r\) for the number \(r\) of distinct prime divisors, with \(\mu(1)=1\).
The finite product \(\prod_{p\mid n}(1-1)\) proves
\(\sum_{d\mid n}\mu(d)=0\) for \(n>1\), and the sum is one for \(n=1\).
For a primitive \(N\)-th root \(\zeta\), the coprimality indicator and the geometric sum then give
\[
 \begin{aligned}
 \sum_{\substack{1\le a\le N\\(a,N)=1}}\zeta^a
 &=\sum_{d\mid N}\mu(d)\sum_{b=1}^{N/d}\zeta^{db}\\
 &=\mu(N).
 \end{aligned}                                             \tag{11}
\]
In the second line, the inner sum is zero unless \(d=N\), when it is one.
Taking real parts proves
\[
 \sum_{\substack{1\le a\le N\\(a,N)=1}}
 \left(1-\cos\frac{2\pi a}{N}\right)=\varphi(N)-\mu(N).
\]
The second derivative of \(\operatorname{arsinh}u\) is \(-u/(1+u^2)^{3/2}\le0\), so its graph on \([0,2]\) lies above the chord from zero to two:
\[
 \operatorname{arsinh}u\ge\frac u2\operatorname{arsinh}2.
\]
Combining this with (10) gives
\[
 m(f)\ge\frac{\operatorname{arsinh}2}{4}
             (\varphi(N)-\mu(N)).                          \tag{12}
\]

<a id="uniform-factor-gap"></a>
## The uniform golden-ratio bound

For \(N>1\), \(\varphi(N)-\mu(N)\) is a positive integer, as is already clear from the displayed sum of \(1-\cos(2\pi a/N)\) above.
For \(N=2\) it equals two.
For \(N>2\), pairing an invertible residue \(a\) with \(-a\) shows that \(\varphi(N)\) is even.
Thus \(\varphi(N)-\mu(N)=1\) can occur only if \(\varphi(N)=2\) and \(\mu(N)=1\).

Inclusion-exclusion of the residue classes divisible by each prime gives
\[
 \varphi(N)=\prod_{p^r\parallel N}p^{r-1}(p-1).
\]
If this value is two, every prime divisor is two or three, the exponent of three is at most one, and the exponent of two is at most two.
If three divides \(N\), the exponent of two is at most one.
The cases with totient two are exactly \(N=3,4,6\), of which only six has \(\mu(N)=1\).
Therefore every \(N>1\) other than six has \(\varphi(N)-\mu(N)\ge2\), and (12) gives
\[
 m(f)\ge\tfrac12\operatorname{arsinh}2,
 \qquad M(f)\ge\sqrt{2+\sqrt5}.                            \tag{13}
\]
For \(N=6\), the two primitive roots have real part \(1/2\), so the exact bound (10) gives
\[
 m(f)\ge\operatorname{arsinh}(1/2)
 =\log\frac{1+\sqrt5}{2}.                                 \tag{14}
\]
Since \((1+\sqrt5)^2/4=(3+\sqrt5)/2<2+\sqrt5\), (13) is strictly larger than the bound in (14).
This proves the uniform constant (1); it exceeds \(6/5\), for example because \(\sqrt5>2\) makes the golden ratio greater than \(3/2\).

Finally factor any monic rational divisor of \(P_g\) into its monic irreducible factors with multiplicity.
The only irreducible factors of measure one are \(z-1\) and \(z+1\), by (4)--(6).
If the divisor has positive logarithmic measure, at least one irreducible factor obeys (1), and multiplication of the full root products proves the stated divisor conclusion.

<a id="scope"></a>
## Scope of the factorwise conclusion

The complete-polynomial growth theorem in v1 remains unchanged, and its general fixed-symbol scope is not enlarged to arbitrary irreducible factors.
The new arithmetic step depends on the particular alternating fiber identity (3), its positivity, and the unique phase recovery (5).
These properties are not asserted for an arbitrary Laurent symbol or for the nonperiodic cluster words in C889.
Neither an embedding-commutation assumption nor a bound on a selected exterior root is substituted for the complete sum (9).
The result rules out obtaining a positive measure below the golden ratio by taking any rational polynomial factor of this alternating family.
It leaves other sign patterns, other symbols and the unrestricted G0001 objective unresolved.

## Assessment history

### Decision alternating-rational-factor-gap

| Field | Value |
| --- | --- |
| date | 2026-11-10T10:49 |
| status | proved |
| reason | Complete independent review verifies a uniform golden-ratio lower bound for every positive-measure monic rational divisor of the explicit alternating family, including proper factors and all lengths. The proof uses exact positive fibers, distinct cyclotomic embeddings and the complete absolute-log budget of an integer unit; no factor gap for arbitrary symbols or other shear patterns is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete factorwise statement](#statement) | Every even g at least six, all monic rational irreducible factors and divisors, both neutral linear factors, full multiplicities and the uniform golden-ratio bound. |
| argument | [Positive fibers and phase recovery](#positive-fiber) | Full Fourier product, exact adjoint-product order, all fiber eigenvalues, unique phase and the degenerate phase-one factor. |
| argument | [Distinct conjugates](#distinct-conjugates) | Every primitive embedding extended to the compositum, determinant transfer and fresh phase recovery without commuting embeddings with complex conjugation. |
| argument | [Integer units and complete cost](#unit-cost) | Integral monic factors, constant terms plus or minus one, all conjugates, exact absolute-log identity and every factor multiplicity. |
| argument | [Primitive-root sum](#primitive-sum) | Mobius identity, finite root sums, concavity and every normalization factor. |
| argument | [Uniform factor gap](#uniform-factor-gap) | All root orders, the order-six exception, exact constant comparisons and reducible divisor conclusion. |
| argument | [Scope](#scope) | Explicit alternating family only, with general symbols, other signs and cluster factors remaining outside the assertion. |
| dependency | [Adopted v1 model](../claims/Yin_C_G0888_v1.md#decision-fixed-periodic-symbol-growth) | The selected integral alternating model, exact identities, unit-root multiplicities and complete two-site Fourier factorization, not the general asymptotic growth estimate. |
| dependency | [Alternating identities](../claims/Yin_C_G0888_v1.md#alternating-identities) | Actual integer symplectic normalization and squared-product identities. |
| dependency | [Complete alternating spectrum](../claims/Yin_C_G0888_v1.md#alternating-complete-spectrum) | The exact unit roots and their complete multiplicities. |
| dependency | [Two-site symbol](../claims/Yin_C_G0888_v1.md#alternating-fixed-symbol) | Exact Laurent entries, shift convention and every characteristic fiber. |
| dependency | [Cyclotomic input](../audits/literature/Bel17/Yin_U001.md#bel17-u001) | Only the accepted monic integral irreducible polynomial of all primitive N-th roots with degree phi(N); its original irreducibility proof is not newly audited. |
| review | [Complete independent finding](../audits/reviews/Yin_R_G1107_v39.md#alternating-factor-gap-review) | Entire fixed contribution, all original model and source interfaces, every small order and multiplicity, and all stated limits. |

## Current assessment

[Selected decision](#decision-alternating-rational-factor-gap)

