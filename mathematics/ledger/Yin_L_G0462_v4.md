---
author: Yin
---

# Quotients of nearby Salem numbers and the cost of their other conjugates

Agent-S derived and self-checked this test on 2026-11-08 for Yin's [unrestricted Lehmer objective](../tasks/Yin_T_G0001_v1.md#contract).
The [irreducible Salem progression](Yin_L_G0462_v3.md#minus-delay-progression) provides pairs of distinct positive real algebraic units whose ratio tends to one.
The proposed sampling rule chooses two such seeds and outputs the minimal polynomial of their quotient, allowing powers and a root-of-unity multiplier.
The obstruction below uses the fields of the two actual positive seeds.
The [off-pair argument for conjugates of one Salem number](../claims/Yin_C_G0165_v1.md#off-pair-salem-ratio-statement) concerns a different pairing, and the [fixed-seed radical argument](Yin_L_G0450_v1.md#unit-ray-saturation) bounds factors over a single base.
Throughout, \(M(\alpha)\) means the full multiplicative Mahler measure of the minimal polynomial over \(\mathbb Q\) and \(m(\alpha)=\log M(\alpha)\).

<a id="cross-field-fibers"></a>
## A bound from embeddings fixing one seed

Let \(\lambda,\mu>1\) be genuine Salem numbers in their positive real embeddings, let \(\xi\) be any root of unity, and let \(a,b\) be positive integers.
Put \(F=\mathbb Q(\lambda,\mu)\), \(e_\lambda=[F:\mathbb Q(\lambda)]\) and \(e_\mu=[F:\mathbb Q(\mu)]\).
For \(\gamma=\xi\lambda^a/\mu^b\) one has
\[
   m(\gamma)\ \ge\
    \max\{(e_\lambda-1)a\log\lambda,\ (e_\mu-1)b\log\mu\}.                 \tag{1}
\]
Among the \(e_\lambda\) distinct images \(\mu_i\) obtained by fixing \(\lambda\), exactly one is \(\mu\), and all the others have modulus at most one.
For each of these embeddings choose an extension to \(F(\xi)\).
The corresponding images \(\xi_i\lambda^a/\mu_i^b\) of \(\gamma\) are distinct.
Indeed equality would make \(\mu_i/\mu_j\) a root of unity, so their powers of some positive order would agree.
An embedding of the normal closure taking \(\mu_i\) to \(\mu\) would then take \(\mu_j\) to a conjugate of modulus \(\mu>1\).
Only \(\mu\) has this modulus, proving \(i=j\).
Thus the \(e_\lambda-1\) nonprincipal images each contribute at least \(a\log\lambda\) to the measure of the minimal polynomial, even if \(F(\xi)\) has larger degree than \(\mathbb Q(\gamma)\).
Interchanging the seeds and using \(m(\gamma^{-1})=m(\gamma)\) for the unit \(\gamma\) proves the second bound.
No disjointness of the fields or normal closures is assumed.

For any \(1<A<B\), consider all genuine Salem seeds in \([A,B]\).
If the two fields are different, at least one relative degree in (1) is at least two, so every such quotient has \(M(\gamma)\ge A\).
If the fields coincide in their positive real embeddings, the [common-field generator theorem used in C485](../claims/Yin_C_G0485_v1.md#salem-relative-regulator-identity) gives \(\lambda=\tau^i\), \(\mu=\tau^j\) for a common smallest Salem number \(\tau\) in the field and positive integers \(i,j\).
Then \(\gamma=\xi\tau^{ai-bj}\) has measure one when \(ai=bj\), and otherwise \(M(\gamma)\ge\tau\), using its displayed modulus or that of its inverse.
In particular a positive quotient measure below \(A\) already entails a Salem number of at most that measure.

Conversely, if genuine Salem numbers \(\tau\) approach one from above, then for all sufficiently small \(\tau-1\) both \(\tau^j,\tau^{j+1}\) lie in \([A,B]\) for \(j=\lceil\log A/\log\tau\rceil\), since \(A\tau^2<B\).
They are still Salem numbers: distinct conjugates of \(\tau\) have distinct positive powers by the same unique-exterior-conjugate argument, and all the nonreal conjugates remain on the circle.
Their ratio in decreasing order is \(\tau\).
Thus a law giving positive mass to every pair of such seeds and allowed powers and twists, whenever the sampling set is nonempty, has positive mass in every strict near-one shell exactly when Salem numbers themselves approach one.
This concerns an unrestricted supply of Salem seeds in the given interval, rather than a method for producing the required seed.
For a restricted law the obstruction (1) still applies to its entire support.

<a id="adjacent-ratios"></a>
## Exponential full-measure cost in the three-arm progression

Take \(f(z)=z^3-z-1\) and \(Q_N=(z^N f-f^*)/(z-1)\), with \(f^*(z)=z^3 f(1/z)\), on \(N\ge8,\ N\equiv8\bmod360\).
The [exterior-root calculation](../claims/Yin_C_G0578_v1.md#plastic-tree-all-root-cost) applies with its index \(n=N+1\).
It gives one simple expanding positive root \(\lambda_N\), its contracting reciprocal and all remaining roots on the unit circle, with \(\lambda_N\) strictly increasing to the real root of \(f\).
The [progression argument](Yin_L_G0462_v3.md#minus-delay-progression) excludes every cyclotomic factor on this congruence class by bounding each possible torsion order by divisibility into \(360\) and comparing at \(N=8\).
Together with the unique positive-measure factor of multiplicity one this gives irreducibility, and the actual degree of \(Q_N\) is \(N+2\).
In particular all the \(\lambda_N\) on this progression are distinct genuine Salem numbers, with smallest member the degree-ten Lehmer number \(\lambda_8\).

For two consecutive progression indices the degrees \(N+2\) and \(N+362\) have greatest common divisor \(10\).
The compositum degree over \(\mathbb Q\) is a multiple of both degrees, giving \(e_{\lambda_N}\ge (N+362)/10\).
Therefore
\[
  1<\frac{\lambda_{N+360}}{\lambda_N}\longrightarrow1,\qquad
  M\!\left(\frac{\lambda_{N+360}}{\lambda_N}\right)
     \ge \lambda_N^{(N+362)/10-1}\longrightarrow\infty .                  \tag{2}
\]
Already the first such pair has whole measure at least \(\lambda_8^{36}\).
Moreover any two different members of this progression have different field degrees, so every choice of powers and twists in (1) has full measure at least \(\lambda_8\).
If the same member is selected twice, the quotient is torsion or has house at least \(\lambda_8\) after possible inversion.
Every sampling law on this entire progression thus has zero probability in \(1<M<\lambda_8\), including laws biased towards pairs whose principal real values are close.

<a id="aligned-radical-test"></a>
## What degree alignment by radicals can change

Now take two distinct members \(\lambda,\mu\) of the [equal-degree radical construction](Yin_L_G0462_v3.md#same-degree-radicals).
Write their respective base degrees as \(D/h,D/k\), where \(h,k\) are the squarefree subset products there.
Their positive radicals \(\lambda^{1/h},\mu^{1/k}\) both have actual degree \(D\).
For the quotient \(\gamma=\xi\lambda^{1/h}/\mu^{1/k}\), put \(g=\gcd(h,k)\), \(l=\operatorname{lcm}(h,k)\) and \(r=[\mathbb Q(\gamma):\mathbb Q(\gamma^l)]\).
Then
\[
 m(\gamma)\ge r\max\{(1/g-1/h)\log\lambda,\ (1/g-1/k)\log\mu\}.           \tag{3}
\]
Indeed \(e_\lambda\ge h/g\) and \(e_\mu\ge k/g\) by the same least-common-multiple bound on the two base degrees.
Apply (1) to \(\gamma^l=\xi^l\lambda^{l/h}/\mu^{l/k}\).
Each conjugate of \(\gamma^l\) occurs exactly \(r\) times among the \(l\)-th powers of the conjugates of \(\gamma\).
Summing positive logarithms gives \(l\,m(\gamma)=r\,m(\gamma^l)\), yielding (3).

For two distinct subsets of the same cardinality each set difference is nonempty.
If \(P_0\) is the least available prime for this degree alignment, then \(h/g,k/g\ge P_0\).
The bound is at least \((r/g)(1-1/P_0)\log\lambda_8\).
Hence any sequence from this radical-ratio ensemble with strictly positive whole measures tending to one must have \(g\to\infty\) and \(r/g\to0\).
In particular disjoint subsets and bounded common parts cannot deliver arbitrarily small positive measures.
Large intersecting subsets could evade this estimate only with the indicated relative-degree loss on the quotient itself.
The equal degrees and known measures of the two input radicals supply neither that loss nor a positive near-one measure of their quotient.
