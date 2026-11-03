---
author: Yin
---

# G0001: exact projection cancellation in the companion mixed-minor test

Current complete proof: [C226](../claims/Yin_C_G0226_v1.md#projection-cost-identity), adopted at its actual current decision.
The original dated mathematical argument remains below as a fixed historical input; it supplies no Task resumption.

Date: 2026-10-07.
Direct bounded calculation by assigned AI assess_shortness_route for Yin.
This examines the [joint-prime proposal in L G0054](Yin_L_G0054_v1.md#joint-frobenius-minor-test), using the actual relation lattice and finite Gram certificate of [L G0004](Yin_L_G0004_v1.md#gram-lower-certificate) and the polynomial-shift maps in [C217v2](../claims/Yin_C_G0217_v2.md#argument).
No source search, numerical experiment or new external premise is used.

The conclusion is a precise relaxation boundary.
Every mixed-minor certificate of this type is pointwise bounded above by the direct orbit-Gram certificate at the same window.
Minimizing its full coefficient cost over rational lifts gives exactly that Gram certificate, independent of which full-rank arithmetic maps supplied the numerator.
Integral lifts retain an arithmetic restriction, and an arithmetic estimate could still establish the missing uniform lower bound on the Gram determinant.
The calculation does not rule out such a theorem or all joint-prime methods.

<a id="projection-cost-identity"></a>
## The exact normalized-row identity

Let V be a real d by N matrix of full row rank, with N>=d.
Let E be N by m, where m>=d, and suppose F=VE has row rank d.
Put

    W=VV^T,       G=det W,
    J=det(FF^T),
    C(E)=sum_(|I|=|H|=d) det(E[I,H])^2=e_d(E^T E).

Here e_d is the d-th elementary symmetric function of the eigenvalues; I and H are row and column subsets.
Define the normalized row matrix and the orthogonal projection

    U=W^(-1/2)V,       UU^T=I_d,
    Pi=U^T U=V^T W^(-1)V.

The rows of U form an orthonormal basis of the row space of V.
Extend them to an orthonormal basis of R^N.
In these coordinates E takes the block form

    E -> [ B ; Z ],       B=UE=W^(-1/2)F.

Projection replaces Z by zero, while preserving B.
Cauchy--Binet in the d by m matrix B gives

    C(Pi E)=det(BB^T)=J/G.                              (1)

All the terms counted by C(Pi E) are also present among the nonnegative minor-square terms of C(E) in these orthonormal coordinates.
The cost is unchanged by an orthogonal change of row coordinates.
Therefore

    J/C(E)=G eta(E),
    eta(E):=C(Pi E)/C(E),       0<eta(E)<=1.             (2)

This is an exact factorization of the normalized certificate into the actual orbit Gram determinant and a nonpositive logarithmic projection loss.
It uses the full mixed-minor sum, without independence assumptions on the column blocks.

<a id="unique-minimum-lift"></a>
## The projected representative is the unique minimum-cost lift

Fix V and F with the preceding ranks.
Every real lift E' satisfying VE'=F has the same first block B=W^(-1/2)F and an arbitrary second block Z.
Equation (1) shows that

    E_0=V^T W^(-1)F

attains cost J/G.
It is the unique minimizing lift.

To check strictness, suppose Z has a nonzero row z.
The d rows b_1,...,b_d of B are linearly independent because F has row rank d.
There is a choice of d-1 of these rows whose wedge with z is nonzero.
If z is outside their span, any d-1 suffice.
If z lies in their span, omit a row having nonzero coefficient in its expansion.
This also covers d=1 by the empty wedge convention.
At least one d by d column minor of these d selected rows is nonzero.
Its square is an additional positive term in C(E'), distinct from the terms using only B.
Hence

    E'!=E_0  =>  C(E')>J/G.                             (3)

In particular,

    min_(VE'=F, E' real) C(E')=J/G,
    max_(VE'=F, E' real) J/C(E')=G.                     (4)

If V and F are rational, E_0 is rational, so the same minima and maxima hold over rational lifts.
Thus relaxing the coefficient representatives to rational ones cancels the entire arithmetic numerator exactly.
It does not create a new entropy estimate.

<a id="polynomial-relation-lifts"></a>
## The companion relation lattice and integral boundary

For a monic polynomial p of degree d and N>=d, take V=V_N with columns t^j mod p, 0<=j<N, in the power basis.
Its first d columns are the identity.
The relation matrix K consists of the coefficient columns

    p,tp,...,t^(N-d-1)p.

The exact L G0004 interface is

    ker_Z(V)=K Z^(N-d),       det(K^T K)=G_N.

The same columns span the real and rational kernels.
Thus every real, rational or integral lift of the original F=VE is respectively

    E+K H

with H over the same scalar domain.
In polynomial language, these are precisely the modifications of the coefficient columns by multiples of p within the fixed degree window.
Moreover

    E_0=Pi E=E-K(K^T K)^(-1)K^T E.                      (5)

The cost-minimizing operation is therefore projection along the actual polynomial relation space, rather than an unrelated matrix relaxation.

If V,F are integral, W and its adjugate are integral and

    E_0=(1/G_N)V^T adj(W)F.

Projection denominators divide G_N.
They need not disappear: a rational representative of minimal cost is not automatically an admissible integral representative.
Integral lifts exist because the original E is one.
Their costs are positive integers, so the minimum integral cost exists.
By the strictness proof,

    min_(VE'=F, E' integral) C(E')=J/G_N
       if and only if E_0 is integral.                  (6)

If E_0 is not integral, every integral lift has strictly larger cost and the minimum is at least floor(J/G_N)+1.
This is the remaining discrete optimization boundary, not a proof of a positive entropy gap.

There are two useful exact endpoints.
Reducing each column to its degree-less-than-d remainder gives the integral lift

    E_rem=[F;0],       C(E_rem)=J,

so its ratio J/C is exactly one: the joint arithmetic determinant cancels completely in this particular short representative.
Alternatively, multiplying F by G_N clears the denominators of E_0.
For the scaled numerator G_N F, the integral lift G_N E_0 then has ratio exactly G_N.
The numerator and cost both scale by G_N^(2d), so clearing denominators still recovers only the old Gram quantity.

<a id="joint-prime-gram-ceiling"></a>
## Consequence for the proposed two-prime certificate

In L G0054 take N=4d and

    E=[E_2 E_3],       F=[p(A^2) p(A^3)].

Both arithmetic maps are nonsingular by the retained Frobenius argument, so the hypotheses above hold.
The actual E has column rank 2d.
Indeed a relation among its columns is a polynomial identity

    p(t^2)u(t)+p(t^3)v(t)=0,       deg u,deg v<d.

If v is nonzero, its summand has degree at least 3d, whereas the first summand has degree at most 3d-1, which is impossible.
Thus v=0 and then u=0.
Since Pi E has rank d, E differs from Pi E.
The strict minimum result therefore gives

    J/C(E)<G_(4d).                                      (7)

No degree-uniform size of this strict loss follows merely from the rank argument.

Let Delta=|disc p|.
The proposed finite entropy lower bound is exactly

    [log Delta+log J-log C(E)-d log N]/[2(N-1)]
      = [log(Delta G_N)-d log N]/[2(N-1)]
           + log eta(E)/[2(N-1)].                       (8)

The first term is the already proved direct Gram certificate of L G0004.
The second is nonpositive, and is strictly negative for the displayed two-prime coefficient matrix.
Thus evaluating the complete arithmetic maps and their full coefficient cost cannot improve that direct certificate pointwise at the same N.
Optimizing arbitrary rational coefficient lifts attains equality with the old certificate; using integral lifts can leave an additional loss.

This projection identity alone does not refute the arithmetic target proposed in L G0054.
The separate [exact control in L G0055](Yin_L_G0055_v1.md#lehmer-joint-prime-control) does refute that universal two-prime target on its stated domain, even after optimizing the entire two-prime coefficient space.
Another arithmetic estimate on the original G_N, or a justified change of maps or domain, could still establish a uniform positive Gram surplus.
The result identifies the obligation: arithmetic has to prove that surplus while controlling the projection loss.
It cannot obtain an additional independent prime surplus simply by normalizing the row space or by treating the projected cost as independent of the numerator.
The exact identities hold for any finite collection of full-rank coefficient maps at the fixed window, not only primes two and three; this generality does not supply the missing arithmetic bound or reopen the refuted fixed-space target.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0018_v1.md#actual-review-and-scope), with its original inspected scopes, author self-check and the two genuinely unknown separate/coordinator initial arrangements.
