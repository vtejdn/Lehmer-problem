---
author: Yin
---

# A three-time all-prime return obstruction on the retained plastic-seed Salem family

Date: 2026-10-08.
Direct derivation by the assigned growth_arithmetic_status AI for Yin, under the authorized bounded G0001 exploration.
The coordinator selected the partial-return and exponent-cost question and allocated this working draft after receiving the derivation.
The fixed adoption and completed proof review are recorded below.

## Question and scope

This tests the [arithmetic route's next coverage question](../strategies/Yin_S_G0008.md#next-coverage-test) at the three support-adjacent times \(N,N+1,N+2\) in the already retained [plastic-seed Salem family](Yin_L_G0020_v1.md#sparse-salem-delay-family).
The test permits arbitrary rational primes, arbitrary distinct prime ideals and their full actual valuation depths.
The conclusion is an obstruction to this concrete time selection, including its divisor times.
It is not an obstruction to the aggregate method at other times or to coverage in a sufficiently near-one window.

All logarithms are natural.
No new external theorem or numerical experiment is a premise.
The construction of the actual Salem factors is retained at the existing L G0020 / Smy15 statement scope; the calculations below are direct algebraic arguments.

## The retained family on an arithmetic progression

Put
\[
 f(t)=t^3-t-1,\qquad f^*(t)=t^3f(1/t)=1-t^2-t^3,
 \qquad F_N(t)=t^Nf(t)+f^*(t).
 \tag{1}
\]
Let \(\theta>1\) be the real root of \(f\).
As recorded in [L G0020](Yin_L_G0020_v1.md#sparse-salem-delay-family), the rational-root test proves irreducibility, the discriminant is \(-23\), and the other two roots have modulus \(\theta^{-1/2}<1\).
Thus \(\theta\) is Pisot.
Also \(\theta<4/3\), since \(f\) is strictly increasing on \([1,\infty)\) and \(f(4/3)=1/27>0\).

For every sufficiently large integer \(N\), the already accepted [Smy15 construction statement](../audits/literature/Smy15/readme.md) gives
\[
 F_N=P_N C_N,
 \tag{2}
\]
where \(P_N\) is the monic minimal polynomial of a Salem number \(\tau_N\), and \(C_N\) is a monic product of cyclotomic polynomials.
In particular \(F_N\) has exactly one root outside the unit circle, and \(M(F_N)=M(P_N)=\tau_N\).
This uses exactly the retained external construction statement.
Its original proof is not newly proved or newly source-audited here.
The symbol \(C_N\) denotes the cyclotomic polynomial factor; cyclic resultants below use the separate symbol \(R_n\).

Restrict to
\[
 N=24k+9,\qquad k\geq0,
 \tag{3}
\]
beyond that construction's threshold and with \(N\geq16\).
These conditions leave an infinite progression.
Direct substitution gives
\[
 F_N(\theta)=-\theta(\theta+1)<0,
 \qquad
 F_N(4/3)=\frac{(4/3)^N-85}{27}>0.
\]
The unique exterior root supplied by (2) therefore satisfies
\[
 \theta<\tau_N<4/3.
 \tag{4}
\]
For any fixed \(b>\theta\), one has \(f(b)>0\), so \(b^Nf(b)+f^*(b)>0\) for sufficiently large \(N\).
The same argument then gives \(\tau_N<b\), proving \(\tau_N\to\theta\) on (3).
No assertion that \(N=16\) clears the external construction threshold is made.

The \(\tau_N\) are distinct.
If \(\tau>\theta\) were a root of both \(F_N\) and \(F_M\), then \(f(\tau)\ne0\) and
\[
 \tau^N=-f^*(\tau)/f(\tau)=\tau^M,
\]
forcing \(N=M\).
Consequently \(d_N=\deg P_N\) tends to infinity: for each fixed degree bound, the coefficient estimate \(\lvert a_j\rvert\leq\binom{d}{j}M(P)\) leaves only finitely many monic integer polynomials of degree at most that bound and measure below \(4/3\), and hence finitely many possible roots.

Every positive power of \(\tau_N\) retains degree \(d_N\).
Indeed, if the extension \(\mathbb Q(\tau_N)/\mathbb Q(\tau_N^a)\) had degree greater than one, its distinct conjugates of \(\tau_N\) would all have modulus \(\tau_N>1\).
They would be distinct conjugates over \(\mathbb Q\), contrary to the unique exterior root of \(P_N\).
This is also the one-expanding-conjugate argument used in L G0020.
Thus the progression gives actual reciprocal noncyclotomic unit cores of unbounded degree with all-power degree preservation.
Their measures approach \(\theta\), not one.

<a id="three-time-resultant-obstruction"></a>
## Exact resultants at the three support-adjacent times

For a monic integer polynomial \(H\), define
\[
 R_n(H)=\lvert\operatorname{Res}(H,t^n-1)\rvert,
 \qquad n\geq1,
 \tag{5}
\]
allowing zero if there is a common root.
For \(j=0,1,2\), set \(n=N+j\).
At every \(z\) satisfying \(z^n=1\), equation (1) gives
\[
 z^j F_N(z)=f(z)+z^j f^*(z).
\]
The product of the monomial factors over all \(n\)-th roots of unity has modulus one.
Since interchanging the two arguments of a resultant changes at most its sign,
\[
 R_{N+j}(F_N)
   =\left\lvert\operatorname{Res}\bigl(t^{N+j}-1,h_j(t)\bigr)\right\rvert,
 \qquad h_j=f+t^j f^*.
 \tag{6}
\]
Direct expansion and factorization give the identities in \(\mathbb Z[t]\)
\[
 \begin{aligned}
 h_0&=-t(t+1),\\
 h_1&=-(t^4+1)=-\Phi_8(t),\\
 h_2&=-(t+1)(t^4-t^2+1)=-\Phi_2(t)\Phi_{12}(t).
 \end{aligned}
 \tag{7}
\]

For \(j=0\), the exponent \(N\) is odd.
The factor \(t\) in (7) contributes absolute value one, while \(t+1\) contributes \(\lvert(-1)^N-1\rvert=2\).
Hence
\[
 R_N(F_N)=2.
 \tag{8}
\]

For \(j=1\), equation (3) gives \(N+1\equiv2\pmod8\).
Among the four primitive eighth roots \(\eta\), the values \(\eta^{N+1}\) equal \(i\) twice and \(-i\) twice.
Thus
\[
 R_{N+1}(F_N)
   =\lvert(i-1)^2(-i-1)^2\rvert=4.
 \tag{9}
\]

For \(j=2\), the exponent \(N+2\) is odd and is congruent to \(11\pmod{12}\).
Raising to that exponent permutes the primitive twelfth roots, so their contribution in (7) is \(\Phi_{12}(1)=1\).
The \(\Phi_2\) factor contributes two.
Therefore
\[
 R_{N+2}(F_N)=2.
 \tag{10}
\]
In particular all three full resultants are nonzero.
No unremoved cyclotomic zero is being interpreted as a positive norm.

## Passing to the actual irreducible core

Multiplicativity in (2) gives, for each \(n\in\{N,N+1,N+2\}\),
\[
 R_n(F_N)=R_n(P_N)R_n(C_N).
 \tag{11}
\]
Both factors on the right are nonzero integers by (8)--(10).
Consequently
\[
 R_N(P_N)\mid2,\qquad
 R_{N+1}(P_N)\mid4,\qquad
 R_{N+2}(P_N)\mid2.
 \tag{12}
\]
Each core norm is at least one.
In particular every rational prime that occurs in any of these three core norms is two.
These conclusions do not assume \(C_N=1\), bound its degree, or identify its individual cyclotomic factors.

<a id="all-prime-partial-return-cost"></a>
## Arbitrary local contributions cannot pay the aggregate cost

Write \(K_N=\mathbb Q(\tau_N)\).
Since \(P_N\) is its monic minimal polynomial,
\[
 R_n(P_N)=\left\lvert
   \operatorname{Norm}_{K_N/\mathbb Q}(\tau_N^n-1)
   \right\rvert.
 \tag{13}
\]
For any finite collection of distinct prime ideals \(\mathfrak q\) of \(\mathcal O_{K_N}\), let \(\ell_{\mathfrak q}\) be the underlying rational prime and \(f_{\mathfrak q}\) its residue degree.
Let \(w_{\mathfrak q}\geq0\) be any certified lower bound for the integer valuation \(\operatorname{ord}_{\mathfrak q}(\tau_N^n-1)\).
Define
\[
 A(n)=\sum_{\mathfrak q}
 f_{\mathfrak q}w_{\mathfrak q}\log\ell_{\mathfrak q}.
\]
The exact ideal-norm accounting in [L G0074](Yin_L_G0074_v1.md#content-versus-ideal-norm) gives
\[
 \begin{aligned}
 A(n)
 &\leq\sum_{\text{all }\mathfrak q}
  f_{\mathfrak q}\operatorname{ord}_{\mathfrak q}(\tau_N^n-1)
    \log\ell_{\mathfrak q}\\
 &=\log R_n(P_N).
 \end{aligned}
 \tag{14}
\]
This includes ramified primes and arbitrary actual valuation depths.
It uses no good-prime or squarefreeness hypothesis.
The prime ideals are distinct: several lower bounds for the same ideal cannot be added without proving disjoint valuation layers.

Equations (12)--(14) yield
\[
 A(N)\leq\log2,\qquad
 A(N+1)\leq\log4,\qquad
 A(N+2)\leq\log2.
 \tag{15}
\]
These bounds allow the rational primes to vary with \(N\), and remain valid even when every actual local contribution is known exactly.
Increasing a prime cutoff or improving valuation precision cannot increase the total beyond (15).

The retained [aggregate cyclic-norm certificate](Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion) is
\[
 m(P_N)\geq\frac{A(n)-d_N\log2}{n}.
 \tag{16}
\]
At all three times, the certified right side of (16) is nonpositive once \(d_N\geq2\), and strictly negative once \(d_N>2\).
Since \(d_N\to\infty\), no choice of distinct local contributions at these times can pay even the \(d_N\log2\) archimedean cost.
This is a limitation of the specified certificate and time selection, not an upper bound for the true positive Mahler measure.

The obstruction also holds at every positive divisor of any of these three times.
If \(r\mid n\), then
\[
 \tau_N^n-1=(\tau_N^r-1)
    (1+\tau_N^r+\cdots+\tau_N^{n-r}).
\]
Both factors are nonzero algebraic integers.
Taking absolute norms therefore proves \(R_r(P_N)\mid R_n(P_N)\).
Thus \(R_r(P_N)\leq4\), and (14)--(16) give the same certificate obstruction at \(r\).

## Consequence and boundaries

The tested partial-return mechanism fails at three natural support-offset exponents and their divisor times because of exact polynomial remainder identities.
This conclusion includes all primes and full valuation depths; it is not a failure caused by stopping a prime search early.
A revised candidate must choose genuinely different exponents or add new arithmetic information.

The three exponents are \(D_N-3,D_N-2,D_N-1\) for the presentation degree \(D_N=N+3\).
No bound comparing \(N\) with the irreducible degree \(d_N\) is asserted.
Arbitrary other times, larger multiples, and sharper joint archimedean estimates remain outside this result.
In particular it is not an all-time obstruction.
Combining separate instances of (16) only gives the already recorded weighted-average boundary in L G0074 unless additional joint information is supplied.

The family has \(m(P_N)\to\log\theta>0\).
It does not refute Lehmer, does not establish the required near-one arithmetic coverage, and does not invalidate a claim explicitly restricted to a sufficiently small window below \(\theta\).
Existing fixed-prime scans, fixed-input norm asymptotics and scalar-period mechanisms are neither rerun nor improved by this calculation.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0038_v1.md#contribution-and-actual-review-scope), with its original inspected scope and relationship.
