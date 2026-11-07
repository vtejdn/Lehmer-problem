---
author: Yin
---

# Independent review of eventual irreducibility in the odd-prime square family

A separately assigned reviewer for Yin examined the entire working-copy statement and four proof sections of C877 v1 at 2026-11-07T17:04 UTC.
The reviewer received the fixed proof and its source locations without participating in its development or receiving its development discussion.
The review used prior findings for unchanged premises, with their scopes identified below.
The final section reviewed here uses the unique binary endpoint block in C871.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole proof](#whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole proof](#whole-proof) | [Statement](../../claims/Yin_C_G0877_v1.md#statement) | Eventual rational irreducibility, a uniform positive logarithmic measure for all nonconstant monic integral divisors at every odd prime, and exclusion of sublinear factor degrees. |
| [Whole proof](#whole-proof) | [Factor inputs](../../claims/Yin_C_G0877_v1.md#factor-inputs) | Cleared specialization, Gaussian orbit, archimedean and dyadic products, discriminant, degree and uniform height bounds. |
| [Whole proof](#whole-proof) | [Poles](../../claims/Yin_C_G0877_v1.md#poles) | Cayley identity, exact Sturm count, exterior and interior pairing, and the unique root in the exterior disk. |
| [Whole proof](#whole-proof) | [Logarithmic test](../../claims/Yin_C_G0877_v1.md#singular-test) | Uniform circle-pole exclusion, cutoff regularity and energy, quantitative discrepancy, circle integral and localization. |
| [Whole proof](#whole-proof) | [Irreducibility](../../claims/Yin_C_G0877_v1.md#irreducibility) | Gaussian-component involution, unique reciprocal endpoint factor, both localized roots, squarefreeness and the gap including the finite exceptional set. |

<a id="whole-proof"></a>
## Finding on the complete statement and argument

The proof establishes the statement for the specified \(H_p\).
The [odd-prime identities](../../ledger/Yin_L_G0458_v4.md#prime-square-family-inputs) give coprimality, degree \(8p-6\), constant coefficient one and reciprocity.
Clearing the two cyclotomic quotient denominators gives \(D(A_p-iB_p)=U(z^{4p}+1)-iV(z^{2p}+1)^2\), including the factor \(D\).
Since \(U-V\) has even coefficients and \(U,V\) have disjoint root sets, \(a,b\) are Gaussian integral and have no common zero.
The equality \(i=A_p(\beta)/B_p(\beta)\) fixes the embedding of \(K\) and defines exactly one \(K\)-orbit in the rational orbit.
Complex conjugation pairs the remaining embeddings with those in this orbit.
In the norm of \(a(\beta)\), a paired embedding conjugates both the root and the coefficients of \(a\).
Consequently the absolute norm is the square of \(\prod_{g(z)=0}|a(z)|\), giving the factor \(1/e\) in (1).
The same pairing for \(\log^+|z|\) gives \(\log M(g)/n=h(\beta)\).
The monic minimal polynomial \(g\) has Gaussian integral coefficients by integral closedness, and separability makes its discriminant a nonzero Gaussian integer of modulus at least one.

I checked the [C873 height and dyadic arguments](../../claims/Yin_C_G0873_v1.md#argument) against their [previous whole-proof finding](Yin_R_G1098_v1.md#factor-heights).
The height estimates applied to \(t+t^{-1}\) give \((4p-5)h(\beta)\le\log C\) uniformly.
At odd primes a nonunit value of \(a\) would force a common residue zero of \(U,V\).
At two, the two embeddings reducing to the endpoint are conjugate locally, with \(v(\beta-1)=1/2\) from \(H_p(1)=2\).
They have \(v(V)=3/2\), \(v(U)\ge5/2\) and \(v(a)=1\), while every other dyadic embedding gives a unit.
This gives the [norm \(2^\delta\)](../../claims/Yin_C_G0873_v1.md#dyadic-identity) for \(\delta\in\{0,2\}\).
The [cyclotomic exclusion](../../ledger/Yin_L_G0458_v4.md#prime-square-no-cyclotomic-factors) covers every odd prime, including the pure dyadic possibilities and conductors \(2^kp\) with \(0\le k\le4\).
Thus the roots are nontorsion units, and Northcott finiteness with the uniform height bound forces the minimum degree to tend to infinity.
For large \(p\) the [Voutier bound](../literature/JT26/Yin_U001.md#external-inputs) gives \(e h(\beta)>1/(4\log^3(8p))\), hence \(n=e/2\gg p/\log^3(8p)\).
I checked the height normalization on p. 1 and the theorem on p. 3 of [Voutier's author version](https://arxiv.org/pdf/1211.3110).

Writing \(w=1-iu\), the four Cayley numerators for \(z-1,z+1,z^2+1,z^4+1\) are \(2iu,2,2(1-u^2),2(1-6u^2+u^4)\), with denominator \(w,w,w^2,w^4\), respectively.
Substitution gives \(4iS\) exactly, with \(a(-1)=-4(1+i)\) and \(S(-i)=-8(1+i)\).
Exact rational polynomial division gives negative remainders equal to the four displayed Sturm polynomials times \(2/25,\ 50/21,\ 4/169,\ 3062787/1261129\), respectively.
The signs at the two infinities are \((-,+,-,-,+,-)\) and \((+,+,+,-,-,-)\).
The constant last remainder establishes simplicity, and the Cayley map sends conjugate \(u\)'s to inverse complex conjugates.
Exactly one root contributes to the positive monic logarithmic measure \(m(a)\).
On the compact boundary of the exterior disk the perturbation of \(a\) is exponentially small in \(p\), and the divisor \(z^{4p}\) is nonvanishing in the disk.
The one simple zero of \(a\) therefore yields exactly one specialization zero there.

At a unit-circle zero \(\gamma\), the disk of radius \(1/p\) has \(z^{2p}\) and \(z^{-2p}\) uniformly bounded, while \(a(z)=O(1/p)\) and \(b(z)\) stays away from zero.
The equation \(b=a(z)(z^{2p}+z^{-2p})\) excludes every solution from these three disks.
The monic specialization has bounded coefficient one-norm, giving a single disk that contains all conjugates for all \(p\).
On a hypothetical sequence missing both off-circle neighborhoods each truncated test thus agrees with \(\log|a|\) at every selected conjugate.
Each circle cutoff has Lipschitz constant at most \(p\) and costs \(O(1+\log p)\) in planar Dirichlet integral by radial integration.
The exterior spatial cutoff contributes bounded energy because its gradient is supported a fixed positive distance from the five zeros.
I checked [Pritsker's Theorem 4.2, (4.16)](https://arxiv.org/pdf/1307.5734) on pp. 14-15 against the [accepted source unit](../literature/Pri11/Yin_U002.md#pri11-u002).
It applies to each real compactly supported Lipschitz test and each complex polynomial with simple zeros, with its modulus of continuity and Dirichlet integral evaluated separately.
With \(\epsilon=p^{-3}\) the modulus term is \(O(p^{-2})\).
The square of the remaining upper bound after dropping the nonpositive discriminant term is \(O((1+\log p)(p^{-1}+(\log p)/n+p^{-3}))=o(1)\).
On the unit circle the fixed off-circle cutoffs contribute exactly their logarithms.
At each unit-circle zero the logarithm is locally \(\log|\theta-\theta_0|+O(1)\), integrable and dominating the negative part of its truncations.
The circle means therefore tend to the positive \(m(a)\), whereas (1) bounds the absolute empirical mean by \(2\log(2)/e\).
This rules out every exceptional sequence, uniformly over the rational factors.

The map \(z\mapsto1/\bar z\) exchanges the disjoint disks \(B,B'\) and preserves \(A_p/B_p=i\) by equal degrees and opposite reversal signs.
Since every zero of \(D\) is on the circle, each disk contains exactly one selected root, counted with multiplicity.
The choice of \(\eta\) puts each localization neighborhood inside its respective disk.
I checked the endpoint and squarefreeness inputs in [C871](../../claims/Yin_C_G0871_v1.md#argument) and its [independent review](Yin_R_G1095_v1.md#integral-block-finding).
Every \(f\) has constant term a unit, so passage to the monic reciprocal associate permutes the irreducible factors and preserves vanishing of their binary reductions at one.
Uniqueness of the endpoint-bearing factor fixes it under that permutation.
Its roots are closed under inverse complex conjugation, so localization puts both of the two selected roots in this single factor.
Distinct rational irreducibles have disjoint root sets.
Squarefreeness excludes a power of the endpoint factor and the sole factor consequently has degree \(8p-6\).

For the large primes the [complete-measure bound](../../ledger/Yin_L_G0458_v4.md#prime-square-original-factor-cost) is bounded below by a positive constant (\(3\log(2)/8\) suffices for \(p\ge3\)).
Its norm argument retains all original embeddings and follows from integrality of \((\beta^{8p}-1)/2\).
For each exceptional prime the nonconstant monic divisors form a finite set, and every such divisor has positive measure by the cyclotomic exclusion and Kronecker's theorem.
Taking the minimum over this finite set when nonempty gives the claimed uniform gap together with the large-prime bound.
The review establishes neither a numerical irreducibility threshold nor any assertion for unrestricted integral polynomials.
The two external quantitative theorems were checked at statement and application scope without a reproof of their source proofs.
