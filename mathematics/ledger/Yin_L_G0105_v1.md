---
author: Yin
---

# Weighted trace decay and the cost of moving the multiplier

The current complete mathematical proof is retained in [C302](../claims/Yin_C_G0302_v1.md#argument).
The original mathematical text below remains the fixed old input,with its original date and exact old review bindings.

Date: 2026-10-07.
Bounded direct proof by the assigned assess_shortness_route AI for Yin.
The coordinator checked the proposed scope and requested an explicit fixed-test-parameter boundary.
This note extends the unit-circle argument of [L G0102](Yin_L_G0102_v1.md#unit-circle-trace-witness-decay) to every fixed nonzero algebraic-integer multiplier and all finite prefixes.
It also gives an actual moving-unit control.
No new source, computation, or novelty claim is involved.

Let alpha be an algebraic unit with monic irreducible polynomial P of degree d, m=log M(P)>0, and at least one unit-circle conjugate.
Put K=Q(alpha).
The unit norm and m>0 imply both stable and expanding conjugates.
All field embeddings below are counted, including both members of complex pairs.

<a id="weighted-central-trace-prefix-decay"></a>
## Every fixed nonzero multiplier has uniform prefix decay

Fix theta in O_K minus {0}.
For every integer j define

    u_(theta,j)=sum_(|sigma(alpha)|<1) sigma(theta) sigma(alpha)^j,
    v_(theta,j)=sum_(|sigma(alpha)|>1) sigma(theta) sigma(alpha)^j,
    w_(theta,j)=sum_(|sigma(alpha)|=1) sigma(theta) sigma(alpha)^j.

Each sum is real, and their total is the integer Tr_(K/Q)(theta alpha^j).
Negative j are allowed because alpha is a unit.
In general w_(theta,-j) need not equal w_(theta,j); no such identity is used.

Use stable real coordinates, with one complex coordinate per conjugate pair, and let A be multiplication by alpha there.
Put rho=||A||<1 and let iota be the embedding map.
For a real stable place, give zeta_(theta,0) coordinate sigma(theta); for a complex representative give it the two real coordinates (2 Re sigma(theta), -2 Im sigma(theta)).
Then, for t>=0,

    zeta_(theta,t)=(A^T)^(-t) zeta_(theta,0),
    <zeta_(theta,t),iota(alpha^j)>=u_(theta,j-t).

Let mu_N be the law of the actual stable fair-sign sum Y_N=sum_(j=0)^(N-1) xi_j iota(alpha^j).
There are constants C_theta>=1 and eta_theta>0 such that

    |hat mu_N(zeta_(theta,t))|
       <=C_theta exp[-eta_theta min(N,t)]
               for all N>=1 and integers t>=0.           (1)

Here and below the Fourier character is exp(2pi i<zeta,y>).

To prove (1), write the central conjugates as beta_1,...,beta_q and their coefficients as c_i=sigma_i(theta).
They are distinct, none is a root of unity, and all c_i are nonzero.
The last assertion uses injectivity of each field embedding.
Consider directly the negative sequence

    z_k=w_(theta,-k)=sum_(i=1)^q c_i beta_i^(-k), k>=0.

If |cos(2pi z_k)|=1 for every k, then z_k is a bounded half-integer sequence, hence has a finite alphabet.
It obeys the order-q recurrence with distinct characteristic roots beta_i^(-1).
Repeated length-q blocks make it eventually periodic.
Subtracting one period p and using q consecutive indices gives an invertible Vandermonde system, forcing c_i beta_i^(-a)(beta_i^(-p)-1)=0 for every i.
This is impossible.
Thus some k_0 has |cos(2pi z_(k_0))|<1.

Let H be the closure of the nonnegative powers of (beta_1^(-1)...,beta_q^(-1)) in the compact torus.
As in L G0102, H is a group and its rotation by this point is minimal: each orbit is dense in H.
The continuous function sum_i c_i x_i is real on H, since it is real on the dense power orbit.
A neighborhood U of the point at k_0 and an epsilon in (0,1/2) can therefore be chosen so that |cos(2pi sum_i c_i x_i)|<=1-2epsilon on U.

For clarity, the bounded-gap step uses only compactness.
The translates U z^(-n), n>=0, cover H, since every forward orbit is dense.
A finite subcover gives B such that every block of B+1 consecutive nonnegative indices visits U.
The group-closure fact follows by taking differences of a convergent subsequence of powers to approach the identity; either the difference exponents are unbounded, giving the inverse generator as a limit of nonnegative powers, or a fixed positive power is the identity.
Thus no independence or equidistribution assertion is needed.

The trace identity gives

    |cos(2pi u_(theta,-k))|
       =|cos(2pi[v_(theta,-k)+w_(theta,-k)])|.

Since v_(theta,-k)->0, all visits to U after a fixed K_0 satisfy |cos(2pi u_(theta,-k))|<=1-epsilon.
The Fourier product for mu_N contains the negative-index block

    k=max(1,t-N+1)...,t,

whose length is min(N,t).
At least floor[(min(N,t)-K_0)_+/(B+1)] of its factors have the displayed bound; all other factors have absolute value at most one.
This proves (1), for instance with

    eta_theta=-log(1-epsilon)/(B+1),
    C_theta=exp(eta_theta K_0)/(1-epsilon).               (2)

The same argument bounds the infinite stable fair-sign law at these frequencies by C_theta exp(-eta_theta t).
The finite-prefix bound (1) is stronger than just that infinite-law conclusion.

<a id="bounded-multiplier-family-obstruction"></a>
## Finite multiplier sets and bounded conjugate size

For any fixed finite set Theta of nonzero multipliers, take C=max C_theta and eta=min eta_theta.
Equation (1) then holds uniformly for theta in Theta.

This applies in particular to all theta in O_K minus {0} whose conjugates have absolute value at most a fixed H.
There are only finitely many such theta: their monic minimal polynomials have degree at most d, and each integer coefficient is bounded by the appropriate elementary symmetric-function bound in H.
There are finitely many possible polynomials and finitely many roots of each.
Every conjugate of theta occurs among its extensions to embeddings of K, so this argument applies to the stated bound.
No choice of an integral basis is required.

Consequently, if theta_n is chosen with |hat mu_(N_n)(zeta_(theta_n,t_n))|>=c>0 and min(N_n,t_n)->infinity, then

    max_sigma |sigma(theta_n)| -> infinity.              (3)

This is a necessary escape from every bounded set, not a quantitative growth rate for that conjugate size.
The decay constants in (1) are not shown to be uniform over unbounded multipliers.

<a id="moving-unit-low-frequency-control"></a>
## An actual moving multiplier restores amplitude at low frequency

For every integer q, theta=alpha^q is an algebraic integer.
Its trace frequency satisfies the exact identity

    zeta_(alpha^q,t)=(A^T)^(q-t) zeta_(1,0)
                    =zeta_(1,t-q),                     (4)

where the last notation is extended to every integer index.
Thus multipliers from these powers merely reindex the same trace frequencies.
When t-q>=0 the fixed-multiplier decay already applies with effective index t-q.

There is nevertheless a real high-amplitude moving family.
Fix an integer J>=0, take q=N+J, and use t=1,...,N.
Put nu_(N,t)=zeta_(alpha^(N+J),t) and T=max_(stable beta)(1-|beta|)^(-1).
The stable dimension is s, and ||Y_N||<=sqrt(s)T.
Normality of A gives

    ||nu_(N,t)||<=||zeta_(1,0)|| rho^(N+J-t),
    sum_(t=1)^N ||nu_(N,t)||^2
       <=||zeta_(1,0)||^2 rho^(2J)/(1-rho^2).             (5)

Symmetry and cos x>=1-x^2/2 imply uniformly in N,t

    hat mu_N(nu_(N,t))
       >=1-2pi^2 sT^2 ||zeta_(1,0)||^2 rho^(2J).          (6)

Hence J can make all N coefficients exceed any fixed 1-epsilon.
This does not contradict (1): the multiplier changes with N, and its conjugate size grows exponentially.
If lambda_max=max_sigma |sigma(alpha)|>1, it is exactly lambda_max^(N+J).

The frequencies in (5) remain in one fixed small ball.
They cannot satisfy the L G0102 normalization ||nu_j||>=4^j for a number of indices proportional to N.
In particular high amplitude alone has not supplied its Gaussian Riesz-product premise.

<a id="moving-frequency-fixed-test-cost"></a>
## The same Gaussian test has an explicit bounded gain

This can be quantified without a packing assertion.
Either use mu_N itself, or add independent symmetric noise U_N uniform on aA^N K_0 for any fixed a>0, where K_0 is the product of stable unit intervals/discs.
For the latter law f_N of Y_N+U_N,

    E||Y_N+U_N||^2<=s(T+a)^2=:K_2.

The unit-circle branch does not inherit L G0102's disjoint packing or its Nm-H_N differential-entropy identity.
We use only this moment bound.
Let G be the standard Gaussian in the same real space, and fix a test coefficient u>=0.
For arbitrary signs epsilon_t, set

    F_N(x)=u sum_(t=1)^N epsilon_t cos(2pi<nu_(N,t),x>).

The inequalities 1-cos x<=x^2/2 and 1-exp(-x)<=x, together with symmetry, give

    |E_(f_N) cos(2pi<nu,x>)-E_G cos(2pi<nu,G>)|
       <=2pi^2(K_2+1)||nu||^2.

Jensen's inequality says log E_G exp(F_N)>=E_G F_N.
Thus the variational expression used in L G0102 satisfies

    E_(f_N) F_N-log E_G exp(F_N)
       <=2pi^2 u(K_2+1)||zeta_(1,0)||^2
                         rho^(2J)/(1-rho^2).             (7)

The same bound applies to the unsmoothed mu_N with K_2=sT^2.
It is independent of N for fixed P,J,u.
No assertion of finite relative entropy for the discrete law is needed to bound this displayed variational expression.

Equation (7) is deliberately restricted to fixed u; if u=u_N grows, its explicit right side grows proportionally.
It does not exclude every optimized moving test or every other multiplier.
For an isotropic Gaussian of standard deviation sigma_N the exact comparison term is

    D(f_N||phi_(sigma_N))=-h_diff(f_N)+(s/2)log(2pi)
                +s log sigma_N+E||Y_N+U_N||^2/(2sigma_N^2).

If that rescaling is to put even the first displayed frequency above a fixed Gaussian frequency threshold c>0, it needs sigma_N||nu_(N,1)||>=c.
Equation (5) then forces

    log sigma_N>=(N+J-1)(-log rho)
                           +log(c/||zeta_(1,0)||).

Thus the explicit s log sigma_N cost is linear in N.
This is an accounted cost, not a proof that every rescaled argument fails; anisotropic or otherwise changed tests are not analyzed here.
What is proved is that this actual high-amplitude family gives no linear-in-N saving through the fixed-strength, fixed-Gaussian test used above.

## Consequence and review scope

Every fixed nonzero integral multiplier, and every bounded conjugate-size family of multipliers, fails to restore the constant-amplitude deep-frequency premise in the unit-circle branch.
Moving actual unit powers can restore amplitude, but only by the explicitly exhibited index shift and low frequencies, with the bounded test gain (7).
These results leave arbitrary unbounded multipliers and changed test normalizations open; they are not a complete optimized no-go theorem or an entropy-gap result.

## Original contribution and actual checks

The complete original author,contributor,partial and whole checking account is retained in [R543](../audits/reviews/Yin_R_G0543_v1.md#complete-original-l105-checking-account).
Its original inputs,date,mathematical scopes and verdicts remain unchanged,with exact finding-specific relationships.
