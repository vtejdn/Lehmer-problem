---
author: Yin
---

# Actual cyclic-product cost for general algebraic units

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded G0001 candidate assembled by assigned AI `entropy_status` for Yin from the coordinator's supplied kernel, cutoff and degree-escape outline.
Contributor-checked and completely independently reviewed; the coordinator adopts this fixed bounded result after clearance.
No actual norm income, numerical execution or new control is asserted.

The sole new external statement interface is [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001), Theorem 3.1 at its recorded statement-acceptance scope.
The proof also reuses the height, coefficient and Kronecker conventions in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) and the original-field local-income convention of [L74](Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion).
The source theorem's analytic proof is not independently reproduced here.

<a id="general-unit-actual-product-cost"></a>
## 1. Actual degree and the normalized product

Let alpha be a nontorsion algebraic unit of degree d, with m=log M(P_alpha)>0.
For any integer n>=1 put beta=alpha^n, N=[Q(beta):Q], and h=h_abs(beta)=nm/d.
If beta_1,...,beta_N are its distinct conjugates and C_n=|Norm_(Q(alpha)/Q)(alpha^n-1)|, the field norm tower and height identities give exactly

    log C_n/d=(1/N)sum_i log|1-beta_i|,
    h=(1/N)sum_i log max(1,|beta_i|).                        (1)

Indeed the extension degree Q(alpha)/Q(beta) is d/N, and taking the norm of beta-1 repeats the smaller-field norm that many times.
All norms are nonzero because beta is nontorsion.
No hypothesis that N=d, or that any positive power preserves degree, is made.

Define on C the normalized chord and its logarithm by

    u(z)=|1-z|/max(1,|z|),        f(z)=log u(z),              (2)

with f(1)=-infinity.
Then 0<=u<=2.
The functions |1-z| and v(z)=max(1,|z|) are 1-Lipschitz, v>=1, and |u(z)-u(w)|<=|z-w|/v(z)+u(w)|v(z)-v(w)|/v(z)<=3|z-w|.

## 2. A compact Lipschitz test with all truncation costs

Fix T>=1 and R>=2.
Put f_T=log max(u,exp(-T)), and let chi_R equal one on |z|<=R, decrease linearly to zero on R<=|z|<=2R, and equal zero outside that disk.
Then

    -T<=f_T<=log2,        Lip(f_T)<=3exp(T),
    phi=chi_R f_T,        Lip(phi)<=A:=3exp(T)+T/R.          (3)

The latter product estimate uses |f_T|<=T, |chi_R|<=1 and Lip(chi_R)<=1/R.
Thus phi is a real compactly supported Lipschitz test whose support is contained in |z|<=2R.

For every z, including the extended-real value at z=1,

    f(z)<=phi(z)+1/R.                                      (4)

Inside |z|<=R this follows from f<=f_T.
Outside, if f_T<=0 then phi>=f_T>=f.
If f_T>0, it equals f and f-phi<=(1-chi_R)f<=log(1+1/|z|)<=1/R.

Let mu be normalized arclength measure on the unit circle.
Since chi_R=1 there, the elementary logarithmic sine integral gives integral f dmu=0.
One may verify this by applying the double-angle identity to the equal integrals of log sin and log cos on [0,pi/2].
For -pi<=theta<=pi, |1-exp(i theta)|>=2|theta|/pi.
Hence

    0<=integral phi dmu
      =integral(f_T-f)dmu
      <=(1/pi) integral_0^(pi exp(-T)/2)
                         log[pi exp(-T)/(2theta)] dtheta
      =exp(-T)/2.                                         (5)

For N>=55 the accepted Pri11 Theorem 3.1, applied to the monic integral minimal polynomial of beta and this test supported in radius 2R, gives

    |(1/N)sum_i phi(beta_i)-integral phi dmu|
       <=A(4R+1)sqrt(max(log N/N,h)).                       (6)

Its degree is the actual N and its Mahler-height term is h, not m or nm/N.
Separability in characteristic zero supplies its simple-root hypothesis.
Combining (1)--(6) proves

    0<=log C_n/d
       <=h+exp(-T)/2+1/R
              +(3exp(T)+T/R)(4R+1)sqrt(max(log N/N,h)).     (7)

The lower bound uses the nonzero integer norm.
This formula keeps every support, Lipschitz, height and actual-degree cost.

<a id="bounded-power-degree-escape"></a>
## 3. Small height forces the actual powered degree to grow

For any integer B>=55 there is a finite, effectively definable epsilon_B>0 such that every nontorsion algebraic unit of degree N<=B has absolute height at least epsilon_B.
Here is a finite construction, with no enumeration claimed to have been performed.

If such a unit has h<=1, its monic minimal polynomial coefficients satisfy |a_(N-j)|<=binom(N,j)exp(Nh)<=binom(N,j)3^N.
List all monic integer polynomials of degrees 1 through B with constant term plus or minus one and these integer coefficient bounds.
Retain their irreducible noncyclotomic members.
This is a finite set, and Kronecker gives positive height for every member.
Define epsilon_B as the minimum of one and all these positive heights, taking epsilon_B=1 if the retained set were empty.        (8)

Every unit of degree at most B and height at most one occurs in this list; those of height greater than one also satisfy the bound.
The finite polynomial list, factorization and cyclotomic tests are effective, and the positive algebraic Mahler measures permit certified approximations to a positive lower bound.
Thus (8) specifies a finite algorithm, not a closed numerical lower bound or an executed computation.

Fix C>0.
For n<=Cd we have h=nm/d<=Cm.
As m tends to zero, h tends to zero uniformly and (8) forces N to tend to infinity uniformly, even if the power has a degree drop.
In (7), first fix T,R; its last term and h then tend to zero.
Subsequently let T,R grow to make exp(-T)/2+1/R arbitrarily small.
Therefore

    log C_n/d ->0 uniformly for all integers 1<=n<=Cd
    as m->0 among nontorsion algebraic units.               (9)

No existence of a sequence approaching measure one is asserted.
This is not restricted to Salem or reciprocal inputs.

<a id="general-unit-finite-income-criterion"></a>
## 4. A finite conditional income criterion

Fix eta,C>0.
Choose T>=1,R>=2 so exp(-T)/2+1/R<=eta/4, write K_0=(3exp(T)+T/R)(4R+1), and choose

    tau=min(1,eta/4,eta^2/(16K_0^2)).

Choose an integer B>=55 with log B/B<=tau, and use (8).
Put

    m_0=min(tau/C,epsilon_B/(2C))>0.                        (10)

If m<=m_0 and n<=Cd, then h<=tau and h<epsilon_B, so N>B.
Monotonicity of log x/x for x>=3 gives log N/N<=tau.
Formula (7) consequently yields

    log C_n/d<=tau+eta/4+K_0 sqrt(tau)<=3eta/4<eta.          (11)

Thus any certified same-exponent local income A(n)<=log C_n with A(n)>=eta d and n<=Cd forces m>m_0.
No actual income covering a near-one class is proved here.
The finite epsilon_B construction is part of the cost, not an unstated uniform height theorem, and no different-exponent incomes are merged.

The coordinator supplied the normalized kernel, cutoff constants, circle integral target, source-theorem interface and bounded-degree escape outline.
The assigned entropy_status AI checked each estimate, completed the norm and finite-enumeration guards, and derived the explicit finite choices (10)--(11).
This is contributor verification; the separate noncontributor review is complete as recorded below.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0067_v1.md#general-unit-cost-independent-review), with its original inspected scope and relationship.
