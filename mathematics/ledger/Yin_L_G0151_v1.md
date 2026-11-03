---
author: Yin
---

# Actual integer resonances in Salem transition averaging

Date: 2026-10-09.
Direct G0001 derivation by the coordinating Codex AI for Yin.
This tests the actual resonance mass left open in [L G0126](Yin_L_G0126_v1.md#algebraic-transition-return-mass), using the already retained finite collision bound.
It does not use an energy collar, a support-count estimate in place of the true law, or a new external theorem.
Accepted for fixed-ledger preservation on 2026-10-09 after the complete independent review recorded below.
No numerical experiment or novelty claim.

Local reuse checked L G0123, L G0126, L G0129 and the finite collision interfaces in L G0089/L G0094/L G0097.
L G0126 explicitly leaves actual integer resonance mass uncontrolled by its supplied lower bounds.
The argument below uses the one expanding embedding of a Salem field to identify that mass, then applies those fixed finite-law inequalities.

<a id="salem-integer-resonance-fibers"></a>
## 1. The actual resonance fibers are rational lines

Let alpha>1 be a Salem number of degree d=q+2>=4, K0=Q(alpha), with its specified real expanding embedding sigma_+.
Thus q>=2 embeddings are central, and there is exactly one stable embedding.
Let theta be a nonzero algebraic integer in K0.
For x in K0 put

    psi_theta(x)=sum_(sigma != sigma_+) sigma(theta x).

For every algebraic integer x in K0,

    psi_theta(x) in Z  <=>  theta x in Z.                (1)

Indeed psi_theta(x)=Tr(theta x)-sigma_+(theta x), and the trace is integral.
If the left side is integral, sigma_+(theta x) is an integer a; injectivity of this embedding gives theta x=a in K0.
The converse is immediate, with psi_theta(x)=(d-1)a.
This does not assert such an equivalence for multiple expanding embeddings.

Fix J>=0, r=2J+1, and the actual fair-sign sum

    S=sum_(j=-J)^J xi_j alpha^j,
    Col_r=Pr(S=S'),
    p_(theta,J)=Pr(psi_theta(S-S') in Z),                (2)

where S' is an independent copy.
The unit property makes all these summands algebraic integers.
If every central |sigma(theta)|<=e, then

    Col_r <= p_(theta,J)
          <= (floor(2 r e)+1) Col_r.                    (3)

To see this, partition the distinct support values z of S by theta(z-z') in Z.
This is precisely the resonance equivalence relation by (1).
In a class choose z0, and write a_z=theta(z-z0) in Z.
Different support points give different integers.
For any two such points and any central embedding,

    |a_z-a_z'|=|sigma(theta) sigma(z-z')|<=2 r e.

Thus each class has at most floor(2 r e)+1 points.
If their actual probabilities are p_z, Cauchy--Schwarz gives (sum_class p_z)^2 <= (floor(2 r e)+1) sum_class p_z^2.
Summing over the classes proves (3), with no uniformity assumption on the algebraic-sum law.
In particular,

    2 r e<1  ==>  p_(theta,J)=Col_r.                    (4)

This is equality of events: there are then no nonzero integer resonances in the difference support.

<a id="actual-salem-resonance-bound"></a>
## 2. A finite upper bound using the original binary law

Put m=log M(P)=log alpha.
The fixed finite comparison in [L G0097](Yin_L_G0097_v1.md#refined-binary-poisson-rates) gives Col_r<=exp(-r D(m)/2), with D(m) as defined there.
Multiplying S by alpha^J and converting signs to bits preserve all fibers, so the bound applies at exactly this r.
Consequently

    p_(theta,J) <= (floor(2 r e)+1) exp(-r D(m)/2).       (5)

For 0<m<=1/32 one has the convenient weaker estimate

    D(m)>=m(1-m)>=3m/4.                                (6)

Indeed the same retained definition has D(m)>=g(sqrt(1-exp(-2m))), and g(x)>=x^2/2 for 0<=x<1: g(0)=g'(0)=0 and g''(x)=1/(1-x^2)>=1.
Also exp(-2m)<=1-2m+2m^2 for m>=0, by twice integrating the bound exp(-t)<=1.
This proves (6).
No asymptotic error or unspecified initial time is used.

<a id="simultaneous-multiple-resonance-barrier"></a>
## 3. Even the true resonance mass cannot pay the zero-multiplier cost

Assume 0<m<=1/32 and choose

    0<epsilon<=sqrt(m)/(16q),  0<delta<=m/8,
    integer K>=2,  b=K-1.

Let a nonzero integral seed theta have all central conjugates bounded by epsilon/b, and let H>=1 bound all its conjugates.
Use the common transition window which certifies every multiplier 1<=k<K:

    J=ceil(log(d b H/delta)/m),  r=2J+1.                (7)

Thus bH bounds every candidate's height and epsilon its central size.
These are sufficient simultaneous bounds; no claim is made that a seed violating them cannot contain an individually good multiplier.
The L G0129 Salem choice epsilon=kappa/sqrt(N), kappa=sqrt(m)/(16q), delta=sqrt(m(1-exp(-2m)))/16 satisfies the displayed parameter range for every N>=1.
This assertion concerns its tail window, not the other noise and time guards.

For the true mass in (2),

    K p_(theta,J)<1/4<1.                               (8)

Here is a complete uniform cost calculation.
Integer norm gives

    1<=|Norm(theta)|<=H^2(epsilon/b)^q,
    H>=(b/epsilon)^(q/2).

Set L=log(d b H/delta) and

    L0=log[(d/delta) b^(d/2) epsilon^(-q/2)].

Then L>=L0>log(32/m)>=log(1024)>4/3.
Equations (5)--(6) and K/b<=2 imply

    K p_(theta,J) <= (2b+4 r epsilon) exp(-3mr/8).

For r>=2L/m the right side decreases in r, since 3mr/8>=3L/4>1.
It follows that

    K p_(theta,J)
      <= (2b+8 epsilon L/m) exp(-3L/4)
      <= (2b+8 epsilon L0/m) exp(-3L0/4).              (9)

The last expression likewise decreases in L>=L0, by differentiating; 3L/4>1 suffices.
Its first term obeys

    2b exp(-3L0/4)
      =2(delta/d)^(3/4) b^(1-3d/8) epsilon^(3q/8)
      <=2(m/32)^(3/4)<1/16.                           (10)

We used d>=4, b>=1, epsilon<1, and m<=1/32.
For the second term, the elementary maximum x exp(-3x/8)<=8/(3 exp(1))<8/3 yields

    (8 epsilon/m)L0 exp(-3L0/4)
      <(64 epsilon/(3m)) exp(-3L0/8)
      <=(64/(3m))(m/32)^(3/8) epsilon^(11/8)
      <=[2/(3*32^(3/4))] m^(1/16)<1/12.              (11)

Here q>=2, epsilon<=sqrt(m)/32 and 32^(3/4)>8.
Equations (10)--(11) give Kp<7/48<1/4, proving (8).

The exact L G0126 Fejer identity for Q(k)=C(k theta,J) is

    1+2 sum_(k=1)^(K-1)(1-k/K) Q(k)^2
      =E F_K(psi_theta(S-S')) >=K p_(theta,J).

After removing the zero multiplier, its resonance-only lower bound is (Kp-1)/(K-1).
Formula (8) shows that this lower bound is negative even with the exact mass, throughout the displayed simultaneous near-one domain.
This strengthens L G0126's failure of its particular supplied lower estimate.
It does NOT bound individual Q(k) from above, discard the positive contribution from noninteger near-resonances as an upper bound, or exclude a finite selection using that contribution.
It also does not address L G0126's arbitrary many-candidate Gram test.

<a id="salem-resonance-continuation-boundary"></a>
## 4. Consequence and remaining obligation

The new actual information is the rational-line description (1), the true-mass comparison (3)--(5), and the all-parameter obstruction (8) for this simultaneous multiple test.
They bypass L G0149's energy budget hypothesis, but do not supply an actual product lower bound or a uniform Mahler gap.
Better exact algebraic collision probabilities or extra integer trace resonances cannot rescue this particular resonance-only Fejer floor in the stated domain.
A next averaging candidate must use quantified off-integer near-resonance mass, a different candidate geometry, or different costs, keeping the actual height and central constraints.
A single successful multiplier found outside the simultaneous seed conditions is not excluded.

The unrestricted G0001 objective remains active and unresolved.
No finite-window algorithm, source audit or numerical experiment was run.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0051_v1.md#actual-resonance-independent-review), with its original inspected scope and relationship.
