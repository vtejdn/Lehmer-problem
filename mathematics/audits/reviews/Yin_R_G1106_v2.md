---
author: Yin
---

# Review of the interior profiles and the explicit central prefix

<a id="finite-prefix-review"></a>
## Whole-proof finding

At 2026-11-08T03:02 UTC a separately assigned agent for Yin independently checked both assertions and the neutral examples in [C881 v2](../../claims/Yin_C_G0881_v2.md#statement).
The reviewer took no part in developing v2 and received its fixed mathematical inputs without proof-generation dialogue, author explanations or a prior verdict on v2.
For the shrinking-shell classification the reviewer checked the hypotheses and conclusion of [C881 v1](../../claims/Yin_C_G0881_v1.md#statement) and consulted its [existing independent finding](Yin_R_G1106_v1.md#chebyshev-shell-review).
The checks below support the complete v2 refinement under the strict two-block residue hypothesis and left endpoint inequality.

### Interior denominators and neutral examples

When the interior cut \(c\) is a pole, the density sign from v1 gives the reduced monic numerator the sign \((-1)^{a+1}\) away from its roots, with \(a\) the multiplicity of \(2\) in the denominator.
For denominator \(t-c\), a monic linear numerator must be negative throughout the open interval and can only be \(t-2\).
Adding just the pole \(-2\) would force a negative monic quadratic to have a root at each endpoint, violating coprimality.
Adding both endpoints would make all three zeros interior, with at least one of odd multiplicity.
Adding just \(2\) forces the nonnegative quadratic to have a double root, since \(2\) is excluded and each interior zero must have even multiplicity.
This root is rational from the linear coefficient and integral from monicity, so it belongs to \(\{-2,-1,0,1\}\setminus\{c\}\).
The no-pole case uses the reduced linear quotient from v1.

For the displayed neutral controls, the two geometric sums have total degree \(2d-2\), and the remaining quadratic has its roots on the unit circle for each permitted \(c\).
At each internal node \(\zeta\), the factors \(1-\zeta^{d-k}\) and \(1-\zeta^{d+k}\) are conjugate and \(\gcd(d-k,2d)=1\) makes their product positive.
The derivative of \(U_{d-1}(t/2)\) gives \(r_j=-\nu_jP(\zeta)\), so the sign is that of \(b_j-c\).
The odd degrees prime to three avoid all three possible interior cuts as grid nodes, and \(d\ge5\) supplies a node on either side.
At \(-1\) the lift takes value \(2+c\), giving \(Q(-2)/B(-2)=-(2+c)/d<0\).
At fixed \(k\) the coefficientwise limit is \((1-cz+z^2)/(1-z)^2=(t-c)/(t-2)\).
These witnesses have \(M(P)=1\) and establish no occurrence in a strictly positive shrinking shell.

### Uniform estimates and exact recovery

Multiplying the prefix by \((1-z^2)/(1-z^{2d})\) gives the signed semicircle moments through degree \(2045\) and \(a=-1\).
The quadrature localization only requires positivity of \((b_i-c_d)r_i\), so it applies to the angular midpoint as well.
For \(h=1023\), the signed test \((t-c_d)g^2\) has degree \(2043\), and its semicircle integrand after multiplication by \(t\) has degree \(2044\), within quadrature exactness through \(2045\).
This gives \(|c_d|\le 2\sin(\pi/1024)<7/1000\).
The midpoint resultant and \(n\log(1+1/n)\le1<2\log d\) give \(\mathbb E_d\log X_i\ge-\log 2\).

The finite Fourier expansion of \(2\operatorname{Re} S\) gives \(h_m\ge1/2\), even at \(e^{4i\theta}=1\).
The signed test \((b-c_d)h_m\) has degree at most \(2045\), and \((1-u)S=1-K\) and Fourier orthogonality give \(\mathbb E_dY_i=1+1/512\).
The scaled consecutive coefficient ratio for \(S(mu/(m-1))\) is \(m(m-j-1)/((m-1)(m-j))\le1\) for \(0\le j<m-1\).
Multiplying the scaled polynomial by \(1-u\) excludes zeros in the open unit disk, giving \(\lvert\beta\rvert^{-N}\le(1-1/m)^N\le e^{-8}\) for the original zeros.
Factoring \(S(u)=\prod_\beta(1-u/\beta)\) counts each zero with multiplicity and gives the full-grid factors \(1-\beta^{-N}\), including for even \(d\) when each grid root occurs twice.
Removing the node at \(u=1\) with index zero costs \(2\log((m+1)/2)/n\) in addition to the rescaled full-grid error.
With \(n\ge8191\) and \(N\ge4096\), the combined loss is at most \((8192/8191)\,1022/(2000\cdot4096)+12/8191=6511/4095500<1/600\).

The entropy bound is consequently \(1/512+1/600=139/38400<1/250\).
Cauchy–Schwarz with \(\mathbb E_d\max(1,Y_i)\le2+1/512\) gives \(\mathbb E_d|Y_i-1|<0.127\).
Distinct exponents of \(K\) are orthogonal modulo \(N\), and deleting its endpoint value of modulus one gives \(\mathbb E_d|1-h_m f|\le2/\sqrt{512}+1/512<0.091\).
Since \(h_m\ge1/2\), these bounds give \(\mathbb E_d|X_i-f(\theta_i)|<0.436\).
The moment identities \(\sum\nu_i=\sum b_i^2\nu_i=1\) and \(n/d=1-1/d\) then bound \(\sum|(b_i-c_d)(r_i-b_i\nu_i)|\) by \(0.436+2/8192+0.007<0.444\).

The residual trace moments are integral by monic polynomial division and the first two vanish by prefix agreement.
The uniform recurrence error is less than one, so induction and interpolation force \(r_i=b_i\nu_i\) at every node.
The polynomial part \(t+1\) recovers \(Q=t(B+U_{d-2}(t/2))\), whose lift is \((1+z^2)(1-z^{2d-1})/(1-z)\).
Thus the \(2048\) tested coefficients suffice for every \(d\ge8192\) without a bound on \(M(P)\).
At even \(d\) the recovered polynomial has a zero central residue, so the strict chamber has no input with that prefix.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#finite-prefix-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#finite-prefix-review) | [Statement](../../claims/Yin_C_G0881_v2.md#statement) | Interior coefficient limits in the strict shrinking shell and the uniform prefix implication for every degree at least 8192. |
| [Whole-proof finding](#finite-prefix-review) | [Interior list](../../claims/Yin_C_G0881_v2.md#interior-list) | All reduced denominator choices, possible numerator zeros, neutral examples, signs and limiting quotients. |
| [Whole-proof finding](#finite-prefix-review) | [Finite filter](../../claims/Yin_C_G0881_v2.md#finite-filter) | Degree of each moment test, positivity at the angular midpoint, filter identities and exact mean. |
| [Whole-proof finding](#finite-prefix-review) | [Finite product](../../claims/Yin_C_G0881_v2.md#finite-product) | Root annulus, full grid with multiplicities, omitted endpoint, entropy and uniform constants. |
| [Whole-proof finding](#finite-prefix-review) | [Exact recovery](../../claims/Yin_C_G0881_v2.md#finite-conclusion) | Weighted error below one half, exact recurrence, interpolation and recovery of the monic numerator. |
| [Whole-proof finding](#finite-prefix-review) | [Inherited theorem](../../claims/Yin_C_G0881_v1.md#statement) | Original hypotheses and the necessary limits used for the interior refinement. |
| [Whole-proof finding](#finite-prefix-review) | [Five cuts](../../claims/Yin_C_G0881_v1.md#five-cuts) | Denominator orders, density sign and no-pole quotient at an interior cut. |
| [Whole-proof finding](#finite-prefix-review) | [Product inequality](../../claims/Yin_C_G0881_v1.md#saturation) | Positive finite-grid resultant and scalar entropy inequality for positive numbers. |
| [Whole-proof finding](#finite-prefix-review) | [Integer recurrence](../../claims/Yin_C_G0881_v1.md#integer-recurrence) | Integrality, uniform-in-order error and induction from the first two moments. |
| [Whole-proof finding](#finite-prefix-review) | [Central control](../../ledger/Yin_L_G0464_v3.md#central-control) | Central residues, polynomial part, lift and Mahler measure. |
| [Whole-proof finding](#finite-prefix-review) | [Prefix moments](../../ledger/Yin_L_G0464_v3.md#fourth-root) | Finite coefficient-to-moment conversion for the prescribed signed measure. |
| [Whole-proof finding](#finite-prefix-review) | [Cut localization](../../ledger/Yin_L_G0464_v3.md#cut-localization) | Gauss nodes, polynomial degrees and positivity at any separator in the transition gap. |
