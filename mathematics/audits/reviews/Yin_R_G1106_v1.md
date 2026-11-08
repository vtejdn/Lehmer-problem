---
author: Yin
---

# Review of limiting Chebyshev cuts and finite central determination

<a id="chebyshev-shell-review"></a>
## Whole-proof finding

At 2026-11-08T02:55 UTC a separately assigned agent for Yin independently inspected the [statement and proof of C881 v1](../../claims/Yin_C_G0881_v1.md#statement).
The reviewer took no part in the argument's development and received the fixed text without proof-generation dialogue, author explanations or a prior verdict on this Claim.
The whole argument supports its two conclusions under the stated Chebyshev grid, residue signs and left endpoint condition.

### From the shell to exact moments

Matching the same-sign gaps and the left endpoint interval to their right-hand poles leaves just two trace roots and one pole unmatched.
Each exceptional trace root has modulus at most \(5/2\) when \(M(P)\le2\), since the larger radius in its reciprocal lift is at most \(M(P)\).
The variation bounds for the first three Newton sums consequently bound \(a,\sum r_i,\sum b_i r_i\) and the positive mass \(\sum(b_i-c_d)r_i\) uniformly for either type of exceptional root.
The maximal trace mesh is at most \(2\pi/d\), so one can fix a subsequential separator limit and the angular midpoint gives the same limit.
The integral-limit argument supplies a further subsequence with cyclotomic rational \(F\) and constant term one.
I checked its bounded-characteristic and zero-free hypotheses against the [Cantor source unit](../literature/Can63/Yin_U001.md#cantor-rationality) and the reciprocal radius bound, respectively.
Cantor's theorem and the classical Kronecker theorem are used at statement level.

Clearing \(E(z)E(z^{-1})\) in the two conjugate expressions for \(R\) leaves antisymmetric integral Laurent numerators divisible by \(z-z^{-1}\).
The resulting symmetric quotients are integral polynomials in \(t\), and the leading coefficient of the common denominator is a unit because the cyclotomic \(E\) has constant term \(\pm1\).
With \(w=A^2\), eventual equality of each integral Taylor coefficient transfers to each fixed Laurent order at infinity by the branch \(z=t^{-1}+O(t^{-3})\).
The proper part of \(wR=wJ+zG\) has the moments of \(G\nu\), since \((G(t)-G(b))/(t-b)\) is polynomial and \(z\) is the semicircle Cauchy transform.
The discrete sine weights integrate fixed polynomials by sine orthogonality.
Applying both moment identities to \(h\) and \(th\) proves weak convergence of the positive measures to the stated angular density, including a cut at either endpoint.

### Resultant, saturation and rigidity

The derivative magnitude \(d/(2\sin^2\theta_i)\) and \(\prod_i\sin\theta_i=d/2^n\) give \(\prod_i|B'(b_i)|=(2d)^n/d^2\).
At the angular midpoint \(|B(c_d)|=1/\sin\theta_{\rm mid}\ge1\), and strict residues make \(|\operatorname{Res}(B,Q)|\) a positive integer.
Omitting the at most \(\deg A\) common roots subtracts at most \(O(\log d)\) from the lower bound for the log product, since each \(n\mu_i\) is \(O(d)\).
The resultant with \(B/\gcd(B,A)\) controls the remaining factors of \(A\).
The positive geometric-mean bound on \(n-O(1)\) nodes gives nonzero limiting mass even when \(A\) vanishes on grid nodes.

For \(Y_i=X_i/(f(\theta_i)+\epsilon)\), weak convergence bounds the limiting average of \(Y_i\) by one at every fixed \(\epsilon>0\).
Cauchy-Schwarz applied to \((Y_i-1)^2\le2\max(1,Y_i)(Y_i-1-\log Y_i)\) bounds the mean absolute deviation by the square root of the mean entropy defect times a bounded factor.
The nonzero trigonometric polynomial \(f\) has integrable logarithm and finitely many zeros, which justifies taking \(\epsilon\downarrow0\) after the degree limit.
For \(D_0\ne2\) the factor \(|1-sz^{2-D_0}|\) has zero logarithmic mean by the unit-circle root formula, as do the monic trace factors, including double circle roots at endpoint traces.
Real coefficients identify the two semicircle means.
The remaining factor \(\sin\theta\) gives exactly \(-\log2\), the equality value required for convergence in mean absolute deviation.

Replacing \(n\) by \(d\) and \(c_*\) by \(c_d\) in the density costs \(O(d^{-1}+|c_d-c_*|)\) in that norm.
The trace polynomials \(\xi_i^j+\xi_i^{-j}\) have integer coefficients in \(b_i\), and both \(w(b_i)r_i\) and \(G(b_i)\nu_i\) have integral moments by monic division.
The recurrence error for the integers \(h_j\) is at most \(2\sum_i |(b_i-c_d)e_i|<1\) for all \(j\) at once.
Starting with the exact \(h_0=h_1=0\) gives \(h_j=0\) for every \(j\), regardless of the arithmetic of \(c_d\).
Polynomial interpolation then gives equality of the two residue systems at every node.
The resulting variation bound for the one fixed nonzero integral \(w\) contradicts the [fixed-weight gap](../../claims/Yin_C_G0880_v2.md#statement) on the hypothesized positive shell.
I checked its hypotheses and used its [existing whole-proof review](Yin_R_G1105_v2.md#weighted-lift-review) for the gap itself.
The phase \(D_0=2,s=1\) gives zero density, so the only remaining phase has \(D_0=2,s=-1\).

### Competing poles, signs and the central prefix

Reversal in the remaining phase fixes \(F/(1-z^2)\), and its value one at \(z=0\) gives equal degrees and equal leading coefficients for the reduced trace quotient.
Its finite roots and poles are conjugacy-stable torsion traces, giving the stated monic integral normalization.
For any subsequential positive mass limit, division by \(w\) on compact sets avoiding its zeros identifies its density as \(-2(t-c_*)H(t)\,d\nu(t)\) there.
Positivity and bounded total mass force one-sided integrability even in the presence of atoms at the omitted points.
An interior pole away from the cut would give a nonintegrable singularity, and a pole at an interior cut has order at most one.
At an endpoint the local exponent is \(1/2-m\) for pole order \(m\), increasing by one at an endpoint cut, which gives the two endpoint order bounds.
The resulting total denominator degree is at most three for all cuts.
The finite list follows by the elementary symmetric coefficient bounds for roots in \([-2,2]\).

Conjugacy forbids an irrational interior pole, since a different conjugate would be a second interior pole and a rational endpoint cannot be its conjugate.
At an interior cut without a pole, a constant quotient cannot change sign.
If both endpoints are poles, both roots of the numerator lie strictly between them, so the quotient has the same sign near both endpoints.
For a linear numerator and denominator only \(D=t-2\), \(N=t-c_*\) have the required sign order.
Integrality therefore gives the three interior cut values, also accounting for an arbitrary paired subsequential coefficient and separator limit.

For a sequence of increasingly long central prefixes, \(a=-1,\sum r_i=0,\sum b_i r_i=1\) yield positive mass exactly one without using a Mahler bound.
The normalized limit has \(D_0=3\), \(g(t)=t\), \(A=1\), so the saturation and recurrence apply directly and give \(r_i=b_i\nu_i\) on the subsequence.
The polynomial part and these simple-pole residues determine \(Q\) uniquely.
The reference lift is \((1+z^2)(1-z^{2d-1})/(1-z)\) and has measure one.
Even \(d\) gives a zero central residue in this reference, incompatible with strict signs.
Failure of a single absolute \(L_0\) would yield a sequence \(d_j>L_j\to\infty\) with different \(Q_j\), contradicting exact recovery along its subsequence.
The finding gives a qualitative determination length and necessary conditions on a hypothetical shrinking shell.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#chebyshev-shell-review) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#chebyshev-shell-review) | [Statement](../../claims/Yin_C_G0881_v1.md#statement) | Paired subsequential limits, all cuts and both exceptional-root types, with a separate uniform central prefix assertion. |
| [Whole-proof finding](#chebyshev-shell-review) | [Weighted moments](../../claims/Yin_C_G0881_v1.md#moments) | Integral clearing, eventual fixed moments, quadrature and weak positive angular density. |
| [Whole-proof finding](#chebyshev-shell-review) | [Product and equality](../../claims/Yin_C_G0881_v1.md#saturation) | Nonzero mass with omitted nodes and passage from entropy equality to convergence in mean absolute deviation. |
| [Whole-proof finding](#chebyshev-shell-review) | [Integer recurrence](../../claims/Yin_C_G0881_v1.md#integer-recurrence) | All reversal cases, uniform recurrence, integer moments, exact recovery and fixed-weight contradiction. |
| [Whole-proof finding](#chebyshev-shell-review) | [Remaining rational functions](../../claims/Yin_C_G0881_v1.md#five-cuts) | Descent, finite degree, boundary integrability, conjugacy and signs. |
| [Whole-proof finding](#chebyshev-shell-review) | [Central determination](../../claims/Yin_C_G0881_v1.md#central-isolation) | Compactness and exact recovery for every Mahler measure, including the even-degree exclusion. |
| [Whole-proof finding](#chebyshev-shell-review) | [Three trace sums](../../ledger/Yin_L_G0462_v2.md#central-sign-test) | Matching and moment bounds used at any moving cut. |
| [Whole-proof finding](#chebyshev-shell-review) | [Compactness](../../ledger/Yin_L_G0464_v2.md#rational-prefix) | Locally uniform subsequences and applicability of the bounded-characteristic input. |
| [Whole-proof finding](#chebyshev-shell-review) | [Cyclotomic limit](../../ledger/Yin_L_G0464_v2.md#cyclotomic-prefix) | Integrality, zero-free limits and normalized cyclotomic quotients. |
| [Whole-proof finding](#chebyshev-shell-review) | [Resultant identity](../../ledger/Yin_L_G0464_v2.md#torsion-limits) | Exact derivative product and the angular-midpoint lower bound. |
| [Whole-proof finding](#chebyshev-shell-review) | [Fixed-weight gap](../../claims/Yin_C_G0880_v2.md#statement) | Applicability to the fixed weight selected on one positive shrinking subsequence. |
| [Whole-proof finding](#chebyshev-shell-review) | [Central comparison](../../ledger/Yin_L_G0464_v3.md#central-control) | The finite reference's residues, polynomial part, lift and parity. |
