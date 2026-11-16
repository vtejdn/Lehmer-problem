---
author: Yin
---

# Integer prefix bounds for cyclotomic parents with a sign-changing neutral phase

<a id="statement"></a>
## Bounds independent of the conductor

Let \(A\) be a product of cyclotomic polynomials of orders at least three with any multiplicities, of degree \(2d\) with \(d\ge2\).
Write \(s=d-1\), take odd \(r>2d+1\), and set \(p=r+2s=2n+1,\ m=(r-1)/2\).
Let \(A(z)=z^d C_A(z+z^{-1})\), \(B_j(2\cos\theta)=\sin((2j+1)\theta/2)/\sin(\theta/2)\), and \(b_j=2\cos(2\pi j/p)\) for \(1\le j\le n\).
Put \(Q_0=C_A B_m,\ Q=Q_0+H\), where \(H\in\mathbb Z[t]\) is nonzero of degree at most \(n-2\).
If the residues \(Q(b_j)/B_n'(b_j)\) are strictly positive through some \(1\le c<n\) and strictly negative thereafter, the matching length \(L=n-\deg H\) satisfies
\[
             L<(4d+2)\big(2^{16(2d+5)}-1\big)+3.              \tag{1}
\]
Here \(P(z)=z^{n+1}Q(z+z^{-1})\) agrees with \(A(z)/(1-z)\) through coefficient index \(L\) and first differs at index \(L+1\).
The conclusion holds without a restriction on the first coefficients of \(A\), an endpoint inequality, or a height bound on \(H\).
In particular an arbitrarily long integral matching prefix in this construction requires unbounded parent degree, even if the perturbation degree is allowed to grow with the conductor.

There is a sharper structural form if on \(|z|=1\) one can write
\[
 |A(z)|=\prod_{i=1}^{k}|1-\sigma_i z^{a_i}|,\qquad
 |\sigma_i|=1,\ a_i\in\mathbb Z_{\ge1},
 \tag{2}
\]
with the multiset of pairs \((a_i,\sigma_i)\) stable under complex conjugation.
For \(R=k+4,\ D=2s+4+\sum_i a_i\), the bound is
\[
                      L<D(2^{16(R+1)}-1)+3.                   \tag{3}
\]
Thus a bounded number of such binomial factors gives a bound linear in their total exponent plus the parent degree.
For \(F_s=(1+z^2)^2(1-z^{2s})/(1-z^2)\) with \(s\ge2\), we also retain the [exceptional-parent bound](Yin_C_G0892_v1.md#statement) \(L\le Cs\) with an absolute \(C\), and its [three-factor estimate](../ledger/Yin_L_G0457_v10.md#explicit-bound) \(L<(2s+3)(20\,000\,000-1)+3\).
These sharper estimates use the nonnegative neutral phase on that family.
The main researcher obtained the general result by taking the absolute value of the signed neutral comparison and approximating the inverse square root of each binomial.

<a id="comparison"></a>
## A product for the absolute value of the signed comparison

The neutral lift is \(A(z)(1-z^r)/(1-z)\).
Since \(n+1<r\), the first term of \(z^{n+1}H(z+z^{-1})\) is precisely \(\operatorname{lc}(H)z^{n+1-\deg H}\), proving the prefix assertion.
Write \(\rho_j,\mu_j\) for the perturbed and neutral residues.
Take \(a=2\cos((2c+1)\pi/p)\) in the sign gap, let \(\mathbb E\) average over \(j=1,\ldots,n\), and set
\[
 X_j=p(b_j-a)\rho_j>0,\qquad G_j=p(b_j-a)\mu_j .
\]
By the [partial fraction moment identity](Yin_C_G0892_v1.md#moments), which concerns the difference \(H/B_n\), one has
\[
 \mathbb E X V=\mathbb E G V\quad (\deg V\le L-3),\qquad
 \mathbb E|X-G|\ge p/(2n)>1 \quad(L\ge3).                     \tag{4}
\]
For the inequality, use the monic polynomial \((t-a)T_{L-2}(t)\) with \(T_k(2\cos\theta)=2\cos(k\theta)\) against the residue difference.
Its moment equals \(\operatorname{lc}(H)\in\mathbb Z\setminus\{0\}\), while \(|T_{L-2}|\le2\).
Also \(\mathbb E\log X\ge0\) by the [grid product identity](Yin_C_G0892_v1.md#saturation).
It uses only the integral \(Q\) with nonzero pole values, the midpoint formula \(|B_n(a)|\ge1\), and \(\prod(4-b_j^2)=p,\ \prod|B_{n-1}(b_j)|=1\).

For \(t=2\cos\theta\), write \(E_{s-1}(t)=\sin(s\theta)/\sin\theta\).
The [grid derivative and phase formula](../ledger/Yin_L_G0457_v4.md#residue-formula) give \(p\mu_j=(4-b_j^2)C_A(b_j)E_{s-1}(b_j)\), with either sign allowed.
For \(a=2\cos\phi\), define the nonnegative function
\[
 f(t)=|(t-a)(4-t^2)C_A(t)E_{s-1}(t)|.
\]
Then \(f(b_j)=|G_j|\ge G_j\).
For \(z=e^{i\theta}\), the function is the product
\[
       f(t)=|1-e^{i\phi}z|\,|1-e^{-i\phi}z|\,
             |1-z^2|\,|1-z^{2s}|\,|A(z)|.
\]
This uses \(|C_A(t)|=|A(z)|\) and \(|1-z^2|=2|\sin\theta|\), with endpoint values by continuity.
With (2) there are \(R\) factors, of total exponent \(D\), with conjugate phases paired at equal exponents.
Every \(A\) in (1) satisfies (2) with \(2d\) factors of exponent one, by its full unit-circle root multiset.
Thus (3) implies (1).

<a id="filter"></a>
## A polynomial under the reciprocal of each binomial modulus

Put \(\eta=2^{-8(R+1)},\ \lambda=1-\eta,\ N=\eta^{-2}\), and \(\tau=\eta^2\).
For each factor \(f_i=|1-x|\) with \(x=\sigma z^e\), take
\[
 U(x)=\sum_{\ell=0}^{N-1}\binom{2\ell}{\ell}4^{-\ell}(\lambda x)^\ell,
 \qquad w_i=\frac{\sqrt\lambda\,|U(x)|^2}{(1+\tau)^2}.
\]
The infinite series equals \((1-\lambda x)^{-1/2}\), using the branch with value one at the origin.
Since every coefficient before \((\lambda x)^\ell\) is at most one, the tail is at most \(\lambda^N/\eta\).
Relative to the infinite sum its modulus is at most \(\sqrt2 e^{-1/\eta}/\eta\le\tau\).
The latter bound follows for \(0<\eta\le2^{-16}\) from \(e^v\ge v^4/24\) with \(v=1/\eta\).
In particular all \(w_i\) are positive.
Since \(|1-\lambda x|^2=\lambda|1-x|^2+\eta^2\) and \(|1-\lambda x|\le f_i+\eta\), we have
\[
 f_i\le 1/w_i\le
  \lambda^{-1/2}\left(\frac{1+\tau}{1-\tau}\right)^2(f_i+\eta)
 \le(1+3\eta)(f_i+\eta).
 \tag{5}
\]
For the last inequality use \(\lambda^{-1/2}\le1+\eta\) and \(((1+\tau)/(1-\tau))^2\le1+5\tau\) in this range.
Since \(0\le f_i\le2\), (5) gives \(0\le 1/w_i-f_i\le8\eta\).
The product \(w=\prod_i w_i\) is a real polynomial in \(t=z+z^{-1}\) of degree at most \(D(N-1)\), because its Laurent polynomial is unchanged by \(z\mapsto z^{-1}\) and conjugation on account of the phase pairing.
By telescoping the products,
\[
       f w\le1,\qquad 1/w\le 2^{R+1},\qquad
       0\le 1/w-f\le 8R\,2^R\eta.                             \tag{6}
\]
Indeed \((2+8\eta)^R\le2^R e^{4R\eta}<2^{R+1}\), and the sum of the \(R\) single-factor errors is bounded by \(8R\eta(2+8\eta)^{R-1}\le8R2^R\eta\).

<a id="determinant"></a>
## The finite grid logarithmic estimate

Assume \(L\ge D(N-1)+3\).
Now \(Y=Xw>0\) satisfies \(\mathbb EY=\mathbb E Gw\le1\) by (4) and (6).
For \(\psi(y)=y-1-\log y\), it follows that \(\mathbb E\psi(Y)\le-\mathbb E\log w\).
The relative tail bound gives
\[
 -\log w_i\le-\tfrac12\log\lambda+
            2\log\frac{1+\tau}{1-\tau}+\log|1-\lambda\sigma z^e|.
\]
On the full \(p\)-grid the sum of the final logarithm is at most \(e\log2\), because the \(p/\gcd(p,e)\) distinct powers each occur \(\gcd(p,e)\) times and the corresponding product has modulus at most \(2^{\gcd(p,e)}\).
At \(z=1\) the logarithm is at least \(\log\eta\).
The sum of these logarithms over all factors is even in angle, so deleting \(z=1\) and taking conjugate halves yields an upper bound \((D\log2+R\log(1/\eta))/(p-1)\) for its empirical average.
This argument does not require an individual nonreal phase to have even logarithm.
Since \(p-1\ge2L\), \(D\ge R\) and \(N=\eta^{-2}\), the last bound is at most \(\eta\), using \((\log2+\log(1/\eta))/(2(N-1))\le\eta\).
Also \(-\tfrac12\log\lambda+2\log((1+\tau)/(1-\tau))\le2\eta\).
Consequently \(\mathbb E\psi(Y)\le(2R+1)\eta\).

By \((y-1)^2\le2(1+y)\psi(y)\) and Cauchy-Schwarz,
\[
 \mathbb E|X-f|\le 2^{R+2}\sqrt{(2R+1)\eta}+8R2^R\eta<1/2.
\]
For example \(\sqrt{2R+1}\le2^R\) for \(R\ge1\) makes the first term at most \(2^{-2R-2}\), and \(R\le2^R\) makes the second term at most \(2^{-6R-5}\).
Since \(G\le f\) and \(\mathbb EX=\mathbb EG\) by (4), one has \(\mathbb E|f-G|=\mathbb E(f-X)\le\mathbb E|X-f|\).
Thus \(\mathbb E|X-G|<1\), contrary to (4).
This proves (3).

## Assessment history

### Decision signed-neutral-parent-draft

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:44 |
| status | open |
| reason | Retain the general signed comparison and finite-grid prefix bound for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [General prefix bound](#statement) | All cyclotomic parents of the stated degree, arbitrary multiplicities, and the more precise binomial bound. |
| argument | [Signed comparison](#comparison) | Integer first changed moment, grid product, and factorization of the absolute neutral comparison. |
| argument | [Binomial approximation](#filter) | Inverse square root series, conjugate symmetry and pointwise estimates. |
| argument | [Finite grid contradiction](#determinant) | Composite grid, phases, integer discrepancy and explicit constants. |
| dependency | [Matched moments](Yin_C_G0892_v1.md#moments) | Partial fractions of the integer correction. |
| dependency | [Full-grid product](Yin_C_G0892_v1.md#saturation) | Determinant at a strict cut and its angular midpoint. |
| dependency | [Neutral phase](../ledger/Yin_L_G0457_v4.md#residue-formula) | Neutral residues at the allowed grid and lengths. |


### Decision general-parent-prefix-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T08:50 |
| status | proved |
| reason | Adopt the conductor-independent bound for every parent in the construction together with the separately reviewed sharper bounds on the exceptional family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [General prefix bound](#statement) | All cyclotomic parents of the stated degree, arbitrary multiplicities, and the more precise binomial bound. |
| argument | [Signed comparison](#comparison) | Integer first changed moment, grid product, and factorization of the absolute neutral comparison. |
| argument | [Binomial approximation](#filter) | Inverse square root series, conjugate symmetry and pointwise estimates. |
| argument | [Finite grid contradiction](#determinant) | Composite grid, phases, integer discrepancy and explicit constants. |
| dependency | [Matched moments](Yin_C_G0892_v1.md#moments) | Partial fractions of the integer correction. |
| dependency | [Full-grid product](Yin_C_G0892_v1.md#saturation) | Determinant at a strict cut and its angular midpoint. |
| dependency | [Neutral phase](../ledger/Yin_L_G0457_v4.md#residue-formula) | Neutral residues at the allowed grid and lengths. |
| dependency | [Exceptional-parent statement](Yin_C_G0892_v1.md#statement) | The sharper uniform linear dependence on the exceptional parent parameter. |
| argument | [Exceptional-family saturation](Yin_C_G0892_v1.md#saturation) | Nonnegative neutral residues and logarithmic regularization. |
| argument | [Exceptional-family first discrepancy](Yin_C_G0892_v1.md#rigidity) | The uniform discrepancy contradiction at all integer heights. |
| dependency | [Explicit linear estimate](../ledger/Yin_L_G0457_v10.md#explicit-bound) | Reviewed numerical refinement on the exceptional subclass. |
| review | [Independent exceptional-family finding](../audits/reviews/Yin_R_G1107_v50.md#uniform-prefix-review) | The qualitative linear bound for all exceptional parents in the fixed v1 statement and its proof. |
| review | [Independent explicit-constant finding](../audits/reviews/Yin_R_G1107_v52.md#explicit-prefix-review) | The three-factor bound for those exceptional parents with the numerical degree and error estimates. |
| review | [Independent proof finding](../audits/reviews/Yin_R_G1107_v54.md#general-parent-prefix-review) | Both general bounds, the signed comparison, half-power series, composite grids, and the first changed integer moment. |

## Current assessment
[Selected decision](#decision-general-parent-prefix-reviewed)
