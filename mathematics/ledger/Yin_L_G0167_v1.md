---
author: Yin
---

# Actual Salem circle cost from the powered discriminant

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded G0001/S_G0008 candidate written by assigned AI `entropy_status` for Yin.
The author and coordinator independently obtained the same regularized-energy argument during this round; their contribution scope is recorded below.
This result is contributor-checked; complete noncontributor independent AI review and fixed adoption are recorded below.
No numerical run, prime scan, or new uniform Mahler gap is claimed.

Local reuse inspected [L74](Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion), [L75](Yin_L_G0075_v1.md#chebotarev-period-cost), the unique-exterior power-degree argument in [L128](Yin_L_G0128_v1.md), and [L152](Yin_L_G0152_v1.md#real-cyclotomic-primitive-norm).
The present bound uses the actual conjugates of a powered Salem number, rather than the circle supremum of an auxiliary polynomial.
It supplies a new upper cost, not missing local norm income.

<a id="actual-powered-salem-discriminant-energy"></a>
## 1. Degree preservation and central discriminant energy

Let alpha>1 be a Salem number with monic irreducible polynomial P, degree d>=4, and m=log alpha=log M(P)>0.
For an integer n>=1 put

    beta=alpha^n,     t=nm,     q=d-2,
    C_n=|Norm_(Q(alpha)/Q)(alpha^n-1)|.

Every positive power beta has degree d.
Indeed, if the extension Q(alpha)/Q(beta) had degree k>1, its k distinct embeddings fixing beta would send alpha to k distinct roots of X^n-beta.
All have absolute value alpha>1 and are conjugates of alpha over Q, contradicting its unique exterior conjugate.
Thus Q(beta)=Q(alpha).
The conjugates of beta are distinct and have the form

    e^t, e^(-t), gamma_1,...,gamma_q,      |gamma_j|=1.      (1)

None is one, since beta is noncyclotomic.
Its minimal polynomial is monic integral, so the absolute value of its nonzero discriminant is an integer at least one.
Separating its two off-circle roots gives

    -sum_(i!=j) log|gamma_i-gamma_j|
       <=2 log|e^t-e^(-t)|
          +2 sum_j log|e^t-gamma_j|
          +2 sum_j log|e^(-t)-gamma_j|
       <=H:=2(q+1)t+4q log2.                               (2)

For the last line use |e^t-e^(-t)|<=e^t, |e^t-gamma_j|<=2e^t and |e^(-t)-gamma_j|<=2.
In the first line, the ordered sum i!=j is precisely the logarithm of the central squared Vandermonde product, so no factor of two is missing.
The use of the powered discriminant is legitimate because the preceding degree argument retains all d embeddings.

## 2. Regularization, diagonal energy, and the actual product

Fix any real 0<r<1 and set

    L_r=-log(1-r),           S_k=sum_(j=1)^q gamma_j^k.

Absolute convergence of the logarithmic power series gives

    E_r:=sum_(k>=1) r^k |S_k|^2/k
        =-sum_(i,j) log|1-r gamma_i conjugate(gamma_j)|.    (3)

To verify the identity, use -log|1-r z|=sum_(k>=1)r^k Re(z^k)/k on |z|=1 and sum over the finite set of pairs; their sum is |S_k|^2.
For |z|=1 the exact identity

    |1-r z|^2=r|1-z|^2+(1-r)^2

implies log|1-r z|>=log|1-z|+(log r)/2 whenever z!=1.
The q diagonal terms in (3) are exactly q L_r.
Applying (2) to the off-diagonal terms therefore proves

    0<=E_r<=B_r:=2(q+1)nm+4q log2+q L_r
                         -[q(q-1)/2]log r.                (4)

Thus for the empirical measure q^(-1)sum_j delta_(gamma_j), its regularized logarithmic energy is E_r/q^2, bounded by B_r/q^2.
The diagonal self-energy q L_r and the regularization correction involving log r are both retained explicitly.

The same elementary modulus inequality, now at each gamma_j, gives

    sum_j log|1-gamma_j|
       <=sum_j log|1-r gamma_j|-(q/2)log r
       =-Re sum_(k>=1) r^k S_k/k-(q/2)log r
       <=sqrt(E_r L_r)-(q/2)log r.                         (5)

The last step is Cauchy--Schwarz with the two sequences r^(k/2)S_k/sqrt(k) and r^(k/2)/sqrt(k).
Their squared norms are E_r and L_r respectively, both finite.
If some unregularized factor vanished the product bound would hold by a limit; in the present noncyclotomic domain it does not vanish.

The off-circle contribution to C_n is

    |e^t-1||e^(-t)-1|=e^t(1-e^(-t))^2<=e^t.

Combining this with (4)--(5) proves the complete finite bound

    0<=log C_n<=nm+E(d,n,m;r),
    E(d,n,m;r)=-(q/2)log r+sqrt(B_r L_r).                   (6)

The lower bound uses that C_n is a nonzero integer.
Every quantity on the right is explicit; r is an arbitrary chosen parameter.
No external equidistribution or discrepancy theorem is a premise.

<a id="sublinear-actual-circle-cost"></a>
## 3. Uniform sublinear cost on linear-degree windows

Write h=nm/d.
For 0<delta<=1/2 choose r=1-delta and L=log(1/delta).
The inequalities -log(1-delta)<=2delta and q+1<=d give from (6)

    E(d,n,m;1-delta)/d
       <=delta+sqrt([2h+delta+(4log2+L)/d]L).               (7)

This estimate is valid for every n>=1 and m>0; only the chosen delta is restricted.
In particular if h<=1/2, choose

    delta=max(h,1/d),            L=log(1/delta).             (8)

As h tends to zero and d tends to infinity, the right side of (7) tends to zero.
Indeed delta tends to zero, h<=delta, and L<=log d, so the quantity under the square root is at most

    3delta log(1/delta)+(4log2+log d)log d/d ->0.            (9)

For every fixed C>0 this convergence is uniform over all integers 1<=n<=Cd along m->0 and d->infinity, because h<=Cm.
Hence

    log C_n<=nm+o(d)       uniformly for 1<=n<=Cd,
    log C_n=o(d)           on the same near-one regime.     (10)

More generally the proof only requires nm/d->0.
If additionally c_0d<=n<=Cd for a fixed c_0>0, then E/n<=E/(c_0d)->0.
There is no assumption of root separation beyond distinctness, and no hidden input-dependent equidistribution constant.
The statement is conditional on whatever inputs occur in this regime; it asserts no existence of a sequence with m->0.

<a id="actual-income-reduced-circle-threshold"></a>
## 4. A finite same-exponent income criterion

The cost reduction changes the sufficient arithmetic target.
Let A(n) be any certified local lower income at the same exponent, counting distinct ideals and actual layers as in L74, so A(n)<=log C_n.
Fix eta>0 and C>0.
Choose one delta in (0,1/2] such that, with L=log(1/delta),

    delta+sqrt(delta L)<=eta/4.                             (11)

Such a choice exists because delta log(1/delta)->0.
The choice is independent of the polynomial, degree and unknown m.
Define

    D=max(4,ceil[16(4log2+L)L/eta^2]),
    m_0=min(eta/(8C), eta^2/(128 C L))>0.                   (12)

If d>=D, n<=Cd and m<=m_0, equation (7) and sqrt(x+y+z)<=sqrt(x)+sqrt(y)+sqrt(z) imply

    log C_n/d
       <=Cm+sqrt(2Cm L)
             +delta+sqrt(delta L)
             +sqrt((4log2+L)L/d)
       <=eta/4+eta/4+eta/4=3eta/4.                         (13)

Here Cm<=eta/8 and sqrt(2Cm L)<=eta/8 follow individually from the two choices in m_0.
Consequently a certified income

    A(n)>=eta d,       1<=n<=Cd,       d>=D                 (14)

forces m>m_0.
This is an explicit sufficient implication for large degree and any positive linear income eta d; the old requirement of first exceeding d log2 has been removed on this Salem near-one test.
Finite degrees below D would need their separate fixed-degree treatment before any all-degree assertion.

No hypothesis (14) is established here.
In particular the L152 floor from one primitive inversion orbit at an index n>=3 is only 2log(n-1), which is o(d) for n<=Cd, and does not meet a fixed eta d target.
Automatic lifts or the degree-four prime range of L166 do not automatically produce (14).
Contributions at different exponents cannot be added and then inserted into (6) or (14) without a separately proved joint-exponent inequality.

The gain is therefore a strictly weaker required same-time income, with explicit finite constants.
It leaves the actual near-one arithmetic coverage unproved and does not reopen L153's retained mixed-trace Fourier certificate.
Only the actual cyclic norm and its original d conjugates are used.

## Contribution, attribution and current review scope

The assigned entropy_status AI derived the powered-discriminant bound, r-regularized energy and Fourier Cauchy--Schwarz estimate, the delta parameter choice, and the explicit same-time income transfer.
During the same round the coordinator independently supplied the same energy and product proof with r=exp(-2t_0), including the diagonal term and all factors of two.
These parallel derivations were compared and agree; the coordinator's contribution is acknowledged rather than called independent review of this source.

The growth_arithmetic_status AI separately located the known discriminant/regularized-energy mechanism in Igor E. Pritsker's *Distribution of algebraic numbers*, J. reine angew. Math. 657 (2011), 57--80.
The coordinator retained arXiv:1307.5734v1 and read pp. 1, 7 and 14--17, including visual inspection of pp. 15--16.
Theorem 4.2, equation (4.16) on p. 15 and its discriminant-energy proof on p. 16 provide standard-mechanism attribution, with precise scope in the [Pri11 reading note](../audits/literature/Pri11/readme.md#pri11-actual-product-energy).
The raw logarithmic test here is not directly a compact finite-energy test of that theorem.
No such direct application or additional external premise is used: the Salem specialization and displayed constants above are derived locally in full.
No novelty is claimed for the general energy method.
The completed independent review of all sections is recorded below.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0066_v1.md#actual-circle-cost-independent-review), with its original inspected scope and relationship.
