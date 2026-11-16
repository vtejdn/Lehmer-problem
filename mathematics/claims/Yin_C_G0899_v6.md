---
author: Yin
---

# The prime-order Mahler rate below the degree for Salem numbers from fixed Pisot seeds

<a id="statement"></a>
## One sublinear prime order for every sign and seed in a finite list

Let \(\mathcal F\) be a nonempty finite set of monic minimal polynomials \(f\) of Pisot numbers \(\theta_f>1\) with \(f\) not proportional to \(f^*(z)=z^{\deg f}f(1/z)\).
For each sign \(\sigma=\pm1\) and every sufficiently large delay \(N\), write \(P_{f,\sigma,N}\) for the Salem minimal polynomial dividing \(z^N f-\sigma f^*\).
Its unique exterior root tends to \(\theta_f\), and \(d_{f,\sigma,N}=\deg P_{f,\sigma,N}=N+O_f(1)\).
Write \(T_P\) for its integral trace polynomial and \(S_p\) for the minimal polynomial of \(2\cos(2\pi/p)\) for an odd prime \(p\).
Use the positive integers
\[
   G_p(P)=\max_{a\in\mathbb Z}\gcd(T_P(a),S_p(a)),\qquad
   B_p(P)=|\operatorname{Res}(T_P,S_p)|.
\]
There are odd primes \(p_N\to\infty\) with \(p_N/\min_{f,\sigma} d_{f,\sigma,N}\to0\) for which
\[
 \max_{f,\sigma}\left|\frac{\log G_{p_N}(P_{f,\sigma,N})}{p_N-1}
               -\tfrac12\log\theta_f\right|\longrightarrow0,\qquad
 \max_{f,\sigma}\left|\frac{\log B_{p_N}(P_{f,\sigma,N})}{p_N-1}
               -\tfrac12\log\theta_f\right|\longrightarrow0 .
\]
The single prime at each delay serves every seed and both signs in this list.
The comparison value may equivalently be half the logarithmic Mahler measure of the varying Salem polynomial itself, since its exterior root tends to \(\theta_f\).
In fact a single prime sequence \(p_N\to\infty,\ p_N=o(N)\) works pointwise for every fixed eligible seed and both signs, with the onset allowed to depend on the seed.

<a id="transfer"></a>
## Keeping the trace ideal when the delay is shortened

Fix a seed and a sign and write \(H_N=z^N f-\sigma f^*\).
The [circle-root and torsion calculation](../ledger/Yin_L_G0462_v27.md#fixed-seed-return) gives one simple positive exterior root converging to \(\theta_f\), its inverse inside the disk, and a cofactor \(C_N\) of cyclotomic factors with uniformly bounded orders and eventually simple roots.
In particular \(H_N=P_N C_N\) for large \(N\) with reciprocal \(P_N\) irreducible and of degree \(N+O_f(1)\).
These facts hold also for degree-one and nonunit Pisot seeds.
The [cofactor calculation](../ledger/Yin_L_G0462_v111.md#cofactor) gives a common multiplicity \(e\) of \(z-1\) for all sufficiently large delays at a fixed sign, either zero or one.
The other cyclotomic factors take unit values at a primitive \(p\)-th root \(\zeta\) when \(p\) exceeds every torsion order: for \(1<m<p\), the Möbius product for \(\Phi_m(\zeta)\) has absolute norm \(p^{\sum_{j\mid m}\mu(m/j)}=1\).

For large delays \(N,a\) and such a prime \(p\mid N-a\), we have \(H_N(\zeta)=H_a(\zeta)\).
Cancel the common \((\zeta-1)^e\) and the remaining units to see that \(P_N(\zeta)\) and \(P_a(\zeta)\) are associates in \(\mathbb Z[\zeta]\).
Their trace values at \(t=\zeta+\zeta^{-1}\) differ by an additional power of \(\zeta\).
The ratio of trace values and its inverse are real units in \(\mathbb Z[\zeta]\) and therefore belong to \(\mathbb Z[t]\), by the [real-order argument](../ledger/Yin_L_G0462_v111.md#ideals).
It follows that \((T_{P_N},S_p)=(T_{P_a},S_p)\) in \(\mathbb Z[X]\).
Evaluation at any integer preserves equality of the two ideals, so \(G_p(P_N)=G_p(P_a)\); norms also give \(B_p(P_N)=B_p(P_a)\).

<a id="selection"></a>
## A growing prime that is sublinear in every original degree

Fix \(k\ge1\).
For each residue class \(\rho\bmod k\) fix two sufficiently large short delays \(a_\rho,a_\rho+k\) in this class so the preceding facts hold for the whole finite list, \(a_\rho\ge9\max_f\deg f\), and all their exterior roots have logarithms within \(1/k\) of the respective \(\log\theta_f\).
For \(N\equiv\rho\bmod k\) large take \(u=(N-a_\rho)/k\) and let \(p\) be the greatest prime divisor of \(u(u-1)\).
For fixed \(k\) this prime tends to infinity through all delays.
Otherwise infinitely many positive pairs \(u,u-1\) solving \(x-y=1\) would consist entirely of units with prime support in a fixed finite set, contrary to the [finite-rank unit equation theorem](../audits/literature/ESS02/Yin_U001.md#ess-exact-counting-bound).
At every delay \(p\) divides the difference from one of the two short delays and \(p\le (N-a_\rho)/k\le\min d_{f,\sigma,N}/k\) by the degree bound \(d_{f,\sigma,N}\ge N-9\deg f\).
There are just \(2k\) fixed short delays at this stage.
The [fixed-base all-prime theorem](Yin_C_G0899_v5.md#statement) gives both rates to within \(1/k\) of the respective half log measures for these finitely many Salem polynomials at all large primes.
The ideal transfer gives the same rates at the original delay.
Choose increasing thresholds \(N_k\) such that for \(N\ge N_k\) all stage-\(k\) comparisons hold, their errors from the limiting half log seed measures are at most \(2/k\), and \(p\ge k\).
Using stage \(k\) on \(N_k\le N<N_{k+1}\) proves all assertions, as in the [simultaneous selection](../ledger/Yin_L_G0462_v111.md#selection).
For the pointwise assertion enumerate the eligible integer polynomials and perform stage \(k\) for the first \(k\) seeds and both signs.
Every fixed seed belongs to every sufficiently late stage, so the [countable diagonal choice](../ledger/Yin_L_G0462_v111.md#all-seeds) gives its two limits along that single sequence.

## Assessment history

### Decision sublinear-pisot-seeds-submitted

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:54 |
| status | open |
| reason | Submit the simultaneous sublinear prime-order recovery theorem for both signs at arbitrary fixed finite sets of nonreciprocal Pisot seeds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Sublinear prime orders](#statement) | The original Salem minimal polynomials, all sufficiently large delays, both signs, every fixed finite list, common integer moduli, resultants and both rate formulations. |
| argument | [Trace ideal](#transfer) | Fixed torsion supply and multiplicities, parity, cancellation and ideal equality at the original primitive factors. |
| argument | [Prime choice](#selection) | Finitely many delays at each stage, a largest prime factor, degree-relative window and simultaneous diagonal convergence. |
| dependency | [Fixed-seed return](../ledger/Yin_L_G0462_v27.md#fixed-seed-return) | Unique exterior root, convergence, sole reciprocal factor and bounded cyclotomic cofactor. |
| dependency | [Actual cofactor](../ledger/Yin_L_G0462_v111.md#cofactor) | Torsion orders, multiplicities, the lower degree bound and the factor at one. |
| dependency | [Real trace ideals](../ledger/Yin_L_G0462_v111.md#ideals) | Unit descent and equality of integer-valued gcds and norms. |
| dependency | [Simultaneous selection](../ledger/Yin_L_G0462_v111.md#selection) | Sublinear degree ratio and simultaneous order for every seed and sign. |
| dependency | [Pointwise prime sequence](../ledger/Yin_L_G0462_v111.md#all-seeds) | Countable diagonalization over all fixed seeds and absence of a uniform onset. |
| dependency | [Unit equation](../audits/literature/ESS02/Yin_U001.md#ess02-u001) | Finiteness for consecutive positive integers over a fixed finite set of primes. |
| dependency | [Fixed-base rates](Yin_C_G0899_v5.md#statement) | Common divisor and trace norm rates for all sufficiently large primes on each fixed short Salem polynomial. |

### Decision sublinear-pisot-seeds-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:00 |
| status | proved |
| reason | Independent review verifies the primitive factor and cofactor transfer, preservation of the trace ideal, simultaneous sublinear prime selection and the countable pointwise result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Sublinear prime orders](#statement) | The original Salem minimal polynomials, all sufficiently large delays, both signs, every fixed finite list, common integer moduli, resultants and both rate formulations. |
| argument | [Trace ideal](#transfer) | Fixed torsion supply and multiplicities, parity, cancellation and ideal equality at the original primitive factors. |
| argument | [Prime choice](#selection) | Finitely many delays at each stage, a largest prime factor, degree-relative window and simultaneous diagonal convergence. |
| dependency | [Fixed-seed return](../ledger/Yin_L_G0462_v27.md#fixed-seed-return) | Unique exterior root, convergence, sole reciprocal factor and bounded cyclotomic cofactor. |
| dependency | [Actual cofactor](../ledger/Yin_L_G0462_v111.md#cofactor) | Torsion orders, multiplicities, the lower degree bound and the factor at one. |
| dependency | [Real trace ideals](../ledger/Yin_L_G0462_v111.md#ideals) | Unit descent and equality of integer-valued gcds and norms. |
| dependency | [Simultaneous selection](../ledger/Yin_L_G0462_v111.md#selection) | Sublinear degree ratio and simultaneous order for every seed and sign. |
| dependency | [Pointwise prime sequence](../ledger/Yin_L_G0462_v111.md#all-seeds) | Countable diagonalization over all fixed seeds and absence of a uniform onset. |
| dependency | [Unit equation](../audits/literature/ESS02/Yin_U001.md#ess02-u001) | Finiteness for consecutive positive integers over a fixed finite set of primes. |
| dependency | [Fixed-base rates](Yin_C_G0899_v5.md#statement) | Common divisor and trace norm rates for all sufficiently large primes on each fixed short Salem polynomial. |
| review | [Independent review](../audits/reviews/Yin_R_G1114_v95.md#sublinear-prime-order) | All three claim sections, all direct dependencies, both signs and both rates for the varying Salem minimal factors. |

## Current assessment

[Selected decision](#decision-sublinear-pisot-seeds-reviewed)
